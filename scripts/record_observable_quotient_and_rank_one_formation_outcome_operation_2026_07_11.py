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


def finite_completion_signature(
    coupling: int,
    couple_law_to_readout: bool = False,
    initial: dict[tuple[int, int, int], sp.Matrix] | None = None,
) -> tuple:
    """Rebuild a finite completion and compute its record-level signature.

    The baseline completion appends H_lambda but does not pass it into the
    successor or readout maps.  The hostile control deliberately exposes one
    Hamiltonian entry to readout so the invariance check is mutation-sensitive.
    The ``initial`` argument supplies the initial record-history support; the
    quotient theorem compares completions only at equal initial support, and
    the premise control varies it.
    """
    hamiltonian = exchange_interaction(coupling)
    path = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
    state: dict[tuple[int, int, int], sp.Matrix] = dict(initial or {})
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

    # Equal-initial-history-support premise control: identical successor
    # conditions, weights, and readouts but a different supplied initial
    # record configuration produce a different record-history signature, so
    # the premise in the quotient theorem is load-bearing.
    baseline = finite_completion_signature(2)
    shifted_initial = finite_completion_signature(2, initial={(10, 0, 0): P0})
    check("R09", baseline != shifted_initial, "unequal initial record-history supports break record equivalence for the same record-null parameter")


def commutant_solution_space(frames: tuple[sp.Matrix, ...]) -> tuple[sp.Matrix, list[sp.Matrix]]:
    variables = sp.symbols("h0:16")
    hamiltonian = sp.Matrix(4, 4, variables)
    lifted = [sp.kronecker_product(frame, I2) for frame in frames]
    equations = []
    for lift in lifted:
        equations.extend(list(hamiltonian * lift - lift * hamiltonian))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    return coefficient_matrix, coefficient_matrix.nullspace()


def commutant_checks() -> None:
    # Supplied recordable-frame spanning condition: the four recordable frames
    # used here linearly span M_2(C).  The theorem states this as a supplied
    # zero-premise-weight condition; the check verifies the runner instance
    # satisfies it.
    frames = (P0, P1, PX, PY)
    frame_span = sp.Matrix.hstack(*(sp.Matrix(list(frame)) for frame in frames))
    check("P00", frame_span.rank() == 4, "the four recordable frames linearly span M_2(C), realizing the supplied spanning condition")

    coefficient_matrix, nullspace = commutant_solution_space(frames)
    check("P01", coefficient_matrix.rank() == 12, "four spanning rank-one record frames impose rank 12 on a 16-dimensional two-site operator")
    check("P02", len(nullspace) == 4, "same-carrier record-preserving commutant has dimension four")

    # Direct structural verification, independent of the linear system: every
    # nullspace element has the exact block form I_site tensor B.
    structural = True
    for vector in nullspace:
        matrix = sp.Matrix(4, 4, list(vector))
        structural &= matrix[0:2, 2:4] == sp.zeros(2, 2)
        structural &= matrix[2:4, 0:2] == sp.zeros(2, 2)
        structural &= sp.simplify(matrix[0:2, 0:2] - matrix[2:4, 2:4]) == sp.zeros(2, 2)
    check("P03a", structural, "every commutant solution has the exact block form I_site tensor B")

    # Reverse membership, also independent of the linear system: every
    # I tensor E_ij commutes with every lifted recordable frame.
    membership = True
    for row, column in itertools.product(range(2), repeat=2):
        matrix_unit = sp.zeros(2, 2)
        matrix_unit[row, column] = 1
        candidate = sp.kronecker_product(I2, matrix_unit)
        for frame in frames:
            lift = sp.kronecker_product(frame, I2)
            membership &= sp.simplify(candidate * lift - lift * candidate) == sp.zeros(4, 4)
    check("P03b", membership, "every I_site tensor matrix-unit commutes directly with all four lifted frames")

    # Mutation control: an operator acting nontrivially on the record site is
    # rejected by the same direct commutator test.
    intruder = sp.kronecker_product(P0, I2)
    lift_x = sp.kronecker_product(PX, I2)
    check("P03c", sp.simplify(intruder * lift_x - lift_x * intruder) != sp.zeros(4, 4), "a site-nontrivial operator fails the direct frame-commutation test")

    # Non-spanning control: dropping to the commuting two-frame family leaves
    # a strictly larger commutant, so the spanning condition is load-bearing.
    _, partial_nullspace = commutant_solution_space((P0, P1))
    check("P06", len(partial_nullspace) == 8, "a non-spanning recordable family leaves an eight-dimensional commutant")

    swap = sp.zeros(4, 4)
    for left, right in itertools.product(range(2), repeat=2):
        source = 2 * left + right
        target = 2 * right + left
        swap[target, source] = 1
    lift_p0 = sp.kronecker_product(P0, I2)
    commutator = swap * lift_p0 - lift_p0 * swap
    check("P04", commutator != sp.zeros(4, 4), "SWAP does not preserve an arbitrary locked local record projector")

    raising = sp.Matrix([[0, 1], [0, 0]])
    lowering = raising.T
    hopping = sp.kronecker_product(raising, lowering) + sp.kronecker_product(lowering, raising)
    hop_commutator = hopping * lift_p0 - lift_p0 * hopping
    check("P05", hop_commutator != sp.zeros(4, 4), "ordinary hopping also fails the same-carrier permanence demand")


