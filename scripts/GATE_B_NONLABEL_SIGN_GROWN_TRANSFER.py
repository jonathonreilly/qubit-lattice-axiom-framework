#!/usr/bin/env python3
"""Grown-row non-label sign-law transfer test.

This is the grown-geometry follow-on to the earlier Gate B non-label
connectivity work. The question is whether the old geometry-sector architecture
still carries the retained fixed-field signed-source response when we apply it
to the current retained grown row.

Scope:
  - retained grown row only: drift=0.2, restore=0.7
    (retained-bounded authority: docs/GATE_B_GROWN_DISTANCE_LAW_NOTE.md)
  - compare label-grown control vs position-based geometry-sector candidate
  - exact zero-source and neutral same-point cancellation checks
  - small source-charge linearity sanity pass

The result is intentionally narrow: it should tell us whether the old
architecture genuinely applies here, not whether it becomes a geometry-generic
field theory.

This runner uses explicit PASS/FAIL checks with module-level _PASS / _FAIL
counters rather than only printing replay values. A successful run prints
``PASS=<n> FAIL=0`` and exits with status 0.
"""

from __future__ import annotations

import math
import os
import sys
from dataclasses import dataclass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from scripts.gate_b_grown_joint_package import grow


H = 0.5
K = 5.0
BETA = 0.8
NL = 25
DRIFT = 0.2
RESTORE = 0.7
SOURCE_Z = 3.0
SOURCE_STRENGTH = 5e-5
FIELD_POWER = 1
OFFSET = 1.0
MIN_EDGES = 5
SEEDS = [0]

# Module-level PASS/FAIL counters (visible to importers / audit scrapers).
_PASS = 0
_FAIL = 0

# Numerical pass criteria for the seed-0 retained grown-row replay.
ZERO_NEUTRAL_TOL = 1e-12             # zero-source and neutral controls must vanish
SIGN_ANTISYMMETRY_REL_TOL = 5e-3     # | (plus + minus) / max(|plus|, |minus|) |
CHARGE_LINEARITY_TOL = 5e-3          # | charge_exponent - 1 |
ORIENTATION_REQUIRES_PLUS_NEGATIVE = True  # plus delta_z < 0, minus delta_z > 0
SIGNAL_MAGNITUDE_MIN = 1e-6          # geometry-sector response must be nonzero


@dataclass(frozen=True)
class Family:
    positions: list[tuple[float, float, float]]
    layers: list[list[int]]
    adj: dict[int, list[int]]


def _check(name: str, ok: bool, detail: str = "") -> bool:
    """Record a PASS/FAIL check at module scope and print it."""

    global _PASS, _FAIL
    status = "PASS" if ok else "FAIL"
    if ok:
        _PASS += 1
    else:
        _FAIL += 1
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return ok


def _nearest_node_in_layer(
    pos: list[tuple[float, float, float]],
    layer_nodes: list[int],
    x_target: float,
    y_target: float,
    z_target: float,
) -> int | None:
    best = None
    best_d = float("inf")
    for idx in layer_nodes:
        x, y, z = pos[idx]
        d = (x - x_target) ** 2 + (y - y_target) ** 2 + (z - z_target) ** 2
        if d < best_d:
            best = idx
            best_d = d
    return best


def _field_from_sources(
    pos: list[tuple[float, float, float]],
    layers: list[list[int]],
    sources: list[tuple[float, int]],
) -> list[float]:
    field = [0.0] * len(pos)
    source_layer = NL // 3
    x_target = source_layer * H
    for z_phys, charge in sources:
        node = _nearest_node_in_layer(pos, layers[source_layer], x_target, 0.0, z_phys)
        if node is None:
            continue
        mx, my, mz = pos[node]
        for i, (x, y, z) in enumerate(pos):
            r = math.sqrt((x - mx) ** 2 + (y - my) ** 2 + (z - mz) ** 2) + 0.1
            field[i] += charge * SOURCE_STRENGTH / (r**FIELD_POWER)
    return field


