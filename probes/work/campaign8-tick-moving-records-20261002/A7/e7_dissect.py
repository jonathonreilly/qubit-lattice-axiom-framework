"""E7: dissect the forced-signalling instance (seed 4, trial 1, A settings at ticks 0,1,2;
B settings at ticks 0,1; tick moves).  Which constraint families are needed?
  variants: full; no CAUS; only NS-B (B's history independent of A's settings);
            only NS-A; soft NS-B with hard NS-A, etc.
Also verify the soft-LP solution independently (C, CAUS residuals; NS deviation recomputed).
"""
import pickle
import numpy as np
from mtlp import Model, history_lp, tick_support_adj

inst = pickle.load(open('inst_seed4_trial1.pkl', 'rb'))
T = 3
keepA, keepB = [0, 1, 2], [0, 1]
UA = [inst['UA'][k] if k in keepA else inst['UA'][k][:1] for k in range(T)]
UB = [inst['UB'][k] if k in keepB else inst['UB'][k][:1] for k in range(T)]
movA = [tick_support_adj(UA[k][0]) for k in range(T)]
movB = [tick_support_adj(UB[k][0]) for k in range(T)]
m = Model(inst['psi0'], UA, UB, movA, movB)


def run(label, ns=True, caus=True, soft=()):
    lp, idx = history_lp(m, ns=ns, caus=caus)
    if soft:
        r = lp.solve(soft=soft)
        print(f"  {label:42s}: status {r.status}; min violation of {soft} = {r.fun if r.fun is None else f'{r.fun:.4e}'}")
        return lp, idx, r
    r = lp.solve()
    print(f"  {label:42s}: status {r.status}")
    return lp, idx, r


run('C + CAUS + NS(both)')
run('C + NS(both), no CAUS', caus=False)
run('C + CAUS only', ns=False)
run('soft NS-B, hard NS-A', soft=('NSB',))
run('NS-A only (hard), no NS-B: use soft NSB weight', soft=('NSB',))
run('soft NS-A, hard NS-B', soft=('NSA',))
lp, idx, r = run('soft both', soft=('NSA', 'NSB'))

# independent verification of the soft solution
x = r.x[:lp.nv]
maxC = 0.0
for sig, (start, H) in idx.items():
    q = x[start:start + len(H)]
    for k in range(T + 1):
        P = m.born(sig[:k])
        M = np.zeros_like(P)
        for i, h in enumerate(H):
            M[h[k]] += q[i]
        maxC = max(maxC, np.abs(M - P).max())
print(f"  verify: max |time-k marginal - Born| = {maxC:.2e}; min Q = {x.min():.2e}")
# NS deviation: B-history law for each r-class, max TV across A settings
for side in ('B', 'A'):
    worst = 0.0
    classes = {}
    for sig in idx:
        key = tuple(s[1] for s in sig) if side == 'B' else tuple(s[0] for s in sig)
        classes.setdefault(key, []).append(sig)
    for key, members in classes.items():
        laws = []
        for sig in members:
            start, H = idx[sig]
            d = {}
            for i, h in enumerate(H):
                hh = tuple(z[1] for z in h) if side == 'B' else tuple(z[0] for z in h)
                d[hh] = d.get(hh, 0.0) + x[start + i]
            laws.append(d)
        keys = set().union(*laws)
        for L in laws[1:]:
            tv = 0.5 * sum(abs(L.get(k_, 0) - laws[0].get(k_, 0)) for k_ in keys)
            worst = max(worst, tv)
    print(f"  verify: max TV of {side}-history law across the other side's settings = {worst:.3e}")
