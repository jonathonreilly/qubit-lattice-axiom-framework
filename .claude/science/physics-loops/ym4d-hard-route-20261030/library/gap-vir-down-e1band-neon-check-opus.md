# Check of row 1638 (gap-vir-down-e1band-neon.md) -- FINISH.md row 1640

Checker: Claude Opus 5.5 (laptop subagent, row 1640). Checked by hand, line by line. Status: complete.

## 0. Reading log

- FINISH.md row 1638 (brief and RESULT), read in full.
- `library/gap-vir-down-e1band-neon.md` (row 1638, 453 lines), read in full.
- Check 1630 (`library/gap-vir-down-twoside-check-opus.md`) sections 1 and 3 (3.1-3.3), read in full.
- Check 1634 (`library/gap-vir-down-e12-check-opus.md`) and check 1635 (`library/gap-vir-down-e2-neon-check-opus.md`), read in full.
- Row 1628 (`library/gap-vir-down-twoside-astra62.md`), read in full.
- Registry row VIR-DOWN (`library/open-registry.md` L1028).
- Duplicate checks (grep of `library/`, `FINISH.md`, excluding every `gap-vir-down-e1band*` file): row 710 (`gap-vir-sc.md`) Theorem U L64-79 and Section 8 item 4 L200; row 1619 (`gap-vir-down-fable.md`) Sections 3.0-3.3 L118-149 and L170-178; row 1618 (`gap-vir-down-neon.md`) L160-183; row 1626 (`gap-vir-down-dom-astra62.md`) L148-156; row 1171 (`gap-solve14-astra62.md`) L17, L34; row 1632 (`gap-vir-down-e2-astra62.md`) (11) L148, L200; row 1553 (`gap-mech-direction4-fable.md`) L190-194.
- Not read: `library/gap-vir-down-e1band-check-opus.md`, and rows 1636, 1637 (`gap-vir-down-e1band-astra62.md`, `gap-vir-down-e1band-obstruct*`). My check is independent of them.
- Guide run: see section 6 (floating point, not a proof step).

## 1. Theorem 1(1)-(2): the split, the Hankel formula, the identity, the Bessel bound

**(1.1)-(1.3), the split b_r = beta^-1 a_r^aniso + 2 b_r^(M). HOLDS.** Redone by hand.
- T(beta_t, beta_s) = M_(beta_s) C_(beta_t) M_(beta_s). M' = -(V/2) M and M commutes with V, so d_(beta_s) T = -(VT + TV)/2.
- On ran F~_r, T F~_r = lambda F~_r. So lambda_0^-1 F~(-(VT+TV)/2)F~ = -r F~ V F~. First-order perturbation of the simple top level gives d_(beta_s) log lambda_0 = -<V>_Omega. Hence b^(M) = F~(<V>_Omega - V)F~. Correct.
- d/dbeta = d_t + d_s on the diagonal, and d/dxi of (xi beta, beta/xi) at xi = 1 is beta(d_t - d_s). So a = beta(b^E - b^M), and b = a/beta + 2 b^M = -a/beta + 2 b^E. Correct.
- Absolute convergence: ||b^(M)|| <= 2|P| and G(t) < infinity. Correct.
- Standing: ON FILE in substance. Row 710 Theorem U (ii) gives the electric and the magnetic partial derivatives of every level. Row 710 Section 8 item 4 (L200) names exactly this route: "the candidate is the response to an anisotropy ... E is a combination of them whose two coefficients are the derivatives of the couplings with respect to the anisotropy" (Karsch coefficients, the energy sum rule), with the verdict "I see no reduction in strength". Row 1619 Sections 3.0, 3.1 and 3.3 (L118-149) repeat it. New here: the operator a_r^aniso on each eigenspace and the formula (1.2) as stated. The file's novelty grep (L26, "zero prior hits") is wrong for this item.

