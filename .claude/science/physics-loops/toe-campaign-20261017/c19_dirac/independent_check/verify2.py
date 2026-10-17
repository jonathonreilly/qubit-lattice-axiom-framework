"""Verify second-search candidates: fine extremes of bands lev, lev+1 vs E_d; extra touchings; massive
global gap (folded bands 2lev+1, 2lev+2) vs 2 m_D."""
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
N = 28; g = (np.arange(N) + 0.37) * 2 * np.pi / N
KG = np.vstack([np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T, KS, -KS])
def ext(F, band, sign, nref=10):
    E = sign * F(KG)[:, band]; best = E.max()
    for i in np.argsort(-E)[:nref]:
        r = minimize(lambda k: -sign * F(k[None])[0, band], KG[i], method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-14, maxiter=6000))
        best = max(best, -r.fun)
    return sign * best
M = addm(*Mb, coeffs=list(rng.normal(size=len(Mb)))); nr = max(np.abs(v).max() for v in M.values()); M = {k: v / nr for k, v in M.items()}
for f in sorted(glob.glob('search2_*.pkl')):
    for fun, t1, x in pickle.load(open(f, 'rb')):
        H = build(t1, x[0], 10 ** x[1], x[2:]); F = lambda ks: np.linalg.eigvalsh(bloch_batch(H, ks))
        print(f"\n{f}: t1={t1:+.0f} t2={x[0]:+.5f} delta={10**x[1]:.5f} grid badness {fun:.2e}")
        for lev, Ed in doublets(H):
            mx = ext(F, lev, +1); mn = ext(F, lev + 1, -1)
            gl = Ed - ext(F, lev - 1, +1) if lev > 0 else np.inf; gu = ext(F, lev + 2, -1) - Ed if lev < 10 else np.inf
            dirs = rng.normal(size=(6, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
            vW = np.mean([np.diff(np.linalg.eigvalsh(bloch(H, KS + 1e-5 * d))[lev:lev+2])[0] / 2e-5 for d in dirs])
            print(f"   doublet lev {lev} E_d={Ed:+.5f}: max(band {lev}) - E_d = {mx-Ed:+.2e}; E_d - min(band {lev+1}) = {Ed-mn:+.2e}; v_W={vW:.4f};"
                  f" separation from band {lev-1}: {gl:.4f}, from band {lev+2}: {gu:.4f}")
            if mx - Ed < 1e-6 and Ed - mn < 1e-6:
                # touchings away from +-k*
                gap = F(KG)[:, lev + 1] - F(KG)[:, lev]; tch = []
                for i in np.argsort(gap)[:30]:
                    r = minimize(lambda k: np.diff(np.linalg.eigvalsh(bloch(H, k))[lev:lev+2])[0], KG[i], method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-14, maxiter=6000))
                    d = min(np.linalg.norm((r.x - q + np.pi) % (2*np.pi) - np.pi) for q in (KS, -KS))
                    if r.fun < 1e-6 and d > 1e-2: tch.append(np.linalg.eigvalsh(bloch(H, r.x))[lev] - Ed)
                print(f"      extra touchings of bands {lev},{lev+1}: {len(tch)} (E - E_d: {np.round(sorted(set(np.round(tch, 6))), 5)})")
                for m in (1e-3, 3e-3, 1e-2, 3e-2):
                    Mm = {k: m * v for k, v in M.items()}; Ff = lambda ks: np.linalg.eigvalsh(fold_batch(H, Mm, ks))
                    e = np.linalg.eigvalsh(fold(H, Mm, KS)); mD = (e[2*lev + 2] - e[2*lev + 1]) / 2
                    gg = ext(Ff, 2*lev + 2, -1, 6) - ext(Ff, 2*lev + 1, +1, 6)
                    print(f"      m={m:.0e}: m_D={mD:.3e}; global gap {gg:+.3e}; 2 m_D = {2*mD:.3e}; ratio {gg/(2*mD):.4f}")
