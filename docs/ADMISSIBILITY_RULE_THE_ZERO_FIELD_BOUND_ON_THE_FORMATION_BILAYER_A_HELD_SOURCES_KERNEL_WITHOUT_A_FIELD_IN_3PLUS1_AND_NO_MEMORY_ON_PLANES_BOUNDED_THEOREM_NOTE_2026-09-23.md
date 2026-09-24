---
claim_id: admissibility_rule_the_zero_field_bound_on_the_formation_bilayer_a_held_sources_kernel_without_a_field_in_3plus1_and_no_memory_on_planes_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Excluded re-recording sphere comparator on finite even bilayers: zero-field rotation inequality, stationary response bounds and a planar magnetization limit. No claim of loss of every form of memory."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_re_recording_at_every_tick_static_law_stationary_light_cone_bilayer_long_range_order_green_function_response_conditional_on_an_excluded_clause_bounded_theorem_note_2026-09-20
  - admissibility_rule_light_cone_formation_keeps_memory_in_3plus1_its_stationary_law_is_one_layer_of_a_reflection_positive_bilayer_ordered_above_beta_0p5905_bounded_theorem_note_2026-09-23
  - admissibility_rule_a_pinned_source_under_light_cone_formation_is_answered_by_the_inverse_lattice_laplacian_within_a_factor_between_m_squared_and_one_bounded_theorem_note_2026-09-23
runner: scripts/admissibility_rule_zero_field_bound_on_the_formation_bilayer_held_source_kernel_in_3plus1_no_memory_on_planes_2026_09_23.py
---

# Zero-field bilayer response bounds and vanishing planar magnetization

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects
Use the excluded re-recording sphere model of PR8692 on an even torus L>=4 in d=2 or3, beta>0, zero field. Let N=L^d,V=2N, E(k)=sum_j(2-2cos k_j), Q=<|V^-1 sum_u s_u|^2>, and u(k)=V^-1<|sum_u exp(-ik dot x_u)s_u^1|^2>. These are stationary equilibrium quantities under supplied dynamics.

## Theorem T1 — finite zero-field inequality
Let D=sum c_u L_u, c_u=exp(ik dot x_u), A=sum conjugate(c_u)s_u^1 and m3=V^-1sum s_u^3. Then DA=Vm3, Dm3=-conjugate(A)/V, and <D(Am3)>=VQ/3-u by rotational invariance. With |m3|<=1 and the rotation integration-by-parts inequality from PR8696, <|Am3|^2><=Vu and <Dbar D H><=VE, hence (a-u/V)^2<=beta E u, a=Q/3.
The identity (beta E+2a/V)u-a^2=beta E u-(a-u/V)^2+u^2/V^2 gives
u>=a^2/(beta E+2a/V)>=a^2/(beta E+2/(3V)).
The equal-phase rungs contribute no stiffness. This proof uses sphere rotational invariance and cannot be transferred to arbitrary discrete menus.

## Theorem T2 — three-dimensional response comparison
PR8696 gives Rhat=beta u. The bilayer sum rule in PR8692 gives Q>=1-beta_L/beta, beta_L=3(G_L+H_L)/2. For beta>beta_L this yields
[(1-beta_L/beta)/3]^2/[E(k)+2/(3beta V)] <= Rhat(k) <=1/E(k).
Exact beta_L at L4 and L6 are 18239/35840 and 27735979/51891840. Along nonzero momentum sequences tending to a fixed k, the bounds have their corresponding limits with beta0=3(I0+I2)/2 whenever beta>beta0. This does not assert existence of an infinite-volume response function, its exact shape or a rigorously bounded decimal threshold.

## Theorem T3 — planar stationary magnetization
The symmetric branch sum satisfies sum_k u(k)<=V/3. For d=2 the nonzero grid modes have E(k)<=|k|^2 and 2/(3V)<=|k|^2/(12pi^2). A square shell max(|n1|,|n2|)=j<L/2 contains 8j points, each |n|^2<=2j^2, so sum_(k!=0)|k|^-2 >=(N/pi^2)H_(L/2-1). Dyadic groups of harmonic terms each contribute at least 1/2, hence H diverges.
Summing T1 gives Q^2 <=(6pi^2 beta+1/2)/H_(L/2-1). An original-level mean equals the bilayer mean plus the staggered antisymmetric mode. Slab swap removes the cross term, and its three-component variance is at most 3/[2beta N(E(pi)+2)]=3/(20beta N) in two dimensions. Therefore <|m0|^2><=Q+3/(20beta N) tends to zero.
This is absence of stationary uniform magnetization in the stated planar limit, not a theorem that every observable or initial-information measure is forgotten. Finite simulation plateaus and their rates of decay are deferred.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
The sphere, zero-field and finite even-grid hypotheses are essential. Vanishing stationary magnetization is narrower than absence of every form of temporal memory.

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
The sphere, zero-field and finite even-grid hypotheses are essential. Vanishing stationary magnetization is narrower than absence of every form of temporal memory.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_re_recording_at_every_tick_static_law_stationary_light_cone_bilayer_long_range_order_green_function_response_conditional_on_an_excluded_clause_bounded_theorem_note_2026-09-20](ADMISSIBILITY_RULE_RE_RECORDING_AT_EVERY_TICK_STATIC_LAW_STATIONARY_LIGHT_CONE_BILAYER_LONG_RANGE_ORDER_GREEN_FUNCTION_RESPONSE_CONDITIONAL_ON_AN_EXCLUDED_CLAUSE_BOUNDED_THEOREM_NOTE_2026-09-20.md): supplied mathematical construction from PR #8507; no premise adoption or retained grade is inferred.
- [admissibility_rule_light_cone_formation_keeps_memory_in_3plus1_its_stationary_law_is_one_layer_of_a_reflection_positive_bilayer_ordered_above_beta_0p5905_bounded_theorem_note_2026-09-23](ADMISSIBILITY_RULE_LIGHT_CONE_FORMATION_KEEPS_MEMORY_IN_3PLUS1_ITS_STATIONARY_LAW_IS_ONE_LAYER_OF_A_REFLECTION_POSITIVE_BILAYER_ORDERED_ABOVE_BETA_0P5905_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied mathematical construction from PR #8692; no premise adoption or retained grade is inferred.
- [admissibility_rule_a_pinned_source_under_light_cone_formation_is_answered_by_the_inverse_lattice_laplacian_within_a_factor_between_m_squared_and_one_bounded_theorem_note_2026-09-23](ADMISSIBILITY_RULE_A_PINNED_SOURCE_UNDER_LIGHT_CONE_FORMATION_IS_ANSWERED_BY_THE_INVERSE_LATTICE_LAPLACIAN_WITHIN_A_FACTOR_BETWEEN_M_SQUARED_AND_ONE_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied mathematical construction from PR #8696; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8703 head `3e26092f3c43921e0096c930dad5a8ad1362d4b6`, branch `physics-loop/admissibility-induced-law-block92-zero-field-bound-on-the-formation-bilayer-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_zero_field_bound_on_the_formation_bilayer_held_source_kernel_in_3plus1_no_memory_on_planes_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
