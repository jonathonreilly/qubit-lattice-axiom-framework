#!/usr/bin/env python3
"""J:attack-b:PR8142 — pattern (b) SAME TEST, BOTH SIDES.

Same test: are the three orbit weights equal? Constant rule (2,2,2) yes;
(3,1,2) no. They separate the exceptional constant locus from a generic
product rule.
"""
from __future__ import annotations

HITS = []


def main():
    eq_222 = (2, 2, 2) == (2, 2, 2)
    eq_312 = (3, 1, 2)[0] == (3, 1, 2)[1] == (3, 1, 2)[2]
    print(f"equal-weights test: (2,2,2)={eq_222} (3,1,2)={eq_312}")
    if eq_222 == eq_312:
        HITS.append("does not separate")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the same equal-weight "
        "test holds at (2,2,2) and fails at (3,1,2)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
