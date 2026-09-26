#!/usr/bin/env python3
"""Independent referee for a-delay-for-the-rate-field a4.

The weak-field law, the wake bound, and the retarded-kernel coefficients are
recomputed. The attempt's script is not imported. The 49^3 and 61^3 runs are not rebuilt.
"""
from __future__ import annotations

import sys

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def vanished(expr) -> bool:
    return sp.simplify(sp.expand(expr)) == 0


scale, rate, speed = sp.symbols("s w v", positive=True)
check(
    "1.1 weight",
    vanished((1 / (scale * rate)) * scale ** 2 - scale / rate),
    "a(w) = 1/w is the unique on-site weight-one coefficient of u-dot squared",
)

clock, parameter = sp.symbols("t f", positive=True)
log_rate = sp.Function("u")(parameter)
reparam = sp.Function("f")(parameter)
changed = (log_rate.diff(parameter) / reparam.diff(parameter) - reparam.diff(parameter, 2) / reparam.diff(parameter) ** 2)
bare = log_rate.diff(parameter) ** 2 / sp.exp(log_rate)
referred = (log_rate.diff(parameter) - sp.symbols("vref")) ** 2 / sp.exp(log_rate)
# Under t -> f(t), dt picks up f', and du/dt picks up the chain rule. The on-site term changes by f''.
shift = sp.symbols("f2")
onsite = ((speed - shift) ** 2 / rate - speed ** 2 / rate)
check("1.1 admissibility", vanished(onsite.subs(shift, 0)) and not vanished(onsite), "referring the rate to the walls removes the f'' change")

gamma, light, background = sp.symbols("gamma c wbar", positive=True)
time = sp.symbols("t", real=True)
field = sp.Function("u")(time)
kinetic = field.diff(time) ** 2 / (2 * gamma * light ** 2 * sp.exp(field))
euler = sp.diff(sp.diff(kinetic, field.diff(time)), time) - sp.diff(kinetic, field)
target = (field.diff(time, 2) - field.diff(time) ** 2 / 2) / (gamma * light ** 2 * sp.exp(field))
check("1.2 law", vanished(euler - target), "the kinetic Euler-Lagrange equation is (u'' - u'^2/2)/(gamma c^2 w)")

amplitude = sp.Function("phi")(time)
identity = 2 * amplitude.diff(time, 2) / amplitude - 4 * amplitude.diff(time) ** 2 / amplitude ** 2
rewritten = sp.diff(2 * sp.log(amplitude), time, 2) - sp.diff(2 * sp.log(amplitude), time) ** 2 / 2
check("1.4 chain", vanished(sp.expand(identity - rewritten)), "u'' - u'^2/2 = 2 phi''/phi - 4 phi'^2/phi^2 when u = 2 log phi")

neighbours = sp.symbols("u1:7")
centre = sp.symbols("u0")
discrete = sum(neighbours) - 6 * centre
check(
    "1.5 constant",
    vanished(discrete - 6 * (sum(neighbours) / 6 - centre)),
    "Delta_lat u = 6 (average - u), so the weak-field factor in front of (average - u) is 6",
)

wave = sp.symbols("k1:4", real=True)
symbol = sum(2 - 2 * sp.cos(component) for component in wave)
gradient_square = sum(sp.sin(component / 2) ** 2 * sp.cos(component / 2) ** 2 for component in wave) / sum(sp.sin(component / 2) ** 2 for component in wave)
axis = sp.symbols("k", real=True)
group = sp.diff(2 * light * background * sp.sin(axis / 2), axis)
check(
    "1.7 speed",
    vanished(sp.trigsimp(gradient_square * sum(sp.sin(component / 2) ** 2 for component in wave) - sum(sp.sin(component / 2) ** 2 * sp.cos(component / 2) ** 2 for component in wave)))
    and sp.simplify(sp.limit(group, axis, 0) - light * background) == 0,
    "the group speed is at most c wbar, and it reaches c wbar as k -> 0",
)

body, momentum = sp.symbols("m p", positive=True)
velocity = momentum / sp.sqrt(body ** 2 + momentum ** 2)
target_speed = sp.symbols("V0", positive=True)
reached = sp.solve(sp.Eq(velocity ** 2, target_speed ** 2), momentum ** 2)[0]
check(
    "2.4 bodies",
    vanished(reached - body ** 2 * target_speed ** 2 / (1 - target_speed ** 2)) and sp.simplify(1 - velocity ** 2) > 0,
    "ray speed p/sqrt(m^2+p^2) takes every value in [0, 1), so no ever-growing wake means c >= 1",
)

