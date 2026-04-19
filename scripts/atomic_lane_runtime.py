#!/usr/bin/env python3
"""Shared runtime helpers for the atomic-lane science program."""

from __future__ import annotations

from dataclasses import asdict, dataclass, is_dataclass
from hashlib import sha256
import itertools
import json
from pathlib import Path
import sys
import time
from typing import Any, Callable, Iterable

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scipy import sparse  # noqa: E402

from scripts.frontier_bound_state_selection import (  # noqa: E402
    analyze_localization,
    build_nd_laplacian,
    count_bound_states,
    coupling_scan,
    coulomb_potential_nd,
)
from toy_event_physics import (  # noqa: E402
    AtomicLaneEnsembleSummaryRow,
    DegreeProfileFallbackRow,
    ExtendedAtomicRouteOverlapRow,
    ExtendedProxyRouteRow,
    ThresholdCoreOverlapRow,
    ThresholdCoreShellCaseAggregateRow,
    ThresholdCoreShellCaseRow,
    ThresholdCoreShellOffenderRow,
    ThresholdCoreShellRow,
    _best_extended_proxy_route_row,
    _named_overlap_row,
    abbreviate_feature_subset,
    atomic_lane_summary_row_from_components,
    canonical_generated_ensemble_specs,
    classify_extended_proxy_family,
    classify_extended_route_role,
    degree_basis_feature_names,
    degree_profile_fallback_benchmark,
    degree_profile_fallback_sets,
    extended_atomic_route_overlap_benchmark,
    extended_proxy_route_benchmark,
    generated_ensemble_spec,
    generated_prediction_node_sets,
    high_degree_threshold_feature_names,
    local_shape_feature_bundle,
    local_neighborhood_motif_feature_names,
    neighbor_leverage_threshold_feature_names,
    neighbor_reach_threshold_feature_names,
    soft_hub_exposure_feature_names,
    threshold_core_case_shell_flip_analysis,
    threshold_core_overlap_analysis,
    threshold_core_shell_mechanism_analysis,
    threshold_core_shell_offender_analysis,
    threshold_exposure_decomposition_feature_names,
)

DEFAULT_OUTPUT_ROOT = REPO_ROOT / "outputs" / "atomic_lane"
DEFAULT_CACHE_DIR = DEFAULT_OUTPUT_ROOT / "cache"
HELPER_VERSION_TAG = "atomic-lane-runtime-2026-04-19-v3"
ENSEMBLE_CACHE_STAGE = "ensemble-supports"

COMPACT_MATCH_THRESHOLD = 0.98
COMPACT_SUBSET_THRESHOLD = 0.99
NESTING_THRESHOLD = 0.98
MAX_ATOMIC_PARITY_SIZE = 3
NONVACUOUS_SPARSE_SUPPORT_FRACTION = 0.95
ANTI_SPARSE_MAX_EXCLUDED_FRACTION = 0.80
ANTI_SPARSE_DEFAULT_ENSEMBLES = ("default", "broader")

ATOMIC_ANCHOR_FEATURES = (
    "motif_low_degree_neighbor_fraction",
    "motif_pocket_adjacent_fraction",
    "motif_deep_pocket_adjacent_fraction",
)
SPARSE_FALLBACK_FEATURES = (
    "degree_0_fraction",
    "degree_1_fraction",
    "degree_2_fraction",
    "degree_7_fraction",
    "degree_8_fraction",
    "motif_mean_neighbor_degree",
    "motif_neighbor_degree_variation",
    "motif_two_hop_occupied_fraction",
    "motif_two_hop_open_fraction",
)
LOW_TARGET_FAMILIES = {"low-degree", "low-degree+sparse"}
POCKET_TARGET_FAMILIES = {"pocket", "pocket+hub", "pocket+sparse"}
DEEP_TARGET_FAMILIES = {"deep-pocket", "deep-pocket+hub"}
PURE_SPARSE_FAMILIES = {"sparse-structure", "degree-profile"}
BOUND_STATE_CONFIGS = (
    (2, (30, 30), 1.0),
    (3, (16, 16, 16), 2.0),
    (4, (10, 10, 10, 10), 3.0),
    (5, (5, 5, 5, 5, 5), 4.0),
)
MOTIF_FEATURE_INDEX = {
    feature_name: index
    for index, feature_name in enumerate(local_neighborhood_motif_feature_names())
}
HIGH_DEGREE_THRESHOLD_FEATURE_INDEX = {
    feature_name: index
    for index, feature_name in enumerate(high_degree_threshold_feature_names())
}
SOFT_HUB_EXPOSURE_FEATURE_INDEX = {
    feature_name: index
    for index, feature_name in enumerate(soft_hub_exposure_feature_names())
}
NEIGHBOR_REACH_FEATURE_INDEX = {
    feature_name: index
    for index, feature_name in enumerate(neighbor_reach_threshold_feature_names())
}
NEIGHBOR_LEVERAGE_FEATURE_INDEX = {
    feature_name: index
    for index, feature_name in enumerate(neighbor_leverage_threshold_feature_names())
}
THRESHOLD_EXPOSURE_FEATURE_INDEX = {
    feature_name: index
    for index, feature_name in enumerate(threshold_exposure_decomposition_feature_names())
}


@dataclass(frozen=True)
class CacheStageRecord:
    stage_name: str
    search_stage: str
    ensemble_name: str
    cache_key: str
    path: str
    cache_hit: bool
    elapsed_seconds: float


@dataclass(frozen=True)
class AtomicRouteCandidateSpec:
    feature_subset: tuple[str, ...]
    feature_subset_label: str
    abbreviated_label: str
    tier: int
    proxy_family: str
    route_role: str
    atomic_target: str | None
    contains_sparse: bool


@dataclass(frozen=True)
class AntiSparseDiscriminatorSpec:
    feature_subset: tuple[str, ...]
    feature_subset_label: str
    abbreviated_label: str
    tier: int
    feature_scope: str


@dataclass(frozen=True)
class PolarityAtomSpec:
    feature_name: str
    polarity: str
    label: str


@dataclass(frozen=True)
class PolarityDiscriminatorSpec:
    atoms: tuple[PolarityAtomSpec, ...]
    feature_subset_label: str
    abbreviated_label: str
    tier: int
    feature_scope: str


def canonical_atomic_lane_ensembles() -> tuple[str, ...]:
    return tuple(name for name, *_rest in canonical_generated_ensemble_specs())


def canonical_atomic_lane_index(ensemble_name: str) -> int:
    return canonical_atomic_lane_ensembles().index(ensemble_name)


def neighboring_stricter_ensemble(ensemble_name: str) -> str | None:
    names = canonical_atomic_lane_ensembles()
    index = names.index(ensemble_name)
    if index + 1 >= len(names):
        return None
    return names[index + 1]


