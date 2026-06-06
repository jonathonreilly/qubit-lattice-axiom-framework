claim_id: record_reset_sink_entropy_ledger_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "finite sink-memory ledger for reset-with-sink; no thermodynamic cost law"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block supplies finite support accounting only; thermodynamic cost, sink preparation, physical reset dynamics, rates, and dial selection remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false

# Certificate

## Dependency Classes

- Parent reset-with-sink construction.
- Parent blank-boundary no-go.
- Finite support-cardinality arithmetic.

## Open Imports

- Sink blankness / preparation.
- Thermodynamic reset cost.
- Physical reset dynamics.
- Clock/rate normalization.
- Any dial selection.

## Wording Firewall

Allowed: bounded support, finite sink-memory ledger, exported old memory,
many-to-one discard/reblanking, thermodynamic cost open.

Not allowed: thermodynamic cost derived, sink blankness derived, physical reset
dynamics derived, rate/clock closure, dial fixed or forced.
