trace_class: upstream_support
target_claim_id: s3_time_theta_to_slice_coupling_note
target_blocker_text: "underlying readout-map endpoint triple is not yet derived"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "attempt connected-current selector theorem kappa=0"

## Explanation

This block supports the endpoint orientation sign under explicit premises:
`s_TE=-2`, `q_T>0`, and `q_E>0` force `sign(c_TE)=-1`.  It does not close the
endpoint triple because the magnitude `|c_TE|=8/9`, equivalently the connected
selector `kappa=0`, remains open.
