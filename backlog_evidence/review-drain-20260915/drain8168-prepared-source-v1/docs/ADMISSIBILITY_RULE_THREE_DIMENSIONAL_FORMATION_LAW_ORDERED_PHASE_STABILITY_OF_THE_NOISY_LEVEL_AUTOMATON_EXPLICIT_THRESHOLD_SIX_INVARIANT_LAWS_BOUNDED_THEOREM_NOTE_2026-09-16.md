---
claim_id: admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_of_the_noisy_level_automaton_explicit_threshold_six_invariant_laws_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
bodyType: bounded_theorem
claim_scope: "For the three-dimensional monotone formation law of the covariant product rule on the six-axis menu with positive orbit weights (p, q, r) — records forming in level order, each drawn from the rule's conditional given its three recorded predecessors, read as the synchronous level automaton on Z^2 — and for the noisy majority automaton eta_x = maj(eta_{x-e_1}, eta_{x-e_2}, eta_{x-e_3}) or zeta_x with i.i.d. Bernoulli(epsilon) noise zeta and eta = 0 on levels <= 0: (T1-T4) every 1 at a site x admits an explanation tree — a subtree of the space-time graph of arrows (x, x - e_i) and forks (x, x + e_i - e_j), rooted at x, whose marked nodes are noise sites, with n marked nodes and at most 4(n - 1) edges — built by refining spanned clusters along the functionals M_k(z) = z_k - tau(z)/3 whose span rises by at least one per refinement and equals the fork count at the end; every node of the tree has at most one arrow to a predecessor, the marked nodes are exactly the nodes with none, the forks number n - 1 and the arrows at most 3(n - 1) (proved; executed on every noise configuration of the depth-2 backward cone, every depth-3 configuration with at most four noise sites, random deeper cones and structured seeds); (T5) such trees lift injectively to admissible rooted subtrees of the typed regular tree of the twelve edge types, whose weight sum with t per arrow and s per fork obeys a three-term recursion bounded by an exact rational super-solution: at (t, s) = (91/1000, 1000/107653) the sum is below 391/100 (proved; the counts of the 66103 trees with at most four edges executed against the recursion's coefficients; the certificate exact); (T6) hence P(eta_x = 1) <= (391/100) epsilon <= 3/10^5 uniformly in x for every epsilon <= epsilon_0 := 7/10^6 (proved; exact); (T7) with the domination of the coarse-graining 1{v_x != a} by eta at noise level epsilon(p, q, r) = max(1 - p^3/(p^3 + q^3 + 4 r^3), 1 - p^2 q/(p q (p + q) + 4 r^3), 1 - p^2 r/(r (p^2 + q^2) + r^2 (p + q) + 2 r^3)), strictly decreasing in p, the formation law started from the all-a level has P(v_x != a) <= 3/10^5 at every later site whenever epsilon(p, q, r) <= epsilon_0 — at (p, 1, 2) for every integer p >= 285718 — and its level automaton has at least six pairwise distinct translation-invariant invariant laws, one per value: an ordered phase (proved; the thresholds exact). The supplied stability obligation is proved at scope; the location of the true threshold is not claimed; no coupling, reading or rule is selected as physical; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_strong_coupling_formation_law_level_automaton_eroder_metastability_ordered_phase_obligation_bounded_theorem_note_2026-09-15
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_noisy_level_automaton_2026_09_16.py
---

# The three-dimensional formation law has an ordered phase: stability of the noisy level automaton re-proved with an explicit noise threshold, and at least six invariant laws at strong coupling

**Date:** 2026-09-16
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

The level-automaton source read the three-dimensional formation law level by level
and found a plain cellular automaton: each site takes the majority of its
three recorded predecessors, with a small probability of overruling that is
computed exactly and falls like one over the coupling. It proved the
noiseless majority erodes any finite island, and it reduced the question
"does the formation reading order at strong coupling?" to one obligation:
that a majority eroder with small one-sided noise, started from the all-zero
level, keeps the density of ones below one half forever. This note proves
that obligation for this automaton, with every constant explicit, and draws
the consequence: at strong enough coupling the formation law started from
each of the six constant planes stays, at every later site, within
`3/10⁵` of that value, and the level automaton has at least six distinct
invariant laws. The formation reading orders.

The proof is a contour argument in space-time. A one at a site `x` that is
not itself a noise site has two predecessors that are ones; following such
"excuses" backward gives a tree, but the naive tree has far too many nodes
per noise site. The repair, classical in outline, is to follow the excuses
along three charges — the functionals `M_k(z) = z_k − τ(z)/3`, which sum to
zero and each of which increases by exactly `1/3` along a suitable
predecessor of any one — and to connect the pieces at the same level by
"forks" between sibling sites. A potential, the span, rises by at least one
per refinement and equals the number of forks at the end; the forks form a
tree on the noise nodes; so the explanation has `n` noise nodes, `n − 1`
forks and at most `3(n − 1)` arrows, and the noise nodes are read off the
tree as the nodes with no arrow to a predecessor. The trees are counted by
lifting them to the regular tree of the twelve edge types, where the weight
sum with `t` per arrow and `s` per fork obeys a three-term recursion; an exact
rational super-solution bounds it, and the arrow budget turns the bound into
`P(one at x) ≤ (391/100)ε` for every `ε ≤ 7/10⁶`. The whole construction is
executed on every noise configuration of small backward cones, where the tree
property, the marks and the edge counts are checked case by case, and the tree
counts with at most four edges are checked against the recursion.

