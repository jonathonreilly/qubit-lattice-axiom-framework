---
claim_id: admissibility_rule_finite_unrecorded_component_factorization_and_attachment_factors_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "Finite supplied positive static models: component factorization and conditional averaging, constancy with at most one attachment, exact single-bridge/path/spectral factors, and explicitly scoped finite graph witnesses. No universal graph iff or all-axiom-model certification."
upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.py
---

# Finite unrecorded components: factorization, attachment factors and exact marginalization witnesses

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (supplied finite probability models; unaudited)

## Result up front

For the explicitly supplied static models below, summing finite unrecorded components multiplies the recorded-site bond weight by one effective factor per component. Components with zero or one recorded attachment contribute constants. A single bridging site or a simple bridging path has the exact nonconstant factor stated below when the six-axis rule is nonconstant. General two-attachment factors have an exact spectral constancy criterion; no proof that this criterion always fails for every nonconstant rule and every component is supplied.

The genuine unit-cube and pendant examples are nearest-neighbour cubic-lattice fixtures. The three square-plus-extra-vertex values are retained as abstract-graph diagnostics: the extra vertex touches adjacent square corners, creating a triangle, so that graph cannot be a nearest-neighbour subgraph of the cubic lattice. The general factorization and conditional-average identities apply to finite graphs and justify that diagnostic separately.

The original universal graph-based iff, its unsupported cancellation argument, and claims of two complete models of all axiom sentences are deferred. No physical reading is selected. A component touching two recorded sites is not by itself a proved sufficient condition for different normalized laws in general.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Finite supplied-law marginalization; universal graph criterion and physical reading selection remain outside this theorem."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independent source review and finite evidence; independent audit remains separate."
conditional_surface_status: "Explicit finite positive models, scoped attachment factors and named graph examples only."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) provides framework context, without selecting either supplied probability convention. The [finite-window static-law source](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md) supplies the product-law reading; the [possibility-covariance source](POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md) supplies the conditional sphere/value-covariance context. These conditional inputs do not establish two models satisfying every framework requirement.

Declared objects.
- **Menus and rules.** The six-axis menu `M = {±e_1, ±e_2, ±e_3}` with the product rule `φ(v, v') = p` if `v = v'`, `q` if `v = −v'`, `r` otherwise (`p, q, r > 0`); the sphere `S²` with `φ(s, s') = e^{β s·s'}`, `β > 0`, and the rotation-invariant surface-area measure `dσ` of total mass `4π`. Both rules have **value-only covariance**: `φ(gv, gv') = φ(v, v')` for every `g` in the covariance group `G` (`O`, the 24 proper cube rotations, on `M`; `SO(3)` on `S²`), which acts transitively on the menu.
- **Sites.** A finite set `W` of recorded sites and a finite set `E` of unrecorded sites, with the nearest-neighbour graph of `Z³` restricted to `W ∪ E`; the connected components `C` of the graph induced on `E`; `∂C = {x ∈ W : x ~ a for some a ∈ C}` (the recorded sites `C` touches).
- **The three readings.** `μ_W^{(1)}(v) = Z_1^{−1} Π_{⟨xy⟩ ⊂ W} φ(v_x, v_y)` (R1, free window); `μ_{W∪E}(v, u) = Z^{−1} Π_{⟨ab⟩ ⊂ W∪E} φ` and `μ_W^{(2)}` its marginal on `W` (R2, integrated exterior); `μ_W^{(3)}(v | ω) = Z(ω)^{−1} Π_{⟨xy⟩⊂W} φ(v_x, v_y) Π_{x ∈ W, a ∈ E, x ~ a} φ(v_x, ω_a)` (R3, exterior records `ω` held; the object of blocks 17 and 23).
- **The effective factor.** `F_C(v_{∂C}) = Σ_{u ∈ M^C} Π_{⟨ab⟩ ⊂ C} φ(u_a, u_b) Π_{x ∈ ∂C, a ∈ C, x ~ a} φ(v_x, u_a)` (an integral against `dσ^C` on the sphere).
- **The spectral sectors of `φ` on `M`.** `P_0` the projector onto constants; `P_odd` onto odd functions (`f(−v) = −f(v)`, dimension `3`); `P_even` onto even functions with zero sum (dimension `2`); `Z_1 = p + q + 4r`.
- **Total variation.** `TV(μ, ν) = (1/2)Σ_v |μ(v) − ν(v)|`.


