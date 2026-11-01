lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T07:31Z

# Upper chain by hand: the Gruss bound, marginal convexity, the nest objection

Queue item 17, `hand-upper`, neutral. Statements pinned at commit 28e261c17. Work in progress; sections are written as they are finished.

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

- *Step 1.* Hess U >= 1 gives (mid) with c = 1 by the Taylor identity of Lemma M with u = v. Lemma P gives the Poincare inequality; no semigroup is used.
- *Step 2, with its regularity.* Let LL(K) be the bounded C^1 functions on K with bounded gradient, and G in LL(K_y). For x in a compact ball in K_x and fixed y_0, Hess_y S >= 1 gives S(x, y) >= -C - C |y - y_0| + |y - y_0|^2 / 2, and ||S_xy|| <= r gives |S_x(x, y)| <= C + r |y - y_0|. So derivatives in x pass under the integral, and d_e g(x) = -Cov_(y | x)(G, e . S_x), with no boundary term, since K_y does not move with x. e . S_x(x, .) is C^1 with gradient of norm at most r and lies in L^2, so Lemma P in its unbounded form bounds the covariance, and |grad g(x)| <= r ||grad G||_(L^2(. | x)). Hence g is in LL(K_x), and the printed inequality follows. The same holds with x, y exchanged.
- *Step 4.* S_xx^-1 <= 1 gives S_yy - S_yx S_xx^-1 S_xy >= 1 - r^2 at every point. Z(y) is finite, positive and continuous, by the domination of Step 2 with the roles exchanged. Lemma M with Sigma := 1 - r^2 is (mid) for V = -log Z with c = 1 - r^2, and Lemma P gives Var_(p_y)(h) <= (1 - r^2)^-1 E |grad h|^2 on LL(K_y). No derivative of V is taken.
- *Step 5.* LL(K_y) is T-invariant by Step 2, and it is dense in L^2(p_y), as it contains the restrictions of C_c^infinity. For G in LL(K_y) of mean zero, a_n := ||T^n G||_2^2 <= C r^(4 n). The spectral theorem can be replaced by one line: a_n^2 <= a_(n-1) a_(n+1) by Cauchy-Schwarz and self-adjointness, so a_(n+1) / a_n is non-decreasing, and it cannot exceed r^4 anywhere, or a_n would outgrow C r^(4 n). So ||T G||_2 <= r^2 ||G||_2.
- *Steps 3, 6.* Unchanged. They are Hilbert space algebra, and I checked them.

**The middle variable.** Let Hess S >= A on K_x x K_z x K_y, a product of open convex sets, A constant and positive definite, with either K_z bounded and S C^2 on its closure, or ||Hess S|| <= H_max. Then S-tilde(w) := -log integral dz exp(-S(w, z)), w := (x, y), is C^2. Domination as in Step 2 allows two derivatives under the integral, and with E_z the law exp(-S) dz normalized,

    d_i S-tilde = E_z[S_i],   d_i d_j S-tilde = E_z[S_ij] - Cov_z(S_i, S_j).

That is the identity the inventory asked for, and the formula printed for S-tilde_xy. Lemma M with z in the role of x and Sigma := Schur(A) gives Hess S-tilde >= Schur(A) by Corollary M', and this bound did not need the identity. As a by-product, Cov_z(e . S_w, e . S_w) <= E_z[e . S_ww e] - e . Schur(A) e, which is the Brascamp-Lieb statement in the only form used here. So the first main theorem applies to S-tilde with A_x, A_y the diagonal blocks of Schur(A).

**Still a citation.** The bound on the mixed block in the library uses the Helffer-Sjostrand representation Cov_z = E_z < grad_z S_x, L^-1 grad_z S_y > and the sign of the Bochner term on a box. Neither is rebuilt here, and no target text derives them. So the marginal inequality and r <= 1 for the first theorem are discharged, while the printed rate r <= C (H_max / kappa)^2 exp(-mu' D) keeps that one literature input. Label: gap, small, outside this item.
