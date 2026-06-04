actual_current_surface_status: bounded-support repair proposal
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: audited_conditional until independent audit reruns
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch proposes closure of an audited conditional blocker, but only the audit lane can change effective status."
audit_required_before_effective_retained: true
bare_retained_allowed: false

# Certificate

The branch does not claim retained status. It repairs the exact conditional
blocker by:

- narrowing the theorem from "no proper subspace" to "no nonzero proper
  invariant subspace";
- replacing the false matrix-unit prose with the retained Burnside formula;
- refreshing the runner/cache so B8 and the verdict text use the repaired
  scope.
