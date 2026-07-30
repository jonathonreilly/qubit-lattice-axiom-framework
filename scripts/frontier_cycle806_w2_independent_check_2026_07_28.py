#!/usr/bin/env python3
"""Cycle 806 independent adversarial check of the W2 unsatisfiability claim.

The copied Cycle-752 runner and Cycle-806 primary are text/AST inputs only.
This checker independently encodes exact basis-state gate action and directly
visits every one of the 2^11 local boundary-order assignments at every one of
the 11 adjacent starts.
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


# Literal, existing, worktree-relative disk inputs.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py",
    "scripts/frontier_cycle806_w2_indistinguishability_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
EXPECTED_SHA256 = {
    "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py":
        "fb50873dd30a0d580bfd03a19cc4613dd9517816e1e9aab7adba6bd77ed2c2a1",
    "scripts/frontier_cycle806_w2_indistinguishability_2026_07_28.py":
        "d9a8cb70f3c0a99c112b7ca3e962941f7524dc743c56979ef9d4f6b06fa58c5c",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py":
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
COPIED_TEXT_ONLY_MODULES = (
    "frontier_cycle752_lawful_adjacency_attempt_2026_07_28",
    "frontier_cycle806_w2_indistinguishability_2026_07_28",
)
RING_STATIONS = 11
FIXTURE_BANKS = 2
ASSIGNMENTS_PER_START = 1 << RING_STATIONS
REALIZABLE_FIXED_ORDER_CLASSES = ASSIGNMENTS_PER_START - 2
EXPECTED_TWO_SOURCE_SHA256 = (
    "3513b562570c8ee4723fad82900dea66e6df5933fe40ac5e06a85bc513fea213"
)
RUNTIME_LIMIT_SECONDS = 1200.0
STDOUT_LIMIT_BYTES = 150 * 1024
ROOT = Path(__file__).resolve().parents[1]


class _CopiedInputBlocker(importlib.abc.MetaPathFinder):
    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        del path, target
        if fullname in COPIED_TEXT_ONLY_MODULES:
            raise ImportError(f"{fullname} is text/AST-only in this checker")
        return None


_IMPORT_BLOCKER = _CopiedInputBlocker()
sys.meta_path.insert(0, _IMPORT_BLOCKER)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Word = tuple[tuple[str, tuple[int, ...]], ...]
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


def apply_word_own(state: int, word: Word) -> int:
    """Exact, independently written X/CNOT/TOF basis-state encoder."""

    for kind, wires in word:
        if kind == "X":
            state ^= 1 << wires[0]
        elif kind == "CNOT":
            state ^= ((state >> wires[0]) & 1) << wires[1]
        elif kind == "TOF":
            controls = ((state >> wires[0]) & 1) & (
                (state >> wires[1]) & 1
            )
            state ^= controls << wires[2]
        else:
            raise AssertionError(("unsupported gate", kind, wires))
    return state


def assignment_node(tree: ast.Module, name: str) -> ast.expr:
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
        raise AssertionError(("assignment count", name, len(matches)))
    return matches[0]


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function count", name, len(matches)))
    return matches[0]


def static_eval(node: ast.AST) -> object:
    """Evaluate only inert literal tuple/list/dict and +/* expressions."""

    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Tuple):
        return tuple(static_eval(row) for row in node.elts)
    if isinstance(node, ast.List):
        return [static_eval(row) for row in node.elts]
    if isinstance(node, ast.Dict):
        return {
            static_eval(key): static_eval(value)
            for key, value in zip(node.keys, node.values)
        }
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return static_eval(node.left) + static_eval(node.right)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
        return static_eval(node.left) * static_eval(node.right)
    raise AssertionError(("non-static expression", ast.dump(node)))


def named_return_value(function: ast.FunctionDef, key_name: str) -> ast.AST:
    returns = [
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    for returned in returns:
        assert isinstance(returned, ast.Dict)
        for key, value in zip(returned.keys, returned.values):
            if isinstance(key, ast.Constant) and key.value == key_name:
                return value
    raise AssertionError(("return key absent", function.name, key_name))


def exact_call_assignment(
    function: ast.FunctionDef,
    target_name: str,
    function_name: str,
    argument_names: tuple[str, ...],
) -> bool:
    for node in ast.walk(function):
        target: ast.expr | None = None
        value: ast.expr | None = None
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target, value = node.targets[0], node.value
        elif isinstance(node, ast.AnnAssign):
            target, value = node.target, node.value
        if (
            isinstance(target, ast.Name)
            and target.id == target_name
            and isinstance(value, ast.Call)
            and isinstance(value.func, ast.Name)
            and value.func.id == function_name
            and tuple(
                arg.id for arg in value.args if isinstance(arg, ast.Name)
            )
            == argument_names
            and len(value.args) == len(argument_names)
        ):
            return True
    return False


def has_name_equality(
    function: ast.FunctionDef,
    left_name: str,
    right_name: str,
) -> bool:
    return any(
        isinstance(node, ast.Compare)
        and len(node.ops) == 1
        and isinstance(node.ops[0], ast.Eq)
        and isinstance(node.left, ast.Name)
        and node.left.id == left_name
        and len(node.comparators) == 1
        and isinstance(node.comparators[0], ast.Name)
        and node.comparators[0].id == right_name
        for node in ast.walk(function)
    )


def extract_primary_expected_counts(primary_main: ast.FunctionDef) -> tuple[int, ...]:
    matches: list[tuple[int, ...]] = []
    for node in ast.walk(primary_main):
        if not isinstance(node, ast.Compare) or len(node.comparators) != 1:
            continue
        if "local_success_counts_by_start" not in ast.unparse(node.left):
            continue
        value = static_eval(node.comparators[0])
        if isinstance(value, tuple) and all(
            isinstance(row, int) for row in value
        ):
            matches.append(value)
    if len(matches) != 1:
        raise AssertionError(("primary expected count matches", matches))
    return matches[0]


def extract_primary_expected_totals(primary_main: ast.FunctionDef) -> dict[str, int]:
    matches: list[dict[str, int]] = []
    for node in ast.walk(primary_main):
        if (
            isinstance(node, ast.Compare)
            and isinstance(node.left, ast.Name)
            and node.left.id == "totals"
            and len(node.comparators) == 1
        ):
            value = static_eval(node.comparators[0])
            if isinstance(value, dict):
                matches.append(value)
    if len(matches) != 1:
        raise AssertionError(("primary expected totals matches", matches))
    return matches[0]


def extract_profile_names(primary_tree: ast.Module) -> tuple[str, ...]:
    value = assignment_node(primary_tree, "PROFILE_COMPONENTS")
    if not isinstance(value, ast.Tuple):
        raise AssertionError("PROFILE_COMPONENTS is not a literal tuple")
    names = []
    for row in value.elts:
        if not isinstance(row, ast.Dict):
            raise AssertionError(("profile row", ast.dump(row)))
        fields = {
            key.value: field
            for key, field in zip(row.keys, row.values)
            if isinstance(key, ast.Constant)
        }
        name = static_eval(fields["name"])
        if not isinstance(name, str):
            raise AssertionError(("profile name", name))
        names.append(name)
    return tuple(names)


def criterion_fidelity(
    copied_tree: ast.Module,
    primary_tree: ast.Module,
) -> dict[str, object]:
    allocator = function_node(copied_tree, "allocator_expected")
    adjacent = function_node(copied_tree, "route3_adjacent_full_battery")
    order_census = function_node(
        copied_tree, "route3_order_dependence_census"
    )
    orbit = function_node(copied_tree, "fixed_word_orbit")
    primary_fixture = function_node(primary_tree, "build_fixture")
    primary_enumeration = function_node(
        primary_tree, "enumerate_success_assignments"
    )

    allocator_text = ast.unparse(allocator)
    orbit_text = ast.unparse(orbit)
    primary_fixture_text = ast.unparse(primary_fixture).replace(" ", "")
    primary_enum_text = ast.unparse(primary_enumeration).replace(" ", "")
    copied_exact = (
        exact_call_assignment(
            adjacent,
            "expected_data",
            "allocator_expected",
            ("data", "EXPECTED_COUNT"),
        )
        and exact_call_assignment(
            order_census,
            "expected_data",
            "allocator_expected",
            ("data", "EXPECTED_COUNT"),
        )
        and has_name_equality(adjacent, "output", "expected_data")
        and has_name_equality(order_census, "output", "expected_data")
        and "for _source in range(source_count)" in allocator_text
        and "output = K.A.apply_semantic(output, allocator)" in allocator_text
        and "for _step in range(RING_STATIONS)" in orbit_text
        and "state = apply_word(state, word)" in orbit_text
    )
    primary_exact = (
        "expected=apply_word_int(apply_word_int(initial,allocator),allocator)"
        in primary_fixture_text
        and "frontier.get(fixed['expected'],())" in primary_enum_text
        and "forstartinrange(RING_STATIONS)" in primary_enum_text
        and "forstepinrange(RING_STATIONS)" in primary_enum_text
    )
    return {
        "pass": copied_exact and primary_exact,
        "copied_criterion": (
            "final extracted data register equals data after exactly two "
            "applications of K.M.global_allocator_word(2)"
        ),
        "primary_criterion": (
            "final independently simulated data state equals the same "
            "twice-applied allocator target"
        ),
        "copied_citations": {
            "allocator_expected":
                f"allocator_expected lines {allocator.lineno}-{allocator.end_lineno}",
            "adjacent_equality":
                f"route3_adjacent_full_battery lines {adjacent.lineno}-{adjacent.end_lineno}",
            "order_census_equality":
                f"route3_order_dependence_census lines {order_census.lineno}-{order_census.end_lineno}",
        },
        "primary_citations": {
            "target": (
                f"build_fixture lines {primary_fixture.lineno}-"
                f"{primary_fixture.end_lineno}"
            ),
            "success_set": (
                f"enumerate_success_assignments lines "
                f"{primary_enumeration.lineno}-{primary_enumeration.end_lineno}"
            ),
        },
        "divergence": "NONE" if copied_exact and primary_exact else (
            "AST criterion mismatch; satisfiability comparison is not valid"
        ),
        "finding_verbatim": (
            "CRITERION FIDELITY: NONE — both tests accept exactly when the "
            "final data equals the frozen two-allocator output."
            if copied_exact and primary_exact
            else
            "CRITERION FIDELITY REFUTATION: the primary does not encode the "
            "copied Cycle-752 final-data equality exactly."
        ),
    }


def l1(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def build_fixture_own() -> dict[str, object]:
    """Construct only from the landed Cycle-719 support API."""

    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    data = tuple(
        K.M.prepare_endpoint(K.M.pack_state(banks, links), (1, 0))
    )
    semantic_words = tuple(
        freeze_word(K.mapped_macro(row)) for row in program
    )
    data_width = len(data)
    initial = bits_to_int(data)
    allocator = freeze_word(K.M.global_allocator_word(FIXTURE_BANKS))
    expected = initial
    for _ in range(2):
        expected = apply_word_own(expected, allocator)

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
    if physical_program != program:
        raise AssertionError("held physical program differs")
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


def enumerate_direct(fixture: dict[str, object]) -> dict[str, object]:
    """Visit masks 0..2047 directly for every start; no frontier algorithm."""

    words: tuple[Word, ...] = fixture["semantic_words"]

    @lru_cache(maxsize=None)
    def apply_macro(station: int, state: int) -> int:
        return apply_word_own(state, words[station])

    success_sets = []
    distinct_output_counts = []
    coverage_digests = []
    for start in range(RING_STATIONS):
        successful = []
        outputs = set()
        visited = []
        for assignment in range(ASSIGNMENTS_PER_START):
            visited.append(assignment)
            state = fixture["initial"]
            for step in range(RING_STATIONS):
                left = (start + step) % RING_STATIONS
                right = (left + 1) % RING_STATIONS
                if (assignment >> step) & 1:
                    first, second = right, left
                else:
                    first, second = left, right
                state = apply_macro(first, state)
                state = apply_macro(second, state)
            outputs.add(state)
            if state == fixture["expected"]:
                successful.append(assignment)
        if visited != list(range(ASSIGNMENTS_PER_START)):
            raise AssertionError(("coverage gap", start))
        success_sets.append(tuple(successful))
        distinct_output_counts.append(len(outputs))
        coverage_digests.append(
            sha256(
                b"".join(
                    value.to_bytes(2, "little") for value in visited
                )
            ).hexdigest()
        )
    projection = {
        "success_sets": tuple(success_sets),
        "distinct_output_counts": tuple(distinct_output_counts),
        "coverage_digests": tuple(coverage_digests),
    }
    return {
        **projection,
        "projection_sha256": sha256(
            compact(projection).encode("utf-8")
        ).hexdigest(),
        "transition_cache": {
            "hits": apply_macro.cache_info().hits,
            "misses": apply_macro.cache_info().misses,
            "entries": apply_macro.cache_info().currsize,
        },
    }


def absolute_orientation_from_order(order: tuple[int, ...]) -> int:
    rank = {station: index for index, station in enumerate(order)}
    if set(rank) != set(range(RING_STATIONS)):
        raise AssertionError(("not a station order", order))
    mask = 0
    for left in range(RING_STATIONS):
        right = (left + 1) % RING_STATIONS
        mask |= int(rank[right] < rank[left]) << left
    return mask


def local_mask(absolute_mask: int, start: int) -> int:
    mask = 0
    for step in range(RING_STATIONS):
        edge = (start + step) % RING_STATIONS
        mask |= ((absolute_mask >> edge) & 1) << step
    return mask


def identity_controls(
    success_sets: tuple[tuple[int, ...], ...],
    witness_order: tuple[int, ...],
) -> dict[str, object]:
    success_lookup = tuple(set(rows) for rows in success_sets)
    class_scores = []
    histogram = Counter()
    uniform = 0
    for absolute_mask in range(1, ASSIGNMENTS_PER_START - 1):
        successful_starts = tuple(
            start
            for start in range(RING_STATIONS)
            if local_mask(absolute_mask, start) in success_lookup[start]
        )
        class_scores.append((absolute_mask, successful_starts))
        histogram[len(successful_starts)] += 1
        uniform += len(successful_starts) == RING_STATIONS

    witness_absolute_mask = absolute_orientation_from_order(witness_order)
    witness_local_masks = tuple(
        local_mask(witness_absolute_mask, start)
        for start in range(RING_STATIONS)
    )
    witness_success_starts = tuple(
        start
        for start in range(RING_STATIONS)
        if witness_local_masks[start] in success_lookup[start]
    )
    best = max(histogram)
    return {
        "pass": (
            len(class_scores) == REALIZABLE_FIXED_ORDER_CLASSES
            and best == 1
            and uniform == 0
            and witness_success_starts == (0,)
            and witness_local_masks[0] in success_lookup[0]
            and histogram == Counter({0: 1535, 1: 511})
        ),
        "realizable_fixed_order_classes": len(class_scores),
        "excluded_directed_cycle_orientations": (
            0,
            ASSIGNMENTS_PER_START - 1,
        ),
        "pass_count_histogram": dict(sorted(histogram.items())),
        "best_fixed_order_successes": best,
        "position_uniform_classes": uniform,
        "cycle756_witness_order": witness_order,
        "witness_absolute_orientation_mask": witness_absolute_mask,
        "witness_local_assignment_masks_by_start": witness_local_masks,
        "witness_success_starts": witness_success_starts,
        "witness_assignment_in_success_set": (
            len(witness_success_starts) == 1
            and witness_local_masks[witness_success_starts[0]]
            in success_lookup[witness_success_starts[0]]
        ),
        "finding_verbatim": (
            "IDENTITY CONTROLS: best fixed-order score 1/11; "
            "position-uniform classes 0/2,046; the Cycle-756 witness "
            "succeeds only at start 0 and its local assignment is present."
        ),
    }


def contender_profile_own(
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
    return (
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


def named_profile(profile: tuple[object, ...]) -> dict[str, object]:
    if len(profile) != len(PROFILE_NAMES):
        raise AssertionError(("profile width", len(profile)))
    return dict(zip(PROFILE_NAMES, profile))


def forced_flexible_recount(
    fixture: dict[str, object],
    success_sets: tuple[tuple[int, ...], ...],
    primary_profile_names: tuple[str, ...],
    primary_expected_totals: dict[str, int],
) -> dict[str, object]:
    satisfiable_starts = tuple(
        start for start, rows in enumerate(success_sets) if rows
    )
    forced_rows = []
    flexible = 0
    if len(satisfiable_starts) == 1:
        start = satisfiable_starts[0]
        successful = success_sets[start]
        for step in range(RING_STATIONS):
            decisions = tuple(
                sorted({(mask >> step) & 1 for mask in successful})
            )
            if len(decisions) == 1:
                left = (start + step) % RING_STATIONS
                right = (left + 1) % RING_STATIONS
                left_profile = contender_profile_own(
                    fixture, start, step, left
                )
                right_profile = contender_profile_own(
                    fixture, start, step, right
                )
                decision = decisions[0]
                first = right if decision else left
                second = left if decision else right
                if left_profile == right_profile:
                    lower_first = None
                    key = (left_profile, right_profile)
                else:
                    key = tuple(sorted((left_profile, right_profile)))
                    lower_station = left if left_profile == key[0] else right
                    lower_first = first == lower_station
                forced_rows.append(
                    {
                        "start": start,
                        "step": step,
                        "contenders": (left, right),
                        "decision": decision,
                        "forced_order_verbatim":
                            f"station {first} before station {second}",
                        "profile_lower": named_profile(key[0]),
                        "profile_higher": named_profile(key[1]),
                        "profile_lower_first": lower_first,
                        "_key": key,
                    }
                )
            elif decisions == (0, 1):
                flexible += 1
            else:
                raise AssertionError(("decision census", start, step, decisions))

    groups: dict[
        tuple[tuple[object, ...], tuple[object, ...]],
        set[bool | None],
    ] = defaultdict(set)
    for row in forced_rows:
        groups[row["_key"]].add(row["profile_lower_first"])
    symmetric = any(key[0] == key[1] for key in groups)
    opposite = any(values == {False, True} for values in groups.values())
    public_rows = tuple(
        {key: value for key, value in row.items() if key != "_key"}
        for row in forced_rows
    )
    expected_forced = primary_expected_totals.get("forced")
    expected_flexible = primary_expected_totals.get("flexible")
    passed = (
        satisfiable_starts == (0,)
        and len(forced_rows) == expected_forced == 2
        and flexible == expected_flexible == 9
        and primary_profile_names == PROFILE_NAMES
        and len(primary_profile_names) == 15
        and not symmetric
        and not opposite
    )
    return {
        "pass": passed,
        "satisfiable_start": satisfiable_starts[0]
        if len(satisfiable_starts) == 1 else None,
        "forced_boundaries": len(forced_rows),
        "flexible_boundaries": flexible,
        "primary_expected_forced": expected_forced,
        "primary_expected_flexible": expected_flexible,
        "profile_component_count": len(PROFILE_NAMES),
        "profile_names_match_primary_ast": primary_profile_names == PROFILE_NAMES,
        "forced_records_verbatim": public_rows,
        "unordered_profile_pair_groups": len(groups),
        "symmetric_profile_forced": symmetric,
        "opposite_order_collision": opposite,
        "collision_verdict": (
            "COLLISION_FOUND" if symmetric or opposite else "NO_COLLISION"
        ),
        "finding_verbatim": (
            "FORCED/FLEXIBLE RECOUNT: start 0 has 2 forced and 9 flexible "
            "boundaries under the primary's 15-component profile; "
            "NO_COLLISION."
            if passed else
            "FORCED/FLEXIBLE RECOUNT REFUTATION: the independent forced "
            "profile census diverges from the primary."
        ),
    }


def scope_honesty(
    primary_tree: ast.Module,
    primary_text: str,
) -> dict[str, object]:
    decision = function_node(primary_tree, "decision_certificate")
    build = function_node(primary_tree, "build_fixture")
    enumeration = function_node(primary_tree, "enumerate_success_assignments")
    scope = static_eval(named_return_value(decision, "scope"))
    subsumes = static_eval(named_return_value(decision, "subsumes"))
    docstring = ast.get_docstring(primary_tree) or ""
    decision_source = ast.get_source_segment(primary_text, decision) or ""
    forbidden = (
        "all fixture families",
        "every fixture family",
        "any fixture family",
        "all possible fixtures",
        "all configuration families",
    )
    forbidden_hits = tuple(
        phrase
        for phrase in forbidden
        if phrase in (docstring + "\n" + decision_source).lower()
    )
    positive_scope = (
        "held adjacent-start experiment" in docstring
        and "declared landed-local profile" in scope
        and "fixture-aware complete boundary-order assignments" in scope
        and any(
            "landed-local profile function" in item for item in subsumes
        )
        and "for start in range(RING_STATIONS)" in ast.unparse(enumeration)
        and "K.interleaved_program(FIXTURE_BANKS)" in ast.unparse(build)
    )
    return {
        "pass": positive_scope and not forbidden_hits,
        "module_scope_verbatim": docstring,
        "decision_scope_verbatim": scope,
        "subsumes_verbatim": subsumes,
        "fixture_citations": {
            "build_fixture": f"lines {build.lineno}-{build.end_lineno}",
            "enumeration": (
                f"lines {enumeration.lineno}-{enumeration.end_lineno}"
            ),
            "decision": f"lines {decision.lineno}-{decision.end_lineno}",
        },
        "other_fixture_family_claims_found": forbidden_hits,
        "finding_verbatim": (
            "SCOPE HONESTY: the verdict is confined to the held Cycle-752 "
            "11-start fixture battery and its landed success criterion; no "
            "claim about other fixture families was found."
            if positive_scope and not forbidden_hits else
            "SCOPE HONESTY REFUTATION: an unscoped other-family verdict was "
            "found or the positive fixture scope was absent."
        ),
    }


def main() -> int:
    started = perf_counter()
    copied_path, primary_path, _support_path = AUDIT_INPUT_PATHS
    copied_text = (ROOT / copied_path).read_text(encoding="utf-8")
    primary_text = (ROOT / primary_path).read_text(encoding="utf-8")
    copied_tree = ast.parse(copied_text, filename=copied_path)
    primary_tree = ast.parse(primary_text, filename=primary_path)
    own_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )

    criterion = criterion_fidelity(copied_tree, primary_tree)
    witness_order = static_eval(
        assignment_node(copied_tree, "ROUTE3_FIXED_Q_ORDER")
    )
    if not isinstance(witness_order, tuple):
        raise AssertionError(("witness order", witness_order))
    primary_main = function_node(primary_tree, "main")
    primary_expected_counts = extract_primary_expected_counts(primary_main)
    primary_expected_totals = extract_primary_expected_totals(primary_main)
    primary_profile_names = extract_profile_names(primary_tree)

    fixture = build_fixture_own()
    first = enumerate_direct(fixture)
    second = enumerate_direct(fixture)
    success_sets = first["success_sets"]
    success_counts = tuple(len(rows) for rows in success_sets)
    dead_starts = tuple(
        start for start, count in enumerate(success_counts) if count == 0
    )
    live_starts = tuple(
        start for start, count in enumerate(success_counts) if count > 0
    )

    identity = identity_controls(success_sets, witness_order)
    exhaustive_pass = (
        success_counts == primary_expected_counts
        and success_counts == (512,) + (0,) * 10
        and dead_starts == tuple(range(1, RING_STATIONS))
        and live_starts == (0,)
        and all(
            len(digest) == 64 for digest in first["coverage_digests"]
        )
    )
    exhaustive = {
        "pass": exhaustive_pass,
        "assignment_encoding": (
            "local 11-bit mask; bit step=0 applies left=(start+step) then "
            "right, bit step=1 applies right then left"
        ),
        "method": (
            "direct nested loops over every integer mask 0..2047 at every "
            "start; macro state transitions are memoized, assignments are "
            "not pruned or sampled"
        ),
        "assignments_per_start": ASSIGNMENTS_PER_START,
        "starts": RING_STATIONS,
        "total_complete_assignments":
            RING_STATIONS * ASSIGNMENTS_PER_START,
        "success_counts_by_start": success_counts,
        "primary_ast_expected_counts_by_start": primary_expected_counts,
        "dead_starts": dead_starts,
        "satisfiable_starts": live_starts,
        "full_success_count_on_satisfiable_start":
            success_counts[live_starts[0]] if len(live_starts) == 1 else None,
        "distinct_final_outputs_by_start":
            first["distinct_output_counts"],
        "coverage_sha256_by_start": first["coverage_digests"],
        "transition_cache": first["transition_cache"],
        "sharp_refutation_assignment": (
            next(
                (
                    {"start": start, "mask": rows[0]}
                    for start, rows in enumerate(success_sets)
                    if start in range(1, RING_STATIONS) and rows
                ),
                None,
            )
        ),
        "finding_verbatim": (
            "EXHAUSTIVE RE-ENUMERATION: success counts by start are "
            f"{success_counts}; all 2,048 assignments per start were visited."
            if exhaustive_pass else
            "EXHAUSTIVE RE-ENUMERATION REFUTATION: "
            f"success counts by start are {success_counts}, versus primary "
            f"{primary_expected_counts}."
        ),
    }
    forced = forced_flexible_recount(
        fixture,
        success_sets,
        primary_profile_names,
        primary_expected_totals,
    )
    scope = scope_honesty(primary_tree, primary_text)

    observed_sha = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    own_paths_literal = static_eval(
        assignment_node(own_tree, "AUDIT_INPUT_PATHS")
    )
    blocked_loaded = tuple(
        name for name in COPIED_TEXT_ONLY_MODULES if name in sys.modules
    )
    deterministic = (
        first["projection_sha256"] == second["projection_sha256"]
        and first["success_sets"] == second["success_sets"]
        and first["distinct_output_counts"]
        == second["distinct_output_counts"]
        and first["coverage_digests"] == second["coverage_digests"]
    )
    runtime_seconds = perf_counter() - started
    controls_pass = (
        own_paths_literal == AUDIT_INPUT_PATHS
        and all(not Path(path).is_absolute() for path in AUDIT_INPUT_PATHS)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and observed_sha == EXPECTED_SHA256
        and _IMPORT_BLOCKER in sys.meta_path
        and not blocked_loaded
        and deterministic
        and fixture["expected_sha256"] == EXPECTED_TWO_SOURCE_SHA256
        and runtime_seconds < RUNTIME_LIMIT_SECONDS
    )
    controls = {
        "pass": controls_pass,
        "audit_input_paths_literal": own_paths_literal,
        "all_paths_worktree_relative": all(
            not Path(path).is_absolute() for path in AUDIT_INPUT_PATHS
        ),
        "all_paths_exist": all(
            (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
        ),
        "observed_sha256": observed_sha,
        "expected_sha256": EXPECTED_SHA256,
        "sha256_match": observed_sha == EXPECTED_SHA256,
        "import_blocklist": COPIED_TEXT_ONLY_MODULES,
        "blocklist_active": _IMPORT_BLOCKER in sys.meta_path,
        "blocked_modules_loaded": blocked_loaded,
        "determinism_run_1_sha256": first["projection_sha256"],
        "determinism_run_2_sha256": second["projection_sha256"],
        "determinism_match": deterministic,
        "expected_two_source_sha256": fixture["expected_sha256"],
        "runtime_seconds": runtime_seconds,
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "runtime_within_limit": runtime_seconds < RUNTIME_LIMIT_SECONDS,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_within_limit": True,
        "finding_verbatim": (
            "CONTROLS: SHA anchors, literal relative paths, primary "
            "blocklist, deterministic rerun, runtime, and stdout bounds pass."
            if controls_pass else
            "CONTROLS FAILURE: at least one SHA/path/blocklist/determinism/"
            "runtime control failed."
        ),
    }

    certificates = (
        ("CERTIFICATE_1_CRITERION_FIDELITY", criterion),
        ("CERTIFICATE_2_IDENTITY_CONTROLS", identity),
        ("CERTIFICATE_3_EXHAUSTIVE_RE_ENUMERATION", exhaustive),
        ("CERTIFICATE_4_FORCED_FLEXIBLE_RECOUNT", forced),
        ("CERTIFICATE_5_SCOPE_HONESTY", scope),
        ("CERTIFICATE_6_CONTROLS", controls),
    )

    def render() -> str:
        lines = [
            f"{'PASS' if detail['pass'] else 'FAIL'} {name} :: "
            f"{compact(detail)}"
            for name, detail in certificates
        ]
        confirmed = all(detail["pass"] for _name, detail in certificates)
        lines.append(
            "OVERALL="
            + ("CONFIRMED" if confirmed else "REFUTED")
            + f" runtime_seconds={runtime_seconds:.6f}"
        )
        return "\n".join(lines) + "\n"

    for _ in range(8):
        output = render()
        size = len(output.encode("utf-8"))
        replacement = size
        within = size < STDOUT_LIMIT_BYTES
        if (
            controls["stdout_bytes"] == replacement
            and controls["stdout_within_limit"] == within
        ):
            break
        controls["stdout_bytes"] = replacement
        controls["stdout_within_limit"] = within
    output = render()
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if all(detail["pass"] for _name, detail in certificates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
