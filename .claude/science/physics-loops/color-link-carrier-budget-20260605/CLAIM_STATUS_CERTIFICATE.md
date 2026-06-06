# Claim Status Certificate

```yaml
actual_current_surface_status: bounded-support
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block gives a carrier budget and prunes one-qubit routing; it does not derive link routing or physical color."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Dependency classes

- Qubit-link U(2) connection boundary.
- Symmetric-base color carrier support.
- Carrier/routing split support.
- Record dynamics as downstream consumer only.

## Open imports

- Projection/constraint.
- Link-end pairing convention.
- SU(3)-restricted transport.
- Gauss/Wilson observables.
- Action/couplings/rates/time.
- Color-record readout.

## Wording firewall

Allowed: bounded support, exact obstruction, carrier budget, minimal host.

Not allowed: physical color derived, link ontology established, projection
derived, action/coupling selected, dial selected.
