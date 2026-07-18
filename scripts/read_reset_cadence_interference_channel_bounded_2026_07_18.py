#!/usr/bin/env python3
"""Independent finite checks for the read/reset cadence theorem.

This runner deliberately excludes the Cycle-222 mass construction.  It checks
only the linear-algebra identities and controls stated by the canonical
bounded note.  The historical campaign runner remains the executable surface
for the conditional Cycle-222 application.
"""

from __future__ import annotations

import numpy as np


PASSED = 0
FAILED = 0
TOL = 2.0e-12


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASSED, FAILED
    if condition:
        PASSED += 1
        print(f"PASS {label}")
    else:
        FAILED += 1
        print(f"FAIL {label} :: {detail}")


def haar_unitary(dimension: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    raw = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
        size=(dimension, dimension)
    )
    q, r = np.linalg.qr(raw)
    phases = np.diag(r)
    phases = phases / np.abs(phases)
    return q @ np.diag(np.conjugate(phases))


def kernel(unitary: np.ndarray, ticks: int) -> np.ndarray:
    return np.abs(np.linalg.matrix_power(unitary, ticks)) ** 2


def dephase(matrix: np.ndarray) -> np.ndarray:
    return np.diag(np.diag(matrix))


def channel_defect_column(
    unitary: np.ndarray, first_ticks: int, second_ticks: int, source: int
) -> np.ndarray:
    dimension = unitary.shape[0]
    rho = np.zeros((dimension, dimension), dtype=complex)
    rho[source, source] = 1.0
    u_first = np.linalg.matrix_power(unitary, first_ticks)
    u_second = np.linalg.matrix_power(unitary, second_ticks)
    after_first = u_first @ rho @ u_first.conj().T
    interference = after_first - dephase(after_first)
    after_second = u_second @ interference @ u_second.conj().T
    return np.real(np.diag(dephase(after_second)))


def cross_term_entry(
    unitary: np.ndarray,
    first_ticks: int,
    second_ticks: int,
    target: int,
    source: int,
) -> complex:
    u_first = np.linalg.matrix_power(unitary, first_ticks)
    u_second = np.linalg.matrix_power(unitary, second_ticks)
    total = 0.0j
    dimension = unitary.shape[0]
    for middle in range(dimension):
        for other in range(dimension):
            if middle == other:
                continue
            total += (
                u_second[target, middle]
                * u_first[middle, source]
                * np.conjugate(u_second[target, other] * u_first[other, source])
            )
    return total


def monomial_unitary() -> np.ndarray:
    permutation = np.array([2, 0, 3, 1])
    phases = np.exp(1j * np.array([0.2, -0.7, 1.1, 2.0]))
    unitary = np.zeros((4, 4), dtype=complex)
    for column, row in enumerate(permutation):
        unitary[row, column] = phases[column]
    return unitary


def main() -> int:
    unitary = haar_unitary(5, 20260718)
    first_ticks, second_ticks = 3, 2
    k_first = kernel(unitary, first_ticks)
    k_second = kernel(unitary, second_ticks)
    direct = kernel(unitary, first_ticks + second_ticks)
    reset = k_second @ k_first
    defect = direct - reset

    check(
        "seeded control is unitary",
        np.linalg.norm(unitary.conj().T @ unitary - np.eye(5)) < TOL,
    )
    check(
        "every tested kernel is doubly stochastic",
        all(
            np.max(np.abs(k.sum(axis=0) - 1.0)) < TOL
            and np.max(np.abs(k.sum(axis=1) - 1.0)) < TOL
            for k in (k_first, k_second, direct)
        ),
    )

    channel_columns = np.column_stack(
        [
            channel_defect_column(
                unitary, first_ticks, second_ticks, source
            )
            for source in range(unitary.shape[0])
        ]
    )
    check(
        "channel representation equals K_(m+n)-K_m K_n",
        np.max(np.abs(channel_columns - defect)) < TOL,
        np.max(np.abs(channel_columns - defect)),
    )

    cross_terms = np.empty_like(defect, dtype=complex)
    for target in range(unitary.shape[0]):
        for source in range(unitary.shape[0]):
            cross_terms[target, source] = cross_term_entry(
                unitary, first_ticks, second_ticks, target, source
            )
    check(
        "entrywise defect equals distinct-intermediate-path cross terms",
        np.max(np.abs(cross_terms - defect)) < TOL,
        np.max(np.abs(cross_terms - defect)),
    )
    check(
        "cadence defect has zero row and column sums",
        np.max(np.abs(defect.sum(axis=0))) < TOL
        and np.max(np.abs(defect.sum(axis=1))) < TOL,
    )
    check(
        "interval order is non-vacuous on the seeded control",
        np.linalg.norm(k_second @ k_first - k_first @ k_second) > 1.0e-3,
    )

    monomial = monomial_unitary()
    monomial_closes = True
    for m in range(1, 7):
        for n in range(1, 7):
            monomial_closes &= np.max(
                np.abs(kernel(monomial, m + n) - kernel(monomial, m) @ kernel(monomial, n))
            ) < TOL
    check("monomial unitary closes every tested cadence pair", monomial_closes)

    hadamard = np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex) / np.sqrt(2.0)
    check(
        "finite-order nonmonomial recurrence does not imply kernel semigroup closure",
        np.max(np.abs(kernel(hadamard, 2) - kernel(hadamard, 1) @ kernel(hadamard, 1)))
        > 0.4,
    )

    k_one = kernel(unitary, 1)
    column_norms = np.linalg.norm(k_one, axis=0)
    check(
        "Hadamard determinant bound is strict on the seeded nonmonomial kernel",
        abs(np.linalg.det(k_one)) < np.prod(column_norms) + TOL
        and np.prod(column_norms) < 1.0 - 1.0e-6,
    )

    monomial_kernel = kernel(monomial, 1)
    check(
        "determinant-bound saturation gives one unit entry per column",
        abs(abs(np.linalg.det(monomial_kernel)) - 1.0) < TOL
        and np.all(np.sum(monomial_kernel > 1.0 - TOL, axis=0) == 1)
        and np.all(np.sum(monomial_kernel > 1.0 - TOL, axis=1) == 1),
    )

    print(f"TOTAL PASS={PASSED} FAIL={FAILED}")
    print(
        "BOUNDARY: finite supplied unitaries and a declared rank-one frame; "
        "no instrument, Record, probability law, clock, or mass law is derived"
    )
    return 0 if FAILED == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
