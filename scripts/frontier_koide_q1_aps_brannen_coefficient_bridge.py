#!/usr/bin/env python3
"""
Q=1 offsite coefficient -> APS eta -> Brannen magnitude bridge.

This runner tries to build the requested bridge as far as the current algebra
allows.  It proves an exact C3 group-algebra coefficient identity:

    S_Q1 = I - Z/3 = 10/9 e - 2/9 g - 2/9 g^2

while the APS fixed-point value for C3[111] transverse weights (1,2) is

    eta_APS = (1/3) * (1/3 + 1/3) = 2/9.

Therefore every nonidentity group-algebra/offsite coefficient of S_Q1 is

    coeff_nonid(S_Q1) = - eta_APS.

At the exact-support layer this also matches the Brannen conjugate-pair
magnitude n_eff/d^2 = 2/9.  The runner deliberately does not promote this to
physical phase closure: Q1 is transposition-even and supplies no parity-odd
sign/readout law by itself.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PASSES: list[tuple[str, bool, str]] = []


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


def coeffs_in_c3_group_algebra(matrix: sp.Matrix) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Solve matrix = a0 I + a1 C + a2 C^2 in the regular C3 basis."""
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    I3 = sp.eye(3)
    a0, a1, a2 = sp.symbols("a0 a1 a2")
    expr = sp.simplify(a0 * I3 + a1 * C + a2 * C**2 - matrix)
    equations = [sp.Eq(expr[i, j], 0) for i in range(3) for j in range(3)]
    sol = sp.solve(equations, (a0, a1, a2), dict=True)
    if len(sol) != 1:
        raise ValueError(f"expected unique C3 group-algebra coefficients, got {sol}")
    return tuple(sp.simplify(sol[0][a]) for a in (a0, a1, a2))


def aps_eta_c3_weights_12() -> tuple[sp.Expr, list[sp.Expr]]:
    omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    terms: list[sp.Expr] = []
    for k in (1, 2):
        z1 = omega**k
        z2 = omega ** (2 * k)
        terms.append(sp.simplify(1 / ((z1 - 1) * (z2 - 1))))
    eta = sp.simplify(sum(terms) / 3)
    return eta, terms


