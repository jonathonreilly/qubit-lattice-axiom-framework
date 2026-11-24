lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T05:55Z

# Check of rows 1489 and 1490 (gap-k2-pin-interface-check-opus, row 1491)

Started 2026-11-24T17:55Z (date -u), Mac mini worker 2, Claude Opus 5.5 high, pinned at e52329569.
Cross-provider check of two gpt-6.2-astra max outputs, line by line.

## Plan

- (A) library/gap-k2-interface-decide-astra62.md (row 1489): private-link regularization;
  lower bound 529/2048 from the single-crossing-link law; exclusion of partition-function
  trials outside (3/10, 2^15); explicit polynomial trial with positive-row sum in (6/25, 97/100);
  bound on the omitted probe space; cutoff at error 1/1024; check the four Lean theorems state
  what the text uses.
- (B) library/gap-k2-nonlinear-pin-astra62.md (row 1490): full stationary equation; uniqueness of
  the Cartan stripe minimum for |t| <= arcsin(1/4); Hessian lower bound 1/108900 and volume
  independence; minimum 8 + a - sqrt(64 + a^2 + 16 a cos t); cancellation of 19 h^4/(729 x).
- Verdict for each: HOLDS / HOLDS AFTER CORRECTION / FAILS at first wrong line.

Credit: Balaban, Kotecky-Preiss, Sussman-Alpoge (with Claude and Codex), gpt-6.2-astra (rows 1489-1490).

## Repo search

The two rows checked here are the only treatments of these objects. `grep` of `library/open-core.md` and the FINISH rows for "interface-decide", "nonlinear-pin", "529/2048", "108900" and "Cartan stripe" finds only rows 1489-1493 and the two notes under check. This file is a check, not a new statement, so rule 0a has nothing to stop. Inputs read: row 1485 (`gap-k2-wilson-interface-astra62.md`) (1), (2), (6)-(13); row 1348 (`gap-blockstep3-astra62.md`) (13).

## (A) Row 1489, `gap-k2-interface-decide-astra62.md`: verdict HOLDS

Provenance: Claude Opus 5.5, high effort, commit e52329569, one reading by another provider (the note is gpt-6.2-astra max). Not an audit. Every step was redone by hand. No numeric replay was run: `memory_pressure` showed 38 percent free at 2026-11-24 ~18:30Z, below the 50 percent bar, so the tight rational inequalities were recomputed by hand (Step A9). The Lean replay of row 1489 (lead, rc 0) is the kernel check of record. First failing step: none. Three wording notes below (N1-N3) change no claim.

**A1. Private-link regularization. HOLDS.** The words in 1485 (1) are q(a^-1 v b v^-1) = a_0 b_0 + **a**.R(v)**b**. The span of {1, R_kl(v)} is the 10-dimensional space of even quadratics on S^3. So the coordinate change to (s, M) = (1/12) sum_e V(a_e, b_e) is linear and invertible. Two perpendicular faces of {0,1}^4 share one square (4 edges). Opposite faces share none. The 8 private edges give 8 pairs (A_e, D_e) of links that no other read uses. Under product Haar conditioned on all other links, these pairs are independent Haar. With the crossings fixed, b_e = r_s D_e r_t^-1 is Haar. Checked.

**A2. Support is K = {|s| + ||M||_* <= 1}. HOLDS.** One increment: |a_0 b_0| + |**a**||**b**| <= 1 by Cauchy-Schwarz in R^2. Converse: cos a cos g = s, sin a sin g = r gives s + r = cos(a - g), s - r = cos(a + g). Then a in [0, pi/2] exactly when arccos(s - r) + arccos(s + r) <= pi, that is s >= 0. The four sign vectors (+++), (+--), (-+-), (--+) have mean outer product I (off-diagonal sums are 1 - 1 - 1 + 1 = 0). Each block U sqrt(L) sigma sigma^t sqrt(L) V^t has nuclear norm tr L. Three copies give the 12 terms. The 12 central and 12 neighbour links of one face are distinct links, so all 12 pairs can be prescribed together. Checked.

