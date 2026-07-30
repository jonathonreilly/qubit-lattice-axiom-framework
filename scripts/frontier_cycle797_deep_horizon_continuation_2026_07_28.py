#!/usr/bin/env python3
"""Cycle 797: deep-horizon continuation and Cycle-795 hypothesis tests.

The Cycle-791 primary is main-guarded, so this runner imports its exact
checkpoint/recurrence machinery.  The Cycle-795 primary is likewise guarded;
all 103 clean-separator forecasts are deterministically reconstructed from
its feature table rather than copied from stdout.  The Cycle-792/794 selector
references were materialized on disk before this run and are text/hash
anchors only: the one-tick battery is reconstructed with landed machinery.

Every separator and forecast remains a hypothesis.  This is a finite
continuation census, with content versus dirt left open.
"""
from __future__ import annotations

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle791_open_keys_resolution_2026_07_28.py",
    "scripts/frontier_cycle795_discriminator_census_2026_07_28.py",
    "scripts/frontier_cycle792_extended_horizon_selector_2026_07_28.py",
    "scripts/frontier_cycle794_second_selection_2026_07_28.py",
)

import ast
from collections import Counter
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle791_open_keys_resolution_2026_07_28 as M791
import frontier_cycle795_discriminator_census_2026_07_28 as M795


EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "3380b3f0820a74e0f538b54144bb926a2a4be9041ed21ae5181216f481c8a98a",
    AUDIT_INPUT_PATHS[1]:
        "6a52229e9ac3bf5ab45bd25a4088e354c759fc499b58462aa0c2401f89474e7f",
    AUDIT_INPUT_PATHS[2]:
        "7f7470b3d759c84ccc0c2c6559d62448340fb8a0b0915eb98d450635a72730df",
    AUDIT_INPUT_PATHS[3]:
        "5fcb9f015b7690df833a3b3d1dc7bdc81162e066f1f25d34d420d8779c563582",
}

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
FAMILY_SIZE = 176
T1024_OPEN_SIZE = 162
HORIZONS = (2048, 4096)
BATCH_SIZE = 16
EXPECTED_SEPARATOR_COUNT = 103
EXPECTED_FORECAST_VECTOR_COUNT = 46
FORECAST_LABELS = ("TRANSIENT", "CYCLE", "UNSEEN")
SELECTION_REFERENCE_COMMITS = (
    "04499b4251",
    "0f4bace05d",
)
ORIGINAL_TRANSIENT_POSITIONS = ((1, 10), (0, 7))

Key = tuple[int, tuple[int, int]]
CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label}")
    return passed


def data(label: str, value: object) -> None:
    OUTPUT_LINES.append(f"DATA {label} {compact(value)}")


def disk_path(path: str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else ROOT / candidate


def audit_tuple_is_literal() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    nodes = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
            nodes.append(node.value)
    return (
        len(nodes) == 1
        and isinstance(nodes[0], ast.Tuple)
        and all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in nodes[0].elts
        )
        and ast.literal_eval(nodes[0]) == AUDIT_INPUT_PATHS
    )


