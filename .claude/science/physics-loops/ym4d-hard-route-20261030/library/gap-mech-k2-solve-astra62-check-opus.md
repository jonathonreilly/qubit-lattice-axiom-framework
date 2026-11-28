# Check of library/gap-mech-k2-solve-astra62.md (FINISH row 1548)

Checker: Claude (Opus 5.5). Target: row 1544, author gpt-6.2-astra max.

## Plan
1. Read GOAL.md, FINISH.md Rules and Working efficiently.
2. Read the target note in full.
3. Check Theorem A line by line.
4. Check Theorem B line by line (eqs (5), (6), flat saddle, residues, finite exceptional set).
5. Check the consequence (no fixed-temporal-range coarse potential on an open interval).
6. Check the seed section (countable union, beta_K limitation, purity separation via check 1527 (iii) and row 1143, U(1) and 5D SU(2)).
7. Check the open step against row 1468 section 4.3.
8. Novelty against rows 1468-1500, checkpoints 1496, 1497, and library/open-registry.md.
9. RESULT line.

## Progress
(complete; steps 1-9 below)

Step 1 done: read GOAL.md (computation-as-proof rule, model floors), FINISH Rules and Working efficiently (equivalent-is-not-progress rule; save as you go). Step 2 done: read the target note in full (198 lines).

## Theorem A (entire coarse actions), checked line by line

Lines 19-26 (setup). D(V) = int exp(sum_e kappa_e M_e(W).V_e) d eta(W), |M_e| <= 1. For Q2, M_e is an average of unit quaternions, so |M_e| <= 1; Re(M V^{-1}) = M.V for unit V since V^{-1} = conj(V). The normalizers 1/Z_c(kappa|M_c|) depend on W only and go into eta. HOLDS.

Line 28-34, bound (1). With theta = x + iy, cos(x+iy) = cos x cosh y - i sin x sinh y and sin(x+iy) = sin x cosh y + i cos x sinh y. So the real (quaternion-coefficient) part of V_e(x+iy) = U_e(cos theta + X sin theta) is cosh(y) V_e(x), and Re(kappa M.V_e) = kappa cosh(y) M.V_e(x) <= kappa cosh R. Hence |F| <= eta(1) exp(K cosh R). HOLDS.

Line 36, entire logarithm. F zero-free and entire on C^E gives an entire log H; fix the branch real at one real point; then H is real on R^E (log F is real there and H - log F is a continuous 2 pi i Z-valued function). H(theta + 2 pi e_j) - H(theta) is a continuous 2 pi i Z-valued function, zero on R^E, hence zero. HOLDS.

Line 36-40, inequality (2). H periodic entire, so H(theta) = sum h_m e^{i m.theta} converges on all of C^E. Fix m != 0, s_e = sgn(m_e). For real theta, H(theta + iRs) has m-coefficient h_m e^{-R m.s} = h_m e^{-R||m||_1}; conj H(theta+iRs) = H(theta - iRs) (reality on R^E) has m-coefficient h_m e^{+R||m||_1}. So Re H(. + iRs) has m-coefficient h_m cosh(R||m||_1) and mean h_0. Since |Im theta_e| = R|s_e| <= R, (1) gives g = C + K cosh R - Re H(. + iRs) >= 0, and a nonnegative integrable function has |g^(m)| <= g^(0). This is (2). HOLDS.

Line 42, killing modes. As R -> infinity, LHS ~ |h_m| e^{R||m||_1}/2 and RHS ~ K e^R/2, so h_m = 0 for ||m||_1 >= 2. For m = +-e_j: the central gauge change -1 at one endpoint x of bond j maps V_e -> -V_e on every bond incident to x (exactly once each, since there are no self-loops; parallel bonds are allowed), and -U_e(cos theta + X sin theta) = U_e(cos(theta+pi) + X sin(theta+pi)). So gauge invariance of D gives F(theta) = F(theta + pi 1_I), I the bonds at x, hence H likewise (reality fixes the 2 pi i constant), hence h_{+-e_j} = -h_{+-e_j} = 0. Fourier uniqueness gives H = h_0. HOLDS. Remark: the centre symmetry is essential; eta concentrated at M = 1 gives the non-invariant linear density exp(kappa Re V_e), which is the frequency-one case.

