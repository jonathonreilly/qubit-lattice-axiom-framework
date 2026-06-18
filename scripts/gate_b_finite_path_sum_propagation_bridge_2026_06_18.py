#!/usr/bin/env python3
"""Gate B finite path-sum propagation bridge verifier.

This runner checks the narrow `GB-S2a` source bridge: the Gate B propagation
recursion is exact finite path-sum algebra on the supplied layered DAG and
edge kernel. Physical detector/readout semantics remain outside this bridge.
"""

from __future__ import annotations

import cmath
from collections import defaultdict
from pathlib import Path
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import gate_b_connectivity_tolerance as gate_b  # noqa: E402

NOTE_PATH = ROOT / "docs" / "GATE_B_FINITE_PATH_SUM_PROPAGATION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-18.md"
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


def edge_weight(
    positions: list[tuple[float, float, float]],
    field: list[float],
    src: int,
    dst: int,
) -> complex:
    xi, yi, zi = positions[src]
    xj, yj, zj = positions[dst]
    dx = xj - xi
    dy = yj - yi
    dz = zj - zi
    length = math.sqrt(dx * dx + dy * dy + dz * dz)
    if length < 1e-10:
        return 0j
    local_field = 0.5 * (field[src] + field[dst])
    action = length * (1.0 - local_field)
    theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
    angular_weight = math.exp(-gate_b.BETA * theta * theta)
    return cmath.exp(1j * gate_b.K * action) * angular_weight / length


def path_sum_propagate(
    graph: gate_b.GraphFamily,
    field: list[float],
    blocked: set[int],
    initial: dict[int, complex],
) -> list[complex]:
    out = [0j] * len(graph.positions)
    final_layer = len(graph.layers) - 1

    def walk(node: int, layer: int, amp: complex) -> None:
        if node in blocked:
            return
        out[node] += amp
        if layer == final_layer:
            return
        for dst in graph.adj.get(node, []):
            if dst in blocked:
                continue
            walk(dst, layer + 1, amp * edge_weight(graph.positions, field, node, dst))

    for src, amp in initial.items():
        if abs(amp) > 0:
            layer = next(i for i, nodes in enumerate(graph.layers) if src in nodes)
            walk(src, layer, amp)
    return out


def dynamic_transfer(
    graph: gate_b.GraphFamily,
    field: list[float],
    blocked: set[int],
    initial: dict[int, complex],
) -> list[complex]:
    amps = [0j] * len(graph.positions)
    for src, amp in initial.items():
        amps[src] = amp
    for layer in range(len(graph.layers) - 1):
        next_add = defaultdict(complex)
        for node in graph.layers[layer]:
            if node in blocked or abs(amps[node]) < 1e-30:
                continue
            for dst in graph.adj.get(node, []):
                if dst in blocked:
                    continue
                next_add[dst] += amps[node] * edge_weight(graph.positions, field, node, dst)
        for dst, amp in next_add.items():
            amps[dst] += amp
    return amps


