#!/usr/bin/env python3
"""Finite per-plaquette support under a unit-neighborhood link license.

This runner does not derive the gauge action from the axioms and does not
derive theta_bare. It checks a bounded finite statement: if the site
nearest-neighbor dependency relation is lifted to links by the
unit-neighborhood endpoint rule, then rooted simple length-4 loops are
plaquettes and licensed, while rooted simple length-6 loops are not licensed.
"""
from __future__ import annotations

import itertools
from pathlib import Path

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def add(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(x + y for x, y in zip(a, b))


def dist(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return sum(abs(x - y) for x, y in zip(a, b))


def edge(a: tuple[int, int, int], b: tuple[int, int, int]):
    return (tuple(a), tuple(b))


def closed_loops(length: int):
    dirs = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]
    loops = []
    for steps in itertools.product(dirs, repeat=length):
        pos = (0, 0, 0)
        pts = [pos]
        ok = True
        for i, direction in enumerate(steps):
            if i > 0 and add(steps[i - 1], direction) == (0, 0, 0):
                ok = False
                break
            pos = add(pos, direction)
            pts.append(pos)
        if not ok or pts[-1] != (0, 0, 0):
            continue
        edges = [edge(pts[i], pts[i + 1]) for i in range(length)]
        if len({frozenset(ed) for ed in edges}) == length:
            loops.append(edges)
    return loops


def unit_neighborhood_licensed(loop_edges) -> bool:
    """Every endpoint in the loop lies in B_1 of each target link."""
    for target in loop_edges:
        for used in loop_edges:
            for point in used:
                if min(dist(point, target[0]), dist(point, target[1])) > 1:
                    return False
    return True


def is_plaquette(loop_edges) -> bool:
    return len({point for ed in loop_edges for point in ed}) == 4


def main() -> int:
    print("=" * 88)
    print("PER-PLAQUETTE LINK-LICENSE FINITE ENUMERATION SUPPORT")
    print("=" * 88)

    docs = Path(__file__).resolve().parent.parent / "docs"

    section("Reference text checks")
    reachability = (docs / "LATTICE_NN_LIGHT_CONE_NOTE.md").read_text(encoding="utf-8")
    primitive = (docs / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md").read_text(
        encoding="utf-8"
    )
    check(
        "reachability note contains one-tick dependency wording",
        "allowed to use the value at" in reachability,
    )
    check(
        "reachability note contains listed-dependency boundary wording",
        "no arguments outside" in reachability,
    )
    check(
        "kinetic-isotropy primitive contains the one-tick form wording",
        "One tick is one edge in" in primitive,
    )

    section("Strict link lift check")
    plaquette = [
        edge((0, 0, 0), (1, 0, 0)),
        edge((1, 0, 0), (1, 1, 0)),
        edge((1, 1, 0), (0, 1, 0)),
        edge((0, 1, 0), (0, 0, 0)),
    ]
    share_site = lambda l1, l2: bool(set(l1) & set(l2))
    opposite_share = share_site(plaquette[0], plaquette[2]) or share_site(
        plaquette[1], plaquette[3]
    )
    check(
        "strict share-site lift rejects the plaquette's opposite edges",
        not opposite_share,
        "strict lift is too strict for plaquette support",
    )

    section("Finite loop enumeration")
    length4 = closed_loops(4)
    length6 = closed_loops(6)
    licensed4 = [loop for loop in length4 if unit_neighborhood_licensed(loop)]
    licensed6 = [loop for loop in length6 if unit_neighborhood_licensed(loop)]

    check(
        "length-4 rooted simple loops: expected count",
        len(length4) == 24,
        f"found {len(length4)}",
    )
    check(
        "length-4 rooted simple loops are all plaquettes",
        all(is_plaquette(loop) for loop in length4),
    )
    check(
        "length-4 plaquette loops all satisfy the unit-neighborhood license",
        len(licensed4) == len(length4),
        f"licensed {len(licensed4)} / {len(length4)}",
    )
    check(
        "length-6 rooted simple loops: expected count",
        len(length6) == 264,
        f"found {len(length6)}",
    )
    check(
        "length-6 rooted simple loops do not satisfy the unit-neighborhood license",
        len(licensed6) == 0,
        f"licensed {len(licensed6)} / {len(length6)}",
    )

    section("Scope guard")
    print("  Scope is finite enumeration support only.")
    print("  The paired source note excludes theta and downstream closure claims.")

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