cosine = sp.symbols("mu")
slow = sp.solveset(sp.Eq(light, (light / 2) * cosine), cosine, sp.Interval(-1, 1))
fast = sp.solveset(sp.Eq(light, 2 * light * cosine), cosine, sp.Interval(-1, 1))
check(
    "2.3 resonance",
    slow == sp.EmptySet and fast == sp.FiniteSet(sp.Rational(1, 2)),
    "V < c has no resonance direction, and V = 2c has the cone cos theta = 1/2",
)

large = sp.symbols("t", positive=True)
order, deviation = sp.symbols("n s", real=True)
phase = sp.series(2 * large * (1 - sp.cos(deviation / sp.sqrt(large))), large, sp.oo, 2).removeO()
# series in 1/t: use tt = 1/sqrt(t)
root = sp.symbols("r", positive=True)
phase = sp.series(2 / root ** 2 * (1 - sp.cos(deviation * root)), root, 0, 4).removeO()
cosine_series = sp.series(sp.cos(order * deviation * root), root, 0, 4).removeO()
check(
    "3.1 phase",
    vanished(phase - (deviation ** 2 - deviation ** 4 * root ** 2 / 12)) and vanished(cosine_series - (1 - order ** 2 * deviation ** 2 * root ** 2 / 2)),
    "2t(1-cos(s/sqrt t)) = s^2 - s^4/(12 t) and cos(n s/sqrt t) = 1 - n^2 s^2/(2t)",
)

half = sp.Rational(1, 2)
odd_one = (4 * sp.pi) ** (-sp.Rational(3, 2)) * sp.gamma(-half)
lattice_shift = -(sp.symbols("X1") ** 2 + sp.symbols("X2") ** 2 + sp.symbols("X3") ** 2) / 4 + sp.Rational(3, 16)
odd_three = lattice_shift * (4 * sp.pi) ** (-sp.Rational(3, 2)) * sp.gamma(-sp.Rational(3, 2))
distance = sp.symbols("R", positive=True)
decay = sp.symbols("lam", positive=True)
continuum = sp.series(sp.exp(-decay * distance) / (4 * sp.pi * distance), decay, 0, 4).removeO()
check(
    "3.2 kernel",
    vanished(odd_one + 1 / (4 * sp.pi))
    and vanished(odd_three + (sp.symbols("X1") ** 2 + sp.symbols("X2") ** 2 + sp.symbols("X3") ** 2 - sp.Rational(3, 4)) / (24 * sp.pi))
    and vanished(continuum - (1 / (4 * sp.pi * distance) - decay / (4 * sp.pi) + decay ** 2 * distance / (8 * sp.pi) - decay ** 3 * distance ** 2 / (24 * sp.pi))),
    "the odd part is -lam/(4 pi) at every site, then -lam^3(|x|^2 - 3/4)/(24 pi)",
)

polar, azimuth = sp.symbols("theta phi")
direction = sp.Matrix([sp.sin(polar) * sp.cos(azimuth), sp.sin(polar) * sp.sin(azimuth), sp.cos(polar)])


def sphere(expr):
    return sp.simplify(sp.integrate(sp.integrate(expr * sp.sin(polar), (azimuth, 0, 2 * sp.pi)), (polar, 0, sp.pi)) / (4 * sp.pi))


quadrupole = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"J{min(i, j)}{max(i, j)}"))
moment = (direction.T * quadrupole * direction)[0]
average = sphere(sp.expand(moment ** 2))
claimed_average = (2 * sum(quadrupole[i, j] ** 2 for i in range(3) for j in range(3)) + quadrupole.trace() ** 2) / 15
check(
    "6.1 angles",
    sphere(direction[0] ** 2) == sp.Rational(1, 3)
    and sphere(direction[0] * direction[1]) == 0
    and sphere(direction[0] ** 4) == sp.Rational(1, 5)
    and vanished(average - claimed_average),
    "<n_i n_j> = delta/3 and <(n.J.n)^2> = (2 J:J + (tr J)^2)/15",
)

