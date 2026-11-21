First failing step: none

# PW gate: line-by-line check of library/pw.md

Text read: library/pw.md, lines 1-1197, by section. Sources read for the check: p82.md sections 1-4; h-walk.md section 4; o1-decoupled.md lines 105-135 and 399-406; dr.md section 1; dr-draft.md section 6; dec-field.md (5.3); in1.md order table; SA ym4.tex lines 10125-10156, 10369-10372, 10384, 10548-10552, 10562, 10582.

## Findings

No step fails. Three repairable points, none fatal:

- **F1 (lines 212-220 and Result, line 1176). Inputs named too narrowly.** Repairable, editorial. The text says it uses P82's I1, I2, I4, I5. It actually uses P82's proved Lemmas 1 ((17)-(19) and the averaging estimate, lines 247-289), 2 (R an orthogonal projection; Schur elimination), 3 (bare inverses) and 4 (uniform five-variable energy inverse, used in section 3). These are proved in frozen P82 from I1, I2, I5 under Reg_alpha, so the mathematical claim stands. It also uses the h-walk Theorem W identity K B = 1 - R, h-walk Lemma C (C1)-(C4) and the h-walk-gate repairs, which are part of the dr.md section 1 specification. Repair: name P82 Lemmas 1-4 as proved consequences, and name the h-walk structural lemmas, in section 4 and in the Result.
- **F2 (lines 282-287, Cauchy step for (4.4)).** Repairable, editorial. The circle a + z h with |z| = c/(m_c||h||) stays in the analytic ball only if a lies in a smaller ball (say m_c||a|| < r_0/2) and c <= r_0/2. The text does not say this. Repair: state (4.1) on the half-radius ball; it is used only at the reference (a = 0).
- **F3 (line 984 and Result, lines 1180-1183). Hypothesis (P) not named in the Result.** Repairable. The parameter count (8.2) uses Hypothesis (P) of o1-decoupled line 116: every set of d_B-diameter < l_P/2 meets at most 2^4 parameter cubes. O1D (line 406) records that this needs the parameter cubes to be large in every local unit, and fails if they are finer in finer layers. The Result claims "the whole decoupling polydisc" without naming (P). Section 9 item 4 ("M large enough for the parameter grid") is right only if the NL1-L D1 level-(i-1) side-M cubes have physical side at least l_P xi_max/2. That is the same inherited premise O1D Theorem B carries; pw neither adds nor removes it. Repair: add "(P) on the parameter partition" to the Result's hypotheses.

The checks the lead asked for, in short (detail in the section record below):
- Rough current force: handled in section 6, not by section 2 or 3 alone. In the unfolded system the current sits only in the A-row and in the lambda-component of the Y-row, whose unknown is p = h' + D^T A/2. The rough part stays a divergence D^T Z_lambda with |Z_lambda| <= C gamma_0 m^{-3}|lambda|. p is estimated only in W^{1,8}, and the field equation sees only Dp in L^8. The Y-variable lambda solves the current-free Z-row equation, so D lambda is bounded. No difference of J and no sup bound on Dp is used. Section 2 (congruence) and section 3 (coercivity) supply the baseline local inverses only; section 3 removes the multiplier only on real flat/bare baselines, and Proposition 5 then perturbs without positivity. Sound.
- s != 1: no equation is used for a switched sum. Each switched operator is an absolutely convergent sum of unswitched walk/tree terms times s^{P(omega)}. Each term is estimated termwise from genuine local inverses and commutators. Sound.
- Section 5: energy premise from I1 flat models and P82 Lemma 3 bare models through the congruence, then a complex current-corrected parametrix. Schur factors: A_s, Q'A_s^{-2}Q'^T, T and QT^{-1}Q^T are all shown invertible. Sound.
- Section 6: the energy-to-W^{2,8} bootstrap is mesh-uniform. The Calderon-Zygmund constants are lattice-uniform, and point evaluation covers a bounded radius/mesh ratio. The bootstrap closes under the cutoffs by the two exact cancellations (6.10)-(6.11). Sound.
- Complex pairs: positivity and orthogonality of R are used only at real baselines. All other bounds are absolute complex series, density or form bounds. Sound.
- e^{16 kappa-bar}, tau, theta <= tau/16: the exponent ledger is checked; 2048 = 128 x 16. The constant order matches IN1 rows 1-10 with Amendment 1, dr.md's Order, and SA 10582. Sound.

