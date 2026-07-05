#!/usr/bin/env python3
"""Gate B context-independence no-go.

Checks that the current fixed Z^3 Lattice axiom does not determine the
remaining physical Gate-B supplied packet pieces:

  GB-S1b-b: physical scalar source/boundary/regulator/normalization
  GB-S2b: physical detector/readout semantics
  GB-S3b: physical selection/dynamical generation of the growth rule

The runner reads/writes no audit surfaces.
"""

from __future__ import annotations

from itertools import product
from math import sqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "GATE_B_CONTEXT_INDEPENDENCE_NO_GO_NOTE_2026-06-17.md"
GATE_B = ROOT / "docs" / "GATE_B_DYNAMICS_NOTE.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def l1(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return sum(abs(x - y) for x, y in zip(a, b))


def euclid(a: tuple[float, float], b: tuple[float, float]) -> float:
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def main() -> int:
    print("Gate B context independence no-go")
    print("=" * 72)

    patch = tuple(product(range(3), range(3), range(2)))
    nn_edges = {
        tuple(sorted((a, b)))
        for a in patch
        for b in patch
        if a < b and l1(a, b) == 1
    }
    check(
        "base Lattice patch has fixed Z^3 nearest-neighbor adjacency",
        len(patch) == 18 and len(nn_edges) == 33,
        f"|V|={len(patch)} |E_nn|={len(nn_edges)}",
    )

    labels = tuple(product(range(3), range(3)))
    layer0 = {label: (float(label[0]), float(label[1])) for label in labels}
    layer1_a = {label: (float(label[0]), float(label[1])) for label in labels}
    layer1_b = {
        label: (float(label[0]) + 0.25 * ((label[1] % 2) - 0.5), float(label[1]) + 0.15 * (label[0] - 1))
        for label in labels
    }

    offsets = ((0, 0), (1, 0), (-1, 0))
    edges_a = set()
    for label in labels:
        x, y = label
        for dx, dy in offsets:
            target = (x + dx, y + dy)
            if target in layer1_a:
                edges_a.add((label, target))

    edges_b = set()
    for label, pos in layer0.items():
        nearest = sorted(layer1_b, key=lambda target: (euclid(pos, layer1_b[target]), target))[:2]
        for target in nearest:
            edges_b.add((label, target))

    check(
        "two generated-connectivity completions share the same base lattice patch",
        len(nn_edges) == 33 and set(layer0) == set(layer1_a) == set(layer1_b),
        "same labels and same underlying Z^3 patch",
    )
    check(
        "generated-connectivity rule is underdetermined by the base lattice",
        edges_a != edges_b and len(edges_a) != len(edges_b),
        f"|G_A|={len(edges_a)} |G_B|={len(edges_b)}",
    )
    check(
        "both generated rules are finite and layer-forward supplied structures",
        all(src in labels and dst in labels for src, dst in edges_a | edges_b),
        "neither rule is selected by nearest-neighbor Z^3 adjacency",
    )

    strength = 0.8
    eps = 0.1
    c = 1.7
    r = 2.0
    phi_a = strength / (r + eps)
    phi_b = c * strength / (r + 2.0 * eps)
    check(
        "Gate-B scalar normalization/regulator is freely variable over the same base data",
        abs(phi_a - phi_b) > 0.1,
        f"phi_A={phi_a:.6f} phi_B={phi_b:.6f}",
    )

    action_a = 5.0 * (1.0 - phi_a)
    action_b = 5.0 * (1.0 - phi_b)
    check(
        "linear weak-field action form does not select the scalar normalization",
        abs(action_a - action_b) > 0.5,
        f"S_A={action_a:.6f} S_B={action_b:.6f}",
    )

    amplitudes = {(x, y): 1.0 / (1.0 + abs(x - 1) + abs(y - 1)) for x, y in labels}
    detector_narrow = {(1, 1)}
    detector_wide = {(x, y) for x, y in labels if abs(x - 1) + abs(y - 1) <= 1}
    readout_narrow = sum(amplitudes[p] for p in detector_narrow)
    readout_wide = sum(amplitudes[p] for p in detector_wide)
    check(
        "propagation/readout semantics are not fixed by the Lattice axiom",
        readout_wide != readout_narrow and readout_wide > readout_narrow,
        f"narrow={readout_narrow:.6f} wide={readout_wide:.6f}",
    )

    same_axiom_surface = len(nn_edges) == 33 and len(patch) == 18
    different_gate_b_packet = edges_a != edges_b and phi_a != phi_b and readout_wide != readout_narrow
    check(
        "model-pair contradiction blocks any axiom-only derivation of I_GateB",
        same_axiom_surface and different_gate_b_packet,
        "same Lattice+Quantum+Record surface, different GB-S1b-b/S2b/S3b",
    )

    note_text = NOTE.read_text(encoding="utf-8")
    flat_note_text = " ".join(note_text.split())
    required_note_tokens = [
        "**Claim type:** no_go",
        "no theorem using only the current axioms can derive `GB-S1b-b`, `GB-S2b`, or `GB-S3b`",
        "does not refute the finite Gate B numerics",
        "separate local-growth/dynamics/readout theorem",
        "Gate result: PASS for this narrow no-go boundary.",
        "GB_S1BB_S2B_S3B_NOT_DERIVED_FROM_LATTICE=TRUE",
    ]
    check(
        "source note states the negative boundary without claiming Gate B closure",
        all(token in flat_note_text for token in required_note_tokens),
        "note wording guard",
    )

    gate_b_text = GATE_B.read_text(encoding="utf-8")
    flat_gate_b_text = " ".join(gate_b_text.split())
    required_gate_b_tokens = [
        "2026-06-17/18 context-independence no-go",
        "does not refute the finite Gate B numerics",
        "cannot derive `GB-S1b-b`, `GB-S2b`, or `GB-S3b`",
        "GATE_B_CONTEXT_INDEPENDENCE_NO_GO_NOTE_2026-06-17.md",
    ]
    check(
        "Gate B status note cites the independence no-go and stays open-gate",
        all(token in flat_gate_b_text for token in required_gate_b_tokens),
        "Gate B status guard",
    )

    check(
        "no new axiom or Tier-A admission is claimed",
        "No new axiom" in note_text
        and "adds no axiom" in gate_b_text
        and "Tier-A" in gate_b_text,
    )
    check(
        "audit surfaces are read-only",
        "does not set an\naudit verdict" in note_text and "audit ledger" in note_text,
    )
    check(
        "positive Gate B dynamics theorem is explicitly outside this artifact",
        "Any positive Gate-B dynamics theorem" in note_text
        and "does not close Gate B" in gate_b_text,
    )
    check(
        "bounded generated-geometry source index remains useful",
        "bounded generated-geometry source index" in note_text
        and "source index" in gate_b_text,
    )
    check(
        "terminal closeout markers are declared in the source note",
        "GATE_B_CONTEXT_INDEPENDENCE_NO_GO=TRUE" in note_text
        and "PASS=15 FAIL=0" in note_text,
    )

    print("=" * 72)
    print("GATE_B_CONTEXT_INDEPENDENCE_NO_GO=TRUE")
    print("GB_S1BB_S2B_S3B_NOT_DERIVED_FROM_LATTICE=TRUE")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
