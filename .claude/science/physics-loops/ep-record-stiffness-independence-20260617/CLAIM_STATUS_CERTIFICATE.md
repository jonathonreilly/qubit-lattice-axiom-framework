# Claim Status Certificate

```yaml
actual_current_surface_status: no-go
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is an exact negative boundary, not a retained-positive EP closure."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Retained-proposal checklist:

| criterion | result |
|---|---|
| no open imports for positive EP closure | no |
| all dependencies retained/current axioms | yes for the no-go only |
| no observed/fitted values | yes |
| runner checks dependency classes | yes |
| direct blocker/import closure path | yes, for Record-only route only |
| review-loop disposition | reviewer pending |

Status language allowed in the PR: `no-go`, `exact negative boundary`,
`source-side audit unlock`. Status language not allowed: bare `retained`,
`proposed_retained`, or positive WEP closure.
