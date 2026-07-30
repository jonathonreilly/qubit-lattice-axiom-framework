#!/usr/bin/env python3
"""Cycle 795: landed-feature census for resolved postimage outcomes.

This runner reuses the landed Cycle-790/791 machinery to reproduce the
14 resolved keys, then computes a priori features for the complete 176-key
family.  A disjoint resolved-value census is only a hypothesis generator:
its open-key output is labelled as a feature implication, never as a law.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle790_horizon_extension_2026_07_28.py",
    "scripts/frontier_cycle791_open_keys_resolution_2026_07_28.py",
    "scripts/frontier_cycle762_residual_as_content_probe_2026_07_28.py",
    "scripts/frontier_cycle762_residual_probe_independent_check_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle790_horizon_extension_2026_07_28 as M790
import frontier_cycle791_open_keys_resolution_2026_07_28 as M791


EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "bc1a47b591e4b308ef3e57ea7776a56223c76c0eca3867816d408f5021e86ac6",
    AUDIT_INPUT_PATHS[1]:
        "3380b3f0820a74e0f538b54144bb926a2a4be9041ed21ae5181216f481c8a98a",
    AUDIT_INPUT_PATHS[2]:
        "cb5f80cf5d0e169e01561bd9a8665fc8492036398bc0f3eeebe2e326497dbd0d",
    AUDIT_INPUT_PATHS[3]:
        "c8d43dc2c65b851554393c493d016f6341ba9eb8c3a35bb9f361d77a2f16c619",
    AUDIT_INPUT_PATHS[4]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[5]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}

FAMILY_SIZE = 176
RESOLVED_SIZE = 14
OPEN_SIZE = 162
RING_STATIONS = 11
LANDED_CONSTANTS = (130, 11, 2, 5, 12, 288, 6, 3)
PAIR_FEATURE_LIMIT = 24
STDOUT_LIMIT_BYTES = 150 * 1024

EXPECTED_TRANSIENTS = {
    (3, (1, 10)): 252,
    (3, (0, 7)): 371,
}
EXPECTED_CYCLES = {
    **{
        (event, positions): (period, period)
        for event, positions, period in M790.EXPECTED_PERIODIC_KEYS_T64
    },
    (2, (0, 9)): (288, 6),
}

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


def audit_tuple_is_literal() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    matches = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
            matches.append(node.value)
    return (
        len(matches) == 1
        and isinstance(matches[0], ast.Tuple)
        and all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in matches[0].elts
        )
        and ast.literal_eval(matches[0]) == AUDIT_INPUT_PATHS
    )


def anchor_certificate() -> dict[str, object]:
    actual = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "input_sha256": actual,
        "literal_tuple": audit_tuple_is_literal(),
        "module_paths_exact": (
            Path(M790.__file__).resolve()
            == (ROOT / AUDIT_INPUT_PATHS[0]).resolve()
            and Path(M791.__file__).resolve()
            == (ROOT / AUDIT_INPUT_PATHS[1]).resolve()
        ),
        "guarded_imports_clean":
            not M790.CHECKS and not M790.OUTPUT_LINES
            and not M791.CHECKS and not M791.OUTPUT_LINES,
    }
    result["pass"] = (
        actual == EXPECTED_INPUT_SHA256
        and result["literal_tuple"]
        and result["module_paths_exact"]
        and result["guarded_imports_clean"]
    )
    return result


def resolved_catalog(
    script_started: float,
) -> tuple[
    tuple[dict[str, object], ...],
    tuple[Key, ...],
    dict[str, object],
]:
    """Reproduce the Cycle-790/791 resolved catalog and 162 open keys."""

    identity, checkpoints, family = M791.build_identity_and_checkpoints()
    sweep = M791.resolution_sweep(
        checkpoints,
        family,
        script_started,
        fixed_prefix_count=len(checkpoints),
    )
    snapshot = sweep["snapshots"][1024]
    new_records = sweep["records"]

    observed_transients = {
        M791.EXPECTED_BASELINE_CLEAN_KEY: 252,
        **{
            key: new_records[key]["first_clean"]
            for key in snapshot["clean_keys"]
        },
    }
    observed_cycles = {
        **{
            (event, positions): (period, period)
            for event, positions, period
            in M790.EXPECTED_PERIODIC_KEYS_T64
        },
        **{
            key: (
                new_records[key]["state_period"],
                new_records[key]["residual_period"],
            )
            for key in snapshot["cycle_keys"]
        },
    }
    rows = []
    for key, first_clean in sorted(observed_transients.items()):
        rows.append(
            {
                "k": key,
                "v": "TRANSIENT",
                "first_clean": first_clean,
                "state_period": None,
                "residual_period": None,
            }
        )
    for key, periods in sorted(observed_cycles.items()):
        rows.append(
            {
                "k": key,
                "v": "CYCLE",
                "first_clean": None,
                "state_period": periods[0],
                "residual_period": periods[1],
            }
        )

    controls = {
        "identity_pass": identity["pass"],
        "baseline": identity["cycle790_facts"],
        "observed_transients": observed_transients,
        "observed_cycles": observed_cycles,
        "T1024_family_counts": {
            "transient": snapshot["family_clean_count"],
            "cycle": snapshot["family_cycle_count"],
            "open": snapshot["family_open_count"],
            "uncovered": snapshot["family_uncovered_count"],
        },
        "full_T1024_prefix": sweep["prefix_count"] == len(checkpoints),
        "digest_collisions": sum(
            record["digest_collisions"]
            for record in new_records.values()
        ),
        "exact_new_cycle_confirmations": sum(
            record["exact_recurrence_confirmations"]
            for record in new_records.values()
        ),
        "catalog_sha256": digest(rows),
        "resolution_sha256": sweep["deterministic_sha256"],
    }
    controls["pass"] = (
        identity["pass"]
        and observed_transients == EXPECTED_TRANSIENTS
        and observed_cycles == EXPECTED_CYCLES
        and len(rows) == RESOLVED_SIZE
        and snapshot["family_clean_count"] == 2
        and snapshot["family_cycle_count"] == 12
        and snapshot["family_open_count"] == OPEN_SIZE
        and snapshot["family_uncovered_count"] == 0
        and controls["full_T1024_prefix"]
        and controls["digest_collisions"] == 0
        and controls["exact_new_cycle_confirmations"] == 1
    )
    return tuple(rows), tuple(snapshot["open_keys"]), {
        "controls": controls,
        "family": family,
    }


def feature_schema() -> tuple[str, ...]:
    base = (
        "epoch",
        "epoch_parity",
        "epoch_direction",
        "left",
        "right",
        "clockwise_gap",
        "counterclockwise_gap",
        "ring_separation",
        "ring_long_distance",
        "short_orientation",
        "direction_short_alignment",
        "position_sum",
        "position_product",
        "occupancy_mask",
        "chord_midpoint_mod11",
        "short_arc_start",
        "short_arc_end",
        "left_parity",
        "right_parity",
        "parity_code",
        "same_position_parity",
        "epoch_sum_parity",
        "initial_residual_weight",
        "initial_support_size",
        "support_signature_id",
        "support_kind_mask",
        "support_source_count",
        "support_bank_count",
        "support_link_count",
        "support_bank0_count",
        "support_bank1_count",
        "support_bank_imbalance",
        "support_coordinate_index_sum",
    )
    alignment = tuple(
        f"{stem}_mod_{constant}"
        for constant in LANDED_CONSTANTS
        for stem in (
            "left",
            "right",
            "position_sum",
            "clockwise_gap",
            "ring_separation",
            "epoch",
        )
    )
    same_residue = tuple(
        f"same_position_residue_mod_{constant}"
        for constant in LANDED_CONSTANTS
    )
    return base + alignment + same_residue


FEATURE_SCHEMA = feature_schema()
PAIR_FEATURES = (
    "epoch",
    "epoch_parity",
    "epoch_direction",
    "left",
    "right",
    "clockwise_gap",
    "counterclockwise_gap",
    "ring_separation",
    "short_orientation",
    "direction_short_alignment",
    "position_sum",
    "position_product",
    "occupancy_mask",
    "chord_midpoint_mod11",
    "parity_code",
    "same_position_parity",
    "epoch_sum_parity",
    "initial_residual_weight",
    "support_signature_id",
    "support_kind_mask",
    "support_source_count",
    "support_bank_count",
    "support_link_count",
    "support_bank_imbalance",
)


def feature_table(
    family: dict[str, object],
) -> tuple[
    dict[Key, tuple[int, ...]],
    tuple[tuple[int, ...], ...],
    dict[str, object],
]:
    """Compute only key geometry and the landed initial postimage support."""

    canonical_supports = {
        key: M790.canonical_support(support)
        for key, support in family["residues"].items()
    }
    support_classes = {
        support: index
        for index, support in enumerate(
            sorted(set(canonical_supports.values()))
        )
    }
    features: dict[Key, tuple[int, ...]] = {}
    rows = []
    directions = family["summary"]["directions"]

    for key in sorted(family["states"]):
        epoch, (left, right) = key
        clockwise = (right - left) % RING_STATIONS
        counterclockwise = (left - right) % RING_STATIONS
        separation = min(clockwise, counterclockwise)
        long_distance = max(clockwise, counterclockwise)
        short_orientation = 1 if clockwise < counterclockwise else -1
        epoch_direction = 1 if directions[epoch] == (1, 0) else -1
        short_start = left if short_orientation == 1 else right
        short_end = right if short_orientation == 1 else left
        support = canonical_supports[key]
        source_count = sum(row[0] == "source" for row in support)
        bank_count = sum(row[0] == "bank" for row in support)
        link_count = sum(row[0] == "link" for row in support)
        bank0_count = sum(
            row[0] == "bank" and row[2] == 0 for row in support
        )
        bank1_count = sum(
            row[0] == "bank" and row[2] == 1 for row in support
        )
        kind_mask = (
            source_count > 0
        ) | ((bank_count > 0) << 1) | ((link_count > 0) << 2)

        values = [
            epoch,
            epoch % 2,
            epoch_direction,
            left,
            right,
            clockwise,
            counterclockwise,
            separation,
            long_distance,
            short_orientation,
            epoch_direction * short_orientation,
            left + right,
            left * right,
            (1 << left) | (1 << right),
            (6 * (left + right)) % RING_STATIONS,
            short_start,
            short_end,
            left % 2,
            right % 2,
            2 * (left % 2) + right % 2,
            int(left % 2 == right % 2),
            (epoch + left + right) % 2,
            len(support),
            len(support),
            support_classes[support],
            int(kind_mask),
            source_count,
            bank_count,
            link_count,
            bank0_count,
            bank1_count,
            bank1_count - bank0_count,
            sum(row[2] for row in support),
        ]
        for constant in LANDED_CONSTANTS:
            values.extend(
                (
                    left % constant,
                    right % constant,
                    (left + right) % constant,
                    clockwise % constant,
                    separation % constant,
                    epoch % constant,
                )
            )
        values.extend(
            int(left % constant == right % constant)
            for constant in LANDED_CONSTANTS
        )
        feature_row = tuple(map(int, values))
        if len(feature_row) != len(FEATURE_SCHEMA):
            raise AssertionError(
                ("feature schema mismatch", len(feature_row))
            )
        features[key] = feature_row
        rows.append((epoch, left, right, *feature_row))

    metadata = {
        "row_prefix": ("epoch_key", "left_key", "right_key"),
        "feature_schema": FEATURE_SCHEMA,
        "landed_alignment_constants": {
            "orbit_length": 130,
            "station_count": 11,
            "bank_sizes": (2, 5, 12),
            "state_and_residual_periods_seen": (288, 6, 2, 3),
        },
        "parity_orientation_basis": (
            "key parity; canonical left<right ring orientation; "
            "landed epoch endpoint direction"
        ),
        "support_basis": (
            "Cycle-790 residual_support of the landed t=0 postimage"
        ),
        "support_classes": len(support_classes),
        "pair_feature_limit": PAIR_FEATURE_LIMIT,
        "pair_feature_basis": PAIR_FEATURES,
        "table_sha256": digest(rows),
    }
    return features, tuple(rows), metadata


def value_for(
    row: tuple[int, ...],
    names: tuple[str, ...],
    feature_indices: dict[str, int],
) -> tuple[int, ...]:
    return tuple(row[feature_indices[name]] for name in names)


def candidate_result(
    names: tuple[str, ...],
    features: dict[Key, tuple[int, ...]],
    transient_keys: tuple[Key, ...],
    cycle_keys: tuple[Key, ...],
    open_keys: tuple[Key, ...],
    feature_indices: dict[str, int],
) -> dict[str, object]:
    transient_groups: dict[tuple[int, ...], list[Key]] = {}
    cycle_groups: dict[tuple[int, ...], list[Key]] = {}
    for key in transient_keys:
        transient_groups.setdefault(
            value_for(features[key], names, feature_indices), []
        ).append(key)
    for key in cycle_keys:
        cycle_groups.setdefault(
            value_for(features[key], names, feature_indices), []
        ).append(key)
    overlap = sorted(set(transient_groups) & set(cycle_groups))

    remove_to_clean = []
    for value in overlap:
        transient_group = transient_groups[value]
        cycle_group = cycle_groups[value]
        if len(transient_group) <= len(cycle_group):
            remove_to_clean.extend(transient_group)
        else:
            remove_to_clean.extend(cycle_group)

    margin = min(
        (
            sum(abs(left - right) for left, right in zip(tvalue, cvalue))
            for tvalue in transient_groups
            for cvalue in cycle_groups
        ),
        default=0,
    )
    implications = {"TRANSIENT": 0, "CYCLE": 0, "UNSEEN": 0}
    transient_values = set(transient_groups)
    cycle_values = set(cycle_groups)
    for key in open_keys:
        value = value_for(features[key], names, feature_indices)
        if value in transient_values and value not in cycle_values:
            implication = "TRANSIENT"
        elif value in cycle_values and value not in transient_values:
            implication = "CYCLE"
        else:
            implication = "UNSEEN"
        implications[implication] += 1

    return {
        "f": names,
        "dimension": len(names),
        "overlap_values": overlap,
        "violations_to_clean": len(remove_to_clean),
        "remove_to_clean": tuple(sorted(remove_to_clean)),
        "margin_L1": margin,
        "open_implication_counts": implications,
        "open_classified": OPEN_SIZE - implications["UNSEEN"],
    }


def discrimination_census(
    features: dict[Key, tuple[int, ...]],
    catalog: tuple[dict[str, object], ...],
    open_keys: tuple[Key, ...],
) -> dict[str, object]:
    transient_keys = tuple(
        sorted(row["k"] for row in catalog if row["v"] == "TRANSIENT")
    )
    cycle_keys = tuple(
        sorted(row["k"] for row in catalog if row["v"] == "CYCLE")
    )
    feature_indices = {
        name: index for index, name in enumerate(FEATURE_SCHEMA)
    }
    candidates = [(name,) for name in FEATURE_SCHEMA]
    candidates.extend(combinations(PAIR_FEATURES, 2))

    clean = []
    near = []
    for names0 in candidates:
        names = tuple(names0)
        result = candidate_result(
            names,
            features,
            transient_keys,
            cycle_keys,
            open_keys,
            feature_indices,
        )
        if result["violations_to_clean"] == 0:
            clean.append(result)
        elif result["violations_to_clean"] == 1:
            near.append(result)

    clean.sort(
        key=lambda row: (
            -row["open_classified"],
            row["dimension"],
            -row["margin_L1"],
            row["f"],
        )
    )
    near.sort(
        key=lambda row: (
            -row["open_classified"],
            row["dimension"],
            row["f"],
        )
    )
    best = clean[0] if clean else None
    forecast = ()
    if best is not None:
        transient_values = {
            value_for(features[key], best["f"], feature_indices)
            for key in transient_keys
        }
        cycle_values = {
            value_for(features[key], best["f"], feature_indices)
            for key in cycle_keys
        }
        forecast = tuple(
            {
                "k": key,
                "imp": (
                    "TRANSIENT"
                    if value_for(
                        features[key], best["f"], feature_indices
                    ) in transient_values
                    else "CYCLE"
                    if value_for(
                        features[key], best["f"], feature_indices
                    ) in cycle_values
                    else "UNSEEN"
                ),
            }
            for key in open_keys
        )

    return {
        "single_features_tested": len(FEATURE_SCHEMA),
        "pair_features_in_basis": len(PAIR_FEATURES),
        "pairs_tested": len(tuple(combinations(PAIR_FEATURES, 2))),
        "candidates_tested": len(candidates),
        "clean": tuple(clean),
        "near": tuple(near),
        "best": best,
        "forecast": forecast,
        "result_sha256": digest(
            {
                "clean": clean,
                "near": near,
                "best": best,
                "forecast": forecast,
            }
        ),
    }


def boundaries() -> dict[str, object]:
    return {
        "features_are_data": True,
        "separator_status": "HYPOTHESIS_GENERATOR_NOT_A_LAW",
        "forecast_status": "FEATURE_IMPLICATION_ONLY_NOT_A_CLAIM",
        "probabilities_assigned": False,
        "statistical_weights_assigned": False,
        "axiom_update_triggered": False,
        "scope": "FINITE_14_RESOLVED_KEY_DISCRIMINATION_CENSUS",
        "plain_reading": {
            "declared_named_input_files": len(AUDIT_INPUT_PATHS),
            "maximum_named_input_files": 6,
            "docs_read": 0,
            "ledgers_read": 0,
        },
    }


def compact_candidate(row: dict[str, object]) -> dict[str, object]:
    return {
        "f": row["f"],
        "dimension": row["dimension"],
        "margin_L1": row["margin_L1"],
        "violations_to_clean": row["violations_to_clean"],
        "remove_to_clean": row["remove_to_clean"],
        "open_implication_counts": row["open_implication_counts"],
        "open_classified": row["open_classified"],
    }


def run() -> int:
    started = monotonic()
    boundary = boundaries()

    anchors = anchor_certificate()
    catalog, open_keys, landed = resolved_catalog(started)
    controls = landed["controls"]
    a_pass = (
        anchors["pass"]
        and controls["pass"]
        and tuple(sorted(row["k"] for row in catalog))
        == tuple(sorted(set(EXPECTED_TRANSIENTS) | set(EXPECTED_CYCLES)))
        and len(open_keys) == OPEN_SIZE
        and not (
            set(open_keys)
            & (set(EXPECTED_TRANSIENTS) | set(EXPECTED_CYCLES))
        )
    )
    check("A_anchors_and_resolved_key_identity_controls", a_pass)
    data(
        "A_ANCHORS",
        {
            "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
            "input_sha256": anchors["input_sha256"],
            "literal_tuple": anchors["literal_tuple"],
            "guarded_imports_clean": anchors["guarded_imports_clean"],
        },
    )
    data("A_RESOLVED_CATALOG_14", catalog)
    data(
        "A_IDENTITY_CONTROLS",
        {
            key: value
            for key, value in controls.items()
            if key not in {"observed_transients", "observed_cycles"}
        },
    )

    features, table_rows, metadata = feature_table(landed["family"])
    b_pass = (
        len(features) == len(table_rows) == FAMILY_SIZE
        and set(features) == set(landed["family"]["states"])
        and len(FEATURE_SCHEMA) == len(set(FEATURE_SCHEMA))
        and len(PAIR_FEATURES) == PAIR_FEATURE_LIMIT
        and set(PAIR_FEATURES) <= set(FEATURE_SCHEMA)
        and all(
            len(row) == 3 + len(FEATURE_SCHEMA)
            for row in table_rows
        )
        and landed["family"]["summary"]["pass"]
        and metadata["support_classes"] == 25
    )
    check("B_full_176_key_landed_feature_table", b_pass)
    data("B_FEATURE_SCHEMA", metadata)
    data("B_FULL_TABLE_176", table_rows)

    discrimination = discrimination_census(
        features, catalog, open_keys
    )
    candidate_count = (
        len(FEATURE_SCHEMA)
        + len(tuple(combinations(PAIR_FEATURES, 2)))
    )
    c_pass = (
        discrimination["single_features_tested"] == len(FEATURE_SCHEMA)
        and discrimination["pair_features_in_basis"]
        == PAIR_FEATURE_LIMIT
        and discrimination["pairs_tested"]
        == len(tuple(combinations(PAIR_FEATURES, 2)))
        and discrimination["candidates_tested"] == candidate_count
        and all(
            row["violations_to_clean"] == 0
            and row["margin_L1"] > 0
            for row in discrimination["clean"]
        )
        and all(
            row["violations_to_clean"] == 1
            and row["margin_L1"] == 0
            for row in discrimination["near"]
        )
    )
    check("C_all_single_and_bounded_pair_discrimination_tests", c_pass)
    data(
        "C_TEST_BOUNDS",
        {
            "single_features_tested":
                discrimination["single_features_tested"],
            "pair_feature_basis": PAIR_FEATURES,
            "pairs_tested": discrimination["pairs_tested"],
            "candidates_tested": discrimination["candidates_tested"],
            "zero_overlap_definition":
                "resolved transient-value set disjoint from "
                "resolved cycle-value set",
            "margin_definition":
                "minimum L1 distance between resolved class values",
            "near_definition":
                "minimum one resolved-row removal makes value sets disjoint",
            "clean_separator_count": len(discrimination["clean"]),
            "near_separator_count": len(discrimination["near"]),
        },
    )
    for row in discrimination["clean"]:
        data("C_CLEAN_SEPARATOR", compact_candidate(row))
    for row in discrimination["near"]:
        data("C_NEAR_SEPARATOR_ONE_VIOLATION", compact_candidate(row))

    best = discrimination["best"]
    verdict = "SEPARATOR_FOUND" if best is not None else "NO_SEPARATOR"
    forecast = discrimination["forecast"]
    forecast_counts = {
        label: sum(row["imp"] == label for row in forecast)
        for label in ("TRANSIENT", "CYCLE", "UNSEEN")
    }
    d_pass = (
        (
            best is not None
            and len(discrimination["clean"]) > 0
            and len(forecast) == OPEN_SIZE
            and sum(forecast_counts.values()) == OPEN_SIZE
            and tuple(row["k"] for row in forecast) == open_keys
        )
        or (
            best is None
            and not discrimination["clean"]
            and not forecast
        )
    )
    check("D_verdict_and_open_key_feature_implication_forecast", d_pass)
    data(
        "D_VERDICT",
        {
            "verdict": verdict,
            "best_separator":
                compact_candidate(best) if best is not None else None,
            "interpretation": boundary["separator_status"],
            "forecast_label": boundary["forecast_status"],
        },
    )
    if best is not None:
        data(
            "D_HYPOTHESIS_FEATURE_IMPLICATION_FORECAST_162",
            {
                "feature": best["f"],
                "not_a_claim": True,
                "counts": forecast_counts,
                "rows": forecast,
            },
        )

    features_replay, table_replay, metadata_replay = feature_table(
        landed["family"]
    )
    discrimination_replay = discrimination_census(
        features_replay, catalog, open_keys
    )
    deterministic = (
        features_replay == features
        and table_replay == table_rows
        and metadata_replay == metadata
        and discrimination_replay["result_sha256"]
        == discrimination["result_sha256"]
        and discrimination_replay["forecast"] == forecast
    )
    elapsed = monotonic() - started
    current_bytes = len(
        ("\n".join(OUTPUT_LINES) + "\n").encode("utf-8")
    )
    e_pass = (
        deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and current_bytes < STDOUT_LIMIT_BYTES - 8192
        and boundary["features_are_data"]
        and boundary["separator_status"]
        == "HYPOTHESIS_GENERATOR_NOT_A_LAW"
        and boundary["forecast_status"]
        == "FEATURE_IMPLICATION_ONLY_NOT_A_CLAIM"
        and boundary["probabilities_assigned"] is False
        and boundary["statistical_weights_assigned"] is False
        and boundary["axiom_update_triggered"] is False
        and boundary["plain_reading"]["declared_named_input_files"] <= 6
    )
    check("E_boundaries_determinism_runtime_and_stdout_bounds", e_pass)
    data(
        "E_BOUNDARIES_AND_BOUNDS",
        {
            "boundaries": boundary,
            "deterministic": deterministic,
            "feature_table_sha256": metadata["table_sha256"],
            "discrimination_sha256":
                discrimination["result_sha256"],
            "replay_discrimination_sha256":
                discrimination_replay["result_sha256"],
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes_before_E_and_terminal": current_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    report = {
        "cycle": 795,
        "verdict": verdict,
        "best_separator":
            compact_candidate(best) if best is not None else None,
        "resolved": {
            "transients": len(EXPECTED_TRANSIENTS),
            "cycles": len(EXPECTED_CYCLES),
            "open": len(open_keys),
        },
        "feature_rows": len(table_rows),
        "features": len(FEATURE_SCHEMA),
        "pairs_tested": discrimination["pairs_tested"],
        "clean_separators": len(discrimination["clean"]),
        "near_separators": len(discrimination["near"]),
        "forecast_implication_counts": forecast_counts,
        "feature_table_sha256": metadata["table_sha256"],
        "discrimination_sha256": discrimination["result_sha256"],
        "runtime_seconds": round(monotonic() - started, 6),
        "boundaries": boundary,
        "checks": dict(CHECKS),
        "pass": all(CHECKS.values()),
    }
    report["terminal"] = (
        "CYCLE795_DISCRIMINATOR_CENSUS_PASS"
        if report["pass"]
        else "CYCLE795_DISCRIMINATOR_CENSUS_HONEST_FAIL"
    )
    report["report_sha256"] = digest(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + compact(report) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal": "CYCLE795_DISCRIMINATOR_CENSUS_HONEST_FAIL",
            "failure": "stdout bound exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
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
            "terminal": "CYCLE795_DISCRIMINATOR_CENSUS_HONEST_FAIL",
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
