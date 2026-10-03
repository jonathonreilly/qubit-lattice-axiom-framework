"""E17: the triangle no-go compressed to TWO ticks.
tick 0: B applies R(theta), theta in {pi/8, 3pi/8} (B's choice); A idle.
tick 1: A applies R(pi/4) on its bond; B moves site 0 -> 5 (R(pi/2) on pair (5,0)).
Times 0,1,2 readable.  Expect min TV of A's history law = sqrt2 - 1.
Also: the same with B's tick-1 split replaced by B idle (no registration): expect 0.
"""
import numpy as np
from mtlp import Model, history_lp, block_unitary, ring_adj, rot
n, T = 6, 2
I6 = np.eye(n, dtype=complex)
loc = np.zeros((n, n), complex); loc[0, 0] = loc[1, 1] = 1 / np.sqrt(2)
psi0 = loc.reshape(n * n)
UA = [[I6], [block_unitary(n, [[0, 1]], [rot(np.pi / 4)])]]
for label, split in (('B splits its branches at tick 1', True), ('B idle at tick 1 (no registration)', False)):
    UB = [[block_unitary(n, [[0, 1]], [rot(t)]) for t in (np.pi / 8, 3 * np.pi / 8)],
          [block_unitary(n, [[5, 0]], [rot(np.pi / 2)]) if split else I6]]
    m = Model(psi0, UA, UB, [ring_adj(n)] * T, [ring_adj(n)] * T)
    lp, idx = history_lp(m, ns=True, caus=True)
    r = lp.solve(soft={'NSA': 1.0, 'BORN': 1e4}, method='highs-ds')
    print(f"{label:38s}: min sum|mu_A diff| = {r.slack_by_tag['NSA']:.6f}  -> min TV = {r.slack_by_tag['NSA']/2:.6f}"
          f"  (sqrt2-1 = {np.sqrt(2)-1:.6f}); vars {lp.nv}")
