#!/usr/bin/env python3
"""Separate-factor chiral Dirac mass algebra support.

The runner verifies a narrow finite-dimensional claim:

* the 4x4 Dirac matrices have the standard massive Dirac algebra;
* gamma_5 is a balanced chiral grading, conserved in the massless Hamiltonian
  and flipped by the Dirac mass term; and
* this separate L/R-factor grading is not the 3-dimensional generation grading
  targeted by the narrow Koide hybrid no-go.

It does not build an emergent-time massive field, derive generation identity,
derive a Q=2/3 mechanism, or close any Koide magnitude/phase selector.
"""

from __future__ import annotations

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(ok))
    FAIL += int(not ok)
    return bool(ok)


I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), complex)
s1 = np.array([[0, 1], [1, 0]], complex)
s2 = np.array([[0, -1j], [1j, 0]], complex)
s3 = np.array([[1, 0], [0, -1]], complex)


def block(A: np.ndarray, B: np.ndarray, C: np.ndarray, D: np.ndarray) -> np.ndarray:
    return np.block([[A, B], [C, D]])


def anti(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return A @ B + B @ A


def comm(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return A @ B - B @ A


def main() -> int:
    print("SEPARATE-FACTOR CHIRAL DIRAC MASS ALGEBRA")
    print("=" * 68)

    gamma0 = block(I2, Z2, Z2, -I2)
    gamma_spatial = [block(Z2, s, -s, Z2) for s in (s1, s2, s3)]
    alpha = [gamma0 @ gi for gi in gamma_spatial]
    beta = gamma0
    gamma5 = 1j * gamma0 @ gamma_spatial[0] @ gamma_spatial[1] @ gamma_spatial[2]
    I4 = np.eye(4, dtype=complex)

    check(
        "ALG Dirac-Clifford alpha/beta relations",
        all(np.allclose(anti(alpha[i], alpha[j]), 2 * (i == j) * I4) for i in range(3) for j in range(3))
        and all(np.allclose(anti(alpha[i], beta), 0) for i in range(3))
        and np.allclose(beta @ beta, I4),
        "{alpha_i,alpha_j}=2 delta_ij, {alpha_i,beta}=0, beta^2=I",
    )

    p = np.array([0.7, -1.3, 0.4])
    m = 0.9
    H = sum(p[i] * alpha[i] for i in range(3)) + m * beta
    E = float(np.sqrt(p @ p + m * m))
    eigs = np.sort(np.linalg.eigvalsh(H))
    check(
        "ALG massive Hamiltonian squares to p^2+m^2",
        np.allclose(H @ H, (p @ p + m * m) * I4),
        f"H^2=(p^2+m^2)I with E={E:.4f}",
    )
    check(
        "ALG spectrum has two positive and two negative Dirac branches",
        np.allclose(eigs[:2], -E) and np.allclose(eigs[2:], E),
        f"eigs={np.round(eigs, 4)}; positive branch can be filled after field quantization",
    )

    check(
        "CHI gamma5 is a balanced chiral grading",
        np.allclose(gamma5 @ gamma5, I4) and abs(np.trace(gamma5)) < 1e-12,
        "gamma5^2=I and Tr(gamma5)=0",
    )
    check(
        "CHI gamma5 commutes with massless alpha.p",
        all(np.allclose(comm(gamma5, alpha[i]), 0) for i in range(3)),
        "[gamma5, alpha_i]=0",
    )
    check(
        "CHI mass term flips chirality",
        np.allclose(anti(gamma5, beta), 0),
        "{gamma5,beta}=0",
    )

    PL = (I4 + gamma5) / 2
    PR = (I4 - gamma5) / 2
    check(
        "CHI Dirac mass couples L to R, not L to L",
        np.allclose(PL @ beta @ PL, 0) and not np.allclose(PL @ beta @ PR, 0),
        "P_L beta P_L=0 and P_L beta P_R!=0",
    )

    J3 = np.ones((3, 3))
    gamma_chi = (2.0 / 3.0) * J3 - np.eye(3)
    check(
        "SEP generation grading is a separate 3D involution",
        gamma_chi.shape == (3, 3) and np.allclose(gamma_chi @ gamma_chi, np.eye(3)),
        "Gamma_chi=(2/3)J-I acts on generation R^3",
    )
    check(
        "SEP gamma5 is a separate 4D Dirac/LR operator",
        gamma5.shape == (4, 4),
        "gamma5 acts on the Dirac L/R factor, not on generation R^3",
    )

    factorized = np.kron(np.eye(3), np.diag([1.0, -1.0]))
    hybrid = np.kron(gamma_chi, np.eye(2))
    check(
        "SEP factorized chirality differs from the hybrid generation grading",
        factorized.shape == hybrid.shape
        and np.allclose(factorized @ factorized, np.eye(6))
        and np.allclose(hybrid @ hybrid, np.eye(6))
        and not np.allclose(factorized, hybrid),
        "I_3 x sigma_3 is not Gamma_chi x I_2",
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the separate Dirac L/R factor supplies a standard chiral Dirac mass algebra, "
        "and that grading is distinct from the generation-space Gamma_chi targeted by the narrow "
        "hybrid no-go. This is algebra support only: it does not construct the emergent-time "
        "massive field, derive generation identity, derive Q=2/3, or close Koide selectors."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
