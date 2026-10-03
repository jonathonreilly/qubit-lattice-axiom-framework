"""Mod-2 linear part of the covariant Clifford-QCA problem on Z^3 qubits.

Unknown f = alpha(X_0) as a mod-2 Pauli string on a box B (O-invariant).
Linear constraints (exact over F2):
  L_R f = f  for R in D4_x (stabilizer of the label X)  [generators C4x, C2y]
  f + L_C3 f + L_C3^2 f = 0                               [alpha(Y_0) = alpha(X_0)+alpha(Z_0)]
with (L_R f)_{R v} = g_R f_v.
"""
import itertools
import numpy as np
from grp import named, label_bits_matrix


def box(shape, r):
    pts = []
    for v in itertools.product(range(-r, r + 1), repeat=3):
        if shape == "cube" or (shape == "oct" and sum(map(abs, v)) <= r):
            pts.append(v)
    return pts


def Lmat(R, pts, idx):
    n = len(pts)
    g = label_bits_matrix(R)
    L = np.zeros((2 * n, 2 * n), dtype=np.uint8)
    for i, v in enumerate(pts):
        j = idx[tuple(int(c) for c in R @ np.array(v))]
        for a in range(2):
            for b in range(2):
                if g[b, a]:
                    L[2 * j + b, 2 * i + a] ^= 1
    return L


def nullspace_f2(A):
    """Basis (rows) of {x : A x = 0} over F2."""
    A = A.copy() % 2
    m, n = A.shape
    piv_cols, r = [], 0
    for c in range(n):
        p = None
        for i in range(r, m):
            if A[i, c]:
                p = i; break
        if p is None:
            continue
        A[[r, p]] = A[[p, r]]
        for i in range(m):
            if i != r and A[i, c]:
                A[i] ^= A[r]
        piv_cols.append(c); r += 1
        if r == m:
            break
    free = [c for c in range(n) if c not in set(piv_cols)]
    basis = []
    for fc in free:
        x = np.zeros(n, dtype=np.uint8); x[fc] = 1
        for i, pc in enumerate(piv_cols):
            if A[i, fc]:
                x[pc] = 1
        basis.append(x)
    return np.array(basis, dtype=np.uint8).reshape(len(basis), n)


def solve(shape, r):
    G = named()
    pts = box(shape, r)
    idx = {v: i for i, v in enumerate(pts)}
    n2 = 2 * len(pts)
    I = np.eye(n2, dtype=np.uint8)
    L4 = Lmat(G["C4x"], pts, idx); L2 = Lmat(G["C2y"], pts, idx); L3 = Lmat(G["C3"], pts, idx)
    L33 = (L3.astype(int) @ L3) % 2
    A = np.vstack([(L4 + I) % 2, (L2 + I) % 2, (I + L3 + L33) % 2]).astype(np.uint8)
    Bs = nullspace_f2(A)
    # sanity: every basis vector satisfies constraints
    assert not ((A.astype(int) @ Bs.T.astype(int)) % 2).any()
    return pts, idx, Bs, L3


if __name__ == "__main__":
    for shape, r in [("oct", 1), ("cube", 1), ("oct", 2), ("cube", 2), ("oct", 3)]:
        pts, idx, Bs, _ = solve(shape, r)
        # also the dimension without the C3 relation
        print(f"{shape} r={r}: |B|={len(pts)}  dim(solutions of linear constraints) = {len(Bs)}")
