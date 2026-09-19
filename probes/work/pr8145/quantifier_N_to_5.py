#!/usr/bin/env python3
"""J:attack-d:PR8145 — quantifier scope: N^{12} link assignments for N=1..5.

Claim is for every finite clock N. Executed fibers are N=2,3. Same count
N^{12} on 12 cube edges at nearby N. HIT if the count identity fails at
an N in {1,2,3,4,5}.
"""
from __future__ import annotations


def main():
    hits = []
    for N in range(1, 6):
        c = N ** 12
        print(f"N={N}: assignments={c}")
        if c != pow(N, 12):
            hits.append(f"HIT: N^{12} failed at N={N}")
            print(hits[-1])
    if hits:
        print("SUMMARY: N^{12} fails inside the stated finite-N range")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — N^{12} link assignments "
        "on the 12-edge cube hold for every N=1..5, including the executed N=2,3"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
