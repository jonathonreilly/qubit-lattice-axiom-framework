"""side check: which positions of a C2[110] axis give the TM1 column relative to the site-centred C3[111]?
x -> R x + t with R = C2[110]; the axis passes through c iff t = c - R c. Image on bilinears is defined up to T(1,1,1) = -1."""
import itertools, numpy as np
from t4_core import *
for c in [(0,0,0),(0,0,.5),(0,1,0),(1,0,0),(0,0,1),(.5,.5,0),(.5,0,0),(0,.5,.5),(1,1,0),(.5,-.5,0)]:
    c = np.array(c, float); t = c - R110 @ c
    if not np.allclose(t, np.round(t)): print(f"axis through {c}: t={t} not a lattice translation"); continue
    g = rep_tr(np.round(t).astype(int)) @ rep_rot(R110)
    w, V = np.linalg.eig(g); w = np.round(w.real, 8); vals, cnt = np.unique(w, return_counts=True)
    u = V[:, list(w).index(vals[cnt == 1][0])]; col = np.sort(np.abs(FOUR.conj().T @ u) ** 2)
    kind = 'site' if np.allclose(c, np.round(c)) else 'non-site'
    print(f"axis [110] through {c} ({kind}): translation part {np.round(t).astype(int)}, image {g.tolist()}, fixed column {col.round(4)}")
