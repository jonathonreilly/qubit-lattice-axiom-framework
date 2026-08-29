#!/usr/bin/env python3
"""Finite-field certificate for the Block241 all-spin q=4 O01 kernel.

The nine supplied original-link traces are rebuilt from the Block240 geometry.
Every non-h0 link is integrated in an independent Brauer basis.  The four
column pairs at h0 are then closed with the declared normalized identity I/3,
while all eight row indices remain open.  This is only the row-reduced O01
kernel; it is not the complete sixteen-index endpoint tensor or the full q=4
temporal response.
"""

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
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_V4_ALL_SPIN_PERMUTATION_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_V4_JUNCTION_RECOUPLING_EXACT_SUPPORT_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_SEVEN_CHANNEL_TEMPORAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
MUTATIONS = (
    "wrong_column_normalization",
    "cross_column_pairing",
    "wrong_kernel_coefficient",
    "drop_degree_eight_rank",
    "claim_unprojected_endpoint",
    "claim_full_q4_response",
)


def row_reduced_factors(prime: int, mutation: str | None = None):
    """Return exact-mod-p factors and the physical row order."""

    occurrences = block240.original_link_occurrences("O01")
    factors = []
    auxiliary = 500_000
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
        "left_p0", "left_D", "left_E", "left_F"
    ):
        raise AssertionError("unexpected left h0 occurrence order")
    if tuple(name for name, _row, _column in right) != (
        "right_A", "right_D", "right_E", "right_F"
    ):
        raise AssertionError("unexpected right h0 occurrence order")

    normalization = pow(3, -1, prime)
    if mutation == "wrong_column_normalization":
        normalization = 1
    normalized_delta = np.eye(3, dtype=np.int64) * normalization % prime
    paired_right = list(right)
    if mutation == "cross_column_pairing":
        paired_right[0], paired_right[1] = paired_right[1], paired_right[0]
    for left_occurrence, right_occurrence in zip(left, paired_right):
        factors.append((normalized_delta, [left_occurrence[2], right_occurrence[2]]))

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
    for a, b, c, d in product(range(3), repeat=4):
        tensor[a, b, c, d, a, b, c, d] = coefficient
    return tensor


def run_prime(prime: int, mutation: str | None = None) -> dict[str, object]:
    factors, output_order, census = row_reduced_factors(prime, mutation)
    tensor, labels = block240.greedy_modular_tensor(factors, prime)
    tensor = np.transpose(tensor, [labels.index(label) for label in output_order])
    expected = expected_kernel(prime, mutation)
    actual_values = tuple(sorted(int(value) for value in np.unique(tensor[tensor != 0])))
    note = (ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8").lower()
    if mutation == "drop_degree_eight_rank":
        degree_eight_rank = 90
    else:
        degree_eight_rank = len(block240.modular_moment_factors(8, prime)[0])
    scope_ok = (
        "row-reduced" in note
        and "not the complete sixteen-index" in note
        and "no full `q=4` temporal response is claimed" in note
    )
    if mutation == "claim_unprojected_endpoint":
        scope_ok = False
    if mutation == "claim_full_q4_response":
        scope_ok = False
    return {
        "prime": prime,
        "shape": tensor.shape,
        "nonzero_entries": int(np.count_nonzero(tensor)),
        "mismatches": int(np.count_nonzero(tensor != expected)),
        "values": actual_values,
        "expected_value": pow(243, -1, prime),
        "moment_census": census,
        "degree_eight_rank": degree_eight_rank,
        "scope_ok": scope_ok,
    }


def checks_for_result(result: dict[str, object]):
    return (
        ("original-link moments retain the Block240 2/4/6/8 census",
         result["moment_census"] == {2: 9, 4: 4, 6: 4, 8: 4}),
        ("the degree-eight Brauer image has exact rank 91",
         result["degree_eight_rank"] == 91),
        ("the row-reduced endpoint has eight vector indices",
         result["shape"] == (3,) * 8),
        ("exactly 81 identity-support entries survive",
         result["nonzero_entries"] == 81),
        ("all surviving entries have coefficient 1/243",
         result["values"] == (result["expected_value"],)),
        ("the full finite-field tensor equals identity support over V^4",
         result["mismatches"] == 0),
        ("the note preserves the row-reduced and incomplete-response boundary",
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
        print(
            f"F_{prime}: shape={result['shape']} nonzero={result['nonzero_entries']} "
            f"coefficient={result['values']} mismatches={result['mismatches']}"
        )
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
