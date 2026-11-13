# FINISH row 920, gap-glue2-opus, Claude Opus 5.5 max

(file seeded by the lead; the author writes below)

Clone: /Users/jonreilly/ym4d-lead/clone at commit 1f6e9018affb95f6576883dce4197190e600fa7f (pulled 2026-11-13, already up to date).
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
SA sources: /Users/jonreilly/ym4d-lead/sa at commit 31a47c543775 (bounded reads only).
Author: Claude Opus 5.5, max effort. Status labels: PROVED (mine), READ (path:line), ARGUED, GUIDE, OPEN.

## Target (provisional; fixed in Step 2 after reading)

The glue half of (SEED-FP): the centre-even thermal sum S_ev <= 1/10 on one box (Lemma SPLIT,
Corollary O1, row 892). Candidate forms: (Z0)+(COUNT) of row 895, the transport form (BETA)_C,
or a corrected form after check 896. Box size from the margins of row 918.

## Plan (at most eight steps, one per response)

1. Read sources: SEED-FP (gap-finishline-opus.md 110-160), row 892/893 split, row 895 and its check 896, row 918 margins. Record exact statements (READ).
2. Fix the target: choose among (Z0)+(COUNT), (BETA)_C, corrected form; set the box size; say why it is the best form.
3. Read the tools: virial identity and even D-shape (kept by 896), B1 two-slice bridge (row 863, check 879), Langevin gap and (VAR-SLAB) (rows 899, 901), fact tests (rows 786, 838, 839, 843, 845).
4. Crux lemma, stage A: reduce the target to one inequality on one box; state it with constants.
5. Crux lemma, stage B: attempt the proof by the strongest available tool; check against the fact tests (U(1) Coulomb must fail; Q_8/2T distinction).
6. Crux lemma, stage C: continue or try the second tool; record exactly where it stops.
7. GUIDE run if useful (small, refute/guide only), and the fact-test audit of the argument.
8. Summary: PROVED / ARGUED / OPEN list; RESULT line.

## Step 1 notes (reading; READ items)

1a. (SEED-FP) (READ D/library/gap-finishline-opus.md L114-118): one physical size ell, ell/(2 a_K) integer >= 3, s_* < 1/5041, for every first-passage datum (K, beta) at g, K >= K_0: S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) <= s_*. Bare Wilson transfer operator, periodic cube, time ell/2. Lemma FL (L131-137, ARGUED there) gives (SEED-FP) at a larger size from an order-one seed through Theorem SH; constants absolute.
1b. Lemma SPLIT (READ D/library/gap-crux-core-max.md L265-270): T = positive trace-class transfer operator of a periodic box B; Z_chi(t) = Tr(T^t P_chi) over the 8 centre sectors; S = Tr T^t/lambda_0^t - 1; S_ev = Z_0(t)/lambda_0^t - 1; q_i = (1 - Z^(v_1i)/Z^0)/2, Q_0 = max q_i. If 3 Q_0 < 1: (1 + S_ev)/(1 - Q_0) <= 1 + S <= (1 + S_ev)/(1 - 3 Q_0). Corollary O1 (b) (L272): S_ev <= 1/10 and Q_0 <= 1/20 give S < 3/10.
1c. The glue half as row 892 states it (READ L276-279): GLUE-FP: S_ev(a; b^3) <= t(r)/2, which is 1/10 at r = b/a >= 24 (Theorem SH line r >= 24, thresholds READ gap-seed-shape.md L116-125: t = 1/1650 (r=2), 1/100 (3), 1/25 (4), 1/10 (6), 3/10 (r >= 24)). One torus (a, b, b, b): time a, spatial cube b^3, m = 0, no rate.
   Note for the target: at r >= 24 the spatial cube is 24 times the time. S_ev counts every even state of the spatial box b^3, so a dilute glueball gas gives S_ev ~ exp(b^3 sum_p e^(-a E(p))) - 1 (GUIDE heuristic). The smaller r rows (r = 2: t/2 = 1/3300; r = 6: 1/20) trade threshold for volume. Step 2 must choose the line.

