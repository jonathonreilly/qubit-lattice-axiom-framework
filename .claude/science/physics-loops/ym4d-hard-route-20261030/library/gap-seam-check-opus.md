# Check of library/gap-seam-astra.md (FINISH row 798), by Claude Opus 5.5, line by line

- Checker: Claude Opus 5.5, one session, no subagents, 2026-11-12. Cross-provider check of a Codex gpt-6-astra max note.
- Clone read: `/Users/jonreilly/ym4d-lead/clone`, HEAD `8c4f5a61621350d8f2f6646578ab083de732fb77`.
- File checked (read in full, 847 lines): `.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-seam-astra.md`. The note calls itself FINISH row 796 (lines 22, 26). The header uses row 798 as requested.
- Context read: `gap-ext-astra.md` Section 5.1 ((E21)-(E23), lines 574-673); `gap-ext-check-opus.md` in full; `gap-trf-astra.md` lines 95-210 ((T1)-(T5)); the (T3)-(T5) and (T7) items of `gap-trf-check-opus.md`.
- Method: by hand. One GUIDE run (scalar sign check of Lemma 1 on a = 4, 8 and the failure of periodicity at a = 6; script `guide_lemma1.py` next to this report, under 1 MB). It agreed with the hand proof and decides nothing.
- Not checked: Section 9 (search record, source excerpts, hashes); the GUIDE paragraph of Section 6.

## 1. (S2), the seam cochain (S4), the identities (S5)

**(S2).** It is (E22)-(E23) with m = 0, mu = mu_+, mu' = mu_(eta_0), F = -log(Z_(eta_0)/Z_+). Row 791 checked (E23) and F >= 0. HOLDS.

**(S4).** Sigma_0 = {p_13(x): x_1 = x_3 = 0} is closed mod 2. A 3-cube in directions 1, 3, nu (nu = 2, 4) has its two 13-faces at the same (x_1, x_3); both lie in Sigma_0 or neither. Cubes 124 and 234 have no 13-face. A unit shift is explicit: b = {e_3(x): x_1 = 0, x_3 = 0} has delta b = 1_(Sigma_(0,0)) + 1_(Sigma_(-1,0)). Plaquettes 23 and 34 contain two such 3-links or none, so they get 0. A shift in x_3 uses 1-links the same way. Composing shifts gives b for any t. HOLDS.

**(S5), first identity.** U_p(B_b V) = (-1)^((delta b)_p) U_p(V), because the signs are central. So eta_(0,p) (-1)^((delta b)_p) = (-1)^(1_(Sigma_0) + 1_(Sigma_0) + 1_(Sigma_t)) = eta_(t,p) on every plaquette. HOLDS.

**(S5), second identity.** B_b is an involution and preserves Haar. The density of (B_b)_* mu_(eta_t) at V is Z_(eta_t)^(-1) exp(-S_(eta_t)(B_b V)) = Z_(eta_t)^(-1) exp(-S_(eta_0)(V)). The substitution V -> B_b V in Z_(eta_t) gives Z_(eta_t) = Z_(eta_0). HOLDS.

**(S5), third identity (the information term).** Pushforward by one bijection commutes with mixing: (B_b)_* nu = sum_j pi_j (B_b)_* nu_j. Relative entropy is invariant under a common measurable bijection with measurable inverse. So D((B_b)_* nu_j || (B_b)_* nu) = D(nu_j || nu) for every j, and I_pi is unchanged. The substitution must be common to all labels; Section 2 requires that. HOLDS.

**Reduction.** For T_j = B_b R_j the summands become E[S_(eta_t)(R_j U) - S_+(U)]. The right side becomes F + D(nu_R || mu_(eta_t)), with the same F. This is (E23) for the representative eta_t. HOLDS.

Verdict for item 1: HOLDS.

## 2. The class (S6)-(S7)

