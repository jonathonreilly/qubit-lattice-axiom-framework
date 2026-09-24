---
claim_id: admissibility_rule_six_axis_formation_threshold_the_unit_budget_is_false_one_seed_witness_with_family_constant_ten_ninths_tight_sibling_lemma_refuted_bounded_theorem_note_2026-09-20
claim_type: bounded_theorem
claim_scope: "For the one-sided two-level majority automaton in level time on Z^3 of block 30 (PR #8174) and the counted family of marked explanation trees of block 32 (PR #8176; budget E <= 3(|S| - 1) + c|A|): (T1) the realization from the ten marks {000, 001, 010, 100, 021, 102, 210, 113, 131, 311} has exactly 37 one-sites, all in [0,3]^3, one seed (000), nine amplified and 27 processed sites, invariant under the cyclic shift of the coordinates; (T2) at its top site 333 every tree of the family has E - |A| >= 1, the minimum of E - (10/9)|A| is 0, and the minimum of E - c|A| is positive for every c < 10/9, so the family constant at this realization is exactly 10/9 and the family constant c* of block 32 is at least 10/9; (T3) the three 1-predecessors of 333 are processed with rooted value 0, so the hypothesis of block 33's tight-sibling lemma (PR #8177) holds at 333 while its conclusion fails (the rooted value of 333 is 1), and block 33's hypothesis (H) fails at 333 and at no other site of this realization. CONSEQUENCES: block 32's conjecture c* = 1 is false; the unit-budget certificates of block 33 (405, and the stake 453 of block 31) are unavailable; block 30's proved count with c = 2 is untouched. EXECUTED, not claimed: an integer program gives the same constant; a local search over 705 neighbouring realizations found none with a larger constant. No upper bound on c* below 2 and no statement about the formation law's ordering threshold is made."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_six_axis_formation_threshold_unit_budget_false_one_seed_witness_family_constant_ten_ninths_2026_09_20.py
---

# The unit budget of the explanation-tree route is false: a one-seed realization whose family constant is `10/9`, and the tight-sibling lemma refuted

