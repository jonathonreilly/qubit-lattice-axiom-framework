"""E13: search 'nice' instances (gate angles in multiples of pi/8, initial 2x2 linked state
with entries in {0, +-1}) of the minimal forced-signalling scenario:
two rings Z_6, records start in bond {0,1}, brickwork ticks E,O,E; A fixed; B chooses its
tick-0 gate (2 options); lattice moves.  Reports instances with the largest minimal
signalling (sum over A-histories of |law difference|, minimised over all C + I2 rules).

Usage: python3 e13_nice_search.py <nsamples> <seed>
"""
import sys
import time
import pickle
import numpy as np
from mtlp import Model, history_lp, block_unitary, ring_adj

ns = int(sys.argv[1]); seed = int(sys.argv[2])
rng = np.random.default_rng(seed)
n, T = 6, 3
EVEN = [[0, 1], [2, 3], [4, 5]]
ODD = [[1, 2], [3, 4], [5, 0]]


def R(m):
    th = m * np.pi / 8
    return np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]], complex)


def tick(blocks, ms):
    return block_unitary(n, blocks, [R(m) for m in ms])


best = []
t0 = time.time()
for it in range(ns):
    if len(sys.argv) > 3 and sys.argv[3] == 'bell':
        M = np.eye(2)
    else:
        M = rng.integers(-1, 2, size=(2, 2)).astype(float)
    if np.count_nonzero(M) < 2:
        continue
    loc = np.zeros((n, n), complex); loc[:2, :2] = M
    psi0 = (loc / np.linalg.norm(loc)).reshape(n * n)
    gA = rng.integers(0, 16, size=6)
    gB = rng.integers(0, 16, size=7)
    UA = [[tick(EVEN, [gA[0], 0, 0])], [tick(ODD, [gA[1], 0, gA[2]])], [tick(EVEN, [gA[3], gA[4], gA[5]])]]
    UB = [[tick(EVEN, [gB[0], 0, 0]), tick(EVEN, [gB[1], 0, 0])], [tick(ODD, [gB[2], 0, gB[3]])],
          [tick(EVEN, [gB[4], gB[5], gB[6]])]]
    m = Model(psi0, UA, UB, [ring_adj(n)] * T, [ring_adj(n)] * T)
    lp, idx = history_lp(m, ns=True, caus=False)
    r = lp.solve(soft={'NSA': 1.0, 'BORN': 1e4})
    if r.status != 0:
        continue
    v = r.slack_by_tag['NSA']
    best.append((v, M.tolist(), gA.tolist(), gB.tolist()))
best.sort(key=lambda z: -z[0])
print(f"{len(best)} valid samples in {time.time()-t0:.1f}s; positives (>1e-6): {sum(b[0] > 1e-6 for b in best)}")
for b in best[:6]:
    print(f"  viol {b[0]:.5f}  M={b[1]}  gA={b[2]}  gB={b[3]}")
pickle.dump(best[:20], open(f'nice_best_seed{seed}.pkl', 'wb'))
