lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T08:08Z

# Witness steps by hand (queue row 18, `hand-witness`)

Author: anthropic/claude-opus-5-5/max mac-mini-worker, 2026-11-01. Pinned at `f3aa2a8c5` on `claude/ym4d-hard-route`. Neutral: it reads `parts/witness.md`, the NT2 and free-value library notes, and clause statements of `parts/upper-chain.md`, and it uses no proof text of either hard-core attempt.

Same-model author work, not a review or an audit. No status. Every step below is written to be checked by hand. The runs in `checks/hand_witness/` are kill tests, with criteria written first; no step rests on them.

## State of attack

| Queue task | Result | Label |
|---|---|---|
| Lemma 3.6 without the symbolic run | Proved in section 1, plus the Ward identity (V5) and (3.4), which Theorem 3.8 reads | discharged |
| Stieltjes and density inputs of Lemma RM' | Theorem S, Lemma D and Theorem RM' in section 2, at the stated scope (D1) to (D3). Corrections: Lemma RM's form needs a contact term c_0 >= 0, and (D3) cannot be dropped | discharged at that scope |
| (H21) applied to the order of b and L in NT1-F | Order A in section 3.2, with an explicit L_1. Stronger: Lemma CL and order B in section 3.3 keep the printed order b, L, X with b free of L | implication, as NT1-F is |

Still open: tensor multipliers in RM', the one-link sentence of RM', C_s free of L, the new request that c_E be free of L, and every producer clause of NT1-F. Nothing here is a fact about Wilson.

## 1. Lemma 3.6 without the symbolic run

Statement, `parts/witness.md:438-440`. For E_i = a^i exp(i k^i . x), with real k^1 + k^2 + k^3 = 0 and a^i_mu = atil^i_mu exp(i k^i_mu / 2), the sum of V_p over the plaquettes at one site is

    -2i [ (atil^1, D_3 atil^2) (Y_12 . atil^3) + (atil^2, D_1 atil^3) (Y_23 . atil^1) + (atil^3, D_2 atil^1) (Y_31 . atil^2) ],

with (a, b) the bilinear pairing, D_l := diag(cos(k^l_mu / 2)), Y_ij := (2 sin((k^i_nu - k^j_nu) / 2))_nu.

**Step 1, one plaquette [discharged].** For a plaquette with links b_1, ..., b_4 in path order and signs eps_s, let e^s in C^3 have entries e^s_k := eps_s E_k(b_s), k = 1, 2, 3. Then P_k(p) is the k-th entry of e^1 + e^2 + e^3 + e^4, and V_p of Text 2.1 is the sum over s < t of det(P, e^s, e^t), with P, e^s, e^t as columns. Expand P. A term with u in {s, t} has a repeated column and vanishes. For a < b < c the three surviving terms are det(e^a, e^b, e^c), det(e^b, e^a, e^c) = -det(e^a, e^b, e^c) and det(e^c, e^a, e^b) = det(e^a, e^b, e^c). So

    V_p = sum_(a<b<c) det(e^a, e^b, e^c).                                        (V1)

A cyclic shift of the links, and the reversal e^s -> -e^(5-s), each permute the four terms of (V1) with no change of value, so V_p depends only on the unoriented plaquette.

**Step 2, one plane [discharged].** Fix mu != nu, the plaquette with corner at 0 and path 0, e_mu, e_mu + e_nu, e_nu, 0. A translate by x multiplies V_p by exp(i (k^1 + k^2 + k^3) . x) = 1, by trilinearity. For i = 1, 2, 3 put

    A_i := atil^i_mu,  B_i := atil^i_nu,  x_i := exp(i k^i_mu / 2),  y_i := exp(i k^i_nu / 2),

so x_1 x_2 x_3 = y_1 y_2 y_3 = 1. The entries of the increments are

    e^1_i = A_i x_i,   e^2_i = B_i y_i x_i^2,   e^3_i = -A_i x_i y_i^2,   e^4_i = -B_i y_i.

A determinant is the sum over bijections of columns to rows, and the sign of (i, j, l) is + on a cyclic order of (1, 2, 3). Let (i, j, l) be such an order. The terms det(e^1, e^3, e^4) and det(e^1, e^2, e^3) contain A A B, and det(e^1, e^2, e^4) and det(e^2, e^3, e^4) contain A B B.

Coefficient of A_i A_j B_l. In det(e^1, e^3, e^4) the B sits in the third column: rows (i, j, l) give + x_i (-x_j y_j^2)(-y_l), and rows (j, i, l) give - x_j (-x_i y_i^2)(-y_l). In det(e^1, e^2, e^3) the B sits in the middle column: rows (i, l, j) give - x_i (y_l x_l^2)(-x_j y_j^2), and rows (j, l, i) give + x_j (y_l x_l^2)(-x_i y_i^2). The total is x_i x_j (1 + x_l^2) y_l (y_j^2 - y_i^2). Since x_i x_j = 1 / x_l and y_l = 1 / (y_i y_j),

    x_i x_j (1 + x_l^2) = 2 cos(k^l_mu / 2),
    y_l (y_j^2 - y_i^2) = y_j / y_i - y_i / y_j = -2i sin((k^i_nu - k^j_nu) / 2).

