#!/usr/bin/env python3
"""Cycle 810 independent adversarial check: mechanism versus correlation.

The Cycle-810 primary and Cycle-752 source are text/AST-only audit inputs.
This checker rebuilds the held two-bank fixture from the landed Cycle-719
support API, simulates its basis-state gates with an independent integer
engine, and treats the Cycle-752 adjacent-start generator as the complete
lawful start domain.  It never imports or executes the Cycle-810 primary.
"""
from __future__ import annotations

import ast
from collections import defaultdict
from functools import lru_cache
from hashlib import sha256
import importlib
import importlib.abc
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Iterable


AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle810_satisfiable_start_discriminator_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fb50873dd30a0d580bfd03a19cc4613dd9517816e1e9aab7adba6bd77ed2c2a1",
    AUDIT_INPUT_PATHS[1]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[2]:
        "2f39e834f89be02bf40bbe9a0d9cac905dc8f4294096faaa7914cfc31fed26a7",
}
TEXT_AST_ONLY_MODULES = (
    Path(AUDIT_INPUT_PATHS[0]).stem,
    Path(AUDIT_INPUT_PATHS[2]).stem,
)
PRIMARY_MODULE = Path(AUDIT_INPUT_PATHS[2]).stem
RING_STATIONS = 11
FIXTURE_BANKS = 2
ASSIGNMENTS_PER_START = 1 << RING_STATIONS
CLAIMED_SUCCESS_COUNTS = (512,) + (0,) * 10
CLAIMED_SEPARATOR_COUNT = 142
EXPECTED_TARGET_SHA256 = (
    "3513b562570c8ee4723fad82900dea66e6df5933fe40ac5e06a85bc513fea213"
)
RUNTIME_LIMIT_SECONDS = 1200.0
STDOUT_LIMIT_BYTES = 150 * 1024
ROOT = Path(__file__).resolve().parents[1]

PROFILE_NAMES = (
    "program_kind",
    "program_charge_row_index",
    "initial_station_occupancy",
    "event_station_occupancy",
    "initial_relay_occupancy",
    "initial_handoff_occupancy",
    "event_relay_occupancy",
    "event_handoff_occupancy",
    "semantic_gate_count",
    "semantic_gate_vector_X_CNOT_TOF",
    "physical_gate_count",
    "physical_gate_vector_CNOT_TOF",
    "token_travel_distance",
    "rail_hop_distance_A_to_B",
    "rail_hop_distance_B_to_next_A",
)
VECTOR_COMPONENT_NAMES = {
    "semantic_gate_vector_X_CNOT_TOF": ("X", "CNOT", "TOF"),
    "physical_gate_vector_CNOT_TOF": ("CNOT", "TOF"),
}
PROVENANCE = {
    "ring_and_fixture_constants": (
        f"{AUDIT_INPUT_PATHS[0]}:"
        "RING_STATIONS,FIXTURE_BANKS"
    ),
    "program_generator": (
        f"{AUDIT_INPUT_PATHS[0]}:main(program="
        "K.interleaved_program(FIXTURE_BANKS)); "
        f"{AUDIT_INPUT_PATHS[1]}:interleaved_program"
    ),
    "lawful_start_generator": (
        f"{AUDIT_INPUT_PATHS[0]}:route3_adjacent_full_battery("
        "for position in range(RING_STATIONS); "
        "positions=(position,(position+1)%RING_STATIONS))"
    ),
    "landed_quantities": (
        f"{AUDIT_INPUT_PATHS[1]}:mapped_macro,controlled_macro,"
        "held_physical_program_and_track"
    ),
    "predicate_grammar": (
        f"{AUDIT_INPUT_PATHS[2]}:separator_hunt (text/AST only)"
    ),
}

FINDING_SEPARATOR = (
    "The landed Cycle-752-lineage program_kind values split start 0 from "
    "starts 1-10 exactly: only start 0 has source on the left token row."
)
FINDING_ANATOMY = (
    "Complete 11x2048 enumeration and independent backward pruning show "
    "that both boundary-0 orders have zero completions for every "
    "unsatisfiable start 1-10; every such left row is non-source."
)
FINDING_MECHANISM = (
    "correlation proven at scope; causation untestable at scope"
)
FINDING_RECOUNT = (
    "The declared size-at-most-2 grammar has 142 exact minimal separators; "
    "size 0 cannot separate and the source-kind predicate is size 1."
)


class _TextOnlyBlocker(importlib.abc.MetaPathFinder):
    """Fail closed if either inert audit source is imported."""

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        del path, target
        if fullname in TEXT_AST_ONLY_MODULES:
            raise ImportError(f"{fullname} is text/AST-only in this checker")
        return None


