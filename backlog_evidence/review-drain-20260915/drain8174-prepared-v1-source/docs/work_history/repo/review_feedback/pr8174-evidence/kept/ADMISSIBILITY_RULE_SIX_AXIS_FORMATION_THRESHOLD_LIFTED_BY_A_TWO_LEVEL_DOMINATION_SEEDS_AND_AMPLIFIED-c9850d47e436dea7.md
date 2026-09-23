---
claim_id: admissibility_rule_six_axis_formation_threshold_lifted_by_a_two_level_domination_seeds_and_amplified_nodes_in_the_explanation_tree_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "For the three-dimensional monotone formation law of the covariant product rule on the six-axis menu with positive orbit weights (p, q, r), read as the level automaton on Z^2, started from the all-a plane, with the three deviations d_1 = 1 - p^3/(p^3 + q^3 + 4 r^3), d_2 = 1 - p^2 q/(p q (p + q) + 4 r^3), d_3 = 1 - p^2 r/(r (p^2 + q^2) + r^2 (p + q) + 2 r^3): (T1) the dissent indicator is dominated by the two-level noisy majority automaton eta' — a site with at least two 1-predecessors is 1, a site with exactly one is 1 with probability epsilon_2 = max(d_2, d_3), a site with none with probability epsilon_1 = d_1, through i.i.d. uniforms (proved; the closed forms and the monotonicity in p re-checked); (T2) every 1 of eta' at x has an extended explanation tree: a subtree of G through 1-sites with at most one arrow to a predecessor per node, seeds S (no arrow to a predecessor; no 1-predecessor), amplified nodes A (an amplification arrow to their single 1-predecessor), processed nodes (an excuse arrow), with forks = |S| - 1 and excuse arrows E <= 3(|S| - 1) + 2|A| (proved; executed on every configuration of the depth-2 cone, every depth-3 configuration with at most four noise sites and random cones); (T3) P(eta'_x = 1) <= epsilon_1 R(t + epsilon_2/t^2, epsilon_1/t^3) for every t in (0, 1] with the point in the domain of the recursion D = (1+xU)^2(1+3xD)(1+yF)^6, U = (1+xU)^3(1+yF)^6, F = (1+xU)^3(1+3xD)(1+yF)^5, R = (1+xU)^3(1+3xD)(1+yF)^6 (proved); (T4) with exact rational super-solutions, the formation law keeps its plane and its level automaton has at least six invariant laws for p >= 4165 at (p, 1, 2), p >= 2085 at (p, 1, 1), p >= 8330 at (p, 2, 4), p >= 6247 at (p, 1, 3) — a factor 69 below block 25's 285718, 142861, 571436, 428576 (proved; the certificates exact); (T5) the recursion's domain at y = 0 is x < 4/27, so this route needs epsilon_2 < 256/531441, which on (p, 1, 2) fails for every p <= 4150: the route is at its ceiling (proved). Not claimed: the location of the true strength (block 28 locates it at p in (10.5, 11) on (p, 1, 2)); the tree-of-trees refinement that would reach p of order 200 (its overlaps break the budgets; named). No reading, rule or coupling is selected as physical; exact arithmetic throughout the runner."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_six_axis_formation_threshold_two_level_domination_seeds_and_amplified_nodes_2026_09_16.py
---

# The six-axis formation threshold lifted by a two-level domination: seeds and amplified nodes in the explanation tree, `p ≥ 4165` at `(p, 1, 2)` from `285718`, and the route's ceiling

**Date:** 2026-09-16
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

Block 25 proves that the six-axis formation law keeps a plane of identical
records once the rule's preference for agreement is strong enough, with the
region `p ≥ 285718` at weights `(p, 1, 2)`; block 28 locates the actual
strength at `p ∈ (10.5, 11)`. Block 25's count of explanation trees is at its
own edge, so the slack is elsewhere: in the step that dominates the formation
law by a majority automaton with noise. That step uses the worst case over all
predecessor triples with two agreeing records — a dissent probability of order
`2/p` — while in the ordered state almost every site sees three agreeing
predecessors and dissents with probability only `d_1 ≈ 33/p³`.