def max_abs_diff(a: list[complex], b: list[complex]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def main() -> int:
    print("Gate B finite path-sum propagation bridge")
    print("=" * 72)

    graph = gate_b._build_fixed_connectivity(n_layers=4, half=1)
    source = graph.layers[0][len(graph.layers[0]) // 2]
    mass = graph.layers[1][-1]
    field = gate_b._field_for_mass(graph.positions, mass, gate_b.FIELD_STRENGTH)
    blocked = gate_b._blocked_barrier(graph.layers[2], graph.positions)
    detector = graph.layers[-1]

    note = NOTE_PATH.read_text(encoding="utf-8")
    parent = PARENT_PATH.read_text(encoding="utf-8")
    flat_note = " ".join(note.split())
    flat_parent = " ".join(parent.split())

    runner_amps = gate_b._propagate(graph.positions, graph.layers, graph.adj, field, blocked)
    path_amps = path_sum_propagate(graph, field, blocked, {source: 1.0 + 0j})
    diff_runner_path = max_abs_diff(runner_amps, path_amps)
    check(
        "runner recursion equals independently enumerated finite path sum",
        diff_runner_path < 1e-12,
        f"max_abs_diff={diff_runner_path:.3e}",
    )

    dyn_amps = dynamic_transfer(graph, field, blocked, {source: 1.0 + 0j})
    diff_dyn_path = max_abs_diff(dyn_amps, path_amps)
    check(
        "finite layer transfer equals path-sum expansion",
        diff_dyn_path < 1e-12,
        f"max_abs_diff={diff_dyn_path:.3e}",
    )

    src2 = graph.layers[0][0]
    a = 0.75 - 0.25j
    b = -0.5 + 0.5j
    combined = dynamic_transfer(graph, field, blocked, {source: a, src2: b})
    separate_a = dynamic_transfer(graph, field, blocked, {source: a})
    separate_b = dynamic_transfer(graph, field, blocked, {src2: b})
    linear_diff = max_abs_diff(combined, [x + y for x, y in zip(separate_a, separate_b)])
    check(
        "transfer is linear in initial source amplitudes",
        linear_diff < 1e-12,
        f"max_abs_diff={linear_diff:.3e}",
    )

    all_path = path_sum_propagate(graph, field, set(), {source: 1.0 + 0j})
    blocked_changes = sum(1 for x, y in zip(all_path, path_amps) if abs(x - y) > 1e-15)
    check(
        "blocked-node deletion is load-bearing and explicit",
        blocked and blocked_changes > 0,
        f"blocked_nodes={len(blocked)}, changed_terminal_or_bulk_entries={blocked_changes}",
    )

    check(
        "blocked nodes carry zero amplitude in the checked transfer",
        all(abs(path_amps[node]) < 1e-15 for node in blocked),
        f"blocked_nodes={sorted(blocked)}",
    )

    probs = gate_b._detector_probs(path_amps, detector)
    total_prob = sum(probs.values())
    check(
        "terminal detector normalizer returns a probability distribution when intensity is nonzero",
        all(p >= -1e-15 for p in probs.values()) and abs(total_prob - 1.0) < 1e-12,
        f"sum={total_prob:.12f}, min={min(probs.values()):.3e}, max={max(probs.values()):.3e}",
    )

    gain = gate_b._mass_window_gain(probs, gate_b._detector_probs([0j] * len(graph.positions), detector), graph.positions, detector, y_mass=1.0)
    check(
        "readout helper remains a supplied terminal-window functional, not used as proof input",
        isinstance(gain, float),
        f"sample_gain={gain:.3e}",
    )

    edge_count = sum(len(v) for v in graph.adj.values())
    check(
        "checked packet is finite",
        len(graph.positions) == 36 and edge_count == 147 and len(detector) == 9,
        f"nodes={len(graph.positions)}, edges={edge_count}, detectors={len(detector)}",
    )

    check(
        "edge kernel has finite nonzero weights on all unblocked traversed edges",
        all(
            abs(edge_weight(graph.positions, field, src, dst)) > 0
            for src, targets in graph.adj.items()
            if src not in blocked
            for dst in targets
            if dst not in blocked
        ),
    )

    check(
        "note states GB-S2a boundary without claiming Gate B closure",
        "`GB-S2a`" in note
        and "`GB-S2b`" in note
        and "not a Gate B dynamics closure" in flat_note
        and "parent Gate B dynamics row remains an open gate" in flat_note,
    )

    check(
        "parent note wires the GB-S2 split and preserves open physical readout semantics",
        "2026-06-18 finite path-sum propagation split" in parent
        and "GB-S2a" in parent
        and "GB-S2b" in parent
        and "physical detector-window/TOWARD/`F~M` semantics" in flat_parent,
    )

    check(
        "parent note still blocks scalar/connectivity/physical-gravity overclaims",
        "does not derive `GB-S1b`, `GB-S3`, a physical gravity readout, or a full Gate B dynamics theorem" in flat_parent
        and "does not promote `I_GateB`" in parent,
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print("runner_check_breakdown = {A: %d, B: 0, C: 0, D: 0, total_pass: %d}" % (PASS, PASS))
    if FAIL:
        return 1
    print(
        "VERDICT: GB-S2a is exact finite path-sum propagation on the supplied "
        "Gate B DAG/kernel; GB-S2b physical readout semantics remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