**A3. Exclusion of the (12) trials outside (3/10, 2^15). HOLDS.**
- A_t = E_0 exp(t beta S), with E_0 = isolated neighbour law x Haar crossings. Then F_t = A_t/A_1 = K_i B_i(t) by 1485 (12). The cut traces have mean 0, variance 1/4 and covariance 0: condition on the shared endpoint. The bipartite sign flip gives A_t = A_-t. Jensen applies to the convex series cosh(beta sqrt y) = sum beta^2k y^k/(2k)!, so A_1 >= cosh(beta sqrt 3). Also 3 beta^2 = 15.87 > 63/4, and the k <= 4 partial sum at y = 63/4 is 26.16 > 25.
- Quotient bound: numerator/Z^2 = |Cov(F_t(X_i), F_t(X_j))| <= Var F_t. Denominator/Z^2 = E F_{2t-1} - (E F_t)^2. If F_t^2 <= k F_{2t-1} pointwise with k <= 1, then (kD - m^2)/(D - m^2) <= k. Also A_t^2 <= A_1 A_{2t-1} (Cauchy-Schwarz at t beta = (beta + (2t-1) beta)/2). Checked.
- t <= 0: A_v^2 <= A_{2v} A_0 and A_{2v+1}/A_{2v} >= A_1/A_0 (secant slopes of a convex function). The ratio is <= A_1^-2. For 0 <= t <= 1/6: A_t <= A_1^t and A >= 1 (even and convex, minimum 1 at 0). The ratio is <= A_1^{2t-1} <= A_1^{-2/3}. Checked.
- Fourth moment E_u S^4 = 105/4 + (3/8) sum_sq q(A_sq) q(D_sq), redone: single edges 12 E x^4 = 12/8; pairs 6 C(12,2)/16 = 99/4; even 4-edge subgraphs of the 3-cube are its 6 squares; the cycle integral is 4^-4 tr(M_4 M_3 M_2 M_1) since E uu^t = I/4; tr(x -> P x Q) = 4 Re P Re Q; ordering multiplicity 24. Total 24 * 4/256 = 3/8. Checked.
- |E q(D_sq)| < 5/6: the neighbour link lies in exactly 3 of the box's plaquettes (each link of {0,1}^4 has one plaquette per transverse direction), field t <= 3 beta = 6.9. The axial second moment is 1 - 3 r_1/t, from integrating d/dx[e^{tx}(1 - x^2)^{3/2}]. The continued fraction t/r_1 < 4 + x/(6 + x/(8 + x/10)) is redone from I_{k-1} - I_{k+1} = (2k/t) I_k and I_5/I_4 < t/10. That fraction equals x(80 + x)/(480 + 16x), which is < 5 iff x^2 < 2400. So E c^2 < 2/3 and |E c| < sqrt(2/3) < 5/6. Then E_0 S^4 >= 105/4 - (3/8) 6 (5/6) = 195/8. Moment log-convexity gives m_k >= 3 (65/8)^{k-1}, and A_1 > 130 (replayed, A9). Checked.
- t <= 3/10: ratio <= A_1^{-2/5} < 130^{-2/5} < 1/7 (16900 > 16807). t <= 0: < 1/16900. Checked.
- Large t: with crossings absorbed by neighbour frame changes (the neighbour action is gauge invariant), A_t = z(t beta)^12 (C_{t beta} f)(A). Gauge-fixing the 8 normal links (a matching) gives f proportional to W (C_beta W), and sup f / inf f <= e^{24 beta}. z(x) = (2/pi) e^x int_0^2 e^{-xv} sqrt(v(2 - v)) dv. Upper: sqrt(2/pi) < 1. Lower: [0, 1/x] gives 4/(3 pi e) >= 1/9. Ratio z(t beta)^2/(z(beta) z((2t-1) beta)) <= 9 e^beta beta^{-3/2} t^-3 (2t-1)^{3/2} <= 9 e^beta t^{-3/2} (beta > 2). Then e^{48 beta} < 8^{55.2} < 2^166, so the bound is 2^262 t^-18 <= 2^-8 for t >= 2^15. Seven terms sum to < 1 outside (3/10, 2^15). Checked. The scope "common parameter in each pair" is as in 1485 (12).

