#!/usr/bin/env python3
"""Exact checks for the neutrino Γ₁ W-source application bridge."""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

try:
    import sympy
    from sympy import Abs, Matrix, Rational, eye, log, simplify, sqrt, symbols, zeros
except ImportError:
    print("[FAIL] sympy is required")
    print("TOTAL: PASS=0 FAIL=1")
    print("VERDICT: FAIL")
    sys.exit(1)


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
    print(f"[{tag}] {label}{suffix}")


def matrix_eq(left: Matrix, right: Matrix) -> bool:
    if left.shape != right.shape:
        return False
    return all(simplify(value) == 0 for value in left - right)


def kron(*mats: Matrix) -> Matrix:
    """Iterated sympy Kronecker product."""
    out = mats[0]
    for m in mats[1:]:
        out = sympy.kronecker_product(out, m)
    return out


def construction() -> tuple[Matrix, Matrix, Matrix, Matrix]:
    I2 = eye(2)
    SX = Matrix([[0, 1], [1, 0]])
    SZ = Matrix([[1, 0], [0, -1]])

    G0 = kron(SZ, SZ, SZ, SX)
    G1 = kron(SX, I2, I2, I2)
    G2 = kron(SZ, SX, I2, I2)
    G3 = kron(SZ, SZ, SX, I2)
    I16 = eye(16)

    GAMMA5 = G0 * G1 * G2 * G3
    # GAMMA5 is Hermitian and involutive and anticommutes with G0..G3.

    # Chiral projectors
    P_L = (I16 + GAMMA5) / 2
    P_R = (I16 - GAMMA5) / 2

    Y = P_R * G1 * P_L
    Y_dag = Y.H

    return I16, GAMMA5, G1, Y


