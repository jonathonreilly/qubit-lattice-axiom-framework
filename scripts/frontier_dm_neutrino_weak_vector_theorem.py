#!/usr/bin/env python3
"""Exact verifier for the finite-dimensional chiral vector theorem.

All load-bearing checks use SymPy matrices over Gaussian rationals. Floating
values are printed only in the SUPPORT lane. The MUTATION lane passes only
when a hostile alteration produces a nonzero residual in a computed
validator.
"""

from __future__ import annotations

import sys
from collections.abc import Iterable, Sequence

import sympy as sp


LANES = ("EXACT", "SUPPORT", "MUTATION")
COUNTS = {lane: {"pass": 0, "fail": 0} for lane in LANES}


def report(lane: str, name: str, condition: bool, detail: str = "") -> bool:
    status = "PASS" if condition else "FAIL"
    COUNTS[lane]["pass" if condition else "fail"] += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}][{lane}] {name}{suffix}")
    return condition


def is_zero_matrix(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def all_zero(residuals: Iterable[sp.MatrixBase]) -> bool:
    return all(is_zero_matrix(residual) for residual in residuals)


def exact(name: str, residuals: Sequence[sp.MatrixBase], detail: str = "") -> bool:
    return report(
        "EXACT",
        name,
        all_zero(residuals),
        detail or f"{len(residuals)} residuals",
    )


def reject_mutation(name: str, residuals: Sequence[sp.MatrixBase]) -> bool:
    nonzero = sum(not is_zero_matrix(residual) for residual in residuals)
    return report(
        "MUTATION",
        name,
        nonzero > 0,
        f"validator found {nonzero}/{len(residuals)} nonzero residuals",
    )


I2 = sp.eye(2)
I8 = sp.eye(8)
I16 = sp.eye(16)

SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])


def kron(*factors: sp.MatrixBase) -> sp.MatrixBase:
    return sp.kronecker_product(*factors)


G_SPATIAL_8 = (
    kron(SX, I2, I2),
    kron(SY, SX, I2),
    kron(SY, SY, SX),
)

G0_16 = kron(SZ, SZ, SZ, SX)
G_SPATIAL_16 = (
    kron(SX, I2, I2, I2),
    kron(SZ, SX, I2, I2),
    kron(SZ, SZ, SX, I2),
)


def commutator(left: sp.MatrixBase, right: sp.MatrixBase) -> sp.MatrixBase:
    return left * right - right * left


def weak_bivectors(gammas: Sequence[sp.MatrixBase]) -> tuple[sp.MatrixBase, ...]:
    result = []
    for a in range(3):
        bivector = sp.zeros(gammas[0].rows)
        for m in range(3):
            for n in range(3):
                bivector += (
                    -sp.I
                    * sp.Rational(1, 4)
                    * sp.LeviCivita(a, m, n)
                    * gammas[m]
                    * gammas[n]
                )
        result.append(bivector)
    return tuple(result)


B_8 = weak_bivectors(G_SPATIAL_8)
B_16 = weak_bivectors(G_SPATIAL_16)

GAMMA5 = G0_16 * G_SPATIAL_16[0] * G_SPATIAL_16[1] * G_SPATIAL_16[2]
P_L = (I16 + GAMMA5) / 2
P_R = (I16 - GAMMA5) / 2
Y = tuple(P_R * gamma * P_L for gamma in G_SPATIAL_16)


VECTOR_TABLE = {
    (0, 1): (1, 2),
    (1, 0): (-1, 2),
    (1, 2): (1, 0),
    (2, 1): (-1, 0),
    (2, 0): (1, 1),
    (0, 2): (-1, 1),
}


def vector_target(
    a: int,
    b: int,
    family: Sequence[sp.MatrixBase],
    target_sign: int = 1,
) -> sp.MatrixBase:
    if a == b:
        return sp.zeros(family[0].rows)
    sign, index = VECTOR_TABLE[(a, b)]
    return target_sign * sign * sp.I * family[index]


def clifford_residuals(
    family: Sequence[sp.MatrixBase], identity: sp.MatrixBase
) -> list[sp.MatrixBase]:
    return [
        family[i] * family[j]
        + family[j] * family[i]
        - (2 * identity if i == j else sp.zeros(identity.rows))
        for i in range(3)
        for j in range(3)
    ]


