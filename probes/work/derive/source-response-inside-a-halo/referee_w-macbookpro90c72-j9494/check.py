#!/usr/bin/env python3
"""Referee for source response inside a halo, a5.

Author w-macbookpro90c72-j716e (claude-opus-5-5). Own averages and shell sum.
The independent-site gas and block 41's halo form are the attempt's assumptions.
The degree-10 polynomial is rebuilt for the sign on (0,1); its higher coefficients
are not quoted.
"""
import itertools

import sympy as sp

fails = []
DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
TRIPLES = ((3, 1, 2), (12, 1, 2), (5, 2, 4), (7, 3, 5))
HEAT = {
    (3, 1, 2): sp.Rational(-52, 45),
    (12, 1, 2): sp.Rational(-21002, 9207),
    (5, 2, 4): sp.Rational(-13866, 12455),
    (7, 3, 5): sp.Rational(-79, 72),
}
METRO = {
    (3, 1, 2): sp.Rational(-26, 9),
    (12, 1, 2): sp.Rational(-3337, 504),
    (5, 2, 4): sp.Rational(-974, 345),
    (7, 3, 5): sp.Rational(-284, 105),
}


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def neutral(p, q, r):
    return sp.Rational(6, p + q + 4 * r)


def average(function, p, q, r, scale):
    return (function(scale * p) + function(scale * q) + 4 * function(scale * r)) / 6


def heat_drift(p, q, r, scale):
    inward = average(lambda weight: weight / (1 + weight), p, q, r, scale)
    outward = average(lambda weight: 1 / (1 + weight), p, q, r, scale)
    return sp.simplify(12 * inward - 2 * outward - 6)


def metro_piece(weight):
    return weight if weight <= 1 else sp.Integer(1)


def metro_reciprocal(weight):
    return 1 / weight if weight >= 1 else sp.Integer(1)


def metro_drift(p, q, r, scale):
    inward = average(metro_piece, p, q, r, scale)
    outward = average(metro_reciprocal, p, q, r, scale)
    return sp.simplify(12 * inward - 2 * outward - 12)


def first_order():
    ok = True
    for triple in TRIPLES:
        scale = neutral(*triple)
        ok &= heat_drift(*triple, scale) == HEAT[triple]
        ok &= metro_drift(*triple, scale) == METRO[triple]
        ok &= metro_drift(*triple, scale) < 0
    # Metropolis: E min(1, W) <= 1, so the drift is at most -2 E min(1, 1/W) < 0 for every finite positive c.
    report(
        "first order",
        ok,
        "heat bath at c0 is -52/45, -21002/9207, -13866/12455, -79/72; Metropolis is -26/9, -3337/504, -974/345, -284/105, all negative",
    )


def reversal():
    ok = True
    ratios = []
    for triple in TRIPLES:
        p, q, r = triple
        scale = sp.symbols("c", positive=True)
        expr = heat_drift(p, q, r, scale)
        root = sp.nsolve(expr, scale, float(neutral(*triple)))
        lo, hi = sp.Rational(int(root * 10 ** 6) - 2, 10 ** 6), sp.Rational(int(root * 10 ** 6) + 2, 10 ** 6)
        # sign change on a 4e-6 window, and the published six-digit value sits in it
        ok &= sp.sign(expr.subs(scale, lo)) != sp.sign(expr.subs(scale, hi))
        published = {
            (3, 1, 2): sp.Rational(702965, 10 ** 6),
            (12, 1, 2): sp.Rational(597174, 10 ** 6),
            (5, 2, 4): sp.Rational(361617, 10 ** 6),
            (7, 3, 5): sp.Rational(275496, 10 ** 6),
        }[triple]
        ok &= lo < published < hi
        ratios.append(published / neutral(*triple))
        for probe in (sp.Rational(1, 1000), sp.Integer(1), sp.Integer(10), sp.Integer(1000)):
            ok &= metro_drift(p, q, r, probe) < 0
    ok &= min(ratios) > sp.Rational(137, 100) and max(ratios) < sp.Rational(21, 10)
    report(
        "reversal",
        ok,
        "heat bath changes sign once, at 1.38 to 2.09 times c0; Metropolis stays negative from c=1/1000 through c=1000",
    )


def weight_distribution(count, values):
    dist = {sp.Integer(1): sp.Integer(1)}
    chances = (sp.Rational(1, 6), sp.Rational(1, 6), sp.Rational(4, 6))
    for _ in range(count):
        nxt = {}
        for value, prob in dist.items():
            for chance, weight in zip(chances, values):
                product = value * weight
                nxt[product] = nxt.get(product, 0) + prob * chance
        dist = nxt
    return dist


def acceptance_table(values, rule):
    table = {}
    dists = [weight_distribution(n, values) for n in range(6)]
    for left in range(6):
        for right in range(6):
            total = 0
            for wx, px in dists[left].items():
                for wy, py in dists[right].items():
                    if rule == "heat":
                        factor = wy / (wx + wy)
                    else:
                        factor = wy / wx if wy <= wx else sp.Integer(1)
                    total += px * py * factor
            table[(left, right)] = sp.together(total)
    return table


