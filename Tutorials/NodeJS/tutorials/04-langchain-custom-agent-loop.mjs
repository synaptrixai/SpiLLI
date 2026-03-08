import {
  createSpilliService,
  parseHarmonyOutput,
  renderHarmonyForDisplay
} from '@synaptrix/spilli';
import { buildResource, getRuntimeConfig } from './common.mjs';

const config = getRuntimeConfig();
const service = createSpilliService(config.keyPath);
const session = service.getOrCreateSession(buildResource(config));

function buildTranscript(history) {
  return history
    .map((m, i) => `[${i}] ${m.role.toUpperCase()}:\n${m.content}`)
    .join('\n\n');
}

function extractToolCalls(raw) {
  const parsed = parseHarmonyOutput(raw);
  if (!parsed.isHarmony) {
    return [];
  }

  const calls = [];
  for (const segment of parsed.messages) {
    const hasRecipient = typeof segment.recipient === 'string' && segment.recipient.trim().length > 0;
    const looksLikeToolCall = segment.terminator === 'call' || (segment.terminator === 'end' && hasRecipient);
    if (!looksLikeToolCall) {
      continue;
    }

    try {
      const json = JSON.parse(segment.content);
      if (!json || typeof json !== 'object') {
        continue;
      }
      const record = json;
      const toolName =
        typeof record.toolName === 'string' && record.toolName.trim().length > 0
          ? record.toolName
          : segment.recipient;
      if (!toolName) {
        continue;
      }

      calls.push({
        toolName,
        callId:
          typeof record.callId === 'string' && record.callId.trim().length > 0
            ? record.callId
            : `${Date.now()}-${Math.random().toString(36).slice(2)}`,
        args: record.args && typeof record.args === 'object' ? record.args : record
      });
    } catch {
      // Ignore invalid tool-call payloads.
    }
  }

  return calls;
}

const tools = {
  'util.getCurrentTime': async () => {
    return {
      iso: new Date().toISOString(),
      locale: new Date().toString()
    };
  },
  'math.add': async args => {
    const a = Number(args.a ?? 0);
    const b = Number(args.b ?? 0);
    return { a, b, sum: a + b };
  }
};

async function executeTool(call) {
  const handler = tools[call.toolName];
  if (!handler) {
    return {
      callId: call.callId,
      toolName: call.toolName,
      ok: false,
      error: `Tool not allowlisted: ${call.toolName}`
    };
  }

  try {
    const result = await handler(call.args || {});
    return {
      callId: call.callId,
      toolName: call.toolName,
      ok: true,
      result
    };
  } catch (error) {
    return {
      callId: call.callId,
      toolName: call.toolName,
      ok: false,
      error: error instanceof Error ? error.message : String(error)
    };
  }
}

const systemPrompt = [
  'You are a Node.js agent tutor operating in a tool loop.',
  'If a tool would improve accuracy, emit Harmony tool calls as JSON with toolName/callId/args.',
  'Available tools: util.getCurrentTime, math.add.'
].join('\n');

const history = [
  {
    role: 'human',
    content:
      'What time is it now, and what is 21 + 34? Use tools if needed, then provide a short final answer.'
  }
];

const maxIterations = 5;
let finalAnswer = '';

console.log('\n=== Tutorial 04: Custom agent loop ===');
console.log(
  `model=${config.model} scope=${config.scope}${config.team ? ` team=${config.team}` : ''}`
);

for (let iteration = 1; iteration <= maxIterations; iteration += 1) {
  const query = buildTranscript(history);
  const raw = await session.run({ prompt: systemPrompt, query });
  const rendered = renderHarmonyForDisplay(raw);
  const toolCalls = extractToolCalls(raw);

  console.log(`\n=== Iteration ${iteration} ===`);
  console.log(rendered.display || raw);

  if (toolCalls.length === 0) {
    finalAnswer = rendered.display || raw;
    break;
  }

  for (const call of toolCalls) {
    const result = await executeTool(call);
    history.push({
      role: 'ai',
      content: `Tool result:\n${JSON.stringify(result)}`
    });
  }
}

if (!finalAnswer) {
  console.log('\nLoop ended at max iterations; review prompts/tools for convergence.');
} else {
  console.log('\n=== Tutorial 04: Final answer ===');
  console.log(finalAnswer);
}
