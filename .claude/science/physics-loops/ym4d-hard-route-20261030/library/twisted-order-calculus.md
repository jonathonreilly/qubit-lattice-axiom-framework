# Leaf Scalar by an order calculus on the twisted algebra

Status: own derivation, each step written, not reviewed. Numerics: `checks/hard-core--mapped_order_calculus.py`, criteria written first; result recorded at the end of this note. Consumer: Theorem P1 of `parts/hard-core--mapped.md`, Text 3.7, so the Gaussian part of the coupling flow.

Credit for method: twisted convolution and its derivations are the standard calculus of the noncommutative torus (Connes, Rieffel), and the factorisation behind the gap is the textbook one for Landau levels. Everything used is proved here.

## The statement

Fix the level k. All operators live on the level-k lattice Z^4, at constant flux theta in the (1, 2) plane, charged sector. X := D^* D, the covariant Laplacian. E_theta := h_theta - K_{k,theta}, Y_theta := X^-1 D^* E_theta D X^-1, r_theta := 1 + Y_theta, and L(theta) := tau(log r_theta) = log det_c r_theta per site.

**Theorem LS.** There are C free of k and theta_k > 0 such that, for 0 < |theta| <= theta_k, L is twice differentiable with |L''(theta)| <= C, and |L(theta) - L(0)| <= (C/2) theta^2.

Theorem P1 reads the Taylor coefficient of Gamma_k at theta = 0 at fixed k (Lemma 3.4), so theta_k may depend on k, and this is what makes the proof short. The constant C must not, and it does not.

**Input (E), from Prop 3.11 and from analyticity at fixed k.** E_theta = Op_theta(e_theta) with e_theta = e_0 + theta e_1 + theta^2 e_2 + theta^3 rho_theta, matrix kernels in the bond indices.
- e_0, e_1, e_2 are free of theta, with sum_y |e_i(y)| (1 + |y|)^{N_0} <= C free of k, for a fixed N_0 (N_0 = 20 is more than enough).
- e_0 has vanishing moments below order 4 and e_1 below order 2. These are h_0,mu - |p^|^2 = O(p^4), which is Prop 3.11(a), and h_1 - S_1 = O(p^2), which is Prop 3.11(b) with S_1(p) = S_0 + O(p^2) from Lemma 3.10 at eta = 1. No moment condition on e_2.
- rho_theta and its first two theta-derivatives have weighted norm at most C_k, for |theta| <= theta_k, with no claim of uniformity in k. Reason: h_theta is a block of the inverse of the saddle matrix [[K, Q^o*], [Q^o, 0]], invertible since K is coercive on ker Q^o, so it is analytic in theta with exponentially local kernel at fixed k.
- On the whole torus, 1 + Y^_0(q) = sum_mu |s_mu|^2 h_0,mu / |p^|^4 >= c_0 > 0 free of k, since 1/h_0,mu = G_0,mu <= C/|p^|^2. And |E^_mu| <= C_E |p^|^4.

*Status of (E).* Prop 3.11 is written for C^2 bounds. The C^{N_0 + 5} bounds that give the kernel norms come from the same count: each derivative in q brings a factor s_j <= 1 in Lemma 3.9(c), the sum over positions is still geometric, and h_0,mu = Y_0^2 eps_eta / (1 + W_0 eps_eta) with all factors smooth. That extension is an implication, not displayed term by term. On the convention: Text 3.7 takes bond variables at midpoints. Going to start points multiplies by analytic phases and adds Poisson brackets of higher order, so the orders of e_0, e_1, e_2 are unchanged.

## 1. The algebra

W_y, y in Z^4, are the magnetic translations: W_y W_z = e^{i theta w(y, z)} W_{y + z}, w(y, z) := (y_1 z_2 - y_2 z_1)/2. T_mu := W_{e_mu}, so T_1 T_2 = e^{i theta} T_2 T_1, and D_mu = T_mu - 1. Op_theta(a) := sum_y a(y) W_y; a is the kernel. (a * b)(z) = sum_y a(y) b(z - y) e^{i theta w(y, z)}. tau(a) := a(0), a finite cyclic trace with tau(1) = 1, so |tau(a)| <= ||a||. eps^{12} = -eps^{21} = 1.

Two operations on kernels: (delta_mu a)(y) := y_mu a(y), and (da)(y) := d a_theta(y) / d theta, the derivative of the kernel at fixed y. Exactly, by differentiating the phase and using w(y, z) = w(y, z - y):

