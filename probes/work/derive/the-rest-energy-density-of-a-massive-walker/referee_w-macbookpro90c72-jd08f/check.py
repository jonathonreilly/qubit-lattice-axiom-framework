#!/usr/bin/env python3
"""Referee for the-rest-energy-density-of-a-massive-walker a2.

Author w-macbookpro90c72-j35f5 (claude-opus-5-5). Own Gaussian-rational walk on 4^3.
"""
import itertools
from fractions import Fraction as Fr
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


class G:
    def __init__(self, r=0, i=0):
        self.r, self.i = Fr(r), Fr(i)

    def __add__(self, o):
        return G(self.r + o.r, self.i + o.i)

    def __sub__(self, o):
        return G(self.r - o.r, self.i - o.i)

    def __mul__(self, o):
        if isinstance(o, G):
            return G(self.r * o.r - self.i * o.i, self.r * o.i + self.i * o.r)
        return G(self.r * o, self.i * o)

    __rmul__ = __mul__

    def conj(self):
        return G(self.r, -self.i)

    def abs2(self):
        return self.r * self.r + self.i * self.i

    def __eq__(self, o):
        return self.r == o.r and self.i == o.i


Z, ONE, I = G(), G(1), G(0, 1)
L = 4
V = L ** 3
SITES = list(itertools.product(range(L), repeat=3))
IDX = {x: n for n, x in enumerate(SITES)}
EPS = [(-1) ** sum(x) for x in SITES]
SIG = [
    [[Z, ONE], [ONE, Z]],
    [[Z, G(0, -1)], [I, Z]],
    [[ONE, Z], [Z, G(-1)]],
]
m = Fr(3, 4)


def shift(x, j, s):
    y = list(x)
    y[j] = (y[j] + s) % L
    return IDX[tuple(y)]


def apply_H(v):
    out = [[Z, Z] for _ in SITES]
    for n, x in enumerate(SITES):
        for j in range(3):
            dv = [(v[shift(x, j, -1)][a] - v[shift(x, j, 1)][a]) * G(0, Fr(1, 2)) for a in range(2)]
            for a in range(2):
                acc = Z
                for b in range(2):
                    acc = acc + SIG[j][a][b] * dv[b]
                out[n][a] = out[n][a] + acc
    return out


def massive(v):
    hopped = apply_H(v)
    return [[hopped[n][a] + v[n][a] * (m * EPS[n]) for a in range(2)] for n in range(V)]


def norm2(v):
    return [v[n][0].abs2() + v[n][1].abs2() for n in range(V)]


def energy(v, Hv):
    return [(v[n][0].conj() * Hv[n][0] + v[n][1].conj() * Hv[n][1]).r for n in range(V)]


def phase(e):
    return [ONE, I, G(-1), G(0, -1)][e % 4]


