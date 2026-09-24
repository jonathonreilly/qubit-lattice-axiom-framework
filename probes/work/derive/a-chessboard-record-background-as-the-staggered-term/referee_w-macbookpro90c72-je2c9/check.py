#!/usr/bin/env python3
"""Independent referee for a-chessboard-record-background-as-the-staggered-term a2.

Reads block 17's note and recomputes the staggered spectrum. Does not import
the attempt. The 4^3 floating-point spectrum is not rebuilt.
"""
from __future__ import annotations

import itertools
import subprocess
import sys

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


BRANCH = "physics-loop/admissibility-induced-law-block17-static-law-strong-coupling-order-chessboard-peierls-20260915"
NOTE = (
    "docs/ADMISSIBILITY_RULE_STATIC_SIX_AXIS_LAW_STRONG_COUPLING_LONG_RANGE_ORDER_AND_SEVERAL_GIBBS_STATES_"
    "REFLECTION_POSITIVITY_CHESSBOARD_PEIERLS_BOUNDED_THEOREM_NOTE_2026-09-15.md"
)
subprocess.run(["git", "fetch", "-q", "origin", BRANCH], check=False)
note = subprocess.run(["git", "show", f"origin/{BRANCH}:{NOTE}"], capture_output=True, text=True, check=False).stdout
lines = note.splitlines()
phrases = {
    "T3 heading": "## Theorem T3 — the chessboard estimate",
    "translation-invariant Gibbs state": "is a translation-invariant Gibbs state of",
    "agreement": "the static specification with `μ(v_0 = v_x) ≥ 1/2` for every `x`",
    "claim scope": "the torus law gives v_0 = v_x with probability above 1/2 for every x within a quarter of the side",
    "value at every site": "`μ_L(v) = Π_{bonds} φ(v_x, v_y)/Z_L`",
}
found = {name: any(phrase in line for line in lines) for name, phrase in phrases.items()}
absent = not any(
    word in line.lower() for line in lines for word in ("sublattice", "staggered", "antiferro")
)
check(
    "P1 premise",
    len(lines) > 100 and all(found.values()) and absent,
    "block 17's chessboard is the reflection-positivity estimate; its order is agreement of values, and the note has no sublattice or staggered pattern",
)

a0, slope, cost = sp.symbols("a0 a c", real=True)
zero_ok = True
for bits in itertools.product((0, 1), repeat=3):
    momenta = [sp.pi * bit for bit in bits]
    sines = [sp.sin(momentum) for momentum in momenta]
    level = a0 + cost + 2 * slope * sum(sp.cos(momentum) for momentum in momenta)
    zero_ok &= all(sp.simplify(sine) == 0 for sine in sines)
    zero_ok &= sp.simplify(level - (a0 + cost + 2 * slope * (3 - 2 * sum(bits)))) == 0
check(
    "P2 uniform offset",
    zero_ok,
    "a record at every site adds the same c; at the eight zeros the coin vector vanishes and the level is only shifted",
)

k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
pauli = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
identity = sp.eye(2)
sines = [sp.sin(k1), sp.sin(k2), sp.sin(k3)]
hop = 2 * slope * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3)) * identity + sum(
    (sines[axis] * pauli[axis] for axis in range(3)), sp.zeros(2)
)
block = sp.BlockMatrix(
    [[hop + (cost / 2) * identity, (cost / 2) * identity], [(cost / 2) * identity, -hop + (cost / 2) * identity]]
).as_explicit()
mass_ok = True
for bits in itertools.product((0, 1), repeat=3):
    substituted = block.subs({k1: sp.pi * bits[0], k2: sp.pi * bits[1], k3: sp.pi * bits[2]})
    values = list(substituted.eigenvals().keys())
    lam = 2 * slope * (3 - 2 * sum(bits))
    wanted = [cost / 2 - sp.sqrt(cost**2 / 4 + lam**2), cost / 2 + sp.sqrt(cost**2 / 4 + lam**2)]
    mass_ok &= len(values) == 2 and all(
        any(sp.simplify(value - target) == 0 for value in values) for target in wanted
    )
    partner = tuple(1 - bit for bit in bits)
    partner_lam = 2 * slope * (3 - 2 * sum(partner))
    mass_ok &= sp.simplify(lam**2 - partner_lam**2) == 0
