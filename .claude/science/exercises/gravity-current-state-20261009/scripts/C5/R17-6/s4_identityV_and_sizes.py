# R17-6 s4. (i) Identity V: for N0914's integer vector stencil, along k = k z_hat
#   (Gn)_x(k) = (1-e^{-ik}) n_xz(k), (Gn)_y(k) = (1-e^{-ik}) n_yz(k), (Gn)_z(k) = (e^{ik}-1) n_zz(k)
#   exactly, for any label configuration (checked on random configs, L=6).
# (ii) ED feasibility: zero-syndrome (mod-2 vector law) sector dimension 2^(6L^3 - rank_F2 G)
#   for the smallest tori that carry both axial TT polarizations (diag + face slots).
import itertools, numpy as np
rng = np.random.default_rng(1)
types = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)]
def G_apply(n, L):
    # n: array (L,L,L,6) integer labels; returns (L,L,L,3)
    out = np.zeros((L, L, L, 3), int)
    for j in range(3):
        out[..., j] += np.roll(n[..., types.index((j, j))], -1, axis=j) - n[..., types.index((j, j))]
        for i in range(3):
            if i == j: continue
            t = types.index(tuple(sorted((i, j))))
            out[..., j] += n[..., t] - np.roll(n[..., t], 1, axis=i)
    return out
L = 6; worst = 0
for trial in range(20):
    n = rng.integers(0, 2, size=(L, L, L, 6))
    g = G_apply(n, L)
    for m in range(1, L):
        k = 2 * np.pi * m / L
        ph = np.exp(-1j * k * np.arange(L))  # Fourier along z only, k_x = k_y = 0
        F = lambda a: np.einsum('xyz,z->', a, ph)
        lhs = [F(g[..., 0]), F(g[..., 1]), F(g[..., 2])]
        rhs = [(1 - np.exp(-1j * k)) * F(n[..., types.index((0, 2))]),
               (1 - np.exp(-1j * k)) * F(n[..., types.index((1, 2))]),
               (np.exp(1j * k) - 1) * F(n[..., types.index((2, 2))])]
        worst = max(worst, max(abs(a - b) for a, b in zip(lhs, rhs)))
print(f'(i) Identity V on 20 random configs, L=6, all k = 2 pi m/6 along z: max |lhs - rhs| = {worst:.2e}')
def gf2_rank(A):
    A = A.copy() % 2; A = A.astype(np.uint8); r = 0
    for c in range(A.shape[1]):
        p = np.nonzero(A[r:, c])[0]
        if len(p) == 0: continue
        p = p[0] + r; A[[r, p]] = A[[p, r]]
        nz = np.nonzero(A[:, c])[0]; nz = nz[nz != r]; A[nz] ^= A[r]; r += 1
        if r == A.shape[0]: break
    return r
for L in [2, 3]:
    nS = 6 * L ** 3; rows = []
    for idx in range(nS):
        e = np.zeros(nS, int); e[idx] = 1
        rows.append(G_apply(e.reshape(L, L, L, 6), L).reshape(-1))
    Gm = np.array(rows).T % 2   # (3L^3) x nS
    r = gf2_rank(Gm)
    print(f'(ii) L={L}: slots {nS}, Gauss rows {3*L**3}, rank_F2 {r}, zero-syndrome sector dim 2^{nS - r} = {2.0**(nS - r):.3g}')