**At most one link of A per plaquette.** A plaquette p_(nu rho) with nu, rho != mu has no mu-link. A plaquette p_(mu nu)(x) has two mu-links, e_mu(x) and e_mu(x + nu). Their x_nu parities differ, so at most one lies in A. HOLDS. Each link of A lies in 6 plaquettes, and no plaquette is shared by two links of A. There are 4 x 2^3 = 32 colours. HOLDS.

**What the class allows.** Each R_j fixes U_W, acts on each fibre by a Haar-preserving bijection of SU(2)^A with measurable inverse, and its e-output reads u on Q_(j,e) subset A cap B_R(e), with arbitrary dependence on w. The count |Q_(j,e)| <= (2R+1)^4 holds for the l-infinity coordinate ball, and a fortiori for l1 or Euclidean balls; A has at most one link per base. The inverse may be nonlocal; displacements and the number of maps are unbounded; labels may be correlated, with field-independent probabilities. The proofs below use exactly these properties. HOLDS.

**Seam-first maps (lines 182-184).** R_j = B_b Q_j B_b. On W it returns (B_b)^2 w = w. On the fibre it is a sign flip, a Haar-preserving fibre map at the exterior (B_b w)_W, and a sign flip. Sign flips preserve Haar and do not change which inputs an output reads. Exterior dependence is arbitrary, so the new exterior argument is allowed. HOLDS.

**What it excludes.** A composition of maps of two colours changes links of both colours. Neither colour's W is then fixed, so it falls outside the class. The note says so (lines 186-189, 585-590). HOLDS. "Failure on the subsequence 4 | a defeats the uniform supplier" is correct: (TR-F) must hold for every a. HOLDS.

Verdict for item 2: HOLDS.

## 3. (S8)-(S11)

**(S8).** Given U_W = w, the Wilson weight exp(beta sum_p s_p) splits into plaquettes not meeting A (functions of w) and plaquettes meeting A in one link e. For the latter, cyclicity, and tr X = tr X^(-1) in SU(2), write s_p = (1/2) tr(U_e K_p) with K_p the staple. So the conditional density is prod_e exp(beta ell_(H_e)(u_e))/norm. HOLDS. The target conditional law is the same product with signed staples H_e^t, since the at-most-one property does not depend on eta. HOLDS.

**(S9).** Write S_eta(v, w) = beta sum_(p not in P_A)(1 - eta_p s_p(w)) + beta |P_A| - beta sum_(e in A) ell_(H_e^eta)(v_e). Subtract the eta = + case at (u, w). The constants beta |P_A| cancel. Off P_A the difference is beta (1 - eta_(t,p)) s_p(w). On P_A it is beta [ell_(H_e)(u_e) - ell_(H_e^t)(v_e)]. This is (S9), with the stated signs. Each plaquette of P_A has exactly one link of A, so it enters exactly one staple sum, once. HOLDS. For mu = 1, 3 the a^2 - a^2/4 sheet plaquettes outside P_A appear in the first sum as 2 beta s_p(w); for mu = 2, 4 all a^2 do.

**(S10).** The joint density of mu_+ on W x A is rho_W(w) p_A(u | w). R_j acts by R_(j,w) on each fibre and preserves Haar there. So the pushforward density is rho_W(w) p_A(R_(j,w)^(-1) v | w). HOLDS. The W-marginal of every nu_j is rho_W. Hence the conditional label weights given W = w remain pi_j. This fact is used silently in Lemma 2; it holds because all maps in one class fix the same W.

**(S11).** rho = sum_j pi_j rho_j = rho_W f, and rho_j/rho = f_j/f. HOLDS.

Verdict for item 3: HOLDS.

## 4. Lemma 1: (S12)-(S13)

**Periodicity.** The exponent in (S13) does not involve y_mu. Replacing y_nu by y_nu + a changes floor((y_nu - eps_nu)/2) by a/2. This is even iff 4 | a. So (S13) is well defined on the torus exactly when 4 | a. HOLDS. GUIDE: the scalar check finds the parity of the exponent changes at a = 6.

