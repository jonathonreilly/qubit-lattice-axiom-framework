lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-11T09:49Z

# gap-zero-transport: from zeros of torus partition functions to a spectral gap

Written by the author run of FINISH row 670 (`library/gap-skeleton-max-b.md`), as a self-contained unit for a line-by-line check. Proved by Claude Fable 5.2, not yet checked by another model. Research-stage working state. It grants no status. It proves implications only. It does not prove a mass gap. Section 6 (boxes with free walls) is the version that the plan uses after its correction 2.5; Sections 2, 3 and 5 are about periodic tori.

Credits. The transfer operator is classical (Luescher; Osterwalder and Seiler; not read in this run) and is the object of FINISH row 667 (`library/gap-transfer.md`, not opened by me). The twisted partition functions are 't Hooft's (not read). The two-constants theorem is Nevanlinna's and classical. The use of analyticity to get decay is in the manner of Lebowitz and Penrose (not read). The picture that zeros of the partition function in the complex coupling plane bound the flows to strong coupling, with numerical evidence for SU(2), is due to Denbleyker, Du, Liu, Meurice and Zou (arXiv:1005.1993, read). What is added here is the chain of exact inequalities from "no zeros" to a gap with a rate.

## 1. Setting and inputs

Group G = SU(2), Haar probability measure. Lattice torus with sides n = (n_1, n_2, n_3, n_4), each at least 3, |n| = n_1 n_2 n_3 n_4. One group variable per positively oriented link. Plaquette action a_p(U) = 1 - (1/2) Re tr U_p, in [0, 2]. There are 6|n| plaquettes. For complex beta, Z(n; beta) = int exp(-beta sum_p a_p) dU. It is an entire function of beta. For real beta >= 0, exp(-12 beta |n|) <= Z <= 1. For real beta < 0, 1 <= Z <= exp(12 |beta| |n|). For complex beta, |Z(n; beta)| <= Z(n; Re beta).

Input (TM), for real beta > 0. For the box (n_2, n_3, n_4) there is a self-adjoint, positive semi-definite, trace-class operator T on L^2 of the spatial link variables, with a continuous strictly positive kernel after the average over gauge transformations, such that Z(n; beta) = Tr T^{n_1} for all n_1 >= 3. Its largest eigenvalue lambda_0 > 0 is simple, with a strictly positive eigenfunction Psi_0. The same holds with any direction as direction 1. (Row 667.)

Notation. Eigenvalues lambda_0 > lambda_1 >= lambda_2 >= ... >= 0 with multiplicity, r_i = lambda_i/lambda_0, S(k) = sum_{i>=1} r_i^k, lattice gap m = log(lambda_0/lambda_1) > 0. F(n) = log Z(n), f(n) = F(n)/|n| for real beta.

Input (SC), strong coupling at complex beta. There are r_0 > 0, C_0, kappa_0 > 0 such that for |beta| <= r_0 and symmetric tori n^4, n >= 4: the limit f_inf(beta) = lim f(2^j n; beta) exists and is analytic, and |f(n; beta) - f_inf(beta)| <= C_0 exp(-kappa_0 n). The same for the zero-flux functions of Section 3. (Convergent polymer expansion; a closed winding surface has at least 4n plaquettes; not proved here.)

## 2. Free energy bounds the spectrum

**Lemma 1.** Let beta > 0 be real.
(a) For a positive semi-definite trace-class A with largest eigenvalue lambda_0 > 0, k -> (Tr A^k)^{1/k} is non-increasing on k >= 1 and tends to lambda_0.
(b) S(k + k') <= S(k) S(k') for k, k' >= 1.
(c) f(n) is non-increasing in each side. Put f_inf = inf_n f(n). Then f(n) tends to f_inf along every sequence with all sides tending to infinity, and Delta(n) := F(n) - |n| f_inf >= 0.
(d) For the transfer operator of the box (n_2, n_3, n_4): 1 + S(n_1) <= exp(Delta(n)) for every n_1 >= 3. So exp(-n_1 m) <= exp(Delta(n)) - 1.

