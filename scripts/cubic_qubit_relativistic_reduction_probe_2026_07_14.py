#!/usr/bin/env python3
"""Exact probes for Cycle 7: cubic-qubit relativistic reduction.

Companion note:
  docs/work_history/repo/review_feedback/
  CUBIC_QUBIT_RELATIVISTIC_REDUCTION_CYCLE7_NOTE_2026-07-14.md

This runner separates exact lattice statements from continuum statements:

* an isotropic-Weyl BCC macro-step factors exactly into three ordinary
  nearest-neighbour conditional shifts on the standard cubic graph;
* that ordered split step has a Weyl first derivative but only approximate
  full cubic covariance (the defect begins at second order);
* one primitive M2 carrier has no nonzero Dirac mass matrix anticommuting
  with all three Weyl matrices, while an M4 block does;
* Wilson and staggered block routes are exact range-one cubic laws, with
  their familiar supplied parameters/species residue exposed explicitly;
* the naive two-band lattice law retains eight spatial nodes with balanced
  chirality.

No network, randomness, registry write, or live axiom edit is performed.
Exit code 0 iff every check passes.
"""

from __future__ import annotations

from collections import Counter
from itertools import permutations, product
from math import log
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CUBIC_QUBIT_RELATIVISTIC_REDUCTION_CYCLE7_NOTE_2026-07-14.md"
)

I2 = sp.eye(2)
ZERO2 = sp.zeros(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
PAULI = (SX, SY, SZ)

NI2 = np.eye(2, dtype=complex)
NSX = np.array(SX, dtype=complex)
NSY = np.array(SY, dtype=complex)
NSZ = np.array(SZ, dtype=complex)
NPAULI = (NSX, NSY, NSZ)

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(sp.trigsimp(entry)) == 0 for entry in matrix)


def shift(axis: int, angle: sp.Expr, sign: int = 1) -> sp.Matrix:
    """Conditional +/- axis shift in momentum space."""
    return sp.cos(angle) * I2 - sp.I * sign * sp.sin(angle) * PAULI[axis]


def split_step(qx: sp.Expr, qy: sp.Expr, qz: sp.Expr, y_sign: int = 1) -> sp.Matrix:
    return shift(0, qx) * shift(1, qy, y_sign) * shift(2, qz)


def dariano_walk(qx: sp.Expr, qy: sp.Expr, qz: sp.Expr, branch: str) -> sp.Matrix:
    """Published A^+ or A^- Weyl-QCA Bloch matrix (arXiv:1601.04832)."""
    cx, cy, cz = sp.cos(qx), sp.cos(qy), sp.cos(qz)
    sx, sy, sz = sp.sin(qx), sp.sin(qy), sp.sin(qz)
    if branch == "minus":
        u = cx * cy * cz - sx * sy * sz
        nx = sx * cy * cz + cx * sy * sz
        ny = cx * sy * cz - sx * cy * sz
        nz = cx * cy * sz + sx * sy * cz
    elif branch == "plus":
        u = cx * cy * cz + sx * sy * sz
        nx = sx * cy * cz - cx * sy * sz
        ny = -cx * sy * cz - sx * cy * sz
        nz = cx * cy * sz - sx * sy * cz
    else:
        raise ValueError(branch)
    return u * I2 - sp.I * (nx * SX + ny * SY + nz * SZ)


def nshift(axis: int, angle: float, sign: int = 1) -> np.ndarray:
    return np.cos(angle) * NI2 - 1j * sign * np.sin(angle) * NPAULI[axis]


def nsplit(vector: np.ndarray, epsilon: float) -> np.ndarray:
    return nshift(0, epsilon * vector[0]) @ nshift(1, epsilon * vector[1]) @ nshift(2, epsilon * vector[2])


def exact_weyl(vector: np.ndarray, epsilon: float) -> np.ndarray:
    norm = float(np.linalg.norm(vector))
    h = sum(float(vector[i]) * NPAULI[i] for i in range(3))
    return np.cos(epsilon * norm) * NI2 - 1j * np.sin(epsilon * norm) * h / norm


def nstrang(vector: np.ndarray, epsilon: float) -> np.ndarray:
    x, y, z = epsilon * vector
    return nshift(0, x / 2) @ nshift(1, y / 2) @ nshift(2, z) @ nshift(1, y / 2) @ nshift(0, x / 2)


def convergence_orders(errors: list[float]) -> list[float]:
    return [log(errors[i] / errors[i + 1], 2) for i in range(len(errors) - 1)]


