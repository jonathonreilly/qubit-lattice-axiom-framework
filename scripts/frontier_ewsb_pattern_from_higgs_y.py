#!/usr/bin/env python3
"""Discriminating checks for EWSB pattern from Higgs Y_H = +1."""

from fractions import Fraction
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "EWSB_PATTERN_FROM_HIGGS_Y_NOTE_2026-05-02.md"
TOL = 1.0e-12

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    print(f"[{tag}] {label} ({detail})")


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def nullspace_from_svd(matrix: np.ndarray, tol: float = TOL):
    _, singular_values, vh = np.linalg.svd(matrix, full_matrices=True)
    rank = int(np.sum(singular_values > tol))
    return vh[rank:].conj().T, singular_values, rank


def coefficient_map(vev: np.ndarray, y_h: float) -> np.ndarray:
    return np.column_stack((T3 @ vev, (y_h * I2) @ vev))


def stabilizer_coefficients(vev: np.ndarray, y_h: float) -> tuple[np.ndarray, np.ndarray, int]:
    mapping = coefficient_map(vev, y_h)
    kernel, singular_values, rank = nullspace_from_svd(mapping)
    if kernel.shape[1] != 1:
        return np.array([np.nan, np.nan], dtype=complex), singular_values, rank
    coeff = kernel[:, 0]
    norm = np.max(np.abs(coeff))
    if norm > 0:
        coeff = coeff / norm
    return coeff, singular_values, rank


def ratio_from_stabilizer(vev: np.ndarray, y_h: float) -> complex:
    coeff, _, _ = stabilizer_coefficients(vev, y_h)
    if abs(coeff[0]) < TOL:
        return np.nan + 0j
    return coeff[1] / coeff[0]


def close(a: np.ndarray, b: np.ndarray, tol: float = TOL) -> bool:
    return np.linalg.norm(a - b) < tol


def frac_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


note_text = NOTE_PATH.read_text(encoding="utf-8")

sigma1 = np.array([[0, 1], [1, 0]], dtype=complex)
sigma2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
T1 = sigma1 / 2
T2 = sigma2 / 2
T3 = sigma3 / 2

# The overall v/sqrt(2) factor cancels in every stabilizer and action check.
vev_lower = np.array([0, 1], dtype=complex)
vev_upper = np.array([1, 0], dtype=complex)


section("Displayed note scope")
displayed_fragments = [
    "Q  =  T_3  +  Y/2",
    "⟨H⟩ = (0, v/√2)^T",
    "T_3 · ⟨H⟩",
    "(T_3 + α·Y) · ⟨H⟩",
    "α  =  +1/2.",
    "T_1 · ⟨H⟩",
    "T_2 · ⟨H⟩",
    "(T_3 − Y/2) · ⟨H⟩",
]
for fragment in displayed_fragments:
    check(f"note displays {fragment!r}", fragment in note_text)


section("E1/E2: neutral-VEV stabilizer inside span{T3, Y}")
check(
    "displayed T3 action on the neutral VEV is -1/2 times the VEV",
    close(T3 @ vev_lower, -0.5 * vev_lower),
    detail=f"T3*vev={T3 @ vev_lower}",
)
check(
    "displayed Y action on the neutral VEV is +1 times the VEV",
    close(I2 @ vev_lower, vev_lower),
    detail=f"Y*vev={I2 @ vev_lower}",
)
coeff, singular_values, rank = stabilizer_coefficients(vev_lower, y_h=1.0)
kernel_dim = 2 - rank
check(
    "E1 stabilizer is exactly one-dimensional by SVD",
    kernel_dim == 1,
    detail=f"singular_values={singular_values}, rank={rank}, nullity={kernel_dim}",
)
annihilator_action = (coeff[0] * T3 + coeff[1] * I2) @ vev_lower
check(
    "E1 computed null vector annihilates the neutral VEV",
    np.linalg.norm(annihilator_action) < TOL,
    detail=f"coefficients=(T3:{coeff[0]:.16g}, Y:{coeff[1]:.16g})",
)
ratio = ratio_from_stabilizer(vev_lower, y_h=1.0)
check(
    "E2 derived coefficient ratio is +1/2",
    abs(ratio.real - 0.5) < TOL and abs(ratio.imag) < TOL,
    detail=f"Y coefficient / T3 coefficient = {ratio:.16g}",
)


