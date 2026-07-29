#!/usr/bin/env python3
"""Cycle 732 bounded independent checker.

The Cycle 732 primary is parsed as inert AST data.  Only the Cycle 719 core
is imported, and the genesis gates, simulator, count/parity/charge law, and
corruption sweeps below are independent implementations.
"""
from __future__ import annotations

import ast
from hashlib import sha256
from pathlib import Path
from time import perf_counter

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/GENESIS_WORD_SELF_VERIFICATION_CYCLE732_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

STDOUT_LIMIT_BYTES = 150 * 1024

# All audit expectations that stand in for upstream Cycle 730/731 objects are
# deliberately literal.  Nothing in this file imports those primaries.
FROZEN_LAYOUT = {
    "stations": 11,
    "data_width": 5815,
    "a_base": 5815,
    "b_base": 5826,
    "work_base": 5837,
    "pre_ref_aux_base": 5848,
    "ref_base": 5947,
    "pre_h_aux_base": 5958,
    "h_wire": 5969,
    "audited_width": 5970,
}

FROZEN_DATA_ONE_WIRES = (
    6,
    40,
    109,
    110,
    111,
    112,
    113,
    114,
    116,
    117,
    118,
    119,
    126,
    127,
    128,
    129,
    257,
    258,
    259,
    260,
)

# This is the odd-ring marked-edge pattern: the 0->1 edge is twisted by h.
FROZEN_REFS = (0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1)
FROZEN_H = 1
FROZEN_TARGET_ONE_WIRES = (
    6,
    40,
    109,
    110,
    111,
    112,
    113,
    114,
    116,
    117,
    118,
    119,
    126,
    127,
    128,
    129,
    257,
    258,
    259,
    260,
    5815,
    5949,
    5951,
    5953,
    5955,
    5957,
    5969,
)

FROZEN_GENESIS_WORD = (
    ("X", (5815,)),
    ("CNOT", (5815, 6)),
    ("CNOT", (6, 40)),
    ("CNOT", (40, 109)),
    ("CNOT", (109, 110)),
    ("CNOT", (110, 111)),
    ("CNOT", (111, 112)),
    ("CNOT", (112, 113)),
    ("CNOT", (113, 114)),
    ("CNOT", (114, 116)),
    ("CNOT", (116, 117)),
    ("CNOT", (117, 118)),
    ("CNOT", (118, 119)),
    ("CNOT", (119, 126)),
    ("CNOT", (126, 127)),
    ("CNOT", (127, 128)),
    ("CNOT", (128, 129)),
    ("CNOT", (129, 257)),
    ("CNOT", (257, 258)),
    ("CNOT", (258, 259)),
    ("CNOT", (259, 260)),
    ("CNOT", (260, 5949)),
    ("CNOT", (5949, 5951)),
    ("CNOT", (5951, 5953)),
    ("CNOT", (5953, 5955)),
    ("CNOT", (5955, 5957)),
    ("CNOT", (5957, 5969)),
)

# The Boolean column is the frozen predicted acceptance verdict.
FROZEN_DELETION_ACCEPTANCE = (
    (0, False),
    (1, False),
    (2, False),
    (3, False),
    (4, False),
    (5, False),
    (6, False),
    (7, False),
    (8, False),
    (9, False),
    (10, False),
    (11, False),
    (12, False),
    (13, False),
    (14, False),
    (15, False),
    (16, False),
    (17, False),
    (18, False),
    (19, False),
    (20, False),
    (21, False),
    (22, False),
    (23, False),
    (24, False),
    (25, False),
    (26, False),
)

FROZEN_BITFLIP_ACCEPTANCE = (
    ("A[0]", 5815, False),
    ("A[1]", 5816, False),
    ("A[2]", 5817, False),
    ("A[3]", 5818, False),
    ("A[4]", 5819, False),
    ("A[5]", 5820, False),
    ("A[6]", 5821, False),
    ("A[7]", 5822, False),
    ("A[8]", 5823, False),
    ("A[9]", 5824, False),
    ("A[10]", 5825, False),
    ("refs[0]", 5947, False),
    ("refs[1]", 5948, False),
    ("refs[2]", 5949, False),
    ("refs[3]", 5950, False),
    ("refs[4]", 5951, False),
    ("refs[5]", 5952, False),
    ("refs[6]", 5953, False),
    ("refs[7]", 5954, False),
    ("refs[8]", 5955, False),
    ("refs[9]", 5956, False),
    ("refs[10]", 5957, False),
    ("h", 5969, False),
)

