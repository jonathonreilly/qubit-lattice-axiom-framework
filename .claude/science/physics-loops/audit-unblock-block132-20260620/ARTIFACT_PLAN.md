# Artifact Plan

## Cleanup

- Run `precompute_audit_runners.py --cleanup-orphans --all --check-only --allow-non-main`.
- Commit only the 8 deleted cache files plus this loop pack.

## Verification

- Post-cleanup dry run must report 0 orphan cache files.
- Full-ledger runner-cache check must remain `fresh=3123`, `stale=0`,
  `missing=0`.
- Full audit pipeline unit suite.
- Strict audit lint.
- Python compile check.
- `git diff --check`.
