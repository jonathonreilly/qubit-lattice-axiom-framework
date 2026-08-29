#!/usr/bin/env python3
"""Factored-Brauer finite-field certificate for all eight q=4 Gram terms.

This companion inserts the supplied temporal operators before contracting the
complete Block240 original-link networks.  It checks all eight terms at the
disclosed Block240 sample and checks the Block241-inspired O10 post/pre path
candidate at eight rational samples over three primes.  These inputs are audit
dependencies, not independently rederived geometry.  The finite-field checks
do not turn the candidate into a symbolic response theorem or identify the cup
projector with physical Q.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache

import numpy as np

import admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_2026_08_29 as block240


PRIMES = (1009, 1013, 1019)
AUDIT_TIMEOUT_SEC = 180
SAMPLE = {
    0: {"odd": F(1, 5), "even": F(1)},
    1: F(3, 10),
    2: F(2, 5),
    3: F(1, 2),
    4: F(3, 5),
    5: F(7, 10),
}
SECOND_SAMPLE = {
    0: F(3, 8),
    1: F(2, 7),
    2: F(-1, 3),
    3: F(5, 11),
    4: F(7, 13),
    5: F(4, 9),
}
EXTRA_SAMPLES = (
    {0: F(2, 3), 1: F(3, 7), 2: F(5, 8), 3: F(7, 9), 4: F(11, 13), 5: F(4, 5)},
    {0: F(-1, 4), 1: F(5, 6), 2: F(2, 9), 3: F(-3, 10), 4: F(8, 11), 5: F(6, 7)},
    {0: F(4, 9), 1: F(-2, 5), 2: F(7, 12), 3: F(1, 8), 4: F(-5, 14), 5: F(9, 10)},
    {0: F(5, 11), 1: F(1, 3), 2: F(4, 7), 3: F(6, 13), 4: F(2, 15), 5: F(7, 16)},
    {0: F(7, 10), 1: F(9, 17), 2: F(-4, 13), 3: F(3, 11), 4: F(5, 19), 5: F(8, 21)},
    {0: F(3, 5), 1: F(7, 18), 2: F(11, 20), 3: F(-2, 7), 4: F(13, 22), 5: F(5, 12)},
)
EXPECTED = {
    1009: {
        "O01": {("pre", "pre"): 284, ("pre", "post"): 317,
                ("post", "pre"): 297, ("post", "post"): 216},
        "O10": {("pre", "pre"): 284, ("pre", "post"): 634,
                ("post", "pre"): 616, ("post", "post"): 707},
    },
    1013: {
        "O01": {("pre", "pre"): 534, ("pre", "post"): 569,
                ("post", "pre"): 983, ("post", "post"): 648},
        "O10": {("pre", "pre"): 534, ("pre", "post"): 372,
                ("post", "pre"): 332, ("post", "post"): 711},
    },
    1019: {
        "O01": {("pre", "pre"): 321, ("pre", "post"): 927,
                ("post", "pre"): 951, ("post", "post"): 380},
        "O10": {("pre", "pre"): 321, ("pre", "post"): 501,
                ("post", "pre"): 310, ("post", "post"): 98},
    },
}
MUTATIONS = (
    "include_action_in_pre",
    "identify_o10_with_o01",
    "claim_symbolic_response",
    "identify_cup_projector_with_physical_q",
    "axiom_edit",
)


def _kron_all(factors: tuple[np.ndarray, ...]) -> np.ndarray:
    result = np.array([[1]], dtype=np.int64)
    for factor in factors:
        result = np.kron(result, factor)
    return result


@lru_cache(None)
def integer_total_casimir(power: int) -> np.ndarray:
    identity = np.eye(3, dtype=np.int64)
    generators = (
        np.array(((0, 0, 0), (0, 0, 1), (0, -1, 0)), dtype=np.int64),
        np.array(((0, 0, -1), (0, 0, 0), (1, 0, 0)), dtype=np.int64),
        np.array(((0, 1, 0), (-1, 0, 0), (0, 0, 0)), dtype=np.int64),
    )
    dimension = 3**power
    casimir = 2 * power * np.eye(dimension, dtype=np.int64)
    for left in range(power):
        for right in range(left + 1, power):
            for generator in generators:
                factors = tuple(
                    generator if position in (left, right) else identity
                    for position in range(power)
                )
                casimir -= 2 * _kron_all(factors)
    return casimir


def fraction_mod(value: F, prime: int) -> int:
    return value.numerator * pow(value.denominator, -1, prime) % prime


@lru_cache(None)
def modular_spectral_projectors(power: int, prime: int) -> dict[int, np.ndarray]:
    dimension = 3**power
    identity = np.eye(dimension, dtype=np.int64)
    casimir = integer_total_casimir(power) % prime
    spins = (1,) if power == 1 else tuple(range(power + 1))
    projectors: dict[int, np.ndarray] = {}
    for spin in spins:
        eigenvalue = spin * (spin + 1)
        projector = identity.copy()
        denominator = 1
        for other in spins:
            if other == spin:
                continue
            other_eigenvalue = other * (other + 1)
            projector = (
                projector @ ((casimir - other_eigenvalue * identity) % prime)
            ) % prime
            denominator = denominator * (eigenvalue - other_eigenvalue) % prime
        projectors[spin] = projector * pow(denominator, -1, prime) % prime
    return projectors


def modular_temporal_operator(
    power: int,
    prime: int,
    mutation: str | None = None,
) -> np.ndarray:
    projectors = modular_spectral_projectors(power, prime)
    result = np.zeros((3**power, 3**power), dtype=np.int64)
    for spin, projector in projectors.items():
        if spin == 0:
            value = SAMPLE[0]["odd" if power % 2 else "even"]
        else:
            value = SAMPLE[spin]
        result = (result + fraction_mod(value, prime) * projector) % prime
    return result


def selected_columns(
    occurrences: list[tuple[str, int, int]],
    side: str,
    mode: str,
    mutation: str | None = None,
) -> list[int]:
    result = []
    for name, _row, column in occurrences:
        if not name.startswith(f"{side}_"):
            continue
        is_action = name.startswith(f"{side}_p")
        include = mode == "post" or not is_action
        if mutation == "include_action_in_pre":
            include = True
        if include:
            result.append(column)
    return result


def apply_group_operator(
    tensor: np.ndarray,
    labels: list[int],
    chosen: list[int],
    operator: np.ndarray,
    prime: int,
) -> tuple[np.ndarray, list[int]]:
    axes = [labels.index(label) for label in chosen]
    power = len(chosen)
    transformed = np.tensordot(
        tensor,
        operator.reshape((3,) * (2 * power)),
        axes=(axes, tuple(range(power))),
    ) % prime
    remaining = [label for index, label in enumerate(labels) if index not in axes]
    return transformed, remaining + chosen


def gram_term(
    orientation: str,
    modes: tuple[str, str],
    prime: int,
    mutation: str | None = None,
) -> int:
    occurrences = block240.original_link_occurrences(orientation)
    factors: list[tuple[np.ndarray, list[int]]] = []
    auxiliary = 700_000
    operators = {
        power: modular_temporal_operator(power, prime, mutation)
        for power in range(1, 6)
    }
    for link_occurrences in occurrences.values():
        degree = len(link_occurrences)
        _basis, pairing, inverse_gram = block240.modular_moment_factors(
            degree, prime
        )
        row_auxiliary, column_auxiliary = auxiliary, auxiliary + 1
        auxiliary += 2
        row_labels = [row for _name, row, _column in link_occurrences]
        column_labels = [column for _name, _row, column in link_occurrences]
        column_tensor = pairing
        labels = column_labels + [column_auxiliary]
        for side, mode in (("left", modes[0]), ("right", modes[1])):
            chosen = selected_columns(link_occurrences, side, mode, mutation)
            if chosen:
                column_tensor, labels = apply_group_operator(
                    column_tensor, labels, chosen, operators[len(chosen)], prime
                )
        factors.extend((
            (pairing, row_labels + [row_auxiliary]),
            (inverse_gram, [row_auxiliary, column_auxiliary]),
            (column_tensor, labels),
        ))
    return block240.greedy_modular_contract(factors, prime)


def selected_power_census(
    orientation: str,
    modes: tuple[str, str],
) -> Counter[int]:
    census: Counter[int] = Counter()
    for occurrences in block240.original_link_occurrences(orientation).values():
        for side, mode in (("left", modes[0]), ("right", modes[1])):
            chosen = selected_columns(occurrences, side, mode)
            if chosen:
                census[len(chosen)] += 1
    return census


def o10_path_formula(modes: tuple[str, str], sample: dict[int, F]) -> F:
    """Evaluate the projector-transport O10 formula for one history."""

    d, t, u, v, w = (sample[index] for index in range(5))
    x = (F(1), t, u)
    y = (d, t, u, v)
    z = (F(1), t, u, v, w)
    census = selected_power_census("O10", modes)
    return sum((
        F(2 * total_spin + 1, 243)
        * t**census[1]
        * x[pair_spin]**census[2]
        * y[triple_spin]**(census[3] + census[5])
        * z[total_spin]**census[4]
        for pair_spin in range(3)
        for triple_spin in range(abs(pair_spin - 1), pair_spin + 2)
        for total_spin in range(abs(triple_spin - 1), triple_spin + 2)
    ), F(0))


def o01_path_formula(modes: tuple[str, str], sample: dict[int, F]) -> F:
    """Evaluate the role-resolved O01 formula for one history.

    When the right insertion is post-action, its extra degree-two cut is the
    p1-A scalar and has multiplier one.  Its two degree-five cuts reduce
    through that scalar pair to the DEF total-spin label, adding two y_J
    powers rather than an independent r5 multiplier.
    """

    d, t, u, v, w = (sample[index] for index in range(5))
    x = (F(1), t, u)
    y = (d, t, u, v)
    z = (F(1), t, u, v, w)
    census = selected_power_census("O01", modes)
    action_pair_count = int(modes[1] == "post")
    return sum((
        F(2 * total_spin + 1, 243)
        * t**census[1]
        * x[pair_spin]**(census[2] - action_pair_count)
        * y[triple_spin]**(census[3] + census[5])
        * z[total_spin]**census[4]
        for pair_spin in range(3)
        for triple_spin in range(abs(pair_spin - 1), pair_spin + 2)
        for total_spin in range(abs(triple_spin - 1), triple_spin + 2)
    ), F(0))


def path_formula(
    orientation: str,
    modes: tuple[str, str],
    sample: dict[int, F],
) -> F:
    return (
        o01_path_formula(modes, sample)
        if orientation == "O01"
        else o10_path_formula(modes, sample)
    )


def _current_sample() -> dict[int, F]:
    return {
        0: SAMPLE[0]["odd"],
        **{spin: SAMPLE[spin] for spin in range(1, 6)},
    }


def _set_sample(sample: dict[int, F]) -> None:
    SAMPLE[0]["odd"] = sample[0]
    for spin in range(1, 6):
        SAMPLE[spin] = sample[spin]


def run(mutation: str | None = None):
    original_sample = _current_sample()
    actual: dict[int, dict[str, dict[tuple[str, str], int]]] = {}
    modes = (("pre", "pre"), ("pre", "post"),
             ("post", "pre"), ("post", "post"))
    for prime in PRIMES:
        actual[prime] = {}
        for orientation in ("O01", "O10"):
            actual[prime][orientation] = {
                mode: gram_term(orientation, mode, prime, mutation)
                for mode in modes
            }
    expected = EXPECTED
    if mutation == "identify_o10_with_o01":
        expected = {
            prime: {"O01": values["O01"], "O10": values["O01"]}
            for prime, values in EXPECTED.items()
        }
    scope_ok = mutation not in (
        "claim_symbolic_response",
        "identify_cup_projector_with_physical_q",
        "axiom_edit",
    )
    checks = tuple(
        (f"F_{prime} {orientation} {mode[0]}/{mode[1]}",
         actual[prime][orientation][mode] == expected[prime][orientation][mode])
        for prime in PRIMES
        for orientation in ("O01", "O10")
        for mode in modes
    )

    formula_by_orientation_mode = {
        (orientation, mode): path_formula(orientation, mode, original_sample)
        for orientation in ("O01", "O10")
        for mode in modes
    }
    formula_checks = tuple(
        (f"F_{prime} corrected {orientation} {mode[0]}/{mode[1]} 19-path formula",
         actual[prime][orientation][mode]
         == fraction_mod(formula_by_orientation_mode[(orientation, mode)], prime))
        for prime in PRIMES
        for orientation in ("O01", "O10")
        for mode in modes
    )

    _set_sample(SECOND_SAMPLE)
    second_formula_by_orientation_mode = {
        (orientation, mode): path_formula(orientation, mode, SECOND_SAMPLE)
        for orientation in ("O01", "O10")
        for mode in modes
    }
    second_checks = tuple(
        (f"F_{prime} independent second-sample {orientation} {mode[0]}/{mode[1]} formula",
         gram_term(orientation, mode, prime, mutation)
         == fraction_mod(second_formula_by_orientation_mode[(orientation, mode)], prime))
        for prime in PRIMES
        for orientation in ("O01", "O10")
        for mode in modes
    )

    extra_checks = []
    for sample_index, extra_sample in enumerate(EXTRA_SAMPLES, start=3):
        _set_sample(extra_sample)
        extra_formula_by_orientation_mode = {
            (orientation, mode): path_formula(orientation, mode, extra_sample)
            for orientation in ("O01", "O10")
            for mode in modes
        }
        for prime in PRIMES:
            for orientation in ("O01", "O10"):
                for mode in modes:
                    extra_checks.append((
                        f"F_{prime} rational sample {sample_index} {orientation} {mode[0]}/{mode[1]} formula",
                        gram_term(orientation, mode, prime, mutation)
                        == fraction_mod(
                            extra_formula_by_orientation_mode[(orientation, mode)],
                            prime,
                        ),
                    ))

    identity_sample = {spin: F(1) for spin in range(6)}
    _set_sample(identity_sample)
    identity_checks = tuple(
        (f"F_{prime} identity-limit {orientation} {mode[0]}/{mode[1]} normalization",
         gram_term(orientation, mode, prime, mutation)
         == pow(3, -1, prime))
        for prime in PRIMES
        for orientation in ("O01", "O10")
        for mode in modes
    )
    _set_sample(original_sample)

    census_checks = (
        ("the exact O10 pre/pre census is t^15 x^8 y^13 z^5",
         selected_power_census("O10", ("pre", "pre"))
         == Counter({1: 15, 2: 8, 3: 13, 4: 5})),
        ("the raw O10 pre/post census is t^16 x^8 y^13 z^2 degree5^3",
         selected_power_census("O10", ("pre", "post"))
         == Counter({1: 16, 2: 8, 3: 13, 4: 2, 5: 3})),
        ("the exact O10 post/pre census is t^17 x^8 y^11 z^7",
         selected_power_census("O10", ("post", "pre"))
         == Counter({1: 17, 2: 8, 3: 11, 4: 7})),
        ("the raw O10 post/post census is t^18 x^8 y^11 z^4 degree5^3",
         selected_power_census("O10", ("post", "post"))
         == Counter({1: 18, 2: 8, 3: 11, 4: 4, 5: 3})),
        ("the previous O01 assignment is t^16 x^8 y^10 z^8",
         selected_power_census("O01", ("post", "pre"))
         == Counter({1: 16, 2: 8, 3: 10, 4: 8})),
        ("the O01 right-post action adds one scalar pair and two five-strand cuts",
         selected_power_census("O01", ("pre", "post"))
         == Counter({1: 15, 2: 9, 3: 13, 4: 3, 5: 2})
         and selected_power_census("O01", ("post", "post"))
         == Counter({1: 16, 2: 9, 3: 10, 4: 6, 5: 2})),
        ("scope remains an eight-term pre-Q finite-field certificate", scope_ok),
    )
    checks = (
        checks + formula_checks + second_checks + tuple(extra_checks)
        + identity_checks + census_checks
    )
    return actual, checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    arguments = parser.parse_args()
    actual, checks = run(arguments.mutation)
    print(f"audit_timeout_sec: {AUDIT_TIMEOUT_SEC}")
    for prime in PRIMES:
        for orientation in ("O01", "O10"):
            values = actual[prime][orientation]
            print(f"F_{prime} {orientation}: {values}")
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks)-failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
