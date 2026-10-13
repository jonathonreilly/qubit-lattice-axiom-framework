"""R19-13 library: entangled ("isometric") site insertion on an infinite chain, per transverse momentum.

Lattice units a = c = hbar = 1.  Scalar chain H = sum_i [pi_i^2/2 + M^2 phi_i^2/2] + sum_bonds (phi_i - phi_j)^2/2.
Insertion: a new site n is placed between old neighbours s_R and s_{R+1}.  Old slab S_old = 2R consecutive sites,
new slab S_new = S_old + n (2R+1 sites, radius R around n).  Boundary sites bL, bR (adjacent to the slab) and
everything beyond them (Rbar) keep their OLD joint state (the operation acts only on the slab).

Window reduction (exact for the infinite chain):
  E_new(psi) - E_old(GS) = E_mid_new(psi) - E_mid_old(GS),  E0_new - E0_old = e0(M) = int dk/2pi omega_k/2,
  so dE = E_mid_new(psi) - E_mid_old(GS) - e0(M).
E_mid only involves the slab block Gamma_SS and the slab-boundary cross covariance.

Two computations of min dE over operations on the slab:
  (U) explicit Gaussian isometry: new site appended in its local GS, then a symplectic S on S_new; minimise
      E(S) = 1/2 tr(S^T A S G0) + tr(S^T B) + const over Sp(2n)  -> an UPPER bound (an explicit rule).
  (L) convex relaxation over ALL states of S_new u Rbar whose Rbar marginal is the old one (any channel on S_old,
      any ancilla, Gaussian or not):  Gamma_{S,Rbar} = T F,  Gamma_SS + iJ/2 - T Q0 T^T >= 0 with
      Q0 = Gamma0_{S_old} + iJ/2 (Schur complement of the old pure state).  -> a LOWER bound (SDP).
"""
import numpy as np
import warnings
warnings.filterwarnings('ignore', message='.*roundoff.*')
from scipy import integrate
from scipy.linalg import expm, expm_frechet, eigh
from functools import lru_cache


@lru_cache(maxsize=None)
def chain_corr(M, nmax):
    """Infinite-chain GS correlators <phi_0 phi_n>, <pi_0 pi_n> (n = 0..nmax) and e0 = (1/2) int omega dk/2pi."""
    def om(k):
        return np.sqrt(M * M + 4 * np.sin(k / 2) ** 2)
    kc = min(np.pi, 20 * max(M, 1e-12))
    Gx = np.zeros(nmax + 1); Gp = np.zeros(nmax + 1)
    for n in range(nmax + 1):
        # (1/pi) int_0^pi cos(nk) f(k) dk ; split near k=0 where 1/omega peaks (width M)
        fx = lambda k: 1.0 / (2 * om(k))
        fp = lambda k: om(k) / 2
        vx = 0.0; vp = 0.0
        for (a, b) in ((0.0, kc), (kc, np.pi)) if kc < np.pi else ((0.0, np.pi),):
            if n == 0:
                vx += integrate.quad(fx, a, b, limit=400, epsabs=1e-15, epsrel=1e-13)[0]
                vp += integrate.quad(fp, a, b, limit=400, epsabs=1e-15, epsrel=1e-13)[0]
            else:
                vx += integrate.quad(fx, a, b, weight='cos', wvar=n, limit=400, epsabs=1e-15, epsrel=1e-13)[0]
                vp += integrate.quad(fp, a, b, weight='cos', wvar=n, limit=400, epsabs=1e-15, epsrel=1e-13)[0]
        Gx[n] = vx / np.pi; Gp[n] = vp / np.pi
    e0 = 0.5 * integrate.quad(lambda k: om(k), 0, np.pi, epsabs=1e-15, epsrel=1e-13)[0] / np.pi
    return Gx, Gp, e0


