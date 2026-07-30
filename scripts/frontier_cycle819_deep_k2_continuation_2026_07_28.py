#!/usr/bin/env python3
"""Cycle 819: deep in-domain k=2 continuation and forecast tests.

The Cycle-795, Cycle-797, and Cycle-816 primaries are SHA-pinned text/AST
references only.  They are blocklisted from import and execution.  This
single runner executes only the landed Cycle-719 controller core, independently
reconstructs the 176-key k=2 family and the exact 103-separator/46-vector
Cycle-795 forecast class, and continues every key open through T=4096 to the
deepest complete power-of-two horizon admitted by the measured budget.

Every landed-clean event is verified by exact per-moment re-evolution, and
every cycle is verified by exact recurrence with a proper-divisor minimality
check.  UNSEEN is a wrong forecast for either resolved binary outcome.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle795_discriminator_census_2026_07_28.py",
    "scripts/frontier_cycle797_deep_horizon_continuation_2026_07_28.py",
    "scripts/frontier_cycle816_first_forecast_test_2026_07_28.py",
)

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import prod
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
        "7ece6f7c818a4dcffb3019c610ca0861998f19cfae0287e23fe98562c1a09698",
    AUDIT_INPUT_PATHS[3]:
        "9655e17fed30caf5d8b921a8674fde0897c286c99918214447893a50e21dfee2",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "45afe5159562f28bb9edebf7340b582408ad4ba7",
    AUDIT_INPUT_PATHS[2]: "5d70ba232efcbd4f8c0a2d798f735907d4207b81",
    AUDIT_INPUT_PATHS[3]: "bdc3231ecfdd5edd9e0c4bb9fa85bee43037ad20",
}
REFERENCE_COMMITS = {
    "cycle795_primary":
        "6427de5c6bdd1e1f7939bac7855e1e188d28daef",
    "cycle797_primary":
        "3cf5931aa9",
    "cycle816_primary":
        "5a5b032bdd",
}


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Fail closed if a text/AST-only predecessor is imported."""

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


RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
BASELINE_HORIZON = 4096
TARGET_HORIZON = 16384
POWER_BOUNDARIES = (4096, 8192, 16384)
BUDGET_DECISION_LIMIT_SEC = 1320
BUDGET_SAFETY_FACTOR = 1.35
BUDGET_RESERVE_SEC = 60.0
DETERMINISM_SLICE_SIZE = 8
EXPECTED_OPEN_SIZE = 162
EXPECTED_SEPARATOR_COUNT = 103
EXPECTED_FORECAST_VECTOR_COUNT = 46
LANDED_CONSTANTS = (130, 11, 2, 5, 12, 288, 6, 3)
EXPECTED_PRIMARY_TABLE_SHA256 = (
    "266dd5f0c36cb79eb88a143c303e31ef1f79b068d6131545962ee38f8d24e705"
)
EXPECTED_CLEAN_NAMES_SHA256 = (
    "dc265dc602faef161bf1483f95810396fe3c4dfa75e7afb1cf9f871a396e6d91"
)
EXPECTED_TRANSIENTS = {
    (3, (1, 10)): 252,
    (3, (0, 7)): 371,
}
EXPECTED_CYCLES = {
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

Coordinate = tuple[str, str, int]
Support = frozenset[Coordinate]
Key = tuple[int, tuple[int, int]]


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
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
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    direct_frontier_imports = {
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    }
    primary795_names = function_names(trees[AUDIT_INPUT_PATHS[1]])
    primary797_names = function_names(trees[AUDIT_INPUT_PATHS[2]])
    primary816_names = function_names(trees[AUDIT_INPUT_PATHS[3]])
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
        "git_blobs": actual_blobs,
        "expected_sha256": EXPECTED_SHA256,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "reference_commits": REFERENCE_COMMITS,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(IMPORT_FIREWALL.hits),
        "direct_frontier_imports": tuple(sorted(direct_frontier_imports)),
        "cycle795_AST_basis": {
            "feature_schema",
            "feature_table",
            "candidate_result",
            "discrimination_census",
        } <= primary795_names,
        "cycle797_AST_basis": {
            "run_continuation",
            "resolution_rows",
            "hypothesis_table",
        } <= primary797_names,
        "cycle816_AST_basis": {
            "source_certificate",
            "separator_reconstruction",
            "prospective_test",
        } <= primary816_names,
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "maximum_named_files": 7,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and direct_frontier_imports == {
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
        }
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and result["cycle795_AST_basis"]
        and result["cycle797_AST_basis"]
        and result["cycle816_AST_basis"]
        and len(AUDIT_INPUT_PATHS) <= 7
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


def synchronous_word(
    program: tuple[object, ...],
    positions0: tuple[int, int],
) -> tuple[object, ...]:
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


def compile_word(
    word: tuple[object, ...],
) -> tuple[tuple[int, int, int, int], ...]:
    """Compile landed gates to a small bit-slice instruction tuple."""

    rows = []
    for gate in word:
        if gate.kind == "X":
            rows.append((0, gate.wires[0], 0, 0))
        elif gate.kind == "CNOT":
            rows.append((1, gate.wires[0], gate.wires[1], 0))
        elif gate.kind == "TOF":
            rows.append((
                2,
                gate.wires[0],
                gate.wires[1],
                gate.wires[2],
            ))
        else:
            raise ValueError(("unsupported landed gate", gate))
    return tuple(rows)


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


def residual_support(state: tuple[int, ...]) -> Support:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    rows: set[Coordinate] = set()
    if state[K.R3.X.SOURCE_POINTER]:
        rows.add(("source", "SOURCE_POINTER", 0))
    for bank_index, bank in enumerate(banks):
        for register_name, wire in watched_registers():
            if bank[wire]:
                rows.add(("bank", register_name, bank_index))
    for link_index, link in enumerate(links):
        for wire_index, bit in enumerate(link):
            if bit:
                rows.add(("link", f"WIRE_{wire_index}", link_index))
    return frozenset(rows)


def canonical_support(support: Support) -> tuple[Coordinate, ...]:
    return tuple(sorted(support))


def build_family() -> dict[str, object]:
    started = monotonic()
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs = []
    epoch_failures = 0
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        epoch_failures += after != K.A.apply_semantic(before, allocator)
        epoch_failures += rail_a != (1,) + (0,) * (len(program) - 1)
        epoch_failures += any(rail_b)
        epoch_failures += len(trace) != len(program)
        epochs.append((event, direction, before))
        state = after

    positions = separated_pairs()
    words = {
        positions0: synchronous_word(program, positions0)
        for positions0 in positions
    }
    compiled_words = {
        positions0: compile_word(words[positions0])
        for positions0 in positions
    }
    states: dict[Key, tuple[int, ...]] = {}
    supports: dict[Key, Support] = {}
    composition_failures = 0
    rail_failures = 0
    inverse_failures = 0
    for event, _direction, before in epochs:
        for positions0 in positions:
            after, rail_a, rail_b, _trace = K.run_orbit(
                before, program, token_positions=positions0
            )
            expected_rail = tuple(
                int(station in positions0)
                for station in range(RING_STATIONS)
            )
            restored, inverse_a, inverse_b, _ = K.run_orbit(
                after,
                program,
                token_positions=positions0,
                reverse=True,
            )
            composition_failures += (
                after != K.A.apply_semantic(before, words[positions0])
            )
            rail_failures += rail_a != expected_rail or any(rail_b)
            inverse_failures += (
                restored != before
                or inverse_a != rail_a
                or inverse_b != rail_b
            )
            key = (event, positions0)
            states[key] = after
            supports[key] = residual_support(after)

    unique_supports = set(supports.values())
    summary = {
        "epochs": len(epochs),
        "directions": tuple(row[1] for row in epochs),
        "program_stations": len(program),
        "positions": len(positions),
        "keys": len(states),
        "unique_frozen_signatures": len(unique_supports),
        "unique_signatures_by_epoch": tuple(
            len({
                supports[(event, positions0)]
                for positions0 in positions
            })
            for event in range(2 * FIXTURE_BANKS)
        ),
        "epoch_failures": epoch_failures,
        "composition_failures": composition_failures,
        "rail_return_failures": rail_failures,
        "literal_inverse_failures": inverse_failures,
        "all_frozen_residues_nonzero": all(supports.values()),
        "family_sha256": digest(tuple(
            (key, canonical_support(supports[key]))
            for key in sorted(supports)
        )),
        "runtime_seconds": round(monotonic() - started, 6),
    }
    summary["pass"] = (
        summary["epochs"] == 4
        and summary["directions"]
        == ((1, 0), (0, 1), (1, 0), (0, 1))
        and summary["program_stations"] == RING_STATIONS
        and summary["positions"] == 44
        and summary["keys"] == FAMILY_SIZE
        and summary["unique_frozen_signatures"] == 25
        and summary["unique_signatures_by_epoch"] == (1, 1, 12, 14)
        and summary["epoch_failures"] == 0
        and summary["composition_failures"] == 0
        and summary["rail_return_failures"] == 0
        and summary["literal_inverse_failures"] == 0
        and summary["all_frozen_residues_nonzero"]
    )
    return {
        "program": program,
        "epochs": tuple(epochs),
        "positions": positions,
        "words": words,
        "compiled_words": compiled_words,
        "states": states,
        "supports": supports,
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


def support_statistics(support: Support) -> dict[str, int]:
    source_count = sum(row[0] == "source" for row in support)
    bank_count = sum(row[0] == "bank" for row in support)
    link_count = sum(row[0] == "link" for row in support)
    bank0_count = sum(
        row[0] == "bank" and row[2] == 0 for row in support
    )
    bank1_count = sum(
        row[0] == "bank" and row[2] == 1 for row in support
    )
    return {
        "source_count": source_count,
        "bank_count": bank_count,
        "link_count": link_count,
        "bank0_count": bank0_count,
        "bank1_count": bank1_count,
        "kind_mask": (
            int(source_count > 0)
            + 2 * int(bank_count > 0)
            + 4 * int(link_count > 0)
        ),
        "coordinate_index_sum": sum(row[2] for row in support),
    }


def named_features(
    event: int,
    positions: tuple[int, int],
    direction: tuple[int, int],
    support: Support,
    support_classes: dict[Support, int],
) -> dict[str, Any]:
    left, right = positions
    clockwise = (right - left) % RING_STATIONS
    counterclockwise = (left - right) % RING_STATIONS
    separation = min(clockwise, counterclockwise)
    short_orientation = 1 if clockwise < counterclockwise else -1
    epoch_direction = 1 if direction == (1, 0) else -1
    position_sum = sum(positions)
    stats = support_statistics(support)
    named: dict[str, Any] = {
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
        "position_product": prod(positions),
        "occupancy_mask": sum(1 << position for position in positions),
        "chord_midpoint_mod11":
            (pow(len(positions), -1, RING_STATIONS) * position_sum)
            % RING_STATIONS,
        "short_arc_start": left if short_orientation == 1 else right,
        "short_arc_end": right if short_orientation == 1 else left,
        "left_parity": left % 2,
        "right_parity": right % 2,
        "parity_code": 2 * (left % 2) + right % 2,
        "same_position_parity":
            int(len({position % 2 for position in positions}) == 1),
        "epoch_sum_parity": (event + position_sum) % 2,
        "initial_residual_weight": len(support),
        "initial_support_size": len(support),
        "support_signature_id": support_classes[support],
        "support_kind_mask": stats["kind_mask"],
        "support_source_count": stats["source_count"],
        "support_bank_count": stats["bank_count"],
        "support_link_count": stats["link_count"],
        "support_bank0_count": stats["bank0_count"],
        "support_bank1_count": stats["bank1_count"],
        "support_bank_imbalance":
            stats["bank1_count"] - stats["bank0_count"],
        "support_coordinate_index_sum": stats["coordinate_index_sum"],
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
                int(
                    len({
                        position % modulus for position in positions
                    }) == 1
                ),
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
        support: identifier
        for identifier, support in enumerate(
            sorted(
                set(family["supports"].values()),
                key=canonical_support,
            )
        )
    }
    features: dict[Key, dict[str, Any]] = {}
    rows = []
    for key in sorted(family["states"]):
        event, positions = key
        named = named_features(
            event,
            positions,
            directions[event],
            family["supports"][key],
            support_classes,
        )
        features[key] = named
        rows.append(
            (event, positions[0], positions[1])
            + tuple(named[name] for name in FEATURE_SCHEMA)
        )
    return {
        "features": features,
        "rows": tuple(rows),
        "support_classes": support_classes,
        "table_sha256": digest(tuple(rows)),
    }


def projection(
    features: dict[str, Any],
    names: tuple[str, ...],
) -> tuple[Any, ...]:
    return tuple(features[name] for name in names)


def forecast_side(
    value: tuple[Any, ...],
    transient_values: set[tuple[Any, ...]],
    cycle_values: set[tuple[Any, ...]],
) -> str:
    if value in transient_values and value not in cycle_values:
        return "TRANSIENT"
    if value in cycle_values and value not in transient_values:
        return "CYCLE"
    return "UNSEEN"


def separator_reconstruction(
    feature_table: dict[str, object],
) -> dict[str, object]:
    features = feature_table["features"]
    transient_keys = tuple(sorted(EXPECTED_TRANSIENTS))
    cycle_keys = tuple(sorted(EXPECTED_CYCLES))
    open_keys = tuple(
        sorted(set(features) - set(transient_keys) - set(cycle_keys))
    )
    candidate_names = (
        tuple((name,) for name in FEATURE_SCHEMA)
        + tuple(combinations(PAIR_FEATURES, 2))
    )
    clean = []
    for names in candidate_names:
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
            sum(
                abs(left - right)
                for left, right in zip(tvalue, cvalue)
            )
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
                sum(side != "UNSEEN" for side in forecast),
        })
    clean.sort(
        key=lambda row: (
            -row["open_classified"],
            len(row["names"]),
            -row["margin"],
            row["names"],
        )
    )
    sequences = tuple(sorted({row["forecast"] for row in clean}))
    vector_by_sequence = {
        sequence: f"V{index:02d}"
        for index, sequence in enumerate(sequences)
    }
    rows = []
    for index, hypothesis in enumerate(clean):
        rows.append({
            "separator_id": f"S{index:03d}",
            "features": hypothesis["names"],
            "vector_id": vector_by_sequence[hypothesis["forecast"]],
            "margin_L1": hypothesis["margin"],
            "open_classified": hypothesis["open_classified"],
            "forecast_sha256": digest(hypothesis["forecast"]),
        })
    return {
        "open_keys": open_keys,
        "candidate_names": candidate_names,
        "clean": tuple(clean),
        "separator_catalog": tuple(rows),
        "clean_names_sha256":
            digest(tuple(row["names"] for row in clean)),
        "forecast_vector_count": len(sequences),
        "forecast_vectors": tuple({
            "vector_id": vector_by_sequence[sequence],
            "forecast_sha256": digest(sequence),
            "separator_ids": tuple(
                f"S{index:03d}"
                for index, row in enumerate(clean)
                if row["forecast"] == sequence
            ),
            "implication_counts": {
                label: sequence.count(label)
                for label in ("TRANSIENT", "CYCLE", "UNSEEN")
            },
        } for sequence in sequences),
        "forecast_table_sha256": digest({
            "open_keys": open_keys,
            "clean_names": tuple(row["names"] for row in clean),
            "forecasts": tuple(row["forecast"] for row in clean),
        }),
    }


