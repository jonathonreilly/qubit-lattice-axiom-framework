# Check of row 1618 (library/gap-vir-down-neon.md), row 1622

Checker: Claude Opus 5.5 (checker for FINISH.md row 1622). Started 2026-11-27.

Status: complete for this run. Hand check by Claude Opus 5.5 of a gemini-4-neon-xhigh file (cross-provider). No Lean. One floating-point guide run from stdin, outside the repository (not a proof step). Nothing committed or pushed; no other file written.

## 0. Reading log (appended as read)

- FINISH.md rows 1618 (brief and RESULT) and 1622 (this brief): read.
- `library/gap-vir-down-neon.md` (row 1618): read in full, L1-389.
- `library/gap-direction7-fable.md` (row 1610): read in full. `library/gap-direction7-fable-check-astra62.md` (check 1613): read in full.
- `library/gap-mid-max.md` (row 708) L45-145: (VIR_K), Theorem TR, Remarks CH and LEV, Lemmas 4.1-4.2.
- Not opened: `library/gap-vir-down-astra62-check-opus.md` (as instructed).

- Cited rows read in their files: row 710 (`gap-vir-sc.md` L43-76: Lemma J, Lemma C, input (RK), Theorem U); row 1143 (`gap-solve-astra62.md` L19-100, L160-200: (1), (2), (3), (4), (11)) and check 1144 (`gap-solve-check-opus.md` verdict lines on (1), (2), (3), (11), (13)); row 1215 (`gap-solve23-astra62.md` L21-24, L44-96, L314-329: the normalization of F, (4), (5), (20)) and check 1221 (`gap-solve23-check-opus.md` L35-36, L73-75, L202, L213); row 1461 (`gap-crux-direction-astra62.md` L56-95: (1), (2), the table bounds) and checks 1462 (`gap-crux-direction-astra-check-opus.md` L42-54) and 1465 (`gap-crux-direction-astra-check2-opus.md` L37-51); check 1453 BND-1 (`sa-ym4-lean-trajectory-check-astra62.md` L18, L32, L107).

Conventions. "R" below is the thermal coupling-rate ratio of row 1618 (0.2): R = d_beta G / (-t d_t G). For integer t, d_beta G = (1+G)(t a_0 - A_t) and -t d_t G = (1+G) t Ebar_t (Remark FIELD of row 1610, checked in 1613). For real t, check 1613 (R) gives d_beta G = t sum_{i>=1} (D_i - D_0) r_i^t and -t d_t G = t sum_{i>=1} m_i r_i^t in any eigenbasis; I re-derived both from 1 + G = Tr Rhat^t.

## 1. Claim 1: Lemma 1, Theorem 1, Corollaries 1A-1C

**Lemma 1 (L44-70). HOLDS.**
- (1) Poisson integral. Standard form I_n(b) = (b/2)^n / (sqrt(pi) Gamma(n+1/2)) * int_{-1}^{1} (1-t^2)^{n-1/2} e^{bt} dt, and Gamma(n+1/2) = sqrt(pi) (2n-1)!!/2^n, give the printed prefactor b^n/(pi (2n-1)!!). The Wallis recursion W(n,k) = (2k-1)/(2(n+k)) W(n,k-1) and the closed form were redone. Correct.
- (2) Integration by parts with u = (1-t^2)^{n+1/2}, u(+-1) = 0, u' = -(2n+1) t (1-t^2)^{n-1/2}: I_{n+1} = b^n/(pi (2n-1)!!) int t (1-t^2)^{n-1/2} e^{bt}, using (2n+1)!! = (2n+1)(2n-1)!!. Then I_n - I_{n+1} has the positive integrand (1-t)(1-t^2)^{n-1/2} e^{bt}. Correct at every b > 0. Row 710 Lemma J(c) gives only r_n <= b/(2(n+1)), so this is the step that removes the restriction b <= 4 of Lemma J(e). Not new mathematics (I_{n+1} < I_n for b > 0 is classical), but correctly proved.
- (3) From c_j = e^{-b} sum_k (b/2)^{2j+2k}/(k!(2j+1+k)!) (row 710 Lemma J(d), read): the k = 0 term gives the lower bound; (2j+1+k)! >= (2j+1)! k! and sum (b^2/4)^k/(k!)^2 <= e^{b^2/4} give the upper bound. The identity -b eta_j' = 2j - b(1 - r_{2j+1}) follows from b I_n' = n I_n + b I_{n+1} (row 710 Lemma J(b), all s > 0): -b eta_j' = -1 - b + (2j+1) + b r_{2j+1}. Redone. Correct.

