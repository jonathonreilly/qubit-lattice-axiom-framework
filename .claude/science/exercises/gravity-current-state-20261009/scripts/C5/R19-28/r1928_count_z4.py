"""R19-28: what (Sigma) imposes on a hypercubic Z^4 vacuum (Euclidean), vs O_h x T (R19-20) and O(4).

Written from scratch (does not import R19-20 code). Counts, for the lowest state's linear
gravitating response through two derivatives,
  one-point s^{mn} (symmetric), Pi^{mnrs}(p) = C^{mnrs} + D^{mnrs ab} p_a p_b,
with symmetries (mn), (rs), (mn)<->(rs), (ab); degree 1 excluded by inversion (-I is in B4+).
Ward identity (linearized diffeo, Euclidean): p_m Pi^{mnrs}(p) == 0 for all p.
Groups: W(B4) (all signed permutations), B4+ (proper), O(4) (Lie algebra), and O_h x T (R19-20 control).
"""
import itertools
import numpy as np

d = 4


def sym_basis(nidx, pairs_sym, exch):
    gens = []
    for (i, j) in pairs_sym:
        p = list(range(nidx)); p[i], p[j] = p[j], p[i]; gens.append(tuple(p))
    if exch is not None:
        (i, j), (k, l) = exch
        p = list(range(nidx)); p[i], p[k] = p[k], p[i]; p[j], p[l] = p[l], p[j]
        gens.append(tuple(p))
    group = {tuple(range(nidx))}
    frontier = list(group)
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                c = tuple(g[h[t]] for t in range(nidx))
                if c not in group:
                    group.add(c); new.append(c)
        frontier = new
    N = d ** nidx
    idx = list(itertools.product(range(d), repeat=nidx))
    lin = {t: n for n, t in enumerate(idx)}
    P = np.zeros((N, N))
    for g in group:
        for t in idx:
            tp = tuple(t[g[s]] for s in range(nidx))
            P[lin[tp], lin[t]] += 1.0
    P /= len(group)
    w, v = np.linalg.eigh(P)
    return v[:, w > 0.5]


def kron_power(M, n):
    out = np.array([[1.0]])
    for _ in range(n):
        out = np.kron(out, M)
    return out


def nullspace(M):
    if M.shape[1] == 0:
        return np.zeros((0, 0))
    G = M.T @ M
    w, v = np.linalg.eigh(G)
    scale = max(1.0, w.max())
    return v[:, w < 1e-10 * scale]


def invariants(B, nidx, gens, lie=()):
    rows = [kron_power(L, nidx) @ B - B for L in gens]
    for X in lie:
        A = np.zeros((d ** nidx, d ** nidx))
        for s in range(nidx):
            A += np.kron(np.kron(kron_power(np.eye(d), s), X), kron_power(np.eye(d), nidx - s - 1))
        rows.append(A @ B)
    return B @ nullspace(np.vstack(rows))


def perm_matrix(i, j):
    P = np.eye(d); P[[i, j]] = P[[j, i]]; return P


def rot90(i, j):
    R = np.eye(d); R[i, i] = 0; R[j, j] = 0; R[i, j] = -1; R[j, i] = 1; return R


WB4 = [perm_matrix(0, 1), perm_matrix(1, 2), perm_matrix(2, 3), np.diag([-1.0, 1, 1, 1])]
B4P = [rot90(0, 1), rot90(1, 2), rot90(2, 3)]
LIE_O4 = [(lambda X: X - X.T)(np.outer(np.eye(d)[i], np.eye(d)[j])) for i in range(d) for j in range(i + 1, d)]
OHT = []
for R in (np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], float), np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]], float), -np.eye(3)):
    L = np.eye(4); L[1:, 1:] = R; OHT.append(L)
OHT.append(np.diag([-1.0, 1, 1, 1]))


def ward_deg2(V):
    cols = []
    for c in range(V.shape[1]):
        Dt = V[:, c].reshape((d,) * 6)  # indices m n r s a b ; contract m with p
        S = np.zeros((d,) * 6)
        # p_m p_a p_b D^{mnrs ab}: symmetrize over (m,a,b) -> positions (0,4,5)
        for perm in itertools.permutations((0, 4, 5)):
            axes = list(range(6))
            axes[0], axes[4], axes[5] = perm
            S += np.transpose(Dt, axes)
        cols.append(S.ravel())
    return np.array(cols).T


def ward_deg0(V):
    return V  # p_m C^{mnrs} = 0 for all p  <=>  C = 0


one_B = sym_basis(2, [(0, 1)], None)
c_B = sym_basis(4, [(0, 1), (2, 3)], ((0, 1), (2, 3)))
D_B = sym_basis(6, [(0, 1), (2, 3), (4, 5)], ((0, 1), (2, 3)))

out = []
for name, gens, lie in (("W(B4)", WB4, ()), ("B4+", B4P, ()), ("O(4)", WB4, LIE_O4), ("O_h x T (control)", OHT, ())):
    s1 = invariants(one_B, 2, gens, lie)
    c0 = invariants(c_B, 4, gens, lie)
    c2 = invariants(D_B, 6, gens, lie)
    w0 = nullspace(ward_deg0(c0)).shape[1] if c0.shape[1] else 0
    w2 = nullspace(ward_deg2(c2)).shape[1] if c2.shape[1] else 0
    tot = s1.shape[1] + c0.shape[1] + c2.shape[1]
    out.append(f"{name:18s} one-point {s1.shape[1]}  deg0 {c0.shape[1]}  deg2 {c2.shape[1]}  total {tot}  "
               f"Ward-exact deg0 {w0} deg2 {w2}  -> Ward conditions on response {c0.shape[1]+c2.shape[1]-w0-w2}")
print("\n".join(out))