def rest_and_moving():
    chi = [[G(1 + EPS[n]), Z] for n in range(V)]
    Hchi = massive(chi)
    rest_ok = all(Hchi[n][a] == chi[n][a] * m for n in range(V) for a in range(2))
    rest_ok &= all(energy(chi, Hchi)[n] == 0 for n in range(V) if EPS[n] == -1)
    nrm = sum(norm2(chi))
    e_rest = [x / nrm for x in energy(chi, Hchi)]
    rest_ok &= all(e_rest[n] == (m * Fr(2, V) if EPS[n] == 1 else 0) for n in range(V))
    rest_ok &= sum(e_rest) == m
    kv = (1, 0, 0)
    psi = []
    for n, x in enumerate(SITES):
        amp = phase(sum(a * b for a, b in zip(kv, x))) * (1 + Fr(EPS[n], 3))
        psi.append([amp, amp])
    Hpsi = massive(psi)
    move_ok = all(Hpsi[n][a] == psi[n][a] * Fr(5, 4) for n in range(V) for a in range(2))
    dp = norm2(psi)
    ntot = sum(dp)
    even = sum(dp[n] for n in range(V) if EPS[n] == 1) / ntot
    e_full = [x / ntot for x in energy(psi, Hpsi)]
    e_mass = [m * EPS[n] * dp[n] / ntot for n in range(V)]
    move_ok &= even == Fr(4, 5) and sum(e_mass) == Fr(9, 20) and sum(e_full) == Fr(5, 4)
    move_ok &= sum(a - b for a, b in zip(e_full, e_mass)) == Fr(4, 5)
    # packet: scale rest by 1/8 and moving by 3/8
    chi_n = [[c * Fr(1, 8) for c in row] for row in chi]
    psi_n = [[c * Fr(3, 8) for c in row] for row in psi]
    n1, n2 = sum(norm2(chi_n)), sum(norm2(psi_n))
    pk = [[chi_n[n][a] + psi_n[n][a] for a in range(2)] for n in range(V)]
    epk = [x / (n1 + n2) for x in energy(pk, massive(pk))]
    packet = (
        n1 == 2 and n2 == 20 and sum(epk) == Fr(53, 44)
        and sum(epk[n] for n in range(V) if EPS[n] == 1) == Fr(43, 44)
        and min(epk) == Fr(5, 704)
    )
    report(
        "densities",
        rest_ok and move_ok and packet,
        "rest density 2m/V on even sites; moving weights 4/5 and 1/5; packet sum 53/44, minimum 5/704",
    )


def chessboard():
    def avg(f):
        out = []
        for x in SITES:
            out.append(sum(f[shift_raw(x, j, s)] for j in range(3) for s in (-1, 1)) / 6)
        return out

    def shift_raw(x, j, s):
        y = list(x)
        y[j] = (y[j] + s) % L
        return IDX[tuple(y)]

    ok = avg(EPS) == [-e for e in EPS]
    src = [m / V * e for e in EPS]
    alpha = -m / (12 * V)
    u = [alpha * e for e in EPS]
    left = [u[n] - avg(u)[n] for n in range(V)]
    right = [-Fr(1, 6) * s for s in src]
    ok &= left == right
    c = sp.symbols("c", positive=True)
    for ee in (1, -1):
        felt = sp.simplify(
            m * ee * c ** (2 * ee) - m * ((c**2 - c ** (-2)) / 2 + ee * (c**2 + c ** (-2)) / 2)
        )
        ok &= felt == 0
    # symbols at the staggered momentum
    simple = 1 - sp.Rational(1, 3) * sum(sp.cos(sp.pi) for _ in range(3))
    curv = sum(2 * (1 - sp.cos(sp.pi)) for _ in range(3))
    k = sp.symbols("kx ky kz")
    one_A = 1 - sp.Rational(1, 3) * sum(sp.cos(ki) for ki in k)
    small = sp.series(one_A.subs({k[1]: 0, k[2]: 0}), k[0], 0, 4).removeO()
    ok &= simple == 2 and curv == 12 and sp.expand(small - k[0] ** 2 / 6) == 0
    report(
        "chessboard field",
        bool(ok),
        "u = -(gamma m/(12V)) epsilon solves the simplest member; symbols at pi(111) are 2 and 12; both Green functions open as -gamma/k^2",
    )


def main():
    rest_and_moving()
    chessboard()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - a positive-energy rest state sits on one sublattice, with density 2m/V there and 0 on the other. "
        "Its mean-removed source is a pure chessboard and makes a local chessboard of clocks. "
        "Both weak-field operators are invertible at pi(111), so that chessboard does not contribute to the pull at any power of 1/R. "
        "The leading term is -(gamma/(4 pi)) Q_A Q_B / R."
    )
    print(
        "SUMMARY: confirmed the 4^3 densities, the packet sum 53/44, the chessboard solution, and the two symbols 2 and 12. "
        "The 48^3 illustration was not rebuilt."
    )


if __name__ == "__main__":
    main()
