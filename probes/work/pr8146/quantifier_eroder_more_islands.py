#!/usr/bin/env python3
"""J:attack-d:PR8146 — S2 eroder bound on extra islands; not the known S1 iff HIT.

S2: every finite island dies within M1+M2+M3-t0+1 levels. Executed on 300
random islands. Quantifier: check further islands including a 3x3 square
slice and a 2x2x2 cube slice. HIT if any island still has a 1 after the bound.
"""
from __future__ import annotations


def preds(x, y, z):
    out = []
    if x:
        out.append((x - 1, y, z))
    if y:
        out.append((x, y - 1, z))
    if z:
        out.append((x, y, z - 1))
    return out


def evolve(island, steps):
    live = set(island)
    counts = [len(live)]
    for _ in range(steps):
        cand = set()
        for x, y, z in live:
            cand.add((x + 1, y, z))
            cand.add((x, y + 1, z))
            cand.add((x, y, z + 1))
        nxt = set()
        for p in cand:
            vals = [1 if q in live else 0 for q in preds(*p)]
            while len(vals) < 3:
                vals.append(0)
            if sum(vals) >= 2:
                nxt.add(p)
        live = nxt
        counts.append(len(live))
    return counts


def main():
    hits = []
    cases = [
        {(0, 0, 0)},
        {(i, 0, 0) for i in range(6)},
        {(x, y, 0) for x in range(3) for y in range(3)},
        {(x, y, z) for x in range(2) for y in range(2) for z in range(2)},
        {(x, 5 - x, 0) for x in range(6)},
        {(x, y, 4 - x - y) for x in range(5) for y in range(5 - x)},
    ]
    for island in cases:
        t0 = min(sum(p) for p in island)
        xs, ys, zs = zip(*island)
        bound = max(xs) + max(ys) + max(zs) - t0 + 1
        counts = evolve(island, bound + 2)
        dead = next((i for i, n in enumerate(counts) if n == 0), None)
        print(f"|I|={len(island)} t0={t0} M=({max(xs)},{max(ys)},{max(zs)}) bound={bound} dead_at={dead} counts={counts}")
        if dead is None or dead > bound:
            hits.append(
                f"HIT: island |I|={len(island)} still live after bound {bound}: {counts}"
            )
            print(hits[-1])
    if hits:
        print("SUMMARY: S2 eroder bound fails on an extra island inside the stated quantifier")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note beyond the known S1 iff HIT "
        "— S2's M1+M2+M3-t0+1 bound holds on six extra islands (origin, line, "
        "3x3 square, 2-cube, 6-site level line, 15-site simplex)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
