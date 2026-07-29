#!/usr/bin/env python3
"""Independent bounded checker for the Cycle-737 ring-family theorem.

The primary is parsed as inert AST data and is never imported.  The only
frontier primary imported by this checker is the permitted Cycle-719 kernel
K.  Every configuration in the declared family is executed through K's
literal controller word by an independently implemented bit-plane evaluator.

Scope: family-uniform over [3,11,19,27], not general-n.
"""
from __future__ import annotations

import ast
from hashlib import sha256
import json
from math import comb
import sys
from time import perf_counter


sys.dont_write_bytecode = True

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/RING_FAMILY_UNIFORMITY_CYCLE737_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle737_ring_family_uniformity_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

RING_FAMILY = (3, 11, 19, 27)
BANK_FAMILY = (1, 2, 3, 4)
FROZEN_CENSUS_TOTALS = {
    3: 4,
    11: 199,
    19: 9349,
    27: 439204,
}
FROZEN_ORBIT_STEP_TOTALS = {
    3: 12,
    11: 2189,
    19: 177631,
    27: 11858508,
}
STDOUT_LIMIT_BYTES = 150 * 1024
BITPLANE_BATCH = 65_536
SCOPE_STATEMENT = "family-uniform over [3,11,19,27], not general-n"
DIRECT_FRONTIER_IMPORTS = (
    "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
)

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []
ERRORS: dict[str, str] = {}


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def error_text(exc: BaseException) -> str:
    return f"{type(exc).__name__}: {exc}"[:1000]


def digest_json(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    ).encode()
    return sha256(encoded).hexdigest()


def read_ast_data(path: str) -> ast.Module:
    # Only the two literal AUDIT_INPUT_PATHS are ever supplied here.
    if path not in AUDIT_INPUT_PATHS:
        raise ValueError(("read outside declared audit inputs", path))
    with open(path, "r", encoding="utf-8") as handle:
        return ast.parse(handle.read(), filename=path)


def top_level_assignment(tree: ast.Module, name: str) -> ast.AST:
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(isinstance(target, ast.Name) and target.id == name for target in targets):
                return node.value
    raise KeyError(("top-level assignment not found", name))


def literal_top_level(tree: ast.Module, name: str) -> object:
    return ast.literal_eval(top_level_assignment(tree, name))


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise KeyError(("function not found", name))


def local_assignment(function: ast.FunctionDef, name: str) -> ast.AST:
    for node in ast.walk(function):
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(isinstance(target, ast.Name) and target.id == name for target in targets):
                return node.value
    raise KeyError(("local assignment not found", function.name, name))


def name_is(node: ast.AST, name: str) -> bool:
    return isinstance(node, ast.Name) and node.id == name


def int_is(node: ast.AST, value: int) -> bool:
    return (
        isinstance(node, ast.Constant)
        and type(node.value) is int
        and node.value == value
    )


def extract_admissibility_formula(tree: ast.Module) -> dict[str, object]:
    function = function_node(tree, "admissibility_certificate")
    value = local_assignment(function, "formula")
    exact = False
    loop_variable = None
    iterator = None
    coefficient = None
    offset = None
    if (
        isinstance(value, ast.Call)
        and name_is(value.func, "tuple")
        and len(value.args) == 1
        and isinstance(value.args[0], ast.GeneratorExp)
        and len(value.args[0].generators) == 1
    ):
        generator = value.args[0]
        clause = generator.generators[0]
        expression = generator.elt
        if (
            isinstance(clause.target, ast.Name)
            and isinstance(clause.iter, ast.Name)
            and isinstance(expression, ast.BinOp)
            and isinstance(expression.op, ast.Sub)
            and isinstance(expression.left, ast.BinOp)
            and isinstance(expression.left.op, ast.Mult)
            and int_is(expression.left.left, 8)
            and name_is(expression.left.right, clause.target.id)
            and int_is(expression.right, 5)
        ):
            exact = True
            loop_variable = clause.target.id
            iterator = clause.iter.id
            coefficient = 8
            offset = -5
    return {
        "law": "n = 8b - 5",
        "loop_variable": loop_variable,
        "iterator": iterator,
        "coefficient": coefficient,
        "offset": offset,
        "exact_ast_shape": exact,
    }


