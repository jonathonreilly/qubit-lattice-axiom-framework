#!/usr/bin/env python3
"""Exact-rational audit primary for the Block240 q=4 V^4 junction.

The imported finite-field helper performs the fast endpoint checks.  This
primary executes those checks, then contracts the decisive O01 K=0 block and
the disclosed unnormalized O10 determinant/cup row overlap over Q.  It imports
the helper's geometry and basis code, so the two scripts form one audit chain
rather than independent implementations.  Degree eight is represented in a
91-element independent Brauer basis, never as a dense 3^16 Haar tensor.
"""

from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache
from itertools import product

import numpy as np
import sympy as sp

import admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_2026_08_29 as modular


AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = modular.AUDIT_INPUT_PATHS


@lru_cache(None)
def exact_moment_factors(degree: int):
    # Independence modulo 1009 implies independence over Q; the rational
    # inverse below is the final gate and would fail if the principal Gram
    # block were singular on the actual surface.
    basis = modular.independent_pairings(degree, 1009)
    gram = sp.Matrix([
        [3 ** modular.joined_pairing_loops(left, right, degree)
         for right in basis]
        for left in basis
    ])
    inverse = gram.inv()
    rational_inverse = np.empty(inverse.shape, dtype=object)
    for row in range(inverse.rows):
        for column in range(inverse.cols):
            entry = inverse[row, column]
            rational_inverse[row, column] = F(
                int(sp.numer(entry)), int(sp.denom(entry))
            )
    pairing_tensor = np.zeros((3,) * degree + (len(basis),), dtype=object)
    for indices in product(range(3), repeat=degree):
        for basis_index, pairing in enumerate(basis):
            pairing_tensor[indices + (basis_index,)] = int(
                all(indices[left] == indices[right] for left, right in pairing)
            )
    return pairing_tensor, rational_inverse, len(basis)


def exact_network_factors(orientation: str):
    occurrences = modular.original_link_occurrences(orientation)
    factors = []
    next_auxiliary = 400_000
    for link, link_occurrences in occurrences.items():
        if link == modular.OPEN_LINK:
            continue
        pairing_tensor, inverse_gram, _basis_size = exact_moment_factors(
            len(link_occurrences)
        )
        row_auxiliary = next_auxiliary
        column_auxiliary = next_auxiliary + 1
        next_auxiliary += 2
        factors.extend((
            (pairing_tensor, [row for _name, row, _column in link_occurrences]
             + [row_auxiliary]),
            (inverse_gram, [row_auxiliary, column_auxiliary]),
            (pairing_tensor, [column for _name, _row, column in link_occurrences]
             + [column_auxiliary]),
        ))
    return occurrences, factors


def greedy_exact_contract(factors):
    factors = list(factors)
    while len(factors) > 1:
        best = None
        for left_index, (left_tensor, left_labels) in enumerate(factors):
            for right_index in range(left_index + 1, len(factors)):
                right_tensor, right_labels = factors[right_index]
                shared = set(left_labels) & set(right_labels)
                if not shared:
                    continue
                output_labels = (
                    [label for label in left_labels if label not in shared]
                    + [label for label in right_labels if label not in shared]
                )
                output_size = 1
                for label in output_labels:
                    if label in left_labels:
                        output_size *= left_tensor.shape[left_labels.index(label)]
                    else:
                        output_size *= right_tensor.shape[right_labels.index(label)]
                score = (output_size, len(output_labels), -len(shared))
                if best is None or score < best[0]:
                    best = (score, left_index, right_index, shared)
        if best is None:
            raise AssertionError("exact original-link network disconnected")
        _score, left_index, right_index, shared = best
        left_tensor, left_labels = factors[left_index]
        right_tensor, right_labels = factors[right_index]
        left_axes = [index for index, label in enumerate(left_labels) if label in shared]
        shared_order = [left_labels[index] for index in left_axes]
        right_axes = [right_labels.index(label) for label in shared_order]
        result = np.tensordot(
            left_tensor, right_tensor, axes=(left_axes, right_axes)
        )
        result_labels = (
            [label for label in left_labels if label not in shared]
            + [label for label in right_labels if label not in shared]
        )
        for index in sorted((left_index, right_index), reverse=True):
            factors.pop(index)
        factors.append((result, result_labels))
    tensor, labels = factors[0]
    if labels or tensor.shape:
        raise AssertionError("exact contraction did not close to a scalar")
    return tensor.item()


