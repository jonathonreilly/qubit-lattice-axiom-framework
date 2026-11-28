# Check 1639: (E1) on the band, rows 1636 and 1637

Checker: Claude Opus 5.5 (row 1639). Files checked: `library/gap-vir-down-e1band-astra62.md` (row 1636), `library/gap-vir-down-e1band-obstruct.md` (row 1637). Status: complete (2026-11-27). Checked by hand, line by line.

## 0. Reading log

- FINISH.md rows 1636, 1637 (briefs and RESULT texts), read in full.
- `library/gap-vir-down-e1band-astra62.md` (row 1636, 246 lines) and `library/gap-vir-down-e1band-obstruct.md` (row 1637, 163 lines), read in full.
- Check 1630 (`library/gap-vir-down-twoside-check-opus.md`), read in full; sections 1 and 3.3 with care.
- Checks 1634 (`library/gap-vir-down-e12-check-opus.md`) and 1635 (`library/gap-vir-down-e2-neon-check-opus.md`), read in full.
- Row 1628 (`library/gap-vir-down-twoside-astra62.md`) L150-286 (families A, B, tests (16)-(23)); row 1631 (`library/gap-vir-down-e1-astra62.md`), read in full.
- Registry row VIR-DOWN (`library/open-registry.md` L1028).
- Row 710 (`library/gap-vir-sc.md`) section 8 (L185-205: the lattice action sum rule, the heat-kernel reading "the electric part alone gives K = 1/s") and Proposition EL (L82).
- Not read: `library/gap-vir-down-e1band-neon.md`. Not re-read: rows 941, 947 (midpoint, bridge) and check 1297; I re-derived every formula of row 1636 that uses them.
- Guide run (floating point; not a proof step, not a verification record): one Python process, a few MB, in this session's scratchpad outside the repository (`g1639/guide.py`). Results are quoted where used.

## 1. Row 1636, line by line

Setup. In temporal gauge the Wilson temporal plaquette on link e is (1/2) tr(x_e y_e^(-1)) = x_e . y_e for unit quaternions, so the temporal kernel is e^(beta x.y) = e^(beta L) e^(-beta |x-y|^2/2). The constant e^(beta L) and the Gaussian normalisation have the same log-derivative for every state, so they cancel in b_psi. The pair law a(dx) a(dy) e^(-beta|x-y|^2/2), a = M Omega dx, has marginal lambda_0 Omega^2 dx (use K M Omega = lambda_0 Omega / M), and E f(X) f(Y) = r. b_psi = <psi, T' psi>/(r lambda_0) - lambda_0'/lambda_0 equals the eigenspace compression <psi, A' psi>/r of row 1628 (19). The unprojected kernel acts as the projected one on gauge-invariant, centre-neutral vectors, and its Perron vector is invariant. HOLDS.

**(1). HOLDS.** Re-derived.
- Spatial part: M' = -(V/2) M and K M psi = r lambda_0 psi / M give -E_pi(f^2 V); minus the vacuum value gives -Cov_pi(f^2, V).
- Temporal part: e^(-beta|x-y|^2/2) is p_tau convolved from two p_(tau/2), tau = 1/beta, so the temporal factor is log of int k^2 / int h^2 with k = p_(tau/2) * (f a), h = p_(tau/2) * a. d/dtau int v_(tau/2)^2 = -(1/2) int |grad v|^2; d tau/d beta = -1/beta^2. With k = sqrt(r) h g and one integration by parts, the temporal part is (1/(2 beta^2)) [int |grad g|^2 d eta - Cov_eta(g^2, Delta h / h)].
- Delta p_s(z - x) = (|z-x|^2/s^2 - D/s) p_s, s = 1/(2 beta), so Delta h/h = 4 beta^2 H - 2 beta D. This gives (1).
- Strict positivity: g is bounded, real analytic, mean zero, unit norm in L^2(eta), so it is not constant. HOLDS.

**Direct check and (2). HOLDS.** Re-derived each line: grad g = 2 beta (E[Xf|Z]/sqrt r - g q); the temporal insertion X.Y - L; grad log(d eta/dz) = 4 beta (q - z); div q = 2 beta (L - |q|^2); the mean-zero field -L - |q|^2 + 2 z.q. With h = e^(-beta|z|^2 - beta L) B(z), Delta_(z_e) B = 4 beta^2 B and Delta_(z_e)(B g) = 4 beta^2 B g (|x_e| = 1), so (Delta_e + grad_e log rho . grad_e) g = -4 beta z_e . grad_e g. Integrating against g and then by parts (div_e z_e = 4) gives (2). Then the temporal slope is 2 Cov_eta(g^2, |Z|^2), which also follows directly from 2|W|^2 = L + X.Y. Both forms agree with (1) after H = |z|^2 + L - 2 z.q.
Standing: (2) is a gradient norm written as a covariance, so its sign is automatic. The useful content is the identity b_psi = 2 Cov_eta(g^2, |Z|^2) - Cov_pi(f^2, V): the slope is a midpoint-radius covariance minus a spatial-action covariance. Neither term has a known sign or size. The radius reading is ON FILE (row 1290; row 1636 cites it).

