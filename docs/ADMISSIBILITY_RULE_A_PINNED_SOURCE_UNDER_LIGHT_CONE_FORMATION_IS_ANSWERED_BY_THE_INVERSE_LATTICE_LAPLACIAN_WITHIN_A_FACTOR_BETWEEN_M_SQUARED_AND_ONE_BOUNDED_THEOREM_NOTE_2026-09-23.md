---
claim_id: admissibility_rule_a_pinned_source_under_light_cone_formation_is_answered_by_the_inverse_lattice_laplacian_within_a_factor_between_m_squared_and_one_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Excluded re-recording comparator with a supplied symmetric stencil and source: exact stationary covariance identity, sphere transverse finite-mode inequalities and potential-difference bounds. No exact real-space inverse-distance shape."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_re_recording_at_every_tick_static_law_stationary_light_cone_bilayer_long_range_order_green_function_response_conditional_on_an_excluded_clause_bounded_theorem_note_2026-09-20
  - admissibility_rule_light_cone_formation_keeps_memory_in_3plus1_its_stationary_law_is_one_layer_of_a_reflection_positive_bilayer_ordered_above_beta_0p5905_bounded_theorem_note_2026-09-23
runner: scripts/admissibility_rule_pinned_source_under_light_cone_formation_inverse_lattice_laplacian_within_m_squared_and_one_2026_09_23.py
---

# Conditional source-response identities and finite spectral bounds

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects
Use the excluded re-recording model and even L>=4 bilayer of PR8692. A uniform field epsilon e_z and a pinned source h at x0 enter the update exponent as beta s' dot (neighbor sum+epsilon e_z+h). Derivatives below are at h=0. For sphere bounds take beta>0 and epsilon>=0. The source and update dynamics are supplied, not consequences of the axioms.

## Theorem T1 — source on both levels
Detailed balance holds for pi_h(s) proportional to exp(beta epsilon sum s_z+beta h dot s_(x0)) product_x Z(h_x(s)+epsilon e_z+h 1_(x=x0)). Multiplying by the transition kernel gives a symmetric pair density whose exponent includes the same fields on both levels. Differentiation in finite volume gives d<f>/dh_alpha=beta Cov(f,s_(x0,0)^alpha+s_(x0,1)^alpha).

## Theorem T2 — symmetric branch response
In bilayer coordinates put S_+=(S0+S1)/2, S_-=(S0-S1)/2. An original level is S_+(x)+(-1)^parity(x)S_-(x). Slab swap kills mixed covariances, so R(x)=2beta Cov(S_+^alpha(x),S_+^alpha(0)) and Rhat(k)=2beta <|S_+hat^alpha(k)|^2>/N for k!=0. The original-level structure factor has the sum of the symmetric contribution at k and antisymmetric contribution at k+(pi,pi,pi), with zero cross term. Exact finite-ring enumerations check these identities.

## Theorem T3 — sphere finite-mode bounds
For the sphere with the specified uniform field, the reflection-domination argument of PR8507 still uses identical single-site measures, now weighted by exp(beta epsilon s_z). Reflections preserve that measure. The transverse mean vanishes, and the normalized symmetric eigenmode has variance at most 1/(beta E(k)). T2 thus gives Rhat_perp(k)<=1/E(k).
For the lower bound let D=sum_u c_u L_u, c_u=exp(ik dot x_u), where L rotates the spin in the xz plane. Integration by parts and Cauchy give |<DF>|^2<=beta<|F|^2><Dbar D H>. With F=sum_u conjugate(c_u)s_u^x=2S_+hat(k), <DF>=2Nm and <Dbar D H>=2N[P_b E(k)+epsilon m]; rungs have equal phases and contribute zero, while both slab bond sums give 2NE. Here m=<s_z> and P_b=<s_u^x s_v^x+s_u^z s_v^z><=1 on a slab bond.
Writing D_k=P_b E+epsilon m, the undivided inequality is m^2<=Rhat_perp D_k. The denominator is nonnegative by the same integration-by-parts variance identity. Where D_k>0 this gives Rhat_perp>=m^2/D_k>=m^2/(E+epsilon m). At finite zero field m=0, so this lower bound is trivial. No spontaneous magnetization limit is assumed here.

## Theorem T4 — scope of the spectral comparison
Nonnegative weights 1-cos(k dot x) preserve the bounds in R(0)-R(x)=N^-1 sum_(k!=0)(1-cos(k dot x))Rhat(k). A bounded nonconstant multiplier of 1/E meets a spectral window but is not a constant multiple of it. Thus these inequalities do not identify R(x) pointwise or establish a 1/r tail.
The recurrence theta'=(1-E/7)theta+(A/7)h is a separately supplied gain-one comparator with stationary response A/E; A=coth(7beta)-1/(7beta). It is not derived as the exact derivative of the nonlinear chain. Historical finite-source simulation and infinite-volume state-selection claims are deferred.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Spectral bounds and potential-difference bounds do not determine a real-space kernel shape. The sphere proof does not assert an infrared bound for every arbitrary menu.

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
Spectral bounds and potential-difference bounds do not determine a real-space kernel shape. The sphere proof does not assert an infrared bound for every arbitrary menu.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_re_recording_at_every_tick_static_law_stationary_light_cone_bilayer_long_range_order_green_function_response_conditional_on_an_excluded_clause_bounded_theorem_note_2026-09-20](ADMISSIBILITY_RULE_RE_RECORDING_AT_EVERY_TICK_STATIC_LAW_STATIONARY_LIGHT_CONE_BILAYER_LONG_RANGE_ORDER_GREEN_FUNCTION_RESPONSE_CONDITIONAL_ON_AN_EXCLUDED_CLAUSE_BOUNDED_THEOREM_NOTE_2026-09-20.md): supplied mathematical construction from PR #8507; no premise adoption or retained grade is inferred.
- [admissibility_rule_light_cone_formation_keeps_memory_in_3plus1_its_stationary_law_is_one_layer_of_a_reflection_positive_bilayer_ordered_above_beta_0p5905_bounded_theorem_note_2026-09-23](ADMISSIBILITY_RULE_LIGHT_CONE_FORMATION_KEEPS_MEMORY_IN_3PLUS1_ITS_STATIONARY_LAW_IS_ONE_LAYER_OF_A_REFLECTION_POSITIVE_BILAYER_ORDERED_ABOVE_BETA_0P5905_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied mathematical construction from PR #8692; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8696 head `036826ac2e7b7ff8c3b2529c25db4839e7e4748d`, branch `physics-loop/admissibility-induced-law-block91-a-held-source-under-light-cone-formation-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_pinned_source_under_light_cone_formation_inverse_lattice_laplacian_within_m_squared_and_one_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
