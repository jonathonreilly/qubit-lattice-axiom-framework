#!/usr/bin/env python3
"""Live bounded packet for staggered capture-closure backreaction."""

from __future__ import annotations

import hashlib
from pathlib import Path
import statistics
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PROTOTYPE_SOURCE = SCRIPTS / "frontier_staggered_backreaction_prototype.py"
PROTOTYPE_CACHE = ROOT / "logs/runner-cache/frontier_staggered_backreaction_prototype.txt"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import frontier_staggered_backreaction_capture_closure_harness as cap  # noqa: E402


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def prototype_source_packet_ok() -> bool:
    source = PROTOTYPE_SOURCE.read_text(encoding="utf-8", errors="replace")
    cache = PROTOTYPE_CACHE.read_text(encoding="utf-8", errors="replace") if PROTOTYPE_CACHE.exists() else ""
    source_markers = [
        "class GraphFamily",
        "def _source_density",
        "def _solve_phi",
        "def _build_hamiltonian",
        "def _force_from_phi",
        "def _measure_family",
    ]
    cache_markers = [
        "===== runner cache v1 =====",
        "runner: scripts/frontier_staggered_backreaction_prototype.py",
        f"runner_sha256: {sha256_file(PROTOTYPE_SOURCE)}",
        "status: ok",
        "STAGGERED SOURCE-GENERATED BACKREACTION PROTOTYPE",
    ]
    return (
        len(source) > 20_000
        and all(marker in source for marker in source_markers)
        and all(marker in cache for marker in cache_markers)
    )


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
    )

    print()
    print("SAFE READ")
    print(f"  cycle battery scores: {[row.score for row in cycle_results]}")
    print(f"  cycle mean gap: {baseline_cycle_mean:.3e} -> {closed_cycle_mean:.3e}")
    print(f"  cycle gap improvement factor: {cycle_improvement:.2f}x")
    two_body_readout = (
        "<1e-12" if two_body_max < 1e-12 else f"={two_body_max:.3e}"
    )
    print(f"  cycle mean R2: {mean_r2:.6f}; two-body max {two_body_readout}")
    print(
        f"  holdout gap: {holdout_result.baseline_gap:.3e} -> "
        f"{holdout_result.closed_gap:.3e} ({holdout_improvement:.2f}x)"
    )
    prototype_packet_ok = prototype_source_packet_ok()
    print("PROTOTYPE_SOURCE_PACKET")
    print(f"  source: {PROTOTYPE_SOURCE.relative_to(ROOT)}")
    print(f"  cache: {PROTOTYPE_CACHE.relative_to(ROOT)}")
    print(f"  untruncated source/cache assertion: {'PASS' if prototype_packet_ok else 'FAIL'}")
    print("  bounded live packet only: no old stale table or continuum closure")
    all_ok = assertions_ok and prototype_packet_ok
    print(f"  [{'PASS' if all_ok else 'FAIL'} (C)] live capture packet")
    print(f"ASSERTIONS: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