FROZEN_CENSUSES = {
    "genesis_gates": 27,
    "genesis_x": 1,
    "genesis_cnot": 26,
    "deletion_total": 27,
    "deletion_refused": 27,
    "deletion_output_neutral": 0,
    "bitflip_total": 23,
    "bitflip_refused": 23,
}

FROZEN_SIZE_ARITHMETIC = {
    "genesis": 27,
    "Cycle731_word": 112912,
    "interface_overhead": 10354,
    "composed": 123293,
    "held_stations": 11,
    "held_step_word": 11206,
}

FROZEN_BOUNDARY = {
    "genesis_state_now_derived_output": True,
    "genesis_word_selection_supplied": True,
    "w1_remaining_gap": "genesis word selection (convention), not inventory declaration",
}

BLOCKLISTED_CYCLE_PREFIXES = (
    "frontier_cycle732_",
    "frontier_cycle731_",
    "frontier_cycle730_",
    "frontier_cycle724_",
)

FROZEN_LITERAL_NAMES = (
    "AUDIT_INPUT_PATHS",
    "FROZEN_LAYOUT",
    "FROZEN_DATA_ONE_WIRES",
    "FROZEN_REFS",
    "FROZEN_H",
    "FROZEN_TARGET_ONE_WIRES",
    "FROZEN_GENESIS_WORD",
    "FROZEN_DELETION_ACCEPTANCE",
    "FROZEN_BITFLIP_ACCEPTANCE",
    "FROZEN_CENSUSES",
    "FROZEN_SIZE_ARITHMETIC",
    "FROZEN_BOUNDARY",
    "BLOCKLISTED_CYCLE_PREFIXES",
)


def _module_literal(tree: ast.Module, name: str) -> object:
    matches = []
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            matches.append(node.value)
    if len(matches) != 1:
        raise ValueError(("literal assignment census", name, len(matches)))
    return ast.literal_eval(matches[0])


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise ValueError(("function census", name, len(matches)))
    return matches[0]


def _qualified_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = _qualified_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def _has_expression(scope: ast.AST, expression: str) -> bool:
    expected = ast.dump(
        ast.parse(expression, mode="eval").body,
        include_attributes=False,
    )
    return any(
        ast.dump(node, include_attributes=False) == expected
        for node in ast.walk(scope)
    )


def _assignment_value(scope: ast.AST, name: str) -> ast.AST:
    matches = [
        node.value
        for node in ast.walk(scope)
        if isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
        and node.targets[0].id == name
    ]
    if len(matches) != 1:
        raise ValueError(("assignment census", name, len(matches)))
    return matches[0]


def _boundary_literals(tree: ast.Module) -> dict[str, object]:
    boundary = _assignment_value(_function(tree, "main"), "boundary")
    if not isinstance(boundary, ast.Dict):
        raise TypeError("boundary is not a dict literal")
    output = {}
    for key_node, value_node in zip(boundary.keys, boundary.values):
        if key_node is None:
            continue
        key = ast.literal_eval(key_node)
        if key in FROZEN_BOUNDARY:
            output[key] = ast.literal_eval(value_node)
    return output