def exact_o01_entry(left_channel: int, right_channel: int):
    occurrences, factors = exact_network_factors("O01")
    open_occurrences = occurrences[modular.OPEN_LINK]
    left = [item for item in open_occurrences if item[0].startswith("left_")]
    right = [item for item in open_occurrences if item[0].startswith("right_")]
    left_rows = {name: row for name, row, _column in left}
    right_rows = {name: row for name, row, _column in right}
    factors.extend((
        (modular.integer_k0_invariant(left_channel).astype(object),
         [left_rows[name] for name in ("left_D", "left_E", "left_F", "left_p0")]),
        (modular.integer_k0_invariant(right_channel).astype(object),
         [right_rows[name] for name in ("right_A", "right_D", "right_E", "right_F")]),
    ))
    normalized_delta = np.zeros((3, 3), dtype=object)
    for index in range(3):
        normalized_delta[index, index] = F(1, 3)
    for (_left_name, _left_row, left_column), (
        _right_name, _right_row, right_column
    ) in zip(left, right):
        factors.append((normalized_delta, [left_column, right_column]))
    return greedy_exact_contract(factors)


def exact_o10_determinant_cup():
    occurrences, factors = exact_network_factors("O10")
    open_occurrences = occurrences[modular.OPEN_LINK]
    left = [item for item in open_occurrences if item[0].startswith("left_")]
    right = [item for item in open_occurrences if item[0].startswith("right_")]
    left_rows = {name: row for name, row, _column in left}
    right_rows = {name: row for name, row, _column in right}
    left_columns = {name: column for name, _row, column in left}
    right_columns = {name: column for name, _row, column in right}
    epsilon = modular.integer_epsilon().astype(object)
    delta = np.eye(3, dtype=object)
    normalized_delta = delta.copy()
    for index in range(3):
        normalized_delta[index, index] = F(1, 81)
    factors.extend((
        (epsilon, [left_rows[name] for name in ("left_D", "left_E", "left_F")]),
        (epsilon, [right_rows[name] for name in ("right_D", "right_E", "right_F")]),
        (delta, [right_rows["right_p0"], right_rows["right_A"]]),
        (normalized_delta, [left_columns["left_D"], right_columns["right_D"]]),
        (delta, [left_columns["left_E"], right_columns["right_E"]]),
        (delta, [left_columns["left_F"], right_columns["right_F"]]),
        (delta, [right_columns["right_p0"], right_columns["right_A"]]),
    ))
    return greedy_exact_contract(factors)


def main() -> int:
    modular_results = modular.run_probe()
    modular_checks = tuple(
        (f"F_{prime}: {label}", passed)
        for prime, result in modular_results.items()
        for label, passed in modular.checks_for_prime(prime, result, None)
    )
    actual_o01 = tuple(
        tuple(exact_o01_entry(left, right) for right in range(3))
        for left in range(3)
    )
    expected_o01 = tuple(
        tuple(F(int(modular.RAW_RECOUPLING[left, right]), 243)
              for right in range(3))
        for left in range(3)
    )
    actual_o10 = exact_o10_determinant_cup()
    rational_checks = (
        ("degree-eight rational Brauer basis has size 91",
         exact_moment_factors(8)[2] == 91),
        ("O01 raw K=0 recoupling block is exact over Q",
         actual_o01 == expected_o01),
        ("O10 unnormalized determinant/cup row overlap is 18/243 over Q",
         actual_o10 == F(2, 27)),
    )
    checks = modular_checks + rational_checks
    print(f"audit_timeout_sec: {AUDIT_TIMEOUT_SEC}")
    print(f"o01_actual: {actual_o01}")
    print(f"o01_expected: {expected_o01}")
    print(f"o10_actual: {actual_o10} expected: {F(2, 27)}")
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
