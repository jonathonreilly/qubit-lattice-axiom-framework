trace_class: negative_route_pruning
target_claim_id: s3_time_theta_to_slice_coupling_note
target_blocker_text: "the readout-map endpoint triple is not derived, blocking the unique exact Theta_R -> Lambda_R coupling theorem"
source_of_blocker_text: user_goal
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Derive a channel metric/normalization primitive, or construct a new nonseparable total-degree-2 primitive outside current K_R source-side Gram contractions."

## Explanation

If block13 is true, it prunes the source-side Gram/tensor-power route inside
the current `K_R` grammar. It does not close the endpoint; it shows the next
successful primitive must add derived channel normalization or leave the
current carrier grammar.
