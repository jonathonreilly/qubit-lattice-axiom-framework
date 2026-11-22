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
