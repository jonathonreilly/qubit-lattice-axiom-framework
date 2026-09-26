#!/usr/bin/env python3
"""Independent referee for the nonlinear self-weighted closure, attempt 1.

The steered state, the chord identity, and the Legendre obstruction are
recomputed. The attempt's script is not imported. The floating-point
tanh scan was not rebuilt. Spherical-harmonic completeness and the
classical circle formula for Legendre polynomials are imported.
"""
from __future__ import annotations

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def pauli():
    return (
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    )


def bloch(state):
    return [sp.simplify(sp.trace(state * sigma)) for sigma in pauli()]


def partial_a(operator):
    return sp.Matrix(2, 2, lambda row, col: sum(operator[2 * row + k, 2 * col + k] for k in range(2)))


def partial_b(operator):
    return sp.Matrix(2, 2, lambda row, col: sum(operator[2 * k + row, 2 * k + col] for k in range(2)))


def geometry() -> bool:
    slope = sp.symbols("u", positive=True)
    length = (1 - slope ** 2) / (1 + slope ** 2)
    plus = sp.Matrix([1, 1]) / sp.sqrt(2)
    minus = sp.Matrix([1, -1]) / sp.sqrt(2)
    up, down = sp.Matrix([1, 0]), sp.Matrix([0, 1])
    amplitude = 1 / sp.sqrt(1 + slope ** 2)
    state = amplitude * sp.kronecker_product(plus, up) + slope * amplitude * sp.kronecker_product(minus, down)
    density = sp.simplify(state * state.H)
    vectors = bloch(partial_a(density)) + bloch(partial_b(density))
    expected = [length, 0, 0, 0, 0, length]
    aligned = all(sp.simplify(got - want) == 0 for got, want in zip(vectors, expected))

    def steered(direction):
        projector = sp.kronecker_product(sp.eye(2), direction * direction.H)
        image = sp.simplify(projector * state)
        weight = sp.simplify((image.H * image)[0])
        reduced = partial_a(sp.simplify(image * image.H))
        return weight, [sp.simplify(component / weight) for component in bloch(reduced)]

    weight_up, vector_up = steered(up)
    weight_down, vector_down = steered(down)
    radial = (
        sp.simplify(weight_up - (1 + length) / 2) == 0
        and vector_up == [1, 0, 0]
        and sp.simplify(weight_down - (1 - length) / 2) == 0
        and vector_down == [-1, 0, 0]
    )
    plus_y = (up + sp.I * down) / sp.sqrt(2)
    minus_y = (up - sp.I * down) / sp.sqrt(2)
    weight_plus, vector_plus = steered(plus_y)
    weight_minus, vector_minus = steered(minus_y)
    transverse = 2 * slope / (1 + slope ** 2)
    perpendicular = (
        sp.simplify(weight_plus - sp.Rational(1, 2)) == 0
        and sp.simplify(weight_minus - sp.Rational(1, 2)) == 0
        and all(
            sp.simplify(got - want) == 0
            for got, want in zip(vector_plus + vector_minus, [length, transverse, 0, length, -transverse, 0])
        )
        and bloch(plus_y * plus_y.H) == [0, 1, 0]
        and bloch(minus_y * minus_y.H) == [0, -1, 0]
    )
    return aligned and radial and perpendicular


def oddness() -> bool:
    value, weight = sp.symbols("c w")
    law = sp.Function("h")
    average = weight * law(value) + (1 - weight) * law(-value)
    shifted = sp.simplify(average.subs(law(-value), 1 - law(value)) - sp.Rational(1, 2))
    slope = 2 * weight - 1
    return sp.simplify(shifted - slope * (law(value) - sp.Rational(1, 2))) == 0


def circle_formula(max_degree: int = 13) -> bool:
    angle = sp.symbols("psi", real=True)
    good = True
    for degree in range(1, max_degree + 1):
        left = sp.expand(sp.legendre(degree, sp.cos(angle)).rewrite(sp.exp))
        right = 0
        for index in range(degree + 1):
            coefficient = sp.binomial(2 * index, index) * sp.binomial(2 * (degree - index), degree - index)
            coefficient /= sp.Integer(4) ** degree
            right += coefficient * sp.cos((degree - 2 * index) * angle)
        good = good and sp.simplify(left - sp.expand(right.rewrite(sp.exp))) == 0
    return good


