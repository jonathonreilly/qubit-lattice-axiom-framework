#!/usr/bin/env python3
"""Referee for moving-kernel-with-vacancies a4.

Author w-jonathonsmac4f50-jb1d8 (claude-opus-5). Own Ising sums on the induced subgraphs.
FKG and the value of 3G(0) are not re-proved.
"""
from itertools import product
from fractions import Fraction as Fr
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def ring(n):
    sites = [(i,) for i in range(n)]
    bonds = [((i,), ((i + 1) % n,)) for i in range(n)]
    return sites, bonds


def torus(L):
    sites = [(i, j) for i in range(L) for j in range(L)]
    bonds = []
    for i, j in sites:
        bonds.append(((i, j), ((i + 1) % L, j)))
        bonds.append(((i, j), (i, (j + 1) % L)))
    return sites, bonds


def partition(sites, bonds, w):
    """mask -> z-free content sum on the induced subgraph."""
    index = {s: i for i, s in enumerate(sites)}
    induced = []
    for a, b in bonds:
        induced.append((index[a], index[b]))
    out = []
    n = len(sites)
    for mask in range(1 << n):
        bits = [i for i in range(n) if mask >> i & 1]
        inner = [(i, j) for i, j in induced if (mask >> i & 1) and (mask >> j & 1)]
        total = Fr(0)
        for cfg in product((1, -1), repeat=len(bits)):
            spin = {bits[t]: cfg[t] for t in range(len(bits))}
            weight = Fr(1)
            for i, j in inner:
                weight *= w if spin[i] == spin[j] else 1 / w
            total += weight
        out.append(total)
    return out


def marginals():
    sites, bonds = ring(4)
    zpart = partition(sites, bonds, Fr(2))
    empty = zpart[0] == 1
    one = zpart[1] == 2
    adjacent = zpart[0b0011] == 2 * (Fr(2) + Fr(1, 2))
    opposite = zpart[0b0101] == 4
    report(
        "induced partition",
        empty and one and adjacent and opposite,
        "on a 4-ring at w=2, Z_empty=1, Z_one=2, adjacent=5, and two opposite sites (no bond) give 4",
    )


def lattice(name, sites, bonds, w, z):
    n = len(sites)
    base = partition(sites, bonds, w)
    mu = [z ** bin(mask).count("1") * base[mask] for mask in range(1 << n)]
    bad = 0
    pairs = 0
    for a in range(1 << n):
        for b in range(a, 1 << n):
            pairs += 1
            if mu[a | b] * mu[a & b] < mu[a] * mu[b]:
                bad += 1
    return bad, pairs


def lattices():
    specs = [
        ("ring6", ring(6), Fr(2), Fr(1), 2080),
        ("ring6", ring(6), Fr(3), Fr(1, 2), 2080),
        ("ring8", ring(8), Fr(2), Fr(2), 32896),
        ("torus3", torus(3), Fr(2), Fr(1), 131328),
    ]
    ok = True
    detail = []
    for name, graph, w, z, expect in specs:
        bad, pairs = lattice(name, graph[0], graph[1], w, z)
        ok &= bad == 0 and pairs == expect
        detail.append(f"{name}@{w},{z}:{pairs}")
    # zero coupling is an equality, not only an inequality
    sites, _bonds = ring(6)
    n = len(sites)
    z = Fr(1, 3)
    mu = [(2 * z) ** bin(mask).count("1") for mask in range(1 << n)]
    tight = all(
        mu[a | b] * mu[a & b] == mu[a] * mu[b]
        for a in range(1 << n)
        for b in range(a, 1 << n)
    )
    report(
        "lattice condition",
        ok and tight,
        "no violations in " + ", ".join(detail) + "; at w=1 the 6-ring marginal multiplies exactly",
    )


def densities():
    sites, bonds = torus(3)
    n, bcount = len(sites), len(bonds)
    rows = []
    for w in (Fr(1), Fr(2), Fr(4)):
        base = partition(sites, bonds, w)
        for z in (Fr(1, 8), Fr(1, 4), Fr(1, 2), Fr(1), Fr(2)):
            part = occ = oo = Fr(0)
            for mask in range(1 << n):
                weight = z ** bin(mask).count("1") * base[mask]
                part += weight
                occ += weight * bin(mask).count("1")
                both = 0
                for u, v in bonds:
                    iu = sites.index(u)
                    iv = sites.index(v)
                    if (mask >> iu & 1) and (mask >> iv & 1):
                        both += 1
                oo += weight * both
            rho, rho2 = occ / (part * n), oo / (part * bcount)
            rows.append((w, z, rho, rho2))
    low = [row for row in rows if row[2] < Fr(1, 2)]
    closed = all(
        rho == 2 * z / (1 + 2 * z) and rho2 == rho * rho
        for w, z, rho, rho2 in rows
        if w == 1
    )
    ok = (
        len(rows) == 15
        and all(rho2 >= rho * rho for _, _, rho, rho2 in rows)
        and len(low) == 4
        and all(2 * rho - 1 < 0 <= rho * rho <= rho2 for _, _, rho, rho2 in low)
        and closed
    )
    report(
        "densities",
        ok,
        "15 exact 3x3 points have rho_2 >= rho^2; four have rho<1/2; at w=1, rho=2z/(1+2z) and rho_2=rho^2",
    )


def thresholds():
    rho = sp.symbols("rho", positive=True)
    gap = sp.factor(sp.together(rho ** 2 - (2 * rho - 1)))
    old_vs_new = sp.simplify(sp.together(1 / rho ** 3 - 1 / (rho * (2 * rho - 1))))
    at_one = sp.simplify((rho ** 2 - (2 * rho - 1)).subs(rho, 1))
    below = all(2 * Fr(p, q) - 1 < 0 for p, q in ((1, 4), (2, 5)))
    above = []
    for value in (Fr(3, 5), Fr(9, 10)):
        new = 1 / value ** 3
        old = 1 / (value * (2 * value - 1))
        above.append(new < old)
    report(
        "thresholds",
        gap == (rho - 1) ** 2 and at_one == 0 and old_vs_new.subs(rho, Fr(3, 5)) < 0 and below and all(above),
        "rho^2-(2rho-1)=(rho-1)^2, so 3G/rho^3 is below 3G/(rho(2rho-1)) on (1/2,1) and equal at 1",
    )


def main():
    marginals()
    lattices()
    densities()
    thresholds()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the two-valued vacancy marginal is log-supermodular on the 6-ring, the 8-ring, "
        "and the 3x3 torus at the tested (w,z), and the 15 exact 3x3 densities satisfy rho_2 >= rho^2, "
        "including four with rho<1/2. Given that inequality, beta > 3G(0)/rho^3 is finite for every rho>0 "
        "and is strictly below 3G(0)/(rho(2rho-1)) on (1/2,1), with equality at rho=1."
    )
    print(
        "SUMMARY: confirmed the induced partition, the exhaustive lattice counts, and the threshold comparison. "
        "FKG itself and the bracket 3G(0) in (0.75, 0.76) were not re-proved. "
        "The lattice condition is checked, not proved for every graph."
    )


if __name__ == "__main__":
    main()
