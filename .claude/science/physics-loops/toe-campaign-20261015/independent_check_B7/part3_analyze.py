"""Part 3b: re-find nearest-site unitary covariant walks (least squares, NUMERICAL), decode each into
the exact orbit coefficients c_type (hop types relative to a corner: i=inward, o=outward, 0 per axis),
save them, report which hop types are active and whether the spectrum disperses."""
import numpy as np, sys, pickle, itertools
from scipy.optimize import least_squares
from walks import *
ci = int(sys.argv[1]); nstart = int(sys.argv[2])
D = class_D(ci)
dat = pickle.load(open(f"nn_eqs_class{ci}.pkl", "rb"))
names, Bo = dat["names"], dat["B"].astype(float)       # orbit basis, entries 0,+-1
nb = len(names)
KG = np.array(list(itertools.product(np.arange(5) * 2 * np.pi / 5, repeat=3)))
PH = np.exp(1j * KG @ np.array(OFFS).T)
BK = np.einsum('kn,bnij->bkij', PH, Bo)
def resid(x):
    z = x[:nb] + 1j * x[nb:]
    Wk = np.tensordot(z, BK, axes=1)
    r = (np.einsum('kji,kjl->kil', Wk.conj(), Wk) - np.eye(8)).reshape(-1)
    return np.concatenate([r.real, r.imag])
def cps(A, nk=40):
    rng = np.random.default_rng(0)
    c = np.array([np.poly(symbol(A, k)) for k in rng.uniform(-np.pi, np.pi, (nk, 3))])
    return np.abs(c - c[0]).max()
rng = np.random.default_rng(int(sys.argv[3]) if len(sys.argv) > 3 else 1)
out = []
for s in range(nstart):
    x0 = rng.normal(size=2 * nb) * rng.uniform(0.1, 0.6)
    r = least_squares(resid, x0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=3000)
    if np.sum(r.fun ** 2) < 1e-22:
        z = r.x[:nb] + 1j * r.x[nb:]
        A = np.tensordot(z, Bo, axes=1)
        sp = cps(A)
        act = [names[j] for j in range(nb) if abs(z[j]) > 1e-7]
        print(f"start {s}: spread {sp:.2e} cov {covariance_defect(A, D):.1e} unit {unitarity_defect(A):.1e} active {act}", flush=True)
        print("    |c| =", {names[j]: round(abs(z[j]), 5) for j in range(nb) if abs(z[j]) > 1e-7}, flush=True)
        out.append((z, sp))
pickle.dump((names, out), open(f"nn_solutions_class{ci}.pkl", "wb"))
