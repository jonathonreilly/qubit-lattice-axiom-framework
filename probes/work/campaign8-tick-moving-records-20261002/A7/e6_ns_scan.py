"""E6: scan random plaquette instances, T=3 ticks, for forced signalling (C + NS infeasible).
Reports min total NS violation (L1, summed over NS rows) when infeasible.

Usage: python3 e6_ns_scan.py <ntrials> <seed> <setA> <setB>
"""
import sys
import time
import numpy as np
from mtlp import (Model, history_lp, haar_unitary, rand_state, block_unitary, tick_support_adj)

ntr = int(sys.argv[1]); seed = int(sys.argv[2])
setA = [int(c) for c in sys.argv[3]] if sys.argv[3] != '-' else []
setB = [int(c) for c in sys.argv[4]] if sys.argv[4] != '-' else []
T = 3
rng = np.random.default_rng(seed)
EVEN = [[0, 1], [2, 3]]
ODD = [[1, 2], [3, 0]]


def tick_unitaries(k, nset):
    blocks = EVEN if k % 2 == 0 else ODD
    return [block_unitary(4, blocks, [haar_unitary(2, rng), haar_unitary(2, rng)]) for _ in range(nset)]


t0 = time.time()
viol = []
for tr in range(ntr):
    psi0 = rand_state(16, rng)
    UA = [tick_unitaries(k, 2 if k in setA else 1) for k in range(T)]
    UB = [tick_unitaries(k, 2 if k in setB else 1) for k in range(T)]
    movA = [tick_support_adj(UA[k][0]) for k in range(T)]
    movB = [tick_support_adj(UB[k][0]) for k in range(T)]
    m = Model(psi0, UA, UB, movA, movB)
    lp, idx = history_lp(m, ns=True)
    rs = lp.solve(soft=('NSA', 'NSB'))
    viol.append(rs.fun)
viol = np.array(viol)
print(f"seed {seed} A@{setA} B@{setB}: {ntr} trials, min-NS-violation > 1e-6 in {(viol > 1e-6).sum()}/{ntr}; "
      f"values: {np.round(np.sort(viol)[::-1][:6], 5).tolist()}  ({time.time()-t0:.1f}s)")
