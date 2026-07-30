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


def enumerate_success_assignments(
    fixed: dict[str, object],
) -> dict[str, object]:
    """Enumerate every binary pair order at every boundary of every start."""

    semantic_words: tuple[Word, ...] = fixed["semantic_words"]

    @lru_cache(maxsize=None)
    def apply_macro(station: int, state: int) -> int:
        return apply_word_int(state, semantic_words[station])

    def apply_pair(state: int, first: int, second: int) -> int:
        return apply_macro(second, apply_macro(first, state))

    fixtures = []
    success_start_mask_by_absolute_orientation = [0] * COMPLETE_ASSIGNMENTS
    for start in range(RING_STATIONS):
        frontier: dict[int, list[int]] = {fixed["initial"]: [0]}
        frontier_widths = []
        for step in range(RING_STATIONS):
            left = (start + step) % RING_STATIONS
            right = (left + 1) % RING_STATIONS
            next_frontier: dict[int, list[int]] = defaultdict(list)
            for state, masks in frontier.items():
                forward = apply_pair(state, left, right)
                reverse = apply_pair(state, right, left)
                next_frontier[forward].extend(masks)
                decision_bit = 1 << step
                next_frontier[reverse].extend(
                    mask | decision_bit for mask in masks
                )
            frontier = dict(next_frontier)
            frontier_widths.append(len(frontier))

        enumerated_masks = tuple(
            sorted(mask for masks in frontier.values() for mask in masks)
        )
        if enumerated_masks != tuple(range(COMPLETE_ASSIGNMENTS)):
            raise AssertionError(
                ("complete assignment coverage", start, len(enumerated_masks))
            )
        successful_masks = tuple(
            sorted(frontier.get(fixed["expected"], ()))
        )
        for local_mask in successful_masks:
            absolute_mask = 0
            for step in range(RING_STATIONS):
                edge = (start + step) % RING_STATIONS
                decision = (local_mask >> step) & 1
                absolute_mask |= decision << edge
            success_start_mask_by_absolute_orientation[
                absolute_mask
            ] |= 1 << start

        boundary_rows = []
        for step in range(RING_STATIONS):
            left = (start + step) % RING_STATIONS
            right = (left + 1) % RING_STATIONS
            decisions = tuple(
                sorted({(mask >> step) & 1 for mask in successful_masks})
            )
            if not successful_masks:
                status = "UNRESOLVED"
                forced_decision = None
                unresolved_reason = (
                    "empty successful complete-assignment set; exact "
                    "enumeration, not a sampling or runtime bound"
                )
            elif len(decisions) == 1:
                status = "FORCED"
                forced_decision = decisions[0]
                unresolved_reason = None
            else:
                status = "FLEXIBLE"
                forced_decision = None
                unresolved_reason = None
            first = (
                None
                if forced_decision is None
                else (left if forced_decision == 0 else right)
            )
            second = (
                None
                if forced_decision is None
                else (right if forced_decision == 0 else left)
            )
            boundary_rows.append(
                {
                    "start": start,
                    "step": step,
                    "contenders": (left, right),
                    "successful_decisions": decisions,
                    "status": status,
                    "forced_decision": forced_decision,
                    "forced_order": (
                        None
                        if forced_decision is None
                        else {
                            "first": first,
                            "second": second,
                            "verbatim": f"station {first} before station {second}",
                        }
                    ),
                    "unresolved_reason": unresolved_reason,
                    "profiles": (
                        contender_profile(fixed, start, step, left),
                        contender_profile(fixed, start, step, right),
                    ),
                }
            )

        fixtures.append(
            {
                "start": start,
                "assignments_enumerated": COMPLETE_ASSIGNMENTS,
                "successful_assignment_count": len(successful_masks),
                "successful_assignment_masks_decimal": successful_masks,
                "successful_assignment_signatures_step_0_to_10": tuple(
                    "".join(
                        str((mask >> step) & 1)
                        for step in range(RING_STATIONS)
                    )
                    for mask in successful_masks
                ),
                "final_distinct_outputs": len(frontier),
                "frontier_widths_after_each_boundary":
                    tuple(frontier_widths),
                "boundaries": tuple(boundary_rows),
            }
        )

    histogram = Counter(
        success_start_mask_by_absolute_orientation[mask].bit_count()
        for mask in range(1, COMPLETE_ASSIGNMENTS - 1)
    )
    local_success_counts = tuple(
        fixture["successful_assignment_count"] for fixture in fixtures
    )
    return {
        "assignment_encoding": (
            "11-bit local mask; bit step=0 means left=(start+step) first, "
            "bit step=1 means right=(start+step+1) first"
        ),
        "enumeration_scope": (
            "all 2^11 complete boundary-order assignments for each of "
            "all 11 adjacent starts; no sampling"
        ),
        "assignments_per_fixture": COMPLETE_ASSIGNMENTS,
        "total_assignments_enumerated":
            RING_STATIONS * COMPLETE_ASSIGNMENTS,
        "fixtures": tuple(fixtures),
        "fixed_total_order_crosscheck": {
            "absolute_edge_orientation_classes": COMPLETE_ASSIGNMENTS,
            "realizable_fixed_total_order_classes":
                COMPLETE_ASSIGNMENTS - 2,
            "excluded_directed_cycles": (0, COMPLETE_ASSIGNMENTS - 1),
            "pass_count_histogram":
                dict(sorted(histogram.items())),
            "position_uniform_fixed_orders": sum(
                success_start_mask_by_absolute_orientation[mask]
                == COMPLETE_ASSIGNMENTS - 1
                for mask in range(1, COMPLETE_ASSIGNMENTS - 1)
            ),
            "best_fixed_order_passes": max(histogram),
        },
        "local_success_counts_by_start": local_success_counts,
        "macro_cache": {
            "hits": apply_macro.cache_info().hits,
            "misses": apply_macro.cache_info().misses,
            "entries": apply_macro.cache_info().currsize,
        },
    }