**(3). HOLDS.** Re-derived.
- X, Z_s, Y have joint density a(dx) p_s(z - x) p_(s')(z - y) a(dy); the normaliser int h_s h_(s') = int int a p_tau a does not depend on s (Chapman-Kolmogorov). u_s = E[f(Y) | Z_s]. F(s_0) = r; F <= 1 by conditional Jensen.
- (d_s + (1/2) Delta + v . grad) u = 0 with v = grad log h_(s'); d_s nu = (1/2) Delta nu - div(v nu). Then d/ds int phi d nu = int O phi d nu with O = d_s + (1/2) Delta + v . grad, so F' = int |grad u|^2 d nu (row 947's identity) and F'' = int (||grad^2 u||^2 - 2 grad u^T (grad^2 log h_(s')) grad u) d nu.
- The flat Bochner identity int (L_s u)^2 d nu = int (||grad^2 u||^2 - grad u^T grad^2 log rho grad u) d nu, with log rho = log h_s + log h_(s') + const, gives F'' = int (L_s u)^2 - int grad u^T B_s grad u. Completing the square with alpha = F'/F gives (log F)'' = D_s - C_s exactly.
- Taylor with weight (s_1 - s) and s_1 - s_0 = 1/(4 beta); (log F)'(s_0) = int |grad g|^2 d eta. Multiplying by 1/(2 beta^2) gives (3). 0 <= A_psi <= 2m/beta from F(s_0) = r <= F(s_1) <= 1.
- Strictness: D_(s_0) = 0 forces L g = -alpha g, and summing the link identities gives z . grad g = (alpha/(4 beta)) g; a bounded function homogeneous of positive degree on R^D is zero. HOLDS. No size of the loss is claimed. Correct.

**(4). HOLDS.** The block version: the same differentiation applies component by component; with the common scalar alpha = F_r'/F_r the completed square is sum_j int (L u_j + alpha u_j)^2 = sum_j int (L u_j)^2 - (sum F_j')^2/(sum F_j). ||Gamma_t|| = sum_r k_r r^t log(F_r(s_1)/r) <= W_obs. The term (2/beta)(s_1 - s) C^(r) integrates to the [B_s]_Y integral against Gamma_t. Basis invariance holds (Y_r is a trace over an orthonormal frame). Absolute summability: |S_psi| <= C_box / r uniformly over unit eigenvectors at a fixed box, and sum_r k_r r^(t-1) converges for t > 2. The existence of one visible excitation is ON FILE (rows 1617, 1624 (14), 1628 (17)). HOLDS.

**(5). HOLDS.** grad^2 log h_v = -I/v + Sigma_v/v^2 (exponential family in z/v). So B_s = (1/s - 1/s') I + Sigma_(s')/s'^2 - Sigma_s/s^2, and 1/s - 1/s' <= 0 for s >= s'. The weight (2/beta)(s_1 - s)/s'^2 = 2(3/4 - x)/(1 - x)^2 <= 2 on [1/2, 3/4] because (1-x)^2 - (3/4 - x) = (x - 1/2)^2. HOLDS.

**(6). HOLDS.** It is (4) plus row 1631 (6) (checked in check 1634). The necessary condition S(t) + Q_+(t) > (1/16 + eps) W_t - 2 W_obs/beta follows. Standing: (4) and (6) are UPPER bounds on N. They give a necessary condition for (E1), not a step toward a proof of it.
The content worth recording: the change of Gaussian time (the A-term) can pay at most 2 W_obs/beta = O(W_t / log n) on the window. So the whole order-one rate in (E1) must come from S(t) (spatial-action and midpoint-radius covariances) or from Q_+ (positive bridge curvature). This is the bridge-coordinate form of row 710 section 8 item 3 ("the electric part alone gives K = 1/s, and everything beyond it is the magnetic deficit plus the entropy term"); see 1.2 below.

