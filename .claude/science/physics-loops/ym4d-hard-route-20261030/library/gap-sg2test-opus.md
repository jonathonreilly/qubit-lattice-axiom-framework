lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-14T21:59Z

# Row 952 (`gap-sg2test-opus`): GUIDE refutation test of (SG2)

Started 2026-11-14 09:59Z on the Mac mini, worker 1, pinned at commit 8ce7831ef. Claude Opus 5.5, max effort, as author.
This is a GUIDE item: a run may refute (SG2) or guide; no run proves anything. Every statement is marked PROVED,
CONDITIONAL (on named inputs), GUIDE or OPEN. Scripts and logs: `library/guide/lane952/`.

Builds on row 950 (`library/gap-sc-max.md`, Sections 5 and 7: (SG2), frame-lag test 7.4, first run 7.5) and on the
Sussman-Alpoge account (outline `YM4_sketch_500.tex` and complete account at commit 31a47c543775; credited where used).

## 0. Plan (at most eight steps; one step per response; each result appended before the next)

1. Read row 950 Sections 5 and 7 (and row 951 if present). Restate (SG2) and the frame-lag observable exactly.
   Write pass and fail criteria before any run. Duplicate check against `library/open-core.md` and FINISH rows.
2. Port or rebuild the frame-only heat-bath code (row 950's scripts if found). Run the two controls:
   compact U(1) at u_xy must grow like L^3; the temporal-gauge covariance C_0 must reproduce row 950's volume growth at
   beta 2.5-2.6.
3. Slice family A: anisotropic deformations of the layered pi-flux slice u_pi; beta 2.3, 2.45, 2.6; L sweep.
4. Slice family B: tilted copies of u_xy at several tilt angles.
5. Slice family C: slices drawn from the vacuum (typical slices, which the averaged chain sees).
6. Slice family D: slices interpolating between two gauge-inequivalent near-degenerate configurations.
7. Analysis: top eigenvalue versus L with errors and lag convergence, per slice and coupling; verdict per cell.
8. RESULT line.

Compute budget: about 60 minutes in total, one numeric job at a time under `scripts/lab_ops.py numeric-lock`,
BLAS threads 1, nice, peak memory under 2 GB, started only at 50 percent memory free or more.

## 1. Inputs, the statement under test, a new slice family, and criteria (step 1; written before any run)

**1.1 Inputs read.** Row 950 (`library/gap-sc-max.md`, Claude Fable 5.2, unchecked): Sections 5.1-5.2, 5.5-5.8, 6,
7.1-7.6, 8 (READ). Row 951 (its check) is not on disk at 8ce7831ef. Row 950's scripts sit in a scratch folder of another
session (`/tmp/gap-sc-950/`), outside my scope, so the code here is rebuilt from row 950's text alone.
Duplicate check (rule 0a): `library/open-core.md` has no entry for (SG2) or the frame-lag test; among the FINISH rows
only 950 (which defines (SG2)), 952 (this row) and 953 (its check) name it. No other row attacks it.

**1.2 The statement under test (row 950, 7.3-7.4, quoted in substance).** Model: SU(2) Wilson half-space slab in
temporal gauge, slices t = 0..T (T = 6), slice 0 frozen at the Dirichlet datum u, spatial plaquettes of slice T at
weight beta/2, spatial torus of side L. Links are unit quaternions; <a, b> = Re(a b^*).
First-step field E_l = Im(w_l u_l^*), w = slice 1, l = (x, i). Frame law, given both slices:
  mu_(u,w)(dg) proportional to exp( beta sum_l <u_l, g_x w_l g_(x+i)^*> ) prod_x dg_x   (Haar),
Ebar_l(u, w) := E_(mu_(u,w)) Im( (g.w)_l u_l^* ), a function of u and of the gauge orbit of the slab t >= 1.
  (SG2)  sup_u || Cov_(pi_u)(Ebar) ||_op <= sigma_2^2/beta^2, box-free.
Frame-lag test (7.4): run the frame heat bath from g = 1 on each sampled w; E^(n) := Im((g^(n).w) u^*);
C_n := Cov(E^(0), E^(n)) tends to Cov_(pi_u)(Ebar) (row 950, PROVED there).
I use a palindromic sweep (sites forward, then backward). Then the kernel is K = A A^*, self-adjoint and positive on
L^2(mu), so for every fixed vector v the lagged value v^T C_n v DECREASES in n to v^T Cov(Ebar) v (PROVED: spectral
theorem; E[E^(0) | orbit] = Ebar as in row 950). So a lagged value at finite n is an upper bound of its limit, and a
refutation cannot rest on it alone.

**1.3 A lower bound that needs no frame chain (Lemma LB; PROVED).** Let X = <v, E^(0)> for a fixed unit vector v,
Xbar = <v, Ebar>, and let Y_1..Y_m be functions of the gauge orbit of the slab t >= 1 alone (gauge-invariant
functions of slices 1..T). Let c_j = Cov(Y_j, X), G = Cov(Y). Then
  lambda_max( Cov(Ebar) ) >= Var(Xbar) >= c^T G^(-1) c.
Proof. E[X | orbit] = Xbar (the temporal-gauge draw is an exact draw of the frame given the orbit; row 950 7.4).
So Cov(Y_j, X) = Cov(Y_j, Xbar), and c^T G^(-1) c is the variance of the best linear predictor of Xbar from Y, which
is at most Var(Xbar) <= lambda_max. QED.
So a lower bound needs only outer samples and a gauge-invariant proxy Y. I report it beside the lagged values; the
truth lies between them. (Statistical bias: one or two regressors, thousands of samples; I also fit on one half of
the samples and evaluate on the other.)

**1.4 A new slice family: u_xy with a flat colour twist along z (design; the lemmas are PROVED, the prediction is
ARGUED).** Write k for the quaternion unit of colour 3. For delta = phi/L put
  u_phi:  x- and y-links as u_xy (u_y(x,y,z) = (-1)^x, u_x = 1),  every z-link = exp(delta k).
(a) u_phi is flat on every xz and yz plaquette, and its xy plaquettes are those of u_xy. The gauge transformation
k(z) = exp(z delta k) maps it to u_xy with a seam: the z-links from z = L-1 to z = 0 carry exp(phi k). So u_phi is
locally gauge equivalent to the central slice u_xy and differs from it only by the z-holonomy exp(phi k). (PROVED,
direct computation: the x, y links are +-1 and commute with k.)
(b) For phi not in {0, pi} (mod 2 pi) the constant gauge transformations that fix u_phi are exp(alpha k) and -exp(alpha k).
For every such c the frame law is invariant under g -> c g, and Ebar_l = Ad_c Ebar_l. Hence **Ebar_l is parallel to e_3
on every link, for every w** (PROVED: c commutes with every u_l, so <u_l, c (g.w)_l c^*> = <u_l, (g.w)_l> and
Im(c (g.w)_l c^* u_l^*) = Ad_c Im((g.w)_l u_l^*); Haar is left invariant).
(c) Let S = (conjugation by the quaternion unit i) composed with the reflection z -> -z of every slice. S maps
exp(delta k) on z-links to exp(-delta k) and back, and fixes the z-independent real x, y links: S(u_phi) = u_phi. The slab
measure with datum u_phi is S-invariant. On the tie-mode amplitude X_3 := sum over x, y links of eps_l Ebar_l^3 / sqrt(2 L^3)
(eps_l = (-1)^(x+y) on x-links, -(-1)^(x+y) on y-links, row 950 5.1) S acts as X_3 -> -X_3. So E[X_3] = 0, and the raw
second moment of X_3 is its variance under pi_(u_phi) (PROVED).
(d) S is a lattice reflection, not a gauge transformation. The two staggered patterns with colour direction n = +e_3 and
n = -e_3 on slice 1 are exchanged by S. They are gauge INEQUIVALENT as slices when sin(4 theta) sin(phi) != 0: the closed
loop "xy plaquette at (x, y, 0), then once around z" has trace -2 cos(4 theta e_p + phi) for n = +e_3 and -2 cos(4 theta e_p - phi)
for n = -e_3 (PROVED in the abelian pattern; theta is the pattern angle of row 950 5.1).
(e) Prediction (ARGUED). Locally u_phi is u_xy, so its boundary layer has the same colour order as u_xy: none at
beta 2.3, order at beta >= 2.5 (row 950, GUIDE). The holonomy makes n relative to the z-axis gauge invariant: a pattern
with n perpendicular to e_3 must wind by 2 phi along z (cost of order rho L phi^2), so n -> +-e_3, an Ising order tied by S.
The frame is pinned by the seam (cost of order beta L per unit rotation off the U(1) of 1.4(b)), so Ebar keeps a fixed
fraction c of the e_3 part of the pattern, and Var(X_3) is about c^2 sin^2(theta) (2 L^3) E[cos^2 alpha], alpha the angle of n to e_3.
**If the colour order of u_xy at beta >= 2.5 is real, (SG2) fails at u_phi with growth like L^3.** The same order is pure
frame at phi = 0 (Lemma CEN, row 944), so row 950's conclusion that SU(2) cannot fail (SG2) "this way" does not cover
this slice: what the holonomy does is turn the frame order into gauge-invariant data. Row 950 tested a different tilt
(along the pattern, which is not flat and acts as an explicit field on n; no tie).
Gauge-invariant proxy for Lemma LB at u_phi: with H(x, y) = product of the z-links of slice 1 around z from (x, y, 0) and
U_p the xy plaquette of slice 1 at (x, y, 0), Y := sum over (x, y) of e_p Re(U_p H(x, y)) / sqrt(L^2), e_p = (-1)^(x+y).
In the abelian pattern Re(U_p H) = -cos(4 theta) cos(phi) + e_p sin(4 theta) sin(phi) (n . e_3), so Y is S-odd and reads n . e_3.

**1.5 Pass and fail criteria (fixed here, before any run).** Notation per slice and coupling: A_lo(L) = the bound of
Lemma LB on the named mode (split-sample), A_n(L) = v^T C_n v at lag n (n = 0 is the temporal-gauge value), each with a
standard error from 8 blocks.
- REFUTES (SG2) at that coupling (GUIDE): A_lo increases at each step of the L sweep by more than 2 standard errors, and
  A_lo(L_max)/A_lo(L_min) >= 2.5 with L_max/L_min = 2. (Volume growth gives 8; a critical point L^(2-eta) gives about 3.5.)
- Saturation (no refutation; establishes nothing): A_lo and A_64 change by at most 30 percent from the middle size to L_max.
- Otherwise inconclusive; the frame-lag value A_n must also show lag convergence (A_64/A_16 within 10 percent) before it
  is read as the limit.
- For families without a gauge-invariant proxy (vacuum slices, interpolations), the observable is the top eigenvalue of
  the split-sample estimate of lim C_n over all links and colours, with the same growth rule.
Controls (must pass, else the batch is reported as failed): (C1) u = 1, beta 2.3, L = 4: per-component variance of E in
temporal gauge 0.160 within 3 percent (rows 944, 950). (C2) u_xy, beta 2.6: the temporal-gauge tie-mode value lambda_* at
L = 4 and 8 within 15 percent of row 950's 4.19 and 22.6 (volume growth of C_0). (C3) compact U(1), u_xy, beta 2.3: the
lag-64 value of the tie mode must grow from L = 4 to 6 by a factor >= 2.5 (volume: 3.4), and equal the lag-0 value within
10 percent. (C4) estimator null test: at phi = 0 (u_xy itself) Ebar = 0 exactly (Lemma CEN), so A_lo must be within 2
standard errors of 0, and A_n must fall toward 0.

## 2. Code and controls (step 2)

**2.1 Code.** `library/guide/lane952/sg2lab.py` (numpy, one thread, nice; written for this row from row 950's text):
quaternion links, Kennedy-Pendleton heat bath, checkerboard by direction and parity of x + y + z + t; frame chain on
g_x with the palindromic sweep (parity 0, 1, 0) of 1.2; Lambda(k) by FFT; tie-mode amplitudes X_a; the proxy Y of 1.4
on slices 1 and 2; Lemma LB with one regressor (product of the two half-sample means of Y X_3 over the mean of Y^2) and
with two regressors (Y_1, Y_2); optional split-sample PCA of lim C_n over all 9 L^3 coordinates; a compact U(1) branch
(von Mises heat bath) with the U(1) proxy Y = sum over xy plaquettes of slice 1 of e_p sin(theta_p) (gauge invariant).
Logs (JSON): `library/guide/lane952/logs/`. Speed: 1.3 ms per sweep at L = 4, T = 6.

**2.2 Control C1 (run about 10:14Z under the numeric lock, 71 percent memory free).** u = 1, beta 2.3, L = 4,
1500 sweeps after 200: per-component variance 0.1597 +- 0.0005 against 0.160 (rows 944, 950): **PASS**. (The k = 0 value of
Lambda is 0.294; the max over k is 0.319 at a noisy k on a flat top, against row 950's 0.2984 from 20000 sweeps.)

**2.3 Batch 1 plan (fixed before it runs).** All T = 6, cold start, measured every sweep, a frame chain every 20 sweeps
with lags 0, 1, 2, 4, 8, 16, 32, 64.
(i) C2 + C4: u_xy, beta 2.6, L = 4 (1000 + 8000 sweeps) and L = 8 (1500 + 6000).
(ii) Twisted u_phi, phi = pi/2, beta 2.6, L = 4, 6, 8 (same lengths; L = 6: 1200 + 7000).
(iii) C3: compact U(1), u_xy, beta 2.3, L = 4 and 6 (1000 + 6000; frame chain every 20).
Reading rule for (ii): the criteria of 1.5 on A_lo (one regressor, split halves) and on the lagged X_3 moment.

**2.4 Code additions before batch 1 ran (10:16Z).** The first launch of batch 1 ran no job (a zsh word-splitting error in
the runner; nothing was computed). Before the relaunch I added: slice kinds `xyyz` (u_x = 1, u_y = (-1)^x, u_z = (-1)^y:
flux -1 on xy and yz, +1 on xz; an anisotropic deformation of u_pi, see 3.1), `xyyztwist`, `xtwist` (u_xy with a flat
colour twist along x), the general proxy Y(plane, sign pattern, holonomy direction), and `--pca3` (raw-moment split-sample
PCA of the e_3 components of lim C_n, which by 1.4(b) is all of Cov(Ebar) at a twisted slice; 3 L^3 coordinates).
Smoke runs (under the lock, L = 4, beta 2.6, 600 sweeps, 20 frame chains; not used for any verdict) at phi = pi/2:
twisted u_xy put the tie mode on e_3 (temporal-gauge raw moments 0.51, 0.87, 11.4 for colours 1, 2, 3) and the lagged
X_3 moment stayed at 10.7 at lag 64, while X_1 fell from 0.66 to 0.23; Lemma LB gave 4.2. So at L = 4 the frame average
keeps the e_3 order, as 1.4(e) predicts. Twisted u_xyyz and twisted u_pi gave tie-mode moments of 0.3-0.4 at L = 4.
[Correction, 11:57Z: those two smoke commands did not pass `--mode xyz`, so they measured the xy tie mode, which is not
the pattern of u_xyyz. They say nothing about order on the xyz mode; see 3.3 for the proper screen.]

**2.5 Batch 2 plan (fixed at 10:19Z, before batch 1 reported; chained to start when batch 1 ends).** Twisted u_xy (phi = pi/2)
at beta 2.3 and 2.45, L = 4, 6, 8 (lengths as batch 1, `--pca3`). Twist along x (`xtwist`, proxy with the x-holonomy) at
beta 2.6, L = 4 and 8. Twist angle phi = pi/4 at beta 2.6, L = 4 and 8. Criteria: those of 1.5, per coupling and per slice.

## 3. Results

**3.0 Batch 1 (run 10:18-10:22Z under the numeric lock, 70 percent memory free).** Log `library/guide/lane952/logs/batch1.log`,
JSON `logs/b1_*.json`, table by `summarize.py`. Errors are one standard error from 8 contiguous blocks.
A_lo = Lemma LB (proxy Y_1, split halves); A_n = lagged raw moment E[X_3^(0) X_3^(n)] of the e_3 tie mode (frame chain every
20 sweeps: 400, 350, 300 chains at L = 4, 6, 8); PCA = split-sample top eigenvalue of the lag-64 raw moment matrix of all
e_3 components (3 L^3 coordinates; two halves).

| slice | beta | L | temporal-gauge raw moments X_1/X_2/X_3 | A_0 | A_8 | A_16 | A_64 | A_lo | PCA (halves) |
|---|---|---|---|---|---|---|---|---|---|
| u_xy (C2, C4) | 2.6 | 4 | 3.42/4.73/4.68 (lambda_* 4.28 +- 0.14) | 4.77 | 3.36 | 2.62 | 0.59 +- 0.24 | 0.00 +- 0.00 | |
| u_xy (C2, C4) | 2.6 | 8 | 50.9/3.8/10.2 (lambda_* 21.6 +- 0.7) | 9.99 | 9.45 | 9.39 | 7.26 +- 1.37 | 0.02 +- 0.02 | |
| **u_phi, phi = pi/2** | **2.6** | 4 | 1.35/1.46/7.91 | 7.81 | 7.10 | 6.82 | **6.37 +- 0.58** | **2.96 +- 0.58** | 6.9, 5.7 |
| **u_phi** | **2.6** | 6 | 1.90/2.40/27.2 | 27.4 | 26.1 | 25.5 | **24.9 +- 1.1** | **10.65 +- 0.79** | 24.4, 24.7 |
| **u_phi** | **2.6** | 8 | 5.48/7.03/50.0 | 50.3 | 49.5 | 49.4 | **49.2 +- 5.1** | **15.5 +- 3.6** | 52.5, 43.4 |

Compact U(1), u_xy, beta 2.3 (C3): lagged moment 41.40 (lag 0) and 41.30 +- 0.15 (lag 64) at L = 4; 139.82 and 139.69 +- 0.30 at
L = 6; A_lo (U(1) plaquette proxy) 38.1 and 136.2.
**Controls.** C1 PASS (2.2). C2 PASS: lambda_* = 4.28 +- 0.14 and 21.6 +- 0.7 against row 950's 4.19 and 22.6 (2 and 4 percent): the
temporal-gauge covariance C_0 grows like the volume at u_xy, beta 2.6, as in row 950. C3 PASS: the U(1) lag-64 value grows by
3.38 from L = 4 to 6 (volume ratio 3.375) and equals the lag-0 value within 0.3 percent; the frame chain removes nothing, as
row 950 7.6 found. (This L = 4 run sat in the ordered state, 41.3; row 950's frame run had a metastable 19.1.) C4: A_lo = 0
within errors at u_xy (PASS); the lagged moments fall toward 0 (to 12 percent of lag 0 at L = 4 by lag 64), but at L = 8
the global SU(2) frame rotation is slow (78 percent of colour 1 left at lag 64), as row 950's validation (V) found. This
slowness is the free rotation of the frame at a central slice. At u_phi it does not touch X_3: by 1.4(b) the frame law is
invariant under exp(alpha k), which fixes e_3.
**Twisted slice, beta 2.6.** Lag convergence holds at all three sizes (A_64/A_16 = 0.93, 0.97, 0.99). The frame-averaged tie
moment grows like the volume: A_64 = 6.4, 24.9, 49.2 at L = 4, 6, 8; volume scaling from L = 4 predicts 21.5 and 51. The
temporal-gauge order sits almost wholly on e_3 (27.2 against 1.9 and 2.4 at L = 6), as 1.4(e) predicts. The PCA top
eigenvalue agrees with the tie mode. Against 1.5: the lag criteria are met; A_lo grows 2.96 -> 10.65 -> 15.5 (ratio 5.2 >= 2.5),
but the step from L = 6 to 8 is 1.3 standard errors, below the 2 required. **So by the criteria written before the run,
beta 2.6 is not yet a refutation: inconclusive on A_lo, volume growth on the lagged values (upper side).** Cause: the proxy
Y_1 reads n . e_3 through the winding holonomy H, whose angle wanders by a random walk along z, so its correlation with X_3
falls (A_lo/A_64 = 0.46, 0.43, 0.32 at L = 4, 6, 8). Remedy in batch 3: a proxy built on z-links averaged over slices 1-3
(the frame acts on all slices t >= 1 in the same way, so the average transforms like one link and the proxy stays gauge
invariant), larger L, and a long-lag check.

**3.1 Batch 3 plan and criteria (fixed at 10:26Z, before batch 2 or 3 reported; script `batch3.sh`, code `sg2lab_b3.py`).**
New proxies (all gauge invariant, functions of slices 1..T only): Y_3 = sum_x e_p <Im P_1(x), axis of H~(x)> / sqrt(L^3), with
H~ the z-holonomy of the z-links averaged over slices 1-3 and normalised, P_1 the xy plaquette of slice 1; Y_4 the same with
the normalised sum of the plaquettes of slices 1 and 2. Primary lower bound, chosen now: **A_lo := LB134**, Lemma LB with
regressors (Y_1, Y_3, Y_4), coefficients fitted on one half of the samples and applied to the other (`lb_multi`).
(a) Twisted u_xy, phi = pi/2, beta 2.6, L = 4, 6, 8, 10, 12; lags to 512 at L = 8.
Criterion for (a), written now because batch 1 showed that the per-step rule of 1.5 cannot be met by five sizes whose steps
are 20-40 percent: **REFUTES (SG2) at beta 2.6** if A_lo(8) - A_lo(4) and A_lo(12) - A_lo(6) both exceed 2 combined standard
errors and both ratios are >= 2.5, and the lagged values plateau (A_512 within 10 percent of A_16 at L = 8). Saturation if
A_lo(12)/A_lo(6) <= 1.3. Otherwise inconclusive. The verdict of batch 1 under 1.5 stays as written ("inconclusive").
(b) Screening (criteria of 1.5): family A = u_xyyz (flux -1 on xy and yz; tie mode (pi, pi, pi), polarization (1, -1, 1)) at
beta 2.3 and 2.6, and u_pi at beta 2.6, temporal gauge only, L = 4 and 8: does the boundary layer order (volume growth of the
max over k of Lambda)? Family D = the interpolation u_z = exp(s pi [x + y odd] k) from u_xy (s = 0) to u_pi (s = 1) at s = 0.5,
with the z-twist, beta 2.6, L = 4 and 8 (frame chains, e_3 PCA). Family C = vacuum slices (middle slice of a free slab of
12 slices, 600 sweeps) at beta 2.3 and 2.6, L = 4 and 6, frame chains to lag 32, split-sample PCA over all 9 L^3 coordinates
(mean subtracted). Family C has little power: with 400 chains and up to 1944 coordinates the split estimate of the top
eigenvalue is biased low. A bounded value there establishes nothing.

**3.2 Batch 2 (run 10:22-10:30Z under the lock, 71 percent free).** Log `logs/batch2.log`, JSON `logs/b2_*.json`. Same columns as
3.0; A_lo is LB with Y_1 (the holonomy along the twist direction), split halves. Criteria of 1.5.

| slice | beta | L | temporal-gauge X_1/X_2/X_3 | A_0 | A_16 | A_64 | A_64/A_16 | A_lo | PCA (halves) |
|---|---|---|---|---|---|---|---|---|---|
| u_phi (z), phi = pi/2 | 2.3 | 4 | 0.96/1.09/2.58 | 2.59 | 1.75 | 1.42 +- 0.19 | 0.81 | 0.24 +- 0.06 | 1.2, 1.4 |
| u_phi (z), phi = pi/2 | 2.3 | 6 | 1.47/1.24/3.16 | 3.12 | 1.98 | 1.23 +- 0.18 | 0.62 | 0.08 +- 0.02 | 0.8, 0.9 |
| u_phi (z), phi = pi/2 | 2.3 | 8 | 2.09/1.81/2.70 | 2.81 | 1.89 | 1.35 +- 0.32 | 0.71 | 0.01 +- 0.01 | 0.6, 0.7 |
| u_phi (z), phi = pi/2 | 2.45 | 4 | 1.09/1.26/5.96 | 5.90 | 4.58 | 4.33 +- 0.49 | 0.95 | 1.68 +- 0.38 | 4.3, 4.1 |
| u_phi (z), phi = pi/2 | 2.45 | 6 | 2.84/2.27/11.8 | 11.5 | 10.4 | 9.44 +- 0.91 | 0.91 | 2.04 +- 0.41 | 7.5, 10.6 |
| u_phi (z), phi = pi/2 | 2.45 | 8 | 2.71/2.38/24.8 | 25.3 | 23.6 | 21.9 +- 2.2 | 0.93 | 2.55 +- 0.77 | 21.3, 19.8 |
| **u_xy twisted along x, phi = pi/2** | **2.6** | 4 | 2.11/2.45/4.82 | 4.90 | 4.17 | 3.35 +- 0.36 | 0.80 | **1.62 +- 0.32** | 3.0, 3.4 |
| **u_xy twisted along x, phi = pi/2** | **2.6** | 8 | 13.0/4.5/43.2 | 44.4 | 43.4 | 41.7 +- 2.7 | 0.96 | **20.9 +- 4.1** | 38.7, 41.5 |
| u_phi (z), phi = pi/4 | 2.6 | 4 | 3.41/4.00/4.83 | 4.89 | 3.30 | 2.55 +- 0.22 | 0.77 | 0.53 +- 0.13 | 1.9, 2.7 |
| u_phi (z), phi = pi/4 | 2.6 | 8 | 12.8/18.1/35.7 | 35.0 | 33.6 | 31.5 +- 5.8 | 0.94 | 3.4 +- 1.6 | 38.5, 21.9 |

**Verdicts against 1.5 (GUIDE).**
- **beta 2.6, u_xy twisted along x: (SG2) REFUTED on the boxes run.** A_lo rises from 1.62 +- 0.32 to 20.9 +- 4.1 between L = 4 and 8:
  +19.3, 4.6 combined standard errors, ratio 12.9 >= 2.5. A_lo is the lower side (Lemma LB, no frame chain). The lagged value at
  L = 8 has converged (A_64/A_16 = 0.96) and sits at 41.7, so the frame-averaged tie moment is between 21 and 42 at L = 8, against
  1.6 to 3.4 at L = 4. The tie vector v (eps_l e_3 on x and y links) has zero covariant divergence at this slice (its x and y
  links are central), so z_v is horizontal and Var(phi_(u,z_v)) = beta^2 Var(<v, Ebar>): **(SG-step) in gauge-invariant form
  fails with it, with the same growth (GUIDE).**
- beta 2.6, z-twist at phi = pi/4: lagged values grow 2.55 -> 31.5 (lag-converged at L = 8); A_lo 0.53 -> 3.4 is 1.8 standard
  errors: inconclusive on A_lo. Smaller phi pins n to e_3 more weakly (the temporal-gauge order spreads over the three
  colours, 12.8/18.1/35.7), as the cost rho L phi^2 of 1.4(e) predicts.
- beta 2.45, z-twist at phi = pi/2: the lagged values grow 4.33 -> 9.44 -> 21.9 (ratio 5.1 from L = 4 to 8; lag-converged within
  10 percent at all sizes), with the temporal-gauge order on e_3 (24.8 against 2.7 and 2.4 at L = 8). A_lo 1.68 -> 2.04 -> 2.55
  stays within errors: **inconclusive by 1.5** (growth on the upper side only; the holonomy proxy is weak here).
- beta 2.3, z-twist at phi = pi/2: no growth. A_64 is 1.42, 1.23, 1.35 (it was still falling at lag 64, so the limit is lower);
  A_lo falls to 0; the PCA top falls 1.3 -> 0.9 -> 0.6. Saturation: (SG2) survives this slice at beta 2.3 (establishes
  nothing). Row 950 found no colour order at u_xy at beta 2.3 (finite correlation length, level 2.5), and the twist
  converts only existing order into gauge-invariant data.

## 4. What the refutation means (by hand; written while batch 3 runs)

**4.1 Proposition TW (PROVED).** Let u be u_xy with a flat colour twist along d in {x, z}: every d-link multiplied by
exp((phi/L) k), phi not in pi Z. Then (i) u is flat on every plaquette except the xy ones, where it equals u_xy, and a gauge
transformation moves the twist into one seam of d-links carrying exp(phi k): u is locally gauge equivalent to u_xy;
(ii) the constant gauge transformations fixing u include exp(alpha k), so Ebar_l is parallel to e_3 for every l and every
next slice (1.4(b)); (iii) S_d = (conjugation by i) composed with the reflection of the d-axis fixes u, preserves the tie
vector eps (a reversed link reverses the sign of E, and eps on the reflected links matches), and maps X_3 to -X_3, so
E[X_3] = 0 under pi_u; (iv) the tie vector v = eps e_3 / sqrt(2 L^3) has zero covariant divergence at u (its links are the
central x and y links, and eps has zero lattice divergence), so z_v = (v_l u_l) is horizontal and
Var_(pi_u)( phi_(u,z_v) ) = beta^2 Var_(pi_u)( <v, Ebar> ) >= beta^2 A_lo   (Lemma LB).
Proof: (i), (ii), (iii) as in 1.4 with d in place of z (for d = x: the y-links (-1)^x are even under x -> -x; the x-links
exp(delta k) are reversed to exp(-delta k) and conjugation by i restores exp(delta k)); (iv) is the definition of 6.1 of
row 950 with u_l^* xi_l u_l = xi_l on central links. QED.

**4.2 Reading (ARGUED; the runs are GUIDE).** Row 950 found that the colour direction n of the first-step pattern orders at
u_xy for beta >= 2.5, and that for SU(2) this order is pure gauge frame at u_xy itself (Ebar = 0 there, Lemma CEN), because
charge conjugation is inner. A flat holonomy along one axis costs nothing locally, but it gives the slab a gauge-invariant
reference axis: the angle of n to the holonomy axis becomes gauge-invariant data (the winding loop of 1.4(d) reads it). A
pattern with n off the axis must wind around it along d (cost of order rho L phi^2), so n -> +-e_3. The reflection S_d, which is
a lattice symmetry and not a gauge transformation, ties the two states. So the frame order of row 950 turns into an order of
gauge-invariant boundary data with an exact tie: the "tie between gauge-inequivalent next slices" that row 950 7.3 named as
the only way to violate (SG2). It needs no fine tuning and no first-order transition: it holds on the whole ordered side.
Row 950's conclusion "the SU(2) chain cannot fail (SG-step) this way" (7.2) is right for charge conjugation and does not
cover lattice reflections combined with a colour rotation.

**4.3 General form (ARGUED).** If at coupling beta some central slice u_c has an ordered Dirichlet boundary layer (the
temporal-gauge first-step susceptibility grows like the volume), and u_c has a reflection symmetry along an axis d, then
the flat twist of u_c along d violates (SG2) and (SG-step) at beta, with Var(<v, Ebar>) of the order of the frame-averaged
ordered moment. So (SG2) at beta needs that no Dirichlet boundary layer orders at beta, over all slices: a statement of
uniqueness of the boundary Gibbs state, uniform in the datum. Any proof of (SG-step) must use a property of that kind,
and must fail for the twisted u_xy at beta 2.6 (fact test).

**4.4 Batch 4 plan and criteria (fixed at 10:33Z, before batch 3 reported; chained after it; script `batch4.sh`, code
`sg2lab_b3.py`).** The x-twist gave the best proxy (A_lo/A_64 about 0.5 at L = 4 and 8), so the coupling scan is repeated on it:
u_xy twisted along x, phi = pi/2, at beta 2.3 and 2.45 with L = 4, 6, 8, and at beta 2.6 with L = 6 and 12 (L = 4, 8 are in
batch 2). Primary A_lo: LB134 for the new runs; the one-regressor A_lo(Y_1) is also reported, because it is the quantity
batch 2 has at L = 4, 8. Criteria: those of 1.5 (REFUTES if A_lo rises at each step by more than 2 combined standard errors
and A_lo(8)/A_lo(4) >= 2.5; saturation if A_lo and A_64 change by at most 30 percent from L = 6 to 8). At beta 2.6 the
added sizes test persistence: growth persists if A_lo(12)/A_lo(6) >= 2.5 beyond 2 standard errors.

**3.3 Batch 3 (run 10:30-10:39Z under the lock, 71 percent free; then a hang, see 3.4).** Log `logs/batch3.log`, JSON
`logs/b3_*.json`. Code `sg2lab_b3.py`. A_lo = LB134 (primary, fixed in 3.1); A_lo(Y_1) given for comparison with 3.0.

| slice | beta | L | temporal-gauge X_1/X_2/X_3 | A_16 | A_64 | A_lo = LB134 | A_lo(Y_1) | PCA (halves) | A_lo/L^3 | A_64/L^3 |
|---|---|---|---|---|---|---|---|---|---|---|
| u_phi (z), pi/2 | 2.6 | 4 | 1.65/1.40/7.74 | 6.55 | 6.49 +- 0.75 | 3.54 +- 0.73 | 2.63 | 6.8, 6.0 | 0.055 | 0.101 |
| u_phi (z), pi/2 | 2.6 | 6 | 2.79/1.92/23.1 | 22.4 | 21.9 +- 1.2 | 13.6 +- 1.4 | 8.32 | 20.2, 22.7 | 0.063 | 0.101 |
| u_phi (z), pi/2 | 2.6 | 8 | 2.79/5.30/51.5 | 51.1 | 49.1; A_512 = 50.1 +- 6.1 | 32.8 +- 7.8 | 15.1 | 39.3, 55.8 | 0.064 | 0.096 |
| u_phi (z), pi/2 | 2.6 | 10 | 5.47/4.72/84.7 | 86.6 | 86.4 +- 7.7 | 55.1 +- 11.2 | 17.1 | 90.8, 75.7 | 0.055 | 0.086 |
| u_phi (z), pi/2 | 2.6 | 12 | 8.71/9.12/182.3 | 177.1 | 175.5 +- 5.4 | 115.7 +- 7.1 | 28.6 | 174.1, 160.7 | 0.067 | 0.102 |

Lags at L = 8: 52.8, 51.5, 51.1, 49.9, 49.1, 50.4, 49.7, 50.1 at n = 0, 8, 16, 32, 64, 128, 256, 512 (flat from lag 8 to 512).
**Verdict against 3.1: (SG2) REFUTED at beta 2.6 on the z-twisted u_xy (GUIDE).** A_lo(8) - A_lo(4) = 29.3 (3.8 combined standard
errors), ratio 9.3; A_lo(12) - A_lo(6) = 102.2 (14 standard errors), ratio 8.5; A_512/A_16 = 0.98 at L = 8. The lower bound grows
like the volume: A_lo/L^3 stays at 0.055-0.067 from L = 4 to 12, and the upper side at 0.086-0.102. So
Var_(pi_u)(<v, Ebar>) lies between about 0.06 L^3 and 0.10 L^3 at beta 2.6 on these boxes, and by 4.1(iv)
Var(phi_(u,z_v)) = beta^2 Var(<v, Ebar>) is between 0.4 L^3 and 0.7 L^3: at L = 12, between 780 and 1190.
The better proxy (averaged links) raised A_lo/A_64 from 0.32-0.46 (Y_1) to 0.55-0.66, which removed the doubt of 3.0.
The temporal-gauge lambda_* of the twisted slice (3.60, 9.28, 19.9, 31.6, 66.7) tracks row 950's u_xy values (4.19, 11.3, 22.6,
41.6, 64.9) within 25 percent, as 4.1(i) (local equivalence to u_xy) predicts.
**Family A screen (temporal gauge; criteria of 1.5 on the max over k of Lambda).** u_xyyz (flux -1 on xy and yz; pattern
(pi, pi, pi), (1, -1, 1)): beta 2.3, lambda_max = 1.32 (L = 4) and 1.43 (L = 8), at (pi, pi, pi): saturation, no order. beta 2.6:
3.53 and 13.3 (ratio 3.8, between L^2 and L^3; the order is spread over the three colours, 17.2/10.7/7.9, as at a central
slice): growth, so this anisotropic deformation of u_pi also orders at beta 2.6, and by 4.3 its twist would violate (SG2) too
(ARGUED; its twisted runs were not made). u_pi itself at beta 2.6, L = 4: lambda_max = 0.58 (frustrated, no order seen; L = 8
not run).

**3.4 What failed in batch 3, and a rule breach (reported plainly).** The next job, family D (interpolation u_xy -> u_pi at
s = 0.5 with the z-twist, L = 4), hung from 10:39Z until the task limit stopped it at about 11:55Z. Cause, found by hand:
at the cold start every y-link of the last slice t = T has an exactly vanishing staple. Its two xy staples give -2 u_y
(flux -1), its two yz staples cancel (the yz plaquettes of that slice are exp(+-(pi/2) k), so up + down = (-1)^x (k - k) = 0),
and the half weight of slice T gives S = (beta/2)(-2 u_y) + beta u_y = 0. The code then sets kappa = 1e-12, and the Kennedy-Pendleton
loop never accepts. (Other slices are not affected: for u_xy and its twists the yz staples add to +2 u_y.) Fix for a rerun:
sample Haar when kappa < 1e-3, or start hot. Not rerun.
**Breach.** My lock expired at 11:25Z while the hung process was still running. Row 954 took the lock at 11:25:57Z, so my
process ran without the lock for about 30 minutes, beside row 954's jobs (one thread; L = 4 arrays; its memory was not measured). The hung process used
about 76 CPU minutes (estimated from wall time: it spun in one loop on one core) and produced nothing. With it, this row used about 98 CPU minutes against the 60 asked: about 22 in
useful batches (smoke 1, batch 1 4, batch 2 8, batch 3 9) and 76 lost. So I stopped computing. Not run: batch 3's
remaining screens (u_pi at L = 8, family D, family C = vacuum slices) and batch 4 (the x-twist scan at beta 2.3 and 2.45, and
L = 6, 12 at beta 2.6). The lock is now held by row 954.

## 5. Result (step 8)

Reading order: Sections 0, 1, 2, then 3.0, 3.2, 3.3, 3.4 (results), 4.1-4.3 (meaning), 5; 2.3, 2.5, 3.1 and 4.4 are run plans
written before their runs. The sections sit in the order of work, so 3.3 and 3.4 follow Section 4. PCA values are given as
the two half-sample estimates; their spread is the error.
Plan against what was done: steps 1, 2 and 7 ran in full. Step 4 (tilted copies of u_xy) became the main result: twists
along z (phi = pi/2, pi/4) and along x. Step 3 (anisotropic deformations of u_pi) ran as a temporal-gauge screen of u_xyyz and
u_pi; their twisted versions did not run. Step 6 (interpolation) hung (3.4), and step 5 (vacuum slices) did not run.
Started 09:59Z; runs 10:13-10:39Z under the lock, plus the hung process to about 11:55Z (3.4); result written 11:58Z.

| Statement | Label |
|---|---|
| Lemma LB (1.3): any gauge-invariant proxy Y gives lambda_max(Cov Ebar) >= Var(<v, Ebar>) >= c^T G^(-1) c; lagged values of a palindromic frame chain decrease to their limit | PROVED (by hand, Claude Opus 5.5, not yet checked) |
| Proposition TW (1.4, 4.1): u_xy with a flat colour twist along x or z is locally gauge equivalent to u_xy; Ebar is parallel to e_3; the reflection S_d fixes the slice and gives E[X_3] = 0; the tie vector is horizontal, so Var(phi_(u,z_v)) = beta^2 Var(<v, Ebar>); the patterns n = +-e_3 are gauge-inequivalent (winding loop) | PROVED |
| Mechanism (4.2-4.3): a flat holonomy turns the colour order of a central slice's boundary layer into gauge-invariant data with an exact tie under a lattice reflection; (SG2) at beta needs that no Dirichlet boundary layer orders at beta | ARGUED |
| **(SG2), and (SG-step) in gauge-invariant form, for SU(2) Wilson at beta 2.6** | **REFUTED at GUIDE level** at u_xy twisted along z (phi = pi/2; L = 4 to 12; the lower bound A_lo grows like 0.06 L^3, 3.8 and 14 standard errors on the pre-set differences) and along x (L = 4, 8; 4.6 standard errors). Var(phi_(u,z_v)) is between 0.4 L^3 and 0.7 L^3. No proof either way; boxes up to 12 only |
| (SG2) at beta 2.45 (z-twist, phi = pi/2) | inconclusive by the pre-set criterion: the lagged (upper-side) values grow 4.3 -> 9.4 -> 21.9 (L = 4 to 8, lag-converged), the lower bound with the weak proxy Y_1 does not separate from noise |
| (SG2) at beta 2.3 (z-twist, phi = pi/2) | survives (bounded: lagged values 1.2-1.4, lower bound to 0); GUIDE only, establishes nothing |
| Family A screen: u_xyyz orders at beta 2.6 (lambda_max 3.5 -> 13.3 from L = 4 to 8), not at 2.3 (1.3, 1.4); u_pi at 2.6, L = 4: 0.58 | GUIDE |
| Controls C1-C3 pass; C4 passes on the lower bound, while the lagged values at the central slice fall only slowly at L = 8 (row 950's validation (V) issue) | GUIDE |
| Family C (vacuum slices), family D (interpolation), twisted u_xyyz and u_pi | NOT RUN (3.4) |
| (SG2) and (SG-step) at beta 2.3-2.4 | **OPEN** |

**Answers to the row.** (SG2) is the top eigenvalue of lim_n Cov(E^(0), E^(n)) over all slices. The search found a violation:
**at beta 2.6, (SG2) is refuted at GUIDE level, at a non-central slice with an exact tie between gauge-inequivalent next
slices.** The slice is the layered pi-flux slice u_xy with a flat colour holonomy along one axis (one of the "tilted
copies of u_xy" the row asked for, with the tilt on the links that do not carry the pattern). The frame-averaged
tie-mode variance grows like the volume on boxes 4 to 12, by a lower bound that needs no frame chain (Lemma LB) and by
lag-converged frame-lag values (flat from lag 8 to lag 512 at L = 8). Because the tie vector is horizontal at that slice,
(SG-step) in gauge-invariant form fails with it. The mechanism is not charge conjugation (inner for SU(2), row 950 7.2)
but a lattice reflection composed with a colour rotation (4.2). At beta 2.45 the upper side grows (inconclusive by the
criteria); at beta 2.3 nothing grows on the slices tried. Controls: compact U(1) at u_xy grows like L^3 after projection
(lag 64 = lag 0, ratio 3.38 from L = 4 to 6); the temporal-gauge C_0 reproduces row 950's volume growth at beta 2.6 (4.28 and
21.6 against 4.19 and 22.6).

**What a next lane should take (ranked).** (1) The chain's input (SG-step) is false in gauge-invariant form at beta 2.6 and,
by row 950's ordering coupling 2.45-2.5 for u_xy and 4.3, very likely for beta >= 2.5. The window for the hypercontractivity
route shrinks to beta 2.3-2.4 at best, and by 4.3 a proof there must show that no Dirichlet boundary layer orders, uniformly
in the slice (boundary uniqueness). (2) Cheap reruns that would sharpen this, about 10 CPU minutes: the x-twist scan at
beta 2.45 and 2.3 (`batch4.sh`, unchanged); twisted u_xyyz at beta 2.6; family D after the Haar fix of 3.4. (3) The question
on which the window turns: does any central slice order at beta 2.3-2.4? u_xy (row 950) and u_xyyz (here) do not, at the
sizes tried. Boxes of the seed size are out of reach of a run.

**Limits.** All runs are GUIDE: boxes 4 to 12 (z-twist) and 4, 8 (x-twist), slab thickness 6, cold starts, block errors from
8 contiguous blocks (Ising states may persist through a whole run; raw moments are used, which the symmetry S makes exact).
The small-box caveat of row 950 applies: at beta 2.6 the bulk deconfinement extent is about 10-12 lattice units (RECALLED),
so the order seen here might stop on much larger boxes. Row 950's growth at beta 2.5 to L = 20 argues against that (GUIDE).
The refutation stands or falls with the colour order of u_xy's boundary layer, by 4.1(i). The proofs (Lemma LB,
Proposition TW) are by hand by Claude Opus 5.5 and checked by no other model; row 953 is the check. Row 950 is used as READ
(unchecked; row 951 not on disk). The code was written for this row from row 950's text. Row 950's scripts in another
session's scratch folder were not read. Credit: the slab model, (SG2), the frame-lag test and the tie mode are row 950's
(Claude Fable 5.2), resting on row 944; the transfer frame and outline are Ethan Sussman and Levent Alpoge's (with Claude and
Codex as authors of their text). Kennedy-Pendleton heat bath (RECALLED). Nothing here is a public claim.

RESULT: Row 952 (Claude Opus 5.5 max, Mac mini; unchecked, check = row 953): (SG2), and with it (SG-step) in gauge-invariant form, is REFUTED at GUIDE level for SU(2) Wilson at beta 2.6. The slice is the layered pi-flux slice u_xy with a flat colour holonomy along z or x. The frame-averaged first-step tie-mode variance grows like the volume: lower bound (Lemma LB, no frame chain) 3.5 -> 115.7 for L = 4 -> 12, about 0.06 L^3; lag-converged upper side about 0.10 L^3; pre-set criteria met at 3.8, 14 and 4.6 standard errors. PROVED by hand: Lemma LB, and Proposition TW (local equivalence to u_xy, Ebar parallel to e_3, an exact tie between the gauge-inequivalent states n = +-e_3 under a lattice reflection composed with a colour rotation, and the tie vector is horizontal). ARGUED: (SG2) at beta needs that no Dirichlet boundary layer orders at beta. At beta 2.45 the upper side grows (inconclusive); at beta 2.3 nothing grows (GUIDE only). Controls pass (U(1) grows like L^3 after projection; C_0 reproduces row 950). Not run: vacuum slices, interpolation (a cold-start hang, diagnosed in 3.4, cost 76 CPU minutes and ran 30 minutes past my lock). OPEN: (SG2)/(SG-step) at beta 2.3-2.4; persistence beyond L = 12.
