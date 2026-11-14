---
claim_id: first_slab_fixes_lambda_only_at_the_planck_scale_and_a_record_count_multiplier_gives_a_wrong_sign_or_a_drifting_lambda_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Two size rules for the response law's constant Lambda per proper 4-volume, tested against Lambda L^2 = 7.15e-121 (L = sqrt(8 pi) l_P) and w = -1. (a) First-slab charge. Conserved totals of the laws (fermion number, Gauss charges) dilute as a^-3 (w = 0), and the tick's conserved quasi-energy has w = n/3 under lapse a^n, so 1/3 under the fixed lapse (symbolic). Of the three carrying modes tested (a conserved total, a per-cell energy copied at splits, a constant per proper 4-volume), only the last is Lambda-like: the per-4-volume phase over a split is exactly conserved (8 x 2 x 2^-4 = 1), and a per-cell energy copied at splits is w = -1 only on average, with a factor-8 sawtooth (cascade, 10 cycles). Fixing Lambda by the one-cube start's mean-zero dark constant, Lambda = <K>/<v> (rebuilt construction of PR #9947), is split-stable given the supplied rule that every newborn cube starts at flat on the same register, and then predicts Lambda > 0, w0 = -1 and wa = 0. With a closed window top the allowed set is the generalised Rayleigh interval [Lambda_min, Lambda_max] of (K, v), with Lambda_min L^2 = 1.3e-3 to 9.6e-2 and Lambda_max L^2 = 7.1e7 to 2.0e9, so the measured value is excluded, by 1e117 to 1e119. With a transparent top Lambda_min falls as (top)^-6 (slope -6.00), so the size is free; it would need a top near 1e20 L. A matter-filled first cube needs a cancellation to 9e-120 (fitted). (b) Fixed 4-volume per record. Under the supplied record rule (one record per site per half-tick) record counts are exact (Fano 0), so no Sorkin fluctuation arises. A sharp integer count makes Lambda L^2 defined only modulo 4 pi/sig (581 to 2902), a Planck-sized circle with the point on it free. A fixed total count of the history needs a finite 4-volume, which forces Lambda <= 0 (wrong sign). A to-date count N gives N^-1/2 = 0.011 to 0.14 times the measured value and N^-1 ~ 1e-122 times it, with w0 from -0.58 to +0.32 and wa from +0.51 to +1.63. (c) A first-slab integer (Q = 4) per 4-volume to date gives 4e-240 and tracks. None of the rules tested fixes the size; the gate result is FAILURE. Supplied model, finite diagnostic: LambdaCDM (Planck 2018), the eps0 range, the window and hop kinetic, v_r = sig/2, Q = 4, and DESI DR2 central values for a sign comparison."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/first_slab_fixes_lambda_only_at_the_planck_scale_and_a_record_count_multiplier_gives_a_wrong_sign_or_a_drifting_lambda_2026_10_22.py
---

# In the rebuilt one-cube window the first slab allows Lambda only at the Planck scale or above, and the tested record-count multipliers give a wrong sign or a drifting Lambda

