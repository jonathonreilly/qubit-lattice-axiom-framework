#!/usr/bin/env python3
"""Checks the fixed-energy eikonal index bridge for gravity Premise (4)."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GRAVITY_FIXED_ENERGY_EIKONAL_INDEX_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md"
SOURCE_BRIDGE = ROOT / "docs" / "GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
SCALAR_SHIFT_BRIDGE = ROOT / "docs" / "GRAVITY_SCALAR_SHIFT_SIGN_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md"
SCALAR_FIELD_PACKET = ROOT / "docs" / "SELF_CONSISTENCY_FORCES_POISSON_NOTE.md"
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


def lam_axis(k: float) -> float:
    return 2.0 - 2.0 * math.cos(k)


def d_lam_axis(k: float) -> float:
    return 2.0 * math.sin(k)


def k_of_shift(E: float, s: float) -> float:
    return math.acos(1.0 - (E - s) / 2.0)


def main() -> int:
    note_text = NOTE.read_text(encoding="utf-8")
    source_text = SOURCE_BRIDGE.read_text(encoding="utf-8")
    scalar_shift_bridge_text = SCALAR_SHIFT_BRIDGE.read_text(encoding="utf-8")
    scalar_field_text = SCALAR_FIELD_PACKET.read_text(encoding="utf-8")
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]

    required_phrases = [
        "Claim type:** bounded_theorem",
        "Status authority:** independent audit lane only",
        "H_s = H_0 + s I",
        "lambda_axis(k_s) + s = E",
        "n_j := k_{s_j} / k0",
        "S_eik[s] = sum_j n_j Delta l_j",
        "GRAVITY_SCALAR_SHIFT_SIGN_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md",
        "phi_action = c_E s",
        "c_E = 1 / (k0 lambda_axis'(k0))",
        "c_E = 1/(2E) + 1/24 + O(E)",
        "n(s) = 1 - (1/(2E) + 1/24 + O(E)) s + O(s^2/E^2).",
        "order-one `1/24` correction",
        "No observed constants, PDG values, fitted selectors, new repo-wide axioms",
        "it does not rederive universal matter coupling",
        "The scalar generator shift/sign and fixed-energy action normalization are",
        "Independent audit must decide",
    ]
    for phrase in required_phrases:
        check(f"note contains required phrase: {phrase}", phrase in note_text)

    forbidden_phrases = [
        "**Status:** retained",
        "full Einstein equations are derived",
        "G_Newton in SI units is derived",
        "adds a new axiom",
        "textbook theorem supplies the proof",
    ]
    for phrase in forbidden_phrases:
        check(f"note excludes forbidden phrase: {phrase}", phrase not in note_text)

    bridge_row = rows.get("gravity_weak_field_source_response_bridge_bounded_theorem_note_2026-06-11", {})
    scalar_field_row = rows.get("self_consistency_forces_poisson_note", {})
    check(
        "weak-field source-response bridge is retained_bounded in current ledger",
        bridge_row.get("effective_status") == "retained_bounded",
        f"effective_status={bridge_row.get('effective_status')}",
    )
    check(
        "self-consistency scalar-field packet is retained_bounded in current ledger",
        scalar_field_row.get("effective_status") == "retained_bounded",
        f"effective_status={scalar_field_row.get('effective_status')}",
    )
    check(
        "source-response bridge supplies S_test sign convention",
        "S_test(phi; x) = L_test (1 - phi(x))" in source_text
        and "U_test(phi; x) = -m phi(x)" in source_text,
    )
    check(
        "new scalar-shift bridge derives +sI sign and action normalization",
        "H_s = H_0 + s I" in scalar_shift_bridge_text
        and "lambda_axis(k_s) + s = E" in scalar_shift_bridge_text
        and "phi_action := c_E s" in scalar_shift_bridge_text
        and "s = phi_action / c_E = k0 lambda_axis'(k0) phi_action" in scalar_shift_bridge_text,
    )
    check(
        "eikonal note consumes the new scalar-shift bridge",
        "GRAVITY_SCALAR_SHIFT_SIGN_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md" in note_text
        and "phi_action = c_E s" in note_text,
    )
    check(
        "self-consistency packet supplies scalar propagator/action surface",
        "The propagator uses action S = L(1-phi)" in scalar_field_text
        and "gravitational field phi is sourced" in scalar_field_text,
    )

    E = 0.04
    k0 = k_of_shift(E, 0.0)
    check("free wavenumber solves lambda(k0)=E", abs(lam_axis(k0) - E) < 1e-14)
    check("axis derivative is positive on selected branch", d_lam_axis(k0) > 0.0, f"dlam={d_lam_axis(k0):.8f}")

    exact_ok = True
    monotone_ok = True
    prior_k = k0
    for s in [0.0005, 0.001, 0.002, 0.004]:
        ks = k_of_shift(E, s)
        exact_ok &= abs(lam_axis(ks) + s - E) < 1e-14
        monotone_ok &= ks < prior_k
        prior_k = ks
    check("scalar-shifted symbol solves lambda(k_s)+s=E exactly", exact_ok)
    check("positive scalar shift lowers fixed-energy wavenumber", monotone_ok)

    h = 1e-6
    deriv_numeric = (k_of_shift(E, h) / k0 - k_of_shift(E, -h) / k0) / (2.0 * h)
    c_exact = 1.0 / (k0 * d_lam_axis(k0))
    check(
        "first derivative of n=k/k0 is -1/(k0 lambda'(k0))",
        abs(deriv_numeric + c_exact) < 1e-8,
        f"numeric={deriv_numeric:.10f}, exact={-c_exact:.10f}",
    )
    check(
        "small-k coefficient agrees with 1/(2E) at weak-field accuracy",
        abs(c_exact - 1.0 / (2.0 * E)) / (1.0 / (2.0 * E)) < 0.02,
        f"c_exact={c_exact:.8f}, 1/(2E)={1/(2*E):.8f}",
    )
    series_residuals = []
    correction_improves = True
    for e_test in [0.04, 0.01, 0.0025]:
        k_test = k_of_shift(e_test, 0.0)
        c_test = 1.0 / (k_test * d_lam_axis(k_test))
        leading = 1.0 / (2.0 * e_test)
        corrected = leading + 1.0 / 24.0
        correction_improves &= abs(c_test - corrected) < abs(c_test - leading)
        series_residuals.append((c_test - corrected) / e_test)
    target_residual = 11.0 / 1440.0
    check(
        "small-k expansion includes the +1/24 lattice correction beyond 1/(2E)",
        correction_improves and max(abs(r - target_residual) for r in series_residuals) < 1.0e-4,
        "residuals="
        + ",".join(f"{r:.8f}" for r in series_residuals)
        + f"; target={target_residual:.8f}",
    )

    lengths = np.array([1.0, 0.5, 1.7, 0.8, 1.2], dtype=float)
    shifts = np.array([0.0004, 0.0012, 0.0008, 0.0016, 0.0002], dtype=float)
    ks = np.array([k_of_shift(E, float(s)) for s in shifts])
    phase = float(np.dot(ks, lengths))
    optical = float(np.dot(ks / k0, lengths))
    check("normalized phase count equals sum (k_s/k0) Delta l", abs(phase / k0 - optical) < 1e-13)

    L = float(np.sum(lengths))
    linear = L - c_exact * float(np.dot(shifts, lengths))
    second_order_error = abs(optical - linear)
    check(
        "linearized eikonal action has sign S=L-c_E int s dl",
        second_order_error < 5e-4,
        f"error={second_order_error:.3e}",
    )

    no_shift = np.zeros_like(shifts)
    ks0 = np.array([k_of_shift(E, float(s)) for s in no_shift])
    check("zero scalar shift gives n=1 on every segment", np.allclose(ks0 / k0, np.ones_like(ks0)))

    a = 0.7
    c = c_exact
    ray_ok = True
    products = []
    for b in [3.0, 5.0, 8.0, 13.0]:
        alpha = c * quad(lambda z: a * b / (b * b + z * z) ** 1.5, -np.inf, np.inf)[0]
        target = 2.0 * c * a / b
        ray_ok &= abs(alpha - target) < 1e-8
        products.append(alpha * b)
    check("linearized eikonal ray-angle magnitude is 2 c_E a / b", ray_ok)
    check("ray-angle product alpha*b is constant", max(products) - min(products) < 1e-8)

    E2 = 0.01
    k02 = k_of_shift(E2, 0.0)
    c2 = 1.0 / (k02 * d_lam_axis(k02))
    check(
        "continuum limit improves c_E -> 1/(2E)",
        abs(c2 - 1.0 / (2.0 * E2)) / (1.0 / (2.0 * E2)) < abs(c_exact - 1.0 / (2.0 * E)) / (1.0 / (2.0 * E)),
        f"rel_E={abs(c_exact - 1/(2*E))/(1/(2*E)):.3e}, rel_E2={abs(c2 - 1/(2*E2))/(1/(2*E2)):.3e}",
    )

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
