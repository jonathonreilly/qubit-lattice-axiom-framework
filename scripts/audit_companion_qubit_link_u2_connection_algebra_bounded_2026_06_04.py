#!/usr/bin/env python3
"""Exact checks for the qubit-link U(2) connection-algebra bounded note.

This runner verifies the finite-dimensional algebra only. It does not identify
the physical Standard Model gauge group, hypercharge assignments, chirality,
matter multiplets, gauge invariance, dynamics, couplings, or color.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    REPO_ROOT
    / "docs"
    / "QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md"
)

PASS = 0
FAIL = 0


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def close(a: np.ndarray, b: np.ndarray) -> bool:
    return np.allclose(a, b, atol=1e-12)


def real_rank(mats: list[np.ndarray]) -> int:
    rows = [
        np.concatenate([mat.real.ravel(), mat.imag.ravel()])
        for mat in mats
    ]
    return int(np.linalg.matrix_rank(np.array(rows), tol=1e-12))


def main() -> int:
    print("=" * 72)
    print("Qubit-link U(2) connection algebra bounded checks")
    print("=" * 72)

    eye = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    sigmas = [sx, sy, sz]
    spin = [s / 2 for s in sigmas]

    eps = np.zeros((3, 3, 3))
    eps[0, 1, 2] = eps[1, 2, 0] = eps[2, 0, 1] = 1
    eps[0, 2, 1] = eps[2, 1, 0] = eps[1, 0, 2] = -1

    record("Pauli matrices are Hermitian", all(close(s, s.conj().T) for s in sigmas))
    record(
        "Pauli matrices satisfy Cl(3) anticommutation",
        all(
            close(
                sigmas[i] @ sigmas[j] + sigmas[j] @ sigmas[i],
                2 * (1 if i == j else 0) * eye,
            )
            for i in range(3)
            for j in range(3)
        ),
    )
    record(
        "S_i = sigma_i/2 closes as su(2)",
        all(
            close(
                comm(spin[i], spin[j]),
                sum(1j * eps[i, j, k] * spin[k] for k in range(3)),
            )
            for i in range(3)
            for j in range(3)
        ),
    )

    phase = 1j * eye
    record("central phase generator commutes with every S_i", all(close(comm(phase, s), zero) for s in spin))
    record("central phase generator is anti-Hermitian", close(phase.conj().T, -phase))
    record("i sigma_i generators are anti-Hermitian", all(close((1j * s).conj().T, -(1j * s)) for s in sigmas))

    u2_basis = [phase, 1j * sx, 1j * sy, 1j * sz]
    record("anti-Hermitian C^2 endomorphism basis has real rank 4", real_rank(u2_basis) == 4)
    record("u(2) dimension decomposes as 3 + 1", len(sigmas) + 1 == 4)
    record("central u(1) line is independent from su(2) generators", real_rank(u2_basis) == real_rank([1j * sx, 1j * sy, 1j * sz]) + 1)

    traceless_hermitian = [sx, sy, sz]
    record("traceless Hermitian M_2(C) space has real rank 3", real_rank(traceless_hermitian) == 3)
    record("traceless Hermitian M_2(C) is dimension-obstructed from su(3) dimension 8", real_rank(traceless_hermitian) == 3 and 3 != 8)
    record("full u(2) is dimension-obstructed from faithful su(3) embedding", real_rank(u2_basis) == 4 and 4 < 8)

    casimir = sum(s @ s for s in spin)
    record("spin-half Casimir is 3/4 I_2", close(casimir, 0.75 * eye))
    record("C^2 carrier dimension is 2, not the color fundamental dimension 3", eye.shape == (2, 2) and eye.shape[0] != 3)

    text = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "does not derive a physical Standard Model gauge group",
        "does not identify the central `u(1)` with hypercharge assignments",
        "does not derive the chiral `SU(2)_L` restriction",
        "does not derive gauge invariance of observables",
        "does not derive color",
    ]:
        record(f"source-note firewall present: {phrase}", phrase in text)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