def json_ready(value: Any) -> Any:
    if is_dataclass(value):
        return {key: json_ready(inner) for key, inner in asdict(value).items()}
    if isinstance(value, dict):
        return {str(key): json_ready(inner) for key, inner in sorted(value.items())}
    if isinstance(value, (list, tuple)):
        return [json_ready(inner) for inner in value]
    if isinstance(value, set):
        return [json_ready(inner) for inner in sorted(value)]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.floating):
        return float(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, (bool, int, float, str)) or value is None:
        return value
    return str(value)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(json_ready(payload), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def helper_version_hash(extra_paths: Iterable[Path] = ()) -> str:
    digest = sha256()
    digest.update(HELPER_VERSION_TAG.encode("utf-8"))
    base_paths = (
        REPO_ROOT / "toy_event_physics.py",
        Path(__file__).resolve(),
    )
    for path in (*base_paths, *tuple(extra_paths)):
        digest.update(path.read_bytes())
    return digest.hexdigest()[:16]


def atomic_lane_cache_key(
    *,
    ensemble_name: str,
    retained_weight: float,
    candidate_features: tuple[str, ...] = (),
    search_stage: str,
    helper_hash: str,
) -> str:
    payload = {
        "ensemble_name": ensemble_name,
        "retained_weight": retained_weight,
        "candidate_features": list(candidate_features),
        "search_stage": search_stage,
        "helper_hash": helper_hash,
    }
    return sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()[:20]


def _load_or_compute_stage(
    *,
    cache_dir: Path,
    ensemble_name: str,
    stage_name: str,
    search_stage: str,
    retained_weight: float,
    candidate_features: tuple[str, ...],
    compute_fn: Callable[[], Any],
    helper_hash: str,
    use_cache: bool = True,
) -> tuple[Any, CacheStageRecord]:
    cache_key = atomic_lane_cache_key(
        ensemble_name=ensemble_name,
        retained_weight=retained_weight,
        candidate_features=candidate_features,
        search_stage=f"{search_stage}:{stage_name}",
        helper_hash=helper_hash,
    )
    path = cache_dir / search_stage / ensemble_name / stage_name / f"{cache_key}.json"
    started = time.perf_counter()
    cache_hit = False
    resolved_path = path
    if use_cache and path.exists():
        payload = read_json(path)
        cache_hit = True
    elif use_cache and path.parent.exists():
        compatible_paths = sorted(
            path.parent.glob("*.json"),
            key=lambda candidate_path: candidate_path.stat().st_mtime,
            reverse=True,
        )
        if compatible_paths:
            resolved_path = compatible_paths[0]
            payload = read_json(resolved_path)
            cache_hit = True
        else:
            payload = {
                "stage_name": stage_name,
                "cache_key": cache_key,
                "payload": json_ready(compute_fn()),
            }
            write_json(path, payload)
    else:
        payload = {
            "stage_name": stage_name,
            "cache_key": cache_key,
            "payload": json_ready(compute_fn()),
        }
        write_json(path, payload)
    elapsed = time.perf_counter() - started
    return payload, CacheStageRecord(
        stage_name=stage_name,
        search_stage=search_stage,
        ensemble_name=ensemble_name,
        cache_key=cache_key,
        path=str(resolved_path),
        cache_hit=cache_hit,
        elapsed_seconds=elapsed,
    )


def _deserialize_row(cls: type[Any], payload: dict[str, Any]) -> Any:
    return cls(**payload)


def _deserialize_rows(cls: type[Any], payloads: Iterable[dict[str, Any]]) -> list[Any]:
    return [cls(**payload) for payload in payloads]


def stage_record_table(records: Iterable[CacheStageRecord]) -> list[dict[str, Any]]:
    return [asdict(record) for record in records]


def summarize_stage_records(records: Iterable[CacheStageRecord]) -> dict[str, Any]:
    records = list(records)
    return {
        "total_elapsed_seconds": sum(record.elapsed_seconds for record in records),
        "stage_elapsed_seconds": {
            record.stage_name: round(record.elapsed_seconds, 6) for record in records
        },
        "cache_hits": {
            record.stage_name: record.cache_hit for record in records
        },
    }


def evaluate_atomic_lane_ensemble(
    *,
    ensemble_name: str,
    cache_dir: Path,
    retained_weight: float = 1.0,
    mode_retained_weight: float | None = 1.0,
    search_stage: str = "current-family",
    use_cache: bool = True,
) -> tuple[
    AtomicLaneEnsembleSummaryRow,
    dict[str, Any],
    list[CacheStageRecord],
]:
    helper_hash = helper_version_hash()
    spec = generated_ensemble_spec(ensemble_name)
    active_ensemble = (spec,)
    records: list[CacheStageRecord] = []

    threshold_stage, record = _load_or_compute_stage(
        cache_dir=cache_dir,
        ensemble_name=ensemble_name,
        stage_name="threshold-core-overlap",
        search_stage=ENSEMBLE_CACHE_STAGE,
        retained_weight=retained_weight,
        candidate_features=(),
        helper_hash=helper_hash,
        use_cache=use_cache,
        compute_fn=lambda: {
            "row": asdict(
                threshold_core_overlap_analysis(
                    retained_weight=retained_weight,
                    mode_retained_weight=mode_retained_weight,
                    ensembles=active_ensemble,
                    include_models=False,
                )[0][0]
            ),
        },
    )
    records.append(record)

    support_stage, record = load_feature_supports(
        ensemble_name=ensemble_name,
        cache_dir=cache_dir,
        retained_weight=retained_weight,
        search_stage=ENSEMBLE_CACHE_STAGE,
        use_cache=use_cache,
    )
    records.append(record)

    threshold_row = _deserialize_row(ThresholdCoreOverlapRow, threshold_stage["payload"]["row"])
    low_candidate = build_candidate_spec((ATOMIC_ANCHOR_FEATURES[0],))
    pocket_candidate = build_candidate_spec((ATOMIC_ANCHOR_FEATURES[1],))
    deep_candidate = build_candidate_spec((ATOMIC_ANCHOR_FEATURES[2],))

    low_support = candidate_support_details(low_candidate, support_stage)
    pocket_support = candidate_support_details(pocket_candidate, support_stage)
    deep_support = candidate_support_details(deep_candidate, support_stage)
    low_set = low_support["support"]
    pocket_set = pocket_support["support"]
    deep_set = deep_support["support"]

    pocket_implies_low = len(pocket_set & low_set) / len(pocket_set) if pocket_set else 1.0
    deep_implies_pocket = len(deep_set & pocket_set) / len(deep_set) if deep_set else 1.0
    deep_implies_low = len(deep_set & low_set) / len(deep_set) if deep_set else 1.0

    fallback_candidate, fallback_support = best_sparse_fallback_candidate(support_stage)
    fallback_is_distinct = bool(
        fallback_candidate is not None
        and fallback_candidate.proxy_family in PURE_SPARSE_FAMILIES
        and fallback_support["support_fraction"]
        < max(
            low_support["support_fraction"],
            pocket_support["support_fraction"],
            deep_support["support_fraction"],
        )
    )
    failed_criteria: list[str] = []
    if threshold_row.ge6_share6_support_match_fraction < COMPACT_MATCH_THRESHOLD:
        failed_criteria.append("compact-ge6-share6")
    if threshold_row.ge7_subset_of_ge6_fraction < COMPACT_SUBSET_THRESHOLD:
        failed_criteria.append("compact-ge7-subset")
    if low_support["support_count"] == 0:
        failed_criteria.append("low-missing")
    if pocket_support["support_count"] == 0:
        failed_criteria.append("pocket-missing")
    if deep_support["support_count"] == 0:
        failed_criteria.append("deep-missing")
    if pocket_implies_low < NESTING_THRESHOLD:
        failed_criteria.append("pocket=>low")
    if deep_implies_pocket < NESTING_THRESHOLD:
        failed_criteria.append("deep=>pocket")
    if deep_implies_low < NESTING_THRESHOLD:
        failed_criteria.append("deep=>low")
    if not fallback_is_distinct:
        failed_criteria.append("fallback-leakage")

    summary_row = AtomicLaneEnsembleSummaryRow(
        ensemble_name=ensemble_name,
        graph_count=threshold_row.graph_count,
        total_nodes=threshold_row.total_nodes,
        compact_ge6_share6_match_fraction=threshold_row.ge6_share6_support_match_fraction,
        compact_ge7_subset_fraction=threshold_row.ge7_subset_of_ge6_fraction,
        compact_ge6_only_fraction=threshold_row.ge6_without_ge7_fraction,
        low_parity_size=1 if low_support["support_count"] > 0 else None,
        low_feature_subset=low_candidate.feature_subset_label,
        low_support_fraction=low_support["support_fraction"],
        pocket_parity_size=1 if pocket_support["support_count"] > 0 else None,
        pocket_feature_subset=pocket_candidate.feature_subset_label,
        pocket_support_fraction=pocket_support["support_fraction"],
        deep_parity_size=1 if deep_support["support_count"] > 0 else None,
        deep_feature_subset=deep_candidate.feature_subset_label,
        deep_support_fraction=deep_support["support_fraction"],
        pocket_implies_low=pocket_implies_low,
        deep_implies_pocket=deep_implies_pocket,
        deep_implies_low=deep_implies_low,
        fallback_parity_size=(
            fallback_candidate.tier if fallback_candidate is not None else None
        ),
        fallback_feature_subset=(
            fallback_candidate.feature_subset_label if fallback_candidate is not None else "-"
        ),
        fallback_proxy_family=(
            fallback_candidate.proxy_family if fallback_candidate is not None else "none"
        ),
        fallback_route_role=(
            fallback_candidate.route_role if fallback_candidate is not None else "none"
        ),
        max_atomic_parity_size=(
            max(1 if support["support_count"] > 0 else 0 for support in (low_support, pocket_support, deep_support))
            if any(support["support_count"] > 0 for support in (low_support, pocket_support, deep_support))
            else None
        ),
        atomic_chain_present=all(
            support["support_count"] > 0 for support in (low_support, pocket_support, deep_support)
        ),
        nesting_floor=min(pocket_implies_low, deep_implies_pocket, deep_implies_low),
        fallback_is_distinct=fallback_is_distinct,
        retained_passes=not failed_criteria,
        failed_criteria=", ".join(failed_criteria) if failed_criteria else "-",
    )
    components = {
        "threshold_row": asdict(threshold_row),
        "support_row_count": support_stage["payload"]["row_count"],
        "low_support": {
            "support_count": low_support["support_count"],
            "support_fraction": low_support["support_fraction"],
        },
        "pocket_support": {
            "support_count": pocket_support["support_count"],
            "support_fraction": pocket_support["support_fraction"],
        },
        "deep_support": {
            "support_count": deep_support["support_count"],
            "support_fraction": deep_support["support_fraction"],
        },
        "fallback_candidate": (
            asdict(fallback_candidate) if fallback_candidate is not None else None
        ),
        "fallback_support_fraction": fallback_support["support_fraction"],
    }
    return summary_row, components, records


def load_shell_mechanism_stages(
    *,
    ensemble_name: str,
    cache_dir: Path,
    retained_weight: float = 1.0,
    mode_retained_weight: float | None = 1.0,
    search_stage: str = "mechanism",
    use_cache: bool = True,
) -> tuple[
    ThresholdCoreShellRow,
    list[ThresholdCoreShellCaseRow],
    list[ThresholdCoreShellCaseAggregateRow],
    list[ThresholdCoreShellOffenderRow],
    list[CacheStageRecord],
]:
    helper_hash = helper_version_hash()
    spec = generated_ensemble_spec(ensemble_name)
    active_ensemble = (spec,)
    records: list[CacheStageRecord] = []

    shell_stage, record = _load_or_compute_stage(
        cache_dir=cache_dir,
        ensemble_name=ensemble_name,
        stage_name="threshold-core-shell",
        search_stage=search_stage,
        retained_weight=retained_weight,
        candidate_features=(),
        helper_hash=helper_hash,
        use_cache=use_cache,
        compute_fn=lambda: {
            "rows": [
                asdict(row)
                for row in threshold_core_shell_mechanism_analysis(ensembles=active_ensemble)
            ],
        },
    )
    records.append(record)

    case_stage, record = _load_or_compute_stage(
        cache_dir=cache_dir,
        ensemble_name=ensemble_name,
        stage_name="threshold-core-case-flips",
        search_stage=search_stage,
        retained_weight=retained_weight,
        candidate_features=(),
        helper_hash=helper_hash,
        use_cache=use_cache,
        compute_fn=lambda: _compute_case_stage_payload(
            retained_weight=retained_weight,
            mode_retained_weight=mode_retained_weight,
            active_ensemble=active_ensemble,
        ),
    )
    records.append(record)

    offender_stage, record = _load_or_compute_stage(
        cache_dir=cache_dir,
        ensemble_name=ensemble_name,
        stage_name="threshold-core-offenders",
        search_stage=search_stage,
        retained_weight=retained_weight,
        candidate_features=(),
        helper_hash=helper_hash,
        use_cache=use_cache,
        compute_fn=lambda: {
            "rows": [
                asdict(row)
                for row in threshold_core_shell_offender_analysis(
                    _deserialize_rows(
                        ThresholdCoreShellCaseRow,
                        case_stage["payload"]["case_rows"],
                    )
                )
            ],
        },
    )
    records.append(record)

    shell_row = _deserialize_row(ThresholdCoreShellRow, shell_stage["payload"]["rows"][0])
    case_rows = _deserialize_rows(ThresholdCoreShellCaseRow, case_stage["payload"]["case_rows"])
    aggregate_rows = _deserialize_rows(
        ThresholdCoreShellCaseAggregateRow,
        case_stage["payload"]["aggregate_rows"],
    )
    offender_rows = _deserialize_rows(
        ThresholdCoreShellOffenderRow,
        offender_stage["payload"]["rows"],
    )
    return shell_row, case_rows, aggregate_rows, offender_rows, records


def load_shell_summary_stage(
    *,
    ensemble_name: str,
    cache_dir: Path,
    retained_weight: float = 1.0,
    search_stage: str = "mechanism",
    use_cache: bool = True,
) -> tuple[ThresholdCoreShellRow, list[CacheStageRecord]]:
    helper_hash = helper_version_hash()
    spec = generated_ensemble_spec(ensemble_name)
    active_ensemble = (spec,)
    shell_stage, record = _load_or_compute_stage(
        cache_dir=cache_dir,
        ensemble_name=ensemble_name,
        stage_name="threshold-core-shell",
        search_stage=search_stage,
        retained_weight=retained_weight,
        candidate_features=(),
        helper_hash=helper_hash,
        use_cache=use_cache,
        compute_fn=lambda: {
            "rows": [
                asdict(row)
                for row in threshold_core_shell_mechanism_analysis(ensembles=active_ensemble)
            ],
        },
    )
    shell_row = _deserialize_row(ThresholdCoreShellRow, shell_stage["payload"]["rows"][0])
    return shell_row, [record]


def atomic_route_feature_vocabulary() -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(
            (
                *ATOMIC_ANCHOR_FEATURES,
                *tuple(
                    feature
                    for feature in local_neighborhood_motif_feature_names()
                    if feature not in set(ATOMIC_ANCHOR_FEATURES)
                ),
                *high_degree_threshold_feature_names(),
                *soft_hub_exposure_feature_names(),
                *neighbor_reach_threshold_feature_names(),
                *neighbor_leverage_threshold_feature_names(),
                *threshold_exposure_decomposition_feature_names(),
                *degree_basis_feature_names(),
            )
        )
    )