section("E3: unbroken Q and the three displayed broken directions")
Q = T3 + 0.5 * I2
Z = T3 - 0.5 * I2
check(
    "E3 Q = T3 + Y/2 annihilates the neutral VEV",
    np.linalg.norm(Q @ vev_lower) < TOL,
    detail=f"Q*vev={Q @ vev_lower}",
)
check(
    "E3 T1 action is the displayed nonzero upper-component vector",
    close(T1 @ vev_lower, np.array([0.5, 0], dtype=complex)),
    detail=f"T1*vev={T1 @ vev_lower}",
)
check(
    "E3 T2 action is the displayed nonzero imaginary upper-component vector",
    close(T2 @ vev_lower, np.array([-0.5j, 0], dtype=complex)),
    detail=f"T2*vev={T2 @ vev_lower}",
)
check(
    "E3 Z = T3 - Y/2 is broken on the neutral VEV",
    close(Z @ vev_lower, np.array([0, -1], dtype=complex)),
    detail=f"Z*vev={Z @ vev_lower}",
)


section("E4/E5: refutation and naming-convention legs")
y0_coeff, y0_singular_values, y0_rank = stabilizer_coefficients(vev_lower, y_h=0.0)
check(
    "E4 Y_H=0 stabilizer is T3-free",
    abs(y0_coeff[0]) < TOL and abs(y0_coeff[1]) > 1 - TOL,
    detail=(
        f"singular_values={y0_singular_values}, rank={y0_rank}, "
        f"coefficients=(T3:{y0_coeff[0]:.16g}, Y:{y0_coeff[1]:.16g})"
    ),
)
check(
    "E4 Y_H=0 gives no GMN mixing with T3",
    np.linalg.norm((y0_coeff[0] * T3 + y0_coeff[1] * 0.0 * I2) @ vev_lower) < TOL,
    detail="annihilator is the degenerate hypercharge-only direction a=0",
)
upper_ratio = ratio_from_stabilizer(vev_upper, y_h=1.0)
check(
    "E5 upper-component VEV derives coefficient -1/2",
    abs(upper_ratio.real + 0.5) < TOL and abs(upper_ratio.imag) < TOL,
    detail=f"Y coefficient / T3 coefficient = {upper_ratio:.16g}",
)


section("Displayed electric-charge table")
particles = [
    ("u_L", Fraction(1, 2), Fraction(1, 3), Fraction(2, 3)),
    ("d_L", Fraction(-1, 2), Fraction(1, 3), Fraction(-1, 3)),
    ("nu_L", Fraction(1, 2), Fraction(-1), Fraction(0)),
    ("e_L", Fraction(-1, 2), Fraction(-1), Fraction(-1)),
    ("u_R", Fraction(0), Fraction(4, 3), Fraction(2, 3)),
    ("d_R", Fraction(0), Fraction(-2, 3), Fraction(-1, 3)),
    ("e_R", Fraction(0), Fraction(-2), Fraction(-1)),
    ("nu_R", Fraction(0), Fraction(0), Fraction(0)),
    ("H+", Fraction(1, 2), Fraction(1), Fraction(1)),
    ("H0", Fraction(-1, 2), Fraction(1), Fraction(0)),
]
for name, t3_value, y_value, expected_q in particles:
    computed_q = t3_value + y_value / 2
    check(
        f"table row {name}: Q = T3 + Y/2",
        computed_q == expected_q,
        detail=(
            f"T3={frac_text(t3_value)}, Y={frac_text(y_value)}, "
            f"Q={frac_text(computed_q)}"
        ),
    )


section("E6: source-boundary firewall")
pinned_note_fragments = [
    (
        "status line",
        "**Status:** exact algebraic identity / support theorem on retained\n"
        "graph-first surface + cycle 15 (Y_H = +1) + standard SU(2) Lie algebra.\n"
        "NOT proposed_retained — see CLAIM_STATUS_CERTIFICATE.md.",
    ),
    (
        "authority role",
        "**Authority role:** exact-support theorem deriving the unbroken\n"
        "electromagnetic charge `Q = T_3 + Y/2` from the Higgs VEV and `Y_H = +1`.",
    ),
    ("boundary: VEV magnitude", "- The VEV `v` magnitude (admitted external observable)."),
    (
        "boundary: W/Z masses",
        "- The W/Z mass formulas (require Higgs kinetic term + EW mixing angle).",
    ),
    (
        "boundary: cycle-15 dependence",
        "- The retention of cycle 15 / Y_H = +1 derivation (still depends on\n"
        "  admitted SM Yukawa structure).",
    ),
    (
        "boundary: status yaml admission",
        "Conditional on cycle 15 (Y_H = +1) which is itself conditional on\n"
        "  admitted SM Yukawa structure. Higgs VEV neutral-component admission\n"
        "  is standard SSB convention, not derivation.",
    ),
]
for label, fragment in pinned_note_fragments:
    check(f"E6 pinned {label}", fragment in note_text)


print("\nSUMMARY: neutral-component EWSB algebra only; VEV convention and upstream Y_H remain source-bound.")
print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
sys.exit(1 if FAIL_COUNT else 0)