def cyclic_bivector_residuals(
    bivectors: Sequence[sp.MatrixBase], gammas: Sequence[sp.MatrixBase]
) -> list[sp.MatrixBase]:
    cyclic = ((1, 2), (2, 0), (0, 1))
    return [
        bivectors[a] + sp.I * sp.Rational(1, 2) * gammas[m] * gammas[n]
        for a, (m, n) in enumerate(cyclic)
    ]


def su2_residuals(generators: Sequence[sp.MatrixBase]) -> list[sp.MatrixBase]:
    return [
        commutator(generators[a], generators[b])
        - vector_target(a, b, generators)
        for a in range(3)
        for b in range(3)
    ]


def vector_residuals(
    generators: Sequence[sp.MatrixBase],
    family: Sequence[sp.MatrixBase],
    target_sign: int = 1,
) -> list[sp.MatrixBase]:
    return [
        commutator(generators[a], family[b])
        - vector_target(a, b, family, target_sign)
        for a in range(3)
        for b in range(3)
    ]


def casimir_residuals(
    generators: Sequence[sp.MatrixBase],
    family: Sequence[sp.MatrixBase],
    coefficient: sp.Expr,
) -> list[sp.MatrixBase]:
    result = []
    for member in family:
        double = sum(
            (
                commutator(generator, commutator(generator, member))
                for generator in generators
            ),
            sp.zeros(member.rows),
        )
        result.append(double - coefficient * member)
    return result


def gram_matrix(family: Sequence[sp.MatrixBase]) -> sp.MatrixBase:
    return sp.Matrix(
        3,
        3,
        lambda i, j: sp.trace(family[i].H * family[j]),
    )


def projector_residuals(
    plus: sp.MatrixBase, minus: sp.MatrixBase
) -> list[sp.MatrixBase]:
    return [
        plus * plus - plus,
        minus * minus - minus,
        plus * minus,
        plus + minus - I16,
        GAMMA5 * plus - plus,
        GAMMA5 * minus + minus,
    ]


def chirality_residuals() -> list[sp.MatrixBase]:
    return [
        GAMMA5 * GAMMA5 - I16,
        GAMMA5.H - GAMMA5,
        *(GAMMA5 * gamma + gamma * GAMMA5 for gamma in G_SPATIAL_16),
    ]


def projector_commutator_residuals() -> list[sp.MatrixBase]:
    return [
        *(commutator(generator, P_L) for generator in B_16),
        *(commutator(generator, P_R) for generator in B_16),
    ]


def chiral_orientation_residuals() -> list[sp.MatrixBase]:
    result = []
    for member in Y:
        result.extend(
            (
                P_R * member * P_L - member,
                P_L * member,
                member * P_R,
            )
        )
    return result


def numeric_max(residuals: Iterable[sp.MatrixBase]) -> float:
    values = (
        abs(complex(sp.N(entry, 16)))
        for residual in residuals
        for entry in residual
    )
    return max(values, default=0.0)


