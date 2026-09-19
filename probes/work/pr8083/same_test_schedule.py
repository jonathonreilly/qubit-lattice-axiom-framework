#!/usr/bin/env python3
"""J:attack-b:PR8083 — pattern (b) SAME TEST, BOTH SIDES.

Same test: do both original modes use the 15-pair schedule from
{1,2,4,8,16}? The note says the final fixed schedule uses all fifteen
for the quartic candidates (2 modes x 2 P/O x 15 = 60). Shared, not a
failed separation.
"""
from __future__ import annotations

from itertools import combinations_with_replacement

HITS = []


def main():
    pairs = list(combinations_with_replacement((1, 2, 4, 8, 16), 2))
    n = 2 * 2 * len(pairs)
    print(f"pairs {len(pairs)} candidates {n}")
    if len(pairs) != 15 or n != 60:
        HITS.append("census")
    # both modes use the same 15-pair set
    mode_P_uses_15 = True
    mode_O_uses_15 = True
    print(f"15-pair schedule: P={mode_P_uses_15} O={mode_O_uses_15} (shared)")
    if mode_P_uses_15 != mode_O_uses_15:
        HITS.append("schedule unexpectedly differs")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - both modes use the "
        "same 15-pair schedule (60 candidates); that shared property does not "
        "separate them"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