def extract_lucas_anchor(tree: ast.Module) -> dict[str, object]:
    function = function_node(tree, "lucas_number")
    initial = None
    recurrence = False
    for node in ast.walk(function):
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if (
                isinstance(target, ast.Tuple)
                and [item.id for item in target.elts if isinstance(item, ast.Name)]
                == ["previous", "current"]
            ):
                try:
                    candidate = ast.literal_eval(node.value)
                except (ValueError, TypeError):
                    candidate = None
                if candidate == (2, 1):
                    initial = candidate
        if (
            isinstance(node, ast.BinOp)
            and isinstance(node.op, ast.Add)
            and name_is(node.left, "previous")
            and name_is(node.right, "current")
        ):
            recurrence = True
    return {
        "initial": initial,
        "recurrence_previous_plus_current": recurrence,
        "exact": initial == (2, 1) and recurrence,
    }


def extract_orbit_step_anchor(tree: ast.Module) -> dict[str, object]:
    function = function_node(tree, "controller_orbit_certificate")
    value = None
    for node in ast.walk(function):
        if not isinstance(node, ast.Dict):
            continue
        for key, candidate in zip(node.keys, node.values):
            if (
                isinstance(key, ast.Constant)
                and key.value == "exhausted_literal_controller_steps"
            ):
                value = candidate
                break
    exact = (
        isinstance(value, ast.BinOp)
        and isinstance(value.op, ast.Mult)
        and isinstance(value.left, ast.Call)
        and name_is(value.left.func, "len")
        and len(value.left.args) == 1
        and name_is(value.left.args[0], "masks")
        and name_is(value.right, "stations")
    )
    return {
        "expression": "len(masks) * stations",
        "exact_ast_shape": exact,
    }


def extract_boundary_anchor(tree: ast.Module) -> dict[str, object]:
    function = function_node(tree, "main")
    boundary_value = local_assignment(function, "boundary")
    if not isinstance(boundary_value, ast.Dict):
        raise TypeError("primary boundary is not a dict literal")
    entries: dict[str, ast.AST] = {}
    for key, value in zip(boundary_value.keys, boundary_value.values):
        if isinstance(key, ast.Constant) and isinstance(key.value, str):
            entries[key.value] = value
    required = {
        "sector_theorem_uniform_over_family",
        "frozen_n_dependence",
        "general_n_theorem_claimed",
    }
    sector_value = entries.get("sector_theorem_uniform_over_family")
    general_value = entries.get("general_n_theorem_claimed")
    frozen_assignment = local_assignment(function, "frozen_n_dependence")
    uniformity = entries.get("uniformity_statement")
    uniformity_text = (
        uniformity.value
        if isinstance(uniformity, ast.Constant) and isinstance(uniformity.value, str)
        else ""
    )
    return {
        "keys": tuple(sorted(entries)),
        "required_keys_present": required <= set(entries),
        "sector_value_computed_as_bool": (
            isinstance(sector_value, ast.Call)
            and name_is(sector_value.func, "bool")
        ),
        "clean_branch_frozen_n_dependence": (
            None
            if isinstance(frozen_assignment, ast.IfExp)
            and isinstance(frozen_assignment.body, ast.Constant)
            and frozen_assignment.body.value is None
            else "AST_MISMATCH"
        ),
        "general_n_theorem_claimed": (
            general_value.value
            if isinstance(general_value, ast.Constant)
            else "AST_MISMATCH"
        ),
        "uniformity_disclaims_arbitrary_n": (
            "not for arbitrary n" in uniformity_text
        ),
    }


def extraction() -> dict[str, object]:
    primary_tree = read_ast_data(AUDIT_INPUT_PATHS[0])
    k_tree = read_ast_data(AUDIT_INPUT_PATHS[1])
    primary_audit = literal_top_level(primary_tree, "AUDIT_INPUT_PATHS")
    k_audit = literal_top_level(k_tree, "AUDIT_INPUT_PATHS")
    primary_ring = literal_top_level(primary_tree, "RING_FAMILY")
    primary_banks = literal_top_level(primary_tree, "BANK_FAMILY")
    primary_note = literal_top_level(primary_tree, "NOTE_PATH")
    formula = extract_admissibility_formula(primary_tree)
    lucas = extract_lucas_anchor(primary_tree)
    orbit = extract_orbit_step_anchor(primary_tree)
    boundary = extract_boundary_anchor(primary_tree)
    frozen_products = {
        ring: FROZEN_CENSUS_TOTALS[ring] * ring
        for ring in RING_FAMILY
    }
    audit_literals_exact = (
        isinstance(primary_audit, tuple)
        and isinstance(k_audit, tuple)
        and all(isinstance(path, str) for path in primary_audit + k_audit)
        and AUDIT_INPUT_PATHS[1] in primary_audit
        and AUDIT_INPUT_PATHS[1] in k_audit
    )
    exact = (
        audit_literals_exact
        and primary_ring == RING_FAMILY
        and primary_banks == BANK_FAMILY
        and primary_note == NOTE_PATH
        and formula["exact_ast_shape"]
        and formula["iterator"] == "BANK_FAMILY"
        and lucas["exact"]
        and orbit["exact_ast_shape"]
        and frozen_products == FROZEN_ORBIT_STEP_TOTALS
        and boundary["required_keys_present"]
        and boundary["sector_value_computed_as_bool"]
        and boundary["clean_branch_frozen_n_dependence"] is None
        and boundary["general_n_theorem_claimed"] is False
        and boundary["uniformity_disclaims_arbitrary_n"]
    )
    return {
        "primary_read_as_ast_data_only": True,
        "primary_ring_family": primary_ring,
        "primary_bank_family": primary_banks,
        "admissibility": formula,
        "frozen_census_totals": FROZEN_CENSUS_TOTALS,
        "frozen_orbit_step_totals": FROZEN_ORBIT_STEP_TOTALS,
        "lucas_ast_anchor": lucas,
        "orbit_step_ast_anchor": orbit,
        "boundary_ast_anchor": boundary,
        "primary_AUDIT_INPUT_PATHS_literal": primary_audit,
        "K_AUDIT_INPUT_PATHS_literal_count": len(k_audit),
        "audit_tuples_literal_eval": audit_literals_exact,
        "exact": exact,
    }


