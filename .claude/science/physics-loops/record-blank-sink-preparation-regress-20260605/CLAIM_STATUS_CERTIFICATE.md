claim_id: record_blank_sink_preparation_regress_no_go_2026-06-05
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: "exact no-go for closed finite blank-sink preparation without outer sink or boundary"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block proves a narrow closed-finite no-go and leaves boundary/open-system dynamics open."
audit_required_before_effective_retained: true
bare_retained_allowed: false

# Certificate

## Dependency Classes

- Parent reset no-go and sink construction.
- Parent finite entropy ledger.
- Finite support-cardinality arithmetic.

## Open Imports

- Low-record boundary.
- Physical open-system erase/reset dynamics.
- Thermodynamic cost law.
- Clock/rate normalization.
- Any dial selection.

## Wording Firewall

Allowed: no-go, exact negative boundary, blank-sink regress, exported-memory
capacity, boundary/open-system residual.

Not allowed: boundary derived, sink blankness derived, thermodynamic cost
derived, physical erase dynamics derived, clock/rate closure, dial fixed or
forced.
