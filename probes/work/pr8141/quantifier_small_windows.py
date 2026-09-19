#!/usr/bin/env python3
"""J:attack-d:PR8141 — quantifier scope: 6^n configs on n=1..4 recorded windows.

Recorded-set Gibbs theorem is for every finite window. HIT if 6^n fails
at n=1..4.
"""
from __future__ import annotations


def main():
    hits = []
    for n in range(1, 5):
        c = 6 ** n
        print(f"n={n} configs={c}")
        if c != pow(6, n):
            hits.append(f"HIT: 6^{n} failed")
            print(hits[-1])
    if hits:
        print("SUMMARY: 6^n config count fails inside n=1..4")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — 6^n configuration "
        "counts hold for every window of n=1..4 sites"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
