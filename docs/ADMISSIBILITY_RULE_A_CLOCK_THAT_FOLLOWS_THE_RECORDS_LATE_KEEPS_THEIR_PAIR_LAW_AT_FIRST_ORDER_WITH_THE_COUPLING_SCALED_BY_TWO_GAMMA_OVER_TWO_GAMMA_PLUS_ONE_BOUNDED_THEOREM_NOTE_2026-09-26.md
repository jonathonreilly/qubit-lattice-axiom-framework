---
claim_id: admissibility_rule_a_clock_that_follows_the_records_late_keeps_their_pair_law_at_first_order_with_the_coupling_scaled_by_two_gamma_over_two_gamma_plus_one_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 95's records as landed (one per site on a finite torus, a move x -> y onto an empty neighbour at rate exp[a u_x + (1 - a) u_y] h/q, h = W(C')/(W(C) + W(C')), q = 2d), with the supplied clause that the clock field relaxes towards the records, du_z/dt = Gamma w_z ((M u)_z + lambda (n_z - nbar)), M = Adj/q - I, lambda = log kappa, and under two stated assumptions, A0 (the joint process is well posed and has the needed stationary laws) and A1 (its stationary law is differentiable at lambda = 0): (T1) sum_z 1/w_z is conserved exactly, and for a fixed configuration the field settles to the slaved field lambda q sum_r G(. - r) plus a constant; (T2) at a = 1, W = 1 a record's steps are uniform whatever the field, and two records' separation jumps as the simple random walk on the torus minus the origin at every Gamma and lambda, so the pair law is set by mean sojourn times; (T3) given A1, at first order in lambda the mean field given the records is gamma times the slaved field, gamma = Gamma/(Gamma + r0 q) = 2 Gamma/(2 Gamma + 1) with r0 = 1/(2q), and the record law is block 95's with lambda -> gamma lambda (on ring 6 the pair weights are -1/3, 1/6, 1/3 times gamma lambda); (T4) given A0, for lambda != 0 and finite Gamma no stationary law is a product of a record law and a field law; (T5) given A0, no stationary law of the joint process is reversible. A harvest of probe #9158 (Claude Opus 5.5, the supervisor's family), confirmed by an other-family referee (#9325, Grok). A0 and A1 are not proved. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_with_a_one_over_r_potential_equal_both_ways_bounded_theorem_note_2026-09-23
runner: scripts/admissibility_rule_a_clock_that_follows_the_records_late_keeps_their_pair_law_at_first_order_2026_09_26.py
---

# A clock that follows the records late keeps their pair law at first order, with the coupling scaled by 2Γ/(2Γ + 1)

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 95's records and a supplied relaxation clause, conditional on two stated assumptions; a harvest of probe #9158, confirmed by an other-family referee in #9325; nothing adopted or registered; unaudited)

This note works within block 95 as landed on main (records moving on their own clocks, with the slaved clock field) and adds the supplied clause that the clock field relaxes towards the records at a finite rate; it reports what survives of block 95's pair law and what the delay changes; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 95 (landed) found the records' pair law when the clock field follows the records at once, and it states that delayed clocks are absent there. This note is a harvest of a probe result that another model family has confirmed. It lets the field lag, relaxing towards the records at a rate `Γ`.

- **T1: what the delay keeps.** `Σ_z 1/w_z` is conserved exactly. For a fixed configuration the field settles to block 95's slaved field, with its level set by this invariant rather than by a zero mean.
- **T2: the separation still walks.** With departure timing (`a = 1`) and `W = 1`:
  - a record's steps are uniform whatever the field;
  - two records' separation jumps as the simple random walk on the torus minus the origin, at every `Γ` and `λ`.

  So the field enters only through waiting times, and the pair law is fixed by the mean sojourn times.
- **T3: the pair law at first order.** At first order in `λ = log κ`:
  - the mean field given the records is `γ` times the slaved field, with `γ = 2Γ/(2Γ + 1)`;
  - the records' law is block 95's with `λ` replaced by `γλ`.

  So a lagging clock keeps the pair law and weakens it by `γ = 1 − 1/(2Γ) + …`.
- **T4: no product law.** For `λ ≠ 0` and finite `Γ`, no stationary law has the records and the field independent.
- **T5: no reversibility.** No stationary law of the joint process is reversible.

T3 needs assumption A1, and T1's settling, T4 and T5 need A0. Both are stated below and not proved.

In plain terms: if the clocks around a record catch up only gradually, records still gather as block 95 found, but less strongly. The factor is `2Γ/(2Γ + 1)`, near one when the clocks keep up fast. The records and their clocks can never be treated as independent, and the joint motion has a direction in time.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The records' rates, the field and its relaxation are supplied clauses. Nothing is adopted.
- **Block 95 (landed on main).** Quoted by the runner (A3).
  - The rates: a move `x → y` onto an empty neighbour at rate `exp[a u_x + (1 − a)u_y] h/q`, with `h = W(C′)/(W(C) + W(C′))`.
  - The slaved law: `π(C) ∝ W(C) exp[qλ(1 − 2a) Σ_pairs G]`.
  - At `a = 1`, `W = 1`, every allowed hop has rate `w_x/(2q)`.
  - Block 95 states delayed clocks are absent. It is stated for `d = 3`, `q = 6`; its arguments and this note hold on any `(ℤ/L)^d`, `L ≥ 3`.
- **Objects.**
  - `Δ = qI − Adj`, `M = Adj/q − I`.
  - `G` solves `ΔG = δ₀ − 1/V` with `Σ G = 0`.
  - `N` records, `1 ≤ N ≤ V − 1`, with occupation `n_C` and `n̄ = N/V`.
  - `w = e^u`, and `r₀ = 1/(2q)`.
- **The relaxation clause (supplied).**
  - `du_z/dt = Γ w_z((Mu)_z + λ(n_z − n̄))`.
  - Block 57 (landed) finds that neighbour-referred motion of the rate field does not propagate a delay, so this first-order relaxation is a separate supplied clause.
  - The joint process is piecewise deterministic: the field follows the flow of the current configuration, and the records jump at block 95's rates evaluated at the current field.
- **Assumptions, not proved here.**
  - **A0 (well-posedness).** The joint process does not explode, and its generator formula holds for the test functions used (Dynkin's formula). Where needed, a stationary law exists on each level set of `Σ 1/w`, with finite moments of `w` and `u`, and long-run averages equal its expectations.
  - **A1 (first order).** On the level set `Σ 1/w = V`, the stationary law is weakly differentiable in `λ` at `0`, and `(C, u/λ)` tends to the `λ = 0` joint law.
- **Sign.** The probe task paraphrased block 95's law with the opposite sign. The landed sign is used.
- **Names.** The generator formula is Dynkin's. The decrease of `E_C` with the invariance principle is LaSalle's.

## Domain qualifications

- The torus is finite, `(ℤ/L)^d` with `L ≥ 3`, and `0 < Γ < ∞`.
- T2 is for departure timing and `W = 1`. T3 holds for every `a`, with `W = 1`. T4 and T5 hold for every `a` and every positive `W`.
- T3 is first order in `λ`, exact in `Γ`.
- These are conditional statements within supplied clauses, not a physical identification.

## Theorem T1 — what the delay keeps

*Statement.*
- `S(u) = Σ_z 1/w_z` is constant along every path, for every `Γ`, `λ`, `a`, `W` and `N`.
- For a fixed configuration `C`, the flow is `Γ w ⊙ M(u − u*(C))`, with `u*(C) = λφ*(C) + const` and `φ*(C) = q Σ_{r∈C} G(· − r)`. The constant is the one that keeps `S`.
- `E_C = ½⟨u − u*, −M(u − u*)⟩` decreases: `dE_C/dt = −Γ Σ_z w_z ((M(u − u*))_z)² ≤ 0`. So the field settles to `u*(C)`.

*Proof.*
- `d/dt Σ e^{−u_z} = −Γ[Σ_z (Mu)_z + λ Σ_z(n_z − n̄)] = 0`, since `M` has zero column sums and `Σ n = N` (B1). Jumps do not move `u`.
- `Mφ*(C) = −(n_C − n̄)` from `ΔG = δ₀ − 1/V` (B2).
- The derivative of `E_C` along the flow is computed directly (B3). A bounded `E_C` bounds the oscillation of `u − u*`, and the invariant bounds its level. So the settling follows by the invariance principle named under the premises. ∎

## Theorem T2 — the separation still walks

*Statement* (`a = 1`, `W = 1`).
- A record at `x` hops to each empty neighbour at rate `r₀w_x`, so its steps are uniform over its empty neighbours whatever the field.
- For two records with separation `D = x₂ − x₁ ≠ 0`:
  - a hop of record 1 by `e ≠ D` sends `D` to `D − e`;
  - a hop of record 2 by `e ≠ −D` sends `D` to `D + e`;
  - each map reaches every nonzero neighbour of `D` exactly once.
- So the separation's jump chain is the simple random walk on the torus minus the origin, at every `Γ` and `λ`.
  - Its stationary law is `ν(D) ∝ deg(D)`.
  - Given A0, the time-stationary pair law is `ν(D)τ̄(D)/Σ ντ̄`, where `τ̄(D)` is the mean sojourn per visit.

*Proof.* The maps are bijections onto the nonzero neighbours (C1, on rings of sides 3–6, the `3 × 3` and `4 × 4` tori and `3³`). Given a hop, both records' clocks enter only through which record moves, and each record's move is uniform. ∎

## Theorem T3 — the pair law at first order

*Statement* (given A1; any `a`, `W = 1`).
- Write `u = λφ` and let `P₀` be the `λ = 0` stationary law. Then `E₀[φ | C] = γφ*(C)`, with `γ = Γ/(Γ + r₀q) = 2Γ/(2Γ + 1) = 1 − 1/(2Γ) + 1/(4Γ²) − …`.
- The record law at `O(λ)` is `π₀(1 + qγλ(1 − 2a)(P(C) − P̄))`, with `P = Σ_pairs G`. This is block 95's law with `λ → γλ`.
- On ring 6 at `a = 1`, the pair weights at separations `1, 2, 3` are `−1/3, 1/6, 1/3` times `γλ`.

*Proof.*
- At `λ = 0` the records do symmetric exclusion at rate `r₀` per bond, and the rescaled field obeys `dφ/dt = Γ(Mφ + n_C − n̄)`.
- The generator formula for `f = 1{C = C₀} φ_z` gives the moment system `Γ[M m(C₀) + π₀(n_{C₀} − n̄)] + r₀ Σ_{C∼C₀}(m(C) − m(C₀)) = 0`, with `m(C) = E₀[φ 1{C}]`.
- `m(C) = π₀γφ*(C)` solves it. This follows from `Mφ* = −(n − n̄)` and the exclusion identity `Σ_{C∼C₀}(n_C − n_{C₀}) = −Δn_{C₀}`.
  - The runner checks it exactly on rings 5 and 6 and the `3 × 3` torus, for `N = 1, 2` and `Γ = 1/3, 1, 5/2` (D1).
  - The controls `γ = 1` and `γ = Γ/(Γ + 1)` fail in every case.
- The operator `ΓM ⊗ I + I ⊗ Q₀` has only the constants as kernel (D2), and `Σφ = 0` fixes the solution.
- The records' master equation at `O(λ)`, with this `m`, is solved by block 95's law at coupling `γλ`, for `a = 1, 1/2, 0` on ring 6 (D3). ∎

## Theorem T4 — no product law

*Statement* (given A0). Let `λ ≠ 0`, `0 < Γ < ∞`, `1 ≤ N ≤ V − 1`, any `a` and any positive `W`. Then no stationary law has the form `μ(C) Q(du)`, for any probability measure `Q`.

*Proof.*
1. **`Q` lies on a line.**
   - Let `ρ = Σ μ(C) n_C`, and let `u_ρ` solve `Mu_ρ = −λ(ρ − n̄)`.
   - Test functions of `E_ρ = ½⟨u − u_ρ, −M(u − u_ρ)⟩` and of the invariant `S` give `∫ h′(E_ρ)ψ(S) Σ_z w_z((M(u − u_ρ))_z)² dQ = 0`.
   - So `Q` is carried by the line `u_ρ + ℝ1`.
2. **One configuration.**
   - On that line the drift of configuration `C` is `Γλe^c w_ρ ⊙ (n_C − ρ)` (E1).
   - Test functions linear across the line then force `w_ρ ⊙ (n_C − ρ)` to be a multiple of `1` for every supported `C`.
   - Since `Σ(n_C − ρ) = 0` and `w_ρ > 0`, the multiple is `0` (E1). So `n_C = ρ`, and `μ` is a single configuration.
3. **Escape.** Some record of that configuration has an empty neighbour, and its escape rate is positive. The probability of that configuration then decreases, which contradicts stationarity. ∎

## Theorem T5 — no reversibility

*Statement* (given A0). For `λ ≠ 0` and every finite `Γ > 0`, no stationary law of the joint process is reversible.

*Proof.*
- Forward paths satisfy `u(t) − u(0) = ∫₀ᵗ F(C_s, u_s) ds`, with `F = Γw ⊙ (Mu + λ(n_C − n̄))`. Time-reversed paths satisfy the same with `−F`.
- Equality in law therefore forces `F = 0` along almost every path.
- Then `u` is constant, and `λ(n_C − n_{C′}) = 0` for two configurations visited with positive probability. So `λ = 0`. ∎

## What this settles and what it does not

- **Settled** (given A0, A1). A lagging clock keeps block 95's pair law at first order, weakened by `2Γ/(2Γ + 1)`. It never gives a product law or a reversible one.
- **For landed block 95.** Its slaved law is the `Γ → ∞` case at first order. This note does not prove that the relaxing process's stationary law tends to block 95's slaved law as `Γ → ∞` at every order.
- **Not settled.**
  - A0 and A1.
  - Orders beyond the first in `λ`.
  - The one-record hop rate beyond first order.
  - The attempt's quasi-static limit, which assumes averaging.
- **Not ported.** The attempt's one-record rate `R/R_∞ = 1 − qλG(0)/(2Γ + 1) + O(λ²)`, its rate-weighted identity, and its direct simulation (floating point).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 95 as landed: delayed clocks are absent; does its pair law survive a clock that follows the records late?"
source_of_blocker_text: probes task J:derive:the-delayed-clock-and-the-pair-law
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "well-posedness (A0) and differentiability (A1); second order in lambda; the limit Gamma -> infinity at every order"
conditional_surface_status: "finite tori; the supplied relaxation clause; A0 and A1 assumed; first order in lambda for T3"
hypothetical_axiom_status: "the records' rates, the field and its relaxation are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 95 (landed): the slaved law.
  - Block 53 (landed): the clock clause and the departure-timed walker.
  - Block 57 (landed): neighbour-referred motion of the rate field does not propagate.
- **Probes.**
  - #9158, worker `w-macbookpro9927a-j0e51`, Claude Opus 5.5, the supervisor's own model family, found T1–T5. It also found the one-record rate and the quasi-static limit, which are not harvested here.
  - Attempt a2 of the same problem (#8887, by a Grok worker) failed at its step S3 in review. It treated product laws only for point masses.
  - #9325, worker `w-macbookpro90c72-jc3d1`, `grok-4.6`, another model family, refereed #9158 with its own checker: "HIT: confirmed - no stationary product law exists at finite Gamma when log kappa is nonzero, the separation is a simple random walk off the origin, and the first-order clock field is slaved with factor 2 Gamma/(2 Gamma+1)." It noted that well-posedness and differentiability at `λ = 0` were not proved.
- **In the literature.** Piecewise-deterministic Markov processes, and the generator formula (Dynkin), are standard. Symmetric exclusion (stirring) is standard. LaSalle's invariance principle is used for the settling.
- **New here.**
  - The harvest.
  - A new exact runner.
  - The wrong-`γ` controls on four tori.
  - The `O(λ)` master equation checked for three timings.
- **Provenance.** Found by the supervisor's family and confirmed by another family.

## Exact target and obligation graph

Target: block 95's records with a lagging clock. The obligations are:
- (O1) the premises (A3);
- (O2) the invariant and the settling (B1–B3);
- (O3) the jump chains (C1);
- (O4) first order (D1–D3);
- (O5) no product law (E1, with the argument);
- (O6) no reversibility (the argument).

## No-Go Discipline Gate

The note's negative sentences:
- no stationary product law for `λ ≠ 0` at finite `Γ`;
- no reversible stationary law.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *A field law not concentrated on a point.* T4 covers every probability measure `Q`, not only point masses; this was attempt a2's gap. ATTEMPTED.
2. *Reversibility up to a time change.* The reversed path's flow has the opposite sign, which a time change cannot undo. ATTEMPTED.

Scope left open: A0 and A1.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- A0, A1 and the relaxation clause are declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 95 (landed) | the rates and the slaved law | yes (quoted, A3) |
| block 57 (landed) | the relaxation clause is separate from kinetic terms | placement |
| probe #9158 and referee #9325 | the result and its confirmation | yes (re-derived, rerun exactly) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the pair law at first order with `γλ`; no product law; no reversibility" | executed: the invariant and `E_C`'s decrease | executed: the slaved equilibrium; the separation maps on seven tori | executed: the moment system with controls; the operator's rank | executed: the `O(λ)` law for three timings; ring-6 weights; the drift on the line | not executed: A0 and A1; higher orders |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "With a lag the attraction should vanish."
  - *Reply:* At first order it survives at every finite `Γ`, weakened by `2Γ/(2Γ + 1)`. The lag changes the strength, not the form.
- *Objection:* "A product law might hold for a spread-out field law."
  - *Reply:* T4 excludes every field law.

### N8 — Cross-cycle echo
- Block 95: the slaved clock.
- This note: the lagging clock.

## Falsifiers

- A torus, `N` and finite `Γ` for which the first-order moment system has a solution other than `π₀γφ*` with zero field sum.
- A stationary product law for `λ ≠ 0` at finite `Γ`, under A0.

## Boundaries and non-claims

- Finite tori; the supplied relaxation clause; A0 and A1 assumed.
- The records' rates and the field are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 95 (landed), restated and quoted. Blocks 53 and 57 (landed), placed.
- Named standard imports, at definition level:
  - Dynkin's formula for piecewise-deterministic processes (under A0);
  - LaSalle's invariance principle;
  - the symmetric exclusion process;
  - exact rational and symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run harvest block (Claude Opus 5.5), 2026-09-26, during the owner's 12-hour campaign.
- **Provenance.**
  - Probe #9158 (Claude Opus 5.5) was refereed by #9325 (`grok-4.6`, another family).
  - The supervisor wrote a new exact runner and did not port the attempt's floating-point simulation.
- **Before writing.** Origin was re-fetched. Block 95 was read as landed. The own prior-art check covered memory (block 95 is the supervisor's, PR #8860), open PRs and main. It found no earlier delayed-clock result.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_clock_that_follows_the_records_late_keeps_their_pair_law_at_first_order_2026_09_26.py
```

Expected: `TOTAL: PASS=16 FAIL=0`.
