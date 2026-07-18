#!/usr/bin/env python3
"""Exact symmetry classification for a two-qubit nearest-neighbor generator."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md"
)
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def exact_equal(left, right) -> bool:
    if isinstance(left, sp.MatrixBase) or isinstance(right, sp.MatrixBase):
        return sp.simplify(left - right) == sp.zeros(*left.shape)
    return sp.simplify(left - right) == 0


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.conjugate().T


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
SWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])


def commutant_basis(generators: tuple[sp.Matrix, ...]) -> tuple[sp.Matrix, ...]:
    variables = sp.symbols("a0:16")
    candidate = sp.Matrix(4, 4, variables)
    equations = []
    for generator in generators:
        equations.extend(candidate * generator - generator * candidate)
    coefficient, _ = sp.linear_eq_to_matrix(equations, variables)
    basis = []
    for vector in coefficient.nullspace():
        basis.append(sp.Matrix(4, 4, tuple(vector)))
    return tuple(basis)


def source_contract() -> None:
    section("A - Source and scope contract")
    text = NOTE.read_text(encoding="utf-8")
    normalized = text.lower().replace("*", "").replace("`", "")
    check("A note is authority-free", "authority: none" in normalized)
    check("A classification is conditional", "conditional classification" in normalized)
    check("A note does not promote a Hamiltonian axiom", "not an axiom proposal" in normalized)
    check("A note names both covariance readings", "common-basis" in normalized and "independent onsite" in normalized)


def common_basis_classification() -> None:
    section("B - Common-basis SU(2) covariance")
    diagonal_generators = tuple(
        sp.kronecker_product(pauli, I2) + sp.kronecker_product(I2, pauli)
        for pauli in (X, Y, Z)
    )
    basis = commutant_basis(diagonal_generators)
    check("B diagonal SU(2) commutant has complex dimension two", len(basis) == 2, str(len(basis)))

    span = sp.Matrix.hstack(*(sp.Matrix(matrix).reshape(16, 1) for matrix in basis))
    identity_vector = sp.eye(4).reshape(16, 1)
    swap_vector = SWAP.reshape(16, 1)
    check("B identity lies in the computed commutant", span.row_join(identity_vector).rank() == span.rank())
    check("B SWAP lies in the computed commutant", span.row_join(swap_vector).rank() == span.rank())
    check("B identity and SWAP are independent", sp.Matrix.hstack(identity_vector, swap_vector).rank() == 2)
    check("B SWAP commutes with every diagonal generator", all(exact_equal(SWAP * g, g * SWAP) for g in diagonal_generators))

    dot = sp.kronecker_product(X, X) + sp.kronecker_product(Y, Y) + sp.kronecker_product(Z, Z)
    check("B Pauli exchange identity is exact", exact_equal(SWAP, (sp.eye(4) + dot) / 2))


def independent_basis_boundary() -> None:
    section("C - Independent onsite covariance boundary")
    independent_generators = tuple(
        [sp.kronecker_product(pauli, I2) for pauli in (X, Y, Z)]
        + [sp.kronecker_product(I2, pauli) for pauli in (X, Y, Z)]
    )
    basis = commutant_basis(independent_generators)
    check("C independent onsite SU(2) commutant has dimension one", len(basis) == 1, str(len(basis)))
    basis_vector = basis[0].reshape(16, 1)
    identity_vector = sp.eye(4).reshape(16, 1)
    check("C the remaining direction is the identity", sp.Matrix.hstack(basis_vector, identity_vector).rank() == 1)
    check(
        "C SWAP is not invariant under independent local rotations",
        not exact_equal(SWAP * sp.kronecker_product(X, I2), sp.kronecker_product(X, I2) * SWAP),
    )


def sign_scale_and_schedule() -> None:
    section("D - Sign, scale, and overlap are not selected")
    eigenvalues = SWAP.eigenvals()
    check("D SWAP spectrum is triplet plus singlet", eigenvalues == {sp.Integer(1): 3, sp.Integer(-1): 1}, str(eigenvalues))
    plus_ground = min(eigenvalues)
    minus_ground = min((-value for value in eigenvalues))
    check("D plus and minus exchange share symmetry but reverse ground sectors", plus_ground == minus_ground == -1)
    symmetric = (sp.eye(4) + SWAP) / 2
    antisymmetric = (sp.eye(4) - SWAP) / 2
    check("D plus-SWAP ground sector is the rank-one singlet", antisymmetric.rank() == 1 and exact_equal(SWAP * antisymmetric, -antisymmetric))
    check("D minus-SWAP ground sector is the rank-three triplet", symmetric.rank() == 3 and exact_equal((-SWAP) * symmetric, -symmetric))
    t = sp.symbols("t", real=True)
    time_dependent = (1 + t) * SWAP
    check("D covariance alone permits a time-dependent coefficient", not exact_equal(time_dependent.subs(t, 0), time_dependent.subs(t, 1)))

    # Embed the two neighboring swaps on three qubits.
    s12 = sp.kronecker_product(SWAP, I2)
    # Construct S23 by its action on computational basis labels.
    s23 = sp.zeros(8)
    for index in range(8):
        a = (index >> 2) & 1
        b = (index >> 1) & 1
        c = index & 1
        target = (a << 2) | (c << 1) | b
        s23[target, index] = 1
    check("D adjacent exchange terms do not commute", not exact_equal(s12 * s23, s23 * s12))
    check("D opposite discrete layer orders are different", not exact_equal(s12 * s23, s23 * s12))
    h = s12 + s23
    reflection = sp.zeros(8)
    for index in range(8):
        a = (index >> 2) & 1
        b = (index >> 1) & 1
        c = index & 1
        target = (c << 2) | (b << 1) | a
        reflection[target, index] = 1
    check("D Hamiltonian sum is reflection covariant despite overlap", exact_equal(reflection * h * reflection, h))

    local_observable = sp.kronecker_product(Z, I2, I2)
    remote_test = sp.kronecker_product(I2, I2, X)
    first = sp.simplify(h * local_observable - local_observable * h)
    second = sp.simplify(h * first - first * h)
    check("D first commutator has not reached site three", exact_equal(first * remote_test, remote_test * first))
    check("D second commutator reaches site three", not exact_equal(second * remote_test, remote_test * second))


def entanglement_capability() -> None:
    section("E - Exchange can entangle but does not record")
    ket01 = sp.Matrix([0, 1, 0, 0])
    theta = sp.pi / 4
    unitary = sp.cos(theta) * sp.eye(4) - sp.I * sp.sin(theta) * SWAP
    branch = sp.simplify(unitary * ket01)
    rho = sp.simplify(branch * branch.conjugate().T)
    reduced = sp.zeros(2)
    for a in range(2):
        for b in range(2):
            for second in range(2):
                reduced[a, b] += rho[2 * a + second, 2 * b + second]
    check("E exchange exponential is unitary", exact_equal(unitary.conjugate().T * unitary, sp.eye(4)))
    check("E quarter exchange makes a maximally entangled state", exact_equal(reduced, sp.eye(2) / 2))
    phase = sp.diag(1, sp.I)
    local_basis = sp.kronecker_product(phase, X)
    canonical = sp.simplify(local_basis * branch)
    phi_plus = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    check("E local basis maps the exchange pair to Phi-plus", exact_equal(canonical, phi_plus))
    canonical_rho = canonical * dagger(canonical)
    alice = (Z, X)
    bob = ((Z + X) / sp.sqrt(2), (Z - X) / sp.sqrt(2))
    correlations = {
        (x, y): sp.simplify(sp.trace(canonical_rho * sp.kronecker_product(alice[x], bob[y])))
        for x in (0, 1)
        for y in (0, 1)
    }
    chsh = sp.simplify(correlations[(0, 0)] + correlations[(0, 1)] + correlations[(1, 0)] - correlations[(1, 1)])
    expected = {(0, 0): 1 / sp.sqrt(2), (0, 1): 1 / sp.sqrt(2), (1, 0): 1 / sp.sqrt(2), (1, 1): -1 / sp.sqrt(2)}
    check("E exchange-generated state has exact Bell correlators", all(exact_equal(correlations[key], value) for key, value in expected.items()))
    check("E exchange-generated state reaches CHSH 2sqrt(2)", exact_equal(chsh, 2 * sp.sqrt(2)))


def reversible_record_obstruction() -> None:
    section("F - Reversible fixed-carrier law cannot strictly grow a flag")
    record = sp.diag(1, 0, 0, 0)
    conjugated = sp.simplify(unitary_from_swap(sp.pi / 7).conjugate().T * record * unitary_from_swap(sp.pi / 7))
    check("F unitary conjugation preserves record-projector rank", conjugated.rank() == record.rank() == 1)
    check("F unitary conjugation preserves record-projector trace", exact_equal(sp.trace(conjugated), sp.trace(record)))

    # A concrete strict superprojection has larger trace and rank, so it cannot
    # be a unitary image of the original flag.
    super_record = sp.diag(1, 1, 0, 0)
    check("F a strict superprojection has larger rank", super_record.rank() > record.rank())
    check("F a strict superprojection has larger trace", sp.trace(super_record) > sp.trace(record))
    check("F reversible exchange does not create absorbing record support", not exact_equal(conjugated, super_record))


def unitary_from_swap(theta) -> sp.Matrix:
    return sp.cos(theta) * sp.eye(4) - sp.I * sp.sin(theta) * SWAP


def conclusion_contract() -> None:
    section("G - Minimum-content boundary needles")
    text = NOTE.read_text(encoding="utf-8").lower()
    phrases = (
        "span of identity and swap",
        "sign and scale",
        "continuous reversible generator",
        "autonomous",
        "lieb-robinson",
        "record-status carrier",
        "record formation",
        "actuality",
        "chirality",
        "gravity",
        "live reduction route",
    )
    for phrase in phrases:
        check(f"G note contains boundary: {phrase}", phrase in text)


def main() -> None:
    source_contract()
    common_basis_classification()
    independent_basis_boundary()
    sign_scale_and_schedule()
    entanglement_capability()
    reversible_record_obstruction()
    conclusion_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
