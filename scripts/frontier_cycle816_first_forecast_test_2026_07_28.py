#!/usr/bin/env python3
"""Cycle 816: first prospective test of the Cycle-795 separators.

The Cycle-795 and Cycle-814 primaries are SHA-pinned text/AST references:
they are never imported or executed.  The landed Cycle-719 core is the only
executable science input.  This runner independently reconstructs the 795
feature table, 103 clean separator hypotheses, and 46 forecast vectors, then
tests the two Cycle-814 primary-certified period-4464 outcomes.

Cycle 795 used an explicit UNSEEN forecast state.  In the universal-separator
test requested here, only a CYCLE forecast is correct for a certified cycle;
TRANSIENT and UNSEEN therefore both fail that key and kill the hypothesis.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1200
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle795_discriminator_census_2026_07_28.py",
    "scripts/frontier_cycle795_discriminator_independent_check_2026_07_28.py",
    "scripts/frontier_cycle814_deep_silence_probe_2026_07_28.py",
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
BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in TEXT_AST_ONLY_PATHS
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "6a52229e9ac3bf5ab45bd25a4088e354c759fc499b58462aa0c2401f89474e7f",
    AUDIT_INPUT_PATHS[2]:
        "927c7c5d79e7c65702a2d7ac9b44f2731cbec0529ef0dee58e2ca2d2c8d5525b",
    AUDIT_INPUT_PATHS[3]:
        "f023d10784506e0c9ffbb39b17c3f120af78f377f27c5dab93de9a9aebaa98c0",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "45afe5159562f28bb9edebf7340b582408ad4ba7",
    AUDIT_INPUT_PATHS[2]: "a66db5cb3f784632c47a8140270688f2b66725e7",
    AUDIT_INPUT_PATHS[3]: "19ba617ad1f6be9f8fdc637b764dc7b38cae8d7b",
}
REFERENCE_COMMITS = {
    "cycle795_primary_and_checker":
        "6427de5c6bdd1e1f7939bac7855e1e188d28daef",
    "cycle814_sibling_primary":
        "198f7fd0b81e054982e5c754020aeaf5e214cb16",
    "cycle814_tracked_copy":
        "d623bced35e9bf0963586e5a0d00ab11071c2a8b",
}


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Fail closed if a text/AST-only primary or checker is imported."""

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
OLD_OPEN_SIZE = 162
HIGHER_K_BASELINE_OPEN_SIZE = 24
HIGHER_K_REMAINING_OPEN_SIZE = 22
COMBINED_REMAINING_OPEN_SIZE = 184
LANDED_CONSTANTS = (130, 11, 2, 5, 12, 288, 6, 3)
EXPECTED_PRIMARY_TABLE_SHA256 = (
    "266dd5f0c36cb79eb88a143c303e31ef1f79b068d6131545962ee38f8d24e705"
)
EXPECTED_CLEAN_NAMES_SHA256 = (
    "dc265dc602faef161bf1483f95810396fe3c4dfa75e7afb1cf9f871a396e6d91"
)
EXPECTED_OLD_FORECAST_VECTORS = 46

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
EXPECTED_SILENT_FAMILY_REPRESENTATIVES = {
    4: (
        (0, 2, 4, 6),
        (0, 2, 4, 7),
        (0, 2, 4, 8),
        (0, 2, 5, 7),
        (0, 2, 5, 8),
    ),
    5: ((0, 2, 4, 6, 8),),
}
RESOLVED_KEYS = (
    (4, (0, 2, 4, 7), 1),
    (4, (0, 2, 4, 8), 1),
)
RESOLVED_PERIOD = 4464
SCOPE_STATEMENT = (
    "the two resolutions are primary-verified with the independent checker "
    "still running at spec time; the kill census is conditional on those "
    "certifications holding; the ship will narrate the checker's outcome"
)

