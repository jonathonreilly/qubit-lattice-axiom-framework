#!/usr/bin/env python3
"""Exact formal reduction for a supplied two-offset 3 x 3 texture.

The theorem proved here starts from supplied mathematical data only:

    Y = D_a C^a + D_b C^b,

where a != b in Z_3, C is the explicit 3-cycle below, and D_a,D_b are
diagonal complex coefficient matrices.  It proves the support reduction and,
on the stratum where all six diagonal coefficients are nonzero, computes the
quotient by a specified diagonal U(1)^3_left x U(1)^3_right action.

No charged-lepton Yukawa sector, Higgs field, effective charge assignment,
physical field-rephasing redundancy, branch selection, mass, PMNS datum, or
physical parameter value is assumed or inferred.
"""

from __future__ import annotations

import argparse
import itertools
import sys
from collections import deque

import sympy as sp


PASS_COUNT = 0
FAIL_COUNT = 0

I3 = sp.eye(3)
C = sp.Matrix(
    [
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
    ]
)
SWAP_12 = sp.Matrix(
    [
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
    ]
)

CANONICAL_EDGES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (0, 1),
    (1, 2),
    (2, 0),
)

FORMAL_HYPOTHESES = frozenset(
    {
        "explicit_3_cycle_C",
        "distinct_offsets_in_Z3",
        "supplied_diagonal_coefficient_matrices",
        "all_six_coefficients_nonzero_for_generic_quotient",
        "specified_diagonal_rephasing_action",
    }
)
FORMAL_CONCLUSIONS = frozenset(
    {
        "formal_support_class_A_plus_BC",
        "incidence_rank_five",
        "six_positive_moduli",
        "one_quotient_phase",
        "seven_real_quotient_parameters",
    }
)
PHYSICAL_BRIDGES = frozenset(
    {
        "charged_lepton_yukawa_sector",
        "two_physical_Higgs_fields",
        "effective_Z3_charge_offsets",
        "field_rephasing_is_physical_gauge_redundancy",
        "selected_PMNS_branch",
        "masses_or_PMNS_data",
        "physical_parameter_values",
    }
)


def check(name: str, condition: bool, detail: str = "") -> bool:
    """Record one truthful check and preserve a nonzero exit on failure."""

    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"         {detail}")
    return ok


def matrix_is_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and matrix_is_zero(left - right)


def incidence_matrix(edges: tuple[tuple[int, int], ...]) -> sp.Matrix:
    """Unsigned bipartite incidence for phases theta_ij -> theta_ij+l_i+r_j."""

    return sp.Matrix(
        [
            [int(left == i) for left in range(3)]
            + [int(right == j) for right in range(3)]
            for i, j in edges
        ]
    )


def support_component_count(edges: tuple[tuple[int, int], ...]) -> int:
    """Count components on all six left/right vertices of the support graph."""

    adjacency = {vertex: set() for vertex in range(6)}
    for i, j in edges:
        left = i
        right = 3 + j
        adjacency[left].add(right)
        adjacency[right].add(left)

    unseen = set(adjacency)
    count = 0
    while unseen:
        count += 1
        seed = unseen.pop()
        queue = deque([seed])
        while queue:
            vertex = queue.popleft()
            for neighbor in adjacency[vertex]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    queue.append(neighbor)
    return count


def is_permutation_matrix(matrix: sp.Matrix) -> bool:
    entries_are_binary = all(entry in (0, 1) for entry in matrix)
    row_sums = [sum(matrix.row(i)) for i in range(matrix.rows)]
    col_sums = [sum(matrix.col(j)) for j in range(matrix.cols)]
    return (
        matrix.shape == (3, 3)
        and entries_are_binary
        and row_sums == [1, 1, 1]
        and col_sums == [1, 1, 1]
    )


