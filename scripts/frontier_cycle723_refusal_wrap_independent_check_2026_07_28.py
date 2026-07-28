#!/usr/bin/env python3
"""Independent bounded checker for the recurrent-controller refusal wrapper.

The primary runner is never imported. It is read only as source text for
the narrowly scoped AST discipline checks below.  All classical gate and
refusal-sandwich semantics in this file are independent reconstructions.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/REFUSAL_WRAPPED_CONTROLLER_CYCLE723_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle723_refusal_wrapped_controller_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/REFUSAL_WRAPPED_CONTROLLER_CYCLE723_BOUNDED_THEOREM_NOTE_2026-07-28.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY_PATH = AUDIT_INPUT_PATHS[0]
PRIMARY_MODULE = "frontier_cycle723_refusal_wrapped_controller_2026_07_28"
TOP_LEVEL_BLOCKLIST = {PRIMARY_MODULE}

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


_BLOCKED_AFTER_IMPORTS = sorted(TOP_LEVEL_BLOCKLIST & set(sys.modules))
assert not _BLOCKED_AFTER_IMPORTS, (
    f"Primary refusal runner imported transitively: {_BLOCKED_AFTER_IMPORTS}"
)

SCRATCH_PER_STATION = 2
# Cross-checks the primary runner's reported wrapped H-word size of 95,850.
EXPECTED_WRAPPED_130_WORD_SIZE = 95_850
CHECKS: list[dict[str, object]] = []


@dataclass(frozen=True)
class ClassicalGate:
    """A small independent classical reversible-gate representation."""

    kind: str
    controls: tuple[int, ...]
    target: int


def x(target: int) -> ClassicalGate:
    return ClassicalGate("X", (), target)


def cn(control: int, target: int) -> ClassicalGate:
    return ClassicalGate("CN", (control,), target)


def tof(left: int, right: int, target: int) -> ClassicalGate:
    return ClassicalGate("TOF", (left, right), target)


def mcx(controls: tuple[int, ...], target: int) -> ClassicalGate:
    return ClassicalGate("MCX", tuple(controls), target)


def toggle(state: dict[int, int], wire: int) -> None:
    state[wire] = 1 - state.get(wire, 0)
    if not state[wire]:
        del state[wire]


def apply_gate(state: dict[int, int], gate: ClassicalGate) -> None:
    """Apply X/CN/TOF/MCX directly to a sparse dict[int, int] state."""
    if gate.kind == "X":
        enabled = True
    elif gate.kind == "CN":
        if len(gate.controls) != 1:
            raise ValueError(("CN arity", gate.controls))
        enabled = bool(state.get(gate.controls[0], 0))
    elif gate.kind == "TOF":
        if len(gate.controls) != 2:
            raise ValueError(("TOF arity", gate.controls))
        enabled = all(state.get(wire, 0) for wire in gate.controls)
    elif gate.kind == "MCX":
        if len(gate.controls) < 1:
            raise ValueError(("MCX arity", gate.controls))
        enabled = all(state.get(wire, 0) for wire in gate.controls)
    else:
        raise ValueError(("unknown classical gate", gate.kind))
    if enabled:
        toggle(state, gate.target)


def apply_word(
    source: dict[int, int],
    word: tuple[ClassicalGate, ...],
    repeats: int = 1,
) -> dict[int, int]:
    output = dict(source)
    for _step in range(repeats):
        for gate in word:
            apply_gate(output, gate)
    return output


def mcx_expansion_size(control_count: int) -> int:
    if control_count < 1:
        raise ValueError(control_count)
    return 1 if control_count <= 2 else 2 * control_count - 3


def expand_mcx(
    controls: tuple[int, ...],
    target: int,
    scratch: tuple[int, ...],
) -> tuple[ClassicalGate, ...]:
    """Independently decompose an MCX through a clean scratch ladder."""
    controls = tuple(controls)
    if len(controls) == 1:
        return (cn(controls[0], target),)
    if len(controls) == 2:
        return (tof(controls[0], controls[1], target),)
    required = len(controls) - 2
    if len(scratch) < required:
        raise ValueError(("clean MCX scratch", len(controls), len(scratch)))

    compute = [tof(controls[0], controls[1], scratch[0])]
    for index in range(2, len(controls) - 1):
        compute.append(
            tof(scratch[index - 2], controls[index], scratch[index - 1])
        )
    action = tof(scratch[required - 1], controls[-1], target)
    return tuple(compute) + (action,) + tuple(reversed(compute))


def imported_macro(row: object) -> tuple[ClassicalGate, ...]:
    """Translate a K macro into this checker's gate vocabulary."""
    output = []
    for gate in K.mapped_macro(row):
        if gate.kind == "X":
            output.append(x(gate.wires[0]))
        elif gate.kind == "CNOT":
            output.append(cn(gate.wires[0], gate.wires[1]))
        elif gate.kind == "TOF":
            output.append(tof(gate.wires[0], gate.wires[1], gate.wires[2]))
        else:
            raise ValueError(("unsupported K macro gate", gate.kind))
    return tuple(output)


