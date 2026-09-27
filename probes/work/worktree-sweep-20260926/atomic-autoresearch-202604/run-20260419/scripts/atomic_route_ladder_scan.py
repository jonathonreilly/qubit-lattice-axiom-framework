#!/usr/bin/env python3
"""Canonical current-family verdict runner for the atomic generated-ensemble ladder."""

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
    evaluate_atomic_lane_ensemble,
    neighboring_stricter_ensemble,
    read_json,
    stage_record_table,
    summarize_stage_records,
    write_json,
)
from toy_event_physics import (  # noqa: E402
    AtomicLaneEnsembleSummaryRow,
    canonical_generated_ensemble_specs,
    generated_ensemble_spec,
    render_atomic_lane_ensemble_summary_table,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ensembles",
        nargs="*",
        help="optional named generated ensembles; defaults to the full canonical ladder",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="resume from an existing state file or prior JSON output",
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
        help="write the machine-readable ladder verdict JSON to this path",
    )
    parser.add_argument(
        "--start-at",
        help="start from this ensemble name within the requested ladder",
    )
    parser.add_argument(
        "--stop-after",
        type=int,
        help="stop after this many ensembles in the current invocation",
    )
    args = parser.parse_args()

    ensemble_names = resolve_ensemble_names(args.ensembles, args.start_at)
    output_path = args.write_json or (DEFAULT_OUTPUT_ROOT / "atomic_route_ladder_scan.json")
    state_path = output_path.with_suffix(".state.json")
    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    completed_rows: list[AtomicLaneEnsembleSummaryRow] = []
    stage_records_by_ensemble: dict[str, list[dict[str, object]]] = {}
    profile_snapshot: dict[str, object] | None = None
    completed_names: list[str] = []

    if args.resume:
        previous_state = load_previous_state(state_path, output_path)
        if previous_state is not None:
            completed_rows = [
                AtomicLaneEnsembleSummaryRow(**row_payload)
                for row_payload in previous_state.get("rows", [])
            ]
            completed_names = [row.ensemble_name for row in completed_rows]
            stage_records_by_ensemble = {
                ensemble_name: list(records)
                for ensemble_name, records in previous_state.get(
                    "stage_records_by_ensemble",
                    {},
                ).items()
            }
            profile_snapshot = previous_state.get("profile_snapshot")

    remaining_ensembles = [
        ensemble_name for ensemble_name in ensemble_names if ensemble_name not in set(completed_names)
    ]
    if args.stop_after is not None:
        remaining_ensembles = remaining_ensembles[: max(0, args.stop_after)]

    print(
        "atomic route ladder scan started "
        f"{started_at} requested={tuple(ensemble_names)} resume={args.resume}",
        flush=True,
    )
    print(f"cache_dir={args.cache_dir}", flush=True)
    print(f"output_json={output_path}", flush=True)

    for index, ensemble_name in enumerate(remaining_ensembles, start=1):
        ensemble_started = time.perf_counter()
        print(
            f"[{index}/{len(remaining_ensembles)}] evaluating {ensemble_name}",
            flush=True,
        )
        row, _components, stage_records = evaluate_atomic_lane_ensemble(
            ensemble_name=ensemble_name,
            cache_dir=args.cache_dir,
            search_stage="current-family",
            use_cache=True,
        )
        completed_rows.append(row)
        stage_records_by_ensemble[ensemble_name] = stage_record_table(stage_records)
        if profile_snapshot is None:
            profile_snapshot = summarize_stage_records(stage_records)
        stage_status = ", ".join(
            f"{record.stage_name}={'cache' if record.cache_hit else 'compute'}:{record.elapsed_seconds:.1f}s"
            for record in stage_records
        )
        print(
            f"[{index}/{len(remaining_ensembles)}] finished {ensemble_name} "
            f"gate={'PASS' if row.retained_passes else 'FAIL'} "
            f"nesting_floor={row.nesting_floor:.2f} "
            f"fails={row.failed_criteria} "
            f"elapsed={time.perf_counter() - ensemble_started:.1f}s "
            f"stages=[{stage_status}]",
            flush=True,
        )
        write_json(
            state_path,
            build_output_payload(
                started_at=started_at,
                completed_at=None,
                requested_ensembles=ensemble_names,
                rows=completed_rows,
                stage_records_by_ensemble=stage_records_by_ensemble,
                profile_snapshot=profile_snapshot,
                total_elapsed_seconds=time.perf_counter() - total_started,
            ),
        )

    completed_rows.sort(
        key=lambda row: next(
            index
            for index, (name, *_rest) in enumerate(canonical_generated_ensemble_specs())
            if name == row.ensemble_name
        )
    )
    finished_at = datetime.now().isoformat(timespec="seconds")
    final_payload = build_output_payload(
        started_at=started_at,
        completed_at=finished_at,
        requested_ensembles=ensemble_names,
        rows=completed_rows,
        stage_records_by_ensemble=stage_records_by_ensemble,
        profile_snapshot=profile_snapshot,
        total_elapsed_seconds=time.perf_counter() - total_started,
    )
    write_json(output_path, final_payload)
    write_json(state_path, final_payload)

    print()
    print("Atomic Lane Ladder Summary")
    print("==========================")
    print(render_atomic_lane_ensemble_summary_table(completed_rows))
    print()
    print("Decision Surface")
    print("================")
    print(
        f"- Retained current family on {sum(row.retained_passes for row in completed_rows)}/{len(completed_rows)} tested ensembles."
    )
    first_failure = final_payload["first_failure"]
    if first_failure is not None:
        print(
            f"- First failure: {first_failure['ensemble_name']} "
            f"criteria={first_failure['failed_criteria']} "
            f"next={final_payload['neighboring_ensemble_beyond_failure']}."
        )
    else:
        print("- No failure detected on the tested ladder.")
    if profile_snapshot is not None:
        stage_timings = ", ".join(
            f"{stage_name}={elapsed:.2f}s"
            for stage_name, elapsed in profile_snapshot["stage_elapsed_seconds"].items()
        )
        print(f"- Profile snapshot: {stage_timings}.")
    print()
    print(
        "atomic route ladder scan completed "
        f"{finished_at} total_elapsed={time.perf_counter() - total_started:.1f}s",
        flush=True,
    )


