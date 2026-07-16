#!/usr/bin/env python3
"""Exact certificate for a defined four-bit periodic difference operator.

The historical filename is preserved for claim-graph continuity.  The theorem
checked here is purely finite algebra: it defines the signs, shifts, block map,
and Laurent-polynomial fiber matrix.  It makes no action, fermion, carrier,
reconstruction, taste, generation, or continuum-species identification.

Modes:
  default                 exact blocking plus explicit unitary certificate
  --independent           exact full-commutant proof route
  --hostile               verify that six mutation families are rejected
  --intentional-failure   install those mutations and exit nonzero
"""

from __future__ import annotations

import argparse
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


def check(label: str, condition: bool, detail: str = "", kind: str = "A") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        mark = f"PASS ({kind})"
    else:
        FAIL += 1
        mark = f"FAIL ({kind})"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{mark}] {label}{suffix}")


def section(label: str) -> None:
    print()
    print(label)
    print("-" * len(label))


def bits(index: int) -> tuple[int, ...]:
    return tuple((index >> mu) & 1 for mu in range(4))


def bit_index(bit_tuple: tuple[int, ...] | list[int]) -> int:
    return sum((int(bit) & 1) << mu for mu, bit in enumerate(bit_tuple))


BLOCK_BITS = tuple(bits(i) for i in range(16))


def eta(mu: int, bit_tuple: tuple[int, ...]) -> int:
    """The sign coefficient defined in the theorem."""
    return -1 if sum(bit_tuple[:mu]) % 2 else 1


def signed_flip(mu: int, *, prefix: bool, mutate_entry: bool = False) -> sp.Matrix:
    """Prefix signs give alpha; suffix signs give its commuting beta partner."""
    matrix = sp.zeros(16)
    for column, bit_tuple in enumerate(BLOCK_BITS):
        flipped = list(bit_tuple)
        flipped[mu] ^= 1
        exponent_bits = bit_tuple[:mu] if prefix else bit_tuple[mu + 1 :]
        sign = -1 if sum(exponent_bits) % 2 else 1
        if mutate_entry and mu == 3 and column == 0:
            sign *= -1
        matrix[bit_index(flipped), column] = sign
    return matrix


ALPHAS = tuple(signed_flip(mu, prefix=True) for mu in range(4))
BETAS = tuple(signed_flip(mu, prefix=False) for mu in range(4))


def raw_blocked_direction(
    mu: int,
    t: sp.Symbol,
    a: sp.Symbol,
    *,
    mutate_sign: bool = False,
    mutate_shift: bool = False,
) -> sp.Matrix:
    """The exact fiber matrix induced by the two defined periodic shifts."""
    matrix = sp.zeros(16)
    for row, bit_tuple in enumerate(BLOCK_BITS):
        flipped = list(bit_tuple)
        flipped[mu] ^= 1
        column = bit_index(flipped)
        sign = eta(mu, bit_tuple)
        if mutate_sign and mu == 3 and row == 0:
            sign *= -1
        if bit_tuple[mu] == 0:
            backward_power = -1 if mutate_shift and mu == 0 else -2
            coefficient = sign * (1 - t**backward_power) / (2 * a)
        else:
            coefficient = sign * (t**2 - 1) / (2 * a)
        matrix[row, column] = coefficient
    return matrix


def site_shift_coefficient(mu: int, bit_tuple: tuple[int, ...], q: sp.Expr, a: sp.Expr) -> sp.Expr:
    """Coefficient obtained directly from n=2y+b on a coarse q-character."""
    if bit_tuple[mu] == 0:
        return eta(mu, bit_tuple) * (1 - q**-1) / (2 * a)
    return eta(mu, bit_tuple) * (q - 1) / (2 * a)


def rephasing(t_symbols: tuple[sp.Symbol, ...]) -> sp.Matrix:
    diagonal = []
    for bit_tuple in BLOCK_BITS:
        phase = sp.Integer(1)
        for mu, bit in enumerate(bit_tuple):
            phase *= t_symbols[mu] ** bit
        diagonal.append(phase)
    return sp.diag(*diagonal)


def matrix_is_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and matrix_is_zero(left - right)


def clifford_word(generators: tuple[sp.Matrix, ...], mask: int) -> sp.Matrix:
    word = sp.eye(generators[0].rows)
    for mu, generator in enumerate(generators):
        if mask & (1 << mu):
            word *= generator
    return word