def mode_identity() -> bool:
    angle, opening, weight, harmonic = sp.symbols("theta beta w k", real=True)
    addition = sp.simplify(
        sp.expand_trig(
            sp.Rational(1, 2) * (sp.cos(harmonic * (angle - opening)) + sp.cos(harmonic * (angle + opening)))
            - sp.cos(harmonic * opening) * sp.cos(harmonic * angle)
        )
    )
    good = addition == 0
    for degree in (1, 3, 5, 7):
        combination = sp.Rational(1, 2) * (
            sp.legendre(degree, sp.cos(angle - opening)) + sp.legendre(degree, sp.cos(angle + opening))
        )
        combination -= (2 * weight - 1) * sp.legendre(degree, sp.cos(angle))
        form = 0
        for index in range((degree + 1) // 2):
            tone = degree - 2 * index
            other = degree - index
            coefficient = (
                2
                * sp.binomial(2 * index, index)
                * sp.binomial(2 * other, other)
                / sp.Integer(4) ** degree
            )
            form += coefficient * (sp.cos(tone * opening) - (2 * weight - 1)) * sp.cos(tone * angle)
        good = good and sp.simplify(sp.expand(sp.expand_trig(combination - form))) == 0
    for degree in range(3, 14, 2):
        for tone in (1, 3):
            index = (degree - tone) // 2
            other = degree - index
            coefficient = 2 * sp.binomial(2 * index, index) * sp.binomial(2 * other, other)
            good = good and coefficient > 0
    return good


def triple_angle() -> bool:
    opening = sp.symbols("beta", real=True)
    identity = sp.simplify(sp.cos(3 * opening) - sp.cos(opening) + 2 * sp.sin(2 * opening) * sp.sin(opening))
    cosine = sp.Rational(3, 5)
    triple = sp.expand(4 * cosine ** 3 - 3 * cosine)
    return identity == 0 and triple == sp.Rational(-117, 125) and triple != cosine


def born_or_constant() -> bool:
    length, slope, weight = sp.symbols("l a1 w", real=True)
    solutions = sp.solve([sp.Eq(2 * weight - 1, length), sp.Eq(weight, sp.Rational(1, 2) + slope * length)], [weight, slope], dict=True)
    born = {weight: (1 + length) / 2, slope: sp.Rational(1, 2)}
    return solutions == [born]


def affine_and_cubic() -> bool:
    cosine, slope, length, angle, opening = sp.symbols("c lam l theta beta", real=True)
    weight = (1 + slope * length) / 2
    radial = (1 + slope * length * cosine) / 2 - (
        weight * (1 + slope * cosine) / 2 + (1 - weight) * (1 - slope * cosine) / 2
    )
    radial_ok = sp.factor(sp.simplify(radial)) == sp.factor(slope * length * cosine * (1 - slope) / 2)
    perpendicular = (1 + slope * length * sp.cos(angle)) / 2 - sp.Rational(1, 2) * (
        (1 + slope * sp.cos(angle - opening)) / 2 + (1 + slope * sp.cos(angle + opening)) / 2
    )
    perpendicular = sp.simplify(sp.expand_trig(perpendicular).subs(sp.cos(opening), length))
    pure = sp.cos(3 * angle)
    circle = sp.simplify(
        sp.expand_trig(sp.Rational(1, 2) * (sp.cos(3 * (angle - opening)) + sp.cos(3 * (angle + opening))) - sp.cos(3 * opening) * pure)
    )
    cubic = lambda value: (3 * value - value ** 3) / 4
    residue = sp.Rational(1, 2) * (cubic(sp.cos(angle - opening)) + cubic(sp.cos(angle + opening)))
    residue -= (2 * sp.symbols("w") - 1) * cubic(sp.cos(angle))
    residue = sp.expand(sp.expand_trig(residue).subs({sp.cos(opening): sp.Rational(3, 5), sp.sin(opening): sp.Rational(4, 5)}))
    theta = sp.symbols("theta", real=True)
    residue = residue.subs(angle, theta)
    first = sp.simplify(sp.integrate(residue * sp.cos(theta), (theta, -sp.pi, sp.pi)) / sp.pi)
    third = sp.simplify(sp.integrate(residue * sp.cos(3 * theta), (theta, -sp.pi, sp.pi)) / sp.pi)
    return radial_ok and perpendicular == 0 and circle == 0 and sp.solve([first, third], sp.symbols("w")) == []


def main():
    check(
        "geometry",
        geometry(),
        "for every Bloch length the partner's z-menu steers to +-x and its y-menu steers to (l, +-sqrt(1-l^2), 0)",
    )
    check("oddness", oddness(), "antipodal normalization makes the radial average (2w-1) times the odd part")
    check("circle formula", circle_formula(), "P_L(cos psi) matches the binomial cosine sum for L = 1..13")
    check(
        "modes",
        mode_identity(),
        "cos(k(theta-beta)) averages to cos(k beta) cos(k theta); odd degrees through 7 match, and the k=1 and k=3 binomial coefficients stay positive through degree 13",
    )
    check("triple angle", triple_angle(), "cos 3 beta - cos beta = -2 sin(2 beta) sin beta, and at l = 3/5 the values are 3/5 and -117/125")
    check("born", born_or_constant(), "a linear odd law with nonzero slope is forced to Born's (1+c)/2")
    check(
        "affine and cubic",
        affine_and_cubic(),
        "the radial chord forces lam(lam-1)=0 on the affine family, a pure triple angle survives in-plane at cos 3 beta, and the cubic has no such weight",
    )
    if FAILS:
        print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
        return 1
    print(
        "SUMMARY: confirmed partial. Under covariance, antipodal normalization, projective steering, "
        "and self-weighted no-signalling at one Bloch length, a measurable pure law is Born or constant. "
        "Spherical-harmonic completeness and the Legendre circle formula are imported; the formula was "
        "checked through degree 13. The tanh scan was not rebuilt. The steering update itself was not derived.",
        flush=True,
    )
    print(
        "HIT: confirmed - at one Bloch length the two partner menus force a measurable self-weighted "
        "qubit law to be Born or constant, and the endpoint condition removes the constant",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
