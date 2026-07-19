#!/usr/bin/env python3
"""Exact finite-CAR checks for the supplied even-bond walk-bound note.

This is deliberately a proof/data-only runner.  It reads no Markdown,
registry, ledger, queue, or other mutable repository source.  The runner
cache therefore has exactly one freshness input: this file's SHA-256.
"""

from __future__ import annotations

import itertools

import sympy as sp


EXPECTED_GATES = 31


class CheckRunner:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: object) -> None:
        if bool(condition):
            self.passed += 1
            print(f"PASS: {label}")
        else:
            self.failed += 1
            print(f"FAIL: {label}")

    def finish(self) -> int:
        total = self.passed + self.failed
        if total != EXPECTED_GATES:
            print(
                f"FAIL: gate-manifest drift: ran {total}, "
                f"expected {EXPECTED_GATES}"
            )
            self.failed += 1
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
ANN = sp.Matrix([[0, 1], [0, 0]])
N_SITES = 4


def kron(*mats: sp.MatrixBase) -> sp.Matrix:
    out = mats[0]
    for mat in mats[1:]:
        out = sp.Matrix(sp.kronecker_product(out, mat))
    return sp.Matrix(out)


def com(a: sp.MatrixBase, b: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(a * b - b * a)


def acom(a: sp.MatrixBase, b: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(a * b + b * a)


def graded_com(
    a: sp.MatrixBase,
    b: sp.MatrixBase,
    parity_a: int,
    parity_b: int,
) -> sp.Matrix:
    return sp.Matrix(a * b - ((-1) ** (parity_a * parity_b)) * b * a)


def is_zero(mat: sp.MatrixBase) -> bool:
    return sp.simplify(mat) == sp.zeros(*mat.shape)


def op_norm_sq(mat: sp.MatrixBase) -> sp.Expr:
    eigenvalues = list((mat.H * mat).eigenvals())
    return max(eigenvalues, key=lambda value: float(sp.N(value)))


def c_op(site: int) -> sp.Matrix:
    return kron(
        *(
            [SZ] * site
            + [ANN]
            + [I2] * (N_SITES - site - 1)
        )
    )


def generated_family(generators: list[sp.Matrix]) -> list[tuple[sp.Matrix, int]]:
    family: list[tuple[sp.Matrix, int]] = [(sp.eye(2**N_SITES), 0)]
    for degree in range(1, len(generators) + 1):
        for indices in itertools.combinations(range(len(generators)), degree):
            word = generators[indices[0]]
            for index in indices[1:]:
                word = word * generators[index]
            family.append((sp.Matrix(word), degree % 2))
    return family


def family_rank(family: list[tuple[sp.Matrix, int]]) -> int:
    columns = [matrix.reshape(matrix.rows * matrix.cols, 1) for matrix, _ in family]
    return int(sp.Matrix.hstack(*columns).rank())


def family_nonzero_and_unique(family: list[tuple[sp.Matrix, int]]) -> bool:
    matrices = [matrix for matrix, _ in family]
    nonzero = all(not is_zero(matrix) for matrix in matrices)
    unique = all(
        not is_zero(matrices[i] - matrices[j])
        for i in range(len(matrices))
        for j in range(i + 1, len(matrices))
    )
    return nonzero and unique


def sign_law_statistics(
    left: list[tuple[sp.Matrix, int]],
    right: list[tuple[sp.Matrix, int]],
) -> tuple[int, int]:
    correct_failures = 0
    wrong_failures = 0
    for a_mat, parity_a in left:
        for b_mat, parity_b in right:
            correct = (-1) ** (parity_a * parity_b)
            wrong = (-1) ** (parity_a + parity_b)
            if not is_zero(a_mat * b_mat - correct * b_mat * a_mat):
                correct_failures += 1
            if not is_zero(a_mat * b_mat - wrong * b_mat * a_mat):
                wrong_failures += 1
    return correct_failures, wrong_failures


def adjoint_chain(hamiltonian: sp.Matrix, source: sp.Matrix, order: int) -> list[sp.Matrix]:
    chain = [source]
    for _ in range(order):
        chain.append(com(hamiltonian, chain[-1]))
    return chain


def canonical_bond(a: tuple[int, int, int], b: tuple[int, int, int]):
    return tuple(sorted((a, b)))


def incident_bonds(site: tuple[int, int, int]):
    steps = (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    )
    return {
        canonical_bond(site, tuple(site[i] + step[i] for i in range(3)))
        for step in steps
    }


def main() -> int:
    checks = CheckRunner()

    c = [c_op(site) for site in range(N_SITES)]
    cd = [operator.H for operator in c]
    identity = sp.eye(2**N_SITES)
    zero = sp.zeros(2**N_SITES, 2**N_SITES)
    parity = kron(SZ, SZ, SZ, SZ)

    car_holds = True
    for i in range(N_SITES):
        for j in range(N_SITES):
            car_holds &= is_zero(acom(c[i], c[j]))
            car_holds &= is_zero(acom(cd[i], cd[j]))
            target = identity if i == j else zero
            car_holds &= is_zero(acom(c[i], cd[j]) - target)
    checks.check("CAR relations hold for every ordered four-site generator pair", car_holds)

    left = generated_family([c[0], cd[0], c[1], cd[1]])
    right = generated_family([c[2], cd[2], c[3], cd[3]])
    checks.check(
        "Two disjoint two-site PBW families each contain sixteen representatives",
        len(left) == 16 and len(right) == 16,
    )
    checks.check(
        "Each PBW family has full rank sixteen",
        family_rank(left) == 16 and family_rank(right) == 16,
    )
    checks.check(
        "Each PBW representative is nonzero and pairwise distinct",
        family_nonzero_and_unique(left) and family_nonzero_and_unique(right),
    )
    correct_failures, wrong_failures = sign_law_statistics(left, right)
    checks.check(
        "All 256 PBW pairs obey the graded sign and 192 reject the p-plus-q sign",
        correct_failures == 0 and wrong_failures == 192,
    )

    duplicate_left = generated_family([c[0], cd[0], c[1], c[1]])
    duplicate_correct_failures, _ = sign_law_statistics(duplicate_left, right)
    checks.check(
        "PBW rank gate kills a duplicated-generator mutation missed by a bare sign check",
        duplicate_correct_failures == 0
        and family_rank(duplicate_left) == 8
        and not family_nonzero_and_unique(duplicate_left),
    )

    hop01 = cd[0] * c[1] + cd[1] * c[0]
    hop12 = cd[1] * c[2] + cd[2] * c[1]
    hop23 = cd[2] * c[3] + cd[3] * c[2]
    pairing01 = cd[0] * cd[1] + c[1] * c[0]
    ham = sp.Matrix(hop01 + hop12 + hop23)
    n0 = cd[0] * c[0]
    n2 = cd[2] * c[2]
    n3 = cd[3] * c[3]
    odd0 = c[0] + cd[0]
    odd3 = c[3] + cd[3]
    odd3_conjugate = sp.I * (c[3] - cd[3])

    checks.check(
        "Even disjoint CAR elements commute with both observable parities",
        is_zero(com(hop01, hop23))
        and is_zero(com(hop01, n3))
        and is_zero(com(hop01, odd3)),
    )
    checks.check(
        "Odd disjoint CAR elements anticommute and need not commute",
        is_zero(acom(odd0, odd3)) and not is_zero(com(odd0, odd3)),
    )
    checks.check(
        "Hopping and pairing bonds are Hermitian, even, norm one, and disjoint-local",
        is_zero(hop01 - hop01.H)
        and is_zero(pairing01 - pairing01.H)
        and is_zero(com(hop01, parity))
        and is_zero(com(pairing01, parity))
        and sp.simplify(op_norm_sq(hop01) - 1) == 0
        and sp.simplify(op_norm_sq(pairing01) - 1) == 0
        and is_zero(com(pairing01, odd3))
        and is_zero(com(pairing01, n3)),
    )
    checks.check(
        "An odd Hermitian disjoint term breaks ordinary boundary reduction",
        is_zero(odd0 - odd0.H)
        and is_zero(acom(odd0, odd3))
        and not is_zero(com(odd0, odd3)),
    )

    n0_chain = adjoint_chain(ham, sp.Matrix(n0), 3)
    odd0_chain = adjoint_chain(ham, sp.Matrix(odd0), 3)
    checks.check(
        "Even-source ordinary commutators vanish through order two and arrive at three",
        tuple(op_norm_sq(com(term, odd3)) for term in n0_chain) == (0, 0, 0, 1),
    )
    checks.check(
        "Odd-odd graded commutators vanish through order two and arrive at three",
        all(
            is_zero(graded_com(term, odd3_conjugate, 1, 1))
            for term in odd0_chain[:3]
        )
        and not is_zero(
            graded_com(odd0_chain[3], odd3_conjugate, 1, 1)
        ),
    )
    checks.check(
        "Odd-odd ordinary Taylor coefficients do not obey a distance-three start",
        tuple(op_norm_sq(com(term, odd3)) for term in odd0_chain) == (4, 4, 8, 20),
    )
    hop01_chain = adjoint_chain(ham, sp.Matrix(hop01), 2)
    checks.check(
        "Even-bond inhomogeneity reaches the odd probe only at recursive order two",
        tuple(op_norm_sq(com(term, odd3)) for term in hop01_chain) == (0, 0, 1),
    )

    jacobi_left = com(com(ham, odd0), odd3)
    jacobi_homogeneous = com(ham, com(odd0, odd3))
    jacobi_source = com(odd0, com(ham, odd3))
    checks.check(
        "Odd-source flow splits exactly into homogeneous transport and inhomogeneity",
        is_zero(jacobi_left - jacobi_homogeneous + jacobi_source)
        and not is_zero(jacobi_homogeneous)
        and not is_zero(jacobi_source),
    )
    unitary = kron(SX, I2, I2, I2)
    transported = unitary * com(odd0, odd3) * unitary.H
    checks.check(
        "Unitary homogeneous transport preserves the initial commutator norm",
        is_zero(unitary.H * unitary - identity)
        and op_norm_sq(transported) == op_norm_sq(com(odd0, odd3)),
    )
    checks.check(
        "Even Hamiltonian adjoints preserve both even and odd parity sectors",
        all(is_zero(com(term, parity)) for term in n0_chain)
        and all(is_zero(acom(term, parity)) for term in odd0_chain),
    )

    checks.check(
        "Fermionic boundary reduction removes both far bonds from the local density flow",
        is_zero(com(hop12, n0))
        and is_zero(com(hop23, n0))
        and is_zero(com(ham, n0) - com(hop01, n0))
        and not is_zero(com(hop01, n0)),
    )
    checks.check(
        "Self-bond deletion leaves the adjacent reduced generator contribution",
        is_zero(com(hop01, hop01))
        and is_zero(com(ham, hop01) - com(hop12, hop01))
        and not is_zero(com(hop12, hop01)),
    )
    reduced_generator = hop01 + hop12
    checks.check(
        "Reduced generator sums remain Hermitian and even",
        is_zero(reduced_generator - reduced_generator.H)
        and is_zero(com(reduced_generator, parity)),
    )

    hop13 = cd[1] * c[3] + cd[3] * c[1]
    bare_x2 = kron(I2, I2, SX, I2)
    checks.check(
        "Fixed-order JW image of a nonadjacent hop is not supported on its endpoint qubits",
        not is_zero(com(hop13, bare_x2)),
    )
    checks.check(
        "The same nonadjacent hop remains intrinsically CAR-local at the intermediate site",
        is_zero(com(hop13, c[2]))
        and is_zero(com(hop13, cd[2]))
        and is_zero(com(hop13, n2)),
    )

    origin = (0, 0, 0)
    neighbor = (1, 0, 0)
    first_bonds = incident_bonds(origin)
    adjacent_nonself = (incident_bonds(origin) | incident_bonds(neighbor)) - {
        canonical_bond(origin, neighbor)
    }
    checks.check(
        "Cubic nearest-neighbor geometry gives six first bonds and ten nonself continuations",
        len(first_bonds) == 6 and len(adjacent_nonself) == 10,
    )
    checks.check(
        "Four-site exact chains distinguish below-cone orders from distance-three arrival",
        all(is_zero(com(term, n3)) for term in n0_chain[:3])
        and not is_zero(com(n0_chain[3], n3)),
    )

    j_sym, n_sym = sp.symbols("J n_X", positive=True)
    checks.check(
        "Walk coefficient assembles as (2J)^k n_X 10^(k-1)=(n_X/10)(20J)^k",
        all(
            sp.simplify(
                (2 * j_sym) ** order * n_sym * 10 ** (order - 1)
                - (n_sym / 10) * (20 * j_sym) ** order
            )
            == 0
            for order in range(1, 9)
        ),
    )
    checks.check(
        "Factorial-tail coefficient domination holds on an exact integer grid",
        all(
            sp.factorial(distance) / sp.factorial(order)
            <= 1 / sp.factorial(order - distance)
            for distance in range(0, 9)
            for order in range(distance, 13)
        ),
    )
    x_sym, mu_sym = sp.symbols("x mu", positive=True)
    checks.check(
        "Exponential reweighting identity is exact at every tested tail order",
        all(
            sp.simplify(
                sp.exp(-mu_sym * order)
                * (x_sym * sp.exp(mu_sym)) ** order
                - x_sym**order
            )
            == 0
            for order in range(0, 9)
        ),
    )

    disconnected_ham = sp.Matrix(hop01 + hop23)
    disconnected_source = adjoint_chain(disconnected_ham, sp.Matrix(hop01), 3)
    checks.check(
        "Disconnected components have zero graded and inhomogeneous cross-component tails",
        all(is_zero(graded_com(term, odd3, 0, 1)) for term in disconnected_source)
        and is_zero(graded_com(odd0, odd3, 1, 1)),
    )
    checks.check(
        "Disconnected odd observables retain a nonzero ordinary statistical initial term",
        op_norm_sq(com(odd0, odd3)) == 4,
    )
    checks.check(
        "Empty Hamiltonian leaves the ordinary commutator equal to its initial datum",
        is_zero(com(zero, odd0))
        and is_zero(identity * odd0 * identity - odd0)
        and is_zero(com(identity * odd0 * identity, odd3) - com(odd0, odd3)),
    )

    bounded_family = [sp.Rational(2 * index, index + 1) for index in range(1, 17)]
    cutoff = sp.symbols("M", integer=True, positive=True)
    checks.check(
        "Family use distinguishes finite J-star from the algebraically unbounded J_n=n",
        max(bounded_family) < 2
        and sp.simplify((cutoff + 1) - cutoff) == 1,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