Exactly: the explanation tree (T1–T4), the count (T5), the bound (T6), the
domination and the six laws with `ε(p, q, r) ≤ 7/10⁶`, i.e. `p ≥ 285718`
at `(p, 1, 2)` (T7). The paired runner defines 22 checks and 13 mutations; the archive preserves historical evidence. Fresh corrected-source capture is pending.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "stability of the supplied noisy majority automaton"
source_of_blocker_text: source
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "six invariant formation laws at the explicit sufficient noise bound; true threshold and unconditional static order remain open"
conditional_surface_status: "T1-T6 proved for the noisy majority automaton for every epsilon <= 7/10^6; T7 proved for the formation law under the monotone order with corner (+,+,+) and the six-axis product rule with positive weights; the construction executed exhaustively on the depth-2 cone and on all depth-3 configurations with at most four noise sites, plus random and structured cases; conditional on the records-only reading, positivity, the six-axis menu and the monotone order as supplied conditions; mathematical compactness and decomposition imports explicitly stated"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The [axioms memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the four sentences quoted in the exact original recovery. The [finite-window product-rule source](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md) supplies only the six-axis menu, positive product weights and one-site conditional. The process below additionally supplies independent level updates, a constant initial plane and independent comparison noise; these are not selected by the axioms. The level-automaton correspondence is used only with spatial invariance as stated in Placement.

Declared objects.
- **The rule.** The six-axis menu `M = {±e_1, ±e_2, ±e_3}` with the product rule `φ(v, v') = p, q, r` for `v' = v`, `v' = −v`, `v' ⊥ v` (`p, q, r > 0`); the one-site conditional given a recorded set `A` of neighbours, `K(v | v_A) = Π_{y∈A} φ(v, v_y) / Σ_{v'} Π_{y∈A} φ(v', v_y)`.
- **Space-time and level time.** Sites `x ∈ Z³` with level `τ(x) = x_1 + x_2 + x_3`; predecessors `x − e_j`, successors `x + e_j` (`j = 1, 2, 3`); siblings `x ± (e_i − e_j)` (`i ≠ j`). Two predecessors of a site are siblings.
- **The formation law in level order.** Records form level by level; the record at `x` is drawn from `K(· | v_{x−e_1}, v_{x−e_2}, v_{x−e_3})`, independently across the sites of a level given the previous level; level `0` carries a supplied constant plane. The **level automaton** is the resulting Markov chain of level configurations (a synchronous probabilistic cellular automaton on `Z²` after the bijection `x ↦ (x_2, x_3)` of each level, with neighbourhood `{(0,0), (−1,0), (0,−1)}`). Its kernel `P` acts on `M^{Z²}`.
- **The coarse-graining and the noise map.** For a value `a`, `ξ_x = 1{v_x ≠ a}`; `ε(p, q, r) = max{1 − K(a | u, v, w) : at least two of u, v, w equal a}`.
- **The noisy majority automaton.** `η_x = maj(η_{x−e_1}, η_{x−e_2}, η_{x−e_3}) ∨ ζ_x` with `ζ_x` i.i.d. Bernoulli(`ε`) and `η ≡ 0` on levels `≤ 0`. A **1-site** is a site with `η_x = 1`; a **noise site** is a 1-site with `ζ_x = 1` and fewer than two 1-predecessors; a 1-site that is not a noise site has at least two 1-predecessors and its **winning pair** `W(x)` is the pair of 1-predecessors with the two smallest indices.
- **The graph `G`.** Vertices `Z³`; **arrows** `{x, x − e_j}`; **forks** `{x, x + e_i − e_j}`, `i ≠ j`. Every vertex meets `6` arrows and `6` forks: degree `12`.
- **The functionals.** `M_k(z) = z_k − τ(z)/3` for `k = 1, 2, 3`; `Σ_k M_k ≡ 0`; `M_k(x − e_j) − M_k(x) = 1/3 − δ_{jk}`; along a fork `x → x + e_i − e_j`, `M_i` rises by `1`, `M_j` falls by `1`, the third is unchanged.
- **Clusters.** At level `s`, the **arrow graph** has the 1-sites of levels `≤ s` as vertices and an edge between a non-noise 1-site and each of its 1-predecessors; a **cluster at level `s`** is the intersection with level `s` of a connected component. A noise site is a singleton cluster (it has no arrows to lower levels and its successors are above `s`).
- **Spanned sets.** `(P, v_1, v_2, v_3)` with `v_k ∈ P`; `Span = Σ_k M_k(v_k)`; `Size(P) = Σ_k max_P M_k`; `Span ≤ Size`. For a non-noise 1-site `v`, `Excuse_k(v)` is the element of `W(v)` with index `≠ k` (the smaller index if both qualify); `M_k(Excuse_k(v)) = M_k(v) + 1/3`.
- **Explanation trees.** Subtrees of `G` containing `x` with at most one arrow to a predecessor at each node; the **marked nodes** of such a tree are its nodes with no arrow to a predecessor, `n` their number, `a` and `f` its numbers of arrows and forks; `𝓔` the family with `f = n − 1` and `a ≤ 3(n − 1)`.
- **The typed tree `𝕋`.** The twelve edge types at a vertex of `G` — *down* `j` (to `x − e_j`), *up* `j` (to `x + e_j`), *fork* `(i, j)` (to `x + e_i − e_j`) — with the reversals *down* `j` ↔ *up* `j` and *fork* `(i, j)` ↔ *fork* `(j, i)`; `𝕋` has as vertices the finite words in the types in which no letter is followed by its reversal, the empty word as root, and the edges `{w, wτ}`. A subtree of `𝕋` containing the root is **admissible** if a vertex entered by an *up* letter has no *down* child and every other vertex, the root included, has at most one *down* child.

## Prior art and what is new

The stability of the majority eroder under small noise is Toom's theorem (1980); Berman and Simon (1988) gave a proof for this automaton, Gács (2021) a simplified exposition of it, and Swart, Szabó and Toninelli (2022) a general contour formulation with the explicit bound `3^{−21}`; Bramson and Gray (1991) gave a continuum route. None is used as authority: T1–T6 are re-proved here, following the structure of Gács's exposition (spanned clusters, excuses, the spanning lemma, refinement), in the level-time coordinates of `Z³` where the three charges are the three coordinate functionals. The result established here: (i) the supplied stability obligation proved at scope, with the constants of this automaton (`degree 12`, threshold `7/10⁶`, bound `3/10⁵`) and the explicit couplings; (ii) the construction executed exhaustively on small backward cones — the tree property, the marks, the spanning identity at every refinement and the edge bound checked case by case — which caught a definitional slip in the first draft (forks sharing a point were allowed to be adjacent, skipping the cluster between them); (iii) six stationary formation laws under the supplied process, independently of the unresolved unconditional static phase; (iv) the count of trees through the lift to the typed regular tree with an exact rational super-solution of its generating-function recursion, which raised the threshold of the first count (a depth-first word with a mark per node, `1/(2·96⁴)`) by a factor above a thousand.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T0 | the closed forms of the kernel; `ε` decreasing in `p`; the domination coupling | level-kernel identities re-proved | B |
| T1 | clusters; the cause graph of a cluster is connected | arrow paths through the past; siblings are forked | D (executed inside the construction) |
| T2 | the excuse lemma `Σ_k M_k(Excuse_k(v_k)) = Span + 1`; fork pairs have `Size = 1` | the increments `1/3 − δ_{jk}` | C |
| T3 | the spanning lemma | the charge partition at each point | D (asserted at every refinement) |
| T4 | the explanation tree: `n` noise nodes = the nodes without an arrow to a predecessor, `n − 1` forks, at most `3(n − 1)` arrows | refinement; span accounting; contraction | D |
| T5 | `Σ_T t^a s^f ≤ R̄ < 391/100` over `𝓔` at `(t, s) = (91/1000, 1000/107653)` | the lift to the typed tree; the recursion; an exact super-solution | D, E |
| T6 | `P(η_x = 1) ≤ (391/100)ε ≤ 3/10⁵` for `ε ≤ ε_0 = 7/10⁶` | the union bound over `𝓔`; the arrow budget | E |
| T7 | the six invariant laws; the coupling thresholds | domination; Cesàro limits; distinctness | B, E |

## Theorem T0 — the kernel, the noise map and the domination (re-proved)

**Statement.** (a) For a value `a`, `b ⊥ a`: `K(a | a,a,a) = p³/(p³ + q³ + 4r³)`, `K(a | a,a,b) = p²r/(r(p² + q²) + r²(p + q) + 2r³)`, `K(a | a,a,−a) = p²q/(pq(p + q) + 4r³)`; hence `ε(p, q, r)` is the maximum of the three deviations `d_1 = 1 − p³/(p³+q³+4r³)`, `d_2 = 1 − p²q/(pq(p+q)+4r³)`, `d_3 = 1 − p²r/(r(p²+q²) + r²(p+q) + 2r³)`. (b) Each deviation is strictly decreasing in `p > 0` for fixed `q, r > 0`, so `ε` is. (c) There is a coupling of the formation law started from the all-`a` level with the noisy majority automaton at noise `ε(p, q, r)` such that `ξ_x ≤ η_x` at every site; hence `P(v_x ≠ a) ≤ P(η_x = 1)`.

**Proof.** (a) `K(a | u,v,w) = Π φ(a, ·)/Σ_{v'} Π φ(v', ·)`; with the three factors `p, p, p` the normalizer is `p³ + q³ + 4r³` (the antipode contributes `q³`, the four orthogonal values `r³` each); with `p, p, r` (two `a`'s and `b ⊥ a`): the numerator `p²r`, the normalizer `r(p² + q²) + r²(p + q) + 2r³` (the values `a, −a, b, −b` and the two remaining); with `p, p, q`: numerator `p²q`, normalizer `pq(p+q) + 4r³`. The triples with at least two entries `a` are, up to the rule's symmetry, exactly these three. (b) `d_1' = −3p²(q³ + 4r³)/(p³ + q³ + 4r³)² < 0`; writing `d_2 = (pq² + 4r³)/(qp² + q²p + 4r³)`, its derivative has numerator `q²(qp² + q²p + 4r³) − (pq² + 4r³)(2qp + q²) = −q³p² − 8qr³p < 0`; writing `d_3 = (r²p + C)/(rp² + r²p + C)` with `C = rq² + r²q + 2r³`, the numerator of its derivative is `r²(rp² + r²p + C) − (r²p + C)(2rp + r²) = −r³p² − 2rCp < 0`. (c) Build both processes level by level, site by site, given the previous level with `ξ ≤ η`. At `x`: if at least two of `η`'s predecessors are `1`, set `η_x = 1 ≥ ξ_x`. Otherwise at most one of `η`'s predecessors is `1`, hence at most one of `ξ`'s, so at least two of `v`'s predecessors equal `a` and `P(ξ_x = 1 | past) = 1 − K(a | v_{x−e_1}, v_{x−e_2}, v_{x−e_3}) ≤ ε`; couple `ξ_x` monotonically with a Bernoulli(`ε`) variable `ζ_x`. The sites of a level are drawn independently given the previous level in both processes. ∎ (Executed: the closed forms symbolically; the derivatives; `ε` as the exact maximum over the 16 majority triples among 216 candidate triples for fixed `a`, and the coupling inequality at every such triple, at `(3, 1, 2)` and `(10, 1, 2)`: B1–B4.)

## Theorem T1 — clusters and the cause graph

**Statement.** Let `K` be a cluster at level `s ≥ 2` whose points are non-noise. Let `V_K` be the set of clusters at level `s − 1` containing a 1-predecessor of some point of `K`, and let two distinct clusters of `V_K` be adjacent if a fork joins a point of one to a point of the other. Then this graph (the **cause graph** of `K`) is connected, and every `Excuse_k(v)` with `v ∈ K` lies in a cluster of `V_K`.

**Proof.** Two points `a, b ∈ K` are joined by a path in the arrow graph through 1-sites of levels `≤ s`. Cut the path at its visits to level `s`: between consecutive visits it stays at levels `≤ s − 1`, so the two predecessors it descends to and ascends from are in the same cluster of level `s − 1`; at a visit `k ∈ K` it arrives from a 1-predecessor `r` and leaves to a 1-predecessor `r'`, and `r, r'` are siblings, hence joined by a fork (or equal). So the clusters met along the path form a connected chain in the cause graph; and any cluster of `V_K` contains a predecessor of some `k ∈ K`, which is a sibling of the predecessor the path uses at `k` (or equal), so it is adjacent to the chain. The last claim holds because `Excuse_k(v)` is a 1-predecessor of `v`. ∎

## Theorem T2 — the excuse lemma

**Statement.** (a) For a non-noise 1-site `v` and each `k`, `W(v)` contains an element with index `≠ k`, and `M_k(Excuse_k(v)) = M_k(v) + 1/3`. Hence for a spanned set `(P, v_1, v_2, v_3)` with non-noise poles, `Σ_k M_k(Excuse_k(v_k)) = Span + 1`. (b) A fork pair `{w, w'}` has `Size = 1`, so any spanned set with base `{w, w'}` has `Span ≤ 1`.

**Proof.** (a) The pair has two distinct indices, so one differs from `k`; for that element `x − e_j` with `j ≠ k`, `M_k(x − e_j) − M_k(x) = 1/3`. Sum over the three charges. (b) With `w' = w + e_i − e_j`: `max M_i = M_i(w) + 1`, `max M_j = M_j(w)`, `max M_l = M_l(w)` for the third index, and `Σ_k M_k(w) = 0`. ∎ (C1–C2.)

## Theorem T3 — the spanning lemma

**Statement.** Let `(L, u_1, u_2, u_3)` be a spanned set. Let `𝓒` be a family of pairwise disjoint subsets of `L` (**clusters**) and `𝓕` a family of two-point subsets of `L` (**forks**), each fork meeting two distinct clusters in one point each, such that the bipartite graph `B` (a cluster adjacent to the forks that meet it) is connected and each pole `u_k` lies in a cluster `C_k ∈ 𝓒`. Then there is a subtree `𝒯` of `B` containing `C_1, C_2, C_3` and minimal (every leaf of `𝒯` is one of the `C_k`; in particular every fork in `𝒯` has both its clusters in `𝒯`), and for each `X ∈ 𝒯` a point set `X' ⊂ X` and poles `u_{X,1}, u_{X,2}, u_{X,3} ∈ X'` such that
```
Σ_{X ∈ 𝒯} Σ_k M_k(u_{X,k}) = Σ_k M_k(u_k),
```
`X'` consists of `u_k` (when `X = C_k`) and the meeting points of `X` with its neighbours in `𝒯`, every point of `X'` is a pole of `X`, and `X' = X` for a fork.

**Proof.** *Construction.* Take a shortest path in `B` from `C_1` to `C_2`, then a shortest path from `C_3` to a vertex of that path, and delete non-terminal leaves until none remain: a minimal subtree `𝒯` (a fork in `𝒯` cannot be a leaf, so it keeps both its clusters). For adjacent `X, Y ∈ 𝒯` let `m(X, Y)` be their unique common point. Put `X' = {u_k : X = C_k} ∪ {m(X, Y) : Y ∼ X in 𝒯}`. For each `k`: if `u_k ∈ X'` put `u_{X,k} = u_k`; otherwise let `Y` be the neighbour of `X` on the path of `𝒯` from `X` to `C_k` and put `u_{X,k} = m(X, Y)`. *Every point of `X'` is a pole.* A meeting point `m(X, Y)`: removing `X` leaves a subtree through `Y` whose leaves are terminals, so some `C_k` lies beyond `Y`; then either `u_k ∉ X'` and `u_{X,k} = m(X, Y)`, or `u_k ∈ X'`, which forces `u_k = m(X, Y)` (a fork containing `u_k` meets `C_k` and `X`, so the path from `X` to `C_k` uses that fork). *The identity.* Let `V = ∪_X X'` and, for `v ∈ V`, `I(v) = {X ∈ 𝒯 : v ∈ X'}`: the unique cluster `C ∋ v` and the forks of `𝒯` containing `v`, each of which is adjacent to `C` in `𝒯` (a fork in `𝒯` has degree two). Fix `v` and a charge `k`. If `v = u_k`, then `u_{X,k} = v` for every `X ∈ I(v)`. If `v ≠ u_k`, let `Y_0` be the neighbour of `C` toward `C_k` (or `C = C_k`): the forks `f ∋ v` of `I(v)` other than `Y_0` have `u_{f,k} = m(f, C) = v`; and, when `v ∈ Y_0`, exactly one of `C` and `Y_0` has its pole at `v` (`C` iff `v ∈ Y_0`, in which case `Y_0`'s pole is its other point; if `C = C_k`, `C`'s pole is `u_k ≠ v` and all forks have theirs at `v`). When `v ∉ Y_0`, neither contributes at `v` and the other incident forks supply `|I(v)| − 1`. So `#{X ∈ I(v) : u_{X,k} = v} = |I(v)| − 1 + [v = u_k]`. Hence `Σ_X Span(X) = Σ_v Σ_k M_k(v)(|I(v)| − 1 + [v = u_k]) = Σ_v (|I(v)| − 1)·0 + Σ_k M_k(u_k)`. ∎ (Asserted at every refinement executed: D1–D3.)

## Theorem T4 — the explanation tree

**Statement.** Let `η_x = 1`. Then there is a subtree `T` of `G` containing `x`, all of whose nodes are 1-sites, such that every node has at most one arrow of `T` to a predecessor of it; the nodes with none — the marked nodes — are exactly the noise sites of `T`, `n ≥ 1` in number; and `T` has exactly `n − 1` forks and at most `3(n − 1)` arrows. In particular `T ∈ 𝓔`.

**Proof.** If `x` is a noise site, the one-node tree `{x}` (marked) has `n = 1` and no edges. Otherwise run the following **refinement** procedure. A *partial explanation tree* consists of a set `𝒰` of unprocessed spanned clusters (a cluster at some level with three poles in it), a set `𝒫` of processed points, and a set of edges (arrows and forks) between poles and processed points, such that the graph obtained by contracting each unprocessed cluster to a node is a tree; its span is `Σ_{𝒰} Span + #forks`. Start with `𝒰 = {({x}, x, x, x)}`, span `0`. While some unprocessed cluster `(K, v_1, v_2, v_3)` has a non-noise pole (then all its points are non-noise, since a cluster containing a noise site is a singleton): let `u_k = Excuse_k(v_k)`; take the cause graph of `K` (T1), choosing one fork for each adjacent pair of clusters; apply T3 to the spanned set `(∪V_K, u_1, u_2, u_3)` with the clusters of `V_K` and the chosen forks; add each cluster `X ∈ 𝒯` with poles `u_{X,·}` to `𝒰`; add each fork of `𝒯` as an edge; let the *kept poles* be the distinct points among `v_1, v_2, v_3` that are incident to an edge already present (if none, `v_1`); for each kept point `w` add the arrow `{w, u_{k(w)}}`, `k(w)` the least `k` with `v_k = w`, and move `w` to `𝒫`; delete `(K, v)` from `𝒰`.
*The tree property.* The node `K` is replaced by the tree `𝒯` (clusters as nodes, forks as edges) with the kept points attached to it by one arrow each, and every old edge incident to a pole of `K` is now incident to that kept point: a tree. No point appears twice: a cluster at level `s − 1` has all its level-`s` parents in one cluster (two parents in different level-`s` clusters would be joined through the child, contradicting distinctness), so a cluster is added at most once; forks are chosen once per pair of clusters; kept points are processed once; points at different levels differ.
*The span rises by at least one.* `Σ_{X ∈ 𝒯} Span(X) = Σ_k M_k(u_k) = Span(K) + 1` by T3 and T2(a); a fork's span is at most `1` by T2(b) while it counts `1` as a fork; so the new span exceeds the old by at least `1`. At most three arrows are added.
*Termination and the end state.* Each refinement replaces a cluster at level `s` by clusters at level `s − 1`; there are no 1-sites at levels `≤ 0`, and every 1-site at level `1` is a noise site; so the procedure ends, with every unprocessed cluster a singleton noise site, of span `0`.
*The count.* Let `n` be the number of noise nodes. Contract every arrow into its lower point: each processed point merges, along its own arrow and the arrows below, into a noise node; the result is a tree whose nodes are the `n` noise nodes and whose edges are the forks, so `#forks = n − 1`. The final span is `n − 1` and rose by at least one per refinement from `0`, so there were at most `n − 1` refinements and at most `3(n − 1)` arrows; the edges number at most `4(n − 1)`. All nodes are 1-sites.
*Arrows at a point.* Every arrow is `{w, u_{k(w)}}` with `w` a processed point and `u_{k(w)}` a predecessor of `w`; so the arrows of the tree at a point `v` are its own — to a predecessor, present iff `v` was processed — and those of processed points above `v` whose excuse is `v`, which join `v` to successors. Hence a node has at most one arrow to a predecessor. Every node is a processed point or a noise node: a fork endpoint or the lower end of an arrow is a pole incident to an edge, hence kept and processed when its cluster is refined, unless that cluster is a noise singleton. So the nodes without an arrow to a predecessor are exactly the noise nodes, which are noise sites. ∎

Executed (D1–D3): on every noise configuration of the depth-2 backward cone of `x` (`1024`), on every depth-3 configuration with at most four noise sites, on random cones of depth `3`–`7`, and on line and triangle seeds, the procedure never fails, the spanning identity holds at every refinement, the point graph is a tree of arrows and forks through 1-sites rooted at `x`, the marked nodes are noise sites, `edges ≤ 4(n − 1)` (the largest ratio observed is below `3`), every node has at most one arrow to a predecessor, the nodes without one are exactly the noise nodes, `forks = n − 1` and `arrows ≤ 3(n − 1)`.

## Theorem T5 — counting the trees

**Statement.** Let `t = 91/1000`, `s = 1000/107653`, and let `D̄ = 3290957526219/10¹²`, `Ū = 514547476033/(25·10¹⁰)`, `F̄ = 943741493637/(25·10¹⁰)`. These satisfy
```
D̄ ≥ (1 + tŪ)²(1 + 3tD̄)(1 + sF̄)⁶,   Ū ≥ (1 + tŪ)³(1 + sF̄)⁶,   F̄ ≥ (1 + tŪ)³(1 + 3tD̄)(1 + sF̄)⁵,
```
and with `R̄ := (1 + tŪ)³(1 + 3tD̄)(1 + sF̄)⁶ < 391/100`,
```
Σ_{T ∈ 𝓔} t^{a(T)} s^{f(T)} ≤ Σ_T t^{a(T)} s^{f(T)} ≤ R̄,
```
the middle sum over all subtrees of `G` containing `x` with at most one arrow to a predecessor at each node.

**Proof.** *The lift.* For such a subtree `T` and a node `v`, let `w(v)` be the word of the types of the edges along the path of `T` from `x` to `v`, each read at the end it leaves (an edge of `G` has one type at each end, reversed at the other; a simple path never follows a letter by its reversal, which would return to the previous node). The set `L(T) = {w(v) : v ∈ T}` is a subtree of `𝕋` containing the root, with one *down* or *up* letter per arrow and one *fork* letter per fork; the projection `π(τ_1…τ_m) = x + (the sum of the displacements of the τ_i)` maps `L(T)` onto the nodes of `T` and its edges onto the edges of `T`, so `T ↦ L(T)` is injective. `L(T)` is admissible: at `w(v)` the arrows of `T` to predecessors of `v` are its *down* children and, when `v` was entered by an *up* letter, its parent. *The recursion.* For `h ≥ 0` let `D_h, U_h, F_h` be the sums of `t^a s^f` over the admissible subtrees of height at most `h` hanging from a vertex entered by a *down*, *up*, *fork* letter — the vertex together with subtrees hanging from some of its free slots, which are `2` *up*, `3` *down* of which at most one may be used, and `6` *fork* slots after a *down* letter; `3` *up* and `6` *fork* after an *up* letter; `3` *up*, `3` *down* of which at most one, and `5` *fork* after a *fork* letter — and let `R_h = (1 + tU_h)³(1 + 3tD_h)(1 + sF_h)⁶`, the sum over the admissible subtrees of `𝕋` of height at most `h + 1`. Then `D_0 = U_0 = F_0 = 1` and
```
D_{h+1} = (1 + tU_h)²(1 + 3tD_h)(1 + sF_h)⁶,   U_{h+1} = (1 + tU_h)³(1 + sF_h)⁶,   F_{h+1} = (1 + tU_h)³(1 + 3tD_h)(1 + sF_h)⁵,
```
since a slot is empty or carries a subtree of height at most `h`, the slots are filled independently, and the three *down* slots carry at most one subtree in all. *The bound.* The right sides are increasing in each argument (positive coefficients) and `D̄, Ū, F̄ ≥ 1`, so by induction `D_h ≤ D̄`, `U_h ≤ Ū`, `F_h ≤ F̄` for every `h`, hence `R_h ≤ R̄`. Every admissible subtree has finite height, so the sum over all of them is the limit of the increasing `R_h`, at most `R̄`; the sum over the lifts of the trees of `G` is smaller still, and the sum over `𝓔` smaller again. The three inequalities and `R̄ < 391/100` are rational arithmetic (E1). ∎ (Executed: the subtrees of `G` containing the origin with at most four edges and at most one arrow to a predecessor per node number `66103`; their lifts are pairwise distinct; counted by `(a, f)`, each count is at most the coefficient of `t^a s^f` in the recursion's series, computed exactly — equal for at most two edges, below it for every pair with four edges — and the coefficients for at most three edges agree with a direct enumeration of the admissible subtrees of `𝕋`: D4.)

## Theorem T6 — the bound

**Statement.** For every site `x` (at any level) and every `ε ≤ ε_0 := 7/10⁶`,
```
P(η_x = 1) ≤ ε·R̄ ≤ (391/100)·ε ≤ 2737/10⁸ < 3/10⁵.
```

**Proof.** By T4, `{η_x = 1} ⊂ ∪_{T ∈ 𝓔} {ζ = 1 on the marked nodes of T}`; the marked nodes of a tree are distinct sites and the `ζ` are independent Bernoulli(`ε`), so `P(η_x = 1) ≤ Σ_{T ∈ 𝓔} ε^{n(T)}`. For `T ∈ 𝓔`, `n = f + 1` and `a ≤ 3f`; with `t = 91/1000 ≤ 1`, `ε^n = ε·ε^f ≤ ε·t^{a − 3f}·ε^f = ε·t^a (ε/t³)^f ≤ ε·t^a s^f`, because `ε/t³ ≤ ε_0/t³ = s` (`t³ s = (753571/10⁹)(1000/107653) = 7/10⁶`, as `753571 = 7·107653`). Sum over `𝓔` and apply T5. ∎ (E1.)

The middle bound is strict when ε>0; at ε=0 the probability bound is zero.

## Theorem T7 — the ordered phase of the formation law

**Statement.** Let `ε(p, q, r) ≤ ε_0 = 7/10⁶`. (a) From the all-`a` level, `P(v_x ≠ a) ≤ 3/10⁵` at every site `x` of every later level. (b) At `(p, 1, 2)` this holds for every integer `p ≥ 285718` and fails the condition `ε ≤ ε_0` at `p = 285717`; at `(p, 1, 1)`, `(p, 2, 4)`, `(p, 1, 3)` the least such integers are `142861`, `571436`, `428576`. (c) The level automaton has at least six translation-invariant invariant laws `μ_a`, one per value, with `μ_a(v_y ≠ a) ≤ 3/10⁵` at every site `y`; they are pairwise distinct; under the extremal decomposition (named under Imports) there are at least six extremal invariant laws.

**Proof.** (a) T0(c) and T6. (b) T0(b) makes `ε` strictly decreasing in `p`; the runner evaluates `ε` exactly at the stated integers and their predecessors. (c) The kernel `P` of the level automaton is Feller on the compact space `M^{Z²}` (the law of a level's cylinder depends continuously on finitely many coordinates of the previous level, all laws being finite products) and commutes with the translations of `Z²`. Let `λ_t` be the law of level `t` from the all-`a` level and `λ^{(T)} = T^{−1}Σ_{t=1}^T λ_t`. By compactness a subsequence of `λ^{(T)}` has a weak limit `μ_a`; for continuous `f`, `|λ^{(T)}(Pf) − λ^{(T)}(f)| = T^{−1}|λ_{T+1}(f) − λ_1(f)| ≤ 2‖f‖/T`, and `Pf` is continuous, so `μ_a(Pf) = μ_a(f)`: `μ_a` is invariant; it is translation-invariant because every `λ_t` is. The function `1{v_y ≠ a}` is continuous and `λ_t(v_y ≠ a) ≤ 3/10⁵` for every `t` by (a), so `μ_a(v_y ≠ a) ≤ 3/10⁵`. For `b ≠ a`, `μ_a(v_y = a) ≥ 1 − 3/10⁵ > 3/10⁵ ≥ μ_b(v_y = a)`, so the six laws are distinct. If there were at most five extremal invariant laws, each `μ_a` would be a mixture of them and some extremal law would give `{v_y = a}` probability at least `1 − 3/10⁵ > 1/2`; two different values cannot both exceed `1/2`, so the map from values to such extremal laws is injective, a contradiction. ∎ (E2–E3.)

*Placement.* The [level-automaton source](ADMISSIBILITY_RULE_STRONG_COUPLING_FORMATION_LAW_LEVEL_AUTOMATON_ERODER_METASTABILITY_ORDERED_PHASE_OBLIGATION_BOUNDED_THEOREM_NOTE_2026-09-15.md) S0 identifies spatially invariant stationary level laws with fully translation-invariant formation laws. The six laws constructed here have both invariances. Only this correspondence and the stated stability target are used; its deferred classifications are not imported. The current static result, `ADMISSIBILITY_RULE_STATIC_SIX_AXIS_REFLECTION_IDENTITIES_AND_CONDITIONAL_CONTOUR_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md`, is conditional because site-reflection parity leaves a dissemination gap. Formation stability here does not depend on static order. The true threshold and intermediate coupling region remain open.

## No-Go Discipline Gate

### N1 — Positive theorem, negative certification deferred
T0–T7 provide a positive theorem for the supplied process. The historical list checked parts of one contour construction; it is not five distinct alternative negative-proof families. No broad negative certificate or route-exhaustion conclusion is asserted.

### N2 — Historical controls
The exact archive retains the original control sources and outputs, including failed proposals. Historical author checks do not become independent wall proofs.

### N3 — Supplied process and imports
Positive weights, six-axis menu, constant initial plane, conditionally independent product updates and independent comparison noise are supplied. Compactness and extremal decomposition are mathematical imports with hypotheses stated under Imports.

### N4 — Parent boundary
Only the actual rule, axiom sentences and spatially invariant stationary-law correspondence are imported. The current static reflection result is conditional; no unconditional static phase is used.

### N5 — Resolution
per_element: finite kernel forms, derivatives, charge increments and fork sizes.
per_site: 216 candidate triples enumerated, 16 majority triples for fixed a tested for the deviation bound; four coupling thresholds.
per_mode: finite exhaustive backward cones, 1200 seeded random cones, structured seeds and 66103 finite trees; exact domains unchanged.
per_block: rational super-solution, bound at epsilon_0 and finite-chain Cesaro identity.
lattice_wide: checked and not executed; T4–T7 are written proofs, not a numerical infinite-lattice execution.

### N6 — Primitive boundary
No primitive selects the process, coupling or initial plane.

### N7 — Unknown threshold and improvements
Finite periodic simulations over finite times and floating fixed-point searches on a finite t-grid with a stopping cutoff are exploratory observations. They do not locate the infinite-system threshold or prove optimality of the count or arrow budget. No new simulation is used here.

### N8 — Preserved failures and open scope
The noiseless eroder and current static dissemination gap remain intact. The full original history and unresolved negative/optimization claims remain recoverable; no missing attack route is invented.

## Falsifiers
- A kernel closed form that differs from the supplied product conditional, a deviation with a non-negative derivative in `p`, a triple with two entries `a` whose deviation exceeds `ε`, or a coupling inequality failing at some triple (B1–B4).
- An increment other than `1/3 − δ_{jk}`, a fork pair of size other than `1`, or a pole assignment of a fork with span above `1` (C1–C2).
- A noise configuration of the tested cones on which the refinement fails, the spanning identity fails, the point graph is not a tree of arrows and forks through 1-sites rooted at `x`, a marked node is not a noise site, `edges > 4(n − 1)`, a node with two arrows to predecessors, a marked set differing from the noise nodes, `forks ≠ n − 1` or `arrows > 3(n − 1)` (D1–D3); a tree count above the recursion's coefficient, two trees with the same lift, or a coefficient disagreeing with the direct enumeration (D4).
- A failure of one of the three super-solution inequalities, `R̄ ≥ 391/100`, `t³s ≠ 7/10⁶`, `ε_0 R̄ > 3/10⁵`, a `p_0` differing from the stated integers, or a failure of the Cesàro identity on the test chain (E1–E3).

## Boundaries and non-claims
This note proves, for the noisy majority automaton of the three-dimensional formation law in level time, that the density of ones from the all-zero level is at most `(391/100)ε` for `ε ≤ 7/10⁶`, and hence that the formation law of the six-axis product rule started from a constant plane keeps every later site within `3/10⁵` of that value whenever `ε(p, q, r) ≤ 7/10⁶`, with at least six distinct invariant laws; it does not locate the true threshold, does not treat couplings between a weak-coupling uniqueness region and this sufficient region, does not treat other menus or orders, does not select a reading, rule or coupling as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. Mathematical compactness and extremal decomposition are explicit theorem imports; no physical selection follows from them.

## Imports

- The linked axiom memo and product-rule source supply the stated sentences, menu and conditional; positivity, synchronous conditionally independent updates, initial plane and comparison-noise law are explicit supplied conditions.
- T0–T6 are proved in full here: kernel algebra, coupling, explanation-tree construction, charge accounting, typed-tree lift, rational super-solution and union bound.
- Weak compactness of probability laws on the compact metrizable finite-alphabet configuration space M^{Z²}, together with the Feller property of this finite-range product kernel, supplies the subsequential Cesaro limit in T7. Translation commutation and invariant initial laws preserve spatial invariance.
- For the optional extremal-count conclusion, import barycentric decomposition of stationary probability laws for a Feller Markov kernel on this compact metrizable space into extreme stationary laws. The stationary-law set is nonempty, compact and convex; cylinder marginals are continuous affine functions. The six directly constructed invariant laws and their separation do not require this optional decomposition conclusion.
- Historical attribution only: Toom, Berman–Simon, Gács, Swart–Szabó–Toninelli and Bramson–Gray. No numerical threshold is imported from them; no exhaustive novelty claim is made.

## Review record

The [exact original recovery](work_history/review_loop/pr8168/README.md) preserves all author/campaign records, full proofs and historical controls. The first cause graph allowed fork–fork adjacency and failed the edge bound; its corrected bipartite construction is retained. The outward-arrow proposal failed on 538 of the earlier 4308 explained trees and on 32 of an independent historical 3253-tree recount. The earlier sample's maximum a/f of 12/7 is a sample observation only. Later HANDOFF and OPPORTUNITY_QUEUE report 743 larger random trees, including a depth-12 a/f=7/3 example against the proposed a<=2f budget. The submitted files contain no seed/configuration or saved output for this later report; it is historical and unverified in this review, not a reconstructed witness or universal bound. All these failures concern particular constructions or candidate lemmas, not every improved contour method.

The original first depth-first count and its valid threshold 1/169869312 remain in the archive. The exact rational super-solution here is retained unchanged. The historical finite-grid floating search near 7.4 times 10^-6 and finite periodic simulations are exploratory only; neither establishes a true threshold nor excludes improving the count.

## Verification

```bash
python3 scripts/admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_noisy_level_automaton_2026_09_16.py
python3 scripts/admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_noisy_level_automaton_2026_09_16.py --list-mutations
python3 scripts/admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_noisy_level_automaton_2026_09_16.py --mutation edge_bound_claimed_tighter
```

Families: A authority and inputs; B the kernel, the noise map, the domination; C the increments and the fork size; D the explanation tree executed and the tree counts against the recursion; E the super-solution certificate and the bound, the thresholds, the Cesàro identity; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 13 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=22 FAIL=0`.