**Opposite signs.** For f = e_mu(x) in A, x_nu - eps_nu = 2k. The neighbours e_mu(x +- nu) have the other x_nu parity, so they are in W. Their nu-floors are k and k - 1; the other floors agree. So the signs are opposite. HOLDS. The wrap-around case x_nu = a - 1 is covered by periodicity.

**Staple cancellation.** In p_(mu nu)(x) the staple is U_nu(x+mu) U_mu(x+nu)^(-1) U_nu(x)^(-1) = sigma_+ I. In p_(mu nu)(x - nu), U_e appears inverted; with tr X = tr X^(-1) the staple is sigma_- I. sigma_+ + sigma_- = 0 for each of the three transverse nu. So H_f(w^*) = 0 for every f in A, with no condition on links of A. HOLDS.

**(S12).** For mu = 1, e = e_1(x) lies in the 13-plaquettes based at x and x - 3. Both lie on Sigma_t iff x_1 = t_1 and x_3 is t_3 or t_3 + 1. Only one of those has parity eps_3. So e lies in exactly one sheet plaquette. The same holds for mu = 3. Flipping the sign of that staple, z_e I, turns 0 into -2 z_e I. HOLDS. GUIDE: the scalar check gives H = 0 on all of A and |H^t| = 2 on all sheet links, for a = 4, 8, three parity choices, mu = 1, 2, 3.

Verdict for item 4: HOLDS.

## 5. Lemma 2: (S14)-(S18) and p_R

**m and m_*.** g -> -g preserves Haar and sends s to -s. So int s e^(ts) = int s sinh(ts) > 0 for t > 0, and m' = Var_t(s) > 0. So m(2 beta) >= m(2 beta_-) = m_* on I. HOLDS. Also m_* < 1, used in item 8.

**F_e and (S15).** Each f in Q_e has six staples of three links each, all in W by item 2. So |F_e| <= 18 M_R. On E_e each staple factor is within delta_R of its central reference value. ||ABC - A_0 B_0 C_0|| <= ||A - A_0|| + ||B - B_0|| + ||C - C_0|| for unitaries, and ||A^(-1) - A_0^(-1)|| = ||A - A_0||. So each staple moves by at most 3 delta_R and each six-staple sum by at most 18 delta_R. With H_f(w^*) = 0 and H_e^t(w^*) = -2 z_e I this is (S15). HOLDS.

**(S16).** |ell_H(g)| = |(1/2) Re tr(gH)| <= ||gH||_op = ||H||_op. With ||H_f|| <= 18 delta_R, the numerator and the normalizer of p_f each lie in [e^(-18 beta delta_R), e^(18 beta delta_R)]. So p_f / Haar lies in [e^(-36 beta_+ delta_R), e^(36 beta_+ delta_R)]. Given w the inputs are independent (S8), so the product over Q_e lies within e^(+-theta_R). The choice of delta_R gives e^(theta_R) - 1 <= m_*/4. HOLDS.

**The key step (lines 345-351).** Fix w outside the finite union of null sets. Let u ~ Haar^A. Then R_(j,w) u ~ Haar^A, so its e-component is Haar on SU(2). That component equals G(u_(Q_(j,e))) for a measurable G = G_(j,e,w). The law of G(u_Q) depends only on the law of u_Q, which is Haar^Q. Hence G_* Haar^Q = Haar. Haar preservation of the whole fibre map therefore does imply that the marginal map from the Q-inputs to the one output link is Haar-preserving. Now let u_Q have density h with e^(-theta) <= h <= e^(theta) relative to Haar^Q; the marginal of the product (S16) on Q_(j,e) subset Q_e obeys the same bounds. For every Borel B, P(G(u_Q) in B) = int 1_(G^(-1)B) h dHaar^Q, which lies between e^(-theta) Haar^Q(G^(-1)B) = e^(-theta) Haar(B) and e^(theta) Haar(B). So the output density lies within e^(+-theta_R). HOLDS. A convex combination keeps these bounds. The conditional weights given w are pi_j by item 3. HOLDS. No property of the other outputs or of the inverse is used.

