"""E8: forced signalling with A's ticks FIXED.  For the seed-4/trial-1 instance, take each
of A's 8 tick sequences in turn (A has no choice), let B choose at the listed ticks, and
ask whether A's 3-tick history law can be independent of B's choices (C + NS-A).

Usage: python3 e8_fixedA.py <B setting ticks>   e.g. 01, 0, 1
"""
import sys
import pickle
import itertools
import numpy as np
from mtlp import Model, history_lp, tick_support_adj

keepB = [int(c) for c in sys.argv[1]]
inst = pickle.load(open('inst_seed4_trial1.pkl', 'rb'))
T = 3
for sA in itertools.product(range(2), repeat=3):
    UA = [[inst['UA'][k][sA[k]]] for k in range(T)]
    UB = [inst['UB'][k] if k in keepB else inst['UB'][k][:1] for k in range(T)]
    movA = [tick_support_adj(UA[k][0]) for k in range(T)]
    movB = [tick_support_adj(UB[k][0]) for k in range(T)]
    m = Model(inst['psi0'], UA, UB, movA, movB)
    lp, idx = history_lp(m, ns=True, caus=True)
    r = lp.solve(soft=('NSA',))
    lp2, _ = history_lp(m, ns=True, caus=False)
    r2 = lp2.solve(soft=('NSA',))
    print(f"A ticks {sA}, B chooses at {keepB}: min NS-A violation = {r.fun:.4e} (with CAUS), "
          f"{r2.fun:.4e} (no CAUS);  vars {lp.nv}")