def register_layout(
    data_width: int,
    stations: int,
    *,
    wrapped: bool,
) -> dict[str, int]:
    a_base = data_width
    b_base = a_base + stations
    work_base = b_base + stations
    layout = {
        "data_width": data_width,
        "stations": stations,
        "a_base": a_base,
        "b_base": b_base,
        "work_base": work_base,
    }
    if wrapped:
        syndrome_base = work_base + stations
        scratch_base = syndrome_base + stations
        layout.update({
            "syndrome_base": syndrome_base,
            "scratch_base": scratch_base,
            "full_width": scratch_base + SCRATCH_PER_STATION * stations,
        })
    else:
        layout["full_width"] = work_base + stations
    return layout


def scratch_wires(layout: dict[str, int], station: int) -> tuple[int, ...]:
    return tuple(
        layout["scratch_base"] + SCRATCH_PER_STATION * station + slot
        for slot in range(SCRATCH_PER_STATION)
    )


def swap_word(left: int, right: int) -> tuple[ClassicalGate, ...]:
    return (cn(left, right), cn(right, left), cn(left, right))


def lift_unwrapped(
    macro: tuple[ClassicalGate, ...],
    control: int,
    work: int,
) -> tuple[ClassicalGate, ...]:
    output = []
    for gate in macro:
        if gate.kind == "X":
            output.append(cn(control, gate.target))
        elif gate.kind == "CN":
            output.append(tof(control, gate.controls[0], gate.target))
        elif gate.kind == "TOF":
            output.extend(expand_mcx(
                (control,) + gate.controls,
                gate.target,
                (work,),
            ))
        else:
            raise ValueError(gate.kind)
    return tuple(output)


def refusal_sandwich(
    macro: tuple[ClassicalGate, ...],
    control: int,
    b_wire: int,
    work: int,
    syndrome: int,
    scratch: tuple[int, ...],
) -> tuple[ClassicalGate, ...]:
    """Own implementation of synd ^= B OR work and the NOT-synd guard."""
    if not macro:
        return ()
    if len(scratch) != SCRATCH_PER_STATION:
        raise ValueError(("fresh refusal scratch", len(scratch)))
    compute = (
        cn(b_wire, syndrome),
        cn(work, syndrome),
        tof(b_wire, work, syndrome),
    )
    lifted = []
    for gate in macro:
        if gate.kind == "X":
            lifted.append(tof(control, syndrome, gate.target))
        elif gate.kind == "CN":
            lifted.extend(expand_mcx(
                (control, syndrome, gate.controls[0]),
                gate.target,
                scratch,
            ))
        elif gate.kind == "TOF":
            lifted.extend(expand_mcx(
                (control, syndrome) + gate.controls,
                gate.target,
                scratch,
            ))
        else:
            raise ValueError(gate.kind)
    return (
        compute
        + (x(syndrome),)
        + tuple(lifted)
        + (x(syndrome),)
        + tuple(reversed(compute))
    )


def controller_word(
    program: tuple[object, ...],
    data_width: int,
    *,
    wrapped: bool,
) -> tuple[tuple[ClassicalGate, ...], dict[str, int]]:
    layout = register_layout(data_width, len(program), wrapped=wrapped)
    q = []
    for station, row in enumerate(program):
        macro = imported_macro(row)
        control = layout["a_base"] + station
        work = layout["work_base"] + station
        if wrapped:
            q.extend(refusal_sandwich(
                macro,
                control,
                layout["b_base"] + station,
                work,
                layout["syndrome_base"] + station,
                scratch_wires(layout, station),
            ))
        else:
            q.extend(lift_unwrapped(macro, control, work))
    rails = []
    for station in range(len(program)):
        rails.extend(swap_word(
            layout["a_base"] + station,
            layout["b_base"] + station,
        ))
    for station in range(len(program)):
        rails.extend(swap_word(
            layout["b_base"] + station,
            layout["a_base"] + (station + 1) % len(program),
        ))
    return tuple(q + rails), layout