**Date:** 2026-09-20
**Type:** bounded_theorem
**Status:** bounded-support (an exact finite witness; a negative result about a conjecture and an open lemma of open PRs #8176 and #8177; unaudited)

## Result up front

Blocks 30 to 33 bound the probability that a site of the six-axis formation law is wrong by counting marked explanation trees whose excuse arrows are paid for by seeds and amplified nodes: `E ≤ 3(|S| − 1) + c|A|`. Block 30 proved the count with `c = 2`. Block 32 showed `c* ≥ 1` for the counted family and conjectured `c* = 1`; block 33 reduced `c* = 1` to one open statement, the tight-sibling lemma, and recorded the thresholds that `c = 1` would give. This note shows that `c = 1` is false.

1. **The witness (T1).** Ten marks in `[0,3]³` produce 37 one-sites with a single seed. The top site `333` is processed, and so are its three 1-predecessors.
2. **The unit budget fails there (T2).** Every tree of the family at `333` has `E − |A| ≥ 1`. The family constant at this realization is exactly `10/9`: a tree with `E = 10`, `|A| = 9` exists, and `E − c|A| > 0` for every `c < 10/9`. So `c* ≥ 10/9`.
3. **The lemma and its induction hypothesis fail (T3).** The three 1-predecessors of `333` are tight (rooted value `0`), so the lemma's hypothesis holds at `333`, and its conclusion does not: the rooted value of `333` is `1`. It is the only site of the realization where (H) fails.
4. **What this removes and what it leaves.** The conjecture `c* = 1`, the certificates at `p ≥ 405` and the stake `p ≥ 453` are gone. Block 30's theorem (`c = 2`, `p ≥ 4165` on `(p,1,2)`) stands. A different count, by refinement histories, was found by the probes and does not use the budget at all; it is not part of this note.

This note proves that the unit budget of the explanation-tree route is false: at the realization from ten marks in `[0,3]³` the family constant at the site `333` is exactly `10/9`, so block 32's conjecture `c* = 1`, block 33's tight-sibling lemma and its hypothesis (H) fail; it proves nothing about the formation law's ordering threshold itself.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "block 33 (PR #8177): 'the unit budget reduced to the tight-sibling lemma ... Next: the tight-sibling lemma'; block 32 (PR #8176): conjecture c* = 1"
source_of_blocker_text: handoff
reachability_to_target: refutes
artifact_role: no_go
next_trace_action: "the tight-sibling lemma, (H) and c* = 1 are false (explicit witness, constant 10/9); the explanation-tree route cannot reach the unit budget. Next: the refinement-history count (probes: p >= 84 on (p,1,2), refereed, not yet a block), which does not use the budget; an upper bound on c* below 2 is open and of little value now"
conditional_surface_status: "T1-T3 exact on one explicit realization, with the definitions of blocks 30, 32, 33 restated; no statement about the ordering threshold; the integer program and the local search are controls and not claims"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." and "Records form.". Block 01 (on `main`, proposed and unaudited) supplies the rule and the static law of a product rule. The objects below are those of blocks 25, 30, 32, 33 (PRs #8168, #8174, #8176, #8177, open), restated.

- **Level time.** Sites `x ∈ Z³`, level `τ(x) = x₁ + x₂ + x₃`, predecessors `x − e_j`, siblings `x ± (e_i − e_j)`.
- **Realization.** From a finite set of marks `ζ`: `η_x = 1` if at least two predecessors are `1`, and otherwise `η_x = 1` exactly when `x ∈ ζ` (the one-sided two-level majority automaton that dominates the law's errors, block 30).
- **Kinds.** A one-site is a **seed** with no 1-predecessor, **amplified** with exactly one, **processed** with two or three.
- **The counted family.** A marked tree at a one-site `x`: a subtree through one-sites containing `x`, in which every non-seed node has exactly one downward arrow to one of its 1-predecessors, seeds have none, and the other edges are forks between siblings. `E` counts the processed nodes (their excuse arrows), `|S|` the seeds, `|A|` the amplified nodes; the number of forks is `|S| − 1`. The budget at `c`: `E ≤ 3(|S| − 1) + c|A|`. The count of block 30 is valid at `c` exactly when every one-site of every realization has a tree within the budget; `c*` is the least such `c`.
- **Rooted value, tightness, (H).** `v(z)` = the minimum of `E − 3(|S| − 1) − |A|` over the trees containing `z` with all nodes at levels `≤ τ(z)`. A site is **tight** when `v = 0`. (H): `v(z) ≤ 0` at every one-site. **Tight-sibling lemma** (block 33, open there): a processed site all of whose 1-predecessors are tight processed sites has a rooted tree of cost at most zero.
- **One seed.** With a single seed there are no forks, and a tree of the family containing `x` is exactly a set of one-sites containing `x` and the seed in which every non-seed node has a 1-predecessor in the set: choosing one such predecessor per node gives the arrows, and following them strictly lowers the level until the seed. The cost `E − c|A|` is additive over nodes, so its minimum is computed exactly by a dynamic program over the subsets of each level.

The stability theorem whose proof technique these trees come from is due to Toom; the fractional program `min E/|A|` is solved in the control by the iteration of Dinkelbach. Neither is used as authority.

## Prior art and what is new

Block 31 (PR #8175) refuted a sharper bad-pair budget by hill-climbed witnesses and recorded the lesson that random sampling is not worst-case evidence. Blocks 32 and 33 then examined about `10⁴` hill-climbed realizations and structural searches and found `c* ≤ 1` everywhere; the probes' counterexample searches found nothing either. The witness here was built by hand by a probe worker (a Claude Opus worker on the `ai/probes` branch, problem `tight-sibling-vacuity`), found independently by a second worker, and is verified here by the supervisor's exact dynamic program of block 32 and, in the control, by block 32's integer program. What is new: the witness; the exact constant `10/9`; the failure of the lemma at a site whose predecessors are all tight, which block 33's induction could not reach. The lesson is sharpened: a climb from random starts is not worst-case evidence either.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T1 | the realization: 37 one-sites in `[0,3]³`, one seed, 9 amplified, 27 processed | the rule at every site; two boxes; the cyclic symmetry | B |
| T2 | `min(E − |A|) = 1` at `333`; `min(E − (10/9)|A|) = 0`; positive below `10/9` | exact dynamic program over level subsets; verified trees | C |
| T3 | the three predecessors tight; `v(333) = 1`; no other site violates (H) | the same program with the level cap | C |

## Theorem T1 — the realization

Let `M = {000, 001, 010, 100, 021, 102, 210, 113, 131, 311}` (sites written `x₁x₂x₃`). Start from the zero state below the marked levels. Every active site has a coordinatewise nondecreasing predecessor path from a mark, so no coordinate can become negative. Every one-site of the realization from `M` lies in `[0,3]³`: a one-site `z` of least level outside the box is unmarked, so it has two 1-predecessors, which lie in the box; then `z = u + e_i` has `z_i = 4`, and its other predecessor `z − e_j` also has `i`-th coordinate `4`, so it lies outside the box at a lower level and is `0`. The runner computes the realization in `[0,3]³` and in `[−2,6]³` (equal), checks the defining rule at every site of `[−1,4]³`, and finds 37 one-sites with level sizes `1, 3, 3, 4, 3, 6, 7, 6, 3, 1`: the seed `000`, the nine other marks amplified, 27 processed sites. The single site of level `9` is `333`; its 1-predecessors `233, 323, 332` are processed. Marks and one-set are invariant under `(a,b,c) → (c,a,b)`. ∎

## Theorem T2 — the unit budget fails at `333`; the constant is `10/9`

There is one seed, so `|S| = 1`, there are no forks, and the budget reads `E ≤ c|A|`. The dynamic program gives `min(E − |A|) = 1`, attained by a tree with `E = 6`, `|A| = 5`: no tree at `333` satisfies `E ≤ |A|`. At `c = 10/9` the minimum of `E − c|A|` is `0`, attained by a tree with `E = 10`, `|A| = 9`. For `c < 10/9` and any tree `T`: if `|A_T| ≥ 1` then `E_T − c|A_T| = (E_T − (10/9)|A_T|) + (10/9 − c)|A_T| > 0`, and if `|A_T| = 0` then `E_T − c|A_T| = E_T ≥ 1` because the root is processed. So the least `c` admitting a tree at `333` is exactly `10/9`, and `c* ≥ 10/9`. ∎

## Theorem T3 — the tight-sibling lemma and (H) fail

With the level cap, the rooted values of `233`, `323`, `332` are exactly `0`: each is a tight processed site. The top site `333` is processed and all its 1-predecessors are tight processed sites, which is the hypothesis of the lemma; its rooted value is `1` (the cap is void at the top level), so it has no rooted tree of cost at most zero. (H) fails at `333`; among the other 36 one-sites the largest rooted value is `0`. This witness separately refutes the unit budget and the stated tight-sibling lemma; no equivalence from an unlanded sibling is needed. ∎

## Executed: the controls (not claimed)

`specs/supervisor_control_block37_refuter.py`: block 32's integer program (a formulation with node, arrow and fork variables, solved by a mixed-integer solver, with the fractional objective handled by iteration) gives `c*(η, 333) = 10/9` with the tree `E = 10`, `|A| = 9`, `|S| = 1`, and rooted values `0, 0, 0` at the predecessors and `1` at `333`. A local search from the witness (adding, deleting and moving single marks inside `[0,4]³`, evaluating the three highest processed sites of each realization) tried 705 realizations in seven minutes and found no constant above `10/9`.

## No-Go Discipline Gate

The note's sentences are negative (a conjecture and a lemma are false); the gate applies.

### N1 — Routes by which the no-go could fail
1. *The family misdescribed* — the definitions are restated from blocks 30, 32, 33 and the dynamic program is block 32's own; the control's integer program is an independent formulation of the same family and agrees.
2. *The realization leaking out of the box* — excluded by the argument of T1 and by the two boxes.
3. *The level cap* — void at `333`, the only site of the top level; applied at the predecessors.
4. *A tree with forks* — impossible with one seed (`F = |S| − 1 = 0`).
5. *Exactness of the program* — with one seed the cost is additive over a node set constrained only level to level, so the minimum over subsets of each level is the minimum over trees; the optimal node sets are verified to be trees of the family node by node.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None: the inputs are the automaton's rule and the family's definition.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms`, block 01 (`main`) | the rule the automaton comes from | placement |
| block 30 (open PR #8174) | the automaton, the amplified nodes, the budget with `c = 2` | yes (definitions, restated) |
| block 32 (open PR #8176) | the counted family, `c*`, the conjecture refuted here | yes (definitions, restated) |
| block 33 (open PR #8177) | rooted value, (H), the lemma refuted here | yes (definitions, restated) |
| block 31 (open PR #8175) | the stake `p ≥ 453` | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the unit budget, the tight-sibling lemma and (H) are false" | executed: the rule at every site of `[−1,4]³`; the kinds | executed: exact minima at `333` for four budgets; the rooted value of every one-site | not applicable | executed: the optimal trees verified node by node | one realization on `Z³` suffices; `c* ≥ 10/9`; no upper bound and no threshold statement |

### N6 — Partial-closure paths and primitive scan
None of the registered primitives bears on the count. A partial closure remains: the lemma might hold under an added hypothesis excluding this pattern, but (H) itself fails, so block 33's induction cannot be repaired by the lemma alone.

### N7 — Steelman
Hostile reviewer: "One realization of probability `ε₂⁹ε₁` is irrelevant to a probability bound; the count could still hold with `c = 1` on average." Reply: block 30's bound is a union bound over trees that must exist for every realization; a single realization without a tree in the family breaks the inclusion of events on which the bound rests. A bound that holds on average would be a different theorem with a different proof, and the refinement-history count is such a different proof.

### N8 — Cross-cycle echo
Block 31's lesson returns in a stronger form. Blocks 32–33's conjecture is closed negatively on the day the probes also produced a route that does not need it.

## Falsifiers
- A one-site of the realization outside `[0,3]³`, a different count of kinds, or a site of `[−1,4]³` violating the rule (B1–B2).
- A tree of the family at `333` with `E ≤ |A|`; a minimum of `E − (10/9)|A|` different from `0`; a budget below `10/9` admitting a tree (C1–C2).
- A predecessor of `333` with non-zero rooted value, or a second site with positive rooted value (C3–C4).

## Boundaries and non-claims
This note proves that the unit budget of the explanation-tree route is false: at the realization from ten marks in `[0,3]³` the family constant at the site `333` is exactly `10/9`, so block 32's conjecture `c* = 1`, block 33's tight-sibling lemma and its hypothesis (H) fail; it proves nothing about the formation law's ordering threshold itself. It gives no upper bound on `c*` below block 30's `2`, does not recompute any threshold, and does not touch block 30's theorem or block 33's two lemmas (extension and seed), which remain true. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms` and block 01 (on `main`): placement. Blocks 30, 32, 33 (open PRs): definitions, restated in full above. Block 31 as an evidence address.
- Named standard imports at definition level: dynamic programming over subsets; in the control only, mixed-integer programming and the iteration of Dinkelbach for a fractional objective.
- Reference only: Toom (1980) for the origin of explanation trees.

## Review record — original author provenance
Supervisor-run block (owner 2026-09-20: "harvest again, and then write any blocks that are meaningful / valuable"). Lens: two probe workers reported the same ten-mark witness against a conjecture and an open lemma of the supervisor's own blocks 32 and 33; the supervisor rebuilt the realization with block 32's automaton and ran block 32's exact single-seed program before reading the workers' checks: `1` at `c = 1`, `0` at `c = 10/9`, `1/10` at `c = 11/10`. Refuting pass: block 32's integer program (disjoint machinery) and the rooted program with the level cap agree; a local search found nothing larger. Fold: the statement "exactly `10/9`" was given its two-line monotonicity proof instead of resting on sampled budgets. Mutation census: seven mutations, each failing in its own family.

The original support scripts and experimental outputs remain recoverable on the PR branch. Historical reports are not the fresh landing certificate.

## Verification

```bash
python3 scripts/admissibility_rule_six_axis_formation_threshold_unit_budget_false_one_seed_witness_family_constant_ten_ninths_2026_09_20.py
python3 scripts/admissibility_rule_six_axis_formation_threshold_unit_budget_false_one_seed_witness_family_constant_ten_ninths_2026_09_20.py --list-mutations
python3 scripts/admissibility_rule_six_axis_formation_threshold_unit_budget_false_one_seed_witness_family_constant_ten_ninths_2026_09_20.py --mutation constant_wrong
```
