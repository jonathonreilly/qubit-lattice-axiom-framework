#!/usr/bin/env python3
"""Exact free-additivity checks plus a finite contact comparator.

The exact claims are fixed-total-momentum reduction and free tensor-product
additivity. Contact binding is measured only on the finite grid printed here.
"""

from __future__ import annotations

from itertools import product

import numpy as np
import sympy as sp


PASS_COUNT = 0
FAIL_COUNT = 0


def report(name: str, ok: bool, residual: float, detail: str) -> None:
    global PASS_COUNT, FAIL_COUNT
    PASS_COUNT += int(ok)
    FAIL_COUNT += int(not ok)
    print(f"{name}: {'PASS' if ok else 'FAIL'} residual={residual:.3e} {detail}")


def momentum_grid(length: int) -> np.ndarray:
    return 2.0 * np.pi * np.arange(length, dtype=float) / float(length)


def signed_momentum_value(index: int, length: int) -> float:
    value = index % length
    if value > length // 2:
        value -= length
    return 2.0 * np.pi * value / float(length)


def near_zero_indices(length: int, radius: int) -> list[int]:
    return [(-n) % length for n in range(radius, 0, -1)] + [0] + list(range(1, radius + 1))


def dispersion(mass: float, momentum: np.ndarray | float) -> np.ndarray | float:
    return np.arcsinh(np.sqrt(mass * mass + np.sin(momentum) ** 2))


def inertial_coefficient(mass: float) -> float:
    return float(mass * np.sqrt(1.0 + mass * mass))


def fourier_matrix(length: int) -> np.ndarray:
    positions = np.arange(length, dtype=float)
    momenta = momentum_grid(length)
    return np.exp(1.0j * np.outer(positions, momenta)) / np.sqrt(float(length))


def spectral_matrix(values: np.ndarray) -> np.ndarray:
    transform = fourier_matrix(len(values))
    matrix = (transform * values[np.newaxis, :]) @ transform.conj().T
    return 0.5 * (matrix + matrix.conj().T)


def pblock_hamiltonian(
    length: int,
    mass_a: float,
    mass_b: float,
    coupling: float,
    total_index: int,
) -> np.ndarray:
    q = momentum_grid(length)
    total_momentum = 2.0 * np.pi * (total_index % length) / float(length)
    kinetic = np.asarray(dispersion(mass_a, q) + dispersion(mass_b, total_momentum - q), dtype=float)
    matrix = spectral_matrix(kinetic)
    matrix[0, 0] -= coupling
    return 0.5 * (matrix + matrix.conj().T)


def lowest_pblock_energy(
    length: int,
    mass_a: float,
    mass_b: float,
    coupling: float,
    total_index: int,
) -> float:
    return float(np.linalg.eigvalsh(pblock_hamiltonian(length, mass_a, mass_b, coupling, total_index))[0])


def full_two_particle_hamiltonian(length: int, mass_a: float, mass_b: float, coupling: float) -> np.ndarray:
    q = momentum_grid(length)
    one_a = spectral_matrix(np.asarray(dispersion(mass_a, q), dtype=float))
    one_b = spectral_matrix(np.asarray(dispersion(mass_b, q), dtype=float))
    identity = np.eye(length)
    matrix = np.kron(one_a, identity) + np.kron(identity, one_b)
    diagonal = np.zeros(length * length)
    for x_a, x_b in product(range(length), repeat=2):
        if x_a == x_b:
            diagonal[x_a * length + x_b] = -coupling
    matrix += np.diag(diagonal)
    return 0.5 * (matrix + matrix.conj().T)


def check_momentum_block_reduction() -> None:
    length = 12
    mass_a, mass_b, coupling = 0.5, 0.8, 0.4
    full = np.linalg.eigvalsh(full_two_particle_hamiltonian(length, mass_a, mass_b, coupling))
    blocked = np.concatenate(
        [np.linalg.eigvalsh(pblock_hamiltonian(length, mass_a, mass_b, coupling, index))
         for index in range(length)]
    )
    residual = float(np.max(np.abs(np.sort(full) - np.sort(blocked))))
    report(
        "CHECK-01 MOMENTUM-BLOCK-REDUCTION",
        residual <= 1.0e-11,
        residual,
        f"L={length} dimensions={len(full)}",
    )


