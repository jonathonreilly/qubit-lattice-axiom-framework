lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-15T12:41Z

# gap-pinsheet-guide (FINISH row 980): GUIDE runs P1 and P3 of row 977

Pinned commit 7362c467a, branch claude/ym4d-hard-route. Status: in progress.
A GUIDE run refutes or guides; it never proves. Nothing here enters the chain.

## Plan (at most eight steps)

1. Read row 977 (library/gap-tiltproof-max.md) Sections 6.4, 9.2 and the P1/P3 rows; copy the criteria C1-C3 verbatim here before any run.
2. Read FINISH efficiency rules, numeric-lock usage; check memory_pressure.
3. Write the simulator (SU(2) Wilson heat bath + overrelaxation with frozen links) in library/guide/lane980/, test it on a small lattice against known plaquette at beta 2.3.
4. Run P1 (sides 8, 12, 16, 24; T >= 2S) under the numeric lock; record raw data.
5. Run P3 (sides 8, 12, 16) for q_0 and R^0_S under the lock.
6. Evaluate C1-C3 for P1 and P3, per criterion.
7. P2 (compact U(1)) only if time is left.
8. Summary and RESULT line.

## Step 1. Criteria, copied before any run (READ; gap-tiltproof-max.md 6.4 lines 290-296 and 9.2 lines 413-419; gap-tiesearch-opus.md lines 55-60)

Source: `library/gap-tiltproof-max.md` (row 977, Claude Fable 5.2 max, checked by no one), at commit 7362c467a. Copied verbatim:

> Row P1 `gap-pinsheet-guide`: SU(2) Wilson, beta 2.3, lattices S^3 x T with S = 8, 12, 16, 24 and T >= 2S, two adjacent time slices with
> all spatial links of directions 2, 3 frozen at 1 and the time-like links between them frozen at 1 (this is J_(beta,phi^infinity)).
> Observables per plane k and slice: M = sum over y of P_k(y); R_S := E|M|^2/A (equals 4 G^e-hat(0)); tau; second-moment correlation length.
> C1 (test of Theorem D2): R_8 >= 21.8, R_12 >= 32.8, R_16 >= 37.9. If any is violated by more than 3 standard errors, D2 is
> wrong and this row's result is withdrawn. C2 (growth): "sheet longer than the box" if R_24 >= 0.25 x 576 = 144. C3: report tau; if tau >= 0.8, 6.2(b) applies.

> Row P3 `gap-pinsheet-quot`: the lattice of row P1 but with ALL spatial links
> of the two slices frozen at 1 except the direction-1 links of one plane. Measure q_0 (one-link second moment of (1/2) tr P), and
> R^0_S := E[(sum over y of (1/2) tr P(y))^2]/A on sides 8, 12, 16. C1 (test of 9.1(d)): R^0_S >= A (q_0 - G_S/beta) with the measured q_0, within 3
> standard errors; else 9.1 is wrong and is withdrawn. C2: "QUOT-CAP applies" if q_0 - 2 errors >= 0.22 on sides 8 to 16.
> C3 (growth, rule of row 973 Section 2): REFUTED (GUIDE) for a box-uniform (TILT-COV-quot) at beta 2.3 if g - 2 sigma_g > 1.25 on 8 -> 16
> with no decreasing step. Expected by the sigma-model reading: R^0 about m^2 A/4 with growth factor near (L + 2)^2/L^2 per step.

Row 973's rule (gap-tiesearch-opus.md 55-60), the reference for P3 C3: g := (lambda(16)/lambda(8))^(1/4), error propagated linearly from
the two block errors; REFUTED if g - 2 sigma_g > 1.25 and no single step shows a decrease by more than 2 standard errors.

**Readings fixed now, before any run (mine; where the copied text leaves a choice).**
- Notation. P_k(y) is the slice-0 direction-1 link from (k, y) to (k+1, y), y = (y_2, y_3) in the S x S plane, A = S^2; P'_k(y) the slice-1 link.
  Unit quaternions are 4-vectors, <a, b> = (1/2) tr(a b^dagger).
- Lattice. Periodic S^3 x T, T = 2S, Wilson action beta sum_p (1 - (1/2) tr U_p), beta = 2.3 on every plaquette (b = beta). Frozen at 1 in P1:
  the S^3 time-like links from slice 0 to slice 1, and the direction-2 and direction-3 links of slices 0 and 1. All other links are Haar
  variables (row 977, 5.1: the time-like links outside the layer 0-1 may be Haar; finite T approximates the T -> infinity law).
