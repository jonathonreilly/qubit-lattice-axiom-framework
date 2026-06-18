actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a route-pruning no-go, not a closure or retained-grade proposal for the statistics atom."
audit_required_before_effective_retained: true
bare_retained_allowed: false

Open imports:

- quotient-level outcome factorization for repeated registrations;
- framework-native record-stack independence, stationarity, or reset/preparation theorem.

Runner evidence:

- `scripts/frontier_statistics_outcome_factorization_not_forced_2026_06_18.py`
  reports `TOTAL: PASS=40 FAIL=0`.
- `scripts/frontier_statistics_atom_reduces_to_product_form_2026_06_12.py`
  reports `TOTAL: PASS=30 FAIL=0` after the companion guard is added.
