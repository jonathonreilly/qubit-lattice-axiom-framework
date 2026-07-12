#!/usr/bin/env python3
"""Snapshot-identifiability no-go for the discrete Shapiro proxy lane.

Question
--------
Can detector-line phase identify a causal history when the propagation kernel
receives only one node-wise field snapshot?

This runner proves the exact implementation-level witness and evaluates one
bounded finite control on three configured grown geometry families:

1. c-indexed cone snapshot (a position-only field; no causal evolution)
2. exact equal-array witness with the same node values
3. fixed-layer scheduling proxy on delays d = 0, 1, 2, 3

The exact no-go is independent of the numeric sweep: a deterministic function
of one field array cannot distinguish two history labels attached to equal
arrays.  The scheduling rows are a bounded finite control, not a universal
exclusion of static schedules and not a physical propagation-delay model.
"""

from __future__ import annotations


# Heavy compute / sweep runner — `AUDIT_TIMEOUT_SEC = 1800`
# means the audit-lane precompute and live audit runner allow up to
# 30 min of wall time before recording a timeout. The 120 s default
# ceiling is too tight under concurrency contention; see
# `docs/audit/RUNNER_CACHE_POLICY.md`.
AUDIT_TIMEOUT_SEC = 1800

import cmath
import math
import random
import statistics
from dataclasses import dataclass


BETA = 0.8
K = 5.0
H = 0.5
NL = 30
PW = 8
MAX_D_PHYS = 3
MASS_Z = 3.0
FIELD_STRENGTH = 0.004
SOURCE_LAYER = NL // 3
SEEDS = [0, 1]
FAMILIES = [
    ("Fam1", 0.20, 0.70),
    ("Fam2", 0.05, 0.30),
    ("Fam3", 0.50, 0.90),
]

# Cone-shape index values.  These are not interpreted as physical speeds.
C_VALUES = [2.0, 1.0, 0.5, 0.25]

# Static lookalikes.
STATIC_CONE_VALUES = [2.0, 1.0, 0.5, 0.25]
STATIC_DELAY_VALUES = [0, 1, 2, 3]
SCHEDULE_NEAR_FLAT_TOL = 1e-3
SNAPSHOT_SCHEDULE_SPAN_GAP_MIN = 2e-2


@dataclass(frozen=True)
class Family:
    label: str
    drift: float
    restore: float


@dataclass(frozen=True)
class Row:
    key: str
    values: dict[str, float]
    spread: float


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else math.nan


