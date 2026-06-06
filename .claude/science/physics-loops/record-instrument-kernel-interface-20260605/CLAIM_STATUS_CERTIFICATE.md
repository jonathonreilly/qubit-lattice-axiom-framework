# Claim Status Certificate

```yaml
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "exact-support given a supplied finite instrument and trace/effect pairing"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block supplies a typed finite interface; it does not derive the instrument, Born/reference bridge, or local-observability bridge."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Dependency Classes

- Current Record typing.
- Finite post-record history/count dynamics.
- Supplied finite instrument / Kraus interface.
- Trace/effect probability pairing.

## Open Imports

- Instrument derivation.
- Born/reference bridge.
- Local observability / redundant broadcast.
- Production, rates, time, and physical measurement dynamics.
- Dial selection.

## Wording Firewall

Allowed: bounded support, exact conditional interface, probability kernel over
possible records, realized one-hot atom, post-record count/history update.

Not allowed: instrument derived, record atom identified with probability
vector, expected count identified with realized count, dial-location closure,
or audit verdict language.
