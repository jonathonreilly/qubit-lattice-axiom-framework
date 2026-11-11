lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T16:40Z

# gap-zf-box-s: harmonic measure of the scaling domain (Z5) and scaling for boxes (Z7)

Queue row 680. Pinned commit dcb15d3d2. Brief: Item 2 of Part 4 of `library/gap-skeleton-max-b.md`, lines 542-548. Research-stage working state; nothing here grants status. Written in steps; each step is appended before the next is thought through.

## Step 0. Started 2026-11-11T04:40Z

Reading: the brief, sections 1.7, 2.4, 2.5 of `library/gap-skeleton-max-b.md`, `library/gap-skeleton-final.md` (nodes Z5, Z7), the account lines named in the brief. Nothing proved yet.

## 1. Repo search, duplicate check, sources (done 04:40-05:10Z)

- **Duplicate check.** `library/open-core.md` and `library/open-registry.md` have no hit for harmonic measure, (HM), N5, Z5, Z7, dominant eigenvalue, Vesentini or Beraha. In the FINISH rows, nodes Z5 and Z7 are owned only by row 680 (this row). Row 677 owns Z6, row 681 owns the transport check, row 683 owns (SC_B). No row attacks what is proved below.
- **Read in full for this item.** `library/gap-skeleton-max-b.md` sections 1.7, 1.9, 2.5, 3.1, Part 4 Item 2. `library/gap-skeleton-final.md` 4.2 and 12. `library/gap-zero-transport-check.md` 3.2-3.6, 4, 9, 10 (corrected Theorem ZB, Lemma S, the lens, (TM_B)). `library/gap-sc-box.md` Section 1 (Theorem SC: r_0 = 1/51200, C_0 = 1/100, kappa_0 = 4 log 2).
- **The account.** `YM4_1400.tex` of the Sussman-Alpoge repository, commit 2bc0658f91d2 (Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text), fetched by URL into my scratch folder. Lines read: 1650-1690 (first passage, the dilation identity, frozen couplings), 1738-1756 (Theorem `thm:continuum-main`, clause (a)), 1822-1836 (clause (d)), 2250-2264 (technical statement B3), 1919-1925.
- **What the account gives for the scale function.** a_K = L^{-K}, K = K(beta, g) the first-passage count (1660-1664). Clause (a), 1751: "beta / log(1/a_K) -> 11 N^2/(12 pi^2) uniformly on W_K(g)". Statement B3, 2254-2263: the increments are b_j = b_j^0 + f_j + q_j with |b_j^0 - c_0| <= C L^{-sigma j} and |f_j| <= C x_{j-1}^{-1/2} (log x_{j-1})^p. The error f_j is not summable over the flow. **So the account fixes a(beta) only up to a factor exp(O(beta^{1/2} polylog beta)). It has no two-loop form.** The brief's phrase "the scale function of the account with its two-loop form" names something the account does not contain. Section 2 states what is needed as the input (2L).
- **Two-loop exponent (literature, recalled, not read; credit Caswell 1974, Jones 1974).** With beta = 4/g^2 for SU(2), b_0 = 11N/(48 pi^2), b_1 = 34 N^2/(3 (16 pi^2)^2): a(beta) Lambda = C beta^{p} exp(-c_a beta)(1 + O(1/beta)), c_a = 12 pi^2/(11 N^2) = 3 pi^2/11, p = b_1/(2 b_0^2) = 51/121. Hand arithmetic: (34/3)(48^2/256)/(2 * 121) = (34/3)(9)/242 = 51/121. Nothing below depends on the value of p in [0, 1).

## 2. Part (i): the harmonic-measure bound (node Z5). PROVED, for the model scale function; not checked by another model

Kind of result: proof of a step that the plan leaves open (N5). Proved by Claude Fable 5.2 (medium). Inputs: only the maximum principle and the definitions of the check `library/gap-zero-transport-check.md` (Section 2 there: omega is the Perron solution; monotone in the domain).

### 2.1 The scale function and its region

Fix c > 0 and p in [0, 1). (For SU(2): c = c_a = 3 pi^2/11 = 2.69..., p = 51/121.) Put kappa = c/4 and x_* = max(1, 4p/c). On the half-plane P = {Re beta > x_*} define, with the principal logarithm,
  phi(beta) = c beta - p Log beta,  F = exp(-phi) = beta^p e^{-c beta},
  phi~(beta) = phi(beta) - kappa/beta,  F~ = exp(-phi~) = F e^{kappa/beta}.
Both phi and phi~ are analytic on P and real on the real axis. Write psi for either.

(F0) Re psi' >= c/2 on P, and |psi' - c| <= c/2. Proof: psi' - c is -p/beta or -p/beta + kappa/beta^2, and p/|beta| <= c/4, kappa/|beta|^2 <= c/4 on P.

(F1) By Cauchy-Riemann, d/dx Re psi = d/dy Im psi = Re psi' >= c/2, and |d/dy Re psi| = |d/dx Im psi| = |Im psi'| <= c/2. So on P: for fixed y, x -> Re psi(x + iy) is strictly increasing with slope >= c/2. For fixed x, y -> Im psi(x + iy) is odd, strictly increasing, with slope >= c/2.

(F2) Hence for each x > x_* there is a unique Y_psi(x) > 0 with Im psi(x + i Y_psi(x)) = pi/2, and |Im psi(x + iy)| < pi/2 exactly for |y| < Y_psi(x). Also Y_psi(x) <= W := pi/c. Y_psi is C^1 (implicit function theorem) with |Y_psi'| = |Im psi'|/Re psi' <= 1.

(F3) Y_phi~(x) < Y_phi(x). Proof: for y > 0, Im phi~ = Im phi + kappa y/|beta|^2 > Im phi. So Im phi(x + i Y_phi~(x)) < pi/2, and (F1) gives the claim.

(F4) For phi: c Y(x) = pi/2 + p arctan(Y(x)/x), so pi/(2c) < Y(x) <= pi/(2(c - p/x)), Y is non-increasing, and Y(x) -> pi/(2c) as x -> infinity. For SU(2), pi/(2 c_a) = 11/(6 pi) = 0.5836. Write Y = Y_phi from now on.

The scaling region is S(x_1) = {x + iy: x > x_1, |y| < Y(x)} for x_1 >= x_*. It is the set of beta with Re beta > x_1 between the two curves on which F is imaginary: on the curve y = +-Y(x), arg F = -+pi/2. This is the region of the brief with the two-loop model F in place of "the continuation of a(beta)".

**Input (2L) (named; an input from node Z0, not proved here and not in the account, see Section 1).** There are C_2 and beta_1 >= x_* with a(beta) <= C_2 beta^p e^{-c beta} for all real beta >= beta_1, where a(beta) = L^{-K(beta, g)}.
Only this upper bound on a is used. If (2L) holds for some p, it holds for every larger p (beta >= 1).

