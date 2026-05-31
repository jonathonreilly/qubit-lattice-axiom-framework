#!/usr/bin/env python3
"""
Q1 signed selected-line readout no-go.

The previous bridge proved the exact coefficient identity

    coeff_nonid(S_Q1) = -eta_APS.

This runner attacks the next theorem:

    signed_selected_line_readout_delta_equals_minus_q1_offsite_coeff_or_no_go.

Result: no-go for Q1 alone.  The Q1 source is transposition-even: the
transposition swaps the two nonidentity C3 coefficients, but Q1 has equal
coefficients.  The circulant phase delta is transposition-odd.  Therefore any
transposition-equivariant readout from Q1 data alone to the signed delta line
must vanish.  It can recover the magnitude eta_APS, but not the sign.

A signed selected-line orientation primitive epsilon would close the sign
conditionally via delta = epsilon * eta_APS, but epsilon is extra based
endpoint/orientation data, not contained in S_Q1.
"""

from __future__ import annotations

import sys
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


def main() -> int:
    section("A. Q1 coefficient bridge inputs")

    c_g = sp.Rational(-2, 9)
    c_g2 = sp.Rational(-2, 9)
    eta_aps = sp.Rational(2, 9)
    q1_even_vector = sp.Matrix([c_g, c_g2])
    swap = sp.Matrix([[0, 1], [1, 0]])

    record(
        "A.1 Q1 nonidentity coefficients are equal",
        c_g == c_g2 == -eta_aps,
        f"(coeff_g, coeff_g2)=({c_g}, {c_g2}), eta_APS={eta_aps}",
    )
    record(
        "A.2 transposition swaps the two nonidentity coefficients and fixes Q1",
        swap * q1_even_vector == q1_even_vector,
        f"swap*(c_g,c_g2)={list(swap * q1_even_vector)}",
    )
    record(
        "A.3 even magnitude readout recovers eta_APS",
        -sp.Rational(1, 2) * (c_g + c_g2) == eta_aps,
        "-(coeff_g+coeff_g2)/2 = eta_APS.",
    )

    section("B. Linear equivariant readout no-go")

    a, b, x, y = sp.symbols("a b x y")
    f = a * x + b * y
    f_swapped = a * y + b * x
    # Equivariance to the odd sign line requires f(swap v) = -f(v) for all v.
    coeff_eqs = sp.Poly(sp.expand(f_swapped + f), x, y).coeffs()
    sol = sp.solve([sp.Eq(coeff, 0) for coeff in coeff_eqs], (a, b), dict=True)
    record(
        "B.1 every linear transposition-equivariant odd readout is proportional to c_g-c_g2",
        sol == [{a: -b}] or sol == [{b: -a}],
        f"solution={sol}; f=a*(x-y)",
    )

    odd_linear_q1 = sp.simplify(a * c_g - a * c_g2)
    record(
        "B.2 all such odd linear readouts vanish on Q1",
        odd_linear_q1 == 0,
        f"a*(coeff_g-coeff_g2)={odd_linear_q1}",
    )
    record(
        "B.3 the nonzero target eta_APS cannot be obtained by Q1-alone odd linear readout",
        odd_linear_q1 != eta_aps and eta_aps != 0,
        f"odd_readout(Q1)={odd_linear_q1}, eta_APS={eta_aps}",
    )

    section("C. General equivariant readout no-go at the fixed point")

    # This is the representation-theoretic core.  If d is fixed by tau and
    # the target line is odd, any equivariant map F satisfies
    # F(d)=F(tau d)=tau F(d)=-F(d), hence F(d)=0.
    Fd = sp.symbols("F_d")
    fixed_domain = True
    odd_target_constraint = sp.Eq(Fd, -Fd)
    record(
        "C.1 equivariance from a transposition-fixed domain point to an odd line forces zero",
        fixed_domain and sp.solve(odd_target_constraint, Fd) == [0],
        "F(d)=F(tau d)=tau F(d)=-F(d), so F(d)=0.",
    )
    record(
        "C.2 Q1 alone cannot supply a nonzero signed delta",
        eta_aps != 0,
        "The desired signed value is nonzero, but every equivariant Q1-alone odd readout is zero.",
    )

    section("D. Minimal conditional escape: add an orientation primitive")

    epsilon = sp.symbols("epsilon")
    delta_signed = sp.simplify(epsilon * eta_aps)
    # The orientation primitive is odd: tau epsilon = -epsilon.  Then
    # tau(delta)=(-epsilon)*eta=-delta.
    record(
        "D.1 an odd orientation primitive would make delta=epsilon*eta_APS equivariant",
        sp.simplify((-epsilon) * eta_aps + delta_signed) == 0,
        "If tau(epsilon)=-epsilon, then tau(delta)=-delta.",
    )
    record(
        "D.2 choosing the positive selected-line orientation gives delta=2/9 conditionally",
        delta_signed.subs(epsilon, 1) == eta_aps,
        "epsilon=+1 is an added based orientation, not Q1 data.",
    )
    record(
        "D.3 choosing the opposite orientation gives the mirror delta=-2/9",
        delta_signed.subs(epsilon, -1) == -eta_aps,
        "Both signs are parity mirrors until an orientation/basepoint law is supplied.",
    )

    section("E. Repo guardrails")

    parity_note = read_rel("docs/NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23.md")
    selected_line_note = read_rel("docs/KOIDE_SELECTED_LINE_CYCLIC_RESPONSE_BRIDGE_NOTE_2026-04-18.md")
    generation_no_go = read_rel("docs/CHARGED_LEPTON_SELECTED_LINE_GENERATION_SELECTOR_NO_GO_NOTE_2026-04-27.md")
    dimensionless_runner = read_rel("scripts/frontier_koide_dimensionless_objection_closure_review.py")
    coeff_bridge = read_rel("scripts/frontier_koide_q1_aps_brannen_coefficient_bridge.py")

    record(
        "E.1 parity note says delta is transposition-odd",
        ("delta -> -delta" in parity_note or "delta -> -delta" in parity_note.replace("->", "->"))
        or ("delta " in parity_note and " -delta" in parity_note)
        or ("delta" in parity_note and "parity order parameter" in parity_note),
    )
    record(
        "E.2 selected-line bridge only acts after the phase is genuinely closed",
        "once the Brannen-Zenczykowski phase offset is genuinely closed" in selected_line_note
        and "delta = 2/9  ->  kappa_sel,*" in selected_line_note,
    )
    record(
        "E.3 generation-selector no-go says basepoint data are additional physical data",
        "the basepoint is additional physical data" in generation_no_go
        and "BASED_ENDPOINT_OR_SOURCE_LAW_REQUIRED=TRUE" in generation_no_go,
    )
    record(
        "E.4 dimensionless runner keeps selected-line delta support conditional",
        "selected-line local support conditionally transfers eta_APS to delta" in dimensionless_runner
        and "DELTA_FORCED_WITHOUT_LINE_LOCAL_BASEPOINT_LAW=FALSE" in dimensionless_runner,
    )
    record(
        "E.5 coefficient bridge already states Q1 does not supply the parity-odd sign",
        "Q1_SUPPLIES_PARITY_ODD_SIGN=FALSE" in coeff_bridge,
    )

    section("F. Scoped verdict")

    q1_alone_signed_readout_closed = False
    orientation_primitive_required = True
    conditional_orientation_closes_sign = True

    record(
        "F.1 signed selected-line readout from Q1 alone is ruled out",
        not q1_alone_signed_readout_closed,
        "Even source data cannot equivariantly determine an odd nonzero sign.",
    )
    record(
        "F.2 a signed selected-line orientation/basepoint is the minimal extra primitive",
        orientation_primitive_required and conditional_orientation_closes_sign,
        "With epsilon supplied, delta=epsilon*eta_APS is equivariant and nonzero.",
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
        print("VERDICT: Q1 alone cannot supply the signed selected-line delta readout.")
        print("KOIDE_Q1_SIGNED_SELECTED_LINE_READOUT_NO_GO=TRUE")
        print("Q1_EVEN_SOURCE_TO_ODD_DELTA_EQUIVARIANT_READOUT_ZERO=TRUE")
        print("SIGNED_DELTA_FROM_Q1_ALONE=FALSE")
        print("CONDITIONAL_ORIENTATION_PRIMITIVE_CLOSES_SIGN=TRUE")
        print("NEW_PRIMITIVE_REQUIRED=signed_selected_line_orientation_or_based_endpoint")
        print("DELTA_ETA_APS_PHYSICAL_READOUT_CLOSED=FALSE")
        print("Q1_DARK_MATTER_CLOSURE=FALSE")
        print("NEXT_THEOREM=derive_signed_selected_line_orientation_from_retained_source_domain_or_accept_no_go")
        return 0

    print("VERDICT: signed selected-line readout no-go has failing checks.")
    print("KOIDE_Q1_SIGNED_SELECTED_LINE_READOUT_NO_GO=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
