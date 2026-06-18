# Opportunity Queue

1. Assumption-derivation ledger meta-runner registration.
   - Critical row, high load, no runner path in current ledger data.
   - Implemented in this branch.

2. Remaining high-load conditionals.
   - Mostly covered by open repair PRs; do not spend this block refreshing
     those branches against main.

3. Theorem-grade ingredient wiring for the assumption ledger.
   - Valuable but larger than runner registration and should be split into
     per-ingredient authority PRs.