Coefficient of B_i B_j A_l. In det(e^1, e^2, e^4) the A sits in the first column: rows (l, i, j) give + x_l (y_i x_i^2)(-y_j), and rows (l, j, i) give - x_l (y_j x_j^2)(-y_i). In det(e^2, e^3, e^4) the A sits in the middle column: rows (i, l, j) give - (y_i x_i^2)(-x_l y_l^2)(-y_j), and rows (j, l, i) give + (y_j x_j^2)(-x_l y_l^2)(-y_i). The total is y_i y_j (1 + y_l^2) x_l (x_j^2 - x_i^2) = 2 cos(k^l_nu / 2) (-2i) sin((k^i_mu - k^j_mu) / 2), the first coefficient with mu and nu exchanged.

Each polarisation of each field occurs once in each term, so these are all the monomials, and with the sum over cyclic orders,

    V_(mu nu) = -2i sum_cyc [ atil^i_mu atil^j_mu cos(k^l_mu / 2) Y_(ij,nu) atil^l_nu
                            + atil^i_nu atil^j_nu cos(k^l_nu / 2) Y_(ij,mu) atil^l_mu ].    (V2)

**Step 3, the sum over planes [discharged].** Summing (V2) over mu < nu gives every ordered pair mu != nu once. Expanding the product (atil^i, D_l atil^j)(Y_ij . atil^l) over all mu, nu gives those terms plus, for each mu, the same-index term. Summed over the cyclic orders, the same-index terms at mu are atil^1_mu atil^2_mu atil^3_mu times sum_cyc cos(k^l_mu / 2) 2 sin((k^i_mu - k^j_mu) / 2). Put a, b, c for the half angles of the three k_mu, so a + b + c = 0. Then

    2 cos(c) sin(a - b) = sin(a - b + c) + sin(a - b - c) = sin(2a) - sin(2b),

and the cyclic sum telescopes to zero. This is the printed form, with the constant -2i. []

**Representatives.** The half angles need k^1 + k^2 + k^3 = 0 exactly, not modulo 2 pi: x_1 x_2 x_3 = 1 fails otherwise. (3.4) uses k^3 := -k^1 - k^2, so this is what it reads.

### 1.1 What (3.4) reads from it

Write form(a^1, a^2, a^3) for the bracket of Lemma 3.6, khat_i := 2 sin(k^i / 2), khat_i^2 := (khat_i, khat_i). `parts/witness.md:452-458` states (3.4) as derived algebra with a numerical check, so here is the algebra.

**Trigonometry [discharged].** Coordinate by coordinate, from the addition formulas and k^1 + k^2 + k^3 = 0,

    khat_1 = -(D_3 khat_2 + D_2 khat_3),   Y_23 = D_3 khat_2 - D_2 khat_3,   and cyclically,        (V3)
    Y_12 . khat_3 = khat_2^2 - khat_1^2.                                                            (V4)

For (V4), with half angles a, b, c: 4 sin(a - b) sin(c) = 2 cos(a - b - c) - 2 cos(a - b + c) = 2 cos(2a) - 2 cos(2b) = 4 sin^2(b) - 4 sin^2(a). From (V3), Y_23 = -khat_1 - 2 D_2 khat_3 and Y_31 = khat_2 + 2 D_1 khat_3.

**Ward identity [discharged].** With j_i := khat_i^2 a^i - khat_i (khat_i, a^i),

    form(a^1, a^2, khat_3) = (j_2, D_3 a^1) - (j_1, D_3 a^2),   form(khat_1, khat_2, khat_3) = 0.    (V5)

Proof. Insert khat_3 and use (V4) and the two lines above. The two products with a factor 2 cancel, leaving

    (a^1, D_3 a^2)(khat_2^2 - khat_1^2) - (a^2, D_1 khat_3)(khat_1, a^1) + (a^1, D_2 khat_3)(khat_2, a^2).

Replace D_1 khat_3 = -khat_2 - D_3 khat_1 and D_2 khat_3 = -khat_1 - D_3 khat_2. The terms (a^2, khat_2)(khat_1, a^1) cancel, and what remains is the right side of (V5). For the second claim, j_i = 0 when a^i = khat_i. []

**(3.4) [discharged, given the symbol of Lemma 3.7].** The field of a source v_i tensor e_a has symbol a^(i)_(a f) = delta_(a f) u_i + h_i^(a f) khat_i, with u_i = v_i / khat_i^2, (khat_i, v_i) = 0. Contract eps_abc eps_fgh over the trilinear form. Three u: 6 form(u_1, u_2, u_3). One h, in the third slot: eps_abc eps_abh = 2 delta_ch gives 2 t_3 form(u_1, u_2, khat_3), and by (V5) with j_i = v_i this is 2 t_3 (v_1, D_3 v_2)(1 / khat_1^2 - 1 / khat_2^2). Two h, in slots 2 and 3: eps_abc eps_agh = delta_bg delta_ch - delta_bh delta_cg gives a(h_2, h_3) form(u_1, khat_2, khat_3), and (V5) with j_2 = 0, j_1 = v_1 gives form(u_1, khat_2, khat_3) = -(v_1, D_3 khat_2) = -lam_1. Three h: zero by (V5). The form is cyclic by construction, so the other slots are the cyclic images. This is (3.4). With the factor 12 of (3.3) and -2i of Lemma 3.6, -24 i form = -4 i (6 form), which matches the prefactor printed under (3.4). []

So the algebra under Theorem 3.8 no longer rests on a run: Lemma 3.6, (V5) and (3.4) are written. Lemma 3.7 was already an argument, and it is not rechecked here.

## 2. Lemma RM': the Stieltjes and density inputs

