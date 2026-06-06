# Opportunity Queue

1. Post-record closeout cache chain
   - Directly addresses latest failed cache-summary blockers.
   - Status in this branch: repaired and ready for review/audit.

2. Remaining conditional rows from the current ledger
   - Need fresh scan after this PR is opened to avoid duplicating already-open repair PRs.

3. Hard physical-bridge rows
   - Examples include path/channel weight selectors, gravitational-wave physical bridge, and source-unit bridge claims.
   - These require new framework-native derivations, not cache hygiene.
