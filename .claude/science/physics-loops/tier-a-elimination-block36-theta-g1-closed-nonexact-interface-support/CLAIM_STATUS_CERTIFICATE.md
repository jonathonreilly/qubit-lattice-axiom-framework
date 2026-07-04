actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: exact-support if the closed-nonexact interface I1-I4 is supplied
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The block depends on a supplied closed-nonexact branch interface that is not derived from the current axioms and is not approved as a primitive."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Dependency Classes

| Dependency | Class | Role |
|---|---|---|
| `minimal_axioms` | zero-input structural | Current-surface boundary only. |
| Tier-A theta registry | admitted derivation target | Names the G1 residual. |
| 4D carrier theorem | exact support | Supplies closed-branch H2/Q and defect witness. |
| Exact-branch no-go | no-go | Blocks `n=dA` as retirement route. |
| G1 current-surface no-go | no-go | Blocks absorption by axioms/primitives/support packets. |
| Closed-nonexact interface `I1-I4` | unsupported import on actual surface | Conditional premise tested by this block. |

## Wording Certificate

- `proposed_retained`: not allowed.
- `proposed_promoted`: not allowed.
- Bare retained/promoted wording: not allowed.
- Honest status: conditional exact support / upstream support.
