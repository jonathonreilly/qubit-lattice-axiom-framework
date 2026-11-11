lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T21:15Z

# gap-seed-limit: from the seed to exponential clustering in every limit state (row 700)

Author run at commit 547801e01, started 2026-11-11T09:15Z. Research-stage working state. **No mass gap is proved by this file.** Everything is conditional on Hypothesis (G) below, which is the conclusion of Theorem S of `library/gap-crux-restate.md` (row 697, not yet checked; checks are rows 698, 699). Nothing here is checked by a model that did not write it. No computer run was made for this file.

## Status block (kept current)

- Steps 1, 2 (torus bound with the thermal error): written, Sections 2, 3. PROVED GIVEN (TR).
- Steps 3 to 7: not yet written (this line is updated as they land).
- Marks: PROVED = by hand in this file from the named inputs, unchecked. PROVED GIVEN (X) = the same, with X an input not proved here. OPEN = one exact statement.

## 0. Repo search, reading state, credits

**Repo search (rule 0a, done before deriving).** Searched `library/gap-*.md`, `library/prior/gap-*.md`, `library/open-core.md` and the FINISH rows for: seed, limit state, limit point, thermal, clustering, exponential clustering, Tychonoff, subsequence. `library/open-core.md` has no match for seed, mass gap, limit state or exponential clustering. No other FINISH row covers this item (rows 698, 699 check Theorem S; 701 is the seed at strong coupling; 702 is literature). Matches that bind this file, reused and not redone:

- `library/gap-transfer.md` (row 667; check row 671 = `gap-transfer-check.md`, verdict HOLDS for (1) to (8a)-(8d)): the transfer operator, the trace formulas (1b), (1c), the slab kernels K_F and the cylinder state (8a), (8b), clustering on the cylinder (8c). Repairs R1 to R8 of the check touch remarks and Section 9, none of the statements used here (R1: Remark 1.8, unused; R2, R3, R5: Section 9; R4: line 256; R6: (8e) stays a citation, and (8e) is not used here; R7, R8: credits and side facts).
- `library/gap-os-equiv.md` (row 668; check `gap-os-equiv-check.md`): Statement (3) (decay on a total class gives the gap; HOLDS), Statement (7c) (the comparison of torus and cylinder with the thermal sum, stated there for single-slice observables and "not proved in physical units"). Its Statement (5) FAILS AS WRITTEN at one sentence (check R1) and is not used here.
- `library/gap-crux-restate.md` Sections 1, 3.1, 3.4 (statements; S(a; B) non-increasing in a and submultiplicative; Theorem D (d); Lemma X; Lemma E and the remark on multiples).
- `library/gap-skeleton-max-b.md` Part 0 (0.1 volume-first limits, 0.4 the statement (GAP)) and Part 4 items 5, 6 (limit chains for boxes with free walls; a different object, not reused).

**Not read:** the bodies of the other gap files; any primary paper. Nothing was fetched from the network; the Sussman-Alpoge account is used only through the quotations in `gap-skeleton-max-b.md` Part 0 (it claims no gap and no exponential decay, lines 3054-3056 there).

**Credits.** Osterwalder and Seiler, Luscher (transfer operator and reflection positivity, through row 667). Sussman and Alpoge with Claude and Codex (the account; the notion of volume-first limit points; not used in a proof). Row 667 author and row 671 checker (trace formulas, slab kernels). Row 668 (the equivalence of decay and gap). Row 697 (Theorem S, Lemmas K, X, E, Theorem D). The comparison "torus = cylinder up to the thermal weight of the excited states" is os-equiv (7c); what is added here is the two-slab form with both error terms, the remark that the error is dominated by the main term on the symmetric tori, and the consequences for limit states.

## 1. Setting, notation, Hypothesis (G)

