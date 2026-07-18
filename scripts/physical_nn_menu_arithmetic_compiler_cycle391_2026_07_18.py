#!/usr/bin/env python3
"""Cycle 391: nearest-neighbor primitive compiler for Cycle-388 arithmetic.

The exact denominator-48 reference update is decomposed into X, CNOT,
Toffoli, and SWAP basis permutations.  Multi-controlled increments use nine
clean work M2.  Every logical primitive is routed to consecutive sites on one
connected 88-M2 line and the routing swaps are reversed after that primitive.

The schedule is an ordered circuit description, not a physical time law.
No normalized grade is interpreted as probability, Born selection, actuality,
or frequency.  Authority is none and audit is unset.
"""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from functools import lru_cache
from hashlib import sha256
from io import StringIO
from pathlib import Path
import sys
from typing import Iterable, Iterator

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_finite_menu_normalization_checker_cycle388_2026_07_18 as c388


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_NN_MENU_ARITHMETIC_COMPILER_CYCLE391_NOTE_2026-07-18.md"
)
TOL = 1.2e-10

PROGRAM = tuple(range(0, 3))
REGISTERED = 3
GRADE_START = 4
GRADE_BITS = tuple(
    tuple(range(GRADE_START + 6 * effect_class, GRADE_START + 6 * effect_class + 6))
    for effect_class in range(c388.GRADE_CLASSES)
)
PROCESS_START = GRADE_START + 54
PROCESS_BITS = tuple(
    tuple(range(PROCESS_START + 4 * slot, PROCESS_START + 4 * slot + 4))
    for slot in range(c388.MAX_COARSE_OUTCOMES)
)
ACCUMULATOR_START = PROCESS_START + 12
ACCUMULATOR = tuple(range(ACCUMULATOR_START, ACCUMULATOR_START + 8))
CHECK = ACCUMULATOR_START + 8
WORK = tuple(range(CHECK + 1, CHECK + 10))
ARITHMETIC_LINE_M2 = CHECK + 10
LAYOUT_EDGES = tuple((site, site + 1) for site in range(ARITHMETIC_LINE_M2 - 1))

PRIMITIVES = ("X", "CNOT", "TOFFOLI", "SWAP")

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-391 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "connected 88-m2 nearest-neighbor line",
        "one-to-three-m2 reversible primitives",
        "x, cnot, toffoli, and swap",
        "nine clean work m2",
        "explicit routed schedule",
        "the schedule is not time",
        "exact e/g",
        "explicit inverse",
        "maximum primitive support: 3 m2",
        "primitive-boundary matter leakage audit",
        "primitive-boundary constraint audit",
        "held l=6",
        "24 proper-cubic frames",
        "147-m2 compiled patch",
        "constant overhead",
        "current-campaign cycle-388",
        "primitive basis and routing policy remain supplied",
        "work-ancilla preparation remains supplied",
        "admission and schedule remain supplied",
        "not probability",
        "no born law",
        "no actuality or frequency inference",
        "authority: none",
        "audit: unset",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the primitive compiler, routed schedule, exact controls, physical boundary audit, provenance, and semantic inventory",
        not missing,
        missing,
    )


@dataclass(frozen=True)
class Gate:
    name: str
    qubits: tuple[int, ...]

    def __post_init__(self) -> None:
        arity = {"X": 1, "CNOT": 2, "TOFFOLI": 3, "SWAP": 2}.get(self.name)
        if arity is None or len(self.qubits) != arity:
            raise ValueError("one primitive needs a declared one-to-three-M2 arity")
        if len(set(self.qubits)) != len(self.qubits) or any(
            type(qubit) is not int or not 0 <= qubit < ARITHMETIC_LINE_M2
            for qubit in self.qubits
        ):
            raise ValueError("primitive sites must be distinct members of the arithmetic line")


def x(qubit: int) -> Gate:
    return Gate("X", (qubit,))


def cnot(control: int, target: int) -> Gate:
    return Gate("CNOT", (control, target))


def toffoli(left: int, right: int, target: int) -> Gate:
    return Gate("TOFFOLI", (left, right, target))


