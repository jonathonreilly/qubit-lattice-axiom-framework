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
                {
                    "step": step,
                    "contenders": (left, right),
                    "left_profile":
                        named_profile(
                            contender_profile(
                                fixture, start, step, left
                            )
                        ),
                    "right_profile":
                        named_profile(
                            contender_profile(
                                fixture, start, step, right
                            )
                        ),
                }
            )
        rows.append(
            {
                "start": start,
                "initial_token_stations": tokens,
                "initial_station_occupancies": occupancy,
                "token_charge_rows": tuple(token_rows),
                "station_semantic_gate_counts": tuple(
                    len(word) for word in fixture["semantic_words"]
                ),
                "station_semantic_gate_vectors_X_CNOT_TOF":
                    fixture["semantic_vectors"],
                "station_physical_gate_counts": tuple(
                    len(word) for word in fixture["physical_words"]
                ),
                "station_physical_gate_vectors_CNOT_TOF":
                    fixture["physical_vectors"],
                "station_rail_hop_distances_A_to_B_to_next_A":
                    fixture["rail_hops"],
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
                "successful_masks": successful,
                "successful_assignment_count": len(successful),
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


def main() -> int:
    started = perf_counter()
    fixture = build_fixture()
    starts = start_level_data(fixture)
    enumeration = enumerate_and_prune(fixture)
    certificate_a = {
        "pass": (
            len(PROFILE_COMPONENTS) == 15
            and len(starts) == RING_STATIONS
            and all(
                len(row["boundary_profiles"]) == RING_STATIONS
                for row in starts
            )
        ),
        "profile_components": PROFILE_COMPONENTS,
        "start_quantity_provenance": START_QUANTITY_PROVENANCE,
        "starts": starts,
    }
    certificate_c_partial = {
        "pass":
            enumeration["success_counts_by_start"]
            == EXPECTED_SUCCESS_COUNTS,
        "enumeration": enumeration,
    }
    runtime = perf_counter() - started
    output = "\n".join(
        (
            "PASS CERTIFICATE_A_START_LEVEL_DATA :: "
            + compact(certificate_a),
            (
                "PASS" if certificate_c_partial["pass"] else "FAIL"
            )
            + " CERTIFICATE_C_ENUMERATION_BASE :: "
            + compact(certificate_c_partial),
            f"OVERALL=INCREMENTAL_BASE runtime_seconds={runtime:.6f}",
        )
    ) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if certificate_a["pass"] and certificate_c_partial["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
