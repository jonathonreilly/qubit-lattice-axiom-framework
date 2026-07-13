#!/usr/bin/env python3
"""Exact countermodel certificate for two conserved-information semantics.

This runner verifies finite witnesses. The analytic proof and claim boundary
are in docs/SINGLE_AXIOM_INFORMATION_TWO_FORMALIZATIONS_NONFORCING_NO_GO_NOTE_2026-07-12.md.
No observational values, fitted selectors, graph models, or dissipative
comparison parameters are proof inputs.
"""

from __future__ import annotations

import sys

import numpy as np


TOL = 2.0e-12

checks: list[tuple[str, bool, str]] = []


def check(check_id: str, condition: bool, detail: str) -> None:
    checks.append((check_id, bool(condition), detail))
    print(f"[{check_id}] {'PASS' if condition else 'FAIL'} — {detail}")


def unitary_from_hermitian(h: np.ndarray, t: float) -> np.ndarray:
    """Compute exp(-itH) from the spectral theorem for Hermitian H."""
    eigenvalues, eigenvectors = np.linalg.eigh(h)
    return (eigenvectors * np.exp(-1j * t * eigenvalues)) @ eigenvectors.conj().T


def additive_conservation_countermodel() -> None:
    print("\nA. Additive conserved flow does not force unitarity")
    t = 0.7
    a = np.exp(-2.0 * t)
    transition = 0.5 * np.array([[1.0 + a, 1.0 - a],
                                 [1.0 - a, 1.0 + a]])
    ones = np.ones(2)
    difference = np.array([1.0, -1.0])

    check("A01", np.min(transition) >= 0.0,
          f"two-state transition is nonnegative (min={np.min(transition):.6g})")
    check("A02", np.max(np.abs(ones @ transition - ones)) < TOL,
          "column sums preserve I(p)=sum_i p_i")
    check("A03", np.linalg.norm(transition @ difference - a * difference) < TOL,
          f"difference mode contracts by exp(-2t)={a:.12f}")
    unitary_error = np.max(np.abs(transition.T @ transition - np.eye(2)))
    check("A04", unitary_error > 1.0e-2,
          f"T(t)^*T(t) differs from identity (max error={unitary_error:.6g})")
    eigenvalue_moduli = np.sort(np.abs(np.linalg.eigvals(transition)))
    check("A05", abs(eigenvalue_moduli[0] - a) < TOL and a < 1.0,
          "subunit eigenvalue modulus rules out unitarity in every positive-definite inner product")


def nonlinear_norm_countermodel() -> None:
    print("\nB. Reversible norm conservation does not force linearity")

    def flow(z: np.ndarray, t: float) -> np.ndarray:
        theta = t * float(np.vdot(z, z).real)
        rotation = np.array([[np.cos(theta), -np.sin(theta)],
                             [np.sin(theta), np.cos(theta)]])
        return rotation @ z

    z = np.array([0.7 + 0.2j, -0.3 + 0.4j])
    s, t = 0.23, 0.37
    norm_error = abs(np.vdot(flow(z, t), flow(z, t)) - np.vdot(z, z))
    group_error = np.linalg.norm(flow(flow(z, s), t) - flow(z, s + t))
    inverse_error = np.linalg.norm(flow(flow(z, t), -t) - z)
    homogeneity_defect = np.linalg.norm(flow(2.0 * np.array([1.0, 0.0]), t)
                                        - 2.0 * flow(np.array([1.0, 0.0]), t))

    transfer = abs(flow(np.array([1.0, 0.0]), t)[1])
    check("B01", norm_error < TOL and transfer > 0.1,
          f"nonlinear rotation preserves norm and transfers components (error={norm_error:.3e})")
    check("B02", group_error < TOL,
          f"F_t composed with F_s equals F_(t+s) (error={group_error:.3e})")
    check("B03", inverse_error < TOL,
          f"F_-t is the inverse of F_t (error={inverse_error:.3e})")
    check("B04", homogeneity_defect > 1.0e-1,
          f"flow violates homogeneity and is not linear (defect={homogeneity_defect:.6g})")


