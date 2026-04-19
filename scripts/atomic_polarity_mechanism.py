#!/usr/bin/env python3
"""Mechanism analysis for a retained polarity discriminator family."""

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
    evaluate_atomic_lane_ensemble,
    infer_atomic_lane_mechanism,
    load_shell_summary_stage,
    read_json,
    stage_record_table,
    write_json,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--validation-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_polarity_candidate_validation.json",
        help="retained polarity candidate validation JSON",
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
        default=DEFAULT_OUTPUT_ROOT / "atomic_polarity_mechanism.json",
        help="mechanism output JSON path",
    )
    args = parser.parse_args()

    validation_payload = read_json(args.validation_json)
    tested_rows = list(validation_payload.get("tested_ensembles", []))
    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    synthesized_rows: list[AtomicLaneEnsembleSummaryRow] = []
    shell_rows: list[dict[str, object]] = []
    mechanism_rows: list[dict[str, object]] = []
    stage_records_by_ensemble: dict[str, list[dict[str, object]]] = {}

    for candidate_result in tested_rows:
        ensemble_name = candidate_result["ensemble_name"]
        base_summary, _components, _summary_records = evaluate_atomic_lane_ensemble(
            ensemble_name=ensemble_name,
            cache_dir=args.cache_dir,
            search_stage="current-family",
            use_cache=True,
        )
        synthesized_row = synthesize_summary_row(base_summary, candidate_result)
        synthesized_rows.append(synthesized_row)
        shell_row, stage_records = load_shell_summary_stage(
            ensemble_name=ensemble_name,
            cache_dir=args.cache_dir,
            use_cache=True,
        )
        stage_records_by_ensemble[ensemble_name] = stage_record_table(stage_records)
        shell_rows.append(asdict(shell_row))
        mechanism_summary = infer_atomic_lane_mechanism(
            summary_row=synthesized_row,
            shell_row=shell_row,
        )
        mechanism_rows.append(mechanism_summary)
        print(
            f"polarity mechanism {ensemble_name}: {mechanism_summary['mechanism_label']} "
            f"fails={mechanism_summary['failed_criteria']}",
            flush=True,
        )
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "validation_json": str(args.validation_json),
        "summary_rows": [asdict(row) for row in synthesized_rows],
        "shell_rows": shell_rows,
        "case_aggregate_rows": [],
        "mechanism_rows": mechanism_rows,
        "offender_rows": [],
        "stage_records_by_ensemble": stage_records_by_ensemble,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Polarity Mechanism")
    print("=========================")
    print(
        f"- Winning family mechanism labels: "
        f"{', '.join(sorted({row['mechanism_label'] for row in mechanism_rows}))}."
    )
    print(f"- Wrote mechanism output to {args.write_json}.")


def synthesize_summary_row(
    base_summary: AtomicLaneEnsembleSummaryRow,
    candidate_result: dict[str, object],
) -> AtomicLaneEnsembleSummaryRow:
    low_support_fraction = float(candidate_result["low_support_fraction"])
    pocket_support_fraction = float(candidate_result["pocket_support_fraction"])
    deep_support_fraction = float(candidate_result["deep_support_fraction"])
    return AtomicLaneEnsembleSummaryRow(
        ensemble_name=base_summary.ensemble_name,
        graph_count=base_summary.graph_count,
        total_nodes=base_summary.total_nodes,
        compact_ge6_share6_match_fraction=base_summary.compact_ge6_share6_match_fraction,
        compact_ge7_subset_fraction=base_summary.compact_ge7_subset_fraction,
        compact_ge6_only_fraction=base_summary.compact_ge6_only_fraction,
        low_parity_size=1 if low_support_fraction > 0.0 else None,
        low_feature_subset=base_summary.low_feature_subset,
        low_support_fraction=low_support_fraction,
        pocket_parity_size=1 if pocket_support_fraction > 0.0 else None,
        pocket_feature_subset=base_summary.pocket_feature_subset,
        pocket_support_fraction=pocket_support_fraction,
        deep_parity_size=1 if deep_support_fraction > 0.0 else None,
        deep_feature_subset=base_summary.deep_feature_subset,
        deep_support_fraction=deep_support_fraction,
        pocket_implies_low=float(candidate_result["pocket_implies_low"]),
        deep_implies_pocket=float(candidate_result["deep_implies_pocket"]),
        deep_implies_low=float(candidate_result["deep_implies_low"]),
        fallback_parity_size=0 if candidate_result["sparse_surface"]["nonvacuous_fallback_candidate"] is None else 1,
        fallback_feature_subset=(
            candidate_result["sparse_surface"]["nonvacuous_fallback_candidate"]["feature_subset_label"]
            if candidate_result["sparse_surface"]["nonvacuous_fallback_candidate"] is not None
            else "-"
        ),
        fallback_proxy_family=(
            candidate_result["sparse_surface"]["nonvacuous_fallback_candidate"]["proxy_family"]
            if candidate_result["sparse_surface"]["nonvacuous_fallback_candidate"] is not None
            else "none"
        ),
        fallback_route_role=(
            candidate_result["sparse_surface"]["nonvacuous_fallback_candidate"]["route_role"]
            if candidate_result["sparse_surface"]["nonvacuous_fallback_candidate"] is not None
            else "none"
        ),
        max_atomic_parity_size=1,
        atomic_chain_present=True,
        nesting_floor=min(
            float(candidate_result["pocket_implies_low"]),
            float(candidate_result["deep_implies_pocket"]),
            float(candidate_result["deep_implies_low"]),
        ),
        fallback_is_distinct=bool(candidate_result["fallback_is_distinct"]),
        retained_passes=bool(candidate_result["passes"]),
        failed_criteria=", ".join(candidate_result["failed_criteria"])
        if candidate_result["failed_criteria"]
        else "-",
    )


if __name__ == "__main__":
    main()
