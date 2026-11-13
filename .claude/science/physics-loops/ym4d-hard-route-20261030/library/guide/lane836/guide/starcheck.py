"""GUIDE only: check the star walk sum S(x) and the Gaussian star response on K_{2,2,2,2}."""
import numpy as np
D = [(i, s) for i in range(4) for s in (1, -1)]          # directions
perp = lambda a, b: a[0] != b[0]
A8 = np.array([[1.0 if perp(a, b) else 0.0 for b in D] for a in D])
c = (0, 1); d = (1, 1)
idx7 = [k for k, a in enumerate(D) if a != c]
A7 = A8[np.ix_(idx7, idx7)]
for x in (0.05, 0.0902, 0.15):
    G = np.linalg.inv(np.eye(7) - x * A7)
    b = np.zeros(7); b[idx7.index(D.index(d))] = 1.0
    print("x", x, "walk sum", G.dot(b).sum(), "formula", (1 + x) / (1 - 4 * x - 6 * x * x))
print("rho(A7)", max(abs(np.linalg.eigvals(A7))), "2+sqrt10", 2 + 10 ** 0.5)
L = 6 * np.eye(8) - A8
ia, ib = D.index(c), D.index(d)
cur = np.zeros(8); cur[ia] = 1; cur[ib] = -1
m = np.linalg.pinv(L).dot(cur)
print("potentials x48:", np.round(48 * m, 6))
print("l1 after best shift:", min(np.abs(m - t).sum() for t in np.linspace(-0.2, 0.2, 40001)))
