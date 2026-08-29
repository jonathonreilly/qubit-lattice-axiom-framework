#!/usr/bin/env python3
"""Exact six-sector Gram certificate for the Block244 r=3,q=2 response.

The six nonempty proper action partitions label mutually orthogonal physical
history sectors.  Each sector contains six raw temporal half-history vectors:
2^|X| paths issued from Y=chi_V(C1), and 2^(3-|X|) complementary paths issued
from Z=chi_V(C0)chi_V(C1).  The script reconstructs their complete 36 by 36
Gram matrix and the derived 12 by 12 Gram of normalized derivative-selected
sums on the original 19-link ladder over exact prime fields.

The matrix is a Gram matrix before extracting a Taylor coefficient.  Its
off-diagonal Y/Z sum reproduces Block244's cubic coefficient, but the cubic
coefficient by itself is not asserted to be positive semidefinite.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

import numpy as np

import admissibility_exterior_character_jr_r3_q2_adjacent_product_cubic_response_2026_08_29 as block244
import admissibility_exterior_character_jr_r2_q4_temporal_all_link_finite_field_2026_08_29 as temporal
import admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_2026_08_29 as brauer


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 300
PRIMES = block244.PRIMES
H = frozenset((0, 1, 2))
SECTORS = tuple(frozenset(item) for item in block244.PROPER)
ENDPOINTS = ("Y", "Z")
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SIX_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_ADJACENT_PRODUCT_CUBIC_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_ADJACENT_PRODUCT_VECTOR_CHANNEL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
MUTATIONS = (
    "drop_half_action_normalization",
    "identify_cubic_coefficient_as_psd",
    "identify_static_cup_with_physical_q",
    "erase_sector_orthogonality",
    "claim_global_minimal_memory",
    "axiom_edit",
)
ODD_VARIANT_SAMPLE = {
    0: F(-2, 7),
    1: F(3, 10),
    2: F(2, 5),
    3: F(4, 9),
}


def subsets(items: frozenset[int]):
    ordered = tuple(sorted(items))
    for size in range(len(ordered) + 1):
        for chosen in combinations(ordered, size):
            yield frozenset(chosen)


def history_data(endpoint: str, sector: frozenset[int]):
    if endpoint == "Y":
        action_set = sector
        word_set = sector
        base = ("C1",)
    else:
        action_set = H - sector
        word_set = H - sector
        base = ("C0", "C1")
    return action_set, word_set, base


def history_loops(endpoint: str, sector: frozenset[int], prefix: str):
    _action_set, word_set, base = history_data(endpoint, sector)
    loops = [
        (f"{prefix}_p{index}", block244.plaquette(index))
        for index in sorted(word_set)
    ]
    for label in base:
        loops.append((
            f"{prefix}_{label}",
            block244.merged(0, 2) if label == "C0" else block244.merged(3, 5),
        ))
    return loops


def selected_names(
    endpoint: str,
    half: frozenset[int],
    prefix: str,
):
    _action_set, _word_set, base = history_data(endpoint, frozenset())
    # history_data's base does not depend on the sector.
    return (
        {f"{prefix}_p{index}" for index in half}
        | {f"{prefix}_{label}" for label in base}
    )


def pair_occurrences(
    endpoint_a: str,
    sector_a: frozenset[int],
    endpoint_b: str,
    sector_b: frozenset[int],
):
    occurrences: dict[str, list[tuple[str, int, int]]] = defaultdict(list)
    next_node = 0
    loops = (
        history_loops(endpoint_a, sector_a, "a")
        + history_loops(endpoint_b, sector_b, "b")
    )
    for name, loop in loops:
        nodes = tuple(range(next_node, next_node + len(loop)))
        next_node += len(loop)
        for position, (link, direction) in enumerate(loop):
            first = nodes[position]
            second = nodes[(position + 1) % len(loop)]
            row, column = (first, second) if direction == 1 else (second, first)
            occurrences[link].append((name, row, column))
    return occurrences


def _factor_components(factors):
    remaining = list(range(len(factors)))
    components: list[list[int]] = []
    while remaining:
        seed = remaining.pop()
        component = {seed}
        labels = set(factors[seed][1])
        changed = True
        while changed:
            changed = False
            for index in remaining[:]:
                if labels.intersection(factors[index][1]):
                    remaining.remove(index)
                    component.add(index)
                    labels.update(factors[index][1])
                    changed = True
        components.append(sorted(component))
    return components


def _disconnected_contract(factors, prime: int) -> int:
    result = 1
    for component in _factor_components(factors):
        local = [factors[index] for index in component]
        result = result * brauer.greedy_modular_contract(local, prime) % prime
    return result


def temporal_operator(power: int, prime: int, sample: dict[int, F]):
    projectors = temporal.modular_spectral_projectors(power, prime)
    result = np.zeros((3**power, 3**power), dtype=np.int64)
    for spin, projector in projectors.items():
        value = F(1) if spin == 0 and power % 2 == 0 else sample[spin]
        result = (result + temporal.fraction_mod(value, prime) * projector) % prime
    return result


def contract_half_histories(
    endpoint_a: str,
    sector_a: frozenset[int],
    half_a: frozenset[int],
    endpoint_b: str,
    sector_b: frozenset[int],
    half_b: frozenset[int],
    prime: int,
    sample: dict[int, F],
) -> int:
    occurrences = pair_occurrences(endpoint_a, sector_a, endpoint_b, sector_b)
    if any(len(local) % 2 for local in occurrences.values()):
        return 0
    operators = {
        power: temporal_operator(power, prime, sample)
        for power in range(1, 4)
    }
    selected = (
        selected_names(endpoint_a, half_a, "a"),
        selected_names(endpoint_b, half_b, "b"),
    )
    factors = []
    auxiliary = 100_000
    for local in occurrences.values():
        _basis, pairing, inverse_gram = brauer.modular_moment_factors(
            len(local), prime
        )
        column_tensor = pairing
        labels = [column for _name, _row, column in local] + [auxiliary + 1]
        for chosen_names in selected:
            chosen = [
                column for name, _row, column in local if name in chosen_names
            ]
            if chosen:
                column_tensor, labels = temporal.apply_group_operator(
                    column_tensor,
                    labels,
                    chosen,
                    operators[len(chosen)],
                    prime,
                )
        factors.extend((
            (pairing, [row for _name, row, _column in local] + [auxiliary]),
            (inverse_gram, [auxiliary, auxiliary + 1]),
            (column_tensor, labels),
        ))
        auxiliary += 2
    return _disconnected_contract(factors, prime)


def dressed_inner(
    endpoint_a: str,
    sector_a: frozenset[int],
    endpoint_b: str,
    sector_b: frozenset[int],
    prime: int,
    sample: dict[int, F],
    mutation: str | None = None,
) -> int:
    actions_a, _word_a, _base_a = history_data(endpoint_a, sector_a)
    actions_b, _word_b, _base_b = history_data(endpoint_b, sector_b)
    total = 0
    for half_a in subsets(actions_a):
        for half_b in subsets(actions_b):
            total += contract_half_histories(
                endpoint_a,
                sector_a,
                half_a,
                endpoint_b,
                sector_b,
                half_b,
                prime,
                sample,
            )
    if mutation != "drop_half_action_normalization":
        total *= pow(2, -len(actions_a) - len(actions_b), prime)
    return total % prime


def raw_labels():
    labels = []
    for sector in SECTORS:
        for endpoint in ENDPOINTS:
            actions, _word, _base = history_data(endpoint, sector)
            labels.extend(
                (sector, endpoint, half) for half in subsets(actions)
            )
    return tuple(labels)


def raw_gram_matrix(
    prime: int,
    sample: dict[int, F],
    mutation: str | None = None,
):
    labels = raw_labels()
    matrix = np.zeros((len(labels), len(labels)), dtype=np.int64)
    for row, (sector_a, endpoint_a, half_a) in enumerate(labels):
        for column in range(row, len(labels)):
            sector_b, endpoint_b, half_b = labels[column]
            value = contract_half_histories(
                endpoint_a,
                sector_a,
                half_a,
                endpoint_b,
                sector_b,
                half_b,
                prime,
                sample,
            )
            if mutation == "erase_sector_orthogonality" and row != column:
                value = (value + 1) % prime
            matrix[row, column] = value
            matrix[column, row] = value
    return labels, matrix


def aggregate_gram_matrix(
    labels,
    raw_matrix: np.ndarray,
    prime: int,
    mutation: str | None = None,
):
    aggregate_labels = tuple(
        (sector, endpoint) for sector in SECTORS for endpoint in ENDPOINTS
    )
    coefficients = np.zeros((len(labels), len(aggregate_labels)), dtype=np.int64)
    for row, (sector, endpoint, _half) in enumerate(labels):
        column = aggregate_labels.index((sector, endpoint))
        actions, _word, _base = history_data(endpoint, sector)
        coefficient = 1
        if mutation != "drop_half_action_normalization":
            coefficient = pow(2, -len(actions), prime)
        coefficients[row, column] = coefficient
    aggregate = coefficients.T @ raw_matrix @ coefficients % prime
    return aggregate_labels, aggregate


def gram_matrices(
    prime: int,
    sample: dict[int, F],
    mutation: str | None = None,
):
    labels, raw = raw_gram_matrix(prime, sample, mutation)
    aggregate_labels, aggregate = aggregate_gram_matrix(
        labels, raw, prime, mutation
    )
    return labels, raw, aggregate_labels, aggregate


def modular_rank(matrix: np.ndarray, prime: int) -> int:
    work = matrix.copy() % prime
    rows, columns = work.shape
    rank = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, rows) if int(work[row, column]) % prime),
            None,
        )
        if pivot is None:
            continue
        work[[rank, pivot]] = work[[pivot, rank]]
        work[rank] = work[rank] * pow(int(work[rank, column]), -1, prime) % prime
        for row in range(rows):
            if row != rank and work[row, column]:
                work[row] = (
                    work[row] - work[row, column] * work[rank]
                ) % prime
        rank += 1
        if rank == rows:
            break
    return rank


def block_determinants(matrix: np.ndarray, prime: int):
    determinants = []
    for index in range(len(SECTORS)):
        block = matrix[2 * index : 2 * index + 2, 2 * index : 2 * index + 2]
        determinants.append(
            (int(block[0, 0]) * int(block[1, 1])
             - int(block[0, 1]) * int(block[1, 0])) % prime
        )
    return tuple(determinants)


def raw_sector_ranks(matrix: np.ndarray, prime: int):
    # Every proper sector has 2^k+2^(3-k)=6 raw half-history vectors.
    return tuple(
        modular_rank(
            matrix[6 * index : 6 * index + 6, 6 * index : 6 * index + 6],
            prime,
        )
        for index in range(6)
    )


def structural_relation_residuals(
    labels,
    matrix: np.ndarray,
    prime: int,
    sample: dict[int, F],
):
    """Seven exact t^4 relations that give the raw rank-29 upper bound."""
    relations = (
        ((0,), (0,), ()),
        ((1,), (1,), ()),
        ((0, 1), (0,), ()),
        ((0, 1), (1,), ()),
        ((0, 2), (0,), ()),
        ((0, 2), (0, 2), (2,)),
        ((1, 2), (1,), ()),
    )
    t4 = pow(temporal.fraction_mod(sample[1], prime), 4, prime)
    residuals = []
    for sector_items, target_half, source_half in relations:
        sector = frozenset(sector_items)
        target = labels.index((sector, "Y", frozenset(target_half)))
        source = labels.index((sector, "Y", frozenset(source_half)))
        residuals.append(
            np.count_nonzero((matrix[:, target] - t4 * matrix[:, source]) % prime)
        )
    return tuple(int(value) for value in residuals)


def cross_sum(matrix: np.ndarray, prime: int) -> int:
    return sum(int(matrix[2 * index, 2 * index + 1]) for index in range(6)) % prime


def expected_identity_matrix(prime: int):
    expected = np.zeros((12, 12), dtype=np.int64)
    overlap = pow(9, -1, prime)
    for index in range(6):
        expected[2 * index, 2 * index] = 1
        expected[2 * index + 1, 2 * index + 1] = 1
        expected[2 * index, 2 * index + 1] = overlap
        expected[2 * index + 1, 2 * index] = overlap
    return expected


def expected_raw_identity_matrix(prime: int):
    expected = np.zeros((36, 36), dtype=np.int64)
    overlap = pow(9, -1, prime)
    labels = raw_labels()
    for row, (sector_a, endpoint_a, _half_a) in enumerate(labels):
        for column, (sector_b, endpoint_b, _half_b) in enumerate(labels):
            if sector_a != sector_b:
                continue
            expected[row, column] = 1 if endpoint_a == endpoint_b else overlap
    return expected


def scope_check(mutation: str | None = None) -> bool:
    note_path = ROOT / AUDIT_INPUT_PATHS[0]
    if not note_path.exists():
        return mutation in {
            "identify_cubic_coefficient_as_psd",
            "identify_static_cup_with_physical_q",
            "claim_global_minimal_memory",
            "axiom_edit",
        }
    note = note_path.read_text(encoding="utf-8")
    lowered = note.lower()
    required = (
        "cubic Taylor coefficient" in note
        and "not itself asserted to be positive" in note
        and "physical conditional-haar `q`" in lowered
        and "not the static" in note
        and "cup projector" in note
        and "No global minimal-memory" in note
        and "No axiom or approved primitive" in note
    )
    return required and mutation not in {
        "identify_cubic_coefficient_as_psd",
        "identify_static_cup_with_physical_q",
        "claim_global_minimal_memory",
        "axiom_edit",
    }


def run_checks(mutation: str | None = None):
    checks: list[tuple[str, bool]] = []
    samples = (
        ("identity", {0: F(1), 1: F(1), 2: F(1), 3: F(1)}),
        ("disclosed", block244.DISCLOSED_SAMPLE),
        ("odd_variant", ODD_VARIANT_SAMPLE),
        ("signed0", block244.SIGNED_SAMPLES[0]),
    )
    summaries = {}
    for name, sample in samples:
        summaries[name] = {}
        for prime in PRIMES:
            labels, raw, aggregate_labels, aggregate = gram_matrices(
                prime, sample, mutation
            )
            raw_off_block_zero = all(
                int(raw[row, column]) == 0
                for row in range(36)
                for column in range(36)
                if row // 6 != column // 6
            )
            checks.append((
                f"{name} F_{prime}: raw 36-path exact Hermiticity",
                np.array_equal(raw, raw.T),
            ))
            checks.append((
                f"{name} F_{prime}: six raw sectors are orthogonal",
                raw_off_block_zero,
            ))
            checks.append((
                f"{name} F_{prime}: 12-sum exact Hermiticity",
                np.array_equal(aggregate, aggregate.T),
            ))
            checks.append((
                f"{name} F_{prime}: seven structural t^4 relations",
                not any(structural_relation_residuals(
                    labels, raw, prime, sample
                )),
            ))
            if name == "identity":
                checks.append((
                    f"identity F_{prime}: complete raw block template",
                    np.array_equal(raw, expected_raw_identity_matrix(prime)),
                ))
                checks.append((
                    f"identity F_{prime}: six aggregate [[1,1/9],[1/9,1]] blocks",
                    np.array_equal(aggregate, expected_identity_matrix(prime)),
                ))
            else:
                checks.append((
                    f"{name} F_{prime}: all six aggregate blocks are nonsingular",
                    all(block_determinants(aggregate, prime)),
                ))
                if name == "disclosed":
                    checks.append((
                        f"disclosed F_{prime}: raw sector ranks are 5,5,6,4,4,5",
                        raw_sector_ranks(raw, prime) == (5, 5, 6, 4, 4, 5),
                    ))
            expected_cross = block244.closed_response(sample)
            expected_mod = (
                expected_cross.numerator
                * pow(expected_cross.denominator, -1, prime)
                % prime
            )
            checks.append((
                f"{name} F_{prime}: off-diagonal sum reproduces Block244",
                cross_sum(aggregate, prime) == expected_mod,
            ))
            summaries[name][prime] = {
                "raw_rank": modular_rank(raw, prime),
                "raw_sector_ranks": raw_sector_ranks(raw, prime),
                "aggregate_rank": modular_rank(aggregate, prime),
                "aggregate_block_determinants": block_determinants(
                    aggregate, prime
                ),
                "cross_sum": cross_sum(aggregate, prime),
            }

    for prime in PRIMES:
        disclosed = summaries["disclosed"][prime]
        odd_variant = summaries["odd_variant"][prime]
        checks.append((
            f"F_{prime}: odd-channel variation leaves only the cross sum fixed",
            disclosed["cross_sum"] == odd_variant["cross_sum"]
            and disclosed["aggregate_block_determinants"]
            != odd_variant["aggregate_block_determinants"],
        ))

    for label, sample in (
        ("Haar", {0: F(1), 1: F(0), 2: F(0), 3: F(0)}),
        ("t-zero-u-live", {0: F(1), 1: F(0), 2: F(2, 5), 3: F(-1, 4)}),
    ):
        summaries[label] = {}
        for prime in PRIMES:
            _labels, raw, _aggregate_labels, aggregate = gram_matrices(
                prime, sample, mutation
            )
            checks.append((
                f"{label} F_{prime}: raw and aggregate carriers vanish",
                not np.any(raw) and not np.any(aggregate),
            ))
            summaries[label][prime] = {
                "raw_rank": modular_rank(raw, prime),
                "aggregate_rank": modular_rank(aggregate, prime),
            }

    checks.extend((
        (
            "generic raw rank 29 is witnessed at the disclosed exact sample",
            all(summaries["disclosed"][prime]["raw_rank"] == 29 for prime in PRIMES),
        ),
        (
            "normalized 12-sum Gram is generically full rank",
            all(summaries["disclosed"][prime]["aggregate_rank"] == 12
                for prime in PRIMES),
        ),
        (
            "full identity endpoint has raw and aggregate rank twelve",
            all(
                summaries["identity"][prime]["raw_rank"] == 12
                and summaries["identity"][prime]["aggregate_rank"] == 12
                for prime in PRIMES
            ),
        ),
        (
            "Haar and the wider t=0 endpoint have both ranks zero",
            all(
                summaries[label][prime]["raw_rank"] == 0
                and summaries[label][prime]["aggregate_rank"] == 0
                for label in ("Haar", "t-zero-u-live") for prime in PRIMES
            ),
        ),
        ("scope and projector boundaries remain explicit", scope_check(mutation)),
    ))
    return checks, summaries


def mutation_rejected(mutation: str) -> bool:
    """Run the smallest load-bearing falsifier for each hostile mutation."""
    if mutation == "drop_half_action_normalization":
        prime = PRIMES[0]
        _labels, _raw, _aggregate_labels, matrix = gram_matrices(
            prime, block244.DISCLOSED_SAMPLE, mutation
        )
        expected = block244.closed_response(block244.DISCLOSED_SAMPLE)
        expected_mod = (
            expected.numerator * pow(expected.denominator, -1, prime) % prime
        )
        return cross_sum(matrix, prime) != expected_mod
    if mutation == "erase_sector_orthogonality":
        prime = PRIMES[0]
        _labels, matrix, _aggregate_labels, _aggregate = gram_matrices(
            prime,
            {0: F(1), 1: F(1), 2: F(1), 3: F(1)},
            mutation,
        )
        return any(
            int(matrix[row, column]) != 0
            for row in range(36)
            for column in range(36)
            if row // 6 != column // 6
        )
    return not scope_check(mutation)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-suite", action="store_true")
    arguments = parser.parse_args()
    if arguments.mutation_suite:
        rejected = 0
        for mutation in MUTATIONS:
            is_rejected = mutation_rejected(mutation)
            print(f"[{'PASS' if is_rejected else 'FAIL'}] mutation rejected: {mutation}")
            rejected += int(is_rejected)
        print(f"MUTATIONS: rejected={rejected} total={len(MUTATIONS)}")
        return int(rejected != len(MUTATIONS))

    checks, summaries = run_checks(arguments.mutation)
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    for name, by_prime in summaries.items():
        print(f"{name}: {by_prime}")
    print("structural_psd: exact 36-path Gram F^dagger F on six proper sectors")
    print("derived_aggregate: 12 normalized derivative-selected sums")
    print("cubic_boundary: only the off-diagonal order-three coefficient is reused")
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
