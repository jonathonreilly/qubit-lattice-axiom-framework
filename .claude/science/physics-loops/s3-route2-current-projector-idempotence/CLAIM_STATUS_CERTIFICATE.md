# Claim Status Certificate

```yaml
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: idempotent current-projector dichotomy kappa in {0,1}
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "Idempotence narrows the selector but does not exclude the full-trace projector."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Dependency classes:

| Dependency | Class | Role |
|---|---|---|
| Two-channel Rconn packet | retained support | Defines the channel fractions. |
| Projector idempotence | conditional-support | Narrows `kappa`. |
| Full-trace exclusion | unsupported import | Still needed for `kappa=0`. |

Review disposition: pass for local branch review.  Audit pipeline intentionally
not run.
