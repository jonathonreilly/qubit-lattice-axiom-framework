#!/usr/bin/env python3
"""J:attack-b:PR8033 — pattern (b) SAME TEST, BOTH SIDES.

Same test: is the Casimir zero? Vacuum (0,0) yes; fundamental (1,0) Q=4 no.
They separate the free charged floor from the neutral ground.
"""
from __future__ import annotations

HITS = []


def Q(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def main():
    vac = Q(0, 0) == 0
    fund = Q(1, 0) == 0
    print(f"Casimir-zero test: vacuum={vac} fundamental={fund} Q(1,0)={Q(1,0)}")
    if vac == fund:
        HITS.append("does not separate")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the same Casimir-zero "
        "test holds for the vacuum and fails for the fundamental (Q=4)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