def unitary_formation_checks() -> None:
    # Two-dimensional blank and record sectors.  Block-diagonal unitaries
    # preserve records but have no blank-to-record matrix element.  U01-U04
    # are explicit witnesses of the two sides of the dichotomy; the universal
    # content is checked by U05-U07 below.
    blank_unitary = sp.Matrix([[0, 1], [1, 0]])
    record_unitary = sp.Matrix([[1, 0], [0, -1]])
    preserving = sp.diag(blank_unitary, record_unitary)
    check("U01", preserving.H * preserving == sp.eye(4), "block-diagonal permanence witness is unitary")
    check("U02", preserving[2:4, 0:2] == sp.zeros(2, 2), "the block-diagonal witness has zero blank-to-record formation block")

    # A swap between blank and record sectors forms a record but maps an old
    # record back to blank, violating permanence.
    forming = sp.zeros(4, 4)
    forming[0:2, 2:4] = sp.eye(2)
    forming[2:4, 0:2] = sp.eye(2)
    check("U03", forming.H * forming == sp.eye(4), "blank-record sector swap is unitary")
    check("U04", forming[0:2, 2:4] != sp.zeros(2, 2), "formation witness violates invariance of the record sector")

    # Universal check on the one-blank/one-record cell: for the general U(2)
    # parameterization, the formation-block norm equals the record-leakage
    # norm identically, so record invariance (zero leakage) forces zero
    # formation for EVERY unitary, not only the displayed witnesses.
    phi, alpha, beta, gamma = sp.symbols("phi alpha beta gamma", real=True)
    general_unitary = sp.Matrix(
        [
            [sp.cos(phi) * sp.exp(sp.I * alpha), sp.sin(phi) * sp.exp(sp.I * beta)],
            [-sp.sin(phi) * sp.exp(sp.I * gamma), sp.cos(phi) * sp.exp(sp.I * (beta + gamma - alpha))],
        ]
    )
    unitary_ok = sp.simplify(general_unitary.H * general_unitary - sp.eye(2)) == sp.zeros(2, 2)
    formation_norm = sp.simplify(sp.Abs(general_unitary[1, 0]) ** 2)
    leakage_norm = sp.simplify(sp.Abs(general_unitary[0, 1]) ** 2)
    check("U05", unitary_ok and sp.simplify(formation_norm - leakage_norm) == 0, "general U(2) has formation-block norm identically equal to record-leakage norm")

    # Sampled higher-dimensional confirmation of the same norm identity for
    # unequal blank/record splits, plus a non-unitary control for which the
    # identity fails, so the check is sensitive to the unitarity hypothesis.
    rng = np.random.default_rng(20260716)
    identity_ok = True
    for total, record_dim in ((4, 2), (5, 3), (6, 2)):
        for _ in range(8):
            random_matrix = rng.normal(size=(total, total)) + 1j * rng.normal(size=(total, total))
            unitary, _ = np.linalg.qr(random_matrix)
            blank_dim = total - record_dim
            formation_block = unitary[blank_dim:, :blank_dim]
            leakage_block = unitary[:blank_dim, blank_dim:]
            identity_ok &= abs(
                np.linalg.norm(formation_block) ** 2 - np.linalg.norm(leakage_block) ** 2
            ) < 1.0e-12
    check("U06", identity_ok, "sampled unitaries satisfy the formation/leakage norm identity on unequal sector splits")

    non_unitary = sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )
    control_leakage = non_unitary[0:2, 2:4]
    control_formation = non_unitary[2:4, 0:2]
    check("U07", control_leakage == sp.zeros(2, 2) and control_formation != sp.zeros(2, 2), "a non-unitary control preserves the record sector yet forms records, so the identity genuinely needs unitarity")