1d. Row 895 (READ D/library/gap-glue-max.md, all 354 lines; author Claude Fable 5.2, unchecked there; its check is row 896). Statements I may need (subject to check 896):
   - G1 (L106-109): r_1^a <= S_ev(a) <= r_1^(a - t_0) S_ev(t_0) <= r_1^(a - t_0) S(t_0); S_ev(t + t') <= S_ev(t) S_ev(t').
   - G2 (L112-116): log(1 + S_ev(a)) <= D_ev(a, s) := log Z_0(a) + log Z_0(s) - log Z_0(a + s) <= log(1 + S_ev(a)) + log(1 + S_ev(s)).
   - G3 (L118-122): S_ev(2s) = E_nu chi^2(Pbar^s(x, .) || nu-bar), the centre-orbit chain.
   - G4 (L124-128): crossing identity at the shape (a, b, b, b): 1 + S_ev(a; b^3) = exp(Cas(a, b)) (1/4) sum_m sigma_m, Cas = b e(a, b, b) - a e(b, b, b).
   - G5 (L176-184): S_ev(a; b^3) <= exp[(2b/a)^3 G_0(a/2) - m_ev a/2], G_0(t) = g(t; (2t)^3) = log(1 + S(t; (2t)^3)); (Z0) m_ev((24a)^3) a >= 2[110592 G + log(1/sigma)], (COUNT) G_0(a/2) <= G. Uses Lemma E' (READ gap-seed-shape.md L60-70): h >= y > t >= 3: g(t; B^h) <= (h/(y - t)) g(t; B), per direction.
   - Even D-shape (L205-210): log(1 + S_ev(a; b^3; beta)) = 6 a b^3 int_0^beta [u_(ev,a)(s) - u_inf(s)] ds.
   - Lemma LOC (L229-233): gauge-invariant f on a non-wrapping region is centre-blind.
   - Lemma MC (L220-223): maximal correlation of two slabs at distance w is r_1^w. Proposition FIB (L238-242): L^2-averaged finite-block conditions equal the worst case.
   - Lemma UP (L250-253): G_0(2t) <= 1728 G_0(t).
   - Proposition TR (L260-264): (BETA)_C (every even branch: -d log E/ds <= C) on [beta_0, beta_1] gives S_ev(a; B; beta_1) <= S_ev(a e^(-C(beta_1 - beta_0)); B; beta_0).
   - Hamiltonian virial identity (L281): for H = K/lambda + lambda N: lambda dG/d lambda = 2 lambda Delta N - G (G a level gap, Delta N its magnetic energy above the vacuum's). Stops there (L280-284): form bounds give extensive constants; no convexity for log(lambda_0 lambda_1); monotone case false.
   - GUIDE (L314): electric model levels E_j(s) = -log(I_(2j+1)(s)/I_1(s)), max -d log E/ds = 1.139 at s = 0.36, 0.39 at 2.5.
   - Where it stops (L340): vacuum functional not known local; pointwise curvature false; averaged block = worst case; global exact inequalities point the wrong way (CS); transport needs volume-uniform C.

1e. Check 896 (READ D/library/gap-glue-check-astra.md, Codex gpt-6-astra xhigh; lines 1-538). Verdicts I rely on:
   - HOLDS: G1, G2 inequalities (not the same-threshold equivalence), G3, Lemma MC, Lemma G5 with 110592 (sufficient only; not "weakest"), even D-shape (signed identity, L440-459), virial identity lambda G' = 2 lambda Delta N - G, (lambda G)' = 2 lambda Delta N (L461-478; Hamiltonian family only, not the isotropic Wilson transfer).
   - Lemma UP improved (L300-305): G_0(2t) <= g(t; (4t)^3) <= 64 G_0(t).
   - G4: product formula only; Cas <= log 4 + log(1 + S_ev); no "no Casimir energy" reading (D1, L130-137).
   - LOC: local gauge-invariant => even (inclusion only). Converse FAILS in the class (D3, L222-232): frozen Q_8/2T have distinct even flat states with identical local holonomies. "The zero-flux gap bounds local decay; equality with the lightest locally accessible energy needs an additional cyclicity/overlap argument."
   - D6 (L405-424, from gap-crux-exercise2-check-astra.md L227-266): frozen Q_8, 2T FAIL static GLUE. Flat triples (1,1,1) and (i,1,1) give orthogonal even flat vectors; ||T - P_flat|| <= eta = (1 + (|G|-1) z)^E - 1 + z, z = exp(-beta d_G), and S_ev(t; B) >= ((1-eta)/(1+eta))^t >= 1/2 when beta >= (1/d_G) log(16 E (|G|-1) t), d_Q8 = 1, d_2T = 1/2. Z_2 passes static GLUE at large beta on a fixed box (Lemma Z2-c, gap-es1-opus.md L157-168: S_ev -> 0, q_i -> 1/2).
     CONSEQUENCE for this note: the torus number S_ev sees topological (flat) even states. A proof of GLUE-FP must use something frozen Q_8/2T lack: the absence of a non-central flat sector degenerate with the vacuum. A proof of only a LOCAL gap would not suffice for the torus number (D3).
   - D5 (L366-382): analyticity plus non-closure does not give one all-level C in (BETA)_C (explicit diagonal counterexample). TR alone proves no cutoff-uniform seed; first passage needs sup_K a_K exp(int C) < infinity.
   - U(1) fact test (L427): row 786 proves a periodic Villain LANGEVIN gap tends to 0; it does not evaluate S_ev, COUNT or m_ev ~ 2 pi/b. The photon numbers are GUIDE.
   - Q8/2T/Z2 "pass all gauge-invariant block criteria" FAILS as proved (L429).

1f. Margins (READ D/library/gap-margins-opus.md L226-265, GUIDE only; corrected by check 919, D/library/gap-margins-check-astra.md L125-148, Codex gpt-6-astra):
   - Direct runs resolve G = log(1 + S) only in hot boxes (t = 2, 3; G = 4 to 27). The cold seed is UNMEASURED.
   - Dilute-gas model (free glueballs + one Z_2 electric flux per direction): cube S(N; (2N)^3) < 1/5041 first at N = 9 to 10 (beta 2.3), N = 14 to 17 (2.5), m_0 N about 12.5. SH shape (a; (24a)^3), S <= 3/10: a = 9 to 10 at 2.3 (b = 216 to 240); at 2.5, a = 14 to 18 (check 919 correction: sides 336 to 432).
   - Check 919: "S_ev = S" FAILS at one advertised box (beta 2.5, m_0 = 0.9, N = 14: S_ev/S about 0.524). The gas forecasts are parameter scenarios, not brackets. Athenodorou-Teper inputs (READ via check 919 L134-135): m_0 = 1.224(16) at beta 2.2986, 0.6563(56) at 2.509.
   - Rate: S falls about 3 to 4 times per lattice unit of N at beta 2.3 (about e^(-m_0) (N+1)^(3/2)/N^(3/2)).
   Reading for the target (ARGUED from GUIDE): at r = 24 the glue half needs a about 9 to 10 at beta 2.3, b about 216 to 240: about 2e9 sites per time slice' worth of cube volume factor (24)^3 = 13824 times a^3. The glue half is the size-setting half.

## Step 3 notes (tools; READ). (Done before Step 2, since the target choice depends on them.)

3a. Row 863 (READ D/library/gap-crux-skeleton-max.md L104-136; checked by row 879): T = e^(-V/2) K e^(-V/2), K = product of one-link kernels k composed with the gauge projection, V = -beta sum over spatial plaquettes (1/2) tr U_p. I1: P f = Omega^(-1) T(Omega f)/lambda_0 is a self-adjoint Markov operator on L^2(nu), nu = Omega^2 dU, P(U, dU') = K(U, U') g(U') dU'/(K g)(U), g = e^(-V/2) Omega, K g = lambda_0 e^V g. I2: S(2s; B) = E_nu chi^2(P^s(U, .) || nu). B1 (check 879 HOLDS): the infinite-time two-slice law is pi(dU, dU') = a(U) k_orb(U, U') a(U') dU dU', a = e^(-V/2) Omega/sqrt(lambda_0): the static Schroedinger bridge from nu to nu with reference kernel k_orb. B3: 1 - r_1 = inf E_pi[(f(U') - f(U))^2]/(2 Var_nu f). Row 863 2.3: a proof must show the long-wavelength response of mu_U is bounded away from 1 by a non-abelian effect. Its claim "Q_8, 2T pass the thermal part" is corrected by check 896 D6 (they fail the torus number).
3b. Row 899 (READ D/library/gap-wall-assume-max.md L299-354; check 901 D/library/gap-wall-assume-check-astra.md L19-67: T2-T5 HOLD, T6 HOLDS AFTER CORRECTION of the force description): (VAR-SLAB) is a FLUX-half reduction: 4p(1-p) = Var_w(rho) <= lambda^(-1) E_w|grad X|^2, lambda the gauge-invariant Langevin (Poincare) constant of the torus measure. Langevin gap proved only for beta_W < 1/4 (8/27 on some tori; READ gap-finishline-opus.md:189 through row 899); Shen-Zhu-Zhu |beta_W| < N^2/48 (READ through check 901 L11). Its Poincare structure for the GLUE half: Var_mu(f) <= lambda^(-1) mu|grad f|^2 for gauge-invariant f on the torus implies the even (and full) spectral gap of T on gauge-invariant functions (ARGUED standard; to be made exact if used).
3c. Fact tests (READ through row 895/896 and row 899): row 786 Villain U(1) at beta >= 2^14: gauge-invariant Langevin gap -> 0 with the torus (Theorem V). Q_8 Haar moments first differ from SU(2) at degree 4, 2T at degree 6 (row 838 through row 895 L94). Caps: single-link 1/3, star 0.3609, vertex block 0.775, layer twist 4 G_3 = 1.0109; (AN1) = worst case (row 845); FIB (check 896: holds for operator inequalities on all fibre tests only).

## Step 2. The target, its box size, and why this form

### 2.1 Target (fixed)

Torus (a, b, b, b), time along direction 1, b = 24 a (row 892's Theorem SH line r >= 24). Bare Wilson SU(2) at one coupling beta in the order-one window [2.3, 2.6]; in the real problem, every first-passage datum (K, beta) at one physical pair (ell_t, 24 ell_t), a = ell_t/a_K.

  (GLUE-FP)   S_ev(a; b^3) <= 1/10.

Box size (GUIDE, row 918 as corrected by check 919): a = 10 to 11 at beta 2.3 (b = 240 to 264), a = 15 to 18 at beta 2.5 (b = 360 to 432), that is m_0 a about 12.5 to 13.5. Margin left by the form below (Step 2.3): it costs at most a factor 2 in log(1 + S_ev), about one more lattice unit of a (S falls 3 to 4 times per unit, GUIDE).

### 2.2 The form I attack: the insertion (cut-and-reglue) form at fixed coupling

Write Z_0(t) = Tr(T^t P_0), P_0 = (1/8) sum_k C^k, and D_ev(a, s) = log Z_0(a) + log Z_0(s) - log Z_0(a + s) (row 895 G2, check 896 HOLDS). Facts (READ check 896 L84-96): log(1 + S_ev(a)) <= D_ev(a, s) <= log(1 + S_ev(a)) + log(1 + S_ev(s)), and D_ev(a, s) -> log(1 + S_ev(a)) as s -> infinity (simple vacuum, trace class).
Each D_ev is a free-energy difference between two GLUINGS of the same slices: Tr(T^a P_0) Tr(T^s P_0) = Tr((T^a P_0 x T^s P_0)), and Z_0(a + s) = Tr((T^a P_0 x T^s P_0) SWAP) (row 863 I3, swap twist). The two gluings differ only on the 2 x 3 b^3 time-like plaquettes of ONE seam. An exponential interpolation of the seam action at fixed beta (Step 4) gives

  (INS)  log(1 + S_ev(a)) = beta * integral_0^1 dtheta  sum over the 6 b^3 seam plaquettes of  E_theta^(a, infinity)[x_p^A - x_p^B],

an exact identity at the one coupling beta, with a LOCAL integrand (x_p = (1/2) tr U_p in gluing A or B). The crux lemma is then a statement on one seam plaquette:

  (SEAM)_psi  for every theta in [0, 1], uniformly in b:  | E_theta^(a, inf)[x_p^A - x_p^B] - E_theta^(inf, inf)[x_p^A - x_p^B] | <= psi(a),

together with the cancellation of the (inf, inf) part (Step 4, to be proved). Then log(1 + S_ev(a; b^3)) <= 6 beta b^3 psi(a), and (GLUE-FP) needs psi(a) <= log(1.1)/(6 beta (24 a)^3) (= 5.0e-10 at a = 10, beta = 2.3).

### 2.3 Why this is the best form (ARGUED, with the reasons that are exact marked)

1. Static. It is at the one coupling beta. The transport form (BETA)_C and the even D-shape both integrate over every coupling in [0, beta], through the crossover near 2.2 and the freezing points of Q_8 (1.15) and 2T (2.15) (GUIDE values); D5 of check 896 shows an all-level C does not follow from analyticity, and first passage needs sup_K a_K exp(int C) < infinity (READ check 896 L384-401). The margins call transport TIGHT (row 918).
2. Sharp. (INS) is an identity; its finite-s version loses at most the factor 2 of G2 (PROVED, G2).
3. Extensive with the physical constant. The integrand is local and there are 6 b^3 terms, so a decay psi(a) of order e^(-m a) gives the dilute-gas size. The gap-times-count forms lose the multi-particle structure: G1 bounds sum_i r_i^a by r_1^(a - t_0) sum_i r_i^(t_0), and in a gas the count at t_0 is exp(b^3 phi(t_0)) while r_1^(a - t_0) removes only one particle. At beta 2.3 (m_0 = 1.22, GUIDE) Lemma G5 needs m_ev a >= 2 x 110592 x g(a/2; a^3), about 4e3 at a = 10, so a of order 3e3 (GUIDE arithmetic). (Z0)+(COUNT) is sufficient but cannot be met near the physical seed size.
4. Local. The integrand is one plaquette pair at the seam. A local-to-global method (cluster expansion, Dobrushin-type with good and bad sets, a multi-scale argument) acts on exactly this kind of quantity. Proposition FIB (check 896 D4) excludes only operator inequalities over all fibre tests; a weighted or good-set estimate on (SEAM) is not excluded.
5. Fact tests at the one coupling (ARGUED; made exact where possible in Step 7). U(1) Coulomb: the photon makes the influence of the compactification on the seam a power of a, so psi(a) is not exponentially small (the failure sits in the bulk). Frozen Q_8, 2T: D_ev(a, a) = log n_ev >= log 2 at the frozen limit (n_ev = number of even flat states, at least 2 by check 896 D6), so the theta-integrand must carry an order-one total although each seam plaquette is flat in both gluings: the theta-path has a sharp switch (a global mismatch of holonomies), and a uniform psi fails. The failure sits in the GLOBAL even states, which a local gap (Z0) does not see (check 896 D3). Frozen Z_2: one even flat state; passes, as it should. So (SEAM) binds both the photon and the topological degeneracy, at one coupling, with no worst case.
6. The form is the one the margins measured (cut and reglue; check 919 L111: the time-regluing construction HOLDS on the used geometries). So a GUIDE number exists for it in hot boxes.

What this form does not do (stated now, so it is not claimed later). (SEAM) is a clustering statement in a defect measure at beta 2.3. It is not easier than the mass gap at one size; it is the same content written locally. The proof attempt below must say where it stops.

## Step 4. Crux, stage A: the insertion identity (PROVED here)

### 4.1 Setting (READ inputs)

Spatial box B = b^3, periodic; X = SU(2)^(3 b^3) the slice configurations; x(W) = (1/2) tr W. V(U) = beta * sum over spatial plaquettes of x(U_p). One-step kernel K(U, U') = integral of prod_x dg_x  prod over spatial links l = (x, x + e_i) of exp(beta x(U_l g_(x+e_i) U'_l^(-1) g_x^(-1))) (g = temporal links, Haar). T = e^(V/2) K e^(V/2). Inputs READ from the class (D/library/gap-finishline-opus.md L101, row 667/671 via that table; check 896 L65): T is positive, trace class, commutes with the centre flips C_i, and has a simple top eigenvalue lambda_0 with an even, positive, normalized eigenvector Omega. P_0 = (1/8) sum_k C^k, H_0 = P_0 L^2. Z_0(t) = Tr(T^t P_0) = lambda_0^t (1 + S_ev(t)). psi := e^(V/2) Omega; then <psi, K psi> = <Omega, T Omega> = lambda_0.

### 4.2 The seam kernel

For (U, W) in X^2 (the last slices before the seam of copies 1 and 2) and (U', W') (the first slices after it), theta in [0, 1]:
  K_theta(U, W; U', W') = integral prod_x dg_x dh_x  exp( beta sum_l [ (1 - theta) x(U_l g U'_l^(-1) g^(-1)) + theta x(U_l g W'_l^(-1) g^(-1)) + (1 - theta) x(W_l h W'_l^(-1) h^(-1)) + theta x(W_l h U'_l^(-1) h^(-1)) ] ),
with g = (g_(x+e_i), g_x) and h likewise on each link. It is continuous, bounded and strictly positive on X^4. K_0 = K(U, U') K(W, W') (gluing A); K_1 = K(U, W') K(W, U') (gluing B).
For one spatial link l put delta_l = x(U_l g U'_l^(-1) g^(-1)) + x(W_l h W'_l^(-1) h^(-1)) - x(U_l g W'_l^(-1) g^(-1)) - x(W_l h U'_l^(-1) h^(-1)) (four seam plaquettes; |delta_l| <= 4).

Lemma S1 (centre invariance; PROVED). For every k: K_theta(C^k U, W; C^k U', W') = integral over the change of variables W -> C^k W, W' -> C^k W' of K_theta(U, W; U', W'). Hence the copy-1 seam step
  Nt_theta(U, U') := e^(V(U)/2) [ integral dW dW' psi(W) K_theta(U, W; U', W') psi(W') / lambda_0 ] e^(V(U')/2)
commutes with every C^k.
Proof. Each A-plaquette contains U_l and U'_l^(-1) on the same link; C^k multiplies both by the same sign (or neither). Each B-plaquette pairs U with W' (or W with U'); after W' -> C^k W' (and W -> C^k W) the signs cancel. Haar measure is invariant, V(C^k U) = V(U), and psi(C^k W) = psi(W) because Omega is even. QED

Lemma S2 (endpoints; PROVED). Nt_0 = T (because the copy-2 factor is <psi, K psi>/lambda_0 = 1), and Nt_1 = lambda_0 |Omega><Omega| (because e^(V/2) K psi = T Omega = lambda_0 Omega on both sides).

### 4.3 Proposition INS (the insertion identity; PROVED)

Put Z_theta(a) := Tr( T^(a-1) P_0 Nt_theta ) for a >= 2. Then Z_0(a) is Z_0(a), Z_1(a) = lambda_0^a, and
  (INS)  log(1 + S_ev(a; b^3)) = beta * integral_0^1 dtheta  sum over the 3 b^3 spatial links l of [ E_theta^(a)(delta_l) - E_theta^(inf)(delta_l) ],
where E_theta^(a) is the expectation under the probability measure with density proportional to the integrand of Z_theta(a) (copy 1 a ring of length a, projected on H_0 by the uniform twist average; copy 2 the vacuum half-lines psi), and E_theta^(inf) is the same with copy 1 also replaced by the vacuum half-lines: density proportional to psi(U) psi(W) K_theta(U, W; U', W') psi(U') psi(W').
Proof. (i) Endpoints by Lemma S2: Tr(T^(a-1) P_0 T) = Z_0(a); Tr(T^(a-1) P_0 lambda_0 |Omega><Omega|) = lambda_0 <Omega, T^(a-1) Omega> = lambda_0^a (P_0 Omega = Omega). (ii) Z_theta(a) is a positive integral: write P_0 = (1/8) sum_k C^k and Tr(T^(a-1) C^k Nt_theta) as an integral of positive kernels (every twisted Wilson weight is positive); so Z_theta(a) > 0 and theta -> log Z_theta(a) is differentiable under the integral (the integrand is smooth in theta and bounded with its derivative on a compact space). (iii) d/dtheta log Z_theta(a) = -beta E_theta^(a)(sum_l delta_l): differentiate the exponent of K_theta. (iv) Integrate: log Z_0(a) - log Z_1(a) = log(1 + S_ev(a)) = beta int_0^1 E_theta^(a)(sum_l delta_l) dtheta. (v) Phi_theta := <psi x psi, K_theta (psi x psi)> satisfies Phi_0 = <psi, K psi>^2 = lambda_0^2 = Phi_1, so beta int_0^1 E_theta^(inf)(sum_l delta_l) dtheta = log Phi_0 - log Phi_1 = 0. Subtract. QED

Remarks (PROVED unless marked).
- R1 (symmetry of the reference). K_theta(U, W; U', W') = K_(1-theta)(U, W; W', U'), and psi x psi is symmetric, so Phi_theta = Phi_(1-theta) and E_theta^(inf)(delta_l) = -E_(1-theta)^(inf)(delta_l): the reference part is odd about theta = 1/2. It is an extensive seam free energy (log Phi_theta is of order b^3 for theta in (0, 1)) that integrates to zero. It need not be small pointwise; only the difference in (INS) carries S_ev.
- R2 (one number per link). Spatial translations act on H_0 and commute with T, P_0 and Nt_theta (a translated twist plane is gauge-equivalent to the original on gauge-invariant functions), and so do the cubic symmetries of B; so all 3 b^3 terms of (INS) are equal: log(1 + S_ev(a; b^3)) = 3 b^3 beta int_0^1 Delta_theta(a; b) dtheta, Delta_theta := E_theta^(a)(delta_l) - E_theta^(inf)(delta_l), one link l. (The translation claim for the twisted operators is the central-gauge-transformation step of Lemma LOC, check 896 L218-223.)
- R3 (the finite-s form, no limit needed). The same construction with copy 2 a ring of length s gives D_ev(a, s) = beta int_0^1 E_theta^(a,s)(sum_l delta_l) dtheta; by G2 this is within log(1 + S_ev(s)) of log(1 + S_ev(a)). (INS) is its s -> infinity limit: T^n/lambda_0^n -> |Omega><Omega| in trace norm and K_theta is a bounded continuous kernel.

### 4.4 The crux lemma, now exact

  (SEAM)_psi at (a, b):  sup over theta in [0, 1] of |Delta_theta(a; b)| <= psi.

By R2, (SEAM)_psi gives log(1 + S_ev(a; b^3)) <= 3 b^3 beta psi. (GLUE-FP) at b = 24 a follows from psi <= log(1.1)/(3 beta (24 a)^3): 1.0e-9 at (a, beta) = (10, 2.3); 3.2e-10 at (15, 2.5) (arithmetic). Conversely (GLUE-FP) gives the theta-average of Delta at most log(1.1)/(3 b^3 beta) (from (INS); PROVED). So (SEAM) differs from (GLUE-FP) only by sup versus average over theta.
Reading (ARGUED). Delta_theta(a; b) is the change of one seam observable when the length-a segment is closed into a ring instead of continuing as the vacuum. In a theory with clustering at rate m it is of order e^(-m a) times a prefactor that does not grow with b (the correlation must run once around the ring). The b^3 in (INS) comes from summing it over the seam, which is the dilute-gas count.

## Step 5. Crux, stage B: (SEAM) as a covariance, a local distance, and three averaged local inputs (PROVED here)

Notation. sigma_l = the seam variables that delta_l reads (U_l, U'_l, W_l, W'_l and the four seam temporal links at the ends of l). phi_i = e_i/Omega for the even eigenvectors e_i of T (real, orthonormal in L^2(nu), nu = Omega^2 dU, phi_0 = 1); pbar_n(U', U) = sum over even i of r_i^n phi_i(U') phi_i(U) = (T^n P_0)(U', U)/(lambda_0^n Omega(U') Omega(U)). pbar_n > 0, since (T^n P_0)(U', U) = (1/8) sum_k (T^n C^k)(U', U) and every twisted kernel is a positive integral. (pbar_n is the centre-averaged transition density of the slice chain of row 895 G3.)

Lemma C1 (covariance form; PROVED). For every bounded seam function f and theta in [0, 1]:
  E_theta^(a)(f) = E_theta^(inf)( f pbar_(a-1)(U', U) ) / E_theta^(inf)( pbar_(a-1)(U', U) ),
so Delta_theta = Cov_theta^(inf)( delta_l, pbar_(a-1)(U', U) ) / E_theta^(inf)( pbar_(a-1)(U', U) ).
Proof. Z_theta(a) = integral dU dU' (T^(a-1) P_0)(U', U) Nt_theta(U, U') (copy 1's ring from U' round to U, then the seam step). The (inf) measure is the same integral with (T^(a-1) P_0)(U', U) replaced by lambda_0^(a-1) Omega(U') Omega(U) (this gives Phi_theta/lambda_0 up to the factor lambda_0^(a-1)). The ratio of the two weights is pbar_(a-1)(U', U), and all other factors agree. QED

Lemma C2 (local total variation; PROVED). Let d_l(theta) be the total-variation distance between the laws of sigma_l under E_theta^(a) and under E_theta^(inf), and chi2_l(theta) the chi-square distance between them. Then
  |Delta_theta| <= 8 d_l(theta) <= 4 sqrt(chi2_l(theta)).
Proof. osc(delta_l) <= 8, and |E_1 f - E_2 f| <= osc(f) d_TV. By C1 the sigma_l-marginal of E^(a) has density E^(inf)[pbar | sigma_l]/E^(inf)[pbar] with respect to that of E^(inf); then 2 d_TV = E|density - 1| <= sqrt(chi2) by Cauchy-Schwarz. QED
So (SEAM) is LOCAL INDISTINGUISHABILITY: one link's seam variables cannot tell (to TV accuracy psi/8) whether copy 1 closes into a ring of length a or runs on as the vacuum.

Lemma C3 (time localization; PROVED). Fix an integer d with 1 <= d and 2d <= a - 3. Let Y be copy 1's slice d steps after the seam and Y' its slice d steps before it. Let F_d(Y, Y') = E_theta[delta_l | Y, Y'] (the same under both measures: given Y and Y', the slab Y' -> seam -> Y and copy 2 have one conditional law), and q(Y, Y') = pbar_(a-1-2d)(Y, Y'). Then Delta_theta = Cov_theta^(inf)(F_d, q)/E_theta^(inf)(q). For any spatial region R containing l, with F_d^R = E^(inf)[F_d | Y_R, Y'_R] (Y_R the links of Y in R) and chi2_R the chi-square distance between the laws of (Y_R, Y'_R) under E^(a) and E^(inf):
  |Delta_theta| <= ||F_d - E^(inf) F_d||_(L^2(E^(inf)))  sqrt(chi2_R)  +  E^(a)|F_d - F_d^R| + E^(inf)|F_d - F_d^R|.
Proof. The first identity is C1 with the slab integrated out: under E^(inf) the law of (Y, Y') has the weight Omega(Y) Omega(Y') lambda_0^(...) times the slab weight, under E^(a) the weight (T^(a-1-2d) P_0)(Y, Y') times the same slab weight; their ratio is q up to a constant. Then split F_d = F_d^R + (F_d - F_d^R). The F_d^R part: Cov(F_d^R, q) = Cov(F_d^R, E[q | Y_R, Y'_R]); divide by E q and use Cauchy-Schwarz; E[q | R]/E q is the density of the R-marginals, so its centred L^2 norm is sqrt(chi2_R); and ||F_d^R - E F_d^R||_2 <= ||F_d - E F_d||_2 (conditional expectation contracts). The remainder: E^(a)(G) - E^(inf)(G) for G = F_d - F_d^R, bounded by the two L^1 norms. QED

Reading of C3 (ARGUED). Three inputs, all expectations under the true measures (no supremum over boundaries or exteriors):
  (I1) slab clustering in L^2: ||F_d - E F_d||_2 <= c_1 e^(-m_1 d) (the seam plaquettes forget the slices at time distance d, for typical slices);
  (I2) spatial localization in L^1: E|F_d - F_d^R| <= c_2 e^(-m_2 r) (they depend on those slices only near l, up to distance r);
  (I3) local even mixing: chi2_R(a - 1 - 2d) small (the ring of length a - 1 - 2d leaves the region R of the two slices nearly independent).
(I3) is a local version of the glue half itself, on a region of side about 2r at the shorter time a - 1 - 2d; (I1) and (I2) are clustering statements in the seam geometry. Proposition FIB (check 896 D4) does not turn these into worst-case statements: each is a scalar estimate for one test function under the true law.
What C3 buys. It removes the volume b^3 from the inputs: each input is local and b-uniform, and the b^3 of (INS) is only the count of seam links. What it costs (ARGUED). The rate: with d of order a/4 the bound behaves like e^(-(m_1/4 + m_I3/4) a) instead of e^(-m a), so the size grows by a factor of about 2 at equal rates. And (I3) must be supplied at a smaller scale, so C3 is one step of a multi-scale induction, not a closed bound.

### 5.4 The endpoints of the seam path and its bridge reading (PROVED here)

Lemma E (endpoint values). With u_(a,ev)^t the mean of one time-like seam plaquette in the twist-averaged ring of length a (twist placed off the seam) and u_inf^t its value in the infinite-time box:
  Delta_0 = u_(a,ev)^t - u_inf^t,    Delta_1 = 0.
Proof. A "mismatched" plaquette, for example x(U_l g W'_l^(-1) g^(-1)) at theta = 0, has mean 0: the law is invariant under the gauge transformation k of the slice W' (W'_l -> k_x W'_l k_(x+e)^(-1), h -> h k^(-1) and the next temporal links of copy 2), which does not touch U or g; the Haar mean of k is the zero matrix and x + e differs from x (b >= 2). At theta = 0 both measures are products (ring or vacuum, times vacuum), so E^(a)(delta_l) = u_(a,ev)^t + u_inf^t and E^(inf)(delta_l) = 2 u_inf^t. At theta = 1 gluing B makes copy 1's segment part of the vacuum cylinder, so E^(a) and E^(inf) both see two actual vacuum plaquettes (the B ones) and two mismatched ones (the A ones; the same gauge argument at the slice after U, resp. after W): E(delta_l) = -2 u_inf^t for both. QED
So the seam integrand starts at the static, one-coupling, time-like part of the even D-shape integrand and ends at 0. (SEAM) asks that it stay small in between.

Lemma BR (bridge reading). Let rho = pbar_(a-1)(U', U). Then E_0^(inf)(rho) = 1 + S_ev(a), E_1^(inf)(rho) = 1, and
  log(1 + S_ev(a)) = log E_0^(inf)(rho) - log E_1^(inf)(rho),   d/dtheta log E_theta^(inf)(rho) = -3 b^3 beta Delta_theta.
Proof. At theta = 0, (U, U') are consecutive slices of one vacuum cylinder: their law is the one-step two-slice law pi of row 863 B1, and E_pi[phi_i(U) phi_i(U')] = <phi_i, P phi_i>_nu = r_i; sum r_i^(a-1) r_i over even i. At theta = 1 they lie on two independent cylinders, each with law nu; only i = 0 survives. The derivative is C1 with the exponential family in theta. QED
Reading. The theta-family moves the joint law of copy 1's two seam slices from "neighbours on one cylinder" (the bridge pi of B1) to "independent" (nu x nu), at the one coupling beta, by a local seam deformation; the glue half is the change of log E[rho] along that path, where rho is the even transition density over the ring.

Note on the account (READ SA YM4_sketch_500.tex L6836-6869, credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text). First passage is the scale where the running inverse coupling x_k first enters the reference window g^(-2) <= x <= g^(-2) + B_sharp of a SMALL reference coupling g. So the account stops at weak coupling; the order-one window lies beyond it. The account's objects are untwisted symmetric tori T_ell (READ via gap-finishline-opus.md L127). (INS) reads twisted tori of shape (a, b, b, b) and a seam: it is not on the account's objects. This settles the brief's item "a finite-box gap from the account's own objects at first passage" for this form: the account supplies no input at the seed size (ARGUED; the account's finite boxes at first passage are weakly coupled boxes far below the seed size).

## Step 6. Crux, stage C: the attempt at order one, and where each route stops

What a supplier must deliver (from Steps 4-5). At beta = 2.3, a = 10 to 11, b = 24 a: sup over theta of |Delta_theta(a; b)| <= 1.0e-9 (SEAM); or the three local inputs (I1)-(I3) of Lemma C3 with rates that beat the loss of C3. Each is a clustering statement for the true measure (or its seam deformation) under typical environments, at a scale of about 12 correlation lengths.

### 6.1 Route V: the virial / Feynman-Hellmann face of the endpoint (PROVED part, then the stop)

Lemma V (PROVED). Give the time-like plaquettes the coupling beta_t and the space-like ones beta_s (positive transfer operator for every beta_t, beta_s > 0, same proof as the isotropic case). Then at beta_t = beta_s = beta:
  d/dbeta_t log(1 + S_ev(a; b^3)) = 3 a b^3 (u_(a,ev)^t - u_inf^t) = 3 a b^3 Delta_0.
Proof. d/dbeta_t log Z_0(a) = (number of time-like plaquettes, 3 a b^3) times the twist-averaged mean u_(a,ev)^t (the twisted weights are positive, so the average over twists is a probability mixture, as in check 896 L440-459); d/dbeta_t (a log lambda_0) = 3 a b^3 u_inf^t by the same limit argument as the even D-shape (check 896 L446-452). Subtract; then Lemma E. QED
So the static endpoint value of the seam path is a transport rate in the ANISOTROPY: Delta_0 = sum over even i >= 1 of r_i^a (-d E_i/d beta_t) / (3 b^3 (1 + S_ev)) (Feynman-Hellmann on each simple branch). This is the Euclidean, one-coupling counterpart of row 895's virial identity (check 896 L461-478, Hamiltonian family): the electric part of an excitation's energy is its beta_t-derivative.
Stop V. (INS) needs sup over theta, not the endpoint. Nothing I can prove bounds Delta_theta by Delta_0. In the dilute picture (ARGUED) Delta_theta is proportional to |tau'(theta)|, tau the transmission of one quantum through the partly glued seam (tau(0) = 1, tau(1) = 0); tau' need not be largest at theta = 0. A convexity route fails: log Z_theta(a) and log Phi_theta are both convex in theta (log-Laplace transforms), but their difference log E_theta^(inf)(rho) has no sign of curvature in general. So Route V gives an exact static identity and no bound.

### 6.2 Route B: the bridge (B1) and projective contraction

Lemma BR moves the joint law of copy 1's seam slices from the bridge pi (B1) to nu x nu. A Schroedinger-bridge tool bounds how a bridge's potentials respond to the marginals; the standard quantitative one is Birkhoff-Hopf contraction in Hilbert's projective metric, with rate tanh(Delta/4), Delta = osc(log k). For k_orb the oscillation is extensive (row 863 B2, check 879: r_1 <= tanh(3 beta_t |B|)). Stop B: the contraction rate tends to 1 with the volume; it holds for U(1) as well, so it cannot be the mechanism (READ row 895 6.4 Stop 2, which this repeats in the seam setting).

### 6.3 Route L: Langevin / Poincare structure (the cleanest supplier, conditional)

Conditional statement (ARGUED; standard Helffer-Sjostrand structure, not re-derived here). If a Gibbs measure on a product of copies of SU(2) with a finite-range potential H satisfies Hess H + Ric >= kappa > 0 as quadratic forms (Bakry-Emery), then Cov(f, g) = E[<grad f, (L^(1))^(-1) grad g>] with ||(L^(1))^(-1)|| <= 1/kappa, and the kernel of (L^(1))^(-1) decays exponentially at a rate fixed by kappa and the range. Applied to the doubled-vacuum seam measure E_theta^(inf) (a finite-range Gibbs measure on the same product) with f = delta_l and g = rho, this gives (I1)-(I3) and hence (SEAM) with explicit constants.
Fact tests of Route L (ARGUED). It needs a Lie group (no gradient for Z_2, Q_8, 2T), so it uses what the finite groups lack. U(1) Coulomb: no uniform kappa; the gauge-invariant Langevin gap tends to 0 (row 786 Theorem V, READ through row 899 L345). Both tests pass by construction.
Stop L (READ inputs). The Bakry-Emery condition holds for the Wilson measure only at small coupling: the gauge-invariant Langevin gap is proved for beta_W < 1/4 (8/27 on some tori; READ row 899 L341 citing gap-finishline-opus.md:189), and Shen-Zhu-Zhu prove a strong-coupling result in |beta_W| < N^2/48 (READ via check 901 L11). At beta = 2.3 the condition fails by a factor of about 9 (2.3 against 1/4; arithmetic). A multi-scale version (a Bakry-Emery bound for the renormalized potential along a renormalization flow) moves the curvature condition to the effective action at each scale; it needs control of the flow across the order-one window, which the account does not give (Step 5.4 note: first passage stops at a small reference coupling g). So Route L stops at the convexity of the action at order one.

### 6.4 Route D: good and bad blocks (not excluded by FIB)

Check 896 D4 leaves open weighted estimates with a bad-set term. A good/bad-block version of (I1)-(I2) would ask: (D-good) for blocks of side l_0 with typical exteriors, the block heat-bath contraction for the seam observable is below 1/(connectivity); (D-bad) the probability, uniformly in the outside, that a block is bad is below the percolation threshold of the block lattice. Stop D. (D-good) is (BC-ord1) of row 836 (OPEN, READ row 895 L247): at beta 2.3 small blocks are nearly Gaussian and their coefficient exceeds 1 (READ row 895 L245-246: "the star tends to 2"), so good blocks must be larger than the correlation length, and their coefficient is a large finite computation, not available by hand. (D-bad) needs a Peierls bound for an event of order-one probability at order one. Neither is supplied.

### 6.5 Route A: the account at first passage

Stop A (READ SA L6836-6869; ARGUED). The account's first passage is at a small reference coupling g; its objects are untwisted symmetric tori; (INS), (SEAM) and (I1)-(I3) read twisted tori, a seam and a scale far beyond first passage. The account supplies no input here.

### 6.6 Where the attempt stops (one sentence)

Every route reduces (SEAM), equivalently (I1)-(I3), to one quantitative clustering statement for the true measure at beta about 2.3 on about 12 correlation lengths, in L^2 for typical environments; the routes stop at, respectively, no bound of sup_theta by the endpoint (V), an extensive projective oscillation (B), non-convexity of the action (L), the order-one block coefficient (D), and the end of the account at weak coupling (A). OPEN.

## Step 7. GUIDE check of the algebra, and the fact-test audit of the chain

### 7.1 GUIDE run (decides nothing; checks the algebra of Steps 4-5)

Script: /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/lane920/guide/ins_check.py; log ins_check.log beside it. Model: two-dimensional Z_N lattice gauge theory on a spatial circle of b = 2 links (so x and x + e are distinct sites, as Lemma E needs), exact enumeration of every slice, temporal link and seam variable; theta-integral by 40-point Gauss-Legendre. 0.8 s, 85 MB. The construction is group-blind, so a finite abelian group checks the same algebra as SU(2).
| N, beta, a | log(1 + S_ev(a)) | (INS) integral | reference integral | Delta_0 vs u_(a,ev) - u_inf | Delta_1 | max_theta Delta / Delta_0 |
|---|---|---|---|---|---|---|
| 4, 0.7, 2 | 1.638927412218e-04 | 1.638927412237e-04 | -3e-17 | 4.3206652386e-04 vs ...82e-04 | -4e-14 | 0.998 |
| 4, 1.5, 3 | 4.301032666916e-03 | 4.301032666909e-03 | -1e-16 | 4.0312195396e-03 vs ...97e-03 | 7e-14 | 0.998 |
| 4, 3.0, 4 | 1.848259934711e-01 | 1.848259934711e-01 | -2e-17 | 3.3689996574e-02 vs ...74e-02 | 7e-14 | 1.585 |
| 6, 2.0, 3 | 2.312535046040e-03 | 2.312535046039e-03 | -4e-17 | 1.5438728726e-03 vs ...27e-03 | 1e-13 | 0.998 |
| 2, 1.0, 3 | 1e-15 (even sector = vacuum only) | -8e-17 | 2e-16 | 0 vs 0 | 0 | (both 0) |
Also: Z_theta(0) = Z_0(a), Z_theta(1) = lambda_0^a, Phi_0 = Phi_1, Phi_0.3 = Phi_0.7 (R1), E_0^(inf)(rho) = 1 + S_ev(a) and E_1^(inf)(rho) = 1 (Lemma BR), all to 12 digits.
Readings (GUIDE). (1) No algebra error was found in (INS), Lemma E, Lemma BR or R1. (2) The endpoint does NOT always dominate: at (N, beta, a) = (4, 3.0, 4), Delta at theta = 0.5 is 4.00e-02 against Delta_0 = 3.37e-02, ratio 1.58. This refutes, in a member of the class, the hope that sup_theta Delta_theta = Delta_0 (Stop V stands). (3) Delta_theta falls to 1e-6 to 1e-11 near theta = 1 in every case.

### 7.2 Fact tests of the chain (target (GLUE-FP) via (INS) and (SEAM))

- U(1) Coulomb (must fail). PROVED part: sup_theta |Delta_theta| >= |Delta_0| = |u_(a,ev)^t - u_inf^t| (Lemma E; theta = 0 is in the range). GUIDE part: for a photon gas the thermal excess of the time-like plaquette is a power of 1/a (about a^(-4)), not exponentially small, so (SEAM) at psi = 1e-9 and a = 10 fails at its static endpoint already. The failure sits in the bulk (clustering), at the one coupling. Row 786 proves only the Langevin face (READ through check 896 L427); the photon values are GUIDE.
- Frozen Q_8 and 2T (a proof must use what they lack). PROVED given check 896 D6 (READ): at large beta on the fixed box, S_ev(a; b^3) >= 1/2, so by (INS) sup_theta Delta_theta >= log(3/2)/(3 b^3 beta) > log(1.1)/(3 b^3 beta): (SEAM) at the GLUE level fails. ARGUED: in Lemma C3 the failure sits in (I2), because F_d depends on the global flat class of the boundary slices, not on their links near l. So a proof of (SEAM) must exclude a non-local even variable of the seam measure; Route L does it by needing a gradient (a Lie group).
- Frozen Z_2 (need not fail). Lemma Z2-c (READ check 896 L157-168): S_ev -> 0 on the fixed box; (INS) is then small. Consistent; nothing in the chain forces a failure.
- No worst case. (SEAM) and (I1)-(I3) are expectations under the true laws (PROVED by inspection of the statements). The caps 2/3, 0.775, 4 G_3 = 1.0109 and (AN1) concern sup-over-environment statements and do not apply to them; they reappear only inside Route D's (D-good).
- The transition points (U(1) 1.01, Z_2 0.44, Q_8 1.15, 2T 2.15; GUIDE) do not enter: the chain is at one coupling.

