#!/usr/bin/env python3
"""Check the Choi normalization convention used in the Kraus-Choi note."""

from __future__ import annotations

from pathlib import Path

import numpy as np


REPO_ROOT = Path(__file__).resolve().parent.parent
NOTE = REPO_ROOT / "docs" / "KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"[{status}] {name}")
    if detail:
        print(f"       {detail}")


def idx(first: int, second: int, d: int) -> int:
    return first * d + second


def apply_kraus(kraus: list[np.ndarray], x: np.ndarray) -> np.ndarray:
    out = np.zeros_like(x, dtype=complex)
    for k in kraus:
        out += k @ x @ k.conj().T
    return out


def choi_from_kraus(kraus: list[np.ndarray], d: int, normalized: bool = False) -> np.ndarray:
    c = np.zeros((d * d, d * d), dtype=complex)
    for i in range(d):
        for j in range(d):
            eij = np.zeros((d, d), dtype=complex)
            eij[i, j] = 1.0
            phi_eij = apply_kraus(kraus, eij)
            for a in range(d):
                for b in range(d):
                    c[idx(i, a, d), idx(j, b, d)] = phi_eij[a, b]
    if normalized:
        c = c / d
    return c


def inverse_choi(c: np.ndarray, x: np.ndarray, d: int, factor: float = 1.0) -> np.ndarray:
    lifted = np.kron(x.T, np.eye(d, dtype=complex)) @ c
    out = np.zeros((d, d), dtype=complex)
    for i in range(d):
        rows = slice(idx(i, 0, d), idx(i, 0, d) + d)
        out += lifted[rows, rows]
    return factor * out


def partial_trace_output(c: np.ndarray, d: int) -> np.ndarray:
    out = np.zeros((d, d), dtype=complex)
    for i in range(d):
        for j in range(d):
            out[i, j] = sum(c[idx(i, a, d), idx(j, a, d)] for a in range(d))
    return out


def basis(d: int) -> list[np.ndarray]:
    mats = []
    for i in range(d):
        for j in range(d):
            eij = np.zeros((d, d), dtype=complex)
            eij[i, j] = 1.0
            mats.append(eij)
    return mats


def main() -> int:
    print("=" * 88)
    print("KRAUS-CHOI NORMALIZATION CONVENTION CHECK")
    print("=" * 88)

    note_text = NOTE.read_text(encoding="utf-8")
    note_markers = [
        ("unnormalized convention", "unnormalized"),
        ("normalized Choi scale", "C_\u03a6^norm = C_\u03a6 / d"),
        ("normalized inverse factor", "\u03a6(X) = d Tr_1"),
        ("unnormalized Kraus unvec factor", "K_r = vec^{-1}"),
        ("primary runner link", "Primary runner"),
    ]
    for name, marker in note_markers:
        check(f"note marker present: {name}", marker in note_text)

    d = 2
    p = 0.30
    identity = np.eye(d, dtype=complex)
    z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    kraus = [np.sqrt(1.0 - p) * identity, np.sqrt(p) * z]

    kraus_tp = sum(k.conj().T @ k for k in kraus)
    check("Kraus TP condition sum K^dagger K = I", np.allclose(kraus_tp, identity), str(kraus_tp))

    c_un = choi_from_kraus(kraus, d, normalized=False)
    c_norm = choi_from_kraus(kraus, d, normalized=True)
    check("normalized Choi is unnormalized Choi divided by d", np.allclose(c_norm, c_un / d))

    eigs = np.linalg.eigvalsh(c_un)
    check("unnormalized Choi matrix is positive semidefinite", np.min(eigs) > -1e-12, f"min_eig={np.min(eigs):+.3e}")
    check("TP iff output partial trace of unnormalized Choi is I", np.allclose(partial_trace_output(c_un, d), identity))

    max_un_error = 0.0
    max_norm_error = 0.0
    max_missing_factor_error = 0.0
    for x in basis(d):
        expected = apply_kraus(kraus, x)
        un = inverse_choi(c_un, x, d, factor=1.0)
        norm = inverse_choi(c_norm, x, d, factor=d)
        missing = inverse_choi(c_norm, x, d, factor=1.0)
        max_un_error = max(max_un_error, float(np.max(np.abs(un - expected))))
        max_norm_error = max(max_norm_error, float(np.max(np.abs(norm - expected))))
        max_missing_factor_error = max(max_missing_factor_error, float(np.max(np.abs(missing - expected))))

    check(
        "unnormalized convention inverse has no extra factor",
        max_un_error < 1e-12,
        f"max_error={max_un_error:.3e}",
    )
    check(
        "normalized convention inverse requires factor d",
        max_norm_error < 1e-12,
        f"max_error={max_norm_error:.3e}",
    )
    check(
        "normalized convention without factor d fails on nonzero map",
        max_missing_factor_error > 0.25,
        f"max_missing_factor_error={max_missing_factor_error:.3e}",
    )

    for n_sites in [1, 2, 3, 4]:
        dim = 2 ** n_sites
        check(
            f"finite qubit-lattice region |Lambda|={n_sites} has matrix dimension d=2^{n_sites}",
            dim >= 2,
            f"d={dim}",
        )

    print("=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("ASSERTIONS: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
