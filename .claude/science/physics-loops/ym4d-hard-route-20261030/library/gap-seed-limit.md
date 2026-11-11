lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T21:15Z

# gap-seed-limit: from the seed to exponential clustering in every limit state (row 700)

Author run at commit 547801e01, started 2026-11-11T09:15Z. Research-stage working state. **No mass gap is proved by this file.** Everything is conditional on Hypothesis (G) below, which is the conclusion of Theorem S of `library/gap-crux-restate.md` (row 697, not yet checked; checks are rows 698, 699). Nothing here is checked by a model that did not write it. No computer run was made for this file.

## Status block (kept current)

- Steps 1, 2 (torus bound with the thermal error): written, Sections 2, 3. PROVED GIVEN (TR).
- Steps 3, 4, 5 (limit states, clustering in all four directions, dependence on the sequence): written, Section 4. PROVED GIVEN (TR), (G), and for the Hilbert-space form `gap-os-equiv.md` (1), (3), Lemma E. One OPEN statement, (U).
- Step 6 (scaling form): written, Section 5. PROVED GIVEN Theorem S, Theorem L3, `gap-os-equiv.md` (5a)-(5c); the continuum datum is an OPEN input.
- Step 7 (converse): written, Section 6. PROVED: gap plus the state count (NS) with theta < 1 gives the seed; the seed gives (NS) with theta = 1. OPEN: (NS-gap). A uniform gap alone is not shown to give the seed.
- Final statement, inputs, open list: Section 7. File complete for this run (2026-11-11, 09:25Z). A self-check by the author was made after writing (constants, the identity of Section 6, the conditions of Lemma M); it is not an independent check.
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

## 4. Steps 3, 4, 5: limit states, clustering in all four directions, dependence on the sequence

### 4.1 Definitions

**Local functions on Z^4 and their versions on tori.** Let F be a local function on Z^4 (Section 1). On a torus L^3 x T, or cylinder, whose spatial side exceeds every spatial width of F by at least 2 and whose time extent exceeds the time width by at least 2, the quotient map Z^4 -> torus is injective on the end points of supp F, and F is read as a function on the torus. Its expectation does not depend on the position, because the torus state is invariant under translations (they permute links and plaquettes; `gap-transfer.md` (1c), last sentence, for time). I write <F>_{k,T} for the expectation on (L_k)^3 x T, T = inf for the cylinder.

**Admissible sequences.** A sequence (k_i, T_i), with T_i an integer or inf, is admissible if k_i -> infinity and T_i - n_(k_i) -> infinity. Examples: the symmetric tori T_i = L_(k_i) (then T_i - n_(k_i) = n_(k_i)); the cylinders T_i = inf (the volume limit taken after the time limit); tori of any shape with T_i >= (1 + c) n_(k_i), c > 0; long tori T_i = j_i L_(k_i).

**Limit state.** A limit state of an admissible sequence is a map nu from local functions to C with nu(F) = lim_i <F>_{k_i,T_i} for every local function F (bounded Borel, not only continuous).

### 4.2 Three lemmas

**Lemma FE (finite energy; PROVED).** On every torus with all sides >= 3, and on every cylinder, for a local function F with supp F = Gamma: |<F>| <= e^(12 beta |Gamma|) times the integral of |F| over G^Gamma with respect to the product Haar measure.

Proof. Let P be the set of plaquettes that contain a link of Gamma; |P| <= 6 |Gamma|, since a link of a four-dimensional lattice lies in 6 plaquettes. Write the action as S = S_P + S', S_P the sum over P. Each term beta (1 - (1/2) tr U_p) lies in [0, 2 beta], so 0 <= S_P <= 12 beta |Gamma|, and S' does not depend on the links of Gamma. Then |integral of F e^(-S)| <= (integral of |F| over G^Gamma)(integral of e^(-S') over the other links), and Z >= e^(-12 beta |Gamma|) (integral of e^(-S') over the other links), because the Haar measure of G^Gamma has mass one. Divide. The cylinder state is the limit T -> infinity of torus states on each local function (`gap-transfer.md` (8a)), so the bound passes to it. QED

