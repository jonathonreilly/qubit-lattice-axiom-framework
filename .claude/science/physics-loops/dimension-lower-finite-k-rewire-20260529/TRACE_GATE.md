trace_class: direct_blocker_closure
target_claim_id: dimension_selection_lower_bound_bridge_v2_2026-05-20
target_blocker_text: "missing_bridge_theorem: provide a discrete-to-eikonal bridge theorem, or an independent finite-k sign proof, showing the runner's normalized centroid shift has the claimed sign for the stated potential family."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Independent audit checks whether the retained finite-k bridge dependency closes the former conditional blocker."

The patch also corrects two source-drift issues from the same audit rationale:
the false blanket `phi < 0` statement and the overstatement that alpha values
match Green-function falloff to runner precision.
