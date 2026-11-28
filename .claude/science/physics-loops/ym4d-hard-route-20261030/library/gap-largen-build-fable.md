lead: anthropic/claude-fable-5-2 laptop subagent
Started Sat Nov 28 17:34:14 UTC 2026, pinned at commit 2a12f2296. Author only, checked by no one.

# A large-N mass-gap theorem for 4D lattice gauge theory: build (FINISH row 1708)

## 0. Plan (written first; steps are filled in below as they are done)

1. Read the crux card and the RESULT texts of rows 1702, 1706, 1707.
2. Choose the mechanism and the group. State the theorem with all quantifiers.
3. Write the proof as a chain of lemmas.
4. Prove the first lemma in full, then as many more as possible.
5. Name the one estimate that spends N. Prove it or reduce it to one lemma.
6. Say what replaces the auxiliary-field saddle; say how U(1) and N = 2 fail.
7. Say what the theorem gives toward SU(2).
8. RESULT line.

## 1. Verdict first

No large-N mass-gap theorem at order-one coupling is proved in this file. The file builds the frame of one, proves its first lemma and three further statements, and reduces the rest to two named estimates. One of my own first designs failed a test that I ran on it (Proposition N, section 6). The failure is recorded, because it fixes what the estimate that spends N must be.

What is built, with status:

| Item | Statement | Status |
|---|---|---|
| Lemma 1 | Edge loop equation for SU(N), with the two terms that separate SU(N) from U(N) | PROVED (section 3); four instances checked on SU(3) by quadrature (floats, guide only) |
| Lemma 2 | Same-norm stability of the planar loop operator is an open condition in beta, with an explicit step | PROVED (section 5); not proved for a tame pair of norms |
| Theorem Q | Tame planar stability (TPS) gives clustering at rate m down to a floor, uniform in the volume and in the boundary condition | PROVED as an implication (section 5). The hypothesis TPS is not proved at any beta |
| Proposition N | On the sector of n-fold windings of one plaquette the split term amplifies by at least n in any one sup norm | PROVED at beta = 0, N = infinity, for that sector (section 6); the failure of TPS itself with a' = a is ARGUED |
| Squeeze | The linear loop-sequence method cannot pass beta of about 0.6 (one-plaquette normalisation, transition at 1) | ARGUED from one sector (section 6) |
| (LD) | Local large-deviation bound at speed N^2: the estimate that spends N | STATED, OPEN (section 7) |
| (PS) | Stability of the linearised planar loop equation at the master field: the estimate that passes order-one coupling | STATED, OPEN beyond small beta (section 7) |
| Theorem T | (LD) and (PS) give a mass gap for N >= N0 | ARGUED architecture only (section 7) |

## 2. Setting and choice of group

Lattice Z^4. Links e carry U_e in G = SU(N). Wilson law with 't Hooft scaling, in a finite set of links Lambda with any fixed values on the other links:

  d mu(U) = Z^-1 exp( N beta sum_p Re Tr U_p ) prod_{e in Lambda} dU_e ,   beta = 2/lambda, lambda = g^2 N.

tr = (1/N) Tr. A loop l is a closed word in the oriented links (no reduction of backtracks). A loop sequence s = (l_1,...,l_k) is a finite multiset of nonempty loops; an empty word is dropped (tr 1 = 1). phi(s) = E prod_i tr U_{l_i}; |phi| <= 1; phi(empty) = 1. |s| is the total length. For a link e: n_e(s) is the number of occurrences of e or e^-1 in s; t_e(s) = #(e) - #(e^-1) is the net current. n_*(s) is the least positive n_e(s). r(s) is the largest sup-norm distance of a site of s from the origin.

Why SU(N) and not U(N) (ARGUED). U(N) has a U(1) factor. The Ricci curvature of U(N) is zero in that direction. A minimal U(1) monopole of U(N) winds one eigenvalue and costs an action of order N beta f, so for large N at weak 't Hooft coupling the U(1) factor is expected to be in a Coulomb phase with a massless photon (compare Guth 1980 and Froehlich-Spencer 1982 for U(1); from memory, UNVERIFIED). So the target statement is expected to be false for U(N) at weak coupling. The choice is SU(N). SO(N) is not treated.