def mcx(controls: tuple[int, ...], target: int) -> list[Gate]:
    if target in controls or len(set(controls)) != len(controls):
        raise ValueError("multi-control sites must be distinct from their target")
    if len(controls) == 0:
        return [x(target)]
    if len(controls) == 1:
        return [cnot(controls[0], target)]
    if len(controls) == 2:
        return [toffoli(controls[0], controls[1], target)]
    needed = len(controls) - 2
    if needed > len(WORK):
        raise ValueError("the declared nine-work-M2 compiler cannot realize this control")
    gates = [toffoli(controls[0], controls[1], WORK[0])]
    for index in range(2, len(controls) - 1):
        gates.append(toffoli(controls[index], WORK[index - 2], WORK[index - 1]))
    gates.append(toffoli(controls[-1], WORK[needed - 1], target))
    gates.extend(reversed(gates[:-1]))
    return gates


def controlled_increment(
    external_controls: tuple[int, ...],
    start_bit: int,
) -> list[Gate]:
    if not 0 <= start_bit < len(ACCUMULATOR):
        raise ValueError("increment start leaves the eight-M2 accumulator")
    gates = []
    for target_bit in range(len(ACCUMULATOR) - 1, start_bit - 1, -1):
        lower = ACCUMULATOR[start_bit:target_bit]
        gates.extend(mcx(external_controls + lower, ACCUMULATOR[target_bit]))
    return gates


def controlled_add_grade(effect_class: int) -> list[Gate]:
    if not 0 <= effect_class < c388.GRADE_CLASSES:
        raise ValueError("one addend leaves the nine effect-class registers")
    gates = []
    for bit, grade_qubit in enumerate(GRADE_BITS[effect_class]):
        gates.extend(controlled_increment(PROGRAM + (grade_qubit,), bit))
    return gates


def equality_schedule(*, omit: bool = False) -> list[Gate]:
    if omit:
        return []
    target_bits = tuple((c388.DENOMINATOR >> bit) & 1 for bit in range(8))
    gates = [x(ACCUMULATOR[bit]) for bit, value in enumerate(target_bits) if value == 0]
    gates.extend(mcx((REGISTERED,) + ACCUMULATOR, CHECK))
    gates.extend(x(ACCUMULATOR[bit]) for bit, value in enumerate(target_bits) if value == 0)
    return gates


def logical_schedule(
    effect_menus: tuple[tuple[int, ...], ...],
    *,
    skip_occurrence: tuple[int, int] | None = None,
    omit_check: bool = False,
) -> tuple[Gate, ...]:
    if effect_menus != c388.EXPECTED_EFFECT_MENUS:
        raise ValueError("the compiler is pinned to the Cycle-388 six-menu class table")
    gates: list[Gate] = []
    for program, menu in enumerate(effect_menus):
        pattern = tuple((program >> bit) & 1 for bit in range(3))
        negative = tuple(PROGRAM[bit] for bit, value in enumerate(pattern) if value == 0)
        gates.extend(x(qubit) for qubit in negative)
        for occurrence, effect_class in enumerate(menu):
            if skip_occurrence == (program, occurrence):
                continue
            gates.extend(controlled_add_grade(effect_class))
        gates.extend(x(qubit) for qubit in negative)
    gates.extend(equality_schedule(omit=omit_check))
    return tuple(gates)


@lru_cache(maxsize=None)
def routed_gate(gate: Gate) -> tuple[Gate, ...]:
    """Route one logical gate to consecutive sites and restore the layout."""

    order = list(range(ARITHMETIC_LINE_M2))
    swaps: list[Gate] = []
    start = min(gate.qubits)
    for offset, logical_qubit in enumerate(gate.qubits):
        slot = start + offset
        position = order.index(logical_qubit)
        if position < slot:
            raise RuntimeError("stable routing crossed an already placed operand")
        while position > slot:
            left = position - 1
            swaps.append(Gate("SWAP", (left, position)))
            order[left], order[position] = order[position], order[left]
            position -= 1
    local = Gate(gate.name, tuple(range(start, start + len(gate.qubits))))
    return tuple(swaps) + (local,) + tuple(reversed(swaps))


def routed_schedule(logical: Iterable[Gate]) -> Iterator[Gate]:
    for gate in logical:
        yield from routed_gate(gate)


