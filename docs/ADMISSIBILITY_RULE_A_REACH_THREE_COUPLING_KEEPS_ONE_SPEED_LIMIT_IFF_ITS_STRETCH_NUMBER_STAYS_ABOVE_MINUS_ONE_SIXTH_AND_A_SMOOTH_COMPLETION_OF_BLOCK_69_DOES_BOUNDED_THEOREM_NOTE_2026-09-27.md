---
claim_id: admissibility_rule_a_reach_three_coupling_keeps_one_speed_limit_iff_its_stretch_number_stays_above_minus_one_sixth_and_a_smooth_completion_of_block_69_does_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN blocks 59, 60 and 69 as landed and the ray model of the principal symbol used by block 173 (pushed branch): (T1) at uniform stretch l, every odd coupling of reach at most three along each axis with long-wave speed w/l has the symbol l s_a = sin k_a (1 - q sin^2 k_a), one number q(l); the frame (block 60's crossing) is q = 0 and block 69's linear completion 1 + b = 1/l is q = 1 - l; (T2) for q in [-1/6, 2/3] no wave, in any direction, outruns w/l, and for q < -1/6 waves near the axes do; (T3) for q in [-1/6, 2/3] the bending factor A = l^2 sum n_a^2 (s_a'^2 + s_a s_a'') is at most 1, and for q < -1/6 it exceeds 1 near k = 0; if also 0 <= rho <= 1 (q' <= 0 and 1 - q + l q' >= 0), every ray crossing the one-body gradient bends at most R = 1 + 2w/(w + w0) times a slow body's fall; (T4) the completion q(l) = (1 - l)/sqrt(1 + 36(l - 1)^2) agrees with block 69 at first order in the strain, stays in (-1/6, 1/6), and meets both conditions at every l > 0, so block 69's coupling can be completed with one speed limit and no excess bending. The supervisor's own derivation (Claude Opus 5.5), unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_a_reach_three_coupling_keeps_one_speed_limit_iff_its_stretch_number_stays_above_minus_one_sixth_2026_09_27.py
---

# A reach-three coupling keeps one speed limit iff its stretch number stays above −1/6, and a smooth completion of block 69 does

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 59, 60 and 69 as landed and the principal-symbol ray model; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 59, 60 and 69 as landed on main (the local ray comparison, the one-body field and the reach-three coupling at uniform strain) and places block 173 (a pushed branch); it reports which completions of the reach-three coupling keep one speed limit; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 69 (landed) states that its leading-order coupling does not determine how it continues at finite strain. Block 173 (pushed) showed that the simplest continuation lets stretched regions carry waves faster than the long-wave speed `w/ℓ`. It also lets rays bend more than three times a slow body's fall. This note asks which continuations avoid both.

- **T1: one number.** At uniform stretch, every reach-three coupling with the right long-wave speed has the symbol `ℓs = sin k(1 − q sin² k)`, fixed by one number `q(ℓ)`.
  - The frame is `q = 0`.
  - Block 69's simple continuation is `q = 1 − ℓ`.
- **T2: one speed limit iff `q ≥ −1/6`.** For `q` between `−1/6` and `2/3`, no wave in any direction outruns `w/ℓ`. Below `−1/6`, waves near the axes do.
- **T3: bending within bounds iff `q ≥ −1/6`.**
  - In the same range the bending factor `A` is at most 1, so no ray bends more than the long-wave ratio `R` times the fall, provided `q` does not grow with stretch.
  - Below `−1/6`, `A` exceeds 1.
- **T4: a good continuation exists.** `q(ℓ) = (1 − ℓ)/√(1 + 36(ℓ − 1)²)` agrees with block 69 to first order in the strain and stays between `−1/6` and `1/6` at every stretch. So block 69's coupling can be continued with one speed limit and no excess bending.

In plain terms: the reach-three coupling has one free knob at finite stretch. Block 69 fixes only its slope at zero stretch. Turn the knob too far and short waves outrun the local speed limit; keep it above −1/6 and they never do. A smooth setting of the knob that matches block 69 exactly where block 69 speaks keeps it in range at every stretch.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-27.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The walk, its coupling to the lengths and its continuation are supplied clauses. Nothing is adopted.
- **Block 69 (landed on main).** Quoted by the runner (A3).
  - For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_j c_j]`.
  - "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion."
- **Blocks 59 and 60 (landed).** Block 59 T4 gives the local ratio. Block 60 T4 gives the one-body field, with `R = 1 + 2w/(w + w₀)` its long-wave ratio.
- **Block 173 (pushed branch).**
  - Bending over fall is `A[1 + ρ(R − 1)]`, with `A = ℓ²Σ n_a²(s_a′² + s_a s_a″)` and `ρ = −ℓ∂_ℓ log|s|`.
  - Block 69's continuation `1 + b = 1/ℓ` fails beyond `ℓ = 7/6`.
  - It is placement here: this note re-derives what it uses.
- **"Reach three"** means an odd trigonometric polynomial of degree at most three in each `k_a`, the same at every corner (block 69's species-blind property).

## Domain qualifications

- The ray model of the principal symbol, as in block 173.
- The family of T1; couplings of longer reach are not treated.
- `q` in `[−1/6, 2/3]` for the positive statements; `q > 2/3` is not needed by the completions here.
- These are conditional statements within supplied clauses, not a physical identification.

## Theorem T1 — one number

*Statement.*
- The odd symbols of reach at most three along an axis are the combinations of `sin k` and `sin k cos² k`, equivalently of `sin k` and `sin 3k`.
- With slope `1/ℓ` at `k = 0` (long-wave speed `w/ℓ`) they are `ℓs = sin k(1 − q sin² k)`.
- The frame is `q = 0`. Block 69's linear continuation, `B = b` isotropic with `1 + b = 1/ℓ`, is `q = 1 − ℓ`.

*Proof.* `sin 3k = sin k(4cos² k − 1)`. The slope at 0 fixes one combination, and the rest follows by substitution (B1). ∎

## Theorem T2 — one speed limit iff `q ≥ −1/6`

*Statement.*
- Along an axis, the group speed in units of `w/ℓ` is `cos k(1 − 3q sin² k)`. Its square is `(1 − x)(1 − 3qx)²`, with `x = sin² k`.
- `1 − speed² = x S(x, q)`, with `S = 9q²x² − 9q²x − 6qx + 6q + 1`.
- For `q` in `[−1/6, 2/3]`, `S ≥ 0` on `[0, 1]`, so no axis wave outruns `w/ℓ`.
- In any direction `|∇_k|s|| ≤ max_a |s_a′|`, so no wave outruns `w/ℓ` in any direction.
- For `q < −1/6` the speed is `1 − (1/2 + 3q)k² + …`, which exceeds 1 near `k = 0`.

*Proof.*
- `S(0) = 6q + 1 ≥ 0`, `S(1) = 1`, and the vertex of the quadratic in `x` is at `1/2 + 1/(3q)`.
  - For `q` in `(0, 2/3]` the vertex is at least 1.
  - For `q` in `[−1/6, 0)` it is at most 0.
  - For `q = 0`, `S = 1`.
  - So the minimum on `[0, 1]` is at an end, where `S ≥ 0` (C1).
- `|∇_k|s||² = Σ(s_a s_a′)²/|s|² ≤ max s_a′²` (C1). ∎

## Theorem T3 — bending within bounds iff `q ≥ −1/6`

*Statement.*
- Per axis, `A_a = ℓ²(s_a′² + s_a s_a″) = 1 − x P(x, q)`, with `P = 18q²x² − 15q²x − 16qx + 12q + 2`.
- For `q` in `[−1/6, 2/3]`, `P ≥ 0` on `[0, 1]`, so `A_a ≤ 1`. The bending factor `A`, a weighted mean of the `A_a`, is at most 1 for every carrier crossing the gradient.
- `A_a = 1 − (2 + 12q)k² + O(k⁴)`, which exceeds 1 near `k = 0` iff `q < −1/6`: the same threshold as T2.
- `ρ_a = 1 + ℓq′x/(1 − qx)`. It lies in `[0, 1]` when `q′ ≤ 0` and `1 − q + ℓq′ ≥ 0`.
- With `A ≤ 1`, `0 ≤ ρ ≤ 1` and `R ≥ 1`, bending over fall `A[1 + ρ(R − 1)]` is at most `R`.

*Proof.*
- `P(0) = 12q + 2 ≥ 0`, and `P(1) = 3q² − 4q + 2 > 0` (negative discriminant). The vertex is at `5/12 + 4/(9q)`: at least 1 for `q` in `(0, 2/3]`, at most 0 for `q` in `[−1/6, 0)`. So `P ≥ 0` on `[0, 1]` (D1).
- `A` and `ρ` are weighted means of the per-axis values, with weights `n_a²` and `s_a²/|s|²`.
- `R − A[1 + ρ(R − 1)] = (1 − A)(1 + ρ(R − 1)) + (1 − ρ)(R − 1) ≥ 0` (D1). ∎

## Theorem T4 — a good continuation exists

*Statement.* The continuation `q(ℓ) = (1 − ℓ)/√(1 + 36(ℓ − 1)²)`:
- agrees with block 69 at first order in the strain: `q = (1 − ℓ) + 18(ℓ − 1)³ + …`;
- stays in `(−1/6, 1/6)` for every `ℓ > 0`;
- has `q′ = −(1 + 36(ℓ − 1)²)^{−3/2} < 0`;
- satisfies `1 − q + ℓq′ ≥ 0` for every `ℓ > 0`.

So by T2 and T3 no wave outruns `w/ℓ` and no ray bends more than `R` times the fall, at every stretch.

*Proof.*
- Series, limits and derivative are exact (E1).
- With `v = ℓ − 1` and `w = √(1 + 36v²) ≥ 1`: `(1 − q + ℓq′)w³ = w²(w + v) − (1 + v)`.
- Since `w ≥ 1` and `w + v ≥ 1 + v > 0` for `ℓ > 0`, this is at least `(w + v) − (1 + v) ≥ 0` (E1). ∎

## What this settles and what it does not

- **Settled.** Within the reach-three family and the ray model:
  - one speed limit, and bending within the long-wave ratio, hold exactly when `q ≥ −1/6` (with `q ≤ 2/3` and `ρ` in `[0, 1]`);
  - block 69's simplest continuation fails beyond `ℓ = 7/6`;
  - a smooth continuation agreeing with block 69 at first order never fails.
- **For the owner.** Block 173's flag is not a verdict on block 69's coupling, only on one continuation of it. The continuation remains a supplied choice, now with an explicit admissible range.
- **Not settled.**
  - What would fix the continuation: a dynamics, or a further clause.
  - Couplings of longer reach.
  - Sub-principal terms.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 69 N1: the leading order does not determine a nonlinear completion; block 173 (pushed): the linear completion carries faster waves beyond l = 7/6"
source_of_blocker_text: blocks 69 and 173
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; a clause or dynamics that fixes the completion; couplings of longer reach"
conditional_surface_status: "the reach-three family at uniform stretch; the principal-symbol ray model"
hypothetical_axiom_status: "the walk, its coupling to the lengths and its completion are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 69 (landed): the coupling at first order, and its open completion.
  - Block 173 (pushed; a harvest of #9018 with #9341): the linear completion's fast waves and excess bending.
- **In the literature.** Lattice dispersions with bounded group velocity, and the use of low-order trigonometric polynomials as symbols, are standard. The threshold here is elementary.
- **New here.** The one-number form of every reach-three completion, the exact admissible range `q ≥ −1/6` for both properties, and a smooth completion that meets it.
- **Provenance.** The supervisor's own derivation, the same family as block 173's finder. No other-family check yet.

## Exact target and obligation graph

Target: which completions of the reach-three coupling keep one speed limit. The obligations are:
- (O1) the premises (A3);
- (O2) the family (B1);
- (O3) speed (C1);
- (O4) bending (D1);
- (O5) a completion (E1).

## No-Go Discipline Gate

The note's negative sentence: every completion with `q < −1/6` carries waves faster than `w/ℓ` near the axes, and bends rays more than the long-wave ratio.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *Some reach-three completion outside the family.* The family is all odd reach-three symbols with the right long-wave speed (T1). ATTEMPTED.
2. *Fast waves off the axes only.* The group speed in any direction is bounded by the axis speeds (T2). ATTEMPTED.

Scope left open: longer reach; sub-principal terms.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The family, the range of `q` and the ray model are declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 69 (landed) | the coupling and its open completion | yes (quoted, A3) |
| blocks 59, 60 (landed) | the local ratio and the one-body `R` | yes (restated) |
| block 173 (pushed) | the flag this note answers | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "one speed limit and bounded bending iff `q ≥ −1/6`; a smooth completion of block 69 meets it" | executed: the family and its number `q` | executed: speed and bending polynomials on the box | executed: the long-wave expansions and the threshold | executed: the completion's series, bounds and inequalities | not executed: longer reach; sub-principal terms |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "The continuation is arbitrary; picking a good one proves nothing."
  - *Reply:* The note proves the exact range, and that it contains continuations agreeing with block 69 where block 69 speaks.
  - It does not claim the continuation is fixed; that remains open.

### N8 — Cross-cycle echo
- Block 69: the coupling at first order.
- Block 173: a bad continuation.
- This note: the admissible range and a good continuation.

## Falsifiers

- A `q` in `[−1/6, 2/3]` and a wave number with axis speed above `w/ℓ`.
- A `q` in `[−1/6, 2/3]` with `A_a > 1` somewhere.

## Boundaries and non-claims

- The reach-three family at uniform stretch; the principal-symbol ray model.
- The walk, its coupling and its continuation are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 69 (landed), restated and quoted. Blocks 59 and 60 (landed), restated. Block 173 (pushed), placed.
- Named standard imports, at definition level:
  - trigonometric identities;
  - elementary bounds for quadratics on an interval;
  - series and limits;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.** The supervisor's own derivation, written after harvesting block 173. It is unrefereed, and a referee should come from another family.
- **Before writing.** Origin was re-fetched. Block 69 was read as landed. Block 173 was re-read on its branch. The own prior-art check covered memory, the held branches and the probes tasks. It found no completion analysis of the reach-three coupling.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_reach_three_coupling_keeps_one_speed_limit_iff_its_stretch_number_stays_above_minus_one_sixth_2026_09_27.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
