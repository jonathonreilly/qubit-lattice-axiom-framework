# Check of library/gap-ext-astra.md (FINISH row 791), by Claude Opus 5.5, line by line

- Checker: Claude Opus 5.5, one session, no subagents, 2026-11-12. Cross-provider check of a Codex gpt-6-astra max note.
- Clone read: `/Users/jonreilly/ym4d-lead/clone`, HEAD `79e7f9ad7`.
- File checked (read in full, 845 lines): `.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-ext-astra.md`. The note calls itself FINISH row 789 (line 46). The header uses row 791 as requested.
- Inputs read: `gap-cf-astra.md` in full (row 783); `gap-cf-check-opus.md` in full (row 788); `gap-vortex-astra.md` lines 1-255 (Sections 1-3, (1)-(4), (FQ)); `gap-means-max.md` Sections 4.1-4.9; `gap-skeleton-final.md` 13.16-13.20; `gap-crux-restate.md` lines 135-165 (Lemma J, Ways 2-3); `gap-fusion-astra.md` lines 93-130 and 360-370 (the witness eta).
- Primary source: Kanazawa arXiv:0808.3442v3, Sections 2.1-2.2, read through a page fetch (first half of the page text only). Seiler was not read.
- Method: by hand. No numerical run.

## 1. Section 2: (E3)-(E7)

