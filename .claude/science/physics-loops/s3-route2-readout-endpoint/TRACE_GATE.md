trace_class: negative_route_pruning
target_claim_id: s3_time_theta_to_slice_coupling_note
target_blocker_text: "the readout-map endpoint triple is not derived, blocking the unique exact Theta_R -> Lambda_R coupling theorem"
source_of_blocker_text: user_goal
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Derive or no-go a leg-level source/readout factorization primitive that fixes the channel gauges."

## Explanation

If block11 is true, it prunes one tempting route: using endpoint product algebra
or the current `P_R` matrix alone to certify two independent source/readout
dual legs. It does not close the endpoint. It names the next required primitive:
a leg-level factorization theorem or equivalent nonseparable total-degree-2
construction.