(A1) d(a_1 * ... * a_n) = sum_i a_1 ... (d a_i) ... a_n + (i/2) eps^{mu nu} sum_{i<j} a_1 ... (delta_mu a_i) ... (delta_nu a_j) ... a_n.

delta_mu is a derivation, and tau(delta_mu a) = 0. tau(da) = d tau(a). Hence tau((delta_mu a)(delta_nu b)) = -tau(a delta_mu delta_nu b), so

(A2) eps^{mu nu} tau((delta_mu a) * (delta_nu b)) = 0.

From a * a^-1 = 1:

(A3) delta_mu(a^-1) = -a^-1 (delta_mu a) a^-1,   d(a^-1) = -a^-1 (da) a^-1 + (i/2) eps^{mu nu} a^-1 (delta_mu a) a^-1 (delta_nu a) a^-1.

At theta != 0 the kernels below decay exponentially (the gap of Lemma 1 and Combes-Thomas), and the inverse is analytic in theta in a weighted l^1 algebra, so these operations are legal. The kernels of X and D are free of theta: dX = 0, dD = 0. So all the theta-dependence of Y_theta outside e_theta comes through (A1), (A3).

## 2. The gap

**Lemma 1.** X >= X_12 >= |theta|/2 for |theta| <= 2/3.

*Proof.* c_mu := T_mu + T_mu^*, s_mu := (T_mu - T_mu^*)/i, self-adjoint, with s_mu^2 = (2 - c_mu)(2 + c_mu) <= 4 (2 - c_mu). So X_12 = sum (2 - c_mu) >= (s_1^2 + s_2^2)/4. Expanding (s_1 +- i s_2)^*(s_1 +- i s_2) >= 0 gives s_1^2 + s_2^2 >= +- i [s_1, s_2]. From the commutation relation, by direct expansion, i [s_1, s_2] = tan(theta/2) {c_1, c_2}. With d_mu := 2 - c_mu: {c_1, c_2} = 8 - 4 d_1 - 4 d_2 + {d_1, d_2}. For a unit vector psi with <psi, X_12 psi> <= 1/3 in the spectral subspace X_12 <= 1/3: ||d_mu psi||^2 <= 4 <psi, d_mu psi>, so |<psi, {d_1, d_2} psi>| <= 8/3 and <psi, {c_1, c_2} psi> >= 8 - 4/3 - 8/3 = 4. So for theta > 0, <psi, X_12 psi> >= (1/4) tan(theta/2) 4 >= theta/2. Hence the bottom of X_12 is at least min(1/3, theta/2) = theta/2. For theta < 0 use the other sign. QED

Also tau(X^-1) <= W_4 := integral dq |q^|^-2 / (2 pi)^4, free of theta. Reason: tau(e^{-t X_theta}) = e^{-t X_0}(0, 0) E[e^{i theta A}] with A the area of the walk's bridge (Lemma 3.14), which is real and at most e^{-t X_0}(0, 0). Integrate over t.

## 3. Order classes

For an element B and an integer m, write B in O_m if for each real s, ||X^s B X^{-s - m/2}|| <= C_B(s) with C_B free of theta and k, for |theta| <= theta_k.

