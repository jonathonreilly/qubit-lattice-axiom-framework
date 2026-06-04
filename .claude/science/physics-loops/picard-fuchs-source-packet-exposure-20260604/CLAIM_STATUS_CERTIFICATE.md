# Claim Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch exposes and verifies the source packet for re-audit, but independent audit must still ratify any effective status change."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The PR title/body should use exact-support or re-audit-ready language, not an
audit-ratified status.