def bit_state(bits: tuple[int, ...]) -> dict[int, int]:
    return {wire: 1 for wire, value in enumerate(bits) if value}


def projected_state(
    state: dict[int, int],
    start: int,
    length: int,
) -> tuple[int, ...]:
    return tuple(state.get(start + index, 0) for index in range(length))


def data_projection(
    state: dict[int, int],
    data_width: int,
) -> dict[int, int]:
    return {
        wire: value
        for wire, value in state.items()
        if wire < data_width and value
    }


def add_register_bit(
    state: dict[int, int],
    layout: dict[str, int],
    register: str,
    station: int,
) -> None:
    wire = layout[f"{register.lower()}_base"] + station
    if state.get(wire, 0):
        raise ValueError(("register bit already set", register, station))
    state[wire] = 1


def independent_host_orbit(
    source_data: dict[int, int],
    program: tuple[object, ...],
    *,
    b_station: int | None = None,
    work_station: int | None = None,
) -> dict[str, object]:
    """Macro-level identity-substitution prediction from explicit rail swaps."""
    stations = len(program)
    a = [0] * stations
    b = [0] * stations
    work = [0] * stations
    a[0] = 1
    if b_station is not None:
        b[b_station] = 1
    if work_station is not None:
        work[work_station] = 1
    data = dict(source_data)
    refused = []

    for step in range(stations):
        for station, row in enumerate(program):
            if not a[station]:
                continue
            if b[station] or work[station]:
                refused.append((step, station))
            else:
                for gate in imported_macro(row):
                    apply_gate(data, gate)
        for station in range(stations):
            a[station], b[station] = b[station], a[station]
        for station in range(stations):
            target = (station + 1) % stations
            b[station], a[target] = a[target], b[station]

    return {
        "data": data,
        "A": tuple(a),
        "B": tuple(b),
        "work": tuple(work),
        "refused": tuple(refused),
    }


def mcx_equivalence_rows() -> dict[str, int]:
    rows = failures = scratch_failures = 0
    for controls_count in (3, 4):
        controls = tuple(range(controls_count))
        target = controls_count
        scratch = tuple(
            range(controls_count + 1, controls_count + 1 + controls_count - 2)
        )
        expanded = expand_mcx(controls, target, scratch)
        for basis in range(1 << (controls_count + 1)):
            source = {
                wire: 1
                for wire in range(controls_count + 1)
                if (basis >> wire) & 1
            }
            direct = apply_word(source, (mcx(controls, target),))
            observed = apply_word(source, expanded)
            rows += 1
            failures += observed != direct
            scratch_failures += any(observed.get(wire, 0) for wire in scratch)
    return {
        "rows": rows,
        "failures": failures,
        "scratch_return_failures": scratch_failures,
    }


def syndrome_or_rows() -> dict[str, int]:
    rows = failures = 0
    b_wire, work, syndrome = 0, 1, 2
    compute = (
        cn(b_wire, syndrome),
        cn(work, syndrome),
        tof(b_wire, work, syndrome),
    )
    for b_value in (0, 1):
        for work_value in (0, 1):
            source = {}
            if b_value:
                source[b_wire] = 1
            if work_value:
                source[work] = 1
            observed = apply_word(source, compute)
            rows += 1
            failures += observed.get(syndrome, 0) != int(
                bool(b_value or work_value)
            )
    return {"rows": rows, "failures": failures}


def two_bank_fixture() -> tuple[
    tuple[object, ...],
    tuple[int, ...],
    dict[int, int],
]:
    program = K.interleaved_program(2)
    banks, links = K.B.chain_genesis(2)
    prepared = K.M.prepare_endpoint(K.M.pack_state(banks, links), (1, 0))
    return program, prepared, bit_state(prepared)


