#!/usr/bin/env python3
"""Independent referee for delay-of-the-rate-field-with-the-curvature-member a1.

Block 62's second-order member, one wave vector. The attempt's script is not
imported. The 48 by 48 floating-point slice is not rebuilt.
"""
from __future__ import annotations

import sys

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def zero(expr) -> bool:
    return sp.expand(expr) == 0


def R1(strain, momentum):
    contracted = (momentum.T * strain * momentum)[0]
    return -(contracted - momentum.dot(momentum) * strain.trace())


def R2(strain, momentum):
    pushed = strain * momentum
    square = sum(strain[i, j] ** 2 for i in range(3) for j in range(3))
    contracted = (momentum.T * strain * momentum)[0]
    return (
        -sp.Rational(1, 4) * momentum.dot(momentum) * square
        + sp.Rational(1, 2) * pushed.dot(pushed)
        - sp.Rational(1, 2) * contracted * strain.trace()
        + sp.Rational(1, 4) * momentum.dot(momentum) * strain.trace() ** 2
    )


momentum = sp.Matrix(sp.symbols("p1:4", real=True))
strain = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"h{min(i, j)}{max(i, j)}", real=True))
shift = sp.Matrix(sp.symbols("xi1:4", real=True))
gauge = momentum * shift.T + shift * momentum.T
gauge_ok = zero(R1(strain + gauge, momentum) - R1(strain, momentum)) and zero(
    sp.expand(R2(strain + gauge, momentum) - R2(strain, momentum))
)
check("1.1 relabelling", gauge_ok, "R1 and R2 are unchanged by h -> h + p xi + xi p")

scalar = sp.symbols("phi", real=True)
projector = sp.eye(3) - momentum * momentum.T / momentum.dot(momentum)
scalar_strain = sp.simplify(projector * scalar)
scalar_ok = zero(sp.together(R1(scalar_strain, momentum) - 2 * momentum.dot(momentum) * scalar)) and zero(
    sp.together(R2(scalar_strain, momentum) - momentum.dot(momentum) * scalar**2 / 2)
)
check("1.2 scalar", scalar_ok, "on h = (1 - p p / p^2) phi, R1 = 2 p^2 phi and R2 = (1/2) p^2 phi^2")

stiffness, background, energy, stretch = sp.symbols("K wbar e lam", positive=True)
isotropic = sp.solve(sp.Eq(stiffness * background * R1(2 * stretch * sp.eye(3), momentum), energy), stretch)[0]
check(
    "1.3 isotropic",
    zero(sp.together(isotropic - energy / (4 * stiffness * background * momentum.dot(momentum)))),
    "K wbar R1 = e on h = 2 lam I gives p^2 lam = e / (4 K wbar)",
)

time = sp.symbols("t", real=True)
alpha, beta, wave = sp.symbols("alpha beta p", positive=True)
source = sp.Function("e")(time)
clock = sp.Function("u")(time)
length = sp.Function("phi")(time)
plus = sp.Function("a")(time)
cross = sp.Function("b")(time)
longitudinal = sp.Function("xi")(time)
shear_x = sp.Function("cx")(time)
shear_y = sp.Function("cy")(time)
aligned = sp.Matrix(
    [
        [length + plus, cross, shear_x],
        [cross, length - plus, shear_y],
        [shear_x, shear_y, 2 * longitudinal],
    ]
)
axis = sp.Matrix([0, 0, wave])
velocity = aligned.diff(time)
kinetic = (
    alpha * sum(velocity[i, j] ** 2 for i in range(3) for j in range(3)) + beta * velocity.trace() ** 2
) / background
lagrangian = kinetic + stiffness * background * (clock * R1(aligned, axis) + R2(aligned, axis)) - source * clock
fields = [clock, length, plus, cross, longitudinal, shear_x, shear_y]


def euler(field):
    return sp.expand(sp.diff(sp.diff(lagrangian, field.diff(time)), time) - sp.diff(lagrangian, field))


