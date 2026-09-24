---
claim_id: admissibility_rule_light_cone_formation_keeps_memory_in_3plus1_its_stationary_law_is_one_layer_of_a_reflection_positive_bilayer_ordered_above_beta_0p5905_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Under an explicitly excluded re-recording clause: positive symmetric-stencil update kernels, even-grid bilayer geometry, sphere reflection bounds and finite stationary moments. No temporal-memory theorem or rigorously bounded numerical onset."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_re_recording_at_every_tick_static_law_stationary_light_cone_bilayer_long_range_order_green_function_response_conditional_on_an_excluded_clause_bounded_theorem_note_2026-09-20
runner: scripts/admissibility_rule_light_cone_formation_keeps_memory_in_3plus1_stationary_law_one_layer_of_a_reflection_positive_bilayer_2026_09_23.py
---

# Conditional reversible update law and bilayer stationary bounds

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects
The model supplies a new record at every site at every tick, independently conditioned on the preceding level. This is the re-recording clause excluded by the repository memo's permanent one-record-per-site reading, as stated in PR8507. It is not adopted.
On a finite cubic torus of even side L>=4, use unit sphere contents with uniform base measure and K(s'_x|s) proportional to exp(beta s'_x dot sum_(d in N7)s_(x+d)), N7={0,+/-e_j}. Reversibility also applies to finite menus with positive finite normalizers; the sphere infrared conclusions require beta>0.

## Theorem T1 — stationary detailed balance and a counter-cycle
For a symmetric effective stencil, pi(s) proportional to product_x Z(h_x(s)) satisfies pi(s)P(s'|s) proportional to exp(beta sum_(x,d)s'_x dot s_(x+d)), symmetric in the two levels. Thus pi is stationary and the pair law is the doubled-graph interaction.
For the specified one-sided stencil on L>=4, opposite unit contents give a three-state cycle with forward/backward ratio exp(8beta), so reversibility fails when beta!=0. The runner checks the symbolic ring cycle and the 4^3 exponent. At beta=0 all updates are independent base-measure draws and are reversible. Raw integer stencil asymmetry is not enough if offsets alias modulo the grid; on a two-site ring +1 and -1 are identical.

## Theorem T2 — bilayer isomorphism
The parity relabelling (x,a) to (x,a xor parity(x)) takes self-offset edges to rungs and neighbor edges to slab bonds. On even L>=4 it gives two cubic slabs with one rung per site. Its Laplacian eigenvalues are E(k) and E(k)+2, E=6-2sum cos k_j, with normalized eigenvectors proportional to exp(ik dot x)(1,+/-1). In original doubled coordinates the branches are E(k),14-E(k); the spectral multisets agree after shifting momentum by (pi,pi,pi), not pointwise between the second branches.

## Theorem T3 — reflection bound and stationary sum rule
For positive beta, bond-plane reflections and slab swap exchange halves without fixed vertices; every crossing edge is a mirror pair and all edges are covered. The sphere interaction crossing factors have nonnegative power-series coefficients, giving reflection positivity.
We explicitly use the mathematical domination proof in current PR8507 T3: reflected-field Cauchy inequality for Z(h); a maximizing field with a minimal number of nonzero edge differences; reflection across any nonzero crossing difference reduces that count, forcing a constant maximizer. Differentiating Z(h)<=Z(0) gives variance <=1/(beta lambda) for each normalized nonzero eigenmode and each spin component. The runner checks finite geometry, not the whole analytic domination theorem.
With N=L^3, G_L=N^-1 sum_(k!=0)1/E(k), H_L=N^-1 sum_k 1/(E(k)+2), and M the total spin, the sum rule yields <|M/(2N)|^2>>=1-3(G_L+H_L)/(2beta). Layer symmetry and |(m0+m1)/2|^2<=(|m0|^2+|m1|^2)/2 give the same lower bound for one original level. The exact coefficient 3(G_L+H_L)/2 is 18239/35840 for L4 and 27735979/51891840 for L6.
Current PR8507 T3 also supplies limiting behavior of these sums to I0 and I2, so the stationary moment has positive liminf when beta>3(I0+I2)/2. No quadrature approximation here is a rigorously bounded upper bound or an exact onset.

## Theorem T4 — original-level reflection is different
For reflection across the two original levels, the crossing matrix is I+A_nn. The staggered spin difference gives quadratic form -64 on the open cube and -20N on the 4^3 torus. The corresponding two-configuration kernel minor is negative for beta>0. This does not contradict positivity of the different bilayer reflections.
Stationary nonzero squared magnetization is not proof of retention of initial information, a mixing time or persistence along every trajectory.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
The re-recording clause is excluded and remains a comparator. Stationary moments and sufficient symbolic bounds are not a dynamic memory theorem or a numerical phase boundary.

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
The re-recording clause is excluded and remains a comparator. Stationary moments and sufficient symbolic bounds are not a dynamic memory theorem or a numerical phase boundary.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_re_recording_at_every_tick_static_law_stationary_light_cone_bilayer_long_range_order_green_function_response_conditional_on_an_excluded_clause_bounded_theorem_note_2026-09-20](ADMISSIBILITY_RULE_RE_RECORDING_AT_EVERY_TICK_STATIC_LAW_STATIONARY_LIGHT_CONE_BILAYER_LONG_RANGE_ORDER_GREEN_FUNCTION_RESPONSE_CONDITIONAL_ON_AN_EXCLUDED_CLAUSE_BOUNDED_THEOREM_NOTE_2026-09-20.md): supplied mathematical construction from PR #8507; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8692 head `c3412ce59542e2edfaef2ae45d19cca9d390c194`, branch `physics-loop/admissibility-induced-law-block90-light-cone-formation-keeps-memory-in-3plus1-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_light_cone_formation_keeps_memory_in_3plus1_stationary_law_one_layer_of_a_reflection_positive_bilayer_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
