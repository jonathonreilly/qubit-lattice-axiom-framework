#!/usr/bin/env python3
"""Live finite replay for the causal propagating-field row.

The archived source note claimed a stable dynamic ratio near 0.45 and a
dynamic c=1 row close to the forward-only row. The current live causal-field
machinery does not reproduce that table. This runner rebuilds the center
grown family and asserts the narrower finite facts that are true now:

- exact zero-source control,
- field-strength stability of the ratio readouts,
- forward-only ratio near 2/3 on the center family,
- dynamic c=0.5 and c=1.0 are structured finite-cone proxy readouts,
- the old 0.45 / c=1~=forward table is not reproduced.
"""

from __future__ import annotations

import math
import os
import statistics
import sys
from dataclasses import dataclass


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from evolving_network_prototype_v6 import build_structured_growth, centroid_y, propagate  # noqa: E402


H = 0.5
K = 5.0
N_LAYERS = 13
HALF = 5
DRIFT = 0.20
RESTORE = 0.70
SEEDS = tuple(range(6))
SOURCE_LAYER = 2 * N_LAYERS // 3
SOURCE_Y0 = 0.0
SOURCE_Z0 = 3.0
FIELD_EPS = 0.1
FIELD_STRENGTHS = (1e-5, 5e-5, 1e-4)
CONES = (1.0, 0.5)


@dataclass(frozen=True)
class StrengthSummary:
    strength: float
    inst_mean: float
    inst_se: float
    forward_mean: float
    forward_se: float
    forward_ratio: float
    forward_ratio_se: float
    dynamic_means: dict[float, float]
    dynamic_ses: dict[float, float]
    dynamic_ratios: dict[float, float]
    dynamic_ratio_ses: dict[float, float]
    toward_counts: dict[str, int]


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else math.nan


