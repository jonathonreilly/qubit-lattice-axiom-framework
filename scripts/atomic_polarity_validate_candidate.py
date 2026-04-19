#!/usr/bin/env python3
"""Validate one polarity discriminator on the full canonical atomic ladder."""

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
    ATOMIC_ANCHOR_FEATURES,
    DEFAULT_CACHE_DIR,
    DEFAULT_OUTPUT_ROOT,
    SPARSE_FALLBACK_FEATURES,
    AtomicLaneEnsembleSummaryRow,
    PolarityDiscriminatorSpec,
    anti_sparse_feature_vocabulary,
    build_polarity_discriminator_spec,
    evaluate_atomic_lane_ensemble,
    evaluate_polarity_discriminator,
    load_feature_supports,
    read_json,
    stage_record_table,
    write_json,
)
from toy_event_physics import canonical_generated_ensemble_specs  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pair-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_polarity_search_sparse_pair.json",
        help="pair-level polarity search output used to seed the default candidate",
    )
    parser.add_argument(
        "--candidate-label",
        help="explicit candidate label; defaults to the first pair-surviving candidate",
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
        default=DEFAULT_OUTPUT_ROOT / "atomic_polarity_candidate_validation.json",
        help="machine-readable validation output path",
    )
    parser.add_argument(
        "--feature-scope",
        choices=("sparse", "full"),
        default="sparse",
        help="feature vocabulary used to load support payloads",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="resume from an existing state file",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    state_path = args.write_json.with_suffix(".state.json")
    discriminator = resolve_discriminator(args.pair_json, args.candidate_label)
    candidate_features = required_candidate_features(args.feature_scope)
    canonical_ensembles = tuple(name for name, *_rest in canonical_generated_ensemble_specs())
    completed_results: list[dict[str, object]] = []
    summary_stage_records: dict[str, list[dict[str, object]]] = {}
    support_stage_records: dict[str, list[dict[str, object]]] = {}
    start_index = 0
    if args.resume and state_path.exists():
        previous_state = read_json(state_path)
        completed_results = list(previous_state.get("tested_ensembles", []))
        summary_stage_records = dict(previous_state.get("summary_stage_records", {}))
        support_stage_records = dict(previous_state.get("support_stage_records", {}))
        start_index = len(completed_results)

    print(
        "atomic polarity candidate validation started "
        f"{started_at} candidate={discriminator.feature_subset_label} "
        f"resume={args.resume}",
        flush=True,
    )
    print(f"cache_dir={args.cache_dir}", flush=True)
    print(f"output_json={args.write_json}", flush=True)

    for offset, ensemble_name in enumerate(canonical_ensembles[start_index:], start=start_index + 1):
        ensemble_started = time.perf_counter()
        print(
            f"[{offset}/{len(canonical_ensembles)}] validating {ensemble_name}",
            flush=True,
        )
        summary_row, _components, summary_records = evaluate_atomic_lane_ensemble(
            ensemble_name=ensemble_name,
            cache_dir=args.cache_dir,
            search_stage="current-family",
            use_cache=True,
        )
        support_payload, support_record = load_feature_supports(
            ensemble_name=ensemble_name,
            cache_dir=args.cache_dir,
            search_stage="polarity-search",
            candidate_features=candidate_features,
            use_cache=True,
        )
        ensemble_result = evaluate_polarity_discriminator(
            discriminator=discriminator,
            summary_row=summary_row,
            support_payload=support_payload,
        )
        completed_results.append(ensemble_result)
        summary_stage_records[ensemble_name] = stage_record_table(summary_records)
        support_stage_records[ensemble_name] = stage_record_table([support_record])
        print(
            f"[{offset}/{len(canonical_ensembles)}] finished {ensemble_name} "
            f"gate={'PASS' if ensemble_result['passes'] else 'FAIL'} "
            f"excluded={ensemble_result['excluded_fraction']:.3f} "
            f"fallback={ensemble_result['score']['residual_fallback_fraction']:.3f} "
            f"nesting={ensemble_result['score']['min_nesting_floor']:.3f} "
            f"fails={ensemble_result['failed_criteria']} "
            f"support_stage={'cache' if support_record.cache_hit else 'compute'}:{support_record.elapsed_seconds:.1f}s "
            f"elapsed={time.perf_counter() - ensemble_started:.1f}s",
            flush=True,
        )
        write_json(
            state_path,
            build_output_payload(
                started_at=started_at,
                completed_at=None,
                discriminator=discriminator,
                tested_ensembles=completed_results,
                summary_stage_records=summary_stage_records,
                support_stage_records=support_stage_records,
                total_elapsed_seconds=time.perf_counter() - total_started,
            ),
        )
        if not ensemble_result["passes"]:
            break

    finished_at = datetime.now().isoformat(timespec="seconds")
    output_payload = build_output_payload(
        started_at=started_at,
        completed_at=finished_at,
        discriminator=discriminator,
        tested_ensembles=completed_results,
        summary_stage_records=summary_stage_records,
        support_stage_records=support_stage_records,
        total_elapsed_seconds=time.perf_counter() - total_started,
    )
    write_json(args.write_json, output_payload)
    write_json(state_path, output_payload)

    print()
    print("Atomic Polarity Candidate Validation")
    print("====================================")
    if output_payload["passes"]:
        print(f"- Candidate retained across the full ladder: {discriminator.feature_subset_label}.")
    else:
        first_failed = output_payload["first_failed"]
        print(
            f"- Candidate failed at {first_failed['ensemble_name']} "
            f"with {first_failed['failed_criteria']}."
        )
    print(f"- Output written to {args.write_json}.")


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


def resolve_discriminator(
    pair_json: Path,
    candidate_label: str | None,
) -> PolarityDiscriminatorSpec:
    if not pair_json.exists() and candidate_label is None:
        raise SystemExit(
            f"pair-level result {pair_json} does not exist and no --candidate-label was supplied"
        )
    if candidate_label is None:
        payload = read_json(pair_json)
        passing_results = payload.get("search", {}).get("passing_results", [])
        if not passing_results:
            raise SystemExit(f"no pair-surviving candidates found in {pair_json}")
        candidate_payload = passing_results[0]["discriminator"]
        atom_specs = tuple(
            (str(atom["feature_name"]), str(atom["polarity"]))
            for atom in candidate_payload["atoms"]
        )
        return build_polarity_discriminator_spec(
            atom_specs,
            feature_scope=str(candidate_payload["feature_scope"]),
        )

    atom_specs: list[tuple[str, str]] = []
    for raw_atom in candidate_label.split(","):
        atom = raw_atom.strip()
        if atom.endswith(">0"):
            atom_specs.append((atom[:-2], "positive"))
        elif atom.endswith("=0"):
            atom_specs.append((atom[:-2], "zero"))
        else:
            raise SystemExit(
                f"could not parse atom {atom!r}; expected suffix >0 or =0"
            )
    return build_polarity_discriminator_spec(
        tuple(atom_specs),
        feature_scope="sparse",
    )


def build_output_payload(
    *,
    started_at: str,
    completed_at: str | None,
    discriminator: PolarityDiscriminatorSpec,
    tested_ensembles: list[dict[str, object]],
    summary_stage_records: dict[str, list[dict[str, object]]],
    support_stage_records: dict[str, list[dict[str, object]]],
    total_elapsed_seconds: float,
) -> dict[str, object]:
    first_failed = next((row for row in tested_ensembles if not row["passes"]), None)
    return {
        "started_at": started_at,
        "completed_at": completed_at,
        "discriminator": {
            "atoms": [atom.__dict__ for atom in discriminator.atoms],
            "feature_subset_label": discriminator.feature_subset_label,
            "abbreviated_label": discriminator.abbreviated_label,
            "tier": discriminator.tier,
            "feature_scope": discriminator.feature_scope,
        },
        "tested_ensembles": tested_ensembles,
        "summary_stage_records": summary_stage_records,
        "support_stage_records": support_stage_records,
        "passes": first_failed is None and len(tested_ensembles) == len(canonical_generated_ensemble_specs()),
        "first_failed": first_failed,
        "total_elapsed_seconds": round(total_elapsed_seconds, 6),
    }


if __name__ == "__main__":
    main()
