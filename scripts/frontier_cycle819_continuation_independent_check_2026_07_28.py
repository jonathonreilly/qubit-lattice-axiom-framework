#!/usr/bin/env python3
"""Cycle 819 independent adversarial checker.

The Cycle-819 and Cycle-795 primaries are SHA-pinned text/AST evidence only.
They are blocklisted from import.  Evolution after construction of the landed
Cycle-719 postimages uses this checker's independent Python-integer state
engine, not either primary's tuple or lane-bit evolution path.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle795_discriminator_census_2026_07_28.py",
    "scripts/frontier_cycle819_deep_k2_continuation_2026_07_28.py",
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

TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "6a52229e9ac3bf5ab45bd25a4088e354c759fc499b58462aa0c2401f89474e7f",
    AUDIT_INPUT_PATHS[2]:
        "e1c18187a4082fc534b9bd94055258a9aedc05c8dda37bb84f6a0d84592308fe",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "45afe5159562f28bb9edebf7340b582408ad4ba7",
    AUDIT_INPUT_PATHS[2]: "c3a071835a61e78a4919decfede8534cbf95e1d9",
}


class _PrimaryBlocklist(importlib.abc.MetaPathFinder):
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
            raise ImportError(f"primary import forbidden: {fullname}")
        return None


IMPORT_FIREWALL = _PrimaryBlocklist()
sys.meta_path.insert(0, IMPORT_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, tuple[int, int]]
Coordinate = tuple[str, str, int]
RING_STATIONS = 11
FIXTURE_BANKS = 2
TARGET_HORIZON = 16384
SHARED_MOMENT = 14744
LANDED_CONSTANTS = (130, 11, 2, 5, 12, 288, 6, 3)
EXPECTED_FEATURE_TABLE_SHA256 = (
    "266dd5f0c36cb79eb88a143c303e31ef1f79b068d6131545962ee38f8d24e705"
)
EXPECTED_CLEAN_NAMES_SHA256 = (
    "dc265dc602faef161bf1483f95810396fe3c4dfa75e7afb1cf9f871a396e6d91"
)

BASELINE_TRANSIENTS = {
    (3, (1, 10)): 252,
    (3, (0, 7)): 371,
}
BASELINE_CYCLES = {
    (3, (0, 5)): (2, 2),
    (3, (0, 6)): (2, 2),
    (3, (1, 6)): (3, 3),
    (3, (1, 7)): (3, 3),
    (3, (2, 7)): (3, 3),
    (3, (2, 8)): (3, 3),
    (3, (3, 8)): (3, 3),
    (3, (3, 9)): (3, 3),
    (3, (4, 9)): (3, 3),
    (3, (4, 10)): (3, 3),
    (3, (5, 10)): (3, 3),
    (2, (0, 9)): (288, 6),
}
CLAIMED_TRANSIENTS = (
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
DECLARED_TRANSIENT_DETAIL_KEYS = (
    (0, (1, 6)),
    (0, (2, 7)),
    (0, (3, 8)),
    (0, (4, 9)),
    (0, (5, 10)),
)
CLAIMED_CYCLES = {
    (1, (0, 9)): (0, 8928),
    (0, (0, 9)): (0, 8930),
}
DECLARED_NULL_KEYS = (
    (1, (1, 6)),
    (2, (1, 6)),
    (1, (1, 7)),
    (2, (1, 7)),
    (1, (2, 7)),
    (2, (2, 7)),
    (1, (2, 8)),
    (2, (2, 8)),
)
DECLARED_DETERMINISM_SLICE = DECLARED_NULL_KEYS[:2]

# Independently derived in the first bounded execution, then pinned so later
# changes cannot silently alter the per-resolution C/W/survivor certificate.
EXPECTED_SCORING_TABLE: tuple[tuple[object, ...], ...] = (
    ((1, (0, 9)), 8928, "CYCLE", 45, 58, 45, 12),
    ((0, (0, 9)), 8930, "CYCLE", 67, 36, 45, 12),
    ((0, (1, 6)), 14744, "TRANSIENT", 6, 97, 2, 2),
    ((0, (1, 7)), 14744, "TRANSIENT", 2, 101, 0, 0),
    ((0, (2, 7)), 14744, "TRANSIENT", 3, 100, 0, 0),
    ((0, (2, 8)), 14744, "TRANSIENT", 1, 102, 0, 0),
    ((0, (3, 8)), 14744, "TRANSIENT", 14, 89, 0, 0),
    ((0, (3, 9)), 14744, "TRANSIENT", 1, 102, 0, 0),
    ((0, (4, 9)), 14744, "TRANSIENT", 2, 101, 0, 0),
    ((0, (4, 10)), 14744, "TRANSIENT", 6, 97, 0, 0),
    ((0, (5, 10)), 14744, "TRANSIENT", 7, 96, 0, 0),
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values = [
        node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(values) != 1:
        return None
    try:
        return ast.literal_eval(values[0])
    except (TypeError, ValueError):
        return None


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_certificate() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if not Path(path).is_absolute() and (ROOT / path).is_file()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    actual_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    actual_blobs = {
        path: git_blob_sha(payload)
        for path, payload in payloads.items()
    }
    direct_frontier_imports = {
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    }
    names795 = function_names(trees[AUDIT_INPUT_PATHS[1]])
    names819 = function_names(trees[AUDIT_INPUT_PATHS[2]])
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_worktree_relative_paths":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS
            and len(payloads) == len(AUDIT_INPUT_PATHS),
        "sha256": actual_sha,
        "git_blobs": actual_blobs,
        "text_AST_only": TEXT_AST_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(IMPORT_FIREWALL.hits),
        "direct_frontier_imports": tuple(sorted(direct_frontier_imports)),
        "cycle795_definition_basis": {
            "feature_schema",
            "feature_table",
            "candidate_result",
            "discrimination_census",
        } <= names795,
        "cycle819_claim_surface": {
            "verify_transient",
            "verify_cycle",
            "score_forecasts",
            "advance_population",
        } <= names819,
        "named_files_read": len(payloads),
        "maximum_files_allowed": 6,
    }
    result["pass"] = (
        result["literal_worktree_relative_paths"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and direct_frontier_imports == {
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
        }
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and result["cycle795_definition_basis"]
        and result["cycle819_claim_surface"]
        and len(payloads) <= 6
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


def two_token_word(
    program: tuple[object, ...],
    positions0: tuple[int, int],
) -> tuple[object, ...]:
    positions = positions0
    output = []
    for _step in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                output.extend(K.mapped_macro(row))
        positions = tuple(
            (position + 1) % len(program) for position in positions
        )
    return tuple(output)


def compile_integer_word(
    word: tuple[object, ...],
) -> tuple[tuple[int, int, int, int], ...]:
    operations = []
    for gate in word:
        if gate.kind == "X":
            operations.append((0, 1 << gate.wires[0], 0, 0))
        elif gate.kind == "CNOT":
            operations.append((
                1, 1 << gate.wires[0], 1 << gate.wires[1], 0
            ))
        elif gate.kind == "TOF":
            operations.append((
                2,
                1 << gate.wires[0],
                1 << gate.wires[1],
                1 << gate.wires[2],
            ))
        else:
            raise ValueError(("unsupported gate", gate.kind))
    return tuple(operations)


def tuple_to_integer(state: tuple[int, ...]) -> int:
    return sum(bit << index for index, bit in enumerate(state))


def integer_to_tuple(state: int, width: int) -> tuple[int, ...]:
    return tuple((state >> index) & 1 for index in range(width))


def apply_integer_word(
    state: int,
    operations: tuple[tuple[int, int, int, int], ...],
) -> int:
    for kind, first, second, third in operations:
        if kind == 0:
            state ^= first
        elif kind == 1:
            if state & first:
                state ^= second
        elif state & first and state & second:
            state ^= third
    return state


def watched_registers() -> tuple[tuple[str, int], ...]:
    return (
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
        *tuple(
            (f"FRESH_{index}", wire)
            for index, wire in enumerate(K.A.FRESH)
        ),
        *tuple(
            (f"ZERO_WORK_{index}", wire)
            for index, wire in enumerate(K.A.ZERO_WORK)
        ),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )


def residue_index_map(
    width: int,
) -> tuple[int, tuple[tuple[int, Coordinate], ...]]:
    tagged = tuple(range(width))
    banks, links = K.M.unpack_state(tagged, FIXTURE_BANKS)
    rows: list[tuple[int, Coordinate]] = [
        (K.R3.X.SOURCE_POINTER, ("source", "SOURCE_POINTER", 0))
    ]
    for bank_index, bank in enumerate(banks):
        for name, wire in watched_registers():
            rows.append((bank[wire], ("bank", name, bank_index)))
    for link_index, link in enumerate(links):
        for wire_index, state_index in enumerate(link):
            rows.append((
                state_index, ("link", f"WIRE_{wire_index}", link_index)
            ))
    rows.sort(key=lambda row: row[1])
    if len({index for index, _coordinate in rows}) != len(rows):
        raise AssertionError("residue state indices are not unique")
    mask = sum(1 << index for index, _coordinate in rows)
    return mask, tuple(rows)


def support_of(
    state: int,
    residue_rows: tuple[tuple[int, Coordinate], ...],
) -> tuple[Coordinate, ...]:
    return tuple(
        coordinate
        for index, coordinate in residue_rows
        if state & (1 << index)
    )


def state_sha256(state: int, width: int) -> str:
    return sha256(
        state.to_bytes((width + 7) // 8, "little")
    ).hexdigest()


def build_family() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    positions = separated_pairs()
    words = {
        pair: two_token_word(program, pair) for pair in positions
    }
    integer_words = {
        pair: compile_integer_word(words[pair]) for pair in positions
    }

    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    running_state = K.M.pack_state(banks, links)
    epochs = []
    epoch_failures = 0
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(running_state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        expected = K.A.apply_semantic(
            before, K.M.global_allocator_word(FIXTURE_BANKS)
        )
        epoch_failures += after != expected
        epoch_failures += (
            rail_a != (1,) + (0,) * (len(program) - 1)
            or any(rail_b)
            or len(trace) != len(program)
        )
        epochs.append((event, direction, before))
        running_state = after

    tuple_states: dict[Key, tuple[int, ...]] = {}
    integer_states: dict[Key, int] = {}
    composition_failures = 0
    rail_failures = 0
    for event, _direction, before in epochs:
        for pair in positions:
            after, rail_a, rail_b, _trace = K.run_orbit(
                before, program, token_positions=pair
            )
            expected_rail = tuple(
                int(station in pair) for station in range(len(program))
            )
            composition_failures += (
                after != K.A.apply_semantic(before, words[pair])
            )
            rail_failures += (
                rail_a != expected_rail or any(rail_b)
            )
            key = (event, pair)
            tuple_states[key] = after
            integer_states[key] = tuple_to_integer(after)

    width = len(next(iter(tuple_states.values())))
    residue_mask, residue_rows = residue_index_map(width)
    supports = {
        key: support_of(state, residue_rows)
        for key, state in integer_states.items()
    }
    equivalence_keys = tuple(sorted(integer_states))[:8]
    integer_equivalence_rows = []
    for key in equivalence_keys:
        observed = apply_integer_word(
            integer_states[key], integer_words[key[1]]
        )
        expected_tuple = K.A.apply_semantic(
            tuple_states[key], words[key[1]]
        )
        expected = tuple_to_integer(expected_tuple)
        integer_equivalence_rows.append((
            key,
            observed == expected,
            state_sha256(observed, width),
            state_sha256(expected, width),
        ))

    unique_supports = set(supports.values())
    summary = {
        "events": len(epochs),
        "directions": tuple(direction for _, direction, _ in epochs),
        "program_stations": len(program),
        "separated_pairs": len(positions),
        "keys": len(integer_states),
        "unique_initial_supports": len(unique_supports),
        "unique_supports_by_event": tuple(
            len({
                supports[(event, pair)] for pair in positions
            })
            for event in range(4)
        ),
        "state_width": width,
        "epoch_failures": epoch_failures,
        "composition_failures": composition_failures,
        "rail_failures": rail_failures,
        "all_initial_residues_nonzero": all(supports.values()),
        "integer_engine_equivalence_slice":
            tuple(integer_equivalence_rows),
    }
    summary["pass"] = (
        summary["events"] == 4
        and summary["directions"]
        == ((1, 0), (0, 1), (1, 0), (0, 1))
        and summary["program_stations"] == 11
        and summary["separated_pairs"] == 44
        and summary["keys"] == 176
        and summary["unique_initial_supports"] == 25
        and summary["unique_supports_by_event"] == (1, 1, 12, 14)
        and summary["epoch_failures"] == 0
        and summary["composition_failures"] == 0
        and summary["rail_failures"] == 0
        and summary["all_initial_residues_nonzero"]
        and all(row[1] for row in integer_equivalence_rows)
    )
    return {
        "program": program,
        "epochs": tuple(epochs),
        "positions": positions,
        "words": words,
        "integer_words": integer_words,
        "states": integer_states,
        "supports": supports,
        "width": width,
        "residue_mask": residue_mask,
        "residue_rows": residue_rows,
        "summary": summary,
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
    modular = tuple(
        f"{coordinate}_mod_{modulus}"
        for modulus in LANDED_CONSTANTS
        for coordinate in (
            "left",
            "right",
            "position_sum",
            "clockwise_gap",
            "ring_separation",
            "epoch",
        )
    )
    equal = tuple(
        f"same_position_residue_mod_{modulus}"
        for modulus in LANDED_CONSTANTS
    )
    return base + modular + equal


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


def named_features(
    key: Key,
    direction: tuple[int, int],
    support: tuple[Coordinate, ...],
    support_classes: dict[tuple[Coordinate, ...], int],
) -> dict[str, int]:
    event, (left, right) = key
    clockwise = (right - left) % RING_STATIONS
    counterclockwise = (left - right) % RING_STATIONS
    separation = min(clockwise, counterclockwise)
    short_orientation = 1 if clockwise < counterclockwise else -1
    epoch_direction = 1 if direction == (1, 0) else -1
    position_sum = left + right
    source_count = sum(row[0] == "source" for row in support)
    bank_count = sum(row[0] == "bank" for row in support)
    link_count = sum(row[0] == "link" for row in support)
    bank0_count = sum(
        row[0] == "bank" and row[2] == 0 for row in support
    )
    bank1_count = sum(
        row[0] == "bank" and row[2] == 1 for row in support
    )
    named = {
        "epoch": event,
        "epoch_parity": event % 2,
        "epoch_direction": epoch_direction,
        "left": left,
        "right": right,
        "clockwise_gap": clockwise,
        "counterclockwise_gap": counterclockwise,
        "ring_separation": separation,
        "ring_long_distance": max(clockwise, counterclockwise),
        "short_orientation": short_orientation,
        "direction_short_alignment":
            epoch_direction * short_orientation,
        "position_sum": position_sum,
        "position_product": left * right,
        "occupancy_mask": (1 << left) | (1 << right),
        "chord_midpoint_mod11": (6 * position_sum) % RING_STATIONS,
        "short_arc_start": left if short_orientation == 1 else right,
        "short_arc_end": right if short_orientation == 1 else left,
        "left_parity": left % 2,
        "right_parity": right % 2,
        "parity_code": 2 * (left % 2) + right % 2,
        "same_position_parity": int(left % 2 == right % 2),
        "epoch_sum_parity": (event + position_sum) % 2,
        "initial_residual_weight": len(support),
        "initial_support_size": len(support),
        "support_signature_id": support_classes[support],
        "support_kind_mask": (
            int(source_count > 0)
            + 2 * int(bank_count > 0)
            + 4 * int(link_count > 0)
        ),
        "support_source_count": source_count,
        "support_bank_count": bank_count,
        "support_link_count": link_count,
        "support_bank0_count": bank0_count,
        "support_bank1_count": bank1_count,
        "support_bank_imbalance": bank1_count - bank0_count,
        "support_coordinate_index_sum": sum(row[2] for row in support),
    }
    for modulus in LANDED_CONSTANTS:
        named.update({
            f"left_mod_{modulus}": left % modulus,
            f"right_mod_{modulus}": right % modulus,
            f"position_sum_mod_{modulus}": position_sum % modulus,
            f"clockwise_gap_mod_{modulus}": clockwise % modulus,
            f"ring_separation_mod_{modulus}": separation % modulus,
            f"epoch_mod_{modulus}": event % modulus,
            f"same_position_residue_mod_{modulus}":
                int(left % modulus == right % modulus),
        })
    if set(named) != set(FEATURE_SCHEMA):
        raise AssertionError(
            ("feature schema mismatch", set(named) ^ set(FEATURE_SCHEMA))
        )
    return named


def reconstruct_feature_table(
    family: dict[str, object],
) -> dict[str, object]:
    directions = {
        event: direction
        for event, direction, _before in family["epochs"]
    }
    support_classes = {
        support: index
        for index, support in enumerate(
            sorted(set(family["supports"].values()))
        )
    }
    features = {}
    rows = []
    for key in sorted(family["states"]):
        named = named_features(
            key,
            directions[key[0]],
            family["supports"][key],
            support_classes,
        )
        features[key] = named
        event, (left, right) = key
        rows.append(
            (event, left, right)
            + tuple(named[name] for name in FEATURE_SCHEMA)
        )
    return {
        "features": features,
        "rows": tuple(rows),
        "support_class_count": len(support_classes),
        "table_sha256": digest(tuple(rows)),
    }


def scan_first_clean(
    key: Key,
    family: dict[str, object],
    claimed_moment: int,
) -> dict[str, object]:
    state = family["states"][key]
    operations = family["integer_words"][key[1]]
    residue_mask = family["residue_mask"]
    residue_rows = family["residue_rows"]
    width = family["width"]
    first_clean = None
    earlier_nonclean = True
    window = []
    selected = key in DECLARED_TRANSIENT_DETAIL_KEYS
    for update in range(claimed_moment + 7):
        if update:
            state = apply_integer_word(state, operations)
        clean = not (state & residue_mask)
        if update < claimed_moment:
            earlier_nonclean &= not clean
        if clean and first_clean is None:
            first_clean = update
        if selected and claimed_moment - 1 <= update <= claimed_moment + 6:
            support = support_of(state, residue_rows)
            window.append({
                "offset": update - claimed_moment,
                "moment": update,
                "landed_clean": not support,
                "support_weight": len(support),
                "support_sha256": digest(support),
                "state_sha256": state_sha256(state, width),
            })
    result = {
        "key": key,
        "declared_detail": selected,
        "claimed_first_clean": claimed_moment,
        "observed_first_clean": first_clean,
        "earlier_times_checked": claimed_moment,
        "all_earlier_times_nonclean": earlier_nonclean,
        "moment_minus_one_veto": (
            bool(window[0]["support_weight"]) if selected else True
        ),
        "plus_1_through_6_present": (
            tuple(row["offset"] for row in window)
            == (-1, 0, 1, 2, 3, 4, 5, 6)
            if selected else True
        ),
        "window": tuple(window),
    }
    result["pass"] = (
        first_clean == claimed_moment
        and earlier_nonclean
        and result["moment_minus_one_veto"]
        and result["plus_1_through_6_present"]
    )
    return result


def proper_divisors(value: int) -> tuple[int, ...]:
    return tuple(
        candidate
        for candidate in range(1, value)
        if value % candidate == 0
    )


def scan_cycle(
    key: Key,
    family: dict[str, object],
    claimed_entry: int,
    claimed_period: int,
) -> dict[str, object]:
    if claimed_entry != 0:
        raise AssertionError("this checker declares both cycle entries zero")
    state0 = family["states"][key]
    state = state0
    operations = family["integer_words"][key[1]]
    residue_mask = family["residue_mask"]
    width = family["width"]
    closure = claimed_entry + claimed_period
    seen = {state0: 0}
    first_repeat = None
    divisor_set = set(proper_divisors(claimed_period))
    divisor_returns = {}
    every_phase_nonclean = bool(state0 & residue_mask)
    phase_hasher = sha256()
    phase_hasher.update(
        (state0 & residue_mask).to_bytes((width + 7) // 8, "little")
    )
    state_at_closure = None
    for update in range(1, closure + 1):
        state = apply_integer_word(state, operations)
        nonclean = bool(state & residue_mask)
        every_phase_nonclean &= nonclean
        phase_hasher.update(
            (state & residue_mask).to_bytes(
                (width + 7) // 8, "little"
            )
        )
        if update in divisor_set:
            divisor_returns[update] = state == state0
        prior = seen.get(state)
        if prior is not None and first_repeat is None:
            first_repeat = (prior, update)
        else:
            seen[state] = update
        if update == closure:
            state_at_closure = state
    result = {
        "key": key,
        "claimed_entry": claimed_entry,
        "claimed_period": claimed_period,
        "claimed_closure": closure,
        "first_exact_repeat": first_repeat,
        "exact_recurrence": state_at_closure == state0,
        "state_period_minimal_by_divisor_rejection":
            not any(divisor_returns.values()),
        "proper_divisor_returns": tuple(sorted(divisor_returns.items())),
        "forever_nonclean_through_preperiod_plus_period":
            every_phase_nonclean,
        "nonclean_moments_checked_inclusive": closure + 1,
        "residual_trace_sha256": phase_hasher.hexdigest(),
        "entry_state_sha256": state_sha256(state0, width),
        "closure_state_sha256": state_sha256(state_at_closure, width),
    }
    result["pass"] = (
        first_repeat == (claimed_entry, closure)
        and result["exact_recurrence"]
        and result["state_period_minimal_by_divisor_rejection"]
        and result["forever_nonclean_through_preperiod_plus_period"]
    )
    return result


def scan_open_key(
    key: Key,
    family: dict[str, object],
    horizon: int,
) -> dict[str, object]:
    state = family["states"][key]
    operations = family["integer_words"][key[1]]
    residue_mask = family["residue_mask"]
    width = family["width"]
    seen = {state}
    events = []
    boundary_rows = []
    for update in range(1, horizon + 1):
        state = apply_integer_word(state, operations)
        if not state & residue_mask:
            events.append(("FIRST_CLEAN", update))
            break
        if state in seen:
            events.append(("EXACT_RECURRENCE", update))
            break
        seen.add(state)
        if update in (4096, 8192, horizon):
            boundary_rows.append({
                "moment": update,
                "state_sha256": state_sha256(state, width),
                "support_weight": (state & residue_mask).bit_count(),
            })
    result = {
        "key": key,
        "horizon": horizon,
        "events": tuple(events),
        "moments_evolved": update,
        "distinct_states_including_t0": len(seen),
        "boundaries": tuple(boundary_rows),
        "final_state_sha256": state_sha256(state, width),
    }
    result["pass"] = (
        not events
        and update == horizon
        and len(seen) == horizon + 1
        and tuple(row["moment"] for row in boundary_rows)
        == (4096, 8192, horizon)
    )
    return result


def replay_boundaries(
    key: Key,
    family: dict[str, object],
    horizon: int,
) -> tuple[dict[str, object], ...]:
    state = family["states"][key]
    operations = family["integer_words"][key[1]]
    residue_mask = family["residue_mask"]
    width = family["width"]
    rows = []
    for update in range(1, horizon + 1):
        state = apply_integer_word(state, operations)
        if update in (4096, 8192, horizon):
            rows.append({
                "moment": update,
                "state_sha256": state_sha256(state, width),
                "support_weight": (state & residue_mask).bit_count(),
            })
    return tuple(rows)


def projection(
    feature_row: dict[str, int],
    names: tuple[str, ...],
) -> tuple[int, ...]:
    return tuple(feature_row[name] for name in names)


def forecast_side(
    value: tuple[int, ...],
    transient_values: set[tuple[int, ...]],
    cycle_values: set[tuple[int, ...]],
) -> str:
    if value in transient_values and value not in cycle_values:
        return "TRANSIENT"
    if value in cycle_values and value not in transient_values:
        return "CYCLE"
    return "UNSEEN"


def reconstruct_hypotheses(
    feature_table: dict[str, object],
) -> dict[str, object]:
    features = feature_table["features"]
    transient_keys = tuple(sorted(BASELINE_TRANSIENTS))
    cycle_keys = tuple(sorted(BASELINE_CYCLES))
    resolved = set(transient_keys) | set(cycle_keys)
    open_keys = tuple(sorted(set(features) - resolved))
    candidates = (
        tuple((name,) for name in FEATURE_SCHEMA)
        + tuple(combinations(PAIR_FEATURES, 2))
    )
    clean = []
    for names in candidates:
        transient_values = {
            projection(features[key], names) for key in transient_keys
        }
        cycle_values = {
            projection(features[key], names) for key in cycle_keys
        }
        if not transient_values.isdisjoint(cycle_values):
            continue
        forecast = tuple(
            forecast_side(
                projection(features[key], names),
                transient_values,
                cycle_values,
            )
            for key in open_keys
        )
        margin = min(
            sum(abs(left - right) for left, right in zip(tvalue, cvalue))
            for tvalue in transient_values
            for cvalue in cycle_values
        )
        clean.append({
            "names": names,
            "transient_values": transient_values,
            "cycle_values": cycle_values,
            "forecast": forecast,
            "margin": margin,
            "open_classified":
                sum(value != "UNSEEN" for value in forecast),
        })
    clean.sort(key=lambda row: (
        -row["open_classified"],
        len(row["names"]),
        -row["margin"],
        row["names"],
    ))
    vectors = tuple(sorted({row["forecast"] for row in clean}))
    return {
        "open_keys": open_keys,
        "candidates": candidates,
        "clean": tuple(clean),
        "vectors": vectors,
        "clean_names_sha256":
            digest(tuple(row["names"] for row in clean)),
        "forecast_table_sha256": digest({
            "open_keys": open_keys,
            "clean_names": tuple(row["names"] for row in clean),
            "forecasts": tuple(row["forecast"] for row in clean),
        }),
    }


def score_hypotheses(
    hypotheses: dict[str, object],
    resolutions: tuple[dict[str, object], ...],
) -> dict[str, object]:
    open_index = {
        key: index for index, key in enumerate(hypotheses["open_keys"])
    }
    survivors = set(range(len(hypotheses["clean"])))
    rows = []
    total_predictions = 0
    for resolution in sorted(
        resolutions,
        key=lambda row: (row["resolution_moment"], row["key"]),
    ):
        key = resolution["key"]
        observed = resolution["outcome"]
        index = open_index[key]
        predictions = tuple(
            hypothesis["forecast"][index]
            for hypothesis in hypotheses["clean"]
        )
        correct = sum(value == observed for value in predictions)
        wrong = len(predictions) - correct
        total_predictions += len(predictions)
        survivors &= {
            hypothesis_index
            for hypothesis_index, prediction in enumerate(predictions)
            if prediction == observed
        }
        surviving_vectors = {
            hypotheses["clean"][hypothesis_index]["forecast"]
            for hypothesis_index in survivors
        }
        rows.append({
            "key": key,
            "resolution_moment": resolution["resolution_moment"],
            "outcome": observed,
            "correct": correct,
            "wrong": wrong,
            "prediction_census": {
                label: predictions.count(label)
                for label in ("TRANSIENT", "CYCLE", "UNSEEN")
            },
            "prediction_sha256": digest(predictions),
            "surviving_separators": len(survivors),
            "surviving_vectors": len(surviving_vectors),
        })
    scoring_table = tuple((
        row["key"],
        row["resolution_moment"],
        row["outcome"],
        row["correct"],
        row["wrong"],
        row["surviving_separators"],
        row["surviving_vectors"],
    ) for row in rows)
    return {
        "rule": "prediction == observed; UNSEEN is WRONG",
        "rows": tuple(rows),
        "scoring_table": scoring_table,
        "total_predictions": total_predictions,
        "initial_separator_count": len(hypotheses["clean"]),
        "initial_vector_count": len(hypotheses["vectors"]),
        "final_surviving_separator_count": len(survivors),
        "final_surviving_vector_count": len({
            hypotheses["clean"][index]["forecast"]
            for index in survivors
        }),
        "score_sha256": digest(tuple(rows)),
    }


def render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = [
        f"{'PASS' if passed else 'FAIL'} {label}"
        for label, passed in checks.items()
    ]
    lines.extend(
        f"FINDING {label} {compact(value)}"
        for label, value in certificates.items()
    )
    lines.append("SUMMARY_JSON " + compact(report))
    lines.append(str(report["terminal"]))
    return "\n".join(lines) + "\n"


def stable_output(
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
    controls_base: bool,
) -> str:
    for _attempt in range(20):
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        if not (
            checks["1_RESOLUTION_VERIFICATION"]
            and checks["2_THE_SHARED_MOMENT"]
        ):
            report["headline"] = "REFUTED_WRONG_RESOLUTION"
        elif report["surviving_vector_count"] != 0:
            report["headline"] = "REFUTED_SURVIVING_FORECAST_VECTOR"
        elif report["pass"]:
            report["headline"] = (
                "PRIMARY_SURVIVES_ALL_FIVE_ADVERSARIAL_ATTACKS"
            )
        else:
            report["headline"] = "PRIMARY_NOT_CERTIFIED_CONTROL_FAILURE"
        report["terminal"] = (
            "CYCLE819_CONTINUATION_INDEPENDENT_CHECK_PASS"
            if report["pass"]
            else "CYCLE819_CONTINUATION_INDEPENDENT_CHECK_HONEST_FAIL"
        )
        output = render(checks, certificates, report)
        size = len(output.encode("utf-8"))
        stdout_ok = size < STDOUT_LIMIT_BYTES
        controls = certificates["5_CONTROLS"]
        stable = (
            controls["stdout_bytes"] == size
            and report["stdout_bytes"] == size
            and checks["5_CONTROLS"] == (controls_base and stdout_ok)
        )
        controls["stdout_bytes"] = size
        controls["stdout_within_limit"] = stdout_ok
        report["stdout_bytes"] = size
        checks["5_CONTROLS"] = controls_base and stdout_ok
        if stable:
            return output
    raise AssertionError("stdout byte fixed point failed")


def run() -> int:
    started = monotonic()
    checks: dict[str, bool] = {}
    certificates: dict[str, object] = {}

    sources = source_certificate()
    family = build_family()
    feature_table = reconstruct_feature_table(family)
    hypotheses = reconstruct_hypotheses(feature_table)

    transient_rows = tuple(
        scan_first_clean(key, family, SHARED_MOMENT)
        for key in CLAIMED_TRANSIENTS
    )
    cycle_rows = tuple(
        scan_cycle(key, family, entry, period)
        for key, (entry, period) in CLAIMED_CYCLES.items()
    )

    detailed_transients = tuple(
        row for row in transient_rows if row["declared_detail"]
    )
    resolution_pass = (
        len(detailed_transients) == 5
        and {row["key"] for row in detailed_transients}
        == set(DECLARED_TRANSIENT_DETAIL_KEYS)
        and all(row["pass"] for row in detailed_transients)
        and len(cycle_rows) == 2
        and all(row["pass"] for row in cycle_rows)
    )
    checks["1_RESOLUTION_VERIFICATION"] = resolution_pass
    certificates["1_RESOLUTION_VERIFICATION"] = {
        "declared_transient_choice": DECLARED_TRANSIENT_DETAIL_KEYS,
        "transients": detailed_transients,
        "cycles": cycle_rows,
        "finding": (
            "five declared transients are nonclean at every earlier "
            "moment, clean first at 14744, vetoed at t-1, and carry "
            "the exact -1..+6 landed window; both cycles recur exactly "
            "with all proper divisors rejected and no clean phase"
        ),
    }

    shared_pass = (
        len(transient_rows) == 9
        and tuple(row["key"] for row in transient_rows)
        == CLAIMED_TRANSIENTS
        and all(row["pass"] for row in transient_rows)
        and {
            row["observed_first_clean"] for row in transient_rows
        } == {SHARED_MOMENT}
    )
    checks["2_THE_SHARED_MOMENT"] = shared_pass
    certificates["2_THE_SHARED_MOMENT"] = {
        "scan_method": (
            "nine independent scalar integer-state evolutions; every "
            "integer update inspected, no stride or scan granularity"
        ),
        "rows": tuple({
            "key": row["key"],
            "observed_first_clean": row["observed_first_clean"],
            "earlier_times_checked": row["earlier_times_checked"],
            "all_earlier_times_nonclean":
                row["all_earlier_times_nonclean"],
            "pass": row["pass"],
        } for row in transient_rows),
        "coincidence_multiplicity": sum(
            row["observed_first_clean"] == SHARED_MOMENT
            for row in transient_rows
        ),
        "finding": "the nine-fold first-clean coincidence is exactly t=14744",
    }

    resolutions = tuple(
        {
            "key": row["key"],
            "outcome": "TRANSIENT",
            "resolution_moment": row["observed_first_clean"],
            "verification_pass": row["pass"],
        }
        for row in transient_rows
    ) + tuple(
        {
            "key": row["key"],
            "outcome": "CYCLE",
            "resolution_moment": row["claimed_closure"],
            "verification_pass": row["pass"],
        }
        for row in cycle_rows
    )
    scores = score_hypotheses(hypotheses, resolutions)
    resolved_keys = {row["key"] for row in resolutions}
    domain_rows = tuple({
        "key": key,
        "in_176_key_family": key in family["states"],
        "in_cycle795_k2_open_domain": key in hypotheses["open_keys"],
        "two_distinct_positions": (
            len(key[1]) == 2 and len(set(key[1])) == 2
        ),
        "separated_pair": key[1] in family["positions"],
    } for key in sorted(resolved_keys))
    all_in_domain = (
        len(domain_rows) == 11
        and all(
            row["in_176_key_family"]
            and row["in_cycle795_k2_open_domain"]
            and row["two_distinct_positions"]
            and row["separated_pair"]
            for row in domain_rows
        )
    )
    scoring_pass = (
        len(FEATURE_SCHEMA) == len(set(FEATURE_SCHEMA)) == 89
        and len(PAIR_FEATURES) == len(set(PAIR_FEATURES)) == 24
        and feature_table["table_sha256"]
        == EXPECTED_FEATURE_TABLE_SHA256
        and len(hypotheses["candidates"]) == 365
        and len(hypotheses["clean"]) == 103
        and hypotheses["clean_names_sha256"]
        == EXPECTED_CLEAN_NAMES_SHA256
        and len(hypotheses["vectors"]) == 46
        and len(hypotheses["open_keys"]) == 162
        and all_in_domain
        and len(scores["rows"]) == 11
        and scores["total_predictions"] == 103 * 11
        and all(
            row["correct"] + row["wrong"] == 103
            for row in scores["rows"]
        )
        and scores["scoring_table"] == EXPECTED_SCORING_TABLE
        and scores["initial_vector_count"] == 46
        and scores["final_surviving_separator_count"] == 0
        and scores["final_surviving_vector_count"] == 0
    )
    checks["3_THE_FORECAST_SCORING"] = scoring_pass
    certificates["3_THE_FORECAST_SCORING"] = {
        "definition_source":
            "Cycle-795 SHA-pinned text/AST only; definitions reimplemented",
        "feature_count": len(FEATURE_SCHEMA),
        "pair_basis_count": len(PAIR_FEATURES),
        "candidate_count": len(hypotheses["candidates"]),
        "feature_table_sha256": feature_table["table_sha256"],
        "clean_separator_count": len(hypotheses["clean"]),
        "clean_names_sha256": hypotheses["clean_names_sha256"],
        "forecast_vector_count": len(hypotheses["vectors"]),
        "forecast_table_sha256": hypotheses["forecast_table_sha256"],
        "domain_rows": domain_rows,
        "every_resolved_key_in_domain": all_in_domain,
        "scoring_rule": scores["rule"],
        "per_resolution_C_W_tables": scores["rows"],
        "pinned_scoring_table_match":
            scores["scoring_table"] == EXPECTED_SCORING_TABLE,
        "total_predictions": scores["total_predictions"],
        "surviving_vectors": (
            scores["initial_vector_count"],
            scores["final_surviving_vector_count"],
        ),
        "surviving_separators":
            scores["final_surviving_separator_count"],
        "score_sha256": scores["score_sha256"],
        "finding": "all 103 hypotheses score on all 11 in-domain resolutions",
    }

    remaining_open = tuple(
        key for key in hypotheses["open_keys"] if key not in resolved_keys
    )
    null_rows = tuple(
        scan_open_key(key, family, TARGET_HORIZON)
        for key in DECLARED_NULL_KEYS
    )
    null_pass = (
        len(remaining_open) == 151
        and len(null_rows) == 8
        and set(DECLARED_NULL_KEYS) <= set(remaining_open)
        and all(row["pass"] for row in null_rows)
    )
    checks["4_NULL_SPOT_COVERAGE"] = null_pass
    certificates["4_NULL_SPOT_COVERAGE"] = {
        "remaining_open_key_count": len(remaining_open),
        "declared_spot_keys": DECLARED_NULL_KEYS,
        "rows": null_rows,
        "event_definition": "first clean or exact full-state recurrence",
        "event_count": sum(len(row["events"]) for row in null_rows),
        "finding": "eight declared remaining keys have zero events through T=16384",
    }

    null_by_key = {row["key"]: row for row in null_rows}
    replay_rows = tuple({
        "key": key,
        "first_scan": null_by_key[key]["boundaries"],
        "replay": replay_boundaries(key, family, TARGET_HORIZON),
    } for key in DECLARED_DETERMINISM_SLICE)
    deterministic = all(
        row["first_scan"] == row["replay"] for row in replay_rows
    )
    elapsed = monotonic() - started
    controls_base = (
        sources["pass"]
        and family["summary"]["pass"]
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and not any(
            name in sys.modules for name in BLOCKLISTED_MODULES
        )
        and not IMPORT_FIREWALL.hits
    )
    checks["5_CONTROLS"] = controls_base
    certificates["5_CONTROLS"] = {
        **sources,
        "family_reconstruction": family["summary"],
        "determinism_slice": {
            "declaration": (
                "two declared null-coverage keys replayed independently "
                "from t=0 to T=16384; exact state/support boundary rows "
                "compared at 4096, 8192, and 16384"
            ),
            "keys": DECLARED_DETERMINISM_SLICE,
            "rows": replay_rows,
            "deterministic": deterministic,
        },
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(IMPORT_FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_within_limit": False,
    }

    report = {
        "cycle": 819,
        "resolved_transients": sum(
            row["pass"] for row in transient_rows
        ),
        "resolved_cycles": sum(row["pass"] for row in cycle_rows),
        "shared_first_clean_moment": SHARED_MOMENT,
        "open_keys_after_resolutions": len(remaining_open),
        "forecast_hypotheses": len(hypotheses["clean"]),
        "forecast_vectors_before": scores["initial_vector_count"],
        "surviving_vector_count":
            scores["final_surviving_vector_count"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "headline": "",
        "terminal": "",
    }
    output = stable_output(
        checks, certificates, report, controls_base
    )
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit exceeded after fixed point")
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        failure = {
            "pass": False,
            "headline": "PRIMARY_NOT_CERTIFIED_CHECKER_EXCEPTION",
            "terminal":
                "CYCLE819_CONTINUATION_INDEPENDENT_CHECK_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
