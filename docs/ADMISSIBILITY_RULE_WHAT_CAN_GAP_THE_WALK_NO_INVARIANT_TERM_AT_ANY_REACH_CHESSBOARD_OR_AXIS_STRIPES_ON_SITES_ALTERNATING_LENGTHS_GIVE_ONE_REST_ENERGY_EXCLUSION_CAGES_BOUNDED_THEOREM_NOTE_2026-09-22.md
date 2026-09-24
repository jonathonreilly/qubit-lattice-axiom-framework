---
claim_id: admissibility_rule_what_can_gap_the_walk_no_invariant_term_any_reach_chessboard_or_axis_stripes_on_sites_alternating_lengths_give_one_rest_energy_exclusion_cages_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Conditional two-coin cubic-covariant symbols, site-field recurrence on nonaliased even grids, supplied bond hopping, and fixed-vacancy projections. No complete classification of physical gap mechanisms."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_axioms_own_generator_the_scalar_hop_splits_the_eight_species_into_four_levels_of_one_sense_and_a_staggered_term_gives_them_mass_bounded_theorem_note_2026-09-22
  - admissibility_rule_a_chessboard_record_background_is_felt_only_as_a_rest_mass_and_a_wall_between_out_of_step_domains_binds_exact_zero_modes_when_odd_bounded_theorem_note_2026-09-22
runner: scripts/admissibility_rule_what_can_gap_the_walk_no_invariant_term_any_reach_stripes_alternating_lengths_rest_energy_exclusion_cages_2026_09_22.py
---

# Corner symmetry, anticommuting site fields and supplied bond spectra

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects
Use H=sum_j sigma_j S_j on the infinite cubic lattice or an even periodic product with lengths at least four; S_j=(T_j-T_j^*)/(2i). The 16-component momentum block is coin times three two-momentum factors. Bond hopping, scalar hopping and frozen vacancy projection are supplied alternatives.

## Theorem T1 — corner degeneracy
Proper cubic rotations permute the eight corners in orbits of sizes 1,1,3,3. Their stabilizers have orders 24 or 8. In the supplied two-dimensional coin action the stabilizer commutant is scalar, as the runner solves exactly. Covariance therefore makes any translation-invariant symbol scalar at a corner. The two eigenbranches coincide there, possibly at a nonzero scalar energy: this does not exclude a gap about a fixed zero reference.
The runner verifies every rotation lift on all three coin axes.

## Theorem T2 — site-field recurrence
Distinct forward and backward edges in {H,M}=0 give M(x+e_j)=-sigma_j M(x)sigma_j. Iterating in a coin basis yields M=c0 epsilon I+sum_j c_j(-1)^x_j sigma_j, with epsilon=(-1)^(x1+x2+x3). The runner solves this recurrence on a two-periodic cell. It does not solve anticommutation with the actual two-site periodic difference operator, which is zero and permits every M.
Writing C=sum_j c_j(-1)^x_j sigma_j gives C^2=|c|^2 I, [epsilon,C]=0 and M^2=(c0^2+|c|^2)I+2c0 epsilon C. In the continuous zone the smallest positive distance is ||c0|-|c||; full symmetric band separation is twice that. Anticommutation is sufficient here, not necessary for all gaps.
For positive static weights the stripe weight qp^2<=max(p^3,q^3), with equality when p=q. Comparing these three configurations does not decide an equilibrium phase.

## Theorem T3 — supplied hopping symbols
For independent bond amplitudes 1+delta(-1)^x_j the block square is beta^2 sum_j(sin^2 k_j+delta^2 cos^2 k_j). Its continuous-zone minimum absolute energy is sqrt(3)|beta|min(1,|delta|). Strictly positive bonds require |delta|<1; no gap follows if beta=0 or delta=0.
Adding the scalar hop through those same bonds gives corner energies +/-r (multiplicity four) and +/-4a +/-r (multiplicity two), r=sqrt(4a^2+3beta^2 delta^2). Multiplicities combine at coincidences. Corners have zero energies when beta^2 delta^2=4a^2; this is not a global-gap criterion.
The supplied Hermitian staggered-phase scalar term i epsilon A, A=2a sum cos k_j, gives (H+i epsilon A)^2=|s|^2+A^2. It has no continuous-zone zero when a!=0: |s|=0 forces a corner, whose cosine sum is odd and nonzero. Corner absolute energies 6|a| and 2|a| are not a proved global minimum.
With a scalar hop and a chessboard scalar m epsilon, the energies are +/-sqrt(m^2+(A+/-|s|)^2). The continuous-zone minimum absolute energy is |m|, since a diagonal momentum solves A=+/-|s|. A finite grid need not contain that momentum.

## Theorem T4 — fixed vacancies
The one-hop projection onto a vacant set is bipartite off-diagonal; if its two sublattice dimensions are 2Ne and 2No, rank bounds give nullity>=2|Ne-No|. Occupying one whole sublattice leaves a zero projected operator. The literal 4^3 one/two-layer fixtures have nullities 48 and 32. These are frozen-obstacle statements, not moving-record dynamics.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Two-site aliasing, zero hopping and corner-zero exceptions matter. Branch degeneracy and fixed-vacancy confinement do not classify all mass or gap mechanisms.

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
Two-site aliasing, zero hopping and corner-zero exceptions matter. Branch degeneracy and fixed-vacancy confinement do not classify all mass or gap mechanisms.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8581; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_axioms_own_generator_the_scalar_hop_splits_the_eight_species_into_four_levels_of_one_sense_and_a_staggered_term_gives_them_mass_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_OF_ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8612; no premise adoption or retained grade is inferred.
- [admissibility_rule_a_chessboard_record_background_is_felt_only_as_a_rest_mass_and_a_wall_between_out_of_step_domains_binds_exact_zero_modes_when_odd_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_A_CHESSBOARD_RECORD_BACKGROUND_IS_FELT_ONLY_AS_A_REST_MASS_AND_A_WALL_BETWEEN_OUT_OF_STEP_DOMAINS_BINDS_EXACT_ZERO_MODES_WHEN_ODD_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8614; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8628 head `5923e87f141cd4431b540234e4a4fad910bd95cb`, branch `physics-loop/admissibility-induced-law-block82-what-can-gap-the-walk-inside-the-qubit-complete-map-20260922`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_what_can_gap_the_walk_no_invariant_term_any_reach_stripes_alternating_lengths_rest_energy_exclusion_cages_2026_09_22.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