def resolve_ensemble_names(
    requested_names: list[str] | None,
    start_at: str | None,
) -> tuple[str, ...]:
    if requested_names:
        ensemble_names = tuple(generated_ensemble_spec(name)[0] for name in requested_names)
    else:
        ensemble_names = tuple(name for name, *_rest in canonical_generated_ensemble_specs())
    if start_at is None:
        return ensemble_names
    if start_at not in ensemble_names:
        raise SystemExit(f"--start-at {start_at!r} is not in the requested ladder {ensemble_names}")
    start_index = ensemble_names.index(start_at)
    return ensemble_names[start_index:]


def load_previous_state(state_path: Path, output_path: Path) -> dict[str, object] | None:
    if state_path.exists():
        return read_json(state_path)
    if output_path.exists():
        return read_json(output_path)
    return None


def build_output_payload(
    *,
    started_at: str,
    completed_at: str | None,
    requested_ensembles: tuple[str, ...],
    rows: list[AtomicLaneEnsembleSummaryRow],
    stage_records_by_ensemble: dict[str, list[dict[str, object]]],
    profile_snapshot: dict[str, object] | None,
    total_elapsed_seconds: float,
) -> dict[str, object]:
    ordered_rows = sorted(
        rows,
        key=lambda row: next(
            index
            for index, (name, *_rest) in enumerate(canonical_generated_ensemble_specs())
            if name == row.ensemble_name
        ),
    )
    first_failure = next((row for row in ordered_rows if not row.retained_passes), None)
    return {
        "started_at": started_at,
        "completed_at": completed_at,
        "requested_ensembles": list(requested_ensembles),
        "rows": [asdict(row) for row in ordered_rows],
        "stage_records_by_ensemble": stage_records_by_ensemble,
        "profile_snapshot": profile_snapshot,
        "retained_all_ensembles": bool(ordered_rows) and all(
            row.retained_passes for row in ordered_rows
        ),
        "first_failure": asdict(first_failure) if first_failure is not None else None,
        "neighboring_ensemble_beyond_failure": (
            neighboring_stricter_ensemble(first_failure.ensemble_name)
            if first_failure is not None
            else None
        ),
        "tested_ensemble_count": len(ordered_rows),
        "total_elapsed_seconds": round(total_elapsed_seconds, 6),
    }


if __name__ == "__main__":
    main()
