trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "record dynamics must not be used to force or fix the Koide/generation dial"
source_of_blocker_text: user_goal
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Route Koide/generation work to a separate selector proof; record dynamics can handle supplied-setting readout."

# Trace Gate

If true, this artifact prunes record-dynamics-as-selector routes for the
Koide/generation dial. It preserves the stable-dial framing by separating
supplied-setting readout from selector derivation.