Closure. (i) O_m O_n in O_{m+n}, by inserting powers of X. (ii) O_m in O_{m'} for m' <= m, as ||X|| <= 16. (iii) B in O_m implies B^* in O_m, by taking adjoints: s becomes -s - m/2. (iv) For real s between two values, three lines applies to z -> X^z B X^{-z - m/2}, since X^{iy} is unitary and X has a bounded inverse at theta != 0. So it is enough to check s at the ends of a net. (v) theta in O_2, by Lemma 1: |theta| ||X^-1|| <= 2. theta^j in O_{2j}.

**Lemma 2.** ||X^s W_y X^{-s}|| <= C_s (1 + |y|)^{ceil|s|}. So if a has finite weighted norm, Op_theta(a) in O_0, with C(s) <= C_s sum |a(y)| (1 + |y|)^{ceil|s|}.

*Proof.* W_y^* T_nu W_y = e^{i phi_nu} T_nu, with |phi_nu| <= |theta| |y|. So X W_y = W_y (X + Delta_y), Delta_y := sum_nu [ (1 - e^{i phi_nu}) T_nu + h.c. ]. For an integer n >= 1, X^n W_y X^{-n} = X^{n-1} W_y X^{-n+1} + X^{n-1} W_y Delta_y X^{-n}, and W_y T_nu is a phase times W_{y + e_nu}. So a_n(y) := ||X^n W_y X^-n|| obeys a_n(y) <= a_{n-1}(y) + 8 |theta| |y| ||X^-1|| max a_{n-1}(y +- e_nu), and |theta| ||X^-1|| <= 2. Since a_0 = 1, a_n(y) <= C_n (1 + |y|)^n. Negative n by the adjoint, real s by (iv). QED

**Lemma 3.** D_mu, D_mu^*, delta_mu X in O_1, delta_mu delta_nu X in O_0, delta^a D_mu in O_0 for a >= 1.

*Proof.* T_mu, T_mu^* in O_0 by Lemma 2. delta_mu X = -(T_mu - T_mu^*) = -(D_mu - D_mu^*), and delta^2 X is a sum of T's. delta_mu D_mu = T_mu. So only D_mu in O_1. s = 0: ||D_mu psi||^2 <= <psi, X psi>; the same for D_mu^*, since T_mu commutes with its adjoint. For an integer n >= 1, X D_mu = D_mu X + T_mu Delta_{e_mu}, so

X^n D_mu X^{-n - 1/2} = X^{n-1} D_mu X^{-(n-1) - 1/2} + X^{n-1} T_mu Delta_{e_mu} X^{-n - 1/2}.

Here Delta_{e_mu} = (1 - cos phi) c_nu + sin phi s_nu, |phi| <= |theta|, with nu the other direction of the plane, and s_nu = (D_nu - D_nu^*)/i. The term with sin phi is at most |theta| C ||X^-1|| <= C by induction on n. The term with 1 - cos phi is at most theta^2 C ||X^{-3/2}|| <= C |theta|^{1/2}. So the bound holds for s = n, for s in [0, n] by (iv), for s <= -1/2 by the adjoint, and for s in (-1/2, 0) by (iv). QED

**Lemma 4 (words).** If a kernel f has vanishing moments below order m, 0 <= m <= 4, and finite weighted norm, then Op_theta(f) in O_m, with a bound by a weighted norm of f.

*Proof.* m = 0 is Lemma 2. Let m >= 1. Telescoping one coordinate at a time gives f = sum_mu d_mu a_mu, with (d_mu a)(y) := a(y - e_mu) - a(y), weighted norms losing finitely many powers, and a_mu with vanishing moments below order m - 1: in symbols, the quotient [f^(q_1, q') - f^(0, q')] / (e^{i q_1} - 1) is O(|q|^{m-1}) because the derivatives of f^ vanish to order m - j. Exactly,

Op(d_mu a) = D_mu Op(a) - T_mu Op(g),   g(z) := (1 - e^{-i phi(z)}) a(z),   phi(z) := theta w(e_mu, z),

and g = i theta w(e_mu, .) a + theta^2 b, |b(z)| <= w(e_mu, z)^2 |a(z)| / 2. Now w(e_mu, .) a is +- (1/2) delta_nu a, of order max(m - 2, 0). So D_mu Op(a) in O_m by Lemma 3 and induction. theta T_mu Op(delta_nu a) in O_{2 + max(m-2, 0)}, within O_m. theta^2 T_mu Op(b) in O_4, within O_m, as m <= 4. QED

*No gain from a commutator is used.* [D_1, D_2] is of the size of theta, which is of the same order as D_1 D_2 here. The calculus works because theta counts as order 2, and this is legal exactly because of the gap.

## 4. The orders of Y

By Lemma 4 and (v), for |theta| <= theta_k with theta_k small at fixed k (the remainder: |theta|^3 C_k ||X^-2|| <= 4 C_k |theta| <= 1, and similarly for its derivatives):

| | E | delta E | delta delta E | dE | d delta E | d d E |
|---|---|---|---|---|---|---|
| order | 4 | 3 | 2 | 2 | 1 | 0 |

For example dE = e_1 + 2 theta e_2 + O_k(theta^2), of order 2 from each of e_1 and theta e_2, and d d E = 2 e_2 + O_k(theta). With G := X^-1, in O_{-2}, (A3) and Lemma 3 give:

| | G | delta G | delta delta G | dG | d delta G | d d G |
|---|---|---|---|---|---|---|
| order | -2 | -3 | -4 | -4 | -5 | -6 |

**Lemma 5.** Y in O_2, delta Y in O_1, delta delta Y in O_0, dY in O_0, d delta Y in O_{-1}, d d Y in O_{-2}.

*Proof.* Y = sum G D_mu^* E_munu D_nu G. Apply (A1) and the Leibniz rule. In each resulting product, a factor that takes a d drops by 2, a factor that takes a delta drops by at most 1, and a d in (A1) is either a d on one factor or a delta on each of two, so it costs 2 in all. A factor takes at most two operations, as (A1) never puts both deltas of one pair on the same factor. So the total order is at least 2 - 2 i - j. QED

## 5. r is bounded below

**Lemma 6.** There is theta_1 free of k with r_theta >= c_0/2 for |theta| <= min(theta_1, theta_k).

*Proof.* Let P be the spectral projector of X on [0, lambda), and Q := 1 - P. By Y in O_2, ||X^{-1/2} Y X^{-1/2}|| <= C_Y, and ||X^{-1/2} Y|| <= 4 C_Y. So ||P Y P|| <= C_Y lambda, and |<P psi, Y Q psi>| <= 4 C_Y lambda^{1/2} ||P psi|| ||Q psi||.

On Q: let g be smooth with g(x) = 1/x for x >= lambda and g = 0 for x <= lambda/2. Then Q G = Q g(X). For smooth functions and |theta| small, g(X) - Op_theta(g o x^) and products of Op_theta minus Op_theta of the commutative product all tend to 0 in norm as theta -> 0, with a rate depending on lambda and on C^N norms only: |e^{i theta w} - 1| <= |theta| |w| in the twisted product, and polynomial approximation of g in C^N. So Q r Q = Q Op_theta(f) Q + o(1), f := 1 + g(x^)^2 sum |s_mu|^2 E^_0,mu. On x^ >= lambda, f = 1 + Y^_0 >= c_0. On x^ < lambda, |f - 1| <= C_E lambda. So f >= c_1 := min(c_0, 1 - C_E lambda), and f - c_1/2 is a square of a smooth real function, so Op_theta(f) >= c_1/2 - o(1) (sharp positivity is not needed). Take lambda small, then theta_1 small. QED

So R := r^-1 and S := (r + s)^-1, s >= 0, are bounded, ||S|| <= 2/(c_0 + 2 s) and more.

**R and S lie in O_0.** R = sum_{i < 2n} (-Y)^i + Y^n R Y^n, and Y^n in O_{2n} gives ||X^s Y^n|| <= C and ||Y^n X^{-s}|| <= C for n >= |s|. So ||X^s R X^{-s}|| <= C(s). With sigma := 1/(1 + s), S = sigma (1 + sigma Y)^-1, and the same expansion gives ||X^{s'} S X^{-s'}|| <= C(s') sigma.

## 6. The second derivative

From log r = integral_0^infty [ (1 + s)^-1 - S ] ds, (A3) and cyclicity:

L' = tau(R dr) - (i/2) eps^{ab} integral_0^infty tau(S (delta_a r) S (delta_b r) S) ds.

Then, by (A1), (A2), (A3):

L'' = tau(R d d r) - tau(R dr R dr) + (i/2) eps^{ab} tau(R (delta_a r) R (delta_b r) R dr) + T',

with T' the derivative of the integral, a finite sum over the terms of (A1) on five factors. Each term of T' has at least three factors S, so it converges in s, and its total order is at least 0. The list: dS with two factors delta r, order 2 or 4; d delta r with delta r, order 0; two deltas on two factors, of order 0, 2, or 4.

**Terms of order at least 0.** A product of total order m >= 0 is bounded in norm, by inserting powers of X and by ||X|| <= 16. Since tau(1) = 1, its trace is bounded.

**The one term of order -2.** B := X^{1/2} (d d r) X^{1/2} is bounded by Lemma 5, with s = 1/2. So

|tau(R d d r)| = |tau( (X^{-1/2} R) (X^{-1/2} B) )| <= ||R|| ||B|| tau(X^-1) <= C,

by Cauchy-Schwarz for tau and Lemma 1's bound on tau(X^-1). So |L''(theta)| <= C on 0 < |theta| <= theta_k, after decreasing theta_k to at most theta_1, 2/3. **No spectral cut enters L'', and no kernel of G.**

## 7. The linear term

L' is Lipschitz on (0, theta_k], so L'(0+) =: a_k exists, and L(theta) - L(0) = a_k theta + O(C theta^2). By Prop 3.6, L(theta) = C_k(theta) + bracket(theta) - Gamma_c(theta) up to a constant, where C_k and Gamma_c are analytic and even at fixed k, and bracket(theta) - bracket(0) = O_k(theta^2) by Prop 3.15. So L(theta) - L(0) = O_k(theta^2) and a_k = 0. Reflection covariance is not read here. QED

So Leaf Scalar holds, and Theorem P1's proof is unchanged after it: |B_k - k c_0| <= C(L), given (E).

## 8. What this retires

(HK), the covariant heat-kernel word bounds with Duhamel, the two-tier form Delta_1, Delta_2, the separate treatment of a fixed kernel in Step 1, and the plan of Text 3.9(b) with a spectral cut. `checks/hard-core--mapped_hk.py` stays as a record of the sizes (PASS) and is no longer consumed.

## 9. Hostile check

1. *An error in the older Step 1.* I had written ell_0' = c eps tau(R delta Y R delta Y) "summing the power series". The weights in the sum are (n - 2 g)/n, not constant, and the correct form is the integral in Section 6. It did not matter for the size. It is corrected here, and F in the check tests this form against a difference quotient.
2. *Is the order of d d r really reachable with no logarithm?* Density count: order -2, against the volume q^3 dq in d = 4. There is room of two powers. A logarithm would need order -4. In the control of the check, E of order 2 gives this.
3. *Does Lemma 2's constant blow up?* Each commutator has |theta| |y| and comes with ||X^-1|| <= 2/|theta|, so it is a power of |y|, with no factor of 1/theta.
4. *Lemma 1 at large k.* theta is in level-k units, the same as in Text 3. It uses only T_1 T_2 = e^{i theta} T_2 T_1. Nothing depends on k.
5. *The trace.* tau(X^-1) is W_4, about 0.155. A massless X in d = 4 has finite tau(X^-1) and logarithmic tau(X^-2). No factor X^-1 beyond the first appears in the trace estimate, since all others are absorbed in operator norm.
6. *The range of s.* A product in d d r has at most nine factors of G and delta X with one E. So |s| <= 3 for all of them, with s_0 = 1/2, and N_0 covers it. R and S need n = 3 in Section 5.
7. *What is not proved.* (E) beyond the C^2 of Prop 3.11, as stated. Lemma 3.2's standing note and Lemma 3.10's bookkeeping remain as Text 3.8 says. Prop 3.6 at f != 0 is read as an identity between absolute values, also as there.
8. *Is theta_k small a cheat?* No. Theorem P1 reads a Taylor coefficient at fixed k, through Lemma 3.4. A bound of L at fixed flux uniformly in k would be a stronger statement, not asked by Theorem P1. At finite theta, one would need (E) uniformly in k at all orders, or a bound on rho_theta free of k, which I have not derived.

## Numerics

`checks/hard-core--mapped_order_calculus.py`, criteria written first, N x N Bloch representation at theta = 2 pi / N, N = 61, 127, 251, 509, with a model E of the stated orders and arbitrary coefficients, integrated over p_3, p_4. PASS, run once.

- A, gap: the bottom of X_12 over theta is 0.954, 0.975, 0.987, 0.994, 0.997, 0.9985 at N = 17, ..., 509, so the true constant is near 1, against the 1/2 proved.
- B, orders: over s in [-5/2, 5/2], at rho = 0, the largest norm at N = 61 and N = 509: T_1 4.26, 1.84; D_1 12.2, 11.2; delta_1 X 21.3, 21.9; E_11 35.6, 39.3; delta_1 E_11 27.9, 33.2; delta delta E_11 71.8, 78.1; dE_11 10.8, 11.7; Y 127, 145; dY 66.1, 77.5. All within the factor 1.5 stated, and with theta falling by 8.3. So the classes are bounded, though the constants at |s| = 5/2 are not small.
- F, the derivative formula: agreement with a five-point difference, to 2e-5 at theta = 0.075, rho = 0.05, and to 4e-8 at theta = 0.125, rho = 0.5. The integral term is needed: it is 1e-4 of L', larger than the agreement.
- C, Leaf Scalar: Q(N) := (L(theta) - L(0))/theta^2 = 0.05509, 0.05568, 0.05589, 0.05597, with differences 0.00059, 0.00021, 0.00008, so it converges, with no logarithm.
- D, control, E of order 2: Q = 0.00334, 0.00408, 0.00477, 0.00549, with differences 0.00074, 0.00069, 0.00072, a constant per doubling. So this is theta^2 log(1/theta), as the order count says, and the test has power.
- K: the Bloch dependence is at most 2e-15.

Limits: a model E, as the true one is known through its orders only, and this is what the proof reads. The check does not test Prop 3.11.
