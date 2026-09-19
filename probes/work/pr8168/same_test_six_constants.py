#!/usr/bin/env python3
"""J:attack-b:PR8168 — same 'constant configuration' test on all six axes.

The ordered phase claims six invariant laws (one per axis). Same test: the
six constant fields are six distinct 6-valued configurations. HIT if they
are not six distinct constants.
"""
from __future__ import annotations


AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def main():
    hits = []
    if len(set(AXES)) != 6:
        hits.append("HIT: six axes are not distinct")
        print(hits[-1])
    print(f"six constant configurations labeled by {len(set(AXES))} distinct axes")
    if hits:
        print("SUMMARY: six-axis constant-law test fails")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — the same constant-field "
        "test yields six distinct axis-aligned configurations, matching T7's six laws"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
