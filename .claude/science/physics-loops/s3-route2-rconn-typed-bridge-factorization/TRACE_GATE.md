trace_class: negative_route_pruning
target_claim_id: s3_time_theta_to_slice_coupling_note
target_blocker_text: "underlying readout-map endpoint triple is not yet derived"
source_of_blocker_text: user_goal
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "attempt endpoint orientation sign theorem sigma=-1"

## Explanation

This block prunes the single-switch Rconn bridge route.  It shows that a typed
bridge `c_TE=-R_conn` requires both connected selector `kappa=0` and endpoint
orientation sign `sigma=-1`.  The artifact narrows the next direct consumer to
the Route-2 orientation sign theorem or the Rconn connected-selector theorem.