def state_sha256(state: tuple[int, ...]) -> str:
    return sha256(bytes(state)).hexdigest()


def state_token(state: tuple[int, ...]) -> int:
    """Compact lookup token; every hit is confirmed by exact state equality."""

    return int.from_bytes(
        sha256(bytes(state)).digest()[:8], "big"
    )


def exact_state_at(
    state0: tuple[int, ...],
    word: tuple[object, ...],
    update: int,
) -> tuple[int, ...]:
    state = state0
    for _step in range(update):
        state = K.A.apply_semantic(state, word)
    return state


def find_exact_entry(
    state0: tuple[int, ...],
    word: tuple[object, ...],
    repeated_state: tuple[int, ...],
    token: int,
    closure: int,
) -> int | None:
    """Scan the bounded prefix only after a token hit; compare exact states."""

    candidate = state0
    for entry in range(closure):
        if state_token(candidate) == token and candidate == repeated_state:
            return entry
        candidate = K.A.apply_semantic(candidate, word)
    return None


def proper_divisors(value: int) -> tuple[int, ...]:
    return tuple(
        candidate
        for candidate in range(1, value)
        if value % candidate == 0
    )


def minimal_phase_period(phases: tuple[Support, ...]) -> int:
    length = len(phases)
    for candidate in range(1, length + 1):
        if length % candidate:
            continue
        if all(
            phases[index] == phases[index % candidate]
            for index in range(length)
        ):
            return candidate
    raise AssertionError(("no finite-word period", length))


def verify_transient(
    state0: tuple[int, ...],
    word: tuple[object, ...],
    moment: int,
    observed_state: tuple[int, ...],
) -> dict[str, object]:
    state = state0
    supports = [residual_support(state)]
    states = [state]
    for _update in range(1, moment + 3):
        state = K.A.apply_semantic(state, word)
        states.append(state)
        supports.append(residual_support(state))
    window_start = max(0, moment - 2)
    window_stop = moment + 2
    window = tuple(
        {
            "moment": update,
            "support_weight": len(supports[update]),
            "landed_clean": not supports[update],
            "support_sha256":
                digest(canonical_support(supports[update])),
            "state_sha256": state_sha256(states[update]),
        }
        for update in range(window_start, window_stop + 1)
    )
    result = {
        "verification": "LANDED_PER_MOMENT_EXACT_REEVOLUTION",
        "moment": moment,
        "earlier_times_checked": moment,
        "earlier_times_nonclean": all(supports[:moment]),
        "event_is_clean": not supports[moment],
        "landed_veto_at_t_minus_1":
            bool(supports[moment - 1]) if moment else True,
        "observed_state_exact": states[moment] == observed_state,
        "window": window,
    }
    result["pass"] = (
        result["earlier_times_nonclean"]
        and result["event_is_clean"]
        and result["landed_veto_at_t_minus_1"]
        and result["observed_state_exact"]
        and sum(not support for support in supports[:moment]) == 0
    )
    return result