Line 44, globalisation. Given real V, V', take U_e = V_e and X_e, theta_e from the axis-angle form of V_e^{-1} V'_e (any X_e if it is +-1). So a zero-free F on every product gives D constant. An action S entire on every angle complexification with D = exp(-S) on the reals gives exp(-S) = F by uniqueness of continuation from the totally real R^E, so F is zero-free. SU(2) spin-j matrix coefficients on U exp(X theta) have frequencies 2m_j in Z (period 2 pi), so finite spin-network sums are trigonometric polynomials, hence entire. HOLDS.

Lines 46-52, two periods. D_v constant forces D_v = exp(c N_v). The Q2 kernel is normalized in V for every W, so Fubini gives int D_v dV = Z^0(v) (fine Wilson partition function). N_{2u} = 2N_u gives Z^0(2u) = Z^0(u)^2. HOLDS (given the doubled torus doubles only the time period, which is the setting here).

Lines 54-61, inequality (3). Z^0(v) = Tr T^v on the gauge-invariant space. T = M^{1/2} C M^{1/2} with C the product of one-link electric convolutions and M the positive spatial weight. The character coefficients of exp(-beta(1 - Re tr U/2)) are (2j+1) * 2 e^{-beta} I_{2j+1}(beta)/beta > 0 (positive power series), so C is positive and injective, M is bounded and invertible, and T is positive, injective and trace class on the finite spatial lattice. A gauge-invariant space of dimension at least 2 (constant and a contractible plaquette trace, both also centre-neutral) then has at least two strictly positive eigenvalues, so sum_{i != j} lambda_i^u lambda_j^u > 0. HOLDS. The side remark "also gives P_K < 1" needs Z_+(v) = Tr(T^v Pi_0) with Pi_0 the centre-neutral projector; the note asserts the neutral-sector independence, which is the only extra input. I did not re-derive the twist-average identity; it is a side remark and not used by A or B.

Verdict Theorem A (including the constant option and the two-period pressure argument): HOLDS.

## Theorem B (temporal range of the full image), checked line by line

Sources read for B: library/gap-k2-tool-design-fable.md 3.2 (Q2 contours: axis path 2y -> 2y+xi, xi in {0,1}^4, axes in order pi, two steps in mu, reverse path; at most 4+2+4 = 10 steps), library/gap-k2-signed-readout-fable.md lines 56-147 (Proposition L, L1, L2), library/gap-k2-signed-readout-check-astra62.md lines 18-44 (L holds on each fixed torus in every C^m_V norm near V = 1; the axial symbol s/[1+(1/a-1/8)s]).

Lines 65-80, definitions and fixed-torus input. The range definition (any summands, constants allowed) is the one used later. Proposition L with check 1483 gives F_x - F_x(1) = x (R_a S_W - R_a S_W(1)) + (Psi - Psi(1)) + O_N(1/x) near V = 1, in every C^m_V norm, on every fixed even torus; R_a S_W is the E_a of line 70 (E = S + aT, T_c = |M_c| - Re(M_c V_c^{-1})). The quadratic form (4) is the Schur complement d^T d + a Q^T Q (check 1483 line 30). The flat-saddle sentence matches check 1483's repair (homotopic contours give equal transports, coarse cycles detect torus holonomies). HOLDS.

