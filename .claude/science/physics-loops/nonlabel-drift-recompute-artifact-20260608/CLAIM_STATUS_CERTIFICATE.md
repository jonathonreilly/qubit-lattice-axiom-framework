actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This PR closes a runner-artifact issue for a bounded finite row grid; it does not propose unbounded retention."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Certificate

The source claim remains bounded to drifts `0.15`, `0.20`, `0.25`, seeds
`0`, `1`, `2`, and fixed `restore = 0.70`. The new cache supplies live
recomputed centroid-shift rows and asserted row gates for that exact grid.
