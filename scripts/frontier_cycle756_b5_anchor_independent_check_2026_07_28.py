#!/usr/bin/env python3
"""Independent checker for the Cycle-756 b=5 exhaustive anchor.

Cycle 756 is parsed only as frozen AST data.  The executable dependencies are
the landed Cycle-719 controller core and the Cycle-740 parameterized mapper.
"""
from __future__ import annotations

import ast
from collections import Counter
import json
from math import comb
from pathlib import Path
import sys
from time import perf_counter

import numpy as np


AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/B5_EXHAUSTIVE_ANCHOR_CYCLE756_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

FROZEN_DATA_PATH = (
    "scripts/frontier_cycle756_b5_exhaustive_anchor_2026_07_28.py"
)
BLOCKLIST = (
    "frontier_cycle756_b5_exhaustive_anchor_2026_07_28",
)


class _PrimaryImportBlocker:
    """Make the data-only boundary executable, including transitive imports."""

    def find_spec(self, fullname, path=None, target=None):
        if fullname in BLOCKLIST:
            raise ImportError(f"blocked primary import: {fullname}")
        return None


_PRIMARY_BLOCKER = _PrimaryImportBlocker()
sys.meta_path.insert(0, _PRIMARY_BLOCKER)
sys.dont_write_bytecode = True

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle740_table_parameterized_mapper_2026_07_28 as M740


STDOUT_LIMIT_BYTES = 150 * 1024
BITPLANE_BATCH = 65_536
BANK_COUNT = 5
CAPACITY = 5
STATIONS = 35
TARGET_L35 = 20_633_239
TARGET_STEPS = 722_163_365
TARGET_NEAR_MISS = 70
TARGET_ROW_KINDS = {
    "bank": 5,
    "cross": 4,
    "finalizer": 1,
    "handoff": 8,
    "relay": 16,
    "source": 1,
}
TARGET_ZERO_KEYS = (
    "controller_structure_failures",
    "translation_failure_config_steps",
    "token_count_failure_config_steps",
    "adjacency_failure_config_steps",
    "adjacency_pair_incidences",
    "ownership_failure_config_steps",
    "ownership_violation_station_incidences",
    "B_rail_failure_config_steps",
    "work_failure_config_steps",
    "distance_failure_config_steps",
    "rail_closure_failures",
)
ANCHOR_LANGUAGE = (
    "This adds the fifth exhaustive anchor only.  It does not strengthen "
    "or otherwise change Cycle 740's conditional table-uniform general-b "
    "claim."
)

CHECKS: dict[str, bool] = {}
ERRORS: dict[str, str] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def error_text(error: BaseException) -> str:
    return f"{type(error).__name__}: {error}"[:1000]


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function", name, len(matches)))
    return matches[0]


def _assignments(scope: ast.AST, name: str) -> list[ast.AST]:
    matches = []
    body = scope.body if isinstance(scope, ast.Module) else ast.walk(scope)
    for node in body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            matches.append(node.value)
    return matches


def _assignment(scope: ast.AST, name: str) -> ast.AST:
    matches = _assignments(scope, name)
    if len(matches) != 1:
        raise AssertionError(("assignment", name, len(matches)))
    return matches[0]


def _literal(scope: ast.AST, name: str) -> object:
    return ast.literal_eval(_assignment(scope, name))


