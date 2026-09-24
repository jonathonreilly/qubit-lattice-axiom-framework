---
claim_id: admissibility_rule_two_instabilities_of_the_uniform_bond_rates_alternation_breaks_translation_below_alpha_plus_2beta_anisotropy_breaks_rotation_below_beta_alone_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Supplied linear bond-law matrix and continuum sea integrals at fixed arithmetic mean. Exact quadratic coefficients along two selected directions; no complete instability classification."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21
  - admissibility_rule_bond_rates_alternate_on_their_own_below_a_threshold_stiffness_the_sea_against_block_59s_bond_law_gives_every_species_one_rest_energy_bounded_theorem_note_2026-09-22
  - admissibility_rule_the_crowd_under_exclusion_also_gains_from_an_alternation_of_the_bond_rates_its_ground_energy_never_rises_the_jam_is_blind_bounded_theorem_note_2026-09-22
runner: scripts/admissibility_rule_two_instabilities_of_the_uniform_bond_rates_alternation_breaks_translation_anisotropy_breaks_rotation_2026_09_22.py
---

# Restricted quadratic responses of linear-rate alternation and anisotropy

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects
Use the supplied matrix M of PR8652 and positive bond rates linear in the deviations, with arithmetic mean fixed for the two comparison paths. Let s_j=sin k_j, |s|=sqrt(sum s_j^2), chi=<sum cos^2 k_j/|s|>, and chi_a=9<s_x^2(s_y^2+s_z^2)/|s|^3>, as continuous three-dimensional zone integrals. The integrals are finite; the anisotropy integrand extends by zero at s=0.

## Theorem T1 — law costs
Direct substitution gives -M_11(q,0,0)/2=alpha(1-cos q)+4beta. The cosine modulation's spatial power is one at q=0,pi and one-half at other allowed nonaliased momenta. At zero momentum M has eigenvalue zero on (1,1,1) and -12beta on its two-dimensional orthogonal space. Thus u=epsilon(2,-1,-1) has quadratic cost 36beta epsilon^2 per site. The alpha-dependent part of the single-axis cost, after subtracting 4beta, is zero at q=0 and 2alpha at pi; its second derivative alpha cos q changes sign.

## Theorem T2 — selected continuum responses
For the traceless anisotropy the sea integrand is -sqrt((1+2epsilon)^2 s_x^2+(1-epsilon)^2(s_y^2+s_z^2)). Its first derivative at zero is -(2s_x^2-s_y^2-s_z^2)/|s|, whose cyclic images sum to zero. Its second derivative is -9s_x^2(s_y^2+s_z^2)/|s|^3, nonpositive and strictly negative away from its zero sets. Differentiation under the integral is justified locally by a constant times |s|.
The three-axis alternation coefficient is -chi/2, as proved for the continuum integral in PR8652. Finite grids containing zero modes instead can have an alternation cusp.

## Theorem T3 — signs of restricted quadratic variations
The selected costs are (6(alpha+2beta)-chi/2)delta^2 and (36beta-chi_a/2)epsilon^2. Their sign changes are alpha+2beta=chi/12 and beta=chi_a/72. Negative coefficients give descent along the corresponding path, positive coefficients local stability along that path. A zero anisotropy coefficient alone does not settle a minimum; higher orders can matter. These are not necessary/sufficient conditions for full stability or spontaneous dynamics.

## Theorem T4 — scope of the endpoint comparison
A uniform change of one axis is not the traceless path: it changes the total arithmetic mean and has a nonzero first derivative. Its Hessian coefficient chi_a/9 and the traceless coefficient per norm chi_a/6 refer to different directions. A historical finite scan with no intermediate maximizer does not prove a common fixed-mean instability race. All claims of a complete two-instability map or absence of intermediate/off-axis modes are deferred.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Two path Hessians do not classify all perturbations. Equality of a quadratic coefficient does not by itself establish a local minimum or a physical transition.

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
Two path Hessians do not classify all perturbations. Equality of a quadratic coefficient does not by itself establish a local minimum or a physical transition.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8581; no premise adoption or retained grade is inferred.
- [admissibility_rule_bond_rates_alternate_on_their_own_below_a_threshold_stiffness_the_sea_against_block_59s_bond_law_gives_every_species_one_rest_energy_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_BOND_RATES_ALTERNATE_ON_THEIR_OWN_BELOW_A_THRESHOLD_STIFFNESS_THE_SEA_AGAINST_BLOCK_59S_BOND_LAW_GIVES_EVERY_SPECIES_ONE_REST_ENERGY_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8652; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_crowd_under_exclusion_also_gains_from_an_alternation_of_the_bond_rates_its_ground_energy_never_rises_the_jam_is_blind_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_THE_CROWD_UNDER_EXCLUSION_ALSO_GAINS_FROM_AN_ALTERNATION_OF_THE_BOND_RATES_ITS_GROUND_ENERGY_NEVER_RISES_THE_JAM_IS_BLIND_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8657; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8665 head `12042bb076d906acc91f8aa6d54c27ea1a0a4f9f`, branch `physics-loop/admissibility-induced-law-block88-the-two-instabilities-of-the-uniform-bond-rates-20260922`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_two_instabilities_of_the_uniform_bond_rates_alternation_breaks_translation_anisotropy_breaks_rotation_2026_09_22.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