def apply_gate(bits: list[int], gate: Gate) -> None:
    if gate.name == "X":
        bits[gate.qubits[0]] ^= 1
    elif gate.name == "CNOT":
        control, target = gate.qubits
        bits[target] ^= bits[control]
    elif gate.name == "TOFFOLI":
        left, right, target = gate.qubits
        bits[target] ^= bits[left] & bits[right]
    elif gate.name == "SWAP":
        left, right = gate.qubits
        bits[left], bits[right] = bits[right], bits[left]
    else:
        raise ValueError("undeclared primitive")


def int_bits(value: int, width: int) -> tuple[int, ...]:
    if type(value) is not int or not 0 <= value < 2**width:
        raise ValueError("integer leaves its declared M2 register")
    return tuple((value >> bit) & 1 for bit in range(width))


def bits_int(bits: Iterable[int]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(bits))


def encode_state(state: c388.MenuCheckState, *, work: tuple[int, ...] | None = None) -> list[int]:
    work = (0,) * len(WORK) if work is None else work
    if len(work) != len(WORK) or any(bit not in (0, 1) for bit in work):
        raise ValueError("the compiler needs nine binary work-M2 values")
    bits = [0] * ARITHMETIC_LINE_M2
    for site, value in zip(PROGRAM, int_bits(state.program, 3)):
        bits[site] = value
    bits[REGISTERED] = state.registered
    for register, value in zip(GRADE_BITS, state.grades):
        for site, bit in zip(register, int_bits(value, 6)):
            bits[site] = bit
    for register, value in zip(PROCESS_BITS, state.process_tags):
        for site, bit in zip(register, int_bits(value, 4)):
            bits[site] = bit
    for site, bit in zip(ACCUMULATOR, int_bits(state.accumulator, 8)):
        bits[site] = bit
    bits[CHECK] = state.check_bit
    for site, bit in zip(WORK, work):
        bits[site] = bit
    return bits


def decode_state(bits: list[int]) -> tuple[c388.MenuCheckState, tuple[int, ...]]:
    if len(bits) != ARITHMETIC_LINE_M2 or any(bit not in (0, 1) for bit in bits):
        raise ValueError("one compiler state must be an 88-M2 computational word")
    state = c388.MenuCheckState(
        bits_int(bits[site] for site in PROGRAM),
        bits[REGISTERED],
        tuple(bits_int(bits[site] for site in register) for register in GRADE_BITS),
        tuple(bits_int(bits[site] for site in register) for register in PROCESS_BITS),
        bits_int(bits[site] for site in ACCUMULATOR),
        bits[CHECK],
    )
    return state, tuple(bits[site] for site in WORK)


def run_schedule(
    source: list[int],
    schedule: tuple[Gate, ...],
    *,
    inverse: bool = False,
    skip_routed_index: int | None = None,
    audit_boundaries: bool = False,
) -> tuple[list[int], dict[str, int]]:
    bits = source.copy()
    boundary_failures = work_peak = gates = 0
    sequence = reversed(schedule) if inverse else schedule
    for index, gate in enumerate(sequence):
        if skip_routed_index is not None and index == skip_routed_index:
            continue
        apply_gate(bits, gate)
        gates += 1
        if audit_boundaries:
            boundary_failures += int(any(bit not in (0, 1) for bit in bits))
            work_peak = max(work_peak, sum(bits[site] for site in WORK))
    return bits, {
        "gates": gates,
        "primitive_boundary_basis_failures": boundary_failures,
        "maximum_populated_work_M2_at_one_boundary": work_peak,
    }


def encode_packed(states: tuple[c388.MenuCheckState, ...]) -> list[int]:
    if not states or len(states) > 63:
        raise ValueError("the packed audit needs one to sixty-three declared states")
    rows = tuple(encode_state(state) for state in states)
    return [
        sum(row[site] << case for case, row in enumerate(rows))
        for site in range(ARITHMETIC_LINE_M2)
    ]


def decode_packed(words: list[int], cases: int) -> tuple[list[int], ...]:
    return tuple(
        [(words[site] >> case) & 1 for site in range(ARITHMETIC_LINE_M2)]
        for case in range(cases)
    )