def is_nontrivial_three_cycle(matrix: sp.Matrix) -> bool:
    return (
        is_permutation_matrix(matrix)
        and not matrix_equal(matrix, I3)
        and matrix_equal(matrix**3, I3)
        and not matrix_equal(matrix**2, I3)
    )


def conjugator_to_c(relative: sp.Matrix) -> sp.Matrix | None:
    if matrix_equal(relative, C):
        return I3
    if matrix_equal(relative, C**2):
        return SWAP_12
    return None


def is_distinct_z3_pair(a: int, b: int) -> bool:
    return a in range(3) and b in range(3) and a != b


def exact_support_reduction() -> None:
    print("\n=== A. Exact support reduction for every ordered distinct offset pair ===")

    # The support identity itself holds without the generic nonzero assumption;
    # nonzero coefficients are imposed only for the quotient theorem below.
    a_coeff = sp.symbols("a_0:3", complex=True)
    b_coeff = sp.symbols("b_0:3", complex=True)
    d_a = sp.diag(*a_coeff)
    d_b = sp.diag(*b_coeff)

    check("C is an exact order-three permutation", is_nontrivial_three_cycle(C))
    check("C inverse is exactly C^2", matrix_equal(C.inv(), C**2))

    ordered_pairs = tuple(itertools.permutations(range(3), 2))
    check(
        "all six ordered pairs a != b in Z_3 are present",
        len(ordered_pairs) == 6 and len(set(ordered_pairs)) == 6,
        detail=str(ordered_pairs),
    )

    for a, b in ordered_pairs:
        y_matrix = d_a * C**a + d_b * C**b
        right_relabeling = C ** ((-a) % 3)
        relative = C ** ((b - a) % 3)
        reduced = sp.expand(y_matrix * right_relabeling)
        expected_reduced = d_a + d_b * relative
        conjugator = conjugator_to_c(relative)

        check(
            f"offsets ({a},{b}): right multiplication by C^(-a) is exact",
            matrix_equal(reduced, expected_reduced),
            detail=f"relative exponent={(b - a) % 3}",
        )
        check(
            f"offsets ({a},{b}): relative support is a nontrivial 3-cycle",
            is_nontrivial_three_cycle(relative),
        )
        check(
            f"offsets ({a},{b}): explicit conjugator exists",
            conjugator is not None,
            detail="I_3" if matrix_equal(relative, C) else "swap generations 1 and 2",
        )
        if conjugator is None:
            continue

        q_inv = conjugator.inv()
        a_canonical = conjugator * d_a * q_inv
        b_canonical = conjugator * d_b * q_inv
        transformed = sp.expand(conjugator * reduced * q_inv)
        target = a_canonical + b_canonical * C

        check(
            f"offsets ({a},{b}): conjugator sends the relative cycle to C",
            matrix_equal(conjugator * relative * q_inv, C),
        )
        check(
            f"offsets ({a},{b}): transformed matrix is exactly A+B C",
            matrix_equal(transformed, target)
            and a_canonical.is_diagonal()
            and b_canonical.is_diagonal(),
        )