**Theorem 1(1) (L75-93). HOLDS.**
- Row 710 Theorem U is stated for 0 < s < 4, but its proofs (i)-(iii) (L74-76, read) use only Lemma C, M' = -(V_1/2) M and the log-sum inequality; none uses s < 4. In H_0 one needs Pi_j and M_beta to commute with the centre flips: a flip multiplies some links by -1, which acts on H_j by (-1)^{2j}, so H_j is invariant; M is a function of plaquettes, which flips preserve. So the transfer to H_0 is valid.
- beta D = <N>_w - beta <R>_w - beta <psi, V_1 psi>: redone from R' = P_0(M'CM + MC'M + MCM')P_0 and MCM psi = lambda psi (MCM commutes with P_0). Bounds: 0 < R(j) < 3|B| by Lemma 1(2), 0 <= V_1 <= 6|B| (3|B| spatial plaquettes, each in [0,2]). So -9|B| <= D <= <N>_w/beta. Correct.
- Energy bound: eta_j >= 2j log(2j/(e b/2)) + b - b^2/4 from Lemma 1(3) and (2j)! >= (2j/e)^{2j}; Jensen for x log x over the m = 3|B| links and then over w. Redone. Correct.
- Vacuum bounds: lambda_0 <= 1 uses ||M|| <= 1 and ||C|| = sup_j prod c_{j_l} = c_0^m (c_j decreasing in j by Lemma 1(2)) with c_0 = Haar mean of e^{-b(1-x)} <= 1. lambda_0 >= <1, MCM 1> >= e^{-6b|B|} c_0^m >= e^{-9b|B|} uses that C preserves positivity and M1 >= e^{-3b|B|}. a_0 = -D_0 in [0, 9|B|]. Correct.

**Theorem 1(2) (L79-80, L95-103). HOLDS.**
- dim H_0 = infinity: chi_j(U_{p0}) are gauge invariant, flip invariant, and orthonormal because U -> U_{p0} pushes Haar to Haar (one edge of p0 occurs once). Correct. R compact, positive, injective on H_0 (check 1613 (R) item 1) gives m_i -> infinity.
- The bound alpha X_i <= m_i + 9b|B| + (3/4)|B| b^2 and the final display were redone term by term, including the constant 3e|B|e^alpha/2 = C e^alpha/b with C = e m b/2. Then 0 <= liminf <= limsup <= 1/(alpha b) and alpha -> infinity. Correct, uniformly in the eigenbasis since every bound is per unit eigenvector.

**Theorem 1(3) (L81-82, L105-115). HOLDS.**
- (1.1): R|_{H_0} = M C_0 M with C_0 = P_0 C P_0, and its nonzero spectrum equals that of C_0^{1/2} M^2 C_0^{1/2}, with e^{-6b|B|} <= M^2 <= 1. Min-max gives (1.1). Correct.
- The two one-link comparisons follow from Lemma 1(3) at b_1 and b_2. The epsilon argument: for N(j) >= N_0, N log(b_2/b_1) <= eps N log(N/(e m b_2/2)) <= eps(eta(j;b_2) - m(b_2 - b_2^2/4)). Redone; K_1 as printed. The finite set N < N_0 is absorbed into c~(eps) since c_j(b_2) <= 1. The operator inequalities hold because all C_b are diagonal in the same Pi_j decomposition, and t -> t^{1+eps} is increasing. The two-sided bound m_i(b_2) - C_2 <= m_i(b_1) <= (1+eps) m_i(b_2) + C_1(eps) was redone with 0 <= -log lambda_0 <= 9b|B|. Correct.

**Corollary 1A (L119-121). HOLDS.** Immediate from Theorem 1(3). Scope: it refutes (LEV-down) with one factor E > 1 for all ordered levels, which row 1610 L188 already called "too strong to be true" (ARGUED there). E = 1 (no transport) is not touched. It does not touch the thermal form (VIR-down), which is the form the consumer uses.

**Corollary 1B (L123-127). HOLDS as stated; the RESULT wording is too broad.** On an eigenvector the commutator term vanishes ((A Rhat - Rhat A) psi_i paired with psi_i gives r_i<psi_i,A psi_i> - r_i<psi_i,A psi_i>), <psi_i, Rhat' psi_i> = r_i (D_i - D_0) and <psi_i, Phi(Rhat) psi_i> = r_i m_i. So the form inequality on all of H_0^perp is the level inequality D_i - D_0 >= kappa m_i for every i, which Theorem 1(2) kills. Correction of scope: what is refuted is a form inequality with a constant kappa > 0, no error term, required on every state of the complement of the vacuum. Weighted forms (for example with a weight Rhat^{t-1}, which is exactly the thermal trace), forms on a low-energy subspace, or forms with an additive error are not refuted. The RESULT phrase "every all-state operator form bound on H_0^perp" must be read with this scope.

**Corollary 1C (L129-133). HOLDS, and is irrelevant to the target.** Convergence for t > 0 from (1.1) and Tr C^t = (sum_j (2j+1)^2 c_j^t)^m. The epsilon split and sum_i m_i = infinity were redone. But (VIR-down) is asked only at t = t(beta) >= u >= 6 on the characteristic (row 1610 3.5, check 1613), never as t -> 0. A "small-time lower bound" is not an input of any consumer on file. So 1C excludes nothing that a route needs.

Verdict on claim 1: HOLDS (Lemma 1, Theorem 1, 1A, 1C), HOLDS AFTER CORRECTION of scope (1B as worded in the RESULT). The content is a proof-method obstruction: it shows that the high-spin tail has relative rate zero at every coupling on every finite box, so no levelwise form can work. It reads only the compact link group and holds verbatim for compact U(1) and 5D SU(2) (the author says so, L334).

