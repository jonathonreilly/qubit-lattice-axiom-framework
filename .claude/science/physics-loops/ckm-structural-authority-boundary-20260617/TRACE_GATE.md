trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "Three runner lanes failed because source notes/runners claimed retained-positive closure while their dependencies are bounded, unaudited, meta, decoration, no-go, comparator, or textbook imports on the current authority surface."
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: demotion
next_trace_action: "Reviewer should decide whether these bounded-support repairs are the right source-side form for audit requeue."

The PR closes the mechanical runner blocker by making each runner return
`HARD_ISSUES=0` when the arithmetic is exact and the only issue is authority
status. It does not close the underlying positive science claims.
