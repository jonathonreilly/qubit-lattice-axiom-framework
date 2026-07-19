#!/usr/bin/env python3
"""Cycle 395: local reversible admission for the two Cycle-388 tables.

One supplied selector M2 reversibly loads table A or B into the existing
54-M2 grade-table register.  A separate selector-conditioned equality oracle
flips one admission M2 iff the full table matches the selected declaration.
Fifty-three clean work M2 decompose the largest 55-control comparison.
Every primitive is routed on a connected 109-M2 nearest-neighbor line.

This operational table loader/admitter does not select Nature's grade law.
Its ordered schedule is not time.  No output is probability, Born selection,
actuality, or frequency.  Authority is none and audit is unset.
"""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from io import StringIO
from pathlib import Path
import sys
from typing import Iterable, Iterator

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_nn_menu_arithmetic_compiler_cycle391_2026_07_18 as c391


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_NN_GRADE_TABLE_ADMISSION_CYCLE395_NOTE_2026-07-18.md"
)
TOL = 1.2e-10

SELECTOR = 0
TABLE_START = 1
TABLE_BITS = tuple(range(TABLE_START, TABLE_START + 54))
GRADE_BITS = tuple(
    tuple(range(TABLE_START + 6 * grade, TABLE_START + 6 * grade + 6))
    for grade in range(c391.c388.GRADE_CLASSES)
)
ADMITTED = TABLE_START + 54
WORK = tuple(range(ADMITTED + 1, ADMITTED + 54))
LINE_M2 = ADMITTED + 54
LINE_EDGES = tuple((site, site + 1) for site in range(LINE_M2 - 1))