def verify_cycle(
    state0: tuple[int, ...],
    word: tuple[object, ...],
    entry: int,
    closure: int,
    observed_closure_state: tuple[int, ...],
) -> dict[str, object]:
    period = closure - entry
    entry_state = exact_state_at(state0, word, entry)
    state = entry_state
    phases = []
    divisor_returns: dict[int, bool] = {}
    divisor_set = set(proper_divisors(period))
    for step in range(period):
        phases.append(residual_support(state))
        state = K.A.apply_semantic(state, word)
        if step + 1 in divisor_set:
            divisor_returns[step + 1] = state == entry_state
    residual_period = minimal_phase_period(tuple(phases))
    result = {
        "verification": "EXACT_RECURRENCE_AND_PROPER_DIVISOR_MINIMALITY",
        "entry": entry,
        "closure": closure,
        "state_period": period,
        "residual_period": residual_period,
        "exact_recurrence": state == entry_state,
        "closure_state_exact": state == observed_closure_state,
        "proper_divisor_returns": tuple(sorted(divisor_returns.items())),
        "state_period_minimal":
            not any(divisor_returns.values()),
        "all_cycle_phases_nonclean": all(phases),
        "phase_count": len(phases),
        "phase_support_sha256": digest(tuple(
            canonical_support(phase) for phase in phases
        )),
    }
    result["pass"] = (
        period > 0
        and result["exact_recurrence"]
        and result["closure_state_exact"]
        and result["state_period_minimal"]
        and result["all_cycle_phases_nonclean"]
        and residual_period > 0
        and period % residual_period == 0
    )
    return result


def initialise_records(
    family: dict[str, object],
) -> dict[Key, dict[str, object]]:
    records = {}
    for key in sorted(family["states"]):
        state = family["states"][key]
        support = family["supports"][key]
        records[key] = {
            "state0": state,
            "state": state,
            "current_support": support,
            "seen_tokens": {state_token(state)},
            "first_clean": 0 if not support else None,
            "cycle_start": None,
            "state_period": None,
            "residual_period": None,
            "cycle_closure": None,
            "cycle_nonzero": None,
            "verification": None,
            "last_evolved": 0,
            "token_collisions": 0,
            "exact_recurrence_confirmations": 0,
            "boundary_controls": {},
        }
    return records


def terminal(record: dict[str, object]) -> bool:
    return (
        record["first_clean"] is not None
        or record["cycle_closure"] is not None
    )


def advance_one_key(
    record: dict[str, object],
    word: tuple[object, ...],
    end_update: int,
) -> int:
    transitions = 0
    for update in range(record["last_evolved"] + 1, end_update + 1):
        transitions += 1
        state = K.A.apply_semantic(record["state"], word)
        support = residual_support(state)
        if observe_state(record, word, update, state, support):
            break
    return transitions


def observe_state(
    record: dict[str, object],
    word: tuple[object, ...],
    update: int,
    state: tuple[int, ...],
    support: Support,
) -> bool:
    record["state"] = state
    record["current_support"] = support
    record["last_evolved"] = update
    if not support:
        record["first_clean"] = update
        record["verification"] = verify_transient(
            record["state0"], word, update, state
        )
        return True

    token = state_token(state)
    if token not in record["seen_tokens"]:
        record["seen_tokens"].add(token)
        return False
    exact_entry = find_exact_entry(
        record["state0"], word, state, token, update
    )
    if exact_entry is None:
        record["token_collisions"] += 1
        return False

    cycle_verification = verify_cycle(
        record["state0"],
        word,
        exact_entry,
        update,
        state,
    )
    record["cycle_start"] = exact_entry
    record["state_period"] = cycle_verification["state_period"]
    record["residual_period"] = cycle_verification["residual_period"]
    record["cycle_closure"] = update
    record["cycle_nonzero"] = (
        cycle_verification["all_cycle_phases_nonclean"]
    )
    record["verification"] = cycle_verification
    record["exact_recurrence_confirmations"] += 1
    return True


