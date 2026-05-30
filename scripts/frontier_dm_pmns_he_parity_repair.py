#!/usr/bin/env python3
"""Fixed-chart Hermitian-block parity repair runner for the DM/PMNS row."""

from __future__ import annotations

import cmath
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "DM_LEPTOGENESIS_PMNS_ANALYTIC_STATIONARY_CLASSIFICATION_THEOREM_NOTE_2026-04-16.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def check_note_boundary() -> None:
    section("Source-note boundary")
    text = NOTE_PATH.read_text()
    normalized = " ".join(text.split())
    required = [
        "bounded-support formal matrix algebra",
        "That fixed-chart Hermitian-block formula and conjugation parity are the entire repaired theorem.",
        "This repair withdraws that selector conclusion from the binding claim.",
        "The bridge from this fixed-chart parity algebra to the full PMNS-assisted leptogenesis selector remains a separate open science problem.",
    ]
    for needle in required:
        check(f"note contains required boundary: {needle!r}", needle in normalized)

    forbidden = [
        "relative-action selector is derived",
        "KKT branch classification is derived",
        "favored-column closure is derived",
        "eta normalization is derived",
        "stationary-branch minimality is proved",
    ]
    for needle in forbidden:
        check(f"note avoids overclaim phrase: {needle!r}", needle not in normalized)


def symbolic_matrices():
    x1, x2, x3, y1, y2, y3, delta = sp.symbols("x1 x2 x3 y1 y2 y3 delta", real=True)
    exp_pos = sp.exp(sp.I * delta)
    exp_neg = sp.exp(-sp.I * delta)
    y = sp.Matrix(
        [
            [x1, y1, 0],
            [0, x2, y2],
            [y3 * exp_pos, 0, x3],
        ]
    )
    h = sp.simplify(y * y.conjugate().T)
    expected = sp.Matrix(
        [
            [x1**2 + y1**2, x2 * y1, x1 * y3 * exp_neg],
            [x2 * y1, x2**2 + y2**2, x3 * y2],
            [x1 * y3 * exp_pos, x3 * y2, x3**2 + y3**2],
        ]
    )
    return delta, h, expected


def matrix_zero(mat: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in mat)


def check_symbolic_formula_and_parity() -> None:
    section("Symbolic formula and parity")
    delta, h, expected = symbolic_matrices()
    check("direct multiplication gives displayed H_e entries", matrix_zero(h - expected))
    check("H_e is Hermitian", matrix_zero(h - h.conjugate().T))
    h_neg = h.subs(delta, -delta)
    check("H_e(-delta) is entrywise conjugate of H_e(delta)", matrix_zero(h_neg - h.conjugate()))

    trace = sp.simplify(h.trace())
    trace2 = sp.simplify((h * h).trace())
    det = sp.simplify(h.det())
    charpoly_coeffs = [sp.simplify(c) for c in h.charpoly().all_coeffs()]
    check("trace is even in delta", sp.simplify(trace.subs(delta, -delta) - trace) == 0)
    check("trace square is even in delta", sp.simplify(trace2.subs(delta, -delta) - trace2) == 0)
    check("determinant is even in delta", sp.simplify(det.subs(delta, -delta) - det) == 0)
    for idx, coeff in enumerate(charpoly_coeffs):
        check(f"characteristic coefficient {idx} is even in delta", sp.simplify(coeff.subs(delta, -delta) - coeff) == 0)


def determinant_3x3(m: list[list[complex]]) -> complex:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def numeric_h(x: tuple[float, float, float], y: tuple[float, float, float], delta: float) -> list[list[complex]]:
    x1, x2, x3 = x
    y1, y2, y3 = y
    return [
        [x1 * x1 + y1 * y1, x2 * y1, x1 * y3 * cmath.exp(-1j * delta)],
        [x2 * y1, x2 * x2 + y2 * y2, x3 * y2],
        [x1 * y3 * cmath.exp(1j * delta), x3 * y2, x3 * x3 + y3 * y3],
    ]


def max_abs_diff(a: list[list[complex]], b: list[list[complex]]) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(3) for j in range(3))


def conjugate_matrix(a: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j].conjugate() for j in range(3)] for i in range(3)]


def frobenius_sq(a: list[list[complex]]) -> float:
    return float(sum(abs(a[i][j]) ** 2 for i in range(3) for j in range(3)))


def check_numeric_samples() -> None:
    section("Numeric parity samples")
    samples = [
        ((0.4, 0.6, 0.7), (0.2, 0.3, 0.5), 0.37),
        ((1.0, -0.2, 0.9), (0.8, 0.1, -0.4), 1.2),
        ((-0.5, 0.25, 0.75), (0.6, -0.3, 0.2), -0.9),
    ]
    for idx, (x, y, delta) in enumerate(samples):
        h = numeric_h(x, y, delta)
        h_neg = numeric_h(x, y, -delta)
        conj = conjugate_matrix(h)
        check(f"sample {idx}: H(-delta) equals conjugate H(delta)", max_abs_diff(h_neg, conj) < 1e-12)
        tr = sum(h[i][i] for i in range(3))
        tr_neg = sum(h_neg[i][i] for i in range(3))
        det = determinant_3x3(h)
        det_neg = determinant_3x3(h_neg)
        check(f"sample {idx}: trace parity", abs(tr_neg - tr.conjugate()) < 1e-12)
        check(f"sample {idx}: determinant parity", abs(det_neg - det.conjugate()) < 1e-10)
        check(f"sample {idx}: Frobenius norm parity", abs(frobenius_sq(h_neg) - frobenius_sq(h)) < 1e-12)


def check_negative_controls() -> None:
    section("Negative controls")
    x = (0.4, 0.6, 0.7)
    y = (0.2, 0.3, 0.5)
    delta = 0.37
    h = numeric_h(x, y, delta)
    h_neg = numeric_h(x, y, -delta)
    phase_sensitive = h[0][2].imag
    phase_sensitive_neg = h_neg[0][2].imag
    check("phase-sensitive entry is not even by itself", abs(phase_sensitive_neg - phase_sensitive) > 1e-6)
    check("phase-sensitive entry is odd under sign flip", abs(phase_sensitive_neg + phase_sensitive) < 1e-12)


def main() -> int:
    print("DM/PMNS fixed-chart Hermitian-block parity repair")
    check_note_boundary()
    check_symbolic_formula_and_parity()
    check_numeric_samples()
    check_negative_controls()
    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
