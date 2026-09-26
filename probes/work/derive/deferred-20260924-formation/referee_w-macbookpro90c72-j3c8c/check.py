#!/usr/bin/env python3
"""Independent referee for deferred-20260924-formation a1.

Exact identities of the sphere chain are recomputed. The attempt's script
is not imported. The seeded Monte Carlo was not repeated, and the
concentration premises A1-A2 are not proved.
"""
from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction as F

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def add(*vectors):
    return tuple(sum(component) for component in zip(*vectors))


def sphere(p, q):
    """Rational point on S^2 from the stereographic parameters p, q."""
    denom = p * p + q * q + 1
    return (2 * p / denom, 2 * q / denom, (p * p + q * q - 1) / denom)


kappa = sp.symbols("kappa", positive=True)
weight = sp.symbols("w")
partition = sp.integrate(sp.exp(kappa * weight), (weight, -1, 1))
mean = sp.integrate(weight * sp.exp(kappa * weight), (weight, -1, 1)) / partition
second = sp.integrate(weight ** 2 * sp.exp(kappa * weight), (weight, -1, 1)) / partition
third = sp.integrate(weight ** 3 * sp.exp(kappa * weight), (weight, -1, 1)) / partition
langevin = sp.coth(kappa) - 1 / kappa
moment_targets = (
    mean - langevin,
    second - (1 - 2 * langevin / kappa),
    third - (sp.coth(kappa) - 3 / kappa + 6 * langevin / kappa ** 2),
)
check(
    "S1 moments",
    all(sp.simplify(item.rewrite(sp.exp)) == 0 for item in moment_targets),
    "E w = A, E w^2 = 1 - 2A/kappa, E w^3 = coth kappa - 3/kappa + 6A/kappa^2",
)
third_moment = mean - third - langevin * (1 - second)
third_target = 2 / kappa - 6 * langevin / kappa ** 2 - 2 * langevin ** 2 / kappa
check(
    "S6 third moment",
    sp.simplify((third_moment - third_target).rewrite(sp.exp)) == 0,
    "E[(1-w^2)(w-A)] = 2/kappa - 6A/kappa^2 - 2A^2/kappa",
)

tilt, noise_b, noise_l = sp.symbols("alpha b l", real=True)
normal = sp.Matrix([0, 0, 1])
direction = sp.Matrix([sp.sin(tilt), 0, sp.cos(tilt)])
covariance = noise_b * (sp.eye(3) - direction * direction.T) + noise_l * direction * direction.T
transverse = sp.eye(3) - normal * normal.T
trace_target = noise_b * (1 + sp.cos(tilt) ** 2) + noise_l * (1 - sp.cos(tilt) ** 2)
check(
    "S5 transverse noise",
    sp.simplify((transverse * covariance).trace() - trace_target) == 0,
    "E|eta^perp|^2 = b(1+c^2) + l(1-c^2)",
)

slope, separation = sp.symbols("beta q", positive=True)
local_span = 3 - separation / 2
model_gain = lambda field: (1 - 1 / field) / field
model_ratio = model_gain(slope * local_span) / model_gain(3 * slope)
ratio_error = sp.together(model_ratio - 6 / (6 - separation))
closed_gain = lambda field: 1 - 1 / field + 2 / (sp.exp(2 * field) - 1)
gain_identity = sp.simplify((langevin - closed_gain(kappa)).rewrite(sp.exp))
tail = sp.simplify(closed_gain(kappa) / kappa - model_gain(kappa) - 2 / (kappa * (sp.exp(2 * kappa) - 1)))
weak_series = sp.series(6 / (6 - separation), separation, 0, 2).removeO()
check(
    "S4 local noise",
    gain_identity == 0
    and tail == 0
    and sp.simplify(ratio_error * (3 * slope - 1) * (6 - separation) ** 2 + 6 * separation) == 0
    and weak_series == 1 + separation / 6,
    "A = 1 - 1/kappa + 2/(e^{2 kappa}-1), and the power-law part of b/sigma^2 is 1 + q/6",
)

