trace_class: direct_blocker_closure
target_claim_id: dimension_selection_note
target_blocker_text: "The runner reports that the three tested observables coexist at d=3,4,5; unique d=3 depends on separate orbital and atomic stability inputs not included as authorities."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: demotion_and_runner_certificate
next_trace_action: "Independent auditor should evaluate the narrowed finite-runner lower-bound claim."

# Trace Explanation

This block does not prove unique `d = 3`. It removes that overclaim from the
parent row and routes the remaining lower-bound claim through the retained
finite-k centroid-sign bridge.
