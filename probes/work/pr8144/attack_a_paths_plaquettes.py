#!/usr/bin/env python3
"""J:attack-a:PR8144 — witness realizability.

Declared setting: finite-clock Villain on a cubic complex; spatial paths of
length R, plaquettes, and a spatial square. Z^3 is bipartite: no triangles.
"""
from __future__ import annotations

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def l1(a, b):
    return sum(abs(a[i] - b[i]) for i in range(3))


def main():
    # Simple length-R axis path
    R = 4
    path = [(i, 0, 0) for i in range(R + 1)]
    if any(l1(path[i], path[i + 1]) != 1 for i in range(R)):
        hit("axis path is not a nearest-neighbour chain")
        return
    print(f"OK: simple length-{R} spatial path along e1 exists in Z^3")

    # Two distinct paths with the same endpoints (path comparison)
    p1 = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0)]
    p2 = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0)]
    if p1[0] != p2[0] or p1[-1] != p2[-1]:
        hit("comparison paths do not share endpoints")
        return
    if p1 == p2:
        hit("comparison paths are identical")
        return
    if any(l1(p1[i], p1[i + 1]) != 1 for i in range(len(p1) - 1)):
        hit("p1 not NN")
        return
    if any(l1(p2[i], p2[i + 1]) != 1 for i in range(len(p2) - 1)):
        hit("p2 not NN")
        return
    print("OK: two distinct NN paths from (0,0,0) to (2,1,0) exist (path comparison)")

    # Spatial plaquette: 4-cycle in a coordinate plane
    plaq = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    edges = list(zip(plaq, plaq[1:] + plaq[:1]))
    if any(l1(a, b) != 1 for a, b in edges):
        hit("plaquette is not a 4-cycle of NN edges")
        return
    if l1(plaq[0], plaq[2]) == 1 or l1(plaq[1], plaq[3]) == 1:
        hit("plaquette has a diagonal NN edge: a triangle")
        return
    colors = [(x[0] + x[1] + x[2]) % 2 for x in plaq]
    if colors != [0, 1, 0, 1]:
        hit(f"plaquette is not bipartite: colors {colors}")
        return
    print("OK: spatial plaquette is a bipartite 4-cycle (no triangles)")

    # Spatial square (four oriented edges) as used by transfer fixtures
    square_edges = [
        ((0, 0, 0), (1, 0, 0)),
        ((1, 0, 0), (1, 1, 0)),
        ((1, 1, 0), (0, 1, 0)),
        ((0, 1, 0), (0, 0, 0)),
    ]
    if any(l1(a, b) != 1 for a, b in square_edges):
        hit("spatial square has a non-NN edge")
        return
    print("OK: four-edge spatial square exists in a coordinate plane of Z^3")

    if HITS:
        print("SUMMARY: pattern (a) WITNESS REALIZABILITY fired; " + "; ".join(HITS))
    else:
        print(
            "SUMMARY: pattern (a) WITNESS REALIZABILITY — length-R spatial paths, "
            "two distinct equal-endpoint NN paths, a bipartite 4-cycle plaquette "
            "(no triangles) and a four-edge spatial square all exist in Z^3; "
            "0 failures; attack does not fire"
        )


if __name__ == "__main__":
    main()
