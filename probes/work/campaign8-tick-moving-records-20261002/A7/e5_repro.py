"""E5: reproduce the E3 (T=3, tick moves, settings at all ticks, seed 4) instances and
re-solve C + NS with a chosen method; optionally drop some settings (sub-scenarios).

Usage: python3 e5_repro.py <trial> <method> <keepA ticks> <keepB ticks>
  keep*: which ticks keep both settings (others keep only setting 0), e.g. 012 / 01 / -
"""
import sys
import time
import pickle
import numpy as np
from mtlp import (Model, history_lp, haar_unitary, rand_state, block_unitary, tick_support_adj)

trial = int(sys.argv[1]); method = sys.argv[2]
keepA = [int(c) for c in sys.argv[3]] if sys.argv[3] != '-' else []
keepB = [int(c) for c in sys.argv[4]] if sys.argv[4] != '-' else []
T = 3
rng = np.random.default_rng(4)
EVEN = [[0, 1], [2, 3]]
ODD = [[1, 2], [3, 0]]


def tick_unitaries(k, nset):
    blocks = EVEN if k % 2 == 0 else ODD
    return [block_unitary(4, blocks, [haar_unitary(2, rng), haar_unitary(2, rng)]) for _ in range(nset)]


for tr in range(trial + 1):
    psi0 = rand_state(16, rng)
    UA = [tick_unitaries(k, 2) for k in range(T)]
    UB = [tick_unitaries(k, 2) for k in range(T)]
inst = dict(psi0=psi0, UA=UA, UB=UB)
with open(f'inst_seed4_trial{trial}.pkl', 'wb') as f:
    pickle.dump(inst, f)
UA = [UA[k] if k in keepA else UA[k][:1] for k in range(T)]
UB = [UB[k] if k in keepB else UB[k][:1] for k in range(T)]
movA = [tick_support_adj(UA[k][0]) for k in range(T)]
movB = [tick_support_adj(UB[k][0]) for k in range(T)]
m = Model(psi0, UA, UB, movA, movB)
t0 = time.time()
lp, idx = history_lp(m, ns=True)
r = lp.solve(method=method)
print(f"trial {trial} keepA={keepA} keepB={keepB}: C+NS status {r.status} ({method}), "
      f"vars {lp.nv}, rows {lp.nr}, {time.time()-t0:.1f}s")
if r.status != 0 and len(sys.argv) > 5:
    rs = lp.solve(soft=('NSA', 'NSB'), method=method)
    print(f"   min total NS violation = {rs.fun:.6e}")
