#!/usr/bin/env python3
"""Reconstruct Cycle-48 tables from compact two-qubit tableau algebra."""

from __future__ import annotations

from itertools import permutations, product

import cycle48_pauli_luders_update_compilation_probe_2026_07_15 as compiled


c48 = compiled.c48
clifford = compiled.clifford
Row = tuple[int, int, int, int, int]  # x0,x1,z0,z1,sign-bit


LETTER_BITS = {
    "I": (0, 0),
    "X": (1, 0),
    "Y": (1, 1),
    "Z": (0, 1),
}


def row(name: str, sign: int = 1) -> Row:
    (x0, z0), (x1, z1) = (LETTER_BITS[letter] for letter in name)
    return (x0, x1, z0, z1, 0 if sign == 1 else 1)


def symplectic(left: Row, right: Row) -> int:
    return (
        left[0] * right[2] + left[1] * right[3]
        + left[2] * right[0] + left[3] * right[1]
    ) & 1


def multiply_commuting(left: Row, right: Row) -> Row:
    assert symplectic(left, right) == 0
    lx = left[:2]
    lz = left[2:4]
    rx = right[:2]
    rz = right[2:4]
    x = tuple(a ^ b for a, b in zip(lx, rx))
    z = tuple(a ^ b for a, b in zip(lz, rz))
    phase_exponent = (
        sum(a * b for a, b in zip(lx, lz))
        + sum(a * b for a, b in zip(rx, rz))
        - sum(a * b for a, b in zip(x, z))
    )
    assert phase_exponent % 2 == 0
    phase_bit = (phase_exponent // 2 + sum(a * b for a, b in zip(lz, rx))) & 1
    return (x[0], x[1], z[0], z[1], left[4] ^ right[4] ^ phase_bit)


def group_key(first: Row, second: Row):
    assert symplectic(first, second) == 0
    third = multiply_commuting(first, second)
    identity = (0, 0, 0, 0)
    assert first[:4] != identity and second[:4] != identity and third[:4] != identity
    return tuple(sorted((first, second, third)))


STATE_GENERATORS = {
    state_id: (
        row(name1, sign1),
        row(name2, sign2),
    )
    for state_id, (name1, sign1, name2, sign2) in enumerate(clifford._LABELS)
}
KEY_STATE = {
    group_key(*generators): state_id
    for state_id, generators in STATE_GENERATORS.items()
}


def h(record: Row, qubit: int) -> Row:
    x = [record[0], record[1]]
    z = [record[2], record[3]]
    sign = record[4] ^ (x[qubit] & z[qubit])
    x[qubit], z[qubit] = z[qubit], x[qubit]
    return (x[0], x[1], z[0], z[1], sign)


def s(record: Row, qubit: int) -> Row:
    x = [record[0], record[1]]
    z = [record[2], record[3]]
    sign = record[4] ^ (x[qubit] & z[qubit])
    z[qubit] ^= x[qubit]
    return (x[0], x[1], z[0], z[1], sign)


def cx(record: Row, control: int, target: int) -> Row:
    x = [record[0], record[1]]
    z = [record[2], record[3]]
    sign = record[4] ^ (
        x[control] & z[target] & (x[target] ^ z[control] ^ 1)
    )
    x[target] ^= x[control]
    z[control] ^= z[target]
    return (x[0], x[1], z[0], z[1], sign)


def swap(record: Row) -> Row:
    return (record[1], record[0], record[3], record[2], record[4])


def apply_gate(record: Row, gate_id: int) -> Row:
    return (
        h(record, 0) if gate_id == 0 else
        h(record, 1) if gate_id == 1 else
        s(record, 0) if gate_id == 2 else
        s(record, 1) if gate_id == 3 else
        cx(record, 0, 1) if gate_id == 4 else
        cx(record, 1, 0) if gate_id == 5 else
        swap(record) if gate_id == 6 else
        (_ for _ in ()).throw(ValueError(gate_id))
    )


def apply_sequence(record: Row, sequence: tuple[int, ...]) -> Row:
    for gate_id in sequence:
        record = apply_gate(record, gate_id)
    return record


def tableau_gate_image(generators: tuple[Row, Row], gate_id: int):
    return KEY_STATE[group_key(*(apply_gate(record, gate_id) for record in generators))]


def measurement_row(measurement_id: int, outcome_bit: int) -> Row:
    name = c48.NONTRIVIAL_PAULI_2[measurement_id][0]
    return row(name, 1 if outcome_bit else -1)


def tableau_measure(generators: tuple[Row, Row], measurement_id: int, outcome_bit: int):
    measured = measurement_row(measurement_id, outcome_bit)
    anti = [index for index, generator in enumerate(generators) if symplectic(generator, measured)]
    if not anti:
        key = group_key(*generators)
        group = set(key)
        if measured in group:
            return (1, KEY_STATE[key])
        opposite = (*measured[:4], measured[4] ^ 1)
        assert opposite in group
        return (0, None)
    pivot = anti[0]
    updated = list(generators)
    for index in anti[1:]:
        updated[index] = multiply_commuting(updated[index], updated[pivot])
    updated[pivot] = measured
    return (1 / 2, KEY_STATE[group_key(*updated)])


def all_bases(state_id: int):
    group = group_key(*STATE_GENERATORS[state_id])
    return tuple(permutations(group, 2))


def main() -> int:
    print("STATE_KEYS", len(STATE_GENERATORS), len(KEY_STATE))
    print("BASES", sum(len(all_bases(state_id)) for state_id in range(60)))
    gate_failures = []
    basis_gate_failures = []
    for state_id in range(60):
        for gate_id in range(7):
            expected = clifford.GATE_IMAGE[(state_id, gate_id)]
            observed = tableau_gate_image(STATE_GENERATORS[state_id], gate_id)
            if observed != expected:
                gate_failures.append((state_id, gate_id, expected, observed))
            for basis in all_bases(state_id):
                if tableau_gate_image(basis, gate_id) != expected:
                    basis_gate_failures.append((state_id, gate_id, basis))
    print("GATES", 60 * 7, len(gate_failures), 60 * 6 * 7, len(basis_gate_failures))

    measure_failures = []
    basis_measure_failures = []
    for state_id in range(60):
        for measurement_id in range(15):
            for outcome_bit in (0, 1):
                probability, target = compiled.BRANCH[(state_id, measurement_id, outcome_bit)]
                expected = (float(probability), target)
                observed = tableau_measure(STATE_GENERATORS[state_id], measurement_id, outcome_bit)
                if observed != expected:
                    measure_failures.append((state_id, measurement_id, outcome_bit, expected, observed))
                for basis in all_bases(state_id):
                    if tableau_measure(basis, measurement_id, outcome_bit) != expected:
                        basis_measure_failures.append((state_id, measurement_id, outcome_bit, basis))
    print("MEASURE", 1_800, len(measure_failures), 60 * 6 * 30, len(basis_measure_failures))

    derived_failures = []
    cx10_sequence = (0, 1, 4, 0, 1)
    swap_sequence = (4, 5, 4)
    for bits in product((0, 1), repeat=5):
        record: Row = bits  # type: ignore[assignment]
        if apply_sequence(record, cx10_sequence) != apply_gate(record, 5):
            derived_failures.append(("CX10", record))
        if apply_sequence(record, swap_sequence) != apply_gate(record, 6):
            derived_failures.append(("SWAP", record))
    print("DERIVED", cx10_sequence, swap_sequence, len(derived_failures))

    result = (
        len(KEY_STATE) == 60
        and not gate_failures
        and not basis_gate_failures
        and not measure_failures
        and not basis_measure_failures
        and not derived_failures
    )
    if gate_failures or basis_gate_failures or measure_failures or basis_measure_failures or derived_failures:
        print("FAILURE_SAMPLE", (
            gate_failures[:2], basis_gate_failures[:2],
            measure_failures[:2], basis_measure_failures[:2], derived_failures[:2],
        ))
    print("RESULT", "SYMPLECTIC_TABLEAU_RECONSTRUCTION" if result else "OPEN")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