def generate_atomic_route_candidates(max_features: int = 3) -> list[AtomicRouteCandidateSpec]:
    vocabulary = atomic_route_feature_vocabulary()
    candidates: list[AtomicRouteCandidateSpec] = []
    for subset_size in range(1, max_features + 1):
        for feature_subset in itertools.combinations(vocabulary, subset_size):
            if subset_size > 1 and not any(
                feature in ATOMIC_ANCHOR_FEATURES for feature in feature_subset
            ):
                continue
            candidates.append(build_candidate_spec(feature_subset))
    candidates.sort(
        key=lambda candidate: (
            candidate.tier,
            0 if candidate.route_role == "atomic-standalone" else 1,
            1 if candidate.contains_sparse else 0,
            candidate.proxy_family,
            candidate.feature_subset_label,
        )
    )
    return candidates


def build_candidate_spec(feature_subset: tuple[str, ...]) -> AtomicRouteCandidateSpec:
    subset_label = ", ".join(feature_subset)
    proxy_family, _signature = classify_extended_proxy_family(subset_label)
    route_role = classify_extended_route_role(subset_label)
    target: str | None
    if proxy_family in LOW_TARGET_FAMILIES:
        target = "low"
    elif proxy_family in POCKET_TARGET_FAMILIES:
        target = "pocket"
    elif proxy_family in DEEP_TARGET_FAMILIES:
        target = "deep"
    else:
        target = None
    return AtomicRouteCandidateSpec(
        feature_subset=feature_subset,
        feature_subset_label=subset_label,
        abbreviated_label=abbreviate_feature_subset(subset_label),
        tier=len(feature_subset),
        proxy_family=proxy_family,
        route_role=route_role,
        atomic_target=target,
        contains_sparse=proxy_family in PURE_SPARSE_FAMILIES or "sparse" in proxy_family,
    )


def generate_sparse_fallback_candidates(max_features: int = 3) -> list[AtomicRouteCandidateSpec]:
    candidates: list[AtomicRouteCandidateSpec] = []
    for subset_size in range(1, max_features + 1):
        for feature_subset in itertools.combinations(SPARSE_FALLBACK_FEATURES, subset_size):
            candidate = build_candidate_spec(feature_subset)
            if candidate.proxy_family not in PURE_SPARSE_FAMILIES and not candidate.contains_sparse:
                continue
            candidates.append(candidate)
    candidates.sort(
        key=lambda candidate: (
            candidate.tier,
            candidate.proxy_family,
            candidate.feature_subset_label,
        )
    )
    return candidates


def anti_sparse_feature_vocabulary(feature_scope: str = "sparse") -> tuple[str, ...]:
    if feature_scope == "sparse":
        return SPARSE_FALLBACK_FEATURES
    if feature_scope == "full":
        return tuple(
            dict.fromkeys(
                (
                    *SPARSE_FALLBACK_FEATURES,
                    *atomic_route_feature_vocabulary(),
                )
            )
        )
    raise ValueError(f"unknown anti-sparse feature scope {feature_scope!r}")


def generate_anti_sparse_discriminator_candidates(
    *,
    max_features: int = 3,
    feature_scope: str = "sparse",
) -> list[AntiSparseDiscriminatorSpec]:
    vocabulary = anti_sparse_feature_vocabulary(feature_scope)
    candidates: list[AntiSparseDiscriminatorSpec] = []
    for subset_size in range(1, max_features + 1):
        for feature_subset in itertools.combinations(vocabulary, subset_size):
            subset_label = ", ".join(feature_subset)
            candidates.append(
                AntiSparseDiscriminatorSpec(
                    feature_subset=feature_subset,
                    feature_subset_label=subset_label,
                    abbreviated_label=abbreviate_feature_subset(subset_label),
                    tier=subset_size,
                    feature_scope=feature_scope,
                )
            )
    candidates.sort(
        key=lambda candidate: (
            candidate.tier,
            candidate.feature_subset_label,
        )
    )
    return candidates


def load_feature_supports(
    *,
    ensemble_name: str,
    cache_dir: Path,
    retained_weight: float = 1.0,
    search_stage: str = "search",
    candidate_features: tuple[str, ...] | None = None,
    use_cache: bool = True,
) -> tuple[dict[str, Any], CacheStageRecord]:
    if candidate_features is None:
        candidate_features = atomic_route_feature_vocabulary()
    helper_hash = helper_version_hash()
    spec = generated_ensemble_spec(ensemble_name)
    _name, geometry_variant_limit, procedural_variant_limit, procedural_styles = spec
    return _load_or_compute_stage(
        cache_dir=cache_dir,
        ensemble_name=ensemble_name,
        stage_name="candidate-feature-supports",
        search_stage=ENSEMBLE_CACHE_STAGE,
        retained_weight=retained_weight,
        candidate_features=candidate_features,
        helper_hash=helper_hash,
        use_cache=use_cache,
        compute_fn=lambda: _compute_feature_support_payload(
            geometry_variant_limit=geometry_variant_limit,
            procedural_variant_limit=procedural_variant_limit,
            procedural_styles=procedural_styles,
            retained_weight=retained_weight,
            candidate_features=candidate_features,
        ),
    )


