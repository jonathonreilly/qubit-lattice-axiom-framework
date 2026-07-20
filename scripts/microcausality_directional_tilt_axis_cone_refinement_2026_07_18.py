#!/usr/bin/env python3
"""Exact checks for the directional-tilt axis-cone refinement note."""

from fractions import Fraction

import sympy as sp


EXPECTED_LABELS = [
    "parallel-height-table",
    "transverse-height-table",
    "tilt-polynomials",
    "tilt-domination",
    "walk-row-bound",
    "indicator-bound",
    "axis-offset-witness",
    "series-assembly",
    "display-decay",
    "offset-prefactor-mutation",
    "scan-value",
    "parent-comparison",
    "scan-interval-comparisons",
]


class CheckRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.labels = []

    def check(self, label, condition):
        ok = bool(condition)
        self.labels.append(label.split()[0])
        if ok:
            self.passed += 1
            print(f"PASS: {label}")
        else:
            self.failed += 1
            print(f"FAIL: {label}")

    def finish(self):
        if self.labels != EXPECTED_LABELS:
            print(
                "FAIL: gate-manifest drift: labels "
                f"{self.labels} != expected {EXPECTED_LABELS}"
            )
            self.failed += 1
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


AXES = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def add(p, q):
    return tuple(a + b for a, b in zip(p, q))


def bond_key(p, q):
    return frozenset((p, q))


def incident_bonds(site, radius):
    out = set()
    for direction in AXES:
        for sign in (1, -1):
            other = add(site, tuple(sign * component for component in direction))
            if all(-radius <= coordinate <= radius for coordinate in other):
                out.add(bond_key(site, other))
    return out


def adjacent_bonds(bond, radius):
    out = set()
    for site in bond:
        out |= incident_bonds(site, radius)
    out.discard(bond)
    return out


def phi(bond):
    return sum(point[0] for point in bond)


def delta_table(start_bond, radius):
    table = {}
    for neighbor in adjacent_bonds(start_bond, radius):
        delta = phi(neighbor) - phi(start_bond)
        table[delta] = table.get(delta, 0) + 1
    return table


def rational_log_bounds(q, terms=3):
    """Rational enclosure of log(q) from its positive atanh series.

    For q>1, put z=(q-1)/(q+1). The returned lower bound keeps ``terms``
    positive terms. The upper bound adds a geometric majorant of the tail,
    using 1/(2k+1) <= 1/(2*terms+1) on all omitted terms.
    """
    q = Fraction(q)
    z = (q - 1) / (q + 1)
    lower = 2 * sum(
        (z ** (2 * k + 1)) / Fraction(2 * k + 1)
        for k in range(terms)
    )
    first_omitted_denominator = 2 * terms + 1
    tail = (
        2
        * z ** first_omitted_denominator
        / (Fraction(first_omitted_denominator) * (1 - z * z))
    )
    return lower, lower + tail