Known in kind (my memory, UNVERIFIED by me; the reading row 1710, library/prior/gap-largen-lit-luna.md, reports the same from a full read: Shen-Zhu-Zhu, arXiv:2204.12737, Theorem 1.1 and Corollary 1.5): a mass gap uniformly in N for SU(N) by the Bakry-Emery criterion for |beta| < 1/(16(d-1)) = 1/48 in d = 4, in that paper's 't Hooft convention (I did not match conventions). Chatterjee (2019), Chatterjee-Jafarov and Jafarov (SU(N)) prove the 1/N expansion of Wilson loops at small beta from the master loop equation. "Beyond strong coupling" below means: beyond any range reached by a contraction estimate of these two kinds.

A fact that bounds every Wilson-action large-N theorem (physics record, numerical, UNVERIFIED): for N at least about 5 the 4D Wilson action has a first-order bulk transition at an order-one beta. At that beta two planar states coexist. A uniform-in-N theorem therefore cannot cover one connected beta interval that contains it; N0(beta) must diverge there. The continuum branch is the weak side. A theorem there cannot be an analytic continuation of the strong-coupling expansion; it must expand about the weak-side planar state.

## 3. Lemma 1 (edge loop equation for SU(N)). PROVED

Notation. Fix a link e that is integrated in mu, and a sequence s. An occurrence x of e in s has sign eps_x = +1 (e) or -1 (e^-1). The 2(d-1) = 6 plaquettes that contain e are each written as a word p that starts with e.
- split_{xy}(s), for x != y in the same loop: if eps_x = eps_y, the loop e A e B is replaced by the two loops (e A), (e B). If eps_x = -eps_y, the loop e A e^-1 B is replaced by (A), (B).
- merge_{xy}(s), for x, y in different loops: (e A), (e B) become (e A e B); (e A), (e^-1 B) become (A B).
- s (+)_x p and s (-)_x p: the word p, or p^-1, is inserted at the occurrence x (before e, or after e^-1).
- (s, p): the plaquette p is added as a new loop.

**Lemma 1.** For every finite Lambda, every boundary condition, every integrated link e whose six plaquettes are in the action, and every s:

  n_e phi(s) = (t_e^2 / N^2) phi(s)
        - sum_{x != y, same loop} eps_x eps_y phi(split_{xy} s)
        - N^-2 sum_{x, y, different loops} eps_x eps_y phi(merge_{xy} s)
        + (beta/2) sum_x eps_x sum_{p contains e} [ phi(s (-)_x p) - phi(s (+)_x p) ]
        + (beta/2) t_e sum_{p contains e} [ phi(s, p) - phi(s, p^-1) ] .        (SD)

For U(N) the first term and the last term are absent.

Proof. Let T_a (a = 1..N^2-1) be a basis of su(N) with Tr(T_a T_b) = -delta_ab, and let d_a f(U) = d/dt f(exp(t T_a) U_e) at t = 0. Haar measure is left invariant, so for smooth f, E_Haar[d_a f] = 0. Take f = (d_a W) exp(S), with W = prod_i Tr U_{l_i} = N^k prod tr and S = N beta sum_p Re Tr U_p, and sum on a:

  E[ sum_a d_a d_a W ] = - E[ sum_a (d_a W)(d_a S) ].                      (1)

The completeness relation of su(N) is sum_a (T_a)_{ij} (T_a)_{kl} = - delta_il delta_jk + (1/N) delta_ij delta_kl. It gives

  sum_a T_a T_a = -(N - 1/N),  sum_a Tr(T_a A T_a B) = -Tr A Tr B + (1/N) Tr(AB),  sum_a Tr(T_a A) Tr(T_a B) = -Tr(AB) + (1/N) Tr A Tr B.   (2)

d_a acts on an occurrence U_e by inserting T_a before it, and on U_e^-1 by inserting -T_a after it. So d_a W = sum_x eps_x W[T_a at x], and sum_a d_a d_a W is a sum over ordered pairs (x, y). The pairs x = y give -(N - 1/N) n_e W. A pair x != y in one loop gives, by (2), eps_x eps_y ( - W_split + (1/N) W ); for opposite signs the two letters e, e^-1 cancel by cyclicity, which is the stated split. A pair in two loops gives eps_x eps_y ( - W_merge + (1/N) W ). The terms in 1/N add to (1/N) (sum_x eps_x)^2 W = (t_e^2/N) W. So

  sum_a d_a d_a W = - N n_e W + (t_e^2/N) W - sum_{same loop} eps eps W_split - sum_{different loops} eps eps W_merge.    (3)

