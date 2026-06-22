# Claim Status Certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The typed bridge needs two unsupported switches: kappa=0 and sigma=-1."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Dependency classes:

| Dependency | Class | Role |
|---|---|---|
| `F_adj=8/9` | retained support | Exact color scalar. |
| `kappa=0` | unsupported import | Connected-trace selector. |
| `sigma=-1` | unsupported import | Endpoint orientation sign. |
| Conditional T-side values | conditional-support | Endpoint algebra conversion. |

Review disposition: pending local branch review.  Audit pipeline intentionally
not run.
