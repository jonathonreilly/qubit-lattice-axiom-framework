# Claim Status Certificate

actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "If a typed single-adjoint-line source selector and complement-rank E-center readout are accepted, the missing E-side entry follows exactly."
hypothetical_axiom_status: "single-adjoint-line source selector absent from the current source bank"
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The decisive selector is a conditional new source/readout primitive, not derived on the actual current surface."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Dependency Classes

| Dependency | Class | Status |
|---|---|---|
| Route-2 endpoint algebra | exact support | available |
| SU(3) adjoint dimension 8 | exact support | available |
| Single typed adjoint line | unsupported import / conditional primitive | absent |
| Complement-rank E-center readout | unsupported import / conditional primitive | absent |

## Certification

The PR title/body may use `conditional-support`. It must not claim closure of the S3/Route-2 endpoint triple or use proposed-retained/proposed-promoted wording.
