claim_id: record_finite_time_reset_semigroup_no_go_2026-06-05
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: "exact no-go for finite-time bounded-generator semigroup realization of exact reset"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block proves a narrow semigroup endpoint no-go and leaves other physical implementation routes open."
audit_required_before_effective_retained: true
bare_retained_allowed: false

# Certificate

## Dependency Classes

- Parent open-system reset channel interface.
- Finite-dimensional matrix-exponential invertibility.
- Reset superoperator rank check.

## Open Imports

- Physical Hamiltonian/bath implementation.
- Thermodynamic cost law.
- Clock/rate normalization for non-exact or asymptotic reset.
- Low-record boundary or environment refresh.
- Any dial selection.

## Wording Firewall

Allowed: no-go, exact negative boundary, finite-time semigroup obstruction,
singular reset endpoint, asymptotic/discrete routes open.

Not allowed: finite physical reset rate derived, Hamiltonian derived,
thermodynamic cost derived, low-record boundary derived, dial fixed or forced.