`library/nt2-chart-free-vertex.md:66-72` says "completely monotone", then "Laplace transforms are dense enough". This section writes both, with the contact term and the boundedness they rest on. The idea that shortens it: boundedness in k_4 extends reflection positivity from test functions to all of L^2(0, infinity), so exponentials are admissible tests, and no distribution theory is needed.

**Setting.** On R^4 take a real current J in C_c^infinity(R^4; R^4), div J = 0, and Jhat(k) := int exp(-i k . x) J(x) dx. The covariance on conserved currents is

    Q(J, J') := int dk / (2 pi)^4  conj(Jhat(k)) . Jhat'(k) D(k).

For a chosen axis write k = (k_4, p), p in R^3, t = x_4. Reflection acts as on a loop current: (Theta J)_4(t, x) = -J_4(-t, x), and (Theta J)_s(t, x) = J_s(-t, x) on the other three components.

- (D1) D: R^4 -> [0, infinity) is measurable and even in each k_i. (Invariance under signed permutations gives this. Permutations are not used, since (RP) is assumed on each axis.)
- (D2) int D(k) (1 + |k|)^(-N) dk < infinity for some N.
- (D3) For each axis and a.e. value of the other three components, M(p) := ess sup over k_i of D is finite.
- (RP) For each axis, Q(Theta J, J) >= 0 for every such J supported in x_i > 0.

**Theorem RM' (precise form) [discharged].** Assume (D1) to (D3) and (RP), and fix an axis. For a.e. p, with m := |p| > 0, there are c_0(p) >= 0 and a positive Borel measure mu_p on [m, infinity), with int dmu_p(w) / (v + w) <= M(p) / 2 for every v > 0, such that

    D(k_4, p) = c_0(p) + int dmu_p(w) 2 w / (w^2 + k_4^2)   for a.e. k_4.          (R1)

With nu_p the image of 2 w dmu_p(w) under s = w^2, this is the printed D(z; p) = c_0 + int dnu_p(s) / (z + s), with supp nu_p in [|p|^2, infinity). Consequently:

- (a) rho(k) := |k|^2 D(k) agrees for a.e. k_4 with a non-decreasing function of k_4^2.
- (b) For each lambda >= 1, rho(lambda k) >= rho(k) for a.e. k.
- (c) r -> Var <j_r, a> = int dm(q) rho(q / r) is non-increasing, with values in [0, infinity], for dm absolutely continuous as in Lemma RM.

**Step 1, from RP to one fixed p [discharged].** For real f in C_c^infinity((0, infinity)) put fhat(k) := int exp(-i k t) f(t) dt, and

    T_f(p) := int dk / (2 pi) D(k, p) fhat(k)^2,
    L_f(p) := int dk / (2 pi) D(k, p) (k^2 + |p|^2) fhat(k)^2.

Both are real and even in p by (D1). fhat is Schwartz, and for |p| <= R one has 1 + |k| <= (1 + R)(1 + |k_4|), so by (D2) and Fubini both are in L^1_loc(R^3), with integral over |p| <= R at most a power of R.

*Transverse test.* Let chi be real in C_c^infinity(R^3), e a unit vector, xi := curl(e chi), J := (0, f(t) xi(x)). Then div J = 0, and Jhat(k) = fhat(k_4) xihat(p) on the spatial components, conj((Theta J)^(k)) = fhat(k_4) conj(xihat(p)), since f is real. So

    Q(Theta J, J) = int dp / (2 pi)^3 |p x e|^2 |chihat(p)|^2 T_f(p) >= 0.                  (R2)

*Gauss-law test.* Let g := phi(t) grad chi(x), phi real in C_c^infinity((0, infinity)), and J_4 := -div g = -phi Laplacian(chi), J_s := d_t g = phi' grad chi. Then div J = 0 and J is supported in t > 0. The transforms are Jhat_4 = phihat(k_4) |p|^2 chihat(p) and Jhat_s = -k_4 phihat(k_4) p chihat(p). The conjugated reflected current has components -|p|^2 phihat(k_4) conj(chihat(p)) and k_4 phihat(k_4) p conj(chihat(p)). Their product with Jhat is -|p|^2 (k_4^2 + |p|^2) phihat(k_4)^2 |chihat(p)|^2, so

    Q(Theta J, J) = - int dp / (2 pi)^3 |p|^2 |chihat(p)|^2 L_phi(p) >= 0.                  (R3)

(R3) is the printed reflected form at ghat parallel to p: for one Proca mode it reads |p|^2 (w^2 - |p|^2) phi~(w)^2 / (2 w) >= 0, and it vanishes for Maxwell, which is Gauss's law.

*Localising in p.* (R2) and (R3) extend to complex chi = chi_1 + i chi_2: the cross term of |chihat|^2 is odd in p, and the rest of each integrand is even, so the integral is the sum of the two real ones. Take chi(x) := exp(i p_0 . x) eta(eps x) with eta real, non-zero, in C_c^infinity(R^3). Then |chihat(p)|^2 = eps^(-6) |etahat((p - p_0) / eps)|^2, a positive multiple of an approximate identity G_eps(p - p_0) with G Schwartz. At a Lebesgue point p_0 of a locally integrable function T whose averages grow at most polynomially, int T G_eps(p - p_0) dp -> T(p_0): near p_0 by the Lebesgue differentiation theorem, and far from p_0 by the decay of G. So for each fixed f, T_f(p) >= 0 for a.e. p (take e = e_1; the weight |p x e|^2 vanishes only on a line) and L_f(p) <= 0 for a.e. p.

Fix once and for all psi_1 in C_c^infinity((0, 1)), psi_1 >= 0, psi_1 != 0. Let S_a be the shift of Step 2, F a countable subset of real C_c^infinity((0, infinity)) dense in L^2(0, infinity), and P the countable family of finite sums sum_j c_j S_j psi_1, c_j rational, j in N. Call p **good** if p != 0, M(p) < infinity, D(., p) is even, T_f(p) >= 0 for f in F, and L_f(p) <= 0 for f in P. A.e. p is good.

**Step 2, the Stieltjes input.**

**Theorem S [discharged].** Let D in L^infinity(R) be even with D >= 0, M := ||D||_infinity, and suppose int D(k) fhat(k)^2 dk >= 0 for f in a dense subset of real L^2(0, infinity). Then there are c_0 >= 0 and a positive Borel measure mu on (0, infinity), with int dmu(w) / (v + w) <= M / 2 for v > 0, such that

    D(k) = c_0 + int dmu(w) 2 w / (w^2 + k^2)   for a.e. k,                                 (R4)
    int dk / (2 pi) D(k) fhat(k) ghat(k) = int f~(w) g~(w) dmu(w)   for f, g in L^1 and L^2 of (0, infinity),   (R5)

with f~(w) := int exp(-w t) f(t) dt. c_0 is invisible in (R5).

Proof. *S0, the form.* On H, the real L^2(0, infinity), put B(f, g) := int dk / (2 pi) D fhat ghat. By Plancherel |B(f, g)| <= M ||f|| ||g||; B is real by evenness of D, symmetric, and positive on H by density. Let (S_a f)(t) := f(t - a) 1(t > a), a >= 0. Then (S_a f)^ = exp(-i k a) fhat, ||S_a f|| = ||f||, S_a S_b = S_(a+b), and B(S_a f, g) = B(f, S_a g). Put q(b) := B(S_b f, S_b f) = B(S_(2b) f, f). Cauchy-Schwarz for B gives q(b) <= q(2b)^(1/2) q(0)^(1/2), and q <= M ||f||^2 always. Iterating from b = a,

    q(a) <= q(0)^(1 - 2^-n) (M ||f||^2)^(2^-n),   so q(a) <= q(0),

and B(S_a f, f) = q(a / 2) >= 0. This is the only place where the bound on D is used against the shifts, and it is what fails for a polynomial D.

*S1, a moment measure.* Let A := S_h, h > 0. For every f in H: B(A f, f) >= 0; B((1 - A) f, f) >= 0, since B(A f, f) <= B(A f, A f)^(1/2) B(f, f)^(1/2) <= B(f, f); and B(A (1 - A) f, f) >= 0, since x (1 - x) = x (1 - x)^2 + (1 - x) x^2 gives B(A g, g) + B((1 - A) g', g') with g := (1 - A) f, g' := A f. Fix psi in H, and let Lam(P) := B(P(A) psi, psi) for real polynomials P. Write j = 2 j' + e, l = 2 l' + e' with e, e' in {0, 1}, and g := A^(j') (1 - A)^(l') psi. Symmetry of A gives Lam(x^j (1 - x)^l) = B(A^e (1 - A)^(e') g, g) >= 0.