**(S17).** |E_nu phi_e| = |int phi_e (h - 1) dHaar| <= sup |h - 1| <= e^(theta_R) - 1, since |phi_e| <= 1 and 1 - e^(-theta) <= e^(theta) - 1. HOLDS.

**Target mean.** At w^*, q_e is proportional to exp(beta ell_(-2 z_e I)(g)) = exp(-2 beta z_e s(g)) = exp(2 beta phi_e(g)). The substitution g -> -z_e g (Haar invariant) gives mean m(2 beta). At w in E_e the density ratio actual/ideal is exp(beta ell_(H^t + 2zI)) / normalizer, within e^(+-36 beta_+ delta_R) by (S15). The mean of phi_e shifts by at most e^(36 beta_+ delta_R) - 1 <= e^(theta_R) - 1 <= m_*/4 (M_R >= 1). So E_q phi_e >= 3 m_*/4. HOLDS.

**Pinsker step.** The mean gap is h >= 3m_*/4 - m_*/4 = m_*/2. A test in [-1, 1] gives TV >= h/2 = m_*/4. Data processing to the TV set gives a Bernoulli divergence. Its second derivative in the first argument is 1/(t(1-t)) >= 4, with value and slope zero at equality. So D >= 2 TV^2 >= m_*^2/8. HOLDS (same argument as row 791, item 5f). The direction D(nu_e || q_e) is the one Theorem 3 needs.

**p_R.** Condition on all links outside F_e. The log density of U_(F_e) relative to product Haar is beta sum_(p meets F_e) s_p plus a constant. At most 6 |F_e| <= 108 M_R plaquettes meet F_e, each s_p in [-1, 1]. So the oscillation is at most 216 beta_+ M_R and the normalized density is at least e^(-216 beta_+ M_R). Each ball around +-I has Haar measure v_R by invariance. So the Haar mass of E_e is v_R^(|F_e|) >= v_R^(18 M_R). Hence mu_+(E_e) >= p_R. HOLDS. No independence of events is used.

**Precision.** The cap delta_R <= 1/12 is not used in Lemma 2; it serves Corollary 5 (sin theta >= theta/2). Harmless.

Verdict for item 5: HOLDS. The key claim is correct for the reason above.

## 6. Theorem 3: the count, (S20)-(S23)

**Count a^2/4 (mu = 1).** e_1(x) in A needs x_2, x_3, x_4 at parities eps. On the sheet, x_1 = t_1 and x_3 is the one of t_3, t_3 + 1 with parity eps_3. x_2 and x_4 have a/2 choices each. So a^2/4 links. Direction-3 links are not in A. The case mu = 3 is symmetric. HOLDS (GUIDE agrees for a = 4, 8).

**(S20).** nu has W-marginal mu_(+,W) and conditional f(.|w). mu_(eta_t) has W-marginal mu_(eta_t,W) and conditional q_A(.|w), a product by item 3. The chain rule gives (S20). HOLDS.

**(S21).** log(f / prod q_e) = log(f / prod f_e) + sum_e log(f_e / q_e). Integrate against f. The f_e are the one-link marginals of f. All terms are finite: f(.|w) is a mixture of p_A(R^(-1) v | w), bounded above and away from zero on the finite torus, and so is q_A. HOLDS.

**(S22).** Drop the first term of (S20) and the first term of (S21). For each of the a^2/4 sheet links, Lemma 2 gives D(f_e(.|w) || q_e(.|w)) >= m_*^2/8 for a.e. w in E_e. Integrate: at least mu_+(E_e) m_*^2/8 >= p_R m_*^2/8 = d_R. Summing gives d_R a^2/4. HOLDS. The overlap of the E_e is harmless: the sum is over e inside one integral.

**Conclusion, mu = 1, 3.** C = F + D(nu || mu_(eta_t)) >= d_R a^2/4 >= c_R a^2, with F >= 0. HOLDS.

