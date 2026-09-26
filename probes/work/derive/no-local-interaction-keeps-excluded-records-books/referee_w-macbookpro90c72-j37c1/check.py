#!/usr/bin/env python3
"""Independent referee for no-local-interaction-keeps-excluded-records-books a2.

The algebraic certificates are recomputed on a fresh finite-rank instance.
The attempt's script is not imported. The named theorems I1-I8 are not re-proved.
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


def zero(matrix) -> bool:
    return sp.simplify(matrix) == sp.zeros(*matrix.shape)


I = sp.I
R = sp.Rational

# A fresh rank-2 instance: a double shell at energy 0, g non-constant there.
free = sp.diag(0, 0, 2, R(-3, 2))
momentum = sp.diag(4, -1, 3, R(1, 5))
columns = sp.Matrix([[1, I], [R(1, 2), 2], [-I, R(3, 2)], [1 - I, -1]])
coupling = sp.Matrix([[R(1, 2), 1 + I], [1 - I, R(-2, 3)]])
interaction = columns * coupling * columns.H
perturbed = free + interaction
kept = 3 * sp.eye(4) + 2 * perturbed - perturbed ** 2
remainder = kept - momentum
check(
    "setup",
    zero(perturbed * kept - kept * perturbed) and zero(free * momentum - momentum * free),
    "the test current commutes with the perturbed fiber Hamiltonian, and the free momentum commutes with the free Hamiltonian",
)


def resolvent(operator, energy):
    return (operator - energy * sp.eye(4)).inv()


identity_ok = True
for energy in (R(1, 4) + I / 3, R(-1, 5) + 2 * I):
    free_resolvent = resolvent(free, energy)
    full_resolvent = resolvent(perturbed, energy)
    transition = interaction - interaction * full_resolvent * interaction
    left = momentum * transition - transition * momentum
    right = (free - energy * sp.eye(4)) * (remainder * full_resolvent - full_resolvent * remainder) * (free - energy * sp.eye(4))
    identity_ok = identity_ok and zero(left - right)
height = R(1, 5)
shell_energy = I * height
full_resolvent = resolvent(perturbed, shell_energy)
transition = interaction - interaction * full_resolvent * interaction
shell = sp.diag(1, 1, 0, 0)
shell_left = shell * (momentum * transition - transition * momentum) * shell
shell_right = shell * (I * height * (remainder * full_resolvent * interaction - interaction * full_resolvent * remainder)) * shell
check(
    "C1 resolvent",
    identity_ok and zero(shell_left - shell_right),
    "[g, T(z)] = (h0 - z)[F2, R(z)](h0 - z), and on the shell the sandwich is i eta times the mixed remainder",
)

free_resolvent = resolvent(free, R(1, 4) + I / 3)
full_resolvent = resolvent(perturbed, R(1, 4) + I / 3)
transition = interaction - interaction * full_resolvent * interaction
overlap = columns.H * free_resolvent * columns
pushed = columns * coupling * (sp.eye(2) + overlap * coupling).inv() * columns.H
push_ok = zero(transition - pushed)
push_ok = push_ok and zero((sp.eye(4) + interaction * free_resolvent) * (sp.eye(4) - interaction * full_resolvent) - sp.eye(4))
push_ok = push_ok and sp.simplify((sp.eye(2) + coupling * overlap).det() * (sp.eye(2) - coupling * columns.H * full_resolvent * columns).det() - 1) == 0
check(
    "C2 push-through",
    push_ok,
    "T = A W (1 + Q0 W)^{-1} A*, (1 + F1 R0)(1 - F1 R) = 1, and the two determinants multiply to 1",
)

scale = sp.symbols("c")
width = sp.Matrix([[3, R(1, 4) - I, 0], [R(1, 4) + I, -2, R(1, 3)], [0, R(1, 3), R(3, 5)]])
base = sp.Matrix([[R(2, 3) + I, 1, -I / 2], [R(1, 7), -2 + I, 2], [1, I, R(1, 3)]])
factor = sp.Matrix([[1, 2 * I], [R(1, 3), -1], [1 - I, R(2, 5)]])
gram = factor * factor.H
middle = width * (sp.eye(3) + base * width).inv()
left_det = (sp.eye(3) + width * (base - scale * gram)).det()
right_det = (sp.eye(3) + width * base).det() * (sp.eye(2) - scale * factor.H * middle * factor).det()
check(
    "C3 Sylvester",
    sp.simplify(sp.expand(left_det - right_det)) == 0,
    "det(1 + W(Q - c Gamma)) = det(1 + W Q) det(1 - c B* M B) identically in c",
)

pauli = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
vector_h = sp.symbols("h1:4", real=True)
vector_f = sp.symbols("f1:4", real=True)
spin_h = sum((vector_h[axis] * pauli[axis] for axis in range(3)), sp.zeros(2))
spin_f = sum((vector_f[axis] * pauli[axis] for axis in range(3)), sp.zeros(2))
length_h = sum(component ** 2 for component in vector_h)
dot = sum(vector_h[axis] * vector_f[axis] for axis in range(3))
double = spin_h * spin_f - spin_f * spin_h
double = spin_h * double - double * spin_h
claimed = 4 * sum(((length_h * vector_f[axis] - dot * vector_h[axis]) * pauli[axis] for axis in range(3)), sp.zeros(2))
cross = spin_h * spin_f - spin_f * spin_h
one_body = zero(sp.expand(double - claimed)) and zero(sp.expand(cross.subs({vector_f[i]: vector_h[i] for i in range(3)})))

other_h = sp.symbols("u1:4", real=True)
other_f = sp.symbols("v1:4", real=True)
left_h = sum((vector_h[axis] * pauli[axis] for axis in range(3)), sp.zeros(2))
right_h = sum((other_h[axis] * pauli[axis] for axis in range(3)), sp.zeros(2))
left_f = sum((vector_f[axis] * pauli[axis] for axis in range(3)), sp.zeros(2))
right_f = sum((other_f[axis] * pauli[axis] for axis in range(3)), sp.zeros(2))
pair = sp.kronecker_product(left_h, sp.eye(2)) + sp.kronecker_product(sp.eye(2), right_h)
placement = sp.kronecker_product(left_f, sp.eye(2)) + sp.kronecker_product(sp.eye(2), right_f)


def commutator(left, right):
    return left * right - right * left


split = commutator(pair, commutator(pair, placement))
split = split - sp.kronecker_product(commutator(left_h, commutator(left_h, left_f)), sp.eye(2))
split = split - sp.kronecker_product(sp.eye(2), commutator(right_h, commutator(right_h, right_f)))
check(
    "C4 placement",
    one_body and zero(sp.expand(split)),
    "[h,[h,f]] = 4(|h|^2 f - (h.f)h), so it vanishes exactly when f is parallel to h, and the two-record double commutator splits",
)

points = (
    (R(3, 5), R(4, 5)),
    (R(5, 13), R(12, 13)),
    (R(20, 29), R(21, 29)),
    (R(8, 17), R(15, 17)),
    (R(7, 25), R(24, 25)),
    (R(9, 41), R(40, 41)),
)
witness_ok = True
derivatives = []
for dimension in (2, 3):
    first, second = points[:dimension], points[3 : 3 + dimension]
    added = first[0][0] * second[0][1] + first[0][1] * second[0][0]
    subtracted = first[0][0] * second[0][1] - first[0][1] * second[0][0]
    derivative = -2 * added * subtracted
    energy_first = sum(component[0] ** 2 for component in first)
    energy_second = sum(component[0] ** 2 for component in second)
    sine_first = 2 * first[1][0] * first[1][1]
    sine_second = 2 * second[1][0] * second[1][1]
    witness_ok = witness_ok and derivative != 0 and sine_first ** 2 * energy_second != sine_second ** 2 * energy_first
    derivatives.append(derivative)
wave, relative = sp.symbols("K q", real=True)
symbol = sp.sin(wave) * sp.cos(2 * relative)
witness_ok = witness_ok and sp.expand(sp.trigsimp((sp.sin(2 * (wave / 2 + relative)) + sp.sin(2 * (wave / 2 - relative))) / 2 - symbol)) == 0
check(
    "C5 shell",
    witness_ok,
    f"g = sin K cos 2q, and at the Pythagorean point the shell derivatives are {derivatives[0]} and {derivatives[1]}, with the wedge nonzero",
)


def tilt(slopes):
    sine_square = [value ** 2 / (1 + value ** 2) for value in slopes]
    sine_cosine = [value / (1 + value ** 2) for value in slopes]
    return sum(value ** 2 for value in sine_cosine) / sum(sine_square)


plane = tilt((F(5, 6), F(18, 5)))
space = tilt((F(5, 6), F(18, 5), F(1, 2)))
check(
    "C6 cones",
    plane == F(139761000, 606502321) and space == F(2653455542, 8714332815) and plane < 1 and space < 1,
    f"the cone tilts at tan K0 are {plane} and {space}, both below 1",
)

momentum_line = sp.sin(wave) * sp.cos(2 * relative)
check(
    "C7 line",
    sp.simplify(momentum_line - momentum_line.subs(relative, -relative)) == 0
    and sp.simplify(momentum_line - momentum_line.subs(relative, sp.pi - relative)) == 0,
    "on the line both two-point shells carry one value of g",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed no-go. A kept fiber current forces the one-body placement current to vanish, and the "
    "resolvent identity then makes the on-shell transition zero wherever g varies. The finite-rank determinant "
    "identity makes Delta real on the continuum. At block 143's K0 the cone tilts are 139761000/606502321 and "
    "2653455542/8714332815, both below 1, which is the input for bounded spectral densities. Delta = 1 then "
    "contradicts the removed on-site states. The named theorems I1-I8 are the imports; they are not re-proved. "
    "The argument covers Z^2 and Z^3, and on the line g is constant on each shell.",
    flush=True,
)
print(
    "HIT: confirmed - no finite-range interaction with a local placement keeps the total energy current of two "
    "excluded records on Z^2 or Z^3",
    flush=True,
)