Proof. (a) With eigenvalues mu_i >= 0: sum mu_i^{k+1} <= mu_max sum mu_i^k <= (sum mu_i^k)^{1/k} sum mu_i^k, so (Tr A^{k+1})^{1/(k+1)} <= (Tr A^k)^{1/k}. And lambda_0^k <= Tr A^k <= lambda_0^{k-1} Tr A. (b) sum_{i>=1} r_i^{k+k'} <= (max_{j>=1} r_j^{k'}) sum_{i>=1} r_i^k <= S(k') S(k). (c) Apply (a) to the transfer operator of each direction: (Tr T^{n_mu})^{1/n_mu} is non-increasing in n_mu, and f(n) is its logarithm divided by the product of the other sides. f >= -12 beta. A function on N^4 that is non-increasing in each variable and bounded below converges to its infimum when all variables tend to infinity: given eps, pick n* with f(n*) <= f_inf + eps; for n >= n* in every component, f_inf <= f(n) <= f(n*). (d) By (a), log lambda_0 = lim_{n_1} F(n)/n_1 = n_2 n_3 n_4 lim_{n_1} f(n) >= n_2 n_3 n_4 f_inf. Hence Z(n) = lambda_0^{n_1} (1 + S(n_1)) >= exp(|n| f_inf)(1 + S(n_1)). Finally r_1^{n_1} <= S(n_1). QED.

**Lemma 2 (integral formula).** For fixed n, F(n; beta) is smooth and convex in real beta, with dF/dbeta = -6|n| abar(n; beta), abar the mean of a_p. The function f_inf is convex on [0, infinity), f_inf(0) = 0, and with abar_inf := -f_inf'/6 (defined almost everywhere),
Delta(n; beta) = 6|n| int_0^beta (abar_inf(s) - abar(n; s)) ds.
Proof. d^2F/dbeta^2 is the variance of the action, so F is convex; f_inf is a pointwise limit of convex functions, hence convex, hence locally Lipschitz on (0, infinity) and absolutely continuous on [0, beta] (it is bounded between -12 beta and 0 and convex, so it is continuous at 0). F(n; 0) = 0 = f_inf(0). Both sides of the formula vanish at 0 and have the same derivative almost everywhere. QED.

## 3. The zero-flux sector

Let direction 1 be the time direction. For i = 2, 3, 4 let C_i act on functions of the spatial links by composition with the map that multiplies by -1 every link in direction i from the layer x_i = 0 to the layer x_i = 1.

**Lemma 3.** (a) C_i is unitary, C_i^2 = 1, the C_i commute with each other and with T. (b) For k in Z_2^3, with C^k = prod_i C_i^{k_i}: Tr(T^{n_1} C^k) = Z_k(n; beta), where Z_k is the partition function in which, for each i with k_i = 1, the plaquettes in the plane (1, i) that join the last time layer to the first and sit on the flipped links have 1 - (1/2) Re tr U_p replaced by 1 + (1/2) Re tr U_p. Z_k is entire in beta, positive for real beta, and |Z_k(beta)| <= exp(12 |n| max(0, -Re beta)). (c) C_i Psi_0 = Psi_0. (d) Multiplication by a function of the holonomies of contractible closed spatial loops commutes with every C_i.
Proof. (a) The map is a measure-preserving involution of the configuration space. A spatial plaquette contains either no flipped link or two (its two links in direction i lie in the same pair of layers), so the spatial action is invariant. A time-like plaquette on a spatial link b involves U_b at two consecutive times; the kernel of T depends on them through tr of a product that contains each once, and both are flipped. So the kernel satisfies K(U^C, U'^C) = K(U, U'), which is C T = T C. (b) Write the trace as the integral over n_1 time layers with the last factor K(U(n_1), U(1)^C). In that factor the time-like plaquettes on the flipped links get the opposite sign of the trace, all others are unchanged. Entire: an integral of an entire function over a compact space. The modulus bound: 0 <= 1 +- (1/2) Re tr <= 2. (c) C_i Psi_0 is an eigenfunction for lambda_0, which is simple, so C_i Psi_0 = +-Psi_0; both functions are positive. (d) A contractible closed loop crosses the pair of layers an even number of times, so its holonomy is unchanged by the flip. QED.

Let P_0 = prod_i (1 + C_i)/2, the projection on the zero-flux subspace H_0, and Z^(0)(n; beta) = Tr(T^{n_1} P_0) = (1/8) sum_k Z_k(n; beta). By Lemma 3, Psi_0 is in H_0 and T maps H_0 to itself.

**Lemma 1'.** For real beta > 0, with S^(0)(k) the sum of r_i^k over the eigenvalues of T on H_0 other than lambda_0, and Delta^(0)(n) = log Z^(0)(n) - |n| f_inf: 0 <= Delta^(0)(n) <= Delta(n) and 1 + S^(0)(n_1) <= exp(Delta^(0)(n)). So the gap m^(0) of T on H_0 satisfies exp(-n_1 m^(0)) <= exp(Delta^(0)(n)) - 1.
Proof. Z^(0)(n) = lambda_0^{n_1}(1 + S^(0)(n_1)), and lambda_0^{n_1} >= exp(|n| f_inf) by Lemma 1(d). Z^(0) <= Z because T >= 0 and P_0 is a projection commuting with T. QED.

## 4. Two classical tools

**Theorem LP (two constants).** Let Omega be a bounded domain whose boundary is the union of two closed sets Gamma_1 and Gamma_2, and let omega be the harmonic function on Omega with boundary values 1 on Gamma_1 and 0 on Gamma_2 (the harmonic measure of Gamma_1; if the boundary has irregular points, the Perron solution). Let h be analytic on Omega and continuous on its closure, |h| <= eps on Gamma_1, |h| <= M on Gamma_2, 0 < eps < M. Then |h(z)| <= eps^{omega(z)} M^{1 - omega(z)} on Omega.
Proof. log|h| is subharmonic on Omega (with value -infinity at zeros). v = omega log eps + (1 - omega) log M is harmonic, and limsup of (log|h| - v) at every boundary point is <= 0. The maximum principle for subharmonic functions gives log|h| <= v. QED.

**Lemma HM (half-strip).** In {x > 0, |y| < w} the bounded harmonic function with values 1 on x = 0 and 0 on |y| = w is omega(x, y) = (4/pi) sum_{k odd >= 1} ((-1)^{(k-1)/2}/k) cos(k pi y/(2w)) exp(-k pi x/(2w)). On the axis omega(x, 0) = (4/pi) arctan(exp(-pi x/(2w))) >= exp(-pi x/(2w)).
Proof. Each term is harmonic and vanishes on |y| = w. At x = 0 the series is the Fourier expansion of 1 on (-w, w). Uniqueness of bounded solutions in the half-strip (Phragmen-Lindeloef). On the axis sum_{k odd} (-1)^{(k-1)/2} q^k/k = arctan q, and arctan q >= (pi/4) q on [0, 1] by concavity. QED.
Monotonicity of domain: if Omega is enlarged with Gamma_1 kept, omega does not decrease on the smaller domain (maximum principle).

## 5. No zeros implies the gap

**Theorem Z.** Let (SC) hold on |beta| <= 2 r_0. Let D be a bounded simply connected domain, symmetric under complex conjugation, containing the closed disc B = {|beta| <= r_0} and the real interval [0, X), with D intersected with {Re beta <= 0} inside {|beta| < 2 r_0}. Put H = sup of |Im beta| over D. Shape condition (TUBE): there is theta in (0, 1] such that for every beta = x + iy in D with x >= 0, the closed disc with centre x and radius |y| + theta d(beta) lies in D, where d(beta) is the distance from beta to the boundary of D. Let n_j = 2^j n_0. Assume (TM), and
(ZF) Z^(0)(n_j^4; beta) != 0 for all j >= 0 and all beta in D.
Then, with f_j = n_j^{-4} log Z^(0)(n_j^4; .) (the branch that is real on the real axis):
1. |f_j(beta)| <= 12 (2 r_0 + x)(1 + 4|y|/(theta d(beta))) for beta = x + iy in D with x >= 0.
2. f_j converges locally uniformly on D to an analytic function f_inf, which is the function of Lemma 1 on the real axis.
3. For every j, every real beta in D with beta > r_0, and delta_j = 1/n_j:
Delta^(0)(n_j^4; beta) <= 24 (2 r_0 + X)(1 + 4 H n_j/theta) max(1, C_0) n_j^4 exp(-kappa_0 omega_j(beta) n_j),
where omega_j is the harmonic measure of the circle |beta| = r_0 in the domain D_j = {beta in D: Re beta > 0, d(beta) > delta_j, |beta| > r_0}.
4. Consequently, as j grows, the gap of T on H_0 for the box n_j^3 at coupling beta is at least kappa_0 omega_j(beta) - (5 log n_j + c)/n_j, with c depending on r_0, X, theta, C_0 only, as soon as the right side of 3 is at most log 2.

Proof.
Step 1. By (ZF) and simple connectedness, f_j is analytic on D. For beta in D: |Z^(0)(beta)| <= (1/8) sum_k |Z_k(beta)| <= exp(12 n^4 max(0, -Re beta)) (each plaquette factor has modulus at most exp(2|Re beta|) if Re beta < 0 and at most 1 otherwise). So Re f_j <= A := 24 r_0 on D (the part of D with Re beta <= 0 lies in |beta| < 2 r_0). At a real x in [0, X): Z^(0) is real and positive, f_j(x) is real, and -12 x <= f_j(x) <= 0 because exp(-12 x n^4) <= lambda_0^{n} <= Z^(0) <= Z <= 1. For beta = x + iy in D with x >= 0, use the Borel-Caratheodory inequality on the disc of (TUBE), centre x, radius R = |y| + theta d, at distance r = |y| from the centre: |f_j(beta)| <= (2r/(R - r)) A + ((R + r)/(R - r)) |f_j(x)| <= (2|y|/(theta d)) 24 r_0 + (1 + 2|y|/(theta d)) 12 x. This gives 1. On the part of D with x <= 0, which lies in |beta| < 2 r_0, (SC) gives |f_j| <= sup over |beta| <= 2 r_0 of |f_inf| + C_0.
Step 2. On the real interval, f_j(x) tends to f_inf(x) (Lemma 1(c) gives f(n_j^4) -> f_inf, and f_inf <= f^(0) <= f by Lemma 1'). The f_j are locally uniformly bounded by Step 1. Vitali's theorem: a locally bounded sequence of analytic functions on a domain that converges on a set with a limit point in the domain converges locally uniformly to an analytic function. The limit agrees with the f_inf of (SC) on the disc.
Step 3. Put u_j = f_j - f_inf on D. By Steps 1, 2: |u_j(beta)| <= 24 (2 r_0 + X)(1 + 4H/(theta d(beta))) for Re beta >= 0. On the circle |beta| = r_0, |u_j| <= C_0 exp(-kappa_0 n_j) by (SC). u_j is analytic on a neighbourhood of the closure of D_j. The boundary of D_j consists of the arc of the circle |beta| = r_0 with Re beta >= 0, a segment of the imaginary axis inside |beta| < 2 r_0 (where |u_j| <= C_0 exp(-kappa_0 n_j) again by (SC); count it with the circle), and points with d = delta_j = 1/n_j, where |u_j| <= M_j := 24 (2 r_0 + X)(1 + 4 H n_j/theta). Theorem LP with eps = C_0 exp(-kappa_0 n_j): |u_j(beta)| <= M_j^{1 - omega_j} (C_0)^{omega_j} exp(-kappa_0 omega_j n_j) on D_j, with omega_j the harmonic measure of the first two pieces (it is at least the harmonic measure of the arc alone). On the real axis u_j = Delta^(0)/n_j^4 >= 0. Multiply by n_j^4. (If eps >= M_j the bound is trivial. The constants are not optimised.)
Step 4. Lemma 1' with n_1 = n_j. QED.

Remarks. (i) The hypothesis is that explicit entire functions have no zeros in D. No bound is assumed: the bounds come from positivity on the real axis. (ii) The same proof works for the full Z in place of Z^(0), and for v_j = f_j - f_{j+1} in place of u_j. (iii) As j grows, omega_j increases to the harmonic measure omega_D of the circle in D minus B.

**Corollary A (fixed coupling).** Under (TM), (SC), (ZF) on D: for every real beta in D, liminf_j m^(0)(n_j^3; beta) >= kappa_0 omega_D(beta) > 0. If D contains B and the rectangle {0 < Re beta < X, |Im beta| < w}, then for r_0 < beta < X - w: omega_D(beta) >= c(r_0, w) exp(-pi beta/(2w)).

**Corollary B (scaling form; this is Corollary 5 of the plan).** Let a(beta) > 0 be a function on the real axis (the lattice spacing in physical units). Assume, for each n in a doubling sequence, a domain D_n as in Theorem Z, cut at Re beta = X_n, on which Z^(0)((2^j n)^4; .) has no zeros for all j, with theta and r_0 independent of n, and assume (HM): the harmonic measure of the circle in D_n satisfies omega(beta) >= eps a(beta) for real beta in [beta_1, X_n - s]. Then for such beta and n: Delta^(0)(n^4; beta) <= C (1 + X_n) n^5 exp(-kappa_0 eps' a(beta) n) with eps' = eps (1 - o(1)), and the gap of the zero-flux sector of the box n^3 is at least kappa_0 eps' a(beta) - (5 log n + C')/n in lattice units. In physical units, with l = n a(beta), the gap is at least kappa_0 eps' - (5 log(l/a(beta)) + C')/l. It is at least kappa_0 eps/2 once l >= C'' log(1/a(beta)).
Proof. Theorem Z on D_n. The harmonic measure in the domain shrunk by 1/n differs from that in D_n by a factor that tends to 1 when X_n/n tends to 0 (in a strip of half-width w the exponent pi x/(2w) changes by pi x/(2 w^2 n)); this is the o(1). To be written out with the domain of (HM). QED given that estimate.

## 6. Warning on Corollary B, and the version for boxes with free walls

**Warning.** On a periodic torus the hypothesis of Theorem Z can hold in the scaling region only in a tube of half-width pi/(4 c_a), where c_a = -d log a/d beta, because the zero-flux sector contains pairs of winding flux tubes and the vacuum energy contains winding sheets, whose weights involve the string tension, a quantity of dimension two (plan, 2.5). The harmonic measure of that tube decays like a(beta)^2. So Corollary B, applied to periodic tori, gives a lattice mass of at least c a(beta)^2 and no gap in physical units. Theorem Z and Corollary A stand as stated. The version that the plan uses is the following.

Setting. B is a finite box in Z^3 with free boundary conditions: the links are those with both ends in B, the spatial plaquettes are those inside B, every link carries time-like plaquettes, time is periodic with k steps, and gauge transformations act at every site of B. Z(k, B; beta) is the partition function, entire in beta, with exp(-12 k |B| beta) <= Z <= 1 for real beta >= 0 (there are at most 6 k |B| plaquettes) and |Z(beta)| <= exp(12 k |B| max(0, -Re beta)).

Input (TM_B). For real beta > 0 there is a positive semi-definite trace-class operator T_B with a simple largest eigenvalue lambda_0 > 0 and Z(k, B; beta) = Tr T_B^k for k >= 3. (The construction of row 667 with free walls; not written here.) Notation: s_k = sum_{i >= 1} (lambda_i/lambda_0)^k, gap m_B = log(lambda_0/lambda_1).

Input (SC_B). There are r_0, C_0, kappa_0 > 0, independent of B, such that for |beta| <= 2 r_0, k >= 4, q >= 1: |log Z(k,B;beta) - (1/q) log Z(qk,B;beta)| <= C_0 |B| k exp(-kappa_0 k), with the branches of the logarithms that are real on the real axis (Z has no zeros in that disc).

**Theorem ZB.** Let D be a domain as in Theorem Z (bounded, simply connected, symmetric, containing |beta| <= r_0 and [0, X), its part in Re beta <= 0 inside |beta| < 2 r_0, shape condition (TUBE) with theta, H = sup |Im beta|). Assume (TM_B), (SC_B) and
(ZF_B) Z(k, B; beta) != 0 for all beta in D and all k >= k_0.
Then for every real beta in D with beta > r_0: m_B(beta) >= kappa_0 omega_D(beta), where omega_D is the harmonic measure of the arc {|beta| = r_0, Re beta >= 0} in the domain {beta in D: Re beta > 0, |beta| > r_0}.

Proof.
Step 1. Fix k >= k_0, q >= 1. By (ZF_B) the functions L_1 = log Z(k,B;.) and L_q = (1/q) log Z(qk,B;.) are analytic on D. For both: the real part is at most 24 k |B| r_0 on D, and at real x in [0, X) the value is real and lies in [-12 k |B| x, 0]. The Borel-Caratheodory inequality on the disc of (TUBE), as in step 1 of Theorem Z, gives |L(beta)| <= 12 k |B| (2 r_0 + x)(1 + 4|y|/(theta d(beta))) for beta = x + iy in D, x >= 0.
Step 2. Put g_q = L_1 - L_q. On D_k = {beta in D: Re beta > 0, |beta| > r_0, d(beta) > 1/k}: the boundary consists of the arc, a segment of the imaginary axis inside |beta| < 2 r_0, and points with d = 1/k. On the first two, |g_q| <= eps_k := C_0 |B| k exp(-kappa_0 k) by (SC_B). On the third, |g_q| <= M_k := 24 k |B| (2 r_0 + X)(1 + 4 H k/theta). Theorem LP: |g_q(beta)| <= max(M_k, 1) max(C_0 |B| k, 1) exp(-kappa_0 omega_k(beta) k) on D_k, where omega_k is the harmonic measure of the arc in D_k. The bound is uniform in q.
Step 3. Let beta be real. By (TM_B), Z(k,B) = lambda_0^k (1 + s_k) and Z(qk,B) = lambda_0^{qk}(1 + s_{qk}) where s_j = sum_{i >= 1} (lambda_i/lambda_0)^j. Each ratio is below 1 and s_k is finite, so s_{qk} -> 0 as q -> infinity by dominated convergence. The powers of lambda_0 cancel in g_q. So g_q(beta) = log(1 + s_k) - (1/q) log(1 + s_{qk}) -> log(1 + s_k) as q -> infinity. Hence log(1 + s_k(beta)) <= max(M_k,1) max(C_0|B|k,1) exp(-kappa_0 omega_k(beta) k).
Step 4. exp(-k m_B) <= s_k <= exp(R_k) - 1 with R_k the right side of Step 3. For k large R_k <= 1 and s_k <= 2 R_k. So m_B >= kappa_0 omega_k(beta) - (1/k) log(2 max(M_k,1) max(C_0|B|k,1)). As k -> infinity the domains D_k increase to the domain of the statement, omega_k(beta) increases to omega_D(beta) (harmonic measure is monotone in the domain and continuous under increasing unions), and the last term tends to 0. QED.

**Corollary 5'.** If (TM_B), (SC_B), (ZF_B) hold for every box B with sides at least n_min on one domain D, and omega_D(beta) >= eps a(beta) for real beta >= beta_1, then m_B(beta) >= kappa_0 eps a(beta) for all those boxes and couplings.

## 7. What is not proved here

- (TM): row 667. (TM_B): the same construction with free walls, to be written. (SC), (SC_B): to be written with constants.
- (ZF) and (ZF_B) on any domain beyond the strong-coupling disc. This is the open crux. It is false for U(1) and for Z_2 on any domain that crosses their transitions, and (by simulations) for an SU(2) action with an adjoint term beyond its critical end point.
- The harmonic-measure bound for the asymptotic-freedom domain.
- The passage from Corollary 5' to infinite volume and to the continuum limit, and the relation between limits of boxes with free walls and the periodic Gibbs states of the account (plan, nodes N9 to N11).
