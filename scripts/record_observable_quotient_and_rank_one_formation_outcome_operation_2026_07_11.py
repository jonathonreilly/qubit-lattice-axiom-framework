#!/usr/bin/env python3
"""Exact checks for the record-observable quotient and instrument lemmas.

The runner separates three objects: an appended Hamiltonian interaction, a
same-carrier unitary, and a record-forming CP operation.  It derives no Born
rule, event rate, physical clock, or coherent carrier selector.
"""

from __future__ import annotations

import itertools

import numpy as np
import sympy as sp


PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label}: {detail}")


I2 = sp.eye(2)
P0 = sp.Matrix([[1, 0], [0, 0]])
P1 = sp.Matrix([[0, 0], [0, 1]])
PX = sp.Matrix([[1, 1], [1, 1]]) / 2
PY = sp.Matrix([[1, -sp.I], [sp.I, 1]]) / 2


def neighbors(site: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    result = []
    for axis in range(3):
        for sign in (-1, 1):
            point = list(site)
            point[axis] += sign
            result.append(tuple(point))
    return result


def available_support(record: dict[tuple[int, int, int], sp.Matrix], site: tuple[int, int, int]) -> sp.Matrix:
    total = sp.zeros(2, 2)
    for neighbor in neighbors(site):
        total += record.get(neighbor, sp.zeros(2, 2))
    if total == sp.zeros(2, 2) or total == sp.eye(2):
        return sp.eye(2)
    # The runner histories use rank-one multiples or the three displayed
    # projectors.  Numerical diagonalization only chooses the top support for
    # these finite witness checks; the theorem itself is extensional.
    total_np = np.array(total.tolist(), dtype=complex)
    values, vectors = np.linalg.eigh(total_np)
    top = values[-1]
    selected = vectors[:, np.isclose(values, top)]
    projector = selected @ selected.conj().T
    return sp.Matrix(projector).applyfunc(lambda value: sp.nsimplify(value, [sp.sqrt(2)]))


def is_available(record: dict[tuple[int, int, int], sp.Matrix], site: tuple[int, int, int], candidate: sp.Matrix) -> bool:
    support = available_support(record, site)
    return sp.simplify(support * candidate - candidate) == sp.zeros(2, 2)


def all_records_still_admissible(record: dict[tuple[int, int, int], sp.Matrix]) -> bool:
    return all(is_available(record, site, projector) for site, projector in record.items())


def record_signature(history: list[dict[tuple[int, int, int], sp.Matrix]]) -> tuple:
    return tuple(
        (
            tuple(sorted(state)),
            tuple(sp.srepr(state[site]) for site in sorted(state)),
            len(state),
        )
        for state in history
    )


def exchange_interaction(coupling: int) -> sp.Matrix:
    swap = sp.zeros(4, 4)
    for left, right in itertools.product(range(2), repeat=2):
        source = 2 * left + right
        target = 2 * right + left
        swap[target, source] = 1
    return coupling * (sp.eye(4) - swap)


def finite_completion_signature(coupling: int, couple_law_to_readout: bool = False) -> tuple:
    """Rebuild a finite completion and compute its record-level signature.

    The baseline completion appends H_lambda but does not pass it into the
    successor or readout maps.  The hostile control deliberately exposes one
    Hamiltonian entry to readout so the invariance check is mutation-sensitive.
    """
    hamiltonian = exchange_interaction(coupling)
    path = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
    state: dict[tuple[int, int, int], sp.Matrix] = {}
    history = [dict(state)]
    for site in path:
        if not is_available(state, site, P0):
            raise AssertionError("finite completion witness became unavailable")
        state = dict(state)
        state[site] = P0
        if not all_records_still_admissible(state):
            raise AssertionError("finite completion witness lost admissibility")
        history.append(dict(state))
    readouts = tuple(
        len(entry) + (hamiltonian[1, 1] if couple_law_to_readout else 0)
        for entry in history
    )
    return record_signature(history), readouts


def history_checks() -> None:
    path = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0)]
    state: dict[tuple[int, int, int], sp.Matrix] = {}
    history = [dict(state)]
    step_ok = True
    persistence_ok = True
    for site in path:
        step_ok &= is_available(state, site, P0)
        state = dict(state)
        state[site] = P0
        persistence_ok &= all_records_still_admissible(state)
        history.append(dict(state))
    check("R01", step_ok, "connected all-|0> additions are available at insertion")
    check("R02", persistence_ok, "all-|0> history also satisfies the stronger continual-admissibility reading")
    check("R03", [len(entry) for entry in history] == [0, 1, 2, 3, 4], "readout is the monotone record count")

    # Construct genuinely different exchange interactions, then recompute the
    # finite record completion separately for every coupling.
    couplings = (-3, 0, 2, 7)
    interactions = [exchange_interaction(coupling) for coupling in couplings]
    check("R04", len({tuple(matrix) for matrix in interactions}) == len(couplings), "four lambda(I-SWAP) Hamiltonians are algebraically distinct")
    signatures = {finite_completion_signature(coupling) for coupling in couplings}
    check("R05", len(signatures) == 1, "distinct appended exchange laws have one recomputed record-history/readout signature")
    hostile_signatures = {
        finite_completion_signature(coupling, couple_law_to_readout=True)
        for coupling in couplings
    }
    check("R06", len(hostile_signatures) == len(couplings), "hostile law-to-readout coupling makes the quotient check fail as intended")

    # Reproduce the repair target in the July witness: after the middle plus
    # record is added, the two endpoint records are no longer top-supported.
    bad = {(0, 0, 0): P0, (2, 0, 0): P1}
    check("R07", is_available(bad, (1, 0, 0), PX), "the middle |+> insertion is initially available")
    bad[(1, 0, 0)] = PX
    check("R08", not all_records_still_admissible(bad), "mixed history separates insertion-only from continual-admissibility readings")


