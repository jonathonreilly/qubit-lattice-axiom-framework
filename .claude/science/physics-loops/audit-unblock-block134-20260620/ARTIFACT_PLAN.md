# Artifact Plan

## Source Change

- Make the three runner-path canonicalizers return `""` for `None`.
- Extend the canonicalization guard and precompute unit tests for the null
  path case.

## Generated Refresh

- Run precompute for:
  - `scripts/audit_runner_path_canonicalization_guard_2026_06_17.py`
  - `scripts/audit_packet_script_deps.py`
- Commit refreshed:
  - `docs/audit/data/audit_packet_script_deps.json`
  - `logs/runner-cache/audit_packet_script_deps.txt`
  - `logs/runner-cache/audit_runner_path_canonicalization_guard_2026_06_17.txt`

## Verification

- Canonicalization guard.
- Packet-deps runner summary.
- Focused and full unit tests.
- PR-scoped runner-cache freshness check.
- Strict audit lint.
- Python compile check.
- `git diff --check`.