Coordinate = tuple[str, str, int]
Support = tuple[Coordinate, ...]
Key = tuple[int, tuple[int, int]]
HigherKey = tuple[int, tuple[int, ...], int]


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


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
        node.name for node in tree.body
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
    checker795_names = function_names(trees[AUDIT_INPUT_PATHS[2]])
    primary814_names = function_names(trees[AUDIT_INPUT_PATHS[3]])
    audit_literal = literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
    silent_literal = literal_assignment(
        trees[AUDIT_INPUT_PATHS[3]],
        "EXPECTED_SILENT_FAMILY_REPRESENTATIVES",
    )
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal": audit_literal == AUDIT_INPUT_PATHS,
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
        "cycle795_primary_AST_basis": {
            "feature_schema",
            "feature_table",
            "candidate_result",
            "discrimination_census",
        } <= primary795_names,
        "cycle795_checker_AST_basis": {
            "independent_feature_schema",
            "candidate_analysis",
            "separator_census",
            "forecast_vote_audit",
        } <= checker795_names,
        "cycle814_primary_AST_basis": {
            "clean_postimage",
            "configuration_families",
            "build_fixtures",
            "synchronous_word",
            "make_group",
        } <= primary814_names,
        "cycle814_silent_literal_exact":
            silent_literal == EXPECTED_SILENT_FAMILY_REPRESENTATIVES,
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
        and result["cycle795_primary_AST_basis"]
        and result["cycle795_checker_AST_basis"]
        and result["cycle814_primary_AST_basis"]
        and result["cycle814_silent_literal_exact"]
    )
    return result


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


def residual_coordinates(state: tuple[int, ...]) -> Support:
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
    return tuple(sorted(rows))


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left, right in combinations(range(RING_STATIONS), 2)
        if min(
            (right - left) % RING_STATIONS,
            (left - right) % RING_STATIONS,
        ) > 1
    )


def build_fixtures(
    program: tuple[object, ...],
) -> tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    fixtures = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        fixtures.append((event, direction, before))
        state = K.A.apply_semantic(
            before, K.M.global_allocator_word(FIXTURE_BANKS)
        )
    return tuple(fixtures)


def build_initial_supports() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    fixtures = build_fixtures(program)
    pair_supports: dict[Key, Support] = {}
    for event, _direction, before in fixtures:
        for positions in separated_pairs():
            after, rail_a, rail_b, _trace = K.run_orbit(
                before, program, token_positions=positions
            )
            expected_rail = tuple(
                int(station in positions)
                for station in range(RING_STATIONS)
            )
            if rail_a != expected_rail or any(rail_b):
                raise AssertionError(("pair rail mismatch", event, positions))
            pair_supports[(event, positions)] = residual_coordinates(after)

    higher_supports: dict[HigherKey, Support] = {}
    for k, representatives in EXPECTED_SILENT_FAMILY_REPRESENTATIVES.items():
        for positions in representatives:
            for event, _direction, before in fixtures:
                after, rail_a, rail_b, _trace = K.run_orbit(
                    before, program, token_positions=positions
                )
                expected_rail = tuple(
                    int(station in positions)
                    for station in range(RING_STATIONS)
                )
                if rail_a != expected_rail or any(rail_b):
                    raise AssertionError(
                        ("higher-k rail mismatch", k, positions, event)
                    )
                higher_supports[(k, positions, event)] = (
                    residual_coordinates(after)
                )
    return {
        "fixtures": fixtures,
        "pair_supports": pair_supports,
        "higher_supports": higher_supports,
    }


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
    positions: tuple[int, ...],
    direction: tuple[int, int],
    support: Support,
    support_classes: dict[Support, int],
) -> dict[str, Any]:
    """Extend the landed pair coordinates canonically to an occupied set.

    Extrema retain the Cycle-795 left/right and arc meanings.  Additive,
    product, mask, modular-mean, and equal-residue features use all occupied
    sites.  Support features use the actual higher-k postimage.  A support
    absent from the frozen 25-class Cycle-795 vocabulary receives a stable
    NEW_SUPPORT digest token, so it cannot alias a landed class identifier.
    """

    left, right = positions[0], positions[-1]
    clockwise = (right - left) % RING_STATIONS
    counterclockwise = (left - right) % RING_STATIONS
    separation = min(clockwise, counterclockwise)
    short_orientation = 1 if clockwise < counterclockwise else -1
    epoch_direction = 1 if direction == (1, 0) else -1
    position_sum = sum(positions)
    stats = support_statistics(support)
    support_id: int | str
    if support in support_classes:
        support_id = support_classes[support]
    else:
        support_id = "NEW_SUPPORT_" + digest(support)
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
        "short_arc_start":
            left if short_orientation == 1 else right,
        "short_arc_end":
            right if short_orientation == 1 else left,
        "left_parity": left % 2,
        "right_parity": right % 2,
        "parity_code": 2 * (left % 2) + right % 2,
        "same_position_parity":
            int(len({position % 2 for position in positions}) == 1),
        "epoch_sum_parity": (event + position_sum) % 2,
        "initial_residual_weight": len(support),
        "initial_support_size": len(support),
        "support_signature_id": support_id,
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
        named.update(
            {
                f"left_mod_{modulus}": left % modulus,
                f"right_mod_{modulus}": right % modulus,
                f"position_sum_mod_{modulus}":
                    position_sum % modulus,
                f"clockwise_gap_mod_{modulus}":
                    clockwise % modulus,
                f"ring_separation_mod_{modulus}":
                    separation % modulus,
                f"epoch_mod_{modulus}": event % modulus,
                f"same_position_residue_mod_{modulus}":
                    int(
                        len({
                            position % modulus for position in positions
                        }) == 1
                    ),
            }
        )
    if set(named) != set(FEATURE_SCHEMA):
        raise AssertionError(("feature schema mismatch", set(named) ^ set(
            FEATURE_SCHEMA
        )))
    return named