- P3 frozen set: the time-like links of layer 0-1 and every spatial link of slices 0 and 1 except the direction-1 links of plane k = 0 in
  both slices (the tilt <phi, x/s + w/s'> pins x and w on the same links).
- P1 estimators. R_S is averaged over the S planes and the 2 slices of each configuration (equivalent by translation in direction 1 and by
  the time reflection through the layer). tau := E<P_k(y), P'_k(y)>, averaged over all k, y. Second-moment length
  xi := (G(0)/G(p_1) - 1)^(1/2) / (2 sin(pi/S)), G(p) := E|sum_y e^(i p.y) P_k(y)|^2 / A, p_1 = (2 pi/S, 0) and (0, 2 pi/S) averaged.
- P3 estimators. q_0 := E[((1/2) tr P)^2] over the S^2 free links of slice 0 and the S^2 of slice 1; R^0_S per slice, averaged over the 2 slices.
  P3 C3 with sides 8, 12, 16 only: g := (R^0_16/R^0_8)^(1/4); "no decreasing step" checked on the steps 8 -> 12 and 12 -> 16 (2 standard errors).
- Errors. Binned (jackknife-free) block means: 16 blocks after thermalisation; the error is the block standard error, with the integrated
  autocorrelation of the per-sweep series reported as a check. If tau_int exceeds a twentieth of the block length, the side is marked UNDER-SAMPLED.
- Lattice sums G_S and thresholds lam_* are recomputed in the script (floating, GUIDE) and compared with row 977's values.

## Step 2. Machine state, lock, efficiency rules (done 00:44Z)

- `memory_pressure`: 70 percent free at start. Numeric lock: `python3 scripts/lab_ops.py numeric-lock acquire --holder lane980-pinsheet-guide-w2`
  returned status acquired, holder_id lane980-pinsheet-guide-w2 (mine), expires 2026-11-15T10:44Z. One job at a time, BLAS threads 1, `nice`,
  RSS stop at 2 GB inside the program (lattice at S = 24, T = 48 is about 85 MB). No process pool.
- Repo search for prior work on these runs: grep of FINISH.md and library/ for `gap-pinsheet` finds only row 980 itself and row 977's
  proposal (gap-tiltproof-max.md 290, 413). Row 973's `lane973` scripts (sg2lab.py, a half-space slab with a frozen slice) are a different
  geometry; I wrote a new simulator rather than modify them. Not an open lemma, so no open-core check is needed: this is a GUIDE row.

## Step 3. Simulator and its validation (GUIDE; done 00:45Z)

Files: `library/guide/lane980/pinsheet.c` (SU(2) Wilson, Kennedy-Pendleton heat bath + 4 over-relaxation sweeps per sweep, frozen-link
mask for modes P1 and P3; compiled to /tmp, binary not kept), `analyze.py` (16-block errors, Sokal-window tau_int, jackknife xi),
`run.sh` (sequential driver with the memory check). Data in `library/guide/lane980/data/`.

Validation (each is an independent check of the update, not of the criteria):
- Unfrozen 8^4, beta 2.3, 300 sweeps: plaquette 0.60266 +- 0.00030; the large-volume value at beta 2.3 is about 0.6024 (RECALLED, not re-read). Agrees.
- Unfrozen 4^4, beta 0.2, 2000 sweeps: plaquette 0.049935 +- 0.00026 against the leading strong-coupling value I_2(0.2)/I_1(0.2) = 0.049917. Agrees.
- P1 pilot, S = 8, T = 16, 2000 sweeps (seed 21): E[a_0^2] = 0.2476 +- 0.0029, the value 1/4 forced by the plane-wise O(4) symmetry of
  Lemma D1(iii). Agrees. Pilot R_8 = 42.23 +- 0.02, tau = 0.7514 +- 0.0002, xi_2nd = 7.8 (about the side). Production numbers in Step 4.
- Speed: about 70 ns per link update on the M4 (one core).

Lattice sums (floating, GUIDE; agree with row 977 5.5 and 10.1): G_8 = 0.37929, G_12 = 0.44405, G_16 = 0.48992, G_24 = 0.55452.
Thresholds lam_* = 4A(1/4 - G_S/beta): 21.78, 32.79, 37.88 (and 20.52 on side 24, not a criterion). P3 thresholds G_S/beta: 0.1649, 0.1931, 0.2130.

Production plan (fixed 00:45Z, before any production data): P1 sides 8, 12, 16, 24 with T = 2S, 500/500/500/400 thermalisation sweeps
from the cold start, 10000/8000/5000/2500 measured sweeps; P3 sides 8, 12, 16 with 10000/8000/5000. One chain per side (seeds in run.sh).
Extra check added now: the infrared bound itself, Ghat^e(p_1) <= 1/(2 beta E(p_1)) (row 977 5.3), per component, from the p_1 data.

## Step 4. P1 results (GUIDE), sides 8 and 12 (analysed 00:56Z; sides 16 and 24 follow)

Raw data `library/guide/lane980/data/p1_S8_T16_seed801.txt`, `p1_S12_T24_seed1201.txt`; analysis output `data/analysis_p1_S8_S12.txt`.
Errors: 16 blocks of 625 (side 8) and 500 (side 12) sweeps.

| side | R_S = E|M|^2/A | R_S/A | lam_* (C1 bound) | tau = E<P,P'> | xi_2nd | Ghat^e(p_1) | IR bound 1/(2 beta E(p_1)) | E[a_0^2] |
|---|---|---|---|---|---|---|---|---|
| 8 | 42.241 +- 0.004 | 0.660 | 21.78 | 0.75130 +- 0.00010 | 7.84 +- 0.005 | 0.2851 | 0.7422 | 0.2512 +- 0.0006 |
| 12 | 89.939 +- 0.017 | 0.625 | 32.79 | 0.75116 +- 0.00006 | 12.33 +- 0.01 | 0.5385 | 1.6226 | 0.2501 +- 0.0017 |

Notes. tau_int of R is about 1 sweep (4 over-relaxation passes per sweep). The half-chain test on side 8 differs by 3.3 sigma
(42.229 against 42.252, a 0.05 percent shift): the block error there may be low by a factor up to about 3; this does not touch any
criterion (the C1 margin is thousands of standard errors). E[a_0^2] = 1/4 within errors on both sides (Lemma D1 symmetry).
The infrared bound of row 977 5.3 holds at p_1 with room (ratio 0.38 and 0.33).

**P1 side 16 (analysed 01:12Z; `data/p1_S16_T32_seed1601.txt`, `data/analysis_p1_S16.txt`; 16 blocks of 312 sweeps).**

| side | R_S | R_S/A | lam_* | tau | xi_2nd | Ghat^e(p_1) | IR bound | E[a_0^2] |
|---|---|---|---|---|---|---|---|---|
| 16 | 153.832 +- 0.032 | 0.601 | 37.88 | 0.75099 +- 0.00006 | 16.76 +- 0.02 | 0.8787 | 2.8559 | 0.2514 +- 0.0021 |

Half-chain test 0.97 sigma. (analyze.py: half-split fixed to whole blocks after a reshape error on this file; no number changed.)

## Step 5. P3 results (GUIDE), sides 8 and 12 (analysed 01:22Z; side 16 running)

Raw `data/p3_S8_T16_seed803.txt`, `data/p3_S12_T24_seed1203.txt`; analysis `data/analysis_p3_S8_S12.txt`. 16 blocks of 625 and 500 sweeps.
R^0_S = E[(sum_y a_0(y))^2]/A (a_0 = (1/2) tr P), averaged over the two slices; R4 := E|M|^2/A (all four components) for comparison with P1.

| side | q_0 | R^0_S | C1 bound A(q_0 - G_S/beta) | R^0_S/A | R4 | R4/4 | tau | Ghat^0(p_1) | IR bound |
|---|---|---|---|---|---|---|---|---|---|
| 8 | 0.2526 +- 0.0037 | 10.80 +- 0.27 | 5.61 | 0.169 | 42.37 +- 0.02 | 10.59 | 0.7520 +- 0.0002 | 0.2786 | 0.7422 |
| 12 | 0.2448 +- 0.0066 | 21.70 +- 1.11 | 7.45 | 0.151 | 90.29 +- 0.06 | 22.57 | 0.7517 +- 0.0002 | 0.5363 | 1.6226 |

tau_int of R^0 is 3.0 (side 8) and 7.8 (side 12) sweeps, under the 1/20-of-a-block limit; half-chain tests -0.8 and -1.4 sigma.
Observation (not a criterion): q_0 is 1/4 within errors and R^0 = R4/4 within errors, so with every other link pinned the free plane
still behaves as an O(4)-symmetric ordered sheet whose frame direction is nearly uniform; R4 equals P1's R_S within about 0.3 percent.
This is what row 977 9.1 ARGUED (q_0 = 1/4 up to winding effects); the run sees no winding effect at the 2 to 3 percent level.
The slow mode of R^0 is the drift of that frame direction, which no exact symmetry averages; its tau_int grows with the side.

**P3 side 16 (analysed 01:38Z; `data/p3_S16_T32_seed1603.txt`, `data/analysis_p3_S16.txt`; 16 blocks of 312 sweeps).**

| side | q_0 | R^0_S | C1 bound | R^0_S/A | R4 | R4/4 | tau | Ghat^0(p_1) | IR bound |
|---|---|---|---|---|---|---|---|---|---|
| 16 | 0.2435 +- 0.0066 | 36.67 +- 2.00 | 7.81 | 0.143 | 154.53 +- 0.11 | 38.63 | 0.7516 +- 0.0001 | 0.8865 | 2.8559 |

tau_int of R^0 = 14.4 sweeps against the limit 312/20 = 15.6: passes the fixed rule, narrowly; half-chain test -1.25 sigma.

**P3 verdicts (rules of Step 1, GUIDE).**
- C1 (test of 9.1(d)): R^0_S >= A(q_0 - G_S/beta): 10.80 >= 5.61, 21.70 >= 7.45, 36.67 >= 7.81. Holds on all three sides (not near the bound).
  The infrared bound itself also holds at p_1 (0.279, 0.536, 0.886 against 0.742, 1.623, 2.856). 9.1 is not withdrawn.
- C2: q_0 - 2 errors = 0.2452, 0.2316, 0.2303 >= 0.22 on sides 8, 12, 16. **"QUOT-CAP applies"** (GUIDE): the condition q_0 >= 0.24 of
  Proposition QUOT-CAP is met by the central values on all three sides (0.253, 0.245, 0.243) and by q_0 - 2 errors >= 0.22 as the criterion asks;
  q_0 - 2 errors is below 0.24 on sides 12 and 16, so the run supports the condition but does not place q_0 above 0.24 with 2-sigma margin.
- C3 (row 973 rule): g = (R^0_16/R^0_8)^(1/4) = 1.358, sigma_g = g(r_8 + r_16)/4 = 0.027; g - 2 sigma_g = 1.304 > 1.25. Steps 8 -> 12 and 12 -> 16 both
  increase (+9.5 and +6.6 sigma), so no decreasing step. **REFUTED (GUIDE) for a box-uniform (TILT-COV-quot) at beta 2.3** in the rule's sense.
  Robustness, reported, not part of the rule: with every error doubled g - 2 sigma_g = 1.2501 (still above, by 0.0001); with R4/4 in place of
  R^0 (the O(4)-averaged estimator, error 0.1 percent) g = 1.382. The row-977 expectation "growth factor near (L + 2)^2/L^2 per step" (1.56 to
  1.27 on 8 -> 16, about 1.41 averaged) matches within errors.
- Amendment (01:38Z, before the data it governs): one second P3 side-16 chain (seed 1604), run after P1 side 24, as a check of the
  error of R^0_16 only; the verdict above stays on the first chain by the fixed rule, the second chain is reported beside it.

## Step 6 (prepared 01:41Z, before any P2 data). P2 criterion, copied from gap-tiltproof-max.md 6.4 (line 297-298)

> Row P2 `gap-pinsheet-u1`: the same for compact U(1) at beta 2.3 with sides 8 to 32. Criterion: R_S/A does not fall by more than
> a factor 2 from side 8 to side 32 (power-law order). This tests the U(1) reading of 5.6.

Readings fixed now: compact U(1) Wilson action beta sum_p (1 - cos theta_p), beta 2.3 (Coulomb phase; transition near 1.01, RECALLED),
frozen set as P1; R_S := E|M|^2/A with M = sum_y e^(i theta_k(y)) (2 components), averaged over planes and the two slices. Sides 8, 16, 32
with T = 2S; 500/500/300 thermalisation and 8000/4000/1500 measured sweeps; same block and tau_int rules. Verdict: the criterion HOLDS if
(R_32/32^2)/(R_8/64) >= 1/2 with the 2-sigma margin on the safe side, FAILS if <= 1/2 likewise, else INCONCLUSIVE. Program
`pinsheet_u1.c` (von Mises heat bath, Best-Fisher; reflection over-relaxation), validated before production on two exact values:
strong coupling <cos theta_p> = I_1(beta)/I_0(beta) at beta 0.2, and the weak-coupling equipartition value 1 - 1/(4 beta) at beta 10.
Also, before P2 and after P1 side 24: a second P3 side-16 chain (seed 1604), Step 5 amendment. Driver `run2.sh`.

