# Check of rows 1628 and 1629 (VIR-DOWN two-sided tests), row 1630

Checker: Claude Opus 5.5. Sources read in full: listed per item below.

## 0. Reading log

- FINISH.md rows 1628, 1629, 1630 (briefs and RESULT texts), read in full.
- `library/gap-vir-down-twoside-astra62.md` (row 1628, 286 lines) and `library/gap-vir-down-twoside-neon.md` (row 1629, 313 lines), read in full.
- Registry rows VIR-DOWN (L1028) and LEV-FAIL (L1029) of `library/open-registry.md`.
- `library/gap-direction7-fable.md` sections 2.3-3.8 (Theorem TR-down, Corollary B, Remark CH-down, Proposition EQ-down), read in full.
- Row 1618 Theorem 3 (`library/gap-vir-down-neon.md` L196-229) and check 1622 section 3 (`library/gap-vir-down-neon-check-opus.md` L91-105).
- Row 1461 displays (1)-(2) and their proof (`library/gap-crux-direction-astra62.md` L56-95).
- Check 1527 (ii) and its handoff (`library/gap-agy-seed-approaches-neon-check-astra62.md` L45-56); check 1370 L88-108 (aspect table).
- Check 1625 section 3 benchmark (L103); check 1627 sections 1.7-1.8 and RESULT; row 1626 L146-156.
- Lemma ALG and tests (g1)-(g6), row 1553 (`library/gap-mech-direction4-fable.md` L180-196).
- Not re-read: check 1453 in full (I used BND-2 as quoted by both authors and by row 1618 Theorem 3); check 1613 in full (I used its regularity and enlargement as cited in rows 1618, 1626, 1628, 1629); row 1624 in full (I used its (6)/(10), (14), (18), (21) as cited, all checked in check 1625).

Guide run (floating point, not a proof step, not a verification record): one Python process, a few MB, file `g1630/guide.py` in this session's scratchpad (outside the repository). It evaluates the finite examples of both files with a separate implementation of the pair integrals. Results are quoted below where used.

## 1. Item 1: the rate budget (decided first)

### 1.1 What each author proves

- Row 1628 (1)-(2): with HOT certified at one period T at a fixed right endpoint, the integral of kappa must be at least [log(512T/n) - J_o]_+. On row 1624's window w_0 = (3/8) log 512 with the certificate G(n; beta_h) <= 4/21, the required mean is log 512 / w_0 = 8/3 exactly. So zero reduction. HOLDS. This is arithmetic on (1).
- Row 1628 (3) and row 1629 Theorem 1.2(3): start the characteristic at n/34, keep HOT at n, feed the checked aspect-34 consumer. Required mean 8 log 34/(3 log 512) = 1.5075 (GUIDE). Row 1629 proves < 368/243 < 1.515 from 34^9 < 2^46 (checked by integer multiplication: 34^9 = 60716992766464 < 70368744177664). HOLDS in both. Row 1628 is right that this is a different characteristic and a different conclusion (G(n/34; beta_K) <= 4/21, not G(n/512; beta_K)). The aspect-34 handoff is ON FILE and checked (check 1527 (ii) "Handoff", check 1370 L88-108; divisibility 4 * 34 | l).
- Row 1629 Theorem 1.2(1), display (1.8): fix the hot side L_h, put l = L_h b^r with r fixed by (1.8). Then the lattice n_K = L_h b^(K+r) at beta_(K+r) is the calibrated box of side L_h at cutoff K + r. A constant rate kappa_0 with kappa_0 (s r - W(r)) >= log_+(A alpha_h) carries HOT at that box to the seed at K. HOLDS as an implication.
- Row 1628 has the same theorem. Its paragraph "PROVED (fixed depth shifts for the infinitely-often quantifier)" says: given any constant k > 0 choose d with k(s d - U_d) >= log 512 and l = b^d l_h; then a thermal bound of at least k on the cold points suffices, with "a different physical side and a longer interval requiring the bound" as the price. U_d of row 1628 is W(r) of row 1629 (both are row 1618 (3.2)).

So the two files do not disagree. FINISH row 1629's RESULT text ("disagrees in reach with row 1628, which allows no reduction on the original window") compares row 1629's long-window theorem with row 1628's fixed-window statement. Row 1628's file contains the long-window theorem too. The disagreement is in the RESULT summaries, not in the mathematics.

### 1.2 Quantifiers

