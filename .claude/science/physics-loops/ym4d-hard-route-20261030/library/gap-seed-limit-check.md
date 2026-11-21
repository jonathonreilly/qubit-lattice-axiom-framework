lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T21:37Z

# Check of `library/gap-seed-limit.md` (row 700), and the port to every integer side (row 703)

Written by Claude Opus 5.5 at high effort, worker 2 on the Mac mini, at commit 87f777e7a. This is one reading by one model. It is not an audit, and the text it checks was written by Claude Fable 5.2 medium, so this is a different model but the same provider. No mass gap is claimed.

## Status block

- Started 2026-11-11T09:37Z. **Complete for this run.** Part A: every point asked HOLDS; no statement of `gap-seed-limit.md` fails. One correction, to a remark used in no proof (A12: the trace bound is (NS) with theta = 1/n, not theta = 0), and one out-of-date label (A13: Lemma X is now checked). Counterexample attempt for Theorem L1 (A15): none; margin about 1.43 at worst in the regime computed. Part B: (G-all) for every integer side L >= 2N, PROVED GIVEN Theorem S and Lemma E'; a new Lemma V bounds S(a; L^3) down to times of order log L; every statement of the file holds along arbitrary integer sides, with 1.002 replaced by 1.085 off the dyadic sides; the symmetric tori L^4 serve for every integer L. Removed open items: sizes other than 2^(k+1) n, and the compatibility of sequences. Still open: (SEED), (U), (NS-gap), d' below max(N, (6/m_0) log L), diagonal rate.
- Not covered: the regime of A15 with rho^d of order 1; Lemma 1.1 of `gap-seed-check.md` (the extension of (TM) to every box) is cited, not re-checked here; the guide on free particles in Section 6 (labelled guide there) is not checked.
- Read in full: `library/gap-seed-limit.md` (all of it, at 87f777e7a). Read for the inputs: `library/gap-transfer.md` N.1-N.8, Lemmas A0, A4, Statements (1)-(8) with proofs; the verdict table of `library/gap-transfer-check.md` (all of (1)-(8d) HOLD; R1-R8 touch none of the statements used here); `library/gap-os-equiv.md` S.1-S.4, Statement (1), Lemma E, Statements (3), (5) with proofs; the verdict table of `library/gap-os-equiv-check.md` ((1), (3), Lemma E HOLD; (5) FAILS AS WRITTEN only at its (5d), line 228; (5a)-(5c) HOLD); `library/gap-crux-restate.md` Sections 1, 3.1, 3.2, 3.4 with the corrections of rows 698, 699 (Lemma E', Corollary S3').
- Repo search (rule 0a): `library/open-core.md` has no line on seed, limit state, thermal sum or clustering. FINISH rows 698-702 cover the seed check, the strong-coupling seed and literature; none covers this check or Part B. So this row attacks nothing that another row covers.
- Not used: the network, the Sussman-Alpoge repository (the checked file uses none of their statements in a proof; nothing in Part B needs them), any numeric run.

## Part A. Line-by-line check of `gap-seed-limit.md`

Notation as in the checked file: R = T_P of the cube, rho_j = lambda_j/lambda_0 over the positive eigenvalues of R (those of R_inv; R = 0 on the rest), S(a) = S(a; L^3).

### A1. Lemma T (trace formula) — HOLDS

