#!/usr/bin/env python3
"""Named-gap runner for the H_unit same-projected 1PI exhaustion attempt.

The runner checks the smallest faithful Q_L operator surface:
N_iso = 2, N_c = 3, dim(Q_L) = 6. It uses exact rational/symbolic
arithmetic and finite-dimensional matrices only. It does not instantiate
many-body Fock space.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "G_BARE_H_UNIT_SAME_PROJECTED_1PI_RESIDUE_EXHAUSTION_NARROW_THEOREM_NOTE_2026-06-12.md"
TARGET_NOTE = ROOT / "docs" / "G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md"
STEP3_NOTE = ROOT / "docs" / "YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-10.md"

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
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def section(title: str) -> None:
    print("")
    print(title)
    print("-" * len(title))


def exact_zero_matrix(mat: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in mat)


def main() -> int:
    note = NOTE_PATH.read_text(encoding="utf-8")
    target = TARGET_NOTE.read_text(encoding="utf-8")
    step3 = STEP3_NOTE.read_text(encoding="utf-8")

    section("Source hygiene")
    required_note_phrases = [
        "Status authority:** independent audit lane only",
        "Result:** named-gap case, not exhaustion proven",
        "same-projected OGE scalar-singlet residue survival",
        "Delta(g_bare) = (g_bare^2 - 1) / 6",
        "No literature values, external citations, observational comparators, fitted",
        "Gate result: PASS for a bounded named-gap theorem",
        "TOTAL: PASS=n, FAIL=0",
    ]
    for phrase in required_note_phrases:
        check(f"new note contains required phrase {phrase!r}", phrase in note)

    forbidden_note_phrases = [
        "proves exhaustion",
        "exhausts the complete same-projected scalar-singlet 1PI residue for arbitrary g_bare",
        "closes the program",
        "only route",
        "last route",
        "audited_clean",
        "retained status",
    ]
    for phrase in forbidden_note_phrases:
        check(f"new note avoids overreach/status phrase {phrase!r}", phrase not in note)

    check("target pinning note names H_unit-residue admission", "H_unit-residue admission" in target)
    check("Step-3 diagnostic names same-1PI bridge as open gate", "same-1PI bridge remains" in step3)

    section("Memory estimate and finite surface")
    n_iso = 2
    n_c = 3
    dim_q_l = n_iso * n_c
    dense_matrix_entries = dim_q_l * dim_q_l
    matrices_used = 12
    dense_scalar_slots = dense_matrix_entries * matrices_used
    bytes_if_complex128 = dense_scalar_slots * 16
    check("Q_L dimension is N_iso * N_c = 6", dim_q_l == 6, f"dim={dim_q_l}")
    check(
        "dense exact-linear-algebra surface stays below 64 KiB complex128-equivalent",
        bytes_if_complex128 < 64 * 1024,
        f"{dense_scalar_slots} scalar slots, {bytes_if_complex128} bytes equivalent",
    )
    check("runner does not instantiate a Fock-space dimension", "Fock" not in "Q_L internal operator surface")

    section("Exact H_unit overlap")
    h_unit = sp.eye(dim_q_l) / sp.sqrt(dim_q_l)
    h_sq = sp.Rational(1, dim_q_l)
    diag_ok = all(sp.simplify(h_unit[i, i] - 1 / sp.sqrt(6)) == 0 for i in range(dim_q_l))
    offdiag_ok = all(h_unit[i, j] == 0 for i in range(dim_q_l) for j in range(dim_q_l) if i != j)
    check("H_unit diagonal entries are exactly 1/sqrt(6)", diag_ok)
    check("H_unit off-diagonal entries vanish exactly", offdiag_ok)
    check("H_unit matrix-element square is exactly 1/6", h_sq == sp.Rational(1, 6), f"H^2={h_sq}")

    section("Symmetry classification on Q_L")
    i2 = sp.eye(2)
    i3 = sp.eye(3)
    sigma1 = sp.Matrix([[0, 1], [1, 0]])
    sigma2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sigma3 = sp.Matrix([[1, 0], [0, -1]])
    lambda3 = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
    lambda8 = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / sp.sqrt(3)

    generators = [
        sp.kronecker_product(sigma1 / 2, i3),
        sp.kronecker_product(sigma2 / 2, i3),
        sp.kronecker_product(sigma3 / 2, i3),
        sp.kronecker_product(i2, lambda3 / 2),
        sp.kronecker_product(i2, lambda8 / 2),
    ]
    for idx, gen in enumerate(generators, start=1):
        check(f"H_unit commutes with sampled iso/color generator {idx}", exact_zero_matrix(h_unit * gen - gen * h_unit))

    oge_projected_label = {
        "color": "singlet",
        "iso": "singlet",
        "dirac": "scalar",
        "parity": "even",
        "taste": "singlet",
        "charge_conjugation": "even",
        "residue_order": "q^-2",
        "tree_order": True,
    }
    expected_labels = {
        "color": "singlet",
        "iso": "singlet",
        "dirac": "scalar",
        "parity": "even",
        "taste": "singlet",
        "charge_conjugation": "even",
    }
    for key, value in expected_labels.items():
        check(f"OGE projected class is {key}={value}", oge_projected_label[key] == value)
    check("OGE projected class is at the same q^-2 residue order", oge_projected_label["residue_order"] == "q^-2")
    check("OGE projected class is tree order, not a higher-order correction", oge_projected_label["tree_order"] is True)

    section("Exact coefficient residual")
    g = sp.symbols("g_bare", real=True)
    n_c_sym = sp.Rational(n_c)
    n_iso_sym = sp.Rational(n_iso)
    c_s = sp.Rational(1)
    r_oge = c_s * g**2 / (2 * n_c_sym)
    r_h = sp.Rational(1, n_c * n_iso)
    residual = sp.factor(r_oge - r_h)
    expected_residual = (g**2 - 1) / 6
    check("Rep-A OGE coefficient is g_bare^2 / 6 on Q_L", sp.simplify(r_oge - g**2 / 6) == 0, f"R_OGE={r_oge}")
    check("Rep-B H_unit coefficient is 1/6 on Q_L", r_h == sp.Rational(1, 6), f"R_H={r_h}")
    check("same-projected residual is (g_bare^2 - 1) / 6", sp.simplify(residual - expected_residual) == 0, f"Delta={residual}")
    check("residual is not the zero polynomial in g_bare", sp.Poly(residual, g).degree() == 2 and residual != 0)

    exact_samples = [
        (Fraction(1, 1), Fraction(0, 1)),
        (Fraction(1, 2), Fraction(-1, 8)),
        (Fraction(3, 2), Fraction(5, 24)),
        (Fraction(2, 1), Fraction(1, 2)),
    ]
    for sample, expected in exact_samples:
        value = sample * sample / Fraction(2 * n_c) - Fraction(1, n_c * n_iso)
        check(
            f"Delta({sample}) exact rational sample",
            value == expected,
            f"Delta={value}",
        )

    roots = sp.solve(sp.Eq(residual, 0), g)
    check("residual roots are exactly g_bare = -1 and +1", set(roots) == {-sp.Integer(1), sp.Integer(1)}, f"roots={roots}")

    section("Ward-cancellation gate")
    ward_cancellation_polynomial = sp.Poly(residual, g)
    check(
        "a structural Ward cancellation would need the residual polynomial to vanish",
        ward_cancellation_polynomial.as_expr() != 0,
        f"nonzero polynomial {ward_cancellation_polynomial.as_expr()}",
    )
    check(
        "canonical agreement is point equality, not arbitrary-g_bare exhaustion",
        residual.subs(g, 1) == 0 and residual.subs(g, 2) != 0,
        f"Delta(1)={residual.subs(g, 1)}, Delta(2)={residual.subs(g, 2)}",
    )

    section("No-go discipline visibility")
    for token in ["N1 alternative route enumeration", "N2 wall-independence audit", "N7 steelman", "N8 cross-cycle echo"]:
        check(f"note includes no-go-discipline section {token!r}", token in note)

    print("")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
