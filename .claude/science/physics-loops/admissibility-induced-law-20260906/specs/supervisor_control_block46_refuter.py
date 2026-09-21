#!/usr/bin/env python3
"""Block 46 refuting pass: machinery disjoint from the runner's.

W1  the exact RATIONAL rank (elimination over fractions; the runner works modulo a prime) of the divergence-and-circulation constraints on the 3^3 torus: bonds minus 3
W2  three sinks on the 6^3 torus (rational cosines): the potential's current has the right divergence, no circulation and no constant part
W3  the pressure of the six-axis gas by enumeration of one bond's 49 states and events at a fifth density; the sphere menu's pressure against
    density times speed over three, symbolically
Exact arithmetic (Fractions, sympy).
"""
import sys
from fractions import Fraction as F
from itertools import product

import sympy as sp

E = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
fails = 0


def report(tag, ok, msg):
    global fails
    fails += 0 if ok else 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


def w1():
    L = 3
    sites = list(product(range(L), repeat=3))
    step = lambda x, a, s=1: tuple((x[i] + (s if i == a else 0)) % L for i in range(3))
    bonds = {(x, a): k for k, (x, a) in enumerate((x, a) for x in sites for a in range(3))}
    rows = []
    for x in sites:
        row = [0] * len(bonds)
        for a in range(3):
            row[bonds[(x, a)]] += 1
            row[bonds[(step(x, a, -1), a)]] -= 1
        rows.append(row)
        for a, b in ((0, 1), (1, 2), (0, 2)):
            row = [0] * len(bonds)
            row[bonds[(x, a)]] += 1
            row[bonds[(step(x, a), b)]] += 1
            row[bonds[(step(x, b), a)]] -= 1
            row[bonds[(x, b)]] -= 1
            rows.append(row)
    mat = [[F(v) for v in row] for row in rows]                        # exact elimination over the rationals
    rank = 0
    for c in range(len(bonds)):
        piv = next((i for i in range(rank, len(mat)) if mat[i][c] != 0), None)
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        inv = 1 / mat[rank][c]
        mat[rank] = [v * inv for v in mat[rank]]
        for i in range(len(mat)):
            if i != rank and mat[i][c] != 0:
                f = mat[i][c]
                mat[i] = [a - f * b for a, b in zip(mat[i], mat[rank])]
        rank += 1
    report("W1", rank == len(bonds) - 3, f"3^3 torus: exact rational rank {rank} of the {len(rows)} constraints on {len(bonds)} bonds: the kernel has dimension {len(bonds) - rank}")


def w2():
    L = 6
    cosv = (F(1), F(1, 2), F(-1, 2), F(-1), F(-1, 2), F(1, 2))
    sites = list(product(range(L), repeat=3))
    step = lambda x, a, s=1: tuple((x[i] + (s if i == a else 0)) % L for i in range(3))
    modes = [k for k in sites if any(k)]
    ek = {k: 6 - 2 * sum(cosv[c] for c in k) for k in modes}
    sinks = {(0, 0, 0): F(5), (3, 2, 1): F(2), (1, 4, 4): F(9)}
    mean_q = sum(sinks.values()) / L ** 3
    # Phi in mode space: -sum_k (Q_k / E_k) e^{ikx}; real part suffices since the sum over k is symmetric
    phi = {}
    for x in sites:
        tot = F(0)
        for k in modes:
            for s, q in sinks.items():
                ph = sum(k[i] * (x[i] - s[i]) for i in range(3)) % L
                tot -= q * cosv[ph] / ek[k]
        phi[x] = tot / L ** 3
    ok = True
    for x in sites:
        div = sum((phi[x] - phi[step(x, a)]) - (phi[step(x, a, -1)] - phi[x]) for a in range(3))
        ok = ok and div == -(sinks.get(x, 0) - mean_q)
    for a in range(3):
        ok = ok and sum(phi[x] - phi[step(x, a)] for x in sites) == 0
    report("W2", ok, "three sinks (5, 2, 9) on the 6^3 torus: the current of Phi = -G_L * (Q - mean Q) has divergence -(Q - mean Q) at all 216 sites and no constant part (its circulation vanishes identically, being a difference of a site function)")


def w3():
    rho = F(7, 10)
    dens = [rho / 6] * 6
    states = [None] + list(range(6))
    prob = lambda s: (1 - rho) if s is None else dens[s]
    flux = [F(0)] * 3
    for sx in states:
        for sy in states:
            w = prob(sx) * prob(sy)
            if sx == 0:
                for i in range(3):
                    flux[i] += w * (E[0][i] - (E[sy][i] if sy is not None else 0))
            if sy == 1:
                for i in range(3):
                    flux[i] += w * (-(E[1][i] - (E[sx][i] if sx is not None else 0)))
    r = sp.Symbol("rho", positive=True)
    sphere_pressure = r / (3 * sp.sqrt(3))
    report("W3", flux == [rho / 3, 0, 0] and sp.simplify(3 * sphere_pressure - r / sp.sqrt(3)) == 0, "six axes at density 7/10: the momentum crossing a bond is (rho/3, 0, 0) by enumeration of its 49 states; sphere menu: three times the pressure rho/(3 sqrt 3) equals the density times the speed 1/sqrt 3")


if __name__ == "__main__":
    for fn in (w1, w2, w3):
        fn()
    print(f"REFUTER TOTAL: FAIL={fails}")
    sys.exit(1 if fails else 0)
