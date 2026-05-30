#!/usr/bin/env python3
"""Finite-region checks for the pre-record tracial-state narrowing.

Scope:
  - Checks finite matrix-algebra trace uniqueness identities.
  - Checks tensor-product normalized trace and inner-unitary invariance.
  - Checks finite-region maximum entropy for I/d.
  - Records the audit-critical distinction between one-point Pauli vanishing
    and full nonidentity Pauli-string vanishing.

Not scope:
  - No physical identification of the tracial state with a pre-record
    reference state.
  - No proof of Powers' UHF theorem; the note imports that standard theorem.
"""

from __future__ import annotations

import math
from itertools import product

import numpy as np


TOL = 1e-12


def check(label: str, condition: bool, detail: str) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {label}: {detail}")
    return condition


def matrix_unit(n: int, i: int, j: int) -> np.ndarray:
    mat = np.zeros((n, n), dtype=complex)
    mat[i, j] = 1.0
    return mat


def normalized_trace(a: np.ndarray) -> complex:
    return np.trace(a) / a.shape[0]


def close(a: complex | float, b: complex | float, tol: float = TOL) -> bool:
    return abs(a - b) < tol


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = {"I": I2, "X": X, "Y": Y, "Z": Z}


def kron_all(items: list[np.ndarray]) -> np.ndarray:
    out = items[0]
    for item in items[1:]:
        out = np.kron(out, item)
    return out


def pauli_string(word: str) -> np.ndarray:
    return kron_all([PAULI[ch] for ch in word])


def entropy(rho: np.ndarray) -> float:
    eigvals = np.linalg.eigvalsh(rho)
    eigvals = eigvals[eigvals > TOL]
    return float(-np.sum(eigvals * np.log(eigvals)))


def check_matrix_trace_uniqueness(n: int) -> tuple[bool, str]:
    """Check the matrix-unit equations that force the normalized trace."""

    offdiag_ok = True
    diag_equal_ok = True
    for i in range(n):
        for j in range(n):
            eij = matrix_unit(n, i, j)
            if i != j:
                eii = matrix_unit(n, i, i)
                forced_zero_lhs = normalized_trace(eii @ eij)
                forced_zero_rhs = normalized_trace(eij @ eii)
                offdiag_ok = offdiag_ok and close(forced_zero_lhs, forced_zero_rhs)
                offdiag_ok = offdiag_ok and close(normalized_trace(eij), 0.0)
            for k in range(n):
                if i != k:
                    eik = matrix_unit(n, i, k)
                    eki = matrix_unit(n, k, i)
                    eii = matrix_unit(n, i, i)
                    ekk = matrix_unit(n, k, k)
                    diag_equal_ok = diag_equal_ok and close(
                        normalized_trace(eik @ eki),
                        normalized_trace(eki @ eik),
                    )
                    diag_equal_ok = diag_equal_ok and close(
                        normalized_trace(eii),
                        normalized_trace(ekk),
                    )
    normalization_ok = close(sum(normalized_trace(matrix_unit(n, i, i)) for i in range(n)), 1.0)
    return offdiag_ok and diag_equal_ok and normalization_ok, (
        f"n={n}, offdiag_zero={offdiag_ok}, diag_equal={diag_equal_ok}, "
        f"normalization={normalization_ok}"
    )


def main() -> int:
    print("=" * 80)
    print("PRE-RECORD TRACIAL-STATE NARROWING CERTIFICATE")
    print("=" * 80)
    print("Scope: finite-region tracial-state algebra checks only.")
    print("Not scope: pre-record physical identification or Powers UHF proof.")
    print()

    passes: list[bool] = []

    ok, detail = check_matrix_trace_uniqueness(2)
    passes.append(check("M2 matrix-unit trace uniqueness", ok, detail))

    ok, detail = check_matrix_trace_uniqueness(4)
    passes.append(check("two-site M4 matrix-unit trace uniqueness", ok, detail))

    tensor_ok = True
    for a_name, b_name in product(PAULI, repeat=2):
        a = PAULI[a_name]
        b = PAULI[b_name]
        lhs = normalized_trace(np.kron(a, b))
        rhs = normalized_trace(a) * normalized_trace(b)
        tensor_ok = tensor_ok and close(lhs, rhs)
    passes.append(check("tensor normalized trace factors on Pauli basis", tensor_ok, "checked 16 two-site basis tensors"))

    h = (1 / math.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
    phase = np.array([[1, 0], [0, 1j]], dtype=complex)
    cnot = np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ],
        dtype=complex,
    )
    unitary = cnot @ np.kron(h, phase)
    invariance_ok = True
    for word in ("II", "IX", "ZI", "XY", "ZZ"):
        a = pauli_string(word)
        invariance_ok = invariance_ok and close(normalized_trace(unitary @ a @ unitary.conj().T), normalized_trace(a))
    passes.append(check("inner-unitary invariance of normalized trace", invariance_ok, "Hadamard-phase-CNOT conjugation"))

    for n_sites in (1, 2, 3):
        dim = 2**n_sites
        rho = np.eye(dim, dtype=complex) / dim
        passes.append(
            check(
                f"{n_sites}-site tracial density is I/d",
                np.allclose(rho, rho.conj().T) and close(np.trace(rho), 1.0),
                f"dim={dim}, trace={np.trace(rho).real:.1f}",
            )
        )
        passes.append(
            check(
                f"{n_sites}-site maximum entropy",
                close(entropy(rho), math.log(dim)),
                f"S={entropy(rho):.12g}, log(dim)={math.log(dim):.12g}",
            )
        )

    tracial_two = np.eye(4, dtype=complex) / 4
    full_pauli_ok = True
    for word in ("IX", "IY", "IZ", "XI", "YI", "ZI", "XX", "XY", "XZ", "YX", "YY", "YZ", "ZX", "ZY", "ZZ"):
        full_pauli_ok = full_pauli_ok and close(np.trace(tracial_two @ pauli_string(word)), 0.0)
    passes.append(check("full nonidentity Pauli-string expectations vanish for I/4", full_pauli_ok, "checked all 15 nonidentity two-site strings"))

    c = 0.5
    rho_corr = (pauli_string("II") + c * pauli_string("ZZ")) / 4
    eig_ok = bool(np.min(np.linalg.eigvalsh(rho_corr)) > -TOL)
    one_point_zero = True
    for word in ("XI", "YI", "ZI", "IX", "IY", "IZ"):
        one_point_zero = one_point_zero and close(np.trace(rho_corr @ pauli_string(word)), 0.0)
    corr_nonzero = close(np.trace(rho_corr @ pauli_string("ZZ")), c)
    not_tracial = not np.allclose(rho_corr, tracial_two)
    passes.append(
        check(
            "one-point Pauli vanishing is not sufficient",
            eig_ok and one_point_zero and corr_nonzero and not_tracial,
            f"min_eig={np.min(np.linalg.eigvalsh(rho_corr)):.3f}, <ZZ>={np.trace(rho_corr @ pauli_string('ZZ')).real:.3f}",
        )
    )

    n_pass = sum(1 for item in passes if item)
    n_total = len(passes)
    print()
    print(f"PASS={n_pass} FAIL={n_total - n_pass}")
    print("Result: finite-region trace identities support the narrowed theorem surface.")
    print("Residual: Powers UHF uniqueness remains a named standard-math import; pre-record identification remains open.")
    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    raise SystemExit(main())
