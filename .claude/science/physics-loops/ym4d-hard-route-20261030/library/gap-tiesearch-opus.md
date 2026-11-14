lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-15T04:51Z

# gap-tiesearch-opus (FINISH row 973): GUIDE refutation test of box-uniform (TILT-COV-sup) at beta 2.3 and 2.4

Started 2026-11-14T16:51Z on Mac mini worker 2, pinned at a250c7f59. GUIDE level only: a run guides or refutes; it proves nothing.

## Plan (at most eight steps)

1. Read row 970 (library/gap-direction2-max.md sec. 3.4, 3.5, 4 A1, 7a), Lemma SUB, rows 950/952 runs and code (library/guide/lane952/, lane970/).
2. Write the criteria (REFUTED / NOT REFUTED) in this file before any run.
3. Set up library/guide/lane973/ by reusing lane952/lane970 code; dry-run small sizes.
4. Control: reproduce one beta 2.6 value of row 950/970 within 5 percent.
5. beta 2.4: tie-mode variance on sides 8..16, frozen slices incl. reduced-symmetry ones (as row 952).
6. beta 2.3: same.
7. Analysis: per-step growth factors vs 1.25; verdict per beta.
8. RESULT line.

## 1. Repo search, duplicate check, inputs (step 1; READ, no new claim)

Repo search (this folder; branches not searched beyond this checkout): the statement under test is row 970's box-uniform
(TILT-COV-sup) (`library/gap-direction2-max.md`, Sections 3.4, 3.5, 4 A1, 7a). Prior GUIDE data on frozen slices:
row 950 (`library/gap-sc-max.md` 5.5-5.8; Claude Fable 5.2) and row 952 (`library/gap-sg2test-opus.md` Sections 1-5;
Claude Opus 5.5), code `library/guide/lane952/sg2lab.py` (row 952) and `library/guide/lane970/twoslice_tilt.py` (row 970).
Duplicate check: `library/open-core.md` has no entry for (TILT-COV-sup); among FINISH rows only 968, 970 (which state and
refute it in the upper window), 971 (literature, reading only), 972 (check of row 970) and this row name it. Row 974 tests
attack A2 (the trajectory form), a different statement. No other row runs this test. Credit: all code reused here is
rows 952 and 970's; the slice families and the lemma are theirs.

