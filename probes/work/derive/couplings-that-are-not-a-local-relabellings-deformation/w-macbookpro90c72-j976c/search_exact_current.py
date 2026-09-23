#!/usr/bin/env python3
"""Executed search (floating point): couplings on gradients X = dH[d xi] whose operator hops only along the given hop set,
anchored in the window W, with an exactly conserved response on every torus of side 2q (q prime >= 13), i.e.
  (C0) X(k, 0) = 0;  (C1) N(k, g(k) - k) = 0 identically for all 384 g in the symmetry group of |s|^2;  (C2) X = 0 between zeros.
Kernel: X(k, p) = sum_{y in W, d in hops} A_{y,d} e^{-ik.d} e^{-ip.(y+d)};  N = H(k+p) X + X H(k),  H(k) = sum_a sigma_a sin k_a.
Prints the dimension of the solution space and of its part X = i(H(k+p) Q(p) - Q(p) H(k)) (local generators)."""
import itertools, sys
import numpy as np

SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
E = [np.eye(3, dtype=int)[a] for a in range(3)]


def group():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            P = np.zeros((3, 3), int)
            for a in range(3):
                P[a, perm[a]] = signs[a]
            for n in itertools.product((0, 1), repeat=3):
                out.append((P, np.array(n)))
    return out


def build(W, hops):
    unk = [(y, d, r, c) for y in W for d in hops for r in range(2) for c in range(2)]
    return unk


def rows_for_g(unk, P, n):
    """linear map unknowns -> coefficients of N(k, g(k)-k) (dict monomial -> 2x2) as a dense matrix"""
    cols = []
    mons = {}
    entries = []
    for ui, (y, d, r, c) in enumerate(unk):
        Emat = np.zeros((2, 2), complex); Emat[r, c] = 1
        v = np.array(y) + np.array(d)
        sign = (-1) ** int(n @ v)
        m0 = P.T @ v - np.array(y)
        # H(g(k)) X : sum_a (-1)^{n_a} sigma_a [e^{i (Pk)_a} - e^{-i (Pk)_a}]/(2i); e^{i(Pk)_a} = e^{-ik.(-P^T e_a)}
        for a in range(3):
            pa = P.T @ E[a]
            for sgn, mv in ((1, -pa), (-1, pa)):
                coef = ((-1) ** n[a]) * sgn / 2j * sign * (SIG[a] @ Emat)
                entries.append((ui, tuple(m0 + mv), coef))
        # X H(k)
        for a in range(3):
            for sgn, mv in ((1, -E[a]), (-1, E[a])):
                coef = sgn / 2j * sign * (Emat @ SIG[a])
                entries.append((ui, tuple(m0 + mv), coef))
    for ui, m, coef in entries:
        if m not in mons:
            mons[m] = len(mons)
    M = np.zeros((4 * len(mons), len(unk)), complex)
    for ui, m, coef in entries:
        base = 4 * mons[m]
        M[base:base + 4, ui] += coef.reshape(4)
    return M


def linear_constraints(unk, hops):
    rows = []
    # (C0): sum_y A_{y,d} = 0 for each d
    for d in hops:
        for r in range(2):
            for c in range(2):
                row = np.zeros(len(unk), complex)
                for ui, (y, dd, rr, cc) in enumerate(unk):
                    if dd == d and rr == r and cc == c:
                        row[ui] = 1
                rows.append(row)
    # (C2): X(pi m, pi (n - m)) = 0 for all zeros m, n
    for m in itertools.product((0, 1), repeat=3):
        for nn in itertools.product((0, 1), repeat=3):
            for r in range(2):
                for c in range(2):
                    row = np.zeros(len(unk), complex)
                    for ui, (y, d, rr, cc) in enumerate(unk):
                        if rr == r and cc == c:
                            ph = np.exp(-1j * np.pi * (np.dot(m, d) + np.dot(np.array(nn) - np.array(m), np.array(y) + np.array(d))))
                            row[ui] = ph
                    rows.append(row)
    return np.array(rows)


def nullspace(M, tol=1e-9):
    m, n = M.shape
    if m == 0:
        return np.eye(n, dtype=complex), np.zeros(0)
    # full V when there are fewer rows than columns; otherwise the economic SVD already returns all n right vectors
    u, s, vh = np.linalg.svd(M, full_matrices=(m < n))
    del u
    smax = s[0] if len(s) else 1.0
    rank = int(np.sum(s > tol * max(smax, 1.0)))
    return vh[rank:].conj().T, s


