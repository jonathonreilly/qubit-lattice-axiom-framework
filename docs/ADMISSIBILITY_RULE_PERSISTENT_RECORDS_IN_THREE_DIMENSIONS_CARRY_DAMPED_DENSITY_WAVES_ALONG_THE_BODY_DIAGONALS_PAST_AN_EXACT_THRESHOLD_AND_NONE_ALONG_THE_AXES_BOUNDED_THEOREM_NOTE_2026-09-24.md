---
claim_id: admissibility_rule_persistent_records_in_three_dimensions_carry_damped_density_waves_along_the_body_diagonals_past_an_exact_threshold_and_none_along_the_axes_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "WITHIN block 96's direction-memory motion as landed on main (a record keeps its direction with probability p and otherwise turns to one of the other five; the mode matrix M(k) = E(k) T with T = p I + q (J - I), q = (1 - p)/5, E = diag(e^(-i k.d)) over the six directions; p in (1/6, 1), a = p - q = (6p - 1)/5 > 0), supplied. Exact: (T1) along an axis det(lambda - M) = (lambda - a)^3 P(lambda) with P an explicit cubic in c = cos kappa; the density branch is the unique root of P above a, real and simple at every kappa, and the leading multiplier is real at every kappa. (T2) along the body diagonal det(lambda - M) = (lambda - a z)^2 (lambda - a/z)^2 Q(lambda), Q = lambda^2 - 2 lambda c (3p + 2)/5 + (6p - 1)/5, and the density branch is complex exactly when |sin kappa| > 3(1 - p)/(3p + 2), a threshold inside the zone iff p > 1/6 and below the line's (1 - p)/p by 2(1 - p)/(p(3p + 2)); there the leading multiplier leaves the real line. (T3) the diagonal threshold is kappa* = 3 eps/5 + 9 eps^2/25 + 63 eps^3/250 + ... with eps = 1 - p, and it reproduces block 96's executed 24^3 grid. (T4) every such density branch is damped (modulus below one away from k = 0). Harvest block from a Grok-refereed probes attempt, re-checked by an independent runner. General directions and whether the diagonal is extremal are not claimed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_persistent_records_in_three_dimensions_carry_damped_density_waves_along_the_body_diagonals_and_none_along_the_axes_2026_09_24.py
---

# Persistent records in three dimensions carry damped density waves along the body diagonals past an exact threshold, and none along the axes

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 96's direction-memory motion as landed; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within block 96's direction-memory motion of records, as landed on main; it reports where in three dimensions the density branch of persistent records turns complex, along the axes and along the body diagonals, and that the resulting density waves are damped; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 96, as landed, found the threshold on a line: a persistent record's density multiplier turns complex when `|sin k| > (1 − p)/p`. In three dimensions it gives only one executed fixture. This note settles the axes and the body diagonals exactly.

- **T1: along the axes, never.**
  - The characteristic polynomial factorises as `(λ − a)³P(λ)`.
  - The density branch is the unique root of `P` above `a`. It is real and simple at every wave number.
  - The leading multiplier is real everywhere along the axes: no density wave ever appears there.
- **T2: along the body diagonals, past an exact threshold.**
  - The polynomial factorises as `(λ − az)²(λ − a/z)²Q(λ)`.
  - The density branch turns complex exactly when `|sin κ| > 3(1 − p)/(3p + 2)`. That is below the line's threshold `(1 − p)/p`, and inside the zone whenever `p > 1/6`.
- **T3: long memory.** As `p → 1` the diagonal threshold is `κ* ≈ 3(1 − p)/5`. So density waves reach down to wave numbers of order `1 − p`. The formula reproduces block 96's executed grid.
- **T4: damped.** Every such density branch has modulus below one away from `k = 0`, as block 122 requires of any rule with nonnegative weights.

In plain terms, records that tend to keep going the way they were going can make the density of records ripple, but only in some directions. Along the lattice axes the density never ripples. It only relaxes. Along the long diagonals it ripples once the wavelength is short enough, and the more stubborn the records, the longer the ripples can be. Every such ripple dies away. So persistent records give damped, direction-dependent density ripples, not sound. That fits the rest of the waves thread: undamped waves need signed weights (block 122).

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "A site never carries more than one record; records are permanent." Records move under the owner's reading, which is supplied.
  - "Each site has a domain of local possibilities." Here that is the direction a record carries.
  - "Admissibility is not a dynamics axiom." The persistent motion is a supplied clause. Nothing is adopted.