This note replaces the single noise level by two. A site whose three
predecessors all agree is a *seed* of dissent with probability `ε₁ = d_1`; a
site with exactly one dissenting predecessor is *amplified* with probability
`ε₂ = max(d_2, d_3)`; a site with two dissenting predecessors dissents by
majority. The explanation tree of block 25 is extended to carry both: seeds
are its leaves, amplified nodes sit inside its clusters with an arrow to their
single dissenting predecessor, and the potential that drives the construction
loses one unit whenever an amplified node is a pole for the charge along its
own arrow. The accounting closes with `forks = |S| − 1` and
`E ≤ 3(|S| − 1) + 2|A|`, the same generating-function count applies with the
amplification arrows sharing the arrow slots, and the ordered phase follows
wherever `(t + ε₂/t², ε₁/t³)` lies in the recursion's domain. With exact
certificates this gives `p ≥ 4165` at `(p, 1, 2)` — a factor `69` below block
25 on every line of weights. The route's ceiling is also exact: the domain
ends at `x = 4/27`, so it needs `ε₂ < 256/531441`, which on `(p, 1, 2)` fails
for `p ≤ 4150`. What remains between `4165` and the located `11` is a factor
`380`, and the note names the two places it sits: the two excuse arrows an
amplified pole may cost (the executed trees never use more than two thirds of
one), and the overcounting of sub-structures inherent in the union bound.

In plain words: the earlier proof treated every record as if it could be
tempted to dissent by the worst company it might keep; the new proof charges
each dissent by the company it actually keeps — a dissent among three
agreeing neighbours is rare, and only a dissent next to an existing dissent is
cheap. That brings the proved strength from three hundred thousand to four
thousand, while the truth is eleven.

Exactly: the two-level domination (T1); the extended tree with its budgets
(T2); the bound (T3); the certificates at four weight pairs (T4); the ceiling
(T5). Executed with exact arithmetic: 20 checks, 11 mutations; the construction
run on `4290` configurations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the campaign queue's first item after block 28: the six-axis order threshold toward the located strength (285718 proved against 11 located at (p, 1, 2))"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the threshold lifted to p >= 4165 at (p, 1, 2) (2085, 8330, 6247 on the other lines) by the two-level domination; the route's ceiling reached (epsilon_2 < 256/531441). Open: the bad-pair accounting (2 excuse arrows per amplified pole, executed at most 2/3) — a proof of E <= 3(|S| - 1) + |A| would give p of order 500; the tree-of-trees refinement (weight epsilon_2 with no bad pairs, p of order 200) blocked by overlaps; the count's overcounting of sub-structures. Consumers: the campaign's decision record; #8093's assembly"
conditional_surface_status: "T1-T5 proved for every positive weight triple (T4 with content on the four lines at the stated couplings); the construction executed exhaustively on the depth-2 cone and on all depth-3 configurations with at most four noise sites plus random cones; conditional on the records-only reading, positivity, the six-axis menu and the monotone order as supplied conditions; three standard mathematical imports named at definition level"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", "Records form.", and "Only records are readable.". Block 01 (`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`, on `main`) supplies the rule and its one-site conditional given a recorded set; the monotone formation order, its level reading, the coarse-graining and the explanation-tree construction are declared and re-proved below (blocks 05, 08, 12, 25, 28 — open PRs #8003, #8138, #8146, #8168, #8172 — are referenced as evidence addresses only). All proposed and unaudited.

