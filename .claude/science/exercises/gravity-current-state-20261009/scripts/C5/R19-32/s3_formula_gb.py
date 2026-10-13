"""R19-32 s3 (pre-registered 07:37Z): probe (b),(c) for FORMULA lowering parts (CCR Bogoliubov coefficients built from
truncated slot operators; R19-25 s4's definition) in the covariant model on the 1x1xL slice, sector by sector.
On the slice V_total = V_scal (x) V_vecx (x) V_vecy (x) [full TT space] (TT never enters a constraint, s1(4)), so an empty
vector sector empties the whole physical space.
Per case: dim V = dim cap_{k: w_k>0, n} ker D_n(k) (computed in the two total-parity sectors; each D flips parity),
the smallest singular value of the stacked D (best approximate physical state residual), and if V != 0: Krein inertia of V,
quotient dim/signature, and H-leak ||(1-P_V) H P_V|| / ||H P_V||.
Expectation (registered): KREIN-EMPTY when Bogoliubov-mixed. Added prediction (07:37Z, from the proved s2 formula):
 lowering parts commute exactly iff one constrained frequency (L<=2 AP, L<=3 periodic); with nu = that frequency, v = 0
 (pure slot lowering) and V contains the slot vacuum at every d.
"""
import numpy as np, scipy.sparse as sp, scipy.linalg as sl, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from mb import *

def kernel_info(S):
    Ds = S.constraints()
    par = np.zeros(S.dim, int); idx = np.arange(S.dim)
    for s in range(S.ns): par += (idx // S.d**(S.ns - s - 1)) % S.d
    par %= 2
    Vs = []; smins = []
    for p in (0, 1):
        cols = np.where(par == p)[0]; rows = np.where(par != p)[0]
        M = sp.vstack([D[rows][:, cols] for D in Ds]).tocsr()
        if len(cols) <= 4500:
            Md = M.toarray(); s, vh = None, None
            try:
                u, s, vh = np.linalg.svd(Md, full_matrices=True)
            except np.linalg.LinAlgError:
                u, s, vh = sl.svd(Md, full_matrices=True, lapack_driver='gesvd')
            s_full = np.zeros(len(cols)); s_full[:len(s)] = s
            tol = 1e-9*max(1., s.max())
            ker = vh[(s_full > tol).sum():].conj().T if len(s) >= len(cols) else vh[(s > tol).sum():].conj().T
            smins.append(s_full.min())
        else:
            Hm = (M.conj().T@M).toarray()
            ev, U = np.linalg.eigh(Hm)
            tol = 1e-16*max(1., ev.max())
            ker = U[:, ev <= tol]; smins.append(np.sqrt(max(ev.min(), 0)))
        Vfull = np.zeros((S.dim, ker.shape[1]), complex); Vfull[cols] = ker; Vs.append(Vfull)
    V = np.hstack(Vs)
    out = dict(dimV=V.shape[1], smin=min(smins))
    if V.shape[1]:
        Gram = V.conj().T@(S.eta[:, None]*V); Gram = (Gram + Gram.conj().T)/2
        ev = np.linalg.eigvalsh(Gram); tol = 1e-8
        out['inertia'] = (int((ev > tol).sum()), int((ev < -tol).sum()), int((abs(ev) <= tol).sum()))
        out['nonnull'] = np.sort(ev[abs(ev) > tol])[:6]
        HV = S.H@V; out['leakH'] = np.linalg.norm(HV - V@(V.conj().T@HV), 2)/max(1e-300, np.linalg.norm(HV, 2))
    return out

cases = []
for d in range(2, 13): cases.append(('vecx', 1, -1, d))
for d in range(2, 9): cases.append(('vecx', 2, -1, d))
for d in range(2, 5): cases.append(("vecx", 3, 1, d))
for d in range(2, 6): cases.append(('vecx', 3, -1, d))
for d in range(2, 4): cases.append(('vecx', 4, -1, d))
for d in range(2, 7): cases.append(("scal", 1, -1, d))
for d in range(2, 4): cases.append(("scal", 2, -1, d))
which = sys.argv[1] if len(sys.argv) > 1 else 'all'
for (sec, L, tw, d) in cases:
    if which != 'all' and which != f"{sec}{L}{tw}": continue
    S0 = Sector(sec, L, 2, 1.0, tw)
    wpos = sorted(set(np.round([w for w in S0.ws if w > 1e-12], 10)))
    for nu in [1.0] + [w for w in wpos if abs(w - 1) > 1e-9]:
        t0 = time.time(); S = Sector(sec, L, d, nu, tw); o = kernel_info(S)
        line = f"{sec} L={L} {'AP' if tw<0 else 'P '} d={d:2d} nu={nu:.4f} (freqs {np.round(wpos,4)}; mixing={'no' if (len(wpos)==1 and abs(nu-wpos[0])<1e-9) else 'yes'}): dim {S.dim}; dim V = {o['dimV']}; min sing = {o['smin']:.3e}"
        if o['dimV']: line += f"; inertia {o['inertia']}, quotient (+,-) = {o['inertia'][:2]}, smallest nonnull Gram {np.round(o['nonnull'],4)}, H-leak {o['leakH']:.2e}"
        print(line + f"  [{time.time()-t0:.1f}s]", flush=True)
