lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-14T19:05Z

# gap-fctest-opus (FINISH row 946): GUIDE refutation test of (FC) for the vacuum slice chain

Status: in progress. Started 2026-11-14T07:05Z on Mac mini worker 2, at commit 77fc50935
(branch claude/ym4d-hard-route). Everything here is GUIDE unless marked otherwise: a run can
refute (FC) at a coupling, it cannot prove it. No statement of the chain rests on this file.

## Plan (at most eight steps; one per response)

1. Read row 941 (`library/gap-lsivac-max.md`) Steps 1, 5, 6: the exact definitions of the slice
   chain, P, nu, (A3), (FC), (GC), theta_GC, r_1; FINISH efficiency rules; grep open-core and
   FINISH rows for overlap. Record the definitions here verbatim with line references.
2. Write the estimator R(f) and the pass/fail criteria BEFORE any run (what counts as REFUTES,
   what counts as GUIDE-only, error and autocorrelation method).
3. Write code (lane946): SU(2) heat-bath + overrelaxation on a small periodic 4D lattice; frozen
   slice x; resampling of the rest; covariance estimator for grad P f via (A3).
4. Fact-check the code: (a) free photon / Gaussian chain, R = e^(-2 omega) per mode;
   (b) one-plaquette chain, theta_GC near r_1^2 as in row 941.
5. Run beta = 2.3 on the small lattice for the four observables (plaquette, smeared plaquette,
   odd function of (1/2) tr U_p, spatial Wilson line odd under the cut flip). About 45 min cap.
6. If time: beta = 2.6; exact one-cube chain (12 links, 6 plaquettes).
7. Report R(f) per f with error bars and integrated autocorrelation times; verdict per f.
8. RESULT line.

## Step log

(appended as each step completes)

### Step 1: objects, duplicate check, scope (READ; no new claim)

**Read at commit 77fc50935:** FINISH.md (opening, How we work, Joining, Working efficiently, Rules, rows 930,
936, 941, 943, 946-949), GOAL.md, `library/gap-lsivac-max.md` (row 941) Steps 0, 1, 5, 6 and Result,
`library/gap-oddgap-max.md` (row 930) notation and Lemma CUT (for the cut flip).

**Duplicate check (rule 0a).** `grep -i -E "\(FC\)|\(GC\)|fisher.information contract|slice chain"` on
`library/open-core.md`, `library/l17c.md`, `library/open-registry.md`: no hit. FINISH rows naming (FC)/(GC):
941 (states it), 946 (this row, a GUIDE test), 947 (the proof attack on (FC), queued after this row). I do not
attack (FC) as a proof. I run only the refutation test that row 946 assigns.

**Sussman-Alpoge account.** `library/sa-index/` has no heat-bath or Monte Carlo text (grep "heat.bath|monte
carlo|kennedy.pendleton|overrelax": no hit). Their account enters this row only through the transfer frame
(outline (GL8), as located by checks 927, 933, 938; credit: Ethan Sussman and Levent Alpoge, with Claude and
Codex as authors of their text). The chain P, (A1)-(A3), (FC), (GC), Theorem C0 are row 941's (Claude Fable 5.2).

**Objects (row 941, Step 1 (A1)-(A3), Step 5.1, Step 6; quoted in short).**
- Spatial box B, periodic; slice space M = (S^3)^L, L = 3|B| spatial links; a link is a unit quaternion;
  <a, b> is the R^4 inner product, so (1/2) tr(a b^(-1)) = <a, b>. V(x) = -beta sum over spatial plaquettes of
  (1/2) tr x_p.
- (A1) T_0(x, w) = e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2), temporal links set to 1. Omega its top eigenfunction
  (gauge invariant), lambda_0 its eigenvalue. Vacuum slice law nu = Omega^2 dx. One-step law
  pi_x(dw) = T_0(x, w) Omega(w) dw / (lambda_0 Omega(x)). P f(x) = E_(pi_x) f. P is self-adjoint on L^2(nu).
- (A3) For a tangent vector z at x: z . grad(P f)(x) = beta Cov_(pi_x)(<z, w>, f(w)). So
  grad_l (P f)(x) = beta Cov_(pi_x)(Proj_l w_l, f(w)), Proj_l v := v - <v, x_l> x_l (tangent space at x_l).
