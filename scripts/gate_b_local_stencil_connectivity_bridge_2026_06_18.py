#!/usr/bin/env python3
"""Gate B local-stencil connectivity bridge verifier.

This runner checks the narrow `GB-S3a` source bridge: the label/offset
forward connectivity used by the positive Gate B rows is a finite-range
local stencil on the framework Z^3 lattice and exactly matches the current
Gate B connectivity-tolerance runner adjacency.
"""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import gate_b_connectivity_tolerance as gate_b  # noqa: E402

AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"
NOTE_PATH = ROOT / "docs" / "GATE_B_LOCAL_STENCIL_CONNECTIVITY_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-18.md"
PARENT_PATH = ROOT / "docs" / "GATE_B_DYNAMICS_NOTE.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}")
    if detail:
        print(f"       {detail}")
    if ok:
        PASS += 1
    else:
        FAIL += 1


def idx(layer: int, iy: int, iz: int, half: int) -> int:
    span = 2 * half + 1
    return layer * (span * span) + (iy + half) * span + (iz + half)


def label(index: int, half: int) -> tuple[int, int, int]:
    span = 2 * half + 1
    layer, rem = divmod(index, span * span)
    y_slot, z_slot = divmod(rem, span)
    return layer, y_slot - half, z_slot - half


def stencil_targets(layer: int, iy: int, iz: int, n_layers: int, half: int) -> list[tuple[int, int, int]]:
    if layer >= n_layers - 1:
        return []
    out: list[tuple[int, int, int]] = []
    for dy in (-1, 0, 1):
        for dz in (-1, 0, 1):
            jy = iy + dy
            jz = iz + dz
            if -half <= jy <= half and -half <= jz <= half:
                out.append((layer + 1, jy, jz))
    return out


def theorem_adjacency(n_layers: int, half: int) -> dict[int, list[int]]:
    adj: dict[int, list[int]] = {}
    for layer in range(n_layers - 1):
        for iy in range(-half, half + 1):
            for iz in range(-half, half + 1):
                src = idx(layer, iy, iz, half)
                adj[src] = [idx(*target, half=half) for target in stencil_targets(layer, iy, iz, n_layers, half)]
    return adj


def edge_offsets(adj: dict[int, list[int]], half: int) -> list[tuple[int, int, int]]:
    offsets: list[tuple[int, int, int]] = []
    for src, targets in adj.items():
        l0, y0, z0 = label(src, half)
        for dst in targets:
            l1, y1, z1 = label(dst, half)
            offsets.append((l1 - l0, y1 - y0, z1 - z0))
    return offsets


def source_offsets(adj: dict[int, list[int]], source: int, half: int) -> set[tuple[int, int, int]]:
    l0, y0, z0 = label(source, half)
    return {
        (label(dst, half)[0] - l0, label(dst, half)[1] - y0, label(dst, half)[2] - z0)
        for dst in adj.get(source, [])
    }


