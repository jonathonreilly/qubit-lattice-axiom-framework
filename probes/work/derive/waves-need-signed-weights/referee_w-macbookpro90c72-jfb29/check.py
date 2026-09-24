#!/usr/bin/env python3
"""Referee for waves need signed weights, a4.

Author w-macbookpro90c72-jf9e6 (claude-opus-5). Own symbol, discriminant, and cone checks.
The open-set rigidity step is the autocorrelation argument those certificates support.
"""
from fractions import Fraction as Fr

import sympy as sp

fails = []
lam, nu = sp.symbols("lam nu")


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def zero_matrix(matrix):
    simplified = sp.simplify(matrix)
    return all(simplified[i, j] == 0 for i in range(simplified.rows) for j in range(simplified.cols))


def transport():
    kk, mu, vv = sp.symbols("kk mu vv", real=True)
    ok = True
    for depth in (2, 3, 4):
        weights = sp.symbols(f"g0:{depth}", nonnegative=True)
        chi = lam ** depth - sum(
            weights[j] * sp.exp(-sp.I * kk * (j + 1) * vv) * lam ** (depth - 1 - j) for j in range(depth)
        )
        reduced = sp.expand(chi.subs(lam, mu * sp.exp(-sp.I * kk * vv)) * sp.exp(sp.I * depth * kk * vv))
        target = mu ** depth - sum(weights[j] * mu ** (depth - 1 - j) for j in range(depth))
        ok &= sp.simplify(reduced - target) == 0
    cubic = mu ** 3 - sp.Rational(1, 2) * mu ** 2 - sp.Rational(1, 2)
    quadratic = mu ** 2 + mu / 2 + sp.Rational(1, 2)
    ok &= sp.expand(cubic - (mu - 1) * quadratic) == 0
    ok &= sp.discriminant(quadratic, mu) == sp.Rational(-7, 4)
    report(
        "transport",
        ok,
        "a single-site delay makes the symbol k-free for depths 2, 3 and 4; g=(1/2,0,1/2) has one transport root and a pair of modulus 1/sqrt(2)",
    )


def resultant_split():
    ok = True
    seen = {}
    for value, label in ((sp.pi / 3, "pi/3"), (sp.pi / 2, "pi/2"), (sp.pi, "pi"), (0, "0")):
        phase = sp.exp(-sp.I * value)
        poly = sp.expand(lam ** 2 - phase * lam / 2 - phase / 2)
        coeffs = sp.Poly(poly, lam).all_coeffs()
        mirror = sum(sp.conjugate(coeffs[i]) * lam ** i for i in range(len(coeffs)))
        result = sp.simplify(sp.expand_complex(sp.resultant(poly, sp.expand(mirror), lam)))
        seen[label] = result
        ok &= (result == 0) if label == "0" else (result != 0)
    report(
        "split",
        ok and seen == {"pi/3": sp.Rational(1, 8), "pi/2": sp.Rational(1, 4), "pi": sp.Rational(1, 2), "0": 0},
        "equal half-weights on one site have resultants 1/8, 1/4, 1/2, 0 at pi/3, pi/2, pi and 0",
    )


def autocorrelation(weights):
    total = {}
    for left, left_w in weights.items():
        for right, right_w in weights.items():
            lag = left - right
            total[lag] = total.get(lag, 0) + left_w * sp.conjugate(right_w)
    return {lag: sp.simplify(value) for lag, value in total.items() if sp.simplify(value) != 0}


def lags():
    samples = [
        ("one site", {3: Fr(-1)}, True, 0, Fr(1)),
        ("neighbours", {-1: Fr(1, 2), 1: Fr(1, 2)}, False, 2, Fr(1, 4)),
        ("three sites", {0: Fr(1, 2), 2: Fr(1, 3), 5: Fr(1, 6)}, False, 5, Fr(1, 12)),
        ("signed pair", {0: Fr(3, 5), 1: Fr(-4, 5)}, False, 1, Fr(-12, 25)),
    ]
    ok = True
    for _name, weights, unimodular, lag, coeff in samples:
        corr = autocorrelation(weights)
        places = sorted(weights)
        extreme = places[-1] - places[0]
        ok &= (corr == {0: 1}) == unimodular
        ok &= corr.get(extreme, 0) == coeff
        ok &= extreme == lag
    complex_pair = autocorrelation({0: sp.Rational(3, 5), 1: sp.Rational(4, 5) * sp.I})
    ok &= complex_pair[0] == 1 and complex_pair[1] == sp.Rational(12, 25) * sp.I
    report(
        "lags",
        ok,
        "only the single signed site is unimodular; the spread weights have nonzero extreme lags, including 12i/25 at unit l2 norm",
    )


