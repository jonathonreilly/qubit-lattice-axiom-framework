#!/usr/bin/env python3
"""Cycle 820 independent adversarial check of the nine-key merger claim.

Cycle 819 and Cycle 820 are SHA-pinned text/AST-only references.  Neither may
be imported or executed.  Initialization is reconstructed from the landed
Cycle-719 controller API, while every controller orbit and every subsequent
tick is evaluated by the independent gate interpreter in this file.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle819_deep_k2_continuation_2026_07_28.py",
    "scripts/frontier_cycle820_shared_moment_mechanism_2026_07_28.py",
)

import ast
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

TEXT_AST_ONLY_PATHS = (AUDIT_INPUT_PATHS[1], AUDIT_INPUT_PATHS[2])
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "e1c18187a4082fc534b9bd94055258a9aedc05c8dda37bb84f6a0d84592308fe",
    AUDIT_INPUT_PATHS[2]:
        "7344bee5d5f0bcbddcea7b9d83f40a552c90188bf30b4905f2649a49e4bf1649",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "c3a071835a61e78a4919decfede8534cbf95e1d9",
    AUDIT_INPUT_PATHS[2]: "6385dfa0dce58e86345483cc521ffa325e0d1cce",
}


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Reject any attempted import of either inspected primary."""

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


IMPORT_FIREWALL = _BlocklistFinder()
sys.meta_path.insert(0, IMPORT_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, tuple[int, int]]
Operation = tuple[int, int, int, int]

RING_STATIONS = 11
FIXTURE_BANKS = 2
TARGET_MOMENT = 14744
MERGER_MOMENT = 14739
FIXED_LAG = 5
CHECKPOINTS = (0, 1, 14738, 14739, 14740, 14744)
EXPECTED_EQUAL_CHECKPOINTS = (0, 1, 14739, 14744)
NINE_KEYS: tuple[Key, ...] = (
    (0, (1, 6)),
    (0, (1, 7)),
    (0, (2, 7)),
    (0, (2, 8)),
    (0, (3, 8)),
    (0, (3, 9)),
    (0, (4, 9)),
    (0, (4, 10)),
    (0, (5, 10)),
)
OPEN_SAMPLE_KEYS: tuple[Key, ...] = (
    (1, (1, 6)),
    (1, (1, 7)),
    (1, (2, 7)),
    (1, (2, 8)),
    (1, (3, 8)),
    (1, (3, 9)),
    (2, (1, 6)),
    (2, (1, 7)),
    (2, (2, 7)),
    (2, (2, 8)),
    (2, (3, 8)),
    (2, (3, 9)),
)
EXPECTED_CONTROL_TRANSIENTS = {
    (3, (1, 10)): 252,
    (3, (0, 7)): 371,
}
EXPECTED_OLD_CYCLES = {
    (3, (0, 5)),
    (3, (0, 6)),
    (3, (1, 6)),
    (3, (1, 7)),
    (3, (2, 7)),
    (3, (2, 8)),
    (3, (3, 8)),
    (3, (3, 9)),
    (3, (4, 9)),
    (3, (4, 10)),
    (3, (5, 10)),
    (2, (0, 9)),
}
NEW_CYCLE_KEYS = {
    (1, (0, 9)),
    (0, (0, 9)),
}
RESOLVED_THROUGH_819 = (
    set(EXPECTED_CONTROL_TRANSIENTS)
    | EXPECTED_OLD_CYCLES
    | set(NINE_KEYS)
    | NEW_CYCLE_KEYS
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def state_sha256(state: tuple[int, ...]) -> str:
    return sha256(bytes(state)).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (
            node.targets
            if isinstance(node, ast.Assign)
            else (node.target,)
        )
        if isinstance(target, ast.Name) and target.id == name
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef | None:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    return matches[0] if len(matches) == 1 else None


def primary_state_ast_audit(tree: ast.Module) -> dict[str, object]:
    hash_function = function_node(tree, "state_sha256")
    build_function = function_node(tree, "build_family")
    evolve_function = function_node(tree, "evolve_nine")
    hash_text = ast.unparse(hash_function) if hash_function else ""
    build_assigns_complete_after = bool(build_function) and any(
        isinstance(node, ast.Assign)
        and isinstance(node.value, ast.Name)
        and node.value.id == "after"
        and any(
            isinstance(target, ast.Subscript)
            and isinstance(target.value, ast.Name)
            and target.value.id == "states"
            for target in node.targets
        )
        for node in ast.walk(build_function)
    )
    hashes_ordered_full_states = bool(evolve_function) and any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "state_sha256"
        and len(node.args) == 1
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id == "state"
        for node in ast.walk(evolve_function)
    )
    result = {
        "primary_hash_definition":
            "sha256(bytes(full_5815_bit_tuple)).hexdigest()",
        "hash_function_uses_bytes_of_whole_state":
            "sha256(bytes(state)).hexdigest()" in hash_text,
        "family_dictionary_maps_external_key_to_complete_after_tuple":
            build_assigns_complete_after,
        "trajectory_hash_rows_hash_each_ordered_complete_state":
            hashes_ordered_full_states,
    }
    result["pass"] = all(
        value for key, value in result.items()
        if key != "primary_hash_definition"
    )
    return result