Group SU(2), Wilson action, beta > 0 fixed, as in `gap-transfer.md` N.1 to N.7. Space is the periodic cube Lambda_L = (Z/L)^3, L >= 3; time is Z/T (T >= 2) or Z. The torus is written L^3 x T, the cylinder L^3 x Z. <.>_{L,T} is the Wilson expectation on L^3 x T, <.>_{L,inf} the cylinder state of `gap-transfer.md` (8a), (8b).

**Operator.** R := T_P of `gap-transfer.md` Section 1 for the cube of side L, on H = L^2(X). It is self-adjoint, positive, trace class, with eigenvalues lambda_0 > lambda_1 >= lambda_2 >= ... > 0 (with multiplicity; all other spectrum is the kernel), orthonormal eigenvectors phi_0 = Omega > 0, phi_1, ..., and Z_{L,T} = Tr R^T (statements (1) to (5) there). rho_j = lambda_j / lambda_0, so 1 = rho_0 > rho_1 >= rho_2 >= ... > 0. Gap m(L^3) = log(1/rho_1). Rx := sum over j >= 1 of rho_j |phi_j><phi_j| (the excited part of R/lambda_0).

**Thermal sum.** S(a; L^3) = sum over j >= 1 of rho_j^a for integers a >= 1. This is S(a; B) of `gap-crux-restate.md` Section 1 with B = L^3. Facts (two lines each): (i) S(a; L^3) is non-increasing in a, since 0 < rho_j < 1. (ii) rho_1^a <= S(a; L^3). (iii) S(a + a'; L^3) <= S(a; L^3) S(a'; L^3), since a sum of products of positive terms is at most the product of the sums. (iv) Z_{L,T} = lambda_0^T (1 + S(T; L^3)).

**Hypothesis (G)** (the conclusion of Theorem S; taken as given). n >= 3 is an integer, 0 < s < 1/5041, q := 5041 s < 1, n_k = 2^k n, L_k = 2 n_k for k >= 0. For every k >= 0:

- (G1) S(n_k; (L_k)^3) <= s_k := q^(2^k) / 5041;
- (G2) the top eigenvalue of R for the cube of side L_k is simple (this is also part of (TM), proved in `gap-transfer.md` (4));
- (G3) m((L_k)^3) >= m_0 := log(1/q) / n.

Note e^(-m_0 n_k) = q^(2^k) = 5041 s_k. So (G1) reads S(n_k; (L_k)^3) <= e^(-m_0 n_k) / 5041, and (G3) follows from (G1) and fact (ii). The only content is (G1).

**Observables.** A link of Z^4 (or of a torus) is a pair (x, mu). A *local function* is a bounded Borel function F of the variables on a finite set of links, supp F. For a coordinate direction mu, the *mu-range* of F is the smallest interval [a, b] of integers that contains the mu-coordinates of both end points of every link of supp F. With mu = time this is the slab of `gap-transfer.md` Section 8: a time-like link from time t to t + 1 has range [t, t + 1]. The *width* is w(F) = b - a >= 0. ||F|| is the sup norm. Gauge invariance is not required anywhere below (the operator R contains the gauge projection; `gap-transfer.md` (8c), (8d)).

**Slab operators.** For F with time range [a, b], b > a: K_F is the kernel of `gap-transfer.md` Section 8, and k_F := lambda_0^(-(b-a)) S_{K_F}. For b = a (F a function of the spatial links of one slice): k_F := M_F, multiplication by F. In both cases:

(K1) |<phi, k_F psi>| <= ||F|| ||phi|| ||psi|| for all phi, psi in H. Proof for b > a: |K_F| <= ||F|| K_1 and K_1 is the kernel of R^(b-a), which is >= 0 (`gap-transfer.md` 8.3); so |<phi, S_{K_F} psi>| <= ||F|| <|phi|, R^(b-a) |psi|> <= ||F|| lambda_0^(b-a) ||phi|| ||psi||. For b = a it is trivial.

(K2) <Omega, k_F Omega> = <F>_{L,inf} (`gap-transfer.md` (8a), and (6a) for b = a with F placed in a slab of length one; the two agree by the consistency in (8b)).

