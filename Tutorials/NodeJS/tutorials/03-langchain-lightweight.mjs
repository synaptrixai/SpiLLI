import { HumanMessage, SystemMessage } from '@langchain/core/messages';
import { DynamicStructuredTool } from '@langchain/core/tools';
import { z } from 'zod';
import { createSpilliService, renderHarmonyForDisplay } from '@synaptrix/spilli';
import { buildResource, getRuntimeConfig } from './common.mjs';

const config = getRuntimeConfig();

const service = createSpilliService(config.keyPath);
const session = service.getOrCreateSession(buildResource(config));

const estimateStoryPoints = new DynamicStructuredTool({
  name: 'estimate_story_points',
  description: 'Estimate story points from complexity and uncertainty.',
  schema: z.object({
    complexity: z.number().min(1).max(10),
    uncertainty: z.number().min(1).max(10)
  }),
  func: async ({ complexity, uncertainty }) => {
    const value = Math.round((complexity * 0.7 + uncertainty * 0.6) / 1.3 * 8) / 2;
    return JSON.stringify({ storyPoints: Math.max(1, value) });
  }
});

const toolInput = { complexity: 7, uncertainty: 6 };
const toolResult = await estimateStoryPoints.invoke(toolInput);

const messages = [
  new SystemMessage(
    'You are an engineering planning assistant. Keep answers concise and actionable.'
  ),
  new HumanMessage(
    [
      'Using this tool output, provide a short sprint recommendation:',
      toolResult,
      'Include: risk level, sprint-fit, and one mitigation.'
    ].join('\n')
  )
];

const query = messages
  .map((msg, i) => `[${i}] ${msg._getType().toUpperCase()}:\n${String(msg.content)}`)
  .join('\n\n');

const raw = await session.run({
  prompt: 'Use the provided tool output and return a compact recommendation.',
  query
});

const rendered = renderHarmonyForDisplay(raw);

console.log('\n=== Tutorial 03: LangChain lightweight ===');
console.log(
  `model=${config.model} scope=${config.scope}${config.team ? ` team=${config.team}` : ''}`
);
console.log('\nTool output:', toolResult);
console.log('\nResponse:');
console.log(rendered.display || raw);
