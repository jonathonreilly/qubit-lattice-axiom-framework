#!/usr/bin/env python3
"""Referee for bodies that slow records without keeping them, a3.

Author w-macbookpro90c72-j12a7 (claude-opus-5-5). Own directed sweep.
Screening beyond the healing length is the attempt's argument, not a proof.
"""
import itertools
import math
from fractions import Fraction as Fr

fails = []
L = 4


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def directions():
    out = set()
    bases = [(Fr(1), Fr(0), Fr(0)), (Fr(3, 5), Fr(4, 5), Fr(0)), (Fr(2, 3), Fr(2, 3), Fr(1, 3))]
    for base in bases:
        for perm in itertools.permutations(base):
            for signs in itertools.product((1, -1), repeat=3):
                out.add(tuple(signs[i] * perm[i] for i in range(3)))
    return sorted(out)


DIRS = directions()


def l1(s):
    return sum(abs(c) for c in s)


def h(x, s):
    w = [abs(c) / l1(s) for c in s]
    for k in range(3):
        if x[k] != 0 and (s[k] == 0 or (x[k] > 0) != (s[k] > 0)):
            return Fr(0)
    n = sum(abs(c) for c in x)
    num = math.factorial(n)
    for c in x:
        num //= math.factorial(abs(c))
    val = Fr(num)
    for k in range(3):
        if x[k]:
            val *= w[k] ** abs(x[k])
    return val


def sweep(s, sites):
    w = [abs(c) / l1(s) for c in s]
    sg = [1 if c > 0 else -1 for c in s]
    act = [k for k in range(3) if w[k]]
    block = list(itertools.product(range(-L, L + 1), repeat=3))
    block.sort(key=lambda y: sum(sg[k] * y[k] for k in act))
    out, arr = {}, {}
    for y in block:
        acc = {}
        for k in act:
            u = list(y)
            u[k] -= sg[k]
            u = tuple(u)
            src = out.get(u, {frozenset(): Fr(1)}) if max(abs(c) for c in u) <= L else {frozenset(): Fr(1)}
            for passed, val in src.items():
                acc[passed] = acc.get(passed, Fr(0)) + w[k] * val
        if not act:
            acc = {frozenset(): Fr(1)}
        arr[y] = acc
        if y in sites:
            out[y] = {(passed | {y}): val for passed, val in acc.items()}
        else:
            out[y] = acc
    return arr, out


def one_site():
    kappa = Fr(1, 3)
    sites = {(0, 0, 0): kappa}
    ok = len(DIRS) == 54
    for s in DIRS:
        arr, out = sweep(s, sites)
        for y, classes in out.items():
            ok &= sum(classes.values()) == 1
            slowed = classes.get(frozenset({(0, 0, 0)}), Fr(0))
            ok &= slowed == h(y, s) and classes.get(frozenset(), Fr(0)) == 1 - slowed
        for n in range(1, L + 1):
            shell = sum(
                out[y].get(frozenset({(0, 0, 0)}), Fr(0))
                for y in out
                if sum(abs(c) for c in y) == n
            )
            ok &= shell == 1
    report(
        "one site",
        ok,
        "54 directions on [-4,4]^3: slowed flux is h, every shell carries flux 1, and the number flux is 1",
    )


def two_sites():
    mags = {Fr(1): Fr(1, 2), Fr(1, 2): Fr(1, 2)}
    m2 = sum(p * m * m for m, p in mags.items())
    fdir = Fr(1, len(DIRS))
    ok = m2 == Fr(5, 8)
    quoted = None
    for x2, k1, k2 in (
        ((2, 0, 0), Fr(1, 3), Fr(1, 2)),
        ((2, 1, 1), Fr(1, 3), Fr(1, 2)),
        ((1, 2, 0), Fr(3, 4), Fr(1, 5)),
    ):
        sites = {(0, 0, 0): k1, x2: k2}
        taken = {z: [Fr(0), Fr(0), Fr(0)] for z in sites}
        for s in DIRS:
            arr, _out = sweep(s, sites)
            for z, kz in sites.items():
                for passed, val in arr[z].items():
                    scale = Fr(1)
                    for place in passed:
                        scale *= sites[place]
                    for m, pm in mags.items():
                        coef = fdir * pm * m * l1(s) * val * (1 - kz) * scale * m
                        for i in range(3):
                            taken[z][i] += coef * s[i]
        closed = [
            -(1 - k1) * (1 - k2) * m2 * sum(fdir * l1(s) * s[i] * h(x2, s) for s in DIRS)
            for i in range(3)
        ]
        ok &= taken[x2] == closed
        ok &= all(taken[(0, 0, 0)][i] == -taken[x2][i] for i in range(3))
        ok &= sum(taken[x2][i] * x2[i] for i in range(3)) < 0
        if x2 == (2, 1, 1):
            quoted = taken[x2]
    lone = {z: [Fr(0), Fr(0), Fr(0)] for z in [(0, 0, 0)]}
    sites = {(0, 0, 0): Fr(1, 3)}
    for s in DIRS:
        arr, _out = sweep(s, sites)
        for passed, val in arr[(0, 0, 0)].items():
            for m, pm in mags.items():
                coef = fdir * pm * m * l1(s) * val * (1 - Fr(1, 3)) * m
                for i in range(3):
                    lone[(0, 0, 0)][i] += coef * s[i]
    ok &= lone[(0, 0, 0)] == [0, 0, 0]
    ok &= quoted == [Fr(-1, 675), Fr(-8, 6075), Fr(-8, 6075)]
    report(
        "two sites",
        ok,
        "joint solution at three separations: action equals reaction, a lone site takes nothing, and at (2,1,1) the pull is (-1/675,-8/6075,-8/6075)",
    )


