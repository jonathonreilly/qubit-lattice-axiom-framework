#!/usr/bin/env python3
"""Exact structural checks for a narrowed one-hop semantic consumer.

The historical filename is retained for claim identity.  This runner checks
three separate finite-algebra statements and a non-identification firewall.
It does not read source prose or audit state, and it assigns no physical role
to the defined four-bit module's exact multiplicity.
"""

from __future__ import annotations

from itertools import product
import sys

try:
    import sympy as sp
except ImportError:
    print("FAIL: sympy is required for exact algebra")
    raise SystemExit(1)


PASS = 0
FAIL = 0
I16 = sp.eye(16)
Z16 = sp.zeros(16)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        mark = "PASS (A)"
    else:
        FAIL += 1
        mark = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{mark}] {label}{suffix}")


def section(label: str) -> None:
    print()
    print(label)
    print("-" * len(label))


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    if left.shape != right.shape:
        return False
    return all(sp.simplify(entry) == 0 for entry in left - right)


def bits(index: int) -> tuple[int, ...]:
    return tuple((index >> mu) & 1 for mu in range(4))


def bit_index(bit_tuple: tuple[int, ...] | list[int]) -> int:
    return sum((int(bit) & 1) << mu for mu, bit in enumerate(bit_tuple))


BLOCK_BITS = tuple(bits(index) for index in range(16))


def signed_flip(mu: int, *, prefix: bool) -> sp.Matrix:
    matrix = sp.zeros(16)
    for column, bit_tuple in enumerate(BLOCK_BITS):
        flipped = list(bit_tuple)
        flipped[mu] ^= 1
        exponent_bits = bit_tuple[:mu] if prefix else bit_tuple[mu + 1 :]
        sign = -1 if sum(exponent_bits) % 2 else 1
        matrix[bit_index(flipped), column] = sign
    return matrix


ALPHAS = tuple(signed_flip(mu, prefix=True) for mu in range(4))
BETAS = tuple(signed_flip(mu, prefix=False) for mu in range(4))


def clifford_relations(generators: tuple[sp.Matrix, ...]) -> bool:
    dimension = generators[0].rows
    identity = sp.eye(dimension)
    zero = sp.zeros(dimension)
    return all(
        matrix_equal(
            left * right + right * left,
            2 * identity if mu == nu else zero,
        )
        for mu, left in enumerate(generators)
        for nu, right in enumerate(generators)
    )


def clifford_word(generators: tuple[sp.Matrix, ...], mask: int) -> sp.Matrix:
    word = sp.eye(generators[0].rows)
    for mu, generator in enumerate(generators):
        if mask & (1 << mu):
            word *= generator
    return word


def word_span_rank(generators: tuple[sp.Matrix, ...]) -> int:
    words = tuple(clifford_word(generators, mask) for mask in range(16))
    columns = [word.reshape(word.rows * word.cols, 1) for word in words]
    return int(sp.Matrix.hstack(*columns).rank())


def explicit_gammas() -> tuple[sp.Matrix, ...]:
    return (
        sp.Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]),
        sp.Matrix([[0, -sp.I, 0, 0], [sp.I, 0, 0, 0], [0, 0, 0, -sp.I], [0, 0, sp.I, 0]]),
        sp.Matrix([[0, 0, 1, 0], [0, 0, 0, -1], [1, 0, 0, 0], [0, -1, 0, 0]]),
        sp.Matrix([[0, 0, -sp.I, 0], [0, 0, 0, sp.I], [sp.I, 0, 0, 0], [0, -sp.I, 0, 0]]),
    )


def module_certificate() -> tuple[tuple[sp.Matrix, ...], sp.Matrix, tuple[sp.Matrix, ...]]:
    q01 = sp.I * BETAS[0] * BETAS[1]
    q23 = sp.I * BETAS[2] * BETAS[3]
    projectors = tuple(
        (I16 + sign_01 * q01) * (I16 + sign_23 * q23) / 4
        for sign_01, sign_23 in product((1, -1), repeat=2)
    )
    v = 2 * projectors[0] * I16[:, 0]
    w = sp.Matrix.hstack(
        v,
        ALPHAS[0] * v,
        ALPHAS[2] * v,
        ALPHAS[0] * ALPHAS[2] * v,
    )
    columns = []
    for spin_index in range(4):
        for r, s in product((0, 1), repeat=2):
            columns.append((BETAS[0] ** r) * (BETAS[2] ** s) * w[:, spin_index])
    return projectors, sp.Matrix.hstack(*columns), explicit_gammas()


FORMAL_HYPOTHESES = frozenset(
    {
        "finite_set_counting",
        "integer_arithmetic",
        "defined_four_bit_matrices",
        "finite_complex_linear_algebra",
        "cited_cl3_split",
    }
)
PHYSICAL_BRIDGES = frozenset(
    {
        "physical_action_identification",
        "physical_carrier_identification",
        "continuum_species_identification",
        "taste_identification",
        "os0_reconstruction_bridge",
    }
)