def window(M, R):
    """Build the window data for radius R.  Coordinates on S_new: (phi_1..phi_n, pi_1..pi_n), n = 2R+1,
    new order s_1..s_R, new, s_{R+1}..s_{2R}.  Old window = bL, s_1..s_2R, bR (consecutive)."""
    n = 2 * R + 1
    Gx, Gp, e0 = chain_corr(M, 2 * R + 2)
    # old positions (bL = 0, s_j = j, bR = 2R+1); new-slab index -> old position (None for the new site)
    oldpos = list(range(1, R + 1)) + [None] + list(range(R + 1, 2 * R + 1))
    wl = np.sqrt(M * M + 2)
    X = np.zeros((n, n)); P = np.zeros((n, n))
    for i, pi_ in enumerate(oldpos):
        for j, pj in enumerate(oldpos):
            if pi_ is None or pj is None:
                if pi_ is None and pj is None:
                    X[i, j] = 1 / (2 * wl); P[i, j] = wl / 2
                continue
            X[i, j] = Gx[abs(pi_ - pj)]; P[i, j] = Gp[abs(pi_ - pj)]
    G0 = np.block([[X, np.zeros((n, n))], [np.zeros((n, n)), P]])
    # new slab Hamiltonian block A (1/2 z^T A z): phi block tridiagonal (M^2+2, -1), pi block identity
    V = np.diag(np.full(n, M * M + 2.0)) - np.eye(n, k=1) - np.eye(n, k=-1)
    A = np.block([[V, np.zeros((n, n))], [np.zeros((n, n)), np.eye(n)]])
    # cross with boundary: -phi_1 phi_bL - phi_n phi_bR.  B = h_{S,d} Gamma0_{d,S}
    B = np.zeros((2 * n, 2 * n))
    for i, pi_ in enumerate(oldpos):
        if pi_ is None:
            continue
        B[0, i] -= Gx[abs(0 - pi_)]          # <phi_bL phi_s>
        B[n - 1, i] -= Gx[abs(2 * R + 1 - pi_)]  # <phi_bR phi_s>
    # constant: 1/2<phi_bL^2> + 1/2<phi_bR^2> from the two boundary bonds
    const_new = Gx[0]
    # old mid energy: on-site + bonds within old window (sites 1..2R interior; bonds (0,1)...(2R,2R+1))
    if R == 0:
        Emid_old = Gx[0] - Gx[1]   # 1/2<(phi_bL - phi_bR)^2>
    else:
        nn = 2 * R
        Emid_old = nn * (0.5 * Gp[0] + 0.5 * M * M * Gx[0]) + (nn + 1) * (Gx[0] - Gx[1])
    return dict(n=n, G0=G0, A=A, B=B, const=const_new, Emid_old=Emid_old, e0=e0, Gx=Gx, Gp=Gp,
                oldpos=oldpos, X=X, P=P)


def J_of(n):
    return np.block([[np.zeros((n, n)), np.eye(n)], [-np.eye(n), np.zeros((n, n))]])


def energy_S(W, S):
    return 0.5 * np.trace(S.T @ W['A'] @ S @ W['G0']) + np.trace(S.T @ W['B']) + W['const']


def dE_of_S(W, S):
    return energy_S(W, S) - W['Emid_old'] - W['e0']


