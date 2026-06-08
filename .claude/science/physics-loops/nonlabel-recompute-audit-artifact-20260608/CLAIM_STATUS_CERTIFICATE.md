actual_current_surface_status: bounded-support
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This PR closes a runner-artifact issue for a bounded positive basin; it does not propose unbounded retention."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Certificate

The source claim remains a bounded positive basin for three restore values at a
fixed drift row.  The repair adds a live recompute artifact for those rows, so
the audit no longer has to rely only on the frozen transcript.