Next, Re Tr U_p = (Tr U_p + Tr U_p^-1)/2 and d_a Tr U_p^-1 = -Tr(T_a U_p^-1), so d_a S = (N beta/2) sum_p [ Tr(T_a U_p) - Tr(T_a U_p^-1) ]. With (2), for the loop L that carries x (rotated so that T_a is first),

  sum_a Tr(T_a U_L) [ Tr(T_a U_p) - Tr(T_a U_p^-1) ] = - Tr(U_L U_p) + Tr(U_L U_p^-1) + (1/N) Tr U_L ( Tr U_p - Tr U_p^-1 ).   (4)

W_split has k+1 traces, W_merge has k-1, and the last term of (4) has k+1. Divide (1) by N^(k+1) and use (3), (4):

  - n_e phi + (t_e^2/N^2) phi - sum eps eps phi(split) - N^-2 sum eps eps phi(merge)
     = - (beta/2) sum_x eps_x sum_p [ - phi(s (+)_x p) + phi(s (-)_x p) ] - (beta/2) t_e sum_p [ phi(s,p) - phi(s,p^-1) ].

This is (SD). For U(N) the term (1/N) delta_ij delta_kl in the completeness relation is absent, so the t_e^2 term and the last term are absent. QED.

Checks. (a) N = 1: phi = 1, and (SD) reads n = t^2 - (t^2 - n). PROVED. (b) SU(2), one free plaquette V (d = 2, plaquettes independent), s = (p): (SD) reads (3/4) E cos(theta) = beta E sin^2(theta) under the density sin^2(theta) exp(4 beta cos theta); this follows from d/dtheta [ sin^3(theta) exp(4 beta cos theta) ]. PROVED. (c) SU(3), one free plaquette, s = (p), (p^2), (p,p), (p,p^-1): the four residuals of (SD) are below 3e-14 at beta = 0.3, 0.9, 2.0 by a 240 x 240 Weyl quadrature (python3 -I, floats, guide only). Instance (p,p) exercises the merger and the term t^2/N^2; instances (p) and (p,p) exercise the last term. The equation is in the literature in summed form (Chatterjee-Jafarov, Jafarov; from memory, UNVERIFIED); this proof does not use it.

**What the two extra terms are.** The last term of (SD) couples every loop that carries net current t_e to Im tr U_p, the trace part of the field strength at e. It is of order one, not of order 1/N^2. It vanishes on a factorised charge-conjugation-even state, so SU(N) and U(N) have the same planar Wilson loops; but as a linear operator on the odd sector it is of order one. It is the only place where the leading-order loop equations read the U(1) factor. For N = 2 all traces are real and the term is zero.

## 4. What replaces the auxiliary-field saddle

In the vector models the spins are integrated exactly; the auxiliary field sigma has action N S(sigma); the saddle is one number (the mass) from one gap equation; the Hessian of S at the saddle is an explicit kernel with exponential decay; large fields cost exp(-c N).

For a gauge field no auxiliary field with fewer than N^2 components per link exists (ARGUED: the Lagrange multiplier of U U^* = 1 is an N x N matrix, and the plaquette term is quartic). The replacement is:

| Vector model | Gauge model |
|---|---|
| auxiliary field sigma_x | the family of normalised loop variables tr U_l, l in a block |
| action N S(sigma) | a rate function N^2 I on loop data. It is not explicit. Its existence with a uniform bound is the estimate (LD) |
| saddle sigma = m^2 from the gap equation | the master field W_beta: the translation-invariant, positive solution of the planar equation W = F_beta(W), where F_beta is (SD) at N = infinity on factorised states |
| Hessian of S at the saddle, massive | the linearised planar operator 1 - DF_beta(W_beta) on a weighted loop space. Its bounded inverse with exponential weights is the estimate (PS) |
| 1/N vertices | the merger term and the t_e^2 term of (SD), both with factor N^-2 |

The main difference: the gap equation of the vector model is solved in closed form for every beta, so the "planar gap" is free. Here the planar gap (PS) is a deterministic but unsolved problem. Large N removes the randomness. It does not remove the order-one coupling.

## 5. The linear loop-sequence frame: Lemma 2 and Theorem Q. PROVED as implications

Divide (SD) by n_e. For a function psi on sequences and a pair (s, e) with n_e(s) >= 1, write (SD) as phi(s) = (B^e_beta phi)(s) + N^-2 (K^e phi)(s), where B^e_beta holds the split, deformation and last terms and K^e holds the t_e^2 and merger terms. Residual: Res_beta psi (s, e) = psi(s) - (B^e_beta psi)(s).