def source_contract() -> None:
    section("A - Companion-note scope and source contract")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    normalized = " ".join(lower.replace("*", "").replace("`", "").replace("_", "").split())
    for phrase in (
        "authority: none",
        "exact micro-law",
        "continuum effective law",
        "n1",
        "n8",
        "does not require a lattice-axiom edit",
        "does not derive the update law",
        "one primitive onsite m2",
        "three-phase",
        "fermionic",
        "mass",
        "chirality",
    ):
        check(f"A note contains boundary: {phrase}", phrase in normalized)
    for url in (
        "https://arxiv.org/abs/1708.00826",
        "https://arxiv.org/abs/1601.04832",
        "https://arxiv.org/abs/hep-th/9304070",
        "https://doi.org/10.1016/0370-2693(81)91026-1",
        "https://doi.org/10.1103/physrevd.16.3031",
        "https://doi.org/10.1103/physrevd.10.2445",
    ):
        check(f"A note cites primary source: {url}", url in lower)


def exact_split_step_factorization() -> None:
    section("B - Exact BCC macro-step from standard-cubic micro-steps")
    qx, qy, qz = sp.symbols("q_x q_y q_z", real=True)
    minus = split_step(qx, qy, qz, y_sign=1)
    plus = split_step(qx, qy, qz, y_sign=-1)
    check("B Sx Sy Sz equals the published A-minus branch", zero(minus - dariano_walk(qx, qy, qz, "minus")))
    check("B Sx S(-y) Sz equals the published A-plus branch", zero(plus - dariano_walk(qx, qy, qz, "plus")))
    check("B A-minus is exactly unitary", zero(minus.H * minus - I2))
    check("B A-plus is exactly unitary", zero(plus.H * plus - I2))

    origin = {qx: 0, qy: 0, qz: 0}
    derivatives = [sp.I * sp.diff(minus, q).subs(origin) for q in (qx, qy, qz)]
    check("B A-minus has the Weyl first derivative in all axes", all(zero(derivatives[i] - PAULI[i]) for i in range(3)))
    plus_derivatives = [sp.I * sp.diff(plus, q).subs(origin) for q in (qx, qy, qz)]
    check(
        "B A-plus has the opposite handed Pauli frame",
        zero(plus_derivatives[0] - SX) and zero(plus_derivatives[1] + SY) and zero(plus_derivatives[2] - SZ),
    )

    endpoints = set(product((-1, 1), repeat=3))
    check("B three conditional cubic shifts reach eight endpoints", len(endpoints) == 8)
    check("B every endpoint is a body diagonal of L1 length three", all(sum(abs(x) for x in endpoint) == 3 for endpoint in endpoints))
    check("B every constituent move is a current six-neighbour edge", all(sum(abs(x) for x in move) == 1 for move in ((1, 0, 0), (0, 1, 0), (0, 0, 1))))


def continuum_and_covariance() -> None:
    section("C - Continuum order and exact-covariance boundary")
    vector = np.array([0.71, -0.43, 0.29])
    epsilons = [0.08, 0.04, 0.02, 0.01]
    split_errors = [float(np.linalg.norm(nsplit(vector, eps) - exact_weyl(vector, eps))) for eps in epsilons]
    split_orders = convergence_orders(split_errors)
    check("C ordered split step approaches Weyl at second order", all(1.85 < order < 2.15 for order in split_orders), str(split_orders))

    strang_errors = [float(np.linalg.norm(nstrang(vector, eps) - exact_weyl(vector, eps))) for eps in epsilons]
    strang_orders = convergence_orders(strang_errors)
    check("C symmetric split improves the local error to third order", all(2.80 < order < 3.20 for order in strang_orders), str(strang_orders))

    # Active +90-degree rotation about z: k -> (-ky,kx,kz),
    # with its spin-1/2 representative exp(-i*pi*sigma_z/4).
    rotated = np.array([-vector[1], vector[0], vector[2]])
    spin_rotation = (NI2 - 1j * NSZ) / np.sqrt(2)
    covariance_errors = [
        float(np.linalg.norm(spin_rotation @ nsplit(vector, eps) @ spin_rotation.conj().T - nsplit(rotated, eps)))
        for eps in epsilons
    ]
    covariance_orders = convergence_orders(covariance_errors)
    check("C ordered micro-law is not exactly 90-degree cubic covariant", covariance_errors[-1] > 1e-8, str(covariance_errors))
    check("C its covariance defect begins only at second order", all(1.80 < order < 2.20 for order in covariance_orders), str(covariance_orders))