Re-derived. (i) Bookkeeping: with 0 = a <= b < a' <= b' <= T - 1, d = a' - b, d' = T - b', one has d + d' + w(F) + w(H) = (a' - b) + (T - b') + b + (b' - a') = T. The slices 0..b and a'..b' are distinct mod T. (ii) The time-like links that no observable reads are g_t for b <= t < a' and for b' <= t <= T - 1: d + d' of them. Each integrates by 1.3 of `gap-transfer.md` to A_T. The d - 1 slices strictly between b and a' then compose to a_d(U(b), U(a')), and the d' - 1 slices strictly between b' and T to a_(d')(U(b'), U(0)) (A0(e)). The two slab integrals are K_F, K_H of `gap-transfer.md` Section 8. This does not use gauge invariance of F or H: it is an identity of kernel integrals. (iii) Width 0: K_F(u, v) is replaced by F(u) delta(u = v), so S_(K_F) is replaced by M_F. Then Y = M_F R^d S_(K_H) (or M_F R^d M_H) is an integral operator with a bounded kernel (for example F(u) a_d(u, w) H(w) when both widths are 0); this needs d >= 1, which holds. (iv) Trace in the eigenbasis: Y R^(d') = (Y R^(d'-1) S-hat^*) S-hat with S-hat = R^* M P of 3.3 there, a product of two Hilbert-Schmidt operators, so the trace may be taken in the ONB {phi_j} plus an ONB of the complement, on which R = 0. Absolute convergence: as written (Bessel, Cauchy-Schwarz, (K1), and sum_j rho_j <= Tr R / lambda_0 < infinity). (v) (K1) and (K2) re-derived: |K_F| <= ||F|| a_(b-a) pointwise with a_(b-a) >= 0, and ||R|| = lambda_0; (K2) is (8a) there, with Omega real. (vi) The one-function formula needs only T - w(F) >= 1 for distinct slices; the file asks T - w(F) >= 2 to quote 8.1 of `gap-transfer.md` literally, and every use meets it. (vii) t_0 = b_A - a_B: for B_t the range is [a_B + t, b_B + t], so d = t - t_0 >= 1 iff t >= t_0 + 1. The cyclic form Tr(R^(T-t) A R^t B) / Tr R^T for two one-slice functions is Lemma T after a cyclic permutation of a trace of a product of trace-class and bounded operators (equal to the kernel integral read in the other order). No defect.

### A2. Proposition C (four terms) — HOLDS

Re-derived. The (0,0) term is f h by (K2). The (i >= 1, j = 0) term is <k_F^* Omega, Rx^d k_H Omega>; since Rn^d = sum_i rho_i^d |phi_i><phi_i| and K_(FH) = K_F R^d K_H (8.5 there), it equals <FH>_(L,inf) - f h, with modulus <= rho_1^d ||F|| ||H|| ((K1) gives ||k_H Omega||, ||k_F^* Omega|| <= norms). The (0, j >= 1) term is u' as stated; its reading as a cylinder truncated function of (H, F) at distance d' is the same identity with roles exchanged and is not used in a bound. The (i, j >= 1) term: v = sum_(j>=1) rho_j^(d') <phi_j, k_F Rx^d k_H phi_j>, and |<phi_j, X phi_j>| <= ||X|| <= ||F|| ||H|| rho_1^d gives |v| <= ||F|| ||H|| rho_1^d S(d'). The double sum is absolutely convergent (A1 (iv)), so it may be summed in the other order, which gives the second member of the minimum. No defect.

### A3. Theorem L1 — HOLDS

Re-derived the algebra. With N = <FH>_(L,T)(1 + S_T) = fh + u + u' + v and <F> = (f + alpha)/(1 + S_T), <H> = (h + gamma)/(1 + S_T):

<FH> - <F><H> = [N(1 + S_T) - (f + alpha)(h + gamma)] / (1 + S_T)^2 = [u + u' + v + S_T N - f gamma - alpha h - alpha gamma] / (1 + S_T)^2.

Since |N| <= 1 + S_T, the term S_T N contributes at most S_T/(1 + S_T) <= S_T; the others are divided by (1 + S_T)^2 >= 1. This gives the precise form. Short form: T, T - w(F) = d + d' + w(H), T - w(H) are all >= d', so S_T, |alpha|, |gamma| <= sigma := S(d') by monotonicity, and e^(-m d') = rho_1^(d') <= sigma. The total is e^(-md)(1 + sigma) + 4 sigma + sigma^2, which is <= e^(-md) + 6 sigma when sigma <= 1. **Case sigma > 1:** the left side is at most |<FH>| + |<F>||<H>| <= 2 < 6 sigma, so the claim holds there too (the file says "trivial", correctly). The hypotheses T >= 4 and T - w >= 2 are redundant: T - w(F) = d + d' + w(H) >= 2 always. The exchanged form follows by translating F by T around the circle. No defect.

Remark of Section 3 (one-point error): |<F>_(L,T) - <F>_(L,inf)| = |alpha - f S_T|/(1 + S_T) <= S(T - w) + S(T) <= 2 ||F|| S(T - w). HOLDS.

(COV): S(a) <= S(n_k floor(a/n_k)) <= S(n_k)^(floor(a/n_k)) for a >= n_k (facts (i), (iii)); d' >= n_k is T >= n_k + d + w(F) + w(H). On T = 2 n_k this is d + w(F) + w(H) <= n_k. HOLDS as stated, including the uncovered window n_k - w(F) - w(H) < d < n_k.

### A4. Theorem L2 and the constant 1.002 — HOLDS

Under (G): m >= m_0 by (G3); S(d') <= s_k^j with j = floor(d'/n_k) >= 1; s_k^j = e^(-m_0 n_k j) 5041^(-j) <= e^(-m_0 n_k j)/5041. Theorem L1 then gives e^(-m_0 d) + 6 s_k^j. If d <= n_k j, then (6/5041) e^(-m_0 n_k j) <= (6/5041) e^(-m_0 d), and 1 + 6/5041 = 1.00119... <= 1.002. On T = 2 n_k with d + w(F) + w(H) <= n_k: d' >= n_k, so j >= 1 and d <= n_k <= n_k j. The constant 1.002 is right, and "0.12 percent" is right. The hypothesis T >= n_k + 2 is redundant (d' >= n_k and d >= 1 give T >= n_k + 1, and Theorem L1 needs nothing more). No defect.

### A5. Lemma FE (finite energy) — HOLDS

A link of the four-dimensional hypercubic lattice lies in 2(4 - 1) = 6 plaquettes; on a torus with all sides >= 3 these are distinct plaquettes, so |P| <= 6 |Gamma|. Each plaquette term lies in [0, 2 beta]. With S = S_P + S', S' free of the links of Gamma: |integral F e^(-S)| <= integral |F| e^(-S') = (integral over G^Gamma of |F|)(integral of e^(-S') over the other links), and Z >= e^(-12 beta |Gamma|) (same last integral), since the Haar measure of G^Gamma has mass one. The cylinder: (8a) of `gap-transfer.md` gives <F>_inf as a limit of torus values for every slab function, and each torus value obeys the bound. No defect.

### A6. Lemma M (the time extent does not matter) — HOLDS

From the Remark of Section 3: |<F>_(k,T) - <F>_(k,inf)| <= 2 ||F|| S(T - w) <= 2 ||F|| S(n_k) <= 2 ||F|| s_k, using T - w >= n_k and monotonicity; T - w >= n_k >= 3 >= 2 meets the condition of the Remark. Twice gives 4 ||F|| s_k. The case T' = inf is the same with one term zero. Only T - w >= n_k (and the fitting conditions) is used, as the file says (its checker point 3). No defect.

### A7. Lemma RPc (reflection positivity of the cylinder state) — HOLDS

Re-derived the change of variables. theta maps the link from (x, t) to (x, t+1) to the link from (x, -t) to (x, -t-1), which is the link from (x, -t-1) to (x, -t) reversed; so (theta g)_t = (g_(-t-1))^(-1). On the slab [-b, b], with U(0) = u fixed, the density (8b) factors into a negative-time part and a positive-time part. In the negative part put U'(t') = U(-t'), g'_(t') = (g_(-t'-1))^(-1), t' = 0..b-1, and t = -t' - 1. Then U(t) = U'(t'+1), U(t+1) = U'(t'), g_t = (g'_(t'))^(-1), and