def anchor_controls() -> dict[str, object]:
    actual = {
        path: sha256(disk_path(path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    nested_791 = M791.anchor_certificate()
    nested_795 = M795.anchor_certificate()
    guarded_imports_clean = (
        not M791.CHECKS
        and not M791.OUTPUT_LINES
        and not M795.CHECKS
        and not M795.OUTPUT_LINES
    )
    result = {
        "machinery_basis": (
            "DIRECT_MAIN_GUARDED_IMPORTS_CYCLE791_AND_CYCLE795;"
            "NESTED_790_762_PAIR_736_719_ANCHORS;"
            "TEXT_HASH_ONLY_PINNED_792_794_REFERENCES"
        ),
        "forecast_reconstruction": (
            "RE_DERIVED_103_SEPARATOR_VOTES_FROM_IMPORTABLE_CYCLE795_"
            "FEATURE_AND_DISCRIMINATION_FUNCTIONS"
        ),
        "selection_battery_reconstruction": (
            "RECONSTRUCTED_FROM_TEXT_HASH_ONLY_PINNED_CYCLE792_794_"
            "REFERENCES_WITH_LANDED_CYCLE790_FAMILY"
        ),
        "selection_reference_commits": SELECTION_REFERENCE_COMMITS,
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_is_literal_tuple": audit_tuple_is_literal(),
        "all_paths_are_existing_disk_files":
            all(disk_path(path).is_file() for path in AUDIT_INPUT_PATHS),
        "input_sha256": actual,
        "guarded_imports_clean": guarded_imports_clean,
        "nested_cycle791_anchor_pass": nested_791["pass"],
        "nested_cycle795_anchor_pass": nested_795["pass"],
        "nested_cycle791_input_sha256": nested_791["input_sha256"],
        "nested_cycle795_input_sha256": nested_795["input_sha256"],
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_is_literal_tuple"]
        and result["all_paths_are_existing_disk_files"]
        and actual == EXPECTED_INPUT_SHA256
        and guarded_imports_clean
        and nested_791["pass"]
        and nested_795["pass"]
        and Path(M791.__file__).resolve()
        == disk_path(AUDIT_INPUT_PATHS[0]).resolve()
        and Path(M795.__file__).resolve()
        == disk_path(AUDIT_INPUT_PATHS[1]).resolve()
        and len(AUDIT_INPUT_PATHS) <= 7
    )
    return result


def observed_catalog(
    records: dict[Key, dict[str, object]],
    snapshot: dict[str, object],
) -> tuple[dict[str, object], ...]:
    rows = []
    for key in snapshot["clean_keys"]:
        record = records[key]
        rows.append(
            {
                "k": key,
                "v": "TRANSIENT",
                "first_clean": record["first_clean"],
                "state_period": None,
                "residual_period": None,
            }
        )
    for key in snapshot["cycle_keys"]:
        record = records[key]
        rows.append(
            {
                "k": key,
                "v": "CYCLE",
                "first_clean": None,
                "state_period": record["state_period"],
                "residual_period": record["residual_period"],
            }
        )
    baseline_transient = {
        "k": M791.EXPECTED_BASELINE_CLEAN_KEY,
        "v": "TRANSIENT",
        "first_clean": 252,
        "state_period": None,
        "residual_period": None,
    }
    baseline_cycles = tuple(
        {
            "k": (event, positions),
            "v": "CYCLE",
            "first_clean": None,
            "state_period": period,
            "residual_period": period,
        }
        for event, positions, period
        in M791.M790.EXPECTED_PERIODIC_KEYS_T64
    )
    return tuple(
        sorted(
            (baseline_transient, *baseline_cycles, *rows),
            key=lambda row: row["k"],
        )
    )


def t1024_identity(
    records: dict[Key, dict[str, object]],
    snapshot: dict[str, object],
    catalog: tuple[dict[str, object], ...],
) -> dict[str, object]:
    transient_facts = {
        row["k"]: row["first_clean"]
        for row in catalog if row["v"] == "TRANSIENT"
    }
    cycle_facts = {
        row["k"]: (row["state_period"], row["residual_period"])
        for row in catalog if row["v"] == "CYCLE"
    }
    certifications = tuple(
        {
            "key": key,
            "entry": (
                0
                if key not in records
                else records[key]["cycle_start"]
            ),
            "state_period": cycle_facts[key][0],
            "residual_period": cycle_facts[key][1],
            "closure": (
                cycle_facts[key][0]
                if key not in records
                else records[key]["cycle_closure"]
            ),
            "nonzero": (
                True
                if key not in records
                else records[key]["cycle_nonzero"]
            ),
        }
        for key in sorted(cycle_facts)
    )
    result = {
        "T1024_counts": {
            "transient": snapshot["family_clean_count"],
            "cycle": snapshot["family_cycle_count"],
            "open": snapshot["family_open_count"],
            "uncovered": snapshot["family_uncovered_count"],
        },
        "event_moments": tuple(
            {
                "key": key,
                "first_clean": first_clean,
            }
            for key, first_clean in sorted(transient_facts.items())
        ),
        "cycle_certifications": certifications,
        "catalog_sha256": digest(catalog),
        "open_key_sha256": digest(snapshot["open_keys"]),
        "digest_collisions": sum(
            record["digest_collisions"] for record in records.values()
        ),
        "exact_new_cycle_confirmations": sum(
            record["exact_recurrence_confirmations"]
            for record in records.values()
        ),
    }
    result["pass"] = (
        result["T1024_counts"]
        == {"transient": 2, "cycle": 12, "open": 162, "uncovered": 0}
        and transient_facts == M795.EXPECTED_TRANSIENTS
        and cycle_facts == M795.EXPECTED_CYCLES
        and len(catalog) == 14
        and result["digest_collisions"] == 0
        and result["exact_new_cycle_confirmations"] == 1
        and all(row["nonzero"] for row in certifications)
        and all(
            row["entry"] == 0
            for row in certifications
            if row["key"] in {
                (event, positions)
                for event, positions, _period
                in M791.M790.EXPECTED_PERIODIC_KEYS_T64
            }
        )
    )
    return result


def choose_t4096_prefix(
    remaining_open: tuple[Key, ...],
    elapsed: float,
    phase2048_seconds: float,
    phase2048_transitions: int,
) -> tuple[int, dict[str, object]]:
    rate = (
        phase2048_seconds / phase2048_transitions
        if phase2048_transitions
        else 0.0
    )
    safety_factor = 1.5
    reserve_seconds = 45.0
    selected = 0
    selected_projection = elapsed + reserve_seconds
    for candidate in range(len(remaining_open), -1, -1):
        future_upper = candidate * (HORIZONS[1] - HORIZONS[0])
        replay_upper = phase2048_transitions + future_upper
        projected = (
            elapsed
            + safety_factor * rate * (future_upper + replay_upper)
            + reserve_seconds
        )
        if projected < AUDIT_TIMEOUT_SEC:
            selected = candidate
            selected_projection = projected
            break
    decision = {
        "policy": (
            "Complete T2048 for all 162 T1024-open keys; then take the "
            "largest sorted T2048-open-key prefix whose measured-rate "
            "projection includes its T4096 primary continuation, a fixed-"
            "prefix replay from T1024, a 1.5 safety factor, and 45s reserve"
        ),
        "measured_seconds_per_transition": round(rate, 9),
        "phase_T1025_T2048_transitions": phase2048_transitions,
        "T2048_remaining_open": len(remaining_open),
        "declared_T4096_prefix_count": selected,
        "full_T4096_coverage": selected == len(remaining_open),
        "safety_factor": safety_factor,
        "reserve_seconds": reserve_seconds,
        "projected_total_seconds": round(selected_projection, 6),
    }
    return selected, decision


def continuation_row(
    key: Key,
    record: dict[str, object],
) -> dict[str, object]:
    return {
        "key": key,
        "T2048": M791.record_status(record, HORIZONS[0]),
        "T4096": M791.record_status(record, HORIZONS[1]),
        "first_clean": record["first_clean"],
        "cycle_entry": record["cycle_start"],
        "state_period": record["state_period"],
        "residual_period": record["residual_period"],
        "cycle_closure": record["cycle_closure"],
        "cycle_nonzero": record["cycle_nonzero"],
        "last_evolved": record["last_evolved"],
        "digest_collisions": record["digest_collisions"],
        "exact_recurrence_confirmations":
            record["exact_recurrence_confirmations"],
    }


def public_snapshot(snapshot: dict[str, object]) -> dict[str, object]:
    return M791.public_snapshot(snapshot)


def run_continuation(
    seed_records: dict[Key, dict[str, object]],
    checkpoints: dict[Key, dict[str, object]],
    family: dict[str, object],
    open1024: tuple[Key, ...],
    script_started: float,
    fixed_t4096_prefix_count: int | None = None,
) -> dict[str, object]:
    started = monotonic()
    records = deepcopy(seed_records)

    phase_started = monotonic()
    timings2048, transitions2048 = M791.advance_batches(
        records,
        checkpoints,
        family["words"],
        open1024,
        HORIZONS[0],
    )
    phase2048_seconds = monotonic() - phase_started
    snapshot2048 = M791.resolution_snapshot(records, HORIZONS[0])
    remaining2048 = tuple(snapshot2048["open_keys"])

    if fixed_t4096_prefix_count is None:
        prefix_count, decision = choose_t4096_prefix(
            remaining2048,
            monotonic() - script_started,
            phase2048_seconds,
            transitions2048,
        )
    else:
        prefix_count = fixed_t4096_prefix_count
        decision = {
            "policy": "DETERMINISM_REPLAY_USES_PRIMARY_DECLARED_PREFIX",
            "T2048_remaining_open": len(remaining2048),
            "declared_T4096_prefix_count": prefix_count,
            "full_T4096_coverage": prefix_count == len(remaining2048),
        }
    if not 0 <= prefix_count <= len(remaining2048):
        raise AssertionError(
            ("invalid T4096 prefix", prefix_count, len(remaining2048))
        )
    covered4096 = remaining2048[:prefix_count]

    phase_started = monotonic()
    timings4096, transitions4096 = M791.advance_batches(
        records,
        checkpoints,
        family["words"],
        covered4096,
        HORIZONS[1],
    )
    phase4096_seconds = monotonic() - phase_started
    snapshot4096 = M791.resolution_snapshot(records, HORIZONS[1])
    rows = tuple(
        continuation_row(key, records[key]) for key in open1024
    )
    payload = {
        "open1024": open1024,
        "declared_T4096_prefix": covered4096,
        "snapshots": {
            2048: public_snapshot(snapshot2048),
            4096: public_snapshot(snapshot4096),
        },
        "rows": rows,
    }
    return {
        "records": records,
        "snapshots": {2048: snapshot2048, 4096: snapshot4096},
        "remaining2048": remaining2048,
        "covered4096": covered4096,
        "prefix_count": prefix_count,
        "coverage_decision": decision,
        "rows": rows,
        "table_sha256": digest(rows),
        "deterministic_sha256": digest(payload),
        "transition_counts": {
            "T1025_T2048": transitions2048,
            "T2049_T4096": transitions4096,
            "total": transitions2048 + transitions4096,
        },
        "phase_seconds": {
            "T1025_T2048": round(phase2048_seconds, 6),
            "T2049_T4096": round(phase4096_seconds, 6),
        },
        "batch_timings": tuple(timings2048 + timings4096),
        "runtime_seconds": round(monotonic() - started, 6),
    }


def resolution_rows(
    open1024: tuple[Key, ...],
    records: dict[Key, dict[str, object]],
    horizon: int,
) -> tuple[dict[str, object], ...]:
    rows = []
    for key in open1024:
        record = records[key]
        if (
            record["first_clean"] is not None
            and record["first_clean"] <= horizon
        ):
            rows.append(
                {
                    "key": key,
                    "outcome": "TRANSIENT",
                    "first_clean": record["first_clean"],
                    "cycle_entry": None,
                    "state_period": None,
                    "residual_period": None,
                    "cycle_closure": None,
                }
            )
        elif (
            record["cycle_closure"] is not None
            and record["cycle_closure"] <= horizon
        ):
            rows.append(
                {
                    "key": key,
                    "outcome": "CYCLE",
                    "first_clean": None,
                    "cycle_entry": record["cycle_start"],
                    "state_period": record["state_period"],
                    "residual_period": record["residual_period"],
                    "cycle_closure": record["cycle_closure"],
                }
            )
    return tuple(sorted(rows, key=lambda row: row["key"]))


def updated_fractions(snapshot: dict[str, object]) -> dict[str, str]:
    return {
        "clean_transients":
            f"{snapshot['family_clean_count']}/{FAMILY_SIZE}",
        "certified_cycles":
            f"{snapshot['family_cycle_count']}/{FAMILY_SIZE}",
        "open_through_horizon":
            f"{snapshot['family_open_count']}/{FAMILY_SIZE}",
        "uncovered_if_partial":
            f"{snapshot['family_uncovered_count']}/{FAMILY_SIZE}",
    }


def separator_prediction(
    names: tuple[str, ...],
    feature_row: tuple[int, ...],
    transient_values: set[tuple[int, ...]],
    cycle_values: set[tuple[int, ...]],
    feature_indices: dict[str, int],
) -> str:
    value = M795.value_for(feature_row, names, feature_indices)
    if value in transient_values:
        return "TRANSIENT"
    if value in cycle_values:
        return "CYCLE"
    return "UNSEEN"


def hypothesis_table(
    features: dict[Key, tuple[int, ...]],
    catalog: tuple[dict[str, object], ...],
    open1024: tuple[Key, ...],
    resolution_rows_all: tuple[dict[str, object], ...],
) -> dict[str, object]:
    discrimination = M795.discrimination_census(
        features, catalog, open1024
    )
    clean = discrimination["clean"]
    transient_keys = tuple(
        row["k"] for row in catalog if row["v"] == "TRANSIENT"
    )
    cycle_keys = tuple(
        row["k"] for row in catalog if row["v"] == "CYCLE"
    )
    feature_indices = {
        name: index for index, name in enumerate(M795.FEATURE_SCHEMA)
    }

    separator_rows = []
    forecast_by_separator: dict[str, tuple[str, ...]] = {}
    original_consistency: dict[str, bool] = {}
    for index, candidate in enumerate(clean):
        separator_id = f"S{index:03d}"
        names = candidate["f"]
        transient_values = {
            M795.value_for(features[key], names, feature_indices)
            for key in transient_keys
        }
        cycle_values = {
            M795.value_for(features[key], names, feature_indices)
            for key in cycle_keys
        }
        sequence = tuple(
            separator_prediction(
                names,
                features[key],
                transient_values,
                cycle_values,
                feature_indices,
            )
            for key in open1024
        )
        forecast_by_separator[separator_id] = sequence
        original_consistency[separator_id] = all(
            separator_prediction(
                names,
                features[row["k"]],
                transient_values,
                cycle_values,
                feature_indices,
            ) == row["v"]
            for row in catalog
        )
        separator_rows.append(
            {
                "separator_id": separator_id,
                "features": names,
                "dimension": candidate["dimension"],
                "margin_L1": candidate["margin_L1"],
                "forecast_sha256": digest(sequence),
            }
        )

    sequences = tuple(sorted(set(forecast_by_separator.values())))
    vector_id_by_sequence = {
        sequence: f"V{index:02d}"
        for index, sequence in enumerate(sequences)
    }
    separator_to_vector = {
        separator_id: vector_id_by_sequence[sequence]
        for separator_id, sequence in forecast_by_separator.items()
    }
    for row in separator_rows:
        row["vector_id"] = separator_to_vector[row["separator_id"]]
    vector_rows = tuple(
        {
            "vector_id": vector_id_by_sequence[sequence],
            "forecast_sha256": digest(sequence),
            "separator_ids": tuple(
                separator_id
                for separator_id, candidate_sequence
                in forecast_by_separator.items()
                if candidate_sequence == sequence
            ),
            "implication_counts": {
                label: sequence.count(label) for label in FORECAST_LABELS
            },
        }
        for sequence in sequences
    )

    key_index = {key: index for index, key in enumerate(open1024)}
    consistent = {
        separator_id
        for separator_id, passed in original_consistency.items()
        if passed
    }
    scoring_rows = []
    chronological = sorted(
        resolution_rows_all,
        key=lambda row: (
            row["first_clean"]
            if row["outcome"] == "TRANSIENT"
            else row["cycle_closure"],
            row["key"],
        ),
    )
    for resolution in chronological:
        key = resolution["key"]
        observed = resolution["outcome"]
        index = key_index[key]
        correct_ids = tuple(
            separator_id
            for separator_id, sequence in forecast_by_separator.items()
            if sequence[index] == observed
        )
        unseen_ids = tuple(
            separator_id
            for separator_id, sequence in forecast_by_separator.items()
            if sequence[index] == "UNSEEN"
        )
        incorrect_ids = tuple(
            separator_id
            for separator_id, sequence in forecast_by_separator.items()
            if sequence[index] not in {observed, "UNSEEN"}
        )
        consistent &= set(correct_ids)
        scoring_rows.append(
            {
                "key": key,
                "resolution_moment": (
                    resolution["first_clean"]
                    if observed == "TRANSIENT"
                    else resolution["cycle_closure"]
                ),
                "observed": observed,
                "correct_separator_count": len(correct_ids),
                "correct_separator_ids": correct_ids,
                "incorrect_separator_count": len(incorrect_ids),
                "unseen_separator_count": len(unseen_ids),
                "correct_vector_ids": tuple(
                    sorted(
                        {
                            separator_to_vector[separator_id]
                            for separator_id in correct_ids
                        }
                    )
                ),
                "surviving_after_this_resolution": len(consistent),
                "surviving_separator_ids_after":
                    tuple(sorted(consistent)),
            }
        )

    original_consistent_ids = tuple(
        sorted(
            separator_id
            for separator_id, passed in original_consistency.items()
            if passed
        )
    )
    return {
        "discrimination": discrimination,
        "separator_catalog": tuple(separator_rows),
        "vector_catalog": vector_rows,
        "forecast_by_separator": forecast_by_separator,
        "separator_to_vector": separator_to_vector,
        "original_14_consistent_separator_ids":
            original_consistent_ids,
        "scoring_rows": tuple(scoring_rows),
        "surviving_separator_ids": tuple(sorted(consistent)),
        "separator_count": len(clean),
        "forecast_vector_count": len(sequences),
        "forecast_table_sha256": digest(
            {
                "open_keys": open1024,
                "separator_rows": separator_rows,
                "vectors": vector_rows,
                "forecasts": forecast_by_separator,
            }
        ),
    }


def rotation_representative(
    positions: tuple[int, int],
) -> tuple[int, int]:
    stations = M795.RING_STATIONS
    return min(
        tuple(
            sorted(
                (
                    (positions[0] + shift) % stations,
                    (positions[1] + shift) % stations,
                )
            )
        )
        for shift in range(stations)
    )


def selector_clean_matrix(
    family: dict[str, object],
    battery: tuple[tuple[int, int], ...],
    requested_by_event: dict[int, set[int]],
) -> dict[tuple[int, tuple[int, int], int], bool]:
    matrix = {}
    for event, requested in sorted(requested_by_event.items()):
        if not requested:
            continue
        if min(requested) < 0:
            raise ValueError(("negative selector horizon", requested))
        requested_sorted = tuple(sorted(requested))
        maximum = requested_sorted[-1]
        requested_set = set(requested_sorted)
        for positions in battery:
            key = (event, positions)
            state = family["states"][key]
            if 0 in requested_set:
                matrix[(event, positions, 0)] = (
                    not M791.M790.residual_support(state)
                )
            word = family["words"][positions]
            for update in range(1, maximum + 1):
                state = M791.M790.K.A.apply_semantic(state, word)
                if update in requested_set:
                    matrix[(event, positions, update)] = (
                        not M791.M790.residual_support(state)
                    )
    return matrix


def selection_pattern_check(
    family: dict[str, object],
    new_transients: tuple[dict[str, object], ...],
) -> dict[str, object]:
    all_positions = tuple(
        sorted(
            key[1] for key in family["states"] if key[0] == 0
        )
    )
    representatives = tuple(
        sorted(
            {
                rotation_representative(positions)
                for positions in all_positions
            }
        )
    )
    augmented_positions = {
        row["key"][1] for row in new_transients
    }
    battery = tuple(
        sorted(
            set(representatives)
            | set(ORIGINAL_TRANSIENT_POSITIONS)
            | augmented_positions
        )
    )
    baseline_battery = tuple(
        sorted(set(representatives) | set(ORIGINAL_TRANSIENT_POSITIONS))
    )
    requested_by_event: dict[int, set[int]] = {3: {251, 252, 370, 371}}
    for row in new_transients:
        event = row["key"][0]
        moment = row["first_clean"]
        requested_by_event.setdefault(event, set()).update(
            (moment - 1, moment)
        )
    matrix = selector_clean_matrix(
        family, battery, requested_by_event
    )

    def survivors(
        event: int,
        moment: int,
        positions_rows: tuple[tuple[int, int], ...] = battery,
    ) -> tuple[tuple[int, int], ...]:
        return tuple(
            positions
            for positions in positions_rows
            if matrix[(event, positions, moment)]
        )

    baseline_rows = (
        {
            "key": (3, (1, 10)),
            "moment": 252,
            "control_selected":
                matrix[(3, (1, 10), 251)],
            "survivors_at_moment":
                survivors(3, 252, baseline_battery),
        },
        {
            "key": (3, (0, 7)),
            "moment": 371,
            "control_selected":
                matrix[(3, (0, 7), 370)],
            "survivors_at_moment":
                survivors(3, 371, baseline_battery),
        },
    )
    baseline_two_for_two = all(
        not row["control_selected"]
        and row["survivors_at_moment"] == (row["key"][1],)
        for row in baseline_rows
    )
    new_rows = tuple(
        {
            "key": row["key"],
            "moment": row["first_clean"],
            "control_selected": matrix[
                (row["key"][0], row["key"][1], row["first_clean"] - 1)
            ],
            "survivors_at_moment":
                survivors(row["key"][0], row["first_clean"]),
            "unique_one_tick_selection": (
                not matrix[
                    (
                        row["key"][0],
                        row["key"][1],
                        row["first_clean"] - 1,
                    )
                ]
                and survivors(
                    row["key"][0], row["first_clean"]
                ) == (row["key"][1],)
            ),
        }
        for row in sorted(new_transients, key=lambda item: item["key"])
    )
    if not new_transients:
        pattern = "TWO_FOR_TWO_HOLDS_NO_NEW_TRANSIENT_TEST"
    elif baseline_two_for_two and all(
        row["unique_one_tick_selection"] for row in new_rows
    ):
        pattern = (
            f"EXTENDS_TO_{2 + len(new_rows)}_FOR_"
            f"{2 + len(new_rows)}_UNIQUE"
        )
    else:
        pattern = "TWO_FOR_TWO_PATTERN_BREAKS_ON_NEW_DATA"
    return {
        "reference_basis":
            "RECONSTRUCTED_PINNED_CYCLE792_794_ONE_TICK_BATTERY",
        "time_indexing": (
            "family state t=0 is the immediate postimage; moment t applies "
            "t further full landed controller words, matching Cycle794"
        ),
        "rotation_family_representatives": representatives,
        "pinned_baseline_battery": baseline_battery,
        "battery": battery,
        "baseline_rows": baseline_rows,
        "baseline_two_for_two": baseline_two_for_two,
        "new_transient_rows": new_rows,
        "pattern": pattern,
        "verification_pass": (
            baseline_two_for_two
            and len(new_rows) == len(new_transients)
            and all(
                not row["control_selected"]
                and row["key"][1] in row["survivors_at_moment"]
                for row in new_rows
            )
        ),
    }


def boundary_data() -> dict[str, object]:
    return {
        "content_vs_dirt": "OPEN",
        "separator_status": "HYPOTHESES_NOT_LAWS",
        "forecast_status": "HYPOTHESIS_TESTS_ONLY",
        "probabilities_assigned": False,
        "statistical_weights_assigned": False,
        "axiom_update_triggered": False,
        "scope": "FINITE_176_KEY_LANDED_FAMILY_CONTINUATION",
        "plain_reading": {
            "declared_named_input_files": len(AUDIT_INPUT_PATHS),
            "maximum_named_input_files": 7,
            "docs_read": 0,
            "ledgers_read": 0,
        },
    }


def id_mask_hex(ids: tuple[str, ...]) -> str:
    mask = 0
    for identifier in ids:
        mask |= 1 << int(identifier[1:])
    width = max(1, (EXPECTED_SEPARATOR_COUNT + 3) // 4)
    return f"{mask:0{width}x}"


def compact_scoring_row(row: dict[str, object]) -> dict[str, object]:
    correct_ids = row["correct_separator_ids"]
    surviving_ids = row["surviving_separator_ids_after"]
    return {
        "key": row["key"],
        "resolution_moment": row["resolution_moment"],
        "observed": row["observed"],
        "correct_separator_count": row["correct_separator_count"],
        "correct_separator_mask_hex": id_mask_hex(correct_ids),
        "correct_separator_ids_if_at_most_24": (
            correct_ids if len(correct_ids) <= 24 else None
        ),
        "incorrect_separator_count": row["incorrect_separator_count"],
        "unseen_separator_count": row["unseen_separator_count"],
        "correct_vector_ids": row["correct_vector_ids"],
        "surviving_after_this_resolution":
            row["surviving_after_this_resolution"],
        "surviving_separator_mask_hex": id_mask_hex(surviving_ids),
        "surviving_separator_ids_if_at_most_24": (
            surviving_ids if len(surviving_ids) <= 24 else None
        ),
    }


def run() -> int:
    script_started = monotonic()
    boundaries = boundary_data()

    anchors = anchor_controls()
    check("A_anchors_and_machinery_basis", anchors["pass"])
    data("A_ANCHORS_AND_BASIS", anchors)

    identity256, checkpoints, family = (
        M791.build_identity_and_checkpoints()
    )
    sweep1024 = M791.resolution_sweep(
        checkpoints,
        family,
        script_started,
        fixed_prefix_count=len(checkpoints),
    )
    records1024 = sweep1024["records"]
    snapshot1024 = sweep1024["snapshots"][1024]
    catalog = observed_catalog(records1024, snapshot1024)
    identity1024 = t1024_identity(
        records1024, snapshot1024, catalog
    )
    b_pass = (
        identity256["pass"]
        and identity1024["pass"]
        and sweep1024["prefix_count"] == len(checkpoints) == 164
        and snapshot1024["open_count"] == T1024_OPEN_SIZE
        and sweep1024["snapshots"][512]["uncovered_count"] == 0
        and snapshot1024["uncovered_count"] == 0
    )
    check("B_T1024_identity_control_2_12_162", b_pass)
    data(
        "B_T1024_IDENTITY",
        {
            "T256_identity_pass": identity256["pass"],
            "T256_checkpoint_sha256": identity256["checkpoint_sha256"],
            "T1024": identity1024,
            "resolution_sha256": sweep1024["deterministic_sha256"],
            "resolution_table_sha256": sweep1024["table_sha256"],
            "timing_seconds": {
                "T256_identity": identity256["runtime_seconds"],
                "T257_T1024": sweep1024["runtime_seconds"],
            },
        },
    )

    open1024 = tuple(snapshot1024["open_keys"])
    seed_records = deepcopy(records1024)
    primary = run_continuation(
        seed_records,
        checkpoints,
        family,
        open1024,
        script_started,
    )
    snapshot2048 = primary["snapshots"][2048]
    snapshot4096 = primary["snapshots"][4096]
    expected_uncovered4096 = tuple(
        primary["remaining2048"][primary["prefix_count"]:]
    )
    digest_collisions = sum(
        record["digest_collisions"]
        for record in primary["records"].values()
    )
    exact_confirmations = sum(
        record["exact_recurrence_confirmations"]
        for record in primary["records"].values()
    )
    c_pass = (
        len(open1024) == T1024_OPEN_SIZE
        and snapshot2048["uncovered_count"] == 0
        and all(
            M791.terminal(primary["records"][key])
            or primary["records"][key]["last_evolved"] >= 2048
            for key in open1024
        )
        and primary["covered4096"]
        == primary["remaining2048"][:primary["prefix_count"]]
        and snapshot4096["uncovered_keys"] == expected_uncovered4096
        and snapshot2048["family_accounting_total"] == FAMILY_SIZE
        and snapshot4096["family_accounting_total"] == FAMILY_SIZE
        and digest_collisions == 0
        and exact_confirmations == snapshot4096["new_cycle_count"]
        and all(
            primary["records"][key]["cycle_nonzero"]
            for key in snapshot4096["cycle_keys"]
        )
    )
    check("C_continuation_honest_coverage", c_pass)
    data(
        "C_COVERAGE",
        {
            **primary["coverage_decision"],
            "T2048_population_covered": len(open1024),
            "T4096_prefix_sha256": digest(primary["covered4096"]),
            "T4096_uncovered_keys": expected_uncovered4096,
            "transition_counts": primary["transition_counts"],
            "phase_seconds": primary["phase_seconds"],
            "exact_recurrence_confirmations": exact_confirmations,
            "digest_collisions": digest_collisions,
        },
    )
    for timing in primary["batch_timings"]:
        data("C_BATCH_TIMING", timing)

    resolutions2048 = resolution_rows(
        open1024, primary["records"], 2048
    )
    resolutions4096 = resolution_rows(
        open1024, primary["records"], 4096
    )
    resolved2048_keys = {row["key"] for row in resolutions2048}
    after2048 = tuple(
        row for row in resolutions4096
        if row["key"] not in resolved2048_keys
    )
    new_transients = tuple(
        row for row in resolutions4096
        if row["outcome"] == "TRANSIENT"
    )
    features, feature_rows, feature_metadata = M795.feature_table(
        family
    )
    hypotheses = hypothesis_table(
        features,
        catalog,
        open1024,
        resolutions4096,
    )
    pattern = selection_pattern_check(family, new_transients)
    scoring_monotone = all(
        right["surviving_after_this_resolution"]
        <= left["surviving_after_this_resolution"]
        for left, right in zip(
            (
                {
                    "surviving_after_this_resolution":
                        EXPECTED_SEPARATOR_COUNT
                },
                *hypotheses["scoring_rows"],
            ),
            hypotheses["scoring_rows"],
        )
    )
    d_pass = (
        len(feature_rows) == FAMILY_SIZE
        and hypotheses["separator_count"] == EXPECTED_SEPARATOR_COUNT
        and hypotheses["forecast_vector_count"]
        == EXPECTED_FORECAST_VECTOR_COUNT
        and len(
            hypotheses["original_14_consistent_separator_ids"]
        ) == EXPECTED_SEPARATOR_COUNT
        and len(hypotheses["scoring_rows"])
        == len(resolutions4096)
        and all(
            row["correct_separator_count"]
            + row["incorrect_separator_count"]
            + row["unseen_separator_count"]
            == EXPECTED_SEPARATOR_COUNT
            for row in hypotheses["scoring_rows"]
        )
        and scoring_monotone
        and pattern["verification_pass"]
        and sum(
            snapshot4096["family_first_clean_time_census"].values()
        ) == snapshot4096["family_clean_count"]
        and sum(
            snapshot4096["family_residual_period_census"].values()
        ) == snapshot4096["family_cycle_count"]
    )
    check(
        "D_resolution_table_hypothesis_census_and_pattern_check",
        d_pass,
    )
    data(
        "D_RESOLUTION_TABLE",
        {
            "T2048": public_snapshot(snapshot2048),
            "T4096": public_snapshot(snapshot4096),
            "new_resolutions_by_T2048": resolutions2048,
            "additional_resolutions_T2049_T4096": after2048,
            "updated_family_fractions_T2048":
                updated_fractions(snapshot2048),
            "updated_family_fractions_T4096":
                updated_fractions(snapshot4096),
            "continuation_table_sha256": primary["table_sha256"],
        },
    )
    for index, row in enumerate(primary["rows"]):
        data(f"D_KEY_ROW_{index:03d}", row)
    data(
        "D_HYPOTHESIS_TABLE_CONTROL",
        {
            "separator_status": boundaries["separator_status"],
            "forecast_status": boundaries["forecast_status"],
            "original_resolutions_in_consistency_test": len(catalog),
            "original_consistent_separators": len(
                hypotheses["original_14_consistent_separator_ids"]
            ),
            "separator_count": hypotheses["separator_count"],
            "forecast_vector_count":
                hypotheses["forecast_vector_count"],
            "separator_mask_decoding": (
                "hexadecimal bitset; least-significant bit S000, "
                "then S001 through S102"
            ),
            "forecast_table_sha256":
                hypotheses["forecast_table_sha256"],
        },
    )
    for row in hypotheses["separator_catalog"]:
        data("D_SEPARATOR_CATALOG", row)
    for row in hypotheses["vector_catalog"]:
        data("D_FORECAST_VECTOR_CATALOG", row)
    for row in hypotheses["scoring_rows"]:
        data("D_NEW_RESOLUTION_HYPOTHESIS_SCORE", compact_scoring_row(row))
    data(
        "D_SURVIVING_HYPOTHESIS_CENSUS",
        {
            "resolutions_tested": (
                len(catalog) + len(hypotheses["scoring_rows"])
            ),
            "original_resolutions": len(catalog),
            "new_resolutions": len(hypotheses["scoring_rows"]),
            "surviving_separator_count":
                len(hypotheses["surviving_separator_ids"]),
            "surviving_separator_ids":
                hypotheses["surviving_separator_ids"],
            "surviving_separator_mask_hex":
                id_mask_hex(hypotheses["surviving_separator_ids"]),
        },
    )
    data("D_ONE_TICK_SELECTION_PATTERN", pattern)

    replay = run_continuation(
        seed_records,
        checkpoints,
        family,
        open1024,
        script_started,
        fixed_t4096_prefix_count=primary["prefix_count"],
    )
    replay_resolutions = resolution_rows(
        open1024, replay["records"], 4096
    )
    hypothesis_replay = hypothesis_table(
        features,
        catalog,
        open1024,
        replay_resolutions,
    )
    deterministic = (
        replay["deterministic_sha256"]
        == primary["deterministic_sha256"]
        and replay["table_sha256"] == primary["table_sha256"]
        and replay["covered4096"] == primary["covered4096"]
        and replay["remaining2048"] == primary["remaining2048"]
        and replay_resolutions == resolutions4096
        and hypothesis_replay["forecast_table_sha256"]
        == hypotheses["forecast_table_sha256"]
        and hypothesis_replay["scoring_rows"]
        == hypotheses["scoring_rows"]
        and hypothesis_replay["surviving_separator_ids"]
        == hypotheses["surviving_separator_ids"]
    )
    elapsed = monotonic() - script_started
    current_bytes = len(
        ("\n".join(OUTPUT_LINES) + "\n").encode("utf-8")
    )
    e_pass = (
        deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and current_bytes < STDOUT_LIMIT_BYTES - 12 * 1024
        and boundaries["content_vs_dirt"] == "OPEN"
        and boundaries["separator_status"] == "HYPOTHESES_NOT_LAWS"
        and boundaries["forecast_status"] == "HYPOTHESIS_TESTS_ONLY"
        and boundaries["probabilities_assigned"] is False
        and boundaries["statistical_weights_assigned"] is False
        and boundaries["axiom_update_triggered"] is False
        and boundaries["plain_reading"]["declared_named_input_files"]
        <= boundaries["plain_reading"]["maximum_named_input_files"]
    )
    check("E_boundaries_determinism_and_bounds", e_pass)
    data(
        "E_BOUNDARIES_DETERMINISM_BOUNDS",
        {
            "boundaries": boundaries,
            "deterministic": deterministic,
            "primary_continuation_sha256":
                primary["deterministic_sha256"],
            "replay_continuation_sha256":
                replay["deterministic_sha256"],
            "primary_forecast_sha256":
                hypotheses["forecast_table_sha256"],
            "replay_forecast_sha256":
                hypothesis_replay["forecast_table_sha256"],
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes_before_E_and_terminal": current_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    report = {
        "cycle": 797,
        "T1024_counts": identity1024["T1024_counts"],
        "T2048": public_snapshot(snapshot2048),
        "T4096": public_snapshot(snapshot4096),
        "new_resolution_count": len(resolutions4096),
        "new_transient_count": len(new_transients),
        "new_cycle_count": (
            len(resolutions4096) - len(new_transients)
        ),
        "surviving_hypothesis_count":
            len(hypotheses["surviving_separator_ids"]),
        "separator_count": hypotheses["separator_count"],
        "forecast_vector_count": hypotheses["forecast_vector_count"],
        "pattern": pattern["pattern"],
        "coverage": primary["coverage_decision"],
        "runtime_seconds": round(monotonic() - script_started, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "boundaries": boundaries,
        "checks": dict(CHECKS),
        "pass": all(CHECKS.values()),
    }
    report["terminal"] = (
        "CYCLE797_DEEP_HORIZON_CONTINUATION_PASS"
        if report["pass"]
        else "CYCLE797_DEEP_HORIZON_CONTINUATION_HONEST_FAIL"
    )
    report["report_sha256"] = digest(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + compact(report) + "\n"
    stdout_bytes = len(output.encode("utf-8"))
    if stdout_bytes >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal": "CYCLE797_DEEP_HORIZON_CONTINUATION_HONEST_FAIL",
            "failure": "stdout bound exceeded",
            "stdout_bytes": stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "axiom_update_triggered": False,
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        failure = {
            "checks": dict(CHECKS),
            "pass": False,
            "terminal": "CYCLE797_DEEP_HORIZON_CONTINUATION_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
            "axiom_update_triggered": False,
        }
        if OUTPUT_LINES:
            sys.stdout.write("\n".join(OUTPUT_LINES) + "\n")
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
