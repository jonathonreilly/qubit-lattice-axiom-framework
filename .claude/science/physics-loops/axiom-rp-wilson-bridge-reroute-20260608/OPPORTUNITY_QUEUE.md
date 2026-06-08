# Opportunity Queue

1. Open this PR for review-loop extraction.
2. Re-scan `audited_conditional` rows for source-gated repairs that can be
   moved from unaudited dependencies to audited-clean dependencies already on
   `main`.
3. Prefer longer dependency-chain closures when no new axiom is needed.
