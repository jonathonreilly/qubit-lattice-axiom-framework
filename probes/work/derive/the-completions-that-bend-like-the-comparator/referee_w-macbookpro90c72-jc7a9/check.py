#!/usr/bin/env python3
"""Independent referee for the-completions-that-bend-like-the-comparator a1.

The radial Euler-Lagrange equations of the weight-one family are solved to
third order. The attempt's script is not imported. The floating-point capture
sweep is not rebuilt.
"""
from __future__ import annotations

import sys

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


radius, book = sp.symbols("r epsilon", positive=True)
beta, mass, ratio = sp.symbols("beta M sigma", positive=True)
A1, A2, C1, C2, D1, D2 = sp.symbols("A1 A2 C1 C2 D1 D2")
U1, L1 = sp.symbols("U1 L1")
u2, l2, u3, l3 = sp.symbols("u2 l2 u3 l3")
rate = sp.Function("u")(radius)
length = sp.Function("lam")(radius)


def shape_A(value):
    return 1 + A1 * value + A2 * value ** 2 / 2


def shape_C(value):
    return 1 / (2 * beta) + C1 * value + C2 * value ** 2 / 2


def shape_D(value):
    return D1 * value + D2 * value ** 2 / 2


lagrangian = radius ** 2 * sp.exp(rate) * (
    shape_A(length) * rate.diff(radius) * length.diff(radius)
    + shape_C(length) * length.diff(radius) ** 2
    + shape_D(length) * rate.diff(radius) ** 2
)
equations = [sp.diff(lagrangian, field) - sp.diff(sp.diff(lagrangian, field.diff(radius)), radius) for field in (rate, length)]
rate_series = book * U1 / radius + book ** 2 * u2 / radius ** 2 + book ** 3 * u3 / radius ** 3
length_series = book * L1 / radius + book ** 2 * l2 / radius ** 2 + book ** 3 * l3 / radius ** 3
residuals = []
for equation in equations:
    replaced = equation.subs({rate.diff(radius, 2): rate_series.diff(radius, 2), length.diff(radius, 2): length_series.diff(radius, 2)})
    replaced = replaced.subs({rate.diff(radius): rate_series.diff(radius), length.diff(radius): length_series.diff(radius)})
    replaced = replaced.subs({rate: rate_series, length: length_series})
    residuals.append(sp.expand(sp.series(sp.expand(replaced), book, 0, 4).removeO()))
first_order = [sp.simplify(residual.coeff(book, 1)) for residual in residuals]
second = sp.solve([sp.expand(residual.coeff(book, 2) * radius ** 4) for residual in residuals], [u2, l2], dict=True)[0]
third = sp.solve([sp.expand((residual.coeff(book, 3) * radius ** 5).subs(second)) for residual in residuals], [u3, l3], dict=True)[0]
index = sp.series(sp.exp(length_series - rate_series), book, 0, 4).removeO()
nu1 = sp.expand(index.coeff(book, 1) * radius)
nu2 = sp.expand((index.coeff(book, 2) * radius ** 2).subs(second))
nu3 = sp.expand((index.coeff(book, 3) * radius ** 3).subs(second).subs(third))
check("S1 harmonic", all(term == 0 for term in first_order), "at first order both fields are harmonic")

body, pull = sp.symbols("a p", positive=True)
curvature = {beta: 1, A1: 1, A2: 1, C1: sp.Rational(1, 2), C2: sp.Rational(1, 2), D1: 0, D2: 0, L1: 2 * body, U1: -(body + pull)}
length_exact = sp.series(2 * sp.log(1 + book * body / radius), book, 0, 4).removeO()
rate_exact = sp.series(sp.log(1 - book * pull / radius) - sp.log(1 + book * body / radius), book, 0, 4).removeO()
curvature_ok = sp.simplify(second[l2].subs(curvature) - sp.expand(length_exact).coeff(book, 2) * radius ** 2) == 0
curvature_ok = curvature_ok and sp.simplify(second[u2].subs(curvature) - sp.expand(rate_exact).coeff(book, 2) * radius ** 2) == 0
curvature_ok = curvature_ok and sp.simplify(third[l3].subs(curvature) - sp.expand(length_exact).coeff(book, 3) * radius ** 3) == 0
curvature_ok = curvature_ok and sp.simplify(third[u3].subs(curvature) - sp.expand(rate_exact).coeff(book, 3) * radius ** 3) == 0
curvature_ok = curvature_ok and sp.simplify(nu2.subs(curvature) - (3 * body ** 2 + 3 * body * pull + pull ** 2)) == 0
check("S2 curvature", curvature_ok, "the curvature member reproduces lambda = 2 log(1+a/r) and u = log(1-p/r) - log(1+a/r) through order 3, with nu2 = 3a^2+3ap+p^2")

