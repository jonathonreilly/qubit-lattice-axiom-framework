# Artifact Plan

## Source Artifacts

- `docs/ONE_PARAMETER_REDUCED_SHELL_LAW_HELPERS_UMBRELLA_NOTE_2026-04-13.md`
  - Clarifies that generated queue snapshots are not source-claim citations
    for the helper-wrapper firewall.
- `scripts/frontier_one_parameter_reduced_shell_law.py`
  - Skips `docs/repo/FRONT_DOOR_STATUS.md` when scanning direct source
    citations for umbrella misuse.

## Verification Artifacts

- `logs/runner-cache/frontier_one_parameter_reduced_shell_law.txt`
  - Refreshed by `precompute_audit_runners.py`.

## Excluded Generated Artifacts

After the current-main rebase, generated audit ledger/queue/data,
publication effective-status views, packet-dependency outputs, and
`docs/repo/FRONT_DOOR_STATUS.md` are excluded from this PR.