def ladder():
    ok = True
    for depth in (2, 3, 4):
        phases = sp.symbols(f"p0:{depth}", real=True)
        poly = sp.expand(sp.prod(lam - sp.exp(sp.I * phase) for phase in phases))
        coeff = [sp.expand(poly.coeff(lam, power)) for power in range(depth + 1)]
        amplitude = [-coeff[depth - 1 - j] for j in range(depth)]
        for j in range(depth - 1):
            relation = sp.simplify(sp.expand(amplitude[j] + amplitude[depth - 1] * sp.conjugate(amplitude[depth - 2 - j])))
            ok &= relation == 0
    report(
        "ladder",
        ok,
        "unimodular roots force a_j = -a_{J-1} conjugate(a_{J-2-j}) at depths 2, 3 and 4",
    )


def deltoid():
    x, y = sp.symbols("x y", real=True)
    coeff = x + sp.I * y
    cubic = nu ** 3 - coeff * nu ** 2 + sp.conjugate(coeff) * nu - 1
    disc = sp.expand(sp.discriminant(cubic, nu))
    target = sp.expand((x ** 2 + y ** 2) ** 2 + 18 * (x ** 2 + y ** 2) - 8 * x * (x ** 2 - 3 * y ** 2) - 27)
    real = sp.factor(disc.subs(y, 0))
    cusps = [
        sp.simplify(disc.subs({x: sp.re(3 * sp.exp(2 * sp.pi * sp.I * j / 3)), y: sp.im(3 * sp.exp(2 * sp.pi * sp.I * j / 3))}))
        for j in range(3)
    ]
    report(
        "deltoid",
        sp.simplify(disc - target) == 0 and real == sp.factor((x + 1) * (x - 3) ** 3) and all(point == 0 for point in cusps),
        "the self-inversive cubic discriminant is |b|^4+18|b|^2-8 Re(b^3)-27, with real section (b+1)(b-3)^3 and cusps at the cube roots of unity times 3",
    )


def circle():
    t1, t2 = sp.symbols("t1 t2", real=True)
    angles = [t1, t2, -t1 - t2]
    coeff = sum(sp.exp(sp.I * angle) for angle in angles)
    disc = sp.discriminant(nu ** 3 - coeff * nu ** 2 + sp.conjugate(coeff) * nu - 1, nu)
    product = -64 * sp.prod(sp.sin((angles[i] - angles[j]) / 2) ** 2 for i in range(3) for j in range(i + 1, 3))
    rho, delta = sp.symbols("rho", positive=True), sp.symbols("delta", real=True)
    phase = sp.exp(sp.I * delta)
    off = phase ** -2 + rho * phase + phase / rho
    disc_off = sp.discriminant(nu ** 3 - off * nu ** 2 + sp.conjugate(off) * nu - 1, nu)
    formula = (rho - 1 / rho) ** 2 * (2 * sp.cos(3 * delta) - rho - 1 / rho) ** 2
    on_circle = sp.simplify(sp.expand((disc - product).rewrite(sp.exp))) == 0
    off_circle = sp.simplify(sp.expand((disc_off - formula).rewrite(sp.exp))) == 0
    report(
        "circle",
        on_circle and off_circle,
        "unimodular triples have disc = -64 times a product of sines, and off-circle triples have a strictly positive disc",
    )


def blink():
    profile = sp.symbols("Phat", real=True)
    char = sp.expand(lam ** 3 - profile * lam ** 2 - profile * lam + 1)
    factored = sp.expand((lam + 1) * (lam ** 2 - (1 + profile) * lam + 1))
    angle, radius, sign = sp.symbols("w rr sigma", real=True)
    radius = sp.symbols("rr", positive=True)
    pair = lam ** 2 - (1 + profile) * lam + 1
    on = sp.simplify(sp.expand((pair.subs(profile, 2 * sp.cos(angle) - 1) - (lam - sp.exp(sp.I * angle)) * (lam - sp.exp(-sp.I * angle))).rewrite(sp.exp)))
    plus = sp.simplify(sp.expand(pair.subs(profile, radius + 1 / radius - 1) - (lam - radius) * (lam - 1 / radius)))
    minus = sp.simplify(sp.expand(pair.subs(profile, -(radius + 1 / radius) - 1) - (lam + radius) * (lam + 1 / radius)))
    length = 7
    shape = [Fr(k * k + 1, 3 * k + 5) for k in range(length)]

    def average(values):
        return [(values[(i - 1) % length] + values[(i + 1) % length]) / 2 for i in range(length)]

    state = {-2: list(shape), -1: [-z for z in shape], 0: list(shape)}
    blinks = True
    for tick in range(6):
        nxt = [average(state[tick])[i] + average(state[tick - 1])[i] - state[tick - 2][i] for i in range(length)]
        blinks &= nxt == [-z for z in state[tick]]
        state[tick + 1] = nxt
    modes = [sp.cos(2 * sp.pi * j / 6) for j in range(6)]
    window = all(sp.simplify(sp.Abs(1 + mode) - 2) <= 0 for mode in modes)
    report(
        "blink",
        sp.expand(char - factored) == 0 and on == 0 and plus == 0 and minus == 0 and blinks and window,
        "the gain-one three-level rule has a lam=-1 branch, a wave pair exactly on Phat in [-3,1], and (-1)^t f is an exact solution",
    )


