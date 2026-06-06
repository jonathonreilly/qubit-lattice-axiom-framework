# Opportunity Queue

1. `second_grown_family_note`
   - Status: executed in this branch.
   - Reason: missing runner path has a direct repair using current evidence
     packets.

2. `distance_law_note`
   - Status: harder remaining blocker.
   - Reason: exploratory timeout increase did not complete quickly; likely
     needs algorithmic or sampling repair rather than a simple cache refresh.

3. Gauge first-sector rows
   - Status: already packaged in a separate PR.
   - Reason: missing runners/caches were independently repaired.

4. Timeout-cache rows
   - Status: already packaged in a separate PR.
   - Reason: two runners completed under an explicit 600 second budget.
