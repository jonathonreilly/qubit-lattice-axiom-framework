"""E3: two distant plaquettes (4-cycles), brickwork ticks alternating the pairing, so a
record can travel round its plaquette and the one-site limit forces memory.

Each record: 4-cycle {0,1,2,3}; tick k pairs (0,1),(2,3) if k even, (1,2),(3,0) if k odd.
Settings: A and B each choose between two random pair-gate sets at chosen ticks.
psi_0: random linked state on the 16 configurations.

Move sets:  'lattice' = any neighbour on the 4-cycle (the I2 limit itself);
            'tick'    = only along the tick's own support (records follow the flow).

Usage: python3 e3_plaquettes.py <T> <moves> <ntrials> <seed> <setting ticks A> <setting ticks B>
       e.g.  python3 e3_plaquettes.py 2 lattice 20 1 01 01
"""
import sys
import time
import numpy as np
from mtlp import (Model, history_lp, markov_local_lp, haar_unitary, rand_state,
                  block_unitary, ring_adj, tick_support_adj)

T = int(sys.argv[1]); moves = sys.argv[2]; ntr = int(sys.argv[3]); seed = int(sys.argv[4])
setA = [int(c) for c in sys.argv[5]] if len(sys.argv) > 5 else list(range(T))
setB = [int(c) for c in sys.argv[6]] if len(sys.argv) > 6 else list(range(T))
rng = np.random.default_rng(seed)
EVEN = [[0, 1], [2, 3]]
ODD = [[1, 2], [3, 0]]
n = 4


def tick_unitaries(k, nset):
    blocks = EVEN if k % 2 == 0 else ODD
    return [block_unitary(n, blocks, [haar_unitary(2, rng), haar_unitary(2, rng)]) for _ in range(nset)]


cnt = {'C': 0, 'NS': 0, 'ML_all': 0}
ml_tick_fail = np.zeros(T, int)
t0 = time.time()
for tr in range(ntr):
    psi0 = rand_state(16, rng)
    UA = [tick_unitaries(k, 2 if k in setA else 1) for k in range(T)]
    UB = [tick_unitaries(k, 2 if k in setB else 1) for k in range(T)]
    if moves == 'lattice':
        movA = [ring_adj(n)] * T
        movB = [ring_adj(n)] * T
    else:
        movA = [tick_support_adj(UA[k][0]) for k in range(T)]
        movB = [tick_support_adj(UB[k][0]) for k in range(T)]
    m = Model(psi0, UA, UB, movA, movB)
    lp, idx = history_lp(m, ns=False)
    cnt['C'] += lp.solve().status == 0
    lp, idx = history_lp(m, ns=True)
    cnt['NS'] += lp.solve().status == 0
    ok_all = True
    for k in range(T):
        ok = markov_local_lp(m, k)[0].status == 0
        ml_tick_fail[k] += (not ok)
        ok_all &= ok
    cnt['ML_all'] += ok_all
print(f"T={T} moves={moves} settings A@{setA} B@{setB}: {ntr} random linked instances, "
      f"history LP vars ~{lp.nv}, {time.time()-t0:.1f}s")
print(f"  C alone feasible        : {cnt['C']}/{ntr}")
print(f"  C + NS feasible         : {cnt['NS']}/{ntr}")
print(f"  C + Markov-L (all ticks): {cnt['ML_all']}/{ntr};  infeasible at tick k: {ml_tick_fail.tolist()}")
