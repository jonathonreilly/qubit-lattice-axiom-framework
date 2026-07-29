#!/usr/bin/env python3
"""Independent bounded checker for Cycle 734 paired excitation.

Cycle 734 is parsed as inert data.  The Cycle 719 controller core is the only
project module imported, and every recount below is implemented locally.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/PAIRED_EXCITATION_GENESIS_CYCLE734_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle734_paired_excitation_genesis_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Any

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


STDOUT_LIMIT_BYTES = 150 * 1024
EXPECTED_PAIR_TEMPLATE = (
    ("a_base", 0),
    ("a_base", 1),
    ("ref_base", 1),
)
EXPECTED_ADJACENT_CONVENTION = (
    "positive-oriented pair (position, position+1 mod 11), "
    "with reference segment at position+1 and h=0"
)
EXPECTED_DECLARED_LAW = (
    "A_count=2 AND popcount(A) mod 2=h in the B=0,h=0 sector"
)
EXPECTED_GENESIS_AUDIT_INPUTS = (
    "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
EXPECTED_REFUSED_COUNTS = (0, 1, 3, 4)
EXPECTED_OBSTRUCTION_NAME = "ownership_uniqueness_at_adjacent_Q_sites"
EXPECTED_OBSTRUCTION_INVARIANT = (
    "an occupied A station requires own B/work and both neighboring "
    "A/B rails blank at the Q boundary"
)
EXPECTED_MINIMAL_WITNESS = (
    ("ring_stations", 11),
    ("A_count", 2),
    ("A_sites", (0, 1)),
    ("B_count", 0),
    ("work_count", 0),
    ("single_token_control_violations", 0),
)
EXPECTED_W2_REMAINING_COMPONENTS = (
    "finite oriented geometry",
    "program content/order",
    "passive-only covariance",
)
EXPECTED_CLAIM_SCOPE = (
    "translation-covariant preparation and expected_count=2 enforcement "
    "on the held ring-11 register; the adjacent-pair controller wall is "
    "frozen, not solved"
)
BLOCKLISTED_CYCLES = (734, 732, 731, 730, 724)
K_ATTRIBUTE_BASELINE = tuple(
    sorted((name, id(value)) for name, value in vars(K).items())
)


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function census", name, len(matches)))
    return matches[0]


def _assignment_value(scope: ast.Module | ast.FunctionDef, name: str) -> ast.expr:
    matches: list[ast.expr] = []
    for node in scope.body:
        if isinstance(node, ast.Assign):
            if any(
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


def _return_dict(function: ast.FunctionDef) -> ast.Dict:
    matches = [
        node.value
        for node in function.body
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    if len(matches) != 1:
        raise AssertionError(("return dict census", function.name, len(matches)))
    return matches[0]


def _dict_items(node: ast.Dict) -> dict[str, ast.expr]:
    output: dict[str, ast.expr] = {}
    for key_node, value_node in zip(node.keys, node.values):
        if key_node is None:
            raise AssertionError("dictionary unpacking is outside the audit grammar")
        key = ast.literal_eval(key_node)
        if not isinstance(key, str) or key in output:
            raise AssertionError(("non-string or duplicate dictionary key", key))
        output[key] = value_node
    return output


def _qualified_name(node: ast.expr) -> str:
    parts: list[str] = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if not isinstance(node, ast.Name):
        raise AssertionError("non-name attribute root")
    parts.append(node.id)
    return ".".join(reversed(parts))


def _layout_key(node: ast.expr) -> str:
    if not (
        isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id == "layout"
    ):
        raise AssertionError(("not a layout subscript", ast.dump(node)))
    key = ast.literal_eval(node.slice)
    if not isinstance(key, str):
        raise AssertionError(("non-string layout key", key))
    return key


def _position_offset(node: ast.expr) -> int:
    if not (
        isinstance(node, ast.BinOp)
        and isinstance(node.op, ast.Mod)
        and isinstance(node.right, ast.Name)
        and node.right.id == "stations"
    ):
        raise AssertionError(("non-modular position expression", ast.dump(node)))
    numerator = node.left
    if isinstance(numerator, ast.Name) and numerator.id == "position":
        return 0
    if (
        isinstance(numerator, ast.BinOp)
        and isinstance(numerator.op, ast.Add)
        and isinstance(numerator.left, ast.Name)
        and numerator.left.id == "position"
    ):
        offset = ast.literal_eval(numerator.right)
        if isinstance(offset, int) and not isinstance(offset, bool):
            return offset
    raise AssertionError(("unsupported position numerator", ast.dump(numerator)))


def _extract_pair_template(function: ast.FunctionDef) -> tuple[tuple[str, int], ...]:
    returns = [
        node
        for node in function.body
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Tuple)
    ]
    if len(returns) != 1:
        raise AssertionError(("pair return census", len(returns)))
    descriptors: list[tuple[str, int]] = []
    for gate in returns[0].value.elts:
        if not (
            isinstance(gate, ast.Call)
            and _qualified_name(gate.func) == "K.A.x"
            and len(gate.args) == 1
            and not gate.keywords
        ):
            raise AssertionError(("pair gate is not a unary K.A.x", ast.dump(gate)))
        wire = gate.args[0]
        if not (
            isinstance(wire, ast.BinOp)
            and isinstance(wire.op, ast.Add)
        ):
            raise AssertionError(("pair wire grammar", ast.dump(wire)))
        descriptors.append((_layout_key(wire.left), _position_offset(wire.right)))
    return tuple(descriptors)


def _static_int(node: ast.expr, names: dict[str, int]) -> int:
    if (
        isinstance(node, ast.Constant)
        and isinstance(node.value, int)
        and not isinstance(node.value, bool)
    ):
        return node.value
    if isinstance(node, ast.Name) and node.id in names:
        return names[node.id]
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
        return _static_int(node.left, names) ** _static_int(node.right, names)
    raise AssertionError(("unsupported static integer expression", ast.dump(node)))


def _subscript_path(node: ast.expr) -> tuple[str, tuple[str, ...]] | None:
    keys: list[str] = []
    while isinstance(node, ast.Subscript):
        try:
            key = ast.literal_eval(node.slice)
        except (ValueError, TypeError):
            return None
        if not isinstance(key, str):
            return None
        keys.append(key)
        node = node.value
    if not isinstance(node, ast.Name):
        return None
    return node.id, tuple(reversed(keys))


def _comparison_literals(
    expression: ast.expr, root: str
) -> dict[tuple[str, ...], object]:
    output: dict[tuple[str, ...], object] = {}
    for node in ast.walk(expression):
        if not (
            isinstance(node, ast.Compare)
            and len(node.ops) == 1
            and len(node.comparators) == 1
        ):
            continue
        path = _subscript_path(node.left)
        if path is None or path[0] != root:
            continue
        try:
            value = ast.literal_eval(node.comparators[0])
        except (ValueError, TypeError):
            continue
        output[path[1]] = value
    return output


def _find_boundary_true(function: ast.FunctionDef, key: str) -> bool:
    for node in ast.walk(function):
        if not (
            isinstance(node, ast.Compare)
            and len(node.ops) == 1
            and isinstance(node.ops[0], ast.Is)
            and len(node.comparators) == 1
        ):
            continue
        if _subscript_path(node.left) != ("boundary", (key,)):
            continue
        if ast.literal_eval(node.comparators[0]) is True:
            return True
    return False


def extraction() -> tuple[dict[str, object], dict[str, object]]:
    """Extract only frozen syntax/data from Cycle 734; never execute it."""

    source = Path(AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=AUDIT_INPUT_PATHS[0])
    module_literals = {
        name: ast.literal_eval(_assignment_value(tree, name))
        for name in (
            "AUDIT_INPUT_PATHS",
            "RING_STATIONS",
            "EXPECTED_COUNT",
            "EXPECTED_PAIR_GATES",
            "FIXTURE_BANKS",
        )
    }
    ring = module_literals["RING_STATIONS"]
    if not isinstance(ring, int) or isinstance(ring, bool):
        raise AssertionError(("non-integer ring census", ring))

    pair_function = _function(tree, "pair_creation_word")
    pair_template = _extract_pair_template(pair_function)
    pair_exactness_items = _dict_items(
        _return_dict(_function(tree, "pair_word_exactness_certificate"))
    )
    adjacent_convention = ast.literal_eval(
        pair_exactness_items["adjacent_pair_convention"]
    )

    covariance_items = _dict_items(
        _return_dict(_function(tree, "translation_covariance_certificate"))
    )
    covariance_count = _static_int(
        covariance_items["expected_identities"],
        {"RING_STATIONS": ring},
    )

    count_function = _function(tree, "count2_enforcement_certificate")
    refused_counts = ast.literal_eval(
        _assignment_value(count_function, "witness_counts")
    )
    count_return_items = _dict_items(_return_dict(count_function))
    accepted_key_present = "all_11_lawful_pairs_accepted" in count_return_items
    refused_key_present = (
        "all_0_1_3_4_count_witnesses_refused" in count_return_items
    )
    law_items = _dict_items(
        _return_dict(_function(tree, "h0_b0_theorem_recount"))
    )
    declared_law = ast.literal_eval(law_items["full_law"])
    exhaustive_count2 = ast.literal_eval(
        law_items["expected_full_pass_cases"]
    )

    controller_function = _function(tree, "controller_two_token_probe")
    frozen_node = _assignment_value(controller_function, "frozen")
    if not isinstance(frozen_node, ast.Dict):
        raise AssertionError("frozen obstruction is not a dictionary literal")
    frozen_items = _dict_items(frozen_node)
    obstruction_name = ast.literal_eval(frozen_items["name"])
    obstruction_invariant = ast.literal_eval(frozen_items["invariant"])
    minimal_node = frozen_items["minimal_reproducing_census"]
    if not isinstance(minimal_node, ast.Dict):
        raise AssertionError("minimal witness is not a dictionary literal")
    minimal_items = _dict_items(minimal_node)
    exact_comparisons = _comparison_literals(
        _assignment_value(controller_function, "frozen_exact"), "frozen"
    )
    first_step = exact_comparisons[("first_step",)]
    first_stations = exact_comparisons[("first_stations",)]
    minimal_witness = (
        ("ring_stations", ring),
        (
            "A_count",
            exact_comparisons[("minimal_reproducing_census", "A_count")],
        ),
        (
            "A_sites",
            exact_comparisons[("minimal_reproducing_census", "A_sites")],
        ),
        (
            "B_count",
            exact_comparisons[("minimal_reproducing_census", "B_count")],
        ),
        ("work_count", ast.literal_eval(minimal_items["work_count"])),
        (
            "single_token_control_violations",
            exact_comparisons[
                (
                    "minimal_reproducing_census",
                    "single_token_control_violations",
                )
            ],
        ),
    )
    controller_return = _dict_items(_return_dict(controller_function))
    controller_lawful = ast.literal_eval(
        controller_return["controller_two_token_lawful"]
    )

    main_function = _function(tree, "main")
    w2_remaining = tuple(
        ast.literal_eval(
            _assignment_value(main_function, "w2_remaining_components")
        )
    )
    boundary_node = _assignment_value(main_function, "boundary")
    if not isinstance(boundary_node, ast.Dict):
        raise AssertionError("boundary is not a dictionary literal")
    boundary_items = _dict_items(boundary_node)
    claim_scope = ast.literal_eval(boundary_items["claim_scope"])
    controller_boundary_node = _assignment_value(
        main_function, "controller_boundary"
    )
    if not isinstance(controller_boundary_node, ast.Dict):
        raise AssertionError("controller boundary is not a dictionary literal")
    controller_boundary_lawful = ast.literal_eval(
        _dict_items(controller_boundary_node)["lawful"]
    )
    source_boundary_expected = _find_boundary_true(
        main_function, "source_boundary_retired_for_preparation"
    )

    public = {
        "pair_template": pair_template,
        "adjacent_pair_convention": adjacent_convention,
        "covariance_identity_census": covariance_count,
        "accepted_adjacent_pair_census": ring if accepted_key_present else -1,
        "refused_count_census": refused_counts,
        "declared_count_parity_law": declared_law,
        "exhaustive_count2_census": exhaustive_count2,
        "obstruction_name": obstruction_name,
        "obstruction_invariant": obstruction_invariant,
        "first_step": first_step,
        "first_stations": first_stations,
        "minimal_witness": minimal_witness,
        "source_boundary_retired_for_preparation": source_boundary_expected,
        "controller_two_token_lawful": controller_lawful,
        "w2_remaining_components": w2_remaining,
        "claim_scope": claim_scope,
        "genesis_AUDIT_INPUT_PATHS_literal": module_literals[
            "AUDIT_INPUT_PATHS"
        ],
    }
    passed = (
        module_literals["AUDIT_INPUT_PATHS"] == EXPECTED_GENESIS_AUDIT_INPUTS
        and module_literals["EXPECTED_COUNT"] == 2
        and module_literals["EXPECTED_PAIR_GATES"] == 3
        and module_literals["FIXTURE_BANKS"] == 2
        and pair_template == EXPECTED_PAIR_TEMPLATE
        and adjacent_convention == EXPECTED_ADJACENT_CONVENTION
        and covariance_count == 121
        and public["accepted_adjacent_pair_census"] == 11
        and refused_key_present
        and refused_counts == EXPECTED_REFUSED_COUNTS
        and declared_law == EXPECTED_DECLARED_LAW
        and exhaustive_count2 == 55
        and obstruction_name == EXPECTED_OBSTRUCTION_NAME
        and obstruction_invariant == EXPECTED_OBSTRUCTION_INVARIANT
        and first_step == 0
        and first_stations == (0, 1)
        and minimal_witness == EXPECTED_MINIMAL_WITNESS
        and source_boundary_expected is True
        and controller_lawful is False
        and controller_boundary_lawful is False
        and w2_remaining == EXPECTED_W2_REMAINING_COMPONENTS
        and claim_scope == EXPECTED_CLAIM_SCOPE
    )
    public["pass"] = passed
    internal = {
        "ring_stations": ring,
        "expected_count": module_literals["EXPECTED_COUNT"],
        "fixture_banks": module_literals["FIXTURE_BANKS"],
        "pair_template": pair_template,
        "refused_counts": refused_counts,
        "obstruction_name": obstruction_name,
        "obstruction_invariant": obstruction_invariant,
        "first_step": first_step,
        "first_stations": first_stations,
        "minimal_witness": minimal_witness,
        "w2_remaining_components": w2_remaining,
        "claim_scope": claim_scope,
    }
    return public, internal


def _pair_word(
    template: tuple[tuple[str, int], ...],
    layout: dict[str, int],
    position: int,
) -> tuple[tuple[str, int], ...]:
    stations = layout["stations"]
    return tuple(
        ("X", layout[base] + ((position + offset) % stations))
        for base, offset in template
    )


def _apply_x_word(value: int, word: tuple[tuple[str, int], ...]) -> int:
    output = value
    for kind, wire in word:
        if kind != "X" or wire < 0:
            raise AssertionError(("unsupported independent gate", kind, wire))
        output ^= 1 << wire
    return output


def _translate_wire(wire: int, layout: dict[str, int], shift: int) -> int:
    stations = layout["stations"]
    for base_name in ("a_base", "b_base", "ref_base"):
        base = layout[base_name]
        if base <= wire < base + stations:
            return base + ((wire - base + shift) % stations)
    return wire


def pair_word_recount(extracted: dict[str, object]) -> dict[str, object]:
    """Independent integer-bit simulator and all 121 covariance identities."""

    stations = int(extracted["ring_stations"])
    template = extracted["pair_template"]
    if not isinstance(template, tuple):
        raise AssertionError("extracted pair template is not frozen")
    layout = {
        "stations": stations,
        "a_base": 0,
        "b_base": stations,
        "ref_base": 2 * stations,
        "h_wire": 3 * stations,
    }
    exact_failures: list[int] = []
    outputs: list[int] = []
    for position in range(stations):
        word = _pair_word(template, layout, position)
        output = _apply_x_word(0, word)
        following = (position + 1) % stations
        expected = (
            (1 << (layout["a_base"] + position))
            | (1 << (layout["a_base"] + following))
            | (1 << (layout["ref_base"] + following))
        )
        mask = (1 << stations) - 1
        a_mask = (output >> layout["a_base"]) & mask
        b_mask = (output >> layout["b_base"]) & mask
        refs_mask = (output >> layout["ref_base"]) & mask
        h = (output >> layout["h_wire"]) & 1
        exact = (
            output == expected
            and a_mask.bit_count() == 2
            and b_mask == 0
            and refs_mask == 1 << following
            and h == 0
        )
        if not exact:
            exact_failures.append(position)
        outputs.append(output)

    covariance_failures: list[tuple[int, int]] = []
    covariance_count = 0
    for position in range(stations):
        source = _pair_word(template, layout, position)
        for shift in range(stations):
            conjugated = tuple(
                (kind, _translate_wire(wire, layout, shift))
                for kind, wire in source
            )
            target = _pair_word(
                template, layout, (position + shift) % stations
            )
            covariance_count += 1
            if conjugated != target:
                covariance_failures.append((position, shift))
    base = _pair_word(template, layout, 0)
    position0_failures = tuple(
        position
        for position in range(stations)
        if tuple(
            (kind, _translate_wire(wire, layout, position))
            for kind, wire in base
        )
        != _pair_word(template, layout, position)
    )
    return {
        "positions_recounted": stations,
        "bit_exact_outputs": len(outputs) - len(exact_failures),
        "bit_exact_failure_positions": tuple(exact_failures),
        "covariance_identities_recounted": covariance_count,
        "covariance_failures": tuple(covariance_failures),
        "position0_conjugation_failures": position0_failures,
        "pass": (
            len(outputs) == 11
            and not exact_failures
            and covariance_count == 121
            and covariance_count
            == int(extracted["ring_stations"]) ** 2
            and not covariance_failures
            and not position0_failures
        ),
    }


def _declared_count_parity_law(
    a_mask: int, b_mask: int, h: int, expected_count: int
) -> tuple[bool, bool, bool]:
    if b_mask != 0 or h not in (0, 1):
        return False, False, False
    count_ok = a_mask.bit_count() == expected_count
    parity_ok = a_mask.bit_count() % 2 == h
    return count_ok, parity_ok, count_ok and parity_ok


def count2_law_recount(extracted: dict[str, object]) -> dict[str, object]:
    """Reimplement the declared count/parity predicate with count fixed at 2."""

    stations = int(extracted["ring_stations"])
    expected_count = int(extracted["expected_count"])
    adjacent_rows = []
    for position in range(stations):
        mask = (1 << position) | (1 << ((position + 1) % stations))
        count_ok, parity_ok, lawful = _declared_count_parity_law(
            mask, 0, 0, expected_count
        )
        adjacent_rows.append(
            (position, mask.bit_count(), count_ok, parity_ok, lawful)
        )

    refused_rows = []
    refused_counts = extracted["refused_counts"]
    if not isinstance(refused_counts, tuple):
        raise AssertionError("refusal census is not a literal tuple")
    for count in refused_counts:
        mask = (1 << int(count)) - 1
        h = int(count) & 1
        count_ok, parity_ok, lawful = _declared_count_parity_law(
            mask, 0, h, expected_count
        )
        refused_rows.append(
            (int(count), h, count_ok, parity_ok, not lawful)
        )

    exhaustive_lawful = tuple(
        mask
        for mask in range(1 << stations)
        if _declared_count_parity_law(
            mask, 0, 0, expected_count
        )[2]
    )
    accepted = tuple(row[0] for row in adjacent_rows if row[-1])
    refused = tuple(row[0] for row in refused_rows if row[-1])
    return {
        "declared_form": EXPECTED_DECLARED_LAW,
        "expected_count": expected_count,
        "adjacent_acceptance_rows": tuple(adjacent_rows),
        "accepted_positions": accepted,
        "refusal_rows": tuple(refused_rows),
        "refused_counts": refused,
        "exhaustive_B0_h0_count2_cases": len(exhaustive_lawful),
        "pass": (
            extracted["ring_stations"] == 11
            and expected_count == 2
            and accepted == tuple(range(11))
            and refused == EXPECTED_REFUSED_COUNTS
            and all(row[3] for row in refused_rows)
            and len(exhaustive_lawful) == 55
        ),
    }


def _occupied(bits: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(index for index, bit in enumerate(bits) if bit)


def _ownership_violations(
    a: tuple[int, ...],
    b: tuple[int, ...],
    work: tuple[int, ...],
) -> tuple[tuple[int, tuple[str, ...]], ...]:
    if not (len(a) == len(b) == len(work)):
        raise AssertionError("rail-length disagreement")
    stations = len(a)
    failures = []
    for station, occupied in enumerate(a):
        if not occupied:
            continue
        left = (station - 1) % stations
        right = (station + 1) % stations
        dirty = (
            ("own_B", b[station]),
            ("own_work", work[station]),
            ("left_A", a[left]),
            ("left_B", b[left]),
            ("right_A", a[right]),
            ("right_B", b[right]),
        )
        reasons = tuple(name for name, bit in dirty if bit)
        if reasons:
            failures.append((station, reasons))
    return tuple(failures)


def obstruction_reproduction(
    extracted: dict[str, object],
) -> dict[str, object]:
    """Use K's public controller calls and independently test its Q boundary."""

    stations = int(extracted["ring_stations"])
    program = K.interleaved_program(int(extracted["fixture_banks"]))
    banks, links = K.B.chain_genesis(int(extracted["fixture_banks"]))
    data = K.M.prepare_endpoint(K.M.pack_state(banks, links), (1, 0))
    a = (1, 1) + (0,) * (stations - 2)
    b = (0,) * stations
    work = (0,) * stations

    step0_violations = _ownership_violations(a, b, work)
    step_data, step_a, step_b = K.apply_controller_step(
        data, program, a, b
    )
    orbit_data, orbit_a, orbit_b, orbit_trace = K.run_orbit(
        data, program, token_positions=(0, 1)
    )

    control_rows = []
    for position in (0, 1):
        single_a = tuple(
            int(index == position) for index in range(stations)
        )
        control_rows.append(
            (position, _ownership_violations(single_a, b, work))
        )
    control_violation_count = sum(
        len(violations) for _, violations in control_rows
    )
    observed_witness = (
        ("ring_stations", len(program)),
        ("A_count", sum(a)),
        ("A_sites", _occupied(a)),
        ("B_count", sum(b)),
        ("work_count", sum(work)),
        ("single_token_control_violations", control_violation_count),
    )
    observed_stations = tuple(row[0] for row in step0_violations)
    expected_reasons = (
        (0, ("right_A",)),
        (1, ("left_A",)),
    )
    first_trace = orbit_trace[0] if orbit_trace else None
    return {
        "name": extracted["obstruction_name"],
        "invariant": extracted["obstruction_invariant"],
        "first_step": 0,
        "first_stations": observed_stations,
        "violation_reasons": step0_violations,
        "minimal_witness": observed_witness,
        "single_token_controls": tuple(control_rows),
        "specific_to_adjacent_pair": control_violation_count == 0,
        "K_program_stations": len(program),
        "K_step_A_after": _occupied(step_a),
        "K_step_B_after": _occupied(step_b),
        "K_orbit_first_trace": first_trace,
        "K_direct_step_matches_orbit_first_step": (
            first_trace == ((0, 1), (1, 2), 0)
            and _occupied(step_a) == first_trace[1]
            and sum(step_b) == first_trace[2]
        ),
        "K_orbit_token_return": (
            _occupied(orbit_a) == (0, 1) and not any(orbit_b)
        ),
        "K_public_outputs_were_computed": (
            isinstance(step_data, tuple) and isinstance(orbit_data, tuple)
        ),
        "pass": (
            len(program) == stations == 11
            and extracted["obstruction_name"] == EXPECTED_OBSTRUCTION_NAME
            and extracted["obstruction_invariant"]
            == EXPECTED_OBSTRUCTION_INVARIANT
            and extracted["first_step"] == 0
            and extracted["first_stations"] == (0, 1)
            and observed_stations == (0, 1)
            and step0_violations == expected_reasons
            and observed_witness == EXPECTED_MINIMAL_WITNESS
            and observed_witness == extracted["minimal_witness"]
            and control_violation_count == 0
            and first_trace == ((0, 1), (1, 2), 0)
            and _occupied(step_a) == (1, 2)
            and not any(step_b)
            and _occupied(orbit_a) == (0, 1)
            and not any(orbit_b)
        ),
    }