**(S23), mu = 2, 4.** The links of A are direction-2 (or 4) links. Sheet plaquettes are 13-plaquettes with only direction-1 and 3 links. So R_j changes no sheet link and E_nu s_p = E_(mu_+) s_p >= r_I by (T5) (a >= 4 >= 3). With X = S_(eta_t) - S_+ = 2 beta sum_(Sigma_t) s_p, (E23) reads C = E_nu X + D(nu || mu_+) >= 2 beta_- r_I a^2. HOLDS.

**Constant.** c_R = min{2 beta_- r_I, d_R/4} depends only on I and R. HOLDS.

Verdict for item 6: HOLDS.

## 7. Corollary 4: (S25)-(S26)

**Grouping.** There are 32 colours and a^2 flat residual 13-sheets (t_1, t_3). So at most 32 a^2 groups. HOLDS.

**(S25).** For two cochains with the same sheet, c_j = b_j + b_g has delta c_j = 0. B_(c_j) changes no plaquette trace, so it preserves mu_+; it is a sign flip, so it preserves Haar. B_(b_j) R_j = B_(b_g) (B_(c_j) R_j B_(c_j)) B_(c_j), and (B_(c_j))_* mu_+ = mu_+. This is (S25). HOLDS. The conjugated map stays in the class by the argument of item 2 (seam-first maps): it fixes W, is Haar-preserving on each fibre, and reads the same inputs. HOLDS.

**Group cost.** The cost depends on the maps only through the output laws nu_j and the weights: C = sum_j pi_j E_(nu_j) S_(eta_0) - E_(mu_+) S_+ - I_pi. So C_g, for weights pi_j/w_g, is unchanged by (S25), and by (S5) equals the cost of the R~_j against mu_(eta_t). Theorem 3 gives C_g >= c_R a^2. HOLDS.

**(S26).** G is a function of the label J. The chain rule for mutual information, I(J; V) = I(G; V) + I(J; V | G), is the identity sum_j pi_j D(nu_j || nu) = sum_g w_g sum_(j in g) (pi_j/w_g) D(nu_j || nu_g) + sum_g w_g D(nu_g || nu). The action terms split linearly. This gives C = sum_g w_g C_g - I(G; V). HOLDS. nu >= w_g nu_g gives d nu_g/d nu <= 1/w_g, so D(nu_g || nu) <= log(1/w_g) and I(G; V) <= H(w) <= log(32 a^2). HOLDS.

**Ceiling.** log(32 a^2) <= log 32 + 2a <= 5 + 2a <= 4a for a >= 4. For a >= 8/c_R, c_R a^2 - 4a >= c_R a^2/2 >= 4a >= 16 > 1/96. HOLDS.

Verdict for item 7: HOLDS.

## 8. Corollary 5: (S24a)-(S24d)

**Angle density.** An SU(2) element with eigenvalues e^(+-i theta), theta in [0, pi], has Haar law (2/pi) sin^2 theta d theta. ||g - I||_op = 2 sin(theta/2) <= theta. On [0, delta_R], delta_R <= 1/12, sin theta >= theta/2. So v_R >= (2/pi) int_0^delta (theta^2/4) d theta = delta_R^3/(6 pi). HOLDS. delta_R >= k_I/M since M >= 1. So v_R >= k_I^3/(6 pi M^3). HOLDS.

**(S24d).** p_R >= exp{-216 beta_+ M - 18 M log(6 pi/k_I^3) - 54 M log M}, since 18 M log(M^3) = 54 M log M. d_R/4 = p_R m_*^2/32. HOLDS.