def sandwich_semantics() -> dict[str, object]:
    program, prepared, source_data = two_bank_fixture()
    data_width = len(prepared)
    wrapped_word, wrapped_layout = controller_word(
        program, data_width, wrapped=True
    )
    unwrapped_word, unwrapped_layout = controller_word(
        program, data_width, wrapped=False
    )
    stations = len(program)

    wrapped_source = dict(source_data)
    add_register_bit(wrapped_source, wrapped_layout, "A", 0)
    unwrapped_source = dict(source_data)
    add_register_bit(unwrapped_source, unwrapped_layout, "A", 0)
    wrapped_output = apply_word(wrapped_source, wrapped_word, stations)
    unwrapped_output = apply_word(unwrapped_source, unwrapped_word, stations)
    host = independent_host_orbit(source_data, program)

    lawful_data_equal = (
        data_projection(wrapped_output, data_width)
        == data_projection(unwrapped_output, data_width)
        == host["data"]
    )
    lawful_register_return = (
        projected_state(
            wrapped_output, wrapped_layout["a_base"], stations
        ) == (1,) + (0,) * (stations - 1)
        and not any(projected_state(
            wrapped_output, wrapped_layout["b_base"], stations
        ))
        and not any(projected_state(
            wrapped_output, wrapped_layout["work_base"], stations
        ))
        and not any(projected_state(
            wrapped_output, wrapped_layout["syndrome_base"], stations
        ))
        and not any(projected_state(
            wrapped_output,
            wrapped_layout["scratch_base"],
            SCRATCH_PER_STATION * stations,
        ))
        and projected_state(
            unwrapped_output, unwrapped_layout["a_base"], stations
        ) == (1,) + (0,) * (stations - 1)
        and not any(projected_state(
            unwrapped_output, unwrapped_layout["b_base"], stations
        ))
        and not any(projected_state(
            unwrapped_output, unwrapped_layout["work_base"], stations
        ))
    )

    dirt_cases = dirt_survival_failures = auxiliary_failures = 0
    prediction_mismatches = rail_prediction_mismatches = 0
    refusal_events = refusal_event_failures = 0
    for station in range(stations):
        for dirt_kind in ("B", "work"):
            source = dict(source_data)
            add_register_bit(source, wrapped_layout, "A", 0)
            add_register_bit(source, wrapped_layout, dirt_kind, station)
            observed = apply_word(source, wrapped_word, stations)
            expected = independent_host_orbit(
                source_data,
                program,
                b_station=station if dirt_kind == "B" else None,
                work_station=station if dirt_kind == "work" else None,
            )
            observed_a = projected_state(
                observed, wrapped_layout["a_base"], stations
            )
            observed_b = projected_state(
                observed, wrapped_layout["b_base"], stations
            )
            observed_work = projected_state(
                observed, wrapped_layout["work_base"], stations
            )
            observed_syndrome = projected_state(
                observed, wrapped_layout["syndrome_base"], stations
            )
            observed_scratch = projected_state(
                observed,
                wrapped_layout["scratch_base"],
                SCRATCH_PER_STATION * stations,
            )
            expected_b = tuple(
                int(dirt_kind == "B" and index == station)
                for index in range(stations)
            )
            expected_work = tuple(
                int(dirt_kind == "work" and index == station)
                for index in range(stations)
            )
            dirt_cases += 1
            dirt_survival_failures += observed_b != expected_b
            dirt_survival_failures += observed_work != expected_work
            auxiliary_failures += any(observed_syndrome) or any(observed_scratch)
            prediction_mismatches += (
                data_projection(observed, data_width) != expected["data"]
            )
            rail_prediction_mismatches += (
                observed_a != expected["A"]
                or observed_b != expected["B"]
                or observed_work != expected["work"]
            )
            refusal_events += len(expected["refused"])
            refusal_event_failures += len(expected["refused"]) != 1

    mcx_rows = mcx_equivalence_rows()
    or_rows = syndrome_or_rows()
    nonidentity = sum(bool(K.mapped_macro(row)) for row in program)
    passed = (
        stations == 11
        and nonidentity == 11
        and lawful_data_equal
        and lawful_register_return
        and dirt_cases == 2 * stations == 22
        and dirt_survival_failures == 0
        and auxiliary_failures == 0
        and prediction_mismatches == 0
        and rail_prediction_mismatches == 0
        and refusal_events == dirt_cases
        and refusal_event_failures == 0
        and mcx_rows["failures"] == 0
        and mcx_rows["scratch_return_failures"] == 0
        and or_rows["failures"] == 0
    )
    return {
        "pass": passed,
        "banks": 2,
        "program_stations": stations,
        "nonidentity_stations": nonidentity,
        "data_width": data_width,
        "wrapped_H_gates": len(wrapped_word),
        "unwrapped_H_gates": len(unwrapped_word),
        "lawful_wrapped_unwrapped_host_data_equal": lawful_data_equal,
        "lawful_all_registers_return": lawful_register_return,
        "dirt_cases_tested": dirt_cases,
        "refusal_events_predicted": refusal_events,
        "dirt_survival_failures": dirt_survival_failures,
        "syndrome_scratch_return_failures": auxiliary_failures,
        "identity_substituted_prediction_mismatches": prediction_mismatches,
        "rail_prediction_mismatches": rail_prediction_mismatches,
        "refusal_event_census_failures": refusal_event_failures,
        "syndrome_OR_truth_table": or_rows,
        "MCX_direct_vs_clean_ladder": mcx_rows,
    }


