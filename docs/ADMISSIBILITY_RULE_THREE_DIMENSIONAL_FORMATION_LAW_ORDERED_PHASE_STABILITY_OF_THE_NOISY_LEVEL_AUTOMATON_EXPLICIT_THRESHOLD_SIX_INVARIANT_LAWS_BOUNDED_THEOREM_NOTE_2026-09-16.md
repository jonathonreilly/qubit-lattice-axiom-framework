---
claim_id: admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_of_the_noisy_level_automaton_explicit_threshold_six_invariant_laws_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "For the three-dimensional monotone formation law of the covariant product rule on the six-axis menu with positive orbit weights (p, q, r) — records forming in level order, each drawn from the rule's conditional given its three recorded predecessors, read as the synchronous level automaton on Z^2 — and for the noisy majority automaton eta_x = maj(eta_{x-e_1}, eta_{x-e_2}, eta_{x-e_3}) or zeta_x with i.i.d. Bernoulli(epsilon) noise zeta and eta = 0 on levels <= 0: (T1-T4) every 1 at a site x admits an explanation tree — a subtree of the space-time graph of arrows (x, x - e_i) and forks (x, x + e_i - e_j), rooted at x, whose marked nodes are noise sites, with n marked nodes and at most 4(n - 1) edges — built by refining spanned clusters along the functionals M_k(z) = z_k - tau(z)/3 whose span rises by at least one per refinement and equals the fork count at the end (proved; executed on every noise configuration of the depth-2 backward cone, every depth-3 configuration with at most four noise sites, random deeper cones and structured seeds); (T5) rooted marked subtrees with k edges of the degree-12 graph number at most 2^{k+1} 48^k (proved; executed for k <= 3); (T6) hence P(eta_x = 1) <= (192/95) epsilon/(1 - 96^4 epsilon) uniformly in x, and for epsilon <= epsilon_0 := 1/(2 96^4) the bound is at most 1/42024960 (proved; exact); (T7) with the domination of the coarse-graining 1{v_x != a} by eta at noise level epsilon(p, q, r) = max(1 - p^3/(p^3 + q^3 + 4 r^3), 1 - p^2 q/(p q (p + q) + 4 r^3), 1 - p^2 r/(r (p^2 + q^2) + r^2 (p + q) + 2 r^3)), strictly decreasing in p, the formation law started from the all-a level has P(v_x != a) <= 1/42024960 at every later site whenever epsilon(p, q, r) <= epsilon_0 — at (p, 1, 2) for every integer p >= 339738628 — and its level automaton has at least six pairwise distinct translation-invariant invariant laws, one per value: an ordered phase (proved; the thresholds exact). The block-12 obligation S6 is closed at scope; the location of the true threshold is not claimed; no coupling, reading or rule is selected as physical; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_noisy_level_automaton_2026_09_16.py
---

# The three-dimensional formation law has an ordered phase: stability of the noisy level automaton re-proved with an explicit noise threshold, and at least six invariant laws at strong coupling

**Date:** 2026-09-16
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

