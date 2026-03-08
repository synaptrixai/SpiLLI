import { createSpilliService } from '@synaptrix/spilli';
import { buildResource, getRuntimeConfig } from './common.mjs';

const config = getRuntimeConfig();

const service = createSpilliService(config.keyPath);
const session = service.getOrCreateSession(buildResource(config));

const prompt = [
  'You are a coding tutor.',
  'Respond in markdown with short sections.'
].join('\n');

const query = [
  'Create a 5-step plan for adding an AI assistant to an existing Node.js REST API.',
  'Keep each step to one sentence.'
].join(' ');

let chunkCount = 0;
console.log('\n=== Tutorial 02: Streaming response ===');
console.log(
  `model=${config.model} scope=${config.scope}${config.team ? ` team=${config.team}` : ''}`
);
console.log('\n--- streamed output ---\n');

const finalRaw = await session.run(
  { prompt, query },
  {
    onChunk: chunk => {
      chunkCount += 1;
      process.stdout.write(chunk);
    }
  }
);

console.log('\n\n--- stream complete ---');
console.log(`chunks=${chunkCount} finalLength=${finalRaw.length}`);
