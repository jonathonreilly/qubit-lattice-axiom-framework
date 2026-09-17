---
claim_id: admissibility_rule_six_axis_formation_threshold_the_sharper_bad_pair_budget_is_false_for_the_extended_explanation_tree_explicit_witnesses_and_the_two_level_period_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "For the two-level noisy majority automaton of block 30 (PR #8174) in level time on Z^3 — a site with at least two 1-predecessors is 1, a site with exactly one is 1 only by a noise mark, a site with none only by a noise mark — and block 30's extended explanation tree (seeds S, amplified nodes A with an arrow to their single 1-predecessor, processed nodes with an excuse arrow, forks; the potential Sum of the poles' charges plus the number of forks; bad pairs): (T1) the accounting identities — an amplified excuse changes the charge k by 1/3 - delta_{jk}; the potential rises by 1 - b at a fork-free refinement with b bad pairs and by at most 1 - b + (forks created) otherwise; the rises sum to the number of forks; the excuse arrows and amplified nodes sum over the refinements to E and |A| — and the two-level period: a fork-free refinement with three processed poles (rise 1, three excuse arrows) followed by one with two bad poles and one processed pole (rise -1, one excuse arrow, two amplified nodes) is rise-neutral with four excuse arrows per two amplified nodes, ratio 2 (proved); (T2) the sharper bad-pair budget E <= 3(|S| - 1) + |A| named open in block 30 is false for this construction: three explicit noise configurations (windows 4x4x7 and 5x5x9), re-executed through the automaton and the construction, have valid trees with (E, |A|, |S|) = (16, 10, 1), (20, 12, 1), (23, 12, 2), inside block 30's budget E <= 3(|S| - 1) + 2|A| and above the sharper one by 6, 8 and 8, so that any constant c with E <= 3(|S| - 1) + c|A| on every tree of this construction satisfies c >= 5/3; the first witness's noise marks are exactly its tree's seed and ten amplified nodes; uniformly random cones (300 in the runner, 40 000 in the controls) never exceed the ratio 1, which places block 30's executed maximum 2/3 as a sampling artefact (proved by exhibition; executed); (T3) the stake the refuted budget would have had: with the amplification weight epsilon_2/t the exact super-solutions at (t + epsilon_2/t, epsilon_1/t^3) give p >= 453 at (p, 1, 2), 232 at (p, 1, 1), 905 at (p, 2, 4), 677 at (p, 1, 3), a factor between 8 and 10 below block 30, under a ceiling 4/729 at t = 2/27 crossed between p = 367 and 368 on (p, 1, 2) — none of it claimed as a region (conditional on the false budget; exact). Not claimed: that the constant 2 is attained (the period gives 2 per period; chains of arbitrary length are not constructed); a lowering of block 30's ceiling; anything about a differently built tree; the true strength. No reading, rule or coupling is selected as physical; exact arithmetic throughout the runner."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_six_axis_formation_threshold_sharper_bad_pair_budget_false_explicit_witnesses_and_the_two_level_period_2026_09_16.py
---

# The sharper bad-pair budget is false for the extended explanation tree: explicit witnesses at `8/5` and `5/3` inside block 30's budget, and the two-level period of ratio `2`

**Date:** 2026-09-16
**Type:** bounded_theorem
**Status:** bounded-support (exact; a route pruned by exhibition; conditional on the named supplied readings; unaudited)

## Result up front

