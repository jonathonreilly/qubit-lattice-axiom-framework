trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "exact reset channel must not be treated as finite-time bounded-generator dynamics"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Route future work to asymptotic, discrete, singular-limit, non-Markovian, or open-boundary reset implementations."

# Trace Gate

If true, this artifact prunes the finite-time bounded-generator shortcut for
exact reset. It leaves the parent reset channel interface intact and redirects
physical dynamics work to honest implementation routes.