def _se(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    return statistics.pstdev(values) / math.sqrt(len(values))


def _wrap_phase(delta: float) -> float:
    return (delta + math.pi) % (2 * math.pi) - math.pi


def grow(seed: int, drift: float, restore: float):
    rng = random.Random(seed)
    hw = int(PW / H)
    md = max(1, round(MAX_D_PHYS / H))
    pos: list[tuple[float, float, float]] = []
    adj: dict[int, list[int]] = {}
    nmap: dict[tuple[int, int, int], int] = {}
    pos.append((0.0, 0.0, 0.0))
    nmap[(0, 0, 0)] = 0

    for layer in range(1, NL):
        x = layer * H
        for iy in range(-hw, hw + 1):
            for iz in range(-hw, hw + 1):
                if layer == 1:
                    y, z = iy * H, iz * H
                else:
                    prev = nmap.get((layer - 1, iy, iz))
                    if prev is None:
                        continue
                    _, py, pz = pos[prev]
                    y = py + rng.gauss(0, drift * H)
                    z = pz + rng.gauss(0, drift * H)
                    y = y * (1 - restore) + (iy * H) * restore
                    z = z * (1 - restore) + (iz * H) * restore
                idx = len(pos)
                pos.append((x, y, z))
                nmap[(layer, iy, iz)] = idx
        for iy in range(-hw, hw + 1):
            for iz in range(-hw, hw + 1):
                si = nmap.get((layer - 1, iy, iz))
                if si is None:
                    continue
                for dy in range(-md, md + 1):
                    for dz in range(-md, md + 1):
                        di = nmap.get((layer, iy + dy, iz + dz))
                        if di is not None:
                            adj.setdefault(si, []).append(di)
    return pos, adj, nmap


def _select_source_node(
    pos: list[tuple[float, float, float]],
    nmap: dict[tuple[int, int, int], int],
    target_z: float,
) -> int:
    gl = NL // 3
    iz_s = round(target_z / H)
    mi = nmap.get((gl, 0, iz_s))
    if mi is None:
        raise ValueError("source node lookup failed")
    return mi


def _detector_extent(
    pos: list[tuple[float, float, float]],
    det_nodes: list[int],
    anchor: tuple[float, float, float],
) -> float:
    _, sy, sz = anchor
    return max(
        math.sqrt((pos[idx][1] - sy) ** 2 + (pos[idx][2] - sz) ** 2)
        for idx in det_nodes
    )


def _topo_order(adj: dict[int, list[int]], n: int) -> list[int]:
    indeg = [0] * n
    for nbs in adj.values():
        for j in nbs:
            indeg[j] += 1
    q = [i for i in range(n) if indeg[i] == 0]
    order: list[int] = []
    while q:
        i = q.pop(0)
        order.append(i)
        for j in adj.get(i, []):
            indeg[j] -= 1
            if indeg[j] == 0:
                q.append(j)
    return order


def _propagate(
    pos: list[tuple[float, float, float]],
    adj: dict[int, list[int]],
    field: list[float],
    src: list[int],
) -> list[complex]:
    n = len(pos)
    order = _topo_order(adj, n)
    amps = [0j] * n
    for s in src:
        amps[s] = 1.0 / len(src)
    h2 = H * H
    for i in order:
        if abs(amps[i]) < 1e-30:
            continue
        for j in adj.get(i, []):
            dx = pos[j][0] - pos[i][0]
            dy = pos[j][1] - pos[i][1]
            dz = pos[j][2] - pos[i][2]
            L = math.sqrt(dx * dx + dy * dy + dz * dz)
            if L < 1e-10:
                continue
            theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
            w = math.exp(-BETA * theta * theta)
            lf = 0.5 * (field[i] + field[j])
            act = L * (1.0 - lf)
            amps[j] += amps[i] * complex(math.cos(K * act), math.sin(K * act)) * w * h2 / (L * L)
    return amps


def _centroid_z(
    amps: list[complex],
    pos: list[tuple[float, float, float]],
    det_nodes: list[int],
) -> float:
    total = 0.0
    weighted = 0.0
    for i in det_nodes:
        p = abs(amps[i]) ** 2
        total += p
        weighted += p * pos[i][2]
    return weighted / total if total > 1e-30 else 0.0


def _instantaneous_field(
    pos: list[tuple[float, float, float]],
    anchor: tuple[float, float, float],
    strength: float,
) -> list[float]:
    if strength == 0.0:
        return [0.0] * len(pos)
    sx, sy, sz = anchor
    field = [0.0] * len(pos)
    for idx, (x, y, z) in enumerate(pos):
        r = math.sqrt((x - sx) ** 2 + (y - sy) ** 2 + (z - sz) ** 2) + 0.1
        field[idx] = strength / r
    return field


def _cone_snapshot_field(
    pos: list[tuple[float, float, float]],
    nmap: dict[tuple[int, int, int], int],
    anchor: tuple[float, float, float],
    strength: float,
    cone_index: float,
) -> list[float]:
    """Position-only cone snapshot; contains no time evolution or history."""
    if strength == 0.0:
        return [0.0] * len(pos)
    sx, sy, sz = anchor
    det_nodes = [i for i, p in enumerate(pos) if p[0] == pos[-1][0]]
    det_radius = _detector_extent(pos, det_nodes, anchor)
    x_src = pos[_select_source_node(pos, nmap, MASS_Z)][0]
    x_span = max(pos[det_nodes[0]][0] - sx, 1e-12)
    field = [0.0] * len(pos)
    for idx, (x, y, z) in enumerate(pos):
        dx = x - sx
        if dx < -1e-12:
            continue
        transverse = math.sqrt((y - sy) ** 2 + (z - sz) ** 2)
        cone_radius = cone_index * det_radius * max(dx, 0.0) / x_span
        if transverse > cone_radius + 1e-12:
            continue
        r = math.sqrt(dx * dx + (y - sy) ** 2 + (z - sz) ** 2) + 0.1
        field[idx] = strength / r
    return field


def _equal_array_witness(snapshot: list[float]) -> list[float]:
    """Exact duplicate on the runner's unconstrained field-array input class."""
    return list(snapshot)


def _static_schedule_field(
    pos: list[tuple[float, float, float]],
    nmap: dict[tuple[int, int, int], int],
    anchor: tuple[float, float, float],
    strength: float,
    delay_layers: int,
    cone_c: float = 1.0,
) -> list[float]:
    """Frozen schedule: same cone shape, but a fixed layer delay."""
    if strength == 0.0:
        return [0.0] * len(pos)
    sx, sy, sz = anchor
    det_nodes = [i for i, p in enumerate(pos) if p[0] == pos[-1][0]]
    det_radius = _detector_extent(pos, det_nodes, anchor)
    x_span = max(pos[det_nodes[0]][0] - sx, 1e-12)
    field = [0.0] * len(pos)
    for idx, (x, y, z) in enumerate(pos):
        layer = round(x / H)
        if layer < SOURCE_LAYER + delay_layers:
            continue
        dx = x - sx
        if dx < -1e-12:
            continue
        transverse = math.sqrt((y - sy) ** 2 + (z - sz) ** 2)
        cone_radius = cone_c * det_radius * max(dx, 0.0) / x_span
        if transverse > cone_radius + 1e-12:
            continue
        r = math.sqrt(dx * dx + (y - sy) ** 2 + (z - sz) ** 2) + 0.1
        field[idx] = strength / r
    return field


def _phase_lag(
    pos: list[tuple[float, float, float]],
    adj: dict[int, list[int]],
    nmap: dict[tuple[int, int, int], int],
    anchor: tuple[float, float, float],
    mode: str,
    param: float,
    strength: float = FIELD_STRENGTH,
) -> float:
    det_nodes = [i for i, p in enumerate(pos) if p[0] == pos[-1][0]]
    src = [i for i, p in enumerate(pos) if p[0] == 0.0]
    inst_field = _instantaneous_field(pos, anchor, strength)
    psi_inst = _propagate(pos, adj, inst_field, src)
    det_inst = [psi_inst[i] for i in det_nodes]
    n_inst = math.sqrt(sum(abs(a) ** 2 for a in det_inst))

    if mode == "cone_snapshot":
        field = _cone_snapshot_field(pos, nmap, anchor, strength, param)
    elif mode == "static_cone":
        field = _equal_array_witness(
            _cone_snapshot_field(pos, nmap, anchor, strength, param)
        )
    elif mode == "static_schedule":
        field = _static_schedule_field(pos, nmap, anchor, strength, int(param))
    else:
        raise ValueError(mode)

    psi = _propagate(pos, adj, field, src)
    det = [psi[i] for i in det_nodes]
    n_test = math.sqrt(sum(abs(a) ** 2 for a in det))
    if n_inst <= 1e-30 or n_test <= 1e-30:
        return 0.0
    overlap = sum(a.conjugate() / n_inst * b / n_test for a, b in zip(det_inst, det))
    return _wrap_phase(cmath.phase(overlap))


def _phase_lag_against_baseline(
    pos: list[tuple[float, float, float]],
    adj: dict[int, list[int]],
    psi_inst: list[complex],
    det_nodes: list[int],
    field: list[float],
) -> float:
    det_inst = [psi_inst[i] for i in det_nodes]
    n_inst = math.sqrt(sum(abs(a) ** 2 for a in det_inst))
    psi = _propagate(pos, adj, field, [i for i, p in enumerate(pos) if p[0] == 0.0])
    det = [psi[i] for i in det_nodes]
    n_test = math.sqrt(sum(abs(a) ** 2 for a in det))
    if n_inst <= 1e-30 or n_test <= 1e-30:
        return 0.0
    overlap = sum(a.conjugate() / n_inst * b / n_test for a, b in zip(det_inst, det))
    return _wrap_phase(cmath.phase(overlap))


def _family_rows() -> list[Family]:
    return [Family(*row) for row in FAMILIES]


def _self_overlap_phase(
    state: list[complex],
    det_nodes: list[int],
) -> float:
    det = [state[i] for i in det_nodes]
    norm = math.sqrt(sum(abs(a) ** 2 for a in det))
    if norm <= 1e-30:
        return 0.0
    overlap = sum(a.conjugate() / norm * a / norm for a in det)
    return _wrap_phase(cmath.phase(overlap))


def _sweep_family(family: Family) -> tuple[dict[str, list[float]], float, float, int]:
    per_mode: dict[str, list[float]] = {
        "cone-snapshot:2.0": [],
        "cone-snapshot:1.0": [],
        "cone-snapshot:0.5": [],
        "cone-snapshot:0.25": [],
        "equal-array-witness:2.0": [],
        "equal-array-witness:1.0": [],
        "equal-array-witness:0.5": [],
        "equal-array-witness:0.25": [],
        "static-schedule:0": [],
        "static-schedule:1": [],
        "static-schedule:2": [],
        "static-schedule:3": [],
    }
    zero_ok = 0.0
    witness_max_node_delta = 0.0
    witness_rows = 0

    for seed in SEEDS:
        pos, adj, nmap = grow(seed, family.drift, family.restore)
        source_idx = _select_source_node(pos, nmap, MASS_Z)
        anchor = pos[source_idx]
        det_nodes = [i for i, p in enumerate(pos) if p[0] == pos[-1][0]]
        src = [i for i, p in enumerate(pos) if p[0] == 0.0]
        inst_field = _instantaneous_field(pos, anchor, FIELD_STRENGTH)
        psi_inst = _propagate(pos, adj, inst_field, src)

        # Exact self-overlap control uses the actual computed baseline state.
        zero_ok = max(zero_ok, abs(_self_overlap_phase(psi_inst, det_nodes)))

        for c in C_VALUES:
            key = str(c)
            snapshot_field = _cone_snapshot_field(
                pos, nmap, anchor, FIELD_STRENGTH, c
            )
            static_witness = _equal_array_witness(snapshot_field)
            witness_max_node_delta = max(
                witness_max_node_delta,
                max(abs(a - b) for a, b in zip(snapshot_field, static_witness)),
            )
            witness_rows += 1
            phase = _phase_lag_against_baseline(
                pos, adj, psi_inst, det_nodes, snapshot_field
            )
            per_mode[f"cone-snapshot:{key}"].append(phase)
            # Exact theorem specialization: equal arrays enter the same
            # deterministic kernel, so a second expensive propagation would
            # be an implementation duplicate rather than an independent test.
            per_mode[f"equal-array-witness:{key}"].append(phase)
        for delay in STATIC_DELAY_VALUES:
            static_schedule_field = _static_schedule_field(
                pos, nmap, anchor, FIELD_STRENGTH, int(delay)
            )
            per_mode[f"static-schedule:{delay}"].append(
                _phase_lag_against_baseline(pos, adj, psi_inst, det_nodes, static_schedule_field)
            )

    return per_mode, zero_ok, witness_max_node_delta, witness_rows


def main() -> int:
    print("=" * 88)
    print("SHAPIRO SNAPSHOT-IDENTIFIABILITY NO-GO")
    print("  exact equal-array witness + bounded fixed-layer scheduling control")
    print("=" * 88)
    print()
    print(f"families={len(FAMILIES)} seeds={len(SEEDS)} c-values={C_VALUES}")
    print(f"static cone candidates={STATIC_CONE_VALUES}")
    print(f"static schedule delays={STATIC_DELAY_VALUES}")
    print()

    family_rows = []
    candidate_equal_array: dict[str, list[float]] = {
        f"equal-array-witness:{str(c)}": [] for c in STATIC_CONE_VALUES
    }
    candidate_static_schedule: dict[str, list[float]] = {
        f"static-schedule:{d}": [] for d in STATIC_DELAY_VALUES
    }
    snapshot_means: dict[str, list[float]] = {
        f"cone-snapshot:{str(c)}": [] for c in C_VALUES
    }
    witness_max_node_delta = 0.0
    witness_rows = 0

    for family in _family_rows():
        per_mode, zero_ok, family_witness_delta, family_witness_rows = _sweep_family(family)
        family_rows.append((family.label, zero_ok, per_mode))
        witness_max_node_delta = max(witness_max_node_delta, family_witness_delta)
        witness_rows += family_witness_rows
        for key in snapshot_means:
            snapshot_means[key].append(_mean(per_mode[key]))
        for key in candidate_equal_array:
            candidate_equal_array[key].append(_mean(per_mode[key]))
        for key in candidate_static_schedule:
            candidate_static_schedule[key].append(_mean(per_mode[key]))

    # Position-only cone-snapshot curve
    print("C-INDEXED CONE-SNAPSHOT PHASE CURVE")
    print(f"{'family':>20s} {'zero':>10s} {'c=2.0':>10s} {'c=1.0':>10s} {'c=0.5':>10s} {'c=0.25':>10s}")
    print("-" * 72)
    for label, zero_ok, per_mode in family_rows:
        print(
            f"{label:>20s} {zero_ok:+10.3e} "
            f"{_mean(per_mode['cone-snapshot:2.0']):+10.4f} {_mean(per_mode['cone-snapshot:1.0']):+10.4f} "
            f"{_mean(per_mode['cone-snapshot:0.5']):+10.4f} {_mean(per_mode['cone-snapshot:0.25']):+10.4f}"
        )
    print()

    # Static cone shape family
    print("EXACT EQUAL-ARRAY-WITNESS FAMILY")
    print(f"{'family':>20s} {'cone=2.0':>10s} {'cone=1.0':>10s} {'cone=0.5':>10s} {'cone=0.25':>10s}")
    print("-" * 72)
    for label, _, per_mode in family_rows:
        print(
            f"{label:>20s} "
            f"{_mean(per_mode['equal-array-witness:2.0']):+10.4f} {_mean(per_mode['equal-array-witness:1.0']):+10.4f} "
            f"{_mean(per_mode['equal-array-witness:0.5']):+10.4f} {_mean(per_mode['equal-array-witness:0.25']):+10.4f}"
        )
    print()

    # Static scheduling family
    print("STATIC SCHEDULE FAMILY")
    print(f"{'family':>20s} {'d=0':>10s} {'d=1':>10s} {'d=2':>10s} {'d=3':>10s}")
    print("-" * 72)
    for label, _, per_mode in family_rows:
        print(
            f"{label:>20s} "
            f"{_mean(per_mode['static-schedule:0']):+10.4f} {_mean(per_mode['static-schedule:1']):+10.4f} "
            f"{_mean(per_mode['static-schedule:2']):+10.4f} {_mean(per_mode['static-schedule:3']):+10.4f}"
        )
    print()

    snapshot_curve = [
        _mean(snapshot_means[f"cone-snapshot:{str(c)}"]) for c in C_VALUES
    ]
    equal_array_curve = [
        _mean(candidate_equal_array[f"equal-array-witness:{str(c)}"])
        for c in STATIC_CONE_VALUES
    ]
    static_sched_curve = [
        _mean(candidate_static_schedule[f"static-schedule:{d}"]) for d in STATIC_DELAY_VALUES
    ]
    schedule_span = max(static_sched_curve) - min(static_sched_curve)
    snapshot_span = max(snapshot_curve) - min(snapshot_curve)
    span_gap = snapshot_span - schedule_span
    expected_witness_rows = len(FAMILIES) * len(SEEDS) * len(C_VALUES)

    checks = [
        (f"all {expected_witness_rows} configured cone snapshots have exact equal-array witnesses", witness_rows == expected_witness_rows),
        ("maximum snapshot/witness node delta is exactly zero", witness_max_node_delta == 0.0),
        ("all baseline self-overlap phases are zero within 1e-15 rad", max(row[1] for row in family_rows) < 1e-15),
        ("snapshot and equal-array-witness curves are exactly equal", snapshot_curve == equal_array_curve),
        (f"configured fixed-layer proxy span is below operational tolerance {SCHEDULE_NEAR_FLAT_TOL:.0e} rad", schedule_span < SCHEDULE_NEAR_FLAT_TOL),
        (f"snapshot/fixed-layer span gap exceeds {SNAPSHOT_SCHEDULE_SPAN_GAP_MIN:.0e} rad", span_gap > SNAPSHOT_SCHEDULE_SPAN_GAP_MIN),
    ]
    assertions_ok = all(flag for _label, flag in checks)

    print("CERTIFICATE")
    print(f"  cone snapshot mean curve: {', '.join(f'{v:+.4f}' for v in snapshot_curve)}")
    print(f"  equal-array witness curve: {', '.join(f'{v:+.4f}' for v in equal_array_curve)}")
    print(f"  fixed-layer proxy curve: {', '.join(f'{v:+.4f}' for v in static_sched_curve)}")
    print("  equal-array witness equality: exact by definition on the input class")
    print(f"  cone snapshot span: {snapshot_span:.6f} rad")
    print(f"  fixed-layer proxy span: {schedule_span:.6f} rad")
    print(f"  snapshot/fixed-layer span gap: {span_gap:.6f} rad")
    print(f"  snapshot/witness max node delta: {witness_max_node_delta:.3e}")
    print()
    print("ASSERTIVE CHECKS")
    for label, flag in checks:
        print(f"  [{'PASS' if flag else 'FAIL'}] {label}")
    print()
    print("SAFE READ")
    print("  - The runner contains no causal time evolution; c indexes a spatial cone snapshot.")
    print("  - Any supplied snapshot has an exact equal-array witness on the unconstrained field-array input surface.")
    print("  - Detector-line phase therefore cannot identify a history label absent from this interface.")
    print("  - The four configured fixed-layer proxies stay near-flat and separated.")
    print("  - No physical static-solution, universal schedule, or history-sensitive-observable claim is made.")
    print()
    print(f"ASSERTIONS: {'PASS' if assertions_ok else 'FAIL'}")
    return 0 if assertions_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