def main() -> int:
    print("=" * 78)
    print("FINITE-DIMENSIONAL CHIRAL VECTOR REPRESENTATION THEOREM")
    print("=" * 78)

    load_bearing: list[sp.MatrixBase] = []

    def run_exact(name: str, residuals: list[sp.MatrixBase], detail: str = "") -> None:
        load_bearing.extend(residuals)
        exact(name, residuals, detail)

    print("\nPart 1: exact Clifford and chirality packet")
    run_exact("C^8 spatial Clifford relations", clifford_residuals(G_SPATIAL_8, I8))
    run_exact(
        "C^16 spatial Clifford relations",
        clifford_residuals(G_SPATIAL_16, I16),
    )
    run_exact(
        "gamma_5 involution, Hermiticity, and spatial anticommutation",
        chirality_residuals(),
    )
    run_exact("oriented complementary chiral projectors", projector_residuals(P_L, P_R))

    print("\nPart 2: exact derived bivectors and vector laws")
    run_exact(
        "C^8 bivector double-sum equals cyclic formula",
        cyclic_bivector_residuals(B_8, G_SPATIAL_8),
    )
    run_exact(
        "C^16 bivector double-sum equals cyclic formula",
        cyclic_bivector_residuals(B_16, G_SPATIAL_16),
    )
    run_exact("C^8 bivectors obey su(2)", su2_residuals(B_8))
    run_exact("C^16 bivectors obey su(2)", su2_residuals(B_16))
    run_exact(
        "C^8 Gamma family obeys the vector commutator",
        vector_residuals(B_8, G_SPATIAL_8),
    )
    run_exact(
        "C^16 Gamma family obeys the vector commutator",
        vector_residuals(B_16, G_SPATIAL_16),
    )
    run_exact(
        "bivectors commute with both chiral projectors",
        projector_commutator_residuals(),
    )

    print("\nPart 3: exact chiral family, Casimir, and Gram identities")
    run_exact(
        "Y_i maps the P_L subspace to the P_R subspace",
        chiral_orientation_residuals(),
    )
    run_exact("Y_i obeys the vector commutator", vector_residuals(B_16, Y))
    run_exact(
        "C^8 Gamma family has adjoint Casimir 2",
        casimir_residuals(B_8, G_SPATIAL_8, sp.Integer(2)),
    )
    run_exact(
        "C^16 Gamma family has adjoint Casimir 2",
        casimir_residuals(B_16, G_SPATIAL_16, sp.Integer(2)),
    )
    run_exact(
        "Y_i has adjoint Casimir 2",
        casimir_residuals(B_16, Y, sp.Integer(2)),
    )
    gram_y = gram_matrix(Y)
    run_exact("Tr(Y_i^dag Y_j) = 8 delta_ij", [gram_y - 8 * sp.eye(3)])

    print("\nPart 4: universal symbolic rescaling identities")
    lam = sp.Symbol("lambda", complex=True)
    scaled_y = tuple(lam * member for member in Y)
    run_exact(
        "symbolic lambda Y_i obeys the vector commutator",
        vector_residuals(B_16, scaled_y),
        "polynomial identity in lambda",
    )
    run_exact(
        "symbolic lambda Y_i has adjoint Casimir 2",
        casimir_residuals(B_16, scaled_y, sp.Integer(2)),
        "polynomial identity in lambda",
    )
    run_exact(
        "Gram(lambda Y) = conjugate(lambda) lambda Gram(Y)",
        [gram_matrix(scaled_y) - sp.conjugate(lam) * lam * gram_y],
        "symbolic complex scalar",
    )

    print("\nPart 5: numerical support (non-load-bearing)")
    max_residual = numeric_max(load_bearing)
    report(
        "SUPPORT",
        "floating evaluation agrees with exact zero residuals",
        max_residual < 1.0e-12,
        f"max residual = {max_residual:.3e}",
    )
    scaled_two_gram = gram_matrix(tuple(2 * member for member in Y))
    scaled_two_error = numeric_max([scaled_two_gram - 32 * sp.eye(3)])
    report(
        "SUPPORT",
        "lambda=2 sample has Gram diagonal 32",
        scaled_two_error < 1.0e-12,
        f"max residual = {scaled_two_error:.3e}",
    )

    print("\nPart 6: hostile mutation rejection")
    reject_mutation("wrong bivector sign", su2_residuals(tuple(-generator for generator in B_8)))
    doubled_b = tuple(2 * generator for generator in B_8)
    reject_mutation(
        "wrong bivector normalization",
        [*su2_residuals(doubled_b), *vector_residuals(doubled_b, G_SPATIAL_8)],
    )
    reject_mutation("wrong vector sign", vector_residuals(B_16, Y, target_sign=-1))
    reject_mutation("wrong vector index", vector_residuals(B_16, (Y[1], Y[0], Y[2])))
    reject_mutation("reversed chiral projector orientation", projector_residuals(P_R, P_L))
    reject_mutation(
        "false adjoint Casimir coefficient 3",
        casimir_residuals(B_16, Y, sp.Integer(3)),
    )
    reject_mutation("false Gram normalization 16 delta_ij", [gram_y - 16 * sp.eye(3)])
    false_off_diagonal = 8 * sp.eye(3)
    false_off_diagonal[0, 1] = 1
    false_off_diagonal[1, 0] = 1
    reject_mutation("false nonzero off-diagonal Gram claim", [gram_y - false_off_diagonal])
    reject_mutation("false invariant Gram under lambda=2", [scaled_two_gram - gram_y])

    print("\n" + "=" * 78)
    total_pass = sum(COUNTS[lane]["pass"] for lane in LANES)
    total_fail = sum(COUNTS[lane]["fail"] for lane in LANES)
    for lane in LANES:
        print(f"{lane}: PASS={COUNTS[lane]['pass']} FAIL={COUNTS[lane]['fail']}")
    print(f"RESULT: PASS={total_pass} FAIL={total_fail}")
    print("=" * 78)
    return 0 if total_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
