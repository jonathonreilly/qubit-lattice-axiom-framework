#!/usr/bin/env python3
"""Independent check of two held sources under light-cone formation, attempt a1.

Does not import the author's script. The reversibility and factorisation
checks on the rings, and the cumulant 2804904263700/2797699210501, are not
rebuilt. The sign at a non-mirror separation is.
"""
from fractions import Fraction
from itertools import product
from math import factorial

import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def double_factorial(odd):
    value = 1
    while odd > 1:
        value *= odd
        odd -= 2
    return value


def sphere_moment(exponents):
    if any(power % 2 for power in exponents):
        return Fraction(0)
    degree = sum(exponents) // 2
    numerator = 1
    for power in exponents:
        numerator *= double_factorial(power - 1)
    return Fraction(numerator, double_factorial(2 * degree + 1))


theta, phi = sp.symbols("theta phi")
moment_ok = True
checked = 0
for exponents in product(range(5), repeat=3):
    if sum(exponents) > 4:
        continue
    checked += 1
    density = (
        (sp.sin(theta) * sp.cos(phi)) ** exponents[0]
        * (sp.sin(theta) * sp.sin(phi)) ** exponents[1]
        * sp.cos(theta) ** exponents[2]
        * sp.sin(theta)
    )
    integral = sp.integrate(sp.integrate(density, (phi, 0, 2 * sp.pi)), (theta, 0, sp.pi)) / (4 * sp.pi)
    moment_ok &= sp.simplify(integral - sp.Rational(sphere_moment(exponents))) == 0
check(
    "sphere moments",
    moment_ok and checked == 35 and sphere_moment((2, 0, 0)) == Fraction(1, 3),
    "direct integration agrees with (a-1)!!(b-1)!!(c-1)!!/(a+b+c+1)!! for a+b+c <= 4, and E[x^2] = 1/3",
)

# two-valued menu on the doubled ring: edges from level 0 to level 1 along {0, +1, -1}
def tanh_polynomials(length):
    edges = [((site, 0), ((site + step) % length, 1)) for site in range(length) for step in (0, 1, -1)]

    def multiply(left, right):
        out = [0] * (len(left) + len(right) - 1)
        for i, left_term in enumerate(left):
            if left_term:
                for j, right_term in enumerate(right):
                    out[i + j] += left_term * right_term
        return out

    def add(left, right):
        width = max(len(left), len(right))
        return [(left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0) for i in range(width)]

    numerator = {distance: [0] for distance in (1, 2, 3)}
    denominator = [0]
    for bits in product((1, -1), repeat=2 * length):
        spin = {(site, level): bits[2 * site + level] for site in range(length) for level in (0, 1)}
        weight = [1]
        for left, right in edges:
            weight = multiply(weight, [1, spin[left] * spin[right]])
        denominator = add(denominator, weight)
        for distance in (1, 2, 3):
            pair = (spin[(0, 0)] + spin[(0, 1)]) * (spin[(distance, 0)] + spin[(distance, 1)])
            numerator[distance] = add(numerator[distance], [pair * term for term in weight])
    return numerator, denominator


numerator, denominator = tanh_polynomials(6)
orders = {distance: next(power for power, term in enumerate(numerator[distance]) if term) for distance in (1, 2, 3)}
positive_sample = all(
    sum(term * Fraction(1, 3) ** power for power, term in enumerate(numerator[distance])) > 0
    for distance in (1, 2, 3)
)
check(
    "two-valued sign",
    all(term >= 0 for term in denominator)
    and all(all(term >= 0 for term in numerator[distance]) for distance in (1, 2, 3))
    and orders == {1: 1, 2: 2, 3: 3}
    and positive_sample,
    f"on the doubled ring of 6 the tanh polynomials are non-negative and start at orders {orders}",
)


def series_at(length, start, end, order, field):
    vertices = [(site, level) for site in range(length) for level in (0, 1)]
    index = {vertex: i for i, vertex in enumerate(vertices)}
    edges = [((site, 0), ((site + step) % length, 1)) for site in range(length) for step in (0, 1, -1)]
    linear = {}
    for left, right in edges:
        for component in range(3):
            key = [0] * (3 * len(vertices))
            key[3 * index[left] + component] += 1
            key[3 * index[right] + component] += 1
            linear[tuple(key)] = linear.get(tuple(key), 0) + 1
    if field:
        for vertex in vertices:
            key = [0] * (3 * len(vertices))
            key[3 * index[vertex] + 2] += 1
            linear[tuple(key)] = linear.get(tuple(key), 0) + field
    seed = [0] * (3 * len(vertices))
    seed[3 * index[start]] += 1
    seed[3 * index[end]] += 1
    current = {tuple(seed): Fraction(1)}
    coefficients = []
    for power in range(order + 1):
        total = Fraction(0)
        for key, coeff in current.items():
            moment = Fraction(1)
            for slot in range(0, len(key), 3):
                moment *= sphere_moment(key[slot:slot + 3])
                if moment == 0:
                    break
            total += coeff * moment
        coefficients.append(total / factorial(power))
        nxt = {}
        for key, coeff in current.items():
            for bump, weight in linear.items():
                raised = tuple(key[i] + bump[i] for i in range(len(key)))
                nxt[raised] = nxt.get(raised, 0) + coeff * weight
        current = nxt
    return coefficients


same_level = series_at(4, (0, 0), (2, 0), 4, 0)
across = series_at(4, (0, 0), (2, 1), 4, Fraction(1, 2))
check(
    "sphere series",
    same_level == [Fraction(0), Fraction(0), Fraction(2, 27), Fraction(0), Fraction(22, 135)]
    and across == [Fraction(0), Fraction(0), Fraction(0), Fraction(2, 27), Fraction(0)],
    f"non-mirror separation 2 on the doubled ring of 4: {same_level}; with field 1/2 across levels: {across}",
)

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL on the doubled ring the two-valued correlations at distances 1, 2 and 3 are ratios of "
        "polynomials in tanh(beta) with non-negative coefficients, starting at orders 1, 2 and 3. "
        "Sphere moments through degree 4 match the double-factorial formula, so E[x^2] = 1/3. "
        "At the non-mirror separation 2 the unnormalised sphere correlation starts 2/27 beta^2 + 22/135 beta^4, "
        "and with a field 1/2 the transverse across-level series starts 2/27 beta^3. "
        "The reversibility, factorisation and the ring-of-six cumulant were not rebuilt.",
        flush=True,
    )
    print(
        "HIT: confirmed - aligned sources have a positive cross term at a non-mirror separation. "
        "On the doubled ring of 6 the two-valued correlations start at tanh orders 1, 2 and 3, "
        "and on the doubled ring of 4 the sphere series at separation 2 is 2/27 beta^2 + 22/135 beta^4.",
        flush=True,
    )