For the separately labeled abstract-graph diagnostic, replace only the cubic-lattice graph by its explicitly listed finite graph. This extension is a mathematical diagnostic, not a proposed lattice geometry. Using normalized sphere measure instead multiplies the displayed integrals by fixed constants which cancel in normalized laws.

## Theorem Q1 — factorization and the average identity

**Statement.** `μ_W^{(2)}(v) = Z^{−1} Π_{⟨xy⟩ ⊂ W} φ(v_x, v_y) Π_C F_C(v_{∂C})`, the product over the connected components `C` of `E`; and `μ_W^{(2)} = Σ_ω μ_{W∪E}(u = ω) μ_W^{(3)}(· | ω)`, the sum over the exterior configurations weighted by their marginal law.

**Proof.** A bond of `W ∪ E` lies within `W`, within a single component of `E` (two adjacent unrecorded sites are in the same component), or between `W` and a component. Summing `Π φ` over `u ∈ M^E = Π_C M^C` therefore factorizes into the `W`-bond product times `Π_C F_C`, and `F_C` depends on `v` only through `v_{∂C}`. The average identity is the definition of the conditional law: `μ_{W∪E}(v, ω) = μ_{W∪E}(ω) μ_W^{(3)}(v | ω)`, since the conditional density of `v` given `u = ω` is the `W`-bond product times the `W–E` factors with `u = ω`, normalized. ∎ (D4 checks the identity on the explicitly abstract square-plus-vertex graph.)

## Theorem Q2 — one attachment gives a constant factor

**Statement.** If `∂C = {b}` (the component touches exactly one recorded site, through any number of bonds), then `F_C(v_b)` does not depend on `v_b`. Consequently `μ_W^{(2)} = μ_W^{(1)}` whenever every component of `E` touches at most one recorded site. A component with no attachment has no recorded argument and is constant by definition.

**Proof.** For `g ∈ G`, `F_C(g v_b) = Σ_u Π_{⟨ab⟩⊂C} φ(u_a, u_b) Π_{a ~ b} φ(g v_b, u_a)`. Substitute `u_a = g u'_a` for every `a ∈ C` (a bijection of `M^C`; on the sphere the invariant measure `dσ^C` is preserved): by value-only covariance every factor returns to `φ(u'_a, u'_{a'})` or `φ(v_b, u'_a)`, so `F_C(g v_b) = F_C(v_b)`. `G` is transitive on the menu, so `F_C` is constant. A constant factor cancels between numerator and normalization in Q1. ∎ (Executed: the factor of a pendant path of two and of three unrecorded sites, symbolically in `p, q, r`, is the same polynomial for all six values of `v_b`; the plaquette with two pendant components has `TV(R1, R2) = 0` exactly at `(2, 1, 2)`: B4, D3.)

