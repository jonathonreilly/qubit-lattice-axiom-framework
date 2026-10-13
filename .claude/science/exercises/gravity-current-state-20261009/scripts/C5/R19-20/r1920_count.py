"""R19-20 independent count (written from scratch; does not import R19-19 code).

Counts the local data of a vacuum's linear gravitating response through two
derivatives, for (i) the grid symmetry O_h x T and (ii) the Lorentz group,
with and without the linearized-diffeo Ward identity, and maps the Ward-exact
O_h x T kernels to the six cone rows (Xi_Eg, Xi_T2g, face1, face2, mu_E, mu_T2).

Kernel: Pi^{mn rs}(p) = C^{mnrs} + D^{mnrs ab} p_a p_b  (degree 1 excluded by
inversion parity). Symmetries: (mn), (rs), (mn)<->(rs), (ab).
One-point part: s^{mn}, symmetric.
"""
import itertools
import numpy as np

np.set_printoptions(precision=4, suppress=True, linewidth=140)
d = 4
TOL = 1e-9


def sym_basis(nidx, pairs_sym, exch):
    """Orthonormal basis of tensors with nidx indices (dim 4 each), symmetric in
    each index pair listed in pairs_sym, and under the pair exchange exch
    ((i,j),(k,l)) if given."""
    N = d ** nidx
    perms = [tuple(range(nidx))]
    gens = []
    for (i, j) in pairs_sym:
        p = list(range(nidx)); p[i], p[j] = p[j], p[i]; gens.append(tuple(p))
    if exch is not None:
        (i, j), (k, l) = exch
        p = list(range(nidx)); p[i], p[k] = p[k], p[i]; p[j], p[l] = p[l], p[j]
        gens.append(tuple(p))
    # close the group of index permutations
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
    P = np.zeros((N, N))
    idx = list(itertools.product(range(d), repeat=nidx))
    lin = {t: n for n, t in enumerate(idx)}
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


def ohT_generators():
    gens = []
    Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], float)
    Rx = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]], float)
    Inv = -np.eye(3)
    for R in (Rz, Rx, Inv):
        L = np.eye(4); L[1:, 1:] = R; gens.append(L)
    T = np.eye(4); T[0, 0] = -1.0; gens.append(T)
    return gens


def lorentz_generators():
    # O_h x T plus boosts (infinitesimal generators handled as finite small boosts
    # would break exactness; use the Lie-algebra condition instead)
    return ohT_generators()


def invariant_space(B, nidx, gens, lie=None):
    rows = []
    for L in gens:
        G = kron_power(L, nidx)
        rows.append(G @ B - B)
    if lie is not None:
        for X in lie:
            # derivation action of Lie algebra element X on nidx-index tensors
            A = np.zeros((d ** nidx, d ** nidx))
            for s in range(nidx):
                left = kron_power(np.eye(4), s)
                right = kron_power(np.eye(4), nidx - s - 1)
                A += np.kron(np.kron(left, X), right)
            rows.append(A @ B)
    M = np.vstack(rows)
    null = nullspace(M)
    return B @ null  # invariant tensors, columns


def boost_generators():
    lie = []
    for i in range(1, 4):
        K = np.zeros((4, 4)); K[0, i] = 1.0; K[i, 0] = 1.0  # acts on upper-index vectors (eta=diag(-1,1,1,1))
        lie.append(K)
    return lie


def ward_matrix_deg2(V, spatial_only):
    """V: columns are D tensors (6 indices m,n,r,s,a,b). Ward: sum_r D^{mn r s ab} p_r p_a p_b = 0
    for all p, for s in allowed set. Symmetrize over (r,a,b) and require zero."""
    cols = []
    sset = [1, 2, 3] if spatial_only else [0, 1, 2, 3]
    for c in range(V.shape[1]):
        Dt = V[:, c].reshape((d,) * 6)
        # W[m,n,s,r,a,b] = D[m,n,r,s,a,b]; symmetrize over r,a,b
        W = np.transpose(Dt, (0, 1, 3, 2, 4, 5))
        S = np.zeros_like(W)
        for perm in itertools.permutations((3, 4, 5)):
            S += np.transpose(W, (0, 1, 2) + perm)
        S = S[:, :, sset]
        cols.append(S.ravel())
    return np.array(cols).T


def ward_matrix_deg0(V, spatial_only):
    cols = []
    sset = [1, 2, 3] if spatial_only else [0, 1, 2, 3]
    for c in range(V.shape[1]):
        Ct = V[:, c].reshape((d,) * 4)
        cols.append(Ct[:, :, :, sset].ravel())
    return np.array(cols).T


def nullspace(M):
    G = M.T @ M
    w, v = np.linalg.eigh(G)
    scale = max(1.0, w.max())
    return v[:, w < 1e-10 * scale]


def null_combos(M):
    if M.shape[1] == 0:
        return np.zeros((0, 0))
    return nullspace(M)


def pol(mat3):
    e = np.zeros((4, 4)); e[1:, 1:] = mat3
    return e / np.linalg.norm(mat3)


