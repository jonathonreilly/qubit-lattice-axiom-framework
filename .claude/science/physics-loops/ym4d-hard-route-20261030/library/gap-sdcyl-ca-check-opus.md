# Check of gap-sdcyl-ca-astra.md (FINISH row 868)

- Checker: Claude Opus 5.5 (high effort), by hand, no subagents.
- Clone commit: 69d39b9d9e35a4b442a34927aeaa4c5b9d62edd5 (/Users/jonreilly/ym4d-lead/clone, pulled 2026-11-12, already up to date).
- Object checked: D/library/gap-sdcyl-ca-astra.md (row 865, written by OpenAI Codex gpt-6-astra).
- Sources (row 844 section 5, the Lemma FL check, was read; it is not used by the target): CA-I Theorem 0 (iv), lines 2715-2826 of /Users/jonreilly/ym4d-lead/sa/theorem_0_complete_account_raw_I.tex (Sussman-Alpoge complete account at 31a47c543775; mathematics credited to Ethan Sussman and Levent Alpoge, text by Claude and Codex); D/library/gap-e17phys-opus.md sections 4-5 (row 844); D/library/gap-e17phys-check-astra.md section 13.
- D = .claude/science/physics-loops/ym4d-hard-route-20261030.

Source bytes: sha256 of CA-I starts 4cb5cb5e0af8dbdd and of CA-II starts 6a1f74b05f74ba44, the hashes the target records for revision 31a47c543775. Bounded extra reads (to check the target's locators that my six statements rest on): CA-II 142316-142372 (Corollary 8.22:cor-transfer-depth-floor, statement) and a keyword search in 142372-142546 (its reserve arithmetic); CA-I 101-102, 208, 218, 731 (trace normalization, observable, connected Schwinger function). Nothing else in CA-II was re-read. Marks: READ = I read the source text at the cited lines; checked = I re-did the step by hand.

## Statement 1. The reading of c_K, C_K and the depth floors (target Step 4) -- HOLDS

Line by line against CA-I 2715-2795.

1. c_K, C_K. CA-I 2729 introduces "constants c_K, C_K > 0", 2734-2735 says none depends on K, g_0, m, d or the position, and c_K (with C_W) depends on theta. The sandwich c_K ||f_1|| ||f_2|| <= K_s^star(f_1,f_2) <= C_K ||f_1|| ||f_2|| (CA-I 2778-2781) holds for every pair in T(d; theta) at every admitted d. CA-II 142319-142320 (READ) confirms that the corollary carrying the half-error uses "the constants k_W, c_K, C_K of that clause". The target reads c_K, C_K as these absorbed sup-norm constants, not as the raw c_0, C_0 of CA-II Lemma 8.1. That reading is right. The two constants may depend on g, L, the parameters p and theta. g and theta are fixed before the cutoff, so this does no harm.
2. K_s^star is K_s read on the bare lattice of the reference torus T_{m_T(g_-(g))} (CA-I 2747-2748). It depends on K. Its comparison constants do not. The target says the same.
3. Depth floors. CA-I (3.1:eq-main-1, -2) requires max{s_W, s_vol^star, s_T} <= s(d) and K - s(d) >= k_W. The target's admission contains both. The target adds the three H-depth inequalities at s itself (s - r(s) >= s_*, s >= m_T(g), 2B(r(s)+1) <= x_s). CA-I defines s_W(g) as the least s with these three (CA-I 2755-2758). It does not say they hold at every s >= s_W. The extra requirement only shrinks the admitted set of d. It is satisfiable for small d only if the three hold on a tail; the target cites CA-II 69049-69069 for that. I did not read that range: NOT CHECKED here, and it matters only for the existence of an admissible d, not for any inequality below.
4. Cutoff floor. K_0 is fixed by K - s(d) >= k_W and a_K <= min{d/8, theta^2 d/32}. Both involve only K, d, theta. So K_0 is fixed before the cutoff. Note that CA-I's own K - s >= k_W already gives a_K = L^-K <= L^-(k_W + s) <= L^-k_W d, because d >= C_W(s) L^-s >= L^-s by the definition of s(d). The bound theta^2 d/32 (for the discrete admission, CA-II 68788-68795, NOT READ) is an extra restriction. It is harmless, but it is not required by CA-I's displayed statement, which takes the tests as continuous functions on T_m.
5. Coupling ceiling. CA-I states the clause for g <= gamma_W^T. The target's gamma_W^VT is the ceiling of the corollary that proves the half-error (CA-II 142321-142322 READ: "Let gamma_W^VT be the coupling ceiling of (8.22:eq-expansion-consistency-a)"; conclusion for g <= gamma_W^VT, 142345). So gamma_W^VT is a real account symbol, not a typo. The strict inequality is P9's extra qualification and only shrinks the range.

One wording point, no change of substance. The target writes that "all kernel, extraction and transfer constants must be chosen for this admitted shape", after mentioning both theta and the discrete shape theta/2. Under CA-I's displayed statement, the tent pair is in T(d; 1/300) as continuous functions, so c_K = c_K(theta = 1/300). If the discrete admission is used instead, c_K is the constant at the discrete shape. Either way it is one fixed positive number, and every later step uses only that. The target should name which one it means.

Rests on account statements that are themselves conditional: the sandwich comes from CA-II 8.1:lem-kernel-bounds with its hypotheses (h1)-(h3), including the free comparison (target Step 4; I did not re-read CA-II 69925-70152). The target marks this correctly as a named hypothesis.

## Statement 2. The bounds on K_s^star at the two tent separations (target Step 5) -- HOLDS

I re-did each membership condition of CA-I's class T(d; theta) (CA-I 2761-2765) for (f, h_1) and (f, h_2), with f = (r - |x - x_0|)_+, r = d/4, theta = 1/300, h_i = tau_{t_i a_K} f, t_1 = ceil(3d/(2a_K)), t_2 = 2t_1, a_K <= d/8.

- Non-negative, Lipschitz, not zero: yes.
- Support in a ball of radius d: the closed ball of radius d/4. Yes.
- Mass: integral of f = 2 pi^2 int_0^r (r - p) p^3 dp = 2 pi^2 r^5 (1/4 - 1/5) = pi^2 r^5/10. The class needs theta ||f|| d^4 = theta r (4r)^4 = 256 r^5/300. Since pi^2/10 = 0.987 > 0.853, yes.
- Lipschitz: Lip f = 1 <= ||f||/(theta d) = (d/4)(300/d) = 75. Yes.
- Separation window: sigma = t_1 a_K is in [3d/2, 3d/2 + a_K). The distance between supports (balls of radius r centred at x_0 and x_0 + t_i a_K e_0) is t_i a_K - 2r. For i = 1 it is sigma - d/2, in [d, d + a_K). For i = 2 it is 2 sigma - d/2, in [5d/2, 5d/2 + 2a_K). Both lie in [d, 6d] because a_K <= d/8. Yes.
- Common ball: centre x_0 + sigma e_0; the farthest point of either support is at distance sigma + r < 7d/4 + a_K <= 2d (needs a_K <= d/4). So both pairs fit in one radius-2d ball, inside the radius-5d ball the transfer clause asks for (CA-I 2792-2794).

So both pairs are in the class, and the class-wide sandwich of CA-I 2778-2781 gives, with ||f|| = ||h_i|| = r:

  K_s^star(f, h_2) >= c_K r^2,   K_s^star(f, h_1) <= C_K r^2,   K_s^star(f, h_2)/K_s^star(f, h_1) >= c_K/C_K.

The denominator is positive because K_s^star(f, h_1) >= c_K r^2 > 0. The target is right not to multiply in (2/7)^8: that factor came from the explicit |x - y|^-8 kernel (row 844, 3.2 step (3)), and the class-wide constants already absorb the dependence on the separation over [d, 6d]. The bound is weak (c_K/C_K may be far below (2/7)^8), but it is valid. The positions are irrelevant: CA-I asserts the sandwich uniformly in the position (CA-I 2734).

The reflection symmetry and centre-blindness of O(f) needed by Lemma W are row 844's (3.2 step (1)), checked at row 848 section 5; I did not redo them. The observable agrees with the account's: CA-I 208 and 101-102 (READ) give O(f) = sum_p f(x(p)) [1 - Re tr U(dp)] with tr 1 = 1, which is row 844's a_p = 1 - (1/2) Re Tr U_p at N = 2, and S^T_2 is the connected two-point function (CA-I 218, 731 READ).

Rests on: the sandwich itself, which is conditional on CA-II's (h1)-(h3) (see Statement 1).

## Statement 3. How the half-error |R| <= 1/2 is carried (target Steps 2-4) -- HOLDS, conditional on the named premises; one marking correction

1. CA-I alone does not reach the cylinder. CA-I (3.1:eq-main-3) gives |R_{K,m}| <= 1/2 only on the cubic tori T_m, m >= m_T(g_-(g)), and its volume transfer (CA-I 2790-2799) only between two cubic tori. Neither covers a rectangular torus or the cylinder. The target does not claim otherwise. It goes back to the reserve inside the proof.
2. The reserve (READ CA-II 142316-142372 and the arithmetic lines found at 142372-142546). Corollary 8.22:cor-transfer-depth-floor assumes (a) the single-torus witness law with |R'| <= 1/4 below the horizon and (b) the short-distance volume corollary. It concludes |R_K| <= 1/2 with the same reference kernel K_s^star. The steps are "<= (1/9) b_0 c_K x_s^-2 ||f_1|| ||f_2|| <= (1/4) M^star" because 1/9 = (1/4)(4/9), then |R_K| <= 1/4 + 1/4. The target's Step 2 reproduces this.
3. I redid the arithmetic. M^star = zeta'^2 b_0 g_{K-s}^4 K_s^star >= (4/9) b_0 c_K x_s^-2 ||f|| ||h||, from zeta' >= 2/3 and g_{K-s}^4 >= x_s^-2. CA-I's own corollary display (2/9 = (1/2)(4/9), CA-I 2786) uses the same lower bound on g_{K-s}^4. s(d) >= 1, because d <= 1/40 < C_W(0). Then minimality of s(d) and monotonicity of C_W give d < C_W(s-1) L^-(s-1) <= L C_W(s) L^-s. Hence C_T d^2 ||f|| ||h|| < C_T L^2 C_W(s)^2 L^-2s ||f|| ||h|| <= (1/9) b_0 c_K x_s^-2 ||f|| ||h|| <= M^star/4, using the s_T floor at v = s. With S_target = M^star(1 + R') + Delta, R = R' + Delta/M^star. So |R| <= 1/4 + 1/4 = 1/2. The reserve is additive, as the target says. No relative errors are multiplied.
4. Rectangles. The only new input is that the transfer bound holds between a rectangular torus (periods q_mu l_star^CA) and the reference torus, with the same C_T. I checked the structure of target Step 3 against row 844 P1-P3 and row 848 sections 9-11 (READ; HOLDS there, section 9 after correction). I redid the E_star cancellation: J_T^-1 [ (V_T/V_star)(E_star + Re E_src + E_+ V_star) - V_T (E_star/V_star - C_low - delta_vac) ] = J_star^-1 Re E_src + (E_+ + C_low + delta_vac) l_c^4, with J_T = V_T/l_c^4 and J_star = V_star/l_c^4. It matches the target. Q_star and C_VT contain no target period, so C_T does not depend on q_mu. I did NOT re-read the CA-II locators of Step 3 (140995-141852, 141994-142100, 61205-61415). The claim that the CA-II rectangular pressure lemma is explicitly rectangular is therefore the target's READ, not mine.
5. Cylinder limit. The bound |S_2^{T_q} - M^star| <= M^star/2 is uniform in q, and M^star does not depend on q. Row 844 Lemma W(i) gives trace-norm convergence of the three moments at fixed cutoff (row 848 sections 1 and 12, HOLDS). The closed interval survives. Checked.
6. The half-error is never combined with a kernel approximation. Each covariance is M^star_i (1 + R_i), with the lattice kernel kept. So the obstruction of row 848 section 13, (1 + R)(1 + delta) - 1 reaching 1/2 + 3 delta/2, does not arise. The optional continuum version in target Step 6 is also correct arithmetic: 1/18 = (1/8)(4/9) gives a transfer share of 1/8; |R + delta + R delta| <= 3/8 + 1/16 + 3/128 = 59/128 < 1/2. It is not used.