So Lam(Bern_N P) >= 0 for P >= 0 on [0, 1], with Bern_N P(x) := sum_k P(k / N) binom(N, k) x^k (1 - x)^(N - k). If P has degree d, then Bern_N P has degree at most d and its coefficients tend to those of P: differentiating (x + y)^N gives sum_k k (k - 1) ... (k - r + 1) binom(N, k) x^k (1 - x)^(N - k) = N (N - 1) ... (N - r + 1) x^r, and k^d is a combination of these falling factorials with top coefficient 1. Hence Lam(P) >= 0, so |Lam(P)| <= Lam(1) sup |P| on [0, 1]. By Weierstrass and the Riesz representation theorem there is a finite positive Borel measure mu_h on [0, 1], unique by Weierstrass, with B(S_(j h) psi, psi) = int x^j dmu_h(x), j >= 0.

*S2, all shifts.* The map x -> x^(2^n) carries mu_(2^-n) to a measure with the moments of mu_1, so to mu_1. Hence for dyadic a, B(S_a psi, psi) = int y^a dmu_1(y). Both sides are continuous in a > 0, so this holds for real a > 0. As a -> 0 the left side tends to B(psi, psi) = mu_1([0, 1]) and the right to mu_1((0, 1]), so mu_1({0}) = 0. As a -> infinity the left side tends to 0 by Riemann-Lebesgue, since D psihat^2 is integrable, and the right to mu_1({1}), so mu_1({1}) = 0. With w = -log y and m_psi the image of mu_1 on (0, infinity),

    B(S_a psi, psi) = int exp(-w a) dm_psi(w),   a >= 0,  mass of m_psi = B(psi, psi).     (R6)

A finite measure on (0, infinity) is determined by these values at a in N, by Weierstrass in y.

*S3, one measure.* Let f be in L^1 and L^2 of (0, infinity), real. Then f * psi is in H, with transform fhat psihat. Writing fhat^2 as a double integral of exponentials and using Fubini and (R6), B(S_a (f * psi), f * psi) = int exp(-w a) f~(w)^2 dm_psi(w). By uniqueness, m_(f * psi) = f~^2 m_psi. Let psi_0 >= 0 be non-zero in the same class, so psi_0~ > 0. Commutativity of the convolution gives f~^2 m_(psi_0) = psi_0~^2 m_f. So mu := psi_0~^(-2) m_(psi_0) is a positive Borel measure on (0, infinity) with m_f = f~^2 mu for every f in the class, and it does not depend on psi_0. Polarising the mass identity gives (R5) for real f, g, and its complex-bilinear extension gives it for complex f, g.