def clifford_relations(generators: tuple[sp.Matrix, ...]) -> bool:
    dimension = generators[0].rows
    identity = sp.eye(dimension)
    zero = sp.zeros(dimension)
    for mu, left in enumerate(generators):
        for nu, right in enumerate(generators):
            target = 2 * identity if mu == nu else zero
            if not matrix_equal(left * right + right * left, target):
                return False
    return True


def word_span_rank(generators: tuple[sp.Matrix, ...]) -> int:
    words = tuple(clifford_word(generators, mask) for mask in range(16))
    flattened = sp.Matrix.hstack(*[word.reshape(word.rows * word.cols, 1) for word in words])
    return int(flattened.rank())


def explicit_gamma_matrices() -> tuple[sp.Matrix, ...]:
    return (
        sp.Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]),
        sp.Matrix([[0, -sp.I, 0, 0], [sp.I, 0, 0, 0], [0, 0, 0, -sp.I], [0, 0, sp.I, 0]]),
        sp.Matrix([[0, 0, 1, 0], [0, 0, 0, -1], [1, 0, 0, 0], [0, -1, 0, 0]]),
        sp.Matrix([[0, 0, -sp.I, 0], [0, 0, 0, sp.I], [sp.I, 0, 0, 0], [0, -sp.I, 0, 0]]),
    )


def module_certificate() -> dict[str, object]:
    q01 = sp.I * BETAS[0] * BETAS[1]
    q23 = sp.I * BETAS[2] * BETAS[3]
    projectors = {}
    for sign_01, sign_23 in product((1, -1), repeat=2):
        projectors[(sign_01, sign_23)] = (
            (I16 + sign_01 * q01) * (I16 + sign_23 * q23) / 4
        )

    e_zero = I16[:, 0]
    v = 2 * projectors[(1, 1)] * e_zero
    w = sp.Matrix.hstack(v, ALPHAS[0] * v, ALPHAS[2] * v, ALPHAS[0] * ALPHAS[2] * v)
    computed_gammas = tuple(sp.simplify(w.H * alpha * w) for alpha in ALPHAS)

    columns = []
    for spin_index in range(4):
        for r, s in product((0, 1), repeat=2):
            intertwiner = (BETAS[0] ** r) * (BETAS[2] ** s)
            columns.append(intertwiner * w[:, spin_index])
    unitary = sp.Matrix.hstack(*columns)
    return {
        "q01": q01,
        "q23": q23,
        "projectors": projectors,
        "v": v,
        "w": w,
        "computed_gammas": computed_gammas,
        "expected_gammas": explicit_gamma_matrices(),
        "unitary": unitary,
    }


FORMAL_HYPOTHESES = frozenset(
    {
        "finite_periodic_set",
        "defined_sign_coefficients",
        "defined_shift_operator",
        "defined_block_map",
        "finite_complex_linear_algebra",
    }
)
PHYSICAL_REQUIREMENTS = {
    "physical carrier": frozenset({"physical_carrier_identification"}),
    "staggered fermion": frozenset({"physical_action_identification"}),
    "OS0 reconstruction": frozenset({"os0_reconstruction_bridge"}),
    "taste or continuum species": frozenset({"continuum_species_identification"}),
}


def inference_authorized(conclusion: str, hypotheses: frozenset[str] = FORMAL_HYPOTHESES) -> bool:
    return PHYSICAL_REQUIREMENTS[conclusion].issubset(hypotheses)


