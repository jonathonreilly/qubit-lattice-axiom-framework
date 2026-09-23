---
claim_id: admissibility_rule_covariance_forces_a_reversible_formation_law_three_covariant_pasts_and_the_six_neighbour_past_settles_into_two_copies_of_the_static_law_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the formation reading of the Record axiom in its 3+1 form (levels of records on the Lattice axiom's Z^3; each record forming from nearest-neighbour records of the previous level by block 19's pairwise rule on the sphere, with weights on the offsets); covariance under the Lattice axiom's 24 proper rotations; the covariant pasts exact (a finite group on a finite set); reversibility exact on rings with symbolic weights; the three shapes exact by relabelling on tori of side 4 and 6; the weighted thresholds exact on 4^3, their infinite-volume values executed"
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_covariance_forces_a_reversible_formation_law_three_covariant_pasts_six_neighbour_past_two_static_laws_2026_09_23.py
---

# Covariance forces a reversible formation law: three covariant pasts, and the six-neighbour past settles into two copies of the static law

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact classification of the covariant nearest-neighbour pasts; reversibility of every one under the pairwise rule; exact structure of each; the 3+1 reading, the nearest-neighbour past and the pairwise rule supplied; nothing adopted or registered; unaudited)

This note works within the formation reading of the Record axiom in its 3+1 form (levels of records on the Lattice axiom's Z^3, each record forming from nearest-neighbour records of the previous level by block 19's pairwise rule); it reports what the axioms' covariance allows for the past and what each allowed past does; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