*S4, exponentials.* For Re z > 0 the function exp(-z t) is admissible, with transforms 1 / (z + i k) and 1 / (z + w). Put

    E(z) := int dk / (2 pi) D(k) z / (z^2 + k^2),   Re z > 0.

(R5) reads int dk / (2 pi) D / ((z + i k)(z' + i k)) = int dmu(w) / ((z + w)(z' + w)). Apply the partial fraction 1 / ((a + c)(b + c)) = (1 / (b - a)) (1 / (a + c) - 1 / (b + c)) on both sides. On the left, symmetrise in k, using that D is even: the odd parts of the two simple fractions cancel and the integral converges absolutely. This gives

    E(z) - E(z') = int dmu(w) [ 1 / (z + w) - 1 / (z' + w) ].                                (R7)

For real v < v' the right side is positive, so E decreases on (0, infinity). Also 0 <= E(v) <= M / 2, since D >= 0 and int dk / (2 pi) v / (v^2 + k^2) = 1 / 2. So c_0 := 2 lim_(v -> infinity) E(v) exists in [0, M]. Letting z' = v' -> infinity in (R7), first at real z by monotone convergence, gives int dmu(w) / (v + w) = E(v) - c_0 / 2 <= M / 2. Then dominated convergence gives, for all Re z > 0,

    E(z) = c_0 / 2 + int dmu(w) / (z + w).                                                   (R8)

*S5, the boundary value.* Let P_v(y) := v / (pi (v^2 + y^2)). Since 2 z / (z^2 + k^2) = 1 / (z + i k) + 1 / (z - i k), the real part at z = v + i x, with D even, is 2 Re E(v + i x) = (P_v * D)(x). So (R8) gives

    (P_v * D)(x) = c_0 + int dmu(w) 2 (v + w) / ((v + w)^2 + x^2).                           (R9)

As v -> 0 the left side tends to D(x) at every Lebesgue point. For x != 0 and v <= 1 the integrand is at most C_x / (1 + w), which is mu-integrable, so the right side tends to c_0 + int dmu(w) 2 w / (w^2 + x^2). This is (R4). []

**Step 3, the density input.**

**Lemma D (localising the spectral variable) [discharged].** In Theorem S let m >= 0, and suppose L_phi := int dk / (2 pi) D(k) (k^2 + m^2) phihat(k)^2 <= 0 for phi in the family P of Step 1. Then mu((0, m)) = 0.

Proof. For phi in C_c^infinity((0, infinity)), (phi')^ = i k phihat and (phi')~(w) = w phi~(w). By (R5), with the term m^2 B(phi, phi),

    -L_phi = int (w^2 - m^2) phi~(w)^2 dmu(w).                                               (R10)

c_0 does not enter. Let phi := sum_j c_j S_j psi_1 in P, so phi~(w) = psi_1~(w) Q(exp(-w)), with Q(y) := sum_j c_j y^j, any polynomial with rational coefficients. Let lam be the image under y = exp(-w) of (w^2 - m^2) psi_1~(w)^2 dmu(w). It is a finite signed measure on [0, 1], with total variation at most B(psi_1', psi_1') + m^2 B(psi_1, psi_1), by (R5). (R10) gives int Q^2 dlam >= 0. Rational polynomials are dense in C[0, 1], so int h^2 dlam >= 0 for every continuous h, and every non-negative continuous function is such an h^2. So lam >= 0. Since psi_1~ > 0, the density w^2 - m^2 is strictly negative on (0, m), so mu vanishes on every compact subset of (0, m). []

**Step 4, conclusion.** At a good p, apply Theorem S to D(., p), with the dense set F, and Lemma D with m = |p|. This is (R1). For (a), put rho_p(z) := c_0 (z + m^2) + int dmu_p(w) 2 w (z + m^2) / (z + w^2), z > 0. The integral converges, and each (z + m^2) / (z + w^2) = 1 - (w^2 - m^2) / (z + w^2) is non-decreasing in z because w >= m. So rho(k_4, p) = rho_p(k_4^2) for a.e. k_4.

For (b), fix lambda > 1, and let Lam_i multiply the i-th coordinate by lambda. On a good line, for a.e. k_i, rho(Lam_i k) = rho_p(lambda^2 k_i^2) >= rho_p(k_i^2) = rho(k), the exceptional set being a null set and its dilate. By Fubini this holds for a.e. k in R^4. The Lam_i are invertible linear maps, so they preserve null sets, and the four inequalities chain to rho(lambda k) >= rho(k) for a.e. k. For (c), with r_1 < r_2 and lambda = r_2 / r_1, apply (b) at k = q / r_2 under dm, which is absolutely continuous; the integrands are non-negative, so infinite values cause no trouble. []

**Remarks.**