Correction (marking only). Target Step 4's proof says "The reference witness has error at most 1/4 (CA-II 142328-142346, with its explicit antecedents)". At those lines the quarter-error law is hypothesis (a) of the corollary, not its conclusion. It is stated only for couplings below the horizon, m_T(g_-(g)) <= m_V(g). The conclusion is stated for g <= gamma_W^VT. The target should say that the quarter error is an assumption of 8.22:cor-transfer-depth-floor, to be supplied by the reference-witness theorem it cites (CA-II 144388-144445, 144797-144835, NOT READ here). It should also say that the corollary's ceiling gamma_W^VT and the horizon condition are what make (a) applicable. The target's "strictly below gamma_W^VT, or require the reference-horizon inequality" covers this in substance. No inequality changes.

Rests on: hypothesis (a) (the quarter-error reference witness) and hypothesis (b) (short-distance volume independence) of CA-II 8.22:cor-transfer-depth-floor; the vacuum-density, face-series and source-energy hypotheses of the volume-transfer theorem; and row 844 Lemma F and the row 848 rectangular dictionary. The target's table marks these premises ARGUED, which is right.

## Statement 4. rho_CA = c_K/(3 C_K) (target Step 5) -- HOLDS

- Lemma W(i) (row 844 2.2, READ) gives G(u) = the connected cylinder correlation of F = O(f) and its translate by t = u + w steps. With h_i = tau_{t_i a_K} f, G(u_i) = S_2^cyl(f, h_i), where u_i = t_i - w. u_1 >= 0: w <= 2r/a_K + 3 = d/(2a_K) + 3 and t_1 >= 3d/(2a_K), so u_1 >= d/a_K - 3 >= 5 at a_K <= d/8. Checked.
- A common prefactor. Both pairs use the same d, so the same s = s(d), the same zeta'_{K-s}, g_{K-s} and b_0 (CA-I 2774-2776: zeta' and g are indexed only by K - s), and the same reference run. So Z_{K,s} b_0 is common and cancels. Checked.
- The ratio. G(u_2)/G(u_1) = [K_s^star(f,h_2)/K_s^star(f,h_1)] (1+R_2)/(1+R_1) >= (c_K/C_K)(1/2)/(3/2) = c_K/(3 C_K). The R_i are independent; the worst case is R_2 = -1/2, R_1 = +1/2. Checked.
- Positivity and range. G(u_1) >= Z b_0 c_K r^2/2 > 0 and G(u_2) > 0, which Lemma W(iii) needs. A non-empty class (the tent pairs) forces c_K <= C_K, so rho_CA <= 1/3 < 1. Lemma W(iv) gives G(u_2) <= G(u_1). Checked.
- The remark that separate extremal bounds on zeta' would lose a factor ((4/3)/(2/3))^2 = 4 is right arithmetic.
- The ratio does not depend on the observable's normalization: a constant shift or rescaling of O(f) changes G(u_1) and G(u_2) by the same factor. So the trace convention (CA-I 101-102, tr 1 = 1) does not enter rho_CA.

