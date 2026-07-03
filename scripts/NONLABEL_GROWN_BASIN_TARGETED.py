#!/usr/bin/env python3
"""Targeted basin diagnostic for the grown-row non-label signed-source transfer.

Checks the retained drift=0.2 row with nearby restore values to see whether the
geometry-sector transfer has a real local basin or only a single retained point.
"""

from __future__ import annotations

import argparse
import hashlib
import math
import os
import re
import sys
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
DRIFT = 0.20
RESTORES = [0.60, 0.70, 0.80]
SEED = 0
AUDIT_TIMEOUT_SEC = 120
REPO_ROOT = Path(__file__).resolve().parents[1]
FROZEN_LOG = REPO_ROOT / "logs" / "2026-04-06-nonlabel-grown-basin-targeted.txt"
RECOMPUTE_RUNNER = REPO_ROOT / "scripts" / "nonlabel_grown_basin_recompute_audit_2026_06_08.py"
RECOMPUTE_CACHE = REPO_ROOT / "logs" / "runner-cache" / "nonlabel_grown_basin_recompute_audit_2026_06_08.txt"
ROW_RE = re.compile(
    r"^restore=(?P<restore>[0-9.]+)\s+\|\s+"
    r"zero=(?P<zero>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"plus=(?P<plus>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"minus=(?P<minus>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"neutral=(?P<neutral>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"double=(?P<double>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"exp=\s*(?P<exp>[0-9.]+)\s+(?P<ok>YES|no)$",
    re.MULTILINE,
)
RECOMPUTE_ROW_RE = re.compile(
    r"^restore=(?P<restore>[0-9.]+)\s+"
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


def _verify_recompute_artifact(failures: list[str]) -> None:
    if not RECOMPUTE_RUNNER.exists():
        failures.append("missing live recompute runner")
        return
    if not RECOMPUTE_CACHE.exists():
        failures.append("missing live recompute cache")
        return

    fields = _cache_header(RECOMPUTE_CACHE)
    cache_text = RECOMPUTE_CACHE.read_text(encoding="utf-8")
    rows = [
        {
            "restore": float(m.group("restore")),
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
    score_ok = "SCORECARD PASS=3 FAIL=0" in cache_text
    grid_ok = [round(row["restore"], 2) for row in rows] == [round(r, 2) for r in RESTORES]
    row_gate_ok = True
    for row in rows:
        row_gate_ok = row_gate_ok and row["status"] == "PASS"
        row_gate_ok = row_gate_ok and abs(row["zero"]) < 1.0e-12
        row_gate_ok = row_gate_ok and abs(row["neutral"]) < 1.0e-12
        row_gate_ok = row_gate_ok and row["plus"] < 0.0 < row["minus"]
        row_gate_ok = row_gate_ok and row["double"] < 0.0
        row_gate_ok = row_gate_ok and abs(row["exp"] - 1.0) < 0.05

    print()
    print("Live recompute artifact")
    print(f"  runner={fields.get('runner')} status={fields.get('status')} exit={fields.get('exit_code')}")
    print(f"  runner_sha_fresh={sha_fresh} rows={len(rows)} scorecard_pass={score_ok}")
    for row in rows:
        print(
            f"  recompute restore={row['restore']:.2f} plus={row['plus']:+.12e} "
            f"minus={row['minus']:+.12e} double={row['double']:+.12e} "
            f"exp={row['exp']:.12f} {row['status']}"
        )

    if not header_ok:
        failures.append("live recompute cache header is not SHA-fresh/ok")
    if not score_ok:
        failures.append("live recompute cache scorecard is not PASS=3 FAIL=0")
    if not grid_ok:
        failures.append("live recompute restore grid mismatch")
    if not row_gate_ok:
        failures.append("live recompute row gates failed")


def _nearest_node_in_layer(pos, layer_nodes, x_target, y_target, z_target):
    best = None
    best_d = float("inf")
    for idx in layer_nodes:
        x, y, z = pos[idx]
        d = (x - x_target) ** 2 + (y - y_target) ** 2 + (z - z_target) ** 2
        if d < best_d:
            best = idx
            best_d = d
    return best


def _field_from_sources(pos, layers, sources):
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


def _propagate(pos, adj, field):
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


def _centroid_z(amps, pos, det):
    total = 0.0
    weighted = 0.0
    for i in det:
        p = abs(amps[i]) ** 2
        total += p
        weighted += p * pos[i][2]
    return weighted / total if total > 1e-30 else 0.0


def _build_geometry_sector_grown(pos, layers):
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


def _measure(pos, adj, layers):
    det = layers[-1]
    free = _propagate(pos, adj, [0.0] * len(pos))
    z_free = _centroid_z(free, pos, det)

    def run(sources):
        field = _field_from_sources(pos, layers, sources)
        amps = _propagate(pos, adj, field)
        return _centroid_z(amps, pos, det) - z_free

    zero = run([])
    plus = run([(SOURCE_Z, +1)])
    minus = run([(SOURCE_Z, -1)])
    neutral = run([(SOURCE_Z, +1), (SOURCE_Z, -1)])
    double = run([(SOURCE_Z, +2)])
    exponent = math.log(abs(double / plus)) / math.log(2.0) if abs(plus) > 1e-30 and abs(double) > 1e-30 else math.nan
    ok = (
        abs(zero) < 1e-12
        and abs(neutral) < 1e-12
        and plus != 0.0
        and minus != 0.0
        and plus * minus < 0.0
        and abs(exponent - 1.0) < 0.05
    )
    return zero, plus, minus, neutral, double, exponent, ok


def run_full_replay() -> None:
    print("=" * 90)
    print("NON-LABEL GROWN BASIN TARGETED")
    print(f"  drift={DRIFT}, restore values={RESTORES}, seed={SEED}")
    print("=" * 90)
    passed = 0
    for restore in RESTORES:
        pos, adj, layers = grow(DRIFT, restore, SEED)
        sector_adj = _build_geometry_sector_grown(pos, layers)
        zero, plus, minus, neutral, double, exponent, ok = _measure(pos, sector_adj, layers)
        passed += int(ok)
        print(
            f"restore={restore:.2f} | zero={zero:+.3e} plus={plus:+.3e} "
            f"minus={minus:+.3e} neutral={neutral:+.3e} double={double:+.3e} "
            f"exp={exponent:>5.3f} {'YES' if ok else 'no'}"
        )
    print()
    print("SAFE READ")
    print(f"  passed rows: {passed}/{len(RESTORES)}")
    if passed:
        print("  this is a bounded positive basin around the retained row")
    else:
        print("  this is a clean no-go at the nearest restore neighborhood")


def verify_frozen_log() -> int:
    text = FROZEN_LOG.read_text(encoding="utf-8")
    rows = [
        {
            "restore": float(m.group("restore")),
            "zero": float(m.group("zero")),
            "plus": float(m.group("plus")),
            "minus": float(m.group("minus")),
            "neutral": float(m.group("neutral")),
            "double": float(m.group("double")),
            "exp": float(m.group("exp")),
            "ok": m.group("ok") == "YES",
        }
        for m in ROW_RE.finditer(text)
    ]

    failures: list[str] = []
    if "NON-LABEL GROWN BASIN TARGETED" not in text:
        failures.append("missing frozen-log title")
    if len(rows) != len(RESTORES):
        failures.append(f"expected {len(RESTORES)} rows, found {len(rows)}")
    restores = [round(r["restore"], 2) for r in rows]
    if restores != [round(r, 2) for r in RESTORES]:
        failures.append(f"restore grid mismatch: {restores}")
    summary = re.search(r"passed rows:\s*(\d+)/(\d+)", text)
    if not summary or summary.groups() != ("3", "3"):
        failures.append("safe-read pass count is not 3/3")

    for row in rows:
        restore = row["restore"]
        if not row["ok"]:
            failures.append(f"restore={restore:.2f} is not marked YES")
        if abs(row["zero"]) > 1e-12:
            failures.append(f"restore={restore:.2f} zero gate failed: {row['zero']:+.3e}")
        if abs(row["neutral"]) > 1e-12:
            failures.append(f"restore={restore:.2f} neutral gate failed: {row['neutral']:+.3e}")
        if not (row["plus"] < 0.0 < row["minus"]):
            failures.append(f"restore={restore:.2f} signed orientation failed")
        if row["double"] >= 0.0:
            failures.append(f"restore={restore:.2f} double-source sign failed")
        if abs(row["exp"] - 1.0) > 0.002:
            failures.append(f"restore={restore:.2f} exponent not linear: {row['exp']:.6f}")

    print("=" * 90)
    print("NON-LABEL GROWN BASIN TARGETED FROZEN LOG VERIFIER")
    print(f"log: {FROZEN_LOG.relative_to(REPO_ROOT)}")
    print("=" * 90)
    for row in rows:
        print(
            f"restore={row['restore']:.2f} zero={row['zero']:+.3e} "
            f"neutral={row['neutral']:+.3e} plus={row['plus']:+.3e} "
            f"minus={row['minus']:+.3e} double={row['double']:+.3e} "
            f"exp={row['exp']:.3f} {'PASS' if row['ok'] else 'FAIL'}"
        )

    _verify_recompute_artifact(failures)

    print()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"SCORECARD PASS=0 FAIL={len(failures)}")
        return 1
    print("SAFE READ: bounded positive restore basin; verifier checks frozen rows and the SHA-fresh live recompute artifact.")
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
