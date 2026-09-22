#!/usr/bin/env python3
"""Supervisor control for block 85 (disjoint machinery: floating-point dense and sparse many-record diagonalisation; evidence, not proof).

W1: on the 2D tori 3x3, 4x3 and 4x4, the ground energy per site of the hard-core crowd (anticommuting composition, one record per site;
    block 80's machinery) under the bond-rate alternation c_b = 1 + delta (-1)^{x_a} on both axes, at delta in {0, 1/20, 1/10, 1/5, 3/10},
    against the free sea's energy per site; a fit E(delta) - E(0) = A |delta| + B delta^2 separates the linear part (from the exact zero
    modes of these small tori) from the quadratic response.
W2: the same at every filling n = 1 .. N on 3x3 (N = 9): the quadratic coefficient against filling; the jam n = N is blind.
"""
import itertools
import sys

import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spl

SIG = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], dtype=complex)]


class Torus2:
    def __init__(self, Lx, Ly):
        self.Lx, self.Ly, self.n = Lx, Ly, Lx * Ly
        self.grid = np.indices((Lx, Ly)).reshape(2, -1)
        self.T = [self.shift(a) for a in range(2)]

    def shift(self, axis):
        g = self.grid.copy()
        g[axis] = (g[axis] + 1) % (self.Lx, self.Ly)[axis]
        M = np.zeros((self.n, self.n))
        M[np.arange(self.n), np.ravel_multi_index(g, (self.Lx, self.Ly))] = 1.0
        return M

    def alternating(self, delta):
        """H = sum_a (1/2i)(t_a T_a - T_a^T t_a) (x) sigma_a, t_a(x) = 1 + delta (-1)^{x_a} on the bond x -> x + e_a."""
        H = np.zeros((2 * self.n, 2 * self.n), dtype=complex)
        for a in range(2):
            t = np.diag(1 + delta * (-1.0) ** self.grid[a])
            hop = (t @ self.T[a] - self.T[a].T @ t) / 2j
            H += np.kron(hop, SIG[a])
        return H


def parity(perm):
    p = list(perm)
    s = 1
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]
            p[i], p[j] = p[j], p[i]
            s = -s
    return s


def hardcore_ground(H1, n_rec):
    d = H1.shape[0]
    site = np.arange(d) // 2
    basis = [s for s in itertools.combinations(range(d), n_rec) if len({site[o] for o in s}) == n_rec]
    index = {s: i for i, s in enumerate(basis)}
    by_o = {o: [o2 for o2 in range(d) if abs(H1[o2, o]) > 1e-14] for o in range(d)}
    rows, cols, vals = [], [], []
    for s, i in index.items():
        sset = set(s)
        used = {site[o] for o in s}
        for pos, o in enumerate(s):
            for o2 in by_o[o]:
                if o2 != o and o2 in sset:
                    continue
                if o2 != o and site[o2] != site[o] and site[o2] in used:
                    continue
                new = list(s)
                new[pos] = o2
                order = sorted(range(n_rec), key=lambda k: new[k])
                rows.append(index[tuple(new[k] for k in order)])
                cols.append(i)
                vals.append(parity(order) * H1[o2, o])
    Hm = sps.csr_matrix((vals, (rows, cols)), shape=(len(basis), len(basis)))
    if len(basis) < 600:
        return float(np.linalg.eigvalsh(Hm.toarray())[0]), len(basis)
    return float(spl.eigsh(Hm, k=1, which="SA", tol=1e-9)[0][0]), len(basis)


def free_sea(H1):
    e = np.linalg.eigvalsh(H1)
    return float(e[e < 0].sum())


def fit(ds, E):
    X = np.array([[abs(d), d * d] for d in ds[1:]])
    y = np.array([e - E[0] for e in E[1:]])
    A, B = np.linalg.lstsq(X, y, rcond=None)[0]
    return A, B


DS = (0.0, 0.05, 0.1, 0.2, 0.3)


def w1():
    print("W1: energy per site under the alternation; fit E(delta) - E(0) = A|delta| + B delta^2")
    for (Lx, Ly, fillings) in ((3, 3, (4, 6)), (4, 3, (6, 8)), (4, 4, (4,))):
        tor = Torus2(Lx, Ly)
        N = tor.n
        sea = [free_sea(tor.alternating(d)) / N for d in DS]
        A, B = fit(DS, sea)
        print(f"  {Lx}x{Ly} free sea: " + ", ".join(f"{d:g}: {e:.5f}" for d, e in zip(DS, sea)) + f"; linear {A:.4f}, quadratic {B:.4f}")
        for n in fillings:
            Ec = [hardcore_ground(tor.alternating(d), n)[0] / N for d in DS]
            dim = hardcore_ground(tor.alternating(0.0), n)[1]
            A, B = fit(DS, Ec)
            print(f"  {Lx}x{Ly} crowd n={n} (dim {dim}): " + ", ".join(f"{d:g}: {e:.5f}" for d, e in zip(DS, Ec)) + f"; linear {A:.4f}, quadratic {B:.4f}")


def w2():
    print("W2: 3x3, every filling: quadratic coefficient of the crowd's ground energy per site (the jam n = 9 is blind)")
    tor = Torus2(3, 3)
    N = tor.n
    for n in range(1, N + 1):
        Ec = [hardcore_ground(tor.alternating(d), n)[0] / N for d in DS]
        A, B = fit(DS, Ec)
        print(f"  n={n}: E(0) = {Ec[0]:.5f}, E(0.3) = {Ec[4]:.5f}; linear {A:.4f}, quadratic {B:.4f}")


def main():
    w1()
    w2()


if __name__ == "__main__":
    sys.exit(main())
