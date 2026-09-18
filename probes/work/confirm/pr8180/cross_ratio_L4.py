#!/usr/bin/env python3
"""J:confirm:J-falsifier:PR8180 — independent T-a product-form census at L=4.

Finder (claude-opus-5) used exact cross-ratios on L=4,6 plus FFT quadrature.
This script only uses L=4 rational cosines {1,0,-1,0} and Fraction arithmetic,
with a nested-index census (not the finder's dict-of-pairs helper). HIT if both
the formation spectral density and 1/E fail to be a plane x axis product.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

COS = (Fraction(1), Fraction(0), Fraction(-1), Fraction(0))
L = 4


def cos(n: int) -> Fraction:
    return COS[n % L]


def u(n1: int, n2: int) -> Fraction:
    return (3 + 2 * cos(n1) + 2 * cos(n2) + 2 * cos(n1 - n2)) / 9


def E(n1: int, n2: int, n3: int) -> Fraction:
    return 6 - 2 * cos(n1) - 2 * cos(n2) - 2 * cos(n3)


def Dform(n1: int, n2: int, m: int) -> Fraction:
    return 1 + u(n1, n2) - Fraction(2, 3) * (cos(m) + cos(n1 + m) + cos(n2 + m))


def census(F) -> tuple[int, int, Fraction | None]:
    plane = [(n1, n2) for n1, n2 in product(range(L), repeat=2) if (n1, n2) != (0, 0)]
    axis = list(range(L))
    tot = bad = 0
    wit = None
    for i, p in enumerate(plane):
        for p2 in plane[i + 1 :]:
            for j, a in enumerate(axis):
                for a2 in axis[j + 1 :]:
                    v = (F(p, a), F(p2, a2), F(p, a2), F(p2, a))
                    if any(x == 0 for x in v):
                        continue
                    tot += 1
                    R = v[0] * v[1] / (v[2] * v[3])
                    if R != 1:
                        bad += 1
                        if wit is None:
                            wit = R
    return tot, bad, wit


def main() -> None:
    id_ok = True
    n = 0
    for n1, n2, m in product(range(L), repeat=3):
        n += 1
        if E(n1 + m, n2 + m, m) != 3 * (Dform(n1, n2, m) + 1 - u(n1, n2)):
            id_ok = False
    print(f"identity E(q1+w,q2+w,w)=3(Dform+1-u) on L=4: {id_ok} over {n} points")

    rows = {
        "formation": census(lambda p, a: 1 / Dform(p[0], p[1], a)),
        "comparator_e3": census(lambda p, a: 1 / E(p[0], p[1], a)),
        "comparator_111": census(lambda p, a: 1 / E(p[0] + a, p[1] + a, a)),
    }
    for name, (tot, bad, wit) in rows.items():
        print(f"L=4 {name}: quadruples={tot} R!=1 {bad} first_R={wit}")

    form_bad = rows["formation"][1]
    comp_bad = rows["comparator_e3"][1] + rows["comparator_111"][1]
    if form_bad and comp_bad:
        print(
            "HIT: confirmed - at L=4 both the formation spectral density and 1/E fail the "
            f"exact plane x axis cross-ratio test (formation {form_bad}/{rows['formation'][0]}, "
            f"comparator e3 {rows['comparator_e3'][1]}/{rows['comparator_e3'][0]}, "
            f"111 {rows['comparator_111'][1]}/{rows['comparator_111'][0]}); T3/D2's product-form "
            "separation does not hold in this representation"
        )
        print(
            "SUMMARY: confirmed T3/D2 product-form test does not separate the kernels at L=4: "
            "both fail exact cross-ratio separability; identity 1/G^=3(1/C^+1-u) holds"
        )
    else:
        print("SUMMARY: not reproduced - one of the kernels was a product on the L=4 grid")


if __name__ == "__main__":
    main()