pairs = [(F(p), F(q)) for p in range(-2, 3) for q in range(-2, 3)]
drift_ok = True
for side in (2, 3):
    for shift in (0, 7, 13):
        records = {}
        for n, (i, j) in enumerate(itertools.product(range(side), repeat=2)):
            p, q = pairs[(n + shift) % len(pairs)]
            records[(i, j)] = sphere(p, q)
            drift_ok = drift_ok and dot(records[(i, j)], records[(i, j)]) == 1
        fields = {}
        for i, j in itertools.product(range(side), repeat=2):
            fields[(i, j)] = add(
                records[(i, j)],
                records[((i - 1) % side, j)],
                records[(i, (j - 1) % side)],
            )
        total_field = add(*fields.values())
        total_record = add(*records.values())
        drift_ok = drift_ok and total_field == tuple(3 * component for component in total_record)
        for (i, j), field in fields.items():
            predecessors = [
                records[(i, j)],
                records[((i - 1) % side, j)],
                records[(i, (j - 1) % side)],
            ]
            separation_sum = 0
            for left, right in ((0, 1), (0, 2), (1, 2)):
                difference = tuple(
                    predecessors[left][axis] - predecessors[right][axis] for axis in range(3)
                )
                separation_sum += dot(difference, difference)
            drift_ok = drift_ok and dot(field, field) == 9 - separation_sum
        average = tuple(component / (side * side) for component in total_record)
        average_norm = dot(average, average)
        drift_ok = drift_ok and average_norm != 0
        def transverse_part(vector, origin=average, origin_norm=average_norm):
            scale = dot(vector, origin) / origin_norm
            return tuple(vector[axis] - scale * origin[axis] for axis in range(3))
        drift_ok = drift_ok and transverse_part(total_field) == (0, 0, 0)
        heights = {(i, j): F(i - 2 * j + 1 + shift, 3) for i, j in fields}
        baseline = F(shift - 1, 4)
        weighted = add(*[tuple(heights[key] * c for c in transverse_part(fields[key])) for key in fields])
        shifted = add(*[tuple((heights[key] - baseline) * c for c in transverse_part(fields[key])) for key in fields])
        drift_ok = drift_ok and weighted == shifted
check(
    "D identities",
    drift_ok,
    "sum S = 3 sum s, |S|^2 = 9 - sum_{i<j}|s_i-s_j|^2, and the transverse drift depends only on h_x - hbar",
)


def cosine(index, side):
    reduced = index % side
    table = {
        2: {0: F(1), 1: F(-1)},
        3: {0: F(1), 1: F(-1, 2), 2: F(-1, 2)},
        4: {0: F(1), 1: F(0), 2: F(-1), 3: F(0)},
        6: {0: F(1), 1: F(1, 2), 2: F(-1, 2), 3: F(-1), 4: F(-1, 2), 5: F(1, 2)},
    }
    return table[side][reduced]


def structure_factor(side):
    total = F(0)
    for n1, n2 in itertools.product(range(side), repeat=2):
        if n1 == 0 and n2 == 0:
            continue
        mode = (3 + 2 * cosine(n1, side) + 2 * cosine(n2, side) + 2 * cosine(n1 - n2, side)) / 9
        total += 1 / (1 - mode)
    return total / (side * side)


stars = {side: structure_factor(side) for side in (2, 3, 4, 6)}
check(
    "C1 modes",
    [stars[side] for side in (2, 3, 4, 6)] == [F(27, 32), F(11, 9), F(189, 128), F(2627, 1440)],
    "S*_2,3,4,6 = 27/32, 11/9, 189/128, 2627/1440",
)


def circulant_moments(side):
    sites = [(i, j) for i in range(side) for j in range(side)]
    place = {site: n for n, site in enumerate(sites)}
    steps = [(0, 0), (1, 0), (0, 1)]
    rows = []
    targets = []
    for site in sites:
        row = [sp.Integer(0)] * len(sites)
        row[place[site]] = 1
        for left in steps:
            for right in steps:
                source = (
                    (site[0] - left[0] + right[0]) % side,
                    (site[1] - left[1] + right[1]) % side,
                )
                row[place[source]] -= sp.Rational(1, 9)
        rows.append(row)
        targets.append((1 if site == (0, 0) else 0) - sp.Rational(1, side * side))
    square = sp.Matrix(rows[:-1] + [[sp.Integer(1)] * len(sites)])
    image = sp.Matrix(targets[:-1] + [0])
    solution = square.solve(image)
    residual = sp.Matrix(rows) * solution - sp.Matrix(targets)
    values = {site: sp.together(solution[place[site]]) for site in sites}
    projected = sum(values[((right[0] - left[0]) % side, (right[1] - left[1]) % side)] for left in steps for right in steps) / 9
    return values, residual, projected


lyapunov_ok = True
for side in (2, 3, 4):
    values, residual, projected = circulant_moments(side)
    star = stars[side]
    lyapunov_ok = lyapunov_ok and all(sp.simplify(entry) == 0 for entry in residual)
    lyapunov_ok = lyapunov_ok and values[(0, 0)] == star
    lyapunov_ok = lyapunov_ok and sp.simplify(projected - (star - 1 + F(1, side * side))) == 0
check(
    "C2 Lyapunov",
    lyapunov_ok,
    "for L=2,3,4 the circulant solution has c(0,0)=S* and E(P pi)^2 = S* - 1 + 1/L^2",
)

