---
claim_id: admissibility_rule_a_chessboard_record_background_is_felt_only_as_a_rest_mass_and_a_wall_between_out_of_step_domains_binds_exact_zero_modes_when_odd_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Under supplied scalar site coupling a checkerboard source decomposes into an offset and a staggered term. Reciprocal clock factors cancel only on hopping edges. Five specified 24-site line matrices have exact nullities 0,4,0,4,0. Bare transverse scalar symbol values are computed; independent-corner wall spectra, localization and a universal thickness rule are not established."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_filled_seas_energy_as_the_ledgers_field_term_a_chessboard_of_clocks_is_invisible_the_sea_induces_a_clock_stiffness_not_the_curvature_member_bounded_theorem_note_2026-09-22
  - admissibility_rule_the_axioms_own_generator_the_scalar_hop_splits_the_eight_species_into_four_levels_of_one_sense_and_a_staggered_term_gives_them_mass_bounded_theorem_note_2026-09-22
runner: scripts/admissibility_rule_a_chessboard_record_background_is_felt_only_as_a_rest_mass_walls_bind_zero_modes_2026_09_22.py
---

# Staggered source algebra and exact kernels of five finite line operators

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

The checkerboard configuration n_x=(1+eps_x)/2, eps_x=(-1)^(x+y+z), and the scalar site coupling c n are supplied. No formation or ordering of that configuration is derived. The supplied free walk H has nearest-neighbour hopping. The coefficient c is real. A choice to use a scalar coupling does not prove that every other record coupling is excluded by the axioms.

## Theorem T1 — two distinct clocking choices

The algebraic identity `c n=(c/2)I+(c/2)eps` gives an offset and a staggered term. For the uniform free walk without scalar hopping the latter has gap |c|/2 relative to the offset, by the odd-displacement square identity. The offset matters to absolute energies and level filling.

For phi_x=r^eps_x, r>0, all nearest-neighbour products equal one, so phi H phi=H. This is a conditional hopping identity, not a derivation of the clock field from a nonzero-total record source on a closed torus. A mean-subtracted source or other compatible boundary prescription would have to be explicitly supplied.

Clocking the whole generator yields `phi(H+c n)phi=H+c w n`; it is not H+c n unless the occupied-site rate is one. Adding c n AFTER clocking only the kinetic operator defines a different supplied model, phi H phi+c n=H+c n. Thus the unqualified statement that the background is felt only as the same rest mass is withdrawn. Wall profiles and inhomogeneous rates introduce further changes not derived here.

## Theorem T2 — five literal line matrices

Independently define K on a periodic ring of size 24 with two coin states:
`(K psi)_x=sigma1(psi_(x+1)-psi_(x-1))/(2i)+m_x(-1)^x psi_x`.
Let m0=3/5 and base m_x=+m0 for 6<=x<18 and -m0 otherwise. For z=0,1,2,3 replace m_(6+j) and m_(18+j) by zero for 0<=j<z. Exact nullities of these 48-by-48 matrices are respectively 0,4,0,4. A fifth profile with m_x=+m0 everywhere except m_6=m_18=0 has nullity zero. Exact elimination over complex rational numbers supplies these finite results.

No statement for other m0, ring sizes, wall separations or thicknesses follows from these five counts. Nullity alone does not localize modes or assign two modes to each wall. These are energies of the displayed K with its offset removed and no scalar hopping or clock deformation.

A single transverse plane wave is NOT an invariant subspace of the three-dimensional staggered term: multiplication by (-1)^(y+z) shifts (k_y,k_z) to (k_y+pi,k_z+pi). The original independent-corner reduction therefore cannot establish a three-dimensional wall count. A paired transverse-sector analysis is deferred.

## Theorem T3 — bare transverse scalar values

For the scalar transverse symbol a0+2a(cos k_y+cos k_z), the corners (0,0),(pi,0),(0,pi),(pi,pi) have values a0+4a,a0,a0,a0-4a and formal orientation signs cos k_y cos k_z equal +,-,-,+. For a!=0 this is a 1:2:1 split of the symbol values; for a=0 all coincide. These are not wall eigenvalues: the actual wall operator includes longitudinal scalar hopping and mixes the transverse corners. No wall chirality, rest-mass spectrum or filling is established.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
The five line-matrix nullities are finite examples, not a universal parity or bound-state theorem. Transverse staggering couples corners. Clocking an on-site term differs from clocking hopping alone; source compatibility and model ordering must be specified.

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
The five line-matrix nullities are finite examples, not a universal parity or bound-state theorem. Transverse staggering couples corners. Clocking an on-site term differs from clocking hopping alone; source compatibility and model ordering must be specified.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8568; no premise adoption or retained grade is inferred.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_filled_seas_energy_as_the_ledgers_field_term_a_chessboard_of_clocks_is_invisible_the_sea_induces_a_clock_stiffness_not_the_curvature_member_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_THE_FILLED_SEAS_ENERGY_AS_THE_LEDGERS_FIELD_TERM_A_CHESSBOARD_OF_CLOCKS_IS_INVISIBLE_THE_SEA_INDUCES_A_CLOCK_STIFFNESS_NOT_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8611; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_axioms_own_generator_the_scalar_hop_splits_the_eight_species_into_four_levels_of_one_sense_and_a_staggered_term_gives_them_mass_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_OF_ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8612; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8614 head `d5d68066d3733ee77b57675a6734ea771c1475fb`, branch `physics-loop/admissibility-induced-law-block79-a-chessboard-record-background-and-its-walls-20260922`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_chessboard_record_background_is_felt_only_as_a_rest_mass_walls_bind_zero_modes_2026_09_22.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
