"""Part 3d: exhaustive search for EXACT nearest-site covariant unitary walks with all hop amplitudes in
(1/4){+-1,+-i} on a prescribed set of hop-type orbits (others zero).  Unitarity checked exactly in
Gaussian-integer arithmetic (sum_n A_n^dag A_{n+d} = 16 delta I for 4A).  Then dispersion check."""
import numpy as np, sys, pickle, itertools
from walks import *
ci = int(sys.argv[1]); act = sys.argv[2].split(",")
dat = pickle.load(open(f"nn_eqs_class{ci}.pkl", "rb"))
names, Bo = dat["names"], dat["B"].astype(int)
sel = [names.index(a) for a in act]
DS = [np.array(d) for d in itertools.product(range(-2, 3), repeat=3)]
def is_unitary(A4):   # A4 = 4A, Gaussian-integer entries
    for d in DS:
        S = np.zeros((8, 8), complex)
        for i, n in enumerate(OFFS):
            j = OIDX.get(tuple(n + d))
            if j is not None: S += A4[i].conj().T @ A4[j]
        if not d.any(): S -= 16 * np.eye(8)
        if np.abs(S).max() > 1e-9: return False
    return True
ph = [1, 1j, -1, -1j]
sols = []
for combo in itertools.product(range(4), repeat=len(sel) - 1):
    z = [1] + [ph[c] for c in combo]        # global phase fixed
    A4 = sum(z[t] * Bo[sel[t]] for t in range(len(sel))).astype(complex)
    if is_unitary(A4):
        sols.append(z)
print(f"class {ci}, active {act}: {len(sols)} exact unitary phase patterns (global phase fixed)")
for z in sols[:8]:
    A = sum(z[t] * Bo[sel[t]] for t in range(len(sel))) / 4
    rk = np.random.default_rng(0).uniform(-np.pi, np.pi, (30, 3))
    c = np.array([np.poly(symbol(A, k)) for k in rk])
    print("  phases", dict(zip(act, [str(x) for x in z])), " charpoly spread", f"{np.abs(c-c[0]).max():.3e}",
          " max site displacement", site_disp_max(A), " cov defect", covariance_defect(A, class_D(ci)))
if sols:
    pickle.dump((act, sols), open(f"exact_nn_class{ci}.pkl", "wb"))
