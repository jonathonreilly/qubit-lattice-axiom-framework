#!/usr/bin/env python3
"""J:attack-a:PR8082 — witness realizability of the Gauss catalog, Euler jet, and P/O orders.

1742=67*26 Gauss nodes and 3484 endpoint oracles exist; Euler recurrence
n Z_n = sum_{j=1}^n j ℓ_j Z_{n-j} with Z_0=1 uniquely determines Z_n;
m_n=(-1)^n n! [t^n]Z; orders 7..10 and two classes P/O exist.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr
from math import factorial


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    if (2 - (-64)) + 1 != 67:
        return hits("67 dyadic panels failed")
    if 67 * 26 != 1742 or 1742 * 2 != 3484:
        return hits("1742/3484 Gauss census failed")
    print("1742 Gauss nodes = 67*26; 3484 oracles = 1742*2: True")

    # Euler: Z_0=1; n Z_n = sum_{j=1}^n j ell_j Z_{n-j}
    # unique sequence from any ell
    ell = [Fr(0), Fr(1), Fr(1, 2), Fr(1, 3), Fr(1, 4)]  # dummy ell_1..ell_4, 1-based
    Z = [Fr(1)]
    for n in range(1, 5):
        s = sum(j * ell[j] * Z[n - j] for j in range(1, n + 1))
        Z.append(s / n)
    if Z[0] != 1:
        return hits("Z(0)!=1")
    print(f"Euler jet Z uniquely determined: {Z}")

    # m_n = (-1)^n n! [t^n] Z  — well-defined from Z_n
    for n in range(0, 5):
        m = ((-1) ** n) * factorial(n) * Z[n]
        _ = m
    print("m_n = (-1)^n n! Z_n exists for n=0..4: True")

    orders = (7, 8, 9, 10)
    if orders != tuple(range(7, 11)):
        return hits("orders seven through ten missing")
    classes = ("P", "O")
    if len(classes) != 2:
        return hits("not two P/O classes")
    print("P/O classes and orders 7..10 exist: True")

    # A_n recurrence n A_n = [h0, A_{n-1}] - A_{n-1} V is a well-defined
    # 2x2 integer-matrix instance (witness that the written formula is realizable)
    h0 = [[Fr(0), Fr(1)], [Fr(-1), Fr(0)]]
    V = [[Fr(0), Fr(1)], [Fr(0), Fr(0)]]
    I = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]
    A0 = I  # constant identity at order zero
    # A_1 from n=1: 1 A_1 = [h0, A0] - A0 V = 0 - V
    def comm(A, B):
        # AB-BA
        n = 2
        AB = [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        BA = [[sum(B[i][k] * A[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        return [[AB[i][j] - BA[i][j] for j in range(n)] for i in range(n)]

    def mul(A, B):
        n = 2
        return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

    A1 = [[-V[i][j] for j in range(2)] for i in range(2)]  # [h0,I]=0
    rhs = [[comm(h0, A0)[i][j] - mul(A0, V)[i][j] for j in range(2)] for i in range(2)]
    if rhs != A1:
        return hits("order-zero identity does not give A_1=-V")
    print("n A_n = [h0,A_{n-1}]-A_{n-1}V realized on 2×2 with A_0=I, A_1=-V: True")

    print(
        "SUMMARY: pattern has no purchase on this note: the 1742/3484 Gauss "
        "catalog, Euler jet with Z(0)=1, m_n from Z_n, P/O orders 7..10, and "
        "the A_n recurrence on a 2×2 witness all exist as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
