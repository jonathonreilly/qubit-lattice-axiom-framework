#!/usr/bin/env python3
"""Search polarity-aware discriminator bundles and validate survivors on the canonical ladder."""

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
    ANTI_SPARSE_DEFAULT_ENSEMBLES,
    ANTI_SPARSE_MAX_EXCLUDED_FRACTION,
    ATOMIC_ANCHOR_FEATURES,
    DEFAULT_CACHE_DIR,
    DEFAULT_OUTPUT_ROOT,
    NONVACUOUS_SPARSE_SUPPORT_FRACTION,
    SPARSE_FALLBACK_FEATURES,
    AtomicLaneEnsembleSummaryRow,
    PolarityDiscriminatorSpec,
    anti_sparse_feature_vocabulary,
    build_polarity_discriminator_spec,
    evaluate_atomic_lane_ensemble,
    evaluate_polarity_discriminator,
    evaluate_polarity_discriminator_family,
    load_feature_supports,
    read_json,
    search_polarity_discriminators,
    stage_record_table,
    summarize_sparse_surface,
    write_json,
)
from toy_event_physics import canonical_generated_ensemble_specs  # noqa: E402


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
        default=DEFAULT_OUTPUT_ROOT / "atomic_polarity_search.json",
        help="machine-readable polarity-search output path",
    )
    parser.add_argument(
        "--feature-scope",
        choices=("sparse", "full"),
        default="sparse",
        help="feature vocabulary used for the polarity atoms",
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
        "--canonical-candidates",
        type=int,
        default=25,
        help="validate up to this many pair-surviving candidates on the full canonical ladder",
    )
    parser.add_argument(
        "--max-excluded-fraction",
        type=float,
        default=ANTI_SPARSE_MAX_EXCLUDED_FRACTION,
        help="reject discriminators that exclude more than this fraction",
    )
    parser.add_argument(
        "--max-nonvacuous-support",
        type=float,
        default=NONVACUOUS_SPARSE_SUPPORT_FRACTION,
        help="ignore sparse fallback candidates at or above this support fraction",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    ensemble_names = resolve_ensemble_names(args.ensembles, args.ladder_json)
    print(
        "atomic polarity search started "
        f"{started_at} ensembles={ensemble_names} scope={args.feature_scope}",
        flush=True,
    )
    print(f"cache_dir={args.cache_dir}", flush=True)
    print(f"output_json={args.write_json}", flush=True)
    candidate_features = required_candidate_features(args.feature_scope)

    summary_rows_by_ensemble: dict[str, AtomicLaneEnsembleSummaryRow] = {}
    summary_stage_records: dict[str, list[dict[str, object]]] = {}
    support_payloads_by_ensemble: dict[str, dict[str, object]] = {}
    support_stage_records: dict[str, list[dict[str, object]]] = {}
    baseline_surfaces: dict[str, dict[str, object]] = {}

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
            search_stage="polarity-search",
            candidate_features=candidate_features,
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

    search_payload = search_polarity_discriminators(
        summary_rows_by_ensemble=summary_rows_by_ensemble,
        support_payloads_by_ensemble=support_payloads_by_ensemble,
        ensemble_names=ensemble_names,
        max_features=args.max_features,
        feature_scope=args.feature_scope,
        top_k=args.top_k,
        max_support_fraction=args.max_nonvacuous_support,
        max_excluded_fraction=args.max_excluded_fraction,
    )
    pair_passing = list(search_payload["passing_results"])
    print(
        f"pair search complete: "
        f"tested={sum(tier['tested'] for tier in search_payload['tier_counts'].values())} "
        f"pair_passed={len(pair_passing)}",
        flush=True,
    )

    canonical_ensembles = tuple(name for name, *_rest in canonical_generated_ensemble_specs())
    canonical_validation_results: list[dict[str, object]] = []
    retained_candidate: dict[str, object] | None = None
    if pair_passing:
        canonical_summary_rows_by_ensemble = dict(summary_rows_by_ensemble)
        canonical_support_payloads_by_ensemble = dict(support_payloads_by_ensemble)
        for pair_result in pair_passing[: args.canonical_candidates]:
            discriminator = payload_to_polarity_discriminator(pair_result["discriminator"])
            validation = validate_polarity_candidate_on_canonical_ladder(
                discriminator=discriminator,
                canonical_ensembles=canonical_ensembles,
                summary_rows_by_ensemble=canonical_summary_rows_by_ensemble,
                support_payloads_by_ensemble=canonical_support_payloads_by_ensemble,
                cache_dir=args.cache_dir,
                candidate_features=candidate_features,
                max_support_fraction=args.max_nonvacuous_support,
                max_excluded_fraction=args.max_excluded_fraction,
            )
            canonical_validation_results.append(validation)
            print(
                f"canonical validate {validation['discriminator']['feature_subset_label']}: "
                f"{'PASS' if validation['passes'] else 'FAIL'}",
                flush=True,
            )
            if retained_candidate is None and validation["passes"]:
                retained_candidate = validation

    finished_at = datetime.now().isoformat(timespec="seconds")
    output_payload = {
        "started_at": started_at,
        "completed_at": finished_at,
        "ensemble_names": list(ensemble_names),
        "ladder_json": str(args.ladder_json),
        "feature_scope": args.feature_scope,
        "summary_stage_records": summary_stage_records,
        "support_stage_records": support_stage_records,
        "baseline_surfaces": baseline_surfaces,
        "search": search_payload,
        "canonical_validation_results": canonical_validation_results,
        "retained_candidate": retained_candidate,
        "search_succeeded": retained_candidate is not None,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Polarity Search")
    print("======================")
    if retained_candidate is None:
        if pair_passing:
            print(
                f"- Pair-surviving candidates found on {', '.join(ensemble_names)}, "
                "but none survived the full canonical ladder."
            )
        else:
            print(f"- No pair-surviving discriminator found on {', '.join(ensemble_names)}.")
    else:
        print(
            f"- Retained candidate: {retained_candidate['discriminator']['feature_subset_label']}."
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


def required_candidate_features(feature_scope: str) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(
            (
                *ATOMIC_ANCHOR_FEATURES,
                *anti_sparse_feature_vocabulary(feature_scope),
                *SPARSE_FALLBACK_FEATURES,
            )
        )
    )


def render_candidate_label(candidate_payload: dict[str, object] | None) -> str:
    if candidate_payload is None:
        return "none"
    return str(candidate_payload["feature_subset_label"])


def payload_to_polarity_discriminator(
    payload: dict[str, object],
) -> PolarityDiscriminatorSpec:
    atom_specs = tuple(
        (str(atom["feature_name"]), str(atom["polarity"]))
        for atom in payload["atoms"]
    )
    return build_polarity_discriminator_spec(
        atom_specs,
        feature_scope=str(payload["feature_scope"]),
    )


def validate_polarity_candidate_on_canonical_ladder(
    *,
    discriminator: PolarityDiscriminatorSpec,
    canonical_ensembles: tuple[str, ...],
    summary_rows_by_ensemble: dict[str, AtomicLaneEnsembleSummaryRow],
    support_payloads_by_ensemble: dict[str, dict[str, object]],
    cache_dir: Path,
    candidate_features: tuple[str, ...],
    max_support_fraction: float,
    max_excluded_fraction: float,
) -> dict[str, object]:
    per_ensemble: list[dict[str, object]] = []
    first_failed: dict[str, object] | None = None
    for ensemble_name in canonical_ensembles:
        if ensemble_name not in summary_rows_by_ensemble:
            summary_row, _components, _records = evaluate_atomic_lane_ensemble(
                ensemble_name=ensemble_name,
                cache_dir=cache_dir,
                search_stage="current-family",
                use_cache=True,
            )
            summary_rows_by_ensemble[ensemble_name] = summary_row
        if ensemble_name not in support_payloads_by_ensemble:
            support_payload, _record = load_feature_supports(
                ensemble_name=ensemble_name,
                cache_dir=cache_dir,
                search_stage="polarity-search",
                candidate_features=candidate_features,
                use_cache=True,
            )
            support_payloads_by_ensemble[ensemble_name] = support_payload
        ensemble_result = evaluate_polarity_discriminator(
            discriminator=discriminator,
            summary_row=summary_rows_by_ensemble[ensemble_name],
            support_payload=support_payloads_by_ensemble[ensemble_name],
            max_support_fraction=max_support_fraction,
            max_excluded_fraction=max_excluded_fraction,
        )
        per_ensemble.append(ensemble_result)
        if not ensemble_result["passes"]:
            first_failed = ensemble_result
            break
    return {
        "discriminator": {
            "atoms": [atom.__dict__ for atom in discriminator.atoms],
            "feature_subset_label": discriminator.feature_subset_label,
            "abbreviated_label": discriminator.abbreviated_label,
            "tier": discriminator.tier,
            "feature_scope": discriminator.feature_scope,
        },
        "tested_ensembles": per_ensemble,
        "passes": first_failed is None and len(per_ensemble) == len(canonical_ensembles),
        "first_failed": first_failed,
        "score": {
            "tier": discriminator.tier,
            "max_excluded_fraction": max(
                result["excluded_fraction"] for result in per_ensemble
            ),
            "max_residual_fallback_fraction": max(
                result["score"]["residual_fallback_fraction"] for result in per_ensemble
            ),
            "min_nesting_floor": min(
                result["score"]["min_nesting_floor"] for result in per_ensemble
            ),
        },
    }


if __name__ == "__main__":
    main()
