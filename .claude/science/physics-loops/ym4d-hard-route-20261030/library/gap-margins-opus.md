# FINISH row 918: GUIDE margins campaign for the three live gap families

Author: Claude Opus 5.5 (high effort). Status: GUIDE only. Every number below
is a GUIDE measurement. It may refute or orient. It proves nothing.

Clone: /Users/jonreilly/ym4d-lead/clone at commit
8f6e7a3b7f80a47c49c0987fb329d838aff81ffc (pulled 2026-11-13, already up to date).
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
Scripts: lane918/scripts. Logs: lane918/out.

## Plan

1. Read the status note (row 912) and the definition sources: finishline-opus
   lines 110-160, row 892, crux-core-max Lemma SPLIT, target-max (rows 708, 913),
   rows 898/907/910 (free-wall engine), rows 872/881/888 (EXC). Record each
   definition and the value the proof needs.
2. Read the reusable heat-bath code (typinf.py, blockinf.py, lane860/899).
   Build and validate one SU(2) heat-bath + overrelaxation sampler (check the
   plaquette against known values at beta 2.3 and 2.5).
3. Family 1 (seed): twist ratio Z^v/Z^0 by interpolation in the twisted-plaquette
   coupling; S and S_ev. Criterion written before the run.
4. Family 2 (transport): thermal excess proxy and rate K. Criterion first.
5. Family 3 (free-wall engine): join excess and doubling ratio. Criterion first.
6. Family 4 (EXC): odd-sector excess of spin >= 5/2 temporal plaquettes.
   Criterion first.
7. Final table and RESULT line.

## Log

### Step 1. Definitions read, and the value each family needs (READ; D = lane directory)

Sources read in this step: D/library/gap-status-1113.md (row 912, all 449 lines); D/library/gap-finishline-opus.md
L100-165; D/library/gap-crux-core-max.md (Lemma SPLIT L263-280, (CORE) L298-304, Prop. W L400); D/library/gap-target-max.md
L200-232 and grep hits; D/library/gap-mid-max.md L52-172 (grep hits); D/library/gap-cutth-max.md L11-178 (grep hits);
D/library/gap-filter-ls-opus.md L95-175; FINISH.md rows 708, 872, 881, 888, 898, 907, 910, 913 (first 1500 chars each).

Notation. Wilson action beta * sum_p x_p, x_p = tr(U_p)/2, Haar-normalized so Z = 1 at beta = 0. A torus t x B is
periodic time t and spatial box B. F(t; B) = log Z(t; B). T_B the transfer operator, lambda_0 its top eigenvalue.

Family 1 (seed). S(t; B) = Tr T_B^t / lambda_0^t - 1. G(t; B) := log(1 + S(t; B)) = F(t; B) - t log lambda_0(B).
 Measurable form used here: G(t) - (t/T) G(T) = F(t) - (t/T) F(T) = 6 t |B| int_0^beta [P_t(b') - P_T(b')] db',
 P = mean x_p, T a long torus. Since G(T) >= 0 this is a LOWER bound on G(t); it equals G(t) up to (t/T) G(T).
 Centre flips C_i (i spatial) give the twisted traces Z^(e) = Tr(T^t C^e), e in {0,1}^3 (twists in the (time, i) planes).
 rho_e := Z^(e)/Z^(0). Then 1 + S_ev = (1 + S) (1/8) sum_e rho_e (exact; P_0 = prod (1 + C_i)/2), and
 Q_0 = (1 - rho_(100))/2 (cubic box). Lemma SPLIT (checked 893): (1 + S_ev)/(1 - Q_0) <= 1 + S <= (1 + S_ev)/(1 - 3 Q_0).
 Needed values: (SEED-FP) S(N; (2N)^3) < 1/5041 = 1.98e-4 (cube, time = half side). Theorem SH (r = b/a >= 24):
 S(a; b^3) <= 3/10; split form S_ev <= 1/10 and (CORE) Q_0 <= 1/20, i.e. rho >= 9/10, with b >= 24 a.
 Proposition W needs S_ev <= 160^(-16) = 5.4e-36 with a >= 82 (not a GUIDE-reachable size; recorded only).

Family 2 (transport, rows 708, 913). (VIR_K): d_beta G(t; B) <= K t <E>_t, with <E>_t = -d_t G the thermal mean
 excitation energy, and d_beta G(t) = 6 t |B| (P_t - P_inf) (Lemma 4.2 of row 708). Level form (LEV_K):
 -dE_i/dbeta <= K E_i. In the dilute one-level limit K_eff = d_beta G / (t <E> G) = -d log E / d beta.
 Needed: int of K over [beta_0, beta_1] <= log(b / (2 ceil(log2 b))), b >= 256, beta_0 <= 1/25600. Row 708's GUIDE
 from published a sqrt(sigma): K about 3.3 in [2.3, 2.6]; "K need not be bounded in b; K of order log b serves".
 Magnetic/electric split: the action deficit of a level is (vacuum action - level action) per slab; split into
 spatial (magnetic) and temporal (electric) plaquettes. Row 708 Way 1 (GUIDE from published rates): the magnetic part
 of an excited level lies BELOW the vacuum's by about 3 times its energy, so the pointwise inequality (K = 1/beta)
 fails by a factor about 8.

