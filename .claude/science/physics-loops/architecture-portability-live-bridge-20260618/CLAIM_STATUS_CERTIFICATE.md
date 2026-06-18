# CLAIM_STATUS_CERTIFICATE

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The artifact makes a bounded finite sweep re-auditable but does not certify retained effective status branch-locally."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

This block may say the live bounded sweep is source-side re-audit ready. It must
not claim retained, retained-bounded, or full Newton closure.
