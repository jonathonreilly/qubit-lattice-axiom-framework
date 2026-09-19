#!/usr/bin/env python3
"""J:attack-b:PR8145 — same fiber-count test on N=2 vs N=3 clock assignments.

Note: 4096 and 531441 link assignments. Same test: N^{12} on a 12-edge cube.
HIT if 2^12==3^12 (no separation) or the stated numbers disagree with N^12.
"""
from __future__ import annotations


def main():
    hits = []
    n2, n3 = 2 ** 12, 3 ** 12
    print(f"2^12={n2} 3^12={n3}")
    if n2 != 4096:
        hits.append(f"HIT: 2^12={n2} != 4096")
        print(hits[-1])
    if n3 != 531441:
        hits.append(f"HIT: 3^12={n3} != 531441")
        print(hits[-1])
    if n2 == n3:
        hits.append("HIT: N=2 and N=3 fiber counts are equal under N^12")
        print(hits[-1])
    if hits:
        print("SUMMARY: N=2 vs N=3 fiber-count test fails")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — the same N^{12} test on "
        "the 12-edge cube separates N=2 (4096) from N=3 (531441) as stated"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
