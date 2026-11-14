# An annealed block-response conversion theorem for 4D Wilson SU(2) (FINISH row 845), by Claude Opus 5.5 (max effort), author

- Clone: `/Users/jonreilly/ym4d-lead/clone`, commit `f1c86d81909cfef4bc95cfa244a7086b1f1599fb` (`git pull --ff-only`: already up to date).
- Lane directory D = `.claude/science/physics-loops/ym4d-hard-route-20261030`. Paths below are relative to D.
- Read in full for this note: FINISH rows 820, 832, 836, 845 (`FINISH.md` lines 896, 908, 912, 921); `library/gap-blockcrit-opus.md` (row 836, all 342 lines); `library/prior/gap-lit-dp.md` (row 821, all); `library/gap-tu-retry.md` (row 786, all 533 lines); `library/gap-vmf-lip.md` lines 59-80 and 205-320 (Theorem V, Corollary V1, Lemma DC).
- Method: by hand. No numeric run was made for this note. Row 820 and row 832 GUIDE values are quoted from FINISH as orientation only.
- Labels: PROVED (hand proof in this note; one author, not an independent check), READ (from a file, with path and line), ARGUED (an inference short of proof), GUIDE (a numeric run that may refute or guide, never discharge), OPEN (missing).
- No repository file was edited. Only this file was written.

## 0. Checkpoint (updated in place)

