#!/usr/bin/env python3
"""Exact-rational primary for the Block241 all-spin q=4 O01 kernel."""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

import numpy as np
import sympy as sp

import admissibility_exterior_character_jr_r2_q4_v4_all_spin_permutation_kernel_2026_08_29 as modular
import admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_2026_08_29 as block240
import admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_2026_08_29 as block240_exact


AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = modular.AUDIT_INPUT_PATHS
MUTATIONS = (
    "wrong_physical_order",
    "wrong_scale",
    "collapse_spin_multiplicity",
    "claim_minimal_memory",
    "claim_full_q4_response",
    "axiom_edit",
)


def greedy_exact_tensor(factors):
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
        left_axes = [
            index for index, label in enumerate(left_labels) if label in shared
        ]
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
    return factors[0]


@lru_cache(None)
def exact_row_reduced_kernel():
    occurrences, factors = block240_exact.exact_network_factors("O01")
    open_occurrences = occurrences[block240.OPEN_LINK]
    left = [item for item in open_occurrences if item[0].startswith("left_")]
    right = [item for item in open_occurrences if item[0].startswith("right_")]
    normalized_delta = np.zeros((3, 3), dtype=object)
    for index in range(3):
        normalized_delta[index, index] = F(1, 3)
    for left_occurrence, right_occurrence in zip(left, right):
        factors.append((
            normalized_delta,
            [left_occurrence[2], right_occurrence[2]],
        ))
    tensor, labels = greedy_exact_tensor(factors)
    order = [row for _name, row, _column in left + right]
    tensor = np.transpose(tensor, [labels.index(label) for label in order])
    expected = np.zeros((3,) * 8, dtype=object)
    for a, b, c, d in product(range(3), repeat=4):
        expected[a, b, c, d, a, b, c, d] = F(1, 243)
    return tensor, expected


def _flat(indices: tuple[int, int, int, int]) -> int:
    result = 0
    for index in indices:
        result = 3 * result + index
    return result


def physical_cyclic_permutation(mutation: str | None = None) -> sp.Matrix:
    """Map right (A,D,E,F) to left (D,E,F,p0=A)."""

    permutation = sp.zeros(81, 81)
    for a, d, e, f in product(range(3), repeat=4):
        left = (d, e, f, a)
        if mutation == "wrong_physical_order":
            left = (a, d, e, f)
        permutation[_flat(left), _flat((a, d, e, f))] = 1
    return permutation


def _kron_all(factors: tuple[np.ndarray, ...]) -> np.ndarray:
    result = np.array([[1]], dtype=np.int64)
    for factor in factors:
        result = np.kron(result, factor)
    return result


def integer_total_casimir(power: int) -> np.ndarray:
    identity = np.eye(3, dtype=np.int64)
    generators = (
        np.array(((0, 0, 0), (0, 0, 1), (0, -1, 0)), dtype=np.int64),
        np.array(((0, 0, -1), (0, 0, 0), (1, 0, 0)), dtype=np.int64),
        np.array(((0, 1, 0), (-1, 0, 0), (0, 0, 0)), dtype=np.int64),
    )
    casimir = 2 * power * np.eye(3**power, dtype=np.int64)
    for left in range(power):
        for right in range(left + 1, power):
            for generator in generators:
                factors = tuple(
                    generator if position in (left, right) else identity
                    for position in range(power)
                )
                casimir -= 2 * _kron_all(factors)
    return casimir


@lru_cache(None)
def total_spin_projectors() -> dict[int, sp.Matrix]:
    casimir = sp.Matrix(integer_total_casimir(4).tolist())
    identity = sp.eye(81)
    projectors = {}
    for spin in range(5):
        eigenvalue = spin * (spin + 1)
        projector = identity
        denominator = 1
        for other in range(5):
            if other == spin:
                continue
            other_eigenvalue = other * (other + 1)
            projector = projector * (casimir - other_eigenvalue * identity)
            denominator *= eigenvalue - other_eigenvalue
        projectors[spin] = projector / denominator
    return projectors