## 2. Step 1: the truncated correlation on the torus as a trace

**Lemma T (trace formula; PROVED GIVEN (TR) = `gap-transfer.md` (1.2), 1.3, A0(e), 6.1).** Let F, H be local functions on the torus L^3 x T with time ranges [a, b] and [a', b'], where 0 = a <= b < a' <= b' <= T - 1. Put d = a' - b >= 1 (the gap from F forward to H), d' = T - b' >= 1 (the gap from H forward, around the time circle, to F), so that d + d' + w(F) + w(H) = T. Then

<F H>_{L,T} = Tr(k_F Rn^d k_H Rn^(d')) / (1 + S(T; L^3)), with Rn := R / lambda_0,

and Tr(k_F Rn^d k_H Rn^(d')) = sum over i, j >= 0 of rho_i^d rho_j^(d') <phi_j, k_F phi_i> <phi_i, k_H phi_j>, an absolutely convergent double sum. Also <F>_{L,T} = Tr(k_F Rn^(T - w(F))) / (1 + S(T; L^3)) = (sum over j >= 0 of rho_j^(T - w(F)) <phi_j, k_F phi_j>) / (1 + S(T; L^3)).

Proof. By (1.2) of `gap-transfer.md`, e^(-S(U)) is the product over t in Z/T of T_0(U(t), g_t . U(t+1)). The time-like links g_t with b <= t < a' or b' <= t <= T - 1 are not arguments of F or H. Integrate them: each gives a factor A_T(U(t), U(t+1)) (1.3 there). Integrate the spatial slices strictly between b and a', and strictly between b' and T: this gives the kernels a_d(U(b), U(a')) and a_(d')(U(b'), U(0)) of R^d and R^(d') (A0(e): composition of kernels). Integrate the interior slices and the time-like links of the two slabs: by the definition of K_F and K_H this gives K_F(U(0), U(b)) and K_H(U(a'), U(b')); if b = a, the factor is F(U(0)) and there is no integration, and the same for H. All integrands are bounded and Fubini applies. What remains is the integral over four (or fewer) slices of K_F(u, v) a_d(v, x) K_H(x, y) a_(d')(y, u), with the obvious change when a slab has width 0 (the kernel K_F(u, v) is replaced by F(u) and v = u). The operator Y := S_{K_F} R^d S_{K_H} (or M_F R^d M_H, and the mixed cases) has a bounded kernel, since d >= 1, and R^(d') has the bounded kernel a_(d'). By A0(e) the integral is Tr(Y R^(d')). Dividing by Z_{L,T} = lambda_0^T (1 + S(T; L^3)) and using T = d + d' + w(F) + w(H) gives the first formula.

The eigenbasis form: R^(d') = sum_j lambda_j^(d') |phi_j><phi_j| vanishes on the orthogonal complement of the phi_j, so, as in 6.1 of `gap-transfer.md` (the trace of a product of two Hilbert-Schmidt operators may be taken in any orthonormal basis), Tr(Y R^(d')) = sum_j lambda_j^(d') <phi_j, Y phi_j>. Insert R^d = sum_i lambda_i^d |phi_i><phi_i| (norm convergent). Absolute convergence: by (K1), |<phi_j, k_F phi_i> <phi_i, k_H phi_j>| summed over i with weights rho_i^d <= 1 is at most ||k_F^* phi_j|| ||k_H phi_j|| <= ||F|| ||H|| (Cauchy-Schwarz and Bessel), and sum_j rho_j^(d') < infinity. The one-function formula is the case H = 1 of the same computation (it is 8.1, 8.2 of `gap-transfer.md`, which assume T - w(F) >= 2; this file uses the one-function formula only under that condition). QED

What t_0 is. Let A and B be local functions on Z^4 with time ranges [a_A, b_A] and [a_B, b_B], and let B_t be the translate of B by t in the time direction. Put t_0 := b_A - a_B. Then for t >= t_0 + 1 the pair F = A, H = B_t has d = t - t_0. For two functions of one time slice each (the same slice), t_0 = 0 and the formula is Tr(R^(T-t) A R^t B) / Tr R^T, the form in the row. For functions that are not in one slice, t_0 is the last time of A minus the first time of B, the widths enter T = d + d' + w(A) + w(B), and the multiplication operators are replaced by the slab operators k_A, k_B, which are not multiplication operators but satisfy the same norm bound (K1).

**Proposition C (four terms; PROVED GIVEN (TR)).** In the setting of Lemma T write f = <F>_{L,inf}, h = <H>_{L,inf}, S_T = S(T; L^3). Then

<F H>_{L,T} (1 + S_T) = f h + u + u' + v, where

- u = <k_F^* Omega, Rx^d k_H Omega> = <F H>_{L,inf} - f h, the truncated function on the cylinder, and |u| <= ||F|| ||H|| rho_1^d;
- u' = <k_H^* Omega, Rx^(d') k_F Omega>, the truncated function on the cylinder of the pair in the other order at distance d', and |u'| <= ||F|| ||H|| rho_1^(d');
- v = Tr(k_F Rx^d k_H Rx^(d')), and |v| <= ||F|| ||H|| min( rho_1^d S(d'; L^3), rho_1^(d') S(d; L^3) ).

Proof. Split the double sum of Lemma T into (i, j) = (0, 0); i >= 1, j = 0; i = 0, j >= 1; i, j >= 1. The first is <Omega, k_F Omega><Omega, k_H Omega> = f h by (K2). The second is sum_{i>=1} rho_i^d <k_F^* Omega, phi_i><phi_i, k_H Omega> = <k_F^* Omega, Rx^d k_H Omega>; its modulus is at most ||Rx^d|| ||k_F^* Omega|| ||k_H Omega|| <= rho_1^d ||F|| ||H|| by (K1); and it equals <FH>_{L,inf} - fh by 8.5 of `gap-transfer.md` (there K_{FH} = K_F R^d K_H). The third is the same with the roles exchanged. The fourth is sum_{j>=1} rho_j^(d') <phi_j, X phi_j> with X = k_F Rx^d k_H, ||X|| <= ||F|| rho_1^d ||H||, so its modulus is at most ||X|| S(d'; L^3). The trace is cyclic in the sense that the double sum is symmetric under the exchange (F, d, i) <-> (H, d', j); this gives the second bound of the minimum. QED

## 3. Step 2: the spectral bound with the thermal errors

**Theorem L1 (torus; PROVED GIVEN (TR)).** Let L >= 3, T >= 4, and let F, H be local functions on L^3 x T as in Lemma T, with T - w(F) >= 2 and T - w(H) >= 2. Let m = m(L^3). Then

| <F H>_{L,T} - <F>_{L,T} <H>_{L,T} | <= ||F|| ||H|| ( e^(-m d) + 6 S(d'; L^3) ),

and the same with d and d' exchanged. More precisely the left side is at most ||F|| ||H|| ( e^(-md) (1 + S(d')) + e^(-m d') + S(T) + S(T - w(F)) + S(T - w(H)) + S(T - w(F)) S(T - w(H)) ), all thermal sums for the cube L^3.

Proof. Scale to ||F|| = ||H|| = 1. By Lemma T, <F>_{L,T} = (f + alpha)/(1 + S_T) with alpha = sum_{j>=1} rho_j^(T - w(F)) <phi_j, k_F phi_j>, |alpha| <= S(T - w(F)) by (K1); likewise <H>_{L,T} = (h + gamma)/(1 + S_T), |gamma| <= S(T - w(H)). With N := f h + u + u' + v = <FH>_{L,T} (1 + S_T):

<FH> - <F><H> = [ N (1 + S_T) - (f + alpha)(h + gamma) ] / (1 + S_T)^2 = [ u + u' + v + S_T N - f gamma - alpha h - alpha gamma ] / (1 + S_T)^2.

Now |N| <= 1 + S_T because |<FH>_{L,T}| <= 1; |f|, |h| <= 1; and (1 + S_T)^2 >= 1. So the modulus is at most |u| + |u'| + |v| + S_T + |alpha| + |gamma| + |alpha||gamma|. Insert Proposition C: this is the precise form. For the short form put sigma = S(d'; L^3). Since T, T - w(F), T - w(H) are all >= d', fact (i) gives S_T, |alpha|, |gamma| <= sigma, and e^(-m d') = rho_1^(d') <= sigma by fact (ii). So the modulus is at most e^(-md)(1 + sigma) + 4 sigma + sigma^2. If sigma <= 1 this is at most e^(-md) + 6 sigma. If sigma > 1 the claim is trivial, because the left side is at most 2. QED

**Which time extents Hypothesis (G) covers.** (G1) bounds S(a; (L_k)^3) only for a >= n_k: by facts (i), (iii), S(a; (L_k)^3) <= s_k^(floor(a / n_k)) for a >= n_k. It gives nothing for a < n_k (below half the side). So Theorem L1 has a controlled error exactly when d' >= n_k, that is

(COV) T >= n_k + d + w(F) + w(H).

For T = infinity (the cylinder) there is no error (`gap-transfer.md` (8c)). For T < n_k + d + w(F) + w(H) the hypothesis gives no bound on the wrap-around terms u', v, alpha, gamma. On the symmetric torus T = L_k = 2 n_k, (COV) reads d + w(F) + w(H) <= n_k: separations up to half the time extent, minus the widths. By the exchange of d and d', separations with d >= n_k are covered too, with the roles reversed (the pair is then closer around the back of the circle, and the bound is e^(-m d') + 6 S(d)). Not covered on the symmetric torus: n_k - w(F) - w(H) < d < n_k.

**Theorem L2 (uniform in k; PROVED GIVEN (TR), (G)).** Assume (G). Let k >= 0, T >= n_k + 2, and let F, H be local functions on (L_k)^3 x T as in Lemma T with d' >= n_k. Then

| <F H> - <F> <H> | <= ||F|| ||H|| ( e^(-m_0 d) + 6 s_k^(floor(d'/n_k)) ) <= ||F|| ||H|| ( e^(-m_0 d) + (6/5041) e^(-m_0 n_k floor(d'/n_k)) ).

In particular, if also d <= n_k floor(d'/n_k) (on the symmetric torus T = L_k: if d <= n_k - w(F) - w(H)), then

| <F H> - <F> <H> | <= 1.002 ||F|| ||H|| e^(-m_0 d).

So on the symmetric tori (L_k)^4 the thermal error is not a separate term: it is at most 0.12 percent of the main term, for every k, every pair of local functions, and every separation that (COV) allows. C(A, B) of the row can be taken as 1.002 ||A|| ||B||, with t_0 = b_A - a_B.

Proof. Theorem L1 with m >= m_0 (G3), S(d'; (L_k)^3) <= s_k^(floor(d'/n_k)) (facts (i), (iii), (G1)), s_k = e^(-m_0 n_k)/5041 and s_k^j <= e^(-m_0 n_k j)/5041 for j >= 1. The conditions T - w >= 2 hold since T - w(F) >= d' + d >= n_k + 1 >= 4. QED

Remark (the error for one-point functions). The same computation gives, for T - w(F) >= 2: | <F>_{L,T} - <F>_{L,inf} | = |alpha - f S_T| / (1 + S_T) <= 2 ||F|| S(T - w(F); L^3). This is `gap-transfer.md` (8a) with the sum kept (as in `gap-os-equiv.md` (7c)) instead of the bound e^(12 beta N^3) e^(-m(T-w-1)), which is useless uniformly in the volume. It is used in Section 4.