**(7)-(9). HOLD.**
- (7): h_s = p_delta * h_v, delta = s - s' >= 0, gives grad^2 log h_s = K_z grad^2 log h_v + Cov_(K_z)(grad log h_v); with grad log h_v = (q_v - y)/v and the Hessian formula above, v^2 B_s = Sigma_v(z) - K_z Sigma_v - Cov_(K_z)(q_v - y). Re-derived. HOLDS.
- (8): drop the positive semidefinite covariance; same weight bound 2. HOLDS.
- (9): along z_theta the endpoint law is the exponential family e^(z_theta . x / v) a(dx); d/d theta of Var(w.X) is (1/v) times the third central moment E[(w.(X-q))^2 (z-y).(X-q)]; the mean-derivative term multiplies a centred first moment and vanishes. HOLDS.
- Standing: (8) charges Q_+ only to positive changes of conditional variance, measured by a third central moment (skewness) of the tilted endpoint law. For a Gaussian endpoint law the excess vanishes exactly (row 1636's oscillator check, which I re-derived: F, alpha_s, B_s, and the cancellation 2a_*/beta - a_*/beta - a_*/beta = 0).

**Two signs of [B_s]_Y. HOLDS.**
- At z = 0 the conditional law is a(dx)/int a for both resolutions (|x|^2 = L). E X = 0 and Cov X = I/4 under a: gauge invariance of M Omega at one endpoint makes each link marginal Haar (E x x^T = I/4 on S^3), and the central element -1 at a vertex in one link but not the other kills cross moments (distinct links have distinct endpoint pairs for n >= 3). So B_s(0) = (1/s' - 1/s)((1/s + 1/s')/4 - 1) I, and 1/s + 1/s' = tau/(s s') >= 4 beta. Positive definite for beta > 1 and s > s_0. HOLDS.
- At z = R x_*, R -> infinity: the tilted law concentrates at the unique maximiser x_* (a has a positive continuous density), so both covariances tend to 0 and B_s -> (1/s - 1/s') I < 0. HOLDS.
- tr Y_r > 0 on a nonempty open subset of each region: u_s is entire in z; constancy on an open set forces constancy everywhere, then all moments of (f - c) a vanish and f = c. HOLDS.
- Standing: a qualitative statement with no size, as the file says. Its masses can tend to 0 relative to W_t as K grows.

### 1.1 (10), (11) and the electric-only comparison (12)

**(10). HOLDS.** Re-derived.
- R_j = I_(j+1)/I_j is the mean of x under e^(beta x)(1 - x^2)^(j - 1/2) on (-1, 1) (from d/d beta (beta^(-j) I_j) = beta^(-j) I_(j+1)); R_j' is its variance > 0.
- 1/R_j = 2(j+1)/beta + R_(j+1) (recurrence I_(j-1) - I_(j+1) = (2j/beta) I_j shifted), so R_j/beta = 1/(2(j+1) + beta R_(j+1)) is decreasing, which gives beta R_j' <= R_j.
- With y = beta(1 - x) the density is e^(-y) y^(j-1/2) (2 - y/beta)^(j-1/2) on (0, 2 beta); the likelihood ratio between two couplings is increasing in y (d/dy of log((2 - y/b_2)/(2 - y/b_1)) = 1/(2 b_1 - y) - 1/(2 b_2 - y) > 0 for b_2 > b_1), and the support grows to the right. So beta(1 - R_j) is nondecreasing, which gives beta R_j' <= 1 - R_j.
- So (log R_j)' <= min(1, y_0)/beta with y_0 = (1 - R_j)/R_j, a_j = log(1 + y_0), and min(1, y_0) <= a_j/log 2 by concavity of log(1+y) on [0, 1]. HOLDS.
- The cross-check R_j/beta = E(1 - x^2)/(2j + 1) (integrate the x-derivative of e^(beta x)(1-x^2)^(j+1/2)) and Cov(x^2, x) >= 0 (condition on |x| = u: E[x | u] = u tanh(beta u), and u^2, u tanh(beta u) both increase) HOLDS.

**(11). HOLDS.** g_beta(j) - g_beta(j-1) = (log R_j)' (row 1617 (12)); the clamped electric score telescopes to sum_(j<=q) (log R_j)' d_j(t) (row 1631 (8), checked 1634); positive coefficients and (10) give (11). The consequence (an energy-weighted positive electric excess of at least beta log 2 {(1/16 + eps) W_t - eta_K W_obs} when M_q <= 0) is immediate. HOLDS.

**(12) and the comparison. HOLDS.**
- With the spatial potential deleted, T = C on the invariant space. The spin-label isotypic projectors of each link commute with C, do not depend on beta, and commute with the gauge and centre projections. So every eigenspace of A is a direct sum of label sectors with equal product multiplier, and A' is diagonal in those sectors. On a sector with labels (k_e): m = sum_e sum_(j<=k_e) a_j and b = sum_e sum_(j<=k_e) (log R_j)'. By (10), 0 < b <= m/(beta log 2) on every label sector, hence 0 <= b_r <= (m/(beta log 2)) I on every eigenspace, also at coincidences. (12) follows, and (E1) fails at every point with beta > 1/(kappa_0 log 2). HOLDS.
- Coldness: I_(j+1)(1)/I_j(1) <= 1/(2(j+1)) <= 1/4 (series bound I_(nu+1)/I_nu <= beta/(2(nu+1))); with monotone beta(1 - R_j), a_j >= 1 - R_j >= 3/(4 beta) for beta >= 1. The unprojected normalised trace is (sum_k (k+1)^2 prod_(j<=k) R_j^t)^L <= (1 + 22 y)^L with y = e^(-3t/(4 beta)) <= 1/2 (I get sum_(k>=1) (k+1)^2 2^(1-k) = 22). Projection onto the commuting invariant subspace lowers the trace and keeps the constant vacuum. With t >= n/512 and beta = O(log n), L y -> 0 uniformly, so G -> 0 and the purity (1 + G(2u))/(1 + G(u))^2 -> 1. HOLDS.
- Standing: Proposition EL of row 710 (L82) is the same model, proved for 0 < beta <= 2; row 710 section 8 item 3 already says, as a RECALLED heat-kernel asymptotic and not a proof, that at large beta "the electric part alone gives K = 1/s". New in row 1636: the all-beta rigorous bound (10), the late-cutoff coldness and purity, and stating the separation on the prescribed windows. That "seed passes, (E1) fails" occurs in positive transfer families is ON FILE in substance (check 1613's two-state example; row 1628 family B; row 1637's product example). That a c/beta rate is not selective is ON FILE (row 1618 Theorem 2, check 1622).

**Gaussian check, ON FILE items, 5D/U(1) scope, spectator, quantifier paragraph. HOLD.** The oscillator formulas re-derived (above). The cosine-U(1) R_0 asymptotic: the y-density with power -1/2 tends to the Gamma(1/2) law with mean and variance 1/2, so -log R_0 ~ 1/(2 beta) and R_0' ~ 1/(2 beta^2), and (10) holds for R_0 at late couplings (the ratio (log R_0)'/a_0 tends to 1/beta < 1/(beta log 2)). HOLDS. Spectator: as in row 1631 (checked 1634). Quantifier paragraph: bookkeeping. HOLDS.

