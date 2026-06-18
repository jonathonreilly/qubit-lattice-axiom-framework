#!/usr/bin/env python3
"""Checks the constant-field scalar generator-shift bridge.

The runner verifies the finite-dimensional identity-perturbation theorem used
by the gravity fixed-energy eikonal packet:

    H_s = H_0 + s I.

It checks the source-note boundary text, the retained weak-field source/action
dependency, exact finite-matrix spectrum shifting, diagonal translation
covariance, unit normalization dE/ds=1, and the fixed-energy sign used by the
downstream eikonal phase-count packet.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GRAVITY_CONSTANT_FIELD_SCALAR_GENERATOR_SHIFT_BOUNDED_THEOREM_NOTE_2026-06-18.md"
WEAK_FIELD = ROOT / "docs" / "GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
EIKONAL = ROOT / "docs" / "GRAVITY_FIXED_ENERGY_EIKONAL_INDEX_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{tag}: {label}{suffix}")


def periodic_laplacian(n: int) -> np.ndarray:
    h = np.zeros((n, n), dtype=float)
    for i in range(n):
        h[i, i] = 2.0
        h[i, (i - 1) % n] = -1.0
        h[i, (i + 1) % n] = -1.0
    return h


def translation_matrix(n: int) -> np.ndarray:
    t = np.zeros((n, n), dtype=float)
    for i in range(n):
        t[(i + 1) % n, i] = 1.0
    return t


def lam_axis(k: float) -> float:
    return 2.0 - 2.0 * math.cos(k)


def d_lam_axis(k: float) -> float:
    return 2.0 * math.sin(k)


def k_of_shift(e: float, s: float) -> float:
    return math.acos(1.0 - (e - s) / 2.0)


def main() -> int:
    note = NOTE.read_text(encoding="utf-8")
    weak = WEAK_FIELD.read_text(encoding="utf-8")
    eikonal = EIKONAL.read_text(encoding="utf-8")
    axioms = AXIOMS.read_text(encoding="utf-8")
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]

    required_note_phrases = [
        "Claim type:** bounded_theorem",
        "Status authority:** independent audit lane only",
        "H_s = H_0 + s I",
        "D_s = s I",
        "dE_j/ds = 1",
        "lambda_axis(k_s) + s = E",
        "positive `s` lowers the fixed-energy wavenumber",
        "No observed constants, fitted selectors, PDG values, textbook WKB theorem",
        "does not add an axiom",
        "does not set `G_Newton`",
        "does not supply an audit verdict or effective status change",
    ]
    for phrase in required_note_phrases:
        check(f"note contains required phrase: {phrase}", phrase in note)

    forbidden_note_phrases = [
        "**Status:** retained",
        "full Einstein equations are derived",
        "physical `G_Newton` is derived",
        "adds a new axiom",
        "textbook WKB theorem supplies the proof",
    ]
    for phrase in forbidden_note_phrases:
        check(f"note excludes forbidden phrase: {phrase}", phrase not in note)

    check(
        "weak-field bridge dependency is retained_bounded in current ledger",
        rows.get("gravity_weak_field_source_response_bridge_bounded_theorem_note_2026-06-11", {}).get("effective_status")
        == "retained_bounded",
    )
    check(
        "weak-field dependency supplies action sign convention",
        "S_test(phi; x) = L_test (1 - phi(x))" in weak
        and "H = -Delta_lat" in weak
        and "U_test(phi; x) = -m phi(x)" in weak,
    )
    check(
        "minimal axioms do not contain scalar generator-shift axiom",
        "H_s = H_0 + s I" not in axioms and "scalar generator shift" not in axioms.lower(),
    )

    n = 9
    h0 = periodic_laplacian(n)
    ident = np.eye(n)
    s = 0.037
    hs = h0 + s * ident
    check("finite matrix satisfies H_s - H_0 = sI", np.allclose(hs - h0, s * ident))
    check("identity perturbation commutes with H_0", np.allclose(h0 @ ident - ident @ h0, 0.0))

    eig0 = np.linalg.eigvalsh(h0)
    eigs = np.linalg.eigvalsh(hs)
    check("every eigenvalue shifts by +s", np.allclose(eigs - eig0, s, atol=1.0e-12))

    eps = 1.0e-6
    eig_plus = np.linalg.eigvalsh(h0 + eps * ident)
    eig_minus = np.linalg.eigvalsh(h0 - eps * ident)
    deriv = (eig_plus - eig_minus) / (2.0 * eps)
    check("unit normalization gives dE_j/ds = 1 for all modes", np.allclose(deriv, np.ones(n), atol=1.0e-10))

    t = translation_matrix(n)
    basis = []
    for j in range(n):
        d = np.zeros(n)
        d[j] = 1.0
        mat = np.diag(d)
        comm = t @ mat - mat @ t
        basis.append(comm.reshape(-1))
    constraint = np.stack(basis, axis=1)
    rank = np.linalg.matrix_rank(constraint, tol=1.0e-12)
    check("translation-covariant diagonal perturbation space is one-dimensional", n - rank == 1)

    random_diag = np.diag(np.linspace(0.1, 0.9, n))
    check("nonconstant diagonal perturbation fails translation covariance", not np.allclose(t @ random_diag, random_diag @ t))
    check("constant diagonal perturbation is translation covariant", np.allclose(t @ (s * ident), (s * ident) @ t))

    e = 0.04
    k0 = k_of_shift(e, 0.0)
    check("free axis branch solves lambda(k0)=E", abs(lam_axis(k0) - e) < 1.0e-14)
    check("selected branch has positive derivative", d_lam_axis(k0) > 0.0, f"dlam={d_lam_axis(k0):.8f}")

    sign_ok = True
    exact_ok = True
    prev = k0
    for shift in [0.0005, 0.001, 0.002, 0.004]:
        ks = k_of_shift(e, shift)
        exact_ok &= abs(lam_axis(ks) + shift - e) < 1.0e-14
        sign_ok &= ks < prev
        prev = ks
    check("fixed-energy equation lambda_axis(k_s)+s=E is exact", exact_ok)
    check("positive s lowers fixed-energy wavenumber", sign_ok)

    numeric_dk = (k_of_shift(e, eps) - k_of_shift(e, -eps)) / (2.0 * eps)
    exact_dk = -1.0 / d_lam_axis(k0)
    check("dk_s/ds = -1/lambda_axis'(k0)", abs(numeric_dk - exact_dk) < 1.0e-8)

    c_e = 1.0 / (k0 * d_lam_axis(k0))
    shifts = np.array([0.0004, 0.0012, 0.0008, 0.0016], dtype=float)
    lengths = np.array([1.0, 0.75, 1.5, 0.5], dtype=float)
    ks = np.array([k_of_shift(e, float(x)) for x in shifts])
    optical = float(np.dot(ks / k0, lengths))
    linear = float(np.sum(lengths) - c_e * np.dot(shifts, lengths))
    check("downstream first-order sign is S_eik=L-c_E int s dl", abs(optical - linear) < 5.0e-4)
    check("c_E is positive for the selected branch", c_e > 0.0, f"c_E={c_e:.8f}")

    check(
        "eikonal consumer cites the new scalar-shift bridge",
        "GRAVITY_CONSTANT_FIELD_SCALAR_GENERATOR_SHIFT_BOUNDED_THEOREM_NOTE_2026-06-18.md" in eikonal
        and "unit normalization `dE_j/ds = 1`" in eikonal
        and "lambda_axis(k_s) + s = E" in eikonal,
    )

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
