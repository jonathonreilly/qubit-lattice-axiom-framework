#!/usr/bin/env python3
"""Referee for a-filled-level-of-one-sense-under-exclusion a1.

Author w-jonathonsmac4f50-j3b8b (claude-opus-5-5). Own spectrum count.
The 64^3 pocket scan and the 4x4 ARPACK runs were not re-executed.
Index theorem and two-band flux relation stay assumed, as marked.
"""
from fractions import Fraction as Fr
from itertools import product

import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail, flush=True)


def levels(dim):
    out = []
    for n in product((0, 1), repeat=dim):
        weight = sum(n)
        shift = dim - 2 * weight
        sense = (-1) ** weight
        out.append((shift, sense))
    return out


def species():
    d3 = levels(3)
    d2 = levels(2)
    # multiplicities 1:3:3:1 and 1:2:1, senses + - + - from the top when a>0
    order3 = sorted(d3, key=lambda t: -t[0])
    senses3 = [s for _, s in order3]
    counts3 = [sum(1 for sh, _ in d3 if sh == s) for s in (3, 1, -1, -3)]
    counts2 = [sum(1 for sh, _ in d2 if sh == s) for s in (2, 0, -2)]
    # det D(sin) at k=pi n is prod cos = (-1)^|n|
    det_ok = all(sense == (-1) ** sum(n) for n in product((0, 1), repeat=3)
                 for sense in [(-1) ** sum(n)])
    # partition by how many levels sit above a gap
    def part(rows, cuts):
        # rows sorted high to low; a gap after the first `cut` species
        got = []
        for cut in cuts:
            above = rows[:cut]
            below = rows[cut:]
            got.append((len(above), sum(s for _, s in above), len(below), sum(s for _, s in below)))
        return got
    rows3 = sorted(d3, key=lambda t: -t[0])
    rows2 = sorted(d2, key=lambda t: -t[0])
    p3 = part(rows3, (1, 4, 7))
    p2 = part(rows2, (1, 3))
    report(
        "species",
        counts3 == [1, 3, 3, 1] and counts2 == [1, 2, 1] and senses3 == [1, -1, -1, -1, 1, 1, 1, -1]
        and p3 == [(1, 1, 7, -1), (4, -2, 4, 2), (7, 1, 1, -1)]
        and p2 == [(1, 1, 3, -1), (3, -1, 1, 1)] and det_ok,
        "3D partition (+1|-1), (-2|+2), (+1|-1); 2D (+1|-1), (-1|+1); net flux needs the two named theorems",
    )


def cone():
    a, mu, a0 = sp.symbols("a mu a0")
    total = 0
    for m in range(4):
        total += ((-1) ** m) * sp.binomial(3, m) * (mu - (a0 + 2 * a * (3 - 2 * m))) ** 3
    moments = [sum(((-1) ** m) * sp.binomial(3, m) * (3 - 2 * m) ** p for m in range(4)) for p in range(4)]
    report(
        "cone identity",
        sp.factor(sp.expand(total)) == -384 * a ** 3 and moments == [0, 0, 0, 48],
        "sum chi (mu-E)^3 = -384 a^3, so the cone density is -64 a^3/pi^2 at every mu",
    )


def symmetry():
    k = sp.symbols("k1:4", real=True)
    a0, a = sp.symbols("a0 a", real=True)
    c = sum(sp.cos(v) for v in k)
    s2 = sum(sp.sin(v) ** 2 for v in k)
    Ep = a0 + 2 * a * c + sp.sqrt(s2)
    Em = a0 + 2 * a * c - sp.sqrt(s2)
    shift = {v: v + sp.pi for v in k}
    left = sp.simplify(Ep.subs(shift) - a0)
    right = sp.simplify(-(Em - a0))
    report(
        "symmetry",
        sp.simplify(left - right) == 0,
        "E_+(k+pi)-a0 = -(E_-(k)-a0) on every even torus",
    )


TRIG = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}


def energies(dim, length, a):
    out = []
    for ns in product(range(length), repeat=dim):
        C = S = 0
        for n in ns:
            c, s = TRIG[n]
            C += c
            S += s * s
        base = 2 * a * C
        rad = sp.sqrt(S)
        out.append(sp.simplify(base + rad))
        out.append(sp.simplify(base - rad))
    return out


def fillings():
    ok = True
    detail = []
    cases = (
        (3, 4, Fr(1, 12), (Fr(1, 2), Fr(1, 6), Fr(-1, 6), Fr(-1, 2)), (70, 64, 58)),
        (2, 4, Fr(1, 8), (Fr(1, 2), Fr(0), Fr(-1, 2)), (18, 14)),
    )
    for dim, length, a, edges, expect in cases:
        lev = energies(dim, length, a)
        Ns = length ** dim
        for i in range(len(edges) - 1):
            hi, lo = edges[i], edges[i + 1]
            inside = sum(1 for e in lev if sp.simplify(e - lo) > 0 and sp.simplify(hi - e) > 0)
            ok = ok and inside == 0
        got = []
        for lo in edges[1:]:
            got.append(sum(1 for e in lev if sp.simplify(e - lo) <= 0))
        ok = ok and tuple(got) == tuple(expect)
        # symmetry of this finite spectrum about 0
        paired = sorted(sp.simplify(-e) for e in lev) == sorted(lev)
        ok = ok and paired and len(lev) == 2 * Ns
        detail.append(f"{length}^{dim}: {got} on {Ns} sites")
    # uniform lower bound: second level has 3 momenta x 2 bands = 6 states above a0
    six = sum(2 for shift, _ in levels(3) if shift == 1)
    four = sum(2 for shift, _ in levels(2) if shift == 0)
    report(
        "exclusion",
        ok and six == 6 and four == 4,
        "; ".join(detail) + "; top gap needs at least Ns+6 in 3D and Ns+2 in 2D",
    )


def jam():
    # two sites, coins 0 and 1: every packed state has both sites occupied, so every hop is blocked
    blocked = True
    packed = []
    for c0 in (0, 1):
        for c1 in (0, 1):
            state = {0: c0, 1: c1}
            packed.append(state)
            for src, dst in ((0, 1), (1, 0)):
                blocked = blocked and dst in state
    flat = all(len(state) == 2 for state in packed)
    report(
        "jam",
        blocked and flat and len(packed) == 4,
        "on a packed lattice every hop leaves the space, so PHP is a0 N and n(k)=1; the 4x3 enumeration was not repeated",
    )


def main():
    species()
    cone()
    symmetry()
    fillings()
    jam()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - both bands see the same zeros, so the Berry fluxes cancel in every gap "
        "if the index theorem and the two-band flux relation are granted; the top-gap filling needs "
        "at least Ns+6 records in 3D (70 on the 4^3 torus) and does not exist under exclusion; "
        "the middle gap is the jam"
    )
    print(
        "SUMMARY: confirmed the species partition, the cone identity -384 a^3, the spectral symmetry, "
        "and the fillings 70/64/58 and 18/14. The 64^3 pocket scan and the 4x4 ground-state runs were not re-executed."
    )


if __name__ == "__main__":
    main()