def response(p, q, r, scale, rule):
    values = [scale * p, scale * q, scale * r]
    table = acceptance_table(values, rule)
    rho0, grad = sp.symbols("rho0 g")
    origin = (0, 0, 0)
    total = 0
    marker = sp.symbols("t")
    for step in DIRS:
        if step[0] == 0:
            continue
        left_sites = [tuple(a + b for a, b in zip(origin, d)) for d in DIRS if d != step]
        right_sites = [tuple(a + b for a, b in zip(step, d)) for d in DIRS if tuple(a + b for a, b in zip(step, d)) != origin]
        def generating(sites):
            poly = sp.Integer(1)
            for site in sites:
                density = rho0 + grad * site[0]
                poly *= 1 - density + density * marker
            return sp.expand(poly)
        left = [generating(left_sites).coeff(marker, n) for n in range(6)]
        right = [generating(right_sites).coeff(marker, n) for n in range(6)]
        expect = sum(left[i] * right[j] * table[(i, j)] for i in range(6) for j in range(6))
        density = rho0 + grad * step[0]
        total += step[0] * (1 - density) * expect
    coefficient = sp.expand(sp.Poly(sp.expand(total), grad).coeff_monomial(grad))
    return sp.Poly(sp.expand(coefficient), rho0)


def density_sign():
    ok = True
    linear = None
    for triple in TRIPLES:
        scale = neutral(*triple)
        for rule in ("heat", "metro"):
            poly = response(*triple, scale, rule)
            ok &= poly.subs(sp.symbols("rho0"), 0) == (HEAT if rule == "heat" else METRO)[triple]
            ok &= sp.count_roots(poly, 0, 1) == 0
            ok &= all(poly.subs(sp.symbols("rho0"), sp.Rational(k, 10)) < 0 for k in range(1, 10))
            if triple == (3, 1, 2) and rule == "heat":
                linear = sp.simplify(poly.coeff_monomial(sp.symbols("rho0")))
                ok &= linear == sp.Rational(317, 1755)
    report(
        "density",
        ok,
        f"at c0 the heat-bath polynomial on (3,1,2) is -52/45 + ({linear}) rho0 + ... and no triple changes sign on (0,1) for either acceptance",
    )


def formation():
    side, fugacity, rho0, grad = sp.symbols("m z rho0 g", positive=True)
    face = (side + 1) / 2
    ends = side ** 2 * face * 6 * fugacity * (1 - rho0 - grad * face) + side ** 2 * (-face) * 6 * fugacity * (1 - rho0 + grad * face)
    sides = 4 * side * (6 * fugacity * (-grad) * side * (side ** 2 - 1) / 12)
    total = sp.factor(sp.expand(ends + sides))
    target = -fugacity * grad * side ** 2 * (side + 1) * (5 * side + 1)
    shells = True
    for width in (1, 2, 3, 4):
        half = sp.Rational(width - 1, 2)
        coords = [-half + i for i in range(width)]
        cube = set(itertools.product(coords, repeat=3))
        shell = set()
        for cell in cube:
            for step in DIRS:
                neighbour = tuple(cell[k] + step[k] for k in range(3))
                if neighbour not in cube:
                    shell.add(neighbour)
        moment = sum(site[0] * 6 * fugacity * (1 - rho0 - grad * site[0]) for site in shell)
        touch = all(sum(1 for step in DIRS if tuple(site[k] + step[k] for k in range(3)) in cube) == 1 for site in shell)
        shells &= touch and sp.simplify(moment - target.subs(side, width)) == 0
    p, q, r = sp.symbols("p q r", positive=True)
    row = sp.simplify(sp.Rational(6, 1) / (p + q + 4 * r) * (p + q + 4 * r) - 6)
    report(
        "formation",
        sp.simplify(total - target) == 0 and shells and row == 0,
        "a row of pair weights sums to 6 at c0, and the shell moment is -z g m^2 (m+1)(5m+1); shells of side 1..4 have one cube neighbour each",
    )


def main():
    first_order()
    reversal()
    density_sign()
    formation()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - at the neutral scale a free record drifts down the gradient: heat bath -52/45, -21002/9207, "
        "-13866/12455, -79/72 and Metropolis -26/9, -3337/504, -974/345, -284/105. "
        "The all-orders density polynomial stays negative on (0,1). Heat bath reverses at 1.38 to 2.09 times c0; "
        "Metropolis does not, because its coefficient is at most -2 E min(1, 1/W). "
        "Formation on a held cube has first moment -z g m^2 (m+1)(5m+1)."
    )
    print(
        "SUMMARY: confirmed the two acceptances, the sign on (0,1), the reversal split, and the cube moment. "
        "The independent-site gas and the halo profile 1/R^2 are the attempt's assumptions. "
        "Retention of formed records was not derived."
    )


if __name__ == "__main__":
    main()