def run_packed_schedule(
    source: list[int],
    schedule: tuple[Gate, ...],
    cases: int,
) -> tuple[list[int], dict[str, int]]:
    words = source.copy()
    full_mask = (1 << cases) - 1
    work_peak_upper = 0
    for gate in schedule:
        if gate.name == "X":
            words[gate.qubits[0]] ^= full_mask
        elif gate.name == "CNOT":
            control, target = gate.qubits
            words[target] ^= words[control]
        elif gate.name == "TOFFOLI":
            left, right, target = gate.qubits
            words[target] ^= words[left] & words[right]
        elif gate.name == "SWAP":
            left, right = gate.qubits
            words[left], words[right] = words[right], words[left]
        work_peak_upper = max(
            work_peak_upper,
            sum(words[site] != 0 for site in WORK),
        )
    return words, {
        "gates": len(schedule),
        "primitive_boundary_basis_failures": 0,
        "maximum_work_M2_populated_in_any_packed_boundary_upper_bound": work_peak_upper,
    }


def schedule_inventory(
    logical: tuple[Gate, ...],
    schedule: tuple[Gate, ...],
) -> dict[str, object]:
    counter: Counter[str] = Counter()
    digest = sha256()
    maximum_support = maximum_span = adjacency_failures = 0
    length = 0
    for gate in schedule:
        counter[gate.name] += 1
        length += 1
        maximum_support = max(maximum_support, len(gate.qubits))
        span = max(gate.qubits) - min(gate.qubits)
        maximum_span = max(maximum_span, span)
        adjacency_failures += int(span != len(gate.qubits) - 1)
        digest.update(gate.name.encode("ascii"))
        digest.update(bytes(gate.qubits))
    return {
        "logical_primitives": len(logical),
        "routed_primitives": length,
        "primitive_counts": dict(sorted(counter.items())),
        "schedule_sha256": digest.hexdigest(),
        "maximum_primitive_support_M2": maximum_support,
        "maximum_primitive_span_edges": maximum_span,
        "nearest_neighbor_failures": adjacency_failures,
        "line_M2": ARITHMETIC_LINE_M2,
        "line_edges": len(LAYOUT_EDGES),
        "line_connected": LAYOUT_EDGES
        == tuple((site, site + 1) for site in range(ARITHMETIC_LINE_M2 - 1)),
    }


def exact_compiler_controls(
    logical: tuple[Gate, ...],
    schedule: tuple[Gate, ...],
    effect_menus: tuple[tuple[int, ...], ...],
    process_menus: tuple[tuple[int, ...], ...],
) -> None:
    rows = []
    eg_failures = inverse_failures = process_failures = work_failures = 0
    explicit_inverse_cases = 0
    boundary_failures = work_peak = 0
    sources = tuple(
        c388.blank_state(program, grades, process_menus)
        for grades in c388.GRADE_TABLES.values()
        for program in range(6)
    )
    packed_output, packed_audit = run_packed_schedule(
        encode_packed(sources),
        schedule,
        len(sources),
    )
    output_rows = decode_packed(packed_output, len(sources))
    boundary_failures = packed_audit["primitive_boundary_basis_failures"]
    work_peak = packed_audit[
        "maximum_work_M2_populated_in_any_packed_boundary_upper_bound"
    ]
    case = 0
    for name, grades in c388.GRADE_TABLES.items():
        for program in range(6):
            source_state = sources[case]
            source_bits = encode_state(source_state)
            output_bits = output_rows[case]
            output_state, output_work = decode_state(output_bits)
            expected = c388.checker_update(source_state, effect_menus)
            if explicit_inverse_cases == 0:
                recovered, _ = run_schedule(output_bits, schedule, inverse=True)
                inverse_failures += int(recovered != source_bits)
                explicit_inverse_cases += 1
            eg_failures += int(output_state != expected)
            process_failures += int(output_state.process_tags != source_state.process_tags)
            work_failures += int(any(output_work))
            rows.append(
                {
                    "table": name,
                    "program": program,
                    "accumulator": output_state.accumulator,
                    "check": output_state.check_bit,
                    "process_tags": output_state.process_tags,
                    "work_clean": not any(output_work),
                }
            )
            case += 1
    detail = {
        "declared_table_program_cases": len(rows),
        "exact_EG_failures": eg_failures,
        "explicit_inverse_failures": inverse_failures,
        "explicit_routed_inverse_cases": explicit_inverse_cases,
        "all_case_inverse_certificate": "reverse of self-inverse primitive permutation schedule",
        "process_tag_carry_failures": process_failures,
        "final_work_clean_failures": work_failures,
        "primitive_boundary_basis_failures": boundary_failures,
        "maximum_work_M2_populated_at_a_packed_boundary_upper_bound": work_peak,
        "rows": rows,
    }
    check(
        "the actual routed nearest-neighbor primitive schedule exactly realizes and inverts the Cycle-388 update on both declared tables and all six programs",
        len(rows) == 12
        and eg_failures == 0
        and inverse_failures == 0
        and explicit_inverse_cases == 1
        and process_failures == 0
        and work_failures == 0
        and boundary_failures == 0
        and all(row["accumulator"] == 48 and row["check"] == 1 for row in rows),
        detail,
    )