1. **(D3) cannot be dropped.** D(k) = (|k|^2 - 1)^2 satisfies (D1), (D2) and (RP): a polynomial D is a differential operator, so Q(Theta J, J) = 0 for disjoint supports. It fails (D3), and rho = |k|^2 (|k|^2 - 1)^2 vanishes at |k| = 1, so it is not monotone. RP does not see polynomial contact terms, and boundedness is what removes all of them but the constant.
2. **Lemma RM needs a contact term.** Its form D(k^2) = int dnu(s) / (k^2 + s) has no constant, and RP cannot exclude one, since white noise has no reflected kernel. With rho(z) = c_0 z + int dnu(s) z / (z + s), Lemma RM and Corollary RM stand. In the O(4) case the form follows. **Corollary KL [discharged]:** if D(k) = d(|k|^2) under the hypotheses above, then d(y) = c_0 + int dnu(s) / (y + s) for a.e. y > 0, with c_0 >= 0, nu >= 0 on [0, infinity). Proof: at a good p, shifting s by m^2 in (R1) writes d, a.e. on y > m^2, as a function R_m analytic on the plane cut along (-infinity, 0]. Two such functions agree a.e. on an interval, so they coincide. Take good radii m_n -> 0. []
3. **Not covered, and still open.** Tensor multipliers on the transverse space. The closing sentence of RM' on one-link local maps and Schur powers is not touched here, so it stays unchecked.
4. **Imported, not rebuilt:** Plancherel, Riemann-Lebesgue, Fubini, monotone and dominated convergence, Lebesgue differentiation, Weierstrass approximation, the Riesz representation of positive functionals on C[0, 1]. These are textbook analysis. Everything else above is proved here, including the moment step that Bernstein's or Widder's theorem would give.

## 3. The order of b and L in Corollary NT1-F

`library/nt2-flat-fibre-criterion.md:78` picks b before L from tau_b = C_(n,r) b^(-r), and `:82` lets C_(n,r) grow with log L, so the printed order does not fix the constant that chooses b. Section 3.2 applies (H21) of `library/nt2-free-value-by-hand.md`. Section 3.3 goes further: at fixed L the clip error is a Gaussian moment as g_j -> 0, so it has an L-free limit, and the printed order b, L, X can stand as printed. All of this is implication: nothing here supplies a clause for Wilson.

### 3.1 The constant of (F-3) [discharged]

The printed line gives no derivation. Let X := X_p, X' := X_q >= 0, Y := min(X, b), Z := X - Y, likewise Y', Z', and m_s := max(E_1 X^s, E_1 X'^s). For r >= 1, 0 <= Z <= X^(1 + r) b^(-r) and Y <= X. Then

    Cov_1(X, X') - Cov_1(Y, Y') = Cov_1(Z, X') + Cov_1(Y, Z').                                 (O1)

For non-negative U, V, |Cov(U, V)| <= max(E[U V], E[U] E[V]). Hölder bounds each of these by b^(-r) m_(2 + r), so

    | Cov_1(Y, Y') - Cov_1(X, X') | <= 2 m_(2 + r) b^(-r).                                     (O2)

X_p <= tau_n^2 by the definition of tau_n, t_n(c; 1) = 0 by (LE_j), since Ebar(c'; 1) = 0, and (GS_j)(c) gives m_s <= C_(n, 2 s). So the C_(n,r) of (F-3) is 2 C_(n, 4 + 2 r), with C_(n,s) the constant of (GS_j)(c). The convention "free of L up to powers of log L" is printed for C_n, and (F-3) reads it for C_(n,s).

### 3.2 The order with (H21) [implication]

Inputs, in the form NT1-F reads them. Fix r >= 1. The window is N_D of (H20). All constants below are chosen before L and do not depend on b.

- (E1) 2 C_(N_D, 4 + 2 r)(L) <= A (1 + log L)^alpha.
- (E2) C_(N_D)(L) <= A' (1 + log L)^(alpha'), for the C_n of (GS_j)(a) and (LE_j).
- (E3) C_s free of L [unchecked item of the Obligations], kappa := kappa_lift > 0.
- (E4) A number M_*, free of L, such that at each fixed L, Mbar_1 <= M_* for g_j small. The note's line "bounded independently of L" unpacks as follows. Lemma 10.6 at level j + 1 and Jensen give ||X~_p||_(L^1) <= C_4 / t_1, absolute. The rest is at most ||X_p||_(L^2) P(f_p > eps_1)^(1/2) <= 2^(1/2) t_0^-1 exp(C_4(L) - t_0 x_(j+1) eps_1^2 / 4), which tends to 0 at fixed L. So M_* := (1 + C_4 / t_1) sum_h exp(-c_E h) N_h works, **provided c_E is free of L**, which Text 14 does not say; that is a new one-line request to the consumer.

**Corollary NT1-F, order A.** Assume what the corollary assumes, H-NET, the fixed-scale part of H-SCALE, the clauses of Theorem F, (FT) at the two pairs, and supports within w cells with w free of L, and also (E1) to (E4). Choose in this order:

1. w, then the pair and N_D, then a_0 > 0 and L_0 with a_L >= a_0 for admissible L >= L_0, the window fitting. For (B-1) this is (H18) to (H20), and at a fixed L the finite-regulator value is at least a_0 for j and the torus large.
2. r and the constants of (E1) to (E4).
3. The rule, before any L, as in (H21):

       b(L) := max{ 1, (8 A / a_0)^(1 / r) (1 + log L)^(alpha / r) },

   so that 2 tau_(b(L)) <= a_0 / 4 for every L.
