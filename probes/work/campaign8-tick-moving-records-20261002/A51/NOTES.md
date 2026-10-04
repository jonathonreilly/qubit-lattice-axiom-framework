# A51 notes (long-range inverse search; exploration only, nothing adopted)

Started 2026-10-04 06:37. Owner decisions 28 (exact turns) and 22 (beyond six neighbours, exploration scope).

## 0. Setup / plan
- Basis: dual-frame Heisenberg class sums O_c = sum_{unordered torus pairs in class c} s_i.s_j, c = {|d_a| up to signs
  and perms}, folded components <= L/2 (L=6: 19 classes, L=8: 34, L=10: 55); plus A49's four-spin terms (8 star + 2 plaquette).
- Soldered image of s_x.s_{x+d}: sum_b eps_b(d) s^b s^b, eps_b(d) = (-1)^{d_{b+1}+d_{b+2}} (translation invariant for even L).
  Covariance argument: a turn g maps b -> pi(b), d -> gd with (gd)_{pi(i)} = +-d_i; the complement pair {b+1,b+2} maps to
  {pi(b)+1, pi(b)+2}, so eps_{pi(b)}(gd) = eps_b(d) (EXACT). Numerical check below (cov_defect) for a few classes.
- Estimator: s.s conserves S^z; the parton is an exact singlet in S^z = 0; local estimator X0_ij = z_i z_j + (1 - z_i z_j) R2_ij
  is exact for every pair (any separation) wherever psi(s) != 0 -> rank-0 covariance in S^z = 0 is the full covariance.
- KEY TRAP (EXACT): at full reach the class basis contains the total-spin Casimir sum_{i<j} s_i.s_j = 2 S^2 - 3N/2, which
  annihilates (up to the constant) EVERY singlet -> min relative variance is trivially 0. Also partial Casimirs (all classes
  up to R) get small relative variance for any singlet as R -> L/2. Fix: report lam with the Casimir-removed metric
  G' = G - g g^T / ||Cas||^2 (g_c = <O_c, Cas>/N = G_cc), i.e. size of a rule measured modulo the Casimir. G' -> G at fixed
  reach as N -> infinity. Also report plain-G numbers.
- Positive control for every long-range pair estimator at once: E_Cas(s) = sum_c E_c(s) = -3N/2 per sample for a singlet.

## 1. Basis checks (basis51, 8.7 s, 638 MB)
- 11 classes up to (1,3,4), (0,2,5): soldered image has covariance defect 0.0 and equals its own 24-turn average (4e-16). EXACT+CHECKED.
- (0,0,1) image = A49 dual J1 = -J1 + 2K1 to 6e-17.
- Class counts: L=6: 19, L=8: 34, L=10: 55; sum m_c = N - 1; K symmetric.
- Casimir positive control: random S^z=0 configuration at L=8, 10: sum_c E_c = -3N/2 exactly (-768, -1500).
- Timing: class estimator 10 ms (L=8), 40 ms (L=10) per sample.
- Test VMC 6^3 400 sweeps: NN s.s/bond -1.0122 (A44 -1.010(2)); four-spin <T0> -0.455, <C0> -0.412, <P0> 1.359 (A49 -0.457, -0.407, 1.358);
  Casimir estimator max deviation 8.9e-12 over all samples.
- Infrastructure: chain2.sh queue runner (jobs/ dir; p_* priority) -> every job through run.sh, one at a time.
- Gauge note: at full reach the Casimir-removed minimizer is defined modulo J_c -> J_c + mu; profile uses the most-local gauge
  mu = sum m d^2 J / sum m d^2, then J_NN = 1.

## 2. First 6^3 results (34,138 parton samples; anal51b)
- LSWT formula check (lswt_check): Neel J1-J2 j=0.2 per bond -0.90591 (6^3 grid), -0.90694 (8^3) -> A47 -0.90717 (its 8-site cell,
  i.e. 16^3 equivalent); j=0 cubic AF -0.8956 J_S per site. OK.