def _return_dictionary(function: ast.FunctionDef) -> ast.Dict:
    matches = [
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    if len(matches) != 1:
        raise AssertionError(("return dictionary", function.name, len(matches)))
    return matches[0]


def _dictionary_fields(node: ast.Dict) -> dict[str, ast.AST]:
    fields = {}
    for key, value in zip(node.keys, node.values):
        if key is None:
            continue
        literal_key = ast.literal_eval(key)
        if not isinstance(literal_key, str):
            raise AssertionError(("non-string return key", literal_key))
        fields[literal_key] = value
    return fields


def _multiplication_of_names(
    node: ast.AST, left: str, right: str
) -> bool:
    if not isinstance(node, ast.BinOp) or not isinstance(node.op, ast.Mult):
        return False
    names = (
        node.left.id if isinstance(node.left, ast.Name) else None,
        node.right.id if isinstance(node.right, ast.Name) else None,
    )
    return names in ((left, right), (right, left))


def _twice_stations(node: ast.AST) -> bool:
    if not isinstance(node, ast.BinOp) or not isinstance(node.op, ast.Mult):
        return False
    pair = (node.left, node.right)
    return (
        isinstance(pair[0], ast.Constant)
        and pair[0].value == 2
        and isinstance(pair[1], ast.Name)
        and pair[1].id == "STATIONS"
    ) or (
        isinstance(pair[1], ast.Constant)
        and pair[1].value == 2
        and isinstance(pair[0], ast.Name)
        and pair[0].id == "STATIONS"
    )


def extraction() -> dict[str, object]:
    """Recover the frozen Cycle-756 targets without importing that module."""

    if any(name in sys.modules for name in BLOCKLIST):
        raise AssertionError("primary was imported before extraction")
    source = Path(FROZEN_DATA_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=FROZEN_DATA_PATH)

    audit_node = _assignment(tree, "AUDIT_INPUT_PATHS")
    audit_paths = ast.literal_eval(audit_node)
    literal_audit_tuple = (
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )
    stations = _literal(tree, "STATIONS")
    bank_count = _literal(tree, "BANK_COUNT")
    capacity = _literal(tree, "CAPACITY")
    batch = _literal(tree, "BITPLANE_BATCH")
    l35 = _literal(tree, "EXPECTED_LUCAS_35")

    mapper_function = _function(tree, "mapper_and_i2_certificate")
    row_kinds = ast.literal_eval(
        _assignment(mapper_function, "expected_kind_counts")
    )

    orbit_function = _function(tree, "census_and_orbit_certificate")
    zero_keys = ast.literal_eval(
        _assignment(orbit_function, "zero_failure_keys")
    )
    steps_formula = _assignment(orbit_function, "expected_steps")
    zero_comparison_present = any(
        isinstance(node, ast.Compare)
        and len(node.ops) == 1
        and isinstance(node.ops[0], ast.Eq)
        and len(node.comparators) == 1
        and isinstance(node.comparators[0], ast.Constant)
        and node.comparators[0].value == 0
        for node in ast.walk(orbit_function)
    )

    near_function = _function(tree, "near_miss_certificate")
    near_fields = _dictionary_fields(_return_dictionary(near_function))
    near_formula = near_fields["expected_violating_stations"]

    boundary_function = _function(tree, "boundary_certificate")
    boundary_fields = _dictionary_fields(_return_dictionary(boundary_function))
    anchor_rings = ast.literal_eval(boundary_fields["anchor_ring_family"])
    anchor_banks = ast.literal_eval(boundary_fields["anchor_bank_family"])
    general_b_changed = ast.literal_eval(
        boundary_fields["general_b_claim_changed"]
    )
    language = ast.literal_eval(boundary_fields["general_b_boundary"])
    boundary_keys = tuple(boundary_fields)

    derived_steps = int(l35) * int(stations)
    derived_near_miss = 2 * int(stations)
    exact = (
        literal_audit_tuple
        and audit_paths == AUDIT_INPUT_PATHS
        and stations == STATIONS
        and bank_count == BANK_COUNT
        and capacity == CAPACITY
        and batch == BITPLANE_BATCH
        and l35 == TARGET_L35
        and row_kinds == TARGET_ROW_KINDS
        and tuple(zero_keys) == TARGET_ZERO_KEYS
        and zero_comparison_present
        and _multiplication_of_names(
            steps_formula, "census_total", "STATIONS"
        )
        and derived_steps == TARGET_STEPS
        and _twice_stations(near_formula)
        and derived_near_miss == TARGET_NEAR_MISS
        and anchor_rings == [3, 11, 19, 27, 35]
        and anchor_banks == [1, 2, 3, 4, 5]
        and "fifth_anchor_n35_orbits_exhausted" in boundary_keys
        and "b1_through_b5_now_all_exhausted" in boundary_keys
        and general_b_changed is False
        and language == ANCHOR_LANGUAGE
        and not any(name in sys.modules for name in BLOCKLIST)
    )
    return {
        "audit_input_paths": audit_paths,
        "audit_tuple_is_pure_literal": literal_audit_tuple,
        "stations": stations,
        "bank_count": bank_count,
        "capacity": capacity,
        "bitplane_batch": batch,
        "L35": l35,
        "row_kind_census": row_kinds,
        "expected_controller_steps": derived_steps,
        "zero_violation_keys": zero_keys,
        "zero_violation_target": 0,
        "near_miss_predicted_station_checks": derived_near_miss,
        "anchor_ring_family": anchor_rings,
        "anchor_bank_family": anchor_banks,
        "general_b_claim_changed": general_b_changed,
        "general_b_boundary": language,
        "primary_imported": any(name in sys.modules for name in BLOCKLIST),
        "exact": exact,
    }


def _path_polynomial(length: int) -> tuple[int, ...]:
    """Independent-set polynomial recurrence for a path."""

    if length == 0:
        return (1,)
    previous_previous = [1]
    previous = [1, 1]
    if length == 1:
        return tuple(previous)
    for _ in range(2, length + 1):
        current = [0] * max(len(previous), len(previous_previous) + 1)
        for degree, value in enumerate(previous):
            current[degree] += value
        for degree, value in enumerate(previous_previous):
            current[degree + 1] += value
        previous_previous, previous = previous, current
    return tuple(previous)


def _cycle_polynomial(stations: int) -> tuple[int, ...]:
    """Split on one cycle vertex and retain the coefficients by weight."""

    absent = _path_polynomial(stations - 1)
    present = _path_polynomial(stations - 3)
    result = [0] * (stations // 2 + 1)
    for degree, value in enumerate(absent):
        if degree < len(result):
            result[degree] += value
    for degree, value in enumerate(present):
        if degree + 1 < len(result):
            result[degree + 1] += value
    return tuple(result)


def _lucas(index: int) -> int:
    if index == 0:
        return 2
    if index == 1:
        return 1
    older, newer = 2, 1
    for _ in range(2, index + 1):
        older, newer = newer, older + newer
    return newer


_GAP_CHUNK_BITS = 10
_GAP_CHUNK_MASK = (1 << _GAP_CHUNK_BITS) - 1


def _make_gap_tables() -> tuple[tuple[int, ...], tuple[int, ...]]:
    expanded = []
    populations = []
    for value in range(1 << _GAP_CHUNK_BITS):
        output = 0
        rank = 0
        for bit in range(_GAP_CHUNK_BITS):
            if (value >> bit) & 1:
                output |= 1 << (bit + rank)
                rank += 1
        expanded.append(output)
        populations.append(rank)
    return tuple(expanded), tuple(populations)


_GAP_EXPANDED, _GAP_POPULATIONS = _make_gap_tables()


def _insert_separating_gaps(choice: int) -> int:
    output = 0
    prior_rank = 0
    base = 0
    while choice >> base:
        chunk = (choice >> base) & _GAP_CHUNK_MASK
        output |= _GAP_EXPANDED[chunk] << (base + prior_rank)
        prior_rank += _GAP_POPULATIONS[chunk]
        base += _GAP_CHUNK_BITS
    return output


def _path_masks(
    start: int, length: int, occupied: int
):
    if occupied < 0 or occupied > (length + 1) // 2:
        return
    if occupied == 0:
        yield 0
        return
    choice_width = length - occupied + 1
    choice = (1 << occupied) - 1
    limit = 1 << choice_width
    while choice < limit:
        yield _insert_separating_gaps(choice) << start
        low = choice & -choice
        raised = choice + low
        choice = raised + (((raised ^ choice) // low) >> 2)


def _cycle_masks(stations: int, occupied: int):
    yield from _path_masks(1, stations - 1, occupied)
    if occupied:
        for mask in _path_masks(2, stations - 3, occupied - 1):
            yield mask | 1


def _has_cycle_adjacency(mask: int, stations: int) -> bool:
    full = (1 << stations) - 1
    rotated = ((mask << 1) & full) | (mask >> (stations - 1))
    return bool(mask & rotated)


def census_recount() -> dict[str, object]:
    """Stream every C_35 independent mask and recount each weight stratum."""

    recurrence = _cycle_polynomial(STATIONS)
    streamed = []
    popcount_failures = 0
    adjacency_failures = 0
    for occupied in range(len(recurrence)):
        count = 0
        for mask in _cycle_masks(STATIONS, occupied):
            count += 1
            popcount_failures += int(mask.bit_count() != occupied)
            adjacency_failures += int(
                _has_cycle_adjacency(mask, STATIONS)
            )
        streamed.append(count)
    streamed_tuple = tuple(streamed)
    total = sum(streamed_tuple)
    lucas = _lucas(STATIONS)
    exact = (
        streamed_tuple == recurrence
        and total == sum(recurrence) == lucas == TARGET_L35
        and popcount_failures == adjacency_failures == 0
    )
    return {
        "counts_by_k": streamed_tuple,
        "recurrence_counts_by_k": recurrence,
        "streamed_total": total,
        "lucas_recurrence_total": lucas,
        "popcount_failures": popcount_failures,
        "adjacency_failures": adjacency_failures,
        "exact": exact,
    }


def _apply_small_gate(state: int, gate: tuple[str, tuple[int, ...]]) -> int:
    kind, wires = gate
    if kind == "X":
        return state ^ (1 << wires[0])
    if kind == "CNOT":
        return (
            state ^ (1 << wires[1])
            if (state >> wires[0]) & 1
            else state
        )
    if kind == "TOF":
        return (
            state ^ (1 << wires[2])
            if ((state >> wires[0]) & 1)
            and ((state >> wires[1]) & 1)
            else state
        )
    raise ValueError(kind)


def _apply_small_word(
    state: int, word: tuple[tuple[str, tuple[int, ...]], ...]
) -> int:
    for gate in word:
        state = _apply_small_gate(state, gate)
    return state


def _primitive_clean_truth() -> dict[str, object]:
    definitions = {
        "X": (1, (("X", (0,)),)),
        "CNOT": (2, (("CNOT", (0, 1)),)),
        "TOF": (3, (("TOF", (0, 1, 2)),)),
    }
    report = {}
    total_rows = 0
    total_failures = 0
    for kind, (data_width, semantic) in definitions.items():
        control = data_width
        work = data_width + 1
        if kind == "X":
            lifted = (("CNOT", (control, 0)),)
        elif kind == "CNOT":
            lifted = (("TOF", (control, 0, 1)),)
        else:
            lifted = (
                ("TOF", (control, 0, work)),
                ("TOF", (work, 1, 2)),
                ("TOF", (control, 0, work)),
            )
        failures = 0
        rows = 0
        for clean_basis in range(1 << (data_width + 1)):
            rows += 1
            observed = _apply_small_word(clean_basis, lifted)
            expected = clean_basis
            if (clean_basis >> control) & 1:
                expected = _apply_small_word(expected, semantic)
            failures += int(observed != expected)
            failures += int(bool((observed >> work) & 1))
            failures += int(
                ((observed >> control) & 1)
                != ((clean_basis >> control) & 1)
            )
        total_rows += rows
        total_failures += failures
        report[kind] = {
            "clean_truth_rows": rows,
            "failures": failures,
            "exact": failures == 0,
        }
    return {
        "per_kind": report,
        "clean_truth_rows": total_rows,
        "failures": total_failures,
        "exact": total_failures == 0,
    }


def _compile_mapped_word(
    word: tuple[object, ...],
    data_width: int,
    primitive: dict[str, object],
) -> tuple[tuple[tuple[int, int, int, int], ...], int]:
    compiled = []
    failures = 0
    arity = {"X": 1, "CNOT": 2, "TOF": 3}
    for gate in word:
        kind = getattr(gate, "kind", None)
        wires = tuple(getattr(gate, "wires", ()))
        failures += int(kind not in arity)
        if kind not in arity:
            continue
        failures += int(len(wires) != arity[kind])
        failures += int(
            any(
                isinstance(wire, bool)
                or not isinstance(wire, int)
                or wire < 0
                or wire >= data_width
                for wire in wires
            )
        )
        failures += int(len(set(wires)) != len(wires))
        failures += int(
            not primitive["per_kind"][kind]["exact"]
        )
        if len(wires) != arity[kind]:
            continue
        if kind == "X":
            compiled.append((1, 0, 0, int(wires[0])))
        elif kind == "CNOT":
            compiled.append(
                (2, int(wires[0]), 0, int(wires[1]))
            )
        else:
            compiled.append(
                (3, int(wires[0]), int(wires[1]), int(wires[2]))
            )
    return tuple(compiled), failures


def rows_recount() -> tuple[
    dict[str, object],
    tuple[tuple[tuple[int, int, int, int], ...], ...],
    int,
]:
    """Map all C=5 rows and independently discharge clean-work structure."""

    primitive = _primitive_clean_truth()
    program = M740.parameterized_program(BANK_COUNT, CAPACITY)
    data_width = M740.parameterized_data_width(CAPACITY)
    kind_counts = Counter()
    gate_counts = Counter()
    compiled_rows = []
    row_failures = 0
    mapped_gates = 0
    for row in program:
        kind_counts[row[0]] += 1
        try:
            mapped = tuple(
                M740.parameterized_mapped_macro(row, CAPACITY)
            )
            compiled, failures = _compile_mapped_word(
                mapped, data_width, primitive
            )
        except Exception:
            compiled = ()
            failures = 1
        compiled_rows.append(compiled)
        row_failures += int(failures != 0)
        mapped_gates += len(mapped) if "mapped" in locals() else 0
        if "mapped" in locals():
            gate_counts.update(gate.kind for gate in mapped)
            del mapped
    exact = (
        primitive["exact"]
        and len(program) == STATIONS
        and program == K.interleaved_program(BANK_COUNT)
        and data_width == 2_224
        and dict(sorted(kind_counts.items())) == TARGET_ROW_KINDS
        and row_failures == 0
        and len(compiled_rows) == STATIONS
        and mapped_gates
        == sum(len(row) for row in compiled_rows)
    )
    report = {
        "rows": len(program),
        "capacity": CAPACITY,
        "data_width": data_width,
        "row_kind_census": dict(sorted(kind_counts.items())),
        "semantic_gate_kind_census": dict(sorted(gate_counts.items())),
        "mapped_gates_evaluated": mapped_gates,
        "clean_rows": len(program) - row_failures,
        "clean_row_failures": row_failures,
        "primitive_clean_truth": primitive,
        "exact": exact,
    }
    return report, tuple(compiled_rows), data_width


def _compile_q_evaluator(
    compiled_rows: tuple[
        tuple[tuple[int, int, int, int], ...], ...
    ],
):
    """Specialize the independent controlled semantic-gate evaluator."""

    lines = ["def apply_q(planes, a):"]
    lines.extend(
        f"    control_{station} = a[{station}]"
        for station in range(len(compiled_rows))
    )
    for station, row in enumerate(compiled_rows):
        control = f"control_{station}"
        for kind, left, right, target in row:
            if kind == 1:
                lines.append(
                    f"    planes[{target}] ^= {control}"
                )
            elif kind == 2:
                lines.append(
                    f"    planes[{target}] ^= "
                    f"{control} & planes[{left}]"
                )
            elif kind == 3:
                lines.append(
                    f"    planes[{target}] ^= "
                    f"{control} & planes[{left}] & planes[{right}]"
                )
            else:
                raise AssertionError(("compiled kind", kind))
    namespace: dict[str, object] = {}
    source = "\n".join(lines) + "\n"
    exec(compile(source, "<independent-bitplane-Q>", "exec"), namespace)
    return namespace["apply_q"], len(source.encode())


def _batch_to_planes(
    masks: list[int],
) -> tuple[tuple[int, ...], int]:
    rows = len(masks)
    array = np.asarray(masks, dtype="<u8")
    byte_rows = array.view(np.uint8).reshape(rows, 8)
    bits = np.unpackbits(
        byte_rows, axis=1, bitorder="little"
    )[:, :STATIONS]
    packed = np.packbits(bits.T, axis=1, bitorder="little")
    planes = tuple(
        int.from_bytes(packed[index].tobytes(), "little")
        for index in range(STATIONS)
    )
    return planes, rows


def _population_planes(planes: list[int]) -> tuple[int, ...]:
    digits = [0] * max(1, len(planes).bit_length())
    for plane in planes:
        carry = plane
        digit = 0
        while carry:
            if digit == len(digits):
                digits.append(0)
            overlap = digits[digit] & carry
            digits[digit] ^= carry
            carry = overlap
            digit += 1
    return tuple(digits)


def _empty_orbit_stats() -> dict[str, int]:
    return {
        "evaluated_configurations": 0,
        "exhaustive_controller_steps": 0,
        "occupied_station_invariant_checks": 0,
        "distance_pair_incidence_checks": 0,
        "distance_bitplane_pair_comparisons": 0,
        "mapped_gate_configuration_applications": 0,
        "mapped_gate_bitplane_applications": 0,
        "rail_swap_configuration_applications": 0,
        "controller_structure_failures": 0,
        "translation_failure_config_steps": 0,
        "token_count_failure_config_steps": 0,
        "adjacency_failure_config_steps": 0,
        "adjacency_pair_incidences": 0,
        "ownership_failure_config_steps": 0,
        "ownership_violation_station_incidences": 0,
        "B_rail_failure_config_steps": 0,
        "work_failure_config_steps": 0,
        "distance_failure_config_steps": 0,
        "rail_closure_failures": 0,
    }


def _add_stats(target: dict[str, int], source: dict[str, int]) -> None:
    for key, value in source.items():
        target[key] += value


def _evaluate_batch(
    original_a: tuple[int, ...],
    rows: int,
    occupied: int,
    data_width: int,
    mapped_gates: int,
    apply_q,
) -> dict[str, int]:
    row_full = (1 << rows) - 1
    data = [0] * data_width
    a = list(original_a)
    b = [0] * STATIONS
    work = [0] * STATIONS
    stats = _empty_orbit_stats()
    stats["evaluated_configurations"] = rows

    for step in range(STATIONS):
        translation_bad = 0
        for station in range(STATIONS):
            expected = original_a[(station - step) % STATIONS]
            translation_bad |= a[station] ^ expected
        stats["translation_failure_config_steps"] += (
            translation_bad.bit_count()
        )

        b_bad = 0
        work_bad = 0
        for plane in b:
            b_bad |= plane
        for plane in work:
            work_bad |= plane
        stats["B_rail_failure_config_steps"] += b_bad.bit_count()
        stats["work_failure_config_steps"] += work_bad.bit_count()

        count_bad = 0
        count_digits = _population_planes(a + b)
        for digit, observed in enumerate(count_digits):
            expected = row_full if (occupied >> digit) & 1 else 0
            count_bad |= observed ^ expected
        stats["token_count_failure_config_steps"] += (
            count_bad.bit_count()
        )

        adjacency_bad = 0
        ownership_bad = 0
        for station in range(STATIONS):
            left = (station - 1) % STATIONS
            right = (station + 1) % STATIONS
            adjacent = a[station] & a[right]
            adjacency_bad |= adjacent
            stats["adjacency_pair_incidences"] += adjacent.bit_count()
            dirty = (
                a[left]
                | a[right]
                | b[left]
                | b[station]
                | b[right]
                | work[station]
            )
            violation = a[station] & dirty
            ownership_bad |= violation
            stats[
                "ownership_violation_station_incidences"
            ] += violation.bit_count()
        stats["adjacency_failure_config_steps"] += (
            adjacency_bad.bit_count()
        )
        stats["ownership_failure_config_steps"] += (
            ownership_bad.bit_count()
        )

        distance_bad = 0
        for left in range(STATIONS):
            moved_left = (left + step) % STATIONS
            for right in range(left + 1, STATIONS):
                moved_right = (right + step) % STATIONS
                expected_pair = original_a[left] & original_a[right]
                observed_pair = a[moved_left] & a[moved_right]
                distance_bad |= expected_pair ^ observed_pair
        stats["distance_failure_config_steps"] += (
            distance_bad.bit_count()
        )
        stats["distance_bitplane_pair_comparisons"] += comb(
            STATIONS, 2
        )
        stats["distance_pair_incidence_checks"] += (
            rows * comb(occupied, 2)
        )
        stats["occupied_station_invariant_checks"] += rows * occupied
        stats["exhaustive_controller_steps"] += rows
        stats["mapped_gate_configuration_applications"] += (
            rows * mapped_gates
        )
        stats["mapped_gate_bitplane_applications"] += mapped_gates
        stats["rail_swap_configuration_applications"] += (
            rows * 2 * STATIONS
        )

        apply_q(data, a)
        for station in range(STATIONS):
            a[station], b[station] = b[station], a[station]
        for station in range(STATIONS):
            target = (station + 1) % STATIONS
            b[station], a[target] = a[target], b[station]

    closure_bad = 0
    for observed, expected in zip(a, original_a):
        closure_bad |= observed ^ expected
    for plane in b:
        closure_bad |= plane
    for plane in work:
        closure_bad |= plane
    stats["rail_closure_failures"] += closure_bad.bit_count()
    return stats


def orbit_recount(
    compiled_rows: tuple[
        tuple[tuple[int, int, int, int], ...], ...
    ],
    data_width: int,
    counts_by_k: tuple[int, ...],
) -> dict[str, object]:
    """Run the full 65,536-row independent reversible bit-plane sweep."""

    apply_q, generated_evaluator_bytes = _compile_q_evaluator(
        compiled_rows
    )
    mapped_gates = sum(len(row) for row in compiled_rows)
    aggregate = _empty_orbit_stats()
    batch_count = 0
    streamed_counts = []
    for occupied, expected_count in enumerate(counts_by_k):
        batch = []
        stratum_count = 0
        for mask in _cycle_masks(STATIONS, occupied):
            batch.append(mask)
            stratum_count += 1
            if len(batch) == BITPLANE_BATCH:
                planes, rows = _batch_to_planes(batch)
                _add_stats(
                    aggregate,
                    _evaluate_batch(
                        planes,
                        rows,
                        occupied,
                        data_width,
                        mapped_gates,
                        apply_q,
                    ),
                )
                batch_count += 1
                batch = []
        if batch:
            planes, rows = _batch_to_planes(batch)
            _add_stats(
                aggregate,
                _evaluate_batch(
                    planes,
                    rows,
                    occupied,
                    data_width,
                    mapped_gates,
                    apply_q,
                ),
            )
            batch_count += 1
        streamed_counts.append(stratum_count)
        print(
            f"orbit progress k={occupied} "
            f"configs={stratum_count}/{expected_count}",
            file=sys.stderr,
            flush=True,
        )

    total = sum(streamed_counts)
    expected_steps = total * STATIONS
    expected_occupied = sum(
        occupied * count * STATIONS
        for occupied, count in enumerate(counts_by_k)
    )
    expected_distance = sum(
        comb(occupied, 2) * count * STATIONS
        for occupied, count in enumerate(counts_by_k)
    )
    zero_census = {
        key: aggregate[key] for key in TARGET_ZERO_KEYS
    }
    exact = (
        tuple(streamed_counts) == counts_by_k
        and total == TARGET_L35
        and aggregate["evaluated_configurations"] == total
        and expected_steps == TARGET_STEPS
        and aggregate["exhaustive_controller_steps"] == TARGET_STEPS
        and aggregate["occupied_station_invariant_checks"]
        == expected_occupied
        and aggregate["distance_pair_incidence_checks"]
        == expected_distance
        and all(value == 0 for value in zero_census.values())
        and mapped_gates > 0
        and aggregate["mapped_gate_configuration_applications"]
        == mapped_gates * TARGET_STEPS
        and aggregate["rail_swap_configuration_applications"]
        == 2 * STATIONS * TARGET_STEPS
    )
    return {
        "streamed_counts_by_k": tuple(streamed_counts),
        "evaluated_configurations": total,
        "bitplane_batch": BITPLANE_BATCH,
        "bitplane_batches": batch_count,
        "mapped_gates_per_controller_step": mapped_gates,
        "generated_Q_evaluator_bytes": generated_evaluator_bytes,
        "exhaustive_controller_steps":
            aggregate["exhaustive_controller_steps"],
        "occupied_station_invariant_checks":
            aggregate["occupied_station_invariant_checks"],
        "distance_pair_incidence_checks":
            aggregate["distance_pair_incidence_checks"],
        "distance_bitplane_pair_comparisons":
            aggregate["distance_bitplane_pair_comparisons"],
        "mapped_gate_configuration_applications":
            aggregate["mapped_gate_configuration_applications"],
        "rail_swap_configuration_applications":
            aggregate["rail_swap_configuration_applications"],
        "zero_violation_census": zero_census,
        "full_sweep": True,
        "exact": exact,
    }


def _near_miss_reasons(
    mask: int, station: int
) -> tuple[str, ...]:
    if not ((mask >> station) & 1):
        return ()
    reasons = []
    if (mask >> ((station - 1) % STATIONS)) & 1:
        reasons.append("left_A")
    if (mask >> ((station + 1) % STATIONS)) & 1:
        reasons.append("right_A")
    return tuple(reasons)


def near_miss_recount() -> dict[str, object]:
    predicted_checks = 0
    observed_checks = 0
    unexpected_checks = 0
    failed_controls = 0
    for left in range(STATIONS):
        right = (left + 1) % STATIONS
        mask = (1 << left) | (1 << right)
        predicted = {left, right}
        observed = {
            station
            for station in range(STATIONS)
            if _near_miss_reasons(mask, station)
        }
        predicted_checks += len(predicted)
        observed_checks += len(observed & predicted)
        unexpected_checks += len(observed - predicted)
        reasons = sum(
            len(_near_miss_reasons(mask, station))
            for station in observed
        )
        failed_controls += int(
            observed != predicted or reasons != 2
        )
    exact = (
        predicted_checks == observed_checks == TARGET_NEAR_MISS
        and unexpected_checks == failed_controls == 0
    )
    return {
        "adjacent_pair_controls": STATIONS,
        "predicted_station_checks": predicted_checks,
        "observed_at_predicted_stations": observed_checks,
        "unexpected_station_checks": unexpected_checks,
        "failed_controls": failed_controls,
        "exact": exact,
    }


def discipline(extracted: dict[str, object]) -> dict[str, object]:
    primary_imported = any(name in sys.modules for name in BLOCKLIST)
    exact = (
        BLOCKLIST
        == ("frontier_cycle756_b5_exhaustive_anchor_2026_07_28",)
        and not primary_imported
        and _PRIMARY_BLOCKER in sys.meta_path
        and extracted["anchor_ring_family"] == [3, 11, 19, 27, 35]
        and extracted["anchor_bank_family"] == [1, 2, 3, 4, 5]
        and extracted["general_b_boundary"] == ANCHOR_LANGUAGE
        and extracted["general_b_claim_changed"] is False
    )
    return {
        "blocklist": BLOCKLIST,
        "blocklist_clean": not primary_imported,
        "fifth_anchor_language_verbatim":
            extracted["general_b_boundary"] == ANCHOR_LANGUAGE,
        "b1_through_b5_exhausted_language_anchored":
            extracted["anchor_bank_family"] == [1, 2, 3, 4, 5],
        "general_b_claim_unchanged":
            extracted["general_b_claim_changed"] is False,
        "exact": exact,
    }


def main() -> int:
    started = perf_counter()
    reports: dict[str, object] = {}

    try:
        extracted = extraction()
    except Exception as error:
        ERRORS["extraction"] = error_text(error)
        extracted = {"exact": False}
    reports["extraction"] = extracted
    check(
        "A_AST_extraction_frozen_censuses_and_literal_AUDIT",
        extracted.get("exact", False),
    )

    try:
        census = census_recount()
    except Exception as error:
        ERRORS["census_recount"] = error_text(error)
        census = {"exact": False, "counts_by_k": (), "streamed_total": 0}
    reports["census_recount"] = census
    check(
        "B_streamed_C35_census_by_k_and_Lucas_20633239",
        census["exact"],
    )

    compiled_rows = ()
    data_width = 0
    try:
        rows, compiled_rows, data_width = rows_recount()
    except Exception as error:
        ERRORS["rows_recount"] = error_text(error)
        rows = {"exact": False, "row_kind_census": {}, "clean_rows": 0}
    reports["rows_recount"] = rows
    check(
        "C_all_b5_C5_rows_own_clean_work_and_kind_recount",
        rows["exact"],
    )

    try:
        if not census["exact"] or not rows["exact"]:
            raise AssertionError("orbit prerequisites failed")
        orbit = orbit_recount(
            compiled_rows, data_width, census["counts_by_k"]
        )
    except Exception as error:
        ERRORS["orbit_recount"] = error_text(error)
        orbit = {
            "exact": False,
            "evaluated_configurations": 0,
            "exhaustive_controller_steps": 0,
            "zero_violation_census": {},
        }
    reports["orbit_recount"] = orbit
    check(
        "D_full_722163365_step_own_bitplane_orbit_zero_violations",
        orbit["exact"],
    )

    try:
        near_miss = near_miss_recount()
    except Exception as error:
        ERRORS["near_miss_recount"] = error_text(error)
        near_miss = {"exact": False}
    reports["near_miss_recount"] = near_miss
    check(
        "E_near_miss_70_of_70_at_predicted_stations",
        near_miss["exact"],
    )

    try:
        if not extracted.get("exact", False):
            raise AssertionError("discipline extraction prerequisite failed")
        bounded = discipline(extracted)
    except Exception as error:
        ERRORS["discipline"] = error_text(error)
        bounded = {"exact": False, "blocklist_clean": False}
    reports["discipline"] = bounded
    check(
        "F_blocklist_and_fifth_anchor_general_b_discipline",
        bounded["exact"],
    )

    elapsed = perf_counter() - started
    check(
        "TIMEOUT_runtime_under_1800_seconds",
        elapsed < AUDIT_TIMEOUT_SEC,
    )

    provisional = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "reports": reports,
        "errors": ERRORS,
        "checks": CHECKS,
        "runtime_seconds": round(elapsed, 6),
    }
    provisional_text = "\n".join(OUTPUT_LINES) + "\n" + json.dumps(
        provisional, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(provisional_text.encode()) + 4096 < STDOUT_LIMIT_BYTES,
    )

    report = {
        **provisional,
        "checks": dict(sorted(CHECKS.items())),
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "pass": all(CHECKS.values()),
    }
    report["terminal"] = (
        "CYCLE756_B5_ANCHOR_INDEPENDENT_CHECK_ALL_PASS"
        if report["pass"]
        else "CYCLE756_B5_ANCHOR_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    text = "\n".join(OUTPUT_LINES) + "\n" + json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    ) + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(
            "FAIL OUTPUT_stdout_under_150KB :: False\n"
            '{"pass":false,"terminal":'
            '"CYCLE756_B5_ANCHOR_INDEPENDENT_CHECK_HONEST_FAIL"}\n'
        )
        return 1
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