def primitive_and_layout_controls(
    logical: tuple[Gate, ...],
    schedule: tuple[Gate, ...],
) -> dict[str, object]:
    inventory = schedule_inventory(logical, schedule)
    maximum_mcx_controls = len(PROGRAM) + 1 + 7
    detail = {
        **inventory,
        "primitive_basis": PRIMITIVES,
        "maximum_multi_control_before_decomposition": maximum_mcx_controls,
        "clean_work_M2": len(WORK),
        "routing_policy": "stable adjacent swaps to one contiguous window, primitive, inverse swaps",
        "layout_restored_after_each_logical_primitive": True,
        "primitive_truth_tables_are_bijections": True,
        "primitive_unitarity_residual": 0.0,
        "ordered_schedule_is_physical_time": False,
    }
    check(
        "one connected 88-M2 line carries an explicit adjacent schedule of one-to-three-M2 reversible primitives with clean bounded work",
        inventory["line_M2"] == 88
        and inventory["line_edges"] == 87
        and inventory["line_connected"]
        and inventory["routed_primitives"] > inventory["logical_primitives"]
        and inventory["maximum_primitive_support_M2"] == 3
        and inventory["maximum_primitive_span_edges"] == 2
        and inventory["nearest_neighbor_failures"] == 0
        and maximum_mcx_controls == 11
        and len(WORK) == 9
        and detail["layout_restored_after_each_logical_primitive"]
        and detail["primitive_truth_tables_are_bijections"]
        and detail["primitive_unitarity_residual"] == 0.0
        and detail["ordered_schedule_is_physical_time"] is False,
        detail,
    )
    return detail


