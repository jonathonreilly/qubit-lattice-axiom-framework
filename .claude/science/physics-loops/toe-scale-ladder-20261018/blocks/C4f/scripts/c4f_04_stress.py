#!/usr/bin/env python3
"""C4f stress test where the generalized Lemma I bears load (dense implementation, L=12 torus).

Backgrounds: empty, full, half-space, slab, checkerboard-of-slabs.  On each, place m in [2, 40]
random candidate patterns of random units of either layer (any kind; control sets written too),
then run 8 ticks of U, checking at every tick that each layer is an involution on its input, and
finally apply U^-1 eight times and require the initial configuration back.  Every 25th
configuration is also run through the sparse implementation (c4f_core) for one tick.
usage: c4f_04_stress.py [n_configs]   (default 1500); checkpoint counts printed every 250.
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c4f_dense as Dn
import c4f_core as C

N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
L = 12; DU = Dn.DenseU(L); T = DU.T
wrap = lambda z: (z[0] % L, z[1] % L, z[2] % L)
SU = C.Dyn(wrap)
rng = np.random.default_rng(1018)
bgs = {
    'empty': np.zeros(T.V, bool), 'full': np.ones(T.V, bool),
    'half': T.coords[:, 2] >= 6, 'slab': (T.coords[:, 0] % 6) < 3,
    'checker': ((T.coords[:, 0] // 3 + T.coords[:, 1] // 3) % 2) == 0,
}
names = list(bgs)
bad_inv = bad_rev = bad_sp = 0; cross = {'L1': 0, 'B': 0, 'A': 0}; t0 = time.time()
for it in range(N):
    c = bgs[names[it % len(names)]].copy()
    for _ in range(int(rng.integers(2, 41))):
        lay = (DU.L1, DU.L2)[rng.integers(2)]; u = rng.integers(lay['n']); st = rng.integers(2)
        c[lay['D'][u]] = bool(st == 0); c[lay['Dp'][u]] = bool(st == 1)
        if lay['ctl'][u] == 1: c[lay['G'][u]] = False
        if lay['ctl'][u] == 2: c[lay['G'][u]] = True
    c0 = c.copy()
    if it % 25 == 0:
        sp = SU(frozenset(tuple(int(v) for v in T.coords[i]) for i in np.nonzero(c)[0]))
        bad_sp += sp != frozenset(tuple(int(v) for v in T.coords[i]) for i in np.nonzero(DU(c))[0])
    for t in range(8):
        a, x1 = Dn.apply(DU.L1, c, True)
        bad_inv += not np.array_equal(Dn.apply(DU.L1, a), c)
        b, x2 = Dn.apply(DU.L2, a, True)
        bad_inv += not np.array_equal(Dn.apply(DU.L2, b), a)
        cross['L1'] += len(x1); k = DU.L2['ctl'][x2]
        cross['B'] += int((k == 1).sum()); cross['A'] += int((k == 2).sum())
        c = b
    for t in range(8): c = DU.inv(c)
    bad_rev += not np.array_equal(c, c0)
    if (it + 1) % 250 == 0:
        print(f'checkpoint {it+1}/{N}: bad_inv={bad_inv} bad_rev={bad_rev} bad_sparse={bad_sp} '
              f'crossings={cross} t={time.time()-t0:.0f}s', flush=True)
P = F = 0
def check(name, ok, info=''):
    global P, F
    if ok: P += 1; print('PASS', name, info)
    else: F += 1; print('FAIL', name, info)
check(f'{N} stress configs x 8 ticks: every layer application is an involution on its input', bad_inv == 0,
      f'[crossings {cross}]')
check(f'{N} stress configs: U^-8 U^8 = id', bad_rev == 0)
check(f'sparse == dense on {(N + 24) // 25} stress configs (one tick)', bad_sp == 0)
check('both L2 kinds crossed >= 1000 times', cross['A'] >= 1000 and cross['B'] >= 1000)
print(f'TOTAL: PASS={P} FAIL={F}')