def cones():
    ok = True
    for dim in (1, 2, 3, 4):
        coords = sp.symbols(f"c0:{dim}", real=True)
        total = sum(coords)
        pairs = sum((coords[i] - coords[j]) ** 2 for i in range(dim) for j in range(i + 1, dim))
        spread = sum(1 - item ** 2 for item in coords)
        two = sp.Rational(1, dim) - spread / (dim ** 2 - total ** 2)
        two_target = pairs / (dim * (dim ** 2 - total ** 2))
        three = sp.Rational(1, 2 * dim) - spread / (4 * dim ** 2 - (dim + total) ** 2)
        three_target = ((dim - total) ** 2 + 2 * pairs) / (2 * dim * (4 * dim ** 2 - (dim + total) ** 2))
        ok &= sp.simplify(sp.together(two - two_target)) == 0
        ok &= sp.simplify(sp.together(three - three_target)) == 0
    eps = sp.symbols("eps", positive=True)
    for dim in (2, 3):
        direction = sp.symbols(f"n0:{dim}", positive=True)
        coords = [sp.cos(eps * item) for item in direction]
        total = sum(coords)
        spread = sum(1 - item ** 2 for item in coords)
        ok &= sp.simplify(sp.limit(spread / (dim ** 2 - total ** 2), eps, 0) - sp.Rational(1, dim)) == 0
        ok &= sp.simplify(sp.limit(spread / (4 * dim ** 2 - (dim + total) ** 2), eps, 0) - sp.Rational(1, 2 * dim)) == 0
    step = sp.pi / 12
    left, right = (0, 5 * step), (3 * step, 4 * step)
    same_radius = sp.simplify(left[0] ** 2 + left[1] ** 2 - right[0] ** 2 - right[1] ** 2) == 0
    different = sp.simplify((sp.cos(left[0]) + sp.cos(left[1])) / 2 - (sp.cos(right[0]) + sp.cos(right[1])) / 2) != 0
    report(
        "cones",
        ok and same_radius and different,
        "1/d - |grad w|^2 is a sum of squared cosine gaps, the long-wave limits are 1/d and 1/(2d), and equal |k| need not give equal frequency",
    )


def unitary():
    entries = sp.symbols("u11 u12 u21 u22")
    matrix = sp.Matrix([[entries[0], entries[1]], [entries[2], entries[3]]])
    trace = entries[0] + entries[3]
    det = entries[0] * entries[3] - entries[1] * entries[2]
    cayley = sp.expand(matrix * matrix - trace * matrix + det * sp.eye(2))
    angle, wave = sp.symbols("theta k", real=True)
    coin = sp.Matrix(
        [
            [sp.cos(angle) * sp.exp(-sp.I * wave), sp.sin(angle)],
            [-sp.sin(angle), sp.cos(angle) * sp.exp(sp.I * wave)],
        ]
    )
    report(
        "unitary",
        zero_matrix(cayley)
        and zero_matrix(sp.simplify(coin.H * coin - sp.eye(2)))
        and sp.simplify(sp.det(coin) - 1) == 0
        and sp.simplify(sp.trace(coin) - 2 * sp.cos(angle) * sp.cos(wave)) == 0,
        "Cayley-Hamilton gives a signed depth-2 recursion, and the 1+1 coin symbol is unitary with det 1 and trace 2 cos(theta) cos(k)",
    )


def main():
    transport()
    resultant_split()
    lags()
    ladder()
    deltoid()
    circle()
    blink()
    cones()
    unitary()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - a single-site delay is k-free and unimodular, while equal half-weights are not except at k=0. "
        "Unimodular roots force the reflection ladder. For three levels, lossless is the deltoid disc <= 0, and the gain-one rule blinks at lam=-1 with window [-3,1]. "
        "The signed nearest-neighbour cones are round, of radius 1/sqrt(d) and 1/sqrt(2d), although equal |k| need not share a frequency. "
        "A unitary amplitude step gives each component a signed recursion whose deepest weight is the determinant."
    )
    print(
        "SUMMARY: confirmed the transport symbol, the resultants, the ladder, the deltoid, the blink window, the cone identities, and Cayley-Hamilton. "
        "The open-set step from a vanishing autocorrelation to a single site is the attempt's analytic argument."
    )


if __name__ == "__main__":
    main()