**(1.4)-(1.5), the delay-Hankel formula for N_M. HOLDS.** P^(t/2) is Hilbert-Schmidt for t > 0; K_t = P^(t/2) X P^(t/2) with X = <V>_Omega - V bounded is trace class. JQ = sum of J_r commutes with P, so Tr(JQ K_t) = sum r^t Tr(J_r b_r^(M)). The finite closures J_(L,Q) increase strongly to JQ (row 1628 (17), polynomial argument), and J_(L,Q) K_t -> JQ K_t in trace norm. The block form and the stationary-chain form at t = 2v are correct. Row 1628 uses P^(1+a-theta); the file uses P^(1+a); both have the same closure. Standing: row 1628 (16)-(17) applied to the multiplication operator X. New as written, immediate. "Bessel-free" is cosmetic: P carries the Bessel multipliers. It is a representation of N_M, not a bound on it.

**(1.6)-(1.7), the cumulant-entropy-Bessel identity. HOLDS.** Redone: w(k) = c_k q(k)/lambda; log(w/q^) = log(||M psi||^2/lambda) - eta(k); -log lambda = -log<e^(-beta V)>_psi + E_w eta + D_KL(w||q^); subtract at Omega; beta B_E = Delta E_w eta + Delta E_w delta (the constants g(0), eta_0 cancel because w is a probability for psi and for Omega). Then a = m + Delta Lambda - Delta D_KL + Delta E_w delta. Correct.
Standing: ON FILE in substance. Row 710 Theorem U (iii) is -log lambda = <eta>_w + sum w log(w/q) with the unnormalized q; and sum w log(w/q) = D_KL(w||q^) - log<e^(-beta V)>_psi. So Lambda and q^ only rename row 710's entropy term. Row 1619 Section 3.0 has m_i = Delta<eta>_w + Delta D. New: the anisotropic combination (1.6).

**(1.8), 0 < beta d log(I_(nu+1)/I_nu)/d beta < 1. HOLDS.** r_nu = E_(mu_nu)[x]; r_nu' = Var > 0; conditioning on |x| = y gives f(y) = y tanh(beta y) increasing and g(y) = 1 - y^2 decreasing, so Cov < 0 and r_(nu+1) < r_nu; then beta d log r_nu/d beta = 1 + beta(r_(nu+1) - r_nu). Each line checks. The consequences 0 < g(k) - g(0) < k/beta and delta(k) < k check (eta_k - eta_0 = -log(I_(k+1)/I_1) > 0).
Standing: r_(nu+1) < r_nu is the classical Turan inequality for I_nu, ON FILE as "the Bessel Turan log-concavity recorded in row 996" (`gap-solve40-astra62.md` L236, same mean-of-x proof). The lower bound is ON FILE (row 1617 (12), row 843). The sharpening of row 1631 (8) from q/beta + 1 to q/beta drops a term that check 1634 already noted lies in (0, 1). Small.

## 2. Theorem 1(3)-(4): the dichotomy, the Gaussian signs, the strong-coupling sign

**Theorem 1(3), the dichotomy (M-vis) / (A-vis). HOLDS (elementary).** From (1.3): if N >= (kappa_0+eps)W_t, A <= C W_t and beta >= C/eps, then A/beta <= eps W_t and 2N_M >= kappa_0 W_t. The two-sided version for N_E checks. The spin-cut line uses row 1631 (4) (checked in 1634) summed over a basis of J_r: |N_M - N_M^[q]| <= (8(6+2 delta)/q) W_obs. Correct.
What it is. It says: if a sum of two terms is large, one of them is large. Conversely, (M-vis) at rate (kappa_0+eps)/2 + C/(2 beta) with |A| <= C W_t gives (E1). So on the bounded-anisotropy branch (M-vis) is (E1) up to a rate shift O(C/beta): equivalent, not progress. GUIDE (sum rules; the free photon (1.9) has 0 < a < m): a^aniso is about m at weak coupling, so A/beta = O(W_t/beta) and the (A-vis) branch is not expected late; on the band (E1) should sit in (M-vis). That is row 1619 Section 3.0, last bullet ("the magnetic and entropy parts of a level must lie below the vacuum's by a multiple of the level's energy that grows with the cutoff"), and row 710 Section 8 item 3. ON FILE in substance.

