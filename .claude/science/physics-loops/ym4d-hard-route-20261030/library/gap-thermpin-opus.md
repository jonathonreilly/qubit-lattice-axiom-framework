# FINISH row 923, gap-thermpin-opus, Claude Opus 5.5 max

(file seeded by the lead; the author writes below)

Clone commit: 1020c3efcfe45c942f5711c05eae8fa49e0ea698 (/Users/jonreilly/ym4d-lead/clone, pulled 2026-11-13, already up to date).
Author: Claude Opus 5.5 (max effort), FINISH row 923. Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.

## Target (from the brief; to be restated exactly in step 2 with check 908's corrections)

THERM-DI-pin. Along the pin path (pin field h on spatial links, from h_0 down to 0), the full pinned trace X(h) has a supplied seed X(h_0) <= 64 delta_n. The transport inequality -d_h X <= -c_h t d_t X would carry the seed to h = 0. Question: does a uniform rate c_h hold on (0, h_0]? Where could levels collapse? Does a known transition on the pin path (e.g. the Higgs-confinement crossover of a gauge-Higgs model) block it? Prove a uniform rate on an initial interval [h_1, h_0] with explicit constants, or name the exact obstruction. Test against U(1).

## Plan (one step per response; each step appended here before the next)

1. Read row 905 (D/library/gap-thermdi-astra.md) for the definition of the pinned trace, the seed and the transport inequality. Record exact statements with line numbers.
2. Read check 908 (D/library/gap-thermdi-check-opus.md) corrections (Phi_inf = 0 by cancellation; scope of the full trace) and row 898 attack 3 (D/library/gap-next3-max.md). Write the exact corrected statement of THERM-DI-pin.
3. Read (SEED-FP) in D/library/gap-finishline-opus.md lines 110-160 and the fact rows 786, 838, 843, 839, 845 only as needed for the fact tests.
4. Structure of the pinned transfer operator: what the pin does to the spectrum; derive d_h X and d_t X formulas (PROVED identities where possible).
5. Uniformity question on (0, h_0]: level collapse locations; gauge-Higgs analogy (Fradkin-Shenker / Osterwalder-Seiler analyticity; the pin as a frozen Higgs field); decide whether a transition blocks it.
6. Attempt a uniform rate on [h_1, h_0] with explicit constants (large-h expansion of the pinned operator), or identify the exact obstruction.
7. U(1) test and the Q_8 / 2T fact tests against whatever is proved or argued in 5-6.
8. Write the summary: PROVED / READ / ARGUED / GUIDE / OPEN lists and the RESULT line.

## Steps

### Step 1 — row 905 definitions (READ, D/library/gap-thermdi-astra.md)

- READ (lines 96-101). Z_h(N;B) = int exp{beta sum_p x_p + h sum_l x_l} dU, x_l = (1/2) tr U_l. The pin acts on ALL 4N|B| oriented links (spatial and temporal), not only spatial ones. The brief's "spatial links" is loose; the transfer form below pins both kinds. All four axes stay symmetric, which Theorem D(a,b) needs (line 333).
- READ (lines 105-121), (P2). On L^2(SU(2)^E), E = spatial links of the box B = b^3:
  Q_h = int prod_{x in B} e^{h x(g_x)} R(g) dg (temporal-link pin; R = spatial gauge action),
  M_h = exp{(beta/2) sum_{spatial p} x_p + (h/2) sum_{spatial l} x_l},
  T_h = M_h C_beta Q_h M_h, Z_h(N;B) = Tr T_h^N. Kernel strictly positive for h > 0; top eigenvalue simple. Q_0 = P (gauge average); nonzero spectrum of T_0 = pure-gauge spectrum on the full gauge-invariant space; non-invariant directions have eigenvalue 0.
- READ (lines 129-146). X_h(t) = log Tr T_h^t - t log lambda_0(h); U_h(t) = -d_t X_h(t) >= 0.
  (C8-pin) d_h X_h(t) = 4t|B| [v_{h,t} - v_{h,inf}], v = mean of x_l over all links.
  Forward path s = h_0 - h. Required (P): 4|B| [v_{h,inf} - v_{h,t}] <= c_h(h) U_h(t).
