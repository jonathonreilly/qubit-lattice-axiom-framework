#!/usr/bin/env python3
"""J:falsifier:PR8079 — independent exact checks of the rho4 ellipse identity and Q5 division.

HIT if (3/2)^2-(17/16)^2-(15/16)^2 != 31/128, or if
Q5(t)=E[X^3/(X+t^2)] fails the polynomial-division identity
X^2 - X t^2 + t^4 - t^6/(X+t^2) = X^3/(X+t^2) at tested points,
or if 15 two-link defects times degree-6 adjacency is not 90.
Disjoint from the note's packet-hash runner.
"""
from fractions import Fraction as F
from itertools import combinations


def main() -> None:
    hits = []
    ell = F(9, 4) - F(17, 16) ** 2 - F(15, 16) ** 2
    print(f"ellipse (3/2)^2-(17/16)^2-(15/16)^2 = {ell}")
    if ell != F(31, 128):
        hits.append(f"ellipse {ell} != 31/128")
    # Re z > |Im z| on the ellipse is claimed via 31/128>0
    if ell <= 0:
        hits.append("ellipse quantity not positive")
    labels = list(combinations(range(6), 2))
    degrees = [sum(not (set(a) & set(c)) for c in labels) for a in labels]
    print(f"two-link defects {len(labels)}; degrees {degrees[:3]}...; sum {sum(degrees)}")
    if labels.__len__() != 15:
        hits.append(f"{len(labels)} defects != 15")
    if degrees != [6] * 15 or sum(degrees) != 90:
        hits.append(f"adjacency degrees {degrees} sum {sum(degrees)} != 6*15=90")
    for x in [F(1), F(2), F(3), F(6), F(42)]:
        for t in [F(1, 2), F(1), F(2), F(8)]:
            lhs = x * x - x * t * t + t**4 - t**6 / (x + t * t)
            rhs = x**3 / (x + t * t)
            if lhs != rhs:
                hits.append(f"Q5 division fails at X={x} t={t}: {lhs} vs {rhs}")
    # j = 2√2 h => j^2 = 8 h^2
    if F(2) ** 2 * F(2) != F(8):
        hits.append("j^2 = 8 identity broken")
    print("(2√2)^2 = 8 holds")
    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: PR8079 ellipse/Q5/adjacency falsifier FIRED:", "; ".join(hits))
    else:
        print(
            "SUMMARY: PR8079 ellipse/Q5/adjacency falsifier did not fire: "
            "31/128, 15 defects of degree 6 summing to 90, and the Q5 "
            "polynomial-division identity at 20 test points"
        )


if __name__ == "__main__":
    main()
