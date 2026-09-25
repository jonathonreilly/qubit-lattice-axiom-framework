---
claim_id: admissibility_rule_waves_need_signed_weights_a_formation_rule_with_nonnegative_weights_keeps_an_undamped_branch_only_by_rigid_transport_and_the_amplitude_step_is_a_signed_rule_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "WITHIN block 13's linear formation law in level time as landed on main (theta_{t+1}(x) = sum_j sum_y w_j(y) theta_{t-j}(x - y), vector-valued, finitely supported weights; the branches are the roots of the dispersion relation) and block 54's walk as landed, both supplied. (T1, T2) With entrywise nonnegative weights of gain one (row-stochastic total) every branch has |lambda(k)| <= 1, and a branch is unimodular on a set of wave numbers with nonempty interior only for rigid transport - one velocity with a gauge, mixing between components included - so no such rule disperses, at any depth of memory, any number of components and in any dimension; imports: the theory of nonnegative matrices with its equality case, and one analytic step of the attempts, named in Imports. (T3) the signed two-level rule theta_{t+1} = 2a P theta_t - theta_{t-1} (P the neighbour average) is lossless at every wave number exactly when |a P(k)| <= 1; at a = 1, cos omega = P(k), omega = |k| on the line, and the long-wave cones are round. (T4) the 1+1 coin walk's step U obeys U^2 - (tr U) U + 1 = 0 with tr U = 2 cos theta cos k: the amplitude step is T3's signed rule. Harvest block from five Grok-refereed probes attempts, re-checked by an independent runner (exact certificates at rational angles). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_waves_need_signed_weights_nonnegative_rules_keep_an_undamped_branch_only_by_rigid_transport_2026_09_24.py
---

# Waves need signed weights: a formation rule with nonnegative weights keeps an undamped branch only by rigid transport, and the amplitude step is a signed rule

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 13 and 54 as landed; T2 with named imports; harvest block from five Grok-refereed probes attempts; nothing adopted or registered; unaudited)

This note works within block 13's linear formation law in level time and block 54's walk, both as landed on main and both supplied; it reports that nonnegative weights cannot carry undamped dispersive waves while signed weights can, and that the amplitude walk's step is such a signed rule; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 96, as landed, found that clocked record motion never oscillates. Its detailed balance makes the generator self-adjoint with a real spectrum. That leaves the formation side open: can a rule by which records form carry waves, where the rule's weights are the odds the admissibility rule supplies, nonnegative and summing to one?

- **T1: nonnegative rules damp every non-transport branch.** For such weights, at any depth of memory, every branch has `|λ(k)| ≤ 1`. The witnesses include:
  - the neighbour average;
  - block 96's persistent line walk;
  - two-level and two-component rules.

  All of them have their non-transport branches strictly inside the unit circle at every rational angle tested (exact unit-disk certificates).
- **T2: the only undamped branches are rigid transport.** A branch with `|λ(k)| = 1` on any open set of wave numbers exists only if the rule moves everything at one velocity, up to a gauge. Mixing between components is allowed. So no rule with nonnegative weights disperses: no wave spreads and keeps its amplitude, in any dimension and at any depth of memory. This rests on the theory of nonnegative matrices and its equality case, named imports.
- **T3: signed weights propagate.**
  - The two-level rule `θ_{t+1} = 2aPθ_t − θ_{t−1}` has one negative weight. It is lossless at every wave number exactly when `|aP(k)| ≤ 1`.
  - At `a = 1`, `cos ω = P(k)`. On the line this is `ω = |k|` exactly, and in three dimensions the long-wave cones are round.
- **T4: the amplitude walk is such a rule.** The coin walk's step `U` satisfies `U² − (tr U)U + 1 = 0` with `tr U = 2 cos θ cos k`. So each amplitude obeys T3's signed rule with `a = cos θ`.

In plain terms, the admissibility rule gives each site odds, which are nonnegative numbers adding to one. Any law built by mixing past values with such odds is a kind of averaging. Averaging can move a pattern along bodily, or smear it out, but it can never make a wave that travels without dying. That needs weights that can be negative, so that contributions cancel as well as add. The walker's amplitudes do exactly that: each step of the walk is a rule with a minus sign in it. So waves are one thing that records' odds cannot supply by themselves. They need the amplitude layer, which is supplied.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." Odds are nonnegative and sum to one.
  - "Records form."
  - "Admissibility is not a dynamics axiom." The formation law and the walk are supplied clauses. Nothing is adopted.
- **The formation law in level time** (block 13 as landed, its directed Gaussian propagator; supplied).
  - `θ_{t+1}(x) = Σ_{j<J} Σ_y w_j(y) θ_{t−j}(x − y) (+ noise)`, with `θ_t(x) ∈ ℝ^M` and finitely supported `M × M` weights.
  - Noise does not enter the dispersion relation.
  - A mode `λ^t e^{ik·x}` requires `det(λ^J − Σ_j W_j(k)λ^{J−1−j}) = 0`, with `W_j(k) = Σ_y w_j(y)e^{−ik·y}`. The roots are the *branches*.
