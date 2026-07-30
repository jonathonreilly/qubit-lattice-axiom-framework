#!/usr/bin/env python3
"""Cycle 801 independent adversarial checker.

This runner does not import either Cycle 798 or Cycle 801.  It reconstructs
the higher-k catalog from the landed Cycle-719 controller, executes every
gate with a separate packed-state interpreter, and searches complete
128-bit state-hash histories for an earlier clean postimage or recurrence.

The horizon is a finite controller-orbit index.  Nothing here promotes it to
physical time, actuality, probability, or a content/dirt interpretation.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
    "scripts/frontier_cycle762_residual_probe_independent_check_2026_07_28.py",
    "scripts/frontier_cycle798_higher_k_horizon_scan_2026_07_28.py",
    "scripts/frontier_cycle801_silent_strata_deep_scan_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any

import numpy as np
from numba import njit


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

# This landed controller is a construction supplier, not either blocklisted
# primary.  Its gate application routine and orbit routine are deliberately
# never called below.
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
TARGET_STRATA = (3, 4, 5)
BASELINE_T = 2048
TARGET_T = 8192

PRIMARY_MODULE_NAMES = (
    "frontier_cycle798_higher_k_horizon_scan_2026_07_28",
    "frontier_cycle801_silent_strata_deep_scan_2026_07_28",
)
PRIMARY_PATHS = AUDIT_INPUT_PATHS[-2:]

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    AUDIT_INPUT_PATHS[3]:
        "c8d43dc2c65b851554393c493d016f6341ba9eb8c3a35bb9f361d77a2f16c619",
    AUDIT_INPUT_PATHS[4]:
        "f6ec49636ecb7ec09808eed7d38f2085f6145cd383c306370502c547741942b1",
    AUDIT_INPUT_PATHS[5]:
        "55edc0cc8b3e51de3863819f10303d506e0652dbc031a1f2647c3a11e51cb115",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
    AUDIT_INPUT_PATHS[2]: "4e23e03ecc5f92a0b8348bfa526eb5b2f2b09dd0",
    AUDIT_INPUT_PATHS[3]: "3eff0f787a12cacf504324209f578f0c1df91c90",
    AUDIT_INPUT_PATHS[4]: "9de34ad5adcbf484d4f0c7e6aec13375ed465aab",
    AUDIT_INPUT_PATHS[5]: "8807587899a5664d39a06901b02b22041682c5cc",
}

EXPECTED_CONFIGURATION_COUNTS = {
    0: 1, 1: 11, 2: 44, 3: 77, 4: 55, 5: 11,
}
EXPECTED_FAMILY_COUNTS = {0: 1, 1: 1, 2: 4, 3: 7, 4: 5, 5: 1}
EXPECTED_CLASS_COUNTS = {
    3: {"exact_tie": 7, "unique_survivor": 3, "zero_survivors": 18},
    4: {"exact_tie": 0, "unique_survivor": 0, "zero_survivors": 20},
    5: {"exact_tie": 0, "unique_survivor": 0, "zero_survivors": 4},
}
EXPECTED_ZERO_COUNTS = {3: 18, 4: 20, 5: 4}
EXPECTED_T2048_TRANSIENT_MOMENTS = {
    3: (444, 532, 681, 1385), 4: (), 5: (),
}
EXPECTED_T2048_OPEN_COUNTS = {3: 14, 4: 20, 5: 4}
EXPECTED_T2048_CYCLE_COUNTS = {3: 0, 4: 0, 5: 0}

# Filled from the independently reconstructed payload during incremental
# development, using the Cycle-798 canonical JSON field convention.
EXPECTED_CATALOG_SHA256 = (
    "a04434f9bffac1f04e5f65a613355e020001af44e7b71368b311568a61052934"
)

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []

Key = tuple[int, tuple[int, ...], int]
Circuit = tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]


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
    required_functions = {
        AUDIT_INPUT_PATHS[0]: {
            "interleaved_program", "mapped_macro",
        },
        AUDIT_INPUT_PATHS[1]: {"synchronous_composition_word"},
        AUDIT_INPUT_PATHS[2]: {
            "configuration_families", "clean_postimage",
        },
        AUDIT_INPUT_PATHS[3]: {"residual_support"},
        AUDIT_INPUT_PATHS[4]: {
            "build_zero_survivor_catalog", "scan_key",
        },
        AUDIT_INPUT_PATHS[5]: {
            "initialise_catalog_records", "advance_one_record",
        },
    }
    rows: dict[str, object] = {}
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        payload = path.read_bytes() if path.is_file() else b""
        try:
            tree = ast.parse(payload, filename=relative)
            functions = {
                node.name for node in tree.body
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            }
            ast_control = required_functions[relative] <= functions
        except (SyntaxError, ValueError):
            ast_control = False
        actual_sha = sha256(payload).hexdigest()
        actual_blob = git_blob_sha(payload)
        rows[relative] = {
            "existing_DISK_path": path.is_file(),
            "sha256": actual_sha,
            "expected_sha256": EXPECTED_SHA256[relative],
            "git_blob_sha": actual_blob,
            "expected_git_blob_sha": EXPECTED_GIT_BLOBS[relative],
            "required_function_AST_present": ast_control,
            "execution_mode": (
                "TEXT_ONLY_BLOCKLISTED"
                if relative in PRIMARY_PATHS
                else (
                    "LANDED_IMPORT"
                    if relative == AUDIT_INPUT_PATHS[0]
                    else "PINNED_TEXT_REFERENCE"
                )
            ),
            "match": (
                path.is_file()
                and actual_sha == EXPECTED_SHA256[relative]
                and actual_blob == EXPECTED_GIT_BLOBS[relative]
                and ast_control
            ),
        }

    checker_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )
    assignments = [
        node for node in checker_tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    ]
    literal_tuple = (
        len(assignments) == 1
        and isinstance(assignments[0].value, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in assignments[0].value.elts
        )
        and tuple(ast.literal_eval(assignments[0].value))
        == AUDIT_INPUT_PATHS
    )
    imported_modules = {
        alias.name
        for node in checker_tree.body
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    }
    no_primary_import_syntax = all(
        module not in imported_modules for module in PRIMARY_MODULE_NAMES
    )
    primary_modules_absent = all(
        module not in sys.modules for module in PRIMARY_MODULE_NAMES
    )
    landed_import_exact = (
        Path(K.__file__).resolve()
        == (ROOT / AUDIT_INPUT_PATHS[0]).resolve()
    )
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_tuple": literal_tuple,
        "existing_disk_only": all(
            (ROOT / relative).is_file() for relative in AUDIT_INPUT_PATHS
        ),
        "rows": rows,
        "primary_execution_mode": {
            relative: rows[relative]["execution_mode"]
            for relative in PRIMARY_PATHS
        },
        "no_primary_import_syntax": no_primary_import_syntax,
        "primary_modules_absent": primary_modules_absent,
        "landed_import_exact_disk_path": landed_import_exact,
    }
    result["pass"] = (
        literal_tuple
        and result["existing_disk_only"]
        and all(row["match"] for row in rows.values())
        and no_primary_import_syntax
        and primary_modules_absent
        and landed_import_exact
    )
    return result


def splitmix64(value: int) -> int:
    mask = (1 << 64) - 1
    value = (value + 0x9E3779B97F4A7C15) & mask
    value = ((value ^ (value >> 30)) * 0xBF58476D1CE4E5B9) & mask
    value = ((value ^ (value >> 27)) * 0x94D049BB133111EB) & mask
    return (value ^ (value >> 31)) & mask


def zobrist_tokens(width: int) -> tuple[np.ndarray, np.ndarray]:
    first = np.array(
        [splitmix64(0xC801000000000000 + wire) for wire in range(width)],
        dtype=np.uint64,
    )
    second = np.array(
        [splitmix64(0x7980000000000000 + wire) for wire in range(width)],
        dtype=np.uint64,
    )
    if not np.all(first) or not np.all(second):
        raise AssertionError("zero Zobrist token")
    return first, second


def compile_word(word: tuple[object, ...]) -> Circuit:
    kinds = np.empty(len(word), dtype=np.uint8)
    control_a = np.full(len(word), -1, dtype=np.int32)
    control_b = np.full(len(word), -1, dtype=np.int32)
    targets = np.empty(len(word), dtype=np.int32)
    for index, gate in enumerate(word):
        if gate.kind == "X":
            kinds[index] = 0
            targets[index] = gate.wires[0]
        elif gate.kind == "CNOT":
            kinds[index] = 1
            control_a[index] = gate.wires[0]
            targets[index] = gate.wires[1]
        elif gate.kind == "TOF":
            kinds[index] = 2
            control_a[index] = gate.wires[0]
            control_b[index] = gate.wires[1]
            targets[index] = gate.wires[2]
        else:
            raise ValueError(("unsupported gate", gate))
    return kinds, control_a, control_b, targets


@njit
def apply_circuit_once(
    before: np.ndarray,
    kinds: np.ndarray,
    control_a: np.ndarray,
    control_b: np.ndarray,
    targets: np.ndarray,
) -> np.ndarray:
    state = before.copy()
    for gate_index in range(kinds.size):
        kind = kinds[gate_index]
        target = targets[gate_index]
        if kind == 0:
            state[target] ^= np.uint8(1)
        elif kind == 1:
            state[target] ^= state[control_a[gate_index]]
        else:
            state[target] ^= (
                state[control_a[gate_index]]
                & state[control_b[gate_index]]
            )
    return state


@njit
def evolve_hashed_trace(
    before: np.ndarray,
    kinds: np.ndarray,
    control_a: np.ndarray,
    control_b: np.ndarray,
    targets: np.ndarray,
    first_tokens: np.ndarray,
    second_tokens: np.ndarray,
    residual_indices: np.ndarray,
    horizon_t: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, int, np.ndarray]:
    """Own evolution plus two independent incremental full-state hashes."""

    state = before.copy()
    hashes = np.empty((horizon_t + 1, 2), dtype=np.uint64)
    weights = np.empty(horizon_t + 1, dtype=np.int16)
    first_hash = np.uint64(0)
    second_hash = np.uint64(0)
    for wire in range(state.size):
        if state[wire]:
            first_hash ^= first_tokens[wire]
            second_hash ^= second_tokens[wire]
    hashes[0, 0] = first_hash
    hashes[0, 1] = second_hash
    initial_first = first_hash
    initial_second = second_hash
    weight = 0
    for index in residual_indices:
        weight += state[index]
    weights[0] = weight

    exact_return_t = -1
    closure_state = np.zeros(state.size, dtype=np.uint8)
    for horizon_index in range(1, horizon_t + 1):
        for gate_index in range(kinds.size):
            kind = kinds[gate_index]
            target = targets[gate_index]
            if kind == 0:
                flip = np.uint8(1)
            elif kind == 1:
                flip = state[control_a[gate_index]]
            else:
                flip = (
                    state[control_a[gate_index]]
                    & state[control_b[gate_index]]
                )
            if flip:
                state[target] ^= np.uint8(1)
                first_hash ^= first_tokens[target]
                second_hash ^= second_tokens[target]
        hashes[horizon_index, 0] = first_hash
        hashes[horizon_index, 1] = second_hash
        weight = 0
        for index in residual_indices:
            weight += state[index]
        weights[horizon_index] = weight

        if (
            exact_return_t < 0
            and first_hash == initial_first
            and second_hash == initial_second
        ):
            equal = True
            for wire in range(state.size):
                if state[wire] != before[wire]:
                    equal = False
                    break
            if equal:
                exact_return_t = horizon_index
                closure_state[:] = state
    return hashes, weights, state, exact_return_t, closure_state


def canonical_state_bytes(state: np.ndarray) -> bytes:
    width = int(state.size)
    packed = np.packbits(state, bitorder="little").tobytes()
    return width.to_bytes(4, "little") + packed


def state_sha256(state: np.ndarray) -> str:
    return sha256(canonical_state_bytes(state)).hexdigest()


def direct_zobrist(
    state: np.ndarray,
    first_tokens: np.ndarray,
    second_tokens: np.ndarray,
) -> tuple[int, int]:
    first = 0
    second = 0
    for wire in np.flatnonzero(state):
        first ^= int(first_tokens[wire])
        second ^= int(second_tokens[wire])
    return first, second


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def configuration_census() -> tuple[tuple[int, ...], ...]:
    rows = []
    for mask in range(1 << RING_STATIONS):
        config = tuple(
            (mask >> station) & 1 for station in range(RING_STATIONS)
        )
        if not any(
            config[station] and config[(station + 1) % RING_STATIONS]
            for station in range(RING_STATIONS)
        ):
            rows.append(config)
    return tuple(rows)


def configuration_families(
    configurations: tuple[tuple[int, ...], ...],
) -> dict[int, dict[tuple[int, ...], tuple[tuple[int, ...], ...]]]:
    grouped: dict[
        int, dict[tuple[int, ...], set[tuple[int, ...]]]
    ] = {}
    for config in configurations:
        positions = tuple(
            station for station, occupied in enumerate(config) if occupied
        )
        count = len(positions)
        representative = (
            min(
                rotate_positions(positions, shift)
                for shift in range(RING_STATIONS)
            )
            if positions else ()
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


def synchronous_word(
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


def controller_word_by_rail_simulation(
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> tuple[tuple[object, ...], tuple[int, ...], tuple[int, ...]]:
    """Second construction route: explicitly evolve both controller rails."""

    stations = len(program)
    rail_a = [
        int(station in token_positions) for station in range(stations)
    ]
    rail_b = [0] * stations
    word = []
    for _step in range(stations):
        for station in range(stations):
            if rail_a[station]:
                word.extend(K.mapped_macro(program[station]))
        for station in range(stations):
            rail_a[station], rail_b[station] = (
                rail_b[station], rail_a[station]
            )
        for station in range(stations):
            target = (station + 1) % stations
            rail_b[station], rail_a[target] = (
                rail_a[target], rail_b[station]
            )
    return tuple(word), tuple(rail_a), tuple(rail_b)


def residual_indices() -> np.ndarray:
    watched_bank_wires = (
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        K.A.DIRECTION_OK,
        *K.A.FRESH,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )
    indices = {K.R3.X.SOURCE_POINTER}
    for base in K.M.R12.BANK_BASES[:FIXTURE_BANKS]:
        indices.update(base + wire for wire in watched_bank_wires)
    for base in K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]:
        indices.update(range(base, base + K.B.LINK_WIDTH))
    return np.array(sorted(indices), dtype=np.int32)


def active_state_width(
    program: tuple[object, ...], residual: np.ndarray
) -> int:
    maximum = int(residual[-1])
    for row in program:
        for gate in K.mapped_macro(row):
            maximum = max(maximum, *gate.wires)
    for gate in K.M.global_allocator_word(FIXTURE_BANKS):
        maximum = max(maximum, *gate.wires)
    return maximum + 1


def landed_cleanliness_direct(state: np.ndarray) -> bool:
    """Literal Cycle-758 postimage test, without importing that module."""

    if state[K.R3.X.SOURCE_POINTER]:
        return False
    watched = (
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        K.A.DIRECTION_OK,
        *K.A.FRESH,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )
    for base in K.M.R12.BANK_BASES[:FIXTURE_BANKS]:
        if any(state[base + wire] for wire in watched):
            return False
    for base in K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]:
        if any(
            state[base + wire] for wire in range(K.B.LINK_WIDTH)
        ):
            return False
    return True


def residual_weight(
    state: np.ndarray, residual: np.ndarray
) -> int:
    return int(np.sum(state[residual], dtype=np.int64))


def prepare_endpoint_own(
    state: np.ndarray, direction: tuple[int, int]
) -> np.ndarray:
    result = state.copy()
    if result[K.R3.X.SOURCE_POINTER]:
        raise ValueError("source pointer pending")
    result[K.R3.X.LEFT_ENDPOINT] = int(direction == (0, 1))
    result[K.R3.X.RIGHT_ENDPOINT] = int(direction == (1, 0))
    result[K.R3.X.SOURCE_POINTER] = int(direction != (0, 0))
    return result


def gate_signature(word: tuple[object, ...]) -> tuple[object, ...]:
    return tuple((gate.kind, tuple(gate.wires)) for gate in word)


def build_independent_catalog() -> dict[str, object]:
    configurations = configuration_census()
    families = configuration_families(configurations)
    program = K.interleaved_program(FIXTURE_BANKS)
    residual = residual_indices()
    width = active_state_width(program, residual)

    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    packed = K.M.pack_state(banks, links)
    if any(packed[width:]):
        raise AssertionError("nonzero state outside independent active width")
    state = np.array(packed[:width], dtype=np.uint8)
    allocator_word = tuple(K.M.global_allocator_word(FIXTURE_BANKS))
    one_token_word = synchronous_word(program, (0,))
    allocator_circuit = compile_word(allocator_word)
    one_token_circuit = compile_word(one_token_word)
    allocator_composition_rows = []
    fixtures = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = prepare_endpoint_own(state, direction)
        fixtures.append((event, direction, before.copy()))
        allocator_after = apply_circuit_once(before, *allocator_circuit)
        controller_after = apply_circuit_once(before, *one_token_circuit)
        allocator_composition_rows.append(
            np.array_equal(allocator_after, controller_after)
        )
        state = allocator_after

    word_cache: dict[tuple[int, ...], tuple[object, ...]] = {}
    circuit_cache: dict[tuple[int, ...], Circuit] = {}
    inverse_cache: dict[tuple[int, ...], Circuit] = {}
    controller_controls: dict[tuple[int, ...], dict[str, object]] = {}
    for k in TARGET_STRATA:
        for alternatives in families[k].values():
            for positions in alternatives:
                if positions in word_cache:
                    continue
                word = synchronous_word(program, positions)
                rail_word, rail_a, rail_b = (
                    controller_word_by_rail_simulation(program, positions)
                )
                expected_rail = tuple(
                    int(station in positions)
                    for station in range(len(program))
                )
                word_cache[positions] = word
                circuit_cache[positions] = compile_word(word)
                inverse_cache[positions] = compile_word(
                    tuple(reversed(word))
                )
                controller_controls[positions] = {
                    "composition_exact":
                        gate_signature(word) == gate_signature(rail_word),
                    "rail_return_exact":
                        rail_a == expected_rail and not any(rail_b),
                }

    class_counts: dict[int, Counter[str]] = {
        k: Counter() for k in TARGET_STRATA
    }
    zero_rows: list[dict[str, object]] = []
    records: dict[Key, dict[str, object]] = {}
    residual_equivalence_failures = 0
    inverse_failures = 0
    controller_failures = 0
    zero_other_exclusion_failures = 0
    for k in TARGET_STRATA:
        for representative, alternatives in families[k].items():
            for event, direction, before in fixtures:
                evaluations = []
                for positions in alternatives:
                    after = apply_circuit_once(
                        before, *circuit_cache[positions]
                    )
                    restored = apply_circuit_once(
                        after, *inverse_cache[positions]
                    )
                    direct_clean = landed_cleanliness_direct(after)
                    mask_clean = residual_weight(after, residual) == 0
                    inverse_exact = np.array_equal(restored, before)
                    controls = controller_controls[positions]
                    conditions = {
                        "synchronous_composition":
                            controls["composition_exact"],
                        "token_rail_return":
                            controls["rail_return_exact"],
                        "literal_inverse": inverse_exact,
                        "clean_postimage": direct_clean,
                    }
                    residual_equivalence_failures += (
                        direct_clean != mask_clean
                    )
                    inverse_failures += not inverse_exact
                    controller_failures += not (
                        controls["composition_exact"]
                        and controls["rail_return_exact"]
                    )
                    evaluations.append(
                        {
                            "positions": positions,
                            "state": after,
                            "residual_weight":
                                residual_weight(after, residual),
                            "conditions": conditions,
                            "failed_exclusions": tuple(
                                name for name, passed in conditions.items()
                                if not passed
                            ),
                            "selected": all(conditions.values()),
                        }
                    )
                selected = tuple(
                    row["positions"] for row in evaluations
                    if row["selected"]
                )
                classification = (
                    "zero_survivors" if not selected
                    else "unique_survivor" if len(selected) == 1
                    else "exact_tie"
                )
                class_counts[k][classification] += 1
                if classification != "zero_survivors":
                    continue
                all_failed_only_clean = all(
                    row["failed_exclusions"] == ("clean_postimage",)
                    for row in evaluations
                )
                zero_other_exclusion_failures += sum(
                    any(
                        exclusion != "clean_postimage"
                        for exclusion in row["failed_exclusions"]
                    )
                    for row in evaluations
                )
                representative_evaluation = next(
                    row for row in evaluations
                    if row["positions"] == representative
                )
                zero_row = {
                    "k": k,
                    "representative": representative,
                    "event": event,
                    "direction": direction,
                    "alternative_count": len(alternatives),
                    "representative_initial_residual_weight":
                        representative_evaluation["residual_weight"],
                    "all_failed_only_clean_postimage":
                        all_failed_only_clean,
                }
                zero_rows.append(zero_row)
                key = (k, representative, event)
                if key in records:
                    raise AssertionError(("duplicate catalog key", key))
                records[key] = {
                    "key": key,
                    "k": k,
                    "positions": representative,
                    "event": event,
                    "direction": direction,
                    "initial_state":
                        representative_evaluation["state"].copy(),
                    "word": word_cache[representative],
                    "circuit": circuit_cache[representative],
                    "initial_residual_weight":
                        representative_evaluation["residual_weight"],
                }

    configuration_counts = {
        k: sum(sum(config) == k for config in configurations)
        for k in range(6)
    }
    family_counts = {k: len(families[k]) for k in range(6)}
    normalized_class_counts = {
        k: {
            name: class_counts[k][name]
            for name in ("exact_tie", "unique_survivor", "zero_survivors")
        }
        for k in TARGET_STRATA
    }
    zero_counts = dict(sorted(Counter(
        row["k"] for row in zero_rows
    ).items()))
    catalog_payload = {
        "configuration_counts": configuration_counts,
        "family_counts": family_counts,
        "class_counts": normalized_class_counts,
        "zero_rows": zero_rows,
    }
    return {
        "program": program,
        "state_width": width,
        "residual_indices": residual,
        "fixtures": tuple(fixtures),
        "families": families,
        "records": records,
        "configuration_counts": configuration_counts,
        "family_counts": family_counts,
        "class_counts": normalized_class_counts,
        "zero_counts": zero_counts,
        "zero_rows": tuple(zero_rows),
        "catalog_sha256": digest(catalog_payload),
        "allocator_composition_exact":
            all(allocator_composition_rows),
        "residual_equivalence_failures": residual_equivalence_failures,
        "inverse_failures": inverse_failures,
        "controller_failures": controller_failures,
        "zero_other_exclusion_failures":
            zero_other_exclusion_failures,
        "all_initial_residuals_nonzero": all(
            record["initial_residual_weight"] > 0
            for record in records.values()
        ),
    }


def first_hash_repeat(hashes: np.ndarray) -> tuple[int, int] | None:
    seen: dict[tuple[int, int], int] = {}
    for horizon_t in range(hashes.shape[0]):
        fingerprint = (
            int(hashes[horizon_t, 0]),
            int(hashes[horizon_t, 1]),
        )
        if fingerprint in seen:
            return seen[fingerprint], horizon_t
        seen[fingerprint] = horizon_t
    return None


def scan_record(
    record: dict[str, object],
    horizon_t: int,
    first_tokens: np.ndarray,
    second_tokens: np.ndarray,
    residual: np.ndarray,
) -> dict[str, object]:
    initial = record["initial_state"]
    hashes, weights, final_state, exact_return_t, closure_state = (
        evolve_hashed_trace(
            initial,
            *record["circuit"],
            first_tokens,
            second_tokens,
            residual,
            horizon_t,
        )
    )
    clean_indices = np.flatnonzero(weights == 0)
    first_clean_t = (
        int(clean_indices[0]) if clean_indices.size else None
    )
    initial_hash = direct_zobrist(
        initial, first_tokens, second_tokens
    )
    final_hash = direct_zobrist(
        final_state, first_tokens, second_tokens
    )
    trace_initial_hash = (
        int(hashes[0, 0]), int(hashes[0, 1])
    )
    trace_final_hash = (
        int(hashes[-1, 0]), int(hashes[-1, 1])
    )
    exact_closure = (
        exact_return_t >= 0
        and np.array_equal(closure_state, initial)
    )
    return {
        "key": record["key"],
        "k": record["k"],
        "positions": record["positions"],
        "event": record["event"],
        "direction": record["direction"],
        "horizon_t": horizon_t,
        "hashes": hashes,
        "weights": weights,
        "final_state": final_state,
        "first_clean_t": first_clean_t,
        "exact_return_t":
            None if exact_return_t < 0 else int(exact_return_t),
        "hash_first_repeat": first_hash_repeat(hashes),
        "exact_closure": exact_closure,
        "initial_state_sha256": state_sha256(initial),
        "closure_state_sha256": (
            state_sha256(closure_state) if exact_closure else None
        ),
        "final_state_sha256": state_sha256(final_state),
        "minimum_residual_weight": int(np.min(weights)),
        "initial_residual_weight": int(weights[0]),
        "initial_hash_recomputed_exact":
            initial_hash == trace_initial_hash,
        "final_hash_recomputed_exact":
            final_hash == trace_final_hash,
        "hash_history_sha256": sha256(
            hashes.astype("<u8", copy=False).tobytes()
        ).hexdigest(),
        "residual_history_sha256": sha256(
            weights.astype("<i2", copy=False).tobytes()
        ).hexdigest(),
    }


def outcome_at(scan: dict[str, object], horizon_t: int) -> str:
    first_clean = scan["first_clean_t"]
    exact_return = scan["exact_return_t"]
    if first_clean is not None and first_clean <= horizon_t:
        return "TRANSIENT_CLEAN"
    if exact_return is not None and exact_return <= horizon_t:
        return "CYCLE_CERTIFIED_NONZERO"
    return "OPEN"


def public_scan_fingerprint(scan: dict[str, object]) -> dict[str, object]:
    return {
        "key": scan["key"],
        "horizon_t": scan["horizon_t"],
        "first_clean_t": scan["first_clean_t"],
        "exact_return_t": scan["exact_return_t"],
        "hash_first_repeat": scan["hash_first_repeat"],
        "exact_closure": scan["exact_closure"],
        "initial_state_sha256": scan["initial_state_sha256"],
        "closure_state_sha256": scan["closure_state_sha256"],
        "final_state_sha256": scan["final_state_sha256"],
        "minimum_residual_weight": scan["minimum_residual_weight"],
        "initial_hash_recomputed_exact":
            scan["initial_hash_recomputed_exact"],
        "final_hash_recomputed_exact":
            scan["final_hash_recomputed_exact"],
        "hash_history_sha256": scan["hash_history_sha256"],
        "residual_history_sha256": scan["residual_history_sha256"],
    }


def trace_digest(scan: dict[str, object]) -> str:
    payload = (
        scan["hashes"].astype("<u8", copy=False).tobytes()
        + scan["weights"].astype("<i2", copy=False).tobytes()
        + canonical_state_bytes(scan["final_state"])
    )
    return sha256(payload).hexdigest()


def main() -> int:
    started = monotonic()
    anchors = source_anchors()
    catalog = build_independent_catalog()
    records: dict[Key, dict[str, object]] = catalog["records"]
    residual = catalog["residual_indices"]
    first_tokens, second_tokens = zobrist_tokens(catalog["state_width"])

    scans: dict[Key, dict[str, object]] = {}
    for key in sorted(records):
        scans[key] = scan_record(
            records[key],
            TARGET_T,
            first_tokens,
            second_tokens,
            residual,
        )

    baseline_transient_moments = {
        k: tuple(sorted(
            scan["first_clean_t"]
            for scan in scans.values()
            if scan["k"] == k
            and scan["first_clean_t"] is not None
            and scan["first_clean_t"] <= BASELINE_T
        ))
        for k in TARGET_STRATA
    }
    baseline_cycle_counts = {
        k: sum(
            scan["k"] == k
            and outcome_at(scan, BASELINE_T)
            == "CYCLE_CERTIFIED_NONZERO"
            for scan in scans.values()
        )
        for k in TARGET_STRATA
    }
    baseline_open_counts = {
        k: sum(
            scan["k"] == k and outcome_at(scan, BASELINE_T) == "OPEN"
            for scan in scans.values()
        )
        for k in TARGET_STRATA
    }
    open2048 = tuple(sorted(
        key for key, scan in scans.items()
        if outcome_at(scan, BASELINE_T) == "OPEN"
    ))

    target_cycles = tuple(
        scans[key] for key in open2048
        if outcome_at(scans[key], TARGET_T)
        == "CYCLE_CERTIFIED_NONZERO"
    )
    target_cycles = tuple(sorted(
        target_cycles, key=lambda scan: scan["key"]
    ))
    new_transients = tuple(sorted(
        (
            scans[key] for key in open2048
            if outcome_at(scans[key], TARGET_T) == "TRANSIENT_CLEAN"
        ),
        key=lambda scan: (scan["first_clean_t"], scan["key"]),
    ))
    still_open = tuple(
        scans[key] for key in open2048
        if outcome_at(scans[key], TARGET_T) == "OPEN"
    )

    cycle_certificate_rows = []
    for ordinal, scan in enumerate(target_cycles, start=1):
        period = scan["exact_return_t"]
        if period is None:
            period_nonzero = False
            period_minimum = None
        else:
            period_weights = scan["weights"][:period]
            period_minimum = int(np.min(period_weights))
            period_nonzero = bool(np.all(period_weights > 0))
        expected_period = 5952 if scan["k"] == 3 else 4464
        certificate = {
            "ordinal": ordinal,
            "key": scan["key"],
            "entry_t": 0,
            "period": period,
            "closure_t": period,
            "expected_period_for_stratum": expected_period,
            "hash_first_repeat": scan["hash_first_repeat"],
            "exact_full_state_closure": scan["exact_closure"],
            "state_sha256_at_entry": scan["initial_state_sha256"],
            "state_sha256_at_closure":
                scan["closure_state_sha256"],
            "minimum_residual_weight_one_period": period_minimum,
            "residual_nonzero_on_complete_period": period_nonzero,
            "forever_nonzero_basis": (
                "exact state closure plus nonzero LANDED residual at "
                "every state of one complete period"
            ),
        }
        cycle_pass = (
            period == expected_period
            and scan["hash_first_repeat"] == (0, period)
            and scan["exact_closure"]
            and scan["initial_state_sha256"]
            == scan["closure_state_sha256"]
            and period_nonzero
            and period_minimum is not None
            and period_minimum > 0
            and scan["first_clean_t"] is None
            and scan["initial_hash_recomputed_exact"]
            and scan["final_hash_recomputed_exact"]
        )
        safe_key = (
            f"K{scan['k']}_P"
            + "_".join(str(value) for value in scan["positions"])
            + f"_E{scan['event']}"
        )
        check(
            f"ATTACK_1_CYCLE_{ordinal}_{safe_key}",
            cycle_pass,
            certificate,
        )
        cycle_certificate_rows.append({
            **certificate,
            "pass": cycle_pass,
        })

    cycle_period_census = {
        k: dict(sorted(Counter(
            scan["exact_return_t"]
            for scan in target_cycles if scan["k"] == k
        ).items()))
        for k in TARGET_STRATA
    }
    attack_1_pass = (
        len(target_cycles) == 6
        and cycle_period_census
        == {3: {5952: 4}, 4: {4464: 2}, 5: {}}
        and len(cycle_certificate_rows) == 6
        and all(row["pass"] for row in cycle_certificate_rows)
    )
    check(
        "ATTACK_1_SIX_NEW_CYCLES_INDEPENDENT",
        attack_1_pass,
        {
            "cycle_count": len(target_cycles),
            "cycle_period_census": cycle_period_census,
            "cycles": cycle_certificate_rows,
            "state_hash": (
                "two independently seeded 64-bit Zobrist hashes updated "
                "at every gate; candidate closures then compared bit-exact"
            ),
        },
    )
    OUTPUT_LINES.append(
        "FINDING_ATTACK_1_VERBATIM "
        + compact({
            "statement": (
                "The independent checker finds exactly six cycles: four "
                "k=3 entry-0 period-5952 cycles and two k=4 entry-0 "
                "period-4464 cycles; every state in each certified period "
                "has nonzero LANDED residual, so exact closure makes that "
                "nonzero property permanent."
            ),
            "cycles": tuple(
                {
                    "key": row["key"],
                    "entry_t": row["entry_t"],
                    "period": row["period"],
                    "minimum_residual_weight_one_period":
                        row["minimum_residual_weight_one_period"],
                }
                for row in cycle_certificate_rows
            ),
        })
    )

    target_counts = {
        k: {
            "new_transient": sum(
                scan["k"] == k for scan in new_transients
            ),
            "new_cycle": sum(
                scan["k"] == k for scan in target_cycles
            ),
            "open": sum(scan["k"] == k for scan in still_open),
        }
        for k in TARGET_STRATA
    }
    unexpected_hash_repeats = tuple(
        {
            "key": scans[key]["key"],
            "hash_first_repeat": scans[key]["hash_first_repeat"],
            "exact_return_t": scans[key]["exact_return_t"],
        }
        for key in open2048
        if (
            scans[key]["hash_first_repeat"] is not None
            and scans[key]["exact_return_t"] is None
        )
        or (
            scans[key]["exact_return_t"] is not None
            and scans[key]["hash_first_repeat"]
            != (0, scans[key]["exact_return_t"])
        )
    )
    attack_2_pass = (
        len(open2048) == 38
        and not new_transients
        and len(target_cycles) == 6
        and len(still_open) == 32
        and target_counts
        == {
            3: {"new_transient": 0, "new_cycle": 4, "open": 10},
            4: {"new_transient": 0, "new_cycle": 2, "open": 18},
            5: {"new_transient": 0, "new_cycle": 0, "open": 4},
        }
        and not unexpected_hash_repeats
        and all(
            scan["horizon_t"] == TARGET_T
            and scan["hashes"].shape[0] == TARGET_T + 1
            and scan["weights"].shape[0] == TARGET_T + 1
            and scan["initial_hash_recomputed_exact"]
            and scan["final_hash_recomputed_exact"]
            for key, scan in scans.items() if key in open2048
        )
    )
    check(
        "ATTACK_2_MISSED_EVENT_HUNT_ALL_38_TO_T8192",
        attack_2_pass,
        {
            "T2048_open_input_keys": len(open2048),
            "complete_trace_horizon_t": TARGET_T,
            "new_transients": tuple(
                {
                    "key": scan["key"],
                    "first_clean_t": scan["first_clean_t"],
                }
                for scan in new_transients
            ),
            "new_cycles": tuple(
                {
                    "key": scan["key"],
                    "entry_t": 0,
                    "period": scan["exact_return_t"],
                }
                for scan in target_cycles
            ),
            "remaining_open": len(still_open),
            "counts_by_stratum": target_counts,
            "unexpected_hash_repeats": unexpected_hash_repeats,
            "landed_cleanliness_test": (
                "source pointer + both banks' POINTER/U_TO_V/V_TO_U/"
                "DIRECTION_OK/FRESH/ZERO_WORK/TOKEN_OK + complete link"
            ),
        },
    )
    OUTPUT_LINES.append(
        "FINDING_ATTACK_2_VERBATIM "
        + compact({
            "statement": (
                "The independent T=8192 re-sweep of all 38 Cycle-798 "
                "T=2048-open keys finds no missed transient and no cycle "
                "beyond the six reported events; 10 k=3, 18 k=4, and all "
                "4 k=5 keys remain open."
            ),
            "counts_by_stratum": target_counts,
        })
    )

    catalog_identity_pass = (
        catalog["configuration_counts"] == EXPECTED_CONFIGURATION_COUNTS
        and catalog["family_counts"] == EXPECTED_FAMILY_COUNTS
        and catalog["class_counts"] == EXPECTED_CLASS_COUNTS
        and catalog["zero_counts"] == EXPECTED_ZERO_COUNTS
        and len(catalog["zero_rows"]) == 42
        and len(records) == 42
        and catalog["catalog_sha256"] == EXPECTED_CATALOG_SHA256
        and catalog["allocator_composition_exact"]
        and catalog["residual_equivalence_failures"] == 0
        and catalog["inverse_failures"] == 0
        and catalog["controller_failures"] == 0
        and catalog["zero_other_exclusion_failures"] == 0
        and catalog["all_initial_residuals_nonzero"]
    )
    identity_pass = (
        catalog_identity_pass
        and baseline_transient_moments
        == EXPECTED_T2048_TRANSIENT_MOMENTS
        and baseline_cycle_counts == EXPECTED_T2048_CYCLE_COUNTS
        and baseline_open_counts == EXPECTED_T2048_OPEN_COUNTS
        and len(open2048) == 38
    )
    check(
        "ATTACK_3_IDENTITY_CONTROLS_T2048_AND_CATALOG",
        identity_pass,
        {
            "configuration_counts": catalog["configuration_counts"],
            "family_counts": catalog["family_counts"],
            "class_counts": catalog["class_counts"],
            "zero_counts": catalog["zero_counts"],
            "zero_family_epoch_keys": len(catalog["zero_rows"]),
            "catalog_sha256": catalog["catalog_sha256"],
            "expected_catalog_sha256": EXPECTED_CATALOG_SHA256,
            "T2048_transient_moments": baseline_transient_moments,
            "T2048_cycle_counts": baseline_cycle_counts,
            "T2048_open_counts": baseline_open_counts,
            "T2048_open_key_sha256": digest(open2048),
            "controller_route_failures":
                catalog["controller_failures"],
            "inverse_failures": catalog["inverse_failures"],
            "LANDED_cleanliness_projection_disagreements":
                catalog["residual_equivalence_failures"],
        },
    )
    OUTPUT_LINES.append(
        "FINDING_ATTACK_3_VERBATIM "
        + compact({
            "statement": (
                "The independent identity reconstruction is exact: the "
                "Cycle-798 catalog has 18+20+4 zero-survivor keys, and at "
                "T=2048 the only higher-k clean moments are "
                "444/532/681/1385 in k=3, leaving 14+20+4 open and no "
                "certified cycle."
            ),
            "catalog_sha256": catalog["catalog_sha256"],
        })
    )

    # Declared deterministic slice: opposite ends of the sorted open-key set,
    # evolved twice from their immutable canonical postimages.
    slice_horizon = 257
    slice_keys = (open2048[0], open2048[-1])
    slice_rows = []
    deterministic_slice = True
    for key in slice_keys:
        first = scan_record(
            records[key],
            slice_horizon,
            first_tokens,
            second_tokens,
            residual,
        )
        second = scan_record(
            records[key],
            slice_horizon,
            first_tokens,
            second_tokens,
            residual,
        )
        first_digest = trace_digest(first)
        second_digest = trace_digest(second)
        same = first_digest == second_digest
        deterministic_slice = deterministic_slice and same
        slice_rows.append({
            "key": key,
            "horizon_t": slice_horizon,
            "first_sha256": first_digest,
            "second_sha256": second_digest,
            "same": same,
        })

    scan_summary_sha = digest(tuple(
        public_scan_fingerprint(scans[key]) for key in sorted(scans)
    ))
    checker_source = Path(__file__).read_text(encoding="utf-8")
    checker_tree = ast.parse(checker_source, filename=__file__)
    called_functions = {
        ast.unparse(node.func)
        for node in ast.walk(checker_tree)
        if isinstance(node, ast.Call)
    }
    forbidden_landed_evolution_calls = tuple(sorted(
        {"K.A.apply_semantic", "K.run_orbit"} & called_functions
    ))
    no_landed_evolution_call = (
        not forbidden_landed_evolution_calls
    )
    primary_modules_still_absent = all(
        module not in sys.modules for module in PRIMARY_MODULE_NAMES
    )
    elapsed = monotonic() - started
    projected_stdout_bytes = (
        len("\n".join(OUTPUT_LINES).encode("utf-8")) + 24 * 1024
    )
    attack_4_pass = (
        anchors["pass"]
        and anchors["no_primary_import_syntax"]
        and anchors["primary_modules_absent"]
        and primary_modules_still_absent
        and no_landed_evolution_call
        and deterministic_slice
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES
    )
    check(
        "ATTACK_4_ANCHORS_BLOCKLIST_DETERMINISM_AND_BOUNDS",
        attack_4_pass,
        {
            "anchors": anchors,
            "cycle798_cycle801_TEXT_ONLY_BLOCKLISTED": (
                anchors["no_primary_import_syntax"]
                and anchors["primary_modules_absent"]
                and primary_modules_still_absent
            ),
            "own_evolution_no_K_apply_or_run_orbit":
                no_landed_evolution_call,
            "forbidden_landed_evolution_calls":
                forbidden_landed_evolution_calls,
            "determinism_declared_slice": slice_rows,
            "full_scan_summary_sha256": scan_summary_sha,
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "projected_stdout_bytes": projected_stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )
    OUTPUT_LINES.append(
        "FINDING_ATTACK_4_VERBATIM "
        + compact({
            "statement": (
                "All SHA/blob anchors match; Cycles 798 and 801 remained "
                "text-only blocklisted; the declared two-key T=257 slice "
                "replayed byte-for-byte; runtime and stdout stayed bounded."
            ),
            "runtime_seconds": round(elapsed, 6),
        })
    )

    passed = all(CHECKS.values())
    terminal = {
        "terminal": (
            "CYCLE801_DEEP_SCAN_INDEPENDENT_CHECK_PASS"
            if passed
            else "CYCLE801_DEEP_SCAN_INDEPENDENT_CHECK_HONEST_FAIL"
        ),
        "pass": passed,
        "six_cycles": tuple(
            {
                "key": row["key"],
                "entry_t": row["entry_t"],
                "period": row["period"],
                "forever_nonzero":
                    row["residual_nonzero_on_complete_period"],
            }
            for row in cycle_certificate_rows
        ),
        "missed_transient_count": len(new_transients),
        "additional_cycle_count":
            max(0, len(target_cycles) - 6),
        "remaining_open_by_stratum": {
            k: target_counts[k]["open"] for k in TARGET_STRATA
        },
        "catalog_sha256": catalog["catalog_sha256"],
        "full_scan_summary_sha256": scan_summary_sha,
        "runtime_seconds": round(elapsed, 6),
    }
    output = (
        "\n".join(OUTPUT_LINES)
        + "\nFINAL "
        + compact(terminal)
        + "\n"
    )
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", output_bytes))
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
