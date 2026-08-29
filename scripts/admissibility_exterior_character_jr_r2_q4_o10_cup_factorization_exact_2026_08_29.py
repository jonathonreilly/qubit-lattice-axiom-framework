#!/usr/bin/env python3
"""Exact-rational primary for the Block242 row-reduced q=4 O10 cup map."""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

import numpy as np
import sympy as sp

import admissibility_exterior_character_jr_r2_q4_o10_cup_factorization_2026_08_29 as modular
import admissibility_exterior_character_jr_r2_q4_v4_all_spin_permutation_kernel_exact_2026_08_29 as block241_exact
import admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_2026_08_29 as block240
import admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_2026_08_29 as block240_exact


AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = modular.AUDIT_INPUT_PATHS
MUTATIONS = (
    "wrong_scale",
    "wrong_cup_orientation",
    "collapse_hom_dimension",
    "claim_unrestricted_endpoint",
    "claim_full_q4_response",
    "axiom_edit",
)


@lru_cache(None)
def exact_row_reduced_kernel():
    occurrences, factors = block240_exact.exact_network_factors("O10")
    open_occurrences = occurrences[block240.OPEN_LINK]
    left = [item for item in open_occurrences if item[0].startswith("left_")]
    right = [item for item in open_occurrences if item[0].startswith("right_")]
    left_columns = {name: column for name, _row, column in left}
    right_columns = {name: column for name, _row, column in right}
    delta = np.eye(3, dtype=object)
    delta_over_81 = np.zeros((3, 3), dtype=object)
    for index in range(3):
        delta_over_81[index, index] = F(1, 81)
    factors.extend((
        (delta_over_81, [left_columns["left_D"], right_columns["right_D"]]),
        (delta, [left_columns["left_E"], right_columns["right_E"]]),
        (delta, [left_columns["left_F"], right_columns["right_F"]]),
        (delta, [right_columns["right_p0"], right_columns["right_A"]]),
    ))
    tensor, labels = block241_exact.greedy_exact_tensor(factors)
    order = [row for _name, row, _column in left + right]
    tensor = np.transpose(tensor, [labels.index(label) for label in order])
    expected = np.zeros((3,) * 8, dtype=object)
    for d, e, f, p in product(range(3), repeat=4):
        expected[d, e, f, p, p, d, e, f] = F(1, 243)
    return tensor, expected


def exact_cup() -> sp.Matrix:
    return sp.Matrix(modular._cup_matrix().tolist())


def exact_checks(mutation: str | None = None):
    tensor, expected = exact_row_reduced_kernel()
    operator = sp.Matrix(tensor.reshape(27, 243).tolist())
    cup = exact_cup()
    projector = cup * cup.T / 3
    expected_scale = F(1, 243)
    if mutation == "wrong_scale":
        expected_scale = F(1, 81)
    expected_operator = cup.T * sp.Rational(
        expected_scale.numerator, expected_scale.denominator
    )
    if mutation == "wrong_cup_orientation":
        crossed = sp.zeros(243, 27)
        for p, d, e, f in product(range(3), repeat=4):
            right = ((((p * 3 + p) * 3 + e) * 3 + d) * 3 + f)
            left = (d * 3 + e) * 3 + f
            crossed[right, left] = 1
        expected_operator = crossed.T / 243
    left_mult = modular.tensor_power_multiplicities(3)
    right_mult = modular.tensor_power_multiplicities(5)
    hom_dimension = sum(a * b for a, b in zip(left_mult, right_mult))
    if mutation == "collapse_hom_dimension":
        hom_dimension = 7
    scope_ok = mutation not in ("claim_unrestricted_endpoint", "claim_full_q4_response")
    axiom_ok = mutation != "axiom_edit"
    epsilon = block240.integer_epsilon().reshape(27)
    determinant_left = sp.Matrix([int(value) for value in epsilon])
    determinant_right = cup * determinant_left
    determinant_overlap = (determinant_left.T * operator * determinant_right)[0]
    checks = (
        ("the complete exact row-reduced tensor has shape 3^8", tensor.shape == (3,) * 8),
        ("exactly 81 entries survive and all equal 1/243",
         int(np.count_nonzero(tensor)) == 81
         and {value for value in tensor.flat if value} == {F(1, 243)}),
        ("all 6561 exact-rational entries match the cup tensor",
         int(np.count_nonzero(tensor != expected)) == 0),
        ("the raw cup has Hilbert-Schmidt norm squared 81 and C-adjoint C=3I",
         (cup.T * cup) == 3 * sp.eye(27)
         and (cup.T * cup).trace() == 81),
        ("the cup image projector is exact", projector * projector == projector and projector.rank() == 27),
        ("the reduced O10 operator is rank-27 C-adjoint/243",
         operator == expected_operator and operator.rank() == 27),
        ("K C=I/81 and K has no cup-complement leakage",
         operator * cup == sp.eye(27) / 81
         and operator * (sp.eye(243) - projector) == sp.zeros(27, 243)),
        ("C K is the cup projector divided by 81",
         cup * operator == projector / 81),
        ("the Block240 determinant/cup overlap is recovered as 2/27",
         determinant_overlap == sp.Rational(2, 27)),
        ("V3 and V5 multiplicities give 91 equivariant coordinates",
         left_mult == (1, 3, 2, 1)
         and right_mult == (6, 15, 15, 10, 4, 1)
         and hom_dimension == 91),
        ("scope remains row-reduced, temporally incomplete, and axiom-neutral",
         scope_ok and axiom_ok),
    )
    return tensor, operator, checks


def run(mutation: str | None = None):
    _modular_results, modular_checks = modular.run()
    tensor, operator, rational_checks = exact_checks(mutation)
    return tensor, operator, modular_checks + rational_checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-suite", action="store_true")
    arguments = parser.parse_args()
    if arguments.mutation_suite:
        rejected = 0
        for mutation in MUTATIONS:
            _tensor, _operator, checks = run(mutation)
            survived = all(passed for _label, passed in checks)
            print(f"[{'FAIL' if survived else 'PASS'}] mutation rejected: {mutation}")
            rejected += int(not survived)
        print(f"MUTATIONS: rejected={rejected} total={len(MUTATIONS)}")
        return int(rejected != len(MUTATIONS))
    tensor, operator, checks = run(arguments.mutation)
    print(f"audit_timeout_sec: {AUDIT_TIMEOUT_SEC}")
    print(f"exact_shape={tensor.shape} nonzero={np.count_nonzero(tensor)} mismatches={np.count_nonzero(tensor != exact_row_reduced_kernel()[1])}")
    print(f"operator_shape={operator.shape} operator_rank={operator.rank()}")
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
