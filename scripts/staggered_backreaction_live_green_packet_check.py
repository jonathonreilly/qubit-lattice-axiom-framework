#!/usr/bin/env python3
"""Live bounded packet for the staggered graph-Green backreaction runner."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import frontier_staggered_backreaction_green_closure as green  # noqa: E402


def _compute():
    graphs = green.base._make_graphs()
    mappings = green._make_mappings()
    raw_by_map = {}
    cal_by_map = {}
    summaries = []

    for spec in mappings:
        raw_rows = [green._measure_family(graph, spec, gain=1.0) for graph in graphs]
        cycle_rows = [row for row in raw_rows if "layered" not in row.family]
        gain = green._fit_gain(cycle_rows)
        cal_rows = [green._measure_family(graph, spec, gain=gain) for graph in graphs]
        raw_by_map[spec.name] = raw_rows
        cal_by_map[spec.name] = cal_rows
        summaries.append(green._summarize(spec.name, raw_rows, cal_rows, gain))

    summaries.sort(key=lambda summary: summary.balance_score)
    return summaries, raw_by_map, cal_by_map


def main() -> int:
    summaries, _raw_by_map, cal_by_map = _compute()
    best = summaries[0]
    baseline = next(summary for summary in summaries if summary.mapping == "screened_poisson")
    improvement = baseline.cycle_raw_gap / max(best.cycle_raw_gap, 1e-30)

    print("=" * 96)
    print("STAGGERED BACKREACTION LIVE GRAPH-GREEN PACKET")
    print("  current runner surface; bounded positive read only")
    print("=" * 96)
    print(
        f"{'mapping':<18} {'gain':>8s} {'raw_cycle':>10s} {'cal_cycle':>10s} "
        f"{'raw_hold':>10s} {'cal_hold':>10s} {'balance':>10s}"
    )
    print("-" * 96)
    for summary in summaries:
        print(
            f"{summary.mapping:<18} {summary.gain_fit:8.3f} "
            f"{summary.cycle_raw_gap:10.3e} {summary.cycle_cal_gap:10.3e} "
            f"{summary.holdout_raw_gap:10.3e} {summary.holdout_cal_gap:10.3e} "
            f"{summary.balance_score:10.3e}"
        )

    print()
    print("BEST MAP CALIBRATED READOUT")
    for row in cal_by_map[best.mapping]:
        print(
            f"{row.mapping:<18} {row.family:<26} "
            f"gap={row.solve_gap:.3e} R2={row.source_r2:.4f} "
            f"2body={row.two_body_resid:.3e} self_gap={row.self_gap:.3e} "
            f"norm={row.norm_drift:.2e} TOWARD={row.toward_fraction}/{row.toward_total}"
        )

    assertions_ok = (
        best.mapping == "resistance_yukawa"
        and improvement > 2.5
        and best.cycle_raw_gap < 0.35
        and best.holdout_raw_gap < 0.02
        and best.source_r2_min > 0.997
        and best.two_body_max < 1e-12
        and best.toward_min == 3
        and best.norm_max < 1e-12
        and best.holdout_cal_gap > 0.5
        and best.cycle_raw_self_gap > 0.1
    )

    print()
    print("SAFE READ")
    print(f"  best map: {best.mapping}")
    print(f"  raw cycle-gap improvement over screened Poisson: {improvement:.2f}x")
    print(f"  raw holdout gap: {best.holdout_raw_gap:.3e}")
    print(f"  calibrated holdout gap remains large: {best.holdout_cal_gap:.3e}")
    print(f"  cycle-bearing self-gap remains open: {best.cycle_raw_self_gap:.3e}")
    print("  bounded live packet only: no clean calibrated holdout closure")
    print(f"  [{'PASS' if assertions_ok else 'FAIL'} (C)] live graph-Green packet")
    print(f"ASSERTIONS: {'PASS' if assertions_ok else 'FAIL'}")
    return 0 if assertions_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
