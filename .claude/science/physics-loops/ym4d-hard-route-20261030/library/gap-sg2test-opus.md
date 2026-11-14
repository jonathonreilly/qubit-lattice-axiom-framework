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

