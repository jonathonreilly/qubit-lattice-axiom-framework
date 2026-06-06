actual_current_surface_status: bounded-support
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
proposal_allowed: false
proposal_allowed_reason: "The branch repairs a bounded formula contradiction but leaves the observable-promotion/readout bridge open."
audit_required_before_effective_retained: true
bare_retained_allowed: false

Certified repair:

- The unsigned same-orientation aggregate scales as `L*(2/9)` and is explicitly marked as not the signed global invariant.
- The signed global invariant vanishes under retained `Gamma_5` pairing.
- The runner now checks local signed-pair cancellation directly.

Residual blockers:

- Selecting one `+2/9` local density as the physical observable remains the open gate.
- The signed Brannen/det_R readout remains downstream and not repaired here.