chord = sp.symbols("X", positive=True)
chord_series = sp.series(1 - 1 / sp.sqrt(1 + chord), chord, 0, 3).removeO()
check(
    "S8 chord",
    sp.expand(chord_series - (chord / 2 - sp.Rational(3, 8) * chord ** 2)) == 0,
    "1 - n·n' = X/2 - (3/8) X^2 + O(X^3), X = |b|^2/(m+a)^2",
)

variance, star_symbol, inverse_area = sp.symbols("sigma2 S invL", positive=True)
transverse_noise = 2 * variance * inverse_area * (1 - star_symbol * variance + 2 * variance * (1 - inverse_area))
magnitude = 1 - star_symbol * variance
longitudinal = -variance * inverse_area
mixed = -2 * variance ** 2 * inverse_area ** 2
fourth = 2 * transverse_noise ** 2
one_level = (
    transverse_noise / (2 * magnitude ** 2)
    - (transverse_noise * longitudinal + mixed) / magnitude ** 3
    - sp.Rational(3, 8) * fourth / magnitude ** 4
)
one_series = sp.series(one_level / (variance * inverse_area), variance, 0, 2).removeO()
memory_series = sp.series(-sp.log(1 - one_level) / (variance * inverse_area), variance, 0, 2).removeO()
magnetisation_series = sp.series(1 / magnitude ** 2, variance, 0, 2).removeO()
one_poly = sp.Poly(sp.expand(one_series), variance)
memory_poly = sp.Poly(sp.expand(memory_series), variance)
magnetisation_poly = sp.Poly(sp.expand(magnetisation_series), variance)
check(
    "F coefficients",
    one_poly.coeff_monomial(1) == 1
    and sp.simplify(one_poly.coeff_monomial(variance) - (star_symbol + 2 - inverse_area)) == 0
    and memory_poly.coeff_monomial(1) == 1
    and sp.simplify(memory_poly.coeff_monomial(variance) - (star_symbol + 2 - inverse_area / 2)) == 0
    and magnetisation_poly.coeff_monomial(1) == 1
    and magnetisation_poly.coeff_monomial(variance) == 2 * star_symbol
    and sp.simplify(memory_poly.coeff_monomial(variance).subs({star_symbol: 0, inverse_area: 1}) - sp.Rational(3, 2)) == 0,
    "x1 tau and lambda1 tau open at 1, with slopes S*+2-1/L^2 and S*+2-1/(2L^2); 1/|M|^2 has slope 2 S*",
)

exact_gaps = {
    2: F(33, 32),
    3: F(13, 18),
    4: F(63, 128),
    6: F(233, 1440),
}
gaps = {side: 2 - F(1, 2 * side * side) - stars[side] for side in (2, 3, 4, 6)}
def numeric_structure(side):
    total = 0.0
    for n1, n2 in itertools.product(range(side), repeat=2):
        if n1 == 0 and n2 == 0:
            continue
        mode = (
            3
            + 2 * math.cos(2 * math.pi * n1 / side)
            + 2 * math.cos(2 * math.pi * n2 / side)
            + 2 * math.cos(2 * math.pi * (n1 - n2) / side)
        ) / 9
        total += 1 / (1 - mode)
    return total / side ** 2
numeric_gaps = {side: 2 - 1 / (2 * side * side) - numeric_structure(side) for side in (5, 7, 8, 9, 10, 16, 32, 64)}
check(
    "F4 gap",
    gaps == exact_gaps
    and all(numeric_gaps[side] > 1e-3 for side in (5, 7))
    and all(numeric_gaps[side] < -1e-3 for side in (8, 9, 10, 16, 32, 64)),
    "exact gaps 33/32, 13/18, 63/128, 233/1440; positive at L=5,7 and negative at L=8,9,10,16,32,64",
)

scale = sp.symbols("t")
wave_1, wave_2 = sp.symbols("a b")
mode_symbol = (
    3
    + 2 * sp.cos(scale * wave_1)
    + 2 * sp.cos(scale * wave_2)
    + 2 * sp.cos(scale * (wave_1 - wave_2))
) / 9
quadratic = wave_1 ** 2 - wave_1 * wave_2 + wave_2 ** 2
small_mode = sp.series(1 - mode_symbol, scale, 0, 4).removeO()
angle = sp.symbols("theta")
angular = sp.integrate(1 / (1 - sp.sin(2 * angle) / 2), (angle, 0, 2 * sp.pi))
# 1-u ~ (2/9) Q, so 1/(1-u) ~ (9/2)/Q. The angular integral of 1/Q is `angular`.
# S* ~ [angular * (9/2) / (4 pi^2)] log(1/epsilon) = 2 c0 log, c0 = 3 sqrt(3)/(4 pi).
continuum = sp.simplify(angular * sp.Rational(9, 2) / (4 * sp.pi ** 2))
c0 = 3 * sp.sqrt(3) / (4 * sp.pi)
check(
    "F log coefficient",
    sp.expand(small_mode - sp.Rational(2, 9) * quadratic * scale ** 2) == 0
    and sp.simplify(angular - 4 * sp.pi / sp.sqrt(3)) == 0
    and sp.simplify(continuum - 2 * c0) == 0,
    "1-u = (2/9)(k1^2 - k1 k2 + k2^2) + O(k^4), and the log coefficient is 2 c0 with c0 = 3 sqrt(3)/(4 pi)",
)