- Final checkpoint. All sections written: 1 (inputs), 2 (transport fields, the stationary chain, Condition (AN)), 3 (Lemma P1, Lemma PE, Theorem AG; 3.1 Lemma GQ, Theorem AG'), 4 (Lemma Q, Proposition PB, Lemmas FR, H, N, the open input (SP-ext), Theorem LW), 5 (beta window, GUIDE orientation), 6 (Theorem UA, Proposition GFF-AN), 7 (summary, credits, next steps, RESULT).
- Not done: (SP-ext); optimal gauge corrections and explicit numbers for any block; the seed comparison from (AN); an explicit kmax; any computation. No repository file was edited.

## 1. Inputs reused

- Conventions (READ `library/gap-blockcrit-opus.md` lines 18-26). SU(2) is the unit sphere S^3 in R^4. The torus Lambda has link set E. The measure is `mu(dU) = Z^(-1) prod_p exp(beta eps_p x_p) prod_e sigma(dU_e)` with `x_p = Re U_p` and fixed centre signs eps_p. For a link set B, `gamma_B(. | y)` is the conditional law of the links of B given the links y off B. `Gamma_B` is the block heat-bath operator. It is the mu-conditional expectation given the links off B, a self-adjoint projection in L^2(mu). Write x = beta/4.
- Blocks and events (READ lines 43-50 and 116). For a link set B_a, Ev(a) is the set of links off B_a that share a plaquette with B_a. `gamma_(B_a)(. | y)` depends on y only through Ev(a) (Lemma G (i), READ line 53; its proof uses only the plaquette structure, so it holds for any link set).
- The block criterion (BC-gen) (READ line 118): nonnegative numbers K^a_je (j in Ev(a), e in B_a), weights w_e > 0 and a margin kappa > 0 with `sum_(a : e in B_a) sum_(j in Ev(a)) w_j K^a_je <= (n_e - kappa) w_e` for every link e, where `n_e = #{a : e in B_a}`.
- Theorem R (READ lines 130-154): (BC-gen) with worst-case numbers (valid for every exterior) gives contraction, block gap, Langevin gap, comparison and clustering, uniform in the torus. Its seminorms are sup-norm Lipschitz constants. That is the quantifier this note replaces.
- Theorem ST, Proposition CEIL, Theorem U, Proposition GFF (READ lines 176-200, 266-268, 297-307).
- Row 836's open statement (READ line 291): "the same with the supremum over exteriors replaced by an average under the Wilson law of the exterior, together with a theorem that converts annealed block smallness into Theorem R's conclusions".
- Row 821 (READ `library/prior/gap-lit-dp.md` lines 22 and 50): the bad-set and disagreement-percolation conversions in the literature (Gielis-Maes 1995; van den Berg-Maes 1994; Georgii-Haggstrom-Maes 1999) treat quenched random specifications with independent (one-dependent) environments and total-variation influences. They do not cover an environment that is a Wilson Gibbs configuration.
- Theorem V for periodic Villain U(1) (READ `library/gap-tu-retry.md` lines 92-96; checked by row 794 as recorded in `library/gap-blockcrit-opus.md` line 36): at every fixed beta >= 2^14, the gauge-invariant Langevin gap gamma_V(beta; M) tends to 0 as M tends to infinity. Section 1.3 there (READ lines 198-250): in every periodic local limit the score correlations of the bounded smooth gauge-invariant local observable s_p are not absolutely summable.
- Row 832 GUIDE (READ `FINISH.md` line 908): typical-exterior linear responses of a 2^4 block of 32 links. Best interior plaquette: 0.21-0.22 (beta 0.5), 0.71-0.73 (beta 1), 2.29-2.68 (beta 2). Block-mean plaquette per its Lipschitz bound: 0.24, 1.0-1.1, 7.2-7.7. Row 820 GUIDE (READ line 896): typical single-link influence row sums 2.1 to 4.1 at every order-one beta.

## 2. The response identity and the exact annealed condition

### 2.1 Gradients and transport fields

For a smooth function g on SU(2)^E, a link e and a configuration U, let `|grad_e g|(U)` be the norm of the Riemannian gradient of g in the variable U_e (unit round metric on S^3). Write `||grad_e g||_inf` for its supremum.

Fix a finite family A of link sets B_a (blocks). For a block a write `w_a(sigma, y) = prod_(p meets B_a) exp(beta eps_p x_p)`. Here sigma is the block configuration and y the exterior. So `gamma_a(d sigma | y) = w_a(sigma, y) d sigma / Z_a(y)`, with d sigma Haar on SU(2)^(B_a).

For j in Ev(a) and a unit tangent vector v at y_j, put `h^a_(j,v)(sigma, y) = d/dt log w_a(sigma, y_j(t))` at t = 0, where y_j(t) is the geodesic from y_j with velocity v. Then `h^a_(j,v) = beta sum_(p contains j) eps_p (d/dt) x_p`, a smooth function of sigma.

**Definition (transport field).** A transport field for (a, j) is a family `xi^a_(j,v)(sigma, y)`, linear in v, of measurable tangent vector fields on the block (one tangent vector at sigma_c for each c in B_a) such that, for every exterior y and every smooth psi on SU(2)^(B_a),

    gamma_a( <grad_B psi, xi^a_(j,v)> | y ) = Cov_(gamma_a(.|y)) ( psi, h^a_(j,v) ).          (2.1)

Its response field is `R^a_jc(sigma, y) = sup_(|v| = 1) |xi^a_(j,v),c (sigma, y)|` for c in B_a.

**Lemma T (PROVED; standard elliptic facts).** (i) Transport fields exist. One choice is `xi = grad_B phi`, where phi solves `-L_y phi = h - gamma_a(h | y)` and `L_y = Delta_B + <grad_B log w_a, grad_B>` is the Langevin generator of the block law. (ii) For this choice and a vertex block B(Q), xi is orthogonal to the orbits of the internal gauge group G_Q: internal gauge directions cost nothing. (iii) For every smooth g, every j in Ev(a) and every unit v at y_j,

    d/dt Gamma_a g = Gamma_a( d_(j,v) g ) + gamma_a( <grad_B g, xi^a_(j,v)> ).                (2.2)

*Proof.* (i) The block density with respect to Haar is smooth and lies between two positive constants, uniformly in y. Holley-Stroock from the Haar gap gives `L_y` a spectral gap. So the Poisson equation has a unique centred solution in H^1, smooth by elliptic regularity, and linear in v. Integration by parts gives `gamma_a(<grad psi, grad phi>) = -gamma_a(psi L_y phi) = Cov(psi, h)`. (ii) The density w_a and Haar measure are G_Q-invariant (READ `library/gap-blockcrit-opus.md` Lemma G (ii), line 54). So h is G_Q-invariant as a function of sigma, L_y commutes with the G_Q action, and phi is G_Q-invariant. The gradient of an invariant function is orthogonal to the orbits. (iii) Differentiate `Gamma_a g(y) = integral g(sigma, y) w_a dsigma / Z_a` under the integral sign (smooth integrand, compact space). The derivative of the density gives `Cov(g(., y), h)`. Apply (2.1) with psi = g(., y). QED

**Corollary T1 (PROVED).** For every smooth g, block a and configuration with exterior y,

    |grad_j Gamma_a g|(y) <= Gamma_a(|grad_j g|)(y) + sum_(c in B_a) gamma_a( R^a_jc |grad_c g| | y )   (j in Ev(a)),
    |grad_j Gamma_a g| = 0  (j in B_a),      |grad_j Gamma_a g| <= Gamma_a(|grad_j g|)  (otherwise).      (2.3)

*Proof.* Take the supremum over unit v in (2.2) and use `|<grad_c g, xi_c>| <= |grad_c g| R^a_jc |v|`. The other two cases are immediate. QED

### 2.2 The stationary block chain

Let `(a_s)_(s >= 1)` be independent and uniform on A. Let U_0 have law mu. Given U_(s-1) and a_s, let U_s equal U_(s-1) off B_(a_s) and resample B_(a_s) from `gamma_(a_s)(. | U_(s-1))`. This is the Markov chain of `P = |A|^(-1) sum_a Gamma_a`. Each Gamma_a preserves mu, so every U_s has law mu, also conditionally on the block sequence (PROVED). This chain is the environment generated by the measure itself. It is dependent in space and in time.

### 2.3 The exact annealed condition

A **jump** of the chain at time s is a triple (s, j, c) with j in Ev(a_s) and c in B_(a_s). Its random weight is `R^(a_s)_jc(U_s)`, evaluated at the configuration just after the update (the new block, the old exterior).

**Condition (AN).** There are transport fields for every (a, j), nonnegative numbers k^a_jc (j in Ev(a), c in B_a), weights w_e > 0 and a margin kappa > 0 such that:

(AN1) *annealed path moments:* for every finite block sequence a_1, ..., a_t and every set of jumps (s_1, j_1, c_1), ..., (s_m, j_m, c_m) at distinct times s_1 < ... < s_m <= t,

    E[ prod_(i=1..m) R^(a_(s_i))_(j_i c_i)(U_(s_i))  |  a_1, ..., a_t ]  <=  prod_(i=1..m) k^(a_(s_i))_(j_i c_i) ;        (AN1)

(AN2) *coefficient:* the numbers k satisfy (BC-gen) with weights w and margin kappa:

    sum_(a : e in B_a) sum_(j in Ev(a)) w_j k^a_je  <=  (n_e - kappa) w_e   for every link e.                  (AN2)

In the symmetric case (one shape, its translates and rotations, numbers k invariant under these symmetries, w = 1, all n_e = n) write `alpha_AN = |B|^(-1) sum_(j, c) k^a_jc`; then (AN2) reads `alpha_AN < 1` with kappa = n (1 - alpha_AN) (the proof of Lemma SYM, READ `library/gap-blockcrit-opus.md` line 122, applies verbatim to any symmetric numbers).

**Remark (PROVED).** The proof of Theorem AG (a) below uses (AN1) only through the path sums averaged over the block sequence, with the stay indicators included. So (AN1) may be weakened to: for every path, `E[ prod_s omega_s ] <= prod_s (M/|A|)_(e_(s-1) e_s)`, in the notation of Lemma PE and of that proof.

**What (AN) is (ARGUED).** (AN1) asks only for moments under the Wilson law and its own heat-bath chain. It needs no independence and no uniformity over exteriors. The quenched criterion corresponds to `sup_y gamma_a(R | y) <= k` (Lemma Q below). Section 4 shows which parts of (AN1) are automatic (the block variables) and which are the real input (the exterior variables, through time).

## 3. The conversion theorem

Write `q = 1 - kappa/|A|`, `Delta_(inf,w)(f) = sum_e w_e ||grad_e f||_inf`, `n_max = max_e n_e`, `w_min = min_e w_e`. Let P_a be the set of plaquettes that meet B_a.

**Lemma P1 (PROVED; L^1 block Poincare, uniform in the exterior).** For every block a, exterior y and smooth h,

    gamma_a( |h - gamma_a(h | y)| | y )  <=  c_1(a) sum_(e in B_a) gamma_a( |grad_e h| | y ),   c_1(a) = (pi/2) exp(6 beta |P_a|).      (3.1)

*Proof.* Step 1 (one sphere). For smooth phi on S^3, `integral integral |phi(s) - phi(s')| dsigma(s) dsigma(s') <= (pi/2) integral |grad phi| dsigma`. For s' not equal to -s the minimizing geodesic from s to s' is unique and has length d(s, s') <= pi, and `|phi(s) - phi(s')|` is at most the integral of |grad phi| along it. The occupation measure of these geodesics under sigma x sigma is invariant under O(4), which acts transitively on S^3. So it equals `E[d(s, s')] sigma`. The inner product of two independent uniform points is symmetric about 0, so `E[arccos <s, s'>] = pi/2`. Step 2 (product). Order the links of B_a and change one coordinate at a time. Under Haar x Haar each step is Step 1 in one coordinate, with the others Haar distributed. So `integral integral |h(x) - h(x')| <= (pi/2) sum_e Haar(|grad_e h|)`. Step 3 (density). The density rho of gamma_a(. | y) with respect to normalized Haar lies in `[exp(-2 beta |P_a|), exp(2 beta |P_a|)]`, because `w_a` lies in `[exp(-beta |P_a|), exp(beta |P_a|)]`. Then `gamma_a(|h - gamma_a h|) <= (sup rho)^2 integral integral |h(x) - h(x')| dHaar dHaar` and `Haar(|grad_e h|) <= (inf rho)^(-1) gamma_a(|grad_e h|)`. QED

The same proof gives c_1 = (pi/2) on Haar circles times the density ratio for any compact model with bounded plaquette weights (PROVED; used in Section 6).

**Lemma PE (PROVED; path expansion along the stationary chain).** For smooth f, t >= 0 and every link e,

    mu( |grad_e P^t f| )  <=  E[ sum_(e_1, ..., e_t) prod_(s=1..t) omega_s(e_(s-1), e_s) |grad_(e_t) f|(U_t) ],   e_0 = e,      (3.2)

where `omega_s(e', e') = 1{e' not in B_(a_s)}`, `omega_s(e', c) = 1{e' in Ev(a_s), c in B_(a_s)} R^(a_s)_(e'c)(U_s)` for c not equal to e', and the chain is that of 2.2.

*Proof.* Corollary T1, averaged over a, is the pointwise one-step bound `|grad_e P g|(U) <= E[ sum_(e') omega_1(e, e') |grad_(e') g|(U_1) | U_0 = U ]`: the term `Gamma_a(|grad_e g|)` is the stay step, and `gamma_a(R^a_ec |grad_c g|)` is the jump step with R evaluated at the updated configuration. By induction on t the same bound holds pointwise with the chain started at U: apply the one-step bound to `g = P^(t-1) f`, then the induction hypothesis at U_1. The weights omega_1 are nonnegative and functions of (U_0, a_1, U_1), and given U_1 the chain from time 1 on is the chain started at U_1 (Markov property). Integrate over U_0 with law mu. QED

**Theorem AG (PROVED; the annealed conversion theorem).** Assume (AN) for a block family A on a periodic torus (any torus on which the family is defined, any centre signs). Then:

(a) *Annealed gradient contraction.* For every smooth f and t >= 0, `sum_e w_e mu(|grad_e P^t f|) <= q^t Delta_(inf,w)(f)`.

(b) *Block gap.* For every f in L^2(mu), `sum_a mu(Var_(B_a) f) >= (kappa/2) Var_mu f`.

(c) *Langevin gap.* If every block law has Poincare constant at least c_* for every exterior, then `mu(|grad f|^2) >= (kappa c_*/(2 n_max)) Var_mu f` for every smooth f. For a fixed shape and fixed beta one may take `c_* = 3 exp(-4 beta max_a |P_a|) > 0`. In particular the gauge-invariant Langevin gap is at least `kappa c_*/(2 n_max)`.

(d) *Exponential clustering.* In the symmetric case (alpha_AN < 1), suppose k^a_jc > 0 only when j and c lie within distance r. Let f be smooth, g bounded measurable depending on the links of Y, and m_0 the least number of steps of length at most r that join the links of the blocks meeting Y to the support of grad f. Then

    |Cov_mu(f, g)|  <=  ( 9 c_1 / (1 - alpha_AN) ) sup|g| Delta_inf(f) alpha_AN^(m_0),   c_1 = max_a c_1(a).          (3.3)

All constants depend on kappa, n_max, w, c_1, c_*, r and alpha_AN only, not on the torus.

*Proof.* (a) By (3.2), `mu(|grad_e P^t f|) <= sum_i ||grad_i f||_inf E[ sum over paths from e to i of prod_s omega_s ]`. Fix the block sequence. On a path the stay factors are indicators fixed by the blocks. The jump factors are values of R at distinct times, because a path makes one move per time. So (AN1) bounds the conditional expectation of the product by `prod_s m(e_(s-1), e_s; a_s)`, with `m(e, e; a) = 1{e not in B_a}` and `m(e, c; a) = 1{e in Ev(a), c in B_a} k^a_ec`. The blocks are independent and uniform, so the average over them is `((M/|A|)^t)_(e i)` with `M = |A| I - N + K`, `N = diag(n_e)`, `K_ec = sum_a k^a_ec`. By (AN2), `w^T M <= (|A| - kappa) w^T` entrywise: the i-th entry is `(|A| - n_i) w_i + sum_e w_e K_ei <= (|A| - kappa) w_i`. So `w^T (M/|A|)^t <= q^t w^T`.

(b) Let f be smooth and h = P^s f. By (3.1) integrated over the exterior, `||h - P h||_(L^1(mu)) <= |A|^(-1) sum_a c_1 sum_(e in B_a) mu(|grad_e h|) <= (c_1 n_max / (|A| w_min)) q^s Delta_(inf,w)(f)`, using (a). So P^s f is Cauchy in L^1(mu). Its limit f_inf is bounded by sup|f| and satisfies `P f_inf = f_inf`. Then `0 = <f_inf, (I - P) f_inf> = |A|^(-1) sum_a ||f_inf - Gamma_a f_inf||^2`, so f_inf equals a function of the links off B_a for every a. The blocks cover E (a link in no block would violate (AN2)). mu and Haar are mutually absolutely continuous, and for Haar the operators that integrate out B_a commute; so f_inf is a.s. constant, equal to `mu(f)`. Summing the geometric series, `||P^t f - mu(f)||_1 <= (c_1 n_max/(kappa w_min)) q^t Delta_(inf,w)(f)` (here `|A|(1 - q) = kappa`). Hence `Var(P^t f) <= ||P^t f - mu f||_inf ||P^t f - mu f||_1 <= C(f) q^t` with `C(f) = 2 sup|f| c_1 n_max Delta_(inf,w)(f)/(kappa w_min)`. For centred f with spectral measure nu_f for the self-adjoint P, `Var(P^t f) = integral s^(2t) dnu_f(s)`, so nu_f gives no mass to `|s| > q^(1/2)`. Smooth functions are dense in L^2(mu). So the spectrum of P on centred functions lies in `[-q^(1/2), q^(1/2)]`, and `sum_a mu(Var_(B_a) f) = |A| <f, (I - P) f> >= |A| (1 - q^(1/2)) Var f >= (kappa/2) Var f`, since `1 - q^(1/2) >= (1 - q)/2`. The constant C(f) and c_1 do not enter the rate.

(c) As in Theorem R (c) (READ `library/gap-blockcrit-opus.md` line 150): `sum_a mu(|grad_(B_a) f|^2) <= n_max mu(|grad f|^2)`, and the block Poincare inequality holds conditionally on each exterior. Use (b). For c_*: the Laplacian on the unit S^3 has first nonzero eigenvalue 3, the product of spheres has the same gap, and Holley-Stroock with the density ratio `exp(4 beta |P_a|)` of Step 3 above gives c_*.

(d) Put `G = 1 + g/(2 sup|g|)` and `mut = G mu / mu(G)`, so `mut <= 3 mu`. For a block that does not meet Y, `mut(Gamma_a h) = mut(h)` (Bayes; READ the same step in `library/gap-blockcrit-opus.md` line 154). Telescope: `mut(f) - mu(f) = sum_(t >= 0) mut(P^t f - P^(t+1) f)`; the remainder `mut(P^T f) - mu(f)` is at most `3 ||P^T f - mu f||_1`, which tends to 0 by (b). For a block meeting Y, `|mut(h - Gamma_a h)| <= 3 mu(|h - Gamma_a h|) <= 3 c_1 sum_(e in B_a) mu(|grad_e h|)`. With h = P^t f and the matrix bound of (a), `sum_t (M/|A|)^t = |A| (N - K)^(-1) = |A| n^(-1) sum_(m >= 0) (K/n)^m`. A nonzero entry of (K/n)^m from a link of a block meeting Y to the support of grad f needs m >= m_0. Each link lies in n blocks, and the column sums of (K/n)^m are alpha_AN^m. So `|mut(f) - mu(f)| <= 3 c_1 alpha_AN^(m_0) Delta_inf(f)/(1 - alpha_AN)`. Finally `Cov(f, g) = 2 sup|g| mu(G) (mut(f) - mu(f))` and `mu(G) <= 3/2`. QED

**What the theorem does (ARGUED).** The sup-norm Lipschitz seminorms of Theorem R are replaced by L^1(mu) norms of gradients. Three facts make this close. First, the block heat bath preserves mu, so every configuration on the chain has law mu. Second, the L^1 block Poincare inequality (3.1) turns L^1 gradient decay into L^1 decay of `P^t f - mu f` with a constant that is exponential in the block size but uniform in the exterior; this constant never enters the rate. Third, a variance bound of the form `C(f) q^t` on a dense class pins the spectrum. The environment is the chain itself. No independence and no uniformity over exteriors is used. Gauge directions inside a vertex block cost nothing (Lemma T (ii)).

**What it does not give (OPEN).** The comparison statement of Theorem R (d) for a measure mut that is not dominated by a fixed multiple of mu. Corollary SEED of row 836 (READ `library/gap-blockcrit-opus.md` lines 232-240) uses that statement with mut the folded law of the long torus; its density with respect to mu is not bounded uniformly in the cut. So the annealed theorem gives the Langevin gap and clustering on each torus, but not the seed comparison as written. A route to the seed from (b)-(d) needs either (AN) for the interpolating measures between the a-torus and the 2a-torus, or the standard bridge from uniform clustering to the transfer-matrix gap (Osterwalder-Seiler positivity; ARGUED, not proved here).

### 3.1 The gauge-quotient form (boundary gauge as exterior jumps)

For a block a, a *gauge correction* is a measurable field `zeta(sigma, y)` of infinitesimal gauge motions at the vertices touched by B_a: at each configuration it is the derivative at t = 0 of `exp(t X(sigma, y)).U` for some generators `X_u(sigma, y)` in the Lie algebra, one per vertex u. It moves the links of B_a and the exterior links at the outer vertices. Given a transport field xi for (a, j), put `R'^a_jc = sup_(|v|=1) |(xi + zeta)_c|` for c in B_a and `R''^a_je = sup_(|v|=1) |zeta_e|` for exterior links e at an outer vertex (zeta linear in v).

**Lemma GQ (PROVED).** For every smooth gauge-invariant g and j in Ev(a),

    |grad_j Gamma_a g|  <=  Gamma_a(|grad_j g|) + sum_(c in B_a) gamma_a( R'^a_jc |grad_c g| ) + sum_e gamma_a( R''^a_je |grad_e g| ).        (3.4)

*Proof.* At each configuration zeta is tangent to the gauge orbit, and the gradient of an invariant function is orthogonal to the orbit. So `<grad_B g, zeta_B> + <grad_ext g, zeta_ext> = 0` pointwise, and `<grad_B g, xi> = <grad_B g, xi + zeta_B> + <grad_ext g, zeta_ext>`. Insert this in (2.2) and take the supremum over unit v. QED

**Theorem AG' (PROVED).** Add to the jumps of 2.3 the *gauge jumps* (s, j, e) with j in Ev(a_s) and e an exterior link of a_s at an outer vertex, with weight `R''^(a_s)_je(U_s)`, and use R' for block jumps. If (AN1) holds for these weights (numbers k^a_jc for block jumps and k''^a_je for gauge jumps) and (AN2) holds in the matrix form `sum_j w_j (K + K'')_je <= (n_e - kappa) w_e` for every link e, with `K_jc = sum_a k^a_jc` and `K''_je = sum_a k''^a_je` (a gauge jump from j to j adds to the diagonal), then Theorem AG (a)-(d) hold for gauge-invariant smooth f, and (b), (c) give the gauge-invariant block gap and the gauge-invariant Langevin gap `kappa c_*/(2 n_max)`.

*Proof.* P commutes with gauge transformations (READ `library/gap-blockcrit-opus.md` Lemma G (iv), line 56), so every P^t f is invariant and (3.4) applies at every step of Lemma PE. A gauge jump lands on a link that the update does not resample, so the path expansion and the matrix bound of Theorem AG (a) hold with `M = |A| I - N + K + K''`. The spectral step of (b) runs in the closed subspace of invariant functions, where smooth invariant functions are dense (average over the compact gauge group); the L^1 block Poincare inequality and the block Poincare constant hold for all functions. QED

**Reading (ARGUED).** With zeta = 0 this is Theorem AG. For a vertex block the Poisson field is already horizontal for the internal gauge (Lemma T (ii)). The correction zeta at the outer vertices is the annealed form of the boundary gauge of row 836: the pure-gauge part of the block response is moved onto exterior links at the outer vertices, where it is paid as a gauge jump. For a link block with no internal gauge group, such as the row 832 block, every vertex is outer, and the best zeta decides how much of the gauge-variant response of 5 (1) survives. Optimal zeta for explicit blocks: OPEN.

## 4. Rare bad exteriors: what is automatic and what is the input

### 4.1 The block variables are annealed for free

**Lemma Q (PROVED).** If `k^a_jc >= sup_y gamma_a( R^a_jc(., y) | y )` for all a, j, c, then (AN1) holds with these numbers.

*Proof.* Fix the block sequence and the jumps. Let F be the history up to just before the last jump time s_m. Given F, the new block at s_m has law `gamma_(a_(s_m))(. | y)` with y the current exterior, and the other factors are F-measurable. So the conditional expectation of the last factor is `gamma_a(R^a_(j_m c_m)(., y) | y) <= k_m`. Induct backwards. QED

**Reading (ARGUED).** So Theorem AG contains the criterion "worst case over exteriors, average over the block". With Kantorovich-Rubinstein and Beckmann duality one expects the best such numbers to match the W_1 responses of Lemma GF (READ `library/gap-blockcrit-opus.md` line 86); the per-link form of that duality is not proved here, so Theorem ST is not re-derived from Theorem AG (OPEN detail). The proof of Lemma Q works only for the last jump. For an earlier jump at time s_i, the path lands at a link c_i of the fresh block, and c_i is an exterior event of the next block on the path. So the next exterior contains the block just sampled. The path carries its environment along. This is exactly the dependence that a quenched (independent-environment) theory, as in Gielis-Maes (READ `library/prior/gap-lit-dp.md` line 22), never meets.

### 4.2 A Peierls form of (AN1)

**Proposition PB (PROVED).** Suppose that for every block a there is an event Bad_a, a function of the links of B_a and Ev(a), and numbers k^g, k^max such that

(P1) `R^a_jc <= kg^a_jc` off Bad_a (good responses);

(P2) `R^a_jc <= kmax^a_jc` everywhere (a finite bound; for the Poisson field of Lemma T it exists by continuity on the compact configuration space, PROVED; an explicit value is OPEN);

(P3) (space-time Peierls bound) for every block sequence and every finite set S of times, `P( U_s in Bad_(a_s) for all s in S | blocks ) <= eps^|S|`.

Then (AN1) holds with `k = kg + eps kmax`. In the symmetric case (AN2) holds if `alpha_g + eps alpha_max < 1`, where alpha_g and alpha_max are the symmetric coefficients of kg and kmax.

*Proof.* On a path with m jumps, `prod_i R_i <= prod_i (kg_i 1{good at s_i} + kmax_i 1{bad at s_i})`. Expand the product over subsets S of the jumps, bound the indicator of "good off S" by 1, and use (P3): the expectation is at most `sum_S prod_(i not in S) kg_i prod_(i in S) kmax_i eps^|S| = prod_i (kg_i + eps kmax_i)`. QED

**Lemma FR (PROVED; fresh badness).** If `Bad_a = {(sigma, y) : sigma in D_a(y)}` with `sup_y gamma_a(D_a(y) | y) <= eps`, then (P3) holds with this eps.

*Proof.* At each time the new block is fresh given the past: `P(bad at s | past, blocks) = gamma_(a_s)(D(y_s) | y_s) <= eps`. Condition successively on the past at the times of S, from the last one back. QED

**Lemma H (PROVED; the Hoelder bound and its limit).** For paths with at most m jumps, (AN1) holds with `k^a_jc = ||R^a_jc||_(L^m(mu))`: by Hoelder with m factors, each evaluated at a configuration of law mu. As m grows these numbers increase to the sup-norm of R^a_jc. So (AN1) for all path lengths lies between the one-point average and the worst case; it is a statement about all mixed moments of the responses along the chain.

**Lemma N (PROVED; necessary conditions).** (i) If (AN) holds, then `mu(R^a_jc) <= k^a_jc`; in the symmetric case the one-point annealed coefficient `alpha_1 = |B|^(-1) sum_(j, c) mu(R^a_jc)` is at most alpha_AN < 1. (ii) For every smooth block observable O with `|grad_c O| <= 1` for all c in B_a, `sum_j mu(|grad_j Gamma_a O|) <= sum_(j, c) mu(R^a_jc)`. (iii) Hence, for one such observable O_c per block link c with `|grad_(c') O_c| = 0` for c' not equal to c, `|B|^(-1) sum_c sum_j mu(|grad_j Gamma_a O_c|) <= alpha_AN`, for every choice of transport fields. (iv) If the links of B_a are partitioned into plaquettes p_1, ..., p_L (so 4L = |B_a|), then `alpha_AN >= |B|^(-1) sum_k rho(x_(p_k)) >= (1/4) min_k rho(x_(p_k))`, where `rho(O) = sum_j mu(|grad_j Gamma_a O|)` is the annealed response row sum of O.

*Proof.* (i) is (AN1) with one jump. (ii) By (2.2), for O depending on the block only, `|grad_j Gamma_a O| <= sum_c gamma_a(|grad_c O| R^a_jc)`; integrate over mu. (iii) Apply (ii) to each O_c and sum. (iv) `|grad_c x_p| <= 1` for the four links c of p (the derivative of `Re(U_c T)` along a unit tangent is `Re(v T)`, at most `|v||T| = 1`) and 0 elsewhere; apply (ii) to each x_(p_k) and sum over the partition. QED

For the quotient form of Theorem AG' (3.1), (ii) and (iv) hold with R' in place of R for gauge-invariant O that depend on the block only: the gauge-jump terms of (3.4) vanish because `grad_e O = 0` off the block (PROVED). Part (iii) uses gauge-variant observables and applies to Theorem AG only.

So the typical linear response of block observables, the quantity of the row 832 guide, is a lower bound for what (AN) needs. It is never an upper bound.

### 4.3 What is missing for order one: exterior badness through time (OPEN)

**Reading (ARGUED).** Lemma FR handles badness that sits in the fresh block. With Lemma Q it gives nothing beyond the quenched-exterior criterion. The worst case of the lane sits in the exterior: the zero-field exteriors at which Corollary V1 is attained (READ `library/gap-blockcrit-opus.md` line 270). Exterior badness can persist. If the bad event depends only on the exterior and the exterior is not resampled between two updates of the block, the two bad events coincide, and (P3) fails for that pair. So for exterior events (P3) is a space-time Peierls bound for the stationary heat-bath chain.

**The exact missing statement (SP-ext), OPEN.** For one block shape and one beta, an exterior event Bad_a with (P1), (P2) and (P3) along the stationary block chain, and `alpha_g + eps alpha_max < 1`.

**Possible suppliers (ARGUED; the literature named here was recalled, not read in this session).**
- At one time and for blocks on the sites of a reflection lattice, chessboard estimates under reflection positivity bound `P(all bad)` by `z^|S|`, where z is the chessboard norm of the bad event (Frohlich, Israel, Lieb and Simon; reflection positivity of the Wilson action is due to Osterwalder and Seiler, listed in `library/prior/gap-lit-dp.md` line 42). The chessboard norm is the probability of the bad event repeated over the whole torus, to the power 1/N. It is a free-energy quantity, not a typical probability; whether it is small for a zero-field-type event at order one is OPEN.
- In time, the stationary chain is reversible, so its path measure is reflection positive under time reflection (ARGUED). A joint space-time chessboard bound for the block chain is OPEN.
- Persistence can be paid by size. A path that stays inside one bad space-time region gains at most a factor kmax per jump there. A cluster form of (P3), with eps per unit of space-time volume of a bad region and a count of regions, would replace eps^|S|; that form is not proved here (OPEN).

**No ceiling from Proposition CEIL (PROVED).** Proposition CEIL (READ `library/gap-blockcrit-opus.md` line 266) concerns the hypothesis of Lemma GF, a worst-case single-site walk sum. (AN) uses no single-site bound: transport fields exist for every block and every beta (Lemma T). So CEIL does not bound the range of (AN).

### 4.4 A quenched alternative: bad exteriors paid by local weights (Lyapunov form)

For bounded measurable weights `W_e(U) >= 1`, put `Delta_W(g) = sum_e mu(W_e |grad_e g|)`.

**Theorem LW (PROVED).** Suppose that for every link c and every configuration U

    Phi_c(U) := sum_(a : c not in B_a) Gamma_a(W_c)(U) + sum_(a : c in B_a) sum_(e in Ev(a)) Gamma_a(W_e)(U) R^a_ec(U)  <=  (|A| - kappa) W_c(U).     (LW)

Then `Delta_W(P g) <= q Delta_W(g)` for smooth g, and the conclusions (b) and (c) of Theorem AG hold with the same constants.

*Proof.* For e not in B_a, `|grad_e Gamma_a g|` is a function of the links off B_a, so `mu(W_e |grad_e Gamma_a g|) = mu(Gamma_a(W_e) |grad_e Gamma_a g|)`. Multiply (2.3) by the exterior function `Gamma_a(W_e) >= 0` and integrate. The conditional-expectation identity `mu(Y Gamma_a Z) = mu(Y Z)` for exterior-measurable Y gives `mu(W_e |grad_e Gamma_a g|) <= mu(Gamma_a(W_e) |grad_e g|) + 1{e in Ev(a)} sum_c mu(Gamma_a(W_e) R^a_ec |grad_c g|)`. Average over a and collect the terms by the link that carries `|grad g|`: `Delta_W(P g) <= |A|^(-1) sum_c mu(Phi_c |grad_c g|) <= q Delta_W(g)`. Since W >= 1, `sum_e mu(|grad_e P^s f|) <= q^s ||W||_inf Delta_inf(f)`, and the proof of Theorem AG (b), (c) runs unchanged, with `||W||_inf` entering only the constant C(f). QED

**What (LW) does (ARGUED).** With constant weights, (LW) is the pointwise form of (BC-gen). With weights that are large near bad blocks, a rare bad block can be paid locally: the receivers inside it get a large weight, its sources a smaller one. The price is the drift term `Gamma_a(W_c) - W_c` of the spectator updates, which is controlled by the largest probability `p_create` that one update creates a bad block near c, uniformly in the configuration. That is a quenched bound on a probability, not on a response.

**Where (LW) stops (ARGUED).** A trial potential `W_c = 1 + Lambda sum_b theta^(d(c,b)) 1{b bad}` works for isolated bad blocks, but two adjacent bad blocks force `theta^(-1) X <= n - kappa`, with X the bad response total into a link, which fails when X is large and theta < 1. More generally a cycle of K-steps inside a bad region whose responses multiply to more than 1 per turn cannot be compensated by any potential, because weights return to their value around a cycle. At order-one beta such regions plausibly have positive probability (row 820 GUIDE: typical single-link influence sums 2 to 4); at small beta they do not exist, since R = O(beta). So a pointwise (quenched) criterion with local weights cannot cover amplifying bad clusters; only the motion of the environment in time can, which is the space-time input (P3) of Proposition PB. This is why (SP-ext) of 4.3 is the exact missing statement.

## 5. At which beta (AN) could hold (GUIDE orientation only)

**Fixed points (READ).** Worst case, star blocks: (BC) holds for beta < (sqrt 37 - 5)/3 = 0.3609 (Theorem ST, `library/gap-blockcrit-opus.md` line 181). Worst-case single-site responses inside vertex blocks give nothing at beta >= 0.775 (Proposition CEIL, line 266); by 4.3 that ceiling does not apply to (AN). At beta = 0.5 the worst-case star coefficient is alpha_*(0.5) = 2.08 (line 276).

**Small beta (ARGUED).** For the Poisson transport field, `|grad phi| = O(beta)` pointwise as beta tends to 0 (the source h is O(beta) and L_y tends to the Haar Laplacian), so Lemma Q gives (AN) with numbers O(beta) and (AN2) holds for small beta on any fixed shape. So Theorem AG is not vacuous. An explicit threshold from this route is not computed.

**Reading of the row 832 guide (ARGUED from GUIDE; it decides nothing).** By Lemma N, typical responses of block observables are lower bounds for the numbers that (AN) needs; they can exclude (AN) for a block, never establish it. The row 832 block is a link block of 32 links (the links inside a 2^4 vertex cube) with a typical Wilson exterior. Its 32 links split into 8 disjoint plaquettes (4 squares in each of the two factors of the 4-cube graph Q_2 x Q_2), so Lemma N (iv) applies.

| beta | best interior plaquette (invariant) | block-mean plaquette per Lipschitz bound | block-link coordinates (non-invariant) |
|---|---|---|---|
| 0.5 | 0.21-0.22 | 0.24 | 1.22-1.26 |
| 1.0 | 0.71-0.73 | 1.0-1.1 | 2.17-2.21 |
| 2.0 | 2.29-2.68 (noise 1.0) | 7.2-7.7 | 4.0-5.2 |

(1) *Non-invariant observables.* If the calibration values are row sums of single-link coordinate observables normalized as in Lemma N (iii) (the FINISH row does not state the normalization; not checked here), then for this link block alpha_AN >= 1.2 at beta 0.5, 2.2 at beta 1 and 4 at beta 2: (AN) for all functions fails for it at every tested beta. Every vertex of the 2^4 cube has links that leave the cube, so this block has no internal gauge group, and (AN) for all functions pays its gauge directions. So Theorem AG should be used with vertex blocks, where Lemma T (ii) removes the internal gauge directions, or in the gauge-quotient form of Theorem AG' (3.1), where the boundary gauge is paid as exterior gauge jumps; the optimal gauge correction for this block is OPEN.

(2) *Invariant observables.* Lemma N (iv) with the best plaquette gives only `alpha >= rho_best/4`: about 0.05, 0.18 and 0.57-0.67 at beta 0.5, 1 and 2. The block mean, divided by its Lipschitz bound (if that bound is the largest per-link gradient; not stated in the FINISH row), gives by Lemma N (ii) a total-response lower bound of 7.2-7.7 at beta 2, that is about 0.23 per link. So in the per-link normalization of (AN2) the invariant guide values exclude nothing up to beta 2, for the gauge-quotient form of Theorem AG'. They are lower bounds from one observable each; the true per-link totals can be much larger.

(3) *Orientation.* The invariant per-observable responses cross 1 between beta 1 and beta 2. If the per-link coefficient of a gauge-quotient criterion is of the size of the per-observable response, as the reading of row 836 assumed (READ `library/gap-blockcrit-opus.md` line 276), then small blocks could satisfy (AN) up to about beta 1 and not at beta 2. That is the window I would expect for blocks of this size: beyond the proved 0.3609, below order one. At beta 0.5 the typical invariant responses (about 0.2) sit a factor of about 10 below the worst-case star coefficient 2.08; that is the room an annealed criterion could use. Multi-point moments (4.3) can only raise the needed numbers above the one-point values (Lemma H).

(4) *Order one.* At beta near 2 blocks larger than the correlation length xi are needed. As in row 836 (READ line 289), (3.3) gives invariant correlations decaying at rate at least `log(1/alpha_AN)/r`, so `r >= xi log(1/alpha_AN)` (PROVED from (3.3)). For blocks small compared with xi at weak coupling, the block law is close to a Gaussian law whose covariance does not depend on the exterior, so averaging over exteriors gains nothing there (row 836, line 289: Gaussian star coefficient 2; Proposition GFF-AN below). The annealed gain is an intermediate-coupling effect for small blocks, and an effect of the mass for blocks larger than xi (ARGUED).

## 6. Binding test: periodic Villain U(1) in its Coulomb phase

The model and Theorem V (READ `library/gap-tu-retry.md` lines 61-96): angles on the links of `T_M = (Z/MZ)^4`, weight `prod_p phi_beta((d_1 theta)_p)` with phi_beta positive (Poisson summation, line 73), link metric dtheta^2, and gamma_V(beta; M) the gauge-invariant Langevin gap; at every fixed beta >= 2^14, gamma_V(beta; M) tends to 0.

**Theorem UA (PROVED).** Fix beta >= 2^14. Let a finite link-block shape (a vertex block or any link set) generate a family on T_M by translations (with any subgroup of the hyperoctahedral group). For every kappa > 0 there is M_0 such that for every M >= M_0 no choice of transport fields, numbers k and weights w satisfies (AN) with margin kappa for the periodic Villain measure. Also, in the symmetric case no (AN) with `alpha_AN <= alpha < 1` and a fixed range r holds on infinitely many T_M.

*Proof.* Every step of Theorem AG holds for this model. The block density with respect to Haar on the circles of the block is a product of a bounded number of factors phi_beta, smooth and bounded above and below by positive constants at fixed beta. So transport fields exist (Lemma T (i), with the circle Laplacian), Lemma P1 holds with c_1 = (pi/2) times a density factor independent of M and of the exterior (Step 1 on the circle: the mean geodesic distance of two uniform points is pi/2), Holley-Stroock from the circle gap 1 gives `c_* > 0` independent of M and of the exterior, and Lemma PE and the spectral step are unchanged. If (AN) held with margin kappa on T_M for infinitely many M, Theorem AG (c) would give `gamma_V(beta; M) >= kappa c_*/(2 n_max) > 0` along them, with c_* and n_max fixed by beta and the shape. This contradicts the full limit of Theorem V. For the second claim use Theorem AG (d) with f and g translates of the score `s_p = (log phi_beta)'((d_1 theta)_p)`, which is smooth, bounded and gauge invariant (READ lines 200-205). The bound (3.3), with constants independent of M, passes to every local limit (READ lines 219-226) and makes the score correlations absolutely summable. Section 1.3 there rules this out in every periodic local limit (READ lines 243-250). QED

**The named step.** The step that fails is the hypothesis (AN) itself: the coefficient inequality (AN2) for numbers that satisfy the annealed moment bounds (AN1). The transport fields, the tangent coupling along the stationary chain (Lemma PE), the L^1 block Poincare inequality, the block Poincare constant and the spectral step all hold verbatim for U(1). Abelian gauge invariance of the block law also holds, so Lemma T (ii) holds too.

**Mechanism (ARGUED, with one PROVED model case).** At beta >= 2^14 the Villain block law with a typical exterior is close to a Gaussian (spin-wave) law. Its covariance does not depend on the exterior, and its response to the exterior is the harmonic exit response of the photon, the same for every exterior. So averaging over exteriors gains nothing, and the failure is already at the one-point level of Lemma N. The Gaussian case is exact:

**Proposition GFF-AN (PROVED).** Take the lattice Gaussian field with energy `(1/2) sum_(x~y) (phi_x - phi_y)^2 + (m^2/2) sum_x phi_x^2`, m >= 0, any finite family of site blocks, and any transport fields (defined by (2.1) with real fibres). Then `mu(R^a_yx) >= H_a(x, y)`, the exit distribution from B_a of the walk killed with probability `m^2/(2d + m^2)` per step. Hence if (AN1) holds with numbers k, the margin of (AN2) satisfies `kappa <= sum_(a contains x*) rho_a(x*)` for any weights w, where x* is a site where w is smallest and rho_a(x) is the probability of killing before exit. For the massless field kappa <= 0: (AN) fails for every block family, every choice of transport fields and every weights.

*Proof.* The block conditional law is Gaussian with a covariance independent of the exterior and mean `H_a phi_(boundary)` (READ `library/gap-blockcrit-opus.md` line 307). Apply (2.1) with psi = phi_x: `gamma_a(xi_x | y) = d/dt gamma_a(phi_x) = H_a(x, y)` for a unit change of the exterior value at y. So `gamma_a(|xi_x| | y) >= H_a(x, y)` for every exterior, and `mu(R^a_yx) >= H_a(x, y)`. Lemma N (i) gives `k^a_yx >= H_a(x, y)`. At x*, `sum_a sum_y w_y k^a_(y x*) >= w_(x*) sum_(a contains x*) sum_y H_a(x*, y) = w_(x*) (n_(x*) - sum_a rho_a(x*))`, using `sum_y H_a(x, y) = 1 - rho_a(x)` (READ line 307). Compare with (AN2) at x*. QED

The fibre is R here, so Theorem AG (b) does not apply as written; the proposition concerns the coefficient only, as in row 836.

**Where SU(2) could differ (ARGUED).** The only way (AN2) can have a positive margin at order one is an exterior-averaged response with positive absorption inside the block, the analogue of m > 0 in Proposition GFF-AN. For SU(2) this is expected from the mass gap at the scale of blocks larger than the correlation length; for U(1) in the Coulomb phase Theorem UA forbids it. That large-block annealed absorption is the crux in finite form, as in row 836 (READ line 289). OPEN. The U(1) Wilson cosine is not covered: its periodic gap statement (W-score) is OPEN in `library/gap-tu-retry.md` lines 495-507 (READ).

## 7. Summary, provenance and next steps

| statement | mark | where |
|---|---|---|
| Lemma T: transport fields exist (Poisson choice), are orthogonal to internal gauge orbits for vertex blocks, and give the exact response identity (2.2); Corollary T1 | PROVED (standard elliptic facts) | 2.1 |
| Condition (AN): mixed moments of the block responses along the stationary block chain bounded by numbers k that satisfy (BC-gen) with margin kappa | definition | 2.3 |
| Lemma P1: L^1 block Poincare inequality, constant (pi/2) exp(6 beta \|P_a\|), uniform in the exterior | PROVED | 3 |
| Lemma PE: path expansion of `mu(\|grad P^t f\|)` along the stationary chain (the tangent coupling) | PROVED | 3 |
| Lemma GQ and Theorem AG': gauge-quotient form, boundary gauge paid as exterior gauge jumps; gauge-invariant block and Langevin gaps | PROVED | 3.1 |
| Theorem AG: (AN) gives annealed gradient contraction, block gap kappa/2, Langevin gap kappa c_*/(2 n_max) on all functions, exponential clustering (3.3); uniform in the torus and the centre signs; no independence, no uniformity over exteriors | PROVED | 3 |
| the seed comparison (Theorem R (d) for non-dominated measures) from (AN) | OPEN | 3 |
| Lemma Q: the block variables anneal for free; the quenched-exterior criterion implies (AN) | PROVED | 4.1 |
| Theorem ST re-derived inside Theorem AG (per-link Beckmann duality) | OPEN detail | 4.1 |
| Proposition PB (Peierls form, k = kg + eps kmax), Lemma FR (fresh badness), Lemma H (Hoelder), Lemma N (necessary conditions) | PROVED | 4.2 |
| (SP-ext): a space-time Peierls bound for exterior badness along the stationary chain | OPEN (the crux of the conversion at order one) | 4.3 |
| chessboard and time-reflection suppliers for (SP-ext) | ARGUED (literature recalled, not read) | 4.3 |
| Proposition CEIL does not bound (AN) | PROVED | 4.3 |
| Theorem LW: Lyapunov-weighted quenched criterion gives the block and Langevin gaps | PROVED | 4.4 |
| local weights cannot pay amplifying bad clusters | ARGUED | 4.4 |
| beta window: (AN) at small beta; small blocks plausibly up to about beta 1, not at beta 2; order one needs blocks larger than xi | ARGUED / GUIDE | 5 |
| row 832 calibration excludes (AN) for gauge-variant link blocks at every tested beta (if normalized as in Lemma N (iii)) | ARGUED from GUIDE | 5 |
| Theorem UA: periodic Villain U(1) at beta >= 2^14 fails (AN) for every block shape and every choice of transport fields, for all large tori | PROVED from Theorem V (READ, checked by row 794) | 6 |
| Proposition GFF-AN: Gaussian field, annealed responses at least the exit distribution; margin at most the killing mass, so at most 0 when massless | PROVED | 6 |
| the U(1) failure is already at the one-point level (spin waves) | ARGUED | 6 |

**The coupling, in one paragraph (ARGUED).** The block disagreement coupling of this note is infinitesimal. Two copies differ by a tangent vector at one link. Each block update moves the difference into the block with the random weight R, evaluated on the stationary copy. The environment is therefore the Wilson configuration itself, with law mu at every time. Linearity of expectation and the Markov property replace the independence that the quenched theories need (row 821). The L^1 block Poincare inequality and a spectral argument turn the averaged contraction into a gap. What remains is to show that the averaged products of responses along the chain stay small, which is a space-time statement about bad exteriors.

**Provenance and credits.** One author, Claude Opus 5.5 at max effort, by hand in one session; this is not a check. Reused results: Lemma G, (BC-gen), Lemma SYM, Theorem R, Theorem ST, Proposition CEIL, Theorem U and Proposition GFF of `library/gap-blockcrit-opus.md` (Claude Opus 5.5, row 836; not yet checked, check queued as row 841); Theorem V for periodic Villain, Lemma L and the score nonsummability of `library/gap-tu-retry.md` (Codex gpt-6-astra, row 786; checked by Claude Opus 5.5, row 794), whose covariance method is credited there to Jurg Frohlich and Thomas Spencer; the literature map of `library/prior/gap-lit-dp.md` (Codex gpt-6-luna, row 821), which reports Gielis and Maes, van den Berg and Maes, and Georgii, Haggstrom and Maes; the GUIDE runs of rows 820 and 832 (Claude Opus 5.5, the lead, on the Mac mini). Recalled, not read in this session: the Holley-Stroock perturbation lemma; the Helffer-Sjostrand style representation of covariances by a Poisson equation, behind the transport field of Lemma T; the device of running a coupling along a stationary copy, as in the "coupling with the stationary distribution" of Hayes and Vigoda; Lyapunov-weighted contraction metrics, as in work of Hairer and Mattingly; Kantorovich-Rubinstein and Beckmann duality; chessboard estimates of Frohlich, Israel, Lieb and Simon; reflection positivity of the Wilson action by Osterwalder and Seiler. Novelty is not established: no outside literature search was run for this note, and annealed or stationary-coupling contraction criteria are likely to have precedents in the Markov-chain literature.

**Next steps for the lead (ARGUED).** (1) A cross-provider check of Lemma T, Lemma P1, Lemma PE, Theorem AG, Lemma Q, Proposition PB, Theorem LW, Theorem UA and Proposition GFF-AN; the points that most need it are the spectral step from L^1 decay in Theorem AG (b), the evaluation of R at the updated configuration in Lemma PE, and the regularity of the Poisson field. (2) A literature reading row (owner rule of 2026-11-12) on annealed or stationary-coupling contraction, Lyapunov-weighted Dobrushin criteria, and space-time Peierls bounds for heat-bath dynamics. (3) Optimal gauge corrections zeta for explicit vertex and link blocks in Theorem AG', so that invariant typical responses can be used. (4) The exact crux input (SP-ext), or its cluster form. (5) A GUIDE run, deciding nothing, on vertex blocks: the one-point per-link totals `sum_j mu(R_jc)` at beta 0.5, 1 and 2, and the autocorrelation in heat-bath time of exterior badness (the persistence that (P3) must control).

This note is an author proof by one model. It is not an independent check and not an audit.

RESULT: PROVED a conversion theorem for 4D Wilson SU(2) (Theorem AG): the exact annealed condition (AN), that mixed moments of the block linear-response fields along the stationary block heat-bath chain are bounded by numbers k satisfying (BC-gen) with margin kappa, implies a block gap kappa/2, a Langevin gap kappa c_*/(2 n_max) on all functions and exponential clustering, uniform in the torus and flux sectors, with no independence and no uniformity over exteriors (a tangent coupling along the stationary chain plus an L^1 block Poincare inequality and a spectral step); PROVED that the block variables anneal for free (Lemma Q), a Peierls form (Proposition PB: k = kg + eps kmax under a space-time bad-set bound), fresh badness (Lemma FR), a Lyapunov-weight variant (Theorem LW) and necessary conditions (Lemma N); PROVED a gauge-quotient form (Theorem AG') with the boundary gauge paid as exterior gauge jumps; OPEN: the space-time Peierls bound for exterior badness (SP-ext), which the persistence of bad exteriors makes the crux of the conversion, plus explicit numbers for any block and the seed comparison; GUIDE orientation (row 832): small blocks could satisfy (AN) up to about beta 1, not at beta 2, where blocks larger than the correlation length are needed, and, for Theorem AG without gauge corrections, gauge-variant link blocks fail at every tested beta if the calibration is normalized as in Lemma N; periodic Villain U(1) at beta >= 2^14 fails (AN) for every block shape and every choice of transport fields at the coefficient step (Theorem UA, from Theorem V), and the massless Gaussian field has margin at most 0 for every block family (Proposition GFF-AN).
