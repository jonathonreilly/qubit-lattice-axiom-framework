lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T07:31Z

# Upper chain by hand: the Gruss bound, marginal convexity, the nest objection

Queue item 17, `hand-upper`, neutral. Statements pinned at commit 28e261c17. Finished report; the status table is section 4.

Provenance: Anthropic claude-opus-5-5, effort max, Mac mini worker, commit 28e261c17. Same-model work, not independent and not an audit. Research-stage working state; it grants no status. Paths are relative to the target folder. The source rows are the Upper chain section of `gates/compute-inventory-39189b75b.md`.

## 1. The Gruss bound and Lemma 20.2 (discharged)

**Lemma G (Gruss, with the constant 1/4; credit Gruss, 1935; proof written here).** Let mu be a probability measure and f, g real measurable functions with a <= f <= a + o_f and b <= g <= b + o_g. Then |Cov_mu(f, g)| <= (1/4) o_f o_g.

*Proof.* For a constant m, E (f - m)^2 = Var f + (E f - m)^2 >= Var f. Take m := a + o_f / 2. Then |f - m| <= o_f / 2, so Var f <= o_f^2 / 4. Likewise Var g <= o_g^2 / 4. Cauchy-Schwarz gives |Cov(f, g)|^2 <= Var f Var g. []

**Lemma 20.2, written out.** `parts/upper-chain.md`, Text 20.2. Hypotheses made explicit: K_1, K_2 > 0 are measurable, and Z(a_0, b_0) is finite and positive at one pair. Conclusion as printed, with 4 artanh(t) read as +infinity when t >= 1:

    |log CR(Z)| <= 4 artanh(t),   t := sinh e_1 sinh e_2 exp(e_1 + e_2).

*Proof.* Fix a_0, x_0, y_0, b_0. Put E_1(a, x) := log[ K_1(a, x) K_1(a_0, x_0) / (K_1(a, x_0) K_1(a_0, x)) ], a log cross-ratio of K_1, so |E_1| <= e_1. With v(x) := K_1(a_0, x), u(a) := K_1(a, x_0) / K_1(a_0, x_0), f_a := exp E_1(a, .), we have K_1(a, x) = u(a) v(x) f_a(x). Do the same for K_2: K_2(y, b) = u'(b) v'(y) g_b(y), v'(y) := K_2(y, b_0), |log g_b| <= e_2. Let N := integral v v' d rho = Z(a_0, b_0), and rho-tilde := v v' rho / N, a probability measure. Then Z(a, b) = N u(a) u'(b) E[f_a g_b]. This also shows Z is finite and positive everywhere.