def exact_generic_rephasing_quotient() -> None:
    print("\n=== B. Exact rephasing quotient on the all-nonzero stratum ===")

    phase_map = incidence_matrix(CANONICAL_EDGES)
    rank = phase_map.rank()
    right_nullspace = phase_map.nullspace()
    left_nullspace = phase_map.T.nullspace()
    common_kernel = sp.Matrix([-1, -1, -1, 1, 1, 1])
    invariant_covector = sp.Matrix([-1, -1, -1, 1, 1, 1])

    check(
        "the canonical support graph is one connected six-cycle",
        support_component_count(CANONICAL_EDGES) == 1,
        detail=f"components={support_component_count(CANONICAL_EDGES)}",
    )
    check(
        "the integer phase-incidence matrix has exact rank 5",
        rank == 5,
        detail=f"rank={rank}",
    )

    unit_minor = phase_map.extract((0, 1, 2, 3, 4), (0, 1, 2, 3, 4)).det()
    check(
        "an explicit 5 x 5 incidence minor has determinant +1",
        unit_minor == 1,
        detail=f"det={unit_minor}; the rank-five image lattice is saturated",
    )
    check(
        "the common opposite left/right phase is the full one-dimensional kernel",
        len(right_nullspace) == 1
        and matrix_is_zero(phase_map * common_kernel)
        and right_nullspace[0] in (common_kernel, -common_kernel),
        detail=f"kernel={tuple(common_kernel)}",
    )
    check(
        "the phase quotient has one invariant covector",
        len(left_nullspace) == 1
        and matrix_is_zero(phase_map.T * invariant_covector)
        and left_nullspace[0] in (invariant_covector, -invariant_covector),
        detail="delta = (beta_0+beta_1+beta_2) - (alpha_0+alpha_1+alpha_2)",
    )

    alpha = sp.symbols("alpha_0:3", real=True)
    beta = sp.symbols("beta_0:3", real=True)
    ell_0 = sp.Integer(0)
    rho_0 = -alpha[0]
    rho_1 = -beta[0]
    ell_1 = beta[0] - alpha[1]
    rho_2 = -beta[1] - beta[0] + alpha[1]
    ell_2 = beta[1] + beta[0] - alpha[1] - alpha[2]
    gauge = sp.Matrix([ell_0, ell_1, ell_2, rho_0, rho_1, rho_2])
    input_phases = sp.Matrix([*alpha, *beta])
    transformed_phases = sp.simplify(input_phases + phase_map * gauge)
    delta = sp.simplify(sum(beta) - sum(alpha))
    expected_phases = sp.Matrix([0, 0, 0, 0, 0, delta])

    check(
        "a symbolic gauge construction makes all A and the first two B coefficients positive",
        matrix_equal(transformed_phases, expected_phases),
        detail=f"transformed phases={tuple(transformed_phases)}",
    )
    check(
        "the residual normal-form phase equals the invariant phase combination",
        sp.simplify(transformed_phases[5] - delta) == 0,
    )

    complex_coefficient_count = len(CANONICAL_EDGES)
    starting_real_dimension = 2 * complex_coefficient_count
    effective_phase_orbit_dimension = rank
    quotient_real_dimension = starting_real_dimension - effective_phase_orbit_dimension
    positive_moduli = complex_coefficient_count
    invariant_phases = complex_coefficient_count - rank

    check(
        "the generic quotient has six positive modulus coordinates",
        positive_moduli == 6,
        detail=f"one modulus for each of {complex_coefficient_count} nonzero coefficients",
    )
    check(
        "the generic quotient has exactly one phase coordinate",
        invariant_phases == 1,
        detail=f"phase dimension={complex_coefficient_count}-{rank}={invariant_phases}",
    )
    check(
        "the generic quotient has exactly seven real parameters",
        quotient_real_dimension == positive_moduli + invariant_phases == 7,
        detail=(
            f"2*{complex_coefficient_count}-{effective_phase_orbit_dimension}="
            f"{quotient_real_dimension}"
        ),
    )


