"""Part 3c: restricted-support ansatz search (NUMERICAL): only the listed hop-type orbits may be nonzero.
Used to test, for the spinorial class, the active sets on which the bosonic class has dispersive
solutions.  Reports best unitarity residual reached and dispersion of any unitary solution."""
import numpy as np, sys, pickle, itertools
from scipy.optimize import least_squares
from walks import *
ci = int(sys.argv[1]); act = sys.argv[2].split(","); nstart = int(sys.argv[3])
dat = pickle.load(open(f"nn_eqs_class{ci}.pkl", "rb"))
names, Bo = dat["names"], dat["B"].astype(float)
sel = [names.index(a) for a in act]; Bs = Bo[sel]; nb = len(sel)
KG = np.array(list(itertools.product(np.arange(5) * 2 * np.pi / 5, repeat=3)))
PH = np.exp(1j * KG @ np.array(OFFS).T)
BK = np.einsum('kn,bnij->bkij', PH, Bs)
def resid(x):
    z = x[:nb] + 1j * x[nb:]
    Wk = np.tensordot(z, BK, axes=1)
    r = (np.einsum('kji,kjl->kil', Wk.conj(), Wk) - np.eye(8)).reshape(-1)
    return np.concatenate([r.real, r.imag])
rng = np.random.default_rng(3)
best = 1e9; nsol = 0; maxsp = 0
for s in range(nstart):
    r = least_squares(resid, rng.normal(size=2 * nb) * 0.4, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=3000)
    F = np.sum(r.fun ** 2); best = min(best, F)
    if F < 1e-22:
        z = r.x[:nb] + 1j * r.x[nb:]; A = np.tensordot(z, Bs, axes=1)
        rk = np.random.default_rng(0).uniform(-np.pi, np.pi, (30, 3))
        c = np.array([np.poly(symbol(A, k)) for k in rk]); sp = np.abs(c - c[0]).max()
        nsol += 1; maxsp = max(maxsp, sp)
        actv = [act[j] for j in range(nb) if abs(z[j]) > 1e-7]
        print(f"  sol: spread {sp:.2e} active {actv}", flush=True)
print(f"class {ci} ansatz {act}: {nsol}/{nstart} unitary; best residual {best:.2e}; max spread {maxsp:.2e}")
