# Claim Status Certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The connected-current selector kappa=0 remains an unsupported singlet-annihilation premise."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Dependency classes:

| Dependency | Class | Role |
|---|---|---|
| `F_adj=8/9` | retained support | Exact adjoint fraction. |
| Singlet fraction `1/9` | retained support | Exact disconnected channel. |
| CMT/OZI controls | support-only | Insufficient selector controls. |
| Connected-current projector | unsupported import | Still needed to set `kappa=0`. |

Review disposition: pending local branch review.  Audit pipeline intentionally
not run.