Family 3 (free-wall engine, rows 898, 907, 910). Free box B = (b, c, d): periodic time a, free spatial walls.
 W(a; B) = Z, g(a; B) = log(Tr M_B^a / lambda_0(B)^a). B|B: two boxes joined along one face (side b -> 2b).
 F_join(a; B) = log W(a; B|B) - 2 log W(a; B); J_0(B) = lim_T F_join(T; B)/T. Join excess E(a; B) = F_join - a J_0
 = g(a; B|B) - 2 g(a; B) (Lemma J, checked 911). (J-INT): E = beta int_0^1 [<X_cut>_(a; s) - (a/T) <X_cut>_(T; s)] ds,
 X_cut the sum of x_p over the cut plaquettes (those containing a crossing link), cut coupling s beta.
 Needed: (H-DBL) g(after) <= k g(before) on each of three steps (b,b,b)->(2b,b,b)->(2b,2b,b)->(2b,2b,2b), with a seed
 s_0 = S(a_0; b_0^3) < 1/(4 k^6) (Theorem C; Theorem C' needs doubling only on boxes with S <= 1/(3 k^4)).
 Doubling ratio = g(B|B)/g(B) = 2 + E/g(B) = k. So k = 2 + kappa with (JOIN-TH_kappa) E <= kappa g.
 Row 910 4.5: at small beta k = 2 + 1/(b-1) at leading order (E > 0).

Family 4 (EXC, rows 872, 881, 888). Torus (a, a, c, d), time a, twist plane (time, i). Odd sector P_- = (1 - C_i)/2,
 p = Q_0. N_hi = number of temporal plaquettes of one time step whose character-expansion spin is a half-integer
 >= 5/2. Delta(s) = <N_hi>_- - <N_hi>_all = Cov(N_hi, 1_odd)/p (Lemma 3.1 of row 872). Monte Carlo form used here
 (my derivation from P_- = (1 - C)/2, C commuting with the transfer): Delta(1) = rho (<N>_0 - <N>_v)/(1 - rho),
 <.>_v the twisted ensemble, N measured on time steps that do not contain the twist stack. Spin-j weight of a
 plaquette: the one-link-integrated estimator of row 860's guide860.py.
 Needed: EXC: int_1^(s_*) Delta(s) ds/s >= c_0 > 0 uniformly; area form EXC-W Delta(s) >= delta L_i on [1, s_*];
 (DRESS): Delta(1) > 0 of order L_i. Check 881's scale: gamma about 0.010 per unit L_i at beta 2.3. Only s = 1 is
 reachable by Monte Carlo (for s > 2 the boosted Lagrangian weight is negative at U = -1: e^(-2.3) = 0.10 against
 z d^2 r_(5/2) = 0.098 per unit of s - 1; my arithmetic, GUIDE).

### Step 2. Sampler built and validated (GUIDE)

Scripts: lane918/scripts/su2lat.py (sampler), validate.py; logs lane918/out/validate_{A,B,C}.log.
su2lat.py: per-plaquette coefficient field c_p (twist c = -1, interpolation c = s, free wall c = 0 on every
plaquette holding a wrap-crossing link); heat bath (h1 sampler as in typinf.py) plus 3 overrelaxation steps per
sweep; colour classes that are proper on odd periodic extents (3-colouring of the cycle), which is the defect check
869 found in lane867's N_t = 3 sampler. Heat-bath code was written fresh, with typinf.py and guide860.py as models.

Criterion (written before the runs): pass if (A) the coloured sampler and a plain sequential random-order heat bath
(no colouring at all) agree within 2 sigma on a 3^4 torus (every extent odd, 27 classes); (B) strong coupling and
free-wall decoupling come out right; (C) 8^4 plaquettes and spin weights agree with row 860's guide860.out.

Results (GUIDE):
- (A) 3^4, beta 2.3: coloured <x_p> = 0.61705(70), |P|/2 = 0.46370(67); sequential 0.61860(121), 0.46326(128).
  Differences 1.1 sigma and 0.3 sigma. PASS. (This run took 317 s, a little over the 5-minute guide.)
- (B) beta 0.5 on 3x4^3: <x_p> = 0.12371(23) against u + 4u^5 = 0.12383. Crossing links of a free wall: <a_0> =
  -0.0005, <a_0^2> = 0.2532 (Haar: 0, 0.25). PASS.
- (C) 8^4: beta 2.3 <x_p> = 0.60221(43) (row 860: 0.60244(51)); beta 2.5 0.65227(26) (row 860: 0.65268(22)).
  Spin weights at 2.3: rho_(1/2) = 0.3258(8), rho_(3/2) = 1.25(5)e-3, rho_2 = 2.0(5)e-5, rho_(5/2) = -0.7(6.2)e-7;
  at 2.5: rho_(5/2) = 1.8(1.2)e-6 (row 860: 4.0(27)e-8 and 1.28(38)e-6). PASS.
- Speed: about 10 microseconds per site per sweep (8^4: 0.04 s); peak memory about 64 MB.
Consequence for family 4 (my arithmetic from (C)): one plaquette's spin-5/2 estimator has a standard deviation of
about 6e-4 per configuration, about 400 times the mean density at beta 2.5.

### Step 3. Family 1a: the twist ratio rho = Z^(v_01)/Z^0 (GUIDE)

Method: twist.py, interpolation of the coefficient s of the b^2 stack plaquettes from 1 to -1, Bennett acceptance
ratio between neighbouring s (trapezoid and Simpson as cross-checks). Torus a x b^3 (time a).
Criterion (written before the runs): (CORE) needs rho >= 9/10, log rho >= -0.105, at b >= 24 a. A shape counts as
ROOM if log rho >= -0.105 at 2 sigma, NO ROOM if log rho < -0.105 at 2 sigma. Since b >= 24 a is out of reach, the
verdict for the family rests on the trend: rho must rise toward 1 with b at fixed a above the deconfinement length.
If rho falls with b at fixed a, that a is in the ordered (deconfined) regime and (CORE) fails there.

Runs (logs lane918/out/tw_<a>_<b>_<beta>.log; 17 s-values, 250-800 sweeps each; BAR value with block error; the
Simpson value with the conditional-mean stack estimator agrees within errors in every run). All GUIDE.

| beta | a | b | log rho (BAR) | Simpson, improved | rho | Q_0 = (1 - rho)/2 |
|---|---|---|---|---|---|---|
| 2.3 | 2 | 4 | -7.28 (7) | -7.39 (9) | 6.9e-4 | 0.50 |
| 2.3 | 4 | 4 | -0.82 (7) | -0.89 (8) | 0.44 | 0.28 |
| 2.3 | 4 | 6 | -0.62 (10); repeat -0.66 (16) | -0.71 (14) | 0.54 | 0.23 |
| 2.3 | 4 | 8 | -0.27 (18) | -0.53 (23) | 0.77 (+0.15 -0.12) | 0.12 (6) |
| 2.3 | 6 | 4 | -0.41 (7) | -0.40 (9) | 0.66 | 0.17 (2) |
| 2.3 | 6 | 6 | +0.03 (10) | +0.09 (14) | 1.0 (1); bound rho <= 1 | <= 0.05 at 1 sigma |
| 2.3 | 6 | 8 | +0.28 (20) | +0.21 (26) | 1 (consistent; 1.4 sigma above the bound 0) | <= 0.04 at 1 sigma |
| 2.5 | 6 | 4 | -1.02 (7) | -1.01 (11) | 0.36 | 0.32 |
| 2.5 | 6 | 6 | -1.22 (15) | -1.18 (15) | 0.30 | 0.35 |
| 2.5 | 6 | 8 | -1.23 (28) | -1.30 (36) | 0.29 | 0.35 |

Reading (GUIDE).
- beta 2.3, a = 2 (below the deconfinement length, about 4 here): rho = 7e-4. The twist costs an ordered interface.
  (CORE) fails there by a factor 1300.
- beta 2.3, a = 4 (at the deconfinement length): rho rises with b, 0.44, 0.54, 0.77 for b = 4, 6, 8.
- beta 2.3, a = 6 (above it): rho = 0.66 at b = 4 and is 1 within 0.1 in log at b = 6 and 8. Check against a
  dilute flux gas: Q_0 about exp(-a E_f(b)) with E_f(b) = sigma b - pi/(3b), a^2 sigma = 0.136 (RECALLED value,
  not from this run), gives Q_0 = 0.19 at b = 4 and 0.022 at b = 6, against 0.17 (2) and <= 0.05 measured.
  So at a = 6 the (CORE) margin rho >= 0.9 is met already at b = 6, at 1 sigma, far below b = 24 a.
- beta 2.5, a = 6 (below the deconfinement length there, about 8): rho stays near 0.3 and does not rise with b.
  (CORE) fails at this a; the seed box at beta 2.5 must have a above about 8.
- The criterion: ROOM at (a, b) = (6, 6), (6, 8), beta 2.3 (1 sigma only; 2 sigma reaches log rho = -0.17 at
  b = 6, below the line -0.105, so at 2 sigma it is TIGHT); NO ROOM at every shape with a below the deconfinement
  length. The 8 x 8^3 run at beta 2.5 is in the queue (Step 3b).

### Step 4. Families 1b, 2 and 3: criteria written before the thermodynamic-integration and spectroscopy runs

Runs queued (one at a time, lane918/out/q_main.txt): spectroscopy spec.py on 16 x 8^3 at beta 2.3 and 2.5 (0++
glueball from smeared spatial plaquettes, torelon from smeared spatial Polyakov loops); ti.py on t x b^3, b = 4, 6, 8,
t = 2, 3, 4, 6, 8, 16, grid 0.5 ... 2.5 (16 points); free-wall ti.py on (b,b,b), (2b,b,b), (2b,2b,b), (2b,2b,2b),
b = 2, 3, and (4,4,4), (8,4,4), times 2, 3, 4, 12.

Family 1b (S, S_ev). Criterion: s_* < 1/5041 counts as reachable at a measured cube (N; (2N)^3) only if the
measured G(N) < 2e-4 at 2 sigma; that is not expected at these sizes, so the verdict rests on the fall of G with N
and b and on a dilute-gas extrapolation G = sum over levels of mult x exp(-t E), with E from spectroscopy. The
extrapolation is GUIDE and is valid only where the measured G at the largest t agrees with the gas formula within
2 sigma. NO ROOM if G does not fall with t at fixed b in the confined range.

Family 2 (transport). Measured: d_beta G(t) = 6 t b^3 (P_t - P_T), split into temporal (electric) and spatial
(magnetic) parts, and K_eff = d_beta G / (t <E> G) with <E> from the slope of log G in t, and the level form
K_E = -d log E / d beta from E at beta 2.3 and 2.5. Criterion: compare the average of K over [beta_0, beta_1] with
log(b/(2 ceil(log2 b)))/(beta_1 - beta_0): for beta_1 = 2.3 and b = 256, 1024, 4096 the allowed averages are 1.21,
1.69, 2.17. ROOM if K_eff in the band is below the allowed average, TIGHT if within a factor 2, NO ROOM if above
by more than a factor 2. A sign check: the magnetic (spatial) part of d_beta G must be compared with the electric
part; row 708's Way 1 predicts the magnetic part is negative relative to the vacuum by about 3 E per level.

Family 3 (free-wall engine). Measured: g(a; B) by TI with free walls, E(a; B) = g(a; B|B) - 2 g(a; B), and the
doubling ratios k = g(after)/g(before) on the three ladder steps. Criterion: Theorem C needs k with
s_0 < 1/(4 k^6); with k measured, ROOM if the measured k is at most 3 on every step at a size where the seed
S(a_0; b_0^3) is also within a factor 10 of 1/(4 k^6); TIGHT if k is between 3 and 4; NO ROOM if k > 4 or if k
grows with b. Row 910 4.5 predicts k = 2 + 1/(b-1) at small beta.

### Step 5. Family 4 (EXC): the odd sector's spin excess Delta(1) (GUIDE)

Criterion (written in Step 1, before the twist runs, which carried the spin measurement at s = +1 and s = -1):
(DRESS) needs Delta_hi(1) > 0, of order L_i; a scale for "of order" is check 881's gamma about 0.010 per unit L_i,
so about 0.04 to 0.08 on L_i = 4 to 8. ROOM if Delta_hi(1) exceeds 0.01 L_i at 2 sigma; NO ROOM if it is below 0 at
2 sigma; UNMEASURED if the 1-sigma error exceeds the needed scale's resolution, i.e. if |Delta| cannot be told from 0.

Estimator: Delta(1) = rho (<N>_0 - <N>_v)/(1 - rho) per time step, N the row-860 spin weights summed over the
temporal plaquettes of one time step (steps not containing the stack), for three spin classes. Script
scripts/ana_exc.py, output out/exc_summary.txt (median and 16-84 percent range; rho error included).

| run (a, b, beta) | rho | Delta, all half-integer spins | Delta, spin 3/2 | Delta, spin >= 5/2 | <N_hi>_0 per step |
|---|---|---|---|---|---|
| 4, 4, 2.3 | 0.44 | +0.85 [+0.38, +1.3] | +0.011 [-0.014, +0.036] | -0.0002 [-0.0007, +0.0003] | 3(5)e-4 |
| 4, 6, 2.3 | 0.52 | +3.2 [+1.4, +5.6] | -0.03 [-0.12, +0.06] | -0.0018 [-0.0035, -0.0003] | -1.1(7)e-3 |
| 4, 8, 2.3 | 0.77 | +16 [+6, +55] | -0.2 [-0.9, +0.1] | -0.011 [-0.039, -0.003] | -3(2)e-3 |
| 6, 4, 2.3 | 0.66 | +0.86 [-0.06, +1.9] | -0.004 [-0.05, +0.05] | -0.0013 [-0.0023, -0.0003] | 2(4)e-4 |
| 6, 6 and 6, 8, 2.3 | about 1 | undefined (1 - rho within error of 0) | | | |
| 6, 4, 2.5 | 0.36 | +0.20 [+0.08, +0.32] | +0.019 [+0.006, +0.032] | +0.0004 [-0.0001, +0.0009] | 3(5)e-4 |
| 6, 6, 2.5 | 0.30 | +0.10 [-0.12, +0.33] | +0.016 [-0.02, +0.05] | +0.0005 [-0.0000, +0.0011] | 1.3(1.0)e-3 |
| 6, 8, 2.5 | 0.29 | +1.3 [+0.7, +2.1] | +0.12 [+0.08, +0.20] | -0.0016 [-0.0035, -0.0001] | 0.7(2)e-3 |

Reading (GUIDE).
- The estimator's noise on N_hi is about 5e-4 to 2e-3 per time step, while the true density gives
  <N_hi>_0 = 3 b^3 x 6e-7 to 1.3e-6 = 1e-4 to 7e-4 (row 860's and Step 2's densities). The measured <N_hi>_0 values
  scatter around 0 by this noise (two of them negative at 1.5 sigma). So the spin >= 5/2 column is noise. The 1-sigma
  range of Delta_hi is about +-1e-3, already above the expected signal (next point).
- The lower spins are measurable. The odd sector carries a positive excess of half-integer spin: +0.2 to +16 per
  time step, positive in 7 of 7 defined runs, growing with b at beta 2.3, a = 4 (the flux line plus its dressing).
  At beta 2.5 the spin-3/2 excess is positive at 2 to 3 sigma, and Delta_(3/2)/Delta_half = 0.095 (b = 4) and 0.097
  (b = 8), against the bulk ratio rho_(3/2)/rho_(1/2) = 3.7e-3/0.39 = 0.0095 (Step 2). So the odd sector's excess is
  about 10 times richer in spin 3/2 than the vacuum. This is the sign (DRESS) asks for, one spin lower.
- Extrapolation (ARGUED, GUIDE): if spin 5/2 is enriched by the same factor 10 over the bulk ratio
  rho_(5/2)/rho_(3/2) = 1.3e-6/3.7e-3 = 3.5e-4 at beta 2.5, then Delta_hi(1) is about 0.12 x 3.5e-3 = 4e-4 at
  (6, 8, 2.5), and about 1e-4 at beta 2.3. That is 100 to 200 times below the scale 0.01 L_i and about 4 times below
  this campaign's noise. EXC integrates Delta(s) ds/s up to s_* = r_V^(2T)/r_(5/2), about 0.484/1.85e-3 = 260 at
  beta 2.3 (my arithmetic from gamma = 0.010 and Step 2's r_(5/2)); a linear-response guess Delta(s) about s Delta(1)
  gives an integral of about 260 x 1e-4 = 0.03 per time step, which is not small against any fixed c_0 > 0 only
  if the response stays linear up to s_*. No run here reaches s > 1 (the boosted weight is not positive).
- Verdict: UNMEASURED at spin >= 5/2 (signal below noise); the measured proxy (spin 1/2 and 3/2) has the right sign.

### Step 3b. The last twist shape, and the spectroscopy of the 8^3 box (GUIDE)

- tw_8_8_2.5: log rho = -1.08 (32) by BAR, -0.82 (37) by Simpson, -0.56 (32) by Simpson with the improved estimator
  (the three differ by up to 1.1 sigma; errors are large). rho between 0.3 and 0.6: a = 8 is the deconfinement
  length at beta 2.5 (RECALLED: beta_c(N_t = 8) about 2.51), and (CORE) is not met at b = 8.
- spec.py, 16 x 8^3, 500 measurements, 8 APE steps (logs out/spec_16_8_<beta>.log). Effective energies E(d) =
  log C(d)/C(d+1):
  beta 2.3: torelon (odd under one centre flip) 0.956 (20), 0.924 (42), 0.980 (113) at d = 0, 1, 2: E_f(8) = 0.94 (3).
  Check: sigma b - pi/(3b) with a^2 sigma = 0.136 (RECALLED) gives 0.957. 0++ glueball (even): 1.46 (6), 1.26 (22),
  1.03 (45): m_0 about 1.3 (2) (no plateau; the d = 0 value is an upper bound).
  beta 2.5: torelon 0.206 (7), 0.182 (10), 0.168 (15), 0.142 (17), 0.125 (17), 0.103 (17), 0.076 (16): no plateau, the
  odd level of the 8^3 box is below 0.1 (b sqrt(sigma) about 1.5: small-box regime). 0++: 1.16 (3), 0.98 (11),
  0.86 (19): m_0 about 0.9 (2).

### Step 6. Family 1b: the thermal sum S, its even part S_ev, and the size where s_* < 1/5041 (GUIDE)

Direct measurement (ti.py + ana_ti.py, T = 16 reference, trapezoid on the 16-point grid plus (0, 0); logs
out/ti_<t>_<b>.log). G = log(1 + S) - (t/16) log(1 + S(16)):
| beta | t x b^3 | G measured | gas model (below) |
|---|---|---|---|
| 2.3 | 2 x 4^3 | 6.9 (1.0) | 5.3 |
| 2.3 | 3 x 4^3 | 4.2 (1.2) | 1.7 |
| 2.3 | 4 x 4^3 | -0.5 (1.3) | 1.0 |
| 2.3 | 6 x 4^3 | 0.8 (1.8) | 0.6 |
| 2.5 | 2 x 4^3 | 8.2 (1.0) | (gas undefined: E_f < 0) |
| 2.5 | 3 x 4^3 | 5.2 (1.2) | (undefined) |
| 2.5 | 4 x 4^3 | 0.5 (1.4) | (undefined) |
The error of this estimator is extensive (about 1 to 2 at b = 4, growing like b^(3/2)): it resolves G only in the hot
boxes t = 2, 3, where S is 60 to 3000. Below G of about 2 it resolves nothing; at b = 8 I dropped the runs for that
reason (they would give errors of 5 to 10). So no direct measurement reaches the seed regime; the numbers below are
an extrapolation.

Dilute-gas extrapolation (scripts/gas.py; out/gas_2.3.txt, out/gas_2.5.txt). Assumption: free glueballs (0++ with
m_0 from Step 3b and the RECALLED large-volume value; heavier states with RECALLED mass ratios 1.45 to 1.8 and 15
more states) plus one Z_2 electric flux per direction with E_f(b) = sigma b - pi/(3b), RECALLED a^2 sigma.
Then 1 + S = e^(G_glue + 3z), 1 + S_ev = e^(G_glue) cosh(z)^3, rho = e^(-2z). It ignores deconfinement, so it is
meaningful only for t above the deconfinement length.
Validation against this campaign's data: rho at beta 2.3, a = 6: model log rho -0.37, -0.05, -0.01 for b = 4, 6, 8
against measured -0.41 (7), +0.03 (10), +0.28 (20) (agree within 1.4 sigma). At a = 4 (critical) the model
underestimates the flux: -0.68, -0.25 against -0.82 (7), -0.62 (10). At beta 2.5, a = 6, 8: model -1.72, -0.96, -0.68
against -1.22 (15), -1.23 (28), -0.56 to -1.08: right size, not precise. Torelon energy at b = 8, beta 2.3: model
0.957, measured 0.94 (3).

Results of the extrapolation (GUIDE; two m_0 values bracket the uncertainty):
- (SEED-FP) cube S(N; (2N)^3) < 1/5041: beta 2.3: N = 9 to 10 (cube side 18 to 20, time 9 to 10), m_0 N = 12.6 to 13.0.
  beta 2.5: N = 14 to 17 (side 28 to 34), m_0 N = 11.9 to 12.6. In physical units the box is the same: m_0 N about
  12.5, i.e. N sqrt(sigma) about 3.4 (m_0/sqrt(sigma) about 3.7, RECALLED), side about 6.8/sqrt(sigma).
- How fast: on the cube, S falls by a factor about 3 to 4 per lattice unit of N at beta 2.3 (beta 2.3, m_0 = 1.3:
  N = 4, 5, 6, 8, 10, 12: S = 0.44, 0.064, 0.011, 7.4e-4, 6.8e-5, 6.3e-6), about e^(-m_0) times (N+1)^(3/2)/N^(3/2).
  Flux part: Q_0 = 0.071, 0.0097, 6.8e-4, 5.8e-7 for N = 4, 5, 6, 8: it falls like exp(-2 sigma N^2), much faster than
  the glue part. From N = 6 on, S_ev carries S: S_ev/S = 0.81 at N = 6, 0.998 at N = 8.
- Theorem SH shape (a; (24a)^3), S <= 3/10: beta 2.3: a = 9 (S = 0.47) to 10 (S = 0.12), so b = 216 to 240; beta 2.5:
  a = 14 to 17, b = 336 to 408. The flux half (CORE) is met there by a huge margin (Q_0 below 1e-9 already at a = 3 to
  6 on b = 24 a in the model); the glue half carries everything (S_ev = S).
- What the measurements add: the direct runs confirm the hot boxes (t = 2, 3) are far above any seed (G = 4 to 8);
  the twist runs confirm the flux half is already small at a = 6, b = 6 at beta 2.3 (Step 3). The glue half at the
  seed size is not measured.

Addendum to Step 6 (b = 6, logs out/ti_<t>_6.log, summary out/ti_b6_summary.txt): G(2; 6^3) = 26.6 (2.0) at 2.3 and
30.2 (2.0) at 2.5; G(3; 6^3) = 4.8 (2.2) and 7.5 (2.2); G(4; 6^3) = 2.5 (2.7) and 3.6 (2.8). Gas model at 2.3:
11.7, 1.6, 0.43. The model fails in the hot boxes (deconfined, t below about 4 at 2.3), as expected.

### Step 7. Family 2 (transport): thermal plaquette excess, its magnetic part, and the rate K (GUIDE)

Measured (same runs as Step 6): d_beta G(t) = N_c (P_t - (t/16) P_16 ...) at the endpoint beta, i.e. the thermal excess
of the plaquette action between the short and the long torus, split into temporal (electric) and spatial (magnetic)
plaquettes. <E>_t = -d_t G by the central difference of the measured G. K_eff = d_beta G / (t <E>_t).
| beta | t x b^3 | d_beta G | electric part | magnetic part | <E>_t | K_eff | beta x magnetic / (t <E>) |
|---|---|---|---|---|---|---|---|
| 2.3 | 2 x 4^3 | 10.6 (1.8) | 11.1 (9) | -0.5 (1.0) | 2.7 (1.6) (forward diff.) | 2.0 (1.3) | -0.2 (0.4) |
| 2.3 | 3 x 4^3 | 7.3 (2.7) | 4.1 (1.3) | 3.2 (1.4) | 3.7 (0.8) | 0.66 (0.3) | +0.7 (0.3) |
| 2.5 | 2 x 4^3 | 3.0 (1.4) | 7.7 (7) | -4.7 (9) | 3.0 (1.6) | 0.5 (0.3) | -2.0 (1.1) |
| 2.5 | 3 x 4^3 | 4.6 (1.8) | 3.9 (8) | 0.7 (1.0) | 3.9 (0.9) | 0.40 (0.17) | +0.2 (0.2) |
| 2.3 | 2 x 6^3 | 32.9 (3.3) | 39.8 (1.6) | -6.9 (1.8) | 21.8 (3.0) (forward) | 0.75 (0.13) | -0.36 (0.11) |
| 2.3 | 3 x 6^3 | 29.5 (4.7) | 20.7 (2.1) | 8.8 (2.8) | 12.0 (1.7) | 0.82 (0.2) | +0.56 (0.2) |
| 2.5 | 2 x 6^3 | 13.0 (2.5) | 27.2 (1.2) | -14.2 (1.4) | 22.7 (3.0) (forward) | 0.29 (0.07) | -0.78 (0.13) |
| 2.5 | 3 x 6^3 | 1.9 (4.2) | 6.1 (2.3) | -4.2 (2.0) | 13.3 (1.8) | 0.05 (0.10) | -0.26 (0.13) |
| 2.3, 2.5 | 4, 6 x 4^3, 6^3 | 4 to 12, errors 3 to 6 | | | not resolved (G errors 1.3 to 2.8) | | |
All rows are hot boxes (t at or below the deconfinement length). In the cold boxes, where (VIR-log)'s characteristic
curve lives (Remark CH of row 708), the thermal form is not resolved by these runs.

Level form, from the spectroscopy of the 8^3 box (Step 3b): K_E = -d log E/d beta between 2.3 and 2.5.
- 0++ glueball: m_0 = 1.3 (2) -> 0.9 (2): K_E = log(1.3/0.9)/0.2 = 1.8, range 0 to 3.8 at 1 sigma. RECALLED large-volume
  scaling (row 708's a sqrt(sigma) values): 3.3.
- torelon of the 8^3 box: 0.94 (3) -> about 0.1 to 0.2 (no plateau): K_E = 8 to 11. This level is absent from the
  thermal mean of the b >= 256 cube (E_f = sigma b, about 35 at 2.3), so it does not enter (VIR-log), but it does
  enter the level form (LEV_K) if every ordered level is required.
Needed: average K over [beta_0, 2.3] at most log(b/(2 ceil(log2 b)))/2.3 = 1.21, 1.69, 2.17 for b = 256, 1024, 4096.
The strong-coupling end alone, K about 1/(beta log(4/beta)) (row 708, GUIDE), integrates to about 2.1 between 1/25600
and 1 (my arithmetic: log log(4 x 25600) - log log 4). With K = 1.8 on [1, 2.3] the integral is about 4.4, so
b/(2 ceil(log2 b)) >= e^4.4 = 81, b about 2000; with K = 3.3 it is about 6.4 and b about 2 x 10^4.
Magnetic part: in the hot boxes it is negative at t = 2 (beta x magnetic/(t <E>) = -0.2 to -2.0) and positive at t = 3
at 2.3. Row 708's Way 1 predicts about -3 per level; the hot-box thermal means are of that sign at t = 2, smaller in
size. This is a proxy only: thermal means of hot boxes, not single levels.
Verdict against the pre-registered criterion: K_E (glueball) 1.8 against the allowed 1.2 to 2.2: TIGHT; the hot-box
thermal K_eff 0.05 to 2.0: below the allowed average, but measured in the wrong regime.

### Step 8. Family 3 (free-wall engine): first attempt fails on precision; a second estimator (GUIDE)

First attempt: g(a; B) by beta-TI with free walls (logs out/fwti_*.log, analysis scripts/ana_fw.py), b = 2 ladder,
a = 2, 3, 4. Result: g = 0.1 to 0.6 with errors 0.15 to 0.9 (for example g(2; 2^3) = -0.25 (15), g(4; 2^3) = 0.10 (27)
at 2.3). The doubling ratios k come out as 0.1 (1.3), 4.7 (13) and so on: no information. The TI error is extensive
in the whole box and over the whole beta range, while g itself is of order 0.1. I stopped that queue after the b = 2
ladder and part of b = 3 (no result from it is used below).

Second estimator, new script scripts/split.py ("cut and reglue" in time): a 2a-slice lattice whose gluing plaquettes
(the temporal plaquettes at slices a-1 and 2a-1) interpolate between one torus of period 2a (weight s) and two tori of
period a (weight 1 - s); both staples add. Exact identity: g(2a) - 2 g(a) = beta int_0^1 <X>_s ds, X = sum over gluing
plaquettes of (x^long - x^pair). So Delta(a) = 2 g(a) - g(2a) is measured with an error set by the 2 x (gluing area)
plaquettes only, and g(a) = Delta(a)/2 + Delta(2a)/4 + Delta(4a)/8 + ... (the tail is positive and decays).
Validation (written before the run: pass if it agrees with the TI value of Step 6 within 2 sigma): periodic 2 x 4^3
at 2.3: split.py Delta(2) = 13.4 (8); TI: 2 G(2) - G(4) = 2 x 6.9 (1.0) - (-0.5 (1.3)) = 14.3 (2.4). PASS (0.4 sigma;
independent data paths: one interpolates two gluings at one beta, the other integrates plaquettes over beta).

Free-wall results with split.py at beta 2.3 (logs out/spfw_<a>_<box>_2.3.log, analysis scripts/ana_split.py; b = 2
ladder; 8 Gauss points, 300 measurements each):
| box | Delta(2) | Delta(4) | Delta(8) | g(2) (median, 16-84 %) | g(4) |
|---|---|---|---|---|---|
| 2x2x2 | -0.06 (17) | 0.11 (15) | 0.20 (18) | 0.02 [-0.08, 0.11] | 0.10 [0.02, 0.19] |
| 4x2x2 | 0.10 (36) | -0.46 (26) | 0.07 (24) | -0.06 [-0.25, 0.13] | -0.22 [-0.36, -0.07] |
| 4x4x2 | 0.69 (41) | -0.79 (33) | 0.42 (42) | 0.20 [-0.03, 0.43] | -0.29 [-0.49, -0.10] |
| 4x4x4 | 0.89 (51) | 0.67 (58) | -0.13 (58) | 0.59 [0.29, 0.90] | 0.30 [-0.02, 0.62] |
A positive transfer operator forces Delta >= 0 and g >= 0. Two of the twelve Delta values are negative at 1.8 and 2.4
sigma, so the quoted errors are probably too small (short thermalization between s points, 10 bins); I read every
entry as "0 within about 0.5". The doubling ratios k = g(after)/g(before) come out between -1.6 and +1.8 with ranges
wider than 3: undetermined. The join excess E = g(after) - 2 g(before) is between -0.4 and +0.9: undetermined at the
level that matters (the engine works on cold boxes, g <= 1/(3 k^4), about 1e-3 for k = 3).
So the free-energy route to the doubling ratio is UNMEASURED at these sizes: the required precision (about 1e-4 on g)
is 3000 times below what either estimator delivers here. Next: a spectral proxy (Step 8b).

b = 3 free boxes, beta 2.3: 3x3x3: Delta(2, 4, 8) = 0.84 (38), 0.05 (39), -0.42 (35); 6x3x3: 0.49 (44), 0.20 (70),
0.37 (55). Ratios undetermined (k for a = 2: 0.8 [0.03, 2.1]; a = 4: -0.4 [-3.8, 3.0]). Same reading: 0 within 0.5.

Addendum to Step 6 (periodic boxes with split.py; out/spp_<a>_<b>_<beta>.log): Delta(a; b^3) = 2 G(a) - G(2a):
| beta | a x b^3 | Delta measured | gas model 2 G(a) - G(2a) |
|---|---|---|---|
| 2.3 | 4 x 4^3 | 1.24 (64) | about 1.7 |
| 2.3 | 4 x 6^3 | 1.5 (1.7) | about 0.86 |
| 2.3 | 6 x 6^3 | -0.4 (1.5) | about 0.15 |
| 2.5 | 4 x 4^3 | 3.65 (73) | hot box (a below the deconfinement length) |
| 2.5 | 4 x 6^3 | 5.1 (1.9) | hot box |
Since G(a) >= Delta/2, these give G(4; 4^3) >= 0.6 (3) at 2.3 and G(4; 4^3) >= 1.8 (4) at 2.5. In the cold boxes the
error (1.5 at b = 6) is again far above the seed scale. The split estimator is 2 to 4 times better than beta-TI at the
same cost, not 1000 times.

### Step 8b. Family 3, spectral proxy: the lowest even level of free-wall boxes along the ladder (GUIDE)

Why this proxy (row 910 4.1, READ above): d g_s/ds = -a <m'>_(a; s), so (JOIN-TH) says that closing the cut lowers the
excitation energies, in the thermal mean, by at most about kappa/a. In the dilute cold limit g(B) = n e^(-a m(B)),
so k = g(B|B)/g(B) is about (n'/n) e^(a (m(B) - m(B|B))). Criterion (written before these runs): if the lowest even
level drops by delta m on a ladder step, then a delta m <= log(k/2) is needed (n'/n about 2 for a doubled box).
Runs: spec.py with free walls, 16 x box, 400 measurements, 6 APE steps (logs out/fwspec_<box>_<beta>.log).
Effective energy log C(0)/C(1) of the vacuum-subtracted sum of smeared spatial plaquettes (an UPPER bound on the
lowest even level; no plateau is resolved; d = 1 values have errors 0.4 to 2.4):
| box | beta 2.3 | beta 2.5 |
|---|---|---|
| 4x4x4 | 2.67 (16) | 2.65 (16) |
| 8x4x4 | 2.79 (18) | 2.48 (13) |
| 8x8x4 | 2.26 (16) | 2.16 (9) |
| 8x8x8 | 2.04 (12); d = 1: 1.47 (42) | 1.85 (7); d = 1: 1.57 (41) |
Reading: per ladder step the upper bound drops by -0.12 (24), +0.53 (24), +0.21 (20) at 2.3 and +0.18 (21), +0.31 (16),
+0.31 (11) at 2.5. If the true levels drop like these bounds, then at a = 4 the step 8x4x4 -> 8x8x4 has
a delta m about 2.1 at 2.3, i.e. k about 2 e^2.1 = 16, far above k = 3. These are bounds contaminated by excited
states, so this is an indication, not a measurement. For a massive spectrum the drop per step should shrink like
1/b^2 while a grows like b on the ladder, so a delta m falls like 1/b; at b = 4 to 8 the boxes are still well inside
that finite-size regime (the 8^3 bound 1.5 to 2.0 is above the large-volume m_0 of 1.3 (2) at 2.3).
Verdict for family 3: UNMEASURED (the free-energy estimators give g = 0 within 0.3 to 0.5, against a needed precision
of about 1e-4); the spectral proxy points to large k (TIGHT to NO ROOM) on the small boxes reachable here.

### Step 9. Final table and result

All numbers GUIDE (Monte Carlo on small lattices, this campaign's scripts in lane918/scripts, logs in lane918/out).
"Needed" is the value the proof step needs (Step 1). Errors are 1 sigma.

| family | measured quantity | value the proof needs | measured value (error) | verdict |
|---|---|---|---|---|
| 1 seed: S | G = log(1 + S) on t x b^3 (beta-TI; cut and reglue) | cube S(N; (2N)^3) < 1/5041 = 2.0e-4 | 2.3: G(2; 4^3) = 6.9 (1.0), G(2; 6^3) = 26.6 (2.0), G(4; 4^3) >= 0.62 (32); 2.5: G(2; 4^3) = 8.2 (1.0), G(4; 4^3) >= 1.8 (4). Cold boxes not resolved (errors 1.3 to 2.8). Gas model checked on rho and E_f: S < 2e-4 first at N = 9-10 (2.3), N = 14-17 (2.5), i.e. m_0 N about 12.5; S falls about 3-4 times per lattice unit of N | NO ROOM at N <= 4 (measured); UNMEASURED at the seed size, which the extrapolation puts at cube side 18-20 (2.3) and 28-34 (2.5) |
| 1 seed: S_ev | glue half | S_ev <= 1/10 at b >= 24 a (SH split), or <= s_*/2 | not separable from S at these errors; gas model: S_ev/S = 0.81 (N = 6), 0.998 (N = 8): the glue half carries the whole seed from N = 6 on | UNMEASURED (no direct estimator resolves it); gas model says S_ev = S at the seed size |
| 1 seed: flux half (CORE) | rho = Z^(v_01)/Z^0 by stack interpolation + BAR | rho >= 0.9 (log rho >= -0.105), b >= 24 a | 2.3: a = 6: log rho = -0.41 (7) at b = 4, +0.03 (10) at b = 6, +0.28 (20) at b = 8; a = 4: -0.82, -0.62, -0.27 (18); a = 2: -7.28 (7). 2.5: a = 6: -1.02, -1.22, -1.23 (28); a = 8, b = 8: -0.56 to -1.08 (32) | 2.3: ROOM at a = 6, b = 6 (1 sigma; TIGHT at 2 sigma), already at b = a, not 24 a; NO ROOM for a <= 4. 2.5: NO ROOM for a <= 8 (below the deconfinement length) |
| 2 transport | K_E = -d log E/d beta (spectroscopy, 8^3); K_eff = d_beta G/(t <E>) and its magnetic part (hot boxes) | average K over [beta_0, 2.3] <= 1.21 / 1.69 / 2.17 for b = 256 / 1024 / 4096 | glueball K_E = 1.8 (range 0 to 3.8); torelon of the 8^3 box 8 to 11 (absent from the large-b thermal mean); hot-box K_eff 0.05 (10) to 2.0 (1.3); magnetic part of d_beta G negative at t = 2 (beta x mag/(t <E>) = -0.2 to -2.0), positive at t = 3, 2.3 | TIGHT (glueball rate within a factor 1.5 of the allowed average; strong-coupling end alone uses about 2.1 of the budget; b of order 2e3 to 2e4) |
| 3 free-wall engine | g(a; B), join excess E = g(B|B) - 2 g(B), doubling ratio k on free-wall boxes 2^3 ... 4^3, 3^3, 6x3x3 | k with s_0 < 1/(4 k^6) on cold boxes (S <= 1/(3 k^4)), e.g. k <= 3 and g about 1e-3 | g = 0 within 0.3-0.5 on every box (two Delta values negative at 1.8, 2.4 sigma); k between -1.6 and 1.8 with ranges wider than 3; E between -0.4 and 0.9. Proxy: free-box even-level bound falls 2.67 -> 2.04 (2.3), 2.65 -> 1.85 (2.5) from 4^3 to 8^3; a delta m about 2 at a = 4 on one step | UNMEASURED (needed precision on g about 1e-4, 3000 times below the noise); proxy suggests large k on these small boxes |
| 4 EXC | Delta(1) = rho (<N>_0 - <N>_v)/(1 - rho), spin >= 5/2 half-integer temporal plaquettes per time step | Delta_hi(1) > 0 of order L_i (scale about 0.01 L_i = 0.04-0.08); integrated over s up to s_* about 260 | Delta_hi(1) = 0 within about 1e-3 on all 9 defined runs (e.g. (6, 4, 2.5): +0.0004 [-0.0001, +0.0009]); proxy: Delta_(3/2) = +0.019 (13), +0.12 (5) at 2.5, about 10 times richer in spin 3/2 than the vacuum; extrapolated Delta_hi(1) about 1e-4 to 4e-4 | UNMEASURED (signal 4 times below noise); proxy has the (DRESS) sign, and the extrapolated size is 100-200 times below 0.01 L_i |

Provenance and limits. Every number here comes from this campaign's own sampler (validated in Step 2 against a
sequential heat bath and against row 860), except the RECALLED inputs named where used: a^2 sigma = 0.136 (2.3) and
0.0336 (2.5), the large-volume m_0 values 1.4 and 0.7, glueball mass ratios, beta_c(N_t) values, and row 708's K = 3.3.
Nothing here is proof. No repository file was edited. Runs: about 2 hours of single-core compute in all; one validation
run took 317 s (over the 5-minute guide); one twist run (8 x 8^3) was killed by a monitor timeout and rerun.

RESULT: GUIDE only, no proof: on small Wilson SU(2) lattices the flux half (CORE) has room at beta 2.3 already on 6 x 6^3 (log rho = +0.03 (10), against -0.105 needed) but none at a = 8 or below at beta 2.5; the seed S and its glue half S_ev are measured only in hot boxes (G = 4 to 27, NO ROOM there) and a dilute-gas extrapolation checked on rho and the torelon energy puts S < 1/5041 first at cube side 18-20 (2.3) and 28-34 (2.5), m_0 N about 12.5, with S_ev = S there, so the glue half carries the whole seed; transport is TIGHT (glueball rate K_E = 1.8 (0 to 3.8) against an allowed average of 1.2 to 2.2 for b = 256 to 4096); the free-wall doubling ratio and the EXC spin-5/2 excess are UNMEASURED (signals 3000 and 4 times below the noise), with proxies that point to large k on small free boxes and to a positive but about 100-fold too small (DRESS) excess.
