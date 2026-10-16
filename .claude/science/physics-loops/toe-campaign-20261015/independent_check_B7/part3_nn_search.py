"""Part 3 (numerical exploration): nearest-site covariant walks.  Parametrise A = sum_i x_i B_i
(B_i: real orthonormal basis of the 11-dim covariant nearest-site space, x_i complex), minimise the
unitarity defect  F(x) = sum_d || sum_n A_n^dag A_{n+d} - delta_{d0} I ||^2  from many random starts,
and for every solution found (F < 1e-20) measure k-dependence of the spectrum (characteristic
polynomial coefficients over random k).  NUMERICAL."""
import numpy as np, sys, itertools
from scipy.optimize import least_squares
from walks import *

ci = int(sys.argv[1]) if len(sys.argv) > 1 else 3
nstart = int(sys.argv[2]) if len(sys.argv) > 2 else 300
D = class_D(ci)
B = covariant_basis(D, nn_support())
nb = len(B)
DS = [np.array(d) for d in itertools.product(range(-2, 3), repeat=3)]
pairs = {}
for di, d in enumerate(DS):
    for i, n in enumerate(OFFS):
        j = OIDX.get(tuple(n + d))
        if j is not None:
            pairs.setdefault(di, []).append((i, j))

def Aof(x):
    z = x[:nb] + 1j * x[nb:]
    return np.tensordot(z, B, axes=1)

# exact sampling: W^dag W - I has Fourier support in {-2..2}^3, so vanishing on the 5^3 grid
# k in (2 pi/5){0..4}^3 is equivalent to unitarity for all k.  Same for W W^dag (implied in finite dim).
KG = np.array(list(itertools.product(np.arange(5) * 2 * np.pi / 5, repeat=3)))
PH = np.exp(1j * KG @ np.array(OFFS).T)          # (125, 27)
BK = np.einsum('kn,bnij->bkij', PH, B)            # (nb,125,8,8)
def resid(x):
    z = x[:nb] + 1j * x[nb:]
    Wk = np.tensordot(z, BK, axes=1)              # (125,8,8)
    r = (np.einsum('kji,kjl->kil', Wk.conj(), Wk) - np.eye(8)).reshape(-1)
    return np.concatenate([r.real, r.imag])

def charpoly_spread(A, nk=60, seed=0):
    rng = np.random.default_rng(seed)
    cps = np.array([np.poly(symbol(A, k)) for k in rng.uniform(-np.pi, np.pi, (nk, 3))])
    return np.abs(cps - cps[0]).max()

rng = np.random.default_rng(12345 + ci)
sols = []
for s in range(nstart):
    x0 = rng.normal(size=2 * nb) * rng.uniform(0.2, 1.0)
    r = least_squares(resid, x0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
    F = np.sum(r.fun ** 2)
    if F < 1e-20:
        A = Aof(r.x)
        sp = charpoly_spread(A)
        nz = [i for i, n in enumerate(OFFS) if np.abs(A[i]).max() > 1e-8]
        sols.append((sp, len(nz)))
        print(f"  start {s}: unitary, charpoly spread {sp:.2e}, nonzero offsets {len(nz)}, |c|={np.round(np.abs(r.x[:nb]+1j*r.x[nb:]),4)}", flush=True)
print(f"class {ci}: basis dim {nb}; {len(sols)} unitary solutions out of {nstart} starts")
if sols:
    sp = np.array([s[0] for s in sols])
    print("  max charpoly spread over k among solutions:", sp.max())
    from collections import Counter
    print("  number of nonzero offsets per solution:", Counter(s[1] for s in sols))