- r is fixed before K. In (1.8) r depends on kappa_0, A, alpha_h, b, g_0 and the release-table constants C_I, c, Q only. l = L_h b^r is then one fixed side. HOLDS.
- W(r) is uniform in K. Row 1461 (2) holds for K >= K_I and every r in the level interval I; K_I does not depend on the step count. The proof of row 1618 (3.2) applies (2) at K and at K + r, and the table bound |sum_{i=u}^{v-1} a_i - s(v-u)| <= 2c holds for every u < v. I re-read both. So |(beta_(K+r) - beta_K) - s r| <= W(r) for all K >= K_I and all r >= 1, and s r - W(r) -> infinity because W(r) = O(1 + log r). HOLDS.
- A alpha_h stays bounded: alpha_h is the cooling aspect of the box of fixed physical side L_h at cutoff K' = K + r. It is a hypothesis (C2 of row 1610), independent of r and K by assumption. It does not grow with r. HOLDS (as a hypothesis).
- Last crossing for general (A, s_0): row 1629 uses any c_col in (s_0, 1). I re-derived it: if phi(beta) = G(t(beta); beta) exceeded c_col somewhere, take its last point with phi = c_col; on the rest phi <= c_col, so VIR-down applies and phi is non-decreasing, so phi <= phi(beta_h) <= s_0 < c_col, a contradiction. So phi <= c_col throughout, phi is non-decreasing, and phi(beta_K) <= s_0. HOLDS.
- "o(1) rates fail at fixed r" (row 1629, from row 1618 Theorem 3(2), checked in check 1622): HOLDS, conditional on the hot-end premise limsup n m_1(beta_(K+r)) < A log(1/s_0), as check 1622 noted. A schedule with r_K -> infinity would need a K-dependent side l, which the seed forbids. So r fixed is forced.
- Theorem 1.2(2) (kappa = 0 on the weak tail, kappa_1 on the head): the concatenated profile is not continuous. HOLDS AFTER CORRECTION: TR-down's chain-rule proof works for piecewise continuous kappa (phi is continuous with a non-negative derivative off finitely many points), or smooth the junction.

### 1.3 What a larger r costs

(a) In (HOT): nothing. HOT is asked at the fixed side L_h with the fixed aspect alpha_h.

(b) In the hot certificate: nothing. Row 1628 (21) (checked below) is the sharp certificate from (gamma, t_0, N_0); it does not depend on r.

(c) In the window: the cost is real. At the calibrated roots inside the window the lattice n_K at beta_(K+r-i) is the calibrated box of side L_h b^i (i = 0, ..., r). So the window covers the physical sides from L_h to l = L_h b^r. These sides do not depend on K. The band (order-one box coupling) sits at fixed sides. If L_h is a weak box, the window contains the weak part (C3), the band (C4) and an infrared stretch from the band up to l. A larger r adds only infrared sides. (VIR-down) must hold, at rate kappa_0, at the cold points of the characteristic on all of them, uniformly in K. Pointwise this is weaker than at a larger rate (Phi is decreasing in kappa, row 1628 (14)), but the set of points is larger and different.

(d) A necessary condition that neither file states (PROVED here, from Remark CH-down and the last crossing of 1.2). Put alpha_*(beta) := (1/n_K) inf{t >= 1 : G(t; beta) <= s_0}. If HOT holds and (VIR-down) holds at every cold point of the kappa-characteristic, then phi(beta) <= s_0 for every beta in the window (1.2). Since G decreases strictly in t, this gives the running budget

    integral of kappa over [beta_K, beta] >= log_+(A alpha_*(beta))   for EVERY beta in [beta_K, beta_h].   (RB)

Row 1628 (1) and row 1629 (1.3) are the case beta = beta_h only. For a constant rate, (RB) is kappa_0 >= sup over beta in (beta_K, beta_h] of log_+(A alpha_*(beta))/(beta - beta_K). So a small kappa_0 is consistent with the hypothesis only if the cold-threshold aspects alpha_*(beta) of the band boxes and the infrared boxes obey (RB). Neither file proves anything about alpha_*(beta) on the band. (RB) is a consequence of the hypothesis, so it does not falsify row 1629's implication. It says what the implication silently requires of the Wilson spectrum.

(e) Is (RB) plausible for small kappa_0 and large r? GUIDE (scaling picture, belief I33 and a dilute glueball gas, not a proof): the cold aspect alpha_c(L) of a box of side L decreases as L grows (about g(L)^(-2/3)/c_0 for a weak box, about 3 log(ML)/(ML) for a large box). The constant-kappa_0 characteristic has aspect alpha_h (L_h/L)^(kappa_0/kappa_s), kappa_s = 3 pi^2/11, which also decreases in L but only as a small power. Near the seed end (RB) needs kappa_0 r log b >~ log(A log(M l)); this is what (1.8) gives for large r. So in that picture (RB) holds once r is large, and the band is crossed at an aspect close to alpha_h, not close to 1/A. Near a weak hot box with a tight alpha_h, (RB) needs kappa_0 below the weak level rate (about 1/(3 beta_box) by the toron scaling; row 1629 section 1.4 says about g^2/3; the constant differs, the point is the same). So the original constant 8/3 is inconsistent with a tight weak hot box, and a small kappa_0 removes that conflict. Row 1629 section 1.4 point 2 says this; it is ARGUED, and I agree with it as ARGUED.

### 1.4 Verdict on item 1, and the exact requirement

