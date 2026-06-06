actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This stacked PR repairs a source/trace row-count blocker only; it does not certify downstream physical source-measure claims."
audit_required_before_effective_retained: true
bare_retained_allowed: false
review_loop_disposition: pass

# Certificate

The runner exits `PASS=49 FAIL=0` and preserves all firewall flags. The artifact
supports re-audit of the source-measure trace row only after the base
measure/weight subdivision repair is available.
