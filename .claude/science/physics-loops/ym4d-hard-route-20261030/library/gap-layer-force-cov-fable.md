lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-22T19:48Z

# Row 1388, gap-layer-force-cov-fable: layer-force covariance at physical distance

Provenance: Claude Fable 5.2, medium effort, Mac mini worker 1, pinned commit 05a3af9c4, started
2026-11-22T07:48Z (date -u). Not an audit. Nothing here is checked by another model.

## 0. Plan (written first, save protocol)

Task: prove or refute the displayed estimate in the section 'Next proof row' of
`library/gap-mech-direction2-check-astra62.md`.

Steps, one per response, each appended here before the next:

1. Read the statement (check 1387, 'Next proof row') and its sources: row 1283 (5)-(14), (23); row 1141 (2)
   and check 1142; checks 1381 (lines 88-96) and 1384; row 1380 M-C. Restate the estimate exactly. (Section 1)
2. Repo search: open-core.md, FINISH rows and library for the same statement. (Section 2)
3. Attack. Try to kill first (U(1), five dimensions, what scale the force covariance must have). (Section 3 on)
4. State what a proof gives the chain and what it does not. (last section)

Status: step 1 in progress.

## 1. The statement, restated (step 1; sources read in full: check 1387 whole file; row 1283 lines 11-268)

Setting (check 1387, 'Next proof row'; row 1283 (11)). Ordinary periodic Wilson SU(2) torus, spatial side
n = n_j, beta = beta_j <= B_0 log n, physical side L_* > L_gamma, centre-projected trace of length
t = 2 floor(n/1024). X, Y are the spatial link fields of two adjacent slices away from the seam, g_x in S^3
the temporal links between them. Given (X, Y),

    pi_{X,Y}(dg) = Z(X,Y)^{-1} exp[ A(g) ] prod_x dg_x,   A(g) = beta sum_{e=xy} g_x . R_e g_y,
    R_e q = X_e q Y_e^{-1},  u.v = Re(u^{-1} v).                                   (row 1283 (11))

F_e = (F_e^a)_{a=1,2,3}: the left-invariant derivatives of A in Y_e. Each F_e^a is a function of (g_x, g_y)
only, quadratic in g, so even under the common flip g -> -g, and |F_e^a| <= beta, |grad_g F_e^a| <= 2 beta.
For e != f, Cov_pi(F_e^a, F_f^b) = d_{Y_e}^a d_{Y_f}^b log Z(X,Y) (row 1380 M-C; check 1381 line 88).
Q(X) = 1{lambda_min(L_X) > u}, u = delta/(1 + B_0 log n) (check 1387 section 2; row 1283 (5)-(7)).

(SHELL)   S_n := sum_{f: n/4 <= d_inf(e,f) < n/2} E[ Q(X) Q(Y) || Cov_pi(F_e, F_f) ||_HS ] = o(1)  (j -> infinity).

Three facts that fix the size of the problem (used below):

(a) The shell has about n^3 edges and n >= exp(beta/B_0). So (SHELL) needs the average pair covariance below
    n^{-3} <= exp(-3 beta/B_0). On the asymptotic-freedom trajectory 1/B_0 is about 2.69 (the lane's number,
    row 1332), so the threshold is about exp(-8.07 beta). A non-perturbative effect of size exp(-c beta)
    that does NOT decay with distance would refute (SHELL); one that decays with distance at any rate
    n^{-3-epsilon} would not.
(b) H(g) := -A(g) = (beta/2) <g, L_{X,Y} g> - 3 beta n^3 on the product of unit spheres, where L_{X,Y} is the
    covariant Laplacian with the orthogonal transports R_e on R^4-valued fields (row 1283, after (11)). So
    pi_{X,Y} is the Gaussian law N(0, (beta L_{X,Y})^{-1}) restricted to |g_x| = 1 for all x: a spherical
    (O(4)-type) model with quenched random transports.
