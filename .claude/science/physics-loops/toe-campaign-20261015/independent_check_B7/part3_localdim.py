"""Part 3g: local real dimension of the nearest-site unitary covariant variety at found solutions
(22 - rank of the Jacobian of the exact-sampling residual).  NUMERICAL (SVD rank with gap check)."""
import numpy as np, sys, pickle, itertools
from walks import *
ci = int(sys.argv[1])
dat = pickle.load(open(f"nn_eqs_class{ci}.pkl", "rb")); names, Bo = dat["names"], dat["B"].astype(float)
nb = len(names)
KG = np.array(list(itertools.product(np.arange(5) * 2 * np.pi / 5, repeat=3)))
PH = np.exp(1j * KG @ np.array(OFFS).T); BK = np.einsum('kn,bnij->bkij', PH, Bo)
def resid(x):
    z = x[:nb] + 1j * x[nb:]; Wk = np.tensordot(z, BK, axes=1)
    r = (np.einsum('kji,kjl->kil', Wk.conj(), Wk) - np.eye(8)).reshape(-1)
    return np.concatenate([r.real, r.imag])
nm, sols = pickle.load(open(f"nn_solutions_class{ci}.pkl", "rb"))
from collections import Counter
cnt = Counter()
for z, spr in sols:
    x0 = np.concatenate([z.real, z.imag]); h = 1e-6
    J = np.array([(resid(x0 + h * e) - resid(x0 - h * e)) / (2 * h) for e in np.eye(2 * nb)]).T
    s = np.linalg.svd(J, compute_uv=False)
    rank = np.sum(s > 1e-6 * s[0])
    act = tuple(names[j] for j in range(nb) if abs(z[j]) > 1e-7)
    cnt[(2 * nb - rank, "dispersive" if spr > 1e-8 else "flat", act)] += 1
for k, v in sorted(cnt.items()): print(v, "solutions: local real dim", k[0], k[1], "active", k[2])