def _primary_structure(tree: ast.Module) -> dict[str, bool]:
    target_fn = _function(tree, "declared_genesis_target")
    word_fn = _function(tree, "genesis_word")
    exact_fn = _function(tree, "genesis_exactness_certificate")
    corrupt_fn = _function(tree, "corrupted_genesis_certificate")
    compose_fn = _function(tree, "composed_self_verification_certificate")

    target_calls = {
        _qualified_name(node.func)
        for node in ast.walk(target_fn)
        if isinstance(node, ast.Call)
    }
    word_calls = {
        _qualified_name(node.func)
        for node in ast.walk(word_fn)
        if isinstance(node, ast.Call)
    }
    prepare_directions = [
        ast.literal_eval(node.args[1])
        for node in ast.walk(target_fn)
        if isinstance(node, ast.Call)
        and _qualified_name(node.func) == "K.M.prepare_endpoint"
        and len(node.args) >= 2
    ]
    full_input_calls = [
        node
        for node in ast.walk(target_fn)
        if isinstance(node, ast.Call)
        and _qualified_name(node.func) == "C731.controller_full_input"
    ]
    full_input_keywords = {
        keyword.arg: keyword.value
        for call in full_input_calls
        for keyword in call.keywords
        if keyword.arg is not None
    }
    exact_labels = {
        node.value
        for node in ast.walk(exact_fn)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    composed_value = _assignment_value(compose_fn, "composed")
    expected_composed_value = ast.parse(
        "word + controller_word * len(program)", mode="eval"
    ).body

    return {
        "target_calls_core":
            {
                "K.B.chain_genesis",
                "K.M.pack_state",
                "K.M.prepare_endpoint",
                "E730.lawful_reference_rails",
                "C731.controller_full_input",
            }
            <= target_calls,
        "target_direction": prepare_directions == [(1, 0)],
        "target_source_token":
            len(full_input_calls) == 1
            and "a" in full_input_keywords
            and ast.literal_eval(full_input_keywords["a"]) == (0,),
        "target_refs_h":
            isinstance(full_input_keywords.get("refs"), ast.Name)
            and full_input_keywords["refs"].id == "refs"
            and isinstance(full_input_keywords.get("h"), ast.Name)
            and full_input_keywords["h"].id == "h",
        "word_calls":
            {"compress", "zip", "K.A.x", "K.A.cn"} <= word_calls,
        "word_no_runtime_branches":
            not any(
                isinstance(node, (ast.If, ast.IfExp, ast.Match, ast.While))
                for node in ast.walk(word_fn)
            ),
        "word_order":
            _has_expression(
                word_fn,
                "(layout['a_base'],) + data_ones + ref_ones + (layout['h_wire'],)",
            ),
        "word_return":
            _has_expression(
                word_fn,
                "(K.A.x(ordered_wires[0]),) + tuple(K.A.cn(left, right) for left, right in zip(ordered_wires, ordered_wires[1:]))",
            ),
        "all_declared_registers":
            {
                "data",
                "A_source_only",
                "B_blank",
                "work_blank",
                "refs",
                "h",
                "counter_and_scratch_blank",
            }
            <= exact_labels,
        "deletion_census_form":
            _has_expression(
                tree,
                "deletions['total_gates'] == EXPECTED_GENESIS_GATES",
            )
            and _has_expression(
                tree,
                "deletions['output_different'] == EXPECTED_GENESIS_GATES",
            )
            and _has_expression(
                tree,
                "deletions['refused'] == deletions['output_different']",
            )
            and _has_expression(
                tree,
                "deletions['output_different'] + deletions['output_neutral'] == deletions['total_gates']",
            ),
        "bitflip_census_form":
            _has_expression(tree, "flips['total'] == 2 * RING_STATIONS + 1")
            and _has_expression(
                tree, "flips['predicted_refused'] == flips['total']"
            )
            and _has_expression(
                tree, "flips['observed_refused'] == flips['total']"
            )
            and _has_expression(
                tree, "flips['verdict_agreements'] == flips['total']"
            )
            and _has_expression(tree, "flips['verdict_disagreements'] == 0"),
        "composition_form":
            ast.dump(composed_value, include_attributes=False)
            == ast.dump(expected_composed_value, include_attributes=False),
        "corruption_function_present": bool(corrupt_fn),
    }


def _own_gate_digest(word: tuple[tuple[str, tuple[int, ...]], ...]) -> str:
    payload = "".join(kind + repr(wires) for kind, wires in word)
    return sha256(payload.encode()).hexdigest()


def _target_from_frozen_configuration() -> int:
    return sum(1 << wire for wire in FROZEN_TARGET_ONE_WIRES)


def _compile_extracted_word() -> tuple[tuple[str, tuple[int, ...]], ...]:
    data_ones = tuple(FROZEN_DATA_ONE_WIRES)
    ref_ones = tuple(
        FROZEN_LAYOUT["ref_base"] + station
        for station, bit in enumerate(FROZEN_REFS)
        if bit
    )
    ordered_wires = (
        (FROZEN_LAYOUT["a_base"],)
        + data_ones
        + ref_ones
        + (FROZEN_LAYOUT["h_wire"],)
    )
    return (("X", (ordered_wires[0],)),) + tuple(
        ("CNOT", (left, right))
        for left, right in zip(ordered_wires, ordered_wires[1:])
    )


def extraction(primary_tree: ast.Module) -> dict[str, object]:
    expected_gates = _module_literal(primary_tree, "EXPECTED_GENESIS_GATES")
    expected_digest = _module_literal(primary_tree, "EXPECTED_GENESIS_SHA256")
    cycle731_gates = _module_literal(
        primary_tree, "EXPECTED_CYCLE731_PADDED_GATES"
    )
    ring_stations = _module_literal(primary_tree, "RING_STATIONS")
    fixture_banks = _module_literal(primary_tree, "FIXTURE_BANKS")
    structure = _primary_structure(primary_tree)
    boundary = _boundary_literals(primary_tree)

    program = K.interleaved_program(2)
    banks, links = K.B.chain_genesis(2)
    data = tuple(
        int(bit)
        for bit in K.M.prepare_endpoint(
            K.M.pack_state(banks, links), (1, 0)
        )
    )
    data_ones = tuple(index for index, bit in enumerate(data) if bit)
    extracted_word = _compile_extracted_word()
    extracted_censuses = {
        "genesis_gates": expected_gates,
        "genesis_x": 1,
        "genesis_cnot": expected_gates - 1,
        "deletion_total": expected_gates,
        "deletion_refused": expected_gates,
        "deletion_output_neutral": 0,
        "bitflip_total": 2 * ring_stations + 1,
        "bitflip_refused": 2 * ring_stations + 1,
    }
    conditions = {
        **structure,
        "primary_ring_fixture":
            ring_stations == FROZEN_LAYOUT["stations"]
            and fixture_banks == 2
            and len(program) == ring_stations,
        "core_data_width": len(data) == FROZEN_LAYOUT["data_width"],
        "core_data_pattern": data_ones == FROZEN_DATA_ONE_WIRES,
        "reference_pattern":
            FROZEN_REFS == (0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1)
            and sum(bit << station for station, bit in enumerate(FROZEN_REFS))
            == 1364,
        "h_value": FROZEN_H == 1,
        "word_literal": extracted_word == FROZEN_GENESIS_WORD,
        "word_census":
            len(extracted_word) == expected_gates
            and sum(kind == "X" for kind, _wires in extracted_word) == 1
            and sum(kind == "CNOT" for kind, _wires in extracted_word) == 26,
        "word_digest": _own_gate_digest(extracted_word) == expected_digest,
        "frozen_censuses": extracted_censuses == FROZEN_CENSUSES,
        "Cycle731_size_pin":
            cycle731_gates == FROZEN_SIZE_ARITHMETIC["Cycle731_word"],
        "boundary_exact": boundary == FROZEN_BOUNDARY,
    }
    return {
        "pass": all(conditions.values()),
        "conditions": conditions,
        "word": extracted_word,
        "target": _target_from_frozen_configuration(),
        "digest": _own_gate_digest(extracted_word),
    }


def _apply_classical(
    initial: int,
    word: tuple[tuple[str, tuple[int, ...]], ...],
) -> int:
    """Independent reversible X/CNOT simulator on a Python integer."""

    state = int(initial)
    width = FROZEN_LAYOUT["audited_width"]
    for index, (kind, wires) in enumerate(word):
        if any(not isinstance(wire, int) or not 0 <= wire < width for wire in wires):
            raise ValueError(("wire outside audited layout", index, wires))
        if kind == "X" and len(wires) == 1:
            state ^= 1 << wires[0]
        elif kind == "CNOT" and len(wires) == 2:
            control, target = wires
            if (state >> control) & 1:
                state ^= 1 << target
        else:
            raise ValueError(("unsupported independent gate", index, kind, wires))
    return state


def _bit_row(state: int, base: int, width: int) -> tuple[int, ...]:
    return tuple((state >> (base + offset)) & 1 for offset in range(width))


def _register_rows(state: int) -> dict[str, object]:
    layout = FROZEN_LAYOUT
    return {
        "data": _bit_row(state, 0, layout["data_width"]),
        "A": _bit_row(state, layout["a_base"], layout["stations"]),
        "B": _bit_row(state, layout["b_base"], layout["stations"]),
        "work": _bit_row(state, layout["work_base"], layout["stations"]),
        "pre_ref_aux": _bit_row(
            state,
            layout["pre_ref_aux_base"],
            layout["ref_base"] - layout["pre_ref_aux_base"],
        ),
        "refs": _bit_row(state, layout["ref_base"], layout["stations"]),
        "pre_h_aux": _bit_row(
            state,
            layout["pre_h_aux_base"],
            layout["h_wire"] - layout["pre_h_aux_base"],
        ),
        "h": (state >> layout["h_wire"]) & 1,
    }


def genesis_output_recount(
    extracted: dict[str, object],
) -> dict[str, object]:
    word = extracted["word"]
    observed = _apply_classical(0, word)
    target = int(extracted["target"])
    rows = _register_rows(observed)
    expected_data = tuple(
        int(index in FROZEN_DATA_ONE_WIRES)
        for index in range(FROZEN_LAYOUT["data_width"])
    )
    register_checks = {
        "data": rows["data"] == expected_data,
        "A_source_only":
            rows["A"] == (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        "B_blank": not any(rows["B"]),
        "work_blank": not any(rows["work"]),
        "pre_ref_aux_blank": not any(rows["pre_ref_aux"]),
        "refs": rows["refs"] == FROZEN_REFS,
        "pre_h_aux_blank": not any(rows["pre_h_aux"]),
        "h": rows["h"] == FROZEN_H,
    }
    return {
        "pass":
            observed == target
            and observed.bit_count() == len(FROZEN_TARGET_ONE_WIRES)
            and all(register_checks.values()),
        "observed": observed,
        "target": target,
        "register_checks": register_checks,
    }


def _law_accepts(source: int) -> tuple[bool, tuple[str, ...]]:
    """Own Cycle 731 count/parity plus marked-edge charge-row evaluator."""

    rows = _register_rows(source)
    a = tuple(rows["A"])
    b = tuple(rows["B"])
    work = tuple(rows["work"])
    refs = tuple(rows["refs"])
    h = int(rows["h"])
    failures = []
    if sum(a) != 1:
        failures.append("A_count")
    if any(b):
        failures.append("B_dirty")
    if any(work):
        failures.append("work_dirty")
    if (sum(refs) & 1) != h:
        failures.append("parity_not_h")

    # Every station is visited during the held orbit.  An ordinary edge
    # reverses the binary reference charge; the marked 0->1 edge has the
    # additional h twist needed to close an odd ring.
    for station in range(FROZEN_LAYOUT["stations"]):
        right = (station + 1) % FROZEN_LAYOUT["stations"]
        marked_twist = h if station == 0 else 0
        charge = refs[station] ^ refs[right] ^ 1 ^ marked_twist
        if charge:
            failures.append(f"charge[{station}]")

    return not failures, tuple(failures)


def deletion_sweep_recount(
    extracted: dict[str, object],
) -> dict[str, object]:
    word = tuple(extracted["word"])
    target = int(extracted["target"])
    rows = []
    for index in range(len(word)):
        corrupted = _apply_classical(0, word[:index] + word[index + 1 :])
        accepted, failures = _law_accepts(corrupted)
        rows.append((index, corrupted == target, accepted, failures))
    observed_acceptance = tuple((index, accepted) for index, _n, accepted, _f in rows)
    neutral = sum(is_neutral for _i, is_neutral, _a, _f in rows)
    refused = sum(not accepted for _i, _n, accepted, _f in rows)
    return {
        "pass":
            len(rows) == FROZEN_CENSUSES["deletion_total"]
            and neutral == FROZEN_CENSUSES["deletion_output_neutral"]
            and refused == FROZEN_CENSUSES["deletion_refused"]
            and observed_acceptance == FROZEN_DELETION_ACCEPTANCE,
        "total": len(rows),
        "neutral": neutral,
        "refused": refused,
    }


def bitflip_recount(
    extracted: dict[str, object],
) -> dict[str, object]:
    target = int(extracted["target"])
    lawful_accepts, lawful_failures = _law_accepts(target)
    rows = []
    for label, wire, frozen_acceptance in FROZEN_BITFLIP_ACCEPTANCE:
        accepted, failures = _law_accepts(target ^ (1 << wire))
        rows.append((label, wire, accepted, frozen_acceptance, failures))
    agreements = sum(
        accepted == frozen
        for _label, _wire, accepted, frozen, _failures in rows
    )
    refused = sum(
        not accepted for _label, _wire, accepted, _frozen, _failures in rows
    )
    return {
        "pass":
            lawful_accepts
            and not lawful_failures
            and len(rows) == FROZEN_CENSUSES["bitflip_total"]
            and refused == FROZEN_CENSUSES["bitflip_refused"]
            and agreements == len(rows),
        "total": len(rows),
        "refused": refused,
        "agreements": agreements,
    }


def composition_size_audit(primary_tree: ast.Module) -> dict[str, object]:
    sizes = FROZEN_SIZE_ARITHMETIC
    extracted_genesis = _module_literal(primary_tree, "EXPECTED_GENESIS_GATES")
    extracted_cycle731 = _module_literal(
        primary_tree, "EXPECTED_CYCLE731_PADDED_GATES"
    )
    program_stations = len(K.interleaved_program(2))
    compose_fn = _function(
        primary_tree, "composed_self_verification_certificate"
    )
    composed_value = _assignment_value(compose_fn, "composed")
    source_formula = ast.dump(
        composed_value, include_attributes=False
    ) == ast.dump(
        ast.parse(
            "word + controller_word * len(program)", mode="eval"
        ).body,
        include_attributes=False,
    )
    held_unroll = sizes["held_step_word"] * program_stations
    interface = held_unroll - extracted_cycle731
    total = extracted_genesis + extracted_cycle731 + interface
    return {
        "pass":
            source_formula
            and extracted_genesis == sizes["genesis"]
            and extracted_cycle731 == sizes["Cycle731_word"]
            and program_stations == sizes["held_stations"]
            and held_unroll == sizes["composed"] - sizes["genesis"]
            and interface == sizes["interface_overhead"]
            and total == sizes["composed"],
        "genesis": extracted_genesis,
        "Cycle731_word": extracted_cycle731,
        "interface": interface,
        "total": total,
    }


def _target_roots(target: ast.AST) -> tuple[str, ...]:
    if isinstance(target, ast.Name):
        return (target.id,)
    if isinstance(target, ast.Attribute):
        return (_qualified_name(target).split(".", 1)[0],)
    if isinstance(target, (ast.Tuple, ast.List)):
        return tuple(root for item in target.elts for root in _target_roots(item))
    if isinstance(target, ast.Subscript):
        return (_qualified_name(target.value).split(".", 1)[0],)
    return ()


def discipline(self_tree: ast.Module, primary_tree: ast.Module) -> dict[str, object]:
    imported = []
    for node in ast.walk(self_tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")

    assignment_targets = []
    for node in ast.walk(self_tree):
        if isinstance(node, ast.Assign):
            assignment_targets.extend(node.targets)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign, ast.NamedExpr)):
            assignment_targets.append(node.target)
    k_attribute_writes = sum(
        "K" in _target_roots(target) and not isinstance(target, ast.Name)
        for target in assignment_targets
    )
    k_setattr_writes = sum(
        isinstance(node, ast.Call)
        and _qualified_name(node.func) in {"setattr", "delattr"}
        and bool(node.args)
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id == "K"
        for node in ast.walk(self_tree)
    )
    literal_checks = {
        name: _module_literal(self_tree, name)
        for name in FROZEN_LITERAL_NAMES
    }
    expected_inputs = (
        "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py",
        "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    )
    conditions = {
        "audit_tuple_pure_literal":
            literal_checks["AUDIT_INPUT_PATHS"] == expected_inputs,
        "all_frozen_tables_literal_eval":
            len(literal_checks) == len(FROZEN_LITERAL_NAMES),
        "only_K_cycle_primary_imported":
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
            in imported
            and not any(
                module.startswith(prefix)
                for module in imported
                for prefix in BLOCKLISTED_CYCLE_PREFIXES
            ),
        "no_K_attribute_writes": k_attribute_writes + k_setattr_writes == 0,
        "boundary_language_exact":
            _boundary_literals(primary_tree) == FROZEN_BOUNDARY
            and FROZEN_BOUNDARY["genesis_state_now_derived_output"] is True
            and FROZEN_BOUNDARY["genesis_word_selection_supplied"] is True
            and FROZEN_BOUNDARY["w1_remaining_gap"]
            == "genesis word selection (convention), not inventory declaration",
    }
    return {
        "pass": all(conditions.values()),
        "conditions": conditions,
        "blocked_imports": tuple(
            module
            for module in imported
            if any(
                module.startswith(prefix)
                for prefix in BLOCKLISTED_CYCLE_PREFIXES
            )
        ),
        "K_attribute_writes": k_attribute_writes + k_setattr_writes,
    }


def _safe_certificate(label: str, function, *args) -> dict[str, object]:
    try:
        result = function(*args)
        if not isinstance(result, dict) or "pass" not in result:
            raise TypeError("certificate did not return a pass field")
        return result
    except Exception as exc:  # Honest bounded failure, without a large traceback.
        return {
            "pass": False,
            "error": f"{label}: {type(exc).__name__}: {exc}",
        }


def main() -> int:
    started = perf_counter()
    try:
        primary_source = Path(AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
        self_source = Path(__file__).read_text(encoding="utf-8")
        primary_tree = ast.parse(primary_source, filename=AUDIT_INPUT_PATHS[0])
        self_tree = ast.parse(self_source, filename=__file__)
    except Exception as exc:
        elapsed = perf_counter() - started
        message = f"{type(exc).__name__}: {exc}"
        lines = [
            f"FAIL extraction :: {message}",
            "FAIL genesis recount :: unavailable",
            "FAIL deletion recount :: unavailable",
            "FAIL bit-flip recount :: unavailable",
            "FAIL size arithmetic :: unavailable",
            "FAIL discipline :: unavailable",
            f"SUMMARY 0/6 HONEST_FAIL runtime={elapsed:.6f}s",
        ]
        print("\n".join(lines))
        return 1

    extracted = _safe_certificate("extraction", extraction, primary_tree)
    genesis = _safe_certificate(
        "genesis_output_recount", genesis_output_recount, extracted
    )
    deletions = _safe_certificate(
        "deletion_sweep_recount", deletion_sweep_recount, extracted
    )
    bitflips = _safe_certificate(
        "bitflip_recount", bitflip_recount, extracted
    )
    sizes = _safe_certificate(
        "composition_size_audit", composition_size_audit, primary_tree
    )
    disciplined = _safe_certificate(
        "discipline", discipline, self_tree, primary_tree
    )

    certificates = (
        ("extraction", extracted),
        ("genesis", genesis),
        ("deletions", deletions),
        ("bitflips", bitflips),
        ("sizes", sizes),
        ("discipline", disciplined),
    )
    passed = sum(bool(row.get("pass")) for _label, row in certificates)
    elapsed = perf_counter() - started
    lines = [
        (
            f"{'PASS' if extracted.get('pass') else 'FAIL'} extraction :: "
            f"27 gates (1 X + 26 CNOT), ring-11 boundary/configuration"
        ),
        (
            f"{'PASS' if genesis.get('pass') else 'FAIL'} genesis recount :: "
            f"blank -> declared 27-one configuration, every register exact"
        ),
        (
            f"{'PASS' if deletions.get('pass') else 'FAIL'} deletion recount :: "
            f"{deletions.get('refused', 0)}/{deletions.get('total', 0)} refused, "
            f"{deletions.get('neutral', '?')} output-neutral"
        ),
        (
            f"{'PASS' if bitflips.get('pass') else 'FAIL'} bit-flip recount :: "
            f"{bitflips.get('refused', 0)}/{bitflips.get('total', 0)} refused, "
            f"{bitflips.get('agreements', 0)} frozen-verdict agreements"
        ),
        (
            f"{'PASS' if sizes.get('pass') else 'FAIL'} size arithmetic :: "
            f"{sizes.get('genesis', '?')} + {sizes.get('Cycle731_word', '?')} + "
            f"{sizes.get('interface', '?')} = {sizes.get('total', '?')}"
        ),
        (
            f"{'PASS' if disciplined.get('pass') else 'FAIL'} discipline :: "
            f"AST-only primary, no blocklisted imports, no K writes"
        ),
        (
            f"SUMMARY {passed}/6 "
            f"{'ALL_PASS' if passed == 6 else 'HONEST_FAIL'} "
            f"runtime={elapsed:.6f}s"
        ),
    ]
    text = "\n".join(lines) + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        lines[5] = "FAIL discipline :: stdout exceeded 150KB"
        lines[6] = f"SUMMARY {min(passed, 5)}/6 HONEST_FAIL runtime={elapsed:.6f}s"
        text = "\n".join(lines) + "\n"
        passed = min(passed, 5)
    print(text, end="")
    return 0 if passed == 6 else 1


if __name__ == "__main__":
    raise SystemExit(main())
