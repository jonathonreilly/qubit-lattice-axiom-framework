"""Zero-speed branch (forced by the line-integrality theorem): W(0)=1 and W = 1
identically on the x-axis and on the (1,1,1) diagonal (covariance then gives all
axes/diagonals).  Search for nontrivial covariant unitary walks with moving
weight tau.  usage: python zero_speed_branch.py RHO NSTARTS SEED"""
import sys, time
import numpy as np
from scipy.optimize import least_squares
rho_in, nst, sd = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
sys.argv = ['covariant_walk_search.py', rho_in, '0', str(sd)]
exec(open('covariant_walk_search.py').read().split("t0 = time.time()")[0])
rng = np.random.default_rng(sd)
nt = 4 * rho + 1
ts = np.arange(nt) * 2 * np.pi / nt
lines = [np.array([1, 0, 0]), np.array([1, 1, 1])]
LC = []
for d in lines:
    cols_l = []
    for v0, orb, inv in orbits:
        for B in inv:
            M = np.zeros((nt, 2, 2), complex)
            for w, U in orb.items():
                M += np.exp(-1j * ts * np.dot(d, w))[:, None, None] * (U @ B @ U.conj().T)[None]
            cols_l.append(M)
    LC.append(np.array(cols_l))
def r2(x, tau, lam=3.0):
    out = [resid(x, tau, 1.0)]
    c = unpack(x)
    for C in LC:
        d = (np.einsum('i,itab->tab', c, C) - I2[None]).ravel() * lam / np.sqrt(nt)
        out += [d.real, d.imag]
    return np.concatenate(out)
def j2(x, tau, lam=3.0):
    J = [jac(x, tau, 1.0)]
    for C in LC:
        Ja = C.reshape(len(C), -1).T * lam / np.sqrt(nt)
        JA = np.zeros((2 * Ja.shape[0], 2 * P))
        JA[:Ja.shape[0], :P] = Ja.real; JA[:Ja.shape[0], P:] = -Ja.imag
        JA[Ja.shape[0]:, :P] = Ja.imag; JA[Ja.shape[0]:, P:] = Ja.real
        J.append(JA)
    return np.vstack(J)
t0 = time.time()
for tau in [0.1, 0.5, 1.0, 1.5]:
    best = np.inf
    for s in range(nst):
        sol = least_squares(r2, rng.normal(size=2 * P) * 0.3, jac=j2, args=(tau,), method='lm',
                            xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=2000)
        best = min(best, float(np.sum(sol.fun ** 2)))
        if time.time() - t0 > 50: break
    print(f"rho={rho} zero-speed branch, tau={tau}: min residual^2 = {best:.3e}  (t={time.time()-t0:.0f}s)")
    if time.time() - t0 > 50: break
