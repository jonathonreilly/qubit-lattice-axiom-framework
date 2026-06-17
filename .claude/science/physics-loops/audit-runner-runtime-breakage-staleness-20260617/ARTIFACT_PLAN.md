# Artifact Plan

- Add `scripts/audit_runner_runtime_breakage_staleness_guard_2026_06_17.py`.
- Run it directly to prove the live source/cache state.
- Cache it with `scripts/cached_runner_output.py` so the auditor can inspect a
  SHA-pinned transcript.
- Run Python compile, cache check, diff hygiene, and controlled-path guards.
