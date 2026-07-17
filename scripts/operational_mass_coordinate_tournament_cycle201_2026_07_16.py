#!/usr/bin/env python3
"""Cycle 201: operational mass-coordinate tournament.

Compare two already-live coherent kinetic routes without identifying a record,
an onsite qubit, or a supplied coefficient with physical mass by fiat:

* the exact paired-Weyl Dirac QCA from Cycle 7; and
* the exact finite-block Dirac Hamiltonian from Cycle 7.

The runner checks rest phase/energy, low-momentum curvature, representation
and cubic-frame invariance, decoupled-record redundancy, a record-conditioned
binding control, and continuous parameter freedom.  It does not select a law,
derive a physical mass value, or modify any foundation/audit surface.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path

import numpy as np
import sympy as sp

import cubic_qubit_relativistic_reduction_probe_2026_07_14 as c7


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "OPERATIONAL_MASS_COORDINATE_TOURNAMENT_CYCLE201_NOTE_2026-07-16.md"
)

I2 = np.eye(2, dtype=complex)
I4 = np.eye(4, dtype=complex)
SX = c7.NSX
SY = c7.NSY
SZ = c7.NSZ
PAULI = (SX, SY, SZ)

TX = SX
TZ = SZ
ALPHA = tuple(np.kron(TX, sigma) for sigma in PAULI)
BETA = np.kron(TZ, I2)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def qca_block(momentum: np.ndarray, mass: float) -> np.ndarray:
    normalization = np.sqrt(1.0 - mass * mass)
    weyl = c7.nsplit(np.asarray(momentum, dtype=float), 1.0)
    return np.block(
        [
            [normalization * weyl, 1j * mass * I2],
            [1j * mass * I2, normalization * weyl.conj().T],
        ]
    )


def qca_scalar(momentum: np.ndarray) -> float:
    qx, qy, qz = map(float, momentum)
    return float(
        np.cos(qx) * np.cos(qy) * np.cos(qz)
        - np.sin(qx) * np.sin(qy) * np.sin(qz)
    )


def qca_positive_phase(momentum: np.ndarray, mass: float) -> float:
    normalization = np.sqrt(1.0 - mass * mass)
    return float(np.arccos(np.clip(normalization * qca_scalar(momentum), -1, 1)))


def hamiltonian_block(momentum: np.ndarray, mass: float) -> np.ndarray:
    return sum(
        (np.sin(float(momentum[i])) * ALPHA[i] for i in range(3)),
        np.zeros((4, 4), dtype=complex),
    ) + mass * BETA


def sorted_phases(unitary: np.ndarray) -> np.ndarray:
    return np.sort(np.angle(np.linalg.eigvals(unitary)))


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for order in permutations(range(3)):
        permutation = np.eye(3, dtype=int)[list(order)]
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    unique = {tuple(frame.reshape(-1)): frame for frame in frames}
    return tuple(unique[key] for key in sorted(unique))


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "mass is not identified with a record",
        "rest quasienergy",
        "dispersion mass",
        "spectator record",
        "record-conditioned coupling",
        "mass-to-gravity map remains open",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves the mass-ontology boundary", not missing, missing)


def onsite_and_block_typing() -> None:
    a0, ax, ay, az = sp.symbols("a_0 a_x a_y a_z")
    si = sp.eye(2)
    sx, sy, sz = c7.SX, c7.SY, c7.SZ
    candidate = a0 * si + ax * sx + ay * sy + az * sz
    equations = []
    for sigma in (sx, sy, sz):
        equations.extend(list(candidate * sigma + sigma * candidate))
    matrix, rhs = sp.linear_eq_to_matrix(equations, (a0, ax, ay, az))
    check(
        "one primitive M2 Weyl carrier has no constant Dirac mass matrix",
        matrix.rank() == 4
        and sp.linsolve((matrix, rhs), (a0, ax, ay, az)) == {(0, 0, 0, 0)},
        matrix.rank(),
    )
    check(
        "a finite M4 block has an independent anticommuting mass matrix",
        all(np.linalg.norm(BETA @ alpha + alpha @ BETA) < 1e-12 for alpha in ALPHA)
        and np.linalg.norm(BETA @ BETA - I4) < 1e-12,
    )


def qca_mass_coordinates() -> None:
    m = sp.symbols("m", positive=True)
    t = sp.symbols("t", real=True)
    normalization = sp.sqrt(1 - m**2)
    omega = sp.acos(normalization * sp.cos(t))
    curvature = sp.simplify(sp.diff(omega, t, 2).subs(t, 0))
    rest_phase = sp.asin(m)
    check(
        "QCA rest quasienergy branch is arcsin(m) on 0<m<1",
        sp.simplify(sp.cos(rest_phase) - normalization) == 0
        and sp.simplify(sp.sin(rest_phase) - m) == 0,
        rest_phase,
    )
    check(
        "QCA low-momentum phase curvature is n/m",
        sp.simplify(curvature - normalization / m) == 0,
        curvature,
    )
    dispersion_mass = sp.simplify(1 / curvature)
    check(
        "QCA dispersion mass is m/n = tan(rest phase)",
        sp.simplify(dispersion_mass - m / normalization) == 0,
        dispersion_mass,
    )

    qx, qy, qz = sp.symbols("q_x q_y q_z", real=True)
    scalar = (
        sp.cos(qx) * sp.cos(qy) * sp.cos(qz)
        - sp.sin(qx) * sp.sin(qy) * sp.sin(qz)
    )
    omega_3d = sp.acos(normalization * scalar)
    origin = {qx: 0, qy: 0, qz: 0}
    hessian = sp.Matrix(
        [
            [sp.simplify(sp.diff(omega_3d, a, b).subs(origin)) for b in (qx, qy, qz)]
            for a in (qx, qy, qz)
        ]
    )
    check(
        "QCA full three-dimensional phase Hessian is (n/m) I",
        hessian == (normalization / m) * sp.eye(3),
        hessian,
    )

    momenta = (
        np.array([0.0, 0.0, 0.0]),
        np.array([0.17, -0.23, 0.31]),
        np.array([-0.29, 0.11, 0.07]),
    )
    masses = (0.1, 0.3, 0.6, 0.8)
    for mass in masses:
        for index, momentum in enumerate(momenta):
            block = qca_block(momentum, mass)
            expected = qca_positive_phase(momentum, mass)
            phases = sorted_phases(block)
            check(
                f"QCA m={mass} held-out momentum {index} is unitary",
                np.linalg.norm(block.conj().T @ block - I4) < 2e-12,
            )
            check(
                f"QCA m={mass} held-out momentum {index} has the exact paired phase",
                np.allclose(phases, [-expected, -expected, expected, expected], atol=2e-12),
                phases,
            )

    gaps = []
    for mass in (0.2, 0.1, 0.05, 0.025):
        rest = np.arcsin(mass)
        inertial = mass / np.sqrt(1 - mass * mass)
        gaps.append(abs(inertial - rest) / rest)
    orders = [np.log(gaps[i] / gaps[i + 1]) / np.log(2) for i in range(3)]
    check(
        "QCA rest/dispersion mismatch vanishes quadratically toward the continuum",
        all(1.95 < order < 2.05 for order in orders),
        orders,
    )
    check(
        "standard phase and momentum readings disagree for every tested nonzero mass",
        all(
            mass / np.sqrt(1 - mass * mass) > np.arcsin(mass)
            for mass in masses
        ),
    )


def hamiltonian_mass_coordinates() -> None:
    m = sp.symbols("m", positive=True)
    t = sp.symbols("t", real=True)
    energy = sp.sqrt(sp.sin(t) ** 2 + m**2)
    curvature = sp.simplify(sp.diff(energy, t, 2).subs(t, 0))
    check("Hamiltonian rest energy is m", sp.simplify(energy.subs(t, 0) - m) == 0)
    check("Hamiltonian low-momentum curvature is 1/m", sp.simplify(curvature - 1 / m) == 0)
    check("Hamiltonian dispersion mass equals rest mass", sp.simplify(1 / curvature - m) == 0)

    qx, qy, qz = sp.symbols("q_x q_y q_z", real=True)
    energy_3d = sp.sqrt(sp.sin(qx) ** 2 + sp.sin(qy) ** 2 + sp.sin(qz) ** 2 + m**2)
    origin = {qx: 0, qy: 0, qz: 0}
    hessian = sp.Matrix(
        [
            [sp.simplify(sp.diff(energy_3d, a, b).subs(origin)) for b in (qx, qy, qz)]
            for a in (qx, qy, qz)
        ]
    )
    check(
        "Hamiltonian full three-dimensional energy Hessian is (1/m) I",
        hessian == (1 / m) * sp.eye(3),
        hessian,
    )

    for mass in (0.1, 0.3, 0.6, 0.8):
        for index, momentum in enumerate(
            (np.zeros(3), np.array([0.17, -0.23, 0.31]))
        ):
            hamiltonian = hamiltonian_block(momentum, mass)
            expected = np.sqrt(sum(np.sin(momentum) ** 2) + mass * mass)
            spectrum = np.linalg.eigvalsh(hamiltonian)
            check(
                f"Hamiltonian m={mass} momentum {index} has exact +/-E spectrum",
                np.allclose(spectrum, [-expected, -expected, expected, expected], atol=2e-12),
                spectrum,
            )


def redundancy_and_representation_controls() -> None:
    mass = 0.3
    momentum = np.array([0.17, -0.23, 0.31])
    qca = qca_block(momentum, mass)
    qca_with_record = np.kron(qca, I2)
    phase_counts = np.round(sorted_phases(qca_with_record), 12)
    expected_counts = np.repeat(np.round(sorted_phases(qca), 12), 2)
    check(
        "a decoupled spectator record doubles multiplicity but not QCA phases",
        np.array_equal(phase_counts, np.sort(expected_counts)),
        phase_counts,
    )

    hamiltonian = hamiltonian_block(momentum, mass)
    hamiltonian_with_record = np.kron(hamiltonian, I2)
    check(
        "a decoupled spectator record doubles multiplicity but not Hamiltonian energies",
        np.allclose(
            np.linalg.eigvalsh(hamiltonian_with_record),
            np.sort(np.repeat(np.linalg.eigvalsh(hamiltonian), 2)),
            atol=2e-12,
        ),
    )

    hadamard = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    representation = np.kron(hadamard, I2)
    conjugated_qca = representation @ qca @ representation.conj().T
    conjugated_h = representation @ hamiltonian @ representation.conj().T
    check(
        "block-basis presentation does not change QCA phases",
        np.allclose(sorted_phases(conjugated_qca), sorted_phases(qca), atol=2e-12),
    )
    check(
        "block-basis presentation does not change Hamiltonian energies",
        np.allclose(
            np.linalg.eigvalsh(conjugated_h),
            np.linalg.eigvalsh(hamiltonian),
            atol=2e-12,
        ),
    )

    frames = proper_cubic_frames()
    check("there are exactly 24 proper cubic frames", len(frames) == 24, len(frames))
    hessian_qca = (np.sqrt(1 - mass * mass) / mass) * np.eye(3)
    hessian_h = (1 / mass) * np.eye(3)
    check(
        "QCA dispersion mass tensor is proper-cubic invariant",
        all(np.allclose(frame @ hessian_qca @ frame.T, hessian_qca) for frame in frames),
    )
    check(
        "Hamiltonian dispersion mass tensor is proper-cubic invariant",
        all(np.allclose(frame @ hessian_h @ frame.T, hessian_h) for frame in frames),
    )


def record_conditioned_binding_control() -> None:
    mass = 0.4
    coupling = 0.1
    momentum = np.zeros(3)
    base = hamiltonian_block(momentum, mass)
    conditioned = np.kron(base, I2) + coupling * np.kron(BETA, SZ)
    spectrum = np.linalg.eigvalsh(conditioned)
    expected = np.sort(
        np.array(
            [
                -(mass + coupling),
                -(mass + coupling),
                -(mass - coupling),
                -(mass - coupling),
                mass - coupling,
                mass - coupling,
                mass + coupling,
                mass + coupling,
            ]
        )
    )
    check(
        "record-conditioned coupling changes mass sectors at fixed record count",
        np.allclose(spectrum, expected, atol=2e-12),
        spectrum,
    )
    check(
        "removing the coupling restores spectator redundancy",
        np.allclose(
            np.linalg.eigvalsh(np.kron(base, I2)),
            np.sort(np.repeat(np.linalg.eigvalsh(base), 2)),
            atol=2e-12,
        ),
    )


def parameter_freedom() -> None:
    masses = (0.1, 0.3, 0.6, 0.8)
    momentum = np.array([0.13, -0.19, 0.27])
    check(
        "unitarity, cubic mass isotropy, and redundancy invariance retain multiple masses",
        all(
            np.linalg.norm(
                qca_block(momentum, mass).conj().T @ qca_block(momentum, mass) - I4
            )
            < 2e-12
            for mass in masses
        )
        and len({round(mass / np.sqrt(1 - mass * mass), 10) for mass in masses})
        == len(masses),
        masses,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    onsite_and_block_typing()
    qca_mass_coordinates()
    hamiltonian_mass_coordinates()
    redundancy_and_representation_controls()
    record_conditioned_binding_control()
    parameter_freedom()
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "OPERATIONAL_MASS_COORDINATES_EXACT" if FAIL == 0 else "CYCLE201_OPEN")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
