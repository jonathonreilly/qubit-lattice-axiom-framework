"""A3: what does commuting with BOTH S and P23 (the lane's V4, PMNS_TM2_MAGIC_RESIDUAL note item 4) do to |U_e j|^2 ?
Also the lane's runner control: it counts 'sin^2 theta13 proxy = min over all entries of |U|^2', which is not |U_e3|^2."""
import numpy as np
from common import *
rng = np.random.default_rng(3)
seen = set()
for _ in range(2000):
    A = rng.normal(size=(3, 3)); A = A + A.T
    M = A.copy()
    for g in (I3, S, P23, S @ P23):
        M = (M + g @ M @ g.T) / 2            # project onto the V4 commutant
    assert np.allclose(S @ M, M @ S) and np.allclose(P23 @ M, M @ P23)
    w, V = np.linalg.eigh(M)
    P = np.abs(V) ** 2
    seen.add(tuple(np.round(np.sort(P[0]), 8)))
print("electron-row |U_e j|^2 patterns over 2000 random V4-commuting M (sorted):", seen)
# dimension of the commutant
basis = []
for i in range(3):
    for j in range(3):
        E = np.zeros((3, 3)); E[i, j] = 1
        X = E.copy()
        for g in (I3, S, P23, S @ P23):
            X = (X + g @ X @ g.T) / 2
        basis.append(X.flatten())
print("real dimension of V4-commutant (matrices):", np.linalg.matrix_rank(np.array(basis), tol=1e-9))
# the lane's runner "proxy": min over all |U|^2 entries in the W-preserving (S only) scan
found = []
rng2 = np.random.default_rng(3)
PW = np.outer(W, W)
u1, u2 = XI, ETA
D = np.column_stack([u1, u2])
for _ in range(20000):
    a = rng2.uniform(-1, 1); b = rng2.uniform(-1, 1, 3)
    B = np.array([[b[0], b[2]], [b[2], b[1]]])
    Mw = a * PW + D @ B @ D.T
    w, Uw = np.linalg.eigh(Mw)
    Pw = np.abs(Uw) ** 2
    if any(np.allclose(Pw[:, j], 1 / 3, atol=1e-9) for j in range(3)) and 0.015 < Pw.min() < 0.030:
        s13 = min(Pw[0])   # electron-row minimum
        found.append((Pw.min(), Pw[0].round(4), Pw[1].round(4), Pw[2].round(4)))
        break
print("lane runner's W-preserving hit (S only, NO P23):", found[0] if found else None)
if found:
    print("   -> mu-tau rows equal? ", np.allclose(found[0][2], found[0][3]))