def public_forced_extraction(
    census: dict[str, object],
) -> dict[str, object]:
    fixture_rows = []
    status_totals = Counter()
    for fixture in census["fixtures"]:
        boundary_rows = []
        fixture_status = Counter()
        for boundary in fixture["boundaries"]:
            status = boundary["status"]
            fixture_status[status] += 1
            status_totals[status] += 1
            boundary_rows.append(
                {
                    key: boundary[key]
                    for key in (
                        "step",
                        "contenders",
                        "successful_decisions",
                        "status",
                        "forced_order",
                        "unresolved_reason",
                    )
                }
            )
        fixture_rows.append(
            {
                "start": fixture["start"],
                "contested": RING_STATIONS,
                "forced": fixture_status["FORCED"],
                "flexible": fixture_status["FLEXIBLE"],
                "unresolved": fixture_status["UNRESOLVED"],
                "assignments_enumerated":
                    fixture["assignments_enumerated"],
                "successful_assignment_count":
                    fixture["successful_assignment_count"],
                "successful_assignment_masks_decimal":
                    fixture["successful_assignment_masks_decimal"],
                "successful_assignment_signatures_step_0_to_10":
                    fixture[
                        "successful_assignment_signatures_step_0_to_10"
                    ],
                "final_distinct_outputs":
                    fixture["final_distinct_outputs"],
                "boundary_extraction": tuple(boundary_rows),
            }
        )
    return {
        "success_criterion": (
            "Cycle-752 exact frozen two-allocator output after the full "
            "11-boundary adjacent orbit"
        ),
        "assignment_encoding": census["assignment_encoding"],
        "enumeration_bound": {
            "kind": "EXACT_COMPLETE",
            "per_fixture": COMPLETE_ASSIGNMENTS,
            "fixtures": RING_STATIONS,
            "total": RING_STATIONS * COMPLETE_ASSIGNMENTS,
            "sampled": 0,
        },
        "empty_success_policy": (
            "boundaries of an empty successful-assignment set are "
            "UNRESOLVED, never vacuously FORCED and never silently FLEXIBLE"
        ),
        "totals": {
            "contested": RING_STATIONS ** 2,
            "forced": status_totals["FORCED"],
            "flexible": status_totals["FLEXIBLE"],
            "unresolved": status_totals["UNRESOLVED"],
        },
        "local_success_counts_by_start":
            census["local_success_counts_by_start"],
        "fixed_total_order_crosscheck":
            census["fixed_total_order_crosscheck"],
        "fixtures": tuple(fixture_rows),
    }


