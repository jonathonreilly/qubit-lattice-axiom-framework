---
claim_id: admissibility_rule_the_unit_of_rate_decides_the_alternations_thresholds_in_log_rates_an_exact_mass_a_convexity_term_no_global_minimum_under_a_quadratic_law_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Supplied fixed-mean-log-rate model: exact alternating symbol, continuum second derivatives and an unbounded quadratic-law objective. No uniquely forced clock normalization or physical mass interpretation."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21
  - admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21
  - admissibility_rule_bond_rates_alternate_on_their_own_below_a_threshold_stiffness_the_sea_against_block_59s_bond_law_gives_every_species_one_rest_energy_bounded_theorem_note_2026-09-22
  - admissibility_rule_the_crowd_under_exclusion_also_gains_from_an_alternation_of_the_bond_rates_its_ground_energy_never_rises_the_jam_is_blind_bounded_theorem_note_2026-09-22
  - admissibility_rule_defects_of_the_alternation_are_separable_walls_carry_sheets_of_lower_mass_lines_lower_still_three_crossing_walls_bind_exact_zero_modes_bounded_theorem_note_2026-09-22
  - admissibility_rule_what_a_wall_in_the_alternation_costs_the_sea_charges_it_by_an_exact_level_rule_block_59s_collinear_coupling_rewards_it_domains_iff_alpha_large_bounded_theorem_note_2026-09-22
  - admissibility_rule_two_instabilities_of_the_uniform_bond_rates_alternation_breaks_translation_below_alpha_plus_2beta_anisotropy_breaks_rotation_below_beta_alone_bounded_theorem_note_2026-09-22
runner: scripts/admissibility_rule_the_unit_of_rate_decides_the_alternations_thresholds_in_log_rates_exact_mass_convexity_term_no_global_minimum_2026_09_23.py
---

# Log-rate spectral identities and a constrained quadratic-law comparison

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects
Compare two specified constraints: c=1+u at fixed arithmetic mean, versus c=exp(u) at fixed mean log rate. Use the same supplied quadratic law in its stated variable. Its uniform zero mode does not force a unique normalization of the full objective: the sea energy scales with all hopping rates, whereas a shift-invariant law cost does not. These are different constrained models.

## Theorem T1 — exact log-alternating square
On a momentum pair the operator h=-cosh(delta)sin k tau_z+sinh(delta)cos k tau_y obeys h^2=(sin^2 k+sinh^2 delta)I and h=cosh(delta)h_linear(tanh delta). Independent coordinate pairs commute, so H^2=[sum sin^2 k_j+sum sinh^2 delta_j]I on the 16-component block. The additive constant is a spectral parameter in a lattice sine dispersion, not an exact relativistic dispersion or a derived physical mass.
The eight-ring with alternating amplitudes 2 and 1/2 has squared eigenvalues 9/16,17/16,25/16.

## Theorem T2 — continuum quadratic comparison
Let S=sum sin^2 k_j and I=<1/sqrt(S)>, J=<sqrt(S)>. At S>0 the equal-axis log sea integrand -sqrt(S+3sinh^2 delta) has second derivative -3/sqrt(S), while the linear-rate one has -(3-S)/sqrt(S). Their difference is -sqrt(S), and 3I=chi+J. The singularity 1/|k| is integrable in the three-dimensional continuum zone.
The log-model cost 6kappa delta^2 therefore gives coefficient 6kappa-3I/2, changing sign at kappa=I/4. These are restricted quadratic signs; at equality higher-order analysis is needed. Finite grids with zero modes have a cusp and do not inherit this threshold.

## Theorem T3 — log anisotropy
For rates (exp(2epsilon),exp(-epsilon),exp(-epsilon)), the positive square-root integrand's second derivative exceeds the linear model's by (4a+b)/sqrt(a+b), a=s_x^2, b=s_y^2+s_z^2. The sea energy carries the negative of this derivative. Cyclic integration gives extra magnitude 2J. Thus the total anisotropy coefficient is 36beta-(chi_a+2J)/2. Its zero is beta=(chi_a+2J)/72; neither this nor T2 proves global stability or a dynamical choice.

