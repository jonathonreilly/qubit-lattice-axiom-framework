---
claim_id: admissibility_rule_records_that_move_with_vacancies_the_infrared_stiffness_is_set_by_the_binding_scale_long_range_order_above_the_neutral_scale_and_no_full_bound_at_it_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Supplied annealed static vacancy law with beta>0,c>0 and finite z>=0 on even periodic cubic tori with
  bond multiplicities. Kernel factorization for real beta-prime; positive-semidefinite remainder threshold only
  for gamma=beta-beta-prime>=0. For c>c0(beta), a component infrared bound with proved coefficient beta_A=beta-gamma(c)>0;
  this is a sufficient bound, not a measured or optimal physical stiffness. Exact finite two-valued neutral-scale
  counterexamples refute universal full-beta and bond-density bounds. Sphere torus magnetization liminf is at least
  rho_liminf-3G(0)/beta_A. No formation dynamics, interacting transport, neutral-scale disorder or infinite-volume
  counterexample is claimed.
upstream_dependencies:
- admissibility_rule_binding_scale_pinned_at_the_neutral_value_pair_weight_is_the_rules_likelihood_ratio_no_binding_without_a_cycle_all_binding_is_agreement_around_loops_bounded_theorem_note_2026-09-20
- admissibility_rule_cubic_walk_return_sum_and_sphere_static_magnetization_sufficient_bound_bounded_theorem_note_2026-09-15
- admissibility_rule_records_that_move_pair_weight_transit_has_the_static_law_as_equilibrium_the_binding_scale_is_a_new_constant_clumping_and_jamming_executed_bounded_theorem_note_2026-09-20
- admissibility_rule_sphere_static_law_zero_field_component_fourier_bounds_bounded_theorem_note_2026-09-15
runner: scripts/admissibility_rule_records_that_move_with_vacancies_the_infrared_stiffness_is_set_by_the_binding_scale_2026_09_24.py
---

# Static vacancy law: a sufficient infrared bound and finite neutral-scale counterexamples

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 39 and 40 as landed, carried to the menus of blocks 19 and 22 as landed; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within blocks 39 and 40 as landed on main (the law with vacancies and its neutral scale), carried to the sphere and two-valued menus of blocks 19 and 22 as landed; it reports the infrared bound for the law with vacancies and its stiffness, where it holds and where it fails; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

For the supplied static vacancy law, a positive kernel split proves a component structure-factor bound with coefficient beta_A=beta-gamma(c), provided c>c0(beta). This coefficient does not explicitly contain density, but density still affects correlations and the sufficient magnetization condition. No optimal stiffness is identified.

At the neutral scale beta_A=0, this proof gives no finite bound. Two exact finite two-valued examples refute a universal full-beta bound and its bond-density variant. They do not refute those inequalities for the sphere menu or in an infinite-volume limit. For the sphere law the sum rule gives a torus magnetization-square liminf bound, positive when beta_A times the density liminf exceeds3G(0). A value merely above the neutral scale need not satisfy that condition.

These are equilibrium calculations with annealed vacancies. No transition rates, record-formation law or transport process is analyzed.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "A site never carries more than one record; records are permanent." A site is empty or holds one content. Records that move are the owner's reading, and that reading is supplied.
  - "Each site has a domain of local possibilities." Here that is the menu of contents.
  - "Admissibility is not a dynamics axiom." The motion, the scale, the fugacity and the law with vacancies are supplied clauses. Nothing is adopted.
- **The law with vacancies** (block 39 T5 as landed). The states of a site are `∅` or a content `s`.
  - The a priori weight is `1` for `∅` and `z` times the menu's measure for contents.
  - The bond kernel is `B(∅, ·) = B(·, ∅) = 1` and `B(s, s') = c e^{βs·s'}`.
  - Assume beta>0,c>0 and finite z>=0. The law is `∝ Π_b B(u_x, u_y)` on an even torus, with one bond per site and direction. On a side of two the pair is joined twice.
