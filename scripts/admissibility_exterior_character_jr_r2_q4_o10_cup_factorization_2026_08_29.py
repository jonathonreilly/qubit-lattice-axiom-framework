#!/usr/bin/env python3
"""Three-field certificate for the Block242 row-reduced q=4 O10 cup map."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import product
from pathlib import Path

import numpy as np

import admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_2026_08_29 as block240


PRIMES = block240.PRIMES
AUDIT_TIMEOUT_SEC = 180
ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_O10_CUP_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_V4_ALL_SPIN_PERMUTATION_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_V4_JUNCTION_RECOUPLING_EXACT_SUPPORT_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
MUTATIONS = (
    "wrong_column_normalization",
    "cross_column_cup",
    "wrong_kernel_coefficient",
    "wrong_cup_orientation",
    "wrong_hom_dimension",
    "claim_unrestricted_endpoint",
    "claim_full_q4_response",
)


def tensor_power_multiplicities(power: int) -> tuple[int, ...]:
    multiplicities = {0: 1}
    for _ in range(power):
        following: dict[int, int] = {}
        for spin, multiplicity in multiplicities.items():
            for target in range(abs(spin - 1), spin + 2):
                following[target] = following.get(target, 0) + multiplicity
        multiplicities = following
    return tuple(multiplicities.get(spin, 0) for spin in range(power + 1))


def _cup_matrix() -> np.ndarray:
    """Raw C: V^3 -> V^5, with right order (p0,A,D,E,F)."""

    cup = np.zeros((3**5, 3**3), dtype=np.int64)
    for p, d, e, f in product(range(3), repeat=4):
        right = ((((p * 3 + p) * 3 + d) * 3 + e) * 3 + f)
        left = (d * 3 + e) * 3 + f
        cup[right, left] = 1
    return cup


def row_reduced_factors(prime: int, mutation: str | None = None):
    """Integrate non-h0 links and close columns with the declared C/81."""

    occurrences = block240.original_link_occurrences("O10")
    factors = []
    auxiliary = 600_000
    for link, link_occurrences in occurrences.items():
        if link == block240.OPEN_LINK:
            continue
        _basis, pairing_tensor, inverse_gram = block240.modular_moment_factors(
            len(link_occurrences), prime
        )
        factors.extend((
            (pairing_tensor,
             [row for _name, row, _column in link_occurrences] + [auxiliary]),
            (inverse_gram, [auxiliary, auxiliary + 1]),
            (pairing_tensor,
             [column for _name, _row, column in link_occurrences]
             + [auxiliary + 1]),
        ))
        auxiliary += 2

    open_occurrences = occurrences[block240.OPEN_LINK]
    left = [item for item in open_occurrences if item[0].startswith("left_")]
    right = [item for item in open_occurrences if item[0].startswith("right_")]
    if tuple(name for name, _row, _column in left) != (
        "left_D", "left_E", "left_F"
    ):
        raise AssertionError("unexpected left O10 h0 occurrence order")
    if tuple(name for name, _row, _column in right) != (
        "right_p0", "right_A", "right_D", "right_E", "right_F"
    ):
        raise AssertionError("unexpected right O10 h0 occurrence order")

    left_columns = {name: column for name, _row, column in left}
    right_columns = {name: column for name, _row, column in right}
    normalization = pow(81, -1, prime)
    if mutation == "wrong_column_normalization":
        normalization = pow(27, -1, prime)
    delta = np.eye(3, dtype=np.int64)
    normalized_delta = delta * normalization % prime
    pairs = [
        (left_columns["left_D"], right_columns["right_D"]),
        (left_columns["left_E"], right_columns["right_E"]),
        (left_columns["left_F"], right_columns["right_F"]),
        (right_columns["right_p0"], right_columns["right_A"]),
    ]
    if mutation == "cross_column_cup":
        pairs[0] = (left_columns["left_D"], right_columns["right_A"])
        pairs[3] = (right_columns["right_p0"], right_columns["right_D"])
    factors.append((normalized_delta, list(pairs[0])))
    factors.extend((delta, list(pair)) for pair in pairs[1:])
    output_order = [row for _name, row, _column in left + right]
    census = Counter(
        len(link_occurrences)
        for link, link_occurrences in occurrences.items()
        if link != block240.OPEN_LINK
    )
    return factors, output_order, dict(sorted(census.items()))


def expected_kernel(prime: int, mutation: str | None = None) -> np.ndarray:
    coefficient = pow(243, -1, prime)
    if mutation == "wrong_kernel_coefficient":
        coefficient = pow(81, -1, prime)
    tensor = np.zeros((3,) * 8, dtype=np.int64)
    for d, e, f, p in product(range(3), repeat=4):
        if mutation == "wrong_cup_orientation":
            tensor[d, e, f, p, p, e, d, f] = coefficient
        else:
            tensor[d, e, f, p, p, d, e, f] = coefficient
    return tensor


def run_prime(prime: int, mutation: str | None = None) -> dict[str, object]:
    factors, output_order, census = row_reduced_factors(prime, mutation)
    tensor, labels = block240.greedy_modular_tensor(factors, prime)
    tensor = np.transpose(tensor, [labels.index(label) for label in output_order])
    expected = expected_kernel(prime, mutation)
    operator = tensor.reshape(3**3, 3**5) % prime
    cup = _cup_matrix() % prime
    cup_adjoint = cup.T % prime
    cup_gram = cup_adjoint @ cup % prime
    projector = cup @ cup_adjoint % prime * pow(3, -1, prime) % prime
    hom_dimension = sum(
        left * right
        for left, right in zip(
            tensor_power_multiplicities(3), tensor_power_multiplicities(5)
        )
    )
    if mutation == "wrong_hom_dimension":
        hom_dimension = 7
    note = (ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8").lower()
    scope_ok = (
        "row-reduced" in note
        and "not the unrestricted sixteen-index endpoint" in note
        and "no full `q=4` temporal response is claimed" in note
    )
    if mutation in ("claim_unrestricted_endpoint", "claim_full_q4_response"):
        scope_ok = False
    expected_coefficient = pow(243, -1, prime)
    return {
        "shape": tensor.shape,
        "nonzero_entries": int(np.count_nonzero(tensor)),
        "mismatches": int(np.count_nonzero(tensor != expected)),
        "values": tuple(sorted(int(value) for value in np.unique(tensor[tensor != 0]))),
        "expected_value": expected_coefficient,
        "moment_census": census,
        "cup_gram_ok": bool(np.array_equal(cup_gram, 3 * np.eye(27, dtype=np.int64) % prime)),
        "projector_ok": bool(np.array_equal(projector @ projector % prime, projector)),
        "factorization_ok": bool(np.array_equal(operator, cup_adjoint * expected_coefficient % prime)),
        "right_inverse_ok": bool(np.array_equal(operator @ cup % prime, np.eye(27, dtype=np.int64) * pow(81, -1, prime) % prime)),
        "complement_leakage": int(np.count_nonzero(operator @ (np.eye(243, dtype=np.int64) - projector) % prime)),
        "hom_dimension": hom_dimension,
        "scope_ok": scope_ok,
    }


def checks_for_result(result: dict[str, object]):
    return (
        ("original-link moments retain the Block240 2/4/6/8 census",
         result["moment_census"] == {2: 9, 4: 4, 6: 4, 8: 4}),
        ("the row-reduced endpoint has eight vector indices",
         result["shape"] == (3,) * 8),
        ("all 81 cup-support entries have coefficient 1/243",
         result["nonzero_entries"] == 81
         and result["values"] == (result["expected_value"],)
         and result["mismatches"] == 0),
        ("the raw cup obeys C-adjoint C = 3 I and gives a projector",
         result["cup_gram_ok"] and result["projector_ok"]),
        ("the complete reduced operator is C-adjoint/243",
         result["factorization_ok"]),
        ("K C = I/81 and the cup complement has zero leakage",
         result["right_inverse_ok"] and result["complement_leakage"] == 0),
        ("Hom_O(3)(V^5,V^3) has dimension 91",
         result["hom_dimension"] == 91),
        ("the note preserves the endpoint and temporal-response boundary",
         result["scope_ok"]),
    )


def run(mutation: str | None = None):
    results = {prime: run_prime(prime, mutation) for prime in PRIMES}
    checks = tuple(
        (f"F_{prime}: {label}", passed)
        for prime, result in results.items()
        for label, passed in checks_for_result(result)
    )
    return results, checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-suite", action="store_true")
    arguments = parser.parse_args()
    if arguments.mutation_suite:
        rejected = 0
        for mutation in MUTATIONS:
            _results, checks = run(mutation)
            survived = all(passed for _label, passed in checks)
            print(f"[{'FAIL' if survived else 'PASS'}] mutation rejected: {mutation}")
            rejected += int(not survived)
        print(f"MUTATIONS: rejected={rejected} total={len(MUTATIONS)}")
        return int(rejected != len(MUTATIONS))
    results, checks = run(arguments.mutation)
    print(f"audit_timeout_sec: {AUDIT_TIMEOUT_SEC}")
    for prime, result in results.items():
        print(f"F_{prime}: nonzero={result['nonzero_entries']} mismatches={result['mismatches']} complement_leakage={result['complement_leakage']}")
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