positive_gain = kappa * sp.cosh(kappa) - sp.sinh(kappa)
excess = sp.exp(2 * kappa) - 1 - 2 * kappa - 2 * kappa ** 2
height, width, depth = sp.symbols("s t u", real=True)
triple = sp.integrate(sp.integrate(sp.integrate(8 * sp.exp(2 * depth), (depth, 0, height)), (height, 0, width)), (width, 0, kappa))
identity_gap = (langevin - kappa / (kappa + 1)) - (
    (2 * kappa ** 2 + 2 * kappa - (sp.exp(2 * kappa) - 1)) / ((sp.exp(2 * kappa) - 1) * (kappa ** 2 + kappa))
)
denominator = (sp.exp(2 * kappa) - 1) * kappa * (kappa + 1)
split = (1 - langevin - langevin / kappa) - excess * (kappa + 1) / (kappa * denominator)
log_gap = -sp.log(1 - scale) - scale
check(
    "E single site",
    sp.simplify(positive_gain.subs(kappa, 0)) == 0
    and sp.simplify(sp.diff(positive_gain, kappa) - kappa * sp.sinh(kappa)) == 0
    and sp.simplify(sp.integrate(height * sp.sinh(height), (height, 0, kappa)) - positive_gain) == 0
    and sp.simplify(sp.cosh(kappa) - (sp.exp(kappa) + sp.exp(-kappa)) / 2) == 0
    and sp.simplify(identity_gap.rewrite(sp.exp)) == 0
    and sp.simplify(excess.subs(kappa, 0)) == 0
    and sp.simplify(sp.diff(excess, kappa).subs(kappa, 0)) == 0
    and sp.simplify(sp.diff(excess, kappa, 2).subs(kappa, 0)) == 0
    and sp.simplify(sp.diff(excess, kappa, 3) - 8 * sp.exp(2 * kappa)) == 0
    and sp.simplify(triple - excess) == 0
    and sp.simplify(split.rewrite(sp.exp)) == 0
    and sp.simplify(log_gap.subs(scale, 0)) == 0
    and sp.simplify(sp.diff(log_gap, scale) - scale / (1 - scale)) == 0
    and all(-k * math.log(1 / math.tanh(k) - 1 / k) / (1 / math.tanh(k) - 1 / k) > 1 for k in (F(1, 5), 1, 3, 12)),
    "A < kappa/(kappa+1) < 1, so -kappa log A/A > 1 for every kappa > 0",
)

deviation = sp.symbols("x", positive=True)
model_rate = -sp.log(1 - deviation) / ((1 - deviation) * deviation)
model_variance = (1 - deviation) * deviation
model_difference = sp.series(model_rate - (1 + sp.Rational(3, 2) * model_variance), deviation, 0, 2).removeO()
check(
    "E large beta",
    sp.simplify(model_difference) == 0,
    "dropping the exponential tail, lambda1 tau1 = 1 + (3/2) sigma^2 + O(sigma^4), and this is the L=1 case of the memory law",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. The drift identities, the single-site inequality "
    "-3 beta log A(3 beta)/A(3 beta) > 1, and the first-order law under premises A1-A2 all hold. "
    "S*_2,3,4,6 = 27/32, 11/9, 189/128, 2627/1440. The gap 2 - 1/(2 L^2) - S* equals "
    "33/32, 13/18, 63/128, 233/1440 at those sides, stays positive at L=5 and L=7, and is negative "
    "at L=8,9,10,16,32,64. The log coefficient is 2 c0 sigma^2 with c0 = 3 sqrt(3)/(4 pi). "
    "The additive continuum offset, the seeded Monte Carlo, and premises A1-A2 were not proved.",
    flush=True,
)
print(
    "HIT: confirmed - the 1/|m|^2 factor is not the strong-coupling memory law: "
    "lambda1 tau_L = 1 + sigma^2 (S*_L + 2 - 1/(2 L^2)) under A1-A2, "
    "and at one site the rate exceeds 1 for every beta",
    flush=True,
)