_IMPORT_BLOCKER = _TextOnlyBlocker()
sys.meta_path.insert(0, _IMPORT_BLOCKER)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Gate = tuple[str, tuple[int, ...]]
Word = tuple[Gate, ...]


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest_json(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def freeze_word(word: Iterable[object]) -> Word:
    return tuple((gate.kind, tuple(gate.wires)) for gate in word)


def bits_to_int(bits: Iterable[int]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(bits))


def bit_digest(state: int, width: int) -> str:
    return sha256(
        bytes((state >> index) & 1 for index in range(width))
    ).hexdigest()


def apply_word_int(state: int, word: Word) -> int:
    """Apply X/CNOT/TOF exactly without the landed semantic simulator."""

    for kind, wires in word:
        if kind == "X":
            state ^= 1 << wires[0]
        elif kind == "CNOT":
            state ^= ((state >> wires[0]) & 1) << wires[1]
        elif kind == "TOF":
            state ^= (
                ((state >> wires[0]) & 1)
                & ((state >> wires[1]) & 1)
            ) << wires[2]
        else:
            raise AssertionError(("unsupported gate", kind, wires))
    return state


def ast_assignment(tree: ast.Module, name: str) -> ast.expr:
    matches: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError(("assignment census", name, len(matches)))
    return matches[0]


def ast_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function census", name, len(matches)))
    return matches[0]


def assignment_in_function(
    function: ast.FunctionDef,
    name: str,
) -> tuple[ast.expr, ...]:
    return tuple(
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    )


def dict_value_in_function(
    function: ast.FunctionDef,
    key: str,
) -> ast.expr:
    matches = []
    for node in ast.walk(function):
        if not isinstance(node, ast.Dict):
            continue
        for candidate, value in zip(node.keys, node.values):
            if (
                isinstance(candidate, ast.Constant)
                and candidate.value == key
            ):
                matches.append(value)
    if len(matches) != 1:
        raise AssertionError(("dict key census", key, len(matches)))
    return matches[0]


def source_contract() -> dict[str, object]:
    """Extract the lawful start domain and grammar without source execution."""

    source_path = ROOT / AUDIT_INPUT_PATHS[0]
    primary_path = ROOT / AUDIT_INPUT_PATHS[2]
    source_tree = ast.parse(
        source_path.read_text(encoding="utf-8"),
        filename=AUDIT_INPUT_PATHS[0],
    )
    primary_tree = ast.parse(
        primary_path.read_text(encoding="utf-8"),
        filename=AUDIT_INPUT_PATHS[2],
    )
    ring = ast.literal_eval(ast_assignment(source_tree, "RING_STATIONS"))
    banks = ast.literal_eval(ast_assignment(source_tree, "FIXTURE_BANKS"))
    adjacent = ast_function(source_tree, "route3_adjacent_full_battery")
    position_loops = [
        node
        for node in ast.walk(adjacent)
        if isinstance(node, ast.For)
        and isinstance(node.target, ast.Name)
        and node.target.id == "position"
        and isinstance(node.iter, ast.Call)
        and isinstance(node.iter.func, ast.Name)
        and node.iter.func.id == "range"
        and len(node.iter.args) == 1
        and isinstance(node.iter.args[0], ast.Name)
        and node.iter.args[0].id == "RING_STATIONS"
    ]
    positions_nodes = assignment_in_function(adjacent, "positions")
    expected_positions_ast = ast.parse(
        "positions=(position,(position+1)%RING_STATIONS)"
    ).body[0]
    assert isinstance(expected_positions_ast, ast.Assign)
    positions_shape = (
        len(positions_nodes) == 1
        and ast.dump(positions_nodes[0], include_attributes=False)
        == ast.dump(expected_positions_ast.value, include_attributes=False)
    )
    lawful_pairs = tuple(
        (position, (position + 1) % ring) for position in range(ring)
    )

    main_function = ast_function(source_tree, "main")
    program_assignments = assignment_in_function(main_function, "program")
    expected_program_ast = ast.parse(
        "program=K.interleaved_program(FIXTURE_BANKS)"
    ).body[0]
    assert isinstance(expected_program_ast, ast.Assign)
    fixed_program_shape = (
        len(program_assignments) == 1
        and ast.dump(program_assignments[0], include_attributes=False)
        == ast.dump(expected_program_ast.value, include_attributes=False)
    )

    separator_function = ast_function(primary_tree, "separator_hunt")
    size_bound = ast.literal_eval(
        dict_value_in_function(separator_function, "size_bound")
    )
    boolean_formula = ast.literal_eval(
        dict_value_in_function(separator_function, "boolean_formula")
    )
    size_measure = ast.literal_eval(
        dict_value_in_function(separator_function, "size_measure")
    )
    grammar = {
        "single_literal_atom":
            "q == c | q != c for every observed c",
        "single_threshold_atom": (
            "q < c | q <= c | q > c | q >= c for every observed "
            "integer c"
        ),
        "pairwise_atom": (
            "left q OP right q at the same boundary or across the two "
            "initial token rows; OP is <,<=,==,!=,>=,> for integers "
            "and ==,!= for strings"
        ),
        "boolean_formula": "(atom AND atom) | (atom OR atom)",
        "size_bound": 2,
        "size_measure": "number of atomic leaves",
    }
    primary_strings = {
        node.value
        for node in ast.walk(separator_function)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    grammar_ast_match = (
        size_bound == grammar["size_bound"]
        and boolean_formula == grammar["boolean_formula"]
        and size_measure == grammar["size_measure"]
        and all(
            grammar[name] in primary_strings
            for name in (
                "single_literal_atom",
                "single_threshold_atom",
                "pairwise_atom",
            )
        )
    )
    start_ast_projection = {
        "position_loop": tuple(
            ast.dump(node, include_attributes=False)
            for node in position_loops
        ),
        "positions": tuple(
            ast.dump(node, include_attributes=False)
            for node in positions_nodes
        ),
        "program": tuple(
            ast.dump(node, include_attributes=False)
            for node in program_assignments
        ),
    }
    return {
        "ring_stations": ring,
        "fixture_banks": banks,
        "position_loop_count": len(position_loops),
        "positions_shape_match": positions_shape,
        "fixed_program_shape_match": fixed_program_shape,
        "lawful_pairs": lawful_pairs,
        "lawful_pair_count": len(lawful_pairs),
        "lawful_pairs_unique": len(set(lawful_pairs)) == len(lawful_pairs),
        "start_generator_ast_sha256": digest_json(start_ast_projection),
        "grammar": grammar,
        "grammar_ast_match": grammar_ast_match,
        "primary_separator_function_ast_sha256": sha256(
            ast.dump(separator_function, include_attributes=False).encode()
        ).hexdigest(),
    }


def build_fixture() -> dict[str, object]:
    """Rebuild landed constants from the fixed Cycle-752 two-bank call."""

    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    data = tuple(
        K.M.prepare_endpoint(K.M.pack_state(banks, links), (1, 0))
    )
    data_width = len(data)
    semantic_words = tuple(
        freeze_word(K.mapped_macro(row)) for row in program
    )
    physical_words = tuple(
        freeze_word(
            K.controlled_macro(
                K.mapped_macro(program[station]),
                data_width + station,
                data_width + 2 * RING_STATIONS + station,
            )
        )
        for station in range(RING_STATIONS)
    )
    physical_program, track = K.held_physical_program_and_track(
        FIXTURE_BANKS
    )
    if physical_program != program:
        raise AssertionError("held physical program differs")
    a_sites = track[::2]
    b_sites = track[1::2]

    def l1(left: tuple[int, ...], right: tuple[int, ...]) -> int:
        return sum(abs(a - b) for a, b in zip(left, right))

    rail_hops = tuple(
        (
            l1(a_sites[station], b_sites[station]),
            l1(
                b_sites[station],
                a_sites[(station + 1) % RING_STATIONS],
            ),
        )
        for station in range(RING_STATIONS)
    )
    initial = bits_to_int(data)
    allocator = freeze_word(K.M.global_allocator_word(FIXTURE_BANKS))
    expected = initial
    for _source in range(FIXTURE_BANKS):
        expected = apply_word_int(expected, allocator)
    return {
        "program": program,
        "program_kinds": tuple(row[0] for row in program),
        "data_width": data_width,
        "initial": initial,
        "expected": expected,
        "target_sha256": bit_digest(expected, data_width),
        "semantic_words": semantic_words,
        "semantic_vectors": tuple(
            tuple(
                sum(kind == wanted for kind, _wires in word)
                for wanted in ("X", "CNOT", "TOF")
            )
            for word in semantic_words
        ),
        "physical_words": physical_words,
        "physical_vectors": tuple(
            tuple(
                sum(kind == wanted for kind, _wires in word)
                for wanted in ("CNOT", "TOF")
            )
            for word in physical_words
        ),
        "rail_hops": rail_hops,
    }


def contender_profile(
    fixture: dict[str, object],
    start: int,
    step: int,
    station: int,
) -> tuple[object, ...]:
    initial_occupied = int(
        station in (start, (start + 1) % RING_STATIONS)
    )
    kind, charge_index, _local = fixture["program"][station]
    semantic_word = fixture["semantic_words"][station]
    physical_word = fixture["physical_words"][station]
    hop_out, hop_in = fixture["rail_hops"][station]
    profile: tuple[object, ...] = (
        kind,
        charge_index,
        initial_occupied,
        1,
        int(initial_occupied and kind == "relay"),
        int(initial_occupied and kind == "handoff"),
        int(kind == "relay"),
        int(kind == "handoff"),
        len(semantic_word),
        fixture["semantic_vectors"][station],
        len(physical_word),
        fixture["physical_vectors"][station],
        2 * step,
        hop_out,
        hop_in,
    )
    if len(profile) != len(PROFILE_NAMES):
        raise AssertionError(("profile width", len(profile)))
    return profile


def start_rows(
    fixture: dict[str, object],
    contract: dict[str, object],
) -> tuple[dict[str, object], ...]:
    """Materialize all and only starts emitted by the 752 AST contract."""

    rows = []
    for start, right_station in contract["lawful_pairs"]:
        tokens = (start, right_station)
        occupancy = tuple(
            int(station in tokens) for station in range(RING_STATIONS)
        )
        token_rows = []
        for role, station in zip(("left", "right"), tokens):
            kind, charge_index, _local = fixture["program"][station]
            token_rows.append(
                {
                    "role": role,
                    "station": station,
                    "program_kind": kind,
                    "program_charge_row_index": charge_index,
                    "initial_occupancy": occupancy[station],
                    "semantic_gate_count":
                        len(fixture["semantic_words"][station]),
                    "semantic_gate_vector_X_CNOT_TOF":
                        fixture["semantic_vectors"][station],
                    "physical_gate_count":
                        len(fixture["physical_words"][station]),
                    "physical_gate_vector_CNOT_TOF":
                        fixture["physical_vectors"][station],
                    "initial_token_travel_distance": 0,
                    "rail_hop_distance_A_to_B":
                        fixture["rail_hops"][station][0],
                    "rail_hop_distance_B_to_next_A":
                        fixture["rail_hops"][station][1],
                }
            )
        boundaries = []
        for step in range(RING_STATIONS):
            left = (start + step) % RING_STATIONS
            right = (left + 1) % RING_STATIONS
            boundaries.append(
                (
                    step,
                    (left, right),
                    contender_profile(fixture, start, step, left),
                    contender_profile(fixture, start, step, right),
                )
            )
        rows.append(
            {
                "start": start,
                "initial_token_stations": tokens,
                "initial_station_occupancies": occupancy,
                "token_charge_rows": tuple(token_rows),
                "boundary_profiles": tuple(boundaries),
            }
        )
    return tuple(rows)


def exhaustive_satisfiability(
    fixture: dict[str, object],
) -> dict[str, object]:
    """Enumerate all paths and independently count viable suffixes."""

    words: tuple[Word, ...] = fixture["semantic_words"]

    @lru_cache(maxsize=None)
    def apply_macro(station: int, state: int) -> int:
        return apply_word_int(state, words[station])

    @lru_cache(maxsize=None)
    def transition(
        start: int,
        depth: int,
        state: int,
    ) -> tuple[int, int]:
        left = (start + depth) % RING_STATIONS
        right = (left + 1) % RING_STATIONS
        left_then_right = apply_macro(
            right, apply_macro(left, state)
        )
        right_then_left = apply_macro(
            left, apply_macro(right, state)
        )
        return left_then_right, right_then_left

    @lru_cache(maxsize=None)
    def completion_count(
        start: int,
        depth: int,
        state: int,
    ) -> int:
        if depth == RING_STATIONS:
            return int(state == fixture["expected"])
        destinations = transition(start, depth, state)
        return sum(
            completion_count(start, depth + 1, destination)
            for destination in destinations
        )

    per_start = []
    for start in range(RING_STATIONS):
        prefixes: list[dict[int, int]] = [{0: fixture["initial"]}]
        for depth in range(RING_STATIONS):
            next_prefixes: dict[int, int] = {}
            for mask, state in prefixes[-1].items():
                forward, reverse = transition(start, depth, state)
                next_prefixes[mask] = forward
                next_prefixes[mask | (1 << depth)] = reverse
            prefixes.append(next_prefixes)
        successful_masks = tuple(
            mask
            for mask, state in sorted(prefixes[-1].items())
            if state == fixture["expected"]
        )
        recursive_success_count = completion_count(
            start, 0, fixture["initial"]
        )
        if recursive_success_count != len(successful_masks):
            raise AssertionError(
                (
                    "enumeration/backward disagreement",
                    start,
                    len(successful_masks),
                    recursive_success_count,
                )
            )
        pruning = []
        for depth, prefix_map in enumerate(prefixes):
            viable_paths = sum(
                completion_count(start, depth, state) > 0
                for state in prefix_map.values()
            )
            distinct_states = set(prefix_map.values())
            viable_states = {
                state
                for state in distinct_states
                if completion_count(start, depth, state) > 0
            }
            pruning.append(
                {
                    "depth": depth,
                    "partial_assignments": len(prefix_map),
                    "distinct_reachable_states": len(distinct_states),
                    "viable_partial_assignments": viable_paths,
                    "viable_distinct_states": len(viable_states),
                    "doomed_partial_assignments":
                        len(prefix_map) - viable_paths,
                }
            )
        first_destinations = transition(
            start, 0, fixture["initial"]
        )
        first_branch_completions = tuple(
            completion_count(start, 1, state)
            for state in first_destinations
        )
        earliest_dead = next(
            (
                depth - 1
                for depth in range(1, RING_STATIONS + 1)
                if pruning[depth]["viable_partial_assignments"] == 0
            ),
            None,
        )
        per_start.append(
            {
                "start": start,
                "successful_assignment_count": len(successful_masks),
                "successful_masks_sha256": sha256(
                    b"".join(
                        mask.to_bytes(2, "little")
                        for mask in successful_masks
                    )
                ).hexdigest(),
                "distinct_final_outputs":
                    len(set(prefixes[-1].values())),
                "complete_final_assignments": len(prefixes[-1]),
                "boundary_0_order_completion_counts":
                    first_branch_completions,
                "earliest_all_doomed_boundary": earliest_dead,
                "backward_pruning": tuple(pruning),
            }
        )
    success_counts = tuple(
        row["successful_assignment_count"] for row in per_start
    )
    pruning_projection = tuple(
        {
            "start": row["start"],
            "boundary_0": row["boundary_0_order_completion_counts"],
            "earliest": row["earliest_all_doomed_boundary"],
            "layers": row["backward_pruning"],
        }
        for row in per_start
    )
    return {
        "assignment_encoding": (
            "11-bit mask; bit d=0 applies left then right at boundary d, "
            "bit d=1 applies right then left"
        ),
        "assignments_per_start": ASSIGNMENTS_PER_START,
        "total_assignments":
            RING_STATIONS * ASSIGNMENTS_PER_START,
        "success_counts_by_start": success_counts,
        "starts": tuple(per_start),
        "backward_pruning_sha256": digest_json(pruning_projection),
        "integer_transition_cache": {
            "macro_entries": apply_macro.cache_info().currsize,
            "transition_entries": transition.cache_info().currsize,
            "completion_entries": completion_count.cache_info().currsize,
        },
    }


def add_scalar(
    row: dict[str, object],
    path: str,
    leaf_name: str,
    value: object,
) -> None:
    if leaf_name in VECTOR_COMPONENT_NAMES:
        component_names = VECTOR_COMPONENT_NAMES[leaf_name]
        if not isinstance(value, tuple):
            raise AssertionError(("vector type", path, value))
        if len(value) != len(component_names):
            raise AssertionError(("vector width", path, value))
        for component, scalar in zip(component_names, value):
            row[f"{path}.{component}"] = scalar
    elif isinstance(value, (int, str)):
        row[path] = value
    else:
        raise AssertionError(("undeclared scalar type", path, value))


def scalar_quantity_table(
    starts: tuple[dict[str, object], ...],
) -> tuple[
    dict[str, tuple[object, ...]],
    tuple[tuple[str, str], ...],
]:
    """Flatten the primary's declared identity-free landed leaf domain."""

    flat_rows = []
    pair_paths: set[tuple[str, str]] = set()
    for start_row in starts:
        flat: dict[str, object] = {}
        for station, occupied in enumerate(
            start_row["initial_station_occupancies"]
        ):
            flat[f"initial_occupancy[{station}]"] = occupied

        by_role = {
            token["role"]: token
            for token in start_row["token_charge_rows"]
        }
        for role in ("left", "right"):
            for name, value in by_role[role].items():
                if name in ("role", "station"):
                    continue
                add_scalar(flat, f"token.{role}.{name}", name, value)
        for left_path in tuple(flat):
            if not left_path.startswith("token.left."):
                continue
            leaf = left_path.removeprefix("token.left.")
            pair_paths.add(
                (left_path, f"token.right.{leaf}")
            )

        for boundary in start_row["boundary_profiles"]:
            step, _stations, left_profile, right_profile = boundary
            for side, profile in (
                ("left", left_profile),
                ("right", right_profile),
            ):
                for name, value in zip(PROFILE_NAMES, profile):
                    add_scalar(
                        flat,
                        f"boundary[{step}].{side}.{name}",
                        name,
                        value,
                    )
            prefix = f"boundary[{step}].left."
            for left_path in tuple(flat):
                if left_path.startswith(prefix):
                    leaf = left_path.removeprefix(prefix)
                    pair_paths.add(
                        (
                            left_path,
                            f"boundary[{step}].right.{leaf}",
                        )
                    )
        flat_rows.append(flat)

    schema = tuple(sorted(flat_rows[0]))
    if any(tuple(sorted(row)) != schema for row in flat_rows):
        raise AssertionError("scalar schema differs by start")
    quantities = {
        path: tuple(row[path] for row in flat_rows)
        for path in schema
    }
    if any(
        left not in quantities or right not in quantities
        for left, right in pair_paths
    ):
        raise AssertionError("paired leaf absent from scalar table")
    return quantities, tuple(sorted(pair_paths))


def truth_mask(values: Iterable[bool]) -> int:
    return sum(
        int(value) << start for start, value in enumerate(values)
    )


def literal(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def separator_recount(
    starts: tuple[dict[str, object], ...],
    contract: dict[str, object],
) -> dict[str, object]:
    """Re-enumerate every atom and every normalized size-two formula."""

    quantities, pair_paths = scalar_quantity_table(starts)
    all_mask = (1 << RING_STATIONS) - 1
    target_mask = 1
    atoms: list[tuple[str, str, int]] = []

    def record(
        family: str,
        expression: str,
        evaluations: Iterable[bool],
    ) -> None:
        atoms.append((family, expression, truth_mask(evaluations)))

    for path, values in sorted(quantities.items()):
        constants = tuple(
            sorted(
                set(values),
                key=lambda value: (type(value).__name__, value),
            )
        )
        for constant in constants:
            record(
                "single_literal",
                f"{path} == {literal(constant)}",
                (value == constant for value in values),
            )
            record(
                "single_literal",
                f"{path} != {literal(constant)}",
                (value != constant for value in values),
            )
        if all(type(value) is int for value in values):
            for constant in constants:
                comparisons = (
                    ("<", lambda value, c=constant: value < c),
                    ("<=", lambda value, c=constant: value <= c),
                    (">", lambda value, c=constant: value > c),
                    (">=", lambda value, c=constant: value >= c),
                )
                for operator, predicate in comparisons:
                    record(
                        "single_threshold",
                        f"{path} {operator} {constant}",
                        (predicate(value) for value in values),
                    )

    for left_path, right_path in pair_paths:
        left_values = quantities[left_path]
        right_values = quantities[right_path]
        if all(
            type(left) is type(right) is int
            for left, right in zip(left_values, right_values)
        ):
            operators = (
                ("<", lambda left, right: left < right),
                ("<=", lambda left, right: left <= right),
                ("==", lambda left, right: left == right),
                ("!=", lambda left, right: left != right),
                (">=", lambda left, right: left >= right),
                (">", lambda left, right: left > right),
            )
        elif all(
            isinstance(left, str) and isinstance(right, str)
            for left, right in zip(left_values, right_values)
        ):
            operators = (
                ("==", lambda left, right: left == right),
                ("!=", lambda left, right: left != right),
            )
        else:
            raise AssertionError(
                ("pair type mismatch", left_path, right_path)
            )
        for operator, predicate in operators:
            record(
                "pairwise_comparison",
                f"{left_path} {operator} {right_path}",
                (
                    predicate(left, right)
                    for left, right in zip(left_values, right_values)
                ),
            )

    exact_atoms = tuple(
        sorted(
            (
                {
                    "family": family,
                    "predicate": expression,
                }
                for family, expression, mask in atoms
                if mask == target_mask
            ),
            key=lambda row: (row["family"], row["predicate"]),
        )
    )
    family_counts: dict[str, int] = defaultdict(int)
    for row in exact_atoms:
        family_counts[row["family"]] += 1

    canonical_by_mask: dict[int, str] = {}
    for _family, expression, mask in atoms:
        if mask in (0, all_mask):
            continue
        previous = canonical_by_mask.get(mask)
        if previous is None or expression < previous:
            canonical_by_mask[mask] = expression
    canonical_atoms = tuple(sorted(canonical_by_mask.items()))
    size_two: set[str] = set()
    for left_index, (left_mask, left_expression) in enumerate(
        canonical_atoms
    ):
        for right_mask, right_expression in canonical_atoms[left_index:]:
            combinations = (
                ("AND", left_mask & right_mask),
                ("OR", left_mask | right_mask),
            )
            for operator, combined in combinations:
                if combined == target_mask:
                    size_two.add(
                        f"({left_expression}) {operator} "
                        f"({right_expression})"
                    )
    size_two_rows = tuple(sorted(size_two))
    best = 'token.left.program_kind == "source"'
    best_present = any(
        row["predicate"] == best for row in exact_atoms
    )
    zero_leaf_masks = (0, all_mask)
    size_zero_separates = target_mask in zero_leaf_masks
    minimal_size = (
        0
        if size_zero_separates
        else 1
        if exact_atoms
        else 2
        if size_two_rows
        else None
    )
    return {
        "grammar": contract["grammar"],
        "grammar_ast_match": contract["grammar_ast_match"],
        "scalar_quantity_count": len(quantities),
        "pairwise_quantity_pair_count": len(pair_paths),
        "atomic_predicates_enumerated": len(atoms),
        "canonical_nonconstant_atomic_truth_tables":
            len(canonical_atoms),
        "target_truth_table_start_0_to_10": "10000000000",
        "size_zero_truth_tables": zero_leaf_masks,
        "size_zero_separates": size_zero_separates,
        "size_two_boolean_separators_enumerated":
            len(size_two_rows),
        "size_two_boolean_separator_sha256": sha256(
            "\n".join(size_two_rows).encode("utf-8")
        ).hexdigest(),
        "minimal_size": minimal_size,
        "minimal_separator_count": len(exact_atoms),
        "minimal_separator_counts_by_family":
            dict(sorted(family_counts.items())),
        "minimal_separator_sha256": sha256(
            "\n".join(
                row["family"] + ":" + row["predicate"]
                for row in exact_atoms
            ).encode("utf-8")
        ).hexdigest(),
        "all_minimal_rows_have_exact_target_mask": all(
            mask == target_mask
            for _family, _expression, mask in atoms
            if mask == target_mask
        ),
        "best_separator": best,
        "best_separator_present": best_present,
    }


def split_certificate(
    fixture: dict[str, object],
    starts: tuple[dict[str, object], ...],
    enumeration: dict[str, object],
) -> dict[str, object]:
    left_kinds = tuple(
        row["token_charge_rows"][0]["program_kind"] for row in starts
    )
    predictions = tuple(
        int(kind == "source") for kind in left_kinds
    )
    observed = tuple(
        int(count > 0)
        for count in enumeration["success_counts_by_start"]
    )
    source_rows = tuple(
        station
        for station, kind in enumerate(fixture["program_kinds"])
        if kind == "source"
    )
    passed = (
        len(starts) == RING_STATIONS
        and source_rows == (0,)
        and predictions == observed == (1,) + (0,) * 10
        and enumeration["success_counts_by_start"]
        == CLAIMED_SUCCESS_COUNTS
    )
    return {
        "pass": passed,
        "finding_verbatim": FINDING_SEPARATOR,
        "module_constant_provenance": PROVENANCE,
        "program_kind_by_station_0_to_10":
            fixture["program_kinds"],
        "left_program_kind_by_start_0_to_10": left_kinds,
        "source_program_row_stations": source_rows,
        "separator_output_by_start_0_to_10": predictions,
        "satisfiable_output_by_start_0_to_10": observed,
        "success_counts_by_start_0_to_10":
            enumeration["success_counts_by_start"],
        "split": {"positive": (0,), "negative": tuple(range(1, 11))},
    }


def failure_anatomy_certificate(
    starts: tuple[dict[str, object], ...],
    enumeration: dict[str, object],
) -> dict[str, object]:
    dead = tuple(
        row
        for row in enumeration["starts"]
        if row["successful_assignment_count"] == 0
    )
    rows = []
    for row in dead:
        start = row["start"]
        boundary = starts[start]["boundary_profiles"][0]
        left_profile = boundary[2]
        right_profile = boundary[3]
        rows.append(
            {
                "start": start,
                "boundary_0_contenders": boundary[1],
                "boundary_0_order_completion_counts":
                    row["boundary_0_order_completion_counts"],
                "earliest_all_doomed_boundary":
                    row["earliest_all_doomed_boundary"],
                "left_program_kind": left_profile[0],
                "right_program_kind": right_profile[0],
            }
        )
    passed = (
        tuple(row["start"] for row in rows)
        == tuple(range(1, RING_STATIONS))
        and all(
            row["boundary_0_order_completion_counts"] == (0, 0)
            for row in rows
        )
        and all(
            row["earliest_all_doomed_boundary"] == 0
            for row in rows
        )
        and all(
            row["left_program_kind"] != "source" for row in rows
        )
        and all(
            row["complete_final_assignments"] == ASSIGNMENTS_PER_START
            for row in enumeration["starts"]
        )
    )
    return {
        "pass": passed,
        "finding_verbatim": FINDING_ANATOMY,
        "enumeration_kind": (
            "all 2048 local-order masks at each of 11 starts"
        ),
        "backward_rule": (
            "completion_count(d,state) is the exact sum of the two "
            "completion counts at d+1, with target equality at depth 11"
        ),
        "assignments_per_start": enumeration["assignments_per_start"],
        "total_assignments": enumeration["total_assignments"],
        "success_counts_by_start":
            enumeration["success_counts_by_start"],
        "failure_points": tuple(rows),
        "backward_pruning_sha256":
            enumeration["backward_pruning_sha256"],
        "left_row_signature":
            'boundary[0].left.program_kind != "source"',
    }


def mechanism_certificate(
    contract: dict[str, object],
    starts: tuple[dict[str, object], ...],
    enumeration: dict[str, object],
) -> dict[str, object]:
    rows = []
    for start_row, result in zip(starts, enumeration["starts"]):
        left_kind = start_row["token_charge_rows"][0]["program_kind"]
        rows.append(
            {
                "start": start_row["start"],
                "token_pair": start_row["initial_token_stations"],
                "left_program_kind": left_kind,
                "satisfiable":
                    result["successful_assignment_count"] > 0,
            }
        )
    source_left = tuple(
        row["start"] for row in rows
        if row["left_program_kind"] == "source"
    )
    source_left_beyond_zero = tuple(
        start for start in source_left if start != 0
    )
    start_zero_non_source_variants = tuple(
        row["token_pair"]
        for row in rows
        if row["start"] == 0
        and row["left_program_kind"] != "source"
    )
    exact_fixture_space = (
        contract["position_loop_count"] == 1
        and contract["positions_shape_match"]
        and contract["fixed_program_shape_match"]
        and contract["lawful_pair_count"] == RING_STATIONS
        and contract["lawful_pairs_unique"]
        and tuple(row["start"] for row in rows)
        == tuple(range(RING_STATIONS))
        and tuple(row["token_pair"] for row in rows)
        == contract["lawful_pairs"]
    )
    branch = (
        "c_exact_11_fixture_space_out_of_scope"
        if exact_fixture_space
        and not source_left_beyond_zero
        and not start_zero_non_source_variants
        else "unexpected_counterfactual_branch"
    )
    correlation = all(
        row["satisfiable"]
        == (row["left_program_kind"] == "source")
        for row in rows
    )
    passed = (
        branch == "c_exact_11_fixture_space_out_of_scope"
        and correlation
        and source_left == (0,)
    )
    return {
        "pass": passed,
        "finding_verbatim": FINDING_MECHANISM,
        "branch": branch,
        "lawful_start_generator_provenance":
            PROVENANCE["lawful_start_generator"],
        "lawful_program_provenance":
            PROVENANCE["program_generator"],
        "lawful_start_count": len(rows),
        "lawful_start_generator_ast_sha256":
            contract["start_generator_ast_sha256"],
        "lawful_starts_exhaustive": tuple(rows),
        "part_a_source_left_starts_beyond_start_0":
            source_left_beyond_zero,
        "part_a_testable": bool(source_left_beyond_zero),
        "part_b_start_0_non_source_variants":
            start_zero_non_source_variants,
        "part_b_testable": bool(start_zero_non_source_variants),
        "scope_ruling": FINDING_MECHANISM,
        "reason": (
            "The Cycle-752 adjacent battery fixes one program and emits "
            "exactly the 11 rotational token-pair fixtures.  It supplies "
            "neither another source-left start nor an intervention that "
            "changes start 0's left row while retaining start 0."
        ),
    }


def recount_certificate(
    recount: dict[str, object],
) -> dict[str, object]:
    passed = (
        recount["grammar_ast_match"]
        and recount["grammar"]["size_bound"] == 2
        and not recount["size_zero_separates"]
        and recount["minimal_size"] == 1
        and recount["minimal_separator_count"]
        == CLAIMED_SEPARATOR_COUNT
        and recount["all_minimal_rows_have_exact_target_mask"]
        and recount["best_separator_present"]
    )
    return {
        "pass": passed,
        "finding_verbatim": FINDING_RECOUNT,
        **recount,
    }


def core_experiment() -> dict[str, object]:
    contract = source_contract()
    fixture = build_fixture()
    starts = start_rows(fixture, contract)
    enumeration = exhaustive_satisfiability(fixture)
    recount = separator_recount(starts, contract)
    return {
        "contract": contract,
        "fixture": {
            "program_kinds": fixture["program_kinds"],
            "target_sha256": fixture["target_sha256"],
        },
        "starts": starts,
        "enumeration": enumeration,
        "split": split_certificate(fixture, starts, enumeration),
        "anatomy": failure_anatomy_certificate(starts, enumeration),
        "mechanism": mechanism_certificate(
            contract, starts, enumeration
        ),
        "recount": recount_certificate(recount),
    }


def source_controls() -> dict[str, object]:
    own_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=__file__,
    )
    own_paths = ast.literal_eval(
        ast_assignment(own_tree, "AUDIT_INPUT_PATHS")
    )
    observed = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    source_trees = {
        path: ast.parse(
            (ROOT / path).read_text(encoding="utf-8"),
            filename=path,
        )
        for path in (AUDIT_INPUT_PATHS[0], AUDIT_INPUT_PATHS[2])
    }
    required_functions = {
        AUDIT_INPUT_PATHS[0]: {
            "route3_adjacent_full_battery",
            "route3_full_battery",
            "main",
        },
        AUDIT_INPUT_PATHS[2]: {
            "separator_hunt",
            "enumerate_and_prune",
            "failure_anatomy",
        },
    }
    function_anchors = {}
    for path, tree in source_trees.items():
        names = {
            node.name
            for node in tree.body
            if isinstance(node, ast.FunctionDef)
        }
        function_anchors[path] = tuple(
            sorted(names & required_functions[path])
        )
    paths_literal = own_paths == AUDIT_INPUT_PATHS
    paths_relative = all(
        not Path(path).is_absolute() for path in own_paths
    )
    paths_exist = all((ROOT / path).is_file() for path in own_paths)
    sha_match = observed == EXPECTED_SHA256
    blocklist_active = _IMPORT_BLOCKER in sys.meta_path
    blocked_loaded = tuple(
        module
        for module in TEXT_AST_ONLY_MODULES
        if module in sys.modules
    )
    primary_import_probe_blocked = False
    primary_import_probe_message = None
    try:
        importlib.import_module(PRIMARY_MODULE)
    except ImportError as error:
        primary_import_probe_blocked = True
        primary_import_probe_message = str(error)
    primary_blocklisted = (
        PRIMARY_MODULE in TEXT_AST_ONLY_MODULES
        and PRIMARY_MODULE not in sys.modules
        and blocklist_active
        and primary_import_probe_blocked
    )
    anchors_match = all(
        set(function_anchors[path]) == required_functions[path]
        for path in required_functions
    )
    return {
        "pass": (
            paths_literal
            and paths_relative
            and paths_exist
            and sha_match
            and anchors_match
            and primary_blocklisted
            and not blocked_loaded
        ),
        "audit_input_paths_literal": own_paths,
        "all_paths_worktree_relative": paths_relative,
        "all_paths_exist": paths_exist,
        "observed_sha256": observed,
        "expected_sha256": EXPECTED_SHA256,
        "sha256_match": sha_match,
        "text_ast_only_function_anchors": function_anchors,
        "text_ast_only_modules": TEXT_AST_ONLY_MODULES,
        "cycle810_primary_import_blocklisted": primary_blocklisted,
        "cycle810_primary_import_probe_blocked":
            primary_import_probe_blocked,
        "cycle810_primary_import_probe_message":
            primary_import_probe_message,
        "blocklist_active": blocklist_active,
        "blocked_modules_loaded": blocked_loaded,
        "physics_arithmetic": (
            "exact Python integer basis states and explicit Boolean "
            "X/CNOT/TOF updates"
        ),
    }


def render_certificates(
    certificates: tuple[tuple[str, dict[str, object]], ...],
    runtime: float,
) -> str:
    passed = all(
        bool(certificate["pass"])
        for _name, certificate in certificates
    )
    lines = [
        f"{'PASS' if certificate['pass'] else 'FAIL'} {name} :: "
        f"{compact(certificate)}"
        for name, certificate in certificates
    ]
    lines.append(
        "OVERALL="
        + ("CONFIRMED" if passed else "REFUTED")
        + " mechanism_scope="
        + json.dumps(FINDING_MECHANISM)
        + f" separator_split=1/10 separator_count="
        + str(
            next(
                certificate["minimal_separator_count"]
                for name, certificate in certificates
                if name == "SEPARATOR_SET_RECOUNT"
            )
        )
        + f" runtime_seconds={runtime:.6f}"
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    started = perf_counter()
    first = core_experiment()
    second = core_experiment()
    deterministic = first == second
    first_sha = digest_json(first)
    second_sha = digest_json(second)
    deterministic = (
        deterministic
        and first_sha == second_sha
    )
    controls = source_controls()
    runtime = perf_counter() - started
    controls.update(
        {
            "pass": (
                controls["pass"]
                and deterministic
                and first["fixture"]["target_sha256"]
                == EXPECTED_TARGET_SHA256
                and runtime < RUNTIME_LIMIT_SECONDS
            ),
            "determinism_run_1_sha256": first_sha,
            "determinism_run_2_sha256": second_sha,
            "determinism_match": deterministic,
            "expected_target_sha256": EXPECTED_TARGET_SHA256,
            "observed_target_sha256":
                first["fixture"]["target_sha256"],
            "runtime_seconds": runtime,
            "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
            "runtime_within_limit": runtime < RUNTIME_LIMIT_SECONDS,
            "stdout_bytes": 0,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "stdout_within_limit": True,
        }
    )
    certificates = (
        ("SEPARATOR_VERIFICATION", first["split"]),
        ("FAILURE_ANATOMY_RE_DERIVATION", first["anatomy"]),
        ("THE_MECHANISM_TEST", first["mechanism"]),
        ("SEPARATOR_SET_RECOUNT", first["recount"]),
        ("CONTROLS", controls),
    )
    for _attempt in range(8):
        output = render_certificates(certificates, runtime)
        stdout_bytes = len(output.encode("utf-8"))
        within = stdout_bytes < STDOUT_LIMIT_BYTES
        if (
            controls["stdout_bytes"] == stdout_bytes
            and controls["stdout_within_limit"] == within
        ):
            break
        controls["stdout_bytes"] = stdout_bytes
        controls["stdout_within_limit"] = within
        controls["pass"] = controls["pass"] and within
    output = render_certificates(certificates, runtime)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if all(
        bool(certificate["pass"])
        for _name, certificate in certificates
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
