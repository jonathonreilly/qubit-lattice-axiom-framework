"""E12: the minimal forced-signalling scenario on the saved ring-6 instance:
B makes ONE binary choice of tick operator at tick 0; A's ticks are fixed; 3 ticks;
records move to any lattice neighbour.  Solve with dual simplex, verify the dual
certificate, and print its Born-row weights (the 'signalling witness').
"""
import pickle
import numpy as np
from scipy.sparse import coo_matrix
from mtlp import Model, history_lp, ring_adj

d = pickle.load(open('ring6_best.pkl', 'rb'))
n, T = d['n'], d['T']
UB = [d['UB'][0], d['UB'][1][:1], d['UB'][2]]
m = Model(d['psi0'], d['UA'], UB, [ring_adj(n)] * T, [ring_adj(n)] * T)
lp, idx = history_lp(m, ns=True, caus=False)
weights = {'NSA': 1.0, 'BORN': 1e4}
r = lp.solve(soft=weights, method='highs-ds')
print(f"single B choice at tick 0: min NS-A violation (simplex) = {r.fun:.6f}; Born slack {r.slack_by_tag['BORN']:.1e}")
y = r.eqlin.marginals
A = coo_matrix((lp.vals, (lp.rows, lp.cols)), shape=(lp.nr, lp.nv)).tocsr()
b = np.array(lp.b)
ATy = A.T @ y
wrow = np.array([weights.get(t, np.inf) for t in lp.tags])
print(f"certificate: b.y = {b @ y:.6f}; max(A^T y) = {ATy.max():.2e}; max|y|/w (soft rows) = {np.max(np.abs(y)/wrow):.6f}")

# The A-history laws under the two settings in the optimal solution
x = r.x[:lp.nv]
laws = []
for sig in m.sigmas():
    start, H = idx[sig]
    L = {}
    for i, h in enumerate(H):
        ha = tuple(z[0] for z in h)
        L[ha] = L.get(ha, 0.0) + x[start + i]
    laws.append(L)
keys = sorted(set(laws[0]) | set(laws[1]))
tv = 0.5 * sum(abs(laws[0].get(k, 0) - laws[1].get(k, 0)) for k in keys)
print(f"TV between A's 4-time history laws for B's two choices (optimal rule): {tv:.6f}")
print("A-histories with the largest law differences (a0,a1,a2,a3): r=0 vs r=1")
diffs = sorted(keys, key=lambda k: -abs(laws[0].get(k, 0) - laws[1].get(k, 0)))[:8]
for k in diffs:
    print(f"   {k}: {laws[0].get(k,0):.4f}  {laws[1].get(k,0):.4f}")

# Born marginals of A (should be r-independent) and joint Born tables
for sig in m.sigmas():
    for k in range(T + 1):
        P = m.born(sig[:k])
        print(f"sigma {sig} time {k}: A-marginal {np.round(P.sum(1), 4)}")
