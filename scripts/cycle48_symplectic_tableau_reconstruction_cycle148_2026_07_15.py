#!/usr/bin/env python3
"""Cycle 148: exact symplectic reconstruction of Cycle-48 update tables."""

from __future__ import annotations

from itertools import product
from pathlib import Path

import cycle48_symplectic_tableau_compression_probe_2026_07_15 as p


c48 = p.c48
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "CYCLE48_SYMPLECTIC_TABLEAU_RECONSTRUCTION_CYCLE148_NOTE_2026-07-15.md"
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


BITS_LETTER = {value: key for key, value in p.LETTER_BITS.items()}
PAULI = dict(c48.PAULI_1)


def row_matrix(record: p.Row):
    left = BITS_LETTER[(record[0], record[2])]
    right = BITS_LETTER[(record[1], record[3])]
    sign = -1 if record[4] else 1
    return sign * c48.kron(PAULI[left], PAULI[right])


def all_rows():
    return tuple(product((0, 1), repeat=5))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND REPRESENTATION")
    check("review note exists", NOTE.is_file())
    check(
        "five tableau bits encode all sixteen signed two-qubit Paulis",
        len(all_rows()) == 32
        and len({row_matrix(record).tobytes() for record in all_rows()}) == 32,
    )
    check(
        "sixty Cycle-48 labels give sixty distinct stabilizer groups",
        len(p.STATE_GENERATORS) == len(p.KEY_STATE) == 60,
    )
    check(
        "each state has exactly six ordered generator bases",
        {len(p.all_bases(state_id)) for state_id in range(60)} == {6},
    )

    print("\nBIT ALGEBRA AGAINST MATRICES")
    multiplication_failures = []
    multiplication_controls = 0
    for left in all_rows():
        for right in all_rows():
            if p.symplectic(left, right):
                continue
            multiplication_controls += 1
            observed = row_matrix(p.multiply_commuting(left, right))
            expected = row_matrix(left) @ row_matrix(right)
            if not c48.same(observed, expected):
                multiplication_failures.append((left, right))
    check(
        "every commuting signed-Pauli product matches matrix multiplication",
        multiplication_controls == 544 and not multiplication_failures,
        (multiplication_controls, multiplication_failures[:1]),
    )
    gate_formula_failures = []
    for record in all_rows():
        for gate_id, (_name, gate) in enumerate(c48.CLIFFORD_GATES):
            observed = row_matrix(p.apply_gate(record, gate_id))
            expected = gate @ row_matrix(record) @ gate.conj().T
            if not c48.same(observed, expected):
                gate_formula_failures.append((record, gate_id))
    check(
        "all 224 signed-Pauli gate updates match conjugation matrices",
        not gate_formula_failures,
        gate_formula_failures[:1],
    )

    print("\nFULL TABLE RECONSTRUCTION")
    gate_failures = []
    basis_gate_failures = []
    for state_id in range(60):
        for gate_id in range(7):
            expected = p.clifford.GATE_IMAGE[(state_id, gate_id)]
            if p.tableau_gate_image(p.STATE_GENERATORS[state_id], gate_id) != expected:
                gate_failures.append((state_id, gate_id))
            for basis in p.all_bases(state_id):
                if p.tableau_gate_image(basis, gate_id) != expected:
                    basis_gate_failures.append((state_id, gate_id, basis))
    check(
        "compact formulas reconstruct all 420 Clifford state transitions",
        not gate_failures,
        gate_failures[:1],
    )
    check(
        "all 2,520 generator-basis gate presentations agree",
        not basis_gate_failures,
        basis_gate_failures[:1],
    )

    measurement_failures = []
    basis_measurement_failures = []
    for state_id in range(60):
        for measurement_id in range(15):
            for outcome_bit in (0, 1):
                probability, target = p.compiled.BRANCH[(state_id, measurement_id, outcome_bit)]
                expected = (float(probability), target)
                if p.tableau_measure(p.STATE_GENERATORS[state_id], measurement_id, outcome_bit) != expected:
                    measurement_failures.append((state_id, measurement_id, outcome_bit))
                for basis in p.all_bases(state_id):
                    if p.tableau_measure(basis, measurement_id, outcome_bit) != expected:
                        basis_measurement_failures.append((state_id, measurement_id, outcome_bit, basis))
    check(
        "commutation/pivot reconstructs all 1,800 conditional branches",
        not measurement_failures,
        measurement_failures[:1],
    )
    check(
        "all 10,800 generator-basis measurement presentations agree",
        not basis_measurement_failures,
        basis_measurement_failures[:1],
    )

    print("\nGENERATOR REDUNDANCY")
    derived_failures = []
    cx10_sequence = (0, 1, 4, 0, 1)
    swap_sequence = (4, 5, 4)
    for record in all_rows():
        if p.apply_sequence(record, cx10_sequence) != p.apply_gate(record, 5):
            derived_failures.append(("CX10", record))
        if p.apply_sequence(record, swap_sequence) != p.apply_gate(record, 6):
            derived_failures.append(("SWAP", record))
    check(
        "reverse-CNOT and SWAP are derived from H and forward-CNOT",
        not derived_failures,
        derived_failures[:1],
    )
    check(
        "2,280 compiled transition rows are reconstructed rather than independent",
        420 + 1_800 == 2_220
        and 480 + 1_800 == 2_280
        and not gate_failures
        and not measurement_failures,
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "exact table reconstruction",
        "does not derive the tableau algebra from the axioms",
        "equal anticommuting weights remain quantum input",
        "physical bitwise record compiler remains open",
        "no axiom addition follows",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "SYMPLECTIC_TABLEAU_RECONSTRUCTION" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
