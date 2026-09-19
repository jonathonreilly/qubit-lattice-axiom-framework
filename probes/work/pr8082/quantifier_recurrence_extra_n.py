#!/usr/bin/env python3
"""J:attack-d:PR8082 — QUANTIFIER SCOPE.

n A_n = [h0, A_{n-1}] - A_{n-1} V for every n>=1 (attack-g checked n<=8 on
one 2x2 pair). Extra n through 14 and a second 3x3 integer pair. HIT if the
recurrence disagrees with the truncated exponential series of U-I.
"""
from fractions import Fraction
from math import factorial

HITS = []


def mul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


def smul(s, A):
    return [[s * A[i][j] for j in range(len(A))] for i in range(len(A))]


def comm(A, B):
    return sub(mul(A, B), mul(B, A))


def eye(n):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def _pow(M, n):
    acc = eye(len(M))
    for _ in range(n):
        acc = mul(acc, M)
    return acc


def poly_mul(P, Q, order):
    out = [smul(0, P[0]) for _ in range(order + 1)]
    for i, A in enumerate(P):
        for j, B in enumerate(Q):
            if i + j <= order:
                out[i + j] = add(out[i + j], mul(A, B))
    return out


def check_pair(name, h0, V, N):
    eh = [smul(Fraction(1, factorial(n)), _pow(h0, n)) for n in range(N + 1)]
    hmV = add(h0, V)
    em = [smul(Fraction((-1) ** n, factorial(n)), _pow(hmV, n)) for n in range(N + 1)]
    U = poly_mul(eh, em, N)
    rec = [eye(len(h0))]
    for n in range(1, N + 1):
        rhs = sub(comm(h0, rec[n - 1]), mul(rec[n - 1], V))
        rec.append(smul(Fraction(1, n), rhs))
    bad = [n for n in range(N + 1) if rec[n] != U[n]]
    print(f"{name} N={N}: recurrence vs U fails at {bad[:8]} count={len(bad)}")
    return bad


def main():
    h0 = [[Fraction(0), Fraction(1)], [Fraction(-1), Fraction(0)]]
    V = [[Fraction(0), Fraction(2)], [Fraction(0), Fraction(0)]]
    bad = check_pair("2x2", h0, V, 14)
    if bad:
        HITS.append(f"2x2 extra n {bad}")
    h03 = [
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
        [Fraction(-1), Fraction(0), Fraction(0)],
    ]
    V3 = [
        [Fraction(0), Fraction(0), Fraction(1)],
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0)],
    ]
    bad3 = check_pair("3x3", h03, V3, 10)
    if bad3:
        HITS.append(f"3x3 extra n {bad3}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - n A_n=[h0,A_{n-1}]-"
        "A_{n-1}V matches the truncated series of U through n=14 on the 2x2 "
        "pair and n=10 on a 3x3 pair"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
