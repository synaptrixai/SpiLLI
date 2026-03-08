# Tutorials: `@synaptrix/spilli` + LangChain

These examples are designed for Node.js 20+ and JavaScript ESM.

## How to read this folder

Read these files like a progressive architecture walkthrough, not isolated scripts:

- `common.mjs` is your runtime boundary: env config, key validation, model resource selection.
- Tutorials `01` -> `04` add one capability at a time without changing the core setup pattern.
- This mirrors real app growth: first a working call, then streaming UX, then orchestration, then agent loops.

In all cases, your application code remains in charge of behavior. Spilli provides the runtime model access layer into decentralized inference resources based on the selected scope.

## Files

- `COMMON_SETUP_EXPLAINED.md`
  - Teaches: beginner-friendly internal walkthrough of how `common.mjs` configures Spilli from scratch.
- `01-basic-spilli-call.mjs`
  - Teaches: minimal service/session setup and one call.
  - Output: one full model response.
- `02-streaming-response.mjs`
  - Teaches: `onChunk` streaming and completion summary.
  - Output: streamed text plus chunk count.
- `03-langchain-lightweight.mjs`
  - Teaches: using `@langchain/core` messages/tools with direct Spilli request execution.
  - Output: tool result + concise assistant recommendation.
- `04-langchain-custom-agent-loop.mjs`
  - Teaches: iterative loop, Harmony tool-call extraction, local tool execution, and follow-up turns.
  - Output: per-iteration logs and final response (or max-iteration warning).

## Setup

```bash
npm install
cp .env.example .env
```

Set `SPILLI_KEY_PATH` in `.env`.

If you are new to this flow, read `COMMON_SETUP_EXPLAINED.md` first.

## Run

```bash
npm run tut:01
npm run tut:02
npm run tut:03
npm run tut:04
```

## Expected behavior

- `tut:01` and `tut:02` should work for any valid model/scope access.
- `tut:03` may return plain text or Harmony text depending on model behavior.
- `tut:04` depends on model emitting Harmony tool-call segments; if not, it still prints model output but may skip tool execution.

## When to use which pattern

- Use `01` for connectivity and auth smoke tests.
- Use `02` for chat UI or CLI streaming UX.
- Use `03` for simple app orchestration with LangChain structures.
- Use `04` for controlled tool loops in agent-style systems.