- grad is the Riemannian gradient of M with the metric induced from R^(4L); |grad f|^2 = sum over links.
- (GC)_theta: E_nu |grad P f|^2 <= theta E_nu |grad f|^2 for all smooth gauge-invariant f, theta < 1.
  (FC)_theta: E_nu[|grad P g|^2/P g] <= theta E_nu[|grad g|^2/g] for smooth positive g. (FC)_theta implies
  (GC)_theta (put g = 1 + eps f, second order in eps). So R(f) := E_nu|grad P f|^2 / E_nu|grad f|^2 >= 1 for
  one f refutes (GC) and hence (FC) on that box at that coupling.
- Row 941 GUIDE numbers to reproduce: one-plaquette SU(2) chain, theta_GC = 8.23e-4 (beta 2.3) and 1.15e-3
  (beta 2.6), r_1^2 = 8.02e-4 and 1.12e-3. One Gaussian mode: R = e^(-2 omega).
- Row 930 cut flip J: the centre flip (w -> -w) of the direction-1 links of one cut x_1 = const of a slice.
  J commutes with T_0 (each spatial plaquette meets a cut in 0 or 2 links). A Wilson loop is odd under J iff
  it crosses the cut an odd number of times, e.g. the spatial Wilson line winding once in direction 1.

**Scope of a verdict (fixed before any run).** The target box of rows 941 and 947 is the seed box (24a)^3 with
a about 20 or more at beta 2.3, side about 500 lattice units. This row runs boxes of side 4 and 6. So:
- a run with R(f) >= 1 beyond errors refutes (GC), hence (FC), **on the run's box at that coupling**;
- it is evidence (GUIDE) against (FC) on the seed box only if f is local (support small against the box) and
  R(f) does not fall when the box grows from 4 to 6;
- an f that winds around the box (centre-odd under J) probes SMALL-BOX physics (torelon / flux states, whose
  energy grows with the box in the confined phase). A winding-line R near or above 1 on side 4 says nothing
  about the seed box. It is reported as a SMALL-BOX probe, apart from the verdict.

### Step 2: estimator and pass/fail criteria (written 2026-11-14 before any run)

