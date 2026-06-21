# Opportunity Queue

1. `runner_breakage_inventory` missing-runner evidence guard
   - Selected for block129.
   - Independent of cache refresh PR #4498 at the source-code level.
   - Stacked on #4498 only to avoid duplicating generated strict-lint surfaces.

2. Sidecar dispatch queue stale warnings
   - Already cleared by the full pipeline regeneration carried in #4498.
   - Do not duplicate unless #4498 is rejected.

3. Audit packet dependency helper completeness
   - Null-runner regression and helper-cache refresh covered by #4497.
   - Revisit only for a distinct helper-source omission.

4. Full-ledger stale cache freshness
   - Covered by #4498 for the 13 stale/corrupt caches visible on current main.
