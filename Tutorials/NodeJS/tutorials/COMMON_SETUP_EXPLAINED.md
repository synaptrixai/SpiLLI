# How `common.mjs` Sets Up Spilli (Beginner Guide)

This file explains the shared setup used by all tutorials.

- Source file: `common.mjs`
- Purpose: validate config once, then reuse it in every tutorial

## First, the mental model

`common.mjs` is intentionally small because it defines a clean boundary:

- Above this boundary: your app logic (routes, chat UX, tool execution, memory, business rules).
- At this boundary: runtime config (key path, model, scope, optional team).
- Below this boundary: Spilli service/session that connects to decentralized inference resources.

This separation helps beginners avoid mixing transport/runtime concerns with agent behavior.

## Why this shared module exists

Without a shared setup file, each tutorial would duplicate:

- env variable parsing
- key path validation
- model/scope defaults
- request resource shaping

`common.mjs` keeps that logic in one place and makes beginner errors easier to debug.

## Step-by-step flow

### Step 1: Read required/optional environment values

`getRuntimeConfig()` reads:

- `SPILLI_KEY_PATH` (required)
- `SPILLI_MODEL` (optional, defaults to `gpt-oss-20b`)
- `SPILLI_SCOPE` (optional, defaults to `public`)
- `SPILLI_TEAM` (optional, used only for `team` scope)

### Step 2: Normalize and validate key file path

Before creating any Spilli service/session, `getRuntimeConfig()` checks that:

- path exists
- path is a file (not a folder)
- file ends with `.pem`

This avoids native runtime crashes and gives a clean, actionable error.

### Step 3: Return normalized config object

`getRuntimeConfig()` returns:

```js
{
  keyPath: '/absolute/path/to/key.pem',
  model: 'gpt-oss-20b',
  scope: 'public',
  team: undefined
}
```

Every tutorial uses this same shape.

### Step 4: Build model resource payload

`buildResource(config)` converts config into the object expected by:

- `service.getOrCreateSession({ model, scope, team? })`

`team` is only included when:

- `scope === 'team'`
- `SPILLI_TEAM` is provided

## How this connects to Spilli runtime

In each tutorial, the setup pipeline is:

1. `const config = getRuntimeConfig()`
2. `const service = createSpilliService(config.keyPath)`
3. `const session = service.getOrCreateSession(buildResource(config))`
4. `await session.run({ prompt, query }, { onChunk? })`

This is the minimum production-friendly setup pattern for Node.js apps.

What this means in practice:

- `createSpilliService(...)` gives your app a reusable runtime client.
- `getOrCreateSession(...)` binds that client to a model+scope resource target.
- `run(...)` performs inference for a specific turn (single-shot or loop-driven).

## Minimal copy-paste template

```js
import { createSpilliService } from '@synaptrix/spilli';
import { getRuntimeConfig, buildResource } from './common.mjs';

const config = getRuntimeConfig();
const service = createSpilliService(config.keyPath);
const session = service.getOrCreateSession(buildResource(config));

const raw = await session.run({
  prompt: 'You are a concise assistant.',
  query: 'Hello from Node.js'
});

console.log(raw);
```

## Beginner tips

- Start with `scope=public` first.
- Keep `SPILLI_KEY_PATH` absolute to avoid path confusion.
- If you switch to team scope, set both `SPILLI_SCOPE=team` and `SPILLI_TEAM=<name>`.
