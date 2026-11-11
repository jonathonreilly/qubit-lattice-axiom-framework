lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T21:37Z

# Check of `library/gap-seed-limit.md` (row 700), and the port to every integer side (row 703)

Written by Claude Opus 5.5 at high effort, worker 2 on the Mac mini, at commit 87f777e7a. This is one reading by one model. It is not an audit, and the text it checks was written by Claude Fable 5.2 medium, so this is a different model but the same provider. No mass gap is claimed.

## Status block

- Started 2026-11-11T09:37Z. In progress: the verdicts are appended one at a time below.
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
