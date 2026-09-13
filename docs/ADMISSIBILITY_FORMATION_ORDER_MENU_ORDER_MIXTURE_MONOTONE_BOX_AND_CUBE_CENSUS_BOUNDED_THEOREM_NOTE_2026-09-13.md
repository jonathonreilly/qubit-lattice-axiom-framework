---
claim_id: admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "On the six Bloch-axis projector menu inside M_2(C), for a covariant positive nearest-neighbor rule of product class (P) with orbit weights (p, q, r) and constant covariant prior, the formation law of a formation order sigma on a finite window is fixed by the multiset K(sigma) of recorded-neighbour sets of size at least two (Lemma L, a corollary of the landed identity B1): mu_sigma = W / (M^a0 Z_1^a1 prod_{A in K} Z(v|A)). The map K -> law is injective on every declared window and rule: path3, P4, star4, cycle4 give 2, 3, 5, 4 laws (the landed census); the 2x3 rectangle gives 28 multisets and 28 laws over its 720 orders and 98 acyclic orientations; the open 2x2x2 cube gives 542 multisets and 542 laws over its 40,320 orders and 1,862 acyclic orientations, at both triples (3,1,2) and (5,2,4) and for the declared binary Ising-type kernel with e^J = 2. The monotone-box orders (5 and 48 linear extensions of the product partial order) give one law each, shared by 48 and 120 orders; on the rectangle the reversed order gives the same law because the point reflection fixes the multiset, on the cube it does not (TV 8207/7830108 at (3,1,2)). The uniform order mixture differs from the static law and from the monotone law on both windows, with exact total variations on the rectangle and exact positive pointwise gaps on the cube. The adjacent-pair exchange identity holds only at empty backgrounds for the menu rules and everywhere for the constant rule. Exact arithmetic throughout; no infinite-volume statement; no selection of a rule, coupling, order or reading."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
  - admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_bounded_theorem_note_2026-09-07
runner: scripts/admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_2026_09_13.py
---

# The formation law of a product-class nearest-neighbor rule is fixed by its multiset of recorded-neighbour sets of size at least two, and the order census on the 2x3 rectangle and the 2x2x2 cube gives exactly 28 and 542 laws

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained
**Audit:** unset; the independent audit lane owns any verdict.
**Primary runner:**
[`scripts/admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_2026_09_13.py`](../scripts/admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_2026_09_13.py)
**Pinned cache:**
[`logs/runner-cache/admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_2026_09_13.txt`](../logs/runner-cache/admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_2026_09_13.txt)

## Result up front

Take one fixed nearest-neighbor rule of the product class and grow records on
a finite patch one site at a time. The landed classification note showed that
the pattern law depends on the order in which the records form, and counted
the distinct laws on four small windows. This note says exactly which feature
of an order the law remembers, and finishes the count on the two windows the
campaign asked for.

The law remembers one thing: for each site, the set of its neighbours that
already carried records when it formed, but only when that set has two or more
members. A site that formed with no recorded neighbour or with one recorded
neighbour contributes a constant factor (the menu size `M`, or the one-neighbour
normalizer `Z_1 = p + q + 4r`), so it drops out of the comparison between
orders. Two orders with the same multiset of recorded-neighbour sets of size at
least two give the same law (Lemma L). On every window and rule declared here
the converse also holds: different multisets give different laws (Theorem 1).
Counting multisets therefore counts laws. On the `2x3` rectangle the 720 orders
induce 98 acyclic orientations, 28 multisets and 28 laws. On the open `2x2x2`
cube the 40,320 orders induce 1,862 acyclic orientations, 542 multisets and
542 laws. The four small windows of the landed census fall out as 2, 3, 5 and 4
multisets, matching the landed law counts.

Two consequences. First, the monotone-box order (records growing along the
product partial order, the landed 2D object of the 2026-09-07 note) is one law
shared by 48 of the 720 rectangle orders and 120 of the 40,320 cube orders,
while only 5 and 48 of those orders are linear extensions of the product order.
On the rectangle the reversed order gives the same law, because the point
reflection of the rectangle carries the row-major order to its reverse and
fixes the multiset `{{1,3},{2,4}}`; on the cube the point reflection carries the
monotone multiset `{{1,2},{1,4},{2,4},{3,5,6}}` to `{{1,2,4},{3,5},{3,6},{5,6}}`,
a different multiset, so the reversed order gives a different law. Their total
variation is `8207/7830108` at `(3,1,2)` and `78076639367/38683213526034` at
`(5,2,4)`. The two-dimensional coincidence is a symmetry of the rectangle, not
a property of formation orders. Second, the uniform mixture over all orders is
neither the static law nor the monotone law on either window: on the rectangle
its total variation from the static law is `372254646387017/12790481418000000`
(about `0.0291`) at `(3,1,2)`, and on the cube its pointwise distance from the
static law exceeds `468324690921/13849151214080000` (about `3.4e-5`). The
mixture is a witness-generating device, not a candidate law: the realized-state
primitive supplies no measure over orders, and nothing here supplies one.

