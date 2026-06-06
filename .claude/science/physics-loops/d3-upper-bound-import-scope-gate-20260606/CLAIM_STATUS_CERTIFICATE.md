# Claim Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The artifact certifies import scope and set composition only; named imports remain load-bearing for the upper-bound side."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Dependency Classes

| Dependency | Class | Status in this block |
|---|---|---|
| Lower-bound runner packet | Current bounded source surface | Consumed as `{3,4,5}` |
| Bertrand theorem | Named external import | Still load-bearing for uniqueness |
| Atomic stability | Named external import plus bounded support sublemma | Companion support; weak bound alone leaves `{3,4}` |

## Certificate

The branch may say `exact-support` for the import-scope gate. It may not use
`proposed_retained` or `proposed_promoted` language for the dimension-selection
chain.
