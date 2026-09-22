---
claim_id: admissibility_rule_formation_law_flip_identities_and_finite_mixture_witnesses_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "Exact constant-pattern flip identities and their strictness condition for the positive six-axis product rule; mixtures supported on orders with at most one recorded neighbour give the static law; finite mixture witnesses at (3,1,2), including constant-boundary unit comparisons. Universal mixture necessity and cycle or environment exclusions are deferred."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
  - admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13
runner: scripts/admissibility_rule_static_law_not_a_mixture_of_formation_laws_flip_monotonicity_2026_09_15.py
---

# Formation-law flip identities and finite mixture witnesses

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

The sequential product has an explicit ratio to its edge product. Changing one value of the constant pattern changes only normalizers whose recorded sets contain that site. The normalizer formulas below give an exact nonnegative difference and identify its strictness domain for a nonconstant rule.

Mixtures supported on orders with at most one recorded neighbour per site agree with the static law by the parent factorization. Exact finite mixtures on the path, star, rectangle and plaquette are evaluated at `(3,1,2)`. The uniform rectangle distance is `372254646387017/12790481418000000`. The original universal mixture converse and the cycle and environment exclusions remain deferred pending complete negative certification.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
artifact_role: theorem
next_trace_action: "Retain the named identities and finite witnesses; broad negative certification remains deferred."
conditional_surface_status: "Conditional on the declared six-axis menu, positive product rule and records-only reading."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
The original complete arguments and execution histories are preserved in
[the recovery manifest](work_history/review_loop/pr8150/original-manifest.json).
This source repair does not claim a completed independent audit.

## Premises and declared objects

**Axioms used (verbatim).** From
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): "There is one
fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." — "For each site, the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions." — "Records form." — "Only records are readable."

