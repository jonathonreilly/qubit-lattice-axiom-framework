---
claim_id: admissibility_rule_records_that_move_with_vacancies_the_infrared_stiffness_is_set_by_the_binding_scale_long_range_order_above_the_neutral_scale_and_no_full_bound_at_it_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "WITHIN block 39's law with vacancies (a site empty or holding one content; bond kernel 1 with an empty end and c e^{beta s.s'} between records; fugacity z per record) and block 40's neutral scale, both as landed on main, carried to the sphere menu of blocks 19 and 22 as landed and to the two-valued menu; all supplied. Exact: (T1) for every beta' the bond kernel splits as a Gaussian factor in the embedded field sigma = n s (the empty state at the origin) times the same law's kernel at coupling beta - beta', and that remainder is a non-negative sum of products iff c >= c0(beta - beta'), with c0(gamma) = gamma/sinh(gamma) (sphere) or 1/cosh(gamma) (two-valued), strictly decreasing. (T2) twisting sigma at every site, empty ones included, gives the Laplacian term E(k) sum sigma psi, and on every even torus <|sigma^e(k)|^2> <= 1/(beta_A(c) E(k)) for every k != 0, every z and every component, with beta_A(c) = beta - gamma(c), c0(gamma(c)) = c (gamma = 0 for c >= 1): the stiffness is set by the binding scale, not by the density. (T3) at the neutral scale c = c0(beta), beta_A = 0 and the route gives nothing; and the full-beta bound is false there: on the 2x2x2 torus, two-valued, e^beta = 3, c = 3/5, z = 1/8, S(pi,pi,pi) = 4295671717826064002261/38505646859840596246081 with S beta E > 147/100, and at e^beta = 20, c = 40/401, z = 1/5 even S beta rho_2 E > 181/100. (T4) on Z^3 with the sphere menu M^2 >= rho - 3G(0)/beta_A(c), so long-range order of the contents holds once (beta - gamma(c)) rho > 3G(0) (3G(0) < 76/100 by block 22; G(0) <= sqrt(3) pi/8 elementary). Harvest block from a Grok-refereed probes attempt, re-checked by an independent runner. Nothing adopted; the neutral law's order at large beta is not decided; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_records_that_move_with_vacancies_the_infrared_stiffness_is_set_by_the_binding_scale_2026_09_24.py
---

# Records that move with vacancies: the infrared stiffness is set by the binding scale, long-range order holds above the neutral scale, and at it there is no full bound

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 39 and 40 as landed, carried to the menus of blocks 19 and 22 as landed; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within blocks 39 and 40 as landed on main (the law with vacancies and its neutral scale), carried to the sphere and two-valued menus of blocks 19 and 22 as landed; it reports the infrared bound for the law with vacancies and its stiffness, where it holds and where it fails; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 39, as landed, gave records that move a law with vacancies, and found that it is positive under reflection exactly when the binding scale `c` is at least a neutral value. Block 40, as landed, proposed that value as the scale. Block 19, as landed, proved an infrared bound for the static law with no vacancies, and block 22 gave its constant. This note asks whether the contents of *moving* records line up over long distances, and what the binding scale has to do with it.

