#!/usr/bin/env python3
import numpy as np
from cyc2d import *
rng = np.random.default_rng(13)
shifts = lambda s: [s[k:] + s[:k] for k in range(len(s))]
L = 16; xs, ys = coords(L)
X, Y = (-ys) % L, xs % L; g = Y * L + X                     # 90 deg about site (0,0)
ph = {k: 0 for k in range(4)}; maxd = 0; n = 40
for t in range(n):
    J = rng.random(L * L) < rng.choice([0.05, 0.15, 0.3])
    p0 = run_cycle(L, J)[0]
    J2 = np.zeros_like(J); J2[g] = J
    for k, s in enumerate(shifts(SCHED)):
        ph[k] += np.array_equal(run_cycle(L, J2, s)[0][g], g[p0])
    mv = np.nonzero(p0 != np.arange(L * L))[0]
    if len(mv): maxd = max(maxd, int(cheb_dist_to_locked(L, J)[mv].max()))
print(f"[a] 90-degree image matches phase k in (k: count/{n}): {ph}   [b] max distance of any moved site from a record: {maxd}")
L = 12
for s in (1, 2):
    lk = box(L, 5, 5, s, s); pi, path = run_cycle(L, lk)
    o = orbits(pi)[0]; x0, y0 = 5, 5
    seq = [o[0]]
    for _ in range(len(o) - 1): seq.append(int(pi[seq[-1]]))
    print(f"[e] {s}x{s} record at x,y in [0,{s-1}]: orbit (site -> next site each cycle):",
          " -> ".join(f"({int(coords(L)[0][q])-x0},{int(coords(L)[1][q])-y0})" for q in seq))
