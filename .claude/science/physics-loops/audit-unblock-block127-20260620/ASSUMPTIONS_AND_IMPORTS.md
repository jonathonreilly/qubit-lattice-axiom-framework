# Assumptions And Imports

## Operating Assumptions

- The user asked for source-side audit unblocking only: make PRs, do not audit, and do not
  push directly to `main`.
- The branch starts from `origin/main` at `618f3debbb3d88f76eac27714026b8ed5b1ebe30`.
- The automation lock is unavailable in this environment because `scripts/automation_lock.py`
  fails on `/Users/jonreilly`; block127 uses an isolated worktree and branch-local discipline.
- The frozen-stars cache refresh is generated from the current runner, not hand-authored
  evidence.
- The audit/publication surface changes in this PR are deterministic outputs of
  `docs/audit/scripts/run_pipeline.sh` and `scripts/audit_packet_script_deps.py`.

## Imports Not Retired

- `gw_echo_null_result_note`
- `work_history.gw_echo_timing_route_note`

Those dependencies remain outside this PR. This block does not claim that either dependency is
retained, audited, ready, or otherwise closed.

## Forbidden Imports

- No audit verdicts are imported or hand-applied.
- No observed physics values are used as proof inputs by this branch-local packet.
- No new literature theorem, convention, or external value is imported in this block.
- Queue, ledger, publication effective-status, and front-door status updates are included only
  as generated pipeline output required for strict-lint cleanliness.