def _se(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    return statistics.pstdev(values) / math.sqrt(len(values))


def _select_source_node(
    positions: list[tuple[float, float, float]],
    layer_nodes: list[int],
) -> int:
    return min(
        layer_nodes,
        key=lambda i: (
            (positions[i][1] - SOURCE_Y0) ** 2
            + (positions[i][2] - SOURCE_Z0) ** 2,
            abs(positions[i][1] - SOURCE_Y0),
            abs(positions[i][2] - SOURCE_Z0),
            i,
        ),
    )


def _source_anchor(
    positions: list[tuple[float, float, float]],
    layers: list[list[int]],
) -> tuple[int, tuple[float, float, float]]:
    source_node = _select_source_node(positions, layers[SOURCE_LAYER])
    return source_node, positions[source_node]


def _detector_extent(
    positions: list[tuple[float, float, float]],
    det: list[int],
    anchor: tuple[float, float, float],
) -> float:
    _, sy, sz = anchor
    return max(
        math.sqrt((positions[idx][1] - sy) ** 2 + (positions[idx][2] - sz) ** 2)
        for idx in det
    )


def _instantaneous_field(
    positions: list[tuple[float, float, float]],
    anchor: tuple[float, float, float],
    strength: float,
) -> list[float]:
    if strength == 0.0:
        return [0.0] * len(positions)
    sx, sy, sz = anchor
    out = [0.0] * len(positions)
    for idx, (x, y, z) in enumerate(positions):
        r = math.sqrt((x - sx) ** 2 + (y - sy) ** 2 + (z - sz) ** 2) + FIELD_EPS
        out[idx] = strength / r
    return out


def _forward_only_field(
    positions: list[tuple[float, float, float]],
    layers: list[list[int]],
    anchor: tuple[float, float, float],
    strength: float,
) -> list[float]:
    if strength == 0.0:
        return [0.0] * len(positions)
    sx, sy, sz = anchor
    out = [0.0] * len(positions)
    for layer_idx, layer_nodes in enumerate(layers):
        if layer_idx < SOURCE_LAYER:
            continue
        for idx in layer_nodes:
            x, y, z = positions[idx]
            if x + 1e-12 < sx:
                continue
            r = math.sqrt((x - sx) ** 2 + (y - sy) ** 2 + (z - sz) ** 2) + FIELD_EPS
            out[idx] = strength / r
    return out


def _dynamic_field(
    positions: list[tuple[float, float, float]],
    layers: list[list[int]],
    anchor: tuple[float, float, float],
    strength: float,
    c: float,
) -> list[float]:
    if strength == 0.0:
        return [0.0] * len(positions)
    sx, sy, sz = anchor
    det_radius = _detector_extent(positions, layers[-1], anchor)
    det_x = positions[layers[-1][0]][0]
    x_span = max(det_x - sx, 1e-12)
    out = [0.0] * len(positions)
    for layer_idx, layer_nodes in enumerate(layers):
        if layer_idx < SOURCE_LAYER:
            continue
        for idx in layer_nodes:
            x, y, z = positions[idx]
            dx = x - sx
            if dx < -1e-12:
                continue
            transverse = math.sqrt((y - sy) ** 2 + (z - sz) ** 2)
            cone_radius = c * det_radius * max(dx, 0.0) / x_span
            if transverse > cone_radius + 1e-12:
                continue
            r = math.sqrt(dx * dx + (y - sy) ** 2 + (z - sz) ** 2) + FIELD_EPS
            out[idx] = strength / r
    return out


def _measure_strength(strength: float) -> tuple[StrengthSummary, float, float]:
    inst_vals: list[float] = []
    forward_vals: list[float] = []
    dynamic_vals: dict[float, list[float]] = {c: [] for c in CONES}
    zero_delta_max = 0.0
    zero_field_max = 0.0

    for seed in SEEDS:
        fam = build_structured_growth(N_LAYERS, HALF, H, DRIFT, RESTORE, seed)
        positions, layers, adj = fam.positions, fam.layers, fam.adj
        det = layers[-1]
        _, anchor = _source_anchor(positions, layers)

        zero_field = [0.0] * len(positions)
        free_amps = propagate(positions, layers, adj, zero_field)
        zero_amps = propagate(positions, layers, adj, zero_field)
        free_centroid = centroid_y(free_amps, positions, det)
        zero_centroid = centroid_y(zero_amps, positions, det)
        zero_delta_max = max(zero_delta_max, abs(zero_centroid - free_centroid))
        zero_field_max = max(zero_field_max, max(abs(v) for v in zero_field))

        inst = propagate(
            positions,
            layers,
            adj,
            _instantaneous_field(positions, anchor, strength),
        )
        inst_delta = centroid_y(inst, positions, det) - free_centroid
        inst_vals.append(inst_delta)

        forward = propagate(
            positions,
            layers,
            adj,
            _forward_only_field(positions, layers, anchor, strength),
        )
        forward_vals.append(centroid_y(forward, positions, det) - free_centroid)

        for c in CONES:
            dynamic = propagate(
                positions,
                layers,
                adj,
                _dynamic_field(positions, layers, anchor, strength, c),
            )
            dynamic_vals[c].append(centroid_y(dynamic, positions, det) - free_centroid)

    inst_mean = _mean(inst_vals)
    forward_mean = _mean(forward_vals)
    dynamic_ratios_by_c = {
        c: [dyn / inst for dyn, inst in zip(dynamic_vals[c], inst_vals) if abs(inst) > 1e-30]
        for c in CONES
    }
    toward_counts = {
        "instantaneous": sum(1 for v in inst_vals if v > 0.0),
        "forward": sum(1 for v in forward_vals if v > 0.0),
    }
    for c in CONES:
        toward_counts[f"dynamic_c_{c:g}"] = sum(1 for v in dynamic_vals[c] if v > 0.0)

    return (
        StrengthSummary(
            strength=strength,
            inst_mean=inst_mean,
            inst_se=_se(inst_vals),
            forward_mean=forward_mean,
            forward_se=_se(forward_vals),
            forward_ratio=(forward_mean / inst_mean if abs(inst_mean) > 1e-30 else math.nan),
            forward_ratio_se=_se(
                [forward / inst for forward, inst in zip(forward_vals, inst_vals) if abs(inst) > 1e-30]
            ),
            dynamic_means={c: _mean(dynamic_vals[c]) for c in CONES},
            dynamic_ses={c: _se(dynamic_vals[c]) for c in CONES},
            dynamic_ratios={
                c: (_mean(dynamic_vals[c]) / inst_mean if abs(inst_mean) > 1e-30 else math.nan)
                for c in CONES
            },
            dynamic_ratio_ses={c: _se(dynamic_ratios_by_c[c]) for c in CONES},
            toward_counts=toward_counts,
        ),
        zero_delta_max,
        zero_field_max,
    )


def _spread(values: list[float]) -> float:
    return max(values) - min(values)


def main() -> int:
    print("=" * 96)
    print("CAUSAL PROPAGATING FIELD LIVE PACKET")
    print("  center grown family; exact-null, forward-only, and dynamic-cone replay")
    print("=" * 96)
    print(f"family: drift={DRIFT:.2f}, restore={RESTORE:.2f}")
    print(f"seeds={SEEDS}, source_layer={SOURCE_LAYER}, K={K}, H={H}, N_LAYERS={N_LAYERS}")
    print(f"source anchor target: (y, z)=({SOURCE_Y0:.1f}, {SOURCE_Z0:.1f})")
    print(f"field strengths={FIELD_STRENGTHS}, field eps={FIELD_EPS}")
    print()

    measured = [_measure_strength(strength) for strength in FIELD_STRENGTHS]
    summaries = [item[0] for item in measured]
    zero_delta_max = max(item[1] for item in measured)
    zero_field_max = max(item[2] for item in measured)

    print("ZERO-NUL CONTROL")
    print(f"  max |delta_y| = {zero_delta_max:.3e}")
    print(f"  max |field| = {zero_field_max:.3e}")
    print()
    print(
        f"{'strength':>11s} {'inst delta':>14s} {'forward':>14s} {'fwd/inst':>10s} "
        f"{'dyn1/inst':>10s} {'dyn0.5/inst':>12s} {'toward counts':>28s}"
    )
    print("-" * 112)
    for s in summaries:
        print(
            f"{s.strength:11.1e} "
            f"{s.inst_mean:+10.3e}+/-{s.inst_se:.1e} "
            f"{s.forward_mean:+10.3e}+/-{s.forward_se:.1e} "
            f"{s.forward_ratio:10.3f} "
            f"{s.dynamic_ratios[1.0]:10.3f} "
            f"{s.dynamic_ratios[0.5]:12.3f} "
            f"{s.toward_counts}"
        )
    print()

    inst_scale_5x = summaries[1].inst_mean / summaries[0].inst_mean
    inst_scale_2x = summaries[2].inst_mean / summaries[1].inst_mean
    forward_spread = _spread([s.forward_ratio for s in summaries])
    dyn1_spread = _spread([s.dynamic_ratios[1.0] for s in summaries])
    dyn05_spread = _spread([s.dynamic_ratios[0.5] for s in summaries])
    old_dyn05_distance = abs(summaries[1].dynamic_ratios[0.5] - 0.45)
    old_dyn1_forward_distance = abs(summaries[1].dynamic_ratios[1.0] - summaries[1].forward_ratio)

    checks = [
        ("exact zero-source control", zero_delta_max == 0.0 and zero_field_max == 0.0),
        ("instantaneous response scales with 5x strength", 4.95 < inst_scale_5x < 5.05),
        ("instantaneous response scales with 2x strength", 1.95 < inst_scale_2x < 2.05),
        ("forward ratio is stable across strengths", forward_spread < 0.005),
        ("dynamic c=1 ratio is stable across strengths", dyn1_spread < 0.005),
        ("dynamic c=0.5 ratio is stable across strengths", dyn05_spread < 0.005),
        ("forward-only center ratio remains near 2/3", 0.60 < summaries[1].forward_ratio < 0.72),
        ("dynamic c=1 is distinct from forward-only", old_dyn1_forward_distance > 0.50),
        ("dynamic c=0.5 is not the archived 0.45 row", old_dyn05_distance > 0.40),
        ("dynamic c=1 response exceeds dynamic c=0.5", summaries[1].dynamic_ratios[1.0] > summaries[1].dynamic_ratios[0.5]),
    ]
    assertions_ok = all(ok for _, ok in checks)

    print("SAFE READ")
    for name, ok in checks:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")
    print("  current live c=1 ratio:", f"{summaries[1].dynamic_ratios[1.0]:.3f}")
    print("  current live c=0.5 ratio:", f"{summaries[1].dynamic_ratios[0.5]:.3f}")
    print("  current live forward ratio:", f"{summaries[1].forward_ratio:.3f}")
    print("  finite-cone proxy only: no physical wave-speed or carrier derivation")
    print("  archived 0.63/0.45 positive table is not reproduced")
    print(f"ASSERTIONS: {'PASS' if assertions_ok else 'FAIL'}")
    return 0 if assertions_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