**2.1 Lattice and exact identities used by the estimator (PROVED, by hand, short).** Spatial graph G (periodic
L^3 box; or one plaquette, 4 links; or one cube, 12 links, open) times open time {0, ..., 2K}. Wilson action,
weight beta on every plaquette (spatial and timelike), temporal links dynamical, no gauge fixing. Middle slice
t_0 = K; its spatial links are x.
- (E1) Weight = e^(-V(x_0)/2) T(x_0, x_1) ... T(x_(2K-1), x_(2K)) e^(-V(x_(2K))/2), T = T_0 Pi_G. So the middle
  slice has law nu_K prop. to (T^K b)(x)^2 dx, b = e^(-V/2), and nu_K -> nu as K -> infinity. Only states with
  <psi_n, b> != 0 enter the error: zero momentum, centre-even, cubic-invariant. Error O(e^(-E' K)), E' the lowest
  such energy. (Periodic time would let every state in, including the low centre-odd flux states of a small box.)
- (E2) Given x, the forward half (t > K) and the backward half (t < K) are independent (the action is a sum of
  terms inside one half plus x).
- (E3) Transported slices. For a spatial link l = (a -> b): w_l := U_0(a, K) U_l(K+1) U_0(b, K)^(-1) (forward) and
  w'_l := U_0(a, K-1)^(-1) U_l(K-1) U_0(b, K-1) (backward). Then <x_l, w_l> is the timelike plaquette term at l.
  Change variables w'' -> w (Haar invariance; the rest of the half is a gauge-invariant function of the time-K+1
  slice): w is independent of the temporal links U_0(., K) and has law
  pi_x^(K)(dw) prop. to T_0(x, w) (T^(K-1) b)(w) dw. Same for w'. pi_x^(K) -> pi_x as K -> infinity.
- (E4) pi_x^(K)(dw) = e^(beta <x, w>) m_K(dw)/const with m_K free of x, so (A3) holds for P_K f(x) := E_(pi_x^(K)) f
  exactly: grad_l P_K f(x) = beta Cov_(pi_x^(K))(Proj_l w_l, f(w)). For gauge-invariant f, f(w) = f(slice K+1).
So the run estimates R_K(f) := E_(nu_K)|grad P_K f|^2 / E_(nu_K)|grad f|^2 without bias except the O(tau/n) term
below, and R_K -> R as K grows. K is varied to see the limit.

**2.2 Estimator.** Outer: B independent heat-bath chains (1 heat-bath pass, Kennedy-Pendleton, plus 2
overrelaxation passes per sweep), thermalised; every n_sep sweeps the middle slice x is taken. Inner, per x:
freeze x, run n sweeps of all other links from the outer configuration (already a sample of the conditional law,
so no burn-in is needed); record a_l = Proj_l w_l, a'_l = Proj_l w'_l and the base observables F_j(w), F_j(w').
Per x: C^F_(l,j) = sample covariance of (a_l, F_j(w)) over the n sweeps, C^B from the backward half, and
  S_j(x) := beta^2 sum_l C^F_(l,j) . C^B_(l,j)        (dot product in R^4, sum over all spatial links).
By (E2), E[S_j(x) | x] = beta^2 sum_l E[C^F] . E[C^B] = (1 - O(tau/n))^2 |grad P_K F_j(x)|^2: no positive noise bias
(the naive |C^F|^2 would carry a bias of order L Var(a) Var(F) tau/n). The O(tau/n) bias is downward.
Linear combinations f = sum g_j F_j use C g (linearity of the covariance).
Denominator: |grad f|^2 on the middle slice x of the outer configurations (law nu_K exactly), by closed forms:
|grad Re(W)|^2 = n_W (1 - Re(W)^2) for a Wilson loop W with n_W distinct links; for sums, the Gram matrix of the
per-link tangent gradients. Translation and cubic averages of numerator and denominator are taken over the box.
R_hat = (mean numerator)/(mean denominator); error by jackknife over the B independent outer chains.
Integrated autocorrelation times are reported for the inner series of each base observable and for S along the
outer chains.

**2.3 Calibrations (must PASS before any SU(2) box number is read).**
- C1 free photon (non-compact U(1), action (beta/2) sum_p (dA)_p^2, same geometry 4^3 x (2K+1), same code path
  with a_l = w_l, flat). Exact: for f = sum_s cos(k s_1) (dA)_(12)(s) (one transverse mode, A_2 at momentum k e_1),
  R = e^(-2 omega), cosh omega = 1 + 2 sin^2(k/2); for f = (dA)_p one plaquette, R = |e^(-h) c|^2/|c|^2 with c the
  plaquette's incidence vector and cosh h = 1 + (d^T d)/2 on the co-exact space (exact linear algebra).
- C2 one-plaquette SU(2) chain, beta 2.3 (and 2.6): exact R(f) by the reduced chain on class functions
  (C chi_n = ((2/beta) I_n(beta))^4 chi_n, V = -beta cos theta, |grad F|^2 = 4 F'(theta)^2), for f = cos theta and
  f = tanh(3 cos theta). The reduced code must also return row 941's r_1^2 = 8.02e-4 and theta_GC = 8.23e-4 at
  beta 2.3 within 1 percent.
- PASS for each calibrated f: |R_hat/R_exact - 1| <= max(3 sigma/R_exact, 0.05).

**2.4 Observables on the SU(2) box (base F_j on slice K+1 or K-1).** O1 plaquette c_p = (1/2) tr w_p. O2 smeared
plaquette: (a) the mean of the 4 coplanar plaquettes of a 2 x 2 square, (b) the zero-momentum sum over all
plaquettes. O3 odd functions of c_p: tanh(3 c_p), tanh(10 c_p), c_p^3. O4 winding Wilson line in direction mu
(odd under the cut flip J of row 930): (a) one line, (b) the mean of the 4 lines over a 2 x 2 transverse patch,
(c) the mean over the whole cross-section. I read "a spatial Wilson line around a small transverse
cross-section" as O4a/O4b; O4 is the SMALL-BOX probe of Step 1, not the seed-box verdict.

**2.5 Verdict rules.**
- REFUTES (FC) on box B at beta: some f with R_hat - 3 sigma >= 1, both calibrations passed, and R_hat stable
  within errors when K -> K + 2 and n -> 2n.
- GUIDE evidence against (FC) on the seed box: the above for a local f (O1-O3, O2a), with R_hat on 6^3 not below
  the 4^3 value beyond errors.
- NOT REFUTED (GUIDE only; proves nothing): every R_hat + 3 sigma < 1; "well below 1" means R_hat + 3 sigma < 0.5.
- INCONCLUSIVE otherwise.
Machine rules: one job at a time under `python3 scripts/lab_ops.py numeric-lock`, OMP/BLAS threads 1, nice,
self-stop above 2 GB RSS, start only at >= 50 percent memory free. Compute cap about 45 minutes in total.

### Step 3: code (written 2026-11-14, before any run)

`library/guide/lane946/fct.py` (one file, numpy/scipy, one thread). Pieces: quaternion SU(2); spatial graphs
(periodic L^3 box, one plaquette, one cube) times open time {0..2K}; colouring of links into independent sets;
Kennedy-Pendleton heat bath (rejection from Haar for alpha < 1) plus 2 overrelaxation passes per sweep;
non-compact U(1) Gaussian heat bath on the same tables (calibration C1); transported slices (E3); tangent
gradients of Wilson loops by prefix/suffix products; the accumulator for the two half-chain covariances; the
estimator S = beta^2 sum_l C^F . C^B; jackknife over independent outer chains; Sokal-window tau_int; exact
references `photon_exact` (spectral formula of Step 2.3) and `plaq_exact` (character basis, 40 characters,
800 Gauss points). Self-tests in the file (`fct.py selftest`): quaternion algebra; staple sums against the
total action change; colour classes are independent sets; U(1) conditional mean; loop gradients against
finite differences and |grad_l Re W|^2 = 1 - Re W^2; the Gram sums of den() against explicit gradient sums;
the sampler's E X_0 = I_2(alpha)/I_1(alpha).
Added self-test: the transported slices satisfy <x_l, w_l> = Re(timelike plaquette at K) and <x_l, w'_l> =
Re(timelike plaquette at K-1), and w, w', x are unchanged by a random gauge map that is 1 on slice K.

**Numeric lock.** At 07:25Z the machine lock was held by row 944's GUIDE job (`gap-sgstep-944`, started
07:17Z, lease to 09:17Z). No run of this row starts before it is released; a background poll acquires it.

**Hand value for C1 (by hand, independent of `photon_exact`).** Plaquette flux f = (dA)_p, p in the (0,1)
plane. Its incidence vector has |c^(k)|^2 = khat_0^2 + khat_1^2, khat_i^2 = 4 sin^2(k_i/2), and it is co-exact, so
R = sum_k (khat_0^2 + khat_1^2) e^(-2 omega(khat^2)) / sum_k (khat_0^2 + khat_1^2), cosh omega(u) = 1 + u/2.
On L = 4, khat_i^2 takes 0, 2, 2, 4. e^(-2 omega(u)) for u = 0, 2, ..., 12: 1, 0.0717968, 0.0294373, 0.016133,
0.010205, 0.0070426, 0.0051548. With F(s) = E(s) + 2E(s+2) + E(s+4): F(2) = 0.1468044, F(4) = 0.0719083,
F(6) = 0.0435856, F(8) = 0.029445. Numerator = 8 F(2) + 24 F(4) + 24 F(6) + 8 F(8) = 4.181848; denominator
= 2 x 8 x 16 = 256 (Parseval: 256/64 = |c|^2 = 4). **R_exact(flux, L = 4) = 0.016335.**
Single modes: k = pi/2: (2 - sqrt 3)^2 = 0.071797; k = pi: (3 - 2 sqrt 2)^2 = 0.029437.

### Step 4: self-tests and calibrations (GUIDE runs, 2026-11-14, lock acquired 08:11Z)

Numeric lock acquired 08:11:28Z as `lane946-fctest-opus` (row 944 released it). Memory 71 percent free.
Logs: `library/guide/lane946/logs/`; outputs `out/*.json`, `out/*.npz`. All runs nice, one thread.

**Self-tests (`logs/selftest.log`): all PASS.** Staple sums equal the total action change on box, one plaquette
and one cube; colour classes are independent sets; U(1) conditional mean; transported slices give the
timelike plaquettes and are invariant under gauge maps off slice K; loop gradients agree with finite
differences to 1e-5; Gram sums of den() equal explicit gradient sums; sampler E X_0 = I_2/I_1 at alpha = 0.3, 2, 7.

**Exact one-plaquette chain (`plaq_exact`, deterministic quadrature; reproduces row 941):**

| beta | r_1 | r_1^2 | theta_GC | R(cos th) | R(tanh 3 cos th) | R(tanh 10 cos th) | R(cos^3 th) |
|---|---|---|---|---|---|---|---|
| 2.3 | 0.028317 | 8.018e-4 | 8.229e-4 | 7.877e-4 | 5.450e-4 | 1.754e-4 | 3.425e-4 |
| 2.6 | 0.033408 | 1.116e-3 | 1.1457e-3 | 1.088e-3 | 7.470e-4 | 2.303e-4 | 4.888e-4 |

Row 941: r_1 = 0.02832, 0.03341; theta_GC = 8.23e-4, 1.15e-3. Agreement better than 0.5 percent: PASS.
Each R(f) is below theta_GC, as it must be.

**C1, free photon, 4^3 x 13 (K = 6), B = 16 chains, m = 6 rounds, n = 300 inner sweeps (`c1_photon_L4`):**

| f | R_hat | jackknife err | exact | R_hat/exact - 1 | verdict |
|---|---|---|---|---|---|
| one plaquette flux | 0.016253 | 4.9e-5 | 0.016335 (hand value of Step 3 and `photon_exact`) | -0.5% | PASS |
| mode k = pi/2 | 0.070673 | 1.5e-3 | 0.071797 | -1.6% | PASS |
| mode k = pi | 0.029112 | 5.8e-4 | 0.029437 | -1.1% | PASS |

tau_int (inner) 0.44-0.48. The small downward offset matches the stated O(tau/n) bias, (1 - 2 tau/n)^2 = 0.993.

**C2, one-plaquette SU(2) chain, beta 2.3, K = 4, B = 64, m = 4, n = 2000 (`c2_plaq_b2.3`):**

| f | R_hat | err | exact | verdict |
|---|---|---|---|---|
| cos theta (plaquette) | 8.032e-4 | 1.7e-5 | 7.877e-4 | +2.0%, within 3 sigma: PASS |
| tanh(3 cos theta) | 5.34e-4 | 5.2e-5 | 5.450e-4 | -1.9%: PASS |
| tanh(10 cos theta) | 2.6e-4 | 7.3e-5 | 1.754e-4 | within 3 sigma (noisy): PASS |
| cos^3 theta | 3.95e-4 | 3.2e-5 | 3.425e-4 | within 3 sigma: PASS |

So the code path (heat bath, frozen slice, transport, tangent projection, two-half product, gradient forms,
ratio, errors) returns the exact R to a few percent on an SU(2) chain with R of order 1e-3 and on a Gaussian
chain with R of order 1e-2 to 1e-1. Both calibrations PASS; box numbers may be read.

Timing probe (4^3 x 13, B = 16, n = 20): about 95 ms per inner sweep; peak RSS 566 MB.

### Step 5: SU(2) box at beta 2.3 (GUIDE)

**b1: 4^3 x 13 (K = 6), beta 2.3, B = 16 independent chains, m = 8 rounds, n = 300 inner sweeps, 128 frozen
slices x, every plaquette and line position averaged (`out/b1_L4K6_b2.3.json`, 3.5 min).** Inner tau_int
0.48-0.56 sweeps for every series (so n = 300 is about 300 independent samples per half); outer lag-1
autocorrelation of the per-round numerators between -0.24 and -0.01 (no outer correlation).

| f | R_hat | err | R_hat + 3 err | den E_nu abs(grad f)^2 |
|---|---|---|---|---|
| O1 plaquette c_p | 8.60e-4 | 1.7e-5 | 9.1e-4 | 2.18 |
| O2a 2 x 2 smeared plaquette | 1.129e-3 | 3.3e-5 | 1.23e-3 | 0.558 |
| O2b zero-momentum plaquette sum (one plane) | 3.57e-3 | 2.2e-4 | 4.2e-3 | 146 |
| O3 tanh(3 c_p) | 5.81e-4 | 1.7e-5 | 6.3e-4 | 3.58 |
| O3 tanh(10 c_p) | 1.63e-4 | 8.8e-6 | 1.9e-4 | 10.9 |
| O3 c_p^3 | 4.13e-4 | 1.2e-5 | 4.5e-4 | 3.00 |
| O4a winding line (length 4) | 0.01623 | 1.8e-4 | 0.0168 | 2.99 |
| O4b mean of 2 x 2 transverse patch of lines | 0.04455 | 6.4e-4 | 0.0465 | 0.748 |
| O4c mean over the whole cross-section | 0.1385 | 2.3e-3 | 0.145 | 0.187 |

Reading (GUIDE). Every R_hat + 3 err is below 0.15, so by rule 2.5 this box is NOT REFUTED at beta 2.3 and
the values are "well below 1". The local plaquette value (8.6e-4) is within 10 percent of the exact
one-plaquette chain value R(cos theta) = 7.9e-4: one-step contraction of a plaquette's Dirichlet energy is
fixed at the scale of one plaquette. R grows with the spatial extent of f (plaquette 8.6e-4, 2 x 2 square
1.1e-3, plane sum 3.6e-3; line 0.016, patch 0.045, cross-section 0.14): smooth, extended f contract least,
as in the Gaussian case where R = e^(-2 omega) per mode. The odd functions of c_p contract more than c_p.

### Step 6: beta 2.6, the one-cube chain, and the systematic checks (GUIDE)

**b5: 4^3 x 13, beta 2.6, same parameters as b1 (`out/b5_L4K6_b2.6.json`, 3.6 min).** Inner tau_int 0.50-0.59.

| f | R_hat (beta 2.6) | err | R_hat (beta 2.3, b1) |
|---|---|---|---|
| O1 plaquette | 6.65e-4 | 1.7e-5 | 8.60e-4 |
| O2a 2 x 2 smeared | 8.04e-4 | 2.3e-5 | 1.129e-3 |
| O2b zero-momentum plane sum | 1.35e-3 | 1.6e-4 | 3.57e-3 |
| O3 tanh(3 c_p) | 4.11e-4 | 1.6e-5 | 5.81e-4 |
| O3 tanh(10 c_p) | 9.75e-5 | 9.4e-6 | 1.63e-4 |
| O3 c_p^3 | 3.70e-4 | 1.8e-5 | 4.13e-4 |
| O4a winding line | 0.02159 | 3.3e-4 | 0.01623 |
| O4b 2 x 2 patch of lines | 0.0620 | 1.2e-3 | 0.0446 |
| O4c whole cross-section of lines | 0.2028 | 4.2e-3 | 0.1385 |

Reading (GUIDE). NOT REFUTED at beta 2.6 on 4^3; all R_hat + 3 err below 0.22. The local observables contract
more at 2.6 than at 2.3; only the winding-line family (centre-odd, the SMALL-BOX probe) moves toward 1, as
the side-4 box shrinks in physical units. At this size and coupling it is still far from 1.

**b6: the one-cube chain (12 links, 6 plaquettes, open cube slice), beta 2.3, K = 6, B = 64, m = 4, n = 1000
(`out/b6_cube_b2.3.json`, 1.3 min).** Row 941 named this chain, the smallest unit with a Z_2 monopole, and did not
set it up. Observables as O1, O3 on each face (all 6 averaged) and the smooth Z_2 monopole indicator
mono_kappa = product over the 6 faces of tanh(kappa c_p) (sign -1 iff an odd number of faces has c_p < 0).

| f | R_hat | err |
|---|---|---|
| face plaquette c_p | 8.53e-4 | 1.3e-5 |
| tanh(3 c_p) | 5.76e-4 | 2.6e-5 |
| tanh(10 c_p) | 1.75e-4 | 1.9e-5 |
| c_p^3 | 3.68e-4 | 1.2e-5 |
| monopole indicator, kappa = 3 | 2.52e-4 | 1.9e-5 |
| monopole indicator, kappa = 10 | 5.9e-5 | 7.4e-6 |

Reading (GUIDE). NOT REFUTED; the monopole indicator contracts more strongly than any plaquette function. The
plaquette values on the cube, the 4^3 box and the single plaquette agree within 10 percent (8.5e-4, 8.6e-4,
7.9e-4): no sign of a collective slow mode in the local sector at beta 2.3.