## Section-by-section record

## Section 1 (lines 5-54): contract

Read. The target (PW) is stated with X_w containing mA and m^2 nabla_U A, F_w with m^3 f, Y_w raw counting rows, |s(Delta)| < e^{kappa-bar}. The independent-current hypotheses (SA 10129-10137) are stated as a pointwise bound on J with no difference bound. The text correctly forbids importing QH(s)=1 at switched parameters. No step to check here.

## Section 2 (lines 56-162): local congruence

- (2.2) checked against h-walk.md section 4 (the unfolded system K, rows A, Y, Z, nu) at J = 0, j = 0, with Delta^W replaced by q^T q: the quadratic form <Psi, K Psi> is exactly (2.2). The coefficient one on <t, A_s lambda> is right: it is 2<A, q_{A lambda} lambda> from the polarization of q((A, lambda)).
- Lemma 1, (2.3)-(2.6): checked by hand. Substituting h' = p - t/2 cancels the two <t, A_s lambda> terms; 2<h,p> = ||H||^2 - ||u||^2 with H = p + h/2, u = h - H = h/2 - p; with p = (H-u)/2, h = H+u, the scalar cross terms give 2<H, A_s psi> + 2<u, A_s chi>; the top terms give -2<lambda, Q'^T M_s> - 2<chi, Q'^T mu>, which equals the stated -2<psi,Q'^T M_s> - 2<chi, Q'^T (mu - M_s)>. With v = -chi, N = -zeta this is Q_5 - Q_sc. The inverse (2.6) checked. Q_5 equals the quadratic form of P82 (8) and Q_sc that of P82's scalar subsystem S (rows 2-4). Correct.
- Row conversion (2.1): <QA,nu>_phys = <mQA, m^3 nu>_count with physical row weight m^4. Consistent with h-walk's ||nu||_{row*}^2 = sum xi^6 |nu|^2 = ||zeta||_count^2.
- The text itself flags (line 152-156) that the P82 scalar norm H^2_m and the h-walk graph norm Lambda must be compared. That comparison is checked where it is used (section 5).
- Line 158-162, row mass a_0: harmless; the shift of N absorbs (a_0-1)||KA||^2.

No defect. Note: section 2 is the baseline with both currents zero. It does not by itself touch the rough current force; that is checked in sections 4-5.

## Section 3 (lines 163-210): coercivity lemma

- Lemma 2: checked. M(a,0) = (Ta, -Ka); ||Ta||_{E*} <= sqrt(C_T) <a,Ta>^{1/2} by Cauchy-Schwarz for a nonnegative form; then ||a||_E <= B(||Ta|| + ||Ka||). Correct.
- (3.3): T_0 is P82's Sigma_q = B_q - D P D^T = q^T q + D R D^T + K^T K (P82 Lemma 2, eq. (20)). R is an orthogonal projection at real data (P82 Lemma 2), so T_0 >= 0 and ||Ka||^2 <= a_0^{-1}<a,T_0 a>. C_T follows from boundedness of q, D^T on E and the row trace (P82 (17) by Schur test gives ||Ka||_count <= C||m^{-1}a||). The saddle bound is the (a, nu) block of P82 Lemma 4 (uniform X* -> X bound for M_q), with sources (f,0,0,0,g_5). Correct.
- Small citation point (not a defect of the math): the saddle bound is P82 Lemma 4 (a result proved from I1, I2, I5 via Lemma 1 and the bare Lemma 3, under Reg_alpha), not one of the imports I1-I5 themselves. Section 4 lists "I1, I2, I4, I5" as the inputs; the text should say it uses P82 Lemmas 2 and 4 as proved consequences of them under Reg_alpha at a real reference.