What is known before this row (GUIDE, quoted from the files above):
- Lemma SUB (row 970, 3.4, PROVED there, check pending in row 972): for s in (0, 1/beta), u in M, z orthogonal to the gauge
  orbit of u, kbar_(s,0) >= Var_(pi_(beta u))(<z, w>)/(s'^2 |z|^2). pi_(beta u) is the one-step law of slice 1 of the
  temporal-gauge slab with slice 0 frozen at u. At the mid-slice s' = 1/(2 beta): kbar_(s,0) >= 4 beta^2 lambda, where
  lambda = Var(X_a) is the lag-0 (temporal-gauge, no frame average) second moment of a unit-normalised tie-mode amplitude
  X_a = sum_l eps_l E_l^a / sqrt(#links in the pattern) in one colour a, E_l = Im(w_l u_l^*).
- u_xy (row 950, 5.7), tie mode (pi,pi,0), (1,-1,0): beta 2.3: 2.03, 2.55, 2.51, 2.46 at L = 4, 6, 8, 10 (saturates);
  beta 2.4: 2.74, 8.00, 7.57 at L = 4, 8, 12 (saturates); beta 2.5: 3.56, 16.42, 42.73; beta 2.6: 4.19, 11.34, 22.62, 41.59, 64.87.
- u_phi (z-twist, phi = pi/2; row 952, 3.2), colour 3: beta 2.3 temporal-gauge raw moment 2.58, 3.16, 2.70 at L = 4, 6, 8
  (no growth); beta 2.45: 5.96, 11.8, 24.8 (growth, ratio 4.2 from L = 4 to 8). u_xyyz (mode xyz): beta 2.3 lambda_max 1.32, 1.43
  at L = 4, 8 (no order); beta 2.6: 3.5 -> 13.3.
- Not yet run anywhere: beta 2.4 on any slice other than u_xy; any slice on sides above 12 at beta 2.3-2.4; x-twist,
  twisted u_xyyz, interpolations at beta 2.3-2.4.

## 2. Criteria (written 16:53Z UTC, BEFORE any run of this row)

Object. The SU(2) Wilson half-space slab of row 952 (`sg2lab.py`): temporal gauge, slices t = 0..T, T = 6, slice 0 frozen at
the slice u, spatial torus of side L, slice T at half spatial weight. Observable for slice u and colour a:
lambda_a(L) := E[X_a^2] at lag 0 (no frame chain), X_a the tie-mode amplitude of the slice's named mode (`--mode xy`:
eps = (-1)^(x+y)(1, -1, 0), norm sqrt(2 L^3); `--mode xyz`: eps = (-1)^(x+y+z)(1, -1, 1), norm sqrt(3 L^3)). The raw moment is the
variance because E[X_a] = 0 by symmetry at every slice used (u_xy, u_xyyz: global colour rotations fix the slice;
twisted slices: the U(1) of row 952 1.4(b) for colours 1, 2 and the reflection S of 1.4(c) for colour 3); the run also
reports the mean, which must be within 3 standard errors of 0, else the slice is reported with the connected value.
The reported value per slice is lambda(L) = max over the colours that the slice's symmetry makes equivalent-or-singled-out
(u_xy, u_xyyz: colour mean lambda_star; twisted slices: colour 3). Errors: 8 blocks (sg2lab's blocks_mean).
Sides: L = 8, 10, 12, 14, 16 (a "step of the side" is L -> L + 2). Per-step growth factor
  g := (lambda(16)/lambda(8))^(1/4),  with error from the two block errors (propagated linearly).
Decision rules, per beta, over the slices searched:
- REFUTED (GUIDE) at beta: some slice has g - 2 sigma_g > 1.25, and no single step L -> L + 2 on 8..16 shows a decrease by more
  than 2 standard errors. (Row 970's criterion. Volume law gives (10/8)^3 = 1.95 down to (16/14)^3 = 1.49 per step;
  a critical L^(2 - eta) law gives about 1.41 on average over 8..16; so both refute.)
- NOT REFUTED at beta: every slice searched has g + 2 sigma_g <= 1.25. This means only that the slices tried on sides
  8 to 16 show no growth faster than 1.25 per step; it establishes no bound, says nothing about other slices, other modes,
  t > 0, slabs thicker than T = 6, or sides above 16. (A search that finds nothing does not prove a bound.)
- Otherwise INCONCLUSIVE at that beta (named slice and numbers).
Screening (to choose slices for the full sweep, not a verdict): L = 8 and 12 at beta 2.4 and 2.3 for each candidate; a slice
goes to the full sweep 8..16 if lambda(12)/lambda(8) > 1.2 at either beta, and u_xy and the z-twist go in any case at beta 2.4
(the slice families that order closest to the window, rows 950, 952).
Slices (reduced symmetry, as in row 952): u_xy (control family), z-twist u_phi at phi = pi/2 and pi/4, x-twist at pi/2,
u_xyyz (mode xyz), twisted u_xyyz at pi/2 (mode xyz, colour 3), interpolation u_xy -> u_pi at s = 0.5 (mode xy).
Controls (must pass, else the batch is reported as failed and decides nothing):
- (K1) row 950 reproduction: u_xy, beta 2.6, L = 8, lambda_star within 5 percent of 22.62 (row 950; row 952 batch 1 and row 970 7a
  reproduced it within 2 percent).
- (K2) u = 1, beta 2.3, L = 4: per-component variance of E within 3 percent of 0.160 (rows 944, 950, 952).
- (K3) equilibration at the largest side: at L = 16 the hot and cold starts agree within 15 percent for the slice that decides
  the verdict at each beta, else that point is reported as not equilibrated.
Resources: one job at a time under the numeric lock, nice, OMP/BLAS threads 1, RSS guard 2 GB (the brief says 3 GB; I use the
stricter FINISH value), start only at >= 50 percent memory free.

## 3. Code and first control (step 3)

Code: `library/guide/lane973/tielab.py` = row 952's `lane952/sg2lab.py` (Claude Opus 5.5, row 952) with three additions
for this row: an RSS guard (exit above 2 GB), `--noproxy` (skips the proxies Y of row 952, not used here), progress lines.
No change to the sampler or the observables. Lock: holder `gap-tiesearch-973`, acquired 16:53Z, 71 percent memory free.
- (K2) u = 1, beta 2.3, L = 4, 200 + 1500 sweeps: per-component variance 0.1599 +- 0.0008 against 0.160: **PASS**.
- Speed: about 34 ms per sweep at L = 16 (T = 6), so a side-16 point of 3000 + 12000 sweeps costs about 9 minutes.
- Batch S (screen) + (K1) launched 16:54Z: `lane973/screen.sh`, log `lane973/logs/screen.log`, JSON per run in `logs/`.
  K1: u_xy, beta 2.6, L = 8, 1500 + 6000. Screen: beta 2.4 then 2.3; L = 8 (1500 + 6000) and 12 (2000 + 8000);
  slices xy, z-twist pi/2 and pi/4, x-twist pi/2, xyyz (mode xyz), twisted xyyz pi/2 (mode xyz), interp s = 0.5. Cold starts.

- (K1) u_xy, beta 2.6, L = 8, 1500 + 6000 sweeps, cold: lambda_star = 22.92 +- 0.77 against row 950's 22.62 (1.3 percent): **PASS**.
  Note on the mean rule of Section 2: at beta 2.6 the colour frame drifts slowly, so the per-colour moments are 34.7, 10.4, 23.7
  and colour 1 has a mean 12 standard errors from 0 in this run. This is a slow global rotation, not a non-zero true mean
  (the slab law at u_xy is exactly invariant under constant colour rotations, so E[X_a] = 0 and the three colour variances are
  equal). For u_xy and u_xyyz I therefore read the colour mean lambda_star = E|X|^2/3, which is rotation invariant and equals the
  per-colour variance exactly; the mean rule is applied only to colour 3 of the twisted slices (this reading was fixed after K1 was read, while the screen ran, before any screen result was read).

- Code fix at 17:08Z (before any L = 12 or beta 2.3 screen point ran): the interpolation slice (s = 0.5) hung in thermalization.
  Cause: the Kennedy-Pendleton sampler of row 952 never accepts when a staple is exactly 0 (it occurs at the cold start of
  this slice). Fix in `tielab.py` kp_a0: for kappa < 0.5, the exact rejection sampler "a0 from the Haar marginal, accept with
  probability exp(kappa (a0 - 1))". Check: means of a0 at kappa = 0, 0.2, 3.0 are 0.0010, 0.0492, 0.5678 against the exact
  0, 0.0499, 0.5679 (400,000 draws, errors about 0.0008). Runs before the fix (K1, and the six L = 8 points at beta 2.4 below) used
  the old sampler; both samplers are exact for kappa > 0, so they are kept. The batch resumed as `screen2.sh` (skips finished runs).
- Screen, beta 2.4, L = 8 (1500 + 6000 sweeps; colour moments c1/c2/c3, mean/error per colour, lambda_star = colour mean):
  u_xy 7.45/5.95/7.20, lambda_star 6.87 +- 0.98 (row 950: 8.00); z-twist pi/2 colour 3: 12.07 +- 2.50 (mean/err 0.3);
  z-twist pi/4 colour 3: 7.08 +- 1.58; x-twist pi/2 colour 3: 8.82 +- 1.67 (mean/err -3.3: slow tunnelling between the two tied
  states, so the raw moment is noisy, see below); u_xyyz and twisted u_xyyz: see the table of Section 4.
  Reading rule for a colour-3 mean beyond 3 errors (stated at 17:08Z, after seeing the x-twist number): the exact symmetry S
  makes the true mean 0, so the raw moment remains the estimator of the variance; a large sample mean means the run did not
  tunnel often enough, and that point is flagged "under-sampled" rather than replaced by the connected value (which would
  remove exactly the tie being looked for). This replaces the "connected value" clause of Section 2.

## 4. Screen results (step 4; GUIDE)

**4.1 beta 2.4** (runs 16:54Z to 17:29Z; L = 8: 1500 + 6000 sweeps, L = 12: 2000 + 8000; cold start; errors from 8 blocks).
Value read: lambda_star (colour mean) for u_xy and u_xyyz; colour 3 for the twisted slices (with lambda_star in brackets).

| slice (mode) | lambda, L = 8 | lambda, L = 12 | ratio 12/8 | screen rule (> 1.2) |
|---|---|---|---|---|
| u_xy (xy) | 6.87 +- 0.98 | 6.07 +- 1.01 | 0.88 | no growth (row 950: 8.00, 7.57) |
| z-twist pi/2, colour 3 (xy) | 12.07 +- 2.50 [6.40] | 8.79 +- 2.03 [6.27] | 0.73 | no growth |
| z-twist pi/4, colour 3 (xy) | 7.08 +- 1.58 [6.43] | 8.83 +- 1.85 [9.60] | 1.25 (lambda_star 1.49) | passes the screen (noisy) |
| x-twist pi/2, colour 3 (xy) | 8.82 +- 1.67 [5.52] | 8.18 +- 2.88 [5.82] | 0.93 | no growth |
| u_xyyz (xyz) | 2.01 +- 0.19 | 1.87 +- 0.20 | 0.93 | no growth |
| twisted u_xyyz pi/2, colour 3 (xyz) | 2.50 +- 0.55 [1.81] | 2.19 +- 0.30 [1.90] | 0.88 | no growth |
| interp s = 0.5 (xy) | 0.85 +- 0.10 [0.57] | 1.00 +- 0.09 [0.63] | 1.18 | named mode small; but see 4.2 |

Mean rule: colour-3 means within 3 errors except z-twist pi/4 at L = 12 (4.3 errors) and x-twist at L = 8 (3.3): flagged
under-sampled (slow tunnelling between the tied states), as fixed at 17:08Z.

**4.2 A flag that is not a tie (interp slice).** The colour-averaged raw structure factor's top eigenvalue at k = (pi, pi, 0)
(over polarisations) is 5.05 at L = 8 and 16.75 at L = 12 (ratio 3.3, the volume ratio 3.375), on a polarisation other than
the named mode. This is a RAW moment: the interp slice is fixed only by the colour U(1) exp(alpha k), so the colour-3 mean of E
need not vanish, and a non-zero staggered mean of E gives |<E_k>|^2 of order L^3 trivially. A mean is not a variance and
does not enter Lemma SUB. At 17:30Z I added to `tielab.py` the connected structure factor (sample-mean field subtracted;
outputs `lambda_max_k_conn`, `mean_part_at_kmax`); the interp points at beta 2.4 are re-run with it after the beta 2.3 screen
(rule, fixed now: if the connected value at L = 12 over L = 8 is > 1.2, the interp slice joins the full sweep on its
connected top eigenvalue; the orthogonality of that mode to the gauge orbit would then be an open caveat).

**4.3 Plan of the full sweep at beta 2.4 (fixed 17:31Z, before it runs; `lane973/full24.sh`, log `logs/full.log`).**
Slices: u_xy and z-twist pi/2 (mandatory by Section 2), z-twist pi/4 (passed the screen). Sides 8, 16 first, then 12, 10, 14;
3000 thermalisation sweeps; 24000, 20000, 16000, 14000, 12000 measured sweeps at L = 8, 10, 12, 14, 16; cold start, seed 11.
K3: z-twist pi/4 at L = 16 from a hot start (seed 12). Before the sweep: the interp slice at L = 8, 12 with the connected
structure factor (4.2). The rules of Section 2 decide; g uses lambda(16)/lambda(8) of these long runs only (the screen
values are not pooled in).

**4.4 beta 2.3 screen** (runs 17:29Z to about 17:56Z; same lengths; the connected values exist from the runs started after 17:30Z).

| slice (mode) | lambda, L = 8 | lambda, L = 12 | ratio 12/8 | screen rule (> 1.2) |
|---|---|---|---|---|
| u_xy (xy) | 2.66 +- 0.20 | 2.71 +- 0.17 | 1.02 | no growth (row 950: 2.51 at L = 8, 2.46 at L = 10) |
| z-twist pi/2, colour 3 | 3.25 +- 0.21 [2.25] | 2.33 +- 0.34 [1.93] | 0.72 | no growth |
| z-twist pi/4, colour 3 | 2.55 +- 0.17 [2.30] | 2.82 +- 0.38 [2.44] | 1.11 | no growth |
| x-twist pi/2, colour 3 | 2.59 +- 0.33 [2.33] | 2.55 +- 0.34 [2.26] | 0.98 | no growth |
| u_xyyz (xyz) | 1.26 +- 0.08 | 1.10 +- 0.04 | 0.87 | no growth |
| twisted u_xyyz pi/2, colour 3 (xyz) | 1.32 +- 0.10 [1.14] | 1.04 +- 0.08 [1.11] | 0.79 | no growth |
| interp s = 0.5 (xy) | 0.68 +- 0.07 [0.50] | 0.75 +- 0.05 [0.53] | 1.10 | no growth; connected top eigenvalue 0.54 -> 0.53 |

Interp at beta 2.3, L = 8, with the connected structure factor: raw top eigenvalue 4.18 at (pi, pi, 0), of which the mean part
is 3.96; the connected top eigenvalue is 0.54. So the flag of 4.2 is a non-zero mean field (a deterministic staggered
response of slice 1 to this slice), not a fluctuation, and it does not enter Lemma SUB. (beta 2.4 re-run with the connected
value: in the full batch.) On every other slice the mean part is at most 0.18, as the symmetries require.

**4.5 Plan at beta 2.3 (fixed 17:51Z, before it runs; `lane973/full23.sh`, chained after the beta 2.4 batch).** No slice passed
the screen at 2.3. To give the verdict on sides 8 to 16 as Section 2 asks, the three xy-mode slices with the largest values
(u_xy, z-twist pi/4, z-twist pi/2) run at L = 8, 16, 12 (24000, 12000, 16000 measured sweeps, seed 21), and K3 is u_xy at L = 16
from a hot start. u_xyyz and its twist (values about half, falling) and x-twist (flat) are not continued; the verdict at 2.3
covers the slices of the screen at sides 8, 12 and these three at 16.

**4.6 Interp slice resolved (connected structure factor).** Connected top eigenvalue over all k and polarisations:
beta 2.4: 0.60 (L = 8), 0.64 (L = 12); beta 2.3: 0.54, 0.53. The raw values 5.08 -> 16.83 (2.4) and 4.18 -> 13.53 (2.3) are
mean parts 4.87 -> 16.62 and 3.96 -> 13.32, which scale as L^3: a non-random staggered mean of slice 1, not a variance. The
interp slice does not join the full sweep (rule of 4.2: connected ratio 1.07 at 2.4, below 1.2).
Screen conclusion: at beta 2.3 no slice grows from L = 8 to 12; at beta 2.4 only z-twist pi/4 passed (ratio 1.25, with
errors of about 20 percent); all go to the sweep as planned in 4.3 and 4.5.

## 5. Full sweep (step 5; GUIDE)

**5.1 beta 2.4, raw log lines as they arrive** (value read: lambda_star for u_xy; colour 3 for the twists, lambda_star in brackets).
- L = 8 (3000 + 24000): u_xy 7.54 +- 0.36; z-twist pi/2 9.63 +- 1.14 [5.27]; z-twist pi/4 6.13 +- 0.79 [6.28]. Means within 2.4 errors.

- L = 16 (3000 + 12000): u_xy 7.41 +- 0.72 (so lambda(16)/lambda(8) = 0.98 for u_xy; RSS 0.14 GB, 560 s).
- L = 16: z-twist pi/4 colour 3: 7.05 +- 1.72 [6.46] (ratio 16/8: 1.15); z-twist pi/2 colour 3: **17.04 +- 5.61** [9.10]
  (ratio 16/8: 1.77; colour-1 mean 3.3 errors from 0, colour-3 error 33 percent: few tunnelling events between the tied states).
- Interim per-step factors g = (lambda(16)/lambda(8))^(1/4), sigma_g = g (r_8 + r_16)/4 with r the relative errors:
  u_xy 0.996 +- 0.036 (g + 2 sigma = 1.07: not refuted on this slice); z-twist pi/4 1.036 +- 0.096 (g + 2 sigma = 1.23 <= 1.25: not
  refuted on this slice, barely); z-twist pi/2 1.153 +- 0.130 (between: INCONCLUSIVE on one chain).
- Added at 18:36Z, before any of them ran, because z-twist pi/2 now decides the verdict at 2.4 (`full24b.sh`, chained after
  the beta 2.3 batch): K3 for this slice (L = 16 hot, seed 31; the zt45 hot run of 4.3 stays as planned), two more cold chains at
  L = 16 (seeds 32, 33), one more at L = 8 (seed 32). Pooling rule: the colour-3 value at a side is the plain mean of the
  independent chains' values, error sqrt(sum err^2)/n; g is recomputed from the pooled values; K3 compares the hot chain with
  the mean of the cold ones (within 15 percent, else "not equilibrated").

- L = 12 (3000 + 16000): u_xy **12.69 +- 1.40** (connected 10.48); z-twist pi/4 colour 3 10.12 +- 3.39 [8.56]; z-twist pi/2 colour 3
  9.41 +- 2.45 [7.09]. Warning: u_xy at L = 12 is 12.69 +- 1.40 in this chain against 6.07 +- 1.01 in the screen chain (seed 1)
  and 7.57 in row 950, and above both L = 8 (7.54) and L = 16 (7.41). Two chains of the same point differ by 4 combined block
  errors, so at beta 2.4 the 8-block errors understate the true error: the colour-frame mode has an autocorrelation time
  comparable to the run. Every beta-2.4 number here must be read with this in mind; the verdict at 2.4 uses chain-to-chain
  spread where replicas exist (Section 6).

- Added at 18:52Z, before it runs (`full24c.sh`, chained after F24b): u_xy at beta 2.4, two more chains at L = 8 and two at
  L = 16 (seeds 32, 33), pooled by the rule of the z-twist replicas; the error of a pooled value is then the larger of the
  propagated block error and the chain-to-chain standard error of the mean.

- L = 10 (3000 + 20000): u_xy 8.54 +- 0.73; z-twist pi/4 colour 3 8.55 +- 1.23 [7.11]; z-twist pi/2 colour 3 7.92 +- 1.72 [5.02].