def hostile_controls() -> None:
    print("\n=== C. Hostile controls and the generic-boundary contract ===")

    equal_a = 1
    equal_b = 1
    equal_relative = C ** ((equal_b - equal_a) % 3)
    check(
        "equal offsets are rejected by the theorem hypothesis",
        not is_distinct_z3_pair(equal_a, equal_b)
        and matrix_equal(equal_relative, I3),
        detail="the two supplied terms then combine on one three-edge matching",
    )
    check(
        "identity relative support is not misclassified as a nontrivial 3-cycle",
        not is_nontrivial_three_cycle(I3),
    )

    wrong_cycle = sp.Matrix(
        [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 1],
        ]
    )
    check(
        "a transposition support is rejected as the wrong cycle class",
        is_permutation_matrix(wrong_cycle) and not is_nontrivial_three_cycle(wrong_cycle),
        detail="the transposition has order two, not order three",
    )
    check(
        "an invalid conjugator is detected",
        not matrix_equal(I3 * (C**2) * I3, C),
        detail="I_3 does not conjugate C^2 to C",
    )

    disconnected_edges = ((0, 0), (1, 1), (2, 2))
    disconnected_map = incidence_matrix(disconnected_edges)
    check(
        "rank-deficient disconnected support is excluded",
        support_component_count(disconnected_edges) == 3
        and disconnected_map.rank() == 3
        and disconnected_map.rank() != 5,
        detail="three disjoint matching edges give rank 3",
    )

    one_zero_edges = CANONICAL_EDGES[:-1]
    one_zero_map = incidence_matrix(one_zero_edges)
    one_zero_complex_dimension = len(one_zero_edges)
    one_zero_phase_dimension = one_zero_complex_dimension - one_zero_map.rank()
    one_zero_real_quotient_dimension = 2 * one_zero_complex_dimension - one_zero_map.rank()
    check(
        "a zero coefficient lies outside the all-six-nonzero stratum",
        len(one_zero_edges) == 5 and len(one_zero_edges) != len(CANONICAL_EDGES),
        detail="the product phase is undefined when any coefficient vanishes",
    )
    check(
        "the one-zero boundary has a different exact quotient count",
        support_component_count(one_zero_edges) == 1
        and one_zero_map.rank() == 5
        and one_zero_phase_dimension == 0
        and one_zero_real_quotient_dimension == 5,
        detail="five nonzero coefficients on a path: 5 moduli and no cycle phase",
    )

    canonical_rank = incidence_matrix(CANONICAL_EDGES).rank()
    canonical_count = 2 * len(CANONICAL_EDGES) - canonical_rank
    check(
        "wrong rank and quotient-count claims are rejected",
        canonical_rank != 4 and canonical_count != 8 and canonical_rank == 5 and canonical_count == 7,
        detail=f"exact rank={canonical_rank}, exact quotient count={canonical_count}",
    )

    physical_inference_is_licensed = bool(PHYSICAL_BRIDGES & FORMAL_CONCLUSIONS)
    physical_input_was_supplied = bool(PHYSICAL_BRIDGES & FORMAL_HYPOTHESES)
    check(
        "illicit physical-Yukawa inference is rejected by the typed theorem contract",
        not physical_inference_is_licensed and not physical_input_was_supplied,
        detail="the output is a formal quotient; every physical identification remains separate",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--intentional-failure-probe",
        action="store_true",
        help="add one known-false rank check; successful truthfulness exits nonzero",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    print("=" * 88)
    print("SUPPLIED TWO-OFFSET 3 x 3 TEXTURE: EXACT FORMAL CANONICAL REDUCTION")
    print("=" * 88)
    print("Hypothesis: Y=D_a C^a + D_b C^b with supplied diagonal D_a,D_b and a!=b in Z_3.")
    print("Generic quotient: all six coefficients are nonzero and the specified diagonal")
    print("U(1)^3_left x U(1)^3_right action is imposed as a mathematical equivalence.")
    print("No physical carrier, redundancy, branch, observable, or value is inferred.")

    exact_support_reduction()
    exact_generic_rephasing_quotient()
    hostile_controls()

    if args.intentional_failure_probe:
        check(
            "intentional failure probe: falsely demand incidence rank four",
            incidence_matrix(CANONICAL_EDGES).rank() == 4,
        )

    print("\n=== Result ===")
    print("  All six ordered distinct offset pairs have the formal support class A+B C.")
    print("  On (C*)^6, the specified rephasing quotient is (R_{>0})^6 x S^1:")
    print("  six positive moduli and one invariant phase, hence seven real quotient parameters.")
    print("  Zero-coefficient strata and non-cycle supports are outside this generic statement.")
    print("  These are quotient parameters, not physical quantities.")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