def _embedded_generator(local: np.ndarray, position: int) -> np.ndarray:
    result = np.array([[1]], dtype=np.int64)
    identity = np.eye(3, dtype=np.int64)
    for slot in range(4):
        result = np.kron(result, local if slot == position else identity)
    return result


@lru_cache(None)
def nested_casimir_data():
    generators = (
        np.array(((0, 0, 0), (0, 0, -1), (0, 1, 0)), dtype=np.int64),
        np.array(((0, 0, 1), (0, 0, 0), (-1, 0, 0)), dtype=np.int64),
        np.array(((0, -1, 0), (1, 0, 0), (0, 0, 0)), dtype=np.int64),
    )
    embedded = {
        (axis, position): _embedded_generator(generator, position)
        for axis, generator in enumerate(generators)
        for position in range(4)
    }

    def total_generator(axis: int, positions: tuple[int, ...]) -> np.ndarray:
        return sum(
            (embedded[axis, position] for position in positions),
            np.zeros((81, 81), dtype=np.int64),
        )

    def casimir(positions: tuple[int, ...]) -> np.ndarray:
        return -sum(
            (
                total_generator(axis, positions)
                @ total_generator(axis, positions)
                for axis in range(3)
            ),
            np.zeros((81, 81), dtype=np.int64),
        )

    total_z = total_generator(2, (0, 1, 2, 3))
    return casimir((0, 1)), casimir((0, 1, 2)), casimir((0, 1, 2, 3)), total_z @ total_z


def _fraction_matvec(matrix: np.ndarray, vector: tuple[F, ...]) -> list[F]:
    result = []
    for row in range(81):
        result.append(sum(
            (F(int(matrix[row, column])) * vector[column]
             for column in np.flatnonzero(matrix[row])),
            F(0),
        ))
    return result


def _shifted_apply(
    matrix: np.ndarray,
    shift: int,
    vector: tuple[F, ...] | list[F],
) -> list[F]:
    product_vector = _fraction_matvec(matrix, tuple(vector))
    return [value + F(shift) * old for value, old in zip(product_vector, vector)]


def _spectral_project_vector(
    vector: tuple[F, ...] | list[F],
    casimir: np.ndarray,
    spin: int,
    allowed: range,
) -> list[F]:
    target = spin * (spin + 1)
    result = list(vector)
    for other in allowed:
        if other == spin:
            continue
        eigenvalue = other * (other + 1)
        result = [
            value / F(target - eigenvalue)
            for value in _shifted_apply(casimir, -eigenvalue, result)
        ]
    return result


def _m_zero_project_vector(
    vector: tuple[F, ...] | list[F],
    total_z_squared: np.ndarray,
) -> list[F]:
    result = list(vector)
    for magnetic in range(1, 5):
        result = [
            value / F(magnetic * magnetic)
            for value in _shifted_apply(
                total_z_squared, magnetic * magnetic, result
            )
        ]
    return result


def coupling_paths() -> tuple[tuple[int, int, int], ...]:
    return tuple(
        (pair_spin, triple_spin, total_spin)
        for pair_spin in range(3)
        for triple_spin in range(abs(pair_spin - 1), pair_spin + 2)
        for total_spin in range(abs(triple_spin - 1), triple_spin + 2)
    )


def exact_path_vector(path: tuple[int, int, int]) -> tuple[F, ...]:
    pair_casimir, triple_casimir, total_casimir, total_z_squared = (
        nested_casimir_data()
    )
    pair_spin, triple_spin, total_spin = path
    for seed in range(81):
        vector = [F(0) for _ in range(81)]
        vector[seed] = F(1)
        vector = _spectral_project_vector(vector, pair_casimir, pair_spin, range(3))
        vector = _spectral_project_vector(
            vector, triple_casimir, triple_spin, range(4)
        )
        vector = _spectral_project_vector(
            vector, total_casimir, total_spin, range(5)
        )
        vector = _m_zero_project_vector(vector, total_z_squared)
        if any(vector):
            pivot = next(value for value in vector if value)
            return tuple(value / pivot for value in vector)
    raise AssertionError(f"failed to construct path {path}")


