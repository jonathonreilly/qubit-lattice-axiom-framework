#!/usr/bin/env python3
"""Exact checks for the finite tensor-factorization support/boundary theorem."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SINGLE_AXIOM_HILBERT_NOTE.md"
TOL = 1.0e-11
CHECKS: list[tuple[str, bool]] = []

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)


def check(label: str, condition: bool) -> None:
    value = bool(condition)
    CHECKS.append((label, value))
    print(f"[{'PASS' if value else 'FAIL'}] {label}")


def kron_all(operators: list[np.ndarray]) -> np.ndarray:
    result = operators[0]
    for operator in operators[1:]:
        result = np.kron(result, operator)
    return result


def onsite(operator: np.ndarray, site: int, n_sites: int) -> np.ndarray:
    operators = [I2.copy() for _ in range(n_sites)]
    operators[site] = operator
    return kron_all(operators)


def two_site(operator: np.ndarray, site_i: int, site_j: int, n_sites: int) -> np.ndarray:
    operators = [I2.copy() for _ in range(n_sites)]
    operators[site_i] = operator
    operators[site_j] = operator
    return kron_all(operators)


def factor_locality(n_sites: int) -> None:
    print("\nTHEOREM 1: FACTOR-ALGEBRA LOCALITY")
    x_first = onsite(X, 0, n_sites)
    z_first = onsite(Z, 0, n_sites)
    z_second = onsite(Z, 1, n_sites)
    check(
        "disjoint-factor operators commute",
        np.linalg.norm(x_first @ z_second - z_second @ x_first) < TOL,
    )
    check(
        "the statement is factor-specific rather than global commutativity",
        np.linalg.norm(x_first @ z_first - z_first @ x_first) > 1.0,
    )


def supplied_graph_recovery(n_sites: int) -> None:
    print("\nTHEOREM 2: SUPPLIED SUPPORT RECOVERY")
    dimension = 2**n_sites
    edges = ((0, 1), (1, 2), (2, 3))
    coefficients = {
        (0, 1): Fraction(1, 2),
        (1, 2): Fraction(-3, 4),
        (2, 3): Fraction(5, 3),
    }
    hamiltonian = np.zeros((dimension, dimension), dtype=complex)
    for edge in edges:
        hamiltonian += float(coefficients[edge]) * two_site(X, *edge, n_sites)

    recovered: dict[tuple[int, int], float] = {}
    for site_i in range(n_sites):
        for site_j in range(site_i + 1, n_sites):
            word = two_site(X, site_i, site_j, n_sites)
            coefficient = float(np.real(np.trace(word.conj().T @ hamiltonian) / dimension))
            if abs(coefficient) > TOL:
                recovered[(site_i, site_j)] = coefficient

    check("supplied graph support is recovered exactly", set(recovered) == set(edges))
    check(
        "Hilbert--Schmidt coefficients equal supplied edge coefficients",
        all(abs(recovered[edge] - float(coefficients[edge])) < TOL for edge in edges),
    )


def conditional_unitarity(n_sites: int) -> None:
    print("\nTHEOREM 3: HERMITIAN GENERATOR IMPLIES UNITARITY")
    dimension = 2**n_sites
    hamiltonian = onsite(Z, 0, n_sites)
    time = 0.73
    unitary = np.cos(time) * np.eye(dimension) - 1j * np.sin(time) * hamiltonian
    check("supplied generator is Hermitian", np.allclose(hamiltonian, hamiltonian.conj().T))
    check(
        "exponential of the supplied Hermitian involution is unitary",
        np.allclose(unitary.conj().T @ unitary, np.eye(dimension), atol=TOL),
    )


def born_i3_exact() -> None:
    print("\nTHEOREM 4: BORN QUADRATIC READOUT GIVES I3 = 0")

    def square(value: Fraction) -> Fraction:
        return value * value

    triples = [
        (Fraction(1, 2), Fraction(2, 3), Fraction(-3, 5)),
        (Fraction(-7, 4), Fraction(5, 6), Fraction(11, 9)),
        (Fraction(0), Fraction(3, 7), Fraction(8, 5)),
    ]
    residuals = []
    for a, b, c in triples:
        residual = (
            square(a + b + c)
            - square(a + b)
            - square(a + c)
            - square(b + c)
            + square(a)
            + square(b)
            + square(c)
        )
        residuals.append(residual)
    print(f"exact rational residuals: {residuals}")
    check("Born inclusion--exclusion residuals vanish exactly", residuals == [0, 0, 0])


def source_contract() -> None:
    print("\nSOURCE CONTRACT")
    text = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(text.split())
    check("source note declares bounded_theorem type", "**Type:** bounded_theorem" in text)
    check(
        "source note names the leaf selector no-go without a positive dependency edge",
        "FINITE_FACTORIZED_HILBERT_PHYSICAL_SELECTOR_NONUNIQUENESS_NO_GO_NOTE_2026-07-12.md" in text,
    )
    check(
        "source note rejects the invalid historical localization comparison",
        "sample spaces and normalizations differ" in normalized
        and "makes no numerical localization claim" in normalized,
    )


def main() -> None:
    print("FINITE TENSOR-FACTORIZATION EXACT SUPPORT/BOUNDARY CERTIFICATE")
    print("No observed values, fits, or hidden selector inputs.")
    n_sites = 4
    factor_locality(n_sites)
    supplied_graph_recovery(n_sites)
    conditional_unitarity(n_sites)
    born_i3_exact()
    source_contract()
    passed = sum(value for _, value in CHECKS)
    total = len(CHECKS)
    print("\nSYNTHESIS")
    print(f"checks: {passed}/{total} PASS")
    print("Factor locality is intrinsic. Graph support, unitarity, and I3=0")
    print("are exact consequences only after their named inputs are supplied.")
    if passed != total:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
