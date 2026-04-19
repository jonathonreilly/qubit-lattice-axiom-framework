#!/usr/bin/env python3
"""Bounded bridge from the retained atomic lane to the bound-state / d=3 surface."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys
import time

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_lane_runtime import (  # noqa: E402
    DEFAULT_OUTPUT_ROOT,
    AtomicLaneEnsembleSummaryRow,
    build_bound_state_baseline,
    compare_atomic_lane_to_bound_state,
    read_json,
    write_json,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ladder-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_route_ladder_scan.json",
        help="current-family ladder verdict JSON",
    )
    parser.add_argument(
        "--mechanism-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_route_mechanism.json",
        help="mechanism JSON",
    )
    parser.add_argument(
        "--search-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_route_search.json",
        help="optional search JSON carrying a promoted-family full-ladder validation",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_bound_state_bridge.json",
        help="bridge output JSON path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    ladder_payload = read_json(args.ladder_json)
    ladder_rows = [
        AtomicLaneEnsembleSummaryRow(**row_payload)
        for row_payload in ladder_payload.get("rows", [])
    ]
    mechanism_payload = read_json(args.mechanism_json)
    search_payload = read_json(args.search_json) if args.search_json.exists() else None

    bridge_mode = None
    if ladder_payload.get("retained_all_ensembles"):
        bridge_mode = "current-family"
    elif (
        search_payload is not None
        and search_payload.get("canonical_validation") is not None
        and search_payload["canonical_validation"].get("passes")
    ):
        bridge_mode = "promoted-family"

    if bridge_mode is None:
        output_payload = {
            "started_at": started_at,
            "completed_at": datetime.now().isoformat(timespec="seconds"),
            "bridge_performed": False,
            "reason": "no-retained-family-available",
            "ladder_json": str(args.ladder_json),
            "mechanism_json": str(args.mechanism_json),
            "search_json": str(args.search_json),
        }
        write_json(args.write_json, output_payload)
        print("bridge skipped: no family survived the full requested ladder.", flush=True)
        return

    bound_state_baseline = build_bound_state_baseline()
    if bridge_mode == "current-family":
        comparison_payload = compare_atomic_lane_to_bound_state(
            summary_rows=ladder_rows,
            mechanism_rows=mechanism_payload["mechanism_rows"],
            bound_state_baseline=bound_state_baseline,
        )
    else:
        comparison_payload = build_promoted_family_bridge_payload(
            ladder_rows=ladder_rows,
            mechanism_rows=mechanism_payload["mechanism_rows"],
            bound_state_baseline=bound_state_baseline,
            canonical_validation=search_payload["canonical_validation"],
        )

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "bridge_performed": True,
        "bridge_mode": bridge_mode,
        "comparison": comparison_payload,
        "ladder_json": str(args.ladder_json),
        "mechanism_json": str(args.mechanism_json),
        "search_json": str(args.search_json),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Bound-State Bridge")
    print("=========================")
    print(f"- Bridge mode: {bridge_mode}.")
    print(
        f"- Bounded companion evidence: "
        f"{'YES' if comparison_payload['bounded_companion_evidence'] else 'NO'}."
    )
    print("- Dimension-selection claim support: NO.")
    print(f"- Wrote bridge output to {args.write_json}.")


def build_promoted_family_bridge_payload(
    *,
    ladder_rows: list[AtomicLaneEnsembleSummaryRow],
    mechanism_rows: list[dict[str, object]],
    bound_state_baseline: dict[str, object],
    canonical_validation: dict[str, object],
) -> dict[str, object]:
    ladder_by_ensemble = {row.ensemble_name: row for row in ladder_rows}
    mechanism_by_ensemble = {
        row["ensemble_name"]: row for row in mechanism_rows
    }
    tested_ensembles = canonical_validation["tested_ensembles"]
    atomic_summary = {
        "retained_all_ensembles": canonical_validation["passes"],
        "ensemble_count": len(tested_ensembles),
        "min_compact_match": min(
            ladder_by_ensemble[row["ensemble_name"]].compact_ge6_share6_match_fraction
            for row in tested_ensembles
        ),
        "min_compact_subset": min(
            ladder_by_ensemble[row["ensemble_name"]].compact_ge7_subset_fraction
            for row in tested_ensembles
        ),
        "min_nesting_floor": min(
            min(
                row["pocket_implies_low"],
                row["deep_implies_pocket"],
                row["deep_implies_low"],
            )
            for row in tested_ensembles
        ),
        "mean_ge6_only_fraction": sum(
            ladder_by_ensemble[row["ensemble_name"]].compact_ge6_only_fraction
            for row in tested_ensembles
        )
        / max(1, len(tested_ensembles)),
        "fallback_all_distinct": all(
            ladder_by_ensemble[row["ensemble_name"]].fallback_is_distinct
            for row in tested_ensembles
        ),
        "mean_deep_gap": sum(
            mechanism_by_ensemble[row["ensemble_name"]]["deep_gap"]
            for row in tested_ensembles
        )
        / max(1, len(tested_ensembles)),
        "mean_pocket_gap": sum(
            mechanism_by_ensemble[row["ensemble_name"]]["pocket_gap"]
            for row in tested_ensembles
        )
        / max(1, len(tested_ensembles)),
        "mean_low_gap": sum(
            mechanism_by_ensemble[row["ensemble_name"]]["low_gap"]
            for row in tested_ensembles
        )
        / max(1, len(tested_ensembles)),
    }
    bounded_companion_evidence = bool(
        atomic_summary["retained_all_ensembles"]
        and atomic_summary["fallback_all_distinct"]
        and atomic_summary["min_nesting_floor"] >= 0.98
        and atomic_summary["mean_deep_gap"] > 0.0
        and atomic_summary["mean_pocket_gap"] > 0.0
        and atomic_summary["mean_low_gap"] > 0.0
    )
    return {
        "atomic_summary": atomic_summary,
        "bound_state_baseline": bound_state_baseline,
        "bounded_companion_evidence": bounded_companion_evidence,
        "dimension_selection_claim_supported": False,
    }


if __name__ == "__main__":
    main()