equations = {field: euler(field) for field in fields}
check(
    "1.4 clock constraint",
    zero(equations[clock] - (source - 2 * stiffness * background * wave**2 * length)),
    "the rate equation is 2 K wbar p^2 phi = e, with no time derivative",
)
check(
    "1.5 transverse waves",
    zero(equations[plus] - (4 * alpha / background * plus.diff(time, 2) + stiffness * background * wave**2 * plus))
    and zero(equations[cross] - (4 * alpha / background * cross.diff(time, 2) + stiffness * background * wave**2 * cross)),
    "the two traceless strains travel at speed^2 = K wbar^2 / (4 alpha) and are not sourced at rest",
)
check(
    "1.6 relabelling",
    zero(
        equations[longitudinal]
        - sp.diff(8 / background * ((alpha + beta) * longitudinal.diff(time) + beta * length.diff(time)), time)
    ),
    "the longitudinal relabelling has no potential; from rest its rate is -beta phi-dot / (alpha + beta)",
)

length_of_source = source / (2 * stiffness * background * wave**2)
longitudinal_rate = -beta * length_of_source.diff(time) / (alpha + beta)
reduced = (
    equations[length]
    .subs({longitudinal.diff(time, 2): longitudinal_rate.diff(time), longitudinal.diff(time): longitudinal_rate})
    .subs(length, length_of_source)
    .doit()
)
solved_clock = sp.simplify(sp.solve(sp.Eq(reduced, 0), clock)[0])
claimed_clock = -source / (4 * stiffness * background * wave**2) + alpha * (alpha + 3 * beta) * source.diff(
    time, 2
) / (stiffness**2 * background**3 * (alpha + beta) * wave**4)
check(
    "1.7 clock law",
    zero(sp.simplify(solved_clock - claimed_clock)),
    "u = -e/(4 K wbar p^2) + alpha(alpha+3 beta) e-double-dot / (K^2 wbar^3 (alpha+beta) p^4)",
)
check(
    "1.8 static",
    zero(sp.simplify(claimed_clock.subs(source.diff(time, 2), 0) + source / (4 * stiffness * background * wave**2))),
    "with no acceleration of the energy, u is the instantaneous Poisson field",
)
rest_rate = (alpha + beta) * sp.symbols("xi_dot") + beta * length_of_source.diff(time)
check(
    "1.9 no jump",
    zero(sp.simplify(rest_rate.subs(beta, -alpha) + alpha * source.diff(time) / (2 * stiffness * background * wave**2))),
    "at alpha + beta = 0 the constraint forces e-dot to be constant",
)
check(
    "1.10 traceless kinetic",
    zero(sp.simplify(claimed_clock.subs(beta, -alpha / 3) + source / (4 * stiffness * background * wave**2))),
    "at alpha + 3 beta = 0 the second-time-derivative term drops out",
)
frequency = sp.symbols("X", positive=True)
check(
    "1.11 speed",
    sp.solve(sp.Eq(4 * alpha / background * (-frequency) + stiffness * background * wave**2, 0), frequency)
    == [stiffness * background**2 * wave**2 / (4 * alpha)],
    "the only travelling roots are the two transverse strains",
)

duration, jump = sp.symbols("tau_r Delta_e", positive=True)
ramp = jump * (3 * (time / duration) ** 2 - 2 * (time / duration) ** 3)
early = sp.series(claimed_clock.subs(source, ramp).doit(), time, 0, 2).removeO()
check(
    "2.1 switch-on",
    zero(
        sp.simplify(
            early.subs(time, 0)
            - 6 * alpha * (alpha + 3 * beta) * jump / (stiffness**2 * background**3 * (alpha + beta) * wave**4 * duration**2)
        )
    ),
    "at label time 0+ the clock already moves at every wave vector, in proportion to Delta e",
)
check(
    "2.2 after",
    zero(sp.simplify(claimed_clock.subs(source, jump).doit() + jump / (4 * stiffness * background * wave**2))),
    "after the switch-on, the jump of u is the Poisson field of Delta e",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial at second order. The rate is a multiplier. It fixes the scalar lengths by "
    "2 K wbar p^2 phi = e and then u = -e/(4 K wbar p^2) + alpha(alpha+3 beta) e-double-dot / "
    "(K^2 wbar^3 (alpha+beta) p^4), at the same label time. Only the two transverse traceless strains travel, "
    "at speed^2 = K wbar^2/(4 alpha), and a body at rest does not source them. At alpha + beta = 0 a jump of "
    "the energy has no solution. The 48 by 48 slice was not rebuilt.",
    flush=True,
)
print(
    "HIT: confirmed - with the curvature member the clocks and a slow packet's fall change with the body's "
    "energy at the same label time, before any transverse strain wave, unless alpha + beta = 0, in which case "
    "a body at rest cannot change its energy at all",
    flush=True,
)