def source_certificate() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if (ROOT / path).is_file()
    }
    actual_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    actual_blobs = {
        path: git_blob_sha(payload)
        for path, payload in payloads.items()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_path = Path(__file__)
    self_payload = self_path.read_bytes()
    self_tree = ast.parse(self_payload, filename=self_path.name)
    direct_frontier_imports = {
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    }
    cycle819_functions = {
        node.name
        for node in trees[AUDIT_INPUT_PATHS[1]].body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    primary_tree = trees[AUDIT_INPUT_PATHS[2]]
    primary_constants_match = {
        "NINE_KEYS":
            literal_assignment(primary_tree, "NINE_KEYS") == NINE_KEYS,
        "TARGET_MOMENT":
            literal_assignment(primary_tree, "TARGET_MOMENT")
            == TARGET_MOMENT,
        "MECHANISM_ENTRY":
            literal_assignment(primary_tree, "MECHANISM_ENTRY")
            == MERGER_MOMENT,
        "FIXED_LAG":
            literal_assignment(primary_tree, "FIXED_LAG") == FIXED_LAG,
        "EXPECTED_CONTROL_TRANSIENTS":
            literal_assignment(primary_tree, "EXPECTED_CONTROL_TRANSIENTS")
            == EXPECTED_CONTROL_TRANSIENTS,
        "EXPECTED_OLD_CYCLES":
            literal_assignment(primary_tree, "EXPECTED_OLD_CYCLES")
            == EXPECTED_OLD_CYCLES,
        "NEW_CYCLE_KEYS":
            literal_assignment(primary_tree, "NEW_CYCLE_KEYS")
            == NEW_CYCLE_KEYS,
    }
    state_ast = primary_state_ast_audit(primary_tree)
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": (
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(
                not Path(path).is_absolute() and (ROOT / path).is_file()
                for path in AUDIT_INPUT_PATHS
            )
        ),
        "sha256": actual_sha,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": actual_blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "self_sha256": sha256(self_payload).hexdigest(),
        "self_git_blob": git_blob_sha(self_payload),
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "cycle819_reference_AST_basis": {
            "build_family",
            "residual_support",
            "advance_population",
            "verify_transient",
            "verify_cycle",
        } <= cycle819_functions,
        "cycle820_primary_constants_match": primary_constants_match,
        "cycle820_primary_state_AST_audit": state_ast,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(IMPORT_FIREWALL.hits),
        "direct_frontier_imports": tuple(sorted(direct_frontier_imports)),
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "maximum_named_files": 6,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and result["cycle819_reference_AST_basis"]
        and all(primary_constants_match.values())
        and state_ast["pass"]
        and direct_frontier_imports
        == {
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
        }
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and len(AUDIT_INPUT_PATHS) <= 6
    )
    return result


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left, right in combinations(range(RING_STATIONS), 2)
        if min(
            (right - left) % RING_STATIONS,
            (left - right) % RING_STATIONS,
        ) > 1
    )


def independent_word(
    program: tuple[object, ...],
    positions0: tuple[int, ...],
) -> tuple[object, ...]:
    """Build a full orbit from geometry, without K.run_orbit."""
    positions = tuple(positions0)
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    return tuple(word)


