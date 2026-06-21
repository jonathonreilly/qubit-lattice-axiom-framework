actual_current_surface_status: open
trace_class: methodology
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a source-graph/audit-support repair only; it does not prove or audit any claim."
audit_required_before_effective_retained: true
bare_retained_allowed: false

This block removes cycle edges from the graph when the queue already marks
them as non-load-bearing citations. It does not assert retained,
proposed_retained, or promoted status for any claim.