- READ (lines 154-188), (R): R = d_s X / (-t d_t X) = sum_{j>0} (-E_j') e^{-tE_j} / sum_{j>0} E_j e^{-tE_j}, an energy-weighted mean of -E_j'/E_j. (G): if transport holds for all t >= t_*(B), then m_B(s_1) >= e^{-I} m_B(s_0), I = int c. (cost): a closing gap forces I_B -> infinity.
- READ (lines 190-217), (CE): two-state family E_b(s) = sqrt((1-s)^2 + b^{-2}); R = (1-s)/((1-s)^2 + b^{-2}); int_0^1 R ds = (1/2) log(b^2+1). Positivity + analyticity + thermal mean alone give no uniform rate.
- READ (lines 313-347), seed. h_0 = 78 beta. Phi_h(n) = 16 log Z_h(n^4) - log Z_h((2n)^4), d_n = n/2 - 5/2, n >= 8.
  Phi_h(n) = -4(2n)^4 int_h^inf [e_n(q) - e_{2n}(q)] dq; 0 <= Phi_{h_0}(n) <= delta_n := 4608 beta n^4 2^{1-d_n}/(d_n - 1).
  Theorem D(a,b) gives X_{h_0}(n;(2n)^3) <= delta_n; Lemma E' thrice gives g_n^pin := X_{h_0}(n;(4n)^3) <= 64 delta_n.
- READ (lines 372-382), 905's target. Fixed beta_1 in [2.3, 2.6], h_0 = 78 beta_1. Want c_h >= 0, int_0^{h_0} c_h < infinity, b-independent, with -d_h X_h(t;b^3) <= -c_h(h) t d_t X_h(t;b^3) for every integer b >= 96, real 4 <= t <= b/24, a.e. 0 < h <= h_0. Endpoint by continuity: Q_h -> P in norm, T_h -> T_0 in trace norm. The endpoint full trace bounds S_ev.
- READ (lines 372-382, 133). Domain note: the seed consumer needs only 4 <= t <= b/24, so (G) is not forced from the restricted hypothesis; (CE) still breaks it on that domain.

### Step 2 — check 908 corrections, row 898 attack 3, and the exact statement

READ (D/library/gap-thermdi-check-opus.md). S3 Correction 1: Phi_inf = 0 because the 6 beta |T| constants cancel between 16 copies of n^4 and one (2n)^4, not because of concentration alone. S3 Correction 2: at h = 0 the full trace holds every electric-flux sector e in Z_2^3, so the route is glue plus flux. For h > 0 no centre symmetry separates the would-be flux levels. S4 correction: no rate is supplied anywhere on (0, 78 beta_1], including HL's region 24 beta < h <= 78 beta, because HL/HL2 give absolute, not relative, bounds. S2: the literal centre-even pin path is dead ([T_h, P_ev] != 0 for h > 0).
READ (D/library/gap-next3-max.md:512-514, row 898, Claude Fable 5.2). Pin path = Theorem HL path; proved region {beta < 2/9, all h} union {h > 24 beta}. F1 for the pin path: "the Higgs transition on the pin path". Line 514, labelled there as recalled GUIDE: the fundamental-pin SU(2) model "has a first-order line at large beta that ends near beta 2.7". That claim is checked against an open source in Step 5.

Observation (PROVED, elementary). In unitary gauge the pinned model IS the 4D SU(2) gauge-Higgs model with a fixed-length fundamental Higgs field: with phi_x in SU(2), (1/2) tr(phi_x^* U_l phi_y) becomes x_l when phi = 1, and Haar integration over phi_x is absorbed by the gauge change U_l -> phi_x^* U_l phi_y. So the pin path at fixed beta is a vertical line kappa = h in the (beta, kappa) phase diagram of that model. The literature normalisation of kappa must be matched in Step 5.

**THERM-DI-pin, exact form used below** (from 905 lines 372-382 with the 908 corrections). Fix beta_1 in [2.3, 2.6] and h_0 = 78 beta_1. For each integer b >= 96, B = b^3 periodic, let T_h be (P2) (pin on all links). Let 0 = E_0(h) < E_1(h) <= E_2(h) <= ... be the energies -log(lambda_j/lambda_0) of the WHOLE spectrum of T_h. No projection is applied. At h = 0 the nonzero spectrum is the gauge-invariant spectrum, all eight flux sectors included; the non-invariant directions sit at E = +infinity. Put X_h(t) = log(1 + S_h(t)), S_h(t) = sum_{j>=1} e^{-t E_j(h)}. Want: a measurable c_h >= 0 on (0, h_0] with I := int_0^{h_0} c_h dh < infinity, independent of b, such that for all integer b >= 96, real 4 <= t <= b/24, and a.e. h in (0, h_0]:

  (P-R)  sum_{j>=1} (d_h E_j) e^{-t E_j} <= c_h(h) sum_{j>=1} E_j e^{-t E_j}.

PROVED equivalence (from (R), 905:159, checked 908 S1). -d_h X = t sum (d_h E_j) e^{-tE_j}/(1+S) and -t d_t X = t sum E_j e^{-tE_j}/(1+S), so (P-R) is exactly -d_h X <= -c_h t d_t X. Levels whose energy FALLS as h grows (d_h E_j < 0) help; the cost comes only from levels whose energy RISES with h, i.e. falls along the path s = h_0 - h towards h = 0. The derivative exists for the trace even across crossings (908 S1).
Consumer (READ 905:362-366, 908 S3). With M = e^I, the transported seed gives X_{h=0}(a_1; (24 a_1)^3) <= [8(M+1)]^3 * 64 delta_n -> 0 as n -> infinity, a_1 = ceil(M n). The same chain stops at any intermediate h: for every h in (0, h_0], X_h(a_1; (24 a_1)^3) <= [8(M+1)]^3 * 64 delta_n (PROVED: apply the characteristic comparison on [h, h_0] only; its cost is at most I because c_h >= 0).

### Step 3 — the real object and the fact tests, as they bear on the full-trace pin route

READ (D/library/gap-finishline-opus.md:118-121, row 837, Claude Opus 5.5's port of the Sussman-Alpoge account; credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text). (SEED-FP) asks S_(K,beta)(ell/(2a_K); (ell/a_K)^3) <= s_* < 1/5041 for every first-passage datum (K, beta), K >= K_0: one physical size and one margin along a sequence of bare couplings tending to infinity. THERM-DI-pin works at ONE bare coupling beta_1 in [2.3, 2.6]. Even full success gives a fixed-coupling seed (GLUE-1 type), not (SEED-FP) (row 898 F4, D/library/gap-next3-max.md:514). ARGUED: this lane cannot reach the finish line by itself.

READ facts (FINISH.md rows 786, 838, 843). Row 786 (Codex gpt-6-astra max, unchecked): for periodic Villain U(1) at fixed beta >= 2^14 the gauge-invariant Langevin gap tends to 0 with the torus. Row 838 (GUIDE there): Q_8 freezes near beta 1.15, 2T near 2.15, 2I near 5.7. Row 843: the SU(2) Wilson convolution lies strictly below Q_8, 2T, U(1) on V_(5/2).

ARGUED (consequence for this lane; made precise in Step 7). The consumer of THERM-DI-pin ends at h = 0 with X_0(a_1; (24 a_1)^3) -> 0, a statement about the FULL trace with all flux sectors (Step 2). That endpoint is false in three test models at beta_1:
- U(1) at beta_1 above its Coulomb point: a photon level E <= kappa/b gives X_0(b/24) >= log(1 + e^{-kappa/24}) (GUIDE for compact Villain; 905 5.3).
- Q_8 and 2T at beta_1 >= 2.3, both above their freezing points (GUIDE): a frozen finite gauge group is deconfined, so the eight electric-flux sectors are nearly degenerate with the vacuum, and X_0 >= about log 8.
- Z_2 at large beta: the same, with a provable low-temperature expansion (not written here).
So THERM-DI-pin on the WHOLE path (0, h_0] must fail for U(1), Q_8 and 2T at beta_1: a proof must use an SU(2) input exactly where those models close a level. A proof on an INITIAL interval [h_1, h_0] deep in the pinned (Higgs) region may be group-blind: every compact group is in its Higgs regime there. The worst-case Dobrushin caps (2/3, 0.775) and the layer bound 4 G_3 = 1.0109 (row 839) concern beta, not h; in the pinned model at h >> beta the links are nearly independent and these caps do not bite (ARGUED; Step 6 gives the explicit regime).

### Step 4 — structure of the pinned transfer operator; exact identities

4.1 (PROVED) Self-adjointness and the one-link pin factor. M_h, C_beta, Q_h are self-adjoint, C_beta and Q_h commute (908 S3), so T_h = M_h (C_beta Q_h) M_h is self-adjoint and positive. On the pi = (tensor over x of V_{j_x}) isotypic part of the vertex group, Q_h acts as prod_x a_{j_x}(h) with
  a_j(h) = (1/d_j) int e^{h x(g)} chi_j(g) dg = (2/h) I_{2j+1}(h)
(Haar on class functions (2/pi) sin^2 phi dphi, chi_j = sin((2j+1)phi)/sin phi; the integral is I_{2j} - I_{2j+2} = (2(2j+1)/h) I_{2j+1}). All a_j(h) > 0 for h > 0, so T_h is positive definite for h > 0. Also
  d_h log a_j(h) = I_{2j+2}(h)/I_{2j+1}(h) + 2j/h   (from I_nu' = I_{nu+1} + (nu/h) I_nu).
Near h = 0, a_j ~ h^{2j}: a state carrying charges j_x has E >= sum_x 2 j_x log(1/h) - O(1), and its d_h E < 0. Charged directions fall from E = +infinity as h grows; along the path towards h = 0 they rise. They lower the numerator of (P-R); they are never the cost.

4.2 (PROVED) Hellmann-Feynman. For a simple eigenvalue lambda_j with unit vector phi_j,
  d_h log lambda_j = <phi_j, V_s phi_j> + <M_h phi_j, C_beta Q_h' M_h phi_j>/lambda_j,  V_s = sum_{spatial l} x_l,
with Q_h' acting on the pi-part as Q_h * sum_x d_h log a_{j_x}(h). So d_h E_j = w_0 - w_j, where w_j is the "pin content" of level j (the right side above), and w_0 = d_h log lambda_0 = 4|B| v_{h,inf}. The cost in (P-R) comes from levels with LESS pin content than the vacuum.

4.3 (PROVED) Trace form; no operator form. With H = -log(T_h/lambda_0) and D the pinching onto the eigenspaces of H, (P-R) reads Tr[D(d_h H) e^{-tH}] <= c_h Tr[H e^{-tH}]. The operator bound Q(d_h H)Q <= c H (Q = 1 - |Omega><Omega|) would imply it for all t, but it cannot hold with a box-uniform c whenever the vacuum moves with h. Proof: take n independent copies of one system whose vacuum omega(h) moves, so a := |<chi, (d_h H_1) omega>| = e |<chi, d_h omega>| > 0 for some level chi of energy e. Put psi = eta_1 tensor (tensor_{i>=2} (omega + eps chi)) normalised, with eta_1 excited (energy e_1), eps = (n-1)^{-1/2}, sign chosen. Then psi is orthogonal to the vacuum, <psi, H psi> -> e_1 + e, and <psi, d_h H psi> >= 2a (n-1)^{1/2} - O(1). So the best c grows like n^{1/2}. QED. Any box-uniform statement must be levelwise or in trace form.

4.4 (PROVED) Convexity. t -> X_h(t) is convex (log of a sum of exponentials). So U_h(t) >= X_h(t) - X_h(t+1) >= U_h(t+1). At integer t a sufficient form of (P-R) is the pure partition-function inequality
  (P-int)  4|B| [v_{h,inf} - v_{h,t}] <= c_h [log Z_h(t;B) - log Z_h(t+1;B) + log lambda_0(h)].
It uses no spectral input. Real t still needs (P-R) itself, or a discrete form of the characteristic argument (not written; OPEN technical point).

4.5 (READ, D/library/gap-exit-max.md:466-513, row 861, Claude Fable 5.2; checked by row 877) HL's region h > 24 beta is a single-link Dobrushin region. Every one-link conditional law is von Mises-Fisher with field F_l = h 1 + beta S_l, |F_l| >= h - 6 beta. The influence row sums are 18 beta e^m/(h - 6 beta) (Lemma V-inf). Lemma DC* then gives |e_n(h) - e_{rho n}(h)| <= 2 (36 beta/(h - 6 beta))^{d_n} for h >= 78 beta.

4.6 (PROVED, elementary) Why absolute bounds cannot give (P-R). Suppose the numerator obeys |4|B|(v_inf - v_t)| <= A |B| e^{-m_1 t} and the denominator obeys U_h(t) >= a N_1 e^{-m_2 t} (N_1 one-particle states, each of energy at most m_2 by a variational bound). The quotient bound is (A|B|/(a N_1)) e^{(m_2 - m_1) t}. With N_1 of order |B| it is box-uniform on t <= b/24 only if m_1 >= m_2. Dobrushin-type rates are not sharp: at large h/beta, 4.5 gives m_1 = log((h - 6 beta)/(36 beta)), while the free one-link guide (Step 6) gives m_2 about log(h/beta). The loss is about e^{t log 36}, unbounded on t <= b/24. So a proof needs the numerator's exact leading rate: a ratio expansion in which numerator and thermal energy share their leading wrapping terms. This quantifies check 908 S4.

Correction to 4.1 (self-read). The sentence "a state carrying charges j_x has E >= sum_x 2 j_x log(1/h) - O(1)" is ARGUED, not PROVED: M_h mixes charge sectors, so eigenvectors are not pure-charge. What is PROVED is the factor a_j(h) ~ h^{2j} on each charged part of Q_h.

### Step 5 — where levels could collapse; the transition on the pin path

5.1 READ (C. Bonati, G. Cossu, M. D'Elia, A. Di Giacomo, "Phase diagram of the lattice SU(2) Higgs model", Nucl. Phys. B 828 (2010) 390, arXiv:0911.1721; open LaTeX source downloaded to lane923/dl-3, read with python -I, text.tex lines cited). Monte Carlo results, so GUIDE for this lane.
- Lines 41-45: S = beta sum (1 - (1/2) Re Tr P) - (kappa/2) sum Tr[phi^* U phi]. In unitary gauge the hopping term is -kappa sum x_l. So kappa = h exactly, with the same beta.
- Lines 54-61: at beta = infinity the model is the O(4) sigma model with a transition at kappa about 0.6. Fradkin-Shenker (with the Osterwalder-Seiler cluster expansion) prove analyticity of local observables near beta = 0 and for kappa -> infinity.
- Lines 155-165, 203-206: at beta = 2.5 there is no transition, only a smooth crossover. Susceptibility peaks grow like L^4 up to L about 18, then saturate. The correlation length there is about 10 lattice spacings. Earlier first-order claims for beta >= 2.3 came from lattices up to 25^4.
- Lines 220-234: first order at beta = 2.775, 2.79, 2.8 (kappa = 0.704675(30) at 2.775; double peak at 2.8 on L = 45, 50).
- Lines 287-293: endpoint beta_c = 2.7266(16) and 2.7299(36).
- Lines 464-479: the crossover continuation of the first-order line moves to smaller beta as kappa grows and meets the pure-gauge bulk crossover (beta about 2.2-2.3) at a point A. No transition there.
So row 898's recollection (D/library/gap-next3-max.md:514) is right in substance: the first-order line ends near beta 2.73. For beta_1 in [2.3, 2.6] the pin path (kappa = h from 78 beta_1 down to 0) crosses only a crossover (GUIDE). For beta_1 > 2.73 it crosses a first-order line (GUIDE).

5.2 Lemma CL (closing level kills THERM-DI-pin; PROVED from the consumer chain checked in 908 S3). Fix beta. Suppose there are kappa < infinity and, for all large integers a, some h(a) in (0, h_0] such that the full pinned trace on B = (24a)^3 has E_1(h(a)) <= kappa/(24a). Then no b-independent integrable c_h satisfies (P-R) on (0, h_0].
Proof. If c_h exists with cost I, put M = e^I. Step 2 gives, for every n >= 8 and every h in (0, h_0], X_h(a_1; (24 a_1)^3) <= eps_n := [8(M+1)]^3 * 64 delta_n, a_1 = ceil(Mn), and eps_n -> 0. Take h = h(a_1): X >= log(1 + e^{-a_1 E_1}) >= log(1 + e^{-kappa/24}) > 0. This contradicts eps_n -> 0. QED.
Instances. (i) A first-order point crossed by the path: at the finite-volume pseudo-critical h_c(b) the two phases give a tunnelling doublet with E_1 of order e^{-sigma_I b^3} (Borgs-Kotecky picture; GUIDE for SU(2)-Higgs). (ii) A critical point with E_1 <= kappa/b. (iii) A gapless endpoint phase (U(1) Coulomb; deconfined finite groups), Step 7. So for SU(2) at beta_1 > 2.73 THERM-DI-pin is false, conditional on the Monte Carlo first-order line (GUIDE-conditional refutation). This does not touch the window [2.3, 2.6].

5.3 ARGUED, where the SU(2) levels sit along the path at beta_1 in [2.3, 2.5].
- Near h = 0: charged directions sit high and rise as h -> 0 (4.1). Flux levels sit near sigma b (confinement, GUIDE). Glue levels sit near the glueball mass. Nothing closes, provided SU(2) at beta_1 has the gap we are trying to prove. This is consistent, not a proof.
- Large h: Higgs regime; levels near log(h/beta) and rising with h (Step 6). Nothing closes.
- The crossover near kappa about 0.7-0.8 (GUIDE): minimal gap about 1/xi, about 0.1 at beta = 2.5. Nothing closes in infinite volume; Lemma CL does not apply.
So the transition question does not block a uniform rate in the window (GUIDE). It does set its size. A heuristic cost (the all-time bound (G) read backwards) is I >= log(m(h_0)/m_min), about log(4.4/0.1), about 3.8 at beta 2.5 (GUIDE). Then M about 44, and the consumer needs [8(M+1)]^3 * 64 delta_n <= log(11/10): n about 150 suffices, so a_1 about 6600 and b about 1.6e5 (GUIDE arithmetic; delta_n from 905:325). Box size is not an obstacle at fixed beta. Near the endpoint the cost grows: prefer beta_1 at the low end of the window (2.3 to 2.5), away from beta_c = 2.73.
- The whole strip 0 < h <= 24 beta_1 lies outside every proved expansion region (HL; Fradkin-Shenker's analyticity region is near beta = 0 and kappa = infinity). Analyticity along the path at beta_1 is OPEN.

### Step 6 — a rate on an initial interval: what is proved, and the exact obstruction for SU(2)

6.1 The Gaussian pinned model (the quadratic part of the action). From x = cos(|theta|/2) ~ 1 - |theta|^2/8, each of the three colours carries S_2 = (beta/8) sum_p (dA)_p^2 + (h/8) sum_l A_l^2, a lattice Proca field.
- PROVED (propagator). K = beta (phat^2 delta - phat phat) + h delta; K^{-1} = delta/(beta phat^2 + h) + beta phat phat/(h (beta phat^2 + h)). The only pole in p_0 sits at 4 sinh^2(omega/2) = h/beta + sum_i 4 sin^2(p_i/2), with a residue of rank 3.
- ARGUED (standard, not re-derived here). The transfer operator of this Gaussian reflection-positive measure is the second quantisation of e^{-omega}. Every level is E = sum n_{p,s,c} omega(p): 3 polarisations times 3 colours per spatial momentum.
- PROVED, given that Fock structure. From sinh(omega) d omega = d(h/beta): d_h omega(p) = 1/(beta sinh omega(p)). So d_h log omega decreases in omega and peaks at p = 0. For every level, d_h E/E <= max over modes of d_h log omega = c^G(h) := 1/(beta omega_0 sinh omega_0), omega_0 = 2 arcsinh(sqrt(h/beta)/2). Hence (P-R) holds with c^G for every t > 0 and every box. Its cost is exact: int_{h_1}^{h_0} c^G dh = log(omega_0(h_0)/omega_0(h_1)). The gap bound (G) of 905 is attained with equality: in this model the transport cost is the log of the gap ratio.
- GUIDE arithmetic (python -I, closed forms). omega_0 = 5.835, 4.382, 3.257, 0.962, 0.523 at h/beta = 340, 78, 24, 1, 0.28. Costs: [24 beta, 78 beta] 0.297; [78 beta, 340 beta] 0.286; from 78 beta down to h/beta = 0.28 (h = 0.7 at beta = 2.5, the crossover) 2.125. As h -> 0, omega_0 ~ sqrt(h/beta) and the cost diverges like (1/2) log(beta/h): at h = 0 the model is the free (noncompact U(1)) photon and its level closes. The Gaussian model fails exactly where a Coulomb level closes.
- Integer-time form (P-int) in the same model (PROVED from the leading terms X ~ N e^{-t omega}, D = X(t) - X(t+1) ~ (1 - e^{-omega}) X): it needs c >= d_h omega/(1 - e^{-omega}), and its cost is about omega_0(h_0) - omega_0(h_1), 1.13 on [24 beta, 78 beta]. Finite, but worse than (P-R).

6.2 Seed shift (PROVED). For every h_0' >= 78 beta: X_{h_0'}(n; (4n)^3) <= 64 delta_n, with the same delta_n. Reason: HL2's proof bounds |e_n(a) - e_{2n}(a)| <= 2 (36 beta/(a - 6 beta))^{d_n} pointwise for a >= 78 beta (D/library/gap-exit-max.md:497); integrating from h_0' gives at most the integral from 78 beta; then Theorem D(a,b) and Lemma E' run as in 905 Step 7. So the initial interval may start as high as wanted.

6.3 SU(2) on [h_1, h_0]: the attempt and where it stops.
- What must be bounded. The domain includes t = 4 at b = 96, where the thermal sum is extensive (Gaussian guide at h = 24 beta: S ~ 9 * 96^3 * e^{-13.03}, about 18). So multi-excitation levels dominate. One-particle control is not enough. (P-R) needs the energy-weighted mean of d_h E_j/E_j over the whole many-body spectrum, uniformly in b.
- Excluded tools (PROVED in Step 4). No operator inequality on the vacuum complement works (4.3). Absolute bounds (HL, Dobrushin) lose a factor e^{t (m_2 - m_1)}; at large h/beta the loss rate is about log 36 (4.6).
- What a proof would need (OPEN; the exact obstruction). A box-uniform low-temperature expansion of X_h(t; b^3) over time-wrapping excitation polymers, organised around the exact pinned one-link transfer operator. Each wrapping excitation of length t must carry the exact factor e^{-t omega(h)}, not a Dobrushin rate. The numerator and the thermal energy (or D(t), via (P-int)) must expand in the same polymers, with the one-excitation terms dominating. No such expansion is written in the lane or in the sources read.
- Where such an expansion could converge (GUIDE, crude count, mine). Under the pinned one-link law E[1 - x_l] ~ 3/(2h), so the plaquette activity beta(1 - x_p) has mean about 6 beta/h. Each plaquette meets 20 others through a link. A Kotecky-Preiss count needs roughly 6 beta/h <= 1/(21 e), so h >= about 340 beta, far above HL's 24 beta. By 6.2 the seed may start there. The Gaussian guide prices [78 beta, 340 beta] at 0.29.
- Verdict. No uniform rate is proved for SU(2) on any interval. No obstruction in principle exists on the deep-pinned part: there the Gaussian guide passes with cost below 0.3 per interval above. The missing input is technical and specific: the ratio expansion above. Even that would not touch the hard part of the path, 0 < h <= 24 beta_1, which holds the crossover.

### Step 7 — the fact tests against Steps 5-6

7.1 U(1) (charge-one pin e^{h cos theta_l}; the U(1) gauge-Higgs model). At beta_1 in [2.3, 2.6], above the pure U(1) Coulomb point near 1, the path ends in the Coulomb phase (GUIDE).
- PROVED (continuity). At fixed box, T_h -> T_0 in trace norm as h -> 0+ (905:382, checked 908 S3; the proof is group-blind). So if the h = 0 trace has E_1(0) <= kappa/b, then for each box some h(b) > 0 has E_1(h(b)) <= 2 kappa/b. Lemma CL then forbids an integrable rate.
- So THERM-DI-pin fails for U(1) at beta_1, given a photon level E_1(0) <= kappa/b on the gauge-invariant space. That premise is exact for the noncompact Gaussian model (6.1: omega_0 -> 0 at h = 0, minimal momentum 2 pi/b). For compact Villain or Wilson U(1) it is GUIDE; row 786 proves only the Langevin (not transfer) version for Villain at beta >= 2^14.
- My statements pass the test. Lemma CL predicts the U(1) failure. The Gaussian rate (6.1) diverges exactly at the closing. The seed shift (6.2) and any ratio expansion on h >= 340 beta are group-blind, which is allowed there: U(1) is in its Higgs regime and closes no level at large h. A continuation through the crossover must not be group-blind: it must break where U(1) meets its Higgs-Coulomb line (GUIDE location: kappa of order 0.3 to 0.6).

7.2 Q_8 and 2T at beta_1 >= 2.3, both frozen (row 838, GUIDE). A frozen finite gauge group is deconfined. On T^3 its gauge-invariant ground space carries at least |Z(G)|^3 = 8 nearly degenerate states, labelled by the electric flux e in Z_2^3, split by tunnelling of order e^{-c b^2} (GUIDE; provable at large beta by a low-temperature expansion, not written). By 7.1's continuity step and Lemma CL, THERM-DI-pin fails for Q_8 and 2T at beta_1.
- ARGUED consequence (the main structural point of this step). The failure for Q_8 and 2T runs through the flux sectors at small h. So a proof for SU(2) on the whole path must show, on the low-h part, that the would-be flux levels stay gapped uniformly in b: a confinement statement. That is the flux half of the seed, the lane's hard (CORE)/(E17) problem (row 892). The full-trace pin route therefore does not bypass the flux half. It sharpens check 908's Correction 2 ("glue plus flux") into a necessity: no group-blind or glue-only argument can carry the route to h = 0.
- ARGUED (a centre-symmetric pin does not repair this). The adjoint pin e^{h chi_adj(U_l)} commutes with the cut-link flips G_z (chi_adj(-U) = chi_adj(U)), so it keeps the centre-even sector. But as h -> infinity it forces U_l -> +-1, and the weight becomes e^{beta sum_p sigma_p}: Z_2 gauge theory at coupling beta_1 >= 2.3, far inside its deconfined phase (critical point near 0.44, GUIDE). That Higgs phase is separated from SU(2) confinement by a genuine transition (Fradkin-Shenker's adjoint case). The path then crosses a closing point, and Lemma CL's mechanism applies in the even sector (a critical level or a coexistence doublet; GUIDE). So the two natural pins fail for opposite reasons: the fundamental pin breaks the centre and drags in the flux half; the adjoint pin keeps the centre and crosses a transition.

7.3 The Dobrushin caps (2/3, 0.775), the layer bound 4 G_3 = 1.0109 and (AN1) concern the coupling at h = 0. The proved and guided statements above live at h >= 24 beta (HL's single-link Dobrushin region) or are model computations. No claim here crosses those caps. The strip 0 < h <= 24 beta_1 at beta_1 about 2.5 has h/beta below 24, where no worst-case single-link bound holds (row sums 18 beta/(h - 6 beta) >= 1 once h <= 24 beta); a tool there must be typical-case and SU(2)-specific (7.1, 7.2).

### Step 8 — summary

PROVED (mine, by hand; not checked by anyone else)
- P1 (Step 2). In unitary gauge the pinned model is the fixed-length fundamental SU(2) gauge-Higgs model, with kappa = h in the normalisation of Bonati et al. THERM-DI-pin is exactly (P-R) on the whole spectrum of T_h. The transported bound X_h(a_1; (24 a_1)^3) <= [8(M+1)]^3 * 64 delta_n holds at every h in (0, h_0], not only at h = 0.
- P2 (Step 4). a_j(h) = (2/h) I_{2j+1}(h) and d_h log a_j = I_{2j+2}/I_{2j+1} + 2j/h; Hellmann-Feynman d_h E_j = w_0 - w_j; the pinching form of (P-R); no b-uniform operator inequality Q (d_h H) Q <= c H exists once the vacuum moves (constant at least of order n^{1/2} on n-fold products); convexity in t and the integer-time sufficient form (P-int); absolute bounds need matching exponential rates, and the Dobrushin rate misses the free rate by about log 36 at large h/beta.
- P3 (Step 5.2, 7.1), Lemma CL. If for all large boxes some h in (0, h_0] has E_1 <= kappa/b, or the h = 0 trace has such a level (by trace-norm continuity), then no b-independent integrable rate exists.
- P4 (Step 6.1). In the Gaussian (Proca) pinned model, every level obeys d_h E/E <= c^G = 1/(beta omega_0 sinh omega_0), and the cost is exactly log(omega_0(h_0)/omega_0(h_1)). It diverges like (1/2) log(beta/h) as h -> 0. This rests on the standard Fock structure of Gaussian reflection-positive transfer operators, ARGUED and not re-derived.
- P5 (Step 6.2). The seed X_{h_0'}(n; (4n)^3) <= 64 delta_n holds at every h_0' >= 78 beta.

READ. Rows 905, 908, 898, 861 (HL, HL2), 837 ((SEED-FP)); FINISH rows 786, 838, 843 (paths and lines in Steps 1-5). Bonati, Cossu, D'Elia, Di Giacomo, Nucl. Phys. B 828 (2010) 390, arXiv:0911.1721, text.tex lines 41-61, 155-206, 220-293, 464-479.

GUIDE. The Monte Carlo phase diagram: the first-order line ends at beta_c = 2.7266(16) / 2.7299(36); beta = 2.5 is a crossover with xi about 10; first order at 2.775-2.8. So at beta_1 in [2.3, 2.6] the pin path crosses no transition. At beta_1 > 2.73 it crosses the first-order line, and Lemma CL refutes THERM-DI-pin there (a refutation conditional on that line). Cost estimate about 3.8 at beta 2.5, with b about 1.6e5 in the consumer. Gaussian numbers (0.297 on [24 beta, 78 beta]; 2.125 from 78 beta down to the crossover). The crude expansion threshold h >= about 340 beta. The freezing points of Q_8 and 2T; the photon level of compact U(1).

ARGUED. U(1), Q_8 and 2T at beta_1 fail THERM-DI-pin through a closing photon or flux level at small h (Lemma CL with GUIDE premises). Hence an SU(2) proof through the low-h part must show the would-be flux levels stay gapped, that is, supply the flux half of the seed: the full-trace pin route cannot be glue-only or group-blind. A centre-symmetric (adjoint) pin keeps the even sector but starts in deconfined Z_2 gauge theory and crosses a genuine transition. For SU(2) at beta_1 in [2.3, 2.5] no level closes near h = 0 or at large h (5.3).

OPEN. THERM-DI-pin for SU(2) at any beta_1 in [2.3, 2.6]. A uniform rate on any interval for SU(2), including the deep-pinned part: the missing input is a b-uniform low-temperature ratio expansion built on the exact one-link pinned transfer operator, so that numerator and thermal energy share their leading wrapping terms. The real-t form from (P-int). Analyticity along the path for 0 < h <= 24 beta_1. The flux-half input on the low-h part.

Provenance and limits. Author: Claude Opus 5.5 at max effort, no subagents, no independent check. Only this file was written; no repository file was edited. Downloads: lane923/dl-1 (arXiv metadata), dl-2 (PDF, not read: no renderer), dl-3 (LaTeX source, read with python -I); none is committed. One numeric call (closed-form arithmetic, GUIDE). Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their account, for (SEED-FP) as ported in row 837; Balaban's estimates are not used here. Fradkin-Shenker and Osterwalder-Seiler are credited through the paper read, not read at source.

RESULT: THERM-DI-pin stays OPEN for SU(2), and no uniform rate is proved on any interval; PROVED: Lemma CL (a level at most kappa/b anywhere on (0, h_0], or at h = 0 by continuity, forbids every box-uniform integrable rate), the exact Gaussian (Proca) control with rate 1/(beta omega_0 sinh omega_0) and cost exactly log(omega_0(h_0)/omega_0(h_1)), divergent as h -> 0, the seed shift to any h_0' >= 78 beta, and the exclusion of operator-form and absolute-bound routes (rate mismatch about log 36); GUIDE (Bonati et al. 2010, Monte Carlo): the fixed-length SU(2)-Higgs first-order line ends at beta_c about 2.73, so the pin path at beta_1 in [2.3, 2.6] crosses only a crossover (xi about 10 at 2.5) and is not blocked, while beta_1 > 2.73 is refuted through Lemma CL; ARGUED: U(1), Q_8 and 2T fail through closing photon or flux levels at small h, so any SU(2) proof through the low-h part must supply the flux half (confinement), and an adjoint pin crosses a Z_2 transition instead.
