# Novelty of today's strong-coupling results (FINISH row 819), by Claude Opus 5.5 (max effort)

- Clone: `/Users/jonreilly/ym4d-lead/clone`, commit `0ed7f11bec5fb3f5cdda187f9d3bb63e4e427b76`.
- Main (for PV): `origin/main` = `bb4ec020d5ada57c630dd89acc98a68397ade423`.
- Lane directory D = `.claude/science/physics-loops/ym4d-hard-route-20261030`.
- Read in full: `D/library/gap-vmf-lip.md`, `D/library/gap-vmf-lip-check-opus.md`,
  `D/library/gap-gamma2-astra.md`, `D/library/gap-gamma2-check-opus.md`,
  `D/library/gap-tu-retry.md`, `D/library/gap-tu-check-opus.md`,
  `D/library/prior/gap-lit-gamma2.md`, `D/library/prior/gap-lit-vmf-tor.md`,
  and main's `docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md` (PV).
  `D/library/prior/gap-lit-u1.md` was searched as a pointer only.
- This is a reading and comparison. It is not a proof check and not an audit. No repository file was edited.
- The Codex digests were starting points. Every literature claim below rests on a primary text I read, unless it is marked "not read".

## 0. Headline

The most important finding is a recent unrefereed preprint. Deep Bhattacharjee and Ushashi Bhattacharya,
"Mass Gap of Lattice Yang-Mills Theory up to the Dobrushin Ceiling", is dated 18 October 2026. It is on
Zenodo, DOI 10.5281/zenodo.23449466, version 2.0.0, published 18 October 2026 (record metadata). Its abstract
claims the sharp quarter, W1(nu_b, nu_b') <= |b - b'|/4 for von Mises-Fisher laws on S^3 in the chordal metric.
It also claims uniqueness, decay and a transfer-matrix gap for 4D SU(2) up to beta_W = 2/9. It calls 2/9
"the ceiling of all single-link Dobrushin arguments". These are the lane's Theorem V (bound 1/4), its chord
Lemma INF, and its threshold 2/9. A later version (v3.2.0, 20 October 2026, as cited by Mihajlovic,
arXiv:2611.11534 p. 8) adds a forest gauge with beta_W < 1/3. A related record, "Yang-Mills Theory and the
Mass Gap" v4.47.1 (Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford, Singha Roy; Zenodo
10.5281/zenodo.24117822, 10 November 2026), states the forest-gauge result as Theorem A: SU(2) gap for
|beta_W| < 1/3 with m >= -log(3 beta_W). I did not check any of their proofs. I did not check whether either
project used the other's text.

The same group's Hexagon preprint 2610.00341 (section 8, added at the coordinator's request) has seven
versions, 18 October to 6 November 2026. Its v4 (30 October) and v7 (6 November) cite the quarter and the
single-link range 2/9 from the 18 October paper. They state the forest-gauge range 1/3 and plaquette blocks to
beta_W = 0.345 (v4) and 0.348 (v7). v7 also states a torus-uniform Poincare inequality for a cube-resampling
chain at |beta_W| < 2/9. Every version predates the lane's 2026-11-12 notes.

## 1. Normalizations

All thresholds below are converted to the lane's coupling. The lane's Wilson weight is exp(beta tr(U_p)/2)
per plaquette, that is exp(beta x_p) with x_p = tr(U_p)/2 = Re of the unit quaternion U_p. The action is
beta sum_p (1 - x_p). This is the physics Wilson coupling for SU(2): S = beta_W sum_p (1 - (1/N) Re Tr U_p)
with beta_W = 2N/g^2 = 4/g^2. So **beta_lane = beta_W**.

| Convention | Weight per plaquette, SU(2) | Conversion |
|---|---|---|
| Lane, physics Wilson | exp(beta_W tr(U_p)/2) = exp(beta_W x_p) | identity |
| 't Hooft (SZZ, CNS, Bhattacharjee-Bhattacharya) | exp(N beta Re Tr U_p) = exp(4 beta x_p) | beta_W = N^2 beta = 4 beta (BB footnote 4 says the same) |
| beta/N | exp((beta/N) Re Tr U_p) = exp(beta x_p) | beta_W = beta |
| beta/(2N) with Tr(U_p + U_p^dagger) | equals (beta/N) Re Tr U_p | beta_W = beta |
| beta/(2N) with Re Tr U_p only | exp((beta/4) 2 x_p) | beta_W = beta/2 |

Metrics on SU(2) = S^3. "Unit" means the round metric of the unit sphere in R^4 (quaternion norm). SZZ use
<X,Y> = Re Tr(XY*) (arXiv:2204.12737v1, (2.3), p. 10). For SU(2) this is 2 times the unit metric. Ricci is
2 g_unit = 1 g_SZZ (SZZ (4.8), p. 19: (alpha(N+2)/4 - 1) with alpha = 2). Spectral gaps scale inversely with
the metric: lambda_SZZ = lambda_unit/2. The lane's `gap-ac-lat.md` metric is 4 g_unit (gamma2 check, item 1).

