import { createSpilliService } from '@synaptrix/spilli';
import { buildResource, getRuntimeConfig } from './common.mjs';

const config = getRuntimeConfig();

const service = createSpilliService(config.keyPath);
const session = service.getOrCreateSession(buildResource(config));

const prompt = [
  'You are a concise assistant for Node.js app developers.',
  'Return a short answer and one practical next step.'
].join('\n');

const query = 'Explain in plain terms what an AI agent loop is in a Node.js application.';

const raw = await session.run({ prompt, query });

console.log('\n=== Tutorial 01: Basic call ===');
console.log(
  `model=${config.model} scope=${config.scope}${config.team ? ` team=${config.team}` : ''}`
);
console.log(raw);