- Cross-check vs A49 (plain metric, same operator sets): S1b-inv(3) 0.0412(20) [A49 S1b 0.0399(11)]; S1inv(11) 0.00291(30)
  [A49 0.00257(21)]; S1uS2inv(14) 0.00277(30) [A49 0.00248(20)]. Agree within 1 sigma.
- Full reach, Casimir-removed metric: B (19 classes) lam 0.0061(11); B4 (19+8) lam 0.00263(40).
  finite reach: B_r4 0.0303, B_r9 0.0126, B_inner(9) 0.0131; B4_r4 0.00319, B4_r9 0.00280, B4_inner 0.00292.
- B-only minimizer does NOT decay: J(3,3,3)/J_NN = -0.69, (2,3,3) -0.55 -> long-wavelength structure-factor mode.
  q-orbit check: P_Q at Q = 2pi/6 (0,0,1) alone has lam 0.0077 vs Gaussian estimate Sbar(Q)^2 = 0.0073 (Sbar = 0.085).
  => GENERIC MECHANISM (ARGUED + CHECKED): long-range rules concentrated at small q have lam ~ S(q)^2, S(q->0) -> 0 for any
  singlet / spin liquid; this needs reach ~ 1/q and falls with L trivially. Not a parent.
- B4 minimizer decays fast: NN 1, FD 0.76, (0,0,2) 0.42, rest <= 0.1; four-spin C0 0.90, T0 0.77, T2 0.55.
- HS-like ansatz (J = s/D^alpha): best af alpha=1 0.0175 (B only; small-q dominated), + four-spin 0.012; alpha=2: 0.046 / 0.018. Bad.
- Fix needed: anal51 crashed on 1-operator subsets; add long-wavelength-removed metric (project out q-orbits 0 < |q| <= pi/2
  and the Casimir from the norm: G_W = G - G W (W^T G W)^-1 W^T G).

## 3. 6^3 reach table (parton; mod = Casimir removed; LW = also |q| <= pi/2 orbits removed from the norm)
 R^2 ncls | B mod   B4 mod     | B LW   B4 LW
   1   1  | 0.877   0.0653     | 1.25   0.0846
   2   2  | 0.0514  0.00886    | 0.110  0.0177
   4   4  | 0.0303  0.00319    | 0.0854 0.00732
   6   6  | 0.0147  0.00293    | 0.0814 0.00708
   9   9  | 0.0126  0.00280    | 0.0690 0.00678
  12  12  | 0.0098  0.00275    | 0.0573 0.00664
  27  19  | 0.0061  0.00263    | (full-reach LW row was wrong: Euclidean range choice; fixed with releig_q = quotient/Schur)
- B4 floor is flat with reach (0.0032 -> 0.0026 from R^2=4 to full); B falls with reach via small-q modes.
- The B4 rule's norm sits largely at small q (LW metric raises lam 2.3x): the rule is ~ a smeared local Casimir
  (sum over stars of star-spin^2: AF J1, J2, J3 all positive) -> rewards small local total spin, a generic singlet property.

## 4. 6^3 forward tests (fwd51; J_NN = +1 sign, the sign where the parton is low)
- B4 full reach: LT min Q=2pi/6 (1,2,2), 63/216 k within 2% of span (massively degenerate). Classical collinear energies
  ferro +12.7, layer -0.02, col -0.73, Neel +0.20 per site; all LSWT(Hartree) UNSTABLE. Parton VMC -1.73405(12).
- B4_inner (finite reach |d|<=2 comps): fine-grid (40^3) LT: 18.9% of the BZ within 1% of span, 45% within 5% (volume-like
  near-degeneracy). Parton -1.72680(12); classical collinear >= -0.80.
- B (bilinear, full reach): LT spiral Q=(1,3,3)2pi/6 E_cl -0.890, LSWT -1.768 (stable, but 108/216 k within 2%);
  parton -1.7706(2). Neel LSWT -1.917 but unstable.
- Classical/LSWT competitors are useless here (huge degeneracy); need quantum competitors -> added projected columnar VBS
  ('vbs') and the 0-flux projected Fermi sea ('fs0') as singlet competitors, plus weak-order projected states.

