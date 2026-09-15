---
claim_id: admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "On the six Bloch-axis projector menu with the covariant positive product rule of orbit weights (p, q, r), under the records-only reading, for the monotone class of formation orders (the linear extensions of the product order) on boxes of Z^3, on columns Z x C over a finite open cross-section C, and on Z^3: (Q1) every linear extension of a box gives one formation law, invariant under the internal symmetry group and under permutations of the axes, consistent on down-sets, with the explicit product form whose interaction carries a genuine three-body normalizer K_3 on the predecessor triples (not a sum of pair terms at the nonconstant triples; executed); (Q2) unlike two dimensions, the box laws are not consistent under translation: summing out the first plane reproduces the smaller box's law if and only if the plane transfer preserves the two-dimensional law, which fails on the 2x2 cross-section on every one of its 1296 states at (3,1,2) and (5,2,4) (executed; the constant rule is the control), and hence on every larger cross-section; the successor triple of a site is never the predecessor triple of a site (proved), so the two-dimensional telescoping has no analogue; (Q3) for every finite cross-section the sweep of planes is a strictly positive Markov chain with a unique stationary plane law, which defines the column law; its two boundary planes carry the two-dimensional law; the quadrant column exists for every positive rule by down-set consistency; the stationary 2x2 plane law is computed exactly by orbit reduction and differs from the two-dimensional law; (Q4) with c the largest one-neighbor sensitivity of the one-, two- and three-neighbor kernels, the influence of a site on a site at monotone distance d is at most N c^d with N the number of monotone paths, every pair correlation of every box or column law is at most 4 |g| |h| (3c)^(ceil(|x-y|_1/2)-1), the plane chain mixes at rate c/(1-2c) uniformly in the cross-section, and for c < 1/3 the stationary plane law on the full Z^2 cross-section exists, is unique, is translation invariant, and defines a translation-invariant law on Z^3 to which every box law converges as its corner recedes; c is an exact rational at eight triples and the three silent triples (3,1,2), (5,2,4), (7,3,5) lie inside the region (3c = 81/110, 31950/63407, 5782/10295); (Q5) corollary at scope: in the region every record two-point function of the monotone formation law decays at least exponentially, so no long-range kernel arises from it. No order or corner is selected as physical; nothing about the static law beyond citation; nothing for c >= 1/3; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_infinite_strip_row_sweep_formation_law_versus_static_law_bounded_theorem_note_2026-09-06
  - admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_bounded_theorem_note_2026-09-07
runner: scripts/admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_2026_09_15.py
---

# The three-dimensional formation law of the monotone class: the plane chain, the three-body term, and the coupling region that contains the silent triples

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

Lay records down on a block of the physical lattice, in any order you like,
provided each site waits for the three sites behind it — below it, to its
left, and in front of it — before it forms. As in the plane, every such order
gives exactly the same pattern law, and that law has one new ingredient: a
term that couples the three sites behind a site all at once, not just in
pairs. Unlike the plane, this law remembers where the block began: if you
strip off the first layer, what remains is not the law of the smaller block.
So the pattern law of the whole lattice cannot be built by fitting blocks
together; it is built by letting the first layer recede to infinity. That
limit exists and is unique whenever a single number computed from the rule —
the most that changing one earlier neighbor can change a site's odds — is
below one third. At the three rule settings where all our earlier tests of
the static pattern law were silent, that number is below one third, so there
the formation law is one object with correlations that die off exponentially
in every direction. Nothing here says which order, or which corner, is the
physical one, and nothing is said about the static law itself.

