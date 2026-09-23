---
claim_id: admissibility_rule_six_axis_formation_threshold_the_rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_and_the_one_processed_child_count_bounded_theorem_note_2026-09-17
claim_type: bounded_theorem
claim_scope: "For the two-level noisy majority automaton of block 30 (PR #8174) in level time on Z^3 and the counted family of marked explanation trees of block 32 (PR #8176), with the rooted value v(z) := min over trees of the family containing z with all nodes at levels <= level(z) of E - 3(|S| - 1) - |A|: (T1) the extension lemma v(z) <= 1 + v(u) for every 1-predecessor u of a non-seed site z, and v(z) <= -1 + v(u) at an amplified site; the seed lemma: a processed site with a seed 1-predecessor s and another 1-predecessor w has v(z) <= v(p) - 1 <= -1 for any 1-predecessor p of w (the fork s-w placed below the seed's level cannot meet the tree rooted at p), and two seed 1-predecessors give v(z) <= -2; hence, if v <= 0 at processed and v <= -1 at amplified sites below a level, the same holds at that level at every site except a processed one all of whose 1-predecessors are tight processed sites (v = 0) — the tight-sibling case (proved; the instances verified by an exact brute-force enumeration of rooted trees on tiny realizations, where the rooted inequality itself holds at all 788 sites and the tight-sibling case never arises); the unit budget E <= 3(|S| - 1) + |A| for every realization (block 32's conjecture c* = 1, worth p >= 453 at (p, 1, 2)) is therefore equivalent to the tight-sibling lemma: a processed site all of whose 1-predecessors are tight has a rooted tree of cost at most zero (reduction proved; the lemma open); (T2) on block 32's extremal realizations the tight roots have three processed 1-predecessors of rooted value -1 (exact single-seed program with a level cap), so they are not tight-sibling cases; in about 10^4 realizations of the climbs no processed site has all its predecessors tight and no site violates the rooted inequality (executed); (T3) the count restricted to trees in which every node has at most one processed child: the up-factor (1 + xU)^n becomes (1 + x_A U)^n + n x_P U (1 + x_A U)^(n-1) (symbolic identity), the same code with the full up-factor is block 25's recursion and passes block 30's certificate, and exact rational super-solutions exist at (2921, 1, 2), (1464, 1, 1), (5841, 2, 4), (4380, 1, 3) with c = 2 and at (405, 1, 2), (208, 1, 1), (810, 2, 4), (605, 1, 3) with c = 1 (proved as certificates); (T4) the restriction's admissibility — that some tree with the budget has at most one processed child per node — holds on 60 tiny realizations by brute force and on 125 realizations by the integer program at c = 1, but at c = 2 one realization (block 31's W3) has a restricted minimum one unit above the unrestricted one, so the restriction is not cost-free in general and neither restricted region is claimed (executed). Not claimed: the tight-sibling lemma; any region below block 30's; other counts, menus or orders. No reading, rule or coupling is selected as physical; exact arithmetic throughout the runner."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_six_axis_formation_threshold_rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_and_the_one_processed_child_count_2026_09_17.py
---

# The rooted inequality reduces the unit budget to the tight-sibling lemma, and the one-processed-child count: exact certificates at `p ≥ 2921` (c = 2) and `p ≥ 405` (c = 1), neither claimed

**Date:** 2026-09-17
**Type:** bounded_theorem
**Status:** bounded-support (exact; a reduction with its proved cases and its one open lemma; two conditional regions with exact certificates, not claimed; unaudited)

## Result up front

Block 32 showed that the counted family's constant is at least one and
conjectured, on about `10⁴` realizations, that it is exactly one: every
realization would then have a tree with `E ≤ 3(|S| − 1) + |A|`, and the
ordered region would move from `p ≥ 4165` to `p ≥ 453` at `(p, 1, 2)`. The
existence of such a tree is all the count needs; no explicit rule is
required. This note attacks the existence by induction on levels through the
*rooted value* `v(z)`, the cheapest tree containing `z` that stays at or
below `z`'s level.

