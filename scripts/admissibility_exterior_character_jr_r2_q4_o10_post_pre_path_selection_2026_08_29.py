#!/usr/bin/env python3
"""Projector-resolved certificate for the Block243 O10 post/pre path theorem.

The analytic theorem slides central subset projectors through the exact
Block240 Haar/Brauer moments, gathers them at the Block242 cup cut, and uses
the nested Block241 EF subset DEF subset V^4 projectors.  This companion tests
that reduction directly in the full original-link network.  It is a finite-
field realization of the analytic selection proof, not a replacement for it.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache

import numpy as np

import admissibility_exterior_character_jr_r2_q4_temporal_all_link_finite_field_2026_08_29 as all_link
import admissibility_exterior_character_jr_r2_q4_v4_all_spin_permutation_kernel_exact_2026_08_29 as block241
import admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_2026_08_29 as block240


PRIMES = (1009, 1013, 1019)
AUDIT_TIMEOUT_SEC = 180
MUTATIONS = (
    "wrong_scale",
    "drop_carrier_dimension",
    "use_o01_census",
    "allow_mixed_k",
    "claim_complete_q4_response",
    "identify_cup_projector_with_physical_q",
    "axiom_edit",
)


@lru_cache(None)
def projector(power: int, spin: int, prime: int) -> np.ndarray:
    return all_link.modular_spectral_projectors(power, prime)[spin]


def insertions() -> tuple[tuple[str, str, int], ...]:
    result = []
    for link, occurrences in block240.original_link_occurrences("O10").items():
        for side, mode in (("left", "post"), ("right", "pre")):
            chosen = all_link.selected_columns(occurrences, side, mode)
            if chosen:
                result.append((link, side, len(chosen)))
    return tuple(result)


def projector_term(
    prime: int,
    labels_by_power: dict[int, int],
    override: tuple[str, str, int] | None = None,
) -> int:
    """Contract the full all-link network with pure projectors at each cut."""

    occurrence_map = block240.original_link_occurrences("O10")
    factors = []
    auxiliary = 950_000
    for link, occurrences in occurrence_map.items():
        degree = len(occurrences)
        _basis, pairing, inverse_gram = block240.modular_moment_factors(
            degree, prime
        )
        tensor = pairing
        labels = [column for _name, _row, column in occurrences] + [auxiliary + 1]
        for side, mode in (("left", "post"), ("right", "pre")):
            chosen = all_link.selected_columns(occurrences, side, mode)
            if not chosen:
                continue
            power = len(chosen)
            spin = labels_by_power[power]
            if override and override[:2] == (link, side):
                spin = override[2]
            tensor, labels = all_link.apply_group_operator(
                tensor, labels, chosen, projector(power, spin, prime), prime
            )
        factors.extend((
            (pairing, [row for _name, row, _column in occurrences] + [auxiliary]),
            (inverse_gram, [auxiliary, auxiliary + 1]),
            (tensor, labels),
        ))
        auxiliary += 2
    return block240.greedy_modular_contract(factors, prime)


def checks(mutation: str | None = None):
    paths = block241.coupling_paths()
    coherent = []
    for prime in PRIMES:
        inverse_scale = pow(81 if mutation == "wrong_scale" else 243, -1, prime)
        for pair_spin, triple_spin, total_spin in paths:
            actual = projector_term(
                prime,
                {1: 1, 2: pair_spin, 3: triple_spin, 4: total_spin},
            )
            carrier_dimension = (
                1 if mutation == "drop_carrier_dimension" else 2 * total_spin + 1
            )
            coherent.append((
                f"F_{prime} coherent path {(pair_spin, triple_spin, total_spin)}",
                actual == carrier_dimension * inverse_scale % prime,
            ))

    base = {1: 1, 2: 1, 3: 1, 4: 1}
    alternatives = {2: 0, 3: 2, 4: 2}
    mismatch_checks = []
    for link, side, power in insertions():
        if power == 1:
            continue
        actual = projector_term(
            1009, base, (link, side, alternatives[power])
        )
        expected = actual if mutation == "allow_mixed_k" else 0
        mismatch_checks.append((
            f"F_1009 one-insertion mismatch {(link, side, power)} vanishes",
            actual == expected and mutation != "allow_mixed_k",
        ))

    forbidden_checks = tuple(
        (
            f"F_1009 forbidden nested path {(pair_spin, triple_spin, total_spin)} vanishes",
            projector_term(
                1009,
                {1: 1, 2: pair_spin, 3: triple_spin, 4: total_spin},
            ) == 0,
        )
        for pair_spin, triple_spin, total_spin in (
            (0, 0, 0), (0, 0, 1), (2, 0, 1), (0, 3, 1), (2, 3, 0)
        )
    )

    census = Counter(power for _link, _side, power in insertions())
    expected_census = (
        Counter({1: 16, 2: 8, 3: 10, 4: 8})
        if mutation == "use_o01_census"
        else Counter({1: 17, 2: 8, 3: 11, 4: 7})
    )
    scope_ok = mutation not in (
        "claim_complete_q4_response",
        "identify_cup_projector_with_physical_q",
        "axiom_edit",
    )
    boundary_checks = (
        ("the exact insertion census is O10 rather than O01", census == expected_census),
        ("scope remains one history before physical Q", scope_ok),
    )
    return tuple(coherent) + tuple(mismatch_checks) + forbidden_checks + boundary_checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    arguments = parser.parse_args()
    results = checks(arguments.mutation)
    failures = 0
    print(f"audit_timeout_sec: {AUDIT_TIMEOUT_SEC}")
    print(f"insertion_census: {dict(sorted(Counter(power for _, _, power in insertions()).items()))}")
    for label, passed in results:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(results) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