**Lemma M (the time extent does not matter; PROVED GIVEN (TR), (G1)).** Let F be a local function with time width w, and let T, T' (integers or inf) satisfy T, T' >= n_k + w (and the fitting conditions of 4.1). Then | <F>_{k,T} - <F>_{k,T'} | <= 4 ||F|| s_k.

Proof. By the Remark at the end of Section 3, | <F>_{k,T} - <F>_{k,inf} | <= 2 ||F|| S(T - w; (L_k)^3) <= 2 ||F|| s_k, by fact (i) and (G1), since T - w >= n_k (and T - w >= 3 >= 2). The same for T'. QED

**Lemma RPc (the cylinder state is reflection positive at a site mirror; PROVED GIVEN `gap-transfer.md` (8b)).** On the cylinder L^3 x Z let theta be the reflection t -> -t: (theta U)(t) = U(-t) on spatial links and (theta g)_t = (g_(-t-1))^(-1) on time-like links (the link from (x,t) to (x,t+1) goes to the reverse of the link from (x,-t-1) to (x,-t)). For a local function F put (Theta F)(U) = F(theta U). Then for all local F, G with time ranges in [0, infinity): <conj(Theta F) G>_{L,inf} = <psi_F, psi_G> in L^2(X), where psi_G(u) = lambda_0^(-b) times the integral of G times the product over t = 0..b-1 of T_0(U(t), g_t . U(t+1)) times Omega(U(b)), over all slab variables except U(0) = u (b any integer with range of G inside [0, b]). In particular <conj(Theta F) F>_{L,inf} = ||psi_F||^2 >= 0.

Proof. Take b >= 1 that serves F and G. conj(Theta F) G is a function on the slab [-b, b], and by (8b) its expectation is the integral against lambda_0^(-2b) Omega(U(-b)) prod_{t=-b}^{b-1} T_0(U(t), g_t . U(t+1)) Omega(U(b)). For fixed U(0) = u the integrand is a product of a function of the variables at negative times and a function of those at positive times. The second factor integrates to psi_G(u). In the first substitute U'(t) = U(-t), g'_t = (g_(-t-1))^(-1) for t = 0, ..., b-1; this preserves the Haar measures (N.1 of `gap-transfer.md`). With t = -t'-1: T_0(U(t), g_t . U(t+1)) = T_0(U'(t'+1), (g'_(t'))^(-1) . U'(t')) = T_0(g'_(t') . U'(t'+1), U'(t')) = T_0(U'(t'), g'_(t') . U'(t'+1)), by the invariance T_0(h . a, h . b) = T_0(a, b) and the symmetry of T_0 (N.5, N.7 there). And conj(Theta F)(U) = conj(F(U', g')). So the first factor integrates to conj(psi_F(u)). Independence of b: (8b), consistency (it is the equation R Omega = lambda_0 Omega). QED

### 4.3 Theorem L3 (limit states)

**Theorem L3 (PROVED GIVEN (TR), (G); part (e) also given `gap-os-equiv.md` Statements (1), (3) and Lemma E).** Assume (G).

(a) Existence. Every admissible sequence has a subsequence with a limit state.

(b) Only the sizes matter. If nu is a limit state of the admissible sequence (k_i, T_i), then nu is the limit state of (k_i, T'_i) for every other choice of T'_i that keeps the sequence admissible. In particular nu is the limit of the symmetric tori (L_(k_i))^4 and of the cylinders (L_(k_i))^3 x Z, along the same k_i.

(c) Properties. nu is linear, positive (nu(F) >= 0 for F >= 0), nu(1) = 1, |nu(F)| <= ||F||, and nu obeys Lemma FE. nu is invariant under the translations of Z^4 and under the hypercubic group (signed permutations of the axes, acting on links, with the group element inverted where a link is reversed). nu is reflection positive at every site mirror x_mu = c.

(d) Clustering. Let F, H be local functions and mu one of the four directions, with mu-ranges [a, b] and [a', b'], d := a' - b >= 1. Then

| nu(F H) - nu(F) nu(H) | <= ||F|| ||H|| e^(-m_0 d).

So for A, B local and B_v the translate of B by v in Z^4: | nu(A B_v) - nu(A) nu(B) | <= ||A|| ||B|| e^(-m_0 (|v_mu| - t_0)) for each mu with |v_mu| > t_0, where t_0 is the maximum over the two orders of b_A - a_B, b_B - a_A in that direction. If supp A and supp B lie in the cube [-r, r]^4 and |v|_inf >= 2r + 1, the bound is ||A|| ||B|| e^(-m_0 (|v|_inf - 2r)), |v|_inf the largest |v_mu|. In the Euclidean distance the rate is at least m_0 / 2 (|v|_inf >= |v| / 2 in four dimensions); this file proves no better rate in diagonal directions.

(e) The gap of the limit state. Let V be the space of local functions with time range in [0, infinity), b(F, G) = nu(conj(Theta F) G), tau_t the time translation. This is a time-reflection datum in the sense of `gap-os-equiv.md` S.2 with (P1), (P2), (P3). Its Hilbert space has a unique vector invariant under time translation (the vacuum), and the transfer operator T_nu (translation by one time step) satisfies ||T_nu^t psi|| <= e^(-m_0 t) ||psi|| for every psi orthogonal to the vacuum: the spectrum of T_nu on the complement of the vacuum lies in [-e^(-m_0), e^(-m_0)]. The same holds for each of the four directions.

Proof. (a) Step 1: for a finite link set Gamma, C(G^Gamma) has a countable sup-norm dense subset. G^Gamma is a compact metric space, with metric dist. For each integer r >= 1 take a finite set x_1, ..., x_N with every point within 1/r of some x_j (compactness), put p_j(x) = max(0, 2/r - dist(x, x_j)), and q_j = p_j / (sum_l p_l); the sum is >= 1/r everywhere. For f continuous, |f(x) - sum_j f(x_j) q_j(x)| <= sum_j |f(x) - f(x_j)| q_j(x) <= the modulus of continuity of f at 2/r, because q_j(x) = 0 unless dist(x, x_j) < 2/r. The modulus tends to 0 (uniform continuity). So the combinations of the q_j (all r) with coefficients in Q + iQ are dense. Step 2: there are countably many finite Gamma. Let D be the union of the countable dense sets. For each F in D the numbers <F>_{k_i,T_i} are bounded by ||F||. By the diagonal choice there is a subsequence along which all of them converge. Step 3: for F in C(G^Gamma) and eps > 0 take F' in D with ||F - F'|| < eps; then the limsup minus the liminf of <F>_i is at most 2 eps. So <F>_i converges. Step 4: for F bounded Borel on G^Gamma and eps > 0 take F' continuous with the Haar integral of |F - F'| below eps (continuous functions are dense in L^2 of a Borel probability measure on a compact metric space, Lemma A4 of `gap-transfer.md`, and the L^1 norm is at most the L^2 norm). By Lemma FE, |<F>_i - <F'>_i| <= e^(12 beta |Gamma|) eps for every i. So <F>_i converges. This defines nu on all local functions. (The fitting conditions of 4.1 hold for all large i, since L_(k_i) and T_i tend to infinity.)

(b) For F with time width w and i large enough that T_i, T'_i >= n_(k_i) + w: Lemma M gives |<F>_{k_i,T_i} - <F>_{k_i,T'_i}| <= 4 ||F|| s_(k_i), which tends to 0 because k_i -> infinity and s_k = q^(2^k)/5041.

(c) Linearity, positivity, normalization and the bound by ||F|| hold for each member and pass to the limit; so does Lemma FE. Translations: each member is invariant under the translations of its torus, and a translate of a local function is local. Hypercubic group: by (b), nu is the limit of the states on (L_(k_i))^4. A signed permutation of the axes acts on the torus (L)^4, permutes the links up to orientation, and maps plaquettes to plaquettes; reversing a link inverts its variable, which preserves the Haar measure, and the plaquette term depends only on tr U_p, which is invariant under inversion and conjugation (N.1, N.2 of `gap-transfer.md`). So the state on (L)^4 is invariant, and nu is. Reflection positivity at the time mirror t = 0: by (b), nu is the limit of the cylinder states, which are reflection positive by Lemma RPc, and nu(conj(Theta F) F) is a limit of non-negative numbers. Other time mirrors: translation. Other directions: hypercubic invariance.

(d) Time direction first. By (b) use the symmetric tori T_i = L_(k_i) = 2 n_(k_i). For large i, d + w(F) + w(H) <= n_(k_i), so Theorem L2 gives |<FH>_i - <F>_i <H>_i| <= ||F|| ||H|| (e^(-m_0 d) + 6 s_(k_i)). Let i -> infinity: FH, F, H are local functions, the three expectations converge, and s_(k_i) -> 0. For a space direction mu: let g be the exchange of the axes mu and 4. On (L_(k_i))^4, <FH> = <(g.F)(g.H)> and <F> = <g.F>, <H> = <g.H> by the invariance in (c); g.F and g.H are local functions whose time ranges are the mu-ranges of F and H, with the same sup norms, and the spatial cube of the torus is again (L_(k_i))^3. Apply the time case. (This is where the symmetric tori are used: on them each of the four directions is a time direction with the same operator.) The translate form: if v_mu > t_0 use the order (A, B_v) with d = v_mu - (b_A - a_B); if v_mu < -t_0 use the order (B_v, A). The cube form: both mu-ranges lie in [-r, r] before translation, so d >= |v_mu| - 2r; choose mu with |v_mu| = |v|_inf >= 2r + 1, so that d >= 1.

(e) (P1) is (c). (P2): nu(conj(Theta F) tau_t G) = nu(tau_(-t)[conj(Theta F) tau_t G]) = nu(conj(Theta tau_t F) G) by translation invariance and Theta tau_t = tau_(-t) Theta. (P3): |b(tau_t F, tau_t F)| <= ||F||^2. The unit is the constant 1. Decay on the whole of V: for F in V with time range [a, b], a >= 0, and t >= 1, the function conj(Theta F) has time range [-b, -a] and tau_t F has [a + t, b + t], so d = t + 2a >= 1 and by (d): u(F, F; t) = nu(conj(Theta F) tau_t F) - |nu(F)|^2 <= ||F||^2 e^(-m_0 t). (Here nu(conj(Theta F)) = conj(nu(F)): the reflection t -> -t is an element of the hypercubic group, and its action on links is the theta of Lemma RPc.) This is hypothesis (X_m^C) of `gap-os-equiv.md` Statement (3) with C = V, C_F = ||F||^2, t_F = 1, m = m_0. The class V is total by construction. Statement (3b) and Lemma E (E1, E3) there give the claim. QED

### 4.4 Step 5: does the limit depend on the sequence?

What is proved (Theorem L3 (b)): the limit does not depend on the time extents, as long as T_i - n_(k_i) -> infinity. The time limit and the volume limit can be taken in either order or together, and every limit state is at once a limit of symmetric tori and of cylinders.

What is not proved: that the limit does not depend on the subsequence of sizes k_i. Hypothesis (G) compares no two sizes. So the theorem is stated for every limit state. Each limit state has the same rate m_0 and the same constant.

**OPEN (U), one exact statement.** For every continuous local function F, the sequence <F>_{(L_k)^4}, k = 0, 1, 2, ..., converges.

Remarks, not proofs. (1) Each limit state clusters, so each is a pure phase in the sense of Theorem L3 (e): one vacuum. Two different limit states along two subsequences of sizes are not excluded by anything here. (2) (G) is a statement about the cubes of side 2^(k+1) n only. Cubes of other sides are not covered (Corollary S3 of `gap-crux-restate.md` would cover them from seeds on a block of sizes). So "the" infinite-volume limit over all tori is not addressed at all. (3) Whether a limit state satisfies the Dobrushin-Lanford-Ruelle equations is not needed here and not proved here (it would follow from Lemma FE and the locality of the action by a standard argument, not written).

### 4.5 Step 4, the record of what was asked

Clustering in a space direction for the limit states of step 3 follows (Theorem L3 (d)), for every admissible sequence, not only for the symmetric tori. Nothing is missing. The mechanism: Lemma M moves any admissible sequence to the symmetric tori at a cost 4 ||F|| s_k, and there the exchange of two axes is a symmetry. On a finite torus (L_k)^3 x T with T different from L_k the same holds with an error: for F, H separated by d in a space direction, with time width w <= n_k of the product FH and T >= n_k + w, d + (the widths of F and H in that space direction) <= n_k,

| <FH>_{k,T} - <F>_{k,T} <H>_{k,T} | <= ||F|| ||H|| (1.002 e^(-m_0 d) + 12 s_k)

(Lemma M three times: 4 s_k for <FH>, and 4 s_k + 4 s_k for the product of the one-point functions; then Theorem L2 on (L_k)^4).

## 5. Step 6: the scaling form (a conditional statement; inputs named)

**Setting.** A family of cutoffs, indexed by iota: a coupling beta_iota > 0 and a lattice spacing a_iota > 0 (a positive number attached to the lattice at beta_iota; how the unit of length is fixed is not used). Lengths in physical units are lattice lengths times a_iota.

**(SEED-phys), the hypothesis.** There are ell_* > 0 and s_* < 1/5041 such that for every iota there is an integer n_iota >= 3 with n_iota a_iota <= ell_* and S_{beta_iota}(n_iota; (2 n_iota)^3) <= s_*. In words: on a periodic cube of physical side at most 2 ell_*, at a time of half the side, the thermal sum of the excited states is at most s_*, uniformly in the cutoff. By Theorem D (b) of `gap-crux-restate.md` it suffices that Phi_{beta_iota}(n_iota) = 16 F(n,n,n,n) - F(2n,2n,2n,2n) <= 1.9 x 10^(-4) at n = n_iota.

**Proposition P (PROVED GIVEN Theorem S of row 697, which turns the seed into (G) at each iota, and Theorem L3).** Assume (SEED-phys). Put M_* := log(1 / (5041 s_*)) / ell_*. Then for every iota, with the sizes n_k = 2^k n_iota:

(a) every cube of side 2^(k+1) n_iota has lattice gap at least m_0(iota) = log(1/(5041 s_iota))/n_iota >= M_* a_iota, s_iota the seed value; in physical units the gap is at least M_*;

(b) every limit state nu of an admissible sequence at the cutoff iota satisfies | nu(FH) - nu(F) nu(H) | <= ||F|| ||H|| e^(-M_* x) for local functions F, H separated in a coordinate direction by the physical distance x = d a_iota, d >= 1;

(c) the transfer operator of nu satisfies ||T_nu^t psi|| <= e^(-M_* (t a_iota)) ||psi|| on the complement of the vacuum.

Rate and constant do not depend on the cutoff. Proof: m_0(iota) = log(1/(5041 s_iota))/n_iota >= log(1/(5041 s_*))/n_iota = M_* ell_* / n_iota >= M_* a_iota. Then Theorem L3 (d), (e). QED

**What (b) and (c) are worth in a continuum limit.** The sup norms in (b) are useless for renormalized observables (their sup norms grow with the cutoff). The form that survives is (c), whose constant is the reflection-positivity norm of the vector. So:

**Proposition P' (PROVED GIVEN Proposition P and `gap-os-equiv.md` Statement (5a)-(5c), which its check confirms; the failing sentence of its (5d) is not used).** Let iota_j be a sequence of cutoffs with a_(iota_j) -> 0, nu_j limit states as in (b), and let D_inf be a continuum time-reflection datum with (P1)-(P3) and a class C of observables with: (H2) for each F in C the diagonal truncated reflected functions of the lattice versions of F converge at each time t > 0 in the sense of (H2) there; (TOT) the vacuum and the vectors of C are total in the Hilbert space of D_inf. Then D_inf has a unique vacuum and, with time continuity (P4), spec(H) lies in {0} union [M_*, infinity).

Proof. (H1) there holds with m_n = M_* for every member (Proposition P (c), in the time unit a_(iota_j), with the sector equal to the whole complement of the vacuum). Apply (5a)-(5c). QED

**Inputs of the scaling form, in order.** (1) (SEED-phys): OPEN, the crux; this file does not try it. (2) Theorem S: row 697, under check (rows 698, 699). (3) (TR) and `gap-os-equiv.md` (1), (3), (5a-c), Lemma E: checked, HOLDS. (4) Existence of the continuum datum, (H2) and (TOT): the T0 chain; OPEN (the existence account is conditional, and its observable class is the tr(F^2) sector only, `gap-skeleton-max-b.md` 0.1, 0.4). (5) Compatibility of the sequences: the account's volume-first limits use tori of side 2 L^m with its own L. They are limit states in the sense of Section 4 only if those sides are among the 2^(k+1) n_iota, for example if L is a power of 2 and n_iota is a power of 2. Not verified here: I did not read which L the account fixes. If the sides do not match, seeds on a block of sizes are needed (Corollary S3 of row 697).

**The rate filter, in this form (PROVED, two lines).** If the seed holds at (n, s) then s >= S(n; (2n)^3) >= e^(-n m), m the true gap of the cube of side 2n. So n >= log(1/s)/m > log(5041)/m > 8.5/m, and m_0 = log(1/(5041 s))/n <= m - log(5041)/n. So the seed can only hold at a size of more than 8.5 correlation lengths of the cube (the cube has side more than 17 correlation lengths), and the rate that it gives is below the true one by more than 8.5/n (log 5041 = 2 log 71, and 4.26 < log 71 < 4.27). In physical units: ell_* > 8.5 / M and M_* <= M - 8.5/ell_*. The loss tends to 0 as the seed size grows, if the seed still holds there.

## 6. Step 7: the converse question

Question: does a uniform gap on the cubes, with a bound on the number of states, give the seed at some size?

Notation. For the cube of side L: E_j := log(lambda_0/lambda_j) = -log rho_j for j >= 1 (0 < E_1 <= E_2 <= ..., E_j -> infinity), and N_L(E) := the number of j >= 1 with E_j <= E. It is finite for each E because R is compact.

**Proposition N1 (the seed bounds the number of states; PROVED; this is Theorem D (d) of row 697 in the present notation).** For every a >= 1 and E: N_L(E) <= e^(aE) S(a; L^3). So under (G), for every k and E: N_(L_k)(E) <= s_k e^(n_k E) = e^(n_k (E - m_0)) / 5041. Proof: each j with E_j <= E contributes rho_j^a >= e^(-aE) to S(a). QED

In words: under the seed, the cube of side L has no state below m_0, and the number of states below E grows at most like e^((L/2)(E - m_0)).

**Proposition N2 (gap and a state count give the seed; PROVED).** Let n >= 3, let the cube of side 2n have gap E_1 >= m > 0, and let there be A > 0 and theta in [0, 1) with

(NS) N_(2n)(E) <= A e^(theta n E) for all E >= m.

Then S(n; (2n)^3) <= A e^(-(1 - theta) n m) / (1 - theta). So the seed holds at n if A e^(-(1 - theta) n m) < (1 - theta)/5041.

Proof. For each j >= 1, e^(-n E_j) = n times the integral of e^(-nE) over E >= E_j. Sum over j; all terms are positive, so the sum and the integral may be exchanged: S(n; (2n)^3) = n times the integral over E >= m of N_(2n)(E) e^(-nE) dE (N vanishes below m). Insert (NS): at most A n times the integral over E >= m of e^(-(1-theta) n E) dE = A e^(-(1-theta) n m)/(1 - theta). QED

**Corollary N3 (PROVED).** Let the cubes of side 2n, for n in an infinite set I, have gaps at least m > 0, and let (NS) hold on each with one theta < 1 and constants A_n with liminf over n in I of (log A_n)/n < (1 - theta) m. Then the seed holds at some n in I, and with it (G) from that size on (given Theorem S).

**Answer.** Yes, with a state count of the form (NS) with theta strictly below 1; and this is close to exact, because the seed itself gives (NS) with theta = 1 and A = s < 1/5041 (Proposition N1). In one line: for every n and every theta in [0, 1),

sup over E of N(E) e^(-nE) <= S(n; (2n)^3) <= (1/(1 - theta)) e^(-(1-theta) n m) sup over E >= m of N(E) e^(-theta n E).

A uniform gap alone does not give the seed by any argument in this file: the gap is a statement about E_1, the seed is a statement about all E_j, and the two are tied only through N. I have no example of a lattice gauge theory with a uniform gap on cubes and no seed at any size, and I do not claim one exists.

**OPEN (NS-gap), the exact extra bound.** For the SU(2) Wilson theory at the given beta: if the cubes of side 2n, n in an infinite set, have gaps at least m > 0, then there are theta < 1 and constants A_n with (NS) and liminf (log A_n)/n < (1 - theta) m.

Guide, not a proof: for a gas of free particles of mass m in the cube of side 2n, log N(E) is at most of the order (n^3 E^3)^(1/4) + log(n^3) for E >= m, which is below theta n E + C(theta) for every theta > 0. So (NS) is what a particle picture gives with a large margin; what is missing is any proof of a bound on the number of states of the Wilson transfer operator in a large cube beyond the trace bound Tr R / lambda_0 <= e^(12 beta L^3) of `gap-transfer.md` 6.3, which is (NS) with theta = 0 and log A of the order n^3, and that is too weak by the power n^2.

**A second exact form of the seed (PROVED GIVEN Lemma X of row 697, unchecked).** Fix the two sides (2n, 2n) of the directions 3, 4 and use the notation of Section 3.4 there: kappa(b) is the deficit of the ground-state energy of the box (b, 2n, 2n), and g(a, b) = log(1 + S(a; (b, 2n, 2n))). Lemma X with a = n, b = 2n reads

log(1 + S(n; (2n)^3)) = 2n kappa(n) - n kappa(2n) + log(1 + S(2n; (n, 2n, 2n))).

So the seed at n holds if and only if the right side is below log(1 + 1/5041). Both parts are finite-size effects of the box (n, 2n, 2n) with one short side: the first is a difference of ground-state deficits (0 <= 2n kappa(n) - n kappa(2n) <= 2n kappa(n)), the second is its thermal sum at the long time 2n. A uniform gap controls neither: the first is about lambda_0 only, and the second needs the thermal sum at some earlier time. This names the two quantities a proof of the converse would have to bound; it is not used in the theorem below.

## 7. The conditional theorem, its inputs, and what is open

**Theorem L ((SEED) gives exponential clustering in every limit state).** SU(2), Wilson action, four dimensions, beta > 0 fixed. Let n >= 3 be an integer and assume

(SEED) s := S(n; (2n)^3) < 1/5041,

where S(a; L^3) is the sum over the excited eigenvalues lambda_j, j >= 1, of the transfer operator of the periodic cube of side L, of (lambda_j / lambda_0)^a. (It suffices that 16 log Z(n,n,n,n) - log Z(2n,2n,2n,2n) <= 1.9 x 10^(-4).) Put m_0 = log(1/(5041 s))/n > 0, n_k = 2^k n, L_k = 2 n_k, s_k = (5041 s)^(2^k)/5041 = e^(-m_0 n_k)/5041. Then:

1. (Cubes; this is Theorem S, the input (G).) For every k >= 0: S(n_k; (L_k)^3) <= s_k, and the transfer operator of the cube of side L_k has a simple top eigenvalue and gap at least m_0.

2. (Tori.) Let F, H be bounded Borel functions of finitely many links of the torus (L_k)^3 x T, gauge invariant or not, with time ranges [a, b] and [a', b'], d = a' - b >= 1, and let d' = T - (b' - a) be the gap around the back of the time circle. If d' >= n_k, then
| <F H> - <F><H> | <= ||F|| ||H|| ( e^(-m_0 d) + 6 s_k^(floor(d'/n_k)) ),
and if moreover d <= n_k floor(d'/n_k), the right side is at most 1.002 ||F|| ||H|| e^(-m_0 d). On the symmetric torus (L_k)^4 this holds in each of the four directions, for d + (the two widths in that direction) <= n_k. The hypothesis gives no bound when d' < n_k. On the cylinder (T infinite) the bound is ||F|| ||H|| e^(-m_0 d), with no condition.

3. (Limit states.) Let k_i -> infinity and T_i - n_(k_i) -> infinity (T_i infinite allowed). A subsequence of the states on (L_(k_i))^3 x T_i converges on every bounded Borel function of finitely many links of Z^4. Every such limit nu depends on the k_i only, not on the T_i; it is invariant under translations and the hypercubic group, reflection positive at site mirrors, and

| nu(F H) - nu(F) nu(H) | <= ||F|| ||H|| e^(-m_0 d)

whenever F and H are separated by d >= 1 in one of the four coordinate directions. In its reflection-positivity Hilbert space the vacuum is unique and the transfer operator has norm at most e^(-m_0) on the complement of the vacuum, in each direction.

4. (Scaling.) If (SEED) holds for a family of cutoffs with n a <= ell_* and s <= s_* < 1/5041, the rate in physical units is at least log(1/(5041 s_*))/ell_*, uniformly in the cutoff, and it passes to every continuum limit in the sense of Proposition P'.

**Where each part is proved.** 1: not here (row 697). 2: Theorems L1, L2 (Section 3), and Section 4.5 for space directions. 3: Theorem L3 (Section 4). 4: Propositions P, P' (Section 5).

**Inputs.**

| Input | What it is | Status |
|---|---|---|
| (SEED) | the inequality at one size | OPEN; the crux; not attempted here (row 701 treats strong coupling) |
| Theorem S | (SEED) gives (G) | row 697, PROVED there, not yet checked (rows 698, 699). Parts 2 to 4 use only its conclusion (G); if its proof is corrected and the conclusion changes only in constants, replace 5041 and the exponent accordingly |
| (TR) | `gap-transfer.md` (1.2), 1.3, (1) to (5), 6.1, (8a)-(8c), Lemmas A0, A4 | checked, HOLDS (`gap-transfer-check.md`); (8e), Kolmogorov extension, is not used: limit states are functionals on local functions |
| os-equiv | `gap-os-equiv.md` (1), (3), Lemma E; (5a)-(5c) for Proposition P' | checked, HOLDS for these parts |
| Proved here | Lemma T, Proposition C, Theorems L1, L2, Lemmas FE, M, RPc, Theorem L3, Propositions P, N1, N2 | PROVED, unchecked |
| Continuum datum | existence, (H2), (TOT) for Proposition P' | OPEN (the T0 chain) |

**Open, each one exact statement.**

- (SEED) at one n >= 3 for the given beta (or (SEED-phys) uniformly in the cutoff).
- (U): convergence of <F>_{(L_k)^4} in k for every continuous local F. Without it the theorem speaks of every limit point.
- (NS-gap): the state count that would give the converse (Section 6).
- Sizes other than 2^(k+1) n are not covered by (G).
- Time extents with d' < n_k (a pair separated by nearly half the time circle, within the widths) are not covered.
- Diagonal directions: the rate proved in Euclidean distance is m_0/2, not m_0.

**What this file does not show.** It proves no mass gap: (SEED) is not proved at any coupling here. It does not show that the limit state is unique, that it is a Gibbs state, or anything about a continuum limit beyond the conditional Proposition P'.

**For the checker, the places most likely to hide an error.** (1) Lemma T: the bookkeeping of d, d', the widths, and the case of width 0. (2) Theorem L1: the algebra of the truncation with the denominator 1 + S_T, and the claim that the bound is trivial when S(d') > 1. (3) Lemma M and Theorem L3 (b): that 4 ||F|| s_k needs only T - w >= n_k. (4) Lemma RPc: the change of variables on the time-like links. (5) Theorem L3 (e): that the datum meets (P1)-(P3) of `gap-os-equiv.md` as a functional on local functions, with no measure on the infinite lattice. (6) Proposition N2: the exchange of sum and integral.