def numeric_determinant(matrix: Matrix) -> float:
    return float(sympy.N(matrix.det(), 30))


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    observable_path = root / "docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md"
    companion_path = root / (
        "scripts/audit_companion_dm_neutrino_bosonic_normalization_"
        "observable_principle_bridge_exact_2026_05_16.py"
    )
    note_path = root / (
        "docs/NEUTRINO_GAMMA1_WSOURCE_APPLICATION_BRIDGE_NOTE_2026-07-09.md"
    )

    observable_text = observable_path.read_text(encoding="utf-8")
    observable_flat = " ".join(observable_text.split())
    companion_text = companion_path.read_text(encoding="utf-8") if companion_path.exists() else ""
    companion_flat = " ".join(companion_text.split())
    note_text = note_path.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())

    print("Group A — source needles")
    check(
        "A1 W definition source needle",
        "W[J] = log |det(D+J)| - log |det D|" in observable_flat,
    )
    check(
        "A2 additivity source needle",
        "W[J_1 ⊕ J_2] = W[J_1] + W[J_2]" in observable_flat,
    )
    check(
        "A3 construction-source drift detector",
        companion_path.exists()
        and "Y = P_R" in companion_flat
        and "Γ_1 = Y + Y^†" in companion_flat,
    )
    check(
        "A4 premise labels and observable-principle edge",
        all(
            needle in note_flat
            for needle in (
                "P1",
                "P2",
                "readout-identification admission",
                "](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)",
            )
        ),
    )
    link_targets = re.findall(r"\]\(([^)]+)\)", note_text)
    expected_header_targets = {
        "../scripts/frontier_neutrino_gamma1_wsource_application_bridge_2026_07_09.py",
        "../logs/runner-cache/frontier_neutrino_gamma1_wsource_application_bridge_2026_07_09.txt",
    }
    allowed_targets = expected_header_targets | {"OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md"}
    check(
        "A5 markdown-link hygiene",
        set(link_targets) <= allowed_targets
        and expected_header_targets <= set(link_targets)
        and all(
            target == "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md"
            for target in link_targets
            if target.endswith(".md")
        ),
        detail=f"targets={link_targets}",
    )

    I16, gamma_5, Gamma_1, Y = construction()
    zero16 = zeros(16, 16)

    print("Group B — construction")
    check("B1 Y**2 == 0", matrix_eq(Y**2, zero16))
    check(
        "B2 Hermitian completion",
        matrix_eq(Gamma_1, Y + Y.H) and matrix_eq(Gamma_1.H, Gamma_1),
    )
    check(
        "B3 {gamma_5, Gamma_1} == 0",
        matrix_eq(gamma_5 * Gamma_1 + Gamma_1 * gamma_5, zero16),
    )
    trace_gamma = simplify((Gamma_1.H * Gamma_1).trace())
    trace_y = simplify((Y.H * Y).trace())
    check(
        "B4 exact trace norms",
        trace_gamma == 16 and trace_y == 8,
        detail=f"Tr(Gamma_1.H*Gamma_1)={trace_gamma}, Tr(Y.H*Y)={trace_y}",
    )

    m = symbols("m", positive=True)
    j = symbols("j", real=True)
    det_y = sympy.factor((m * I16 + j * Y).det())
    det_gamma = sympy.factor((m * I16 + j * Gamma_1).det())

    print("Group C — W identities")
    check("C1 det(mI+jY) == m**16", simplify(det_y - m**16) == 0)
    check(
        "C2 det(mI+jGamma_1) == (m**2-j**2)**8",
        simplify(det_gamma - (m**2 - j**2) ** 8) == 0,
    )
    check(
        "C3 eigenvalue multiset",
        Gamma_1.eigenvals() == {sympy.Integer(1): 8, sympy.Integer(-1): 8},
        detail=f"eigenvals={Gamma_1.eigenvals()}",
    )

    m0 = Rational(3)
    j0 = Rational(1, 2)
    source0 = m0 * I16 + j0 * Gamma_1
    base0 = m0 * I16
    w0 = log(source0.det()) - log(base0.det())
    w0_expected = 8 * log(1 - j0**2 / m0**2)
    check(
        "C4 exact-rational W identity",
        simplify(sympy.expand_log(w0 - w0_expected, force=True)) == 0,
        detail=f"m={m0}, j={j0}",
    )

    joint_source = sympy.diag(m * I16 + j * Gamma_1, m * I16 + j * Gamma_1)
    joint_base = sympy.diag(m * I16, m * I16)
    det_joint = sympy.factor(joint_source.det())
    det_joint_base = sympy.factor(joint_base.det())
    w_single_symbolic = log(Abs(det_gamma)) - log(Abs(m**16))
    w_joint_symbolic = log(Abs(det_joint)) - log(Abs(det_joint_base))
    check(
        "C5 direct-sum W additivity",
        simplify(det_joint - det_gamma**2) == 0
        and simplify(det_joint_base - m**32) == 0
        and simplify(
            sympy.expand_log(w_joint_symbolic - 2 * w_single_symbolic, force=True)
        )
        == 0,
    )

    print("Group D — quadratic response and normalization")
    w_symbolic = log(det_gamma)
    w_second_at_zero = simplify(sympy.diff(w_symbolic, j, 2).subs(j, 0))
    check(
        "D1 exact symbolic second response",
        simplify(w_second_at_zero + 16 / m**2) == 0,
        detail=f"W''(0)={w_second_at_zero}",
    )

    m_float = 1.0
    base_float = numeric_determinant(m_float * I16)

    def numeric_w(j_float: float) -> float:
        source = m_float * I16 + sympy.Float(j_float, 30) * Gamma_1
        return math.log(abs(numeric_determinant(source))) - math.log(abs(base_float))

    hs = [0.02, 0.01, 0.005, 0.0025]
    fd_values = [
        (numeric_w(h) - 2.0 * numeric_w(0.0) + numeric_w(-h)) / (h * h)
        for h in hs
    ]
    errors = [abs(value + 16.0) for value in fd_values]
    ratios = [errors[index] / errors[index + 1] for index in range(len(errors) - 1)]
    consecutive = any(
        3.5 <= ratios[index] <= 4.5 and 3.5 <= ratios[index + 1] <= 4.5
        for index in range(len(ratios) - 1)
    )
    check(
        "D2 finite-difference Richardson convergence",
        consecutive,
        detail=f"values={fd_values}, error-ratios={ratios}",
    )

    response_coefficient = simplify((-m**2 * w_second_at_zero) / 16)
    trace_coefficient = simplify(trace_gamma / 16)
    check(
        "D3 per-mode identity chain",
        response_coefficient == trace_coefficient == 1,
        detail=f"response={response_coefficient}, trace={trace_coefficient}",
    )
    chiral_ratio = simplify(trace_y / trace_gamma)
    hs_ratio = simplify(sqrt(chiral_ratio))
    check(
        "D4 chiral-half and HS-norm ratios",
        chiral_ratio == Rational(1, 2)
        and simplify(hs_ratio - 1 / sqrt(2)) == 0,
        detail=f"trace-ratio={chiral_ratio}, HS-ratio={hs_ratio}",
    )

    print("Group E — REJECTORS")
    E = zeros(16, 16)
    E[0, 0] = 1
    Y_bad = Y + Rational(1, 7) * E
    det_y_bad = sympy.factor((m * I16 + j * Y_bad).det())
    check(
        "E1 non-nilpotent perturbation breaks selection",
        not matrix_eq(Y_bad**2, zero16) and simplify(det_y_bad - m**16) != 0,
        detail=f"det difference={simplify(det_y_bad - m**16)}",
    )

    det_rescaled = sympy.factor((m * I16 + j * (2 * Gamma_1)).det())
    w_rescaled_second = simplify(sympy.diff(log(det_rescaled), j, 2).subs(j, 0))
    rescaled_coefficient = simplify((-m**2 * w_rescaled_second) / 16)
    check(
        "E2 rescaled-source normalization discriminator",
        rescaled_coefficient == 4 and rescaled_coefficient != 1,
        detail=f"coefficient={rescaled_coefficient}",
    )

    X = Matrix.vstack(
        Matrix.hstack(Gamma_1, I16),
        Matrix.hstack(I16, Gamma_1),
    )
    source_x = m0 * eye(32) + j0 * X
    base_x = m0 * eye(32)
    ratio_x = simplify(source_x.det() / base_x.det())
    ratio_direct_sum = simplify((source0.det() / base0.det()) ** 2)
    w_x = log(ratio_x)
    w_direct_sum = 2 * log(source0.det() / base0.det())
    check(
        "E3 cross-block coupling breaks direct-sum additivity",
        ratio_x > 0
        and ratio_direct_sum > 0
        and ratio_x != ratio_direct_sum
        and simplify(w_x - w_direct_sum) != 0,
        detail=f"exp(W_X)={ratio_x}, exp(2W)={ratio_direct_sum}",
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("VERDICT: PASS" if FAIL == 0 else "VERDICT: FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