## 5. 8^3 parton (9,448 samples, 3 batches) + releig_q fix
- releig_q (quotient over zero-norm directions, Schur complement) unit test: equals brute-force min 0.02124875; no blow-up for a
  zero-variance null direction. 6^3 full-reach LW row now 0.00652(50) (monotone).
- A49 sets at 8^3 (plain): S1b-inv 0.0410(50) [A49 0.0402(69)]; S1inv 0.00281(20) [0.00247(20)]; S1uS2inv 0.00269(20) [0.00231(15)].
- 8^3 table (mod | LW):  R^2  B mod      B4 mod      | B LW     B4 LW
                          4   0.0301     0.00292(22) | 0.068    0.00591(40)
                          9   0.00727    0.00236(12) | 0.0585   0.00562(30)
                         12   0.00551    0.00219(10) | 0.0552   0.00558(30)
                         16   0.00466    0.00210(20) | 0.0521   0.00552(30)
                         27   0.00239    0.00170(10) | 0.0434   0.00545(30)
                         48   0.00189    0.00154(11) | 0.0315   0.00539(30)   (bias-corr B4 mod full 0.00165)
- q-orbit P_(001) alone at 8^3: lam 0.00252 vs Sbar^2 0.00269 (Sbar 0.052). One long-wavelength mode already ~ the B4 short floor.
- Full-reach B4 profile 8^3: 1, 0.81, (1,1,1) 0.37, (0,0,2) 0.50, ~0.1-0.3 at |d|~3-4, then NEGATIVE far tail -0.16..-0.28
  at |d| 5.2-6.9 (long-wavelength admixture). Power fit alpha 1.67 (not meaningful: non-monotone, sign change).
- HS ansatz 8^3: af alpha=1 0.0072 (B) / 0.0057 (+4); alpha=2 0.028 / 0.014. Not competitive.
- Forward 8^3: B4_inner LT fine grid: 23% of BZ within 1% of span, 61% within 5% (J(q) = big peak at q=0, flat elsewhere:
  smeared local Casimir, pyrochlore-like extensive near-degeneracy). Collinear classical >= -0.76/site, all LSWT unstable;
  parton VMC -1.69469(11) (norm 4.794) under B4_inner; -1.68276(12) (norm 5.764) under B4 full.
- Clock check 07:05 (lane start ~06:31). Queue extended: 8^3 refs (neez, colz, fs0, vbs, lp:0.1), 10^3 parton x6 + neez x2,
  8^3 parton +2 batches; analyses queued after each block. Expected end ~08:35.

## 6. 6^3 references, controls, contest
- Controls (control51, 300 samples each, full sampling): pol predicted 7 null classes (all-same-parity d) -> 7 eigenvalues
  <= 6e-16 then 0.44; cs predicted 9 (|d|_1 even) -> 9 eigenvalues <= 2e-16 then 0.96. Parton plain-metric full-reach B:
  lam -1.3e-14 at the all-ones vector (Casimir) to 6e-11. PASS.
- lam_min (B4 mod) at R^2 = 4 / 9 / 12 / full(19):
  parton 0.00319 / 0.00280 / 0.00275 / 0.00263(40);  lam'=0.1 0.00332 / 0.00277 / 0.00262 / 0.00245(20)
  Neel .05 0.00427 / 0.00382 / 0.00359 / 0.00313(20); col .1 0.00576 / 0.00498 / 0.00466 / 0.00312(20)
  fs0 (0-flux FS) 0.0878 / 0.0464 / 0.0396 / 0.0314;   VBS (columnar dimers) 0 / 0 / 0 / 0 (<= 1e-14!)
  B LW-metric B4: parton 0.0073/0.0068/0.0066/0.0065; Neel 0.0101/0.0095/0.0093/0.0090; col 0.0132/0.0129/0.0121/0.0096.
- Gap Neel/parton (mod): 1.34, 1.37, 1.30, 1.19 -> NARROWS with reach; col/parton 1.81 -> 1.19. Under LW: Neel 1.38 -> 1.38 flat.
- NEW (CHECKED to 1e-15): the columnar VBS is an EXACT eigenstate of covariant rules: B4 at |d|^2 <= 4 (with star four-spin terms)
  and bilinear-only B at |d|^2 <= 12. Mechanism (EXACT algebra): singlet x singlet is annihilated by the inter-dimer coupling iff
  J11 + J22 = J12 + J21 for every dimer pair. So "near eigenstate" is cheap; the parton (0.0026) is LESS of an eigenstate than a VBS.