@lru_cache(None)
def exact_coordinate_blocks():
    permutation = physical_cyclic_permutation()
    by_spin = {spin: [] for spin in range(5)}
    for path in coupling_paths():
        by_spin[path[2]].append(path)
    blocks = {}
    norms = {}
    for spin, paths in by_spin.items():
        vectors = [
            sp.Matrix([
                sp.Rational(value.numerator, value.denominator)
                for value in exact_path_vector(path)
            ])
            for path in paths
        ]
        path_norms = tuple((vector.T * vector)[0] for vector in vectors)
        gram = sp.diag(*path_norms)
        cyclic_form = sp.Matrix([
            [(left.T * permutation * right)[0] for right in vectors]
            for left in vectors
        ])
        norms[spin] = path_norms
        blocks[spin] = gram.inv() * cyclic_form
    return {spin: tuple(paths) for spin, paths in by_spin.items()}, norms, blocks


def expected_coordinate_blocks():
    q = sp.Rational
    return {
        0: sp.Matrix([
            [q(1, 3), q(-2, 3), q(5, 6)],
            [q(-1, 2), q(1, 2), q(5, 8)],
            [q(2, 3), q(2, 3), q(1, 6)],
        ]),
        1: sp.Matrix([
            [q(-1, 3), 0, q(-2, 3), 0, q(-5, 6), 0],
            [q(1, 3), q(1, 3), q(1, 3), q(-5, 9), q(-5, 12), q(5, 6)],
            [q(-1, 4), q(-1, 2), q(-1, 4), q(-5, 12), q(5, 16), q(5, 8)],
            [q(-1, 4), q(1, 2), q(-1, 4), q(-1, 12), q(5, 16), q(1, 8)],
            [q(1, 3), 0, q(-1, 3), -1, q(1, 12), q(-1, 2)],
            [q(1, 2), 0, q(-1, 2), q(1, 2), q(1, 8), q(1, 4)],
        ]),
        2: sp.Matrix([
            [q(1, 3), q(-2, 3), 0, q(5, 6), 0, 0],
            [q(1, 4), q(-1, 4), q(1, 4), q(-5, 16), q(-3, 8), 0],
            [q(-3, 4), q(3, 4), q(1, 4), q(15, 16), q(-3, 8), 0],
            [q(1, 15), q(1, 15), q(1, 5), q(1, 60), q(1, 10), q(14, 15)],
            [q(-1, 2), q(-1, 2), q(-5, 6), q(-1, 8), q(-5, 12), q(7, 9)],
            [q(3, 5), q(3, 5), q(-1, 5), q(3, 20), q(-1, 10), q(1, 15)],
        ]),
        3: sp.Matrix([
            [q(-1, 2), q(3, 4), 0],
            [q(-1, 3), q(-1, 6), q(8, 9)],
            [-1, q(-1, 2), q(-1, 3)],
        ]),
        4: sp.Matrix([[1]]),
    }


