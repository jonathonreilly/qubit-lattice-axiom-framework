# Claim Status Certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block is a route-pruning no-go, not a retained-positive proposal."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Dependency Classes

- The measured `SIZE=15` cache value is a computed lattice input and is
  support-only for exact endpoint status.
- The endpoint conversion `rho_E = 6(q_E - 1)` is reused conditionally when an
  exact quotient is supplied.
- The finite-size witness laws are explicit mathematical counter-witnesses.

## Status Boundary

The block permits this statement:

```text
A single finite-box E-center calibration point cannot certify the exact
infinite-volume limit q_E = 15/8.
```

It does not permit:

```text
The measured calibration route is closed or rejected.
```