Rests on (SD-cyl-CA) (Statement 3) and the sandwich (Statement 1). Given those, it is exact.

## Statement 5. The exponent 2A/(3d) in Proposition W-phys-CA -- HOLDS

- Lemma W(iii) (row 844 2.2, READ; checked HOLDS at row 848 section 3) needs integers 0 <= u_1 < u_2 with G(u_2) > 0 and a >= u_2 - u_1. Here u_2 - u_1 = t_2 - t_1 = t_1. Time a = n_A = A/a_K. t_1 a_K < 3d/2 + a_K <= 2d <= A, using a_K <= d/2 and A >= 2d. So n_A >= t_1. Checked.
- It gives S_ev(n_A; B) >= (G(u_2)/G(u_1))^(n_A/t_1). The base is in [rho_CA, 1], so the right side is >= rho_CA^(n_A/t_1). The exponent obeys n_A/t_1 = A/(t_1 a_K) <= A/(3d/2) = 2A/(3d), because t_1 a_K >= 3d/2. Since rho_CA < 1, rho_CA^(n_A/t_1) >= rho_CA^(2A/(3d)). Checked.
- The even-gap by-product. Lemma W(iv) gives m_ev <= log(G(u_1)/G(u_2))/t_1 <= log(1/rho_CA)/t_1 per lattice step. In physical units this is log(1/rho_CA)/(t_1 a_K) <= (2/(3d)) log(3 C_K/c_K). The target states it as an upper bound only, which is correct.
- The spatial box. W-phys-CA needs the box sides to be multiples of l_star^CA, so that (SD-cyl-CA) applies. That is a hypothesis of the proposition. Statement 6 checks it at the consumer boxes.