Block 12 (PR #8146) read the three-dimensional formation law level by level
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
`1/42024960` of that value, and the level automaton has at least six distinct
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
tree on the noise nodes; so the explanation has `n` noise nodes and at most
`4(n − 1)` edges. The number of such trees is at most `2^{k+1}48^k` for `k`
edges, and the resulting series gives `P(one at x) ≤ (192/95)ε/(1 − 96⁴ε)`.
The whole construction is executed on every noise configuration of small
backward cones, where the tree property, the marks and the edge bound are
checked case by case.

Exactly: the explanation tree (T1–T4), the count (T5), the bound (T6), the
domination and the six laws with `ε(p, q, r) ≤ 1/(2·96⁴)`, i.e. `p ≥ 339738628`
at `(p, 1, 2)` (T7). Executed with exact arithmetic: 22 checks, 13 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "block 12's obligation S6 (PR #8146): the stability of the noisy majority eroder in level time, the last open row of the derivation campaign's record-dynamics seam; whether the formation reading has an ordered phase in three dimensions"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "S6 is closed at scope: for epsilon(p, q, r) <= 1/(2 96^4) the formation law's level automaton has at least six invariant laws, one per value, and the density of dissent from a constant plane stays below 1/42024960 forever. Open: the location of the true threshold (the constant is the crude one of the route); the formation law's phase between block 08's uniqueness region and this one. Consumers: #8093's assembly (record dynamics: both readings order at strong coupling on Z^3); the campaign's decision record"
conditional_surface_status: "T1-T6 proved for the noisy majority automaton at every epsilon with 96^4 epsilon < 1 and the bound stated for epsilon <= 1/(2 96^4); T7 proved for the formation law under the monotone order with corner (+,+,+) and the six-axis product rule with positive weights; the construction executed exhaustively on the depth-2 cone and on all depth-3 configurations with at most four noise sites, plus random and structured cases; conditional on the records-only reading, positivity, the six-axis menu and the monotone order as supplied conditions; three standard mathematical imports named at definition level"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", "Records form.", and "Only records are readable.". Block 01 (`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`, on `main`) supplies the rule and its one-site conditional given a recorded set; the monotone formation order and its level reading are declared below (blocks 05, 08 and 12, open PRs #8003, #8138, #8146, are referenced as evidence addresses only). All proposed and unaudited.

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
- **Explanation trees.** Marked subtrees of `G` (a subtree rooted at `x` with a `0/1` mark on each node); `𝓔` the family with `n` marked nodes and at most `4(n − 1)` edges.

## Prior art and what is new

The stability of the majority eroder under small noise is Toom's theorem (1980); Berman and Simon (1988) gave a proof for this automaton, Gács (2021) a simplified exposition of it, and Swart, Szabó and Toninelli (2022) a general contour formulation with the explicit bound `3^{−21}`; Bramson and Gray (1991) gave a continuum route. None is used as authority: T1–T6 are re-proved here, following the structure of Gács's exposition (spanned clusters, excuses, the spanning lemma, refinement), in the level-time coordinates of `Z³` where the three charges are the three coordinate functionals. What is new here: (i) the obligation S6 of block 12 closed at scope, with the constants of this automaton (`degree 12`, threshold `1/(2·96⁴)`, bound `1/42024960`) and the explicit couplings; (ii) the construction executed exhaustively on small backward cones — the tree property, the marks, the spanning identity at every refinement and the edge bound checked case by case — which caught a definitional slip in the first draft (forks sharing a point were allowed to be adjacent, skipping the cluster between them); (iii) the consequence for the campaign: both readings of the Admissibility rule, static (block 17) and formation (this note), order at strong coupling on `Z³`.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T0 | the closed forms of the kernel; `ε` decreasing in `p`; the domination coupling | block 12's S1, S3 re-proved | B |
| T1 | clusters; the cause graph of a cluster is connected | arrow paths through the past; siblings are forked | D (executed inside the construction) |
| T2 | the excuse lemma `Σ_k M_k(Excuse_k(v_k)) = Span + 1`; fork pairs have `Size = 1` | the increments `1/3 − δ_{jk}` | C |
| T3 | the spanning lemma | the charge partition at each point | D (asserted at every refinement) |
| T4 | the explanation tree: `n` noise nodes, at most `4(n − 1)` edges | refinement; span accounting; contraction | D |
| T5 | marked subtrees with `k` edges: at most `2^{k+1}48^k` | a depth-first encoding | D |
| T6 | `P(η_x = 1) ≤ (192/95)ε/(1 − 96⁴ε)`; `≤ 1/42024960` at `ε_0` | the union bound over `𝓔` | E |
| T7 | the six invariant laws; the coupling thresholds | domination; Cesàro limits; distinctness | B, E |

## Theorem T0 — the kernel, the noise map and the domination (from block 12, re-proved)

**Statement.** (a) For a value `a`, `b ⊥ a`: `K(a | a,a,a) = p³/(p³ + q³ + 4r³)`, `K(a | a,a,b) = p²r/(r(p² + q²) + r²(p + q) + 2r³)`, `K(a | a,a,−a) = p²q/(pq(p + q) + 4r³)`; hence `ε(p, q, r)` is the maximum of the three deviations `d_1 = 1 − p³/(p³+q³+4r³)`, `d_2 = 1 − p²q/(pq(p+q)+4r³)`, `d_3 = 1 − p²r/(r(p²+q²) + r²(p+q) + 2r³)`. (b) Each deviation is strictly decreasing in `p > 0` for fixed `q, r > 0`, so `ε` is. (c) There is a coupling of the formation law started from the all-`a` level with the noisy majority automaton at noise `ε(p, q, r)` such that `ξ_x ≤ η_x` at every site; hence `P(v_x ≠ a) ≤ P(η_x = 1)`.

**Proof.** (a) `K(a | u,v,w) = Π φ(a, ·)/Σ_{v'} Π φ(v', ·)`; with the three factors `p, p, p` the normalizer is `p³ + q³ + 4r³` (the antipode contributes `q³`, the four orthogonal values `r³` each); with `p, p, r` (two `a`'s and `b ⊥ a`): the numerator `p²r`, the normalizer `r(p² + q²) + r²(p + q) + 2r³` (the values `a, −a, b, −b` and the two remaining); with `p, p, q`: numerator `p²q`, normalizer `pq(p+q) + 4r³`. The triples with at least two entries `a` are, up to the rule's symmetry, exactly these three. (b) `d_1' = −3p²(q³ + 4r³)/(p³ + q³ + 4r³)² < 0`; writing `d_2 = (pq² + 4r³)/(qp² + q²p + 4r³)`, its derivative has numerator `q²(qp² + q²p + 4r³) − (pq² + 4r³)(2qp + q²) = −q³p² − 8qr³p < 0`; writing `d_3 = (r²p + C)/(rp² + r²p + C)` with `C = rq² + r²q + 2r³`, the numerator of its derivative is `r²(rp² + r²p + C) − (r²p + C)(2rp + r²) = −r³p² − 2rCp < 0`. (c) Build both processes level by level, site by site, given the previous level with `ξ ≤ η`. At `x`: if at least two of `η`'s predecessors are `1`, set `η_x = 1 ≥ ξ_x`. Otherwise at most one of `η`'s predecessors is `1`, hence at most one of `ξ`'s, so at least two of `v`'s predecessors equal `a` and `P(ξ_x = 1 | past) = 1 − K(a | v_{x−e_1}, v_{x−e_2}, v_{x−e_3}) ≤ ε`; couple `ξ_x` monotonically with a Bernoulli(`ε`) variable `ζ_x`. The sites of a level are drawn independently given the previous level in both processes. ∎ (Executed: the closed forms symbolically; the derivatives; `ε` as the exact maximum over all `216` triples with at least two entries `a`, and the coupling inequality at every such triple, at `(3, 1, 2)` and `(10, 1, 2)`: B1–B4.)

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

**Proof.** *Construction.* Take a shortest path in `B` from `C_1` to `C_2`, then a shortest path from `C_3` to a vertex of that path, and delete non-terminal leaves until none remain: a minimal subtree `𝒯` (a fork in `𝒯` cannot be a leaf, so it keeps both its clusters). For adjacent `X, Y ∈ 𝒯` let `m(X, Y)` be their unique common point. Put `X' = {u_k : X = C_k} ∪ {m(X, Y) : Y ∼ X in 𝒯}`. For each `k`: if `u_k ∈ X'` put `u_{X,k} = u_k`; otherwise let `Y` be the neighbour of `X` on the path of `𝒯` from `X` to `C_k` and put `u_{X,k} = m(X, Y)`. *Every point of `X'` is a pole.* A meeting point `m(X, Y)`: removing `X` leaves a subtree through `Y` whose leaves are terminals, so some `C_k` lies beyond `Y`; then either `u_k ∉ X'` and `u_{X,k} = m(X, Y)`, or `u_k ∈ X'`, which forces `u_k = m(X, Y)` (a fork containing `u_k` meets `C_k` and `X`, so the path from `X` to `C_k` uses that fork). *The identity.* Let `V = ∪_X X'` and, for `v ∈ V`, `I(v) = {X ∈ 𝒯 : v ∈ X'}`: the unique cluster `C ∋ v` and the forks of `𝒯` containing `v`, each of which is adjacent to `C` in `𝒯` (a fork in `𝒯` has degree two). Fix `v` and a charge `k`. If `v = u_k`, then `u_{X,k} = v` for every `X ∈ I(v)`. If `v ≠ u_k`, let `Y_0` be the neighbour of `C` toward `C_k` (or `C = C_k`): the forks `f ∋ v` of `I(v)` other than `Y_0` have `u_{f,k} = m(f, C) = v`; and exactly one of `C` and `Y_0` has its pole at `v` (`C` iff `v ∈ Y_0`, in which case `Y_0`'s pole is its other point; if `C = C_k`, `C`'s pole is `u_k ≠ v` and all forks have theirs at `v`). So `#{X ∈ I(v) : u_{X,k} = v} = |I(v)| − 1 + [v = u_k]`. Hence `Σ_X Span(X) = Σ_v Σ_k M_k(v)(|I(v)| − 1 + [v = u_k]) = Σ_v (|I(v)| − 1)·0 + Σ_k M_k(u_k)`. ∎ (Asserted at every refinement executed: D1–D3.)

## Theorem T4 — the explanation tree

**Statement.** Let `η_x = 1`. Then there is a marked subtree of `G` rooted at `x`, all of whose nodes are 1-sites, whose marked nodes are exactly its noise sites, with `n ≥ 1` marked nodes and at most `4(n − 1)` edges.

**Proof.** If `x` is a noise site, the one-node tree `{x}` (marked) has `n = 1` and no edges. Otherwise run the following **refinement** procedure. A *partial explanation tree* consists of a set `𝒰` of unprocessed spanned clusters (a cluster at some level with three poles in it), a set `𝒫` of processed points, and a set of edges (arrows and forks) between poles and processed points, such that the graph obtained by contracting each unprocessed cluster to a node is a tree; its span is `Σ_{𝒰} Span + #forks`. Start with `𝒰 = {({x}, x, x, x)}`, span `0`. While some unprocessed cluster `(K, v_1, v_2, v_3)` has a non-noise pole (then all its points are non-noise, since a cluster containing a noise site is a singleton): let `u_k = Excuse_k(v_k)`; take the cause graph of `K` (T1), choosing one fork for each adjacent pair of clusters; apply T3 to the spanned set `(∪V_K, u_1, u_2, u_3)` with the clusters of `V_K` and the chosen forks; add each cluster `X ∈ 𝒯` with poles `u_{X,·}` to `𝒰`; add each fork of `𝒯` as an edge; let the *kept poles* be the distinct points among `v_1, v_2, v_3` that are incident to an edge already present (if none, `v_1`); for each kept point `w` add the arrow `{w, u_{k(w)}}`, `k(w)` the least `k` with `v_k = w`, and move `w` to `𝒫`; delete `(K, v)` from `𝒰`.
*The tree property.* The node `K` is replaced by the tree `𝒯` (clusters as nodes, forks as edges) with the kept points attached to it by one arrow each, and every old edge incident to a pole of `K` is now incident to that kept point: a tree. No point appears twice: a cluster at level `s − 1` has all its level-`s` parents in one cluster (two parents in different level-`s` clusters would be joined through the child, contradicting distinctness), so a cluster is added at most once; forks are chosen once per pair of clusters; kept points are processed once; points at different levels differ.
*The span rises by at least one.* `Σ_{X ∈ 𝒯} Span(X) = Σ_k M_k(u_k) = Span(K) + 1` by T3 and T2(a); a fork's span is at most `1` by T2(b) while it counts `1` as a fork; so the new span exceeds the old by at least `1`. At most three arrows are added.
*Termination and the end state.* Each refinement replaces a cluster at level `s` by clusters at level `s − 1`; there are no 1-sites at levels `≤ 0`, and every 1-site at level `1` is a noise site; so the procedure ends, with every unprocessed cluster a singleton noise site, of span `0`.
*The count.* Let `n` be the number of noise nodes. Contract every arrow into its lower point: each processed point merges, along its own arrow and the arrows below, into a noise node; the result is a tree whose nodes are the `n` noise nodes and whose edges are the forks, so `#forks = n − 1`. The final span is `n − 1` and rose by at least one per refinement from `0`, so there were at most `n − 1` refinements and at most `3(n − 1)` arrows; the edges number at most `4(n − 1)`. The marked nodes are the noise nodes, which are noise sites; all nodes are 1-sites. ∎

Executed (D1–D3): on every noise configuration of the depth-2 backward cone of `x` (`1024`), on every depth-3 configuration with at most four noise sites, on random cones of depth `3`–`7`, and on line and triangle seeds, the procedure never fails, the spanning identity holds at every refinement, the point graph is a tree of arrows and forks through 1-sites rooted at `x`, the marked nodes are noise sites, and `edges ≤ 4(n − 1)` (the largest ratio observed is below `3`).

## Theorem T5 — counting marked trees

**Statement.** The number of marked subtrees of `G` with `k` edges containing a given vertex is at most `2^{k+1}(4·12)^k = 2·96^k`.

**Proof.** Traverse the tree depth-first from the given vertex: a word of length `2k` in the letters *down* and *up* (at most `2^{2k}` words), and at each *down* step a choice among at most `12` incident edges (at most `12^k`); the tree is recovered from the word and the choices. The `k + 1` marks give a factor `2^{k+1}`. ∎ (Executed: the exact numbers of subtrees with `k = 1, 2, 3` edges containing the origin are `12, 198, 3688`, below `48^k`: D4.)

## Theorem T6 — the bound

**Statement.** For every site `x` (at any level) and every `ε` with `96⁴ε < 1`,
```
P(η_x = 1) ≤ Σ_{n≥1} ε^n Σ_{k=0}^{4(n−1)} 2·96^k ≤ (192/95) · ε/(1 − 96⁴ε);
```
for `ε ≤ ε_0 := 1/(2·96⁴) = 1/169869312`, `P(η_x = 1) ≤ (384/95)ε ≤ 1/42024960`.

**Proof.** By T4, `{η_x = 1} ⊂ ∪_{T ∈ 𝓔} {ζ = 1 on the marked nodes of T}`; the marked nodes of a tree are distinct sites and the `ζ` are independent Bernoulli(`ε`), so each event has probability `ε^{n(T)}`. Group the trees by `n` and by the number `k ≤ 4(n − 1)` of edges and use T5: `Σ_{k≤K} 2·96^k = 2(96^{K+1} − 1)/95 ≤ (192/95)96^K`. Summing the geometric series in `n` with ratio `96⁴ε` gives the closed form; at `ε ≤ ε_0` the denominator is at least `1/2`. ∎ (E1.)

## Theorem T7 — the ordered phase of the formation law

**Statement.** Let `ε(p, q, r) ≤ ε_0`. (a) From the all-`a` level, `P(v_x ≠ a) ≤ 1/42024960` at every site `x` of every later level. (b) At `(p, 1, 2)` this holds for every integer `p ≥ 339738628` and fails the condition `ε ≤ ε_0` at `p = 339738627`; at `(p, 1, 1)`, `(p, 2, 4)`, `(p, 1, 3)` the least such integers are `169869315`, `679477255`, `509607941`. (c) The level automaton has at least six translation-invariant invariant laws `μ_a`, one per value, with `μ_a(v_y ≠ a) ≤ 1/42024960` at every site `y`; they are pairwise distinct; under the extremal decomposition (named under Imports) there are at least six extremal invariant laws.

**Proof.** (a) T0(c) and T6. (b) T0(b) makes `ε` strictly decreasing in `p`; the runner evaluates `ε` exactly at the stated integers and their predecessors. (c) The kernel `P` of the level automaton is Feller on the compact space `M^{Z²}` (the law of a level's cylinder depends continuously on finitely many coordinates of the previous level, all laws being finite products) and commutes with the translations of `Z²`. Let `λ_t` be the law of level `t` from the all-`a` level and `λ^{(T)} = T^{−1}Σ_{t=1}^T λ_t`. By compactness a subsequence of `λ^{(T)}` has a weak limit `μ_a`; for continuous `f`, `|λ^{(T)}(Pf) − λ^{(T)}(f)| = T^{−1}|λ_{T+1}(f) − λ_1(f)| ≤ 2‖f‖/T`, and `Pf` is continuous, so `μ_a(Pf) = μ_a(f)`: `μ_a` is invariant; it is translation-invariant because every `λ_t` is. The function `1{v_y ≠ a}` is continuous and `λ_t(v_y ≠ a) ≤ 1/42024960` for every `t` by (a), so `μ_a(v_y ≠ a) ≤ 1/42024960`. For `b ≠ a`, `μ_a(v_y = a) ≥ 1 − 1/42024960 > 1/42024960 ≥ μ_b(v_y = a)`, so the six laws are distinct. If there were at most five extremal invariant laws, each `μ_a` would be a mixture of them and some extremal law would give `{v_y = a}` probability at least `1 − 1/42024960 > 1/2`; two different values cannot both exceed `1/2`, so the map from values to such extremal laws is injective, a contradiction. ∎ (E2–E3.)

*Placement.* Block 12's S0 (PR #8146) identifies the invariant laws of the level automaton with the translation-invariant laws of the formation law on `Z³`; under that identification the formation law has at least six such laws at these couplings, while block 08 (PR #8138) proves a unique law in its region `3c < 1`. Block 17 (PR #8151) proves the same for the static reading: both readings of the rule order at strong coupling on `Z³`. Not claimed: the location of the true threshold (the constants of the route are crude); the phase between block 08's region and this one.

## No-Go Discipline Gate

This note's sentence is positive (an ordered phase exists); its escapes are named for the route by which it could fail.

### N1 — Routes by which T6 could fail
1. *A configuration where the refinement fails or its tree has more than `4(n − 1)` edges* — closed for every configuration of the depth-2 cone and every depth-3 configuration with at most four noise sites, and for random and structured deeper cases (D1–D3); the proof (T4) covers all.
2. *Forks sharing a point treated as adjacent* — the first draft's error, caught by the executed check: the cause graph must alternate clusters and forks (T3's bipartite hypothesis; T1).
3. *Marked nodes that are not distinct sites* — closed: a subtree's nodes are distinct points (T4).
4. *A cluster added twice* — closed by the parent-uniqueness argument (T4).
5. *The count* — closed: the depth-first encoding (T5) and the exact counts for `k ≤ 3`.
6. *The domination* — re-proved (T0 c) and executed at every triple (B4).

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
No hidden dependence: the inputs are the axioms' sentences, block 01's rule, and the monotone order as declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the four sentences under Premises | yes (premise) |
| block 01 (`main`) | the rule and its one-site conditional | yes (premise, proposed) |
| block 12 (PR #8146) | the obligation; the level-time reading and S0 for the placement | placement only (evidence address) |
| blocks 05, 08, 17 (open PRs) | the monotone class; the uniqueness region; the static reading's order | placement only (evidence addresses) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the formation law orders at strong coupling" | executed: the kernel's closed forms; the increments; the fork size; the derivatives | executed: the coupling inequality at all `216` triples; the exact `p_0` at four weight pairs | executed: the refinement on `1024 + 2321` configurations exhaustively and on random and structured cones; the subtree counts | executed: the series constant; the bound at `ε_0`; the Cesàro identity on a finite chain | proved for every `ε ≤ ε_0` and every coupling with `ε(p, q, r) ≤ ε_0` (T4–T7); the true threshold not claimed |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling or order; none is a wall.

### N7 — Steelman
Hostile reviewer: "This is a classical theorem with a threshold of `6·10^{−9}`, far from the truth near `1/20`." Reply: the lane's rule is to re-prove what is load-bearing, and the load was the last open obligation of the record-dynamics row; the proof is carried in the lane's own coordinates and its combinatorial core is executed exhaustively on small cones, which no exposition offers; the constant is the crude one of this route and is stated as such. Conceded: the true threshold is not located; the coupling `p_0` is astronomically large.

### N8 — Cross-cycle echo
Block 12's eroder bound is the noiseless case of T4's span accounting (the potential `Σ_k M_k` at the extremes shrinks by one per level); block 17's chessboard-and-contour argument is the static reading's counterpart; blocks 19–23 place the sphere law's kernel.

## Falsifiers
- A kernel closed form that differs from block 01's conditional, a deviation with a non-negative derivative in `p`, a triple with two entries `a` whose deviation exceeds `ε`, or a coupling inequality failing at some triple (B1–B4).
- An increment other than `1/3 − δ_{jk}`, a fork pair of size other than `1`, or a pole assignment of a fork with span above `1` (C1–C2).
- A noise configuration of the tested cones on which the refinement fails, the spanning identity fails, the point graph is not a tree of arrows and forks through 1-sites rooted at `x`, a marked node is not a noise site, or `edges > 4(n − 1)` (D1–D3); a subtree count above `48^k` (D4).
- A series constant other than `192/95`, a bound at `ε_0` other than `1/42024960`, a `p_0` differing from the stated integers, or a failure of the Cesàro identity on the test chain (E1–E3).

## Boundaries and non-claims
This note proves, for the noisy majority automaton of the three-dimensional formation law in level time, that the density of ones from the all-zero level is at most `(192/95)ε/(1 − 96⁴ε)` for `96⁴ε < 1`, and hence that the formation law of the six-axis product rule started from a constant plane keeps every later site within `1/42024960` of that value whenever `ε(p, q, r) ≤ 1/(2·96⁴)`, with at least six distinct invariant laws; it does not locate the true threshold, does not treat couplings between block 08's uniqueness region and this one, does not treat other menus or orders, does not select a reading, rule or coupling as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 01 (on `main`): the rule and its conditional; proposed, unaudited. PRs #8003, #8138, #8146 and #8151 (open) referenced as evidence addresses for the monotone class, the uniqueness region, the obligation and the static counterpart.
- Re-proved at scope: T0 (block 12's closed forms, monotonicity, domination), T1–T4 (the construction and its accounting, after Gács's exposition of the Berman–Simon proof, in the level-time coordinates), T5 (the depth-first encoding), T6, T7 (the Cesàro argument and the distinctness).
- Named standard imports at definition level (never as authority for physics): the union bound and independence of the noise variables; weak compactness of probability laws on a compact product space (the Krylov–Bogolyubov construction of invariant laws for Feller kernels); the extremal decomposition of invariant laws (Choquet).
- Reference only (named, not used): Toom (1980); Berman–Simon (1988); Gács (2021); Swart–Szabó–Toninelli (2022); Bramson–Gray (1991).

## Review record
Supervisor-run block (owner directive 2026-09-16: sync main, read the latest PRs, take the highest-leverage science). The lane assessment read the owner's drafts #8159–#8166 (the fixed-coupling compact U(1) bridge, his live personal campaign, with "the compact winding sum and the uniform susceptibility" and "the compact-to-comparison source map" as his own next steps) and his closed seam blocks #8114 and #8122; working the photon bridge in parallel would collide with live work; block 12's obligation S6 is held by nobody and is proof-shaped. The control (`specs/supervisor_control_block25_toom_stability.py`, with the construction in `specs/supervisor_control_block25_toom_core.py`) implemented the whole refinement and ran it exhaustively on the depth-2 cone, on all depth-3 configurations with at most four noise sites, on random cones of depth `3`–`10` and on structured seeds; its first draft let two forks sharing a point be adjacent in the cause graph, which skipped the cluster between them and produced a tree with more edges than `4(n − 1)` on the very first configuration; the bipartite cause graph fixed it and every later case passed (worst ratio `2.875`). The lens pass is in `GOAL_block25.md`; the primary seat wrote T0–T7 and the runner; the refuting pass (`CHECKER_block25_findings.md`) checked the spanning identity on random abstract instances built independently of the automaton, the noise map against direct enumeration in floating point at random weights, the series constant by direct summation, the tree checks with an independent implementation of the graph, and the stability empirically by simulation far above `ε_0`. Facts settled while executing: the tree must alternate clusters and forks; a cluster at a level has all its parents in one cluster (no duplicates); the subtree counts `12, 198, 3688` show the encoding bound `48^k` is loose by a factor about thirty at `k = 3`.

## Verification

```bash
python3 scripts/admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_noisy_level_automaton_2026_09_16.py
python3 scripts/admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_noisy_level_automaton_2026_09_16.py --list-mutations
python3 scripts/admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_noisy_level_automaton_2026_09_16.py --mutation edge_bound_claimed_tighter
```

Families: A authority and inputs; B the kernel, the noise map, the domination; C the increments and the fork size; D the explanation tree executed and the subtree counts; E the series, the thresholds, the Cesàro identity; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 13 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=22 FAIL=0`.
