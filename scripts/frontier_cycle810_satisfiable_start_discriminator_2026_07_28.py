#!/usr/bin/env python3
"""Cycle 810: exact landed discriminator for the unique satisfiable start.

The Cycle-752, Cycle-783, and Cycle-806 copied packages are inert text/AST
audit inputs.  This runner reimplements their held 11-start fixture through
the landed Cycle-719 support API, uses an independent integer basis-state
simulator, and computes certificates A--E without importing any copied input.
"""
from __future__ import annotations

import ast
from collections import defaultdict
from functools import lru_cache
from hashlib import sha256
import importlib.abc
import json
from pathlib import Path
import subprocess
import sys
from time import perf_counter
from typing import Iterable


# Literal, existing, worktree-relative text/AST-only inputs: the 806 pair and
# the Cycle-752/783 primaries named by the task.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py",
    "scripts/frontier_cycle783_functional_order_w2_2026_07_28.py",
    "scripts/frontier_cycle806_w2_indistinguishability_2026_07_28.py",
    "scripts/frontier_cycle806_w2_independent_check_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fb50873dd30a0d580bfd03a19cc4613dd9517816e1e9aab7adba6bd77ed2c2a1",
    AUDIT_INPUT_PATHS[1]:
        "d773f3ce86d7c7f6fba9d49cddb2e9839f4dce26a30310b7b2bb5568418c94c1",
    AUDIT_INPUT_PATHS[2]:
        "d9a8cb70f3c0a99c112b7ca3e962941f7524dc743c56979ef9d4f6b06fa58c5c",
    AUDIT_INPUT_PATHS[3]:
        "2b4ff166438f1b79969639fdea00c19cef4e1bfd7fe068c54a89ab5d1580a0f2",
}
EXECUTABLE_SUPPORT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
EXPECTED_SUPPORT_SHA256 = {
    EXECUTABLE_SUPPORT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
COPIED_TEXT_ONLY_MODULES = tuple(
    Path(path).stem for path in AUDIT_INPUT_PATHS
)
RING_STATIONS = 11
FIXTURE_BANKS = 2
ASSIGNMENTS_PER_START = 1 << RING_STATIONS
EXPECTED_SUCCESS_COUNTS = (512,) + (0,) * 10
EXPECTED_TARGET_SHA256 = (
    "3513b562570c8ee4723fad82900dea66e6df5933fe40ac5e06a85bc513fea213"
)
RUNTIME_LIMIT_SECONDS = 1200.0
STDOUT_LIMIT_BYTES = 200 * 1024
ROOT = Path(__file__).resolve().parents[1]


class _CopiedInputBlocker(importlib.abc.MetaPathFinder):
    """Fail closed if executable import of a copied audit input is attempted."""

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        del path, target
        if fullname in COPIED_TEXT_ONLY_MODULES:
            raise ImportError(f"{fullname} is text/AST-only in Cycle 810")
        return None


_IMPORT_BLOCKER = _CopiedInputBlocker()
sys.meta_path.insert(0, _IMPORT_BLOCKER)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Gate = tuple[str, tuple[int, ...]]
Word = tuple[Gate, ...]
PROFILE_COMPONENTS = (
    {
        "name": "program_kind",
        "provenance": (
            f"{AUDIT_INPUT_PATHS[1]}:functional_mapping; "
            f"{AUDIT_INPUT_PATHS[2]}:PROFILE_COMPONENTS,contender_profile"
        ),
    },
    {
        "name": "program_charge_row_index",
        "provenance": (
            f"{AUDIT_INPUT_PATHS[1]}:functional_mapping; "
            f"{AUDIT_INPUT_PATHS[2]}:PROFILE_COMPONENTS,contender_profile"
        ),
    },
    {
        "name": "initial_station_occupancy",
        "provenance": (
            f"{AUDIT_INPUT_PATHS[1]}:functional_battery,functional_mapping; "
            f"{AUDIT_INPUT_PATHS[2]}:contender_profile"
        ),
    },
    {
        "name": "event_station_occupancy",
        "provenance":
            f"{AUDIT_INPUT_PATHS[2]}:PROFILE_COMPONENTS,contender_profile",
    },
    {
        "name": "initial_relay_occupancy",
        "provenance":
            f"{AUDIT_INPUT_PATHS[2]}:PROFILE_COMPONENTS,contender_profile",
    },
    {
        "name": "initial_handoff_occupancy",
        "provenance":
            f"{AUDIT_INPUT_PATHS[2]}:PROFILE_COMPONENTS,contender_profile",
    },
    {
        "name": "event_relay_occupancy",
        "provenance":
            f"{AUDIT_INPUT_PATHS[2]}:PROFILE_COMPONENTS,contender_profile",
    },
    {
        "name": "event_handoff_occupancy",
        "provenance":
            f"{AUDIT_INPUT_PATHS[2]}:PROFILE_COMPONENTS,contender_profile",
    },
    {
        "name": "semantic_gate_count",
        "provenance": (
            f"{AUDIT_INPUT_PATHS[1]}:functional_mapping; "
            f"{AUDIT_INPUT_PATHS[2]}:build_fixture,contender_profile"
        ),
    },
    {
        "name": "semantic_gate_vector_X_CNOT_TOF",
        "provenance":
            f"{AUDIT_INPUT_PATHS[2]}:build_fixture,contender_profile",
    },
    {
        "name": "physical_gate_count",
        "provenance": (
            f"{AUDIT_INPUT_PATHS[1]}:fixture,functional_mapping; "
            f"{AUDIT_INPUT_PATHS[2]}:build_fixture,contender_profile"
        ),
    },
    {
        "name": "physical_gate_vector_CNOT_TOF",
        "provenance":
            f"{AUDIT_INPUT_PATHS[2]}:build_fixture,contender_profile",
    },
    {
        "name": "token_travel_distance",
        "provenance": (
            f"{AUDIT_INPUT_PATHS[0]}:route3_adjacent_full_battery; "
            f"{AUDIT_INPUT_PATHS[2]}:contender_profile"
        ),
    },
    {
        "name": "rail_hop_distance_A_to_B",
        "provenance":
            f"{AUDIT_INPUT_PATHS[2]}:build_fixture,contender_profile",
    },
    {
        "name": "rail_hop_distance_B_to_next_A",
        "provenance":
            f"{AUDIT_INPUT_PATHS[2]}:build_fixture,contender_profile",
    },
)
PROFILE_NAMES = tuple(row["name"] for row in PROFILE_COMPONENTS)
START_QUANTITY_PROVENANCE = {
    "initial_token_stations": (
        f"{AUDIT_INPUT_PATHS[0]}:route3_adjacent_full_battery; "
        f"{AUDIT_INPUT_PATHS[1]}:functional_mapping"
    ),
    "initial_station_occupancies": (
        f"{AUDIT_INPUT_PATHS[1]}:functional_battery,functional_mapping"
    ),
    "semantic_gate_count_vectors": (
        f"{AUDIT_INPUT_PATHS[1]}:fixture,functional_mapping; "
        f"{AUDIT_INPUT_PATHS[2]}:build_fixture"
    ),
    "physical_gate_count_vectors": (
        f"{AUDIT_INPUT_PATHS[1]}:fixture,functional_mapping; "
        f"{AUDIT_INPUT_PATHS[2]}:build_fixture"
    ),
    "travel_distances": (
        f"{AUDIT_INPUT_PATHS[0]}:route3_adjacent_full_battery; "
        f"{AUDIT_INPUT_PATHS[2]}:build_fixture,contender_profile"
    ),
    "token_charge_rows": (
        f"{AUDIT_INPUT_PATHS[0]}:fixed_q_order_tick_blocks; "
        f"{AUDIT_INPUT_PATHS[1]}:functional_mapping; "
        f"{AUDIT_INPUT_PATHS[2]}:build_fixture,contender_profile"
    ),
    "boundary_profiles": (
        f"{AUDIT_INPUT_PATHS[2]}:PROFILE_COMPONENTS,contender_profile; "
        f"{AUDIT_INPUT_PATHS[3]}:PROFILE_NAMES,contender_profile_own"
    ),
}


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def freeze_word(word: Iterable[object]) -> Word:
    return tuple((gate.kind, tuple(gate.wires)) for gate in word)


def bits_to_int(bits: Iterable[int]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(bits))


def bit_digest(state: int, width: int) -> str:
    return sha256(
        bytes((state >> index) & 1 for index in range(width))
    ).hexdigest()


def apply_word_int(state: int, word: Word) -> int:
    """Exact independent X/CNOT/TOF action on a basis-state integer."""

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


def l1(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def build_fixture() -> dict[str, object]:
    """Reimplement the exact held fixture without copied-module execution."""

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
    physical_program, track = K.held_physical_program_and_track(FIXTURE_BANKS)
    if physical_program != program or len(program) != RING_STATIONS:
        raise AssertionError(("held fixture mismatch", len(program)))
    a_sites = track[::2]
    b_sites = track[1::2]
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
        "data_width": data_width,
        "initial": initial,
        "expected": expected,
        "expected_sha256": bit_digest(expected, data_width),
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
    kind, index, _local = fixture["program"][station]
    semantic_word = fixture["semantic_words"][station]
    physical_word = fixture["physical_words"][station]
    hop_out, hop_in = fixture["rail_hops"][station]
    profile: tuple[object, ...] = (
        kind,
        index,
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
    if len(profile) != 15:
        raise AssertionError(("profile width", len(profile)))
    return profile


def named_profile(profile: tuple[object, ...]) -> dict[str, object]:
    return dict(zip(PROFILE_NAMES, profile))


def start_level_data(
    fixture: dict[str, object],
) -> tuple[dict[str, object], ...]:
    """Certificate A rows: every declared landed quantity at start time."""

    rows = []
    for start in range(RING_STATIONS):
        tokens = (start, (start + 1) % RING_STATIONS)
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
                "scheduled_token_travel_distance_by_boundary":
                    tuple(2 * step for step in range(RING_STATIONS)),
                "boundary_profiles": tuple(boundaries),
            }
        )
    return tuple(rows)


def enumerate_and_prune(
    fixture: dict[str, object],
) -> dict[str, object]:
    """Complete enumeration plus backward viability pruning at every start."""

    words: tuple[Word, ...] = fixture["semantic_words"]

    @lru_cache(maxsize=None)
    def apply_macro(station: int, state: int) -> int:
        return apply_word_int(state, words[station])

    def transition(state: int, first: int, second: int) -> int:
        return apply_macro(second, apply_macro(first, state))

    start_rows = []
    for start in range(RING_STATIONS):
        prefix_states: list[dict[int, int]] = [
            {0: fixture["initial"]}
        ]
        transitions: list[dict[int, tuple[int, int]]] = []
        for step in range(RING_STATIONS):
            left = (start + step) % RING_STATIONS
            right = (left + 1) % RING_STATIONS
            layer: dict[int, tuple[int, int]] = {}
            next_prefixes: dict[int, int] = {}
            for mask, state in prefix_states[-1].items():
                if state not in layer:
                    layer[state] = (
                        transition(state, left, right),
                        transition(state, right, left),
                    )
                forward, reverse = layer[state]
                next_prefixes[mask] = forward
                next_prefixes[mask | (1 << step)] = reverse
            transitions.append(layer)
            prefix_states.append(next_prefixes)

        successful = tuple(
            mask
            for mask, state in sorted(prefix_states[-1].items())
            if state == fixture["expected"]
        )
        viable_states: list[set[int]] = [
            set() for _ in range(RING_STATIONS + 1)
        ]
        viable_states[-1] = {
            state
            for state in set(prefix_states[-1].values())
            if state == fixture["expected"]
        }
        for step in reversed(range(RING_STATIONS)):
            viable_states[step] = {
                state
                for state, destinations in transitions[step].items()
                if any(
                    destination in viable_states[step + 1]
                    for destination in destinations
                )
            }

        pruning_rows = []
        for depth, prefixes in enumerate(prefix_states):
            viable_prefixes = sum(
                state in viable_states[depth]
                for state in prefixes.values()
            )
            pruning_rows.append(
                {
                    "depth": depth,
                    "partial_assignments": len(prefixes),
                    "distinct_reachable_states": len(set(prefixes.values())),
                    "viable_partial_assignments": viable_prefixes,
                    "viable_distinct_states": len(viable_states[depth]),
                    "doomed_partial_assignments":
                        len(prefixes) - viable_prefixes,
                }
            )
        earliest_dead_boundary = next(
            (
                step
                for step in range(RING_STATIONS)
                if pruning_rows[step + 1]["viable_partial_assignments"] == 0
            ),
            None,
        )
        start_rows.append(
            {
                "start": start,
                "successful_assignment_count": len(successful),
                "successful_masks_sha256": sha256(
                    b"".join(
                        mask.to_bytes(2, "little") for mask in successful
                    )
                ).hexdigest(),
                "successful_mask_range": (
                    None
                    if not successful
                    else (successful[0], successful[-1])
                ),
                "distinct_final_outputs":
                    len(set(prefix_states[-1].values())),
                "backward_pruning": tuple(pruning_rows),
                "earliest_all_doomed_boundary": earliest_dead_boundary,
            }
        )
    return {
        "assignment_encoding": (
            "11-bit local mask; bit step=0 applies left then right and "
            "bit step=1 applies right then left"
        ),
        "assignments_per_start": ASSIGNMENTS_PER_START,
        "total_assignments":
            RING_STATIONS * ASSIGNMENTS_PER_START,
        "starts": tuple(start_rows),
        "success_counts_by_start": tuple(
            row["successful_assignment_count"] for row in start_rows
        ),
        "transition_cache": {
            "hits": apply_macro.cache_info().hits,
            "misses": apply_macro.cache_info().misses,
            "entries": apply_macro.cache_info().currsize,
        },
    }


VECTOR_COMPONENT_NAMES = {
    "semantic_gate_vector_X_CNOT_TOF": ("X", "CNOT", "TOF"),
    "physical_gate_vector_CNOT_TOF": ("CNOT", "TOF"),
}


def add_scalar(
    row: dict[str, object],
    path: str,
    name: str,
    value: object,
) -> None:
    """Flatten only declared vector quantities; identities never enter B."""

    if name in VECTOR_COMPONENT_NAMES:
        components = VECTOR_COMPONENT_NAMES[name]
        if not isinstance(value, tuple) or len(value) != len(components):
            raise AssertionError(("vector shape", path, value))
        for component, scalar in zip(components, value):
            row[f"{path}.{component}"] = scalar
    elif isinstance(value, (int, str)):
        row[path] = value
    else:
        raise AssertionError(("non-scalar quantity", path, value))


def scalar_quantity_table(
    starts: tuple[dict[str, object], ...],
) -> tuple[
    dict[str, tuple[object, ...]],
    tuple[tuple[str, str], ...],
]:
    """Build the exact scalar leaf domain used by certificate B."""

    per_start = []
    pair_paths: set[tuple[str, str]] = set()
    for start_row in starts:
        row: dict[str, object] = {}
        for station, occupied in enumerate(
            start_row["initial_station_occupancies"]
        ):
            row[f"initial_occupancy[{station}]"] = occupied
        token_by_role = {
            token["role"]: token
            for token in start_row["token_charge_rows"]
        }
        for role in ("left", "right"):
            token = token_by_role[role]
            for name, value in token.items():
                if name in ("role", "station"):
                    continue
                add_scalar(row, f"token.{role}.{name}", name, value)
        token_leaf_names = {
            path.removeprefix("token.left.")
            for path in row
            if path.startswith("token.left.")
        }
        for leaf in token_leaf_names:
            pair_paths.add(
                (f"token.left.{leaf}", f"token.right.{leaf}")
            )

        for boundary in start_row["boundary_profiles"]:
            step, _contenders, left_profile, right_profile = boundary
            for side, profile in (
                ("left", left_profile),
                ("right", right_profile),
            ):
                for name, value in zip(PROFILE_NAMES, profile):
                    add_scalar(
                        row,
                        f"boundary[{step}].{side}.{name}",
                        name,
                        value,
                    )
            left_prefix = f"boundary[{step}].left."
            for path in tuple(row):
                if path.startswith(left_prefix):
                    leaf = path.removeprefix(left_prefix)
                    pair_paths.add(
                        (
                            path,
                            f"boundary[{step}].right.{leaf}",
                        )
                    )
        per_start.append(row)
    keys = tuple(sorted(per_start[0]))
    if any(tuple(sorted(row)) != keys for row in per_start):
        raise AssertionError("scalar quantity schemas differ by start")
    quantities = {
        key: tuple(row[key] for row in per_start) for key in keys
    }
    if any(
        left not in quantities or right not in quantities
        for left, right in pair_paths
    ):
        raise AssertionError("pairwise path escaped scalar table")
    return quantities, tuple(sorted(pair_paths))


def truth_mask(values: Iterable[bool]) -> int:
    return sum(
        int(value) << start for start, value in enumerate(values)
    )


def literal(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def separator_hunt(
    starts: tuple[dict[str, object], ...],
) -> dict[str, object]:
    """Exhaust the declared predicate grammar through two atomic leaves."""

    quantities, pair_paths = scalar_quantity_table(starts)
    target_mask = 1
    all_mask = (1 << RING_STATIONS) - 1
    atoms: list[dict[str, object]] = []

    def add_atom(
        family: str,
        expression: str,
        evaluations: Iterable[bool],
    ) -> None:
        atoms.append(
            {
                "family": family,
                "expression": expression,
                "mask": truth_mask(evaluations),
            }
        )

    for path, values in sorted(quantities.items()):
        constants = tuple(
            sorted(set(values), key=lambda value: (type(value).__name__, value))
        )
        for constant in constants:
            add_atom(
                "single_literal",
                f"{path} == {literal(constant)}",
                (value == constant for value in values),
            )
            add_atom(
                "single_literal",
                f"{path} != {literal(constant)}",
                (value != constant for value in values),
            )
        if all(type(value) is int for value in values):
            for constant in constants:
                for operator, predicate in (
                    ("<", lambda value, c=constant: value < c),
                    ("<=", lambda value, c=constant: value <= c),
                    (">", lambda value, c=constant: value > c),
                    (">=", lambda value, c=constant: value >= c),
                ):
                    add_atom(
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
                ("pairwise type mismatch", left_path, right_path)
            )
        for operator, predicate in operators:
            add_atom(
                "pairwise_comparison",
                f"{left_path} {operator} {right_path}",
                (
                    predicate(left, right)
                    for left, right in zip(left_values, right_values)
                ),
            )

    # The size-two Boolean grammar is quotiented by atomic truth table.  This
    # is an explicit semantic normalization, not sampling: on 11 starts every
    # atom has exactly one of 2^11 possible masks.
    canonical_by_mask: dict[int, str] = {}
    for atom in atoms:
        mask = atom["mask"]
        expression = atom["expression"]
        if mask in (0, all_mask):
            continue
        previous = canonical_by_mask.get(mask)
        if previous is None or expression < previous:
            canonical_by_mask[mask] = expression
    canonical_atoms = tuple(sorted(canonical_by_mask.items()))
    size_two_separators = []
    for left_index, (left_mask, left_expression) in enumerate(
        canonical_atoms
    ):
        for right_mask, right_expression in canonical_atoms[left_index:]:
            for operator, combined in (
                ("AND", left_mask & right_mask),
                ("OR", left_mask | right_mask),
            ):
                if combined == target_mask:
                    size_two_separators.append(
                        f"({left_expression}) {operator} "
                        f"({right_expression})"
                    )
    size_two_separators = sorted(set(size_two_separators))
    atomic_separators = tuple(
        sorted(
            (
                {
                    "family": atom["family"],
                    "predicate": atom["expression"],
                }
                for atom in atoms
                if atom["mask"] == target_mask
            ),
            key=lambda row: (row["family"], row["predicate"]),
        )
    )
    if atomic_separators:
        minimal_size = 1
        minimal_separators = atomic_separators
    else:
        minimal_size = 2 if size_two_separators else None
        minimal_separators = tuple(
            {
                "family": "boolean_size_2",
                "predicate": expression,
            }
            for expression in size_two_separators
        )
    best_expression = 'token.left.program_kind == "source"'
    best_present = any(
        row["predicate"] == best_expression for row in minimal_separators
    )
    family_counts: dict[str, int] = defaultdict(int)
    for row in minimal_separators:
        family_counts[row["family"]] += 1
    return {
        "pass": bool(minimal_separators) and best_present,
        "grammar": {
            "scalar_leaf_domain": (
                "every scalar component of all 15-component boundary "
                "profiles, both initial token/charge rows, and the absolute "
                "initial occupancy vector; station/start identity labels "
                "are excluded"
            ),
            "single_literal_atom": "q == c | q != c for every observed c",
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
            "minimality": (
                "globally least atomic-leaf size among exact separators"
            ),
            "boolean_semantic_quotient": (
                "one lexicographic representative per complete 11-bit "
                "atomic truth table; constants removed as Boolean identities"
            ),
        },
        "scalar_quantity_count": len(quantities),
        "pairwise_quantity_pair_count": len(pair_paths),
        "atomic_predicates_enumerated": len(atoms),
        "canonical_nonconstant_atomic_truth_tables":
            len(canonical_atoms),
        "size_two_boolean_separators_enumerated":
            len(size_two_separators),
        "size_two_boolean_separator_sha256": sha256(
            "\n".join(size_two_separators).encode("utf-8")
        ).hexdigest(),
        "size_two_minimal": minimal_size == 2,
        "size_two_nonminimal_reason": (
            None
            if minimal_size != 1
            else "size-one exact separators exist"
        ),
        "target_truth_table_start_0_to_10": "10000000000",
        "minimal_size": minimal_size,
        "minimal_separator_count": len(minimal_separators),
        "minimal_separator_counts_by_family":
            dict(sorted(family_counts.items())),
        "minimal_separators": minimal_separators,
        "best_separator": {
            "predicate": best_expression,
            "reason": (
                "one landed categorical read on the initial left token; "
                "no threshold, comparison, future profile, or Boolean join"
            ),
        },
    }


def failure_anatomy(
    fixture: dict[str, object],
    starts: tuple[dict[str, object], ...],
    enumeration: dict[str, object],
) -> dict[str, object]:
    """Certificate C: first all-doomed boundary and its common signature."""

    dead_rows = tuple(
        row
        for row in enumeration["starts"]
        if row["successful_assignment_count"] == 0
    )
    live_rows = tuple(
        row
        for row in enumeration["starts"]
        if row["successful_assignment_count"] > 0
    )
    failure_rows = []
    full_pairs = []
    for row in dead_rows:
        start = row["start"]
        step = row["earliest_all_doomed_boundary"]
        boundary = starts[start]["boundary_profiles"][step]
        _boundary_step, contenders, left_profile, right_profile = boundary
        full_pairs.append((left_profile, right_profile))
        failure_rows.append(
            {
                "start": start,
                "earliest_all_doomed_boundary": step,
                "contenders": contenders,
                "partial_assignments_after_boundary":
                    row["backward_pruning"][step + 1][
                        "partial_assignments"
                    ],
                "viable_partial_assignments_after_boundary":
                    row["backward_pruning"][step + 1][
                        "viable_partial_assignments"
                    ],
                "left_program_kind": left_profile[0],
                "right_program_kind": right_profile[0],
            }
        )

    shared_equal_components = []
    discriminating_equal_components = []
    success_boundary = starts[0]["boundary_profiles"][0]
    for side_name, profile_index in (("left", 0), ("right", 1)):
        for component_index, component_name in enumerate(PROFILE_NAMES):
            values = tuple(
                pair[profile_index][component_index]
                for pair in full_pairs
            )
            if len(set(values)) == 1:
                record = {
                    "side": side_name,
                    "component": component_name,
                    "value": values[0],
                }
                shared_equal_components.append(record)
                success_value = success_boundary[profile_index + 2][
                    component_index
                ]
                if success_value != values[0]:
                    discriminating_equal_components.append(
                        {
                            **record,
                            "start_0_value": success_value,
                        }
                    )
    mechanism_holds = (
        all(
            fixture["program"][row["start"]][0] != "source"
            for row in dead_rows
        )
        and fixture["program"][0][0] == "source"
    )
    pruning_projection = tuple(
        {
            "start": row["start"],
            "earliest": row["earliest_all_doomed_boundary"],
            "layers": row["backward_pruning"],
        }
        for row in enumeration["starts"]
    )
    return {
        "pass": (
            tuple(row["start"] for row in dead_rows)
            == tuple(range(1, RING_STATIONS))
            and len(live_rows) == 1
            and all(
                row["earliest_all_doomed_boundary"] == 0
                for row in dead_rows
            )
            and mechanism_holds
        ),
        "backward_pruning_definition": (
            "a reachable state at depth d is viable iff one of its two "
            "transitions reaches a viable state at d+1; the final viable "
            "set is the exact allocator target"
        ),
        "failure_point_map": {
            str(row["start"]): row["earliest_all_doomed_boundary"]
            for row in dead_rows
        },
        "failure_points": tuple(failure_rows),
        "backward_pruning_sha256": sha256(
            compact(pruning_projection).encode("utf-8")
        ).hexdigest(),
        "full_15_component_profile_pair_common":
            len(set(full_pairs)) == 1,
        "distinct_full_failure_profile_pairs": len(set(full_pairs)),
        "shared_exact_profile_components":
            tuple(shared_equal_components),
        "shared_exact_components_excluding_start_0":
            tuple(discriminating_equal_components),
        "common_discriminating_predicate_signature": {
            "predicate":
                'boundary[0].left.program_kind != "source"',
            "holds_at_all_10_failure_points": mechanism_holds,
            "holds_at_start_0": False,
            "equivalent_start_form":
                'token.left.program_kind != "source"',
        },
        "signature_outcome": (
            "No single full profile pair, and no exact scalar equality "
            "exclusive to all failures.  A common discriminating predicate "
            "does exist: every all-doomed boundary-0 row lacks source on "
            "the left; start 0 has source there."
        ),
        "mechanism_scope": (
            "necessary-and-sufficient bounded signature on this complete "
            "11-start battery; not a causal theorem for other fixtures"
        ),
    }


def landed_computability(
    separators: dict[str, object],
    anatomy: dict[str, object],
) -> dict[str, object]:
    expression = 'token.left.program_kind == "source"'
    constructive = (
        separators["best_separator"]["predicate"] == expression
        and anatomy["common_discriminating_predicate_signature"][
            "holds_at_all_10_failure_points"
        ]
    )
    return {
        "pass": constructive,
        "classification":
            "COMPUTABLE_FROM_LANDED_LOCAL_QUANTITIES_AT_START",
        "constructive_function": (
            "D(start_data) = int("
            'start_data.token_charge_rows[left].program_kind == "source")'
        ),
        "input_quantity": (
            "program_kind on the initially occupied left token/charge row"
        ),
        "output_on_starts_0_to_10": (1,) + (0,) * 10,
        "non_landed_information_required": (),
        "ruling": (
            "The unique satisfiable start is decidable at start time from "
            "one landed local row-kind read.  Future simulated states, "
            "boundary choices, target output, and start/station identity "
            "are not inputs to D."
        ),
        "scope_caveat": (
            "This classifies the held Cycle-752 battery exactly; it does "
            "not promote source alignment to a universal sufficiency law."
        ),
    }


def assignment_value(tree: ast.Module, name: str) -> ast.expr:
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


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def command_output(arguments: tuple[str, ...]) -> str:
    return subprocess.run(
        arguments,
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def source_controls() -> dict[str, object]:
    own_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )
    own_paths = ast.literal_eval(
        assignment_value(own_tree, "AUDIT_INPUT_PATHS")
    )
    observed = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    support_observed = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in EXECUTABLE_SUPPORT_PATHS
    }
    required = {
        AUDIT_INPUT_PATHS[0]: {
            "allocator_expected",
            "fixed_q_order_tick_blocks",
            "route3_adjacent_full_battery",
        },
        AUDIT_INPUT_PATHS[1]: {
            "fixture",
            "functional_battery",
            "functional_mapping",
        },
        AUDIT_INPUT_PATHS[2]: {
            "build_fixture",
            "contender_profile",
            "enumerate_success_assignments",
        },
        AUDIT_INPUT_PATHS[3]: {
            "build_fixture_own",
            "contender_profile_own",
            "enumerate_direct",
        },
    }
    anchors = {}
    for path in AUDIT_INPUT_PATHS:
        tree = ast.parse(
            (ROOT / path).read_text(encoding="utf-8"), filename=path
        )
        anchors[path] = tuple(sorted(required[path] & function_names(tree)))
    branch = command_output(("git", "branch", "--show-current"))
    head = command_output(("git", "rev-parse", "HEAD"))
    required_parent = "c1b3f8fd2c7626e8b0a9be3f6c8b80fa418ba999"
    parent_is_ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", required_parent, "HEAD"),
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    ).returncode == 0
    return {
        "pass": (
            own_paths == AUDIT_INPUT_PATHS
            and all(not Path(path).is_absolute() for path in own_paths)
            and all((ROOT / path).is_file() for path in own_paths)
            and observed == EXPECTED_SHA256
            and support_observed == EXPECTED_SUPPORT_SHA256
            and all(
                set(anchors[path]) == required[path]
                for path in AUDIT_INPUT_PATHS
            )
            and _IMPORT_BLOCKER in sys.meta_path
            and not any(
                module in sys.modules
                for module in COPIED_TEXT_ONLY_MODULES
            )
            and branch == "physics-loop/proof-grade-blockF12-20260729"
            and parent_is_ancestor
        ),
        "audit_input_paths_literal": own_paths,
        "all_paths_worktree_relative":
            all(not Path(path).is_absolute() for path in own_paths),
        "all_paths_exist":
            all((ROOT / path).is_file() for path in own_paths),
        "observed_sha256": observed,
        "expected_sha256": EXPECTED_SHA256,
        "sha256_match": observed == EXPECTED_SHA256,
        "text_ast_only_function_anchors": anchors,
        "import_blocklist": COPIED_TEXT_ONLY_MODULES,
        "blocklist_active": _IMPORT_BLOCKER in sys.meta_path,
        "blocked_modules_loaded": tuple(
            module
            for module in COPIED_TEXT_ONLY_MODULES
            if module in sys.modules
        ),
        "executable_support_paths": EXECUTABLE_SUPPORT_PATHS,
        "support_observed_sha256": support_observed,
        "support_expected_sha256": EXPECTED_SUPPORT_SHA256,
        "support_sha256_match":
            support_observed == EXPECTED_SUPPORT_SHA256,
        "git_branch": branch,
        "git_head": head,
        "required_parent_f11_sha": required_parent,
        "required_parent_is_ancestor": parent_is_ancestor,
        "third_party_packages": (),
        "physics_arithmetic": (
            "exact Python integer basis states and Boolean X/CNOT/TOF "
            "updates; runtime timing is the only floating-point quantity"
        ),
    }


