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
5. Sharpness (not used): in the coordinate zeta = phi(beta) the function Re F = e^{-Re zeta} cos(Im zeta) is positive harmonic in S and vanishes on the sides, so no domain inside S has harmonic measure larger than a constant times F on the real axis far to the right. The exponent is exact.

**Standing after Step 1 (05:25Z).** Part (i) is proved as Theorem HM-s, given the input (2L), which the account does not contain. Next: part (ii).
