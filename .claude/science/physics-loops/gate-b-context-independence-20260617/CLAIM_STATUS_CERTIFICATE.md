# Claim Status Certificate

```yaml
actual_current_surface_status: no-go
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is an exact negative boundary, not a retained-positive Gate B closure."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Status language allowed in the PR: `no-go`, `exact negative boundary`,
`source-side audit unlock`. Status language not allowed: bare `retained`,
`proposed_retained`, or positive Gate B closure.
