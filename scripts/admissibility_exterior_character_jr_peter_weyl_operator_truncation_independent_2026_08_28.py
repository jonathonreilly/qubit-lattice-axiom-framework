#!/usr/bin/env python3
"""Independent exact controls for the physical-transfer truncation theorem.

This helper uses only Python integers, Fraction, finite enumeration, and
elementary polynomial arithmetic.  It does not import the primary runner,
SymPy, NumPy, or a campaign scratch calculation.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product
from math import factorial


AUDIT_TIMEOUT_SEC = 120
G = (1, -1)
PAIRS = tuple(product(G, repeat=2))
STATES = tuple(product(G, repeat=4))


def determinant3(matrix: tuple[tuple[int, ...], ...]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def trace3(matrix: tuple[tuple[int, ...], ...]) -> int:
    return sum(matrix[i][i] for i in range(3))


def multiply3(
    left: tuple[tuple[int, ...], ...], right: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def signed_permutation_frames() -> tuple[tuple[tuple[int, ...], ...], ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product(G, repeat=3):
            matrix = [[0 for _ in range(3)] for _ in range(3)]
            for row, column in enumerate(permutation):
                matrix[row][column] = signs[row]
            frames.append(tuple(tuple(row) for row in matrix))
    return tuple(frames)


def exterior_facts() -> dict[str, object]:
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    frames = signed_permutation_frames()
    values = set()
    exterior_identity = True
    member_identity = True
    proper = improper = 0
    for frame in frames:
        square = multiply3(frame, frame)
        wedge2_trace = (trace3(frame) ** 2 - trace3(square)) // 2
        chi_exterior = 1 + trace3(frame) + wedge2_trace + determinant3(frame)
        plus_identity = tuple(
            tuple(frame[i][j] + identity[i][j] for j in range(3))
            for i in range(3)
        )
        chi_determinant = determinant3(plus_identity)
        exterior_identity &= chi_exterior == chi_determinant
        determinant = determinant3(frame)
        proper += int(determinant == 1)
        improper += int(determinant == -1)
        q_value = 16 - 2 * chi_exterior
        u_base = Fraction(chi_exterior, 8)
        member_identity &= 0 <= u_base <= 1
        for member in range(1, 6):
            f_value = Fraction(16, member) * (1 - u_base**member)
            if determinant == -1:
                member_identity &= chi_exterior == 0 and f_value == Fraction(16, member)
            else:
                member_identity &= q_value == 16 * (1 - u_base)
        values.add((determinant, chi_exterior, q_value))
    return {
        "frame_count": len(frames),
        "proper": proper,
        "improper": improper,
        "exterior_identity": exterior_identity,
        "member_identity": member_identity,
        "component_values": tuple(sorted(values)),
    }


def weight(value: int, minus: Fraction, plus: Fraction = Fraction(1)) -> Fraction:
    return plus if value == 1 else minus


def factor_census(r: int, q: int) -> tuple[int, int]:
    cells = r * q
    return 3 * cells + 1, 2 * cells


def fine_physical_kernel(
    r: int,
    q: int,
    temporal_minus: Fraction,
    spatial_minus: Fraction,
    temporal_plus: Fraction = Fraction(1),
    spatial_plus: Fraction = Fraction(1),
) -> dict[tuple[int, ...], Fraction]:
    """Raw fine-link enumeration with retained rungs at multiples of r."""

    length = r * q
    retained = tuple(range(0, length + 1, r))
    hidden = tuple(index for index in range(length + 1) if index not in retained)
    endpoints = tuple(product(G, repeat=2 * (q + 1)))
    internal_count = 2 * (length + 1) + 2 * len(hidden)
    normalization = Fraction(1, 2**internal_count)
    output: dict[tuple[int, ...], Fraction] = {}

    for endpoint in endpoints:
        retained_prime = endpoint[: q + 1]
        retained_value = endpoint[q + 1 :]
        total = Fraction(0)
        for internal in product(G, repeat=internal_count):
            cursor = 0
            bottom = internal[cursor : cursor + length + 1]
            cursor += length + 1
            top = internal[cursor : cursor + length + 1]
            cursor += length + 1
            rung_prime: list[int | None] = [None] * (length + 1)
            rung_value: list[int | None] = [None] * (length + 1)
            for retained_index, column in enumerate(retained):
                rung_prime[column] = retained_prime[retained_index]
                rung_value[column] = retained_value[retained_index]
            for column in hidden:
                rung_prime[column] = internal[cursor]
                rung_value[column] = internal[cursor + 1]
                cursor += 2

            integrand = Fraction(1)
            for column in range(length + 1):
                integrand *= weight(
                    int(rung_prime[column]) * top[column]
                    * int(rung_value[column]) * bottom[column],
                    temporal_minus,
                    temporal_plus,
                )
            for column in range(length):
                integrand *= weight(
                    bottom[column + 1] * bottom[column],
                    temporal_minus,
                    temporal_plus,
                )
                integrand *= weight(
                    top[column + 1] * top[column],
                    temporal_minus,
                    temporal_plus,
                )
                integrand *= weight(
                    int(rung_prime[column + 1]) * int(rung_prime[column]),
                    spatial_minus,
                    spatial_plus,
                )
                integrand *= weight(
                    int(rung_value[column + 1]) * int(rung_value[column]),
                    spatial_minus,
                    spatial_plus,
                )
            total += integrand
        output[endpoint] = normalization * total
    return output


def history_data(
    temporal_minus: Fraction,
    spatial_minus: Fraction,
    temporal_plus: Fraction = Fraction(1),
    spatial_plus: Fraction = Fraction(1),
) -> tuple[dict[tuple[int, ...], Fraction], dict[tuple[tuple[int, ...], tuple[int, ...]], Fraction]]:
    onsite = {
        state: weight(state[2] * state[1] * state[3] * state[0], temporal_minus, temporal_plus)
        for state in STATES
    }
    bond = {}
    for left in STATES:
        for right in STATES:
            bond[left, right] = (
                weight(right[0] * left[0], temporal_minus, temporal_plus)
                * weight(right[1] * left[1], temporal_minus, temporal_plus)
                * weight(right[2] * left[2], spatial_minus, spatial_plus)
                * weight(right[3] * left[3], spatial_minus, spatial_plus)
            )
    return onsite, bond


def compose_bonds(
    left: dict[tuple[tuple[int, ...], tuple[int, ...]], Fraction],
    right: dict[tuple[tuple[int, ...], tuple[int, ...]], Fraction],
    onsite: dict[tuple[int, ...], Fraction],
) -> dict[tuple[tuple[int, ...], tuple[int, ...]], Fraction]:
    return {
        (start, stop): sum(
            (left[start, middle] * onsite[middle] * right[middle, stop] / 16 for middle in STATES),
            Fraction(0),
        )
        for start in STATES
        for stop in STATES
    }


def bond_power(
    bond: dict[tuple[tuple[int, ...], tuple[int, ...]], Fraction],
    onsite: dict[tuple[int, ...], Fraction],
    exponent: int,
) -> dict[tuple[tuple[int, ...], tuple[int, ...]], Fraction]:
    result = bond
    for _ in range(1, exponent):
        result = compose_bonds(result, bond, onsite)
    return result


def history_physical_kernel(
    r: int,
    q: int,
    temporal_minus: Fraction,
    spatial_minus: Fraction,
    temporal_plus: Fraction = Fraction(1),
    spatial_plus: Fraction = Fraction(1),
) -> dict[tuple[int, ...], Fraction]:
    onsite, bond = history_data(
        temporal_minus, spatial_minus, temporal_plus, spatial_plus
    )
    powered = bond_power(bond, onsite, r)
    output = {}
    for endpoint in product(G, repeat=2 * (q + 1)):
        retained_pairs = tuple(
            (endpoint[index], endpoint[q + 1 + index]) for index in range(q + 1)
        )
        matching = tuple(
            tuple(state for state in STATES if state[2:] == pair)
            for pair in retained_pairs
        )
        total = Fraction(0)
        for retained_states in product(*matching):
            term = Fraction(1)
            for state in retained_states:
                term *= onsite[state] / 4
            for index in range(q):
                term *= powered[retained_states[index], retained_states[index + 1]]
            total += term
        output[endpoint] = total
    return output


def duplicated_middle_kernel(
    r: int,
    endpoints: tuple[int, ...],
    temporal_minus: Fraction,
    spatial_minus: Fraction,
) -> Fraction:
    """Incorrect q=2 product of independently frame-marginalized strips."""

    onsite, bond = history_data(temporal_minus, spatial_minus)
    powered = bond_power(bond, onsite, r)
    pairs = tuple((endpoints[index], endpoints[3 + index]) for index in range(3))

    def strip(left_pair: tuple[int, int], right_pair: tuple[int, int]) -> Fraction:
        return sum(
            (
                onsite[left] * onsite[right] * powered[left, right] / 16
                for left in STATES
                for right in STATES
                if left[2:] == left_pair and right[2:] == right_pair
            ),
            Fraction(0),
        )

    return strip(pairs[0], pairs[1]) * strip(pairs[1], pairs[2])


def poly_multiply(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    output = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] += a * b
    return tuple(output)


def poly_power(base: tuple[Fraction, ...], exponent: int) -> tuple[Fraction, ...]:
    output = (Fraction(1),)
    for _ in range(exponent):
        output = poly_multiply(output, base)
    return output


def truncation_algorithm_defect() -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    local = (Fraction(1), Fraction(1))
    direct = poly_power(local, 4)
    two_step = poly_power(local, 2)[:2]
    retruncated_staged = poly_power(two_step, 2)
    return direct, retruncated_staged


def z2_fourier_positive(plus: Fraction, minus: Fraction) -> bool:
    return (plus + minus) / 2 >= 0 and (plus - minus) / 2 >= 0


@lru_cache(maxsize=1)
def independent_facts() -> dict[str, object]:
    exterior = exterior_facts()
    temporal_minus = Fraction(1, 2)
    spatial_minus = Fraction(2, 3)
    temporal_delta = Fraction(1, 8)
    spatial_delta = Fraction(1, 6)
    temporal_plus = 1 - temporal_delta
    spatial_plus = 1 - spatial_delta

    direct_21 = fine_physical_kernel(2, 1, temporal_minus, spatial_minus)
    staged_21 = history_physical_kernel(2, 1, temporal_minus, spatial_minus)
    direct_12 = fine_physical_kernel(1, 2, temporal_minus, spatial_minus)
    staged_12 = history_physical_kernel(1, 2, temporal_minus, spatial_minus)
    truncated_12 = fine_physical_kernel(
        1, 2, temporal_minus, spatial_minus, temporal_plus, spatial_plus
    )
    gamma_12 = (1 - temporal_delta) ** 7 * (1 - spatial_delta) ** 4
    sandwich = all(
        gamma_12 * direct_12[key] <= truncated_12[key] <= direct_12[key]
        for key in direct_12
    )
    shared_difference = any(
        duplicated_middle_kernel(1, endpoint, temporal_minus, spatial_minus)
        != staged_12[endpoint]
        for endpoint in staged_12
    )

    cutoff_tail = {
        cutoff: Fraction(8, 7) ** (cutoff + 1) / factorial(cutoff + 1)
        for cutoff in (6, 10, 14, 18)
    }
    direct_poly, retruncated_poly = truncation_algorithm_defect()

    return {
        **exterior,
        "censuses": tuple((r, q, *factor_census(r, q)) for r, q in ((1, 1), (2, 1), (1, 2), (2, 2))),
        "direct_staged_hidden": direct_21 == staged_21,
        "direct_staged_shared": direct_12 == staged_12,
        "duplicated_shared_differs": shared_difference,
        "sandwich": sandwich,
        "gamma_12": gamma_12,
        "max_error_12": max(direct_12[key] - truncated_12[key] for key in direct_12),
        "cutoff_tail": cutoff_tail,
        "direct_polynomial": direct_poly,
        "retruncated_polynomial": retruncated_poly,
        "retruncation_differs": direct_poly != retruncated_poly,
        "z2_character_positive": all(
            (
                z2_fourier_positive(plus, minus)
                for plus, minus in (
                    (Fraction(1), temporal_minus),
                    (temporal_plus, temporal_minus),
                    (Fraction(1), spatial_minus),
                    (spatial_plus, spatial_minus),
                )
            )
        ),
    }


if __name__ == "__main__":
    facts = independent_facts()
    checks = (
        facts["frame_count"] == 48 and facts["proper"] == facts["improper"] == 24,
        facts["exterior_identity"],
        facts["member_identity"],
        facts["censuses"] == ((1, 1, 4, 2), (2, 1, 7, 4), (1, 2, 7, 4), (2, 2, 13, 8)),
        facts["direct_staged_hidden"],
        facts["direct_staged_shared"],
        facts["duplicated_shared_differs"],
        facts["sandwich"],
        facts["z2_character_positive"],
        facts["retruncation_differs"],
        61 * facts["cutoff_tail"][10] < Fraction(1, 100_000),
        61 * facts["cutoff_tail"][18] < Fraction(1, 10**12),
    )
    for index, condition in enumerate(checks, start=1):
        print(f"[{'PASS' if condition else 'FAIL'}] independent check {index}")
    passed = sum(bool(value) for value in checks)
    failed = len(checks) - passed
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    raise SystemExit(int(failed != 0))
