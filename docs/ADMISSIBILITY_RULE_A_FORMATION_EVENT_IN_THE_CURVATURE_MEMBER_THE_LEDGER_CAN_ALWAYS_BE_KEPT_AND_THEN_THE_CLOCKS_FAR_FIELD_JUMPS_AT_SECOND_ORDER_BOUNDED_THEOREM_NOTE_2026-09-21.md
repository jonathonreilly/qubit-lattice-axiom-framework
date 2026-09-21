---
claim_id: admissibility_rule_a_formation_event_in_the_curvature_member_the_ledger_can_always_be_kept_and_then_the_clocks_far_field_jumps_at_second_order_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 58 and 60 (open PRs #8579, #8590; not adopted): block 60's ledger linear in the rates with the curvature member, isotropic stretching, walls held at w = l = 1, and its exact strong field for bodies at rest of bare energies m_x: chi = sqrt(l) = 1 + sum Q_x g(., x) with Q_x chi_x = m_x/(8K); N = w chi = 1 - sum P_x g(., x) with P_x = Q_x w_x; the ledger of the box is the walls' term 8K sum Q_x. Block 58's question: a spread amplitude at rest - bodies m_x = m p_x on several sites, p_x the probability at x - is replaced by ONE record at a site y; NO rule of formation is assumed. (T1) The ledger is kept iff the record's charge is Q' = sum Q_x, that is iff its bare energy is m' = 8K Q'(1 + Q' g_yy); such a record exists for EVERY amplitude (under block 56's law, block 58 found a threshold), and m' - m = 8K sum_xx' Q_x Q_x' (g_yy - g_xx'). If instead the record keeps the amplitude's bare energy the ledger changes. (T2) For every discrete-harmonic h, the sum over wall bonds of (chi_inside - 1) h(wall) equals sum_x Q_x h(x): what the walls see of the LENGTHS are the moments of the charges. With the ledger kept the monopole does not jump and the dipole jumps by Q'(y - Xbar), Xbar the centre of the charges Q_x, which are proportional to p_x/chi_x. Over ANY odds of where the record forms the mean jump is Q'(sum odds_y y - Xbar): it vanishes for odds proportional to p_x/chi_x and not for odds proportional to p_x or to p_x/chi_x^2; at weak field p/chi is block 58's p sqrt(w). (T3) What the walls see of the CLOCKS is sum P_x = sum Q_x w_x, and it is NOT kept when the ledger is: for the stated amplitude it jumps from 1.152 to 0.871; in general the jump is -2[Q'^2 g_yy - sum_xx' Q_x Q_x' g_xx'] = -(m' - m)/(4K) at second order in the charges and vanishes at first order; since the record's P' = Q'/(1 + 2 Q' g_yy) is increasing in Q', the record that keeps the clocks' monopole is another record: none keeps both far-field coefficients. By block 60 T5 nothing in the isotropic lengths or the rates is delayed, so within these clauses the jump is felt at the walls at the same label time. EXECUTED, NOT CLAIMED: brute-force stationary points of the full non-linear ledger in 250 variables reproduce every number (flux of chi 1.450000 before and after; clocks' monopole 1.15184 and 0.87141; the dipole's jump at each of the five sites; mean jumps for three odds); the record keeping the lengths' monopole has bare energy 11.60, the one keeping the clocks' monopole 22.8. NOT claimed: whether an amplitude that has formed no record sources anything; whether a formation event keeps the ledger, the bare energy or anything else; where records form or with what odds (the parked statistical postulate is neither used nor approached); bodies that are not pinned at rest (block 60: a pinned body has P < Q at strong field; internal motion is not examined); the direction-dependent lengths or the frame of blocks 61 to 65; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_a_formation_event_in_the_curvature_member_the_ledger_can_always_be_kept_and_then_the_clocks_far_field_jumps_2026_09_21.py
---

# A formation event in the curvature member: the ledger can always be kept, and then the clocks' far field jumps at second order

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within the supplied clauses of block 60, for bodies at rest; no rule of formation assumed; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates, for lengths of weight zero and for a ledger linear in the rates with the curvature member; it reports what the replacement of a spread amplitude at rest by one record does to the ledger and to what the walls see, of the lengths and of the clocks; no rule of formation is assumed; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The owner's fourth fork asks whether an amplitude that has formed no record sources anything. Block 58 (open PR #8579) gave the fork an exact discriminator under block 56's clock law: replace a spread amplitude at rest by one record and ask what the walls see. The monopole never jumps if the ledger is kept; the dipole jumps; its mean over any odds vanishes for one particular density. But block 56's law has a threshold — beyond a certain energy no single site can show the amplitude's ledger — and only one far-field coefficient. Block 60 (open PR #8590) replaced that law by the curvature member, which has *two*: what the lengths show and what the clocks show. This note runs block 58's question again there, exactly.

1. **The ledger can always be kept.** The ledger of a walled region is `8K` times the total charge `ΣQ_x`. One record of that charge exists for every amplitude, with bare energy `8KQ'(1 + Q'g_yy)` — there is no threshold. At the centre of the box it must carry *more* bare energy than the amplitude did. A record that keeps the bare energy instead lets the ledger fall (T1).
2. **What the walls see of the lengths.** Exactly the moments of the charges. With the ledger kept the monopole does not jump; the dipole jumps by `Q'(y − X̄)`, where `X̄` is the centre of the *charges*, `Q_x ∝ p_x/χ_x`. Over any odds whatever, the mean jump vanishes for odds proportional to that density and for neither of its neighbours. At weak field it is block 58's density (T2).
3. **What the walls see of the clocks.** The clocks' monopole `ΣQ_xw_x` is *not* kept when the ledger is. It jumps, by an amount of second order in the charges, `−(m' − m)/(4K)`. The record that would keep it is a different record — here of about twice the bare energy (executed). **No record keeps both far-field coefficients.** And since nothing in these fields is delayed (block 60 T5), within these clauses the jump arrives at the walls at once (T3).

In plain terms: in the curvature picture a lump of stuff shows the outside two numbers — how much it stretches lengths and how much it slows clocks. For weak lumps they are the same number; for strong ones they differ, and they differ *differently* for a spread-out lump and a concentrated one. So when a spread amplitude becomes one record, you can arrange for the books to balance (always — that is new) and then the length number stays put, but the clock number moves, a little, at once, everywhere. If only records source, the outside sees far more: a whole monopole appearing. Either way formation is visible from afar; the question is at which order.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "decision record (PR #8572), fork 4 and its sharpening after block 58: 'if unformed amplitude sources, formation leaves the far field's leading term untouched and moves the next one'; third addendum, 'What is still open': 'records and formation events (fork 4) inside the curvature member'."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the same event for bodies that are not pinned (internal hop energy raises P: block 60 T3(e)); whether a moving amplitude's formation keeps momentum (block 66's balance); the event in the frame formulation of blocks 62 to 65; the owner's fork 4"
conditional_surface_status: "T1, T2 exact for every amplitude at rest and every site of formation in every box with held walls; the statement about odds holds for ANY odds and assumes none; T3 exact for the stated configuration, its second-order formula for every configuration"
hypothetical_axiom_status: "block 60's clauses and member; bodies pinned at rest; an amplitude at rest sourcing as bodies m p_x (block 58's reading, one side of fork 4); hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the Record axiom's statement that records are permanent, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 58 and 60 (open PRs) supply the question and the exact strong field.

- **Box.** `7 × 7 × 7`, walls held at `w = ℓ = 1`; `g(·, x)` the unit-source potential of `−Δ` on the interior with zero walls; `8K = 6`.
- **Bodies at rest** with bare energies `m_x`: `χ = 1 + ΣQ_xg(·, x)`, `Q_xχ_x = m_x/(8K)`; `N = wχ = 1 − ΣP_xg(·, x)`, `P_x = Q_xw_x` (block 60 T4). **Ledger** `= 8K ΣQ_x`.
- **Spread amplitude at rest**: probabilities `p_x` on sites `x ∈ X`, bodies `m_x = m p_x` (block 58's reading; it is one side of fork 4). Here five sites with charges `1/2, 1/3, 1/5, 1/4, 1/6`.
- **Record** at `y`: one body of bare energy `m'`.
- **Wall moments.** For `h` discrete-harmonic on the box, `Σ_{wall bonds}(χ_inside − 1)h(wall)`; `h = 1` is the flux (monopole), `h = x, y, z` the dipole. Likewise for `1 − N`.
- **Odds.** Any non-negative numbers `π_y` on the sites where the record may form. None is assumed, derived or proposed; the registered and parked statistical statements are not used.

The two far-field coefficients of a static body and their equality only when its stresses are counted are the masses of Arnowitt, Deser and Misner and of Komar and Tolman (named in block 60). That a harmonic function's moments on a boundary equal the moments of the enclosed charges is Green's second identity. Proposals in which the reduction of an amplitude is tied to its field are those of Diósi and of Penrose; nothing of theirs is used, and no rule of reduction is assumed here.

## Prior art and what is new

Classical in kind. New, in the framework's vocabulary: block 58's discriminator re-run in the member that gives the full bending, exactly; that there the ledger can *always* be kept by one record; that the density which holds the dipole's mean is the charge density `p/χ`, agreeing with block 58's at weak field; and that with two far-field coefficients no single record keeps both, the clocks' monopole jumping by `−(m' − m)/(4K)` at second order. No gravitational claim is made.

## Exact target and obligation graph

Target: what a formation event does to the ledger and to the far field in the curvature member. Obligations: (O1) the ledger; (O2) what the walls see of the lengths, and odds; (O3) what they see of the clocks. T1–T3 discharge them.

## Theorem T1 — the ledger can always be kept

*Statement.* (a) The ledger is the same before and after iff `Q' = Σ_xQ_x`, that is iff `m' = 8KQ'(1 + Q'g_yy)`; for every `Q' > 0` this is a positive bare energy. (b) `m' − m = 8K Σ_{x,x'}Q_xQ_{x'}(g_yy − g_{xx'})`. (c) If the record keeps the amplitude's bare energy instead, while the ledger-keeping bare energy of (a) exceeds it, then the record's charge is below `ΣQ_x` and the ledger falls.

*Proof.* (a) The ledger is `8KΣQ` (block 60 T4(c)); one body has `Qχ_y = Q(1 + Qg_yy)`. (b) `m = 8KΣ_xQ_xχ_x = 8K[ΣQ_x + ΣΣQ_xQ_{x'}g_{xx'}]`. (c) `Q(1 + Qg_yy)` is increasing. ∎

Under block 56's law the ledger of one site is bounded (`12/(γg_y)`), so a large enough amplitude had no ledger-keeping record; here the ledger of one site is unbounded (block 60 T4(c)).

## Theorem T2 — what the walls see of the lengths

*Statement.* (a) For `h` discrete-harmonic, `Σ_{wall bonds}(χ_inside − 1)h(wall) = Σ_xQ_xh(x)`. (b) With the ledger kept the monopole is unchanged and the dipole changes by `Q'(y − X̄)`, `X̄ = ΣQ_xx/ΣQ_x`. (c) For any odds `π` the mean change of the dipole is `Q'(Σπ_yy/Σπ_y − X̄)`; it is zero for `π_y ∝ Q_y ∝ p_y/χ_y`.

*Proof.* (a) The second difference identity for `χ − 1` (zero on the walls, `Δ(χ − 1) = −Q_x` at the bodies) and `h` (`Δh = 0`): the interior sum is `−ΣQ_xh(x)` and the boundary sum is `−Σ(χ_inside − 1)h(wall)`. (b), (c) from (a) with `h = 1, x, y, z`; every ledger-keeping record has the same charge `Q'` wherever it forms. ∎

`p/χ = p/√ℓ`. At weak field `1/χ = 1 − λ/2 = 1 + u/2`, and block 58's density `p√w` is `p(1 + u/2)`: the same. The two neighbouring densities `p` and `p/χ²` move the mean by `(0.003, −0.005, 0.006)` and its opposite here.

## Theorem T3 — what the walls see of the clocks

*Statement.* (a) The flux of `1 − N` into the walls is `ΣP_x = ΣQ_xw_x`. (b) For the stated amplitude and the ledger-keeping record at the centre it is `1.152` before and `0.871` after. (c) In general, with the ledger kept, the change is `−2[Q'²g_yy − ΣΣQ_xQ_{x'}g_{xx'}] = −(m' − m)/(4K)` up to terms of third order in the charges, and zero at first order. (d) `P' = Q'/(1 + 2Q'g_yy)` is increasing in `Q'`; hence the record that keeps `ΣP_x` differs from the one that keeps `ΣQ_x` whenever (b)'s change is not zero.

*Proof.* (a) As T2(a) for `1 − N`, which is `ΣP_xg(·, x)`. (b) Computation (runner D1). (c) `w_x = N_x/χ_x = 1 − 2Σ_{x'}Q_{x'}g_{xx'} + …`, so `ΣQ_xw_x = ΣQ − 2ΣΣQQg + …`, and for the record `Q' − 2Q'²g_yy + …`; the identity with `m' − m` is T1(b). (d) Block 60 T4(b). ∎

Block 60 T5: for every kinetic term holding no rate of change of a rate, the rates and the isotropic lengths follow the content at the same label time. Within these clauses, then, the change of the clocks' monopole is present at the walls when the record forms.

## Executed (supervisor control and refuting pass; floating point; evidence, not proof)

`specs/supervisor_control_block67_refuter.py`: stationary points of the full non-linear ledger in all 250 variables by a root search on the analytic gradient, with no unit-source potential in the search. W1: the amplitude (bare energies `3.521, 2.247, 1.320, 1.660, 1.094`): flux of `χ` `1.450000`, flux of `1 − N` `1.151837`, first moments equal to `ΣQx` to the digits printed; the ledger-keeping record (bare energy `11.5883`): flux of `χ` `1.450000`, clocks' monopole `0.871408`. W2: the record that keeps the bare energy: the ledger falls by `1.0766`. W3: a scan of the record's bare energy: the lengths' monopole is kept at `11.60`, the clocks' at `22.8`: two records. W4: formation at each of the five sites: the dipole's jump equals `Q'(y − X̄)` to five digits; mean jump `(0, 0, 0)` for odds `∝ p/χ`, `(0.0032, −0.0055, 0.0055)` for `∝ p`, the opposite for `∝ p/χ²`.

## No-Go Discipline Gate

The note's negative sentences: no record keeps both far-field coefficients; the clocks' monopole is not kept when the ledger is; odds proportional to the probability do not hold the dipole's mean.

### N1 — Routes by which the sentences could fail
1. *Bodies that are not pinned.* `P < Q` at strong field is a property of a body pinned at rest with no internal stress (block 60 T4(d), T3(e)). If internal hop energy restores `P = Q` for a bound body, the clocks' jump would go with it. Not examined; it is on `ai/probes`.
2. *A formation event that keeps something else.* T3(d): one can keep `ΣP` instead, or `ΣP + ΣQ` (what a slow test body feels), each with its own record. The note does not say which, if any, a formation event keeps.
3. *A delay.* The isotropic fields have none (block 60 T5); the direction-dependent ones of blocks 61 to 64 do, and are not part of this note.
4. *Records as the only sources.* Then before the event the walls see nothing and after it the full monopoles: a first-order jump in both coefficients. This is the other side of fork 4 and is not decided here.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Isotropic stretching; bodies pinned at rest; walls held; the spread amplitude sources as bodies `m p_x` (one side of fork 4); the record at the centre in T1(b)'s sign and in T3(b). `K > 0`.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice; records are permanent; the absences that motivate the clauses | yes (premise) |
| block 60 (open PR #8590) | the ledger, the curvature member, the exact strong field, no delay | yes (restated) |
| block 58 (open PR #8579) | the question, the wall-moment identity, the density `p√w` | yes (restated) |
| block 56 (open PR #8573) | the threshold of the simplest clock law | placement |
| decision record (open PR #8572) | fork 4 | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the ledger can always be kept; the lengths' monopole stays, the dipole jumps by `Q'(y − X̄)`, mean zero for odds `∝ p/χ`; the clocks' monopole jumps at second order; no record keeps both" | executed: exact fields of the five-site amplitude and of the ledger-keeping record, both stationarity conditions at all 125 sites | executed: the record's bare energy against the amplitude's; a charge of 1000; the sign when the bare energy is kept | executed: wall moments of `χ − 1` against `ΣQ_xh(x)` for `1, x, y, z`; the flux of `1 − N` against `ΣP_x` | executed: the dipole's jump; the mean for three odds; the clocks' monopole before and after; the second-order formula at charges scaled by 1/1000 | T1, T2 every amplitude at rest, every site, every box with held walls; any odds, none assumed; T3 the stated configuration exactly, the formula generally; fork 4, what an event keeps, where records form not decided |

### N6 — Partial-closure paths and primitive scan
`realized_state_primitive` grants evaluation at a supplied state and no rule for which state is realized; it is not used. The parked statistical postulate (registry entry 1) is not used: no odds are assumed, derived or proposed, and every statement about odds is an identity in arbitrary odds. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "The clocks' jump is an artefact of pinning the bodies." Reply: possibly, and N1.1 says so; the note's statement is about the clauses as they stand, in which bodies at rest are supplied and pinned, and it says exactly what would have to be true of bound bodies for the jump to go away. Second objection: "Instantaneous jumps at a distance are unphysical; the model is sick." Reply: block 60 already reported that the isotropic sector has no delay; this note adds that a formation event makes that visible at second order. It is a fact about these clauses that the owner should have next to fork 4, not a claim about the world. Third objection: "Odds again." Reply: identities in arbitrary odds, as in block 58; the parked postulate is not approached.

### N8 — Cross-cycle echo
Block 49: the record layer is a source, not a carrier. Block 58: the monopole never jumps, the dipole does; a threshold. Block 60: two far-field coefficients, equal at first order only; nothing delayed. Here: no threshold; the same dipole law with the charge density `p/χ`; the second coefficient jumps.

## Falsifiers

- An amplitude at rest for which no single record keeps the ledger.
- A box, amplitude and site for which the wall moments of `χ − 1` are not the moments of the charges, or the dipole's jump is not `Q'(y − X̄)`.
- Odds other than `∝ p/χ` (on the amplitude's sites) for which the dipole's mean jump vanishes for every amplitude.
- A ledger-keeping record whose clocks' monopole equals the amplitude's at second order.

## Boundaries and non-claims

Fork 4 is not decided: the note takes the side on which an unformed amplitude sources, and says under N1.4 what the other side gives. It does not say that a formation event keeps the ledger, or anything else, and assumes no rule or odds of formation. Bodies are pinned at rest; bound bodies with internal motion, moving amplitudes, the direction-dependent lengths and the frame are outside. The absence of a delay is block 60's statement about the isotropic sector. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the permanence of records, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 56, 58, 60 and the decision record (PRs #8573, #8579, #8590, #8572, open): restated or placed.
- Named standard imports at definition level: exact solution of linear systems; the second difference identity on a box; monotone functions; expansion to second order.
- Reference only: Arnowitt, Deser and Misner; Komar; Tolman; Green; Diósi; Penrose.

## Review record
Supervisor-run block, the fifteenth of the source-link direction and the eleventh of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: the block stands next to the parked statistical postulate — no odds assumed, derived or proposed; every statement about odds an identity in arbitrary odds; the registry entry named as not used; and it takes one side of fork 4 openly. A rigour lens: every number is exact (rational charges chosen first, bare energies computed from them), and the brute-force pass finds the same stationary points with no potential in the search; the scan for the record that keeps the clocks' monopole first stopped short of it and was extended (`22.8` against `11.6`). The supervisor checked that the ledger-keeping record's charge does not depend on where it forms, which is what makes the statement about odds clean. A comparator lens: the two masses of a static body — named under the Premises; the jump is tied to pinning and the note says what would remove it. A strategy lens: fork 4's discriminator now exists in the member that gives the full bending, with one new feature (no threshold) and one new cost (the second coefficient). Refuting pass (`specs/supervisor_control_block67_refuter.py`): W1–W4 as reported under Executed; all pass. Mutation census: 8 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_formation_event_in_the_curvature_member_the_ledger_can_always_be_kept_and_then_the_clocks_far_field_jumps_2026_09_21.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.
