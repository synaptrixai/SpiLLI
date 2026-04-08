#!/usr/bin/env bash
set -euo pipefail

# SpiLLIHost resolves PEM from current working directory in container runtime.
cd /usr/bin/SpiLLIHost

binary_candidates=(
  "/usr/bin/SpiLLIHost/SpiLLIHost"
  "/usr/bin/SpiLLIHost"
  "/usr/local/bin/SpiLLIHost"
)

selected_binary=""
if [[ -n "${SPILLIHOST_BINARY:-}" ]]; then
  selected_binary="${SPILLIHOST_BINARY}"
fi

for candidate in "${binary_candidates[@]}"; do
  if [[ -z "$selected_binary" && -x "$candidate" ]]; then
    selected_binary="$candidate"
  fi
done

if [[ -z "$selected_binary" ]] && command -v SpiLLIHost >/dev/null 2>&1; then
  selected_binary="$(command -v SpiLLIHost)"
fi

if [[ -n "$selected_binary" ]]; then
  child_pid=""

  forward_signal() {
    local signal="$1"
    if [[ -n "$child_pid" ]] && kill -0 "$child_pid" 2>/dev/null; then
      kill "-${signal}" "$child_pid" 2>/dev/null || true
    fi
  }

  trap 'forward_signal TERM' TERM
  trap 'forward_signal INT' INT

  "$selected_binary" "$@" &
  child_pid="$!"
  wait "$child_pid"
  exit_code="$?"

  trap - TERM INT
  exit "$exit_code"
fi

echo "Could not locate SpiLLIHost runtime binary in container image." >&2
ls -la /usr/bin || true
ls -la /usr/bin/SpiLLIHost || true
exit 1
