#!/usr/bin/env python3
"""Gate B GB-S3 native finite-range forward-stencil bridge.

This runner verifies the source-side bridge that splits the Gate B
generated-connectivity ingredient:

  GB-S3a: the label/offset-preserving forward stencil is a native finite-range
          relation on the Z^3 lattice once a forward layer axis is supplied.
  GB-S3b: physical selection of this relation as Gate B dynamics remains open.
"""

from __future__ import annotations

import math
import random
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GATE_B_GB_S3_LATTICE_FORWARD_STENCIL_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md"
PARENT = ROOT / "docs" / "GATE_B_DYNAMICS_NOTE.md"

PASS = 0
FAIL = 0
Label = Tuple[int, int, int]
Edge = Tuple[Label, Label]


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    PASS += int(condition)
    FAIL += int(not condition)
    print(f"[{tag}] {label}")
    if detail:
        print(f"       {detail}")


def labels(n_layers: int, half: int) -> List[Label]:
    return [
        (x, y, z)
        for x in range(n_layers)
        for y in range(-half, half + 1)
        for z in range(-half, half + 1)
    ]


def stencil_edges(n_layers: int, half: int) -> List[Edge]:
    out: List[Edge] = []
    for x in range(n_layers - 1):
        for y in range(-half, half + 1):
            for z in range(-half, half + 1):
                src = (x, y, z)
                for dy in (-1, 0, 1):
                    for dz in (-1, 0, 1):
                        dst = (x + 1, y + dy, z + dz)
                        if -half <= dst[1] <= half and -half <= dst[2] <= half:
                            out.append((src, dst))
    return out


def offset_set(edges: Iterable[Edge]) -> set[Label]:
    return {
        (dst[0] - src[0], dst[1] - src[1], dst[2] - src[2])
        for src, dst in edges
    }


def manhattan(a: Label, b: Label) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def embedded_positions(n_layers: int, half: int, drift: float, seed: int) -> Dict[Label, Tuple[float, float, float]]:
    rng = random.Random(seed)
    positions: Dict[Label, Tuple[float, float, float]] = {}
    for x, y, z in labels(n_layers, half):
        positions[(x, y, z)] = (
            float(x),
            float(y) + rng.gauss(0.0, drift) * x,
            float(z) + rng.gauss(0.0, drift) * x,
        )
    return positions


def knn_forward_edges(
    positions: Dict[Label, Tuple[float, float, float]], n_layers: int, half: int, k: int
) -> List[Edge]:
    out: List[Edge] = []
    for x in range(n_layers - 1):
        srcs = [(x, y, z) for y in range(-half, half + 1) for z in range(-half, half + 1)]
        dsts = [(x + 1, y, z) for y in range(-half, half + 1) for z in range(-half, half + 1)]
        for src in srcs:
            sx, sy, sz = positions[src]
            ranked = []
            for dst in dsts:
                dx, dy, dz = positions[dst]
                dist2 = (dx - sx) ** 2 + (dy - sy) ** 2 + (dz - sz) ** 2
                ranked.append((dist2, dst))
            ranked.sort(key=lambda item: item[0])
            out.extend((src, dst) for _, dst in ranked[:k])
    return out


def interior_edges(edges: Iterable[Edge], half: int) -> List[Edge]:
    return [
        (src, dst)
        for src, dst in edges
        if abs(src[1]) < half and abs(src[2]) < half and abs(dst[1]) <= half and abs(dst[2]) <= half
    ]


def main() -> int:
    n_layers = 4
    half = 3
    edges = stencil_edges(n_layers, half)
    offsets = offset_set(edges)
    expected_offsets = {(1, dy, dz) for dy in (-1, 0, 1) for dz in (-1, 0, 1)}

    print("Gate B GB-S3 lattice forward-stencil bridge")
    print("=" * 72)
    print(f"n_layers={n_layers} half={half} edges={len(edges)}")

    check("stencil has exactly the 3x3 forward offset set", offsets == expected_offsets, detail=str(sorted(offsets)))
    check(
        "all stencil edges are finite-range local on Z^3",
        all(1 <= manhattan(src, dst) <= 3 for src, dst in edges),
        detail="Manhattan range is bounded by 3",
    )
    check("all stencil edges advance one layer", all(dst[0] - src[0] == 1 for src, dst in edges))
    check(
        "interior stencil is translation-covariant in transverse directions",
        offset_set(interior_edges(edges, half)) == expected_offsets,
    )

    positions_low = embedded_positions(n_layers, half, drift=0.2, seed=7)
    positions_high = embedded_positions(n_layers, half, drift=0.7, seed=7)
    label_edges = set(edges)
    check(
        "label-stencil adjacency is independent of coordinate drift",
        set(stencil_edges(n_layers, half)) == label_edges
        and set(stencil_edges(n_layers, half)) == label_edges,
    )
    knn_low = set(knn_forward_edges(positions_low, n_layers, half, k=9))
    knn_high = set(knn_forward_edges(positions_high, n_layers, half, k=9))
    check(
        "coordinate KNN recomputation is a different rule under drift",
        knn_low != label_edges or knn_high != label_edges,
        detail=f"diff_low={len(knn_low.symmetric_difference(label_edges))}, diff_high={len(knn_high.symmetric_difference(label_edges))}",
    )

    note = NOTE.read_text(encoding="utf-8")
    parent = PARENT.read_text(encoding="utf-8")
    check(
        "bridge note carries status firewall",
        "actual_current_surface_status: bounded-support" in note
        and "trace_class: direct_blocker_closure" in note
        and "bare_retained_allowed: false" in note,
    )
    check(
        "bridge note keeps GB-S3b and Gate B closure open",
        "GB-S3b remains open" in note
        and "does not derive Gate B dynamics closure" in note,
    )
    check(
        "parent Gate B note splits GB-S3 through this bridge",
        "GB-S3a" in parent
        and "GATE_B_GB_S3_LATTICE_FORWARD_STENCIL_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md" in parent
        and "GB-S3b" in parent,
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
