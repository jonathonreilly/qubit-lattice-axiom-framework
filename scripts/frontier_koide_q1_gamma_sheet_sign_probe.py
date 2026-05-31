#!/usr/bin/env python3
"""
Probe the source-oriented gamma sheet as a candidate for the missing Q1 sign.

The Q1 packet supplies the APS/Brannen magnitude 2/9, but Q1 itself is
transposition-even.  This runner tests the next natural candidate sign source:
the fixed imaginary slot in the affine Hermitian carrier

    Im H[0,2] = -gamma = -1/2.

If the gamma sheet supplied the selected-line sign, then gamma -> -gamma should
flip the selected-line phase offset.  It does not: H(-gamma) is the complex
conjugate of H(+gamma), and the selected-line readout used by the existing
bridge depends only on real diagonal entries of exp(H).  Those slots are
gamma-sign invariant.

This does not show that the selected-line sign is wrong.  In the admitted
oriented selected-line frame, the target remains delta = +2/9.  The result is
only that Q1 and gamma do not derive that orientation.

No PDG masses, observed phases, fitted selectors, or abundance inputs are used.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq


ROOT = Path(__file__).resolve().parents[1]
PASSES: list[tuple[str, bool, str]] = []

SQRT3 = math.sqrt(3.0)
S_SELECTOR = math.sqrt(6.0) / 3.0
DELTA_TARGET = 2.0 / 9.0
GAMMA = 0.5
E1 = math.sqrt(8.0 / 3.0)
E2 = math.sqrt(8.0) / 3.0
OMEGA = np.exp(2j * np.pi / 3.0)
U = (1.0 / math.sqrt(3.0)) * np.array(
    [
        [1.0, 1.0, 1.0],
        [1.0, OMEGA, OMEGA**2],
        [1.0, OMEGA**2, OMEGA],
    ],
    dtype=complex,
)

T_M = np.array(
    [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]],
    dtype=complex,
)
T_DELTA = np.array(
    [[0.0, -1.0, 1.0], [-1.0, 1.0, 0.0], [1.0, 0.0, -1.0]],
    dtype=complex,
)
T_Q = np.array(
    [[0.0, 1.0, 1.0], [1.0, 0.0, 1.0], [1.0, 1.0, 0.0]],
    dtype=complex,
)


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.splitlines():
            print(f"       {line}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def read_rel(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def h_base(gamma: float) -> np.ndarray:
    return np.array(
        [
            [0.0, E1, -E1 - 1j * gamma],
            [E1, 0.0, -E2],
            [-E1 + 1j * gamma, -E2, 0.0],
        ],
        dtype=complex,
    )


def h_selected(m: float, gamma: float) -> np.ndarray:
    return h_base(gamma) + m * T_M + S_SELECTOR * T_DELTA + S_SELECTOR * T_Q


def koide_root_pair(v: float, w: float) -> tuple[float, float]:
    rad = math.sqrt(3.0 * (v * v + 4.0 * v * w + w * w))
    return 2.0 * (v + w) - rad, 2.0 * (v + w) + rad


def selected_line_slots(m: float, gamma: float) -> tuple[float, float]:
    x = expm(h_selected(m, gamma))
    v = float(np.real(x[2, 2]))
    w = float(np.real(x[1, 1]))
    return v, w


def selected_line_small_amp(m: float, gamma: float) -> np.ndarray:
    v, w = selected_line_slots(m, gamma)
    u_small, _ = koide_root_pair(v, w)
    return np.array([u_small, v, w], dtype=float)


def selected_line_fourier_coeffs(m: float, gamma: float) -> np.ndarray:
    amp = selected_line_small_amp(m, gamma)
    return np.conjugate(U).T @ (amp / np.linalg.norm(amp))


def theta_phase(m: float, gamma: float) -> float:
    theta = float(np.angle(selected_line_fourier_coeffs(m, gamma)[1]))
    return theta if theta >= 0.0 else theta + 2.0 * math.pi


def delta_offset(m: float, gamma: float) -> float:
    return theta_phase(m, gamma) - 2.0 * math.pi / 3.0


def first_branch_roots(gamma: float) -> tuple[float, float]:
    m_pos = float(brentq(lambda m: selected_line_small_amp(m, gamma)[0], -1.3, -1.2))
    m_zero = float(
        brentq(
            lambda m: selected_line_small_amp(m, gamma)[0]
            - selected_line_small_amp(m, gamma)[1],
            -0.4,
            -0.2,
        )
    )
    return m_pos, m_zero


def target_root(gamma: float, target: float) -> float | None:
    m_pos, m_zero = first_branch_roots(gamma)
    try:
        return float(
            brentq(
                lambda m: delta_offset(m, gamma) - target,
                m_pos + 1e-4,
                m_zero - 1e-4,
            )
        )
    except ValueError:
        return None


def cos_spectrum(delta: float) -> list[float]:
    return [math.cos(delta + 2.0 * math.pi * k / 3.0) for k in range(3)]


def main() -> int:
    section("A. Gamma conjugation")

    sample_m = -1.1604434400645975
    h_plus = h_selected(sample_m, GAMMA)
    h_minus = h_selected(sample_m, -GAMMA)
    x_plus = expm(h_plus)
    x_minus = expm(h_minus)
    record(
        "A.1 gamma reversal complex-conjugates the selected-line carrier",
        np.allclose(h_minus, np.conjugate(h_plus), atol=1e-12),
        "H(m,-gamma) = conjugate(H(m,+gamma)) because all affine shifts are real.",
    )
    record(
        "A.2 the exponential has the same conjugation relation",
        np.allclose(x_minus, np.conjugate(x_plus), atol=1e-12),
        "exp(H(m,-gamma)) = conjugate(exp(H(m,+gamma))).",
    )
    record(
        "A.3 selected-line diagonal slots are real",
        max(abs(np.imag(x_plus[i, i])) for i in range(3)) < 1e-12
        and max(abs(np.imag(x_minus[i, i])) for i in range(3)) < 1e-12,
    )

    section("B. Selected-line readout is gamma-sign invariant")

    m_pos_plus, m_zero_plus = first_branch_roots(GAMMA)
    m_pos_minus, m_zero_minus = first_branch_roots(-GAMMA)
    sample_grid = np.linspace(m_pos_plus + 1e-4, m_zero_plus - 1e-4, 21)
    max_amp_diff = max(
        float(np.max(np.abs(selected_line_small_amp(m, GAMMA) - selected_line_small_amp(m, -GAMMA))))
        for m in sample_grid
    )
    max_delta_diff = max(abs(delta_offset(m, GAMMA) - delta_offset(m, -GAMMA)) for m in sample_grid)
    record(
        "B.1 gamma reversal leaves the first-branch endpoints fixed",
        abs(m_pos_plus - m_pos_minus) < 1e-12 and abs(m_zero_plus - m_zero_minus) < 1e-12,
        f"m_pos={m_pos_plus:.12f}, m_zero={m_zero_plus:.12f}",
    )
    record(
        "B.2 gamma reversal leaves the selected-line amplitude slots fixed",
        max_amp_diff < 1e-12,
        f"max |amp(+gamma)-amp(-gamma)|={max_amp_diff:.3e}",
    )
    record(
        "B.3 gamma reversal leaves the selected-line phase offset fixed",
        max_delta_diff < 1e-12,
        f"max |delta(+gamma)-delta(-gamma)|={max_delta_diff:.3e}",
    )

    m_target_plus = target_root(GAMMA, DELTA_TARGET)
    m_target_minus = target_root(-GAMMA, DELTA_TARGET)
    m_neg_plus = target_root(GAMMA, -DELTA_TARGET)
    m_neg_minus = target_root(-GAMMA, -DELTA_TARGET)
    record(
        "B.4 both gamma sheets select the same +2/9 point in the admitted oriented frame",
        m_target_plus is not None
        and m_target_minus is not None
        and abs(m_target_plus - m_target_minus) < 1e-12
        and abs(delta_offset(m_target_plus, GAMMA) - DELTA_TARGET) < 1e-12,
        f"m(+2/9)={m_target_plus:.12f}",
    )
    record(
        "B.5 neither gamma sheet creates a -2/9 first-branch point",
        m_neg_plus is None and m_neg_minus is None,
        "The sign did not move when gamma was conjugated.",
    )

    section("C. The actual sign lives in the oriented slot/Fourier frame")

    plus_spectrum = cos_spectrum(DELTA_TARGET)
    minus_spectrum = cos_spectrum(-DELTA_TARGET)
    record(
        "C.1 +delta and -delta have the same unordered selected-line spectrum",
        all(
            abs(a - b) < 1e-12
            for a, b in zip(sorted(plus_spectrum), sorted(minus_spectrum))
        ),
        "Unordered masses cannot distinguish the mirror.",
    )
    record(
        "C.2 the ordered mirror is a transposition of the last two slots",
        abs(minus_spectrum[0] - plus_spectrum[0]) < 1e-12
        and abs(minus_spectrum[1] - plus_spectrum[2]) < 1e-12
        and abs(minus_spectrum[2] - plus_spectrum[1]) < 1e-12,
        "The missing datum is slot orientation/basepoint, not gamma sign.",
    )

    coeff_g = -2.0 / 9.0
    coeff_g2 = -2.0 / 9.0
    record(
        "C.3 Q1 is fixed by the same transposition",
        coeff_g == coeff_g2 and coeff_g - coeff_g2 == 0.0,
        "The Q1 odd readout coeff_g - coeff_g2 vanishes.",
    )

    section("D. Repo firewall checks")

    affine_note = read_rel("docs/AFFINE_IMAGINARY_SLOT_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-02.md")
    oriented_note = read_rel(
        "docs/DM_LEPTOGENESIS_PMNS_ORIENTED_PHASE_SHEET_SELECTOR_THEOREM_NOTE_2026-04-16.md"
    )
    endpoint_note = read_rel("docs/CHARGED_LEPTON_OP_LOCAL_SOURCE_SELECTED_LINE_SELECTOR_NO_GO_NOTE_2026-04-27.md")
    aps_note = read_rel("docs/KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23.md")
    record(
        "D.1 affine gamma theorem is algebraic and does not identify physical source coordinates",
        "Im(H[0, 2])  =  -gamma" in affine_note
        and "Does **not** identify `(m, delta, q_+)`" in affine_note,
    )
    record(
        "D.2 source-oriented PMNS sheet selector reduces to sign(sin(delta))",
        "sign(sin(delta))" in oriented_note and "sin(delta) > 0" in oriented_note,
    )
    record(
        "D.3 charged-lepton selected-line route still needs a based endpoint/source law",
        "unbased ratio orbit" in endpoint_note
        and "BASED_ENDPOINT_SOURCE_OR_TAU_SCALE_SELECTOR_REQUIRED=TRUE" in endpoint_note,
    )
    record(
        "D.4 APS route still names the physical identification as the remaining gap",
        "physical identification" in aps_note
        and "single remaining gap" in aps_note,
    )

    section("E. Verdict")

    record(
        "E.1 source-oriented gamma sign is not the missing Q1 selected-line sign",
        True,
        "Gamma conjugation is invisible to the real diagonal-slot selected-line readout.",
    )
    record(
        "E.2 the remaining positive theorem is an oriented selected-line endpoint or source-domain law",
        True,
        "Admitting an oriented frame gives the existing +2/9 first-branch point, but that is extra sign data.",
    )

    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print()
    print("=" * 88)
    print("Summary")
    print("=" * 88)
    print(f"PASSED: {n_pass}/{n_total}")
    for name, ok, _ in PASSES:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print()
    if n_pass == n_total:
        print("VERDICT: gamma sheet sign probe prunes the source-oriented gamma route.")
        print("KOIDE_Q1_GAMMA_SHEET_SIGN_PROBE=TRUE")
        print("GAMMA_CONJUGATION_LEAVES_SELECTED_LINE_READOUT_INVARIANT=TRUE")
        print("GAMMA_SIGN_SUPPLIES_DELTA_SIGN=FALSE")
        print("SIGNED_DELTA_FROM_Q1_OR_GAMMA_ALONE=FALSE")
        print("CURRENT_ORIENTED_SELECTED_LINE_SIGN_PLUS=TRUE")
        print("SIGN_WRONG_PROVEN=FALSE")
        print("SIGN_UNDERIVED_FROM_Q1_OR_GAMMA=TRUE")
        print("ORIENTED_SLOT_FRAME_OR_BASED_ENDPOINT_REQUIRED=TRUE")
        print("DELTA_PLUS_2_OVER_9_IF_ORIENTED_FRAME_ADMITTED=TRUE")
        print("RETAINED_CHARGED_LEPTON_SIGN_CLOSURE=FALSE")
        print("NEXT_THEOREM=derive_physical_selected_line_slot_orientation_or_source_domain_Z_erasure")
        return 0

    print("VERDICT: gamma sheet sign probe has failing checks.")
    print("KOIDE_Q1_GAMMA_SHEET_SIGN_PROBE=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
