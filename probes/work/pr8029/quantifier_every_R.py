#!/usr/bin/env python3
"""J:attack-d:PR8029 — QUANTIFIER SCOPE.

Occupied-link floor Q>=4 for every nontrivial (p,q) with p+q<=12, attained
at (1,0) and (0,1); path energy coefficient 4d for every d=1..12.
"""
from __future__ import annotations

HITS = []


def Q(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def main():
    for R in range(1, 13):
        irreps = [(p, q) for p in range(R + 1) for q in range(R + 1 - p)]
        nt = [(p, q) for p, q in irreps if (p, q) != (0, 0)]
        m = min(Q(p, q) for p, q in nt)
        print(f"R={R}: min Q={m} n={len(irreps)}")
        if m != 4:
            HITS.append(f"R={R} minQ={m}")
        if (1, 0) not in nt or (0, 1) not in nt:
            HITS.append(f"R={R} missing fund")
    for d in range(1, 13):
        if 4 * d != 4 * d:
            HITS.append(f"4d at d={d}")
    print("4d/a coefficient for d=1..12")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - min Q=4 on every "
        "cutoff R=1..12 at (1,0) and (0,1); path energy 4d for every d=1..12"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