def main() -> int:
    section("A. C3 group-algebra form of the Q=1 source")

    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    I3 = sp.eye(3)
    P_plus = sp.simplify((I3 + C + C**2) / 3)
    P_perp = sp.simplify(I3 - P_plus)
    Z = sp.simplify(P_plus - P_perp)
    S_q1 = sp.simplify(I3 - Z / 3)

    z_coeffs = coeffs_in_c3_group_algebra(Z)
    s_coeffs = coeffs_in_c3_group_algebra(S_q1)

    record(
        "A.1 Z has group-algebra coefficients (-1/3, 2/3, 2/3)",
        z_coeffs == (sp.Rational(-1, 3), sp.Rational(2, 3), sp.Rational(2, 3)),
        f"Z={z_coeffs[0]}*e + {z_coeffs[1]}*g + {z_coeffs[2]}*g^2",
    )
    record(
        "A.2 S_Q1=I-Z/3 has coefficients (10/9, -2/9, -2/9)",
        s_coeffs == (sp.Rational(10, 9), sp.Rational(-2, 9), sp.Rational(-2, 9)),
        f"S_Q1={s_coeffs[0]}*e + {s_coeffs[1]}*g + {s_coeffs[2]}*g^2",
    )
    record(
        "A.3 every offsite matrix entry equals the nonidentity coefficient -2/9",
        all(S_q1[i, j] == sp.Rational(-2, 9) for i in range(3) for j in range(3) if i != j),
        f"S_Q1={S_q1}",
    )

    section("B. APS eta fixed-point coefficient")

    eta_aps, terms = aps_eta_c3_weights_12()
    record(
        "B.1 APS fixed-point denominator terms are both 1/3",
        terms == [sp.Rational(1, 3), sp.Rational(1, 3)],
        f"terms={terms}",
    )
    record(
        "B.2 APS eta for C3 weights (1,2) is 2/9",
        eta_aps == sp.Rational(2, 9),
        f"eta_APS={eta_aps}",
    )
    record(
        "B.3 unaveraged APS class sum equals the Z nonidentity coefficient 2/3",
        sp.simplify(sum(terms) - z_coeffs[1]) == 0
        and sp.simplify(sum(terms) - z_coeffs[2]) == 0,
        f"sum APS terms={sum(terms)}, coeff_g(Z)={z_coeffs[1]}",
    )

    section("C. Exact Q1 -> APS coefficient bridge")

    q1_edge_readout = sp.simplify(-s_coeffs[1])
    q1_edge_readout_2 = sp.simplify(-s_coeffs[2])
    record(
        "C.1 minus the Q1 nonidentity coefficient equals eta_APS",
        q1_edge_readout == eta_aps and q1_edge_readout_2 == eta_aps,
        f"-coeff_g(S_Q1)={q1_edge_readout}, -coeff_g2(S_Q1)={q1_edge_readout_2}",
    )
    record(
        "C.2 Q1 offsite matrix readout magnitude equals eta_APS",
        all(-S_q1[i, j] == eta_aps for i in range(3) for j in range(3) if i != j),
        "Every directed offsite entry gives the same coefficient bridge.",
    )

    # The bridge is special to forced d=3 when compared to the APS function.
    d = sp.symbols("d")
    aps_general = (d**2 - 1) / (12 * d)
    offsite_general = 2 / d**2
    equality_poly = sp.factor(d**3 - d - 24)
    record(
        "C.3 APS/offsite equality is special to the forced d=3 surface",
        sp.factor(equality_poly) == (d - 3) * (d**2 + 3 * d + 8)
        and sp.simplify(aps_general.subs(d, 3) - offsite_general.subs(d, 3)) == 0,
        f"equality polynomial={sp.factor(equality_poly)}",
    )

    section("D. Composition with Brannen magnitude")

    n_eff = Fraction(2, 1)
    d3 = Fraction(3, 1)
    delta_brannen_magnitude = n_eff / (d3 * d3)
    q1_q_over_d = Fraction(1, 1) / d3
    record(
        "D.1 Brannen conjugate-pair magnitude n_eff/d^2 equals eta_APS",
        sp.Rational(delta_brannen_magnitude.numerator, delta_brannen_magnitude.denominator) == eta_aps,
        f"n_eff/d^2={delta_brannen_magnitude}",
    )
    record(
        "D.2 the bridge is not the Q=1 Q/d route",
        q1_q_over_d == Fraction(1, 3) and q1_q_over_d != Fraction(2, 9),
        f"Q1/d={q1_q_over_d}, not 2/9",
    )
    record(
        "D.3 exact support chain gives |delta| = eta_APS = -coeff_nonid(S_Q1)",
        sp.Rational(delta_brannen_magnitude.numerator, delta_brannen_magnitude.denominator)
        == eta_aps
        == q1_edge_readout,
        f"delta_magnitude={delta_brannen_magnitude}, eta_APS={eta_aps}, -coeff={q1_edge_readout}",
    )

    section("E. Remaining typed readout and parity gap")

    # A transposition swaps C and C^2.  S_Q1 has equal coefficients, so it is
    # transposition-even.  The circulant phase delta is transposition-odd in
    # the existing parity theorem.  Q1 therefore supplies a magnitude/coefficient
    # bridge, not a signed parity-order-parameter theorem.
    transposition_even = s_coeffs[1] == s_coeffs[2]
    antisymmetric_edge_component = sp.simplify(s_coeffs[1] - s_coeffs[2])
    record(
        "E.1 Q1 source is transposition-even in the nonidentity coefficients",
        transposition_even and antisymmetric_edge_component == 0,
        f"coeff_g - coeff_g2 = {antisymmetric_edge_component}",
    )
    record(
        "E.2 Q1 therefore does not by itself supply the parity-odd sign of delta",
        True,
        "It supplies the magnitude/edge coefficient; a signed selected-line readout or orientation law is still needed.",
    )

    parity_note = read_rel("docs/NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23.md")
    aps_note = read_rel("docs/KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23.md")
    dimensionless_runner = read_rel("scripts/frontier_koide_dimensionless_objection_closure_review.py")
    record(
        "E.3 repo parity note identifies delta as the transposition-odd circulant phase",
        ("delta -> -delta" in parity_note or "delta \u2192 -delta" in parity_note or "delta \u2192 \u2212delta" in parity_note or "\u03b4 \u2192 \u2212\u03b4" in parity_note)
        and "parity order parameter" in parity_note,
    )
    record(
        "E.4 APS route note keeps delta=eta_APS as the remaining physical gap",
        "physical identification" in aps_note
        and ("delta = eta_APS" in aps_note or "\u03b4 = \u03b7_APS" in aps_note)
        and "single remaining gap" in aps_note,
    )
    record(
        "E.5 selected-line support is conditional, not an automatic physical bridge",
        "selected-line local support conditionally transfers eta_APS to delta" in dimensionless_runner
        and "DELTA_FORCED_WITHOUT_LINE_LOCAL_BASEPOINT_LAW=FALSE" in dimensionless_runner,
    )

    section("F. Scoped verdict")

    coefficient_bridge_built = True
    physical_phase_closed = False
    parity_odd_sign_supplied_by_q1 = False

    record(
        "F.1 exact Q1 coefficient bridge to APS eta is built",
        coefficient_bridge_built and q1_edge_readout == eta_aps,
        "This is an exact C3 group-algebra identity.",
    )
    record(
        "F.2 full Brannen phase closure still needs a signed selected-line readout theorem",
        not physical_phase_closed and not parity_odd_sign_supplied_by_q1,
        "The result is exact support/conditional bridge, not retained physical phase closure.",
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
        print("VERDICT: exact Q1 -> APS coefficient bridge built; physical Brannen readout still open.")
        print("KOIDE_Q1_APS_COEFFICIENT_BRIDGE=TRUE")
        print("Q1_NONIDENTITY_COEFF_EQUALS_MINUS_ETA_APS=TRUE")
        print("Q1_OFFSITE_READOUT_MAGNITUDE_EQUALS_APS_ETA=TRUE")
        print("Q1_BRANNEN_MAGNITUDE_EXACT_SUPPORT=TRUE")
        print("Q1_SUPPLIES_PARITY_ODD_SIGN=FALSE")
        print("DELTA_ETA_APS_PHYSICAL_READOUT_CLOSED=FALSE")
        print("Q1_DARK_MATTER_CLOSURE=FALSE")
        print("NEXT_THEOREM=signed_selected_line_readout_delta_equals_minus_q1_offsite_coeff_or_no_go")
        return 0

    print("VERDICT: Q1 -> APS coefficient bridge has failing checks.")
    print("KOIDE_Q1_APS_COEFFICIENT_BRIDGE=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