**ARGUED paragraph (where the selective estimate is missing).** Agree, as ARGUED.

Row 1636 verdict: every PROVED item HOLDS. No line fails. No correction needed. One wording point: "the all-energy bound ... with a strictly subtracted square" is an upper bound on N, so the RESULT label "(d), a non-tail piece of the observed Wilson slope" is fair only in the sense that it covers all energies and spins; it is not a piece of a lower bound.

**Guide results for row 1636 (floating point, not a proof step).**
- (10): on j = 1..40 and 400 couplings in [0.05, 400], max of (log R_j)' beta log 2 / a_j is 0.745 (< 1), and (log R_j)' > 0 throughout. For R_0 (cosine U(1)) the same ratio is 0.80, 0.71, 0.70, 0.69 at beta = 5, 20, 100, 400 (tends to log 2).
- (1): one-link toy (S^1 in R^2, kernel e^(-beta|x-y|^2/2), potential 1 - cos), a separate implementation by quadrature on a z-grid. At beta = 1.5 and 3, levels 1-3, the right side of (1) agrees with a finite-difference eigenvalue slope to 6 digits (for example 0.058909 and 0.058909; -0.073324 and -0.073324). int g^2 d eta = 1.00000. A_psi lies in [0, 2m/beta] in all six cases. The toy is not a gauge theory; it tests the algebra of (1) and (3) only.
- Memory: the run used 1.38 GB peak resident memory, above the 1 GB limit of the brief (a 58081 x 256 x 2 array). It was one process and ran once (an earlier start failed at import). I did not rerun it.

### 1.2 What row 1636 shows about (E1)

Read together, (3)-(6) and (10)-(12) say where an order-one rate must come from.
- The change of Gaussian time pays at most 2 m/beta per state (A_psi), so O(W_t / log n) in total.
- The electric multipliers pay at most (1/(beta log 2)) times the positive electric-energy excess of the visible states ((10)-(11)). If that excess is of order W_t, the electric part is O(W_t / log n).
- So (E1) at fixed kappa_0 needs one of: an order-one positive magnetic term M_q (an excited visible state with LOWER spatial action than the vacuum, by order kappa_0 m in action units), or a positive electric-energy excess of order beta W_t, or (in bridge form) S(t) + Q_+ of order W_t.
This is the lattice action sum rule (row 710 section 8 item 1: -s dE/ds = Delta N - s Delta R - s Delta V_1, with C. Michael and H. Rothe named in row 711, not read by me either). In the continuum the matching statement is the trace anomaly: for a glueball the excess of the action density is of order m/g^2, not of order m, with the sign fixed by the sign of the beta function (RECALLED, not proved, not read here). Row 1636 makes this split rigorous on the electric side and in bridge coordinates. It proves nothing about the magnetic side.

## 2. Row 1637, line by line

**Quantifiers. HOLDS.** With a_K = inf over cold band points of N/W (inf of the empty set = +infinity): a uniform surplus on the prescribed tail exists iff liminf a_K > kappa; on some subsequence iff limsup a_K > kappa (take half the gap as eps). Bookkeeping, as the file says.

**(1), every spatial symmetry type is met at infinitely many levels. HOLDS.** Re-derived.
- Haar centring: integrating one boundary link of a square makes its holonomy Haar; the trace law is symmetric (g -> -g) with a null zero set, so E[h(w) | rest] = 0; h^2 = 1/4. Zero is a bin boundary.
- Trivial stabiliser: a symmetry of the unordered triple keeps the common normal up to sign; the layer gaps (5, 7, 20) on the circle of length 32 are distinct and their reversals (20, 7, 5), (7, 5, 20), (5, 20, 7) are not cyclic rotations of (5, 7, 20), so each layer is fixed; (2, 3) is fixed mod 32 only by the identity signed permutation; one fixed centre fixes the translation.
- Orthogonality of distinct images: a square S of one image absent from the other meets at most one square of the other (same-normal squares of an image lie in layers at cyclic separation >= 5L, and S has extent 0 or L along that normal); S has a link in none of the other five squares; integrating that link kills the inner product. So the |Gamma| images are orthogonal in output Haar, nonzero (norm 4^(-3)), and orthogonal to constants. The finite-time Wilson flow is an equivariant diffeomorphism, so linear independence and the exclusion of constants pass to the vacuum measure.
- delta_g -> g.f is an injective intertwiner; the momentum projector has identity coefficient n^(-3), an isotypic projector (dim sigma)^2/|Gamma|; so the projected readings are nonzero and nonconstant.
- A finitely-valued nonconstant function has no continuous representative on the connected link manifold; eigenvectors at v > 0 are continuous and Omega > 0 is continuous; so infinitely many spectral components; the vacuum is at most one. The readings are gauge invariant and centre neutral (contractible loops). HOLDS.
- Standing: new. It says no symmetry sector is wholly dark to this design. It says nothing about the lowest level of a sector, or about thermal weight.

