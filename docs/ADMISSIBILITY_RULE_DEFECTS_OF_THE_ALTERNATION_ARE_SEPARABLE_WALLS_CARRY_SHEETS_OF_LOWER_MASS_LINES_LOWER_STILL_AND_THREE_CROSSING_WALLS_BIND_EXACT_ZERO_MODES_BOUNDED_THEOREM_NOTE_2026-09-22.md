---
claim_id: admissibility_rule_defects_of_the_alternation_are_separable_walls_carry_sheets_of_lower_mass_lines_lower_still_three_crossing_walls_bind_exact_zero_modes_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Coordinate-separable real pure-hop profiles: squared-spectrum decomposition, even-ring kernel compatibility, literal ring and 4^3 fixtures. Walls are prescribed, not dynamically formed."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21
  - admissibility_rule_what_can_gap_the_walk_no_invariant_term_any_reach_chessboard_or_axis_stripes_on_sites_alternating_lengths_give_one_rest_energy_exclusion_cages_bounded_theorem_note_2026-09-22
  - admissibility_rule_bond_rates_alternate_on_their_own_below_a_threshold_stiffness_the_sea_against_block_59s_bond_law_gives_every_species_one_rest_energy_bounded_theorem_note_2026-09-22
runner: scripts/admissibility_rule_defects_of_the_alternation_are_separable_walls_carry_sheets_lines_and_three_crossing_walls_bind_exact_zero_modes_2026_09_22.py
---

# Separable bond profiles and conditional product zero modes

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects
For an even ring L>=4 with nonzero real amplitudes t_x let h=(tT-T^*t)/(2i). On a product of three rings use H=sum_j sigma_j tensor h_j, with each h_j acting only on its own coordinate. The wall fixtures have t_x=1+delta s_x(-1)^x, with s=+1 on the first half and -1 on the second. For localization descriptions take 0<delta<1.

## Theorem T1 — separable square and kernel
Since [h_j,h_l]=0 and the coin matrices anticommute, H^2=I tensor sum_j h_j^2. Simultaneous axis eigenvectors therefore give energies +/-sqrt(sum e_j^2). Positivity of each h_j^2 implies
ker H = C^2 tensor ker h_x tensor ker h_y tensor ker h_z.
The least squared energy is the sum of the three least squared axis energies. General spatial profiles depending on multiple coordinates or a scalar coin hop need not have this property.

## Theorem T2 — closure of the ring recurrence
The zero equation is t_x psi_(x+1)=t_(x-1) psi_(x-1). On each parity sublattice all amplitudes are determined by one seed. Closure holds iff product_even t = product_odd t, with exactly two independent kernel vectors when it holds and none otherwise. Nonzero bonds and even L are necessary for this conclusion.
The specified equal-half wall fixture satisfies the product condition. At L=8, delta=3/10 its amplitudes are (13,7,13,7,7,13,7,13)/10; one zero vector is on each sublattice. The recurrence gives powers of 7/13 away from the maxima, with a possible flat pair of peak sites at the strong-bond wall. This is not a theorem that any two walls give two exact zeros. For example on L=8, reversing only the last two bonds gives unequal parity products and no zero. At delta=0 the vectors are not localized wall states; zero bonds at |delta|=1 require separate analysis.

## Theorem T3 — literal product fixtures
On 4^3 with deltas (3/10,1/5,1/2), zero, one, two and three equal-half wall axes give nullities 0,0,0,16 and least E^2 respectively 19/50,29/100,1/4,0. The sixteen products of two one-axis kernel vectors and two coin vectors are independent and annihilated, so span the entire kernel.
For a uniform axis with |delta_j|<=1, the even-grid minimum e_j^2 is delta_j^2, attained at k=0. Hence compatible zero-mode wall axes remove their own contributions to the spectral edge. These conditional sheet/line spectral statements neither establish physical masses nor prove wall formation.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
An arbitrary pair of walls need not meet the exact parity-product compatibility condition. Product zero modes require coordinate separability and are not an inference of formation dynamics.

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
An arbitrary pair of walls need not meet the exact parity-product compatibility condition. Product zero modes require coordinate separability and are not an inference of formation dynamics.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8581; no premise adoption or retained grade is inferred.
- [admissibility_rule_what_can_gap_the_walk_no_invariant_term_any_reach_chessboard_or_axis_stripes_on_sites_alternating_lengths_give_one_rest_energy_exclusion_cages_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_WHAT_CAN_GAP_THE_WALK_NO_INVARIANT_TERM_AT_ANY_REACH_CHESSBOARD_OR_AXIS_STRIPES_ON_SITES_ALTERNATING_LENGTHS_GIVE_ONE_REST_ENERGY_EXCLUSION_CAGES_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8628; no premise adoption or retained grade is inferred.
- [admissibility_rule_bond_rates_alternate_on_their_own_below_a_threshold_stiffness_the_sea_against_block_59s_bond_law_gives_every_species_one_rest_energy_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_BOND_RATES_ALTERNATE_ON_THEIR_OWN_BELOW_A_THRESHOLD_STIFFNESS_THE_SEA_AGAINST_BLOCK_59S_BOND_LAW_GIVES_EVERY_SPECIES_ONE_REST_ENERGY_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8652; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8660 head `45b3da7dc01fd01d1cea8dfc5073d979dc817907`, branch `physics-loop/admissibility-induced-law-block86-defects-of-the-alternation-are-separable-sheets-lines-and-zero-modes-20260922`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_defects_of_the_alternation_are_separable_walls_carry_sheets_lines_and_three_crossing_walls_bind_exact_zero_modes_2026_09_22.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