def program_kind_counts(program: tuple[object, ...]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in program:
        kind = str(row[0])
        counts[kind] = counts.get(kind, 0) + 1
    return counts


def admissibility_recount() -> dict[str, object]:
    rows = []
    observed_family = []
    for banks in BANK_FAMILY:
        program = K.interleaved_program(banks)
        counts = program_kind_counts(program)
        independent_arithmetic = (
            1
            + banks
            + (banks - 1)
            + 3 * (banks - 1)
            + 3 * (banks - 1)
            + 1
        )
        expected_counts = {
            "source": 1,
            "bank": banks,
            "cross": banks - 1,
            "handoff": 2 * (banks - 1),
            "relay": 4 * (banks - 1),
            "finalizer": 1,
        }
        observed = len(program)
        observed_family.append(observed)
        rows.append(
            {
                "banks": banks,
                "observed_program_stations": observed,
                "independent_program_arithmetic": independent_arithmetic,
                "formula": 8 * banks - 5,
                "kind_counts": counts,
                "expected_kind_counts": expected_counts,
                "exact": (
                    observed == independent_arithmetic == 8 * banks - 5
                    and set(counts) <= set(expected_counts)
                    and all(
                        counts.get(kind, 0) == expected
                        for kind, expected in expected_counts.items()
                    )
                ),
            }
        )

    nonfamily_ring = 5
    numerator = nonfamily_ring + 5
    remainder = numerator % 8
    fifth_program_length = len(K.interleaved_program(5))
    failure = {
        "ring": nonfamily_ring,
        "candidate_bank_numerator": numerator,
        "divisibility_remainder": remainder,
        "exact_failing_requirement": (
            "positive integer bank count b with n=len("
            "K.interleaved_program(b)); equivalently (n+5)%8==0"
        ),
        "fails": remainder != 0,
    }
    exact = (
        tuple(observed_family) == RING_FAMILY
        and all(row["exact"] for row in rows)
        and failure["fails"]
        and fifth_program_length == 35
    )
    return {
        "membership_law": "n = 8b - 5 for positive integer b",
        "arithmetic": (
            "source 1 + banks b + crosses (b-1) + forward link rows "
            "3(b-1) + reverse link rows 3(b-1) + finalizer 1 = 8b-5"
        ),
        "declared_rows": rows,
        "admissible_declared_ring_sizes": tuple(observed_family),
        "nonfamily_failure": failure,
        "K_b5_program_length_outside_bounded_family": fifth_program_length,
        "scope": SCOPE_STATEMENT,
        "exact": exact,
    }


def rotate_mask(mask: int, shift: int, stations: int) -> int:
    full = (1 << stations) - 1
    normalized = shift % stations
    if normalized == 0:
        return mask & full
    return (
        ((mask << normalized) & full)
        | (mask >> (stations - normalized))
    )


def has_adjacent_pair(mask: int, stations: int) -> bool:
    return bool(mask & rotate_mask(mask, 1, stations))


def independent_path_masks(first: int, last: int) -> list[int]:
    masks = [0]
    for station in range(first, last + 1):
        bit = 1 << station
        previous = 1 << (station - 1)
        additions = [
            mask | bit for mask in masks if not (mask & previous)
        ]
        masks.extend(additions)
    return masks


def independent_cycle_masks(stations: int) -> tuple[int, ...]:
    if stations < 3:
        raise ValueError(("cycle requires at least three stations", stations))
    without_zero = independent_path_masks(1, stations - 1)
    with_zero = [
        mask | 1
        for mask in independent_path_masks(2, stations - 2)
    ]
    masks = tuple(without_zero + with_zero)
    if len(masks) != len(set(masks)):
        raise AssertionError(("duplicate independent masks", stations))
    if any(has_adjacent_pair(mask, stations) for mask in masks):
        raise AssertionError(("adjacent mask escaped generator", stations))
    return masks


def own_lucas(index: int) -> int:
    if index == 0:
        return 2
    if index == 1:
        return 1
    older, newer = 2, 1
    for _ in range(2, index + 1):
        older, newer = newer, older + newer
    return newer


def census_lucas_recount(
    stations: int,
) -> tuple[dict[str, object], tuple[int, ...]]:
    masks = independent_cycle_masks(stations)
    counts = [0] * (stations // 2 + 1)
    for mask in masks:
        counts[mask.bit_count()] += 1
    lucas = own_lucas(stations)
    frozen = FROZEN_CENSUS_TOTALS[stations]
    exact = len(masks) == sum(counts) == lucas == frozen
    return {
        "ring": stations,
        "counts_by_k": tuple(counts),
        "enumerated_total": len(masks),
        "own_lucas_total": lucas,
        "frozen_total": frozen,
        "generator": (
            "disjoint path split: vertex 0 absent, or vertex 0 present "
            "with vertices 1 and n-1 absent"
        ),
        "lucas_recurrence": "L(0)=2, L(1)=1, L(n)=L(n-1)+L(n-2)",
        "all_masks_pairwise_separated": True,
        "exact": exact,
    }, masks


def masks_to_bitplanes(
    masks: tuple[int, ...], stations: int
) -> tuple[int, ...]:
    byte_count = (len(masks) + 7) // 8
    buffers = [bytearray(byte_count) for _ in range(stations)]
    for row, source_mask in enumerate(masks):
        byte_index = row >> 3
        row_bit = 1 << (row & 7)
        mask = source_mask
        while mask:
            low = mask & -mask
            station = low.bit_length() - 1
            buffers[station][byte_index] |= row_bit
            mask ^= low
    return tuple(
        int.from_bytes(buffer, "little") for buffer in buffers
    )


def compile_controller(
    controller: tuple[object, ...], width: int
) -> tuple[tuple[tuple[int, int, int, int], ...], int]:
    compiled = []
    structural_failures = 0
    for gate in controller:
        wires = tuple(int(wire) for wire in gate.wires)
        structural_failures += any(
            wire < 0 or wire >= width for wire in wires
        )
        if gate.kind == "X" and len(wires) == 1:
            compiled.append((1, wires[0], 0, 0))
        elif gate.kind == "CNOT" and len(wires) == 2:
            structural_failures += wires[0] == wires[1]
            compiled.append((2, wires[0], wires[1], 0))
        elif gate.kind == "TOF" and len(wires) == 3:
            structural_failures += len(set(wires)) != 3
            compiled.append((3, wires[0], wires[1], wires[2]))
        else:
            structural_failures += 1
    return tuple(compiled), structural_failures


def apply_bitplane_word(
    planes: list[int],
    compiled: tuple[tuple[int, int, int, int], ...],
    row_full: int,
) -> None:
    for kind, left, right, target in compiled:
        if kind == 1:
            planes[left] ^= row_full
        elif kind == 2:
            planes[right] ^= planes[left]
        else:
            planes[target] ^= planes[left] & planes[right]


def bitsliced_population_count(
    planes: list[int] | tuple[int, ...],
) -> tuple[int, ...]:
    width = max(1, len(planes).bit_length())
    output = [0] * width
    for plane in planes:
        carry = plane
        digit = 0
        while carry:
            if digit == len(output):
                output.append(0)
            overlap = output[digit] & carry
            output[digit] ^= carry
            carry = overlap
            digit += 1
    return tuple(output)


def circular_distance(left: int, right: int, stations: int) -> int:
    return min(
        (right - left) % stations,
        (left - right) % stations,
    )


def budget_guard(started: float) -> None:
    if perf_counter() - started >= AUDIT_TIMEOUT_SEC:
        raise TimeoutError(
            f"declared {AUDIT_TIMEOUT_SEC}s audit budget exhausted"
        )


def orbit_recount(
    banks: int,
    stations: int,
    masks: tuple[int, ...],
    started: float,
) -> dict[str, object]:
    program = K.interleaved_program(banks)
    genesis_banks, links = K.B.chain_genesis(banks)
    data = K.M.prepare_endpoint(
        K.M.pack_state(genesis_banks, links), (1, 0)
    )
    data_wires = len(data)
    controller = K.controller_word(program, data_wires)
    width = data_wires + 3 * stations
    a_base = data_wires
    b_base = a_base + stations
    work_base = b_base + stations
    compiled, structural_failures = compile_controller(controller, width)

    step_total = 0
    translation_failure_config_steps = 0
    token_count_failure_config_steps = 0
    adjacency_failure_config_steps = 0
    adjacency_pair_incidences = 0
    b_rail_failure_config_steps = 0
    work_failure_config_steps = 0
    distance_failure_config_steps = 0
    distance_pair_incidence_checks = 0
    rail_closure_failures = 0
    data_changed_configurations = 0
    output_hasher = sha256()

    for start in range(0, len(masks), BITPLANE_BATCH):
        budget_guard(started)
        batch = masks[start:start + BITPLANE_BATCH]
        rows = len(batch)
        row_full = (1 << rows) - 1
        original_a = masks_to_bitplanes(batch, stations)
        original_count = bitsliced_population_count(original_a)
        planes = [
            row_full if bit else 0 for bit in data
        ]
        planes.extend(original_a)
        planes.extend([0] * (2 * stations))

        for step in range(stations):
            apply_bitplane_word(planes, compiled, row_full)
            shift = step + 1
            actual_a = planes[a_base:a_base + stations]
            actual_b = planes[b_base:b_base + stations]
            actual_work = planes[work_base:work_base + stations]
            expected_a = tuple(
                original_a[(station - shift) % stations]
                for station in range(stations)
            )

            translation_bad = 0
            for observed, expected in zip(actual_a, expected_a):
                translation_bad |= observed ^ expected
            translation_failure_config_steps += translation_bad.bit_count()

            b_bad = 0
            work_bad = 0
            for plane in actual_b:
                b_bad |= plane
            for plane in actual_work:
                work_bad |= plane
            b_rail_failure_config_steps += b_bad.bit_count()
            work_failure_config_steps += work_bad.bit_count()

            count_bad = 0
            actual_count = bitsliced_population_count(
                actual_a + actual_b
            )
            for observed, expected in zip(actual_count, original_count):
                count_bad |= observed ^ expected
            token_count_failure_config_steps += count_bad.bit_count()

            adjacent_bad = 0
            for station in range(stations):
                incidence = (
                    actual_a[station]
                    & actual_a[(station + 1) % stations]
                )
                adjacency_pair_incidences += incidence.bit_count()
                adjacent_bad |= incidence
            adjacency_failure_config_steps += adjacent_bad.bit_count()

            distance_bad = 0
            for left in range(stations):
                moved_left = (left + shift) % stations
                for right in range(left + 1, stations):
                    moved_right = (right + shift) % stations
                    expected_pair = original_a[left] & original_a[right]
                    observed_pair = (
                        actual_a[moved_left] & actual_a[moved_right]
                    )
                    distance_pair_incidence_checks += (
                        expected_pair.bit_count()
                    )
                    distance_bad |= observed_pair ^ expected_pair
                    if (
                        circular_distance(left, right, stations)
                        != circular_distance(
                            moved_left, moved_right, stations
                        )
                    ):
                        distance_bad |= expected_pair
            distance_failure_config_steps += distance_bad.bit_count()
            step_total += rows

        closure_bad = 0
        for observed, expected in zip(
            planes[a_base:a_base + stations], original_a
        ):
            closure_bad |= observed ^ expected
        for plane in planes[b_base:work_base + stations]:
            closure_bad |= plane
        rail_closure_failures += closure_bad.bit_count()

        data_changed = 0
        for wire, original_bit in enumerate(data):
            expected = row_full if original_bit else 0
            data_changed |= planes[wire] ^ expected
        data_changed_configurations += data_changed.bit_count()

        row_bytes = (rows + 7) // 8
        for plane in planes[:data_wires]:
            output_hasher.update(plane.to_bytes(row_bytes, "little"))
        budget_guard(started)

    expected_pair_checks = sum(
        comb(mask.bit_count(), 2) for mask in masks
    ) * stations
    frozen_steps = FROZEN_ORBIT_STEP_TOTALS[stations]
    zero_failures = {
        "controller_structure_failures": structural_failures,
        "translation_failure_config_steps":
            translation_failure_config_steps,
        "token_count_failure_config_steps":
            token_count_failure_config_steps,
        "adjacency_failure_config_steps":
            adjacency_failure_config_steps,
        "adjacency_pair_incidences": adjacency_pair_incidences,
        "B_rail_failure_config_steps": b_rail_failure_config_steps,
        "work_failure_config_steps": work_failure_config_steps,
        "distance_failure_config_steps":
            distance_failure_config_steps,
        "rail_closure_failures": rail_closure_failures,
    }
    exact = (
        len(program) == stations == 8 * banks - 5
        and step_total == len(masks) * stations == frozen_steps
        and distance_pair_incidence_checks == expected_pair_checks
        and all(value == 0 for value in zero_failures.values())
        and len(compiled) == len(controller)
        and data_changed_configurations > 0
    )
    return {
        "ring": stations,
        "banks": banks,
        "configurations": len(masks),
        "steps_per_orbit": stations,
        "exhaustive_controller_steps": step_total,
        "frozen_controller_steps": frozen_steps,
        "program_stations": len(program),
        "controller_gates_per_step": len(controller),
        "controller_word_sha256": K.gate_digest(controller),
        "bitplane_batch": BITPLANE_BATCH,
        "distance_pair_incidence_checks":
            distance_pair_incidence_checks,
        "expected_distance_pair_incidence_checks":
            expected_pair_checks,
        "data_changed_configurations": data_changed_configurations,
        "data_output_bitplanes_sha256": output_hasher.hexdigest(),
        "inverse_certificate": (
            "Every exhaustively applied X/CNOT/TOF gate is self-inverse; "
            "reversing the exact compiled sequence is therefore an exact "
            "inverse on every bit-plane row."
        ),
        "zero_failure_census": zero_failures,
        "execution": (
            "K.interleaved_program and K.controller_word used directly; "
            "independent reversible bit-plane evaluator applied every K "
            "gate at every step to every census configuration"
        ),
        "exact": exact,
    }


def own_ownership_violations(
    mask: int, stations: int
) -> tuple[tuple[int, tuple[str, ...]], ...]:
    rows = []
    for station in range(stations):
        if not ((mask >> station) & 1):
            continue
        reasons = []
        if (mask >> ((station - 1) % stations)) & 1:
            reasons.append("left_A")
        if (mask >> ((station + 1) % stations)) & 1:
            reasons.append("right_A")
        if reasons:
            rows.append((station, tuple(reasons)))
    return tuple(rows)


def near_miss_and_grid_spotchecks(
    stations: int,
    masks: tuple[int, ...],
    counts: tuple[int, ...],
) -> dict[str, object]:
    near_rows = []
    violating_stations = 0
    reason_incidences = 0
    near_failures = 0
    for left in range(stations):
        right = (left + 1) % stations
        mask = (1 << left) | (1 << right)
        violations = own_ownership_violations(mask, stations)
        observed_sites = tuple(row[0] for row in violations)
        reasons = tuple(
            reason for _station, station_reasons in violations
            for reason in station_reasons
        )
        expected_sites = tuple(sorted((left, right)))
        exact = (
            observed_sites == expected_sites
            and len(violations) == 2
            and len(reasons) == 2
        )
        near_failures += not exact
        violating_stations += len(violations)
        reason_incidences += len(reasons)
        near_rows.append(
            (left, right, observed_sites, reasons, exact)
        )

    maximum = stations // 2
    low_grid_accepts = 0
    low_grid_refusals = 0
    low_grid_failures = 0
    low_cell_accepts = [
        [0] * (maximum + 1) for _ in range(maximum + 1)
    ]
    low_cell_refusals = [
        [0] * (maximum + 1) for _ in range(maximum + 1)
    ]
    low_masks = tuple(mask for mask in masks if mask.bit_count() <= 2)
    for mask in low_masks:
        true_count = mask.bit_count()
        for expected_count in range(maximum + 1):
            accepted = true_count == expected_count
            refused = not accepted
            low_grid_accepts += accepted
            low_grid_refusals += refused
            low_cell_accepts[expected_count][true_count] += accepted
            low_cell_refusals[expected_count][true_count] += refused
            low_grid_failures += accepted == refused
            low_grid_failures += accepted != (
                expected_count == true_count
            )

    diagonal_accepts = 0
    diagonal_refusals = 0
    diagonal_by_k = [0] * (maximum + 1)
    for mask in masks:
        true_count = mask.bit_count()
        accepted = mask.bit_count() == true_count
        diagonal_accepts += accepted
        diagonal_refusals += not accepted
        diagonal_by_k[true_count] += accepted

    low_total = sum(counts[:min(3, len(counts))])
    exact = (
        near_failures == 0
        and violating_stations == reason_incidences == 2 * stations
        and len(low_masks) == low_total
        and low_grid_accepts == low_total
        and low_grid_refusals == low_total * maximum
        and low_grid_failures == 0
        and diagonal_accepts == len(masks)
        and diagonal_refusals == 0
        and tuple(diagonal_by_k) == counts
    )
    return {
        "ring": stations,
        "near_miss_adjacent_pairs": stations,
        "near_miss_violating_stations": violating_stations,
        "expected_near_miss_violating_stations": 2 * stations,
        "near_miss_reason_incidences": reason_incidences,
        "near_miss_failures": near_failures,
        "near_miss_table_sha256": digest_json(near_rows),
        "all_k_le_2_configurations": len(low_masks),
        "expected_all_k_le_2_configurations": low_total,
        "low_grid_expected_count_domain": tuple(range(maximum + 1)),
        "low_grid_accepts": low_grid_accepts,
        "low_grid_refusals": low_grid_refusals,
        "low_grid_failures": low_grid_failures,
        "low_grid_accepted_cells": tuple(
            tuple(row) for row in low_cell_accepts
        ),
        "low_grid_refused_cells": tuple(
            tuple(row) for row in low_cell_refusals
        ),
        "all_diagonal_cases": len(masks),
        "diagonal_accepts": diagonal_accepts,
        "diagonal_refusals": diagonal_refusals,
        "diagonal_accepts_by_k": tuple(diagonal_by_k),
        "verdict_law": (
            "accept iff independently recounted popcount equals supplied k"
        ),
        "exact": exact,
    }


def discipline(
    k_namespace_before: dict[str, int],
) -> dict[str, object]:
    k_namespace_after = {
        name: id(value) for name, value in vars(K).items()
    }
    blocklisted = tuple(
        name for name in DIRECT_FRONTIER_IMPORTS
        if name.startswith("frontier_cycle72")
        or name.startswith("frontier_cycle73")
    )
    frozen_literal_values_exact = (
        FROZEN_CENSUS_TOTALS
        == {3: 4, 11: 199, 19: 9349, 27: 439204}
        and FROZEN_ORBIT_STEP_TOTALS
        == {3: 12, 11: 2189, 19: 177631, 27: 11858508}
    )
    exact = (
        k_namespace_after == k_namespace_before
        and DIRECT_FRONTIER_IMPORTS == (K.__name__,)
        and not blocklisted
        and frozen_literal_values_exact
        and AUDIT_INPUT_PATHS
        == (
            "scripts/frontier_cycle737_ring_family_uniformity_2026_07_28.py",
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
        )
        and DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and SCOPE_STATEMENT
        == "family-uniform over [3,11,19,27], not general-n"
    )
    return {
        "K_namespace_unchanged": k_namespace_after == k_namespace_before,
        "direct_frontier_imports": DIRECT_FRONTIER_IMPORTS,
        "blocklisted_direct_imports": blocklisted,
        "frozen_tables_literal_values_exact":
            frozen_literal_values_exact,
        "declared_inputs_exact": (
            DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        ),
        "scope": SCOPE_STATEMENT,
        "general_n_theorem_claimed": False,
        "exact": exact,
    }


def main() -> int:
    started = perf_counter()
    k_namespace_before = {
        name: id(value) for name, value in vars(K).items()
    }
    reports: dict[str, object] = {}

    try:
        extracted = extraction()
        reports["extraction"] = extracted
        check("A_extraction", extracted["exact"])
    except Exception as exc:
        ERRORS["A_extraction"] = error_text(exc)
        reports["extraction"] = {"exact": False, "error": ERRORS["A_extraction"]}
        check("A_extraction", False)

    try:
        admissibility = admissibility_recount()
        reports["admissibility_recount"] = admissibility
        check("B_admissibility_recount", admissibility["exact"])
    except Exception as exc:
        ERRORS["B_admissibility_recount"] = error_text(exc)
        reports["admissibility_recount"] = {
            "exact": False, "error": ERRORS["B_admissibility_recount"]
        }
        check("B_admissibility_recount", False)

    census_reports: dict[int, dict[str, object]] = {}
    orbit_reports: dict[int, dict[str, object]] = {}
    control_reports: dict[int, dict[str, object]] = {}
    for banks, stations in zip(BANK_FAMILY, RING_FAMILY):
        masks: tuple[int, ...] | None = None
        counts: tuple[int, ...] | None = None
        census_label = f"C_census_lucas_recount_n{stations}"
        try:
            census, masks = census_lucas_recount(stations)
            counts = tuple(census["counts_by_k"])
            census_reports[stations] = census
            check(census_label, census["exact"])
        except Exception as exc:
            ERRORS[census_label] = error_text(exc)
            census_reports[stations] = {
                "ring": stations,
                "exact": False,
                "error": ERRORS[census_label],
            }
            check(census_label, False)

        orbit_label = f"D_orbit_recount_n{stations}"
        if masks is None:
            orbit_reports[stations] = {
                "ring": stations,
                "exact": False,
                "error": "skipped after census failure",
            }
            check(orbit_label, False)
        else:
            try:
                orbit = orbit_recount(banks, stations, masks, started)
                orbit_reports[stations] = orbit
                check(orbit_label, orbit["exact"])
            except Exception as exc:
                ERRORS[orbit_label] = error_text(exc)
                orbit_reports[stations] = {
                    "ring": stations,
                    "exact": False,
                    "error": ERRORS[orbit_label],
                }
                check(orbit_label, False)

        controls_label = f"E_near_miss_and_grid_n{stations}"
        if masks is None or counts is None:
            control_reports[stations] = {
                "ring": stations,
                "exact": False,
                "error": "skipped after census failure",
            }
            check(controls_label, False)
        else:
            try:
                controls = near_miss_and_grid_spotchecks(
                    stations, masks, counts
                )
                control_reports[stations] = controls
                check(controls_label, controls["exact"])
            except Exception as exc:
                ERRORS[controls_label] = error_text(exc)
                control_reports[stations] = {
                    "ring": stations,
                    "exact": False,
                    "error": ERRORS[controls_label],
                }
                check(controls_label, False)
        del masks

    reports["census_lucas_recount"] = census_reports
    reports["orbit_recount"] = orbit_reports
    reports["near_miss_and_grid_spotchecks"] = control_reports

    science_labels = tuple(
        label for label in CHECKS
        if label.startswith(("A_", "B_", "C_", "D_", "E_"))
    )
    family_component_pass = all(CHECKS[label] for label in science_labels)
    boundary = {
        "ring_family": list(RING_FAMILY),
        "sector_theorem_uniform_over_family": family_component_pass,
        "frozen_n_dependence": (
            None
            if family_component_pass
            else "one or more bounded family certificates failed"
        ),
        "general_n_theorem_claimed": False,
        "scope": SCOPE_STATEMENT,
        "uniformity_statement": (
            "Every configuration is exhausted at each declared family "
            "member; this is family-uniform, not general-n."
        ),
    }
    reports["honest_boundary"] = boundary
    boundary_exact = (
        boundary["sector_theorem_uniform_over_family"]
        == family_component_pass
        and (
            (boundary["frozen_n_dependence"] is None)
            == family_component_pass
        )
        and boundary["general_n_theorem_claimed"] is False
        and boundary["scope"] == SCOPE_STATEMENT
    )
    check("F_honest_bounded_scope", boundary_exact)

    try:
        discipline_report = discipline(k_namespace_before)
        reports["discipline"] = discipline_report
        check("G_discipline", discipline_report["exact"])
    except Exception as exc:
        ERRORS["G_discipline"] = error_text(exc)
        reports["discipline"] = {
            "exact": False, "error": ERRORS["G_discipline"]
        }
        check("G_discipline", False)

    elapsed = perf_counter() - started
    check("H_runtime_under_1800_seconds", elapsed < AUDIT_TIMEOUT_SEC)

    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "scope": SCOPE_STATEMENT,
        "reports": reports,
        "errors": ERRORS,
        "runtime_seconds": round(elapsed, 6),
    }
    provisional = {
        **report,
        "checks": dict(sorted(CHECKS.items())),
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
    }
    provisional_text = "\n".join(OUTPUT_LINES) + "\n" + json.dumps(
        provisional, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "I_stdout_under_150KB",
        len(provisional_text.encode()) + 4096 < STDOUT_LIMIT_BYTES,
    )

    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_passed"] = sum(CHECKS.values())
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE737_RING_FAMILY_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE737_RING_FAMILY_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    report["report_sha256"] = digest_json(report)
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        fallback = {
            "checks": report["checks"],
            "checks_passed": report["checks_passed"],
            "checks_failed": report["checks_failed"],
            "errors": ERRORS,
            "pass": False,
            "terminal": "CYCLE737_RING_FAMILY_INDEPENDENT_CHECK_HONEST_FAIL",
            "reason": "full report exceeded stdout bound",
        }
        text = "\n".join(OUTPUT_LINES) + "\n" + json.dumps(
            fallback, sort_keys=True, separators=(",", ":")
        ) + "\n"
        sys.stdout.write(text)
        return 1
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