def forced_record(boundary: dict[str, object]) -> dict[str, object]:
    left, right = boundary["contenders"]
    left_profile, right_profile = boundary["profiles"]
    decision = boundary["forced_decision"]
    if decision not in (0, 1):
        raise AssertionError(("not forced", boundary))
    first = left if decision == 0 else right
    second = right if decision == 0 else left
    if left_profile == right_profile:
        return {
            "boundary": {
                "start": boundary["start"],
                "step": boundary["step"],
                "contenders": boundary["contenders"],
            },
            "symmetric_profile": named_profile(left_profile),
            "forced_order": {
                "first": first,
                "second": second,
                "verbatim": f"station {first} before station {second}",
            },
            "symmetric_impossibility": True,
        }
    lower_profile, higher_profile = sorted((left_profile, right_profile))
    lower_station = left if left_profile == lower_profile else right
    higher_station = right if left_profile == lower_profile else left
    lower_first = first == lower_station
    return {
        "boundary": {
            "start": boundary["start"],
            "step": boundary["step"],
            "contenders": boundary["contenders"],
        },
        "profile_lower": named_profile(lower_profile),
        "profile_higher": named_profile(higher_profile),
        "profile_lower_station": lower_station,
        "profile_higher_station": higher_station,
        "forced_order": {
            "first": first,
            "second": second,
            "verbatim": f"station {first} before station {second}",
            "profile_lower_position":
                "FIRST" if lower_first else "SECOND",
        },
        "lower_first": lower_first,
        "symmetric_impossibility": False,
    }


def collision_census(
    census: dict[str, object],
) -> dict[str, object]:
    records = tuple(
        forced_record(boundary)
        for fixture in census["fixtures"]
        for boundary in fixture["boundaries"]
        if boundary["status"] == "FORCED"
    )
    symmetric = tuple(
        record for record in records if record["symmetric_impossibility"]
    )
    groups: dict[
        tuple[tuple[object, ...], tuple[object, ...]],
        list[dict[str, object]],
    ] = defaultdict(list)
    for fixture in census["fixtures"]:
        for boundary in fixture["boundaries"]:
            if boundary["status"] != "FORCED":
                continue
            left_profile, right_profile = boundary["profiles"]
            if left_profile == right_profile:
                continue
            key = tuple(sorted((left_profile, right_profile)))
            groups[key].append(forced_record(boundary))

    witnesses = []
    collision_groups = 0
    for key in sorted(groups):
        lower_first = [
            record for record in groups[key] if record["lower_first"]
        ]
        lower_second = [
            record for record in groups[key] if not record["lower_first"]
        ]
        if lower_first and lower_second:
            collision_groups += 1
            for first_record in lower_first:
                for second_record in lower_second:
                    witnesses.append(
                        {
                            "profile_pair_verbatim": {
                                "profile_lower":
                                    first_record["profile_lower"],
                                "profile_higher":
                                    first_record["profile_higher"],
                            },
                            "boundary_requiring_profile_lower_FIRST":
                                first_record,
                            "boundary_requiring_profile_lower_SECOND":
                                second_record,
                        }
                    )
    collision_found = bool(symmetric or witnesses)
    return {
        "grouping_rule": (
            "unordered pair {profile(A),profile(B)} over every FORCED "
            "boundary; order is expressed as profile-lower FIRST/SECOND"
        ),
        "forced_boundaries": len(records),
        "unordered_profile_pair_groups": len(groups),
        "opposite_order_collision_groups": collision_groups,
        "symmetric_profile_forced_witnesses": symmetric,
        "opposite_order_witness_pairs_verbatim": tuple(witnesses),
        "collision_found": collision_found,
        "collision_verdict":
            "COLLISION_FOUND" if collision_found else "NO_COLLISION",
        "all_forced_records_verbatim": records,
    }


