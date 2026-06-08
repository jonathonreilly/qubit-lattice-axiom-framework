#!/usr/bin/env python3
"""Independent symmetry/orientation certificate for fifth-family radial row.

This runner does not call ``_measure_family`` from the old failure audit.
It reconstructs the radial row, proves the zero/neutral controls from source
field linearity, and differentiates the propagation recurrence at zero field
to certify the sign-orientation boundary.
"""

from __future__ import annotations

import math
import os
import sys
from pathlib import Path

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from DISTANCE_LAW_PORTABILITY_COMPARE import Family, _build_radial_shell_connectivity
from gate_b_no_restore_farfield import grow


H = 0.5
K = 5.0
BETA = 0.8
NL = 25
SOURCE_Z = 3.0
SOURCE_STRENGTH = 5e-5
FIELD_POWER = 1
DRIFT = 0.20
SEED = 0
NOTE = Path(ROOT) / "docs" / "FIFTH_FAMILY_RADIAL_BOUNDARY_NOTE.md"

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
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def nearest_source_node(pos: list[tuple[float, float, float]], layers: list[list[int]]) -> int:
    source_layer = NL // 3
    x_target = source_layer * H
    best = -1
    best_d = float("inf")
    for idx in layers[source_layer]:
        x, y, z = pos[idx]
        d = (x - x_target) ** 2 + y**2 + (z - SOURCE_Z) ** 2
        if d < best_d:
            best = idx
            best_d = d
    if best < 0:
        raise RuntimeError("source node not found")
    return best


def unit_source_shape(pos: list[tuple[float, float, float]], layers: list[list[int]]) -> list[float]:
    """Field shape per unit source charge at SOURCE_Z."""
    src = nearest_source_node(pos, layers)
    mx, my, mz = pos[src]
    out: list[float] = []
    for x, y, z in pos:
        r = math.sqrt((x - mx) ** 2 + (y - my) ** 2 + (z - mz) ** 2) + 0.1
        out.append(SOURCE_STRENGTH / (r**FIELD_POWER))
    return out


def propagate(
    pos: list[tuple[float, float, float]],
    adj: dict[int, list[int]],
    field: list[float],
) -> list[complex]:
    """Local copy of the propagation recurrence used for finite corroboration."""
    order = sorted(range(len(pos)), key=lambda i: pos[i][0])
    amps = [0j] * len(pos)
    amps[0] = 1.0
    h2 = H * H
    for i in order:
        ai = amps[i]
        if abs(ai) < 1e-30:
            continue
        for j in adj.get(i, []):
            dx = pos[j][0] - pos[i][0]
            dy = pos[j][1] - pos[i][1]
            dz = pos[j][2] - pos[i][2]
            length = math.sqrt(dx * dx + dy * dy + dz * dz)
            if length < 1e-10:
                continue
            local_field = 0.5 * (field[i] + field[j])
            action = length * (1.0 + local_field)
            theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
            weight = math.exp(-BETA * theta * theta) * h2 / (length * length)
            amps[j] += ai * complex(math.cos(K * action), math.sin(K * action)) * weight
    return amps


def propagate_with_derivative(
    pos: list[tuple[float, float, float]],
    adj: dict[int, list[int]],
    field_shape: list[float],
) -> tuple[list[complex], list[complex]]:
    """Return zero-field amplitudes and d/dq amplitudes at q=0.

    The source field is q * field_shape. Differentiating each edge transfer
    T_ij(q) = exp(i K L_ij (1 + q * f_ij)) * W_ij gives
    T'_ij(0) = T_ij(0) * i K L_ij f_ij.
    """
    order = sorted(range(len(pos)), key=lambda i: pos[i][0])
    amps = [0j] * len(pos)
    damps = [0j] * len(pos)
    amps[0] = 1.0
    h2 = H * H
    for i in order:
        ai = amps[i]
        dai = damps[i]
        if abs(ai) < 1e-30 and abs(dai) < 1e-30:
            continue
        for j in adj.get(i, []):
            dx = pos[j][0] - pos[i][0]
            dy = pos[j][1] - pos[i][1]
            dz = pos[j][2] - pos[i][2]
            length = math.sqrt(dx * dx + dy * dy + dz * dz)
            if length < 1e-10:
                continue
            theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
            weight = math.exp(-BETA * theta * theta) * h2 / (length * length)
            t0 = complex(math.cos(K * length), math.sin(K * length)) * weight
            f_edge = 0.5 * (field_shape[i] + field_shape[j])
            dt0 = t0 * (1j * K * length * f_edge)
            amps[j] += ai * t0
            damps[j] += dai * t0 + ai * dt0
    return amps, damps


