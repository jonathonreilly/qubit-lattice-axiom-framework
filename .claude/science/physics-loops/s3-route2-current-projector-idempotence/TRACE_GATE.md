trace_class: upstream_support
target_claim_id: s3_time_theta_to_slice_coupling_note
target_blocker_text: "underlying readout-map endpoint triple is not yet derived"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "attempt exact full-trace exclusion / singlet-annihilation theorem"

## Explanation

This block gives bounded support for the Rconn-side selector path.  Under
current-projector idempotence, `kappa` must be `0` or `1`.  The remaining
import is now the exact exclusion of the full-trace projector, equivalently
singlet annihilation.