**A4. Lower bound 529/2048. HOLDS.** p >= cbar^2/(2 + E c^2) follows from 1485: E[Phi_i Phi_j] >= cbar^2/4 and Var Phi <= Var R = (2 + E c^2)/4. The crossing link lies in exactly 3 plaquettes, and c is linear in it, so E c^2 < 2/3 as in A3. At t = 23/10 the continued fraction is 4.799 < 24/5, so r_1(beta) > 23/48. Then R >= 3p > (9/8)(23/48)^2 = 529/2048. The strict 4 * 2^-2024 comes from 3m + o_1 with m >= o_1 > 2^-2024 (1485 (6), (13)). The upper endpoint is 1485 (7), unchanged. Checked.

**A5. Uniform pivot variance Var(v^t Q v) <= 10. HOLDS.** Write v = (v.e) e + sqrt(u) n. Then v^tQv = lambda_max - a(n) u, with u ~ Beta(3/2, 1/2) independent of n under Haar. The coefficient ratio is 15 k(k-1)/((2k-3)(2k-1)) (Beta function ratio Gamma(7/2)/Gamma(3/2) = 15/4). Then 10 - ratio has the sign of 5(5k - 3)(k - 2) >= 0. The inequality holds pointwise in n, then integrate over n. Checked.

**A6. Score-corrected trace margin (T1). HOLDS.**
- |b_X|^2 <= 2/3: choose for each edge an endpoint crossing that is not the pivot. Every edge has one, since the pivot is one vertex. Conditioned on all else, b is linear in that link, and its mean has norm r_1(|h|) <= sqrt(axial second moment) < sqrt(2/3). Jensen for the norm gives the bound for b_X. Checked.
- Edge-component norm: E_h[((h.a)(h.b) - (a.b)/4)^2] = (|b|^2 + 2(a.b)^2)/24 - (a.b)^2/16 = (2|b|^2 + (a.b)^2)/48. Checked. (a.b_X)^2 = (E[c|X])^2 <= E[c^2|X]. Therefore Var R - ||K Phi||^2 >= 12 (2/3)/48 = 1/6.
- Law of total variance: sigma^2 = Var R - E Var(R | rest) >= 1/2 - 10/(16 beta^2), and sigma^2 <= Var R < 2/3.
- Row: the three positive partners of face x_mu = 1 share three squares of its 3-cube. These squares cover 9 edges, and the 3 edges at the corner (1,1,1) are counted twice, so the multiplicity total is 12. Each covariance is <= 4 x (component norm^2). The sum is <= ||K Phi||^2. Inward faces have K Phi = 0, so the mixed and opposite terms vanish. (T1) gives 0.927 < 15/16. Checked.

**A7. Explicit polynomial (T2) and trial bounds. HOLDS.** Sum_{k<L} (1 - A/H)^k = (H/A)(1 - (1 - A/H)^L). |x| <= 12 beta = 27.6. Taylor: (28e/257)^257 e^28 < 2^-257 2^42. A > e^-28 - 2^-215 > 2^-41 > 2^-43, and A < 2^43. (1 - A/H)^L <= exp(-2^-86 2^95) = e^-512. |B/A - B_e/A_e| <= 56 * 2^-215/A < 2^-166. So ||F - Phi||_inf < 2^-16.
- Normalization: ||x/|x| - y/|y||| <= 2|x - y|/|y|, and sigma > 0.618. Correlation change <= 8 eta. Wilson row <= 15/16 + 56 eta.
- r_*: by reflection Cauchy-Schwarz with Y (||Y|| = 1/2), Corr >= (2 E[F Y]/sd F)^2, with 2 E[FY] >= cbar/2 - eta > 23/96 - eta and sd F <= sqrt(2/3) + eta < 49/60 + eta. Checked.
- Transfer to P on the span of the pair (both directions redone): with probes normalized under W, 2(1 - |rho_W|) = Var_W(f - sg) >= D^-1 (1 - |rho_P|) * 2, so 1 - |rho_P| <= D(1 - |rho_W|). The reverse direction is the same argument. Values 0.0824 > 2/25 and 0.9625 < 97/100 (A9). Checked.