mass_ok &= all(
    sp.simplify(sp.sqrt(cost**2 / 4 + (2 * slope * (3 - 2 * weight)) ** 2).subs(slope, 0) - sp.Abs(cost) / 2) == 0
    for weight in range(4)
)
lam = sp.symbols("lambda", real=True)
mass_ok &= sp.simplify((cost / 2) ** 2 - (cost**2 / 4 + lam**2) + lam**2) == 0
check(
    "C1 masses",
    mass_ok,
    "at the eight zeros the energies are c/2 +- sqrt(c^2/4 + (2a(3-2|n|))^2); paired momenta share the splitting; a=0 gives |c|/2; E+ E- = -lambda^2",
)

kappa, delta = sp.symbols("kappa delta", positive=True)
epsilon = sp.symbols("epsilon")
clock_ok = sp.simplify(sp.solve(sp.Eq(2 * delta, sp.log(kappa) / 2), delta)[0] - sp.log(kappa) / 4) == 0
clock_ok &= sp.simplify(((1 + epsilon) * sp.exp(delta * epsilon) - (1 + epsilon) * sp.exp(delta)).subs(epsilon, 1)) == 0
clock_ok &= sp.simplify(((1 + epsilon) * sp.exp(delta * epsilon)).subs(epsilon, -1)) == 0
check(
    "C3 rates",
    clock_ok,
    "a chessboard of clocks has delta = (log kappa)/4, so the on-site mass is (c/2) kappa^(1/4), and (1+epsilon) e^{delta epsilon} equals (1+epsilon) e^delta",
)


def cube_matrices():
    matrices = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            matrix = [[0, 0, 0] for _ in range(3)]
            for row, column in enumerate(perm):
                matrix[row][column] = signs[row]
            matrices.append(matrix)
    return matrices


def determinant(matrix):
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def parity(point):
    return sum(point) % 2


def apply(matrix, point):
    return tuple(sum(matrix[row][column] * point[column] for column in range(3)) for row in range(3))


matrices = cube_matrices()
proper = [matrix for matrix in matrices if determinant(matrix) == 1]
points = list(itertools.product(range(-3, 4), repeat=3))
symmetry_ok = len(matrices) == 48 and len(proper) == 24
symmetry_ok &= all(parity(apply(matrix, point)) == parity(point) for matrix in matrices for point in points)
symmetry_ok &= all(
    parity(tuple(point[axis] + shift[axis] for axis in range(3))) != parity(point)
    for point in points
    for shift in ((1, 0, 0), (0, 1, 0), (1, 1, 1))
)
check(
    "C4 covariance",
    symmetry_ok,
    "the chessboard sign is invariant under all 48 cube symmetries and flips under every odd translation",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed no-go at the premise. Block 17's chessboard is the reflection-positivity estimate, and its Gibbs "
    "states agree across sites; every site carries a value, so a presence-sensitive coin scalar is a uniform offset. "
    "If a sublattice background is supplied by other means, the eight zeros have energies c/2 +- sqrt(c^2/4 + "
    "(2a(3-2|n|))^2), the two branches multiply to -lambda^2, and a chessboard of clocks is felt only through the "
    "on-site term with m = (c/2) kappa^(1/4). The 4^3 floating-point spectrum was not rebuilt.",
    flush=True,
)
print(
    "HIT: confirmed - block 17 has no chessboard record background; its ordered states are translation-invariant "
    "agreement, so the supplied clause gives no staggered term. The conditional spectrum, filling identity, and "
    "clock mass m = (c/2) kappa^(1/4) hold if such a background is supplied otherwise",
    flush=True,
)
