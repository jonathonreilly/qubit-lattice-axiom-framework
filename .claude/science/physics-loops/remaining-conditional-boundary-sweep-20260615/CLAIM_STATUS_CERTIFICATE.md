actual_current_surface_status: conditional-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a re-audit unlock and boundary repair sweep, not a claim that the hard bridge theorems have been solved."
audit_required_before_effective_retained: true
bare_retained_allowed: false

All changed source notes defer effective status to the independent audit lane.
The local pipeline simulation shows the 13 target rows become `unaudited` and
`ready=true`; generated audit outputs were restored before commit.