def construct_lookup_and_run(
    fixed: dict[str, object],
    census: dict[str, object],
    collisions: dict[str, object],
) -> dict[str, object]:
    if collisions["collision_found"]:
        return {
            "constructed": False,
            "reason": "collision or symmetric-profile impossibility",
            "lookup_table": (),
            "fixture_runs": (),
        }

    pair_boundaries: dict[
        tuple[tuple[object, ...], tuple[object, ...]],
        list[dict[str, object]],
    ] = defaultdict(list)
    for fixture in census["fixtures"]:
        for boundary in fixture["boundaries"]:
            pair_boundaries[
                tuple(sorted(boundary["profiles"]))
            ].append(boundary)

    lookup: dict[
        tuple[tuple[object, ...], tuple[object, ...]],
        bool | None,
    ] = {}
    lookup_rows = []
    for key in sorted(pair_boundaries):
        rows = pair_boundaries[key]
        forced_rows = [
            boundary for boundary in rows
            if boundary["status"] == "FORCED"
        ]
        if key[0] == key[1]:
            decision: bool | None = None
            basis = (
                "SYMMETRIC_FLEXIBLE_OR_UNRESOLVED_TIE"
                if not forced_rows
                else "IMPOSSIBLE_FORCED_SYMMETRY"
            )
        elif forced_rows:
            directions = {
                forced_record(boundary)["lower_first"]
                for boundary in forced_rows
            }
            if len(directions) != 1:
                raise AssertionError(("collision escaped census", key))
            decision = directions.pop()
            basis = "FORCED_UNANIMITY"
        else:
            decision = True
            statuses = {boundary["status"] for boundary in rows}
            basis = (
                "FLEXIBLE_PROFILE_LOWER_DEFAULT"
                if statuses == {"FLEXIBLE"}
                else "UNRESOLVED_PROFILE_LOWER_DEFAULT"
            )
        lookup[key] = decision
        lookup_rows.append(
            {
                "profile_lower": named_profile(key[0]),
                "profile_higher": named_profile(key[1]),
                "order": (
                    "TIE"
                    if decision is None
                    else (
                        "PROFILE_LOWER_FIRST"
                        if decision
                        else "PROFILE_HIGHER_FIRST"
                    )
                ),
                "basis": basis,
                "boundary_occurrences": len(rows),
            }
        )

    semantic_words: tuple[Word, ...] = fixed["semantic_words"]

    @lru_cache(maxsize=None)
    def apply_macro(station: int, state: int) -> int:
        return apply_word_int(state, semantic_words[station])

    fixture_runs = []
    for fixture in census["fixtures"]:
        start = fixture["start"]
        state = fixed["initial"]
        chosen_mask = 0
        tied_boundaries = []
        forced_constraints_satisfied = True
        flexible_choices = []
        unresolved_choices = []
        for boundary in fixture["boundaries"]:
            step = boundary["step"]
            left, right = boundary["contenders"]
            left_profile, right_profile = boundary["profiles"]
            key = tuple(sorted((left_profile, right_profile)))
            lower_first = lookup[key]
            if lower_first is None:
                decision = 0
                tied_boundaries.append(step)
            else:
                left_is_lower = left_profile == key[0]
                decision = (
                    0 if lower_first == left_is_lower else 1
                )
            if decision:
                chosen_mask |= 1 << step
            first, second = (
                (left, right) if decision == 0 else (right, left)
            )
            state = apply_macro(second, apply_macro(first, state))
            if boundary["status"] == "FORCED":
                forced_constraints_satisfied &= (
                    decision == boundary["forced_decision"]
                )
            elif boundary["status"] == "FLEXIBLE":
                flexible_choices.append(
                    {
                        "step": step,
                        "decision": decision,
                        "order": (first, second),
                    }
                )
            else:
                unresolved_choices.append(
                    {
                        "step": step,
                        "decision": decision,
                        "order": (first, second),
                    }
                )
        fixture_runs.append(
            {
                "start": start,
                "chosen_assignment_mask_decimal": chosen_mask,
                "chosen_assignment_signature_step_0_to_10": "".join(
                    str((chosen_mask >> step) & 1)
                    for step in range(RING_STATIONS)
                ),
                "successful_assignment_set_nonempty":
                    bool(fixture["successful_assignment_count"]),
                "chosen_assignment_in_success_set":
                    chosen_mask
                    in fixture["successful_assignment_masks_decimal"],
                "forced_constraints_satisfied":
                    forced_constraints_satisfied,
                "flexible_choices": tuple(flexible_choices),
                "unresolved_default_choices":
                    tuple(unresolved_choices),
                "symmetric_profile_ties": tuple(tied_boundaries),
                "allocator_correct": state == fixed["expected"],
                "output_sha256":
                    int_bit_digest(state, fixed["data_width"]),
            }
        )
    return {
        "constructed": True,
        "lookup_semantics": (
            "unordered profile-pair lookup; forced rows use unanimous "
            "direction, flexible/unresolved rows default profile-lower first"
        ),
        "lookup_table": tuple(lookup_rows),
        "lookup_table_rows": len(lookup_rows),
        "fixture_runs": tuple(fixture_runs),
        "forced_constraint_fixture_score": sum(
            row["forced_constraints_satisfied"] for row in fixture_runs
        ),
        "allocator_correct_fixture_score": sum(
            row["allocator_correct"] for row in fixture_runs
        ),
        "symmetric_tie_count": sum(
            len(row["symmetric_profile_ties"]) for row in fixture_runs
        ),
    }


