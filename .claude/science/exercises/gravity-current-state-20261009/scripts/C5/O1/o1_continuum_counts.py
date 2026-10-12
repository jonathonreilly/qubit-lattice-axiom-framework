"""O1 check 4: exact continuum counts (Lie-algebra null space) for O(4) and SO(1,3): V, S2, MASS, KIN.
Uses the same Sym^2 / Sym^2(Sym^2) / Sym^2 (x) Sym^2(Sym^2) spaces as o1_invariants.py."""
import itertools, numpy as np
def sym_basis(n, k):
    cols = []
    for ms in itertools.combinations_with_replacement(range(n), k):
        v = np.zeros(n ** k)
        for perm in set(itertools.permutations(ms)):
            idx = 0
            for i in perm: idx = idx * n + i
            v[idx] = 1
        cols.append(v)
    return np.array(cols).T
def gens(metric):
    G = []
    for a in range(4):
        for b in range(a + 1, 4):
            X = np.zeros((4, 4)); X[a, b] = 1; X[b, a] = -1
            G.append(X @ metric)   # generator preserving metric: X^T g + g X = 0 form via X g
    return G
def lie_null(Xs, build):
    A = np.vstack([build(X) for X in Xs]); s = np.linalg.svd(A, compute_uv=False)
    return int(sum(s < 1e-9 * max(1, s.max())) + (A.shape[1] - len(s)))
B2 = sym_basis(4, 2); B2n = B2 / np.linalg.norm(B2, axis=0); B55 = sym_basis(10, 2); B55p = np.linalg.pinv(B55)
I4 = np.eye(4)
def d2(X):  return B2n.T @ (np.kron(X, I4) + np.kron(I4, X)) @ B2n          # on Sym2(R4), 10x10
def d55(X):
    D = d2(X); return B55p @ (np.kron(D, np.eye(10)) + np.kron(np.eye(10), D)) @ B55
def dkin(X):
    return np.kron(d2(X), np.eye(55)) + np.kron(np.eye(10), d55(X))
for name, g in [("SO(4)", np.eye(4)), ("SO(1,3)", np.diag([1., -1, -1, -1]))]:
    Xs = gens(g)
    for X in Xs: assert np.allclose(X.T @ g + g @ X, 0)
    print(f"{name}: V={lie_null(Xs, lambda X: X)}  S2={lie_null(Xs, d2)}  MASS={lie_null(Xs, d55)}  KIN={lie_null(Xs, dkin)}")
