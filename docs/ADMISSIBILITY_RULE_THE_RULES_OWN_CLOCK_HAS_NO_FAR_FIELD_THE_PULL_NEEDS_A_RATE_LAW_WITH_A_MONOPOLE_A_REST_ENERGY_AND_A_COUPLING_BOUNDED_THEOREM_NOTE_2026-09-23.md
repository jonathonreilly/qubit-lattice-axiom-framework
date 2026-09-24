---
claim_id: admissibility_rule_the_rules_own_clock_has_no_far_field_the_pull_needs_a_rate_law_with_a_monopole_a_rest_energy_and_a_coupling_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Compact-support clocks have compact-support Laplacian sources; exact contact ratios, an anticommutation obstruction and conditional reciprocity identities."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_inertia_joined_with_the_rules_pair_weights_by_a_clock_global_clock_exact_local_clock_exact_for_pairs_defect_at_three_records_bounded_theorem_note_2026-09-21
  - admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21
  - admissibility_rule_binding_scale_pinned_at_the_neutral_value_pair_weight_is_the_rules_likelihood_ratio_no_binding_without_a_cycle_all_binding_is_agreement_around_loops_bounded_theorem_note_2026-09-20
runner: scripts/admissibility_rule_the_rules_own_clock_has_no_far_field_2026_09_23.py
---

# Finite-range clock support and conditional source-response algebra

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.

## Premises and declared objects
A supplied local clock is ambient1 when no record lies within a fixed graph distanceR. Setu=log w and Lavg=I-Adj/6. On the cubic lattice use six distinct neighbors, with periodic examples of side at least3. The incident-pair clock is w_x=1/pi_x at occupied sites and1 at empty sites, where pi_x is the product of incident occupied-bond weights.

## Theorem T1 — support and source balance
On any torus sum Lavg u=0 because every value occurs once positively and six times with coefficient-1/6. For a finite cluster on the infinite lattice, u iszero outside itsR-neighborhood; Lavg u iszero outside the(R+1)-neighborhood. The same telescoping count over finite support gives totalzero. Any supplied central-difference force proportional tograd u vanishes farther thanR+1.
Zero source sum ALONE does not imply compact support of its inverse: a separated positive-negative source can produce a noncompact dipole field. Here the conclusion comes from the finite-range definition ofu.

An unneutralized torus equation Lavg u=lambda n has no solution if lambda times record count is nonzero. The mean-zero torus clock of PR8860 instead useslambda(n-count/V); its NET source iszero. The bare source count timeslambda is not the total of its realized torus source.

## Theorem T2 — specified contact ratios
At neutral scale for(3,1,2), the occupied weights are3/2,1/2,1. Assume every occupied neighbor's only occupied neighbor isx. Relative to the arithmetic mean of six neighbor clocks, an isolated record has ratio1; one equal, opposite or orthogonal neighbor gives12/17,12/7,1. Two neighbors give1/2,6/5,12/17,3,12/7,1 in the six unordered relation classes.
The one-neighbor average is382/357 under uniform content and352/357 under pair-weighted content. In the geometric-mean version the ratio ispi_x^(-5/6), because the product of the six neighbor incident weights ispi_x. These are local contact identities, not a constant source law for every configuration.

## Theorem T3 — separate algebraic conditions
For an even kernel and a SUPPLIED point-force model, forces sum to-(E_A S_B-E_B S_A)grad G. With nonzero energies and nonzero gradient they cancel iffS_A/E_A=S_B/E_B. If one additionally sets this common ratio to-gamma/6 in chosen units, log kappa=-(gamma/6)E_rec follows by substitution. That identification is not supplied by the ledger alone; a different mean-clock energy convention changes the ratio.

The only2 by2 matrix anticommuting with all three sigma_j iszero: expanding inI andsigma makes every coefficient vanish. This excludes a particular constant anticommuting gap term. It does not force every rest energy tozero: a scalar onsite terma0I shifts energies, and a record's own energy is independently supplied.
The functional(2/gamma)sum_bonds(sqrt wx-sqrt wy)² scales by t underw to tw for everygamma>0. This homogeneity leavesgamma undetermined by that test. A supplied expression-gamma E_A E_B/(4pi r) is a potential energy, not a force, and no such physical law is inferred here.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Compact support is stronger than net neutrality. An anticommuting-gap obstruction does not set record energies, and homogeneity does not determine a physical coupling.

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
Compact support is stronger than net neutrality. An anticommuting-gap obstruction does not set record energies, and homogeneity does not determine a physical coupling.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the mathematical model below.
- [admissibility_rule_inertia_joined_with_the_rules_pair_weights_by_a_clock_global_clock_exact_local_clock_exact_for_pairs_defect_at_three_records_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_INERTIA_JOINED_WITH_THE_RULES_PAIR_WEIGHTS_BY_A_CLOCK_GLOBAL_CLOCK_EXACT_LOCAL_CLOCK_EXACT_FOR_PAIRS_DEFECT_AT_THREE_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8562; no premise adoption or retained grade is inferred.
- [admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8568; no premise adoption or retained grade is inferred.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8571; no premise adoption or retained grade is inferred.
- [admissibility_rule_binding_scale_pinned_at_the_neutral_value_pair_weight_is_the_rules_likelihood_ratio_no_binding_without_a_cycle_all_binding_is_agreement_around_loops_bounded_theorem_note_2026-09-20](ADMISSIBILITY_RULE_BINDING_SCALE_PINNED_AT_THE_NEUTRAL_VALUE_PAIR_WEIGHT_IS_THE_RULES_LIKELIHOOD_RATIO_NO_BINDING_WITHOUT_A_CYCLE_ALL_BINDING_IS_AGREEMENT_AROUND_LOOPS_BOUNDED_THEOREM_NOTE_2026-09-20.md): supplied mathematical construction from PR #8546; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8931 head `fd92c37695798b92e0903309352b39698442b9cb`, branch `physics-loop/admissibility-induced-law-block104-the-rules-own-clock-has-no-far-field-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_rules_own_clock_has_no_far_field_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