def _compute_feature_support_payload(
    *,
    geometry_variant_limit: int,
    procedural_variant_limit: int,
    procedural_styles: tuple[str, ...],
    retained_weight: float,
    candidate_features: tuple[str, ...],
) -> dict[str, Any]:
    graph_rows = generated_prediction_node_sets(
        geometry_variant_limit=geometry_variant_limit,
        procedural_variant_limit=procedural_variant_limit,
        procedural_styles=procedural_styles,
    )
    support_map: dict[str, list[int]] = {}
    for feature_name in candidate_features:
        support_map[feature_name] = []
    for index, source_name in enumerate(sorted(graph_rows)):
        _dataset_name, nodes, wrap_y = graph_rows[source_name]
        (
            _boundary_fraction,
            _pocket_fraction,
            _boundary_roughness,
            _deep_pocket_fraction,
            degree_fractions,
            motif_fractions,
            _high_degree_decomposition,
            high_degree_threshold_fractions,
            soft_hub_exposure,
            neighbor_reach_threshold_fractions,
            neighbor_leverage_threshold_fractions,
            threshold_exposure_decomposition,
        ) = local_shape_feature_bundle(nodes, wrap_y=wrap_y)
        for feature_name in candidate_features:
            if (
                _local_shape_feature_value(
                    feature_name,
                    degree_fractions=degree_fractions,
                    motif_fractions=motif_fractions,
                    high_degree_threshold_fractions=high_degree_threshold_fractions,
                    soft_hub_exposure=soft_hub_exposure,
                    neighbor_reach_threshold_fractions=neighbor_reach_threshold_fractions,
                    neighbor_leverage_threshold_fractions=neighbor_leverage_threshold_fractions,
                    threshold_exposure_decomposition=threshold_exposure_decomposition,
                )
                > 0.0
            ):
                support_map[feature_name].append(index)
    return {
        "row_count": len(graph_rows),
        "feature_supports": support_map,
    }


def _local_shape_feature_value(
    feature_name: str,
    *,
    degree_fractions: tuple[float, ...],
    motif_fractions: tuple[float, ...],
    high_degree_threshold_fractions: tuple[float, ...],
    soft_hub_exposure: tuple[float, ...],
    neighbor_reach_threshold_fractions: tuple[float, ...],
    neighbor_leverage_threshold_fractions: tuple[float, ...],
    threshold_exposure_decomposition: tuple[float, ...],
) -> float:
    if feature_name.startswith("degree_") and feature_name.endswith("_fraction"):
        degree = int(feature_name[len("degree_") : -len("_fraction")])
        return degree_fractions[degree]
    motif_index = MOTIF_FEATURE_INDEX.get(feature_name)
    if motif_index is not None:
        return motif_fractions[motif_index]
    high_degree_index = HIGH_DEGREE_THRESHOLD_FEATURE_INDEX.get(feature_name)
    if high_degree_index is not None:
        return high_degree_threshold_fractions[high_degree_index]
    soft_hub_index = SOFT_HUB_EXPOSURE_FEATURE_INDEX.get(feature_name)
    if soft_hub_index is not None:
        return soft_hub_exposure[soft_hub_index]
    neighbor_reach_index = NEIGHBOR_REACH_FEATURE_INDEX.get(feature_name)
    if neighbor_reach_index is not None:
        return neighbor_reach_threshold_fractions[neighbor_reach_index]
    neighbor_leverage_index = NEIGHBOR_LEVERAGE_FEATURE_INDEX.get(feature_name)
    if neighbor_leverage_index is not None:
        return neighbor_leverage_threshold_fractions[neighbor_leverage_index]
    threshold_exposure_index = THRESHOLD_EXPOSURE_FEATURE_INDEX.get(feature_name)
    if threshold_exposure_index is not None:
        return threshold_exposure_decomposition[threshold_exposure_index]
    raise ValueError(f"unsupported support feature {feature_name!r}")


def candidate_support_details(
    candidate: AtomicRouteCandidateSpec,
    support_payload: dict[str, Any],
) -> dict[str, Any]:
    row_count = int(support_payload["payload"]["row_count"])
    support = support_from_feature_subset(
        candidate.feature_subset,
        support_payload,
        combination_mode="intersection",
    )
    return {
        "support": support,
        "support_count": len(support),
        "support_fraction": len(support) / max(1, row_count),
        "row_count": row_count,
    }


def support_from_feature_subset(
    feature_subset: tuple[str, ...],
    support_payload: dict[str, Any],
    *,
    combination_mode: str = "intersection",
) -> set[int]:
    feature_supports = support_payload["payload"]["feature_supports"]
    support_sets = [
        set(feature_supports.get(feature_name, []))
        for feature_name in feature_subset
    ]
    if not support_sets:
        return set()
    if combination_mode == "intersection":
        return set.intersection(*support_sets)
    if combination_mode == "union":
        return set.union(*support_sets)
    raise ValueError(f"unsupported combination_mode {combination_mode!r}")


def best_sparse_fallback_candidate(
    support_payload: dict[str, Any],
    *,
    candidates: Iterable[AtomicRouteCandidateSpec] | None = None,
    excluded_rows: set[int] | None = None,
    max_support_fraction: float | None = None,
) -> tuple[AtomicRouteCandidateSpec | None, dict[str, Any]]:
    best_candidate: AtomicRouteCandidateSpec | None = None
    row_count = int(support_payload["payload"]["row_count"])
    if excluded_rows is None:
        excluded_rows = set()
    residual_row_count = max(1, row_count - len(excluded_rows))
    best_support = {
        "support": set(),
        "support_count": 0,
        "support_fraction": 0.0,
        "row_count": residual_row_count,
    }
    candidate_iterable = (
        list(candidates)
        if candidates is not None
        else generate_sparse_fallback_candidates()
    )
    for candidate in candidate_iterable:
        support = candidate_support_details(candidate, support_payload)
        if excluded_rows:
            residual_support = support["support"] - excluded_rows
            support = {
                "support": residual_support,
                "support_count": len(residual_support),
                "support_fraction": len(residual_support) / residual_row_count,
                "row_count": residual_row_count,
            }
        if support["support_count"] == 0:
            continue
        if max_support_fraction is not None and support["support_fraction"] >= max_support_fraction:
            continue
        if best_candidate is None or (
            support["support_fraction"],
            support["support_count"],
            -candidate.tier,
            candidate.proxy_family,
            candidate.feature_subset_label,
        ) > (
            best_support["support_fraction"],
            best_support["support_count"],
            -(best_candidate.tier if best_candidate is not None else 99),
            best_candidate.proxy_family if best_candidate is not None else "",
            best_candidate.feature_subset_label if best_candidate is not None else "",
        ):
            best_candidate = candidate
            best_support = support
    return best_candidate, best_support


def support_overlap_summary(
    *,
    left_support: set[int],
    right_support: set[int],
    row_count: int,
    left_label: str,
    right_label: str,
) -> dict[str, Any]:
    intersection = left_support & right_support
    left_only = left_support - right_support
    right_only = right_support - left_support
    return {
        f"{left_label}_count": len(left_support),
        f"{right_label}_count": len(right_support),
        "intersection_count": len(intersection),
        f"{left_label}_implies_{right_label}": (
            len(intersection) / len(left_support) if left_support else 1.0
        ),
        f"{right_label}_implies_{left_label}": (
            len(intersection) / len(right_support) if right_support else 1.0
        ),
        f"{left_label}_only_fraction": len(left_only) / max(1, row_count),
        f"{right_label}_only_fraction": len(right_only) / max(1, row_count),
    }


def summarize_sparse_surface(
    *,
    support_payload: dict[str, Any],
    excluded_rows: set[int] | None = None,
    max_support_fraction: float = NONVACUOUS_SPARSE_SUPPORT_FRACTION,
) -> dict[str, Any]:
    if excluded_rows is None:
        excluded_rows = set()
    row_count = int(support_payload["payload"]["row_count"])
    residual_row_count = max(1, row_count - len(excluded_rows))
    low_set = candidate_support_details(
        build_candidate_spec((ATOMIC_ANCHOR_FEATURES[0],)),
        support_payload,
    )["support"] - excluded_rows
    pocket_set = candidate_support_details(
        build_candidate_spec((ATOMIC_ANCHOR_FEATURES[1],)),
        support_payload,
    )["support"] - excluded_rows
    deep_set = candidate_support_details(
        build_candidate_spec((ATOMIC_ANCHOR_FEATURES[2],)),
        support_payload,
    )["support"] - excluded_rows
    atomic_union = low_set | pocket_set | deep_set
    raw_candidate, raw_support = best_sparse_fallback_candidate(
        support_payload,
        excluded_rows=excluded_rows,
    )
    nonvacuous_candidate, nonvacuous_support = best_sparse_fallback_candidate(
        support_payload,
        excluded_rows=excluded_rows,
        max_support_fraction=max_support_fraction,
    )
    summary = {
        "excluded_count": len(excluded_rows),
        "excluded_fraction": len(excluded_rows) / max(1, row_count),
        "residual_row_count": residual_row_count,
        "atomic_union_count": len(atomic_union),
        "atomic_union_fraction": len(atomic_union) / residual_row_count,
        "raw_fallback_candidate": (
            asdict(raw_candidate) if raw_candidate is not None else None
        ),
        "raw_fallback_support_fraction": raw_support["support_fraction"],
        "nonvacuous_fallback_candidate": (
            asdict(nonvacuous_candidate) if nonvacuous_candidate is not None else None
        ),
        "nonvacuous_fallback_support_fraction": nonvacuous_support["support_fraction"],
    }
    if raw_candidate is not None:
        summary["raw_overlap"] = support_overlap_summary(
            left_support=raw_support["support"],
            right_support=atomic_union,
            row_count=residual_row_count,
            left_label="fallback",
            right_label="atomic_union",
        )
    if nonvacuous_candidate is not None:
        summary["nonvacuous_overlap"] = support_overlap_summary(
            left_support=nonvacuous_support["support"],
            right_support=atomic_union,
            row_count=residual_row_count,
            left_label="fallback",
            right_label="atomic_union",
        )
    return summary


