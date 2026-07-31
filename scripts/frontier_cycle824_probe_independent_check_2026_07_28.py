#!/usr/bin/env python3
"""Cycle 824 independent adversarial checker for the phase-identity claim.

The Cycle-824 and Cycle-820 primaries are SHA-pinned text/AST references only.
They are import-firewalled.  The sole executable repository input is the
landed Cycle-719 controller core, while every repeated-state evolution below
uses this checker's own Boolean X/CNOT/Toffoli interpreter.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle820_shared_moment_mechanism_2026_07_28.py",
    "scripts/frontier_cycle824_k3_merger_probe_2026_07_28.py",
)

import ast
import gc
from hashlib import sha1, sha256
import importlib.abc
import inspect
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

REFERENCE_PRIMARY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in REFERENCE_PRIMARY_PATHS
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "7344bee5d5f0bcbddcea7b9d83f40a552c90188bf30b4905f2649a49e4bf1649",
    AUDIT_INPUT_PATHS[2]:
        "b279582fb8deab4b8713c08353a3c6f3f1239135f1d0f666bdc6b35fe3b99223",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "6385dfa0dce58e86345483cc521ffa325e0d1cce",
    AUDIT_INPUT_PATHS[2]: "423992108cbe1f2d8ce57e2f1618e85c14ac0a2c",
}
REQUIRED_PRIMARY_FUNCTIONS = {
    AUDIT_INPUT_PATHS[1]: {
        "evolve_nine",
        "mechanism_candidates",
        "population_state_at_entry",
        "synchronous_word",
    },
    AUDIT_INPUT_PATHS[2]: {
        "cycle_certificate",
        "k2_sstar",
        "transient_certificate",
        "cross_stratum_certificate",
    },
}


class _PrimaryBlocklist(importlib.abc.MetaPathFinder):
    """Fail closed if either reference primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