**Readings carried, named, nothing new adopted.** The records-only reading
and the sequential formation law of block 01
([`ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)):
along an order `σ` of the window `Λ` the site `x` records with its recorded
neighbours `A_x(σ)` only, `μ_σ(v) = Π_x r(v_x | v_{A_x})`,
`r(a | ∅) = 1/M`, `r(a | A) = Π_{y∈A} K(v_y, a)/K_{|A|}(v_A)`, `K(b,a) = φ(a,b)/Z_1`,
`K_k(v_A) = Σ_s Π_{y∈A} K(v_y, s)`, `K_1 ≡ 1`; block 01's Theorem B (if every
`|A_x| ≤ 1` then `μ_σ` is the static law) and its cycle lemma (on a window
with a cycle every order has a site with `|A_x| ≥ 2`, the last vertex of the
cycle to form). The census note
([`ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md`](ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md)):
Lemma L (the multiset key) and Theorem 3 (the uniform mixture on `2×3`). The
static law `Π_edges φ(v_e)/Z`. The six-axis menu, positivity, the product rule
`(p,q,r)`, `Z_1 = p + q + 4r`.

**Mixtures.** A probability `P` on the orders of `Λ`; `μ_P = Σ_σ P(σ) μ_σ`.
Every value-blind randomization of the order is of this form: the uniform
shuffle, random priorities, clocks whose rates depend on the recorded set
(the rate-clause note, PR #8148, R1), any convex combination.

**Weights and flips.** `w_σ(v) = μ_σ(v)/Π_edges K(v_e) = M^{−n_0(σ)} Π_{x: |A_x| ≥ 2} 1/K_{|A_x|}(v_{A_x})`,
`n_0(σ)` the number of sites with `A_x = ∅` (each edge's `K` appears once, at
its later endpoint; `K_1 ≡ 1`). The static law is `Π_edges K · Z_1^{|E|}/Z`, a
constant multiple of `Π_edges K`. For a value `b`, `v ≡ b` is the constant
pattern and `v^z` the pattern with site `z` set to `−b` (to a `c ⊥ b` when
`p = q`).

**The normalizer lemma (from the formation-unit note, PR #8149; re-proved).**
For `k ≥ 2`: `K_k(b,…,b) − K_k(−b,b,…,b) = ((p−q)/Z_1)[(p/Z_1)^{k−1} − (q/Z_1)^{k−1}] > 0`
for `p ≠ q` (both factors have the sign of `p − q`), and
`K_k(b,…,b) − K_k(c,b,…,b) = [(p−r)(p^{k−1} − r^{k−1}) + (q−r)(q^{k−1} − r^{k−1})]/Z_1^k > 0`
unless `p = q = r`. *Proof.* `K_k(a,b,…,b) = Σ_s K(a,s) K(b,s)^{k−1}` and
`K(b,·) − K(−b,·)` is `±(p−q)/Z_1` at `s = ±b`, zero elsewhere; likewise for
`c`. ∎

## Prior art and what is new

The linked finite-window classification supplies the sequential product and the sufficient at-most-one-recorded-neighbour factorization. The linked census supplies the multiset reduction and uniform rectangle value. The retained contribution is the explicit flip identity, its constant-boundary version and the finite mixture computations. No negative conclusion from companion work is imported.

## Exact target and obligation graph

Exact constant-pattern flip identities and their strictness condition for the positive six-axis product rule; mixtures supported on orders with at most one recorded neighbour give the static law; finite mixture witnesses at (3,1,2), including constant-boundary unit comparisons. Universal mixture necessity and cycle or environment exclusions are deferred.

Universal negative conclusions from the original version remain deferred; they are not consequences promoted by this landing surface.

## Theorem X1 — the flip lemma

**Statement.** For every finite window, every order `σ`, every value `b`, every site `z`, and a nonconstant positive triple (using the orthogonal flip when `p=q`): `w_σ(v^z) ≥ w_σ(v)`, with equality iff `z ∉ ∪_{x: |A_x(σ)| ≥ 2} A_x(σ)`.

*Proof.* `v_z` enters `w_σ` only through the factors `1/K_{|A_x|}(v_{A_x})`
with `z ∈ A_x` and `|A_x| ≥ 2` (the factor of `x = z` itself does not contain
`v_z`). In `v` every member of `A_x` equals `b`; in `v^z` the member `z`
equals `−b` (or `c`) and the others still `b`; by the normalizer lemma each
such `K` strictly decreases, so each such factor strictly increases, and no
other factor changes. ∎ Executed: every (order, site) pair of the plaquette
and of `2×3`, and every (multiset class, site) pair of the cube — `w_σ` depends
on `σ` only through the recorded sets — with strictness exactly on the
predicted pairs (B1); the lemma symbolically for `k = 2..6` (B2).

## Theorem X2 — sufficient mixtures and a difference identity

**Sufficient construction.** If every order charged by `P` has `|A_x(σ)|≤1` at every site, then `μ_P` is the static law. Each charged law equals the static law by the parent factorization, so their probability-weighted sum does also. ∎

**Difference identity.** Linearity gives
`μ_P(v^z)/Π_edges K(v^z) − μ_P(v)/Π_edges K(v) = Σ_σ P(σ)[w_σ(v^z)−w_σ(v)]`.
The summands have the signs proved in the flip lemma. The original promotion of this identity to a universal mixture necessity classification and cycle exclusion remains deferred.

**Finite evidence.** The path has 4 of 6 orders satisfying the sufficient condition; the four-leaf star has 48 of 120. Uniform and seeded pseudo-random mixtures over those orders agree exactly with the static law. The three sampled mixtures charging other orders have positive exact distances. On the rectangle the primary computes the uniform mixture and two sampled class mixtures, and on the plaquette one sampled class mixture. The recorded-set census also verifies the finite graph property on all classes of these windows and the cube. These domains do not mean every possible mixture was executed.

## Theorem X3 — constant-boundary flip identity

**Constant-boundary flip identity.** Let every fixed exterior record equal `b`. Divide the sequential unit law by the product of `K` over inside and unit–exterior edges. Normalizers depending only on exterior records contribute constants. For the inside constant pattern and an inside-site flip, every recorded set containing the flipped site has all its other values equal to `b`. The normalizer lemma therefore gives exactly the factor comparison of the flip proof, with strictness when that inside site lies in a recorded set of size at least two. ∎

The sufficient agreement condition follows by cancelling all normalizers that contain inside values when those recorded sets have size one. The primary computes all domino and path orders in the all-`+x` environment, one sampled mixture for each, and the isolated mixtures supported on qualifying orders. The original universal constant-environment mixture exclusion is deferred. This argument does not vary an arbitrary fixed exterior configuration and does not use the companion note's unsupported arbitrary-environment converse.

## X4 — the boundary

For value-dependent clocks, causal scheduling weights `W_R(σ;v)` can change with the pattern. They are products of sequential site-choice probabilities, not posterior conditional order probabilities. The displayed linear difference identity for fixed mixing weights does not remove those extra terms. This note promotes no value-dependent clock exclusion, on a plaquette or on a larger window.

## No-Go Discipline Gate

### N1 — Deferred negative certification
The original route table mixes changes of scope and non-attempts with actual arguments; it does not establish five independent exact-target attack families. Broad negative certification is withheld. The original full proofs remain byte-exact in the recovery manifest, and the original branches remain recovery handles.

### N2 — Supplied model conditions
The finite menu, positive product rule, records-only reading and any stated clock or joint-law convention are supplied mathematical conditions. The original wall-independence assertion does not complete the negative gate.

### N3 — Hidden conditions
The displayed domains govern: fixed exterior records cannot be varied inside a proof about one fixed environment. Value-blind mixing and causal value-dependent scheduling are distinct constructions.

### N4 — Actual mathematical imports
The linked finite-window classification supplies the product law and its at-most-one-recorded-neighbour sufficient condition. The linked census supplies the recorded-set multiset reduction and the quoted rectangle value. These are conditional mathematical inputs; no broader parent conclusions are imported.

### N5 — Executed resolution
The primary runner states its exact finite domains in five resolution lines. Written identities beyond those domains are checked as arguments, not executed on the infinite lattice. Historical controls have their original domains and are not relabelled as current primary execution.

### N6 — Primitive boundary
No primitive selects a rate, unit, measure over orders or boundary condition. The supplied mathematical constructions do not adopt a framework clause.

### N7 — Remaining objection
Positive identities and finite witnesses do not themselves discharge the deferred universal negative certification. Arbitrary fixed-environment necessity additionally has an unresolved proof gap.

### N8 — Recovery
The original complete proofs, including deferred arguments, are recoverable from the manifest; this narrowing does not declare their mathematical negations.

## Falsifiers

A failure of the normalizer or flip identity, its stated strictness condition, the sufficient static-mixture construction, any quoted finite exact distance, or the constant-boundary factor comparison would falsify the retained result. The primary's finite sampled mixtures are not a universal negative certificate.

## Boundaries and non-claims

This note proves flip identities and a sufficient static-mixture construction and reports finite mixture witnesses; universal mixture necessity and cycle or environment exclusions are deferred; no order, mixture, rule or coupling is selected as physical, and no clause is adopted.

No plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.

The menu, weights and mixture conventions are declared mathematical inputs, not empirical or axiom-selected values.

## Imports

The linked axiom memo supplies only its quoted sentences. The linked finite-window classification supplies the sequential product and sufficient factorization; the linked census supplies the multiset reduction and exact rectangle value. The normalizer lemma and constant-boundary comparison are proved here. No companion negative theorem is an input.

## Review record

The original author controls, checker notes, proofs and outputs are preserved byte-exact in the recovery manifest. Their historical claims are not current review authority. This corrected draft awaits the original independent reviewer's affected-source confirmation and bounded final capture; no old output is restamped.

## Verification

```bash
python3 scripts/admissibility_rule_static_law_not_a_mixture_of_formation_laws_flip_monotonicity_2026_09_15.py
python3 scripts/admissibility_rule_static_law_not_a_mixture_of_formation_laws_flip_monotonicity_2026_09_15.py --exact
python3 scripts/admissibility_rule_static_law_not_a_mixture_of_formation_laws_flip_monotonicity_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_static_law_not_a_mixture_of_formation_laws_flip_monotonicity_2026_09_15.py --mutation mixture_equals_static_claimed
```

Families: A authority and inputs; B the lemma and the flip lemma; C the mixture theorem on the path, the star, `2×3` and the plaquette, and the cycle lemma; D units in a constant environment; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 10 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=17 FAIL=0`.
