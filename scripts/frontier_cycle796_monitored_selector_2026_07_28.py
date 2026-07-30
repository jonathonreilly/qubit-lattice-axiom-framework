#!/usr/bin/env python3
"""Cycle 796 v2: monitored k=2 selector with a declared cadence convention.

This bounded construction measures the two transient keys at each of the four
landed K719 cadences.  Existence and orbit-level acceptance moments are robust;
sub-orbit timing and window fine-structure depend on the loudly declared
cadence convention.  No per-configuration horizon is an input.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
    "scripts/frontier_cycle781_checkpoint_refusal_law_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
LANDED_HORIZON = 0
MONITOR_CUTOFF = 1024
STDOUT_LIMIT_BYTES = 150 * 1024
EXPECTED_ACCEPTANCE_MOMENTS = (252, 371)
EXPECTED_CLASSIFICATION_COUNTS = {
    "transient_accept": 2,
    "certified_cycle_refusal": 12,
    "open_refusal_through_cutoff": 162,
}
BATTERY_CONDITIONS = (
    "synchronous_composition",
    "token_rail_return",
    "literal_inverse",
    "census_membership",
    "pairwise_separation",
    "synchronization",
    "clean_postimage",
)
LANDED_CADENCES = (
    {
        "name": "orbit_return_boundary",
        "landed_surface":
            "K719.run_orbit return after len(program) H applications",
    },
    {
        "name": "H_station_boundary",
        "landed_surface":
            "K719.apply_controller_step return after H=R2 R1 Q",
    },
    {
        "name": "Q_R1_R2_layer_boundary",
        "landed_surface":
            "K719.controller_word explicit Q + R1 + R2 layer split",
    },
    {
        "name": "program_macro_completion",
        "landed_surface":
            "K719.mapped_macro completions inside the Q layer",
    },
)
PROVENANCE_TABLE = (
    {
        "composition_element": "battery elements",
        "classification": "LANDED",
        "landed_source": "Cycles 736, 750, 719, and pinned Cycle 758",
    },
    {
        "composition_element": "monitoring concept",
        "classification":
            "LANDED AT PLURAL GRANULARITIES — THE CHOICE AMONG THEM "
            "IS A DECLARED CONVENTION",
        "landed_source": "K719 structure and pinned Cycle 781",
    },
    {
        "composition_element": "accept-first-pass glue",
        "classification": "DECLARED COMPOSITION GLUE, UNLANDED",
        "landed_source": "Cycle 796 v2 composition",
    },
)

REFERENCE_758_PATH = (
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py"
)
REFERENCE_781_REF = "origin/physics-loop/proof-grade-blockF4-20260729"
REFERENCE_781_PATH = (
    "scripts/frontier_cycle781_checkpoint_refusal_law_2026_07_28.py"
)
REFERENCE_781_SPEC = f"{REFERENCE_781_REF}:{REFERENCE_781_PATH}"
BLOCKLISTED_REFERENCE_MODULES = (
    "frontier_cycle758_selector_multisource_2026_07_28",
    "frontier_cycle781_checkpoint_refusal_law_2026_07_28",
)

EXPECTED_SHA256 = {
    "M736": "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    "F750": "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    "K719": "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    "reference_758": "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    "reference_781": "b1158250dcb1449f6abac4f6bb6a0a90f47511a8a0f587e85483f4b6f3624211",
}
EXPECTED_GIT_BLOB_SHA1 = {
    "M736": "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
    "F750": "0a8f4562d28f12ed64130b3c3b23fccab677d333",
    "K719": "c123b8d681c3d76fce08ef13d7673622deac64ad",
    "reference_758": "4e23e03ecc5f92a0b8348bfa526eb5b2f2b09dd0",
    "reference_781": "d14cd0ece611c647d3cb7b184830ef9b10754b1d",
}
EXPECTED_781_COMMIT = "72efa390fc444a220719ebd261d367145f1e895a"

OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def emit(line: str) -> None:
    OUTPUT_LINES.append(line)
    print(line, flush=True)


def certificate(
    name: str, passed: bool, detail: object
) -> bool:
    emit(
        f"{'PASS' if passed else 'FAIL'} {name} :: {compact(detail)}"
    )
    return bool(passed)


def file_bytes(relative_path: str) -> bytes:
    return (ROOT / relative_path).read_bytes()


def file_sha256(relative_path: str) -> str:
    return sha256(file_bytes(relative_path)).hexdigest()


def git_blob_sha1(relative_path: str) -> str:
    return subprocess.run(
        ["git", "hash-object", relative_path],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def git_text(spec: str) -> bytes:
    return subprocess.run(
        ["git", "show", spec],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def git_rev_parse(spec: str) -> str:
    return subprocess.run(
        ["git", "rev-parse", spec],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    node = next(
        item
        for item in tree.body
        if isinstance(item, ast.FunctionDef) and item.name == name
    )
    return node


def clean_postimage(after, bank_count):
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


def source_and_provenance_audit() -> dict[str, object]:
    local_paths = {
        "M736": AUDIT_INPUT_PATHS[0],
        "F750": AUDIT_INPUT_PATHS[1],
        "K719": AUDIT_INPUT_PATHS[2],
        "reference_758": REFERENCE_758_PATH,
    }
    sha256s = {
        label: file_sha256(path) for label, path in local_paths.items()
    }
    blobs = {
        label: git_blob_sha1(path) for label, path in local_paths.items()
    }
    reference_781 = git_text(REFERENCE_781_SPEC)
    sha256s["reference_781"] = sha256(reference_781).hexdigest()
    blobs["reference_781"] = git_rev_parse(REFERENCE_781_SPEC)
    commit_781 = git_rev_parse(REFERENCE_781_REF)

    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    imports = {
        alias.asname or alias.name: alias.name
        for node in own_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    assignments = {
        target.id: node.value
        for node in own_tree.body
        if isinstance(node, ast.Assign)
        for target in node.targets
        if isinstance(target, ast.Name)
    }
    audit_node = assignments["AUDIT_INPUT_PATHS"]
    literal_audit_tuple = (
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in audit_node.elts
        )
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
    )
    imported_landed_only = {
        key: imports.get(key) for key in ("M736", "F750", "K")
    } == {
        "M736": "frontier_cycle736_pairwise_separated_multisource_2026_07_28",
        "F750": "frontier_cycle750_actual_selector_stretch_2026_07_28",
        "K": "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
    } and not any(
        module in imports.values() for module in BLOCKLISTED_REFERENCE_MODULES
    )

    reference_758_tree = ast.parse(
        file_bytes(REFERENCE_758_PATH), filename=REFERENCE_758_PATH
    )
    own_clean = function_node(own_tree, "clean_postimage")
    reference_clean = function_node(reference_758_tree, "clean_postimage")
    clean_ast_exact = ast.dump(
        ast.Module(body=own_clean.body, type_ignores=[]),
        include_attributes=False,
    ) == ast.dump(
        ast.Module(body=reference_clean.body, type_ignores=[]),
        include_attributes=False,
    )
    reference_758_functions = {
        node.name
        for node in reference_758_tree.body
        if isinstance(node, ast.FunctionDef)
    }

    reference_781_tree = ast.parse(
        reference_781, filename=REFERENCE_781_SPEC
    )
    non_interference_source = ast.unparse(
        function_node(reference_781_tree, "non_interference")
    )
    reference_781_constants = {
        node.value
        for node in ast.walk(reference_781_tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    every_boundary_idiom = (
        "for step in range(C719.CONTROLLER_STATIONS):"
        in non_interference_source
        and any(
            "every tested post-engagement station boundary" in value
            for value in reference_781_constants
        )
    )
    k719_tree = ast.parse(
        file_bytes(AUDIT_INPUT_PATHS[2]), filename=AUDIT_INPUT_PATHS[2]
    )
    k719_functions = {
        node.name
        for node in k719_tree.body
        if isinstance(node, ast.FunctionDef)
    }
    controller_word_source = ast.unparse(
        function_node(k719_tree, "controller_word")
    )
    landed_plural_cadences = (
        {
            "run_orbit",
            "apply_controller_step",
            "controller_word",
            "mapped_macro",
        }.issubset(k719_functions)
        and all(
            token in controller_word_source
            for token in ("q =", "r1 =", "r2 =", "return q + r1 + r2")
        )
        and every_boundary_idiom
    )
    return {
        "sha256": sha256s,
        "git_blob_sha1": blobs,
        "reference_781_commit": commit_781,
        "literal_AUDIT_INPUT_PATHS": literal_audit_tuple,
        "imported_landed_only": imported_landed_only,
        "reference_758_clean_postimage_AST_exact": clean_ast_exact,
        "reference_758_multisource_selector_present":
            "multisource_enforcement_lineage_selector"
            in reference_758_functions,
        "reference_781_every_boundary_idiom": every_boundary_idiom,
        "landed_plural_cadences": landed_plural_cadences,
        "composition_provenance": PROVENANCE_TABLE,
        "pass": (
            sha256s == EXPECTED_SHA256
            and blobs == EXPECTED_GIT_BLOB_SHA1
            and commit_781 == EXPECTED_781_COMMIT
            and literal_audit_tuple
            and imported_landed_only
            and clean_ast_exact
            and "multisource_enforcement_lineage_selector"
            in reference_758_functions
            and every_boundary_idiom
            and landed_plural_cadences
        ),
    }


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def expected_synchronization_trace(
    positions: tuple[int, ...],
) -> tuple[tuple[tuple[int, ...], tuple[int, ...], int], ...]:
    return tuple(
        (
            rotate_positions(positions, step),
            rotate_positions(positions, step + 1),
            0,
        )
        for step in range(RING_STATIONS)
    )


def state_sha256(state: object) -> str:
    return sha256(str(state).encode("ascii")).hexdigest()


def build_base_rows() -> tuple[
    dict[tuple[int, tuple[int, ...]], dict[str, object]],
    tuple[tuple[int, ...], ...],
    dict[str, object],
]:
    census = M736.configuration_census()
    configurations = census["configurations"]
    k2_positions = tuple(
        M736.occupied_sites(config)
        for config in configurations
        if sum(config) == 2
    )
    k2_members = frozenset(k2_positions)
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    word_by_positions = {
        positions: M736.synchronous_composition_word(
            fixtures[0][2], positions
        )
        for positions in k2_positions
    }

    rows: dict[
        tuple[int, tuple[int, ...]], dict[str, object]
    ] = {}
    failure_census: Counter[str] = Counter()
    for event, direction, program, before, _single_expected in fixtures:
        for positions in k2_positions:
            tokens = tuple(
                int(station in positions)
                for station in range(len(program))
            )
            zeros = tuple(value ^ value for value in tokens)
            composition_word = word_by_positions[positions]
            expected = K.A.apply_semantic(before, composition_word)
            after, rail_a, rail_b, trace = K.run_orbit(
                before, program, token_positions=positions
            )
            restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
                after, program, token_positions=positions, reverse=True
            )
            config = tuple(
                int(station in positions)
                for station in range(RING_STATIONS)
            )
            conditions = {
                "synchronous_composition": after == expected,
                "token_rail_return":
                    rail_a == tokens and rail_b == zeros,
                "literal_inverse": (
                    restored == before
                    and inverse_a == rail_a
                    and inverse_b == rail_b
                ),
                "census_membership": positions in k2_members,
                "pairwise_separation":
                    M736.is_pairwise_separated(config),
                "synchronization":
                    trace == expected_synchronization_trace(positions),
            }
            landed_clean = clean_postimage(after, FIXTURE_BANKS)
            for name, passed in {
                **conditions, "clean_postimage": landed_clean
            }.items():
                if not passed:
                    failure_census[name] += 1
            key = (event, positions)
            rows[key] = {
                "key": key,
                "event": event,
                "direction": direction,
                "program": program,
                "before": before,
                "positions": positions,
                "tokens": tokens,
                "zeros": zeros,
                "composition_word": composition_word,
                "after": after,
                "conditions": conditions,
                "landed_clean": landed_clean,
                "evidence": {
                    "configuration_mask":
                        sum(1 << station for station in positions),
                    "composition_word_sha256":
                        K.gate_digest(composition_word),
                    "before_state_sha256": state_sha256(before),
                    "after_state_sha256": state_sha256(after),
                    "restored_state_sha256": state_sha256(restored),
                },
            }

    landed_selected_by_configuration = {
        positions: tuple(
            event
            for event in range(2 * FIXTURE_BANKS)
            if all(rows[(event, positions)]["conditions"].values())
            and rows[(event, positions)]["landed_clean"]
        )
        for positions in k2_positions
    }
    batched_step_failures = []
    for key, row in rows.items():
        direct_state, direct_a, direct_b, _trace = K.run_orbit(
            row["after"],
            row["program"],
            token_positions=row["positions"],
        )
        batched_state = K.A.apply_semantic(
            row["after"], row["composition_word"]
        )
        if (
            batched_state != direct_state
            or direct_a != row["tokens"]
            or direct_b != row["zeros"]
        ):
            batched_step_failures.append(key)
    control = {
        "census_agreement": census["agreement"],
        "configuration_count": len(k2_positions),
        "event_count": len(fixtures),
        "key_count": len(rows),
        "all_non_postimage_conditions_pass": all(
            all(row["conditions"].values()) for row in rows.values()
        ),
        "landed_failure_census": dict(sorted(failure_census.items())),
        "landed_selected_key_count": sum(
            bool(selected)
            for selected in landed_selected_by_configuration.values()
        ),
        "zero_survivor_configurations": sum(
            not selected
            for selected in landed_selected_by_configuration.values()
        ),
        "landed_identity_table_sha256":
            digest(tuple(sorted(landed_selected_by_configuration.items()))),
        "batched_vs_run_orbit_step_cases": len(rows),
        "batched_vs_run_orbit_step_failures":
            tuple(batched_step_failures),
        "pass": (
            census["agreement"]
            and len(k2_positions) == M736.EXPECTED_COUNTS_BY_K[2] == 44
            and len(fixtures) == 2 * FIXTURE_BANKS == 4
            and len(rows) == 176
            and all(
                all(row["conditions"].values())
                for row in rows.values()
            )
            and dict(failure_census) == {"clean_postimage": 176}
            and all(
                not selected
                for selected in landed_selected_by_configuration.values()
            )
            and not batched_step_failures
        ),
    }
    return rows, k2_positions, control


def advance_one_boundary(
    state: object,
    composition_word: tuple[object, ...],
) -> object:
    """Batched exact full-orbit action, precompiled once per configuration."""

    return K.A.apply_semantic(state, composition_word)


def monitor_family(
    rows: dict[tuple[int, tuple[int, ...]], dict[str, object]],
    *,
    label: str,
) -> dict[str, object]:
    """Time-major batch scan; every key sees the same cadence and cutoff."""

    started = monotonic()
    ordered_keys = tuple(sorted(rows))
    state = {key: rows[key]["after"] for key in ordered_keys}
    seen = {key: {state[key]: LANDED_HORIZON} for key in ordered_keys}
    first_clean = {key: None for key in ordered_keys}
    clean_ticks = {key: [] for key in ordered_keys}
    cycles = {key: None for key in ordered_keys}
    transport_failures = Counter()
    active = set(ordered_keys)

    for key in ordered_keys:
        if clean_postimage(state[key], FIXTURE_BANKS):
            first_clean[key] = LANDED_HORIZON
            clean_ticks[key].append(LANDED_HORIZON)
            seen[key] = {}

    for horizon in range(1, MONITOR_CUTOFF + 1):
        retired_cycles = []
        for key in sorted(active):
            row = rows[key]
            next_state = advance_one_boundary(
                state[key], row["composition_word"]
            )
            state[key] = next_state
            clean = clean_postimage(next_state, FIXTURE_BANKS)
            if clean:
                clean_ticks[key].append(horizon)
                if first_clean[key] is None:
                    first_clean[key] = horizon
                    seen[key] = {}
            if first_clean[key] is None:
                if next_state in seen[key]:
                    entry = seen[key][next_state]
                    cycles[key] = {
                        "entry_boundary": entry,
                        "return_boundary": horizon,
                        "period": horizon - entry,
                    }
                    retired_cycles.append(key)
                else:
                    seen[key][next_state] = horizon
        active.difference_update(retired_cycles)
        if horizon % 128 == 0:
            emit(
                "PROGRESS "
                + compact(
                    {
                        "scan": label,
                        "boundary": horizon,
                        "active": len(active),
                        "accepted": sum(
                            moment is not None
                            for moment in first_clean.values()
                        ),
                        "certified_cycles": sum(
                            cycle is not None for cycle in cycles.values()
                        ),
                        "elapsed_seconds": round(monotonic() - started, 3),
                    }
                )
            )

    table = []
    for key in ordered_keys:
        event, positions = key
        moment = first_clean[key]
        if moment is not None:
            classification = "transient_accept"
        elif cycles[key] is not None:
            classification = "certified_cycle_refusal"
        else:
            classification = "open_refusal_through_cutoff"
        acceptance_conditions = None
        if moment is not None:
            acceptance_conditions = {
                **rows[key]["conditions"],
                "clean_postimage": True,
            }
        table.append(
            {
                "event": event,
                "positions": positions,
                "classification": classification,
                "acceptance_moment": moment,
                "clean_ticks_through_cutoff": tuple(clean_ticks[key]),
                "cycle": cycles[key],
                "acceptance_conditions": acceptance_conditions,
                "transport_failures": transport_failures[key],
                "final_state_sha256": state_sha256(state[key]),
            }
        )

    counts = Counter(row["classification"] for row in table)
    moments = tuple(
        sorted(
            row["acceptance_moment"]
            for row in table
            if row["acceptance_moment"] is not None
        )
    )
    return {
        "table": tuple(table),
        "classification_counts": dict(sorted(counts.items())),
        "acceptance_moments": moments,
        "acceptance_keys": tuple(
            (row["event"], row["positions"], row["acceptance_moment"])
            for row in table
            if row["acceptance_moment"] is not None
        ),
        "transport_failure_count": sum(transport_failures.values()),
        "table_sha256": digest(table),
        "runtime_seconds": round(monotonic() - started, 6),
    }


def cadence_probe_for_key(
    row: dict[str, object],
    *,
    maximum_orbit: int,
    window: tuple[int, int, int],
) -> dict[str, object]:
    """Measure all four landed observation cadences on one transient key."""

    program = row["program"]
    stations = len(program)
    state = row["after"]
    a = tuple(
        int(station in row["positions"])
        for station in range(stations)
    )
    b = (0,) * stations
    cadence_names = tuple(row["name"] for row in LANDED_CADENCES)
    first = {cadence: None for cadence in cadence_names}
    window_counts = {
        cadence: Counter() for cadence in cadence_names
    }
    window_examples = {
        cadence: [] for cadence in cadence_names
    }
    recomposition_failures = []

    def observe(
        cadence: str,
        coordinate: dict[str, object],
    ) -> None:
        if (
            not all(row["conditions"].values())
            or not clean_postimage(state, FIXTURE_BANKS)
        ):
            return
        if first[cadence] is None:
            first[cadence] = coordinate
        orbit = int(coordinate["orbit"])
        if orbit in window:
            window_counts[cadence][orbit] += 1
            if len(window_examples[cadence]) < 12:
                window_examples[cadence].append(coordinate)

    absolute_h = 0
    for orbit in range(1, maximum_orbit + 1):
        orbit_input = state
        for step in range(1, stations + 1):
            absolute_h += 1
            live_stations = tuple(
                station
                for station, value in enumerate(a)
                if value
            )
            for station in live_stations:
                state = K.A.apply_semantic(
                    state, K.mapped_macro(program[station])
                )
                observe(
                    "program_macro_completion",
                    {
                        "orbit": orbit,
                        "step": step,
                        "absolute_H": absolute_h,
                        "station": station,
                    },
                )

            layer_coordinate = {
                "orbit": orbit,
                "step": step,
                "absolute_H": absolute_h,
            }
            observe(
                "Q_R1_R2_layer_boundary",
                {**layer_coordinate, "layer": "Q"},
            )

            a_list = list(a)
            b_list = list(b)
            for station in range(stations):
                a_list[station], b_list[station] = (
                    b_list[station],
                    a_list[station],
                )
            a, b = tuple(a_list), tuple(b_list)
            observe(
                "Q_R1_R2_layer_boundary",
                {**layer_coordinate, "layer": "R1"},
            )

            a_list = list(a)
            b_list = list(b)
            for station in range(stations):
                target = (station + 1) % stations
                b_list[station], a_list[target] = (
                    a_list[target],
                    b_list[station],
                )
            a, b = tuple(a_list), tuple(b_list)
            observe(
                "Q_R1_R2_layer_boundary",
                {**layer_coordinate, "layer": "R2"},
            )
            observe("H_station_boundary", layer_coordinate)

        expected_orbit_state = advance_one_boundary(
            orbit_input, row["composition_word"]
        )
        if state != expected_orbit_state:
            recomposition_failures.append(orbit)
        observe(
            "orbit_return_boundary",
            {
                "orbit": orbit,
                "step": stations,
                "absolute_H": absolute_h,
            },
        )

    return {
        "key": row["key"],
        "first": first,
        "window": window,
        "window_clean_observation_counts": {
            cadence: {
                str(orbit): window_counts[cadence][orbit]
                for orbit in window
            }
            for cadence in cadence_names
        },
        "window_examples": {
            cadence: tuple(window_examples[cadence])
            for cadence in cadence_names
        },
        "orbit_recomposition_failures":
            tuple(recomposition_failures),
    }


def cadence_census(
    rows: dict[tuple[int, tuple[int, ...]], dict[str, object]],
    transient_acceptance_keys:
        tuple[tuple[int, tuple[int, ...], int], ...],
) -> dict[str, object]:
    """Run the first-pass selector on both transients under each cadence."""

    target_specs = tuple(
        (
            (event, positions),
            moment + 1,
            (moment - 1, moment, moment + 1),
        )
        for event, positions, moment in sorted(
            transient_acceptance_keys, key=lambda item: item[2]
        )
    )
    probes = {
        key: cadence_probe_for_key(
            rows[key],
            maximum_orbit=maximum_orbit,
            window=window,
        )
        for key, maximum_orbit, window in target_specs
    }
    cadence_names = tuple(row["name"] for row in LANDED_CADENCES)
    first_acceptance_table = tuple(
        {
            "cadence": cadence,
            "key": key,
            "orbit": probes[key]["first"][cadence]["orbit"],
            "step": probes[key]["first"][cadence]["step"],
            "absolute_H":
                probes[key]["first"][cadence]["absolute_H"],
        }
        for cadence in cadence_names
        for key, _maximum_orbit, _window in target_specs
    )
    window_structure = tuple(
        {
            "cadence": cadence,
            "key": key,
            "window": probes[key]["window"],
            "clean_observation_counts":
                probes[key]["window_clean_observation_counts"][cadence],
            "clean_observation_examples":
                probes[key]["window_examples"][cadence],
        }
        for cadence in cadence_names
        for key, _maximum_orbit, _window in target_specs
    )
    selection_existence_cadence_robust = all(
        probes[key]["first"][cadence] is not None
        for cadence in cadence_names
        for key, _maximum_orbit, _window in target_specs
    ) and all(
        Counter(
            row["orbit"]
            for row in first_acceptance_table
            if row["cadence"] == cadence
        ) == Counter(EXPECTED_ACCEPTANCE_MOMENTS)
        for cadence in cadence_names
    )
    orbit_level_moments_cadence_robust = all(
        tuple(
            row["orbit"]
            for row in first_acceptance_table
            if row["cadence"] == cadence
        ) == EXPECTED_ACCEPTANCE_MOMENTS
        for cadence in cadence_names
    )
    sub_orbit_timing_cadence_sensitive = any(
        len(
            {
                row["absolute_H"]
                for row in first_acceptance_table
                if row["key"] == key
            }
        ) > 1
        for key, _maximum_orbit, _window in target_specs
    )
    spill_rows = {
        row["cadence"]: row
        for row in window_structure
        if row["key"] == target_specs[-1][0]
    }
    spill_orbit = str(target_specs[-1][2][-1])
    window_fine_structure_cadence_sensitive = (
        spill_rows["H_station_boundary"][
            "clean_observation_counts"
        ][spill_orbit] > 0
        and spill_rows["orbit_return_boundary"][
            "clean_observation_counts"
        ][spill_orbit] == 0
        and len(
            {
                compact(row["clean_observation_counts"])
                for row in spill_rows.values()
            }
        ) > 1
    )
    robustness_split = {
        "selection_existence_cadence_robust":
            selection_existence_cadence_robust,
        "orbit_level_moments_cadence_robust":
            orbit_level_moments_cadence_robust,
        "sub_orbit_timing_cadence_sensitive":
            sub_orbit_timing_cadence_sensitive,
        "window_fine_structure_cadence_sensitive":
            window_fine_structure_cadence_sensitive,
    }
    return {
        "candidate_cadences_from_719": LANDED_CADENCES,
        "first_acceptance_table": first_acceptance_table,
        "window_structure": window_structure,
        "robustness_split": robustness_split,
        "orbit_recomposition_failures": tuple(
            (key, probe["orbit_recomposition_failures"])
            for key, probe in probes.items()
            if probe["orbit_recomposition_failures"]
        ),
    }


def main() -> int:
    started = monotonic()
    provenance = source_and_provenance_audit()
    rows, k2_positions, landed_control = build_base_rows()

    exact_law = (
        "Measure the two transient keys under each of the four landed "
        "cadences.  For the 176-key family run, DECLARED CONVENTION: observe "
        "at orbit_return_boundary through the global cutoff T=1024.  "
        "DECLARED COMPOSITION GLUE, UNLANDED: accept at the first full-battery "
        "pass; otherwise refuse through T."
    )
    residual_supply = {
        "monitoring_cadence":
            "orbit_return_boundary",
        "cadence_convention":
            "DECLARED CONVENTION: orbit_return_boundary governs the "
            "176-key family run",
        "accept_first_pass_glue":
            "DECLARED COMPOSITION GLUE, UNLANDED",
        "cutoff_T": MONITOR_CUTOFF,
        "cutoff_role": "one global finite bound, not a per-configuration value",
        "per_configuration_horizon_supply": False,
        "declared_residual_supply_elements": ("cadence", "cutoff"),
    }
    emit("COMPOSED_LAW :: " + exact_law)
    emit(
        "DECLARED_CONVENTION :: "
        + residual_supply["cadence_convention"]
    )
    emit(
        "DECLARED_COMPOSITION_GLUE :: "
        + residual_supply["accept_first_pass_glue"]
    )
    emit("RESIDUAL_SUPPLY_SURFACE :: " + compact(residual_supply))
    certificate(
        "Certificate_A_anchors_references_and_composition_provenance",
        provenance["pass"],
        {
            "sha256": provenance["sha256"],
            "git_blob_sha1": provenance["git_blob_sha1"],
            "reference_781_commit":
                provenance["reference_781_commit"],
            "literal_AUDIT_INPUT_PATHS":
                provenance["literal_AUDIT_INPUT_PATHS"],
            "blocklisted_references": BLOCKLISTED_REFERENCE_MODULES,
            "reference_758_clean_postimage_AST_exact":
                provenance[
                    "reference_758_clean_postimage_AST_exact"
                ],
            "reference_781_every_boundary_idiom":
                provenance["reference_781_every_boundary_idiom"],
            "landed_plural_cadences":
                provenance["landed_plural_cadences"],
            "composition_provenance":
                provenance["composition_provenance"],
        },
    )
    certificate(
        "Certificate_B_landed_horizon_identity_44_of_44_zero_survivor",
        landed_control["pass"],
        landed_control,
    )

    prediction = {
        "cutoff_T": MONITOR_CUTOFF,
        "acceptance_moments": EXPECTED_ACCEPTANCE_MOMENTS,
        "classification_counts": EXPECTED_CLASSIFICATION_COUNTS,
        "unique_survivor_at_each_acceptance": True,
        "simultaneous_acceptances": False,
        "prediction_basis":
            "frozen Cycle-792/794 landed-fact predictions; not selector inputs",
    }
    emit("PREDICTION_BEFORE_FAMILY_RUN :: " + compact(prediction))

    primary = monitor_family(rows, label="primary")
    cadence = cadence_census(rows, primary["acceptance_keys"])
    expected_robustness_split = {
        "selection_existence_cadence_robust": True,
        "orbit_level_moments_cadence_robust": True,
        "sub_orbit_timing_cadence_sensitive": True,
        "window_fine_structure_cadence_sensitive": True,
    }
    cadence_claims_pass = (
        cadence["robustness_split"] == expected_robustness_split
        and not cadence["orbit_recomposition_failures"]
    )
    emit(
        "CADENCE_CENSUS :: "
        + compact(cadence["candidate_cadences_from_719"])
    )
    for row in cadence["first_acceptance_table"]:
        emit("CADENCE_FIRST_ACCEPTANCE :: " + compact(row))
    for row in cadence["window_structure"]:
        emit("CADENCE_WINDOW_STRUCTURE :: " + compact(row))
    for key, value in cadence["robustness_split"].items():
        emit(key + ": " + ("true" if value else "false"))
    certificate(
        "Certificate_B2_cadence_census_and_robustness_split",
        cadence_claims_pass,
        cadence,
    )
    emit("ACTUAL_TABLE_BEGIN :: rows=176")
    for index, row in enumerate(primary["table"]):
        emit(
            "ACTUAL "
            + compact(
                {
                    "row": index,
                    "event": row["event"],
                    "positions": row["positions"],
                    "classification": row["classification"],
                    "acceptance_moment": row["acceptance_moment"],
                    "clean_ticks_through_T":
                        row["clean_ticks_through_cutoff"],
                    "cycle": row["cycle"],
                    "transport_failures": row["transport_failures"],
                    "final_state_sha256": row["final_state_sha256"],
                }
            )
        )
    emit("ACTUAL_TABLE_END :: sha256=" + primary["table_sha256"])

    observed_counts = primary["classification_counts"]
    observed_moments = primary["acceptance_moments"]
    accepted_rows = tuple(
        row
        for row in primary["table"]
        if row["acceptance_moment"] is not None
    )
    moment_multiplicities = Counter(
        row["acceptance_moment"] for row in accepted_rows
    )
    isolated_acceptance_tick = all(
        row["acceptance_moment"] - 1
        not in row["clean_ticks_through_cutoff"]
        and row["acceptance_moment"] + 1
        not in row["clean_ticks_through_cutoff"]
        for row in accepted_rows
    )
    never_simultaneous = all(
        multiplicity == 1
        for multiplicity in moment_multiplicities.values()
    )
    clean_survivors_at_acceptance = {
        moment: tuple(
            (row["event"], row["positions"])
            for row in primary["table"]
            if moment in row["clean_ticks_through_cutoff"]
        )
        for moment in observed_moments
    }
    unique_survivor_at_each_acceptance = all(
        len(survivors) == 1
        for survivors in clean_survivors_at_acceptance.values()
    )
    family_matches_prediction = (
        observed_counts == EXPECTED_CLASSIFICATION_COUNTS
        and observed_moments == EXPECTED_ACCEPTANCE_MOMENTS
        and len(primary["table"]) == 176
        and isolated_acceptance_tick
        and never_simultaneous
        and unique_survivor_at_each_acceptance
        and primary["transport_failure_count"] == 0
    )
    certificate(
        "Certificate_C_predictions_then_full_family_run",
        family_matches_prediction,
        {
            "predicted": prediction,
            "actual_classification_counts": observed_counts,
            "actual_acceptance_moments": observed_moments,
            "actual_acceptance_keys": primary["acceptance_keys"],
            "isolated_one_tick_acceptance_each":
                isolated_acceptance_tick,
            "never_simultaneous": never_simultaneous,
            "clean_survivors_at_acceptance":
                clean_survivors_at_acceptance,
            "unique_survivor_at_each_acceptance":
                unique_survivor_at_each_acceptance,
            "transport_failure_count":
                primary["transport_failure_count"],
            "table_sha256": primary["table_sha256"],
        },
    )

    rerun = monitor_family(rows, label="determinism_rerun")
    cadence_rerun = cadence_census(rows, primary["acceptance_keys"])
    family_deterministic = (
        primary["table"] == rerun["table"]
        and primary["table_sha256"] == rerun["table_sha256"]
        and primary["classification_counts"]
        == rerun["classification_counts"]
        and primary["acceptance_moments"]
        == rerun["acceptance_moments"]
    )
    cadence_deterministic = cadence == cadence_rerun
    deterministic = family_deterministic and cadence_deterministic

    expected_acceptance_certificate = {
        name: True for name in BATTERY_CONDITIONS
    }
    acceptance_certificates = tuple(
        {
            "event": row["event"],
            "positions": row["positions"],
            "moment": row["acceptance_moment"],
            "conditions": row["acceptance_conditions"],
            "previous_boundary_clean":
                row["acceptance_moment"] - 1
                in row["clean_ticks_through_cutoff"],
            "next_boundary_clean":
                row["acceptance_moment"] + 1
                in row["clean_ticks_through_cutoff"],
            "later_nonconsecutive_clean_boundaries": tuple(
                tick
                for tick in row["clean_ticks_through_cutoff"]
                if tick > row["acceptance_moment"] + 1
            ),
        }
        for row in accepted_rows
    )
    one_tick_consistency = (
        observed_moments == EXPECTED_ACCEPTANCE_MOMENTS
        and isolated_acceptance_tick
        and never_simultaneous
        and unique_survivor_at_each_acceptance
        and all(
            row["acceptance_conditions"]
            == expected_acceptance_certificate
            for row in accepted_rows
        )
    )

    divergences = []
    if not provenance["pass"]:
        divergences.append(
            {
                "surface": "anchors_or_provenance",
                "expected_sha256": EXPECTED_SHA256,
                "actual_sha256": provenance["sha256"],
            }
        )
    if not landed_control["pass"]:
        divergences.append(
            {
                "surface": "landed_horizon_identity",
                "expected": "44/44 configurations zero-survivor",
                "actual": landed_control,
            }
        )
    if observed_counts != EXPECTED_CLASSIFICATION_COUNTS:
        divergences.append(
            {
                "surface": "classification_counts",
                "expected": EXPECTED_CLASSIFICATION_COUNTS,
                "actual": observed_counts,
            }
        )
    if observed_moments != EXPECTED_ACCEPTANCE_MOMENTS:
        divergences.append(
            {
                "surface": "acceptance_moments",
                "expected": EXPECTED_ACCEPTANCE_MOMENTS,
                "actual": observed_moments,
            }
        )
    if not isolated_acceptance_tick:
        divergences.append(
            {
                "surface": "one_tick_acceptance_isolation",
                "actual_acceptance_certificates":
                    acceptance_certificates,
            }
        )
    if not unique_survivor_at_each_acceptance:
        divergences.append(
            {
                "surface": "survivor_uniqueness_at_acceptance",
                "actual": clean_survivors_at_acceptance,
            }
        )
    if not never_simultaneous:
        divergences.append(
            {
                "surface": "simultaneity",
                "actual_multiplicities":
                    dict(sorted(moment_multiplicities.items())),
            }
        )
    if primary["transport_failure_count"]:
        divergences.append(
            {
                "surface": "horizon_transport",
                "failure_count": primary["transport_failure_count"],
            }
        )
    if not cadence_claims_pass:
        divergences.append(
            {
                "surface": "cadence_robustness_split",
                "expected": expected_robustness_split,
                "actual": cadence,
            }
        )
    if not deterministic:
        divergences.append(
            {
                "surface": "determinism",
                "primary_sha256": primary["table_sha256"],
                "rerun_sha256": rerun["table_sha256"],
                "family_deterministic": family_deterministic,
                "cadence_deterministic": cadence_deterministic,
            }
        )

    robust_content_constructed = (
        not divergences
        and family_matches_prediction
        and one_tick_consistency
        and deterministic
        and cadence_claims_pass
        and cadence["robustness_split"][
            "selection_existence_cadence_robust"
        ]
        and cadence["robustness_split"][
            "orbit_level_moments_cadence_robust"
        ]
    )
    full_construction_convention_free = not (
        cadence["robustness_split"][
            "sub_orbit_timing_cadence_sensitive"
        ]
        or cadence["robustness_split"][
            "window_fine_structure_cadence_sensitive"
        ]
    )
    exact_time_law_constructed_at_scope = {
        "robust_content_constructed": robust_content_constructed,
        "full_construction_convention_free":
            full_construction_convention_free,
    }
    verdict = (
        "CONSTRUCTED_WITH_CADENCE_CONVENTION"
        if robust_content_constructed
        and not full_construction_convention_free
        else "DIVERGENT"
    )
    if divergences:
        for divergence in divergences:
            emit("LOUD_DIVERGENCE :: " + compact(divergence))
    certificate(
        "Certificate_D_one_tick_consistency_and_frozen_verdict",
        (
            robust_content_constructed
            and not full_construction_convention_free
        ),
        {
            "verdict": verdict,
            "exact_time_law_constructed_at_scope":
                exact_time_law_constructed_at_scope,
            "robustness_split": cadence["robustness_split"],
            "Cycle_792_794_expected_moments":
                EXPECTED_ACCEPTANCE_MOMENTS,
            "observed_moments": observed_moments,
            "orbit_return_boundary_convention":
                residual_supply["cadence_convention"],
            "acceptance_certificates": acceptance_certificates,
            "expected_per_exclusion_certificate":
                expected_acceptance_certificate,
            "divergences": divergences,
            "actuality_claim": False,
            "composition_status": "CONSTRUCTION_NOT_LANDED_LAW",
            "axiom_update_triggered": False,
        },
    )
    emit(
        "exact_time_law_constructed_at_scope: "
        + compact(exact_time_law_constructed_at_scope)
    )
    emit("axiom_update_triggered: false")
    emit("actuality_claim: false")
    emit("frozen_verdict: " + verdict)

    elapsed = monotonic() - started
    projected_tail = compact(
        {
            "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
            "checks": "A-E",
            "verdict": verdict,
            "acceptance_moments": observed_moments,
            "acceptance_keys": primary["acceptance_keys"],
            "robustness_split": cadence["robustness_split"],
            "primary_table_sha256": primary["table_sha256"],
            "rerun_table_sha256": rerun["table_sha256"],
            "runtime_seconds": round(elapsed, 6),
        }
    )
    stdout_projected_bytes = (
        len(("\n".join(OUTPUT_LINES) + "\n").encode("utf-8"))
        + len(projected_tail.encode("utf-8"))
        + 10 * 1024
    )
    bounds_pass = (
        deterministic
        and len(rows) == 176
        and len(k2_positions) == 44
        and MONITOR_CUTOFF == 1024
        and elapsed < AUDIT_TIMEOUT_SEC
        and stdout_projected_bytes < STDOUT_LIMIT_BYTES
        and cadence_claims_pass
        and cadence_deterministic
        and residual_supply[
            "declared_residual_supply_elements"
        ] == ("cadence", "cutoff")
        and not residual_supply["per_configuration_horizon_supply"]
    )
    certificate(
        "Certificate_E_boundaries_determinism_and_bounds",
        bounds_pass,
        {
            "landed_horizon": LANDED_HORIZON,
            "monitor_cutoff": MONITOR_CUTOFF,
            "monitoring_cadence":
                residual_supply["monitoring_cadence"],
            "residual_supply_surface": ("cadence", "cutoff"),
            "per_configuration_horizon_supply": False,
            "family_keys": len(rows),
            "deterministic": deterministic,
            "family_deterministic": family_deterministic,
            "cadence_deterministic": cadence_deterministic,
            "primary_table_sha256": primary["table_sha256"],
            "rerun_table_sha256": rerun["table_sha256"],
            "runtime_seconds": round(elapsed, 6),
            "runtime_bound_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_projected_upper_bound_bytes":
                stdout_projected_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    all_pass = (
        provenance["pass"]
        and landed_control["pass"]
        and family_matches_prediction
        and robust_content_constructed
        and not full_construction_convention_free
        and bounds_pass
    )
    report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "pass": all_pass,
        "verdict": verdict,
        "exact_time_law_constructed_at_scope":
            exact_time_law_constructed_at_scope,
        "robustness_split": cadence["robustness_split"],
        "cadence_first_acceptance_table":
            cadence["first_acceptance_table"],
        "cadence_window_structure": cadence["window_structure"],
        "actuality_claim": False,
        "axiom_update_triggered": False,
        "acceptance_moments": observed_moments,
        "acceptance_keys": primary["acceptance_keys"],
        "classification_counts": observed_counts,
        "divergences": divergences,
        "runtime_seconds": round(monotonic() - started, 6),
        "stdout_bytes_before_terminal":
            len(("\n".join(OUTPUT_LINES) + "\n").encode("utf-8")),
        "terminal":
            "CYCLE796_MONITORED_SELECTOR_PASS"
            if all_pass
            else "CYCLE796_MONITORED_SELECTOR_HONEST_FAIL",
    }
    report["report_sha256"] = digest(report)
    emit("REPORT :: " + compact(report))
    emit(report["terminal"])
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