def evaluate_anti_sparse_discriminator(
    *,
    discriminator: AntiSparseDiscriminatorSpec,
    summary_row: AtomicLaneEnsembleSummaryRow,
    support_payload: dict[str, Any],
    max_support_fraction: float = NONVACUOUS_SPARSE_SUPPORT_FRACTION,
    max_excluded_fraction: float = ANTI_SPARSE_MAX_EXCLUDED_FRACTION,
) -> dict[str, Any]:
    row_count = int(support_payload["payload"]["row_count"])
    low_candidate = build_candidate_spec((ATOMIC_ANCHOR_FEATURES[0],))
    pocket_candidate = build_candidate_spec((ATOMIC_ANCHOR_FEATURES[1],))
    deep_candidate = build_candidate_spec((ATOMIC_ANCHOR_FEATURES[2],))
    low_baseline = candidate_support_details(low_candidate, support_payload)["support"]
    pocket_baseline = candidate_support_details(pocket_candidate, support_payload)["support"]
    deep_baseline = candidate_support_details(deep_candidate, support_payload)["support"]
    excluded_rows = support_from_feature_subset(
        discriminator.feature_subset,
        support_payload,
        combination_mode="union",
    )
    residual_row_count = max(1, row_count - len(excluded_rows))
    low_residual = low_baseline - excluded_rows
    pocket_residual = pocket_baseline - excluded_rows
    deep_residual = deep_baseline - excluded_rows
    atomic_union_residual = low_residual | pocket_residual | deep_residual
    pocket_implies_low = (
        len(pocket_residual & low_residual) / len(pocket_residual)
        if pocket_residual
        else 1.0
    )
    deep_implies_pocket = (
        len(deep_residual & pocket_residual) / len(deep_residual)
        if deep_residual
        else 1.0
    )
    deep_implies_low = (
        len(deep_residual & low_residual) / len(deep_residual)
        if deep_residual
        else 1.0
    )
    sparse_surface = summarize_sparse_surface(
        support_payload=support_payload,
        excluded_rows=excluded_rows,
        max_support_fraction=max_support_fraction,
    )
    nonvacuous_overlap = sparse_surface.get("nonvacuous_overlap")
    residual_fallback_fraction = sparse_surface["nonvacuous_fallback_support_fraction"]
    residual_deep_fraction = len(deep_residual) / residual_row_count
    failed_criteria: list[str] = []
    if summary_row.compact_ge6_share6_match_fraction < COMPACT_MATCH_THRESHOLD:
        failed_criteria.append("compact-ge6-share6")
    if summary_row.compact_ge7_subset_fraction < COMPACT_SUBSET_THRESHOLD:
        failed_criteria.append("compact-ge7-subset")
    excluded_fraction = len(excluded_rows) / max(1, row_count)
    if excluded_fraction > max_excluded_fraction:
        failed_criteria.append("exclusion-too-large")
    if not low_residual:
        failed_criteria.append("low-residual-missing")
    if not pocket_residual:
        failed_criteria.append("pocket-residual-missing")
    if not deep_residual:
        failed_criteria.append("deep-residual-missing")
    if pocket_implies_low < NESTING_THRESHOLD:
        failed_criteria.append("pocket=>low")
    if deep_implies_pocket < NESTING_THRESHOLD:
        failed_criteria.append("deep=>pocket")
    if deep_implies_low < NESTING_THRESHOLD:
        failed_criteria.append("deep=>low")
    if sparse_surface["nonvacuous_fallback_candidate"] is None:
        fallback_is_distinct = True
    else:
        fallback_is_distinct = bool(
            residual_fallback_fraction < residual_deep_fraction
            and nonvacuous_overlap is not None
            and nonvacuous_overlap["fallback_implies_atomic_union"] < NESTING_THRESHOLD
            and nonvacuous_overlap["atomic_union_implies_fallback"] < NESTING_THRESHOLD
        )
    if not fallback_is_distinct:
        failed_criteria.append("fallback-embedded")
    return {
        "discriminator": asdict(discriminator),
        "ensemble_name": summary_row.ensemble_name,
        "excluded_count": len(excluded_rows),
        "excluded_fraction": excluded_fraction,
        "residual_row_count": residual_row_count,
        "low_support_fraction": len(low_residual) / residual_row_count,
        "pocket_support_fraction": len(pocket_residual) / residual_row_count,
        "deep_support_fraction": residual_deep_fraction,
        "pocket_implies_low": pocket_implies_low,
        "deep_implies_pocket": deep_implies_pocket,
        "deep_implies_low": deep_implies_low,
        "fallback_is_distinct": fallback_is_distinct,
        "sparse_surface": sparse_surface,
        "passes": not failed_criteria,
        "failed_criteria": failed_criteria,
        "score": {
            "tier": discriminator.tier,
            "excluded_fraction": excluded_fraction,
            "residual_fallback_fraction": residual_fallback_fraction,
            "min_nesting_floor": min(
                pocket_implies_low,
                deep_implies_pocket,
                deep_implies_low,
            ),
        },
    }


def search_anti_sparse_discriminators(
    *,
    summary_rows_by_ensemble: dict[str, AtomicLaneEnsembleSummaryRow],
    support_payloads_by_ensemble: dict[str, dict[str, Any]],
    ensemble_names: tuple[str, ...],
    max_features: int = 3,
    feature_scope: str = "sparse",
    top_k: int = 25,
    start_tier: int = 1,
    initial_top_results: list[dict[str, Any]] | None = None,
    initial_tier_counts: dict[str, Any] | None = None,
    initial_promoted_discriminator: dict[str, Any] | None = None,
    max_support_fraction: float = NONVACUOUS_SPARSE_SUPPORT_FRACTION,
    max_excluded_fraction: float = ANTI_SPARSE_MAX_EXCLUDED_FRACTION,
) -> dict[str, Any]:
    candidates = generate_anti_sparse_discriminator_candidates(
        max_features=max_features,
        feature_scope=feature_scope,
    )
    promoted_discriminator = initial_promoted_discriminator
    top_results: list[dict[str, Any]] = list(initial_top_results or [])
    tier_counts: dict[str, Any] = dict(initial_tier_counts or {})
    for tier in range(start_tier, max_features + 1):
        tier_candidates = [candidate for candidate in candidates if candidate.tier == tier]
        tested = 0
        passed = 0
        tier_results: list[dict[str, Any]] = []
        for discriminator in tier_candidates:
            tested += 1
            per_ensemble: list[dict[str, Any]] = []
            first_failed: dict[str, Any] | None = None
            for ensemble_name in ensemble_names:
                result = evaluate_anti_sparse_discriminator(
                    discriminator=discriminator,
                    summary_row=summary_rows_by_ensemble[ensemble_name],
                    support_payload=support_payloads_by_ensemble[ensemble_name],
                    max_support_fraction=max_support_fraction,
                    max_excluded_fraction=max_excluded_fraction,
                )
                per_ensemble.append(result)
                if first_failed is None and not result["passes"]:
                    first_failed = result
            aggregate_result = {
                "discriminator": asdict(discriminator),
                "tested_ensembles": per_ensemble,
                "passes": all(result["passes"] for result in per_ensemble),
                "first_failed": first_failed,
                "score": {
                    "tier": discriminator.tier,
                    "max_excluded_fraction": max(
                        result["excluded_fraction"] for result in per_ensemble
                    ),
                    "max_residual_fallback_fraction": max(
                        result["score"]["residual_fallback_fraction"]
                        for result in per_ensemble
                    ),
                    "min_nesting_floor": min(
                        result["score"]["min_nesting_floor"] for result in per_ensemble
                    ),
                },
            }
            if aggregate_result["passes"]:
                passed += 1
                if promoted_discriminator is None:
                    promoted_discriminator = aggregate_result
            tier_results.append(aggregate_result)
        tier_results.sort(
            key=lambda result: (
                0 if result["passes"] else 1,
                result["score"]["tier"],
                result["score"]["max_excluded_fraction"],
                result["score"]["max_residual_fallback_fraction"],
                -result["score"]["min_nesting_floor"],
                result["discriminator"]["feature_subset_label"],
            )
        )
        tier_counts[f"tier_{tier}"] = {
            "tested": tested,
            "passed": passed,
        }
        top_results.extend(tier_results[:top_k])
        top_results.sort(
            key=lambda result: (
                0 if result["passes"] else 1,
                result["score"]["tier"],
                result["score"]["max_excluded_fraction"],
                result["score"]["max_residual_fallback_fraction"],
                -result["score"]["min_nesting_floor"],
                result["discriminator"]["feature_subset_label"],
            )
        )
        top_results = top_results[:top_k]
        if promoted_discriminator is not None:
            break
    return {
        "ensemble_names": list(ensemble_names),
        "feature_scope": feature_scope,
        "promoted_discriminator": promoted_discriminator,
        "top_results": top_results,
        "tier_counts": tier_counts,
    }