Row sums. Splits: at most n_e(n_e - 1) ordered pairs, so at most n_e - 1 after division. Deformations: 6 beta. Last term: at most 6 beta. K^e: at most (n_e^2 + n_e(n_e-1))/n_e < 2 n_e. Every sequence s' in (B^e psi)(s) has |s'| <= |s| + 4 and r(s') <= r(s) + 1. Every s' in (K^e psi)(s) has |s'| <= |s| and r(s') <= r(s).

Norms. For m >= 0 and a >= 1: ||psi||_{m,a} = sup_s |psi(s)| exp(-m r(s)) a^(-|s|). For residuals: ||Res psi||_{m,a} = sup over s and over the links e with n_e(s) = n_*(s) of |Res psi(s,e)| exp(-m r(s)) a^(-|s|).

**Hypothesis TPS(beta; m, a, a', kappa)** (tame planar stability), with 1 < a <= a', m > 0: for every psi with psi(empty) = 0 and sup |psi| finite,

  ||psi||_{m,a'} <= kappa ||Res_beta psi||_{m,a}.

**Lemma 2 (open condition; the case a' = a only).** TPS(beta; m, a, a, kappa) implies TPS(beta'; m, a, a, kappa') for |beta' - beta| < 1/(12 a^4 e^m kappa), with kappa' = kappa / (1 - 12 a^4 e^m kappa |beta' - beta|).
Proof. Res_beta' psi - Res_beta psi = -(beta' - beta) D^e psi, where D^e (deformations and last term at beta = 1) has row sum at most 12 and maps s to sequences s' with a^|s'| e^(m r(s')) <= a^4 e^m a^|s| e^(m r(s)). So ||D psi||_{m,a} <= 12 a^4 e^m ||psi||_{m,a}, and ||psi|| <= kappa ( ||Res_beta' psi|| + 12 a^4 e^m |beta' - beta| ||psi|| ). ||psi||_{m,a} is finite because psi is bounded. QED.
For a tame pair a < a' the same proof fails: D is not bounded from the norm (m,a') to the norm (m,a). So for a tame pair the open condition is NOT proved. Lemma 2 is kept as the form of a continuation step: stability can be carried in beta as long as kappa stays finite, with dkappa/dbeta <= 12 a^4 e^m kappa^2. It will be used in section 7 for (PS), where the same proof applies.

**Theorem Q.** Assume TPS(beta; m, a, a', kappa). Let B_R be the box of radius R about the origin. Let phi, phi' be two Wilson states (any finite volumes that contain B_R, any boundary conditions, or a torus) of SU(N) at the same beta and N, in which every link of B_R is integrated. Let l_N be the largest integer with l (a'/a)^l <= N^2/(4 kappa), and assume l_N >= 1/ln a. Then for every sequence s_0 in B_R:

  |phi(s_0) - phi'(s_0)| <= a'^|s_0| e^(m r(s_0)) [ 2 kappa C_1 e^(-m R) + 8 kappa l_N N^-2 a^(-l_N) ],   C_1 = 2/(e ln a) + 24 beta.

If a' = a the floor is 2 a^(-N^2/(4 kappa)). If a' > a the floor is a power N^(-2 - 2 ln a / ln(a'/a)) up to logarithms.

Proof. Put psi = phi - phi' on sequences inside B_R and psi = 0 elsewhere. Then |psi| <= 2, psi(empty) = 0, Psi := ||psi||_{m,a'} <= 2. Let s be a sequence and e a link with n_e = n_*(s).
(i) s inside B_{R-1}. All sequences in (SD) at (s, e) are inside B_R, and (SD) holds for both states. So Res psi(s,e) = N^-2 K^e psi(s). The sequences s' of K^e have |s'| <= |s|, r(s') <= r(s), so |psi(s')| <= min(2, Psi a'^|s| e^(m r(s))). With n_* <= |s|: |Res| a^(-|s|) e^(-m r(s)) <= (2|s|/N^2) min( 2 a^(-|s|), Psi (a'/a)^|s| ). For |s| <= l_N this is at most Psi/(2 kappa). For |s| > l_N it is at most (4/N^2) l_N a^(-l_N), because n a^(-n) decreases for n >= 1/ln a.
(ii) s not inside B_{R-1}. Then r(s) >= R and |Res psi(s,e)| <= 2 + 2(n_* - 1 + 12 beta) <= 2|s| + 24 beta, so the weighted residual is at most C_1 e^(-m R).
TPS gives Psi <= kappa max( Psi/(2 kappa), 4 l_N N^-2 a^(-l_N), C_1 e^(-mR) ), so Psi <= 8 kappa l_N N^-2 a^(-l_N) + 2 kappa C_1 e^(-mR). QED.

Corollary Q1 (clustering to the floor; PROVED from Theorem Q). Let F = prod tr U_{l_i} for a sequence s_F, and let G be any bounded function of the links at distance more than R from s_F, |G| <= 1. Then |Cov(F, G)| <= a'^|s_F| [ 2 kappa C_1 e^(-mR) + floor ]. Proof: E[F G] = E[ E[F | links outside the box] G ], and the conditional law is a Wilson state in the box with a boundary condition; E[F] is an average of such states.

Corollary Q2 (planar limit; PROVED from the same proof). Under TPS, for two states at different N, N' the same argument with the K terms bounded by 2 n_* (N^-2 + N'^-2) gives ||phi_N - phi'_N'||_{m,a'} <= kappa [ C_1 e^(-mR) + (2/(e ln a)) (N^-2 + N'^-2) ]. So the planar limit exists, does not depend on the boundary condition, and is reached at rate N^-2.

Where N is spent in Theorem Q: step (i). The merger and current terms have row sum 2 n_*(s) / N^2. They are small only on sequences with fewer than about N^2/kappa strands on some link. On the other sequences only |psi| <= 2 is used. That is the floor. A floor is not a mass gap: with reflection positivity it says only that states below energy m carry a spectral weight at most of the size of the floor in the vectors W_s Omega (ARGUED).

Status of the hypothesis. TPS is not proved here at any beta, including small beta. Section 6 argues that TPS with a' = a is false at beta = 0 (proved in one sector), and argues that TPS with a' > a can hold only on the strong side. So Theorem Q is a correct implication with a hypothesis that does not reach order-one coupling. I keep it because its step (i) is the exact form of the estimate that spends N, and because its failure names the missing estimate.

## 6. Proposition N and the squeeze: why the linear frame stops on the strong side

**Proposition N (PROVED in the stated sector form).** Fix a plaquette p with first link e. For a partition lam = (k_1,...,k_r) of n let s_lam = (p^k_1, ..., p^k_r), and let X_p be the space of functions on the family {s_lam}. At beta = 0 and N = infinity the equation (SD) at (s_lam, e) involves only the family: (B^e psi)(s_lam) = -(1/n) sum_i k_i sum_{j=1}^{k_i - 1} psi(s_{lam with k_i -> (j, k_i - j)}) (all signs eps are +1; for each j there are k_i ordered pairs). On X_p, with any weight of the form w(s_lam) = c a^(4n), there is no constant kappa with sup |psi|/w <= kappa sup |psi - B^e psi|/w: for every n_0 there is psi in X_p, supported on n <= n_0, with ratio at least n_0.
Proof. Define psi by recursion on the number of parts, from r = n down: psi(s_lam) = rho(lam) + (B^e psi)(s_lam), rho(lam) = (-1)^r w(s_lam) for n <= n_0 and 0 otherwise. Then psi(s_lam) = (-1)^r w(s_lam) F(lam), with F(1^n) = 1 and F(lam) = 1 + (1/n) sum_i k_i sum_j F(refinement), because a refinement has r + 1 parts and the same n. The residual is rho, of weighted size 1. And F((n)) = 1 + sum_{j=1}^{n-1} F((j, n-j)) >= n. QED.

Scope. This is a statement about the operator on the invariant family {s_lam}. It does not by itself refute TPS(0; m, a, a, kappa) as defined in section 5, because there the residual is taken over all sequences, and the function psi above, extended by zero, has large residuals at other sequences (for example at a loop e' A e'^-1 B whose split is in the family). A function that is constant on classes of words under removal of backtracks would be the natural extension; I did not check its residuals. So: "TPS with a' = a is false at beta = 0" is ARGUED, not proved. What is PROVED is that no proof of TPS can treat the split term by a row-sum or sector-wise bound in one sup norm.

Exact values (python3 -I, fractions; guide): F((n)) = 1, 2, 13/3, 10, 121/5, 182/3, ... , equal to (3^n - 1)/(2n) for n <= 18 (closed form GUESSED). So the split term amplifies by about 3 per winding, that is 3^(1/4) per unit length. An upper bound of the same kind is PROVED: F(lam) <= prod_i G(k_i) with G(1) = 1, G(k) = 1 + sum_j G(j) G(k-j), and G(k) <= C 5^k (generating function g = x/(1-x) + g^2, radius 1/5). So at beta = 0, in this sector, the tame form holds with a'^4 >= 5 a^4 (PROVED in the sector) and fails with a'^4 < 3 a^4 (GUESSED from the closed form).

Meaning. A sup norm on loop sequences cannot see that the split term is harmless on factorised states. In a factorised state the split of a long loop gives W(l_1) W(l_2), which is small. An arbitrary function on sequences has no such structure, and the split term then amplifies with alternating signs.

**The squeeze (ARGUED, one sector).** A tame pair needs a' >= 3^(1/4) a > 3^(1/4). But the space of norm (m, a') must not contain the non-physical solutions of the loop equations. For the one-plaquette model at N = infinity (W_k = E tr V^k; strong phase W_1 = beta/2, W_k = 0 for k >= 2; third-order transition at beta = 1 in this normalisation), the planar equation is W_k = - sum_{j=1}^{k-1} W_j W_{k-j} + (beta/2)(W_{k-1} - W_{k+1}), and its linearisation at the strong solution is delta_{k+1} = - delta_{k-1} - (2/beta) delta_k for k >= 3. Its characteristic roots have product 1; the growing root has modulus 1/beta + sqrt(1/beta^2 - 1). With delta_0 = 0 every nonzero solution grows at that rate. So injectivity needs a'^4 < 1/beta + sqrt(1/beta^2 - 1). Together: 1/beta + sqrt(1/beta^2 - 1) > 3, that is beta < 3/5. As beta -> 1 the room closes for every norm of this kind (both roots reach modulus 1). So the linear loop-sequence method with sup norms is a strong-side method. It may improve the constant 1/48; it cannot reach the weak side. This agrees with the reading row's report that Cao-Nissim-Sheffield (arXiv:2505.16585) treat the master equation as a linear inhomogeneous equation with an a priori bound and stay in strong-coupling windows (reported by Luna, not read by me).

Consequence for the build. The estimate that spends N cannot be the row-sum bound 2 n_*/N^2 of Theorem Q. It must give the factorised structure itself, at speed N^2, locally and uniformly in the volume. That is (LD) below. This is the same step as the large-field bound exp(-cN) for the auxiliary field in the vector models.

## 7. The target theorem and its two open estimates

Planar equation. For a function W on loops put, for a loop l and a link e of l,

  F^e_beta(W)(l) = (1/n_e) [ - sum_{x != y} eps_x eps_y W(l_1^{xy}) W(l_2^{xy}) + (beta/2) sum_x eps_x sum_p ( W(l (-)_x p) - W(l (+)_x p) ) + (beta/2) t_e W(l) sum_p ( W(p) - W(p^-1) ) ].

This is (SD) at N = infinity on a factorised state. A master field at beta is a translation-invariant W with |W| <= 1, W(empty) = 1, W = F^e_beta(W) for all (l, e), that is a limit of Wilson states (so it is of positive type).

**(PS)(beta; m, a, kappa), planar stability.** There is a master field W_beta such that for every bounded delta on loops with delta(empty) = 0:

  sup_l |delta(l)| e^(-m r(l)) a^(-|l|) <= kappa sup_{l, e} | delta(l) - (DF^e_beta(W_beta) delta)(l) | e^(-m r(l)) a^(-|l|).

Here the split term is linearised to W_beta(l_1) delta(l_2) + delta(l_1) W_beta(l_2), and the last term to W_beta(l) (delta(p) - delta(p^-1)) plus a term that vanishes because W_beta(p) is real.
Facts about (PS):
- It is a same-norm statement on single loops, so Lemma 2's proof applies once the dependence of W_beta on beta is controlled (ARGUED; the implicit-function step is not written).
- The amplification of Proposition N is absent when |W_beta(l)| <= c rho^|l| with rho < 1 on nontrivial loops: the linearised split has row sum at most 2 sup_x sum_j |W_beta(l_1)|, a convergent series (ARGUED; needs the perimeter bound for W_beta, which is not proved here for order-one beta).
- (PS) with m > 0 is the statement "the planar theory has a mass gap at least m, and the master field is isolated". It fails at a planar first-order transition (two master fields) and for m above the planar mass.
- The U(N) twin: drop the last term of F. By Theorem Q's mechanism, stability for the twin would give exponential decay of N^2 Cov(tr W_C, tr W_C'), which a massless U(1) photon forbids (its exchange gives a power law at order N^-2). So where U(N) has a Coulomb phase at large N the twin of (PS) is false, and the last term of (SD) is the line that must make the difference (ARGUED). At small beta both U(N) and SU(N) have a gap (Nissim, arXiv:2510.22788, Theorem 1.1, as reported by Luna, not read by me), so there the twin passes too: at strong coupling the proof does not need the last term, at weak coupling it must.
- No proof of (PS) at order-one beta is offered. A route: (PS) is a statement about one deterministic system of quadratic equations. A Newton-Kantorovich certificate (an approximate W on finitely many loops, an approximate inverse, a tail bound from the perimeter decay of W) is a finite exact computation in principle, of the kind the lane's rules allow when Lean-checked. The tail bound is the unknown part: the deformation term has row sum 12 beta on arbitrarily long loops, so the tail is not small in a sup norm at order-one beta. GUESSED: the tail needs reflection positivity, as in the bootstrap bounds of the physics literature (UNVERIFIED).

