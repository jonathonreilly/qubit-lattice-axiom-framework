---
claim_id: admissibility_rule_a_formation_event_in_the_curvature_member_the_ledger_can_always_be_kept_and_then_the_clocks_far_field_jumps_at_second_order_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "Conditional comparison of two stationary solutions of the supplied finite grounded positive-K diagonal-source model. Every finite positive total charge has a single-site ledger-preserving replacement. Harmonic wall moments obey the charge identity; the dipole change can vanish, and charge-weighted odds are sufficient but not uniquely necessary for zero mean change. The flux of 1-N, not of the clock w itself, changes in the stated example; its general second-order difference can vanish. A record preserving that flux exists only below the target-site capacity. No instantaneous formation dynamics, universal nonzero jump, or full coupled matter existence is established."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_a_formation_event_in_the_curvature_member_the_ledger_can_always_be_kept_and_then_the_clocks_far_field_jumps_2026_09_21.py
---

# Static single-site replacement: ledger, harmonic moments and the second flux

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within the supplied clauses of block 60, for bodies at rest; no rule of formation assumed; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates, for lengths of weight zero and for a ledger linear in the rates with the curvature member; it reports what the replacement of a spread amplitude at rest by one record does to the ledger and to what the walls see, of the lengths and of the clocks; no rule of formation is assumed; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

This compares stationary source configurations; it supplies no formation dynamics. In the selected positive-K finite box model, a record of charge Q'=sum Q always preserves the ledger. Its bare energy differs by the quadratic expression in T1. The sign is positive in the stated example; a sufficient general condition is g_yy>=g_xx' for all occupied pairs with a strict positively weighted term.

The harmonic moments of chi-1 equal the source-charge moments. The dipole change Q'(y-Xbar) may vanish. Charge-proportional odds give zero expected change but are not the unique such odds: the necessary and sufficient condition is that the probability-weighted mean site equals Xbar.

The second flux is that of 1-N, where N=w chi. It changes in the stated example and has the second-order expression T3; this coefficient may vanish in other configurations. In a formal distant weak exterior, the leading coefficients of ell-1 and 1-w are respectively 2Q and P+Q, not Q and P. Keeping Q makes the change of P equal the change of the latter coefficient. Finite-wall fluxes and asymptotic coefficients remain distinct concepts.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the Record axiom's statement that records are permanent, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 58 and 60 (open PRs) supply the question and the exact strong field.

