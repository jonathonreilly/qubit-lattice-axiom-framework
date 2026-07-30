#!/usr/bin/env python3
"""Cycle 806: decide W2 at the complete landed-local profile scope.

The four Cycle-752/783 sources are inert text/AST audit inputs.  This runner
reimplements their held adjacent-start experiment with an exact integer
basis-state simulator, enumerates all 2^11 complete pair-order assignments
for every start, extracts forced boundaries, and performs the requested
unordered-profile-pair collision census.

An empty successful-assignment set is kept distinct from FLEXIBLE: no order
is forced by an empty set, and no lookup table can repair such a fixture.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
import importlib.abc
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Iterable


# Literal, worktree-relative, and exactly the four copied primary packages.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py",
    "scripts/frontier_cycle752_adjacency_independent_check_2026_07_28.py",
    "scripts/frontier_cycle783_functional_order_w2_2026_07_28.py",
    "scripts/frontier_cycle783_order_independent_check_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fb50873dd30a0d580bfd03a19cc4613dd9517816e1e9aab7adba6bd77ed2c2a1",
    AUDIT_INPUT_PATHS[1]:
        "cfff6c6c8acf971c78682caec55f2bd70d661cd21e70d619ef1e1087fc412fd2",
    AUDIT_INPUT_PATHS[2]:
        "d773f3ce86d7c7f6fba9d49cddb2e9839f4dce26a30310b7b2bb5568418c94c1",
    AUDIT_INPUT_PATHS[3]:
        "e28fc9421d7a50befa08e930f7efe1835320627d8aa28fae4a1cdb161c359c64",
}

# The copied independent checker imports this landed support module.  Cycle
# 806 uses it only to reconstruct the fixture objects; all census execution
# below is this runner's own integer simulator.
EXECUTABLE_SUPPORT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
EXPECTED_SUPPORT_SHA256 = {
    EXECUTABLE_SUPPORT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}

IMPORT_BLOCKLIST = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)
RING_STATIONS = 11
FIXTURE_BANKS = 2
COMPLETE_ASSIGNMENTS = 1 << RING_STATIONS
EXPECTED_TWO_SOURCE_SHA256 = (
    "3513b562570c8ee4723fad82900dea66e6df5933fe40ac5e06a85bc513fea213"
)
EXPECTED_FIXED_CLASS_HISTOGRAM = {0: 1535, 1: 511}
RUNTIME_LIMIT_SECONDS = 1500.0
STDOUT_LIMIT_BYTES = 200 * 1024
ROOT = Path(__file__).resolve().parents[1]


class _CopiedPrimaryImportBlocker(importlib.abc.MetaPathFinder):
    """Fail closed on executable imports of all four copied primaries."""

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        del path, target
        if fullname in IMPORT_BLOCKLIST:
            raise ImportError(
                f"{fullname} is a Cycle-806 text/AST-only audit input"
            )
        return None


_IMPORT_BLOCKER = _CopiedPrimaryImportBlocker()
sys.meta_path.insert(0, _IMPORT_BLOCKER)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


OUTPUT_LINES: list[str] = []
CHECKS: dict[str, bool] = {}


def compact_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def emit(label: str, value: object) -> None:
    OUTPUT_LINES.append(f"{label}={compact_json(value)}")


def check(label: str, condition: bool, detail: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact_json(detail)}"
    )
    return passed


def _assignment_value(tree: ast.AST, name: str) -> ast.expr:
    rows: list[ast.expr] = []
    for node in getattr(tree, "body", ()):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            rows.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            rows.append(node.value)
    if len(rows) != 1:
        raise AssertionError(("assignment census", name, len(rows)))
    return rows[0]


def _function_names(tree: ast.AST) -> set[str]:
    return {
        node.name
        for node in getattr(tree, "body", ())
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_and_blocklist_certificate() -> dict[str, object]:
    own_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )
    own_literal = ast.literal_eval(
        _assignment_value(own_tree, "AUDIT_INPUT_PATHS")
    )
    observed = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    support_observed = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in EXECUTABLE_SUPPORT_PATHS
    }
    trees = {
        path: ast.parse(
            (ROOT / path).read_text(encoding="utf-8"), filename=path
        )
        for path in AUDIT_INPUT_PATHS
    }
    required_functions = {
        AUDIT_INPUT_PATHS[0]: {
            "allocator_expected",
            "route3_adjacent_full_battery",
            "route3_order_dependence_census",
        },
        AUDIT_INPUT_PATHS[1]: {
            "apply_word_own",
            "route3_full_battery_own",
            "witness_verification_certificate",
        },
        AUDIT_INPUT_PATHS[2]: {
            "fixture",
            "functional_battery",
            "functional_mapping",
            "exhaustive_fixed_order_classes",
        },
        AUDIT_INPUT_PATHS[3]: {
            "fixture",
            "event_surface",
            "mapping_fidelity_attack",
            "alternative_functional_hunt",
            "exhaustive_fixed_order_recount",
        },
    }
    functions_present = {
        path: sorted(required_functions[path])
        for path, tree in trees.items()
        if required_functions[path] <= _function_names(tree)
    }
    blocked_loaded = sorted(
        module for module in IMPORT_BLOCKLIST if module in sys.modules
    )
    return {
        "audit_input_paths_literal": own_literal,
        "all_paths_relative": all(
            not Path(path).is_absolute() for path in own_literal
        ),
        "all_paths_exist": all((ROOT / path).is_file() for path in own_literal),
        "observed_sha256": observed,
        "expected_sha256": EXPECTED_SHA256,
        "sha256_match": observed == EXPECTED_SHA256,
        "text_ast_only_function_anchors": functions_present,
        "all_function_anchors_present":
            len(functions_present) == len(required_functions),
        "import_blocklist": IMPORT_BLOCKLIST,
        "blocked_modules_loaded": blocked_loaded,
        "blocklist_active": _IMPORT_BLOCKER in sys.meta_path,
        "executable_support_paths": EXECUTABLE_SUPPORT_PATHS,
        "support_observed_sha256": support_observed,
        "support_expected_sha256": EXPECTED_SUPPORT_SHA256,
        "support_sha256_match": support_observed == EXPECTED_SUPPORT_SHA256,
        "simulation_arithmetic": (
            "exact Python integers and Boolean X/CNOT/TOF updates; "
            "no floating-point physics values"
        ),
        "third_party_packages": (),
    }


Gate = tuple[str, tuple[int, ...]]
Word = tuple[Gate, ...]


def freeze_word(word: Iterable[object]) -> Word:
    return tuple((gate.kind, tuple(gate.wires)) for gate in word)


def bits_to_int(bits: Iterable[int]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(bits))


def int_bit_digest(state: int, width: int) -> str:
    return sha256(bytes((state >> index) & 1 for index in range(width))).hexdigest()


def apply_word_int(state: int, word: Word) -> int:
    """Independent exact basis-state simulator for the lineage gate basis."""

    for kind, wires in word:
        if kind == "X":
            state ^= 1 << wires[0]
        elif kind == "CNOT":
            if state & (1 << wires[0]):
                state ^= 1 << wires[1]
        elif kind == "TOF":
            if (
                state & (1 << wires[0])
                and state & (1 << wires[1])
            ):
                state ^= 1 << wires[2]
        else:
            raise AssertionError(("unsupported gate kind", kind))
    return state


def l1(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def build_fixture() -> dict[str, object]:
    """Reimplement the exact held fixture used by the 752/783 lineage."""

    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    data_bits = K.M.prepare_endpoint(K.M.pack_state(banks, links), (1, 0))
    semantic_objects = tuple(K.mapped_macro(row) for row in program)
    semantic_words = tuple(freeze_word(word) for word in semantic_objects)
    data_width = len(data_bits)
    physical_objects = tuple(
        K.controlled_macro(
            semantic_objects[station],
            data_width + station,
            data_width + 2 * RING_STATIONS + station,
        )
        for station in range(RING_STATIONS)
    )
    physical_words = tuple(freeze_word(word) for word in physical_objects)
    semantic_vectors = tuple(
        tuple(sum(kind == wanted for kind, _ in word) for wanted in ("X", "CNOT", "TOF"))
        for word in semantic_words
    )
    physical_vectors = tuple(
        tuple(sum(kind == wanted for kind, _ in word) for wanted in ("CNOT", "TOF"))
        for word in physical_words
    )
    physical_program, track = K.held_physical_program_and_track(FIXTURE_BANKS)
    if physical_program != program or len(program) != RING_STATIONS:
        raise AssertionError(("held program mismatch", len(program)))
    a_sites = track[::2]
    b_sites = track[1::2]
    rail_hops = tuple(
        (
            l1(a_sites[station], b_sites[station]),
            l1(b_sites[station], a_sites[(station + 1) % RING_STATIONS]),
        )
        for station in range(RING_STATIONS)
    )
    initial = bits_to_int(data_bits)
    allocator = freeze_word(K.M.global_allocator_word(FIXTURE_BANKS))
    expected = apply_word_int(apply_word_int(initial, allocator), allocator)
    return {
        "program": program,
        "data_width": data_width,
        "initial": initial,
        "semantic_words": semantic_words,
        "semantic_vectors": semantic_vectors,
        "physical_words": physical_words,
        "physical_vectors": physical_vectors,
        "physical_counts": tuple(len(word) for word in physical_words),
        "rail_hops": rail_hops,
        "expected": expected,
        "expected_sha256": int_bit_digest(expected, data_width),
    }


PROFILE_COMPONENTS = (
    {
        "name": "program_kind",
        "source": (
            f"{AUDIT_INPUT_PATHS[2]}:functional_mapping; "
            f"{AUDIT_INPUT_PATHS[3]}:event_surface,mapping_fidelity_attack"
        ),
        "meaning": "local source/bank/cross/relay/handoff/finalizer row kind",
    },
    {
        "name": "program_charge_row_index",
        "source": (
            f"{AUDIT_INPUT_PATHS[2]}:functional_mapping; "
            f"{AUDIT_INPUT_PATHS[3]}:mapping_fidelity_attack"
        ),
        "meaning": "local bank/edge charge-row index carried by the program row",
    },
    {
        "name": "initial_station_occupancy",
        "source": (
            f"{AUDIT_INPUT_PATHS[2]}:functional_battery,functional_mapping; "
            f"{AUDIT_INPUT_PATHS[3]}:mapping_fidelity_attack"
        ),
        "meaning": "initial A-token occupancy at the contender station",
    },
    {
        "name": "event_station_occupancy",
        "source": (
            f"{AUDIT_INPUT_PATHS[3]}:event_surface,mapping_fidelity_attack"
        ),
        "meaning": "event-local occupied-A selector for the Q contender",
    },
    {
        "name": "initial_relay_occupancy",
        "source": f"{AUDIT_INPUT_PATHS[3]}:alternative_functional_hunt",
        "meaning": "initial station occupancy restricted to relay rows",
    },
    {
        "name": "initial_handoff_occupancy",
        "source": f"{AUDIT_INPUT_PATHS[3]}:alternative_functional_hunt",
        "meaning": "initial station occupancy restricted to handoff rows",
    },
    {
        "name": "event_relay_occupancy",
        "source": f"{AUDIT_INPUT_PATHS[3]}:alternative_functional_hunt",
        "meaning": "event-local contender restricted to relay rows",
    },
    {
        "name": "event_handoff_occupancy",
        "source": f"{AUDIT_INPUT_PATHS[3]}:alternative_functional_hunt",
        "meaning": "event-local contender restricted to handoff rows",
    },
    {
        "name": "semantic_gate_count",
        "source": (
            f"{AUDIT_INPUT_PATHS[2]}:functional_mapping; "
            f"{AUDIT_INPUT_PATHS[3]}:mapping_fidelity_attack"
        ),
        "meaning": "gate count of the landed station-local mapped macro",
    },
    {
        "name": "semantic_gate_vector_X_CNOT_TOF",
        "source": f"{AUDIT_INPUT_PATHS[3]}:fixture,alternative_functional_hunt",
        "meaning": "per-kind semantic gate-count vector",
    },
    {
        "name": "physical_gate_count",
        "source": (
            f"{AUDIT_INPUT_PATHS[2]}:fixture,functional_mapping; "
            f"{AUDIT_INPUT_PATHS[3]}:fixture,mapping_fidelity_attack"
        ),
        "meaning": "first-Q controlled physical gate count",
    },
    {
        "name": "physical_gate_vector_CNOT_TOF",
        "source": f"{AUDIT_INPUT_PATHS[3]}:fixture,alternative_functional_hunt",
        "meaning": "per-kind first-Q physical gate-count vector",
    },
    {
        "name": "token_travel_distance",
        "source": f"{AUDIT_INPUT_PATHS[3]}:alternative_functional_hunt",
        "meaning": "two unit rail hops per completed landed tick",
    },
    {
        "name": "rail_hop_distance_A_to_B",
        "source": f"{AUDIT_INPUT_PATHS[3]}:fixture,alternative_functional_hunt",
        "meaning": "local L1 lift hop distance",
    },
    {
        "name": "rail_hop_distance_B_to_next_A",
        "source": f"{AUDIT_INPUT_PATHS[3]}:fixture,alternative_functional_hunt",
        "meaning": "local L1 land-to-successor hop distance",
    },
)
PROFILE_NAMES = tuple(row["name"] for row in PROFILE_COMPONENTS)


def contender_profile(
    fixed: dict[str, object],
    start: int,
    step: int,
    station: int,
) -> tuple[object, ...]:
    initial_occupied = int(
        station in (start, (start + 1) % RING_STATIONS)
    )
    kind, index, _local = fixed["program"][station]
    semantic_word = fixed["semantic_words"][station]
    physical_word = fixed["physical_words"][station]
    rail_hops = fixed["rail_hops"][station]
    values: tuple[object, ...] = (
        kind,
        index,
        initial_occupied,
        1,
        int(initial_occupied and kind == "relay"),
        int(initial_occupied and kind == "handoff"),
        int(kind == "relay"),
        int(kind == "handoff"),
        len(semantic_word),
        fixed["semantic_vectors"][station],
        len(physical_word),
        fixed["physical_vectors"][station],
        2 * step,
        rail_hops[0],
        rail_hops[1],
    )
    if len(values) != len(PROFILE_COMPONENTS):
        raise AssertionError(("profile width", len(values)))
    return values


def named_profile(profile: tuple[object, ...]) -> dict[str, object]:
    return dict(zip(PROFILE_NAMES, profile))