def representation_data(mutation: str | None = None):
    permutation = physical_cyclic_permutation(mutation)
    identity = sp.eye(81)
    projectors = total_spin_projectors()
    multiplicities = {}
    spectra = {}
    traces = {}
    for spin, projector in projectors.items():
        carrier_dimension = 2 * spin + 1
        multiplicity = int(sp.trace(projector) / carrier_dimension)
        if mutation == "collapse_spin_multiplicity" and spin == 1:
            multiplicity -= 1
        trace_one = sp.trace(projector * permutation) / carrier_dimension
        trace_two = sp.trace(projector * permutation**2) / carrier_dimension
        trace_three = sp.trace(projector * permutation**3) / carrier_dimension
        imaginary_pairs = sp.simplify((multiplicity - trace_two) / 4)
        real_total = sp.simplify(multiplicity - 2 * imaginary_pairs)
        plus = sp.simplify((real_total + trace_one) / 2)
        minus = sp.simplify((real_total - trace_one) / 2)
        multiplicities[spin] = multiplicity
        traces[spin] = (trace_one, trace_two, trace_three)
        spectra[spin] = (plus, minus, imaginary_pairs)
    return {
        "permutation": permutation,
        "projectors": projectors,
        "multiplicities": multiplicities,
        "traces": traces,
        "spectra": spectra,
        "orthogonal": permutation.T * permutation == identity,
        "order_four": permutation**4 == identity,
        "equivariant": all(
            permutation * projector == projector * permutation
            for projector in projectors.values()
        ),
        "complete": sum(projectors.values(), sp.zeros(81, 81)) == identity,
        "orthogonal_projectors": all(
            left * right == (left if left_spin == right_spin else sp.zeros(81, 81))
            for left_spin, left in projectors.items()
            for right_spin, right in projectors.items()
        ),
    }


def k0_raw_overlap(permutation: sp.Matrix) -> sp.Matrix:
    invariants = [
        sp.Matrix(block240.integer_k0_invariant(channel).reshape(-1).tolist())
        for channel in range(3)
    ]
    return sp.Matrix([
        [(left.T * permutation * right)[0] for right in invariants]
        for left in invariants
    ])