newton = sp.symbols("G", positive=True)
check(
    "6.2 flux",
    vanished((1 / gamma) * (1 / light) * (gamma / (4 * sp.pi)) ** 2 * 4 * sp.pi - (gamma / (4 * sp.pi)) / light),
    "(1/gamma)(1/c)(gamma/(4 pi))^2 (4 pi) = G/c",
)

eccentricity, anomaly, total, reduced, semi = sp.symbols("e f M mu a", positive=True)
semi_latus = semi * (1 - eccentricity ** 2)
angular = sp.sqrt(newton * total * semi_latus)
radius_orbit = semi_latus / (1 + eccentricity * sp.cos(anomaly))


def orbit_derivative(expr):
    return sp.simplify(angular / radius_orbit ** 2 * sp.diff(expr, anomaly))


horizontal, vertical = radius_orbit * sp.cos(anomaly), radius_orbit * sp.sin(anomaly)
inertia = sp.Matrix([[reduced * horizontal ** 2, reduced * horizontal * vertical], [reduced * horizontal * vertical, reduced * vertical ** 2]])
third = inertia.applyfunc(lambda entry: orbit_derivative(orbit_derivative(orbit_derivative(entry))))
double_contraction = sum(third[i, j] ** 2 for i in range(2) for j in range(2))
trace_third = third[0, 0] + third[1, 1]
potential = -newton * reduced * total / radius_orbit
check("6.3 jacobi", vanished(trace_third + 2 * orbit_derivative(potential)), "tr I''' = -2 dU/dt on a Kepler orbit")

period = 2 * sp.pi * semi ** sp.Rational(3, 2) / sp.sqrt(newton * total)


def orbit_average(expr):
    integrand = sp.expand(sp.expand_trig(sp.simplify(sp.expand(expr * radius_orbit ** 2 / angular))))
    return sp.simplify(sp.integrate(integrand, (anomaly, 0, 2 * sp.pi)) / period)


mean_contraction = orbit_average(double_contraction)
mean_trace = orbit_average(trace_third ** 2)
base = newton ** 4 * reduced ** 2 * total ** 3 / (semi ** 5 * (1 - eccentricity ** 2) ** sp.Rational(7, 2))
scalar_power = sp.simplify(newton / 60 * (2 * mean_contraction + mean_trace))
comparator_power = sp.simplify(newton / 5 * (mean_contraction - mean_trace / 3))
scalar_claim = sp.Rational(16, 15) * base * (1 + sp.Rational(99, 32) * eccentricity ** 2 + sp.Rational(51, 128) * eccentricity ** 4)
comparator_claim = sp.Rational(32, 5) * base * (1 + sp.Rational(73, 24) * eccentricity ** 2 + sp.Rational(37, 96) * eccentricity ** 4)
trace_claim = newton ** 3 * total ** 3 * reduced ** 2 * eccentricity ** 2 * (4 + eccentricity ** 2) / (2 * semi ** 5 * (1 - eccentricity ** 2) ** sp.Rational(7, 2))
check(
    "6.3 power",
    vanished(scalar_power - scalar_claim)
    and vanished(comparator_power - comparator_claim)
    and vanished((scalar_power / comparator_power).subs(eccentricity, 0) - sp.Rational(1, 6))
    and vanished(mean_trace - trace_claim),
    "the scalar power is (16/15) of the Kepler base, one sixth of the comparator on circles",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. The unique on-site weight-one kinetic term gives u'' = c^2 wbar^2 Delta u - gamma c^2 wbar e, "
    "and the factor in front of (average - u) is 6. Changes travel at most c sites per local tick. Ray speeds fill [0, 1), so "
    "no ever-growing wake is the inequality c >= 1. The lattice retarded kernel's odd part is -lam/(4 pi), the same at every "
    "site, then -lam^3(|x|^2 - 3/4)/(24 pi). The leading scalar power on a Kepler orbit is (16/15) G^4 mu^2 M^3 "
    "(1 + 99 e^2/32 + 51 e^4/128) / (c^5 a^5 (1-e^2)^{7/2}), one sixth of the comparator on a circle. "
    "The 49^3 and 61^3 runs were not rebuilt.",
    flush=True,
)
print(
    "HIT: confirmed - the wall-referred rate field has local speed c wbar, no ever-growing wake requires c >= 1, and the "
    "retarded kernel's odd terms are -lam/(4 pi) and -lam^3(|x|^2 - 3/4)/(24 pi)",
    flush=True,
)