- **Nonnegative, gain one.** Every entry of every `w_j` is `≥ 0`, and `A = Σ_{j,y} w_j(y)` is row-stochastic (and irreducible, or treat each class).
- **Rigid transport.** Each entry of each `w_j` is carried by a single displacement, and the resulting phases form a diagonal conjugation times a global phase. The rule then moves everything at one velocity, up to a gauge.
- **The walk** (block 54 as landed). The 1+1 coin walk `U(k) = C(θ) diag(e^{−ik}, e^{ik})` is the discrete-step form used for T4.

## Theorem T1 — nonnegative rules damp every non-transport branch

*Statement.*
- For nonnegative gain-one weights, every branch satisfies `|λ(k)| ≤ 1`.
- In the witnesses, every non-transport branch lies strictly inside the unit circle at every tested `k ≠ 0`:
  - the neighbour average `(1 + e^{−ik})/2`;
  - block 96's persistent line walk (`p = 9/25`);
  - the two-level rule `w₀ = ½δ₁`, `w₁ = ½δ₂`;
  - the two-component mixing rule `A = [[1/2, 1/2], [1, 0]]` at displacement `+1`.
- The unimodular branches that remain are transport:
  - `e^{−ik}` for the two-level and mixing rules;
  - `±e^{−ik/2}` for the half-step rule `θ_{t+1}(x) = θ_{t−1}(x − 1)`.

*Proof.* The companion matrix of the rule is dominated entrywise, in modulus, by its value at `k = 0`, which is nonnegative with spectral radius 1. ∎

*Checked (B1).* Exact unit-disk tests (see Imports) with Gaussian-rational coefficients, at five rational angles. The factorisations into transport times a decaying partner are exact.

## Theorem T2 — the only undamped branches are rigid transport

*Statement.* For nonnegative gain-one weights, some branch has `|λ(k)| = 1` on a set of `k` with nonempty interior only if the rule is rigid transport. In particular no such rule disperses, at any depth `J`, any number of components `M`, and in any dimension.

*Proof sketch* (the attempts, refereed).
- **The entrywise half.** Let `C` be nonnegative and irreducible with `ρ(C) = 1`, and let `|B| ≤ C`. If `Bx = λx` with `|λ| = 1`, then `|B| = C`. The chain is `|x| = |Bx| ≤ |B||x| ≤ C|x|`; a positive left eigenvector of `C` kills the slack.
- **The phase half.** The equality case of the theory of nonnegative matrices, imported, makes `B` a diagonal conjugation of `C` times a unit phase.
- **Open sets.** On an open set of `k` this forces each entry to a single displacement: that is rigid transport. The step from an open set to a single displacement is the attempts' analytic argument, named. ∎

*Checked (C1).* On instances of the entrywise lemma, for a row-stochastic irreducible `3×3` `C`:
- a gauge `DCD⁻¹` times a global phase keeps a unimodular eigenvalue;
- a single entry phase that is no gauge, with or without a reduced modulus, puts every root strictly inside (the unit-disk test at five rational angles).

## Theorem T3 — signed weights propagate

*Statement.* For `θ_{t+1} = 2aPθ_t − θ_{t−1}`, where `P` is the neighbour average with symbol `P(k) = (1/d)Σ_j cos k_j`:
- The two roots multiply to 1. So both are unimodular exactly when `|aP(k)| ≤ 1`, and the rule is then lossless at `k`.
- At `a = 1` every wave number propagates, with `cos ω = P(k)`:
  - `ω = |k|` exactly on the line;
  - `ω² = |k|²/3 + O(k⁴)` in three dimensions, along an axis and along the body diagonal alike.
- At `a = 5/4` the rule has the root 2 at `k = 0` and grows.

*Proof.* Use the product of the roots and the discriminant `4(a²P² − 1)`. Then `ω² = 2(1 − P) + (1 − P)²/3 + …`. ∎

*Checked (D1).* Symbolically.

## Theorem T4 — the amplitude step is a signed rule

*Statement.* For the 1+1 coin walk `U(k) = C(θ) diag(e^{−ik}, e^{ik})`:
- `det U = 1` and `tr U = 2 cos θ cos k`;
- `U² − (tr U)U + 1 = 0`.

So each amplitude obeys `ψ_{t+1} = 2 cos θ · Cψ_t − ψ_{t−1}`, where `C` is the neighbour average. That is T3's signed rule with `a = cos θ`, lossless at every wave number.

*Proof.* The characteristic polynomial of a `2×2` matrix vanishes on it. ∎

