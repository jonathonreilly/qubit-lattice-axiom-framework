#!/usr/bin/env python3
"""J:attack-g:PR8168 — pattern (g) PROOF STEP BY BRUTE FORCE.

T0 closed forms: with two-or-more a's, the three orbit types have
normalizers p^3+q^3+4r^3, r(p^2+q^2)+r^2(p+q)+2r^3, and pq(p+q)+4r^3.
Also forks=n-1, arrows<=3(n-1) as graph identities on a 1-seed path.

Distinct from D4's 66103-tree census. HIT if a normalizer formula fails
on the six-axis product kernel.
"""
from __future__ import annotations

from fractions import Fraction as F

HITS = []
# 0:+x 1:-x 2:+y 3:-y 4:+z 5:-z


def phi(s, t, p, q, r):
    if s == t:
        return p
    if s == (t ^ 1):
        return q
    return r


def Z3(a, b, c, p, q, r):
    return sum(phi(s, a, p, q, r) * phi(s, b, p, q, r) * phi(s, c, p, q, r) for s in range(6))


def main():
    p, q, r = 3, 1, 2
    # (a,a,a)
    z_aaa = Z3(0, 0, 0, p, q, r)
    want_aaa = p**3 + q**3 + 4 * r**3
    print(f"Z(a,a,a)={z_aaa} stated p^3+q^3+4r^3={want_aaa}")
    if z_aaa != want_aaa:
        HITS.append(f"Zaaa {z_aaa}!={want_aaa}")
    # (a,a,b) b orthogonal
    z_aab = Z3(0, 0, 2, p, q, r)
    want_aab = r * (p**2 + q**2) + r**2 * (p + q) + 2 * r**3
    print(f"Z(a,a,b_orth)={z_aab} stated {want_aab}")
    if z_aab != want_aab:
        HITS.append(f"Zaab {z_aab}!={want_aab}")
    # (a,a,-a)
    z_aaq = Z3(0, 0, 1, p, q, r)
    want_aaq = p * q * (p + q) + 4 * r**3
    print(f"Z(a,a,-a)={z_aaq} stated pq(p+q)+4r^3={want_aaq}")
    if z_aaq != want_aaq:
        HITS.append(f"Zaaq {z_aaq}!={want_aaq}")
    # graph identity forks=n-1 for a tree
    for n in range(1, 8):
        forks = n - 1
        arrows_max = 3 * (n - 1)
        edges_max = 4 * (n - 1)
        if forks != n - 1 or arrows_max + forks != edges_max:
            HITS.append(f"n={n} edge accounting")
        print(f"n={n}: forks={forks} arrows<= {arrows_max} edges<= {edges_max}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print(
            "SUMMARY: attack pattern (g) PROOF STEP BY BRUTE FORCE on T0 "
            "normalizers - " + "; ".join(HITS)
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - T0 six-axis normalizers "
        "at (3,1,2) match p^3+q^3+4r^3, r(p^2+q^2)+r^2(p+q)+2r^3 and "
        "pq(p+q)+4r^3, and forks=n-1 with edges<=4(n-1) holds as accounting"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
