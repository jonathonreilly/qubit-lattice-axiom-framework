# Artifact Plan

## Source Change

- Add repository reference scanning helpers to
  `scripts/precompute_audit_runners.py`.
- Preserve cache files found in references outside `logs/runner-cache/`.

## Regression Test

- Add a temp-repo fixture with one referenced missing-runner cache and one
  unreferenced missing-runner cache.
- Verify dry-run and real cleanup preserve the referenced cache and only
  report/delete the unreferenced one.

## Verification

- Focused precompute cleanup test class.
- Full-ledger cleanup dry run.
- Full audit pipeline unit suite.
- Strict audit lint.
- Python compile check.
- `git diff --check`.