### 2.2 Lemma A (comparison in a curvilinear rectangle)

Let psi be phi or phi~. For xi_0 < xi_1 put
  R = R_psi(xi_0, xi_1) = {beta in P: |Im psi(beta)| < pi/2, xi_0 < Re psi(beta) < xi_1},
  A(xi) = {beta in P: |Im psi(beta)| <= pi/2, Re psi(beta) = xi}.
Let Omega be an open set in the plane and omega a positive harmonic function on Omega. Assume
 (a) the closure of R is a compact subset of P and of Omega;
 (b) xi_1 - xi_0 >= log 2.
Put eps_1 = min of omega over A(xi_0) (positive: A(xi_0) is a compact subset of Omega). Then for every real x in R with psi(x) <= xi_1 - log 2:
  omega(x) >= (eps_1/2) e^{xi_0} e^{-psi(x)}.

Proof. Put q = exp(-(psi - xi_0)), analytic on P, and t = exp(-(xi_1 - xi_0)) <= 1/2. On R: t < |q| < 1 and Re q > 0. Define
  H = (4/pi) Re arctan(q) - (16 t^2/(3 pi)) Re(1/q).
1. arctan is analytic on the unit disc and arctan(q) = (1/2i) Log M(q), M(q) = (1 + iq)/(1 - iq) (both vanish at 0 and have derivative 1/(1 + q^2)). Re M = (1 - |q|^2)/|1 - iq|^2 > 0 on the disc. So Re arctan(q) = (1/2) Arg M(q) lies in (-pi/4, pi/4). Hence H is harmonic on R, and H <= 1 on R because Re(1/q) = Re q/|q|^2 > 0 there. Also H >= -1 - 16t/(3 pi). So H is bounded.
2. The boundary of R lies in A(xi_0) union A(xi_1) union {|Im psi| = pi/2, xi_0 <= Re psi <= xi_1}: a boundary point lies in P by (a), satisfies the non-strict inequalities by continuity, and at least one equality holds because R is open. H extends continuously to the closure of R except at the two corner points where q = +-i.
3. Sides (|Im psi| = pi/2, so q = i tau with |tau| <= 1, tau != +-1): arctan(i tau) = i artanh(tau), so Re arctan(q) = 0; and Re(1/q) = 0. So H = 0.
4. Exit arc A(xi_1) (|q| = t, Re q >= 0): for q = s + i tau, s >= 0, arctan(q) - arctan(i tau) = int_0^s d sigma/(1 + (sigma + i tau)^2), and |1 + w^2| >= 1 - |w|^2 >= 3/4 for |w| <= 1/2. So Re arctan(q) <= (4/3) s = (4/3) Re q = (4/3) t^2 Re(1/q). So H <= 0.
5. Entry arc A(xi_0), corners excluded: limsup H <= 1 by step 1.
6. v = eps_1 H - omega is harmonic and bounded on R. At every boundary point except the two corners, limsup v <= 0: on the sides v = -omega <= 0, on the exit arc v <= -omega <= 0, on the entry arc v <= eps_1 - omega <= 0. A bounded harmonic function on a bounded open set with limsup <= 0 at all boundary points except finitely many is <= 0 (add eta sum_j log(|z - p_j|/diam) and let eta -> 0; this is the form used in the check, 3.5 step 3). So omega >= eps_1 H on R.
7. At a real x in R, q = e^{-(psi(x) - xi_0)} is real, t < q < 1. arctan q >= (pi/4) q on [0, 1] (concavity). So H(x) >= q - (16/(3 pi)) t^2/q = q (1 - (16/(3 pi)) (t/q)^2) >= q/2 when q >= 2t, since 16/(12 pi) < 1/2. The condition q >= 2t is psi(x) <= xi_1 - log 2. QED.

Remark (what the lemma is). In the coordinate zeta = psi(beta) the set R is the rectangle (xi_0, xi_1) x (-pi/2, pi/2), and (4/pi) Re arctan(e^{-(zeta - xi_0)}) is the function of Lemma HM (plan 1.7) for half-width pi/2. The proof does not use that psi is one-to-one; it only uses that H is a harmonic function of beta.

### 2.3 The domain: a Lipschitz lens inside the brief's domain

Parameters: r_0 > 0 (strong-coupling radius), w_0 > 0 (half-width of the tube over [r_0, beta_1]), beta_1 >= x_*, with
  max(w_0, 5 r_0/4) < pi/(2c).   (For SU(2): w_0 <= 1/2, r_0 <= 2/5 suffice. Theorem SC has r_0 = 1/51200.)
For X > beta_1 + 4 put, with med the middle one of three numbers and (s)_+ = max(s, 0),
  tau(x) = med{ w_0, 5 r_0/4 - 2 (x - r_0)_+, 5 r_0/4 + 2 (x - r_0)_+ } + 2 (x - beta_1)_+,
  h_X(x) = min{ 2 (x + 2 r_0), tau(x), X - x }            for -2 r_0 < x < beta_1,
  h_X(x) = min{ tau(x), Y(x), X - x }                      for beta_1 <= x < X,
  D_X = {x + iy: -2 r_0 < x < X, |y| < h_X(x)}.
In words: the strong-coupling disc is covered by a cap of half-height 5 r_0/4; the tube has half-width w_0 over [r_0, beta_1] (reached from the cap by a ramp of slope 2); from beta_1 the tube opens with slope 2 until it meets the curve y = Y(x); it then follows the curve; a wedge of slope 1 closes it at X.