- **The motion** (block 96 T2 as landed).
  - A record keeps its direction with probability `p`, and otherwise turns to one of the other five.
  - The mode matrix is `M(k) = E(k)T`, with `T = pI + q(J − I)`, `q = (1 − p)/5`, and `E = diag(e^{−ik·d})` over `d = ±e_j`.
  - `a = p − q = (6p − 1)/5`, and `p ∈ (1/6, 1)` so that `a > 0`.
  - `c = cos κ` and `z = e^{−iκ}`. Along an axis `k = (κ, 0, 0)`; along the body diagonal `k = κ(1, 1, 1)`.
- **The density branch** is the multiplier equal to 1 at `k = 0`.

## Theorem T1 — along the axes the density branch is real and leads

*Statement.*
- `det(λ − M) = (λ − a)³P(λ)`, where `P = λ³ − ((10cp + 2p + 3)/5)λ² + (6p − 1)(2cp + 8c + 4p + 1)λ/25 − (6p − 1)²/25`.
- At every `κ`, `P` has exactly one root above `a`. It is simple, and it is the density branch.
- The leading multiplier is real at every `κ`.

*Proof.*
- **The factor `(λ − a)³`.** It comes from the vectors supported on the four transverse directions with zero sum.
- **The root above `a`.** Write `P = (λ − a)D(1 − qG)`, with `D = λ² − 2aλc + a²` and `G` the secular function.
  - `D² − N² = (1 − c²)(λ² − a²)²`, where `N = λ²c − 2aλ + a²c`, so `|N| ≤ D`.
  - Hence `G′ ≤ −2/(λ − a)² < 0` on `(a, ∞)`, and `G = 1/q` has one simple solution there.
  - At `κ = 0` it is 1; by continuity it is the density branch for all `κ`.
- **The leading multiplier.** Write `a = t³`.
  - The bracket of `P(t²)` is linear in `c`. It equals `5(t − 1)³(t + 1)` at `c = 1` and `(5/3)(t − 1)(t + 1)(t² + 4t + 1)` at `c = −1`. Both are negative on `(0, 1)`.
  - So the density root exceeds `a^{2/3}`, and any complex pair of `P` has modulus `√(a²/r) < r`.
  - The factor `(λ − a)³` lies below it too. ∎

*Checked (B1).*
- The factorisation against the full `6×6` determinant, symbolic in `p` and `z`.
- The monotonicity identity and `P(a) = −8qa²(1 − c)`.
- The two bracket values, and that the bracket is linear in `c`.

## Theorem T2 — along the body diagonals the density branch turns complex past an exact threshold

*Statement.*
- `det(λ − M) = (λ − az)²(λ − a/z)²Q(λ)`, where `Q = λ² − 2λc(3p + 2)/5 + (6p − 1)/5`.
- The density branch is complex exactly when `|sin κ| > 3(1 − p)/(3p + 2)`.
- This threshold is inside the zone iff `p > 1/6`, and it is below the line's `(1 − p)/p` by `2(1 − p)/(p(3p + 2))`.
- Where it is complex, its modulus `√a` exceeds the modulus `a` of the other four multipliers. So the leading multiplier leaves the real line exactly there.

*Proof.*
- The sum-zero vectors inside the triples `{+e_j}` and `{−e_j}` give the first factors.
- `Q`'s quarter-discriminant is `[9(1 − p)² − sin²κ(3p + 2)²]/25`, because `(3p + 2)² − 5(6p − 1) = 9(1 − p)²`.
- The product of `Q`'s roots is `a`. ∎

*Checked (C1).* The factorisation, the discriminant identity, the edge value `p = 1/6`, and the gap to the line.

## Theorem T3 — long memory

*Statement.*
- With `ε = 1 − p`, `κ* = arcsin(3ε/(5 − 3ε)) = 3ε/5 + 9ε²/25 + 63ε³/250 + …`, so the memory length per coordinate is about `5/(3ε)`.
- On block 96's `24³` grid (`κ = nπ/12`):
  - at `p = 9/10` and `99/100` the first diagonal point is already past the threshold;
  - at `p = 1/2` the first point is below it and the second is past it.

