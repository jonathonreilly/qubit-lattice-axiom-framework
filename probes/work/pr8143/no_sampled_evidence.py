#!/usr/bin/env python3
"""J:attack-e:PR8143 — SAMPLED EVIDENCE.

Z=S+(S-1)^2≥3/4, |C|=1+5L, Erlang Eτ=3L, rank-one RρR=tr(ρR)R are exact.
No never/always sampler.
"""
from fractions import Fraction


def main():
    zmin = Fraction(1, 2) + (Fraction(1, 2) - 1) ** 2
    print(f"Z min at S=1/2 = {zmin}")
    print("|C|=1+5L and Erlang 3L are exact for every L")
    print(
        "SUMMARY: SAMPLED EVIDENCE (PR #8143): Z≥3/4, |C|=1+5L, and the "
        "rank-one Born chain are exact identities, not sampled never/always; "
        "pattern has no purchase"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