## Section 4 (lines 212-400): coefficients on the complex envelope

- Lines 212-220: the inputs list. See the citation note under section 3 (P82 Lemmas 1, 2, 4 are used, not only the imports).
- Lemma 3 (4.1)-(4.4), lines 224-294: checked.
  - (4.2) is the P82 Lemma 1 averaging estimate (p82.md lines 247-262), which reads only ||b_0||_inf. The complex extension is valid: the class gauge is real (an isometry), and the finite series estimates hold with complex absolute norms. SA 10129-10137 gives xi_j|A'| + xi_j^2|nabla_U A'| < alpha_1, so the first difference of the complex part is a hypothesis, as the text says at lines 237-239 and 347-349.
  - (4.3) dimension check: entries eta^4 m_c^{-3} times (m_c/eta)^4 read bonds gives the row sum m_c. Consistent.
  - (4.4) Cauchy on a + z h: valid if a lies in a smaller ball (say m_c||a|| < r_0/2) and c = r_0/2. The text says "a fixed complex supremum ball"; the shrink of the ball is implicit. Repairable wording only.
  - (4.4) to (4.1): the norm of a linear functional on the coordinate sup ball is the l^1 norm of its coefficients. Correct, and it removes the bond-count factor as claimed.
- (4.5): checked the units. eta^4 E(b,b') = sum_c m_c^3 j(c) D_b D_b' q_c; with |j| <= gamma_j m_c^{-3} and (4.1), the row sum is C gamma_j m_c^{-2} times the number of rows reading b, which is bounded by I5 (bounded heights) and bounded carriers per height. Correct.
- (4.6): weighted Schur test with row/column sums C gamma m^{-2} on comparable scales, then ||m^{-1}(A - D lambda)|| <= ||A||_E + ||lambda||_Lambda. Correct.
- (4.7): the averaging and A_s comparisons follow P82 lines 271-289 with the complex potential in the real class gauge. Correct.
- (4.8): Wilson comparison. The sixteen-term argument with |P-1| <= alpha_0 eta^2 m^{-2} gives a mass-size remainder. Accepted as the finite identity; I did not re-derive SA 11315-11384 line by line, but the stated form (a zeroth-order term of size eps m^{-2}) is what that algebra gives.
- (4.9): c_J terms. |lambda||A||J| <= gamma_0 (m^{-2}|lambda|)(m^{-1}|A|) and |lambda||D lambda||J| <= gamma_0 (m^{-2}|lambda|)(m^{-1}|D lambda|). Correct as an energy bound in E (+) Lambda. It uses no difference of J.

No defect in section 4. Note for later: (4.6) and (4.9) are energy (bilinear) bounds. They do not by themselves give a pointwise force class. Where the rough current force enters a pointwise estimate is checked in section 6.

## Section 5 (lines 401-582): energy premise and Schur factors

- Lemma 4 (lines 403-424): ||lambda||_Lambda <= C ||lambda||_{H^2_m}, then duality. Correct; only this direction is needed.
- Lines 426-436: baseline local eight-variable inverse in graph norm from I1 flat models and P82 Lemma 3 bare models, through the congruence of Lemma 1. The congruence maps (A; H, psi, M_s, N; u, v, n) to the eight variables with bounded maps in both directions (the only derivative is D^T A into an L^2 slot). So K_8,i^{-1} = T^{-1} diag(M_5,i^{-1}, -S_i^{-1}) T^{-T} is bounded. Correct.
- Row-multiplier-deleted local inverse (lines 430-436): deleting nu deletes only N (zeta = -N), so the seven-variable system is congruent to diag(M_4, -S). Its A-Schur complement is T_0 >= 0 on the real flat model, and Lemma 2 applies. Correct.
- Top mass b (lines 438-445): correct.
- Proposition 5 (lines 447-522): the parametrix B = sum chi_i K_i^{-1} chi_i with baseline (real, current-free, flat/bare) local inverses, and K - K_i bounded by (4.6)-(4.9) and the Wilson comparison (4.8). Checked:
  - The D A_s commutator split [D,chi]A_s + D[A_s,chi], with the outer D moved to the test field, costs C/M_P in E (+) Lambda. Correct.
  - Cutoff multiplication is bounded in the graph norm by A_s(chi lambda) = chi A_s lambda + [A_s,chi] lambda. Correct. The bounded-overlap and duality step is the I2 argument repeated for the graph norm; this is a routine extension, not a quoted I2 statement. Acceptable.
  - Neumann series and finite propagation give (5.1) with tau = log 2/(D_L M_P), as in P82 Lemma 4. Correct.
  - The complex and current-corrected systems are not assumed positive. Only the local baselines use positivity (Lemma 2). This is the right way past the positivity gap.
- The proposition needs gamma_j below an early ceiling (line 499-503: "the four early ceilings"). The coefficient j at the G_1 stage is j = H^T J. Whether gamma_j is small, fixed before kappa-bar, at switched parameters, is checked in sections 7-8. Resolved there: gamma_j is an early constant.
- 5.1 (lines 527-582): checked.
  - (5.4) Poincare: ||m^{-1}(lambda - mean)||^2 <= C ||D lambda||^2 on a pillar, and the mean is Q'lambda on flat pillars. The curved correction C alpha_0^2 ||m^{-1}lambda||^2 uses P82 (18) and |D_U - D_1| <= C alpha_0/m. Correct.
  - Invertibility of the complex A_s by a form perturbation of size C alpha_1 in H^1-type energy. Correct.
  - Null vector of Q'A_s^{-2}Q'^T gives the null vector (h, lambda, mu) = (A_s^{-1}Q'^T mu, -A_s^{-2}Q'^T mu, mu) of the scalar system X. Checked: X(h,lambda,mu) = 0. Correct.
  - T invertible from the seven-variable inverse and X invertible; then QT^{-1}Q^T invertible from the eight-variable inverse. Correct finite Schur argument.
  - The displayed T matches h-walk Lemma U(b), with S A = A - D lambda_A. Correct.

## Section 6 (lines 583-809): local energy to field and first difference

- (6.4) checked against the h-walk unfolded rows. With q_{A lambda} lambda = (1/2) D A_s lambda, q_{lambda A} = (1/2) A_s D^T, h' = p - D^T A/2 and the Z-row identity A_s lambda = D^T A + g'_h - h, the A-row becomes (Delta^W + DD^T)A = f_o + Dp + Dh/2 - Q^T a Q A - Q^T nu - F_A, with f = f_o + D g'_h/2. The lambda-component of the Y-row becomes A_s p = g_lambda + Q'^T mu' - (current terms): the two (1/2)A_s D^T A terms cancel. The other rows are read off directly. All eight lines correct.
- (6.5): the c_J derivative in lambda gives endpoint products J x A, J x D lambda (zeroth order, bounded) and one term <i[lambda, D mu], J>, which is D^T of a flux J x lambda. The flux is bounded pointwise by gamma_0 m^{-3}|lambda|. No difference of J is used. E_j enters as E_j(A - D lambda) and its divergence, bounded in L^q by the row and column sums (4.5). Correct.
- This is how the text passes the draft's first failure (dr-draft section 6: the rough force D(R G' D^T Z) is not in P82's force class). The rough current force is never put into a pointwise force class. It stays a divergence in the p equation; p is estimated only in W^{1,8}; the field equation sees only Dp in L^8. P82's pointwise lemmas (I3, I8) are not used at all; section 6 proves its own local estimates. I find this route sound.
- (6.7): Fourier proof of |D^k G_eta| <= C(|x|+eta)^{-2-k}, k <= 3. Small-ball part R^{-2-k}; outer part after k+3 integrations by parts gives R^{-(k+3)} times int_{|t|>1/R} |t|^{-5} d^4t = C R. Correct (smooth split assumed, as the text says).
- Weak (1,1) and Marcinkiewicz for D_i D_j^* Delta^{-1}: standard Calderon-Zygmund argument; the good-part bound 16 t ||f||_1 is the 4D factor 2^4. Correct. Duality for q > 2: the transposed kernel has the same bounds. Correct.
- (6.8): interior W^{2,q} and divergence-form W^{1,q}. Standard; accepted.
- (6.9): Young with DG in L^a, a < 4/3. Exponents checked: 1 + 1/3 = 5/6 + 1/2 (a = 6/5); 1 + 1/8 = 19/24 + 1/3 (a = 24/19); 1 = 7/8 + 1/8 (a = 8/7). All a < 4/3. Correct.
- Bootstrap (lines 721-744): checked each round. Round 0: lambda, lambda' in W^{2,2} from A_s lambda in L^2; h, p in W^{1,2} with the drift in divergence form (needs |dB| bounded, which SA's xi^2|nabla A'| < alpha_1 gives); then h in W^{2,2}; then A in W^{2,2} since Dp, Dh in L^2 and (4.8). Round L^3 and round L^8: the right-hand sides are in L^3 (then L^8) by (6.9), (6.5) and the previous round. The order (p before A) is respected. The drift is moved to the right-hand side using the previous round, so no smallness of B is needed for the bootstrap. Correct.
- The field output: A in W^{2,8} in scale-one units gives |A| and |nabla A| in sup by (6.9). This is the X_w output. Correct.
- 6.1 commutator closure: checked by hand.
  - g'_h = -[D^T,chi]A + [A_s,chi]lambda. Correct.
  - (6.10): [D A_s, chi] = [D,chi]A_s + D[A_s,chi]; subtracting D g'_h/2 cancels D[A_s,chi]lambda/2 and adds D[D^T,chi]A/2. Matches (6.10). Each term is in L^8 given A, lambda in W^{2,8}, h' = p - D^T A/2 in L^8. Correct.
  - (6.11): [A_s D^T,chi] = A_s[D^T,chi] + [A_s,chi]D^T and h' = p - D^T A/2 give the identity. Checked. The term A_s[D^T,chi]A is a divergence of D((nabla chi)A), which uses two cutoff differences and one of A. Correct.
  - Source and solution multiplication rules: (chi F)_o = chi f_o - [D,chi]g'_h/2 and p(chi Psi) = chi p + [D^T,chi]A/2. Checked. Correct.
  - (6.12) with first two scaled cutoff differences O(M_1^{-1}). Correct given the walk cutoffs live on scale M_1 m.
