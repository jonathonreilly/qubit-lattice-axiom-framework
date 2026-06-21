# Claim Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "If the typed magnitude bridge is supplied, endpoint algebra gives rho_E=21/4."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The typed magnitude bridge is still open; the endpoint triple is not derived on the current bank."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Dependency Classes

| Dependency | Class | Disposition |
|---|---|---|
| Route-2 endpoint algebra | exact support | accepted support |
| T-side values `q_T=5/6`, `s_TE=-2` | conditional support | carried with caveat |
| Positivity `q_E>0` | exact support/no-go boundary | used only for sign |
| `R_conn=8/9` scalar | exact support as `F_adj` | used only as magnitude candidate |
| Typed magnitude bridge | unsupported import | open |

## Certification

This block supports the endpoint target by reducing a signed bridge import to a
magnitude bridge import plus positivity.  It is not certified for proposal
language that would treat the endpoint triple as closed.