- **T1: the split.**
  - The bond kernel factors into a Gaussian in the records' field `σ = ns`, with the empty state at the origin, times the same law at a weaker coupling `β − β'`.
  - That remainder is a sum of products with non-negative weights exactly when `c ≥ c₀(β − β')`.
- **T2: the stiffness is set by the scale.**
  - The twist that produces the structure factor has to move the *empty* sites too.
  - On every even torus, `⟨|σ̂(k)|²⟩ ≤ 1/(β_A(c)E(k))`, with `β_A(c) = β − γ(c)` and `c₀(γ(c)) = c`.
  - Above `c = 1` this is block 19's full bound. Between the neutral scale and `1` it is weaker by exactly `γ(c)`.
  - The density does not enter.
- **T3: at the neutral scale the route closes, and the full bound is false.**
  - At `c = c₀(β)`, `β_A = 0`.
  - On the `2×2×2` torus the full-`β` bound fails exactly, and so does the bound with the bond density.
- **T4: long-range order above the neutral scale.**
  - On `Z³` with the sphere menu, `M² ≥ ρ − 3G(0)/β_A(c)`.
  - So the contents of moving records line up over long distances once `(β − γ(c))ρ > 3G(0)`, and `3G(0) < 76/100` (block 22).

In plain terms, records that wander and bind to each other can still line up their contents across the whole lattice, provided they bind more strongly than a neutral amount. The margin above neutral is what sets how stiff the alignment is. At exactly the neutral binding that block 40 proposed, an empty neighbour counts for as much as a record of random content. The argument then gives nothing, and the stiffness it would need is provably absent. Whether records at the neutral binding line up at all is left open here.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "A site never carries more than one record; records are permanent." A site is empty or holds one content. Records that move are the owner's reading, and that reading is supplied.
  - "Each site has a domain of local possibilities." Here that is the menu of contents.
  - "Admissibility is not a dynamics axiom." The motion, the scale, the fugacity and the law with vacancies are supplied clauses. Nothing is adopted.
- **The law with vacancies** (block 39 T5 as landed). The states of a site are `∅` or a content `s`.
  - The a priori weight is `1` for `∅` and `z` times the menu's measure for contents.
  - The bond kernel is `B(∅, ·) = B(·, ∅) = 1` and `B(s, s') = c e^{βs·s'}`.
  - The law is `∝ Π_b B(u_x, u_y)` on an even torus, with one bond per site and direction. On a side of two the pair is joined twice.
- **Menus.** The sphere menu has `s ∈ S²` with the uniform measure (blocks 19 and 22 as landed). The two-valued menu has `s = ±1` with counting measure.
- **Fields.** `σ_x = n_x s_x`, with `n_x = 1[x occupied]`. Also `σ̂^e(k) = N^{−1/2}Σ_x e^{ik·x}σ_x·e` and `E(k) = Σ_i 2(1 − cos k_i)`. The densities are `ρ = ⟨n_x⟩` and, on a bond, `ρ₂ = ⟨n_xn_y⟩`.
- **Scales.** `c₀(γ) = γ/sinh γ` (sphere) or `1/cosh γ` (two-valued), with `c₀(0) = 1`.
  - For `c₀(β) ≤ c < 1`, `γ(c)` is the root of `c₀(γ) = c`. For `c ≥ 1`, `γ(c) = 0`.
  - `β_A(c) = β − γ(c)`.
  - Block 40's neutral scale, carried to these menus, is `c₀(β)` (block 39 T5 as landed gives it for the sphere).
- **Named standard results**, used at definition level: the Schwarz inequality for a positive form; the expansion of `e^{γt}` in the sphere's zonal functions (Legendre polynomials, with the Rodrigues form of their coefficients and the addition theorem); Gaussian domination through reflection in bond planes (Fröhlich–Simon–Spencer), re-proved at this scope in the attempt.

## Theorem T1 — the split and the positivity threshold

*Statement.*
- (a) For every `β'`, `B(u, u′) = e^{(β′/2)(n+n′)} e^{−(β′/2)|σ−σ′|²} R_{β−β′}(u, u′)`. Here `R_γ` is the law's kernel with the same `c` and coupling `γ`.
- (b) `R_γ` is a sum of products with non-negative coefficients iff `c ≥ c₀(γ)`.
  - Two-valued: `R_γ = 1 + (c cosh γ − 1)nn′ + (c sinh γ)(ns)(n′s′)`. The occupied part of the kernel, after the empty state is removed, has eigenvalues `2c cosh γ − 2` and `2c sinh γ`.
  - Sphere: the zonal coefficients of `e^{γt}` are all positive, and the constant one is `sinh γ/γ`.
- (c) `c₀` decreases strictly from `1`.

*Proof.*
- (a) `|σ − σ′|² = n + n′ − 2nn′ s·s′`, since `n² = n` and `|s| = 1`. If `nn′ = 0` both sides are `1`. Otherwise `e^{β′}e^{−β′(1 − s·s′)}ce^{(β−β′)s·s′} = ce^{βs·s′}`.
- (b)
  - Two-valued: `e^{γss′} = cosh γ + ss′ sinh γ`. Removing the empty row and column leaves `R − 1` restricted to records, and its eigenvalues are as stated.
  - Sphere: each zonal coefficient is a positive multiple of `∫(1 − t²)^ℓe^{γt}dt > 0`. By the addition theorem each term is a sum of products. Only the constant term competes with the empty state, through `c·sinh γ/γ − 1`.
  - The converse is block 39 T5 as landed.
- (c) `d(1/cosh γ)/dγ = −sinh γ/cosh²γ`. Also `d(γ/sinh γ)/dγ = (sinh γ − γ cosh γ)/sinh²γ < 0`, because `d(sinh γ − γ cosh γ)/dγ = −γ sinh γ`.

∎

*Checked (B1).*
- The split for the four occupation pairs, symbolically.
- The occupied eigenvalues.
- The zonal coefficients for `ℓ ≤ 3`, and the constant one.
- The derivatives.
- The rational neutral values `1/cosh(ln 3) = 3/5` and `1/cosh(ln 20) = 40/401`.

## Theorem T2 — the stiffness is set by the binding scale

*Statement.*
- (a) Replace `σ_x` by `σ_x − φ_xe` at every site, empty ones included, in the Gaussian factor of T1(a). For `φ = λψ` with `ψ` a plane wave, the linear term is `λβ′E(k)Σ_xσ_x^eψ_x`. Twisting only the bonds between two records does not give this term.
- (b) On every even torus, for every `z`, every component `e` and every `k ≠ 0`, `⟨|σ̂^e(k)|²⟩ ≤ 1/(β_A(c)E(k))`. For `c ≥ 1` this is block 19's bound `1/(βE(k))`.

*Proof.*
- (a) Sum by parts over the bonds. `ψ` is an eigenfunction of the lattice Laplacian with eigenvalue `E(k)`.
- (b) Take `β′ = β_A(c)`, so that `c ≥ c₀(β − β′)` by T1(c).
  - By T1(b) every crossing factor of a reflection through a bond plane is a sum of products with non-negative weights, for every pair of twists.
  - So the twisted partition function obeys `Z(φ)² ≤ Z(φ⁺)Z(φ⁻)`, where `φ±` copy one half onto the other.
  - A maximiser with the fewest non-constant bonds is therefore constant, and `Z(φ) ≤ Z`.
  - Expanding to second order in `λ` gives the bound. The fugacity enters only the site measures.

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

*Reading.* At the neutral scale an empty neighbour weighs what a record of random content weighs on average (block 40 T1 as landed). Records then gain nothing from lining up with a neighbour rather than leaving the site empty. The structure factor stays near `ρ` even at the largest wave numbers, so no bound with a stiffness of order `β` can hold.

## Theorem T4 — long-range order above the neutral scale

*Statement.* On `Z³` with the sphere menu, as the torus limit of T2 (as in block 19):
- `M² ≥ ρ − 3G(0)/β_A(c)`, where `M²` is the limit of the torus magnetization square.
- So long-range order of the contents holds once `(β − γ(c))ρ > 3G(0)`.
- `3G(0) < 76/100` (block 22 as landed). An elementary bound is `G(0) ≤ √3π/8`.

*Proof.*
- The sum rule `Σ_eΣ_k⟨|σ̂^e(k)|²⟩ = Nρ` together with T2 gives `M_N² ≥ ρ_N − (3/β_A)N^{−1}Σ_{k≠0}1/E(k)`. The lattice sum tends to `G(0)` as the torus grows.
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
conditional_surface_status: "T1-T2 on every even torus; T3 exact on the 2x2x2 torus; T4 on Z^3 through the torus limit; the menu, motion, scale and fugacity supplied"
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

  All reference only.
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
| "the stiffness is `1/β_A(c)`; order once `(β − γ(c))ρ > 3G(0)`; no full bound at the neutral scale" | executed: the split; the occupied eigenvalues and zonal coefficients | executed: the all-site twist on all `3⁸` configurations; the record-bond twist on the ring | executed: exact structure factors at all nonzero `k` of the `2×2×2` torus, five parameter sets | executed: the neutral counterexamples with rational log bounds; the criterion's constant | T1–T2 every even torus by proof; T3 on `2×2×2`; T4 on `Z³` through the torus limit; the law and scale supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "The neutral scale was chosen for a reason (block 40). If it kills the order argument, the scale is wrong."
  - *Reply:* Block 40's reasons are about binding and likelihood ratios, not order. This note shows that the two pull apart.
  - Nothing here decides the scale. It records what each choice costs.

### N8 — Cross-cycle echo
- Block 39 found reflection positivity exactly from the neutral scale up.
- Block 40 proposed the neutral scale.
- This note finds that the order argument's stiffness is the margin above that scale, and vanishes at it.

## Falsifiers

- An even torus, `c > c₀(β)` and `k ≠ 0` with `⟨|σ̂(k)|²⟩ > 1/(β_A(c)E(k))`.
- A configuration of the `2×2×2` torus where the all-site linear term differs from `E(k)Σσψ`.
- A recomputation of the neutral structure factor that differs from the stated rational.

## Boundaries and non-claims

- The law, menus, scale, fugacity and motion are supplied.
- The neutral law's order is not decided. The attempt's Theorem B and the occupation-marginal results of a2 and a4 are not used.
- No gravitational claim is made.

## Imports

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
