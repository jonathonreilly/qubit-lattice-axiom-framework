#!/usr/bin/env python3
"""Supervisor control for block 83 (disjoint machinery: floating-point dense operators in position space; evidence, not proof).

W1: on the 6^3 torus, the walk with an alternation of the lengths delta = 3/10 coupled three ways - through block 62's site frame,
    through block 64's strain coupling, and through the bond's own amplitude (block 82 T3(a)) - against the free walk: operator
    differences and spectra (least |E|).
W2: for a smooth random strain (a sum of long-wavelength modes) coupled through block 64's coupling, the largest matrix element
    inside the sixteen-state corner subspace, and the second-order shift of the corner energies (does a smooth strain gap at second
    order?): least |E| of the strained walk near the corners against the free walk.
W3: the sea's energy per site on the 8^3 torus under the bond-amplitude alternation for delta from 0 to 1 (concave, even, never rising)
    and the same under a frame-coupled alternation (exactly constant).
"""
import sys
from itertools import product

import numpy as np

SIG = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], dtype=complex)]


class Torus:
    def __init__(self, L):
        self.L = L
        self.sites = list(product(range(L), repeat=3))
        self.idx = {s: i for i, s in enumerate(self.sites)}
        self.N = len(self.sites)
        self.T = [self.shift(a) for a in range(3)]
        self.S = [(self.T[a] - self.T[a].T) / 2j for a in range(3)]

    def step(self, s, a, d):
        t = list(s)
        t[a] = (t[a] + d) % self.L
        return tuple(t)

    def shift(self, a):
        M = np.zeros((self.N, self.N))
        for s in self.sites:
            M[self.idx[s], self.idx[self.step(s, a, 1)]] = 1
        return M

    def site(self, f):
        return np.diag([f(s) for s in self.sites]).astype(complex)

    def c_weighted(self, a, v):
        M = np.zeros((self.N, self.N), dtype=complex)
        for s in self.sites:
            M[self.idx[s], self.idx[self.step(s, a, 1)]] += 0.5 * v(s)
            M[self.idx[s], self.idx[self.step(s, a, -1)]] += 0.5 * v(self.step(s, a, -1))
        return M

    def bond_hop(self, a, t):
        M = np.zeros((self.N, self.N), dtype=complex)
        for s in self.sites:
            M[self.idx[s], self.idx[self.step(s, a, 1)]] = t(s)
        return (M - M.conj().T) / 2j

    def free(self):
        return sum(np.kron(SIG[a], self.S[a]) for a in range(3))

    def frame(self, e):
        return sum(np.kron(SIG[j], 0.5 * (self.site(e[j]) @ self.S[j] + self.S[j] @ self.site(e[j]))) for j in range(3))

    def strain(self, B):
        return self.free() + sum(np.kron(SIG[a], 0.5 * (self.c_weighted(a, B[a]) @ self.S[a] + self.S[a] @ self.c_weighted(a, B[a]))) for a in range(3))

    def bond_amplitude(self, t):
        return sum(np.kron(SIG[a], self.bond_hop(a, t[a])) for a in range(3))

    def corners(self):
        out = []
        for kc in product((0, 1), repeat=3):
            v = np.array([np.prod([(-1) ** (kc[a] * s[a]) for a in range(3)]) for s in self.sites], dtype=complex) / np.sqrt(self.N)
            for coin in range(2):
                w = np.zeros(2 * self.N, dtype=complex)
                w[coin * self.N:(coin + 1) * self.N] = v
                out.append(w)
        return out


def w1(tor, delta):
    print(f"W1: 6^3 torus, alternation delta = {delta}: operator differences from the free walk and least |E|")
    H0 = tor.free()
    alt = [lambda s, a=a: delta * (-1) ** s[a] for a in range(3)]
    Hf = tor.frame([lambda s, a=a: 1 + delta * (-1) ** s[a] for a in range(3)])
    Hs = tor.strain(alt)
    Hb = tor.bond_amplitude([lambda s, a=a: 1 + delta * (-1) ** s[a] for a in range(3)])
    for name, H in (("frame-coupled", Hf), ("strain-coupled (block 64)", Hs), ("bond's own amplitude", Hb)):
        ev = np.linalg.eigvalsh(H)
        print(f"  {name}: max |H - H_free| = {np.max(np.abs(H - H0)):.2e}; least |E| = {np.min(np.abs(ev)):.4f} (free: {np.min(np.abs(np.linalg.eigvalsh(H0))):.4f}; sqrt3 delta = {np.sqrt(3) * delta:.4f})")


def w2(tor):
    print("W2: a smooth random strain through block 64's coupling: corner matrix elements and the corner energies")
    rng = np.random.default_rng(3)
    L = tor.L
    modes = [(rng.normal(), rng.normal(), rng.integers(0, 2, size=3)) for _ in range(4)]

    def smooth(s):
        return 0.3 * sum(c1 * np.cos(2 * np.pi * (q @ np.array(s)) / L) + c2 * np.sin(2 * np.pi * (q @ np.array(s)) / L) for c1, c2, q in modes)

    B = [lambda s, a=a: smooth(s) * (1 + 0.2 * a) for a in range(3)]
    Hs = tor.strain(B)
    H0 = tor.free()
    V = Hs - H0
    C = tor.corners()
    maxel = max(abs(u.conj() @ V @ w) for u in C for w in C)
    ev0 = np.linalg.eigvalsh(H0)
    ev = np.linalg.eigvalsh(Hs)
    print(f"  max |V| = {np.max(np.abs(V)):.3f}; largest corner matrix element = {maxel:.2e}; zero modes: free {int(np.sum(np.abs(ev0) < 1e-9))}, strained {int(np.sum(np.abs(ev) < 1e-9))}; least |E| strained = {np.min(np.abs(ev)):.2e}")


def sea_per_site(tor, H):
    ev = np.linalg.eigvalsh(H)
    return float(np.sum(ev[ev < 0])) / tor.N


def w3(tor):
    print("W3: sea energy per site on the 8^3 torus against delta: bond's own amplitude / frame-coupled")
    for delta in (0.0, 0.1, 0.2, 0.4, 0.7, 1.0):
        Hb = tor.bond_amplitude([lambda s, a=a: 1 + delta * (-1) ** s[a] for a in range(3)])
        Hf = tor.frame([lambda s, a=a: 1 + delta * (-1) ** s[a] for a in range(3)])
        print(f"  delta={delta:g}: bond amplitude {sea_per_site(tor, Hb):.5f}   frame {sea_per_site(tor, Hf):.5f}")


def main():
    t6 = Torus(6)
    w1(t6, 0.3)
    w2(t6)
    w3(Torus(8))


if __name__ == "__main__":
    sys.exit(main())
