# Claim Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The source-edge blocker is repaired, but the PR has not passed independent review/audit and the theorem still consumes the substep-1 surface at its declared grade."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Use `exact-support` / `source-edge repair` language only. Do not claim retained
closure or audit success.
