---
claim_id: admissibility_rule_binding_scale_pinned_at_the_neutral_value_pair_weight_is_the_rules_likelihood_ratio_no_binding_without_a_cycle_all_binding_is_agreement_around_loops_bounded_theorem_note_2026-09-20
claim_type: bounded_theorem
claim_scope: "CONDITIONAL on the moving-records reading of block 39 (PR #8530) and on the PROPOSAL that the binding scale takes the neutral value; neither is in the axioms memo and neither is adopted or registered. For the six-axis rule with positive weights omega = (p, q, r), one-neighbour probability K_1(b | a) = omega(a, b)/(p + q + 4r), and the law with vacancies (a bond between two records weighs c omega, a bond with an empty end weighs 1, a record weighs z), on finite windows: (T1) c_0 = 6/(p + q + 4r) is the only scale at which the pair weight is the rule's likelihood ratio against the uniform law, W(a, b) = K_1(b | a)/(1/6); equivalently the empty row of the 7 x 7 bond kernel is the average of the six record rows (the vector (-6, 1, ..., 1) is annihilated; by block 39's T5 this is also the least reflection-positive scale); equivalently an empty site next to one record forms at the empty-space rate; and at c_0 the formation rate over its empty-space value is the likelihood ratio of the neighbours' contents under a common uniformly drawn cause against independent uniform draws. (T2) At c_0, on a window without a cycle, the occupancy is independent from site to site with density 6z/(1 + 6z), every occupied forest weighs (6z)^n, and the contents of an occupied tree follow the rule's tree law: records neither attract nor repel. (T3) A fully occupied cycle of length n weighs (6z)^n (1 + 3 l_1^n + 2 l_2^n), l_1 = (p - q)/(p + q + 4r), l_2 = (p + q - 2r)/(p + q + 4r) the non-trivial eigenvalues of K_1: at c_0 all binding comes from cycles and is fixed by the rule; the plaquette factor is 433/432 at (3,1,2) and 83842/64827 at (12,1,2). (T4) At any scale c, on a window without a cycle, the occupied set weighs (6z)^n (c/c_0)^(occupied bonds): the content-less lattice gas with bond activity c/c_0, so c/c_0 is exactly the binding that the rule does not account for. EXECUTED, not claimed (cubic lattice, side 16, line (p,1,2), c = c_0): the onset of alignment moves down as the density rises: above p = 16 at density 1/10, between 8 and 12 at 3/10, between 6 and 8 at 1/2, below 6 at 7/10."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_binding_scale_pinned_neutral_value_likelihood_ratio_no_binding_without_a_cycle_2026_09_20.py
---

# The binding scale pinned at the neutral value: the pair weight is the rule's likelihood ratio, an empty site is a record of unknown content, records do not bind without a cycle, and all binding is agreement around loops

**Date:** 2026-09-20
**Type:** bounded_theorem
**Status:** bounded-support (exact on finite windows; the value is a proposal under a supplied reading; the density map executed, not claimed; nothing adopted or registered; unaudited)

## Result up front

