#!/usr/bin/env python3
"""Supervisor control for block 82 (disjoint machinery: floating-point k-space blocks and dense diagonalisation; evidence, not proof).

W1: the walk with alternating lengths t_j(x) = 1 + delta (-1)^{x_j} on every axis and the axioms' scalar hop through the same lengths,
    as 16 x 16 blocks over a fine grid of the reduced zone: the least |E| (half the gap of the zero-symmetric spectrum), for beta = 1,
    delta in {1/8, 1/4, 1/2} and a in {0, 1/10, 1/4, 1/2}.
W2: the free sea's energy (sum of the negative eigenvalues) per site on L^3 tori (L = 8, 16) as a function of the background strength for
    three backgrounds of equal strength g: alternating lengths (delta = g), the chessboard scalar (m = g), the axis stripes (c_j = g);
    the second-order coefficient -d^2 E/dg^2 at g = 0 (the sea's susceptibility to each background) and whether E decreases to g = 1.
W3: the projected walk on a 6^3 torus for the half-filled equilibrium arrangement sampled by block 81's control (records excluded):
    exact zero-mode count against the sublattice-imbalance bound; the same for the chessboard.
"""
import itertools
import sys

import numpy as np

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
SIG = [SX, SY, SZ]


def place(mat, j):
    fs = [I2, I2, I2]
    fs[j] = mat
    return np.kron(I2, np.kron(fs[0], np.kron(fs[1], fs[2])))


def coin(mat):
    return np.kron(mat, np.eye(8, dtype=complex))


def block16(k, beta, delta, a, m_chess=0.0, c_stripe=0.0):
    """16 x 16 block of the eight species at reduced wave vector k: alternating lengths delta in both hops; optional chessboard m and stripes c."""
    H = np.zeros((16, 16), dtype=complex)
    for j in range(3):
        s, c = np.sin(k[j]), np.cos(k[j])
        H += coin(SIG[j]) @ place(beta * (-s * SZ + delta * c * SY), j)
        H += place(2 * a * (c * SZ + delta * s * SY), j)
        H += coin(SIG[j]) @ place(c_stripe * SX, j)
    H += m_chess * place(SX, 0) @ place(SX, 1) @ place(SX, 2)
    return H


def w1():
    print("W1: alternating lengths (both hops), beta = 1; least |E| over the reduced zone (grid 24^3)")
    grid = np.linspace(0, np.pi, 24)
    for delta in (0.125, 0.25, 0.5):
        for a in (0.0, 0.1, 0.25, 0.5):
            least = 9.0
            for kx in grid:
                for ky in grid:
                    for kz in grid:
                        ev = np.linalg.eigvalsh(block16((kx, ky, kz), 1.0, delta, a))
                        least = min(least, np.min(np.abs(ev)))   # the spectrum is symmetric about zero (eps anticommutes with both hops): least |E| is half the gap
            print(f"  delta={delta:g} a={a:g}: least |E| over the zone = {least:.4f} (sqrt3*delta = {np.sqrt(3)*delta:.4f})")


def sea_energy(L, beta, delta, a, m_chess, c_stripe):
    ks = 2 * np.pi * np.arange(L // 2) / L      # reduced zone: k_j in [0, pi) with the eight species folded in
    tot = 0.0
    for k in itertools.product(ks, repeat=3):
        ev = np.linalg.eigvalsh(block16(k, beta, delta, a, m_chess, c_stripe))
        tot += np.sum(ev[ev < 0])
    return tot / L ** 3


def w2():
    print("W2: free sea energy per site on L^3 tori against the background strength g (a = 0): alternating lengths / chessboard scalar / axis stripes")
    for L in (8, 16):
        rows = []
        for g in (0.0, 0.05, 0.1, 0.2, 0.4, 0.7, 1.0):
            e_len = sea_energy(L, 1.0, g, 0.0, 0.0, 0.0)
            e_ch = sea_energy(L, 1.0, 0.0, 0.0, g, 0.0)
            e_st = sea_energy(L, 1.0, 0.0, 0.0, 0.0, g)
            rows.append((g, e_len, e_ch, e_st))
            print(f"  L={L} g={g:g}: lengths {e_len:.5f}  chessboard {e_ch:.5f}  stripes {e_st:.5f}")
        e0 = rows[0]
        for name, col in (("lengths", 1), ("chessboard", 2), ("stripes", 3)):
            chi = -2 * (rows[2][col] - e0[col]) / rows[2][0] ** 2
            mono = all(rows[i + 1][col] <= rows[i][col] for i in range(len(rows) - 1))
            print(f"    L={L} {name}: second-order coefficient -2 dE/g^2 at g = 0.1: {chi:.4f}; monotone decreasing to g = 1: {mono}")


def lattice(L):
    N = L ** 3
    nb = np.zeros((N, 6), dtype=np.int64)
    par = np.zeros(N, dtype=np.int64)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = (x * L + y) * L + z
                par[i] = (x + y + z) % 2
                for d, off in ((1, 0), (-1, 3)):
                    nb[i, off] = (((x + d) % L) * L + y) * L + z
                    nb[i, off + 1] = (x * L + (y + d) % L) * L + z
                    nb[i, off + 2] = (x * L + y) * L + (z + d) % L
    return N, nb, par


def projected_walk(L, vacant):
    N, nb, par = lattice(L)
    vi = {s: i for i, s in enumerate(vacant)}
    n = len(vacant)
    H = np.zeros((2 * n, 2 * n), dtype=complex)
    for s in vacant:
        for a in range(3):
            for d, off in ((1, 0), (-1, 3)):
                t = nb[s, off + a]
                if t in vi:
                    H[2 * vi[s]:2 * vi[s] + 2, 2 * vi[t]:2 * vi[t] + 2] += d * SIG[a] / (2j)
    ev = np.linalg.eigvalsh(H)
    even = sum(1 for s in vacant if par[s] == 0)
    return int(np.sum(np.abs(ev) < 1e-9)), 2 * abs(even - (n - even)), n


def w3():
    print("W3: projected walk (records excluded) on the 6^3 torus: zero modes against 2|even - odd| of the vacant set")
    L = 6
    N, nb, par = lattice(L)
    chess = [i for i in range(N) if par[i] == 1]
    z, b, n = projected_walk(L, chess)
    print(f"  chessboard: vacant {n}, zero modes {z}, bound {b}")
    rng = np.random.default_rng(7)
    for trial in range(3):
        occ = np.zeros(N, dtype=int)
        occ[rng.choice(N, N // 2, replace=False)] = 1
        vac = [i for i in range(N) if occ[i] == 0]
        z, b, n = projected_walk(L, vac)
        print(f"  random half filling (seed {trial}): vacant {n}, zero modes {z}, bound {b}")


def main():
    w1()
    w2()
    w3()


if __name__ == "__main__":
    sys.exit(main())
