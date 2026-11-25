# Check of library/gap-mech-selective-fact-neon.md (FINISH row 1546)

Checker: Claude (Opus 5.5). Target: row 1538, author gemini-4-neon-xhigh via agy.

## Plan
1. Read GOAL.md, FINISH.md Rules and Working efficiently.
2. Read the prior checks 1535, 1540, 1543 and the relevant parts of rows 1530, 1536, 1532, 1386 (Proposition NEG, Remark STAB).
3. Read the target in ranges; record statements and line numbers.
4. Decisive outcome: what is new.
5. Line-by-line checks: Prop 4.1, Thm 1 (I), Thm 1 (II), Thm 2 (2a)-(2c) with Lemma 2.5, Thm 3.
6. Physical-units content of Theorem 1 against NEG and STAB.
7. Verdicts and RESULT line.

## Decisive outcome: what is new relative to rows 1530/1535, 1536/1540, 1532/1543

Provenance: Claude (Opus 5.5), by hand, lane checkout as read 2026-11-25; no numeric run, no Lean; not an audit.

New, and holding after the corrections below:
1. An intrinsic observable. W_R(U) is a function of the Wilson links and seam signs only (no auxiliary Gaussian,
   unlike row 1530's X_R), gauge invariant and invariant under centre slab flips. Its expectation is proved
   two-sided Theta(1) for 4 <= R <= beta_K^{1/2000} (untwisted, untruncated; all sixteen twisted tori for the
   bounded version), by a Wilson-to-Gaussian comparison: E W_R = E_free W_R + O(beta_K^{-1/200}) (Lemma 3.1).
2. The application of the diluted open-box relative-entropy comparison to a clipped quartic observable, with
   volume-free Lipschitz constants (Lemma 3.1). The comparison method itself is on file (row 1151, lines 313-317
   of library/gap-solve5-astra62.md; rows 1231, 1283) and is not credited for Lemma 2.3.
3. A free adjoint-Higgs computation (Lemma 2.5 (4)) and its Wilson transfer (Theorem 2 (2c)), the latter resting
   on a sketched Lemma 2.3 (3).

Not new:
- Prop 4.1 is a weaker form ((1+beta)^2) of row 1141 (2), which check 1535 already verified on all seam-signed
  tori; the note says the (1+beta) form is known only untwisted, which is out of date.
- Theorem 1 (II) and Theorem 3 are the bare-H_U screening of row 1530's stopping statement and row 1536
  Theorem 3 (checks 1535, 1540), dimension-blind, for a new observable.
- The selectivity is the same as before. U(1): the bracket is zero (built in). 5D: E W_R = Theta(R^{8-2d}), the
  free mode count, the square of check 1535's R^{4-d} (5D lower bound c/R^2 by the same proof; d = 3 grows like
  R^2). Adjoint Higgs: passes only with the W mass at the cutoff (kappa = kappa_0 beta), where the model is abelian
  at R >= 4; for any sub-cutoff W mass Part (I) holds there too (the note's Section 5.1).
- No content in physical units: R a_K <= beta_K^{1/2000} a_K -> 0, nonempty only for beta_K >= 4^2000. Does not
  escape Proposition NEG (a), (b) or Remark STAB (small-field, improves with beta). No consumer. Same verdict as
  checks 1535, 1540, 1543.

Defects found: Prop 4.1 step 3 (partition-function bound needs h_j ~ beta; corrected with an h-dependent radius,
conclusion unchanged); Lemma 2.2 (2.7) and (2.8) wording (tree fix, plane type); Lemma 2.3 (3) and the SU(N)
extension are sketches labelled PROVED; Section 6.1's claim to resolve NEG FAILS; the threshold wording at line 49.

## Progress log
- Step 1 started.
- Step 1 done: GOAL.md, FINISH.md Rules / Working efficiently, FINISH rows 1530-1546 read.
- Step 2 done: checks 1535, 1540, 1543 read in full; row 1386 Proposition NEG, Remark STAB, requirements (a)-(i), filter (t1)-(t5) read (library/gap-mech-direction2-fable.md lines 188-262, 300-320, 355-370).
- Step 3 in progress: target read in ranges. Structure: Sec 1 (setup, W_R, Lemma 1.1) L52-111; Sec 2 Lemmas 2.1-2.5 L112-298; Lemma 3.1 L299-381; Prop 4.1, Thm 1, Cor 4.2 L382-455; Thm 2 L456-505; Thm 3 L506-530; tables L531-558.
- Steps 3-7 done: target read in full in ranges; notes per part below; verdict table and RESULT at the end. Status: done.

## Section 1 notes (lines 52-111)
- W_R (1.8)-(1.11) is a function of (Ad U_e, sigma_p U_p) only: no auxiliary field. HOLDS.
- Lemma 1.1 (1) gauge covariance of F, D_U^* F, H_U, A^(R), J, Phi: checked; HOLDS.
- Lemma 1.1 (2) centre neutrality: a centre translation flips all j-links on a slab x_j = c (all times); every
  plaquette contains 0 or 2 of them, Ad(-I) = I. HOLDS.
- Lemma 1.1 (3) seam moves: flipping d-links at x_j = 0, x_d = 0 moves the (j,d) seam from x_j = 0 to x_j = n-1
  (the note says "to x_j = 1"; direction immaterial); flipping j-links at x_j = 0, x_d = 0 moves it from time 0
  to time -1. (k,d) and (j,k) faces contain 0 or 2 flipped links. HOLDS (same as check 1540).

## Proposition 4.1 (lines 386-408)
- Step 1, (4.2): u2 x v = (a b1 - b alpha) n + |u2|... computed: |u2 x v|^2 = (a beta1 - b alpha)^2 + |u2|^2 gamma1^2
  (exact, not only >=). The 2x2 form [[b^2, -ab], [-ab, |u1|^2 + a^2]] has det b^2 |u1|^2 = |u1 x u2|^2 and trace
  |u1|^2 + |u2|^2 <= 2, so lambda_min >= |u1 x u2|^2 / 2; gamma1^2 coefficient >= |u1 x u2|^2. Times 4 gives
  2 |u1 x u2|^2 |v|^2. HOLDS. (Same bound as row 1536's coarse pin, check 1540: lambda_min >= det/trace.)
- Step 2, figure-eight pairs: e1(x) is the 1-edge at x+e2, e2(x) the 3-edge at x+e4. A face with a 1-edge and a
  3-edge is a (1,3) face, needing (x'+e4) - (x+e2) in {0, e1, -e3, e1-e3} + 4Z^4-shifts: coordinate 2 is -1 mod 4,
  impossible. Two 1-edges (or two 3-edges) of distinct centres differ by >= 3 (with the stated wrap rule; v = u can
  be 2 mod 4, e.g. l = 1024: u = 2 b^K; centres 0,...,v-2 keep the wrap difference -2). The other links of p1(x),
  p2(x) are not in E_ind. So the Wilson weight factorizes over E_ind given the rest. HOLDS.
- Step 3, conditional law: each link in 6 faces; staple sum is a quaternion of norm <= 6, seam signs absorbed;
  h_e <= 6 beta; U_p is a left/right translate of U_e^{+-1}, so a tilt with the same h. HOLDS.
- Step 3, probability bound: FAILS AS WRITTEN, HOLDS AFTER CORRECTION. First failing line: "the partition
  function obeys int e^{-h_j(1-chi)} dg <= C_1 (1+h_j)^{-3/2} <= C'_1 r_0^3". The second inequality needs
  1 + h_j >= c(1 + 6 beta); only 0 <= h_j <= 6 beta is known (staples can cancel; h_j = 0 gives Z = 1 while
  r_0^3 ~ beta^{-3/2}). Then the stated lower bound e^{-1/32}(900/(3 pi)) r_0^3 / Z on Pr(|u_1| >= r_0) is of
  order ((1+h_j)/(1+6beta))^{3/2}, not absolute.
  Correction (checked here): run the same ball argument with the h-dependent radius rho_j := 1/(40 sqrt(1+h_j))
  in place of r_0. Then h_j (10 rho_j)^2 / 2 <= 1/32 still; Z <= C_1 (1+h_j)^{-3/2} = C_1 40^3 rho_j^3 (Laplace:
  1 - cos t >= 2t^2/pi^2, sin^2 t <= t^2); the ball volume >= (1000/(3pi)) rho_j^3; the bad volumes are
  (32/(3pi)) rho^3 and (25/pi) rho^3 exactly as in the note (the theta-spread is <= 10 rho/0.85 < 25 rho). So
  Pr(|u_1| >= rho_1) >= p_0 and Pr(|u_2 x u1hat| >= rho_2 | g_1) >= p_0, p_0 absolute. Since h_j <= 6 beta,
  rho_j >= r_0, so |u_1 x u_2| >= rho_1 rho_2 >= r_0^2 with probability >= p_0^2. Conclusion unchanged.
  (A naive max-density bound would not do for g_2: C(1+6beta)^{3/2} r_0^2 grows like beta^{1/2}; the
  localized ball argument is needed.)
- Hopf measure (1/(2pi^2)) sin a cos a da dtheta dphi and {|u_2 x u1hat| < r} = {sin a < r}, Haar mass r^2:
  HOLDS. Conditional independence of g_1, g_2 and of the xi_x across centres given the outside links: HOLDS.
- Step 4: Hoeffding exp(-2N (p_0^2/2)^2) = exp(-p_0^4 N/2): HOLDS; N >= c_1 s^4 = c_1 C_k^4 log(2+n) gives
  n^{-k-4}; <= n^4 blocks; delta_0 = p_0^2 c_1 / 32. HOLDS. Telescoping |(I - Ad U_p) s(x)|^2 <= 4 E_p(s):
  HOLDS; edge-disjoint supports: HOLDS. Neumann gap of a path of L <= 2s vertices, 4 sin^2(pi/(2L)) >= s^-2:
  HOLDS; Kato | |s(u)| - |s(v)| | <= |s(u) - Ad U s(v)|: HOLDS. Averaging and the block sum: HOLDS.
  1/r_0^4 = 40^4 (1+6beta)^2, s^2 = C_k^2 sqrt(log(2+n)). (4.1) HOLDS on all sixteen tori, every beta > 0,
  constants independent of beta, z, v.
- Novelty: (4.1) is a weaker form of row 1141 (2) (c/(1 + beta + (log(2+n))^{1/2}) in d = 4), and check 1535
  ("Use of row 1141 (2)-(7) under seam signs - HOLDS") already established row 1141 (2) on every seam-signed
  torus. The note's statement that the 1 + beta form is known only on the untwisted torus (lines 384, 433) is
  out of date. Prop 4.1 is dimension-blind (the same pairs and blocks work in 5D with s ~ (log n)^{1/5}).
  NOT NEW.

## Theorem 1 (II) (lines 425-445)
- ||(D_U^* F)_mu(x)|| <= 2(d-1) = 6 (3 values of nu, two unit-norm terms each): HOLDS.
- ||A_2||_2 <= sup_{l >= gamma} e^{-R^2 l}/(l + R^-2) * 6 sqrt V <= 6 R^2 e^{-gamma R^2} sqrt V: HOLDS.
- ||A_1||_inf <= 6 R^2 from Kato domination (walk expansion of e^{-tH_U} and Laplace transform; row sums of the
  scalar kernels are 1 and R^2): HOLDS. ||[X,Y]|| = 2|x cross y| <= 2|x||y|: HOLDS.
- ||J||_2 <= 72 beta R^4 e^{-gamma R^2} sqrt V; W_R <= 5184 beta^2 R^12 e^{-2 gamma R^2}: HOLDS (4.5).
- Off the event, (2.2) gives ||Phi(x)|| <= 72 beta R^6 pointwise: HOLDS; (4.6) HOLDS; at R = u, k = 16:
  C beta^2 n^-4: HOLDS; fixed beta, R >= C_0 log n: exponent >= c (log n)^{3/2}, so the n^-16 term dominates: HOLDS.
- Scope: (II) is the heat-kernel factor e^{-R^2 H_U} of the definition (1.8) times the gap of Prop 4.1. It is
  dimension-blind (Prop 4.1 runs in 5D unchanged) and it is the mechanism of row 1530's stopping statement
  ((5): X_{R_K} -> 0 at R_K ~ u/16, check 1535) and of row 1536 Theorem 3 (check 1540: "spectral gap ... the
  argument is dimension-blind"), here for a different observable. With row 1141 (2) (seam-signed by check
  1535) the bound improves to (1+beta) in place of (1+beta)^2 on all sixteen tori. NOT NEW as a mechanism; new
  only as the bound for this particular observable, which nothing on file consumes.

## Lemma 2.1 (lines 118-136)
- (2.1) Kato domination by the walk expansion; Schur row sums 1 and R^2; (2.2): HOLDS.
- (2.3): E e^{alpha X_mu} = exp(2t(cosh alpha - 1)) <= exp(2 t alpha^2) for |alpha| <= 1; torus images only help;
  2 alpha^2 = 1/(8 d R^2) <= R^-2 / 2; the three bounds: HOLDS.
- (2.4) Dirichlet localization (resolvent and Duhamel identities, boundary sites at distance >= L): read; the
  structure is standard and the bound has slack (beta^-60 tails); accepted as HOLDS at the level of the stated
  estimate. Only Part (I) uses it.

## Lemma 2.2 (lines 140-164)
- (2.5): tree gauge, chord balls, seam count, layer integration: same as row 1530 (7) (check 1535). HOLDS.
- (2.6) chessboard on the untwisted even torus: RP for link-bisecting and site planes (Osterwalder-Seiler);
  Markov on A >= V eta^2; V-th root. HOLDS (untwisted only, as stated).
- (2.7) adjoint Higgs: unitary gauge; Cartan-coset Haar measure flat in (theta, w) (Hopf: |z_2|^2 uniform,
  both phases uniform; unimodular change): HOLDS; (1/2)|e3 - Ad(U)e3|^2 = 2|w|^2: HOLDS (sigma_3-component of
  C is 0). Lower bound: HOLDS. Upper bound: correct only if the residual U(1) tree fix is undone first (each
  tree-fixed spatial link is otherwise a 2D disc integral, not a full Haar integral bounded by C beta^{-3/2}).
  Undoing it is exact (gauge invariance), so (2.7) HOLDS AFTER CORRECTION (wording: state that the upper bound
  is computed without the tree fix).
- (2.8): first bound as (2.6): HOLDS. Second bound: the edge (0, e_1) lies inside the site planes x_2, x_3, x_4 =
  const, so it is moved in directions 2-4 by link-bisecting planes, not site planes; with that change (RP holds
  for both kinds) the dissemination fills all direction-1 edges, and kappa_0 beta sum |w|^2 <= S_AH/2. HOLDS
  AFTER CORRECTION (plane type).

## Lemma 2.3 (lines 166-233): open-box relative entropy
- Bad-cube probabilities: (1) union bound with (2.6): HOLDS. (2) Markov with (2.5), clean cubes have no seam
  face: HOLDS. (3) with (2.8): HOLDS.
- (2.16), (2.17): Im U_p = (da)_p + O(r^2) (BCH commutators), so 1 - chi(U_p) = |da|^2/2 + O(r^3); Jacobian
  (sin|a|/|a|)^2 = 1 + O(r^2); per cube error C h^d (beta r^3 + r^2): HOLDS (crude but sufficient).
- Faddeev-Popov insertion: Z_W >= N / I(I) by gauge invariance of A (seams included) and I(U) <= I(I): HOLDS.
  Diamagnetic inequality: the note's RP / maximizer argument is acceptable; an independent two-line proof:
  expanding e^{eps beta chi} = sum c_j chi_j (c_j >= 0), each term is Tr(D(U) P) with P the product of vertex
  invariant projectors, and |Tr(D P)| <= Tr P (D unitary). HOLDS.
- Step 3 (Gibbs lower bound on N): trial X ~ nu_num, U_e = exp(i phi(X_e)/sqrt(beta)); E|X_e|^2 <= 3/eps (norm
  of (d^*d + eps)^-1); Jacobian and Haar-density errors C/(eps beta); energy errors beta^{-1/2} eps^{-3/2},
  1/(beta eps^2), 1/(beta^2 eps^3); seam faces 2 beta each: HOLDS.
- Step 4 (upper bound on I(I)): dropping edges raises I; bad-spin event via a tree through the bad edge, factor
  e^{-C_* h^d}, beats one missing tree factor (eps beta)^{3/2}: HOLDS. BCH: the cubic term of
  1 - chi(e^{i th_x} e^{-i th_y}) vanishes ((th_x - th_y).(th_x x th_y) = 0), the third-order BCH term is
  O(|th|^2 |Dth|): error C h^{2d+2}/(eps beta) per edge: HOLDS.
- Step 5: Jensen with the product trial (boundary faces E|dX_p|^2 <= 48/eps): HOLDS. Tree-gauge change of
  variables unimodular; integrating the gradient part gives Z_spin exp(-(eps/2)|X^trans|^2); pushforward of the
  chord Gaussian to ker d^* gives E|X^trans|^2 = 3 Tr((d^*d)|_{ker d^*})^{-1}: HOLDS. Cubical Kunneth form of the
  1-form Hodge Laplacian (edge factor m_mu >= 1, vertex factors m_nu >= 0), trace <= C_d h^d (d >= 3): HOLDS.
  Bookkeeping dV = N_clean (M_h + h^d - 1) + E_rem: the (2 pi^2 beta^{3/2}) factors cancel to E_rem log(C eps beta),
  i.e. the V log(beta)/h term: HOLDS. The factor 2 per cube adds N_clean log 2 <= V log 2 / h^d, not listed in
  (2.18) but smaller than the listed terms.
- KL by data processing: the conditional density bound (drop boundary faces, integrate bad cubes and remainder
  links, divide by Pr(S = I)) and the sum over I giving H(S) + log(Zhat^N / Z_W) + C V (beta r^3 + r^2) +
  C' h^d E|C \ S|: HOLDS. Arithmetic for (1), (2), (3): HOLDS ((1): beta r_h^3 ~ beta^{-5/16} (log beta)^{3/2};
  (2): C/h = beta^{-1/30}, (eps h)^{-1} = beta^{-1/60}).
- Verdict: Lemma 2.3 HOLDS (one omitted lower-order term). It is a per-site relative-entropy comparison of the
  Wilson law on cubes of side beta^{1/16} (beta^{1/30} twisted) with the free open-box Gaussian, at error
  beta^{-1/32} (beta^{-1/60}). It is a small-field / weak-coupling statement of the same kind as row 1530 (7) and
  row 1536's good-cube estimates (checks 1535, 1540): it improves with beta (Remark STAB).

## Lemma 2.4 (lines 235-250)
- P_open Pi = P_open, P_open Pi P_per = Pi P_per, so P_open P_per = Pi P_per and
  ||P_per - P_open||_HS^2 = Tr P_open - Tr P_per + 2 Tr((I - Pi) P_per). Tr P_per = 3(d-1)(V-1) (ker d on
  1-forms = gradients plus d harmonic forms); Tr P_open = 3 N_clean M_h. (2.19) HOLDS. P Z with P the
  projection onto im d is the law of d a~ under the chord Gaussian (covariance d (d^T d)^-1 d^T): HOLDS.
  (2.20) Proca: B injective for m_W > 0, equal traces: HOLDS.

## Lemma 2.5 (lines 252-297): the dimension step
- (2.21): A^free covariance c(k) P_perp (transverse propagator 1/k^2 times the multiplier e^{-2R^2 k^2} k^4/
  (k^2 + R^-2)^2); Parseval with J(p) = (1/V) sum_k [A_1(k), A_2(p-k)]; Wick: disconnected pairing has f^{aac} = 0,
  direct pairing + C_G, crossed pairing - C_G; C_SU(2) = sum f^2 = 4 * 6 = 24 for T_a = i sigma_a: HOLDS.
  (1/2) Tr(A adj B) in [0, 1] for 2x2 0 <= A, B <= I: HOLDS (adj B has eigenvalues 1 - t, 1).
- (2.22) lower bound: dual-point counts need n_j >= 8 pi R (given n >= v >= 32R): HOLDS; every numeric
  inequality re-derived: p^2 <= 1/(4R^2); k^2 in [8/(pi^2 R^2), 65/(8R^2)]; c(k) >= e^-18 R^2/125;
  M(k) >= 27/32; (p-k)^2 in [9/(20R^2), 85/(8R^2)]; c(p-k) >= e^-22 R^2/320; t <= (1/2)/(1/2 + 9/20) = 10/19,
  adj M >= 9/19; trace factor > 1/3; R^-8 R^4 R^2 R^2 = 1; c_* as stated. HOLDS.
- (2.26) upper bound: c(k) <= (R^2/4) e^{-2R^2 k^2}; (2.25) per-coordinate triangle inequality; Cauchy-Schwarz
  in k; each normalized momentum sum <= C R^-d. Result C_G C_d R^{8-2d}: HOLDS.
- (2.24) adjoint Higgs Gaussian: W propagator 1/(k^2 + m_W^2), c^(1) <= e^{-2R^2 k^2}/m_W^2, photon-photon bracket
  zero, W-gamma and W-W pairs, result C(1/(m_W^2 R^2) + 1/(m_W^4 R^4)): HOLDS. m_W^2 = 4 kappa_0 in LATTICE units
  (2 kappa |w|^2 = 2 kappa_0 |a~_perp|^2).
- Where d enters: only through the two momentum sums (1/V) sum_q e^{-alpha R^2 q^2} ~ R^-d, against R^8 from the
  four scale-R multipliers. The same box argument in d = 5 gives the matching lower bound c R^{8-10} = c/R^2.
  So E W_R^free = Theta(R^{8-2d}) in every d >= 2 (it GROWS like R^2 in d = 3 and R^4 in d = 2). This is the free
  mode count: the square of check 1535's R^{4-d} (the observable is quartic in the free field), i.e. classical
  power counting of a dimensionless composite of the coupling g^2 of mass dimension 4 - d. It is NOT a property
  specific to four-dimensional Yang-Mills beyond that classical marginality.

## Lemma 3.1 (lines 303-380): Wilson-to-Gaussian bridge
- Step 1 translation reduction to S_in: HOLDS (Lemma 1.1 (3); untwisted and AH tori are translation invariant).
- Step 2 items 1-4: Duhamel and resolvent changes in l^inf are each <= R^2 * 8d r_h * R^2 ||f||_inf with
  ||sqrt(beta) D^*F||_inf <= C sqrt(beta) eta_h; F - da = O(r_h^2); (3.4) exponents re-derived (r_h = C beta^{-7/16}
  (log beta)^{1/2}, R^8 <= beta^{0.004}): HOLDS. (3.5): HOLDS.
- Step 2.5 leak bound (3.5'): structure checked (Tonelli, e^{-alpha L/2} <= beta^-30, bad cubes carry independent
  Gaussian draws with E||dG|| <= sqrt 3); not every constant re-derived. Accepted.
- Step 3 Lipschitz constants: sup sqrt(x)/(x + R^-2) = R/2 and Cauchy-Schwarz on d^*: (R/2); clipped bracket
  2 M_1 R; Phi: 2 M_1 R^3; (3.6), (3.7): HOLDS.
- Step 4: (3.8) Donsker-Varadhan with Gaussian concentration for psi(d a~) = psi(P_open Z), Lipschitz constant
  L_psi in Z since ||P_open|| = 1: HOLDS; L_psi ~ V^{-1/2} against KL ~ V Delta gives a volume-free error.
  (3.9): HOLDS.
- Step 5: variance of A~_mu(y) <= C R^{2-d}; degree-2 hypercontractivity ||xi||_{2q} <= (2q-1)||xi||_2; tails
  beta^-20; (3.10): HOLDS.
- Assembly, Case (1): bad cubes C beta^2 R^12 p_bad; good cubes with and without violations; the exponent
  arithmetic (R^{12+3d/2} (log)^{d+3} beta^{-1/64} <= beta^{-1/200} at R <= beta^{1/2000}; g_2 Lipschitz error
  R^{8-3d/2} beta^{-1/64}): HOLDS. Case (2): HOLDS. Paley-Zygmund lower bound for W^bd (||Phi_a||_4 <= 3||Phi_a||_2,
  Minkowski, E X^2 <= 81 (E X)^2): HOLDS.
- Verdict: Lemma 3.1 HOLDS as checked (the leak constants in (3.5') accepted at the structural level). It is a
  weak-coupling (perturbative) comparison at scales R <= beta^{1/2000}, built on Lemma 2.3.

## Prior work for the comparison machinery (grep)
- library/gap-solve5-astra62.md (row 1151, checked by 1152), lines 313-317: relative entropy of the true density
  against product open-box laws at most exp(C V Delta_b), bad boxes replaced by diluted Gaussians, Gaussian
  concentration for Lipschitz tests of the linear curls. Row 1231 (library/gap-solve26-astra62.md line 105) and
  row 1283 (library/gap-solve33-astra62.md line 171) carry the same diluted open-box relative-entropy bound.
  The target credits row 1231 for Lemma 2.4 but not row 1151 for the method of Lemma 2.3 / 3.1. So the
  Wilson-to-Gaussian machinery is a re-derivation (with a different normalizer route: Faddeev-Popov +
  diamagnetic + Gibbs) of a method on file; its application to the quartic clipped observable W_R is new.

## Theorem 1 (I) (lines 413-433)
- (1): Lemma 2.5 (2) + Lemma 3.1 (1), c_4 = 12 c_*, C_4 = 48 C_*; number of dyadic scales in [4, beta^{1/2000}]
  ~ log_2(beta)/2000: HOLDS.
- (2): Lemma 3.1 (2) + W_R >= W_R^bd: HOLDS.
- (3) SU(N): C_G = 2N^2(N^2-1) re-derived for <X,Y> = (1/N) tr(X^dag Y) (T_a = i sqrt(2N) t_a, F_abc =
  -sqrt(2N) f_abc); positivity of the character expansion of e^{t Re tr/N}: HOLDS. The rest ("every step extends
  verbatim with N-dependent constants") is a sketch: ARGUED, not checked line by line.
- W_R uses no auxiliary field (function of Ad U_e and sigma_p U_p only) and is invariant under the path-integral
  centre transformations (Lemma 1.1 (2)): HOLDS. Note it is a space-time functional, not a time-zero state, so
  "centre-neutral" means invariance under slab flips, not membership in the range of P_0.
- Two-sided bound on 4 <= R <= beta_K^{1/2000}: HOLDS (via Lemmas 2.3, 2.5, 3.1 as checked above). Scope:
  the window is nonempty only when beta_K^{1/2000} >= 4, i.e. beta_K >= 4^2000 ~ 10^1204, so n >= exp(10^1204 / B_0).
  Theorem 1 (I) says E W_R = E_free W_R + O(beta^{-1/200}): it is the free-field value, transported to Wilson by
  a weak-coupling comparison at scales far below beta^{1/16}.

## Theorem 2 (lines 460-485)
- (2a) U(1) and U(1)^m: [X,Y] = 0, W_R = 0 identically; H_U = H_0 has the constant zero mode: HOLDS, trivially
  (built into the observable, as in checks 1535, 1540, 1543).
- (2b) 5D: Lemma 2.5 (3) (R^{8-2d} = R^-2) + Lemma 3.1 (1) at d = 5 (exponents checked: R^{19.5} beta^{-1/64});
  dyadic sum sum 4^{-j} < inf; twisted via W^bd <= W and (3.2): HOLDS. The same box argument gives the matching
  5D lower bound c/R^2, so the 4D/5D split is exactly the free mode count R^{8-2d} (square of check 1535's
  R^{4-d}); it is not a property specific to four dimensions beyond classical marginality, and in d = 3 the same
  proof gives growth R^2.
- (2c) adjoint Higgs at kappa_K = kappa_0 beta_K: Lemma 2.5 (4) HOLDS; Lemma 2.2 (2) HOLDS AFTER the two
  wording corrections above; the adjoint-Higgs case of Lemma 2.3 (3) is a four-line sketch ("Apply the identical
  5 steps ...") - structure plausible (Proca components need no gauge fixing; residual U(1) uses the XY
  diamagnetic inequality), constants not written, so ARGUED rather than PROVED. Given it, (5.4) HOLDS.
  Scope, decisive for selectivity: kappa = kappa_0 beta puts m_W^2 = 4 kappa_0 at the LATTICE scale, so the W
  bosons are frozen at the cutoff and the comparison model is abelian at every R >= 4: (2c) is the (2a) mechanism
  again. For any adjoint-Higgs model whose W mass is below the cutoff (fixed kappa, as the note's Section 5.1
  says, or fixed physical m_W, where xi_W = 1/(m_W a_K) ~ n >> beta^{1/2000}), Part (I) does NOT fail: Lemma 3.1
  and the free computation give the pure-SU(2) value across the whole window. So Theorem 1 (I) does not separate
  4D SU(2) from the gapless adjoint-Higgs (Coulomb-phase) comparison of row 1386 requirement (c) in any regime
  where the Higgs is a physical field.

## Corollary 4.2 (lines 447-453)
- Non-identity, and the mode localization (lower-bound box at |p| <= 1/(4R), |k| ~ 1/R; modes above
  C_0 sqrt(log R)/R give O(R^-10)): HOLDS. "Growing distance" is in lattice units only: R a_K <= beta^{1/2000} a_K
  -> 0.

## Theorem 3 (lines 518-524)
- (6.1): ((1+beta)^2 + sqrt log n) <= C_1 (log n)^2 on the trajectory; R >= C_0 (log n)^{3/2} gives exponent
  >= k log n; at R = u: C beta^2 u^12 n^-k <= C' n^{13-k}: HOLDS. It is Theorem 1 (I) and (II) placed side by
  side; nothing is proved between beta^{1/2000} and (log n)^{3/2}. Wording error (not a defect of (6.1)): line 49
  says screening sets in "beyond scale R ~ sqrt(beta_K log beta_K)"; the proved threshold is R >> beta_K^{3/2}
  ((1+beta)^2 form) or R >> beta_K (row 1141 (2) form).
- Not new as a mechanism: the screening of bare-H_U scale-R operators at the seed scale is row 1530's stopping
  statement and row 1536 Theorem 3 (checks 1535, 1540).

## Section 6.1 claims
- "Theorem 1 is strictly weaker than (PUR-io) and not equivalent": the comparison is empty. Theorem 1 is a proved
  statement that is not proposed as sufficient for anything, so the rule Equivalent-is-not-progress does not bite
  and there is nothing to be weaker or stronger than. No consumer on file: agreed (grep of FINISH.md and
  library/ for a consumer of a scale-R spin-current or quartic adjoint observable found none beyond rows
  1530-1546 themselves).
- "Theorem 1 directly resolves the obstruction posed by Row 1386 (Proposition NEG)": FAILS. See next section.

## Theorem 1 against Proposition NEG and Remark STAB (physical units on the calibrated trajectory)
- NEG (a) asks for content at physical side L > L_gamma at all late cutoffs. Theorem 1 (I) has range
  R <= beta_K^{1/2000} lattice units, physical size R a_K <= beta_K^{1/2000} a_K -> 0 (a_K ~ l/n, beta_K ~ log n).
  No content in physical units. Theorem 1 (II) at R = u has physical size, but it is a negative (the bare
  observable vanishes there), of NEG's F_id kind, and it is dimension-blind (Prop 4.1 runs in 5D unchanged).
- NEG (b): every proof step of Theorem 1 (I) except the two momentum sums of Lemma 2.5 holds in 5D (Lemmas 2.1-2.4,
  3.1 are stated for d in {4,5}); the d-dependence is the free mode count R^{8-2d}, a count over UV scales of
  the free field, with no carry to the band. The sum over dyadic scales diverges only inside the UV window.
- Remark STAB: the hypothesis of Theorem 1 (I) is plaquette concentration on cubes of side beta^{1/16}
  (Lemma 2.3) and the result improves as beta grows (error beta^{-1/200}, window beta^{1/2000}). At a fixed
  lattice with beta -> infinity the same content (E W_R -> free value, Theta(1) in 4D for R << n) persists, so by
  STAB it cannot by itself imply the seed test. It is a small-field statement of exactly the excluded kind.
- Verdict: Theorem 1 has no content in physical units on the calibrated trajectory; it does not escape NEG (a)
  or (b) or STAB. Same verdict as check 1535 for row 1530 (6) and check 1540 for row 1536 (5).
- Consumer grep (library/*.md, FINISH.md for "paramagnetic", "spin current"): hits are one-loop/Hessian
  discussions (gap-council-rg-fable.md, gap-laptop-solve2-fable.md, gap-brainstorm2-max.md) and the mechanism rows
  1526-1538; none consumes a scale-R spin-current amplitude. The free 4D spin-bubble logarithm is on file: row 1244
  Lemma 2.2 / Prop 2.3 (flat torus), row 1526 Thm 5(a) (check 1527 (iv)), row 1528 (Gaussian W law), row 1529 T2
  ("the shell sum is a logarithm only in d = 4"), row 1530 (6) on typical Wilson backgrounds.

## Verdicts

Provenance: Claude (Opus 5.5), laptop subagent, by hand, against the lane checkout as read on 2026-11-25; no
numeric run, no Lean check; not an audit.

| Part | Verdict |
|---|---|
| Lemma 1.1 (gauge, centre, translation; seam moves) | HOLDS |
| Lemma 2.1 (Kato domination, (2.2), (2.3); (2.4) accepted at the stated level) | HOLDS |
| Lemma 2.2 (2.5), (2.6) | HOLDS |
| Lemma 2.2 (2.7) adjoint-Higgs free-energy upper bound | HOLDS AFTER CORRECTION: undo the residual U(1) tree fix before the layer integration (a tree-fixed spatial link is a 2D disc integral, not a full Haar integral <= C beta^{-3/2}); exact by gauge invariance |
| Lemma 2.2 (2.8) second bound | HOLDS AFTER CORRECTION: move the edge (0, e_1) in directions 2-4 with link-bisecting planes (it lies inside the site planes x_2, x_3, x_4 = const) |
| Lemma 2.3 (1), (2) open-box relative entropy | HOLDS (N_clean log 2 term omitted from (2.18), lower order); method on file (row 1151 lines 313-317, rows 1231, 1283), not credited |
| Lemma 2.3 (3) adjoint Higgs | ARGUED (four-line sketch; structure plausible, constants not written) |
| Lemma 2.4 | HOLDS |
| Lemma 2.5 (2.21), (2.22), (2.23), (2.24) | HOLDS (every numeric bound re-derived); the d-step is the free mode count R^{8-2d}, matching lower bound in 5D |
| Lemma 3.1 | HOLDS (leak constants of (3.5') accepted structurally) |
| Prop 4.1 (4.2) commutator bound | HOLDS |
| Prop 4.1 figure-eight conditional independence | HOLDS |
| Prop 4.1 Hopf-coordinate probability bound | FAILS AS WRITTEN at "int e^{-h_j(1-chi)} dg <= C_1 (1+h_j)^{-3/2} <= C'_1 r_0^3" (needs h_j >~ beta; staples can cancel, h_j = 0 gives Z = 1 >> r_0^3); HOLDS AFTER CORRECTION: use rho_j = 1/(40 sqrt(1+h_j)) >= r_0 in the ball argument; the bad volumes (32/(3pi)) rho^3, (25/pi) rho^3 and Z <= C 40^3 rho^3 give Pr >= p_0 absolute, and |u_1 x u_2| >= rho_1 rho_2 >= r_0^2 |
| Prop 4.1 block Hoeffding and Neumann Poincare | HOLDS |
| Prop 4.1 gap (4.1) on all sixteen tori | HOLDS (after the correction); NOT NEW: weaker than row 1141 (2) ((1+beta) form), which check 1535 established on every seam-signed torus; dimension-blind |
| Theorem 1 (I) (1), (2) | HOLDS; W_R auxiliary-field-free and centre-invariant: HOLDS; window nonempty only for beta_K >= 4^2000 |
| Theorem 1 (I) (3) SU(N) | ARGUED (C_G and the character expansion checked; the rest is "verbatim" sketch) |
| Theorem 1 (II) (4.5), (4.6) | HOLDS; dimension-blind; mechanism on file (row 1530 stopping statement, row 1536 Theorem 3) |
| Corollary 4.2 | HOLDS (distances in lattice units only) |
| Theorem 2 (2a) | HOLDS (trivially: abelian bracket) |
| Theorem 2 (2b) | HOLDS; the 4D/5D split is the free mode count R^{8-2d} (5D lower bound c/R^2 by the same box), the square of check 1535's R^{4-d}; not specific to 4D beyond classical marginality (d = 3 gives growth R^2) |
| Theorem 2 (2c) | HOLDS GIVEN Lemma 2.3 (3) (ARGUED); passes only with m_W at the lattice scale (kappa = kappa_0 beta), where the model is abelian at every R >= 4 (the (2a) mechanism); with any sub-cutoff W mass Part (I) holds in the adjoint-Higgs model too (the note's Section 5.1), so the adjoint-Higgs test of row 1386 (c) is not passed in a physical regime |
| Theorem 3 (6.1) | HOLDS (wording: the screening threshold is R >> beta^{3/2}, not sqrt(beta log beta) as line 49 says) |
| Section 6.1 "resolves the obstruction of Proposition NEG" | FAILS: no content at L > L_gamma (R a_K -> 0); d enters only by the free mode count; STAB-excluded small-field hypothesis |
| Physical-units content of Theorem 1 on the calibrated trajectory | None (Part I: R a_K <= beta^{1/2000} a_K -> 0; Part II: a dimension-blind negative) |


Scope of this check: Lemma 1.1, Lemmas 2.1-2.5, Lemma 3.1, Proposition 4.1, Theorem 1, Corollary 4.2, Theorems 2 and 3 and Section 6.1 were checked line by line; (2.4) of Lemma 2.1 and the leak constants (3.5') of Lemma 3.1 were checked at the structural level only; Lemma 2.3 (3) (adjoint Higgs) and the SU(N) extension of Theorem 1 (I) (3) are sketches in the note and were read, not proved here.

RESULT Check 1546 of row 1538: the positive mathematics HOLDS after corrections (Prop 4.1 step 3 needs an h-dependent ball radius; Lemma 2.2 (2.7)/(2.8) wording; Lemma 2.3 (3) adjoint-Higgs and the SU(N) extension are sketches, ARGUED); new is only an intrinsic, auxiliary-field-free, centre-invariant observable W_R with E W_R = free value + O(beta_K^(-1/200)), two-sided Theta(1) on 4 <= R <= beta_K^(1/2000) via a Wilson-to-Gaussian comparison whose method is on file (row 1151); Prop 4.1 is weaker than row 1141 (2) as already seam-signed by check 1535, Part (II)/Theorem 3 repeat the screening of rows 1530/1536, the 4D/5D split is the free mode count R^(8-2d), the adjoint-Higgs failure needs a cutoff-scale W mass, and Theorem 1 has no content in physical units (R a_K -> 0), does not escape Proposition NEG or Remark STAB, has no consumer, and makes no progress toward (PUR-io).
Checked line by line by Claude (Opus 5.5).