- fs0 is 10-30x worse than the parton: the search does discriminate pi-flux from 0-flux.
- Parton's best rules on refs (6^3): B4: lam'=0.1 0.0031, Neel 0.0041, col 0.0049, fs0 0.20, VBS 0.031.
- Energy contest (6^3) under the parton's B4_inner rule (J_NN=1, norm 4.61): parton -1.72680(12); lam'=0.1 +0.00014(20);
  Neel +0.00270(36) 7.5 sig; col +0.00389(30) 13 sig; fs0 +0.318; VBS +0.225. Same under B4 full (norm 4.65): +0.00005, +0.00258
  (7.9 sig), +0.00390 (13.2 sig), +0.315, +0.232.
- Cluster Casimirs: star (J1:J2:J002 = 2:2:1) lam 2.76 bilinear, 0.0052 with four-spin; cube 0.035 / 0.032. The best rule is NOT a
  cluster Casimir; describe it as AF J1 ~ J2 > J(0,0,2) + star four-spin, J(q) peaked at q=0 and flat over most of the zone.

## 7. CORRECTION on the VBS variance (estimator support condition)
- The VBS has structural zeros (dimer ferro configurations); h psi has weight there (T+T- dimer-pair excitations), so the local-
  estimator covariance misses part of the variance. For TWO-SPIN rules the missing part is exactly 2/3 of each dimer-pair
  excitation (EXACT: H^{AB}|ss> = (Delta_AB/4) D_A.D_B|ss>; T0T0 in support = 1/3 of the norm^2 48) -> lam_VMC = lam_true/3,
  so lam = 0 for bilinear rules is exact. With four-spin terms this proportionality is not established -> the B4 lam = 0 at
  |d|^2 <= 4 for the VBS is NOT claimed. VBS ENERGIES are exact estimators (psi* = 0 off support).
- Closed-form exact parent of the columnar VBS (dimer condition 2J(r) = J(r+e1) + J(r-e1), r1 even, r != 0), solved by hand:
  J = j (001,011,111), j/2 (002,012,112), j/4 (022,122), j/8 (222), 0 beyond: finite reach, cubic covariant (dual frame),
  valid on the infinite lattice. (vbs_check queued.)
- Parton / refs / fs0: generic projected determinants, no structural zeros found (A49: 300/300 and 120/120 random configs
  nonsingular) -> estimator valid (ARGUED).

## 8. VBS check + 16-site exact forward test (A49 fwd16 machinery, fwd16_51.py, 84 s)
- vbs_check (6^3): the |d|^2<=12 bilinear VBS minimizer IS the hand-derived rule (1,1,1,1/2,1/2,1/2,1/4,0,1/4,0,0,1/8);
  per-sample spread 0 -> exact eigenstate, E = -1.5 per site (intra-dimer -3 per dimer). Under that rule the PARTON has
  -1.50075/site (lam 0.027): the VBS is not clearly the calmest state of its own exact parent rule.
- 16-site cubic cluster (exact, S^z=0, 12870 states), short-reach rules found here (B4_r4 from 6^3 and 8^3, mapped to A49 basis;
  map check -3.030 vs -3.037):
    L6 rule, sign +1: E0/N -2.33458 (non-degenerate); parton <H>/N -1.77524, var/N 0.0355, overlap with GS 0.0002;
                      Neel .05 -1.77191, col .1 -1.76897.  sign -1: E0/N -13.06, parton +1.775.
    L8 rule, sign +1: E0/N -2.30279; parton -1.76626 (var/N 0.0417), overlap 0.0002; Neel -1.76290; col -1.75996.
  -> parton sits 0.54-0.56 per site (J_NN = 1 units; ~0.12 per unit norm) ABOVE the exact ground state, same as A49.

