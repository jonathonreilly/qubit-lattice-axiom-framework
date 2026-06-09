#!/usr/bin/env python3
"""Tiny drift basin sweep for the grown-row non-label signed-source transfer.

This script tests whether the geometry-sector / non-label connectivity idea
survives a small drift neighborhood around the retained grown row while keeping
the restore knob fixed near the promoted value.

Guard rails:
  - exact zero-source baseline
  - exact neutral +1/-1 cancellation
  - sign orientation
  - weak charge-scaling estimate

The claim surface is intentionally narrow: this is a drift-basin test, not a
family rebuild or a general transport theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import math
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

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
AUDIT_TIMEOUT_SEC = 120
REPO_ROOT = Path(__file__).resolve().parents[1]
FROZEN_LOG = REPO_ROOT / "logs" / "2026-04-06-nonlabel-grown-drift-basin-sweep.txt"
RECOMPUTE_RUNNER = REPO_ROOT / "scripts" / "nonlabel_grown_drift_basin_recompute_audit_2026_06_08.py"
RECOMPUTE_CACHE = REPO_ROOT / "logs" / "runner-cache" / "nonlabel_grown_drift_basin_recompute_audit_2026_06_08.txt"
ROW_RE = re.compile(
    r"^(?P<drift>[0-9.]+)\s+(?P<seed>[0-9]+)\s+\|\s+"
    r"(?P<zero>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"(?P<plus>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"(?P<minus>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"(?P<neutral>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"(?P<double>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"(?P<exp>[0-9.]+)\s+(?P<ok>YES|no)$",
    re.MULTILINE,
)
RECOMPUTE_ROW_RE = re.compile(
    r"^drift=(?P<drift>[0-9.]+)\s+seed=(?P<seed>[0-9]+)\s+"
    r"zero=(?P<zero>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"plus=(?P<plus>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"minus=(?P<minus>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"neutral=(?P<neutral>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"double=(?P<double>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"exp=(?P<exp>[0-9.]+)\s+(?P<status>PASS|FAIL)$",
    re.MULTILINE,
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _cache_header(cache_path: Path) -> dict[str, str]:
    header = cache_path.read_text(encoding="utf-8").split("----- stdout -----", 1)[0]
    fields: dict[str, str] = {}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


@dataclass(frozen=True)
class RowResult:
    drift: float
    seed: int
    zero: float
    plus: float
    minus: float
    neutral: float
    double: float
    exponent: float

    @property
    def signed_ok(self) -> bool:
        return (
            abs(self.zero) < 1e-12
            and abs(self.neutral) < 1e-12
            and self.plus != 0.0
            and self.minus != 0.0
            and self.plus * self.minus < 0.0
            and abs(self.exponent - 1.0) < 0.05
        )


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else math.nan


def _verify_recompute_artifact(failures: list[str]) -> None:
    if not RECOMPUTE_RUNNER.exists():
        failures.append("missing live drift recompute runner")
        return
    if not RECOMPUTE_CACHE.exists():
        failures.append("missing live drift recompute cache")
        return

    fields = _cache_header(RECOMPUTE_CACHE)
    cache_text = RECOMPUTE_CACHE.read_text(encoding="utf-8")
    rows = [
        {
            "drift": float(m.group("drift")),
            "seed": int(m.group("seed")),
            "zero": float(m.group("zero")),
            "plus": float(m.group("plus")),
            "minus": float(m.group("minus")),
            "neutral": float(m.group("neutral")),
            "double": float(m.group("double")),
            "exp": float(m.group("exp")),
            "status": m.group("status"),
        }
        for m in RECOMPUTE_ROW_RE.finditer(cache_text)
    ]

    runner_rel = RECOMPUTE_RUNNER.relative_to(REPO_ROOT).as_posix()
    sha_fresh = fields.get("runner_sha256") == _sha256(RECOMPUTE_RUNNER)
    header_ok = (
        fields.get("runner") == runner_rel
        and fields.get("status") == "ok"
        and fields.get("exit_code") == "0"
        and sha_fresh
    )
    score_ok = "SCORECARD PASS=9 FAIL=0" in cache_text
    grid_ok = [
        (round(row["drift"], 2), row["seed"])
        for row in rows
    ] == [(round(drift, 2), seed) for drift in DRIFTS for seed in SEEDS]

    row_gate_ok = True
    for row in rows:
        row_gate_ok = row_gate_ok and row["status"] == "PASS"
        row_gate_ok = row_gate_ok and abs(row["zero"]) < 1.0e-12
        row_gate_ok = row_gate_ok and abs(row["neutral"]) < 1.0e-12
        row_gate_ok = row_gate_ok and row["plus"] < 0.0 < row["minus"]
        row_gate_ok = row_gate_ok and row["double"] < 0.0
        row_gate_ok = row_gate_ok and abs(row["exp"] - 1.0) < 0.05

    print()
    print("Live drift recompute artifact")
    print(f"  runner={fields.get('runner')} status={fields.get('status')} exit={fields.get('exit_code')}")
    print(f"  runner_sha_fresh={sha_fresh} rows={len(rows)} scorecard_pass={score_ok}")
    for row in rows:
        print(
            f"  recompute drift={row['drift']:.2f} seed={row['seed']} "
            f"plus={row['plus']:+.12e} minus={row['minus']:+.12e} "
            f"double={row['double']:+.12e} exp={row['exp']:.12f} "
            f"{row['status']}"
        )

    if not header_ok:
        failures.append("live drift recompute cache header is not SHA-fresh/ok")
    if not score_ok:
        failures.append("live drift recompute cache scorecard is not PASS=9 FAIL=0")
    if not grid_ok:
        failures.append("live drift recompute grid mismatch")
    if not row_gate_ok:
        failures.append("live drift recompute row gates failed")


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


def _propagate(
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
            L = math.sqrt(dx * dx + dy * dy + dz * dz)
            if L < 1e-10:
                continue
            lf = 0.5 * (field[i] + field[j])
            act = L * (1.0 + lf)
            theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
            w = math.exp(-BETA * theta * theta)
            amps[j] += ai * complex(math.cos(K * act), math.sin(K * act)) * w * hm / (L * L)
    return amps


def _centroid_z(
    amps: list[complex],
    pos: list[tuple[float, float, float]],
    det: list[int],
) -> float:
    total = 0.0
    weighted = 0.0
    for i in det:
        p = abs(amps[i]) ** 2
        total += p
        weighted += p * pos[i][2]
    return weighted / total if total > 1e-30 else 0.0


def _build_geometry_sector_grown(pos, layers):
    """Build a position-based sector stencil from the grown row itself."""

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


def _measure_family(pos, adj, layers) -> tuple[float, float, float, float, float]:
    det = layers[-1]
    free = _propagate(pos, adj, [0.0] * len(pos))
    z_free = _centroid_z(free, pos, det)

    def run(sources: list[tuple[float, int]]) -> float:
        field = _field_from_sources(pos, layers, sources)
        amps = _propagate(pos, adj, field)
        return _centroid_z(amps, pos, det) - z_free

    zero = run([])
    plus = run([(SOURCE_Z, +1)])
    minus = run([(SOURCE_Z, -1)])
    neutral = run([(SOURCE_Z, +1), (SOURCE_Z, -1)])
    double = run([(SOURCE_Z, +2)])
    exponent = math.log(abs(double / plus)) / math.log(2.0) if abs(plus) > 1e-30 and abs(double) > 1e-30 else math.nan
    return zero, plus, minus, neutral, double, exponent


def run_full_replay() -> None:
    print("=" * 90)
    print("NON-LABEL GROWN DRIFT BASIN SWEEP")
    print("  question: does the geometry-sector idea survive a tiny drift basin around")
    print("  the retained grown-row fixed-field signed-source transfer?")
    print("=" * 90)
    print(f"h={H}, NL={NL}, drifts={DRIFTS}, restore={RESTORE}, seeds={SEEDS}")
    print()

    rows: list[RowResult] = []
    for drift in DRIFTS:
        for seed in SEEDS:
            pos, adj, layers = grow(drift, RESTORE, seed)
            sector_adj = _build_geometry_sector_grown(pos, layers)
            zero, plus, minus, neutral, double, exponent = _measure_family(pos, sector_adj, layers)
            rows.append(
                RowResult(
                    drift=drift,
                    seed=seed,
                    zero=zero,
                    plus=plus,
                    minus=minus,
                    neutral=neutral,
                    double=double,
                    exponent=exponent,
                )
            )

    print("drift seed | zero         plus         minus        neutral      double       exp    ok")
    print("-" * 88)
    for row in rows:
        print(
            f"{row.drift:>4.2f}   {row.seed:>2d}  | "
            f"{row.zero:+.3e}  {row.plus:+.3e}  {row.minus:+.3e}  "
            f"{row.neutral:+.3e}  {row.double:+.3e}  {row.exponent:>5.3f}  "
            f"{'YES' if row.signed_ok else 'no'}"
        )

    passed = [r for r in rows if r.signed_ok]
    print()
    print("SAFE READ")
    print(f"  passed rows: {len(passed)}/{len(rows)}")
    if passed:
        print("  this is a bounded positive drift basin on the retained grown family")
        print(f"  mean exponent among passes: {_mean([r.exponent for r in passed]):.6f}")
    else:
        print("  this is a clean no-go on the drift neighborhood")


def verify_frozen_log() -> int:
    text = FROZEN_LOG.read_text(encoding="utf-8")
    rows = [
        RowResult(
            drift=float(m.group("drift")),
            seed=int(m.group("seed")),
            zero=float(m.group("zero")),
            plus=float(m.group("plus")),
            minus=float(m.group("minus")),
            neutral=float(m.group("neutral")),
            double=float(m.group("double")),
            exponent=float(m.group("exp")),
        )
        for m in ROW_RE.finditer(text)
    ]

    failures: list[str] = []
    expected_pairs = [(drift, seed) for drift in DRIFTS for seed in SEEDS]
    observed_pairs = [(round(r.drift, 2), r.seed) for r in rows]
    if "NON-LABEL GROWN DRIFT BASIN SWEEP" not in text:
        failures.append("missing frozen-log title")
    if observed_pairs != [(round(d, 2), s) for d, s in expected_pairs]:
        failures.append(f"drift/seed grid mismatch: {observed_pairs}")
    summary = re.search(r"passed rows:\s*(\d+)/(\d+)", text)
    if not summary or summary.groups() != ("9", "9"):
        failures.append("safe-read pass count is not 9/9")
    mean = re.search(r"mean exponent among passes:\s*([0-9.]+)", text)
    if not mean or abs(float(mean.group(1)) - 1.0002) > 0.0005:
        failures.append("mean exponent summary is missing or outside tolerance")

    for row in rows:
        label = f"drift={row.drift:.2f} seed={row.seed}"
        if not row.signed_ok:
            failures.append(f"{label} signed/neutral/linear gate failed")
        if not (row.plus < 0.0 < row.minus and row.double < 0.0):
            failures.append(f"{label} signed orientation failed")

    print("=" * 90)
    print("NON-LABEL GROWN DRIFT BASIN FROZEN LOG VERIFIER")
    print(f"log: {FROZEN_LOG.relative_to(REPO_ROOT)}")
    print("=" * 90)
    for row in rows:
        print(
            f"drift={row.drift:.2f} seed={row.seed} "
            f"zero={row.zero:+.3e} neutral={row.neutral:+.3e} "
            f"plus={row.plus:+.3e} minus={row.minus:+.3e} "
            f"double={row.double:+.3e} exp={row.exponent:.3f} "
            f"{'PASS' if row.signed_ok else 'FAIL'}"
        )

    _verify_recompute_artifact(failures)

    print()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"SCORECARD PASS=0 FAIL={len(failures)}")
        return 1
    print("SAFE READ: bounded positive drift basin; verifier checks frozen rows and the SHA-fresh live recompute artifact.")
    print(f"SCORECARD PASS={len(rows) + 1} FAIL=0")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--recompute",
        action="store_true",
        help="Run the original live replay instead of verifying the frozen log.",
    )
    args = parser.parse_args()
    if args.recompute:
        run_full_replay()
        return 0
    return verify_frozen_log()


if __name__ == "__main__":
    raise SystemExit(main())