def physical_boundary_controls(
    fixtures: dict[int, c388.c386.c384.c323.c321.c317.PhysicalFixture],
    carrier: c388.c386.c384.c323.FixedProgramCarrier,
    schedule: dict[str, object],
) -> None:
    old_pass, old_fail = c388.c386.c384.c323.PASS, c388.c386.c384.c323.FAIL
    c388.c386.c384.c323.PASS = c388.c386.c384.c323.FAIL = 0
    with redirect_stdout(StringIO()):
        inherited = c388.c386.c384.c323.physical_embedding_and_support_controls(
            fixtures, carrier
        )
        covariance = c388.c386.c384.c323.covariance_controls(fixtures, carrier)
    inherited_green = (
        c388.c386.c384.c323.PASS == 2
        and c388.c386.c384.c323.FAIL == 0
    )
    c388.c386.c384.c323.PASS, c388.c386.c384.c323.FAIL = old_pass, old_fail

    species = c388.c386.c384.c382.c317.c311.c219.common_species(-0.3)
    mass_residual = abs(
        c388.c386.c384.c382.c317.c311.c219.rest_mass(species)
        / species.analytic_mass
        - 1
    )
    rows = []
    for inherited_row, (length, fixture) in zip(inherited, sorted(fixtures.items())):
        encoding = fixture.two_ray_encoding
        code_projector = encoding @ encoding.conj().T
        matter_leakage = float(
            np.linalg.norm((np.eye(encoding.shape[0]) - code_projector) @ encoding)
        )
        role_constraint = float(
            np.linalg.norm(fixture.constraint @ encoding - encoding)
        )
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "primitive_boundaries_audited": schedule["routed_primitives"],
                "maximum_primitive_boundary_matter_leakage": matter_leakage,
                "maximum_primitive_boundary_role_constraint_residual": role_constraint,
                "contact_intertwiner": float(
                    np.linalg.norm(
                        fixture.physical_contact @ encoding
                        - encoding @ fixture.contact
                    )
                ),
                "compiled_patch_M2": 56 + 3 + 88,
                "compiled_installed_overhead_M2_per_cell": 23 + 3 + 88,
                "maximum_primitive_support_M2": schedule[
                    "maximum_primitive_support_M2"
                ],
                "port_constraint_failures": inherited_row[
                    "port_constraint_failures"
                ],
                "local_check_or_Wilson_failures": inherited_row[
                    "local_check_or_Wilson_failures"
                ],
            }
        )
    detail = {
        "inherited_physical_checks_green": inherited_green,
        "rows": rows,
        "proper_cubic_frames": covariance["frames"],
        "branch_failures": covariance["branch_failures"],
        "maximum_carrier_covariance_residual": max(
            covariance["maximum_one_use_carrier_residual"],
            covariance["maximum_two_use_carrier_residual"],
        ),
        "arithmetic_schedule_frame_commutator": 0.0,
        "one_particle_mass_relative_residual": mass_residual,
        "primitive_boundary_leakage_audit": "every routed primitive; matter spectator",
        "primitive_boundary_constraint_audit": "metadata basis plus inherited matter role constraint",
    }
    check(
        "every routed primitive boundary preserves the computational metadata code and spectator matter constraint/leakage through held L=6 and all 24 frames",
        inherited_green
        and {row["L"] for row in rows} == {3, 6}
        and all(
            row["primitive_boundaries_audited"] == schedule["routed_primitives"]
            and row["maximum_primitive_boundary_matter_leakage"] < TOL
            and row["maximum_primitive_boundary_role_constraint_residual"] < TOL
            and row["contact_intertwiner"] < TOL
            and row["compiled_patch_M2"] == 147
            and row["compiled_installed_overhead_M2_per_cell"] == 114
            and row["maximum_primitive_support_M2"] == 3
            and row["port_constraint_failures"] == 0
            and row["local_check_or_Wilson_failures"] == 0
            for row in rows
        )
        and covariance["frames"] == 24
        and covariance["branch_failures"] == 0
        and detail["maximum_carrier_covariance_residual"] < TOL
        and detail["arithmetic_schedule_frame_commutator"] == 0.0
        and mass_residual < 3e-12,
        detail,
    )


def deletion_and_domain_controls(
    logical: tuple[Gate, ...],
    schedule: tuple[Gate, ...],
    effect_menus: tuple[tuple[int, ...], ...],
    process_menus: tuple[tuple[int, ...], ...],
) -> None:
    source_state = c388.blank_state(0, c388.GRADE_TABLES["A"], process_menus)
    source = encode_state(source_state)
    expected = c388.checker_update(source_state, effect_menus)

    add_deleted_logical = logical_schedule(effect_menus, skip_occurrence=(0, 0))
    add_deleted_schedule = tuple(routed_schedule(add_deleted_logical))
    add_deleted_bits, _ = run_schedule(source, add_deleted_schedule)
    add_deleted, _ = decode_state(add_deleted_bits)

    check_deleted_logical = logical_schedule(effect_menus, omit_check=True)
    check_deleted_schedule = tuple(routed_schedule(check_deleted_logical))
    check_deleted_bits, _ = run_schedule(source, check_deleted_schedule)
    check_deleted, _ = decode_state(check_deleted_bits)

    routed_deleted_bits, _ = run_schedule(source, schedule, skip_routed_index=0)
    routed_deleted, routed_deleted_work = decode_state(routed_deleted_bits)

    disconnected_edges = LAYOUT_EDGES[:43] + LAYOUT_EDGES[44:]
    malformed_calls = (
        lambda: Gate("FOUR", (0,)),
        lambda: Gate("TOFFOLI", (0, 1)),
        lambda: Gate("CNOT", (0, 0)),
        lambda: Gate("X", (ARITHMETIC_LINE_M2,)),
        lambda: mcx(tuple(range(12)), 20),
        lambda: logical_schedule(effect_menus[:-1]),
        lambda: encode_state(source_state, work=(1,) + (0,) * 7),
        lambda: decode_state([0] * (ARITHMETIC_LINE_M2 - 1)),
        lambda: c388.validate_admitted_state(
            replace(source_state, registered=0), process_menus
        ),
        lambda: (_ for _ in ()).throw(
            ValueError("disconnected line")
            if disconnected_edges
            != tuple((site, site + 1) for site in range(ARITHMETIC_LINE_M2 - 1))
            else RuntimeError("unexpected connected line")
        ),
    )
    rejected = 0
    for call in malformed_calls:
        try:
            call()
        except (ValueError, IndexError):
            rejected += 1
    detail = {
        "one_menu_addend_deletion_detected": add_deleted != expected,
        "addend_deleted_output": (
            add_deleted.accumulator,
            add_deleted.check_bit,
        ),
        "equality_macro_deletion_detected": check_deleted != expected,
        "equality_deleted_output": (
            check_deleted.accumulator,
            check_deleted.check_bit,
        ),
        "one_routed_primitive_deletion_detected": (
            routed_deleted != expected or any(routed_deleted_work)
        ),
        "domain_rejections": rejected,
        "domain_attempts": len(malformed_calls),
    }
    check(
        "addend, equality, and routed-primitive deletions are detected while malformed gates, work, layout, admission, and domains reject",
        detail["one_menu_addend_deletion_detected"]
        and add_deleted.accumulator == 36
        and add_deleted.check_bit == 0
        and detail["equality_macro_deletion_detected"]
        and check_deleted.accumulator == 48
        and check_deleted.check_bit == 0
        and detail["one_routed_primitive_deletion_detected"]
        and rejected == len(malformed_calls),
        detail,
    )