def _propagate(pos: list[tuple[float, float, float]], adj: dict[int, list[int]], field: list[float]) -> list[complex]:
    n = len(pos)
    order = sorted(range(n), key=lambda i: pos[i][0])
    amps = [0j] * n
    amps[0] = 1.0
    hm = H * H
    for i in order:
        ai = amps[i]
        if abs(ai) < 1e-30:
            continue
        for j in adj.get(i, []):
            dx = pos[j][0] - pos[i][0]
            dy = pos[j][1] - pos[i][1]
            dz = pos[j][2] - pos[i][2]
            L = math.sqrt(dx * dx + dy * dy + dz * dz)
            if L < 1e-10:
                continue
            lf = 0.5 * (field[i] + field[j])
            act = L * (1.0 + lf)
            theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
            w = math.exp(-BETA * theta * theta)
            amps[j] += ai * complex(math.cos(K * act), math.sin(K * act)) * w * hm / (L * L)
    return amps


def _centroid_z(amps: list[complex], pos: list[tuple[float, float, float]], det: list[int]) -> float:
    total = 0.0
    weighted = 0.0
    for i in det:
        p = abs(amps[i]) ** 2
        total += p
        weighted += p * pos[i][2]
    return weighted / total if total > 1e-30 else 0.0


def _build_geometry_sector_grown(fam: Family) -> Family:
    """Build a position-based sector stencil from the grown row itself."""

    pos, layers = fam.positions, fam.layers
    adj: dict[int, list[int]] = {}

    for layer in range(len(layers) - 1):
        dst_nodes = layers[layer + 1]
        dst_pos = [pos[i] for i in dst_nodes]
        for src in layers[layer]:
            sx, sy, sz = pos[src]
            sector_best: dict[tuple[int, int], tuple[float, int]] = {}
            ranked: list[tuple[float, int]] = []
            for dst, (dx, dy, dz) in zip(dst_nodes, dst_pos):
                by = max(-1, min(1, int(round((dy - sy) / H))))
                bz = max(-1, min(1, int(round((dz - sz) / H))))
                dist2 = (dx - sx) ** 2 + (dy - sy) ** 2 + (dz - sz) ** 2
                ranked.append((dist2, dst))
                key = (by, bz)
                prev = sector_best.get(key)
                if prev is None or dist2 < prev[0]:
                    sector_best[key] = (dist2, dst)

            selected = [dst for _, dst in sorted(sector_best.values(), key=lambda item: item[0])]
            for _, dst in sorted(ranked, key=lambda item: item[0]):
                if len(selected) >= MIN_EDGES:
                    break
                if dst not in selected:
                    selected.append(dst)
            adj[src] = selected

    return Family(pos, layers, adj)


def _evaluate_family(fam: Family) -> dict[str, float]:
    pos, layers, adj = fam.positions, fam.layers, fam.adj
    det = layers[-1]
    free = _propagate(pos, adj, [0.0] * len(pos))
    z_free = _centroid_z(free, pos, det)

    cases = {
        "zero": [],
        "plus": [(SOURCE_Z, +1)],
        "minus": [(SOURCE_Z, -1)],
        "neutral": [(SOURCE_Z, +1), (SOURCE_Z, -1)],
        "double": [(SOURCE_Z, +2)],
    }
    out: dict[str, float] = {}
    for label, sources in cases.items():
        field = _field_from_sources(pos, layers, sources)
        amps = _propagate(pos, adj, field)
        out[label] = _centroid_z(amps, pos, det) - z_free
    out["alpha"] = math.log(abs(out["double"] / out["plus"])) / math.log(2.0) if abs(out["plus"]) > 1e-30 and abs(out["double"]) > 1e-30 else float("nan")
    return out


def _print_case(name: str, out: dict[str, float]) -> None:
    print(name)
    print(f"  zero-source delta_z        {out['zero']:+.6e}")
    print(f"  single +1 delta_z          {out['plus']:+.6e}")
    print(f"  single -1 delta_z          {out['minus']:+.6e}")
    print(f"  neutral +1/-1 delta_z      {out['neutral']:+.6e}")
    print(f"  double +2 delta_z          {out['double']:+.6e}")
    print(f"  charge exponent            {out['alpha']:.6f}")


def _check_zero_controls(label: str, out: dict[str, float]) -> None:
    """Zero-source and neutral controls must vanish to numerical tolerance."""

    _check(
        f"{label}: zero-source delta_z vanishes",
        abs(out["zero"]) <= ZERO_NEUTRAL_TOL,
        f"|delta_z_zero|={abs(out['zero']):.3e}, tol={ZERO_NEUTRAL_TOL:.0e}",
    )
    _check(
        f"{label}: neutral +1/-1 delta_z vanishes",
        abs(out["neutral"]) <= ZERO_NEUTRAL_TOL,
        f"|delta_z_neutral|={abs(out['neutral']):.3e}, tol={ZERO_NEUTRAL_TOL:.0e}",
    )


