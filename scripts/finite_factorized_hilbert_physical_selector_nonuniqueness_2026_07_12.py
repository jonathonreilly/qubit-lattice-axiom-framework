#!/usr/bin/env python3
"""Exact finite certificate for Hilbert-base underdetermination.

The base object is one four-qubit tensor-factorized Hilbert space.  The runner
constructs incompatible graph, dynamics, and readout expansions of that same
base, verifies their defining invariants, and verifies the positive survivor:
operators on disjoint factors commute.

This is a countermodel certificate, not a numerical search and not a claim
that richer operational axiom systems cannot derive unitary/Born structure.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "FINITE_FACTORIZED_HILBERT_PHYSICAL_SELECTOR_NONUNIQUENESS_NO_GO_NOTE_2026-07-12.md"
)
TOL = 1.0e-11
CHECKS: list[tuple[str, bool]] = []


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)


def check(label: str, condition: bool) -> None:
    """Record a decisive check and fail the process at synthesis if needed."""
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


def two_site(
    first: np.ndarray,
    site_i: int,
    second: np.ndarray,
    site_j: int,
    n_sites: int,
) -> np.ndarray:
    operators = [I2.copy() for _ in range(n_sites)]
    operators[site_i] = first
    operators[site_j] = second
    return kron_all(operators)


def graph_hamiltonian(
    edges: tuple[tuple[int, int], ...], n_sites: int
) -> np.ndarray:
    dimension = 2**n_sites
    hamiltonian = np.zeros((dimension, dimension), dtype=complex)
    for site_i, site_j in edges:
        hamiltonian += two_site(X, site_i, X, site_j, n_sites)
    return hamiltonian


def extract_xx_support(hamiltonian: np.ndarray, n_sites: int) -> set[tuple[int, int]]:
    """Recover the displayed XX support by Hilbert--Schmidt orthogonality."""
    dimension = 2**n_sites
    support: set[tuple[int, int]] = set()
    for site_i in range(n_sites):
        for site_j in range(site_i + 1, n_sites):
            word = two_site(X, site_i, X, site_j, n_sites)
            coefficient = np.trace(word.conj().T @ hamiltonian) / dimension
            if abs(coefficient) > TOL:
                support.add((site_i, site_j))
    return support


def degree_multiset(
    edges: tuple[tuple[int, int], ...], n_sites: int
) -> tuple[int, ...]:
    degrees = [0] * n_sites
    for site_i, site_j in edges:
        degrees[site_i] += 1
        degrees[site_j] += 1
    return tuple(sorted(degrees))


def graph_countermodels(n_sites: int) -> None:
    print("\nGRAPH COUNTERMODELS ON ONE FACTORIZED HILBERT SPACE")
    path_edges = tuple((site, site + 1) for site in range(n_sites - 1))
    complete_edges = tuple(
        (site_i, site_j)
        for site_i in range(n_sites)
        for site_j in range(site_i + 1, n_sites)
    )
    path_hamiltonian = graph_hamiltonian(path_edges, n_sites)
    complete_hamiltonian = graph_hamiltonian(complete_edges, n_sites)

    check(
        "path XX support is recovered exactly",
        extract_xx_support(path_hamiltonian, n_sites) == set(path_edges),
    )
    check(
        "complete XX support is recovered exactly",
        extract_xx_support(complete_hamiltonian, n_sites) == set(complete_edges),
    )
    check(
        "both support witnesses are Hermitian on the same base space",
        np.allclose(path_hamiltonian, path_hamiltonian.conj().T, atol=TOL)
        and np.allclose(complete_hamiltonian, complete_hamiltonian.conj().T, atol=TOL)
        and path_hamiltonian.shape == complete_hamiltonian.shape,
    )
    path_degrees = degree_multiset(path_edges, n_sites)
    complete_degrees = degree_multiset(complete_edges, n_sites)
    print(f"path degree multiset:     {path_degrees}")
    print(f"complete degree multiset: {complete_degrees}")
    check(
        "path and complete graphs are not related by factor relabeling",
        path_degrees != complete_degrees,
    )


def unitary_evolution(rho: np.ndarray, time: float, z_operator: np.ndarray) -> np.ndarray:
    dimension = z_operator.shape[0]
    unitary = np.cos(time) * np.eye(dimension) - 1j * np.sin(time) * z_operator
    return unitary @ rho @ unitary.conj().T


def dephasing(
    rho: np.ndarray, time: float, rate: float, z_operator: np.ndarray
) -> np.ndarray:
    return sum(
        kraus @ rho @ kraus.conj().T
        for kraus in dephasing_kraus(time, rate, z_operator)
    )


def dephasing_kraus(
    time: float, rate: float, z_operator: np.ndarray
) -> list[np.ndarray]:
    if time < 0 or rate <= 0:
        raise ValueError("dephasing semigroup requires time >= 0 and rate > 0")
    decay = np.exp(-2.0 * rate * time)
    weight_identity = (1.0 + decay) / 2.0
    weight_z = (1.0 - decay) / 2.0
    identity = np.eye(z_operator.shape[0], dtype=complex)
    return [np.sqrt(weight_identity) * identity, np.sqrt(weight_z) * z_operator]


def channel_superoperator(kraus_operators: list[np.ndarray]) -> np.ndarray:
    """Column-vectorized superoperator for a Kraus channel."""
    return sum(np.kron(kraus.conj(), kraus) for kraus in kraus_operators)


def choi_from_kraus(kraus_operators: list[np.ndarray]) -> np.ndarray:
    """Choi matrix as a Gram sum of column-vectorized Kraus operators."""
    vectors = [kraus.reshape(-1, order="F") for kraus in kraus_operators]
    return sum(np.outer(vector, vector.conj()) for vector in vectors)


def dynamics_countermodels(n_sites: int) -> None:
    print("\nDYNAMICS COUNTERMODELS ON THE SAME BASE")
    dimension = 2**n_sites
    z_first = onsite(Z, 0, n_sites)
    time = 0.7
    rate = 0.8

    unitary = np.cos(time) * np.eye(dimension) - 1j * np.sin(time) * z_first
    check(
        "the reversible extension is unitary",
        np.allclose(unitary.conj().T @ unitary, np.eye(dimension), atol=TOL),
    )

    plus = np.array([1.0, 1.0], dtype=complex) / np.sqrt(2.0)
    zero = np.array([1.0, 0.0], dtype=complex)
    state = kron_all([plus] + [zero for _ in range(n_sites - 1)])
    rho = np.outer(state, state.conj())
    rho_unitary = unitary_evolution(rho, time, z_first)
    rho_dephased = dephasing(rho, time, rate, z_first)

    purity_unitary = float(np.real(np.trace(rho_unitary @ rho_unitary)))
    purity_dephased = float(np.real(np.trace(rho_dephased @ rho_dephased)))
    print(f"unitary purity:   {purity_unitary:.12f}")
    print(f"dephased purity:  {purity_dephased:.12f}")
    check("unitary dynamics preserves purity", abs(purity_unitary - 1.0) < TOL)
    check("dephasing dynamics is nonunitary", purity_dephased < 1.0 - 1.0e-6)
    kraus = dephasing_kraus(time, rate, z_first)
    kraus_completeness = sum(operator.conj().T @ operator for operator in kraus)
    check(
        "dephasing is trace preserving by Kraus completeness",
        np.allclose(kraus_completeness, np.eye(dimension), atol=TOL),
    )
    choi = choi_from_kraus(kraus)
    check(
        "dephasing is completely positive by Choi positivity",
        float(np.linalg.eigvalsh(choi).min()) >= -TOL,
    )

    time_s = 0.31
    time_t = 0.47
    super_s = channel_superoperator(dephasing_kraus(time_s, rate, z_first))
    super_t = channel_superoperator(dephasing_kraus(time_t, rate, z_first))
    super_direct = channel_superoperator(
        dephasing_kraus(time_s + time_t, rate, z_first)
    )
    check(
        "the nonunitary extension obeys the semigroup law on the full matrix algebra",
        np.allclose(super_t @ super_s, super_direct, atol=TOL),
    )


def context_probabilities(
    amplitudes: tuple[Fraction, ...], power: int
) -> tuple[Fraction, ...]:
    weights = tuple(abs(amplitude) ** power for amplitude in amplitudes)
    normalization = sum(weights)
    if normalization == 0:
        raise ValueError("at least one amplitude must be nonzero")
    return tuple(weight / normalization for weight in weights)


def readout_countermodels() -> None:
    print("\nREADOUT COUNTERMODELS ON ONE STATE AND PVM")
    amplitudes = (Fraction(1), Fraction(2))
    born = context_probabilities(amplitudes, 2)
    quartic = context_probabilities(amplitudes, 4)
    print(f"common projective amplitudes: {amplitudes}")
    print(f"p=2 weights: {born}")
    print(f"p=4 weights: {quartic}")
    check("p=2 context probabilities are normalized", sum(born) == 1)
    check("p=4 context probabilities are normalized", sum(quartic) == 1)
    check("both context probability assignments are nonnegative", min(born + quartic) >= 0)
    check("the same Hilbert amplitudes permit distinct normalized readouts", born != quartic)


def factor_locality_survivor(n_sites: int) -> None:
    print("\nEXACT POSITIVE SURVIVOR")
    x_first = onsite(X, 0, n_sites)
    z_first = onsite(Z, 0, n_sites)
    z_second = onsite(Z, 1, n_sites)
    disjoint_commutator = x_first @ z_second - z_second @ x_first
    same_factor_commutator = x_first @ z_first - z_first @ x_first
    check(
        "operators on disjoint factors commute",
        np.linalg.norm(disjoint_commutator) < TOL,
    )
    check(
        "factorization does not make every operator commute",
        np.linalg.norm(same_factor_commutator) > 1.0,
    )


def selector_independence(n_sites: int) -> None:
    print("\nPAIRWISE-INDEPENDENT SELECTOR WITNESSES")
    dimension = 2**n_sites
    path_edges = tuple((site, site + 1) for site in range(n_sites - 1))
    complete_edges = tuple(
        (site_i, site_j)
        for site_i in range(n_sites)
        for site_j in range(site_i + 1, n_sites)
    )
    graph_models = {"path": path_edges, "complete": complete_edges}

    plus = np.array([1.0, 1.0], dtype=complex) / np.sqrt(2.0)
    zero = np.array([1.0, 0.0], dtype=complex)
    state = kron_all([plus] + [zero for _ in range(n_sites - 1)])
    rho = np.outer(state, state.conj())
    z_first = onsite(Z, 0, n_sites)
    time = 0.41
    rate = 0.73
    readout_models = {
        "p2": context_probabilities((Fraction(1), Fraction(2)), 2),
        "p4": context_probabilities((Fraction(1), Fraction(2)), 4),
    }

    outcome_signatures = set()
    all_valid = True
    for graph_name, dynamics_name, readout_name in product(
        graph_models, ("unitary", "dephasing"), readout_models
    ):
        edges = graph_models[graph_name]
        hamiltonian = graph_hamiltonian(edges, n_sites)
        graph_valid = (
            hamiltonian.shape == (dimension, dimension)
            and extract_xx_support(hamiltonian, n_sites) == set(edges)
        )
        if dynamics_name == "unitary":
            evolved = unitary_evolution(rho, time, z_first)
            dynamics_valid = abs(np.trace(evolved) - 1.0) < TOL
        else:
            evolved = dephasing(rho, time, rate, z_first)
            completeness = sum(
                operator.conj().T @ operator
                for operator in dephasing_kraus(time, rate, z_first)
            )
            dynamics_valid = (
                abs(np.trace(evolved) - 1.0) < TOL
                and np.allclose(completeness, np.eye(dimension), atol=TOL)
            )
        probabilities = readout_models[readout_name]
        readout_valid = sum(probabilities) == 1 and min(probabilities) >= 0
        purity = round(float(np.real(np.trace(evolved @ evolved))), 10)
        signature = (
            degree_multiset(edges, n_sites),
            purity,
            probabilities[0],
        )
        outcome_signatures.add(signature)
        valid = graph_valid and dynamics_valid and readout_valid
        all_valid = all_valid and valid
        print(
            f"  {graph_name} / {dynamics_name} / {readout_name}: "
            f"valid={valid}, degree={signature[0]}, purity={purity}, "
            f"P0={probabilities[0]}"
        )
    check(
        "all 2 x 2 x 2 concrete selector combinations are valid and distinct",
        all_valid and len(outcome_signatures) == 8,
    )


def source_contract() -> None:
    text = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(text.split())
    check("source note declares no_go type", "**Type:** no_go" in text)
    check(
        "source note carries the complete N1-N8 discipline record",
        all(f"### N{index}" in text for index in range(1, 9)),
    )
    check(
        "source note links the current minimal-axiom authority",
        "MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in text,
    )
    check(
        "invalid historical participation-ratio comparison is rejected",
        "different sample spaces" in normalized
        and "No numerical localization claim carries weight" in normalized,
    )


def main() -> None:
    print("FINITE FACTORIZED HILBERT-BASE UNDERDETERMINATION CERTIFICATE")
    print("Exact countermodels; no observed or fitted inputs.")
    n_sites = 4
    print(f"base: {n_sites} qubit factors, total dimension {2**n_sites}")

    graph_countermodels(n_sites)
    dynamics_countermodels(n_sites)
    readout_countermodels()
    factor_locality_survivor(n_sites)
    selector_independence(n_sites)
    source_contract()

    passed = sum(value for _, value in CHECKS)
    total = len(CHECKS)
    print("\nSYNTHESIS")
    print(f"checks: {passed}/{total} PASS")
    print("The same tensor-factorized Hilbert base admits incompatible graph,")
    print("dynamics, and readout expansions. Only factor-algebra locality is")
    print("derived. Richer operational premises remain valid positive routes.")
    if passed != total:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
