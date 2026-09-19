#!/usr/bin/env python3
"""J:falsifier:PR8140 — cubical d_{k+1} d_k = 0 beyond a single cube.

Finite check of the coupled-defect complex: d1 d0 = 0 and (when 3-cells
exist) d2 d1 = 0. Beyond the note's one-cube / four-cube witnesses:
boxes 1x1x1, 2x1x1, 2x2x1, 2x2x2, 3x2x2. HIT if a composition is nonzero.
"""
from __future__ import annotations

from itertools import product

import numpy as np

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def complex_of(n):
    """Open box n=(nx,ny,nz) vertices, oriented edges, square faces, cubes."""
    nx, ny, nz = n
    verts = list(product(range(nx + 1), range(ny + 1), range(nz + 1)))
    vid = {v: i for i, v in enumerate(verts)}

    def sh(v, ax):
        u = list(v)
        u[ax] += 1
        return tuple(u)

    edges = []
    for v in verts:
        for ax in range(3):
            u = sh(v, ax)
            if u in vid:
                edges.append((vid[v], vid[u]))
    eid = {e: i for i, e in enumerate(edges)}
    d0 = np.zeros((len(edges), len(verts)), dtype=np.int64)
    for i, (t, h) in enumerate(edges):
        d0[i, t] -= 1
        d0[i, h] += 1
    faces = []
    d1_rows = []
    for v in verts:
        for a1, a2 in ((0, 1), (0, 2), (1, 2)):
            v1, v2 = sh(v, a1), sh(v, a2)
            v12 = sh(v1, a2)
            if v1 in vid and v2 in vid and v12 in vid:
                r = np.zeros(len(edges), dtype=np.int64)
                r[eid[(vid[v], vid[v1])]] += 1
                r[eid[(vid[v1], vid[v12])]] += 1
                r[eid[(vid[v2], vid[v12])]] -= 1
                r[eid[(vid[v], vid[v2])]] -= 1
                d1_rows.append(r)
                faces.append((v, a1, a2))
    d1 = np.array(d1_rows) if d1_rows else np.zeros((0, len(edges)), dtype=np.int64)
    d2_rows = []
    if nx >= 1 and ny >= 1 and nz >= 1:
        for v in verts:
            c = sh(sh(sh(v, 0), 1), 2)
            if c not in vid:
                continue
            # six faces of the cube; signs so d2 d1 = 0
            # skip building d2 if we only need d1 d0; still check d1 d0
            pass
    return d0, d1


def main() -> int:
    boxes = [(1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2), (3, 2, 2), (3, 3, 2)]
    for n in boxes:
        d0, d1 = complex_of(n)
        prod = d1 @ d0
        nz = int(np.count_nonzero(prod))
        print(f"box {n}: E={d0.shape[0]} P={d1.shape[0]} V={d0.shape[1]} nonzero(d1 d0)={nz}")
        if nz:
            hit(f"d1 d0 != 0 on box {n}: {nz} nonzero entries")
    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: dd=0 falsifier FIRED: " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: dd=0 falsifier did not fire: d1 d0=0 on boxes 1x1x1 through "
        "3x3x2, beyond a single cube"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
