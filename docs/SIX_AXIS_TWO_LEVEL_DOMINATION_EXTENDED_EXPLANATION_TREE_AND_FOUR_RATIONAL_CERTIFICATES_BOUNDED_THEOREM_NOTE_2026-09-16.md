---
claim_id: six_axis_two_level_domination_extended_explanation_tree_and_four_rational_certificates_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "For a supplied six-axis product kernel with p >= q > 0, r > 0, records-only level order, independent conditional site draws and an all-a initial plane: the two-level dissent coupling, complete extended explanation-tree construction with forks=|S|-1 and E<=3(|S|-1)+2|A|, lifted recursion bound, and four exact rational sufficient certificates imply sitewise dissent below 10^-7 and six distinct invariant laws on the stated large-p rays. Positive fixed-point parametrization is also given. No actual threshold, optimal integer, exhaustive route exclusion, physical selection or deferred-science premise is claimed."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
  - admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_of_the_noisy_level_automaton_explicit_threshold_six_invariant_laws_bounded_theorem_note_2026-09-16
runner: scripts/six_axis_two_level_domination_extended_explanation_tree_four_rational_certificates_2026_09_16.py
---

# Six-axis two-level domination, extended explanation trees and four rational certificates

**Date:** 2026-09-16
**Type:** bounded_theorem
**Status:** proposed_retained
**Audit authority:** independent audit lane only.
**Primary runner:** [six_axis_two_level_domination_extended_explanation_tree_four_rational_certificates_2026_09_16.py](../scripts/six_axis_two_level_domination_extended_explanation_tree_four_rational_certificates_2026_09_16.py)
**Planned cache:** [six_axis_two_level_domination_extended_explanation_tree_four_rational_certificates_2026_09_16.txt](../logs/runner-cache/six_axis_two_level_domination_extended_explanation_tree_four_rational_certificates_2026_09_16.txt)

## Result up front