- **Menus.** The sphere menu has `s ∈ S²` with the uniform measure (blocks 19 and 22 as landed). The two-valued menu has `s = ±1` with counting measure.
- **Fields.** The component vector e is a unit vector.  `σ_x = n_x s_x`, with `n_x = 1[x occupied]`. Also `σ̂^e(k) = N^{−1/2}Σ_x e^{ik·x}σ_x·e` and `E(k) = Σ_i 2(1 − cos k_i)`. The densities are `ρ = ⟨n_x⟩` and, on a bond, `ρ₂ = ⟨n_xn_y⟩`.
- **Scales.** `c₀(γ) = γ/sinh γ` (sphere) or `1/cosh γ` (two-valued), with `c₀(0) = 1`.
  - For `c₀(β) ≤ c < 1`, `γ(c)` is the root of `c₀(γ) = c`. For `c ≥ 1`, `γ(c) = 0`.
  - `β_A(c) = β − γ(c)`.
  - Block 40's neutral scale, carried to these menus, is `c₀(β)` (block 39 T5 as landed gives it for the sphere).
- **Named standard results**, used at definition level: the Schwarz inequality for a positive form; the expansion of `e^{γt}` in the sphere's zonal functions (Legendre polynomials, with the Rodrigues form of their coefficients and the addition theorem); Gaussian domination through reflection in bond planes (Fröhlich–Simon–Spencer), re-proved at this scope in the attempt.

## Theorem T1 — the split and the positivity threshold

*Statement.*
- (a) For every `β'`, `B(u, u′) = e^{(β′/2)(n+n′)} e^{−(β′/2)|σ−σ′|²} R_{β−β′}(u, u′)`. Here `R_γ` is the law's kernel with the same `c` and coupling `γ`.
- (b) For gamma>=0, `R_γ` is a sum of products with non-negative coefficients iff `c ≥ c₀(γ)`.
  - Two-valued: `R_γ = 1 + (c cosh γ − 1)nn′ + (c sinh γ)(ns)(n′s′)`. The occupied part of the kernel, after the empty state is removed, has eigenvalues `2c cosh γ − 2` and `2c sinh γ`.
  - Sphere: for gamma>0 the zonal coefficients of `e^{γt}` are all positive; at gamma=0 only the constant coefficient survives, and the constant one is `sinh γ/γ`.
- (c) On gamma>=0, c0 decreases strictly from1 (its derivative is zero only at the endpoint). For gamma<0 the odd occupied mode is negative, so the asserted positive-kernel threshold would be false; that region is excluded.

*Proof.*
- (a) `|σ − σ′|² = n + n′ − 2nn′ s·s′`, since `n² = n` and `|s| = 1`. If `nn′ = 0` both sides are `1`. Otherwise `e^{β′}e^{−β′(1 − s·s′)}ce^{(β−β′)s·s′} = ce^{βs·s′}`.
- (b)
  - Two-valued: `e^{γss′} = cosh γ + ss′ sinh γ`. Removing the empty row and column leaves `R − 1` restricted to records, and its eigenvalues are as stated.
  - Sphere: for gamma>0 each zonal coefficient is a positive multiple of `∫(1 − t²)^ℓe^{γt}dt > 0`. By the addition theorem each term is a sum of products. Only the constant term competes with the empty state, through `c·sinh γ/γ − 1`.
  - The converse is block 39 T5 as landed.
- (c) `d(1/cosh γ)/dγ = −sinh γ/cosh²γ`. Also `d(γ/sinh γ)/dγ = (sinh γ − γ cosh γ)/sinh²γ < 0`, because `d(sinh γ − γ cosh γ)/dγ = −γ sinh γ`.

∎

*Checked (B1).*
- The split for the four occupation pairs, symbolically.
- The occupied eigenvalues.
- The zonal coefficients for `ℓ ≤ 3`, and the constant one.
- The derivatives.
- The rational neutral values `1/cosh(ln 3) = 3/5` and `1/cosh(ln 20) = 40/401`.

## Theorem T2 — a sufficient component bound from the kernel split

*Statement.*
- (a) Replace `σ_x` by `σ_x − φ_xe` at every site, empty ones included, in the Gaussian factor of T1(a). For `φ = λψ` with `ψ` a plane wave, the linear term is `λβ′E(k)Σ_xσ_x^eψ_x`. Twisting only the bonds between two records does not give this term.
- (b) For c>c0(beta), on every even torus, for finite z>=0, every unit component e and every k!=0, `⟨|σ̂^e(k)|²⟩ ≤ 1/(β_A(c)E(k))`. For `c ≥ 1` this is block 19's bound `1/(βE(k))`.