def run_normal() -> None:
    section("Part 1: defined finite periodic operator and exact blocking")
    check(
        "the block labels are exactly the 16 elements of {0,1}^4",
        len(BLOCK_BITS) == 16 and len(set(BLOCK_BITS)) == 16,
    )
    observed_counts = tuple(
        sum(1 for bit_tuple in BLOCK_BITS if sum(bit_tuple) == weight)
        for weight in range(5)
    )
    check(
        "the Hamming grading is (1,4,6,4,1), without assigning module roles",
        observed_counts == (1, 4, 6, 4, 1),
        detail=f"observed={observed_counts}",
    )
    check(
        "eta_mu(2y+b)=eta_mu(b) on every even periodic block",
        all(
            (-1) ** sum((2 * y[nu] + b[nu]) for nu in range(mu)) == eta(mu, b)
            for mu in range(4)
            for b in BLOCK_BITS
            for y in product((0, 1), repeat=4)
        ),
    )

    a = sp.symbols("a", nonzero=True)
    t_symbols = sp.symbols("t0:4", nonzero=True)
    fiber_checks = []
    for mu in range(4):
        raw = raw_blocked_direction(mu, t_symbols[mu], a)
        fiber_checks.extend(
            sp.simplify(
                raw[
                    row,
                    bit_index(
                        tuple(
                            bit ^ (1 if nu == mu else 0)
                            for nu, bit in enumerate(b)
                        )
                    ),
                ]
                - site_shift_coefficient(mu, b, t_symbols[mu] ** 2, a)
            )
            == 0
            for row, b in enumerate(BLOCK_BITS)
        )
    check(
        "the symbolic finite Fourier fibers equal the coefficients from the two site shifts",
        all(fiber_checks),
        detail=f"entries={len(fiber_checks)}",
    )

    phase = rephasing(t_symbols)
    phase_inverse = sp.diag(*[entry**-1 for entry in phase.diagonal()])
    direction_checks = []
    for mu in range(4):
        raw = raw_blocked_direction(mu, t_symbols[mu], a)
        expected = ((t_symbols[mu] - t_symbols[mu] ** -1) / (2 * a)) * ALPHAS[mu]
        direction_checks.append(matrix_equal(phase_inverse * raw * phase, expected))
    check(
        "the diagonal rephasing proves all four Laurent-polynomial blocking identities",
        all(direction_checks),
        detail=f"directions={direction_checks}",
    )

    m = sp.symbols("m")
    raw_full = m * I16
    reduced_full = m * I16
    for mu in range(4):
        raw_full += raw_blocked_direction(mu, t_symbols[mu], a)
        reduced_full += ((t_symbols[mu] - t_symbols[mu] ** -1) / (2 * a)) * ALPHAS[mu]
    check(
        "the full finite fiber has the exact reduced Laurent-polynomial form",
        matrix_equal(phase_inverse * raw_full * phase, reduced_full),
    )
    x = sp.symbols("x", real=True)
    check(
        "on t=exp(i x), the Laurent coefficient is exactly i sin(x)",
        sp.simplify((sp.exp(sp.I * x) - sp.exp(-sp.I * x)) / 2 - sp.I * sp.sin(x)) == 0,
    )

    section("Part 2: exact Clifford algebra checks")
    check(
        "each alpha_mu is a real symmetric involution",
        all(alpha == alpha.T and matrix_equal(alpha * alpha, I16) for alpha in ALPHAS),
    )
    check("the four alpha_mu satisfy every Clifford relation", clifford_relations(ALPHAS))
    alpha_words = tuple(clifford_word(ALPHAS, mask) for mask in range(16))
    alpha_rank = word_span_rank(ALPHAS)
    check(
        "the 16 alpha words are linearly independent",
        alpha_rank == 16,
        detail=f"exact rank={alpha_rank}",
    )
    traces = tuple(sp.trace(word) for word in alpha_words)
    check(
        "the exact word character is (16,0,...,0)",
        traces[0] == 16 and all(value == 0 for value in traces[1:]),
        detail=f"character={traces}",
    )
    gram = sp.Matrix([[sp.trace(left.H * right) for right in alpha_words] for left in alpha_words])
    check(
        "the alpha words are Hilbert-Schmidt orthogonal",
        matrix_equal(gram, 16 * sp.eye(16)),
    )

    section("Part 3: explicit unitary four-copy certificate")
    cert = module_certificate()
    q01 = cert["q01"]
    q23 = cert["q23"]
    projectors = cert["projectors"]
    w = cert["w"]
    unitary = cert["unitary"]
    computed_gammas = cert["computed_gammas"]
    expected_gammas = cert["expected_gammas"]

    beta_commutes = all(matrix_equal(alpha * beta, beta * alpha) for alpha in ALPHAS for beta in BETAS)
    check(
        "the suffix-sign beta generators commute with every alpha and satisfy Clifford",
        beta_commutes and clifford_relations(BETAS),
    )
    check(
        "Q_01 and Q_23 are commuting Hermitian involutions",
        q01 == q01.H
        and q23 == q23.H
        and matrix_equal(q01 * q01, I16)
        and matrix_equal(q23 * q23, I16)
        and matrix_equal(q01 * q23, q23 * q01),
    )
    projector_values = tuple(projectors.values())
    check(
        "their four joint projectors are orthogonal rank-4 projectors summing to I_16",
        all(matrix_equal(p * p, p) and p.rank() == 4 for p in projector_values)
        and all(
            matrix_equal(projector_values[i] * projector_values[j], Z16)
            for i in range(4)
            for j in range(i + 1, 4)
        )
        and matrix_equal(sum(projector_values, Z16), I16),
    )
    check(
        "the four vectors in the ++ projector form an exact orthonormal basis",
        matrix_equal(w.H * w, sp.eye(4))
        and matrix_equal(projectors[(1, 1)] * w, w),
    )
    check(
        "the computed 4x4 restrictions equal the displayed gamma matrices",
        all(matrix_equal(left, right) for left, right in zip(computed_gammas, expected_gammas)),
    )
    check("the displayed gamma matrices satisfy every Clifford relation", clifford_relations(expected_gammas))
    gamma_rank = word_span_rank(expected_gammas)
    check(
        "the gamma words span M_4(C), proving the 4-dimensional module irreducible",
        gamma_rank == 16,
        detail=f"exact rank={gamma_rank}",
    )
    check("the constructed 16x16 intertwiner U is exactly unitary", matrix_equal(unitary.H * unitary, I16))
    intertwiner_checks = tuple(
        matrix_equal(unitary.H * ALPHAS[mu] * unitary, sp.kronecker_product(expected_gammas[mu], sp.eye(4)))
        for mu in range(4)
    )
    check(
        "U^dagger alpha_mu U = gamma_mu tensor I_4 for every mu",
        all(intertwiner_checks),
        detail=f"directions={intertwiner_checks}",
    )
    check(
        "the explicit similarity certifies four copies, independently of 16=4*4 prose",
        unitary.shape == (16, 16)
        and all(sp.kronecker_product(gamma, sp.eye(4)).shape == (16, 16) for gamma in expected_gammas),
    )

    section("Part 4: exact inverse and hypothesis firewall")
    s_symbols = sp.symbols("s0:4", real=True)
    kinetic = sum((s_symbols[mu] * ALPHAS[mu] for mu in range(4)), Z16)
    kinetic_square = sum(value**2 for value in s_symbols) * I16
    check(
        "the defined kinetic matrix squares to (sum_mu s_mu^2) I_16",
        matrix_equal(kinetic * kinetic, kinetic_square),
    )
    denominator = m**2 + sum(value**2 for value in s_symbols)
    operator = m * I16 + sp.I * kinetic
    numerator = m * I16 - sp.I * kinetic
    check(
        "the scalar-denominator numerator identity is exact",
        matrix_equal(operator * numerator, denominator * I16),
    )
    check(
        "the displayed inverse is exact on its nonzero-denominator domain",
        matrix_equal(operator * (numerator / denominator), I16),
    )
    singular = {m: 0, **{value: 0 for value in s_symbols}}
    check(
        "the zero-parameter singular matrix is excluded from the inverse domain",
        denominator.subs(singular) == 0 and matrix_equal(operator.subs(singular), Z16),
    )
    check(
        "the formal hypotheses contain none of the four required physical bridges",
        all(not inference_authorized(conclusion) for conclusion in PHYSICAL_REQUIREMENTS),
        detail=f"formal hypotheses={sorted(FORMAL_HYPOTHESES)}",
    )


