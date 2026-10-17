"""Validate lock_mc against exact enumeration on the 4^3 torus, N = 4 records,
content-less, g in {0, 0.3, 3}: <bonds per record> and <m_s^2>."""
import itertools, math, sys
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import lock_mc as M

L, N = 4, 4
nbr, par = M.build_nbr(L)
V = L ** 3
stag = np.where(par == 0, 1, -1)
# bonds of each pair
adj = np.zeros((V, V), np.int8)
for x in range(V):
    for d in (0, 2, 4):
        y = nbr[x, d]
        adj[x, y] = adj[y, x] = 1
Bcnt = {}
for c in itertools.combinations(range(V), N):
    B = int(sum(int(adj[a, b]) for a, b in itertools.combinations(c, 2)))
    m = int(stag[list(c)].sum())
    Bcnt.setdefault((B, m * m), 0)
    Bcnt[(B, m * m)] += 1
for g in (0.0, 0.3, 3.0):
    Z = sum(n * (g ** B if B > 0 else 1.0) for (B, mm), n in Bcnt.items())
    EB = sum(n * B * (g ** B if B > 0 else 1.0) for (B, mm), n in Bcnt.items()) / Z
    Em2 = sum(n * mm * (g ** B if B > 0 else 1.0) for (B, mm), n in Bcnt.items()) / Z / V ** 2
    res, _ = M.run_point(L, N / V, g, None, "rand", 7, neq=500, nmeas=40000, every=5)
    print(f"g={g}: exact bonds/rec={EB / N:.5f} MC={res['bonds_per_rec']:.5f} | exact ms2={Em2:.6f} MC={res['ms2']:.6f}+-{res['ms2_se']:.6f}", flush=True)
# contents: N=2 adjacent-pair probability with (3,1,2), g = 0.5 on 4^3, exact
pqr = (3, 1, 2); g = 0.5
lm = M.content_logM(*pqr)
Mm = np.exp(lm)
Q1 = Mm.mean()  # E_uniform M over two independent contents = 1 (rows sum to 6)
npairs = V * (V - 1) // 2
nb = 3 * V
Zc = (npairs - nb) + nb * g * Q1
print("contents: E M =", Q1, " exact P(bond) =", nb * g * Q1 / Zc)
res, _ = M.run_point(L, 2 / V, g, pqr, "rand", 9, neq=500, nmeas=40000, every=5)
print("MC P(bond) =", res['bonds_per_rec'] * 2, flush=True)