def inverse_certificate() -> dict[str, object]:
    program, prepared, _source_data = two_bank_fixture()
    data_width = len(prepared)
    word, layout = controller_word(program, data_width, wrapped=True)
    inverse = tuple(reversed(word))
    active_data_wires = tuple(sorted({
        wire
        for row in program
        for gate in K.mapped_macro(row)
        for wire in gate.wires
    }))[:5]
    rows = failures = 0
    for basis in range(1 << 5):
        source = {
            wire: 1
            for index, wire in enumerate(active_data_wires)
            if (basis >> index) & 1
        }
        add_register_bit(source, layout, "A", 0)
        observed = apply_word(source, word, len(program))
        restored = apply_word(observed, inverse, len(program))
        rows += 1
        failures += restored != source
    return {
        "pass": (
            len(active_data_wires) == 5
            and rows == 32
            and failures == 0
        ),
        "basis_scope": (
            "exhaustive 32 states on five macro-touched data wires through "
            f"the full H^{len(program)} two-bank orbit, embedded in the "
            f"full {layout['full_width']}-wire wrapped register"
        ),
        "reduced_data_width": 5,
        "sampled_active_data_wires": active_data_wires,
        "full_data_width": data_width,
        "full_register_width": layout["full_width"],
        "forward_H_applications": len(program),
        "inverse_reversed_H_applications": len(program),
        "basis_rows": rows,
        "restoration_failures": failures,
        "inverse_construction": "tuple(reversed(wrapped_word))",
    }


def module_assignment(tree: ast.Module, name: str) -> ast.AST:
    values = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets = node.targets
            value = node.value
        elif isinstance(node, ast.AnnAssign):
            targets = (node.target,)
            value = node.value
        else:
            continue
        if value is not None and any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            values.append(value)
    if len(values) != 1:
        raise ValueError(("module assignment", name, len(values)))
    return values[0]


def assignment_targets(node: ast.AST) -> tuple[ast.AST, ...]:
    if isinstance(node, (ast.Tuple, ast.List)):
        return tuple(
            child
            for element in node.elts
            for child in assignment_targets(element)
        )
    return (node,)


def attribute_root(node: ast.AST) -> str | None:
    while isinstance(node, (ast.Attribute, ast.Subscript)):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def branch_kind(node: ast.If) -> str | None:
    test = node.test
    if not (
        isinstance(test, ast.Compare)
        and len(test.ops) == 1
        and isinstance(test.ops[0], ast.Eq)
        and len(test.comparators) == 1
        and isinstance(test.left, ast.Attribute)
        and isinstance(test.left.value, ast.Name)
        and test.left.value.id == "gate"
        and test.left.attr == "kind"
        and isinstance(test.comparators[0], ast.Constant)
        and isinstance(test.comparators[0].value, str)
    ):
        return None
    return test.comparators[0].value


def called_a_function(call: ast.Call, name: str) -> bool:
    return (
        isinstance(call.func, ast.Attribute)
        and isinstance(call.func.value, ast.Name)
        and call.func.value.id == "A"
        and call.func.attr == name
    )


def name_is(node: ast.AST, name: str) -> bool:
    return isinstance(node, ast.Name) and node.id == name


