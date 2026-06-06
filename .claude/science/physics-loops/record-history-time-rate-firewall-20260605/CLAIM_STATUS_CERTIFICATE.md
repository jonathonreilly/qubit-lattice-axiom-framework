# Claim Status Certificate

```yaml
actual_current_surface_status: bounded-support
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: "exact support for order/count/per-step-kernel facts; no physical time/rate closure"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block prunes time/rate overclaims; it does not derive a clock, generator, production law, or physical rate."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Dependency Classes

- Record history/count monoid.
- Conditional instrument-kernel interface.
- Elementary finite kernel and probability/rate algebra.

## Open Imports

- Clock map / metric time.
- Production law / measurement Hamiltonian.
- Continuous-time generator.
- Rate normalization.
- Decoherence and global arrow boundary condition.

## Wording Firewall

Allowed: bounded support, negative route pruning, record order, per-step kernel,
clock residual, rate-normalization residual.

Not allowed: physical time derived, rates derived, generator derived, unlimited
metric-duration closure from unbounded retention, dial-location closure, or audit verdict
language.