**(E1)-(E2) setup.** Z_m = int e^(-S_m) dU = e^(-beta N_p) Z^m. HOLDS. With eta' = eta_m (-1)^(1_Sigma), S_m + X_Sigma^m = beta sum_p (1 - eta'_p s_p). So E_(mu_m) W_Sigma = Z_(eta')/Z_m. If 1_Sigma is closed of class v, eta' has class m+v, and R_m(v) = Z^(m+v)/Z^m. HOLDS.

**(E2) equals row 783 (26).** For m = 0 and row 783's Sigma, X = 2 beta H(xi). H depends only on unselected links. The xi-marginal of mu_0 is B_0 dxi/Z^0. HOLDS. *Precision:* this is exact for row 783's Sigma (or any representative that avoids the selected links), not for every representative.

**(E3).** A link sign is central and (-U)^(-1) = -U^(-1). So U_p(T_b U) = (-1)^((delta b)_p) U_p(U), and s_p changes by the same sign. Hence S_eta(T_b U) = S_(eta (-1)^(delta b))(U). U_e -> -U_e is left multiplication by -I, so it preserves Haar measure. Two closed cochains of one class differ by a coboundary. So Z_eta depends only on the class. HOLDS. Credit check: Kanazawa's Lemma 1 (Section 2.2) is stated for general N with z = exp(2 pi i/N) and homologous vortices; the SU(2) sign case is the N = 2 instance. HOLDS.

**(E4).** Each term equals R_m(v) by the setup paragraph. pi is a field-independent probability. HOLDS. The caveat lines 158-161 are correct: T_b does not preserve mu_m.

**(E5).** Disjoint supports give prod_(j in A) W_j = exp(-2 beta sum over the union of eta_m s_p). The indicator of a disjoint union is the sum of indicators, with no cancellation. Its class is |A| v mod 2. So the expectation is Z^m/Z^m = 1 (|A| even, including A empty) or R (|A| odd). HOLDS. The disjointness remark is correct: on an overlap the weight is exp(-4 beta eta s_p), not a sign flip.

**Flat stacks.** The stack {p_34(x): x_3 = t_3, x_4 = t_4} is closed and represents v_34 (row 788, 2a). Distinct (t_3, t_4) give disjoint sets. There are n_3 n_4 of them. HOLDS.

**(E6).** Cov(W_j, W_k) = E W_j W_k - R^2 = 1 - R^2 for j != k. Var(M^(-1) sum W_j) = M^(-2) sum Var W_j + M^(-2) M(M-1)(1 - R^2). HOLDS.

**Projector remark.** E prod_(j in A) P_j = 2^(-|A|) sum_(B subset A) (-1)^|B| E prod_B W = 2^(-|A|)(2^(|A|-1) - 2^(|A|-1) R) = (1-R)/2 for A nonempty. HOLDS. W_j > 1 where X < 0, for example where s_p < 0 on Sigma (m = 0). So P_j can be negative. HOLDS.

**(E7).** The pairing of a 2-cocycle with the 2-cycle T_34(y) depends only on the class. The flat stack at x_3 = x_4 = 0 meets T_34(y) exactly once. So every representative meets each T_34(y) an odd number of times. HOLDS. The a^2 tori T_34(y), indexed by (y_1, y_2), are plaquette-disjoint. So |Sigma| >= a^2. HOLDS. On {s_p > 1/2 for all p}, W_Sigma^0 = exp(-2 beta sum_Sigma s_p) < exp(-beta |Sigma|) <= exp(-beta a^2). A probability average of terms each below e^(-beta a^2) is below it. HOLDS. The set does not depend on Sigma, is open, and contains the identity. Haar measure has full support, and the Wilson density is positive. So it has positive Haar and Wilson measure. HOLDS. The scope sentences (no bound on the integrated mean; transports with densities not excluded) are correct. The pointwise statement holds even for field-dependent pi.

Verdict for item 1: HOLDS, with one precision on which representative makes (E2) equal row 783 (26).

## 2. Section 3: (E8)-(E12)

**(E8) reading.** Kanazawa Theorem 1 prints <W(C)> <= 2 {(1/2)(1 - Z^-/Z)}^(A_C/(L_mu L_nu)), with L_mu = 2^p l_mu and L_nu = 2^q l_nu for p, q in N. The twist is a plaquette stack winding around the two directions not spanned by C. The note's q and exponent match. *Precision:* the printed bound is on <W(C)>, not on |<W(C)>|. The note (and row 778) write the absolute value. That is not what the quoted theorem states. It is immaterial here: the limitation argument needs only the printed form. Also "positive integers u, w" is slightly narrower than the printed p, q in N. ARGUED status is correct.

**Limitation.** From <W> <= 2 q^(A/(n_r n_i)) with positive exponent, q >= (<W>/2)^(n_r n_i/A) whenever <W> > 0. This is a lower bound on q. An upper bound on another loop observable cannot give an upper bound on q. HOLDS. The zero-winding remark refers to row 778's word; I accept it as reused.

**Reflected-product remark.** By the projector identity of item 1, E P_1 P_2 = (1-R)/2 = q for two disjoint insertions. HOLDS. "None follows from repeated Cauchy-Schwarz" is a remark, not a theorem; the note labels it so.

**(E9).** K_beta(g) = e^(beta s(g)) is a class function. For f = tr, (K * f)(U) = int K(W) tr(W^(-1) U) dW. Schur gives int K(W) rho(W^(-1)) dW = c I with c = (1/2) int K chi = int s e^(beta s) dg. HOLDS. Haar invariance under g -> -g makes int s cosh(beta s) = 0, so c_beta = int s sinh(beta s) dg. HOLDS. s sinh(beta s) >= 0 with equality only on the Haar-null set s = 0. So c_beta > 0. HOLDS.

**(E10).** K_beta(-g) = e^(-beta s(g)) = K_(-beta)(g), with eigenvalue c_(-beta) = -c_beta on f. ||f||_2^2 = int |tr g|^2 dg = 1. So the form equals -c_beta < 0. HOLDS. The diagnostic is meaningful: the untwisted kernel is positive definite (its character coefficients are positive), so the sign change is due to the twist. The closing remarks are interpretation and are labelled as such.

**(E11) as quoted.** It matches Proposition R3 (gap-means-max.md 4.5): sum p(1-p) <= 4 theta, theta = 1 - e^(-Delta)(1+eps)^(-2), Delta = a(2e(a,c,d) - e(2a,c,d)), eps = S_ev(a; A). The sum of p is four (R2 (a)). For theta < 1/20, R2 (b) gives eta <= 2Q <= 8 theta. HOLDS. The three candidates come from Theorem R Steps 2-3, which use the cube c = d = a. Those steps need only theta < 1/20, not the full (ES) constants. HOLDS. The exclusion of the diagonal candidate is row 778 Section 3, reused. HOLDS.

**(E12) selection.** In frame 1, X's coordinates are x_3 = m_3 = k_24 and x_4 = m_4 = k_23. So m = v_23 is the point x = (0,0,0,1). On the cube, axis exchange 2 <-> 4 gives Z^(v_23) = Z^(v_34) (TM-tw). HOLDS. The electric group is alpha_per: A_0 = {(0,0),(1,0)}, L = {x_3 = x_4 = 0}. x is not in L, so p_(0,m) <= eta <= 8 theta. HOLDS.

**Z_(chi,m) <= Z_(0,m).** Z_(chi,m) = (1/8) sum_e (-1)^(chi.e) Z^(e+m) <= (1/8) sum_e Z^(e+m) = Z_(0,m), because every Z^(e+m) > 0. HOLDS. Only positivity of the twisted integrals is used; Fourier positivity is not needed for this direction.

**Factors 8 and 64.** sum_chi Z_(chi,m) = (1/8) sum_e Z^(e+m) sum_chi (-1)^(chi.e) = Z^m. Likewise for m = 0. So Z^m/Z^0 <= 8 Z_(0,m)/Z_(0,0) = 8 p_(0,m) <= 64 theta (8 values of chi; drop all but chi = 0 in the denominator). This contradicts (E12). HOLDS. The same bound also excludes the diagonal candidate: there (x_2, x_4) = (0,1) is not in {(0,0),(1,1)}. So (E12) selects magnetic without row 778's exclusion. *Wording:* the "prior dominance inequality" in line 337 is this positivity bound, not Theorem R's dominance rho(sigma) <= rho(sigma|nu).

**OPEN paragraph.** Correct. (E12) needs theta < 1/20 as a hypothesis, so it cannot supply small S or Delta.

Verdict for item 2: HOLDS, with two precisions: the printed Tomboulis-Yaffe form has no absolute value, and "dominance" in line 337 means the positivity bound.

## 3. Section 4.1: (E13)-(E17)

**v_34 minimum zero.** Take g_3, g_4 anticommuting (for example i and j) and g_1 = g_2 = I. The corner-stack construction of row 788 gives a flat twisted field. E_(v_34) = 0. HOLDS.

**(E14).** The map (g_1,...,g_4) -> max_(mu<nu) ||[g_mu,g_nu] - (-1)^(k_*,mu nu) I|| is continuous on the compact SU(2)^4. The minimum exists. A zero would give four SU(2) matrices with central commutator matrix k_*. Row 783 Section 1.3 excludes this (checked in row 788, 1h). So d_* > 0. HOLDS. It is an existence constant; d_* <= 2.

**Peeling identity.** The cut rectangle of T_(mu nu)(y) has boundary edges on the mu- and nu-circles through y. So its boundary word is [g_mu, g_nu] with the circle holonomies based at y. Removing one plaquette at a time multiplies the word by that plaquette, conjugated by a path to y. All n_mu n_nu plaquettes are removed once. No centrality is used. HOLDS (standard non-abelian Stokes, lasso form).

**Signs and the norm bound.** For closed eta of class k_*, prod_(p in T_(mu nu)(y)) eta_p = (-1)^(k_*,mu nu). Since eta_p is central, prod_j V_j = (prod eta_j) prod_j (eta_j V_j). So ||[g_mu,g_nu] - (-1)^k I|| = ||prod_j eta_j V_j - I|| <= sum_j ||eta_j U_(p_j) - I||, by telescoping and conjugation invariance. HOLDS.

**SU(2) norm identity.** V in SU(2) has eigenvalues e^(+-i phi). ||I - V||^2 = |1 - e^(i phi)|^2 = 2 - 2 cos phi = 2(1 - tr V/2). eta U is in SU(2) for eta = +-1. HOLDS.

**(E15).** Cauchy-Schwarz over the n_mu n_nu plaquettes: (sum_j x_j)^2 <= n_mu n_nu sum_j x_j^2 = 2 n_mu n_nu sum_(p in T) [1 - eta_p s_p]. The quadruple g(y) has max error >= d_*, and max^2 <= sum of the six squares. This gives (E15) with the factor 2. HOLDS.

**Summation.** A mu nu plaquette lies in T_(mu nu)(y) iff y matches it in the two complementary coordinates: n_mu n_nu vertices. Summing over V_lat = a^2 cd vertices gives V_lat d_*^2 <= 2 sum_p (n_mu n_nu)^2 [1 - eta s_p]. Every bracket is >= 0. The largest side product on (a,a,c,d) with c,d in {a,2a} is cd. So the right side is <= 2(cd)^2 E_(k_*). HOLDS. Then E >= a^2 cd d_*^2/(2 c^2 d^2) = d_*^2 a^2/(2cd) >= d_*^2/8, since cd <= 4a^2. HOLDS.

**(E16).** With U_p = U_mu(x) U_nu(x+mu) U_mu(x+nu)^(-1) U_nu(x)^(-1), all factors in exp(i R sigma_3). Write the exponent of i sigma_3.
- x_nu != n_nu - 1: -theta x_nu + theta(x_nu + 1) = theta.
- x_nu = n_nu - 1, x_mu != n_mu - 1: -theta(n_nu - 1) + 0 + theta n_nu (x_mu + 1) - theta n_nu x_mu = theta.
- x_nu = n_nu - 1, x_mu = n_mu - 1: -theta(n_nu - 1) + 0 - theta n_nu(n_mu - 1) = theta - theta n_mu n_nu = theta - pi.
So the corner plaquette is -exp(i theta sigma_3). HOLDS. In planes mu rho and nu rho the links depend only on x_mu, x_nu, which a rho-step does not change; U_rho = I. Those plaquettes are I. HOLDS.

**Product of two plane fields.** The 12-field lives on directions 1, 2 and depends on (x_1,x_2). The 34-field lives on 3, 4 and depends on (x_3,x_4). In a cross plane such as 13, U_1 is constant in x_3 and U_3 is constant in x_1, and all factors commute. So cross curvatures are I. HOLDS. The two corner stacks are disjoint closed cochains of classes v_12 and v_34. Their sum has class k_*. With this eta, eta_p U_p = exp(i theta sigma_3) on all 12- and 34-plaquettes.

**(E17).** There are V_lat plaquettes per orientation. theta_12 = pi/a^2, theta_34 = pi/(cd). So E = a^2 cd {1 - cos(pi/a^2) + 1 - cos(pi/(cd))} <= (pi^2/2)(cd/a^2 + a^2/(cd)). With x = cd/a^2 in [1,4], x + 1/x <= 17/4. So E <= 17 pi^2/8. HOLDS. (E3) makes the infimum independent of the representative. HOLDS.

**Remarks after (E17).** Row 783 (21) gives E >= Delta_G a^2 for finite G. The upper field takes values in the Cartan U(1). The scope statements (no finite-beta consequence, no limit interchange) are correct.

Verdict for item 3: HOLDS. The load-bearing noncentral bound (E15) and its incidence count are correct.

## 4. Sections 4.2-4.3: (LC), binding tests, (E18)-(E20), the coin

**Choice of alpha.** For N >= 2, theta = pi/N <= pi/2, so sin(theta/2) is in (0, 1/sqrt 2]. An alpha in (0, pi/2) with sin^2 alpha = sin(theta/2) exists. HOLDS.

**Conjugation of j.** j e^(-i alpha) = e^(i alpha) j, so e^(i alpha) j e^(-i alpha) = e^(2 i alpha) j = cos 2alpha j + sin 2alpha k. HOLDS.

**Scalar part.** ABA^(-1) = cos alpha + sin alpha (cos 2alpha j + sin 2alpha k), and B^(-1) = cos alpha - sin alpha j. For quaternions (c + v)(c' + v') the scalar part is cc' - v.v'. Here it is cos^2 alpha + sin^2 alpha cos 2alpha = cos^2 alpha + sin^2 alpha - 2 sin^4 alpha = 1 - 2 sin^4 alpha = 1 - 2 sin^2(theta/2) = cos theta. HOLDS.

**Axis.** The commutator is a unit quaternion cos theta + sin theta n for a pure unit n (sin theta >= 0). A common conjugation rotates n to the sigma_3 axis and conjugates the commutator. So [A_N, B_N] = e^(i pi sigma_3/N) and C_N^N = e^(i pi sigma_3) = -I. HOLDS.

**Bounds.** 1 - tr A/2 = 1 - cos alpha = sin^2 alpha/(1 + cos alpha) <= sin^2 alpha = sin(theta/2) <= theta/2 = pi/(2N). The same for B. N(1 - cos theta) <= N theta^2/2 = pi^2/(2N). HOLDS. ||I - A||^2 = 2(1 - cos alpha) <= pi/N -> 0. HOLDS.

**Binding tests.** In finite G, every g != I has 1 - tr g/2 >= Delta_G > 0 (Delta_G is conjugation invariant). For N > pi/(2 Delta_G) the bounds force A_N = B_N = I, so the commutator is I, not C_N (and I^N != -I). HOLDS for those N; "sufficiently large N" is exactly this. In U(1) every commutator is I. HOLDS. So (LC) holds in SU(2) and fails in every finite subgroup (binary icosahedral included) and in U(1). HOLDS. The scope paragraph (lines 517-520) is correct: (LC) bounds only the commutator elements.

**(E18).** E[G C_N G^(-1)] commutes with SU(2), so it is (tr C_N/2) I = cos(pi/N) I. For independent matrix factors, E of the ordered product is the product of the means. So E tr g/2 = cos(pi/N)^N. HOLDS. With x = 1 - cos(pi/N) in [0,1] and x <= pi^2/(2N^2), Bernoulli gives (1-x)^N >= 1 - Nx >= 1 - pi^2/(2N). HOLDS.

**(E19).** With TV = sup_A |nu(A) - nu^-(A)|, a test f with |f| <= 1 obeys |int f d(nu - nu^-)| <= 2 TV. For f = tr/2, odd, the difference is 2 cos(pi/N)^N. So TV >= cos(pi/N)^N -> 1. HOLDS.

**(E20).** Conjugation invariance and Schur make each mean matrix (1 - eps_j) I. Independence gives the product mean prod (1 - eps_j). On [0, 1/2], log(1-x) is concave and lies above its chord, slope 2 log(1/2) = -1.386 > -2. So log(1-x) >= -2x and the product is >= exp(-2 sum eps_j). HOLDS. If the mean is <= e^(-T), then sum eps_j >= T/2. *Precision:* in line 561, "N" in exp(-sigma N) is a generic exponent (or the number of increments); the inequality holds for any target exponent.

**Coin example.** With probability 1/2 all increments are I (product I); with 1/2 all are C_N (product -I). The endpoint law is (delta_I + delta_(-I))/2, whose fundamental mean is 0. The expected deficit sum is (1/2) N (1 - cos(pi/N)) <= pi^2/(4N). HOLDS. The increments are neither independent nor conjugation invariant, so (E20) does not apply. (A common Haar conjugation would make each increment conjugation invariant and keep the product -I.) The GUIDE label for its Wilson use is correct.

Verdict for item 4: HOLDS, with one wording precision on the exponent in line 561.

## 5. Section 5: (E21)-(E25)

**(E21).** With eta_(m+v) = eta_m (-1)^(1_Sigma), X = S_(m+v) - S_m = X_Sigma^m. dmu'/dmu = e^(-X) Z_m/Z_(m+v) = e^(-X)/R = e^(F - X). HOLDS. For nu << mu (hence nu << mu'), D(nu||mu) = D(nu||mu') + E_nu log(dmu'/dmu) = D(nu||mu') + F - E_nu X. X is bounded, so all terms are finite. This is (E21). HOLDS. Equality at nu = mu' and the circularity remark are correct.

**Density of nu_j.** For Haar-preserving T, int f d(T_* mu) = int f(TU) rho(U) dU = int f(V) rho(T^(-1) V) dV, with rho = e^(-S_m)/Z_m. HOLDS.

**D(nu_j||mu) = E_mu[S_m(T_j U) - S_m(U)].** D = int rho(T^(-1)U) log[rho(T^(-1)U)/rho(U)] dU. Substitute U = TV (Haar preserving): int rho(V) log[rho(V)/rho(TV)] dV = E_mu[S_m(TV) - S_m(V)]. Z_m cancels. HOLDS.

**Action term.** E_(nu_j) X = E_mu[X(T_j U)] = E_mu[S_(m+v)(T_j U) - S_m(T_j U)]. Adding gives E_mu[S_(m+v)(T_j U) - S_m(U)], the jth term of (E22). HOLDS.

**Mixture identity.** log(dnu_j/dmu) = log(dnu_j/dnu) + log(dnu/dmu). Integrate against nu_j and average with pi_j (indices with pi_j = 0 drop): sum pi_j D(nu_j||mu) = I_pi + D(nu||mu). HOLDS.

**(E23).** sum_j pi_j E_mu[...] = E_nu X + D(nu||mu) + I_pi. So C(T,pi) = E_nu X + D(nu||mu) = F + D(nu||mu') >= F. F >= 0 because R <= 1 for admissible pairs. HOLDS.

**Sign of I_pi.** I_pi >= 0 and it is subtracted. This is the convexity gain: D(nu||mu) = sum pi_j D(nu_j||mu) - I_pi. The sign is correct. I_pi is the mutual information between the index and the output, so I_pi <= H(pi). Replacing I_pi by H(pi) would subtract too much and lose the inequality C >= F. The note's warning is correct. In dnu_j/dnu = rho(T_j^(-1)U)/sum_k pi_k rho(T_k^(-1)U), Z_m cancels. HOLDS.

**Finiteness.** 0 <= S_m <= 2 beta N_p. So every density ratio lies in [e^(-2 beta N_p), e^(2 beta N_p)]. HOLDS.

**(TR-V).** C <= C a^p e^(-sigma a^2) gives F <= that bound for every required pair. With q = (1 - e^(-F))/2 <= F/2 and row 778 (2), D <= 24 Q <= 12 max F once Q <= 1/24. So (V) follows with the constant multiplied by 12. HOLDS. *Precision:* "this would give (V)" is through row 778 (2), with a changed constant.

**(TR-F) constants.** q = (1 - e^(-F))/2 <= F/2 <= C/2. So 8q <= 4C <= K(a) eta_*^(a/2) <= K(a) sqrt(S_ev), using the witness S_ev >= eta_*^a. HOLDS. F <= 1/96 gives q <= 1/192, and q < 1/192 strictly: for F > 0, 1 - e^(-F) < F; for F = 0, q = 0. HOLDS. Taking the maximum over the crossed pairs gives (FQ) with the same K(a). HOLDS.

**(E24).** With uniform pi on all b, T_e o T_b = T_(b+e) permutes the index set, so nu is invariant under each link flip T_e. Flipping one edge of p sends s_p to -s_p, so E_nu s_p = 0. For m = 0, X = 2 beta sum_(p in Sigma) s_p, so E_nu X = 0. Then C = E_nu X + D(nu||mu_0) = D(nu||mu_0). HOLDS.

**kappa_I.** c_0(beta) = int e^(beta s) dg > e^(beta E s) = 1 by strict Jensen (s nonconstant, E_Haar s = 0). log c_0(beta)/beta is continuous and positive on the compact I. So kappa_I > 0. HOLDS.

**Z^0 >= c_0.** Fix the four edges of p. Each q != p has an edge e outside p: with sides >= 3, a plaquette is determined by its edge set. s_q is linear in U_e, and int U_e dU_e = 0. So the conditional Haar mean of sum_(q != p) s_q is 0. Jensen gives a conditional integral of prod_(q != p) e^(beta s_q) of at least e^0 = 1. Four independent Haar edges make U_p Haar distributed, so the rest integrates to c_0. HOLDS.

**Convexity step.** f = log Z^0 is convex, f(0) = 0 (normalized Haar), f'(beta) = sum_p E_(mu_0) s_p = N_p E_(mu_0) A. Convexity gives f'(beta) >= f(beta)/beta >= log c_0(beta)/beta >= kappa_I. So E_(mu_0) A >= kappa_I/N_p, while E_nu A = 0. HOLDS.

**Pinsker.** Data processing to the partition {dnu/dmu >= 1} and its complement reduces D to a Bernoulli divergence d(t||u) with |t - u| = TV. d''(t) = 1/(t(1-t)) >= 4, with d = d' = 0 at t = u. Integrating twice gives d >= 2(t-u)^2. HOLDS. A test in [-1,1] has |mean difference| <= 2 TV. So TV >= kappa_I/(2 N_p) and D >= 2 TV^2 >= kappa_I^2/(2 N_p^2). HOLDS.

**(E25).** N_p = 6 a^2 cd <= 24 a^4, so 2 N_p^2 <= 1152 a^8. HOLDS. The bound is uniform on I.

**Comparison with the tolerances.** The (TR-V) tolerance C a^p e^(-sigma a^2) falls below kappa_I^2/(1152 a^8) for large a. HOLDS. The (TR-F) tolerance min{1/96, K(a) eta_*^(a/2)/4} is exponentially small only if eta_* < 1. *Precision:* the note does not state this. It holds for the cited witness: gap-fusion-astra.md (2) has eta(beta) = e^(-80 beta) r^4/(4 + 16 r^4) < 1/16, since r = I_2/I_1 <= 1. With that witness, the claim HOLDS. The scope sentence (a statement about trial cost, not a lower bound on F) is correct.

**Section 5.3.** The cited gap-crux-restate.md lines 143-160 contain Lemma J and Way 3, as described: gauge averaging reads the corner factors, and the first-order Abelian spreading cost grows like pi^2 |n|/min(n_1,n_2)^2. The citation is accurate. The OPEN paragraph is correct.

Verdict for item 5: HOLDS, with two precisions: (TR-V) gives (V) through row 778 (2) with constant 12, and the (TR-F) comparison needs eta_* < 1, which the cited witness supplies.

## 6. The table (lines 801-807) and the RESULT line (line 845)

**Table.** Each row matches its section. (E3)-(E7): substitution, exact common covariance (E6), pointwise failure (E7); what remains is the weighted mean. Correct. (E9)-(E12): the negative odd form and the conditional selection. (E11) is a reused input, not the author's, but the row says only what was established with it. Correct. (E13)-(E17): constants c_* = d_*^2/8 and 17 pi^2/8, both independent of a, c, d. Correct. (LC), (E18)-(E20): exact small commutators that fail in finite subgroups and U(1); the obstruction covers independent conjugation-invariant mixing. Correct. (E21)-(E25): the exact identity and the polynomial lower cost of uniform sign randomization. Correct. The row label "PROVED by the author, not independently checked" was true when written.

**RESULT line.** (26), (V) and order-one (FQ)/(F-h) are left OPEN in every section. Correct. "Bound the rank-four SU(2) classical cost between constants" is (E13). Correct. "(LC) that fails both comparison groups" means (LC) holds in SU(2) but not in finite subgroups or U(1). Correct. "Exclude the stated averaging shortcuts" holds in the stated limited senses: no variance gain (E6), pointwise failure (E7), independent mixing (E19)-(E20), uniform sign randomization (E25). The missing input is correctly named as a weighted correlated comparison meeting (TR-F) or an equivalent direct estimate. The line MATCHES what is proved.

## Verdict table

| # | Statement (lines) | Verdict | Finding |
|---|---|---|---|
| 1a | (E1)-(E2); (E2) = row 783 (26) (80-108) | HOLDS AFTER CORRECTION (precision) | Exact for row 783's Sigma, or any representative avoiding the selected links |
| 1b | (E3) centre substitution (134-148) | HOLDS | Kanazawa Lemma 1 is the general-N form |
| 1c | (E4) (150-161) | HOLDS | |
| 1d | (E5), disjoint representatives, flat stacks (163-182) | HOLDS | Disjoint union has class \|A\| v |
| 1e | (E6) and the projector remark (184-202) | HOLDS | E prod P_j = (1-R)/2; P_j can be negative |
| 1f | (E7): odd intersection, a^2 tori, the open set (204-228) | HOLDS | Pairing with T_34(y) is a class invariant |
| 2a | (E8) reading (234-250) | HOLDS AFTER CORRECTION (precision) | Printed bound is on <W(C)>, not \|<W(C)>\|; p, q in N |
| 2b | Limitation of (E8); reflected product (252-261) | HOLDS | Lower bound on q only; E P_1 P_2 = q |
| 2c | (E9)-(E10) (263-294) | HOLDS | Eigenvalue int s sinh(beta s) > 0, twisted -c_beta |
| 2d | (E11) as quoted (296-314) | HOLDS | Matches R3 and R2 (b); candidates need the cube |
| 2e | (E12): Z_(chi,m) <= Z_(0,m), factors 8 and 64 (316-338) | HOLDS | "Dominance" here is the positivity bound; also excludes the diagonal group |
| 3a | (E14) existence of d_* > 0 (366-379) | HOLDS | Compactness and row 783 1.3 |
| 3b | Noncentral peeling identity (381-392) | HOLDS | Lasso form of Stokes |
| 3c | (E15): factor 2, Cauchy-Schwarz, SU(2) norm identity (393-404) | HOLDS | |
| 3d | Summation; E >= d_*^2 a^2/(2cd) >= d_*^2/8 (406-417) | HOLDS | Incidence n_mu n_nu, max product cd <= 4a^2 |
| 3e | (E16) curvatures; product field; (E17) (419-457) | HOLDS | Corner exponent theta - pi; x + 1/x <= 17/4 |
| 4a | (LC): alpha, scalar part, axis, bounds (476-507) | HOLDS | 1 - 2 sin^4 alpha = cos theta |
| 4b | Binding tests, finite subgroups and U(1) (509-520) | HOLDS | For N > pi/(2 Delta_G) |
| 4c | (E18)-(E19) (522-548) | HOLDS | |
| 4d | (E20) (550-563) | HOLDS AFTER CORRECTION (precision) | "N" in exp(-sigma N) is a generic exponent |
| 4e | Coin example (565-572) | HOLDS | Deficit sum <= pi^2/(4N) |
| 5a | (E21) (578-595) | HOLDS | |
| 5b | (E22)-(E23), D(nu_j\|\|mu) formula, sign of I_pi (597-646) | HOLDS | I_pi subtracted is the convexity gain; H(pi) would be invalid |
| 5c | (TR-V) (648-657) | HOLDS AFTER CORRECTION (precision) | Gives (V) through row 778 (2), constant times 12 |
| 5d | (TR-F) constants: q <= F/2, 1/96, K(a)/4 eta_*^(a/2) (658-673) | HOLDS | q < 1/192 strictly |
| 5e | (E24) (675-686) | HOLDS | |
| 5f | kappa_I, Z^0 >= c_0, convexity, Pinsker, (E25) with 1152 a^8 (688-731) | HOLDS | |
| 5g | (E25) exceeds the tolerances (732-737) | HOLDS AFTER CORRECTION (precision) | (TR-F) case needs eta_* < 1; the cited witness has eta < 1/16 |
| 5h | Section 5.3 citation of Lemma J, Way 3 (741-756) | HOLDS | |
| 6a | Table, lines 801-807 | MATCHES | |
| 6b | RESULT line, line 845 | MATCHES | Exclusions hold in the stated limited senses |
| - | Seiler arXiv:0901.4246; second half of Kanazawa page; Section 6 source checks | NOT CHECKED | Outside the brief |

Checked line by line by Claude Opus 5.5. Nothing FAILS. Six precision corrections (1a, 2a, 4d, 5c, 5g, and the wording in 2e). None changes a conclusion. Credit Codex gpt-6-astra max for the noncentral incidence bound (E15), the Cartan upper field (E16)-(E17), the group input (LC), the transport identity (E22)-(E23) and the trial-cost bound (E25).

RESULT: Every item of gap-ext-astra.md in the brief HOLDS under a hand check by Claude Opus 5.5 — (E3)-(E7), (E9)-(E12), (E13)-(E17) including the noncentral bound (E15), (LC) with (E18)-(E20), and (E21)-(E25) are correct, with six precisions that change no conclusion (the Sigma in (E2), the printed Tomboulis-Yaffe form has no absolute value, positivity not dominance in (E12), the generic exponent in (E20), the constant 12 in (TR-V) => (V), and eta_* < 1 for the (TR-F) comparison, supplied by the cited witness); nothing FAILS, and the table and RESULT line match.