Both authors are right, in different senses.
- Fixed window w_0 with the aspect-1 certificate: required mean exactly 8/3; zero reduction (row 1628 (2)).
- Same window, aspect-34 consumer: required mean 8 log 34/(3 log 512), about 1.51, on a different characteristic (both).
- Fixed r chosen first, l = L_h b^r: every constant kappa_0 > 0 suffices as an implication (row 1629 (1.8); row 1628's fixed-depth-shift paragraph). r is fixed before K, W(r) is uniform in K, and A alpha_h does not depend on r.

The exact requirement on the profile is:
- sufficient: HOT at (L_h, alpha_h, s_0) at cutoff K + r, an integral of kappa over [beta_K, beta_(K+r)] at least log_+(A alpha_h) (for a constant: kappa_0 (s r - W(r)) >= log_+(A alpha_h)), and (VIR-down) at the cold points G <= c_col of that characteristic;
- necessary for the hypothesis to hold at all: (RB) at every beta of the window.
The margin "3 pi^2/11 - kappa_0, up to 100%" of row 1629 (1.9) is bookkeeping. It is not a margin of any proved inequality. The real gain from a small kappa_0 is in the tests: their tolerance for hidden thermal energy grows (row 1628 (23) with kappa small; section 3 below).

Overclaim, row 1629 section 3 item 2: "the live threat ... is eliminated by combining Part 1 and Part 2". Part 1 moves the characteristic and lengthens the window; Part 2 removes some phantom costs. Neither bounds the hidden or the observed response on the band. The word should be "relaxed, conditionally". The section is labelled ARGUED / GUIDE, so this is a wording correction.

## 2. Item 2: the two-sided tests, line by line

### 2.1 Row 1628

- (1), (2), (3): see 1.1. HOLD. The scaling-margin arithmetic (9 pi^2 - 88)/33 > 0 from 223/71 < pi: (223/71)^2 = 49729/5041 > 88/9. HOLDS. The two-state equality example for (1) HOLDS.
- Fixed depth shifts: if w_K <= s d - eps for all K >= K_0, summing along K_0 + j d gives limsup beta_K/K <= s - eps/d, against BND-2. HOLDS.
- Inclusions C = PEP <= P^2 <= P^(2 theta) <= I: HOLD (E <= I; spectrum of P in (0, 1]).
- (5): expand ||D^(1/2) d_j||^2; the one-point terms die by the zero marginals; the cross term is -2 Tr(P^j D P^j P^k S P^k) = -2 Tr(D R) since j + k = v - 1. HOLDS. Note: j + k = v - 1 for every buffer, so the buffer drops out; this is why row 1626 (1) is buffer-independent.
- (6): -2 Tr(P^(2 theta) R) = -2 Tr(P^(t-2) S) and row 1624 (10). HOLDS (ON FILE, check 1625 1.2).
- (7): Douglas factorization Y = H^(1/2) J H^(1/2), 0 <= J <= I on the range closure, then the positive spectral projection. HOLDS (standard).
- (4) implies (VIR-down): -2 Tr(P^(2 theta) R) = V - 2 Tr(H_theta R) >= V - 2 Tr B(H_theta)_+ by (7) with Y = H_theta; H_theta <= H_0 nests the suprema; e^m - 1 >= m. HOLDS.
- (8): D_j - L_(j+1) = ||H_0^(1/2) d_j||^2, so M_15 = V - Tr N_-. The operator form of (5) gives N_+ - N_- = -2 B(H_0), so 2B(H_0) <= N_- and 2 Tr B(H_0)_+ <= Tr N_-. HOLDS.
- (9): gain = Tr N_- - Tr(N_- - N_+)_+ = (1/2)[Tr(N_- + N_+) - ||N_- - N_+||_1]. HOLDS. Strict positivity: H_0 maps the excited space into itself and is injective there (||PQ|| = r_1 < 1); P^j H_0^(1/2) f is analytic and non-constant, so its equal-value pairs are null; N_+ and N_- are then positive definite on the excited space provided mu_k is not zero. HOLDS given mu_k != 0 (ON FILE, row 1624 (14)). No size is claimed. Correct.
- (10): the series bounds 0 <= h_p - h_inf <= r(1-r)^(p+1)/(p+1) and h_(p-1) - h_p = r(1-r)^(p+1)/(p(p+1)) HOLD (tail of -log r = sum (1-r)^a/a, bounded by (1-r)^(p+1)/(r(p+1)) times r^2). Monotonicity of Phi_p in p, sufficiency via C + Y = P^(2 theta), and the uniform error 4 kappa G(2v-1)/(p+1): HOLD.
- (11): Tr(P^(t-2) h_inf(P)) = sum r^t m. HOLDS.
- (12): -2 Tr(C(R_p - R)) = 4 kappa Tr(C P^(2v-2)(h_0 - h_p)(P)), because P^(v-1) and h(P) commute. S_p <= s_n Q needs S^0 <= 24 n^3 Q (row 1624 (21), ON FILE) and 0 <= h_p <= 1/4. Then sup over Y <= H_theta of Tr(Y R_p) <= s_n Tr(H_theta P^(2v-2) Q) = s_n [G(t-2) - Tr(E P^(2v) Q)]. HOLDS. The factor s_n ~ 24 n^3 makes (12) useless at late cutoffs unless the hidden heat trace is below V/(48 n^3); row 1628 says so.
- (13): subtract (10) at p = infinity from (11). HOLDS. It is an identity; row 1628 says so.
- (14): each affine branch has kappa-slope -4 Tr((C+Y) P^(2v-2) h_inf(P)) in [-4 W_t, -4 W_E]; minimizers exist by (7). HOLDS.
- First cold family (15), families A and B. Positivity of entries needs r <= s; in A this is c > 8/3. G <= (N-1)/(8(N-1)) = 1/8 on the window. P_K >= (8/9)^2 = 64/81. The mark S on O and F. In A: S <= 0, B(H)_+ = 0, V > 0, so (4) and (10) pass. At x = 0, M_15 = (D/2) z^(2j)[4z^2 - 2(N-2)] < 0. I re-derived each line (d_j = N z^j (1_x1 - 1_x2); L_(j+1) = 4 z^(2j+2) on opposite labels; D_j = 2N z^(2j) on distinct equal-label states with conditional probability 1 - 2/N). HOLDS.
- Family B: all observed data agree with A (F is supported on equal labels, where every L_s vanishes); R_B = c(1-z)/((N-1) z (-log z)) -> c/(N-1); R_B < 2c/(N-1) < 8/3. HOLDS. So no test that reads only these coarse data certifies more than about c/(N-1). This is the N-level form of check 1625 section 3 (one hidden zero-slope level at the cold scale) and of row 1629 Corollary 2.2(2)-(3).
- (16): T_L^* (T_L T_L^*)^+ T_L is the projection on ran T_L^*. HOLDS. C <= C_L <= C_(L+1) <= P^(2 theta): HOLDS (P^(1-theta) E P^(1-theta) is a positive contraction with range in ran J_0). The fractional-lag majorant is a sketch; it is not used later. HOLDS in outline.
- (17)-(18): the polynomial [1 - (x - r)^2]^q equals 1 at r and is at most (1 - delta_r^2)^q on the rest of spec P in [0, 1]; it has degree 2q, so its value on P^(1-theta) E g lies in ran J_(2q). F_r g = ||Ef|| f for g = Ef/||Ef||. HOLD.
- Limit of the finite-delay margins: J commutes with P; strong convergence of C_L, H_L and their square roots; trace-norm convergence on trace-class R; (7) is 1-Lipschitz in trace norm. HOLDS.
- (19): compression F_r S F_r = -2 r^2 (b_r - kappa m) gives F_r A F_r = -2 r^t (b_r - kappa m). Restricting the competitors to block-diagonal contractions on the D_r still contains Y = D, so the bound stays below the true response, and it is sharper. HOLDS.
- (20): Tr(J_r(b - kappa m)) + Tr_D(b^h - kappa m) = Tr F_r (b - kappa m), and -(kappa m - b)_+ = (b - kappa m) - (b - kappa m)_+. HOLDS. Standing: (20) is the exact form of check 1627 section 1.1's corollary ("an exactly hidden level slower than kappa is charged its full deficit, and a faster one gives no credit"), with "hidden" now meaning outside the delay closure J.
- (21): with x_i = e^(-t_0 m_i) in (0, d_h] and sum x_i <= N_0, the maximum of sum x_i^p (p >= 1) is D_h d_h^p + e_h^p by the mass-transfer argument. The Markov witness eta I + (alpha - eta) E_0 + (1 - alpha) Pi has eigenvalues 1, alpha (D_h times), eta; its entries are positive since eta < alpha < 1. For p < 1 the bound is unbounded. HOLDS.
- (22): b_r = 0 on every photon eigenspace (the compression of a commutator with the transfer vanishes on an eigenspace, so this is independent of the rescaling convention); the observation and its delay closure lie in the zero-charge sector by the flat-shift invariance (row 1626 (12)-(13), check 1627 1.8); hidden sectors only subtract. So B(kappa) <= -kappa sum over zero-charge photons of m e^(-tm) < 0. HOLDS, and it is convention-free. The finite-delay tests lie below (19), so they fail too. HOLDS.
- Spectator paragraph: after the last crossing of 1/2 the mean value theorem gives a cold point with G_beta/t - kappa W_t <= -(1/2 - 4/21)/(w t) = -13/(42 w t), and B <= (R - kappa) W_t. HOLDS. Weak 5D: not claimed. Correct.
- Mode interchange: the observed sign now has a beta-independent multiplier 1/2 and its excited space is invariant under every delay, so the observed term of (19) is -kappa 2^(-t) log 2 < 0. HOLDS.
- (23): the first term of (19) is (1 - h) W_t (c_o - kappa) because sum r^t m Tr J_r = (1 - h) W_t; the hidden term is at most h W_t (kappa - rho)_+. HOLDS. The tolerances 1 - 88/(9 pi^2) at 8/3 and 1 - 88 log 34/(9 pi^2 log 512) at rate (3): HOLD (arithmetic).
- Wilson substitute rho = -9 n^3 t/log 2: each electric summand of row 1617's formula is >= -1 on 3 n^3 links, the spatial action is <= 6 n^3, D_Omega <= 0, and t m >= log 2 at cold points. HOLDS given row 1617 (ON FILE).

Row 1628 verdict: every listed item HOLDS. No line fails.

### 2.2 Row 1629

- Theorem 1.1, (1.3)-(1.6): HOLDS (1.2 above). "If and only if" is correct for (HOT); it is not the requirement on the profile, which is (RB).
- Theorem 1.2: (1) HOLDS; (2) HOLDS AFTER CORRECTION (continuity, 1.2); (3) HOLDS, including (1.10) (log(21/4) > 1.658; 60 log 2 < 42; log(848/42) > 3). The margin (1.9) is bookkeeping (1.4).
- Theorem 2.1. Step 1: the Lyapunov operator gives -(P A'_T + A'_T P) = S_T; the affine family is positive, symmetric, keeps pi, and has trace derivative (c/4) integral of D_(*,k) dT (I checked Tr(P^(t-1) A'_T) = -(1/2) sum r_i^(t-2) <f_i, S_T f_i> and the zero-marginal identity). Density of finite-rank kernels in Z_0 and L^1-continuity: HOLD. Step 2: the four-neighbourhood measure gives T(mu) > 0 and T(-mu) > 0 while the integral of D tends to -2[p(x0,y0) + p(x1,y1) - p(x0,y1) - p(x1,y0)] != 0. HOLDS. Step 3: separation in R^2; lambda > 0 from mu = f_1 (x) f_1. HOLDS. Step 4: the cycle inequality from the zero-marginal cyclic measure, then shortest-path potentials. HOLDS AFTER CORRECTION: the displayed d_L(x) := inf({0} union ...) must read "0 only for x = x_0"; with the literal text, d_L <= 0 everywhere and g_+(x, y) >= d_R(y) - d_L(x) is not justified. With the correction the averaging gives g_+ >= f (+) f and g_- >= -f (+) f, which is (2.4).
  Scope: "sound" means sound for every smooth positive Markov family with fixed pi through P. The theorem says nothing about tests that use Wilson-specific a priori bounds (such as row 1628 (12)) or that are not pointwise Jordan weights (row 1628 (4), (10), (19)).
- Corollary 2.2(1): at x = y, (2.4) gives f <= 0, hence lambda W_- >= D_(*,k). HOLDS. This is the answer to "no test of this shape can do better": inside the class of universally sound pointwise Jordan tests with W_+(x, x) >= 0, the negative weight cannot be cut below the full D_(*,k), and with lambda = 1 and 0 <= W_+ <= L_(j+1) the gain over (15) is at most the rounding slack, zero at even t. HOLDS.
- Corollary 2.2(2), late Wilson boxes: gauge fixing on a tree leaves 2n^3 + 1 links, 6n^3 dimensions after the global SO(3); a level set of the |C| cell probabilities has positive dimension; distinct orbits are separated by some f_i. HOLDS. Four-state chain: entries positive (g(m) = 1 + e^(-m) - 2e^(-0.6m) increasing from 0); S_k > 0 on all cross-cell pairs for kappa <= 3r; at m = 1/4, t = 20: G = 0.106 and R = 0.304 (GUIDE values agree with the printed bounds; the bounds themselves are elementary). HOLDS.
- Corollary 2.2(3): a unit g in V_L with E P^a g = 0 for a <= M exists by dimension count; adding c|g><g| to S leaves every E P^a S P^b E unchanged and lowers G_beta/t by (c/2)<g, P^(t-2) g>. HOLDS. Scope: the anchor P is unchanged and only the derivative moves; a test that also uses an a priori bound on S on the unobserved space (row 1628 (12)) is outside the no-go. Row 1629 states the no-go for observed products only; correct.
- Corollary 2.2(4): D_s - 2u_s(x) - 2u_s(y) = L_s - ||R_s^(1/2)(e_x + e_y)||^2, M_+ - M_- = 2 B_s. HOLDS.
- Theorem 2.3(1), test (2.12): D_s - L_s = C_s(x,x) + C_s(y,y) - 2 C_s(x,y); the potential f = C_s(x, x) is bounded; the two pointwise bounds and 0 <= D_(*,k) - D_s <= R_t hold. Sound. HOLDS. Note W_+(x, x) = -2 C_s(x, x) <= 0, so (2.12) escapes Corollary 2.2(1) exactly as it must.
- Test (2.13): the zero marginals of mu^cell kill the diagonal terms, so the integral of D_(*,k) against mu^cell equals sum mu(C x C') L~_(*)(C, C'); then L~_s <= L~_(*) <= L~_j. HOLDS.
- Theorem 2.3(2), finite periods: an outline resting on row 1624 (22) with an unstated absolute constant K_0. HOLDS in outline only; not a complete proof.
- Theorem 2.4(1): E = 91/20, V = 1/20, 2 Tr B_+ = 1/2, M_sym = M_decsym = 1/20 (GUIDE agrees). HOLDS AFTER CORRECTION: row 1629 evaluates (15) with L_j on the positive side. Row 1624's (15), as row 1629 itself states it in 2.1, uses L_(j+1). The correct value is -761/160, not -107/40, and the row 1626 bound with V = integral of L_(j+1) is 1/80 - 1/2 = -39/80, not -9/20 (GUIDE: -4.75625 and -0.4875). Both are negative, so the separation stands. Also "fails for every buffer k": at t = 4 only k = 0 is admissible.
- Theorem 2.4(2): C_j = r^(2j)(1 - eta) f_1 (x) f_1 and S_k = c_1 r^(2k) f_1 (x) f_1 have opposite signs, so M_sym = -2 c_1 eta r^(t-2) > 0. HOLDS. Correction for (15): with L_(j+1) = r^2 eta D_j, (15) = (-c_1) r^(t-2)[r^2 eta (2 + K) - K], so it fails for eta < K/(r^2 (2 + K)), a larger range; the conclusion strengthens. The Gaussian value K = 4/pi - 1 is right (E[X^3 Y; XY > 0] = 2/pi, E[X^2 Y^2; XY > 0] = 1/2), but the Gaussian mode is a guide, not a Wilson box. Eight-state family: HOLDS AFTER CORRECTION: K = p(1-p) a b (a - b)^2 = (1 - 2 sqrt(p(1-p)))/(4 sqrt(p(1-p))), not (1 - 2p)^2/(4 sqrt(p(1-p))). It still tends to infinity as p -> 0, so eta_crit -> 1 stands.
- Theorem 2.4(3): pair classes, masses and kernels re-derived; M_sym = (36 - 32M/(M+1)) alpha, M_decsym = 36 alpha (GUIDE at M = 1, 2, 3, r = 0.7: 20, 14.67, 12 and 36, 36, 36). HOLDS. Correction for (15): with L_(j+1) it is (36 r^2 - 32 M) alpha (GUIDE: -14.36 alpha at M = 1), so (15) fails already at M = 1 when r^2 < 8/9.
- Theorem 2.4(4): GUIDE at r = 399/400, t = 400, k = 50: M_decsym equals the exact contrast E at kappa = 1.1, 1.2, 1.4, 1.49, 1.5 and is below it at 0.9; M_sym is positive up to between 1.49 and 1.5; (15) is negative at 1.2 (-3.0e-4, as in check 1625). The zero of E sits just below the thermal rate 1.5 because e^m - 1 > m. HOLDS (the hand proof of the sign pattern I checked at the level of the signs of S_k^perp and C_j; the numbers are guides).
- Theorem 2.5(1): (2.16) is trivial. (2.17): M_decsym <= V_s - 2 Tr(E(P^(2s) - P^s E P^s) E * E S_k E) <= V_s <= 0 when E = JEJ, [J, P] = 0, JSJ >= 0. HOLDS. Free photon: M <= E < 0 for kappa > 0. HOLDS. Compact Gaussian U(1), kappa >= 1/beta: M <= E < 0 (row 1624 (18)). HOLDS.
  Contractible loops at 0 < kappa < 1/beta, (2.18): HOLDS ONLY IN THE RESCALED COMPARISON COORDINATES. The step J_ph S J_ph = 2 kappa J_ph (P - P^2) J_ph needs S^0 = 0 on the photon sector as an operator. Under a beta-dependent rescaling, S^0 changes by a commutator with A^2. A commutator has zero diagonal blocks on each eigenspace, but not zero off-diagonal blocks, and V_s reads off-diagonal elements through E. Row 1626 (12)-(13) and row 1628 (22) use eigenspace-diagonal quantities only, so they are convention-free (check 1627 1.7 made this point). Row 1629's (2.12)-(2.13) are not. To close: either fix the comparison convention for all models, or bound M_sym and M_decsym by an eigenspace-diagonal quantity. The kappa = 0 Mehler argument is in the same coordinates, and its photon kernel exponent should be 2k + 1, not h; positivity is unaffected.
- Theorem 2.5(2): the reading at kappa >= 1/beta (the target fails) HOLDS. The claim that Q = 0 excitations of strong-coupling 4D Wilson U(1) carry rate about 4/(beta log(2/beta)) is not proved in the file. A strong-coupling mass m about -4 log(beta/2) gives -m'/m = 1/(beta log(2/beta)); either way it is ARGUED, not PROVED. So "passes (g3)" is ARGUED.
- Theorem 2.5(3), mode exchange: E projects on the functions of the observed sign, commutes with P, E S E = 2 kappa s(1-s)|f_1><f_1| >= 0, so both tests are <= V_s < 0 for kappa > 0. HOLDS (notation: s is both a multiplier and a step).
- No-go for the observed products E P^a S P^b E: HOLDS (Corollary 2.2(3) above). Its content is the same as row 1628's families A and B.

Row 1629 verdict: no line FAILS. Five corrections: Theorem 1.2(2) continuity; the d_L definition in Theorem 2.1 Step 4; the (15) values in Theorem 2.4(1)-(3) (L_j used for L_(j+1); signs stand); the eight-state K formula; (2.18) is proved only in the rescaled comparison coordinates. Theorem 2.3(2) is an outline. One wording overclaim (section 3, "eliminated").

## 3. Item 3: selectivity, and the band

### 3.1 Do the photon and compact Gaussian U(1) failures read the law?

- Free photon, every kappa > 0, both files: the target itself fails (d/dbeta G = 0 after rescaling). The failure reads the law (a beta-independent spectrum). It is inherited from (VIR-down); it says nothing about the test.
- Compact Gaussian U(1), kappa >= 1/beta, both files: the target fails (R < 1/beta, row 1618 Theorem 2). It reads the rotor dispersion e_Q = |Q|^2/(2 beta n), a property of the law. At a fixed kappa_0 > 0 this covers every late cutoff (beta_K > 1/kappa_0). This is the o(1) mechanism of row 1618 Theorem 3(2). The selective content is in the target: on the long window the SU(2) weak rate is set by the box coupling of the fixed side L_h, not by the bare beta. That SU(2) half is GUIDE (toron scaling); it is not proved.
- Compact Gaussian U(1), 0 < kappa < 1/beta, contractible flowed loops: here the TEST fails where the target holds (R > 9/(10 beta)). It is a failure of the observation. It reads two things: flat-shift invariance of contractible loops (a symmetry) and zero slopes in the zero-charge photon sector (the law). Row 1628 (22) proves it convention-free; row 1629 (2.18) proves it in the rescaled coordinates only (2.2).
- (g3), the gapped twin (strong-coupling 4D U(1)): the symmetry line still fires (contractible loops stay in the zero-charge sector), but the slope line should not, because zero-charge levels depend on beta at strong coupling. Neither file proves a slope there. So "reads the law, passes (g3)" is ARGUED in both files. I agree with it as ARGUED.
- (g4), the product with a light neutral spectator: both tests fail, as Lemma ALG requires of any test that implies the seed. Row 1628 gives a size (-13/(42 w t)). HOLDS.
- (g2), weak 5D SU(2): open in both files.

One warning for the lead, ARGUED. The U(1) observation failure is the same mechanism that threatens SU(2) on the band: thermal weight in levels that the flowed loops do not see and whose slope is small (momentum levels have rate kappa_s M^2/E^2; row 1610 3.3 warning). Passing (g1) this way is not evidence of a positive SU(2) margin.

### 3.2 A positive margin on the cold calibrated SU(2) band?

Undecided, in both files, and I agree. No estimate on file bounds the observed response or the hidden adverse response of a calibrated Wilson box at the required cold points. Check 1627's partial-hiding theorem (||E f_i|| < 1) has no uniform size. Row 1628's families A and B meet the same calibration labels, the same HOT threshold and the same observed data and have opposite signs; so the sign is not decided by anything the tests read without a Wilson-specific estimate.

### 3.3 The exact estimate that is left

Use row 1628 (19), (23), the strongest test on file, with row 1629's long window (kappa_0 small, r fixed by (1.8)). At every cold point (G <= c_col) of the kappa_0-characteristic on [beta_K, beta_(K+r)], for the infinitely many K with K + r in E', uniformly in K:

    (1 - h) (c_o - kappa_0) > h (kappa_0 - rho)_+,

where h is the exactly invisible thermal-energy fraction for the delay closure J of the flowed loops, c_o is the observed rate sum_r r^t Tr(J_r b_r)/((1-h) W_t), and rho m is a lower bound for the hidden blocks b_r^h. If every hidden block is non-negative (rho = 0), this is (1 - h) c_o > kappa_0: the observed part of the thermal response must exceed kappa_0 W_t. So two estimates are left:
- (E1) a lower bound sum_r r^t Tr(J_r b_r) >= (kappa_0 + eps) W_t on the band, the weak part and the infrared stretch;
- (E2) an upper bound on the hidden adverse trace sum_r r^t Tr_(D_r)((kappa_0 m - b_r^h)_+), for instance rho >= 0 (no hidden level rises). On file is only rho >= -9 n^3 t/log 2 (row 1628, from row 1617), which is useless.
And the profile must obey (RB) of 1.3(d). For row 1629's (2.12) the analogue is a lower bound on V_s against an upper bound on 2 integral[(C_s)_+ d mu^+ + (C_s)_- d mu^-] + integral R_t d mu^-; it is a pointwise version of the same two estimates.

A small kappa_0 helps (E1) and (E2) directly: at rate 8/3 with c_o = c and rho = 0 the tolerance is h < 1 - 88/(9 pi^2), about 0.9%; at rate kappa_0 it is h < 1 - kappa_0/c. This is the real gain of Part 1. It is conditional on rho >= 0 and on (RB).

## 4. Item 4: new and on file; agreement

| Statement | Standing |
|---|---|
| Endpoint budget, row 1628 (1)-(2), row 1629 (1.3)-(1.6) | ON FILE in substance: Corollary B (row 1610), row 1618 Theorem 3(1)-(2), check 1613, check 1622. The T_* form and general (A, s_0) are bookkeeping. |
| Aspect-34 rate 8 log 34/(3 log 512) | New arithmetic on ON FILE parts (rows 1368, 1370, 1527 (ii), TR-down). Both authors. |
| Long window, any kappa_0 > 0 | New combination of ON FILE parts (TR-down, row 1618 (3.2), row 1461 (2)). Both authors (row 1628 "fixed depth shifts"; row 1629 (1.8)). |
| Running budget (RB) | New here (one line from Remark CH-down). |
| Row 1628 (21), sharp two-number certificate | New. |
| Row 1628 (4), (8) | (8) is row 1626 (1); using its right side as a passing test is new and immediate from (7). |
| Row 1628 (9)-(14), (16)-(18) | New. |
| Row 1628 (19)-(20) | New as a test; (20) is the exact form of check 1627 1.1's corollary, with J the delay closure. |
| Row 1628 families A, B; row 1629 Corollary 2.2(2), (3) | New examples; one mechanism, already in check 1625 section 3 (one hidden zero-slope cold level). |
| Row 1629 Theorem 2.1, Corollary 2.2(1) | New: the potential characterization and the no-go for universally sound pointwise Jordan tests with W_+(x,x) >= 0. |
| Row 1629 (2.12), (2.13), Theorem 2.4 | New tests and separations. |
| (22) and (2.17)-(2.18) | Mechanism ON FILE (row 1626 (12)-(13), check 1627 1.8); new forms. |

Where the two authors agree: the rate budget (same theorem, same value at aspect 34); an observed-only negative charge is unsound (families A, B against Corollary 2.2(2)); tests that read only observed data are capped by the hidden share (families A, B against Corollary 2.2(3)); both tests fail for the photon and, for contractible loops, for compact Gaussian U(1); the mode exchange shows both are strictly stronger than (VIR-down); the band is undecided. In each case both authors combine the same on-file pieces by the same route. Their agreement is two readings of one route, not an independent check. My check is a third reading by hand of the same route; the only different data path is the floating-point guide of the finite examples (section 0), which is not a proof.

What moved: nothing on the critical path. (VIR-down) on the band, (HOT), (PUR-io) and the gap stay open. The registry row VIR-DOWN could note: "rows 1628-1629 (check 1630): on a fixed long window [beta_K, beta_(K+r)] with l = L_h b^r any constant rate kappa_0 > 0 suffices as an implication, subject to the running budget (RB); sharper two-sided tests on file (row 1628 (19), row 1629 (2.12)-(2.13)); band undecided; the estimates left are (E1), (E2) of check 1630 3.3." I have not edited the registry.

## RESULT

Rate budget: both are right. Fixed window w_0, aspect-1 certificate: mean exactly 8/3, zero reduction (row 1628 (2)).
Aspect-34 handoff on that window: 8 log 34/(3 log 512), about 1.51, on a different characteristic (both authors).
r fixed first, l = L_h b^r: every constant kappa_0 > 0 suffices as an implication (row 1629 (1.8); row 1628 "fixed depth shifts").
FINISH's "disagrees in reach" is a summary artefact. W(r) is uniform in K; A alpha_h does not depend on r.
Cost of larger r: none in HOT or its certificate; (VIR-down) must hold on all sides L_h..L_h b^r, a longer infrared stretch.
Exact requirement: HOT, integral of kappa >= log_+(A alpha_h), (VIR-down) at cold points; necessary (new, from CH-down):
the running budget integral_[beta_K,beta] kappa >= log_+(A alpha_*(beta)) at every beta. "Margin up to 100%" is bookkeeping;
the real gain is a hidden-energy tolerance h < 1 - kappa_0/c, if no hidden level rises (unproved).
Row 1628: (1)-(23), families A and B, (21), (22): all HOLD; no line fails.
Row 1629: Thms 1.1-1.2, 2.1, 2.3(1), Cor 2.2, (2.12), (2.13), the observed-product no-go HOLD, some after small fixes
(continuity in 1.2(2); d_L in 2.1; Thm 2.4 evaluates (15) with L_j, not L_(j+1), signs stand; 8-state K formula).
2.3(2) is an outline; (2.18) holds only in rescaled coordinates; "passes (g3)" is ARGUED; "eliminated" (section 3) overclaims.
Selectivity: photon and U(1) failures at kappa >= 1/beta come from the target; contractible loops fail by observation (ARGUED law).
Band sign undecided in both; left: estimates (E1), (E2) of section 3.3. Overall: sound tools, correct budget, no gap input moves.