**(LD)(beta; eps, l_0, L, c), local large deviations. The estimate that spends N.** Call a cube Delta of side L bad for a configuration U if some loop l in Delta with |l| <= l_0 has |tr U_l - W_beta(l)| > eps. For every N, every finite Lambda, every boundary condition, and every family Delta_1, ..., Delta_k of cubes in Lambda with mutual distances and distances to the boundary at least L:

  mu( Delta_1, ..., Delta_k are all bad ) <= exp( - c N^2 k ).

Facts about (LD):
- It is the gauge form of "large auxiliary fields cost exp(-cN) per site". It contains large-N factorisation, uniformly in the volume.
- It is known in kind only at strong coupling, from the log-Sobolev inequality with constant of order N (Shen-Zhu-Zhu; Nissim Theorem 1.5 for U(N); both as reported by Luna). At order-one beta it is open. It is false at a planar first-order transition.
- It needs "distance at least L from the boundary", so it presupposes a decay of boundary influence over the distance L at the planar level. This is why (LD) at scale L and (PS) at rate m must be proved together, with L of order (1/m) log(1/eps). This is the gauge form of the vector-model fact that N0 grows with the correlation length.
- N is spent here and only here: the polymer activity of a bad cube is exp(-cN^2), against an entropy factor exp(C) per cube and a loss a^(C L^4 l_0) from the norms, so N0^2 = C' L^4 l_0 ln(a) / c.