Block 30 (PR #8174) lifted the six-axis formation threshold to `p ≥ 4165` at
`(p, 1, 2)` and named, as the first item after it, a sharper accounting for
its extended explanation tree: `E ≤ 3(|S| − 1) + |A|` in place of the proved
`E ≤ 3(|S| − 1) + 2|A|`, where `E` counts excuse arrows, `S` the seeds and `A`
the amplified nodes. Every executed tree of block 30 used at most `2/3` of the
allowed two arrows per amplified node, and a proof of the sharper budget
would have moved the region to `p ≈ 500`. This note closes that item in the
negative.

The sharper budget is false for the construction. A hill-climb over noise
configurations in a `4×4×7` window finds trees with `(E, |A|, |S|) =
(16, 10, 1)` and `(20, 12, 1)`, and a `5×5×9` window gives `(23, 12, 2)`; each
is a valid extended explanation tree, each lies inside block 30's budget, and
each exceeds the sharper one — by `6`, `8` and `8`. Their ratio
`(E − 3(|S| − 1))/|A|` is `8/5`, `5/3`, `5/3`, so any constant `c` with
`E ≤ 3(|S| − 1) + c|A|` on every tree of this construction is at least `5/3`.
The first witness is self-contained: its eleven noise marks are exactly its
tree's seed and ten amplified nodes. The mechanism is read off the
construction's own log. Two kinds of refinement alternate: one keeps three
processed poles (three excuse arrows, and the potential rises by one), the
next keeps two bad amplified poles and one processed pole (one excuse arrow,
two amplified nodes, and the potential falls by one). The pair is neutral for
the potential and spends four excuse arrows on two amplified nodes — ratio
exactly `2`, the constant block 30 proved. Uniform random sampling never
sees this: `40 000` random cones stay at or below ratio `1`, which is why
block 30 measured `2/3`.

What the route would have been worth is recorded and not claimed: under the
false budget the exact certificates give `p ≥ 453` on `(p, 1, 2)` and a
factor between `8` and `10` on every line, with a ceiling `4/729`. Block 30's
ceiling `256/531441` stands. The remaining factor from `4165` to the located
`11` must be sought in a differently built tree or a different count, not in
this accounting.

In plain words: the earlier proof allowed each cheap dissent to drag along
two expensive explanations, and every example we had looked at used less
than one. We hoped the proof was merely loose. It is not: a deliberately
built example makes the cheap dissents come in pairs, and each pair really
does drag along four explanations. The allowance of two was the truth about
this way of counting, so the next improvement has to count differently.

Exactly: the identities and the period (T1); the witnesses (T2); the stake
(T3). Executed with exact arithmetic: 20 checks, 9 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "block 30's first open item: the sharper bad-pair budget E <= 3(|S| - 1) + |A| for the extended explanation tree (would give p of order 500 at (p, 1, 2))"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the item closed in the negative by exhibition: three witnesses with ratio 8/5, 5/3, 5/3 inside block 30's budget; the two-level period has ratio exactly 2; the stake (p >= 453 on (p, 1, 2)) recorded and not claimed. Next for the threshold: a count of the amplification part by clusters rather than sub-structures, or a tree built with a different pole rule (the witnesses are the test cases either must pass); the overlap-free tree of trees remains blocked. Consumers: the campaign's decision record; block 30's N1 item 5"
conditional_surface_status: "T1 proved for the construction as declared; T2 proved by exhibition and executed (the witnesses rebuilt from their noise marks; every arrow checked against the 1-predecessors; block 30's budget verified on them); T3 exact and conditional on the false budget, recorded as the stake only; conditional on the records-only reading, positivity, the six-axis menu and the monotone order as supplied conditions for the automaton's meaning; the standard mathematical imports named at definition level"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", "Records form.", and "Only records are readable.". Block 01 (`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`, on `main`) supplies the rule and its one-site conditional given a recorded set; the level automaton, the two-level domination and the extended explanation tree are block 30's objects (PR #8174, an open hand-off referenced as an evidence address), restated here as declared objects and re-executed by the runner's embedded construction. All proposed and unaudited.

Declared objects.
- **Level time and the one-sided automaton.** Sites `x ∈ Z³`, level `τ(x) = x_1 + x_2 + x_3`, predecessors `x − e_j`, siblings `x ± (e_i − e_j)`. A **noise set** `ζ` is a set of sites; the automaton sets `η_x = 1` if at least two of `η_{x−e_j}` are `1`, and otherwise `η_x = 1` if and only if `x ∈ ζ`; sites outside the window are `0`. This is block 30's automaton `η'` with the uniforms replaced by the marks they produce: `ζ` is the set of sites at which the uniform falls below the relevant noise level. A **seed** is a 1-site with no 1-predecessor, an **amplified site** one with exactly one (its **direction** `j` is the index of that predecessor), a **processed-type site** one with at least two; the **winning pair** of a processed-type site is its two 1-predecessors of smallest index.
- **The graph `G`, the functionals, the excuse, bad pairs.** Arrows `{x, x − e_j}`, forks `{x, x ± (e_i − e_j)}`; `M_k(z) = z_k − τ(z)/3`; for a processed-type `v`, `Excuse_k(v)` is the winning-pair member with index `≠ k` (the smaller if both); for an amplified `v` with direction `j`, `Excuse_k(v) = v − e_j` for every `k`; the pair `(v, k)` is **bad** if `v` is amplified with direction `k`.
- **Clusters, poles, refinements — block 30's construction.** At level `s` the clusters are the level-`s` parts of the components of the graph on 1-sites of levels `≤ s` with an edge from each processed-type or amplified site to each of its 1-predecessors. A cluster carries three **poles** `(p_0, p_1, p_2)` (the root's cluster `{x}` with poles `(x, x, x)`); a **refinement** of a cluster `K` with poles `p_k` takes the excuses `u_k = Excuse_k(p_k)`, the clusters of the 1-predecessors of `K`, one representative fork between each pair of these clusters that a fork joins, and the minimal tree of clusters and forks connecting the clusters of `u_0, u_1, u_2`; each cluster of that tree receives the poles `u_k` it contains and, for the other charges, the endpoint of the fork toward the cluster of `u_k`; the forks of the tree become tree edges. A pole is **kept** if it is incident to an existing tree edge or is a bad amplified pole for its charge (the first pole if none is); a kept processed-type pole `v` with charge `k` gets the **excuse arrow** `{v, u_k}`, a kept amplified pole the **amplification arrow** to its single 1-predecessor. Seeds are singleton clusters and end the recursion.
- **The potential and the log.** `Span(K) = Σ_k M_k(p_k)`; `Φ = Σ_{unprocessed clusters} Span + #forks`, `Φ = 0` at the start. The construction's **log** records, at each refinement, `(b, kept, a, e, f, r, d)`: bad pairs, kept poles, amplified and processed-type kept poles, forks created, the rise `r = 1 − b + Σ_{forks created}(1 − Span(fork))` of `Φ`, and the number of distinct poles.
- **The budgets.** `F = #forks`, `E = Σ e`, `|A| = Σ a` over the refinements; block 30's budget is `E ≤ 3(|S| − 1) + 2|A|`; the **sharper budget** is `E ≤ 3(|S| − 1) + |A|`; the **ratio** of a tree with `|A| ≥ 1` is `(E − 3(|S| − 1))/|A|`.
- **The witnesses.** `W1`: window `[0,4)²×[0,7)`, root `(3, 3, 4)`, marks `(0,0,0), (0,0,1), (0,1,0), (1,0,0), (1,0,2), (1,2,0), (1,3,1), (2,0,0), (2,2,3), (2,3,4), (3,0,2)`. `W2`: the same window, root `(3, 3, 6)`, the forty marks listed in the runner. `W3`: window `[0,5)²×[0,9)`, root `(4, 4, 5)`, the seventy-four marks listed in the runner.
- **The recursion of block 25 and the stake's weights.** `D = (1 + xU)²(1 + 3xD)(1 + yF)⁶`, `U = (1 + xU)³(1 + yF)⁶`, `F = (1 + xU)³(1 + 3xD)(1 + yF)⁵`, `R = (1 + xU)³(1 + 3xD)(1 + yF)⁶`; under a budget `E ≤ 3(|S| − 1) + c|A|` the amplification weight in block 30's count is `ε₂/t^c`, so `x = t + ε₂/t^c`, `y = ε₁/t³`; a **super-solution** at `(x, y)` is a rational triple `≥ 1` dominating its own right sides; `ε₁ = d_1`, `ε₂ = max(d_2, d_3)` with block 30's closed forms.

## Prior art and what is new

Block 30 (PR #8174) built the extended explanation tree on top of block 25's level-time carrying of Toom's stability theorem (in the Berman–Simon route as exposed by Gács), proved `E ≤ 3(|S| − 1) + 2|A|`, measured `2/3` on its executed trees and named the sharper budget as its first open item. What is new: (i) the sharper budget is refuted by explicit witnesses found by a hill-climb rather than by uniform sampling (T2); (ii) the mechanism — the two-level period of the potential's accounting with ratio exactly `2` (T1) — which identifies block 30's constant as the value of this accounting rather than its slack; (iii) the stake of the refuted route recorded exactly and not claimed (T3); (iv) the identification of the executed `2/3` as a sampling artefact, with the blind spot quantified.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T1 | the accounting identities; the two-level period has ratio `2` | block 30's spanning identity; the log | B |
| T2 | the sharper budget fails: three witnesses, ratio `8/5`, `5/3`, `5/3`; `c ≥ 5/3`; the blind spot | exhibition; the construction re-executed; uniform sampling | C |
| T3 | the stake: certificates under the false budget; the ceiling `4/729` | exact super-solutions; a one-variable maximum | D |

## Theorem T1 — the accounting identities and the two-level period

**T1.1 (increments).** For an amplified `v` with direction `j`, `M_k(v − e_j) − M_k(v) = 1/3 − δ_{jk}`; for a processed-type `v`, `M_k(Excuse_k(v)) − M_k(v) = 1/3`. *Proof.* `τ` drops by one along either arrow; the coordinate `k` drops by one exactly when the arrow's direction is `k`. ∎

**T1.2 (the rise).** At a refinement of `K` with `b` bad pairs, `Σ_{clusters of the tree} Span + Σ_{forks of the tree} Span(fork) = Span(K) + 1 − b` (block 30's spanning identity, restated: each pole's charge either travels to its excuse, gaining `1/3` or losing `2/3`, or is carried across the forks with the fork endpoints' charges telescoping); hence `Φ` rises by `r = 1 − b + Σ_{forks created}(1 − Span(fork))`, which is `1 − b` at a fork-free refinement and at most `1 − b + f` otherwise. Since `Φ = 0` at the start and `Φ = #forks` at the end (seeds are singleton clusters with `Span = 0`), `Σ_i r_i = F`. Trivially `Σ_i e_i = E`, `Σ_i a_i = |A|`, `b_i ≤ a_i` (a bad pole is amplified and kept) and `e_i + a_i ≤ 3`. Executed on the three witnesses' logs (B2).

**T1.3 (the two-level period).** A fork-free refinement keeping three processed-type poles has `b = 0`, `r = 1`, `e = 3`, `a = 0`; a fork-free refinement keeping two bad amplified poles and one processed-type pole has `b = 2`, `r = −1`, `e = 1`, `a = 2`. Their sum has `r = 0`, `e = 4`, `a = 2`: the pair leaves the potential where it was and spends four excuse arrows on two amplified nodes, `(e − 3r)/a = 2`. *Proof.* T1.2 with `f = 0`. ∎ Each of the three witnesses realises the pair as consecutive refinements of its log (B3: `4` occurrences; W1 twice, W2 twice). Whether the pair can be repeated an arbitrary number of times is not proved here; the witnesses contain two periods each.

*Remark (what a per-refinement proof would need).* Per refinement, `e ≤ 3r + 2a` always (block 30's proof), with equality at `(b, a, e) = (1, 1, 2)`, `(2, 2, 1)`, `(3, 3, 0)`; the sharper inequality `e ≤ 3r + a` fails at each of these, and each occurs in W1 (C3). So no per-refinement argument can give a constant below `2`, and T2 shows that no global compensation rescues `1`.

## Theorem T2 — the witnesses

**T2.1.** Run the automaton from the marks of W1 in its window. The root `(3, 3, 4)` is `1`; the construction returns a tree with `27` nodes, `E = 16`, `|A| = 10`, `|S| = 1`, no fork, `10` refinements and `10` bad pairs; every excuse arrow joins a processed-type node to one of its 1-predecessors, every amplification arrow joins an amplified node to its single 1-predecessor, the seed has no 1-predecessor, and the point graph is a tree through 1-sites containing the root. Block 30's budget reads `16 ≤ 20`; the sharper budget reads `16 ≤ 10` and is false. The eleven marks are exactly the tree's seed and its ten amplified nodes, so W1 is self-contained (C1, C5).

**T2.2.** W2 gives `E = 20`, `|A| = 12`, `|S| = 1`, no fork (`20 ≤ 24` against `20 ≤ 12`), and W3 gives `E = 23`, `|A| = 12`, `|S| = 2`, one fork (`23 ≤ 27` against `23 ≤ 15`) (C2). Hence any constant `c` with `E ≤ 3(|S| − 1) + c|A|` on every tree of this construction satisfies `c ≥ 5/3`; the sharper budget, `c = 1`, is false. ∎

**T2.3 (the blind spot).** On `300` uniformly random cones of depth `3` to `8` at four noise densities the construction never exceeds the ratio `1` (worst `1/2` in the runner; `1` on `40 000` cones in the controls), while W1 reaches `8/5` (C4). Block 30's executed maximum `2/3` measured the sampling, not the construction. The witnesses were found by a hill-climb on the ratio (`specs/supervisor_control_block31_climb.py`), which reaches `5/3` from random starts within four minutes in both windows.

*Reading of the witnesses.* W1's log is `(0,1,0,1)`, `(1,2,1,1)`, `(0,2,0,2)`, `(1,3,1,2)`, `(0,3,0,3)`, `(2,3,2,1)`, `(0,3,0,3)`, `(2,3,2,1)`, `(1,3,1,2)`, `(3,3,3,0)` in `(b, kept, a, e)`: the root's single arrow, a bad pole appearing beside it, the width growing to three poles, then two periods of T1.3, and the bottom refinement with three bad poles all pointing at the seed. The three-pole width is sustained because the two amplification arrows of a two-bad refinement land on processed-type sites that are kept at the next level, and that level's three excuse arrows land on two amplified sites and one processed-type site — the excuse rule (the smaller index of the winning pair) and the one-sided rule's forced ones cooperate to keep three distinct poles incident without any fork.

## Theorem T3 — the stake of the refuted budget

Had the sharper budget held, block 30's count would read `P(η'_x = 1) ≤ ε₁ R(t + ε₂/t, ε₁/t³)`, and the region would need `t + ε₂/t < 4/27`, i.e. `ε₂ < max_t t(4/27 − t) = 4/729` (at `t = 2/27`), which on `(p, 1, 2)` is crossed between `p = 367` and `368`. The rational triples of the runner are exact super-solutions at `(453, 1, 2)` with `t = 77/1000`, `(232, 1, 1)` with `19/250`, `(905, 2, 4)` with `39/500`, `(677, 1, 3)` with `77/1000`, each with `ε₁ R̄ < 10⁻⁵` (D1–D2): a factor between `8` and `10` below block 30's `4165`, `2085`, `8330`, `6247` (D3). By T2 the premise is false and none of this is a region; it is recorded so that the item's value and the ceiling it was aiming at are on the record. Block 30's ceiling `ε₂ < 256/531441` stands.

## No-Go Discipline Gate

This note's sentence is negative — a route is pruned — and the gate applies in full.

### N1 — Routes by which the negative sentence could fail, and the routes beyond it
1. *The witnesses invalid* — closed: rebuilt from their marks through the one-sided rule, every arrow checked against the 1-predecessors, the tree checked (C1–C2); the refuting pass repeats the checks with a separate implementation.
2. *The construction implemented differently from block 30's* — the runner embeds block 30's control core with a per-refinement log added; the refuting pass re-derives the witnesses' counts from the edge lists alone.
3. *A differently built tree* — not covered: a construction with another pole or excuse rule may satisfy a smaller constant; the witnesses' configurations are the test cases it must pass (N7).
4. *The sharper budget rescued by a global compensation* — closed by T2 (the ratio `5/3` is global).
5. *The constant `2` attained* — not claimed: the period gives `2` per period, but chains of arbitrary length are not constructed; the executed maximum is `5/3` (windows `4×4×7` and `5×5×9`, four minutes of hill-climb each).
6. *The stake's certificates* — exact (D1); conditional on the false budget; not a region.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
No hidden dependence: the inputs are the axioms' sentences, block 01's rule, and block 30's automaton and construction as declared and re-executed.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the four sentences under Premises | yes (premise) |
| block 01 (`main`) | the rule and its one-site conditional | yes (premise, proposed) |
| block 30 (open PR #8174) | the automaton, the construction, the budget, the open item; re-executed here | yes (the object of the refutation; construction embedded) |
| block 25 (open PR #8168) | the recursion used in T3 | the stake only |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the sharper bad-pair budget is false for block 30's extended explanation tree" | executed: the increments of an amplified excuse; the rise identity at every refinement of the witnesses; the period's arithmetic | executed: the witnesses rebuilt from their marks through the one-sided automaton; every arrow against the 1-predecessors; the ceiling's crossing at `367`/`368` | executed: the trees' counts; the sharper budget failing by `6`, `8`, `8` and block 30's holding; `300` random cones never above `1` | executed: the four certificates of the stake; the maximum `4/729` symbolically | a statement about block 30's construction for any weights; the constant's attainment, other constructions and the true strength not claimed |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling or order; none is a wall.

### N7 — Steelman
Hostile reviewer: "You refuted a budget for one implementation of one tree; the idea of a sharper accounting is untouched." Reply: the constant is shown to be the value of this accounting's period, not an artefact of one implementation — the period uses only the spanning identity and the one-arrow-per-kept-pole rule; a different construction must change one of those, and the three witnesses are the configurations on which it will be judged. Conceded: no theorem says every extended tree of these configurations has ratio above `1`; the negative sentence is about block 30's construction.

### N8 — Cross-cycle echo
Block 25's sharpening refuted its own candidate lemma (arrows point down) by search; block 30 named this item on executed evidence that this note shows to be a sampling artefact; the lesson of block 04 (sup-of-sums) and block 07 (no iff without a witness search) recurs: an executed maximum on random inputs is not evidence about a worst case.

## Falsifiers
- An increment of an amplified excuse other than `1/3 − δ_{jk}`; a refinement of the witnesses whose rise is not `1 − b` when fork-free or exceeds `1 − b + f`; rises not summing to the number of forks; `e`, `a`, `b` not summing to `E`, `|A|` and the bad count; `b > a` or `e + a > 3` somewhere; the period's pair with a sum other than `(r, e, a) = (0, 4, 2)` or absent from the logs (B1–B3).
- W1 failing to rebuild to a valid tree with `(E, |A|, |S|, F) = (16, 10, 1, 0)`; W2 or W3 not at ratio `5/3` or outside block 30's budget; W1 without the two local patterns; a random cone above ratio `1`; W1's or W2's bad count differing from `|A|` (C1–C5).
- A super-solution inequality failing at one of the four points of the stake; `t(4/27 − t)` exceeding `4/729`; the crossing not between `367` and `368`; a line's factor outside `(8, 10)` (D1–D3).

## Boundaries and non-claims
This note proves that block 30's extended explanation tree does not satisfy the sharper bad-pair budget `E ≤ 3(|S| − 1) + |A|`: three explicit configurations of the two-level noisy majority automaton, re-executed from their noise marks, have valid trees with `(E − 3(|S| − 1))/|A| = 8/5`, `5/3` and `5/3` inside block 30's budget `E ≤ 3(|S| − 1) + 2|A|`, and the two-level period of the potential's accounting has ratio exactly `2`; it does not prove that the constant `2` is attained, does not lower block 30's ceiling, does not treat other tree constructions, other menus or orders, does not select a reading, rule or coupling as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 01 (on `main`): the rule and its conditional; proposed, unaudited. Block 30 (PR #8174, open) is the object refuted: its automaton and construction are restated as declared objects and re-executed by the embedded core; block 25 (PR #8168, open) supplies the recursion used for the stake. Both referenced as evidence addresses.
- Named standard imports at definition level (never as authority for physics): none beyond finite arithmetic and the union bound implicit in block 30's count (used only in T3, the stake).
- Reference only (named, not used): Toom (1980); Berman–Simon (1988); Gács (2021).

## Review record
Supervisor-run block (owner directive 2026-09-16, evening: "try the sharper bad-pair budget next"). The attempt began as a proof search: the per-refinement accounting was shown to reach equality at `(1, 1, 2)`, `(2, 2, 1)`, `(3, 3, 0)` and `40 000` uniformly random trees never exceeded the ratio `1` (`specs/supervisor_control_block31_search.py`), which suggested a global compensation; a hand analysis of chains with three kept poles produced a candidate family that the construction collapsed to ratio `1` (the one-arrow-per-kept-pole rule leaves the second wall unkept); a hill-climb on the ratio (`..._climb.py`) then found `5/3` in both windows within minutes, and the witnesses' logs exposed the period. The witnesses were verified (`..._witness.py`), W1 reduced to its own marks, and the stake's certificates computed (`..._certify.py`) before the note was written. The refuting pass (`CHECKER_block31_findings.md`, `..._refuter.py`) rebuilds the witnesses' trees from the edge lists with an independent implementation, enumerates the per-refinement accounting to confirm that `2` is its maximum and where `1` fails, and re-runs the majority rule with a separate array implementation. Block 30's N1 item 5 and its "executed `2/3`" are superseded by this note; its theorems are untouched.

## Verification

```bash
python3 scripts/admissibility_rule_six_axis_formation_threshold_sharper_bad_pair_budget_false_explicit_witnesses_and_the_two_level_period_2026_09_16.py
python3 scripts/admissibility_rule_six_axis_formation_threshold_sharper_bad_pair_budget_false_explicit_witnesses_and_the_two_level_period_2026_09_16.py --list-mutations
python3 scripts/admissibility_rule_six_axis_formation_threshold_sharper_bad_pair_budget_false_explicit_witnesses_and_the_two_level_period_2026_09_16.py --mutation sharper_budget_asserted
```

Families: A authority and inputs; B the identities and the period; C the witnesses and the blind spot; D the stake; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 9 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=20 FAIL=0`.
