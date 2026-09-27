#!/usr/bin/env python3
"""Explain the retained or failing atomic-lane mechanism across the selected ensembles."""

from __future__ import annotations

import argparse
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
import sys
import time

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_lane_runtime import (  # noqa: E402
    DEFAULT_CACHE_DIR,
    DEFAULT_OUTPUT_ROOT,
    AtomicLaneEnsembleSummaryRow,
    infer_atomic_lane_mechanism,
    load_shell_mechanism_stages,
    read_json,
    stage_record_table,
    write_json,
)
from toy_event_physics import threshold_core_shell_offender_analysis  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ladder-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_route_ladder_scan.json",
        help="current-family ladder verdict JSON",
    )
    parser.add_argument(
        "--search-json",
        type=Path,
        help="optional search JSON for promoted-family comparison",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=DEFAULT_CACHE_DIR,
        help="persistent stage-cache directory",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_route_mechanism.json",
        help="mechanism output JSON path",
    )
    args = parser.parse_args()

    ladder_payload = read_json(args.ladder_json)
    ladder_rows = [
        AtomicLaneEnsembleSummaryRow(**row_payload)
        for row_payload in ladder_payload.get("rows", [])
    ]
    first_failure = next((row for row in ladder_rows if not row.retained_passes), None)
    if first_failure is None:
        target_ensembles = tuple(row.ensemble_name for row in ladder_rows)
    else:
        target_ensembles = tuple(
            row.ensemble_name
            for row in ladder_rows
            if row.retained_passes or row.ensemble_name == first_failure.ensemble_name
        )

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    shell_rows: list[dict[str, object]] = []
    aggregate_rows: list[dict[str, object]] = []
    mechanism_rows: list[dict[str, object]] = []
    combined_case_rows = []
    stage_records_by_ensemble: dict[str, list[dict[str, object]]] = {}
    ladder_by_ensemble = {row.ensemble_name: row for row in ladder_rows}

    for ensemble_name in target_ensembles:
        shell_row, case_rows, case_aggregate_rows, _offender_rows, stage_records = (
            load_shell_mechanism_stages(
                ensemble_name=ensemble_name,
                cache_dir=args.cache_dir,
                use_cache=True,
            )
        )
        stage_records_by_ensemble[ensemble_name] = stage_record_table(stage_records)
        shell_rows.append(asdict(shell_row))
        aggregate_rows.extend(asdict(row) for row in case_aggregate_rows)
        combined_case_rows.extend(case_rows)
        mechanism_summary = infer_atomic_lane_mechanism(
            summary_row=ladder_by_ensemble[ensemble_name],
            shell_row=shell_row,
        )
        mechanism_rows.append(mechanism_summary)
        stage_status = ", ".join(
            f"{record.stage_name}={'cache' if record.cache_hit else 'compute'}:{record.elapsed_seconds:.1f}s"
            for record in stage_records
        )
        print(
            f"mechanism {ensemble_name}: {mechanism_summary['mechanism_label']} "
            f"fails={mechanism_summary['failed_criteria']} stages=[{stage_status}]",
            flush=True,
        )

    offender_rows = [
        asdict(row) for row in threshold_core_shell_offender_analysis(combined_case_rows)
    ]
    candidate_family_comparison = None
    if args.search_json is not None and args.search_json.exists():
        search_payload = read_json(args.search_json)
        if search_payload.get("promoted_family") is not None:
            candidate_family_comparison = {
                "promoted_family": search_payload["promoted_family"],
                "tested_ensembles": (
                    search_payload.get("canonical_validation")
                    or search_payload["promoted_family"]["tested_ensembles"]
                ),
            }

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "ladder_json": str(args.ladder_json),
        "search_json": str(args.search_json) if args.search_json is not None else None,
        "target_ensembles": list(target_ensembles),
        "shell_rows": shell_rows,
        "case_aggregate_rows": aggregate_rows,
        "mechanism_rows": mechanism_rows,
        "offender_rows": offender_rows,
        "first_failure_mechanism": next(
            (
                row
                for row in mechanism_rows
                if first_failure is not None and row["ensemble_name"] == first_failure.ensemble_name
            ),
            None,
        ),
        "candidate_family_comparison": candidate_family_comparison,
        "stage_records_by_ensemble": stage_records_by_ensemble,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Route Mechanism")
    print("======================")
    if output_payload["first_failure_mechanism"] is None:
        print("- No failing ensemble was present in the ladder input.")
    else:
        first_failure_mechanism = output_payload["first_failure_mechanism"]
        print(
            f"- First failure mechanism: {first_failure_mechanism['ensemble_name']} "
            f"=> {first_failure_mechanism['mechanism_label']}."
        )
    print(f"- Wrote mechanism output to {args.write_json}.")


if __name__ == "__main__":
    main()