def commutant_checks() -> None:
    variables = sp.symbols("h0:16")
    hamiltonian = sp.Matrix(4, 4, variables)
    projectors = [sp.kronecker_product(projector, I2) for projector in (P0, PX, PY)]
    equations = []
    for projector in projectors:
        equations.extend(list(hamiltonian * projector - projector * hamiltonian))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    nullspace = coefficient_matrix.nullspace()
    check("P01", coefficient_matrix.rank() == 12, "three rank-one record frames impose rank 12 on a 16-dimensional two-site operator")
    check("P02", len(nullspace) == 4, "same-carrier record-preserving commutant has dimension four")

    rest_basis = []
    for row, column in itertools.product(range(2), repeat=2):
        matrix_unit = sp.zeros(2, 2)
        matrix_unit[row, column] = 1
        rest_basis.append(sp.kronecker_product(I2, matrix_unit))
    flattened_rest = [sp.Matrix(list(matrix)) for matrix in rest_basis]
    flattened_null = [sp.Matrix(vector) for vector in nullspace]
    span_rank = sp.Matrix.hstack(*flattened_rest, *flattened_null).rank()
    check("P03", span_rank == 4, "the full commutant is exactly I_site tensor M2_rest")

    swap = sp.zeros(4, 4)
    for left, right in itertools.product(range(2), repeat=2):
        source = 2 * left + right
        target = 2 * right + left
        swap[target, source] = 1
    commutator = swap * projectors[0] - projectors[0] * swap
    check("P04", commutator != sp.zeros(4, 4), "SWAP does not preserve an arbitrary locked local record projector")

    raising = sp.Matrix([[0, 1], [0, 0]])
    lowering = raising.T
    hopping = sp.kronecker_product(raising, lowering) + sp.kronecker_product(lowering, raising)
    hop_commutator = hopping * projectors[0] - projectors[0] * hopping
    check("P05", hop_commutator != sp.zeros(4, 4), "ordinary hopping also fails the same-carrier permanence demand")


def unitary_formation_checks() -> None:
    # Two-dimensional blank and record sectors.  Block-diagonal unitaries
    # preserve records but have no blank-to-record matrix element.
    blank_unitary = sp.Matrix([[0, 1], [1, 0]])
    record_unitary = sp.Matrix([[1, 0], [0, -1]])
    preserving = sp.diag(blank_unitary, record_unitary)
    check("U01", preserving.H * preserving == sp.eye(4), "block-diagonal permanence witness is unitary")
    check("U02", preserving[2:4, 0:2] == sp.zeros(2, 2), "a reducing record sector has zero blank-to-record formation block")

    # A swap between blank and record sectors forms a record but maps an old
    # record back to blank, violating permanence.
    forming = sp.zeros(4, 4)
    forming[0:2, 2:4] = sp.eye(2)
    forming[2:4, 0:2] = sp.eye(2)
    check("U03", forming.H * forming == sp.eye(4), "blank-record sector swap is unitary")
    check("U04", forming[0:2, 2:4] != sp.zeros(2, 2), "formation witness violates invariance of the record sector")


def instrument_checks() -> None:
    p = sp.Matrix([1, 0])
    projector = p * p.H
    vectors = [
        sp.Matrix([sp.Rational(1, 6), sp.I / 5]),
        sp.Matrix([sp.Rational(1, 8) + sp.I / 12, -sp.Rational(1, 7)]),
    ]
    kraus = [p * vector.H for vector in vectors]
    effect = sum((vector * vector.H for vector in vectors), sp.zeros(2, 2))

    r00, r11, u, v = sp.symbols("r00 r11 u v", real=True)
    rho = sp.Matrix([[r00, u + sp.I * v], [u - sp.I * v, r11]])
    operation = sum((operator * rho * operator.H for operator in kraus), sp.zeros(2, 2))
    normal_form = sp.trace(effect * rho) * projector
    check("J01", sp.simplify(operation - normal_form) == sp.zeros(2, 2), "locked-output Kraus operation equals Tr(E rho) P exactly")
    check("J02", sp.simplify((I2 - projector) * operation) == sp.zeros(2, 2), "operation output is supported on the locked rank-one record")
    check("J03", effect.det() > 0 and effect.trace() > 0, "constructed effect is positive definite")
    complement = I2 - effect
    check("J04", complement[0, 0] > 0 and complement.det() > 0, "constructed effect obeys E less-than-or-equal-to I")
    check("J05", sp.simplify(sp.trace(operation) - sp.trace(effect * rho)) == 0, "formation weight is the effect functional")

    effect_1 = sp.diag(sp.Rational(1, 3), sp.Rational(2, 3))
    effect_2 = PX / 2
    check("J06", effect_1 != effect_2, "permanence and locked output admit inequivalent formation effects")
    check("J07", effect_1.is_positive_semidefinite and effect_2.is_positive_semidefinite, "both alternative effects define valid positive weights")
    check("J08", (I2 - effect_1).is_positive_semidefinite and (I2 - effect_2).is_positive_semidefinite, "both alternative effects are trace-nonincreasing")


def main() -> int:
    history_checks()
    commutant_checks()
    unitary_formation_checks()
    instrument_checks()
    print("BOUNDARY: record-equivalence is operational; deleting record-null ontology requires a separate criterion.")
    print("BOUNDARY: the rank-one outcome-operation normal form fixes neither E, full-instrument normalization, firing site/rate, nor coherent evolution.")
    print("BOUNDARY: same-carrier permanence excludes both SWAP and ordinary hopping, so it is not a Dirac selector.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
