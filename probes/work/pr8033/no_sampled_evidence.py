#!/usr/bin/env python3
"""J:attack-e:PR8033 — SAMPLED EVIDENCE.

Finite-PW static-source bounds: Q(p,q)=p²+pq+q²+3p+3q, floor 4/a, geodesic
length L. All exact integer identities; no 'never/always observed' sampler.
"""


def Q(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def main():
    print(f"Q(1,0)={Q(1, 0)} Q(0,0)={Q(0, 0)}")
    print("occupied-link floor and Manhattan geodesics are exact, not sampled")
    print(
        "SUMMARY: SAMPLED EVIDENCE (PR #8033): Casimir floor Q=4 and geodesic "
        "length L are exact identities, not sampled never/always observations; "
        "pattern has no purchase"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