**Theorem 1(4)(i), free photon. HOLDS.** Redone. Kernel exp(-beta[cosh omega (q^2+q'^2)/2 - q q']) with 2 sinh(omega/2) = omega_0; Mehler gives Omega ~ exp(-beta sinh omega q^2/2); omega_0^2/(4 sinh omega) = tanh(omega/2)/2; a^2, (a^+)^2 shift energy by -/+ 2 omega, so their compression to any eigenspace is 0. So b^(M) = -(1/beta) sum n tanh(omega/2). With b = 0 (row 1628 (22)), a = 2 sum n tanh(omega/2) < m. Second derivation (mine, different route): rescale q -> q/sqrt(beta xi); the anisotropic photon is the isotropic one with omega_0 -> omega_0/xi; d omega/d xi = -2 tanh(omega/2) at xi = 1. Same a.

**Theorem 1(4)(i), compact Gaussian U(1) with P_0. HOLDS, in the zero-monopole zero-flux law of row 1618 Section 2.1 / row 1628 (22).** The flux rotor sits in C_(beta_t) only, so b^(M) is the photon value tensor I; b = e_Q/beta gives a = e_Q + 2 sum n tanh. (1.9): W_obs <= W_(t,Q=0) (flat shift, row 1626 (12)-(13)); the ratio bound uses row 1618 Theorem 2(2), E_phot/E_flux <= 280 beta e^(-2.5 beta) (`gap-vir-down-neon.md` L183, located, not re-proved). Correct.

**Theorem 1(4)(ii), strong coupling. HOLDS at fixed n as beta -> 0 (all O-constants depend on n), with one correction.** Redone by hand:
- Spin grading on H_0: every non-constant label has sum |k| >= 4; sum = 4 is an elementary plaquette (non-contractible 4-cycles at n = 4 have odd winding, removed by P_0); sum = 5 is excluded by parity or P_0. Correct. F_4 = span{chi_p} (SU(2)), span{c_p, s_p} (U(1)).
- (I1) F_4 S F_4 = 0: |dp triangle dq| is in {0, 6, 8}, never 4. Correct. (I2): an odd-multiplicity plaquette keeps an edge of odd multiplicity; four distinct plaquettes would need 8 shared edges from at most 6 pairs; so only pairings; distinct plaquettes are pairwise independent Haar. Correct.
- (1.12)-(1.15): Weyl, the projected eigen-equation, |<u, phi>| = O(beta^5), K K* = F_4 + O(beta^2) by (I1), the cluster in a(1 + O(beta^2)), (I - F_4)psi = O(beta), F_4 e^(beta S/2) psi = psi_0 + O(beta^2), and (1.14). Each step checks.
- SU(2): 4||S psi_0||^2 = d_sp - 1 + 2|sum alpha|^2 (int chi^4 = 2). So B_M = -beta/4 + O(beta^2). U(1): int c^4 = 3/2, int c^2 s^2 = 1/2, so B_M = -beta(3/4 sum alpha^2 + 1/4 sum gamma^2) + O(beta^2). I recomputed both pairing sums. Check by a one-plaquette hand expansion: psi = chi + (beta/4) chi_1 - beta/4 gives <S>_psi = O(beta^2), <S>_Omega = beta/4. Agrees.
- N_M < 0 for small beta when t >= 4: P_4 part <= -(beta/5) r_min^t Tr(J P_4) = -Theta(beta^(4t+1)); rest O(beta^(6t-6)); 6t - 6 > 4t + 1 iff t > 7/2. Correct.
- **Correction (L194, also L328 of Thm 3(1b)).** "T^ = M C^ M <= C^" is not an operator inequality. What holds and is enough: lambda_j(M C^ M) = s_j(C^(1/2) M)^2 <= ||M||^2 lambda_j(C^) by the singular-value inequality, with ||M|| <= 1. The conclusions stand.
- Guide (section 6): two U(1) plaquettes sharing one link, Fourier basis, beta = 0.02: B_M/beta on the 4-dim lowest cluster = {-0.7499, -0.7498, -0.2500, -0.2499}. Agrees with (1.11).

Standing: new as a stated sign at fixed n. Inputs ON FILE: the strong-coupling plaquette band (rows 683, 701; row 1611 degree-four join coefficient, check 1627 L12); row 710 (BAND-sc) L181-184 asks for the same band uniformly in the cube, which this does not give. The sign holds identically in 4D SU(2), 5D SU(2) and 4D U(1): it reads only (I1)-(I2), which hold for any compact group with a centre element acting as -1 and any dimension. Not selective.

**"(M-vis) reverses sign inside 4D SU(2) by the law and the scale, not the algebra or the centre". FAILS as PROVED.** First failing line, L379: "Thus `(M-vis)` changes sign as $\beta$ varies inside 4D $SU(2)$: it reads **`P-law`** and **`P-scale`**". Only one end is proved: N_M < 0 at fixed n for beta < eps_n, with eps_n -> 0 as n grows. The other end, N_M > 0 on the band, is (E1) itself via Theorem 1(3); it is open. So the true statement is conditional: *if* (E1) holds on the band with |A| <= C W_t, *then* N_M has opposite signs at beta < eps_n and on the band. Even this is not a selective step: the proved end is the same in 5D SU(2) and 4D U(1), and the band end is the target. The dichotomy also does not apply at strong coupling (it needs beta >= C/eps), and there (E1) itself holds (Theorem 3(1c)) through the anisotropic branch. So strong coupling gives no failure of (M-vis) as a criterion for (E1).
Answer to question 3: it is a strong-coupling statement at fixed box and beta -> 0 (beta < eps_n, eps_n -> 0 as n -> infinity, while beta_K grows like log n on the window). It never reaches the band and reads no property of the law at the band. It is GUESSED/ARGUED (sum rules: B_M about kappa m/2 > 0 for SU(2) glueballs, GUIDE) that the sign flips; that is the open estimate.

## 3. Theorem 2: the loop-algebra no-go and incomparability (decides the route)

**Theorem 2(1). HOLDS.** Redone by hand.
- P_hid = r_M I + (1 - r_M) Pi on M+1 uniform states: positive entries, eigenvalues 1 and r_M (M-fold). G_hid = M r_M^t = delta; W_hid = (delta/t) log(M/delta).
- (a) ran E = ran E_1 tensor 1, and P_hid 1 = 1, so every correlation of ran E, with any powers and any coupling-derivative marks, is that of (P_1, E_1) (P_hid does not depend on beta). (2.6), (2.7) and J^prod = J^(1) tensor Pi check. On F_s^(1) tensor (I - Pi), b = (s r_M)^-1 F_s P_1' F_s tensor r_M (I - Pi) = b_s^(1) tensor (I - Pi); at s = 1 this is 0. So N, W_obs, c_o are unchanged: (2.1).
- (b) (1 + G_1)(1 + delta) = 1 + c_col. (2.2) checks (the two hidden blocks are b-invariant; M r_M^t = delta).
- (c) W^prod = (1 + delta) W^(1) + (1 + G_1)(delta/t) log(M/delta) -> infinity. Correct.

Question 2(i): every family, or a special family? Both, in different slots. The base is arbitrary: any (P_1, E_1) at a strictly cold point, so every flowed-loop family that row 1628 allows, and actual Wilson SU(2) with row 1624's loops. The counterexample is always one special family: the base tensored with a coupling-independent (M+1)-state spectator. So the theorem says: for every base there is a law with the same loop data (all delays, all marks), coldness exactly c_col and H_0/W_t -> 0, in which (E1) fails. That is a statement about inference from loop data, not about the base law.

Question 2(ii): does (E1) fail for actual Wilson SU(2)? No. The SU(2) factor's own N^(1), W^(1) are untouched; only the product's W_t grows. The product is the (g4) member of Lemma ALG (row 1553 L191), not a Wilson law. The file's wording "keeping cold 4D SU(2) ... intact while killing (E1)" should read "keeping the SU(2) factor, its loop data, coldness and (E2) intact, while (E1) fails for the product". What it shows: (E1) does not follow from loop data + coldness + (E2); a proof needs a Wilson-specific bound on the invisible thermal fraction h. 
Standing: ON FILE in substance. The spectator test: row 1553 (g4), row 1617 L235, row 1628 spectator paragraph (L256), check 1634 "Spectator. HOLDS", check 1635 section 9 (iii) ("(E1) fails once the spectator is light"). Same loop data at all delays with opposite verdicts: row 1628 families A and B (L227: "all delay readings and their Gram matrices agree"), row 1629 Corollary 2.2(3), check 1635 Theorem 1.2(1). The forced bound on h: check 1635 Q1 ((E1) forces h <= 1 - (kappa_0+eps)/c_o) and check 1630 3.2. New: the exact coldness value c_col, formula (2.2) and the rate (2.3). Small content.

**Theorem 2(2)(a). HOLDS.** Redone: t m_1 = a_1 e^(-x/3) in [3, a_1]; t m_hid = log(25M); G_1 < e^-3 < 1/20; G_hid = 1/25; G < (21/20)(26/25) - 1 = 23/250 < 4/21 (483 < 1000); P_K > (250/273)^2 = 62500/74529 > 457/625 (39,062,500 > 34,059,753, integer products redone). Slopes 3m_1, (8/3)m_hid, 3m_1 + (8/3)m_hid, all >= (8/3)m, so R > 8/3 and H_0 = 0. N = 3 m_1 e^(-t m_1) <= 3/(e t); W >= log(25M)/(25 t); ratio <= 75/(e log(25M)). Correct.

**Theorem 2(2)(b). HOLDS.** f_1, f_2, f_3 orthonormal in L^2(uniform); ran E = span{1, f_1}; at beta_0 one 3-dim eigenspace with J = span f_1, D = span{f_2, f_3}; b = diag(5m, -10m, -10m); G(8) = 3e^-4 < 4/21; N = (5/3) W_8; R = -5. Correct.

Question 2(iii): what "strictly incomparable" means here. Exactly this: in the class of finite smooth positive self-adjoint Markov transfer families with a finite observation (not Wilson laws), (a) there is a family in which (VIR-down) at rate 8/3, (HOT), (PUR-io) and H_0 = 0 hold on the whole calibrated-shape window while (E1) fails at every point for the given kappa_0; and (b) there is a family and one point (t = 8, beta_0) at which (E1) holds (N = (5/3) W_8) while R = -5 < 0. So neither statement implies the other in that class. Restricted to Wilson SU(2) nothing is decided (the file's L229 scope note says so). Content: (b) says (E1) ignores hidden levels, which is why check 1630 3.3 pairs it with (E2) (row 1628 (20); check 1635 six-state family Theorem 1.2(3) is the same mechanism). (a) says (E1) gives no credit to hidden rising levels (check 1635 (C2): "strictly stronger than (VIR-down) (it discards hidden credit)"; row 1628 mode interchange L258). New: the two explicit families. It does not show (E1) is non-equivalent for Wilson: check 1635 section 8 proves that if D = 0 then (E1) is (VIR-down) with a margin, and row 1633 argues D = 0 is generic for row 1624's partition (unchecked).

**Route verdict from Theorem 2.** Theorem 2 does not refute (E1) for Wilson SU(2). It confirms, with a cleaner family, what is on file: no argument from loop correlations, coldness and (E2) can reach (E1); it needs a Wilson-specific global statement that almost no cold thermal energy is loop-invisible (h small), plus an order-one observed rate c_o. Both are statements about the Wilson spectrum on the band at order-one coupling.

## 4. Theorem 3

**3(1)(a), U(1) flat-shift charges at every beta. HOLDS.** Summing div k = 0 over a slice x_j = c gives F_j(c) = F_j(c-1) = Q_j; S_alpha acts by e^(i n Q.alpha); the hyperplane centre flip acts by (-1)^(Q_j), so P_0 gives Q in (2Z)^3; sum |k_e| >= n||Q||_1 >= 2n for Q != 0; Omega in H_(Q=0) by uniqueness; ran E in H_(Q=0) for flat-shift-invariant E. Each step checks. Standing: flat-shift invariance of contractible loops for U(1) is ON FILE (row 1171 L34; row 1626 (12)-(13), check 1627 1.8, there in Gaussian coordinates). The exact charge sectors for interacting Wilson U(1) with the bound sum |k| >= n||Q||_1 are new as stated, elementary.

**3(1)(b), (3.1). HOLDS AFTER CORRECTION.** Correction: "T^ <= C^ on H_(Q != 0)" (L328) is not an operator inequality; use the singular-value domination of section 2. Then: lambda^_0 >= e^(-2 beta d) >= e^(-1/8); off-constant multipliers on Q != 0 are <= (beta/2)^(2n); Tr C^ <= e^(beta d) <= e^(1/16); the C-odd trial vector sqrt2 sin theta_p gives r_1^(Q=0) >= e^(-1/4)(beta/2)^4 and m_1 > 1. The exponent (2n-4)t - 3n, the value 4 at n = t = 4, e^(13/8) < 8, 8 * 6144^-4 < 10^-14, and monotonicity in n, t all check. Scope: beta <= 1/(48 n^3). No content on the band.

**3(1)(c), "(g3) pass". HOLDS AFTER CORRECTION.**
- J_r = F_r on P_4: overlaps <u_p, c_q> = (2 sqrt2/pi) delta_pq, <u_p, s_q> = 0, etc.; the sum of squares is 8/pi^2; ||psi - psi_0||, ||Omega - 1|| = O_n(beta); so ran P_4 meets ker E~_el only in 0. Correct (J_r = F_r iff ran F_r meets ker E only in 0).
- b_psi = 4/beta + O_n(beta), m = 4 log(2/beta) + O(beta^2). Correct. The Q_(>=6) tail display at L347 does not follow as written (the factor (5/3)^d and the geometric sum are not justified). The conclusion O_n(beta^2) holds by a simpler line: sum over K >= 6 of w(k) K <= (max_(K>=6) K c^_k) (sum_k q(k)) / lambda~ <= 6 (beta/2)^6 e^(beta d)/lambda~ = O_n(beta^2), since lambda~ is of order beta^4.
- (3.2) uses row 1632 (11) (b_r >= 1/(2 beta) on every level, checked in 1634 for U(1)) and W_(>=6)/W_(P_4) = O(beta^(2t - 15/2)). Correct for t >= 4. The SU(2) variant (8/(3 pi) > 4/5, log(4/beta)) checks.
- Correction to the claim. This is a fixed-n, beta -> 0 statement for an n-dependent elementary-plaquette partition C_el. It is not row 1624's flowed partition, not uniform in n, and not at a fixed coupling as n -> infinity, which is how (g3) is posed for a seed argument (row 1553 L190). So it settles check 1630 3.1's ARGUED line only for C_el at beta < eps_n. Its own SU(2) variant shows the same pass in 4D and 5D SU(2): it is the strong-coupling "every level falls" (row 1632 (11), row 1610 L141) plus visibility of the plaquette band. It separates nothing between 4D SU(2) and the comparison models.

**3(2), SU(2) no-flat-shift. HOLDS.** Both substitutions check (U_2 = h gives a trivial commutator; U_1 = h^-1, U_2 = h gives g_j central); the -I shift is a product of centre flips, trivial on H_0. Standing: ON FILE in substance, row 1171 L17 and L34 (contractible SU(2) traces fix the connection up to gauge and the eight centre flips; U(1) flat shifts survive). The Lemma ALG caveat in the file is right.

**3(3)(a)-(c). HOLD.** (a) translation-invariant E sees only p = 0; at fixed n, beta -> 0, 3 of 3n^3 cluster states. (b) The centre argument forces R = I, a = 0 (2 m_0 = n/16 is not 0 mod n); the separating configuration works even when g S_1 is not a grid square; the O_h orbit of a generic momentum has 48 elements, so rank F_r >= 48. (c) rank(J_L Q) <= (L+1) d_E and Ky Fan. Scope: (3.3) and (3.4) concern observations that are translation invariant or of rank < 48; row 1624's partition is neither. (3.6) holds at fixed L with d_E independent of K, but d_E for row 1624's joint bins is astronomically large, and (E1) uses the infinite-delay closure J, about which (3.5)-(3.6) say nothing. New, elementary, no consequence for (E1).

## 5. Section 4 of the file: selectivity claims and labels

- "Candidate selective property isolated (PROVED necessary ...)" (L373): (M-vis) is necessary for (E1) only on the bounded-anisotropy branch at beta >= C/eps, and there it is equivalent to (E1) up to O(C/beta) (section 2). It is the target, rewritten. ON FILE in substance (row 1619 3.0; row 710 Section 8 items 3-4).
- "genuinely selective is the separation proved in Theorem 3(1) + (1.9)" (L397): **FAILS.** That separation is between strong-coupling U(1) at fixed n (passes) and weak compact Gaussian U(1) (fails). It separates two couplings of abelian laws. The same strong-coupling pass holds for 4D and 5D SU(2) (Theorem 3(1c), last paragraph). It is not a property of 4D SU(2) that 4D U(1) or 5D SU(2) lacks, so it is not selective in the sense of row 1386 or Lemma ALG.
- Table row "Weak 4D Wilson U(1) (g1) ... FAILS (conditional on row 1573 ...)": the failure of (E1) for weak interacting Wilson U(1) is ARGUED, not proved (N_M < 0 there is ARGUED). The cell should say ARGUED.
- Novelty grep (L26, "Zero prior hits on file"): false. The anisotropy route and the electric/magnetic split are row 710 Theorem U and Section 8 item 4 and row 1619 Section 3; Bessel Turan log-concavity is row 996 (`gap-solve40-astra62.md` L236); the spectator and all-delay data no-go are rows 1553, 1628, 1629, check 1635; SU(2) has no flat shift is row 1171.
- Section 4.2 attacks 1-5: I agree they stop where stated; each stop is at the band sign.

## 6. Guide run (floating point; not a proof step)

One Python process, a few MB, `g1640/guide.py` in this session's scratchpad, outside the repository. Model: two U(1) plaquettes sharing one link (7 links; gauge-invariant functions of the two independent plaquette angles), Fourier truncation |n_i| <= 10, T = M C M with the exact Bessel multipliers, shared link carrying n_1 - n_2. This is a different data path from the author's one-plaquette script: it tests (I1)-(I2) with a shared link. B_M/beta on the 4-dim lowest excited cluster: beta = 0.02: {-0.7499, -0.7498, -0.2500, -0.2499}; beta = 0.1: {-0.7487, -0.7462, -0.2495, -0.2470}; beta = 1: {-0.683, -0.588, -0.243, -0.133}; beta = 3: {-0.201, -0.181, -0.090, -0.079}. Agrees with (1.11) as beta -> 0, and stays negative at beta = 3 in this toy (no scaling region; says nothing on the band).

## 7. Question 4: new and on file

| Claim (row 1638) | Verdict | Standing |
|---|---|---|
| Thm 1(1) (1.1)-(1.3) split | HOLDS | ON FILE in substance: row 710 Thm U (ii), Section 8 item 4 (anisotropy route, "no reduction in strength"); row 1619 3.0-3.3. New: operator a_r^aniso, formula (1.2) |
| Thm 1(1) (1.4)-(1.5) Hankel | HOLDS | Row 1628 (16)-(17) applied to V; new as written, immediate; a representation, not a bound |
| Thm 1(2) (1.6)-(1.7) | HOLDS | Row 710 Thm U (iii) renamed (Lambda, q^); row 1619 3.0. New: the anisotropic combination |
| Thm 1(2) (1.8) | HOLDS | Turan log-concavity ON FILE (row 996, `gap-solve40-astra62.md` L236); lower bound row 1617 (12); upper bound classical, small |
| Thm 1(3) dichotomy | HOLDS (elementary) | Equivalent to (E1) on the bounded-A branch; ON FILE in substance (row 1619 3.0 last bullet) |
| Thm 1(4) Gaussian signs, (1.9) | HOLDS | New explicit forms; inputs ON FILE (rows 1618 Thm 2(2), 1626 (12)-(13), 1628 (22)) |
| Thm 1(4) strong-coupling B_M | HOLDS at fixed n, beta -> 0 (correction: singular-value domination, not "T^ <= C^") | New; non-selective (same in 4D/5D SU(2), 4D U(1)) |
| "(M-vis) reverses sign inside 4D SU(2)" | FAILS as PROVED (L379); true only conditional on (E1) | The band end is the open target |
| Thm 2(1) no-go | HOLDS | ON FILE in substance: (g4) (rows 1553, 1617, 1628; checks 1634, 1635), all-delay data no-go (row 1628 A/B, row 1629 Cor 2.2(3), check 1635 Thm 1.2(1)), forced h bound (check 1635 Q1). New: exact c_col, (2.2), (2.3) |
| Thm 2(2) incomparability | HOLDS (abstract positive families only) | New explicit families of ON FILE mechanisms (row 1628 (20), mode interchange; check 1635 (C2), Thm 1.2(3)) |
| Thm 3(1a) | HOLDS | Flat shift ON FILE (rows 1171, 1626); exact Wilson charge sectors new, elementary |
| Thm 3(1b) (3.1) | HOLDS AFTER CORRECTION (operator inequality) | New; beta <= 1/(48 n^3) only |
| Thm 3(1c) "(g3) pass" | HOLDS AFTER CORRECTION (fixed n, beta < eps_n, C_el only; L347 display repaired) | New; shared by 4D/5D SU(2); not selective |
| Thm 3(2) no-flat-shift | HOLDS | ON FILE in substance (row 1171 L17, L34) |
| Thm 3(3) rank ceilings | HOLD | New, elementary; no consequence for infinite-delay (E1) |
| "Selective separation" (L397) | FAILS | Separates two couplings of U(1), not 4D SU(2) from U(1)/5D |
| Novelty claim L26 | FAILS | See section 5 |

Same-route note: my check is a reading by hand of the author's routes. The second derivations are the photon anisotropy by rescaling (section 2) and the one-plaquette hand expansion of B_M; the only other data path is the floating-point guide of section 6, which is not a proof.

What moved: nothing on the critical path. (E1) on the band, (VIR-down), (HOT), (PUR-io) and the gap stay open.

## RESULT

Thm 1(1)-(2) HOLD: split b = a^aniso/beta + 2b^(M), Hankel form of N_M, identity (1.6), and (1.8) are correct; all are ON FILE in substance
(row 710 Thm U and Sec. 8 item 4, row 1619 Sec. 3, row 996 Turan, row 1628 (16)-(17)); the file's "zero prior hits" is false.
Thm 1(3) HOLDS, elementary: with bounded anisotropy (M-vis) is (E1) up to O(1/beta), equivalent, not progress. Thm 1(4) HOLDS (photon, compact Gaussian U(1), strong coupling at fixed n; fix "T^ <= C^" to singular-value domination).
"(M-vis) reverses sign inside 4D SU(2)" FAILS as PROVED (L379): only the beta < eps_n end is proved, and it is identical in
5D SU(2) and 4D U(1); the band end is (E1) itself. It is a fixed-box strong-coupling statement that never reaches the band.
Thm 2 HOLDS: for every base law (Wilson included) a spectator product keeps all loop data, coldness and (E2) and kills (E1);
it does not show (E1) fails for Wilson SU(2), only that loop data cannot give it (ON FILE in substance: (g4), rows 1628, 1629,
check 1635). "Strictly incomparable" holds only in abstract positive transfer families; for Wilson with D = 0, (E1) is (VIR-down).
Thm 3 HOLDS (two small corrections); its "(g3) pass" is fixed-n strong coupling, shared by SU(2); the claimed selective separation FAILS.
Recommendation: stop the (E1) route. Every proved piece is non-selective; what is left is a Wilson-specific band statement (h small and
c_o of order one), i.e. the order-one wall of row 1386. Reopen only with a new (K-I)/(K-II) band input, e.g. a sign for the magnetic action excess of cold levels.