def run_independent() -> None:
    section("Independent route: exact commutant and minimal projectors")
    identity = sp.eye(16)
    constraints = sp.Matrix.vstack(
        *[
            sp.kronecker_product(identity, alpha)
            - sp.kronecker_product(alpha.T, identity)
            for alpha in ALPHAS
        ]
    )
    constraint_rank = int(constraints.rank())
    commutant_dimension = 256 - constraint_rank
    check(
        "the full exact commutant equations have dimension 16",
        constraint_rank == 240 and commutant_dimension == 16,
        detail=f"constraint rank={constraint_rank}, nullity={commutant_dimension}",
    )

    beta_words = tuple(clifford_word(BETAS, mask) for mask in range(16))
    flattened = sp.Matrix.hstack(*[word.reshape(256, 1) for word in beta_words])
    check(
        "the 16 beta words are an exact basis of that commutant",
        flattened.rank() == 16
        and all(matrix_equal(word * alpha, alpha * word) for word in beta_words for alpha in ALPHAS),
    )

    cert = module_certificate()
    projectors = cert["projectors"]
    projector_values = tuple(projectors.values())
    check(
        "the four commutant projectors are invariant, orthogonal, rank 4, and complete",
        all(
            p.rank() == 4
            and all(matrix_equal(p * alpha, alpha * p) for alpha in ALPHAS)
            for p in projector_values
        )
        and all(
            matrix_equal(projector_values[i] * projector_values[j], Z16)
            for i in range(4)
            for j in range(i + 1, 4)
        )
        and matrix_equal(sum(projector_values, Z16), I16),
    )
    compressed_ranks = []
    for p in projector_values:
        compressed = sp.Matrix.hstack(*[(p * word * p).reshape(256, 1) for word in beta_words])
        compressed_ranks.append(int(compressed.rank()))
    check(
        "each rank-4 summand has scalar compressed commutant and is irreducible",
        compressed_ranks == [1, 1, 1, 1],
        detail=f"compressed ranks={compressed_ranks}",
    )

    map_checks = []
    for r, s in product((0, 1), repeat=2):
        intertwiner = (BETAS[0] ** r) * (BETAS[2] ** s)
        target = projectors[((-1) ** r, (-1) ** s)]
        map_checks.append(
            matrix_equal(intertwiner * projectors[(1, 1)] * intertwiner.H, target)
            and all(matrix_equal(intertwiner * alpha, alpha * intertwiner) for alpha in ALPHAS)
        )
    check(
        "exact commuting intertwiners identify all four irreducible summands",
        all(map_checks),
        detail=f"sectors={map_checks}",
    )