*Proof.*
- (a) Sum by parts over the bonds. `ψ` is an eigenfunction of the lattice Laplacian with eigenvalue `E(k)`.
- (b) Take `β′ = β_A(c)`, so that `c ≥ c₀(β − β′)` by T1(c).
  - The factor exp[(beta-prime/2)(n+n-prime)] over all bonds becomes the identical site weight exp(3 beta-prime n). Keep this factor: shifted fields do not have constant norm.
  - Across a bond reflection the remaining crossing kernel is R_gamma(u,v) exp[-beta-prime |(sigma_u-phi_u e)-(sigma_v-phi_v e)|^2/2]. It is positive semidefinite on pairs (u,phi): the first factor is positive by T1, and the second factors into the two norm factors times the exponential dot-product series with nonnegative coefficients. Products of their sum-of-products expansions remain positive. The positive-form inequality yields Z(phi)^2<=Z(phi-plus)Z(phi-minus), with either half copied by reflection.
  - Modulo a constant shift, the finite-dimensional function Z(phi) attains its maximum: sigma is bounded and the connected graph's quadratic gradient penalty forces Z(phi) to0 as the mean-zero phi norm grows. Choose a maximizer with the fewest edges on which phi differs. If any such edge exists, reflect in its bond plane and the antipodal plane. Copied configurations have zero differences on the cut edges. Their total numbers of differing internal edges sum to twice the original internal count, so at least one has strictly fewer differing edges than the original. The partition inequality and maximality make both copied configurations maximizers, a contradiction. Thus a maximizer is constant and Z(phi)<=Z(0).
  - Write X=sum_b grad(psi)grad(sigma dot e), Q=sum_b grad(psi)^2. Spin inversion gives mean X=0; the second derivative gives beta-prime squared times mean X squared <= beta-prime Q. For real cosine and sine modes sum their variance bounds, using norms N/2 each. At nonzero self-inverse momenta the sine vanishes and cosine norm is N, giving the same component normalization. Consequently mean|sigma-hat^e(k)|^2<=1/(beta-prime E(k)). No arbitrary site-dependent measure is imported from block19.

∎

*Checked (C1).*
- The all-site linear term against `E(k)Σσψ` on all `3⁸` configurations of the `2×2×2` torus, at every `k ≠ 0`.
- The bonds-between-records term is `0`, against `2`, on the ring `(+1, +1, ∅, +1)` at `k = π/2`.
- Where the proof applies, the bound holds on the torus at `e^β = 3` and `z = 1/8`:
  - at `c = 1` and `2`, with `β_A = β`;
  - at `c = 4/5`, where `γ = arccosh(5/4) = ln 2` and `β_A = ln(3/2)`.

  Every nonzero `k` is checked, with rational upper bounds on the logarithms.

## Theorem T3 — at the neutral scale the route closes and the full bound is false

*Statement.*
- (a) At `c = c₀(β)`, `γ(c) = β`, so `β_A = 0`: T2 gives nothing.
- (b) On the `2×2×2` torus, two-valued menu, at `e^β = 3`, `c = 3/5 = c₀(ln 3)`, `z = 1/8` and `k = (π, π, π)`:
  - `⟨|σ̂(k)|²⟩ = 4295671717826064002261/38505646859840596246081` exactly;
  - `⟨|σ̂(k)|²⟩βE(k) > 147/100`.
- (c) At `e^β = 20`, `c = 40/401 = c₀(ln 20)` and `z = 1/5`: `⟨|σ̂(k)|²⟩βρ₂E(k) > 181/100`, with `ρ ∈ (8/10, 801/1000)`.

So at the neutral scale neither `1/(βE)` nor `1/(βρ₂E)` bounds the structure factor.

*Proof.*
- (a) By T1(c).
- (b), (c) Exact enumeration of the `3⁸` configurations, with the logarithms bounded below by rational partial sums of `2 atanh`.

∎

*Checked (D1).* Both values and both inequalities, exactly.

*Reading.* Equality of the orientation-averaged occupied-neighbor weight and the empty-neighbor weight does not erase the energetic gain of alignment: an aligned pair has weight c exp(beta). The two finite counterexamples establish only their stated inequalities. They do not establish an asymptotic stiffness law or neutral-scale disorder.

## Theorem T4 — long-range order above the neutral scale