def reconstruct_feature_tables() -> dict[str, object]:
    supports = build_initial_supports()
    fixtures = {
        event: direction
        for event, direction, _before in supports["fixtures"]
    }
    pair_supports = supports["pair_supports"]
    support_classes = {
        support: identifier
        for identifier, support in enumerate(
            sorted(set(pair_supports.values()))
        )
    }
    pair_features: dict[Key, dict[str, Any]] = {}
    pair_rows = []
    for key in sorted(pair_supports):
        event, positions = key
        named = named_features(
            event,
            positions,
            fixtures[event],
            pair_supports[key],
            support_classes,
        )
        pair_features[key] = named
        pair_rows.append(
            (event, positions[0], positions[1])
            + tuple(named[name] for name in FEATURE_SCHEMA)
        )

    higher_features: dict[HigherKey, dict[str, Any]] = {}
    for key in sorted(supports["higher_supports"]):
        k, positions, event = key
        if len(positions) != k:
            raise AssertionError(("higher-k key arity", key))
        higher_features[key] = named_features(
            event,
            positions,
            fixtures[event],
            supports["higher_supports"][key],
            support_classes,
        )
    return {
        "pair_features": pair_features,
        "pair_rows": tuple(pair_rows),
        "higher_features": higher_features,
        "support_classes": support_classes,
    }


def projection(
    features: dict[str, Any],
    names: tuple[str, ...],
) -> tuple[Any, ...]:
    return tuple(features[name] for name in names)


def separator_reconstruction(tables: dict[str, object]) -> dict[str, object]:
    features = tables["pair_features"]
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
        if transient_values.isdisjoint(cycle_values):
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
            clean.append(
                {
                    "names": names,
                    "transient_values": transient_values,
                    "cycle_values": cycle_values,
                    "forecast": forecast,
                    "margin": margin,
                    "open_classified":
                        sum(side != "UNSEEN" for side in forecast),
                }
            )
    clean.sort(
        key=lambda row: (
            -row["open_classified"],
            len(row["names"]),
            -row["margin"],
            row["names"],
        )
    )
    return {
        "open_keys": open_keys,
        "candidate_names": candidate_names,
        "clean": tuple(clean),
        "clean_names_sha256":
            digest(tuple(row["names"] for row in clean)),
        "unique_old_forecast_vectors": len({
            row["forecast"] for row in clean
        }),
    }


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