(c) Riemannian Hessian of H on prod_x S^3 at g, for tangent xi (xi_x orthogonal to g_x in R^4):
        Hess H (xi, xi) = beta sum_{e=xy} |xi_x - R_e xi_y|^2 - beta sum_x lambda_x(g) |xi_x|^2,
        lambda_x(g) = sum_{y ~ x} (1 - g_x . R_e g_y) >= 0   (six bonds at x).
    Proof: on one sphere, Hess(-beta g.m)(xi,xi) = beta (g.m)|xi|^2 with m_x = sum_{y~x} R_e g_y, and
    g_x.m_x = 6 - lambda_x; the mixed blocks are -beta xi_x . R_e xi_y. Expand the square.
    At a critical point g*, L g* = lambda* g* sitewise, so L - lambda* has the exact normal zero mode g*.

Status: step 1 done. Next: repo search (Section 2), then the attacks.

## 2. Repo search (step 2, 2026-11-22T07:58Z by date -u)

Searched `library/gap-*.md`, `library/open-core.md`, `library/open-registry.md` and the FINISH rows from 350 on
(grep -l -i -F) for: LAY-cov, layer covariance, layer-force, Langevin, finite speed, Lieb-Robinson, Helffer,
Brascamp, Bakry, Poincare, Glauber, heat-bath, Debye, Gribov, Faddeev. A search that finds nothing does not
prove absence.

- (LAY-cov) and the derivative identity: row 1380 M-C (`gap-mech-direction-fable.md` 223-246); check 1381
  (`gap-mech-direction-check-astra62.md` 88-96): unrestricted (LAY-cov) FAILS in 4D by row 1283 (23); the
  force-only estimate is open. Check 1384 line 91-93 repeats this. Check 1387 poses (SHELL). No row attacks
  (SHELL) itself; `open-core.md` and `open-registry.md` have no entry for it.
- Linear inputs: row 1141 (2) (`gap-crux2-astra62.md`), row 1283 (1)-(10) and the paired version after (11).
- What (12), (23) of row 1283 rule out: for the odd spins g_x, E||C_xy||_* >= (1 - C/beta)^r and the replica
  overlap is at least 1 - C beta^{-eta} at every separation. So no bound of the covariance of ALL local
  functions by the Green kernel exists. The forces F_e are even; (12) and (23) say nothing on them.
- Finite speed by Duhamel is used for a different chain in `gap-mini-solve-w-opus.md` line 139 and
  `gap-mini-solve-q-fable.md` Lemma 6.2. The exact cone of the transfer step is row 1032 B2
  (`gap-afield-b-max.md` 120). I found no file that combines finite speed of the LAYER dynamics with a
  spectral gap or a relaxation bound to control the layer covariance. Theorem A below is that combination.
- Outline (Sussman and Alpoge, with Claude and Codex as authors of their text): not consulted for this row
  beyond the citations already in check 1387 (their separated-correlation bound, outline 3238-3254, is for
  other observables). I take no step from it.

## 3. Try to kill first (step 3a)

Criteria written first: (SHELL) is refuted by any mechanism that gives E||Cov_pi(F_e,F_f)|| >= c n^{-3} on a
positive fraction of the shell, that is about exp(-3 beta/B_0) per pair without decay in distance (fact (a)).

1. **Rare flat regions (Griffiths).** A covariance at distance r through a region of coherent adjoint
   transport needs a tube of length r in which the cell defects D_z of row 1283 (2) are all small. By (2)
   each cell costs a factor C b v, so a tube costs at most (C b v)^{c r}. At r = n/4 this is exp(-c n), far
   below n^{-3}. This is the same count that gives (5). No refutation.
2. **Global modes.** In U(1) the shell sum is carried by the massless mode (Proposition B). For SU(2) the
   only global symmetry of pi_{X,Y} on a slice with non-abelian holonomy is g -> -g
   (`gap-cuttyp-max.md` 108-112), and F is even. Domain flips g -> -g on a set D give only coboundaries of
   D; they cost exp(-2 beta |boundary|) and are local. No refutation.