No order is selected as physical. No rule, coupling or reading is selected. The
axioms supply no order; whatever fixes the order is physics the axioms leave
open, and this note measures how much of the pattern law that open physics
carries: on the cube, 542 laws from one rule.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "what the Admissibility rule induces on the infinite lattice — the framework-level action — is unidentified (owner sequencing rule 2026-08-26); the parked statistical-bridge decision wakes on 'the committed-action identification lands', which this note does not fire"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "carry the multiset key to the 3x3 window and to the handed census (which recorded-neighbour multisets are realized by translation-covariant order families); state the minimal clause on orders that would collapse the 542 cube laws to one, as an owner decision, not an adoption"
conditional_surface_status: "if a clause fixing the formation order or a covariant law over orders were supplied, Lemma L reduces its content on any finite window to a distribution over multisets of recorded-neighbour sets; no such clause is supplied here"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "every statement is an exact finite computation or an algebraic corollary of the landed identity B1 on declared windows, rules and orders; no order, rule, coupling or reading is selected and no infinite-volume object is constructed"
```

## Premises and declared objects

**Axiom text used (quoted from `docs/MINIMAL_AXIOMS_2026-06-29.md` on `main`
at `b8c9d9d819`).** Admissibility: "There is one fixed nearest-neighbor
admissibility rule, covariant under lattice translations and proper cubic
rotations. For each site, the probability distribution over the possibilities
is determined by, and varies with, the nearest-neighbor conditions." Record:
"Records form." "Only records are readable." "records are permanent". The
reading note that the distribution "does not supply the formation site,
probability, or rate" is the reason every statement below quantifies over
orders or names a declared order family. The realized-state primitive (live
supplied foundation, `docs/audit/data/axiom_premise_nodes.json`) forbids
"averaging over alternatives"; it is cited only to fix the status of the
uniform order mixture as a device.

**Menu M.** The six Bloch-axis projectors `P(±e_a) = (I ± σ_a)/2` inside
`M_2(C)`, `M = 6`. The 24 proper cubic rotations act as signed axis
permutations and preserve the three pair orbits, labelled by
`Tr(PP') ∈ {1, 0, 1/2}`: parallel (6 ordered pairs), antiparallel (6),
orthogonal (24). Rebuilt and checked by the runner (family B).

**Rules.** Class (P): `r(s | η) ∝ ψ(s) Π_{y∈A} φ(s, η_y)` with `φ` symmetric,
positive and isotropic, taking the orbit values `(p, q, r)`; `ψ` covariant
hence constant. Triples `(3,1,2)` and `(5,2,4)`; the constant rule `(2,2,2)`
as the boundary case. The one-neighbour normalizer `Z_1 = Σ_s φ(s,t) = p + q +
4r` is independent of `t`: `12` at `(3,1,2)`, `23` at `(5,2,4)`. The binary
Ising-type kernel of the concurrent note (below), `φ(s,t) = 4` if `s = t` and
`1` otherwise on `{0,1}`, `M = 2`, `Z_1 = 5`, is carried as a declared witness
kernel only; it is a class-(P) rule on a two-element menu and is not the
Admissibility rule.

**Windows.** path3 (edges 0-1, 1-2), P4 (0-1, 1-2, 2-3), star4 (0-1, 0-2,
0-3), cycle4 (0-1, 1-2, 2-3, 3-0), the `2x3` rectangle (sites `3r + c`, 7
edges), the open `2x2x2` cube (sites `4x + 2y + z`, 12 bit-flip edges, degree
3). Records-only reading: a site's condition is the values of its recorded
neighbours; unrecorded neighbours do not enter. No exterior records.

**Formation law.** For a total order `σ = (x_1, …, x_n)` of a window `W`, the
recorded-neighbour set of `x_k` is `A_k = N(x_k) ∩ {x_1, …, x_{k−1}}`, and the
formation law is `μ_σ(v) = Π_k r(v_{x_k} | v restricted to A_k)`, exactly the
"FORMATION law of a rule for a formation order" of the classification note.
The static law is `μ(v) = W(v)/Z_W` with `W(v) = Π_{xy∈E} φ(v_x, v_y)` and
`Z_W = Σ_v W(v)`; it is the joint law whose full conditionals are the rule
with every neighbour recorded (Theorem A of the classification note, cited).

**Declared order families.** Every order (`n!`), the monotone-box class (the
linear extensions of the product partial order on the rectangle and the cube,
"every linear extension of the product partial order" in the words of the
2026-09-07 note, here in three dimensions for the first time), the row-major
order and its reverse, and the named orders of the concurrent note: ends-first
`(0,2,1)` on path3, cyclic `(0,1,2,3)` and opposite-corners `(0,2,1,3)` on
cycle4, corners-first `(0,2,3,5,1,4)` on the rectangle.

**Configuration family F (cube).** The reference `(0,…,0)`, its 40 one-site
and 700 two-site changes, and 300 draws of the fixed linear congruential
generator (seed `20260913`, multiplier `1103515245`, increment `12345`,
modulus `2^31`, value `(state >> 16) mod 6`), de-duplicated. F is scaffolding
for separating cube laws cheaply; where F already separates two multisets no
full pass is needed, and the runner reports the groups still ambiguous after F
(there are none).

## Prior art and what is new

[The classification note](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)
(unaudited; its own status field reads proposed_retained) proves the identity
`μ_σ(v) · Π_k Z_k(v_{A_k}) = μ(v) · Z_W` (its B1), the one-neighbour constancy
of the normalizer (D7), the criterion `μ_σ = μ` iff every `|A_k| ≤ 1` (B2), the
census "path3 2 laws (4,2), P4 3 (8,8,8), star4 5 (12,6,2,2,2), cycle4 4
(8,8,4,4)" (B5), and the cycle4 uniform-mixture gaps `899/2341664` and
`3478458125/23066700436908` (E5). It states that the formation law "is not a
nearest-neighbor field of the static kind" (E4c). Everything in this paragraph
is cited, not re-claimed.

[The monotone-order note](ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md)
(unaudited) proves that "every linear extension of the product partial order
(every monotone order) gives one formation law" on the `2x3`, `3x3`, `3x4` and
`4x4` rectangles, and computes its corner law. It is two-dimensional
throughout.

[The infinite-strip note](ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md)
(unaudited) treats a row sweep on a strip; it does not use a multiset key.

**Concurrent work, not upstream.** An open sister pull request (branch
`physics-loop/formation-order-covariance-20260913`, PR 8096, note
`docs/FORMATION_ORDER_COVARIANCE_AND_ISOTROPIC_BINARY_ORDER_BLIND_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-13.md`)
proves that no total order on `Z^3` is invariant under a non-identity proper
rotation, characterizes order-blind interior binary rules as the constant
rules, states the adjacent-pair exchange identity, and computes a binary
Ising-type witness: "path3 chain versus ends-first differs on all 8
configurations with total variation 9/50 and all-minus masses 8/25 versus
4/17; the 24 plaquette orders collapse to 4 laws and cyclic versus
opposite-corners has total variation 9/50; the 720 orders on the 2x3 window
give twenty-eight laws, and corners-first versus row-major differs on 44 of 64
configurations with total variation 135/578". Its four separating clauses are
recorded there as owner options, not adopted. None of that is claimed here.
Its binary numbers are re-derived below by a different implementation path
(the multiset denominator rather than the sequential product) as an
independence check, and its "row-major = reverse" observation receives its
reason.

**New here.** (i) Lemma L: the law-determining data of an order is the
multiset of recorded-neighbour sets of size at least two, with the explicit
denominator `M^a0 · Z_1^a1 · Π_{A∈K} Z(v|A)`. (ii) Theorem 1: the multiset-to-law
map is injective on every declared window and rule, so the census of laws is
the census of multisets: 28 on the rectangle, 542 on the cube, with the
acyclic-orientation counts 98 and 1,862 as upper bounds. (iii) Theorem 2: the
monotone-box class in three dimensions (48 linear extensions, 120 orders
sharing the law), the point-reflection explanation of the rectangle's
reverse-order coincidence and its failure on the cube with exact total
variations. (iv) Theorem 3: exact distances between the uniform order
mixture, the static law and the monotone law on the rectangle, and exact
positive lower bounds on the cube. (v) Theorem 4: the exchange-identity census
on the menu rules and the constant rule. (vi) Theorem 5: the binary witness
numbers re-derived from the denominator form, with the cycle4 ratio
`M · Z(v_0, v_2) / Z_1^2 ∈ {34/25, 16/25}` in closed form.

## Exact target and obligation graph

**Target.** For every finite window `W`, class-(P) rule with constant prior
and symmetric `φ`, and total order `σ`, express `μ_σ` through `K(σ)`; on the
declared windows and rules decide whether `K ↦ μ_K` is injective and count the
laws; compute the monotone-box class, the reversed order, the uniform mixture
and the exchange identity exactly.

| obligation | disposition |
| --- | --- |
| identity `μ_σ · Π_k Z_k = μ · Z_W` | cited (classification note B1); re-proved here at scope as the chain rule of the product form |
| one-neighbour normalizer constant | cited (classification note D7); re-checked (C1) |
| Lemma L, the multiset key | proved here (corollary of B1 and D7) |
| every acyclic orientation is order-induced; counts 4, 8, 8, 14, 98, 1862 | executed (B5) |
| linear extensions of the product order: 5 (rectangle), 48 (cube) | executed (B6); the 5 matches the 2026-09-07 note |
| small-window census equals the landed B5 | executed (D1) |
| injectivity on the rectangle: 28 multisets, 28 laws at both triples and for the binary kernel | executed (D3, D4, E3) |
| injectivity on the cube: 542 multisets, 542 laws at both triples | executed (D13, D14, D15): F separates every pair of multisets, so no full-pass resolution was needed |
| monotone-box class sizes 48 and 120; rectangle reverse shares the multiset; cube reverse does not | executed (D5, D6, D16, D17) |
| exact TV(μ_P, μ), TV(μ_P, μ_rev) on the cube by a full pass | executed (D18, D19) |
| exact TV(μ_P, μ), TV(μ̄, μ), TV(μ̄, μ_P), max gap, spread on the rectangle | executed (D7 to D11) |
| positive lower bounds `max_F |μ̄ − μ|`, `max_F |μ̄ − μ_P|` on the cube | executed (D20, D21) |
| cycle4 mixture gap reproduces the landed E5 | executed (D2) |
| static partition function on the cube by two methods | executed (C5) |
| exchange identity census | executed (D22) |
| binary witness numbers of the concurrent note | executed by the denominator path (E1 to E4) |
| infinite-volume law, existence or uniqueness | referenced only; not used and not proved |
| `3x3` window (design target) | open; not this note (the `9!` orders and `6^9` configurations exceed the declared budget) |
| a physical order, a covariant law over orders, a clause | open; not this note |

## Lemma L — the law-determining data of a formation order

**Statement.** Let `W` be a finite graph, `φ` symmetric positive on the menu,
`ψ` constant, and `σ` a total order of the sites. Write `Z(v|A) = Σ_s Π_{y∈A}
φ(s, v_y)` for the normalizer of a site whose recorded neighbours carry the
values `v|A`, with `Z(∅) = M` and `Z(v|{a}) = Z_1` for every value. Let
`K(σ)` be the multiset `{{ A_k : |A_k| ≥ 2 }}`, `a1` the number of `k` with
`|A_k| = 1` and `a0` the number with `|A_k| = 0`. Then

`μ_σ(v) = W(v) / ( M^a0 · Z_1^a1 · Π_{A∈K(σ)} Z(v|A) )`,

with `a1 = |E| − Σ_{A∈K(σ)} |A|` and `a0 = n − a1 − |K(σ)|`. Hence `μ_σ`
depends on `σ` only through `K(σ)`, and two orders with equal multisets have
equal laws.

**Proof.** Each factor of the formation product is `r(v_{x_k} | v|A_k) =
Π_{y∈A_k} φ(v_{x_k}, v_y) / Z(v|A_k)`, the constant `ψ` cancelling. Every edge
`xy` of `W` appears exactly once in the numerator, at the later of its two
endpoints, so the numerators multiply to `W(v)`. The denominators multiply to
`Π_k Z(v|A_k)`; the factors with `|A_k| = 0` equal `M`, those with `|A_k| = 1`
equal `Z_1` by the one-neighbour constancy, and the rest are indexed by `K(σ)`.
The edge count `Σ_k |A_k| = |E|` gives `a1`, and `n = a0 + a1 + |K|` gives
`a0`. This is the landed identity B1 with the constant factors made explicit.
The runner checks the closed form against the sequential product on every
order and configuration of the four small windows and the rectangle: 424,320
evaluations, 0 mismatches (C2). ∎

**Remark (orientations).** The sets `A_k` are the in-neighbourhoods of the
acyclic orientation of `W` induced by `σ` (orient each edge from the earlier
to the later site). Every acyclic orientation arises from some order (any
linear extension of it), so the number of laws is at most the number of
multisets, which is at most the number of acyclic orientations. The runner
enumerates the acyclic orientations directly and confirms they coincide with
the order-induced ones: 4, 8, 8, 14, 98, 1,862 on path3, P4, star4, cycle4,
rectangle, cube (B5). On a tree every orientation is acyclic and `Z_W = M ·
Z_1^(n−1)`; the orders with `μ_σ = μ` are those with `K(σ) = ∅`, counted 4,
8, 12, 0 on the four small windows (C4), as in the landed B2 and B3.

## Theorem 1 — the multiset determines the law, and the census

**Statement.** On path3, P4, star4, cycle4, the `2x3` rectangle and the
`2x2x2` cube, for the rules `(3,1,2)`, `(5,2,4)` and the binary kernel, the
map `K ↦ μ_K` is injective. The census of laws therefore equals the census of
multisets:

| window | orders | acyclic orientations | multisets = laws | class sizes (orders per law) |
| --- | --- | --- | --- | --- |
| path3 | 6 | 4 | 2 | (4, 2) |
| P4 | 24 | 8 | 3 | (8, 8, 8) |
| star4 | 24 | 8 | 5 | (12, 6, 2, 2, 2) |
| cycle4 | 24 | 14 | 4 | (8, 8, 4, 4) |
| `2x3` rectangle | 720 | 98 | 28 | 48 for the monotone-box law |
| `2x2x2` cube | 40,320 | 1,862 | 542 | 120 for the monotone-box law |

The four small rows reproduce the landed B5 exactly (D1). For the constant
rule `(2,2,2)` every normalizer table is constant and there is one law on
every window (D12); for the binary constant rule there is one law over the 720
rectangle orders (E4).

**Proof.** Lemma L gives at most one law per multiset. For the rectangle the
runner accumulates, in one pass over the `6^6` configurations, the static
weight `W(v)` keyed by the tuple of the 28 denominators `D_K(v)`; the
signature of a multiset is its column of denominators, and 28 distinct
signatures were found at each triple (D4), as were 28 distinct laws for the
binary kernel (E3). For the cube, evaluating the 542 denominators on the
family F separates every pair of multisets at both triples (D15 reports no
ambiguous group), which is already a proof of injectivity since a single
configuration with distinct denominators gives distinct laws (the numerators
agree). Each law sums to one (C3), and the cube partition function
`Z_W(3,1,2) = 6982520832` computed by a face-by-face contraction equals the
full pass (C5). ∎

## Theorem 2 — the monotone-box class in three dimensions, and the reversed order

**Statement.** (a) The product partial order has 5 linear extensions on the
rectangle and 48 on the cube (B6). Every linear extension induces the same
orientation (each edge from the smaller to the larger site) hence the same
multiset and the same law `μ_P`; the multiset is `{{1,3},{2,4}}` on the
rectangle and `{{1,2},{1,4},{2,4},{3,5,6}}` on the cube. The law `μ_P` is
shared by 48 of the 720 rectangle orders and by 120 of the 40,320 cube orders
(D6, D17), so the monotone class is a proper subclass of the orders giving its
law. Every cube order has a largest recorded-neighbour set of size exactly 3
(B7).

(b) The point reflection `g` (site `i ↦ 5 − i` on the rectangle, `i ↦ 7 − i`
on the cube) is a graph automorphism carrying the row-major order to its
reverse, so `μ_rev = μ_P ∘ g^{−1}` on both windows, and `μ` is `g`-invariant.
On the rectangle `g` fixes the multiset `{{1,3},{2,4}}`, so `μ_rev = μ_P`
(D5): the reverse order and the row-major order are the same law. On the cube
`g` carries the monotone multiset to `{{1,2,4},{3,5},{3,6},{5,6}}`, a different
multiset (D16), so by Theorem 1 `μ_rev ≠ μ_P`. Exactly:

| quantity | `(3,1,2)` | `(5,2,4)` |
| --- | --- | --- |
| `TV(μ_P, μ) = TV(μ_rev, μ)` on the cube | `1182193085/23402354976` (about `0.0505`) | `180429904845630987241/6061376968596116197338` (about `0.0298`) |
| `TV(μ_P, μ_rev)` on the cube | `8207/7830108` (about `1.05e-3`) | `78076639367/38683213526034` (about `2.02e-3`) |
| `TV(μ_P, μ)` on the rectangle | `166597/6750000` (about `0.0247`) | `18031280990/1152766563947` (about `0.0156`) |

The equality `TV(μ_P, μ) = TV(μ_rev, μ)` on the cube is the `g`-invariance of
`μ`; the inequality `TV(μ_P, μ_rev) > 0` is the failure of `g` to fix the
multiset. The rectangle's coincidence is a symmetry of the `2x3` window, not
a statement about formation orders.

**Proof.** (a) is the acyclic-orientation remark of Lemma L applied to the
product order; the counts are exact enumerations. (b) For any automorphism `g`
and order `σ`, `K(g∘σ) = g(K(σ))` and `μ_{g∘σ}(v) = μ_σ(g^{−1} v)` because `φ`
and the edge set are `g`-invariant; the row-major order reversed is the
row-major order composed with the point reflection on both windows. The
multisets are read off directly (D5, D16) and the total variations are
computed by a full pass over `6^8 = 1,679,616` cube configurations keyed by the
pair of denominators (D18, D19). ∎

## Theorem 3 — the uniform order mixture against the static and monotone laws

**Statement.** Let `μ̄ = (1/n!) Σ_σ μ_σ = Σ_K (c_K / n!) μ_K`, where `c_K` is
the number of orders with multiset `K`. On the rectangle, exactly:

| quantity | `(3,1,2)` | `(5,2,4)` |
| --- | --- | --- |
| `TV(μ̄, μ)` | `372254646387017/12790481418000000` (about `0.0291`) | `6628058424854510226272127920221/381356895652498781589963821562900` (about `0.0174`) |
| `TV(μ̄, μ_P)` | `44446481797/2046477026880` (about `0.0217`) | `201171497997761809454557/14788697255605118189282400` (about `0.0136`) |
| `max_v |μ̄(v) − μ(v)|` | `8535587/105456000000` (about `8.1e-5`) | `75088901087821671875/3583863012400439488911216` (about `2.1e-5`) |
| spread `max_K TV(μ_K, μ)` | `16549/281250` (about `0.0588`) | `125508731/3410832276` (about `0.0368`) |

On the cube, over the family F (a lower bound on the maximum over all
configurations, and positive, so `μ̄ ≠ μ` and `μ̄ ≠ μ_P` exactly):

| quantity | `(3,1,2)` | `(5,2,4)` |
| --- | --- | --- |
| `max_F |μ̄(v) − μ(v)|` | `468324690921/13849151214080000` (about `3.4e-5`) | `1083259980382858024033073095703125/238113505325368709377379573647456927296` (about `4.5e-6`) |
| `max_F |μ̄(v) − μ_P(v)|` | `3230469/511813120000` (about `6.3e-6`) | `221362490334912109375/252089923069262577014315712` (about `8.8e-7`) |

On cycle4 the same computation reproduces the landed E5 gaps `899/2341664`
and `3478458125/23066700436908` (D2), fixing the convention: free window, no
exterior records, records-only reading.

**Proof.** By Lemma L, `μ̄(v) = W(v) · Σ_K (c_K / n!) / D_K(v)`, so one pass
keyed by the denominator tuple gives every quantity exactly; the rectangle's
pointwise maximum is attained at the largest weight within each denominator
class. The cube values restrict the same formula to F. ∎

**Status of `μ̄`.** The mixture is a witness-generating device. The
realized-state primitive forbids averaging over alternatives, and the axioms
supply no measure over orders; `μ̄` would be a law only if a clause supplied
the uniform measure, and no clause is supplied or proposed here. Its use is to
show that the three natural candidates for "the law of the rule" (static,
monotone, order-averaged) are pairwise distinct on both windows.

## Theorem 4 — the adjacent-pair exchange identity on the menu

**Statement.** For two consecutive sites `x, y` of an order that are lattice
neighbours, with recorded backgrounds `η_x` (for `x`) and `η_y` (for `y`,
excluding `x`), the adjacent transposition leaves `μ_σ` unchanged at a
configuration iff `Z(η_x) · Z(η_y + a) = Z(η_y) · Z(η_x + b)`, where `a = v_x`
and `b = v_y`. For the rules `(3,1,2)` and `(5,2,4)` the identity holds at every
value assignment when both backgrounds are empty and fails at some assignment
for every other pair of background sizes up to 2; for the constant rule it
holds everywhere (D22). At background sizes `(0,1)` the identity reads
`M · Z(c, a) = Z_1^2` and fails on 72 of the 216 assignments `(c, a, b)` at
`(3,1,2)` and on all 216 at `(5,2,4)`.

**Proof.** With both backgrounds empty each side is `M · Z_1`. At `(0,1)` the
left side is `M · Z(c,a)` and the right side `Z_1 · Z_1`. At `(3,1,2)`, `Z_1^2 /
M = 24` while `Z(c,a) = p^2 + q^2 + 4r^2 = 26` (parallel), `2pq + 4r^2 = 22`
(antiparallel) and `2r(p+q) + 2r^2 = 24` (orthogonal): the identity fails on
the 12 parallel or antiparallel ordered pairs `(c,a)` for each of the 6
values of `b`. At `(5,2,4)`, `Z_1^2 / M = 529/6` is not an integer, so every
assignment fails. Larger backgrounds are exact enumerations. ∎

## Theorem 5 — the binary witness of the concurrent note, re-derived

**Statement.** For the binary kernel by the denominator form of Lemma L:
path3 chain `(0,1,2)` versus ends-first `(0,2,1)` differ on all 8
configurations with total variation `9/50` and all-zero masses `8/25` versus
`4/17` (E1); cycle4 has laws with class sizes `(8,8,4,4)`, and cyclic
`(0,1,2,3)` versus opposite-corners `(0,2,1,3)` differ on all 16 configurations
with total variation `9/50` (E2); the rectangle has 28 laws, row-major equals
reverse, and corners-first `(0,2,3,5,1,4)` versus row-major differ on 44 of 64
configurations with total variation `135/578` (E3); the binary constant rule
gives one law (E4). In closed form on cycle4, `K(cyclic) = {{0,2}}` and
`K(opposite) = {{0,2},{0,2}}`, so `μ_cyc(v)/μ_opp(v) = M · Z(v_0, v_2) / Z_1^2`,
equal to `34/25` when `v_0 = v_2` and `16/25` otherwise.

**Proof.** Lemma L with `M = 2`, `Z_1 = 5`, `Z(0,0) = 17`, `Z(0,1) = 8`. The
numbers agree with the concurrent note's, which were produced by the
sequential product; the agreement is the independence check for both. ∎

## No-Go Discipline Gate

The negative sentences of this note are: "different multisets give different
laws" (Theorem 1, so 542 laws on the cube), "the reversed cube order is not
the monotone law", "the uniform mixture is neither the static law nor the
monotone law", and "the exchange identity fails at every non-empty background
size for the menu rules". Each is an exact finite statement on the declared
windows, rules and orders, or a corollary of Lemma L; none is a route no-go
beyond that scope.

### N1 — Attempted routes (all executed this block)

| route | what it would attempt | why it fails here | marker |
| --- | --- | --- | --- |
| a coarser key than the multiset | fix the law by the count of recorded neighbours per site, or by the orientation's degree sequence | orders with equal degree data but different sets give different laws (Theorem 1 injectivity, 542 > number of degree profiles) | D13, D14 |
| a finer key than the multiset | claim the law remembers the order beyond `K` | Lemma L: `K` fixes the law; 48 and 120 orders share `μ_P` | C2, D6, D17 |
| reversal invariance in three dimensions | carry the rectangle's `μ_rev = μ_P` to the cube | the point reflection moves the cube multiset | D16, D19 |
| the mixture as the law | adopt `μ̄` as order-free | `μ̄ ≠ μ` and `μ̄ ≠ μ_P` exactly; no measure over orders is supplied | D8 to D10, D20, D21 |
| exchange-symmetric menu rules | find `(p,q,r)` with the identity at one background | at `(0,1)` it needs `Z(c,a) = Z_1^2/M` for all pairs, i.e. `p = q = r` | D22 |

### N2 — Wall-independence audit

No statement depends on the parked statistical bridge, the Born form, the
gravity lane, the infinite-volume law or any retained-tier equality. The
inputs are the axiom text, the two landed formation-order notes (for the
identity B1, the constancy D7 and the small-window census), and exact
arithmetic.

### N3 — Hidden-wall scan

The results hold for any symmetric positive `φ` on any finite menu with a
constant prior; the specific triples enter only the numbers. Injectivity is
verified, not proved in general: for some window and rule two multisets could
give one law, which would lower the law count below the multiset count and
is a falsifier below, not a wall.

### N4 — Per-citation table

| citation | used for | re-proved here |
| --- | --- | --- |
| classification note B1 | the identity behind Lemma L | yes, as the chain rule of the product form |
| classification note D7 | `Z_1` constant | yes (C1) |
| classification note B5, E5 | small-window census; cycle4 mixture gaps | yes (D1, D2) |
| monotone-order note P1 | one law per monotone class in 2D | re-derived on the rectangle (5 extensions, one multiset) and extended to the cube |
| concurrent note (PR 8096) | binary witness numbers | yes by a different path (E1 to E4); its theorems are not used |

### N5 — Resolution audit

The runner prints its resolution certificate (family G): per-element,
per-site, per-mode and per-block executed; lattice-wide not claimed. Every
number in this note is an exact rational or integer produced by the runner;
decimal approximations in the tables are for reading only.

### N6 — Partial-closure paths and primitive scan

No primitive is changed and none is proposed. The clause that would make the
542 cube laws one is named as an owner decision in the machine status (a
fixed order, a covariant law over orders, or an order-blind rule, which on
the menu is the constant rule by Theorem 4 at background `(0,1)`); it is not
adopted, and its content is not supplied by the axioms.

### N7 — Steelman

"Formation is not a total order; records may lock simultaneously, and a
partial order or a joint formation on covariant sets is the physical object."
Granted: this note quantifies over total orders because the landed formation
law is defined for them, and Lemma L extends verbatim to any acyclic
orientation (a partial order's transitive reduction restricted to edges),
since only the in-neighbourhoods enter. Simultaneous formation on a covariant
set is the second separating clause of the concurrent note and is not computed
here.

### N8 — Cross-cycle echo

The rectangle's `μ_rev = μ_P` was observed in the concurrent note without a
reason; here it is the point-reflection invariance of one multiset, and the
cube shows the general case. The `3x3` window named in the campaign design is
not executed here and is listed as an extension target.

## Falsifiers

The theorems fail if any of the following finite statements fails: the
closed form of Lemma L differs from the sequential product on any order and
configuration of the small windows or the rectangle; the acyclic orientations
of any declared window differ from the order-induced ones or from the counts
4, 8, 8, 14, 98, 1,862; the rectangle or cube has fewer laws than multisets at
either triple or for the binary kernel (28, 28; 542, 542); the monotone-box
class sizes differ from 48 and 120 or the extension counts from 5 and 48; the
cube's reversed multiset equals the monotone one; any total variation or gap
in the tables differs; the exchange identity holds at a non-empty background
for a menu rule or fails for the constant rule; the small-window census differs
from the landed B5; the cycle4 mixture gaps differ from the landed E5.

## Boundaries and non-claims

This note selects no physical rule, no coupling value, no formation order and
no reading of the axioms; the records-only reading is a named premise. The
two-element binary kernel is a declared witness, not the Admissibility rule.

No statement is made about the infinite lattice beyond naming the
specification; existence or uniqueness of an infinite-volume law is outside
this note, and this note does not fire wake condition 1 of the parked
statistical-bridge decision.

This note does not derive, explain, bear on or decide the parked statistical
bridge, the Born form, or the gravity lane's action.

Every negative sentence in this note is an exact finite statement on the
declared windows, rules and orders or a corollary of Lemma L; none is a route
no-go beyond that scope. Injectivity of `K ↦ μ_K` is verified on the declared
windows and rules, not proved for all windows and rules.

Further: no formation site, probability or rate is supplied; the pattern of
records depends on the order through the multiset of recorded-neighbour sets,
so the rule alone does not fix the pattern, and whatever fixes the order is
physics the axioms leave open; the uniform mixture is a witness-generating
device and not a law; no axiom or primitive is changed; the `3x3` window is
not executed; the concurrent note's theorems and clauses are cited, not used,
not adopted and not claimed.

## Imports

References, re-proved at scope, never authority, no values imported: the
landed identity B1 and constancy D7 of the classification note, re-proved
above as Lemma L; the landed censuses B5 and E5, re-computed; the linear
extensions of the product order, re-counted. Declared mathematical
scaffolding: the exact weight triples `(3,1,2)`, `(5,2,4)`, `(2,2,2)`, the
binary kernel with `e^J = 2`, the named orders, and the configuration family F
(the reference configuration, its one- and two-site changes, and 300 draws of
the fixed linear congruential generator, seed `20260913`, multiplier
`1103515245`, increment `12345`, modulus `2^31`, value `(state >> 16) mod 6`).
No observation, fitted value or literature constant enters.

## Review record

Single Fable 5.1 seat, run by the owner's instruction without subagents; no
independent checker seat was engaged. Independence rests on three things:
the runner's 29-mutation census (each mutation perturbs one object at
construction time and must fail in exactly its declared family); the
re-derivation of the concurrent note's binary numbers by a different
implementation path (denominator form versus sequential product) with exact
agreement; and the reproduction of the landed B5 census, the landed E5 gaps,
and the 2026-09-07 note's five linear extensions on the `2x3` rectangle. One
genuine error was caught by the runner during construction: the cube's
reversed multiset was first declared in size-sorted form and disagreed with
the lexicographic key the runner produces; the declaration was corrected to
the runner's canonical form. The expected values in the runner were filled
from its own first exact run and then re-verified on a second run; they are
regression pins, not independent derivations, except where a second method is
executed (C2, C5, D1, D2, E1 to E4).

## Verification

```bash
python3 scripts/admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_2026_09_13.py
python3 scripts/admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_2026_09_13.py --list-mutations
python3 scripts/admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_2026_09_13.py --mutation census_key_keeps_singletons
```

Families: A authority and inputs (the note carries its claim id and fence
sentences; the axiom sentences and the parent notes' phrases are present
verbatim); B menu, covariance, windows, orientations and extensions; C the
normalizers, the closed form of Lemma L against the sequential product, the
tree and cube partition functions; D the census, injectivity, monotone-box,
reversal, mixture and exchange results; E the binary witness; F fences and
the floating-point self-scan of the runner source; G the resolution
certificate. Each of the 29 declared mutations perturbs one object at
construction time and fails in exactly one family, reported by the runner's
`mutation_family_expected:` and `mutation_family_observed:` lines. The runner
prints an exact fraction when its decimal form is short and a twelve-digit
decimal expansion computed by integer arithmetic otherwise; this note quotes
the exact fractions. Expected final line: `TOTAL: PASS=55 FAIL=0`.