**Corrigendum (2026-09-23): status and prior art.** Status: the clause behind this note (a record at every site of `Z³` at every tick, each drawn from the previous tick's records) is the clause that block 36 (open PR #8507, 2026-09-20) found EXCLUDED by the axioms memo as written: "A site never carries more than one record; records are permanent." Every result here is conditional on that clause and would need an axiom change; it is not a reading the memo permits. Under the memo as written every site is recorded once (Z³ read as spacetime, blocks 05–35), where blocks 13, 26 and 35 found that a continuous menu loses its memory and that no three-dimensional inverse-Laplacian kernel appears; the owner's reading of 2026-09-20 (records move; one record per site at a time) is a third reading, not this one. Prior art: block 36 (open PR #8507) already proved, under the same clause, that synchronous re-recording from the six neighbours splits into two alternating chains whose space-time checkerboard carries the static law, and that asynchronous re-recording is reversible for the static law (its T1). This note re-derived the first without citing block 36. New here: the classification of the covariant pasts under the rotations, reversibility at every pair of weights, the weighted thresholds and the record-below past. "What the axioms allow in the 3+1 reading" must be read as "what covariance allows within block 36's excluded clause".

## Result up front

Blocks 90–92 (open PRs #8692, #8696, #8703) worked with a supplied light-cone clause: a record forms from the seven records of the previous level around it. The owner's fork (decision record row 61) asked which past the axioms mean by a forming record's "nearest-neighbor conditions". This note asks what the axioms themselves allow. The Admissibility axiom asks for one rule that is covariant under the lattice's symmetries. The Lattice axiom names those symmetries: translations and the 24 proper rotations of the cube. In the 3+1 reading, where levels of records sit on `Z³` and each record forms from nearest-neighbour records of the level below, the answer is short.

1. **Covariance allows three pasts (T1).** The 24 rotations split the candidates `{0, ±e_j}` into two orbits: the record directly below, and its six neighbours. So a covariant rule weights the record below by one number `w₀` and all six neighbours by one number `w₁`. The pasts are the record below alone, the six neighbours alone, or all seven. Every one is symmetric (`w_{−d} = w_d`), because the rotations include the half-turns that send `e_j` to `−e_j`. The level-ordered past `{0, −e₁, −e₂, −e₃}` of blocks 26–28 is fixed by only 3 of the 24 rotations. In this reading it is not covariant; it belongs to the other reading, where levels are diagonals of `Z³` and the time direction itself breaks the rotations.
2. **Every covariant past is reversible (T2).** Under block 19's pairwise rule, every symmetric past gives detailed balance with `π(s) = Π_x Z(h_x(s))`, at every pair of weights. So covariance alone makes forming records reversible: run the history backwards and its statistics are the same.
3. **What each past does (T3).**
   - *The record below alone* (`w₁ = 0`). Sites decouple, each record re-forms from the one beneath it, and the long-time law is uniform at every `β`. No common direction ever forms: `⟨|m|²⟩ = 1/N`.
   - *The six neighbours alone* (`w₀ = 0`). Every step flips the parity of `x`, so the event lattice splits into two classes, `x₁ + x₂ + x₃ + t` even or odd, that never interact. After the parity relabelling the doubled graph is two **disjoint** cubic tori. Two successive levels carry two independent copies of **the static sphere law** with coupling `βw₁`, block 19's comparator. A level's even and odd sites are independent. Each class orders by itself when the static law does (by the single torus's sum rule, for `βw₁ > 3I₀ = 0.758`), in its own direction.
   - *All seven.* Block 90's bilayer, with rung coupling `βw₀` and slab coupling `βw₁`, reflection positive by the same structure. A level keeps a common direction for `β > (3/(2w₁))(I(0) + I(2w₀/w₁))`, with `I(a) = ∫ d³k/(2π)³ 1/(E(k) + a)`. That is `0.5905` at `w₀ = w₁`. Exactly on `4³`: `18239/35840`, `2857397/10250240` and `32773/71680` at `(w₀, w₁) = (1, 1), (1, 2), (2, 1)`.

So in the 3+1 reading the axioms leave a two-weight family of formation laws, all reversible. The static law, until now only the equilibrium comparator, is exactly the long-time law of one of them (the six-neighbour past, on each of its two classes). Block 90's light-cone clause is the generic member. In plain terms: if the rule by which a record forms treats every direction of space alike, it can look only at the record beneath it, at that record's six neighbours, or at all seven, and each choice makes the forming of records reversible. Looking only beneath, records never come to agree. Looking only sideways, the world splits into two interleaved halves that never exchange anything, and each settles into the campaign's static law. Looking at all seven, records keep a common direction above a definite strength.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "decision record row 61(a): which past the axioms mean by a forming record's nearest-neighbor conditions (light-cone versus level-ordered); block 90's light-cone clause supplied"
source_of_blocker_text: blocks 90-92 and the eighth addendum of the decision record (#8572)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "in the 3+1 reading covariance leaves the pasts {0}, the six neighbours and all seven (weights w_0, w_1), all reversible under the pairwise rule; the six-neighbour past settles into two independent copies of the static law; next: the owner's reading (3+1 versus diagonal levels); rules beyond the pairwise family; negative weights"
conditional_surface_status: "T1 exactly; T2 for every ring or torus and every menu by the symmetry of the weighted stencil, checked on rings; T3 for every even L by the parity argument, checked on 4 and 6, with blocks 19 and 90 for memory"
hypothetical_axiom_status: "the 3+1 reading of 'Records form'; a nearest-neighbour past from the previous level; block 19's pairwise rule on the sphere with nonnegative weights; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (the lattice `Z³`; its point symmetries are the 24 proper rotations, with no inversion or reflection), the Admissibility axiom (one rule, covariant under the lattice's symmetries, of nearest-neighbour range; it does not define a time metric) and the Record axiom ("Records form"; permanence). Block 19 (open PR #8153) supplies the pairwise rule on the sphere and the static law; block 90 (open PR #8692) the doubled graph, the relabelling and the bilayer. Nothing is adopted here.

- **The 3+1 reading (supplied).** Levels `t = 0, 1, …` of records on `(Z/L)³`; the record at `(t + 1, x)` forms from records of level `t` at `x + d`, `d` in a past `N ⊂ {0, ±e_j}`, with density proportional to `exp(β s'·Σ_{d∈N} w_d s_{x+d})`, weights `w_d ≥ 0`.
- **Covariance.** The rule is unchanged when the rotation `R` acts on offsets: `w_{Rd} = w_d` for every proper rotation `R`.
- **The classes of the six-neighbour past.** `A = {(x, t): x₁ + x₂ + x₃ + t even}` and its complement.
- **Sums.** `G_L = N⁻¹Σ_{k≠0}1/E(k)`, `H_L(a) = N⁻¹Σ_k 1/(E(k) + a)`, `I(a)` their integrals.

That covariant rules on a lattice have weights constant on orbits of the point group is elementary group theory; the detailed-balance argument and the bilayer are blocks 90's; the static law's sum-rule threshold is block 19's method (after Fröhlich, Simon and Spencer). None is used as authority; every step is checked here.

## Prior art and what is new

Blocks 26–28 studied level-ordered formation on `Z³` read as spacetime; blocks 90–92 the light-cone clause in 3+1. New here: in the 3+1 reading, the classification of the covariant nearest-neighbour pasts (three shapes, two weights), the fact that covariance alone makes formation reversible under the pairwise rule, and the identification of the six-neighbour past's long-time law with two independent copies of the static law, so that the static comparator is realized exactly inside a covariant formation law.

## Exact target and obligation graph

Target: what covariance allows for the past, and what each allowed past does. Obligations: (O1) the covariant pasts; (O2) their reversibility; (O3) the structure of each. T1–T3 discharge them.

## Theorem T1 — covariance allows three pasts, all symmetric

*Statement.* A weighting `w` of `{0, ±e_j}` is invariant under the 24 proper rotations iff `w_0` is arbitrary and `w_{±e_j} = w₁` for all six; every invariant weighting is symmetric. The level-ordered past `{0, −e₁, −e₂, −e₃}` has a stabiliser of order 3 and is not symmetric.

*Proof.* The rotations fix `0` and act transitively on the six face vectors, including the half-turns `e_j ↦ −e_j`. Family B enumerates the 24 rotations (signed permutation matrices of determinant one), checks all 2187 weightings with weights `0, 1, 2` (exactly 9 invariant, all orbit-constant and symmetric), and computes the level-ordered past's stabiliser. ∎

## Theorem T2 — every covariant past is reversible

*Statement.* For weights `(w₀, w₁)`, any menu and any `β`, the pairwise chain satisfies `π(s)P(s'|s) = π(s')P(s|s')` with `π(s) = Π_x Z(h_x(s))`.

*Proof.* `π(s)P(s'|s) = exp(β Σ_{x,d} w_d s'_x·s_{x+d})`, symmetric in `(s, s')` because `w_{−d} = w_d` (block 90 T1 with weights). Family C checks every pair on a ring of four (two values) and a ring of three (four six-axis contents), with `t₀ = e^{βw₀}`, `t₁ = e^{βw₁}` symbolic. ∎

## Theorem T3 — the three shapes

*Statement.* (a) With `w₁ = 0` the chain factorises over sites and its stationary law is uniform; `⟨|m|²⟩ = 1/N`. (b) With `w₀ = 0` the relabelled doubled graph is two disjoint cubic tori, slab 0 being the even sites of level `t` with the odd sites of level `t + 1`. The pair law of two successive levels is the product of two static laws with coupling `βw₁`, and a level's even and odd sites are independent. By the single torus's sum rule each orders for `βw₁ > 3G_L` (`1517/2560` on `4³`). (c) With `w₀, w₁ > 0` the relabelling carries rung weight `w₀` and slab weight `w₁`; the sum rule over the two branches `w₁E(k)` and `w₁E(k) + 2w₀` gives memory of a level for `β > (3/(2w₁))(G_L + H_L(2w₀/w₁))`.

*Proof.* (a) The one-site kernel `t^{c'·c}/Z` is symmetric with equal row sums (family D, six-axis contents); for the sphere it is rotation invariant. (b) Every offset `±e_j` flips parity, so an edge `(x, 0)–(x ± e_j, 1)` stays in one slab (family D, edge by edge on `4³` and `6³`, the classes vertex by vertex). (c) Family D checks the weighted relabelling for three weight pairs; family E evaluates the thresholds exactly on `4³`. Reflection positivity and the infrared bound are block 90's T3 with positive weights. ∎

## Executed (supervisor control; floating point; evidence, not proof)

Controls in the pack (`specs/supervisor_control_block93_covariant_pasts.py`, output in `.out.txt`).

*W1 — infinite-volume thresholds.* `β₀(w₀, w₁) = (3/(2w₁))(I(0) + I(2w₀/w₁))` by quadrature: `0.5905` at `(1, 1)`, `0.3174` at `(1, 2)`, `0.5398` at `(2, 1)`; the six neighbours alone, `3I(0)/w₁ = 0.7582` at `w₁ = 1`; the record below alone never.

*W2 — the two classes, seen directly.* A level on `16³` is started with its even sites along `z` and its odd sites along `x`, and the formation law runs at `β = 1.5` (block 19's rule, exact sampling). The table gives the cosine between the even-site mean and the odd-site mean of the current level:

| levels | 1 | 5 | 10 | 50 | 100 | 400 |
|---|---|---|---|---|---|---|
| six neighbours alone (`w₀ = 0`) | −0.013 | +0.019 | −0.001 | −0.053 | −0.105 | −0.116 |
| all seven (`w₀ = w₁`) | +0.314 | +0.914 | +0.998 | +1.000 | +1.000 | +1.000 |

With the six neighbours alone the two halves stay orthogonal: each keeps its own direction (both means stay near `0.82`) and drifts independently. With all seven they align within ten levels.

## No-Go Discipline Gate

The note's negative sentences: the level-ordered past is not covariant in the 3+1 reading; the record below alone keeps no common direction; the six-neighbour past's two classes never interact.

### N1 — Routes by which the sentences could fail or mislead
1. *The reading.* The classification is for the 3+1 reading; in the reading where levels are diagonals of `Z³` (blocks 26–28) the time direction breaks the rotations and the level-ordered past is natural there. Which reading the axioms mean is the owner's.
2. *The rule.* Reversibility is for block 19's pairwise rule; a covariant rule that is not pairwise (for example weighting `(s'·h)²`) need not be reversible.
3. *The range.* Nearest-neighbour pasts only; second neighbours would add orbits.
4. *Signs.* Nonnegative weights; negative weights (anti-alignment) are not treated.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The pairwise rule; nonnegative weights; even tori for the relabelling.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the 24 proper rotations; one covariant nearest-neighbour rule; "Records form" | yes (premise) |
| block 19 (open PR #8153) | the pairwise rule; the static law | yes |
| block 90 (open PR #8692) | the doubled graph, the relabelling, the bilayer | yes |
| blocks 26–28 (open PRs #8170, #8172) | the level-ordered reading | no (placed) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "covariance leaves three pasts, all reversible; the six-neighbour past settles into two static laws" | executed: 2187 weightings against 24 rotations; detailed balance on two rings; the copy kernel | executed: the six-neighbour relabelling and classes; the weighted relabelling | executed: weighted thresholds on 4³; control quadrature and simulation | executed: the level-ordered stabiliser; the uniform copy law; the six-neighbour threshold | T1 exactly; T2, T3 for every even L with the stated scope

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "Covariance is doing nothing; you chose the 3+1 reading." Reply: the reading is supplied and named, and it is the owner's fork. Within it, covariance is the whole argument: it removes every asymmetric past, and symmetry is exactly what makes the pairwise chain reversible. Second objection: "The six-neighbour result is trivial parity bookkeeping." Reply: the bookkeeping is trivial. The consequence is not: the campaign's static comparator is the exact long-time law of a covariant formation rule.

### N8 — Cross-cycle echo
Block 90 took the light-cone past as a supplied clause; here it is the generic member of the covariant family. Blocks 26–28 found forgetting in the level-ordered reading; here that past is not covariant in 3+1. Block 19's static law, the comparator since block 17, is here a formation law's stationary law.

## Falsifiers

- A rotation-invariant weighting of `{0, ±e_j}` that is not symmetric.
- A pair of configurations on a ring for which a covariant weighted chain violates detailed balance.
- An edge of the six-neighbour doubled graph whose relabelled endpoints lie in different slabs.

## Boundaries and non-claims

The 3+1 reading, the nearest-neighbour past, the pairwise rule and nonnegative weights are supplied; which reading and which weights the axioms mean is the owner's; no statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice, Admissibility and Record axioms. Blocks 19, 26–28, 90 (PRs): restated or used as machinery.
- Named standard imports at definition level: the rotation group of the cube as signed permutation matrices; detailed balance; the infrared bound's sum rule (block 90, block 19); quadrature and simulation for the control.

## Review record
Corrigendum (2026-09-23, supervisor): block 36 (#8507) is prior art and its excluded clause governs this note's status; missed in the lens pass, found when the owner asked to probe the readings against known physics. Text-only; no theorem, check or number changed.

Supervisor-run block, the forty-first since the source-link direction opened; the formation lane; the fifth run on Claude Opus 5.5. Found while preparing the decision record's eighth addendum: the owner's fork on the past (row 61a) is partly decided by the axioms' covariance in the 3+1 reading. Lens pass, in writing, by the supervisor: a foundations lens — the reading, the range, the rule and the sign of the weights are named as supplied, and the level-ordered past is placed in its own reading rather than dismissed; a rigour lens — the classification is a finite enumeration, reversibility is checked with symbolic weights, the decoupling edge by edge, and the thresholds exactly. Mutation census: eight mutations, each failing in its own family only. No independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_covariance_forces_a_reversible_formation_law_three_covariant_pasts_six_neighbour_past_two_static_laws_2026_09_23.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