**Scope inside a degenerate space. HOLDS.** Row 1617 (2) (ON FILE, checked) gives b/m -> 0+ for high levels at a fixed box.

**Multiplet dichotomy. HOLDS.** Re-derived: one momentum star by irreducibility; the stabiliser of p in O_h acts irreducibly on V_p (Mackey; fine translations act by scalars); grid translation by L e_j acts on V_p by exp(2 pi i k_j/32); under the stated hypothesis the grid projectors separate the V_p; ran J_v is invariant under grid translations and signed permutations about the origin (both map the n/32 grid and its bins to themselves); so J_v = 0 or F_v. Representatives with |k_i| < 16 give distinct residues mod 32. HOLDS. New.

**Adjoint pair. HOLDS.** 4w^2 - 1 is the adjoint character; X > 4 where both |w_i| > 7/8 (4 * 49/64 - 1 = 33/16 > 2); X < 0 where |w_1| > 7/8, |w_2| < 1/8; both events are unions of joint cells of positive vacuum probability; so E_C(X - E X) is not zero. Content is small (X is almost a function of the two bins). The file's caveat (no claim about a bound state, its energy or slope) is correct.

**Size of the observation space. HOLDS.** 32^3/2 xy-squares of even base parity are link-disjoint (adjacent squares have opposite parity; 32 is even, so the parity is consistent across seams); their output holonomies are independent Haar; 16 bins each of positive probability; hence M + 1 >= 16^(32^3/2). The cold count sum_(tm<=B) dim F_v <= c e^B is immediate. HOLDS.

