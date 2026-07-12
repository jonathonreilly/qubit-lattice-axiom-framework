#!/usr/bin/env python3
"""Exact reparameterization no-go for the historical CKM mass-basis NNI route.

The displayed map p_ij = g_ij*sqrt(mu_i/mu_j) is a coordinate change for
M_ij = g_ij*sqrt(mu_i*mu_j) only when the converted reconstruction is
M_ij = p_ij*mu_j.  Inserting p_ij back into the geometric reconstruction
instead produces a different matrix.  This runner proves that distinction
without PDG values, fitted coefficients, or observed CKM targets.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "ckm" / "CKM_MASS_BASIS_NNI_NOTE.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"[{status}] {name}{suffix}")


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def symbolic_entry_checks() -> None:
    print("PART 1: exact coefficient/reconstruction algebra")
    mu_i, mu_j = sp.symbols("mu_i mu_j", positive=True)
    g = sp.symbols("g", complex=True)

    geometric_entry = g * sp.sqrt(mu_i * mu_j)
    p = g * sp.sqrt(mu_i / mu_j)
    consistent_entry = p * mu_j
    legacy_entry = p * sp.sqrt(mu_i * mu_j)

    check(
        "consistent converted reconstruction returns the geometric entry",
        is_zero(consistent_entry - geometric_entry),
        "p*mu_j = g*sqrt(mu_i*mu_j)",
    )
    check(
        "legacy mixed reconstruction equals g*mu_i",
        is_zero(legacy_entry - g * mu_i),
        "p*sqrt(mu_i*mu_j) = g*mu_i",
    )
    check(
        "legacy/geometric entry ratio is sqrt(mu_i/mu_j)",
        is_zero(legacy_entry / geometric_entry - sp.sqrt(mu_i / mu_j)),
    )

    mu1, mu3 = sp.symbols("mu1 mu3", positive=True)
    g13 = sp.symbols("g13", complex=True)
    legacy_13 = g13 * mu1
    geometric_13 = g13 * sp.sqrt(mu1 * mu3)
    frobenius_delta = 2 * (
        legacy_13 * sp.conjugate(legacy_13)
        - geometric_13 * sp.conjugate(geometric_13)
    )
    expected_delta = 2 * g13 * sp.conjugate(g13) * mu1 * (mu1 - mu3)
    check(
        "legacy insertion changes the Hermitian Frobenius invariant",
        is_zero(frobenius_delta - expected_delta),
        "delta tr(M^2) = 2*|g13|^2*mu1*(mu1-mu3)",
    )


def symbolic_schur_and_eigenvalue_checks() -> None:
    print("\nPART 2: Schur-chain boundary and eigenvalue-label obstruction")
    mu1, mu2, mu3 = sp.symbols("mu1 mu2 mu3", positive=True)
    g12, g23, g13 = sp.symbols("g12 g23 g13", complex=True)

    p12 = g12 * sp.sqrt(mu1 / mu2)
    p23 = g23 * sp.sqrt(mu2 / mu3)
    p13_schur = g12 * g23 * sp.sqrt(mu1 / mu3)
    check(
        "Schur coefficient chain survives as p13 = p12*p23",
        is_zero(p13_schur - p12 * p23),
    )

    matrix = sp.Matrix(
        [
            [mu1, g12 * sp.sqrt(mu1 * mu2), g13 * sp.sqrt(mu1 * mu3)],
            [sp.conjugate(g12) * sp.sqrt(mu1 * mu2), mu2, g23 * sp.sqrt(mu2 * mu3)],
            [sp.conjugate(g13) * sp.sqrt(mu1 * mu3), sp.conjugate(g23) * sp.sqrt(mu2 * mu3), mu3],
        ]
    )
    trace_square_excess = sp.expand(sp.trace(matrix * matrix) - (mu1**2 + mu2**2 + mu3**2))
    expected_excess = 2 * (
        g12 * sp.conjugate(g12) * mu1 * mu2
        + g13 * sp.conjugate(g13) * mu1 * mu3
        + g23 * sp.conjugate(g23) * mu2 * mu3
    )
    check(
        "diagonal labels cannot also be the eigenvalue multiset for nonzero off-diagonals",
        is_zero(trace_square_excess - expected_excess),
        "tr(M^2)-sum(mu_i^2) is a positive sum",
    )


def exact_matrix(
    mus: tuple[sp.Rational, sp.Rational, sp.Rational],
    coefficients: tuple[sp.Rational, sp.Rational, sp.Rational],
    mode: str,
) -> sp.Matrix:
    mu1, mu2, mu3 = mus
    g12, g23, g13 = coefficients
    matrix = sp.diag(mu1, mu2, mu3)

    entries = []
    for i, j, g in ((0, 1, g12), (1, 2, g23), (0, 2, g13)):
        geometric = g * sp.sqrt(mus[i] * mus[j])
        if mode == "geometric":
            value = geometric
        elif mode == "consistent":
            p = g * sp.sqrt(mus[i] / mus[j])
            value = p * mus[j]
        elif mode == "legacy_13":
            if (i, j) == (0, 2):
                p = g * sp.sqrt(mus[i] / mus[j])
                value = p * sp.sqrt(mus[i] * mus[j])
            else:
                value = geometric
        else:  # pragma: no cover - defensive path
            raise ValueError(mode)
        entries.append((i, j, sp.simplify(value)))

    for i, j, value in entries:
        matrix[i, j] = value
        matrix[j, i] = value
    return matrix


def exact_rational_controls() -> None:
    print("\nPART 3: exact rational matrix controls")
    samples = [
        (
            (sp.Rational(1), sp.Rational(16), sp.Rational(400)),
            (sp.Rational(3, 5), sp.Rational(2, 7), sp.Rational(6, 35)),
        ),
        (
            (sp.Rational(1), sp.Rational(9), sp.Rational(225)),
            (sp.Rational(4, 7), sp.Rational(5, 11), sp.Rational(20, 77)),
        ),
    ]

    for index, (mus, coefficients) in enumerate(samples, start=1):
        geometric = exact_matrix(mus, coefficients, "geometric")
        consistent = exact_matrix(mus, coefficients, "consistent")
        legacy = exact_matrix(mus, coefficients, "legacy_13")

        check(f"sample {index}: consistent matrix equals geometric matrix exactly", consistent == geometric)
        check(f"sample {index}: legacy 1-3 insertion changes the matrix", legacy != geometric)
        check(
            f"sample {index}: consistent characteristic polynomial is unchanged",
            sp.expand(consistent.charpoly().as_expr() - geometric.charpoly().as_expr()) == 0,
        )
        check(
            f"sample {index}: legacy characteristic polynomial changes",
            sp.expand(legacy.charpoly().as_expr() - geometric.charpoly().as_expr()) != 0,
        )
        delta = sp.simplify(sp.trace(legacy * legacy) - sp.trace(geometric * geometric))
        check(f"sample {index}: legacy Frobenius invariant decreases for ordered scales", bool(delta < 0), str(delta))


def diagonalizer(matrix: np.ndarray) -> np.ndarray:
    hermitian_square = matrix @ matrix.T
    _, vectors = np.linalg.eigh(hermitian_square)
    return vectors


def synthetic_two_sector_control() -> None:
    print("\nPART 4: synthetic two-sector CKM control")
    up_mus = (sp.Rational(1), sp.Rational(16), sp.Rational(400))
    down_mus = (sp.Rational(1), sp.Rational(9), sp.Rational(225))
    up_coeffs = (sp.Rational(3, 5), sp.Rational(2, 7), sp.Rational(6, 35))
    down_coeffs = (sp.Rational(4, 7), sp.Rational(5, 11), sp.Rational(20, 77))

    up_geometric = np.array(exact_matrix(up_mus, up_coeffs, "geometric"), dtype=float)
    down_geometric = np.array(exact_matrix(down_mus, down_coeffs, "geometric"), dtype=float)
    up_consistent = np.array(exact_matrix(up_mus, up_coeffs, "consistent"), dtype=float)
    down_consistent = np.array(exact_matrix(down_mus, down_coeffs, "consistent"), dtype=float)
    up_legacy = np.array(exact_matrix(up_mus, up_coeffs, "legacy_13"), dtype=float)
    down_legacy = np.array(exact_matrix(down_mus, down_coeffs, "legacy_13"), dtype=float)

    up_spectrum = np.linalg.eigvalsh(up_geometric @ up_geometric.T)
    down_spectrum = np.linalg.eigvalsh(down_geometric @ down_geometric.T)
    min_gap = min(float(np.min(np.diff(up_spectrum))), float(np.min(np.diff(down_spectrum))))
    check(
        "synthetic CKM control has nondegenerate sector spectra",
        min_gap > 1e-8,
        f"minimum squared-spectrum gap={min_gap:.3e}",
    )

    ckm_geometric = diagonalizer(up_geometric).T @ diagonalizer(down_geometric)
    ckm_consistent = diagonalizer(up_consistent).T @ diagonalizer(down_consistent)
    ckm_legacy = diagonalizer(up_legacy).T @ diagonalizer(down_legacy)

    invariant_residual = float(np.max(np.abs(np.abs(ckm_geometric) - np.abs(ckm_consistent))))
    deformation_shift = float(np.max(np.abs(np.abs(ckm_geometric) - np.abs(ckm_legacy))))
    check(
        "consistent reparameterization leaves all synthetic CKM moduli unchanged",
        invariant_residual < 1e-13,
        f"max modulus residual={invariant_residual:.3e}",
    )
    check(
        "legacy mixed reconstruction changes a generic synthetic CKM matrix",
        deformation_shift > 1e-6,
        f"max modulus shift={deformation_shift:.3e}",
    )


def source_boundary_checks() -> None:
    print("\nPART 5: source-boundary checks")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.split())
    check(
        "note declares the canonical no_go claim type",
        "**Type:** no_go" in note and "**Claim type:** no_go" in note,
    )
    print("[INFO] N1-N8 substance is reviewed independently; this runner does not self-certify it.")
    scope_markers_present = (
        "cannot suppress by the displayed map while representing the same matrix" in normalized
        and "a global no-go against all NNI or other flavor textures" in normalized
        and "a no-go against a dynamically derived mass-suppressed texture" in normalized
    )
    print(
        "[INFO] source scope markers present; independent prose review remains authoritative: "
        f"{scope_markers_present}"
    )
    check(
        "note discloses that the former numerical block used imported and fitted inputs",
        "imported PDG quark masses" in normalized
        and "fitted geometric coefficients" in normalized
        and "imported PDG CKM comparator" in normalized,
    )
    check(
        "note links the primary runner and cache",
        "scripts/frontier_ckm_mass_basis_nni_reparameterization_no_go.py" in note
        and "logs/runner-cache/frontier_ckm_mass_basis_nni_reparameterization_no_go.txt" in note,
    )


def main() -> int:
    print("CKM mass-basis NNI reparameterization boundary")
    print("No PDG masses, CKM comparators, fitted coefficients, or observed targets are used.\n")
    symbolic_entry_checks()
    symbolic_schur_and_eigenvalue_checks()
    exact_rational_controls()
    synthetic_two_sector_control()
    source_boundary_checks()
    print(f"\nTOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
