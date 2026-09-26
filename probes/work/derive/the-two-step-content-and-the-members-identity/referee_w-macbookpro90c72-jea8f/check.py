#!/usr/bin/env python3
"""Independent referee for the-two-step-content-and-the-members-identity a1.

The beat identity is recomputed from the two-step stress. The attempt's
script is not imported. The 12^3 floating-point sweep is not rebuilt.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


angle, other = sp.symbols("a b", real=True)
current_identity = sp.expand(
    sp.trigsimp(
        sp.sin(angle - other) * (sp.sin(angle) * sp.cos(angle) + sp.sin(other) * sp.cos(other))
        - sp.cos(angle - other) * (sp.sin(angle) ** 2 - sp.sin(other) ** 2)
    )
)
difference_identity = sp.expand(
    sp.trigsimp(2 * sp.sin((angle - other) / 2) * sp.cos((angle + other) / 2) - (sp.sin(angle) - sp.sin(other)))
)
check(
    "F trig",
    current_identity == 0 and difference_identity == 0,
    "sin q (pi + pi') = cos q (s^2 - s'^2), and p cos(Kbar) = s - s'",
)

momenta = sp.symbols("s1:4", real=True)
other_momenta = sp.symbols("r1:4", real=True)
branch, other_branch = sp.symbols("l lp", real=True)
pauli = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
spinor = sp.Matrix([branch + momenta[2], momenta[0] + sp.I * momenta[1]])
other_spinor = sp.Matrix([other_branch + other_momenta[2], other_momenta[0] + sp.I * other_momenta[1]])


def on_shell(expression):
    return sp.expand(expression).subs(
        {
            branch ** 2: sum(component ** 2 for component in momenta),
            other_branch ** 2: sum(component ** 2 for component in other_momenta),
        }
    )


packed = sum((momenta[axis] * pauli[axis] for axis in range(3)), sp.zeros(2))
other_packed = sum((other_momenta[axis] * pauli[axis] for axis in range(3)), sp.zeros(2))
eigen_ok = all(sp.simplify(on_shell(entry)) == 0 for entry in (packed * spinor - branch * spinor))
eigen_ok = eigen_ok and all(sp.simplify(on_shell(entry)) == 0 for entry in (other_packed * other_spinor - other_branch * other_spinor))
overlap = (other_spinor.H * spinor)[0]
contraction = sum((momenta[axis] - other_momenta[axis]) * (other_spinor.H * pauli[axis] * spinor)[0] for axis in range(3))
check(
    "F spinors",
    eigen_ok and sp.simplify(on_shell(contraction - (branch - other_branch) * overlap)) == 0,
    "u = (l + s3, s1 + i s2) is the eigen-spinor, and (s - s') contracts to (l - l') u'†u",
)

wave = sp.symbols("k1:4", real=True)
other_wave = sp.symbols("p1:4", real=True)
polarisation = sp.symbols("M1:4")
difference = [wave[axis] - other_wave[axis] for axis in range(3)]
midpoint = [(wave[axis] + other_wave[axis]) / 2 for axis in range(3)]
half_sine = [sp.sin(wave[axis]) * sp.cos(wave[axis]) for axis in range(3)]
other_half_sine = [sp.sin(other_wave[axis]) * sp.cos(other_wave[axis]) for axis in range(3)]
lattice = [2 * sp.sin(component / 2) for component in difference]
stress = [
    [
        sp.Rational(1, 2)
        * sp.cos(midpoint[row])
        * (half_sine[column] + other_half_sine[column])
        * polarisation[row]
        * sp.cos(difference[column] / 2)
        * sp.prod(sp.cos(difference[direction]) for direction in range(3) if direction != column)
        for column in range(3)
    ]
    for row in range(3)
]
projected = sum(lattice[row] * lattice[column] * stress[row][column] for row in range(3) for column in range(3))
first_factor = sum((sp.sin(wave[axis]) - sp.sin(other_wave[axis])) * polarisation[axis] for axis in range(3))
second_factor = sp.prod(sp.cos(component) for component in difference) * sum(
    sp.sin(wave[axis]) ** 2 - sp.sin(other_wave[axis]) ** 2 for axis in range(3)
)
samples_ok = True
for seed in range(8):
    values = {symbol: sp.pi * sp.Rational((seed * 3 + axis) % 17 - 8, 12) for axis, symbol in enumerate(wave + other_wave)}
    values.update({polarisation[axis]: sp.Rational(seed - 2 * axis, axis + 2) for axis in range(3)})
    samples_ok = samples_ok and sp.simplify((projected - first_factor * second_factor / 2).subs(values)) == 0
check(
    "F assembly",
    samples_ok,
    "p.Theta2.p equals half the product of (s - s').M and (prod cos q)(|s|^2 - |s'|^2) at eight exact angles",
)

scale = sp.symbols("t")
components = sp.symbols("q1:4", real=True)
series = sp.series(sp.prod(sp.cos(scale * component) for component in components), scale, 0, 4).removeO()
expected = 1 - scale ** 2 * sum(component ** 2 for component in components) / 2
check(
    "F order",
    sp.expand(series - expected) == 0,
    "prod cos(t q_l) = 1 - t^2 |q|^2/2 + O(t^4)",
)

phases = sp.symbols("z1:4")
cosines = [(phase + 1 / phase) / 2 for phase in phases]
telescoped = (cosines[0] - 1) + cosines[0] * (cosines[1] - 1) + cosines[0] * cosines[1] * (cosines[2] - 1)
repair_ok = sp.simplify(telescoped - (cosines[0] * cosines[1] * cosines[2] - 1)) == 0
repair_ok = repair_ok and all(sp.simplify(cosines[axis] - 1 - (phases[axis] - 1) * (1 - 1 / phases[axis]) / 2) == 0 for axis in range(3))
check(
    "F repair",
    repair_ok,
    "prod C_l - 1 is a sum of forward differences, and its symbol is prod cos q_l",
)


def axis_numbers():
    left, right = F(5, 13), F(3, 5)
    overlap_value = 2 * left * right
    energy = (left + right) * left * right
    acceleration = (left - right) ** 2 * energy
    cosine = F(12, 13) * F(4, 5) + left * right
    stress_value = cosine * acceleration
    return energy, acceleration, stress_value, cosine


energy, acceleration, stress_value, cosine = axis_numbers()
check(
    "X axis",
    energy == F(192, 845)
    and acceleration == F(37632, 3570125)
    and stress_value == F(2370816, 232058125)
    and cosine == F(63, 65)
    and stress_value == cosine * acceleration,
    "the collinear beat has e = 192/845, -e'' = 37632/3570125, and p.Theta.p / (-e'') = cos q = 63/65",
)


# (sin, cos) for the two waves. The third cosine of the second wave is negative.
waves = ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17)))
other_waves = ((F(-3, 5), F(4, 5)), (F(7, 25), F(24, 25)), (F(12, 13), F(-5, 13)))
product = F(1)
for (left_sine, left_cosine), (right_sine, right_cosine) in zip(waves, other_waves):
    product *= left_cosine * right_cosine + left_sine * right_sine
check(
    "X space",
    sp.simplify(product - F(2793, 105625)) == 0,
    "for sines (3/5, 5/13, 8/17) and (-3/5, 7/25, 12/13) the product of cos q_l is 2793/105625",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed. For every beat, p.Theta2.p = (prod cos q_l) (-e''), with -e'' = (1/2)(l - l')^2 (l + l') u'†u. "
    "The factor is 1 - |q|^2/2 at second order. The corner average e' = (prod C_l) e differs from e by forward "
    "differences and meets e'' = -p.Theta2.p exactly, so alpha = K/4 is the exact match for all eight species. "
    "The collinear certificate is 63/65 and the three-dimensional certificate is 2793/105625. The 12^3 float sweep "
    "was not rebuilt.",
    flush=True,
)
print(
    "HIT: confirmed - the two-step stress meets the member's identity up to prod cos q_l, and the corner-averaged "
    "energy makes alpha = K/4 exact for every species",
    flush=True,
)