## 9. 8^3 references (1 batch each, ~3200 samples) + contest
- B4 mod at R^2 = 4 / 9 / 12 / 27 / full(34):
  parton 0.00292 / 0.00236 / 0.00219 / 0.00170 / 0.00154(11)
  Neel .05 0.00520 / 0.00391 / 0.00351 / 0.00259 / 0.00208(30);  col .1 0.00488 / 0.00413 / 0.00386 / 0.00250 / 0.00182(10)
  fs0 0.0863 / 0.0364 / 0.0304 / 0.0223 / 0.0197;  VBS (B4) 0 (not established, see sec 7), (B) exact 0 from R^2 = 12.
  Ratio Neel/parton 1.78 -> 1.35, col/parton 1.67 -> 1.18: gap NARROWS with reach. LW metric: parton 0.0059 -> 0.0054;
  Neel 0.0110 -> 0.0084 (1.86 -> 1.56); col 0.0101 -> 0.0072 (1.70 -> 1.34).
- Contest 8^3, parton's B4_inner rule (norm 4.794): parton -1.69469(11); Neel +0.00360(47) 7.6 sig; col +0.00471(39) 12.2 sig;
  fs0 +0.271; VBS +0.195.  B4 full (norm 5.764): Neel +0.00456(78) 5.9 sig, col +0.00451(36) 12.5 sig.
  6^3 inner rule mapped to 8^3: Neel +0.00303(46), col +0.00534(43).
  Margins (unit norm) Neel 0.00059 (6^3) -> 0.00075 (8^3); col 0.00084 -> 0.00098: do not shrink -> A45-style criterion MET
  against this competitor set; but 16-site exact GS is 0.12 per unit norm below the parton (sec 8): weak competitor set.

## 10. 10^3 incident (07:39-07:52)
- First two 10^3 batches (seeds 31, 32) hit signal.alarm(288) during thermalization (ntherm = nsw/20 = 1500 sweeps at ~0.5 s/sweep)
  and saved nothing (288 s, 504-558 MB each). Third (33) killed by hand at 127 s. Fix: time cap now also checked during
  thermalization; 10^3 jobs re-queued with NSWEEP = 2000 (ntherm 100 sweeps). Seeds 34-36, 39, 40 (parton), 37-38 (Neel .05).
- 6^3 B4_inner profile (finite reach, comps <= 2): 1, 0.775(9), (111) 0.057(25), (002) 0.370(14), (012) 0.026(9), (112) 0.023(11),
  (022) 0.005(10), (122) 0.001(10), (222) 0.001(6): effectively star-supported; long-range couplings consistent with 0.

## DRAFT report pieces (methods / open edges / plain language)
Methods:
- Frames as A49: operators in the soldered frame, state = projected pi-flux singlet in the Klein-dual frame (A44).
- Basis: O_c (dual s.s class sums, every class to L/2; 19/34/55 classes) + A49's 8 star four-spin terms (+2 plaquette in B4p).
- Estimator: rank-0 local estimators in S^z = 0 (exact: all operators are dual-SU(2) invariant, S^z conserving; parton is an exact
  singlet). Same estimator for refs (S^z = 0 states; S^z-conserving operators -> exact covariance on their support).
- C = Re Cov(E)/N; G = per-site HS Gram (diag 3 m_c/2 for classes; A49 G4 for four-spin). Metrics: G' (Casimir removed) and
  G_LW (Casimir + q-orbits with |q| <= pi/2 removed), minimisation over the quotient (Schur complement, releig_q).
- Errors: 16-block jackknife + bias correction. Energies: binning (A46 binerr).
- Forward: LT on the L-grid and on a 40^3 grid for finite-reach rules; LSWT single-Q with four-spin Hartree terms for collinear Q
  (exact at quadratic order); VMC contest; 16-site exact (A49 fwd16 machinery) for the |d|^2 <= 4 rules.
Open edges:
1. Long-range FOUR-spin terms (only star/plaquette four-spin used); full covariant weight-4/6 spaces (A49 edge 1).
2. A better competitor set at 6^3/8^3 (optimized projected states, DMRG/ED-quality ground states); 16-site exact only for |d|^2<=4 rules.
3. A size-independent "rule size" that penalises all-to-all couplings (energy-scale norm) instead of HS; the LW cut at pi/2 is a choice.
4. lam' != 0 beyond 0.1; lam' in the full operator space.
5. Whether the columnar VBS is the calmest state of its closed-form parent rule (the parton nearly ties it there: -1.5008 vs -1.5).

