---
claim_id: admissibility_rule_a_record_that_cannot_read_the_field_from_its_own_motion_hops_on_its_own_clock_and_with_kept_books_records_attract_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Homogeneous two-end rates independent of arbitrary clock ratios per own tick; fixed positive diagonal matrix similarities; a conditional finite pair-energy sign."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_with_a_one_over_r_potential_equal_both_ways_bounded_theorem_note_2026-09-23
  - admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_a_record_that_cannot_read_the_field_from_its_own_motion_hops_on_its_own_clock_2026_09_23.py
---

# Own-clock rate independence and fixed-matrix timing similarities

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.

## Premises and declared objects
The rate factor q(wx,wy) is positive and homogeneous of degree one on positive independent clocks. Base proposals are clock-independent. For the equal-direction example all six available neighbors have equal base rates. The clock-only record model is PR8860 with W=1 and a neutralized torus field.

## Theorem T1 — independence is a supplied constitutive condition
Homogeneity gives q(wx,wy)=wx phi(wy/wx). Requiring q/wx to be independent of all clock ratios is equivalent to phi being constant. For q=wx^a wy^(1-a), a real, this is equivalent to a=1, since the derivative in wy has factor1-a. With equal base rates, direction probabilities are wy^(1-a)/sum_neighbors wy^(1-a). Uniform clocks, or only one available neighbor, do not determine a from direction odds alone.
With unequal clock-independent base rates, a=1 removes explicit clock dependence but does not make directions uniform. This condition is not a theorem that every local experiment is insensitive to the field or to occupancy.

## Theorem T2 — fixed matrix similarities
For fixed positive diagonal W and Hermitian H,
W^(-1/2)(WH)W^(1/2)=W^(1/2)HW^(1/2)=W^(1/2)(HW)W^(-1/2).
These are algebraic similarities, with physical equivalence only if states, observables and inner products are transformed consistently. WH and HW are generally not Hermitian in the same ordinary inner product. Time-dependent variable transformations introduce additional derivative terms.
For a single classical record with symmetric base proposals, stationary weights are w^(1-2a). The three named timings give1/w,1,w, generically distinct for nonuniform clocks and identical after normalization for uniform clocks.

## Theorem T3 — sign after a separate matching premise
Independently impose gamma,E,wbar>0 and lambda=-(gamma/6)E/wbar. At a=1 the pair energy of PR8860 is U(d)=-(gamma E/wbar)G(d). On L=4,
U(1,0,0)-U(2,0,0)=-(gamma E/wbar)228/7680<0.
This substitution requires the stated source-response matching; it is not forced by record detailed balance or by the ledger alone. It establishes a finite residence-weight preference, not a general force, inverse-distance limit or common motion of records and amplitudes.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Independence quantifies over all positive clock ratios. Matrix similarity requires transformed metrics; source-energy matching is an additional premise, with no implied physical equivalence.

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
Independence quantifies over all positive clock ratios. Matrix similarity requires transformed metrics; source-energy matching is an additional premise, with no implied physical equivalence.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the mathematical model below.
- [admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_with_a_one_over_r_potential_equal_both_ways_bounded_theorem_note_2026-09-23](ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied mathematical construction from PR #8860; no premise adoption or retained grade is inferred.
- [admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8568; no premise adoption or retained grade is inferred.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8571; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8872 head `f6c81d4a73f6b0547340749e1d1655b2f92a7ef8`, branch `physics-loop/admissibility-induced-law-block97-a-record-that-cannot-read-the-field-hops-on-its-own-clock-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_record_that_cannot_read_the_field_from_its_own_motion_hops_on_its_own_clock_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