def station_landed_table(
    fixture: dict[str, object],
) -> tuple[dict[str, object], ...]:
    rows = []
    for station, program_row in enumerate(fixture["program"]):
        rows.append(
            {
                "station": station,
                "program_kind": program_row[0],
                "program_charge_row_index": program_row[1],
                "semantic_gate_count":
                    len(fixture["semantic_words"][station]),
                "semantic_gate_vector_X_CNOT_TOF":
                    fixture["semantic_vectors"][station],
                "physical_gate_count":
                    len(fixture["physical_words"][station]),
                "physical_gate_vector_CNOT_TOF":
                    fixture["physical_vectors"][station],
                "rail_hop_distance_A_to_B":
                    fixture["rail_hops"][station][0],
                "rail_hop_distance_B_to_next_A":
                    fixture["rail_hops"][station][1],
            }
        )
    return tuple(rows)


def core_experiment() -> dict[str, object]:
    fixture = build_fixture()
    starts = start_level_data(fixture)
    enumeration = enumerate_and_prune(fixture)
    separators = separator_hunt(starts)
    anatomy = failure_anatomy(fixture, starts, enumeration)
    computability = landed_computability(separators, anatomy)
    return {
        "fixture": fixture,
        "starts": starts,
        "station_table": station_landed_table(fixture),
        "enumeration": enumeration,
        "separators": separators,
        "anatomy": anatomy,
        "computability": computability,
    }


