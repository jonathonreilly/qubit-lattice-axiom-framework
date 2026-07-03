#!/usr/bin/env python3
"""Seventh-family signed-source sweep for a diagonal-stripe connectivity rule.

This is intentionally non-shell:
- not radial
- not quadrant-based
- not elliptical-shell based
- not the earlier sector-transition families

The connectivity rule partitions each layer into diagonal stripes in the y/z
plane, with the stripe axis alternating by layer parity.  That makes it a
genuinely different structured family candidate while still remaining sparse
and reviewable.

Guard rails:
- exact zero-source baseline
- exact neutral +1/-1 cancellation
- sign orientation
- weak charge-scaling estimate

The claim surface stays narrow:
- this is a seventh-family scout, not a geometry-generic theorem
- if it fails, the structural miss should be diagnosed instead of softened
"""

from __future__ import annotations

import argparse
import math
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from gate_b_no_restore_farfield import grow


H = 0.5
NL = 25
SOURCE_Z = 3.0
SOURCE_STRENGTH = 5e-5
FIELD_POWER = 1
K = 5.0
BETA = 0.8
MIN_EDGES = 5
STRIPE_COUNT = 9
DRIFTS = [0.0, 0.05, 0.10, 0.20, 0.30, 0.50]
SEEDS = [0, 1, 2]
AUDIT_TIMEOUT_SEC = 120
REPO_ROOT = Path(__file__).resolve().parents[1]
FROZEN_LOG = REPO_ROOT / "logs" / "2026-04-06-seventh-family-diagonal-sweep-boundary.txt"
ROW_RE = re.compile(
    r"^(?P<drift>[0-9.]+)\s+(?P<seed>[0-9]+)\s+"
    r"(?P<zero>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"(?P<plus>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"(?P<minus>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"(?P<neutral>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"(?P<double>[+-][0-9.]+e[+-][0-9]+)\s+"
    r"(?P<exp>[0-9.]+)\s+(?P<ok>YES|no)$",
    re.MULTILINE,
)


@dataclass(frozen=True)
class Family:
    positions: list[tuple[float, float, float]]
    layers: list[list[int]]
    adj: dict[int, list[int]]


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
    def ok(self) -> bool:
        zero_gate = abs(self.zero) < 1e-12
        neutral_gate = abs(self.neutral) < 1e-12
        sign_gate = self.plus > 0.0 and self.minus < 0.0 and self.plus * self.minus < 0.0
        fm_gate = abs(self.exponent - 1.0) < 0.05
        return zero_gate and neutral_gate and sign_gate and fm_gate


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else math.nan


def _layer_centers(
    pos: list[tuple[float, float, float]],
    layers: list[list[int]],
) -> list[tuple[float, float]]:
    centers = []
    for layer in layers:
        ys = [pos[i][1] for i in layer]
        zs = [pos[i][2] for i in layer]
        centers.append((sum(ys) / len(ys), sum(zs) / len(zs)))
    return centers


def _diag_coord(y: float, z: float, cy: float, cz: float, layer_idx: int) -> float:
    dy = y - cy
    dz = z - cz
    if layer_idx % 2 == 0:
        return dy + dz
    return dy - dz


def _stripe_index(value: float, lo: float, hi: float) -> int:
    width = max((hi - lo) / max(STRIPE_COUNT - 1, 1), H)
    stripe = int(round((value - lo) / width))
    return max(0, min(STRIPE_COUNT - 1, stripe))


def _neighbor_stripe(stripe: int, layer_idx: int) -> int:
    if layer_idx % 2 == 0:
        return min(STRIPE_COUNT - 1, stripe + 1)
    return max(0, stripe - 1)


def _build_diagonal_stripe_connectivity(fam: Family) -> Family:
    """Build a parity-alternating diagonal-stripe connectivity family."""

    pos = fam.positions
    layers = fam.layers
    centers = _layer_centers(pos, layers)
    adj: dict[int, list[int]] = {i: [] for i in range(len(pos))}

    for layer_idx in range(len(layers) - 1):
        src_layer = layers[layer_idx]
        dst_layer = layers[layer_idx + 1]
        cy_src, cz_src = centers[layer_idx]
        cy_dst, cz_dst = centers[layer_idx + 1]

        src_vals = [
            _diag_coord(pos[idx][1], pos[idx][2], cy_src, cz_src, layer_idx)
            for idx in src_layer
        ]
        dst_vals = [
            _diag_coord(pos[idx][1], pos[idx][2], cy_dst, cz_dst, layer_idx + 1)
            for idx in dst_layer
        ]
        src_lo, src_hi = min(src_vals), max(src_vals)
        dst_lo, dst_hi = min(dst_vals), max(dst_vals)

        dst_by_stripe: dict[int, list[int]] = {s: [] for s in range(STRIPE_COUNT)}
        for dst in dst_layer:
            val = _diag_coord(pos[dst][1], pos[dst][2], cy_dst, cz_dst, layer_idx + 1)
            dst_by_stripe[_stripe_index(val, dst_lo, dst_hi)].append(dst)

        for src in src_layer:
            val = _diag_coord(pos[src][1], pos[src][2], cy_src, cz_src, layer_idx)
            stripe = _stripe_index(val, src_lo, src_hi)
            target_stripes = [stripe, _neighbor_stripe(stripe, layer_idx)]

            chosen: list[int] = []
            for target in target_stripes:
                candidates = dst_by_stripe.get(target, [])
                if not candidates:
                    continue
                best = min(
                    candidates,
                    key=lambda dst: (
                        pos[dst][0] - pos[src][0]
                    ) ** 2
                    + (pos[dst][1] - pos[src][1]) ** 2
                    + (pos[dst][2] - pos[src][2]) ** 2,
                )
                if best not in chosen:
                    chosen.append(best)

            if not chosen:
                best = min(
                    dst_layer,
                    key=lambda dst: (
                        pos[dst][0] - pos[src][0]
                    ) ** 2
                    + (pos[dst][1] - pos[src][1]) ** 2
                    + (pos[dst][2] - pos[src][2]) ** 2,
                )
                chosen.append(best)

            for dst in sorted(
                dst_layer,
                key=lambda d: (
                    pos[d][0] - pos[src][0]
                ) ** 2
                + (pos[d][1] - pos[src][1]) ** 2
                + (pos[d][2] - pos[src][2]) ** 2,
            ):
                if len(chosen) >= MIN_EDGES:
                    break
                if dst not in chosen:
                    chosen.append(dst)
            adj[src].extend(chosen)

    return Family(pos, layers, adj)


def _field_from_sources(
    pos: list[tuple[float, float, float]],
    layers: list[list[int]],
    sources: list[tuple[float, int]],
) -> list[float]:
    field = [0.0] * len(pos)
    source_layer = NL // 3
    x_target = source_layer * H
    layer_nodes = layers[source_layer]
    for z_phys, charge in sources:
        best = None
        best_d = float("inf")
        for idx in layer_nodes:
            x, y, z = pos[idx]
            d = (x - x_target) ** 2 + y**2 + (z - z_phys) ** 2
            if d < best_d:
                best = idx
                best_d = d
        if best is None:
            continue
        mx, my, mz = pos[best]
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


def _measure_family(pos, adj, layers) -> RowResult:
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
    exponent = (
        math.log(abs(double / plus)) / math.log(2.0)
        if abs(plus) > 1e-30 and abs(double) > 1e-30
        else math.nan
    )
    return RowResult(
        drift=float("nan"),
        seed=-1,
        zero=zero,
        plus=plus,
        minus=minus,
        neutral=neutral,
        double=double,
        exponent=exponent,
    )


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else math.nan


def run_full_replay() -> None:
    print("=" * 96)
    print("SEVENTH FAMILY DIAGONAL SWEEP")
    print("  question: does a non-shell diagonal-stripe connectivity rule carry the")
    print("  signed-source fixed-field package on the no-restore grown family?")
    print("=" * 96)
    print(f"h={H}, NL={NL}, drifts={DRIFTS}, seeds={SEEDS}, stripes={STRIPE_COUNT}")
    print("guards: exact zero-source baseline, exact neutral cancellation, sign orientation")
    print()
    print(f"{'drift':>5s} {'seed':>4s} {'zero':>12s} {'plus':>12s} {'minus':>12s} {'neutral':>12s} {'double':>12s} {'exp':>7s} {'ok':>4s}")
    print("-" * 96)

    rows: list[RowResult] = []
    for drift in DRIFTS:
        for seed in SEEDS:
            pos, adj, layers, _nmap = grow(drift, seed)
            fam = Family(pos, layers, adj)
            diag = _build_diagonal_stripe_connectivity(fam)
            out = _measure_family(diag.positions, diag.adj, diag.layers)
            rows.append(RowResult(
                drift=drift,
                seed=seed,
                zero=out.zero,
                plus=out.plus,
                minus=out.minus,
                neutral=out.neutral,
                double=out.double,
                exponent=out.exponent,
            ))

    for r in rows:
        print(
            f"{r.drift:5.2f} {r.seed:4d} "
            f"{r.zero:+12.3e} {r.plus:+12.3e} {r.minus:+12.3e} "
            f"{r.neutral:+12.3e} {r.double:+12.3e} {r.exponent:7.3f} "
            f"{'YES' if r.ok else 'no':>4s}"
        )

    passed = [r for r in rows if r.ok]
    print()
    print("SAFE READ")
    print(f"  passed rows: {len(passed)}/{len(rows)}")
    if passed:
        drift_vals = sorted({r.drift for r in passed})
        seed_vals = sorted({r.seed for r in passed})
        print(f"  drift coverage: {drift_vals}")
        print(f"  seed coverage: {seed_vals}")
        print(f"  mean charge exponent among passes: {_mean([r.exponent for r in passed]):.6f}")
        print("  boundary read: seed-selective pocket only, not family-wide closure")
    else:
        print("  no row survived the exact zero/neutral gate")
        print("  the diagonal-stripe rule is a diagnosed failure on this slice")


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
    ok_flags = [m.group("ok") == "YES" for m in ROW_RE.finditer(text)]
    passed = [row for row, ok in zip(rows, ok_flags) if ok]
    stale_summary = re.search(r"passed rows:\s*(\d+)/(\d+)", text)

    failures: list[str] = []
    expected_pairs = [(drift, seed) for drift in DRIFTS for seed in SEEDS]
    observed_pairs = [(round(row.drift, 2), row.seed) for row in rows]
    if "SEVENTH FAMILY DIAGONAL SWEEP" not in text:
        failures.append("missing frozen-log title")
    if observed_pairs != [(round(d, 2), s) for d, s in expected_pairs]:
        failures.append(f"drift/seed grid mismatch: {observed_pairs}")
    if len(rows) != 18:
        failures.append(f"expected 18 rows, found {len(rows)}")
    if len(passed) != 7:
        failures.append(f"expected 7 row-derived passing pockets, found {len(passed)}")
    if stale_summary and stale_summary.groups() != ("6", "18"):
        failures.append(f"unexpected legacy summary line: {stale_summary.group(0)}")
    if "boundary read: seed-selective pocket only" not in text:
        failures.append("seed-selective boundary read missing")

    for row, ok in zip(rows, ok_flags):
        label = f"drift={row.drift:.2f} seed={row.seed}"
        if abs(row.zero) > 1e-12:
            failures.append(f"{label} zero gate failed")
        if abs(row.neutral) > 1e-12:
            failures.append(f"{label} neutral gate failed")
        if abs(row.exponent - 1.0) > 0.003:
            failures.append(f"{label} exponent gate failed")
        sign_gate = row.plus > 0.0 > row.minus and row.double > 0.0
        if ok and not sign_gate:
            failures.append(f"{label} marked YES but sign gate does not pass")
        if (not ok) and sign_gate:
            failures.append(f"{label} marked no but row has passing sign orientation")

    drift_coverage = sorted({row.drift for row in passed})
    seed_coverage = sorted({row.seed for row in passed})
    mean_exp = _mean([row.exponent for row in passed])

    print("=" * 96)
    print("SEVENTH FAMILY DIAGONAL SWEEP FROZEN LOG VERIFIER")
    print(f"log: {FROZEN_LOG.relative_to(REPO_ROOT)}")
    print("=" * 96)
    for row, ok in zip(rows, ok_flags):
        print(
            f"drift={row.drift:.2f} seed={row.seed} "
            f"zero={row.zero:+.3e} neutral={row.neutral:+.3e} "
            f"plus={row.plus:+.3e} minus={row.minus:+.3e} "
            f"double={row.double:+.3e} exp={row.exponent:.3f} "
            f"{'PASS' if ok else 'boundary'}"
        )
    print()
    print(f"row-derived passing rows: {len(passed)}/{len(rows)}")
    if stale_summary:
        print(f"legacy frozen-log summary line: {stale_summary.group(1)}/{stale_summary.group(2)}")
    print(f"drift coverage: {drift_coverage}")
    print(f"seed coverage: {seed_coverage}")
    print(f"mean charge exponent among row-derived passes: {mean_exp:.6f}")
    print()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"SCORECARD PASS=0 FAIL={len(failures)}")
        return 1
    print("SAFE READ: seed-selective boundary pocket only, not family-wide closure.")
    print(f"SCORECARD PASS={len(rows)} FAIL=0")
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
