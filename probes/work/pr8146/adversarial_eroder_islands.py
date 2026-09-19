#!/usr/bin/env python3
"""J:attack-e:PR8146 — pattern (e) SAMPLED EVIDENCE.

Not the known S1 iff HIT at (5,2,4).

S2: every finite island dies within M1+M2+M3-t0+1 levels (executed on 300
random islands). Adversarial constructions instead of more samples: a long
line, a filled triangle, a 3-cube, a diagonal rod, and a greedy add-a-site
hill-climb maximizing lifetime. HIT if any island is still live after the
stated bound.
"""
from __future__ import annotations

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


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


def bound_of(island):
    t0 = min(sum(p) for p in island)
    xs, ys, zs = zip(*island)
    return max(xs) + max(ys) + max(zs) - t0 + 1


def check(name, island):
    island = set(island)
    b = bound_of(island)
    counts = evolve(island, b + 3)
    dead = next((i for i, n in enumerate(counts) if n == 0), None)
    print(f"{name}: |I|={len(island)} bound={b} dead_at={dead} counts={counts[: b + 2]}")
    if dead is None or dead > b:
        hit(f"{name} still live after bound {b} (dead_at={dead})")
    return dead, b


def main() -> int:
    cases = [
        ("origin", {(0, 0, 0)}),
        ("line12", {(i, 0, 0) for i in range(12)}),
        ("triangle21", {(x, y, 0) for x in range(6) for y in range(6 - x)}),
        ("cube3", {(x, y, z) for x in range(3) for y in range(3) for z in range(3)}),
        ("diag_rod", {(i, i, 0) for i in range(8)}),
        ("L_shape", {(i, 0, 0) for i in range(8)} | {(0, j, 0) for j in range(8)}),
    ]
    for name, island in cases:
        check(name, island)

    # greedy hill-climb: add a site that maximizes (dead_at - bound)
    live = {(0, 0, 0), (1, 0, 0), (0, 1, 0)}
    best_gap = -10
    for _ in range(12):
        cand_sites = set()
        xs, ys, zs = zip(*live)
        for x in range(min(xs), max(xs) + 2):
            for y in range(min(ys), max(ys) + 2):
                for z in range(0, max(zs) + 2):
                    p = (x, y, z)
                    if p not in live:
                        cand_sites.add(p)
        picked = None
        for p in list(cand_sites)[:40]:
            trial = live | {p}
            b = bound_of(trial)
            counts = evolve(trial, b + 2)
            dead = next((i for i, n in enumerate(counts) if n == 0), b + 2)
            gap = dead - b
            if gap > best_gap:
                best_gap, picked, live = gap, p, trial
        if picked is None:
            break
        print(f"climb add {picked} |I|={len(live)} gap={best_gap}")
    check("climbed", live)

    if HITS:
        print("SUMMARY: attack pattern (e) SAMPLED EVIDENCE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - adversarial islands "
        "(line12, triangle21, 3-cube, diagonal rod, L, greedy climb) all die "
        "within M1+M2+M3-t0+1; not the known S1 iff HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
