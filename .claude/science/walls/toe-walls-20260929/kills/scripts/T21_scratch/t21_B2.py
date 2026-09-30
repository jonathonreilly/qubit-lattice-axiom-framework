"""Test B2: separate localized in-gap (defect) states from the extended band edge, via IPR."""
import sys, time
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from t21_common import *

L = int(sys.argv[1]); nsamp = int(sys.argv[2]); cs = [float(x) for x in sys.argv[3].split(',')]
gs = [float(x) for x in sys.argv[4].split(',')]
N = L ** 3
nb = neighbours(L)
eps = eps_array(L).astype(np.int8)
H0 = walker_H0(L)
print(f"L={L} N={N} samples={nsamp} c={cs} g={gs}; localized := IPR*N > 10")
def analyse(n, c):
    d = np.repeat(n.astype(float), 2) * c
    E, V = np.linalg.eigh(H0 + np.diag(d))
    rho = (np.abs(V) ** 2).reshape(N, 2, -1).sum(axis=1)   # site density of each eigenvector, (N, 2N)
    ipr = (rho ** 2).sum(axis=0) * N
    loc = ipr > 10
    inwin = (E > 0.1 * c) & (E < 0.9 * c)
    n_loc_in = int((loc & inwin).sum())
    n_ext_in = int((~loc & inwin).sum())
    ext = ~loc
    dext = np.min(np.abs(E[ext] - 0.5 * c)) if ext.any() else np.nan
    return n_loc_in, n_ext_in, dext
for g in gs:
    K = np.log(1.0 / g) / 4.0
    pbond = 1.0 - np.exp(-2.0 * K)
    seed_numba(999 + int(1000 * g))
    sig = np.ones(N, dtype=np.int8)
    wolff_steps(sig, nb, pbond, 500, 0)
    samples = []
    for _ in range(nsamp):
        wolff_steps(sig, nb, pbond, 40, 0)
        s = sig.copy()
        if s.sum() < 0: s = -s
        samples.append(s)
    nflip = np.mean([(s == -1).sum() for s in samples])
    for c in cs:
        rows = np.array([analyse((1 + eps * s) // 2, c) for s in samples], float)
        nfl = np.array([(s == -1).sum() for s in samples], float)
        print(f"g={g:.3f} c={c:.1f} flipped sites/sample={nflip:.1f} | localized in-gap states: med={np.median(rows[:,0]):.0f} "
              f"(per flipped site {np.median(rows[:,0]/np.maximum(nfl,1)):.2f}) | extended in-gap: med={np.median(rows[:,1]):.0f} max={rows[:,1].max():.0f} "
              f"| d_ext/(c/2): med={np.nanmedian(rows[:,2])/(c/2):.3f} min={np.nanmin(rows[:,2])/(c/2):.3f}")
        sys.stdout.flush()