*Proof.* Expand. Compare with `sin(π/12) = (√6 − √2)/4` exactly. ∎

*Checked (D1).* Symbolically and exactly.

## Theorem T4 — the density waves are damped

*Statement.*
- On the line (block 96 T2.1), the density multiplier `μ² − 2p cos k μ + (2p − 1)` is complex exactly when `|sin k| > (1 − p)/p`.
- The diagonal's density branches have modulus below one away from `k = 0`: `√a` when complex, and inside the unit interval when real.

*Proof.* The quarter-discriminant `(1 − p)² − p² sin²k` settles the line. For the diagonal, use the product of `Q`'s roots, and block 122 T1. ∎

*Checked (E1).* The line's identity; the damping at `p = 1/2, 9/10, 99/100` and three angles, exactly.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 96 as landed: T2 treats direction memory by one executed fixture at (pi/2, 0, 0) and the line; the three-dimensional threshold is not stated"
source_of_blocker_text: block 96 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "every direction in the coordinate planes and whether the body diagonal is extremal (a second attempt treats them, unrefereed); p <= 1/6"
conditional_surface_status: "T1-T4 exact along the axes and the body diagonals for p in (1/6, 1)"
hypothetical_axiom_status: "the persistent motion is a hypothesis; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 96: the direction-memory matrix, the line threshold and one fixture.
  - Block 122: every nonnegative gain-one rule damps.
- **The probes attempt.** `the-persistent-record-threshold-in-3d` a1 (Claude Opus 5.5, issue #8884) found T1–T3. A Grok referee confirmed it (#9096).
  - A second attempt (#8988) treats every direction in the coordinate planes and the long-memory limit in every direction. It is not refereed and is not used here.
- **In the literature.** The persistent random walk and its telegraph-like density relaxation. Reference only.
- **New here:**
  - an independent exact runner;
  - the damping, placed against block 122;
  - the results placed against block 96 as landed.

## Exact target and obligation graph

Target: block 96's three-dimensional threshold along the axes and the body diagonals. The obligations are:
- (O1) the axes;
- (O2) the body diagonals;
- (O3) long memory;
- (O4) damping.

T1–T4 discharge them.

## No-Go Discipline Gate

The note's negative sentence: along the axes the density branch is never complex.

### N1 — Routes by which the sentence could fail or mislead
1. *Other directions.* Not claimed here. The face diagonals and the rest of the coordinate planes are the second attempt's (unrefereed).
2. *`p ≤ 1/6`.* Here `a ≤ 0`, and the axis argument needs `a > 0`.
3. *Interactions between records.* The motion here is of one record, or of a dilute gas.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied motion.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | one record per site; a site's possibilities; no dynamics in the axioms | yes |
| blocks 96, 122 | the motion; damping | yes (restated) |
| probes (#8884; Grok-refereed #9096) | T1–T3 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "persistent records carry damped density waves along the body diagonals past `3(1 − p)/(3p + 2)`, none along the axes" | executed: both factorisations against the `6×6` determinant | executed: the monotonicity identity and `P(a)` | executed: the bracket values; the discriminant; the series | executed: block 96's grid; the damping | the axes and the body diagonals for `p ∈ (1/6, 1)`; the motion supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Complex multipliers mean waves." *Reply:* Damped ones. T4 gives modulus below one, as block 122 requires. These are ripples that die, not sound.

### N8 — Cross-cycle echo
- Block 96 found the line threshold.
- Block 122 found that nonnegative rules damp.
- This note finds the exact three-dimensional picture along the axes and the diagonals.

## Falsifiers

- A `κ` along an axis at which the leading multiplier is complex.
- A diagonal `κ` with `|sin κ| ≤ 3(1 − p)/(3p + 2)` and a complex density branch.
- A density branch of modulus one or more away from `k = 0`.

## Boundaries and non-claims

- The motion is supplied.
- General directions and the diagonal's extremality are not claimed.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 96 and 122, restated or placed.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - continuity of simple roots;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the seventy-first since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results (#8884). A Grok referee confirmed them (#9096).
  - The supervisor re-checked them with its own runner.
- **Before writing.** Main was re-fetched, and block 96 was read as landed.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_persistent_records_in_three_dimensions_carry_damped_density_waves_along_the_body_diagonals_and_none_along_the_axes_2026_09_24.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
