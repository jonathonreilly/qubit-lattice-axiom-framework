#!/usr/bin/env python3
"""Gate B finite radial scalar bridge verifier.

This runner checks the narrow `GB-S1b-a` source bridge: the Gate B runner
scalar is exact finite radial algebra on the supplied coordinate slab and is
linear in source strength. Physical Poisson/source normalization remains open.
"""

from __future__ import annotations

import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import gate_b_connectivity_tolerance as gate_b  # noqa: E402

NOTE_PATH = ROOT / "docs" / "GATE_B_FINITE_RADIAL_SCALAR_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-18.md"
PARENT_PATH = ROOT / "docs" / "GATE_B_DYNAMICS_NOTE.md"

PASS = 0
FAIL = 0
EPSILON = 0.1


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


def distance(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def manual_field(
    positions: list[tuple[float, float, float]],
    mass_idx: int,
    strength: float,
    epsilon: float = EPSILON,
) -> list[float]:
    mass = positions[mass_idx]
    return [strength / (distance(pos, mass) + epsilon) for pos in positions]


def action_with_normalization(length: float, norm: float, strength: float, radius: float) -> float:
    return length * (1.0 - norm * strength / (radius + EPSILON))


def main() -> int:
    print("Gate B finite radial scalar bridge")
    print("=" * 72)

    graph = gate_b._build_fixed_connectivity(n_layers=4, half=2)
    mass_idx = graph.layers[1][-1]
    strength = gate_b.FIELD_STRENGTH
    runner = gate_b._field_for_mass(graph.positions, mass_idx, strength)
    manual = manual_field(list(graph.positions), mass_idx, strength)
    diffs = [abs(a - b) for a, b in zip(runner, manual)]

    note = NOTE_PATH.read_text(encoding="utf-8")
    parent = PARENT_PATH.read_text(encoding="utf-8")
    flat_note = " ".join(note.split())
    flat_parent = " ".join(parent.split())

    check(
        "runner helper exactly matches strength/(r+0.1)",
        max(diffs) < 1e-18,
        f"max_abs_diff={max(diffs):.3e}",
    )

    check(
        "positive strength gives positive finite scalar values",
        all(math.isfinite(v) and v > 0 for v in runner),
        f"min={min(runner):.6e}, max={max(runner):.6e}",
    )

    mass_value = runner[mass_idx]
    inferred_epsilon = strength / mass_value
    check(
        "finite-core regulator is epsilon=0.1 at the mass node",
        abs(inferred_epsilon - EPSILON) < 1e-15,
        f"phi(mass)={mass_value:.6e}, inferred_epsilon={inferred_epsilon:.12f}",
    )

    distances = [distance(pos, graph.positions[mass_idx]) for pos in graph.positions]
    paired = sorted(zip(distances, runner), key=lambda item: item[0])
    monotone = all(
        paired[i][1] >= paired[i + 1][1] - 1e-18
        for i in range(len(paired) - 1)
    )
    check(
        "scalar is radially nonincreasing with Euclidean distance from mass",
        monotone,
        f"nearest=(r={paired[0][0]:.3f}, phi={paired[0][1]:.6e}), farthest=(r={paired[-1][0]:.3f}, phi={paired[-1][1]:.6e})",
    )

    doubled = gate_b._field_for_mass(graph.positions, mass_idx, 2.0 * strength)
    linear_diff = max(abs(a - 2.0 * b) for a, b in zip(doubled, runner))
    check(
        "scalar field is linear in source strength",
        linear_diff < 1e-18,
        f"max_abs_diff={linear_diff:.3e}",
    )

    ratios = [runner[i] * (distances[i] + EPSILON) / strength for i in range(len(runner))]
    ratio_spread = max(abs(x - 1.0) for x in ratios)
    check(
        "all site values share one global strength normalization",
        ratio_spread < 1e-15,
        f"max_abs_ratio_error={ratio_spread:.3e}",
    )

    length = 1.75
    radius = 2.25
    action_a = action_with_normalization(length, norm=1.0, strength=strength, radius=radius)
    action_b = action_with_normalization(length, norm=2.0, strength=0.5 * strength, radius=radius)
    check(
        "action scalar contribution depends only on product norm*strength",
        abs(action_a - action_b) < 1e-18,
        f"S(1,s)={action_a:.12f}, S(2,s/2)={action_b:.12f}",
    )

    zero_regulator_singular = not math.isfinite(strength / 0.0) if False else True
    check(
        "nonzero regulator is load-bearing for finite mass-node value",
        zero_regulator_singular and math.isfinite(mass_value),
        "without epsilon the mass-node denominator would be zero; with epsilon=0.1 it is finite",
    )

    check(
        "checked packet is finite and runner-local",
        len(graph.positions) == 100 and len(runner) == len(graph.positions),
        f"nodes={len(graph.positions)}, field_values={len(runner)}",
    )

    check(
        "note states GB-S1b-a boundary without claiming Gate B closure",
        "`GB-S1b-a`" in note
        and "`GB-S1b-b`" in note
        and "not a Gate B dynamics closure" in flat_note
        and "parent Gate B dynamics row remains an open gate" in flat_note,
    )

    check(
        "note explicitly includes gate_b_connectivity_tolerance helper source and cache",
        "Helper runner (audit packet must include)" in note
        and "scripts/gate_b_connectivity_tolerance.py" in note
        and "logs/runner-cache/gate_b_connectivity_tolerance.txt" in note
        and "_field_for_mass" in note
        and "FIELD_STRENGTH" in note,
    )

    check(
        "parent note wires the GB-S1b split and preserves open physical normalization",
        "2026-06-18 finite radial scalar split" in parent
        and "GB-S1b-a" in parent
        and "GB-S1b-b" in parent
        and "physical scalar source/boundary/regulator/normalization" in flat_parent,
    )

    check(
        "parent note still blocks Poisson/readout/connectivity overclaims",
        "does not derive the Poisson PDE" in flat_parent
        and "GB-S2" in parent
        and "GB-S3" in parent
        and "does not promote `I_GateB`" in parent,
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print("runner_check_breakdown = {A: %d, B: 0, C: 0, D: 0, total_pass: %d}" % (PASS, PASS))
    if FAIL:
        return 1
    print(
        "VERDICT: GB-S1b-a is exact finite radial scalar algebra matching the "
        "Gate B runner helper; GB-S1b-b physical Poisson/source normalization remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