def main(window, hopset):
    W = [tuple(y) for y in itertools.product(range(-window, window + 1), repeat=3)]
    if hopset == 'nn':
        hops = [tuple(E[a] * s) for a in range(3) for s in (1, -1)]
    elif hopset == 'nn0':
        hops = [(0, 0, 0)] + [tuple(E[a] * s) for a in range(3) for s in (1, -1)]
    unk = build(W, hops)
    Z, _ = nullspace(linear_constraints(unk, hops))
    print(f"window {window}, hops {hopset}: {len(unk)} unknowns, after (C0),(C2): {Z.shape[1]}", flush=True)
    minsv = []
    grp = sorted(group(), key=lambda g: (int(np.sum(g[0] != np.eye(3, dtype=int))), int(np.sum(np.abs(g[0] - np.eye(3, dtype=int))))))
    for i, (P, n) in enumerate(grp):
        M = rows_for_g(unk, P, n) @ Z
        Zn, s = nullspace(M)
        if Zn.shape[1] < Z.shape[1]:
            kept = s[len(s) - (Z.shape[1] - Zn.shape[1]):] if len(s) else []
        Z = Z @ Zn
        # re-orthonormalize
        q, _ = np.linalg.qr(Z)
        Z = q[:, :Zn.shape[1]] if Zn.shape[1] else Z[:, :0]
        if i % 48 == 47:
            print(f"  after {i + 1} symmetries: dim {Z.shape[1]}", flush=True)
        if Z.shape[1] == 0:
            break
    print(f"solution space dimension: {Z.shape[1]}")
    return unk, Z


if __name__ == '__main__':
    main(int(sys.argv[1]), sys.argv[2])


def u1_vector(unk):
    """the U(1) coupling X = i(H(k+p) - H(k)) in the unknowns' coordinates"""
    v = np.zeros(len(unk), complex)
    idx = {u: i for i, u in enumerate(unk)}
    for a in range(3):
        ea = tuple(E[a])
        mea = tuple(-E[a])
        # i H(k+p) = sum_a sigma_a (e^{i(k_a+p_a)} - e^{-i(k_a+p_a)})/2 : d = -e_a, y = 0 (coef +1/2); d = +e_a, y = 0 (coef -1/2)
        # -i H(k) = -sum_a sigma_a (e^{ik_a} - e^{-ik_a})/2 : d = -e_a, y = e_a (coef -1/2); d = +e_a, y = -e_a (coef +1/2)
        for (y, d, cf) in (((0, 0, 0), mea, 0.5), ((0, 0, 0), ea, -0.5), (ea, mea, -0.5), (mea, ea, 0.5)):
            for r in range(2):
                for c in range(2):
                    key = (y, d, r, c)
                    if key in idx:
                        v[idx[key]] += cf * SIG[a][r, c]
    return v


def onsite_family(unk, window):
    """X = i(H(k+p) Q(p) - Q(p) H(k)), Q(p) = sum_{y in Y} Q_y e^{-ip.y}, Y = {-(window-1)..window-1}^3, sum_y Q_y scalar:
    the couplings i[H, zeta] with zeta an on-site coin field linear in xi (local generators). Returns a basis in the unknowns' coordinates."""
    idx = {u: i for i, u in enumerate(unk)}
    Y = [tuple(y) for y in itertools.product(range(-(window - 1), window), repeat=3)]
    vecs = []
    for y in Y:
        for r in range(2):
            for c in range(2):
                Q = np.zeros((2, 2), complex); Q[r, c] = 1
                v = np.zeros(len(unk), complex)
                for a in range(3):
                    ea, mea = np.array(E[a]), -np.array(E[a])
                    # i H(k+p) Q e^{-ip.y}: sigma_a (e^{i(k_a+p_a)} - e^{-i(k_a+p_a)})/2 : hop d = -e_a (coef +1/2), d = +e_a (-1/2), anchor y
                    for d, cf in ((tuple(mea), 0.5), (tuple(ea), -0.5)):
                        M = cf * (SIG[a] @ Q)
                        for rr in range(2):
                            for cc in range(2):
                                v[idx[(y, d, rr, cc)]] += M[rr, cc]
                    # -i Q H(k) e^{-ip.y}: -Q sigma_a (e^{ik_a} - e^{-ik_a})/2 : hop d = -e_a (coef -1/2) anchor y + e_a; d = +e_a (+1/2) anchor y - e_a
                    for d, cf, yy in ((tuple(mea), -0.5, tuple(np.array(y) + ea)), (tuple(ea), 0.5, tuple(np.array(y) - ea))):
                        M = cf * (Q @ SIG[a])
                        for rr in range(2):
                            for cc in range(2):
                                v[idx[(yy, d, rr, cc)]] += M[rr, cc]
                vecs.append(v)
    V = np.array(vecs).T                     # columns: Q_y basis
    # constraint: sum_y Q_y scalar, i.e. its traceless part vanishes: act on the coefficient space
    nQ = V.shape[1]
    C = np.zeros((3, nQ), complex)
    for iy, y in enumerate(Y):
        for r in range(2):
            for c in range(2):
                col = iy * 4 + r * 2 + c
                # traceless components of Q: (Q_01), (Q_10), (Q_00 - Q_11)
                if (r, c) == (0, 1): C[0, col] = 1
                if (r, c) == (1, 0): C[1, col] = 1
                if (r, c) == (0, 0): C[2, col] = 1
                if (r, c) == (1, 1): C[2, col] = -1
    Nc, _ = nullspace(C)
    return V @ Nc
