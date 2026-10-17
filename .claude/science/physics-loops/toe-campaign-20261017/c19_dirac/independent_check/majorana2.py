"""Majorana masses, proper gap test (Bloch BdG; conventions and the real-space cross-check are in
majorana.py / majorana.log).  Small pairing amplitude; search for BdG zero modes in a ball of radius
~8 Delta/v_W around k* by local minimization of the smallest |E| from many starts."""
import os, pickle
import numpy as np
from scipy.optimize import minimize
from core import *
from bases import get
from invspace import invariant_basis, shifts

rng = np.random.default_rng(9)
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4
Xb = get('X_r1')
def rnd(bs, cplx=False):
    c = rng.normal(size=len(bs)) + (1j * rng.normal(size=len(bs)) if cplx else 0); m = addm(*bs, coeffs=list(c))
    nrm = max(np.abs(M).max() for M in m.values()); return {k: v / nrm for k, v in m.items()}
Hb = addm(hop(-1.0, 0.2), rnd(Xb), coeffs=[1, 0.05])
EN = np.linalg.eigvalsh(bloch(Hb, KS))[0]
dirs = rng.normal(size=(8, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
vW = np.mean([(np.linalg.eigvalsh(bloch(Hb, KS + 1e-5 * d))[1] - np.linalg.eigvalsh(bloch(Hb, KS + 1e-5 * d))[0]) / 2e-5 for d in dirs])
print(f"E_N = {EN:.6f}, v_W = {vW:.5f}")
CP = 'pair_bases.pkl'
db = pickle.load(open(CP, 'rb')) if os.path.exists(CP) else {}
def pair_basis(S, P, tw):
    key = (S, P, tw)
    if key not in db:
        idx, b = invariant_basis(shifts(S), stag=(P == 'Q'), imag=True, chiA2=1 if tw else 0, with_inv=False)
        out = []
        for v in b:
            m = {}
            for (sh, c2, c1), i in idx.items():
                if v[i]: m.setdefault(sh, np.zeros((12, 12), complex))[c2, c1] += v[i]
            out.append(m)
        db[key] = out; pickle.dump(db, open(CP, 'wb'))
    return db[key]
def Dk(d, P, k):
    Pv = Q if P == 'Q' else np.zeros(3); out = np.zeros((12, 12), complex)
    for sh, M in d.items(): out += M * np.exp(-1j * (Pv - k) @ np.array(sh))
    return out
def bdg(d, P, k, amp):
    Pv = Q if P == 'Q' else np.zeros(3); X = -amp * Dk(d, P, k).T
    A = bloch(Hb, k) - EN * np.eye(12); B = bloch(Hb, Pv - k) - EN * np.eye(12)
    return np.block([[A, X], [X.conj().T, -B.T]])
def minE(d, P, amp, R, nstart=30):
    f = lambda q: np.abs(np.linalg.eigvalsh(bdg(d, P, KS + q, amp))).min()
    best = f(np.zeros(3)); at = 0.0
    for _ in range(nstart):
        q0 = rng.normal(size=3); q0 *= R * rng.random() ** (1 / 3) / np.linalg.norm(q0)
        r = minimize(f, q0, method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-12, maxiter=3000))
        if np.linalg.norm(r.x) < 2 * R and r.fun < best: best, at = r.fun, np.linalg.norm(r.x)
    return best, at, f(np.zeros(3))
for S in ('onsite', 'r1'):
    for P in ('0', 'Q'):
        for tw in (True, False):
            bs = pair_basis(S, P, tw)
            for trial in range(2):
                d = rnd(bs, cplx=True)
                for amp in (1e-3, 3e-3):
                    # first-order node-space pairing: <node| D(k*) |node>
                    e, V = np.linalg.eigh(bloch(Hb, KS)); Vn = V[:, :2]
                    Pv = Q if P == 'Q' else np.zeros(3)
                    e2, V2 = np.linalg.eigh(bloch(Hb, Pv - KS)); Vn2 = V2[:, :2]
                    blk = Vn.conj().T @ (-amp * Dk(d, P, KS).T) @ Vn2.conj()
                    sv = np.linalg.svd(blk, compute_uv=False)
                    R = 8 * max(sv.max(), amp) / vW
                    b, at, at0 = minE(d, P, amp, R)
                    print(f"{S:6s} P={P} {'twisted ' if tw else 'untwist.'}-inv (dim {len(bs):2d}) #{trial} amp {amp:.0e}: node pairing sv {np.round(sv, 6)};"
                          f" min|E_BdG| in ball R={R:.3f}: {b:.2e} at |q|={at:.4f} (|E| at k*: {at0:.2e})")