**Theorem T (target; ARGUED architecture, not proved).** Let G = SU(N), d = 4. Suppose (PS)(beta; m, a, kappa) holds. Then there are eps_0, l_0, L_0 depending on (beta, m, a, kappa) such that: if (LD)(beta; eps, l_0, L, c) holds with eps <= eps_0 and L >= L_0, then for all N >= N0 = C (L^4 l_0 / c)^(1/2), all finite Lambda and all boundary conditions, and all loop sequences s, s',

  | Cov( W_s, W_s' ) | <= C(s) C(s') exp( - (m/2) dist(s, s') ).

Chain of lemmas:
1. Lemma 1, (SD). PROVED.
2. Small-field loop equations. With a smooth cutoff chi on good cubes, (SD) holds for the cut-off law up to terms supported on the cutoff boundary. On good regions products of loop variables factorise up to (1 + eps)^k, so the cumulants are small and the sequence equations reduce to the linearised planar equation plus N^-2 terms with bounded row sums (the high-multiplicity problem of Theorem Q is removed because |tr U_l| is pinned near W_beta(l)). NOT WRITTEN. This is the step I expect to be hardest after (LD) and (PS): pinning finitely many short loops in a cube must control the long loops that the loop equation produces.
3. (PS) inverts the linearised equation with exponential weights; Theorem Q's argument, steps (i) and (ii), then gives decay of boundary influence inside good regions with no floor. The mechanism is PROVED in Theorem Q; its use here is ARGUED.
4. (LD) makes bad cubes a dilute polymer gas. A standard polymer expansion then gives the stated clustering. ARGUED, not written.
5. A transfer-matrix gap at least m/2 follows from clustering for the loop vectors W_s Omega, which span a dense set, with reflection positivity. ARGUED; the constants C(s) must not spoil density, which is not checked.

How this goes beyond strong coupling: it does not, as proved. The frame is valid at any beta where (PS) and (LD) hold; both are proved in kind only in the strong-coupling windows. The frame says exactly which two estimates a weak-side theorem needs, and Section 6 says which cheaper substitute cannot work.

## 8. Twins and limits

- U(1), any charge (PROVED from (SD) with N = 1, U(N) form). All loops commute, phi(s) depends on the current only, and the split and merger terms carry the same weight: the equation is t_e^2 phi = (beta/2) t_e sum_p [ phi(current - p) - phi(current + p) ]. There is no parameter that separates mergers from splits. A loop of charge q sees the coupling beta/q, but the law does not change with q; the photon stays massless at weak coupling (Coulomb phase, UNVERIFIED citation above). So no step of Theorem T exists for U(1): there is no planar limit, no (LD).
- U(N) at large N: section 7, fourth fact. The frame must fail through (PS) in the odd sector at weak coupling.
- N = 2: (i) the last term of (SD) is identically zero, so the line that separates SU(N) from U(N) at leading order is absent; the separation sits in the term t_e^2/4 and in the trace identity tr A tr B = (tr AB + tr AB^-1)/2, which makes mergers and splits the same size. (ii) (LD) at speed N^2 = 4 gives no dilute gas. (iii) In Theorem Q the condition l (a'/a)^l <= N^2/(4 kappa) has no solution l >= 1 unless kappa <= 1. So nothing in the frame survives at N = 2 except Lemma 1.
- The Wilson bulk transition (UNVERIFIED lore): N0(beta) must diverge at one order-one beta. The frame is consistent with this ((PS) and (LD) both fail there).

## 9. What this gives toward the SU(2) crux (PUR-io)

A separate theorem. No comparison, no interpolation in N: N0 exceeds 2 by construction, and the frame has no monotonicity in N.
What transfers, all small:
1. Lemma 1 at N = 2 is an exact identity for every beta, volume and boundary condition, in single-link form, with its t_e^2/4 term checked. It is a (T1)-type relation only in the weak sense that it holds for every law of the family; it compares no two laws.
2. Proposition N and the squeeze are a negative tool: any plan to get clustering from the loop equations as a linear system in a sup norm stops on the strong side, at any N. This removes one class from the campaign list (the class of the reading row's "MAY APPLY: uniqueness plus contraction for the all-coupling master equation").
3. The pair (LD), (PS) is the large-N form of the pre-filter questions (Q2) and (Q3) of the crux card: (Q2) what replaces a small parameter at order-one coupling: here N^-2, through (LD); (Q3) the line where the group is read: here the last term of (SD). For SU(2) neither exists. That is a statement of why large N is a different problem, not a step toward (PUR-io).

## 10. Open items by name

- TPS at small beta (non-vacuity of Theorem Q): not proved.
- (PS) at any order-one beta; the perimeter bound for W_beta; the dependence of W_beta on beta.
- (LD) at any order-one beta.
- Step 2 of Theorem T (small-field loop equations).
- The closed form F((n)) = (3^n - 1)/(2n).
- All citations are from memory or from the reading row 1710 as reported; none was read by me in this row.

Used from the coordinator's note on row 1710 (library/prior/gap-largen-lit-luna.md, read once, not verified against the papers): the Shen-Zhu-Zhu window; Nissim Theorems 1.1 and 1.5 (small-beta U(N) gap and concentration), used in section 7 to limit the U(N) twin claim to weak coupling; the Cao-Nissim-Sheffield description, used in section 6. Not used: the Cao-Park-Sheffield surface sum.

RESULT: no large-N mass-gap theorem at order-one coupling is proved; target Theorem T: for SU(N) Wilson, planar stability (PS) of the linearised master-field equation plus a local large-deviation bound (LD) at speed N^2 give volume-uniform exponential clustering for N >= N0 ~ (L^4 l_0/c)^(1/2). Mechanism: single-link loop equation, master field as saddle, bad cubes as a dilute gas. PROVED: the SU(N) edge loop equation with its U(1)-reading term (checked on SU(2), SU(3)); Theorem Q (tame stability gives clustering down to a floor in N, any boundary condition); Proposition N (in the winding sector at beta = 0 the split term amplifies without bound in one sup norm; the linear method is argued to stop near beta 0.6). The estimate that spends N is (LD): stated, open; (PS) passes order one: open. Toward SU(2): a separate theorem; only the exact identity and the negative tool transfer.
