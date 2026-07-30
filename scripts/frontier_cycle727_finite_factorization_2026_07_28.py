#!/usr/bin/env python3
"""Self-contained finite companion factorization for Cycle 727."""

from __future__ import annotations

from dataclasses import dataclass

import frontier_cycle727_finite_fixtures_2026_07_28 as M
from frontier_cycle727_finite_pauli_tableau_2026_07_28 import (
    Pauli,
    canonical_pauli,
    complete_tableau,
    decode,
    gf2_rank,
    gf2_solve,
    homogeneous_nullspace,
    independent_paired_basis,
    symplectic,
    symplectic_split_paired,
    symplectic_split_vectors,
    xor_rows,
)


@dataclass(frozen=True)
class Factorization:
    fixture: M.CompanionFixture
    physical_w: tuple[Pauli, ...]
    physical_v: tuple[Pauli, ...]
    target_w: tuple[Pauli, ...]
    target_v: tuple[Pauli, ...]
    logical: int
    gauge: int
    center: int
    local_center_rank: int
    phase_rank: int
    phase_contradictions: int


def local_centralizer_basis(
    fixture: M.CompanionFixture,
    physical_generators: tuple[Pauli, ...],
    radius: int,
) -> tuple[int, ...]:
    radius_rows = []
    for center_coordinate in fixture.cells:
        allowed_qubits = tuple(
            qubit
            for qubit in range(fixture.qubits)
            if sum(
                abs(a - b)
                for a, b in zip(
                    fixture.cells[M.qubit_cell(fixture, qubit)],
                    center_coordinate,
                )
            )
            <= radius
        )
        local_index = {
            qubit: index
            for index, qubit in enumerate(allowed_qubits)
        }
        equations = []
        for generator in physical_generators:
            mask = 0
            for qubit, index in local_index.items():
                if (generator.z >> qubit) & 1:
                    mask ^= 1 << (2 * index)
                if (generator.x >> qubit) & 1:
                    mask ^= 1 << (2 * index + 1)
            equations.append(mask)
        for local in homogeneous_nullspace(
            tuple(equations), 2 * len(allowed_qubits)
        ):
            x = z = 0
            for qubit, index in local_index.items():
                x |= ((local >> (2 * index)) & 1) << qubit
                z |= ((local >> (2 * index + 1)) & 1) << qubit
            radius_rows.append(x | (z << fixture.qubits))
    independent = []
    rank = 0
    for row in radius_rows:
        trial = gf2_rank((*independent, row))
        if trial > rank:
            independent.append(row)
            rank = trial
    return tuple(independent)


def gauge_structure(
    fixture: M.CompanionFixture,
    physical_generators: tuple[Pauli, ...],
    _relation_rows: tuple[Pauli, ...],
) -> tuple[dict[str, object], tuple[int, ...]]:
    gauge = local_centralizer_basis(
        fixture, physical_generators, 1
    )
    return {"local_centralizer_rank": len(gauge)}, gauge


def local_center_basis(
    fixture: M.CompanionFixture,
    gauge: tuple[int, ...],
    radius: int,
) -> tuple[int, ...]:
    count = len(gauge)
    qubits = fixture.qubits
    gram_equations = tuple(
        sum(
            symplectic(
                gauge[left], gauge[right], qubits
            )
            << left
            for left in range(count)
        )
        for right in range(count)
    )
    displayed = []
    for coordinate in fixture.cells:
        allowed = {
            qubit
            for qubit in range(qubits)
            if sum(
                abs(a - b)
                for a, b in zip(
                    fixture.cells[M.qubit_cell(fixture, qubit)],
                    coordinate,
                )
            )
            <= radius
        }
        equations = list(gram_equations)
        for bit in range(2 * qubits):
            if bit % qubits in allowed:
                continue
            equations.append(sum(
                ((row >> bit) & 1) << index
                for index, row in enumerate(gauge)
            ))
        for coefficients in homogeneous_nullspace(
            tuple(equations), count
        ):
            displayed.append(xor_rows(
                gauge[index]
                for index in range(count)
                if (coefficients >> index) & 1
            ))
    pivots: dict[int, int] = {}
    basis = []
    for original in displayed:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                basis.append(original)
                break
    return tuple(basis)


def parity_complement(
    local_rows: tuple[int, ...], parity: int, desired: int
) -> tuple[int, ...]:
    pivots: dict[int, int] = {
        parity.bit_length() - 1: parity
    }
    output = []
    for original in local_rows:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                output.append(original)
                break
    return tuple(output[:desired])


