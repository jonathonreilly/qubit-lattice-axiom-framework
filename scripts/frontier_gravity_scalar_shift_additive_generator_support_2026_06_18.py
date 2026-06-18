#!/usr/bin/env python3
"""Support runner for the gravity scalar-shift additive generator bridge."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GRAVITY_SCALAR_SHIFT_ADDITIVE_GENERATOR_SUPPORT_NOTE_2026-06-18.md"
PARENT = ROOT / "docs" / "GRAVITY_FIXED_ENERGY_EIKONAL_INDEX_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md"
SOURCE_BRIDGE = ROOT / "docs" / "GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
SCALAR_SURFACE = ROOT / "docs" / "SELF_CONSISTENCY_FORCES_POISSON_NOTE.md"
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


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def lam_axis(k: float) -> float:
    return 2.0 - 2.0 * math.cos(k)


def d_lam_axis(k: float) -> float:
    return 2.0 * math.sin(k)


def k_of_shift(e_value: float, shift: float) -> float:
    return math.acos(1.0 - (e_value - shift) / 2.0)


def open_path_laplacian(size: int) -> np.ndarray:
    mat = np.zeros((size, size), dtype=float)
    for i in range(size):
        if i > 0:
            mat[i, i] += 1.0
            mat[i, i - 1] = -1.0
        if i + 1 < size:
            mat[i, i] += 1.0
            mat[i, i + 1] = -1.0
    return mat


def main() -> int:
    print("Gravity scalar-shift additive generator support")
    print("Source-side bounded support only; no audit status is set here.")

    note_text = read(NOTE)
    parent_text = read(PARENT)
    source_text = read(SOURCE_BRIDGE)
    scalar_text = read(SCALAR_SURFACE)
    rows = json.loads(read(LEDGER))["rows"]

    required_note_phrases = [
        "H_s = H_0 + s I",
        "c_E s = phi_phys",
        "lambda_axis(k_s) + s = E",
        "k_s/k0 = 1 - phi_phys + O(phi_phys^2)",
        "positive",
        "`phi_phys` gives positive `s`",
        "does not derive a physical Newton constant",
        "Independent audit decides",
    ]
    for phrase in required_note_phrases:
        check(f"support note contains required phrase: {phrase}", phrase in note_text)

    forbidden_note_phrases = [
        "**Status:** " + "retained",
        "G_Newton in SI units " + "is derived",
        "full Einstein " + "equations",
        "textbook theorem supplies the proof",
        "adds a new axiom",
    ]
    for phrase in forbidden_note_phrases:
        check(f"support note excludes forbidden phrase: {phrase}", phrase not in note_text)

    check(
        "parent eikonal note links the scalar-shift support note",
        "GRAVITY_SCALAR_SHIFT_ADDITIVE_GENERATOR_SUPPORT_NOTE_2026-06-18.md"
        in parent_text,
    )
    check(
        "weak-field action source supplies the sign convention",
        "S_test(phi; x) = L_test (1 - phi(x))" in source_text
        and "U_test(phi; x) = -m phi(x)" in source_text,
    )
    check(
        "scalar surface supplies propagator/action context",
        "The propagator uses action S = L(1-phi)" in scalar_text
        and "gravitational field phi is sourced" in scalar_text,
    )
    for claim_id in [
        "gravity_weak_field_source_response_bridge_bounded_theorem_note_2026-06-11",
        "self_consistency_forces_poisson_note",
    ]:
        row = rows.get(claim_id, {})
        check(
            f"one-hop input has current retained_bounded effective status: {claim_id}",
            row.get("effective_status") == "retained_bounded",
            f"effective_status={row.get('effective_status')}",
        )

    size = 31
    h0 = open_path_laplacian(size)
    shift = 0.037
    hs = h0 + shift * np.eye(size)
    vals0, vecs0 = np.linalg.eigh(h0)
    vals_s, vecs_s = np.linalg.eigh(hs)
    check(
        "finite open-path Laplacian eigenvalues shift by +s",
        np.max(np.abs(vals_s - vals0 - shift)) < 1.0e-12,
        f"max_error={np.max(np.abs(vals_s - vals0 - shift)):.3e}",
    )
    overlap = np.abs(np.diag(vecs0.T @ vecs_s))
    check(
        "finite nondegenerate eigenvectors are unchanged up to signs by +sI",
        float(np.min(overlap)) > 1.0 - 1.0e-10,
        f"min_overlap={float(np.min(overlap)):.12f}",
    )

    e_value = 0.04
    k0 = k_of_shift(e_value, 0.0)
    c_e = 1.0 / (k0 * d_lam_axis(k0))
    check("free symbol solves lambda(k0)=E", abs(lam_axis(k0) - e_value) < 1.0e-14)
    check("c_E is positive on the selected branch", c_e > 0.0, f"c_E={c_e:.10f}")

    scalar_fields = [0.0005, 0.0010, 0.0020]
    sign_ok = True
    norm_ok = True
    exact_ok = True
    for phi_phys in scalar_fields:
        s = phi_phys / c_e
        ks = k_of_shift(e_value, s)
        exact_ok &= abs(lam_axis(ks) + s - e_value) < 1.0e-14
        sign_ok &= s > 0.0 and ks < k0
        first_order = 1.0 - phi_phys
        norm_ok &= abs((ks / k0) - first_order) < 2.0e-5
        print(
            f"phi_phys={phi_phys:.6e} s={s:.12e} "
            f"k_s/k0={ks/k0:.12f} first_order={first_order:.12f}"
        )
    check("fixed-energy symbol equation holds for normalized shifts", exact_ok)
    check("positive action field maps to positive +s and lowers k_s", sign_ok)
    check("normalization c_E*s=phi_phys gives first-order S/L=1-phi_phys", norm_ok)

    h = 1.0e-7
    dn_ds = (k_of_shift(e_value, h) / k0 - k_of_shift(e_value, -h) / k0) / (2.0 * h)
    dn_dphi = dn_ds / c_e
    check(
        "derivative with respect to phi_phys is -1 under c_E*s normalization",
        abs(dn_dphi + 1.0) < 1.0e-8,
        f"dn_dphi={dn_dphi:.12f}",
    )
    check(
        "small-k c_E approaches 1/(2E)",
        abs(c_e - 1.0 / (2.0 * e_value)) / (1.0 / (2.0 * e_value)) < 0.02,
        f"c_E={c_e:.10f}",
    )

    e_lower = 0.01
    k_lower = k_of_shift(e_lower, 0.0)
    c_lower = 1.0 / (k_lower * d_lam_axis(k_lower))
    rel_e = abs(c_e - 1.0 / (2.0 * e_value)) / (1.0 / (2.0 * e_value))
    rel_lower = abs(c_lower - 1.0 / (2.0 * e_lower)) / (1.0 / (2.0 * e_lower))
    check(
        "continuum coefficient improves as E decreases",
        rel_lower < rel_e,
        f"rel_E={rel_e:.3e}, rel_lower={rel_lower:.3e}",
    )

    lengths = np.array([0.7, 1.1, 0.4, 1.8], dtype=float)
    phis = np.array([0.0004, 0.0012, 0.0008, 0.0016], dtype=float)
    shifts = phis / c_e
    ks = np.array([k_of_shift(e_value, float(s)) for s in shifts])
    normalized_phase = float(np.dot(ks / k0, lengths))
    weak_action = float(np.dot(1.0 - phis, lengths))
    check(
        "piecewise normalized phase matches weak action to first order",
        abs(normalized_phase - weak_action) < 3.0e-5,
        f"error={abs(normalized_phase - weak_action):.3e}",
    )

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