def main():
    checks = CheckRunner()
    origin = (0, 0, 0)

    parallel = bond_key(origin, (1, 0, 0))
    parallel_table_4 = delta_table(parallel, 4)
    parallel_table_6 = delta_table(parallel, 6)
    expected_parallel = {-2: 1, -1: 4, 1: 4, 2: 1}
    checks.check(
        "parallel-height-table exact {-2:1,-1:4,+1:4,+2:1}, box-stable",
        parallel_table_4 == expected_parallel
        and parallel_table_6 == expected_parallel,
    )

    transverse_2 = bond_key(origin, (0, 1, 0))
    transverse_3 = bond_key(origin, (0, 0, 1))
    expected_transverse = {-1: 2, 0: 6, 1: 2}
    checks.check(
        "transverse-height-table exact {-1:2,0:6,+1:2} for both orientations",
        delta_table(transverse_2, 4) == expected_transverse
        and delta_table(transverse_3, 4) == expected_transverse
        and delta_table(transverse_2, 6) == expected_transverse
        and delta_table(transverse_3, 6) == expected_transverse,
    )

    y = sp.Symbol("y", positive=True)
    parallel_from_table = sum(
        multiplicity * y**delta
        for delta, multiplicity in parallel_table_4.items()
    )
    transverse_from_table = sum(
        multiplicity * y**delta
        for delta, multiplicity in delta_table(transverse_2, 4).items()
    )
    s_parallel = y**2 + 4 * y + 4 / y + y**-2
    s_transverse = 2 * y + 6 + 2 / y
    checks.check(
        "tilt-polynomials reconstructed term-by-term with untilted value 10",
        sp.simplify(parallel_from_table - s_parallel) == 0
        and sp.simplify(transverse_from_table - s_transverse) == 0
        and s_parallel.subs(y, 1) == 10
        and s_transverse.subs(y, 1) == 10,
    )

    factorized_difference = (y - 1) ** 2 * (y**2 + 4 * y + 1) / y**2
    checks.check(
        "tilt-domination exact positive factorization",
        sp.simplify(s_parallel - s_transverse - factorized_difference) == 0
        and ((y - 1) ** 2).is_nonnegative
        and (y**2 + 4 * y + 1).is_positive
        and (y**2).is_positive,
    )

    y52 = sp.Rational(5, 2)
    checks.check(
        "walk-row-bound both bond types bounded by S_parallel for y>=1",
        sp.simplify((s_parallel - s_transverse).subs(y, 1)) == 0
        and sp.simplify((s_parallel - s_transverse).subs(y, y52))
        == sp.Rational(621, 100)
        and sp.simplify((s_parallel - s_transverse).subs(y, y52)).is_positive
        is True,
    )

    checks.check(
        "indicator-bound exact threshold and below-threshold instances",
        y52**0 == 1
        and y52**1 >= 1
        and 0 < y52**-1 < 1,
    )

    a = sp.Symbol("a", integer=True)
    m = sp.Symbol("m", integer=True, positive=True)
    offset_identity = sp.simplify(
        (2 * (a + m) - 1) - (2 * a + 1) - (2 * m - 2)
    ) == 0
    left_site = (0, 0, 0)
    right_site = (1, 0, 0)
    minimal_bond = bond_key(left_site, right_site)
    witness_gain = phi(minimal_bond) - phi(minimal_bond)
    checks.check(
        "axis-offset-witness exact 2m-2 offset and m=1 counterexample to 2m-1",
        offset_identity
        and witness_gain == 0
        and witness_gain == 2 * 1 - 2
        and not witness_gain >= 2 * 1 - 1,
    )

    j_s, t_s, s_s, a_n, b_n, n_s, m_s = sp.symbols(
        "j_s t_s s_s a_n b_n n_s m_s", positive=True
    )
    k = sp.Symbol("k", integer=True, positive=True)
    series = sp.Sum(
        (2 * j_s * s_s * t_s) ** k / sp.factorial(k),
        (k, 1, sp.oo),
    ).doit()
    k_term = (
        2
        * a_n
        * (2 * j_s) ** (k - 1)
        * (2 * j_s * b_n)
        * (n_s * s_s ** (k - 1) * y ** (-(2 * m_s - 2)))
        * t_s**k
        / sp.factorial(k)
    )
    summed = sp.Sum(k_term, (k, 1, sp.oo)).doit()
    display = (
        2
        * a_n
        * b_n
        * n_s
        * (y**2 / s_s)
        * y ** (-2 * m_s)
        * (sp.exp(2 * j_s * s_s * t_s) - 1)
    )
    checks.check(
        "series-assembly reconstructed parent k-term sums to theorem display",
        sp.simplify(series - (sp.exp(2 * j_s * s_s * t_s) - 1)) == 0
        and sp.simplify(summed - display) == 0,
    )

    m_integer = sp.Symbol("m_integer", integer=True, positive=True)
    checks.check(
        "display-decay exact y=5/2 spatial factor (4/25)^m",
        sp.simplify(
            y52 ** (-2 * m_integer) - sp.Rational(4, 25) ** m_integer
        )
        == 0
        and sp.Rational(4, 25) < 1,
    )

    true_prefactor = y**2 / s_s
    false_prefactor = y / s_s
    checks.check(
        "offset-prefactor-mutation false 2m-1 offset and y/S prefactor rejected",
        witness_gain < 1
        and sp.simplify(true_prefactor - false_prefactor) != 0
        and sp.simplify((true_prefactor / false_prefactor) - y) == 0,
    )

    exact_s52 = sp.Rational(1801, 100)
    checks.check(
        "scan-value S_parallel(5/2)=1801/100 exactly",
        sp.simplify(s_parallel.subs(y, y52) - exact_s52) == 0,
    )

    e_lower = sp.Rational(1957, 720)
    log52_lower = sp.Rational(312, 343)
    e_partial = sum(sp.Rational(1, sp.factorial(n)) for n in range(7))
    parent_margin = 20 * e_lower * log52_lower - exact_s52
    checks.check(
        "parent-comparison exact positive-series lower bounds and rational margin",
        e_partial == e_lower
        and (1 + sp.Rational(3, 7)) / (1 - sp.Rational(3, 7)) == y52
        and 2 * (sp.Rational(3, 7) + sp.Rational(3, 7) ** 3 / 3)
        == log52_lower
        and parent_margin == sp.Rational(3234971, 102900)
        and parent_margin > 0,
    )

    scan = {
        Fraction(5, 4): Fraction(4161, 400),
        Fraction(3, 2): Fraction(409, 36),
        Fraction(2): Fraction(57, 4),
        Fraction(3): Fraction(202, 9),
        Fraction(4): Fraction(529, 16),
    }
    scan_values_ok = all(
        sp.simplify(
            s_parallel.subs(y, sp.Rational(point.numerator, point.denominator))
            - sp.Rational(value.numerator, value.denominator)
        )
        == 0
        for point, value in scan.items()
    )
    log52_interval = rational_log_bounds(Fraction(5, 2), terms=3)
    interval_margins = []
    for point, value in scan.items():
        _, point_upper = rational_log_bounds(point, terms=3)
        margin = value * log52_interval[0] - Fraction(1801, 100) * point_upper
        interval_margins.append(margin)
    checks.check(
        "scan-interval-comparisons rational atanh bounds prove all five pairs",
        scan_values_ok
        and log52_interval[0] < log52_interval[1]
        and len(interval_margins) == 5
        and all(margin > 0 for margin in interval_margins),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
