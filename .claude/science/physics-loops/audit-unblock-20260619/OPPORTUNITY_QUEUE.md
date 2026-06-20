# Opportunity Queue

## Current Block

1. `post_record_flow_thermal_stable_setting_certificate_2026-06-06`
   - Status: completed source-side repair, PR pending.
   - Movement: positive-theorem author hint demoted to bounded theorem;
     current row-map and helper packet coverage refreshed.
   - Audit state after pipeline: unaudited and ready.

## Next Campaign Candidates

1. Source-side stale count or claim-type repairs exposed by ready queue rows
   with archived prior audits.
   - Rationale: these are landable unblock PRs when the source boundary is
     already clear and no audit verdict is needed.

2. Helper-dependency packet repairs for pending rows whose queue entries need
   transitive runner helper inclusion.
   - Rationale: `audit_packet_script_deps.py` reports 386 pending claims with
     helper imports that would otherwise trigger packet-incompleteness risk.

3. Additional supplied-interface rows still described as positive theorem
   where prior audit rationale says supplied-rule discipline or bookkeeping.
   - Rationale: these can be demoted honestly to bounded support and returned
     to the independent audit queue.

Selection rule after PR creation: fetch current `origin/main`, create a fresh
block worktree, choose the highest-ready source-side repair that does not
depend on this unmerged PR, and open one PR for that block.