def polarity_atom_label(feature_name: str, polarity: str) -> str:
    if polarity == "positive":
        return f"{feature_name}>0"
    if polarity == "zero":
        return f"{feature_name}=0"
    raise ValueError(f"unsupported polarity {polarity!r}")


def build_polarity_discriminator_spec(
    atom_specs: tuple[tuple[str, str], ...],
    *,
    feature_scope: str,
) -> PolarityDiscriminatorSpec:
    atoms = tuple(
        PolarityAtomSpec(
            feature_name=feature_name,
            polarity=polarity,
            label=polarity_atom_label(feature_name, polarity),
        )
        for feature_name, polarity in atom_specs
    )
    label = ", ".join(atom.label for atom in atoms)
    return PolarityDiscriminatorSpec(
        atoms=atoms,
        feature_subset_label=label,
        abbreviated_label=abbreviate_feature_subset(label),
        tier=len(atoms),
        feature_scope=feature_scope,
    )


def generate_polarity_discriminator_candidates(
    *,
    max_features: int = 3,
    feature_scope: str = "sparse",
    polarities: tuple[str, ...] = ("positive", "zero"),
) -> list[PolarityDiscriminatorSpec]:
    vocabulary = anti_sparse_feature_vocabulary(feature_scope)
    candidates: list[PolarityDiscriminatorSpec] = []
    for subset_size in range(1, max_features + 1):
        for feature_subset in itertools.combinations(vocabulary, subset_size):
            for polarity_subset in itertools.product(polarities, repeat=subset_size):
                atom_specs = tuple(zip(feature_subset, polarity_subset, strict=True))
                candidates.append(
                    build_polarity_discriminator_spec(
                        atom_specs,
                        feature_scope=feature_scope,
                    )
                )
    candidates.sort(
        key=lambda candidate: (
            candidate.tier,
            candidate.feature_subset_label,
        )
    )
    return candidates


def polarity_atom_support(
    atom: PolarityAtomSpec,
    support_payload: dict[str, Any],
) -> set[int]:
    row_count = int(support_payload["payload"]["row_count"])
    positive_support = set(
        support_payload["payload"]["feature_supports"].get(atom.feature_name, [])
    )
    if atom.polarity == "positive":
        return positive_support
    if atom.polarity == "zero":
        return set(range(row_count)) - positive_support
    raise ValueError(f"unsupported polarity {atom.polarity!r}")


def evaluate_polarity_discriminator(
    *,
    discriminator: PolarityDiscriminatorSpec,
    summary_row: AtomicLaneEnsembleSummaryRow,
    support_payload: dict[str, Any],
    max_support_fraction: float = NONVACUOUS_SPARSE_SUPPORT_FRACTION,
    max_excluded_fraction: float = ANTI_SPARSE_MAX_EXCLUDED_FRACTION,
) -> dict[str, Any]:
    row_count = int(support_payload["payload"]["row_count"])
    low_candidate = build_candidate_spec((ATOMIC_ANCHOR_FEATURES[0],))
    pocket_candidate = build_candidate_spec((ATOMIC_ANCHOR_FEATURES[1],))
    deep_candidate = build_candidate_spec((ATOMIC_ANCHOR_FEATURES[2],))
    low_baseline = candidate_support_details(low_candidate, support_payload)["support"]
    pocket_baseline = candidate_support_details(pocket_candidate, support_payload)["support"]
    deep_baseline = candidate_support_details(deep_candidate, support_payload)["support"]
    excluded_rows = set().union(
        *(polarity_atom_support(atom, support_payload) for atom in discriminator.atoms)
    )
    residual_row_count = max(1, row_count - len(excluded_rows))
    low_residual = low_baseline - excluded_rows
    pocket_residual = pocket_baseline - excluded_rows
    deep_residual = deep_baseline - excluded_rows
    pocket_implies_low = (
        len(pocket_residual & low_residual) / len(pocket_residual)
        if pocket_residual
        else 1.0
    )
    deep_implies_pocket = (
        len(deep_residual & pocket_residual) / len(deep_residual)
        if deep_residual
        else 1.0
    )
    deep_implies_low = (
        len(deep_residual & low_residual) / len(deep_residual)
        if deep_residual
        else 1.0
    )
    sparse_surface = summarize_sparse_surface(
        support_payload=support_payload,
        excluded_rows=excluded_rows,
        max_support_fraction=max_support_fraction,
    )
    nonvacuous_overlap = sparse_surface.get("nonvacuous_overlap")
    residual_fallback_fraction = sparse_surface["nonvacuous_fallback_support_fraction"]
    residual_deep_fraction = len(deep_residual) / residual_row_count
    failed_criteria: list[str] = []
    if summary_row.compact_ge6_share6_match_fraction < COMPACT_MATCH_THRESHOLD:
        failed_criteria.append("compact-ge6-share6")
    if summary_row.compact_ge7_subset_fraction < COMPACT_SUBSET_THRESHOLD:
        failed_criteria.append("compact-ge7-subset")
    excluded_fraction = len(excluded_rows) / max(1, row_count)
    if excluded_fraction > max_excluded_fraction:
        failed_criteria.append("exclusion-too-large")
    if not low_residual:
        failed_criteria.append("low-residual-missing")
    if not pocket_residual:
        failed_criteria.append("pocket-residual-missing")
    if not deep_residual:
        failed_criteria.append("deep-residual-missing")
    if pocket_implies_low < NESTING_THRESHOLD:
        failed_criteria.append("pocket=>low")
    if deep_implies_pocket < NESTING_THRESHOLD:
        failed_criteria.append("deep=>pocket")
    if deep_implies_low < NESTING_THRESHOLD:
        failed_criteria.append("deep=>low")
    if sparse_surface["nonvacuous_fallback_candidate"] is None:
        fallback_is_distinct = True
    else:
        fallback_is_distinct = bool(
            residual_fallback_fraction < residual_deep_fraction
            and nonvacuous_overlap is not None
            and nonvacuous_overlap["fallback_implies_atomic_union"] < NESTING_THRESHOLD
            and nonvacuous_overlap["atomic_union_implies_fallback"] < NESTING_THRESHOLD
        )
    if not fallback_is_distinct:
        failed_criteria.append("fallback-embedded")
    return {
        "discriminator": asdict(discriminator),
        "ensemble_name": summary_row.ensemble_name,
        "excluded_count": len(excluded_rows),
        "excluded_fraction": excluded_fraction,
        "residual_row_count": residual_row_count,
        "low_support_fraction": len(low_residual) / residual_row_count,
        "pocket_support_fraction": len(pocket_residual) / residual_row_count,
        "deep_support_fraction": residual_deep_fraction,
        "pocket_implies_low": pocket_implies_low,
        "deep_implies_pocket": deep_implies_pocket,
        "deep_implies_low": deep_implies_low,
        "fallback_is_distinct": fallback_is_distinct,
        "sparse_surface": sparse_surface,
        "passes": not failed_criteria,
        "failed_criteria": failed_criteria,
        "score": {
            "tier": discriminator.tier,
            "excluded_fraction": excluded_fraction,
            "residual_fallback_fraction": residual_fallback_fraction,
            "min_nesting_floor": min(
                pocket_implies_low,
                deep_implies_pocket,
                deep_implies_low,
            ),
        },
    }