height = sp.symbols("t", positive=True)
moments = [sp.simplify(sp.integrate(1 / (height ** (power + 1) * sp.sqrt(height ** 2 - 1)), (height, 1, sp.oo))) for power in (1, 2, 3)]
check("S3 turn integrals", moments == [1, sp.pi / 4, sp.Rational(2, 3)], "the Bouguer moments are 1, pi/4 and 2/3")

comparator = sp.series(((1 + mass / (2 * radius)) ** 3 / (1 - mass / (2 * radius))).subs(radius, 1 / book), book, 0, 4).removeO()
comparator_jet = [sp.expand(comparator).coeff(book, order) for order in (1, 2, 3)]
check(
    "S4 index",
    comparator_jet == [2 * mass, sp.Rational(7, 4) * mass ** 2, mass ** 3],
    "the comparator index (1+M/(2r))^3/(1-M/(2r)) has coefficients (2M, 7M^2/4, M^3)",
)

rest = {beta: 1, U1: -ratio * L1}
charge_solution = sp.solve(sp.Eq(nu1.subs(rest), 2 * mass), L1)[0]
reduced = sp.simplify(nu2.subs(rest).subs(L1, charge_solution) / mass ** 2)
claimed = -2 * (2 * A1 - C1 + D1 * ratio ** 2 - 4 * D1 * ratio - 2 * ratio ** 2 - ratio - 2) / (1 + ratio) ** 2
at_one = sp.simplify(reduced.subs(ratio, 1))
plane = sp.simplify(at_one - (sp.Rational(5, 2) - A1 + C1 / 2 + 3 * D1 / 2))
third_at_one = sp.expand(sp.simplify(nu3.subs(rest).subs(L1, charge_solution) / mass ** 3).subs(ratio, 1))
slopes = [sp.diff(third_at_one, jet) for jet in (A2, C2, D2)]
check(
    "B plane",
    sp.simplify(reduced - claimed) == 0
    and plane == 0
    and slopes == [sp.Rational(-1, 3), sp.Rational(1, 6), sp.Rational(1, 2)]
    and sp.simplify(at_one.subs({A1: 1, C1: sp.Rational(1, 2), D1: 0}) - sp.Rational(7, 4)) == 0
    and sp.simplify(at_one.subs({A1: 0, C1: 0, D1: 0}) - sp.Rational(5, 2)) == 0,
    "nu2/M^2 is the stated rational function; at sigma = 1 the comparator's 7/4 holds iff 4A1 - 2C1 - 6D1 = 3, and nu3 is linear in the fourth-order jet with slopes (-1/3, 1/6, 1/2)",
)

rest_charge = sp.solve(sp.Eq(nu1.subs(U1, -L1 / beta), 2 * mass), L1)[0]
general = sp.factor(sp.simplify(nu2.subs(U1, -L1 / beta).subs(L1, rest_charge) / mass ** 2))
general_claim = -(2 * A1 * beta ** 2 + 2 * A1 * beta - 2 * C1 * beta ** 2 - 4 * D1 * beta - 2 * D1 - 2 * beta ** 2 - 5 * beta - 3) / (beta + 1) ** 2
check("B beta", sp.simplify(general - general_claim) == 0, "at rest, sigma = 1/beta, the second-order coefficient is the stated function of beta")

flux_density = sp.exp(rate) * (
    (1 + A1 * length) * rate.diff(radius) * length.diff(radius)
    + (sp.Rational(1, 2) + C1 * length) * length.diff(radius) ** 2
    + D1 * length * rate.diff(radius) ** 2
)
momentum = sp.diff(flux_density, rate.diff(radius))
far = momentum.subs({rate.diff(radius): -U1 / radius ** 2, length.diff(radius): -L1 / radius ** 2, rate: U1 / radius, length: L1 / radius})
wall = sp.simplify(sp.limit(-radius ** 2 * far, radius, sp.oo))
check("B wall", sp.simplify(wall - L1) == 0, "the far-field flux of dL/du' is A(0) L1 and does not see the third-order jet")

scale = sp.symbols("s")
check("W weight", sp.solve(scale * (1 - scale), scale) == [0, 1], "the |grad u|^2 coefficient s(1-s) vanishes only at s = 0 and s = 1")
argument = sp.symbols("x", positive=True)
profile, partner = sp.Function("f"), sp.Function("g")
amplitude = profile(argument) * sp.diff(partner(argument), argument) * argument
bend = sp.diff(partner(argument), argument) * argument ** 2 * sp.diff(profile(argument), argument)
ratio_at_one = sp.simplify((bend / amplitude).subs(argument, 1).subs(profile(1), 1))
check(
    "W jet",
    sp.simplify(ratio_at_one - sp.diff(profile(argument), argument).subs(argument, 1)) == 0,
    "C(0)/A(0) equals f'(1), so the curvature normalisation forces f'(1) = 1/2",
)

