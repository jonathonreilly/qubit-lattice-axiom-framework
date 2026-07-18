#!/usr/bin/env python3
"""Exact directional-tilt enumeration for nearest-neighbor bonds of Z^3."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import lcm

import sympy as sp


Point = tuple[int, int, int]
Bond = tuple[Point, Point]


def add(p: Point, q: Point) -> Point:
    return tuple(a + b for a, b in zip(p, q))  # type: ignore[return-value]


def canonical_bond(p: Point, q: Point) -> Bond:
    return tuple(sorted((p, q)))  # type: ignore[return-value]


def height(bond: Bond) -> int:
    return bond[0][0] + bond[1][0]


def orientation(bond: Bond) -> int:
    differing = [i for i in range(3) if bond[0][i] != bond[1][i]]
    assert len(differing) == 1
    return differing[0]


def lattice_box_bonds(radius: int) -> set[Bond]:
    """All positive-axis bonds whose two endpoints lie in [-radius,radius]^3."""
    axes: tuple[Point, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    points = set(product(range(-radius, radius + 1), repeat=3))
    bonds: set[Bond] = set()
    for p in points:
        for axis in axes:
            q = add(p, axis)
            if q in points:
                bonds.add(canonical_bond(p, q))
    return bonds


def adjacency_map(bonds: set[Bond]) -> dict[Bond, set[Bond]]:
    incident: dict[Point, set[Bond]] = defaultdict(set)
    for bond in bonds:
        incident[bond[0]].add(bond)
        incident[bond[1]].add(bond)
    adjacent: dict[Bond, set[Bond]] = {}
    for bond in bonds:
        adjacent[bond] = (incident[bond[0]] | incident[bond[1]]) - {bond}
    return adjacent


def delta_counts(bond: Bond, adjacent: dict[Bond, set[Bond]]) -> Counter[int]:
    return Counter(height(other) - height(bond) for other in adjacent[bond])


EXPECTED_PAR = Counter({-2: 1, -1: 4, 1: 4, 2: 1})
EXPECTED_PERP = Counter({-1: 2, 0: 6, 1: 2})


def ordered_counter(counter: Counter[int]) -> str:
    entries = ", ".join(f"{delta}: {counter[delta]}" for delta in sorted(counter))
    return "{" + entries + "}"


def verify_box(radius: int) -> tuple[int, int, int, Counter[int], Counter[int]]:
    bonds = lattice_box_bonds(radius)
    adjacent = adjacency_map(bonds)

    origin = (0, 0, 0)
    parallel_start = canonical_bond(origin, (1, 0, 0))
    transverse_start = canonical_bond(origin, (0, 1, 0))
    par_central = delta_counts(parallel_start, adjacent)
    perp_central = delta_counts(transverse_start, adjacent)
    assert par_central == EXPECTED_PAR
    assert perp_central == EXPECTED_PERP

    safe_bonds = [
        bond
        for bond in bonds
        if all(abs(coordinate) <= radius - 1 for point in bond for coordinate in point)
    ]
    safe_parallel = 0
    safe_transverse = 0
    for bond in safe_bonds:
        counts = delta_counts(bond, adjacent)
        if orientation(bond) == 0:
            assert counts == EXPECTED_PAR, (radius, bond, counts)
            safe_parallel += 1
        else:
            assert counts == EXPECTED_PERP, (radius, bond, counts)
            safe_transverse += 1

    return len(bonds), safe_parallel, safe_transverse, par_central, perp_central


def fraction_text(value: sp.Rational) -> str:
    numerator, denominator = value.as_numer_denom()
    if denominator == 1:
        return str(numerator)
    return f"{numerator}/{denominator}"


def as_fraction(value: sp.Rational) -> Fraction:
    numerator, denominator = value.as_numer_denom()
    return Fraction(int(numerator), int(denominator))


def exact_velocity_certificate(
    best_y: sp.Rational,
    best_s: sp.Rational,
    other_y: sp.Rational,
    other_s: sp.Rational,
) -> tuple[int, int, bool]:
    """Certify best_s/log(best_y) < other_s/log(other_y) exactly.

    The inequality is equivalent to
        other_y**best_s < best_y**other_s.
    Multiplication by the LCM of the two denominators in the S values
    turns both exponents into integers, so Fraction comparison suffices.
    """
    best_s_fraction = as_fraction(best_s)
    other_s_fraction = as_fraction(other_s)
    common = lcm(best_s_fraction.denominator, other_s_fraction.denominator)
    other_exponent = best_s_fraction.numerator * (
        common // best_s_fraction.denominator
    )
    best_exponent = other_s_fraction.numerator * (
        common // other_s_fraction.denominator
    )
    lhs = as_fraction(other_y) ** other_exponent
    rhs = as_fraction(best_y) ** best_exponent
    return other_exponent, best_exponent, lhs < rhs


def main() -> None:
    print("EXACT LOCAL SIGNATURES")
    print(f"parallel:   {ordered_counter(EXPECTED_PAR)}")
    print(f"transverse: {ordered_counter(EXPECTED_PERP)}")
    print()

    print("FINITE-BOX STABILITY CHECKS")
    for radius in (2, 4):
        total, safe_par, safe_perp, par_central, perp_central = verify_box(radius)
        print(
            f"radius={radius}: total_bonds={total}, "
            f"safe_parallel_checked={safe_par}, safe_transverse_checked={safe_perp}"
        )
        print(f"  central parallel   {ordered_counter(par_central)}")
        print(f"  central transverse {ordered_counter(perp_central)}")
    print()

    y = sp.symbols("y", positive=True)
    s_par = y**2 + 4 * y + 4 / y + y**-2
    s_perp = 2 * y + 6 + 2 / y
    s_coefficientwise = y**2 + 4 * y + 6 + 4 / y + y**-2
    difference = sp.factor(s_par - s_perp)
    expected_difference = (y - 1) ** 2 * (y**2 + 4 * y + 1) / y**2
    assert sp.simplify(difference - expected_difference) == 0
    assert s_par.subs(y, 1) == 10
    assert s_perp.subs(y, 1) == 10
    assert s_coefficientwise.subs(y, 1) == 16

    print("SYMBOLIC TILT DATA")
    print(f"S_par(y)  = {s_par}")
    print(f"S_perp(y) = {s_perp}")
    print(f"S_coefficientwise(y) = {s_coefficientwise}")
    print(f"S_par(y) - S_perp(y) = {difference}")
    print("S_max(y) = S_par(y) for y >= 1")
    print(f"S_par(1) = {s_par.subs(y, 1)}, S_perp(1) = {s_perp.subs(y, 1)}")
    print()

    rational_points = tuple(
        sp.Rational(f.numerator, f.denominator)
        for f in (
            Fraction(5, 4),
            Fraction(3, 2),
            Fraction(2, 1),
            Fraction(5, 2),
            Fraction(3, 1),
            Fraction(4, 1),
        )
    )
    scan: list[tuple[sp.Rational, sp.Rational, sp.Rational, sp.Expr]] = []
    print("RATIONAL TILT SCAN")
    print("velocity convention: v(y)/J = S_max(y)/ln(y)")
    for point in rational_points:
        par_value = sp.factor(s_par.subs(y, point))
        perp_value = sp.factor(s_perp.subs(y, point))
        velocity_over_j = par_value / sp.log(point)
        scan.append((point, par_value, perp_value, velocity_over_j))
        advisory = sp.N(velocity_over_j, 12)
        print(
            f"y={fraction_text(point)}: S_par={fraction_text(par_value)}, "
            f"S_perp={fraction_text(perp_value)}, "
            f"v/J=({fraction_text(par_value)})/ln({fraction_text(point)}), "
            f"advisory_float={advisory}"
        )

    point = sp.Rational(5, 2)
    best = next(row for row in scan if row[0] == point)
    point, par_value, _, velocity_over_j = best
    exact_certificates: list[str] = []
    for other_point, other_par, _, _ in scan:
        if other_point == point:
            continue
        other_exponent, best_exponent, certified = exact_velocity_certificate(
            point, par_value, other_point, other_par
        )
        assert certified
        exact_certificates.append(
            f"  ({fraction_text(other_point)})^{other_exponent} "
            f"< ({fraction_text(point)})^{best_exponent}: {certified}"
        )
    parent = 20 * sp.E
    improvement_factor = 2000 * sp.E * sp.log(sp.Rational(5, 2)) / 1801
    print()
    print("SCAN SUMMARY")
    print(
        f"best scanned y={fraction_text(point)}: "
        f"v=({fraction_text(par_value)})*J/ln({fraction_text(point)})"
    )
    print("exact best-point certificates (each is equivalent to v_best < v_other):")
    for certificate in exact_certificates:
        print(certificate)
    print(f"best advisory v/J={sp.N(velocity_over_j, 12)}")
    print(f"parent 20*e advisory={sp.N(parent, 12)}")
    print(f"parent/best exact ratio={improvement_factor}")
    print(f"parent/best advisory ratio={sp.N(improvement_factor, 12)}")


if __name__ == "__main__":
    main()
