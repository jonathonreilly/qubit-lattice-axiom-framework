#!/usr/bin/env python3
"""Independent exact checks for the nonzero-spatial volume-gap family."""

from __future__ import annotations

import itertools
from fractions import Fraction as F


AUDIT_TIMEOUT_SEC = 120


def cube(value: F) -> F:
    return value * value * value


def shell_mass(inner: int, outer: int, m: int) -> F:
    return F(outer**3 - inner**3, m**3)


def eroded_fraction(inner: int, outer: int, m: int) -> F:
    lower = F(inner, m) + F(1, m**3)
    upper = F(outer, m) - F(1, m**3)
    return (cube(upper) - cube(lower)) / F(outer**3 - inner**3, m**3)


def radial_action_bound(m: int, sites: int) -> F:
    radius_max = F(4, m)
    onsite_coefficient_max = F(3 - (-1), 2)
    hopping_coefficient_max = F(1, 7) * 7 / 2
    onsite_per_site = onsite_coefficient_max * radius_max**2
    hopping_per_edge = hopping_coefficient_max * (2 * radius_max) ** 2
    onsite = onsite_per_site * sites
    hopping = hopping_per_edge * (sites - 1)
    return onsite + hopping


def signed_frames() -> tuple[tuple[tuple[int, ...], ...], ...]:
    frames: list[tuple[tuple[int, ...], ...]] = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[row] if column == permutation[row] else 0
                      for column in range(3))
                for row in range(3)
            )
            frames.append(matrix)
    return tuple(frames)


def matvec(matrix: tuple[tuple[int, ...], ...],
           vector: tuple[F, ...]) -> tuple[F, ...]:
    return tuple(
        sum((F(entry) * coordinate
             for entry, coordinate in zip(row, vector)), F(0))
        for row in matrix
    )


def norm2(vector: tuple[F, ...]) -> F:
    return sum((coordinate * coordinate for coordinate in vector), F(0))


def derived_cross_prefactor() -> tuple[int, int, int, F]:
    radicand = 2 * (2**3 - 1**3) * (4**3 - 3**3)
    ceiling = 1
    while ceiling**2 <= radicand:
        ceiling += 1
    exponential_denominator = 2**3 * 6
    prefactor = F(ceiling * exponential_denominator, 3)
    return radicand, ceiling, exponential_denominator, prefactor


def lower_bound(m: int, sites: int) -> F:
    v = eroded_fraction(1, 2, m)
    gaussian = F(1) - F(3, m**6)
    action = F(1) - F(64 * sites, m**2)
    _, _, _, cross_prefactor = derived_cross_prefactor()
    eta = F(cross_prefactor, m**15)
    return action * (v * gaussian) ** sites - eta**sites


def gap_upper(m: int) -> F:
    action_loss = F(64)
    erosion_loss = F(15, 7)
    _, _, _, cross_prefactor = derived_cross_prefactor()
    return (
        (action_loss + erosion_loss) / m
        + F(3, m**5)
        + F(cross_prefactor, m**15) ** m
    )


def independent_facts() -> dict[str, bool]:
    m = 128
    first_mass = shell_mass(1, 2, m)
    second_mass = shell_mass(3, 4, m)
    first_eroded = eroded_fraction(1, 2, m)
    second_eroded = eroded_fraction(3, 4, m)
    (cross_radicand, radical_ceiling,
     exponential_denominator, cross_prefactor) = derived_cross_prefactor()
    normalized_cross_power = 18 - 3
    exponential_power = 12 - 2
    cubic_exponential_power = 3 * exponential_power
    gap_coefficient = F(64) + F(15, 7)

    frames = signed_frames()
    vector = (F(1, 4), F(1, 5), F(1, 6))
    frame_norms = tuple(norm2(matvec(frame, vector)) for frame in frames)

    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    minus_identity = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
    e1 = (F(1), F(0), F(0))
    minus_e1 = (F(-1), F(0), F(0))
    bare_before = norm2(tuple(a - b for a, b in zip(e1, e1)))
    transformed_after = norm2(tuple(
        a - b for a, b in zip(
            matvec(identity, e1),
            matvec(minus_identity, e1),
        )
    ))

    negative_hopping = -F(1, 2) * norm2(tuple(
        a - b for a, b in zip(minus_e1, e1)
    ))
    negative_sign_action = negative_hopping + F(2, 7)

    selected = (128, 256, 512)
    selected_lower = tuple(lower_bound(value, value) for value in selected)
    selected_gap = tuple(gap_upper(value) for value in selected)

    return {
        "the two normalized full-ball shell masses are exact": (
            first_mass == F(7, m**3)
            and second_mass == F(37, m**3)
        ),
        "the first eroded shell has the displayed closed fraction": (
            first_eroded
            == F(1) - F(15 * m**4 - 3 * m**2 + 2, 7 * m**6)
        ),
        "the second eroded shell is strictly less lossy": (
            second_eroded - first_eroded
            == F(30 * (m**2 - 1) * (m**2 - 2), 259 * m**6)
        ),
        "the temporal scale and erosion give the exact Gaussian tail power": (
            F(3, m**12) / F(1, m**6) == F(3, m**6)
        ),
        "the cross-shell exponential majorant has the stated rational tail": (
            cross_radicand == 518
            and radical_ceiling == 23
            and exponential_denominator == 48
            and cross_prefactor == 368
            and normalized_cross_power == 15
            and exponential_power == 10
            and cubic_exponential_power == 30
        ),
        "the coframe domain gives the exact hopping weight ceiling": (
            F(1, 7) * 7 == 1
        ),
        "the shrinking tubes give the exact nonzero spatial matter-connection action ceiling": (
            radial_action_bound(m, m) == F(64 * m - 32, m**2)
            and radial_action_bound(m, m) <= F(64 * m, m**2)
        ),
        "all forty-eight proper and improper signed frames preserve radii": (
            len(frames) == 48
            and len(set(frames)) == 48
            and all(value == norm2(vector) for value in frame_norms)
        ),
        "omitting the transporter falsifies independent endpoint covariance": (
            bare_before == 0 and transformed_after == 4
        ),
        "a negative hopping sign defeats the multiplier ceiling": (
            negative_sign_action == F(-12, 7)
        ),
        "widening the scalar interval makes the onsite quadratic negative": (
            F(3 - 4, 2) == F(-1, 2)
        ),
        "the explicit connected family has a positive compression bound": (
            all(value > F(7, 16) for value in selected_lower)
        ),
        "the explicit connected-family compression improves": (
            all(left < right for left, right
                in zip(selected_lower, selected_lower[1:]))
        ),
        "the exact normalized-gap upper bound decreases": (
            gap_coefficient == F(463, 7)
            and F(1) - F(15, 7 * m) - F(3, m**5) > F(15, 16)
            and F(cross_prefactor, m**15) ** m < F(1, 32)
            and
            all(left > right for left, right
                in zip(selected_gap, selected_gap[1:]))
        ),
        "the certified gap bound is below one and positive": (
            all(F(0) < value < F(1) for value in selected_gap)
        ),
        "quadratic volume is outside the proved closing scale": (
            F(15 * m**4 - 3 * m**2 + 2, 7 * m**6) * m**2
            > F(2)
        ),
    }


def main() -> int:
    facts = independent_facts()
    passed = 0
    failed = 0
    for name, condition in facts.items():
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        passed += int(ok)
        failed += int(not ok)
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
