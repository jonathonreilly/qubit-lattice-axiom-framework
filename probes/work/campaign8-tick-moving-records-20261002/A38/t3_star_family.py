"""A38 t3: the calm star-local family of H8 (24 dims inside 47 glued covariant star-local terms).
What single-flip hopping can it produce?  (1) structure of the one-flip Hamiltonian over the family:
on-site cost, NN, NNN, distance-2 hops; (2) the subfamily with zero on-site cost and NN hops only;
(3) reachable plaquette phases (sampling + targeted search for pi on every face); (4) spectra."""
import os, sys, signal, itertools, time
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(55)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import least_squares
from lib38 import *
t0 = time.time()
H8 = {r: np.array([(-1) ** r[0], (-1) ** r[1], (-1) ** r[2]], float) / np.sqrt(3) for r in CELL}
shapes = [[(0, 0, 0), (1, 0, 0)], [(1, 0, 0), (0, 1, 0)], [(-1, 0, 0), (1, 0, 0)],
          [(0, 0, 0), (1, 0, 0), (0, 1, 0)], [(-1, 0, 0), (0, 0, 0), (1, 0, 0)],
          [(1, 0, 0), (0, 1, 0), (0, 0, 1)], [(-1, 0, 0), (0, 1, 0), (1, 0, 0)]]
basis = []
kind = []
for i, sh in enumerate(shapes):
    b = covariant_basis(sh); basis += b; kind += [i] * len(b)
# make sure the NN pair block is exactly (J, K, D) so that the pair law is a clean coordinate
basis[0:3] = [pair_law(1, 0, 0), pair_law(0, 1, 0), pair_law(0, 0, 1)]
M, _ = calm_matrix(H8, basis)
N, S = null_space(M, tol=1e-9)
print(f"calm family dimension {N.shape[1]} of {len(basis)}")
# TR parity of each basis term: k-body with k odd is TR-odd
# one-flip hop table per basis term
rows = {}
per = []
for t in basis:
    d = {}
    for a, b, dv, amp, Si, Sj in onefl_terms(H8, t):
        key = (a, b, tuple(int(v) for v in dv))
        d[key] = d.get(key, 0) + amp
    per.append(d)
keys = sorted(set(k for d in per for k in d))
A = np.array([[d.get(k, 0) for d in per] for k in keys])            # complex, rows x 47
cls = np.array([sum(v * v for v in k[2]) for k in keys])
AN = A @ N                                                           # rows x 24
for c in (0, 1, 2, 4):
    sub = AN[cls == c]
    r = np.linalg.matrix_rank(np.vstack([sub.real, sub.imag]), tol=1e-9)
    print(f"  one-flip entries with |d|^2={c}: {sub.shape[0]} entries, rank over the calm family {r}")
# (2) subfamily: zero on-site cost, no NNN and no distance-2 hops
cond = AN[cls != 1]
Wc, Sc = null_space(np.vstack([cond.real, cond.imag]), tol=1e-9)
print(f"(2) calm laws with zero on-site cost and NN hops only: dimension {Wc.shape[1]}")
def hopdict(w):
    c = N @ w
    terms = []
    for t, ci in zip(basis, c):
        if abs(ci) > 1e-14:
            for a, b, dv, amp, Si, Sj in onefl_terms(H8, t):
                terms.append((a, b, dv, ci * amp, Si, Sj))
    return terms
def fluxes(terms):
    return plaquette_fluxes(realspace_hop(terms))
if Wc.shape[1] > 0:
    for j in range(Wc.shape[1]):
        c = N @ Wc[:, j]
        print(f"   direction {j}: pair part (J,K,D) = {np.round(c[:3] / np.max(np.abs(c)), 6).tolist()}, "
              f"uses kinds {sorted(set(kind[i] for i in range(len(c)) if abs(c[i]) > 1e-9))}")
    rng = np.random.default_rng(3)
    for trial in range(4):
        w = Wc @ rng.normal(size=Wc.shape[1])
        f = fluxes(hopdict(w))
        vals = sorted(set((fc, round(ph, 4)) for x, fc, aw, ph in f))
        mags = sorted(set(round(aw, 4) for x, fc, aw, ph in f))
        print(f"   random member {trial}: |W| values {mags}; (face, phase/pi) values {vals[:12]}{' ...' if len(vals) > 12 else ''}")
# (3) whole calm family: how many distinct face phases (orbits) for a random member, and can all reach pi?
rng = np.random.default_rng(7)
w = rng.normal(size=N.shape[1])
f = fluxes(hopdict(w))
ph = np.array([p for x, fc, aw, p in f])
print(f"(3) random calm member: distinct face phases/pi {len(set(np.round(ph, 6)))}: {sorted(set(np.round(ph, 4)))}")
def resid_pi(w):
    f = fluxes(hopdict(w))
    out = []
    for x, fc, aw, p in f:
        W = aw * np.exp(1j * np.pi * p) if aw > 1e-12 else 0
        out += [np.real(W) / max(aw, 1e-9) + 1.0, np.imag(W) / max(aw, 1e-9)]
    nrm = np.linalg.norm(w)
    out.append(nrm - 1.0)
    return np.array(out)
best = None
for trial in range(6):
    w0 = rng.normal(size=N.shape[1]); w0 /= np.linalg.norm(w0)
    r = least_squares(resid_pi, w0, method="lm", max_nfev=400)
    val = np.linalg.norm(r.fun)
    if best is None or val < best[0]:
        best = (val, r.x)
    if time.time() - t0 > 35:
        break
print(f"   targeted search for phase pi on all 24 faces per cell (whole calm family): best residual {best[0]:.3e}")
wb = best[1]
f = fluxes(hopdict(wb))
print("   faces at the best point (face, |W|, phase/pi):", sorted(set((fc, round(aw, 4), round(p, 4)) for x, fc, aw, p in f))[:10])
np.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "t3_best_pi.npy"), wb)
print(f"time {time.time() - t0:.1f} s")