x, y, z = np.eye(3)
EG = pol(np.outer(x, x) - np.outer(y, y))
T2 = pol(np.outer(x, y) + np.outer(y, x))
nz = np.array([0, 0, 0, 1.0])
a = (x - y) / np.sqrt(2); b = z
F1 = pol(np.outer(a, a) - np.outer(b, b))
F2 = pol(np.outer(a, b) + np.outer(b, a))
nf = np.array([0, 1, 1, 0]) / np.sqrt(2)


def rows_of(Ct, Dt):
    """Six rows for kernel (C, D). Xi(n,e) = e.(d/dw^2 + d/dq^2)Pi.e at 0; mu = e.C.e"""
    def xi(n, e):
        t0 = np.einsum('mn,rs,mnrs->', e, e, Dt[:, :, :, :, 0, 0])
        tq = np.einsum('mn,rs,a,b,mnrsab->', e, e, n, n, Dt)
        return t0 + tq
    def mu(e):
        return np.einsum('mn,rs,mnrs->', e, e, Ct)
    return np.array([xi(nz, EG), xi(nz, T2), xi(nf, F1), xi(nf, F2), mu(EG), mu(T2)])


def main():
    B2 = sym_basis(2, [(0, 1)], None)                         # one-point s^{mn}
    B4 = sym_basis(4, [(0, 1), (2, 3)], ((0, 1), (2, 3)))      # C
    B6 = sym_basis(6, [(0, 1), (2, 3), (4, 5)], ((0, 1), (2, 3)))  # D
    print('symmetric-space dims: one-point %d, deg0 %d, deg2 %d' % (B2.shape[1], B4.shape[1], B6.shape[1]))
    g = ohT_generators()
    V2 = invariant_space(B2, 2, g)
    V4 = invariant_space(B4, 4, g)
    V6 = invariant_space(B6, 6, g)
    print('O_h x T invariant: one-point %d, deg0 %d, deg2 %d  -> total local data %d'
          % (V2.shape[1], V4.shape[1], V6.shape[1], V2.shape[1] + V4.shape[1] + V6.shape[1]))
    lie = boost_generators()
    # Lorentz-covariant tensors: invariance under rotations/T and boosts.
    # Boost generator acting on upper indices with eta=diag(-1,1,1,1): K^0_i = K^i_0 = 1.
    L2 = invariant_space(B2, 2, g, lie)
    L4 = invariant_space(B4, 4, g, lie)
    L6 = invariant_space(B6, 6, g, lie)
    print('Lorentz x T invariant (upper-index tensors): one-point %d, deg0 %d, deg2 %d'
          % (L2.shape[1], L4.shape[1], L6.shape[1]))
    for label, sp in (('FULL', False), ('SPATIAL', True)):
        n6 = null_combos(ward_matrix_deg2(V6, sp)); n4 = null_combos(ward_matrix_deg0(V4, sp))
        W6 = V6 @ n6 if n6.size else np.zeros((V6.shape[0], 0))
        W4 = V4 @ n4 if n4.size else np.zeros((V4.shape[0], 0))
        print('\n[%s Ward, O_h x T] allowed deg2 %d, deg0 %d' % (label, W6.shape[1], W4.shape[1]))
        R = []
        for c in range(W6.shape[1]):
            R.append(rows_of(np.zeros((d,) * 4), W6[:, c].reshape((d,) * 6)))
        for c in range(W4.shape[1]):
            R.append(rows_of(W4[:, c].reshape((d,) * 4), np.zeros((d,) * 6)))
        R = np.array(R)
        if R.size:
            u, sv, vt = np.linalg.svd(R)
            r = int((sv > 1e-9 * sv.max()).sum())
            print('  rank of map to rows (Xi_Eg, Xi_T2g, face1, face2, mu_E, mu_T2) = %d' % r)
            img = vt[:r]
            # normalize image directions for readability
            for v in img:
                k = np.argmax(np.abs(v)); print('  image dir:', v / v[k])
        if sp:
            continue
        # Lorentz + Ward: should be EH only
        n6L = null_combos(ward_matrix_deg2(L6, False)); n4L = null_combos(ward_matrix_deg0(L4, False))
        print('[FULL Ward, Lorentz] allowed deg2 %d, deg0 %d' % (n6L.shape[1] if n6L.size else 0,
                                                                n4L.shape[1] if n4L.size else 0))
        if n6L.size:
            for c in range(n6L.shape[1]):
                Dt = (L6 @ n6L[:, c]).reshape((d,) * 6)
                print('  EH-type kernel rows:', rows_of(np.zeros((d,) * 4), Dt))
    # all-kernel rank (no Ward)
    R = [rows_of(np.zeros((d,) * 4), V6[:, c].reshape((d,) * 6)) for c in range(V6.shape[1])]
    R += [rows_of(V4[:, c].reshape((d,) * 4), np.zeros((d,) * 6)) for c in range(V4.shape[1])]
    sv = np.linalg.svd(np.array(R), compute_uv=False)
    print('\n[no Ward, O_h x T] rank of map to six rows = %d' % int((sv > 1e-9 * sv.max()).sum()))


if __name__ == '__main__':
    main()
