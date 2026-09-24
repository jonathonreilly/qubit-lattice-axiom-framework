---
claim_id: admissibility_rule_alternating_lengths_are_a_relabelling_invisible_and_free_for_the_ledger_rest_energy_needs_the_bonds_own_amplitude_no_first_order_strain_gap_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Conditional additive site-frame and reach-two strain couplings, curl/constant-volume functionals, and pure bond hopping. The finite corner projection is first-order only; no universal frame or field no-go."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
  - admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
  - admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21
  - admissibility_rule_what_can_gap_the_walk_no_invariant_term_any_reach_chessboard_or_axis_stripes_on_sites_alternating_lengths_give_one_rest_energy_exclusion_cages_bounded_theorem_note_2026-09-22
runner: scripts/admissibility_rule_alternating_lengths_are_a_relabelling_invisible_and_free_rest_energy_needs_the_bonds_own_amplitude_2026_09_22.py
---

# Alternating site frames, corner projections and a finite sea-energy comparison

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects
On even product grids of length at least four let q_j(x)=(-1)^x_j, S_j=(T_j-T_j^*)/(2i), and diagonal additive stretch B_j^j=delta q_j. The site-frame coupling is sum_j sigma_j {1+B_j^j,S_j}/2. The stated reach-two strain coupling uses the symmetric weighted bond operator C_j[B] inside {C_j[B],S_j}/2. These are specific supplied couplings, not every completion of a coframe theory.

## Theorem T1 — exact cancellation in the specified couplings
Since q_j S_j=-S_j q_j, the alternating site-frame contribution vanishes. For the weighted symmetric bond operator, C_j[B]=i delta q_j S_j, also anticommuting with S_j; its reach-two strain term vanishes. The runner verifies both at delta=3/10 on 4^3.
With xi_j=-delta q_j/2, B_j^j=xi_j(x+e_j)-xi_j(x). Every off-diagonal discrete curl is zero. Product averaging yields sum_x product_j(1+delta q_j)=N. Thus a curl-only energy and a constant-coefficient linear total-volume term have the same value as at B=0. This does not cover nonlinear functions of volume, variable clock factors, inverse frames or continuum curvature. Positive invertibility of this diagonal frame needs |delta|<1.
A later reach-three strain coupling uses the two-step momentum P_j=S_j(T_j+T_j^*)/2 in place of S_j. Here q_j commutes with P_j, and {C_j[B],P_j}/2=i delta q_j S_j P_j is generally nonzero. The cancellation is range-specific.

## Theorem T2 — corner projections
If an orthogonal subspace projector Pi is annihilated on both sides by S_j, then Pi{X,S_j}Pi=0 for every X. Corner plane waves have this property, so all the indicated first-order corner blocks vanish. Coupling through intermediate states can still affect higher orders.
The independent bond-amplitude perturbation with alternating strengths has a nonzero corner block, whose square is 3delta^2 I in the equal-axis fixture. This supplies one contrasting example and proves no uniqueness of bond coupling.

## Theorem T3 — sea energy of the supplied bond model
On the four-ring with coin sigma_x and amplitudes 1+delta(-1)^x, the characteristic polynomial is (E^2-1)^2(E^2-delta^2)^2, including coincident-root multiplicities. The sum of negative energies is -2-2|delta|; it has a cusp at zero.
For any finite affine Hermitian H(delta), the negative-energy sum equals min_(0<=Q<=I) Tr(QH(delta)), hence is concave. For the pure-hop even-grid alternation, translation along every alternated axis conjugates H(delta) to H(-delta), so the sum is even and cannot exceed its value at zero. This does not provide differentiability, a minimization dynamics or a physical filling rule.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Cancellation applies to the stated low-range operators and field energies. First-order corner blindness cannot exclude a higher-order gap.

### N2 — Wall independence
No repository no-go wall is used.

### N3 — Supplied structure
The operators, domains, boundary conditions and state assumptions stated above are explicit mathematical hypotheses. They do not add a framework axiom or primitive.

### N4 — Dependencies
The dependencies below identify the actual supplied inputs; earlier stronger conclusions are not imported.

### N5 — Resolution
The canonical runner checks the finite examples and identities stated above using exact arithmetic. General conclusions require the displayed arguments, not extrapolation from samples. Historical simulations are deferred.

### N6 — Primitive boundary
No new primitive, species selection, filling rule or physical interpretation is adopted.

### N7 — Strongest objection
Cancellation applies to the stated low-range operators and field energies. First-order corner blindness cannot exclude a higher-order gap.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8592; no premise adoption or retained grade is inferred.
- [admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8593; no premise adoption or retained grade is inferred.
- [admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8601; no premise adoption or retained grade is inferred.
- [admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8581; no premise adoption or retained grade is inferred.
- [admissibility_rule_what_can_gap_the_walk_no_invariant_term_any_reach_chessboard_or_axis_stripes_on_sites_alternating_lengths_give_one_rest_energy_exclusion_cages_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_WHAT_CAN_GAP_THE_WALK_NO_INVARIANT_TERM_AT_ANY_REACH_CHESSBOARD_OR_AXIS_STRIPES_ON_SITES_ALTERNATING_LENGTHS_GIVE_ONE_REST_ENERGY_EXCLUSION_CAGES_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8628; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8632 head `3944a9633f3ef9e209645753d93109f834089d10`, branch `physics-loop/admissibility-induced-law-block83-alternating-lengths-are-a-relabelling-invisible-and-free-20260922`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_alternating_lengths_are_a_relabelling_invisible_and_free_rest_energy_needs_the_bonds_own_amplitude_2026_09_22.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