def decision_certificate(
    census: dict[str, object],
    collisions: dict[str, object],
    lookup: dict[str, object],
) -> dict[str, object]:
    empty_starts = tuple(
        fixture["start"]
        for fixture in census["fixtures"]
        if fixture["successful_assignment_count"] == 0
    )
    if collisions["collision_found"]:
        verdict = "FUNCTION_CLASS_KILLED_COLLISION_FOUND"
        proof = (
            "identical unordered landed-local profile pair requires opposite "
            "forced orders (or a symmetric profile requires asymmetry)"
        )
        order_source_exists = False
    elif empty_starts:
        verdict = "FUNCTION_CLASS_KILLED_EMPTY_SUCCESS_SETS"
        proof = (
            "exact complete assignment enumeration is empty on starts "
            f"{empty_starts}; therefore even an omniscient fixture-aware "
            "order supplier cannot make those fixtures allocator-correct"
        )
        order_source_exists = False
    else:
        verdict = "NO_COLLISION_LOOKUP_CONSTRUCTED_SEARCH_REOPENS"
        proof = (
            "forced directions define a single-valued unordered-profile-pair "
            "lookup; flexible behavior is reported by the constructive run"
        )
        order_source_exists = True
    return {
        "collision_verdict": collisions["collision_verdict"],
        "decision_verdict": verdict,
        "empty_success_fixture_starts": empty_starts,
        "order_source_exists": order_source_exists,
        "proof": proof,
        "scope": (
            "all deterministic functions of the declared landed-local "
            "profile; the empty-set branch is stronger and also excludes "
            "nonlocal, fixture-aware complete boundary-order assignments"
        ),
        "subsumes": (
            "2,046 fixed-total-order behavior classes",
            "all 18 Cycle-783 functional candidates",
            "every other landed-local profile function",
        ),
        "lookup_constructed_for_no_collision_control":
            lookup["constructed"],
        "lookup_forced_constraint_fixture_score":
            lookup.get("forced_constraint_fixture_score", 0),
        "lookup_allocator_correct_fixture_score":
            lookup.get("allocator_correct_fixture_score", 0),
        "no_collision_branch_precondition_satisfied": not empty_starts,
        "no_collision_branch_precondition_note": (
            "NO_COLLISION alone implies a constructive reopening only when "
            "every fixture has at least one successful complete assignment"
        ),
    }


def deterministic_projection(
    profile_certificate: dict[str, object],
    forced: dict[str, object],
    collisions: dict[str, object],
    lookup: dict[str, object],
    decision: dict[str, object],
) -> dict[str, object]:
    return {
        "profile": profile_certificate,
        "forced": forced,
        "collisions": collisions,
        "lookup": lookup,
        "decision": decision,
    }


def projection_sha256(value: object) -> str:
    return sha256(compact_json(value).encode("utf-8")).hexdigest()


