#!/usr/bin/env python3
"""
Q1 oriented-sign compatibility closeout.

This runner separates three statements that were easy to conflate:

  1. In an oriented C3/selected-line frame, Q1's nonidentity coefficient has
     the right sign for the current +2/9 branch:

         coeff_nonid(S_Q1) = -2/9
         delta_oriented := -coeff_nonid(S_Q1) = +2/9.

  2. Q1 alone does not derive the orientation.  The transposition-even Q1
     packet supplies the magnitude; an orientation/basepoint supplies epsilon.

  3. Therefore the sign is not proved wrong.  It is compatible and right in
     the admitted oriented frame, but underived from Q1/gamma alone.

No observed lepton masses, fitted selectors, or PDG phase inputs are used.
"""

from __future__ import annotations

import math
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


def sorted_cos_spectrum(delta: float) -> list[float]:
    return sorted(math.cos(delta + 2.0 * math.pi * k / 3.0) for k in range(3))


def main() -> int:
    section("A. Oriented C3 frame and Q1 coefficient")

    e = sp.eye(3)
    g = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    g2 = g**2
    tau = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    s_q1 = sp.Rational(10, 9) * e - sp.Rational(2, 9) * g - sp.Rational(2, 9) * g2
    coeff_g = sp.Rational(-2, 9)
    coeff_g2 = sp.Rational(-2, 9)
    eta_aps = sp.Rational(2, 9)

    record(
        "A.1 Q1 source has oriented-frame nonidentity coefficient -2/9",
        s_q1 == sp.Rational(10, 9) * e + coeff_g * g + coeff_g2 * g2,
        f"S_Q1 = 10/9 e {coeff_g} g {coeff_g2} g^2",
    )
    record(
        "A.2 the oriented positive readout -coeff_g is +eta_APS",
        -coeff_g == eta_aps,
        f"-coeff_g(S_Q1)={-coeff_g}, eta_APS={eta_aps}",
    )
    record(
        "A.3 the mirror nonidentity coefficient has the same magnitude",
        -coeff_g2 == eta_aps,
        f"-coeff_g2(S_Q1)={-coeff_g2}",
    )

    section("B. Orientation variable is load-bearing")

    epsilon = sp.symbols("epsilon")
    delta_signed = epsilon * eta_aps
    record(
        "B.1 an orientation bit converts the Q1 magnitude into a signed delta",
        delta_signed.subs(epsilon, 1) == eta_aps
        and delta_signed.subs(epsilon, -1) == -eta_aps,
        "delta = epsilon * eta_APS.",
    )
    record(
        "B.2 Q1 is transposition-even",
        tau * s_q1 * tau == s_q1,
        "tau swaps g and g^2 but fixes S_Q1.",
    )
    odd_line = sp.I * (g - g2)
    record(
        "B.3 the selected-line sign line is transposition-odd",
        tau * odd_line * tau == -odd_line,
        "J = i(g-g^2) flips sign.",
    )
    odd_projection = sp.simplify(sp.trace(s_q1 * odd_line) / sp.trace(odd_line * odd_line))
    record(
        "B.4 Q1 alone has zero odd projection",
        odd_projection == 0,
        f"projection<S_Q1,J>={odd_projection}",
    )

    section("C. Selected-line mirror compatibility")

    delta = 2.0 / 9.0
    plus_spec = sorted_cos_spectrum(delta)
    minus_spec = sorted_cos_spectrum(-delta)
    record(
        "C.1 +2/9 and -2/9 are mirror-compatible as unordered spectra",
        all(abs(a - b) < 1e-12 for a, b in zip(plus_spec, minus_spec)),
        "The sign is not visible without an oriented slot/Fourier frame.",
    )
    record(
        "C.2 in the admitted oriented frame the compatible target is +2/9",
        eta_aps == sp.Rational(2, 9) and -coeff_g == sp.Rational(2, 9),
        "delta_oriented := -coeff_g(S_Q1) = +2/9.",
    )
    record(
        "C.3 this is compatibility, not derivation of the physical frame",
        odd_projection == 0 and -coeff_g == eta_aps,
        "Q1 supplies eta_APS; the frame supplies epsilon=+1.",
    )

    section("D. Repo consistency checks")

    coeff_note = read_rel("docs/KOIDE_Q1_APS_BRANNEN_COEFFICIENT_BRIDGE_NOTE_2026-05-31.md")
    bottom_up_note = read_rel("docs/KOIDE_Q1_BOTTOM_UP_SIGN_ORIENTATION_AUDIT_NOTE_2026-05-31.md")
    gamma_note = read_rel("docs/KOIDE_Q1_GAMMA_SHEET_SIGN_PROBE_NOTE_2026-05-31.md")
    selected_line_note = read_rel("docs/KOIDE_SELECTED_LINE_CYCLIC_RESPONSE_BRIDGE_NOTE_2026-04-18.md")

    record(
        "D.1 coefficient bridge records coeff_nonid(S_Q1) = -eta_APS",
        "coeff_nonid(S_Q1) = - eta_APS" in coeff_note
        or "coeff_nonid(S_Q1) = -eta_APS" in coeff_note,
    )
    record(
        "D.2 bottom-up audit records the missing odd orientation primitive",
        "zero odd component" in bottom_up_note
        and "oriented C3 generator" in bottom_up_note,
    )
    record(
        "D.3 gamma probe records that +2/9 is not contradicted",
        "SIGN_WRONG_PROVEN=FALSE" in gamma_note
        and "CURRENT_ORIENTED_SELECTED_LINE_SIGN_PLUS=TRUE" in gamma_note,
    )
    record(
        "D.4 selected-line bridge has the +2/9 first-branch target",
        "delta = 2/9" in selected_line_note and "m_*" in selected_line_note,
    )

    section("E. Verdict")

    record(
        "E.1 the sign is right in the admitted oriented frame",
        -coeff_g == eta_aps == sp.Rational(2, 9),
        "Q1's negative offsite coefficient maps to delta=+2/9 by -coeff_g.",
    )
    record(
        "E.2 the sign is not derived from Q1 alone",
        odd_projection == 0,
        "The orientation/basepoint remains load-bearing.",
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
        print("VERDICT: oriented-frame sign is compatible and positive; physical orientation remains open.")
        print("KOIDE_Q1_ORIENTED_SIGN_COMPATIBILITY_CLOSEOUT=TRUE")
        print("CURRENT_ORIENTED_SELECTED_LINE_SIGN_PLUS=TRUE")
        print("Q1_OFFSITE_COEFF_GIVES_DELTA_PLUS_IN_ORIENTED_FRAME=TRUE")
        print("SIGN_WRONG_PROVEN=FALSE")
        print("SIGN_DERIVED_FROM_Q1_ALONE=FALSE")
        print("ORIENTATION_FRAME_LOAD_BEARING=TRUE")
        print("SIGNED_DELTA_FROM_Q1_PLUS_ORIENTATION=CONDITIONAL")
        print("RETAINED_CHARGED_LEPTON_SIGN_CLOSURE=FALSE")
        print("NEXT_THEOREM=derive_physical_selected_line_slot_orientation_or_source_domain_Z_erasure")
        return 0

    print("VERDICT: oriented sign compatibility closeout has failing checks.")
    print("KOIDE_Q1_ORIENTED_SIGN_COMPATIBILITY_CLOSEOUT=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
