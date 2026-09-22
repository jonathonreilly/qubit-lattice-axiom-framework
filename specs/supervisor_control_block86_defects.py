#!/usr/bin/env python3
"""Supervisor control for block 86 (disjoint machinery: floating-point dense diagonalisation; evidence, not proof).

W1: on the 6^3 and 8^3 tori with alternations (delta_x, delta_y, delta_z) and two walls on none, one, two or all three axes: the number of
    zero modes and the least |E|, against the separable prediction (bulk sqrt(sum delta^2); sheet sqrt(delta_y^2 + delta_z^2); line |delta_z|; point 0).
W2: the sheet's dispersion: with walls across x only, the energies of the wall-bound states against the transverse wave vector on the 8^3 torus,
    against sqrt(sin^2 k_y + sin^2 k_z + delta_y^2 cos^2 k_y + delta_z^2 cos^2 k_z).
W3: the one-axis wall modes on the ring of 16: the decay ratio per two sites against (1 - delta)/(1 + delta) for delta = 1/10, 3/10, 1/2, 7/10.
"""
import sys

import numpy as np

SIG = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], dtype=complex)]


def h1d(L, delta, walls):
    T = np.roll(np.eye(L), -1, axis=1)
    s = np.array([1 if (not walls or x < L // 2) else -1 for x in range(L)])
    t = np.diag(1 + delta * s * (-1.0) ** np.arange(L))
    return (t @ T - T.T @ t) / 2j


def full(L, deltas, walls):
    hs = [h1d(L, deltas[j], walls[j]) for j in range(3)]
    I = np.eye(L)

    def emb(m, j):
        fs = [I, I, I]
        fs[j] = m
        return np.kron(fs[0], np.kron(fs[1], fs[2]))

    return sum(np.kron(SIG[j], emb(hs[j], j)) for j in range(3)), hs


def w1():
    print("W1: zero modes and least |E| against the separable prediction")
    for L in (6, 8):
        for deltas in ((0.3, 0.3, 0.3), (0.3, 0.2, 0.5)):
            for walls in ((False, False, False), (True, False, False), (True, True, False), (True, True, True)):
                H, hs = full(L, deltas, walls)
                ev = np.linalg.eigvalsh(H)
                nz = int(np.sum(np.abs(ev) < 1e-9))
                pred = {0: np.sqrt(sum(d * d for d in deltas)), 1: np.sqrt(deltas[1] ** 2 + deltas[2] ** 2), 2: abs(deltas[2]), 3: 0.0}[sum(walls)]
                print(f"  L={L} deltas={deltas} walls on {sum(walls)} axes: zero modes {nz}, least |E| = {np.min(np.abs(ev)):.4f} (predicted {pred:.4f})")


def w2():
    print("W2: separability of the whole spectrum with walls across x only (8^3, deltas = (0.3, 0.2, 0.5)) and the sheet branch")
    L = 8
    deltas = (0.3, 0.2, 0.5)
    H, hs = full(L, deltas, (True, False, False))
    ev = np.sort(np.linalg.eigvalsh(H))
    e = [np.linalg.eigvalsh(h) for h in hs]
    pred = np.sort(np.array([np.sqrt(a * a + b * b + c * c) * s for a in e[0] for b in e[1] for c in e[2] for s in (1, -1)]))
    zero_x = int(np.sum(np.abs(e[0]) < 1e-9))
    sheet = np.sort(np.array([np.sqrt(b * b + c * c) for b in e[1] for c in e[2]]))
    print(f"  full spectrum equals +-sqrt(e_x^2 + e_y^2 + e_z^2) over all triples: max deviation {np.max(np.abs(ev - pred)):.2e}; h_x has {zero_x} zero modes (two walls)")
    print(f"  the sheet branch (e_x = 0): energies sqrt(e_y^2 + e_z^2) from {sheet[0]:.4f} (= sqrt(delta_y^2 + delta_z^2) = {np.sqrt(deltas[1]**2 + deltas[2]**2):.4f}) to {sheet[-1]:.4f}; a massive two-dimensional band with the transverse alternations as its mass")


def w3():
    print("W3: wall-mode decay ratio per two sites on the ring of 16")
    L = 16
    for delta in (0.1, 0.3, 0.5, 0.7):
        h = h1d(L, delta, True)
        w, v = np.linalg.eigh(h)
        modes = v[:, np.abs(w) < 1e-9]
        ratios = []
        for m in modes.T:
            a = np.abs(m)
            peak = int(np.argmax(a))
            x = peak
            rs = []
            for step in range(3):
                nxt = (x + 2) % L
                if a[nxt] > 1e-12 and a[x] > 1e-12:
                    rs.append(a[nxt] / a[x])
                x = nxt
            ratios.append(rs)
        print(f"  delta={delta}: ratios from the peaks {np.round(ratios, 4).tolist()} against (1 - delta)/(1 + delta) = {(1 - delta) / (1 + delta):.4f}")


def main():
    w1()
    w2()
    w3()


if __name__ == "__main__":
    sys.exit(main())