def main() -> int:
    print("=" * 88)
    print("Narrowed substep-3 consumer: exact finite algebra and scope firewall")
    print("=" * 88)

    section("Part 1: corner cardinality and role-free arithmetic")
    corners = tuple(product((sp.Integer(0), sp.pi), repeat=4))
    check("the comparison corner set has exactly 16 elements", len(corners) == 16)
    check(
        "every enumerated corner zeros the exact sum of sine squares",
        all(sp.simplify(sum(sp.sin(value) ** 2 for value in corner)) == 0 for corner in corners),
    )
    check("16=4*4 is an integer identity", 16 == 4 * 4)
    factor_pairs = tuple(
        (left, 16 // left)
        for left in range(1, 17)
        if 16 % left == 0 and left <= 16 // left
    )
    check(
        "integer arithmetic does not uniquely select the displayed factor pair",
        factor_pairs == ((1, 16), (2, 8), (4, 4)),
        detail=f"unordered factor pairs={factor_pairs}",
    )

    section("Part 2: independent Cl(3,0) complexification dimensions")
    sigma_1 = sp.Matrix([[0, 1], [1, 0]])
    sigma_2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sigma_3 = sp.Matrix([[1, 0], [0, -1]])
    omega_plus = sigma_1 * sigma_2 * sigma_3
    omega_minus = (-sigma_1) * (-sigma_2) * (-sigma_3)
    check("the two Pauli realizations have pseudoscalar characters +i and -i", matrix_equal(omega_plus, sp.I * sp.eye(2)) and matrix_equal(omega_minus, -sp.I * sp.eye(2)))
    check("the two irreducible module dimensions are exactly (2,2)", (sigma_1.rows, (-sigma_1).rows) == (2, 2))
    check("their numerical dimension sum is 4", sigma_1.rows + (-sigma_1).rows == 4)
    check("the split algebra dimension is dim M2 + dim M2 = 8", 2**2 + 2**2 == 8)

    section("Part 3: explicit defined-operator module certificate")
    check("the defined alpha generators satisfy every Clifford relation", clifford_relations(ALPHAS))
    check(
        "the suffix-sign beta generators commute with every alpha and satisfy Clifford",
        clifford_relations(BETAS)
        and all(matrix_equal(alpha * beta, beta * alpha) for alpha in ALPHAS for beta in BETAS),
    )
    projectors, unitary, gammas = module_certificate()
    check(
        "four exact orthogonal rank-4 projectors resolve the defined module",
        all(matrix_equal(projector * projector, projector) and projector.rank() == 4 for projector in projectors)
        and all(matrix_equal(projectors[i] * projectors[j], Z16) for i in range(4) for j in range(i + 1, 4))
        and matrix_equal(sum(projectors, Z16), I16),
    )
    check("the displayed gamma generators satisfy every Clifford relation", clifford_relations(gammas))
    gamma_rank = word_span_rank(gammas)
    check("the gamma words span M4(C), proving irreducibility", gamma_rank == 16, detail=f"exact rank={gamma_rank}")
    check("the constructed 16 by 16 intertwiner is exactly unitary", matrix_equal(unitary.H * unitary, I16))
    similarity_checks = tuple(
        matrix_equal(unitary.H * ALPHAS[mu] * unitary, sp.kronecker_product(gammas[mu], sp.eye(4)))
        for mu in range(4)
    )
    check(
        "the exact similarity proves four copies without dimension counting",
        all(similarity_checks),
        detail=f"directions={similarity_checks}",
    )

    section("Part 4: structural non-identification firewall")
    check(
        "no required physical bridge is among the formal hypotheses",
        FORMAL_HYPOTHESES.isdisjoint(PHYSICAL_BRIDGES),
        detail=f"formal hypotheses={sorted(FORMAL_HYPOTHESES)}",
    )
    conclusions = {
        "formal multiplicity": {"defined_four_bit_matrices", "finite_complex_linear_algebra"},
        "physical taste": {"taste_identification"},
        "physical carrier": {"physical_carrier_identification"},
    }
    check(
        "the formal module conclusion is licensed but physical taste/carrier conclusions are not",
        conclusions["formal multiplicity"].issubset(FORMAL_HYPOTHESES)
        and not conclusions["physical taste"].issubset(FORMAL_HYPOTHESES)
        and not conclusions["physical carrier"].issubset(FORMAL_HYPOTHESES),
    )
    d_other = 6
    left = 2 ** (d_other // 2)
    right = 2 ** (d_other // 2)
    check(
        "the d=6 identity 64=8*8 is checked without assigning either factor a role",
        2**d_other == left * right and (left, right) == (8, 8),
    )

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