*Remark.* The soldered reading acts on sites and values jointly; the argument uses only invariance of `φ` under value rotations, which the lane's rules have (the pair relation same/antipodal/orthogonal, and `s·s'`, are invariant).

## Theorem Q3 — two attachments

**Statement.** (a) *Spectral decomposition.* On functions on `M`, `φ = Z_1 P_0 + (p − q) P_odd + (p + q − 2r) P_even`. (b) *One unrecorded site.* If `C = {a}` and `∂C = {x, y}`, then `F_C(v_x, v_y) = (φ²)(v_x, v_y) = Z_1² P_0 + (p−q)² P_odd + (p+q−2r)² P_even`, which is a constant matrix if and only if `p = q = r`; explicitly `φ²_{same} − φ²_{orth} = (p−r)² + (q−r)²` and `φ²_{anti} − φ²_{orth} = 2(p−r)(q−r)`. (c) *A path.* If `C` consists of a path of `k` internal bonds with exactly the two endpoint bonds to `x` and `y` and no other attachments, `F_C = φ^{k+2}`, constant iff `p = q = r`. (d) *In general.* For `∂C = {x, y}`, `F_C` is `G`-covariant, hence `F_C = λ_0 P_0 + λ_odd P_odd + λ_even P_even` as a matrix in `(v_x, v_y)`, and it is constant iff `λ_odd = λ_even = 0`; when `x` and `y` attach to distinct sites `a ≠ b` of `C` through single bonds, `F_C = φ T φ` with `T(u_a, u_b)` the weight of `C` with `u_a, u_b` held, itself `G`-covariant with sectors `τ_0, τ_odd, τ_even`, so `λ_odd = (p−q)² τ_odd` and `λ_even = (p+q−2r)² τ_even`. (e) *The sphere.* For `C = {a}`, `∂C = {x, y}`: `F_C = 4π sinh(β|v_x + v_y|)/(β|v_x + v_y|)` with `|v_x + v_y|² = 2 + 2 v_x·v_y`, with value `4π` at `v_x + v_y = 0` by continuity and strictly increasing in `v_x·v_y`; for `∂C = {b}` it is `4π sinh β/β`.

**Proof.** (a) For `f` on `M`, `(φf)(v) = p f(v) + q f(−v) + r Σ_{v' ⊥ v} f(v')`. If `f` is odd, `Σ_{v'⊥v} f(v') = 0` (the four orthogonal values come in antipodal pairs), so `φf = (p − q)f`. If `f` is even with zero sum, `Σ_{v'⊥v} f(v') = Σ_{all} f − f(v) − f(−v) = −2f(v)`, so `φf = (p + q − 2r)f`. Constants are eigenvectors with `Z_1`. The three sectors span all functions (dimensions `1 + 3 + 2`). (b) `F_C(v_x, v_y) = Σ_u φ(v_x, u)φ(u, v_y) = (φ²)(v_x, v_y)` since `φ` is symmetric; squaring the decomposition gives the sectors; a matrix `λ_0 P_0 + λ_odd P_odd + λ_even P_even` is constant (a multiple of `P_0`) iff `λ_odd = λ_even = 0`, i.e. `(p−q)² = 0 = (p+q−2r)²`, i.e. `p = q = r`; the entry differences follow by expanding `φ²` (executed). (c) The factor is the matrix product of `k + 2` copies of `φ`, with eigenvalues the `(k+2)`-th powers. (d) `F_C(gv_x, gv_y) = F_C(v_x, v_y)` by the substitution of Q2, so `F_C` commutes with the action of `G`; the commutant of a representation decomposing into three inequivalent irreducibles (the trivial, the odd three-dimensional and the even two-dimensional sectors, inequivalent by their dimensions and the trivial one's character) is spanned by the three projectors; the rest is (b)'s argument with `T` in place of the middle factor. (e) `∫ e^{β u·w} dσ(u) = 4π sinh(β|w|)/(β|w|)` for `w ≠ 0` (polar coordinates about `w`; `2π∫_{−1}^{1} e^{β|w|t} dt`), applied to `w = v_x + v_y` and to `w = v_b`; `sinh z/z` is strictly increasing on `z > 0` because `(sinh z/z)' = (z cosh z − sinh z)/z²` and `z cosh z − sinh z = Σ_{n≥1} 2n z^{2n+1}/(2n+1)! > 0`. ∎

Executed: the three eigenvalues with explicit eigenvectors, the entry differences and the constancy criterion (B1–B2); the path powers for `k ≤ 3` (B3); the sphere factors and the series positivity (C1–C2); two single-site components attached to the same pair of recorded sites (the two unrecorded corners of a plaquette), whose combined factor is the entrywise square of `φ²` and is nonconstant unless `p = q = r`: the entries of `φ²` are positive and squaring is injective on positive reals, so this follows from (b). E1 checks the sector formulas and a named nonconstant example; it is not an exhaustive numerical test.

## Theorem Q4 — named finite-graph witnesses

