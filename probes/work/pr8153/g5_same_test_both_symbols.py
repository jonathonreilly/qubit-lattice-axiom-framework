#!/usr/bin/env python3
"""J:attack:PR8153 — pattern (b) SAME TEST, BOTH SIDES on G5.

G5: the ordered unsoldered static law carries the lattice Green symbol 1/E(k)
in the transverse channel, which the formation law (parabolic) does not.
Test: on the L=4 plane, is S(k)*E(k) independent of k? Applied to
  static symbol S=1/E  (product identically 1)
  formation S=1/(1-u(q)) with u=|phi|^2, E=2(1-cos q1)+2(1-cos q2)
Exact Fraction. HIT if both objects pass or both fail this constancy test.
"""
from __future__ import annotations

from fractions import Fraction

COS = (Fraction(1), Fraction(0), Fraction(-1), Fraction(0))


def c(n: int) -> Fraction:
    return COS[n % 4]


def u(n1: int, n2: int) -> Fraction:
    return (3 + 2 * c(n1) + 2 * c(n2) + 2 * c(n1 - n2)) / 9


def E(n1: int, n2: int) -> Fraction:
    return 2 * (1 - c(n1)) + 2 * (1 - c(n2))


def main() -> None:
    static_prod = set()
    form_prod = set()
    for n1 in range(4):
        for n2 in range(4):
            if (n1, n2) == (0, 0):
                continue
            ee = E(n1, n2)
            static_prod.add(ee * (1 / ee))
            onemu = 1 - u(n1, n2)
            form_prod.add(ee / onemu)
            print(f"k=2pi({n1},{n2})/4  E={ee}  1-u={onemu}  E/(1-u)={ee/onemu}")
    print(f"static S=1/E products {static_prod}")
    print(f"formation E/(1-u) values {sorted(form_prod)}")
    static_const = len(static_prod) == 1
    form_const = len(form_prod) == 1
    if static_const == form_const:
        print(
            "HIT: G5 same-test both-sides: constancy of S(k) E(k) is "
            f"{'shared' if static_const else 'shared-absent'} by static 1/E and formation 1/(1-u)"
        )
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES on G5 - FIRES")
    else:
        print(
            "SUMMARY: attack pattern (b) SAME TEST BOTH SIDES on G5 - static S=1/E has "
            f"constant S E ({static_prod}); formation 1/(1-u) has E/(1-u) in {sorted(form_prod)}; "
            "the objects differ as G5 states; attack does not fire"
        )


if __name__ == "__main__":
    main()