def symp_opt(W, S_init=None, tol=1e-13, maxiter=20000, verbose=False):
    """Minimise E(S) over Sp(2n) by L-BFGS in the Lie algebra with periodic re-centring.
    S = expm(J K) S_ref, K symmetric.  Returns (dE, S)."""
    from scipy.optimize import minimize
    n = W['n']; J = J_of(n); A = W['A']; G0 = W['G0']; B = W['B']
    iu = np.triu_indices(2 * n)
    S_ref = np.eye(2 * n) if S_init is None else S_init.copy()

    def unpack(k):
        K = np.zeros((2 * n, 2 * n)); K[iu] = k; K = K + K.T - np.diag(np.diag(K)); return K

    best = None
    for outer in range(60):
        def f(k):
            K = unpack(k); X = J @ K
            Ex = expm(X); S = Ex @ S_ref
            E = 0.5 * np.trace(S.T @ A @ S @ G0) + np.trace(S.T @ B)
            G = A @ S @ G0 + B            # dE/dS
            GE = G @ S_ref.T              # dE/dEx
            GX = expm_frechet(X.T, GE, compute_expm=False)   # adjoint of Frechet derivative
            GK = J.T @ GX
            GK = GK + GK.T
            # diagonal entries counted once
            d = np.arange(2 * n)
            gfull = GK.copy(); gfull[d, d] = GK[d, d] / 2
            return E, gfull[iu]
        k0 = np.zeros(len(iu[0]))
        res = minimize(f, k0, jac=True, method='L-BFGS-B',
                       options=dict(maxiter=400, ftol=1e-16, gtol=1e-12, maxcor=30))
        K = unpack(res.x); S_ref = expm(J @ K) @ S_ref
        E = res.fun
        if verbose:
            print(outer, E + W['const'] - W['Emid_old'] - W['e0'], res.nit, np.abs(res.jac).max())
        if best is not None and abs(best - E) < tol * max(1, abs(E)) and np.abs(res.jac).max() < 1e-9:
            best = E; break
        best = E
    return best + W['const'] - W['Emid_old'] - W['e0'], S_ref


def sdp_lower(W, solver='CLARABEL', eps=1e-10):
    """Convex relaxation over all states with fixed Rbar marginal (window form).  Returns lower bound on dE."""
    import cvxpy as cp
    n = W['n']; R = (n - 1) // 2
    oldidx = [i for i, p in enumerate(W['oldpos']) if p is not None]
    if R == 0:
        # S_old empty: T has no columns; state on new site arbitrary; cross terms zero
        G = cp.Variable((2, 2), symmetric=True)
        Jn = J_of(1)
        cons = [cp.bmat([[G, np.zeros((2, 2))], [np.zeros((2, 2)), np.zeros((2, 2))]]) >> 0]  # placeholder
        # direct: min 1/2 tr(A G) s.t. G + iJ/2 >= 0  -> GS of A: omega/2
        w = np.sqrt(W['A'][0, 0])
        return 0.5 * w + W['const'] - W['Emid_old'] - W['e0']
    m = 2 * R
    # old marginal on S_old (consecutive old positions 1..2R)
    Gx, Gp = W['Gx'], W['Gp']
    Xo = np.array([[Gx[abs(i - j)] for j in range(m)] for i in range(m)])
    Po = np.array([[Gp[abs(i - j)] for j in range(m)] for i in range(m)])
    Go = np.block([[Xo, np.zeros((m, m))], [np.zeros((m, m)), Po]])
    Q0 = Go + 0.5j * J_of(m)
    w, U = np.linalg.eigh(Q0)
    keep = w > 1e-14 * w.max()
    L = U[:, keep] * np.sqrt(w[keep])
    r = L.shape[1]
    # cross covariance old S_old <-> boundary phis (bL at 0, bR at 2R+1; S_old at 1..2R)
    Fd = np.zeros((2 * m, 2))
    for i in range(m):
        Fd[i, 0] = Gx[abs(i + 1 - 0)]; Fd[i, 1] = Gx[abs(i + 1 - (2 * R + 1))]
    Gs = cp.Variable((2 * n, 2 * n), symmetric=True)
    T = cp.Variable((2 * n, 2 * m))
    Jn = J_of(n)
    top = Gs + 0.5j * Jn
    TL = T @ L
    Mbig = cp.bmat([[top, TL], [TL.H, np.eye(r)]])
    cons = [Mbig >> 0]
    # energy: 1/2 tr(A Gs) + cross: -<phi_1 phi_bL> - <phi_n phi_bR>, Gamma_{S,d} = T Fd
    cross = T @ Fd
    E = 0.5 * cp.trace(W['A'] @ Gs) - cross[0, 0] - cross[n - 1, 1]
    prob = cp.Problem(cp.Minimize(E), cons)
    prob.solve(solver=solver)
    return prob.value + W['const'] - W['Emid_old'] - W['e0'], prob.status
