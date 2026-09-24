---
claim_id: admissibility_rule_the_axioms_own_generator_the_scalar_hop_splits_the_eight_species_into_four_levels_of_one_sense_and_a_staggered_term_gives_them_mass_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Supplied normalized translation-invariant cubic hopping family: nonzero scalar hopping separates the eight corner crossings into four levels. Six nonidentity exchange maps break; the all-axis map survives at zero offset. Odd-displacement operators anticommute with a supplied staggered sign. Paired spectral energies are exact; their corner magnitudes are not generally rest masses."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
  - admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_makes_a_varying_rotation_of_the_coin_axes_a_symmetry_bounded_theorem_note_2026-09-21
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_the_axioms_own_generator_scalar_hop_splits_species_staggered_term_gives_mass_2026_09_22.py
---

# Scalar hopping and staggered fields: level offsets, symmetry exceptions and exact paired spectra

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

On an even torus (or as a bounded translation-invariant operator on the infinite lattice), use the supplied normalized family
`H_a=a0 I+2a sum_j C_j+sum_j sigma_j S_j`, with real a0,a, C_j=(T_j+T_j^-1)/2 and S_j=(T_j-T_j^-1)/(2i).
This is a restricted covariant hopping ansatz with vector hopping normalized to one, not amplitude dynamics derived from the axioms. The extra staggered field m eps_x, eps_x=(-1)^(x+y+z), is supplied, breaks one-site translation and is invariant under proper lattice rotations about a site. Assume real m.

## Theorem T1 — corner crossings

At k=pi n, n in {0,1}^3, the vector symbol sin k vanishes and the scalar value is a0+2a(3-2|n|). For a!=0 these are four distinct levels with multiplicities 1,3,3,1 and orientation signs (-1)^|n|. For a=0 all levels coincide and both signs occur at the common level. Scalar hopping leaves the two coin branches touching at each corner; this is not a claim about a fixed Fermi energy or occupation. Finite tori include all corners when each side is even.

## Theorem T2 — the surviving exception

For the exchange maps V_n, let D_j=(-1)^n_j and s=product_j D_j. Their exact difference is
`V_n H_a V_n-s H_a=(1-s)a0 I+2a sum_j(D_j-s)C_j`.
This follows by applying the exchange to C_j and the free vector walk separately. For a!=0 the six n with |n|=1 or 2 have a nonzero shift coefficient, so their operator differences are nonzero (on the infinite lattice or nonaliasing even tori). For n=(1,1,1), every D_j=s=-1, so the difference is exactly 2a0 I: it VANISHES when a0=0, regardless of a. The identity map always survives. The antiunitary Theta=sigma2 K commutes with H_a for real coefficients; its interpretation is time reversal, not a same-time unitary spatial symmetry.

## Theorem T3 — displacement parity

If every matrix entry of K connects opposite lattice parities, eps K eps=-K. Even-displacement entries instead commute with eps. Thus the free vector walk, scalar nearest-neighbour hop without its offset, supplied varying frame/twist hopping and reach-three strain term anticommute, while the reach-two strain term and site fields commute. For an odd-displacement Hermitian K,
`(K+m eps)^2=K^2+m^2 I`.
This excludes an on-site offset from K; with an offset apply it to H-a0 I. Moreover `phi(K+m eps)phi=phi K phi+m w eps`. For the uniform free vector walk the gap about zero is |m|. A varying clock multiplies the on-site term but supplies no universal finite-packet force law.

## Theorem T4 — exact paired energies

Multiplication by eps couples k with k+pi(1,1,1). In a coin eigenvector of sigma dot sin k with eigenvalue lambda=+/-|sin k|, the two-momentum block is
`[[a0+2a c+lambda,m],[m,a0-2a c-lambda]]`, c=sum_j cos k_j.
Its characteristic polynomial gives energies `a0+/-sqrt((2a c+lambda)^2+m^2)`.
At the eight corners the four opposite-corner pairs have magnitudes relative to a0: one pair sqrt(m^2+36a^2) and three pairs sqrt(m^2+4a^2). These magnitudes coincide iff a=0 and then equal |m|. For a!=0 they are corner energies, not a derived collection of rest masses: the nearby expression generally splits linearly with |q|. The scalar offset and band crossings also preclude inferring species selection or occupation.

The alternating sign is unique up to overall sign if required to reverse on every edge of a connected bipartite graph. Rotation invariance alone does not impose that edge condition and does not make it the unique rotationally invariant site field.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
The all-axis exchange is an explicit exception at a0=0. Distinct levels require a nonzero hop. Parity squaring applies only to odd-displacement terms; corner energies need not be rest masses. Numerical packet and massive-sea experiments are deferred.

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
The all-axis exchange is an explicit exception at a0=0. Distinct levels require a nonzero hop. Parity squaring applies only to odd-displacement terms; corner energies need not be rest masses. Numerical packet and massive-sea experiments are deferred.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8592; no premise adoption or retained grade is inferred.
- [admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8593; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_makes_a_varying_rotation_of_the_coin_axes_a_symmetry_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_THE_BLIND_WALK_A_SCALAR_HOP_WEIGHTED_BY_THE_TWIST_OF_THE_COIN_ALONG_THE_BOND_MAKES_A_VARYING_ROTATION_OF_THE_COIN_AXES_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8596; no premise adoption or retained grade is inferred.
- [admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8601; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_THE_EIGHT_SPECIES_ARE_EXCHANGED_BY_SITE_SIGNS_AND_A_HALF_TURN_OF_THE_COIN_WHAT_EACH_VARYING_FIELD_BECOMES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8602; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8612 head `a2c138c297024d90879cca1eb58336216ff8cfd0`, branch `physics-loop/admissibility-induced-law-block77-the-axioms-own-generator-and-a-staggered-rest-term-20260922`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_axioms_own_generator_scalar_hop_splits_species_staggered_term_gives_mass_2026_09_22.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