Declared objects.
- **The rule, level time, the level automaton, the coarse-graining, the deviations.** As in block 25 (PR #8168), restated: the six-axis menu with `φ(v, v') = p, q, r` for equal, antipodal, orthogonal pairs; sites `x ∈ Z³`, level `τ(x) = x_1 + x_2 + x_3`, predecessors `x − e_j`, siblings `x ± (e_i − e_j)`; records form level by level from `K(· | v_{x−e_1}, v_{x−e_2}, v_{x−e_3}) ∝ Π_j φ(v, v_{x−e_j})`, level `0` all equal to `a`; `ξ_x = 1{v_x ≠ a}`; `d_1 = 1 − K(a | a, a, a)`, `d_2 = 1 − K(a | a, a, −a)`, `d_3 = 1 − K(a | a, a, b)` for `b ⊥ a`, in the closed forms of the front matter; `ε₁ := d_1`, `ε₂ := max(d_2, d_3)`.
- **The two-level noisy majority automaton `η'`.** With i.i.d. uniforms `U_x` on levels `≥ 1` and `η' ≡ 0` on levels `≤ 0`: `η'_x = 1` if at least two of `η'_{x−e_j}` are `1`; `η'_x = 1{U_x < ε₂}` if exactly one is `1`; `η'_x = 1{U_x < ε₁}` if none is. A **1-site** has `η'_x = 1`; a **seed** is a 1-site with no 1-predecessor; an **amplified site** is a 1-site with exactly one 1-predecessor (its **amplification direction** `j` is the index of that predecessor); a **processed-type site** has at least two, and its **winning pair** is the pair of 1-predecessors with the two smallest indices.
- **The graph `G`, the functionals, spanned sets, the excuse.** As in block 25: arrows `{x, x − e_j}`, forks `{x, x ± (e_i − e_j)}`, degree `12`; `M_k(z) = z_k − τ(z)/3`; `Span(P, v_1, v_2, v_3) = Σ_k M_k(v_k)`; for a processed-type `v`, `Excuse_k(v)` is the winning-pair member with index `≠ k` (the smaller if both), with `M_k(Excuse_k(v)) = M_k(v) + 1/3`; for an amplified `v` with direction `j`, `Excuse_k(v) := v − e_j` for every `k`, with `M_k(v − e_j) − M_k(v) = 1/3 − δ_{jk}`; the pair `(v, k)` is **bad** if `v` is amplified with direction `k`.
- **The extended arrow graph and clusters.** At level `s`, vertices the 1-sites of levels `≤ s`, an edge from every processed-type or amplified site to each of its 1-predecessors; a **cluster at level `s`** is the intersection with level `s` of a connected component. A seed is a singleton cluster.
- **Extended explanation trees.** Subtrees `T` of `G` containing `x` with at most one arrow to a predecessor at each node; `S(T)` the nodes without such an arrow, `A(T)` the nodes whose arrow to a predecessor is labelled an amplification arrow, `E(T)` the number of excuse arrows, `F(T)` the number of forks; `𝓔` the family with `F = |S| − 1` and `E ≤ 3(|S| − 1) + 2|A|`.
- **The recursion and its domain.** `D = (1 + xU)²(1 + 3xD)(1 + yF)⁶`, `U = (1 + xU)³(1 + yF)⁶`, `F = (1 + xU)³(1 + 3xD)(1 + yF)⁵`, `R = (1 + xU)³(1 + 3xD)(1 + yF)⁶` (block 25's count, restated in T3); its **domain** `𝒟` is the set of `(x, y) ≥ 0` at which the iteration from `(1, 1, 1)` stays bounded; a **super-solution** at `(x, y)` is a triple `(D̄, Ū, F̄) ≥ 1` dominating its own right sides.

## Prior art and what is new

Toom's stability theorem for eroders under small noise, in Gács's exposition of the Berman–Simon proof, is the route block 25 carried in level-time coordinates with an explicit threshold; block 12 supplied the domination of the formation law by the noisy majority automaton at the worst-case noise, and block 25 sharpened the count to its edge. None is used as authority: the construction is restated and re-proved here in its extended form. What is new: (i) the two-level domination (T1), which separates seeding from amplification; (ii) the extended explanation tree with amplified nodes inside the clusters, the bad pairs, and the closed accounting `forks = |S| − 1`, `E ≤ 3(|S| − 1) + 2|A|` (T2); (iii) the bound with the amplification arrows in the arrow slots (T3) and the region with exact certificates, a factor `69` below block 25 on every line (T4); (iv) the route's exact ceiling `ε₂ < 256/531441` with the two named places where the remaining factor `380` to the located strength sits (T5, N1).

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T1 | `ξ ≤ η'` from the all-`a` plane; `ε₁ = d_1`, `ε₂ = max(d_2, d_3)`, decreasing in `p` | block 12's coupling, refined by the predecessors' state | B |
| T2 | the extended tree: `F = |S| − 1`, `E ≤ 3(|S| − 1) + 2|A|` | block 25's construction with amplified poles; bad pairs; the potential | C |
| T3 | `P(η'_x = 1) ≤ ε₁·R(t + ε₂/t², ε₁/t³)` | the lift to the typed tree; the budget in the exponent | D |
| T4 | the region on four lines; six invariant laws | exact super-solutions; monotonicity; the Cesàro route | D |
| T5 | the ceiling `x < 4/27`, `ε₂ < 256/531441`; `p > 4150` on `(p, 1, 2)` | tangency of `U = (1 + xU)³`; a one-variable maximum | E |

## Theorem T1 — the two-level domination

**Statement.** (a) `d_1, d_2, d_3` have the closed forms of the front matter and are strictly decreasing in `p > 0` at fixed `q, r > 0`; `d_1 ≤ max(d_2, d_3)`. (b) There is a coupling of the formation law from the all-`a` plane with `η'` such that `ξ_x ≤ η'_x` at every site; hence `P(v_x ≠ a) ≤ P(η'_x = 1)`.

**Proof.** (a) Block 25's T0(a)–(b), re-executed (B1–B2); `d_1 ≤ d_3` because `K(a | a, a, a) ≥ K(a | a, a, b)` (the normalizer with three factors `p` is smaller relative to `p³` than that with `p, p, r` relative to `p²r`: both are `1 − (ratio)` with the aligned triple's dissent mass `q³ + 4r³` over `p³` against `(rq² + r²(p + q) + 2r³)/(p²r) ≥ 4r³/p³` — executed at the four lines, B2). (b) Build both processes level by level given the previous level with `ξ ≤ η'`. At `x`: if at least two `η'`-predecessors are `1`, set `η'_x = 1 ≥ ξ_x`. If exactly one is `1`, at most one `ξ`-predecessor is `1`, so at least two of `v`'s predecessors equal `a` and `P(ξ_x = 1 | past) = 1 − K(a | preds) ≤ max(d_1, d_2, d_3) = ε₂`; draw `ξ_x` and `η'_x = 1{U_x < ε₂}` monotonically from one uniform. If none is `1`, all three of `v`'s predecessors equal `a` and `P(ξ_x = 1 | past) = d_1 = ε₁`; couple with `1{U_x < ε₁}`. Sites of a level are drawn independently given the previous level in both processes. ∎

## Theorem T2 — the extended explanation tree

**Statement.** Let `η'_x = 1`. Then there is `T ∈ 𝓔` rooted at `x` all of whose nodes are 1-sites, such that every node of `S(T)` is a seed, every node of `A(T)` is an amplified site whose amplification arrow ends at its single 1-predecessor, and every other node is processed-type with its excuse arrow to a 1-predecessor.

**Proof.** The construction is block 25's with three changes: the arrow graph links amplified sites to their single 1-predecessor, so they lie inside clusters; the excuse of an amplified pole is that predecessor, for every charge; and bad amplified poles are always kept. The ingredients, restated.
*(T2.1, clusters and the cause graph.)* For a cluster `K` at level `s` with no seed, let `V_K` be the clusters at level `s − 1` containing a 1-predecessor of a point of `K`, two of them adjacent if a fork joins a point of one to a point of the other; this graph is connected and every `Excuse_k(v)`, `v ∈ K`, lies in a cluster of `V_K`. Proof: two points of `K` are joined by a path through 1-sites of levels `≤ s`; cut it at its visits to level `s`; between visits it stays below and its end predecessors are in one cluster of level `s − 1`; at a visit `k` it arrives from a 1-predecessor `r` and leaves to a 1-predecessor `r'` (equal if `k` is amplified), and `r, r'` are siblings or equal, hence forked or in one cluster; any cluster of `V_K` contains a predecessor of some `k ∈ K`, a sibling of the one the path uses. The excuse of a point is one of its 1-predecessors.
*(T2.2, the excuse identity.)* For a spanned set `(P, v_1, v_2, v_3)` with no seed pole, `Σ_k M_k(Excuse_k(v_k)) = Span + 1 − b`, where `b` is the number of bad pairs `(v_k, k)`: each processed-type pole contributes `+1/3` for its charge, an amplified pole `+1/3` for the charges other than its direction and `−2/3` for its direction (C1). A fork pair has `Size = 1`, so a spanned set on it has `Span ≤ 1` (block 25's T2(b)).
*(T2.3, the spanning lemma.)* Block 25's T3 verbatim: for a spanned set `(L, u_1, u_2, u_3)`, disjoint clusters `𝓒`, forks `𝓕` between distinct clusters with the bipartite cluster–fork graph connected and `u_k ∈ C_k ∈ 𝓒`, there is a minimal subtree `𝒯` through `C_1, C_2, C_3` and poles `u_{X,k} ∈ X' ⊂ X` for `X ∈ 𝒯` with `Σ_{X∈𝒯} Σ_k M_k(u_{X,k}) = Σ_k M_k(u_k)`, `X'` the transported poles and meeting points, every point of `X'` a pole of `X`, `X' = X` for a fork. (Its proof — shortest paths, pruning, the transport of poles toward the terminals, and the count `#{X ∈ I(v) : u_{X,k} = v} = |I(v)| − 1 + [v = u_k]` — does not use the nature of the poles and is unchanged; it is asserted at every refinement executed, C2–C4.)
*(T2.4, refinement and accounting.)* A partial tree: unprocessed spanned clusters `𝒰`, processed points, and edges (excuse arrows, amplification arrows, forks) whose cluster-contracted graph is a tree; potential `Φ = Σ_𝒰 Span + #forks`. Start with `({x}, x, x, x)`, `Φ = 0`. While an unprocessed cluster `(K, v)` has a non-seed pole (then `K` has no seed, a seed being a singleton): put `u_k = Excuse_k(v_k)`, `b` the number of bad pairs; apply T2.3 to `(∪V_K, u_1, u_2, u_3)` with the clusters of `V_K` and one fork per adjacent pair; add the clusters of `𝒯` with their poles to `𝒰` and the forks of `𝒯` as edges; the *kept poles* are the distinct points among `v_1, v_2, v_3` that are incident to an existing edge or are bad amplified poles (if none, `v_1`); for a kept processed-type `w` add the excuse arrow `{w, u_{k(w)}}`, `k(w)` the least `k` with `v_k = w`; for a kept amplified `w` add the amplification arrow `{w, w − e_j}` to its predecessor; delete `(K, v)`. *Tree property:* as in block 25 — `K` is replaced by `𝒯` with the kept points attached by one arrow each; a cluster at level `s − 1` has all its level-`s` parents in one cluster, now also for amplified parents (they are linked to their predecessor), so no cluster is added twice; kept points are processed once. *The potential:* by T2.2 and T2.3, `Σ_{X∈𝒯} Span(X) = Span(K) + 1 − b`, and each fork counts `1` against a span of at most `1`, so `Φ` rises by at least `1 − b`. *Termination:* levels descend; every 1-site at level `1` is a seed. *The count:* let `S` be the seeds left as singleton clusters, `A` the kept amplified points, `B = Σ b` over refinements. `Φ` ends at `#forks` and rose by at least `1 − b` per refinement from `0`, so `#refinements ≤ #forks + B`. Contract every arrow of either kind into its lower point: each processed point and each amplified point merges, along its own arrow and the arrows below, into a seed; the forks then form a tree on the seeds, so `#forks = |S| − 1`. A bad pair is an amplified pole in its own direction; a point is a pole of at most one refined cluster (its own) and is bad for at most one charge, and bad amplified poles are kept, so `B ≤ |A|`. Arrows number at most three per refinement (one per kept pole) and every kept amplified pole carries an amplification arrow, so `E + |A| ≤ 3(|S| − 1 + B) ≤ 3(|S| − 1) + 3|A|`, i.e. `E ≤ 3(|S| − 1) + 2|A|`. Every node has at most one arrow to a predecessor (its own), the nodes without one are the seeds, and the amplified nodes' arrows end at their single 1-predecessor. ∎

Executed (C2–C4): on every noise configuration of the depth-2 backward cone (`932` explained), on every depth-3 configuration with at most four noise sites (`2321`), and on random cones of depth `3`–`8`, the extended construction never fails, the identity `Σ_X Span(X) = Span(K) + 1 − b` holds at every refinement, the point graph is a tree of arrows and forks through 1-sites, seeds have no 1-predecessor, amplified nodes have exactly one at their arrow's end, `#forks = |S| − 1`, `#refinements ≤ |S| − 1 + B`, `B ≤ |A|`, and `E ≤ 3(|S| − 1) + 2|A|`; the largest executed value of `(E − 3(|S| − 1))/|A|` is `2/3`.

## Theorem T3 — the count and the bound

**Statement.** For every site `x` and every `t ∈ (0, 1]` with `(t + ε₂/t², ε₁/t³) ∈ 𝒟`,
```
P(η'_x = 1) ≤ ε₁ · R(t + ε₂/t², ε₁/t³).
```

**Proof.** By T2 and independence of the uniforms at distinct sites, `P(η'_x = 1) ≤ Σ_{T∈𝓔} ε₁^{|S(T)|} ε₂^{|A(T)|}` (a seed has `U < ε₁`, an amplified node `U < ε₂`). For `T ∈ 𝓔`, `|S| = F + 1` and `E ≤ 3F + 2|A|`, so with `t ≤ 1`: `ε₁^{|S|} ε₂^{|A|} = ε₁·ε₁^{F}·ε₂^{|A|} ≤ ε₁ · t^{E}·(ε₁/t³)^{F}·(ε₂/t²)^{|A|}`. The right side is the weight of `T` with `t` per excuse arrow, `ε₂/t²` per amplification arrow and `ε₁/t³` per fork; both kinds of arrow are arrows of `G` (an edge to a predecessor), so in the lift of `T` to the typed regular tree (block 25's lift: the words of edge types along root paths, injective, with at most one *down* child per vertex and none after an *up* letter) an arrow slot carries the total weight `t + ε₂/t²`. The weight sum over all admissible subtrees of the typed tree is `lim_h R_h(x, y)` with `x = t + ε₂/t²`, `y = ε₁/t³`, where `R_h` are the recursion's height-`h` truncations from `(1, 1, 1)`; a super-solution bounds every `R_h` by induction (the right sides are increasing), so the sum is at most `R̄`, and `(x, y) ∈ 𝒟` is exactly the existence of a bounded iteration. ∎ (D1: the lift's slot structure re-executed on the enumerated subtrees with `≤ 4` edges as in block 25; D2: the certificates.)

## Theorem T4 — the region

**Statement.** With `ε₁ = d_1`, `ε₂ = max(d_2, d_3)`: the formation law from the all-`a` plane satisfies `P(v_x ≠ a) ≤ ε₁ R̄ < 10⁻⁷` at every later site, and its level automaton has at least six pairwise distinct translation-invariant invariant laws, for every integer `p ≥ 4165` at `(p, 1, 2)`, `p ≥ 2085` at `(p, 1, 1)`, `p ≥ 8330` at `(p, 2, 4)`, `p ≥ 6247` at `(p, 1, 3)`.

**Proof.** At `p = 4165, q = 1, r = 2`: `t = 99/1000`, `x = t + ε₂/t² = 0.14804…`, `y = ε₁/t³ = 4.7·10⁻⁷`, and the rational triple `(D̄, Ū, F̄)` of the runner is a super-solution with `R̄ = 168.44…`, so `P(v_x ≠ a) ≤ ε₁ R̄ = 7.7·10⁻⁸` (D2); the other three lines likewise (`t = 49/500`, `99/1000`, `99/1000`; `R̄ = 131.3, 168.4, 145.0`; bounds `7.2, 7.7, 6.5 × 10⁻⁸`). For larger `p` on a line, `ε₁` and `ε₂` decrease (T1a), the recursion's right sides are increasing in `x, y`, so the same triple is a super-solution and the same bound holds. The six laws: block 25's T7 route — the kernel is Feller and translation-covariant, Cesàro averages of the levels from the all-`a` plane have subsequences with weak limits `μ_a` are invariant, `μ_a(v_y ≠ a) ≤ 10⁻⁷ < 1/2`, so the six are distinct, and by the extremal decomposition at least six extremal laws exist. ∎ (D2–D3.)

## Theorem T5 — the ceiling of the route

**Statement.** `(x, 0) ∈ 𝒟` if and only if `x ≤ 4/27`. Hence T3 can apply only if `ε₂ < max_{0<t<4/27} t²(4/27 − t) = 256/531441`, and on `(p, 1, 2)` this fails for every `p ≤ 4150` (`d_3(4150) = 16622/34461622 > 256/531441`).

**Proof.** At `y = 0` the recursion for `U` is `U = (1 + xU)³`; with `v = 1 + xU ≥ 1` this reads `x = (v − 1)/v³`, whose maximum over `v ≥ 1` is `4/27` at `v = 3/2` (E1); for `x > 4/27` the iteration from `1` has no fixed point and diverges, for `x ≤ 4/27` it is bounded by the least fixed point. Since `x = t + ε₂/t² ≤ 4/27` needs `ε₂ ≤ t²(4/27 − t)`, whose maximum over `t` is at `t = 8/81` with value `256/531441` (E1), the route needs `ε₂ < 256/531441`. `d_3` is decreasing in `p`, and its value at `p = 4150` exceeds `256/531441` (E2). ∎

*Reading.* The route is at its ceiling on every line (`p = 4165` against `4150`): the seed noise plays no role there, only the amplification. Two places hold the remaining factor `380` to the located strength `11`. First, the bad-pair accounting charges two excuse arrows per amplified pole (`E ≤ 3(|S| − 1) + 2|A|`), which enters the exponent as `ε₂/t²`; the executed trees never exceed `2/3` of an excuse arrow per amplified node, and a proof of `E ≤ 3(|S| − 1) + |A|` would put the ceiling at `ε₂ < max_t t(4/27 − t) = 4/729` and the region near `p ≈ 500`. Second, the union bound counts every sub-structure of an amplification cluster separately, so the amplification part is finite only for `ε₂ < 4/27` where the branching itself dies out for every `3ε₂ < 1`: the same gap as between lattice-animal and branching-process thresholds. A tree-of-trees construction (fresh trees under amplified leaves, weight `ε₂` with no bad pairs) would reach `p ≈ 200` if its sub-trees did not overlap; they do, and overlaps break the budgets (N1).

## No-Go Discipline Gate

This note's sentence is positive (an ordered region); its escapes are named for the route by which it could fail.

### N1 — Routes by which T4 could fail, and the routes tried beyond it
1. *The extended construction failing on some configuration or exceeding a budget* — closed on `4290` configurations (C2–C4) and by the proof (T2).
2. *The amplified node treated as a noise leaf* — would charge its fork at `ε₂/t³` and give nothing; the construction puts it inside the clusters instead, at the price of the bad pairs.
3. *Bad pairs not kept* — a bad amplified pole that is not a tree node would lose span without paying `ε₂`; hence bad poles are always kept (T2.4).
4. *The tree-of-trees route* — fresh block-25 trees under amplified leaves would give weight `ε₂` per amplified node with `E ≤ 3(|S| − 1)`; the sub-trees can share nodes with the existing structure, the union then has cycles, and breaking them by dropping forks or arrows breaks the budgets (each dropped fork costs three excuse arrows in the accounting); recorded as the obstacle to `p ≈ 200`.
5. *The sharper bad-pair budget* — `E ≤ 3(|S| − 1) + |A|` holds on every executed tree (`2/3` at most) but is not proved: a refinement with a bad amplified pole may keep two other poles.
6. *The domination* — re-proved (T1) at the level of the predecessors' state.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
No hidden dependence: the inputs are the axioms' sentences, block 01's rule, and the monotone order as declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the four sentences under Premises | yes (premise) |
| block 01 (`main`) | the rule and its one-site conditional | yes (premise, proposed) |
| blocks 12, 25 (open PRs) | the coupling and the construction, re-proved here in extended form | re-proved at scope (T1, T2, T3) |
| block 28 (open PR) | the located strength `p ∈ (10.5, 11)` | placement only (evidence address) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the formation law keeps its plane for `p ≥ 4165` at `(p, 1, 2)`" | executed: the deviations' closed forms and monotonicity; `d_1 ≤ max(d_2, d_3)`; the increments of an amplified excuse | executed: the two-level coupling's inequality at every predecessor state; the ceiling's crossing at `4150` | executed: the extended construction on `4290` configurations with all budgets; the lift's slot structure on subtrees with `≤ 4` edges | executed: the four super-solution certificates; the bounds; the one-variable maxima | proved for every `p` above the stated couplings on the four lines (T1–T5); the true strength not claimed |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling or order; none is a wall.

### N7 — Steelman
Hostile reviewer: "A factor `69` when the truth is `26000` times below." Reply: the factor is the whole reach of this route, proved as such (T5); the two places holding the rest are named with the executed evidence (`2/3` against `2`) and the obstacle (overlaps). Conceded: the true strength is not located by a proof; `4165` is not close to `11`.

### N8 — Cross-cycle echo
Block 12's domination is refined; block 25's construction is extended and its count reused at its edge; block 28's located strength is the target the region is measured against; block 26's tree-of-trees obstacle (overlaps) is the same kind of obstacle met here.

## Falsifiers
- A deviation differing from its closed form, non-decreasing in `p`, or `d_1 > max(d_2, d_3)` at some tested line; a failure of the two-level coupling's inequality at some predecessor state (B1–B3).
- An increment of an amplified excuse other than `1/3 − δ_{jk}`; a configuration of the tested cones on which the extended construction fails, the identity `Span + 1 − b` fails, the point graph is not a tree, a seed has a 1-predecessor, an amplified node's arrow does not end at its single 1-predecessor, `#forks ≠ |S| − 1`, `#refinements > |S| − 1 + B`, `B > |A|`, or `E > 3(|S| − 1) + 2|A|` (C1–C4).
- A lifted subtree count above the recursion's coefficient; a super-solution inequality failing at one of the four points; `ε₁ R̄ ≥ 10⁻⁷` (D1–D3).
- `(v − 1)/v³ > 4/27` for some `v ≥ 1`, `t²(4/27 − t) > 256/531441` for some `t`, or `d_3(4150) ≤ 256/531441` (E1–E2).

## Boundaries and non-claims
This note proves, for the six-axis formation law in level time, that its dissent from the all-`a` plane is dominated by the two-level noisy majority automaton with seed noise `d_1` and amplification noise `max(d_2, d_3)`, that this automaton's ones have extended explanation trees with `forks = |S| − 1` and `E ≤ 3(|S| − 1) + 2|A|`, that its density of ones is at most `ε₁ R(t + ε₂/t², ε₁/t³)`, and hence that the formation law keeps its plane with at least six invariant laws for `p ≥ 4165` at `(p, 1, 2)`, `p ≥ 2085` at `(p, 1, 1)`, `p ≥ 8330` at `(p, 2, 4)`, `p ≥ 6247` at `(p, 1, 3)`, with the route's ceiling `ε₂ < 256/531441`; it does not locate the true strength, does not prove the sharper bad-pair budget, does not treat other menus or orders, does not select a reading, rule or coupling as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 01 (on `main`): the rule and its conditional; proposed, unaudited. PRs #8003, #8138, #8146, #8168, #8172 (open) referenced as evidence addresses for the monotone class, the uniqueness region, the level-time reading, the construction and the located strength.
- Re-proved at scope: block 12's domination (refined to two levels); block 25's construction (extended) and count; the Cesàro construction of invariant laws and the distinctness (block 25's T7).
- Named standard imports at definition level (never as authority for physics): the union bound and independence of the uniforms; weak compactness of laws on a compact product space (the Krylov–Bogolyubov construction for Feller kernels); the extremal decomposition of invariant laws (Choquet).
- Reference only (named, not used): Toom (1980); Berman–Simon (1988); Gács (2021); Swart–Szabó–Toninelli (2022).

## Review record
Supervisor-run block (owner directive 2026-09-16, evening: "take the six-axis threshold next"). The lens found the domination step, not the count, to be the loose one at the located strength (`ε ≈ 0.26` worst case against `d_1 ≈ 0.024` and `d_3 ≈ 0.21` at `p = 11`). The control (`specs/supervisor_control_block30_core.py`, `..._construction.py`) extended block 25's construction with amplified nodes and ran it on `4290` configurations with every budget checked; the scan (`..._scan.py`) found the region's edge at `p = 4166` on `(p, 1, 2)` and its coincidence with the ceiling `4/27`; the certificates (`..._certify.py`) were found along the Jacobian's dominant eigenvector at spectral radius `0.99` and verified exactly; the budget measurement (`..._budget.py`) found the executed maximum `2/3` of the allowed `2` excuse arrows per amplified node. Facts settled while executing: the tree-of-trees route (fresh trees under amplified leaves) was worked out to the point of its obstacle — the overlaps — and dropped; the alternative of leaving amplified nodes as leaves was computed to give nothing; the route's ceiling is reached on every line within one unit of `p`. The refuting pass (`CHECKER_block30_findings.md`) simulated the two-level automaton and the six-axis law coupled through shared uniforms far below the proved region, checked the domination pointwise, re-ran the tree checks with an independent graph implementation, and re-derived the certificates' fixed points in floating point.

## Verification

```bash
python3 scripts/admissibility_rule_six_axis_formation_threshold_two_level_domination_seeds_and_amplified_nodes_2026_09_16.py
python3 scripts/admissibility_rule_six_axis_formation_threshold_two_level_domination_seeds_and_amplified_nodes_2026_09_16.py --list-mutations
python3 scripts/admissibility_rule_six_axis_formation_threshold_two_level_domination_seeds_and_amplified_nodes_2026_09_16.py --mutation budget_amplified_dropped
```

Families: A authority and inputs; B the deviations, the domination; C the extended construction executed; D the lift, the certificates, the bounds; E the ceiling; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 11 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=20 FAIL=0`.
