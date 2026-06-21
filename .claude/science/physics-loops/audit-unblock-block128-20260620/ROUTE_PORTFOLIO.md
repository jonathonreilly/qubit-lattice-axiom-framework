# Route Portfolio

| route | status | reason |
|---|---|---|
| Refresh exactly the current stale/corrupt full-ledger caches | selected | Directly removes runner-cache freshness blockers without audit verdict work. |
| Regenerate audit pipeline surfaces | deferred | Handled by separate source-graph PRs; this PR stays cache-only. |
| Run audits or apply verdicts | rejected | User constraint: PR unblockers only, no audits. |