def instrument_checks() -> None:
    p = sp.Matrix([1, 0])
    projector = p * p.H
    r00, r11, u, v = sp.symbols("r00 r11 u v", real=True)
    rho = sp.Matrix([[r00, u + sp.I * v], [u - sp.I * v, r11]])

    # Forward direction on a fully generic symbolic Kraus operator: the
    # locked-output condition (I-P) J(rho) (I-P) = 0 for generic rho forces
    # the bottom row of K to vanish, i.e. K = |p><v|.  The expectation is not
    # assembled from the tested formula: the condition is imposed and solved.
    k_symbols = sp.symbols("k00r k00i k01r k01i k10r k10i k11r k11i", real=True)
    k00 = k_symbols[0] + sp.I * k_symbols[1]
    k01 = k_symbols[2] + sp.I * k_symbols[3]
    k10 = k_symbols[4] + sp.I * k_symbols[5]
    k11 = k_symbols[6] + sp.I * k_symbols[7]
    generic_kraus = sp.Matrix([[k00, k01], [k10, k11]])
    outside = sp.expand(((I2 - projector) * generic_kraus * rho * generic_kraus.H * (I2 - projector))[1, 1])
    polynomial = sp.Poly(outside, r00, r11, u, v)
    coefficient_map = {tuple(monomial): sp.simplify(coefficient) for monomial, coefficient in polynomial.terms()}
    # The pure-state coefficients are exact sums of squares of real symbols,
    # so requiring the locked-output condition for generic rho forces the
    # entire bottom row of K to vanish.
    forcing = (
        coefficient_map.get((1, 0, 0, 0)) == k_symbols[4] ** 2 + k_symbols[5] ** 2
        and coefficient_map.get((0, 1, 0, 0)) == k_symbols[6] ** 2 + k_symbols[7] ** 2
    )
    check("J00", forcing, "the locked-output condition on a generic symbolic Kraus operator forces its bottom row to vanish, hence K=|p><v|")
    reduced_kraus = generic_kraus.subs({k_symbols[4]: 0, k_symbols[5]: 0, k_symbols[6]: 0, k_symbols[7]: 0})
    residual_vector = sp.Matrix([sp.conjugate(k00), sp.conjugate(k01)])
    check("J00b", sp.simplify(reduced_kraus - p * residual_vector.H) == sp.zeros(2, 2), "the forced solution is exactly the rank-one form K=|p><v|")

    # Converse direction with a symbolic two-operator family K_j=|p><v_j|.
    v_symbols = sp.symbols("v1r v1i v2r v2i v3r v3i v4r v4i", real=True)
    vectors = [
        sp.Matrix([v_symbols[0] + sp.I * v_symbols[1], v_symbols[2] + sp.I * v_symbols[3]]),
        sp.Matrix([v_symbols[4] + sp.I * v_symbols[5], v_symbols[6] + sp.I * v_symbols[7]]),
    ]
    kraus = [p * vector.H for vector in vectors]
    effect = sum((vector * vector.H for vector in vectors), sp.zeros(2, 2))
    operation = sum((operator * rho * operator.H for operator in kraus), sp.zeros(2, 2))
    normal_form = sp.trace(effect * rho) * projector
    check("J01", sp.simplify(operation - normal_form) == sp.zeros(2, 2), "a symbolic locked-output Kraus family equals Tr(E rho) P identically")
    check("J02", sp.simplify((I2 - projector) * operation) == sp.zeros(2, 2), "the symbolic operation output is supported on the locked rank-one record")

    # Mutation control: one Kraus operator with support outside the locked
    # record violates the locked-output condition on an explicit input.
    bad_kraus = sp.Matrix([[1, 0], [1, 0]]) / sp.sqrt(2)
    bad_output = bad_kraus * projector * bad_kraus.H
    check("J02c", sp.simplify((I2 - projector) * bad_output * (I2 - projector)) != sp.zeros(2, 2), "a Kraus operator with off-record support is rejected by the locked-output condition")

    numeric_vectors = [
        sp.Matrix([sp.Rational(1, 6), sp.I / 5]),
        sp.Matrix([sp.Rational(1, 8) + sp.I / 12, -sp.Rational(1, 7)]),
    ]
    numeric_effect = sum((vector * vector.H for vector in numeric_vectors), sp.zeros(2, 2))
    numeric_kraus = [p * vector.H for vector in numeric_vectors]
    numeric_operation = sum((operator * rho * operator.H for operator in numeric_kraus), sp.zeros(2, 2))
    check("J03", numeric_effect.det() > 0 and numeric_effect.trace() > 0, "constructed effect is positive definite")
    complement = I2 - numeric_effect
    check("J04", complement[0, 0] > 0 and complement.det() > 0, "constructed effect obeys E less-than-or-equal-to I")
    check("J05", sp.simplify(sp.trace(numeric_operation) - sp.trace(numeric_effect * rho)) == 0, "formation weight is the effect functional")

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
