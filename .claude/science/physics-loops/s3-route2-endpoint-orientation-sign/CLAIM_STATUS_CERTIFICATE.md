# Claim Status Certificate

```yaml
actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: endpoint orientation sign sigma=-1 under s_TE=-2 and positive readouts
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The endpoint sign is supported conditionally, but the magnitude selector kappa=0 remains open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Dependency classes:

| Dependency | Class | Role |
|---|---|---|
| Endpoint algebra | retained support | Gives `c_TE=s_TE*q_T/q_E`. |
| T-side shell orientation | conditional-support | Supplies negative sign. |
| Positive readouts | conditional-support | Prevents sign flip. |
| Connected selector `kappa=0` | unsupported import | Still needed for magnitude. |

Review disposition: pending local branch review.  Audit pipeline intentionally
not run.