Since exp(-e_i) <= f_a, g_b <= exp(e_i), we have osc f_a <= 2 sinh e_1, osc g_b <= 2 sinh e_2, E f_a >= exp(-e_1), E g_b >= exp(-e_2). Let c(a, b) := Cov(f_a, g_b) / (E f_a E g_b). Lemma G gives |c| <= t. Now

    Z(a, b) = N [u(a) E f_a] [u'(b) E g_b] (1 + c(a, b)),

and in CR(Z) the two bracketed factors cancel exactly. What remains is (1 + c(a, b)) (1 + c(a', b')) / ((1 + c(a, b')) (1 + c(a', b))). For t < 1, two values of log(1 + c) differ by at most log((1 + t) / (1 - t)) = 2 artanh t, and there are two such differences. []

*The bound 7 e_1 e_2 for e_i <= 1/4, by hand.*

- sinh e = e (1 + sum_(j>=1) e^(2j) / (2j + 1)!) <= e (1 + (e^2 / 6) / (1 - e^2)) <= (81/80) e, as (1/96) / (15/16) = 1/90 <= 1/80.
- exp(1/2) <= 5/3, as exp(1) < 2 + 1/2 + 1/6 + 1/24 + (1/120)(6/5) < 2.72 < 25/9.
- So t <= (81/80)^2 (5/3) e_1 e_2 <= (7/4) e_1 e_2 <= 7/64 < 1/9. [(81/80)^2 = 6561/6400 < 1.03, and 1.03 * 5/3 < 7/4.]
- artanh t = sum_(j>=0) t^(2j+1) / (2j + 1) <= t / (1 - t^2) <= (81/80) t, for t <= 1/9.
- So 4 artanh t <= (81/80)^3 (20/3) e_1 e_2 <= 7 e_1 e_2, as 20 * 531441 = 10628820 <= 10752000 = 21 * 512000, which says (81/80)^3 <= 21/20.

*The iteration.* If kernels K^(n) over n slabs have the two-slab form with K_1 = K^(n-1), K_2 = K^(1), and e_1 := eps(D_1) <= 1/7, then eps(n D_1) <= (1/7)(7 e_1)^n. Induction: the bound gives eps((n - 1) D_1) <= e_1 <= 1/4, so the lemma applies and eps(n D_1) <= 7 eps((n - 1) D_1) e_1. The printed line in Text 20.2 needs 7 eps(D_1) <= 1 for this, which it does not state; it is what "once e_i are small" has to mean.

*Remark, not consumed.* For fixed a, log f_a(x) - log f_a(x') is itself a log cross-ratio, so f_a / inf f_a lies in [1, exp e_1]. c(a, b) does not change when f_a, g_b are rescaled by constants, so Lemma G gives the sharper |c| <= (1/4)(exp e_1 - 1)(exp e_2 - 1), of order e_1 e_2 / 4 and not e_1 e_2.

## 2. Marginal convexity, and what it leaves of Lemma 21.5 (discharged, except the one citation named at the end)

The inventory proposed a weighted Brascamp-Lieb estimate with boundary conditions. Nothing of that is needed. The route below is the classical one through Prekopa-Leindler: boundaries never appear, since indicators of convex sets enter as functions, and no second derivative of the marginal is taken. Credit: Prekopa, Leindler, Brascamp and Lieb for the inequalities; Bobkov and Ledoux for reading Poincare off Prekopa-Leindler, by the expansion in Lemma P. All proofs are written here.

**Convention.** A convex set and its interior differ by a null set, so integrals over K are integrals over int K. So take K_x, K_y open and convex, and S of class C^2 on K_x x K_y. Hessians of S mean Hessians there.

**Lemma PL (Prekopa-Leindler, midpoint form).** Let f, g, h: R^N -> [0, infinity] be Borel with h((u + v)/2) >= (f(u) g(v))^(1/2) for all u, v, reading 0 * infinity as 0. Then integral h >= ( integral f integral g )^(1/2).

*Proof, N = 1.* If integral f = 0 or integral g = 0 there is nothing to prove. Replacing f, g by min(f, n) 1_[-n, n], min(g, n) 1_[-n, n] keeps the hypothesis, and monotone convergence recovers the claim, so take f, g bounded with positive integrals. Divide f by sup f, g by sup g, h by (sup f sup g)^(1/2): hypothesis and conclusion scale alike, and now sup f = sup g = 1. For 0 < t < 1 the sets A_t := {f > t}, B_t := {g > t} are not empty, and u in A_t, v in B_t give h((u + v)/2) > t, so C_t := {h > t} contains (A_t + B_t)/2. Let A', B' be non-empty compact subsets of A_t, B_t. Translating so that max A' = 0 = min B' gives A' u B' in A' + B' with A' n B' = {0}, so |A' + B'| >= |A'| + |B'|. So |C_t| >= (|A'| + |B'|)/2, and by inner regularity |C_t| >= (|A_t| + |B_t|)/2. Integrating over t in (0, 1), and using f, g <= 1,

    integral h >= integral_0^1 |C_t| dt >= (1/2)(integral f + integral g) >= (integral f integral g)^(1/2).

*N >= 2.* Write u = (u', u_N). For real a, b, c := (a + b)/2, the sections f(., a), g(., b), h(., c) obey the hypothesis in R^(N-1). So F(a) := integral f(u', a) du', and G, H likewise, obey H((a + b)/2) >= (F(a) G(b))^(1/2), by induction. They are Borel into [0, infinity] by Tonelli. The case N = 1 and Tonelli finish. []

**Lemma M (marginal inequality).** Let S be C^2 on K_x x K_y with S_xx positive definite at every point, and let Sigma be a constant symmetric matrix with

    S_yy - S_yx S_xx^-1 S_xy >= Sigma     at every point (x, y).

Let Z(y) := integral_(K_x) exp(-S(x, y)) dx, with values in [0, infinity]. Then for y, y + eta, y - eta in K_y,

    Z(y)^2 >= exp(eta . Sigma eta) Z(y + eta) Z(y - eta).

*Proof.* Let u, v be in K_x, w := (u + v)/2, xi := (u - v)/2, and g(s) := S(w + s xi, y + s eta) on [-1, 1]; the segment lies in the convex set K_x x K_y. Two integrations by parts give g(1) + g(-1) - 2 g(0) = integral_(-1)^1 (1 - |s|) g''(s) ds. And g''(s) is the Hessian form at (xi, eta), which at each s is at least its minimum over xi, namely eta . (S_yy - S_yx S_xx^-1 S_xy) eta >= eta . Sigma eta. The weight 1 - |s| has mass 1. So

    (1/2)[ S(u, y + eta) + S(v, y - eta) ] - S(w, y) >= (1/2) eta . Sigma eta.

Apply Lemma PL to f := 1_(K_x) exp(-S(., y + eta)), g := 1_(K_x) exp(-S(., y - eta)), h := 1_(K_x) exp(-S(., y) + eta . Sigma eta / 2). []

The Schur complement here depends on the point. That is why the minimum over xi has to be taken at each s, and the display "Hess >= S_yy - S_yx S_xx^-1 S_xy" of Step 4 means this uniform form. Monotonicity is immediate from the same minimum: if Hess S >= A, a constant positive definite matrix, then eta . Schur(Hess S) eta = min_xi (xi, eta) . Hess S (xi, eta) >= min_xi (xi, eta) . A (xi, eta) = eta . Schur(A) eta. So Lemma M holds with Sigma := Schur(A), which is the statement used after eliminating a middle variable.

**Corollary M'.** If Z is finite, positive and continuous on K_y, then V := -log Z obeys V(y + eta) + V(y - eta) - 2 V(y) >= eta . Sigma eta. So V - y . Sigma y / 2 is midpoint convex and continuous, hence convex: convexity at dyadic weights follows by induction, and continuity extends it to all weights. If V is C^2, then Hess V >= Sigma at every point. []

**Lemma P (Poincare, from the midpoint inequality).** Let K be open and convex in R^N, V: K -> R Borel with finite positive integral of exp(-V), mu the normalized law, and c > 0 with

    (V(u) + V(v))/2 - V((u + v)/2) >= (c/8) |u - v|^2     for all u, v in K.      (mid)

Then Var_mu(g) <= (1/c) E_mu |grad g|^2 for g bounded, C^1 on K, with sup |grad g| =: l finite.

*Proof.* Take E g = 0, and b := sup |g|. For t > 0 put Q_t g(z) := sup_(x in K) [ g(x) - (c/t) |x - z|^2 ]. For x, y in K, z := (x + y)/2, (mid) and |x - y| = 2 |x - z| give

    (t/2) g(x) - (V(x) + V(y))/2 <= (t/2) [ g(x) - (c/t)|x - z|^2 ] - V(z) <= (t/2) Q_t g(z) - V(z).

So Lemma PL, applied to exp(t g - V), exp(-V), exp((t/2) Q_t g - V), all on K, gives

    E exp((t/2) Q_t g) >= ( E exp(t g) )^(1/2).      (1)

Let G_t := (Q_t g - g)/t. Then 0 <= G_t <= B := l^2 / (4 c), since g(x) - g(z) <= l rho and sup_(rho >= 0) (l rho - (c/t) rho^2) = l^2 t / (4 c). In the supremum only x with (c/t) |x - z|^2 <= g(x) - g(z) <= l |x - z| matter, so |x - z| <= l t / c. Differentiability at z then gives limsup_(t -> 0) G_t(z) <= |grad g(z)|^2 / (4 c). Expand (1), all terms bounded in terms of b, B: the left side is 1 + (t^2/8) E g^2 + (t^2/2) E G_t + O(t^3), and the right side is 1 + (t^2/4) E g^2 + O(t^3). So E g^2 <= 4 E G_t + O(t). Let t -> 0, with reverse Fatou, as 0 <= G_t <= B. []

*Unbounded g.* If g is C^1 with bounded gradient and g is in L^2(mu), apply the lemma to b theta(g / b), theta odd, C^1, bounded, with theta(w) = w on [-1, 1] and 0 <= theta' <= 1, and let b -> infinity.

**Lemma 21.5 re-read.** `library/convex-maximal-correlation.md`, in the coordinates of its first line: S_xx >= 1, S_yy >= 1, ||S_xy|| <= r < 1, on K_x x K_y, open convex. The joint Hessian is at least 1 - r, so exp(-S) has Gaussian tails along every line from a fixed point, the normalizer is finite, and every marginal and conditional law below has all moments.

- *Step 1.* Hess U >= 1 gives (mid) with c = 1 by the Taylor identity in the proof of Lemma M with xi = 0. Lemma P gives the Poincare inequality; no semigroup is used.
- *Step 2, with its regularity.* Let LL(K) be the bounded C^1 functions on K with bounded gradient, and G in LL(K_y). For x in a compact ball in K_x and fixed y_0, Hess_y S >= 1 gives S(x, y) >= -C - C |y - y_0| + |y - y_0|^2 / 2, and ||S_xy|| <= r gives |S_x(x, y)| <= C + r |y - y_0|. So derivatives in x pass under the integral, and d_e g(x) = -Cov_(y | x)(G, e . S_x), with no boundary term, since K_y does not move with x. e . S_x(x, .) is C^1 with gradient of norm at most r and lies in L^2, so Lemma P in its unbounded form bounds the covariance, and |grad g(x)| <= r ||grad G||_(L^2(. | x)). Hence g is in LL(K_x), and the printed inequality follows. The same holds with x, y exchanged.
- *Step 4.* S_xx^-1 <= 1 gives S_yy - S_yx S_xx^-1 S_xy >= 1 - r^2 at every point. Z(y) is finite, positive and continuous, by the domination of Step 2 with the roles exchanged. Lemma M with Sigma := 1 - r^2 is (mid) for V = -log Z with c = 1 - r^2, and Lemma P gives Var_(p_y)(h) <= (1 - r^2)^-1 E |grad h|^2 on LL(K_y). No derivative of V is taken.
- *Step 5.* LL(K_y) is T-invariant by Step 2, and it is dense in L^2(p_y), as it contains the restrictions of C_c^infinity. For G in LL(K_y) of mean zero, a_n := ||T^n G||_2^2 <= C r^(4 n). The spectral theorem can be replaced by one line: a_n^2 <= a_(n-1) a_(n+1) by Cauchy-Schwarz and self-adjointness. If some a_n = 0, then T G = 0. Otherwise a_(n+1) / a_n is non-decreasing, and it cannot exceed r^4 anywhere, or a_n would outgrow C r^(4 n). So ||T G||_2 <= r^2 ||G||_2.
- *Steps 3, 6.* Unchanged. They are Hilbert space algebra, and I checked them.

**The middle variable.** Let Hess S >= A on K_x x K_z x K_y, a product of open convex sets, A constant and positive definite, with either K_z bounded and S C^2 on its closure, or ||Hess S|| <= H_max. Then S-tilde(w) := -log integral dz exp(-S(w, z)), w := (x, y), is C^2. Domination as in Step 2 allows two derivatives under the integral, and with E_z the law exp(-S) dz normalized,

    d_i S-tilde = E_z[S_i],   d_i d_j S-tilde = E_z[S_ij] - Cov_z(S_i, S_j).

That is the identity the inventory asked for, and the formula printed for S-tilde_xy. Lemma M with z in the role of x and Sigma := Schur(A) gives Hess S-tilde >= Schur(A) by Corollary M', and this bound did not need the identity. As a by-product, Cov_z(e . S_w, e . S_w) <= E_z[e . S_ww e] - e . Schur(A) e, which is the Brascamp-Lieb statement in the only form used here. So the first main theorem applies to S-tilde with A_x, A_y the diagonal blocks of Schur(A).

**Still a citation.** The bound on the mixed block in the library uses the Helffer-Sjostrand representation Cov_z = E_z < grad_z S_x, L^-1 grad_z S_y > and the sign of the Bochner term on a box. Neither is rebuilt here. So the marginal inequality and the reduction to the first theorem are discharged, while the printed rate r <= C (H_max / kappa)^2 exp(-mu' D) keeps that one literature input. Label: gap, outside this item.

## 3. The nest objection of Text 23.5, by hand (discharged as a negative statement at U = 1)

This replaces the machine-supplied exterior cost. Everything below is exact on the lattice. No run is used. `checks/hand_upper/nest_mode_exact.py` is a kill test only: criteria first, exact rationals, all PASS; see 3.7.

**What is refuted.** The sharp form that Text 23.5 tests, ||H/s||^2 <= C (||dH||^2 + ||P_N D^*H||^2) with C absolute. `library/fibre-propagator.md` has since moved to the weight s^#, and Theorem N does not touch that form: see 3.7.

### 3.1 The setting, and the reduction to a line

At U = 1, as in `checks/upper-chain_nest.py`, which is what Text 23.5 tested. Level-l block B_l(y) := y + [0, L^l)^d, y in L^l Z^d. r^(l) is the plain mean on a block. Q^(l) H(y, mu) is the mean over x in B_l(y) of the sum of H_mu along the straight line from x to x + L^l e_mu. Layers Sigma_l are slabs normal to e_1, each a union of whole level-(l+1) blocks. ker bC: Q^(n) H = 0 on all level-n bonds, and Q^(l) H = 0 on level-l bonds with both ends in Sigma_l. P_N is the orthogonal projector on ker r_N, where r_N is r^(n) on all level-n sites and r^(l) on Sigma_l. s(x) := L^l for the least l >= 1 with x in the shadow of Sigma_l, else L^n.

Let f be a real function on the points m of the normal circle, and H^f the field with H_1(x) := f(x_1 + 1) and no other component. So the bond from site m - 1 to site m carries f(m), and site x is the unit interval [x, x + 1]. Then:

- d H^f = 0, and D^* H^f (x) = -delta f(x_1), with delta f(x) := f(x + 1) - f(x).
- Q^(l) H^f (y, 1) = W_sigma[f](y_1 + sigma), sigma := L^l, with W_sigma[f](c) := sum_(|k| < sigma) (1 - |k|/sigma) f(c + k): the pairs (a, j) in [0, sigma)^2 with a + j = sigma - 1 + k number sigma - |k|. The rows with mu != 1 vanish.
- Since layers are unions of whole parent blocks, the rows of r_N span the indicators of the atoms: level-l blocks in the shadow of Sigma_l and off the shadow of the next finer layer, and level-n blocks off every layer. So on functions of x_1 alone, 1 - P_N is the mean over the normal interval of the atom.

All norms below carry one common factor, the number of transverse sites, and it cancels. So write En(f) := sum over atoms I of sum_(x in I) (delta f(x) - mean_I delta f)^2. A layer with sites alpha .. beta - 1 is the closed interval [alpha, beta] of points, and a bond with both ends in it has its kernel centre c strictly inside. So H^f is in ker bC exactly when W_(L^n)[f] = 0 at all multiples of L^n and W_(L^l)[f](c) = 0 at all c in L^l Z strictly inside the interval of Sigma_l.

### 3.2 Theorem N

**Theorem N.** Let L >= 3, n >= 2, 1 <= k <= n - 1, r >= 1, t >= 1, X >= t + 1 be integers, and s_j := L^(n-k+j), so s_0 >= L and M := s_k = L^n. On a normal circle of X M sites, in any d, let Lambda_(k-1) be t consecutive level-n blocks, and for j = k - 1, ..., 1 let Lambda_(j-1) be Lambda_j with r cells of scale s_j removed at each end, assumed non-empty. Lambda_j is the layer of scale s_j. Then there is a non-zero H in ker bC with dH = 0 and

    ||P_N D^* H||^2 <= 284 L^-k Gamma^2 ||H / s||^2,   Gamma <= ( (2 + 16 / (5 L)) 4^(r-1) )^(k-1).

So, with c the best constant, C = 1/c:

- k = 1, one jump: c <= 284 / L, for every thickness t and every exterior X - t >= 1. **So C >= L / 284, and the sharp form with C absolute is false.**
- k = 2, r = 1, two jumps at clearance 1: c <= 284 (2 + 16/(5 L))^2 / L^2.
- General k, r: c <= (284 / L) ( (2 + 16/(5 L))^2 16^(r-1) / L )^(k-1). **At small clearance the loss compounds geometrically with the depth,** as soon as (2 + 16/(5 L))^2 16^(r-1) < L. For r = 1 that is L >= 7.

### 3.3 Four identities

Put h(sigma) := (sigma^2 - 1) / (6 sigma), and M^+_sigma[f](c), M^-_sigma[f](c) := sum_(k=1)^(sigma-1) (1 - k/sigma) f(c +- k). So W_sigma[f](c) = f(c) + M^+ + M^-.

**(I1)** W_(L sigma)[f](c) = sum_(|k| < L) (1 - |k|/L) W_sigma[f](c + k sigma), for every f. *Proof.* W_(L sigma)[f](c) = (L sigma)^-1 sum_(a, j in [0, L sigma)) f(c - L sigma + 1 + a + j). Write a = sigma a' + a'', j = sigma j' + j'', with a', j' in [0, L), a'', j'' in [0, sigma). The sum over a'', j'' is sigma W_sigma[f](c - L sigma + sigma + sigma (a' + j')), and a' + j' = L - 1 + k has L - |k| solutions. []

**(I2)** If f is affine on the cell from c to c + sigma, with end values p at c and w at c + sigma, then M^+_sigma[f](c) = p (sigma - 1)/2 + h(sigma)(w - p). The same for M^- on the cell from c to c - sigma. *Proof.* sum_(k=1)^(sigma-1) (1 - k/sigma) = (sigma - 1)/2, and sum_(k=1)^(sigma-1) (1 - k/sigma)(k/sigma) = h(sigma). [] So if f is affine on both cells at c, with values p', p, w at c - sigma, c, c + sigma, then W_sigma[f](c) = 0 reads

    p' + kappa(sigma) p + w = 0,   kappa(sigma) := sigma / h(sigma) - 2 = (4 sigma^2 + 2) / (sigma^2 - 1) > 4.      (R)

**(I3) Conservation.** If W_sigma[f](c - k sigma) = 0 for k = 1, ..., L - 1, then M^-_(L sigma)[f](c) = M^-_sigma[f](c). The same with + and c + k sigma. *Proof.* Apply (I1) to f_- := f on points < c, and 0 on points >= c. At k >= 1 the kernel of W_sigma(c + k sigma) lies in points > c, so that term vanishes. At k <= -1 it lies in points < c, so W_sigma[f_-] = W_sigma[f] = 0 there. At k = 0, W_sigma[f_-](c) = M^-_sigma[f](c). And W_(L sigma)[f_-](c) = M^-_(L sigma)[f](c). []

**(I4) The exterior cubic.** For an integer M >= 3 and reals A, tau let

    g(m) := A (1 - m/M) + a e_0(m) + b e_1(m),   e_0(m) := m (M - m),   e_1(m) := m (M - m)(2 m - M),   0 <= m <= M,
    a := -6 A (tau + (M - 1)/2) / (M (M^2 - 1)),   b := 30 A (tau M + (M - 1)(M - 2)/6) / (M (M^2 - 1)(M^2 - 4)).

Then g(0) = A, g(M) = 0,

    sum_(m=1)^(M-1) (1 - m/M) g(m) = -tau A,    sum_(m=1)^(M-1) (m/M) g(m) = 0,      (C)

and, for the increments on the block, the energy is

    E(tau, M) := sum_(m=0)^(M-1) (delta g(m) - mean)^2 = 12 A^2 (tau + (M - 1)/2)^2 / (M (M^2 - 1)) + 180 A^2 (tau M + (M - 1)(M - 2)/6)^2 / (M (M^2 - 1)(M^2 - 4)).      (En)

*Proof.* All sums run over 1 <= m <= M - 1, and y := 2 m - M. By parity about M/2, sum e_1 = 0 = sum y e_0. Directly,

    sum e_0 = M (M^2 - 1)/6,    Y := sum y e_1 = M (M^2 - 1)(M^2 - 4)/30,

the second from y^2 = M^2 - 4 e_0 and sum e_0^2 = (M^5 - M)/30. Also sum (1 - m/M) = (M - 1)/2 and sum y (1 - m/M) = -(M - 1)(M - 2)/6. (C) is equivalent to sum g = -tau A and sum y g = tau A M. These read a sum e_0 = -A (tau + (M - 1)/2) and b Y = A (tau M + (M - 1)(M - 2)/6), which are the definitions of a, b. For (En): w := a e_0 + b e_1 vanishes at 0 and M, so mean delta g = -A/M and the mean of delta w is 0. With D^2 w(m) := w(m + 1) + w(m - 1) - 2 w(m), we have D^2 e_0 = -2, D^2 e_1 = -6 y, since D^2 m^3 = 6 m and D^2 m^2 = 2. Summation by parts gives sum_(m=0)^(M-1) (delta w)^2 = -sum w D^2 w = 2 a^2 sum e_0 + 6 b^2 Y = a^2 M (M^2 - 1)/3 + b^2 M (M^2 - 1)(M^2 - 4)/5, the cross terms vanishing by parity. Substitute a, b. []

g is the minimizer of the energy on one block under (C), which is why a cubic and nothing else appears. The trial (1 - u)(1 - 4 u) of Text 23.5 has energy (16/3) A^2 / M but fails the second equation of (C). This cubic at tau = 0, M large, is A (1 - u)(1 - 8 u + 10 u^2), of energy 8 A^2 / M.

### 3.4 The construction

Let rho(sigma) in (0, 1) solve rho + 1/rho = kappa(sigma). As 3/11 + 11/3 < 4 < kappa, rho(sigma) < 3/11.

*Level 0.* Lambda_0 = [alpha_0, beta_0] has T_0 := (beta_0 - alpha_0)/s_0 cells of scale s_0. T_0 is a multiple of L, so T_0 >= 3. Put rho := rho(s_0), and at the nodes alpha_0 + i s_0

    f_i := [ (-rho)^i + (-rho)^(T_0 - i) ] / ( 1 + (-rho)^(T_0) ),   0 <= i <= T_0,

with f affine on each cell. So f_0 = f_(T_0) = 1 =: A_0, and (R) holds at i = 1, ..., T_0 - 1. Let q := -f_1 and tau_0 := (s_0 + 1)/2 - h(s_0)(1 + q). By (I2), the moment of f over the cell inside an edge of Lambda_0 is (tau_0 - 1) A_0.

*Levels j = 1, ..., k - 1.* Go outward from each edge of Lambda_(j-1) through the r cells of scale sigma := s_j, mirror-symmetrically. At distance i sigma from the edge put F_i, with f affine between:

    F_0 := A_(j-1),   F_1 := -a_j A_(j-1),   a_j := (tau_(j-1) + (sigma - 1)/2) / h(sigma) - 1,   F_(i+1) := -kappa(sigma) F_i - F_(i-1).

Let A_j := F_r, R_i := -F_(i+1) / F_i, and tau_j := (sigma + 1)/2 - h(sigma)(1 + 1/R_(r-1)). So the moment over the cell inside an edge of Lambda_j is (tau_j - 1) A_j, by (I2).

*The exterior.* On the level-n block next to each edge of Lambda_(k-1), at distance m from the edge, put g(m) of (I4) with A := A_(k-1), tau := tau_(k-1), M := s_k. If X = t + 1 the one exterior block gets the sum of the two mirror copies. Elsewhere f := 0.

### 3.5 f is admissible, and where its energy sits

**Constraints.** Claim: for each j, W_(s_j)[f] vanishes at all points of the grid s_j Z strictly inside Lambda_j. For j = 0 this is (R). Let it hold at j - 1, and take sigma := s_j and c on that grid, strictly inside Lambda_j. There are three cases.

- c strictly inside Lambda_(j-1). Lambda_(j-1) is a union of cells of scale sigma, so c is at distance at least sigma from its edges, and all c + k s_(j-1), |k| < L, are grid points strictly inside it. (I1) and the claim at j - 1 give 0.
- c an edge of Lambda_(j-1). Its length is at least sigma = L s_(j-1), so (I3) applies on the inner side, and the inner moment is M_(s_(j-1)) = (tau_(j-1) - 1) A_(j-1). (I2) gives the outer moment. So W_sigma[f](c) = A_(j-1) [ tau_(j-1) + (sigma - 1)/2 - h(sigma)(1 + a_j) ] = 0, by the definition of a_j.
- c in an annulus. (R) holds by construction.

At the top level, a multiple of M strictly inside Lambda_(k-1) is the first case again. At an edge, (I3) and (C) give W_M[f] = A + (tau - 1) A - tau A = 0, with A := A_(k-1), tau := tau_(k-1); a mirror copy at distance M adds the second sum of (C), which is 0. At a node at distance M from an edge in the exterior, (C) gives 0 for each copy, and g(M) = 0. At any other multiple of M, f vanishes on the kernel. So H^f is in ker bC, and H^f != 0.

**Energy.** On each cell inside Lambda_0 and each annulus cell, f is affine, and these cells are atoms, so they contribute nothing. Each exterior block adjacent to the nest contributes E(tau_(k-1), M). If X = t + 1, the sum of the mirror copies is the linear function of constant value A plus 2 a e_0, as e_1 is odd about M/2, and it contributes 4 a^2 M (M^2 - 1)/3. All other atoms have f = 0.

### 3.6 The bounds

**(B1) q.** 0 < q <= 3/10. If T_0 is even (so T_0 >= 4), q = (rho + rho^(T_0-1)) / (1 + rho^(T_0)) <= rho + rho^3 < 3/11 + 27/1331 = 390/1331. If T_0 is odd, q = (rho - rho^(T_0-1)) / (1 - rho^(T_0)), so 0 < q <= rho / (1 - rho^3) < (3/11)(1331/1304) = 363/1304.

**(B2) tau, a, R.** For all j, 0 < tau_j <= (s_j + 1)(2 s_j + 1)/(6 s_j) <= (14/27) s_j, and 1 < a_j <= 2 + 16/(5 L), and 1 <= R_i <= 4.

Indeed tau_j has the form (s + 1)/2 - h(s)(1 + w), with s := s_j and w := q at j = 0, w := 1/R_(r-1) at j >= 1. If 0 < w <= 1, then the value lies between (s + 1)(s + 2)/(6 s) > 0 and (s + 1)(2 s + 1)/(6 s) = s/3 + 1/2 + 1/(6 s) <= (14/27) s, the last for s >= 3. Now take j >= 1, sigma := s_j >= 9. a_j = (2 sigma - 1)/(sigma + 1) + 6 sigma tau_(j-1) / (sigma^2 - 1). The first term lies in [1, 2). The second is positive and, as tau_(j-1) <= (14/27) sigma / L, at most (28/(9 L)) (81/80) <= 16/(5 L). So a_j <= 46/15. Let R_* := 1/rho(sigma). Since kappa(sigma) <= kappa(9) = 163/40 < 4 + 1/4, R_* <= 4; and R_* > 11/3 > 46/15. With R_0 = a_j, the rule R_i = kappa - 1/R_(i-1) keeps R_i in [1, R_*]: if 1 <= R_(i-1) <= R_*, then kappa - 1 <= R_i <= kappa - 1/R_* = R_*. So w = 1/R_(r-1) is in (0, 1], and the induction runs.

**(B3) Gamma.** |A_j / A_(j-1)| = a_j R_1 ... R_(r-1) <= (2 + 16/(5 L)) 4^(r-1). So Gamma := |A_(k-1)| obeys the bound of Theorem N.

**(B4) Energy.** With tau := tau_(k-1), s := s_(k-1), M = L s >= 9: 0 < tau <= (14/27) M / L <= 14 M / 81 <= M/5. So tau + (M - 1)/2 <= 7 M / 10, and tau M + (M - 1)(M - 2)/6 <= 11 M^2 / 30. With M^2 >= 81, M^2 / (M^2 - 1) <= 81/80, and M^4 / ((M^2 - 1)(M^2 - 4)) <= 6561/6160 <= 1.07. So, by (En),

    E(tau, M) <= (A^2 / M) ( (147/25)(81/80) + (121/5)(1.07) ) <= 32 A^2 / M.

If X = t + 1, the single block has 4 a^2 M (M^2 - 1)/3 = 48 A^2 (tau + (M - 1)/2)^2 / (M (M^2 - 1)) <= 24 A^2 / M. In every case En(f) <= 64 Gamma^2 / M.

**(B5) Norm.** Bonds strictly inside the first and last cell of Lambda_0 have both ends in the shadow of the layer of scale s_0, where s = s_0, whichever end carries the weight. T_0 >= 3, so these are 2 (s_0 - 1) distinct bonds. On them f = 1 - (1 + q) i / s_0, i = 1, ..., s_0 - 1, and

    G := sum_(i=1)^(s_0-1) (1 - (1 + q) i / s_0)^2 = (s_0 - 1) [ (1 + q)^2 (2 s_0 - 1)/(6 s_0) - q ].

For s_0 >= 3: s_0 - 1 >= 2 s_0 / 3, and (2 s_0 - 1)/(6 s_0) >= 5/18. The function (5/18)(1 + q)^2 - q decreases on [0, 3/10], and it equals 61/360 at 3/10. So G >= 61 s_0 / 540, and ||H/s||^2 >= 2 G / s_0^2 >= 61 / (270 s_0), up to the common factor.

**(B6) Conclusion.** En(f) / ||f/s||^2 <= (64 Gamma^2 / M) (270 s_0 / 61) = (17280/61) L^-k Gamma^2 <= 284 L^-k Gamma^2. []

### 3.7 Remarks

- **The numbers of Text 23.5.** The bounds above are loose on purpose. As L, s_0 -> infinity, the same mode has quotient about 16 sqrt 3 / L = 27.7 / L, or 12 sqrt 3 / L = 20.8 / L when the exterior is one block. Two jumps at clearance 1, mirror geometry: Gamma -> 2, so about 64 sqrt 3 / L^2 = 110.9 / L^2, or 48 sqrt 3 / L^2 = 83.1 / L^2 at one exterior block. These limit values are a remark, checked in floats only, and nothing below rests on them. At L = 25, 41, X = 2 the mode has L Q = 21.4, 21.2, above the printed minima 20.5, 20.6, as a trial field must be. The printed series is not one series: `checks/upper-chain_nest2.py` uses X = 4 below L = 25 and X = 2 from there on, so the rise from 18.1 to 20.5 comes from X and not from L. The fitted 18/L and 90/L^2 stay evidence, and nothing consumes them. K_1 about 5 to 6 is not used.
- **Corrections to the wording of Text 23.5.** The recurrence is p' + kappa(s) p + w = 0 with kappa(s) > 4, and 4 is the limit s -> infinity. So r = -0.268 and the growth 3.73 are limits too; at s = 3, kappa = 19/4. A mode of amplitude A at an inner edge has amplitude about 2 A, 7 A, 26 A at clearance 1, 2, 3 (1, 2, 7, 26 by F_(i+1) = 4 F_i - F_(i-1)), so about half of the printed 3.73^r A. The onset of compounding moves by a constant only.
- **What stands untouched.** (NC) with s^# in `library/fibre-propagator.md` is not contradicted: near a wall s^# is the coarse weight, and at its clearance the amplitude factor is huge. The repaired weight s~ stays unchecked, and Theorem N gives it nothing. This is a negative statement only.
- **Scope.** H^f has zero curvature and is a pure gradient, since sum f = 0 follows from the top constraints. So Theorem N refutes the inequality as displayed, gauge term included. Text 23.5's further reading, that the loss is not a gauge artefact, rests on run N8 and is not rebuilt here. It stays evidence.
- **Runs.** `checks/hand_upper/nest_mode_exact.py`, criteria in its header, all PASS. C1 to C6 are exact in rationals, at 24 configurations including L = 4: every constraint is exactly 0 and every inequality of 3.6 holds. Controls fail as they must, with tau off by 1 or with kappa = 4 in place of kappa(s). C7: the full d = 2 operator of `checks/upper-chain_nest.py` agrees with the line to 1e-9. C8, C9: the Rayleigh minima of `checks/upper-chain_nest2.py` lie below the mode's quotient, by factors 1.13 to 1.81. `checks/hand_upper/marginal_schur_check.py`, three potentials on a box with moving Schur complement: M1, M2 PASS. `checks/hand_upper/nest_limits.py`: L0, L1, L2 PASS. All ran under the numeric lock, with 59 to 67 percent of memory free at the start. These can refute, and they discharge nothing.
- **One rule broken.** The first run of `nest_limits.py` had no RSS guard and peaked at 2.76 GB, above the 2 GB limit of `FINISH.md`. It also had a wrong edge weight in its norm. That run is void, its header records it, and the guarded rerun peaked at 0.62 GB.

## 4. Status

| Statement | Label | Where |
|---|---|---|
| Gruss bound, Lemma 20.2, the bound 7 e_1 e_2, the iteration (needs 7 eps(D_1) <= 1) | discharged | section 1 |
| Prekopa-Leindler; marginal inequality with moving Schur complement; Schur monotonicity | discharged | section 2 |
| Poincare on convex sets, from Prekopa-Leindler | discharged | section 2, Lemma P |
| Lemma 21.5, first theorem, with its regularity | discharged, same-model reading | section 2 |
| Hess S-tilde >= Schur(A) and the formula for S-tilde_xy | discharged, under K_z bounded or ||Hess S|| <= H_max | section 2 |
| Helffer-Sjostrand form and Bochner sign in the printed rate of the middle variable | gap, not in this item | library note |
| Sharp-weight nest coercivity is false, c <= 284/L; compounding at small clearance | discharged at U = 1, flat walls | section 3 |
| Fitted 18/L, 90/L^2, K_1, run N8 | evidence only | Text 23.5 |

For the owner of `parts/upper-chain.md` and `library/convex-maximal-correlation.md`, to be applied by the lead: Lemma 20.2 can cite Lemma G and state 7 eps(D_1) <= 1 for the iteration. The library note's citations can point here, with Step 4 read as the uniform form of Lemma M. The obligation line "discharged: nest coercivity with the sharp weight" can cite Theorem N in place of its three scripts, with the bounds above in place of 18/L and 90/L^2.

Read: `FINISH.md`, `GOAL.md`, `gates/compute-inventory-39189b75b.md`, `parts/upper-chain.md` Text 20.2 and 23.3 to 23.6 and the obligations near its top, `library/convex-maximal-correlation.md`, `library/convex-laplace-tree-decay.md`, `library/fibre-propagator.md` to Theorem F-D, `checks/upper-chain_nest.py`, `checks/upper-chain_nest2.py`, the registrations of `checks/upper-chain_nest3.py`. No proof text was carried between the attempts. Not read: the attempts' part files. Literature was used from memory only for the shape of the classical arguments, and every step they supply is written above.
