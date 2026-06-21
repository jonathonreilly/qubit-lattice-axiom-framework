# Artifact Plan

## Source Change

- Update `canonical_runner_path()` in:
  - `scripts/codex_audit_runner.py`
  - `scripts/audit_packet_script_deps.py`
  - `scripts/precompute_audit_runners.py`
- Extend `scripts/audit_runner_path_canonicalization_guard_2026_06_17.py`
  to cover nested absolute paths and precompute's canonicalizer.
- Refresh the guard cache transcript.

## Regression Test

- Add a unit fixture proving precompute maps an absolute
  `/tmp/.../scripts/corrections/valid_nested.py` path to
  `scripts/corrections/valid_nested.py`.

## Verification

- Canonicalization guard.
- Focused unit test class.
- Full audit pipeline unit suite.
- PR-scoped runner-cache freshness check.
- Strict audit lint.
- Python compile check.
- `git diff --check`.
