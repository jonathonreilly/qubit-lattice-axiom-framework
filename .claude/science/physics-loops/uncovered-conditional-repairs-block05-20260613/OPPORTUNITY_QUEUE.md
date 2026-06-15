# Opportunity Queue

This branch is a packaging checkpoint, not the end of the audit-unlock campaign.

## Next Candidates After PR #3825 Refresh

1. `FS_FORCED_MODULO_EMERGENT_LORENTZ_STRESS_TEST_NOTE_2026-06-06`
   - No open PR was found in the last scan.
   - Likely needs direct source-side repair or demotion packet.

2. Existing open conditional-repair PRs
   - Recheck mergeability and runner freshness after #3825 refresh.
   - Known surfaces include Koide Q reduced carrier, SM `gstar/I12`, and YT
     boundary rows.

3. Audit-lane reseed/requeue
   - Not source-side work for this branch.
   - Prior disposable diagnostics indicated a reseed materially reduces stale
     ledger noise, but that belongs to the audit lane.