Block 39 (PR #8530) showed that once records move, the overall scale `c` of the pair weights, which the axioms' normalized distribution cannot see, becomes a binding constant, and that reflection positivity of the law with vacancies requires `c ≥ c₀ = 6/(p + q + 4r)`. The owner asked whether the constant can be derived and accepted the recommendation to proceed with the most promising value. This note gives the case for `c = c₀` and what that value does.

This note works under the moving-records reading of block 39 and proposes the value c = c_0 for the binding scale; neither the reading nor the value is in the axioms memo, and neither is adopted or registered here.

1. **Four characterizations of one value (T1).** At `c₀`, and only there: the pair weight is the rule's own probability divided by chance, `W(a, b) = K₁(b | a)/(1/6)`, a likelihood ratio, so a bond with an empty end, of weight `1`, carries no information; an empty site acts on each neighbour exactly as a record of uniformly random content would; an empty site next to one record forms at the rate of an isolated empty site; and (block 39) the law with vacancies is reflection positive from this value up and not below it. The formation rate becomes a likelihood ratio too: how much more likely the neighbours' contents are if they share a common cause than if they are unrelated.
2. **No binding without a cycle (T2).** At `c₀`, on any window whose graph has no cycle, the occupancy of the sites is exactly independent, with density `6z/(1 + 6z)`, and the contents follow the rule's own tree law. Records neither attract nor repel.
3. **All binding is agreement around loops (T3).** A fully occupied cycle of length `n` carries the extra factor `1 + 3λ₁ⁿ + 2λ₂ⁿ`, with `λ₁, λ₂` the two non-trivial eigenvalues of the rule's one-neighbour probability. That factor is the whole interaction between records at `c₀`, and the rule fixes it: `433/432` on a plaquette at `(3,1,2)`, `1.29` at `(12,1,2)`.
4. **What any other value adds (T4).** At another scale the occupancy on a window without a cycle is the content-less lattice gas with bond activity `c/c₀`. So `c/c₀` is precisely a glue, or a repulsion, that the rule does not account for. At `c₀` there is none.
5. **Executed, not claimed.** With the scale pinned, where records gather is a consequence of the rule and the density alone: on the line `(p,1,2)` the onset of alignment lies above `p = 16` at density `0.1`, between `8` and `12` at `0.3`, between `6` and `8` at `0.5`, below `6` at `0.7`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "owner, 2026-09-20: 'this weight is a primitive like planck - if we derive or find it, we can state it'; 'can the constant be derived by lattice length? or is it separate?'; 'Whatever looks most promising, ill take you recommendation - lets proceed'"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the case for the neutral value made exact (likelihood ratio; absence as ignorance; no binding without a cycle; loop factors from the rule's eigenvalues; the glue c/c_0) and the pinned law's density map executed on one line. Next: the owner's act on the value (register it, or leave it free); with the value pinned, the sphere menu's law with vacancies (c_0 = beta/sinh beta), its long-range order and the stiffness of its kernel, which is what a strength of the long-range potential in lattice units would be computed from"
conditional_surface_status: "T1-T4 proved for every finite window and every positive six-axis triple; the value c = c_0 is proposed, not adopted and not registered; the executed density map (one seed, side 16, 3000 sweeps) is in the controls and not claimed"
hypothetical_axiom_status: "the moving-records clause of block 39 and the value c = c_0 of the binding scale; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full) is used through "No possibility is privileged.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." and "A site with no record cannot be read.". Block 01 (on `main`, proposed and unaudited) supplies the rule as a product of pair weights and the static law. Block 39 (open PR #8530) supplies the moving-records reading, the law with vacancies and the reflection-positivity bound; its objects are restated here.

- **The rule's one-neighbour probability.** `K₁(b | a) = ω(a, b)/(p + q + 4r)`, a symmetric stochastic matrix with eigenvalues `1`, `λ₁ = (p − q)/(p + q + 4r)` (three times) and `λ₂ = (p + q − 2r)/(p + q + 4r)` (twice).
- **The law with vacancies.** A site is empty or carries a record; a record weighs `z`; a bond between two records weighs `W = cω`; a bond with an empty end weighs `1`. The bond kernel is the `7 × 7` matrix with first row and column `1` and the block `cω`.
- **Neutral scale.** `c₀ = 6/(p + q + 4r)`.
- **Formation rate** (block 39, T4): `zZ_x`, `Z_x = Σ_a Π_{y∼x, occupied} W(a, s_y)`.

A ratio of a probability to a reference probability is a likelihood ratio; the ratio of the probability of data under two hypotheses is the factor of Bayes; independent occupancies are variables of Bernoulli; laws of this kind are those of Gibbs. None is used as authority.

## Prior art and what is new

Block 24 (PR #8158) asked how an unrecorded site should be weighed and found two readings that differ on bridges. Block 39 found the binding scale and its reflection-positivity floor. What is new: the identification of that floor with a normalization that has a meaning in the axioms' own terms (the pair weight as the rule's probability against chance, with an empty bond as "no information"); the theorem that at this value records do not interact on any window without a cycle; the closed form of the loop factor from the rule's eigenvalues; and the reading of `c/c₀` as the one quantity the rule leaves unexplained. High-temperature (loop) expansions of lattice gases are classical; the statements here are elementary and are proved in full.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T1 | four characterizations of `c₀`; the formation rate as a likelihood ratio | row sums of `cω`; one line each | B |
| T2 | no cycle: independent occupancy, forests weigh `(6z)ⁿ`, the rule's tree law | summing out a leaf | C |
| T3 | the loop factor `1 + 3λ₁ⁿ + 2λ₂ⁿ` | the trace of `(6K₁)ⁿ` | D |
| T4 | away from `c₀`: bond activity `c/c₀` | the same leaf argument | E |

## Theorem T1 — four characterizations of the neutral scale

The rows of `ω` sum to `p + q + 4r`. Hence `cω(a, b) = K₁(b | a)/(1/6)` exactly when `c(p + q + 4r) = 6`. The same equation says that the rows of `cω` average to `1`, which is the weight of a bond with an empty end: the empty row of the bond kernel is the average of the six record rows, and `(−6, 1, …, 1)` is annihilated. It also says `Z_x = 6` next to one record, the empty-space value. By block 39's T5 the bond kernel is positive semidefinite exactly for `c ≥ c₀` (given `p ≥ q`, `p + q ≥ 2r`), so `c₀` is the least reflection-positive scale. At `c₀`, `Z_x/6 = (1/6) Σ_a Π_y [K₁(s_y | a)/(1/6)]`, which is the probability of the neighbours' contents if each is drawn from the rule around one uniformly drawn content `a`, divided by their probability as independent uniform draws. ∎

**Reading.** "No possibility is privileged" makes the uniform law the reference; the rule supplies `K₁`; "a site with no record cannot be read" makes an absent record carry no information, weight `1`. The three together give `W = K₁/(1/6)`, that is `c = c₀`. This is a reading of the axioms' sentences, not a derivation from them: the memo does not say that weights are likelihood ratios.

## Theorem T2 — at the neutral scale records do not bind without a cycle

Let `x` be a leaf attached to `y`. Summing over the state of `x`: an empty `x` contributes `1`; a record contributes `z Σ_b W(b, s_y) = 6z` if `y` carries a record and `6z` if `y` is empty. So the sum is `1 + 6z` whatever the state of `y`: the leaf separates, empty with probability `1/(1 + 6z)`. Removing leaves one at a time, on a window without a cycle every site is occupied independently with probability `6z/(1 + 6z)`, an occupied set of `n` sites weighs `(6z)ⁿ`, and the contents of an occupied tree have weight `Π_edges 6K₁`, which normalized is the rule's tree law: a uniform root and `K₁` along each edge. The same holds for every occupied set without a cycle inside a larger window: `57` of the `64` occupied sets of the `2 × 3` window, exactly. ∎

## Theorem T3 — all binding is agreement around loops

For a fully occupied cycle of length `n` the sum over contents is the trace of `(cω)ⁿ = (6K₁)ⁿ`, that is `6ⁿ(1 + 3λ₁ⁿ + 2λ₂ⁿ)`. Against the value `6ⁿ` of a path of the same length, the cycle carries the factor `1 + 3λ₁ⁿ + 2λ₂ⁿ`, larger than `1` for the even cycles of the cubic lattice. On the plaquette it is `433/432` at `(3,1,2)`, `280086/279841` at `(5,2,4)` and `83842/64827` at `(12,1,2)`; at `(3,1,2)` with `z = 1/12` the covariance of two neighbouring occupancies on the plaquette is `15552/1224510049`, positive and produced by this factor alone. The interaction between records at `c₀` is therefore a sum over the cycles of the occupied set with weights computed from the rule's eigenvalues, and nothing else. ∎

## Theorem T4 — what any other scale adds

Repeat the leaf argument at a scale `c`: a record at a leaf next to a record contributes `z · c(p + q + 4r) = 6z · (c/c₀)`, next to an empty site `6z`. On a window without a cycle the occupied set then weighs `(6z)ⁿ (c/c₀)^{occupied bonds}`: the content-less lattice gas with bond activity `c/c₀`. The contents still follow the rule's tree law. So a scale above `c₀` is a content-blind attraction of strength `log(c/c₀)` per bond that the rule does not account for, a scale below it a repulsion (and a loss of reflection positivity). ∎

## Executed: the pinned law on the cubic lattice (not proved)

Controls in the pack (`specs/supervisor_control_block40_*`; the simulator is block 39's). Line `(p,1,2)`, `c = c₀`, side `16`, `3000` sweeps, one seed. Entries: recorded neighbours per record over the random value / fraction of record–record bonds with equal contents (`0.17` at random) / fraction of moves accepted.

| `p` | density `0.1` | density `0.3` | density `0.5` | density `0.7` |
|---|---|---|---|---|
| `6` | `1.15 / 0.40 / 0.46` | `1.05 / 0.42 / 0.40` | `1.02 / 0.47 / 0.36` | `1.05 / 0.75 / 0.32` |
| `8` | `1.16 / 0.47 / 0.44` | `1.07 / 0.52 / 0.36` | `1.19 / 0.81 / 0.30` | `1.08 / 0.86 / 0.25` |
| `10` | `1.16 / 0.53 / 0.43` | `1.21 / 0.69 / 0.33` | `1.28 / 0.91 / 0.26` | `1.10 / 0.90 / 0.20` |
| `12` | `1.16 / 0.57 / 0.41` | `1.42 / 0.83 / 0.30` | `1.33 / 0.94 / 0.24` | `1.11 / 0.92 / 0.17` |
| `16` | `1.18 / 0.65 / 0.39` | `1.78 / 0.94 / 0.27` | `1.38 / 0.96 / 0.20` | `1.11 / 0.93 / 0.13` |

The onset of alignment moves down as the lattice fills, in the direction of the full-lattice value `p ∈ (3.6, 3.7)` that block 28 (PR #8172) located for the static law. The refuting control recomputes T2 and T3's covariances by an independent enumeration at three scales: exactly zero on the path and the star at `c₀`, `15552/1224510049` on the plaquette, `12/289` and `−240/9409` on the path at `c = 1` and `c = 1/4`.

## No-Go Discipline Gate

The note's sentences are positive, with one uniqueness sentence (no other scale has the properties of T1); the gate is applied for that sentence.

### N1 — Routes by which the sentences could fail
1. *The reading* — that weights are likelihood ratios is a reading, stated as such; the theorems are about the value, whatever its motivation.
2. *Menus without constant row sums* — T1 uses that every row of `ω` has the same sum, which the covariance of the rule gives for the six axes (and for any menu on which the symmetry group acts transitively); otherwise "the neutral scale" is not one number.
3. *Cycles inside the window* — T2 is about windows and occupied sets without a cycle; the cubic lattice is full of cycles, and there T3's factors act. No statement about the infinite lattice is made.
4. *The executed map* — one seed, side `16`, finite time, contents conserved so that alignment requires records to travel; the brackets are wide.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond block 39's reading and law, declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the three sentences behind the reading | yes (premise of the reading) |
| block 01 (`main`) | the rule as a product of pair weights | yes (premise, proposed) |
| block 39 (open PR #8530) | the reading, the law with vacancies, the reflection-positivity bound, the rate `zZ_x` | yes (restated) |
| block 24 (open PR #8158), block 28 (open PR #8172) | the unrecorded-site question; the full-lattice located value | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "at the neutral scale the pair weight is the rule's likelihood ratio, records do not bind without a cycle, and the loop factor is fixed by the rule's eigenvalues" | executed: the characterizations at three triples; the formation rate on all 36 neighbour pairs | executed: exact occupancy laws on four windows without a cycle; all 64 occupied sets of the `2×3` window | executed: loop factors for `n = 4, 6` at three triples | executed: the lattice-gas form away from `c₀` | proved for every finite window; the value is a proposal; the density map executed and not claimed |

### N6 — Partial-closure paths and primitive scan
The registered primitives do not supply the scale. Registering `c = c₀` as a primitive, or stating it as a consequence of a reading of the axioms, is the owner's act.

### N7 — Steelman
Hostile reviewer: "You chose a normalization and then admired its properties; any value could be decorated the same way." Reply: four properties that have no reason to coincide pick the same number: a likelihood-ratio normalization, the equality of an empty site with an unknown record, a formation rate insensitive to a single neighbour, and the boundary of reflection positivity; and at that number, and at no other, the interaction between records vanishes on every window without a cycle, so that the rule alone accounts for all binding. Any other value adds a glue `c/c₀` with no origin in the rule. That is an argument for the value, not a proof that nature uses it.

### N8 — Cross-cycle echo
Block 14's equality of growth and static law on trees returns as T2's tree law; block 38's `Z = D_min` on windows without a cycle is the full-occupancy case of the same leaf argument; block 39's floor becomes the value.

## Falsifiers
- A second scale with any of T1's properties; a neighbour pair where the formation rate is not the stated likelihood ratio (B1–B3).
- A window without a cycle where occupancies are correlated at `c₀`, or an occupied forest not weighing `(6z)ⁿ` (C1–C2).
- A cycle whose factor differs from `1 + 3λ₁ⁿ + 2λ₂ⁿ` (D1–D2).
- A window without a cycle, at a scale `c ≠ c₀`, whose occupied sets do not weigh `(6z)ⁿ(c/c₀)^{bonds}` (E1).

## Boundaries and non-claims
This note works under the moving-records reading of block 39 and proposes the value c = c_0 for the binding scale; neither the reading nor the value is in the axioms memo, and neither is adopted or registered here. It proves T1–T4 on finite windows; it makes no infinite-volume statement, proves no onset of clumping, and identifies nothing it finds with anything in nature. It does not derive the value from the axioms: it shows that one reading of three of their sentences gives it, and what the value does. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises. Block 01 (on `main`): the rule; proposed, unaudited. Block 39 (PR #8530, open): restated. Blocks 24 and 28 as evidence addresses.
- Named standard imports at definition level: the trace of a power of a symmetric matrix as the sum of the powers of its eigenvalues; summation over a leaf of a tree.
- Reference only: the high-temperature expansion of lattice gases; Bayes for the name of the factor in T1.

## Review record
Supervisor-run block (owner 2026-09-20: "can the constant be derived by lattice length? or is it separate?", then "Whatever looks most promising, ill take you recommendation - lets proceed! if that value is a pin that solves the TOE, then so be it"). Lens: a length cannot give a pure number, so the value has to come from the rule; block 39's floor had one more property than the supervisor had noticed, the averaged empty row, and with it the prediction that records should not interact on a window without a cycle. That prediction was tested exactly before anything was written (covariance `0` on the path and the star at `c₀`, `12/289` and `−240/9409` at `c = 1` and `1/4`). Refuting pass: an independent enumeration for the covariances; the density map with block 39's validated simulator. Fold: the uniqueness sentence in T1 and the scope of T2 (occupied sets without a cycle inside larger windows) were added after the runner's `2×3` census. The note says plainly that pinning one constant settles one constant. Mutation census: eight mutations, each failing in its own family.

## Verification

```bash
python3 scripts/admissibility_rule_binding_scale_pinned_neutral_value_likelihood_ratio_no_binding_without_a_cycle_2026_09_20.py
python3 scripts/admissibility_rule_binding_scale_pinned_neutral_value_likelihood_ratio_no_binding_without_a_cycle_2026_09_20.py --list-mutations
python3 scripts/admissibility_rule_binding_scale_pinned_neutral_value_likelihood_ratio_no_binding_without_a_cycle_2026_09_20.py --mutation tree_independence_at_wrong_scale
```
