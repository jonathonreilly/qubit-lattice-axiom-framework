# Opportunity Queue

1. `runner_breakage_inventory` missing-runner evidence guard
   - Selected for block129.
   - Rebased directly on `main` at `ca3f6f8d3`; independent of PR #4498.

2. Sidecar dispatch queue stale warnings
   - Still avoid duplicating broad generated strict-lint surfaces unless a
     source-side blocker requires them.

3. Audit packet dependency helper completeness
   - Null-runner regression and helper-cache refresh covered by #4497.
   - Revisit only for a distinct helper-source omission.

4. Full-ledger stale cache freshness
   - Covered by #4498 for the current stale/corrupt cache batch on
     `ca3f6f8d3`; re-scan before opening more cache-only work because main
     can move again.