def gaussian_packet(length: int, center: float, width: float) -> np.ndarray:
    positions = np.arange(length, dtype=float)
    distance = np.minimum(np.abs(positions - center), length - np.abs(positions - center))
    vector = np.exp(-(distance**2) / (4.0 * width * width)).astype(complex)
    return vector / np.linalg.norm(vector)


def check_free_additivity() -> None:
    length = 24
    mass_a, mass_b = 0.5, 0.8
    q = momentum_grid(length)
    rest_residual = abs(
        float(np.min(dispersion(mass_a, q)) + np.min(dispersion(mass_b, q)))
        - float(np.arcsinh(mass_a) + np.arcsinh(mass_b))
    )

    mass = 0.7
    even_split_residual = 0.0
    for total_index in (0, 2, 4):
        total_momentum = 2.0 * np.pi * total_index / length
        free_values = np.asarray(dispersion(mass, q) + dispersion(mass, total_momentum - q), dtype=float)
        target = 2.0 * float(dispersion(mass, total_momentum / 2.0))
        even_split_residual = max(even_split_residual, abs(float(np.min(free_values)) - target))

    m_sym, p_sym = sp.symbols("m p", positive=True, real=True)
    single = sp.asinh(sp.sqrt(m_sym**2 + sp.sin(p_sym) ** 2))
    composite = 2 * single.subs(p_sym, p_sym / 2)
    curvature = sp.simplify(sp.diff(composite, p_sym, 2).subs(p_sym, 0))
    curvature_target = 1 / (2 * m_sym * sp.sqrt(1 + m_sym**2))
    curvature_ok = sp.simplify(curvature - curvature_target) == 0

    kinetic_a = spectral_matrix(np.asarray(dispersion(mass_a, q), dtype=float))
    kinetic_b = spectral_matrix(np.asarray(dispersion(mass_b, q), dtype=float))
    identity = np.eye(length)
    free_hamiltonian = np.kron(kinetic_a, identity) + np.kron(identity, kinetic_b)
    expectation_residual = 0.0
    for centers in ((4.0, 4.0), (4.0, 16.0)):
        packet_a = gaussian_packet(length, centers[0], 1.5)
        packet_b = gaussian_packet(length, centers[1], 1.5)
        product_state = np.kron(packet_a, packet_b)
        full_expectation = float(np.vdot(product_state, free_hamiltonian @ product_state).real)
        separate = float(np.vdot(packet_a, kinetic_a @ packet_a).real + np.vdot(packet_b, kinetic_b @ packet_b).real)
        expectation_residual = max(expectation_residual, abs(full_expectation - separate))

    residual = max(rest_residual, even_split_residual, expectation_residual, 0.0 if curvature_ok else 1.0)
    report(
        "CHECK-02 FREE-ADDITIVITY",
        residual <= 1.0e-11,
        residual,
        f"rest={rest_residual:.3e} even_split={even_split_residual:.3e} "
        f"product_expectation={expectation_residual:.3e} curvature={curvature}",
    )


def check_finite_contact_comparator() -> None:
    length = 64
    rows: list[str] = []
    minimum_separation = float("inf")
    all_below = True
    for mass in (0.5, 1.0):
        edge = 2.0 * float(np.arcsinh(mass))
        for coupling in (0.2, 0.8):
            measured = lowest_pblock_energy(length, mass, mass, coupling, 0)
            separation = edge - measured
            minimum_separation = min(minimum_separation, separation)
            all_below = all_below and separation > 0.0
            rows.append(f"m={mass:.1f},U={coupling:.1f},E0={measured:.12e},edge={edge:.12e},sep={separation:.3e}")
    report(
        "CHECK-03 FINITE-CONTACT-COMPARATOR",
        all_below,
        max(0.0, -minimum_separation),
        f"L={length} measured_rows=[" + "; ".join(rows) + "]",
    )


def main() -> int:
    print("COMPOSITE FREE ADDITIVITY AND FINITE CONTACT COMPARATOR")
    check_momentum_block_reduction()
    check_free_additivity()
    check_finite_contact_comparator()
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