def compile_word(word: tuple[object, ...]) -> tuple[Operation, ...]:
    rows = []
    for gate in word:
        if gate.kind == "X":
            rows.append((0, gate.wires[0], 0, 0))
        elif gate.kind == "CNOT":
            rows.append((1, gate.wires[0], gate.wires[1], 0))
        elif gate.kind == "TOF":
            rows.append((2, gate.wires[0], gate.wires[1], gate.wires[2]))
        else:
            raise ValueError(("unsupported landed gate", gate))
    return tuple(rows)


def apply_scalar(
    state: tuple[int, ...],
    operations: tuple[Operation, ...],
) -> tuple[int, ...]:
    """Independent Boolean interpreter for X, CNOT, and Toffoli."""
    bits = list(state)
    for kind, first, second, third in operations:
        if kind == 0:
            bits[first] ^= 1
        elif kind == 1:
            bits[second] ^= bits[first]
        elif kind == 2:
            bits[third] ^= bits[first] & bits[second]
        else:
            raise AssertionError(kind)
    return tuple(bits)


def slice_states(states: tuple[tuple[int, ...], ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def unslice(columns: list[int], lane: int) -> tuple[int, ...]:
    return tuple((column >> lane) & 1 for column in columns)


def apply_sliced(
    columns: list[int],
    operations: tuple[Operation, ...],
    lane_mask: int,
) -> None:
    """Independent bit-sliced evaluation of one compiled transition word."""
    for kind, first, second, third in operations:
        if kind == 0:
            columns[first] ^= lane_mask
        elif kind == 1:
            columns[second] ^= columns[first]
        else:
            columns[third] ^= columns[first] & columns[second]


def residual_wire_indices(
    example_state: tuple[int, ...],
) -> tuple[int, ...]:
    """Construct the complete cleanliness projection through the core ABI."""
    banks, links = K.M.unpack_state(example_state, FIXTURE_BANKS)
    watched = (
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        K.A.DIRECTION_OK,
        *K.A.FRESH,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )
    mask_banks = []
    for bank in banks:
        row = [0] * len(bank)
        for wire in watched:
            row[wire] = 1
        mask_banks.append(tuple(row))
    mask_links = tuple(
        tuple(1 for _bit in link) for link in links
    )
    packed = list(K.M.pack_state(tuple(mask_banks), mask_links))
    packed[K.R3.X.SOURCE_POINTER] = 1
    indices = tuple(index for index, bit in enumerate(packed) if bit)
    if not indices:
        raise AssertionError("empty residual projection")
    return indices


def support_weight(
    state: tuple[int, ...],
    residual_indices: tuple[int, ...],
) -> int:
    return sum(state[index] for index in residual_indices)


def build_model() -> dict[str, object]:
    """Reconstruct only the attacked keys using the independent interpreter."""
    program = K.interleaved_program(FIXTURE_BANKS)
    positions = tuple(key[1] for key in NINE_KEYS)
    words = {
        position: independent_word(program, position)
        for position in positions
    }
    operations = {
        position: compile_word(words[position])
        for position in positions
    }
    one_token_operations = compile_word(
        independent_word(program, (0,))
    )

    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    epoch_inputs = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        epoch_inputs.append(before)
        state = apply_scalar(before, one_token_operations)

    requested_keys = NINE_KEYS + OPEN_SAMPLE_KEYS
    initial_states = {
        key: apply_scalar(epoch_inputs[key[0]], operations[key[1]])
        for key in requested_keys
    }
    residual_indices = residual_wire_indices(initial_states[NINE_KEYS[0]])

    all_keys = {
        (event, position)
        for event in range(2 * FIXTURE_BANKS)
        for position in separated_pairs()
    }
    open_keys = all_keys - RESOLVED_THROUGH_819
    summary = {
        "program_stations": len(program),
        "one_token_word_gates": len(one_token_operations),
        "position_word_gate_counts":
            tuple(sorted({len(row) for row in operations.values()})),
        "state_bits": len(initial_states[NINE_KEYS[0]]),
        "state_values_binary": all(
            bit in (0, 1)
            for state_row in initial_states.values()
            for bit in state_row
        ),
        "distinct_requested_keys": len(set(requested_keys)),
        "distinct_nine_keys": len(set(NINE_KEYS)),
        "distinct_nine_epoch_components":
            len({key[0] for key in NINE_KEYS}),
        "distinct_nine_position_pairs":
            len({key[1] for key in NINE_KEYS}),
        "family_key_count": len(all_keys),
        "resolved_key_count": len(RESOLVED_THROUGH_819),
        "open_key_count": len(open_keys),
        "open_sample_count": len(OPEN_SAMPLE_KEYS),
        "open_sample_is_subset": set(OPEN_SAMPLE_KEYS) <= open_keys,
        "open_sample_rule":
            "epochs 1 and 2 crossed with the first six merger position pairs",
        "residual_projection_wire_count": len(residual_indices),
        "initial_state_hashes": tuple(
            (key, state_sha256(initial_states[key]))
            for key in requested_keys
        ),
    }
    summary["pass"] = (
        summary["program_stations"] == 11
        and summary["one_token_word_gates"] == 3106
        and summary["position_word_gate_counts"] == (6212,)
        and summary["state_bits"] == 5815
        and summary["state_values_binary"]
        and summary["distinct_requested_keys"] == 21
        and summary["distinct_nine_keys"] == 9
        and summary["distinct_nine_epoch_components"] == 1
        and summary["distinct_nine_position_pairs"] == 9
        and summary["family_key_count"] == 176
        and summary["resolved_key_count"] == 25
        and summary["open_key_count"] == 151
        and summary["open_sample_count"] == 12
        and summary["open_sample_is_subset"]
    )
    return {
        "program": program,
        "words": words,
        "operations": operations,
        "epoch_inputs": tuple(epoch_inputs),
        "initial_states": initial_states,
        "residual_indices": residual_indices,
        "summary": summary,
    }


def support_mask(
    columns: list[int],
    residual_indices: tuple[int, ...],
) -> int:
    mask = 0
    for index in residual_indices:
        mask |= columns[index]
    return mask


def sliced_support_weight(
    columns: list[int],
    lane: int,
    residual_indices: tuple[int, ...],
) -> int:
    return sum(
        (columns[index] >> lane) & 1
        for index in residual_indices
    )


def evolve_attacked_population(
    model: dict[str, object],
) -> dict[str, object]:
    """Evolve nine claimed keys plus 12 open controls through t=14744."""
    operations: dict[
        tuple[int, int], tuple[Operation, ...]
    ] = model["operations"]
    initial_states: dict[Key, tuple[int, ...]] = model["initial_states"]
    residual_indices: tuple[int, ...] = model["residual_indices"]
    position_order = tuple(key[1] for key in NINE_KEYS)
    requested_keys = NINE_KEYS + OPEN_SAMPLE_KEYS
    groups: dict[tuple[int, int], dict[str, object]] = {}
    key_lanes: dict[Key, tuple[tuple[int, int], int]] = {}
    for position in position_order:
        keys = tuple(
            key for key in requested_keys if key[1] == position
        )
        columns = slice_states(tuple(initial_states[key] for key in keys))
        groups[position] = {
            "keys": keys,
            "columns": columns,
            "lane_mask": (1 << len(keys)) - 1,
        }
        for lane, key in enumerate(keys):
            key_lanes[key] = (position, lane)

    snapshots: dict[int, dict[Key, tuple[int, ...]]] = {}
    support_weights_at_checkpoints: dict[
        int, dict[Key, int]
    ] = {}
    first_clean: dict[Key, int | None] = {
        key: None for key in NINE_KEYS
    }
    open_target_rows: dict[Key, dict[str, object]] = {}
    all_equal_times = []
    trajectory_hasher = sha256()
    low_bit_table = bytes(value & 1 for value in range(256))
    trajectory_hasher.update(compact(tuple(
        (position, groups[position]["keys"])
        for position in position_order
    )).encode("utf-8"))

    for update in range(TARGET_MOMENT + 1):
        trajectory_hasher.update(update.to_bytes(4, "big"))
        main_state_bytes = []
        for position in position_order:
            columns = groups[position]["columns"]
            encoded_columns = bytes(columns)
            trajectory_hasher.update(encoded_columns)
            main_state_bytes.append(
                encoded_columns.translate(low_bit_table)
            )
            nonclean_lanes = support_mask(columns, residual_indices)
            for lane, key in enumerate(groups[position]["keys"]):
                if (
                    key in first_clean
                    and first_clean[key] is None
                    and not ((nonclean_lanes >> lane) & 1)
                ):
                    first_clean[key] = update
        if all(
            state_bytes == main_state_bytes[0]
            for state_bytes in main_state_bytes[1:]
        ):
            all_equal_times.append(update)

        if update in CHECKPOINTS:
            snapshot = {}
            weights = {}
            for key in NINE_KEYS:
                position, lane = key_lanes[key]
                columns = groups[position]["columns"]
                snapshot[key] = unslice(columns, lane)
                weights[key] = sliced_support_weight(
                    columns, lane, residual_indices
                )
            snapshots[update] = snapshot
            support_weights_at_checkpoints[update] = weights

        if update == TARGET_MOMENT:
            for key in OPEN_SAMPLE_KEYS:
                position, lane = key_lanes[key]
                columns = groups[position]["columns"]
                state = unslice(columns, lane)
                weight = sliced_support_weight(
                    columns, lane, residual_indices
                )
                open_target_rows[key] = {
                    "support_weight": weight,
                    "clean": weight == 0,
                    "state_sha256": state_sha256(state),
                }

        if update < TARGET_MOMENT:
            for position in position_order:
                group = groups[position]
                apply_sliced(
                    group["columns"],
                    operations[position],
                    group["lane_mask"],
                )

    equality = {
        update: len(set(snapshots[update].values())) == 1
        for update in CHECKPOINTS
    }
    hashes = {
        update: tuple(
            (key, state_sha256(snapshots[update][key]))
            for key in NINE_KEYS
        )
        for update in CHECKPOINTS
    }
    return {
        "snapshots": snapshots,
        "support_weights_at_checkpoints":
            support_weights_at_checkpoints,
        "first_clean": first_clean,
        "open_target_rows": open_target_rows,
        "checkpoint_exact_equality": equality,
        "checkpoint_hashes": hashes,
        "all_nine_exact_equality_times": tuple(all_equal_times),
        "trajectory_sha256": trajectory_hasher.hexdigest(),
    }


def merger_certificate(
    evolution: dict[str, object],
) -> dict[str, object]:
    equality: dict[int, bool] = evolution["checkpoint_exact_equality"]
    hashes: dict[
        int, tuple[tuple[Key, str], ...]
    ] = evolution["checkpoint_hashes"]
    expected = {
        update: update in EXPECTED_EQUAL_CHECKPOINTS
        for update in CHECKPOINTS
    }
    exact_equality_times: tuple[int, ...] = evolution[
        "all_nine_exact_equality_times"
    ]
    result = {
        "equality_basis":
            "exact 5815-bit tuple equality; SHA256 rows are labels only",
        "checkpoint_rows": tuple({
            "time": update,
            "expected_all_nine_equal": expected[update],
            "observed_all_nine_exact_equal": equality[update],
            "distinct_full_state_hash_count":
                len({row[1] for row in hashes[update]}),
            "full_state_hashes": hashes[update],
        } for update in CHECKPOINTS),
        "all_nine_exact_equality_times_through_t14744":
            exact_equality_times,
        "expected_exact_equality_times_through_t14744":
            EXPECTED_EQUAL_CHECKPOINTS,
        "profile_finding":
            "equal at 0,1,14739,14744; unequal at 14738,14740",
    }
    result["pass"] = (
        equality == expected
        and exact_equality_times == EXPECTED_EQUAL_CHECKPOINTS
        and all(
            len({row[1] for row in hashes[update]}) == 1
            for update in EXPECTED_EQUAL_CHECKPOINTS
        )
        and all(
            len({row[1] for row in hashes[update]}) > 1
            for update in (14738, 14740)
        )
    )
    return result


def state_object_certificate(
    sources: dict[str, object],
    model: dict[str, object],
    evolution: dict[str, object],
) -> dict[str, object]:
    snapshots: dict[
        int, dict[Key, tuple[int, ...]]
    ] = evolution["snapshots"]
    state0 = snapshots[0][NINE_KEYS[0]]
    banks, links = K.M.unpack_state(state0, FIXTURE_BANKS)
    ast_audit = sources[
        "cycle820_primary_state_AST_audit"
    ]
    result = {
        "exact_state_object_definition":
            "the complete immutable tuple of 5815 binary controller-data "
            "bits; the dictionary key (epoch, position_pair) is external",
        "full_tuple_type": type(state0).__name__,
        "full_tuple_bits": len(state0),
        "full_tuple_is_binary": all(bit in (0, 1) for bit in state0),
        "unpacked_bank_count": len(banks),
        "unpacked_bank_widths": tuple(len(bank) for bank in banks),
        "unpacked_link_count": len(links),
        "unpacked_link_widths": tuple(len(link) for link in links),
        "primary_AST_audit": ast_audit,
        "distinct_key_count": len(set(NINE_KEYS)),
        "distinct_epoch_component_count":
            len({key[0] for key in NINE_KEYS}),
        "distinct_position_pair_count":
            len({key[1] for key in NINE_KEYS}),
        "epoch_wording_finding":
            "the nine identities are distinct keys/configurations but all "
            "have epoch component 0; their nine position pairs are distinct",
        "key_identity_excluded_from_state":
            "states[key]=after stores key outside the tuple; full-state "
            "SHA256 is sha256(bytes(state)), not a residual/support subobject",
        "distinct_keys_equal_at_t0":
            len(set(snapshots[0].values())) == 1,
        "distinct_keys_equal_at_t1":
            len(set(snapshots[1].values())) == 1,
        "hash_covers_complete_tuple": (
            state_sha256(state0)
            == sha256(bytes(state0)).hexdigest()
        ),
        "claim_is_meaningful":
            "YES: equality compares the complete dynamical state while "
            "deliberately excluding external selector metadata",
    }
    result["pass"] = (
        result["full_tuple_type"] == "tuple"
        and result["full_tuple_bits"] == 5815
        and result["full_tuple_is_binary"]
        and ast_audit["pass"]
        and result["distinct_key_count"] == 9
        and result["distinct_epoch_component_count"] == 1
        and result["distinct_position_pair_count"] == 9
        and result["distinct_keys_equal_at_t0"]
        and result["distinct_keys_equal_at_t1"]
        and result["hash_covers_complete_tuple"]
    )
    return result


def funnel_certificate(
    model: dict[str, object],
    evolution: dict[str, object],
) -> dict[str, object]:
    operations: dict[
        tuple[int, int], tuple[Operation, ...]
    ] = model["operations"]
    residual_indices: tuple[int, ...] = model["residual_indices"]
    snapshots: dict[
        int, dict[Key, tuple[int, ...]]
    ] = evolution["snapshots"]
    sstar = snapshots[MERGER_MOMENT][NINE_KEYS[0]]
    rows = []
    final_images = []
    for key in NINE_KEYS:
        current = sstar
        weights = [support_weight(current, residual_indices)]
        hashes = [state_sha256(current)]
        for _lag in range(FIXED_LAG):
            current = apply_scalar(current, operations[key[1]])
            weights.append(support_weight(current, residual_indices))
            hashes.append(state_sha256(current))
        final_images.append(current)
        rows.append({
            "key": key,
            "support_weights_lag_0_through_5": tuple(weights),
            "state_hashes_lag_0_through_5": tuple(hashes),
            "nonclean_lags_1_through_4":
                all(weights[lag] > 0 for lag in range(1, 5)),
            "clean_at_lag_5": weights[5] == 0,
            "isolated_image_equals_continuous_t14744":
                current == snapshots[TARGET_MOMENT][key],
        })
    result = {
        "entry_time": MERGER_MOMENT,
        "entry_state_sha256": state_sha256(sstar),
        "ticks_evolved_independently": FIXED_LAG,
        "target_time": MERGER_MOMENT + FIXED_LAG,
        "rows": tuple(rows),
        "all_final_images_exact_tuple_equal":
            len(set(final_images)) == 1,
        "common_clean_image_sha256": state_sha256(final_images[0]),
        "finding":
            "each distinct word leaves residuals at 14740..14743 and "
            "reaches one common clean image at 14744",
    }
    result["pass"] = (
        result["target_time"] == TARGET_MOMENT
        and all(row["nonclean_lags_1_through_4"] for row in rows)
        and all(row["clean_at_lag_5"] for row in rows)
        and all(
            row["isolated_image_equals_continuous_t14744"]
            for row in rows
        )
        and result["all_final_images_exact_tuple_equal"]
    )
    return result


def candidate_certificates(
    model: dict[str, object],
    evolution: dict[str, object],
    merger: dict[str, object],
    funnel: dict[str, object],
) -> tuple[dict[str, object], dict[str, object]]:
    equality_times: tuple[int, ...] = evolution[
        "all_nine_exact_equality_times"
    ]
    earlier_entries = tuple(
        update for update in equality_times
        if update < TARGET_MOMENT
        and (update == 0 or update - 1 not in equality_times)
    )
    first_clean: dict[Key, int | None] = evolution["first_clean"]
    candidate_a = {
        "candidate":
            "A_common_exact_configuration_plus_landed_lag_5",
        "status": "HOLDS_EXACTLY",
        "shared_entry_times_before_target": earlier_entries,
        "last_shared_entry": MERGER_MOMENT,
        "entry_state_sha256": funnel["entry_state_sha256"],
        "fixed_lag": FIXED_LAG,
        "prediction_relation": "14739+5=14744",
        "all_nine_first_clean": tuple(
            (key, first_clean[key]) for key in NINE_KEYS
        ),
        "causal_bridge_for_lag_value": "OPEN_NOT_DERIVED",
        "exact_statement_finding":
            "S* plus the nine landed words gives the exact five-tick "
            "funnel; the origin of S* and an a-priori lag selector remain open",
    }
    candidate_a["pass"] = (
        merger["pass"]
        and funnel["pass"]
        and earlier_entries == (0, MERGER_MOMENT)
        and all(
            first_clean[key] == TARGET_MOMENT for key in NINE_KEYS
        )
        and MERGER_MOMENT + FIXED_LAG == TARGET_MOMENT
    )

    operations: dict[
        tuple[int, int], tuple[Operation, ...]
    ] = model["operations"]
    operation_rows = tuple(
        operations[key[1]] for key in NINE_KEYS
    )
    left_key, right_key = NINE_KEYS[:2]
    first_difference = next(
        index for index, (left, right) in enumerate(zip(
            operations[left_key[1]], operations[right_key[1]]
        )) if left != right
    )
    candidate_f = {
        "candidate": "F_identical_transition_words",
        "status": "FAILS",
        "counterexample_kind":
            "syntactically distinct complete compiled transition words",
        "compiled_word_sha256": tuple(
            (key, digest(operations[key[1]])) for key in NINE_KEYS
        ),
        "distinct_word_count": len(set(operation_rows)),
        "counterexample_keys": (left_key, right_key),
        "first_differing_operation_index": first_difference,
        "left_operation":
            operations[left_key[1]][first_difference],
        "right_operation":
            operations[right_key[1]][first_difference],
        "despite_common_clean_five_step_image":
            funnel["all_final_images_exact_tuple_equal"],
        "finding":
            "all nine transition words are distinct; identical words "
            "cannot explain the merger or five-step reconvergence",
    }
    candidate_f["pass"] = (
        candidate_f["distinct_word_count"] == 9
        and candidate_f["left_operation"]
        != candidate_f["right_operation"]
        and candidate_f["despite_common_clean_five_step_image"]
    )
    return candidate_a, candidate_f


def open_key_certificate(
    model: dict[str, object],
    evolution: dict[str, object],
) -> dict[str, object]:
    rows_by_key: dict[Key, dict[str, object]] = evolution[
        "open_target_rows"
    ]
    rows = tuple({
        "key": key,
        **rows_by_key[key],
    } for key in OPEN_SAMPLE_KEYS)
    result = {
        "population_open_key_count": model["summary"]["open_key_count"],
        "sample_rule": model["summary"]["open_sample_rule"],
        "sample_size": len(rows),
        "sample_keys": OPEN_SAMPLE_KEYS,
        "sample_is_subset_of_open_151":
            model["summary"]["open_sample_is_subset"],
        "scan_time": TARGET_MOMENT,
        "cleanliness_scan":
            "direct scan of every source-pointer, watched-bank, and link "
            "residual wire in each independently evolved full state",
        "rows": rows,
        "clean_sample_keys": tuple(
            row["key"] for row in rows if row["clean"]
        ),
        "finding":
            "zero of 12 deterministic open-key controls is clean at 14744",
    }
    result["pass"] = (
        result["population_open_key_count"] == 151
        and result["sample_size"] == 12
        and result["sample_is_subset_of_open_151"]
        and not result["clean_sample_keys"]
        and all(row["support_weight"] > 0 for row in rows)
    )
    return result


def stable_render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = ["CYCLE820_MECHANISM_INDEPENDENT_CHECK"]
    for name, value in certificates.items():
        lines.append(
            f"{'PASS' if checks[name] else 'FAIL'} {name} :: "
            f"{compact(value)}"
        )
    lines.append(f"REPORT={compact(report)}")
    lines.append(report["terminal"])
    return "\n".join(lines) + "\n"


def run() -> int:
    started = monotonic()
    sources = source_certificate()
    model = build_model()
    evolution = evolve_attacked_population(model)
    replay = evolve_attacked_population(model)

    merger = merger_certificate(evolution)
    state_object = state_object_certificate(sources, model, evolution)
    funnel = funnel_certificate(model, evolution)
    candidate_a, candidate_f = candidate_certificates(
        model, evolution, merger, funnel
    )
    open_control = open_key_certificate(model, evolution)

    deterministic = evolution == replay
    elapsed = monotonic() - started
    controls = {
        "sources": sources,
        "model_reconstruction": model["summary"],
        "evolution_implementation":
            "local compiled X/CNOT/TOF scalar and bit-sliced interpreters; "
            "K.run_orbit and K.A.apply_semantic are never called",
        "primary_and_predecessor_mode":
            "Cycle 820 and Cycle 819 are SHA-pinned text/AST-only",
        "primary_trajectory_sha256": evolution["trajectory_sha256"],
        "replay_trajectory_sha256": replay["trajectory_sha256"],
        "determinism_scope":
            "all 21 full-state trajectories t=0..14744, all cleanliness "
            "results, all six checkpoints, and the exact equality-time list",
        "deterministic_exact_replay": deterministic,
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(IMPORT_FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
    }
    controls_base = (
        sources["pass"]
        and model["summary"]["pass"]
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
    )

    checks = {
        "THE_MERGER": merger["pass"],
        "STATE_OBJECT_AUDIT": state_object["pass"],
        "THE_FUNNEL": funnel["pass"],
        "CANDIDATE_A_EXACT_STATEMENT": candidate_a["pass"],
        "CANDIDATE_F_COUNTEREXAMPLE": candidate_f["pass"],
        "THE_OPEN_KEY_CONTROL": open_control["pass"],
        "CONTROLS": False,
    }
    certificates = {
        "THE_MERGER": merger,
        "STATE_OBJECT_AUDIT": state_object,
        "THE_FUNNEL": funnel,
        "CANDIDATE_A_EXACT_STATEMENT": candidate_a,
        "CANDIDATE_F_COUNTEREXAMPLE": candidate_f,
        "THE_OPEN_KEY_CONTROL": open_control,
        "CONTROLS": controls,
    }
    report = {
        "cycle": 820,
        "role": "INDEPENDENT_ADVERSARIAL_CHECKER",
        "verdict": "REFUTED",
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal":
            "CYCLE820_MECHANISM_INDEPENDENT_CHECK_REFUTED",
    }

    for _iteration in range(8):
        controls["pass"] = controls_base
        checks["CONTROLS"] = controls["pass"]
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["verdict"] = (
            "CONFIRMED" if report["pass"] else "REFUTED"
        )
        report["terminal"] = (
            "CYCLE820_MECHANISM_INDEPENDENT_CHECK_CONFIRMED"
            if report["pass"]
            else "CYCLE820_MECHANISM_INDEPENDENT_CHECK_REFUTED"
        )
        output = stable_render(checks, certificates, report)
        stdout_bytes = len(output.encode("utf-8"))
        stdout_ok = stdout_bytes < STDOUT_LIMIT_BYTES
        controls["stdout_bytes"] = stdout_bytes
        controls["pass"] = controls_base and stdout_ok
        checks["CONTROLS"] = controls["pass"]
        report["stdout_bytes"] = stdout_bytes

    output = stable_render(checks, certificates, report)
    final_bytes = len(output.encode("utf-8"))
    if final_bytes >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "verdict": "REFUTED",
            "terminal":
                "CYCLE820_MECHANISM_INDEPENDENT_CHECK_REFUTED",
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
            "verdict": "REFUTED",
            "terminal":
                "CYCLE820_MECHANISM_INDEPENDENT_CHECK_REFUTED",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