IMPORT_FIREWALL = _PrimaryBlocklist()
sys.meta_path.insert(0, IMPORT_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_WIDTH = 5815
K3_PERIOD = 5952
PHASE_CHECKPOINT_SPEC = {
    "start": 0,
    "stop_inclusive": K3_PERIOD,
    "stride": 1,
}
K3_CYCLE_KEYS = (
    (3, (0, 2, 5), 1),
    (3, (0, 2, 6), 1),
    (3, (0, 2, 7), 1),
    (3, (0, 2, 8), 1),
)
EXPECTED_TRANSIENT_MOMENTS = (444, 532, 681, 1385)
TRANSIENT_SCAN_END = max(EXPECTED_TRANSIENT_MOMENTS)
SSTAR_KEY = (2, (1, 6), 0)
SSTAR_TIME = 14739
LAG_RADIUS = 8

Key = tuple[int, tuple[int, ...], int]
Operation = tuple[int, int, int, int]
CompiledWord = tuple[Operation, ...]
ExactState = bytes


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def state_digest(state: ExactState | bytearray | tuple[int, ...]) -> str:
    return sha256(bytes(state)).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            values.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            values.append(node.value)
    if len(values) != 1:
        return None
    try:
        return ast.literal_eval(values[0])
    except (TypeError, ValueError):
        return None


def source_certificate() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if (ROOT / path).is_file()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    actual_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    actual_blobs = {
        path: git_blob_sha(payload)
        for path, payload in payloads.items()
    }
    reference_rows = {}
    for path in REFERENCE_PRIMARY_PATHS:
        functions = {
            node.name
            for node in trees[path].body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        reference_rows[path] = {
            "mode": "TEXT_AST_ONLY_BLOCKLISTED",
            "required_functions":
                tuple(sorted(REQUIRED_PRIMARY_FUNCTIONS[path])),
            "required_functions_present":
                REQUIRED_PRIMARY_FUNCTIONS[path] <= functions,
        }

    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    direct_frontier_imports = {
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    }
    lineage_literals = {
        "cycle820_MECHANISM_ENTRY":
            literal_assignment(trees[AUDIT_INPUT_PATHS[1]], "MECHANISM_ENTRY"),
        "cycle820_FIXTURE_BANKS":
            literal_assignment(trees[AUDIT_INPUT_PATHS[1]], "FIXTURE_BANKS"),
        "cycle820_NINE_KEYS":
            literal_assignment(trees[AUDIT_INPUT_PATHS[1]], "NINE_KEYS"),
        "cycle824_K3_CYCLE_KEYS":
            literal_assignment(trees[AUDIT_INPUT_PATHS[2]], "K3_CYCLE_KEYS"),
        "cycle824_K3_CYCLE_PERIOD":
            literal_assignment(trees[AUDIT_INPUT_PATHS[2]], "K3_CYCLE_PERIOD"),
        "cycle824_K2_SSTAR_KEY":
            literal_assignment(trees[AUDIT_INPUT_PATHS[2]], "K2_SSTAR_KEY"),
        "cycle824_K2_SSTAR_TIME":
            literal_assignment(trees[AUDIT_INPUT_PATHS[2]], "K2_SSTAR_TIME"),
    }
    nine_keys = lineage_literals["cycle820_NINE_KEYS"]
    lineage_exact = (
        lineage_literals["cycle820_MECHANISM_ENTRY"] == SSTAR_TIME
        and lineage_literals["cycle820_FIXTURE_BANKS"] == FIXTURE_BANKS
        and isinstance(nine_keys, tuple)
        and (0, (1, 6)) in nine_keys
        and lineage_literals["cycle824_K3_CYCLE_KEYS"] == K3_CYCLE_KEYS
        and lineage_literals["cycle824_K3_CYCLE_PERIOD"] == K3_PERIOD
        and lineage_literals["cycle824_K2_SSTAR_KEY"] == SSTAR_KEY
        and lineage_literals["cycle824_K2_SSTAR_TIME"] == SSTAR_TIME
    )
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "named_file_count": len(AUDIT_INPUT_PATHS),
        "named_file_limit": 6,
        "existing_worktree_relative": (
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(
                not Path(path).is_absolute()
                and (ROOT / path).is_file()
                for path in AUDIT_INPUT_PATHS
            )
        ),
        "sha256": actual_sha,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": actual_blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "reference_AST": reference_rows,
        "lineage_literals": lineage_literals,
        "lineage_literals_exact": lineage_exact,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(IMPORT_FIREWALL.hits),
        "direct_frontier_imports": tuple(sorted(direct_frontier_imports)),
        "execution_policy":
            "stdlib plus sole landed Cycle-719 core; Cycle-820/824 text/AST only",
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["named_file_count"] <= result["named_file_limit"]
        and result["existing_worktree_relative"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and all(
            row["required_functions_present"]
            for row in reference_rows.values()
        )
        and lineage_exact
        and direct_frontier_imports
        == {
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
        }
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


def compile_word(word: tuple[object, ...]) -> CompiledWord:
    operations = []
    for gate in word:
        kind = str(gate.kind)
        wires = tuple(int(wire) for wire in gate.wires)
        if kind == "X" and len(wires) == 1:
            operations.append((0, wires[0], 0, 0))
        elif kind == "CNOT" and len(wires) == 2:
            operations.append((1, wires[0], wires[1], 0))
        elif kind == "TOF" and len(wires) == 3:
            operations.append((2, wires[0], wires[1], wires[2]))
        else:
            raise AssertionError(("unsupported exact gate", kind, wires))
    return tuple(operations)


def apply_scalar(state: bytearray, operations: CompiledWord) -> None:
    """Apply one word in place, independently of the core semantic engine."""
    for kind, first, second, third in operations:
        if kind == 0:
            state[first] ^= 1
        elif kind == 1:
            state[second] ^= state[first]
        else:
            state[third] ^= state[first] & state[second]


def slice_states(states: tuple[tuple[int, ...] | ExactState, ...]) -> list[int]:
    if not states or len({len(state) for state in states}) != 1:
        raise AssertionError("bit-slice states require one nonempty width")
    return [
        sum(int(state[wire]) << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def apply_sliced(
    columns: list[int],
    operations: CompiledWord,
    lane_mask: int,
) -> None:
    """Apply one common word to selected bit-sliced lanes."""
    for kind, first, second, third in operations:
        if kind == 0:
            columns[first] ^= lane_mask
        elif kind == 1:
            columns[second] ^= columns[first] & lane_mask
        else:
            columns[third] ^= (
                columns[first] & columns[second] & lane_mask
            )


def lane_state(columns: list[int], lane: int) -> ExactState:
    mask = 1 << lane
    return bytes(bool(column & mask) for column in columns)


def synchronous_word(
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> tuple[object, ...]:
    """Compose one orbit directly from moving token positions."""
    positions = tuple(token_positions)
    word = []
    for _step in range(len(program)):
        live = frozenset(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    return tuple(word)


def build_fixtures(
) -> tuple[
    tuple[object, ...],
    tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
]:
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = bytearray(K.M.pack_state(banks, links))
    allocator = compile_word(K.M.global_allocator_word(FIXTURE_BANKS))
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = tuple(K.M.prepare_endpoint(tuple(state), direction))
        rows.append((event, direction, before))
        state = bytearray(before)
        apply_scalar(state, allocator)
    return program, tuple(rows)


def separated(positions: tuple[int, ...]) -> bool:
    occupied = frozenset(positions)
    return all(
        (position + 1) % RING_STATIONS not in occupied
        for position in occupied
    )


def rotate(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(sorted(
        (position + shift) % RING_STATIONS for position in positions
    ))


def k3_families(
) -> dict[tuple[int, ...], tuple[tuple[int, ...], ...]]:
    grouped: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
    for mask in range(1 << RING_STATIONS):
        positions = tuple(
            station
            for station in range(RING_STATIONS)
            if mask & (1 << station)
        )
        if len(positions) == 3 and separated(positions):
            representative = min(
                rotate(positions, shift)
                for shift in range(RING_STATIONS)
            )
            grouped.setdefault(representative, set()).add(positions)
    return {
        representative: tuple(sorted(alternatives))
        for representative, alternatives in sorted(grouped.items())
    }


def changed_coordinate(
    baseline: tuple[int, ...], changed: tuple[int, ...]
) -> int:
    differences = tuple(
        index
        for index, (left, right) in enumerate(zip(baseline, changed))
        if left != right
    )
    if len(baseline) != len(changed) or len(differences) != 1:
        raise AssertionError(("coordinate audit failed", len(differences)))
    return differences[0]


def watched_coordinates() -> tuple[int, ...]:
    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    baseline = K.M.pack_state(banks0, links0)
    indices = {int(K.R3.X.SOURCE_POINTER)}
    registers = (
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        K.A.DIRECTION_OK,
        *K.A.FRESH,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )
    for bank_index in range(FIXTURE_BANKS):
        for wire in registers:
            banks = [list(bank) for bank in banks0]
            links = [list(link) for link in links0]
            banks[bank_index][wire] ^= 1
            changed = K.M.pack_state(
                tuple(tuple(bank) for bank in banks),
                tuple(tuple(link) for link in links),
            )
            indices.add(changed_coordinate(baseline, changed))
    for link_index, link in enumerate(links0):
        for wire in range(len(link)):
            banks = [list(bank) for bank in banks0]
            links = [list(item) for item in links0]
            links[link_index][wire] ^= 1
            changed = K.M.pack_state(
                tuple(tuple(bank) for bank in banks),
                tuple(tuple(item) for item in links),
            )
            indices.add(changed_coordinate(baseline, changed))
    return tuple(sorted(indices))


def clean_lane(
    columns: list[int],
    lane: int,
    watched: tuple[int, ...],
) -> bool:
    mask = 1 << lane
    return not any(columns[index] & mask for index in watched)


def clean_state(
    state: ExactState | bytearray | tuple[int, ...],
    watched: tuple[int, ...],
) -> bool:
    return not any(state[index] for index in watched)


def derive_transient_catalog(
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    watched: tuple[int, ...],
) -> tuple[
    dict[str, object],
    tuple[Key, ...],
    dict[tuple[int, ...], CompiledWord],
]:
    families = k3_families()
    representatives = tuple(families)
    fixture_states = tuple(row[2] for row in fixtures)
    operations_by_positions = {}
    all_operations = {
        positions: compile_word(synchronous_word(program, positions))
        for alternatives in families.values()
        for positions in alternatives
    }
    zero_rows = set()
    for representative, alternatives in families.items():
        for event, before in enumerate(fixture_states):
            alternative_cleanliness = []
            for positions in alternatives:
                state = bytearray(before)
                apply_scalar(state, all_operations[positions])
                alternative_cleanliness.append(
                    clean_state(state, watched)
                )
            if not any(alternative_cleanliness):
                zero_rows.add((3, representative, event))
    first_clean: dict[Key, int | None] = {}
    for positions in representatives:
        operations = all_operations[positions]
        operations_by_positions[positions] = operations
        initial_states = []
        for before in fixture_states:
            state = bytearray(before)
            apply_scalar(state, operations)
            initial_states.append(bytes(state))
        columns = slice_states(tuple(initial_states))
        unresolved = set(range(len(fixture_states)))
        for horizon_t in range(TRANSIENT_SCAN_END + 1):
            for lane in tuple(unresolved):
                if clean_lane(columns, lane, watched):
                    first_clean[(3, positions, lane)] = horizon_t
                    unresolved.remove(lane)
            if horizon_t < TRANSIENT_SCAN_END:
                apply_sliced(
                    columns,
                    operations,
                    (1 << len(fixture_states)) - 1,
                )
        for lane in unresolved:
            first_clean[(3, positions, lane)] = None

    positive = tuple(sorted(
        (
            (key, moment)
            for key, moment in first_clean.items()
            if (
                key in zero_rows
                and moment is not None
                and moment > 0
            )
        ),
        key=lambda row: (row[1], row[0]),
    ))
    selected_keys = tuple(key for key, _moment in positive)
    moments = tuple(moment for _key, moment in positive)
    result = {
        "k3_representatives": representatives,
        "representative_count": len(representatives),
        "configuration_count": sum(
            len(alternatives) for alternatives in families.values()
        ),
        "zero_row_count": len(zero_rows),
        "zero_rows": tuple(sorted(zero_rows)),
        "scanned_key_count": len(first_clean),
        "scan_domain": (0, TRANSIENT_SCAN_END),
        "positive_first_clean_rows": positive,
        "positive_first_clean_count": len(positive),
        "expected_moments": EXPECTED_TRANSIENT_MOMENTS,
        "pass": (
            len(representatives) == 7
            and sum(
                len(alternatives) for alternatives in families.values()
            ) == 77
            and len(zero_rows) == 18
            and len(first_clean) == 28
            and len(positive) == 4
            and moments == EXPECTED_TRANSIENT_MOMENTS
        ),
    }
    return result, selected_keys, operations_by_positions


def capture_transients(
    keys: tuple[Key, ...],
    moments: dict[Key, int],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    operations_by_positions: dict[tuple[int, ...], CompiledWord],
    watched: tuple[int, ...],
) -> tuple[dict[Key, tuple[ExactState, ...]], dict[str, object]]:
    fixture_by_event = {event: before for event, _direction, before in fixtures}
    trajectories = {}
    identity_rows = []
    for key in keys:
        _k, positions, event = key
        operations = operations_by_positions[positions]
        state = bytearray(fixture_by_event[event])
        apply_scalar(state, operations)
        rows = []
        clean_times = []
        for horizon_t in range(moments[key] + 1):
            exact = bytes(state)
            rows.append(exact)
            if clean_state(exact, watched):
                clean_times.append(horizon_t)
            if horizon_t < moments[key]:
                apply_scalar(state, operations)
        trajectories[key] = tuple(rows)
        identity_rows.append({
            "key": key,
            "expected_first_clean": moments[key],
            "clean_times_through_first": tuple(clean_times),
            "initial_state_sha256_label_only": state_digest(rows[0]),
            "terminal_state_sha256_label_only": state_digest(rows[-1]),
        })
    result = {
        "trajectory_domains": tuple(
            (key, (0, len(trajectories[key]) - 1)) for key in keys
        ),
        "identity_rows": tuple(identity_rows),
        "trajectory_sha256": digest(tuple(
            (
                key,
                tuple(state_digest(state) for state in trajectories[key]),
            )
            for key in keys
        )),
        "pass": all(
            row["clean_times_through_first"]
            == (row["expected_first_clean"],)
            for row in identity_rows
        ),
    }
    return trajectories, result


def no_coincidence_certificate(
    keys: tuple[Key, ...],
    trajectories: dict[Key, tuple[ExactState, ...]],
) -> dict[str, object]:
    rows = []
    collision_rows = []
    signed_lags = tuple(range(-LAG_RADIUS, LAG_RADIUS + 1))
    for left_index, right_index in combinations(range(len(keys)), 2):
        left_key = keys[left_index]
        right_key = keys[right_index]
        left = trajectories[left_key]
        right = trajectories[right_key]
        for signed_lag in signed_lags:
            start = max(0, -signed_lag)
            stop = min(len(left), len(right) - signed_lag)
            exact_times = tuple(
                horizon_t
                for horizon_t in range(start, max(start, stop))
                if left[horizon_t] == right[horizon_t + signed_lag]
            )
            row = {
                "key_indices": (left_index, right_index),
                "signed_lag": signed_lag,
                "definition":
                    "state_left(t) == state_right(t + signed_lag)",
                "left_time_domain": (
                    (start, stop - 1) if stop > start else None
                ),
                "exact_full_state_equality_times": exact_times,
            }
            rows.append(row)
            if exact_times:
                collision_rows.append(row)
    passed = (
        len(keys) == 4
        and len(rows) == 6 * len(signed_lags)
        and not collision_rows
    )
    finding = (
        "PASS: the independently rebuilt four k=3 transient trajectories "
        "have no exact 5815-bit cross-key state equality at same time or "
        "at any signed lag 1..8 over every overlapping trajectory domain."
        if passed else
        "FAIL: at least one exact 5815-bit cross-key transient state "
        "equality occurs at same time or signed lag 1..8; see collision_rows."
    )
    return {
        "status": "PASS" if passed else "FAIL",
        "finding": finding,
        "key_index": tuple(enumerate(keys)),
        "lag_definition":
            "all signed lags -8..8; lag 0 is same-time equality",
        "comparison_row_count": len(rows),
        "collision_rows": tuple(collision_rows),
        "map_sha256": digest(tuple(rows)),
        "pass": passed,
    }


def first_operation_difference(
    left: CompiledWord, right: CompiledWord
) -> dict[str, object]:
    for index, (left_operation, right_operation) in enumerate(
        zip(left, right)
    ):
        if left_operation != right_operation:
            return {
                "operation_index": index,
                "left_operation": left_operation,
                "right_operation": right_operation,
            }
    if len(left) != len(right):
        return {
            "operation_index": min(len(left), len(right)),
            "left_operation":
                left[min(len(left), len(right))]
                if len(left) > len(right) else None,
            "right_operation":
                right[min(len(left), len(right))]
                if len(right) > len(left) else None,
        }
    return {
        "operation_index": None,
        "left_operation": None,
        "right_operation": None,
    }


def compute_sstar(
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
) -> tuple[ExactState, dict[str, object]]:
    _k, positions, event = SSTAR_KEY
    before = next(
        state
        for fixture_event, _direction, state in fixtures
        if fixture_event == event
    )
    operations = compile_word(synchronous_word(program, positions))
    state = bytearray(before)
    apply_scalar(state, operations)
    for _horizon_t in range(SSTAR_TIME):
        apply_scalar(state, operations)
    exact = bytes(state)
    result = {
        "lineage_key": SSTAR_KEY,
        "lineage_time": SSTAR_TIME,
        "word_gate_count": len(operations),
        "state_width": len(exact),
        "binary_encoding": set(exact) <= {0, 1},
        "state_sha256_label_only": state_digest(exact),
        "pass": len(exact) == STATE_WIDTH and set(exact) <= {0, 1},
    }
    return exact, result


def phase_identity_certificate(
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    sstar: ExactState,
) -> tuple[dict[str, object], tuple[tuple[Key, tuple[int, ...]], ...]]:
    fixture_by_event = {event: before for event, _direction, before in fixtures}
    words = {}
    operations = {}
    states = []
    initial_states = []
    rail_inputs = []
    for key in K3_CYCLE_KEYS:
        _k, positions, event = key
        word = synchronous_word(program, positions)
        compiled = compile_word(word)
        state = bytearray(fixture_by_event[event])
        apply_scalar(state, compiled)
        words[key] = word
        operations[key] = compiled
        states.append(state)
        initial_states.append(bytes(state))
        rail_inputs.append((
            tuple(int(station in positions) for station in range(len(program))),
            (0,) * len(program),
        ))

    pairwise_input_rows = []
    for left_index, right_index in combinations(
        range(len(K3_CYCLE_KEYS)), 2
    ):
        left_key = K3_CYCLE_KEYS[left_index]
        right_key = K3_CYCLE_KEYS[right_index]
        left_operations = operations[left_key]
        right_operations = operations[right_key]
        pairwise_input_rows.append({
            "key_indices": (left_index, right_index),
            "keys_exactly_distinct": left_key != right_key,
            "token_positions_distinct": left_key[1] != right_key[1],
            "rail_inputs_exactly_distinct":
                rail_inputs[left_index] != rail_inputs[right_index],
            "compiled_words_exactly_distinct":
                left_operations != right_operations,
            "first_compiled_operation_difference":
                first_operation_difference(
                    left_operations, right_operations
                ),
        })

    mismatch_times = []
    return_times = []
    cycle_visit_rows = [[] for _key in K3_CYCLE_KEYS]
    first_orbit_states: set[ExactState] = set()
    sampled_times = {
        0, 1, 2, 7, 31, 127, 511, 1023, 2047, 4095,
        K3_PERIOD - 1, K3_PERIOD,
    }
    samples = []
    trajectory_hasher = sha256()
    for horizon_t in range(
        PHASE_CHECKPOINT_SPEC["start"],
        PHASE_CHECKPOINT_SPEC["stop_inclusive"] + 1,
        PHASE_CHECKPOINT_SPEC["stride"],
    ):
        exact_states = tuple(bytes(state) for state in states)
        if not all(
            state == exact_states[0] for state in exact_states[1:]
        ):
            mismatch_times.append(horizon_t)
        if horizon_t > 0 and exact_states[0] == initial_states[0]:
            return_times.append(horizon_t)
        if horizon_t < K3_PERIOD:
            first_orbit_states.add(exact_states[0])
            for index, state in enumerate(exact_states):
                if state == sstar:
                    cycle_visit_rows[index].append(horizon_t)
        if horizon_t in sampled_times:
            samples.append({
                "time": horizon_t,
                "state_sha256_labels_only":
                    tuple(state_digest(state) for state in exact_states),
                "exact_all_four_equal":
                    all(
                        state == exact_states[0]
                        for state in exact_states[1:]
                    ),
            })
        trajectory_hasher.update(horizon_t.to_bytes(4, "little"))
        for state in exact_states:
            trajectory_hasher.update(state)
        if horizon_t < K3_PERIOD:
            for index, key in enumerate(K3_CYCLE_KEYS):
                apply_scalar(states[index], operations[key])

    word_hashes = tuple(
        digest(operations[key]) for key in K3_CYCLE_KEYS
    )
    checkpoint_count = (
        (
            PHASE_CHECKPOINT_SPEC["stop_inclusive"]
            - PHASE_CHECKPOINT_SPEC["start"]
        ) // PHASE_CHECKPOINT_SPEC["stride"]
        + 1
    )
    keys_distinct = len(set(K3_CYCLE_KEYS)) == len(K3_CYCLE_KEYS)
    inputs_distinct = (
        len(set(rail_inputs)) == len(K3_CYCLE_KEYS)
        and len(set(operations.values())) == len(K3_CYCLE_KEYS)
        and all(
            row["keys_exactly_distinct"]
            and row["token_positions_distinct"]
            and row["rail_inputs_exactly_distinct"]
            and row["compiled_words_exactly_distinct"]
            and row["first_compiled_operation_difference"][
                "operation_index"
            ] is not None
            for row in pairwise_input_rows
        )
    )
    exact_period = (
        tuple(return_times) == (K3_PERIOD,)
        and len(first_orbit_states) == K3_PERIOD
        and bytes(states[0]) == initial_states[0]
    )
    passed = (
        keys_distinct
        and inputs_distinct
        and len(set(initial_states)) == 1
        and checkpoint_count == K3_PERIOD + 1
        and not mismatch_times
        and exact_period
    )
    finding = (
        "PASS: all four distinct k=3 keys have exact 5815-bit state "
        "equality at phase offset 0 at every declared checkpoint "
        "t=0..5952 inclusive; their distinct token-position rails and "
        "distinct fixed words are controller inputs external to the packed "
        "data-state coordinates."
        if passed else
        "FAIL: the four claimed k=3 cycle keys are not exact phase-offset-0 "
        "copies over the declared full-period checkpoint set; see mismatches "
        "or state-object controls."
    )
    result = {
        "status": "PASS" if passed else "FAIL",
        "finding": finding,
        "key_index": tuple(enumerate(K3_CYCLE_KEYS)),
        "keys_exactly_distinct": keys_distinct,
        "checkpoint_declaration": PHASE_CHECKPOINT_SPEC,
        "checkpoint_count": checkpoint_count,
        "checkpoint_set_sha256": digest(tuple(range(K3_PERIOD + 1))),
        "offset_definition":
            "state_i(t) == state_j((t+offset) mod 5952); tested offset=0",
        "offset_zero_mismatch_count": len(mismatch_times),
        "offset_zero_mismatch_times": tuple(mismatch_times),
        "full_period_controls": {
            "exact_return_times_through_5952": tuple(return_times),
            "unique_exact_states_t0_through_t5951":
                len(first_orbit_states),
            "closure_exact": bytes(states[0]) == initial_states[0],
            "unique_compatible_phase_offsets": (0,) if exact_period else None,
        },
        "state_object_audit": {
            "what_differs_in_inputs":
                "the four key tuples, token-position rail vectors, and "
                "compiled fixed words are pairwise distinct",
            "where_key_identity_does_not_live":
                "K.M.pack_state encodes banks and links only; controller "
                "rail vectors are supplied to run_orbit separately and are "
                "not appended to the 5815 packed data coordinates",
            "packed_data_width": STATE_WIDTH,
            "controller_rail_width_if_augmented": 2 * len(program),
            "packed_postimages_exactly_equal":
                len(set(initial_states)) == 1,
            "rail_inputs": tuple(rail_inputs),
            "compiled_word_gate_counts": tuple(
                len(operations[key]) for key in K3_CYCLE_KEYS
            ),
            "compiled_word_sha256_labels_only": word_hashes,
            "pairwise_distinct_input_rows": tuple(pairwise_input_rows),
        },
        "sampled_checkpoint_labels": tuple(samples),
        "trajectory_sha256_label_only": trajectory_hasher.hexdigest(),
        "pass": passed,
    }
    visits = tuple(
        (key, tuple(times))
        for key, times in zip(K3_CYCLE_KEYS, cycle_visit_rows)
    )
    return result, visits


def sstar_visit_certificate(
    sstar: ExactState,
    sstar_control: dict[str, object],
    transient_keys: tuple[Key, ...],
    transient_trajectories: dict[Key, tuple[ExactState, ...]],
    cycle_visits: tuple[tuple[Key, tuple[int, ...]], ...],
) -> dict[str, object]:
    transient_visits = tuple(
        (
            key,
            tuple(
                horizon_t
                for horizon_t, state in enumerate(
                    transient_trajectories[key]
                )
                if state == sstar
            ),
        )
        for key in transient_keys
    )
    exact_visit_count = sum(
        len(times)
        for _key, times in transient_visits + cycle_visits
    )
    passed = (
        sstar_control["pass"]
        and len(transient_visits) == 4
        and len(cycle_visits) == 4
        and exact_visit_count == 0
    )
    finding = (
        "PASS: the Cycle-820-lineage S* state was independently rebuilt at "
        "k=2 time 14739 and has zero exact 5815-bit visits across all four "
        "complete k=3 transient scopes and all four full 5952-cycle periods."
        if passed else
        "FAIL: the independently rebuilt Cycle-820-lineage S* has at least "
        "one exact visit in a scoped k=3 transient or 5952-cycle trajectory, "
        "or its lineage reconstruction failed."
    )
    return {
        "status": "PASS" if passed else "FAIL",
        "finding": finding,
        "Sstar": sstar_control,
        "comparison_rule":
            "exact bytes equality over all 5815 binary coordinates; SHA256 "
            "is printed only as a label",
        "transient_exact_visits": transient_visits,
        "cycle_exact_visits_one_complete_period": cycle_visits,
        "exact_visit_count": exact_visit_count,
        "pass": passed,
    }


def relative_definition(code: Any) -> str:
    path = Path(code.co_filename).resolve()
    try:
        relative = path.relative_to(ROOT)
    except ValueError:
        relative = path
    return f"{relative}:{code.co_firstlineno}"


def state_space_certificate(
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    sstar: ExactState,
    transient_keys: tuple[Key, ...],
    transient_trajectories: dict[Key, tuple[ExactState, ...]],
) -> dict[str, object]:
    fixture_by_event = {event: before for event, _direction, before in fixtures}
    k3_key = K3_CYCLE_KEYS[0]
    _k3, k3_positions, k3_event = k3_key
    k3_operations = compile_word(
        synchronous_word(program, k3_positions)
    )
    k3_initial = bytearray(fixture_by_event[k3_event])
    apply_scalar(k3_initial, k3_operations)
    k3_exact = bytes(k3_initial)
    transient_exact = transient_trajectories[transient_keys[0]][0]

    def roundtrip(state: ExactState) -> bool:
        banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
        matter = sum(int(state[wire]) << wire for wire in range(12))
        pointer = int(state[K.R3.X.SOURCE_POINTER])
        return bytes(
            K.M.pack_state(
                banks,
                links,
                matter=matter,
                pointer=pointer,
            )
        ) == state

    pack_code = K.M.pack_state.__code__
    unpack_code = K.M.unpack_state.__code__
    orbit_code = K.run_orbit.__code__
    widths = {
        len(sstar),
        len(k3_exact),
        len(transient_exact),
        *(len(before) for before in fixture_by_event.values()),
    }
    binary = all(
        set(state) <= {0, 1}
        for state in (sstar, k3_exact, transient_exact)
    )
    same_runtime_objects = (
        K.M.pack_state is sys.modules[
            K.M.pack_state.__module__
        ].pack_state
        and K.M.unpack_state is sys.modules[
            K.M.unpack_state.__module__
        ].unpack_state
    )
    passed = (
        widths == {STATE_WIDTH}
        and binary
        and roundtrip(sstar)
        and roundtrip(k3_exact)
        and roundtrip(transient_exact)
        and same_runtime_objects
        and "token_positions" not in inspect.signature(
            K.M.pack_state
        ).parameters
        and "token_positions" in inspect.signature(
            K.run_orbit
        ).parameters
    )
    finding = (
        "PASS: k=2 and k=3 use the identical K.M.pack_state/unpack_state "
        "object, bank_count=2 layout, 5815-coordinate binary encoding, and "
        "exact round trip; k only selects an external fixed word, so exact "
        "S* comparison needs no projection."
        if passed else
        "FAIL: k=2 and k=3 were not certified as the same packed 5815-bit "
        "state object and encoding; an exact S* visit claim is not comparable."
    )
    return {
        "status": "PASS" if passed else "FAIL",
        "finding": finding,
        "dimensions": {
            "k2_fixture_banks": FIXTURE_BANKS,
            "k3_fixture_banks": FIXTURE_BANKS,
            "observed_widths": tuple(sorted(widths)),
            "expected_width": STATE_WIDTH,
        },
        "encodings": {
            "normalized_exact_type": "bytes",
            "coordinate_alphabet": (0, 1),
            "all_samples_binary": binary,
            "k2_roundtrip_exact": roundtrip(sstar),
            "k3_cycle_roundtrip_exact": roundtrip(k3_exact),
            "k3_transient_roundtrip_exact": roundtrip(transient_exact),
            "projection_required": False,
            "global_coordinate_preservation":
                "pack_state matter reconstructs coordinates 0..11 and "
                "pointer reconstructs K.R3.X.SOURCE_POINTER; unpack_state "
                "returns the bank/link blocks",
        },
        "module_definition_citations": {
            "pack_state": {
                "callable_module": K.M.pack_state.__module__,
                "definition": relative_definition(pack_code),
                "signature": str(inspect.signature(K.M.pack_state)),
            },
            "unpack_state": {
                "callable_module": K.M.unpack_state.__module__,
                "definition": relative_definition(unpack_code),
                "signature": str(inspect.signature(K.M.unpack_state)),
            },
            "controller_run_orbit": {
                "callable_module": K.run_orbit.__module__,
                "definition": relative_definition(orbit_code),
                "signature": str(inspect.signature(K.run_orbit)),
                "relevance":
                    "token_positions is a controller argument; returned data "
                    "and the two rail vectors are separate objects",
            },
        },
        "same_pack_unpack_runtime_objects": same_runtime_objects,
        "reason_exact_cross_stratum_equality_is_meaningful":
            "both strata are elements of the same {0,1}^5815 encoding",
        "pass": passed,
    }


def engine_control(
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    operations: CompiledWord,
) -> dict[str, object]:
    initial = tuple(row[2] for row in fixtures)
    scalar = []
    for state0 in initial:
        state = bytearray(state0)
        apply_scalar(state, operations)
        scalar.append(bytes(state))
    columns = slice_states(initial)
    apply_sliced(columns, operations, (1 << len(initial)) - 1)
    sliced = tuple(
        lane_state(columns, lane) for lane in range(len(initial))
    )
    exact = tuple(scalar) == sliced
    return {
        "scope":
            "one full k=3 fixed word across all four fixture events",
        "scalar_vs_bit_sliced_exact_full_state_equality": exact,
        "state_widths": tuple(len(state) for state in sliced),
        "pass": exact and set(map(len, sliced)) == {STATE_WIDTH},
    }


def run_science() -> dict[str, object]:
    program, fixtures = build_fixtures()
    watched = watched_coordinates()
    catalog, transient_keys, operations_by_positions = (
        derive_transient_catalog(program, fixtures, watched)
    )
    moments = dict(catalog["positive_first_clean_rows"])
    transient_trajectories, transient_identity = capture_transients(
        transient_keys,
        moments,
        fixtures,
        operations_by_positions,
        watched,
    )
    no_coincidence = no_coincidence_certificate(
        transient_keys, transient_trajectories
    )
    sstar, sstar_control = compute_sstar(program, fixtures)
    phase_identity, cycle_visits = phase_identity_certificate(
        program, fixtures, sstar
    )
    sstar_visits = sstar_visit_certificate(
        sstar,
        sstar_control,
        transient_keys,
        transient_trajectories,
        cycle_visits,
    )
    state_space = state_space_certificate(
        program,
        fixtures,
        sstar,
        transient_keys,
        transient_trajectories,
    )
    engine = engine_control(
        fixtures,
        operations_by_positions[transient_keys[0][1]],
    )
    reconstruction = {
        "watched_coordinate_count": len(watched),
        "expected_watched_coordinate_count": 477,
        "fixture_count": len(fixtures),
        "program_station_count": len(program),
        "catalog": catalog,
        "transient_identity": transient_identity,
        "engine": engine,
    }
    reconstruction["pass"] = (
        len(watched) == 477
        and len(fixtures) == 4
        and len(program) == RING_STATIONS
        and catalog["pass"]
        and transient_identity["pass"]
        and engine["pass"]
    )
    return {
        "phase_identity": phase_identity,
        "no_coincidence": no_coincidence,
        "sstar_visits": sstar_visits,
        "state_space": state_space,
        "reconstruction": reconstruction,
        "pass": (
            phase_identity["pass"]
            and no_coincidence["pass"]
            and sstar_visits["pass"]
            and state_space["pass"]
            and reconstruction["pass"]
        ),
    }


def stable_render(
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = [
        "CYCLE824_INDEPENDENT_ADVERSARIAL_CHECKER",
        *(
            f"CERTIFICATE_{name}={compact(value)}"
            for name, value in certificates.items()
        ),
        f"REPORT={compact(report)}",
    ]
    return "\n".join(lines) + "\n"


def run() -> int:
    started = monotonic()
    sources = source_certificate()
    primary = run_science()
    gc.collect()
    replay = run_science()
    deterministic = primary == replay
    elapsed = monotonic() - started

    checks = {
        "1_THE_PHASE_IDENTITY":
            primary["phase_identity"]["pass"],
        "2_THE_NO_COINCIDENCE_MAP":
            primary["no_coincidence"]["pass"],
        "3_THE_SSTAR_VISIT_SCAN":
            primary["sstar_visits"]["pass"],
        "4_STATE_SPACE_COMPARABILITY":
            primary["state_space"]["pass"],
        "5_CONTROLS": False,
    }
    controls_base = (
        sources["pass"]
        and primary["reconstruction"]["pass"]
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and not any(
            name in sys.modules for name in BLOCKLISTED_MODULES
        )
        and not IMPORT_FIREWALL.hits
    )
    controls = {
        **sources,
        "status": "FAIL",
        "finding":
            "FAIL: SHA/AST blocklist, determinism, runtime, or stdout "
            "controls did not all close.",
        "independent_evolution":
            "local Boolean X/CNOT/Toffoli scalar and bit-sliced engines; "
            "neither Cycle-824 nor Cycle-820 is imported or executed",
        "determinism_scope":
            "complete transient catalog, all transient lag scans, S*, four "
            "full cycle evolutions, phase checkpoints, visits, and "
            "state-space citations",
        "primary_science_sha256": digest(primary),
        "replay_science_sha256": digest(replay),
        "deterministic_exact_certificate_equality": deterministic,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(IMPORT_FIREWALL.hits),
        "pass": False,
    }
    certificates = {
        "1_THE_PHASE_IDENTITY": primary["phase_identity"],
        "2_THE_NO_COINCIDENCE_MAP": primary["no_coincidence"],
        "3_THE_SSTAR_VISIT_SCAN": primary["sstar_visits"],
        "4_STATE_SPACE_COMPARABILITY": primary["state_space"],
        "5_CONTROLS": controls,
        "RECONSTRUCTION": primary["reconstruction"],
    }
    if not primary["phase_identity"]["pass"]:
        verdict = "PRIMARY_PHASE_IDENTITY_REFUTED"
    elif not all((
        primary["no_coincidence"]["pass"],
        primary["sstar_visits"]["pass"],
        primary["state_space"]["pass"],
    )):
        verdict = "PRIMARY_AUXILIARY_CLAIM_REFUTED"
    else:
        verdict = "PRIMARY_STRATUM_STRUCTURE_FOUND_SURVIVES"
    report = {
        "cycle": 824,
        "verdict": verdict,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE824_INDEPENDENT_CHECK_HONEST_FAIL",
    }

    for _iteration in range(8):
        checks["5_CONTROLS"] = controls["pass"]
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE824_INDEPENDENT_CHECK_EXACT_PASS"
            if report["pass"]
            else "CYCLE824_INDEPENDENT_CHECK_HONEST_FAIL"
        )
        output = stable_render(certificates, report)
        stdout_bytes = len(output.encode("utf-8"))
        controls["stdout_bytes"] = stdout_bytes
        controls["pass"] = (
            controls_base and stdout_bytes < STDOUT_LIMIT_BYTES
        )
        controls["status"] = "PASS" if controls["pass"] else "FAIL"
        controls["finding"] = (
            "PASS: all declared input SHAs and git blobs match; Cycle-824 "
            "and Cycle-820 remained AST-only and import-blocklisted; the "
            "complete science certificate replayed exactly; runtime is below "
            "1400 seconds and stdout is below 150 KiB."
            if controls["pass"] else
            "FAIL: SHA/AST blocklist, determinism, runtime, or stdout "
            "controls did not all close."
        )
        report["stdout_bytes"] = stdout_bytes

    output = stable_render(certificates, report)
    final_bytes = len(output.encode("utf-8"))
    if final_bytes >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal": "CYCLE824_INDEPENDENT_CHECK_HONEST_FAIL",
            "failure": "stdout bound exceeded",
            "stdout_bytes": final_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
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
            "pass": False,
            "terminal": "CYCLE824_INDEPENDENT_CHECK_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
