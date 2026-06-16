# Assumptions And Imports

## Retained / Retained-Bounded Inputs

- `gravity_weak_field_source_response_bridge_bounded_theorem_note_2026-06-11`
  is current-ledger `retained_bounded` and supplies the weak-field scalar
  source/action sign and test-source response boundary.
- `self_consistency_forces_poisson_note`,
  `finite_rank_source_to_metric_theorem_note`,
  `lattice_greens_1_over_r_from_heat_kernel_resolvent_theorem_note_2026-06-07`,
  and
  `lensing_exponent_is_a_dipole_crossover_resolution_bounded_theorem_note_2026-06-07`
  remain bounded context/support inputs already used by the parent packet.

## Newly Proved In This Branch

- For the axis lattice symbol `lambda_axis(k)=2-2 cos(k)`, a scalar-shifted
  fixed-energy packet satisfies `lambda_axis(k_s)+s=E`.
- The optical index `n=k_s/k0` is the normalized local phase count, not a
  textbook import.
- The first-order coefficient is exactly
  `c_E=1/(k0 lambda_axis'(k0))`, with small-`k` limit `1/(2E)`.

## Still Out Of Scope

- No new repo-wide axioms.
- No physical value of `G_Newton`.
- No arbitrary-graph WKB theorem.
- No nonlinear metric or full Einstein closure.
- No effective-status change until independent audit.