3. **Non-perturbative local defects** of weight exp(-c beta) exist (a tail of each one-site law), and exceed
   n^{-3} per site when c < 3/B_0. They are local: a correlation at distance n/4 needs a chain of them. No
   refutation.

Verdict of the kill attempts: no mechanism found for SU(2). This is not evidence that (SHELL) holds.

## 4. Theorem A: (SHELL) follows from one relaxation bound for one force (PROVED here, unchecked)

**Dynamics.** Fix (X, Y). M = (S^3)^V, V = (Z/n)^3, unit spheres, product metric. H = -A is smooth.
Let \mathcal L = sum_x (Delta_x - grad_x H . grad_x), P_t = exp(t \mathcal L). It is self-adjoint and
non-positive in L^2(pi), pi = pi_{X,Y}, with pi(F \mathcal L G) = - pi(grad F . grad G). The flip g -> -g is an isometry that
preserves H, so P_t maps even functions to even functions. Let gamma_even(X,Y) > 0 be the bottom of the
spectrum of -\mathcal L on even functions of mean zero. (M is compact and connected, so it is positive.)

**Theorem A.** Let c_0 = 10^{-3}, T = c_0 n / beta, n >= 64. For every (X, Y), all edges e, f with
d_inf(e, f) >= n/4 and all a, b:

    | Cov_pi(F_e^a, F_f^b) - Cov_pi(P_{T/2} F_e^a, P_{T/2} F_f^b) |  <=  3 c_0 beta n e^{-n/4},           (A1)
    | Cov_pi(P_{T/2} F_e^a, P_{T/2} F_f^b) |  <=  beta^2 exp( - c_0 gamma_even n / beta ).                 (A2)

Consequently, with v_n := E[ Q(X) Q(Y) sum_a Var_pi(P_{T/2} F_e^a) ] (one rooted edge e),

    S_n  <=  81 beta n^4 e^{-n/4}  +  27 n^3 v_n .                                                          (A3)

So (SHELL) holds if

    (LAY-relax)   v_n = o(n^{-3}),

and (LAY-relax) holds if  P( Q(X)Q(Y) = 1, gamma_even(X,Y) < (4/c_0) beta log n / n ) = o(n^{-3} beta^{-2})
(call this (LAY-gap); then v_n <= 3 beta^2 [ n^{-4} + that probability ]).

**Proof.** (i) Semigroup identity. d/dt pi(F P_t G) = pi(F \mathcal L P_t G) = - pi(grad F . grad P_t G). So

    Cov_pi(F, G) = int_0^T pi( grad F . grad P_t G ) dt + Cov_pi(F, P_T G),

and Cov_pi(F, P_T G) = Cov_pi(P_{T/2} F, P_{T/2} G) by self-adjointness.

(ii) Site-resolved gradient bound. Let f_t = P_t G and u_x(t) = |grad_x f_t|^2. Bochner's formula on the
factor x (Ricci curvature 2 on the unit S^3), and commutation of derivatives on different factors, give

    (1/2) \mathcal L |grad_x f|^2 - < grad_x f, grad_x \mathcal L f >
        = sum_y |grad_y grad_x f|^2 + 2 |grad_x f|^2 + sum_y Hess_{xy} H (grad_x f, grad_y f).

(The drift terms: < grad_x f, grad_x (sum_y < grad_y H, grad_y f >) > = sum_y Hess_{xy}H(grad_x f, grad_y f)
+ sum_y Hess_{xy} f (grad_x f, grad_y H), and the last sum equals (1/2) grad H . grad |grad_x f|^2.) By
fact (c), Hess_{xx} H = beta (6 - lambda_x) >= -6 beta, and for y ~ x the block Hess_{xy} H has norm at most
beta; other blocks vanish. With 2ab <= a^2 + b^2 on the six neighbours,

    \mathcal L u_x - 2 < grad_x f, grad_x \mathcal L f >  >=  - 18 beta u_x - beta sum_{y ~ x} u_y .