## 11. 10^3 (parton 3,259 samples / 5 batches; Neel .05 1,410 / 2 batches)
- A49 sets (plain): S1b-inv 0.0428(60), S1inv 0.00287(20), S1uS2inv 0.00265(20).
- B4 mod R^2 = 4 / 9 / 12 / 27 / 48 / full(55): parton 0.00286 / 0.00242 / 0.00225 / 0.00141 / 0.00092 / 0.00075(5) (bc 0.00082)
  Neel .05: 0.00443 / 0.00333 / 0.00293 / 0.00145 / 0.00072 / 0.00051(5) (bc 0.00056)  -> Neel BELOW parton at long reach.
  B4 LW: parton 0.0069 / 0.0066 / 0.0065 / 0.0064 / 0.0061 / 0.0061 (flat); Neel 0.0105 ... 0.0090 (ratio ~1.5 flat).
- q-orbit P_(001): lam 0.00098 vs Sbar^2 0.00119 (Sbar 0.0345). Sbar(2pi/L): 0.0854, 0.0518, 0.0345 (L = 6, 8, 10) ~ q^1.8.
  The full-reach B4 minimum (0.00075) is essentially this single long-wavelength mode.
- Fixed reach is L-independent: R^2<=4: 0.00319 / 0.00292 / 0.00286; R^2<=9: 0.00280 / 0.00236 / 0.00242; R^2<=12: 0.00275 /
  0.00219 / 0.00225 (L = 6 / 8 / 10).
- B4_inner (comps <= 4) profile at 10^3: smooth, all positive, 1, .84, .43(111), .53(002), .34, .31, .25, .21, ... ~0 at |d| ~ 5.7;
  exponential xi 1.09 (chi2 67) beats power law alpha 2.29 (chi2 223). The profile width tracks the available reach (star at 6^3,
  |d|~5.5 at 10^3): it approximates a small-q projector (LT: 47% of BZ within 1% of span, 92% within 5%).
- HS ansatz 10^3: af alpha=2: 0.0228 / 0.0114 (+4); alpha=1: 0.0049 / 0.0039. Cluster star Casimir 1.97 / 0.0047.
- Contest 10^3 (B4_inner, norm 5.789): parton -1.66264(14); Neel .05 +0.00374(45) (8.4 sigma).
- Parton best rule on Neel at 10^3: lam 0.00112 (vs parton 0.00075).

## 12. Final 8^3 pieces (08:27) and wrap-up
- lam'=0.1 at 8^3 (3,126 samples): B4 mod R^2<=4 0.00281, <=9 0.00236, full 0.00137(8); LW full 0.00497. Same as lam'=0 within error.
  Contest (B4_inner): lam'=0.1 -0.00008(22) vs parton (tie).
- 8^3 B4_inner profile (comps <= 3): 1, .807, .225, .412, .149, .128, .084, .062, .073, .050, .040, .043, .026, .022, .009, .008,
  .006, .000, -.001; all positive; exp xi 0.63 (chi2 565) vs power alpha 3.4 (chi2 837): neither fits; width tracks reach.
- GAUGE CAVEAT: full-reach rules are defined modulo the Casimir; for non-singlet refs both the variance and the energy depend on
  the Casimir admixture mu (energy shift 2 mu <S^2>/N, ~0.006 per unit mu at 6^3 for Neel) -> use finite-reach (inner) rules for
  "parton rule on refs" and for the contest. The full-reach "parton rule on refs" numbers (e.g. 8^3 Neel 0.016) are not reported.
- Queue stopped 08:28; NUMLOCK free; 66 run.sh invocations in chain.log, 4 SKIPPED (lock held by my own orphan job, 06:40-06:44),
  none for load or memory. Max runtime 288 s (two alarm-killed 10^3 batches), max peak RSS 638 MB (basis51).
