# Assumptions And Imports

## Operating Assumptions

- The user asked for source-side audit unblocking only: make PRs, do not audit, and do not
  push directly to `main`.
- The branch is rebased onto `origin/main` at `678b38ce7d8f9c092a7e19bf8272847f03bd799f`.
- The automation lock is unavailable in this environment because `scripts/automation_lock.py`
  fails on `/Users/jonreilly`; block127 uses an isolated worktree and branch-local discipline.
- The frozen-stars cache refresh is generated from the current runner, not hand-authored
  evidence.
- Generated audit/publication surface changes are intentionally excluded after the current-main
  rebase.

## Imports Not Retired

- `gw_echo_null_result_note`
- `work_history.gw_echo_timing_route_note`

Those dependencies remain outside this PR. This block does not claim that either dependency is
retained, audited, ready, or otherwise closed.

## Forbidden Imports

- No audit verdicts are imported or hand-applied.
- No observed physics values are used as proof inputs by this branch-local packet.
- No new literature theorem, convention, or external value is imported in this block.
- Queue, ledger, publication effective-status, and front-door status updates are excluded from
  this narrowed PR.
