#!/usr/bin/env python3
"""Koide Record sign route diagnosis.

Open-gate support only. The runner checks additivity, sign erasure under
squaring, an eta counterexample, and the observed all-positive comparator.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "KOIDE_RECORD_SIGN_AGNOSTIC_ETA_REFUTED_2026-06-04.md"
PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def blockdiag(*mats: np.ndarray) -> np.ndarray:
    size = sum(m.shape[0] for m in mats)
    out = np.zeros((size, size))
    cursor = 0
    for mat in mats:
        width = mat.shape[0]
        out[cursor : cursor + width, cursor : cursor + width] = mat
        cursor += width
    return out


def koide_q_from_sqrt_masses(values: np.ndarray) -> float:
    return float(np.sum(values**2) / (np.sum(values) ** 2))


def main() -> int:
    print("=" * 72)
    print("Koide Record sign route diagnosis")
    print("=" * 72)
    print("Scope: open-gate route diagnosis; no readout rule adopted.")

    cyclic = np.array([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
    identity = np.eye(3)
    h_one = 1.3 * identity + 0.5 * (cyclic + cyclic.T)
    h_two = np.diag([0.8, -0.4, 1.1])
    combined = blockdiag(h_one, h_two)
    eig_one = np.linalg.eigvalsh(h_one)
    eig_two = np.linalg.eigvalsh(h_two)
    eig_combined = np.linalg.eigvalsh(combined)

    functionals = (
        lambda ev: np.sum(ev),
        lambda ev: np.sum(np.abs(ev)),
        lambda ev: np.sum(np.log(np.abs(ev))),
        lambda ev: np.sum(np.sign(ev)),
    )
    additivity_ok = all(
        abs(func(eig_combined) - (func(eig_one) + func(eig_two))) < 1e-9 for func in functionals
    )
    check("tested_functionals_add_over_direct_sum", additivity_ok)

    x = 0.6
    check("squaring_erases_single_sign", abs(x**2 - (-x) ** 2) < 1e-15)

    spectrum_a = np.array([1.0, 1.0, 1.0])
    spectrum_b = np.array([1.0, 1.0, 4.0])
    eta_a = np.sum(np.sign(spectrum_a))
    eta_b = np.sum(np.sign(spectrum_b))
    q_a = koide_q_from_sqrt_masses(spectrum_a)
    q_b = koide_q_from_sqrt_masses(spectrum_b)
    check(
        "eta_count_does_not_fix_q",
        eta_a == eta_b == 3 and abs(q_a - 1 / 3) < 1e-12 and abs(q_b - 0.5) < 1e-12,
        f"eta=3 for both; q_a={q_a:.4f}, q_b={q_b:.4f}",
    )

    # Comparator only: PDG charged-lepton central masses in GeV.
    masses_gev = np.array([0.51099895e-3, 105.6583755e-3, 1776.86e-3])
    sqrt_m = np.sqrt(masses_gev)
    q_signed = koide_q_from_sqrt_masses(sqrt_m)
    q_unsigned = koide_q_from_sqrt_masses(np.abs(sqrt_m))
    check(
        "charged_lepton_comparator_sign_homogeneous",
        np.all(sqrt_m > 0) and abs(q_signed - q_unsigned) < 1e-12 and abs(q_signed - 2 / 3) < 2e-3,
        f"q_signed=q_unsigned={q_signed:.6f}",
    )

    r = 0.5
    check("r_half_maps_to_q_two_thirds", abs((1 + 2 * r) / 3 - 2 / 3) < 1e-12)

    note_text = NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())
    note_lower = note_flat.lower()
    check("note_declares_open_gate", "**Type:** open_gate" in note_text)
    check(
        "pdg_comparator_non_load_bearing",
        "PDG charged-lepton square-root comparator is a non-load-bearing sanity check only"
        in note_flat
        and "not a framework derivation input" in note_lower,
    )
    check(
        "not_no_go_against_all_signed_readouts",
        "Do not cite this note as a no-go against all signed readout routes" in note_flat
        and "future signed-readout route remains open" in note_flat,
    )
    check(
        "future_route_requires_framework_native_readout",
        "framework-native readout functional" in note_flat
        and "sign data survive the relevant Born/readout stage" in note_flat
        and "proves the needed Koide denominator inside that route" in note_flat,
    )
    check(
        "refutes_only_tested_shortcuts",
        "refutes only the tested sign-blind" in note_lower
        and "`eta`-only shortcuts" in note_text,
    )

    print("=" * 72)
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