Claim type: bounded_theorem.
Primary runner: `scripts/first_slab_fixes_lambda_only_at_the_planck_scale_and_a_record_count_multiplier_gives_a_wrong_sign_or_a_drifting_lambda_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its response law (CL-3) carries Lambda as a supplied constant per proper 4-volume, with w = -1 exactly and a free size. This note follows two leads the register leaves open: "a conserved charge set by the first slab" (lambda-size-rule boundary), and a unimodular reading in which Lambda is the Lagrange multiplier of a fixed 4-volume per record. It builds on PR #9947 (fixed lapse, one-cube sign), PR #9962 (counts, spreads and window powers), PR #9900 (fixed 4-volume per record conserves a Lambda set by initial data) and PR #9876 (a record-count Lambda needs Poisson input). The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

Units: rung units, L the flat cell rung, 8 pi G hbar = L^2, c = 1. Per cell and tick the proper time is sig l, sig = sin(eps0)/sqrt3; a half-tick is half of that. Measured: Lambda L^2 = 7.151e-121, H0 L = 5.90e-61.

## Statement

A. Which conserved quantity is Lambda-like.

1. The laws' conserved totals (fermion number, Gauss charges, and any total carried at a fixed energy per unit) dilute as a^-3, so w = 0. The tick's conserved quasi-energy under lapse a^n has w = n/3, so under the fixed lapse (n = 1) the dark constant is dark radiation (rederives PR #9947 item 1). The edge-pair totals n1 + n2 = 1 are labels, carrying no phase.
2. Of the three carrying modes tested, only a quantity copied per cell at splits and carried per proper 4-volume behaves as a cosmological constant; other carrying rules are not tested. Over a split, 8 children x 2 child ticks x 2^-4 of the 4-volume gives exactly 1, so the per-4-volume phase is conserved. A per-cell energy copied at splits but fixed per cell is w = -1 only on average: over a 10-cycle cascade the fitted w is -0.990, with a factor-8 sawtooth in each cycle. The laws' one carrier of this kind is CL-3's constant itself, and in each cube it is tied to the edge zero-point by the mean-zero dark constant, <K> = Lambda <v>. Edge terms are not subtracted.

B. The first-slab rule: Lambda is fixed by the one-cube start's mean-zero dark constant.

3. On the rebuilt construction of PR #9947 (window l/L = 2^(n/s - 3), hop kinetic, Dirichlet walls), the closed-top minimum is Lambda_min L^2 = 8.35e-2, 9.14e-2 and 9.56e-2 at s = 23, 50 and 113 (Delta = 0), and 1.30e-3, 1.42e-3 and 1.49e-3 at Delta = 1. The mean form <K> = Lambda <v> admits exactly the Lambda in [Lambda_min, Lambda_max]: with y = v^(1/2) psi, <K>/<v> is the ordinary Rayleigh quotient of v^(-1/2) K v^(-1/2), so K - Lambda v is positive definite below the interval and negative definite above it (the runner checks both and that the extreme eigenvectors attain the ends). Lambda_max L^2 is 7.09e7, 3.72e8 and 2.04e9 at s = 23, 50 and 113, for either Delta. Corrected 2026-11-14 from "every Lambda >= Lambda_min", which is false above Lambda_max. The measured value lies below the allowed interval by a factor of 1.8e117 to 1.3e119, so the rule EXCLUDES the measured size. It does not merely miss it.
4. With a transparent top, Lambda_min falls as (top length)^-6 (fitted slope -6.00 over tops of 2, 8 and 32 L). The start then fixes only the sign. The measured value would need a top of 1.1e20 L (8.5e-15 m), a length no law contains.
5. With matter in the first cube, Lambda <v> = <K> - <E_m>. Reaching the measured value needs <E_m>/<K> = 1 - 8.6e-120, which is initial-data tuning (FITTED).
6. The rule is split-stable given a supplied premise: every newborn cube is born at the flat length on the same register, so its constraint has the same allowed interval, and nothing is kicked at splits. With that premise it predicts Lambda > 0, w0 = -1 and wa = 0. The runner prints this as a SUPPLIED line, not a counted check (it was a literal-True check before 2026-11-14).

C. Fixed 4-volume per record: Lambda as the multiplier of the record count.

7. Under CL-2 every site records once per half-tick, and splits go 1 -> 8, so the count is a fixed function of the split history and is exact (Fano 0; one-cube start, 3 splits x 5 ticks: 46800 records, variance 0 by construction, printed as SUPPLIED). The counted check is the control: the Fano statistic detects a seeded Poisson count (Fano 0.999). A Sorkin-type dV4 ~ sqrt(N) has no source. Conjugacy with a sharp count leaves Lambda's value unconstrained; it does not give 1/sqrt(N).
8. With V4 = N v_r exactly, and v_r = (sig/2) L^4, the Lambda phase is (Lambda L^2) v_r N with N an integer. So Lambda L^2 is defined only modulo 4 pi/sig, which is 581 to 2902 over the eps0 range: a Planck-sized circle. The measured value is 1.2e-123 of a turn, and nothing picks a point on the circle. PR #9947 found no such circle when the 4-volume per record varies with the edges. It exists only under the dropped fixed-4-volume clause.
9. A fixed total record count for the whole history needs a finite total 4-volume. For Lambda > 0 the cascade's future 4-volume diverges, because splits never stop while H > 0 and the integral of e^(3Ht) dt diverges. A finite total therefore forces Lambda <= 0 and recollapse. The sign is wrong.
10. A to-date count, taken as records in the past cone or as the Hubble volume times the age, is horizon-tied and not conserved, so it is no first-slab charge. Today N is 9.4e241 to 4.7e242 (past cone) or 3.0e243 to 1.5e244 (Hubble volume x age). The rule Lambda L^2 = N^-q gives:
   - past cone, q = 1/2: 0.065 to 0.14 times the measured value; w0 = -0.34, wa = +0.51;
   - past cone, q = 1: about 1e-122 times it; w0 = +0.32, wa = +1.01;
   - Hubble volume x age, q = 1/2: 0.011 to 0.025 times it; w0 = -0.58, wa = +0.81;
   - Hubble volume x age, q = 1: about 1e-124 times it; w0 = -0.17, wa = +1.63.
   Every form drifts with wa > 0, opposite in sign to the DESI DR2 hint (about -0.75, -0.86).

D. Other.

11. A first-slab integer charge Q (Q = 4, the fermion number of a half-filled cube) spread over the 4-volume to date gives 3.9e-240, about 1e-119 of the measured value, and tracks as V4^-1.

## Candidate rule tested (not adopted)

> "First-slab constant. Lambda is the value at which the one-cube start's mean dark constant vanishes; each newborn cube inherits it per proper 4-volume."

Gate, item by item:
1. No measured number is chosen.
2. No observed structure is inserted; the rule uses only CL-1's window and CL-3's constraint.
3. It makes untargeted predictions: Lambda > 0 (true), w = -1 and wa = 0 (consistent with Planck; DESI's 2.8 to 4.2 sigma hint aside), and, with the closed top, Lambda L^2 in [Lambda_min, Lambda_max] with Lambda_min >= 1.3e-3, which is FALSIFIED by 1e117 or more.
4. It bends no axiom beyond the existing laws.

With a transparent top the rule fixes the sign only. Result: FAILURE of the size goal.

The record-multiplier rules pass gate items 1 and 2 and bend the Record axiom (records each half-tick, CL-2's existing departure). The global form is falsified by the sign and the to-date form by size and drift; the to-date form also needs Poisson counts, which CL-2 forbids. The circle form fixes nothing below the Planck scale.

## Derivation

Item 1 is sympy on rho ~ a^-3 and a^-(n+3). Item 2 is a cascade with edge l = L 2^phase, splits at 2L and 8^k cells, with w fitted from ln rho against ln a. Items 3 to 5 build the tridiagonal hop kinetic, with bond weights 1/m, m = 6 x^2 (ln2/s)^2 (sig cancels), and v = x^4, and take the lowest and highest generalised eigenvalues of (K, v). The transparent top drops the top wall's diagonal share. Item 8 is the phase of an integer count. Item 9 is sympy. Item 10 integrates LambdaCDM (Omega_m 0.3153, Omega_r 9.1e-5, Omega_L 0.6847) on 200001 log-a points; the past-cone V4 is the trapezoid integral of a^3 (4 pi/3) chi^3 dt; w = -1 + (q/3) dlnN/dlna; and wa comes from a secant between a ~ 0.5 and 1.

## Finite checks

The runner gives 11 PASS and 0 FAIL and exits nonzero if any check fails. Several PASS lines record a failure against measurement. Two lines are printed but not counted: the split-stability premise (SUPPLIED) and the gate verdict (a judgement); before 2026-11-14 both were literal-True checks.
- Exact: w_total = 0 and w_D = n/3; split phase 1; Lambda_min(s = 23) = 8.346e-2, matching PR #9947; the Rayleigh interval and its definiteness controls; slope -6.00; the Poisson control of 0.999; the divergent integral.
- Diagnostics: as listed in items 2 to 5, 8 and 10.

## Boundary

Not claimed: that no first-slab or unimodular rule exists. These are not computed: inhomogeneous edge modes, coherent many-cell edge states for the first slab (the block form gives b^-6, PR #9947), a self-consistent everpresent history, and closed recollapsing histories in detail. The DESI comparison is a sign test. Open: a law that picks a point on the Planck circle of item 8, or a transparent-top start whose top is fixed by a rule.

## Supplied vs forced

Supplied: LambdaCDM and the measured values; the eps0 range; the window [L/8, 2^(1+Delta) L] and the hop kinetic; v_r = sig/2; Q = 4; the power q; and DESI central values.

Forced, given the supplied models and the laws as this note states them (zero premise weight):
- the a^-3 and n/3 laws;
- per-4-volume conservation at splits;
- Lambda_min > 0, the finite upper end Lambda_max, and the (top)^-6 scaling of Lambda_min;
- exact counts;
- the circle period;
- Lambda <= 0 for a finite global total;
- drift of every horizon-tied count.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records.
- [Candidate-law register](CANDIDATE_LAWS.md): CL-1's fixed lapse, window and split; CL-2's record per site per half-tick; CL-3's constant per proper 4-volume and mean-zero dark constant. Zero premise weight.
- Builds on the open PRs #9947, #9962, #9900 and #9876. #9900 and #9876 are carried on this branch ([fixed 4-volume](FIXED_FOUR_VOLUME_PER_RECORD_CANCELS_VACUUM_ENERGY_AND_LEAVES_LAMBDA_AS_HISTORY_BOUNDED_THEOREM_NOTE_2026-10-21.md), [time reversal](TIME_REVERSAL_FREEZES_HALF_FILLED_SEA_RECORDS_AND_RECORD_COUNT_LAMBDA_NEEDS_POISSON_INPUT_BOUNDED_THEOREM_NOTE_2026-10-21.md)); #9947 and #9962 are recorded only in the consolidation's map.

## How to run

```
python3 scripts/first_slab_fixes_lambda_only_at_the_planck_scale_and_a_record_count_multiplier_gives_a_wrong_sign_or_a_drifting_lambda_2026_10_22.py
```

Needs numpy, scipy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in under 1 s with about 114 MB resident, prints about 6 kB and ends with `TOTAL: PASS=11 FAIL=0` (12 at the held head, which counted the two literal-True lines). It is seeded, and repeated runs gave identical output.
