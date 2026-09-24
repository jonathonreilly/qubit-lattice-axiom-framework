#!/usr/bin/env python3
"""Independent checks for the two-level signed families."""
from fractions import Fraction as F
import cmath


def green_ok():
    a = F(3, 5)
    c = F(5, 8)
    r = F(1, 3)

    def G(x):
        return c * r ** abs(x)

    # (2 - a (T+Tinv)) G = delta
    for x in range(-20, 21):
        val = 2 * G(x) - a * (G(x + 1) + G(x - 1))
        want = F(1) if x == 0 else F(0)
        if val != want:
            return False
    for x in range(-10, 11):
        val = 2 * (F(-abs(x), 2)) - (F(-abs(x + 1), 2) + F(-abs(x - 1), 2))
        want = F(1) if x == 0 else F(0)
        if val != want:
            return False
    return True


def main():
    # a = 5/4 at k=0: root a + sqrt(a^2-1) = 2
    a = F(5, 4)
    root = a + (a * a - 1).numerator ** F(1)  # not sqrt of fraction easily
    disc = a * a - 1
    ok = disc == F(9, 16)
    big = a + F(3, 4)
    ok &= big == 2
    print("unstable root", big, ok)
    # nearest-neighbour average: arccos(cos k) = |k| on (-pi, pi]
    good = 0
    for m in range(0, 13):
        k = cmath.pi * m / 12
        w = cmath.acos(cmath.cos(k).real)
        if abs(w - abs(k)) < 1e-12:
            good += 1
    print("arccos samples", good)
    ok &= good == 13
    ok &= green_ok()
    print("greens", green_ok())
    if ok:
        print(
            "HIT: confirmed - a=5/4 has a root 2 at k=0, the 1D average has omega=|k|, "
            "G=(5/8) 3^{-|x|} at cos theta=3/5, and G=-|x|/2 at a=1"
        )
        print(
            "SUMMARY: confirmed the a-family stability edge and the static kernels; "
            "the multi-level classification was not re-proved from scratch"
        )
    else:
        print("SUMMARY: fails at a checked identity")


if __name__ == "__main__":
    main()