Chord versus geodesic metric for W1. The chord metric is |x - x'| in R^4. The lane and Bhattacharjee-Bhattacharya
use the chord metric. Wu 2006 also uses it ("Euclidean metric d_E", Prop. 5.5). Royer 1986 uses the geodesic
metric. Chord-1-Lipschitz implies geodesic-1-Lipschitz. BB footnote 14 (p. 9) shows the quarter fails in the
geodesic metric.

Slab (layer) sigma model. Conditioning on the horizontal links of a height-1 slab gives a 3D sigma model on
the vertical links. Its bond weight is exp(N beta Re Tr(Q_x A Q_y^-1 B^-1)) (CNS arXiv:2509.04688v2,
Definition 2.1, p. 3). For SU(2) this is exp(beta_W x_b). So the lane's layer coupling (gap-vmf-lip
section 3, y_b = h_x . O_b h_y) equals beta_W.

Villain U(1). The lane's phi_beta(t) = sum_n exp(-n^2/(2 beta)) e^{int} is, by Poisson summation, proportional
to sum_m exp(-beta (t + 2 pi m)^2 / 2). This is the standard Villain weight at coupling beta. I could not read
FS82 or Guth to confirm their conventions.

Converted thresholds (sufficient conditions only, not transition points):

| Source | Stated | beta_W |
|---|---|---|
| SZZ 2022/23, SU(N) Bakry-Emery (Assumption 1.1, p. 4) | abs(beta) < 1/(16(d-1)) | 1/12 = 0.0833 |
| BB 18 Oct 2026, sharp Hessian 4d (abstract, Theorem B) | abs(beta) < 1/(8d) | 1/8 = 0.125 |
| CNS 2509.04688, area law via slab Bakry-Emery (Def. 1.4, Thm 1.6) | beta < 1/(8(d-1)) | 1/6 = 0.1667 |
| Lane / BB 18 Oct 2026, single-link chord Dobrushin | abs(beta) < 1/(6(d-1)) | 2/9 = 0.2222 |
| BB 20 Oct / 10 Nov 2026, forest gauge (Theorem A); Hexagon v4 30 Oct, v7 6 Nov, Theorem 1 | 3 beta_W < 1 | 1/3 = 0.333 |
| Hexagon 2610.00341 v4 / v7, plaquette blocks (Theorem 3) | alpha(beta_W) < 1 | 0.345 (v4), 0.348 (v7) |
| Hexagon v4 / v7, Bakry-Emery in the forest gauge (Theorem 4, Corollary 23) | abs(beta) < 1/29 | 4/29 = 0.138 |
| Hexagon v7, cube-resampling Poincare (Corollary 74(i)) | abs(beta_W) < 2/9, alpha_n < 1 | 2/9 (block chain, not Langevin) |
| BBLR+ 10 Nov 2026, cube-resampling gap by "stars" (release notes) | beta_W = 7/20 | 0.35 (different object) |
| Lane (AS-bg), slab sigma model | 3 beta/2 < 1 | 2/3 = 0.667 (layer model, not the 4D measure) |

## 2. Result 1: gap-vmf-lip.md

### 2.1 Theorem V (single-site vMF bound)

Lane statement (lines 59-77). For mu_F proportional to exp(F.h) on S^3, every unit e and every
chord-1-Lipschitz phi: abs(Cov(phi, h.e)) <= a(abs(F)) <= 1/4, with a(k) = z'(k)/(k z(k)) = E_F h_v^2 for
v orthogonal to F. The supremum over e and phi equals a(abs(F)). Corollary V1: W1_chord(mu_F, mu_F') <= abs(F - F')/4.
The proof (lines 80-190) builds a divergence-free field in the ball. The Opus check
(`gap-vmf-lip-check-opus.md` section 1) re-derived it and found it holds.

Comparison.
- The variance part, a(k) = E h_v^2 <= 1/4, is the Dyson-Lieb-Simon bound var(x.sigma) <= 1/n for O(n) spins.
  Bauerschmidt-Bodineau (arXiv:1712.03676v2, p. 2) and Royer 1986 (Theorem 1.3, p. 31) both use it.
  **EQUAL** to a known result (DLS 1978, Theorem D.2 as cited; DLS itself not read).
