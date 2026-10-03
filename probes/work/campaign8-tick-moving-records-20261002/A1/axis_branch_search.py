"""Branch-resolved search using the exact axis integrality condition.

For an exactly unitary, finite-range, O-covariant spin-1/2 walk normalised by
W(0) = 1 (W(0) is forced to be scalar), the restriction to the k_x axis must be
W(t,0,0) = exp(-i m t sigma_x) with integer |m| <= rho (unimodular trig
polynomials are monomials).  Imposing this as an extra (linear) residual for
each branch m removes the quasi-local approximants (whose axis phase is not
linear) and leaves only candidate exact solutions.
usage: python axis_branch_search.py RHO NSTARTS SEED
"""
import sys
import time
import numpy as np
from scipy.optimize import least_squares

rho_in = sys.argv[1]
nst = int(sys.argv[2])
sd = int(sys.argv[3])
sys.argv = ['covariant_walk_search.py', rho_in, '0', str(sd)]
exec(open('covariant_walk_search.py').read().split("t0 = time.time()")[0])
rng = np.random.default_rng(sd)
nt = 4 * rho + 1
ts = np.arange(nt) * 2 * np.pi / nt
axis_cols = []
for v0, orb, inv in orbits:
    for B in inv:
        M = np.zeros((nt, 2, 2), complex)
        for w, U in orb.items():
            M += np.exp(-1j * ts * w[0])[:, None, None] * (U @ B @ U.conj().T)[None]
        axis_cols.append(M)
axis_cols = np.array(axis_cols)
SX = np.array([[0, 1], [1, 0]], complex)


def target(m):
    return np.array([np.cos(m * t) * I2 - 1j * np.sin(m * t) * SX for t in ts])


def resid2(x, m, lam=3.0):
    r = resid(x, 1.0, 1.0) if m == 0 else resid(x, 0.0, 0.0)[:-1]
    c = unpack(x)
    Wa = np.einsum('i,itab->tab', c, axis_cols)
    d = (Wa - target(m)).ravel() * lam / np.sqrt(nt)
    return np.concatenate([r, d.real, d.imag])


def jac2(x, m, lam=3.0):
    J = jac(x, 1.0, 1.0) if m == 0 else jac(x, 0.0, 0.0)[:-1]
    P_ = len(axis_cols)
    Ja = axis_cols.reshape(P_, -1).T * lam / np.sqrt(nt)  # d(Wa)/d c (complex)
    JA = np.zeros((2 * Ja.shape[0], 2 * P_))
    JA[:Ja.shape[0], :P_] = Ja.real
    JA[:Ja.shape[0], P_:] = -Ja.imag
    JA[Ja.shape[0]:, :P_] = Ja.imag
    JA[Ja.shape[0]:, P_:] = Ja.real
    return np.vstack([J, JA])


t0 = time.time()
for m in range(0, rho + 1):
    best = np.inf
    bx = None
    for s in range(nst):
        x0 = rng.normal(size=2 * P) * 0.3
        sol = least_squares(resid2, x0, jac=jac2, args=(m,), method='lm', xtol=1e-15,
                            ftol=1e-15, gtol=1e-15, max_nfev=3000)
        cost = float(np.sum(sol.fun ** 2))
        if cost < best:
            best, bx = cost, sol.x
        if time.time() - t0 > 50:
            break
    c = unpack(bx)
    wmov = np.real(c.conj() @ (gram * np.outer(mov, mov)) @ c)
    print(f"rho={rho} branch m={m}: min total residual^2 = {best:.3e} (moving weight {wmov:.3f}), t={time.time()-t0:.0f}s")
    if time.time() - t0 > 50:
        break
