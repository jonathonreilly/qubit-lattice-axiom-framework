#!/usr/bin/env python3
"""Independent referee for the curvature member, attempt 2.

The turn coefficients, the capture discriminant, and the 7^3 boxes are
recomputed. The attempt's script is not imported. The coefficient ratio
scan and the monotonicity grid were not rebuilt.
"""
from __future__ import annotations

import random
from fractions import Fraction as F

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def turn_weight(order: int):
    return sp.simplify(sp.sqrt(sp.pi) * sp.gamma(sp.Rational(order + 1, 2)) / sp.gamma(sp.Rational(order, 2) + 1))


def beta_integral(order: int):
    height = sp.symbols("y", positive=True)
    return sp.simplify(2 * sp.integrate(height ** order / sp.sqrt(1 - height ** 2), (height, 0, 1)))


def weights() -> bool:
    listed = [2, sp.pi / 2, sp.Rational(4, 3), 3 * sp.pi / 8, sp.Rational(16, 15), 5 * sp.pi / 16]
    return all(sp.simplify(turn_weight(order) - listed[order - 1]) == 0 and sp.simplify(beta_integral(order) - listed[order - 1]) == 0 for order in range(1, 7))


def coefficient(series, power, degree=None):
    symbol = sp.symbols("u") if degree is None else degree
    return sp.series(series, symbol, 0, power + 1).removeO().coeff(symbol, power)


def generic_orders() -> bool:
    degree = sp.symbols("u")
    slopes = sp.symbols("nu1:6")
    index = 1 + sum(slopes[k - 1] * degree ** k for k in range(1, 6))
    order1 = 2 * slopes[0]
    order2 = sp.pi * (slopes[1] + slopes[0] ** 2 / 2)
    order3 = sp.Rational(4, 3) * (slopes[0] ** 3 + 6 * slopes[0] * slopes[1] + 3 * slopes[2])
    order4 = 3 * sp.pi / 8 * (slopes[0] ** 4 + 12 * slopes[0] ** 2 * slopes[1] + 12 * slopes[0] * slopes[2] + 6 * slopes[1] ** 2 + 4 * slopes[3])
    order5 = sp.Rational(16, 15) * (
        slopes[0] ** 5 + 20 * slopes[0] ** 3 * slopes[1] + 30 * slopes[0] ** 2 * slopes[2] + 30 * slopes[0] * slopes[1] ** 2
        + 20 * slopes[0] * slopes[3] + 20 * slopes[1] * slopes[2] + 5 * slopes[4]
    )
    targets = [order1, order2, order3, order4, order5]
    good = True
    for order, target in enumerate(targets, start=1):
        got = sp.expand(turn_weight(order) * coefficient(index ** order, order))
        good = good and sp.expand(got - target) == 0
    return good


def multiply(left, right, order):
    out = [F(0) for _ in range(order + 1)]
    for i, value in enumerate(left):
        for j, other in enumerate(right):
            if i + j <= order:
                out[i + j] += value * other
    return out


def compose_index(coefficients, series, order):
    out = [F(0) for _ in range(order + 1)]
    power = [F(1)] + [F(0)] * order
    for coefficient_value in coefficients:
        for degree, term in enumerate(power):
            out[degree] += coefficient_value * term
        power = multiply(power, series, order)
    return out


def logarithm(series, order):
    # log(1+X) with X starting at order 1
    out = [F(0) for _ in range(order + 1)]
    power = series[:]
    sign = 1
    for step in range(1, order + 1):
        for degree, term in enumerate(power):
            out[degree] += F(sign, step) * term
        power = multiply(power, series, order)
        sign = -sign
    return out


def power_coefficient(coefficients, order):
    degree = sp.symbols("u")
    index = sum(coefficients[k] * degree ** k for k in range(len(coefficients)))
    return sp.series(index ** order, degree, 0, order + 1).removeO().coeff(degree, order)


def lagrange(order: int = 10) -> bool:
    rng = random.Random(20260926)
    samples = []
    for _ in range(4):
        samples.append([F(1)] + [F(rng.randint(-3, 3), rng.randint(1, 4)) for _ in range(6)])
    slope, charge = sp.Rational(2, 7), sp.Rational(3, 5)
    member = [sp.series(((1 + slope * sp.symbols("u")) ** 3 / (1 - charge * sp.symbols("u"))), sp.symbols("u"), 0, order + 1).removeO().coeff(sp.symbols("u"), k) for k in range(order + 1)]
    samples.append([F(term) for term in member])
    good = True
    for coefficients in samples:
        series = [F(0), F(1)] + [F(0)] * (order - 1)
        for _ in range(order + 1):
            image = compose_index(coefficients, series, order)
            series = [F(0)] + image[:order]
        image = compose_index(coefficients, series, order)
        logged = logarithm([image[k] - (1 if k == 0 else 0) for k in range(order + 1)], order)
        for degree in range(1, order + 1):
            expected = F(power_coefficient(coefficients, degree)) / degree
            good = good and logged[degree] == expected
    return good


