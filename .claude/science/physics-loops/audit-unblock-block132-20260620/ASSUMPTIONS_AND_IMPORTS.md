# Assumptions And Imports

## Repo Inputs

- Block130 preserves caches with live header runner paths.
- Block131 preserves caches linked from repo text outside `logs/runner-cache/`.
- The block132 deletion set is the output of
  `python3 scripts/precompute_audit_runners.py --cleanup-orphans-dry-run --all --check-only --allow-non-main`
  after those guards.

## Imports Avoided

- No claim truth, audit verdict, or retained status is imported.
- No ledger row is hand-edited.
- No note link is removed or rewritten.

## Open Imports

- The historical reason the deleted cache files existed is not adjudicated in
  this PR. The only claim is that the current cleanup tool classifies them as
  unreferenced runner orphans.
