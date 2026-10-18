"""Item 5 and the Answer's common-speed claim: invariant-tensor counts beyond scalars.
Reynolds projection on explicit tensor bases (independent of the runner's random-seed SVD)."""
import itertools
import numpy as np
def sp(n, fix_last):
    out = []; m = n - 1 if fix_last else n
    for p in itertools.permutations(range(m)):
        for s in itertools.product((1, -1), repeat=n):
            M = np.zeros((n, n))
            for i, j in enumerate(p): M[i, j] = s[i]
            if fix_last: M[n - 1, n - 1] = s[n - 1]
            out.append(M)
    return out
def rot4(th, a, b):
    M = np.eye(4); M[a, a] = M[b, b] = np.cos(th); M[a, b] = -np.sin(th); M[b, a] = np.sin(th); return M
GROUPS = {'B4 (384)': sp(4, False), 'O_h x T (96)': sp(4, True)}
def count(rank, act, G, dim):
    """dimension of invariant subspace of a representation given by act(g) (dim x dim matrices)"""
    P = sum(act(g) for g in G) / len(G)
    return int(round(np.real(np.trace(P))))
# rank-2 general tensors (fermion gamma_mu k_nu coupling): act = g (x) g
# symmetric rank-2 (scalar kinetic), antisymmetric-pair quadratic forms (F_mu nu F_rho sigma), symmetric rank-4 (dim-6 LV)
pairs = list(itertools.combinations(range(4), 2))
def lam2(g):
    A = np.zeros((6, 6))
    for b, (r, s) in enumerate(pairs):
        for a, (m, n) in enumerate(pairs):
            A[a, b] = g[m, r] * g[n, s] - g[m, s] * g[n, r]
    return A
def sym2(A):  # action on symmetric bilinear forms of a d-dim rep
    d = A.shape[0]; idx = [(i, j) for i in range(d) for j in range(i, d)]
    K = np.kron(A, A); S = np.zeros((d * d, len(idx)))
    for c, (i, j) in enumerate(idx):
        S[i * d + j, c] += 1; S[j * d + i, c] += 1
    S /= np.linalg.norm(S, axis=0)
    return S.T @ K @ S
def sym4(g):
    idx = [c for c in itertools.combinations_with_replacement(range(4), 4)]
    B = []
    for c in idx:
        v = np.zeros(4 ** 4)
        for p in set(itertools.permutations(c)): v[np.ravel_multi_index(p, (4,) * 4)] = 1
        B.append(v / np.linalg.norm(v))
    B = np.array(B).T; K = np.kron(np.kron(g, g), np.kron(g, g))
    return B.T @ K @ B
for name, G in GROUPS.items():
    print(name)
    print("  symmetric rank-2 (scalar K_mu nu):", count(2, sym2, G, 10))
    print("  general rank-2 (Dirac c_mu nu gamma_mu k_nu):", count(2, lambda g: np.kron(g, g), G, 16))
    print("  quadratic forms in F_mu nu (gauge-invariant spin-1 kinetic):", count(2, lambda g: sym2(lam2(g)), G, 21))
    print("  symmetric rank-4 (k^4 terms; >1 means LV allowed at this order):", count(4, sym4, G, 35))
# SO(4) reference for rank-4: 1 (delta delta symmetrized); check by averaging over many random rotations is
# unnecessary: symmetric invariant rank-4 of SO(4) is (k^2)^2 only.