4. L >= max(L_0, L_1), admissible, with

       B_1 := max{1, (8 A / a_0)^(2 / r)},   gamma := 2 alpha / r + 2 alpha',   m_0 := ceiling(gamma) + 1,
       B := (15/2) B_1 (2 + 3 A') A' C_s^2 M_*,
       L_1 := exp( max{ 1, 4 B 2^gamma m_0! (2 kappa)^(-m_0) / a_0 } ).                         (O3)

5. b := b(L). From here L and b are numbers.
6. X so large that on the trajectory, at this L and b: omega_L(g_j) <= 1; Mbar_1 <= M_*; (FT) holds within a_0 / 8 at both pairs; and 6 b^2 (2 omega + 2 eta + C_n omega^GS_j) <= a_0 / 8.

Then at fixed level distance from the top, for all large i, the difference of Cov_nu(Y_p, Y_q) at q_n and q_f is at least a_0 / 4, and Theorem 4.1 gives H != 0 on Omega-perp.

Proof. By (E2) and omega_L <= 1, bold-C_n <= 2 + 3 C_n, so by (E2), (E3), (E4) the smoothing term of 6 b^2 eps_j is at most

    (15/2) b(L)^2 (2 + 3 C_n) C_n C_s^2 M_* L^(-2 kappa) <= B (1 + log L)^gamma L^(-2 kappa).

With t := log L >= 1: (1 + t) <= 2 t, and exp(2 kappa t) >= (2 kappa t)^(m_0) / m_0!, so this is at most B 2^gamma m_0! (2 kappa)^(-m_0) t^(gamma - m_0) <= B 2^gamma m_0! (2 kappa)^(-m_0) / t <= a_0 / 4 at L >= L_1. Adding (F-2) at the two pairs, (F-3) and (FT): a_0 - a_0 / 8 - a_0 / 4 - a_0 / 4 - a_0 / 8 = a_0 / 4. []

The printed requirement L^(2 kappa_lift) >= C b^2 C_n^2 C_s^2 Mbar_1 / a_0 is the inequality of step 4 with b = b(L), and L appears on both sides only through powers of log L. (NF-3) keeps the same order, adding the same requirement for b^2 ((5/4) bold-C_n theta_L Mbar_2)^2, a term of size power of log L times L^(-4 kappa), with the L-free limit of Mbar_2 found as in (E4).

### 3.3 The printed order stands: the clip constant is free of L as g_j -> 0

The clip is read only under E_1, at fixed L, in the regime where (FT) already holds. There the moments of X_p are Gaussian, and the L-dependence of C_(n,s) survives only multiplied by something that tends to 0.

**Lemma CL [implication, from the clauses (FT) reads].** Fix L and D. Assume (OS_j)(b), (c) at W = 1, Gamma_pp(1) = 4 P^fib_pp 1_3 from (OS_j)(d), and (GS_j)(c) at W = 1, with any dependence of C_(n,s) on L. Then, uniformly in j, for s = 1, ..., 4,

    limsup_(g_j -> 0) E_1 X_p^s <= (P^fib_pp / 2)^s prod_(i=0)^(s-1) (3 + 2 i),                 (O4)

and for p, q in D and b > 0, with P_m := max(P^fib_pp, P^fib_qq),

    limsup_(g_j -> 0) | Cov_1(Y_p, Y_q) - Cov_1(X_p, X_q) | <= (945 / 8) P_m^4 b^(-2).          (O5)

Proof. Read the chart as (FT) reads it: on an event C of probability at least 1 - omega, X_p = Q_p + g_j Y_p, Q_p = (1/8) |(D xi)_p|^2, |Y_p| <= C(L) (1 + |xi|_loc)^4, since phi = 0 at W = 1. Let T := {|xi|_loc <= R}, R := g_j^(-1/8). By (c) in degree 8 and Chebyshev, P(C and not T) <= (C(L) + omega) g_j. On C and T, X_p <= Q_p + eps_g, with eps_g := C(L) g_j (1 + R)^4 -> 0. So

    E_1 X_p^s <= E_1 [ 1_C (Q_p + eps_g)^s ] + P_1((C and T)^c)^(1/2) (E_1 X_p^(2 s))^(1/2).

The first term is a polynomial of degree 2 s <= 8 in xi, so by (c) it tends to E_N Q_p^s. The second is at most (omega + C(L) g_j)^(1/2) C_(n, 4 s)^(1/2), which tends to 0 at fixed L, because C_(n, 4 s) is finite. Under N(0, C_1), (D xi)_p has covariance 4 P^fib_pp 1_3, so Q_p = (P^fib_pp / 2) |zeta|^2 with zeta standard in R^3, and integration by parts gives E |zeta|^(2 s) = (2 s + 1) E |zeta|^(2 s - 2). This is (O4). (O5) is (O2) at r = 2 with (O4) at s = 4: 2 (945 / 16) = 945 / 8. []

Degree 8 of (OS_j)(c) is exactly what r = 2 needs. Constants in (O5) contain no L.

**(P*) [discharged for (B-1)].** Let P_* be free of L with P^fib_pp <= P_*. For (B-1), P_* = 1. Indeed P^fib_pp <= P^inf_pp, since delta_pp >= 0 by (H6). The flux of a level-j plaquette in the (a, b) plane, n = L^j, is Sum_p w_p F_p over fine (a, b) plaquettes: by (B-1) the coarse flux is n^-4 times the sum, over the n^4 points x of the block, of the circulation around the n x n square at x, and Stokes applies to each square. Thus w_p = n^-4 #{x : p in the square at x}, which gives w_p <= n^-2 and Sum_p w_p = n^2, so Sum_p w_p^2 <= 1. The fine covariance of F is 4 times d (-Delta)^+ d^T, the orthogonal projector onto exact two-forms, which is at most 1. So P^inf_pp = w^T (d (-Delta)^+ d^T) w <= Sum_p w_p^2 <= 1, at every n, S.

**Corollary NT1-F, order B [implication].** Assume what order A assumes, except (E1), which is dropped, and also (P*). Choose: w, the pair, N_D, then a_0, L_0, then

    b_* := (1000 P_*^4 / a_0)^(1/2),   before L and free of L,                                  (O6)

then L >= max(L_0, L_1^*), with L_1^* the formula (O3) at B = (15/2) b_*^2 (2 + 3 A') A' C_s^2 M_*, gamma = 2 alpha'; then X large as in step 6, also so that the left side of (O5) is at most (945 / 8) P_*^4 b_*^(-2) + small, which gives 2 tau_b <= a_0 / 4 since 945 / 4 < 250. The conclusion is that of order A.

So (E1) is not needed for the clip. Only the C_n of (GS_j)(a) and (LE_j) still have to grow slower than L^(2 kappa). **Decision: order B is the form to adopt**, since it keeps the printed sequence b, L, X and reads fewer hypotheses; order A is (H21) as the queue asked, and it is the fallback if (FT) is delivered directly, without (OS_j)(c) in degree 8.

**Size.** With (H18) at d = 64, a_0 is about 1.3e-23, not the 4e-9 printed at `library/nt2-flat-fibre-criterion.md:86`, which came from the enclosures. Order B at (B-1) needs L^(2 kappa) above 3e4 (2 + 3 C_n) C_n C_s^2 M_* / a_0^2, about 2e50 times those constants. This is harmless to the logic, as defect 2 of `gates/free-value-lead-read-28e261c17.md` says, and it conflicts with any fixed L elsewhere.

## 4. Carry-over, checks, reads

**For other owners; no other file was edited.**

- `parts/witness.md:438-442`, `:452`, and the Obligations line `:137`: Lemma 3.6 and (3.4) now have written proofs, section 1 here. The sympy and sampling scripts become evidence only.
- `library/nt2-chart-free-vertex.md:66-72`: replace the hypotheses of RM' by (D1) to (D3) and (RP), and the proof by Theorem RM' here. `parts/witness.md:1474` can drop its caveat on the two inputs.
- `library/nt2-coherence-and-positive-norm.md:39-45`: add the constant c_0 >= 0 to the Kallen-Lehmann form. The claim that any RP vector field with O(4) invariance has this form is Corollary KL, under (D1) to (D3).
- `library/nt2-flat-fibre-criterion.md:68`, `:78`, `:82`, `:84`, `:86` and `parts/witness.md:1430-1435`: (F-3) with the constant of (O2); order B, or order A; the size line with the hand a_0. Replacement for the sentence of the part: "Fix the geometry and a_0, take b_* := (1000 P_*^4 / a_0)^(1/2) free of L by Lemma CL of `library/witness-by-hand.md`, then L, then X large."
- `parts/upper-chain.md:859`, request to the consumer: state that c_E in Ebar is free of L. (E4) needs it.

**Kill tests.** Criteria `checks/hand_witness/CRITERIA.md`, script `kill_tests.py`, results `RESULTS.md`, 2026-11-01, one job under the numeric lock at 61 percent memory free. All 18 checks pass, with the two negative controls behaving as required. They test the formulas of sections 1 to 3 on samples, including the sign of (R3) in the time domain and in Fourier form. A pass refutes nothing and proves nothing: no step above rests on a run. W3d was corrected before its first run, since the draft misplaced the contact term; the correction is recorded in `RESULTS.md`.

**Read.** `FINISH.md`, `GOAL.md`; the Witness sections of `gates/compute-inventory-39189b75b.md` and `gates/compute-inventory-2-28e261c17.md`; `gates/free-value-lead-read-28e261c17.md`; `parts/witness.md:205-269`, `:395-494`, `:1415-1494` and search hits; all of `library/nt2-free-value-by-hand.md`; `library/nt2-chart-free-vertex.md`; `library/nt2-flat-fibre-criterion.md:1-150`; `library/nt2-coherence-and-positive-norm.md:20-69`; `library/witness-interface-moments.md:1-45`; `library/witness-two-separation.md:50-99`; `library/witness-blocked-tree-limit.md:12-80`; in `parts/upper-chain.md`, lines 180, 605-649 and 859-891, as clause statements.

**Not read.** Either hard-core attempt file, or any gate on an attempt. `gates/nt2-gate-2285befef.md`. Lemma 3.7 and the proof of Theorem 3.8 were read and not rechecked. The prefactor of (3.4) was matched to (3.3), not rederived from Proposition 2.2.

## Endpoint

**Discharged:** Lemma 3.6, the Ward identity of the form, and (3.4), given the symbol of Lemma 3.7; (F-3) with its constant; P^fib_pp <= 1 for (B-1); Theorem S, Lemma D, Theorem RM' at scope (D1) to (D3), and Corollary KL.

**Implication:** Corollary NT1-F in orders A and B, and Lemma CL. They assume everything the printed corollary assumes. Order A adds (E1), and both add (E2) to (E4); (E4) includes c_E free of L.

**Gap or open:** every producer clause of NT1-F, H-NET, H-SCALE and w free of L; C_s free of L; tensor multipliers; the one-link sentence of RM'. This is same-model author work with no outside read.
