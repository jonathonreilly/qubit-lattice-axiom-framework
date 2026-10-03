"""E14: greedily simplify a forced-signalling instance (Bell-pair start on rings Z_6):
replace gate angles (units of pi/8) by simpler values (0 = identity, 8 = -identity,
4/12 = swap-like, 2/6/10/14 = quarter-mixers) while the minimal signalling stays >= keep*current.

Usage: python3 e14_simplify.py <gA comma list> <gB comma list> [keep]
"""
import sys
import numpy as np
from mtlp import Model, history_lp, block_unitary, ring_adj

gA = [int(v) for v in sys.argv[1].split(',')]
gB = [int(v) for v in sys.argv[2].split(',')]
keep = float(sys.argv[3]) if len(sys.argv) > 3 else 0.999
n, T = 6, 3
EVEN = [[0, 1], [2, 3], [4, 5]]
ODD = [[1, 2], [3, 4], [5, 0]]


def R(m):
    th = m * np.pi / 8
    return np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]], complex)


def tick(blocks, ms):
    return block_unitary(n, blocks, [R(m) for m in ms])


loc = np.zeros((n, n), complex); loc[0, 0] = loc[1, 1] = 1
psi0 = (loc / np.linalg.norm(loc)).reshape(n * n)


def viol(gA, gB, method='highs-ipm'):
    UA = [[tick(EVEN, [gA[0], 0, 0])], [tick(ODD, [gA[1], 0, gA[2]])], [tick(EVEN, [gA[3], gA[4], gA[5]])]]
    UB = [[tick(EVEN, [gB[0], 0, 0]), tick(EVEN, [gB[1], 0, 0])], [tick(ODD, [gB[2], 0, gB[3]])],
          [tick(EVEN, [gB[4], gB[5], gB[6]])]]
    m = Model(psi0, UA, UB, [ring_adj(n)] * T, [ring_adj(n)] * T)
    lp, idx = history_lp(m, ns=True, caus=False)
    r = lp.solve(soft={'NSA': 1.0, 'BORN': 1e4}, method=method)
    return r.slack_by_tag['NSA'] if r.status == 0 else -1


cur = viol(gA, gB)
print(f"start: {cur:.6f}  gA={gA} gB={gB}")
simple = [0, 8, 4, 12, 2, 6, 10, 14]
changed = True
while changed:
    changed = False
    for side in ('A', 'B'):
        g = gA if side == 'A' else gB
        for i in range(len(g)):
            for v in simple:
                if v == g[i] or simple.index(v) >= (simple.index(g[i]) if g[i] in simple else 99):
                    continue
                old = g[i]
                g[i] = v
                val = viol(gA, gB)
                if val >= keep * cur:
                    cur = val
                    changed = True
                    print(f"  {side}[{i}] {old} -> {v}: {cur:.6f}")
                    break
                g[i] = old
print(f"final: {cur:.6f} (simplex check {viol(gA, gB, 'highs-ds'):.6f})  gA={gA} gB={gB}")