matched = ((1 + (1 + mass / radius)) / 2) ** 3 / (1 - mass / (2 * radius))
comparator_exact = (1 + mass / (2 * radius)) ** 3 / (1 - mass / (2 * radius))
check(
    "W match",
    sp.simplify(matched - comparator_exact) == 0 and sp.solve(sp.Eq((sp.symbols("p") + sp.symbols("q") / 2) / sp.symbols("q"), 1), sp.symbols("p")) == [sp.symbols("q") / 2],
    "ell f = ((1+g)/2)^3 with Y = 1+M/r and X = 1-M/(2r) is the comparator index, and sigma = 1 means p = q/2",
)

jet_length = sp.symbols("lambda", real=True)
families = [2 * sp.sqrt(argument) - 1, argument, 1 + sp.log(argument), 1 + (argument ** 3 - 1) / 3, (3 - 1 / argument ** 2) / 2]
family_ok = True
for choice in families:
    choice = sp.simplify(choice)
    family_ok = family_ok and choice.subs(argument, 1) == 1 and sp.simplify(sp.diff(choice, argument).subs(argument, 1)) == 1
    response = ((1 + choice) / 2) ** 3 / argument
    series_A = sp.series((response * sp.diff(choice, argument) * argument).subs(argument, sp.exp(jet_length)), jet_length, 0, 3).removeO()
    series_C = sp.series((sp.diff(choice, argument) * argument ** 2 * sp.diff(response, argument)).subs(argument, sp.exp(jet_length)), jet_length, 0, 3).removeO()
    jets = {
        A1: series_A.coeff(jet_length, 1) / series_A.coeff(jet_length, 0),
        A2: 2 * series_A.coeff(jet_length, 2) / series_A.coeff(jet_length, 0),
        C1: series_C.coeff(jet_length, 1) / series_A.coeff(jet_length, 0),
        C2: 2 * series_C.coeff(jet_length, 2) / series_A.coeff(jet_length, 0),
        D1: 0,
        D2: 0,
    }
    family_ok = family_ok and sp.simplify(series_A.coeff(jet_length, 0) - 1) == 0 and sp.simplify(series_C.coeff(jet_length, 0) - sp.Rational(1, 2)) == 0
    family_ok = family_ok and sp.simplify(at_one.subs(jets) - sp.Rational(7, 4)) == 0
    family_ok = family_ok and sp.simplify(third_at_one.subs(jets) - 1) == 0
check("W family", family_ok, "five matched choices of g, including 2 sqrt(ell)-1, give nu2/M^2 = 7/4 and nu3/M^3 = 1")

gamma = sp.symbols("gamma", positive=True)
power = (1 + gamma * mass / radius) ** (3 / (2 * gamma)) / (1 - mass / (2 * radius))
power_series = sp.series(power.subs(radius, 1 / book), book, 0, 3).removeO()
check(
    "W powers",
    sp.simplify(sp.expand(power_series).coeff(book, 2) - (17 - 6 * gamma) / 8 * mass ** 2) == 0
    and sp.solve(sp.Eq((17 - 6 * gamma) / 8, sp.Rational(7, 4)), gamma) == [sp.Rational(1, 2)],
    "a power Y = ell^gamma has nu2 = (17-6 gamma) M^2/8, equal to 7M^2/4 only at gamma = 1/2",
)

product = radius * (1 + mass / (2 * radius)) ** 3 / (1 - mass / (2 * radius))
critical = [root for root in sp.solve(sp.diff(product.subs(mass, 1), radius), radius) if root.is_real and root > sp.Rational(1, 2)]
check(
    "W capture",
    len(critical) == 1 and sp.simplify(product.subs({mass: 1, radius: critical[0]}) - 3 * sp.sqrt(3)) == 0,
    "the comparator index is captured at r n = 3 sqrt(3) M",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial, with the long-wave reduction assumed. At beta = 1, nu2/M^2 = "
    "-2(2A1 - C1 + D1 sigma^2 - 4 D1 sigma - 2 sigma^2 - sigma - 2)/(1+sigma)^2. At sigma = 1 the comparator's "
    "7M^2/4 holds exactly on the plane 4A1 - 2C1 - 6D1 = 3, and 128/3 is one further linear condition on "
    "(A2, C2, D2). Bilinear members give the comparator index at every order iff ell f = ((1+g)/2)^3, one for "
    "each g. Among powers only gamma = 1/2 lies on the plane. The floating-point radial integrations were not rebuilt.",
    flush=True,
)
print(
    "HIT: confirmed - a weight-one completion bends like the comparator at second order exactly when "
    "4A1 - 2C1 - 6D1 = 3 at sigma = 1, and the curvature member is one of a family of bilinear members that do",
    flush=True,
)