def member_sum(order, slope, charge):
    total = 0
    for index in range(order + 1):
        total += sp.binomial(3 * order, order - index) * sp.binomial(order + index - 1, index) * slope ** (order - index) * charge ** index
    return sp.expand(total)


def member() -> bool:
    slope, charge, degree = sp.symbols("a p u", positive=True)
    index = (1 + slope * degree) ** 3 / (1 - charge * degree)
    good = all(sp.expand(member_sum(order, slope, charge) - coefficient(index ** order, order, degree)) == 0 for order in range(1, 9))
    mass, ratio = sp.symbols("M rho", positive=True)
    scale = 2 * mass / (3 + ratio)
    second = sp.simplify(turn_weight(2) * member_sum(2, scale, ratio * scale) / mass ** 2)
    third = sp.simplify(turn_weight(3) * member_sum(3, scale, ratio * scale) / mass ** 3)
    good = good and sp.simplify(second - 6 * sp.pi * (5 + 4 * ratio + ratio ** 2) / (3 + ratio) ** 2) == 0
    good = good and sp.simplify(third - sp.Rational(64, 3) * (42 + 54 * ratio + 27 * ratio ** 2 + 5 * ratio ** 3) / (3 + ratio) ** 3) == 0
    good = good and third.subs(ratio, 0) == sp.Rational(896, 27) and third.subs(ratio, 1) == sp.Rational(128, 3)
    equal = [sp.simplify(turn_weight(order) * member_sum(order, mass / 2, mass / 2) / mass ** order) for order in range(1, 7)]
    listed = [4, 15 * sp.pi / 4, sp.Rational(128, 3), 3465 * sp.pi / 64, sp.Rational(3584, 5), 255255 * sp.pi / 256]
    return good and all(sp.simplify(got - want) == 0 for got, want in zip(equal, listed))


def capture() -> bool:
    slope, charge, impact, degree = sp.symbols("a p b u", positive=True)
    cubic = sp.expand((1 + slope * degree) ** 3 - impact * degree * (1 - charge * degree))
    discriminant = sp.discriminant(sp.Poly(cubic, degree))
    mass, ratio, root = sp.symbols("M rho s", positive=True)
    scale = 2 * mass / (3 + ratio)
    closed = 2 * mass * (ratio + root + 2) ** 3 / ((ratio + 3) * (root + 1) * (ratio + root + 1))
    numerator = sp.numer(sp.together(discriminant.subs({slope: scale, charge: ratio * scale, impact: closed})))
    reduced = sp.rem(sp.Poly(sp.expand(numerator), root), sp.Poly(root ** 2 - ratio ** 2 - ratio - 1, root))
    gap = sp.sqrt(slope ** 2 + slope * charge + charge ** 2)
    radius = slope + charge + gap
    turning = 1 / radius
    threshold = (radius + slope) ** 3 / (radius * (radius - charge))
    double = sp.simplify(cubic.subs({degree: turning, impact: threshold})) == 0
    derivative = sp.simplify(sp.diff(cubic, degree).subs({degree: turning, impact: threshold})) == 0
    values = []
    for sample in (0, sp.Rational(1, 2), 1, 3):
        values.append(sp.simplify((closed / mass).subs({ratio: sample, root: sp.sqrt(sample ** 2 + sample + 1)})))
    targets = [sp.Rational(9, 2), 4 * sp.sqrt(7) - sp.Rational(40, 7), 3 * sp.sqrt(3), (70 + 26 * sp.sqrt(13)) / 27]
    limit = sp.limit((closed / mass).subs(root, sp.sqrt(ratio ** 2 + ratio + 1)), ratio, sp.oo)
    weight = degree * (1 - charge * degree) / (1 + slope * degree) ** 3
    derivative_weight = sp.factor(sp.diff(weight, degree))
    return (
        sp.expand(reduced.as_expr()) == 0
        and double
        and derivative
        and all(sp.simplify(got - want) == 0 for got, want in zip(values, targets))
        and limit == 8
        and sp.simplify(derivative_weight * (1 + slope * degree) ** 4 - (1 - 2 * (slope + charge) * degree + slope * charge * degree ** 2)) == 0
    )