- **Model domain.** Finite grounded nearest-neighbour boxes, K>0, nonnegative supplied diagonal source energies and finite charges. Static field solutions do not establish a stationary quantum body or a formation process.
- **Box.** `7 × 7 × 7`, walls held at `w = ℓ = 1`; `g(·, x)` the unit-source potential of `−Δ` on the interior with zero walls; `8K = 6`.
- **Bodies at rest** with bare energies `m_x`: `χ = 1 + ΣQ_xg(·, x)`, `Q_xχ_x = m_x/(8K)`; `N = wχ = 1 − ΣP_xg(·, x)`, `P_x = Q_xw_x` (block 60 T4). **Ledger** `= 8K ΣQ_x`.
- **Spread amplitude at rest**: probabilities `p_x` on sites `x ∈ X`, bodies `m_x = m p_x` (block 58's reading; it is one side of fork 4). Here five sites with charges `1/2, 1/3, 1/5, 1/4, 1/6`.
- **Record** at `y`: one body of bare energy `m'`.
- **Wall moments.** For `h` discrete-harmonic on the box, `Σ_{wall bonds}(χ_inside − 1)h(wall)`; `h = 1` is the flux (monopole), `h = x, y, z` the dipole. Likewise for `1 − N`.
- **Odds.** Any non-negative numbers `π_y` on the sites where the record may form. None is assumed, derived or proposed; the registered and parked statistical statements are not used.

The continuum comparison in the original source invokes the masses of Arnowitt, Deser and Misner and of Komar and Tolman (named in block 60). Those names do not identify the finite-box fluxes with physical masses or prove a general equality after adding unspecified stresses. That a harmonic function's moments on a boundary equal the moments of the enclosed charges is Green's second identity. Proposals in which the reduction of an amplitude is tied to its field are those of Diósi and of Penrose; nothing of theirs is used, and no rule of reduction is assumed here.

## Prior art and what is new

The contribution is an algebraic comparison within the supplied static model, with an explicit finite example. It derives no physical bending law or unique statistical rule.

## Theorem T1 — the ledger can always be kept

*Statement.* (a) The ledger is the same before and after iff `Q' = Σ_xQ_x`, that is iff `m' = 8KQ'(1 + Q'g_yy)`; for every `Q' > 0` this is a positive bare energy. (b) `m' − m = 8K Σ_{x,x'}Q_xQ_{x'}(g_yy − g_{xx'})`. (c) If the record keeps the amplitude's bare energy instead, while the ledger-keeping bare energy of (a) exceeds it, then the record's charge is below `ΣQ_x` and the ledger falls.

*Proof.* (a) The ledger is `8KΣQ` (block 60 T4(c)); one body has `Qχ_y = Q(1 + Qg_yy)`. (b) `m = 8KΣ_xQ_xχ_x = 8K[ΣQ_x + ΣΣQ_xQ_{x'}g_{xx'}]`. (c) `Q(1 + Qg_yy)` is increasing. ∎

Under block 56's law the ledger of one site is bounded (`12/(γg_y)`), so a large enough amplitude had no ledger-keeping record; here the ledger of one site is unbounded (block 60 T4(c)).

## Theorem T2 — what the walls see of the lengths

*Statement.* (a) For `h` discrete-harmonic, `Σ_{wall bonds}(χ_inside − 1)h(wall) = Σ_xQ_xh(x)`. (b) With the ledger kept the monopole is unchanged and the dipole changes by `Q'(y − X̄)`, `X̄ = ΣQ_xx/ΣQ_x`. (c) For any odds `π` the mean change of the dipole is `Q'(Σπ_yy/Σπ_y − X̄)`; it is zero for `π_y ∝ Q_y ∝ p_y/χ_y`.

*Proof.* (a) The second difference identity for `χ − 1` (zero on the walls, `Δ(χ − 1) = −Q_x` at the bodies) and `h` (`Δh = 0`): the interior sum is `−ΣQ_xh(x)` and the boundary sum is `−Σ(χ_inside − 1)h(wall)`. (b), (c) from (a) with `h = 1, x, y, z`; every ledger-keeping record has the same charge `Q'` wherever it forms. ∎

`p/χ = p/√ℓ`. At leading weak-field order, with λ=-u at that order, `1/χ = 1 − λ/2 + O(λ²)` and block 58's density `p√w` agrees to first order. This is not an exact identification of the two models. The two neighbouring densities `p` and `p/χ²` move the mean by `(0.003, −0.005, 0.006)` and its opposite here.

## Theorem T3 — the flux of 1 − N

*Statement.* (a) The flux of `1 − N` into the walls is `ΣP_x = ΣQ_xw_x`. (b) For the stated amplitude and the ledger-keeping record at the centre it is `1.152` before and `0.871` after. (c) In general, with the ledger kept, the change is `−2[Q'²g_yy − ΣΣQ_xQ_{x'}g_{xx'}] = −(m' − m)/(4K)` up to terms of third order in the charges, and zero at first order. (d) `P' = Q'/(1 + 2Q'g_yy)` is strictly increasing with range `0<P'<1/(2g_yy)`. For a desired positive flux S a finite record exists iff `S<1/(2g_yy)`, with `Q'=S/(1-2g_yy S)`. When it exists and (b)'s change is nonzero, it differs from the ledger-preserving record.

*Proof.* (a) As T2(a) for `1 − N`, which is `ΣP_xg(·, x)`. (b) Computation (runner D1). (c) `w_x = N_x/χ_x = 1 − 2Σ_{x'}Q_{x'}g_{xx'} + …`, so `ΣQ_xw_x = ΣQ − 2ΣΣQQg + …`, and for the record `Q' − 2Q'²g_yy + …`; the identity with `m' − m` is T1(b). (d) Differentiate the displayed rational function and solve it for Q'; its denominator must remain positive. ∎

The static solutions give before/after values only. The corrected earlier rate/length note does not establish an instantaneous finite formation event at every wall.

## Historical experiments — deferred

Original floating-point root searches and record-energy scans remain recoverable on the original PR branch. They are not fresh landing evidence; the canonical exact runner verifies the specified static configurations.

## No-Go Discipline Gate

The only strict nonzero-jump assertion concerns the specified example. No universal exclusion of simultaneous preservation is claimed.

### N1 — Exceptions
Already localized configurations, zero dipole displacement, vanishing quadratic flux difference, and symmetric probability distributions are legitimate exceptions. A different source/stress model can change both fluxes.

### N2 — Wall independence
No repository no-go wall is used.

### N3 — Supplied structure
Positive K, fixed walls, isotropic lengths and diagonal sources are premises. All finite target sites admit a ledger-preserving record; preserving the second flux separately has the capacity restriction in T3(d).

### N4 — Dependencies
The corrected static rate/length model supplies the fields; the earlier formation comparison supplies the question. Neither supplies a finite-event dynamical law.

### N5 — Resolution
The runner checks exact stationarity at 125 sites, the full bond ledger, four harmonic wall moments and a finite example's flux difference. Its small-charge numerical comparison is support for the analytic second-order expansion, not a proof of a universal nonzero coefficient. The target-site flux capacity is checked separately.

### N6 — Primitive boundary
No state-selection or probability rule is derived or adopted.

### N7 — Strongest objection
A stationary before/after comparison does not establish a physically possible formation trajectory or its speed. The claims stop at the comparison.

### N8 — Earlier claims
Earlier universal delay and unique-weight assertions are not inputs.

## Falsifiers

- Failure of the static ledger or harmonic-moment identity under the stated hypotheses.
- Failure of the second-order expression under uniform small-charge scaling with fixed finite inverse operator.
- Failure of the record flux range or inverse formula in T3(d).

## Boundaries and non-claims

No universal nonzero jump, unique odds, formation dynamics, instantaneous remote response, complete matter solution or physical bending prediction is established. The original filename is retained for traceability.

## Imports
- `minimal_axioms`: the Lattice axiom, the permanence of records, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 56, 58, 60 and the decision record (PRs #8573, #8579, #8590, #8572, open): restated or placed.
- Named standard imports at definition level: exact solution of linear systems; the second difference identity on a box; monotone functions; expansion to second order.
- Reference only: Arnowitt, Deser and Misner; Komar; Tolman; Green; Diósi; Penrose.

## Dependencies

The linked source notes are used only with the corrected conditional scopes stated here. Historical campaign decisions and deferred experiments are not premise authority.

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion source PR #8573](ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8579](ADMISSIBILITY_RULE_WHAT_A_FORMATION_EVENT_DOES_TO_THE_LEDGER_AND_TO_THE_FAR_FIELD_THE_MONOPOLE_NEVER_JUMPS_THE_DIPOLE_DOES_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8590](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md)

## Review record

Original author content is preserved at PR #8598 head `3bea45f6d8dddddd0ce44e94e083bb597b86967a`, branch `physics-loop/admissibility-induced-law-block67-a-formation-event-in-the-curvature-member-20260921`. Landing review distinguishes flux of N from clock w, corrects the existence restriction for a flux-preserving record, and limits all nonzero and dynamical assertions. Original auxiliary experiments are deferred. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_formation_event_in_the_curvature_member_the_ledger_can_always_be_kept_and_then_the_clocks_far_field_jumps_2026_09_21.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