Since d/ds [ P_s u_x(t - s) ] = P_s[ \mathcal L u_x - 2 < grad_x f, grad_x \mathcal L f > ](t - s), integration over
s in [0, t] and the sup norm U_x(t) = sup_g u_x(t, g) give

    U_x(t) <= U_x(0) + beta int_0^t [ 18 U_x(r) + sum_{y ~ x} U_y(r) ] dr .

Iterate (the kernel is non-negative): U(t) <= exp(t beta (18 + Adj)) U(0) entrywise. For G = F_f^b,
U_y(0) <= beta^2 for the two ends of f and U_y(0) = 0 otherwise (F_f^b is beta times a form bilinear in the
two end spins through orthogonal maps). Paths of k steps from x number at most 6^k, and
sum_{k >= d} a^k / k! <= (e a / d)^d for a <= d. Hence, for x an end of e, d >= n/4 - 1 the graph distance
to f, and beta t <= c_0 n:

    |grad_x P_t G|^2 <= 2 beta^2 e^{18 beta t} (6 e beta t / d)^d <= 2 beta^2 exp( 0.018 n - (n/4 - 1) * 2.6 )
                    <= 2 beta^2 e^{-n/2}        (n >= 64; 6 e c_0 n / d <= 24 e c_0 * (64/60) < 0.07 < e^{-2.6}).

(iii) (A1): |grad_x F_e^a| <= beta at each of the two ends of e, so the integral in (i) is at most
T * 2 * beta * sqrt(2) beta e^{-n/4} <= 3 c_0 beta n e^{-n/4}. (A2): F_f^b is even, so P_{T/2} F_f^b - pi(F_f^b)
is even of mean zero and has norm at most beta e^{-gamma_even T/2}; the same holds for F_e^a; Cauchy-Schwarz.

(iv) (A3): the shell has at most 3 n^3 edges and nine pairs (a, b). Bound the Hilbert-Schmidt norm by the
sum of the nine entries. For the second term use |Cov(P F_e^a, P F_f^b)| <= sqrt(Var Var), then
sum_{a,b} sqrt(v_a w_b) <= 3 sqrt(sum v_a sum w_b), then Cauchy-Schwarz in the expectation. The law of
(X, Y) is invariant under spatial translations and the cubic rotations of the slice, the layer law is
covariant, and sum_a Var_pi(P_{T/2} F_f^a) does not depend on the orthonormal basis. So
E[Q Q sum_a Var_pi(P_{T/2}F_f^a)] = v_n for every f. (With a centre seam elsewhere on the time circle the
slice symmetries are the same.) The gap form: on {gamma_even >= (4/c_0) beta log n / n},
Var_pi(P_{T/2} F) <= beta^2 e^{-gamma_even T} <= beta^2 n^{-4}. QED

**Remarks.**

1. The theorem holds for every pair (X, Y): no Q, no trajectory, no Wilson law is used in (A1), (A2). It
   holds for every even local function with bounded gradient in place of F, for the X-derivatives as well,
   in any dimension (replace 6 by the degree), and for U(1) (unit circles, Ricci 0).
2. (LAY-relax) is a statement on one stationary reversible process: draw (X, Y, g) from the Wilson law, freeze
   X and Y, run the Langevin dynamics of the one layer. It asks that the autocorrelation of one force at
   time c_0 n / beta be o(n^{-3}). In spectral terms: Var_pi(P_{T/2}F) = int e^{-s T} d mu_F(s), so it is
   enough that the annealed spectral mass of F_e below s_n = (4/c_0) beta log n / n is o(n^{-3}).
   A polynomial decay t^{-3-epsilon} of the annealed autocorrelation suffices. No mass of order one is needed.
3. Size of the slack: n >= e^{beta/B_0}. A lower bound gamma_even >= e^{-c beta} with c < 1/B_0 on an event of
   probability 1 - o(n^{-3} beta^{-2}) proves (SHELL).
4. Ballistic speed is wasteful: the true spread is diffusive. A diffusive version would allow T of order
   n^2/(beta log n). I did not prove one: the diagonal block beta (6 - lambda_x) is not bounded below by
   6 beta, and the defect lambda_x has no deterministic small bound.

