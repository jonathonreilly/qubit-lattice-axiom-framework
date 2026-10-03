"""A17 check C5 (supplied toy; COMPARATOR-guided: rotor-router / Propp machine, not adopted).
Independent chips on an L^3 torus (non-lazy, 6 directions), density u.  Two relocation rules:
  RW    : each chip picks a direction at random each tick (random odds);
  rotor : each site holds a pointer (one of 6 directions, random at start); chips leaving the site take
          pointer, pointer+1, ... in turn and the pointer advances by the number of chips (deterministic).
Pace = occupation of a ball of radius 1 at a fixed site.  Measured: Var over replicas of the time-integrated
pace, sum_{t<T} (n_B(t) - mean), at several T.  Expectation: RW grows ~ T (accumulating noise);
rotor stays bounded on the finite torus (only frozen start randomness, no fresh randomness).
"""
import os
for k in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[k] = "1"
import sys
import time
import numpy as np

t0 = time.time()
mode = sys.argv[1]
L, u, M, T = 12, 0.1, 200, 3000
V = L ** 3
Nc = int(round(u * V))
rng = np.random.default_rng(5)
co = np.array(np.unravel_index(np.arange(V), (L, L, L))).T
steps = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
nb = np.array([np.ravel_multi_index(((co + d) % L).T, (L, L, L)) for d in steps]).T     # (V, 6)
c0 = np.array([6, 6, 6])
d2 = (np.minimum((co - c0) % L, (c0 - co) % L) ** 2).sum(1)
inB = (d2 <= 1).astype(float)                                                            # ball R=1, 7 sites
pos = rng.integers(0, V, size=(M, Nc))
rot = rng.integers(0, 6, size=M * V)
rep = np.repeat(np.arange(M), Nc)
mean = Nc * inB.sum() / V
cum = np.zeros(M)
checkpoints = {300, 600, 1200, 3000}
out = []
for t in range(1, T + 1):
    cum += inB[pos].sum(1) - mean
    g = (rep * V + pos.ravel())
    if mode == "rw":
        dirs = rng.integers(0, 6, size=g.size)
    else:
        order = np.argsort(g, kind="stable")
        gs = g[order]
        start = np.r_[0, np.flatnonzero(np.diff(gs)) + 1]
        runlen = np.diff(np.r_[start, gs.size])
        rank = np.arange(gs.size) - np.repeat(start, runlen)
        d_sorted = (rot[gs] + rank) % 6
        dirs = np.empty_like(d_sorted); dirs[order] = d_sorted
        ug = gs[start]
        rot[ug] = (rot[ug] + runlen) % 6
    pos = nb[pos.ravel(), dirs].reshape(M, Nc)
    if t in checkpoints:
        out.append((t, cum.var(ddof=1)))
print(f"mode={mode}: L={L}, chips={Nc} (u={Nc/V:.3f}), replicas={M}; Var of time-integrated ball(R=1) occupation:")
for t, v in out:
    print(f"   T={t:5d}: Var = {v:9.2f}   Var/T = {v/t:.4f}")
print(f"elapsed {time.time()-t0:.1f} s")