**c_R >= exp[-L_I M log(eM)].** Every term of L_I is nonnegative: 6 pi/k_I^3 > 1, 32/m_*^2 > 32 since m_* < 1, and the max term. With log(eM) >= 1 and M log(eM) >= 1: 216 beta_+ M <= 216 beta_+ M log(eM); 18 M log(6pi/k^3) <= 18 log(6pi/k^3) M log(eM); 54 M log M <= 54 M log(eM); log(32/m_*^2) <= log(32/m_*^2) M log(eM). So d_R/4 >= exp(-L_I M log eM). Also log(1/(2 beta_- r_I)) <= L_I <= L_I M log(eM). Both branches of the minimum are bounded. HOLDS.

**(S24b).** One class, C <= epsilon_a and C >= c_R a^2 give exp(-L_I M log eM) a^2 <= epsilon_a, which is the first inequality. epsilon_a <= C_1 a^(p_1) eta_*^(a/2)/4 gives -log epsilon_a >= (a/2) log(1/eta_*) - p_1 log a + log(4/C_1). HOLDS.

**(S24c).** C >= c_R a^2 - log(32 a^2) and C <= 1/96 give c_R a^2 <= log(32 a^2) + 1/96. HOLDS. Its right side tends to infinity, so M_R must grow. "No uniformly bounded range" HOLDS. (S24b) gives the sharper M_R log(e M_R) >= c a for one class.

**Varying R.** Theorem 3 and Corollary 4 hold for each a and each R, with constants depending only on R. So R = R(a) is allowed. HOLDS.

Verdict for item 8: HOLDS.

## 9. Section 6: (S27)-(S28) and the shear; Section 7: (S29)-(S31)

**Polar form.** A sum of SU(2) elements is a real quaternion H with H^* H = h^2 I. So H = h V with V in SU(2) when h > 0. HOLDS.

**(S27) is in the class.** V_e, W_e and the branch condition depend only on w. Each output reads only u_e, so Q = {e}. Left multiplication by a w-measurable SU(2) element preserves Haar, and its inverse is left multiplication by V_e^* W_e. HOLDS.

**Output law.** u has density proportional to exp(t (1/2) tr(u V)), t = beta h. With g = W^* V u, u = V^* W g and tr(V^* W g V) = tr(W g). So the output density is proportional to exp(t ell_W(g)). The target has exp(s ell_W(g)), s = beta k. HOLDS.

**(S28).** Both normalizers are c_0 by the substitution g -> g W^*. E_t ell_W = m(t). So D = (t - s) m(t) - log c_0(t) + log c_0(s). This is the Bregman divergence of log c_0, which is strictly convex (second derivative Var_t(s) > 0). So D > 0 unless t = s. HOLDS. For h = 0, D(Haar || q) = log c_0(s) > 0 when k > 0. HOLDS. *Precision:* the branch h > 0, k = 0 (identity map, Haar target) is not mentioned. It gives D = t m(t) - log c_0(t) > 0, the case s = 0 of (S28). No conclusion changes.

**The shear does not raise expected target action.** Under exp(t ell_V(u)), u = V^* g with g ~ exp(t s(g)); conjugation invariance gives E g = m(t) I, so E u = m(t) V^*. Before the shear, E ell_(kW)(u) = (k/2) tr(E u W) = k m(t) (1/2) tr(V^* W). After it, (k/2) tr(W^* V u W) = (k/2) tr(V u), with mean k m(t). The gain k m(t)(1 - (1/2) tr(V^* W)) >= 0, since k, m(t) >= 0 and (1/2) tr <= 1. By (S9) the target action changes by -beta times the sum of these gains, each plaquette once. So the expected target action does not increase. HOLDS. The statement "lowers" in the brief is "does not increase" in the note; equality occurs when V_e = W_e. Theorem 3 still applies, since (S27) is in the class. HOLDS.

**(S29).** Each path composes Haar-preserving bijections, so each cumulative map is one. (E23) gives C_s = F + D(lambda_s || mu_(eta_0)). I_0 = 0 because every path starts with the same B_b. Labels are full paths; components at scale s - 1 depend only on prefixes, and the definition of I_(s-1) with full labels agrees with prefix labels. HOLDS.