def build_factorization(
    fixture: M.CompanionFixture,
) -> Factorization:
    rows = M.operator_rows(fixture)
    physical = tuple(row[1] for row in rows)
    target = tuple(row[2] for row in rows)
    paired = independent_paired_basis(
        tuple(
            row.symplectic(fixture.qubits) for row in physical
        ),
        tuple(
            row.symplectic(fixture.matter_qubits)
            for row in target
        ),
    )
    _radicals, logical_pairs = symplectic_split_paired(
        paired, fixture.qubits
    )
    relations = M.relation_certificate(fixture)["relation_rows"]
    _gauge_report, gauge = gauge_structure(
        fixture, physical, relations
    )
    gauge_radicals, gauge_pairs = symplectic_split_vectors(
        gauge, fixture.qubits
    )
    parity = Pauli(
        z=(1 << fixture.matter_qubits) - 1
    ).symplectic(fixture.qubits)
    local_center_all = local_center_basis(fixture, gauge, 2)
    local_center = parity_complement(
        local_center_all,
        parity,
        len(gauge_radicals) - 1,
    )
    center = local_center + (parity,)
    physical_w = tuple(
        [
            canonical_pauli(pair[0][0], fixture.qubits)
            for pair in logical_pairs
        ]
        + [
            canonical_pauli(pair[0], fixture.qubits)
            for pair in gauge_pairs
        ]
        + [
            canonical_pauli(row, fixture.qubits)
            for row in center
        ]
    )
    physical_v_explicit = tuple(
        [
            canonical_pauli(pair[1][0], fixture.qubits)
            for pair in logical_pairs
        ]
        + [
            canonical_pauli(pair[1], fixture.qubits)
            for pair in gauge_pairs
        ]
    )
    physical_v = complete_tableau(
        physical_w,
        physical_v_explicit,
        fixture.qubits,
    )
    target_w = tuple(
        [
            canonical_pauli(
                pair[0][1], fixture.matter_qubits
            )
            for pair in logical_pairs
        ]
        + [
            Pauli(
                z=(1 << fixture.matter_qubits) - 1
            )
        ]
    )
    target_v = complete_tableau(
        target_w,
        tuple(
            canonical_pauli(
                pair[1][1], fixture.matter_qubits
            )
            for pair in logical_pairs
        ),
        fixture.matter_qubits,
    )
    phase_equations = []
    for physical_row, target_row in zip(physical, target):
        physical_coordinates = decode(
            physical_row,
            physical_w,
            physical_v,
            fixture.qubits,
        )
        target_coordinates = decode(
            target_row,
            target_w,
            target_v,
            fixture.matter_qubits,
        )
        delta = (
            target_coordinates.phase
            - physical_coordinates.phase
        ) % 4
        mask = (
            (
                physical_coordinates.v_mask
                & ((1 << len(logical_pairs)) - 1)
            )
            | (
                (
                    physical_coordinates.w_mask
                    & ((1 << len(logical_pairs)) - 1)
                )
                << len(logical_pairs)
            )
            | (
                (
                    (
                        physical_coordinates.w_mask
                        >> (
                            len(logical_pairs)
                            + len(gauge_pairs)
                        )
                    )
                    & ((1 << (len(center) - 1)) - 1)
                )
                << (2 * len(logical_pairs))
            )
        )
        phase_equations.append((mask, delta // 2))
    solution, phase_rank, phase_contradictions = gf2_solve(
        phase_equations
    )
    physical_w = list(physical_w)
    physical_v = list(physical_v)
    for index in range(len(logical_pairs)):
        if (solution >> index) & 1:
            row = physical_v[index]
            physical_v[index] = Pauli(
                (row.phase + 2) % 4, row.x, row.z
            )
        if (
            solution
            >> (len(logical_pairs) + index)
        ) & 1:
            row = physical_w[index]
            physical_w[index] = Pauli(
                (row.phase + 2) % 4, row.x, row.z
            )
    for index in range(len(center) - 1):
        if (
            solution
            >> (2 * len(logical_pairs) + index)
        ) & 1:
            position = (
                len(logical_pairs) + len(gauge_pairs) + index
            )
            row = physical_w[position]
            physical_w[position] = Pauli(
                (row.phase + 2) % 4, row.x, row.z
            )
    return Factorization(
        fixture,
        tuple(physical_w),
        tuple(physical_v),
        target_w,
        target_v,
        len(logical_pairs),
        len(gauge_pairs),
        len(center),
        gf2_rank(local_center),
        phase_rank,
        phase_contradictions,
    )
