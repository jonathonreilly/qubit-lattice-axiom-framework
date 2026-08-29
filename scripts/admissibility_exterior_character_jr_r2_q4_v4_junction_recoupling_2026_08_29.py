#!/usr/bin/env python3
"""Exact finite-field certificate for the Block240 q=4 V^4 junction.

This bounded certificate constructs
the nine original-link traces, integrates every non-h0 link in an independent
Brauer basis, and projects O01 into the three K=0 multiplicity channels.  The
degree-eight O(3) moment uses a 91-element independent subbasis of the 105
pairings, avoiding both a singular inverse and a dense 3^16 moment tensor.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path

import numpy as np


PRIMES = (1009, 1013, 1019)
OPEN_LINK = "h0"
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_V4_JUNCTION_RECOUPLING_EXACT_SUPPORT_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_SEVEN_CHANNEL_TEMPORAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_ORIENTED_VECTOR_TRIPLE_CHANNEL_RESOLUTION_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
MUTATIONS = (
    "wrong_rank",
    "wrong_census",
    "wrong_o01",
    "wrong_o10_scalar",
    "wrong_o10_cup",
    "wrong_parity",
    "wrong_action",
    "claim_full_response",
)
VECTOR = (1, -1)
ROOT = Path(__file__).resolve().parents[1]


def fine_plaquette(index: int):
    return (
        (f"u{index}", 1),
        (f"h{index + 1}", 1),
        (f"v{index}", -1),
        (f"h{index}", -1),
    )


def merged_interval(first_cell: int, last_cell: int):
    first = 2 * first_cell
    last = 2 * last_cell + 1
    return tuple(
        [(f"u{index}", 1) for index in range(first, last + 1)]
        + [(f"h{last + 1}", 1)]
        + [(f"v{index}", -1) for index in range(last, first - 1, -1)]
        + [(f"h{first}", -1)]
    )


A = merged_interval(0, 0)
D = merged_interval(0, 1)
E = merged_interval(0, 2)
F = merged_interval(0, 3)


def repeated_fine_word(first_cell: int, last_cell: int) -> frozenset[int]:
    return frozenset(range(2 * first_cell, 2 * last_cell + 2))


def parity_placements() -> tuple[tuple[int, int, int, int], ...]:
    y_word = (
        repeated_fine_word(0, 1)
        ^ repeated_fine_word(0, 2)
        ^ repeated_fine_word(0, 3)
    )
    z_word = repeated_fine_word(0, 0) ^ y_word
    matches = []
    for p_y in range(8):
        for p_z in range(8):
            for parity_y in (-1, 1):
                for parity_z in (-1, 1):
                    left = y_word ^ (
                        frozenset((p_y,)) if parity_y == -1 else frozenset()
                    )
                    right = z_word ^ (
                        frozenset((p_z,)) if parity_z == -1 else frozenset()
                    )
                    if left == right:
                        matches.append((p_y, p_z, parity_y, parity_z))
    return tuple(matches)


def scalar_in_product(left: tuple[int, int], right: tuple[int, int]) -> bool:
    """Return whether two O(3) irreps contain the even scalar."""

    return left[0] == right[0] and left[1] * right[1] == 1


def action_irrep_survivors():
    # The supplied n=1 exterior-action menu is V, det tensor V, and det.
    # Enumerate it on both rails instead of inserting the desired answer.
    action_labels = (VECTOR, (1, 1), (0, -1))
    left_survivors = tuple(
        label for label in action_labels if scalar_in_product(VECTOR, label)
    )
    right_survivors = tuple(
        label for label in action_labels if scalar_in_product(VECTOR, label)
    )
    return tuple(product(left_survivors, right_survivors))


def authority_and_scope() -> bool:
    note = (ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    return (
        "actual_current_surface_status: exact-support" in note
        and "complete unprojected `3^16` tensor" in note
        and "symbolic identity over `Q`" in note
        and "No full `q=4` temporal response is claimed" in note
        and "Axiom/primitive effect:** none" in note
    )


def trace_family(orientation: str):
    if orientation == "O01":
        return (
            ("left_p0", fine_plaquette(0)),
            ("left_D", D),
            ("left_E", E),
            ("left_F", F),
            ("right_p1", fine_plaquette(1)),
            ("right_A", A),
            ("right_D", D),
            ("right_E", E),
            ("right_F", F),
        )
    if orientation == "O10":
        return (
            ("left_p1", fine_plaquette(1)),
            ("left_D", D),
            ("left_E", E),
            ("left_F", F),
            ("right_p0", fine_plaquette(0)),
            ("right_A", A),
            ("right_D", D),
            ("right_E", E),
            ("right_F", F),
        )
    raise ValueError("orientation must be O01 or O10")


def original_link_occurrences(orientation: str):
    occurrences = defaultdict(list)
    next_node = 0
    for trace_name, loop in trace_family(orientation):
        nodes = tuple(range(next_node, next_node + len(loop)))
        next_node += len(loop)
        for position, (link, direction) in enumerate(loop):
            first = nodes[position]
            second = nodes[(position + 1) % len(loop)]
            row, column = (first, second) if direction == 1 else (second, first)
            occurrences[link].append((trace_name, row, column))
    return occurrences


@lru_cache(None)
def pair_partitions(items: tuple[int, ...]):
    if not items:
        return ((),)
    first = items[0]
    result = []
    for position in range(1, len(items)):
        second = items[position]
        rest = items[1:position] + items[position + 1:]
        for tail in pair_partitions(rest):
            result.append(((first, second),) + tail)
    return tuple(result)


def joined_pairing_loops(left, right, degree: int) -> int:
    parent = list(range(degree))

    def find(item: int) -> int:
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    for a, b in left + right:
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a
    return len({find(item) for item in range(degree)})


def independent_pairings(degree: int, prime: int):
    pairings = pair_partitions(tuple(range(degree)))
    gram = [
        [3 ** joined_pairing_loops(left, right, degree) % prime
         for right in pairings]
        for left in pairings
    ]
    rows = []
    pivots = []
    selected = []
    for pairing_index, candidate in enumerate(gram):
        row = candidate[:]
        for previous, pivot in zip(rows, pivots):
            if row[pivot]:
                coefficient = row[pivot]
                row = [
                    (value - coefficient * old) % prime
                    for value, old in zip(row, previous)
                ]
        pivot = next((index for index, value in enumerate(row) if value), None)
        if pivot is None:
            continue
        inverse = pow(row[pivot], -1, prime)
        row = [value * inverse % prime for value in row]
        for index, previous in enumerate(rows):
            if previous[pivot]:
                coefficient = previous[pivot]
                rows[index] = [
                    (value - coefficient * new) % prime
                    for value, new in zip(previous, row)
                ]
        rows.append(row)
        pivots.append(pivot)
        selected.append(pairing_index)
    return tuple(pairings[index] for index in selected)


def invert_mod(matrix, prime: int):
    size = len(matrix)
    augmented = [
        [int(matrix[row][column]) % prime for column in range(size)]
        + [int(row == column) for column in range(size)]
        for row in range(size)
    ]
    for column in range(size):
        pivot = next(row for row in range(column, size) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        inverse = pow(augmented[column][column], -1, prime)
        augmented[column] = [value * inverse % prime for value in augmented[column]]
        for row in range(size):
            if row != column and augmented[row][column]:
                coefficient = augmented[row][column]
                augmented[row] = [
                    (value - coefficient * pivot_value) % prime
                    for value, pivot_value in zip(augmented[row], augmented[column])
                ]
    return np.asarray([row[size:] for row in augmented], dtype=np.int64)


@lru_cache(None)
def modular_moment_factors(degree: int, prime: int):
    basis = independent_pairings(degree, prime)
    gram = [
        [3 ** joined_pairing_loops(left, right, degree) % prime
         for right in basis]
        for left in basis
    ]
    inverse_gram = invert_mod(gram, prime)
    pairing_tensor = np.zeros((3,) * degree + (len(basis),), dtype=np.int64)
    for indices in product(range(3), repeat=degree):
        for basis_index, pairing in enumerate(basis):
            pairing_tensor[indices + (basis_index,)] = int(
                all(indices[left] == indices[right] for left, right in pairing)
            )
    return basis, pairing_tensor, inverse_gram


def integer_k0_invariant(channel: int):
    tensor = np.zeros((3, 3, 3, 3), dtype=np.int64)
    delta = lambda left, right: int(left == right)
    for a, b, c, e in product(range(3), repeat=4):
        if channel == 0:
            value = delta(a, b) * delta(c, e)
        elif channel == 1:
            value = delta(a, c) * delta(b, e) - delta(a, e) * delta(b, c)
        elif channel == 2:
            value = (
                3 * (delta(a, c) * delta(b, e) + delta(a, e) * delta(b, c))
                - 2 * delta(a, b) * delta(c, e)
            )
        else:
            raise ValueError("K=0 path channel must be 0, 1, or 2")
        tensor[a, b, c, e] = value
    return tensor


def integer_epsilon():
    tensor = np.zeros((3, 3, 3), dtype=np.int64)
    for a, b, c in product(range(3), repeat=3):
        if len({a, b, c}) < 3:
            continue
        inversions = int(a > b) + int(a > c) + int(b > c)
        tensor[a, b, c] = -1 if inversions % 2 else 1
    return tensor


RAW_GRAM = np.diag((9, 12, 180))
RAW_RECOUPLING = np.asarray(((3, -6, 30), (-6, 6, 30), (30, 30, 30)))


def projected_factors(left_channel: int, right_channel: int, prime: int):
    occurrences = original_link_occurrences("O01")
    factors = []
    next_auxiliary = 100_000
    for link, link_occurrences in occurrences.items():
        if link == OPEN_LINK:
            continue
        degree = len(link_occurrences)
        _basis, pairing_tensor, inverse_gram = modular_moment_factors(degree, prime)
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

    open_occurrences = occurrences[OPEN_LINK]
    left = [item for item in open_occurrences if item[0].startswith("left_")]
    right = [item for item in open_occurrences if item[0].startswith("right_")]
    if len(left) != 4 or len(right) != 4:
        raise AssertionError("O01 must expose V^4 on both sides")
    left_rows = {name: row for name, row, _column in left}
    right_rows = {name: row for name, row, _column in right}
    factors.append((
        integer_k0_invariant(left_channel) % prime,
        [left_rows[name] for name in ("left_D", "left_E", "left_F", "left_p0")],
    ))
    factors.append((
        integer_k0_invariant(right_channel) % prime,
        [right_rows[name] for name in ("right_A", "right_D", "right_E", "right_F")],
    ))
    normalized_delta = np.eye(3, dtype=np.int64) * pow(3, -1, prime) % prime
    for (_left_name, _left_row, left_column), (
        _right_name, _right_row, right_column
    ) in zip(left, right):
        factors.append((normalized_delta, [left_column, right_column]))
    return factors, Counter(
        len(link_occurrences)
        for link, link_occurrences in occurrences.items()
        if link != OPEN_LINK
    )


def o10_determinant_cup_factors(prime: int):
    """Take the disclosed unnormalized O10 determinant/cup row overlap.

    The row closure is epsilon(D,E,F) on the left and
    delta(p0,A) epsilon(D,E,F) on the right, whose overlap with the raw
    candidate is 18.  The column copy of the candidate is divided by its
    norm-squared 81.  The computed raw overlap is 18/243=2/27; this function
    does not certify a normalized determinant-channel weight.
    """

    occurrences = original_link_occurrences("O10")
    factors = []
    next_auxiliary = 200_000
    for link, link_occurrences in occurrences.items():
        if link == OPEN_LINK:
            continue
        degree = len(link_occurrences)
        _basis, pairing_tensor, inverse_gram = modular_moment_factors(degree, prime)
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

    open_occurrences = occurrences[OPEN_LINK]
    left = [item for item in open_occurrences if item[0].startswith("left_")]
    right = [item for item in open_occurrences if item[0].startswith("right_")]
    if len(left) != 3 or len(right) != 5:
        raise AssertionError("O10 must expose V^3 on the left and V^5 on the right")
    left_rows = {name: row for name, row, _column in left}
    right_rows = {name: row for name, row, _column in right}
    left_columns = {name: column for name, _row, column in left}
    right_columns = {name: column for name, _row, column in right}
    epsilon = integer_epsilon() % prime
    delta = np.eye(3, dtype=np.int64)
    factors.extend((
        (epsilon, [left_rows[name] for name in ("left_D", "left_E", "left_F")]),
        (epsilon, [right_rows[name] for name in ("right_D", "right_E", "right_F")]),
        (delta, [right_rows["right_p0"], right_rows["right_A"]]),
        (delta * pow(81, -1, prime) % prime,
         [left_columns["left_D"], right_columns["right_D"]]),
        (delta, [left_columns["left_E"], right_columns["right_E"]]),
        (delta, [left_columns["left_F"], right_columns["right_F"]]),
        (delta, [right_columns["right_p0"], right_columns["right_A"]]),
    ))
    return factors


def o10_determinant_cup_open_factors(prime: int):
    """Project the row endpoint and leave all eight column indices open."""

    occurrences = original_link_occurrences("O10")
    factors = []
    next_auxiliary = 300_000
    for link, link_occurrences in occurrences.items():
        if link == OPEN_LINK:
            continue
        degree = len(link_occurrences)
        _basis, pairing_tensor, inverse_gram = modular_moment_factors(degree, prime)
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
    open_occurrences = occurrences[OPEN_LINK]
    left = [item for item in open_occurrences if item[0].startswith("left_")]
    right = [item for item in open_occurrences if item[0].startswith("right_")]
    left_rows = {name: row for name, row, _column in left}
    right_rows = {name: row for name, row, _column in right}
    columns = {name: column for name, _row, column in left + right}
    factors.extend((
        (integer_epsilon() % prime,
         [left_rows[name] for name in ("left_D", "left_E", "left_F")]),
        (integer_epsilon() % prime,
         [right_rows[name] for name in ("right_D", "right_E", "right_F")]),
        (np.eye(3, dtype=np.int64),
         [right_rows["right_p0"], right_rows["right_A"]]),
    ))
    output_order = [
        columns[name] for name in (
            "left_D", "left_E", "left_F",
            "right_p0", "right_A", "right_D", "right_E", "right_F",
        )
    ]
    return factors, output_order


def greedy_modular_tensor(factors, prime: int):
    factors = list(factors)
    while len(factors) > 1:
        best = None
        for left_index, (_left_tensor, left_labels) in enumerate(factors):
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
                        output_size *= factors[left_index][0].shape[
                            left_labels.index(label)
                        ]
                    else:
                        output_size *= right_tensor.shape[right_labels.index(label)]
                score = (output_size, len(output_labels), -len(shared))
                if best is None or score < best[0]:
                    best = (score, left_index, right_index, shared)
        if best is None:
            raise AssertionError("projected original-link network disconnected")
        _score, left_index, right_index, shared = best
        left_tensor, left_labels = factors[left_index]
        right_tensor, right_labels = factors[right_index]
        left_axes = [index for index, label in enumerate(left_labels) if label in shared]
        shared_order = [left_labels[index] for index in left_axes]
        right_axes = [right_labels.index(label) for label in shared_order]
        result = np.tensordot(
            left_tensor, right_tensor, axes=(left_axes, right_axes)
        ) % prime
        result_labels = (
            [label for label in left_labels if label not in shared]
            + [label for label in right_labels if label not in shared]
        )
        for index in sorted((left_index, right_index), reverse=True):
            factors.pop(index)
        factors.append((result, result_labels))
    return factors[0]


def greedy_modular_contract(factors, prime: int) -> int:
    tensor, labels = greedy_modular_tensor(factors, prime)
    if labels or tensor.shape:
        raise AssertionError("projected contraction did not close to a scalar")
    return int(tensor) % prime


def run_probe():
    results = {}
    for prime in PRIMES:
        actual = np.zeros((3, 3), dtype=np.int64)
        census = None
        for left_channel, right_channel in product(range(3), repeat=2):
            factors, current_census = projected_factors(
                left_channel, right_channel, prime
            )
            census = dict(sorted(current_census.items()))
            actual[left_channel, right_channel] = greedy_modular_contract(
                factors, prime
            )
        expected = RAW_RECOUPLING * pow(243, -1, prime) % prime
        o10_k0 = greedy_modular_contract(o10_determinant_cup_factors(prime), prime)
        expected_o10_k0 = 2 * pow(27, -1, prime) % prime
        o10_open, o10_open_labels = greedy_modular_tensor(
            o10_determinant_cup_open_factors(prime)[0], prime
        )
        o10_output_order = o10_determinant_cup_open_factors(prime)[1]
        o10_open = np.transpose(
            o10_open, [o10_open_labels.index(label) for label in o10_output_order]
        )
        expected_o10_open = np.zeros((3,) * 8, dtype=np.int64)
        expected_open_value = expected_o10_k0
        for indices in product(range(3), repeat=8):
            if (
                indices[0] == indices[5]
                and indices[1] == indices[6]
                and indices[2] == indices[7]
                and indices[3] == indices[4]
            ):
                expected_o10_open[indices] = expected_open_value
        o10_open_mismatches = int(np.count_nonzero(o10_open != expected_o10_open))
        crossed_o10_open = np.zeros((3,) * 8, dtype=np.int64)
        for indices in product(range(3), repeat=8):
            if (
                indices[0] == indices[4]
                and indices[1] == indices[6]
                and indices[2] == indices[7]
                and indices[3] == indices[5]
            ):
                crossed_o10_open[indices] = expected_open_value
        results[prime] = {
            "degree_eight_basis_size": len(modular_moment_factors(8, prime)[0]),
            "moment_census": census,
            "actual": actual,
            "expected": expected,
            "o10_k0": o10_k0,
            "expected_o10_k0": expected_o10_k0,
            "o10_open_mismatches": o10_open_mismatches,
            "o10_crossed_mismatches": int(
                np.count_nonzero(o10_open != crossed_o10_open)
            ),
            "o10_open_nonzero": int(np.count_nonzero(o10_open)),
            "placements": parity_placements(),
            "action_survivors": action_irrep_survivors(),
            "scope": authority_and_scope(),
        }
    return results


def checks_for_prime(prime: int, result: dict[str, object], mutation: str | None):
    expected_rank = 91
    expected_census = {2: 9, 4: 4, 6: 4, 8: 4}
    expected_o01 = np.asarray(result["expected"]).copy()
    expected_o10_k0 = int(result["expected_o10_k0"])
    cup_mismatches = int(result["o10_open_mismatches"])
    expected_placements = ((0, 1, -1, -1), (1, 0, -1, -1))
    expected_action = ((VECTOR, VECTOR),)
    scope = bool(result["scope"])

    if mutation == "wrong_rank":
        expected_rank = 90
    elif mutation == "wrong_census":
        expected_census = {2: 9, 4: 4, 6: 5, 8: 3}
    elif mutation == "wrong_o01":
        expected_o01[0, 1] = (int(expected_o01[0, 1]) + 1) % prime
    elif mutation == "wrong_o10_scalar":
        expected_o10_k0 = (expected_o10_k0 + 1) % prime
    elif mutation == "wrong_o10_cup":
        cup_mismatches = int(result["o10_crossed_mismatches"])
    elif mutation == "wrong_parity":
        expected_placements = ((0, 1, 1, 1), (1, 0, 1, 1))
    elif mutation == "wrong_action":
        expected_action = ((VECTOR, (0, 1)),)
    elif mutation == "claim_full_response":
        scope = False

    return (
        ("degree-eight invariant basis has rank 91",
         int(result["degree_eight_basis_size"]) == expected_rank),
        ("nine-trace non-h0 moment census is 9/4/4/4",
         result["moment_census"] == expected_census),
        ("all nine raw K=0 entries equal the recoupling block over 243",
         np.array_equal(result["actual"], expected_o01)),
        ("O10 unnormalized determinant/cup row overlap is 18/243",
         int(result["o10_k0"]) == expected_o10_k0),
        ("O10 projected open endpoint is exactly the p0-A cup and D/E/F identity",
         cup_mismatches == 0 and int(result["o10_open_nonzero"]) == 81),
        ("q4 parity matching leaves only O01 and O10 in cell zero",
         result["placements"] == expected_placements),
        ("the scalar action selector forces a defining-vector insertion on both rails",
         result["action_survivors"] == expected_action),
        ("the note keeps the result finite, support-only, and axiom-neutral",
         scope),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-suite", action="store_true")
    arguments = parser.parse_args()
    print(f"audit_timeout_sec: {AUDIT_TIMEOUT_SEC}")
    results = run_probe()
    if arguments.mutation_suite:
        failed_mutations = 0
        for mutation in MUTATIONS:
            rejected = all(
                any(not passed for _label, passed in checks_for_prime(
                    prime, result, mutation
                ))
                for prime, result in results.items()
            )
            print(f"[{'PASS' if rejected else 'FAIL'}] mutation rejected: {mutation}")
            failed_mutations += int(not rejected)
        print(
            f"MUTATION TOTAL: PASS={len(MUTATIONS) - failed_mutations} "
            f"FAIL={failed_mutations}"
        )
        return int(failed_mutations != 0)

    failures = 0
    for prime, result in results.items():
        checks = checks_for_prime(prime, result, arguments.mutation)
        print(f"prime={prime}")
        print(f"actual={result['actual'].tolist()}")
        print(f"expected={result['expected'].tolist()}")
        print(f"o10_k0={result['o10_k0']} expected_o10_k0={result['expected_o10_k0']}")
        print(
            f"o10_open_mismatches={result['o10_open_mismatches']} "
            f"o10_open_nonzero={result['o10_open_nonzero']}"
        )
        for label, passed in checks:
            print(f"[{'PASS' if passed else 'FAIL'}] {label}")
            failures += int(not passed)
    total = len(PRIMES) * 8
    print(f"TOTAL: PASS={total - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