Separating rare seed dissent from amplification of existing dissent gives four exact sufficient bounds. The complete coupling and tree argument follows below, with its supplied hypotheses. The four rational certificates improve the earlier sufficient integers by at least 68 (approximately 69). They do not locate an actual transition. Fresh corrected-source execution is pending; the source defines 17 checks and 11 mathematical mutations. Historical outputs remain exact recovery, not a fresh result.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Sufficient stability bounds for a supplied level product process"
source_of_blocker_text: review_loop
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independent affected-source review and bounded evidence capture; consumer is a future sharper supplied-process stability bound"
conditional_surface_status: "p >= q > 0, r > 0; supplied six-axis menu, records-only level order, independent conditional updates and all-a initial plane"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Conditional complete coupling/tree proofs and four rational sufficient certificates; deferred negative claims are not premises"
```

## Premises and declared objects

The [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the lattice, one-site possibility, admissibility and fixed-record vocabulary. The [product-rule parent](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md) defines the six-axis orbit weights and the records-only product conditional. The [single-noise formation theorem](ADMISSIBILITY_RULE_THREE_DIMENSIONAL_FORMATION_LAW_ORDERED_PHASE_STABILITY_OF_THE_NOISY_LEVEL_AUTOMATON_EXPLICIT_THRESHOLD_SIX_INVARIANT_LAWS_BOUNDED_THEOREM_NOTE_2026-09-16.md) supplies the earlier sufficient-certificate comparison and the pole-transport construction reproduced completely below. These are conditional source results, not physical rule selection. The registered primitives supply units, graining and pointwise realized-state evaluation at their own scope; no choice of these weights, menu, initial state or process is attributed to them.

All product weights and all updates here are supplied mathematical hypotheses: p >= q > 0, r > 0; records form in level order, with independent draws at distinct sites conditional on the previous level; the initial plane is all a. Weak compactness on a finite-alphabet product space and, only for the optional extreme-law conclusion, stationary barycentric decomposition are standard mathematical imports.

Declared objects.
- **The rule, level time, the level automaton, the coarse-graining, the deviations.** Supplied model: the six-axis menu with `φ(v, v') = p, q, r` for equal, antipodal, orthogonal pairs; sites `x ∈ Z³`, level `τ(x) = x_1 + x_2 + x_3`, predecessors `x − e_j`, siblings `x ± (e_i − e_j)`; records form level by level from `K(· | v_{x−e_1}, v_{x−e_2}, v_{x−e_3}) ∝ Π_j φ(v, v_{x−e_j})`, level `0` all equal to `a`; `ξ_x = 1{v_x ≠ a}`; `d_1 = 1 − K(a | a, a, a)`, `d_2 = 1 − K(a | a, a, −a)`, `d_3 = 1 − K(a | a, a, b)` for `b ⊥ a`, in the closed forms of T1; `ε₁ := d_1`, `ε₂ := max(d_2, d_3)`.
- **The two-level noisy majority automaton `η'`.** With i.i.d. uniforms `U_x` on levels `≥ 1` and `η' ≡ 0` on levels `≤ 0`: `η'_x = 1` if at least two of `η'_{x−e_j}` are `1`; `η'_x = 1{U_x < ε₂}` if exactly one is `1`; `η'_x = 1{U_x < ε₁}` if none is. A **1-site** has `η'_x = 1`; a **seed** is a 1-site with no 1-predecessor; an **amplified site** is a 1-site with exactly one 1-predecessor (its **amplification direction** `j` is the index of that predecessor); a **processed-type site** has at least two, and its **winning pair** is the pair of 1-predecessors with the two smallest indices.
- **The graph `G`, the functionals, spanned sets, the excuse.** Definitions: arrows `{x, x − e_j}`, forks `{x, x ± (e_i − e_j)}`, degree `12`; `M_k(z) = z_k − τ(z)/3`; `Span(P, v_1, v_2, v_3) = Σ_k M_k(v_k)`; for a processed-type `v`, `Excuse_k(v)` is the winning-pair member with index `≠ k` (the smaller if both), with `M_k(Excuse_k(v)) = M_k(v) + 1/3`; for an amplified `v` with direction `j`, `Excuse_k(v) := v − e_j` for every `k`, with `M_k(v − e_j) − M_k(v) = 1/3 − δ_{jk}`; the pair `(v, k)` is **bad** if `v` is amplified with direction `k`.
- **The extended arrow graph and clusters.** At level `s`, vertices the 1-sites of levels `≤ s`, an edge from every processed-type or amplified site to each of its 1-predecessors; a **cluster at level `s`** is the intersection with level `s` of a connected component. A seed is a singleton cluster.
- **Extended explanation trees.** Subtrees `T` of `G` containing `x` with at most one arrow to a predecessor at each node; `S(T)` the nodes without such an arrow, `A(T)` the nodes whose arrow to a predecessor is labelled an amplification arrow, `E(T)` the number of excuse arrows, `F(T)` the number of forks; `𝓔` the family with `F = |S| − 1` and `E ≤ 3(|S| − 1) + 2|A|`.
- **The recursion and its domain.** `D = (1 + xU)²(1 + 3xD)(1 + yF)⁶`, `U = (1 + xU)³(1 + yF)⁶`, `F = (1 + xU)³(1 + 3xD)(1 + yF)⁵`, `R = (1 + xU)³(1 + 3xD)(1 + yF)⁶` (restated in the count theorem below); its **domain** `𝒟` is the set of `(x, y) ≥ 0` at which the iteration from `(1, 1, 1)` stays bounded; a **super-solution** at `(x, y)` is a triple `(D̄, Ū, F̄) ≥ 1` dominating its own right sides.

## Theorem T1 — two-level domination on the stated weight domain

**Statement.** For p >= q > 0 and r > 0 the deviations below satisfy d1 <= d2 <= max(d2,d3). Each di is strictly decreasing in p for all p,q,r > 0. Under the supplied conditionally independent level product law, the dissent indicator from the all-a plane is coupled below the two-level automaton.

**Proof of formulas and monotonicity.** Sum the six product weights for triples (a,a,a), (a,a,−a), (a,a,b), b perpendicular to a. Their aligned probabilities are respectively p³/(p³+q³+4r³), p²q/(pq(p+q)+4r³), and p²/(p²+q²+r(p+q)+2r²). Therefore

```
d1 = 1 − p³/(p³+q³+4r³),
d2 = 1 − p²q/(pq(p+q)+4r³),
d3 = 1 − p²/(p²+q²+r(p+q)+2r²).
∂p d1 = −3p²(q³+4r³)/(p³+q³+4r³)²,
∂p d2 = −(q³p²+8qr³p)/(pq(p+q)+4r³)²,
∂p d3 = −p(rp+2q²+2rq+4r²)/(p²+q²+r(p+q)+2r²)².
```

Every derivative is strictly negative. Put A=p³+q³+4r³ and B=pq(p+q)+4r³. Direct subtraction gives

```
d2 − d1 = p²(p−q)[q²(p+q)+4r³]/(A B) >= 0.
```

Here p >= q is essential: at (p,q,r)=(1/10,1,1), d1=5000/5001 while d2=d3=410/411. This exact example explains the scope correction; it does not invalidate the four large-p certificates.

**Proof of the coupling.** Build both processes level by level with independent uniforms at different sites. If at least two comparison predecessors dissent, set the comparison value to one and it dominates. If exactly one comparison predecessor dissents, at most one actual predecessor differs from a. The actual dissent probability is one of d1,d2,d3, hence at most epsilon2=max(d2,d3) by the factorization. If no comparison predecessor dissents, all actual predecessors equal a and dissent has probability epsilon1=d1. Draw actual dissent as 1{U<d} and comparison dissent as 1{U<epsilon_i}. Conditional on actual dissent, use an additional independent draw for the five non-a possibilities to recover the entire six-state product kernel. This constructs the correct conditionally independent laws and preserves domination by induction. Finite ancestor cones make the induction local at every infinite-plane site. ∎

## Theorem T2 — the extended explanation tree

**Statement.** Let `η'_x = 1`. Then there is `T ∈ 𝓔` rooted at `x` all of whose nodes are 1-sites, such that every node of `S(T)` is a seed, every node of `A(T)` is an amplified site whose amplification arrow ends at its single 1-predecessor, and every other node is processed-type with its excuse arrow to a 1-predecessor.

**Finite localization before refinement.** Fix a site x at level n > 0. Its ancestor cone down to level zero consists of the finitely many x − a with a in the nonnegative integer triples and sum(a) <= n. Every positive-level site's three predecessors belong to the cone. Set sites outside it to zero for this construction and keep the prescribed zero level; induction in level shows that all values in this cone equal the values of the infinite process. Apply the cluster construction to this finite directed graph. Restricting a cluster in this way changes no predecessor of any included positive-level point, hence no winning pair, seed or amplified classification used by the construction. All paths and shortest paths below are now finite. The resulting finite explanation tree embeds in the original infinite graph. This supplies the infinite-process use without assuming finite global clusters.

**Proof.** The extended construction has three features: the arrow graph links amplified sites to their single 1-predecessor, so they lie inside clusters; the excuse of an amplified pole is that predecessor, for every charge; and bad amplified poles are always kept. The ingredients, restated.
*(T2.1, clusters and the cause graph.)* For a cluster `K` at level `s` with no seed, let `V_K` be the clusters at level `s − 1` containing a 1-predecessor of a point of `K`, two of them adjacent if a fork joins a point of one to a point of the other; this graph is connected and every `Excuse_k(v)`, `v ∈ K`, lies in a cluster of `V_K`. Proof: two points of `K` are joined by a path through 1-sites of levels `≤ s`; cut it at its visits to level `s`; between visits it stays below and its end predecessors are in one cluster of level `s − 1`; at a visit `k` it arrives from a 1-predecessor `r` and leaves to a 1-predecessor `r'` (equal if `k` is amplified), and `r, r'` are siblings or equal, hence forked or in one cluster; any cluster of `V_K` contains a predecessor of some `k ∈ K`, a sibling of the one the path uses. The excuse of a point is one of its 1-predecessors.
*(T2.2, the excuse identity.)* For a spanned set `(P, v_1, v_2, v_3)` with no seed pole, `Σ_k M_k(Excuse_k(v_k)) = Span + 1 − b`, where `b` is the number of bad pairs `(v_k, k)`: each processed-type pole contributes `+1/3` for its charge, an amplified pole `+1/3` for the charges other than its direction and `−2/3` for its direction (C1). A fork pair has `Size = 1`, so a spanned set on it has `Span ≤ 1` (because the coordinate maxima on a sibling pair sum to one).
*(T2.3, the spanning lemma and complete pole transport.)*


**Statement.** Let `(L, u_1, u_2, u_3)` be a spanned set. Let `𝓒` be a family of pairwise disjoint subsets of `L` (**clusters**) and `𝓕` a family of two-point subsets of `L` (**forks**), each fork meeting two distinct clusters in one point each, such that the bipartite graph `B` (a cluster adjacent to the forks that meet it) is connected and each pole `u_k` lies in a cluster `C_k ∈ 𝓒`. Then there is a subtree `𝒯` of `B` containing `C_1, C_2, C_3` and minimal (every leaf of `𝒯` is one of the `C_k`; in particular every fork in `𝒯` has both its clusters in `𝒯`), and for each `X ∈ 𝒯` a point set `X' ⊂ X` and poles `u_{X,1}, u_{X,2}, u_{X,3} ∈ X'` such that
```
Σ_{X ∈ 𝒯} Σ_k M_k(u_{X,k}) = Σ_k M_k(u_k),
```
`X'` consists of `u_k` (when `X = C_k`) and the meeting points of `X` with its neighbours in `𝒯`, every point of `X'` is a pole of `X`, and `X' = X` for a fork.

**Proof.** *Construction.* Take a shortest path in `B` from `C_1` to `C_2`, then a shortest path from `C_3` to a vertex of that path, and delete non-terminal leaves until none remain: a minimal subtree `𝒯` (a fork in `𝒯` cannot be a leaf, so it keeps both its clusters). For adjacent `X, Y ∈ 𝒯` let `m(X, Y)` be their unique common point. Put `X' = {u_k : X = C_k} ∪ {m(X, Y) : Y ∼ X in 𝒯}`. For each `k`: if `u_k ∈ X'` put `u_{X,k} = u_k`; otherwise let `Y` be the neighbour of `X` on the path of `𝒯` from `X` to `C_k` and put `u_{X,k} = m(X, Y)`. *Every point of `X'` is a pole.* A meeting point `m(X, Y)`: removing `X` leaves a subtree through `Y` whose leaves are terminals, so some `C_k` lies beyond `Y`; then either `u_k ∉ X'` and `u_{X,k} = m(X, Y)`, or `u_k ∈ X'`, which forces `u_k = m(X, Y)` (a fork containing `u_k` meets `C_k` and `X`, so the path from `X` to `C_k` uses that fork). *The identity.* Let `V = ∪_X X'` and, for `v ∈ V`, `I(v) = {X ∈ 𝒯 : v ∈ X'}`: the unique cluster `C ∋ v` and the forks of `𝒯` containing `v`, each of which is adjacent to `C` in `𝒯` (a fork in `𝒯` has degree two). Fix `v` and a charge `k`. If `v = u_k`, then `u_{X,k} = v` for every `X ∈ I(v)`. If `v ≠ u_k`, let `Y_0` be the neighbour of `C` toward `C_k` (or `C = C_k`): the forks `f ∋ v` of `I(v)` other than `Y_0` have `u_{f,k} = m(f, C) = v`; and, when `v ∈ Y_0`, exactly one of `C` and `Y_0` has its pole at `v` (`C` iff `v ∈ Y_0`, in which case `Y_0`'s pole is its other point; if `C = C_k`, `C`'s pole is `u_k ≠ v` and all forks have theirs at `v`). When `v ∉ Y_0`, neither contributes at `v` and the other incident forks supply `|I(v)| − 1`. So `#{X ∈ I(v) : u_{X,k} = v} = |I(v)| − 1 + [v = u_k]`. Hence `Σ_X Span(X) = Σ_v Σ_k M_k(v)(|I(v)| − 1 + [v = u_k]) = Σ_v (|I(v)| − 1)·0 + Σ_k M_k(u_k)`. ∎


*(T2.4, refinement and accounting.)* A partial tree: unprocessed spanned clusters `𝒰`, processed points, and edges (excuse arrows, amplification arrows, forks) whose cluster-contracted graph is a tree; potential `Φ = Σ_𝒰 Span + #forks`. Start with `({x}, x, x, x)`, `Φ = 0`. While an unprocessed cluster `(K, v)` has a non-seed pole (then `K` has no seed, a seed being a singleton): put `u_k = Excuse_k(v_k)`, `b` the number of bad pairs; apply T2.3 to `(∪V_K, u_1, u_2, u_3)` with the clusters of `V_K` and one fork per adjacent pair; add the clusters of `𝒯` with their poles to `𝒰` and the forks of `𝒯` as edges; the *kept poles* are the distinct points among `v_1, v_2, v_3` that are incident to an existing edge or are bad amplified poles (if none, `v_1`); for a kept processed-type `w` add the excuse arrow `{w, u_{k(w)}}`, `k(w)` the least `k` with `v_k = w`; for a kept amplified `w` add the amplification arrow `{w, w − e_j}` to its predecessor; delete `(K, v)`. *Tree property:* under the following invariant — `K` is replaced by `𝒯` with the kept points attached by one arrow each; a cluster at level `s − 1` has all its level-`s` parents in one cluster, now also for amplified parents (they are linked to their predecessor), so no cluster is added twice; kept points are processed once. *The potential:* by T2.2 and T2.3, `Σ_{X∈𝒯} Span(X) = Span(K) + 1 − b`, and each fork counts `1` against a span of at most `1`, so `Φ` rises by at least `1 − b`. *Termination:* levels descend; every 1-site at level `1` is a seed. *The count:* let `S` be the seeds left as singleton clusters, `A` the kept amplified points, `B = Σ b` over refinements. `Φ` ends at `#forks` and rose by at least `1 − b` per refinement from `0`, so `#refinements ≤ #forks + B`. Contract every arrow of either kind into its lower point: each processed point and each amplified point merges, along its own arrow and the arrows below, into a seed; the forks then form a tree on the seeds, so `#forks = |S| − 1`. A bad pair is an amplified pole in its own direction; a point is a pole of at most one refined cluster (its own) and is bad for at most one charge, and bad amplified poles are kept, so `B ≤ |A|`. Arrows number at most three per refinement (one per kept pole) and every kept amplified pole carries an amplification arrow, so `E + |A| ≤ 3(|S| − 1 + B) ≤ 3(|S| − 1) + 3|A|`, i.e. `E ≤ 3(|S| − 1) + 2|A|`. Every node has at most one arrow to a predecessor (its own), the nodes without one are the seeds, and the amplified nodes' arrows end at their single 1-predecessor. ∎

## Theorem T3 — the count and the bound

**Statement.** For every site `x` and every `t ∈ (0, 1]` with `(t + ε₂/t², ε₁/t³) ∈ 𝒟`,
```
P(η'_x = 1) ≤ ε₁ · R(t + ε₂/t², ε₁/t³).
```

**Proof.** By T2 and independence of the uniforms at distinct sites, `P(η'_x = 1) ≤ Σ_{T∈𝓔} ε₁^{|S(T)|} ε₂^{|A(T)|}` (a seed has `U < ε₁`, an amplified node `U < ε₂`). For `T ∈ 𝓔`, `|S| = F + 1` and `E ≤ 3F + 2|A|`, so with `t ≤ 1`: `ε₁^{|S|} ε₂^{|A|} = ε₁·ε₁^{F}·ε₂^{|A|} ≤ ε₁ · t^{E}·(ε₁/t³)^{F}·(ε₂/t²)^{|A|}`. The right side is the weight of `T` with `t` per excuse arrow, `ε₂/t²` per amplification arrow and `ε₁/t³` per fork; both kinds of arrow are arrows of `G` (an edge to a predecessor), so in the lift of `T` to the typed regular tree (the words of edge types along root paths, injective, with at most one *down* child per vertex and none after an *up* letter) an arrow slot carries the total weight `t + ε₂/t²`. The weight sum over all admissible subtrees of the typed tree is `lim_h R_h(x, y)` with `x = t + ε₂/t²`, `y = ε₁/t³`, where `R_h` are the recursion's height-`h` truncations from `(1, 1, 1)`; a super-solution bounds every `R_h` by induction (the right sides are increasing), so the sum is at most `R̄`, and `(x, y) ∈ 𝒟` is exactly the existence of a bounded iteration. ∎

**The complete slot count.** Give each edge its displacement label: three down, three up, six fork labels. A rooted lattice tree has a unique root path to each vertex; reading its labels gives a word, and projecting that word's displacements recovers the lattice vertex and all edges. Thus distinct rooted trees have distinct lifts. After a down step, the reverse up slot is occupied, leaving two up slots, at most one of three down slots, and six fork slots; its contribution is D. After an up step, the reverse down arrow is occupied, so there are no further down slots, three up slots and six fork slots; its contribution is U. After a fork step, five fork slots remain with three up slots and at most one of three down slots; this is F. The root has all six fork slots and the root expression R. Independent optional up/fork slots give factors (1+xU) and (1+yF); the choice of zero or one of three down slots gives (1+3xD). These are precisely the four displayed recursions. Forgetting geometric collisions only adds lifted subtrees, so this count is an upper bound. Height truncations increase from (1,1,1); a finite super-solution bounds every truncation and therefore their nonnegative weight sum.

## Theorem T4 — four rational certificates and six invariant laws

**Statement.** Under the supplied process and weight hypotheses, from the all-a plane, P(v_x != a) < 10^−7 at every later site on each ray: p >= 4165 at (p,1,2); p >= 2085 at (p,1,1); p >= 8330 at (p,2,4); p >= 6247 at (p,1,3). The level process has at least six pairwise distinct translation-invariant invariant laws. The inequalities hold for real p on these rays, in particular for integers.

**Exact certificates.** With x=t+epsilon2/t² and y=epsilon1/t³, the following positive rational triples dominate the three recursion right sides, entry by entry:

| (p,q,r) | t | Dbar | Ubar | Fbar |
|---|---|---|---|---|
| (4165,1,2) | 99/1000 | 56694252249173/500000000000 | 3279872914431/1000000000000 | 168429466648591/1000000000000 |
| (2085,1,1) | 49/500 | 88632394933177/1000000000000 | 3254100818939/1000000000000 | 131311435970231/1000000000000 |
| (8330,2,4) | 99/1000 | 56694252249173/500000000000 | 3279872914431/1000000000000 | 168429466648591/1000000000000 |
| (6247,1,3) | 99/1000 | 24445325573453/250000000000 | 3264868815393/1000000000000 | 9064364177089/62500000000 |

For each row define Rbar=(1+x Ubar)³(1+3x Dbar)(1+y Fbar)⁶. Substitution in exact rational arithmetic gives epsilon1 Rbar < 1/10^7. Approximate values, for readability only, are respectively 7.6934551567, 7.2441560890, 7.6934551567 and 6.4848260436 times 10^−8; the strict rational inequalities are the certificates. All entries are at least one. Since the deviations decrease with p, the same t and triple remain super-solutions along the entire larger-p ray. T1 and T3 therefore prove the stated uniform probability bound.

**Invariant-law construction.** The finite-menu configuration space M^{Z²} is compact metrizable. The level kernel P is Feller: a cylinder's next-step law depends continuously on finitely many old coordinates, and cylinder functions uniformly approximate continuous functions. It commutes with plane translations. If lambda_t is the level-t law from the all-a plane, the Cesaro average lambda^(T)=T^−1 sum_{t=1}^T lambda_t has a weakly convergent subsequence by compactness. For every continuous f,

```
|lambda^(T)(Pf) − lambda^(T)(f)|
 = |lambda_(T+1)(f) − lambda_1(f)|/T <= 2||f||/T.
```

Feller continuity passes this identity to the limit mu_a, making it invariant. Translation invariance also passes to the limit. The single-site dissent indicator is continuous, so mu_a(v_y != a) <= 10^−7. For b != a, mu_a(v_y=a) >= 1−10^−7 > 10^−7 >= mu_b(v_y=a); the six laws are distinct. If one also imports barycentric decomposition of stationary laws for this compact Feller process, at least six extreme stationary laws exist: if there were at most five, each mu_a would be a mixture of these finitely many laws, so some extreme law would give v_y=a probability greater than 1/2; the same extreme law cannot do this for two distinct a. The six directly constructed laws need no extremal-decomposition import. ∎

The earlier single-noise sufficient thresholds are 285718, 142861, 571436 and 428576 on the corresponding rays. Their ratios to the four displayed integers are at least 68 and approximately 69, not at least 69. These compare sufficient certificates, not physical thresholds or optimal integers for this method.

## Theorem T5 — positive fixed-point parametrization

For 1 <= v < 3/2 put x=(v−1)/v³ and y=0. Then U=v³, D=v²/(1−3xv²), F=v³(1+3xD) give a finite nonnegative fixed point of all three recursions. The denominator equals (3−2v)/v and is positive. Direct substitution proves the claim; all three entries are at least one and bound the iteration from (1,1,1). The map x(v) has derivative (3−2v)/v⁴ and increases from 0 to 4/27 on this half-open interval. Also t²(4/27−t) has derivative t(8/27−3t), and its maximum on [0,4/27] is 256/531441 at t=8/81.

The complete corrected full-domain, strict-endpoint and necessary-route-bound argument is preserved readably in the deferred-science recovery. That scoped mathematical proof remains valid; its formal negative-certification promotion and the broader route-exhaustion conclusions are deferred. It is not a premise of the positive certificate theorem.

## No-Go Discipline Gate

### N1 — Actual route record and deferred promotion
The historical list mixed tests of one construction with proposed alternatives. It does not establish five normalized attempted negative families. No formal negative packet PASS or exhaustive route closure is asserted. The exact original list, complete corrected route-bound proof and untested sharper constructions are retained in [historical recovery](work_history/repo/review_feedback/pr8174-evidence/README.md). The positive theorem does not use deferred conclusions.

### N2 — Relation of open obligations
Sharper bad-pair accounting and an overlap-controlled tree-of-trees count are open research obligations. Their independence is not established and no numerical wall count is claimed.

### N3 — Explicit hypotheses
The menu, p >= q > 0, r > 0, records-only product update, level order, conditional independence and constant plane are supplied. Compactness and optional extremal decomposition are mathematical imports, not hidden physical premises.

### N4 — Source roles
The axiom memo supplies framework vocabulary, the product-rule parent the conditional model, and the single-noise parent the earlier certificate comparison and reproduced transport construction. Historical simulations and floating scans are not threshold or negative-certificate authorities.

### N5 — Resolution
The primary defines finite exact formula checks, all 216 triples at five declared weight triples, exhaustive small cones, 1200 seeded random cones, 66103 finite lifted-tree candidates and four rational certificates. The original primary output reports 932+2321+843=4096 explained configurations; the distinct 1500-random-cone historical construction control reports 4290. These are separate historical protocols. Corrected-source outcomes remain pending. Infinite-plane statements use the written localization, probability and compactness proofs, not an executed infinite lattice.

### N6 — Partial paths
Treating amplified nodes as leaves loses the two-level improvement; it does not make the ordered region empty, since epsilon2 tends to zero along fixed-q,r large-p rays. No new primitive is requested. Other counting and coupling arguments remain open.

### N7 — Strongest unresolved alternative
An overlap-controlled cluster or tree-of-trees argument, or a sharper bad-pair potential, might improve the sufficient region. The historical packet supplies neither an explicit overlap/cycle witness closing all constructions nor a proof of the sharper budget. Their estimates remain proposals.

### N8 — Historical comparison
The prior single-noise construction is a positive sufficient result. The archived finite simulations and floating scans cannot establish a true infinite-volume threshold or exhaustive optimality. The branch retains recovery value for those deferred proposals.

## Boundaries and imports

The result is conditional on the stated model and initial plane. No physical rule, formation schedule, coupling value or readout bridge is selected. No actual threshold or optimal integer is claimed. The two-level tree proof and rational certificates stand independently of the deferred negative packet. Standard compactness and optional stationary-law decomposition have precisely the roles stated in T4. No fitted or observed value is an input.

## Review and verification record

Original source findings corrected the weight domain and strict endpoint, supplied complete localization and pole transport, separated finite controls from universal proofs, repaired input/graph links, and quarantined unsupported threshold and no-go claims. All original source and raw evidence is recovered exactly in the [archive](work_history/repo/review_feedback/pr8174-evidence/README.md); historical author PASS wording is not present-day review authority.

The paired runner preserves the original construction, cone fixtures, random seed, lifted enumeration and four rational certificates. It strengthens derivative and domain controls and writes input/source-bound JSON under logs/runner-cache. Eleven mathematical mutations are declared, with no successful outcomes claimed before execution. Two original prose-only mutations remain recoverable in the historical runner. Expected baseline contract: `TOTAL: PASS=17 FAIL=0`, subject to actual future execution. Neither primary nor mutation execution occurred during preparation.
