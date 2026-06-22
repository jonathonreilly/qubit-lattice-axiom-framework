# Claim Status Certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "Restricted-family-only E-center selection is blocked by the shift orbit."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Dependency classes:

| Dependency | Class | Role |
|---|---|---|
| Restricted carrier/readout family | retained support | Defines the exact family being classified. |
| Conditional T-side values | conditional-support | Reduces the remaining ambiguity to `rho_E`. |
| E-center target premise | unsupported import | Exposed as required for positive closure. |

Review disposition: pending local branch review.  Audit pipeline intentionally
not run.