**Statement.** Exact values of `TV(μ_W^{(1)}, μ_W^{(2)})`: (a) On an abstract graph, `W` is a four-cycle and `E` one vertex joined to two adjacent cycle vertices (a triangle is present; this is not a cubic-lattice fixture): `78621/4563820` at `(3, 1, 2)`, `675203620/64463986907` at `(5, 2, 4)`, `221667/30063356` at `(2, 1, 2)`; (b) `W` the bottom face of the unit cube, `E` its top face (a four-cycle touching all four recorded sites): `9778807/1312253264` at `(3, 1, 2)`; (c) `W` a plaquette, `E` a pendant path of two sites off one corner and a pendant site off the opposite corner: `0` at `(2, 1, 2)`.

**Proof.** Enumeration of `M^{W∪E}` with integer weights and exact rational normalization; (c) is Q2. ∎ (D1–D3.)

## Conditional averaging and scope

For every finite exterior, the integrated law is a mixture of the conditional exterior-record laws with the actual exterior marginal weights. A bound on an expectation that holds uniformly for every exterior record therefore holds after averaging. This does not by itself transfer nonlinear properties or certify every result from a historical lane. A full finite torus has no exterior in this construction; no comparison of alternative infinite-volume state selections is asserted.

The two declared finite probability conventions can differ, as the valid cube example shows. The candidate clauses “sum over unrecorded possibilities” and “normalize over recorded sites alone” are descriptive alternatives, not adopted axiom readings. No all-axiom consistency or logical independence theorem follows solely from the finite witnesses.

## No-go applicability

N1: General normalized equality is equivalent to the PRODUCT of component factors being constant on recorded configurations (the base density is strictly positive). At most one attachment per component is sufficient. The converse based only on graph attachments is deferred. Distinct factors can share recorded arguments; their being written as a product does not rule out cancellation.
N2: No repository no-go wall is a premise.
N3: The rule, graph and probability convention are explicit supplied objects; no physical interpretation is hidden in the calculation.
N4: The two linked scientific parents supply conditional model context; the axiom memo is framework context. The commutant statement and sphere integration are mathematical tools stated below.
N5: Finite spectral, symbolic path, sphere-integral and rational graph calculations test the named formulas. The cube and pendant fixtures are lattice examples; the triangle-containing diagnostic is an abstract graph. No finite census proves the deferred universal converse.
N6: Neither the registered primitives nor these finite examples supply a preferred reading.
N7: General marginalization is standard. The useful content is the explicit attachment factors, exact scoped examples and conditional-average identity under the stated assumptions.
N8: The complete original source, numerical controls, historical claims and failed proof of the universal converse remain in the recovery archive.

## Boundaries and non-claims

This note proves finite component factorization, conditional averaging, at-most-one-attachment constancy, scoped bridge and path factors, and named finite graph witnesses for supplied positive static models; it does not prove a universal graph-based equivalence or select a physical reading.

No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.

The mathematical imports and supplied probability conventions are explicit; they do not establish a physical interpretation.

## Imports

The two scientific parents and framework context are linked above. The finite factorization and averaging identities are proved here. The six-axis spectral decomposition is proved directly. The general two-attachment representation uses the stated standard commutant fact for pairwise inequivalent irreducible representations (Schur); this is a mathematical import, not physical authority. The sphere integral uses polar coordinates. No imported result selects a probability convention.

## Recovery and verification

All 22 original path/mode/blob versions, original broad claims, historical control source and output, and prior review assertions are preserved in the [original recovery archive](work_history/review_loop/pr8158/README.md). Historical review and execution assertions are not current evidence. The original branch is retained for the deferred universal and physical claims.

The [runner](../scripts/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.py) and its [canonical capture](../logs/runner-cache/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.txt) provide 20 checks, including metadata and scope predicates. They do not prove the deferred graph converse. The 13 original mutation routes are preserved in source and archive; they are not rerun or claimed as fresh evidence here.

```bash
python3 scripts/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.py
```

Expected final line: `TOTAL: PASS=20 FAIL=0`.
