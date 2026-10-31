#!/usr/bin/env python3
"""The relative form of the fill: small removed cells next to a large removed set G that is already good.

G is the refinement of a good pattern of blocks of side B on a torus of side N = n_b B: a random set of blocks, closed under
the fill at the block scale, then refined. Lambda_0 is a set of small cells drawn at random near G and away from it, and by a
hill climb. Claim tested: cl(G u Lambda_0) \\ G lies within sup distance D of Lambda_0, and G has no bad pattern.

Pre-registered criteria, written before the first run.
    PASS-G: a refined good pattern has no bad face, in every run. FAIL-G otherwise: then refinement does not keep goodness.
    PASS-DREL: D <= 3 in every run and climb. FAIL-DREL: D >= 5 in some run. Neither: report.

Result, under a confirmed lock: PASS-G, PASS-DREL, worst D = 2. Blocks of side 3 to 5 only, and coarse closure often fills much of
the coarse torus, so large G leaves few free cells: a weak test of the relative form.

Run under the numeric lock, BLAS threads 1, nice, RSS checked against 2 GB.
"""
import importlib.util
import os
import pathlib
import random
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import numpy as np

HERE = pathlib.Path(__file__)
spec = importlib.util.spec_from_file_location("pf", HERE.with_name("hard-core--independent_patterns_fast.py"))
pf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pf)


def refine(a, B):
    return np.kron(a, np.ones((B, B, B, B), dtype=bool))


def distance_from(seeds, target):
    cur = seeds.copy()
    d = 0
    while (target & ~cur).any():
        nxt = cur.copy()
        for axis in range(4):
            nxt = nxt | np.roll(nxt, 1, axis=axis) | np.roll(nxt, -1, axis=axis)
        cur = nxt
        d += 1
        if d > 20:
            return d
    return d


def main():
    t3, t4 = pf.tables()
    rnd = random.Random(20261031)
    t0 = time.time()
    worst = 0
    g_ok = True
    for (nb, B) in ((2, 5), (3, 3), (2, 4)):
        N = nb * B
        for pc in (0.1, 0.2, 0.3):
            for trial in range(4):
                coarse = np.array([rnd.random() < pc for _ in range(nb**4)]).reshape((nb,) * 4)
                coarse, _ = pf.closure(coarse, t3, t4)
                G = refine(coarse, B)
                Gc, passes0 = pf.closure(G, t3, t4)
                if (Gc != G).any():
                    g_ok = False
                    print(f"refined pattern not closed nb={nb} B={B} pc={pc}", flush=True)
                    G = Gc
                for p in (0.005, 0.01, 0.02, 0.04):
                    seeds = np.array([rnd.random() < p for _ in range(N**4)]).reshape((N,) * 4) & ~G
                    if not seeds.any():
                        continue
                    f, passes = pf.closure(G | seeds, t3, t4)
                    extra = f & ~G
                    d = distance_from(seeds, extra)
                    worst = max(worst, d)
                    if trial == 0:
                        print(f"nb={nb} B={B} pc={pc} p={p} |G|={G.sum()} n0={seeds.sum()} extra={extra.sum()} ratio={extra.sum()/seeds.sum():.2f} passes={passes} D={d} t={time.time()-t0:.0f}", flush=True)
                # hill climb on D
                seeds = np.array([rnd.random() < 0.02 for _ in range(N**4)]).reshape((N,) * 4) & ~G
                f, _ = pf.closure(G | seeds, t3, t4)
                cur = (distance_from(seeds, f & ~G), (f & ~G).sum())
                for it in range(800 if N <= 10 else 300):
                    c = tuple(rnd.randrange(N) for _ in range(4))
                    if G[c]:
                        continue
                    seeds[c] = ~seeds[c]
                    f, _ = pf.closure(G | seeds, t3, t4)
                    new = (distance_from(seeds, f & ~G), (f & ~G).sum())
                    if new >= cur:
                        cur = new
                    else:
                        seeds[c] = ~seeds[c]
                worst = max(worst, cur[0])
                if trial == 0:
                    print(f"climb nb={nb} B={B} pc={pc} D={cur[0]} extra={cur[1]} n0={seeds.sum()} t={time.time()-t0:.0f}", flush=True)
                pf.pm.check_rss()
    print(f"worst D {worst}")
    print("PASS-G" if g_ok else "FAIL-G")
    print("PASS-DREL" if worst <= 3 else ("FAIL-DREL" if worst >= 5 else "NEITHER-DREL"))


if __name__ == "__main__":
    main()
