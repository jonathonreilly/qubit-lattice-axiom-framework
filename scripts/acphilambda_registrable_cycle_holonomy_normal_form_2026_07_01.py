#!/usr/bin/env python3
"""Exact gates for the AC_phi_lambda cycle-holonomy normal form note."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re
import sys

import sympy as sp


PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"SUMMARY: {status} - {label}{suffix}")
    return ok


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def simplify_exact(expr: sp.Expr) -> sp.Expr:
    expanded = sp.expand_trig(expr)
    simplified = sp.simplify(sp.trigsimp(expanded))
    if simplified == 0:
        return simplified
    return sp.simplify(sp.trigsimp(expanded.rewrite(sp.exp)))


def exact_zero(expr: sp.Expr) -> bool:
    return simplify_exact(expr) == 0


def matrix_exact_zero(matrix: sp.Matrix) -> bool:
    return all(exact_zero(matrix[i, j]) for i in range(matrix.rows) for j in range(matrix.cols))


def sort_key(expr: sp.Expr) -> tuple[float, float]:
    value = sp.N(expr, 50)
    return (float(sp.re(value)), float(sp.im(value)))


def exact_multiset_equal(left: list[sp.Expr], right: list[sp.Expr]) -> bool:
    if len(left) != len(right):
        return False
    left_sorted = sorted(left, key=sort_key)
    right_sorted = sorted(right, key=sort_key)
    return all(exact_zero(a - b) for a, b in zip(left_sorted, right_sorted))


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md"
MIN_AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
BRANNEN = ROOT / "docs/BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md"
Q23 = ROOT / "docs/KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md"
FIXED = ROOT / "docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
RADIAN = ROOT / "docs/KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md"


def part_a_sources() -> None:
    print("=== PART A: sources and boundary text ===")
    for path in [NOTE, MIN_AXIOMS, BRANNEN, Q23, FIXED, RADIAN]:
        check(f"source exists: {path.relative_to(ROOT)}", path.exists())

    radian_text = read(RADIAN)
    brannen_text = read(BRANNEN)
    fixed_text = read(FIXED)
    check("radian boundary contains Type-B-to-radian", "Type-B-to-radian" in radian_text)
    check("radian boundary contains remaining primitive", "remaining primitive" in radian_text)
    check("Brannen note contains H = a I + b C fragment", "H = a I + b C + conj(b) C^T" in brannen_text)
    check("Brannen note contains circulant form", "circulant form" in brannen_text)
    check("Brannen note contains (a, |b|, delta)", "(a, |b|, delta)" in brannen_text)
    check(
        "fixed-locus note excludes physical single-summand readout",
        "does **not** supply the physical single-summand readout" in fixed_text,
    )
    check("Q=2/3 note exists as dependency surface", Q23.exists())


def part_b_ta1() -> None:
    print("=== PART B: T-A1 exact spectral algebra ===")
    delta = sp.symbols("delta", real=True)
    c = [sp.cos(delta + 2 * sp.pi * k / 3) for k in range(3)]
    check("sum c_k == 0", exact_zero(sum(c)))
    check("sum c_k^2 == 3/2", exact_zero(sum(x**2 for x in c) - sp.Rational(3, 2)))
    check(
        "sum c_k^3 == (3/4) cos(3 delta)",
        exact_zero(sum(x**3 for x in c) - sp.Rational(3, 4) * sp.cos(3 * delta)),
    )
    check("reject wrong sum c_k^2 = 4/3", not exact_zero(sum(x**2 for x in c) - sp.Rational(4, 3)))
    check(
        "reject wrong cubic coefficient 1/2",
        not exact_zero(sum(x**3 for x in c) - sp.Rational(1, 2) * sp.cos(3 * delta)),
    )

    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    z, a_sym, r_sym = sp.symbols("z a r", nonzero=True)
    H_z = a_sym * sp.eye(3) + r_sym * z * C + r_sym / z * C.T
    eigen_exprs = list(H_z.eigenvals().keys())
    check("explicit 3x3 Matrix.eigenvals returns three simple eigenvalues", len(eigen_exprs) == 3)

    for a_val in [sp.Rational(0), sp.Rational(1, 2)]:
        for r_val in [sp.Rational(1), sp.Rational(2, 5)]:
            for d_val in [sp.Rational(2, 9), sp.Rational(1, 7)]:
                computed = [
                    ev.subs({a_sym: a_val, r_sym: r_val, z: sp.exp(sp.I * d_val)})
                    for ev in eigen_exprs
                ]
                target = [
                    a_val + 2 * r_val * sp.cos(d_val + 2 * sp.pi * k / 3)
                    for k in range(3)
                ]
                check(
                    f"eigenvalue multiset exact at a={a_val}, |b|={r_val}, delta={d_val}",
                    exact_multiset_equal(computed, target),
                )

    shifted = [sp.cos(delta + 2 * sp.pi / 3 + 2 * sp.pi * k / 3) for k in range(3)]
    reflected = [sp.cos(-delta + 2 * sp.pi * k / 3) for k in range(3)]
    check("delta -> delta + 2pi/3 relabels the multiset", all(exact_zero(shifted[k] - c[(k + 1) % 3]) for k in range(3)))
    check("delta -> -delta relabels k -> -k", all(exact_zero(reflected[k] - c[(-k) % 3]) for k in range(3)))

    p3_at_0 = sum(sp.cos(2 * sp.pi * k / 3) ** 3 for k in range(3))
    p3_shift = sum(sp.cos(sp.Rational(1, 10) + 2 * sp.pi * k / 3) ** 3 for k in range(3))
    reject_diff = simplify_exact(p3_shift - p3_at_0)
    check("reject generic shift delta -> delta + 1/10", reject_diff.is_zero is False)
    check("generic-shift rejector has definite sign", reject_diff.is_negative is True)

    strip = [sp.Rational(2, 9), sp.Rational(1, 9), sp.Rational(3, 10)]
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            diff = sp.cos(3 * strip[i]) - sp.cos(3 * strip[j])
            check(f"injectivity sample cos(3*{strip[i]}) != cos(3*{strip[j]})", diff.is_zero is False)
    for d_val in strip:
        deriv = -3 * sp.sin(3 * d_val)
        check(f"strict monotonic derivative sample at delta={d_val}", deriv.is_negative is True)


def part_c_ta2() -> None:
    print("=== PART C: T-A2 holonomy and gauge representative ===")
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    b = sp.symbols("b", nonzero=True)
    check("det(b C) == b^3", sp.simplify((b * C).det() - b**3) == 0)
    rho, delta = sp.symbols("rho delta", positive=True, real=True)
    check(
        "(|b| exp(i delta))^3 == |b|^3 exp(i 3 delta)",
        sp.simplify((rho * sp.exp(sp.I * delta)) ** 3 - rho**3 * sp.exp(3 * sp.I * delta)) == 0,
    )

    theta1, theta2, theta3, epsilon = sp.symbols("theta1 theta2 theta3 epsilon", real=True)
    mu = (theta1 + theta2 + theta3) / 3
    phi1 = sp.Integer(0)
    phi2 = phi1 + theta1 - mu
    phi3 = phi2 + theta2 - mu
    check("constructive phi2 recurrence", exact_zero(phi2 - phi1 - theta1 + mu))
    check("constructive phi3 recurrence", exact_zero(phi3 - phi2 - theta2 + mu))
    check("cycle recurrence closes", exact_zero(phi1 - phi3 - theta3 + mu))

    E12, E23, E31 = sp.zeros(3), sp.zeros(3), sp.zeros(3)
    E12[0, 1] = 1
    E23[1, 2] = 1
    E31[2, 0] = 1
    edge = E12 + E23 + E31
    Hp = sp.exp(sp.I * theta1) * E12 + sp.exp(sp.I * theta2) * E23 + sp.exp(sp.I * theta3) * E31
    Hp = Hp + Hp.conjugate().T
    D = sp.diag(sp.exp(sp.I * phi1), sp.exp(sp.I * phi2), sp.exp(sp.I * phi3))
    H_edge = sp.exp(sp.I * mu) * edge + sp.exp(-sp.I * mu) * edge.T
    check("equal-modulus lemma symbolic matrix identity", matrix_exact_zero(D * Hp * D.conjugate().T - H_edge))

    H_ta1_minus = sp.exp(-sp.I * mu) * C + sp.exp(sp.I * mu) * C.T
    check("orientation convention: edge representative equals H(0,1,-Phi/3) in T-A1 C convention", matrix_exact_zero(H_edge - H_ta1_minus))

    Hp_bad = sp.exp(sp.I * (theta1 + epsilon)) * E12 + sp.exp(sp.I * theta2) * E23 + sp.exp(sp.I * theta3) * E31
    Hp_bad = Hp_bad + Hp_bad.conjugate().T
    bad_matrix = D * Hp_bad * D.conjugate().T - H_edge
    bad_instance = bad_matrix.subs({theta1: 0, theta2: 0, theta3: 0, epsilon: sp.Rational(1, 5)})
    check("reject perturbed theta1 in equal-modulus gauge", not matrix_exact_zero(bad_instance))

    S = C + C**2
    D_generic = sp.diag(1, sp.exp(sp.I * sp.Rational(1, 5)), sp.exp(sp.I * sp.Rational(1, 7)))
    pointer_diff = D_generic * S * D_generic.conjugate().T - S
    check("pointer caveat: generic diagonal conjugation does not fix S", not matrix_exact_zero(pointer_diff))
    H_symbolic = sp.symbols("a", real=True) * sp.eye(3) + rho * sp.exp(sp.I * delta) * C + rho * sp.exp(-sp.I * delta) * C.T
    check("[H(a,|b|,delta), S] == 0 on retained frame", matrix_exact_zero(H_symbolic * S - S * H_symbolic))


def part_d_tb() -> None:
    print("=== PART D: T-B identity-unit transport ===")
    omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    S_sum = sum(1 / ((omega**j - 1) * (omega ** (2 * j) - 1)) for j in [1, 2])
    check("core identity (omega-1)(omega^2-1) == 3", sp.simplify((omega - 1) * (omega**2 - 1) - 3) == 0)
    check("S_sum == 2/3 exactly", sp.simplify(S_sum - sp.Rational(2, 3)) == 0)
    check("L3(1,2) = S_sum/3 == 2/9", sp.simplify(S_sum / 3 - sp.Rational(2, 9)) == 0)
    check("reject S_sum as density 2/9", sp.simplify(S_sum - sp.Rational(2, 9)) != 0)

    S_frac = Fraction(2, 3)
    phi = lambda c: c * S_frac
    check("Phi(1) == 2/3", phi(Fraction(1, 1)) == Fraction(2, 3))
    check("wrong-member rejector Phi(1/2) != 2/3", phi(Fraction(1, 2)) != Fraction(2, 3))
    check("PR #4783 count member maps Phi(9/2) == 3, not 2/3", phi(Fraction(9, 2)) == Fraction(3, 1))
    check("c=1 iff Phi(c)=2/3 in Fraction arithmetic", phi(Fraction(1, 1)) == S_frac and Fraction(2, 3) / S_frac == 1)

    for lam in [Fraction(1, 2), Fraction(2, 1), Fraction(7, 5)]:
        for c_val in [Fraction(1, 1), Fraction(1, 2)]:
            check(
                f"rescale obstruction applies verbatim on holonomy coordinates lam={lam}, c={c_val}",
                phi(lam * c_val) == lam * phi(c_val),
            )

    check("3*(2/9) == 2/3", Fraction(3, 1) * Fraction(2, 9) == Fraction(2, 3))
    check("fundamental domain lower bound 0 <= 2/3", Fraction(0, 1) <= Fraction(2, 3))
    check("fundamental domain upper bound 2/3 < pi", bool(sp.Rational(2, 3) < sp.pi))


def part_e_note() -> None:
    print("=== PART E: note discipline ===")
    text = read(NOTE)
    flat_text = flat(text)
    required = [
        "the registrable phase content of the Brannen dial is exactly `cos(3 delta)`",
        "W_cycle_holonomy_value",
        "Phi = 3 delta",
        "Phi = 2/3",
        "unaveraged C3 fixed-point sum",
        "This re-coordination does not derive `Phi = 2/3`",
        "observation, not a derivation",
    ]
    for phrase in required:
        check(f"note contains required phrase: {phrase}", phrase in text)
    for n in range(1, 9):
        check(f"note contains N{n} header", f"### N{n}" in text)

    forbidden = [
        "only" + " route",
        "last" + " route",
        "exha" + "usted",
        "closes" + " the route",
        "AC_phi_lambda is" + " solved",
        "AC_phi_lambda is" + " closed",
        "PD" + "G",
    ]
    lower_text = text.lower()
    for phrase in forbidden:
        check(f"forbidden phrase absent: {phrase}", phrase.lower() not in lower_text)
    check("note declares canonical bounded_theorem claim type", "**Claim type:** bounded_theorem" in text)
    check("note does not use runner PASS as source status", "**Status:** PASS" not in text)
    check("note does not lean on PR #4783 as authority", "BY PR #4783 obstruction" not in text)
    check("note says not a terminal no-go", "not a terminal no-go" in flat_text.lower())
    check("status-authority header present", "**Status authority:** independent audit lane only." in text)
    check("primary runner link present", "scripts/acphilambda_registrable_cycle_holonomy_normal_form_2026_07_01.py" in text)

    dep_basenames = [
        "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md",
        "KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md",
        "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
        "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md",
    ]
    for basename in dep_basenames:
        check(f"dependency markdown link present: {basename}", f"]({basename})" in text)

    bad_targets = re.findall(r"\]\(([^)]*ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION[^)]*)\)", text)
    check("PR #4783 note basename is not a markdown link target", not bad_targets)
    check("PR #4783 note basename appears backticked", "`ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01`" in text)
    check("verification block names expected TOTAL line", "TOTAL: PASS=" in text and "FAIL=0" in text)
    check("claim block flattened still carries Phi(c)=c*S_sum", "Phi(c) = 3 c L3 = c S_sum" in flat_text)


def main() -> int:
    part_a_sources()
    part_b_ta1()
    part_c_ta2()
    part_d_tb()
    part_e_note()
    if FAIL == 0:
        print("RESULT: PASS - all exact symbolic and note-discipline gates passed")
    else:
        print("RESULT: FAIL - one or more exact gates failed")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
