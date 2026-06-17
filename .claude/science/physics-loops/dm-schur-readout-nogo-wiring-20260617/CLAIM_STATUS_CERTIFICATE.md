# Claim Status Certificate

actual_current_surface_status: bounded-support
trace_class: negative_route_pruning
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: "ADM-1 physical readout remains admitted; ADM-2 g remains comparator-scoped"
proposal_allowed: false
proposal_allowed_reason: "ADM-1 positive readout, ADM-2 physical coupling, and ADM-3 phi-space transport remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
review_loop_disposition: reviewer_owned_not_run

This PR is an audit-unlock source repair only. It adds route-pruning support for ADM-1 and
keeps the parent Schur coefficient bounded on named admissions.
