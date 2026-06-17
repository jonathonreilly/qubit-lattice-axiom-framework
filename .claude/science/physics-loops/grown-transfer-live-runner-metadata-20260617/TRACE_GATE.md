trace_class: direct_blocker_closure
target_claim_id: grown_transfer_basin_targeted_repair_note_2026-06-04
target_blocker_text: "Generated metadata currently selects the slow targeted replay as the primary runner, even though the source note describes the live packet as the cache-backed verifier."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: tooling
next_trace_action: "After review, rebuild audit metadata from source and let the independent audit lane decide the row."

This branch does not audit the row. It changes the source note so the parser's
first primary-runner path is the fast live packet; the slow replay scripts stay
visible through imports and explicit runner-packet prose.