def solve(matrix, rhs):
    rows = [row[:] + [rhs[index]] for index, row in enumerate(matrix)]
    size = len(rhs)
    for column in range(size):
        pivot = next(row for row in range(column, size) if rows[row][column] != 0)
        rows[column], rows[pivot] = rows[pivot], rows[column]
        scale = rows[column][column]
        rows[column] = [entry / scale for entry in rows[column]]
        for row in range(size):
            if row == column or rows[row][column] == 0:
                continue
            factor = rows[row][column]
            rows[row] = [entry - factor * rows[column][index] for index, entry in enumerate(rows[row])]
    return [rows[index][size] for index in range(size)]


def configure(side, sources, bonds):
    eight_k = F(1)
    interior = [(i, j, k) for i in range(1, side - 1) for j in range(1, side - 1) for k in range(1, side - 1)]
    index = {site: number for number, site in enumerate(interior)}
    steps = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

    def neighbours(site):
        return [(site[0] + step[0], site[1] + step[1], site[2] + step[2]) for step in steps]

    count = len(interior)
    matrix = [[F(0) for _ in range(count)] for _ in range(count)]
    for site in interior:
        row = index[site]
        for other in neighbours(site):
            matrix[row][row] -= 1
            if other in index:
                matrix[row][index[other]] += 1
    chi_rhs = [-sources.get(site, F(0)) - sum(1 for other in neighbours(site) if other not in index) for site in interior]
    chi = solve(matrix, chi_rhs)
    content = {site: F(0) for site in interior}
    for (left, right), energy in bonds.items():
        if left in index:
            content[left] += energy / 2
        if right in index:
            content[right] += energy / 2
    clock_matrix = [row[:] for row in matrix]
    for site in interior:
        clock_matrix[index[site]][index[site]] -= sources.get(site, F(0)) / chi[index[site]]
    clock_rhs = [2 * content[site] / (eight_k * chi[index[site]]) - sum(1 for other in neighbours(site) if other not in index) for site in interior]
    amplitude = solve(clock_matrix, clock_rhs)

    def laplacian(field, site):
        return sum((field[index[other]] if other in index else F(1)) - field[index[site]] for other in neighbours(site))

    edge = {site: -eight_k * amplitude[index[site]] * laplacian(chi, site) for site in interior}
    rest = {site: edge[site] - content[site] for site in interior}
    seen = set()
    bond_energy = F(0)
    for site in interior:
        for other in neighbours(site):
            key = tuple(sorted((site, other)))
            if key in seen:
                continue
            seen.add(key)
            other_amplitude = amplitude[index[other]] if other in index else F(1)
            other_chi = chi[index[other]] if other in index else F(1)
            bond_energy += -eight_k * (other_amplitude - amplitude[index[site]]) * (other_chi - chi[index[site]])
    charge_q = -sum(laplacian(chi, site) for site in interior)
    charge_p = sum(laplacian(amplitude, site) for site in interior)
    return {
        "sites": interior,
        "index": index,
        "chi": chi,
        "amplitude": amplitude,
        "edge": edge,
        "content": content,
        "rest": rest,
        "bond": bond_energy,
        "P": charge_p,
        "Q": charge_q,
        "hop": sum(bonds.values()),
        "rest_sum": sum(rest.values()),
        "lap": laplacian,
    }


def identities(config):
    eight_k = F(1)
    index = config["index"]
    good_sites = True
    for site in config["sites"]:
        chi = config["chi"][index[site]]
        amplitude = config["amplitude"][index[site]]
        clock = amplitude / chi
        edge = config["edge"][site]
        good_sites = good_sites and config["lap"](config["chi"], site) == -edge / (eight_k * clock * chi)
        good_sites = good_sites and config["lap"](config["amplitude"], site) == (edge + 2 * config["content"][site]) / (eight_k * chi)
    flux_q = sum(config["edge"][site] / (eight_k * (config["amplitude"][index[site]] / config["chi"][index[site]]) * config["chi"][index[site]]) for site in config["sites"])
    flux_p = sum((config["edge"][site] + 2 * config["content"][site]) / (eight_k * config["chi"][index[site]]) for site in config["sites"])
    energy = config["rest_sum"] + config["hop"]
    first = eight_k * config["Q"] - (energy + config["bond"])
    second = eight_k / 2 * (config["P"] + config["Q"]) - (config["rest_sum"] + 2 * config["hop"])
    return good_sites and flux_q == config["Q"] and flux_p == config["P"], first, second


