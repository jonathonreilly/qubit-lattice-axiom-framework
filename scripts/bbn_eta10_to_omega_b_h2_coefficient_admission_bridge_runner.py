#!/usr/bin/env python3
"""Exact checker for cubic-reciprocal bounds and rational normalization.

The source path is historical. The repaired theorem is self-contained:
rational integral-test brackets for sum(k^-3), plus scaling and unique target
normalization for a positive rational monomial. This runner reads no audit
state, imports no physical data, and writes no files.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import lcm
from pathlib import Path
from typing import Callable, Sequence


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "BBN_ETA10_TO_OMEGA_B_H2_COEFFICIENT_ADMISSION_BRIDGE_"
    "BOUNDED_NOTE_2026-05-28.md"
)

F0 = Fraction(0)
F1 = Fraction(1)
F2 = Fraction(2)

MUTATION_NAMES = (
    "series-power-two",
    "lower-tail-wrong-endpoint",
    "upper-tail-wrong-endpoint",
    "temperature-square",
    "density-in-numerator",
    "normalizer-inverted",
    "coerce-non-fractions",
    "interpretation-physical",
    "interpretation-comparator",
    "interpretation-framework",
)
MUTATIONS: frozenset[str] = frozenset()


class Harness:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def banner(self, title: str) -> None:
        print()
        print("-" * 88)
        print(title)
        print("-" * 88)

    def check(self, name: str, condition: bool, detail: str = "") -> bool:
        status = "PASS" if condition else "FAIL"
        suffix = f"  ({detail})" if detail else ""
        print(f"  [{status}] {name}{suffix}")
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        return condition

    def expect_raises(
        self,
        name: str,
        error: type[BaseException],
        operation: Callable[[], object],
    ) -> bool:
        try:
            operation()
        except error:
            return self.check(name, True)
        except BaseException as exc:
            return self.check(
                name,
                False,
                f"raised {type(exc).__name__}, expected {error.__name__}",
            )
        return self.check(name, False, f"expected {error.__name__}")


def require_index(value: object) -> int:
    if type(value) is not int:
        raise TypeError("N must be an exact built-in integer")
    if value < 1:
        raise ValueError("N must be at least one")
    return value


def require_fraction(name: str, value: object) -> Fraction:
    if "coerce-non-fractions" in MUTATIONS:
        try:
            return Fraction(value)  # type: ignore[arg-type]
        except (TypeError, ValueError, ZeroDivisionError) as exc:
            raise TypeError(f"{name} must be coercible to Fraction") from exc
    if type(value) is not Fraction:
        raise TypeError(f"{name} must be an exact Fraction")
    return value


def require_positive_fraction(name: str, value: object) -> Fraction:
    result = require_fraction(name, value)
    if result <= F0:
        raise ValueError(f"{name} must be positive")
    return result


def partial_sum(n: object) -> Fraction:
    index = require_index(n)
    power = 2 if "series-power-two" in MUTATIONS else 3
    return sum((Fraction(1, k**power) for k in range(1, index + 1)), F0)


def tail_bracket(n: object) -> tuple[Fraction, Fraction]:
    index = require_index(n)
    total = partial_sum(index)
    lower_endpoint = index if "lower-tail-wrong-endpoint" in MUTATIONS else index + 1
    upper_endpoint = index + 1 if "upper-tail-wrong-endpoint" in MUTATIONS else index
    lower = total + Fraction(1, 2 * lower_endpoint**2)
    upper = total + Fraction(1, 2 * upper_endpoint**2)
    return lower, upper


def doubled_bracket(n: object) -> tuple[Fraction, Fraction]:
    lower, upper = tail_bracket(n)
    return F2 * lower, F2 * upper


def coefficient(a: object, t: object, m: object, r: object, s: object) -> Fraction:
    a_q = require_positive_fraction("a", a)
    t_q = require_positive_fraction("t", t)
    m_q = require_positive_fraction("m", m)
    r_q = require_positive_fraction("r", r)
    s_q = require_positive_fraction("s", s)
    power = 2 if "temperature-square" in MUTATIONS else 3
    numerator = a_q * t_q**power * m_q * s_q
    if "density-in-numerator" in MUTATIONS:
        return numerator * r_q
    return numerator / r_q


def target_normalization(
    a: object,
    t: object,
    m: object,
    r: object,
    target: object,
) -> Fraction:
    target_q = require_positive_fraction("target", target)
    raw = coefficient(a, t, m, r, F1)
    if "normalizer-inverted" in MUTATIONS:
        return raw / target_q
    return target_q / raw


def rational_grid() -> tuple[Fraction, ...]:
    return tuple(
        sorted(
            {
                Fraction(numerator, denominator)
                for denominator in range(1, 6)
                for numerator in range(1, 7)
            }
        )
    )


def effective_note_text() -> str:
    text = NOTE_PATH.read_text(encoding="utf-8")
    if "interpretation-physical" in MUTATIONS:
        text += "\nThis theorem derives the physical baryon density coefficient.\n"
    if "interpretation-comparator" in MUTATIONS:
        text += "\nThe rational example is the published Cyburt coefficient.\n"
    if "interpretation-framework" in MUTATIONS:
        text += "\nThe normalization is selected by the framework.\n"
    return text


def source_boundary_checks(h: Harness) -> None:
    h.banner("Source theorem and authority boundary")
    text = effective_note_text()
    flattened = " ".join(text.split())
    h.check(
        "explicit positive-theorem typing",
        "**Type:** positive_theorem" in text
        and "**Claim type:** positive_theorem" in text,
    )
    h.check("dependencies are explicitly empty", "**Dependencies:** none" in text)
    h.check("T1 universal integer domain is written", "every integer `N >= 1`" in text)
    h.check("T2 positive-rational domain is written", "positive rationals `a,t,m,r,s`" in text)
    h.check("historical premise packet removed", "P1-P4" not in text)
    h.check("historical comparator name removed", "Cyburt" not in text)
    h.check("historical distribution setup removed", "Planck distribution" not in text)
    h.check("historical CMB symbol removed", "T_CMB" not in text)
    h.check("historical residual symbol removed", "S_Cyburt" not in text)
    h.check("historical admission heading removed", "Supplied premise packet" not in text)

    forbidden_overclaims = (
        "derives the physical baryon density coefficient",
        "rational example is the published Cyburt coefficient",
        "normalization is selected by the framework",
    )
    hits = [phrase for phrase in forbidden_overclaims if phrase in flattened]
    h.check(
        "physical/comparator/framework overclaims are absent",
        not hits,
        f"hits={hits}" if hits else "",
    )


class FractionSubclass(Fraction):
    pass


class IntSubclass(int):
    pass


def common_api_checks(h: Harness) -> None:
    h.banner("Strict public API")
    h.expect_raises(
        "coefficient rejects integer scalar",
        TypeError,
        lambda: coefficient(1, F1, F1, F1, F1),
    )
    h.expect_raises(
        "coefficient rejects boolean scalar",
        TypeError,
        lambda: coefficient(True, F1, F1, F1, F1),
    )
    h.expect_raises(
        "coefficient rejects float scalar",
        TypeError,
        lambda: coefficient(1.0, F1, F1, F1, F1),
    )
    h.expect_raises(
        "coefficient rejects Fraction subclass",
        TypeError,
        lambda: coefficient(FractionSubclass(1), F1, F1, F1, F1),
    )
    h.expect_raises(
        "partial sum rejects boolean index",
        TypeError,
        lambda: partial_sum(True),
    )
    h.expect_raises(
        "partial sum rejects integer subclass",
        TypeError,
        lambda: partial_sum(IntSubclass(2)),
    )


def normal_checks(h: Harness) -> None:
    source_boundary_checks(h)
    common_api_checks(h)

    h.banner("T1 exact rational series brackets")
    indices = tuple(range(1, 181))
    h.check("S_1=1", partial_sum(1) == F1)
    h.check("S_2=9/8", partial_sum(2) == Fraction(9, 8))
    h.check("S_3=251/216", partial_sum(3) == Fraction(251, 216))
    h.check(
        "partial-sum recurrence holds through N=180",
        all(partial_sum(n + 1) - partial_sum(n) == Fraction(1, (n + 1) ** 3) for n in indices[:-1]),
    )
    h.check(
        "lower bracket has the stated endpoint",
        all(tail_bracket(n)[0] == partial_sum(n) + Fraction(1, 2 * (n + 1) ** 2) for n in indices),
    )
    h.check(
        "upper bracket has the stated endpoint",
        all(tail_bracket(n)[1] == partial_sum(n) + Fraction(1, 2 * n**2) for n in indices),
    )
    h.check(
        "exact width formula holds through N=180",
        all(
            tail_bracket(n)[1] - tail_bracket(n)[0]
            == Fraction(2 * n + 1, 2 * n**2 * (n + 1) ** 2)
            for n in indices
        ),
    )
    h.check(
        "doubled bracket is exactly twice the original",
        all(
            doubled_bracket(n)
            == (
                F2 * partial_sum(n) + Fraction(1, (n + 1) ** 2),
                F2 * partial_sum(n) + Fraction(1, n**2),
            )
            for n in indices
        ),
    )
    h.check(
        "lower endpoints strictly increase",
        all(tail_bracket(n + 1)[0] > tail_bracket(n)[0] for n in indices[:-1]),
    )
    h.check(
        "upper endpoints strictly decrease",
        all(tail_bracket(n + 1)[1] < tail_bracket(n)[1] for n in indices[:-1]),
    )
    h.check(
        "every bracket is ordered",
        all(tail_bracket(n)[0] < tail_bracket(n)[1] for n in indices),
    )
    h.check(
        "bracket widths strictly decrease",
        all(
            tail_bracket(n + 1)[1] - tail_bracket(n + 1)[0]
            < tail_bracket(n)[1] - tail_bracket(n)[0]
            for n in indices[:-1]
        ),
    )

    h.banner("T2 exact monomial scaling and normalization")
    grid = rational_grid()
    samples = grid[::4]
    h.check(
        "coefficient is positive on the finite domain",
        all(coefficient(a, t, m, r, s) > F0 for a in samples for t in samples for m in samples for r in samples for s in samples),
    )
    base = (Fraction(2, 3), Fraction(3, 5), Fraction(5, 7), Fraction(7, 11), Fraction(11, 13))
    base_value = coefficient(*base)
    h.check(
        "a scaling law",
        all(coefficient(scale * base[0], *base[1:]) == scale * base_value for scale in grid),
    )
    h.check(
        "t cubic scaling law",
        all(
            coefficient(base[0], scale * base[1], base[2], base[3], base[4])
            == scale**3 * base_value
            for scale in grid
        ),
    )
    h.check(
        "m scaling law",
        all(
            coefficient(base[0], base[1], scale * base[2], base[3], base[4])
            == scale * base_value
            for scale in grid
        ),
    )
    h.check(
        "r inverse scaling law",
        all(
            coefficient(base[0], base[1], base[2], scale * base[3], base[4])
            == base_value / scale
            for scale in grid
        ),
    )
    h.check(
        "s scaling law",
        all(
            coefficient(base[0], base[1], base[2], base[3], scale * base[4])
            == scale * base_value
            for scale in grid
        ),
    )

    second = (Fraction(3, 2), Fraction(5, 3), Fraction(7, 5), Fraction(11, 7), Fraction(13, 11))
    expected_ratio = (
        (second[0] / base[0])
        * (second[1] / base[1]) ** 3
        * (second[2] / base[2])
        * (base[3] / second[3])
        * (second[4] / base[4])
    )
    h.check("complete ratio identity", coefficient(*second) / base_value == expected_ratio)

    fixed = (Fraction(2), Fraction(3), Fraction(5), Fraction(7))
    raw = coefficient(*fixed, F1)
    targets = grid
    normalizations = [target_normalization(*fixed, target) for target in targets]
    h.check("raw example coefficient is 270/7", raw == Fraction(270, 7))
    h.check(
        "normalization reaches every tested target",
        all(coefficient(*fixed, norm) == target for norm, target in zip(normalizations, targets)),
    )
    h.check(
        "normalization is the direct rational solution",
        all(norm == target * fixed[3] / (fixed[0] * fixed[1] ** 3 * fixed[2]) for norm, target in zip(normalizations, targets)),
    )
    h.check(
        "normalization displacement identity",
        all(norm - F1 == (target - raw) / raw for norm, target in zip(normalizations, targets)),
    )
    example_norm = target_normalization(*fixed, Fraction(54))
    h.check("named example normalization is 7/5", example_norm == Fraction(7, 5))
    h.check("named example reaches 54 exactly", coefficient(*fixed, example_norm) == Fraction(54))


def independent_partial_sum(n: int) -> Fraction:
    """Reconstruct S_N through one integer common denominator."""
    index = require_index(n)
    denominator = 1
    for k in range(1, index + 1):
        denominator = lcm(denominator, k**3)
    numerator = sum(denominator // (k**3) for k in range(1, index + 1))
    return Fraction(numerator, denominator)


def integral_x_minus_3(left: int, right: int) -> Fraction:
    if type(left) is not int or type(right) is not int or left < 1 or right <= left:
        raise ValueError("integral endpoints must be integers with 1 <= left < right")
    return Fraction(1, 2 * left**2) - Fraction(1, 2 * right**2)


def independent_checks(h: Harness) -> None:
    source_boundary_checks(h)
    common_api_checks(h)

    h.banner("Independent series reconstruction and integral cells")
    indices = tuple(range(1, 61))
    h.check(
        "primary sums match common-denominator reconstruction",
        all(partial_sum(n) == independent_partial_sum(n) for n in indices),
    )
    h.check(
        "decreasing-cell lower inequalities hold exactly",
        all(integral_x_minus_3(k, k + 1) < Fraction(1, k**3) for k in range(1, 401)),
    )
    h.check(
        "decreasing-cell upper inequalities hold exactly",
        all(Fraction(1, k**3) < integral_x_minus_3(k - 1, k) for k in range(2, 401)),
    )
    finite_pairs = tuple((n, n + offset) for n in range(1, 31) for offset in (1, 5, 30))
    h.check(
        "finite tails dominate telescoped lower integrals",
        all(
            partial_sum(m) - partial_sum(n)
            >= integral_x_minus_3(n + 1, m + 1)
            for n, m in finite_pairs
        ),
    )
    h.check(
        "finite tails are bounded by telescoped upper integrals",
        all(
            partial_sum(m) - partial_sum(n)
            <= integral_x_minus_3(n, m)
            for n, m in finite_pairs
        ),
    )
    h.check(
        "independent lower-tail endpoint formula",
        all(tail_bracket(n)[0] - partial_sum(n) == Fraction(1, 2 * (n + 1) ** 2) for n in indices),
    )
    h.check(
        "independent upper-tail endpoint formula",
        all(tail_bracket(n)[1] - partial_sum(n) == Fraction(1, 2 * n**2) for n in indices),
    )
    h.check(
        "lower nesting numerator is 3N+5",
        all(
            (tail_bracket(n + 1)[0] - tail_bracket(n)[0])
            * (2 * (n + 1) ** 3 * (n + 2) ** 2)
            == 3 * n + 5
            for n in indices
        ),
    )
    h.check(
        "upper nesting numerator is 3N+1",
        all(
            (tail_bracket(n)[1] - tail_bracket(n + 1)[1])
            * (2 * n**2 * (n + 1) ** 3)
            == 3 * n + 1
            for n in indices
        ),
    )

    h.banner("Independent cleared-denominator monomial checks")
    grid = rational_grid()[::4]
    tuples = tuple((a, t, m, r, s) for a in grid for t in grid for m in grid for r in grid for s in grid)
    h.check(
        "coefficient satisfies the cleared defining equation",
        all(coefficient(a, t, m, r, s) * r == a * t**3 * m * s for a, t, m, r, s in tuples),
        f"tuples={len(tuples)}",
    )
    ratio_samples = tuples[::257]
    h.check(
        "independent ratio identity by cross-products",
        all(
            coefficient(*right)
            * left[0]
            * left[1] ** 3
            * left[2]
            * right[3]
            * left[4]
            == coefficient(*left)
            * right[0]
            * right[1] ** 3
            * right[2]
            * left[3]
            * right[4]
            for left, right in zip(ratio_samples, reversed(ratio_samples))
        ),
    )
    fixed = (Fraction(2), Fraction(3), Fraction(5), Fraction(7))
    raw_direct = fixed[0] * fixed[1] ** 3 * fixed[2] / fixed[3]
    h.check("independent raw coefficient", coefficient(*fixed, F1) == raw_direct)
    h.check(
        "normalizer matches direct equation solution",
        all(
            target_normalization(*fixed, target)
            == target * fixed[3] / (fixed[0] * fixed[1] ** 3 * fixed[2])
            for target in rational_grid()
        ),
    )
    h.check(
        "substitution of direct normalizer clears to target",
        all(
            fixed[0]
            * fixed[1] ** 3
            * fixed[2]
            * target_normalization(*fixed, target)
            == target * fixed[3]
            for target in rational_grid()
        ),
    )


def hostile_checks(h: Harness) -> None:
    source_boundary_checks(h)
    common_api_checks(h)

    h.banner("Hostile index and scalar domains")
    for bad in (0, -1):
        h.expect_raises(
            f"partial sum rejects nonpositive index {bad}",
            ValueError,
            lambda bad=bad: partial_sum(bad),
        )
    for bad in (1.0, Fraction(1), "1", None):
        h.expect_raises(
            f"partial sum rejects {type(bad).__name__}",
            TypeError,
            lambda bad=bad: partial_sum(bad),
        )

    bad_scalars: tuple[object, ...] = (0, True, 1.0, "1", None, FractionSubclass(1))
    for index, bad in enumerate(bad_scalars):
        for position in range(5):
            values: list[object] = [F1, F1, F1, F1, F1]
            values[position] = bad
            h.expect_raises(
                f"coefficient rejects malformed scalar #{index} at position {position}",
                TypeError,
                lambda values=values: coefficient(*values),
            )

    for bad in (F0, -F1):
        for position in range(5):
            values = [F1, F1, F1, F1, F1]
            values[position] = bad
            h.expect_raises(
                f"coefficient rejects nonpositive scalar {bad} at position {position}",
                ValueError,
                lambda values=values: coefficient(*values),
            )
        h.expect_raises(
            f"normalizer rejects nonpositive target {bad}",
            ValueError,
            lambda bad=bad: target_normalization(F1, F1, F1, F1, bad),
        )

    h.banner("Hostile theorem spot checks")
    h.check("hostile S_3 exact value", partial_sum(3) == Fraction(251, 216))
    h.check(
        "hostile N=2 exact bracket",
        tail_bracket(2) == (Fraction(9, 8) + Fraction(1, 18), Fraction(9, 8) + Fraction(1, 8)),
    )
    fixed = (Fraction(2), Fraction(3), Fraction(5), Fraction(7))
    h.check("hostile coefficient example", coefficient(*fixed, F1) == Fraction(270, 7))
    h.check("hostile normalizer example", target_normalization(*fixed, Fraction(54)) == Fraction(7, 5))
    h.check(
        "hostile normalized coefficient reaches target",
        coefficient(*fixed, target_normalization(*fixed, Fraction(54))) == Fraction(54),
    )


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--independent", action="store_true", help="use independent exact reconstructions")
    mode.add_argument("--hostile", action="store_true", help="exercise hostile input and scope guards")
    parser.add_argument(
        "--mutate",
        action="append",
        default=[],
        choices=(*MUTATION_NAMES, "all"),
        help="activate a fail-closed mutation fixture (repeatable)",
    )
    parser.add_argument("--list-mutations", action="store_true", help="print mutation names and exit")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    global MUTATIONS
    args = parse_args(argv)
    if args.list_mutations:
        print("\n".join(MUTATION_NAMES))
        return 0
    selected = set(args.mutate)
    if "all" in selected:
        selected = set(MUTATION_NAMES)
    MUTATIONS = frozenset(selected)

    mode = "hostile" if args.hostile else "independent" if args.independent else "normal"
    print("=" * 88)
    print("Cubic-reciprocal series bounds and rational normalization")
    print(f"MODE={mode}")
    print(f"MUTATIONS={','.join(sorted(MUTATIONS)) if MUTATIONS else 'none'}")
    print("=" * 88)

    h = Harness()
    if args.hostile:
        hostile_checks(h)
    elif args.independent:
        independent_checks(h)
    else:
        normal_checks(h)

    print()
    print("=" * 88)
    print(f"SUMMARY: PASS={h.passed} FAIL={h.failed}")
    print(f"PASSED: {h.passed}/{h.passed + h.failed}")
    print("=" * 88)
    if h.failed:
        print("RATIONAL_SERIES_NORMALIZATION_POSITIVE_THEOREM=FALSE")
        return 1
    print("RATIONAL_SERIES_NORMALIZATION_POSITIVE_THEOREM=TRUE")
    print("EXACT_ARITHMETIC=TRUE")
    print("DEPENDENCIES=NONE")
    print("PHYSICAL_INTERPRETATION_ASSERTED=FALSE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
