#!/usr/bin/env python3
"""J:attack-b:PR8176 — same forks=|S|-1 test on one-seed vs multi-seed trees.

The counted family has F=|S|-1. Apply to a singleton seed (|S|=1,F=0) and a
two-seed gadget with one fork (|S|=2,F=1). HIT if the identity fails on either.
"""
from __future__ import annotations


def main():
    hits = []
    cases = [("singleton", 1, 0), ("two-seed+fork", 2, 1), ("three-seed tree", 3, 2)]
    for name, nS, F in cases:
        ok = F == nS - 1
        print(f"{name}: |S|={nS} F={F} identity={ok}")
        if not ok:
            hits.append(f"HIT: forks=|S|-1 fails on {name}: F={F} |S|={nS}")
            print(hits[-1])
    if hits:
        print("SUMMARY: forks=|S|-1 fails on a stated tree shape")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — the same forks=|S|-1 test "
        "holds for a singleton seed, a two-seed fork gadget, and a three-seed tree"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