## 2. Claim 2: Theorem 2 (compact Gaussian U(1) with P_0)

### 2.1 Line by line

**The model (L143-152). HOLDS AFTER CORRECTION of its description.**
- Flux factor. For a uniform spatial field the holonomy Phi_i in R/2piZ (the uniform link value has period 2pi/n modulo the large gauge transformation e^{2 pi i x_i/n}) has temporal kinetic term (beta/2) n^3 (Phi_dot/n)^2 = (beta n/2) Phi_dot^2. The Villain transfer kernel on e^{iQ Phi} is e^{-Q^2/(2 beta n)}. A spatial centre half-turn shifts Phi_i by pi and acts by (-1)^{Q_i}, so P_0 keeps Q in (2Z)^3. Correct.
- Photon factor. Two transverse modes per nonzero k, with the lattice-time free dispersion sinh(omega/2) = sqrt(sum sin^2(k_j/2)), independent of beta (row 929 dispersion as quoted in check 1613 L109). P_0 acts trivially on them. Correct.
- Correction. The text calls R_flux (x) R_phot "the zero-monopole sector of 4D Villain U(1)". The zero-monopole sector also contains the spatial magnetic flux sectors M in Z^3 (integer flux through the three spatial 2-tori). They are P_0-neutral (a flip leaves every plaquette fixed) and have energy 2 pi^2 beta |M|^2/n. The model of L145 is the zero-monopole, zero-magnetic-flux sector. Effect (ARGUED by this checker, GUIDE-checked): the magnetic factor depends on (t, beta) through t beta, so it adds -E_mag/beta to the numerator and +E_mag to the denominator of R. On a cold torus t > 1.7 beta n, so its weights are at most e^{-3.4 pi^2 beta^2} relative to the flux weights; at beta >= 4 the change in beta R is below 10^{-200}. Statements (1)-(3) of Theorem 2 survive for the corrected model, with "0 < R < 1/beta" in (1) replaced by "R < 1/beta" (the numerator becomes (E_flux - E_mag)/beta; I did not check its sign at hot times, where both terms are of order one; at cold times it is positive). Theorem 2 as printed is a theorem about the printed model, which is a legitimate positive trace-class family; the correction concerns only its name.

**(1) Global sandwich (L157-158, L168-169). HOLDS.** G_flux depends on (t, beta) only through t/beta, so beta d_beta log(1+G_flux) = E_flux; the photon factor has no beta. R = (1/beta) E_flux/(E_flux + E_phot). Redone.

**(2) Cold-torus bound (L159-162, L171-183). HOLDS.** Checked every inequality:
- 6 e^{-2t/(beta n)} <= G_flux <= G <= 4/21 gives 2t/(beta n) >= log(63/2) = 3.4500; the bound e^{3.4} < 30.375 uses e^3 < 1.65^6 = 20.18 < 20.25 and e^{0.4} < 1.5 (e^{0.4} = 1.4918). So t > 1.7 beta n.
- E_flux >= (126/25) x e^{-x}, x = 2t/(beta n): six terms with |Q|^2 = 4, divided by 1 + G_flux <= 25/21.
- E_phot = sum_k 2 t omega/(e^{t omega} - 1) is the correct -t d_t of -2 sum log(1 - e^{-t omega}).
- 2.5 |m|/n <= omega <= 2 pi |m|/n: sin x >= 2x/pi on [0, pi/2], concavity of arsinh on [0, sqrt 3], arsinh(sqrt 3) = log(2 + sqrt 3) = 1.317 > 1.1. Correct.
- t omega >= x + 1.5 t|m|/n needs 2.5|m| - 2/beta >= 1.5|m|, true for beta >= 2, |m| >= 1. t omega >= 8.5 > log 2.
- The prefactor uses the upper bound on omega and the exponential uses the lower bound; both factors are positive, so the product bound is valid. Shell count 24 r^2 + 2 <= 26 r^2, |m|_2 <= sqrt 3 r < 2r, r^3 <= e^{3(r-1)}, alpha >= 5, 1/(1 - e^{-2}) = 1.1565 < 7/6, 52 * 7/6 = 60.7 < 104, 4 pi 104/5 = 261 < 280, 1120 e^{-10} = 0.0508 < 1/10. All correct. The constant is generous; the true ratio E_phot/E_flux is far smaller (GUIDE below).
- Hence R > 10/(11 beta) > 9/(10 beta) at beta >= 4, every n >= 4, every real t with G <= 4/21.

**(3) Failure of (T-down) (L163-165, L185-186). HOLDS.** G(u; beta_1) >= 6 e^{-2u/(beta_1 n)} = 6 e^{-1/(256 beta_1)} > 5 for beta_1 >= 1. With (VIR-down) on the window, kappa <= R < 1/beta pointwise, so t_h < u beta_h/beta_1 and G(t_h; beta_h) >= 6 e^{-2 t_h/(beta_h n)} > 6 e^{-2u/(beta_1 n)} > 5. Correct. Note that the first bullet alone already kills every (T-down) witness, by check 1613's mean-value argument (L105): the seed fails at the start.