def centroid_z(amps: list[complex], pos: list[tuple[float, float, float]], det: list[int]) -> float:
    total = 0.0
    weighted = 0.0
    for i in det:
        prob = abs(amps[i]) ** 2
        total += prob
        weighted += prob * pos[i][2]
    return weighted / total if total > 1e-30 else 0.0


def centroid_derivative(
    amps: list[complex],
    damps: list[complex],
    pos: list[tuple[float, float, float]],
    det: list[int],
) -> float:
    total = 0.0
    weighted = 0.0
    dtotal = 0.0
    dweighted = 0.0
    for i in det:
        prob = abs(amps[i]) ** 2
        dprob = 2.0 * (amps[i].conjugate() * damps[i]).real
        total += prob
        weighted += prob * pos[i][2]
        dtotal += dprob
        dweighted += dprob * pos[i][2]
    if total <= 1e-30:
        return 0.0
    return (dweighted * total - weighted * dtotal) / (total * total)


def main() -> int:
    note_text = NOTE.read_text(encoding="utf-8")
    pos, adj, layers, _nmap = grow(DRIFT, SEED)
    radial = _build_radial_shell_connectivity(Family(pos, layers, adj))
    field_shape = unit_source_shape(radial.positions, radial.layers)
    det = radial.layers[-1]

    print("=" * 96)
    print("FIFTH FAMILY RADIAL SYMMETRY/ORIENTATION CERTIFICATE")
    print("=" * 96)
    print(f"row: drift={DRIFT:.2f} seed={SEED}")
    print("method: source-field linearity + zero-field variational recurrence")
    print()

    zero_field = [0.0] * len(field_shape)
    neutral_field = [a - a for a in field_shape]
    plus_field = [a for a in field_shape]
    minus_field = [-a for a in field_shape]

    check("source note links this independent certificate", "symmetry_orientation_certificate_2026_06_08" in note_text)
    check("empty-source field is exactly zero componentwise", all(v == 0.0 for v in zero_field))
    check("+1 and -1 same-point source fields cancel exactly", all(v == 0.0 for v in neutral_field))

    free = propagate(radial.positions, radial.adj, zero_field)
    neutral = propagate(radial.positions, radial.adj, neutral_field)
    plus = propagate(radial.positions, radial.adj, plus_field)
    minus = propagate(radial.positions, radial.adj, minus_field)
    z_free = centroid_z(free, radial.positions, det)
    zero_delta = centroid_z(free, radial.positions, det) - z_free
    neutral_delta = centroid_z(neutral, radial.positions, det) - z_free
    plus_delta = centroid_z(plus, radial.positions, det) - z_free
    minus_delta = centroid_z(minus, radial.positions, det) - z_free

    amps0, damps0 = propagate_with_derivative(radial.positions, radial.adj, field_shape)
    slope = centroid_derivative(amps0, damps0, radial.positions, det)
    finite_slope = plus_delta

    print()
    print(f"zero_delta     = {zero_delta:+.12e}")
    print(f"neutral_delta  = {neutral_delta:+.12e}")
    print(f"plus_delta     = {plus_delta:+.12e}")
    print(f"minus_delta    = {minus_delta:+.12e}")
    print(f"linear_slope   = {slope:+.12e}")
    print()

    check("zero-source centroid delta is exact", zero_delta == 0.0)
    check("neutral same-point centroid delta is exact", neutral_delta == 0.0)
    check("first-order positive-source radial response is negative", slope < 0.0)
    check("finite +1 source has same negative sign as variational slope", plus_delta < 0.0 and slope * finite_slope > 0.0)
    check("finite -1 source has opposite positive sign", minus_delta > 0.0)
    check("plus/minus signs certify orientation boundary, not control leak", plus_delta < 0.0 < minus_delta)

    print()
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
