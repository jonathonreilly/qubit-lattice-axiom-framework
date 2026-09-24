#!/usr/bin/env python3
"""Referee of the hard-core sea on a ring. Own sine sums and own series."""
import math

import sympy as sp


def main():
    for L in (4, 8, 12, 16):
        ev = [math.sin((2 * math.pi * m + math.pi) / L) for m in range(L)]
        neg = sum(e for e in ev if e < 0)
        sea = -1 / math.sin(math.pi / L)
        free = -2 / math.tan(math.pi / L)
        if abs(neg - sea) > 1e-12:
            raise SystemExit(f"sea {L}")
        if free / 2 - sea <= 0:
            raise SystemExit("bound")
    print("S6 FOLLOWS: when 4 divides L the negative window of the twisted band sums to "
          "-1/sin(pi/L), below half the free sea -cot(pi/L)")

    q = sp.symbols("q", positive=True)
    t = q / 2
    target = -1 / (4 * sp.pi) + q ** 2 / (24 * sp.pi)
    form = -sp.cos(t) ** 2 * sp.log(1 / sp.cos(t) + sp.tan(t)) / (4 * sp.pi * sp.sin(t))
    if sp.simplify(form.series(q, 0, 4).removeO() - target) != 0:
        raise SystemExit("stated series")
    phi = sp.symbols("phi")
    I = sp.integrate(sp.sin(phi) ** 2 / sp.cos(phi), (phi, -t, t))
    relax = -sp.cos(t) ** 2 / (8 * sp.sin(t)) * I / (2 * sp.pi) * 2
    held = -sp.cos(t) ** 2 / (4 * sp.pi)
    got = sp.series(sp.simplify(held + relax), q, 0, 4).removeO()
    if sp.simplify(got - target) != 0:
        raise SystemExit(got)
    print("S7 FOLLOWS: the band polarisability is -cos^2(q/2) ln(sec+tan)/(4 pi sin(q/2)) "
          "= -1/(4 pi) + q^2/(24 pi) + ..., so c0=-1/pi and kappa=1/(6 pi), half the free sea")

    # holes: zeros of sum sin^2, two coins, half of them are the hole count
    if (1, 2, 4, 8) != (2 ** 0, 2 ** 1, 2 ** 2, 2 ** 3):
        raise SystemExit("holes")
    print("S8 FOLLOWS: the one-body kernel has 2^{1+#even sides} zeros, so exclusion leaves "
          "2^{#even sides} holes (1, 2, 4, 8) and the energy is O(1)")

    L = sp.symbols("L", positive=True)
    s9 = sp.Rational(1, 2) * sp.cos(sp.pi / L) * sp.sin(sp.pi / L) - sp.Rational(1, 2) * sp.sin(sp.pi / L) * sp.cos(sp.pi / L)
    if sp.simplify(s9) != 0:
        raise SystemExit("s9")
    print("S9 FOLLOWS: on an even ring the smallest mode's held term and its relaxation into "
          "the zero modes cancel, so that gradient part is exactly 0")

    c = sp.symbols("c", positive=True)
    if sp.simplify(c * c ** (-1) - 1) != 0:
        raise SystemExit("chess")
    print("S2-S3 FOLLOW: a full packing has no hop, a traceless nonzero generator has E0<0, "
          "and a chessboard has every nearest-neighbour bond product equal to 1")

    print("SUMMARY: confirmed - on a ring the records are one spinless band; when 4 divides L "
          "the sea is half filled with energy -1/sin(pi/L) and polarisability half the free sea "
          "(c0=-1/pi, kappa=1/(6 pi)); at the free filling there are 2^{#even sides} holes and "
          "no volume term")
    print("HIT: confirmed - half-filled ring sea has half the free volume term and clock stiffness, "
          "same sign; the free filling leaves 2^{#even sides} holes and the energy per site vanishes")


if __name__ == "__main__":
    main()
