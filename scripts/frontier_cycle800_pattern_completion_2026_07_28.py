#!/usr/bin/env python3
"""Cycle 800: monitored-selector completion at every known transient.

This bounded fixture calculation reproduces the six supplied transient
moments, applies the unchanged four-exclusion monitored selector, and tests
cross-stratum simultaneity.  A supplied horizon index t means exactly t+1
complete controller orbits.  It is neither physical time nor actuality.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
    "scripts/frontier_cycle762_residual_as_content_probe_2026_07_28.py",
    "scripts/frontier_cycle762_residual_probe_independent_check_2026_07_28.py",
    "scripts/frontier_cycle784_full_strata_ties_2026_07_28.py",
    "scripts/frontier_cycle794_second_selection_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from hashlib import sha1, sha256
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
WINDOW_OFFSETS = tuple(range(1, 7))

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[3]:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    AUDIT_INPUT_PATHS[4]:
        "cb5f80cf5d0e169e01561bd9a8665fc8492036398bc0f3eeebe2e326497dbd0d",
    AUDIT_INPUT_PATHS[5]:
        "c8d43dc2c65b851554393c493d016f6341ba9eb8c3a35bb9f361d77a2f16c619",
    AUDIT_INPUT_PATHS[6]:
        "b532563da6aa8e84ae8aae2c4ad14c10a50d45d43c020ca2107fd48b79dc8a30",
    AUDIT_INPUT_PATHS[7]:
        "5fcb9f015b7690df833a3b3d1dc7bdc81162e066f1f25d34d420d8779c563582",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
    AUDIT_INPUT_PATHS[2]: "0a8f4562d28f12ed64130b3c3b23fccab677d333",
    AUDIT_INPUT_PATHS[3]: "4e23e03ecc5f92a0b8348bfa526eb5b2f2b09dd0",
    AUDIT_INPUT_PATHS[4]: "87ba84671c246fe3b7473980d395ea94443921fc",
    AUDIT_INPUT_PATHS[5]: "3eff0f787a12cacf504324209f578f0c1df91c90",
    AUDIT_INPUT_PATHS[6]: "b718499f3b6fd1498b9c99e8b87926dcc057f385",
    AUDIT_INPUT_PATHS[7]: "a6debf306793270a4cda61638b619d4ad55dea69",
}

# (label, k, zero-based event, family representative/target, supplied moment)
TRANSIENTS = (
    ("K2_T252", 2, 3, (1, 10), 252),
    ("K2_T371", 2, 3, (0, 7), 371),
    ("K3_T444", 3, 2, (0, 2, 5), 444),
    ("K3_T532", 3, 3, (0, 2, 5), 532),
    ("K3_T681", 3, 1, (0, 2, 4), 681),
    ("K3_T1385", 3, 2, (0, 2, 4), 1385),
)
NEW_TEST_LABELS = ("K3_T532", "K3_T681", "K3_T1385")
KNOWN_CONTROL_LABELS = ("K2_T252", "K2_T371", "K3_T444")

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def check(label: str, condition: bool, detail: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )
    return passed


def source_anchors() -> dict[str, object]:
    runner_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignment = next(
        node
        for node in runner_tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    )
    literal_tuple = (
        isinstance(assignment.value, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in assignment.value.elts
        )
        and tuple(ast.literal_eval(assignment.value)) == AUDIT_INPUT_PATHS
    )
    rows = {}
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        payload = path.read_bytes() if path.is_file() else b""
        observed_sha256 = sha256(payload).hexdigest()
        observed_blob = git_blob_sha(payload)
        rows[relative] = {
            "existing_disk_path": path.is_file(),
            "sha256": observed_sha256,
            "expected_sha256": EXPECTED_SHA256[relative],
            "git_blob_sha": observed_blob,
            "expected_git_blob_sha": EXPECTED_GIT_BLOBS[relative],
            "match": (
                path.is_file()
                and observed_sha256 == EXPECTED_SHA256[relative]
                and observed_blob == EXPECTED_GIT_BLOBS[relative]
            ),
        }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_tuple": literal_tuple,
        "path_count": len(AUDIT_INPUT_PATHS),
        "existing_disk_only": all(row["existing_disk_path"] for row in rows.values()),
        "scripts_only_no_docs_or_ledgers": all(
            relative.startswith("scripts/") for relative in AUDIT_INPUT_PATHS
        ),
        "rows": rows,
    }
    result["pass"] = (
        literal_tuple
        and len(AUDIT_INPUT_PATHS) <= 8
        and result["existing_disk_only"]
        and result["scripts_only_no_docs_or_ledgers"]
        and all(row["match"] for row in rows.values())
    )
    return result


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def occupied_sites(config: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(station for station, bit in enumerate(config) if bit)


def pairwise_separated(config: tuple[int, ...]) -> bool:
    return not any(
        config[station] and config[(station + 1) % RING_STATIONS]
        for station in range(RING_STATIONS)
    )


def configuration_census() -> tuple[tuple[int, ...], ...]:
    rows = []
    for mask in range(1 << RING_STATIONS):
        config = tuple(
            (mask >> station) & 1 for station in range(RING_STATIONS)
        )
        if pairwise_separated(config):
            rows.append(config)
    return tuple(rows)


def configuration_families(
    configurations: tuple[tuple[int, ...], ...],
) -> dict[int, dict[tuple[int, ...], tuple[tuple[int, ...], ...]]]:
    grouped: dict[
        int, dict[tuple[int, ...], set[tuple[int, ...]]]
    ] = {}
    for config in configurations:
        positions = occupied_sites(config)
        representative = (
            min(
                rotate_positions(positions, shift)
                for shift in range(RING_STATIONS)
            )
            if positions
            else ()
        )
        grouped.setdefault(len(positions), {}).setdefault(
            representative, set()
        ).add(positions)
    return {
        k: {
            representative: tuple(sorted(alternatives))
            for representative, alternatives in sorted(families.items())
        }
        for k, families in sorted(grouped.items())
    }


def k_epoch_fixtures(
    bank_count: int,
) -> tuple[tuple[int, tuple[int, int], tuple[object, ...], Any], ...]:
    program = K.interleaved_program(bank_count)
    banks, links = K.B.chain_genesis(bank_count)
    state = K.M.pack_state(banks, links)
    rows = []
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        expected = K.A.apply_semantic(
            before, K.M.global_allocator_word(bank_count)
        )
        rows.append((event, direction, program, before))
        state = expected
    return tuple(rows)


def synchronous_composition_word(
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> tuple[object, ...]:
    positions = tuple(token_positions)
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station in range(len(program)):
            if station in live:
                word.extend(K.mapped_macro(program[station]))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    return tuple(word)


def clean_postimage(after: Any, bank_count: int) -> bool:
    banks, links = K.M.unpack_state(after, bank_count)
    return not any(
        (
            after[K.R3.X.SOURCE_POINTER],
            any(
                bank[wire]
                for bank in banks
                for wire in (
                    K.A.POINTER,
                    K.A.U_TO_V,
                    K.A.V_TO_U,
                    K.A.DIRECTION_OK,
                    *K.A.FRESH,
                    *K.A.ZERO_WORK,
                    K.A.TOKEN_OK,
                )
            ),
            any(any(link) for link in links),
        )
    )


def reverse_extended_horizon(
    after: Any,
    final_a: tuple[int, ...],
    final_b: tuple[int, ...],
    program: tuple[object, ...],
    horizon_t: int,
) -> tuple[Any, tuple[int, ...], tuple[int, ...]]:
    restored = after
    inverse_a = final_a
    inverse_b = final_b
    for _orbit in range(horizon_t + 1):
        for _step in range(len(program)):
            restored, inverse_a, inverse_b = K.apply_controller_step(
                restored,
                program,
                inverse_a,
                inverse_b,
                reverse=True,
            )
    return restored, inverse_a, inverse_b


Snapshot = tuple[
    Any,
    Any,
    tuple[int, ...],
    tuple[int, ...],
]
ConfigurationKey = tuple[int, tuple[int, ...]]


def build_snapshot_cache(
    fixtures_by_event: dict[
        int, tuple[int, tuple[int, int], tuple[object, ...], Any]
    ],
    needed: dict[ConfigurationKey, set[int]],
    transient_keys: frozenset[ConfigurationKey],
) -> tuple[
    dict[tuple[int, tuple[int, ...], int], Snapshot],
    dict[ConfigurationKey, int | None],
]:
    snapshots: dict[tuple[int, tuple[int, ...], int], Snapshot] = {}
    first_clean: dict[ConfigurationKey, int | None] = {
        key: None for key in transient_keys
    }
    for event, positions in sorted(needed):
        requested = needed[(event, positions)]
        _event, _direction, program, before = fixtures_by_event[event]
        tokens = tuple(
            int(station in positions) for station in range(len(program))
        )
        rail_a = tokens
        rail_b = tuple(value ^ value for value in tokens)
        actual = before
        expected = before
        word = synchronous_composition_word(program, positions)
        key = (event, positions)
        for horizon_t in range(max(requested) + 1):
            for _step in range(len(program)):
                actual, rail_a, rail_b = K.apply_controller_step(
                    actual, program, rail_a, rail_b
                )
            expected = K.A.apply_semantic(expected, word)
            if (
                key in transient_keys
                and first_clean[key] is None
                and clean_postimage(actual, FIXTURE_BANKS)
            ):
                first_clean[key] = horizon_t
            if horizon_t in requested:
                snapshots[(event, positions, horizon_t)] = (
                    actual,
                    expected,
                    rail_a,
                    rail_b,
                )
    return snapshots, first_clean


def evaluate_snapshot(
    fixtures_by_event: dict[
        int, tuple[int, tuple[int, int], tuple[object, ...], Any]
    ],
    snapshots: dict[tuple[int, tuple[int, ...], int], Snapshot],
    event: int,
    positions: tuple[int, ...],
    horizon_t: int,
) -> dict[str, object]:
    _event, _direction, program, before = fixtures_by_event[event]
    actual, expected, rail_a, rail_b = snapshots[
        (event, positions, horizon_t)
    ]
    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    zeros = tuple(value ^ value for value in tokens)
    restored, inverse_a, inverse_b = reverse_extended_horizon(
        actual, rail_a, rail_b, program, horizon_t
    )
    conditions = {
        "synchronous_composition": actual == expected,
        "token_rail_return": rail_a == tokens and rail_b == zeros,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "clean_postimage": clean_postimage(actual, FIXTURE_BANKS),
    }
    failed = tuple(
        name for name, passed in conditions.items() if not passed
    )
    return {
        "event": event,
        "positions": positions,
        "horizon_t_SUPPLIED": horizon_t,
        "complete_orbits_applied": horizon_t + 1,
        "conditions": conditions,
        "failed_exclusions": failed,
        "selected": not failed,
        "postimage_sha256":
            sha256(str(actual).encode("ascii")).hexdigest(),
    }


def classify_selection(
    target: tuple[int, ...],
    survivors: tuple[tuple[int, ...], ...],
) -> str:
    if target not in survivors:
        return "STILL_EXCLUDED"
    if len(survivors) == 1:
        return "UNIQUE_SURVIVOR"
    return "TIE"


def exclusion_certificate(
    rows: tuple[dict[str, object], ...],
) -> dict[str, object]:
    invariant_names = (
        "synchronous_composition",
        "token_rail_return",
        "literal_inverse",
    )
    result = {
        "row_count": len(rows),
        "invariant_exclusions_all_pass": all(
            all(row["conditions"][name] for name in invariant_names)
            for row in rows
        ),
        "selected_rows_have_no_failures": all(
            (not row["selected"]) or not row["failed_exclusions"]
            for row in rows
        ),
        "excluded_rows_fail_clean_only": all(
            row["selected"]
            or row["failed_exclusions"] == ("clean_postimage",)
            for row in rows
        ),
        "per_row": tuple(
            {
                "positions": row["positions"],
                "selected": row["selected"],
                "failed_exclusions": row["failed_exclusions"],
            }
            for row in rows
        ),
    }
    result["pass"] = (
        result["invariant_exclusions_all_pass"]
        and result["selected_rows_have_no_failures"]
        and result["excluded_rows_fail_clean_only"]
    )
    return result


def run_experiment() -> dict[str, object]:
    configurations = configuration_census()
    families = configuration_families(configurations)
    fixtures = k_epoch_fixtures(FIXTURE_BANKS)
    fixtures_by_event = {row[0]: row for row in fixtures}
    transient_by_label = {row[0]: row for row in TRANSIENTS}
    all_moments = tuple(row[4] for row in TRANSIENTS)

    k2_representatives = tuple(families[2])
    k2_battery = tuple(
        sorted(
            set(k2_representatives)
            | {
                transient_by_label["K2_T252"][3],
                transient_by_label["K2_T371"][3],
            }
        )
    )
    batteries: dict[str, tuple[tuple[int, ...], ...]] = {}
    for label, k, _event, target, _moment in TRANSIENTS:
        batteries[label] = (
            k2_battery if k == 2 else families[k][target]
        )

    needed: dict[ConfigurationKey, set[int]] = {}

    def need(event: int, positions: tuple[int, ...], horizon_t: int) -> None:
        needed.setdefault((event, positions), set()).add(horizon_t)

    for label, _k, event, target, moment in TRANSIENTS:
        for positions in batteries[label]:
            need(event, positions, moment)
        need(event, target, moment - 1)
        for offset in WINDOW_OFFSETS:
            need(event, target, moment + offset)
        for matrix_moment in all_moments:
            need(event, target, matrix_moment)

    transient_keys = frozenset(
        (event, target)
        for _label, _k, event, target, _moment in TRANSIENTS
    )
    snapshots, first_clean = build_snapshot_cache(
        fixtures_by_event, needed, transient_keys
    )

    selections = {}
    for label, k, event, target, moment in TRANSIENTS:
        rows = tuple(
            evaluate_snapshot(
                fixtures_by_event,
                snapshots,
                event,
                positions,
                moment,
            )
            for positions in batteries[label]
        )
        survivors = tuple(
            row["positions"] for row in rows if row["selected"]
        )
        control = evaluate_snapshot(
            fixtures_by_event,
            snapshots,
            event,
            target,
            moment - 1,
        )
        window = tuple(
            evaluate_snapshot(
                fixtures_by_event,
                snapshots,
                event,
                target,
                moment + offset,
            )
            for offset in WINDOW_OFFSETS
        )
        _event, direction, program, _before = fixtures_by_event[event]
        selections[label] = {
            "label": label,
            "k": k,
            "event": event,
            "direction": direction,
            "target": target,
            "moment_SUPPLIED": moment,
            "battery_basis": (
                "Cycle-758 k=2 representatives plus both supplied "
                "transient configurations"
                if k == 2
                else "complete 11-member Cycle-784 translation family"
            ),
            "battery_size": len(batteries[label]),
            "program_stations": len(program),
            "rows": rows,
            "survivors": survivors,
            "survivor_count": len(survivors),
            "classification": classify_selection(target, survivors),
            "moment_minus_one_veto": control,
            "window_plus_1_through_6": window,
            "exclusion_certificate": exclusion_certificate(rows),
        }

    identity_rows = tuple(
        {
            "label": label,
            "k": k,
            "event": event,
            "positions": target,
            "expected_first_clean_t_SUPPLIED": moment,
            "observed_first_clean_t": first_clean[(event, target)],
            "moment_minus_one_clean":
                selections[label]["moment_minus_one_veto"][
                    "conditions"
                ]["clean_postimage"],
            "moment_clean": next(
                row
                for row in selections[label]["rows"]
                if row["positions"] == target
            )["conditions"]["clean_postimage"],
        }
        for label, k, event, target, moment in TRANSIENTS
    )

    matrix_rows = []
    for row_label, _row_k, _row_event, _row_target, moment in TRANSIENTS:
        cells = []
        for (
            column_label,
            column_k,
            column_event,
            column_target,
            _column_moment,
        ) in TRANSIENTS:
            actual = snapshots[
                (column_event, column_target, moment)
            ][0]
            cells.append(
                {
                    "label": column_label,
                    "k": column_k,
                    "event": column_event,
                    "positions": column_target,
                    "clean": clean_postimage(actual, FIXTURE_BANKS),
                }
            )
        matrix_rows.append(
            {
                "at_label": row_label,
                "moment_SUPPLIED": moment,
                "cells": tuple(cells),
                "other_clean": tuple(
                    cell["label"]
                    for cell in cells
                    if cell["label"] != row_label and cell["clean"]
                ),
            }
        )
    matrix_rows_tuple = tuple(matrix_rows)
    one_at_a_time = all(
        next(
            cell
            for cell in row["cells"]
            if cell["label"] == row["at_label"]
        )["clean"]
        and not row["other_clean"]
        for row in matrix_rows_tuple
    )
    simultaneity_statement = (
        "ONE_AT_A_TIME_ACROSS_STRATA"
        if one_at_a_time
        else "SIMULTANEOUS_TRANSIENT_CLEANLINESS_FOUND"
    )

    unique_labels = tuple(
        label
        for label, *_rest in TRANSIENTS
        if selections[label]["classification"] == "UNIQUE_SURVIVOR"
    )
    pattern_verdict = (
        "SIX_FOR_SIX_UNIQUE"
        if len(unique_labels) == len(TRANSIENTS)
        else "DIVERGENT"
    )
    divergence = tuple(
        {
            "label": label,
            "classification": selections[label]["classification"],
            "survivors": selections[label]["survivors"],
        }
        for label, *_rest in TRANSIENTS
        if selections[label]["classification"] != "UNIQUE_SURVIVOR"
    )
    window_table = tuple(
        {
            "label": label,
            "k": selections[label]["k"],
            "event": selections[label]["event"],
            "positions": selections[label]["target"],
            "moment_SUPPLIED": selections[label]["moment_SUPPLIED"],
            "cells": tuple(
                {
                    "horizon_t_SUPPLIED": row["horizon_t_SUPPLIED"],
                    "selected": row["selected"],
                    "failed_exclusions": row["failed_exclusions"],
                }
                for row in selections[label]["window_plus_1_through_6"]
            ),
        }
        for label, *_rest in TRANSIENTS
    )

    return {
        "configuration_counts": {
            k: sum(sum(config) == k for config in configurations)
            for k in range(6)
        },
        "family_counts": {k: len(families[k]) for k in range(6)},
        "k2_representatives": k2_representatives,
        "k2_battery": k2_battery,
        "identity_rows": identity_rows,
        "selections": selections,
        "simultaneity_matrix": matrix_rows_tuple,
        "simultaneity_statement": simultaneity_statement,
        "one_at_a_time_across_strata": one_at_a_time,
        "unique_labels": unique_labels,
        "pattern_verdict": pattern_verdict,
        "divergence": divergence,
        "window_table": window_table,
    }


def public_selection(row: dict[str, object]) -> dict[str, object]:
    return {
        key: value
        for key, value in row.items()
        if key != "window_plus_1_through_6"
    }


def main() -> int:
    started = monotonic()
    anchors = source_anchors()
    first_run = run_experiment()

    OUTPUT_LINES.append(
        "AUDIT_INPUT_PATHS_LITERAL " + repr(AUDIT_INPUT_PATHS)
    )
    OUTPUT_LINES.append("SOURCE_ANCHORS " + compact(anchors))
    OUTPUT_LINES.append(
        "IDENTITY_CONTROLS " + compact(first_run["identity_rows"])
    )
    for label, *_rest in TRANSIENTS:
        OUTPUT_LINES.append(
            "SELECTION_TEST "
            + label
            + " "
            + compact(public_selection(first_run["selections"][label]))
        )
    OUTPUT_LINES.append(
        "SIMULTANEITY_MATRIX "
        + compact(first_run["simultaneity_matrix"])
    )
    OUTPUT_LINES.append(
        "PATTERN_VERDICT "
        + first_run["pattern_verdict"]
        + " :: "
        + compact(
            {
                "unique_labels": first_run["unique_labels"],
                "divergence": first_run["divergence"],
                "frozen_alternatives":
                    ("SIX_FOR_SIX_UNIQUE", "DIVERGENT"),
            }
        )
    )
    OUTPUT_LINES.append(
        "WINDOW_TABLE " + compact(first_run["window_table"])
    )
    OUTPUT_LINES.append(
        "ONE_AT_A_TIME_STATEMENT "
        + first_run["simultaneity_statement"]
    )

    known_controls = tuple(
        first_run["selections"][label]
        for label in KNOWN_CONTROL_LABELS
    )
    identity_controls_pass = all(
        row["observed_first_clean_t"]
        == row["expected_first_clean_t_SUPPLIED"]
        and not row["moment_minus_one_clean"]
        and row["moment_clean"]
        for row in first_run["identity_rows"]
    )
    known_selection_controls_pass = all(
        row["classification"] == "UNIQUE_SURVIVOR"
        and row["survivors"] == (row["target"],)
        and row["exclusion_certificate"]["pass"]
        and not row["moment_minus_one_veto"]["selected"]
        and row["moment_minus_one_veto"]["failed_exclusions"]
        == ("clean_postimage",)
        for row in known_controls
    )
    certificate_a = (
        anchors["pass"]
        and first_run["configuration_counts"]
        == {0: 1, 1: 11, 2: 44, 3: 77, 4: 55, 5: 11}
        and first_run["family_counts"]
        == {0: 1, 1: 1, 2: 4, 3: 7, 4: 5, 5: 1}
        and first_run["k2_representatives"]
        == ((0, 2), (0, 3), (0, 4), (0, 5))
        and first_run["k2_battery"]
        == ((0, 2), (0, 3), (0, 4), (0, 5), (0, 7), (1, 10))
        and identity_controls_pass
        and known_selection_controls_pass
    )
    check(
        "CERTIFICATE_A_ANCHORS_AND_IDENTITY_CONTROLS",
        certificate_a,
        {
            "anchors_pass": anchors["pass"],
            "configuration_counts": first_run["configuration_counts"],
            "family_counts": first_run["family_counts"],
            "k2_representatives": first_run["k2_representatives"],
            "k2_battery": first_run["k2_battery"],
            "six_moments_reproduced": identity_controls_pass,
            "known_selection_controls": tuple(
                {
                    "label": row["label"],
                    "classification": row["classification"],
                    "survivors": row["survivors"],
                }
                for row in known_controls
            ),
            "t444_selection_reproduced":
                first_run["selections"]["K3_T444"]["classification"]
                == "UNIQUE_SURVIVOR",
        },
    )

    new_tests = tuple(
        first_run["selections"][label] for label in NEW_TEST_LABELS
    )
    certificate_b = all(
        row["k"] == 3
        and row["battery_size"] == 11
        and len(row["rows"]) == 11
        and all(
            battery_row["horizon_t_SUPPLIED"] == row["moment_SUPPLIED"]
            for battery_row in row["rows"]
        )
        and row["classification"]
        in {"UNIQUE_SURVIVOR", "TIE", "STILL_EXCLUDED"}
        and row["exclusion_certificate"]["pass"]
        and not row["moment_minus_one_veto"]["selected"]
        and row["moment_minus_one_veto"]["failed_exclusions"]
        == ("clean_postimage",)
        for row in new_tests
    )
    check(
        "CERTIFICATE_B_THREE_NEW_SELECTION_TESTS",
        certificate_b,
        {
            "tests": tuple(
                {
                    "label": row["label"],
                    "moment_SUPPLIED": row["moment_SUPPLIED"],
                    "battery_size": row["battery_size"],
                    "classification": row["classification"],
                    "survivors": row["survivors"],
                    "moment_minus_one_failed_exclusions":
                        row["moment_minus_one_veto"][
                            "failed_exclusions"
                        ],
                    "per_exclusion_certificate":
                        row["exclusion_certificate"],
                }
                for row in new_tests
            )
        },
    )

    matrix = first_run["simultaneity_matrix"]
    matrix_complete = (
        len(matrix) == len(TRANSIENTS)
        and all(len(row["cells"]) == len(TRANSIENTS) for row in matrix)
        and tuple(row["at_label"] for row in matrix)
        == tuple(row[0] for row in TRANSIENTS)
        and all(
            tuple(cell["label"] for cell in row["cells"])
            == tuple(transient[0] for transient in TRANSIENTS)
            for row in matrix
        )
    )
    diagonal_clean = all(
        next(
            cell
            for cell in row["cells"]
            if cell["label"] == row["at_label"]
        )["clean"]
        for row in matrix
    )
    other_clean_exact = all(
        row["other_clean"]
        == tuple(
            cell["label"]
            for cell in row["cells"]
            if cell["label"] != row["at_label"] and cell["clean"]
        )
        for row in matrix
    )
    statement_exact = (
        first_run["simultaneity_statement"]
        == (
            "ONE_AT_A_TIME_ACROSS_STRATA"
            if first_run["one_at_a_time_across_strata"]
            else "SIMULTANEOUS_TRANSIENT_CLEANLINESS_FOUND"
        )
    )
    check(
        "CERTIFICATE_C_SIMULTANEITY_MATRIX",
        matrix_complete
        and diagonal_clean
        and other_clean_exact
        and statement_exact,
        {
            "matrix_complete": matrix_complete,
            "diagonal_clean": diagonal_clean,
            "other_clean_by_moment": tuple(
                {
                    "at_label": row["at_label"],
                    "moment_SUPPLIED": row["moment_SUPPLIED"],
                    "other_clean": row["other_clean"],
                }
                for row in matrix
            ),
            "one_at_a_time_across_strata":
                first_run["one_at_a_time_across_strata"],
            "statement": first_run["simultaneity_statement"],
        },
    )

    all_selection_rows = tuple(
        first_run["selections"][label] for label, *_rest in TRANSIENTS
    )
    calculated_verdict = (
        "SIX_FOR_SIX_UNIQUE"
        if all(
            row["classification"] == "UNIQUE_SURVIVOR"
            for row in all_selection_rows
        )
        else "DIVERGENT"
    )
    windows_complete = (
        len(first_run["window_table"]) == len(TRANSIENTS)
        and all(
            tuple(
                cell["horizon_t_SUPPLIED"] - row["moment_SUPPLIED"]
                for cell in row["cells"]
            )
            == WINDOW_OFFSETS
            for row in first_run["window_table"]
        )
        and all(
            len(row["window_plus_1_through_6"]) == len(WINDOW_OFFSETS)
            and all(
                all(
                    window_row["conditions"][name]
                    for name in (
                        "synchronous_composition",
                        "token_rail_return",
                        "literal_inverse",
                    )
                )
                and (
                    not window_row["failed_exclusions"]
                    or window_row["failed_exclusions"]
                    == ("clean_postimage",)
                )
                for window_row in row["window_plus_1_through_6"]
            )
            for row in all_selection_rows
        )
    )
    divergence_exact = (
        (not first_run["divergence"])
        if calculated_verdict == "SIX_FOR_SIX_UNIQUE"
        else bool(first_run["divergence"])
    )
    check(
        "CERTIFICATE_D_PATTERN_VERDICT_AND_WINDOWS",
        first_run["pattern_verdict"]
        in {"SIX_FOR_SIX_UNIQUE", "DIVERGENT"}
        and first_run["pattern_verdict"] == calculated_verdict
        and len(all_selection_rows) == 6
        and windows_complete
        and divergence_exact
        and statement_exact,
        {
            "pattern_verdict": first_run["pattern_verdict"],
            "classifications": tuple(
                {
                    "label": row["label"],
                    "classification": row["classification"],
                    "survivors": row["survivors"],
                }
                for row in all_selection_rows
            ),
            "divergence": first_run["divergence"],
            "windows_complete_plus_1_through_6": windows_complete,
            "one_at_a_time_statement":
                first_run["simultaneity_statement"],
        },
    )

    second_run = run_experiment()
    first_digest = digest(first_run)
    second_digest = digest(second_run)
    deterministic = first_run == second_run
    elapsed = monotonic() - started
    supplied_boundaries = (
        {
            "name": "terminal_horizon_index",
            "status": "SUPPLIED",
            "definition":
                "horizon t applies exactly t+1 complete Cycle-719 "
                "controller orbits",
            "scientific_law_changed": False,
        },
        {
            "name": "six_transient_keys_and_moments",
            "status": "SUPPLIED",
            "values": TRANSIENTS,
            "scientific_law_changed": False,
        },
        {
            "name": "selector_batteries",
            "status": "SUPPLIED",
            "definition":
                "unchanged Cycle-794 k=2 battery and complete Cycle-784 "
                "k=3 translation families",
            "landed_exclusions_changed": False,
        },
    )
    boundaries = {
        "horizons_SUPPLIED": True,
        "horizon_is_actuality_or_physical_time": False,
        "actuality_claim": False,
        "fixture_scope_only": True,
        "axiom_update_triggered": False,
        "supplied_boundaries": supplied_boundaries,
    }
    OUTPUT_LINES.append("BOUNDARIES " + compact(boundaries))
    OUTPUT_LINES.append("axiom_update_triggered: false")
    projected_stdout_bytes = (
        len("\n".join(OUTPUT_LINES).encode("utf-8")) + 24 * 1024
    )
    certificate_e = (
        boundaries["horizons_SUPPLIED"]
        and not boundaries["horizon_is_actuality_or_physical_time"]
        and not boundaries["actuality_claim"]
        and boundaries["fixture_scope_only"]
        and not boundaries["axiom_update_triggered"]
        and all(
            row["status"] == "SUPPLIED" for row in supplied_boundaries
        )
        and deterministic
        and first_digest == second_digest
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES
    )
    check(
        "CERTIFICATE_E_BOUNDARIES_DETERMINISM_AND_BOUNDS",
        certificate_e,
        {
            "boundaries": boundaries,
            "determinism_sha256_first": first_digest,
            "determinism_sha256_second": second_digest,
            "deterministic": deterministic,
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "projected_stdout_bytes": projected_stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    passed = all(CHECKS.values())
    terminal = {
        "terminal": (
            "CYCLE800_PATTERN_COMPLETION_PASS"
            if passed
            else "CYCLE800_PATTERN_COMPLETION_HONEST_FAIL"
        ),
        "pass": passed,
        "pattern_verdict": first_run["pattern_verdict"],
        "simultaneity_statement": first_run["simultaneity_statement"],
        "checks": dict(sorted(CHECKS.items())),
        "determinism_sha256": first_digest,
        "runtime_seconds": round(elapsed, 6),
        "axiom_update_triggered": False,
    }
    output = (
        "\n".join(OUTPUT_LINES)
        + "\nFINAL "
        + compact(terminal)
        + "\n"
    )
    actual_stdout_bytes = len(output.encode("utf-8"))
    if actual_stdout_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", actual_stdout_bytes, STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
