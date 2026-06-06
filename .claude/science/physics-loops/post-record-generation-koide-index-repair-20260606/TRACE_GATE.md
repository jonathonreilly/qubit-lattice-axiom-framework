trace_class: direct_blocker_closure
target_claim_id: post_record_generation_koide_stable_location_index_2026-06-06
target_blocker_text: "Re-audit after the source row map is regenerated against the current ledger or the ledger is repaired to make the stated 105/108 counts true."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Route this stacked repair for re-audit after the selector/dial subdivision repair in PR #2966 is handled."

# Trace Explanation

The blocker was a stale row map. The current selector/dial snapshot has 103
Koide/generation selector rows and 3 stable-feature rows. This PR updates the
source note, runner expectations, and cache to that map.
