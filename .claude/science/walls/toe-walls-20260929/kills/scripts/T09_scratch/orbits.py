"""T09 Test 1c: same census but with a general displacement support (orbits of the 24 rotations):
 cross (6), face diagonals (12), body diagonals (8), full 27-cube.  Spin-1/2 (H1) and H2, s=2, plus H1+H1 (s=4)."""
import sys, numpy as np
from scipy.linalg import null_space
from scipy.optimize import least_squares
from common import *

def orbit(d):
    out = []
    for R in ROTS:
        v = tuple(int(x) for x in np.round(R @ np.array(d, float)))
        if v not in out: out.append(v)
    return out

def cov_basis_orbits(names, reps):
    s = sum(IRREP_DIM[n] for n in names)
    rho = [rep_matrix(names, R) for R in ROTS]
    cons = [np.kron(r, r.conj()) - np.eye(s * s) for r in rho]
    N0 = null_space(np.vstack(cons))
    basis0 = [N0[:, j].reshape(s, s) for j in range(N0.shape[1])]
    basisN = []          # each: dict displacement -> matrix
    for d in reps:
        d = np.array(d, float)
        stab = [i for i, R in enumerate(ROTS) if np.allclose(R @ d, d)]
        Nd = null_space(np.vstack([np.kron(rho[i], rho[i].conj()) - np.eye(s * s) for i in stab]))
        for j in range(Nd.shape[1]):
            Ad = Nd[:, j].reshape(s, s)
            m = {}
            for i, R in enumerate(ROTS):
                v = tuple(int(x) for x in np.round(R @ d))
                m[v] = rho[i] @ Ad @ rho[i].conj().T
            basisN.append(m)
    return s, basis0, basisN

def run(names, support_name, reps, tau_list, nstarts, seed=1):
    s, b0, bN = cov_basis_orbits(names, reps)
    rng = np.random.default_rng(seed)
    KS = rng.uniform(-np.pi, np.pi, size=(30, 3))
    n0, nN = len(b0), len(bN)
    disp = sorted({v for m in bN for v in m})
    nb = n0 + nN
    B = np.zeros((nb, len(KS), s, s), complex)
    for j, b in enumerate(b0): B[j] = b[None]
    for j, m in enumerate(bN):
        for v, M in m.items():
            B[n0 + j] += np.exp(1j * (KS @ np.array(v, float)))[:, None, None] * M[None]
    G = np.zeros((nN, nN), complex)
    for a, ma in enumerate(bN):
        for b, mb in enumerate(bN):
            G[a, b] = sum(np.trace(ma[v].conj().T @ mb[v]) for v in ma if v in mb)
    I = np.eye(s)
    best = 1e9; nsol = 0
    for tau in tau_list:
        def res(x):
            c = x[:nb] + 1j * x[nb:]
            U = np.einsum('j,jkab->kab', c, B)
            R = np.einsum('kba,kbc->kac', U.conj(), U) - I[None]
            cn = c[n0:]
            return np.concatenate([R.real.ravel(), R.imag.ravel(), [np.real(cn.conj() @ G @ cn) - tau]])
        for t in range(nstarts):
            sol = least_squares(res, rng.normal(size=2 * nb) * 0.7, method='lm', xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=1500)
            c = np.linalg.norm(sol.fun)
            best = min(best, c)
            if c < 1e-9: nsol += 1
    print(f"{'+'.join(names):8s} s={s} support={support_name:14s} #disp={len(disp):2d} dimA0={n0} dimAd={nN}  best_cost={best:.1e} n_solutions={nsol}", flush=True)
    return best, nsol

face = [(1, 1, 0)]
body = [(1, 1, 1)]
cross = [(1, 0, 0)]
supports = {'cross(6)': cross, 'body diag(8)': body, 'face diag(12)': face,
            'cross+body(14)': cross + body, 'cube27': cross + face + body}
if __name__ == '__main__':
    for names in (['H1'], ['H2']):
        for sname, reps in supports.items():
            run(names, sname, reps, (0.4, 1.0, 1.7), 10)