def lift_branch_guards(function: ast.FunctionDef) -> dict[str, object]:
    loops = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.For)
        and isinstance(node.target, ast.Name)
        and node.target.id == "gate"
        and isinstance(node.iter, ast.Name)
        and node.iter.id == "word"
    ]
    if len(loops) != 1:
        raise ValueError(("gate lift loops", len(loops)))
    loop_scope = ast.Module(body=loops[0].body, type_ignores=[])
    branches: dict[str, ast.If] = {}
    for node in ast.walk(loop_scope):
        if isinstance(node, ast.If):
            kind = branch_kind(node)
            if kind in {"X", "CNOT", "TOF"}:
                if kind in branches:
                    raise ValueError(("duplicate lift branch", kind))
                branches[kind] = node

    details = {}
    expected = {
        "X": ("tof", 2),
        "CNOT": ("mcx", 3),
        "TOF": ("mcx", 4),
    }
    for kind, (function_name, control_count) in expected.items():
        branch = branches.get(kind)
        calls = []
        if branch is not None:
            body_scope = ast.Module(body=branch.body, type_ignores=[])
            calls = [
                call
                for call in ast.walk(body_scope)
                if isinstance(call, ast.Call)
                and called_a_function(call, function_name)
            ]
        guarded = False
        if len(calls) == 1:
            call = calls[0]
            if kind == "X":
                guarded = (
                    len(call.args) >= 2
                    and name_is(call.args[0], "control")
                    and name_is(call.args[1], "syndrome")
                )
            else:
                controls = call.args[0] if call.args else None
                guarded = (
                    isinstance(controls, ast.Tuple)
                    and len(controls.elts) == control_count
                    and name_is(controls.elts[0], "control")
                    and name_is(controls.elts[1], "syndrome")
                )
        details[kind] = {
            "branch_present": branch is not None,
            "lift_call": function_name,
            "expected_control_count": control_count,
            "NOT_syndrome_control_present": guarded,
        }
    return details


def primary_source_discipline() -> dict[str, object]:
    source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)
    audit_node = module_assignment(tree, "AUDIT_INPUT_PATHS")
    audit_error = None
    audit_value = None
    try:
        audit_value = ast.literal_eval(audit_node)
    except (ValueError, TypeError) as exc:
        audit_error = f"{type(exc).__name__}: {exc}"
    audit_literal_tuple = (
        isinstance(audit_node, ast.Tuple)
        and isinstance(audit_value, tuple)
    )
    forbidden_classes = [
        node.name
        for node in ast.walk(tree)
        if isinstance(node, ast.ClassDef)
        and node.name in {"JointOrder", "EventChain"}
    ]

    attribute_assignments = []
    for node in ast.walk(tree):
        targets: tuple[ast.AST, ...] = ()
        if isinstance(node, ast.Assign):
            targets = tuple(
                target
                for raw in node.targets
                for target in assignment_targets(raw)
            )
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            targets = assignment_targets(node.target)
        for target in targets:
            if (
                isinstance(target, ast.Attribute)
                and attribute_root(target) in {"K", "R719"}
            ):
                attribute_assignments.append({
                    "line": target.lineno,
                    "target": ast.unparse(target),
                })
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "setattr"
            and node.args
            and attribute_root(node.args[0]) in {"K", "R719"}
        ):
            attribute_assignments.append({
                "line": node.lineno,
                "target": ast.unparse(node),
            })

    functions = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "refusing_controlled_macro"
    ]
    if len(functions) != 1:
        raise ValueError(("refusing_controlled_macro definitions", len(functions)))
    branch_details = lift_branch_guards(functions[0])
    branch_pass = set(branch_details) == {"X", "CNOT", "TOF"} and all(
        row["branch_present"] and row["NOT_syndrome_control_present"]
        for row in branch_details.values()
    )
    blocked_present = sorted(TOP_LEVEL_BLOCKLIST & set(sys.modules))
    passed = (
        audit_literal_tuple
        and not forbidden_classes
        and not attribute_assignments
        and branch_pass
        and not blocked_present
    )
    return {
        "pass": passed,
        "AUDIT_INPUT_PATHS_literal_tuple": audit_literal_tuple,
        "AUDIT_INPUT_PATHS_literal_value": audit_value,
        "AUDIT_INPUT_PATHS_literal_error": audit_error,
        "forbidden_class_definitions": forbidden_classes,
        "attribute_assignments_onto_K_or_R719": attribute_assignments,
        "refusing_controlled_macro_lift_branches": branch_details,
        "all_three_gate_kinds_NOT_syndrome_guarded": branch_pass,
        "blocked_primary_imports_present": blocked_present,
    }


