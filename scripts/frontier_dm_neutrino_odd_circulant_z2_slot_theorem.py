#!/usr/bin/env python3
"""
Bounded supplied-matrix Hermitian-circulant / P23 even-odd algebra lemma.

This runner independently checks the finite 3x3 algebra.  It does not define
or test a physical leptogenesis observable.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=140)

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "DM_NEUTRINO_ODD_CIRCULANT_Z2_SLOT_THEOREM_NOTE_2026-04-15.md"

PASS_COUNT = 0
FAIL_COUNT = 0
TOL = 1e-11

I3 = np.eye(3, dtype=complex)
S = np.array(
    [
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0],
    ],
    dtype=complex,
)
S2 = S @ S
P23 = np.array(
    [
        [1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0],
        [0.0, 1.0, 0.0],
    ],
    dtype=complex,
)
BASIS = (I3, S + S2, 1j * (S - S2))


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    condition = bool(condition)
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def exit_code_for(fail_count: int) -> int:
    return 1 if fail_count else 0


def hs_inner(a: np.ndarray, b: np.ndarray) -> complex:
    return np.trace(a.conj().T @ b)


def extract_coefficients(
    k: np.ndarray, basis: tuple[np.ndarray, np.ndarray, np.ndarray] = BASIS
) -> np.ndarray:
    gram = np.array(
        [[hs_inner(left, right) for right in basis] for left in basis],
        dtype=complex,
    )
    rhs = np.array([hs_inner(b, k) for b in basis], dtype=complex)
    coeffs = np.linalg.solve(gram, rhs)
    return np.real_if_close(coeffs, tol=1000).astype(float)


def reconstruct(
    coeffs: np.ndarray,
    basis: tuple[np.ndarray, np.ndarray, np.ndarray] = BASIS,
) -> np.ndarray:
    return sum((float(c) * b for c, b in zip(coeffs, basis)), np.zeros((3, 3), dtype=complex))


def raw_hermitian_circulant(d: float, z: complex) -> np.ndarray:
    """Construct from the independent first-row convention [d, z, conjugate(z)]."""
    return np.array(
        [
            [d, z, np.conjugate(z)],
            [np.conjugate(z), d, z],
            [z, np.conjugate(z), d],
        ],
        dtype=complex,
    )


def hermitian_from_coords(x: np.ndarray) -> np.ndarray:
    """Nine-real-coordinate parametrization of every 3x3 Hermitian matrix."""
    return np.array(
        [
            [x[0], x[3] + 1j * x[4], x[5] + 1j * x[6]],
            [x[3] - 1j * x[4], x[1], x[7] + 1j * x[8]],
            [x[5] - 1j * x[6], x[7] - 1j * x[8], x[2]],
        ],
        dtype=complex,
    )


def hermitian_coords(h: np.ndarray) -> np.ndarray:
    return np.array(
        [
            h[0, 0].real,
            h[1, 1].real,
            h[2, 2].real,
            h[0, 1].real,
            h[0, 1].imag,
            h[0, 2].real,
            h[0, 2].imag,
            h[1, 2].real,
            h[1, 2].imag,
        ],
        dtype=float,
    )


def real_imag_vector(a: np.ndarray) -> np.ndarray:
    flat = a.reshape(-1)
    return np.concatenate((flat.real, flat.imag))


def commutant_constraint_matrix() -> np.ndarray:
    columns = []
    for j in range(9):
        coordinate = np.zeros(9, dtype=float)
        coordinate[j] = 1.0
        h = hermitian_from_coords(coordinate)
        columns.append(real_imag_vector(h @ S - S @ h))
    return np.column_stack(columns)


def subspace_projector(columns: np.ndarray) -> np.ndarray:
    q, _ = np.linalg.qr(columns)
    return q @ q.T


def fixed_unitary() -> np.ndarray:
    seed = np.array(
        [
            [1.0 + 0.2j, 0.3 - 0.1j, -0.4 + 0.5j],
            [0.2 + 0.7j, 1.3 + 0.0j, 0.6 - 0.2j],
            [-0.5 + 0.1j, 0.4 + 0.8j, 0.9 - 0.3j],
        ],
        dtype=complex,
    )
    q, r = np.linalg.qr(seed)
    phases = np.diag(r)
    phase_fix = np.ones(3, dtype=complex)
    nonzero = np.abs(phases) > 0.0
    phase_fix[nonzero] = np.conjugate(phases[nonzero]) / np.abs(phases[nonzero])
    return q @ np.diag(phase_fix)


def part1_full_hermitian_circulant_parametrization() -> None:
    print("\n" + "=" * 92)
    print("PART 1: FULL HERMITIAN COMMUTANT PARAMETRIZATION")
    print("=" * 92)

    constraint = commutant_constraint_matrix()
    _, singular_values, vh = np.linalg.svd(constraint)
    rank = int(np.sum(singular_values > TOL))
    null_basis = vh[rank:].T
    candidate_coords = np.column_stack([hermitian_coords(b) for b in BASIS])

    null_projector = subspace_projector(null_basis)
    candidate_projector = subspace_projector(candidate_coords)
    candidate_commutators = [np.linalg.norm(b @ S - S @ b) for b in BASIS]
    hermiticity_errors = [np.linalg.norm(b - b.conj().T) for b in BASIS]

    check(
        "The Hermitian commutant of the supplied S has real dimension three",
        null_basis.shape[1] == 3,
        f"constraint rank={rank}, nullity={null_basis.shape[1]}",
    )
    check(
        "I, S+S^2, and i(S-S^2) are independent Hermitian commutant elements",
        np.linalg.matrix_rank(candidate_coords, tol=TOL) == 3
        and max(candidate_commutators) < TOL
        and max(hermiticity_errors) < TOL,
        (
            f"rank={np.linalg.matrix_rank(candidate_coords, tol=TOL)}, "
            f"max commutator={max(candidate_commutators):.2e}, "
            f"max Hermiticity error={max(hermiticity_errors):.2e}"
        ),
    )
    check(
        "Those three matrices span the full Hermitian commutant",
        np.linalg.norm(null_projector - candidate_projector) < TOL,
        f"projector error={np.linalg.norm(null_projector - candidate_projector):.2e}",
    )

    hostile = np.diag([1.0, 2.0, 3.0]).astype(complex)
    check(
        "Hostile Hermitian but noncirculant matrix is rejected by the commutator constraint",
        np.linalg.norm(hostile @ S - S @ hostile) > 1e-3,
        f"hostile commutator norm={np.linalg.norm(hostile @ S - S @ hostile):.6f}",
    )


def part2_unique_p23_parity_split() -> None:
    print("\n" + "=" * 92)
    print("PART 2: UNIQUE P23 PARITY SPLIT")
    print("=" * 92)

    reflected_basis = tuple(P23 @ b @ P23.conj().T for b in BASIS)
    parity_columns = np.column_stack(
        [extract_coefficients(reflected, BASIS) for reflected in reflected_basis]
    )
    parity_eigenvalues = np.linalg.eigvals(parity_columns)
    even_count = int(np.sum(np.isclose(parity_eigenvalues, 1.0, atol=TOL)))
    odd_count = int(np.sum(np.isclose(parity_eigenvalues, -1.0, atol=TOL)))

    check(
        "P23 exchanges S and S^2 in the supplied convention",
        np.linalg.norm(P23 @ S @ P23.conj().T - S2) < TOL
        and np.linalg.norm(P23 @ S2 @ P23.conj().T - S) < TOL,
    )
    check(
        "Parity acts as diag(+1,+1,-1) on the extracted coefficient space",
        np.linalg.norm(parity_columns - np.diag([1.0, 1.0, -1.0])) < TOL,
        f"representation error={np.linalg.norm(parity_columns - np.diag([1.0, 1.0, -1.0])):.2e}",
    )
    check(
        "The P23-odd Hermitian-circulant subspace is uniquely one-dimensional",
        even_count == 2 and odd_count == 1,
        f"even multiplicity={even_count}, odd multiplicity={odd_count}",
    )
    check(
        "Hostile wrong-parity assignment of S+S^2 as odd is rejected",
        np.linalg.norm(P23 @ BASIS[1] @ P23.conj().T + BASIS[1]) > 1e-3,
    )
    check(
        "Hostile wrong-parity assignment of i(S-S^2) as even is rejected",
        np.linalg.norm(P23 @ BASIS[2] @ P23.conj().T - BASIS[2]) > 1e-3,
    )


def part3_exact_coefficient_extraction() -> None:
    print("\n" + "=" * 92)
    print("PART 3: EXACT COEFFICIENT EXTRACTION AND SIGN CONVENTION")
    print("=" * 92)

    samples = [
        (2.5, 1.25, 0.75),
        (-1.0, -2.0, 3.0),
        (0.0, 4.5, -0.5),
        (3.0, 0.0, 2.0),
        (7.0, -1.5, 0.0),
        (0.0, 0.0, 0.0),
    ]
    for index, (d, c_even, c_odd) in enumerate(samples):
        k = raw_hermitian_circulant(d, complex(c_even, c_odd))
        extracted = extract_coefficients(k)
        entry_readout = np.array([k[0, 0].real, k[0, 1].real, k[0, 1].imag])
        check(
            f"Sample {index}: Hilbert-Schmidt extraction recovers signed/zero coefficients",
            np.linalg.norm(extracted - np.array([d, c_even, c_odd])) < TOL
            and np.linalg.norm(extracted - entry_readout) < TOL
            and np.linalg.norm(reconstruct(extracted) - k) < TOL,
            f"expected={(d, c_even, c_odd)}, extracted={tuple(extracted)}",
        )

    sign_probe = raw_hermitian_circulant(0.0, 1.5 - 0.25j)
    check(
        "The supplied zero-based convention has K_01 = c_even + i c_odd",
        abs(sign_probe[0, 1] - (1.5 - 0.25j)) < TOL
        and abs(sign_probe[0, 2] - (1.5 + 0.25j)) < TOL,
        f"K01={sign_probe[0,1]}, K02={sign_probe[0,2]}",
    )


def part4_entrywise_polynomial_identity() -> None:
    print("\n" + "=" * 92)
    print("PART 4: COORDINATE POLYNOMIAL Im[(K_01)^2]")
    print("=" * 92)

    samples = [
        (0.0, 2.0, 3.0),
        (1.0, -2.0, 3.0),
        (-4.0, 2.0, -3.0),
        (5.0, -2.0, -3.0),
        (2.0, 0.0, 5.0),
        (-1.0, 4.0, 0.0),
        (3.0, 0.0, 0.0),
        (0.0, 0.5, -0.25),
    ]
    for index, (d, c_even, c_odd) in enumerate(samples):
        k = raw_hermitian_circulant(d, complex(c_even, c_odd))
        direct = float(np.imag(k[0, 1] * k[0, 1]))
        expected = 2.0 * c_even * c_odd
        check(
            f"Sample {index}: direct entry multiplication gives 2 c_even c_odd",
            abs(direct - expected) < TOL,
            f"(d,even,odd)={(d,c_even,c_odd)}, direct={direct:.6f}, expected={expected:.6f}",
        )

    k = raw_hermitian_circulant(1.0, 1.25 - 0.4j)
    reflected = P23 @ k @ P23.conj().T
    direct = float(np.imag(k[0, 1] * k[0, 1]))
    reflected_direct = float(np.imag(reflected[0, 1] * reflected[0, 1]))
    wrong_sign = -2.0 * 1.25 * (-0.4)
    check(
        "The coordinate polynomial is P23-odd on the supplied family",
        abs(reflected_direct + direct) < TOL,
        f"A(K)={direct:.6f}, A(PKP)={reflected_direct:.6f}",
    )
    check(
        "Hostile overall-sign formula -2 c_even c_odd is rejected",
        abs(direct - wrong_sign) > 0.5,
        f"direct={direct:.6f}, hostile={wrong_sign:.6f}",
    )


def part5_basis_covariance_and_coordinate_limit() -> None:
    print("\n" + "=" * 92)
    print("PART 5: BASIS-COVARIANT COEFFICIENTS, COORDINATE-DEPENDENT ENTRY POLYNOMIAL")
    print("=" * 92)

    u = fixed_unitary()
    k = raw_hermitian_circulant(1.75, -0.8 + 0.35j)
    transformed_basis = tuple(u @ b @ u.conj().T for b in BASIS)
    transformed_k = u @ k @ u.conj().T
    transformed_p23 = u @ P23 @ u.conj().T
    original_coeffs = extract_coefficients(k)
    transformed_coeffs = extract_coefficients(transformed_k, transformed_basis)

    transformed_odd = transformed_basis[2]
    odd_parity_error = np.linalg.norm(
        transformed_p23 @ transformed_odd @ transformed_p23.conj().T
        + transformed_odd
    )
    original_entry_polynomial = float(np.imag(k[0, 1] * k[0, 1]))
    transformed_entry_polynomial = float(
        np.imag(transformed_k[0, 1] * transformed_k[0, 1])
    )

    check(
        "Simultaneous unitary conjugation preserves Hilbert-Schmidt coefficients",
        np.linalg.norm(original_coeffs - transformed_coeffs) < TOL,
        f"coefficient drift={np.linalg.norm(original_coeffs-transformed_coeffs):.2e}",
    )
    check(
        "Simultaneous unitary conjugation preserves the one-dimensional odd parity class",
        odd_parity_error < TOL,
        f"odd parity error={odd_parity_error:.2e}",
    )
    check(
        "Hostile claim that the raw 01-entry polynomial is basis invariant is rejected",
        abs(original_entry_polynomial - transformed_entry_polynomial) > 1e-3,
        (
            f"original A01={original_entry_polynomial:.6f}, "
            f"transformed raw A01={transformed_entry_polynomial:.6f}"
        ),
    )


def part6_source_scope_firewall() -> None:
    print("\n" + "=" * 92)
    print("PART 6: SOURCE-SCOPE FIREWALL")
    print("=" * 92)

    note = NOTE_PATH.read_text(encoding="utf-8")
    required = [
        "**Claim type:** bounded_theorem",
        "Supplied `3 x 3` Hermitian-Circulant / `P_23` Even-Odd Algebra Lemma",
        "coordinate functional",
        "not invariant under an arbitrary basis change",
        "missing_bridge_theorem",
        "**carrier bridge**",
        "**source/activation bridge**",
        "**readout bridge**",
        "**transport bridge**",
        "does not state that any coefficient must be activated",
    ]
    forbidden = [
        "standard leptogenesis CP kernel on this family",
        "must be activated away from zero",
        "exact local slot that carries the CP-supporting deformation",
        "the leptogenesis CP kernel reads",
    ]

    missing = [phrase for phrase in required if phrase not in note]
    leaked = [phrase for phrase in forbidden if phrase in note]
    check(
        "Source declares the bounded supplied-matrix scope and all missing bridges",
        not missing,
        f"missing={missing}",
    )
    check(
        "Source contains no legacy physical-observable or activation wording",
        not leaked,
        f"leaked={leaked}",
    )
    check(
        "Runner does not contain the former definitional cp_tensor helper",
        ("def " + "cp_tensor") not in Path(__file__).read_text(encoding="utf-8"),
    )
    check(
        "Exit policy is truthful: zero failures exits zero and any failure exits nonzero",
        exit_code_for(0) == 0
        and exit_code_for(1) != 0
        and exit_code_for(7) != 0,
    )


def main() -> int:
    print("=" * 92)
    print("SUPPLIED 3x3 HERMITIAN-CIRCULANT / P23 EVEN-ODD ALGEBRA LEMMA")
    print("=" * 92)
    print()
    print("Scope:")
    print("  finite supplied-matrix algebra only")
    print("  no physical carrier, source, observable, or transport identification")

    part1_full_hermitian_circulant_parametrization()
    part2_unique_p23_parity_split()
    part3_exact_coefficient_extraction()
    part4_entrywise_polynomial_identity()
    part5_basis_covariance_and_coordinate_limit()
    part6_source_scope_firewall()

    print("\n" + "=" * 92)
    print("RESULT")
    print("=" * 92)
    print("  Bounded result:")
    print("    - the supplied Hermitian commutant is exactly three-real-dimensional")
    print("    - its P23-odd subspace is uniquely one-dimensional")
    print("    - Hilbert-Schmidt extraction recovers (d, c_even, c_odd)")
    print("    - in the displayed basis Im[(K_01)^2] = 2 c_even c_odd")
    print("    - the entry polynomial is not promoted to a physical observable")
    print()
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return exit_code_for(FAIL_COUNT)


if __name__ == "__main__":
    sys.exit(main())
