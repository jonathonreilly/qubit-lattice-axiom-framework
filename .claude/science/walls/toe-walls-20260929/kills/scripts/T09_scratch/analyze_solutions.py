"""T09 Test 1b: for the exactly covariant unitary ticks found at s=6 (A1+E+T1), classify the band structure:
number of flat bands, isotropic cone at a degenerate point, curved (massive) bands."""
import sys
import numpy as np
from scipy.optimize import least_squares
from common import *
import census

names = sys.argv[1].split('+') if len(sys.argv) > 1 else ['A1', 'E', 'T1']
s, n0, nN, B, G = census.setup(names)
nb = n0 + nN
I = np.eye(s)
rng = np.random.default_rng(7)

def res_factory(tau):
    def res(x):
        c = x[:nb] + 1j * x[nb:]
        U = np.einsum('j,jkab->kab', c, B)
        R = np.einsum('kba,kbc->kac', U.conj(), U) - I[None]
        cn = c[n0:]
        return np.concatenate([R.real.ravel(), R.imag.ravel(), [np.real(cn.conj() @ G @ cn) - tau]])
    return res

def to_A(x):
    c = x[:nb] + 1j * x[nb:]
    s_, b0, bN = covariant_basis(names)
    return build_A(s, b0, bN, c[:n0], c[n0:])

sols = []
for tau in (0.5, 1.0, 2.0, 3.0, 4.5, 5.5):
    res = res_factory(tau)
    for t in range(12):
        x0 = rng.normal(size=2 * nb) * 0.7
        sol = least_squares(res, x0, method='lm', xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=1500)
        if np.linalg.norm(sol.fun) < 1e-10:
            sols.append((tau, sol.x))
print('found', len(sols), 'unitary covariant ticks; analysing')

def analyse(x):
    A0, A = to_A(x)
    # rotational covariance check on random k: U(Rk) vs rho U(k) rho^dag (using found structure implicitly) -> skip
    # unitary check
    kk = rng.uniform(-np.pi, np.pi, size=(50, 3))
    ud = max(np.linalg.norm(U_of_k(A0, A, k).conj().T @ U_of_k(A0, A, k) - np.eye(s)) for k in kk)
    # flat band count: eigenphase spread of each band over random k (sorted eigenphases)
    ph = np.array([np.sort(np.angle(np.linalg.eigvals(U_of_k(A0, A, k)))) for k in kk])
    # tr U(k) constant? flat bands <=> repeated spectrum
    # small-k spectrum
    U0 = U_of_k(A0, A, np.zeros(3))
    ph0 = np.sort(np.angle(np.linalg.eigvals(U0)))
    speeds = {}
    for name, d in (('100', [1, 0, 0]), ('110', [1, 1, 0]), ('111', [1, 1, 1])):
        d = np.array(d, float); d /= np.linalg.norm(d)
        e = 1e-3
        lam0 = np.linalg.eigvals(U0)
        lamk = np.linalg.eigvals(U_of_k(A0, A, e * d))
        dd = np.array([np.min(np.abs(l - lam0)) for l in lamk])
        speeds[name] = np.round(np.sort(dd) / e, 3)
    return ud, ph0, speeds, ph

flat_counts = []
n_show = 0
for tau, x in sols:
    ud, ph0, sp, ph = analyse(x)
    # bands whose eigenphase does not vary over random k: sorted eigenphases variance per index (crude; crossings)
    var = ph.std(axis=0)
    nflat = int(np.sum(var < 1e-6))
    flat_counts.append(nflat)
    if n_show < 6:
        n_show += 1
        print(f'tau={tau}: unitary defect {ud:.1e}; eigenphases at k=0: {np.round(ph0, 3)}; #flat sorted-band slots: {nflat}')
        for k_, v in sp.items():
            print('     |d phase|/k along', k_, ':', v)
print('flat-band slot counts over solutions:', sorted(set(flat_counts)))