## 5. U(1) and five dimensions (step 3b, 2026-11-22T07:59Z by date -u)

**Proposition B (harmonic U(1); the estimate FAILS).** Take real temporal variables theta_x and the layer
exponent A = -(beta/2) sum_{e=xy} (theta_y - theta_x + a_e)^2, a_e the difference of the two spatial fields.
Given (X, Y) the gradients d theta are Gaussian with covariance beta^{-1} P, where P = d Delta^{-1} d^* is the
orthogonal projection of l^2(edges) onto gradients. The force is F_e = -beta (d theta + a)_e, so

    Cov(F_e, F_f) = beta P(e, f)      for every (X, Y).

For e = (0, direction 1) and f = (y, direction 1), sum P over (y_2, y_3) in (Z/n)^2 at fixed y_1. The result is
the same projection on the ring Z/n, which is 1 - (1/n) J (J the all-ones matrix), so the plane sum equals
-1/n for every y_1 != 0. Hence

    sum_{y: n/4 <= |y_1| < n/2} |P(e, (y,1))| >= 1/2 ,

and the shell sum with the closed outer bound d_inf <= n/2 is at least beta/2 for every n: a positive
limsup, growing with beta. For the half-open shell of (SHELL) one removes the points with y_2 = n/2 or
y_3 = n/2, at most n^2 points at distance at least n/4. With the kernel bound |P(0, y)| <= C |y|^{-3} on the
torus (lattice Calderon-Zygmund estimate; cited, NOT rebuilt here: gap) they carry at most C/n, and the
shell sum is at least beta (1/2 - C/n). The same computation holds in every layer dimension d >= 1, so in
five dimensions as well. The relaxation side agrees: the harmonic layer has gamma = 4 beta sin^2(pi/n),
below the threshold beta log n / n of Theorem A by a factor n, and the autocorrelation of a force at time t
is of order beta (beta t)^{-3/2}, which is n^{-3/2} at t = T, not o(n^{-3}).

Compact Wilson U(1): the layer is a three-dimensional XY model in the background a. At weak coupling the
same Goldstone mode is expected (row 1380 M-C, ARGUED there). I did not prove a lower bound for it.
Verdict for U(1): (SHELL) fails in the harmonic model (proved up to the cited kernel bound; proved as
written for the closed shell); expected to fail for Wilson U(1); not proved.

**Five dimensions, SU(2).** Theorem A holds verbatim (degree 8, constants change). The linear inputs transfer:
row 1141 (2) with exponent 2/d and row 1283 (8) at d = 4 (check 1387, table row F4). The open input is the
same lemma (LAY-relax) for the four-dimensional layer. Its expected mechanism (Section 6) is the roughness of
single links, which is the same in five dimensions at weak coupling. So (SHELL) is expected to hold in 4D
and in 5D together, as row 1380 said of (LAY-cov), and neither case is proved. (SHELL) is group-selective
(SU(2) against U(1)) and not dimension-selective.

## 6. Three attacks on (LAY-relax) / (SHELL) for SU(2), and why each stops

All three stop at the same point: the fluctuation operator of the layer has no small parameter against the
roughness. In units of 1/beta, three pure numbers of order one compete at every beta.

**The numbers.** By fact (c), Hess H + Ric = beta L_{X,Y} - (beta lambda_x(g) - 2) on tangent fields.
(1) beta lambda_x is the sum of six bond deficits beta (1 - w_p) of temporal plaquettes. Its mean tends to
6 * 3/4 = 9/2 at weak coupling (plaquette value 1 - 3/(4 beta); recalled, not proved here), and it has a
non-degenerate limit law with unbounded support. (2) Ric = 2. (3) The bottom of beta L on tangent fields: a
tangent field is xi_x = g_x omega_x with omega_x in su(2), and |xi_x - R_e xi_y| = |omega_x - p_e Ad(Y_e) omega_y|
with p_e = g_x^{-1} X_e g_y Y_e^{-1} the temporal plaquette, acting by left multiplication (p_e is within
O(beta^{-1/2}) of 1 on typical bonds). So this is beta times the bottom of an adjoint Laplacian of the type of
L_Y, which rows 1141 (2) and 1283 (1)-(5) bound below by beta u = delta beta/(1 + beta): a small constant.
Its true typical value is an unknown number c_1.