def bit_slice(
    states: tuple[tuple[int, ...], ...],
) -> list[int]:
    if not states:
        return []
    return [
        sum(state[wire] << index for index, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def un_slice(
    columns: list[int],
    index: int,
) -> tuple[int, ...]:
    return tuple((column >> index) & 1 for column in columns)


def apply_compiled_bit_slice(
    columns: list[int],
    operations: tuple[tuple[int, int, int, int], ...],
    width: int,
) -> None:
    mask = (1 << width) - 1
    for kind, first, second, third in operations:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first]
        else:
            columns[third] ^= columns[first] & columns[second]


def bit_slice_equivalence_certificate(
    family: dict[str, object],
) -> dict[str, object]:
    rows = []
    for positions in family["positions"]:
        keys = tuple((event, positions) for event in range(4))
        states = tuple(family["states"][key] for key in keys)
        columns = bit_slice(states)
        apply_compiled_bit_slice(
            columns, family["compiled_words"][positions], len(states)
        )
        observed = tuple(
            un_slice(columns, index) for index in range(len(states))
        )
        expected = tuple(
            K.A.apply_semantic(state, family["words"][positions])
            for state in states
        )
        rows.append({
            "positions": positions,
            "keys": len(keys),
            "word_gates": len(family["words"][positions]),
            "exact": observed == expected,
            "observed_sha256": digest(tuple(
                state_sha256(state) for state in observed
            )),
            "expected_sha256": digest(tuple(
                state_sha256(state) for state in expected
            )),
        })
    return {
        "basis": (
            "all 44 position-words, all four event states, one exact "
            "landed step: bit-sliced X/CNOT/TOF equals scalar apply_semantic"
        ),
        "rows": tuple(rows),
        "row_sha256": digest(tuple(rows)),
        "pass": len(rows) == 44 and all(row["exact"] for row in rows),
    }


def advance_key_group(
    records: dict[Key, dict[str, object]],
    keys: tuple[Key, ...],
    word: tuple[object, ...],
    operations: tuple[tuple[int, int, int, int], ...],
    end_update: int,
) -> int:
    active = list(keys)
    if not active:
        return 0
    update = records[active[0]]["last_evolved"]
    columns = bit_slice(tuple(records[key]["state"] for key in active))
    transitions = 0
    while active and update < end_update:
        update += 1
        apply_compiled_bit_slice(columns, operations, len(active))
        next_active = []
        for index, key in enumerate(active):
            state = un_slice(columns, index)
            support = residual_support(state)
            transitions += 1
            if not observe_state(
                records[key], word, update, state, support
            ):
                next_active.append(key)
        if len(next_active) != len(active):
            active = next_active
            columns = bit_slice(tuple(
                records[key]["state"] for key in active
            ))
        else:
            active = next_active
    return transitions


def record_status(
    record: dict[str, object],
    horizon: int,
) -> str:
    if (
        record["first_clean"] is not None
        and record["first_clean"] <= horizon
    ):
        return f"FIRST_CLEAN(t={record['first_clean']})"
    if (
        record["cycle_closure"] is not None
        and record["cycle_closure"] <= horizon
    ):
        return (
            f"CYCLE(state_period={record['state_period']},"
            f"residual_period={record['residual_period']},"
            f"entry={record['cycle_start']},"
            f"closure={record['cycle_closure']})"
        )
    if record["last_evolved"] >= horizon:
        return f"OPEN_THROUGH_T={horizon}"
    return (
        f"UNMEASURED_AFTER_T={record['last_evolved']}"
        f"_FOR_REQUESTED_T={horizon}"
    )


def population_snapshot(
    records: dict[Key, dict[str, object]],
    horizon: int,
) -> dict[str, object]:
    clean = []
    cycles = []
    open_keys = []
    uncovered = []
    for key, record in sorted(records.items()):
        status = record_status(record, horizon)
        if status.startswith("FIRST_CLEAN"):
            clean.append(key)
        elif status.startswith("CYCLE"):
            cycles.append(key)
        elif status.startswith("OPEN_THROUGH"):
            open_keys.append(key)
        else:
            uncovered.append(key)
    return {
        "horizon": horizon,
        "keys": len(records),
        "transient_count": len(clean),
        "first_clean_time_census": dict(sorted(Counter(
            records[key]["first_clean"] for key in clean
        ).items())),
        "cycle_count": len(cycles),
        "state_period_census": dict(sorted(Counter(
            records[key]["state_period"] for key in cycles
        ).items())),
        "residual_period_census": dict(sorted(Counter(
            records[key]["residual_period"] for key in cycles
        ).items())),
        "open_count": len(open_keys),
        "uncovered_count": len(uncovered),
        "accounting_total":
            len(clean) + len(cycles) + len(open_keys) + len(uncovered),
        "all_certified_cycles_nonclean": all(
            records[key]["cycle_nonzero"] for key in cycles
        ),
        "clean_keys": tuple(clean),
        "cycle_keys": tuple(cycles),
        "open_keys": tuple(open_keys),
        "uncovered_keys": tuple(uncovered),
    }


def public_snapshot(snapshot: dict[str, object]) -> dict[str, object]:
    return {
        key: value
        for key, value in snapshot.items()
        if key not in {
            "clean_keys", "cycle_keys", "open_keys", "uncovered_keys"
        }
    }


def advance_population(
    records: dict[Key, dict[str, object]],
    words: dict[tuple[int, int], tuple[object, ...]],
    compiled_words: dict[
        tuple[int, int],
        tuple[tuple[int, int, int, int], ...],
    ],
    keys: tuple[Key, ...],
    start_horizon: int,
    end_horizon: int,
) -> dict[str, object]:
    started = monotonic()
    transitions = 0
    resolved = []
    active_before = tuple(
        key for key in keys if not terminal(records[key])
    )
    for key in active_before:
        record = records[key]
        if record["last_evolved"] != start_horizon:
            raise AssertionError((
                "non-boundary continuation start",
                key,
                record["last_evolved"],
                start_horizon,
            ))
    grouped = {
        positions: tuple(
            key for key in active_before if key[1] == positions
        )
        for positions in sorted({key[1] for key in active_before})
    }
    for positions, group in grouped.items():
        transitions += advance_key_group(
            records,
            group,
            words[positions],
            compiled_words[positions],
            end_horizon,
        )
    for key in active_before:
        record = records[key]
        if terminal(record):
            resolved.append(key)
        else:
            if record["last_evolved"] != end_horizon:
                raise AssertionError(("partial key", key, record))
            support = record["current_support"]
            record["boundary_controls"][end_horizon] = {
                "landed_clean": not support,
                "support_weight": len(support),
                "support_sha256": digest(canonical_support(support)),
                "state_sha256": state_sha256(record["state"]),
            }
    upper = len(active_before) * (end_horizon - start_horizon)
    result = {
        "start_horizon": start_horizon,
        "end_horizon": end_horizon,
        "active_keys_before": len(active_before),
        "active_key_sha256": digest(active_before),
        "transitions_executed": transitions,
        "transition_upper_if_no_terminals": upper,
        "transitions_saved_by_terminals": upper - transitions,
        "resolutions_in_phase": len(resolved),
        "resolved_keys": tuple(resolved),
        "complete_population": all(
            terminal(records[key])
            or records[key]["last_evolved"] == end_horizon
            for key in active_before
        ),
        "seconds": round(monotonic() - started, 6),
    }
    result["transitions_account"] = (
        result["transitions_executed"]
        + result["transitions_saved_by_terminals"]
        == result["transition_upper_if_no_terminals"]
    )
    return result


def choose_complete_horizon(
    script_started: float,
    baseline_phase: dict[str, object],
) -> dict[str, object]:
    elapsed = monotonic() - script_started
    transitions = baseline_phase["transitions_executed"]
    rate = baseline_phase["seconds"] / transitions if transitions else 0.0
    candidates = []
    chosen = BASELINE_HORIZON
    for candidate in (TARGET_HORIZON, 8192):
        future_upper = (
            EXPECTED_OPEN_SIZE * (candidate - BASELINE_HORIZON)
        )
        replay_upper = DETERMINISM_SLICE_SIZE * candidate
        projected = (
            elapsed
            + BUDGET_SAFETY_FACTOR
            * rate
            * (future_upper + replay_upper)
            + BUDGET_RESERVE_SEC
        )
        fits = projected < BUDGET_DECISION_LIMIT_SEC
        candidates.append({
            "horizon": candidate,
            "future_transition_upper": future_upper,
            "determinism_slice_transition_upper": replay_upper,
            "projected_total_seconds": round(projected, 6),
            "fits": fits,
        })
        if fits and chosen == BASELINE_HORIZON:
            chosen = candidate
    return {
        "policy": (
            "after complete T4096 reconstruction, choose deepest target "
            "power of two whose measured-rate projection includes every "
            "T4096-open key, the declared determinism slice, 1.35 safety, "
            "and 60s reserve; never start a rejected boundary"
        ),
        "target_horizon": TARGET_HORIZON,
        "measured_seconds_per_transition": round(rate, 12),
        "elapsed_at_decision_seconds": round(elapsed, 6),
        "safety_factor": BUDGET_SAFETY_FACTOR,
        "reserve_seconds": BUDGET_RESERVE_SEC,
        "decision_limit_seconds": BUDGET_DECISION_LIMIT_SEC,
        "candidate_decisions": tuple(candidates),
        "declared_complete_horizon": chosen,
        "target_fits": chosen == TARGET_HORIZON,
    }


def resolution_row(
    key: Key,
    record: dict[str, object],
) -> dict[str, object]:
    if record["first_clean"] is not None:
        return {
            "key": key,
            "outcome": "TRANSIENT",
            "resolution_moment": record["first_clean"],
            "first_clean": record["first_clean"],
            "cycle_entry": None,
            "state_period": None,
            "residual_period": None,
            "cycle_closure": None,
            "verification": record["verification"],
        }
    return {
        "key": key,
        "outcome": "CYCLE",
        "resolution_moment": record["cycle_closure"],
        "first_clean": None,
        "cycle_entry": record["cycle_start"],
        "state_period": record["state_period"],
        "residual_period": record["residual_period"],
        "cycle_closure": record["cycle_closure"],
        "verification": record["verification"],
    }


def boundary_ledger(
    records: dict[Key, dict[str, object]],
    baseline_open: tuple[Key, ...],
    horizons: tuple[int, ...],
) -> tuple[dict[str, object], ...]:
    ledgers = []
    for horizon in horizons:
        rows = []
        for key in baseline_open:
            record = records[key]
            status = record_status(record, horizon)
            row = {"key": key, "status": status}
            if status.startswith("OPEN_THROUGH"):
                row["landed_boundary_test"] = (
                    record["boundary_controls"][horizon]
                )
            rows.append(row)
        open_rows = tuple(
            row for row in rows
            if row["status"].startswith("OPEN_THROUGH")
        )
        ledgers.append({
            "horizon": horizon,
            "baseline_open_population": len(baseline_open),
            "rows": tuple(rows),
            "open_at_boundary": len(open_rows),
            "all_open_landed_nonclean": all(
                not row["landed_boundary_test"]["landed_clean"]
                and row["landed_boundary_test"]["support_weight"] > 0
                for row in open_rows
            ),
            "row_sha256": digest(tuple(rows)),
        })
    return tuple(ledgers)


def score_forecasts(
    separators: dict[str, object],
    resolutions: tuple[dict[str, object], ...],
) -> dict[str, object]:
    key_index = {
        key: index for index, key in enumerate(separators["open_keys"])
    }
    survivors = set(range(len(separators["clean"])))
    scoring_rows = []
    chronological = tuple(sorted(
        resolutions,
        key=lambda row: (row["resolution_moment"], row["key"]),
    ))
    for resolution in chronological:
        index = key_index[resolution["key"]]
        observed = resolution["outcome"]
        tests = []
        correct = []
        wrong = []
        for hypothesis_index, hypothesis in enumerate(separators["clean"]):
            separator_id = f"S{hypothesis_index:03d}"
            prediction = hypothesis["forecast"][index]
            passed = prediction == observed
            (correct if passed else wrong).append(separator_id)
            tests.append({
                "separator_id": separator_id,
                "prediction": prediction,
                "observed": observed,
                "result": "CORRECT" if passed else "WRONG",
            })
        survivors &= {
            hypothesis_index
            for hypothesis_index, hypothesis
            in enumerate(separators["clean"])
            if hypothesis["forecast"][index] == observed
        }
        surviving_vectors = {
            separators["clean"][hypothesis_index]["forecast"]
            for hypothesis_index in survivors
        }
        scoring_rows.append({
            "key": resolution["key"],
            "resolution_moment": resolution["resolution_moment"],
            "outcome": observed,
            "verification_pass": resolution["verification"]["pass"],
            "hypothesis_tests": tuple(tests),
            "correct_count": len(correct),
            "wrong_count": len(wrong),
            "correct_ids": tuple(correct),
            "wrong_ids": tuple(wrong),
            "surviving_separator_count": len(survivors),
            "surviving_vector_count": len(surviving_vectors),
            "surviving_separator_ids": tuple(
                f"S{index:03d}" for index in sorted(survivors)
            ),
        })
    return {
        "rule": (
            "prediction must equal observed binary outcome; UNSEEN is WRONG"
        ),
        "in_domain": True,
        "chronological_resolution_count": len(chronological),
        "rows": tuple(scoring_rows),
        "surviving_separator_count": len(survivors),
        "surviving_vector_count": len({
            separators["clean"][index]["forecast"]
            for index in survivors
        }),
        "score_sha256": digest(tuple(scoring_rows)),
    }


def replay_declared_slice(
    family: dict[str, object],
    keys: tuple[Key, ...],
    horizon: int,
    boundaries: tuple[int, ...],
) -> tuple[dict[str, object], ...]:
    row_by_key = {
        key: {"key": key, "boundaries": []}
        for key in keys
    }
    boundary_set = set(boundaries)
    for positions in sorted({key[1] for key in keys}):
        group = tuple(key for key in keys if key[1] == positions)
        columns = bit_slice(tuple(
            family["states"][key] for key in group
        ))
        for update in range(1, horizon + 1):
            apply_compiled_bit_slice(
                columns,
                family["compiled_words"][positions],
                len(group),
            )
            if update in boundary_set:
                for index, key in enumerate(group):
                    state = un_slice(columns, index)
                    support = residual_support(state)
                    row_by_key[key]["boundaries"].append({
                        "horizon": update,
                        "landed_clean": not support,
                        "support_weight": len(support),
                        "support_sha256":
                            digest(canonical_support(support)),
                        "state_sha256": state_sha256(state),
                    })
        for index, key in enumerate(group):
            row_by_key[key]["final_state_sha256"] = state_sha256(
                un_slice(columns, index)
            )
    return tuple({
        **row_by_key[key],
        "boundaries": tuple(row_by_key[key]["boundaries"]),
    } for key in keys)


def primary_slice_rows(
    records: dict[Key, dict[str, object]],
    keys: tuple[Key, ...],
    boundaries: tuple[int, ...],
) -> tuple[dict[str, object], ...]:
    return tuple({
        "key": key,
        "boundaries": tuple({
            "horizon": horizon,
            **records[key]["boundary_controls"][horizon],
        } for horizon in boundaries),
        "final_state_sha256": state_sha256(records[key]["state"]),
    } for key in keys)


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
        f"CERTIFICATE {label} {compact(value)}"
        for label, value in certificates.items()
    )
    lines.append("SUMMARY_JSON " + compact(report))
    lines.append(str(report["terminal"]))
    return "\n".join(lines) + "\n"