Three things are proved. Any 1-predecessor extends: `v(z) ≤ 1 + v(u)`, and
an amplified site has `v(z) ≤ −1 + v(u)`. A seed predecessor closes: a
processed site with a seed 1-predecessor `s` and another 1-predecessor `w`
has `v(z) ≤ v(p) − 1` for any 1-predecessor `p` of `w`, because the fork
`s—w` can be placed above a tree rooted at `p`, which lives strictly below
the seed's level and so cannot meet it; two seed predecessors give `−2`.
Consequently, if the inequality `v ≤ 0` (processed), `v ≤ −1` (amplified)
holds below a level, it holds at that level at every site but one kind: a
processed site all of whose 1-predecessors are *tight* — processed with
`v = 0`. The unit budget is therefore equivalent to a single lemma: such a
site has a rooted tree of cost at most zero. The lemma is open. It is
supported by everything executed: the inequality holds at all `788` sites of
`140` tiny realizations enumerated exactly and at every site of about
`10⁴` realizations of the climbs, the tight-sibling case never arises, and on
the extremal realizations the tight roots have all three 1-predecessors at
`−1`.

Two more things are computed exactly. In the optimal trees of block 32 a
node never has two processed children. The count restricted to such trees
replaces the up-factor `(1 + xU)^n` by `(1 + x_A U)^n + n x_P U (1 + x_A U)^{n−1}`,
the same code with the full factor is block 25's recursion and passes block
30's certificate, and the restricted recursion has exact super-solutions at
`p ≥ 2921` on `(p, 1, 2)` with the proved budget `c = 2` and at `p ≥ 405`
with `c = 1`. Neither is claimed: the restriction is admissible on every tiny
realization and on `125` realizations at `c = 1`, but at `c = 2` block 31's
`W3` has a restricted minimum one unit above the unrestricted one, so a
proof of admissibility would have to be an existence argument, not an
exchange on minimal trees.

In plain words: to prove that the cheapest family tree always fits the
one-per-dissent budget, we tried to build it level by level from the ground
up. Every step works except one — when a site's supports are all exactly at
the break-even point — and we have never seen that step occur. We also found
that the cheapest trees never branch twice through ordinary sites, which
would shave the proved bound by a third if it could be guaranteed; it cannot
yet, since one configuration shows the shaving is not always free.

