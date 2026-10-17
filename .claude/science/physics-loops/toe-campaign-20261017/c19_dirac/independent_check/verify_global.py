"""Verify search candidates off-grid (fine grid + many local optimizations) and test the massive global gap."""
import glob, pickle
import numpy as np
from scipy.optimize import minimize
from core import *
from bases import get

rng = np.random.default_rng(0)
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4
Xb = get('X_r1'); Mb = get('Q_onsite_im_A2')
def build(t1, t2, dl, c):
    X = addm(*Xb, coeffs=list(c / np.linalg.norm(c))); nrm = max(np.abs(M).max() for M in X.values())
    return addm(hop(t1, t2), X, coeffs=[1, dl / nrm])
def doublets(H):
    e = np.linalg.eigvalsh(bloch(H, KS)); out = []; i = 0
    while i < 12:
        j = i
        while j + 1 < 12 and abs(e[j+1] - e[i]) < 1e-8: j += 1
        if j - i + 1 == 2: out.append((i, e[i]))
        i = j + 1
    return out
def extreme(F, band, sign, N=32, nref=12, nb=12):
    """sign=+1: global max of band; -1: global min.  F(ks) -> eigenvalues (batch)."""
    g = (np.arange(N) + 0.5) * 2 * np.pi / N
    KG = np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T
    KG = np.vstack([KG, KS, -KS])
    E = sign * F(KG)[:, band]          # maximize sign*E
    best = E.max(); at = KG[np.argmax(E)]
    for i in list(np.argsort(-E)[:nref]) + [None] * 4:
        k0 = KG[i] if i is not None else rng.uniform(0, 2 * np.pi, 3)
        r = minimize(lambda k: -sign * F(k[None])[0, band], k0, method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-13, maxiter=5000))
        if -r.fun > best: best, at = -r.fun, r.x
    return sign * best, at
cands = []
for f in sorted(glob.glob('global_search_*.pkl')):
    for fun, t1, x in pickle.load(open(f, 'rb')):
        if fun < 1e-3 and 10 ** x[1] > 1e-3 and abs(x[0]) > 1e-3: cands.append((fun, t1, x))
print(f"{len(cands)} nondegenerate candidates with grid badness < 1e-3")
for fun, t1, x in cands:
    t2, dl, c = x[0], 10 ** x[1], x[2:]
    H = build(t1, t2, dl, c)
    Fb = lambda ks: np.linalg.eigvalsh(bloch_batch(H, ks))
    print(f"\ncandidate t1={t1:+.0f} t2={t2:+.5f} delta={dl:.5f} (grid badness {fun:.2e}); X coefficients {np.round(c/np.linalg.norm(c), 4)}")
    E0 = np.linalg.eigvalsh(bloch(H, KS)); print("   levels at k*:", np.round(E0, 4))
    for lev, Ed in doublets(H):
        mx, kmx = extreme(Fb, lev, +1); mn, kmn = extreme(Fb, lev + 1, -1)
        dirs = rng.normal(size=(6, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
        vW = np.mean([(np.linalg.eigvalsh(bloch(H, KS + 1e-5 * d))[lev+1] - np.linalg.eigvalsh(bloch(H, KS + 1e-5 * d))[lev]) / 2e-5 for d in dirs])
        lo = extreme(Fb, lev, -1)[0]; hi = extreme(Fb, lev + 1, +1)[0]
        below = extreme(Fb, lev - 1, +1)[0] if lev > 0 else -np.inf; above = extreme(Fb, lev + 2, -1)[0] if lev + 2 < 12 else np.inf
        print(f"   doublet at level {lev}, E_d={Ed:.6f}: max band {lev} - E_d = {mx - Ed:+.2e} (at k/pi {np.round(kmx/np.pi % 2, 3)}),"
              f" E_d - min band {lev+1} = {Ed - mn:+.2e}; v_W = {vW:.4f}; band {lev} width {Ed-lo:.4f}, band {lev+1} width {hi-Ed:.4f};"
              f" gaps to neighbours: E_d - max(band {lev-1}) = {Ed-below:.4f}, min(band {lev+2}) - E_d = {above-Ed:.4f}")
        if mx - Ed < 1e-7 and Ed - mn < 1e-7:
            M = addm(*Mb, coeffs=list(rng.normal(size=len(Mb)))); nr = max(np.abs(v).max() for v in M.values()); M = {k: v / nr for k, v in M.items()}
            for m in (1e-3, 5e-3, 1e-2, 3e-2):
                Mm = {k: m * v for k, v in M.items()}
                Ff = lambda ks: np.linalg.eigvalsh(fold_batch(H, Mm, ks))
                e = np.linalg.eigvalsh(fold(H, Mm, KS)); mD = (e[2 * lev + 2] - e[2 * lev + 1]) / 2
                top = extreme(Ff, 2 * lev + 1, +1, N=20, nref=8)[0]; bot = extreme(Ff, 2 * lev + 2, -1, N=20, nref=8)[0]
                print(f"      mass m={m:.0e}: m_D = {mD:.5f}; global gap min(folded band {2*lev+2}) - max(folded band {2*lev+1}) = {bot-top:.5f}  (2 m_D = {2*mD:.5f}; ratio {(bot-top)/(2*mD):.4f})")
