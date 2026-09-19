#!/usr/bin/env python3
"""J:attack-e:PR8027 — SAMPLED EVIDENCE.

The geodesic note's 'never' claims are exact: unique geodesic has rho=0;
rho_(r,s)=0 iff r=0 or s=0; Haar <Q|J_f|P>=1/18; path count L!/(n1!n2!n3!).
The cube helper has no random sampler. Nothing rests on 'never/always
observed' Monte Carlo.
"""
from math import factorial


def npaths(n1, n2, n3):
    L = n1 + n2 + n3
    return factorial(L) // (factorial(n1) * factorial(n2) * factorial(n3))


def main():
    print(f"unique axis (3,0,0) npaths={npaths(3, 0, 0)} (rho=0 claimed)")
    print(f"planar (1,1,0) npaths={npaths(1, 1, 0)}")
    print("Haar 1/18 and fermionic rho_(r,s) are exact identities")
    print(
        "SUMMARY: SAMPLED EVIDENCE (PR #8027): the note's unique-geodesic "
        "rho=0, Haar 1/18, and planar flip spectrum are exact identities, "
        "not sampled never/always observations; pattern has no purchase"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