Lemma B. D_X is a Lipschitz lens in the sense of the check (3.2) with Lambda = 2. So it satisfies every shape hypothesis of the corrected Theorem ZB (3.6 there): bounded, simply connected, symmetric, contains |beta| <= r_0, [0, X) in D_X, D_X in {Re beta < X}, its part in Re beta <= 0 lies in |beta| < 2 r_0, D_X intersected with {|beta| < 2 r_0} is connected, (TUBE') with theta = 1/sqrt 5. Also D_X is contained in D_X' for X <= X', and D_X is contained in the brief's domain (cap, tube, region between the curves) as soon as that domain's tube has half-width at least max(w_0, 5 r_0/4) near r_0.
Proof. Each function in the minima is 2-Lipschitz ((F2) for Y; a median of 2-Lipschitz functions is 2-Lipschitz). h_X is continuous at beta_1 because tau(beta_1) <= max(w_0, 5 r_0/4) < pi/(2c) < Y(beta_1), so Y is not the minimum near beta_1. h_X > 0, and h_X -> 0 at both ends. For x <= r_0, tau = 5 r_0/4, so h_X = min{2(x + 2 r_0), 5 r_0/4}. With s = x + 2 r_0: for x <= 0, 2s < sqrt(4 r_0 s - s^2) = sqrt(4 r_0^2 - x^2) when s < 4 r_0/5, and the ramp reaches 5 r_0/4 at s = 5 r_0/8 < 4 r_0/5; for s >= 5 r_0/8 and x <= 0, 5 r_0/4 < sqrt(4 r_0^2 - x^2) because |x| <= 11 r_0/8 < 1.56 r_0. On [-r_0, r_0], s >= r_0, so h_X = 5 r_0/4 > sqrt(r_0^2 - x^2). Monotone in X: clear. QED.

D'_X = {beta in D_X: Re beta > 0, |beta| > r_0} is connected (from any point move right at constant y to Re beta slightly above r_0 if needed, then vertically to the real axis; h_X = 5 r_0/4 on (0, r_0] allows the first move). omega_X denotes the harmonic measure of the arc {|beta| = r_0, Re beta >= 0} in D'_X, as in the corrected Theorem ZB. It is positive on D'_X (it is not identically zero and D'_X is connected) and non-decreasing in X (check, Section 2).

### 2.4 Theorem HM-s (node Z5 for the model scale function)

Let c, p, r_0, w_0, beta_1 be as above and D_X the lens of 2.3. There are eps > 0, s > 0 and X_0, depending on (c, p, r_0, w_0, beta_1) only, such that for every X >= X_0 and every real beta in [beta_1, X - s]:
  omega_X(beta) >= eps beta^p e^{-c beta}.
With input (2L): omega_X(beta) >= (eps/C_2) a(beta) on the same range.

Proof. Work with psi = phi~. Constants, in order:
 x_2 = beta_1 + W/2 (for x >= x_2 the ramp is above the curve: tau(x) >= 2(x - beta_1) >= W >= Y(x));
 xi_0 = 1 + max{Re phi~(x_2 + iy): |y| <= W};
 C_4 = W c/2 (so |Re phi~(x + iy) - phi~(x)| <= C_4 for |y| <= W, by (F1));
 x_3 = the real solution of phi~(x_3) = xi_0 (unique, x_3 > x_2, by (F1));
 X_0 = x_3 + 2 C_4/c + W + 1 + (2/c) log 2;   s = W + 1 + 2 (C_4 + log 2)/c.