GUIDE (floating point, one process, run from stdin; never a proof step): for n in {4, 8}, beta in {2, 4, 10}, at the first time with G <= 4/21 and at twice that time, beta R = 0.99999816 to 1.00000000 and E_phot/E_flux <= 1.9e-6; adding the magnetic flux factor changed beta R by less than 1e-10 in every case.

### 2.2 Is the model a fair comparison for the trigger of row 1610 section 4?

The trigger (row 1610 L241): "a lower bound for t a_0 - A_t against kappa t Ebar_t on cold neutral tori at late bare couplings, with a method that fails for the free photon".

Yes, it is a fair test of that trigger, with three scope remarks.
1. It is the leading weak-coupling model of 4D compact U(1) with the literal P_0 (the three Z_2 half-turns of the brief). It is an exact positive trace-class transfer family, gapless (m_1 = 2/(beta n) -> 0, and a massless photon), and its cold-torus rate is R in (10/(11 beta), 1/beta) at beta >= 4. So a cold-torus lower bound with kappa(beta) = c/beta, c < 10/11, is TRUE in a gapless compact model, and it fails for the free photon (R = 0). A method that proves only such a bound meets the letter of the trigger and cannot be selective.
2. It is not interacting Wilson or Villain U(1): monopoles and magnetic fluxes are dropped (the latter harmlessly, 2.1). So Theorem 2 does not prove the cold rate of weak Wilson U(1). It does not need to: a test of a trigger needs one gapless compact model in which the triggered inequality holds.
3. Its cold tori lie at t > 1.7 beta n. The consumer's characteristic starts at t = u = n/512, where this model is hot (G > 5). So the inequality holds in the model only off the consumer's path. This does not weaken the point about the trigger, which quantifies over all cold neutral tori.
4. With the full continuous centre in place of P_0 the flux levels disappear and the model has R <= 0 on cold tori (photon plus magnetic sectors). The comparison therefore depends on the literal P_0, as the brief's setting requires.

### 2.3 What exactly is weak: the trigger, not row 1610's selectivity claim

- The trigger is weak. It names no size for kappa. Theorem 2 with Theorem 3 below shows the size that matters: a rate O(1/beta) is met by gapless compact U(1) and gives no budget on windows of bounded bare width. A sharpened trigger: a lower bound kappa >= kappa_0 > 0, uniform in K, on the cold part of [beta_K, beta_{K+r}] for some fixed r (or directly the budget int kappa >= log(512 log(21/4)/(n_K m_1(beta_h)))), by a method that fails both for the free photon and for compact Gaussian U(1) with P_0.
- Row 1610 L137 is not refuted in its conclusion. L137 says weak compact U(1) fails, first failing line "(VIR-down) with any kappa whose integral meets the budget". Theorem 2(3) confirms this in the Gaussian model, and check 1613 L110 had already proved failure (via G_even(u) >= 2 d_gamma^4 > 1) for Villain and weak Wilson.
- What Theorem 2 refutes is L137's stated reason. L137 argued that the beta dependence "does not change the low levels of a cold box at leading order. So the rate is zero to that order". In the Gaussian model the lowest levels of a cold box at beta >= 2 are the even electric flux levels (2/(beta n) < 2.5/n <= omega_min), and they move at the logarithmic rate exactly 1/beta. So the rate is not zero; it is 1/beta, which is o(1) only as beta -> infinity. The mechanism of failure is also different from the photon's: (VIR-down) with kappa near 1/beta transports the flux part exactly (G_flux depends on t/beta), so the hot flux sector at t = u stays hot. Check 1613 L110 had already said that the photon-rate claim of L137 "does not follow".
- So the RESULT phrase "refuting row 1610 L137" is an overclaim. Correct form: Theorem 2 refutes the reason given in L137 and confirms its conclusion; it shows that the section 4 trigger needs a size condition on kappa and a compact-U(1) test.

Verdict on claim 2: HOLDS AFTER CORRECTION. Theorem 2 (1)-(3) hold as stated for the printed model; the model is the zero-monopole, zero-magnetic-flux sector (not the whole zero-monopole sector), which does not change (2)-(3). "Refuting row 1610 L137" must read "refuting the argued reason in L137; its conclusion stands". "The section 4 trigger is weak" HOLDS.

## 3. Claim 3: Theorem 3 (budget, width, rate obstructions)

**(1) Necessary budget (L200-201, L213). HOLDS.** e^{-t_h m_1(beta_h)} <= G(t_h; beta_h) <= 4/21 gives t_h m_1(beta_h) >= log(21/4), and t_h = (n_K/512) e^{int kappa}. log(21/4) = 1.6582 > 1.65 (the printed series bound for e^{0.65} is correct), so 512 log(21/4) = 849.0 > 844. Standing: this is ON FILE in substance. Check 1613 L111 states "HOT gives the necessary bound t_h m_{1,h} >= log(21/4)". Row 1618's 0.1 duplicate check does not list it. When n_K m_1(beta_h) >= 849 the bound is vacuous.

