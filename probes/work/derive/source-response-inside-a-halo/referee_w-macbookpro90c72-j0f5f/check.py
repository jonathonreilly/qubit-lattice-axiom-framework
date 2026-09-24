#!/usr/bin/env python3
"""Referee for source-response-inside-a-halo a3.

Author w-jonathonsmac4f50-jf032 (claude-opus-5). Own enumeration of the one-record gas.
"""
import sympy as sp

fails = []
p, q, r, c = sp.symbols("p q r c", positive=True)
AX = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def omega(a, b):
    if a == b:
        return p
    if a == tuple(-x for x in b):
        return q
    return r


def neighbours(origin):
    return [tuple(origin[i] + d[i] for i in range(3)) for d in AX]


def gas_sites():
    found = set()
    for target in AX:
        found.add(target)
        for nxt in neighbours(target):
            found.add(nxt)
    found.discard((0, 0, 0))
    return sorted(found)


def drift(block=True, weigh=True):
    total = 0
    sites = gas_sites()
    for test in AX:
        for place in sites:
            for content in AX:
                hop = 0
                for step in AX:
                    target = step
                    if block and target == place:
                        continue
                    here = c * omega(test, content) if place in neighbours((0, 0, 0)) else sp.Integer(1)
                    there = c * omega(test, content) if place in neighbours(target) else sp.Integer(1)
                    if not weigh:
                        here = there = sp.Integer(1)
                    hop += step[0] * there / (here + there)
                total += sp.Rational(1, 36) * place[0] * hop
    return sp.simplify(total)


def main():
    blocked = drift(block=True, weigh=False)
    report("blocking", sp.simplify(blocked + 1) == 0, f"occupied targets alone contribute {blocked}")
    full = drift()
    closed = (
        18 * c ** 3 * p * q * r
        - 10 * c ** 2 * p * q
        + 11 * c ** 2 * p * r
        + 11 * c ** 2 * q * r
        - 17 * c * p
        - 17 * c * q
        + 4 * c * r
        - 24
    ) / (3 * (c * p + 1) * (c * q + 1) * (c * r + 1))
    report(
        "closed form",
        sp.simplify(full - closed) == 0,
        "the enumeration is the stated rational function",
    )
    weights = drift(block=False, weigh=True)
    rows = {
        (3, 1, 2): (sp.Rational(-52, 45), sp.Rational(-2, 15)),
        (12, 1, 2): (sp.Rational(-21002, 9207), sp.Rational(-3370, 3069)),
        (5, 2, 4): (sp.Rational(-13866, 12455), sp.Rational(-8466, 87185)),
        (7, 3, 5): (sp.Rational(-79, 72), sp.Rational(-1, 12)),
    }
    neutral = True
    for (pp, qq, rr), (want, want_w) in rows.items():
        c0 = sp.Rational(6, pp + qq + 4 * rr)
        sub = {p: pp, q: qq, r: rr, c: c0}
        neutral &= sp.simplify(full.subs(sub) - want) == 0
        neutral &= sp.simplify(weights.subs(sub) - want_w) == 0
        neutral &= want < 0
    phi = sp.symbols("phi", positive=True)
    concave = sp.diff(phi / (1 + phi), phi, 2)
    report(
        "neutral scale",
        neutral and sp.simplify(concave + 2 / (1 + phi) ** 3) == 0,
        "all four triples are negative at c0, and phi/(1+phi) is concave",
    )
    # reversal: the positive root of the numerator, as a ratio to c0
    ratios = []
    for pp, qq, rr in rows:
        c0 = sp.Rational(6, pp + qq + 4 * rr)
        num = sp.numer(sp.together(closed.subs({p: pp, q: qq, r: rr})))
        roots = [z for z in sp.real_roots(sp.Poly(sp.expand(num), c)) if z > 0]
        ratios.append(float(roots[0] / c0))
    report(
        "reversal",
        all(1.3 < z < 2.2 for z in ratios),
        "c*/c0 is " + ", ".join(f"{z:.4f}" for z in ratios),
    )
    g, kappa, m, Q, R = sp.symbols("g kappa m Q R", positive=True)
    mass_rate = kappa * m ** 2 * ((g * m / 2) + (-g * m / 2))
    momentum = kappa * m ** 2 * ((g * m / 2) * (m / 2) + (-g * m / 2) * (-m / 2))
    speed = sp.simplify(momentum / m ** 3)
    halo = sp.simplify(kappa * (Q / (4 * sp.pi * kappa * R ** 2)) * m / 2)
    report(
        "cube and halo",
        mass_rate == 0 and speed == kappa * g * m / 2 and halo == Q * m / (8 * sp.pi * R ** 2),
        "a held cube drifts at kappa g m/2; inside a halo that is Q m/(8 pi R^2)",
    )
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the first-order drift is the stated rational function. "
        "Blocking contributes -1. At c0=6/(p+q+4r) the drift is negative on (3,1,2), (12,1,2), (5,2,4) and (7,3,5). "
        "A held cube of side m drifts up the gradient at kappa g m/2, which is not symmetric in two bodies."
    )
    print(
        "SUMMARY: confirmed the enumeration, the four neutral values, the reversal ratios, and the cube scaling. "
        "The gas is an imposed independent gradient. A bound cluster was not in the attempt."
    )


if __name__ == "__main__":
    main()
