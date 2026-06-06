trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "The route still needs a direct finite SU(3), Wilson beta=6 table/source-data bracket or a repo-owned beta=6 SDP reproduction."
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Attempt primary source-data extraction at lambda=1.5 or derive beta-coupled loop equations for a repo-owned SDP."

## Explanation

This block partially sharpens the remaining K-Z blocker by pruning a tempting
but invalid reproduction route. It proves that support-only SDP constraints
cannot provide a nontrivial beta=6 upper bound because the endpoint witness
`P=R=Q=1` satisfies them.

It does not close the blocker. The live positive paths remain primary source
data at `lambda=1.5` or a repo-owned SDP with beta-coupled loop equations.
