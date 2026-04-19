#!/usr/bin/env python3
"""Open atomic-family expansion search after the current family first fails."""

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
    AtomicRouteCandidateSpec,
    DEFAULT_CACHE_DIR,
    DEFAULT_OUTPUT_ROOT,
    AtomicLaneEnsembleSummaryRow,
    evaluate_atomic_lane_ensemble,
    evaluate_candidate_family,
    load_feature_supports,
    read_json,
    search_atomic_route_family,
    stage_record_table,
    write_json,
)
from toy_event_physics import canonical_generated_ensemble_specs  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ladder-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_route_ladder_scan.json",
        help="current-family ladder verdict JSON",
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
        default=DEFAULT_OUTPUT_ROOT / "atomic_route_search.json",
        help="machine-readable search output path",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="resume from a prior tier checkpoint",
    )
    parser.add_argument(
        "--max-features",
        type=int,
        default=3,
        help="maximum candidate feature count per atomic leg",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=25,
        help="retain this many ranked families in the output",
    )
    args = parser.parse_args()

    ladder_payload = read_json(args.ladder_json)
    ladder_rows = [
        AtomicLaneEnsembleSummaryRow(**row_payload)
        for row_payload in ladder_payload.get("rows", [])
    ]
    first_failure = next((row for row in ladder_rows if not row.retained_passes), None)
    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    state_path = args.write_json.with_suffix(".state.json")

    if first_failure is None:
        output_payload = {
            "started_at": started_at,
            "completed_at": datetime.now().isoformat(timespec="seconds"),
            "ladder_json": str(args.ladder_json),
            "search_performed": False,
            "reason": "current-family-already-retained",
        }
        write_json(args.write_json, output_payload)
        write_json(state_path, output_payload)
        print("current family retained across the tested ladder; no open search needed.", flush=True)
        return

    summary_rows_by_ensemble = {row.ensemble_name: row for row in ladder_rows}
    failure_index = next(
        index
        for index, row in enumerate(ladder_rows)
        if row.ensemble_name == first_failure.ensemble_name
    )
    passing_ensembles = tuple(
        row.ensemble_name
        for row in ladder_rows[:failure_index]
        if row.retained_passes
    )
    stricter_ensemble = ladder_payload.get("neighboring_ensemble_beyond_failure")
    if stricter_ensemble and stricter_ensemble not in summary_rows_by_ensemble:
        stricter_row, _components, _records = evaluate_atomic_lane_ensemble(
            ensemble_name=stricter_ensemble,
            cache_dir=args.cache_dir,
            search_stage="current-family",
            use_cache=True,
        )
        summary_rows_by_ensemble[stricter_ensemble] = stricter_row

    relevant_ensembles = list(passing_ensembles) + [first_failure.ensemble_name]
    if stricter_ensemble:
        relevant_ensembles.append(stricter_ensemble)

    invariant_blockers = []
    for ensemble_name in relevant_ensembles:
        row = summary_rows_by_ensemble[ensemble_name]
        blocked_by = []
        if row.compact_ge6_share6_match_fraction < 0.98:
            blocked_by.append("compact-ge6-share6")
        if row.compact_ge7_subset_fraction < 0.99:
            blocked_by.append("compact-ge7-subset")
        if not row.fallback_is_distinct:
            blocked_by.append("fallback-leakage")
        if blocked_by:
            invariant_blockers.append(
                {
                    "ensemble_name": ensemble_name,
                    "blocked_by": blocked_by,
                }
            )

    if invariant_blockers:
        output_payload = build_output_payload(
            started_at=started_at,
            completed_at=datetime.now().isoformat(timespec="seconds"),
            ladder_json=args.ladder_json,
            first_failure=first_failure,
            passing_ensembles=passing_ensembles,
            stricter_ensemble=stricter_ensemble,
            support_stage_records={},
            top_results=[],
            tier_counts={},
            promoted_family=None,
            canonical_validation=None,
            completed_tier=0,
            total_elapsed_seconds=time.perf_counter() - total_started,
        )
        output_payload["invariant_blockers"] = invariant_blockers
        output_payload["search_aborted"] = True
        output_payload["reason"] = "candidate-invariant-failure"
        write_json(args.write_json, output_payload)
        write_json(state_path, output_payload)
        print()
        print("Atomic Route Search")
        print("===================")
        print(
            f"- Search aborted: invariant blockers present on "
            f"{', '.join(blocker['ensemble_name'] for blocker in invariant_blockers)}."
        )
        print(f"- Wrote search output to {args.write_json}.")
        return

    completed_tier = 0
    top_results: list[dict[str, object]] = []
    tier_counts: dict[str, object] = {}
    promoted_family: dict[str, object] | None = None
    canonical_validation: dict[str, object] | None = None
    if args.resume and state_path.exists():
        previous_state = read_json(state_path)
        completed_tier = int(previous_state.get("completed_tier", 0))
        top_results = list(previous_state.get("top_results", []))
        tier_counts = dict(previous_state.get("tier_counts", {}))
        promoted_family = previous_state.get("promoted_family")
        canonical_validation = previous_state.get("canonical_validation")

    support_payloads_by_ensemble: dict[str, dict[str, object]] = {}
    support_stage_records: dict[str, list[dict[str, object]]] = {}
    for ensemble_name in relevant_ensembles:
        support_payload, record = load_feature_supports(
            ensemble_name=ensemble_name,
            cache_dir=args.cache_dir,
            search_stage="search",
            use_cache=True,
        )
        support_payloads_by_ensemble[ensemble_name] = support_payload
        support_stage_records[ensemble_name] = stage_record_table([record])
        print(
            f"supports {ensemble_name}: {'cache' if record.cache_hit else 'compute'} "
            f"elapsed={record.elapsed_seconds:.1f}s",
            flush=True,
        )

    for tier in range(completed_tier + 1, args.max_features + 1):
        tier_started = time.perf_counter()
        print(
            f"search tier {tier}: exhaustive families up to {tier} feature(s) per leg",
            flush=True,
        )
        search_payload = search_atomic_route_family(
            summary_rows_by_ensemble=summary_rows_by_ensemble,
            support_payloads_by_ensemble=support_payloads_by_ensemble,
            passing_ensembles=passing_ensembles,
            first_failing_ensemble=first_failure.ensemble_name,
            stricter_ensemble=stricter_ensemble,
            max_features=tier,
            top_k=args.top_k,
            start_tier=tier,
            initial_top_results=top_results,
            initial_tier_counts=tier_counts,
            initial_promoted_family=promoted_family,
        )
        top_results = list(search_payload["top_results"])
        tier_counts = dict(search_payload["tier_counts"])
        promoted_family = search_payload["promoted_family"]
        completed_tier = tier
        write_json(
            state_path,
            build_output_payload(
                started_at=started_at,
                completed_at=None,
                ladder_json=args.ladder_json,
                first_failure=first_failure,
                passing_ensembles=passing_ensembles,
                stricter_ensemble=stricter_ensemble,
                support_stage_records=support_stage_records,
                top_results=top_results,
                tier_counts=tier_counts,
                promoted_family=promoted_family,
                canonical_validation=canonical_validation,
                completed_tier=completed_tier,
                total_elapsed_seconds=time.perf_counter() - total_started,
            ),
        )
        tier_count = tier_counts.get(f"tier_{tier}", {})
        print(
            f"search tier {tier}: tested={tier_count.get('tested', 0)} "
            f"passed={tier_count.get('passed', 0)} "
            f"elapsed={time.perf_counter() - tier_started:.1f}s",
            flush=True,
        )
        if promoted_family is not None:
            break

    if promoted_family is not None:
        requested_ensembles = tuple(name for name, *_rest in canonical_generated_ensemble_specs())
        for ensemble_name in requested_ensembles:
            if ensemble_name not in summary_rows_by_ensemble:
                row, _components, _records = evaluate_atomic_lane_ensemble(
                    ensemble_name=ensemble_name,
                    cache_dir=args.cache_dir,
                    search_stage="current-family",
                    use_cache=True,
                )
                summary_rows_by_ensemble[ensemble_name] = row
            if ensemble_name not in support_payloads_by_ensemble:
                support_payload, record = load_feature_supports(
                    ensemble_name=ensemble_name,
                    cache_dir=args.cache_dir,
                    search_stage="search",
                    use_cache=True,
                )
                support_payloads_by_ensemble[ensemble_name] = support_payload
                support_stage_records[ensemble_name] = stage_record_table([record])
        canonical_validation = evaluate_candidate_family(
            low_candidate=AtomicRouteCandidateSpec(**promoted_family["low_candidate"]),
            pocket_candidate=AtomicRouteCandidateSpec(**promoted_family["pocket_candidate"]),
            deep_candidate=AtomicRouteCandidateSpec(**promoted_family["deep_candidate"]),
            summary_rows_by_ensemble=summary_rows_by_ensemble,
            support_payloads_by_ensemble=support_payloads_by_ensemble,
            ensemble_names=requested_ensembles,
        )
        promoted_family["canonical_validation"] = canonical_validation

    finished_at = datetime.now().isoformat(timespec="seconds")
    output_payload = build_output_payload(
        started_at=started_at,
        completed_at=finished_at,
        ladder_json=args.ladder_json,
        first_failure=first_failure,
        passing_ensembles=passing_ensembles,
        stricter_ensemble=stricter_ensemble,
        support_stage_records=support_stage_records,
        top_results=top_results,
        tier_counts=tier_counts,
        promoted_family=promoted_family,
        canonical_validation=canonical_validation,
        completed_tier=completed_tier,
        total_elapsed_seconds=time.perf_counter() - total_started,
    )
    write_json(args.write_json, output_payload)
    write_json(state_path, output_payload)

    print()
    print("Atomic Route Search")
    print("===================")
    if promoted_family is None:
        print(
            f"- No admissible family survived through tier {completed_tier}; "
            f"boundary remains at {first_failure.ensemble_name}."
        )
    else:
        low_candidate = promoted_family["low_candidate"]["feature_subset_label"]
        pocket_candidate = promoted_family["pocket_candidate"]["feature_subset_label"]
        deep_candidate = promoted_family["deep_candidate"]["feature_subset_label"]
        print(
            f"- Promoted family at tier {completed_tier}: "
            f"low={low_candidate}; pocket={pocket_candidate}; deep={deep_candidate}."
        )
        if canonical_validation is not None:
            print(
                f"- Full-ladder validation: {'PASS' if canonical_validation['passes'] else 'FAIL'}."
            )
    print(f"- Search output written to {args.write_json}.")


def build_output_payload(
    *,
    started_at: str,
    completed_at: str | None,
    ladder_json: Path,
    first_failure: AtomicLaneEnsembleSummaryRow,
    passing_ensembles: tuple[str, ...],
    stricter_ensemble: str | None,
    support_stage_records: dict[str, list[dict[str, object]]],
    top_results: list[dict[str, object]],
    tier_counts: dict[str, object],
    promoted_family: dict[str, object] | None,
    canonical_validation: dict[str, object] | None,
    completed_tier: int,
    total_elapsed_seconds: float,
) -> dict[str, object]:
    return {
        "started_at": started_at,
        "completed_at": completed_at,
        "ladder_json": str(ladder_json),
        "search_performed": True,
        "first_failure": asdict(first_failure),
        "passing_ensembles": list(passing_ensembles),
        "stricter_ensemble": stricter_ensemble,
        "support_stage_records": support_stage_records,
        "top_results": top_results,
        "tier_counts": tier_counts,
        "promoted_family": promoted_family,
        "canonical_validation": canonical_validation,
        "completed_tier": completed_tier,
        "total_elapsed_seconds": round(total_elapsed_seconds, 6),
    }


if __name__ == "__main__":
    main()