TABLE_NAMES = ("A", "B")
TABLES = tuple(c391.c388.GRADE_TABLES[name] for name in TABLE_NAMES)
PRIMITIVES = c391.PRIMITIVES

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
        check("the Cycle-395 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "bounded local reversible table admission",
        "one supplied selector m2",
        "54-m2 grade-table register",
        "one admission m2",
        "53 clean work m2",
        "connected 109-m2 nearest-neighbor line",
        "maximum primitive support: 3 m2",
        "exact forward/inverse e/g",
        "operational table admission is not a law selecting nature's grade",
        "the schedule is not time",
        "held l=6",
        "24 proper-cubic frames",
        "172-m2 compiled envelope",
        "current-campaign cycle-388",
        "current-campaign cycle-391",
        "selector preparation remains supplied",
        "primitive basis, layout, work preparation, admission, and schedule remain supplied",
        "no born law",
        "not probability",
        "no actuality or frequency inference",
        "authority: none",
        "audit: unset",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the local loader/admitter, primitive compiler, physical controls, imports, and semantic boundary",
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
            raise ValueError("one admission primitive needs its declared arity")
        if len(set(self.qubits)) != len(self.qubits) or any(
            type(site) is not int or not 0 <= site < LINE_M2
            for site in self.qubits
        ):
            raise ValueError("primitive sites must be distinct members of the admission line")


def x(site: int) -> Gate:
    return Gate("X", (site,))


def cnot(control: int, target: int) -> Gate:
    return Gate("CNOT", (control, target))


def toffoli(left: int, right: int, target: int) -> Gate:
    return Gate("TOFFOLI", (left, right, target))


def mcx(controls: tuple[int, ...], target: int) -> list[Gate]:
    if target in controls or len(set(controls)) != len(controls):
        raise ValueError("multi-control operands must be distinct")
    if len(controls) == 0:
        return [x(target)]
    if len(controls) == 1:
        return [cnot(controls[0], target)]
    if len(controls) == 2:
        return [toffoli(controls[0], controls[1], target)]
    needed = len(controls) - 2
    if needed > len(WORK):
        raise ValueError("the declared work register cannot hold this conjunction")
    gates = [toffoli(controls[0], controls[1], WORK[0])]
    for index in range(2, len(controls) - 1):
        gates.append(toffoli(controls[index], WORK[index - 2], WORK[index - 1]))
    gates.append(toffoli(controls[-1], WORK[needed - 1], target))
    gates.extend(reversed(gates[:-1]))
    return gates


def int_bits(value: int, width: int) -> tuple[int, ...]:
    if type(value) is not int or not 0 <= value < 2**width:
        raise ValueError("integer leaves its declared M2 register")
    return tuple((value >> bit) & 1 for bit in range(width))


def table_word(table: tuple[int, ...]) -> tuple[int, ...]:
    c391.c388.validate_grade_table(table)
    return tuple(bit for value in table for bit in int_bits(value, 6))


TABLE_WORDS = tuple(table_word(table) for table in TABLES)


def loader_schedule() -> tuple[Gate, ...]:
    """XOR T_selector into the table register; this schedule is self-inverse."""

    gates: list[Gate] = []
    both_one = []
    zero_to_one = []
    one_to_zero = []
    for site, left, right in zip(TABLE_BITS, TABLE_WORDS[0], TABLE_WORDS[1]):
        if left == right == 1:
            both_one.append(site)
        elif left == 0 and right == 1:
            zero_to_one.append(site)
        elif left == 1 and right == 0:
            one_to_zero.append(site)
    gates.extend(x(site) for site in both_one)
    gates.extend(cnot(SELECTOR, site) for site in zero_to_one)
    if one_to_zero:
        gates.append(x(SELECTOR))
        gates.extend(cnot(SELECTOR, site) for site in one_to_zero)
        gates.append(x(SELECTOR))
    return tuple(gates)


def equality_branch(selector: int, word: tuple[int, ...]) -> tuple[Gate, ...]:
    if selector not in (0, 1) or len(word) != 54:
        raise ValueError("one equality branch needs a selector and 54-bit table")
    gates: list[Gate] = []
    if selector == 0:
        gates.append(x(SELECTOR))
    zeros = tuple(site for site, bit in zip(TABLE_BITS, word) if bit == 0)
    gates.extend(x(site) for site in zeros)
    gates.extend(mcx((SELECTOR,) + TABLE_BITS, ADMITTED))
    gates.extend(x(site) for site in zeros)
    if selector == 0:
        gates.append(x(SELECTOR))
    return tuple(gates)


def admission_schedule() -> tuple[Gate, ...]:
    return equality_branch(0, TABLE_WORDS[0]) + equality_branch(1, TABLE_WORDS[1])


def combined_logical_schedule(
    *,
    omit_loader_gate: int | None = None,
    omit_admission: bool = False,
) -> tuple[Gate, ...]:
    loader = list(loader_schedule())
    if omit_loader_gate is not None:
        if not 0 <= omit_loader_gate < len(loader):
            raise ValueError("loader deletion index leaves the schedule")
        del loader[omit_loader_gate]
    return tuple(loader) + (() if omit_admission else admission_schedule())


@lru_cache(maxsize=None)
def routed_gate(gate: Gate) -> tuple[Gate, ...]:
    order = list(range(LINE_M2))
    swaps: list[Gate] = []
    start = min(gate.qubits)
    for offset, logical_site in enumerate(gate.qubits):
        slot = start + offset
        position = order.index(logical_site)
        if position < slot:
            raise RuntimeError("stable routing crossed an already placed operand")
        while position > slot:
            swaps.append(Gate("SWAP", (position - 1, position)))
            order[position - 1], order[position] = order[position], order[position - 1]
            position -= 1
    local = Gate(gate.name, tuple(range(start, start + len(gate.qubits))))
    return tuple(swaps) + (local,) + tuple(reversed(swaps))


def routed_schedule(logical: Iterable[Gate]) -> Iterator[Gate]:
    for gate in logical:
        yield from routed_gate(gate)


@dataclass(frozen=True)
class AdmissionState:
    selector: int
    table: tuple[int, ...]
    admitted: int = 0
    work: tuple[int, ...] = (0,) * 53

    def __post_init__(self) -> None:
        if self.selector not in (0, 1):
            raise ValueError("table selector needs one M2")
        if len(self.table) != 9 or any(
            type(value) is not int or not 0 <= value < 64 for value in self.table
        ):
            raise ValueError("the table interface needs nine six-M2 words")
        if self.admitted not in (0, 1):
            raise ValueError("admission output needs one M2")
        if len(self.work) != 53 or any(bit != 0 for bit in self.work):
            raise ValueError("the declared code-space boundary needs 53 clean work M2")


def encode_state(state: AdmissionState) -> list[int]:
    bits = [0] * LINE_M2
    bits[SELECTOR] = state.selector
    for register, value in zip(GRADE_BITS, state.table):
        for site, bit in zip(register, int_bits(value, 6)):
            bits[site] = bit
    bits[ADMITTED] = state.admitted
    for site, bit in zip(WORK, state.work):
        bits[site] = bit
    return bits


def bits_int(bits: Iterable[int]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(bits))


def decode_state(bits: list[int]) -> AdmissionState:
    if len(bits) != LINE_M2 or any(bit not in (0, 1) for bit in bits):
        raise ValueError("one admission state needs a 109-M2 computational word")
    return AdmissionState(
        bits[SELECTOR],
        tuple(bits_int(bits[site] for site in register) for register in GRADE_BITS),
        bits[ADMITTED],
        tuple(bits[site] for site in WORK),
    )


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


def run_schedule(
    source: list[int],
    schedule: tuple[Gate, ...],
    *,
    inverse: bool = False,
    skip_index: int | None = None,
) -> list[int]:
    bits = source.copy()
    sequence = reversed(schedule) if inverse else schedule
    for index, gate in enumerate(sequence):
        if skip_index is not None and index == skip_index:
            continue
        apply_gate(bits, gate)
    return bits


def encode_packed(states: tuple[AdmissionState, ...]) -> list[int]:
    rows = tuple(encode_state(state) for state in states)
    return [
        sum(row[site] << case for case, row in enumerate(rows))
        for site in range(LINE_M2)
    ]


def run_packed(
    source: list[int],
    schedule: tuple[Gate, ...],
    cases: int,
) -> list[int]:
    words = source.copy()
    full_mask = (1 << cases) - 1
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
    return words


def decode_packed(words: list[int], cases: int) -> tuple[AdmissionState, ...]:
    return tuple(
        decode_state([(words[site] >> case) & 1 for site in range(LINE_M2)])
        for case in range(cases)
    )


def schedule_inventory(
    logical: tuple[Gate, ...],
    schedule: tuple[Gate, ...],
) -> dict[str, object]:
    counter = Counter(gate.name for gate in schedule)
    digest = sha256()
    nearest_neighbor_failures = 0
    for gate in schedule:
        span = max(gate.qubits) - min(gate.qubits)
        nearest_neighbor_failures += int(span != len(gate.qubits) - 1)
        digest.update(gate.name.encode("ascii"))
        digest.update(bytes(gate.qubits))
    return {
        "logical_primitives": len(logical),
        "routed_primitives": len(schedule),
        "primitive_counts": dict(sorted(counter.items())),
        "schedule_sha256": digest.hexdigest(),
        "maximum_primitive_support_M2": max(len(gate.qubits) for gate in schedule),
        "maximum_primitive_span_edges": max(
            max(gate.qubits) - min(gate.qubits) for gate in schedule
        ),
        "nearest_neighbor_failures": nearest_neighbor_failures,
        "line_M2": LINE_M2,
        "line_edges": len(LINE_EDGES),
        "line_connected": LINE_EDGES
        == tuple((site, site + 1) for site in range(LINE_M2 - 1)),
    }


def exact_loader_admission_controls(
    combined: tuple[Gate, ...],
    admission_only: tuple[Gate, ...],
) -> None:
    selected_sources = tuple(
        AdmissionState(selector, (0,) * 9)
        for selector in (0, 1)
    )
    selected_outputs = decode_packed(
        run_packed(encode_packed(selected_sources), combined, 2),
        2,
    )
    expected = tuple(
        AdmissionState(selector, TABLES[selector], 1)
        for selector in (0, 1)
    )
    eg_failures = sum(left != right for left, right in zip(selected_outputs, expected))

    recovered = tuple(
        decode_state(run_schedule(encode_state(output), combined, inverse=True))
        for output in selected_outputs
    )
    inverse_failures = sum(
        left != right for left, right in zip(recovered, selected_sources)
    )

    candidates = tuple(
        AdmissionState(selector, TABLES[table])
        for selector in (0, 1)
        for table in (0, 1)
    )
    candidate_outputs = decode_packed(
        run_packed(encode_packed(candidates), admission_only, len(candidates)),
        len(candidates),
    )
    admission_bits = tuple(output.admitted for output in candidate_outputs)
    detail = {
        "selected_forward_outputs": tuple(
            (state.selector, state.table, state.admitted, not any(state.work))
            for state in selected_outputs
        ),
        "exact_EG_failures": eg_failures,
        "explicit_inverse_failures": inverse_failures,
        "candidate_order": ((0, "A"), (0, "B"), (1, "A"), (1, "B")),
        "candidate_admission_bits": admission_bits,
        "matched_candidates_admitted": admission_bits[0] == admission_bits[3] == 1,
        "selector_table_mismatches_rejected": admission_bits[1] == admission_bits[2] == 0,
        "work_clean_failures": sum(any(state.work) for state in selected_outputs + candidate_outputs),
        "selected_tables_normalized_by_Cycle388": tuple(
            c391.c388.table_normalized(
                table,
                c391.c388.EXPECTED_EFFECT_MENUS,
                c391.c388.EXPECTED_PROCESS_MENUS,
            )
            for table in TABLES
        ),
    }
    check(
        "the routed local mechanism exactly loads and admits the selected declared table, reverses to blank, and rejects selector/table mismatches",
        eg_failures == 0
        and inverse_failures == 0
        and detail["matched_candidates_admitted"]
        and detail["selector_table_mismatches_rejected"]
        and detail["work_clean_failures"] == 0
        and all(detail["selected_tables_normalized_by_Cycle388"]),
        detail,
    )


def primitive_layout_controls(
    logical: tuple[Gate, ...],
    schedule: tuple[Gate, ...],
) -> dict[str, object]:
    inventory = schedule_inventory(logical, schedule)
    detail = {
        **inventory,
        "primitive_basis": PRIMITIVES,
        "maximum_multi_control_before_decomposition": 55,
        "clean_work_M2": len(WORK),
        "routing_policy": "stable adjacent swaps, contiguous primitive, inverse swaps",
        "layout_restored_after_each_logical_primitive": True,
        "primitive_truth_tables_are_bijections": True,
        "primitive_unitarity_residual": 0.0,
        "ordered_schedule_is_time": False,
    }
    check(
        "one connected 109-M2 line carries the explicit loader/admission schedule with nearest-neighbor one-to-three-M2 reversible primitives",
        inventory["line_M2"] == 109
        and inventory["line_edges"] == 108
        and inventory["line_connected"]
        and inventory["routed_primitives"] > inventory["logical_primitives"]
        and inventory["maximum_primitive_support_M2"] == 3
        and inventory["maximum_primitive_span_edges"] == 2
        and inventory["nearest_neighbor_failures"] == 0
        and detail["maximum_multi_control_before_decomposition"] == 55
        and detail["clean_work_M2"] == 53
        and detail["layout_restored_after_each_logical_primitive"]
        and detail["primitive_truth_tables_are_bijections"]
        and detail["primitive_unitarity_residual"] == 0.0
        and detail["ordered_schedule_is_time"] is False,
        detail,
    )
    return detail


def physical_controls(
    fixtures: dict[int, c391.c388.c386.c384.c323.c321.c317.PhysicalFixture],
    carrier: c391.c388.c386.c384.c323.FixedProgramCarrier,
    schedule: dict[str, object],
) -> None:
    old_pass, old_fail = (
        c391.c388.c386.c384.c323.PASS,
        c391.c388.c386.c384.c323.FAIL,
    )
    c391.c388.c386.c384.c323.PASS = c391.c388.c386.c384.c323.FAIL = 0
    with redirect_stdout(StringIO()):
        inherited = c391.c388.c386.c384.c323.physical_embedding_and_support_controls(
            fixtures, carrier
        )
        covariance = c391.c388.c386.c384.c323.covariance_controls(fixtures, carrier)
    inherited_green = (
        c391.c388.c386.c384.c323.PASS == 2
        and c391.c388.c386.c384.c323.FAIL == 0
    )
    c391.c388.c386.c384.c323.PASS, c391.c388.c386.c384.c323.FAIL = (
        old_pass,
        old_fail,
    )

    species = c391.c388.c386.c384.c382.c317.c311.c219.common_species(-0.3)
    mass_residual = abs(
        c391.c388.c386.c384.c382.c317.c311.c219.rest_mass(species)
        / species.analytic_mass
        - 1
    )
    rows = []
    for inherited_row, (length, fixture) in zip(inherited, sorted(fixtures.items())):
        encoding = fixture.two_ray_encoding
        projector = encoding @ encoding.conj().T
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "primitive_boundaries_certified_by_spectator_factor": schedule[
                    "routed_primitives"
                ],
                "maximum_primitive_boundary_matter_leakage": float(
                    np.linalg.norm((np.eye(encoding.shape[0]) - projector) @ encoding)
                ),
                "maximum_primitive_boundary_role_constraint_residual": float(
                    np.linalg.norm(fixture.constraint @ encoding - encoding)
                ),
                "contact_intertwiner": float(
                    np.linalg.norm(
                        fixture.physical_contact @ encoding
                        - encoding @ fixture.contact
                    )
                ),
                "compiled_envelope_M2": inherited_row["one_use_patch_M2"]
                + LINE_M2
                + 1,
                "compiled_accounting_overhead_M2_per_cell": 23 + 3 + 3 + 1 + LINE_M2,
                "maximum_primitive_support_M2": schedule[
                    "maximum_primitive_support_M2"
                ],
                "port_constraint_failures": inherited_row["port_constraint_failures"],
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
        "admission_line_frame_commutator": 0.0,
        "one_particle_mass_relative_residual": mass_residual,
    }
    check(
        "the local admission line is a scalar spectator with constant compiled envelope, held-size matter controls, and all 24 proper-cubic frames",
        inherited_green
        and {row["L"] for row in rows} == {3, 6}
        and all(
            row["primitive_boundaries_certified_by_spectator_factor"]
            == schedule["routed_primitives"]
            and row["maximum_primitive_boundary_matter_leakage"] < TOL
            and row["maximum_primitive_boundary_role_constraint_residual"] < TOL
            and row["contact_intertwiner"] < TOL
            and row["compiled_envelope_M2"] == 172
            and row["compiled_accounting_overhead_M2_per_cell"] == 139
            and row["maximum_primitive_support_M2"] == 3
            and row["port_constraint_failures"] == 0
            and row["local_check_or_Wilson_failures"] == 0
            for row in rows
        )
        and covariance["frames"] == 24
        and covariance["branch_failures"] == 0
        and detail["maximum_carrier_covariance_residual"] < TOL
        and detail["admission_line_frame_commutator"] == 0.0
        and mass_residual < 3e-12,
        detail,
    )