def count_consistency() -> dict[str, object]:
    program, track = K.held_physical_program_and_track(12)
    census: Counter[str] = Counter()
    nonidentity = 0
    row_gate_counts = []
    for station, row in enumerate(program):
        macro = K.mapped_macro(row)
        nonidentity += bool(macro)
        row_gate_counts.append(len(macro))
        census.update(gate.kind for gate in macro)

    unknown_kinds = sorted(set(census) - {"X", "CNOT", "TOF"})
    shell_per_nonidentity = 3 + 1 + 1 + 3
    shell_gates = shell_per_nonidentity * nonidentity
    lifted_x = census["X"]
    lifted_cnot = mcx_expansion_size(3) * census["CNOT"]
    lifted_tof = mcx_expansion_size(4) * census["TOF"]
    rail_swaps = 2 * len(program)
    rail_gates = 3 * rail_swaps
    rebuilt = (
        shell_gates + lifted_x + lifted_cnot + lifted_tof + rail_gates
    )
    passed = (
        len(program) == 130
        and len(track) == 260
        and nonidentity == 91
        and not unknown_kinds
        and rebuilt == EXPECTED_WRAPPED_130_WORD_SIZE
    )
    return {
        "pass": passed,
        "stations": len(program),
        "track_sites": len(track),
        "nonidentity_stations": nonidentity,
        "identity_stations": len(program) - nonidentity,
        "program_row_gate_total": sum(row_gate_counts),
        "program_gate_census": dict(sorted(census.items())),
        "unknown_gate_kinds": unknown_kinds,
        "sandwich_shell": {
            "gates_per_nonidentity_station": shell_per_nonidentity,
            "subtotal": shell_gates,
        },
        "lifted_X_subtotal": lifted_x,
        "lifted_CNOT_subtotal": lifted_cnot,
        "lifted_TOF_subtotal": lifted_tof,
        "MCX_expansion_sizes": {
            "three_controls": mcx_expansion_size(3),
            "four_controls": mcx_expansion_size(4),
        },
        "rail_swaps": rail_swaps,
        "rail_gates": rail_gates,
        "formula": (
            f"{shell_gates} + {lifted_x} + {lifted_cnot} + "
            f"{lifted_tof} + {rail_gates} = {rebuilt}"
        ),
        "rebuilt_wrapped_word_size": rebuilt,
        "expected_primary_report_cross_check": EXPECTED_WRAPPED_130_WORD_SIZE,
    }


def check(label: str, condition: bool, detail: object = "") -> None:
    passed = bool(condition)
    CHECKS.append({"label": label, "pass": passed, "detail": detail})
    print("PASS" if passed else "FAIL", label)


def run_certificate(
    label: str,
    function: Callable[[], dict[str, object]],
) -> dict[str, object]:
    try:
        result = function()
    except Exception as exc:
        result = {
            "pass": False,
            "error": f"{type(exc).__name__}: {exc}",
        }
    check(label, bool(result.get("pass")), result)
    return result


def main() -> int:
    started = perf_counter()
    sandwich = run_certificate("sandwich_semantics", sandwich_semantics)
    inverse = run_certificate("inverse_certificate", inverse_certificate)
    discipline = run_certificate(
        "primary_source_discipline", primary_source_discipline
    )
    counts = run_certificate("count_consistency", count_consistency)

    passing = all(row["pass"] for row in CHECKS)
    report = {
        "status": "PASS" if passing else "FAIL",
        "authority": "none",
        "audit": "unset",
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "top_level_blocklist": sorted(TOP_LEVEL_BLOCKLIST),
        "blocked_primary_imports_present": sorted(
            TOP_LEVEL_BLOCKLIST & set(sys.modules)
        ),
        "checks": CHECKS,
        "certificates": {
            "sandwich_semantics": sandwich,
            "inverse_certificate": inverse,
            "primary_source_discipline": discipline,
            "count_consistency": counts,
        },
        "runtime_seconds": perf_counter() - started,
    }
    report["report_sha256"] = sha256(json.dumps(
        report,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()).hexdigest()
    print(json.dumps(report, indent=2, sort_keys=True))
    print(
        "REFUSAL_WRAPPED_CONTROLLER_INDEPENDENT_CHECK_PASS"
        if passing
        else "REFUSAL_WRAPPED_CONTROLLER_INDEPENDENT_CHECK_FAIL"
    )
    return 0 if passing else 1


if __name__ == "__main__":
    raise SystemExit(main())