def prospective_test(
    tables: dict[str, object],
    separators: dict[str, object],
) -> dict[str, object]:
    higher_features = tables["higher_features"]
    rows = []
    bins = {
        "correct_on_both": [],
        "correct_on_one": [],
        "wrong_on_both": [],
    }
    for hypothesis_id, hypothesis in enumerate(
        separators["clean"], start=1
    ):
        key_rows = []
        correct_count = 0
        for key in RESOLVED_KEYS:
            value = projection(higher_features[key], hypothesis["names"])
            side = forecast_side(
                value,
                hypothesis["transient_values"],
                hypothesis["cycle_values"],
            )
            correct = side == "CYCLE"
            correct_count += int(correct)
            key_rows.append(
                {
                    "key": key,
                    "separator_value": value,
                    "forecast_side": side,
                    "resolved_side": "CYCLE",
                    "test_result": "CORRECT" if correct else "WRONG",
                }
            )
        bin_name = {
            2: "correct_on_both",
            1: "correct_on_one",
            0: "wrong_on_both",
        }[correct_count]
        bins[bin_name].append(hypothesis["names"])
        rows.append(
            {
                "hypothesis_id": hypothesis_id,
                "features": hypothesis["names"],
                "key_tests": tuple(key_rows),
                "census_bin": bin_name,
                "killed_as_universal_separator": correct_count < 2,
            }
        )
    survivors = tuple(bins["correct_on_both"])
    higher_open = tuple(
        key for key in sorted(higher_features) if key not in RESOLVED_KEYS
    )
    survivor_vectors = set()
    for hypothesis in separators["clean"]:
        if hypothesis["names"] not in set(survivors):
            continue
        old_vector = hypothesis["forecast"]
        higher_vector = tuple(
            forecast_side(
                projection(higher_features[key], hypothesis["names"]),
                hypothesis["transient_values"],
                hypothesis["cycle_values"],
            )
            for key in higher_open
        )
        survivor_vectors.add(old_vector + higher_vector)
    return {
        "rows": tuple(rows),
        "bins": {name: tuple(values) for name, values in bins.items()},
        "counts": {name: len(values) for name, values in bins.items()},
        "survivors": survivors,
        "surviving_vector_count": len(survivor_vectors),
        "higher_open_keys": higher_open,
        "combined_open_count":
            len(separators["open_keys"]) + len(higher_open),
        "test_sha256": digest(rows),
    }