def _immutable_literal(value: object) -> bool:
    if value is None or type(value) in (bool, int, float, str):
        return True
    return type(value) is tuple and all(_immutable_literal(item) for item in value)


def discipline(
    extracted: dict[str, object],
    source_boundary_retired: bool,
) -> dict[str, object]:
    """Check import/module discipline and publish the exact honest boundary."""

    loaded_blocklisted = tuple(
        sorted(
            name
            for name in sys.modules
            if any(
                name == f"frontier_cycle{cycle}"
                or name.startswith(f"frontier_cycle{cycle}_")
                for cycle in BLOCKLISTED_CYCLES
            )
        )
    )
    current_k_attributes = tuple(
        sorted((name, id(value)) for name, value in vars(K).items())
    )
    frozen_tables = (
        AUDIT_INPUT_PATHS,
        EXPECTED_PAIR_TEMPLATE,
        EXPECTED_GENESIS_AUDIT_INPUTS,
        EXPECTED_REFUSED_COUNTS,
        EXPECTED_MINIMAL_WITNESS,
        EXPECTED_W2_REMAINING_COMPONENTS,
        BLOCKLISTED_CYCLES,
    )
    boundary = {
        "source_boundary_retired_for_preparation": source_boundary_retired,
        "controller_two_token_lawful": False,
        "w2_remaining_components": extracted["w2_remaining_components"],
        "claim_scope": extracted["claim_scope"],
    }
    return {
        "K_attribute_writes": current_k_attributes != K_ATTRIBUTE_BASELINE,
        "blocklisted_imports": loaded_blocklisted,
        "frozen_tables_are_immutable_literals": all(
            _immutable_literal(table) for table in frozen_tables
        ),
        "AUDIT_INPUT_PATHS_is_pure_literal_tuple": (
            type(AUDIT_INPUT_PATHS) is tuple
            and AUDIT_INPUT_PATHS
            == (
                "scripts/frontier_cycle734_paired_excitation_genesis_2026_07_28.py",
                "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
            )
        ),
        "honest_boundary": boundary,
        "pass": (
            current_k_attributes == K_ATTRIBUTE_BASELINE
            and not loaded_blocklisted
            and all(_immutable_literal(table) for table in frozen_tables)
            and source_boundary_retired is True
            and boundary["controller_two_token_lawful"] is False
            and boundary["w2_remaining_components"]
            == EXPECTED_W2_REMAINING_COMPONENTS
            and boundary["claim_scope"] == EXPECTED_CLAIM_SCOPE
        ),
    }


