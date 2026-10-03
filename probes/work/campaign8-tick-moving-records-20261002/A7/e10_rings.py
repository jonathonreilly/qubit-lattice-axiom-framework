"""E10: forced signalling on larger rings, where even lattice moves (any neighbour) cannot
forget a record's position.  Each record lives on a ring Z_n; brickwork ticks alternate the
pairing; the initial linked state is supported on the first `w` sites of each ring.
A's ticks fixed; B chooses its gate at the listed ticks (2 options each).

Usage: python3 e10_rings.py <n> <w> <T> <Bticks> <ntrials> <seed> <moves> [complex]
"""
import sys
import time
import numpy as np
from mtlp import (Model, history_lp, haar_unitary, block_unitary, ring_adj, tick_support_adj)

n = int(sys.argv[1]); w = int(sys.argv[2]); T = int(sys.argv[3])
Bt = [int(c) for c in sys.argv[4]]; ntr = int(sys.argv[5]); seed = int(sys.argv[6])
moves = sys.argv[7]; cplx = len(sys.argv) > 8 and sys.argv[8] == 'complex'
rng = np.random.default_rng(seed)
EVEN = [[2 * i, 2 * i + 1] for i in range(n // 2)]
ODD = [[2 * i + 1, (2 * i + 2) % n] for i in range(n // 2)]


def gate():
    if cplx:
        return haar_unitary(2, rng)
    th = rng.uniform(0, 2 * np.pi)
    return np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]], complex)


def tick(k):
    blocks = EVEN if k % 2 == 0 else ODD
    return block_unitary(n, blocks, [gate() for _ in blocks])


t0 = time.time()
vals = []
bslack = [0.0]
nv = 0
for tr in range(ntr):
    loc = np.zeros((n, n), complex)
    if cplx:
        loc[:w, :w] = rng.normal(size=(w, w)) + 1j * rng.normal(size=(w, w))
    else:
        loc[:w, :w] = rng.normal(size=(w, w))
    psi0 = (loc / np.linalg.norm(loc)).reshape(n * n)
    UA = [[tick(k)] for k in range(T)]
    UB = [[tick(k), tick(k)] if k in Bt else [tick(k)] for k in range(T)]
    if moves == 'lattice':
        movA = [ring_adj(n)] * T; movB = [ring_adj(n)] * T
    else:
        movA = [tick_support_adj(UA[k][0]) for k in range(T)]
        movB = [tick_support_adj(UB[k][0]) for k in range(T)]
    m = Model(psi0, UA, UB, movA, movB)
    lp, idx = history_lp(m, ns=True, caus=True)
    nv = max(nv, lp.nv)
    r = lp.solve(soft={'NSA': 1.0, 'BORN': 1e4})
    if r.status == 0:
        vals.append(r.slack_by_tag['NSA'])
        bslack.append(r.slack_by_tag['BORN'])
    else:
        vals.append(np.nan)
vals = np.array(vals)
pos = vals[vals > 1e-7]
print(f"ring n={n} w={w} T={T} B@{Bt} moves={moves} complex={cplx} seed={seed}: forced signalling in "
      f"{len(pos)}/{ntr}; max {np.nanmax(vals):.4e}; failures {np.isnan(vals).sum()}; max Born slack {max(bslack):.1e}; vars<= {nv} ({time.time()-t0:.1f}s)")