**(2), the observed heat trace on a cold interval. HOLDS.** Re-derived.
- Fixed-box real analyticity of the kernel in beta, simple vacuum, analytic projections of isolated clusters; Rellich-type analytic branches (the file's induction is the standard reduction); generic ranks j_i of the Gram minors; P_i A' P_i = v_i' P_i, so on a regular branch Tr(J b) = j_i v_i'/v_i.
- d/d beta (j v^t) = t v^t j (v'/v - kappa m) on the kappa-characteristic (t' = kappa t). Summed: t (N - kappa W_o).
- The cutoff chi_eta and the tail bounds (H = sup sum v^2 dim F_v, D = sup ||A'||, t_0 > 3, v |chi_eta'| <= 4) give uniform convergence of the continued sums and of their derivatives at regular points. HOLDS.
- (3): if N > kappa W on the regular interior then N - kappa W_o > kappa W_D a.e., so G(y) >= G_o-hat(y) > kappa int t W_D, against (3). HOLDS.

**(4). HOLDS.** Coldness gives tm >= a, so t m e^(-tm) >= w(a, B) on [a, B] (z e^(-z) is unimodal); G_o-hat(y) <= G(y) - d e^(-B) by continuity from regular points; the contradiction is as for (3). The monotone-branch example (m' <= 0 on hidden branches with positive slope gives t m <= e^(kappa(y-x)) B_0) and the dimension-count variant HOLD.

**Two examples. HOLD.** The four-state family (N = z s^t with W independent of z at beta_*; P = rI + (1-r) Pi + (s-r) O is positive) and the two-bit product (b = kappa m on every branch; G = 1/16 + 1/64 + 1/1024 < 1/8; w(log 2, log 16) = (log 2)/4 >= 1/8; (4) holds; with both bits observed N = kappa W, no surplus; purity >= 64/81 > 457/625). Small content: (4) is sufficient, not necessary, for an (E1) failure. Same mechanism as row 1628 families A, B and check 1625 section 3 (ON FILE).

**(5). HOLDS.** The one-step slab action is in [0, 12 n^3] (3n^3 temporal plaquettes with action <= 2; two half-weighted spatial slices of 3n^3 plaquettes); so ||T'|| <= 12 n^3 lambda_0, |lambda_0'| <= 12 n^3 lambda_0 and ||A'|| <= 24 n^3 (ON FILE as the marked-kernel bound, row 1624 (21), row 1628 (12)). Then |N| <= 24 n^3 G(tau) e^(-(t-1-tau) m_o) and W >= d_1 m_1 e^(-t m_1). With tau = (t-1)/2, G(tau) <= C and tau m_o - t m_1 >= (4 + xi) log n, |N|/W = O(n^(-xi)) because 1/m_1 <= t/a = O(n). HOLDS.
Standing: new as stated; the method is row 1626 (4)-(6) (energy truncation with the marked kernel). The premise needs m_o > 2 m_1 + 2(4 + xi) log n / t: the lowest VISIBLE level must lie above twice the lowest level.

**Three laws.**
- 4D SU(2) ARGUED paragraph: agree, as ARGUED.
- Gaussian laws: ON FILE (row 1628 (22)).
- Cold-point qualification (Q = +-2 e_1 give G >= 2 exp(-2t/(beta n)) -> 2 on late windows, so late compact Gaussian windows have no cold points): HOLDS. ON FILE in substance: check 1622 L79 ("Its cold tori lie at t > 1.7 beta n ... where this model is hot (G > 5)"). Consequence for the brief's framing: restricted to cold points, (E1) is vacuous, not failing, for compact Gaussian U(1) on the prescribed late windows; the chain fails there at HOT and at the cold set. Row 1631's comparison paragraph already warned of this ("does not establish that a specified characteristic enters the cold region").
- Weak 4D Wilson U(1), symmetry only: flat shifts (phases with trivial product round every contractible loop) commute with the cosine action, the flow and the transfer; nonzero charges are exactly invisible to contractible loops; link inversion fixes every real-trace bin, so the C-odd part of Q = 0 is invisible too. HOLDS. Note: the single-photon states of compact U(1) are C-odd, so under this design they are exactly hidden. This makes the abelian hidden fraction large for a reason of the group (U(1) has an outer charge conjugation; in SU(2) it is inner). By Lemma ALG (row 1553) this is a group-level difference and cannot by itself be the selective step.
- 5D SU(2): the counts (40 n^4; fourth coordinates 0, 6L, 14L with gap multisets {5, 7, 20} and {6, 8, 18}) and the commutator argument against a nonabelian flat shift HOLD.

**Surviving estimate.** A restatement of check 1634 section 4. ON FILE.

Row 1637 verdict: every PROVED item HOLDS. No line fails. No correction needed. Wording: "Persistent invisible thermal weight ... would force a violation of E1" should say "at some interior point of each such interval", which is what (2)-(4) prove.

## 3. The decisive question: the electric-only comparison

### 3.1 Is it a fair proxy for the Wilson band? No. It is far from it.

1. Spectrum. Each unit of electric label costs a_j >= 3/(4 beta) (PROVED in row 1636). So every excited level has t m >= 3t/(4 beta), of order n/log n on the windows. The model is cold trivially, and its purity tends to 1 because of a LATTICE-scale gap of order 1/log n. On the Wilson band the cold points have t m of order one to a few tens, and the thermally relevant levels have m of order 1/n. GUIDE (dilute-gas picture of check 1630 1.3(e)): at aspect about 512, G <= 1/2 needs t M of about 20-25 for the lowest mass M.
2. Dynamics. With no spatial plaquettes the links do not interact (apart from the gauge projection). There is no running and no trace anomaly. The only beta-dependence is the one-link Bessel multiplier, which gives b <= m/(beta log 2). This is the c/beta rate of row 1618 Theorem 2 and check 1622, here in an SU(2) model. ON FILE: a c/beta rate is not selective.
3. Calibration. The beta_K are only numbers here. The model has no calibrated trajectory. Its passing seed does not enter the seed-to-gap chain, which uses the Wilson calibration (check 1453).
4. It is the model of row 710 Proposition EL (the strong-coupling Kogut-Susskind Hamiltonian with the magnetic term deleted), moved to weak bare coupling.

### 3.2 What it says about (E1)

- It shows that the numerical seed does not imply (E1) in positive transfer families, even with the SU(2) group, centre, dimension, lattice and bare sequence. That seed does not imply (E1) in general families is ON FILE in substance (check 1613's two-state example; row 1628 family B; row 1637's two-bit product). New: the same-group form.
- It does not show that (E1) is stronger than what the WILSON gap needs. Whether (E1) holds for Wilson SU(2) is untouched.
- Its useful content is negative and structural (1.2): at fixed kappa_0 > 0, the order-one rate cannot come from the electric multipliers or from the change of Gaussian time. It must come from the magnetic term (an excited visible state with lower spatial action than the vacuum, by about kappa_0 m in action units), or from an electric-energy excess of order beta W_t. That is the lattice action sum rule at order-one coupling (row 710 section 8). Row 710 section 8 item 4 already concluded that a proof there "would need bounds of order one on them [the anisotropy coefficients], and that is a statement of the same kind as (VIR_K)".

### 3.3 Is (E1) likely false for Wilson SU(2)?

Not decided. My reading (GUIDE and BELIEF, not proof):
- Infrared stretch (large physical boxes). Levels in the scaling regime have rate -d log m/d beta close to 3 pi^2/11 = 2.69 (asymptotic scaling, the registry's kappa_s). At cold points of aspect 512 the thermal momenta are nonrelativistic (p of order M/5), so momentum dilution is small. Exact visibility with all delays is generic (3.4 and section 4). So (E1) at kappa_0 = 1/16 is plausible there, with a large margin.
- Band. In a box of physical side L the rate is about kappa_s d log(E(L) L)/d log L. This is positive and of order one if E(L) L increases with L. No proof is on file.
- Weak part (if L_h is a weak box, check 1630 1.3(c)). Perturbative levels have small rates (O(g^4) for momentum states, about 1/(3 beta_box) for toron states), and row 1633 section 5.2 ARGUES rising two-gluon levels (b < 0) on the weak torus (one-plaquette version PROVED, row 1633 Theorem 2.2, check 1635). This is where (E1) at a fixed kappa_0 could fail. It also interacts with (RB).
So (E1) is not likely false on the band and the infrared stretch, but it is at risk on the weak part of the window. Nothing on file decides either part.

### 3.4 Is the (E1) route still worth proof rows?

Check 1635: if the delay closure hides nothing (D = 0), (E1) is (VIR-down) with a margin. Row 1637 (1) and its multiplet dichotomy (PROVED), and row 1633 section 5.2 (ARGUED), both point to D = 0 or a negligible hidden fraction on Wilson boxes. Then (E1) is (VIR-down) on the band. By 3.2, at order-one coupling that is a non-perturbative lattice trace-anomaly inequality: the K-II input of row 1386 itself. The route adds no reduction. It renames the crux.
Rows 1628-1637 (ten rows, all checked) produced identities, tail cuts, upper bounds, toy separations and obstruction implications with unproved premises. None gave a lower bound on the visible slope. The two rows checked here bound N from ABOVE. Upper bounds cannot prove (E1).

## 4. Row 1637's premises on the calibrated 4D SU(2) band

**(P1) Persistent invisible thermal weight.** (4) needs only a few exactly hidden eigenvectors with t m <= B on a cold interval: d [e^(-B) + kappa (y - x) w(a, B)] >= G(y), with G(y) <= c. Plausibility: low (ARGUED here).
- Analyticity. On a fixed box the overlaps of a branch with the cell vectors are real analytic in beta. Exact hiding on an interval is then an analytic identity on the whole chart. It needs a structural reason, in practice a symmetry.
- Symmetry. Row 1637 (1) proves that no spatial symmetry type is wholly dark. Its dichotomy proves that an isolated multiplet whose star is distinct mod 32 is wholly visible or wholly dark. Multiplets with aliased momenta (some k_i = 0 or 16 mod 32, or k_i = +-k_j mod 32) can have J_v a proper subspace. But ran E is an enormous permutation module of the grid group (dimension >= 16^(32^3/2)), so a rank deficit there is again non-generic without an extra symmetry. Row 1637 shows that the abelian flat shift, the one symmetry on file that hides whole sectors, has no SU(2) analogue.
- On file: not proved and not refuted. Related: check 1627 section 2 (every level partly hidden, ||E f_i|| < 1, for a single delay); row 1628 (17)-(18) (all delays recover every nonzero overlap); row 1633 section 5.2 (ARGUED: D = 0 generic; not checked by check 1635); row 1204 (28) (neutral sources at every momentum, at bounded lattice energy).

**(P2) Separation of the lowest visible energy.** (5) needs tau m_o - t m_1 >= (4 + xi) log n with tau = (t-1)/2, that is m_o > 2 m_1 + 2(4 + xi) log n / t. So the lowest visible level must lie above twice the lowest level. Plausibility: very low (ARGUED here). The lowest level of the neutral sector at a cold band point sits at zero momentum. Its star is one point, so the dichotomy applies: the whole level is visible or the whole level is dark. Dark would mean every flowed-loop cell vector has zero overlap with the lowest level of its symmetry type, and the loops are the standard probes of exactly those levels. On file: not proved and not refuted. Row 1624 (14) and row 1628 (17) give only that some excited level is visible.

Conclusion: neither premise is established. Both are implausible on the band. Row 1637 therefore gives no credible refutation route for (E1). Its use is to say what a refutation would need.

## 5. Selectivity (Lemma ALG, row 1553)

No proved item in either file reads a property of 4D SU(2) that weak 4D U(1) and 5D SU(2) lack.
- Row 1636 (1)-(9): the files prove them for cosine U(1) (links as unit vectors in R^2, origin covariance I/2) and for 5D SU(2) (L = 4n^4). I re-checked the changes. They read only the Euclidean Gaussian temporal weight on a product of spheres.
- Row 1636 (10)-(12): one-link Bessel facts. They hold for every SU(2) dimension, and for U(1) except R_0, which (10) covers at late couplings (guide ratio 0.69-0.80 < 1). They read the compact group's one-link multiplier: a group-level property, which Lemma ALG excludes as a selective step.
- Row 1637 (1)-(5): spatial-group counting, Haar centring, fixed-box analytic perturbation theory, and the marked-kernel norm. Its 5D and U(1) forms are proved in the file (U(1) inside the Q = 0, C-even sector).
- The one group-dependent proved difference is exact hiding of the charged and C-odd sectors in U(1) (flat shifts; link inversion), which fails in SU(2). It is abelian against nonabelian, a statement about the algebra and centre, so Lemma ALG excludes it as the selective step. Row 1637 also notes that it gives no sign of N for weak Wilson U(1).
- Tests: (g4) the spectator passes every proved bound in both files while the seed fails (row 1636 PROVED; row 1631 and check 1634). (g1) In compact Gaussian U(1) the late windows have no cold points (ON FILE, check 1622 L79), so (E1) at cold points is vacuous there, not failing; the chain fails at HOT. (g2) Weak 5D SU(2): every proved item holds; the sign is open in both files.
- Row 1636's electric-only separation is one more instance of Lemma ALG: same algebra, centre and dimension, seed passes, (E1) fails.

## 6. New and on file

| Statement | Standing |
|---|---|
| 1636 (1): slope = midpoint gradient term - 2 Cov(g^2, H) - Cov(f^2, V); equivalently 2 Cov_eta(g^2, |Z|^2) - Cov_pi(f^2, V) | New as a slope formula; midpoint ON FILE (row 941), radius reading ON FILE (row 1290) |
| 1636 (2) | New; a gradient norm written as a covariance |
| 1636 (3)-(4): A_psi in [0, 2m/beta], (log F)'' = D - C, the block form with Gamma_t | New; F' = int |grad u|^2 ON FILE (row 947); Bochner identity standard |
| 1636 (5)-(9) | New; the conditional-variance derivative is in row 947 section 5.6 (COV-dir); the marginal-Hessian identity in the convex maximal-correlation note |
| 1636 two-sign test | New, qualitative |
| 1636 (10) | New as an all-beta bound; row 710 section 8 item 3 has the heat-kernel form as RECALLED asymptotics |
| 1636 (11) | New combination of (10) with row 1631 (8) |
| 1636 electric-only separation (12) | Model ON FILE (row 710 Proposition EL, beta <= 2). Separation new in same-group form; "seed does not imply (E1)" ON FILE in substance (check 1613, row 1628 family B); "c/beta not selective" ON FILE (row 1618 Thm 2, check 1622) |
| 1636 Gaussian, spectator, U(1)/5D scope | Gaussian bridge ON FILE (row 947 section 5.4); spectator ON FILE (rows 1553, 1631); scope new, immediate |
| 1637 quantifiers, (2)-(4) | New; (4)'s mechanism (one hidden slow level) ON FILE (check 1625 section 3, row 1628 families A, B) |
| 1637 (1), multiplet dichotomy, observation-space size | New |
| 1637 adjoint pair | New, small content |
| 1637 (5) | New as stated; method of row 1626 (4)-(6); norm bound ON FILE (row 1624 (21)) |
| 1637 compact-Gaussian cold-point emptiness | ON FILE in substance (check 1622 L79) |
| 1637 U(1) flat shift and C-odd hiding | Flat shift ON FILE (row 1171, rows 1626-1627); C-odd hiding new, immediate |
| 1637 5D adaptations and non-abelian flat-shift failure | New, immediate |
| This check: (E1) as the lattice action sum rule at order-one coupling; analyticity argument against (P1); dichotomy argument against (P2) | ARGUED here; the action-sum-rule reading is ON FILE in row 710 section 8 |

Independence: both files are by one model (gpt-6.2-astra max). My check re-derives the same routes by hand. The only different data path is the floating-point guide for (1), the A-bound of (3) and (10), which is not a proof. Nothing on the critical path moved: (E1), (VIR-down) on the band, (HOT), (PUR-io) and the gap stay open.

Suggested registry note for VIR-DOWN (not edited by me): "Rows 1636-1637 (check 1639): the visible slope splits as midpoint-radius covariance minus spatial-action covariance; the change of Gaussian time pays at most 2 W_obs/beta and the electric multipliers at most 1/(beta log 2) per unit of positive electric-energy excess, so an order-one rate must come from the magnetic action deficit (the lattice action sum rule). Electric-only 4D SU(2): seed passes, (E1) fails (rate <= 1/(beta log 2)). Refutation premises of row 1637 (persistent exact hiding; lowest visible level above twice the lowest) not established and ARGUED implausible. (E1) route stopped; reopen on a proved order-one lower bound for the magnetic deficit of visible levels."

## RESULT

Row 1636: (1)-(12), the two-sign test, the Gaussian check, the U(1)/5D scope and the spectator all HOLD; no line fails.
Row 1637: quantifiers, (1), the multiplet dichotomy, adjoint pair, observation-space size, (2)-(5), both examples and the three-law items HOLD.
Guide (floats): (1) matches a finite-difference slope to 6 digits on a one-link toy; (10) ratio <= 0.745. The run peaked at 1.38 GB, over the 1 GB limit.
Both files bound N from above. They give necessary conditions and an obstruction with unproved premises; no lower bound on the visible slope.
Electric-only comparison: far from the band (lattice-scale gap, t m ~ n/log n, no running, no calibration; row 710 Prop EL).
It shows the seed does not imply (E1) (ON FILE in substance: check 1613, row 1628 B). It says nothing about whether (E1) holds for Wilson.
Its real content: an order-one rate must come from the magnetic action deficit, i.e. the lattice action sum rule / trace anomaly at order-one coupling.
Row 1637's premises (persistent exact hiding; m_o > 2 m_1) are not on file and ARGUED implausible (analyticity; the dichotomy).
Selectivity: no proved item reads a 4D SU(2) property absent in weak 4D U(1) or 5D SU(2) (Lemma ALG); compact Gaussian U(1) has no cold points (check 1622).
Recommendation: STOP the (E1) route. With D = 0 (argued generic) (E1) is (VIR-down) with a margin, i.e. the order-one running (K-II) input itself.
Ten rows gave no lower bound. Spend proof rows on the order-one magnetic-deficit / running statement directly; reopen (E1) only if such a bound appears.