def boxes() -> bool:
    side = 7
    left, right = (3, 3, 3), (3, 3, 4)
    generic = configure(side, {left: F(1, 2), right: F(1, 3)}, {(left, right): F(1, 20)})
    generic_ok, generic_one, generic_two = identities(generic)
    empty = configure(side, {left: F(1, 2), right: F(1, 3)}, {(left, right): F(0)})
    unit = configure(side, {left: F(1, 2), right: F(1, 3)}, {(left, right): F(1)})
    balance = (empty["Q"] - empty["P"]) / (unit["P"] - empty["P"])
    balanced = configure(side, {left: F(1, 2), right: F(1, 3)}, {(left, right): balance})
    balanced_ok, balanced_one, balanced_two = identities(balanced)
    clocks = [balanced["amplitude"][balanced["index"][site]] / balanced["chi"][balanced["index"][site]] for site in (left, right)]
    rests = [balanced["rest"][site] for site in (left, right)]
    weighted = sum(
        balanced["edge"][site] / balanced["chi"][balanced["index"][site]] * (1 - 3 * clock) / clock
        for site, clock in zip((left, right), clocks)
    )
    strong_empty = configure(side, {left: F(3), right: F(3)}, {(left, right): F(0)})
    strong_unit = configure(side, {left: F(3), right: F(3)}, {(left, right): F(1)})
    strong_balance = (strong_empty["Q"] - strong_empty["P"]) / (strong_unit["P"] - strong_empty["P"])
    compact = configure(side, {left: F(3), right: F(3)}, {(left, right): strong_balance})
    compact_ok, _, _ = identities(compact)
    compact_clocks = [compact["amplitude"][compact["index"][site]] / compact["chi"][compact["index"][site]] for site in (left, right)]
    wall_site, held = (1, 3, 3), (0, 3, 3)
    wall = configure(side, {wall_site: F(1, 2)}, {(wall_site, held): F(1, 10)})
    wall_ok, wall_one, wall_two = identities(wall)
    rest = configure(side, {left: F(1, 2)}, {})
    clock = rest["amplitude"][rest["index"][left]] / rest["chi"][rest["index"][left]]
    return (
        generic_ok and generic_one == 0 and generic_two == 0
        and balanced_ok and balanced["P"] == balanced["Q"] == F(5, 6) and min(rests) > 0
        and balanced_one == 0 and balanced_two == 0 and balanced["bond"] == balanced["hop"]
        and all(0 <= balanced["content"][site] <= balanced["edge"][site] for site in (left, right)) and weighted <= 0
        and compact_ok and compact["P"] == compact["Q"] and max(compact_clocks) < F(1, 3)
        and max(compact["rest"][site] for site in (left, right)) < 0
        and wall_ok and wall_one == F(-1, 20) and wall_two == F(-1, 10)
        and rest["P"] == clock * rest["Q"] and rest["Q"] == F(1, 2)
    )


def main():
    check("weights", weights(), "m_k for k = 1..6 equals both the beta integral and the gamma formula")
    check("orders", generic_orders(), "through order 5, m_k [u^k] n^k reproduces the expanded orbit polynomials")
    check("lagrange", lagrange(), "through order 10, on four random indices and the member, [w^k] log n(u(w)) = (1/k)[u^k] n^k")
    check("member", member(), "the binomial sum, the fixed-turn orders 2 and 3, and the equal-charge series through k = 6")
    check("capture", capture(), "T3's closed form is the positive discriminant root, with the stated double root and the four values")
    check("boxes", boxes(), "on the 7^3 box the balanced content has P = Q = 5/6, compact balance needs negative rest, and a wall bond breaks both global identities by -1/20 and -1/10")
    if FAILS:
        print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
        return 1
    print(
        "SUMMARY: confirmed partial. The turn is sum m_k [u^k] n(u)^k b^{-k}, and for the curvature member the "
        "radius in 1/b is the capture threshold. On exact 7^3 boxes a balanced content has P = Q, too-compact "
        "balance needs negative rest parts, and one content bond into a wall breaks both global identities. "
        "The coefficient growth scan and the monotonicity grid were not rebuilt.",
        flush=True,
    )
    print(
        "HIT: confirmed - the curvature member's turn series has radius exactly the capture threshold, and the "
        "two charges agree on balanced content away from the walls",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