**(2) Width bound (L202-207, L215-223). HOLDS given row 1461 (2) (checked in 1462 Step 2, L46: "HOLDS") and check 1453 BND-1.** I read row 1461 L56-95: B_K = sum_{i<K} a_i + (1/s) sum_{i<K} q_i/(K-i) with one table for all roots, |beta_K(r) - B_K| <= C_I for K >= K_I and r in I, |sum_{u}^{v-1} a_i - s(v-u)| <= 2c, |q_i| <= Q. The difference B_{K+r} - B_K, the two harmonic bounds (Q/s) H_r, H_r <= 1 + log r, and the triangle inequality give (3.2) exactly as printed. The consequences are elementary: on windows of bare width at most Delta, sup kappa -> 0 forces int kappa -> 0, so either premise (limsup n_K m_1(beta_h) < 849, or liminf G(u_K(1+delta); beta_h) > 4/21) contradicts (HOT) eventually; and n_K m_1(beta_h) <= Gamma_h < 849 forces sup kappa >= (1/Delta) log(849/Gamma_h).
- Scope. The obstruction is conditional on one of the two hot-end premises. Neither premise is proved for Wilson on the calibrated trajectory; both are the hot-end component C2 of row 1610 (2.6, "NOT BUILT"). They are the physically expected behaviour of a small box (its dimensionless gap is about g^{2/3} times a constant, far below 849; GUIDE, belief I33). So section 6.3 item 4 of row 1618 ("PROVED insufficient", "Killed on fixed-physical-ratio windows") must read "PROVED insufficient on such windows given a hot-end premise that is itself open". The RESULT's "hot ultraviolet windows" carries the premise in the word "hot", and with that reading it HOLDS.

**(3) Large beta_h (L208-210, L225). HOLDS given row 1215 (5) (checked in 1221, L36, L75: "HOLDS").** Row 1215 (5) (L90-96, read) gives lambda_{j,+}/lambda_0 -> 1 at fixed n and fixed j as beta -> infinity, so m_1(beta; n_K) -> 0 and the right side of (3.1) diverges. The c/beta computation (t_h <= u (beta_h/beta_K)^c) and the c = 1/3 cancellation are one line each; correct. Standing: the c = 1/3 cancellation is the 5D and perturbative-SU(2) argument of row 1610 2.5 (L138-139, ARGUED) and of check 1613 L111 ("If n m_{1,h} <= C(beta_h n)^{-1/3} and the thermal rate ... is at most 1/(3 beta), then t_h m_{1,h} <= (C/512)(beta_K n)^{-1/3}"), here written as a conditional theorem. It is conditional on the toron scaling n m_1 <= C_0 beta_h^{-1/3}, which is not proved.
- One gap in the reading of (3). Theorem 3 does not exclude a rate c/beta with c > 1/3 on an unbounded window: if n m_1(beta_h) ~ beta_h^{-1/3}, then t_h m_1 ~ beta_K^{-c} beta_h^{c-1/3}/512 can exceed log(21/4) for beta_h large enough. Such a schedule would have to keep kappa >= c/beta > 1/(3 beta) through the perturbative part of the window, where the expected SU(2) rate is about 1/(3 beta) (GUIDE, toron scaling). So it is excluded physically, not by Theorem 3. The RESULT does not claim more than bounded windows and L^1 schedules, so this is a remark, not a correction.

### 3.1 What rate does (VIR-down) need on the band? Consistency with rows 1610 and 1619

