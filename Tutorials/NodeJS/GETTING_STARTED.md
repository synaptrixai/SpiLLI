# Getting Started with `@synaptrix/spilli` for Node.js AI Agents

This kit helps Node.js developers build AI agent workflows with the `@synaptrix/spilli` package and LangChain-style patterns.

All example files are in `docs-kit/tutorials/` so you can copy this folder directly into another repository.

## The big picture

`@synaptrix/spilli` is the runtime bridge between your Node.js app and AI inference on the SpiLLI network.

- Your app owns control flow, prompts, tools, and business logic.
- Spilli handles model session connectivity and inference requests at runtime.
- `scope` controls which resource pool (node set) your request is routed through:
  - `public`: broad shared access
  - `private`: restricted tenant access
  - `team`: team-scoped resources (with `team` name)

Think of it this way: your code is still the agent brain, and Spilli is the transport/runtime layer that sends work to the right decentralized inference resources.

## Prerequisites

- Node.js 20+
- npm 10+
- A valid SpiLLI `.pem` key file
- Network access for model calls

## 1) Copy the starter kit

Copy `docs-kit/` into your public repository.

## 2) Install tutorial dependencies

From your target repository:

```bash
cd docs-kit/tutorials
npm install
```

## 3) Configure environment

Create your env file from the template:

```bash
cp .env.example .env
```

Set at least:

- `SPILLI_KEY_PATH`: absolute path to your SpiLLI `.pem` key file

Optional runtime vars used by scripts:

- `SPILLI_MODEL` (default in scripts: `gpt-oss-20b`)
- `SPILLI_SCOPE` (default in scripts: `public`)
- `SPILLI_TEAM` (only if scope is `team`)

## 4) Run the tutorials

```bash
npm run tut:01
npm run tut:02
npm run tut:03
npm run tut:04
```

Before running tutorials, read `docs-kit/tutorials/COMMON_SETUP_EXPLAINED.md` for a beginner walkthrough of how shared setup works in `common.mjs`.

## What you should understand while walking through

- `01` shows the minimum viable shape: config -> service -> session -> `run()`.
- `02` keeps the same structure, but introduces streaming so you can design responsive UI/CLI output.
- `03` shows where LangChain primitives fit: message shaping and tool definitions in app code, with Spilli still executing inference.
- `04` shows full agent-loop control: parse tool calls, execute local tools, feed results back, repeat until final answer.

## Public SDK interface covered

These examples focus on the core APIs:

- `createSpilliService(keyPath, options?)`
- `service.getOrCreateSession({ model, scope, team? })`
- `session.run({ prompt, query }, { onChunk? })`
- `parseHarmonyOutput(raw)` (advanced)
- `renderHarmonyForDisplay(raw)` (advanced)

## Tutorial progression

- `01-basic-spilli-call.mjs`: single request/response
- `02-streaming-response.mjs`: chunk streaming output
- `03-langchain-lightweight.mjs`: LangChain messages/tools + direct call
- `04-langchain-custom-agent-loop.mjs`: iterative tool loop with Harmony tool-call parsing

## How to copy into your app

1. Start with `01` to validate key path and model access.
2. Move to `02` if you need streaming UX.
3. Use `03` for simple app-level orchestration with `@langchain/core` structures.
4. Use `04` only when you need iterative tool execution and loop control.

For production apps, extract shared config into one module (model, scope, session creation, logging, retry behavior).

## Troubleshooting

- `SPILLI_KEY_MISSING`:
  - Confirm `SPILLI_KEY_PATH` is correct and points to a readable `.pem` file.
- `Request failed` / auth errors:
  - Verify account access for selected model/scope.
  - Re-check network and backend reachability.
- No streaming chunks in tutorial 02:
  - Some responses may arrive quickly as a single chunk.
- Team scope failures:
  - Set `SPILLI_SCOPE=team` and provide `SPILLI_TEAM`.

## Notes for public repo maintainers

- Keep this folder isolated so users can copy it without extension-specific code.
- Update model defaults if your published account exposes a different baseline model.
- Add CI smoke checks that run tutorials against a mocked service if you need deterministic tests.
