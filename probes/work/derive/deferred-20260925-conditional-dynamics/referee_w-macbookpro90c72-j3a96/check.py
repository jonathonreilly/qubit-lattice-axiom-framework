#!/usr/bin/env python3
"""Independent referee for deferred-20260925-conditional-dynamics a1.

Two bonded sites, five cancelling records each, and one supplied formation
time. The attempt's script is not imported.
"""
from __future__ import annotations

import sys

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def zero(matrix) -> bool:
    return sp.simplify(matrix) == sp.zeros(*matrix.shape)


pauli = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
polar, azimuth = sp.symbols("theta phi", real=True)
direction = sp.Matrix([sp.sin(polar) * sp.cos(azimuth), sp.sin(polar) * sp.sin(azimuth), sp.cos(polar)])
record = (sp.eye(2) + sum((direction[axis] * pauli[axis] for axis in range(3)), sp.zeros(2))) / 2
field_ok = all(zero(sp.trigsimp(sp.expand(record * pauli[axis] * record - direction[axis] * record))) for axis in range(3))
check("C1 records", field_ok, "P_q sigma_a P_q = q_a P_q for every unit q")

cancelling = [
    sp.Matrix([1, 0, 0]),
    sp.Matrix([sp.Rational(-1, 2), sp.sqrt(3) / 2, 0]),
    sp.Matrix([sp.Rational(-1, 2), -sp.sqrt(3) / 2, 0]),
    sp.Matrix([0, 0, 1]),
    sp.Matrix([0, 0, -1]),
]
check(
    "C2 cancel",
    sum(cancelling, sp.zeros(3, 1)) == sp.zeros(3, 1) and all(sp.simplify(vector.dot(vector) - 1) == 0 for vector in cancelling),
    "three records at 120 degrees plus an antipodal pair sum to zero",
)

coupling, time = sp.symbols("J tau", positive=True)
swap = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
heisenberg = sum((sp.kronecker_product(spin, spin) for spin in pauli), sp.zeros(4))
evolution = sp.exp(sp.I * coupling * time) * (sp.cos(2 * coupling * time) * sp.eye(4) - sp.I * sp.sin(2 * coupling * time) * swap)
check(
    "C3 bond",
    heisenberg == 2 * swap - sp.eye(4)
    and zero(sp.I * sp.diff(evolution, time) - coupling * heisenberg * evolution)
    and evolution.subs(time, 0) == sp.eye(4),
    "sigma.sigma = 2 SWAP - 1, and U solves i dU/dtau = J sigma.sigma U",
)

up = sp.Matrix([1, 0])
right = sp.Matrix([1, 1]) / sp.sqrt(2)
state = evolution * sp.kronecker_product(up, right)
recorded = sp.kronecker_product(sp.eye(2), (sp.eye(2) + pauli[2]) / 2)
conditional = recorded * state
weight = sp.simplify((conditional.H * conditional)[0])
density = sp.simplify(conditional * conditional.H)
reduced = sp.Matrix(2, 2, lambda row, column: sum(density[2 * row + coin, 2 * column + coin] for coin in range(2)))
bloch_z = sp.simplify(sp.expand_complex((reduced * pauli[2]).trace() / reduced.trace()))
angle = 2 * coupling * time
profile = sp.cos(angle) ** 2 / (1 + sp.sin(angle) ** 2)
check(
    "C4 history",
    sp.simplify(weight - (1 + sp.sin(angle) ** 2) / 2) == 0 and sp.simplify(bloch_z - profile) == 0,
    "the +z record has weight (1+sin^2 2J tau)/2 and leaves x with z-component cos^2/(1+sin^2)",
)

later = sp.symbols("t", positive=True)
initial = sp.Matrix(sp.symbols("rx ry rz", real=True))
rotated = sp.Matrix(
    [
        initial[0] * sp.cos(2 * coupling * later) - initial[1] * sp.sin(2 * coupling * later),
        initial[0] * sp.sin(2 * coupling * later) + initial[1] * sp.cos(2 * coupling * later),
        initial[2],
    ]
)
period = sp.pi / coupling
average = sp.Matrix([sp.simplify(sp.integrate(rotated[axis], (later, 0, period)) / period) for axis in range(3)])
check(
    "C5 average",
    average == sp.Matrix([0, 0, initial[2]]),
    "precession about z at frequency 2J averages to (0, 0, r_z)",
)

values = (
    sp.simplify(profile.subs(time, 0)),
    sp.simplify(profile.subs(time, sp.pi / (8 * coupling))),
    sp.simplify(profile.subs(time, sp.pi / (4 * coupling))),
)
check("C6 records", values == (1, sp.Rational(1, 3), 0), "the same final records give lambda = 1, 1/3 and 0")

opposite = sp.kronecker_product(sp.eye(2), (sp.eye(2) - pauli[2]) / 2) * state
opposite_density = sp.simplify(opposite * opposite.H)
opposite_reduced = sp.Matrix(2, 2, lambda row, column: sum(opposite_density[2 * row + coin, 2 * column + coin] for coin in range(2)))
opposite_z = sp.simplify(sp.expand_complex((opposite_reduced * pauli[2]).trace() / opposite_reduced.trace()))
check("C7 other outcome", sp.simplify(opposite_z - 1) == 0, "a -z record leaves x at +z for every tau")

hazard = sp.symbols("f", positive=True)
numerator = sp.integrate(hazard * sp.exp(-hazard * time) * (1 + sp.sin(angle) ** 2) / 2 * profile, (time, 0, sp.oo))
denominator = sp.integrate(hazard * sp.exp(-hazard * time) * (1 + sp.sin(angle) ** 2) / 2, (time, 0, sp.oo))
averaged = sp.simplify(numerator / denominator)
claimed = (8 * coupling ** 2 + hazard ** 2) / (24 * coupling ** 2 + hazard ** 2)
check(
    "C8 clock",
    sp.simplify(averaged - claimed) == 0 and sp.simplify(claimed.subs(hazard, coupling) - claimed.subs(hazard, 2 * coupling)) != 0,
    "a constant formation hazard gives (8J^2+f^2)/(24J^2+f^2), which depends on f/J",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed countermodel. Two bonded sites, each with five cancelling records, start at +z and +x. "
    "If the partner's record forms at time tau with content +z, the isolated site then precesses in the field J z-hat "
    "and its time-averaged odds are (1 + lambda p_z)/2 with lambda = cos^2(2 J tau)/(1 + sin^2(2 J tau)). The same "
    "final records give lambda = 1, 1/3 or 0. A constant formation hazard gives (8 J^2 + f^2)/(24 J^2 + f^2). "
    "The finite autonomous dynamics does not make lambda a function of the records alone.",
    flush=True,
)
print(
    "HIT: confirmed - the same final records give lambda = 1, 1/3 or 0 according to the partner's formation time, "
    "so the isolated-site law is not records-only",
    flush=True,
)