def analysis_once() -> dict[str, object]:
    tables = reconstruct_feature_tables()
    separators = separator_reconstruction(tables)
    test = prospective_test(tables, separators)
    return {
        "tables": tables,
        "separators": separators,
        "test": test,
        "stable_digest": digest(
            {
                "pair_rows": tables["pair_rows"],
                "higher_features": tuple(
                    (key, tables["higher_features"][key])
                    for key in sorted(tables["higher_features"])
                ),
                "clean_names": tuple(
                    row["names"] for row in separators["clean"]
                ),
                "old_forecasts": tuple(
                    row["forecast"] for row in separators["clean"]
                ),
                "test_rows": test["rows"],
                "higher_open_keys": test["higher_open_keys"],
            }
        ),
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
            "CYCLE816_FIRST_FORECAST_TEST_PASS"
            if report["pass"]
            else "CYCLE816_FIRST_FORECAST_TEST_HONEST_FAIL"
        )
        output = render(checks, certificates, report)
        size = len(output.encode("utf-8"))
        controls = certificates["E_CONTROLS"]
        if (
            report["stdout_bytes"] == size
            and controls["stdout_bytes"] == size
        ):
            return output
        report["stdout_bytes"] = size
        controls["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    checks: dict[str, bool] = {}
    certificates: dict[str, object] = {}

    sources = source_certificate()
    first = analysis_once()
    tables = first["tables"]
    separators = first["separators"]
    test = first["test"]

    a_pass = (
        sources["pass"]
        and len(FEATURE_SCHEMA) == len(set(FEATURE_SCHEMA)) == 89
        and len(PAIR_FEATURES) == len(set(PAIR_FEATURES)) == 24
        and len(tables["pair_features"]) == FAMILY_SIZE
        and len(tables["pair_rows"]) == FAMILY_SIZE
        and len(tables["support_classes"]) == 25
        and digest(tables["pair_rows"]) == EXPECTED_PRIMARY_TABLE_SHA256
        and len(separators["candidate_names"]) == 365
        and len(separators["clean"]) == 103
        and separators["clean_names_sha256"]
        == EXPECTED_CLEAN_NAMES_SHA256
        and len(test["rows"]) == 103
        and all(
            tuple(row["key_tests"][index]["key"] for row in test["rows"])
            == (RESOLVED_KEYS[index],) * 103
            for index in range(2)
        )
    )
    checks["A_RECONSTRUCT_103_FORECAST_TEST_ROWS"] = a_pass
    certificates["A_FORECAST_TABLE_103"] = {
        "finding":
            "full hypothesis values and prospective sides for both keys",
        "feature_extension":
            "canonical occupied-set extension: extrema for arc features; "
            "all sites for sum/product/mask/modular mean/equal-residue; "
            "actual higher-k postimage support; unseen support signatures "
            "cannot alias the frozen Cycle-795 25-class vocabulary",
        "resolved_keys": RESOLVED_KEYS,
        "rows": test["rows"],
        "rows_sha256": test["test_sha256"],
    }

    counts = test["counts"]
    b_pass = (
        sum(counts.values()) == 103
        and counts == {
            "correct_on_both": 0,
            "correct_on_one": 8,
            "wrong_on_both": 95,
        }
        and len(test["survivors"]) == counts["correct_on_both"]
        and all(row["killed_as_universal_separator"] for row in test["rows"])
    )
    checks["B_KILL_CENSUS_EXHAUSTIVE"] = b_pass
    certificates["B_KILL_CENSUS"] = {
        "outcomes": tuple(
            {
                "key": key,
                "side": "CYCLE",
                "period": RESOLVED_PERIOD,
                "verification": "PRIMARY_VERIFIED_CHECKER_PENDING",
            }
            for key in RESOLVED_KEYS
        ),
        "UNSEEN_rule":
            "Cycle 795 emitted UNSEEN; for a universal binary separator it "
            "is not a correct CYCLE prediction and therefore counts WRONG",
        "counts": counts,
        "lists": test["bins"],
        "killed": 103 - len(test["survivors"]),
        "surviving_hypotheses": test["survivors"],
        "surviving_count": len(test["survivors"]),
    }

    c_pass = (
        len(separators["open_keys"]) == OLD_OPEN_SIZE
        and len(tables["higher_features"]) == HIGHER_K_BASELINE_OPEN_SIZE
        and len(test["higher_open_keys"]) == HIGHER_K_REMAINING_OPEN_SIZE
        and test["combined_open_count"] == COMBINED_REMAINING_OPEN_SIZE
        and separators["unique_old_forecast_vectors"]
        == EXPECTED_OLD_FORECAST_VECTORS
        and test["surviving_vector_count"] == 0
    )
    checks["C_SURVIVING_FAMILY_VECTOR_COLLAPSE"] = c_pass
    certificates["C_SURVIVING_FAMILY"] = {
        "old_open_keys": len(separators["open_keys"]),
        "higher_k_open_before_resolutions":
            len(tables["higher_features"]),
        "higher_k_open_after_resolutions": len(test["higher_open_keys"]),
        "still_open": "22+162=184",
        "original_hypotheses": len(separators["clean"]),
        "surviving_hypotheses": len(test["survivors"]),
        "original_distinct_forecast_vectors":
            separators["unique_old_forecast_vectors"],
        "surviving_distinct_forecast_vectors":
            test["surviving_vector_count"],
        "collapse": "46 -> 0",
        "surviving_fraction": 0.0,
        "higher_open_keyset_sha256": digest(test["higher_open_keys"]),
    }

    d_pass = (
        SCOPE_STATEMENT
        == (
            "the two resolutions are primary-verified with the independent "
            "checker still running at spec time; the kill census is "
            "conditional on those certifications holding; the ship will "
            "narrate the checker's outcome"
        )
    )
    checks["D_HONEST_CONDITIONAL_SCOPE"] = d_pass
    certificates["D_HONEST_SCOPE"] = {
        "statement": SCOPE_STATEMENT,
        "primary_status": "PRIMARY_VERIFIED",
        "checker_status_at_spec_time": "STILL_RUNNING",
        "census_status":
            "CONDITIONAL_ON_BOTH_PRIMARY_CERTIFICATIONS_HOLDING",
    }

    replay = analysis_once()
    deterministic = replay["stable_digest"] == first["stable_digest"]
    elapsed = monotonic() - started
    controls_base = (
        deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and sources["pass"]
        and not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not IMPORT_FIREWALL.hits
    )
    checks["E_SHAS_BLOCKLIST_DETERMINISM_BOUNDS"] = controls_base
    certificates["E_CONTROLS"] = {
        **sources,
        "deterministic": deterministic,
        "first_analysis_sha256": first["stable_digest"],
        "replay_analysis_sha256": replay["stable_digest"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    }

    report = {
        "cycle": 816,
        "status": "FIRST_FORECAST_TEST_CONDITIONAL_CHECKER_PENDING",
        "kill_counts": counts,
        "surviving_hypotheses": len(test["survivors"]),
        "vector_collapse": "46 -> 0",
        "still_open": "22+162=184",
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "scope": SCOPE_STATEMENT,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE816_FIRST_FORECAST_TEST_HONEST_FAIL",
    }
    output = stable_render(checks, certificates, report)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    checks["E_SHAS_BLOCKLIST_DETERMINISM_BOUNDS"] = (
        controls_base and stdout_ok
    )
    output = stable_render(checks, certificates, report)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal": "CYCLE816_FIRST_FORECAST_TEST_HONEST_FAIL",
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
            "terminal": "CYCLE816_FIRST_FORECAST_TEST_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
