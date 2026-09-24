#!/usr/bin/env python3
"""Independent checks: E(k+pi)=12-E, and the layer-half quadratic form is negative."""
from fractions import Fraction as F
import itertools


def main():
    # E(k+(pi,pi,pi)) = 12 - E(k)
    ok = True
    for n in itertools.product(range(4), repeat=3):
        E = sum(2 * (1 - F(int(round(__import__("math").cos(__import__("math").pi * a / 2))), 1)) for a in n)
    # exact cos of multiples of pi/2
    cos = {0: 1, 1: 0, 2: -1, 3: 0}
    for n in itertools.product(range(4), repeat=3):
        E = sum(2 * (1 - cos[a]) for a in n)
        Ep = sum(2 * (1 - cos[(a + 2) % 4]) for a in n)
        ok &= Ep == 12 - E
    # staggered vector on 2x2x2, z-component 2*(-1)^parity
    sites = list(itertools.product(range(2), repeat=3))
    d = {x: 2 * (1 if sum(x) % 2 == 0 else -1) for x in sites}
    ident = sum(d[x] * d[x] for x in sites)
    off = 0
    undirected = 0
    for x in sites:
        for a in range(3):
            for step in (1, -1):
                y = list(x)
                y[a] = (y[a] + step) % 2
                y = tuple(y)
                off += d[x] * d[y]
    # each undirected edge counted twice above
    undirected = off // 2
    directed = ident + off
    half = ident + undirected
    print(f"E identity {ok} <d,d>={ident} directed={directed} undirected-off={half}")
    ok &= ident == 32 and directed == -160 and half == -64
    ok &= directed < 0 and half < 0
    if ok:
        print(
            "HIT: confirmed - E(k+(pi,pi,pi))=12-E(k), and the staggered 2x2x2 form is -160 for the symmetric adjacency "
            "and -64 for the undirected off-diagonal count the author quotes; both are negative, so the layer halves are not reflection positive"
        )
        print(
            "SUMMARY: confirmed the no-go for the layer halves; the numerical beta_0 was not recomputed"
        )
    else:
        print("SUMMARY: fails at the quadratic form or the spectrum identity")


if __name__ == "__main__":
    main()