def _check_sign_response(label: str, out: dict[str, float]) -> None:
    """Single-source sign response must be antisymmetric, oriented, and nonzero."""

    mag = max(abs(out["plus"]), abs(out["minus"]))
    asym = abs(out["plus"] + out["minus"]) / mag if mag > 0 else float("inf")
    _check(
        f"{label}: single +1 / single -1 are antisymmetric to relative tolerance",
        asym <= SIGN_ANTISYMMETRY_REL_TOL,
        f"|plus+minus|/max={asym:.3e}, tol={SIGN_ANTISYMMETRY_REL_TOL:.0e}",
    )
    if ORIENTATION_REQUIRES_PLUS_NEGATIVE:
        _check(
            f"{label}: single +1 produces negative delta_z (toward sign convention)",
            out["plus"] < 0.0,
            f"delta_z_plus={out['plus']:+.3e}",
        )
        _check(
            f"{label}: single -1 produces positive delta_z (toward sign convention)",
            out["minus"] > 0.0,
            f"delta_z_minus={out['minus']:+.3e}",
        )
    _check(
        f"{label}: single-source signal magnitude above numerical floor",
        mag >= SIGNAL_MAGNITUDE_MIN,
        f"max(|plus|,|minus|)={mag:.3e}, floor={SIGNAL_MAGNITUDE_MIN:.0e}",
    )


def _check_charge_linearity(label: str, out: dict[str, float]) -> None:
    """Charge exponent should be near 1 for a linear sign-law response."""

    if math.isnan(out["alpha"]):
        _check(f"{label}: charge exponent is finite", False, "alpha=nan")
        return
    _check(
        f"{label}: charge exponent within tolerance of 1.0",
        abs(out["alpha"] - 1.0) <= CHARGE_LINEARITY_TOL,
        f"|alpha-1|={abs(out['alpha']-1.0):.3e}, tol={CHARGE_LINEARITY_TOL:.0e}",
    )


def main() -> int:
    print("=" * 94)
    print("GROWN-ROW NON-LABEL SIGN-LAW TEST")
    print("  question: can the old geometry-sector architecture carry the fixed-field")
    print("  signed-source response on the retained grown row?")
    print("  retained grown-row authority: docs/GATE_B_GROWN_DISTANCE_LAW_NOTE.md")
    print("=" * 94)
    print(f"h={H}, NL={NL}, drift={DRIFT}, restore={RESTORE}, seeds={SEEDS}")
    print(f"source_z={SOURCE_Z}, offset={OFFSET}, strength={SOURCE_STRENGTH:g}")
    print()

    for seed in SEEDS:
        pos, adj, layers = grow(DRIFT, RESTORE, seed)
        label_family = Family(pos, layers, adj)
        sector_family = _build_geometry_sector_grown(label_family)

        label_out = _evaluate_family(label_family)
        sector_out = _evaluate_family(sector_family)

        print(f"seed={seed}")
        _print_case("label-grown control", label_out)
        _print_case("geometry-sector candidate", sector_out)
        print()

        # Both families must satisfy the transfer criteria for the narrowed
        # claim that the old geometry-sector architecture genuinely applies on
        # the retained grown row.
        print("Transfer checks (label-grown control):")
        _check_zero_controls("label-grown control", label_out)
        _check_sign_response("label-grown control", label_out)
        _check_charge_linearity("label-grown control", label_out)

        print("Transfer checks (geometry-sector candidate):")
        _check_zero_controls("geometry-sector candidate", sector_out)
        _check_sign_response("geometry-sector candidate", sector_out)
        _check_charge_linearity("geometry-sector candidate", sector_out)

    print()
    print("SAFE READ")
    print("  - If the geometry-sector candidate keeps the zero/neutral controls at zero")
    print("    and preserves the charge-linear sign response, then the old architecture")
    print("    genuinely applies to the current grown-row fixed-field lane.")
    print("  - If it collapses to zero or loses charge linearity, the old architecture")
    print("    was specific to the earlier Gate B families and does not transplant cleanly.")
    print()
    print(f"PASS={_PASS} FAIL={_FAIL}")
    print(f"SUMMARY: PASS={_PASS} FAIL={_FAIL}")
    return 0 if _FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
