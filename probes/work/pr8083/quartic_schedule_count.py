#!/usr/bin/env python3
"""J:attack-g:PR8083 — pattern (g) PROOF STEP BY BRUTE FORCE.

The quartic Ward note: fifteen unordered pairs with repetition from
{1,2,4,8,16}; two modes and two P/O classes hence sixty candidates.

HIT if the combination-with-repetition count is not 15 or 2*2*15 != 60.
"""
from __future__ import annotations

from itertools import combinations_with_replacement

HITS = []


def main():
    S = (1, 2, 4, 8, 16)
    pairs = list(combinations_with_replacement(S, 2))
    print(f"unordered pairs with replacement from {S}: {len(pairs)} {pairs}")
    if len(pairs) != 15:
        HITS.append(f"{len(pairs)} pairs != 15")
    n = 2 * 2 * len(pairs)
    print(f"2 modes * 2 P/O * {len(pairs)} = {n} (stated 60)")
    if n != 60:
        HITS.append(f"candidates {n} != 60")
    # C(5+2-1, 2) = 15
    from math import comb
    if comb(5 + 2 - 1, 2) != 15:
        HITS.append("C(6,2)!=15")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print(
            "SUMMARY: attack pattern (g) PROOF STEP BY BRUTE FORCE on the 15-pair/"
            "60-candidate census - " + "; ".join(HITS)
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - combinations with "
        "repetition of {1,2,4,8,16} number 15, and 2*2*15=60 quartic candidates"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
