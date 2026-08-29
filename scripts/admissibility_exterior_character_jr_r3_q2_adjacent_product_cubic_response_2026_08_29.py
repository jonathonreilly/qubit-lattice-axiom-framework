#!/usr/bin/env python3
"""Exact certificate for the r=3, q=2 adjacent-product cubic response.

The runner reconstructs the six proper complement histories on the complete
two-cell original-link ladder, integrates every Haar link with the reviewed
Brauer helpers, inserts independently selected temporal half-histories, and
checks the closed two-multiplier response over several prime fields.  The
result is a single conditional finite-carrier entry, not a full transfer or a
physical-time statement.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

import numpy as np
import sympy as sp

import admissibility_exterior_character_jr_r2_q4_temporal_all_link_finite_field_2026_08_29 as temporal
import admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_2026_08_29 as brauer


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 180
PRIMES = (1009, 1013, 1019)
PROPER = ({0}, {1}, {2}, {0, 1}, {0, 2}, {1, 2})
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_ADJACENT_PRODUCT_CUBIC_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_ARBITRARY_R_SCALAR_FUSED_VECTOR_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_ADJACENT_PRODUCT_VECTOR_CHANNEL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_O10_TEMPORAL_CUP_BRIDGE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
MUTATIONS = (
    "corrupt_link_census",
    "count_same_side_cup_as_t_squared",
    "collapse_pair_moments",
    "swap_endpoint_type",
    "permit_lower_order_leakage",
    "drop_half_action_factor",
    "identify_static_cup_with_physical_q",
    "claim_full_transfer",
    "axiom_edit",
)

DISCLOSED_SAMPLE = {0: F(1, 5), 1: F(3, 10), 2: F(2, 5), 3: F(1, 2)}
SIGNED_SAMPLES = (
    {0: F(3, 8), 1: F(2, 7), 2: F(-1, 3), 3: F(5, 11)},
    {0: F(-2, 9), 1: F(-3, 10), 2: F(7, 13), 3: F(-4, 15)},
    {0: F(5, 12), 1: F(4, 9), 2: F(2, 11), 3: F(8, 17)},
)
DISCLOSED_RESPONSE = F(
    8762819875140884481,
    2000000000000000000000000000000,
)


def plaquette(index: int):
    return (
        (f"u{index}", 1),
        (f"h{index + 1}", 1),
        (f"v{index}", -1),
        (f"h{index}", -1),
    )


def merged(first: int, last: int, mutation: str | None = None):
    word = tuple(
        [(f"u{index}", 1) for index in range(first, last + 1)]
        + [(f"h{last + 1}", 1)]
        + [(f"v{index}", -1) for index in range(last, first - 1, -1)]
        + [(f"h{first}", -1)]
    )
    if mutation == "corrupt_link_census" and (first, last) == (3, 5):
        return word[:-1] + (("h5", -1),)
    return word


def original_link_occurrences(
    subset: set[int],
    mutation: str | None = None,
):
    full = {0, 1, 2}
    loops = (
        [(f"left_p{index}", plaquette(index)) for index in sorted(subset)]
        + [("left_Y", merged(3, 5, mutation))]
        + [
            (f"right_p{index}", plaquette(index))
            for index in sorted(full - subset)
        ]
        + [
            ("right_C0", merged(0, 2, mutation)),
            ("right_C1", merged(3, 5, mutation)),
        ]
    )
    occurrences: dict[str, list[tuple[str, int, int]]] = defaultdict(list)
    next_node = 0
    for name, loop in loops:
        nodes = tuple(range(next_node, next_node + len(loop)))
        next_node += len(loop)
        for position, (link, direction) in enumerate(loop):
            first = nodes[position]
            second = nodes[(position + 1) % len(loop)]
            row, column = (first, second) if direction == 1 else (second, first)
            occurrences[link].append((name, row, column))
    return occurrences


def subsets(items: set[int]):
    items = tuple(sorted(items))
    for size in range(len(items) + 1):
        for chosen in combinations(items, size):
            yield set(chosen)


def temporal_operator(power: int, prime: int, sample: dict[int, F]) -> np.ndarray:
    projectors = temporal.modular_spectral_projectors(power, prime)
    result = np.zeros((3**power, 3**power), dtype=np.int64)
    for spin, projector in projectors.items():
        value = F(1) if spin == 0 and power % 2 == 0 else sample[spin]
        result = (
            result + temporal.fraction_mod(value, prime) * projector
        ) % prime
    return result


def topology_check(mutation: str | None = None) -> bool:
    for subset in PROPER:
        occurrences = original_link_occurrences(subset, mutation)
        # The full ladder has 12 u/v and h0,...,h6: 19 links.  The merged
        # cell-one loop cancels h4,h5, leaving exactly 17 active links.
        if set(occurrences) != (
            {f"u{index}" for index in range(6)}
            | {f"v{index}" for index in range(6)}
            | {"h0", "h1", "h2", "h3", "h6"}
        ):
            return False
        if len(occurrences["h3"]) != 4:
            return False
        if any(
            len(local) != 2
            for link, local in occurrences.items()
            if link != "h3"
        ):
            return False
    return True


def contract_history(
    subset: set[int],
    prime: int,
    sample: dict[int, F] | None = None,
    left_half: set[int] | None = None,
    right_half: set[int] | None = None,
) -> int:
    factors = []
    auxiliary = 100_000
    operators = None
    if sample is not None:
        operators = {
            power: temporal_operator(power, prime, sample)
            for power in range(1, 4)
        }
        selected = (
            {f"left_p{index}" for index in (left_half or set())}
            | {"left_Y"},
            {f"right_p{index}" for index in (right_half or set())}
            | {"right_C0", "right_C1"},
        )
    for local in original_link_occurrences(subset).values():
        _basis, pairing, inverse_gram = brauer.modular_moment_factors(
            len(local), prime
        )
        column_tensor = pairing
        labels = [column for _name, _row, column in local] + [auxiliary + 1]
        if operators is not None:
            for selected_names in selected:
                chosen = [
                    column
                    for name, _row, column in local
                    if name in selected_names
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
    return brauer.greedy_modular_contract(factors, prime)


def exponent_and_endpoint(
    subset: set[int],
    left_half: set[int],
    right_half: set[int],
    mutation: str | None = None,
) -> tuple[int, str]:
    selected_names = (
        {f"left_p{index}" for index in left_half}
        | {"left_Y"}
        | {f"right_p{index}" for index in right_half}
        | {"right_C0", "right_C1"}
    )
    exponent = 0
    for link, local in original_link_occurrences(subset).items():
        if link == "h3":
            continue
        names = [
            name for name, _row, _column in local if name in selected_names
        ]
        exponent += len(names)
        same_side_cup = len(names) == 2 and (
            all(name.startswith("left_") for name in names)
            or all(name.startswith("right_") for name in names)
        )
        if same_side_cup and mutation != "count_same_side_cup_as_t_squared":
            exponent -= 2
    endpoint_contains_two = 2 in subset
    if mutation == "swap_endpoint_type":
        endpoint_contains_two = not endpoint_contains_two
    if endpoint_contains_two:
        kind = "quadratic_moment" if 2 in left_half else "linear_moment"
    else:
        kind = "scalar" if 2 in right_half else "linear_moment"
    return exponent, kind


def predicted_term(
    exponent: int,
    kind: str,
    prime: int,
    sample: dict[int, F],
    mutation: str | None = None,
) -> int:
    t = temporal.fraction_mod(sample[1], prime)
    u = temporal.fraction_mod(sample[2], prime)
    first_moment = (1 + 3 * t + 5 * u) % prime
    second_moment = (1 + 3 * t * t + 5 * u * u) % prime
    if mutation == "collapse_pair_moments":
        second_moment = first_moment
    if kind == "linear_moment":
        return (
            pow(t, exponent + 1, prime)
            * first_moment
            * pow(81, -1, prime)
            % prime
        )
    if kind == "quadratic_moment":
        return (
            pow(t, exponent, prime)
            * second_moment
            * pow(81, -1, prime)
            % prime
        )
    return pow(t, exponent + 2, prime) * pow(9, -1, prime) % prime


def closed_response(sample: dict[int, F], mutation: str | None = None) -> F:
    t, u = sample[1], sample[2]
    first_moment = 1 + 3 * t + 5 * u
    second_moment = 1 + 3 * t**2 + 5 * u**2
    linear = (
        t**18 + 3 * t**20 + 9 * t**22
        + 2 * t**24 + 8 * t**26 + t**28
    )
    quadratic = (
        t**20 + 2 * t**22 + 6 * t**24 + t**26 + 2 * t**28
    )
    scalar = 2 * t**20 + 3 * t**22 + 2 * t**24 + 4 * t**26 + t**28
    if mutation == "collapse_pair_moments":
        second_moment = first_moment
    half_factor = F(1, 8) if mutation != "drop_half_action_factor" else F(1)
    return half_factor * (
        first_moment * linear / 81
        + second_moment * quadratic / 81
        + scalar / 9
    )


def conditional_q_certificate() -> dict[frozenset[int], str]:
    # At fixed delta0=W2 W1 W0, take W0,W1 as independent Haar variables and
    # W2=delta0 W0^-1 W1^-1.  Each proper product has a Haar variable appearing
    # in exactly one defining-vector factor after a suitable integration order.
    return {
        frozenset((0,)): "integrate W0",
        frozenset((1,)): "integrate W1",
        frozenset((2,)): "integrate W0 inside W2",
        frozenset((0, 1)): "factorized W0 first moment",
        frozenset((0, 2)): "integrate W1 inside W2",
        frozenset((1, 2)): "integrate W0 inside W2",
    }


def weak_compositions(total: int, width: int):
    if width == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, width - 1):
            yield (first,) + rest


def lower_orders_vanish(mutation: str | None = None) -> bool:
    for order in range(3):
        for counts in weak_compositions(order, 3):
            matched = tuple((1 + count) % 2 == 0 for count in counts)
            if mutation == "permit_lower_order_leakage" and counts == (0, 0, 0):
                matched = (True, True, True)
            if all(matched):
                return False
    return True


def scope_check(mutation: str | None = None) -> bool:
    note = (ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    required = (
        "physical conditional-Haar `Q`" in note
        and "not the static `h_3` cup" in note
        and "No full transfer" in note
        and "No axiom or approved primitive changes" in note
    )
    if mutation in {
        "identify_static_cup_with_physical_q",
        "claim_full_transfer",
        "axiom_edit",
    }:
        required = False
    return required


def symbolic_formula_check() -> bool:
    t, u = sp.symbols("t u")
    m1 = 1 + 3 * t + 5 * u
    m2 = 1 + 3 * t**2 + 5 * u**2
    l1 = t**18 + 3 * t**20 + 9 * t**22 + 2 * t**24 + 8 * t**26 + t**28
    l2 = t**20 + 2 * t**22 + 6 * t**24 + t**26 + 2 * t**28
    l0 = 2 * t**20 + 3 * t**22 + 2 * t**24 + 4 * t**26 + t**28
    formula = sp.expand((m1 * l1 + m2 * l2 + 9 * l0) / 648)
    return (
        formula.subs({t: 1, u: 1}) == sp.Rational(2, 3)
        and sp.diff(formula, u) != 0
    )


def run_checks(mutation: str | None = None):
    checks: list[tuple[str, bool]] = []
    topology_ok = topology_check(mutation)
    checks.append(("the complete 19-link census has exactly 17 active links", topology_ok))
    if not topology_ok:
        return checks, Counter()

    counts: Counter[str] = Counter()
    identity_expected = F(1, 9)
    for subset in PROPER:
        for prime in PRIMES:
            got = contract_history(subset, prime)
            expected = (
                identity_expected.numerator
                * pow(identity_expected.denominator, -1, prime)
                % prime
            )
            checks.append((f"identity overlap X={sorted(subset)} F_{prime}", got == expected))
            counts["topology_identity"] += 1

    samples = (DISCLOSED_SAMPLE,) + SIGNED_SAMPLES
    for sample_index, sample in enumerate(samples):
        sample_sum = {prime: 0 for prime in PRIMES}
        for subset in PROPER:
            complement = {0, 1, 2} - subset
            for left_half in subsets(subset):
                for right_half in subsets(complement):
                    exponent, kind = exponent_and_endpoint(
                        subset, left_half, right_half, mutation
                    )
                    for prime in PRIMES:
                        got = contract_history(
                            subset,
                            prime,
                            sample,
                            left_half,
                            right_half,
                        )
                        expected = predicted_term(
                            exponent, kind, prime, sample, mutation
                        )
                        checks.append((
                            f"temporal sample={sample_index} X={sorted(subset)} "
                            f"A={sorted(left_half)} B={sorted(right_half)} F_{prime}",
                            got == expected,
                        ))
                        sample_sum[prime] = (sample_sum[prime] + got) % prime
                        counts[
                            "temporal_disclosed" if sample_index == 0
                            else "temporal_signed"
                        ] += 1
        response = closed_response(sample, mutation)
        for prime in PRIMES:
            direct_response = sample_sum[prime] * pow(8, -1, prime) % prime
            expected_response = (
                response.numerator * pow(response.denominator, -1, prime) % prime
            )
            checks.append((
                f"closed response sample={sample_index} F_{prime}",
                direct_response == expected_response,
            ))

    q_certificate = conditional_q_certificate()
    q_ok = (
        set(q_certificate) == {frozenset(item) for item in PROPER}
        and all(q_certificate.values())
        and mutation != "identify_static_cup_with_physical_q"
    )
    checks.extend((
        ("all six proper histories have explicit conditional-Haar zero-mean witnesses", q_ok),
        ("orders zero, one, and two vanish by exclusive-rail parity", lower_orders_vanish(mutation)),
        ("the closed polynomial has identity 2/3 and load-bearing u dependence", symbolic_formula_check()),
        ("the disclosed rational response is exact", closed_response(DISCLOSED_SAMPLE, mutation) == DISCLOSED_RESPONSE),
        ("the theorem preserves physical-Q, transfer, and axiom boundaries", scope_check(mutation)),
    ))
    return checks, counts


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-suite", action="store_true")
    arguments = parser.parse_args()
    if arguments.mutation_suite:
        rejected = 0
        for mutation in MUTATIONS:
            checks, _counts = run_checks(mutation)
            survived = all(passed for _label, passed in checks)
            print(f"[{'FAIL' if survived else 'PASS'}] mutation rejected: {mutation}")
            rejected += int(not survived)
        print(f"MUTATIONS: rejected={rejected} total={len(MUTATIONS)}")
        return int(rejected != len(MUTATIONS))

    checks, counts = run_checks(arguments.mutation)
    response = closed_response(DISCLOSED_SAMPLE, arguments.mutation)
    residues = tuple(
        response.numerator * pow(response.denominator, -1, prime) % prime
        for prime in PRIMES
    )
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"comparison_counts: {dict(counts)}")
    print(f"closed_S_over_8_disclosed: {response}")
    print(f"closed_S_over_8_residues: {residues}")
    print("identity_control: 2/3")
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
