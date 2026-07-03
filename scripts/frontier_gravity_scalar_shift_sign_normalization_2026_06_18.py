#!/usr/bin/env python3
"""Verify the gravity scalar-shift sign and fixed-energy normalization bridge."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GRAVITY_SCALAR_SHIFT_SIGN_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md"
SOURCE_RESPONSE = ROOT / "docs" / "GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
EIKONAL = ROOT / "docs" / "GRAVITY_FIXED_ENERGY_EIKONAL_INDEX_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

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


def axis_laplacian(n: int) -> np.ndarray:
    h = np.zeros((n, n), dtype=float)
    for i in range(n):
        h[i, i] = 2.0
        h[i, (i + 1) % n] = -1.0
        h[i, (i - 1) % n] = -1.0
    return h


def lam_axis(k: float) -> float:
    return 2.0 - 2.0 * math.cos(k)


def d_lam_axis(k: float) -> float:
    return 2.0 * math.sin(k)


def k_of_shift(energy: float, shift: float) -> float:
    return math.acos(1.0 - (energy - shift) / 2.0)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    note = read(NOTE)
    source_response = read(SOURCE_RESPONSE)
    eikonal = read(EIKONAL)
    rows = json.loads(read(LEDGER))["rows"]

    required = [
        "H_s = H_0 + s I",
        "lambda_axis(k_s) + s = E",
        "positive `s` lowers the normalized phase action",
        "phi_action := c_E s",
        "s = phi_action / c_E = k0 lambda_axis'(k0) phi_action",
        "s = 2E phi_action + O(E^2 phi_action)",
        "No observed constants, fitted selectors, textbook WKB theorem, new axiom",
        "Independent audit is the only effective-status authority.",
    ]
    for phrase in required:
        check(f"note contains required phrase: {phrase}", phrase in note)

    forbidden = [
        "**Status:** retained",
        "full Einstein equations",
        "G_Newton in SI units",
        "derives arbitrary-graph WKB",
        "adds a new axiom",
        "textbook WKB theorem supplies the proof",
    ]
    for phrase in forbidden:
        check(f"note excludes forbidden phrase: {phrase}", phrase not in note)

    source_row = rows.get("gravity_weak_field_source_response_bridge_bounded_theorem_note_2026-06-11", {})
    check(
        "weak-field source-response bridge is retained_bounded",
        source_row.get("effective_status") == "retained_bounded",
        f"effective_status={source_row.get('effective_status')}",
    )
    check(
        "source-response note supplies action-lowering sign",
        "S_test(phi; x) = L_test (1 - phi(x))" in source_response
        and "U_test(phi; x) = -m phi(x)" in source_response,
    )
    check(
        "eikonal note already consumes H_s sign surface",
        "H_s = H_0 + s I" in eikonal and "lambda_axis(k_s) + s = E" in eikonal,
    )

    n = 16
    h0 = axis_laplacian(n)
    shift = 0.037
    eig0 = np.sort(np.linalg.eigvalsh(h0))
    eigs = np.sort(np.linalg.eigvalsh(h0 + shift * np.eye(n)))
    check("finite matrix shift sends every eigenvalue to lambda+s", np.allclose(eigs, eig0 + shift))

    ks = [2.0 * math.pi * m / n for m in range(n)]
    expected = np.sort([lam_axis(k) for k in ks])
    check("axis Laplacian spectrum matches 2-2cos(k)", np.allclose(eig0, expected, atol=1e-12))

    energy = 0.04
    k0 = k_of_shift(energy, 0.0)
    c_e = 1.0 / (k0 * d_lam_axis(k0))
    check("free branch solves lambda(k0)=E", abs(lam_axis(k0) - energy) < 1e-14)
    check("normalization coefficient c_E is positive", c_e > 0, f"c_E={c_e:.10f}")

    monotone = True
    prior = k0
    for s in [0.00025, 0.0005, 0.001, 0.002]:
        k_s = k_of_shift(energy, s)
        monotone &= k_s < prior
        prior = k_s
    check("positive +sI shift lowers fixed-energy wavenumber", monotone)

    h = 1e-6
    derivative = (k_of_shift(energy, h) / k0 - k_of_shift(energy, -h) / k0) / (2.0 * h)
    check(
        "d(k_s/k0)/ds equals -c_E",
        abs(derivative + c_e) < 1e-8,
        f"numeric={derivative:.10f}, -c_E={-c_e:.10f}",
    )

    phi_action = 0.015
    normalized_shift = phi_action / c_e
    n_shifted = k_of_shift(energy, normalized_shift) / k0
    check(
        "s=phi_action/c_E gives action density 1-phi_action to first order",
        abs(n_shifted - (1.0 - phi_action)) < 4e-4,
        f"n={n_shifted:.10f}, target={1.0 - phi_action:.10f}",
    )

    small_energy = 0.01
    k_small = k_of_shift(small_energy, 0.0)
    c_small = 1.0 / (k_small * d_lam_axis(k_small))
    scale = 1.0 / c_small
    check(
        "small-k generator shift scale tends to 2E",
        abs(scale - 2.0 * small_energy) / (2.0 * small_energy) < 0.01,
        f"1/c_E={scale:.10f}, 2E={2.0 * small_energy:.10f}",
    )

    negative_shift = -0.001
    check(
        "negative scalar shift raises fixed-energy action density",
        k_of_shift(energy, negative_shift) / k0 > 1.0,
    )

    no_new_axiom = "new axiom" in note and "No observed constants" in note
    no_physical_constant = "physical value of `G_Newton`" in note and "physical Newton constant" in note
    check("boundary denies new axiom route", no_new_axiom)
    check("boundary denies physical Newton-constant normalization", no_physical_constant)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
