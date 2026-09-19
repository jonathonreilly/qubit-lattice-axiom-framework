#!/usr/bin/env python3
"""J:attack:PR8027 — pattern (c) EXECUTED NUMBERS.

rho_(1,1)=1, rho_(2,1)=√2, rho_(2,2)=√5; path count L!/(n1!n2!n3!).
"""
from math import factorial

import sympy as sp

HITS = []


def npaths(n1, n2, n3):
    L = n1 + n2 + n3
    return factorial(L) // (factorial(n1) * factorial(n2) * factorial(n3))


def rho_rs(r, s):
    L = r + s
    return sp.simplify(2 * sum(sp.cos(sp.pi * k / (L + 1)) for k in range(1, s + 1)))


def main():
    if npaths(1, 1, 0) != 2:
        HITS.append("npaths(1,1,0)")
    if npaths(2, 1, 0) != 3:
        HITS.append("npaths(2,1,0)")
    if npaths(2, 2, 0) != 6:
        HITS.append("npaths(2,2,0)")
    print(f"npaths (1,1,0)={npaths(1,1,0)} (2,1,0)={npaths(2,1,0)} (2,2,0)={npaths(2,2,0)}")
    r11, r21, r22 = rho_rs(1, 1), rho_rs(2, 1), rho_rs(2, 2)
    print(f"rho(1,1)={r11} rho(2,1)={r21} rho(2,2)={r22}")
    if sp.simplify(r11 - 1) != 0:
        HITS.append(f"rho11={r11}")
    if sp.simplify(r21 - sp.sqrt(2)) != 0:
        HITS.append(f"rho21={r21}")
    if sp.simplify(r22 - sp.sqrt(5)) != 0:
        HITS.append(f"rho22={r22}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: attack pattern (c) EXECUTED NUMBERS - rho_(1,1)=1, "
        "rho_(2,1)=√2, rho_(2,2)=√5 and path counts 2,3,6 hold; pattern has no purchase"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