def stable_render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    for _attempt in range(20):
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE819_DEEP_K2_CONTINUATION_PASS"
            if report["pass"]
            else "CYCLE819_DEEP_K2_CONTINUATION_HONEST_FAIL"
        )
        output = render(checks, certificates, report)
        size = len(output.encode("utf-8"))
        controls = certificates["E_CONTROLS"]
        if report["stdout_bytes"] == size and controls["stdout_bytes"] == size:
            return output
        report["stdout_bytes"] = size
        controls["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    script_started = monotonic()
    checks: dict[str, bool] = {}
    certificates: dict[str, object] = {}

    sources = source_certificate()
    family = build_family()
    bit_slice_control = bit_slice_equivalence_certificate(family)
    feature_table = reconstruct_feature_table(family)
    separators = separator_reconstruction(feature_table)
    records = initialise_records(family)

    baseline_phase = advance_population(
        records,
        family["words"],
        family["compiled_words"],
        tuple(sorted(records)),
        0,
        BASELINE_HORIZON,
    )
    snapshot4096 = population_snapshot(records, BASELINE_HORIZON)
    baseline_open = tuple(snapshot4096["open_keys"])
    budget = choose_complete_horizon(script_started, baseline_phase)
    reached = budget["declared_complete_horizon"]
    phases = [baseline_phase]
    snapshots = {BASELINE_HORIZON: snapshot4096}
    prior = BASELINE_HORIZON
    for boundary in (8192, TARGET_HORIZON):
        if boundary > reached:
            continue
        phase = advance_population(
            records,
            family["words"],
            family["compiled_words"],
            tuple(snapshots[prior]["open_keys"]),
            prior,
            boundary,
        )
        phases.append(phase)
        snapshots[boundary] = population_snapshot(records, boundary)
        prior = boundary

    reached_boundaries = tuple(
        boundary for boundary in POWER_BOUNDARIES if boundary <= reached
    )
    boundary_rows = boundary_ledger(
        records, baseline_open, reached_boundaries
    )
    final_snapshot = snapshots[reached]
    new_resolutions = tuple(
        resolution_row(key, records[key])
        for key in baseline_open
        if terminal(records[key])
        and (
            records[key]["first_clean"]
            if records[key]["first_clean"] is not None
            else records[key]["cycle_closure"]
        ) > BASELINE_HORIZON
        and (
            records[key]["first_clean"]
            if records[key]["first_clean"] is not None
            else records[key]["cycle_closure"]
        ) <= reached
    )
    forecast_scores = score_forecasts(separators, new_resolutions)

    a_pass = (
        family["summary"]["pass"]
        and bit_slice_control["pass"]
        and snapshot4096["transient_count"] == 2
        and snapshot4096["cycle_count"] == 12
        and snapshot4096["open_count"] == EXPECTED_OPEN_SIZE
        and snapshot4096["uncovered_count"] == 0
        and baseline_open == separators["open_keys"]
        and reached in POWER_BOUNDARIES
        and all(phase["complete_population"] for phase in phases)
        and all(phase["transitions_account"] for phase in phases)
        and all(
            snapshots[horizon]["uncovered_count"] == 0
            and snapshots[horizon]["accounting_total"] == FAMILY_SIZE
            for horizon in reached_boundaries
        )
        and all(
            row["all_open_landed_nonclean"] for row in boundary_rows
        )
    )
    checks["A_DEEP_CONTINUATION_COMPLETE_BOUNDARIES"] = a_pass
    certificates["A_DEEP_CONTINUATION"] = {
        "baseline": "162 k=2 keys open through complete T=4096",
        "bit_slice_scalar_equivalence": bit_slice_control,
        "budget_decision": budget,
        "horizon_reached": reached,
        "target_reached": reached == TARGET_HORIZON,
        "complete_boundaries": reached_boundaries,
        "snapshots": tuple(
            public_snapshot(snapshots[horizon])
            for horizon in reached_boundaries
        ),
        "transition_accounting": tuple(phases),
        "boundary_landed_cleanliness_ledgers": boundary_rows,
        "final_open_key_sha256": digest(final_snapshot["open_keys"]),
    }

    b_pass = (
        len(FEATURE_SCHEMA) == len(set(FEATURE_SCHEMA)) == 89
        and len(PAIR_FEATURES) == len(set(PAIR_FEATURES)) == 24
        and feature_table["table_sha256"]
        == EXPECTED_PRIMARY_TABLE_SHA256
        and len(separators["candidate_names"]) == 365
        and len(separators["clean"]) == EXPECTED_SEPARATOR_COUNT
        and separators["clean_names_sha256"]
        == EXPECTED_CLEAN_NAMES_SHA256
        and separators["forecast_vector_count"]
        == EXPECTED_FORECAST_VECTOR_COUNT
        and all(
            resolution["verification"]["pass"]
            for resolution in new_resolutions
        )
        and forecast_scores["chronological_resolution_count"]
        == len(new_resolutions)
        and all(
            len(row["hypothesis_tests"]) == EXPECTED_SEPARATOR_COUNT
            and row["correct_count"] + row["wrong_count"]
            == EXPECTED_SEPARATOR_COUNT
            for row in forecast_scores["rows"]
        )
    )
    checks["B_RESOLUTIONS_VERIFIED_AND_103_FORECASTS_TESTED"] = b_pass
    certificates["B_RESOLUTIONS_AND_FORECAST_TESTS"] = {
        "domain": (
            "EXACT_CYCLE795_TWO_POSITION_K2_DOMAIN;"
            "THESE_ARE_FIRST_TRUE_TESTS_IF_ANY_RESOLUTION_EXISTS"
        ),
        "separator_count": len(separators["clean"]),
        "forecast_vector_count": separators["forecast_vector_count"],
        "feature_table_sha256": feature_table["table_sha256"],
        "clean_names_sha256": separators["clean_names_sha256"],
        "forecast_table_sha256": separators["forecast_table_sha256"],
        "separator_catalog": separators["separator_catalog"],
        "forecast_vector_catalog": separators["forecast_vectors"],
        "new_resolutions": new_resolutions,
        "forecast_tests_verbatim": forecast_scores,
    }

    null_applies = len(new_resolutions) == 0
    c_pass = (
        (not null_applies)
        or (
            forecast_scores["chronological_resolution_count"] == 0
            and forecast_scores["surviving_separator_count"]
            == EXPECTED_SEPARATOR_COUNT
            and forecast_scores["surviving_vector_count"]
            == EXPECTED_FORECAST_VECTOR_COUNT
            and sum(
                phase["resolutions_in_phase"] for phase in phases[1:]
            ) == 0
        )
    )
    checks["C_NULL_BRANCH_EXPLICIT_IF_APPLICABLE"] = c_pass
    certificates["C_NULL_BRANCH"] = {
        "applies": null_applies,
        "statement": (
            "NO K2 KEY RESOLVED AFTER T4096; THE CYCLE795 FORECAST "
            "PROGRAM REMAINS UNTESTED IN DOMAIN"
            if null_applies
            else
            "NULL DOES NOT APPLY; CERTIFICATE B PRINTS EVERY IN-DOMAIN "
            "FORECAST TEST VERBATIM"
        ),
        "continuation_transition_accounting": tuple(phases[1:]),
        "forecast_program_status": (
            "UNTESTED_NO_IN_DOMAIN_RESOLUTION"
            if null_applies else
            "TESTED_IN_DOMAIN"
        ),
        "unchanged_surviving_separator_count":
            forecast_scores["surviving_separator_count"],
        "unchanged_surviving_vector_count":
            forecast_scores["surviving_vector_count"],
    }

    actual_transients = {
        key: records[key]["first_clean"]
        for key in records
        if records[key]["first_clean"] is not None
        and records[key]["first_clean"] <= BASELINE_HORIZON
    }
    actual_cycles = {
        key: (
            records[key]["state_period"],
            records[key]["residual_period"],
        )
        for key in records
        if records[key]["cycle_closure"] is not None
        and records[key]["cycle_closure"] <= BASELINE_HORIZON
    }
    identity_cycle_key = (2, (0, 9))
    identity_cycle = records[identity_cycle_key]
    transient_verifications = tuple({
        "key": key,
        "first_clean": records[key]["first_clean"],
        "verification": records[key]["verification"],
    } for key in sorted(EXPECTED_TRANSIENTS))
    identity_cycle_row = {
        "key": identity_cycle_key,
        "entry": identity_cycle["cycle_start"],
        "closure": identity_cycle["cycle_closure"],
        "state_period": identity_cycle["state_period"],
        "residual_period": identity_cycle["residual_period"],
        "verification": identity_cycle["verification"],
    }
    d_pass = (
        actual_transients == EXPECTED_TRANSIENTS
        and actual_cycles == EXPECTED_CYCLES
        and all(
            row["verification"]["pass"]
            and row["verification"]["earlier_times_nonclean"]
            and row["verification"]["event_is_clean"]
            for row in transient_verifications
        )
        and identity_cycle_row["state_period"] == 288
        and identity_cycle_row["residual_period"] == 6
        and identity_cycle_row["verification"]["pass"]
        and identity_cycle_row["verification"]["state_period_minimal"]
    )
    checks["D_IDENTITY_252_371_AND_CERTIFIED_CYCLE"] = d_pass
    certificates["D_IDENTITY_CONTROLS"] = {
        "transients": transient_verifications,
        "certified_cycle": identity_cycle_row,
        "all_T4096_transient_facts": tuple(
            {"key": key, "first_clean": moment}
            for key, moment in sorted(actual_transients.items())
        ),
        "all_T4096_cycle_facts": tuple(
            {
                "key": key,
                "state_period": periods[0],
                "residual_period": periods[1],
            }
            for key, periods in sorted(actual_cycles.items())
        ),
        "identity_statement":
            "first-clean moments 252 and 371 reproduce; exact minimal "
            "state-period-288/residual-period-6 cycle reproduces",
    }

    final_open = tuple(final_snapshot["open_keys"])
    determinism_slice_rows = []
    for positions in sorted({key[1] for key in final_open}):
        determinism_slice_rows.extend(
            key for key in final_open if key[1] == positions
        )
        if len(determinism_slice_rows) >= DETERMINISM_SLICE_SIZE:
            break
    determinism_slice = tuple(
        determinism_slice_rows[:DETERMINISM_SLICE_SIZE]
    )
    primary_slice = primary_slice_rows(
        records, determinism_slice, reached_boundaries
    )
    replay_slice = replay_declared_slice(
        family, determinism_slice, reached, reached_boundaries
    )
    deterministic = primary_slice == replay_slice
    elapsed = monotonic() - script_started
    controls_base = (
        sources["pass"]
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not IMPORT_FIREWALL.hits
        and reached <= TARGET_HORIZON
    )
    checks["E_SHAS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT"] = controls_base
    certificates["E_CONTROLS"] = {
        **sources,
        "determinism_scope": {
            "declaration":
                "first eight lexicographic keys still open at the reached "
                "horizon, replayed exactly from their landed t=0 postimage "
                "through every reached boundary",
            "keys": determinism_slice,
            "primary_rows": primary_slice,
            "replay_rows": replay_slice,
            "primary_sha256": digest(primary_slice),
            "replay_sha256": digest(replay_slice),
            "deterministic": deterministic,
        },
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(IMPORT_FIREWALL.hits),
    }

    report = {
        "cycle": 819,
        "horizon_reached": reached,
        "target_horizon": TARGET_HORIZON,
        "new_resolution_count": len(new_resolutions),
        "new_transient_count": sum(
            row["outcome"] == "TRANSIENT" for row in new_resolutions
        ),
        "new_cycle_count": sum(
            row["outcome"] == "CYCLE" for row in new_resolutions
        ),
        "forecast_program_status": (
            "UNTESTED_NO_IN_DOMAIN_RESOLUTION"
            if null_applies else "TESTED_IN_DOMAIN"
        ),
        "surviving_separator_count":
            forecast_scores["surviving_separator_count"],
        "surviving_vector_count":
            forecast_scores["surviving_vector_count"],
        "final_counts": public_snapshot(final_snapshot),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE819_DEEP_K2_CONTINUATION_HONEST_FAIL",
    }
    output = stable_render(checks, certificates, report)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    checks["E_SHAS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT"] = (
        controls_base and stdout_ok
    )
    output = stable_render(checks, certificates, report)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal": "CYCLE819_DEEP_K2_CONTINUATION_HONEST_FAIL",
            "failure": "stdout bound exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
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
            "terminal": "CYCLE819_DEEP_K2_CONTINUATION_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