*Statement.* On `Z³` with the sphere menu and beta_A>0, as the torus liminf consequence of T2 (as in block 19):
- `M² ≥ ρ − 3G(0)/β_A(c)`, where M²=liminf M_N² and rho=liminf rho_N along the same even cubic volumes. No unique infinite-volume state or full limit is assumed.
- So long-range order of the contents holds once `(β − γ(c))ρ > 3G(0)`.
- `3G(0) < 76/100` (block 22 as landed). An elementary bound is `G(0) ≤ √3π/8`.

*Proof.*
- The sum rule `Σ_eΣ_k⟨|σ̂^e(k)|²⟩ = Nρ` together with T2 gives `M_N² ≥ ρ_N − (3/β_A)N^{−1}Σ_{k≠0}1/E(k)`. The lattice sum tends to G(0): using E(k)>=4|k|^2/pi^2, integer shells bound the normalized contribution from 0<|k|<delta by C delta+O(1/L); away from zero ordinary grid integration applies. This is the parent19 shell argument. Taking liminf gives the stated bound. Positive M² is the torus long-range-order diagnostic, not a selected extremal-state or pointwise correlation theorem.
- For the elementary bound, `1 − cos u = 2 sin²(u/2) ≥ 2u²/π²` on `[−π, π]`, by the concavity of sine on `[0, π/2]`. So `E(k) ≥ 4|k|²/π²`, and the integral over the ball of radius `π√3` gives `√3π/8`.

∎

*Checked (E1).* The identity, the endpoint value, and the ball integral, exactly.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "blocks 39-40 as landed: the law with vacancies is reflection positive exactly from the neutral scale up; whether moving records' contents order, and with what stiffness, is not stated"
source_of_blocker_text: blocks 39 and 40 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the neutral law at large beta: an infrared bound by another embedding of the empty state, or a lower bound on S(k) at large k; the full-beta threshold c1 for the sphere menu (numerical in the attempt)"
conditional_surface_status: "T1-T2 on every even torus; T3 exact on the 2x2x2 torus; T4 for the torus magnetization liminf; the menu, motion, scale and fugacity supplied"
hypothetical_axiom_status: "records that move, the law with vacancies and the scale are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 19: the sphere static law's Gaussian domination and component infrared bounds (with Gaussian domination explicitly imported).
  - Block 22: `75/100 < 3G(0) < 76/100`.
  - Block 39: the law with vacancies and its reflection positivity from the neutral scale up (T5, the sphere case included).
  - Block 40: the neutral scale as a proposal.