**A8. Omitted probe space, (1)-(3). HOLDS.**
- One-pair Fourier bound: the phase is a^t B b/12. Choose the axis along B^t a. The x-derivative of (2/pi) sqrt(1 - x^2) E_u[m] has L^1 norm <= 4/pi + 240/pi < 122. So the bound is 1464/|B^t a|. ||B||_op >= |xi|/2, because otherwise xi_0^2 + ||Xi||_F^2 < |xi|^2/4 + 3|xi|^2/4. E|a.e|^{-7/8} <= (4/pi) * 8 < 16. Then 1464^{7/8} 2^{7/8} 16 ~ 1.7 * 10^4 < 2^16. Checked.
- Coefficient sums: P >= 1/13 (1348 (13) confirmed at its line 193). Each link has degree <= 60 (at most 6 plaquettes, degree 10). Plancherel shell sum 2^{23-2j} plus a ball term 2^11 < 2^25. Inversion integral < 2^23. The ell-density change costs 2^5 and 2^10. Tally: H^1 constant about 2^{146} * bracket^312, sup constant about 2^{225} * bracket^312, both <= C = 2^228 * bracket^312. Checked. Conditioning on Y_j averages the frozen-link bound, because face i's private pairs are not read by Y_j.
- (2): h(y) = int g(z) k_z(y) dmu_j(z) is the density of E[g(Y_j); Y_i in dy], and ||h||_{H^1} <= C. Split int f h dell = int f (1 - b p_i) h dell + int f b h dmu_i. First term: Cauchy-Schwarz with sup_z int (1 - bp)^2 k_z <= ||1 - bp||_{L^4(K)}^2 C. Second: f is orthogonal to b h_J (coordinatewise degree <= J + deg_max b). The Legendre tail is <= ||grad h||/(J + 1) via -[(1 - x^2) L_n']' = n(n+1) L_n. Checked.
- (3): ||u - p||_4^2 <= ||u - p||_inf ||u - p||_2, and p_i obeys the same tail bound. Checked. The sphere monomial formula reproduces E x^2 = 1/4, E x^4 = 1/8, E x_1^2 x_2^2 = 1/24.
- Block-matrix test, [a G_i, H; H^t, a G_j] >= 0 iff |x^t H y| <= a sqrt(x^t G_i x * y^t G_j y). Decomposition T - P_i T P_j = (I - P_i) T + P_i T (I - P_j). Checked.
- Reflection positivity at P: with P = I_0 + 2 sum I_j T_j - 2^-21 and 2T_j = U_j - U_{j-2}, the U_k coefficient is I_k - I_{k+2} (minus 2^-21 at k = 0). The termwise ratio is x^2/((k+j+1)(k+j+2)) <= 529/800 for the common truncation k <= 16. All U_k coefficients are positive. Checked.
- Opposite-pair finite rank: a separated polynomial density in disjoint raw arrays pushes forward to sum_k E[phi_k | Y_i] E[psi_k | Y_j]. Checked.

**A9. Cutoff at 1/1024 and the four Lean theorems. HOLDS.**
- (4): Translating the private sum by <= 4r/12 changes event probabilities by <= C r (L^1 gradient bound). Haar chord ball mass >= r^3/(12 pi) > r^3/64, from the graph over |v| <= r/2, chord <= r/sqrt 2. Four balls of radius a/(2C) give Pr_Haar(E) >= (a/2)(a^3/(2^3 C^3 64))^4 = a^13/(2^37 C^12). Under Haar, Y_i given the j-reads depends only on the four shared links, so Pr_Haar(Y_i in E | j-reads) = F_E(x). The tilt max/min is <= C, used twice. This gives 2^{37/13} C^2 mu^{1/13} <= 8 C^2 mu^{1/13}. Checked.
- Hoelder 1/4 and the Durrmeyer polynomial u_n: Beta variance <= 1/(4(n+3)), mean variance <= n/(4(n+2)^2), bias <= 1/(n+2). The sum is <= 1.5/(n+1) per coordinate, giving 60/(n+1) after x4 and x10. Checked.
- Cutoff chain redone: ||p - u_n|| <= C eps/(8m) <= eps^2 delta/32 <= delta/2. b u_n = 1 - (1 - u_n/C)^m. On {p >= delta}: m delta/(2C) >= 2/eps, so |1 - bp| <= eps/2 + eps/8. Off it, the mass is <= delta, so by (4) the conditional probability is <= eps^2/16. The first term is eps sqrt(25/64 + 81/1024) < 3eps/4. This uses the conditional-probability form directly, not the L^4 form, and is valid. The second term is sqrt(C) m/(J+1) <= eps/(4 sqrt C). Then 24/25 + 14/1024 = 0.9737 < 122/125 = 0.976. Checked.
- Lean theorems against the text: `besselBounds` holds the 2400 test, the 24/5 bound and 529/2048. `crossingBounds` holds cosh > 25, 3 beta^2 > 63/4, 195/8, 5/6, A_1 > 130 and 7^5 < 130^2. `remainderMargins` holds the 3/4 margin, 122/125, the U_0 positivity and 2^37 < 8^13. `trialBounds` holds sigma > 1/2, (T1) 15/16, 49/60, 2/25, 97/100, 1/12 and (49/100)^4. Each statement matches the inequality the text uses, and partial sums are used only as lower bounds, which is correct. Not in Lean (hand arithmetic, all rechecked here): e^28 < 2^42, 28e/257 < 1/2, the 2^-166 and e^-512 steps, 9 e^beta < 2^8, e^{48 beta} 2^96 < 2^262, 25^2 > 8^3, 4/(3 pi e) >= 1/9, 12 pi < 64, and the Fourier and Plancherel constants. These are elementary bounds with wide margins. Hand recomputation of the tightest Lean items: the k = 1..10 sum at y = (529/100)(65/8) = 42.98 is 21.49 + 76.98 + 110.28 + 84.64 + 40.42 + 13.16 + 3.11 + 0.56 + 0.08 + 0.01 = 350.73, so A_1 >= 1 + (24/65) 350.73 = 130.5 > 130 (margin 0.5); cosh partial at 63/4 = 26.16; r_* = (0.23957/0.81668)^2 = 0.08605 and 1 - (251/250)(0.91395) = 0.0824 > 0.08; 7 - (250/251)(6.06164) = 0.9625 < 0.97; (49/60)^2 = 2401/3600 > 2/3. All agree with the Lean statements.

**Wording notes (no claim changes).**
- N1. "Result" says R <= 7 - (2966/495) 2^-822. That is 1485's endpoint, quoted, not re-proved. Correct as cited.
- N2. "Exclusion": "the denominator is strictly positive since the cut sum varies on open sets" holds because Var F_t > 0 for t != 1 and E F_{2t-1} >= E F_t^2. A one-line reason; not a gap.
- N3. The heading "eight or twelve free pairs" treats the face-j conditioning as an average over frozen links. That is valid because face i's 8 private pairs are not read by Y_j. The note states this only implicitly.

**What (A) does not show.** The decision at beta = 23/10 stays open, as the note says: 529/2048 < R <= 7 - ... The finite compression at the explicit cutoff d > 2^228 is not computable, so row 1493's route (bound the finite forms without materializing them, or sharpen C) is the live one. (T2) is a lower check only.