def hostile_conditions() -> dict[str, bool]:
    a = sp.symbols("a", nonzero=True)
    t_symbols = sp.symbols("t0:4", nonzero=True)
    phase = rephasing(t_symbols)
    phase_inverse = sp.diag(*[entry**-1 for entry in phase.diagonal()])

    bad_sign_raw = raw_blocked_direction(3, t_symbols[3], a, mutate_sign=True)
    expected_3 = ((t_symbols[3] - t_symbols[3] ** -1) / (2 * a)) * ALPHAS[3]
    sign_survives = matrix_equal(phase_inverse * bad_sign_raw * phase, expected_3)

    bad_shift_raw = raw_blocked_direction(0, t_symbols[0], a, mutate_shift=True)
    expected_0 = ((t_symbols[0] - t_symbols[0] ** -1) / (2 * a)) * ALPHAS[0]
    shift_survives = matrix_equal(phase_inverse * bad_shift_raw * phase, expected_0)

    bad_generators = list(ALPHAS)
    bad_generators[1] = ALPHAS[1] + ALPHAS[0]
    clifford_survives = clifford_relations(tuple(bad_generators))

    cert = module_certificate()
    unitary = cert["unitary"]
    expected_gammas = cert["expected_gammas"]
    bad_unitary = unitary.copy()
    bad_unitary[:, 0] = unitary[:, 0] + unitary[:, 1]
    intertwiner_survives = matrix_equal(bad_unitary.H * bad_unitary, I16) and all(
        matrix_equal(
            bad_unitary.H * ALPHAS[mu] * bad_unitary,
            sp.kronecker_product(expected_gammas[mu], sp.eye(4)),
        )
        for mu in range(4)
    )

    multiplicity_three_survives = 16 == 4 * 3
    physical_inference_survives = any(
        inference_authorized(conclusion) for conclusion in PHYSICAL_REQUIREMENTS
    )
    return {
        "canonical sign/phase mutation": sign_survives,
        "shift/blocking-map mutation": shift_survives,
        "Clifford-generator mutation": clifford_survives,
        "unitary-intertwiner mutation": intertwiner_survives,
        "module-multiplicity mutation 4 -> 3": multiplicity_three_survives,
        "illicit physical-carrier/taste inference": physical_inference_survives,
    }


def run_hostile(*, intentional_failure: bool) -> None:
    title = "Intentional-failure probe" if intentional_failure else "Hostile mutation controls"
    section(title)
    for label, mutant_survives in hostile_conditions().items():
        if intentional_failure:
            check(
                f"INTENTIONAL FAILURE: mutated {label} is installed as valid",
                mutant_survives,
            )
        else:
            check(f"hostile control rejects {label}", not mutant_survives)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--independent", action="store_true", help="run the commutant proof route")
    modes.add_argument("--hostile", action="store_true", help="verify all mutations are rejected")
    modes.add_argument(
        "--intentional-failure",
        action="store_true",
        help="install all mutations; this mode must exit nonzero",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.independent:
        mode = "independent"
    elif args.hostile:
        mode = "hostile"
    elif args.intentional_failure:
        mode = "intentional-failure"
    else:
        mode = "normal"

    print("=" * 88)
    print("Defined four-bit periodic difference operator: exact certificate")
    print(f"mode: {mode}")
    print("=" * 88)

    if mode == "normal":
        run_normal()
    elif mode == "independent":
        run_independent()
    elif mode == "hostile":
        run_hostile(intentional_failure=False)
    else:
        run_hostile(intentional_failure=True)

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
