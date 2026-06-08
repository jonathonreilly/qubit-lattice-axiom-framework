actual_current_surface_status: open
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The result is an open-gate diagnostic boundary, not a retained/proposed-retained theorem."
audit_required_before_effective_retained: true
bare_retained_allowed: false

The branch closes the specific runner-certificate defect called out by audit:
the squared Gaussian norm now uses `hermgauss`, whose weight is `exp(-x^2)`.
The runner also adds an analytic interval lower bound showing the `H` ratios
diverge, so the diagnostic does not rely only on the finite quadrature table.