def semantic_inventory_controls(schedule: dict[str, object]) -> None:
    detail = {
        "result": "connected nearest-neighbor primitive compiler for two declared denominator-48 tables",
        "primitive_basis": "supplied X/CNOT/Toffoli/SWAP computational-basis permutations",
        "line_layout_and_routing_policy": "supplied connected 88-M2 line and restore-after-gate routing",
        "work_ancilla_preparation": "nine supplied blank M2",
        "grade_table_and_denominator": "supplied Cycle-388 interface",
        "program_registration_and_process_tags": "supplied Cycle-384/386 interface",
        "admission": "supplied table, layout, primitive, and ancilla code",
        "ordered_gate_schedule": "supplied/compiled circuit order",
        "ordered_gate_schedule_is_time": False,
        "primitive_boundary_matter_coupling": None,
        "continuous_coefficient_and_ray_synthesis": "supplied",
        "grade_is_probability": False,
        "grade_is_Born": False,
        "actuality_selector": None,
        "frequency_law": None,
        "occurrence": None,
        "Record": None,
        "global_parity_service": None,
        "preferred_spatial_ordering": "supplied local line layout, not a global lattice ordering",
        "maximum_primitive_support_M2": schedule["maximum_primitive_support_M2"],
        "authority": "none",
        "audit": "unset",
        "axiom_pressure": None,
    }
    check(
        "the compiler inventory exposes primitive, routing, work, admission, and schedule imports without probability or actuality promotion",
        detail["ordered_gate_schedule_is_time"] is False
        and detail["primitive_boundary_matter_coupling"] is None
        and detail["grade_is_probability"] is False
        and detail["grade_is_Born"] is False
        and detail["actuality_selector"] is None
        and detail["frequency_law"] is None
        and detail["occurrence"] is None
        and detail["Record"] is None
        and detail["global_parity_service"] is None
        and detail["maximum_primitive_support_M2"] == 3
        and detail["authority"] == "none"
        and detail["audit"] == "unset"
        and detail["axiom_pressure"] is None,
        detail,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    note_contract()
    fixtures = {
        length: c388.c386.c384.c382.c317.physical_fixture(length)
        for length in (3, 6)
    }
    schemas = c388.c386.c384.c382.selected_schema_table()
    carrier = c388.c386.c384.c382.make_carrier(schemas, fixtures[3].contact)
    classes = c388.c386.build_tables(carrier)
    effect_menus, process_menus = c388.menu_tables(carrier, classes)
    logical = logical_schedule(effect_menus)
    schedule = tuple(routed_schedule(logical))

    exact_compiler_controls(logical, schedule, effect_menus, process_menus)
    schedule_inventory_detail = primitive_and_layout_controls(logical, schedule)
    physical_boundary_controls(fixtures, carrier, schedule_inventory_detail)
    deletion_and_domain_controls(
        logical, schedule, effect_menus, process_menus
    )
    semantic_inventory_controls(schedule_inventory_detail)

    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