- (6.13): Proposition 5 plus (6.6). Correct.

No defect in section 6. The passage from energy to the pointwise field and its first difference is mesh-uniform (Calderon-Zygmund constants are lattice-uniform; bounded radius/mesh uses point evaluation) and closes under the cutoffs.

## Section 7 (lines 810-953): actual walks, second lift, composed Green operator

- (7.1): each walk step costs C_L/M_1 by (6.12) and carries e^{-tau d} by (6.13). Half the exponent pays the path through the cells; the other half sums intermediate pillars by I4 at rate tau/2 (gap floor 16 log L/(tau/2)). Correct.
- Lines 831-850, the coefficient j_beta: checked the normalization. h-walk's nu row is physical, [K^{-1}]_{A nu} is the per-length lift, and (H^T J)(c) = m_c^{-4}<H e_c, J>_f by the physical row weight m_c^4. The source e_c has S-norm m_c; <A,J>_{f,y} <= C gamma_0 ||A||_{X,y} by pillarwise Cauchy-Schwarz (||mJ||_{2,y} <= gamma_0). So m_c^3|j_beta(c)| <= C gamma_0 (C/M_1)^{|beta|} e^{-(tau/4)t}. Correct; the raw/per-length bookkeeping is terse but consistent with O1D (2.1), H(s) = H-sans(s) m^{-1}.
- Important check (my concern from section 5): the coefficient j of the second system is built from the UNSWITCHED walk terms of the first lift (line 812: "All coefficients in this section are unswitched coefficients until section 8"). So gamma_j <= max(C_0, C_J) gamma_0 is an early constant, independent of kappa-bar. The switch then multiplies the whole tree once (section 8). This matches dr.md section 1 ("Tag every closed fine cube meeting a coefficient's full connected enlarged hull once ... branches carry their own reads") and SA 10548 (mechanism (g): the length-zero part stays in the local operators; the remainder is a small vertex). No circularity: the first system has j = 0.
- K_1 B^{(0)} = 1 - R^{(0)} + sum V_beta B^{(0)}: correct, with j^{(0)} in the local matrices (Proposition 5 accepts any j with sup m^3|j| <= gamma_j).
- (7.3): with n trunk factors, v of them vertices, branch lengths m_i >= 1, N = n + sum m_i + v; 3p_* - N = 2n - 4v + 2 sum m_i = 2(n-v) + 2 sum(m_i - 1) >= 0. Checked. So M_1^{-p_*} <= M_1^{-N/3}, giving (7.4). Correct.
- Tree count C_0 C_1^N: bounded overlap of cells; accepted.
- Lines 905-917: AA blocks sum to G_1 - H_1 Q G_1 (h-walk Lemma U(c)); deleting nu gives G_1; scalar h<-h block is P = 1 - R (P82 Lemma 2). Correct.
- (7.5)-(7.6): type chain checked: m^3 f -> mA (W^{2,8}) -> m^2 D^T A -> m^2 h (L_sigma accepts an L^8 scalar input in the h-slot; A_s h = Q'^T mu, A_s lambda = s_h - h give W^{2,8}) -> m^3 Dh -> mA_out. Scalings consistent with (6.2)-(6.3). Correct.
- (7.7): each factor has rate tau/4; 3 tau/16 kept on the tree, tau/16 per intermediate sum (at most two). Correct. (N+1)^2 <= 4^{N+1}. Correct.

No defect in section 7.

## Section 8 (lines 955-1049): switches

- (8.1) is the composite-before-tagging specification of dr.md section 1 and dec-field (5.3) (checked: dec-field line 283-287 says the third term needs its own composed expansion and forbids multiplying separately decoupled factors). The text uses exactly that. Correct.
- (8.2): double traversal of a tree of length t gives at most 8t/l_P + 1 arcs of length <= l_P/4; with l_P > 8R_* each R_*-thickened arc has diameter < l_P/2 and meets at most 16 cubes under (P). So #P <= 16 + 128t/l_P and |s^P| <= e^{16 kappa-bar} e^{128 kappa-bar t/l_P}. Checked. (O1D Lemma P has 64 for a single path; 128 is the tree version.) Correct.
- (8.3): 128 kappa-bar/l_P <= tau/16 iff l_P >= 2048 kappa-bar/tau. Checked.
- Exponent ledger: H: tau/2 - tau/16 >= tau/8; H_1, G: 3 tau/16 - tau/16 = tau/8. The switch factor is applied per walk/tree before the sum over walks; the walk count is paid by (C_L M_1^{-1/3})^N, not by the exponent; t_omega >= d(y,z) gives the endpoint decay. Correct.
- The e^{16 kappa-bar} factor appears once per connected composite hull (the composite factors overlap at their joining cells, so the hull is connected). Correct; this is why the bound is e^{16 kappa-bar} and not e^{48 kappa-bar}.
- s != 1: the text never uses an equation for a switched sum. Each switched sum is an absolutely convergent sum of unswitched terms times monomials s^{P(omega)}; every term is bounded by the unswitched termwise estimates of sections 6-7, which are estimates of genuine local inverses (which do satisfy local equations) and commutators. This is how the text passes the draft's second and third failures (dr-draft 6.4: decoupled sums satisfy no equation; 6.5.1: Definition D termwise bounds blocked by the rough current in the unfolded scalar rows). The termwise block of 6.5.1 is removed by section 6: in the unfolded system the current sits only in the A-row and in the lambda-component of the Y-row, whose unknown is p (= h' + D^T A/2); the lambda of Y solves the Z-row A_s lambda = D^T A + g'_h - h, which has no current, so D lambda is bounded in sup; and p is needed only in W^{1,8}. WW is not needed. I find this sound.
- Weights (lines 1026-1033): w(y)/w(z) <= e^{theta d}, theta <= tau/16, leaves e^{-(tau/16)d}, summed by K_{tau/16} (I4, gap floor 256 log L/tau, stated in section 9 item 2). Pillar pieces of a force have S-norm <= C w(z)^{-1}||f||_{F,w} since the S-norm is an L^8 average of m^3 f. Correct. No derivative of a weight or switch is taken.
- (8.5): sum P - G D D^T G + G D P D^T G = G_1 - H_1 Q G_1 - G_1 D (1-P) D^T G_1 = G_1 - H_1 Q G_1 - G_1 D R D^T G_1. Matches dec-field (5.3) and SA 10141-10155 (S = 1 - D G' R D^T, G_1 with Delta^(2)[H^T J]). Correct.
- Line 984: the count uses Hypothesis (P) on the parameter partition. See finding F3.

## Section 9 (lines 1051-1117): constant order

Checked against IN1 rows 1-10 and Amendment 1 (in1.md lines 227-236), dr.md section 1 "Order", P82 section 2 and SA 10582.
- L (row 2, with L_0^natural), then M_P, tau, cut-down gap with tau rho' >= 256 log L (row 3), then the current ceiling max(C_0,C_J) gamma_0 <= gamma_j, then M_1, R_1, then C_PW: all before kappa (row 4). Correct. The current ceiling is an early upper bound; IN1 row 6 later picks the actual current radius below it, as dr.md does with gamma_*. SA 10582 also places the ceiling on alpha_0, alpha_1, gamma_0 in the L group, before M_1. Consistent.
- kappa-bar (row 5), then l_P by (8.3), then M. Matches IN1 row 5 ("response-parameter length ... then M") and dr.md's order. Correct.
- C_PW and tau do not depend on M or kappa-bar. Correct.

## Section 10 and Result (lines 1119-1197)

- Source lines checked: SA 10129-10137 (regular pairs; the first-difference bound on A' and |J| < gamma_0 xi^{-3} with no difference bound on J: matches the text's use); SA 10139 (row mass a = a_0 xi^{-2}, comparable top weight: matches); SA 10141-10155 (defining inverses in order G, H, G_1, H_1; S = 1 - D G' R D^T; (A, Delta^(2)[j]A) = 2(C^(2)(A), j): consistent with (4.5) and section 5.1); SA 10369-10372 and 10562 (no identities on decoupled sums; QH(s) = 0 near killed rows: matches line 30-32); SA 10384 (C e^{16 kappa-bar}, not used as proof: matches); SA 10548-10552 (trees, length against parameters: matches sections 7-8). I did not read SA 11315-11384 and 11510-11639 line by line or CA-I 49495-49547 (the CA file was not in the supplied scratch). The text does not rest on them: it reproves the Wilson comparison (4.8) and the second-jet bound (Lemma 3) by hand.
- Library sources checked: p82.md sections 1-4 (I1, I2, I4, I5 as stated; Lemmas 1-4); h-walk.md section 4; o1-decoupled.md Definition D, (P), Lemma P, Theorem B; dr.md section 1; dr-draft.md section 6; dec-field.md (5.3); in1.md order table. Used as stated.

## Verdict

[PW] is proved as claimed. The proof covers H(s), H_1(s) and G(s) of the dr.md section 1 walk family, on every admitted real or complex regular pair with independent bounded current, for all weights of rate theta <= tau/16, with C_PW and tau fixed before kappa. It is conditional, as the text says, on frozen P82 (I1, I2, I4, I5 and the Lemmas 1-4 proved from them), the h-walk walk structure in the dr.md specification, and the regular-pair envelope. It is subject to F3: the "whole decoupling polydisc" claim holds for parameter partitions satisfying Hypothesis (P), the premise O1D Theorem B already carries. The Result should name (P). F1 and F2 are wording repairs. The chain-domain admission (dr.md line 32) stays outside [PW], as the text says.

Checked line by line by Claude (fresh session).