**Attack 1: the paired Green kernel through the Helffer-Sjostrand / Brascamp-Lieb representation** (the route
named in check 1387). Cov_pi(F, G) = pi < grad F, W^{-1} grad G >, W = -\mathcal L (x) 1 + Hess H + Ric on
1-forms. A walk expansion of W^{-1} dominated by the walk of row 1283 (9) needs the zeroth-order part
Hess H + Ric to be bounded below by beta L - (small) on the configurations that carry the mass. It is
beta L - (beta lambda - 2), and beta lambda - 2 is positive of order one on a positive density of sites
(mean about 5/2). The killing rate gamma/b of (9) is of order 1/beta per four steps against a growth rate of
order 1/beta per step from the potential, both after division by beta. There is no parameter that makes
the first win. The same negative potential is present in the flat O(4) model, where the true covariance is
positive and massless; so the pointwise operator W(g) is not the object that carries the mass. FAILS; no
repair seen.

**Attack 2: Theorem A plus a contraction estimate for gamma_even** (Dobrushin in the Wasserstein metric, or
path coupling for the heat bath). The one-site law is von Mises-Fisher on S^3 with mean direction
m_x/|m_x|, m_x = sum_{y~x} R_e g_y. The mean direction is Lipschitz in each neighbour with constant
1/|m_x|, and |m_x| <= 6 with |m_x| = 6 - lambda_x + O(lambda^2). The row sum is 6/|m_x| = 1 + lambda_x/6 + ...,
above one by a quantity of order 1/beta. The gain from non-abelian holonomy is of order 1/beta per closed
four-step loop (row 1283 (9)). Same competition, same stop. Holley-Stroock and block-dynamics comparisons
need either a total oscillation of order beta (it is of order beta n^3) or the spatial mixing that is to be
proved. FAILS at the same number.

