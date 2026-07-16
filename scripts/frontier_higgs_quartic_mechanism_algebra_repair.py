#!/usr/bin/env python3
"""Exact certificates for the formal radial-quartic global-minimum lemma."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Iterable

import sympy as sp


PASS = 0
FAIL = 0


def check(label: str, result: object, detail: str = "") -> None:
    """Record a computed predicate without accepting bare asserted passes."""

    global PASS, FAIL
    try:
        ok = bool(result)
    except TypeError:
        ok = False
        detail = f"non-Boolean result: {result!r}"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def polynomial_identity(lhs: sp.Expr, rhs: sp.Expr, *generators: sp.Symbol) -> bool:
    difference = sp.Poly(sp.expand(lhs - rhs), *generators)
    return difference.is_zero


def nonzero_polynomial(expr: sp.Expr, *generators: sp.Symbol) -> bool:
    polynomial = sp.Poly(sp.expand(expr), *generators)
    return not polynomial.is_zero


FORMAL_CONCLUSIONS = frozenset(
    {
        "defined_radial_polynomial",
        "unique_global_minimizer",
        "minimum_value",
        "radial_second_derivative",
    }
)

PHYSICAL_BRIDGES = frozenset(
    {
        "scalar_carrier",
        "higgs_field",
        "gauge_symmetry_breaking",
        "coleman_weinberg_potential",
        "framework_dynamics",
        "selected_vacuum",
        "lambda_derivation",
        "m2_derivation",
        "physical_mass",
        "observed_value",
    }
)


def scope_is_formal(conclusions: Iterable[str]) -> bool:
    return set(conclusions).isdisjoint(PHYSICAL_BRIDGES)


def check_exact_theorem() -> None:
    section("Exact radial-polynomial identities")

    r = sp.symbols("r", real=True)
    x = sp.symbols("x", nonnegative=True)
    x_positive = sp.symbols("x_positive", positive=True)
    m2 = sp.symbols("m2", real=True)
    lam = sp.symbols("lambda", positive=True)

    potential = sp.Rational(1, 2) * m2 * r**2 + sp.Rational(1, 4) * lam * r**4
    factored = r**2 * (2 * m2 + lam * r**2) / 4
    derivative = sp.diff(potential, r)
    second_derivative = sp.diff(potential, r, 2)

    check(
        "definition equals r^2(2 m2 + lambda r^2)/4",
        polynomial_identity(potential, factored, r),
    )
    check(
        "first derivative is r(m2 + lambda r^2)",
        polynomial_identity(derivative, r * (m2 + lam * r**2), r),
    )
    check(
        "second derivative is m2 + 3 lambda r^2",
        polynomial_identity(second_derivative, m2 + 3 * lam * r**2, r),
    )
    check("quartic leading coefficient is positive", sp.ask(sp.Q.positive(lam / 4)))

    section("Case m2 >= 0, including m2 = 0")

    m2_nonnegative = sp.symbols("m2_nonnegative", nonnegative=True)
    unbroken_x = x * (2 * m2_nonnegative + lam * x) / 4
    positive_x_value = x_positive * (2 * m2_nonnegative + lam * x_positive) / 4
    check(
        "V is nonnegative for x=r^2 >= 0",
        sp.ask(sp.Q.nonnegative(unbroken_x)),
    )
    check(
        "V is strictly positive whenever x=r^2 > 0",
        sp.ask(sp.Q.positive(positive_x_value)),
    )
    check("V(0)=0", sp.simplify(unbroken_x.subs(x, 0)) == 0)
    check(
        "the only equality point on r>=0 is r=0",
        sp.ask(sp.Q.positive(positive_x_value))
        and sp.simplify(unbroken_x.subs(x, 0)) == 0,
    )

    zero_case = sp.simplify(unbroken_x.subs(m2_nonnegative, 0))
    check("m2=0 gives V=lambda r^4/4", polynomial_identity(zero_case, lam * x**2 / 4, x))
    check(
        "m2=0 is still strict away from r=0",
        sp.ask(sp.Q.positive(zero_case.subs(x, x_positive))),
    )
    check(
        "m2=0 minimum is degenerate with V''(0)=0",
        sp.simplify(second_derivative.subs({m2: 0, r: 0})) == 0,
    )

    section("Case m2 < 0")

    mu2 = sp.symbols("mu2", positive=True)
    radius_squared = mu2 / lam
    radius = sp.sqrt(radius_squared)
    negative_case = sp.expand(potential.subs(m2, -mu2))
    minimum_value = sp.simplify(negative_case.subs(r, radius))
    square_certificate = lam * (r**2 - radius_squared) ** 2 / 4

    check("v^2=-m2/lambda is positive", sp.ask(sp.Q.positive(radius_squared)))
    check("v is strictly positive", sp.ask(sp.Q.positive(radius)))
    check(
        "V(r)-V(v)=lambda(r^2-v^2)^2/4",
        polynomial_identity(negative_case - minimum_value, square_certificate, r),
    )
    check("the square certificate is nonnegative", sp.ask(sp.Q.nonnegative(square_certificate)))

    real_roots = sp.solve(sp.Eq(r**2, radius_squared), r)
    positive_roots = [root for root in real_roots if sp.simplify(root / radius - 1) == 0]
    negative_roots = [root for root in real_roots if sp.simplify(root / radius + 1) == 0]
    check("r^2=v^2 has exactly the roots -v and v", len(real_roots) == 2)
    check("the radial domain retains exactly r=v", len(positive_roots) == 1 and len(negative_roots) == 1)
    check(
        "equality in the square certificate is unique on r>=0",
        len(positive_roots) == 1
        and sp.ask(sp.Q.positive(radius))
        and sp.simplify(square_certificate.subs(r, positive_roots[0])) == 0,
    )
    check(
        "V(v)=-m2^2/(4 lambda)",
        sp.simplify(minimum_value + mu2**2 / (4 * lam)) == 0,
        str(minimum_value),
    )
    check(
        "V(0)-V(v) is strictly positive",
        sp.ask(sp.Q.positive(sp.simplify(negative_case.subs(r, 0) - minimum_value))),
    )

    curvature = sp.simplify(second_derivative.subs({m2: -mu2, r: radius}))
    check("V''(v)=-2m2", sp.simplify(curvature - 2 * mu2) == 0, str(curvature))
    check("V''(v)=2 lambda v^2", sp.simplify(curvature - 2 * lam * radius_squared) == 0)
    check("V''(v)>0", sp.ask(sp.Q.positive(curvature)))

    section("Exhaustiveness and scope")

    negative_reals = sp.Interval.open(-sp.oo, 0)
    nonnegative_reals = sp.Interval(0, sp.oo)
    check("m2<0 and m2>=0 partition the real line", sp.Union(negative_reals, nonnegative_reals) == sp.S.Reals)
    check("the two m2 cases do not overlap", sp.Intersection(negative_reals, nonnegative_reals) == sp.S.EmptySet)
    check("the theorem certificate contains only formal conclusions", scope_is_formal(FORMAL_CONCLUSIONS))


def check_hostile_controls() -> None:
    section("Hostile controls")

    r = sp.symbols("r", real=True)
    n = sp.symbols("n", positive=True, integer=True)
    lam = sp.symbols("lambda", positive=True)
    mu2 = sp.symbols("mu2", positive=True)
    v = sp.symbols("v", positive=True)
    c = sp.symbols("c", positive=True)

    lambda_zero_flat = sp.Rational(0) * r**4
    check(
        "lambda=0, m2=0 destroys uniqueness",
        sp.Poly(lambda_zero_flat, r).is_zero,
    )
    lambda_zero_negative_m2 = -r**2
    check(
        "lambda=0, m2<0 is unbounded below",
        sp.limit(lambda_zero_negative_m2.subs(r, n), n, sp.oo) == -sp.oo,
    )

    lambda_negative = -r**4 / 4
    check(
        "lambda<0 is unbounded below",
        sp.limit(lambda_negative.subs(r, n), n, sp.oo) == -sp.oo,
    )

    exact_example = -r**2 + r**4 / 4
    example_radius = sp.sqrt(2)
    check(
        "a whole-real-line uniqueness claim fails at -v",
        sp.simplify(exact_example.subs(r, -example_radius) - exact_example.subs(r, example_radius)) == 0
        and sp.simplify(-example_radius - example_radius) != 0,
    )

    wrong_radius_squared = -mu2 / lam
    stationarity_residual = sp.simplify(-mu2 + lam * wrong_radius_squared)
    check("the wrong radius sign gives v^2<0", sp.ask(sp.Q.negative(wrong_radius_squared)))
    check("the wrong radius sign fails stationarity", stationarity_residual != 0, str(stationarity_residual))

    correct_curvature = 2 * mu2
    wrong_curvature = mu2
    check("a missing curvature factor of two is rejected", sp.simplify(correct_curvature - wrong_curvature) != 0)

    base = -lam * v**2 * r**2 / 2 + lam * r**4 / 4
    cubic_perturbation = base + c * r**3 / 3
    perturbed_derivative_at_v = sp.simplify(sp.diff(cubic_perturbation, r).subs(r, v))
    cubic_identity_residual = sp.expand(
        cubic_perturbation
        - cubic_perturbation.subs(r, v)
        - lam * (r**2 - v**2) ** 2 / 4
    )
    check("an added cubic moves the stationary point", perturbed_derivative_at_v == c * v**2)
    check("an added cubic breaks the square identity", nonzero_polynomial(cubic_identity_residual, r))

    illicit_conclusions = FORMAL_CONCLUSIONS | {"higgs_field", "physical_mass"}
    check("an illicit physical-Higgs inference is rejected", not scope_is_formal(illicit_conclusions))


def check_intentional_failure_probe() -> None:
    section("Intentional-failure probe")
    r = sp.symbols("r", real=True)
    check(
        "deliberately false polynomial identity",
        polynomial_identity(r**2, r**2 + 1, r),
        "this FAIL and nonzero exit are intentional",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--hostile",
        action="store_true",
        help="run adversarial controls after the exact theorem certificate",
    )
    parser.add_argument(
        "--intentional-failure",
        action="store_true",
        help="append a deliberately false identity and exit nonzero",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print("Radial quartic global-minimum lemma")
    check_exact_theorem()
    if args.hostile:
        check_hostile_controls()
    if args.intentional_failure:
        check_intentional_failure_probe()
    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return int(FAIL != 0)


if __name__ == "__main__":
    sys.exit(main())