**(S30).** S_eta(U_s) - S_eta(U_(s-1)) = beta sum_p eta_p (s_p(U_(s-1)) - s_p(U_s)). Subtract I_s - I_(s-1). HOLDS.

**(S31).** C_0 = E[S_(eta_t)(U) - S_+(U)] = 2 beta sum_(Sigma_t) E s_p = 2 beta a^2 E s_p >= 2 beta_- r_I a^2 by (T5). C_J = C_0 + sum b_s telescopes. HOLDS. Lines 697-700: C_1 >= c_R a^2 - log(32 a^2) and C_J <= epsilon_a give C_1 - C_J >= c_R a^2 - log(32 a^2) - epsilon_a. The seam-first form of the first relaxation is in the class by item 2. HOLDS.

**Information convention.** A Haar-preserving bijection preserves differential entropy, so H(lambda_(alpha,s)) = H(mu_+). Splitting the logarithm gives I_s = H(lambda_s) - H(mu_+). HOLDS. The coin example: flip B_c with probability 1/2 at scale 1 and again at scale 2. Then I_2 = 0 and I_1 > 0 when the two laws differ, so the increment can be negative. HOLDS. With a fresh independent label beta_s and a map depending only on it, H(U_s | beta_s) = H(U_(s-1)), so H(lambda_s) - H(lambda_(s-1)) = I(beta_s; U_s). HOLDS.

Verdict for item 9: HOLDS AFTER CORRECTION (precision): the omitted branch h_e > 0, k_e = 0 of (S28). No conclusion changes.

## 10. Section 8 and scope

**Section 5 scope (577-590).** The proved class is exactly item 2: one colour per map, fixed exterior W after the common substitution, finite input range, arbitrary exterior dependence, any mixture of colours, flat sheets and closed-cochain choices. The OPEN list (two colour layers, connected blocks, field-dependent centre cochains, unbounded radius) is outside the proofs. "The theorem does not prove that every finite-range transport fails" is correct. HOLDS. "Not a consequence of (SD)": the class allows order-one moves at every updated link and at the seam, and the proof uses no displacement bound. HOLDS.

**Section 8, (LC) and the binding tests.** Reused from row 791, item 4b. HOLDS.

**Section 8, the extension to U(1) and the binary icosahedral group (lines 733-738).** The geometry (S6), Lemma 1 (centre signs +-1), the pushforward step and the Pinsker step carry over. In the finite group the ball becomes {+-I} for small delta, with Haar mass 1/120 > 0. Two inputs are used but not stated. (i) F >= 0 for those groups, that is Z_(eta_0) <= Z_+. For U(1) it holds term by term: the character coefficients I_n(beta) are positive and each link integral is an indicator, so each term changes only by a sign. For the binary icosahedral group the standard route is the centre-sector decomposition Z^m = sum_e chi(e, m) Z_e with |chi| = 1 and Z_e >= 0 (a transfer-matrix trace with a sector projection, by reflection positivity of the Wilson action). I did not re-derive that route here; the note must supply or cite it. (ii) The analogue of (T5), used in the mu = 2, 4 branch. (T4) carries over: the unselected plaquettes have conditional Haar mean zero, since the defining representation is a nontrivial irreducible; four independent Haar factors give a Haar holonomy; strict Jensen gives c_0 > 1. Corollary 5's angle density is SU(2)-specific, but Section 8 does not claim it. Verdict: HOLDS AFTER CORRECTION (state inputs (i) and (ii)).

**Checkpoint (54-62), N1-N8 and the RESULT line (847).** They state the Corollary 4 class, with fixed R, 4 | a, and the cost c_R a^2 - log(32 a^2). This matches what is proved. Nothing is stated beyond the class. The OPEN items (overlapping colours, blocks, unrestricted (TR-F), (26), order-one (FQ)) are not claimed. The labels "PROVED by hand, not independently checked" were true when written. MATCHES.

**Row number.** The note says FINISH row 796; this check is filed as row 798 at the lead's request. Bookkeeping only.

Verdict for item 10: MATCHES, with the Section 8 precision above.

