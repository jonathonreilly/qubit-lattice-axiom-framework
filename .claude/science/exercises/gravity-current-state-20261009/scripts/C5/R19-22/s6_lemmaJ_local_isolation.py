"""R19-22 s6 (added 06:41Z, before running): Lemma J's rank step is LOCAL?
For each of the 6 slot types at a central site of an L=6 torus, test whether the unit vector e_a is an exact linear
combination of double-commutator rows (D_q and D_p separately) whose supports lie within Chebyshev distance 2 of
that site. If yes for all 6 types, the left inverse is finitely supported and Lemma J holds on the infinite lattice
and on any box containing the neighbourhood (no wrap-around used)."""
import numpy as np, importlib.util, os
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "s3_hp_constraint_algebra.py")).read().split("for L in [3, 4, 5]:")[0]
ns = {}; exec(src, ns); stencils = ns['stencils']
L = 6; G, Sm = stencils(L); nslot = G.shape[1]
c0 = np.array([3, 3, 3]); sites = [tuple(s) for s in np.ndindex(L, L, L)]
def site_of_slot(a): return np.array(sites[a//6])
def near(vec, R=2):
    nz = np.nonzero(vec)[0]
    return all(np.max(np.abs(site_of_slot(a) - c0)) <= R for a in nz)
rowsQ, rowsP = [], []
for e in range(G.shape[0]):
    nz = np.nonzero(G[e])[0]
    if not near(G[e], 3): continue
    ys = np.unique(np.nonzero(Sm[:, nz])[0]); es = np.unique(np.nonzero(G[:, nz])[0])
    for y in ys:
        for e2 in es:
            v = G[e]*G[e2]*Sm[y]
            if v.any() and near(v): rowsQ.append(v)
        for y2 in ys:
            v = G[e]*Sm[y]*Sm[y2]
            if v.any() and near(v): rowsP.append(v)
DQ = np.array(rowsQ, float).T; DP = np.array(rowsP, float).T
sid0 = sites.index(tuple(c0))
for name, D in [("D_q", DQ), ("D_p", DP)]:
    res = []
    for t in range(6):
        ea = np.zeros(nslot); ea[6*sid0 + t] = 1
        coef, *_ = np.linalg.lstsq(D, ea, rcond=None)
        res.append(np.abs(D@coef - ea).max())
    print(f"{name}: {D.shape[1]} local rows; max residual isolating each of the 6 central slot types = {np.round(res, 12)}")
