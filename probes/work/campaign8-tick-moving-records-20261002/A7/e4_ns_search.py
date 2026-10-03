"""E4: search for instances where C + NS is infeasible (forced signalling for ANY rule),
plaquette toy, 3 ticks (4 times).  Confirms with dual simplex and reports the minimal
total NS violation (sum over B- and A-histories of |law difference| across settings).

Usage: python3 e4_ns_search.py <ntrials> <seed> <setA ticks> <setB ticks> <moves>
"""
import sys
import time
import numpy as np
from mtlp import (Model, history_lp, haar_unitary, rand_state, block_unitary,
                  ring_adj, tick_support_adj)

ntr = int(sys.argv[1]); seed = int(sys.argv[2])
setA = [int(c) for c in sys.argv[3]] if sys.argv[3] != '-' else []
setB = [int(c) for c in sys.argv[4]] if sys.argv[4] != '-' else []
moves = sys.argv[5] if len(sys.argv) > 5 else 'tick'
T = 3
rng = np.random.default_rng(seed)
EVEN = [[0, 1], [2, 3]]
ODD = [[1, 2], [3, 0]]


def tick_unitaries(k, nset):
    blocks = EVEN if k % 2 == 0 else ODD
    return [block_unitary(4, blocks, [haar_unitary(2, rng), haar_unitary(2, rng)]) for _ in range(nset)]


t0 = time.time()
found = 0
for tr in range(ntr):
    psi0 = rand_state(16, rng)
    UA = [tick_unitaries(k, 2 if k in setA else 1) for k in range(T)]
    UB = [tick_unitaries(k, 2 if k in setB else 1) for k in range(T)]
    if moves == 'lattice':
        movA = [ring_adj(4)] * T; movB = [ring_adj(4)] * T
    else:
        movA = [tick_support_adj(UA[k][0]) for k in range(T)]
        movB = [tick_support_adj(UB[k][0]) for k in range(T)]
    m = Model(psi0, UA, UB, movA, movB)
    lp, idx = history_lp(m, ns=True)
    r = lp.solve()
    if r.status != 0:
        r2 = lp.solve(method='highs-ds')
        rs = lp.solve(soft=('NSA', 'NSB'))
        found += 1
        print(f"  trial {tr}: C+NS infeasible (ipm status {r.status}, simplex status {r2.status}); "
              f"min total NS violation = {rs.fun:.4e}")
print(f"settings A@{setA} B@{setB} moves={moves}: C+NS infeasible in {found}/{ntr}  "
      f"(vars {lp.nv}, rows {lp.nr}, {time.time()-t0:.1f}s)")