def _honest_failure(label: str, error: BaseException) -> dict[str, object]:
    return {
        "pass": False,
        "certificate": label,
        "error": f"{type(error).__name__}: {error}",
    }


def main() -> int:
    started = perf_counter()
    checks: dict[str, bool] = {}
    certificates: dict[str, dict[str, object]] = {}
    extracted: dict[str, object] = {}

    try:
        extraction_public, extracted = extraction()
    except BaseException as error:
        extraction_public = _honest_failure("extraction", error)
    certificates["extraction"] = extraction_public
    checks["extraction"] = bool(extraction_public.get("pass"))

    try:
        pair = pair_word_recount(extracted)
    except BaseException as error:
        pair = _honest_failure("pair_word_recount", error)
    certificates["pair_word_recount"] = pair
    checks["pair_word_recount"] = bool(pair.get("pass"))

    try:
        law = count2_law_recount(extracted)
    except BaseException as error:
        law = _honest_failure("count2_law_recount", error)
    certificates["count2_law_recount"] = law
    checks["count2_law_recount"] = bool(law.get("pass"))

    try:
        obstruction = obstruction_reproduction(extracted)
    except BaseException as error:
        obstruction = _honest_failure("obstruction_reproduction", error)
    certificates["obstruction_reproduction"] = obstruction
    checks["obstruction_reproduction"] = bool(obstruction.get("pass"))

    source_boundary_retired = (
        checks["extraction"] and checks["pair_word_recount"]
    )
    try:
        disciplined = discipline(extracted, source_boundary_retired)
    except BaseException as error:
        disciplined = _honest_failure("discipline", error)
    certificates["discipline"] = disciplined
    checks["discipline"] = bool(disciplined.get("pass"))

    elapsed = perf_counter() - started
    all_pass = all(checks.values()) and elapsed < AUDIT_TIMEOUT_SEC
    report: dict[str, Any] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "checks": checks,
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "pass": all_pass,
        "runtime_seconds": round(elapsed, 6),
        "certificates": certificates,
        "terminal": (
            "CYCLE734_PAIRED_EXCITATION_INDEPENDENT_CHECK_PASS"
            if all_pass
            else "CYCLE734_PAIRED_EXCITATION_INDEPENDENT_CHECK_HONEST_FAIL"
        ),
    }
    lines = [
        f"{'PASS' if passed else 'FAIL'} {label} :: {passed}"
        for label, passed in checks.items()
    ]
    payload = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(lines) + "\nSUMMARY_JSON " + payload + "\n"
    if len(text.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        compact = {
            "checks": checks,
            "checks_passed": sum(checks.values()),
            "checks_total": len(checks),
            "pass": False,
            "runtime_seconds": round(elapsed, 6),
            "stdout_bytes_before_compaction": len(text.encode("utf-8")),
            "terminal": (
                "CYCLE734_PAIRED_EXCITATION_INDEPENDENT_CHECK_HONEST_FAIL"
            ),
        }
        text = (
            "\n".join(lines)
            + "\nFAIL stdout_under_150KB :: False\nSUMMARY_JSON "
            + json.dumps(compact, sort_keys=True, separators=(",", ":"))
            + "\n"
        )
        all_pass = False
    sys.stdout.write(text)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