def main() -> int:
    started = perf_counter()
    first = core_experiment()
    second = core_experiment()
    fixture = first["fixture"]
    starts = first["starts"]
    enumeration = first["enumeration"]
    separators = first["separators"]
    anatomy = first["anatomy"]
    computability = first["computability"]
    certificate_a = {
        "pass": (
            len(PROFILE_COMPONENTS) == 15
            and len(starts) == RING_STATIONS
            and all(
                len(row["boundary_profiles"]) == RING_STATIONS
                for row in starts
            )
            and fixture["expected_sha256"] == EXPECTED_TARGET_SHA256
        ),
        "profile_value_encoding": (
            "each boundary row is (step,(left_station,right_station),"
            "left_profile,right_profile); each profile is ordered exactly "
            "by profile_component_names"
        ),
        "profile_component_names": PROFILE_NAMES,
        "profile_components": PROFILE_COMPONENTS,
        "start_quantity_provenance": START_QUANTITY_PROVENANCE,
        "global_station_landed_table": first["station_table"],
        "starts": starts,
    }
    certificate_b = separators
    certificate_c = {
        **anatomy,
        "complete_enumeration": {
            "assignment_encoding": enumeration["assignment_encoding"],
            "assignments_per_start":
                enumeration["assignments_per_start"],
            "total_assignments": enumeration["total_assignments"],
            "success_counts_by_start":
                enumeration["success_counts_by_start"],
            "expected_success_counts_by_start":
                EXPECTED_SUCCESS_COUNTS,
            "per_start": tuple(
                {
                    "start": row["start"],
                    "successful_assignment_count":
                        row["successful_assignment_count"],
                    "successful_masks_sha256":
                        row["successful_masks_sha256"],
                    "successful_mask_range":
                        row["successful_mask_range"],
                    "distinct_final_outputs":
                        row["distinct_final_outputs"],
                    "earliest_all_doomed_boundary":
                        row["earliest_all_doomed_boundary"],
                }
                for row in enumeration["starts"]
            ),
            "transition_cache": enumeration["transition_cache"],
        },
    }
    certificate_d = computability
    controls = source_controls()
    first_projection = {
        "starts": first["starts"],
        "station_table": first["station_table"],
        "enumeration": first["enumeration"],
        "separators": first["separators"],
        "anatomy": first["anatomy"],
        "computability": first["computability"],
    }
    second_projection = {
        "starts": second["starts"],
        "station_table": second["station_table"],
        "enumeration": second["enumeration"],
        "separators": second["separators"],
        "anatomy": second["anatomy"],
        "computability": second["computability"],
    }
    first_digest = sha256(
        compact(first_projection).encode("utf-8")
    ).hexdigest()
    second_digest = sha256(
        compact(second_projection).encode("utf-8")
    ).hexdigest()
    deterministic = (
        first_projection == second_projection
        and first_digest == second_digest
    )
    runtime = perf_counter() - started
    controls.update(
        {
            "pass": (
                controls["pass"]
                and deterministic
                and enumeration["success_counts_by_start"]
                == EXPECTED_SUCCESS_COUNTS
                and fixture["expected_sha256"]
                == EXPECTED_TARGET_SHA256
                and runtime < RUNTIME_LIMIT_SECONDS
            ),
            "determinism_run_1_sha256": first_digest,
            "determinism_run_2_sha256": second_digest,
            "determinism_match": deterministic,
            "expected_target_sha256": EXPECTED_TARGET_SHA256,
            "observed_target_sha256": fixture["expected_sha256"],
            "runtime_seconds": runtime,
            "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
            "runtime_within_limit": runtime < RUNTIME_LIMIT_SECONDS,
            "stdout_bytes": 0,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "stdout_within_limit": True,
        }
    )
    certificates = (
        ("CERTIFICATE_A_START_LEVEL_DATA", certificate_a),
        ("CERTIFICATE_B_SEPARATOR_HUNT", certificate_b),
        ("CERTIFICATE_C_FAILURE_ANATOMY", certificate_c),
        ("CERTIFICATE_D_LANDED_COMPUTABILITY", certificate_d),
        ("CERTIFICATE_E_CONTROLS", controls),
    )

    def render() -> str:
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
            + f" separator_count="
            + str(separators["minimal_separator_count"])
            + " best_separator="
            + json.dumps(separators["best_separator"]["predicate"])
            + " failure_signature="
            + json.dumps(
                anatomy["common_discriminating_predicate_signature"][
                    "predicate"
                ]
            )
            + " computability="
            + computability["classification"]
            + f" runtime_seconds={runtime:.6f}"
        )
        return "\n".join(lines) + "\n"

    for _attempt in range(8):
        output = render()
        size = len(output.encode("utf-8"))
        within = size < STDOUT_LIMIT_BYTES
        if (
            controls["stdout_bytes"] == size
            and controls["stdout_within_limit"] == within
        ):
            break
        controls["stdout_bytes"] = size
        controls["stdout_within_limit"] = within
        controls["pass"] = controls["pass"] and within
    output = render()
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if all(
        bool(certificate["pass"]) for _name, certificate in certificates
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