def dense_unitary_countermodel() -> None:
    print("\nC. Unitarity does not force sparse/local support")
    edge_counts = []
    for n in (4, 8, 16):
        h = np.ones((n, n)) - np.eye(n)
        u = unitary_from_hermitian(h, 0.41)
        hermitian_error = np.max(np.abs(h - h.conj().T))
        unitary_error = np.max(np.abs(u.conj().T @ u - np.eye(n)))
        edges = int(np.count_nonzero(np.triu(np.abs(h) > TOL, k=1)))
        edge_counts.append(edges)
        check(f"C{n:02d}", hermitian_error < TOL and unitary_error < TOL
              and edges == n * (n - 1) // 2,
              f"N={n}: unitary error={unitary_error:.3e}, complete edges={edges}")

    ratios = [edges / (n * n) for edges, n in zip(edge_counts, (4, 8, 16))]
    check("C20", edge_counts == [6, 28, 120] and ratios[-1] > 0.4,
          "complete-support family has Theta(N^2), not O(N), edges")


def basis_support_countermodel() -> None:
    print("\nD. Entrywise support is not basis invariant")
    n = 7
    h_path = np.zeros((n, n))
    for i in range(n - 1):
        h_path[i, i + 1] = h_path[i + 1, i] = 1.0

    eigenvalues, eigenvectors = np.linalg.eigh(h_path)
    h_eigenbasis = eigenvectors.conj().T @ h_path @ eigenvectors
    site_edges = int(np.count_nonzero(np.triu(np.abs(h_path) > TOL, k=1)))
    eigenbasis_edges = int(np.count_nonzero(
        np.triu(np.abs(h_eigenbasis) > 2.0e-10, k=1)))
    diagonalization_error = np.max(np.abs(h_eigenbasis - np.diag(eigenvalues)))

    check("D01", site_edges == n - 1,
          f"site-basis support is the {n}-vertex path ({site_edges} edges)")
    check("D02", eigenbasis_edges == 0 and diagonalization_error < 2.0e-10,
          f"same operator has empty off-diagonal support in eigenbasis (error={diagonalization_error:.3e})")


def conditional_reconstruction_certificate() -> None:
    print("\nE. Conditional self-adjoint-generator reconstruction")
    h = np.array([[0.2, 0.7 + 0.3j, 0.0],
                  [0.7 - 0.3j, -0.4, -0.5j],
                  [0.0, 0.5j, 0.9]], dtype=complex)
    a = -1j * h
    u = unitary_from_hermitian(h, 0.29)

    check("E01", np.max(np.abs(h - h.conj().T)) < TOL,
          "H=iA is self-adjoint when A is anti-Hermitian")
    check("E02", np.max(np.abs(a + a.conj().T)) < TOL,
          "differentiated norm-preservation identity gives A*+A=0")
    check("E03", np.max(np.abs(u.conj().T @ u - np.eye(3))) < TOL,
          "exp(-itH) is unitary on the supplied Hilbert surface")
    adjacency = np.abs(h) > TOL
    np.fill_diagonal(adjacency, False)
    check("E04", np.array_equal(adjacency, adjacency.T),
          "self-adjoint support is symmetric in a supplied orthonormal basis")
    check("E05", np.count_nonzero(adjacency) // 2 == 2,
          "support-as-edges extracts a graph only after the basis and definition are supplied")


def main() -> int:
    print("=" * 78)
    print("TWO CONSERVED-INFORMATION SEMANTICS: NON-FORCING CERTIFICATE")
    print("Actual surface: no-go proposal; independent audit required")
    print("=" * 78)

    additive_conservation_countermodel()
    nonlinear_norm_countermodel()
    dense_unitary_countermodel()
    basis_support_countermodel()
    conditional_reconstruction_certificate()
    passed = sum(condition for _, condition, _ in checks)
    failed = len(checks) - passed
    print("\n" + "=" * 78)
    print(f"SUMMARY: PASS={passed} FAIL={failed} TOTAL={len(checks)}")
    print("Claim-state result: exact scoped non-entailment; not a positive graph-unitary derivation")
    print("Conditional positive: Hilbert + linear differentiable norm-preserving group -> self-adjoint H")
    print("Remaining independent inputs: carrier basis, support semantics, locality bound")
    print("=" * 78)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