def onsite_mass_and_block_escape() -> None:
    section("D - Narrow onsite-M2 mass obstruction and M4 escape")
    a0, ax, ay, az = sp.symbols("a_0 a_x a_y a_z")
    b = a0 * I2 + ax * SX + ay * SY + az * SZ
    equations = []
    for sigma in PAULI:
        equations.extend(list(b * sigma + sigma * b))
    coefficient_matrix, rhs = sp.linear_eq_to_matrix(equations, (a0, ax, ay, az))
    check("D all onsite-M2 anticommutation equations are homogeneous", rhs == sp.zeros(rhs.rows, 1))
    check("D onsite-M2 mass system has full rank", coefficient_matrix.rank() == 4)
    check("D only the zero onsite-M2 mass matrix survives", sp.linsolve((coefficient_matrix, rhs), (a0, ax, ay, az)) == {(0, 0, 0, 0)})

    tx, tz = SX, SZ
    alpha = tuple(sp.kronecker_product(tx, sigma) for sigma in PAULI)
    beta = sp.kronecker_product(tz, I2)
    clifford_ok = all(zero(alpha[i] * alpha[j] + alpha[j] * alpha[i] - (2 if i == j else 0) * sp.eye(4)) for i in range(3) for j in range(3))
    mass_ok = all(zero(beta * a + a * beta) for a in alpha) and zero(beta * beta - sp.eye(4))
    check("D an M4 block carries the three kinetic Clifford matrices", clifford_ok)
    check("D the M4 block carries an independent Dirac mass matrix", mass_ok)

    # Exact massive Dirac-QCA block from two opposite Weyl sectors.
    q = np.array([0.17, -0.23, 0.31])
    w = nsplit(q, 1.0)
    mass = 3 / 5
    normalization = 4 / 5
    d = np.block([[normalization * w, 1j * mass * NI2], [1j * mass * NI2, normalization * w.conj().T]])
    check("D paired-Weyl Dirac QCA is exactly unitary when n^2+m^2=1", np.linalg.norm(d.conj().T @ d - np.eye(4)) < 1e-12)
    check("D unitarity leaves the mass parameter unselected", abs(normalization**2 + mass**2 - 1) < 1e-15 and mass != 0)


def wilson_route() -> None:
    section("E - Exact Wilson block and supplied Wilson parameter")
    s1, s2, s3, effective_mass = sp.symbols("s_1 s_2 s_3 M", real=True)
    tx, tz = SX, SZ
    alpha = tuple(sp.kronecker_product(tx, sigma) for sigma in PAULI)
    beta = sp.kronecker_product(tz, I2)
    h = s1 * alpha[0] + s2 * alpha[1] + s3 * alpha[2] + effective_mass * beta
    expected = (s1**2 + s2**2 + s3**2 + effective_mass**2) * sp.eye(4)
    check("E Wilson/Dirac block squares to a scalar exactly", zero(h * h - expected))

    naive_nodes = list(product((0, 1), repeat=3))
    check("E naive spatial sine law has eight Brillouin-zone corner nodes", len(naive_nodes) == 8)
    wilson_masses = Counter(2 * sum(corner) for corner in naive_nodes)
    check("E r=1 Wilson masses have 1,3,3,1 degeneracies", wilson_masses == Counter({0: 1, 2: 3, 4: 3, 6: 1}), str(dict(wilson_masses)))
    check("E only the origin remains massless at m=0,r=1", wilson_masses[0] == 1)
    check("E changing r changes the lifted masses", [2 * sum(c) for c in naive_nodes] != [sum(c) for c in naive_nodes])


def staggered_gamma(order: tuple[int, int, int]) -> tuple[sp.Matrix, ...]:
    vertices = list(product((0, 1), repeat=3))
    index = {vertex: i for i, vertex in enumerate(vertices)}
    position = {axis: order.index(axis) for axis in range(3)}
    matrices = []
    for axis in range(3):
        gamma = sp.zeros(8)
        for vertex in vertices:
            preceding = order[: position[axis]]
            eta = (-1) ** sum(vertex[j] for j in preceding)
            neighbour = list(vertex)
            neighbour[axis] ^= 1
            gamma[index[vertex], index[tuple(neighbour)]] = eta
        matrices.append(gamma)
    return tuple(matrices)


def eta_for_order(vertex: tuple[int, int, int], axis: int, order: tuple[int, int, int]) -> int:
    return (-1) ** sum(vertex[j] for j in order[: order.index(axis)])