def main() -> int:
    print("Gate B local-stencil connectivity bridge")
    print("=" * 72)

    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    note = NOTE_PATH.read_text(encoding="utf-8")
    parent = PARENT_PATH.read_text(encoding="utf-8")
    flat_axiom = " ".join(axiom.split())
    flat_note = " ".join(note.split())
    flat_parent = " ".join(parent.split())

    check(
        "Lattice axiom supplies Z^3, nearest-neighbor adjacency, and finite-range locality",
        "The site set is `Z^3`" in flat_axiom
        and "nearest-neighbor cubic adjacency" in flat_axiom
        and "Finite-range locality means finite support or finite graph-distance range" in flat_axiom,
    )

    n_layers = 5
    half = 3
    theorem_adj = theorem_adjacency(n_layers=n_layers, half=half)
    runner_graph = gate_b._build_fixed_connectivity(n_layers=n_layers, half=half)
    runner_adj = {src: list(targets) for src, targets in runner_graph.adj.items()}

    check(
        "theorem stencil exactly matches gate_b_connectivity_tolerance fixed adjacency",
        theorem_adj == runner_adj,
        f"theorem_edges={sum(len(v) for v in theorem_adj.values())}, runner_edges={sum(len(v) for v in runner_adj.values())}",
    )

    offsets = edge_offsets(theorem_adj, half)
    distances = [abs(dl) + abs(dy) + abs(dz) for dl, dy, dz in offsets]
    check(
        "every edge is finite range with cubic graph distance <= 3",
        offsets and max(distances) <= 3 and min(distances) >= 1,
        f"min_distance={min(distances)}, max_distance={max(distances)}",
    )

    check(
        "all edges advance exactly one layer",
        all(dl == 1 for dl, _dy, _dz in offsets),
        f"unique_layer_offsets={sorted({dl for dl, _dy, _dz in offsets})}",
    )

    check(
        "transverse offsets are restricted to {-1,0,1}^2",
        all(dy in (-1, 0, 1) and dz in (-1, 0, 1) for _dl, dy, dz in offsets),
        f"unique_offsets={sorted(set(offsets))}",
    )

    outdegrees = [len(targets) for targets in theorem_adj.values()]
    check(
        "out-degree is bounded by the 9-edge local stencil",
        max(outdegrees) == 9 and min(outdegrees) == 4,
        f"min_outdegree={min(outdegrees)}, max_outdegree={max(outdegrees)}",
    )

    interior_expected = {(1, dy, dz) for dy in (-1, 0, 1) for dz in (-1, 0, 1)}
    interior_sources = [
        idx(layer, iy, iz, half)
        for layer in range(n_layers - 1)
        for iy in range(-half + 1, half)
        for iz in range(-half + 1, half)
    ]
    check(
        "interior sources all have the same translation-covariant offset set",
        all(source_offsets(theorem_adj, src, half) == interior_expected for src in interior_sources),
        f"interior_sources={len(interior_sources)}",
    )

    corner_source = idx(0, -half, -half, half)
    check(
        "finite boundary only clips off-slab stencil targets",
        source_offsets(theorem_adj, corner_source, half) == {(1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)},
        f"corner_offsets={sorted(source_offsets(theorem_adj, corner_source, half))}",
    )

    terminal_sources = [
        idx(n_layers - 1, iy, iz, half)
        for iy in range(-half, half + 1)
        for iz in range(-half, half + 1)
    ]
    check(
        "terminal layer has no outgoing forward edges",
        all(src not in theorem_adj for src in terminal_sources),
        f"terminal_sources={len(terminal_sources)}",
    )

    check(
        "note states GB-S3a boundary without claiming Gate B closure",
        "`GB-S3a`" in note
        and "`GB-S3b`" in note
        and "not a Gate B dynamics closure" in flat_note
        and "the parent Gate B dynamics row remains an open gate" in flat_note,
    )

    check(
        "note explicitly includes gate_b_connectivity_tolerance helper source and cache",
        "Helper runner (audit packet must include)" in note
        and "scripts/gate_b_connectivity_tolerance.py" in note
        and "logs/runner-cache/gate_b_connectivity_tolerance.txt" in note
        and "_build_fixed_connectivity" in note,
    )

    check(
        "parent note wires the GB-S3 split and preserves open physical-growth selector",
        "2026-06-18 local stencil connectivity split" in parent
        and "GB-S3a" in parent
        and "GB-S3b" in parent
        and "physical selection/dynamical generation of that stencil remains supplied" in flat_parent,
    )

    check(
        "parent note still blocks scalar/readout/physical-gravity overclaims",
        "does not derive `GB-S1b`, `GB-S2`, a physical gravity readout, or a full Gate B dynamics theorem" in flat_parent
        and "does not promote `I_GateB`" in parent,
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print("runner_check_breakdown = {A: %d, B: 0, C: 0, D: 0, total_pass: %d}" % (PASS, PASS))
    if FAIL:
        return 1
    print(
        "VERDICT: GB-S3a is a finite-range Z^3 local-stencil bridge matching the "
        "Gate B runner adjacency; GB-S3b physical selection/readout remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
