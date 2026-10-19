"""T-F3 task 1: counts of G-allowed cross operators (character formula over B3)."""
import numpy as np
from t4_core import *
def rep(proj):
    basis = []
    for i in range(3):
        for j in range(3):
            E = np.zeros((3, 3)); E[i, j] = 1; basis.append(proj(E).ravel())
    U, S, Vt = np.linalg.svd(np.array(basis)); Vb = Vt[:int((S > 1e-10).sum())]
    return [Vb @ np.array([act(g, v.reshape(3, 3)).ravel() for v in Vb]).T for g in B3]
R = {nm: rep(pr) for nm, pr in PROJ.items()}
idx = {tuple(g.ravel()): i for i, g in enumerate(B3)}
sq = [idx[tuple((g @ g).ravel())] for g in B3]
def ch(content):   # content: dict irrep -> real copies
    return np.array([sum(n * np.trace(R[r][k]) for r, n in content.items()) for k in range(len(B3))])
Vl = {'A1': 2, '3M': 2, "3M'": 2}; Vn = {'A1': 2, 'E': 2, '3M': 2}
Vl_noA1 = {'3M': 2, "3M'": 2}; Vn_noA1 = {'E': 2, '3M': 2}
Dirac = {'A1': 1, 'E': 1, '3M': 1, "3M'": 1}; Maj = {'A1': 1, 'E': 1, '3M': 1}
def hom(chs, target):
    return int(round(np.mean(np.prod(chs, 0) * ch(target))))
def S2(c): return (c ** 2 + c[sq]) / 2
cl, cn, cl0, cn0 = ch(Vl), ch(Vn), ch(Vl_noA1), ch(Vn_noA1)
print("linear insertions (complex couplings): phi_nu -> M_l:", hom([cn], Dirac), "; phi_l -> M_nu:", hom([cl], Maj),
      " [without A1 parts:", hom([cn0], Dirac), ",", hom([cl0], Maj), "]")
print("phi_l(x)phi_l -> M_nu at second order (no phi_nu at all):", hom([S2(cl)], Maj), " ; phi_nu(x)phi_nu -> M_l:", hom([S2(cn)], Dirac))
print("trilinear shaping-proof: phi_l (x) S2(phi_nu) -> M_l:", hom([cl, S2(cn)], Dirac), " ; phi_nu (x) S2(phi_l) -> M_nu:", hom([cn, S2(cl)], Maj))
print("   (without A1 parts:", hom([cl0, S2(cn0)], Dirac), ",", hom([cn0, S2(cl0)], Maj), ")")
print("within-sector for comparison: phi_l -> M_l:", hom([cl], Dirac), "; phi_l (x) S2 phi_l -> M_l:", hom([cl, S2(cl)], Dirac))