*Checked (E1).* Symbolically.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 96 as landed: clocked record motion never oscillates; the formation side (block 13's law in level time with the odds as weights) not treated"
source_of_blocker_text: blocks 13 and 96 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the full multi-level classification without the analytic step; the minimal signed rules' stability regions (the attempts' deltoid and blink window); whether any formation clause can carry signed weights"
conditional_surface_status: "T1, T3, T4 exact; T2 with the named imports on nonnegative matrices and one analytic step"
hypothetical_axiom_status: "the formation law and the walk are hypotheses; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 13: the formation law in level time.
  - Block 26: its gain one at `k = 0`, which is the conserved mean and not a wave.
  - Block 54: the walk.
  - Block 96: clocked motion never oscillates. Its line walk is T1's second witness.
- **The probes attempts** `waves-need-signed-weights`, all refereed by a Grok model and confirmed:
  - a1 (issue #8539, referee #9071): the entrywise half of the lemma, without Wielandt;
  - a2 (#8462, #8932): the signed rule and its Green functions;
  - a3 (#8535, #8911): the classification at any depth and any number of components;
  - a4 (#8522, #9055): the transport classification, the signed ladder, the deltoid and the unitary step;
  - a5 (#8516, #9006): mixing and the fronts.

  They were written by Claude Opus 5 (the supervisor's model family).
- **In the literature.**
  - The entrywise lemma is the Perron–Frobenius theory of nonnegative matrices, with Wielandt's equality case.
  - The Schur–Cohn test decides whether all roots lie inside the unit disk.
  - That a positive (stochastic) evolution cannot carry undamped waves, while a signed or unitary one can, is the classical contrast between diffusion and wave propagation. Reference only.
- **New here:**
  - an independent exact runner, with Schur–Cohn certificates at rational angles;
  - the results placed against blocks 13, 54 and 96 as landed.

## Exact target and obligation graph

Target: whether a formation rule with the odds as weights can carry waves, and what the amplitude layer adds. The obligations are:
- (O1) the bound;
- (O2) the classification;
- (O3) signed rules;
- (O4) the walk.

T1–T4 discharge them, with T2's imports named.

## No-Go Discipline Gate

The note's negative sentence: no nonnegative gain-one rule keeps a dispersive undamped branch on an open set of wave numbers.

### N1 — Routes by which the sentence could fail or mislead
1. *Nonlinear rules.* T1–T2 are about the linear law in level time. A nonlinear formation law is not covered.
2. *Gain above one.* Excluded. Such a rule grows.
3. *Signed weights from formation.* A formation clause whose weights can be negative is not a set of odds. T3 shows what such a clause would allow.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
T2's imports are named in Imports: the theory of nonnegative matrices with its equality case, and the attempts' analytic step.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | odds from the admissibility rule; records form; no dynamics in the axioms | yes |
| blocks 13, 54, 96 (landed) | the formation law, the walk, clocked motion | yes (restated) |
| probes (#8462, #8516, #8522, #8535, #8539; Grok-refereed) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "waves need signed weights" | executed: unit-disk certificates for the witnesses | executed: the entrywise lemma on instances | executed: the signed rule's dispersion | executed: the coin walk's identity | T2 for every nonnegative gain-one rule, with named imports; T3–T4 for every wave number; the clauses supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Block 26 found gain-one spin waves in a formation law." *Reply:* Gain one there is the multiplier at `k = 0`, the conserved mean. T2 is about an open set of wave numbers.
- *Objection:* "Persistent records do oscillate." *Reply:* Their density modes can be complex, but they damp. T1's second witness shows that.

### N8 — Cross-cycle echo
- Block 96 found that clocked motion never oscillates.
- This note finds that formation with odds never makes undamped waves either, except by rigid transport.
- The waves the lane has come from signed weights: the amplitude walk.

## Falsifiers

- A nonnegative gain-one rule with a dispersive branch of modulus one on an open set of wave numbers.
- A tested witness with a non-transport root on or outside the unit circle.
- A coin walk whose step fails `U² − (tr U)U + 1 = 0`.

## Boundaries and non-claims

- The formation law and the walk are supplied.
- T2 carries named imports.
- Nonlinear laws are not treated.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 13, 26, 54 and 96, restated or placed.
- The probes attempts, refereed by another model family.
- Named standard imports, at definition level:
  - the Perron–Frobenius theorem and Wielandt's equality case;
  - the Schur–Cohn test;
  - the Cayley–Hamilton identity for `2×2` matrices;
  - exact rational and symbolic arithmetic.
- Reference only: Perron; Frobenius; Wielandt; Schur; Cohn; Cayley; Hamilton.

## Review record

- **Who and when.** Supervisor-run block, the seventieth since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - Five probes attempts by Claude Opus 5 derived the results. Grok referees confirmed them (#8911, #8932, #9006, #9055, #9071).
  - The supervisor re-checked them with its own runner.
- **Before writing.** Main was re-fetched. Blocks 13, 26 and 96 were checked as landed.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_waves_need_signed_weights_nonnegative_rules_keep_an_undamped_branch_only_by_rigid_transport_2026_09_24.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
