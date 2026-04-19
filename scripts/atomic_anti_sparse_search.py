#!/usr/bin/env python3
"""Search for a sparse discriminator that preserves the atomic chain while de-embedding fallback."""

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
    ANTI_SPARSE_DEFAULT_ENSEMBLES,
    ANTI_SPARSE_MAX_EXCLUDED_FRACTION,
    DEFAULT_CACHE_DIR,
    DEFAULT_OUTPUT_ROOT,
    NONVACUOUS_SPARSE_SUPPORT_FRACTION,
    AtomicLaneEnsembleSummaryRow,
    evaluate_atomic_lane_ensemble,
    load_feature_supports,
    read_json,
    search_anti_sparse_discriminators,
    stage_record_table,
    summarize_sparse_surface,
    write_json,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ensembles",
        nargs="*",
        help="optional named ensembles; defaults to first-failure plus its neighbor, else default/broader",
    )
    parser.add_argument(
        "--ladder-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_route_ladder_scan.json",
        help="optional ladder verdict JSON used to seed the default ensemble pair",
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
        default=DEFAULT_OUTPUT_ROOT / "atomic_anti_sparse_search.json",
        help="machine-readable anti-sparse output path",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="resume from a prior tier checkpoint",
    )
    parser.add_argument(
        "--feature-scope",
        choices=("sparse", "full"),
        default="sparse",
        help="feature vocabulary used for the exclusion bundles",
    )
    parser.add_argument(
        "--max-features",
        type=int,
        default=3,
        help="maximum discriminator bundle size",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=25,
        help="retain this many ranked discriminator bundles in the output",
    )
    parser.add_argument(
        "--max-excluded-fraction",
        type=float,
        default=ANTI_SPARSE_MAX_EXCLUDED_FRACTION,
        help="reject discriminators that exclude more than this residual fraction",
    )
    parser.add_argument(
        "--max-nonvacuous-support",
        type=float,
        default=NONVACUOUS_SPARSE_SUPPORT_FRACTION,
        help="ignore sparse fallback candidates at or above this support fraction",
    )
    args = parser.parse_args()

    ensemble_names = resolve_ensemble_names(args.ensembles, args.ladder_json)
    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    state_path = args.write_json.with_suffix(".state.json")
    completed_tier = 0
    top_results: list[dict[str, object]] = []
    tier_counts: dict[str, object] = {}
    promoted_discriminator: dict[str, object] | None = None
    if args.resume and state_path.exists():
        previous_state = read_json(state_path)
        completed_tier = int(previous_state.get("completed_tier", 0))
        top_results = list(previous_state.get("top_results", []))
        tier_counts = dict(previous_state.get("tier_counts", {}))
        promoted_discriminator = previous_state.get("promoted_discriminator")

    summary_rows_by_ensemble: dict[str, AtomicLaneEnsembleSummaryRow] = {}
    summary_stage_records: dict[str, list[dict[str, object]]] = {}
    support_payloads_by_ensemble: dict[str, dict[str, object]] = {}
    support_stage_records: dict[str, list[dict[str, object]]] = {}
    baseline_surfaces: dict[str, dict[str, object]] = {}

    print(
        "atomic anti-sparse search started "
        f"{started_at} ensembles={ensemble_names} scope={args.feature_scope} "
        f"resume={args.resume}",
        flush=True,
    )
    print(f"cache_dir={args.cache_dir}", flush=True)
    print(f"output_json={args.write_json}", flush=True)

    for ensemble_name in ensemble_names:
        summary_row, _components, summary_records = evaluate_atomic_lane_ensemble(
            ensemble_name=ensemble_name,
            cache_dir=args.cache_dir,
            search_stage="current-family",
            use_cache=True,
        )
        summary_rows_by_ensemble[ensemble_name] = summary_row
        summary_stage_records[ensemble_name] = stage_record_table(summary_records)
        support_payload, support_record = load_feature_supports(
            ensemble_name=ensemble_name,
            cache_dir=args.cache_dir,
            search_stage="anti-sparse",
            use_cache=True,
        )
        support_payloads_by_ensemble[ensemble_name] = support_payload
        support_stage_records[ensemble_name] = stage_record_table([support_record])
        baseline_surfaces[ensemble_name] = summarize_sparse_surface(
            support_payload=support_payload,
            max_support_fraction=args.max_nonvacuous_support,
        )
        print(
            f"baseline {ensemble_name}: "
            f"raw={render_candidate_label(baseline_surfaces[ensemble_name].get('raw_fallback_candidate'))} "
            f"raw_frac={baseline_surfaces[ensemble_name]['raw_fallback_support_fraction']:.3f} "
            f"nonvacuous={render_candidate_label(baseline_surfaces[ensemble_name].get('nonvacuous_fallback_candidate'))} "
            f"nonvacuous_frac={baseline_surfaces[ensemble_name]['nonvacuous_fallback_support_fraction']:.3f}",
            flush=True,
        )

    for tier in range(completed_tier + 1, args.max_features + 1):
        tier_started = time.perf_counter()
        print(
            f"search tier {tier}: {args.feature_scope} exclusion bundles up to {tier} feature(s)",
            flush=True,
        )
        search_payload = search_anti_sparse_discriminators(
            summary_rows_by_ensemble=summary_rows_by_ensemble,
            support_payloads_by_ensemble=support_payloads_by_ensemble,
            ensemble_names=ensemble_names,
            max_features=tier,
            feature_scope=args.feature_scope,
            top_k=args.top_k,
            start_tier=tier,
            initial_top_results=top_results,
            initial_tier_counts=tier_counts,
            initial_promoted_discriminator=promoted_discriminator,
            max_support_fraction=args.max_nonvacuous_support,
            max_excluded_fraction=args.max_excluded_fraction,
        )
        top_results = list(search_payload["top_results"])
        tier_counts = dict(search_payload["tier_counts"])
        promoted_discriminator = search_payload["promoted_discriminator"]
        completed_tier = tier
        write_json(
            state_path,
            build_output_payload(
                started_at=started_at,
                completed_at=None,
                ensemble_names=ensemble_names,
                ladder_json=args.ladder_json,
                feature_scope=args.feature_scope,
                summary_stage_records=summary_stage_records,
                support_stage_records=support_stage_records,
                baseline_surfaces=baseline_surfaces,
                top_results=top_results,
                tier_counts=tier_counts,
                promoted_discriminator=promoted_discriminator,
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
        if promoted_discriminator is not None:
            break

    finished_at = datetime.now().isoformat(timespec="seconds")
    output_payload = build_output_payload(
        started_at=started_at,
        completed_at=finished_at,
        ensemble_names=ensemble_names,
        ladder_json=args.ladder_json,
        feature_scope=args.feature_scope,
        summary_stage_records=summary_stage_records,
        support_stage_records=support_stage_records,
        baseline_surfaces=baseline_surfaces,
        top_results=top_results,
        tier_counts=tier_counts,
        promoted_discriminator=promoted_discriminator,
        completed_tier=completed_tier,
        total_elapsed_seconds=time.perf_counter() - total_started,
    )
    write_json(args.write_json, output_payload)
    write_json(state_path, output_payload)

    print()
    print("Atomic Anti-Sparse Search")
    print("=========================")
    if promoted_discriminator is None:
        print(
            f"- No discriminator survived through tier {completed_tier} "
            f"on {', '.join(ensemble_names)}."
        )
    else:
        print(
            f"- Promoted discriminator at tier {completed_tier}: "
            f"{promoted_discriminator['discriminator']['feature_subset_label']}."
        )
    print(f"- Output written to {args.write_json}.")


def resolve_ensemble_names(
    requested_names: list[str] | None,
    ladder_json: Path,
) -> tuple[str, ...]:
    if requested_names:
        return tuple(requested_names)
    if ladder_json.exists():
        ladder_payload = read_json(ladder_json)
        first_failure = ladder_payload.get("first_failure")
        neighbor = ladder_payload.get("neighboring_ensemble_beyond_failure")
        if first_failure is not None:
            names = [first_failure["ensemble_name"]]
            if neighbor:
                names.append(neighbor)
            return tuple(dict.fromkeys(names))
    return ANTI_SPARSE_DEFAULT_ENSEMBLES


def render_candidate_label(candidate_payload: dict[str, object] | None) -> str:
    if candidate_payload is None:
        return "none"
    return str(candidate_payload["feature_subset_label"])


def build_output_payload(
    *,
    started_at: str,
    completed_at: str | None,
    ensemble_names: tuple[str, ...],
    ladder_json: Path,
    feature_scope: str,
    summary_stage_records: dict[str, list[dict[str, object]]],
    support_stage_records: dict[str, list[dict[str, object]]],
    baseline_surfaces: dict[str, dict[str, object]],
    top_results: list[dict[str, object]],
    tier_counts: dict[str, object],
    promoted_discriminator: dict[str, object] | None,
    completed_tier: int,
    total_elapsed_seconds: float,
) -> dict[str, object]:
    return {
        "started_at": started_at,
        "completed_at": completed_at,
        "ensemble_names": list(ensemble_names),
        "ladder_json": str(ladder_json),
        "feature_scope": feature_scope,
        "summary_stage_records": summary_stage_records,
        "support_stage_records": support_stage_records,
        "baseline_surfaces": baseline_surfaces,
        "top_results": top_results,
        "tier_counts": tier_counts,
        "promoted_discriminator": promoted_discriminator,
        "completed_tier": completed_tier,
        "search_succeeded": promoted_discriminator is not None,
        "total_elapsed_seconds": round(total_elapsed_seconds, 6),
    }


if __name__ == "__main__":
    main()
