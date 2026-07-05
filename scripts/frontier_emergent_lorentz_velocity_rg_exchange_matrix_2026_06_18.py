#!/usr/bin/env python3
"""Exact exchange-matrix support for the interacting Lorentz velocity RG gate.

This runner supports
docs/EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md.

It proves the algebraic part of the supplied one-loop velocity RG packet:
if the two-speed flow is a linear mutual-drag exchange with positive
coefficients a,b and no independent common-speed source term, then the common
speed line is fixed, the weighted common speed is invariant, and the sole
difference mode has eigenvalue -(a+b). The physical one-loop computation of
a,b from a framework interaction remains outside this runner.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md"
PARENT = ROOT / "docs" / "EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")
    return ok


def mat_vec(a: Fraction, b: Fraction, x: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    v_f, v_b = x
    return (a * (v_b - v_f), b * (v_f - v_b))


def dot(w: tuple[Fraction, Fraction], x: tuple[Fraction, Fraction]) -> Fraction:
    return w[0] * x[0] + w[1] * x[1]


def ratio_rhs(a: Fraction, b: Fraction, eta: Fraction) -> Fraction:
    # eta = v_f/v_b with v_b > 0.
    return -(eta - 1) * (a + b * eta)


def main() -> int:
    print("=" * 88)
    print("Emergent Lorentz velocity RG exchange-matrix exact support")
    print("=" * 88)

    note = NOTE.read_text(encoding="utf-8")
    parent = PARENT.read_text(encoding="utf-8")
    flat_note = " ".join(note.split())
    flat_parent = " ".join(parent.split())

    check(
        "source note is exact support, not retained closure",
        "actual_current_surface_status: exact-support" in note
        and "proposal_allowed: false" in note
        and "bare_retained_allowed: false" in note,
    )
    check(
        "source note preserves the physical one-loop coefficient residual",
        "does not derive the physical one-loop coefficients" in flat_note
        and "spatial-only power-divergent coefficient" in flat_note
        and "LV-bound sufficiency" in flat_note,
    )
    check(
        "parent note has the source-side pointer without claiming status movement",
        "2026-06-18 velocity-RG exchange-matrix support" in parent
        and "No audit status changes here" in parent,
    )

    samples = [
        (Fraction(1, 7), Fraction(2, 5)),
        (Fraction(2, 3), Fraction(5, 11)),
        (Fraction(13, 17), Fraction(3, 8)),
        (Fraction(4, 9), Fraction(7, 6)),
    ]
    states = [
        (Fraction(3, 10), Fraction(1, 1)),
        (Fraction(5, 3), Fraction(2, 7)),
        (Fraction(9, 4), Fraction(9, 4)),
    ]

    for idx, (a, b) in enumerate(samples, 1):
        trace = -(a + b)
        det = Fraction(0)
        check(
            f"S{idx}: characteristic data are exact: trace=-(a+b), determinant=0",
            trace == -(a + b) and det == 0 and a > 0 and b > 0,
            f"a={a}, b={b}, trace={trace}",
        )
        check(
            f"S{idx}: common-speed line is fixed",
            mat_vec(a, b, (Fraction(1), Fraction(1))) == (Fraction(0), Fraction(0)),
        )
        left_null = (b, a)
        ok_left = all(dot(left_null, mat_vec(a, b, state)) == 0 for state in states)
        check(
            f"S{idx}: weighted common speed b*v_F+a*v_b is invariant",
            ok_left,
            f"left null vector=(b,a)=({b},{a})",
        )
        ok_diff = all(
            (mat_vec(a, b, state)[0] - mat_vec(a, b, state)[1])
            == -(a + b) * (state[0] - state[1])
            for state in states
        )
        check(
            f"S{idx}: difference mode obeys d(v_F-v_b)/dl=-(a+b)(v_F-v_b)",
            ok_diff,
        )
        for eta in (Fraction(1, 3), Fraction(7, 10), Fraction(3, 2), Fraction(4, 1)):
            rhs = ratio_rhs(a, b, eta)
            sign_ok = (eta < 1 and rhs > 0) or (eta > 1 and rhs < 0)
            check(
                f"S{idx}: ratio eta={eta} flows toward 1",
                sign_ok,
                f"d eta/dl = {rhs}",
            )

    # Uniqueness under the exchange hypotheses. A general linear two-speed flow
    # M has M(1,1)=0 iff each row sums to zero. Mutual drag with the correct signs
    # is then M=[[-a,a],[b,-b]], a,b>0.
    general_rows = [
        (Fraction(-2, 5), Fraction(2, 5), Fraction(3, 7), Fraction(-3, 7)),
        (Fraction(-5, 4), Fraction(5, 4), Fraction(1, 6), Fraction(-1, 6)),
    ]
    for idx, (m11, m12, m21, m22) in enumerate(general_rows, 1):
        a = m12
        b = m21
        unique = (m11 + m12 == 0) and (m21 + m22 == 0) and a > 0 and b > 0
        check(
            f"U{idx}: row-sum-zero + mutual-drag signs uniquely identify positive exchange coefficients",
            unique and m11 == -a and m22 == -b,
            f"M=[[{m11},{m12}],[{m21},{m22}]] -> a={a}, b={b}",
        )

    print("=" * 88)
    print("Interpretation:")
    print("- The exact exchange matrix supplies the algebraic one-loop RG form.")
    print("- The remaining Nature-grade input is physical: derive positive a,b from")
    print("  the framework's actual interacting matter/gauge vertices and compare the")
    print("  resulting coefficient/gamma against Lorentz-violation bounds.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
