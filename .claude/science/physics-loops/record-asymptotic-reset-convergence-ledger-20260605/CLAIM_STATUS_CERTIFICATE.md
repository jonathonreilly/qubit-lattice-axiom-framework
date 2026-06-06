claim_id: record_asymptotic_reset_convergence_ledger_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "epsilon-reset convergence ledger; no exact finite-time reset or physical rate"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block supplies residual accounting only; p, clock map, bath/cost model, exact finite endpoint, and dial selection remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false

# Certificate

## Dependency Classes

- Parent finite-time reset semigroup no-go.
- Supplied per-step damping parameter.
- Elementary residual arithmetic.

## Open Imports

- Physical derivation of `p`.
- Clock/rate normalization.
- Bath/cost model.
- Exact finite reset endpoint.
- Any dial selection.

## Wording Firewall

Allowed: bounded support, epsilon reset, residual ledger, step-count threshold,
physical rate open.

Not allowed: exact finite reset derived, finite-time rate derived, clock
derived, thermodynamic cost derived, dial fixed or forced.
