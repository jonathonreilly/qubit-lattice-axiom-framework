#!/usr/bin/env python3
"""J:attack-d:PR8176 — QUANTIFIER SCOPE.

Not the known provenance HIT (4165 unsourced).

T4: max_{t} t(4/27-t)=4/729 at t=2/27, so the quadratic is <= 4/729 for
every t. Extra t in [0, 4/27] and beyond the vertex. HIT if some t in the
stated range exceeds 4/729.
"""
from __future__ import annotations

from fractions import Fraction as F

HITS: list[str] = []
CAP = F(4, 729)
VERTEX = F(2, 27)


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def f(t: F) -> F:
    return t * (F(4, 27) - t)


def main() -> int:
    print(f"vertex t={VERTEX} f={f(VERTEX)} stated 4/729={CAP} eq={f(VERTEX)==CAP}")
    if f(VERTEX) != CAP:
        hit(f"vertex {f(VERTEX)} != 4/729")
    grid = (
        [F(0), F(1, 27), VERTEX, F(3, 27), F(4, 27)]
        + [F(k, 270) for k in range(0, 41)]
        + [F(1, 1000), F(1, 100), F(1, 10)]
    )
    for t in grid:
        v = f(t)
        inside = F(0) <= t <= F(4, 27)
        print(f"t={t} f={v} <=4/729 {v <= CAP} inside={inside}")
        if inside and v > CAP:
            hit(f"t={t} f={v} > 4/729")
        if t == VERTEX and v != CAP:
            hit("vertex not unique max")
    # extra p=367,368 from the note: d3 vs 4/729 already in attack-c; skip

    if HITS:
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - t(4/27-t)<=4/729 for "
        "every tested t in [0,4/27] with equality only at t=2/27; not the "
        "known 4165 provenance HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