For X >= X_0 put xi_1 = phi~(X - W - 1) - C_4, and R = R_phi~(xi_0, xi_1).
1. xi_1 - xi_0 >= log 2: phi~(X - W - 1) - phi~(x_3) >= (c/2)(X_0 - W - 1 - x_3) = C_4 + log 2.
2. The closure of R lies in {x_2 < x <= X - W - 1, |y| <= Y_phi~(x)}. Indeed on the closure |Im phi~| <= pi/2, so |y| <= Y_phi~(x) <= W. If x <= x_2 then Re phi~(x + iy) <= Re phi~(x_2 + iy) <= xi_0 - 1 by (F1), against Re phi~ >= xi_0. And phi~(x) - C_4 <= Re phi~(x + iy) <= xi_1 = phi~(X - W - 1) - C_4 gives x <= X - W - 1. So the closure is compact in P.
3. The closure of R lies in D'_X: for x_2 < x <= X - W - 1 and |y| <= Y_phi~(x) we have |y| < Y(x) by (F3), |y| < tau(x) by the choice of x_2, and |y| <= W < X - x. So |y| < h_X(x). Also Re beta > x_2 > r_0.
4. The entry arc A(xi_0) lies in D'_{X_0} by the same argument (its points have x <= x_3 + 2 C_4/c). Put eps_1 = min of omega_{X_0} over A(xi_0) > 0. For X >= X_0, omega_X >= omega_{X_0} >= eps_1 on A(xi_0).
5. Lemma A with Omega = D'_X, omega = omega_X: for real x with xi_0 < phi~(x) <= xi_1 - log 2, omega_X(x) >= (eps_1/2) e^{xi_0} F~(x) >= (eps_1/2) e^{xi_0} F(x), since F~ = F e^{kappa/x} >= F on the real axis. The condition holds for x_3 < x <= X - s: phi~(x) <= phi~(X - W - 1) - (c/2)(s - W - 1) = xi_1 - log 2.
6. On [beta_1, x_3]: put eps_2 = min of omega_{X_0} over [beta_1, x_3] > 0 (a compact subset of D'_{X_0}) and F_max = max of F over [beta_1, x_3]. Then omega_X >= eps_2 >= (eps_2/F_max) F there.
Take eps = min{(eps_1/2) e^{xi_0}, eps_2/F_max}. QED.

Remarks.
1. **The constants eps_1 and eps_2 are defined by an existence argument** (the minimum of a positive continuous function on a compact set). They depend on the tube over [r_0, beta_1] through the harmonic measure of D_{X_0}. Lemma HM (plan 1.7) and Harnack chains would make them explicit; no consumer needs that.
2. **Corollary 5' (check, Section 4) now has its harmonic-measure input** in the form it asks for: a family D_X of lenses, the same r_0, and omega_{D_X}(beta) >= eps' a(beta) on [beta_1, X - s], given (2L).
3. **Robust form (Lemma A is the tool).** Let psi be any function analytic on P, real on the real axis, with Re psi' >= c/2 and |psi' - c| <= c/2. Then (F1), (F2) hold for psi, and the proof of 2.4 gives: if a lens D_X follows the curve y = Y_psi^(x) of some psi^ with Y_psi < Y_psi^, then omega_X(beta) >= eps e^{-psi(beta)} on [beta_1, X - s]. Example: psi = phi + kappa'/beta for any kappa' in [-c/4, c/4]; its region differs from S by an angle of order |Im beta|/|beta|^2. So a correction factor 1 + O(1/beta) in the scale function, real on the real axis, moves the curves and changes only eps. A change of p changes the answer by a power of beta: for the region of beta^{p'} e^{-c beta} the bound is eps beta^{p'} e^{-c beta}.
4. **What it does not show.** It does not show that the lattice theory is zero-free, or has a dominant eigenvalue, in S. It does not show (2L). It is a statement about harmonic functions in an explicit domain.
5. Sharpness (expected, not proved, not used): in the coordinate zeta = phi(beta) the function Re F = e^{-Re zeta} cos(Im zeta) is positive harmonic in S and vanishes on the sides. So I expect that no domain inside S has harmonic measure larger than a constant times F on the real axis far to the right, that is, that the exponent is exact. A proof needs a comparison at the corners of a cross-cut (a boundary Harnack inequality), which I did not write.

**Standing after Step 1 (05:25Z).** Part (i) is proved as Theorem HM-s, given the input (2L), which the account does not contain. Next: part (ii).

## 3. Part (ii), first half: dominance replaces zero-freeness (node Z7). PROVED here; not checked by another model

Kind of result: a correction of the plan's node Z7, and proofs of the steps that the correction needs. Proved by Claude Fable 5.2 (medium).

**Summary of this section.** (1) The literal statement (ZF_B-s), "no zeros of Z(k, B; beta) in the whole scaling region for all k >= k_0(B)", does not follow from positivity of the real parts of the levels, and it is expected to be false: Example 3.8. Zeros of Z(k, B; .) sit at distance of order 1/k from the side curves, inside the region. (2) The transport does not need it. Theorem V (3.6) gives m_B >= kappa_0 omega_D from **dominance**: the continued transfer operator has a simple eigenvalue that is strictly largest in modulus. (3) Zero-freeness on a lens implies dominance there (Proposition D, 3.5), so the crux node Z6 keeps its form. (4) Dominance in the scaling region is exactly the inequality of the brief for the levels (Section 4).

### 3.1 The transfer operator at complex coupling, (TM_B-c)

Setting and notation of the check, Section 9: X_B = G^{E_B}, H_B = L^2(X_B), V_B, K_B, the gauge average P, T_B = P T P. For complex beta define T_B(beta) by the same formulas.

(c1) beta -> T_B(beta) is an entire function with values in the trace class of H_B.
(c2) Tr T_B(beta)^k = Z(k, B; beta) for every complex beta and every k >= 2.
(c3) For real beta > 0, T_B(beta) is the operator of (TM_B).

Proof. (c3) is the definition. (c1): by the expansion used in the check (Section 9, step 3; row 667, 2.2), K_B(u, v) = e^{-beta |E_B|} sum_n ((beta/2)^n/n!) (sum_l tr(u_l v_l^{-1}))^n, and sum_l tr(u_l v_l^*) = sum_{i in I} iota_i(u) conj(iota_i(v)) with sum_i |iota_i(u)|^2 = 2 |E_B|. So the operator Q_n with kernel (sum_l tr(u_l v_l^{-1}))^n is a sum of rank-one operators |f_J><f_J|, J in I^n, with sum_J ||f_J||^2 = (2|E_B|)^n. It is positive with trace (2|E_B|)^n. The series e^{-beta |E_B|} sum_n ((beta/2)^n/n!) Q_n converges in trace norm, locally uniformly in beta (sum_n |beta|^n |E_B|^n/n! = e^{|beta||E_B|}). So the operator of kernel K_B is entire in trace norm. Multiplication by e^{-V_B/2} = exp(-(beta/2) sum_p a_p) is entire in operator norm. P does not depend on beta. A product of an entire trace-class function with entire bounded functions is entire in trace norm. (c2): both sides are entire in beta (the trace is continuous on the trace class) and they agree for real beta > 0 by (TM_B)(c). QED.
Standing: I read the check's Section 9, not row 667's step 2.2 itself. The expansion is quoted from the check.

**Cited input (FD), classical, recalled, not rebuilt (Fredholm; Grothendieck; Simon, Trace Ideals, Chapter 3).** For a trace-class operator A on a Hilbert space, d(w) = det(1 - wA) is entire. Its zeros are the points w = 1/nu, nu a nonzero eigenvalue of A, and the order of the zero is the algebraic multiplicity of nu. For small |w|, -w d'(w)/d(w) = sum_{m>=1} w^m Tr A^m. Also (Riesz): the nonzero spectrum of a compact operator consists of isolated eigenvalues of finite algebraic multiplicity, and the algebraic multiplicity of nu != 0 for A = T^{k_0} is the sum of the algebraic multiplicities of the eigenvalues lambda of T with lambda^{k_0} = nu.
Label: unchecked citation. It is the only citation in Section 3 that carries weight. It replaces the plan's citation of Beraha, Kahane and Weiss, which is not used.

### 3.2 Dominance

**Definition (DOM).** A compact operator T satisfies (DOM) if it has an eigenvalue lambda_0 != 0 of algebraic multiplicity one, and every other point of its spectrum has modulus < |lambda_0|. Then rho(T) := max{|lambda|/|lambda_0|: lambda in spec T, lambda != lambda_0} < 1 (the maximum exists because the nonzero spectrum is discrete), and m(T) := -log rho(T) in (0, infinity]. For T = T_B(beta) write rho_B(beta), m_B(beta). For real beta > 0, (TM_B)(d),(e) give (DOM), and m_B(beta) is the gap log(lambda_0/lambda_1) of the plan.

**(DOM_B) on a set U:** T_B(beta) satisfies (DOM) for every beta in U.

### 3.3 Lemma G (from winding bounds to dominance)

Let T be trace class, k_0 >= 1, 0 < vartheta < 1. Assume that for every m >= 1, Tr T^{k_0 m} != 0 and has a logarithm L_m such that, for all m, q >= 1,
  |L_m - (1/q) L_{mq}| <= eps_m,  with limsup_m eps_m^{1/m} <= vartheta^{k_0}.
Then T satisfies (DOM) and rho(T) <= vartheta.

Proof. 1. Put l_m = L_m/m. Then |l_m - l_{mq}| <= eps_m/m. For j <= j', j'! is a multiple of j!, so |l_{j!} - l_{j'!}| <= eps_{j!}/j! -> 0: the sequence l_{j!} converges, to Lambda say. For every m and j >= m, j! is a multiple of m, so |l_m - l_{j!}| <= eps_m/m; hence |l_m - Lambda| <= eps_m/m.
2. So Tr T^{k_0 m} = e^{m Lambda}(1 + eta_m) with |eta_m| <= e^{eps_m} - 1, and limsup |eta_m|^{1/m} <= vartheta^{k_0}.
3. Put A = T^{k_0}, d(w) = det(1 - wA), and G(w) = -w d'(w)/d(w). By (FD), G is meromorphic in the plane; its poles are the points 1/nu, they are simple, and the residue at w_0 = 1/nu is -w_0 times the algebraic multiplicity of nu. Near 0, G(w) = sum_m w^m Tr A^m = e^{Lambda} w/(1 - e^{Lambda} w) + sum_m eta_m (e^{Lambda} w)^m. The last series is analytic in |w| < |e^{-Lambda}| vartheta^{-k_0}. The first term has one pole, at w_0 = e^{-Lambda}, simple, with residue -w_0.
4. By uniqueness of the meromorphic continuation, in the disc |w| < |e^{-Lambda}| vartheta^{-k_0} the function G has exactly one pole, w_0 = e^{-Lambda}, and the multiplicity there is 1. So A has the eigenvalue nu_0 = e^{Lambda} with algebraic multiplicity one, and every other nonzero eigenvalue nu of A has |nu| <= |nu_0| vartheta^{k_0}.
5. By (FD), last sentence: exactly one eigenvalue lambda_0 of T has lambda_0^{k_0} = nu_0, it has algebraic multiplicity one, and every other eigenvalue has |lambda| <= |lambda_0| vartheta. QED.

### 3.4 Proposition C (the strong-coupling disc)

For every finite B with free walls and every complex beta with 0 < |beta| < R = 1/12800: T_B(beta) satisfies (DOM) and rho_B(beta) <= (12800 |beta|)^4. In particular m_B(beta) >= kappa_0 = 4 log 2 for |beta| <= 2 r_0 = R/2. (At beta = 0, T_B is the rank-one projection on constants.)
Proof. Theorem SC of `library/gap-sc-box.md` (Opus 5.5; its check is row 694, not read by me): Z(k, B; beta) != 0 and |log Z(k) - (1/q) log Z(qk)| <= (|B| k/100)(12800 |beta|)^{4k} for k >= 3, q >= 1, with the branch that vanishes at beta = 0. Apply Lemma G with k_0 = 3, L_m = log Z(3m, B; beta), eps_m = (3 |B| m/100)(12800|beta|)^{12 m}, vartheta = (12800 |beta|)^4, and (c2). QED.
Inherits: Theorem SC (unchecked by me).

### 3.5 Proposition D (zero-freeness on a lens implies dominance; the complex form of Theorem ZB)

Assume the hypotheses of the corrected Theorem ZB (check, 3.6) for a box B on a domain D: the shape conditions, (TM_B), (SC_B), and (ZF_B): Z(k, B; beta) != 0 for beta in D, k >= k_0. Then for **every complex** beta in D' = {beta in D: Re beta > 0, |beta| > r_0}: T_B(beta) satisfies (DOM) and m_B(beta) >= kappa_0 omega_D(beta).
Proof. The check's proof (3.4, step 2) shows, for every k >= k_0, every q >= 1 and every beta in D_k = {beta in D': d(beta) > 1/k}: |g_q(beta)| <= E_k(beta) := max(M_k, 1) max(C_0 |B| k, 1) exp(-kappa_0 omega_k(beta) k), where g_q = log Z(k) - (1/q) log Z(qk) with the branches on D, M_k is polynomial in k, and omega_k increases to omega_D (3.5 there; that argument is pointwise on D'). The check then restricts to real beta. Instead, fix a complex beta in D' with omega_D(beta) > 0 (every beta in D' when D' is connected, as for a lens; at a point with omega_D(beta) = 0 the proposition claims nothing). Choose m_0 with d(beta) > 1/(k_0 m_0). Apply Lemma G with k_0 m_0 in place of k_0, L_m = the D-branch of log Z(k_0 m_0 m, B; beta), eps_m = E_{k_0 m_0 m}(beta), and (c2). Then limsup eps_m^{1/m} = exp(-kappa_0 omega_D(beta) k_0 m_0) < 1, so rho_B(beta) <= exp(-kappa_0 omega_D(beta)). QED.
Meaning: this is the direction "no zeros implies a strictly dominant eigenvalue" that the plan cites from memory (Beraha-Kahane-Weiss), with a rate. It rests on the check's bound, which I read and did not re-derive.

### 3.6 Lemma V and Theorem V (transport from dominance)

**Lemma V (Vesentini 1968; rebuilt here).** Let Omega be open in the plane and N an analytic function on Omega with values in the bounded operators of a Hilbert space. Then u(beta) = log r(N(beta)), r the spectral radius, is subharmonic on Omega: it is upper semicontinuous with values in [-infinity, infinity) and u(beta_0) <= (1/2 pi) int_0^{2 pi} u(beta_0 + r e^{it}) dt for every closed disc in Omega.
Proof. 1. For unit vectors f, g and n >= 1, beta -> <f, N(beta)^n g> is analytic, so its log-modulus has the sub-mean-value property. ||N(beta)^n|| is the supremum of these moduli over f, g, and it is continuous in beta. A supremum of functions with the sub-mean-value property has it, when the supremum is continuous. So log ||N^n|| is subharmonic and continuous into [-infinity, infinity).
2. u_j = 2^{-j} log ||N^{2^j}|| is non-increasing in j, because ||A^2|| <= ||A||^2, and u_j -> log r(N) by the spectral radius formula.
3. A non-increasing limit of continuous subharmonic functions is upper semicontinuous, and the sub-mean-value inequality passes to the limit by monotone convergence (u_1 is bounded above on the circle). QED.

**Theorem V.** Let D be a bounded connected open set that contains the closed disc |beta| <= r_0, with r_0 <= R/4 = 1/51200. Put D' = {beta in D: Re beta > 0, |beta| > r_0}, Gamma = {|beta| = r_0, Re beta >= 0}, and let omega_D be the Perron solution on D' for the boundary function 1_Gamma (the harmonic measure of the arc, as in the check). Let B be a finite box with free walls. Assume (DOM_B) on D'. Then, with kappa_0 = 4 log 2,
  m_B(beta) >= kappa_0 omega_D(beta)  for every beta in D', real or complex.
No shape condition on D is needed, and no zero-freeness of any Z(k, B; .).

Proof. 1. (lambda_0 is analytic.) Fix beta_* in D'. Let gamma be a circle about lambda_0(beta_*) whose closed disc meets spec T_B(beta_*) only in lambda_0(beta_*), and let rho' be strictly between rho_B(beta_*) and 1, with gamma outside the disc |z| <= rho' |lambda_0(beta_*)|. The set of z outside gamma with rho' |lambda_0(beta_*)| <= |z| <= ||T_B(beta_*)|| + 1 is a compact subset of the resolvent set of T_B(beta_*). T_B(.) is norm continuous (c1). By the Neumann series, for beta near beta_* this compact set and gamma stay in the resolvent set of T_B(beta), and the Riesz projection P_gamma(beta) = (1/2 pi i) oint_gamma (z - T_B(beta))^{-1} dz is analytic in beta and has rank one (projections close in norm have equal rank). So for beta near beta_*, T_B(beta) has exactly one eigenvalue inside gamma, of multiplicity one, and all other spectrum in |z| < rho' |lambda_0(beta_*)|. That eigenvalue is therefore the dominant one, lambda_0(beta) = Tr(T_B(beta) P_gamma(beta)), which is analytic, and P_0(beta) := P_gamma(beta) is its Riesz projection. So lambda_0 and P_0 are analytic on D', and lambda_0 != 0.
2. N(beta) := T_B(beta)(1 - P_0(beta))/lambda_0(beta) is analytic on D'. Its spectrum is {lambda/lambda_0(beta): lambda in spec T_B(beta), lambda != lambda_0(beta)} union {0}. So r(N(beta)) = rho_B(beta) < 1.
3. By Lemma V, u = log rho_B is subharmonic on D', and u < 0. On a component of D' where u is identically -infinity the claim holds trivially. Elsewhere s := -u/kappa_0 is superharmonic, s > 0.
4. By Proposition C, s >= 1 on D' intersected with {|beta| <= 2 r_0}. Every point of Gamma has a neighbourhood whose part in D' lies in that set. So liminf s >= 1 at every point of Gamma, and liminf s >= 0 at every other boundary point of D'. So s is in the upper Perron class of 1_Gamma on D', and omega_D <= s (the infimum of the upper class; same step as in the check's proof of Theorem LP). This is m_B = -u >= kappa_0 omega_D. QED.

Remarks.
1. Theorem V at real beta has the conclusion of Theorem ZB. Its hypothesis is different in kind: one spectral inequality at each point of D', instead of the non-vanishing of all Z(k, B; .), k >= k_0. It needs neither (TUBE'), nor Lemma S, nor the limit k -> infinity.
2. The bound is sharp in the model case (plan 1.7, last lines): if rho_B = |exp(-mu)| with mu analytic and Re mu > 0 in D, then -u = Re mu is harmonic.

### 3.7 Lemma E and Corollary 5'' (the conditional theorem in its corrected form)

**Lemma E (dominance gives zero-freeness on compact sets).** If (DOM_B) holds on an open set U and K is a compact subset of U, there is k_0(K, B) with Z(k, B; beta) != 0 for beta in K, k >= k_0.
Proof. With N as in Theorem V (its steps 1, 2 use only (DOM_B) on an open set): Z(k, B; beta) = lambda_0^k (1 + Tr N^k) for k >= 2, by (c2) and T^k = lambda_0^k P_0 + (lambda_0 N)^k. The function u = log r(N) is upper semicontinuous and < 0, so u <= -2 delta on K for some delta > 0. The functions u_j of Lemma V are continuous and decrease to u. The compact sets K_j = {beta in K: u_j(beta) >= -delta} decrease and have empty intersection, so K_j is empty for some j = j_0. Then ||N^{2^{j_0}}|| <= e^{-delta 2^{j_0}} on K, so ||N^k|| <= C e^{-delta k} on K with C = max over K and over i < 2^{j_0} of e^{delta i} ||N^i||. Finally |Tr N^k| <= ||N||_1 ||N^{k-1}|| -> 0 uniformly on K (the trace norm of N is continuous in beta, hence bounded on K). QED.

**Corollary 5'' (replaces Corollary 5' as the conditional theorem of Route Z).** Fix c, p, r_0 <= 1/51200, w_0 <= 1/2, beta_1 >= x_* as in Section 2. Let tau_0 be tau without its last term, w^ = tau_0(beta_1) (equal to w_0 once the cap ramp has ended), and let D^tube be the lens with height min{2(x + 2 r_0), tau_0(x), w^ + 2(beta_1 - x)} on (-2 r_0, beta_1 + w^/2): cap, tube of half-width w_0 over [r_0, beta_1], wedge end of slope 2 beyond beta_1. Let B be a box with free walls. Assume
 (ZF_B-x) Z(k, B; beta) != 0 for beta in D^tube and k >= k_0(B);  [node Z6]
 (DOM_B-s) T_B(beta) satisfies (DOM) for every beta in S(beta_1) = {Re beta > beta_1, |Im beta| < Y(Re beta)};  [replaces node Z7]
 (2L) a(beta) <= C_2 beta^p e^{-c beta} for real beta >= beta_1.  [input for node Z5]
Then m_B(beta) >= (kappa_0 eps/C_2) a(beta) for every real beta >= beta_1, with eps of Theorem HM-s. The constant does not depend on B. So if the hypotheses hold for all boxes with sides at least n_min, all these boxes have a gap of at least kappa_0 eps/C_2 in physical units at every beta >= beta_1.
Proof. D^tube is a Lipschitz lens with Lambda = 2 (same verification as Lemma B), so Proposition D gives (DOM_B) on (D^tube)'. For every X, the set D'_X of 2.3 lies in (D^tube)' union S(beta_1). Indeed, for x <= beta_1 the height of D_X is at most min{2(x + 2 r_0), tau_0(x)}, and this is the height of D^tube there, because tau_0 is 2-Lipschitz, so tau_0(x) <= w^ + 2(beta_1 - x). For x > beta_1 the height of D_X is at most Y(x). So (DOM_B) holds on D'_X. Apply Theorem V on D_X, then Theorem HM-s and (2L), and let X -> infinity. QED.
Note. (ZF_B-x) is asked on the lens D^tube, which ends at beta_1 + w^/2. If the crux is proved in the form (DOM_B) on a neighbourhood of the tube, Proposition D is not needed and D^tube can be any open set that contains D'_X intersected with {Re beta <= beta_1}.

### 3.8 Example: positivity of the levels does not give (ZF_B-s) as stated

Let F = beta^p e^{-c beta} and consider the family T(beta) = diag(1, e^{-F(beta)}, e^{-F(beta)}) on C^3, beta in S(x_*). It scales exactly: the two excited levels are F(beta) times the constant 1, a doubly degenerate level. Re F > 0 on S, so (DOM) holds on all of S, with gap Re F. But Tr T(beta)^k = 1 + 2 e^{-k F(beta)} vanishes where k F(beta) = log 2 + i pi (2j + 1), j an integer.
Claim: for every large X_1 and every k >= k_1(X_1) there is such a zero beta in S(x_*) with x_* + 1 <= Re beta <= X_1, for a suitable j >= 0. There Re F = (log 2)/k > 0, so the zero is inside S, at distance of order 1/(k |F(beta)|) from a side curve.
Proof. For zeta = xi - i alpha with xi >= c(x_* + 1) and |alpha| < pi/2, the map beta -> (zeta + p Log beta)/c sends the closed set {Re beta >= xi/c} into itself (there |beta| >= 1, so the real part of the image is >= xi/c) and contracts by p/(c |beta|) <= 1/4. Its fixed point solves phi(beta) = zeta, and it lies in S because |Im phi| < pi/2. It has |Im beta| <= W, so xi = c Re beta - p log|beta| >= c Re beta - p log(Re beta + W), and the right side increases with Re beta. Hence xi <= c X_1 - p log(X_1 + W) gives Re beta <= X_1. Take t_j = log 2 + i pi(2j + 1), j >= 0, and zeta = -Log(t_j/k), so xi = log(k/|t_j|) and alpha = arg t_j in (0, pi/2). The two conditions on xi say k e^{-c X_1}(X_1 + W)^p <= |t_j| <= k e^{-c(x_* + 1)}. For X_1 large this interval is non-empty, its length grows linearly in k, and |t_j| lies in [pi(2j+1), pi(2j+1) + log 2]; so for k >= k_1(X_1) some j fits. QED.
Consequences.
1. An implication "scaling and positivity of the real parts of the levels imply (ZF_B-s) on the whole region for k >= k_0" is false. This is a counterexample to the reduction of the brief **as an implication between the stated properties**. It is an abstract family, not the Wilson theory.
2. For the Wilson theory under scaling, Z(k, B; beta)/lambda_0^k is close to Theta(k F(beta)) with Theta(t) = sum_i exp(-t (E_i - E_0)), the thermal partition function of the box at complex inverse temperature t. Zeros of Theta in Re t > 0 are generic (already for 1 + w^2 + w^3 with w = e^{-e_1 t/2}, levels e_1 and 3 e_1/2: the complex roots have modulus (1.4656)^{-1/2} < 1), and Theta is almost periodic on vertical lines, so they recur with |Im t| -> infinity. Each gives zeros of Z(k, B; .) inside the region for every large k. So I expect the hypothesis (ZF_B) of Theorem ZB to fail on any domain that follows the side curves, also for the lattice theory. This expectation is not proved.
3. Nothing is lost: by Theorem V the transport needs (DOM_B), not (ZF_B). In a domain whose closure lies inside the dominance region the two agree for large k (Lemma E, Proposition D).

**Standing after Steps 2-3 (06:05Z).** Proved: (TM_B-c), Lemma G, Propositions C and D, Lemma V, Theorem V, Lemma E, Corollary 5'', Example 3.8. Open: the scaling statement and the reduction to the continuum levels (Section 4).

## 4. Part (ii), second half: scaling for boxes and the reduction to the continuum levels. PROVED as an implication from one named hypothesis; not checked by another model

### 4.0 Addendum to Section 2: Theorem HM-s for an admissible scale function

The scale function of the lattice theory, if it exists as an analytic function, is not exactly beta^p e^{-c beta}. So the hypothesis below is stated for a class of scale functions, and Theorem HM-s is needed for that class.

Definition. psi is **admissible** if it is analytic on a half-plane P = {Re beta > x_*}, x_* >= 1, real on the real axis, and |psi' - c| <= c/4 on P. Example: phi (then |phi' - c| = p/|beta| <= c/4). Example: phi + r with r analytic, real on the real axis, |r'| <= c/4 - p/|beta|; in particular phi + kappa'/beta for small |kappa'| after an increase of x_*.

For admissible psi put psi~ = psi - kappa/beta, kappa = c/4, after an increase of x_* to x_* >= 1 (so that kappa/|beta|^2 <= c/4). Then |psi~' - c| <= c/2, so (F0), (F1), (F2) of 2.1 hold for psi and psi~ with W = pi/c, and (F3) holds: Im psi~ = Im psi + kappa y/|beta|^2. In place of (F4): the slope of Im psi in y is at most 5c/4, so Y_psi(x) >= 2 pi/(5c).

**Theorem HM-s' .** Let psi be admissible, max(w_0, 5 r_0/4) < 2 pi/(5c), r_0 < beta_1, beta_1 >= x_*. Let D_X^psi be the lens of 2.3 with Y_psi in place of Y. Then Lemma B holds for D_X^psi, and there are eps > 0, s, X_0 with omega_{D_X^psi}(beta) >= eps e^{-psi(beta)} for all X >= X_0 and all real beta in [beta_1, X - s].
Proof. The proofs of Lemma B and of Theorem HM-s use only (F0)-(F3), the bound Y <= W, the inequality tau(beta_1) < Y(beta_1), and e^{-psi~(x)} = e^{-psi(x)} e^{kappa/x} >= e^{-psi(x)} for real x. They hold here. QED.
For SU(2), 2 pi/(5 c_a) = 0.467; so w_0 <= 0.46 is allowed.

**Input (2L_psi).** a(beta) <= C_2 e^{-psi(beta)} for real beta >= beta_1.

### 4.1 Lemma U (the complex size is a coordinate)

Let phi = c beta - p Log beta on P as in 2.1, and xi_* = c(x_* + 1), q_* = e^{-xi_*}. Then:
(a) phi is one-to-one on P, and F = e^{-phi} is one-to-one on S(x_*).
(b) For every q with Re q > 0 and |q| < q_* there is exactly one beta in S(x_*) with F(beta) = q; it has Re beta >= x_* + 1.
So for each integer n >= 1 the map beta -> l = n F(beta) is an analytic bijection from S^0 = {beta in S(x_*): |F(beta)| < q_*} onto the half-disc {Re l > 0, |l| < n q_*}, and arg l = -Im phi(beta). (The set S^0 lies in S(x_*) and contains S(x_1) for x_1 large; I do not need its exact shape.)
Proof. (a) P is convex and Re phi' >= c/2 on P. For a != b in P, phi(b) - phi(a) = (b - a) int_0^1 phi'(a + t(b - a)) dt, and the integral has real part >= c/2, so it is not zero. If F(beta) = F(beta') with both in S(x_*), then phi(beta) - phi(beta') is in 2 pi i Z and its imaginary part has modulus < pi, so it is zero.
(b) Put zeta = -Log q = xi - i alpha, xi > xi_*, |alpha| < pi/2. As in the proof of 3.8, beta -> (zeta + p Log beta)/c is a contraction of {Re beta >= xi/c} into itself, and its fixed point solves phi(beta) = zeta. It lies in S(x_*) since |Im phi(beta)| = |alpha| < pi/2. Uniqueness is (a). QED.
The same holds for an admissible psi with the part (b) restricted to what (a) gives: psi is one-to-one on P and F^ = e^{-psi} is one-to-one on S_psi(x_*). Only this is used below.

### 4.2 Levels and the statement of scaling

B_n is the cube {0, ..., n-1}^3 with free walls. (For a box with sides n_1, n_2, n_3 the same text holds with functions that also depend on the ratios of the sides.)

Definition (levels). If T_{B_n}(beta) has an eigenvalue lambda_0 != 0 of algebraic multiplicity one, the **levels** of the box at beta relative to lambda_0 are the numbers mu with e^{-mu} = lambda/lambda_0, lambda a nonzero eigenvalue other than lambda_0. Each is defined modulo 2 pi i. Only Re mu = -log|lambda/lambda_0| enters. (DOM) says: Re mu > 0 for every level.

**Hypothesis (SCAL_B): scaling for boxes with free walls at complex bare coupling (the one named hypothesis of this item).** There are an admissible psi, with F^ = e^{-psi}; a coupling beta_1 >= x_*; a size n_min; a set I and functions e_i, i in I, on the half-plane {Re l > 0}; and eta in [0, 1); such that for every n >= n_min and every beta in S_psi(beta_1), with l = n F^(beta):
 (S1) T_{B_n}(beta) has an eigenvalue lambda_0(n, beta) != 0 of algebraic multiplicity one;
 (S2) for every other nonzero eigenvalue lambda of T_{B_n}(beta) there is i in I with
   -log |lambda/lambda_0(n, beta)| >= (1 - eta) Re( F^(beta) e_i(n F^(beta)) ).
In words: each level of the box is F^(beta) times a function of the complex size l = n F^(beta), and the real part is controlled from below up to a fixed fraction. The e_i stand for the differences E_i(l) - E_0(l) of the levels of the continuum Hamiltonian of a box of size l with free walls, continued to complex l. Note that l runs over Re l > 0 as beta runs over S_psi: arg l = -Im psi(beta) lies in (-pi/2, pi/2).

What (SCAL_B) contains, part by part.
- That a scale function exists as an analytic function near the real axis, with the two-loop form up to an admissible correction. At real beta this is input (2L) and more; the account has neither (Section 1).
- At real beta: the levels of T_{B_n}(beta), divided by a(beta), converge as beta -> infinity at fixed n a(beta) = l. This is a continuum limit of the spectrum of a box with free walls. The account has continuum limits of correlations of one observable on periodic tori, and their uniqueness given the renormalised coupling (clause (d), 1826-1833); it has no box with free walls and no convergence of spectra.
- At complex beta: the same after continuation. The dilation identity (1667-1671) is the real-axis reason for the form: the lattice measure depends on (beta, n) only, and first passage fixes the unit of length as a function of beta; a complex beta is a complex unit of length.
- (S2) is one-sided, and relative to the real part. This is the weakest form that the reduction uses. A two-sided error relative to the modulus is not enough near the side curves; see 4.4.

**Statement (CP): positivity for the continuum levels.** For every i in I, every |l| > 0 and every theta in (-pi/2, pi/2):
  Re( e^{-i theta} e_i(|l| e^{-i theta}) ) > 0.
This is the statement of the brief, Re(e^{-i theta}(E_i - E_0)(|l| e^{-i theta})) > 0.

### 4.3 Theorem R (the reduction)

Assume (SCAL_B) and (CP). Then (DOM_{B_n}) holds on S_psi(beta_1) for every n >= n_min. Hence, with Theorem V and Theorem HM-s':
if in addition (DOM_{B_n}) holds on an open set that contains D_X^psi intersected with {0 < Re beta <= beta_1, |beta| > r_0} for every X (for example by (ZF_{B_n}-x) on the tube lens and Proposition D), and (2L_psi) holds, then
  m_{B_n}(beta) >= (kappa_0 eps/C_2) a(beta) for every real beta >= beta_1 and every n >= n_min.

Proof. Fix n >= n_min and beta in S_psi(beta_1). Put l = n F^(beta) and theta = Im psi(beta), so |theta| < pi/2 and l = |l| e^{-i theta}. For i in I: F^(beta) e_i(l) = (l/n) e_i(l), so Re(F^(beta) e_i(l)) = (|l|/n) Re(e^{-i theta} e_i(|l| e^{-i theta})) > 0 by (CP). By (S2) every nonzero eigenvalue other than lambda_0 has |lambda| < |lambda_0|. The rest of the spectrum of the compact operator T_{B_n}(beta) is at most the point 0. With (S1) this is (DOM). The second part: (DOM_{B_n}) holds on (D_X^psi)' for every X, Theorem V gives m >= kappa_0 omega, Theorem HM-s' and (2L_psi) give the bound, and X -> infinity. QED.

Converse (exact scaling). If (S2) holds with equality and eta = 0 for a surjective assignment of levels to indices, then (DOM_{B_n}) on S_psi(beta_1) for all n >= n_min is equivalent to (CP) at the sizes l = n F^(beta) that occur. So (CP) is not only sufficient: under exact scaling it is the statement.

**What replaces node Z7.** Not "(ZF_B-s): no zeros in the scaling region" (Example 3.8), but "(DOM_B-s): a strictly dominant simple eigenvalue in the scaling region", which under (SCAL_B) is (CP).

### 4.4 Tests of (CP), and what would make it fail (guides, by hand; nothing here is a proof about Yang-Mills)

1. Free massive particle in a box. e(l) = sqrt(m^2 + k^2/l^2), k real. Then e^{-i theta} e(|l| e^{-i theta}) = sqrt(m^2 e^{-2 i theta} + k^2/|l|^2). For |theta| < pi/2 the number under the root is never in (-infinity, 0] (its imaginary part is -m^2 sin 2 theta, zero only at theta = 0, where it is positive). So the root continued from theta = 0 is the principal one and has positive real part. (CP) holds. Sums of such levels (free multi-particle states) also satisfy it.
2. Small boxes. e(l) = c_i/l with c_i > 0 (the perturbative regime, up to the running of the coupling): e^{-i theta} e(|l| e^{-i theta}) = c_i/|l| > 0. (CP) holds, with a margin that does not shrink at theta -> +-pi/2.
3. A level of dimension two. e(l) = sigma l (a flux tube that spans the box): e^{-i theta} e = sigma |l| e^{-2 i theta}, with real part sigma |l| cos 2 theta < 0 for |theta| > pi/4. (CP) fails beyond half the angle. This is the periodic case of plan 2.5, in the present language. So the content of (CP) for a box with free walls includes: no level grows linearly with the size. The plan argues this from the absence of winding flux; it is not proved.
4. An exceptional point of the ground level. If E_0(l) and some E_i(l) coincide at a complex l_* with Re l_* > 0 (a square-root branch point of the vacuum energy), then e_i(l_*) = 0 and (CP) fails there. So (CP) includes: the vacuum level of the box has no branch point in Re l > 0.
5. Why (S2) is relative to the real part. In test 1, the margin is Re sqrt(...) which tends to k/|l| > 0 at theta -> +-pi/2 for k != 0 but to 0 for k = 0 (a particle at rest: e^{-i theta} m). So near the side curves the real part of the lowest levels is a small fraction of their modulus, and an error relative to the modulus (lattice artefacts, or the difference between psi and the exact scale function) can change its sign in a thin sliver along the sides. The remedy within the present framework: such errors change the region to that of another admissible function (4.0), and Theorem HM-s' then loses only a constant, as long as the change of angle is at most of order |Im beta|/|beta|^2. A larger change, of order 1/|beta|, changes the power of beta in the bound (Section 2, Remark 3). I did not write this as a theorem, because the error terms are not known.

**Standing after Step 4 (06:35Z).** The scaling statement is the named hypothesis (SCAL_B). The reduction to the continuum levels is Theorem R. Open: (SCAL_B) itself, (CP), (2L).
