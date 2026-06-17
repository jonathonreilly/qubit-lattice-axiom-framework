# Handoff

## What moved

- `scripts/codex_audit_runner.py` now canonicalizes row runner paths before
  runner source is read and before `{{RUNNER_PATH}}` is rendered.
- `scripts/audit_packet_script_deps.py` now applies the same canonicalization
  before deciding a row's runner is missing.
- `scripts/audit_runner_path_canonicalization_guard_2026_06_17.py` checks the
  current `missing_runner_file` inventory and the prompt-rendering path.

## Audit Boundary

No audit verdicts, ledgers, queues, or generated audit-result files were edited.
This branch is intended to make later audit-loop packet construction see the
checked-in runner files already present under `scripts/`.

## Review

reviewer_owned_not_run. The Codex reviewer owns landing and any main freshness.

## Checks

- `python3 scripts/audit_runner_path_canonicalization_guard_2026_06_17.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/audit_runner_path_canonicalization_guard_2026_06_17.py`
- `python3 -m py_compile scripts/codex_audit_runner.py scripts/audit_packet_script_deps.py scripts/audit_runner_path_canonicalization_guard_2026_06_17.py`
- `git diff --check`
- `git diff --name-only -- docs/audit docs/publication/ci3_z3 docs/repo/FRONT_DOOR_STATUS.md` (empty)
