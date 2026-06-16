# Claim Status Certificate

## SU3 dabc

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch corrects a source defect and proposes re-audit; it does not set audit status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Record Unbounded

```yaml
actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: "Exact finite-additivity arithmetic conditional on supplied nonzero produced records and supplied readout context."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "Record does not supply production, context, lower bound, or unbounded nonzero availability."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