## Verdict table

| # | Statement (lines) | Verdict | Finding |
|---|---|---|---|
| 1a | (S2) (85-110) | HOLDS | (E22)-(E23) at m = 0 |
| 1b | (S4) seam cochain (112-123) | HOLDS | Explicit unit-shift cochain; Sigma_0 is closed |
| 1c | (S5), three identities, reduction (124-142) | HOLDS | I_pi invariant under one common bijection |
| 2 | Class (S6)-(S7), seam-first form, exclusions (144-189) | HOLDS | At most one A-link per plaquette; 32 colours |
| 3a | (S8) product conditional law (193-209) | HOLDS | |
| 3b | (S9) exact action difference (210-222) | HOLDS | Each P_A plaquette in one staple sum; signs correct |
| 3c | (S10)-(S11) (224-247) | HOLDS | Conditional label weights stay pi_j (used in Lemma 2) |
| 4 | Lemma 1, (S12)-(S13) (251-286) | HOLDS | Periodic iff 4 \| a; opposite neighbour signs; H_f = 0; one sheet plaquette per sheet link |
| 5a | (S14)-(S16) (288-343) | HOLDS | Telescoping 18 delta_R; theta_R bound |
| 5b | Pushforward through the finite-input Haar map (345-351) | HOLDS | Marginal map G_* Haar^Q = Haar follows from Haar preservation of the fibre map |
| 5c | (S17)-(S18), Pinsker (352-381) | HOLDS | Mean gap m_*/2, D >= m_*^2/8 |
| 5d | p_R (383-391) | HOLDS | Oscillation 216 beta_+ M_R; Haar mass v_R^(18 M_R) |
| 6 | Theorem 3, count a^2/4, (S20)-(S23) (395-465) | HOLDS | |
| 7 | Corollary 4, (S25)-(S26), ceiling (467-516) | HOLDS | Closed c_j; MI chain rule; I(G;V) <= log(32 a^2) |
| 8 | Corollary 5, (S24a)-(S24d) (518-575) | HOLDS | All L_I terms nonnegative; both branches bounded |
| 9a | (S27)-(S28), shear does not raise target action (592-634) | HOLDS AFTER CORRECTION (precision) | Branch h_e > 0, k_e = 0 omitted; it is (S28) at s = 0 |
| 9b | (S29)-(S31), information convention (646-714) | HOLDS | |
| 10a | Section 5 scope, checkpoint, N1-N8, RESULT line | MATCHES | Claims stay inside the class of Section 2 |
| 10b | Section 8 extension to U(1) and binary icosahedral (733-740) | HOLDS AFTER CORRECTION | Needs F >= 0 for those groups (U(1) term by term; finite group via centre sectors, not re-derived here) and the (T5) analogue (carries over) |
| - | Section 6 GUIDE paragraph; Section 9 search record | NOT CHECKED | Outside the brief |

Checked line by line by Claude Opus 5.5. Nothing FAILS. Two corrections, neither changes the SU(2) conclusions: the omitted branch of (S28), and the unstated inputs of the Section 8 extension to other groups. The key step of Lemma 2 is correct: the law of one output link depends only on the law of the inputs it reads, so Haar preservation of the whole fibre map forces the one-link marginal map to push Haar^Q to Haar. Credit Codex gpt-6-astra max for the central cancellation configuration (S13), the finite-input pushforward bound and the conditional entropy sum (S22).

RESULT: Every item of gap-seam-astra.md in the brief HOLDS under a hand check by Claude Opus 5.5 — (S2)-(S11), Lemmas 1-2 (including the finite-input Haar pushforward), Theorem 3, Corollaries 4-5, (S27)-(S31) and the scope match what is proved, with two corrections that leave the SU(2) result unchanged (the omitted h_e > 0, k_e = 0 branch of (S28), and the unstated F >= 0 and (T5) inputs for the U(1) and binary icosahedral extension in Section 8); nothing FAILS.
