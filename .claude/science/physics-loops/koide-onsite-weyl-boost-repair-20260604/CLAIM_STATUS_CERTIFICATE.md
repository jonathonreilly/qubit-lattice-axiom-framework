actual_current_surface_status: bounded-support repair proposal
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: audited_conditional until independent audit reruns
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "Only the independent audit lane can change effective status."
audit_required_before_effective_retained: true
bare_retained_allowed: false

# Certificate

This branch repairs the exact audit blocker by:

- making the source convention `H=iD`, equivalently `D=-iH`;
- removing the non-load-bearing CPT packet from the restricted source/runner/cache surface;
- adding direct runner checks for anti-Hermiticity of `D` and Hermiticity of
  `H=iD`.
