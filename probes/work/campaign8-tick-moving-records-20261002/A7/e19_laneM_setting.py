"""E19: lane M's t7b geometry (each record on 4 sites with static bonds (0,1),(2,3), so its
bond label is conserved; linked state on 16 configurations; two gate settings per side;
one tick).  General Markov-L (any local move odds, not just lane M's minimal rule), and
C + NS, by LP.  Also the product-state control.
"""
import numpy as np
from mtlp import Model, history_lp, markov_local_lp, haar_unitary, rand_state, block_unitary
rng = np.random.default_rng(31)
bonds = [[0, 1], [2, 3]]
mov = np.zeros((4, 4), bool)
for b in bonds:
    for i in b:
        for j in b:
            mov[i, j] = True
res = {'lin_ML': 0, 'lin_NS': 0, 'prod_ML': 0}
N = 50
for tr in range(N):
    UA = [[block_unitary(4, bonds, [haar_unitary(2, rng), haar_unitary(2, rng)]) for _ in range(2)]]
    UB = [[block_unitary(4, bonds, [haar_unitary(2, rng), haar_unitary(2, rng)]) for _ in range(2)]]
    psi = rand_state(16, rng)
    m = Model(psi, UA, UB, [mov], [mov])
    res['lin_ML'] += markov_local_lp(m, 0, method='highs-ds')[0].status == 0
    lp, idx = history_lp(m, ns=True)
    res['lin_NS'] += lp.solve(method='highs-ds').status == 0
    psip = np.kron(rand_state(4, rng), rand_state(4, rng))
    mp = Model(psip, UA, UB, [mov], [mov])
    res['prod_ML'] += markov_local_lp(mp, 0, method='highs-ds')[0].status == 0
print(f"lane-M geometry, {N} instances: linked: C+Markov-L feasible {res['lin_ML']}/{N}, C+NS feasible {res['lin_NS']}/{N}; "
      f"unlinked control: C+Markov-L feasible {res['prod_ML']}/{N}")
