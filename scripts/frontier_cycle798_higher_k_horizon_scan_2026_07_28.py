#!/usr/bin/env python3
"""Cycle 798: bounded higher-k postimage-residual horizon scan.

The complete ring-11 k=3,4,5 selector census is reconstructed from the
landed Cycle-719/736/750/758 laws and the blocklisted Cycle-784 primary.
Exactly the 42 zero-survivor family-epoch keys are then scanned at their
canonical representatives.  The supplied horizon index t has the landed
Cycle-794 convention: t means t+1 complete controller orbits.

This is a bounded fixture calculation.  A horizon index is not physical time,
and neither residual cleanliness nor monitored selection supplies actuality.
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
from collections import Counter
from hashlib import sha1, sha256
import inspect
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
TARGET_STRATA = (3, 4, 5)
MANDATORY_HORIZON_T = 1024
SCAN_HORIZON_T = 2048

EXPECTED_CONFIGURATION_COUNTS = {
    0: 1,
    1: 11,
    2: 44,
    3: 77,
    4: 55,
    5: 11,
}
EXPECTED_FAMILY_COUNTS = {0: 1, 1: 1, 2: 4, 3: 7, 4: 5, 5: 1}
EXPECTED_CLASS_COUNTS = {
    3: {"exact_tie": 7, "unique_survivor": 3, "zero_survivors": 18},
    4: {"exact_tie": 0, "unique_survivor": 0, "zero_survivors": 20},
    5: {"exact_tie": 0, "unique_survivor": 0, "zero_survivors": 4},
}
EXPECTED_ZERO_FAMILY_EPOCHS = {3: 18, 4: 20, 5: 4}
EXPECTED_K2_TRANSIENTS = (
    (3, (1, 10), 252),
    (3, (0, 7), 371),
)

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

FETCHED_REFERENCE_PROVENANCE = {
    AUDIT_INPUT_PATHS[4]:
        "DISK_COPY from origin/physics-loop/proof-grade-blockP6-20260729",
    AUDIT_INPUT_PATHS[5]:
        "DISK_COPY from origin/physics-loop/proof-grade-blockP6-20260729",
    AUDIT_INPUT_PATHS[6]:
        "DISK_COPY/TEXT_ONLY_BLOCKLISTED from "
        "origin/physics-loop/proof-grade-blockP5-20260729",
}

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def check(label: str, condition: bool, detail: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )
    return passed


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("named function", name, len(matches)))
    return matches[0]


def source_anchors() -> dict[str, object]:
    rows = {}
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        payload = path.read_bytes() if path.is_file() else b""
        rows[relative] = {
            "existing_DISK_path": path.is_file(),
            "sha256": sha256(payload).hexdigest(),
            "expected_sha256": EXPECTED_SHA256[relative],
            "git_blob_sha": git_blob_sha(payload),
            "expected_git_blob_sha": EXPECTED_GIT_BLOBS[relative],
            "match": (
                path.is_file()
                and sha256(payload).hexdigest() == EXPECTED_SHA256[relative]
                and git_blob_sha(payload) == EXPECTED_GIT_BLOBS[relative]
            ),
            "execution_mode": (
                "TEXT_ONLY_BLOCKLISTED"
                if relative == AUDIT_INPUT_PATHS[6]
                else (
                    "LANDED_IMPORT"
                    if relative == AUDIT_INPUT_PATHS[0]
                    else "PINNED_TEXT_REFERENCE"
                )
            ),
            "fetch_provenance":
                FETCHED_REFERENCE_PROVENANCE.get(relative, "LANDED_DISK"),
        }
    runner_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    audit_assignment = next(
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
        isinstance(audit_assignment.value, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_assignment.value.elts
        )
        and tuple(ast.literal_eval(audit_assignment.value))
        == AUDIT_INPUT_PATHS
    )
    return {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_tuple": literal_tuple,
        "path_count": len(AUDIT_INPUT_PATHS),
        "existing_disk_only": all(
            (ROOT / relative).is_file() for relative in AUDIT_INPUT_PATHS
        ),
        "no_docs_or_ledgers": all(
            relative.startswith("scripts/") for relative in AUDIT_INPUT_PATHS
        ),
        "rows": rows,
        "cycle784_imported":
            "frontier_cycle784_full_strata_ties_2026_07_28" in sys.modules,
        "pass": (
            literal_tuple
            and len(AUDIT_INPUT_PATHS) == 8
            and all(row["match"] for row in rows.values())
            and "frontier_cycle784_full_strata_ties_2026_07_28"
            not in sys.modules
        ),
    }


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
    return tuple(
        tuple((mask >> station) & 1 for station in range(RING_STATIONS))
        for mask in range(1 << RING_STATIONS)
        if pairwise_separated(
            tuple(
                (mask >> station) & 1
                for station in range(RING_STATIONS)
            )
        )
    )


def configuration_families(
    configurations: tuple[tuple[int, ...], ...],
) -> dict[int, dict[tuple[int, ...], tuple[tuple[int, ...], ...]]]:
    """Reimplement the Cycle-758 construction used by blocklisted Cycle 784."""

    grouped: dict[
        int, dict[tuple[int, ...], set[tuple[int, ...]]]
    ] = {}
    for config in configurations:
        positions = occupied_sites(config)
        count = len(positions)
        representative = (
            min(
                rotate_positions(positions, shift)
                for shift in range(RING_STATIONS)
            )
            if positions
            else ()
        )
        grouped.setdefault(count, {}).setdefault(
            representative, set()
        ).add(positions)
    return {
        count: {
            representative: tuple(sorted(alternatives))
            for representative, alternatives in sorted(families.items())
        }
        for count, families in sorted(grouped.items())
    }


def synchronous_composition_word(
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> tuple[object, ...]:
    stations = len(program)
    positions = tuple(token_positions)
    word = []
    for _step in range(stations):
        live = set(positions)
        for station in range(stations):
            if station in live:
                word.extend(K.mapped_macro(program[station]))
        positions = tuple((station + 1) % stations for station in positions)
    return tuple(word)


def k_epoch_fixtures(
    bank_count: int,
) -> tuple[tuple[int, tuple[int, int], tuple[object, ...], Any], ...]:
    """Exact Cycle-750 fixture reconstruction without importing Cycle 750."""

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


Coordinate = tuple[str, str, int]
Support = frozenset[Coordinate]


def watched_bank_registers() -> tuple[tuple[str, int], ...]:
    rows = [
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
    ]
    rows.extend(
        (f"FRESH_{index}", wire)
        for index, wire in enumerate(K.A.FRESH)
    )
    rows.extend(
        (f"ZERO_WORK_{index}", wire)
        for index, wire in enumerate(K.A.ZERO_WORK)
    )
    rows.append(("TOKEN_OK", K.A.TOKEN_OK))
    return tuple(rows)


def residual_support(state: tuple[int, ...]) -> Support:
    """Own exact support projection of the postimage-cleanliness registers."""

    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    result: set[Coordinate] = set()
    if state[K.R3.X.SOURCE_POINTER]:
        result.add(("source", "SOURCE_POINTER", 0))
    for bank_index, bank in enumerate(banks):
        for register, wire in watched_bank_registers():
            if bank[wire]:
                result.add(("bank", register, bank_index))
    for link_index, link in enumerate(links):
        for wire, content in enumerate(link):
            if content:
                result.add(("link", f"WIRE_{wire}", link_index))
    return frozenset(result)


def clean_postimage(after: int, bank_count: int) -> bool:
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


def residual_definition_basis() -> dict[str, object]:
    trees = {
        relative: ast.parse(
            (ROOT / relative).read_text(encoding="utf-8"),
            filename=relative,
        )
        for relative in (
            AUDIT_INPUT_PATHS[1],
            AUDIT_INPUT_PATHS[3],
            AUDIT_INPUT_PATHS[5],
            AUDIT_INPUT_PATHS[6],
            AUDIT_INPUT_PATHS[7],
        )
    }
    landed_sync = named_function(
        trees[AUDIT_INPUT_PATHS[1]], "synchronous_composition_word"
    )
    landed_clean = named_function(
        trees[AUDIT_INPUT_PATHS[3]], "clean_postimage"
    )
    independent_residual = named_function(
        trees[AUDIT_INPUT_PATHS[5]], "residual_support"
    )
    cycle784_experiment = named_function(
        trees[AUDIT_INPUT_PATHS[6]], "full_strata_experiment"
    )
    cycle794_snapshot = named_function(
        trees[AUDIT_INPUT_PATHS[7]], "evaluate_snapshot"
    )
    local_sync = ast.parse(
        inspect.getsource(synchronous_composition_word)
    ).body[0]
    local_clean = ast.parse(inspect.getsource(clean_postimage)).body[0]
    local_residual = ast.parse(inspect.getsource(residual_support)).body[0]
    residual_names = {
        node.id
        for node in ast.walk(independent_residual)
        if isinstance(node, ast.Name)
    }
    clean_arguments = tuple(
        argument.arg for argument in landed_clean.args.args
    )
    residual_arguments = tuple(
        argument.arg for argument in independent_residual.args.args
    )
    cycle784_source = ast.unparse(cycle784_experiment)
    cycle794_source = ast.unparse(cycle794_snapshot)
    result = {
        "landed_736_synchronous_composition_exact": (
            ast.dump(landed_sync, include_attributes=False)
            == ast.dump(local_sync, include_attributes=False)
        ),
        "landed_758_clean_postimage_exact": (
            ast.dump(landed_clean, include_attributes=False)
            == ast.dump(local_clean, include_attributes=False)
        ),
        "independent_762_residual_support_exact": (
            ast.dump(independent_residual, include_attributes=False)
            == ast.dump(local_residual, include_attributes=False)
        ),
        "clean_postimage_arguments": clean_arguments,
        "residual_support_arguments": residual_arguments,
        "residual_has_no_k_or_positions_input": not (
            {"k", "positions", "token_positions"} & residual_names
        ),
        "cycle784_delegates_family_construction":
            "F758.configuration_families" in cycle784_source,
        "cycle794_horizon_retains_four_exclusions": all(
            token in cycle794_source
            for token in (
                "synchronous_composition",
                "token_rail_return",
                "literal_inverse",
                "clean_postimage",
                "horizon_t_SUPPLIED",
            )
        ),
        "function_AST_sha256": {
            "736_synchronous_composition_word":
                sha256(
                    ast.dump(landed_sync, include_attributes=False).encode()
                ).hexdigest(),
            "758_clean_postimage":
                sha256(
                    ast.dump(landed_clean, include_attributes=False).encode()
                ).hexdigest(),
            "762_residual_support":
                sha256(
                    ast.dump(
                        independent_residual, include_attributes=False
                    ).encode()
                ).hexdigest(),
        },
        "basis": (
            "LANDED/K_AGNOSTIC: clean_postimage(after, bank_count) and the "
            "independent residual_support(state) inspect only the fixed "
            "source/bank/link postimage registers; neither receives k nor "
            "source positions. Cycle-736 already accepts an arbitrary "
            "token_positions tuple."
        ),
        "SUPPLIED_generalization": False,
    }
    result["pass"] = (
        result["landed_736_synchronous_composition_exact"]
        and result["landed_758_clean_postimage_exact"]
        and result["independent_762_residual_support_exact"]
        and clean_arguments == ("after", "bank_count")
        and residual_arguments == ("state",)
        and result["residual_has_no_k_or_positions_input"]
        and result["cycle784_delegates_family_construction"]
        and result["cycle794_horizon_retains_four_exclusions"]
    )
    return result


def evaluate_landed_alternative(
    program: tuple[object, ...],
    before: Any,
    positions: tuple[int, ...],
) -> dict[str, object]:
    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    zeros = tuple(value ^ value for value in tokens)
    word = synchronous_composition_word(program, positions)
    expected = K.A.apply_semantic(before, word)
    after, rail_a, rail_b, _trace = K.run_orbit(
        before, program, token_positions=positions
    )
    restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
        after, program, token_positions=positions, reverse=True
    )
    clean = clean_postimage(after, FIXTURE_BANKS)
    support_row = residual_support(after)
    conditions = {
        "synchronous_composition": after == expected,
        "token_rail_return": rail_a == tokens and rail_b == zeros,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "clean_postimage": clean,
    }
    return {
        "positions": positions,
        "conditions": conditions,
        "failed_exclusions": tuple(
            name for name, passed in conditions.items() if not passed
        ),
        "selected": all(conditions.values()),
        "clean_equals_empty_residual": clean == (not support_row),
        "residual_weight": len(support_row),
    }


def outcome_class(
    selected: tuple[tuple[int, ...], ...],
) -> str:
    if not selected:
        return "zero_survivors"
    if len(selected) == 1:
        return "unique_survivor"
    return "exact_tie"


def build_zero_survivor_catalog() -> dict[str, object]:
    configurations = configuration_census()
    families = configuration_families(configurations)
    fixtures = k_epoch_fixtures(FIXTURE_BANKS)
    class_counts: dict[int, Counter[str]] = {
        k: Counter() for k in TARGET_STRATA
    }
    zero_rows = []
    zero_failed_conditions: Counter[str] = Counter()
    residual_equivalence_failures = 0
    other_exclusion_failures = 0

    for k in TARGET_STRATA:
        for representative, alternatives in families[k].items():
            for event, direction, program, before in fixtures:
                evaluations = tuple(
                    evaluate_landed_alternative(
                        program, before, positions
                    )
                    for positions in alternatives
                )
                selected = tuple(
                    row["positions"]
                    for row in evaluations
                    if row["selected"]
                )
                classification = outcome_class(selected)
                class_counts[k][classification] += 1
                residual_equivalence_failures += sum(
                    not row["clean_equals_empty_residual"]
                    for row in evaluations
                )
                if classification != "zero_survivors":
                    continue
                for evaluation in evaluations:
                    zero_failed_conditions.update(
                        evaluation["failed_exclusions"]
                    )
                    other_exclusion_failures += any(
                        name != "clean_postimage"
                        for name in evaluation["failed_exclusions"]
                    )
                zero_rows.append(
                    {
                        "k": k,
                        "representative": representative,
                        "event": event,
                        "direction": direction,
                        "alternative_count": len(alternatives),
                        "representative_initial_residual_weight": next(
                            row["residual_weight"]
                            for row in evaluations
                            if row["positions"] == representative
                        ),
                        "all_failed_only_clean_postimage": all(
                            row["failed_exclusions"]
                            == ("clean_postimage",)
                            for row in evaluations
                        ),
                    }
                )

    configuration_counts = {
        k: sum(sum(config) == k for config in configurations)
        for k in range(6)
    }
    family_counts = {k: len(families[k]) for k in range(6)}
    normalized_class_counts = {
        k: {
            name: class_counts[k][name]
            for name in (
                "exact_tie",
                "unique_survivor",
                "zero_survivors",
            )
        }
        for k in TARGET_STRATA
    }
    zero_counts = Counter(row["k"] for row in zero_rows)
    result = {
        "configurations": configurations,
        "families": families,
        "fixtures": fixtures,
        "configuration_counts": configuration_counts,
        "family_counts": family_counts,
        "class_counts": normalized_class_counts,
        "zero_counts": dict(sorted(zero_counts.items())),
        "zero_rows": tuple(zero_rows),
        "zero_failed_condition_census":
            dict(sorted(zero_failed_conditions.items())),
        "zero_configuration_evaluations":
            sum(row["alternative_count"] for row in zero_rows),
        "other_exclusion_failures": other_exclusion_failures,
        "residual_equivalence_failures": residual_equivalence_failures,
    }
    result["catalog_sha256"] = digest(
        {
            "configuration_counts": configuration_counts,
            "family_counts": family_counts,
            "class_counts": normalized_class_counts,
            "zero_rows": zero_rows,
        }
    )
    result["pass"] = (
        configuration_counts == EXPECTED_CONFIGURATION_COUNTS
        and family_counts == EXPECTED_FAMILY_COUNTS
        and normalized_class_counts == EXPECTED_CLASS_COUNTS
        and dict(zero_counts) == EXPECTED_ZERO_FAMILY_EPOCHS
        and len(zero_rows) == 42
        and result["zero_configuration_evaluations"] == 42 * 11
        and result["zero_failed_condition_census"]
        == {"clean_postimage": 42 * 11}
        and other_exclusion_failures == 0
        and residual_equivalence_failures == 0
        and all(
            row["all_failed_only_clean_postimage"]
            for row in zero_rows
        )
    )
    return result


def scan_key(
    event: int,
    direction: tuple[int, int],
    program: tuple[object, ...],
    before: Any,
    positions: tuple[int, ...],
    horizon_t: int,
) -> dict[str, object]:
    word = synchronous_composition_word(program, positions)
    initial, rail_a, rail_b, _trace = K.run_orbit(
        before, program, token_positions=positions
    )
    expected_initial = K.A.apply_semantic(before, word)
    expected_rail = tuple(
        int(station in positions) for station in range(len(program))
    )
    state = initial
    initial_support = residual_support(state)
    minimum_weight = len(initial_support)
    first_clean_t = 0 if not initial_support else None
    cycle_period = None
    final_t = 0

    if first_clean_t is None:
        for horizon_index in range(1, horizon_t + 1):
            state = K.A.apply_semantic(state, word)
            final_t = horizon_index
            support_row = residual_support(state)
            minimum_weight = min(minimum_weight, len(support_row))
            if not support_row:
                first_clean_t = horizon_index
                break
            if state == initial:
                cycle_period = horizon_index
                break

    if first_clean_t is not None:
        classification = "TRANSIENT_CLEAN"
    elif cycle_period is not None:
        classification = "CYCLE_CERTIFIED_NONZERO"
    else:
        classification = "OPEN"
        final_t = horizon_t
    return {
        "event": event,
        "direction": direction,
        "positions": positions,
        "horizon_t": horizon_t,
        "classification": classification,
        "first_clean_t": first_clean_t,
        "cycle_start_t": 0 if cycle_period is not None else None,
        "cycle_period": cycle_period,
        "open_through_t":
            horizon_t if classification == "OPEN" else None,
        "last_evaluated_t": final_t,
        "minimum_residual_weight": minimum_weight,
        "initial_residual_weight": len(initial_support),
        "initial_composition_exact": initial == expected_initial,
        "initial_rails_exact":
            rail_a == expected_rail and not any(rail_b),
        "initial_postimage_sha256":
            sha256(str(initial).encode("ascii")).hexdigest(),
    }


def scan_catalog(
    catalog: dict[str, object], horizon_t: int
) -> tuple[dict[str, object], ...]:
    fixture_by_event = {
        row[0]: row for row in catalog["fixtures"]
    }
    rows = []
    for catalog_row in catalog["zero_rows"]:
        event = catalog_row["event"]
        _event, direction, program, before = fixture_by_event[event]
        scan = scan_key(
            event,
            direction,
            program,
            before,
            catalog_row["representative"],
            horizon_t,
        )
        rows.append(
            {
                "k": catalog_row["k"],
                "key": (
                    catalog_row["k"],
                    catalog_row["representative"],
                    event,
                ),
                "family_representative":
                    catalog_row["representative"],
                "family_alternative_count":
                    catalog_row["alternative_count"],
                **scan,
            }
        )
    return tuple(rows)


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


def monitored_selector_evaluation(
    before: Any,
    program: tuple[object, ...],
    positions: tuple[int, ...],
    horizon_t: int,
) -> dict[str, object]:
    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    zeros = tuple(value ^ value for value in tokens)
    actual = before
    expected = before
    rail_a = tokens
    rail_b = zeros
    word = synchronous_composition_word(program, positions)
    for _orbit in range(horizon_t + 1):
        for _step in range(len(program)):
            actual, rail_a, rail_b = K.apply_controller_step(
                actual, program, rail_a, rail_b
            )
        expected = K.A.apply_semantic(expected, word)
    restored, inverse_a, inverse_b = reverse_extended_horizon(
        actual, rail_a, rail_b, program, horizon_t
    )
    conditions = {
        "synchronous_composition": actual == expected,
        "token_rail_return":
            rail_a == tokens and rail_b == zeros,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "clean_postimage": clean_postimage(
            actual, FIXTURE_BANKS
        ),
    }
    return {
        "positions": positions,
        "horizon_t_SUPPLIED": horizon_t,
        "complete_orbits_applied": horizon_t + 1,
        "conditions": conditions,
        "failed_exclusions": tuple(
            name for name, passed in conditions.items() if not passed
        ),
        "selected": all(conditions.values()),
    }


def monitored_selector_for_first_transient(
    transient: dict[str, object],
    catalog: dict[str, object],
) -> dict[str, object]:
    k = transient["k"]
    representative = transient["family_representative"]
    event = transient["event"]
    horizon_t = transient["first_clean_t"]
    fixture = next(
        row for row in catalog["fixtures"] if row[0] == event
    )
    _event, direction, program, before = fixture
    alternatives = catalog["families"][k][representative]
    rows = tuple(
        monitored_selector_evaluation(
            before, program, positions, horizon_t
        )
        for positions in alternatives
    )
    survivors = tuple(
        row["positions"] for row in rows if row["selected"]
    )
    return {
        "k": k,
        "key": transient["key"],
        "event": event,
        "direction": direction,
        "horizon_t_SUPPLIED": horizon_t,
        "battery_basis":
            "complete 11-member Cycle-784 translation family",
        "rows": rows,
        "survivors": survivors,
        "survivor_count": len(survivors),
        "unique": len(survivors) == 1,
        "representative_selected": representative in survivors,
    }


def main() -> int:
    started = monotonic()

    anchors = source_anchors()
    basis = residual_definition_basis()
    catalog = build_zero_survivor_catalog()

    public_catalog = {
        key: value
        for key, value in catalog.items()
        if key not in {
            "configurations",
            "families",
            "fixtures",
            "zero_rows",
        }
    }
    OUTPUT_LINES.append(
        "AUDIT_INPUT_PATHS_LITERAL " + repr(AUDIT_INPUT_PATHS)
    )
    OUTPUT_LINES.append("SOURCE_ANCHORS " + compact(anchors))
    OUTPUT_LINES.append(
        "FETCHED_REFERENCE_DECLARATION "
        + compact(FETCHED_REFERENCE_PROVENANCE)
    )
    OUTPUT_LINES.append(
        "RESIDUAL_DEFINITION_BASIS " + compact(basis)
    )
    OUTPUT_LINES.append("CATALOG_SUMMARY " + compact(public_catalog))
    for row in catalog["zero_rows"]:
        OUTPUT_LINES.append("CATALOG_ZERO_ROW " + compact(row))

    certificate_a = (
        anchors["pass"]
        and catalog["pass"]
        and catalog["zero_counts"] == EXPECTED_ZERO_FAMILY_EPOCHS
    )
    check(
        "CERTIFICATE_A_ANCHORS_REFERENCES_CATALOG_IDENTITY",
        certificate_a,
        {
            "anchors_pass": anchors["pass"],
            "cycle784_TEXT_ONLY_BLOCKLISTED":
                not anchors["cycle784_imported"],
            "configuration_counts": catalog["configuration_counts"],
            "family_counts": catalog["family_counts"],
            "class_counts": catalog["class_counts"],
            "zero_counts": catalog["zero_counts"],
            "catalog_sha256": catalog["catalog_sha256"],
        },
    )

    certificate_b = basis["pass"]
    check(
        "CERTIFICATE_B_RESIDUAL_DEFINITION_LANDED_K_AGNOSTIC",
        certificate_b,
        {
            "basis": basis["basis"],
            "SUPPLIED_generalization":
                basis["SUPPLIED_generalization"],
            "exact_reconstructions": {
                "synchronous_composition":
                    basis[
                        "landed_736_synchronous_composition_exact"
                    ],
                "clean_postimage":
                    basis["landed_758_clean_postimage_exact"],
                "residual_support":
                    basis[
                        "independent_762_residual_support_exact"
                    ],
            },
            "arguments": {
                "clean_postimage":
                    basis["clean_postimage_arguments"],
                "residual_support":
                    basis["residual_support_arguments"],
            },
            "function_AST_sha256":
                basis["function_AST_sha256"],
        },
    )

    fixture_by_event = {
        row[0]: row for row in catalog["fixtures"]
    }
    k2_control_rows = []
    for event, positions, expected_t in EXPECTED_K2_TRANSIENTS:
        _event, direction, program, before = fixture_by_event[event]
        row = scan_key(
            event,
            direction,
            program,
            before,
            positions,
            expected_t,
        )
        k2_control_rows.append(
            {
                "expected_first_clean_t": expected_t,
                **row,
            }
        )
    k2_controls_pass = all(
        row["classification"] == "TRANSIENT_CLEAN"
        and row["first_clean_t"] == row["expected_first_clean_t"]
        and row["minimum_residual_weight"] == 0
        and row["initial_composition_exact"]
        and row["initial_rails_exact"]
        for row in k2_control_rows
    )
    OUTPUT_LINES.append("K2_IDENTITY_CONTROLS " + compact(k2_control_rows))

    first_scan = scan_catalog(catalog, SCAN_HORIZON_T)
    second_scan = scan_catalog(catalog, SCAN_HORIZON_T)
    deterministic = first_scan == second_scan
    scan_sha = digest(first_scan)
    second_scan_sha = digest(second_scan)
    for row in first_scan:
        OUTPUT_LINES.append("SCAN_ROW " + compact(row))

    classification_counts = {
        k: {
            name: sum(
                row["k"] == k and row["classification"] == name
                for row in first_scan
            )
            for name in (
                "TRANSIENT_CLEAN",
                "CYCLE_CERTIFIED_NONZERO",
                "OPEN",
            )
        }
        for k in TARGET_STRATA
    }
    transients = tuple(
        sorted(
            (
                row
                for row in first_scan
                if row["classification"] == "TRANSIENT_CLEAN"
            ),
            key=lambda row: (row["first_clean_t"], row["key"]),
        )
    )
    cycles = tuple(
        row
        for row in first_scan
        if row["classification"] == "CYCLE_CERTIFIED_NONZERO"
    )
    open_rows = tuple(
        row for row in first_scan if row["classification"] == "OPEN"
    )
    certificate_c = (
        len(first_scan) == 42
        and Counter(row["k"] for row in first_scan)
        == Counter(EXPECTED_ZERO_FAMILY_EPOCHS)
        and all(
            row["initial_composition_exact"]
            and row["initial_rails_exact"]
            and row["initial_residual_weight"] > 0
            for row in first_scan
        )
        and all(
            (
                row["first_clean_t"] is not None
                and row["first_clean_t"] <= SCAN_HORIZON_T
            )
            if row["classification"] == "TRANSIENT_CLEAN"
            else (
                row["cycle_period"] is not None
                and row["cycle_period"] <= SCAN_HORIZON_T
            )
            if row["classification"] == "CYCLE_CERTIFIED_NONZERO"
            else row["open_through_t"] == SCAN_HORIZON_T
            for row in first_scan
        )
        and sum(
            sum(counts.values())
            for counts in classification_counts.values()
        )
        == 42
    )
    check(
        "CERTIFICATE_C_FULL_42_KEY_SCAN_TABLE",
        certificate_c,
        {
            "keys": len(first_scan),
            "mandatory_horizon_t": MANDATORY_HORIZON_T,
            "actual_horizon_t": SCAN_HORIZON_T,
            "extension_to_2048_used":
                SCAN_HORIZON_T == 2048,
            "classification_counts": classification_counts,
            "scan_sha256": scan_sha,
        },
    )

    supplied_deviations = (
        {
            "name": "terminal_horizon_index",
            "status": "SUPPLIED",
            "definition":
                "horizon t applies exactly t+1 complete Cycle-719 "
                "controller orbits",
            "landed_exclusions_changed": False,
        },
        {
            "name": "higher_k_family_epoch_scan_key",
            "status": "SUPPLIED",
            "definition":
                "each of the 42 Cycle-784/787 zero-survivor "
                "family-epochs is scanned at its canonical translation "
                "representative",
            "catalog_family_members_changed": False,
        },
        {
            "name": "horizon_extension",
            "status": "SUPPLIED",
            "mandatory_t": MANDATORY_HORIZON_T,
            "used_t": SCAN_HORIZON_T,
            "scientific_law_changed": False,
        },
        {
            "name": "monitored_selector_composition",
            "status": "SUPPLIED",
            "definition":
                "if a representative cleans, reconstruct the Cycle-796 "
                "composition from the landed exact-horizon evolution and "
                "unchanged Cycle-758 four exclusions over the complete "
                "11-member family",
            "used": bool(transients),
            "landed_exclusions_changed": False,
        },
        {
            "name": "reference_disk_transport",
            "status": "SUPPLIED",
            "definition": FETCHED_REFERENCE_PROVENANCE,
            "scientific_law_changed": False,
        },
    )
    for row in supplied_deviations:
        OUTPUT_LINES.append("SUPPLIED_DEVIATION " + compact(row))

    selector_test = None
    if transients:
        outcome = "HIGHER_K_TRANSIENTS_FOUND"
        for row in transients:
            OUTPUT_LINES.append(
                "HIGHER_K_TRANSIENT "
                + compact(
                    {
                        "stratum": row["k"],
                        "key": row["key"],
                        "moment": row["first_clean_t"],
                    }
                )
            )
        selector_test = monitored_selector_for_first_transient(
            transients[0], catalog
        )
        OUTPUT_LINES.append(
            "FIRST_TRANSIENT_MONITORED_SELECTOR "
            + compact(selector_test)
        )
        selector_construction_complete = (
            len(selector_test["rows"]) == 11
            and selector_test["representative_selected"]
            and all(
                row["conditions"]["synchronous_composition"]
                and row["conditions"]["token_rail_return"]
                and row["conditions"]["literal_inverse"]
                for row in selector_test["rows"]
            )
        )
    else:
        outcome = "ALL_CYCLIC_OR_OPEN"
        selector_construction_complete = True
        OUTPUT_LINES.append(
            "ALL_CYCLIC_OR_OPEN "
            + compact(
                {
                    "statement":
                        "higher-k canonical residual keys never clean at "
                        "the scanned horizons; k=2 transients are "
                        "stratum-specific data",
                    "classification_counts": classification_counts,
                }
            )
        )

    certificate_d = (
        k2_controls_pass
        and selector_construction_complete
        and (
            outcome == "HIGHER_K_TRANSIENTS_FOUND"
            if transients
            else outcome == "ALL_CYCLIC_OR_OPEN"
        )
    )
    check(
        "CERTIFICATE_D_OUTCOME_AND_ON_THE_SPOT_SELECTION",
        certificate_d,
        {
            "outcome": outcome,
            "classification_counts": classification_counts,
            "transients": tuple(
                {
                    "stratum": row["k"],
                    "key": row["key"],
                    "moment": row["first_clean_t"],
                }
                for row in transients
            ),
            "k2_identity_controls": k2_control_rows,
            "selection_test": (
                None
                if selector_test is None
                else {
                    "key": selector_test["key"],
                    "moment": selector_test["horizon_t_SUPPLIED"],
                    "survivors": selector_test["survivors"],
                    "unique": selector_test["unique"],
                }
            ),
        },
    )

    elapsed = monotonic() - started
    boundaries = {
        "actuality_claim": False,
        "horizon_is_actuality_or_physical_time": False,
        "fixture_scope_only": True,
        "content_vs_dirt": "OPEN",
        "content_vs_dirt_open": True,
        "axiom_update_triggered": False,
        "cycle_certificate_basis":
            "exact return of the full state to t=0 under a reversible "
            "fixed gate word after every prior projected residual was "
            "nonzero",
        "supplied_deviations": supplied_deviations,
    }
    OUTPUT_LINES.append("BOUNDARIES " + compact(boundaries))
    OUTPUT_LINES.append("axiom_update_triggered: false")
    projected_stdout_bytes = (
        len("\n".join(OUTPUT_LINES).encode("utf-8")) + 16 * 1024
    )
    certificate_e = (
        not boundaries["actuality_claim"]
        and not boundaries["horizon_is_actuality_or_physical_time"]
        and boundaries["fixture_scope_only"]
        and boundaries["content_vs_dirt_open"]
        and not boundaries["axiom_update_triggered"]
        and all(
            row["status"] == "SUPPLIED"
            for row in supplied_deviations
        )
        and deterministic
        and scan_sha == second_scan_sha
        and k2_controls_pass
        and SCAN_HORIZON_T >= MANDATORY_HORIZON_T
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES
    )
    check(
        "CERTIFICATE_E_BOUNDARIES_DETERMINISM_AND_BOUNDS",
        certificate_e,
        {
            "boundaries": boundaries,
            "determinism_sha256_first": scan_sha,
            "determinism_sha256_second": second_scan_sha,
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
            "CYCLE798_HIGHER_K_HORIZON_SCAN_PASS"
            if passed
            else "CYCLE798_HIGHER_K_HORIZON_SCAN_HONEST_FAIL"
        ),
        "pass": passed,
        "outcome": outcome,
        "classification_counts": classification_counts,
        "transient_count": len(transients),
        "cycle_count": len(cycles),
        "open_count": len(open_rows),
        "selection_test": (
            None
            if selector_test is None
            else {
                "key": selector_test["key"],
                "moment": selector_test["horizon_t_SUPPLIED"],
                "survivors": selector_test["survivors"],
                "unique": selector_test["unique"],
            }
        ),
        "determinism_sha256": scan_sha,
        "runtime_seconds": round(elapsed, 6),
        "axiom_update_triggered": False,
    }
    output = (
        "\n".join(OUTPUT_LINES)
        + "\nFINAL "
        + compact(terminal)
        + "\n"
    )
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