- **The probes attempts.**
  - `moving-kernel-with-vacancies` a1 (Claude Opus 5.5, issue #8616) found T1–T4 and the counterexamples. A Grok referee confirmed them (#9114).
  - The attempt's Theorem B (the full-`β` bound for the two-valued menu above a threshold `c₁(β) < 1`) rests on a checked identification, and is not used here.
  - Attempts a2 and a4 (#8538, #8537; Grok-confirmed #9044, #9003) proved lattice conditions for the occupation marginal. They served a3's criterion with `ρ₂`, which T3(c) refutes at the neutral scale. They are not used here.
- **In the literature.**
  - Gaussian domination and infrared bounds (Fröhlich, Simon and Spencer).
  - Reflection positivity through bond planes.
  - Zonal expansions on the sphere.

  The kernel expansions and positive-form inequality are mathematical tools used in the displayed proof; historical attribution is not additional evidence.
- **New here:**
  - an independent exact runner;
  - the results placed against blocks 39 and 40 as landed.
  - The reading is that the proposed neutral scale is exactly where this route to order fails.

## Exact target and obligation graph

Target: the infrared bound for the law with vacancies, and its stiffness. The obligations are:
- (O1) the split and the threshold (T1);
- (O2) the bound (T2);
- (O3) the neutral scale (T3);
- (O4) long-range order (T4).

T1–T4 discharge them. Open: the neutral law at large `β`.

## No-Go Discipline Gate

The note's negative sentence: at the neutral scale the full-`β` infrared bound, and the bound with the bond density, are false for the law with vacancies.

### N1 — Routes by which the sentence could fail or mislead
1. *Small torus.* The counterexamples use the `2×2×2` torus with doubled bonds. That refutes an inequality the argument would deliver on every even torus. It says nothing about the infinite-volume stiffness.
2. *Another embedding of the empty state.* Placing the empty state elsewhere than the origin of the field could give a different split. That route is not closed here.
3. *Order at the neutral scale.* The sentence is about a bound, not about order. Whether the neutral law has long-range order at large `β` is open.
4. *The six-axis menu.* Blocks 39 and 40 treat the six-axis rule. This note treats the sphere and two-valued menus, where the neutral scale has the same meaning: the empty state weighs the average of the record states.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied law, menu, scale and fugacity.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | a site empty or with one record; a site's possibilities; no dynamics in the axioms | yes |
| blocks 19, 22, 39, 40 (landed) | the domination template; `3G(0)`; the law with vacancies; the neutral scale | yes (restated) |
| probes (#8616; Grok-refereed #9114) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the sufficient bound coefficient is beta_A(c)>0; order once `(β − γ(c))ρ > 3G(0)`; no full bound at the neutral scale" | executed: the split; the occupied eigenvalues and zonal coefficients | executed: the all-site twist on all `3⁸` configurations; the record-bond twist on the ring | executed: exact structure factors at all nonzero `k` of the `2×2×2` torus, five parameter sets | executed: the neutral counterexamples with rational log bounds; the criterion's constant | T1–T2 every even torus by proof; T3 on `2×2×2`; T4 for the torus magnetization liminf; the law and scale supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "The neutral scale was chosen for a reason (block 40). If it kills the order argument, the scale is wrong."
  - *Reply:* Block 40's reasons are about binding and likelihood ratios, not order. This note shows that the two pull apart.
  - Nothing here decides the scale. It records what each choice costs.

### N8 — Cross-cycle echo
- Block 39 found reflection positivity exactly from the neutral scale up.
- Block 40 proposed the neutral scale.
- This note finds that the coefficient supplied by this proof tends to zero at that scale; no optimal stiffness is determined.

## Falsifiers

- An even torus, `c > c₀(β)` and `k ≠ 0` with `⟨|σ̂(k)|²⟩ > 1/(β_A(c)E(k))`.
- A configuration of the `2×2×2` torus where the all-site linear term differs from `E(k)Σσψ`.
- A recomputation of the neutral structure factor that differs from the stated rational.

## Boundaries and non-claims

- The law, menus, scale, fugacity and motion are supplied.
- The neutral law's order is not decided. The attempt's Theorem B and the occupation-marginal results of a2 and a4 are not used.
- No gravitational claim is made.

## Imports

- [Supplied source, block 19](ADMISSIBILITY_RULE_SPHERE_STATIC_LAW_ZERO_FIELD_COMPONENT_FOURIER_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 22](ADMISSIBILITY_RULE_CUBIC_WALK_RETURN_SUM_AND_SPHERE_STATIC_MAGNETIZATION_SUFFICIENT_BOUND_BOUNDED_THEOREM_NOTE_2026-09-15.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 39](ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 40](ADMISSIBILITY_RULE_BINDING_SCALE_PINNED_AT_THE_NEUTRAL_VALUE_PAIR_WEIGHT_IS_THE_RULES_LIKELIHOOD_RATIO_NO_BINDING_WITHOUT_A_CYCLE_ALL_BINDING_IS_AGREEMENT_AROUND_LOOPS_BOUNDED_THEOREM_NOTE_2026-09-20.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.

- `minimal_axioms`. Blocks 19, 22, 39 and 40, restated.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - the Schwarz inequality for a positive form;
  - Gaussian domination through reflection in bond planes (Fröhlich, Simon and Spencer);
  - the expansion in Legendre polynomials, with the Rodrigues form and the addition theorem;
  - the concavity of sine on `[0, π/2]`;
  - exact rational arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the seventy-fourth since the source-link direction opened; 2026-09-24. It belongs to the moving-records thread of blocks 39–40.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results (#8616). A Grok referee confirmed them (#9114).
  - The supervisor re-checked them with its own runner.
- **Before writing.**
  - Main was re-fetched, and blocks 19, 22, 39 and 40 were read as landed.
  - The own-prior-art check found the probes attempts a2–a4 of the same problem by the supervisor's model family. a3's criterion is refuted by T3(c), and a2 and a4 are not used.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_records_that_move_with_vacancies_the_infrared_stiffness_is_set_by_the_binding_scale_2026_09_24.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
