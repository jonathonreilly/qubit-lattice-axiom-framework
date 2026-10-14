"""Exploratory: smallest segment witnesses (X0 grid x R set), P = Q = 0, Y0 = 0."""
import numpy as np, itertools
from t22lib import box4
d = 0.6
def lm(X, R):
    XX, RR = np.meshgrid(X, R, indexing='ij'); XX = XX.ravel(); RR = RR.ravel()
    a = np.maximum(2 * d - np.abs(XX[:, None] - XX[None, :]), 0)
    A = np.stack([a, a, 2 * d + 0 * a, 2 * d + 0 * a], -1)
    Km = box4((RR[:, None] - RR[None, :]) / 2, A); ev = np.linalg.eigvalsh(Km)
    return ev[0] / ev[-1], len(XX)
for R in ([-1.1, 1.1], [-1.1, 0, 1.1], [0, 1.1], [-0.55, 0.55]):
    best = None
    for hx in (0.05, 0.1, 0.15, 0.2, 0.25, 0.3):
        for nx in range(2, 16):
            X = np.arange(nx) * hx
            v, n = lm(X, R)
            if v < -1e-9 and (best is None or n < best[1] or (n == best[1] and v < best[0])):
                best = (v, n, hx, nx)
    print("R set", R, "-> smallest negative:", best)