## Theorem T4 — unbounded supplied objective and corner zeros
For any fixed finite quadratic coefficient, -<sqrt(S+3sinh^2 delta)>+6kappa delta^2 tends to minus infinity as delta tends to plus infinity. For kappa>0 the explicit witness delta_w=6+12sqrt(3)kappa already lies below the uniform energy: sqrt(3)delta_w^3/6-6kappa delta_w^2-sqrt(3)=sqrt(3)(delta_w^2-1)>0, using sinh delta>=delta^3/6 and J<=sqrt(3). This requires the unbounded supplied log-amplitude domain; a nonlinear completion can change it.
For equal log amplitudes and scalar hop a, the corner energy branches are +/-r and +/-4a cosh(delta)+/-r, r=sqrt(4a^2 cosh^2(delta)+3sinh^2(delta)). Corner zeros require tanh^2(delta)=4a^2. Positive a,delta reduce this to tanh(delta)=2a, with a finite positive solution only 0<2a<1. This is not a global-gap criterion.
For equal-axis magnitudes only, the compressed pure-hop crowd likewise scales by cosh(delta). Its finite ground energy is nonpositive by trace zero, so the even-grid nonincrease from PR8657 survives the positive common scaling. This does not prove differentiability or a threshold for the crowd.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Normalization and law completion are explicit choices. Lattice spectral constants, quadratic signs and an objective unbounded below do not establish actual species or dynamics.

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
Normalization and law completion are explicit choices. Lattice spectral constants, quadratic signs and an objective unbounded below do not establish actual species or dynamics.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8571; no premise adoption or retained grade is inferred.
- [admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8581; no premise adoption or retained grade is inferred.
- [admissibility_rule_bond_rates_alternate_on_their_own_below_a_threshold_stiffness_the_sea_against_block_59s_bond_law_gives_every_species_one_rest_energy_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_BOND_RATES_ALTERNATE_ON_THEIR_OWN_BELOW_A_THRESHOLD_STIFFNESS_THE_SEA_AGAINST_BLOCK_59S_BOND_LAW_GIVES_EVERY_SPECIES_ONE_REST_ENERGY_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8652; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_crowd_under_exclusion_also_gains_from_an_alternation_of_the_bond_rates_its_ground_energy_never_rises_the_jam_is_blind_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_THE_CROWD_UNDER_EXCLUSION_ALSO_GAINS_FROM_AN_ALTERNATION_OF_THE_BOND_RATES_ITS_GROUND_ENERGY_NEVER_RISES_THE_JAM_IS_BLIND_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8657; no premise adoption or retained grade is inferred.
- [admissibility_rule_defects_of_the_alternation_are_separable_walls_carry_sheets_of_lower_mass_lines_lower_still_three_crossing_walls_bind_exact_zero_modes_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_DEFECTS_OF_THE_ALTERNATION_ARE_SEPARABLE_WALLS_CARRY_SHEETS_OF_LOWER_MASS_LINES_LOWER_STILL_AND_THREE_CROSSING_WALLS_BIND_EXACT_ZERO_MODES_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8660; no premise adoption or retained grade is inferred.
- [admissibility_rule_what_a_wall_in_the_alternation_costs_the_sea_charges_it_by_an_exact_level_rule_block_59s_collinear_coupling_rewards_it_domains_iff_alpha_large_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_WHAT_A_WALL_IN_THE_ALTERNATION_COSTS_THE_SEA_CHARGES_IT_BY_AN_EXACT_LEVEL_RULE_BLOCK_59S_COLLINEAR_COUPLING_REWARDS_IT_DOMAINS_IFF_ALPHA_LARGE_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8662; no premise adoption or retained grade is inferred.
- [admissibility_rule_two_instabilities_of_the_uniform_bond_rates_alternation_breaks_translation_below_alpha_plus_2beta_anisotropy_breaks_rotation_below_beta_alone_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_THE_TWO_INSTABILITIES_OF_THE_UNIFORM_BOND_RATES_THE_ALTERNATION_BREAKS_TRANSLATION_BELOW_ALPHA_PLUS_2BETA_THE_ANISOTROPY_BREAKS_ROTATION_BELOW_BETA_ALONE_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8665; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8678 head `e7b0c1dfe24724bcdb792a8b95f247ad7c188a53`, branch `physics-loop/admissibility-induced-law-block89-the-unit-of-rate-decides-the-alternations-thresholds-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_unit_of_rate_decides_the_alternations_thresholds_in_log_rates_exact_mass_convexity_term_no_global_minimum_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