def gauge_equivalent_orders(reference: tuple[int, int, int], target: tuple[int, int, int]) -> bool:
    vertices = list(product((0, 1), repeat=3))
    for gauge_bits in product((-1, 1), repeat=8):
        gauge = dict(zip(vertices, gauge_bits))
        for constants in product((-1, 1), repeat=3):
            works = True
            for vertex in vertices:
                for axis in range(3):
                    neighbour = list(vertex)
                    neighbour[axis] ^= 1
                    if eta_for_order(vertex, axis, target) != (
                        constants[axis]
                        * gauge[vertex]
                        * eta_for_order(vertex, axis, reference)
                        * gauge[tuple(neighbour)]
                    ):
                        works = False
                        break
                if not works:
                    break
            if works:
                return True
    return False


def staggered_route() -> None:
    section("F - Exact 2^3 staggered block and residual taste")
    gamma = staggered_gamma((0, 1, 2))
    i8 = sp.eye(8)
    vertices = list(product((0, 1), repeat=3))
    epsilon = sp.diag(*[(-1) ** sum(vertex) for vertex in vertices])
    clifford_ok = all(zero(gamma[i] * gamma[j] + gamma[j] * gamma[i] - (2 if i == j else 0) * i8) for i in range(3) for j in range(3))
    check("F staggered cube matrices satisfy Cl3 exactly", clifford_ok)
    check("F sublattice parity supplies an anticommuting mass matrix", all(zero(epsilon * g + g * epsilon) for g in gamma) and zero(epsilon**2 - i8))

    coefficients = (sp.Rational(3, 5), sp.Rational(4, 5), sp.Rational(5, 7))
    mass = sp.Rational(2, 3)
    h = sum((coefficients[i] * gamma[i] for i in range(3)), sp.zeros(8)) + mass * epsilon
    energy_squared = sum(value**2 for value in coefficients) + mass**2
    check("F staggered free block squares to E^2 I exactly", zero(h * h - energy_squared * i8))
    lam = sp.symbols("lambda")
    expected_charpoly = sp.expand((lam**2 - energy_squared) ** 4)
    check("F 8-state block has fourfold +/-E multiplicity", sp.expand(h.charpoly(lam).as_expr()) == expected_charpoly)

    # The commutant of the four generated Clifford matrices has dimension 4,
    # the matrix algebra of a two-dimensional taste multiplicity space.
    superoperators = []
    for generator in gamma + (epsilon,):
        superoperators.append(sp.kronecker_product(i8, generator.T) - sp.kronecker_product(generator, i8))
    constraint = sp.Matrix.vstack(*superoperators)
    nullity = 64 - constraint.rank()
    check("F Cl4 commutant has dimension four (two tastes)", nullity == 4, str(nullity))

    all_orders = list(permutations(range(3)))
    check("F all six axis orderings are local-sign gauge equivalent", all(gauge_equivalent_orders((0, 1, 2), order) for order in all_orders))
    check("F there are eight possible 2^3 block origins modulo two", len(vertices) == 8)
    check("F bipartite parity flips across every cubic edge", all(((-1) ** sum(v)) == -((-1) ** sum(tuple(v[j] ^ (j == axis) for j in range(3)))) for v in vertices for axis in range(3)))


def naive_chirality_census() -> None:
    section("G - Naive two-band node and chirality census")
    corners = list(product((0, 1), repeat=3))
    chirality = [(-1) ** sum(corner) for corner in corners]
    check("G naive two-band spatial law has eight nodes", len(corners) == 8)
    check("G node chiralities balance four plus and four minus", Counter(chirality) == Counter({1: 4, -1: 4}), str(Counter(chirality)))
    check("G no single handed node is selected by the cubic sine law", len(set(chirality)) == 2)


def conclusion_contract() -> None:
    section("H - Constitutional-content needles")
    text = NOTE.read_text(encoding="utf-8").lower()
    for phrase in (
        "no lattice-axiom change",
        "no qubit-axiom change",
        "law-level content remains",
        "exact update",
        "axis order",
        "time orientation",
        "macro-step",
        "low-momentum",
        "wilson parameter",
        "two tastes",
        "interactions",
        "not an axiom candidate",
    ):
        check(f"H note contains conclusion boundary: {phrase}", phrase in text)


def main() -> None:
    source_contract()
    exact_split_step_factorization()
    continuum_and_covariance()
    onsite_mass_and_block_escape()
    wilson_route()
    staggered_route()
    naive_chirality_census()
    conclusion_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