The exponent is the same as row 844's. Only the base changes, from (2/7)^8/3 to c_K/(3 C_K).

## Statement 6. (E17-phys-CA) implies (FQ) with a cutoff-independent constant -- HOLDS

- The consumer boxes. CA-I 108 and 410-412 (READ) give T_m = R^4/(2L^m Z^4), so l_star^CA = 2L^(m_star) with m_star = m_T(g_-(g)). The consumer spatial boxes (n_A, n_C, n_D), (n_C, n_D) in {(n_A,n_A), (2n_A,n_A), (2n_A,2n_A)}, have physical sides A or 2A, with A = 2L^m >= l_star^CA. So m >= m_star, and A/l_star^CA = L^(m - m_star) is an integer, and so is 2A/l_star^CA. W-phys-CA therefore applies to all three boxes. n_A = A/a_K = 2L^(m+K) is an integer >= 3. The bare sites sit at L^-K (Z + 1/2)^4 (CA-I 418, READ). Time translation by t_i a_K and reflection through a plane of sites both preserve this lattice, so the tent centre can be put on a plane of sites as row 844 requires. Checked.
- The inequality. W-phys-CA gives sqrt(S_ev(n_A; B)) >= rho_CA^(A/(3d)). With (E17-phys-CA), 8 Q_F <= K_F rho_CA^(A/(3d)) <= K_F sqrt(S_ev(n_A; B)), and Q_F < 1/192 is part of the hypothesis. This is row 844's (FQ) (row 844 1.1, READ: 8 Q_F <= K(a) sqrt(S_ev(a; (a,c,d))), Q_F < 1/192, K(a) <= C_1 a^(p_1)) with K(a) = K_F, p_1 = 0, C_1 = K_F. Checked.
- The rate. rho_CA^(A/(3d)) = exp(-(A/(3d)) log(3 C_K/c_K)) = e^(-Lambda_CA A), with Lambda_CA = log(3 C_K/c_K)/(3d). Checked.
- Cutoff independence. K_F, A, d, theta are fixed by hand. c_K and C_K do not depend on K, g_0, m, d or the position (CA-I 2734-2735). K_0 depends only on d, theta, k_W and s(d), and s(d) does not depend on K (CA-I 2750-2751). So the constant K(a) = K_F and the rate Lambda_CA do not depend on the cutoff, on g_0 or on the lattice sizes. They may depend on g, L, p and theta, which are fixed. Checked.
- Scope. (E17-phys-CA) is a hypothesis, the flux estimate, and the target marks it OPEN. The implication is all that is proved. That is right.