T_0(U(t), g_t . U(t+1)) = T_0(U'(t'+1), (g'_(t'))^(-1) . U'(t')) = T_0(g'_(t') . U'(t'+1), U'(t')) = T_0(U'(t'), g'_(t') . U'(t'+1)),

by T_0(h.x, h.y) = T_0(x, y) with x = U'(t'+1), y = (g'_(t'))^(-1) . U'(t') (left action, N.5), then symmetry of T_0 (N.7). Inversion preserves the Haar measure of each g_t(x) (N.1). Omega(U(-b)) = Omega(U'(b)). conj(Theta F)(U) = conj(F(U', g')). T_0 and Omega are real. So the negative part integrates to lambda_0^b conj(psi_F(u)) and the positive part to lambda_0^b psi_G(u), and lambda_0^(-2b) cancels both. Fubini: all factors bounded. Independence of b: integrating one more slab with the end factor Omega gives T_P Omega = lambda_0 Omega. No defect.

### A8. Theorem L3 (a)-(e) — HOLDS

(a) The partition of unity: each x is within 1/r of some x_j, so p_j(x) >= 1/r there and the sum is >= 1/r; q_j(x) = 0 unless dist(x, x_j) < 2/r; so |f - sum f(x_j) q_j| <= modulus of continuity at 2/r. Rational coefficients: replace f(x_j) by a point of Q + iQ within eps, and use sum q_j = 1. Countably many finite Gamma; diagonal subsequence; continuous F by the 2 eps argument; bounded Borel F by Lemma A4 (L^2 density, hence L^1 density on a probability space) and Lemma FE applied to F - F', with a constant e^(12 beta |Gamma|) that does not depend on i. Fitting conditions hold for large i. Correct.

(b) Lemma M with T_i, T'_i >= n_(k_i) + w for large i (both sequences admissible) and s_(k_i) -> 0. Correct. The symmetric tori (T - n_k = n_k) and the cylinders are admissible.

(c) Linearity, positivity, normalisation, |nu(F)| <= ||F|| and Lemma FE pass to the limit. Translations: each member is invariant under its torus translations. Hypercubic group: through (b), nu is a limit of the states on (L_(k_i))^4, which are invariant under signed permutations of the axes (the plaquette weight depends on tr U_p only, which is invariant under inversion and cyclic order, N.2; inversion preserves Haar measure, N.1). Reflection positivity at t = 0 from Lemma RPc through the cylinders; at other site mirrors by translation and by the hypercubic group. Correct.

(d) Time direction: on (L_(k_i))^4 and for large i, d + w(F) + w(H) <= n_(k_i), so Theorem L2 gives e^(-m_0 d) + 6 s_(k_i), and s_(k_i) -> 0 while the three expectations converge (FH is local). Space directions: the exchange of the axes mu and 4 is a symmetry of (L)^4, with all four sides equal. Translate form: for v_mu > t_0, d = v_mu - (b_A - a_B) >= v_mu - t_0 >= 1; for v_mu < -t_0, d = |v_mu| - (b_B - a_A) >= |v_mu| - t_0. Cube form: d >= |v_mu| - 2r. Euclidean: |v| <= 2 |v|_inf in four dimensions, so the rate is m_0/2. Correct.

(e) The point the row asks about. `gap-os-equiv.md` S.2 defines a datum as (V, b, tau, 1) with V a complex vector space and b a sesquilinear map; no measure is part of the definition. Statement (1), Lemma E and Statement (3) use only (P1)-(P3) (its check confirms each, rows "(1) HOLDS", "(3) HOLDS", "E.1-E.12 HOLDS"). Here V = local functions with time range in [0, infinity): a complex vector space (a sum of two local functions is local, with the union of the supports), tau_t V subset V for t >= 0, tau_0 = id, tau_s tau_t = tau_(s+t), tau_t 1 = 1, b(1, 1) = nu(1) = 1, b antilinear in the first slot because F -> conj(Theta F) is antilinear and nu is linear. (P1): b(F, F) = nu(conj(Theta F) F) >= 0 by (c). (P2): Theta tau_t = tau_(-t) Theta and translation invariance, as written. (P3): |b(tau_t F, tau_t F)| <= ||F||^2 since |nu(G)| <= ||G||. The truncated function of S.2 is u(F, F; t) = b(F, tau_t F) - b(F, 1) b(1, F) with b(F, 1) = nu(conj(Theta F)) = conj(nu(F)) (the time reflection is in the hypercubic group) and b(1, F) = nu(F); so u(F, F; t) = nu(conj(Theta F) tau_t F) - |nu(F)|^2, as the file says. conj(Theta F) has time range [-b, -a], tau_t F has [a + t, b + t], so (d) applies with gap t + 2a >= t >= 1 and gives |u| <= ||F||^2 e^(-m_0 t). This is (X_m^C) with C = V, C_F = ||F||^2, t_F = 1 (the hypothesis is asked only at even t >= t_F). The class V is total in the completion of V/N by construction. So (3b) gives (G_m), (E1) gives (V), and (E3) gives spec(T|_(Omega-perp)) in [-e^(-m_0), e^(-m_0)]. No measure on the infinite lattice is used, and Kolmogorov's extension ((8e), not rebuilt) is not needed. Other directions: hypercubic invariance. Correct.

### A9. Section 4.4 and the bound of Section 4.5 — HOLDS

4.4: correct as a statement of what is and is not proved; (U) is correctly stated as open.

4.5: Lemma M with T' = L_k needs T >= n_k + w and L_k = 2 n_k >= n_k + w, that is w <= n_k, which the file assumes. Then |<FH>_T - <FH>_(L_k)| <= 4 s_k ||F|| ||H||, and |<F>_T <H>_T - <F>_(L_k) <H>_(L_k)| <= |<F>_T - <F>_(L_k)| ||H|| + ||F|| |<H>_T - <H>_(L_k)| <= 8 s_k ||F|| ||H||; on (L_k)^4 the exchange of axes and Theorem L2 give 1.002 e^(-m_0 d). Total 1.002 e^(-m_0 d) + 12 s_k. Correct.

### A10. Propositions P and P' — HOLD (as conditional statements)

P: with s_iota = S(n_iota; (2 n_iota)^3) <= s_* < 1/5041, Theorem S gives (G) at each iota with m_0(iota) = log(1/(5041 s_iota))/n_iota >= log(1/(5041 s_*))/n_iota = M_* ell_*/n_iota >= M_* a_iota, since n_iota a_iota <= ell_*. (b), (c) are Theorem L3 (d), (e) with e^(-m_0 d) <= e^(-M_* d a_iota). The remark "it suffices that Phi <= 1.9 x 10^(-4)" gives s_iota <= e^(1.9 x 10^(-4)) - 1 < 1.91 x 10^(-4) =: s_* < 1/5041 = 1.9837... x 10^(-4). Correct.

P': (H1) of `gap-os-equiv.md` (5) is asked on the time set a_n Z with ||T_t psi|| <= e^(-m_n t) ||psi|| for t in a_n Z_+; Theorem L3 (e) gives e^(-m_0 t/a) <= e^(-M_* t) in physical time t, with S_n = Omega_n-perp, so m_n = M_*. (H2), (TOT), (P1)-(P3) and (P4) of the limit datum are hypotheses of P'. Then (5a)-(5c) give the claim; the false sentence of (5d) is not used. Correct.

### A11. The rate filter — HOLDS

s = S(n; (2n)^3) >= rho_1^n = e^(-nm). With s < 1/5041: n >= log(1/s)/m > log(5041)/m, and log 5041 = 2 log 71 = 8.525... > 8.5 (e^4.26 = 70.81 < 71 < 71.52 = e^4.27). m_0 = (log(1/s) - log 5041)/n <= m - log(5041)/n. Physical form: M_* <= m_0(iota)/a_iota <= M - log(5041)/(n_iota a_iota) <= M - log(5041)/ell_*, where M is the physical gap of the cube of side 2 n_iota at that cutoff. Correct.

### A12. Propositions N1, N2, Corollary N3 — HOLD; one remark corrected

N1: each j with E_j <= E contributes rho_j^a >= e^(-aE) to S(a). Under (G), s_k e^(n_k E) = e^(n_k(E - m_0))/5041. Correct.

N2: e^(-n E_j) = n times the integral of e^(-nE) over E >= E_j; Tonelli gives S(n) = n times the integral of N(E) e^(-nE), and N = 0 below E_1 >= m. Then A n times the integral over [m, infinity) of e^(-(1 - theta) n E) is A e^(-(1-theta) n m)/(1 - theta). Correct.

N3: if log A_n / n < (1 - theta) m - eps for infinitely many n in I, then log A_n - (1 - theta) n m < -eps n, which is below log((1 - theta)/5041) for large such n. Correct. The two-sided "one line" is N1 with a = n and N2 with A = sup over E >= m of N(E) e^(-theta n E). Correct.

**Correction (remark after (NS-gap), not used in any proof).** The file says the trace bound Tr R/lambda_0 <= e^(12 beta L^3) "is (NS) with theta = 0". The trace bound does not give that: a bound with theta = 0 says N(E) <= A for all E, so that R has at most A positive eigenvalues, and the trace bound says nothing of the kind. What it gives is N(E) e^(-E) <= S(1) <= e^(12 beta (2n)^3), that is (NS) with theta = 1/n and log A = 96 beta n^3. Corrected text: "which is (NS) with theta = 1/n and log A = 96 beta n^3, too weak by the power n^2". The conclusion of the remark (too weak) is unchanged.

### A13. The second exact form of the seed (Section 6) — HOLDS

With W(a, b) = Z(a, b, 2n, 2n) (directions 3, 4 fixed at 2n), T_b is the transfer operator of the box (b, 2n, 2n), so g(n, 2n) = log(1 + S(n; (2n)^3)) and g(2n, n) = log(1 + S(2n; (n, 2n, 2n))). Lemma X at (a, b) = (n, 2n): n kappa(2n) + g(n, 2n) = 2n kappa(n) + g(2n, n). This is the identity. Bounds: kappa(2n) <= kappa(n) (Lemma K (d), corrected domain b >= 3, which n >= 3 meets), so 2n kappa(n) - n kappa(2n) >= n kappa(n) >= 0; and <= 2n kappa(n) since kappa >= 0. ell is finite by (LB). The "if and only if" holds. Lemma X is now checked (rows 698, 699), so the label "unchecked" in the file is out of date.

### A14. Theorem L as stated in Section 7 — HOLDS

Item 1 is Theorem S as corrected (it gives (G1)-(G3) with s = S(n; (2n)^3), including simplicity from (TM)). Item 2: with general a, d' = T - (b' - a) agrees with Lemma T after translation; the four-direction clause on (L_k)^4 uses the axis exchange; the cylinder clause is (8c) with m >= m_0. Item 3 is Theorem L3. Item 4 is Proposition P, P'. The input table is right, with two updates: Theorem S and Lemma X are now checked (rows 698, 699, no statement fails), and the open list changes as Part B below says.

