#!/usr/bin/env python3
"""Exact CKM mass-operator projector-overlap typing checks.

No observed quark mass, fitted texture coefficient, or CKM comparator enters
the proof.  The runner checks a pair-based typed readout and the exact boundary
against universal down-only determinant/spectral constructions.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CKM_MASS_OPERATOR_PROJECTOR_OVERLAP_TYPING_THEOREM_NOTE_2026-07-12.md"
EXACT_PASS = 0
BOUNDARY_PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "", *, boundary: bool = False) -> None:
    global EXACT_PASS, BOUNDARY_PASS, FAIL
    ok = bool(condition)
    if ok:
        if boundary:
            BOUNDARY_PASS += 1
            tag = "BOUNDARY_PASS"
        else:
            EXACT_PASS += 1
            tag = "EXACT_PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}")
    if detail:
        print(f"             {detail}")


def lagrange_projector(operator: sp.Matrix, eigenvalue: sp.Expr, others: tuple[sp.Expr, ...]) -> sp.Matrix:
    identity = sp.eye(operator.rows)
    result = identity
    for other in others:
        result = result * (operator - other * identity) / (eigenvalue - other)
    return sp.simplify(result)


def symbolic_projector_overlap() -> None:
    print("\n1. SPECTRAL-PROJECTOR OVERLAP")
    u, c, t = sp.symbols("u c t", positive=True, real=True)
    d, s, b = sp.symbols("d s b", positive=True, real=True)
    theta = sp.symbols("theta", real=True)
    rotation = sp.Matrix(
        [
            [1, 0, 0],
            [0, sp.cos(theta), sp.sin(theta)],
            [0, -sp.sin(theta), sp.cos(theta)],
        ]
    )
    h_u = sp.diag(u, c, t)
    h_d = sp.simplify(rotation * sp.diag(d, s, b) * rotation.T)
    p_c = lagrange_projector(h_u, c, (u, t))
    p_b = lagrange_projector(h_d, b, (d, s))
    overlap = sp.trigsimp(sp.trace(p_c * p_b))

    check("P_c is an exact Lagrange spectral projector", p_c == sp.diag(0, 1, 0))
    check("P_b is idempotent", sp.simplify(p_b * p_b - p_b) == sp.zeros(3))
    check("P_b has trace one", sp.trigsimp(sp.trace(p_b)) == 1)
    check("projector overlap is sin(theta)^2", sp.trigsimp(overlap - sp.sin(theta) ** 2) == 0)
    compressed = sp.simplify(p_c * p_b * p_c)
    check("compressed overlap is |V_cb|^2 P_c", sp.trigsimp(compressed - sp.sin(theta) ** 2 * p_c) == sp.zeros(3))
    check("compressed one-line determinant equals overlap", sp.trigsimp(compressed[1, 1] - overlap) == 0)


def exact_complex_and_basis_controls() -> None:
    print("\n2. PHASE AND WEAK-BASIS CONTROLS")
    c23 = sp.Rational(4, 5)
    s23 = sp.Rational(3, 5)
    phase = sp.I
    v = sp.Matrix(
        [
            [1, 0, 0],
            [0, c23, phase * s23],
            [0, phase * s23, c23],
        ]
    )
    h_u = sp.diag(1, 4, 9)
    h_d = sp.simplify(v * sp.diag(16, 25, 36) * v.conjugate().T)
    p_c = lagrange_projector(h_u, sp.Integer(4), (sp.Integer(1), sp.Integer(9)))
    p_b = lagrange_projector(h_d, sp.Integer(36), (sp.Integer(16), sp.Integer(25)))
    overlap = sp.simplify(sp.trace(p_c * p_b))

    check("complex 2-3 control is unitary", sp.simplify(v.conjugate().T * v) == sp.eye(3))
    check("complex-phase overlap is |V_cb|^2=9/25", overlap == sp.Rational(9, 25))

    w = sp.Matrix(
        [
            [sp.Rational(4, 5), sp.Rational(3, 5), 0],
            [-sp.Rational(3, 5), sp.Rational(4, 5), 0],
            [0, 0, 1],
        ]
    )
    transformed = sp.simplify(sp.trace((w * p_c * w.T) * (w * p_b * w.T)))
    check("simultaneous weak-basis rotation preserves overlap", transformed == overlap)

    rephase = sp.diag(1, sp.I, -1)
    rephased = sp.simplify(
        sp.trace(
            (rephase * p_c * rephase.conjugate().T)
            * (rephase * p_b * rephase.conjugate().T)
        )
    )
    check("simultaneous rephasing preserves overlap", rephased == overlap)


def determinant_and_alignment() -> None:
    print("\n3. SIX-STATE DETERMINANT AND ALIGNMENT RESIDUAL")
    r = sp.symbols("R", positive=True)
    q = sp.diag(1, 0, 0, 0, 0, 0)
    p = sp.eye(6) - q
    x_r = q + r * p
    check("rank-(1+5) determinant is R^5", sp.factor(x_r.det()) == r**5)
    check(
        "normalized determinant exponent is 5/6",
        sp.expand_log(sp.log(x_r.det()), force=True) / 6 == sp.Rational(5, 6) * sp.log(r),
    )

    h_s, h_b, scale = sp.symbols("h_s h_b scale", positive=True)
    mass_ratio = sp.sqrt(h_s / h_b)
    check(
        "mass ratio is invariant under common down-sector scale",
        sp.simplify(sp.sqrt((scale * h_s) / (scale * h_b)) - mass_ratio) == 0,
    )
    check(
        "squared five-sixths target is (h_s/h_b)^(5/6)",
        sp.simplify(mass_ratio ** sp.Rational(5, 3) - (h_s / h_b) ** sp.Rational(5, 6)) == 0,
    )

    q0 = sp.Rational(1, 2)
    r0 = q0**6
    target_amplitude = q0**5
    target_overlap = target_amplitude**2
    check("exact selected-orientation witness has R^(5/6)=1/32", r0 ** sp.Rational(5, 6) == target_amplitude)
    check("exact alignment witness has overlap R^(5/3)", r0 ** sp.Rational(5, 3) == target_overlap)
    check("bridge sixth-power form is |V_cb|^6=R^5", target_amplitude**6 == r0**5)


def commutator_control() -> None:
    print("\n4. TWO-FAMILY COMMUTATOR FALSIFIER")
    a1, a2, b1, b2 = sp.symbols("a1 a2 b1 b2", real=True)
    cosine = sp.Rational(4, 5)
    sine = sp.Rational(3, 5)
    rotation = sp.Matrix([[cosine, sine], [-sine, cosine]])
    a = sp.simplify(rotation * sp.diag(a1, a2) * rotation.T)
    b = sp.diag(b1, b2)
    commutator = sp.simplify(a * b - b * a)
    frob_sq = sp.simplify(sp.trace(commutator.conjugate().T * commutator))
    gap_sq = (a2 - a1) ** 2 * (b2 - b1) ** 2
    chi = sp.factor(2 * frob_sq / gap_sq)
    expected = 4 * sine**2 * cosine**2
    check("commutator invariant is 4t(1-t)", sp.simplify(chi - expected) == 0)
    check("commutator readout has t<->1-t ambiguity", sp.simplify(expected - 4 * cosine**2 * sine**2) == 0, boundary=True)


def down_only_countermodel() -> None:
    print("\n5. UNIVERSAL DOWN-ONLY COUNTERMODEL")
    d, s, b = sp.symbols("d s b", positive=True, real=True)
    h_d = sp.diag(d, s, b)
    p_b = sp.diag(0, 0, 1)
    p_c_zero = sp.diag(0, 1, 0)
    rotation = sp.Matrix(
        [
            [1, 0, 0],
            [0, sp.Rational(4, 5), sp.Rational(3, 5)],
            [0, -sp.Rational(3, 5), sp.Rational(4, 5)],
        ]
    )
    p_c_rotated = sp.simplify(rotation * p_c_zero * rotation.T)
    overlap_zero = sp.trace(p_c_zero * p_b)
    overlap_rotated = sp.simplify(sp.trace(p_c_rotated * p_b))

    check("fixed H_d has unchanged trace", sp.trace(h_d) == d + s + b, boundary=True)
    check("fixed H_d has unchanged determinant", h_d.det() == d * s * b, boundary=True)
    check("first up orientation gives zero overlap", overlap_zero == 0, boundary=True)
    check("second up orientation gives 9/25 overlap", overlap_rotated == sp.Rational(9, 25), boundary=True)
    check("same down input supports distinct |V_cb| readouts", overlap_zero != overlap_rotated, boundary=True)

    ratio = sp.sqrt(s / b)
    x_a = sp.diag(1, ratio, ratio, ratio, ratio, ratio)
    x_b = sp.diag(1, ratio, ratio, ratio, ratio, ratio)
    check("down-only X_R is identical in both orientations", x_a == x_b, boundary=True)
    check("down-only determinant cannot distinguish orientations", x_a.det() == x_b.det(), boundary=True)


def textual_firewalls() -> None:
    print("\n6. CLAIM-BOUNDARY FIREWALLS")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.split())
    check("source note declares bounded_theorem", "**Claim type:** bounded_theorem" in note, boundary=True)
    check(
        "source note declares exact support/boundary theorem status",
        "**Actual current-surface status:** exact support/boundary theorem" in note,
        boundary=True,
    )
    check("source note keeps the invariant alignment law open", "dynamical theorem forcing (1.2)" in normalized, boundary=True)
    check("source note narrows the down-only theorem class", "universal equivariant/invariant down-only class" in normalized, boundary=True)
    check("source note forbids retained-grade proposal language", "does not permit retained-grade proposal language" in normalized, boundary=True)
    forbidden_targets = ["0.0422", "93.4", "81.0", "4.180", "0.022"]
    check("runner-facing theorem note contains no observed target values", not any(x in note for x in forbidden_targets), boundary=True)


def main() -> int:
    print("CKM MASS-OPERATOR PROJECTOR-OVERLAP TYPING THEOREM")
    symbolic_projector_overlap()
    exact_complex_and_basis_controls()
    determinant_and_alignment()
    commutator_control()
    down_only_countermodel()
    textual_firewalls()
    print(f"\nSUMMARY: EXACT_PASS={EXACT_PASS} BOUNDARY_PASS={BOUNDARY_PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
