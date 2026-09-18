#!/usr/bin/env python3
"""J:attack:PR8147 — pattern (c) EXECUTED NUMBERS: T3 SRW return = C(2n,n)/4^n * P_n.

P_n is the coincidence probability of two independent 3-direction directed
walks after n steps. Simple random walk on Z^3 has 6 neighbors. HIT if
u_{2n} != binom(2n,n)/4^n * P_n for n=1..8.
"""
from fractions import Fraction
from math import comb


def P_n(n: int) -> Fraction:
    # sum_{a+b+c=n} [n!/(a!b!c! 3^n)]^2
    s = Fraction(0)
    for a in range(n + 1):
        for b in range(n - a + 1):
            c = n - a - b
            s += Fraction(comb(n, a) * comb(n - a, b)) ** 2
    return s / Fraction(3 ** (2 * n))


def srw_return_2n(n: int) -> Fraction:
    """P(S_{2n}=0) for SRW on Z^3, 6 neighbors.

    Need n_++ = n_+- for each axis... equivalently 2n steps of ±e_i with
    net zero. Number of steps on axis i is 2 k_i with k1+k2+k3=n, and on
    each axis k_i + and k_i -.
    """
    s = Fraction(0)
    for k1 in range(n + 1):
        for k2 in range(n - k1 + 1):
            k3 = n - k1 - k2
            # multinomial(2n; k1,k1,k2,k2,k3,k3) / 6^{2n}
            ways = comb(2 * n, k1) * comb(2 * n - k1, k1)
            rest = 2 * n - 2 * k1
            ways *= comb(rest, k2) * comb(rest - k2, k2)
            rest2 = rest - 2 * k2
            ways *= comb(rest2, k3) * comb(rest2 - k3, k3)
            s += Fraction(ways, 6 ** (2 * n))
    return s


def main() -> None:
    hits = []
    for n in range(1, 9):
        pn = P_n(n)
        rhs = Fraction(comb(2 * n, n), 4**n) * pn
        lhs = srw_return_2n(n)
        print(f"n={n} P_n={pn} C(2n,n)/4^n * P_n={rhs} SRW u_{{2n}}={lhs} eq={lhs==rhs}")
        if lhs != rhs:
            hits.append(f"n={n}: {lhs} != {rhs}")
    if hits:
        print("HIT: " + "; ".join(hits))
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS on T3 SRW identity - " + "; ".join(hits))
    else:
        print(
            "SUMMARY: attack pattern (c) EXECUTED NUMBERS on T3 SRW identity - "
            "u_{2n} = C(2n,n)/4^n P_n for n=1..8; does not fire"
        )


if __name__ == "__main__":
    main()
