#!/usr/bin/env python3
"""Live recompute audit artifact for the non-label grown drift-basin row.

This runner intentionally does not read the frozen log. It reruns the
geometry-sector grown-row measurement for the nine drift/seed rows named in
``docs/NONLABEL_GROWN_DRIFT_BASIN_NOTE.md`` and checks the same row gates used
by the frozen verifier.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.gate_b_grown_joint_package import grow


H = 0.5
K = 5.0
BETA = 0.8
NL = 25
SOURCE_Z = 3.0
SOURCE_STRENGTH = 5e-5
FIELD_POWER = 1
MIN_EDGES = 5

DRIFTS = [0.15, 0.20, 0.25]
RESTORE = 0.70
SEEDS = [0, 1, 2]
AUDIT_TIMEOUT_SEC = 420


@dataclass(frozen=True)
class Row:
    drift: float
    seed: int
    zero: float
    plus: float
    minus: float
    neutral: float
    double: float
    exponent: float

    @property
    def ok(self) -> bool:
        return (
            abs(self.zero) < 1e-12
            and abs(self.neutral) < 1e-12
            and self.plus != 0.0
            and self.minus != 0.0
            and self.plus * self.minus < 0.0
            and self.double < 0.0
            and abs(self.exponent - 1.0) < 0.05
        )


def nearest_node_in_layer(
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


def field_from_sources(
    pos: list[tuple[float, float, float]],
    layers: list[list[int]],
    sources: list[tuple[float, int]],
) -> list[float]:
    field = [0.0] * len(pos)
    source_layer = NL // 3
    x_target = source_layer * H
    for z_phys, charge in sources:
        node = nearest_node_in_layer(pos, layers[source_layer], x_target, 0.0, z_phys)
        if node is None:
            continue
        mx, my, mz = pos[node]
        for i, (x, y, z) in enumerate(pos):
            r = math.sqrt((x - mx) ** 2 + (y - my) ** 2 + (z - mz) ** 2) + 0.1
            field[i] += charge * SOURCE_STRENGTH / (r**FIELD_POWER)
    return field


def propagate(
    pos: list[tuple[float, float, float]],
    adj: dict[int, list[int]],
    field: list[float],
) -> list[complex]:
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
            length = math.sqrt(dx * dx + dy * dy + dz * dz)
            if length < 1e-10:
                continue
            local_field = 0.5 * (field[i] + field[j])
            action = length * (1.0 + local_field)
            theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
            weight = math.exp(-BETA * theta * theta)
            amps[j] += (
                ai
                * complex(math.cos(K * action), math.sin(K * action))
                * weight
                * hm
                / (length * length)
            )
    return amps


def centroid_z(
    amps: list[complex],
    pos: list[tuple[float, float, float]],
    detector: list[int],
) -> float:
    total = 0.0
    weighted = 0.0
    for i in detector:
        p = abs(amps[i]) ** 2
        total += p
        weighted += p * pos[i][2]
    return weighted / total if total > 1e-30 else 0.0


def build_geometry_sector_grown(
    pos: list[tuple[float, float, float]],
    layers: list[list[int]],
) -> dict[int, list[int]]:
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
    return adj


def measure_row(drift: float, seed: int) -> Row:
    pos, _adj, layers = grow(drift, RESTORE, seed)
    sector_adj = build_geometry_sector_grown(pos, layers)
    detector = layers[-1]
    free = propagate(pos, sector_adj, [0.0] * len(pos))
    z_free = centroid_z(free, pos, detector)

    def run(sources: list[tuple[float, int]]) -> float:
        field = field_from_sources(pos, layers, sources)
        amps = propagate(pos, sector_adj, field)
        return centroid_z(amps, pos, detector) - z_free

    zero = run([])
    plus = run([(SOURCE_Z, +1)])
    minus = run([(SOURCE_Z, -1)])
    neutral = run([(SOURCE_Z, +1), (SOURCE_Z, -1)])
    double = run([(SOURCE_Z, +2)])
    exponent = (
        math.log(abs(double / plus)) / math.log(2.0)
        if abs(plus) > 1e-30 and abs(double) > 1e-30
        else math.nan
    )
    return Row(
        drift=drift,
        seed=seed,
        zero=zero,
        plus=plus,
        minus=minus,
        neutral=neutral,
        double=double,
        exponent=exponent,
    )


def main() -> int:
    rows = [measure_row(drift, seed) for drift in DRIFTS for seed in SEEDS]
    failures: list[str] = []

    print("=" * 90)
    print("NON-LABEL GROWN DRIFT BASIN LIVE RECOMPUTE AUDIT")
    print(
        f"drifts={DRIFTS} restore={RESTORE:.2f} seeds={SEEDS} "
        f"NL={NL} source_strength={SOURCE_STRENGTH:.1e}"
    )
    print("=" * 90)
    for row in rows:
        print(
            f"drift={row.drift:.2f} seed={row.seed} "
            f"zero={row.zero:+.12e} "
            f"plus={row.plus:+.12e} "
            f"minus={row.minus:+.12e} "
            f"neutral={row.neutral:+.12e} "
            f"double={row.double:+.12e} "
            f"exp={row.exponent:.12f} "
            f"{'PASS' if row.ok else 'FAIL'}"
        )

        label = f"drift={row.drift:.2f} seed={row.seed}"
        if abs(row.zero) > 1e-12:
            failures.append(f"{label} zero-source gate failed")
        if abs(row.neutral) > 1e-12:
            failures.append(f"{label} neutral-pair gate failed")
        if not (row.plus < 0.0 < row.minus):
            failures.append(f"{label} sign orientation failed")
        if row.double >= 0.0:
            failures.append(f"{label} double-charge sign failed")
        if abs(row.exponent - 1.0) > 0.05:
            failures.append(f"{label} charge exponent outside basin tolerance")

    print()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"SCORECARD PASS=0 FAIL={len(failures)}")
        return 1

    print("SAFE READ: live recompute confirms the nine-row bounded drift-basin gates.")
    print(f"SCORECARD PASS={len(rows)} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
