#!/usr/bin/env python3
"""J:attack:PR8146 — pattern (a) S2 eroder bound on finite islands.

S2: deterministic majority of the three level-predecessors is an eroder:
every finite island dies within M1+M2+M3-t0+1 levels. Simulated exactly
on nonnegative orthant sites (missing predecessor = 0). HIT if an island
still has a 1 after that many levels.
"""
from __future__ import annotations

from itertools import combinations_with_replacement


def preds(x, y, z):
    out = []
    if x:
        out.append((x - 1, y, z))
    if y:
        out.append((x, y - 1, z))
    if z:
        out.append((x, y, z - 1))
    return out


def majority(vals):
    return 1 if sum(vals) >= 2 else 0


def evolve(island: set[tuple[int, int, int]], t0: int, steps: int) -> list[int]:
    """island sites all at level t0. Return occupancy counts for t0..t0+steps."""
    live = {p for p in island}
    counts = [len(live)]
    t = t0
    for _ in range(steps):
        t += 1
        nxt = set()
        # candidates: one step forward from each live site
        cand = set()
        for x, y, z in live:
            cand.add((x + 1, y, z))
            cand.add((x, y + 1, z))
            cand.add((x, y, z + 1))
        for p in cand:
            vals = [1 if q in live else 0 for q in preds(*p)]
            while len(vals) < 3:
                vals.append(0)
            if majority(vals):
                nxt.add(p)
        live = nxt
        counts.append(len(live))
    return counts


def maxima(island, t0):
    xs, ys, zs = zip(*island) if island else ((0,), (0,), (0,))
    return max(xs), max(ys), max(zs)


def main() -> None:
    hits = []
    cases = []
    # t0=0 origin
    cases.append({(0, 0, 0)})
    # a 2D triangle at t0=3: all x+y=3, z=0
    cases.append({(x, 3 - x, 0) for x in range(4)})
    # a filled simplex slice t0=4
    cases.append({(x, y, 4 - x - y) for x in range(5) for y in range(5 - x)})
    # a line along e1 at t0=5: (5,0,0) only
    cases.append({(5, 0, 0)})
    # a 2x2 block lifted to a level: (2,0,0),(1,1,0),(1,0,1),(0,1,1) sum=2
    cases.append({(2, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1), (0, 2, 0), (0, 0, 2)})

    for island in cases:
        t0 = sum(next(iter(island)))
        assert all(sum(p) == t0 for p in island)
        M = maxima(island, t0)
        bound = M[0] + M[1] + M[2] - t0 + 1
        counts = evolve(island, t0, bound + 2)
        dead_at = next((i for i, n in enumerate(counts) if n == 0), None)
        print(f"t0={t0} |I|={len(island)} M={M} bound={bound} counts={counts} dead_at={dead_at}")
        if dead_at is None or dead_at > bound:
            hits.append(f"island {island} survived past bound {bound}: {counts}")

    # S1: majority most likely iff p > max(q,r) on a unanimous triple of +x
    # Z_3(+x,+x,+x) = p^3+q^3+4r^3; weight of +x is p^3 relative... skip if no closed form needed
    if hits:
        print("HIT: " + "; ".join(hits))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY on S2 eroder - " + "; ".join(hits))
    else:
        print(
            "SUMMARY: attack pattern (a) WITNESS REALIZABILITY on S2 eroder - "
            "all tested islands died within M1+M2+M3-t0+1 levels; does not fire"
        )


if __name__ == "__main__":
    main()
