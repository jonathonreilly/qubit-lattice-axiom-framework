import sys, pickle, itertools, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
from rp import rp_matrix
D = pickle.load(open('d4.pkl', 'rb')); tix = {t: i for i, t in enumerate(D.types)}
# real-space P1 couplings between distinct vertices (sum over simplices of vol grad_i . grad_j)
coup = {}
for vs in D.simp:
    P = np.array([D.pos(v) for v in vs]); E = P[1:] - P[0]; vol = abs(np.linalg.det(E))/24; Ei = np.linalg.inv(E)
    gl = [-(Ei.sum(axis=1))] + [Ei[:, i] for i in range(4)]
    for i, j in itertools.combinations(range(5), 2):
        key, _ = RG._key_pair(vs[i], vs[j]); coup[key] = coup.get(key, 0.0) + vol*gl[i] @ gl[j]
vals = np.array(list(coup.values()))
pos = [(k, v) for k, v in coup.items() if v > 1e-12]
print(f"P1 couplings: {len(vals)} edge classes; negative (ferromagnetic) {int((vals < -1e-12).sum())}, zero {int((abs(vals) <= 1e-12).sum())}, positive {len(pos)}")
for k, v in pos[:6]:
    t1, t2, rel = k; print("   positive:", D.OFF[t1], "->", np.array(rel) + D.OFF[t2], f"{v:+.4f}")