Not checked here (dictionary): the consumer's first-passage data are stated in row 844 as (K, beta), beta in W_K(g), in the outline's terms. The target quantifies over CA's data, g_0 in (0, g_-(g)], K = K(g_0, g) (CA-I 111, 682). That the two sets of data agree, or that the consumer needs only CA's, is not shown in the target and was not checked by me. It changes no inequality.

## Summary

| Statement | Verdict |
|---|---|
| 1. c_K, C_K and the depth floors | HOLDS (name which shape c_K is taken at: theta = 1/300 under CA-I's continuous class, or the discrete shape) |
| 2. K_s^star bounds at the tent separations | HOLDS |
| 3. Carrying the half-error | HOLDS, conditional; marking correction: the quarter-error law at CA-II 142328-142346 is hypothesis (a) of 8.22:cor-transfer-depth-floor, valid below the horizon, not a conclusion |
| 4. rho_CA = c_K/(3 C_K) | HOLDS |
| 5. Exponent 2A/(3d) | HOLDS |
| 6. (E17-phys-CA) => (FQ), K(a) = K_F | HOLDS |

What rests on statements the account itself leaves as hypotheses or does not write: (i) the kernel sandwich, from CA-II 8.1:lem-kernel-bounds under its (h1)-(h3), including the free comparison. The target says CA-II 145220-145222 leaves the continuum-kernel lemma unwritten; I did not read that range. (ii) Hypotheses (a) and (b) of CA-II 8.22:cor-transfer-depth-floor (READ: stated there as "Assume the following two statements"). (iii) The analytic premises of the volume-transfer theorem (source energy, face series, vacuum density, lower stability). (iv) The H-depth tail (CA-II 69049-69069, NOT READ). The rectangular extension is the target's port (target Step 3), built on row 844 Lemma F and the row 848 dictionary. CA-I states the transfer only between cubic tori. I checked its structure and the E_star cancellation, but not the CA-II locators it cites.

Provenance: checked by hand by Claude Opus 5.5 (high effort). The target is by Codex gpt-6-astra. Row 844 is by Claude Opus 5.5, the same provider as this check. For the parts of the target that reuse row 844, this check is not independent in the sense of the working rules.

RESULT: gap-sdcyl-ca-astra (row 865) checked line by line by Claude Opus 5.5 against CA-I 2715-2826, row 844 sections 3-5 and the row 848 check section 13: all six statements HOLD (c_K/C_K and depth-floor reading, tent-separation kernel bounds, additive 1/4+1/4 half-error reserve, rho_CA = c_K/(3C_K), exponent 2A/(3d), (E17-phys-CA) => (FQ) with K(a)=K_F cutoff-independent), with one marking correction (the quarter-error law at CA-II 142328-142346 is hypothesis (a) of 8.22:cor-transfer-depth-floor, valid below the horizon) and one wording request (name the shape at which c_K is taken); everything stays conditional on the account's (h1)-(h3) kernel comparison, the corollary's hypotheses (a)-(b), the volume-transfer premises and the target's rectangular port; no mass gap, and (E17-phys-CA) stays OPEN.
