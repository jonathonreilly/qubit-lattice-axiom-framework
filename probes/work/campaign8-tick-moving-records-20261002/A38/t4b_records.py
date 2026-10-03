"""A38 t4b (part 4 of t4): (1) NN plaquette phases over H8 for RANDOM covariant star-local laws (calm or not): fixed?
(2) margin of the rank-1 NN block over the calm family; (3) the one-flip spectra over the calm family:
zero-cost modes, touchings at Gamma and at the zone corner, slopes; (4) records next to H8:
which contents keep it calm (pair law and the whole calm star family)."""
import os, sys, signal, itertools, time
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(55)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import functools
print = functools.partial(print, flush=True)
from lib38 import *
t0 = time.time()
H8 = {r: np.array([(-1) ** r[0], (-1) ** r[1], (-1) ** r[2]], float) / np.sqrt(3) for r in CELL}
shapes = [[(0, 0, 0), (1, 0, 0)], [(1, 0, 0), (0, 1, 0)], [(-1, 0, 0), (1, 0, 0)],
          [(0, 0, 0), (1, 0, 0), (0, 1, 0)], [(-1, 0, 0), (0, 0, 0), (1, 0, 0)],
          [(1, 0, 0), (0, 1, 0), (0, 0, 1)], [(-1, 0, 0), (0, 1, 0), (1, 0, 0)]]
basis = []
for sh in shapes:
    basis += covariant_basis(sh)
basis[0:3] = [pair_law(1, 0, 0), pair_law(0, 1, 0), pair_law(0, 0, 1)]
M, _ = calm_matrix(H8, basis)
N, S = null_space(M, tol=1e-9)
# (4) records next to H8: content c at the origin; compressed law; flips not touching the origin
def record_amps(c_law, content):
    ov = {(0, 0, 0): content}
    amps = {}
    for x in itertools.product(range(-2, 2), repeat=3):
        for key, C in c_law.items():
            S = [tuple(np.array(x) + np.array(s)) for s in key]
            if all(max(abs(v) for v in y) > 2 for y in S):
                continue
            Bs = [site_B(ov[y] if y in ov else tex_m(H8, y)) for y in S]
            k = len(S)
            for f in itertools.product((0, 1), repeat=k):
                if sum(f) == 0:
                    continue
                if any(f[i] and S[i] == (0, 0, 0) for i in range(k)):
                    continue                   # killed by the record's compression
                T = C
                for i in range(k):
                    T = np.tensordot(Bs[i][:, f[i], 0], T, axes=([0], [0]))
                fl = tuple(sorted(S[i] for i in range(k) if f[i]))
                if all(max(abs(v) for v in y) <= 1 for y in fl):   # patterns near the record only (all complete)
                    amps[fl] = amps.get(fl, 0) + complex(T)
    return amps
m0 = H8[(0, 0, 0)]
pl = pair_law(1, 1, 0)
for nm, cont in [("+m (background)", m0), ("-m", -m0), ("+z axis", np.array([0, 0, 1.])), ("(1,1,-1)/sqrt3", np.array([1, 1, -1.]) / np.sqrt(3))]:
    a = record_amps(pl, cont)
    print(f"(4) pair law, record content {nm:16s}: largest surviving flip amplitude near it {max(abs(v) for v in a.values()):.3e}")
# whole calm family with a -m record: is any member calm next to it?
cols = []
allk = set()
recs = []
for j in range(len(basis)):
    recs.append(record_amps(basis[j], -m0))
    allk |= set(recs[-1])
allk = sorted(allk)
R = np.array([[r.get(k, 0) for r in recs] for k in allk])
RN = R @ N
sv = np.linalg.svd(np.vstack([RN.real, RN.imag]), compute_uv=False)
print(f"(4) calm star family next to a -m record: smallest singular value {sv[-1]:.3e} (largest {sv[0]:.3f}); "
      f"members calm next to it: {int(np.sum(sv < 1e-9 * sv[0]))} dims of {N.shape[1]}")
print(f"time {time.time() - t0:.1f} s")