### A15. Attempt to break Theorem L1 in a model solved by hand: independent two-state rings — no counterexample; margin about 1.43 at worst in the regime computed

All by hand. No run was made.

**One ring.** Two states, a symmetric 2 x 2 transfer matrix R_1 = lambda_0 |phi_0><phi_0| + lambda_1 |phi_1><phi_1| with 0 < rho = lambda_1/lambda_0 < 1, phi_0 = (c, s), phi_1 = (-s, c), c, s > 0. Its entries are positive (the off-diagonal entry is (lambda_0 - lambda_1) c s > 0), so it is the transfer matrix of a nearest-neighbour chain on a ring of length T with a positive-definite weight: a reflection-positive instance of Lemma T with widths 0 and k_F = M_F. Let f = diag(1, -1). In the eigenbasis f_00 = c^2 - s^2 =: g, f_11 = -g, f_01^2 = 4 c^2 s^2 = 1 - g^2. With d + d' = T, Lemma T gives exactly (terms (0,0), (1,0), (0,1), (1,1) are g^2, rho^d (1 - g^2), rho^(d') (1 - g^2), rho^T g^2):

<f>_T = g (1 - rho^T)/(1 + rho^T),  <f_0 f_d>_T = g^2 + (1 - g^2)(rho^d + rho^(d'))/(1 + rho^T).

**N independent rings.** R = R_1 tensored N times: excited ratios rho^r with multiplicity C(N, r), so rho_1 = rho and S(a) = (1 + rho^a)^N - 1. Take F = H = the product of the N spins (sup norm 1). Everything factorizes, x := rho^T:

Delta := <F_0 F_d>_T - <F>_T^2 = [g^2 + (1 - g^2)(rho^d + rho^(d'))/(1 + x)]^N - g^(2N) ((1 - x)/(1 + x))^(2N).

Precise bound of Theorem L1 (widths 0): B = rho^d (1 + S(d')) + rho^(d') + 3 S(T) + S(T)^2.

**Exact limit g -> 1.** Then f is diagonal in the eigenbasis, u = u' = 0, v = S(T) exactly, alpha = gamma = (1 - x)^N - 1, and the numerator of Theorem L1 is exactly (1 + S_T)^2 - (1 + alpha)^2. So the thermal terms S_T, |alpha|, |gamma| of B are attained exactly; only the bound |v| <= rho^d S(d') for v = S(T) is loose.

**Regime.** Let rho^d -> 0, rho^(d' - d) -> 0 (d' much larger than d), N -> infinity with N rho^(d') -> y' > 0 fixed, and N(1 - g^2) -> z >= 0. Then N x = y' rho^d -> 0, S(d') -> e^(y') - 1, S(T) = y' rho^d (1 + o(1)), and expanding both terms of Delta to first order:

Delta = rho^d e^(-z) (z + 4 y') (1 + o(1)),  B = rho^d (e^(y') + 3 y') (1 + o(1)).

So Delta/B -> e^(-z)(z + 4y')/(e^(y') + 3y'). For 4y' >= 1 the maximum over z is at z = 0, giving 4y'/(e^(y') + 3y'), whose maximum over y' is at y' = 1 (the derivative is proportional to e^(y')(1 - y')): 4/(e + 3) = 0.6995. For 4y' < 1 the maximum over z is e^(4y' - 1)/(e^(y') + 3y') <= 1/(e^(1/4) + 3/4) < 0.50. With d = d' instead, the limit ratio is at most 4y/(e^y + 1 + 3y) <= 0.61 (maximum near y = 1.28).

Short form e^(-md) + 6 S(d') in the same regime: B_short = rho^d + 6 (e^(y') - 1) + o(1), which is of order 1 when y' is of order 1, and when y' = c rho^d it is rho^d (1 + 6c) against Delta <= rho^d e^(-1) (1 + o(1)) (z = 1): a ratio at most 0.37.

**Result of the attempt.** No counterexample; none can exist, since Theorem L1 holds (A3). In this family, in the regime above, the precise form is tight to the factor 1/0.6995 = 1.43, and three of its thermal coefficients are attained exactly at g = 1; the short form has a margin of at least about 2.7. Not shown: the supremum of Delta/B over all parameters of the family (the regime with rho^d of order 1 was not computed), and optimality of the constant 6 in general.

## Part B. Port to every integer side

Throughout: N >= 3 an integer, s = S(N; (2N)^3) < 1/5041, q = 5041 s, m_0 = log(1/q)/N, s_i = q^(2^i)/5041 = e^(-m_0 2^i N)/5041. For an integer L >= 2N let k = k(L) >= 0 be the integer with D := 2^(k+1) N <= L < 2D, and put a_L := D/2 = 2^k N and t_L := q^(2^k)/71 = e^(-m_0 a_L)/71. Then L/4 < a_L <= L/2, k(L) > log_2(L/(4N)), so k(L) -> infinity and t_L -> 0 as L -> infinity.

### B1. Lemma E' and Corollary S3' (row 699) — re-derived here, HOLD

Lemma E': Lemma A (a) for T_a gives W(a, h) <= W(a, b)^(h/b) for h >= b. Write log W(a, h) = a e(h) + g(a, h) = a ell h + a kappa(h) + g(a, h); the terms a ell h cancel against (h/b) a ell b. With kappa(h) >= 0: g(a, h) <= (a h/b) kappa(b) + (h/b) g(a, b). Lemma X (b > a): kappa(b) <= g(a, b)/(b - a). So g(a, h) <= (h/b)(a/(b - a) + 1) g(a, b) = (h/(b - a)) g(a, b). Hypotheses h >= b > a >= 3 are what Lemmas K, X need. Correct.

Corollary S3': three applications of Lemma E' with a = D/2, b = D, h = L, to the families W(a', b') = Z(a', b', D, D), then Z(a', L, b', D), then Z(a', L, L, b') (each symmetric in a', b' by an axis exchange; all sides >= 3; ell finite by (LB)). The base of the second step is the output of the first (the box (L, D, D) read with b' = D in the varying direction), and so on. Each exponent is L/(D/2) = 2L/D < 4, so 1 + S(D/2; L^3) <= (1 + s_k)^64; s_k <= 1/5041 < 1/640 gives S(D/2; L^3) <= 71 s_k = q^(2^k)/71. The gap: rho_1^(D/2) <= S(D/2; L^3) (simple top eigenvalue). Correct.

### B2. Hypothesis (G-all) for every integer side — PROVED GIVEN Theorem S, Lemma E', (TM)

**(G-all).** For every integer L >= 2N:
- (G-all 1) S(a_L; L^3) <= t_L = e^(-m_0 a_L)/71;
- (G-all 2) the top eigenvalue of the transfer operator of the cube of side L is simple ((TM), extended to every box by `gap-seed-check.md` Lemma 1.1);
- (G-all 3) m(L^3) >= m_0 + log(71)/a_L >= m_0.

Proof. (G-all 1) is Corollary S3' (B1). (G-all 3): rho_1^(a_L) <= S(a_L; L^3) <= e^(-m_0 a_L)/71. QED

For L = 2^(k+1) N (a dyadic side), Theorem S gives the stronger (G1) with 1/5041 in place of 1/71; the other sides have 1/71.

### B3. The time extents covered (COV-all), with a new volume bound — PROVED GIVEN Theorem S, Lemma E'

**Lemma V (thermal sums at shorter times).** Let L >= 2N and 0 <= i <= k(L), a = 2^i N. Then

S(a; L^3) <= exp((L/a)^3 s_i) - 1 = exp((L/a)^3 e^(-m_0 a)/5041) - 1.

Hence for every integer a with N <= a <= L/2:

S(a; L^3) <= exp(X) - 1 with X := 8 (L/a)^3 e^(-m_0 a/2)/5041, and S(a; L^3) <= 2X when X <= 1.

Proof. Theorem S: S(a; (2a)^3) <= s_i. Lemma E' three times as in B1, now with b = 2a and h = L (h >= b because 2^(i+1) N <= 2^(k+1) N <= L), each exponent L/(b - a) = L/a: 1 + S(a; L^3) <= (1 + s_i)^((L/a)^3) <= exp((L/a)^3 s_i). For general a with N <= a <= L/2, let a_i = 2^i N with a/2 < a_i <= a; then 2 a_i <= L, so i <= k(L); S is non-increasing in time, so S(a) <= S(a_i), and (L/a_i)^3 < 8 (L/a)^3, e^(-m_0 a_i) <= e^(-m_0 a/2). Last: e^X - 1 <= (e - 1) X on [0, 1]. QED

(For i = k(L) this is S3' up to the constant: (L/a_L)^3 < 64.)

**(COV-all).** In Theorem L1 on L^3 x T the error term 6 S(d') is controlled in two ranges:
- d' >= a_L: 6 S(d') <= 6 t_L^(floor(d'/a_L)) (facts (i), (iii) and (G-all 1));
- N <= d' <= L/2: 6 S(d') <= 12 X(d') when X(d') <= 1. Since 8/(5041 d'^3) < 1, X(d') <= L^3 e^(-m_0 d'/2), so X(d') <= 1 as soon as d' >= (6/m_0) log L.

So every d' >= max(N, (6/m_0) log L) is covered (the uncovered extents lie below that number): (COV-all) holds for T >= max(N, (6/m_0) log L) + d + w(F) + w(H), with an error that tends to 0 when d' - (6/m_0) log L -> infinity. For dyadic sides this improves the file's (COV), which needed d' >= n_k = L/2.

### B4. Which statements of `gap-seed-limit.md` hold along arbitrary integer sides

An *admissible sequence* is now (L_i, T_i) with L_i integers, L_i -> infinity (in any order, not monotone, any residues), and T_i (an integer or infinity) with T_i - a_(L_i) -> infinity. Symmetric tori T_i = L_i are admissible (T_i - a_(L_i) >= L_i/2), and so are cylinders. By Lemma V one may relax this to T_i - (6/m_0) log L_i -> infinity; see Lemma M-all.

| Statement of `gap-seed-limit.md` | Along arbitrary integer sides | Mark |
|---|---|---|
| Lemma T, Proposition C, Theorem L1 | Unchanged: they read only (TR) and hold for every L >= 3 | PROVED (A1-A3) |
| Theorem L2 | **L2-all.** L >= 2N, d' >= a_L: trunc <= ||F|| ||H|| (e^(-m_0 d) + 6 t_L^(floor(d'/a_L))). If also d <= a_L floor(d'/a_L): trunc <= (1 + 6/71) ||F|| ||H|| e^(-m_0 d), and 1 + 6/71 = 1.0845... <= **1.085** (the constant 1.002 becomes 1.085; on dyadic sides 2^(k+1) N the constant 1.002 stays). On L^4: covered for d + w(F) + w(H) <= L - a_L (and L - a_L >= L/2); the 1.085 form for d + w(F) + w(H) <= a_L. Proof: Theorem L1 with (G-all), t_L^j <= e^(-m_0 a_L j)/71 | PROVED GIVEN (G-all) |
| Lemma FE, Lemma RPc | Unchanged: no (G) | PROVED (A5, A7) |
| Lemma M | **M-all.** T, T' >= a_L + w: difference <= 4 ||F|| t_L. Also: if N <= T - w, T' - w <= L/2 and X(T - w), X(T' - w) <= 1, the difference is <= 4 ||F|| (X(T - w) + X(T' - w)) (Lemma V and the Remark of Section 3: 2 S(T - w) each) | PROVED GIVEN (G-all), Lemma V |
| Theorem L3 (a) | Unchanged (compactness and Lemma FE; no (G)) | PROVED |
| Theorem L3 (b) | Holds with t_(L_i) -> 0 in place of s_(k_i); the limit depends on the L_i only. With M-all it also holds for T_i with T_i - (6/m_0) log L_i -> infinity | PROVED GIVEN (G-all), Lemma V |
| Theorem L3 (c) | Holds; the symmetric tori L_i^4 exist for every integer L_i, and the hypercubic group acts on them | PROVED GIVEN (G-all) |
| Theorem L3 (d) | Holds with the same rate m_0 and constant 1: on L_i^4, for large i, d + w(F) + w(H) <= a_(L_i) (a_L > L/4 -> infinity), L2-all gives e^(-m_0 d) + 6 t_(L_i), and t_(L_i) -> 0. Space directions by the exchange of axes on L_i^4. **So the symmetric tori L^4 serve in Theorem L3 (d) for every integer L >= 2N**, not only for L = 2^(k+1) n | PROVED GIVEN (G-all) |
| Theorem L3 (e) | Holds unchanged (it reads only (c), (d) and `gap-os-equiv.md` (1), (3), Lemma E) | PROVED GIVEN (G-all), os-equiv |
| Section 4.5 bound | **4.5-all.** w(FH) <= L - a_L, T >= a_L + w(FH), d + (the two widths in the space direction) <= a_L: trunc <= ||F|| ||H|| (1.085 e^(-m_0 d) + 12 t_L) | PROVED GIVEN (G-all) |
| Proposition P | (a) every cube of side L >= 2 n_iota (not only 2^(k+1) n_iota) has physical gap >= M_*; (b), (c) for limit states along any admissible integer-side sequence; M_* unchanged | PROVED GIVEN (SEED-phys), Theorem S, Lemma E' |
| Proposition P' | Unchanged in form; the members may now be limit states along any integer sides | PROVED GIVEN P and os-equiv (5a)-(5c); continuum datum OPEN |
| Rate filter | Unchanged (it reads the seed only) | PROVED |
| N1 | **N1-all.** N_L(E) <= t_L e^(a_L E) = e^(a_L (E - m_0))/71 | PROVED GIVEN (G-all) |
| N2, N3, second exact form | Unchanged (no (G)) | PROVED (N3 given Theorem S) |
| Theorem L, items 1-3 | Item 1 extends to (G-all); item 2 to every L >= 2N with t_L, a_L, 1.085; item 3 to every admissible integer-side sequence; item 4 as P, P' | PROVED GIVEN (SEED), Theorem S, Lemma E' |

### B5. Open items of Section 7 of `gap-seed-limit.md`

- "Sizes other than 2^(k+1) n are not covered by (G)": **REMOVED** for every L >= 2N (B2). Sides below 2N do not enter limits.
- Input (5) of Section 5, "compatibility of the sequences" (the account's tori of side 2 L^m): **REMOVED**. Any sequence of integer sides tending to infinity is admissible; no power of 2 is needed.
- "Time extents with d' < n_k are not covered": **REDUCED** (Lemma V): on the cube of side L every d' >= max(N, (6/m_0) log L) is covered. OPEN: d' below that, where the hypothesis gives no bound on S(d'; L^3).
- (U), convergence of <F>_(L^4) as L -> infinity: **still OPEN**, now over all integers L. (G-all) compares no two sizes either, so two limit points along two sequences of sides are not excluded.
- (SEED), (NS-gap), and the Euclidean rate m_0/2 in diagonal directions: unchanged, OPEN.

## Verdict table

| Point | Verdict |
|---|---|
| Lemma T (d, d', widths, width 0) | HOLDS |
| Proposition C | HOLDS |
| Theorem L1 (denominator 1 + S_T; case S(d') > 1) | HOLDS |
| Theorem L2 and 1.002 | HOLDS |
| Lemma FE | HOLDS |
| Lemma M | HOLDS |
| Lemma RPc (time-like links) | HOLDS |
| Theorem L3 (a)-(e), incl. (e) as a datum with no measure and Statement (3) with the class V | HOLDS |
| Section 4.5 bound | HOLDS |
| Propositions P, P' | HOLD (conditional as stated) |
| Rate filter | HOLDS |
| N1, N2, N3 | HOLD; remark after (NS-gap) corrected (theta = 1/n, not 0; not used in a proof) |
| Second exact form of the seed | HOLDS (label "unchecked" on Lemma X out of date) |
| Theorem L (Section 7) | HOLDS |
| Counterexample to L1 (two-state rings) | none; Delta/B <= 0.70 in the regime computed |
| Part B: (G-all), Lemma V, L2-all (1.085), M-all, L3-all, 4.5-all, P-all, N1-all | PROVED GIVEN Theorem S, Lemma E' (and (SEED-phys) for P) |

Consumer line: a consumer may use Theorem L of `gap-seed-limit.md` as stated, given (SEED), and with B4 in place of its restriction to the sides 2^(k+1) n: limit states along any sequence of integer sides, rate m_0, constant 1; on finite tori constant 1.085 (1.002 on dyadic sides) and error 6 t_L.

RESULT: Part A — all points of `gap-seed-limit.md` HOLD (one remark corrected: the trace bound is (NS) with theta = 1/n; no counterexample to Theorem L1, margin about 1.43 in the two-state-ring regime computed). Part B — (G-all) PROVED GIVEN Theorem S and Lemma E': S(a_L; L^3) <= q^(2^k)/71 and m(L^3) >= m_0 for every integer L >= 2N; new Lemma V covers time extents down to max(N, (6/m_0) log L); Theorem L holds along arbitrary integer sides (constant 1.085 off dyadic sides), and the symmetric tori L^4 serve in L3 (d) for every L. Removed: other sizes, compatibility of sequences. Open: (SEED), (U), (NS-gap), d' below max(N, (6/m_0) log L), diagonal rate m_0/2.
