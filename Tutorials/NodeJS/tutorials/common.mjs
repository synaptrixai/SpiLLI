import fs from 'node:fs';
import path from 'node:path';

export function getRuntimeConfig() {
  // 1) Read env config.
  const keyPath = process.env.SPILLI_KEY_PATH;
  if (!keyPath) {
    throw new Error('Missing SPILLI_KEY_PATH. Set it in .env (see .env.example).');
  }

  // 2) Resolve and validate key path before touching native runtime.
  const absoluteKeyPath = path.resolve(keyPath);
  if (!fs.existsSync(absoluteKeyPath)) {
    throw new Error(
      `SPILLI_KEY_PATH does not exist: ${absoluteKeyPath}. Update .env with a valid .pem path.`
    );
  }

  const stat = fs.statSync(absoluteKeyPath);
  if (!stat.isFile()) {
    throw new Error(`SPILLI_KEY_PATH must point to a file: ${absoluteKeyPath}`);
  }

  if (!absoluteKeyPath.toLowerCase().endsWith('.pem')) {
    throw new Error(`SPILLI_KEY_PATH must point to a .pem file: ${absoluteKeyPath}`);
  }

  const model = process.env.SPILLI_MODEL || 'gpt-oss-20b';
  const scope = process.env.SPILLI_SCOPE || 'public';
  const team = process.env.SPILLI_TEAM;

  // 3) Return a normalized runtime config object.
  return {
    keyPath: absoluteKeyPath,
    model,
    scope,
    team
  };
}

export function buildResource(config) {
  // Team is only included when scope=team and team name is present.
  return {
    model: config.model,
    scope: config.scope,
    ...(config.scope === 'team' && config.team ? { team: config.team } : {})
  };
}