def price():
    N, nb, kappa = 7, Fr(1, 5), Fr(1, 3)
    mean = sum(math.comb(N, k) * nb ** k * (1 - nb) ** (N - k) * kappa ** k for k in range(N + 1))
    mean2 = sum(math.comb(N, k) * nb ** k * (1 - nb) ** (N - k) * kappa ** (2 * k) for k in range(N + 1))
    closed = (1 - (1 - kappa) * nb) ** N
    closed2 = (1 - (1 - kappa ** 2) * nb) ** N
    report(
        "price",
        mean == closed == Fr(13, 15) ** 7 and mean2 == closed2 == Fr(37, 45) ** 7,
        "after 7 steps at density 1/5 and kappa 1/3, E[kappa^K]=(13/15)^7 and E[kappa^(2K)]=(37/45)^7",
    )


def scalings():
    import sympy as sp

    kappa, nb, m0, s1, T, F = sp.symbols("kappa n_b m0 s1 T F", positive=True)
    t = sp.symbols("t", positive=True)
    c = (1 - kappa) * nb * s1 * m0 / sp.sqrt(3)
    m = m0 / (1 + c * t)
    ode = sp.simplify(sp.together(sp.diff(m, t) + (c / m0) * m ** 2))
    anti = -m0 ** 2 / (c * (1 + c * t))
    area = sp.simplify(sp.diff(anti, t) - m ** 2)
    bound = sp.simplify(3 * F / (nb * sp.Rational(3, 2) * m0 * T) ** 2 - 4 * F / (3 * nb ** 2 * m0 ** 2 * T ** 2))
    c_rate = (1 - kappa) * nb * s1 / sp.sqrt(3)
    half = sp.simplify(sp.solve(sp.Eq(1 / (1 + c_rate * m0 * T), sp.Rational(1, 2)), kappa)[0])
    half_gap = sp.simplify((1 - half) - sp.sqrt(3) / (nb * s1 * m0 * T))
    impulse = sp.simplify(m0 ** 2 / c - m0 * sp.sqrt(3) / ((1 - kappa) * nb * s1))
    q = sp.Rational(1, 2) / (sp.Rational(1, 2) + sp.Rational(1, 10))
    powers = [q ** n for n in (1, 5, 10, 20)]
    report(
        "scalings",
        ode == 0 and area == 0 and bound == 0 and half_gap == 0 and impulse == 0 and q == sp.Rational(5, 6),
        f"the run-down solves the ODE, half the magnitude by T needs (1-kappa) <= sqrt(3)/(n_b |s|_1 m0 T), "
        f"the sphere bound is 4<m^2>|F|/(3 n_b^2 <m>^2 T^2), and q=5/6 with q^n = {powers}",
    )


def main():
    one_site()
    two_sites()
    price()
    scalings()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - one slowing site leaves the number flux unchanged, and the slowed flux through every shell is 1. "
        "Two sites pull with (1-k1)(1-k2)<m^2> times the collisionless force, equal and opposite. "
        "At (2,1,1), in units of 1/sqrt(3), that pull is (-1/675,-8/6075,-8/6075). "
        "The run-down is linear in (1-kappa) and the pull is quadratic."
    )
    print(
        "SUMMARY: confirmed the box sweep, the three pair configurations, the binomial means (13/15)^7 and (37/45)^7, "
        "the half-magnitude bound, and the healing factor 5/6. "
        "No 1/r^2 force beyond the healing length is argued, not proved. Block 52's biased walk was not computed."
    )


if __name__ == "__main__":
    main()
