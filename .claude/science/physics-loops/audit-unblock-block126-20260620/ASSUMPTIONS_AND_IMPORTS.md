# Assumptions And Imports

## Operating Assumptions

- The user asked for source-side audit unblocking only: make PRs, do not audit, and do not
  push directly to `main`.
- The branch starts from `origin/main` at `cd9cf25180e17c46706a73341144ee1b71a1c7d2`.
- The automation lock is unavailable in this environment because `scripts/automation_lock.py`
  fails on `/Users/jonreilly`; block126 uses an isolated worktree and branch-local discipline.
- The cache refresh is generated from the current runner, not hand-authored evidence.
- The audit/publication surface changes in this PR are deterministic outputs of
  `docs/audit/scripts/run_pipeline.sh` and `scripts/audit_packet_script_deps.py`.

## Imports Not Retired

- `neutrino_dirac_z3_support_trichotomy_note`
- `dm_neutrino_dirac_bridge_theorem_note_2026-04-15`

Those dependencies remain outside this PR. This block does not claim that either dependency is
retained, audited, ready, or otherwise closed.

## Forbidden Imports

- No audit verdicts are imported or hand-applied.
- No observed physics values are used as proof inputs by this branch-local packet.
- No literature theorem, convention, or external value is imported in this block.
- Queue, ledger, publication effective-status, and front-door status updates are included only
  as generated pipeline output required for strict-lint cleanliness.