Exactly: the lemmas and the reduction (T1); the extremal realizations (T2);
the restricted count (T3); its admissibility (T4). Executed with exact
arithmetic: 18 checks, 7 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "block 32's queue: a construction attaining c = 1 with a proof (would give p >= 453 at (p, 1, 2)); a count of the family that is not a union bound over sub-structures"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the unit budget reduced to the tight-sibling lemma (the extension and seed lemmas proved; the induction closes everywhere else); the one-processed-child count with exact certificates (2921 at c = 2, 405 at c = 1), conditional on an admissibility that is not always cost-free. Next: the tight-sibling lemma (a local statement about the automaton's marks around a site whose supports are all tight), or an existence argument for the restricted trees; the exact programs are the oracles. Consumers: the campaign's decision record; block 32's open items"
conditional_surface_status: "T1 proved (extension and seed lemmas; the reduction) and executed as instances; T2 exact on the extremal realizations, executed on the climbs; T3 exact certificates; T4 executed with a counter-case at c = 2; the regions p >= 2921 and p >= 405 conditional on unproved statements and not claimed; conditional on the records-only reading, positivity, the six-axis menu and the monotone order as supplied conditions for the automaton's meaning; the standard mathematical imports named at definition level"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", "Records form.", and "Only records are readable.". Block 01 (`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`, on `main`) supplies the rule and its one-site conditional given a recorded set; the level automaton, the counted family, its recursion and the extremal realizations are the objects of blocks 25, 30, 31 and 32 (PRs #8168, #8174, #8175, #8176, open hand-offs referenced as evidence addresses), restated here as declared objects and re-executed by the runner. All proposed and unaudited.

Declared objects.
- **Level time, the one-sided automaton, the family, the cost.** As in block 32: sites `x ∈ Z³`, level `τ(x)`, predecessors `x − e_j`, siblings `x ± (e_i − e_j)`; a realization `η` is the output of the one-sided two-level majority rule from a finite set of marks; seeds, amplified and processed-type sites by their number of 1-predecessors (`0`, `1`, `≥ 2`); a marked tree of the family is a subtree of `G` through 1-sites with exactly one downward arrow at every non-seed node (to a 1-predecessor; an amplified node to its single one), forks between siblings, `F = |S| − 1`; `cost(T) = E − 3(|S| − 1) − |A|` (the unit budget's parameter `c = 1`). A **child** of a node `u` in `T` is a node whose arrow points to `u`.
- **The rooted value.** `v(z) := min cost(T)` over trees of the family containing `z` all of whose nodes have level `≤ τ(z)`. A processed site is **tight** if `v(z) = 0`. For a seed `s`, `v(s) ≤ 0` (`{s}` alone).
- **The rooted inequality (H).** `v(z) ≤ 0` at every processed site and `v(z) ≤ −1` at every amplified site. Since the unrooted minimum is at most the rooted one, (H) implies block 32's conjecture `c* ≤ 1`, i.e. the unit budget at every realization.
- **The restricted family and its recursion.** Trees of the family in which every node has at most one processed child. With `x_P = t`, `x_A = ε₂/t^c`, `x = x_P + x_A`, `y = ε₁/t³` and `U_n := (1 + x_A U)^n + n x_P U (1 + x_A U)^{n−1}`: `D = U_2 (1 + 3xD)(1 + yF)⁶`, `U = U_3 (1 + yF)⁶`, `F = U_3 (1 + 3xD)(1 + yF)⁵`, `R = U_3 (1 + 3xD)(1 + yF)⁶`; with `U_n := (1 + xU)^n` this is block 25's recursion (T3.2). A super-solution is a rational triple `≥ 1` dominating its right sides; the bound is `ε₁ R̄`.
- **The realizations.** `Z_A`, `Z_B` (block 32); `W3` (block 31), restated in the runner and the controls.

## Prior art and what is new

Blocks 25, 30, 31 and 32 (PRs #8168, #8174, #8175, #8176) carried Toom's stability theorem into level time with explicit thresholds, the two-level domination, and the family-level constant. What is new: (i) the rooted value and its two lemmas, in particular the fork-below trick of the seed lemma, which closes every inductive case but one (T1); (ii) the exact reduction of the unit budget to the tight-sibling lemma, with the case's non-occurrence executed (T1–T2); (iii) the observation that optimal trees never branch twice through processed nodes, the restricted recursion with its up-factor identity, and exact certificates a third below block 30 at the proved budget (T3); (iv) the admissibility question posed exactly, with its counter-case (T4).

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T1 | the extension and seed lemmas; the reduction to the tight-sibling lemma; (H) executed | rooted trees; the fork below the seed's level; exact brute force | B |
| T2 | the extremal realizations: tight roots with predecessors at `−1` | the single-seed program with a level cap | C |
| T3 | the restricted recursion and its certificates | the up-factor identity; super-solutions | D |
| T4 | admissibility of the restriction, executed; the counter-case | brute force; the integer program (controls) | E |

## Theorem T1 — the lemmas and the reduction

**T1.1 (extension).** For a non-seed site `z` and any 1-predecessor `u`: `v(z) ≤ 1 + v(u)`, and `v(z) ≤ −1 + v(u)` if `z` is amplified. *Proof.* Take a rooted tree `T` of `u` with `cost(T) = v(u)`; all its nodes lie at levels `≤ τ(u) < τ(z)`, so `z ∉ T`, and `T ∪ {z}` with the arrow `z → u` is a tree of the family rooted at `z` (for an amplified `z`, `u` is its single 1-predecessor); its cost is `cost(T) + 1` or `cost(T) − 1`. ∎

**T1.2 (seed lemma).** Let `z` be processed with a seed 1-predecessor `s` and another 1-predecessor `w`. If `w` is processed, then for any 1-predecessor `p` of `w`: `v(z) ≤ v(p) − 1 ≤ −1` given (H) at `p`; if `w` is amplified with predecessor `q`: `v(z) ≤ v(q) − 3`. If `z` has two seed 1-predecessors `s, s'`: `v(z) ≤ −2`. *Proof.* Take a rooted tree `T_p` of `p` of cost `v(p)`; its nodes lie at levels `≤ τ(p) = τ(z) − 2`, so `s, w, z ∉ T_p`. Then `T := T_p ∪ {w, s, z}` with arrows `z → w`, `w → p` and the fork `s—w` (siblings, both predecessors of `z`) is a tree of the family: `s` is its own arborescence, `w` joins `p`'s, the fork joins the two, and `F = |S| − 1` is preserved. Its cost is `v(p) + 1 + 1 − 3`. For amplified `w` the same with `w → q` gives `v(q) − 1 + 1 − 3`. For two seeds, `{z, s, s'}` with `z → s` and the fork `s—s'` costs `1 − 3`. ∎

**T1.3 (the inductive step and the reduction).** Assume (H) at all sites below level `ℓ`, and let `z` be a non-seed site at level `ℓ`. If `z` is amplified, `v(z) ≤ −1` by T1.1. If `z` is processed: with an amplified 1-predecessor `u`, `v(z) ≤ 1 + v(u) ≤ 0`; with a seed 1-predecessor, `v(z) ≤ −1` by T1.2; with a processed 1-predecessor `w` of `v(w) ≤ −1`, `v(z) ≤ 0` by T1.1. The only case left is a processed `z` whose 1-predecessors are all processed with `v = 0` — the **tight-sibling case**. Hence (H), and with it the unit budget at every realization and the region `p ≥ 453` of block 31's certificates, is equivalent to:

> **Tight-sibling lemma (open).** A processed site all of whose 1-predecessors are tight processed sites has a rooted tree of cost at most zero.

Executed (B1–B3): on `140` tiny realizations with every rooted tree enumerated exactly, the extension inequalities hold at `357` predecessor pairs and `121` amplified sites, the seed lemma's instances at `15` single-seed and `78` double-seed cases, (H) at all `788` sites, and the tight-sibling case does not arise.

*Remark (what the lemma is about).* In a component with one seed, forks are unavailable and `v(z) = 1 + min` over closed sets `N` below `z` (containing a 1-predecessor of `z`, with the sites at `z`'s level other than `z` allowed as tops) of their cost; a tight `w` has an optimal set that is *saturated* — every amplified site whose predecessor lies in it is already in it — so the lemma asks whether, around a site whose supports are all saturated, some amplified site at the site's own level hangs off a support. That is a statement about the marks near `z`, not about trees far away.

## Theorem T2 — the extremal realizations

On `Z_A` the root `(3, 3, 3)` has rooted value `0` and its three 1-predecessors, all processed, have rooted values `−1, −1, −1` (exact single-seed program with a level cap; C1). On `Z_B` the root `(4, 4, 4)` has value `0` with predecessors at `−1, −1, 0`, and the tight predecessor `(4, 4, 3)` has its own three predecessors at `−1, −1, −1` (C2). So the tight sites of the extremal realizations are supported by non-tight sites and the induction passes through them. Executed in the controls: the climbs on the family's value (block 32, about `10⁴` realizations), four seeded climbs on the rooted and unrooted minima from `Z_A` and `Z_B` (`specs/supervisor_control_block33_violate.py`), and three climbs maximizing `min(v(w₁), v(w₂))` over sibling processed predecessors of a processed site (`..._tightpairs.py`) never find a violation of (H) nor two tight siblings (the largest minimum found from random starts is `−2`; on `Z_A` it is `−1`).

## Theorem T3 — the one-processed-child count

**T3.1 (the up-factor).** For `n` successor positions each empty, processed (weight `x_P U`) or amplified (weight `x_A U`), the sum over configurations with at most one processed child is `(1 + x_A U)^n + n x_P U (1 + x_A U)^{n−1}` (D1, symbolic for `n = 2, 3`).

**T3.2 (the recursion).** Replacing `(1 + xU)^n` by this factor in block 25's recursion counts the trees of the family in which every node has at most one processed child, with the same weights; with the full factor the code is block 25's recursion and block 30's certificate passes it (D3). The kind-typed count (processed, amplified, seed nodes with entries by down-step, up-step and fork) reduces to this three-variable form because the two up-kinds satisfy the same equation and the kind split of the other variables is fixed by their images (`specs/supervisor_control_block33_restricted_count.py`, which reproduces `4165, 2085` at `c = 2` and `453, 232` at `c = 1` on the unrestricted count).

**T3.3 (certificates).** Exact rational super-solutions of the restricted recursion exist at `(2921, 1, 2)`, `(1464, 1, 1)`, `(5841, 2, 4)`, `(4380, 1, 3)` with `c = 2`, and at `(405, 1, 2)`, `(208, 1, 1)`, `(810, 2, 4)`, `(605, 1, 3)` with `c = 1`, each with `ε₁ R̄ < 10⁻⁵` (D2). Were the restriction admissible, the ordered phase would follow at these couplings with block 30's proved budget — a factor `1.43` below block 30 on every line — and at `405` with the unit budget. Neither is claimed (T4).

## Theorem T4 — admissibility of the restriction (executed)

The restriction is admissible at a realization if some tree with the budget has at most one processed child per node. On `60` tiny realizations at `c = 1` and `c = 2`, whenever a tree with the budget exists a restricted one does too (E1: `120` cases; the restricted and unrestricted minima coincide in most and differ in a few). On the `125` realizations of block 32's shape survey (`specs/supervisor_control_block33_shape.py`, `..._shape2.py`) the minima coincide at `c = 1` in every case; at `c = 2` the restricted minimum of block 31's `W3` is `−61` against `−62` — still within the budget, but one unit worse. So the restriction is not cost-free on minimal trees, an exchange argument cannot prove it, and its admissibility (restricted minimum `≤ 0` whenever the unrestricted one is) remains an open existence statement. The optimal trees' shape statistics: a processed node's children are `()`, `(amp)`, `(proc)`, rarely `(amp, amp)` or `(amp, proc)`, never `(proc, proc)`; non-seed nodes never have three children; seeds do. The restriction "at most two children at non-seed nodes" adds almost nothing to the count (`2887` against `2921`).

## No-Go Discipline Gate

The note's sentences are a reduction and two conditional regions; the gate applies to the negative part (the counter-case to cost-free admissibility) and to the scope of the conditionals.

### N1 — Routes by which the sentences could fail, and the routes beyond them
1. *The lemmas false* — the proofs are three lines each and the instances are verified exactly (B1–B2); the fork-below trick needs only that a rooted tree of `p` lies below `τ(p)`.
2. *The reduction incomplete* — T1.3 lists the cases by the kinds and values of the 1-predecessors; the case analysis is exhaustive.
3. *The tight-sibling lemma false* — then (H) fails and `c* > 1`; the climbs (block 32's and this block's) never produce it; not excluded.
4. *The restricted certificates wrong* — exact (D2); block 30's certificate under the same code (D3).
5. *The restriction admissible after all* — open; the counter-case only shows it is not cost-free on minimal trees.
6. *A different route below `p = 368`* — outside this note (block 32's floor).

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
No hidden dependence: the inputs are the axioms' sentences, block 01's rule, and blocks 25/30/31/32's objects as declared and re-executed.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the four sentences under Premises | yes (premise) |
| block 01 (`main`) | the rule and its one-site conditional | yes (premise, proposed) |
| block 25 (open PR #8168) | the recursion | yes (restated; T3) |
| block 30 (open PR #8174) | the automaton; the budget `c = 2`; the certificate at `4165` | yes (restated; D3) |
| block 31 (open PR #8175) | `W3`; the certificates at `c = 1` | data (T4); placement |
| block 32 (open PR #8176) | the family, its constant, the extremal realizations, the conjecture `c* = 1` | yes (restated; T2) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the unit budget is equivalent to the tight-sibling lemma; the one-processed-child count has exact certificates at `2921` and `405`" | executed: the lemmas' instances by exact rooted brute force; the up-factor identity | executed: (H) at every site of the tiny realizations; the tight roots and their predecessors | executed: the tight-sibling case absent; the restriction's admissibility on tiny realizations | executed: the eight certificates; block 30's under the same code | the lemmas hold for every realization; the open lemma and the admissibility are not claimed, so no region is claimed |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling or order; none is a wall.

### N7 — Steelman
Hostile reviewer: "A reduction to an unproved lemma and two regions you refuse to claim: what has been established?" Reply: the inductive structure is now exact — every case but one is a theorem, the remaining one is a local statement with an oracle, and the two regions are exact certificates waiting on a single existence statement each; the counter-case at `c = 2` is itself a finding, since it rules out the obvious proof. Conceded: no coupling moves today.

### N8 — Cross-cycle echo
Block 30's potential method could not see past the two-level period; block 32 moved the question to the family; this note moves it to a single site's neighbourhood. The fork-below trick is block 25's spanning-lemma fork used at the smallest scale.

## Falsifiers
- A tiny realization where `v(z) > 1 + v(u)` for a 1-predecessor, or `v(z) > −1 + v(u)` at an amplified site, or the seed lemma's bound fails, or (H) fails, or a processed site has all its 1-predecessors tight (B1–B3).
- A rooted value of a tight root other than `0`, or a 1-predecessor of it with value other than `−1` where stated (C1–C2).
- The up-factor identity failing symbolically; a super-solution inequality failing at one of the eight points; block 30's certificate failing the full-factor code (D1–D3).
- A tiny realization with a tree within the budget but none with at most one processed child per node (E1).

## Boundaries and non-claims
This note proves the extension and seed lemmas for the rooted value of the counted family, reduces the unit budget `E ≤ 3(|S| − 1) + |A|` (block 32's conjecture `c* = 1`, worth `p ≥ 453` at `(p, 1, 2)`) to one open lemma — a processed site all of whose 1-predecessors are tight processed sites has a rooted tree of cost at most zero — and gives, for the count restricted to trees with at most one processed child per node, exact super-solutions on the four lines at `c = 2` (`p ≥ 2921` at `(p, 1, 2)`) and `c = 1` (`p ≥ 405`); it does not prove the tight-sibling lemma, does not prove that the restriction is admissible (a realization is exhibited where it costs one unit), so neither restricted region is claimed, does not lower block 30's region, does not treat other counts, menus or orders, does not select a reading, rule or coupling as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 01 (on `main`): the rule and its conditional; proposed, unaudited. Blocks 25, 30, 31, 32 (PRs #8168, #8174, #8175, #8176, open) supply the recursion, the automaton and budget, the witnesses and certificates, the family and the extremal realizations; restated and re-executed; evidence addresses.
- Named standard imports at definition level (never as authority for physics): induction on levels; finite enumeration.
- Reference only (named, not used): Toom (1980); Berman–Simon (1988); Gács (2021).

## Review record
Supervisor-run block (continuing the owner's 2026-09-17 directive). The attempt at the `c = 1` construction was reframed as an existence proof by induction on levels; the rooted value was computed at every site of `63` realizations by the integer program with a level cap (`specs/supervisor_control_block33_rooted.py`: no site above `0`, no amplified site above `−1`), the hard cases were listed (`..._tight.py`: all with seed predecessors only), three candidate lemmas tabulated (`..._lemmas.py`), and the tight-sibling pairs and violations searched by climbs (`..._tightpairs.py`, `..._violate.py`). A greedy harvesting rule was scored and found far from the minimum (forks are essential), which is why the proof is by existence. The shape of optimal trees (`..._shape.py`, `..._shape2.py`) led to the restricted count: an eight-variable kind-typed recursion (`..._restricted_count.py`) reproduced blocks 30 and 31 exactly and was reduced to three variables; certificates were found by block 30's displacement method (`..._certify33.py`) after an eight-variable attempt failed on scaling (`..._kind_certs.py`, `..._diag.py`). Lens pass on the contract: the regions `2921` and `405` kept unclaimed; the counter-case `W3` reported with its size; the runner's forbidden phrases carried over from block 32. Refuting pass (`CHECKER_block33_findings.md`, `..._refuter.py`): the rooted values by the integer program against the exact program on the extremal realizations, the restricted count's fixed points by the eight-variable and three-variable iterations, and the seed lemma's construction re-checked on the tiny realizations with a separate tree verifier.

## Verification

```bash
python3 scripts/admissibility_rule_six_axis_formation_threshold_rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_and_the_one_processed_child_count_2026_09_17.py
python3 scripts/admissibility_rule_six_axis_formation_threshold_rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_and_the_one_processed_child_count_2026_09_17.py --list-mutations
python3 scripts/admissibility_rule_six_axis_formation_threshold_rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_and_the_one_processed_child_count_2026_09_17.py --mutation seed_lemma_wrong
```

Families: A authority and inputs; B the lemmas and the rooted inequality by exact brute force; C the extremal realizations; D the restricted count; E its admissibility on tiny realizations; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 7 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=18 FAIL=0`.