def scope_check(mutation: str | None = None) -> bool:
    note = (modular.ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8").lower()
    scope = (
        "actual_current_surface_status: conditional-support" in note
        and "status: conditional-support" in note
        and "proposal_allowed: false" in note
        and "row-reduced" in note
        and "no full `q=4` temporal response is claimed" in note
        and "minimal memory remains open" in note
        and "axiom/primitive effect:** none" in note
    )
    if mutation in {"claim_minimal_memory", "claim_full_q4_response", "axiom_edit"}:
        scope = False
    return scope


def exact_checks(mutation: str | None = None):
    tensor, expected = exact_row_reduced_kernel()
    representation = representation_data(mutation)
    permutation = representation["permutation"]
    scale = F(1, 243) if mutation != "wrong_scale" else F(1, 81)
    expected_multiplicities = {0: 3, 1: 6, 2: 6, 3: 3, 4: 1}
    expected_traces = {
        0: (1, 3, 1),
        1: (0, -2, 0),
        2: (0, 2, 0),
        3: (-1, -1, -1),
        4: (1, 1, 1),
    }
    expected_spectra = {
        0: (2, 1, 0),
        1: (1, 1, 2),
        2: (2, 2, 1),
        3: (0, 1, 1),
        4: (1, 0, 0),
    }
    expected_paths = {
        0: ((0, 1, 0), (1, 1, 0), (2, 1, 0)),
        1: ((0, 1, 1), (1, 0, 1), (1, 1, 1), (1, 2, 1), (2, 1, 1), (2, 2, 1)),
        2: ((0, 1, 2), (1, 1, 2), (1, 2, 2), (2, 1, 2), (2, 2, 2), (2, 3, 2)),
        3: ((1, 2, 3), (2, 2, 3), (2, 3, 3)),
        4: ((2, 3, 4),),
    }
    expected_norms = {
        0: (sp.Integer(9), sp.Integer(12), sp.Rational(45, 4)),
        1: (sp.Integer(6), sp.Integer(6), sp.Integer(8), sp.Rational(40, 3), sp.Rational(15, 2), sp.Integer(10)),
        2: (sp.Integer(18), sp.Integer(24), sp.Integer(8), sp.Rational(45, 2), sp.Integer(6), sp.Rational(70, 3)),
        3: (sp.Integer(20), sp.Integer(15), sp.Rational(40, 3)),
        4: (sp.Rational(280, 9),),
    }
    coordinate_paths, coordinate_norms, coordinate_blocks = exact_coordinate_blocks()
    expected_blocks = expected_coordinate_blocks()
    raw_overlap = k0_raw_overlap(permutation)
    return representation, (
        ("the complete row-reduced tensor is exact over Q",
         tensor.shape == (3,) * 8 and np.count_nonzero(tensor != expected) == 0),
        ("the exact tensor has 81 entries, each 1/243",
         np.count_nonzero(tensor) == 81
         and set(tensor.flatten()) - {0} == {F(1, 243)}
         and scale == F(1, 243)),
        ("the physical strand map is an orthogonal order-four permutation",
         representation["orthogonal"] and representation["order_four"]),
        ("the permutation commutes with every total-spin projector",
         representation["equivariant"]),
        ("the five rational total-spin projectors are complete and orthogonal",
         representation["complete"] and representation["orthogonal_projectors"]),
        ("V^4 has multiplicities 3,6,6,3,1",
         representation["multiplicities"] == expected_multiplicities),
        ("the cyclic multiplicity-block traces are exact for powers one to three",
         representation["traces"] == expected_traces),
        ("all five multiplicity spectra are fixed by fourth roots of unity",
         representation["spectra"] == expected_spectra),
        ("the five spin sectors exhaust all 81 carrier dimensions",
         sum((2 * spin + 1) * multiplicity
             for spin, multiplicity in representation["multiplicities"].items()) == 81),
        ("the equivariant V^4 commutant has dimension 91",
         sum(value * value for value in representation["multiplicities"].values()) == 91),
        ("nested pair/triple/total Casimirs resolve the canonical 19 paths",
         coordinate_paths == expected_paths and coordinate_norms == expected_norms),
        ("the exact rational coordinate matrices fix every all-spin block",
         coordinate_blocks == expected_blocks),
        ("every coordinate block is full rank and has fourth power one",
         all(
             block.rank() == block.rows and block**4 == sp.eye(block.rows)
             for block in coordinate_blocks.values()
         )),
        ("every rational coordinate block is orthogonal in its exact path Gram metric",
         all(
             block.T * sp.diag(*coordinate_norms[spin]) * block
             == sp.diag(*coordinate_norms[spin])
             for spin, block in coordinate_blocks.items()
         )),
        ("the explicit blocks have the independently counted support",
         tuple(sum(int(value != 0) for value in block)
               for block in coordinate_blocks.values()) == (9, 31, 31, 8, 1)),
        ("the cyclic permutation reproduces the reviewed raw K=0 matrix",
         raw_overlap == sp.Matrix(block240.RAW_RECOUPLING.tolist())),
        ("the theorem keeps response, memory, and axiom boundaries honest",
         scope_check(mutation)),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-suite", action="store_true")
    arguments = parser.parse_args()
    if arguments.mutation_suite:
        rejected = 0
        for mutation in MUTATIONS:
            _representation, checks = exact_checks(mutation)
            survived = all(passed for _label, passed in checks)
            print(f"[{'FAIL' if survived else 'PASS'}] mutation rejected: {mutation}")
            rejected += int(not survived)
        print(f"MUTATIONS: rejected={rejected} total={len(MUTATIONS)}")
        return int(rejected != len(MUTATIONS))

    modular_results, modular_checks = modular.run()
    representation, rational_checks = exact_checks(arguments.mutation)
    coordinate_paths, coordinate_norms, coordinate_blocks = exact_coordinate_blocks()
    checks = modular_checks + rational_checks
    print(f"audit_timeout_sec: {AUDIT_TIMEOUT_SEC}")
    print(f"multiplicities: {representation['multiplicities']}")
    print(f"cyclic_traces: {representation['traces']}")
    print(f"cyclic_spectra_(plus,minus,i_pairs): {representation['spectra']}")
    for spin in range(5):
        print(f"K={spin} paths: {coordinate_paths[spin]}")
        print(f"K={spin} norms: {coordinate_norms[spin]}")
        print(f"K={spin} coordinate_cycle_block: {coordinate_blocks[spin].tolist()}")
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