def evaluate_polarity_discriminator_family(
    *,
    discriminator: PolarityDiscriminatorSpec,
    summary_rows_by_ensemble: dict[str, AtomicLaneEnsembleSummaryRow],
    support_payloads_by_ensemble: dict[str, dict[str, Any]],
    ensemble_names: tuple[str, ...],
    max_support_fraction: float = NONVACUOUS_SPARSE_SUPPORT_FRACTION,
    max_excluded_fraction: float = ANTI_SPARSE_MAX_EXCLUDED_FRACTION,
) -> dict[str, Any]:
    per_ensemble: list[dict[str, Any]] = []
    first_failed: dict[str, Any] | None = None
    for ensemble_name in ensemble_names:
        result = evaluate_polarity_discriminator(
            discriminator=discriminator,
            summary_row=summary_rows_by_ensemble[ensemble_name],
            support_payload=support_payloads_by_ensemble[ensemble_name],
            max_support_fraction=max_support_fraction,
            max_excluded_fraction=max_excluded_fraction,
        )
        per_ensemble.append(result)
        if first_failed is None and not result["passes"]:
            first_failed = result
    return {
        "discriminator": asdict(discriminator),
        "tested_ensembles": per_ensemble,
        "passes": all(result["passes"] for result in per_ensemble),
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


def search_polarity_discriminators(
    *,
    summary_rows_by_ensemble: dict[str, AtomicLaneEnsembleSummaryRow],
    support_payloads_by_ensemble: dict[str, dict[str, Any]],
    ensemble_names: tuple[str, ...],
    max_features: int = 3,
    feature_scope: str = "sparse",
    top_k: int = 25,
    max_support_fraction: float = NONVACUOUS_SPARSE_SUPPORT_FRACTION,
    max_excluded_fraction: float = ANTI_SPARSE_MAX_EXCLUDED_FRACTION,
) -> dict[str, Any]:
    candidates = generate_polarity_discriminator_candidates(
        max_features=max_features,
        feature_scope=feature_scope,
    )
    top_results: list[dict[str, Any]] = []
    passing_results: list[dict[str, Any]] = []
    tier_counts: dict[str, Any] = {}
    for tier in range(1, max_features + 1):
        tested = 0
        passed = 0
        tier_results: list[dict[str, Any]] = []
        for discriminator in candidates:
            if discriminator.tier != tier:
                continue
            tested += 1
            family_result = evaluate_polarity_discriminator_family(
                discriminator=discriminator,
                summary_rows_by_ensemble=summary_rows_by_ensemble,
                support_payloads_by_ensemble=support_payloads_by_ensemble,
                ensemble_names=ensemble_names,
                max_support_fraction=max_support_fraction,
                max_excluded_fraction=max_excluded_fraction,
            )
            tier_results.append(family_result)
            if family_result["passes"]:
                passed += 1
                passing_results.append(family_result)
        tier_results.sort(
            key=lambda result: (
                0 if result["passes"] else 1,
                result["score"]["tier"],
                result["score"]["max_excluded_fraction"],
                result["score"]["max_residual_fallback_fraction"],
                -result["score"]["min_nesting_floor"],
                result["discriminator"]["feature_subset_label"],
            )
        )
        tier_counts[f"tier_{tier}"] = {
            "tested": tested,
            "passed": passed,
        }
        top_results.extend(tier_results[:top_k])
        top_results.sort(
            key=lambda result: (
                0 if result["passes"] else 1,
                result["score"]["tier"],
                result["score"]["max_excluded_fraction"],
                result["score"]["max_residual_fallback_fraction"],
                -result["score"]["min_nesting_floor"],
                result["discriminator"]["feature_subset_label"],
            )
        )
        top_results = top_results[:top_k]
    passing_results.sort(
        key=lambda result: (
            result["score"]["tier"],
            result["score"]["max_excluded_fraction"],
            result["score"]["max_residual_fallback_fraction"],
            -result["score"]["min_nesting_floor"],
            result["discriminator"]["feature_subset_label"],
        )
    )
    return {
        "ensemble_names": list(ensemble_names),
        "feature_scope": feature_scope,
        "passing_results": passing_results[:top_k],
        "top_results": top_results,
        "tier_counts": tier_counts,
    }


def evaluate_candidate_family(
    *,
    low_candidate: AtomicRouteCandidateSpec,
    pocket_candidate: AtomicRouteCandidateSpec,
    deep_candidate: AtomicRouteCandidateSpec,
    summary_rows_by_ensemble: dict[str, AtomicLaneEnsembleSummaryRow],
    support_payloads_by_ensemble: dict[str, dict[str, Any]],
    ensemble_names: tuple[str, ...],
) -> dict[str, Any]:
    per_ensemble: list[dict[str, Any]] = []
    first_failed: dict[str, Any] | None = None
    for ensemble_name in ensemble_names:
        support_payload = support_payloads_by_ensemble[ensemble_name]
        summary_row = summary_rows_by_ensemble[ensemble_name]
        low_support = candidate_support_details(low_candidate, support_payload)
        pocket_support = candidate_support_details(pocket_candidate, support_payload)
        deep_support = candidate_support_details(deep_candidate, support_payload)
        low_set = low_support["support"]
        pocket_set = pocket_support["support"]
        deep_set = deep_support["support"]
        pocket_intersection = pocket_set & low_set
        deep_pocket_intersection = deep_set & pocket_set
        deep_low_intersection = deep_set & low_set
        pocket_implies_low = len(pocket_intersection) / len(pocket_set) if pocket_set else 1.0
        deep_implies_pocket = (
            len(deep_pocket_intersection) / len(deep_set) if deep_set else 1.0
        )
        deep_implies_low = len(deep_low_intersection) / len(deep_set) if deep_set else 1.0
        failed_criteria: list[str] = []
        if summary_row.compact_ge6_share6_match_fraction < COMPACT_MATCH_THRESHOLD:
            failed_criteria.append("compact-ge6-share6")
        if summary_row.compact_ge7_subset_fraction < COMPACT_SUBSET_THRESHOLD:
            failed_criteria.append("compact-ge7-subset")
        if low_support["support_count"] == 0:
            failed_criteria.append("low-missing")
        if pocket_support["support_count"] == 0:
            failed_criteria.append("pocket-missing")
        if deep_support["support_count"] == 0:
            failed_criteria.append("deep-missing")
        if pocket_implies_low < NESTING_THRESHOLD:
            failed_criteria.append("pocket=>low")
        if deep_implies_pocket < NESTING_THRESHOLD:
            failed_criteria.append("deep=>pocket")
        if deep_implies_low < NESTING_THRESHOLD:
            failed_criteria.append("deep=>low")
        if (
            low_candidate.proxy_family in PURE_SPARSE_FAMILIES
            or pocket_candidate.proxy_family in PURE_SPARSE_FAMILIES
            or deep_candidate.proxy_family in PURE_SPARSE_FAMILIES
        ):
            failed_criteria.append("sparse-dominant")
        if not summary_row.fallback_is_distinct:
            failed_criteria.append("fallback-leakage")
        if summary_row.fallback_feature_subset in {
            low_candidate.feature_subset_label,
            pocket_candidate.feature_subset_label,
            deep_candidate.feature_subset_label,
        }:
            failed_criteria.append("fallback-collision")
        ensemble_result = {
            "ensemble_name": ensemble_name,
            "compact_ge6_share6_match_fraction": summary_row.compact_ge6_share6_match_fraction,
            "compact_ge7_subset_fraction": summary_row.compact_ge7_subset_fraction,
            "low_feature_subset": low_candidate.feature_subset_label,
            "low_support_fraction": low_support["support_fraction"],
            "pocket_feature_subset": pocket_candidate.feature_subset_label,
            "pocket_support_fraction": pocket_support["support_fraction"],
            "deep_feature_subset": deep_candidate.feature_subset_label,
            "deep_support_fraction": deep_support["support_fraction"],
            "pocket_implies_low": pocket_implies_low,
            "deep_implies_pocket": deep_implies_pocket,
            "deep_implies_low": deep_implies_low,
            "fallback_is_distinct": summary_row.fallback_is_distinct,
            "passes": not failed_criteria,
            "failed_criteria": failed_criteria,
        }
        per_ensemble.append(ensemble_result)
        if failed_criteria and first_failed is None:
            first_failed = ensemble_result
    total_features = (
        len(low_candidate.feature_subset)
        + len(pocket_candidate.feature_subset)
        + len(deep_candidate.feature_subset)
    )
    mean_nesting_floor = sum(
        min(
            result["pocket_implies_low"],
            result["deep_implies_pocket"],
            result["deep_implies_low"],
        )
        for result in per_ensemble
    ) / max(1, len(per_ensemble))
    return {
        "low_candidate": asdict(low_candidate),
        "pocket_candidate": asdict(pocket_candidate),
        "deep_candidate": asdict(deep_candidate),
        "tested_ensembles": per_ensemble,
        "passes": all(result["passes"] for result in per_ensemble),
        "first_failed": first_failed,
        "score": {
            "tier": max(
                low_candidate.tier,
                pocket_candidate.tier,
                deep_candidate.tier,
            ),
            "total_features": total_features,
            "mean_nesting_floor": mean_nesting_floor,
            "sparse_penalty": int(low_candidate.contains_sparse)
            + int(pocket_candidate.contains_sparse)
            + int(deep_candidate.contains_sparse),
        },
    }


def search_atomic_route_family(
    *,
    summary_rows_by_ensemble: dict[str, AtomicLaneEnsembleSummaryRow],
    support_payloads_by_ensemble: dict[str, dict[str, Any]],
    passing_ensembles: tuple[str, ...],
    first_failing_ensemble: str,
    stricter_ensemble: str | None,
    max_features: int = 3,
    top_k: int = 25,
    start_tier: int = 1,
    initial_top_results: list[dict[str, Any]] | None = None,
    initial_tier_counts: dict[str, Any] | None = None,
    initial_promoted_family: dict[str, Any] | None = None,
) -> dict[str, Any]:
    candidates = generate_atomic_route_candidates(max_features=max_features)
    tested_ensembles = passing_ensembles + (first_failing_ensemble,)
    if stricter_ensemble is not None:
        tested_ensembles = tested_ensembles + (stricter_ensemble,)

    by_target: dict[int, dict[str, list[AtomicRouteCandidateSpec]]] = {}
    for tier in range(1, max_features + 1):
        pools = {"low": [], "pocket": [], "deep": []}
        for candidate in candidates:
            if candidate.tier > tier or candidate.atomic_target is None:
                continue
            pools[candidate.atomic_target].append(candidate)
        by_target[tier] = pools

    promoted_family: dict[str, Any] | None = initial_promoted_family
    top_results: list[dict[str, Any]] = list(initial_top_results or [])
    tier_counts: dict[str, Any] = dict(initial_tier_counts or {})

    for tier in range(start_tier, max_features + 1):
        pools = by_target[tier]
        tested = 0
        passed = 0
        tier_results: list[dict[str, Any]] = []
        for low_candidate in pools["low"]:
            failing_low = candidate_support_details(
                low_candidate,
                support_payloads_by_ensemble[first_failing_ensemble],
            )
            if failing_low["support_count"] == 0:
                continue
            for pocket_candidate in pools["pocket"]:
                failing_pocket = candidate_support_details(
                    pocket_candidate,
                    support_payloads_by_ensemble[first_failing_ensemble],
                )
                if failing_pocket["support_count"] == 0:
                    continue
                pocket_support = failing_pocket["support"]
                low_support = failing_low["support"]
                pocket_implies_low = (
                    len(pocket_support & low_support) / len(pocket_support)
                    if pocket_support
                    else 1.0
                )
                if pocket_implies_low < NESTING_THRESHOLD:
                    continue
                for deep_candidate in pools["deep"]:
                    failing_deep = candidate_support_details(
                        deep_candidate,
                        support_payloads_by_ensemble[first_failing_ensemble],
                    )
                    if failing_deep["support_count"] == 0:
                        continue
                    deep_support = failing_deep["support"]
                    deep_implies_pocket = (
                        len(deep_support & pocket_support) / len(deep_support)
                        if deep_support
                        else 1.0
                    )
                    deep_implies_low = (
                        len(deep_support & low_support) / len(deep_support)
                        if deep_support
                        else 1.0
                    )
                    if (
                        deep_implies_pocket < NESTING_THRESHOLD
                        or deep_implies_low < NESTING_THRESHOLD
                    ):
                        continue
                    tested += 1
                    family_result = evaluate_candidate_family(
                        low_candidate=low_candidate,
                        pocket_candidate=pocket_candidate,
                        deep_candidate=deep_candidate,
                        summary_rows_by_ensemble=summary_rows_by_ensemble,
                        support_payloads_by_ensemble=support_payloads_by_ensemble,
                        ensemble_names=tested_ensembles,
                    )
                    tier_results.append(family_result)
                    if family_result["passes"]:
                        passed += 1
                        if promoted_family is None:
                            promoted_family = family_result
        tier_results.sort(
            key=lambda result: (
                0 if result["passes"] else 1,
                result["score"]["tier"],
                result["score"]["total_features"],
                -result["score"]["mean_nesting_floor"],
                result["score"]["sparse_penalty"],
                result["low_candidate"]["feature_subset_label"],
                result["pocket_candidate"]["feature_subset_label"],
                result["deep_candidate"]["feature_subset_label"],
            )
        )
        tier_counts[f"tier_{tier}"] = {
            "tested": tested,
            "passed": passed,
        }
        top_results.extend(tier_results[:top_k])
        if promoted_family is not None:
            break

    top_results.sort(
        key=lambda result: (
            0 if result["passes"] else 1,
            result["score"]["tier"],
            result["score"]["total_features"],
            -result["score"]["mean_nesting_floor"],
            result["score"]["sparse_penalty"],
        )
    )
    return {
        "passing_ensembles": list(passing_ensembles),
        "first_failing_ensemble": first_failing_ensemble,
        "stricter_ensemble": stricter_ensemble,
        "tested_ensembles": list(tested_ensembles),
        "promoted_family": promoted_family,
        "top_results": top_results[:top_k],
        "tier_counts": tier_counts,
    }


def infer_atomic_lane_mechanism(
    *,
    summary_row: AtomicLaneEnsembleSummaryRow,
    shell_row: ThresholdCoreShellRow,
) -> dict[str, Any]:
    deep_gap = shell_row.shell_deep_fraction - shell_row.core_deep_fraction
    pocket_gap = shell_row.shell_pocket_fraction - shell_row.core_pocket_fraction
    low_gap = shell_row.shell_low_degree_fraction - shell_row.core_low_degree_fraction
    boundary_gap = (
        shell_row.shell_boundary_deficit_mean - shell_row.core_boundary_deficit_mean
    )
    mechanism_label: str
    if summary_row.compact_ge6_share6_match_fraction < COMPACT_MATCH_THRESHOLD or (
        summary_row.compact_ge7_subset_fraction < COMPACT_SUBSET_THRESHOLD
    ):
        mechanism_label = "compact-core regression"
    elif not summary_row.fallback_is_distinct:
        mechanism_label = "fallback leakage"
    elif summary_row.deep_parity_size is None or (
        summary_row.deep_implies_pocket < NESTING_THRESHOLD
        or summary_row.deep_implies_low < NESTING_THRESHOLD
    ):
        mechanism_label = "deep-pocket isolation collapse" if deep_gap <= pocket_gap else "nesting collapse"
    elif summary_row.pocket_parity_size is None or summary_row.pocket_implies_low < NESTING_THRESHOLD:
        mechanism_label = "pocket concentration collapse" if pocket_gap <= low_gap else "nesting collapse"
    elif summary_row.low_parity_size is None:
        mechanism_label = "low-degree exposure collapse"
    elif boundary_gap <= 0.0 or deep_gap <= 0.0 or pocket_gap <= 0.0 or low_gap <= 0.0:
        mechanism_label = "shell dilution"
    else:
        mechanism_label = "shell-localization retained"
    return {
        "ensemble_name": summary_row.ensemble_name,
        "mechanism_label": mechanism_label,
        "ge6_only_shell_fraction": shell_row.ge6_only_fraction,
        "deep_gap": deep_gap,
        "pocket_gap": pocket_gap,
        "low_gap": low_gap,
        "boundary_gap": boundary_gap,
        "failed_criteria": summary_row.failed_criteria,
    }


def build_bound_state_baseline() -> dict[str, Any]:
    coupling_grid = np.array([0.5, 1.0, 2.0, 3.0, 4.0], dtype=float)
    rows: list[dict[str, Any]] = []
    for d, sizes, coupling in BOUND_STATE_CONFIGS:
        laplacian = build_nd_laplacian(sizes)
        potential = coulomb_potential_nd(sizes, d, coupling=coupling)
        hamiltonian = laplacian + sparse.diags(potential, 0, format="csr")
        bound_states = count_bound_states(hamiltonian, n_eig=min(40, int(np.prod(sizes)) - 2))
        localization = (
            analyze_localization(bound_states["ground_state"], sizes, d)
            if len(bound_states["ground_state"]) > 0
            else {
                "ipr": 0.0,
                "n_eff": 0.0,
                "fraction": 1.0,
                "center_weight": 0.0,
                "decay_rate": 0.0,
                "fall_to_center": False,
                "genuinely_localized": False,
                "physical_bound": False,
            }
        )
        localization["physical_bound"] = bool(
            bound_states["n_bound"] > 0
            and localization["genuinely_localized"]
            and not localization["fall_to_center"]
        )
        rows.append(
            {
                "d": d,
                "sizes": list(sizes),
                "coupling": coupling,
                "n_bound": int(bound_states["n_bound"]),
                "lowest_eigenvalue": (
                    float(bound_states["eigenvalues"][0])
                    if len(bound_states["eigenvalues"]) > 0
                    else None
                ),
                "localization": json_ready(localization),
                "coupling_scan": json_ready(coupling_scan(d, sizes, coupling_grid)),
            }
        )
    stable_dims = [
        row["d"]
        for row in rows
        if row["localization"]["physical_bound"]
    ]
    unstable_dims = [
        row["d"]
        for row in rows
        if row["localization"]["fall_to_center"] or row["n_bound"] == 0
    ]
    return {
        "rows": rows,
        "stable_dims": stable_dims,
        "unstable_dims": unstable_dims,
    }


def compare_atomic_lane_to_bound_state(
    *,
    summary_rows: Iterable[AtomicLaneEnsembleSummaryRow],
    mechanism_rows: Iterable[dict[str, Any]],
    bound_state_baseline: dict[str, Any],
) -> dict[str, Any]:
    summary_rows = list(summary_rows)
    mechanism_rows = list(mechanism_rows)
    atomic_summary = {
        "retained_all_ensembles": all(row.retained_passes for row in summary_rows),
        "ensemble_count": len(summary_rows),
        "min_compact_match": min(
            row.compact_ge6_share6_match_fraction for row in summary_rows
        ),
        "min_compact_subset": min(row.compact_ge7_subset_fraction for row in summary_rows),
        "min_nesting_floor": min(row.nesting_floor for row in summary_rows),
        "mean_ge6_only_fraction": sum(row.compact_ge6_only_fraction for row in summary_rows)
        / max(1, len(summary_rows)),
        "fallback_all_distinct": all(row.fallback_is_distinct for row in summary_rows),
        "mean_deep_gap": sum(row["deep_gap"] for row in mechanism_rows)
        / max(1, len(mechanism_rows)),
        "mean_pocket_gap": sum(row["pocket_gap"] for row in mechanism_rows)
        / max(1, len(mechanism_rows)),
        "mean_low_gap": sum(row["low_gap"] for row in mechanism_rows)
        / max(1, len(mechanism_rows)),
    }
    bounded_companion_evidence = bool(
        atomic_summary["retained_all_ensembles"]
        and atomic_summary["fallback_all_distinct"]
        and atomic_summary["min_nesting_floor"] >= NESTING_THRESHOLD
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


def _compute_case_stage_payload(
    *,
    retained_weight: float,
    mode_retained_weight: float | None,
    active_ensemble: tuple[tuple[str, int, int, tuple[str, ...]], ...],
) -> dict[str, Any]:
    case_rows, aggregate_rows = threshold_core_case_shell_flip_analysis(
        retained_weight=retained_weight,
        mode_retained_weight=mode_retained_weight,
        ensembles=active_ensemble,
    )
    return {
        "case_rows": [asdict(row) for row in case_rows],
        "aggregate_rows": [asdict(row) for row in aggregate_rows],
    }