**Attack 3: Laplace expansion of Z(X,Y) at its maximiser g*, and the annealed replica route.** At g* the
operator P_tan (L - lambda*) P_tan is non-negative, and L - lambda* has the normal zero mode g* (fact (c)).
Its gap is not controlled by Q(X) Q(Y): that would again compare c_1 with the potential lambda*. A
one-loop formula d d log Z = -beta d d dist^2 - (1/2) d d log det + remainder has a remainder that is
extensive in n^3 and is not localised without the decay that is to be proved. The alternative, to compute
E ||Cov||_HS^2 as a gauge-invariant replica expectation and use reflection positivity or the chessboard
bound of row 1283 (20), fails at its first line: two layer replicas over the same (X, Y) have the joint
weight e^{A(g) + A(g')} / Z(X,Y), and the factor 1/Z is not a local Gibbs weight. The signed mean
E Cov_pi(F_e^a, F_f^b) vanishes by gauge covariance at an end of f, so only the norm carries information.
FAILS.

**What all three need (one lemma).** A renormalised statement: after the fluctuations of g at scales up to
sqrt(beta) lattice units are integrated, the adjoint fluctuation of the layer has a positive mass of order
beta^{-1/2} in lattice units on typical (X, Y). In physical language it is the electric (Debye) screening
of the temporal link in a time slab of one step, with the spatial fields quenched. It is a one-loop
statement with constants of order one, not a perturbation of row 1141 (2). I know of no proof at weak
coupling, here or in the literature I can cite from memory (none cited).

## 7. The open lemma, exactly

**(LAY-relax).** On the trajectory (n = n_j, beta_j <= B_0 log n_j), with c_0 = 10^{-3} and T = c_0 n / beta:

    E[ Q(X) Q(Y) sum_a Var_{pi_{X,Y}}( P_{T/2} F_e^a ) ] = o(n^{-3}).

Sufficient: (LAY-gap), P(Q Q = 1, gamma_even < (4/c_0) beta log n / n) = o(n^{-3} beta^{-2}); or a bound
gamma_even >= e^{-c beta}, c < 1/B_0, on an event of that probability. (LAY-relax) implies (SHELL) by
Theorem A. It fails for harmonic U(1) by the factor n^{3/2}. It is not known to be necessary for (SHELL).

## 8. What a proof of (SHELL) would give the chain, and what it would not

Gives: the mixed second derivatives of log K(X, Y) in two links at physical distance are small in the mean
on the slices kept by Q. This is quasi-locality of the scalar one-step kernel (row 1380 M-C, the force-only
form left open by checks 1381 and 1384). By Theorem A, Remark 1, the same lemma gives it for X-derivatives
and for all even local functions of the layer.

Does not give, each a separate obligation:
1. **Absolute control of the neutral trace.** The seed needs s_{n,beta}(2w) <= 4/21. (SHELL) concerns one
   layer with both faces fixed. The trace composes about n/512 layers and integrates the faces; the
   correlation between distant regions is then carried by the spatial fields through time, which is the
   mass gap itself. Row 1283 (7) compares traces as a ratio only (check 1387 section 2).
2. **A dimension-selective iteration.** (SHELL) is expected in 5D too (Section 5). A chain that used only
   (SHELL) and dimension-blind steps would prove the seed in 5D, where (P5) forbids it (check 1387, (b)).
3. **A consumer.** Row 1380 found none for (LAY-cov). The background-uniform form needed by the
   Durhuus-Frohlich comparison is false (rows 1139, 1140); (SHELL) is a mean over typical faces.
4. **The odd sector.** (12), (23) of row 1283 stand: odd local functions of the layer stay correlated at all
   distances.

Recommendation to the lead (unproved opinion): do not queue (LAY-relax) as a hard-proof row for the seed. It is
a self-contained weak-coupling problem (screening in a quenched layer) with no consumer and no dimension
selectivity. Theorem A is worth one line-by-line check if any later row wants to use relaxation in place of
a Green-kernel comparison.

## 9. Status

- PROVED here, not checked by another model: Theorem A ((A1)-(A3), every (X,Y), any dimension, any group
  with the constants changed); fact (c); Proposition B for the closed shell.
- GAP (cited, not rebuilt): the torus kernel bound |P(0,y)| <= C |y|^{-3} used for the half-open shell in
  Proposition B; the weak-coupling plaquette value in Section 6 (used only to explain a failure).
- OPEN: (SHELL) for SU(2) in 4D, neither proved nor refuted. It is reduced to (LAY-relax). No refuting
  mechanism was found (Section 3). Compact U(1) and 5D SU(2) verdicts are expected, not proved.
- No numeric run was made (none would be a step; memory was not checked). No subagent. Outline not used.
- Reading not done: row 1141 (2) and its check 1142 were read only through the quotations in check 1387
  (section 2) and row 1283 (the proofs of (1)-(3)); the files themselves were not opened. No step here uses
  them beyond those quotations.
- Finished 2026-11-22T08:00Z (date -u).

RESULT (FINISH 1388): (SHELL) for SU(2) in 4D is neither proved nor refuted. Proved (unchecked): Theorem A,
for every pair of faces |Cov_pi(F_e,F_f)| <= 3 c_0 beta n e^{-n/4} + beta^2 exp(-c_0 gamma_even n/beta) at
distance n/4, so (SHELL) follows from the one-force relaxation bound (LAY-relax), for which a layer gap as
small as beta log n / n suffices; harmonic U(1) refutes the estimate (shell sum at least beta/2, closed
shell). Open: (LAY-relax) (three attacks stop at one order-one competition, Section 6); compact U(1) and 5D
verdicts are expected only. A proof would give quasi-locality of the one-step kernel, not the neutral trace
bound and not dimension selectivity.
