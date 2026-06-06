claim_id: record_dephasing_broadcast_interface_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "dephasing/broadcast interface; selective post-record atom remains a separate gate"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block supplies a nonselective dephasing/broadcast interface only; selection, Born frequencies, rates, and dial selection remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false

# Certificate

## Dependency Classes

- Supplied finite broadcast isometry.
- Finite density-matrix partial traces.
- Record dynamics gate ladder.

## Open Imports

- Selective outcome event / produced atom.
- Born-frequency derivation.
- Physical collapse.
- Clock/rate normalization.
- Any dial selection.

## Wording Firewall

Allowed: bounded support, dephasing/broadcast interface, nonselective ensemble,
selective atom gate open.

Not allowed: outcome selection derived, Born frequencies derived, physical
collapse derived, clock/rate closure, dial fixed or forced.
