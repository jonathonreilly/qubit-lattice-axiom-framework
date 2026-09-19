#!/usr/bin/env python3
"""J:attack-g:PR8137 — pattern (g) PROOF STEP BY BRUTE FORCE.

Theorem 2: K^2(+|+)-K^2(+|-) = (pplus-pminus)^2.
Theorem 3: cubic kernel a+b+4c=1, same-minus-opposite = (a-b)^2, and
Haar-square + a=b implies (6c-1)^2/3=0.

Distinct from same_test_both_orders.py (pattern b). HIT if an identity fails.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

HITS = []


def k2_plus(pp, pm):
    k2pp = pp * pp + (1 - pp) * pm
    k2pm = pm * pp + (1 - pm) * pm
    return k2pp, k2pm, k2pp - k2pm


def six_K(a, b, c):
    # rows/cols 0..5, antipode i^1, orthogonal else
    K = [[None] * 6 for _ in range(6)]
    for s in range(6):
        for t in range(6):
            if s == t:
                K[s][t] = a
            elif s == (t ^ 1):
                K[s][t] = b
            else:
                K[s][t] = c
    return K


def matmul(A, B):
    n = len(A)
    C = [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    return C


def main():
    grid = [F(0), F(1, 5), F(1, 2), F(4, 5), F(1)]
    for pp, pm in product(grid, repeat=2):
        k2pp, k2pm, diff = k2_plus(pp, pm)
        want = (pp - pm) ** 2
        if diff != want:
            HITS.append(f"two-state ({pp},{pm}): {diff} != {want}")
        print(f"two-state p+={pp} p-={pm}: K2diff={diff} (p+-p-)^2={want}")

    # Theorem 1 executed numbers: (4/5,1/5) K^2(+|+)=17/25, P(L=R=+)=17/50
    k2pp, _, _ = k2_plus(F(4, 5), F(1, 5))
    print(f"Ising (4/5,1/5) K2(+|+)= {k2pp} stated 17/25")
    if k2pp != F(17, 25):
        HITS.append(f"K2(+|+)+={k2pp} != 17/25")
    p_eq = F(1, 2) * k2pp
    print(f"P(L=R=+)={p_eq} stated 17/50")
    if p_eq != F(17, 50):
        HITS.append(f"P(L=R=+)={p_eq} != 17/50")

    # six-axis (a-b)^2
    for a, b, c in (
        (F(1, 6), F(1, 6), F(1, 6)),
        (F(1, 2), F(0), F(1, 8)),
        (F(3, 1), F(1, 1), F(2, 1)),  # unnormalized skip
    ):
        if a + b + 4 * c != 1:
            continue
        K = six_K(a, b, c)
        K2 = matmul(K, K)
        same = K2[0][0]
        opp = K2[0][1]
        print(f"six-axis a={a} b={b} c={c}: K2same-K2opp={same-opp} (a-b)^2={(a-b)**2}")
        if same - opp != (a - b) ** 2:
            HITS.append(f"six-axis (a-b)^2 fails at a={a} b={b}")

    # substitution identity: a=1/2-2c, 2a^2+4c^2-1/6 == (6c-1)^2 / 3 ? note says
    # 2a^2+4c^2=1/6 yields (6c-1)^2/3=0
    c = F(1, 12)
    a = F(1, 2) - 2 * c
    lhs = 2 * a * a + 4 * c * c - F(1, 6)
    rhs = (6 * c - 1) ** 2 / 3
    print(f"quadratic remainder at c=1/12: lhs={lhs} rhs={rhs}")
    # they should be equal as polynomials (both zero only at c=1/6)
    # check polynomial identity 2(1/2-2c)^2+4c^2-1/6 = (6c-1)^2/3
    from sympy import symbols, simplify, Rational
    cc = symbols("c")
    aa = Rational(1, 2) - 2 * cc
    ident = simplify(2 * aa**2 + 4 * cc**2 - Rational(1, 6) - (6 * cc - 1) ** 2 / 3)
    print(f"poly identity remainder {ident}")
    if ident != 0:
        HITS.append(f"Thm3 substitution poly {ident} != 0")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print(
            "SUMMARY: attack pattern (g) PROOF STEP BY BRUTE FORCE on Haar-square "
            "identities - " + "; ".join(HITS)
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - two-state K^2 difference "
        "is (pplus-pminus)^2 on a 5x5 grid, Ising 17/25 and 17/50 hold, six-axis "
        "same-minus-opposite is (a-b)^2, and (6c-1)^2/3 is the Haar-square remainder"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