- The uniform bound W1 <= abs(b - b')/4, chord metric, constant attained at b = 0: Bhattacharjee-Bhattacharya,
  "Dobrushin Ceiling", Theorem 7 "The sharp quarter" (p. 9). Their L(c,h) <= 1/4 holds for every c in R^4 and
  unit h. Their proof uses a harmonic extension, a Dirichlet-to-Neumann norm, Bessel series and a case split
  at kappa = sqrt(88)/3 (Lemmas 8-9, Propositions 11-12, pp. 9-12). **EQUAL** to this unrefereed claim.
- The field-dependent sharp form, sup over e and phi = a(abs(F)) for every F: the BB v4.47.1 appendix
  (`detailed/app/C_sharp.tex` lines 132-134) computes L(c,h) = A(kappa)/kappa only for h orthogonal to c.
  It bounds the general case by 1/4. I found no source that bounds every direction by a(abs(F)).
  **NEW** relative to all sources read. The proof route is also different and shorter.
- Older Dobrushin work on N-vector models gets weaker constants. Royer 1986 (Ann. IHP A 44, 29-38, abstract
  p. 29) obtains J_c >= (N(N-3))^{1/2} by Dobrushin, that is 2 for N = 4, and about 2.25 by a second method
  (table, p. 38). He notes the mean-field value J_c >= N (Simon) as the target he cannot reach. Wu 2006
  (Ann. Probab. 34, Prop. 5.5, p. 23) bounds the chord coefficient by |J| sigma_E/sqrt(p+1) through
  Cauchy-Schwarz. Dorlas-Savoie (arXiv:2305.19371v4, Prop. 6.1, p. 21) get beta < (24 d J)^-1 for Heisenberg.
  Le-Lewis-Bharath-Fallaize (arXiv:2003.11497v3, Example 2(i), pp. 17-18) bound W1 between vMF laws only
  under a curvature restriction and with extra factors. Levin 1980 (CMP 78, 65-74) gives a weaker bound per
  Royer (p. 30); not read. Theorem V reaches the mean-field value N = 4 by Dobrushin for O(4) with arbitrary
  signed couplings. Relative to the refereed literature this is **NEW**. Relative to BB 18 Oct 2026 it is EQUAL
  at the level of the uniform 1/4.

### 2.2 The 4D seed and lattice gap (Theorem DOB chord form, (17)-(21))

Lane statement. For 0 < beta_W < 2/9, q = 9 beta/2: Lemma INF chord form gives row sum alpha <= 9 beta/2
(line 324). Theorem DOB gives S(a;(2a)^3;beta) < 1/1650 for suitable a, and m(L^3;beta) >= 3/(50a) for all
L >= 64a on periodic spatial cubes, with all electric-flux sectors (lines 438-466). Example: beta = 1/9,
a = 96, m >= 1/1600 for L >= 6144 (lines 584-593). The gap uses inherited in-lane results (TM), Identity FL,
Lemma M and the corrected Theorem SH. These are not literature results.

Comparison.
- Refereed: SZZ 2022 (CMP 400, 2023) proves uniqueness, LSI, Poincare and exponential decay for
  beta_W < 1/12 (Assumption 1.1 p. 4; Theorem 1.4 p. 6; Corollary 1.6 p. 7). SZZ write that a Dobrushin
  uniqueness argument with a Wasserstein metric "has not been carried out in detail for lattice Yang Mills"
  (p. 6). SZZ's YMH paper (arXiv:2401.13299v3, (BE-YM) p. 4) keeps the same pure-gauge condition. CNS
  (arXiv:2509.04688v2) prove area law, not a 4D gap, for beta_W < 1/6. CNS (arXiv:2505.16585v3, p. 1-3)
  describe Osterwalder-Seiler as beta <= c(d)/N with a small unspecified c(d). Chatterjee
  (arXiv:1502.07719, Theorem 3.1) needs abs(beta) <= beta_0(d), existential, for SO(N) at large N.
  OS78 and Seiler 1982: not read (paywalled); SZZ (p. 2) describe them as convergent cluster expansions for
  sufficiently strong coupling, with no explicit threshold. Relative to refereed work, beta_W < 2/9 is **NEW**.
- Unrefereed: BB 18 Oct 2026, Theorem E (p. 2): uniqueness for abs(beta) < 1/(6(d-1)), that is beta_W < 2/9,
  and decay at every rate below -log(6(d-1) abs(beta)). Theorem F (pp. 2-3): the infinite-volume transfer
  matrix has gap m = -log(9 beta_W/2). Proposition 13 (p. 12): no single-link chordal or geodesic
  Wasserstein-Dobrushin argument passes 2/9. The range is **EQUAL**. The lane's gap size is **WEAKER**: at
  beta_W = 1/9 the lane gives 1/1600, BB give log 2 = 0.693. The forest-gauge range 1/3 (v3.2.0, 20 Oct;
  Hexagon 2610.00341 v4, 30 Oct, Theorem 1; v4.47.1 Theorem A) and the plaquette-block range 0.345 (Hexagon
  v4 Theorem 3) or 0.348 (v7 Theorem 3) are larger, so the lane's range is **WEAKER** than those claims.
- Form. BB's Theorem F is an infinite-volume statement. Their Proposition 22 (p. 16) gives only a
  non-uniform finite-volume gap, and Proposition 24 (p. 17) is conditional on inf_L Delta_L > 0. The lane's
  (21) is uniform over finite periodic spatial cubes and includes every flux sector. I found no source that
  states this form at beta_W < 2/9. **NEW in form**, but it follows from the same Dobrushin condition and
  its constant is far from what that condition gives.
- Lemma DC (chord Dobrushin comparison with averaged updates) is the classical comparison theorem in
  Wasserstein form. BB's Appendix D and Mihajlovic's Lemma SC.3 state versions. **EQUAL** to known.

### 2.3 (AS-bg): background-uniform layer twist for beta < 2/3

Lane statement (lines 352-417). For the 3D O(4) layer model with arbitrary orthogonal bond backgrounds and
coefficients in [-1, 1], Lemma INF gives alpha <= 3 beta/2 and the twist bound (14) holds for beta < 2/3,
uniform in background and box.

Comparison.
- CNS 2509.04688v2, Proposition 3.2 (pp. 4-5): uniform covariance decay for the same slab sigma model by
  Bakry-Emery, K = (N+2)/2 - 1 - 4N beta (d-1), that is beta_W < 1/6 for SU(2), d = 4.
- Bauerschmidt-Bodineau 2019 (Theorem 1 and remark, pp. 1-2): LSI for O(n) when the coupling spectrum spread
  lambda_+ - lambda_- < n. They state it for scalar couplings M_xy. For the trivial background on Z^3 the
  spread is 12 beta, so beta < 1/3. Extending to orthogonal bond matrices is not stated there.
- Aizenman-Simon 1980 (ferromagnets only) give the mean-field range, which is 2/3 here for the trivial
  background. Not read (Project Euclid blocked automated access); per the Codex digest.
- BB 2026 materials: I found no slab or layer sigma-model statement (searches of the 18 Oct PDF and the
  v4.47.1 sources for slab, layer, sigma model, Durhuus).
- Verdict: **NEW** as a stated result. It is a three-line corollary of the public sharp quarter (BB Theorem 7)
  plus Dobrushin's theorem.
- Consequence not stated by the lane or by any source found, and not verified here. CNS Theorem 2.3
  (Durhuus-Frohlich 1980, Theorems 1.2-1.3, pp. 3-4) derives area law from slab-sigma-model covariance decay
  that is uniform in the boundary fields A, B. The uniform Dobrushin condition alpha = 3 beta_W/2 < 1 gives
  such decay. So area law for 4D SU(2) Wilson theory for beta_W < 2/3 appears to follow. That would be four
  times CNS's 1/6. This needs a check of DF80's exact hypotheses before anyone relies on it.

### 2.4 Verdict for result 1

Theorem V: NEW in its sharp field-dependent form and proof; the uniform 1/4 is EQUAL to BB 18 Oct 2026,
Theorem 7 (unrefereed); the variance part is EQUAL to DLS. 4D seed and gap: the range 2/9 is EQUAL to BB
18 Oct 2026 (unrefereed) and NEW relative to refereed work (SZZ 1/12); the gap constant is WEAKER than BB's
Theorem F; the range is WEAKER than BB's forest-gauge 1/3 and Hexagon's plaquette blocks 0.345-0.348; the
finite-cube, all-flux, uniform-in-L form is NEW. (AS-bg) for beta < 2/3: NEW (closest: CNS Bakry-Emery 1/6).

## 3. Result 2: gap-gamma2-astra.md

Lane statement. (15): E(f) >= (2 - 9 beta) Var(f) for every f, every beta < 2/9, unit metric, all periodic
tori, center twists allowed. Section 2: (G2) holds with volume-uniform constants if and only if a
volume-uniform invariant gap holds, via (3) and the Hessian bound (7). Section 4: sphere Lemma L, gap
implies exponential covariance decay. Section 5: (23) pointwise Bakry-Emery fails for beta > 1/8; (24)
single-link chord Dobrushin cannot pass 2/9. The Opus check found every item holds.

Conversions. SZZ's Poincare constant K_S = 1 - 48 beta_SZZ in g_SZZ gives the unit-metric gap 2 - 24 beta_W
for beta_W < 1/12 (SZZ Theorem 1.4 p. 6, Lemma 4.1 p. 17, (4.8) p. 19). BB's sharp Hessian 4d gives the
unit-metric Bakry-Emery gap 2 - 16 beta_W for beta_W < 1/8. The lane's 2 - 9 beta_W equals 1 - 18 beta_SZZ in
SZZ's metric.

Comparison.
- Mechanism. Wu 2006 (Ann. Probab. 34, 1960-1989; arXiv:math/0611635) Theorem 2.1 (p. 5) gives the Glauber
  gap 1 - r_sp(C) under Dobrushin's condition. Theorem 2.2 (p. 6) gives the Poincare constant
  lambda_0 (1 - r_sp(C)) with lambda_0 the uniform conditional gap. The lane's (14)-(15) are exactly this,
  with lambda_0 = 2 from its (10) and r_sp(C) <= 9 beta/2 from Theorem V. **EQUAL** to Wu's theorem as a method.
- Statement. SZZ stop at 1/12. BB 18 Oct 2026 prove Bakry-Emery LSI and Poincare to 1/8 (Theorems B, D) and
  Dobrushin uniqueness to 2/9 (Theorem E). Their footnote 30 (p. 19) calls the Dobrushin-to-Poincare step
  classical and cites Wu. I found no statement of a Langevin Poincare inequality beyond 1/8 in their text.
- Hexagon 2610.00341 (section 8). v4 and v7, Corollary 23, give a Bakry-Emery Poincare inequality for the
  forest-gauge-fixed box measure with K = kappa_G - (29/2) N abs(beta); for SU(2) this is unit gap
  2 - 14.5 beta_W for beta_W < 4/29. v7 (dated 4 Nov, posted 6 Nov 2026), Corollary 74(i) (pp. 42-43), states a
  Poincare inequality BP(n, 1 - alpha_n), uniform over even tori L >= 2n + 4, for every real f, for SU(2) with
  abs(beta_W) < 2/9 and alpha_n = abs(beta_W)(18n - 3)/((4 - 18 abs(beta_W)) n^2) < 1. Its generator resamples cubes of
  side n >= 2; it is not the single-link Langevin diffusion. Its mechanism is the same: single-link Kantorovich
  coefficients abs(beta) = beta_W/4 with 18 partners, turned into a spectral gap (v7 Theorem 125).
- So the lane's statement is **NEW** only as the Langevin (single-link diffusion) version with the explicit
  unit-metric constant 2 - 9 beta_W. The threshold 2/9 and the Dobrushin-to-Poincare mechanism on tori are
  **EQUAL** to Hexagon v7 Corollary 74(i) for a different local dynamics.
- Constant. BB's Lemma 4 (p. 7) claims the vMF Poincare constant 1/3 for every field, that is conditional gap
  3. With Wu's Theorem 2.2 this would give 3 (1 - 9 beta_W/2), which beats the lane's 2 - 9 beta_W on the
  whole range. That combination is not stated by BB. The lane's constant is **WEAKER** than what public
  ingredients give.
- The lane's direct bound (11), gap >= 2 - 18 beta_W for beta_W < 1/9, is WEAKER than BB's pointwise 2 - 16
  beta_W on that range (if BB's sharp Hessian holds).
- (G2) equivalence. The integrated identity int Gamma_2 = int (Lf)^2 is classical (Bakry-Gentil-Ledoux 2014,
  cited by the Codex digest; not reread). The lane adds one convex-combination step. **EQUAL** in substance.
- Lemma L. Gap implies exponential decay through commutator bounds and a semigroup interpolation. SZZ use it
  (Corollary 1.6 p. 7, Corollary 4.11). SZZ's YMH paper (p. 5) traces it to Guionnet-Zegarlinski 2003,
  section 8.3. **EQUAL** to known technique.
- (23) and (24). BB claim the sharp Hessian bound 4d, so Bakry-Emery stops exactly at beta_W = 1/8; the
  lane's (23) is the lower-bound half. BB Proposition 13 states the 2/9 ceiling for chordal and geodesic
  metrics; the lane's (24) states it for the chord metric. **EQUAL** to BB 18 Oct 2026.

Verdict for result 2: the uniform Langevin Poincare gap for beta_W < 2/9 is NEW only as the single-link
diffusion version. It is Wu's Theorem 2.2 applied to the public sharp quarter. The range and mechanism are
EQUAL to Hexagon v7 Corollary 74(i) for a cube-resampling chain. Its constant is WEAKER than BB's Lemma 4
(Hexagon v4 Lemma 122) plus Wu would give. The equivalence with integrated Bakry-Emery and Lemma L are
EQUAL to known results.

## 4. Result 3: gap-tu-retry.md

Lane statement. Theorem V (U-tor): for periodic Villain U(1) on (Z/M)^4, M >= 4 including odd M, at fixed
beta >= 2^14, the gauge-invariant Langevin gap gamma_V(beta; M) tends to 0 (lines 92-101). The proof extends
PV's coset estimate to odd M (108 colours, exponent 1/1296), passes to continuous Haar links, proves
non-summable score correlations in every periodic local limit, and uses Lemma L. Section 3 gives a
fixed-action counterexample to the lane's (TU) continuation. The Opus check found every step holds.

Comparison.
- Static masslessness. FS82 (CMP 83, 411-454) and Guth 1980 (PRD 21, 2291-2307): not read. The IHES preprint
  host did not resolve; Project Euclid blocked automated access; APS and Springer are paywalled. Secondary
  statements: SZZ YMH (p. 9) say Guth and FS82 proved a massless phase for sufficiently large beta. CNS
  2505.16585 (p. 1) say FS82 showed no area law for 4D U(1) at large beta. The Codex digest `gap-lit-u1.md`
  reports fixed boundary links, an infinite-volume conclusion and the existential condition beta > 108 beta_1
  for Villain. Guth's abstract reportedly gives g^2 < 0.168. The lane's periodic statement for every M and
  every periodic local limit differs from that setting. It rests on PV, a repository note, not on literature.
- Dynamics. I found no published theorem on Langevin or Glauber gaps of 4D U(1) (web search; SZZ YMH treats
  only strong coupling). Two unrefereed 2026 texts come close. BB 18 Oct 2026, Section VII-B (p. 17), asserts
  inf_L Delta_L = 0 for the transfer matrix of 4D U(1) at large beta, from FS82 and their Proposition 23. The
  sentence does not address that FS82's state comes from fixed boundary links, not from periodic limits.
  BBLR+ v4.47.1, `detailed/sec/11_weak.tex` item (c), says their cube-resampling condition fails for Villain
  U(1) at large beta, again from FS82. Neither concerns the Langevin generator.
- Lemma L is EQUAL to known technique (section 3 above).
- Threshold. beta >= 2^14 = 16384 is far larger than PV's beta >= 2000 (even M, finite clock) and than the
  reported existential FS and Guth conditions. As a coupling range it is WEAKER than the static results, but
  those are different statements.

Verdict for result 3: **NEW** as stated (Langevin dynamics, every periodic torus, full limit). The ingredients
are known: FS-type masslessness (made periodic in PV) and the standard gap-implies-decay bridge. The
closest public analogues are the unrefereed BB transfer-matrix remark and the BBLR+ cube-condition failure.

## 5. Comparison table

| Lane result | Lane range (beta_W) | Best refereed comparison | Best unrefereed public comparison | Verdict |
|---|---|---|---|---|
| Theorem V, sup = a(abs(F)) <= 1/4, chord | all F | DLS var <= 1/n (variance part); Royer 1986: J_c >= 2 for N = 4; Wu 2006 Prop. 5.5 (Cauchy-Schwarz) | BB 18 Oct 2026 Thm 7: L(c,h) <= 1/4 for all c, h | uniform 1/4: EQUAL (BB); field-dependent sharp form and proof: NEW |
| 4D chord Dobrushin, seed, m(L^3) >= 3/(50a) | 0 < beta_W < 2/9 | SZZ 2023: 1/12 (gap, LSI); CNS 2509: 1/6 (area law); OS78: existential | BB 18 Oct: 2/9, m = -log(9 beta_W/2) (infinite volume); BB 20 Oct, Hexagon v4 30 Oct, v7 6 Nov: 1/3 forest gauge (m >= -log 3 beta_W); Hexagon plaquette blocks to 0.345 / 0.348 | range: EQUAL to BB 18 Oct, WEAKER than 1/3 and 0.348; gap size: WEAKER; finite-cube all-flux form: NEW; vs refereed: NEW |
| (AS-bg) layer twist | beta_W < 2/3 (slab sigma model) | CNS 2509 Prop 3.2: 1/6; BB19 spectral: 1/3 (scalar couplings); Aizenman-Simon 2/3 (ferromagnet only) | none found | NEW (corollary of BB Thm 7 + Dobrushin) |
| Langevin Poincare gap >= 2 - 9 beta_W, all f | beta_W < 2/9 | SZZ: 2 - 24 beta_W, beta_W < 1/12; Wu 2006 Thm 2.2 (method) | BB: Bakry-Emery 2 - 16 beta_W to 1/8; Hexagon v4/v7 Cor 23: gauge-fixed 2 - 14.5 beta_W to 4/29; Hexagon v7 Cor 74(i): cube-chain Poincare to 2/9 on tori; BB Lemma 4 + Wu would give 3 - 27 beta_W/2 (not stated) | NEW only as the single-link Langevin version; range and mechanism EQUAL to Hexagon v7 Cor 74(i); constant WEAKER than public ingredients give |
| (G2) <=> uniform gap | compact intervals | integrated Gamma_2 identity (BGL 2014) | - | EQUAL in substance |
| Sphere Lemma L | given a gap | SZZ Cor 1.6 / 4.11; GZ03 sec. 8.3 | - | EQUAL (known technique) |
| (23), (24) | 1/8, 2/9 | - | BB sharp Hessian 4d; BB Prop 13 ceiling | EQUAL (BB) |
| Villain U(1) Langevin gap -> 0 | beta >= 2^14 | FS82, Guth 1980 (static; not read) | BB Sec. VII-B (transfer matrix); BBLR+ sec. 11(c) (cube condition) | NEW as stated; ingredients known; range WEAKER than static results |

## 6. Assumptions of the comparison

1. beta_lane = beta_W, and 't Hooft beta = beta_W/4 for SU(2) (section 1). BB state beta_W = N^2 beta in their
   footnote 4, which agrees.
2. Gap comparisons use the unit round metric on each S^3 and the generator L = -Delta + grad S . grad.
   SZZ's metric is twice the unit metric, so their K_S converts to 2 K_S.
3. W1 comparisons use the chord metric. Royer's geodesic results are compared only through the uniqueness
   threshold J_c, which does not depend on the metric choice.
4. "Range" means a sufficient condition proved by the source, not a transition point.
5. Unrefereed preprints are treated as public claims. I read their statements, not their proofs. Dates come
   from the documents and Zenodo metadata: BB "Dobrushin Ceiling" dated 18 Oct 2026 (Zenodo v2.0.0, 18 Oct
   2026); its v3.2.0 dated 20 Oct 2026 per Mihajlovic's reference [5]; BBLR+ v4.47.1 dated 10 Nov 2026;
   Hexagon 2610.00341 v1-v7 posted 18 Oct to 6 Nov 2026 per its version history.
   Zenodo metadata can be edited after publication; I did not check edit history.
6. Not read in primary form: Osterwalder-Seiler 1978, Seiler 1982 (paywalled); FS82 (IHES host did not
   resolve; Project Euclid blocked); Guth 1980 (paywalled); Driver 1987 (Project Euclid blocked); Levin 1980,
   Aizenman-Simon 1980 (Project Euclid blocked); Simon 1980 J. Stat. Phys. (Springer sign-in redirect;
   stopped). I found no open Dobrushin-uniqueness paper for lattice gauge theory by Borgs or by
   Brydges-Frohlich-Seiler; SZZ (p. 6) say none existed in detail as of 2022. Their characterizations above
   come from the secondary statements cited.
7. The search was bounded (web search plus targeted reading). It is not an absence theorem.
8. The lane's 4D gap (21) also depends on in-lane inherited results (TM, Identity FL, Lemma M, Theorem SH).
   I did not re-derive them.

## 7. Primary sources read, with locations

Downloads sit in fresh directories under
`/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/novelty-dl/`.
Text was extracted with a PDFKit tool kept in a separate directory (`.../scratchpad/novelty-tools/`).

- Shen-Zhu-Zhu, arXiv:2204.12737v1 (CMP 400, 2023): pp. 2, 4, 6, 7, 10, 17, 19.
- Shen-Zhu-Zhu, arXiv:2401.13299v3 (YMH): pp. 4, 5, 7, 9, 28-29.
- Cao-Nissim-Sheffield, arXiv:2509.04688v2: pp. 1-6. Cao-Nissim-Sheffield, arXiv:2505.16585v3: pp. 1-3.
- Chatterjee, arXiv:1502.07719: Theorem 3.1.
- Wu, arXiv:math/0611635 (Ann. Probab. 34, 2006): Theorems 2.1-2.2, Example 5.3, Lemma 5.4, Prop. 5.5.
- Royer, Ann. IHP A 44 (1986) 29-38 (NUMDAM open archive): full text.
- Dorlas-Savoie, arXiv:2305.19371v4: Section 6.1, Remark 6.2.
- Bauerschmidt-Bodineau, arXiv:1712.03676v2 (JFA 276, 2019): pp. 1-3.
- Le-Lewis-Bharath-Fallaize, arXiv:2003.11497v3: Example 1(i), Section 5.1, Example 2(i).
- Bhattacharjee-Bhattacharya, "Mass Gap of Lattice Yang-Mills Theory up to the Dobrushin Ceiling" (PDF in
  the Zenodo 24117822 archive, dated 18 Oct 2026; record 23449466 metadata): abstract, pp. 2-3, Lemma 4,
  Theorem 7, Proposition 13, Section VII.
- Bhattacharjee et al., Zenodo 24117822 v4.47.1 archive: RELEASE-NOTES, `detailed/sec/01_intro.tex`,
  `detailed/app/C_sharp.tex`, `detailed/sec/11_weak.tex`, `YangMills/StrongCoupling/Thresholds.lean`
  (read as text; nothing was executed).
- Mihajlovic, arXiv:2611.11534v1: abstract, section 1.2 (p. 8), reference [5].
- Faizal-Shabir, arXiv:2606.19362v1: abstract only; it claims a uniform gap via polymer expansions with no
  explicit SU(2) threshold found in the abstract. Not used.
- Hexagon 2610.00341: v4 PDF (https://hexagonmath.org/pdf/2610.00341v4, 70 pages, dated 30 October 2026),
  v7 landing page (https://hexagonmath.org/2610.00341v7, version history) and v7 PDF
  (https://hexagonmath.org/pdf/2610.00341v7, 385 pages, dated 4 November 2026). Each was fetched once into
  its own new directory and read as text (section 8).

## 8. Hexagon 2610.00341 (added at the coordinator's request)

Source. Deep Bhattacharjee, Ushashi Bhattacharya and James Montgomery Lockwood (v4); Tristan Romanov joins
in v7. Non-refereed platform preprint, CC BY 4.0, no arXiv identifier. The v7 landing page lists the history:
v1 18 Oct 2026 (29 pp.), v2 22 Oct (28 pp.), v3 28 Oct (54 pp.), v4 30 Oct (70 pp.), v5 31 Oct (150 pp.),
v6 2 Nov (105 pp.), v7 6 Nov (385 pp., current). v4 is titled "Mass Gap of Four-Dimensional Lattice
Yang-Mills Theory for Every Compact Simple Group" (PDF dated 30 October 2026). v7 is retitled "One Cube
Estimate Implies the Yang-Mills Mass Gap" (PDF dated 4 November 2026). The v7 provenance statement says the
authors worked with AI agents, including Claude Opus 5.5, and that every constant is now proved by hand.
I did not fetch v1-v3, v5 or v6. All versions are earlier than the lane's 2026-11-12 results.

What it says about item 1 (the beta_W < 2/9 seed and gap).
- Single-link route. v4 p. 2 and v7 p. 1: the SU(2) one-link law is von Mises-Fisher, "the sharp Kantorovich
  modulus of that family is one quarter", every link has eighteen partners, "which gives beta_W < 2/9 and
  nothing beyond, because the coefficients are attained". Both attribute this to their earlier paper ([14] in
  v4, [20] in v7), the Zenodo "Dobrushin Ceiling" paper of 18 October 2026. The quarter is restated as
  Theorem 125 (v4, Appendix I) and Theorem 682 (v7, Appendix K): L(c,h) <= 1/4 for all c, h, equality at
  c = 0, W1(nu_b, nu_b') <= abs(b - b')/4, constant best possible. No field-dependent bound a(abs(F)) appears in the
  v4 statement.
- Forest gauge. Theorem 1 (v4 and v7, p. 2): a field of straight lines fixes one link in every plaquette, so
  each free link has twelve partners. For 0 <= beta_W < 1/3: free-boundary box limits converge to a unique
  state on gauge-invariant observables, invariant and reflection positive; truncated correlations of Lipschitz
  observables decay at every rate below -log(3 beta_W); the transfer matrix has gap m >= -log(3 beta_W).
  Theorem 2: no single-link Kantorovich argument in a forest gauge reaches 1/3.
- Plaquette blocks (Dobrushin-Shlosman type, three-link blocks, ten outside partners). Theorem 3: v4 to
  beta_W <= 0.345 with alpha(0.345) <= 0.9973; v7 to beta_W <= 0.348 with alpha(0.348) <= 0.9936; gap
  m >= -(1/2) log alpha(beta_W), for example m >= 0.0224 (v4) or 0.0279 (v7) at beta_W = 1/3.
- Form. These gaps concern the free-boundary infinite-volume state. v4 footnote 10 notes that on a torus the
  line field closes into cycles. I found no statement of a gap uniform over finite periodic spatial tori with
  all flux sectors (searches of v4 and v7 for flux, twist sector, spatial torus, uniform in L). v7
  Theorem 252 treats a spatial torus at weak coupling (beta_W >= 1), not this.
- Effect on the verdict. The lane's range 2/9 is EQUAL to the cited 18 October result and WEAKER than the
  Hexagon ranges 1/3 and 0.345-0.348. The lane's gap constant is WEAKER. The finite-periodic-cube, all-flux
  form remains NEW in form.

What it says about item 2 (the Langevin gap below 2/9).
- v4 and v7, Corollary 23 (v4 p. 13): the forest-gauge-fixed box measure satisfies Bakry-Emery with
  K = kappa_G - (29/2) N abs(beta), hence LSI and Poincare with constant 1/K, for N abs(beta) < (2/29) kappa_G. For SU(2)
  this is beta_W < 4/29 = 0.138 and unit-metric gap 2K = 2 - 14.5 beta_W. The measure is gauge fixed, in boxes
  with free boundary; it is not the gauge-invariant Langevin gap of the periodic Wilson measure.
- v4 Lemma 122 (p. 63), restated in v7's Appendix K: the one-link law satisfies the Poincare inequality with
  constant 1/3 for every field.
- v7 Corollary 74(i) (pp. 42-43), from Theorem 72 and the general Theorem 125: for SU(2) with abs(beta_W) < 2/9,
  BP(n, 1 - alpha_n) holds on every even torus L >= 2n + 4 for every real f, with
  alpha_n = abs(beta_W)(18n - 3)/((4 - 18 abs(beta_W)) n^2), whenever alpha_n < 1 (for n = 2 this needs abs(beta_W) < 16/105).
  BP is a Poincare inequality for the chain that resamples cubes of side n, with Dirichlet form
  E_n(f) = n^-4 sum_x mu|f - P_x f|^2. This is a torus-uniform spectral gap of a local block dynamics at the
  lane's threshold, from the same single-link coefficients. It is not the Langevin diffusion, and no explicit
  Langevin constant is given.
- I found no Hexagon statement of a single-link Langevin Poincare inequality for the ungauged measure beyond
  the curvature range.
- Effect on the verdict. Item 2 stays NEW only as the single-link Langevin version with the explicit constant
  2 - 9 beta_W. Its range and mechanism are EQUAL to v7 Corollary 74(i) for a different local dynamics.
  The public Lemma 122 constant plus Wu's Theorem 2.2 would give the stronger 3 - 27 beta_W/2.

These are the authors' claims. I recorded them; I did not check their proofs and do not adopt them.

RESULT: Result 1 is mostly anticipated: the uniform vMF quarter and the 4D single-link chord-Dobrushin range beta_W < 2/9 are EQUAL to Bhattacharjee-Bhattacharya's unrefereed Zenodo preprint dated 18 Oct 2026 (restated in their Hexagon 2610.00341 v4 of 30 Oct and v7 of 6 Nov), the lane's gap constant 3/(50a) is WEAKER than their -log(9 beta_W/2), and the range is WEAKER than their forest-gauge beta_W < 1/3 and plaquette-block 0.345-0.348; NEW are the field-dependent sharp bound a(|F|) with its proof, the finite-periodic-cube all-flux form of the gap, and (AS-bg) for beta_W < 2/3 (vs CNS's 1/6). Result 2 is NEW only as the single-link Langevin version with constant 2 - 9 beta_W: it is Wu 2006 Theorem 2.2 applied to the public quarter, its range and mechanism are EQUAL to Hexagon v7 Corollary 74(i) (torus-uniform Poincare for a cube-resampling chain at |beta_W| < 2/9), its constant is WEAKER than public ingredients give (3 - 27 beta_W/2), and the (G2) equivalence and Lemma L are EQUAL to known facts. Result 3 is NEW as stated (no published Langevin result; closest are unrefereed transfer-matrix and cube-condition remarks resting on FS82), built from known ingredients with a coupling range far weaker than the static FS82 and Guth results. Every competing claim is unrefereed and earlier than 2026-11-12; against refereed work alone (SZZ 1/12, CNS 1/6), every lane threshold is new.
