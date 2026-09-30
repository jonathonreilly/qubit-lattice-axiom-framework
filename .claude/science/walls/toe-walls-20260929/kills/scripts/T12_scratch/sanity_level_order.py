# Sanity: the generic estimator reproduces the exact product-order interval sizes (E1) when fed the level order.
import sys; sys.argv=["x"]
import numpy as np, interval_exponent as ie
L = 25
X, Y, Z = np.meshgrid(*(np.arange(L),)*3, indexing="ij")
t = (X + Y + Z).reshape(-1).astype(float) + 1e-6*np.random.default_rng(1).random(L**3)
P, rank, pos = ie.grid_preds(t, L)
ys = rank[np.array([(L*L*20 + L*20 + 20), (L*L*22 + L*18 + 19)])]
bad = 0; tot = 0; maxN = {}
for y in ys:
    lp = ie.anc_lp(P, int(y))
    for x in np.nonzero(lp >= 2)[0][::7]:
        d = np.abs(pos[int(y)] - pos[int(x)])
        exact = int(np.prod(d + 1))
        n = ie.interval_count(P, int(x), int(y), lp)
        tot += 1; bad += (n != exact)
        h = int(lp[x]); maxN[h] = max(maxN.get(h, 0), n)
        assert h == d.sum()
print("pairs checked", tot, "mismatches", bad)
print("max N by h:", {h: maxN[h] for h in sorted(maxN)[:12]}, " exact (h/3+1)^3 at h=3,6,9:", [(h//3+1)**3 for h in (3,6,9)])
