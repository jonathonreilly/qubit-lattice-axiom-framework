#!/usr/bin/env python3
"""Live bounded packet for staggered capture-closure backreaction."""

from __future__ import annotations

from pathlib import Path
import statistics
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
NOTE_PATH = ROOT / "docs" / "STAGGERED_BACKREACTION_LIVE_CAPTURE_PACKET_NOTE_2026-05-29.md"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import frontier_staggered_backreaction_capture_closure_harness as cap  # noqa: E402


def main() -> int:
    cycle_graphs = [
        cap.cycle.make_random_geometric(seed=42),
        cap.cycle.make_growing(seed=42),
    ]
    holdout = cap.layered._build_layered_family(seed=29, layers=10, width=6, fanout=2)

    print("=" * 96)
    print("STAGGERED BACKREACTION LIVE CAPTURE-CLOSURE PACKET")
    print("  current runner surface; bounded positive read only")
    print("=" * 96)
    print(
        f"closure={cap.CLOSURE.name}, map={cap.CLOSURE.mapping.name}, "
        f"self_mix={cap.CLOSURE.self_mix:.2f}, "
        f"capture_exp={cap.CLOSURE.capture_exponent:.2f}"
    )

    cycle_results = []
    for graph in cycle_graphs:
        print()
        print(f"CAPTURE BATTERY: {graph.name} ({graph.n} nodes)")
        result = cap._measure_cycle_graph(graph, cap.CLOSURE)
        cycle_results.append(result)

    holdout_result = cap._measure_holdout(holdout, cap.CLOSURE)

    baseline_cycle_mean = statistics.fmean(row.baseline_gap for row in cycle_results)
    closed_cycle_mean = statistics.fmean(row.closed_gap for row in cycle_results)
    cycle_improvement = baseline_cycle_mean / max(closed_cycle_mean, 1e-30)
    holdout_improvement = holdout_result.baseline_gap / max(
        holdout_result.closed_gap, 1e-30
    )
    mean_r2 = statistics.fmean(row.linearity_r2 for row in cycle_results)
    two_body_max = max(row.two_body_resid for row in cycle_results)
    norm_max = max(row.norm_drift for row in cycle_results + [holdout_result])
    min_score = min(row.score for row in cycle_results)
    safe_read_lines = [
        f"cycle battery scores: {[row.score for row in cycle_results]}",
        f"cycle mean gap: {baseline_cycle_mean:.3e} -> {closed_cycle_mean:.3e}",
        f"cycle gap improvement factor: {cycle_improvement:.2f}x",
        "cycle mean R2: {:.6f}; two-body max < 1.0e-12".format(mean_r2),
        (
            f"holdout gap: {holdout_result.baseline_gap:.3e} -> "
            f"{holdout_result.closed_gap:.3e} ({holdout_improvement:.2f}x)"
        ),
        "ASSERTIONS: PASS",
    ]
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    note_sync_ok = all(line in note_text for line in safe_read_lines)

    print()
    print("HOLDOUT")
    print(
        f"  {holdout_result.graph}: baseline gap={holdout_result.baseline_gap:.3e}, "
        f"closed gap={holdout_result.closed_gap:.3e}, "
        f"improvement={holdout_improvement:.2f}x, "
        f"R2={holdout_result.linearity_r2:.6f}, TOWARD={holdout_result.toward}/3"
    )

    assertions_ok = (
        min_score == 9
        and baseline_cycle_mean > 0.95
        and closed_cycle_mean < 0.50
        and cycle_improvement > 2.0
        and mean_r2 > 0.99
        and two_body_max < 1e-12
        and holdout_result.zero_force == 0.0
        and holdout_result.closed_force > 0.0
        and holdout_result.closed_gap < holdout_result.baseline_gap
        and holdout_improvement > 1.9
        and holdout_result.linearity_r2 > 0.999
        and norm_max < 1e-12
        and note_sync_ok
    )

    print()
    print("SAFE READ")
    for line in safe_read_lines[:-1]:
        print(f"  {line}")
    print("  bounded live packet only: no old stale table or continuum closure")
    print(f"  [{'PASS' if note_sync_ok else 'FAIL'} (C)] source note live readout matches computed SAFE READ")
    print(f"  [{'PASS' if assertions_ok else 'FAIL'} (C)] live capture packet")
    print(f"ASSERTIONS: {'PASS' if assertions_ok else 'FAIL'}")
    return 0 if assertions_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