def main() -> int:
    started = perf_counter()
    source = source_and_blocklist_certificate()
    for path in AUDIT_INPUT_PATHS:
        OUTPUT_LINES.append(
            f"SHA256 {path} {source['observed_sha256'][path]}"
        )

    fixed = build_fixture()
    profile_certificate = {
        "profile_component_count": len(PROFILE_COMPONENTS),
        "components_in_tuple_order": PROFILE_COMPONENTS,
        "contested_item": (
            "occupied A_s selecting the station-local mapped Q macro, as "
            f"identified by {AUDIT_INPUT_PATHS[3]}:event_surface"
        ),
        "locality_rule": (
            "The profile is what the contested Q boundary physically looks "
            "like in the landed 752/783 value universe: NO global position "
            "index, NO fixture identity, NO boundary coordinates. Program "
            "kind/charge-row index, occupancies, gate-count vectors, and "
            "distances are local values; station/start/step labels identify "
            "certificate records only and are not profile components."
        ),
        "excluded": (
            "global station index",
            "fixture/start identity",
            "boundary/step coordinates",
            "absolute track coordinates",
            "hidden station-index tie completion",
        ),
        "exact_fixture": {
            "stations": len(fixed["program"]),
            "data_width": fixed["data_width"],
            "expected_two_source_sha256": fixed["expected_sha256"],
            "program_kind_charge_rows": tuple(
                (row[0], row[1]) for row in fixed["program"]
            ),
            "semantic_gate_vectors_X_CNOT_TOF":
                fixed["semantic_vectors"],
            "physical_gate_vectors_CNOT_TOF":
                fixed["physical_vectors"],
            "physical_gate_counts": fixed["physical_counts"],
            "rail_hops": fixed["rail_hops"],
        },
    }

    first_census = enumerate_success_assignments(fixed)
    first_forced = public_forced_extraction(first_census)
    first_collisions = collision_census(first_census)
    first_lookup = construct_lookup_and_run(
        fixed, first_census, first_collisions
    )
    first_decision = decision_certificate(
        first_census, first_collisions, first_lookup
    )
    first_projection = deterministic_projection(
        profile_certificate,
        first_forced,
        first_collisions,
        first_lookup,
        first_decision,
    )

    second_census = enumerate_success_assignments(fixed)
    second_forced = public_forced_extraction(second_census)
    second_collisions = collision_census(second_census)
    second_lookup = construct_lookup_and_run(
        fixed, second_census, second_collisions
    )
    second_decision = decision_certificate(
        second_census, second_collisions, second_lookup
    )
    second_projection = deterministic_projection(
        profile_certificate,
        second_forced,
        second_collisions,
        second_lookup,
        second_decision,
    )
    first_hash = projection_sha256(first_projection)
    second_hash = projection_sha256(second_projection)

    emit("CERTIFICATE_A_PROFILE_DEFINITION", profile_certificate)
    check(
        "CERTIFICATE_A_PROFILE_COMPLETE_AND_LOCAL",
        len(PROFILE_COMPONENTS) == len(set(PROFILE_NAMES))
        and fixed["expected_sha256"] == EXPECTED_TWO_SOURCE_SHA256
        and len(fixed["program"]) == RING_STATIONS,
        {
            "component_count": len(PROFILE_COMPONENTS),
            "unique_component_count": len(set(PROFILE_NAMES)),
            "expected_sha256": fixed["expected_sha256"],
        },
    )

    emit("CERTIFICATE_B_FORCED_ORDER_EXTRACTION", first_forced)
    totals = first_forced["totals"]
    fixed_crosscheck = first_forced["fixed_total_order_crosscheck"]
    check(
        "CERTIFICATE_B_EXACT_COMPLETE_ASSIGNMENT_CENSUS",
        first_forced["enumeration_bound"]["kind"] == "EXACT_COMPLETE"
        and first_forced["enumeration_bound"]["total"]
        == RING_STATIONS * COMPLETE_ASSIGNMENTS
        and tuple(first_forced["local_success_counts_by_start"])
        == (512,) + (0,) * 10
        and fixed_crosscheck["pass_count_histogram"]
        == EXPECTED_FIXED_CLASS_HISTOGRAM
        and fixed_crosscheck["best_fixed_order_passes"] == 1
        and fixed_crosscheck["position_uniform_fixed_orders"] == 0
        and totals
        == {
            "contested": 121,
            "forced": 2,
            "flexible": 9,
            "unresolved": 110,
        },
        {
            "local_success_counts":
                first_forced["local_success_counts_by_start"],
            "totals": totals,
            "fixed_total_order_crosscheck": fixed_crosscheck,
        },
    )

    if first_collisions["symmetric_profile_forced_witnesses"]:
        emit(
            "SYMMETRIC_PROFILE_IMPOSSIBILITY_WITNESSES_LOUD",
            first_collisions["symmetric_profile_forced_witnesses"],
        )
    if first_collisions["opposite_order_witness_pairs_verbatim"]:
        emit(
            "COLLISION_WITNESS_PAIRS_VERBATIM",
            first_collisions[
                "opposite_order_witness_pairs_verbatim"
            ],
        )
    emit("CERTIFICATE_C_COLLISION_CENSUS", first_collisions)
    check(
        "CERTIFICATE_C_ALL_FORCED_BOUNDARIES_GROUPED",
        first_collisions["forced_boundaries"] == totals["forced"]
        and (
            first_collisions["collision_found"]
            == bool(
                first_collisions[
                    "symmetric_profile_forced_witnesses"
                ]
                or first_collisions[
                    "opposite_order_witness_pairs_verbatim"
                ]
            )
        ),
        {
            "forced": first_collisions["forced_boundaries"],
            "groups":
                first_collisions["unordered_profile_pair_groups"],
            "collision_verdict":
                first_collisions["collision_verdict"],
        },
    )

    emit("CERTIFICATE_D_PROFILE_ORDER_LOOKUP_TABLE", first_lookup)
    emit("CERTIFICATE_D_VERDICT", first_decision)
    check(
        "CERTIFICATE_D_WHOLE_FUNCTION_CLASS_DECIDED",
        first_decision["decision_verdict"]
        == "FUNCTION_CLASS_KILLED_EMPTY_SUCCESS_SETS"
        and first_decision["empty_success_fixture_starts"]
        == tuple(range(1, RING_STATIONS))
        and not first_decision["order_source_exists"]
        and first_lookup["forced_constraint_fixture_score"]
        == RING_STATIONS
        and first_lookup["allocator_correct_fixture_score"] == 1,
        {
            "collision_verdict":
                first_decision["collision_verdict"],
            "decision_verdict":
                first_decision["decision_verdict"],
            "empty_success_fixture_starts":
                first_decision["empty_success_fixture_starts"],
            "forced_constraint_fixture_score":
                first_lookup["forced_constraint_fixture_score"],
            "allocator_correct_fixture_score":
                first_lookup["allocator_correct_fixture_score"],
        },
    )

    runtime_seconds = perf_counter() - started
    controls = {
        "audit_input_paths_literal": source["audit_input_paths_literal"],
        "all_audit_input_paths_relative": source["all_paths_relative"],
        "all_audit_input_paths_exist": source["all_paths_exist"],
        "observed_sha256": source["observed_sha256"],
        "expected_sha256": source["expected_sha256"],
        "sha256_match": source["sha256_match"],
        "text_ast_only_function_anchors":
            source["text_ast_only_function_anchors"],
        "all_function_anchors_present":
            source["all_function_anchors_present"],
        "import_blocklist": source["import_blocklist"],
        "blocked_modules_loaded": tuple(
            module
            for module in IMPORT_BLOCKLIST
            if module in sys.modules
        ),
        "blocklist_active": source["blocklist_active"],
        "support_observed_sha256":
            source["support_observed_sha256"],
        "support_sha256_match": source["support_sha256_match"],
        "third_party_packages": source["third_party_packages"],
        "exact_arithmetic": source["simulation_arithmetic"],
        "determinism_run_1_sha256": first_hash,
        "determinism_run_2_sha256": second_hash,
        "determinism_match": first_hash == second_hash,
        "runtime_seconds": runtime_seconds,
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "runtime_within_limit":
            runtime_seconds < RUNTIME_LIMIT_SECONDS,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_within_limit": True,
    }
    controls_ok = (
        source["all_paths_relative"]
        and source["all_paths_exist"]
        and source["sha256_match"]
        and source["all_function_anchors_present"]
        and source["support_sha256_match"]
        and not controls["blocked_modules_loaded"]
        and source["blocklist_active"]
        and first_hash == second_hash
        and runtime_seconds < RUNTIME_LIMIT_SECONDS
        and all(CHECKS.values())
    )
    control_line_index = len(OUTPUT_LINES)
    emit("CERTIFICATE_E_CONTROLS", controls)
    check(
        "CERTIFICATE_E_SHAS_BLOCKLIST_DETERMINISM_AND_BOUNDS",
        controls_ok,
        {
            "determinism_sha256": first_hash,
            "runtime_seconds": runtime_seconds,
            "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )
    for _iteration in range(8):
        rendered = "\n".join(OUTPUT_LINES) + "\n"
        stdout_bytes = len(rendered.encode("utf-8"))
        controls["stdout_bytes"] = stdout_bytes
        controls["stdout_within_limit"] = (
            stdout_bytes < STDOUT_LIMIT_BYTES
        )
        replacement = (
            "CERTIFICATE_E_CONTROLS=" + compact_json(controls)
        )
        if OUTPUT_LINES[control_line_index] == replacement:
            break
        OUTPUT_LINES[control_line_index] = replacement
    rendered = "\n".join(OUTPUT_LINES) + "\n"
    final_stdout_bytes = len(rendered.encode("utf-8"))
    if final_stdout_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", final_stdout_bytes, STDOUT_LIMIT_BYTES)
        )
    if not all(CHECKS.values()):
        print(rendered, end="")
        return 1
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