Exactly: for the covariant positive product rule with orbit weights `(p, q, r)`
on the six-axis menu, with `K(a, s) = φ(s, a)/Z_1` and
`K_k(a_1, …, a_k) = Σ_s Π_i K(a_i, s)`, the monotone-class law of a box
`B ⊂ Z^3` is `μ_B(v) = (1/6) Π_{y ∈ A_x} K(v_y, v_x) / Π_{|A_x| ≥ 2} K_{|A_x|}(v_{A_x})`
with `A_x = {x − e_i : x_i ≥ 1}` the predecessor set (Q1); `log K_3` is not a
sum of pair terms (the third difference `2160/2197 ≠ 1` at `(3, 1, 2)`). The
first plane cannot be summed out: on the `2×2` cross-section the plane
transfer moves the two-dimensional law on all `1296` states, by total
variation `356696849/806187919680` at `(3, 1, 2)` (Q2). Every finite
cross-section has a unique stationary plane law (Q3); the causal coupling
gives `|Cov(g(v_x), h(v_y))| ≤ 4 ‖g‖ ‖h‖ (3c)^{⌈|x − y|_1/2⌉ − 1}` and
mixing at rate `c/(1 − 2c)` (Q4), with
`c = 27/110, 10650/63407, 5782/30885` at `(3, 1, 2), (5, 2, 4), (7, 3, 5)`.
Executed with exact arithmetic: 33 checks, 26 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the owner's corrected queue (block-04 refresh, item 4): 'a three-dimensional formation process [is a] different object. Declare the order and initial or boundary law and the exact uniqueness quantifier.'; block 02's N1 route 3: 'a three-recorded-neighbor sweep … ATTEMPTED (witness only; no theorem)'; the derivation campaign's record-dynamics block (#8093): whether long-range record correlations arise from the formation law without a supplied tick; the owner's sequencing gate (2026-08-26): what the Admissibility rule induces on the infinite lattice is unidentified"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the monotone class on Z^3 is now a declared, constructed object with an exact coupling region; next: the eight corner classes as one covariant family and their relation to the random-priority law; the exact region boundary in (p, q, r); consumers: the campaign's queue, the derivation campaign's assembly (an edge 'clause-needed' for long-range record fields under positive product rules), the parked statistical-bridge material (read-only)"
conditional_surface_status: "exact on the declared menu and triples; Q1 is proved for every box and every positive symmetric rule; Q2 is a proved reduction with an executed refutation at the declared nonconstant triples and a proved lemma on the mechanism; Q3 is proved for every finite cross-section and every positive rule, with the 2x2 stationary law executed; Q4 is proved for every box and column, and on Z^2 x Z / Z^3 under c < 1/3; the region membership of eight triples is executed; conditional on the records-only reading, positivity, the six-axis menu and the monotone class as supplied conditions; no static-law statement; no order selected as physical"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Q1 is elementary (recorded sets; regrouping of normalizers) with exact witnesses; Q2 is an exact reduction plus a finite refutation (1296 states) plus a combinatorial lemma; Q3 is the elementary contraction of a strictly positive finite chain plus down-set consistency and the two-dimensional translate consistency re-proved from the parent's 180-degree identity; Q4 is a coupling argument along monotone paths with an explicit path count, a level-chain conditioning argument for the covariance bound, and compactness plus the same coupling for the infinite cross-section; every number printed is an exact rational; nothing infinite-volume is claimed outside the region except existence of the quadrant column"
```

## Premises and declared objects

**Axioms used (verbatim, the only framework premises).** From
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): "There is one
fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." — "For each site, the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions." — "No possibility is privileged. Possibilities are distinguished by
the supplied algebraic structure alone." — "Records form." — "When present, a
record locks exactly one admissible local possibility. A site never carries more
than one record; records are permanent." — "Only records are readable."

**Readings carried from blocks 01–05, named, nothing new adopted.** The
records-only reading (an unrecorded neighbor contributes no factor and is not a
condition); positivity of the rule; the six-axis menu
`M = {P(±e_1), P(±e_2), P(±e_3)}` with the orbit weights `φ(s, t) = p` (same
axis and sign), `q` (same axis, opposite sign), `r` (orthogonal), `p, q, r > 0`;
the variation clause restricted to the menu (`p, q, r` not all equal) names the
nonconstant case, and the constant rule `(2, 2, 2)` is a control. The formation
law of an order `σ` on a finite window: the product of the one-site conditionals
`r(s | recorded neighbors)` (block 01's definition). The monotone class: the
linear extensions of the product partial order on a box (block 05's class, one
dimension up). No order and no corner is selected as physical; the axioms supply
no order.

**Notation.** `Z_1 = p + q + 4r`; `K(a, s) = φ(s, a)/Z_1`, a symmetric doubly
stochastic `6 × 6` matrix; for `k ≥ 1`,
`K_k(a_1, …, a_k) = Σ_s Π_{i=1}^k K(a_i, s)`, so `K_1 ≡ 1`, `K_2(a, b) = (K^2)(a, b)`
(block 02's E1), and `K_3` is a symmetric three-index array. The `k`-neighbor
kernel is `r(s | a_1, …, a_k) = Π_i K(a_i, s)/K_k(a)` for `k ≥ 1` — the product
rule's conditional, since `Z_k(a) = Σ_s Π φ(s, a_i) = Z_1^k K_k(a)` — and
`r(s | ∅) = 1/6`, the uniform law on the menu (forced by the internal covariance
below on a transitive menu; block 01 declared it). A box is
`B = {0, …, n_1} × {0, …, n_2} × {0, …, n_3}` with the product order `≤`; the
level `|x|_1 = x_1 + x_2 + x_3`; the predecessor set `A_x = {x − e_i : x_i ≥ 1}`
(`|A_x| ∈ {0, 1, 2, 3}`); the successor set `S_x = {x + e_i} ∩ B`. A down-set is
`D ⊆ B` with `A_x ⊆ D` for every `x ∈ D`. For `z ≤ x`, `N(z, x)` is the number of
monotone lattice paths from `z` to `x`, the multinomial
`|x − z|_1! / Π_i (x_i − z_i)!`; `Σ_{z: |x − z|_1 = d} N(z, x) ≤ 3^d`.

**The internal symmetry group.** The 48 signed permutations of the axes act on
`M`; `φ` is invariant, so every law built from `φ` is invariant under the
simultaneous action on all site values; the group is transitive on `M` and on
each of the three ordered-pair types (same, opposite, orthogonal). The proper
cubic rotations are 24 of the 48; the axioms' covariance clause is under those;
the extra inversion is a symmetry of the declared rule, not an axiom statement.

**The plane transfer and the two-dimensional law.** For a cross-section
`C = {0, …, n_2} × {0, …, n_3}` and plane states `w, v ∈ M^C`,
`P_C(w, v) = Π_{y ∈ C} r(v_y | w_y, v_{y − e_2}, v_{y − e_3})` (absent
predecessors omitted); `μ_C(v) = Π_{y ∈ C} r(v_y | v_{y − e_2}, v_{y − e_3})` is
the two-dimensional monotone law of the rectangle `C` (block 05's `μ_P` in the
coordinates `(x_2, x_3)`). Then `μ_B(v) = μ_C(v^{(0)}) Π_{t=1}^{n_1} P_C(v^{(t−1)}, v^{(t)})`
for `B = {0, …, n_1} × C`, `v^{(t)}` the plane `x_1 = t`.

**The sensitivities.** `c_k = max TV(r(· | A), r(· | A'))` over `k`-tuples
`A, A' ∈ M^k` differing in exactly one entry (`k = 1, 2, 3`); `c = max(c_1, c_2, c_3)`;
`θ = c/(1 − 2c)` when `2c < 1`. Exact at eight triples (runner E1):

| triple | `c_1` | `c_2` | `c_3` | `c` | `3c` | `θ` |
|---|---|---|---|---|---|---|
| `(3, 1, 2)` | `1/6` | `30/143` | `27/110` | `27/110` | `81/110` | `27/56` |
| `(5, 2, 4)` | `3/23` | `65/434` | `10650/63407` | `10650/63407` | `31950/63407` | `10650/42107` |
| `(7, 3, 5)` | `2/15` | `910/5609` | `5782/30885` | `5782/30885` | `5782/10295` | `5782/19321` |
| `(2, 1, 2)` | `1/11` | `1/10` | `1/9` | `1/9` | `1/3` | `1/7` |
| `(3, 2, 2)` | `1/13` | `39/406` | `234/2077` | `234/2077` | `702/2077` | `234/1609` |
| `(5, 4, 4)` | `1/25` | `25/546` | `500/9701` | `500/9701` | `1500/9701` | `500/8701` |
| `(11, 10, 10)` | `1/61` | `671/38502` | `73810/3994861` | `73810/3994861` | `221430/3994861` | `73810/3847241` |
| `(2, 2, 2)` | `0` | `0` | `0` | `0` | `0` | `0` |

All eight triples lie inside the region `3c < 1`; at `(2, 1, 2)`, `3c = 1/3`. The
three silent triples of blocks 03–04 lie inside with room to spare
(`3c = 81/110, 31950/63407, 5782/10295`). The finite-box bounds of Q4(a), (b)
hold at every triple; the infinite-cross-section statements need the strict
inequality, which the region names.

## Prior art and what is new

Block 02 (on main) proved that the row sweep on a strip preserves the chain law
(`p_0 P = p_0`, E3) and built the strip's formation law as a projective limit;
its N1 route 3 records a three-recorded-neighbor sweep as attempted by witness
only. Block 05 (on main) gave the monotone class on rectangles: one law (P1),
rows and columns as chains (P4), the corner law (P5), the opposite-corner
identity by the edge/plaquette product (P7(a)). The plane-law note
[`ADMISSIBILITY_PLANE_FORMATION_DIAGONAL_INTERACTION_NOTE_2026-09-08.md`](ADMISSIBILITY_PLANE_FORMATION_DIAGONAL_INTERACTION_NOTE_2026-09-08.md)
(PR #8039; landed on main on 2026-09-15 after this block's branch was cut;
unaudited; not an input here) extends the rectangle laws to the plane by
projective consistency using P7(a) and identifies the pair potential; it states
that it "does not construct an infinite physical formation schedule". The concurrent PR #8102
(open; not an input) gives the recorded-set multiset key and finds on the
`2×2×2` cube that the reversed order's law differs from the row-major one — a
finite fact consistent with Q2 here. The owner's random-priority formation law
on `Z^3` (`docs/ADMISSIBILITY_RANDOM_PRIORITY_FORMATION_NOTE_2026-09-07.md`, on
the branch `physics-loop/toe-campaign-20260907`, unlanded; not an input) is a
covariant random-order construction whose decay comes from finite ancestry; it
is a different object with a different mechanism. The classical references —
unilateral Markov fields and Markov meshes, probabilistic cellular automata and
their high-noise uniqueness by coupling, the Doeblin contraction for positive
finite chains, the Kolmogorov extension, the Krylov–Bogolyubov existence of
invariant laws for Feller kernels on compact spaces — are named here and under
Imports; every one is re-proved at the scope used, and no value or theorem is
imported as authority.

New here: the three-dimensional monotone class as one constructed object — the
three-body normalizer and its irreducibility (Q1), the failure of translate
consistency reduced to one exact identity and refuted (Q2), the plane chain with
its unique stationary law per cross-section and the two-dimensional boundary
planes (Q3), and the causal coupling theorem with its exact region, uniform in
the cross-section, giving existence, uniqueness, translation invariance and
exponential decay on `Z^3` for `c < 1/3` (Q4) — a region that contains the
silent triples, where the static law's uniqueness is undecided by every
criterion tried (blocks 03–04, both on main).

## Exact target and obligation graph

**Target.** For the declared rule on the six-axis menu: (Q1) the box law of the
monotone class and its structure; (Q2) the failure of translation consistency;
(Q3) the plane chain and the column law; (Q4) the coupling theorem, the region,
and the `Z^3` law; (Q5) the decay of record two-point functions at scope.

| obligation | status here |
|---|---|
| one law per box; internal and axis symmetry; down-set consistency (Q1a–d) | proved for every box and every positive symmetric rule; executed on the cube (B1–B4) |
| the product form with the three-body normalizer (Q1e); irreducibility (Q1f) | proved (regrouping); executed on the cube and small boxes (B5); third difference executed (B6) |
| the first plane cannot be summed out (Q2) | reduction proved (a, c); refuted at `(3, 1, 2)`, `(5, 2, 4)` on all 1296 states (C1–C3); the mechanism lemma proved (e); a proof at every nonconstant triple is not given |
| the two-dimensional translate consistency (Q2b) | re-proved from P7(a) and down-set consistency; executed on the `2×3` rectangle (C4) |
| the plane chain: positivity, contraction, unique stationary law (Q3a–b) | proved for every finite cross-section; executed at `2×2` (D1–D3) |
| boundary planes carry the two-dimensional law (Q3c); the quadrant column (Q3d) | proved; executed at `2×2` (D4) |
| the exact stationary `2×2` plane law (Q3e) | executed by orbit reduction: 32 orbits; TV from `μ_C` and the interior pair (D2, D5) |
| the influence bound and the covariance bound (Q4a–b) | proved for every box and column; executed against the exact cube influence and the `2×3` rectangle (E2–E4) |
| the sweep rate and the uniform spectral bound (Q4c) | proved; the sector contraction executed at `2×2` (E5) |
| the full cross-section and the `Z^3` law for `c < 1/3` (Q4d–e) | proved; the region membership executed at eight triples (E1) |
| the decay of two-point functions (Q5) | corollary; N-gated; executed on the cube's pairs (E6) |
| the static law of `Z^3` at the silent triples; `c ≥ 1/3`; a physical order or corner; the eight corner laws' distinctness on `Z^3` | open; not this note |

The strongest missing lemma is a proof that the plane transfer moves the
two-dimensional law at every nonconstant triple (here: two executed triples and
the mechanism lemma); it is not used by Q3–Q5, which hold with or without it.

## Theorem Q1 — the box law of the monotone class

**(a) One law.** Every linear extension `σ` of the product order on `B` gives
the same formation law `μ_B(v) = Π_{x ∈ B} r(v_x | v_{A_x})`, for every
nearest-neighbor rule.

*Proof.* The neighbors of `x` are `x ± e_i`; those with `x − e_i` are below `x`
in the product order, hence before it in every linear extension, and those with
`x + e_i` are above it, hence after it. So the recorded set of `x` is `A_x` for
every `σ`. ∎ Executed: the `48` linear extensions of the `2×2×2` product order
share the recorded-set family, which equals the predecessor family (B1).

**(b) Internal covariance.** `μ_B(gv) = μ_B(v)` for every `g` in the internal
group; hence every one-site marginal is uniform on `M`, and every pair marginal
`P(v_x = a, v_y = b)` depends on `(a, b)` only through its type (same, opposite,
orthogonal).

*Proof.* `φ(gs, gt) = φ(s, t)`, so every kernel satisfies
`r(gs | gA) = r(s | A)` and the product is invariant. The group is transitive on
`M` and on each ordered-pair type. ∎ Executed on the cube: all one-site
marginals equal `1/6`; every pair marginal is constant on each type (B2).

**(c) Axis symmetry.** For a permutation `τ` of the coordinate axes,
`μ_{τB}(τv) = μ_B(v)`, where `τ` acts on sites and `τB` is the permuted box.

*Proof.* `τ` maps predecessor sets to predecessor sets, and each kernel
`r(s | A)` is symmetric in the recorded values. ∎ (Block 05's P3, one dimension
up.) Executed: the cube law is invariant under the six axis permutations (B3).

**(d) Down-set consistency.** For every down-set `D ⊆ B`, the marginal of `μ_B`
on `D` is `μ_D(v_D) = Π_{x ∈ D} r(v_x | v_{A_x})`, the monotone law of `D`
itself.

*Proof.* For `x ∈ D`, `A_x ⊆ D`, so the factors of `D`'s sites are exactly
`μ_D`. Sum out the sites of `B ∖ D` in the reverse of a linear extension: the
site summed is maximal among the remaining ones, so it occurs in no remaining
factor except its own kernel, which sums to one. ∎ Executed: the cube's
marginal on the plane `x_3 = 0` is the `2×2` two-dimensional law, and its
marginals on the corner lines are the `K`-chain with the uniform start (B4).
In particular the three coordinate planes of a box carry the two-dimensional
monotone laws of their rectangles, and the three coordinate lines carry the
`K`-chain.

**(e) The product form.**
`μ_B(v) = (1/6) Π_{x ∈ B} Π_{y ∈ A_x} K(v_y, v_x) / Π_{x : |A_x| ≥ 2} K_{|A_x|}(v_{A_x})`.
Every nearest-neighbor edge of `B` occurs exactly once in the numerator (as
`y ∈ A_x` for its upper endpoint `x`); the denominator carries `K_2 = K^2` on
the two-predecessor sites (the three coordinate planes, block 05's anti-diagonal
denominators) and `K_3` on every site with three predecessors.

*Proof.* `Z_k(a) = Σ_s Π_i φ(s, a_i) = Z_1^k K_k(a)`, so
`r(s | a) = Π_i φ(s, a_i)/Z_k(a) = Π_i K(a_i, s)/K_k(a)`, and `r(s | ∅) = 1/6`
at the origin. Multiply over `x`. ∎ Executed: the product form agrees with the
product of conditionals on every configuration of the `1×2×2` and `2×2×1`
boxes and on a fixed sample of `2000` configurations of the cube (B5).

**(f) The three-body normalizer is irreducible.** At a nonconstant triple
`log K_3` is not a sum of pair functions: for
`(a_0, a_1; b_0, b_1; c_0, c_1) = (+x, +y; +x, +y; +x, +z)`,
`K_3(a_0,b_0,c_0) K_3(a_1,b_1,c_0) K_3(a_1,b_0,c_1) K_3(a_0,b_1,c_1) / [K_3(a_1,b_0,c_0) K_3(a_0,b_1,c_0) K_3(a_0,b_0,c_1) K_3(a_1,b_1,c_1)]`
equals `2160/2197` at `(3, 1, 2)` and `686196/704969` at `(5, 2, 4)`, while any
`F(a, b, c) = g(a, b) + g(b, c) + g(a, c)` has vanishing alternating sum over
the eight corners of the cube of choices, so the ratio would be `1`. At the
constant rule the ratio is `1` (B6). Hence the interaction of `μ_B` in the
bulk is a nearest-neighbor pair term `−log K` plus a genuine three-body term
`+log K_3` on the predecessor triples `{x − e_1, x − e_2, x − e_3}`, which are
pairwise at face-diagonal distance; the two-body diagonal terms of the plane
(block 05; the plane-law note, #8039) survive only on the three coordinate
planes of the box. ∎

## Theorem Q2 — the first plane cannot be summed out

**(a) The reduction.** Let `B = {0, …, n_1} × C` with `n_1 ≥ 1` and let
`B^+ = {1, …, n_1} × C` be the box without its first plane, with its own
monotone law `μ_{B^+}` (the same law as `μ_{\{0,…,n_1−1\} × C}` translated by
`e_1`). Then the marginal of `μ_B` on `B^+` equals `μ_{B^+}` for every
configuration if and only if `μ_C P_C = μ_C`.

*Proof.* `μ_B(v) = μ_C(v^{(0)}) Π_{t ≥ 1} P_C(v^{(t−1)}, v^{(t)})`; summing
`v^{(0)}` gives `(μ_C P_C)(v^{(1)}) Π_{t ≥ 2} P_C(v^{(t−1)}, v^{(t)})`, while
`μ_{B^+}(v) = μ_C(v^{(1)}) Π_{t ≥ 2} P_C(v^{(t−1)}, v^{(t)})` because the sites of
plane `1` have no predecessor in `B^+` outside their plane. The common factor
is strictly positive, so the two agree for all `v` iff `(μ_C P_C)(u) = μ_C(u)`
for all `u`. ∎

**(b) Two dimensions: translate consistency holds (re-proved).** For a
rectangle `R` and a sub-rectangle `R' ⊆ R`, the marginal of `μ_R` on `R'` is
the monotone law of `R'`.

*Proof.* Removing last rows and columns is down-set consistency (Q1d, which
holds in every dimension). To remove the first row: by block 05's P7(a),
`μ_R` equals the law of the bottom-right class of `R` (the 180-degree
identity); in that class the first row consists of last-formed sites, so
summing it out is down-set consistency for that class and leaves the
bottom-right law of the smaller rectangle, which by P7(a) again is its
top-left monotone law. The first column is the same with left-right
reflection. ∎ This is the projective-consistency argument of the plane-law note
(#8039, landed on main 2026-09-15), re-proved here; the one-row case is exactly
block 02's `p_0 P = p_0` (E3). Executed: the marginals of the `2×3` law on its four `2×2`
sub-rectangles and on its translated `1×3` and `2×2` sub-rectangles are the
sub-rectangle laws (C4).

**(c) Three dimensions: one cross-section refutes all larger ones.** If
`μ_{C_2} P_{C_2} ≠ μ_{C_2}` for the `2×2` corner square `C_2`, then
`μ_C P_C ≠ μ_C` for every cross-section `C ⊇ C_2` (with the same corner).

*Proof.* `C_2` is a down-set of `C`, so the marginal of `μ_C` on `C_2` is
`μ_{C_2}` (Q1d). The sites of `C_2` in the new plane record only sites of
`C_2` in both planes, so the marginal of `μ_C P_C` on `C_2` equals
`μ_{C_2} P_{C_2}` (sum the other sites of the new plane in reverse order —
leaves — and then the other sites of the old plane, which enter only through
`μ_C`). If `μ_C P_C = μ_C`, taking marginals on `C_2` gives
`μ_{C_2} P_{C_2} = μ_{C_2}`. ∎

**(d) The refutation, exact.** At `(3, 1, 2)`, `μ_{C_2} P_{C_2}` differs from
`μ_{C_2}` on every one of the `1296` plane states, with total variation
`356696849/806187919680`; at `(5, 2, 4)` on every state, with total variation
`17075751317037722924/75640257098415067067163`; at the constant rule
`(2, 2, 2)` the two coincide (the uniform law is invariant). Under
`μ_{C_2} P_{C_2}` the one-site marginals are still uniform and the two pairs
adjacent to the corner, `((0,0),(1,0))` and `((0,0),(0,1))`, are still
`(1/6) K`-pairs (they lie on the coordinate lines, Q1d), while the pairs
`((0,1),(1,1))` and `((1,0),(1,1))` are no longer `(1/6) K`-pairs and the
anti-diagonal pair `((0,1),(1,0))` is no longer a `(1/6) K^2`-pair (C1–C3).
Hence, by (a) and (c): for every box `B = {0, …, n_1} × C` with
`n_1 ≥ 1` and `C ⊇ C_2`, at these two triples, the marginal of `μ_B` on the
box without its first plane is not the smaller box's monotone law; by Q1c the
same holds for the first plane in any of the three directions. The family of
monotone box laws is therefore not consistent under translation, and no law on
`Z^3` has every box marginal equal to `μ_B`: the infinite-volume object must
be a limit, which Q3–Q4 construct.

**(e) Why the two-dimensional proof has no analogue (the mechanism lemma).** In
E3's telescoping, summing the previous row's sites in order produces at each
step the two-step kernel `K^2` on the two successors of the summed site,
which is the normalizer of the site whose predecessor pair is exactly that
pair; the cancellation drives the induction. In three dimensions the sum over
a site `z` of a plane produces `K_3` on its three successors
`z + e_1, z + e_2, z + e_3`, and no site of `Z^3` has this triple as its
predecessor set: if `{z + e_i} = {x − e_i}` then `x = z + e_1 + e_{π(1)} =
z + e_2 + e_{π(2)}` for a permutation `π`, forcing `π(1) = 2`, `π(2) = 1`, and
then `x = z + e_3 + e_{π(3)} = z + 2e_3 ≠ z + e_1 + e_2`. ∎ The successor
triple of a site and the predecessor triple of a site are the two tetrahedral
sublattices of a unit cube's corners; in two dimensions the two successors of a
plaquette's first corner are the two predecessors of its last corner, and that
coincidence is what E3 and P7(a) use. This lemma explains the failure of the
mechanism; the refutation itself is (d).

## Theorem Q3 — the plane chain and the column law

**(a) Contraction.** For every finite cross-section `C`, `P_C` is a stochastic
matrix on `M^C` with every entry at least `δ_C = min_{w,v} P_C(w, v) > 0`.
Consequently for any two laws `ν, ν'` on `M^C`,
`‖ν P_C − ν' P_C‖_TV ≤ (1 − 6^{|C|} δ_C) ‖ν − ν'‖_TV`, there is exactly one
stationary law `π_C`, and `‖ν P_C^n − π_C‖_TV ≤ (1 − 6^{|C|} δ_C)^n`.

*Proof.* Positivity of `φ` makes every kernel value positive, hence every entry
of `P_C`. Write `P_C(w, v) = ε u(v) + (1 − ε) R(w, v)` with `u` uniform,
`ε = 6^{|C|} δ_C ∈ (0, 1]` and `R` stochastic; then
`ν P − ν' P = (1 − ε)(ν − ν') R` and `‖(ν − ν') R‖_TV ≤ ‖ν − ν'‖_TV`. The map
`ν ↦ ν P_C` is a strict contraction of the complete metric space of laws on
`M^C` under total variation, so it has exactly one fixed point, reached
geometrically from every start. ∎ Executed at `C_2`: the minimal entry of
`P_{C_2}` is positive, every row sums to one (D1).

**(b) The column law.** The stationary two-sided chain `(v^{(t)})_{t ∈ Z}` with
`v^{(t)} ~ π_C` and transitions `P_C` is a law on `M^{Z × C}` — *the monotone
formation law of the column `Z × C`*. It is the limit of the box laws
`μ_{\{0,…,n\} × C}` as the first plane recedes: the plane-`t` marginals of the box
law are `μ_C P_C^t → π_C`, and the joint law of planes `t − k, …, t` converges
to the stationary `k`-step joint law (a). Any limit point of box laws with the
first plane receding is this chain.

**(c) The boundary planes carry the two-dimensional law.** Under the column
law, the restriction to the boundary plane `Z × {0, …, n_2} × {0}` is the
two-dimensional monotone law of the two-sided strip `Z × {0, …, n_2}` (every
finite window of it carries the rectangle law of that window); likewise for
`x_2 = 0`. In particular the row `x_3 = 0` and the row `x_2 = 0` of every plane
are `K`-chains, and the line `x_2 = x_3 = 0` is a `K`-chain.

*Proof.* The box law's marginal on its plane `x_3 = 0` is the rectangle law of
`{0, …, n} × {0, …, n_2}` (Q1d); restricted to the planes `t − k, …, t` it is the
marginal of that rectangle law on its last `k + 1` columns, which is the
`(k+1) × (n_2+1)` rectangle law by (Q2b), independently of `t` and `n`. The
box law converges to the column law on every such window (b); the marginals
agree at every finite stage, hence in the limit. Rows and lines: block 05's P4
and Q1d. ∎ Executed at `C_2`: under `π_{C_2}` the pairs on the coordinate
lines are `(1/6) K`-pairs and the one-site marginals are uniform (D4).

**(d) Cross-section consistency and the quadrant column.** If `C ⊆ C'` are
cross-sections with the same corner (`C` a down-set of `C'`), the column law of
`C'` restricted to `Z × C` is the column law of `C`. Hence the column laws over
the quadrant cross-sections `{0, …, n_2} × {0, …, n_3}` are consistent, and the
extension theorem for consistent families on a countable product (cited under
Imports) gives one law on `Z × [0, ∞)^2` — *the quadrant column* —
for every positive rule, without any coupling condition. It is invariant under
`x_1`-translations and carries the two-dimensional law on its two boundary
planes.

*Proof.* Under the `C'`-chain the restriction of each plane to `C` evolves by
`P_C` (the sites of `C` record only sites of `C`, in both planes) and is
stationary, so by uniqueness (a) its one-plane law is `π_C` and the restricted
process is the `C`-chain. Consistency over the increasing family of
cross-sections gives the extension on the countable product. ∎

**(e) The stationary `2×2` plane law, exactly.** `π_{C_2}` is computed exactly
from the orbit quotient of `P_{C_2}` under the internal group and the plane
transpose (32 orbits of the `1296` states; the quotient's rows are
independent of the representative, D2). It differs from `μ_{C_2}` by total
variation `0.000454716…` (an exact rational with 51-digit numerator and denominator, printed under `--exact`) at `(3, 1, 2)` and `0.000227752…` at `(5, 2, 4)`; its one-site
marginals are uniform; the coordinate-line pairs are `(1/6) K`-pairs; the
interior pair `((0,1),(1,1))` is not: its same-axis-and-sign entry is
`0.0416936074…` against `(1/6) K(+x, +x) = `0.0416666…`` at `(3, 1, 2)` (D5). So the
bulk plane of the three-dimensional formation law is not the two-dimensional
monotone law: it keeps that law on its two boundary lines and loses it one step
in.

## Theorem Q4 — the causal coupling theorem and the region

**Setting.** A monotone coupling of two copies `V, V'` of a box law with forced
values on a set `S` of source sites: run a linear extension; at each site
`x ∉ S` draw `(V_x, V'_x)` from a maximal coupling of `r(· | V_{A_x})` and
`r(· | V'_{A_x})`, diagonal when the recorded tuples coincide. The discrepancy
set is `D = {x : V_x ≠ V'_x} ⊇ S`. One-entry changes chain the two tuples, so
`TV(r(· | a), r(· | a')) ≤ c_{|A_x|} · #{i : a_i ≠ a'_i}` and
`P(x ∈ D | past) ≤ c Σ_{z ∈ A_x} 1_{z ∈ D}`.

**(a) The influence bound.** For `m(x) = P(x ∈ D)`:
`m(x) ≤ Σ_{z ∈ S} N(z, x) c^{|x − z|_1}` for every `x ∉ S`. In particular, for a
single source `x` and a site `y ≥ x`, the conditional laws of `V_y` given the
configuration of the down-set `B ∖ {y' ≥ x}` and `V_x = s`, respectively
`V_x = s'`, differ in total variation by at most `N(x, y) c^{|y − x|_1} ≤ (3c)^{|y − x|_1}`,
and for a function `g` of the configuration on a set `Y ⊆ {y ≥ x}`, the two
conditional expectations differ by at most `2 ‖g‖_∞ Σ_{y ∈ Y} N(x, y) c^{|y − x|_1}`.

*Proof.* Induction along the linear extension:
`m(x) ≤ c Σ_{z' ∈ A_x} m(z') ≤ c Σ_{z' ∈ A_x} Σ_{z ∈ S} N(z, z') c^{|z' − z|_1} = Σ_{z ∈ S} c^{|x − z|_1} Σ_{z' ∈ A_x} N(z, z') = Σ_{z ∈ S} N(z, x) c^{|x − z|_1}`,
since every monotone path to `x` passes through a predecessor of `x` last. The
conditional-law statements follow because the two copies' marginals are the two
conditional laws and they differ only on `D`. ∎ Executed on the cube at
`(3, 1, 2)`: the exact total variation between the laws of `v_{111}` given
`v_{000} = s` and `v_{000} = s'`, maximized over `s ≠ s'`, is `273651254/10658734515 = 0.02567389…`, against
the bound `N c^3 = 6 · (27/110)^3 = `59049/665500 = 0.08872877…`` (E2); on the `2×3` rectangle
with two predecessors the influence of `v_{00}` on `v_{12}` is bounded by
`3 c_{(2)}^3` (E3).

**(b) The covariance bound.** For every box law and all sites `x, y` and
functions `g, h` on `M`,
`|Cov(g(v_x), h(v_y))| ≤ 4 ‖g‖_∞ ‖h‖_∞ (3c)^{ρ(x, y) − 1}`, where
`ρ(x, y) = max(|x − x∧y|_1, |y − x∧y|_1) ≥ ⌈|x − y|_1/2⌉` and `x∧y` is the
componentwise minimum. The same bound holds for the column law, the quadrant
column, and (Q4e) the `Z^3` law, as limits of box laws.

*Proof.* Let `L_t = {z ∈ B : |z|_1 = t}` and `𝔉_t` the σ-field of the
configuration on levels `≤ t`. Every predecessor of a site at level `t` lies at
level `t − 1`, so given `𝔉_t` the configuration above level `t` is generated by
the kernels level by level (a Markov chain of levels). Put `m = |x∧y|_1 + 1`.
The sites `z ≤ x` with `|z|_1 ≥ m` and the sites `z ≤ y` with `|z|_1 ≥ m` are
disjoint: a common one satisfies `z ≤ x∧y`, hence `|z|_1 ≤ m − 1`. Therefore,
given `𝔉_m`, `v_x` and `v_y` are functions of disjoint sets of the
`𝔉_m`-measurable values at level `m` and of the kernels' innovations at
disjoint sets of sites; they are conditionally independent (if one of them is
already `𝔉_m`-measurable the statement is trivial). Hence
`Cov(g(v_x), h(v_y)) = Cov(G, H)` with `G = E[g(v_x) | 𝔉_m]`,
`H = E[h(v_y) | 𝔉_m]`. If `|y|_1 > m`, `H` depends on the level-`m`
configuration only through `B_y = {z ∈ L_m : z ≤ y}`, and by (a) applied with
sources the sites of `B_y` on which two configurations differ,
`osc(H) ≤ 2 ‖h‖_∞ Σ_{z ∈ B_y} N(z, y) c^{|y|_1 − m} ≤ 2 ‖h‖_∞ (3c)^{|y|_1 − m}`,
since the number of monotone paths of length `ℓ` descending from `y` is at most
`3^ℓ`. Then `|Cov(G, H)| ≤ E|G − EG| · osc(H) ≤ 2 ‖g‖_∞ · 2 ‖h‖_∞ (3c)^{|y|_1 − m}`,
and `|y|_1 − m = |y − x∧y|_1 − 1`. The same with the roles exchanged gives the
exponent `|x − x∧y|_1 − 1`; take the larger of the two (if the larger belongs to
a site at level `≤ m`, both exponents are `≤ 0` and the bound is trivial). Finally
`|x − x∧y|_1 + |y − x∧y|_1 = |x − y|_1`. The column, quadrant-column and `Z^3`
laws are limits of box laws on every finite window (Q3b, Q3d, Q4e), and the
bound passes to the limit. ∎ Executed on the cube at `(3, 1, 2)`: every pair
`(x, y)` and every pair of axis indicators satisfies the bound (E6).

**(c) The sweep rate, uniform in the cross-section.** Assume `2c < 1` and let
`θ = c/(1 − 2c)`. For any two initial plane laws `ν, ν'` on `M^C`, the coupled
chains have `P(y ∈ D)` at plane `n` at most
`Σ_{j ≥ 0} C(n + j, n) 2^j c^{n + j} = c^n (1 − 2c)^{−n−1} = (1 − 2c)^{−1} θ^n`
for every site `y`, uniformly in `C`. Hence
`‖ν P_C^n − ν' P_C^n‖_TV ≤ |C| (1 − 2c)^{−1} θ^n` and every eigenvalue of `P_C`
other than `1` has modulus at most `θ`, for every finite cross-section.

*Proof.* Every site of plane `0` is a potential source. A monotone path from
`y` in plane `n` down to plane `0` takes exactly `n` steps `−e_1` and some `j ≥ 0`
steps in `{−e_2, −e_3}`, in any order: at most `C(n + j, n) 2^j` such paths of
length `n + j`; apply (a) and sum the series. The total-variation bound is the
union over the sites of `C`; the spectral statement follows because
`‖(P_C − 1π_C)^n‖_{∞ → ∞} ≤ 2 sup_w ‖P_C^n(w, ·) − π_C‖_TV` and the spectral
radius is the limit of the `n`-th roots. ∎ Executed at `C_2`, `(3, 1, 2)`: the
maximal total variation between two rows of the orbit quotient's `n`-th power
is below `θ^n` for `n = 1, …, 6`, with `θ = 27/56` (E5).

**(d) The full cross-section.** Assume `c < 1/3` (so `2c < 1` and `θ < 1`).

*(i) The plane kernel on `Z^2`.* For `w ∈ M^{Z^2}` and a quadrant
`Q_a = [a, ∞)^2 ⊂ Z^2`, let `P_{Q_a}(w, ·)` be the law of the in-plane formation
`v_y ~ r(· | w_y, v_{y − e_2}, v_{y − e_3})` over `Q_a` (predecessors outside
`Q_a` omitted), well defined on the countable product by down-set consistency
and the extension theorem cited under Imports. As `a → −∞` these laws converge on every finite
window, uniformly in `w`: for `a' < a`, couple the two formations with sources
the sites of the boundary rays of `Q_a` (whose kernels differ, having one
in-plane predecessor fewer); a site `y` at in-plane distance `≥ d` from the
boundary is reached by at most `2^ℓ` monotone paths of length `ℓ ≥ d`, so its
discrepancy is at most `Σ_{ℓ ≥ d} (2c)^ℓ = (2c)^d/(1 − 2c)`. The limit
`P(w, ·)` is a Markov kernel on `M^{Z^2}`; it is Feller (changing `w_z` is a
source at `z`, whose influence on a window at distance `d` is at most
`c (2c)^d/(1 − 2c)`, a summable tail), and it commutes with the in-plane
translations (the kernels and the predecessor structure are
translation-invariant on `Z^2`).

*(ii) Existence.* `M^{Z^2}` is compact and metrizable; the Cesàro averages of
`δ_w P^n` have a weakly convergent subsequence, and Feller continuity passes
invariance to the limit: an invariant law `π_∞` exists.

*(iii) Uniqueness and translation invariance.* For two invariant laws `π, π'`,
couple the two chains with every site of plane `0` a source: by (c) the
discrepancy at any site of plane `n` is at most `(1 − 2c)^{−1} θ^n → 0`, so
`π = π P^n` and `π' = π' P^n` agree on every finite window. The translate of
`π_∞` is invariant (i), hence equals `π_∞`.

*(iv) Boundary planes are lost.* The full-cross-section law has no boundary
plane; the two-dimensional law survives only in the quadrant column (Q3c–d).

**(e) The `Z^3` law.** Under `c < 1/3`, the stationary two-sided chain of
`P` on `M^{Z^2}` with one-plane law `π_∞` is a law `μ_{Z^3}` on `M^{Z^3}`,
invariant under all lattice translations, with the covariance bound (b) in every
direction and the sweep-direction bound (c). Every box law converges to it on
finite windows as the box's corner recedes in all three directions (in any
manner): the box law is the column law of its cross-section up to the
plane-chain error (Q3b), and the column law over `C` restricted to a window at
in-plane distance `d` from the cross-section's boundary rays differs from the
`Z^2`-chain's law on that window by at most a constant times `(2c)^d/(1 − 2c)`
(couple the two plane chains from a common start; the boundary rays are sources
in every plane, their influence in-plane decays as in (d)(i), and their
accumulated influence along the sweep is summed by (c)). `μ_{Z^3}` is not
invariant under the proper cubic rotations that move the corner (the eight
corner classes are its images under the eight reflections of the axes; whether
they are distinct on `Z^3` is not executed here; on the `2×2×2` cube the
reversed order's law differs, #8102). ∎

**The region.** The hypothesis `c < 1/3` is an exact inequality between
rationals at each triple. It holds at `(3, 1, 2)`, `(5, 2, 4)`, `(7, 3, 5)`,
`(2, 1, 2)`, `(3, 2, 2)`, `(5, 4, 4)`, `(11, 10, 10)` and at the constant rule;
along the line `(1, 1, t)` it fails for large `t` (the sensitivity of three
orthogonal-preferring neighbors to one of them tends to `1/2`), so the region is
a proper subset of the positive octant; its boundary is not computed here. For
two dimensions the same proofs with two predecessors give the region
`2 c_{(2)} < 1`, `c_{(2)} = max(c_1, c_2)`, and the plane law of the plane-law note (#8039; whose
existence needs no condition) has exponentially decaying correlations there:
`60/143 < 1` at `(3, 1, 2)`.

## Corollary Q5 — record two-point functions decay exponentially (at scope)

For every box law, every column law, and for `μ_{Z^3}` when `c < 1/3`, and for
every pair of local record observables `g(v_x)`, `h(v_y)` (in particular every
axis indicator and every function of a record's content),
`|Cov(g(v_x), h(v_y))| ≤ 4 ‖g‖ ‖h‖ (3c)^{⌈|x − y|_1/2⌉ − 1}`. Under the monotone
formation law of a positive covariant nearest-neighbor product rule on the
six-axis menu, in the region, no record two-point function decays slower than
exponentially: neither a lattice Green function nor a transverse kernel appears
in the finished record field. This answers, at scope, the reframing test of the
derivation campaign's record-dynamics block: for this rule family and order
class the record statistics carry no long-range field without a supplied
addition. The static law in the region of block 03 (`6c_1 < 1` there) has the
same property by that block's coupling; at the silent triples this note's
region decides the formation law's decay while the static law's uniqueness
remains undecided.

## No-Go Discipline Gate

The negative sentences of this note are Q2 (the first plane cannot be summed
out; a proved reduction with an executed refutation at two triples) and Q5
(no long-range record correlation in the region; a proved bound). Neither is a
route no-go beyond its scope. The gate is answered for both.

### N1 — Routes by which a long-range record correlation could still arise

| route | what it would attempt | why it fails here, or its obligation | marker |
|---|---|---|---|
| 1 strong coupling, `c ≥ 1/3` | let the branching of discrepancies be supercritical | the bound (a) is then not conclusive; nothing is claimed; the finite-box bounds (a), (b) still hold with a rate `3c ≥ 1` that says nothing | not attempted; obligation named |
| 2 another order class | the snake, a random priority, a non-monotone order | the mechanism (discrepancies along recorded-neighbor paths) applies with the branching number replaced by the maximal out-degree of the recorded-set graph; the random-priority process has the owner's factorial ancestry bound (unlanded, cited, not used) | ATTEMPTED (mechanism named; not executed) |
| 3 a non-product or constraint rule | zero-probability supports (a Gauss-type support rule, #8114's line) | outside the positive product class; the kernels' positivity is what (a) uses | RULED OUT BY PRIOR at scope (positivity is a named premise) |
| 4 the static law at a critical coupling | a supplied coupling on the critical surface of the static specification | a static-law statement; not this note; the coupling is a supplied value | not attempted; obligation named |
| 5 a continuum alphabet or a larger menu | change `c` | `c` is menu-specific; the theorems hold for any finite menu with positive symmetric covariant `φ`; the numbers do not transfer | not attempted; obligation named |
| 6 the constant rule | `p = q = r` | `c = 0`; the law is the independent uniform law; excluded by the variation clause restricted to the menu | ATTEMPTED (control) |

### N2 — Wall-independence audit

Walls: `W_pos` (positivity), `W_menu` (the six-axis menu), `W_class` (the
monotone class with a corner), `W_reg` (`c < 1/3`), `W_var` (nonconstant, for
Q1f and Q2d only). `W_reg` and `W_var` are independent: the constant rule
satisfies `W_reg` and fails `W_var`; a triple far along the line `(1, 1, t)`
satisfies `W_var` and fails `W_reg`. `W_pos` is used by Q3a and Q4a (every kernel value
positive; the maximal coupling); `W_menu` fixes the numbers only; `W_class`
fixes the recorded sets and is the object's definition. None follows from
another. Q1a–e and Q3a–d need `W_pos`, `W_class` only; Q4d–e need `W_reg` in
addition; Q1f and Q2d are stated at the executed nonconstant triples.

### N3 — Hidden-wall scan

Scanned for "we assume", "by construction", "as is standard", "the framework
provides", "naturally", "obviously", "canonical", "registered", "background",
"bridge context". Hits: none in the theorems. Every step of Q1–Q4 is written
out; the cited steps (the extension of a consistent family on a countable product; the
compactness of `M^{Z^2}` and the weak-convergence step of (d)(ii)) are named in
the obligation table and under Imports. No wall was promoted.

### N4 — Per-citation table

| cited surface | residual it attacks | residual claimed here | match |
|---|---|---|---|
| block 05's note (proposed, unaudited): P1, P3, P4, P7(a) | the monotone class on rectangles; the 180-degree identity | Q1a–c one dimension up; Q2b; Q3c | yes (parent; cited and re-proved where used) |
| block 02's note (proposed, unaudited): E1–E3 | the row transfer preserves the chain law | Q2e (the mechanism that has no analogue); Q1e (`K_2`) | yes (parent; cited) |
| block 03's note (proposed, unaudited): the coupling method and `6c_1` | uniqueness of the static law by a random-scan coupling | contrast only (Q5); the method re-proved for a different structure | yes (contrast; no value used) |
| the plane-law note (#8039; landed on main 2026-09-15; not an input) | the plane law by projective consistency | Q2b re-proves the consistency; Q4's 2D remark applies to its law | yes (re-proved) |
| #8102 (open PR; not an input) | the multiset key; reversal on the cube | consistent finite fact quoted in Q4e | yes (quoted; not used) |
| the random-priority note (branch; not an input) | a covariant random-order law on `Z^3` | a different object; N1 route 2 | yes (contrast) |

After dropping nothing, the headline rests on the parents' cited statements and
this note's own proofs and executed witnesses.

### N5 — Resolution audit

| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "no record two-point function decays slower than exponentially" | executed: every `(s, s')` and every pair of axis indicators on the cube against the bound; the exact `2×2` transfer on all 1296 states | executed: every site of the cube (uniform marginals; the influence of the corner on the far corner) | executed: the orbit quotient's contraction for `n = 1..6`; the three-body third difference | executed: the `2×2` cross-section's stationary law by orbit reduction; the `2×3` rectangle's sub-rectangle marginals | proved for `c < 1/3` (Q4e); executed only through the region membership of eight triples; not claimed for `c ≥ 1/3` |

The runner prints matching `per_element:` … `lattice_wide:` lines; the
narrowest form is used.

### N6 — Partial-closure paths and primitive scan

The registered approved primitives in
`docs/audit/data/axiom_premise_nodes.json` (`scale_reference_primitive`,
`kinetic_isotropy_primitive`, `realized_state_primitive`) supply a length
reference, a graining ratio and a realized-state notion; none supplies an
order, a corner, a coupling condition or a pair weight, and none is a wall here.
Reframing paths: a stronger coupling (weighted sensitivities, a block coupling)
could enlarge the region without any change of reading; the random-priority
construction gives a covariant order class whose decay comes from a different
mechanism. `docs/repo/DEFERRED_DECISIONS.md` entry 1 wakes on the
committed-action identification, which this note does not supply. This note
does not say a new axiom is required.

### N7 — Steelman

Hostile reviewer: "The monotone class is an artifact: it has a corner, breaks
the cubic symmetry, and its `Z^3` law is one of eight. Physics, if it uses
formation at all, would use a covariant process — the random-priority law —
whose decay is already faster than exponential. So Q4–Q5 say nothing physical:
the axioms supply no order, and this order is the least covariant one." Reply
at scope: the note selects nothing; it constructs the object the owner's queue
named and proves where it exists, is unique and decays — including at the
couplings where the static law's status is unknown — and it records that the
eight corner laws form one covariant family. The steelman's positive claim
(that a covariant formation process has faster decay) is the owner's separate
construction, unlanded; the comparison of the two families on `Z^3` is the next
block's object. Conceded: nothing here identifies a physical order.

### N8 — Cross-cycle echo

`NO_GO_LEDGER.md` holds block 02's separation on the strip (retired by nothing;
extended by #8039 and here), block 03's silent triples (open), block 04's
two-site criterion (closed for the tested criterion only), and block 05's
turning-staircase negative. The wall structurally nearest to Q2 is block 02's
"the normalizer history does not wash out along the sweep" — a different
statement (the static/formation separation), not retired; the nearest to Q5 is
block 03's contraction region, whose mechanism (a random-scan coupling with six
neighbors) is replaced here by the causal coupling with three predecessors;
this replacement, not a relabeling, is what puts the silent triples inside.

## Falsifiers

- A linear extension of a box's product order whose recorded sets are not the
  predecessor sets (refutes Q1a).
- A configuration of the `1×2×2` or `2×2×1` box on which the product form and
  the product of conditionals differ (refutes Q1e).
- A symmetric pair function `g` with `log K_3(a, b, c) = g(a,b) + g(b,c) + g(a,c)`
  at `(3, 1, 2)` (refutes Q1f; the third difference would then be `1`).
- A plane state of `C_2` on which `μ_{C_2} P_{C_2}` and `μ_{C_2}` agree at
  `(3, 1, 2)` (the count `1296` would drop), or a `2×2` sub-rectangle marginal of
  the `2×3` law that is not the `2×2` law (refutes Q2b).
- A site of `Z^3` whose predecessor triple is the successor triple of a site
  (refutes the mechanism lemma).
- Two distinct stationary laws of `P_{C_2}`, or a row of the orbit quotient that
  depends on the representative (refutes Q3a or the reduction).
- A configuration of the cube on which the exact influence of `v_{000}` on
  `v_{111}` exceeds `6 c^3`, or a pair of axis indicators whose covariance
  exceeds the bound (refutes Q4a–b).
- A triple among the eight where the printed `c` is not the exact maximum over
  all one-entry changes (the runner recomputes the maximum over all
  `6^k × k × 5` cases for `k = 1, 2, 3`).
- Two rows of the orbit quotient's `n`-th power at total variation above `θ^n`
  for some `n ≤ 6` (refutes Q4c at `C_2`).

## Boundaries and non-claims

This note describes the monotone class of formation orders on boxes, columns
and `Z^3` for the declared rule; it states nothing about the static law of
`Z^3` beyond citing block 03's region and the silent triples, nothing about any
order or corner being physical, nothing for `c ≥ 1/3` beyond the finite-box
bounds, and nothing about the distinctness of the eight corner laws on `Z^3`.
No plane, bridge, Born or gravity statement enters this note; this note does
not fire wake condition 1 of the parked statistical-bridge decision. The
unilateral Markov field, the probabilistic cellular automaton and the
positive-chain contraction are classical references re-proved here at the scope used; no
value, constant or theorem is imported as authority.

Further: the two executed refutations of Q2d are at `(3, 1, 2)` and `(5, 2, 4)`;
a proof that the plane transfer moves the two-dimensional law at every
nonconstant triple is not given (the mechanism lemma explains the failure of the
proof, not the truth of the identity's negation); the exact stationary plane law
is computed at the `2×2` cross-section only; the region's boundary in `(p, q, r)`
is not computed beyond the eight triples and the two remarks; the covariance
bound is not sharp (the executed cube influence is well below `6 c^3`); the
`Z^3` law's relation to the random-priority law is not studied; no formation
site, probability or rate is supplied; no axiom or primitive is changed.

## Imports

- `minimal_axioms` (the framework premise node): the sentences quoted under
  Premises.
- Block 05's and block 02's notes on main (proposed, unaudited): the rectangle
  law, P1, P3, P4, P7(a); E1–E3. The parts used are restated and, where load-
  bearing (Q2b, Q3c), re-proved from P7(a).
- Elementary mathematics re-proved at scope: the Doeblin contraction of a
  strictly positive stochastic matrix (Q3a); the coupling of two laws with a
  maximal coupling and the triangle inequality for total variation (Q4);
  monotone-path counts and the binomial series `Σ_j C(n+j, n) x^j = (1 − x)^{−n−1}`
  (Q4c); the level-chain conditioning (Q4b).
- Cited, definition-level: the Kolmogorov extension of a consistent family on
  a countable product (Q3d, Q4d); compactness of `M^{Z^2}` and the weak
  subsequential limit of Cesàro averages with Feller continuity (Q4d(ii), the
  classical Krylov–Bogolyubov argument, four lines); uniqueness of a measure on
  a generating π-system (Q4d(iii)).
- No literature value, constant, or theorem enters as authority; the classical
  names appear only in this section and under Prior art.

## Review record

Supervisor-run block (the owner's 2026-09-15 directive: no subagents). The
supervisor's controls (`specs/supervisor_control_block08_z3.py`, `_b.py`) computed
the sensitivities, the `2×2` transfer witness, the third difference, the 48
extensions, the exact stationary `2×2` law and the cube influence before the
contract was written; the contract's lens pass (refuter, prior art, axiom
reading, scope) is recorded in `GOAL_block08.md`; the primary seat wrote the
proofs and the runner; the refuting pass recomputed the load-bearing numbers
by disjoint routes (`CHECKER_block08_findings.md`: the `2×2` transfer's total
variation from the integer-weighted cube marginal on the plane `x_1 = 1`, `c_3`
from the integer `φ`-formulation with total variation as a sum of positive parts,
the stationary law by power iteration against the exact solve, the path count
`N(000, 111) = 6` by enumeration, and the pair-additive control of the third
difference); the fold is recorded in `REVIEW_HISTORY.md`.
Facts settled while executing: the integer-weighted cube pass needs the
common denominator `6 Z_1^3 (lcm Z_2)^3 (lcm Z_3)`, not the lcm of the factors
(the first draft's assertion caught it); the first draft placed `(2, 1, 2)` on
the region's boundary by misreading `3c = 1/3` as `3c = 1` — corrected: it lies
inside; the classical names were moved out of the theorem sections and the
status block.

## Verification

```bash
python3 scripts/admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_2026_09_15.py
python3 scripts/admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_2026_09_15.py --exact
python3 scripts/admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_2026_09_15.py --mutation transfer_invariance_claimed
```

Families: A authority and inputs; B the box law (extensions, covariance, axis
symmetry, down-sets, the product form, the three-body term); C the first plane
(the `2×2` transfer witness, the constant control, the two-dimensional
consistency); D the plane chain (positivity, the orbit quotient, the exact
stationary law, the boundary lines); E the coupling (the sensitivities, the
influence and covariance bounds against exact values, the sector contraction,
the region); F fences, forbidden phrases, the floating-point self-scan and the
placement of the classical names; G the resolution lines. Each of the 26
declared mutations perturbs one object or one comparison and fails in exactly
one family (`mutation_family_expected:` / `mutation_family_observed:` lines);
`--exact` prints the rational endpoints and the stationary `2×2` law's orbit
masses. Expected final line: `TOTAL: PASS=33 FAIL=0`.