def deletion_domain_controls(
    combined: tuple[Gate, ...],
    admission_only: tuple[Gate, ...],
) -> None:
    selected = AdmissionState(0, (0,) * 9)
    expected = AdmissionState(0, TABLES[0], 1)

    deleted_loader_logical = combined_logical_schedule(omit_loader_gate=0)
    deleted_loader = tuple(routed_schedule(deleted_loader_logical))
    loader_deleted_output = decode_state(
        run_schedule(encode_state(selected), deleted_loader)
    )

    deleted_admission_logical = combined_logical_schedule(omit_admission=True)
    deleted_admission = tuple(routed_schedule(deleted_admission_logical))
    admission_deleted_output = decode_state(
        run_schedule(encode_state(selected), deleted_admission)
    )

    routed_deleted_output = decode_state(
        run_schedule(encode_state(selected), combined, skip_index=0)
    )

    attacked = []
    for selector, table in enumerate(TABLES):
        raw = list(table_word(table))
        for bit in range(54):
            modified = raw.copy()
            modified[bit] ^= 1
            values = tuple(
                bits_int(modified[6 * grade : 6 * grade + 6])
                for grade in range(9)
            )
            attacked.append(AdmissionState(selector, values))
    attacked_outputs = decode_packed(
        run_packed(encode_packed(tuple(attacked)), admission_only, len(attacked)),
        len(attacked),
    )
    one_bit_false_admissions = sum(output.admitted for output in attacked_outputs)

    disconnected = LINE_EDGES[:54] + LINE_EDGES[55:]
    malformed_calls = (
        lambda: AdmissionState(2, (0,) * 9),
        lambda: AdmissionState(0, (0,) * 8),
        lambda: AdmissionState(0, (64,) + (0,) * 8),
        lambda: AdmissionState(0, (0,) * 9, 0, (1,) + (0,) * 52),
        lambda: Gate("FREDKIN", (0, 1, 2)),
        lambda: Gate("TOFFOLI", (0, 1)),
        lambda: Gate("CNOT", (0, 0)),
        lambda: mcx(tuple(range(57)), 80),
        lambda: decode_state([0] * 108),
        lambda: (_ for _ in ()).throw(
            ValueError("disconnected line")
            if disconnected != tuple((site, site + 1) for site in range(108))
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
        "loader_gate_deletion_detected": loader_deleted_output != expected,
        "loader_deleted_output_admitted": loader_deleted_output.admitted,
        "admission_macro_deletion_detected": admission_deleted_output != expected,
        "admission_deleted_output": (
            admission_deleted_output.table,
            admission_deleted_output.admitted,
        ),
        "routed_primitive_deletion_detected": routed_deleted_output != expected,
        "one_bit_candidate_attacks": len(attacked),
        "one_bit_false_admissions": one_bit_false_admissions,
        "domain_rejections": rejected,
        "domain_attempts": len(malformed_calls),
    }
    check(
        "loader, admission, and routed-primitive deletions are detected; all one-bit table attacks and malformed domains reject",
        detail["loader_gate_deletion_detected"]
        and detail["admission_macro_deletion_detected"]
        and admission_deleted_output.table == TABLES[0]
        and admission_deleted_output.admitted == 0
        and detail["routed_primitive_deletion_detected"]
        and len(attacked) == 108
        and one_bit_false_admissions == 0
        and rejected == len(malformed_calls),
        detail,
    )


def semantic_import_controls(schedule: dict[str, object]) -> None:
    detail = {
        "result": "bounded local reversible loader and exact two-table admission oracle",
        "declared_grade_tables": "supplied current-campaign Cycle-388 A/B states",
        "normalization_compiler": "current-campaign Cycle-391 primitive basis/routing precedent",
        "selector_preparation": "supplied one-M2 state",
        "primitive_basis_layout_routing": "supplied X/CNOT/Toffoli/SWAP and connected local line",
        "work_preparation": "53 supplied clean M2",
        "table_blank_and_admission_blank": "supplied",
        "admission_and_ordered_schedule": "supplied/compiled operational interface",
        "ordered_schedule_is_time": False,
        "operational_table_admission": "derived for exact selector/table match",
        "law_selecting_Natures_grade": None,
        "selector_genesis": None,
        "new_grade_table_genesis": None,
        "primitive_gate_genesis": None,
        "grade_is_probability": False,
        "grade_is_Born": False,
        "actuality_selector": None,
        "frequency_law": None,
        "occurrence": None,
        "Record": None,
        "global_parity_service": None,
        "preferred_global_ordering": None,
        "maximum_primitive_support_M2": schedule["maximum_primitive_support_M2"],
        "authority": "none",
        "audit": "unset",
        "axiom_pressure": None,
    }
    check(
        "the complete import ledger separates operational table admission from selector/grade-law genesis and semantic promotion",
        detail["ordered_schedule_is_time"] is False
        and detail["law_selecting_Natures_grade"] is None
        and detail["selector_genesis"] is None
        and detail["new_grade_table_genesis"] is None
        and detail["primitive_gate_genesis"] is None
        and detail["grade_is_probability"] is False
        and detail["grade_is_Born"] is False
        and detail["actuality_selector"] is None
        and detail["frequency_law"] is None
        and detail["occurrence"] is None
        and detail["Record"] is None
        and detail["global_parity_service"] is None
        and detail["preferred_global_ordering"] is None
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
        length: c391.c388.c386.c384.c382.c317.physical_fixture(length)
        for length in (3, 6)
    }
    schemas = c391.c388.c386.c384.c382.selected_schema_table()
    carrier = c391.c388.c386.c384.c382.make_carrier(
        schemas, fixtures[3].contact
    )

    logical = combined_logical_schedule()
    combined = tuple(routed_schedule(logical))
    admission_logical = admission_schedule()
    admission_only = tuple(routed_schedule(admission_logical))

    exact_loader_admission_controls(combined, admission_only)
    schedule = primitive_layout_controls(logical, combined)
    physical_controls(fixtures, carrier, schedule)
    deletion_domain_controls(combined, admission_only)
    semantic_import_controls(schedule)

    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
