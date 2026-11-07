#!/usr/bin/env python3
"""How far does the fill closure of hard-core--independent_patterns.py travel from the initial set?

Fast form, by arrays on a torus. Hill climbs on D := the maximum sup distance from the initial set, and on the ratio.

Pre-registered criteria, written before the first run.
    PASS-D: D <= 3 in every run, random at all densities, and every climb, on tori of side 6, 8, 10.
    FAIL-D: D >= 5 in some run. Then the closure is not local in any simple way, and Lemma (fill) by a fixed fattening is dead.
    Neither: report.
    PASS-R: best ratio at side 10 at most 1.3 times the best ratio at side 6. FAIL-R: more than 2 times. A growing ratio would
    suggest that it is not bounded.

Result of the first run, with the table of hard-core--independent_patterns.py: PASS-D, worst D = 2. PASS-R: best ratio 24.67, 23.74, 21.28 at sides 6, 8,
10, growth 0.86. Second run, same criteria, with the vertex pattern of an antipodal pair added to the bad ones (see tables): recorded in the part file.

Run under the numeric lock, BLAS threads 1, nice, RSS checked against 2 GB.
"""
import importlib.util
import itertools
import os
import pathlib
import random
import sys
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import numpy as np

HERE = pathlib.Path(__file__)
spec = importlib.util.spec_from_file_location("patterns", HERE.with_name("hard-core--independent_patterns.py"))
pm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pm)

Q4 = list(itertools.product((0, 1), repeat=4))


def tables():
    bad3, _ = pm.bad_table(3)
    bad4, _ = pm.bad_table(4)
    t3 = np.zeros(256, dtype=bool)
    for m in bad3:
        t3[m] = True
    t4 = np.zeros(65536, dtype=bool)
    for m in bad4:
        t4[m] = True
    # the vertex pattern with an antipodal pair removed has H_1 = 0, but no shelling (checks/hard-core--independent_shelling.py), so it is filled too
    for v in range(16):
        t4[65535 ^ (1 << v) ^ (1 << (15 - v))] = True
    return t3, t4


def closure(a, t3, t4):
    """a: boolean array of removed cells, index = cell. A vertex v has cells v - 1 + b, b in {0, 1}^4."""
    a = a.copy()
    passes = 0
    while True:
        kept = (~a).astype(np.int32)
        idx4 = np.zeros(a.shape, dtype=np.int32)
        for b in Q4:
            k = b[0] | b[1] << 1 | b[2] << 2 | b[3] << 3
            idx4 += np.roll(kept, shift=tuple(1 - x for x in b), axis=(0, 1, 2, 3)) << k
        badv = t4[idx4]
        add = np.zeros(a.shape, dtype=bool)
        for b in Q4:
            add |= np.roll(badv, shift=tuple(-(1 - x) for x in b), axis=(0, 1, 2, 3))
        for axis in range(4):
            others = [i for i in range(4) if i != axis]
            idx3 = np.zeros(a.shape, dtype=np.int32)
            for b in itertools.product((0, 1), repeat=3):
                k = b[0] | b[1] << 1 | b[2] << 2
                sh = [0, 0, 0, 0]
                for j, i in enumerate(others):
                    sh[i] = 1 - b[j]
                idx3 += np.roll(kept, shift=tuple(sh), axis=(0, 1, 2, 3)) << k
            bade = t3[idx3]
            for b in itertools.product((0, 1), repeat=3):
                sh = [0, 0, 0, 0]
                for j, i in enumerate(others):
                    sh[i] = -(1 - b[j])
                add |= np.roll(bade, shift=tuple(sh), axis=(0, 1, 2, 3))
        new = add & ~a
        if not new.any():
            return a, passes
        a |= new
        passes += 1


def distance(init, final):
    """Sup distance from init, by dilation on the torus."""
    cur = init.copy()
    d = 0
    target = final & ~init
    while (target & ~cur).any():
        nxt = cur.copy()
        for axis in range(4):
            nxt = nxt | np.roll(nxt, 1, axis=axis) | np.roll(nxt, -1, axis=axis)
        cur = nxt
        d += 1
        if d > 20:
            return d
    return d


def climb(N, objective, t3, t4, rnd, iters, start_p):
    a = np.array([[[[rnd.random() < start_p for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)])

    def val(x):
        f, _ = closure(x, t3, t4)
        n0 = x.sum()
        if n0 == 0:
            return 0.0, 0
        return (f.sum() / n0, distance(x, f))

    cur = val(a)
    for it in range(iters):
        c = tuple(rnd.randrange(N) for _ in range(4))
        a[c] = ~a[c]
        new = val(a)
        better = (new[objective], new[1 - objective]) >= (cur[objective], cur[1 - objective])
        if better:
            cur = new
        else:
            a[c] = ~a[c]
    return cur, int(a.sum())


def main():
    t3, t4 = tables()
    rnd = random.Random(20261031)
    worst_d = 0
    best_ratio = {}
    t0 = time.time()
    for N in (6, 8, 10):
        for p in (0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.12, 0.2):
            for trial in range(4):
                a = np.array([rnd.random() < p for _ in range(N**4)]).reshape((N,) * 4)
                if not a.any():
                    continue
                f, passes = closure(a, t3, t4)
                d = distance(a, f)
                r = f.sum() / a.sum()
                worst_d = max(worst_d, d)
                best_ratio[N] = max(best_ratio.get(N, 0.0), r)
                if trial == 0:
                    print(f"N={N} p={p} n0={a.sum()} n={f.sum()} ratio={r:.2f} passes={passes} D={d} t={time.time()-t0:.0f}", flush=True)
        pm.check_rss()
    iters = {6: 3000, 8: 2000, 10: 1200}
    for N in (6, 8, 10):
        for objective in (0, 1):
            for restart in range(2):
                (r, d), n0 = climb(N, objective, t3, t4, rnd, iters[N], 0.02)
                print(f"climb N={N} objective={'ratio' if objective == 0 else 'D'} n0={n0} ratio={r:.2f} D={d} t={time.time()-t0:.0f}", flush=True)
                worst_d = max(worst_d, d)
                best_ratio[N] = max(best_ratio[N], r)
                pm.check_rss()
    print(f"worst D {worst_d}; best ratio {best_ratio}")
    print("PASS-D" if worst_d <= 3 else ("FAIL-D" if worst_d >= 5 else "NEITHER-D"))
    q = best_ratio[10] / best_ratio[6]
    print(f"ratio growth {q:.2f}: " + ("PASS-R" if q <= 1.3 else ("FAIL-R" if q > 2 else "NEITHER-R")))


if __name__ == "__main__":
    main()
