"""A51 lswt_check: the single-Q LSWT formula against A47 (dual J1-J2, j = 0.2, Neel, shifted 8^3 grid: -0.90717/bond;
nk = 6: -0.90715) and the cubic NN antiferromagnet (E/site = -0.8956 J_S at S = 1/2, standard 1/S value)."""
import sys, signal, itertools, numpy as np
signal.alarm(100)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from fwd51 import lswt
for nk in (6, 8):
    n = np.array(list(itertools.product(range(nk), repeat=3))); k = 2 * np.pi * (n + 0.5) / nk - np.pi
    J = lambda k, j: 2 * np.cos(k).sum(1) + 2 * j * sum(np.cos(k[:, a] + k[:, b]) + np.cos(k[:, a] - k[:, b]) for a, b in ((0, 1), (0, 2), (1, 2)))
    idx = lambda v: (np.mod(v, nk) @ np.array([nk * nk, nk, 1]))
    sh = idx(n + nk // 2)
    for j in (0.0, 0.2):
        Jk = 4 * J(k, j); JQ = 4 * (-6 + 12 * j)
        corr, w2, Am = lswt(Jk, JQ, Jk[sh], Jk[sh])
        e = 0.5 * (-6 + 12 * j) + corr
        print(f"nk={nk} j={j}: Neel E_LSWT/bond = {e / 3:+.5f}; E/site in J_S=1 units (j=0) = {e / 4:+.5f}; min w^2 {w2:.1e}")
