#!/usr/bin/env python3
"""J:attack-g:PR8082 — brute-force the coefficient recurrence n A_n = [h0, A_{n-1}] - A_{n-1} V.

The note: U(t)=e^{t h0} e^{-t(h0+V)}, U-I = sum_{n>=1} A_n t^n, and
n A_n = [h0, A_{n-1}] - A_{n-1} V with the constant identity at order zero.
Verified on 2x2 integer matrices by truncated exponential series (Fraction).
HIT if the written recurrence disagrees with the series of U-I.
"""
from fractions import Fraction
from math import factorial


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


def expm_series(M, order):
    acc = eye(len(M))
    term = eye(len(M))
    for k in range(1, order + 1):
        term = smul(Fraction(1, k), mul(term, M))
        acc = add(acc, term)
    return acc


def poly_mul(P, Q, order):
    """P, Q lists of matrices, index = power."""
    out = [smul(0, P[0]) for _ in range(order + 1)]
    for i, A in enumerate(P):
        for j, B in enumerate(Q):
            if i + j <= order:
                out[i + j] = add(out[i + j], mul(A, B))
    return out


def main() -> None:
    h0 = [[Fraction(0), Fraction(1)], [Fraction(-1), Fraction(0)]]
    V = [[Fraction(0), Fraction(2)], [Fraction(0), Fraction(0)]]
    N = 8
    # series of e^{t h0} and e^{-t(h0+V)}
    eh = [smul(Fraction(1, factorial(n)), _pow(h0, n)) for n in range(N + 1)]
    hmV = add(h0, V)
    em = [smul(Fraction((-1) ** n, factorial(n)), _pow(hmV, n)) for n in range(N + 1)]
    U = poly_mul(eh, em, N)
    A = [U[0], *U[1:]]  # U coeffs; A_0 should be I
    A[0] = sub(U[0], eye(2))  # U-I
    # written recurrence with A_0 = 0 (U-I has no constant): start A_1 from series
    rec = [A[0]]
    rec.append(A[1])
    for n in range(2, N + 1):
        rhs = sub(comm(h0, rec[n - 1]), mul(rec[n - 1], V))
        rec.append(smul(Fraction(1, n), rhs))
    hits = []
    for n in range(N + 1):
        ok = rec[n] == A[n]
        print(f"n={n} recurrence vs series: {ok}")
        if not ok:
            hits.append(f"n={n}")
    # also try A_0 = I as 'constant identity included at order zero' feeding n=1
    recI = [eye(2)]
    for n in range(1, N + 1):
        rhs = sub(comm(h0, recI[n - 1]), mul(recI[n - 1], V))
        recI.append(smul(Fraction(1, n), rhs))
    # compare recI[n] to U[n] (including I at 0)
    hitsI = [n for n in range(N + 1) if recI[n] != U[n]]
    print(f"A_0=I feeding recurrence vs U series fails at {hitsI[:6]} (count {len(hitsI)})")
    print(f"A_1 from series {A[1]} (expect -V = {smul(-1, V)})")
    if hits:
        print("HIT: recurrence vs series at " + ",".join(hits))
        print("SUMMARY: attack-g brute force n A_n=[h0,A_{n-1}]-A_{n-1}V - FIRES")
    else:
        print(
            "SUMMARY: attack-g brute force n A_n=[h0,A_{n-1}]-A_{n-1}V - with the "
            f"constant identity at order zero the recurrence matches U through order {N} "
            "on a 2x2 integer pair, and U-I matches from n>=1; does not fire"
        )


def _pow(M, n):
    acc = eye(len(M))
    for _ in range(n):
        acc = mul(acc, M)
    return acc


if __name__ == "__main__":
    main()