Line 82, eigenvector claim (terse in the note; I wrote it out). The leg path from 2y to 2y+xi does not depend on mu, so averaged over the 384 pairs the leg contribution to (QA)_mu is Psi(y) - Psi(y+e_mu) for one coarse function Psi: an exact coarse gradient. Writing A = A_T + d phi, the gradient parts give QA_T + d_c chi, so energy(v) = energy_T(Pi_perp v) with Pi_perp the projection off coarse gradients, and Pi_perp Q A_T = Pi_perp S A_T with S the straight-average part, S_mu(k') = prod_i ((1+e^{ik'_i})/2) (1+e^{ik'_mu}). At p = (q, pi/2, 0, 0): S_2 vanishes unless k'_2 = 0, and there the transverse projector fixes e_2 (its longitudinal part carries 1 - e^{ik'_2} = 0). So S C_T S^* e_2 = G e_2 with G the scalar of (5), and Pi_perp e_2 = e_2 since p_2 = 0. Hence e_2 is an eigenvector of a^{-1} + Pi_perp S C_T S^* Pi_perp and the direction-2 Hessian symbol is h = (a^{-1} + G)^{-1}. HOLDS.

Equation (5). Aliases k'_i = p_i/2 + pi n_i. Directions 2, 3: weight (1+cos k')/2 kills the pi alias; direction 2 carries |1+e^{ik'_2}|^2 = 4. Directions 0, 1: cosines tau c and sigma/sqrt2, weights (1+tau c)/2 and w_sigma, Laplacian 4 - 2 sigma/sqrt2 - 2 tau c = A_sigma - 2 tau c. Cell factor 2^{-4}. Inner sum: (1+c)/(2(A-2c)) + (1-c)/(2(A+2c)) = (2A + 4c^2)/(2(A^2-4c^2)) = (A+2c^2)/(A^2-4c^2) = (A+1+z)/(2(t-z)). Zero spatial momentum: G = (1/4) sum_tau (1+tau c)/(2(2-2tau c)) = (1/16)[(1+c)/(1-c) + (1-c)/(1+c)] = (1+c^2)/(8(1-c^2)) = (3+z)/(8(1-z)) = 1/(2(1-z)) - 1/8, agreeing with the axial formula of check 1483 (s = 2(1-z)). HOLDS. Guide only (python3 -I scratch script, floats, not a proof step): the alias sum and the closed form agree to 1e-15 at five values of q in d = 4 and d = 5.

Equation (6). (A+1+z)/(2(t-z)) = (A+1+t)/(2(t-z)) - 1/2 and w_+ + w_- = 1 give the decomposition with r_sigma > 0. t_+ = (4-sqrt2)^2/2 - 1 = 2.343..., t_- = 13.66..., so 1 < t_+ < t_-. On (t_+, t_-) the sum of r_sigma/(t_sigma - z) has derivative sum r_sigma/(t_sigma-z)^2 > 0 and runs from -infinity to +infinity, so there is exactly one zero t_*, for every a > 0 (including a = 8, where the axial symbol is a polynomial). U(t_*) = (t_+ - t_*)(t_- - t_*) != 0, so h = U/D has a genuine pole. On [-1,1], a^{-1} + G > 0. HOLDS.

Line 107, distant pair. m = floor(N/2) >= 2. If all direction-2 entries at cyclic time distance > m-2 vanish, translation invariance (Q2 is covariant under coarse translations; E_a is gauge invariant, so its Hessian does not depend on the tree gauge) gives h(cos q) = a Laurent polynomial of degree <= m-2 on the grid; 2(m-2)+1 < N, so the representatives are distinct. Averaging q, -q gives P(cos q), deg P <= m-2, at the m+1 distinct values cos(2 pi k/N), k = 0..m. D != 0 on the grid, so U - DP (degree <= m) has m+1 zeros, hence U = DP, contradicting D(t_*) = 0, U(t_*) != 0. So a fixed pair e, f of direction-2 bonds at cyclic distance >= m-1 has a nonzero mixed Hessian entry. The pair is chosen once, independent of beta. HOLDS.

Line 109-113, (7). E_a is C^2 near 1 (in fact analytic, implicit function theorem), so a small rectangle in the one-parameter directions V exp(sX) has Delta_ef E_a != 0. Proposition L gives B(beta) = beta delta + Delta_ef Psi + O_N(1/beta); vacuum constants cancel in the rectangular difference. So B(beta)/beta -> delta. HOLDS.

Line 115, finite exceptional set. Z_c(t) = 2 I_1(t)/t is entire and positive on R, so it is nonzero on a complex neighbourhood of the compact segment {a beta_0 t : 0 <= t <= 1}; the integrand is holomorphic and bounded there, D_beta(V) > 0 on real beta, so F_beta(V) is real analytic in beta on all of R. B(0) = 0 (D_0 = 1), but B is not identically zero by (7); its zeros are isolated, none beyond some beta_1 by (7), and none accumulate in [0, beta_1]. Finite. HOLDS.

Lines 117-123, (8). Each summand of a range-R action with R <= m-2 omits e or f, so its rectangular difference vanishes; |Delta_ef g| <= 4 ||g||_infinity. The essential-supremum version follows from continuity of F_beta. |B| >= |delta| beta/2 eventually gives |delta| beta/8. HOLDS.

Lines 125-150, (9). Translation averaging is a convex average of unitary conjugates, preserves range, and does not increase the operator-norm distance to the translation-invariant D^2 E_a(1). The diagonal element in the unit Fourier vector e_2 phi_p is a Laurent polynomial of degree <= R (N > 2R); its q, -q average is a polynomial P(cos q), deg <= R, with |h - P| <= eps on the grid. J = U - DP has degree <= R+2 = L; |J(cos q)| <= eps max_{[-1,1]} |D| on the grid. S(w) = w^L J((w+1/w)/2) has degree <= 2L < N, so each DFT coefficient has modulus <= eps max|D|; w_* + 1/w_* = 2 t_* gives S(w_*) = w_*^L U(t_*), and the geometric sum gives (9). C(a) does not depend on N. The liminf statement uses the C^2 version of L, which check 1483 supplies on each fixed torus. HOLDS. The note itself says there is no crossover estimate at growing N; correct.

Lines 152-159, (10). d/dt M_c.(V_c e^{tX}) = M_c.(V_c X); each V-derivative of log D inserts the score; d_f S_e = 0 for e != f. So d_e d_f log D = Cov(S_e, S_f) and (10) holds with the sign shown. D is real analytic and positive in V, so the mixed derivative is real analytic on SU(2)^E, not identically zero (its integral over the rectangle is B(beta) != 0), hence nonzero off a null set (standard; the stratification sketch is adequate). HOLDS.

Lines 161-169, (11) against R10. (H2) of library/gap-seed-solve-fable.md 4.1 is |Cov_{mu^V}(f, S_c)|^2 <= E sum_l gamma_cl |grad_l f|^2 with S_c the tangential score; the X-component of the covariance is bounded by the vector modulus. g = S_e^X is smooth. Q2 legs move only in positive directions with xi_0 in {0,1}, so every link of a contour of a spatial bond at coarse time t_e has fine base time 2t_e or 2t_e + 1, coarse time t_e. At most 10 steps per contour gives |grad_l g| <= 10 kappa. Weights vanishing beyond m-2 coarse time steps of f give zero on B_e, contradicting (11) off the finite exceptional set. The note correctly says that R10 / (FL) asks only exponential decay of mean weights, which (11) does not touch. HOLDS.

Lines 171-177, conditional mutual information and KL. A conditional product density has vanishing mixed log derivative (rectangular differences a.e., then continuity); by (10) and Fubini factorization fails for a.e. C, so I_mu(V_e; V_f | C) > 0. For nu = exp(-L)/Z with L of range <= m-2, L = L_1(V_e, C) + L_2(V_f, C) + L_3(C), so V_e and V_f are conditionally independent under nu; the chain rule D(mu||nu) = D(mu_C||nu_C) + E_C D(mu_{ef|C} || nu_{e|C} x nu_{f|C}) and the split of the last term give D >= I. HOLDS.

Verdict Theorem B (statement of lines 11 and 63-177, including (5), (6), the flat saddle, the residues and the finite exceptional set): HOLDS.

Consequence (line 11): for a fixed range R and any torus of the class with floor(N/2) - 2 >= R, exact representation forces B(beta) = 0, which happens at finitely many beta; an open interval has infinitely many. So no fixed-temporal-range coarse potential represents the step on an open order-one interval. HOLDS (indeed on all but finitely many couplings for each such torus).

## Seed section (lines 179-185)

Sources: library/gap-k2-tool-design-fable.md 3.1 and 3.3 (Z_+(v) = Tr(P_0 T^v), level-k tori: spatial side l_k, time sides v_k = l_k/512 and 2v_k), library/gap-agy-seed-approaches-neon-check-astra62.md (iii) lines 59-86, library/gap-solve-astra62.md section 3, equation (4).

Line 181, geometry and countable union. I read "both side-two coarse tori" as the two images under the side-two block map. With n = l b^K, l in 1024 N, u = n/512: coarse spatial side n/2 is divisible by 4 (indeed by 512), coarse time N = v/2 is an integer (u/2 = l b^K/1024), and N >= 4 for large K. floor(N/2) - 1 = floor(v/4) - 1, as stated. For fixed a the union over K of finite sets is countable, hence null; any beta off it obeys the range bound on every large K. HOLDS. The stated limitation is correct and needed: B says nothing at the particular beta_K, since beta_K may lie in the K-th exceptional set. A applies at every beta_K: HOLDS.

Line 183, purity separation. At beta = 0 every normalized twisted partition function is 1, so P = 1, and P is continuous in beta: P -> 1 as beta -> 0. At fixed geometry check 1527 (iii) gives P of order beta^{-3/2}/log beta (from row 1143 (4) and Z^0/8 <= Z_+ <= Z^0), so P -> 0; row 1143 (4) covers rectangles with sides at least three, which the seed tori satisfy. Finite exceptional sets can be avoided by continuity of P. Both obstructions (A at every coupling, B off finite sets) hold at both couplings. The inference (an obstruction present at P near 1 and at P near 0 cannot be a purity criterion) is correct. HOLDS.

Line 185, U(1) and 5D SU(2). Theorem A: for U(1) the bilinear continuation of M_1 cos theta + M_2 sin theta has real part cosh(y) times the real value, so (1) holds; the vertex transformation -1 in U(1) shifts incident angles by pi; one-link coefficients e^{-beta} I_n(beta) > 0 give (3). In 5D the graph argument is unchanged. HOLDS. Theorem B: the Hessian computation is abelian at quadratic order; a fifth direction with p_4 = 0 has weight 0 at the pi alias and Laplacian 0 at the zero alias, so A_sigma, t_sigma, w_sigma are unchanged and gamma = 4/2^5 = 1/8; r_sigma > 0; t_* exists for every a. Guide only: the 5D alias sum equals the closed form with gamma = 1/8 at five values of q.
HOLDS AFTER CORRECTION. The note never defines the comparison kernels, and Proposition L is proved only for SU(2) Q2 in 4D. Correction to write in: "U(1): the same 384 contours, tie exp(kappa Re(M_c conj V_c))/I_0(kappa|M_c|); 5D: contours indexed by xi in {0,1}^5 and the 120 permutations of five axes, normalized by 32 x 120. For these kernels the leg contribution is again an exact coarse gradient (the leg does not depend on mu), and the proof of Proposition L as repaired in check 1483 (flat saddle, compactness gap, Laplace expansion in C^m_V) applies unchanged, with I_0(t) ~ (2 pi t)^{-1/2} e^t for U(1)." With that, the conclusion "no group or dimension selectivity" holds: weak-coupling 4D compact U(1) and 5D SU(2) are not expected to have a gap, and both obstructions hold there.

## Open step against row 1468 section 4.3 (lines 187-196)

Row 1468 4.3 (K2-STEP): a, delta_0, r > 0; centres Phi*_k with readout x_k, radius rho_k, wrap error eta_k; Q2 at strength a x_k maps Tube(Phi*_k, rho_k; eta_k) into Tube(Phi*_{k+1}, ...), with (DR) x_{k+1} <= x_k - delta_0, (TR) rho_{k+1} <= rho_bar(x_{k+1}), (WR) eta_{k+1} <= eta_k + size(T) e^{-rs/8}. The note's four displayed conditions match, with size(T) = |Lambda|. It omits that rho_bar stays inside the margin of (C5) and below the end threshold, the start window x_0 in [H, W_*] and the stop rule; these omissions do not change the open statement. HOLDS. The note's statement that (2) and (7)-(11) give no uniform tail bound and no signed decrement is correct: (8) and (9) are fixed-torus or torus-free lower bounds on distance to finite-range actions, and tubes with summable tails are untouched.

## Novelty against rows 1468-1500, checkpoints 1496/1497 and the registry

Searched the 28 library files of rows 1468-1500 (including gap-k2-direction-checkpoint-fable.md and gap-k2-direction-checkpoint-check-astra62.md) and library/open-registry.md for entire or zero-free actions, complex zeros, temporal or finite range, mutual information, Laurent arguments and infinite tails. No file states A or B. Registry: R10 (line 1017) owns the exponential-decay (FL) estimate and asserts no finite support; no row owns either obstruction.
- Theorem A: NEW as a statement. Its method (growth bound on an entire logarithm) is that of row 1290 (library/gap-solve33-astra62.md, one varied link, order-1/2 growth), which the note credits. The new parts are the several-circle Fourier bound (2) and the use of centre parity to remove the frequency-one modes.
- Theorem B: NEW, with a partial prior. The axial symbol s/[1+(1/a-1/8)s] (PR 10114 axial formula; repeated in check 1483, L1 repair) already shows that the classical quadratic image has an infinite tail on the axis for a != 8, in infinite volume. B adds: an off-axis momentum giving a pole for every a > 0 (a = 8 included); a fixed distant pair on each finite torus; the transfer to the full image at finite beta with a finite exceptional set; the conditional-information and KL forms; the bound (9) independent of the torus; and the exclusion of finite-support (H2) weights.
- Both are obstructions, not sufficient conditions, so the equivalence rule does not apply. They exclude two closure classes and do not move (K2-STEP). In check-report terms: CORRECT-NO-ADVANCE on the open step.

## Defects (ranked)

1. Line 185 (U(1), 5D): the comparison kernels and the transfer of Proposition L are not written. The correction is above. This does not affect A or B for 4D SU(2).
2. Line 82: the eigenvector property of e_2 is asserted in three short sentences. It is correct; the full argument (the legs give an exact coarse gradient because the leg path does not depend on mu; S_2 is supported at k'_2 = 0, where the transverse projector fixes e_2) is above. No change to any statement.
3. Line 61, side remark "also gives P_K < 1": correct given Z_+(v) = Tr(P_0 T^v) (row 1468 3.1) and a neutral space of dimension at least 2. A and B do not use it.
No defect breaks a stated theorem.

## Scope

The check line below covers all of library/gap-mech-k2-solve-astra62.md lines 7-198, against the cited lines of rows 1468, 1479, 1483, 1510 (4.1-4.2), 1527 (iii), 1143 (3, eq. 4), 1290, and library/open-registry.md R10. Not checked: the twist-average identity Z_+ = Tr(P_0 T^v) itself (taken from row 1468 3.1), and the repo-search claims about PR branches 10114 and 10141 (not opened). Hand check only; no Lean; the floating-point runs were guides, not proof steps.

RESULT Theorem A HOLDS; Theorem B HOLDS, including (5), (6), the flat saddle, the positive residues, the analytic finite exceptional set, (7)-(11) and the CMI/KL forms; the no-fixed-temporal-range consequence HOLDS; the seed countable-union argument and its beta_K limitation HOLD; the purity separation via check 1527 (iii) and row 1143 HOLDS; the U(1)/5D extension HOLDS AFTER CORRECTION (define the comparison kernels and carry Proposition L over); the open-step statement matches row 1468 4.3; A and B are new relative to rows 1468-1500 and the registry (B has an on-axis prior for a != 8); neither advances (K2-STEP).
Checked line by line by Claude (Opus 5.5).