- Theorem 3 needs, on a window [beta_K, beta_{K+r}] whose top end is a small hot box of side l b^{-r} with dimensionless gap gamma_h = n_K m_1(beta_{K+r}): int kappa >= log(849/gamma_h), over a bare width s r + O(1 + log r). For b = 3 (s = 11 log 3/(3 pi^2) = 0.408) and a top box 512 times smaller (r = 5.7, width 2.3), gamma_h about 4 gives an average kappa of about 5.4/2.3 = 2.3. This is my arithmetic with GUIDE inputs (gamma_h about 4 is row 1610's GUIDE value from belief I33).
- Row 1610 2.3 (L123) puts the budget "near 7" (GUIDE, Corollary B with N_0 about 10); row 1619 3.0 (L125, ARGUED) puts the average rate at "about 1/0.37 = 2.7". The natural scaling-regime rate is -d log a/d beta = 3 pi^2/11 = 2.69, which is 1/s per unit log b: if every low level falls like the lattice spacing, int kappa = r log b and t_h = u b^r, exactly the shrinking box. All three numbers agree to the accuracy of their GUIDE inputs.
- So Theorem 3 is consistent with the order-one estimate. It proves, conditionally on the hot end, the elementary half of row 1619 3.0 ("every bound kappa >= c/beta is worth c log(beta_h/beta_K), which tends to zero on a bounded window"). It does not prove the size of the needed rate (that needs gamma_h, which is C2), and it is not an obstruction to (VIR-down) on the band: an order-one rate is what a gapped scaling regime is expected to supply. It is an obstruction to suppliers whose rate is o(1) in the bare coupling, which covers every weak-coupling or 1/beta argument on file.

Verdict on claim 3: HOLDS, with the scope that (2) and the c/beta part of (3) are conditional on hot-end premises that are open (C2), and that (1) and the c = 1/3 cancellation are ON FILE in check 1613 L111.

## 4. Claim 4: Theorem 4, Remark 4.2, Propositions 5 and 6

**Theorem 4(1) (L239-242, L254-256). HOLDS.** The anisotropic operator P_0 M_{beta_sigma} C_{beta_tau} M_{beta_sigma} P_0 is the transfer operator of the action beta_tau (temporal) + beta_sigma (spatial), and the twists sit on temporal plaquettes only, so S_sigma does not depend on z. With f = log(1 + G) = log Z_+ - t log lambda_0, d_tau f = t a_0^tau - A^tau and d_sigma f = t a_0^sigma - A^sigma (Lemma D1 argument per coupling; joint analyticity in trace norm follows from check 1613 (R) item 1 with two couplings). The chain rule along (xi beta, beta/xi) gives d_xi f = beta(d_tau f - d_sigma f), and (4.1) is d_beta f = d_tau f + d_sigma f rewritten. (4.2): d_sigma R = -(1/2)(V_1 R + R V_1) on H_0, so <psi_i, d_sigma R psi_i> = -lambda_i <psi_i, V_1 psi_i>, and the trace formula gives the printed spectral form. Redone.

**Theorem 4(2) (L243-248, L258). HOLDS; it is an identity, not a constraint.** If (ii) fails, (4.1) and (VIR-down) at integer t give (i). Since (4.1) is exact, the pair (i)-or-(ii) is (VIR-down) at the point split into two terms. It is equivalent to (VIR-down) at that point for C chosen after the fact, so it moves no open item.

**Theorem 4(3) (L249-251, L260-262). HOLDS.** sinh(omega/2) = sqrt(l)/(2 xi) is the anisotropic free lattice dispersion (ratio of spatial to temporal coefficient 1/xi^2). -d_xi omega at xi = 1 is 2y/sqrt(1+y^2) = 2 tanh(omega/2) < omega. Per mode, d_xi log(1+G_phot) = 2 sum t (2 tanh(omega/2))/(e^{t omega} - 1), between 0 and E_phot. The non-compact photon has d_beta f = 0, so t a_0^sigma - A^sigma = -(1/(2 beta)) d_xi f < 0. In the Gaussian model the flux energies |Q|^2/(2 beta_tau n) depend on beta_tau only, so the flux part contributes E_flux to d_xi f and 0 to the spatial deficit. Redone. The final sentence ("both alternatives fail for kappa > 1/beta, C = 1") is the restatement of R < 1/beta from Theorem 2(1). Correct.

**Remark 4.1 (L264-266). Labels correct.** The force identity is labelled ON FILE in substance (rows 913, 934); I did not read those rows, so I do not check it. The toron scaling m proportional to xi^{-1} n^{-1} beta^{-1/3} was redone from the balance 1/(beta_tau lambda^2) ~ beta_sigma lambda^4; it gives d_xi f = t Ebar and t a_0^sigma - A^sigma = -(1/(3 beta)) t Ebar, as printed (ARGUED, a model). The scaling-regime sentence is GUIDE, as labelled.

**Remark 4.2 (L268-269). HOLDS.** omega_1 = 2 arsinh((1/2) sqrt(m_K^2 + 4 sin^2(pi/n_K))), u_K omega_1 -> 2 pi/512, e^{-2 pi/512} = 0.988 > 4/21. So the seed fails in the product and every (T-down) witness fails by check 1613 L105. It is a one-line consequence of the product formula. It tests the target (T-down), not a method: it says the target itself fails (g4), as row 1610 2.5 already argued (L140) and as any target implying the seed must.

**Proposition 5 (L277-306). HOLDS given its inputs; close to ON FILE.**
- Step 1. Row 1143 (1) (L19-28, checked in 1144 L50 for every sign choice) gives Z^z <= I(beta/2)^M J_z(beta/(2Q)). For multi-plane temporal twists the zero locus of A_z was redone: h_0, h_1 anticommuting imaginary units, h_j = +-1 if z_j = 0, h_j = +-u_1 (pure imaginary) if z_j = 1. It is one 3-dimensional orbit of constant gauge rotations, of codimension 9 in SU(2)^4. The three quadratic lower bounds on U_z were redone: the 01 term as in row 1143 L77-78; (u_0 hat . u_j)^2 + (u_1 hat . u_j)^2 <= (1 + |y|)|u_j|^2 (top eigenvalue of the Gram matrix); 1 - |u_0 x u_j|^2 >= x_j^2 and |u_1 x u_j|^2 = |u_1|^2 |w_j|^2. Two density constants are misstated (the marginal density of u_j is 1/(pi^2 sqrt(1-|u|^2)), not 2/(pi^2 sqrt(...)); the two-sheet Haar density in (x_j, w_j) is at most 5/(4 pi^2), not 5/(2 pi^2)). Both errors are in absolute constants C and do not affect J_z(s) <= C'(1+s)^{-9/2}. Then Z^z = O(beta^{-9V/2}) for all seven z != 0 (3M/2 = (9V-9)/2). Row 1143 (3) covers one twisted plane only; this extension to two and three twisted temporal planes is the new part, and it is correct.
- Step 2. Row 1143 (11) (L178-180, checked in 1144 L108) gives the untwisted Z^0 ~ c beta^{-(9V-3)/2} log beta. Row 1215 L21-24 and (4) (L67-75, checked in 1221 L35, L73) give lambda_0 = I_beta^{3n^3} lambda_0(F_{beta,0}), lambda_0(F) -> e^{-3 S_n(0)} > 0, I_beta = (2 pi^2)^{-1}(2 pi/beta)^{3/2}(1 + o(1)) (row 1215 L50). log Z_+ and log lambda_0 are convex (log of a sum of Laplace transforms; row 708 Lemma 4.2). The secant sandwich gives beta f' -> -p for each. Subtraction gives 3/2. Redone.
- Standing. Row 1143 (13) proved the same limit 3/2 by the same secant method for the excess D = F - n^4 f (check 1144 L136), and row 1215 (20) (L317-329, checked in 1221 L213) gives (1 + G(t; beta))/(beta^{3/2} log beta) -> a positive limit at fixed n and integer t >= 3. Proposition 5 is the coupling-derivative version of row 1215 (20); the secant step is needed because log(1 + G) is a difference of convex functions. Not a duplicate, but its content is ON FILE in substance. It is a hot (G -> infinity) fixed-box statement and non-selective, as the author says.

**Proposition 6 (L308-324). HOLDS.** The trace formula d_beta G + kappa t d_t G = t sum_{i>=1} ((D_i - D_0) - kappa m_i) e^{-t m_i} is check 1613 (R). The tail bound uses D_i - D_0 >= -9|B| (Theorem 1(1)), monotonicity of x e^{-tx/2} for x >= 2/t, and sum_{m_i >= Lambda} e^{-t m_i/2} <= G(t/2). Redone. The scope paragraph (Lambda = 2 m_1 + O(log n/n)) is ARGUED, and correct as an order of magnitude: with |B| = n^3, t = n/512 and m_1 >= log(21/4)/t, (5.2) needs t(Lambda/2 - m_1) >= log(9 n^3 M_0/((kappa_1 - kappa) m_1)), that is Lambda - 2 m_1 of order 4096 log n/n. Note that this window reaches energies of order log n/n, about 8 log n times the cold scale 1/t. Hypothesis (5.3) is (VIR-down) restricted to that window, so Proposition 6 is a localization of the target, not a supplier, and it needs a half-time bound G(t/2) <= M_0 that is not on file at the cold times of the characteristic.

Verdict on claim 4: HOLDS. Theorem 4(2) is an identity rewrite of (VIR-down) at a point. Proposition 5 is close to ON FILE (rows 1143 (13), 1215 (20)); its seven-twist extension of row 1143 (3) is correct with two misstated absolute constants that do not matter.

## 5. What is left of (VIR-down) on the band, and equivalence to (PUR-io)

What row 1618 removes (as checked above):
- The level form. (LEV-down) with E > 1 is false on every finite Wilson box (Corollary 1A), and so is every form inequality with a constant positive rate on all states of the complement of the vacuum (Corollary 1B, with the scope of section 1).
- Small rates. A cold-torus rate of order 1/beta is met by a gapless compact model with the literal P_0 (Theorem 2) and gives no budget on windows of bounded bare width (Theorem 3(2), given an open hot-end premise). An L^1 schedule cannot reach arbitrarily large beta_h at fixed K (Theorem 3(3)).

What is left, unchanged in sign and size:
- The thermal (VIR-down) at the cold points of the characteristic t(beta) >= u on [beta_K, beta_h], with int kappa >= log(512 log(21/4)/(n_K m_1(beta_h))). On a window [beta_K, beta_{K+r}] of bounded bare width this is an average rate of order one (about 2.3 to 2.7 with the GUIDE inputs of section 3.1), uniform in K.
- By Proposition 6 (and, sharper, row 1617 (3), (6)-(7)) the high-spin tail can be paid for, so the order-one surplus must come from a low-energy window, given a half-time bound G(t/2) <= M_0 that is not on file at those times.
- By Theorem 4 the surplus must appear as a spatial-action deficit 2(t a_0^sigma - A_t^sigma) >= (kappa - C/beta) t Ebar_t, or as an anisotropy response above C t Ebar_t. This is a rewrite of the same open inequality, with neither term bounded by any method on file. Both terms have the wrong size in the free photon and in compact Gaussian U(1) (Theorem 4(3)); the 4D SU(2) value is GUIDE only (Remark 4.1).
- No supplier, no sign, no size is proved for any level or thermal sum at a box coupling of order one. C2 (the hot end) is also untouched.

Equivalence to (PUR-io). I agree with row 1618 6.2: no statement of the row is equivalent to (PUR-io).
- Theorems 1, 2, 3(2)-(3), 4(1), 4(3), Proposition 5 and Remark 4.2 are unconditional or model statements, true whether (PUR-io) holds or not.
- Theorem 3(1) is a necessary consequence of (HOT) (and is ON FILE, check 1613 L111).
- Theorem 4(2) is (VIR-down) at one point rewritten as an identity, and Proposition 6's hypothesis (5.3) is (VIR-down) restricted to a window. Both are equivalent to, or sufficient for, the open input (VIR-down) at one point. They are not equivalent to (PUR-io). By check 1613, (T-down) implies (PUR-io) by enlargement and the converse is open, so a pointwise rewrite of (VIR-down) inherits that standing and no more.
- The obstructions of the row read the compact link group (claim 1), a Gaussian model (claim 2) and the calibration table (claim 3). None is a selective input, and the author does not claim one.

## 6. Comparison with rows 1617 and 1619 (read after sections 1-5)

Read: `library/gap-vir-down-astra62.md` (row 1617) L15-64 ((1)-(3)) and L155-170 ((9)); `library/gap-vir-down-fable.md` (row 1619) L30-112 (2.1-2.4) and L121-131 (3.0). I did not open `library/gap-vir-down-astra62-check-opus.md`.

| Statement | Row 1618 (this row) | Row 1617 | Row 1619 |
|---|---|---|---|
| Ordered ratio m_i(b_1)/m_i(b_2) -> 1 | Theorem 1(3) | (9) | Proposition UV-LEV, with explicit constants A_0, A_eps |
| (LEV-down) fails for E > 1 | Corollary 1A | L170 | Corollary LEV-FAIL, with an explicit failing index |
| Relative slope of high levels | Theorem 1(2): (D_i - D_0)/m_i -> 0 | (2): beta b_i log m_i / m_i -> 1, so b_i > 0 eventually and the rate is 1/(beta log m) | no slope theorem; GUIDE table of electric rates (3.0) |
| Tail in the thermal test | Proposition 6 (needs G(t/2) <= M_0, uses only D_i - D_0 >= -9 abs(B)) | (3): the tail is strictly negative, between -kappa B and -(kappa/2) B; (6)-(7): spin cutoff uniform in the box | Proposition TRUNC: a truncated level form needs rates up to energy of order beta n^2 |
| Size of the needed rate | Theorem 3 (bounded windows; conditional on the hot end) | (14) (not read here) | 3.0, ARGUED: about 2.7 |

Findings.
- The three level obstructions agree. Theorem 1(3) here, (9) of row 1617 and UV-LEV of row 1619 are the same statement, proved by the same route: the min-max sandwich e^{-beta V_*} C <= C^{1/2} M^2 C^{1/2} <= C on the neutral space, plus the one-link factorial bounds with an exponent 1 + eps. I checked row 1618's proof line by line (section 1) and read row 1619's Steps 1-6 without finding an error; I did not check row 1617 (2) or (9) line by line. So the agreement is three authors on one derivation, not three independent checks in the sense of a different derivation. The FINISH RESULT phrase "three providers independently" should say "three authors, one route".
- Row 1617 (2) is strictly sharper than Theorem 1(2): it gives the exact slope asymptotic and the positivity of the slope of high levels, where Theorem 1(2) gives only that the ratio tends to zero (its lower bound -9 abs(B)/m_i allows either sign). Row 1617 (3) and (6)-(7) also control the tail more sharply than Proposition 6.
- Row 1618 adds to the other two: Corollary 1B (commutator-corrected form inequalities on eigenvectors reduce to the level form), Corollary 1C (t -> 0, irrelevant to the consumer), and the cleanest all-beta link bounds (Lemma 1). Row 1619 adds TRUNC; row 1617 adds the slope asymptotic, the tail sign and the uniform spin cutoff.
- None of the three rows proves anything about the thermal form on the band. All three say so.

## RESULT

RESULT: Row 1622, Claude Opus 5.5 hand check of row 1618 (gemini-4-neon-xhigh). No Lean; one float guide run outside the repo, not a proof step.
Claim 1 HOLDS: Lemma 1, Theorem 1, Corollaries 1A, 1C; 1B HOLDS AFTER CORRECTION of scope (a constant-rate form on every state, no error term;
weighted or windowed forms are not refuted). 1C is irrelevant: the consumer uses t >= u only. All read only the compact link group.
Claim 2 HOLDS AFTER CORRECTION: Theorem 2 (1)-(3) hold; the model is the zero-monopole, zero-magnetic-flux sector (adding magnetic fluxes is harmless).
It is a fair test of the row 1610 section 4 trigger. The trigger is weak: it names no size for kappa. Row 1610 L137 is not refuted: its reason
("rate zero") is wrong, since cold low levels are even flux levels at rate 1/beta, but its conclusion (compact U(1) fails) stands, as check 1613 proved.
Claim 3 HOLDS: (3.1) is ON FILE (check 1613 L111); the width bound follows from row 1461 (2); the o(1), O(1/beta) obstructions on bounded windows
are conditional on an open hot-end premise (C2). The needed average rate, about 2.3-2.7 (GUIDE inputs), agrees with rows 1610 and 1619 and 3 pi^2/11.
Claim 4 HOLDS: Theorem 4(2) is an identity rewrite of (VIR-down); Proposition 5 is close to ON FILE (rows 1143 (13), 1215 (20)), with two harmless misstated constants.
Nothing is equivalent to (PUR-io). Theorem 1 agrees with row 1617 (9) and row 1619 UV-LEV (three authors, one proof route); row 1617 (2) is sharper than Theorem 1(2).
Overall: HOLDS AFTER CORRECTION. Outcome (c) only for the level form and small rates. Thermal (VIR-down) on the band, (HOT), (PUR-io) and the gap stay open.
