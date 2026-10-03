"""E15: the clean forced-signalling ('triangle') instance, checked three ways.

Regions: A and B each a ring Z_6 (only sites 0,1 of A are ever used; B uses 0,1,5).
psi_0 = (|0>_A|0>_B + |1>_A|1>_B)/sqrt2       (linked possibilities, a Bell pair)
tick 0: A idle;            B applies R(theta) on its bond {0,1}, theta chosen by B
tick 1: A idle;            B moves site 0's possibility to site 5 (R(pi/2) on pair (5,0)),
                           site 1 idle  -> B's two branches end up two sites apart
tick 2: A applies R(phi) on its bond {0,1};  B idle
Readable record positions at times 0..3.

Analytic (EXACT):  P(a1 != b1) = sin^2(theta);  b3 = 5 iff b1 = 0 for every one-site rule;
P(a3 != index(b3)) = sin^2(phi - theta).  Triangle inequality on (a1, a3, b1):
   |sin^2 th - sin^2(phi-th)| <= P(a1 != a3) <= sin^2 th + sin^2(phi-th).
theta in {pi/8, 3pi/8}, phi = pi/4  =>  P(a1 != a3) <= 0.2929 for one choice and >= 0.7071
for the other: A's own two-time record law must change by >= sqrt2 - 1 = 0.41421.
"""
import numpy as np
from scipy.sparse import coo_matrix
from mtlp import Model, history_lp, block_unitary, ring_adj, tick_support_adj, rot

n, T = 6, 3
EVEN = [[0, 1], [2, 3], [4, 5]]
ODD = [[1, 2], [3, 4], [5, 0]]
I6 = np.eye(n, dtype=complex)
th = [np.pi / 8, 3 * np.pi / 8]
phi = np.pi / 4
loc = np.zeros((n, n), complex); loc[0, 0] = loc[1, 1] = 1 / np.sqrt(2)
psi0 = loc.reshape(n * n)
UA = [[I6], [I6], [block_unitary(n, [[0, 1]], [rot(phi)])]]
UB = [[block_unitary(n, [[0, 1]], [rot(t)]) for t in th],
      [block_unitary(n, [[5, 0]], [rot(np.pi / 2)])],
      [I6]]

# analytic numbers from the Born odds
for i, t in enumerate(th):
    m = Model(psi0, UA, [[UB[0][i]], UB[1], UB[2]], [ring_adj(n)] * T, [ring_adj(n)] * T)
    P1 = m.born(((0, 0),)); P3 = m.born(((0, 0), (0, 0), (0, 0)))
    d1 = P1[0, 1] + P1[1, 0]
    e3 = P3[0, 1] + P3[1, 5]          # a3 != index(b3): (a=0,b=1) or (a=1,b=5)
    print(f"theta={t/np.pi:.3f}pi: P(a1!=b1)={d1:.6f} (sin^2 th={np.sin(t)**2:.6f}); "
          f"P(a3!=idx b3)={e3:.6f} (sin^2(phi-th)={np.sin(phi-t)**2:.6f}); "
          f"triangle interval for P(a1!=a3): [{abs(d1-e3):.6f}, {min(d1+e3, 2-d1-e3):.6f}]")
print(f"forced gap = {abs(np.sin(th[1])**2 - np.sin(phi-th[1])**2) - (np.sin(th[0])**2 + np.sin(phi-th[0])**2):.6f}"
      f"  (sqrt2-1 = {np.sqrt(2)-1:.6f})")

for moves in ('lattice', 'flow'):
    if moves == 'lattice':
        movA = [ring_adj(n)] * T; movB = [ring_adj(n)] * T
    else:
        movA = [tick_support_adj(UA[k][0]) | np.eye(n, dtype=bool) for k in range(T)]
        movB = [tick_support_adj(UB[k][0]) | np.eye(n, dtype=bool) for k in range(T)]
    m = Model(psi0, UA, UB, movA, movB)
    lp, idx = history_lp(m, ns=True, caus=True)
    w = {'NSA': 1.0, 'BORN': 1e4}
    r = lp.solve(soft=w, method='highs-ds')
    y = r.eqlin.marginals
    A = coo_matrix((lp.vals, (lp.rows, lp.cols)), shape=(lp.nr, lp.nv)).tocsr()
    b = np.array(lp.b)
    wrow = np.array([w.get(t, np.inf) for t in lp.tags])
    hard = np.isinf(wrow)
    print(f"[{moves} moves] min over all C+I2 rules of sum_h |mu_A^th1(h) - mu_A^th0(h)| = {r.fun:.6f} "
          f"(2(sqrt2-1) = {2*(np.sqrt(2)-1):.6f}); Born slack {r.slack_by_tag['BORN']:.1e}")
    print(f"     dual certificate: b.y = {b @ y:.6f}, max(A^T y) = {(A.T @ y).max():.1e}, "
          f"max |y|/w on soft rows = {np.max(np.abs(y[~hard]) / wrow[~hard]):.6f}")
