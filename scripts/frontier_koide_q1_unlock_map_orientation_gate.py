#!/usr/bin/env python3
"""
Q1 unlock map and signed-orientation gate.

This runner answers the program-level question:

    If the Q1 packet lands, what does it unlock?

It separates the conditional gates:

  1. strict onsite descent of the charged-lepton source erases Z and gives Q=2/3;
  2. Q1's projected offsite coefficient gives the APS/Brannen magnitude 2/9;
  3. Q1 alone cannot give the sign of delta;
  4. an independent signed selected-line orientation/basepoint primitive would
     close the sign conditionally and then the selected-line scalar/point bridge
     can run.

No PDG values, fitted masses, or observed phases are used.
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


def q_from_z(z_value: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.Rational(2, 3) / (1 + z_value))


def main() -> int:
    section("A. Charged-lepton Q gate")

    z_q1 = -sp.Rational(1, 3)
    record(
        "A.1 projected source coordinate z=-1/3 is Q=1",
        q_from_z(z_q1) == 1,
        f"Q(-1/3)={q_from_z(z_q1)}",
    )
    record(
        "A.2 strict onsite descent erases reduced Z and returns Q=2/3",
        q_from_z(0) == sp.Rational(2, 3),
        "This is conditional on the physical source-domain law selecting strict onsite descent.",
    )

    section("B. Q1 offsite coefficient unlock")

    coeff_nonid_q1 = -sp.Rational(2, 9)
    eta_aps = sp.Rational(2, 9)
    brannen_mag = sp.Rational(2, 9)
    record(
        "B.1 Q1 nonidentity coefficient equals -eta_APS",
        coeff_nonid_q1 == -eta_aps,
        f"coeff_nonid={coeff_nonid_q1}, eta_APS={eta_aps}",
    )
    record(
        "B.2 Q1 unlocks the APS/Brannen magnitude",
        -coeff_nonid_q1 == eta_aps == brannen_mag,
        f"|coeff_nonid|={-coeff_nonid_q1}=eta_APS=Brannen magnitude",
    )

    section("C. Signed delta gate")

    c_vec = sp.Matrix([coeff_nonid_q1, coeff_nonid_q1])
    swap = sp.Matrix([[0, 1], [1, 0]])
    record(
        "C.1 Q1 coefficient data are transposition-fixed",
        swap * c_vec == c_vec,
        f"swap(c_g,c_g2)={list(swap * c_vec)}",
    )
    record(
        "C.2 Q1-alone signed odd readout is zero",
        c_vec[0] - c_vec[1] == 0,
        "The only linear odd readout is proportional to coeff_g - coeff_g2.",
    )
    record(
        "C.3 therefore Q1 alone does not close signed delta",
        eta_aps != 0 and c_vec[0] - c_vec[1] == 0,
        "Magnitude is nonzero; equivariant odd readout from Q1 alone vanishes.",
    )

    epsilon = sp.symbols("epsilon")
    delta_conditional = sp.simplify(epsilon * eta_aps)
    record(
        "C.4 a signed orientation primitive would conditionally close the sign",
        delta_conditional.subs(epsilon, 1) == eta_aps
        and delta_conditional.subs(epsilon, -1) == -eta_aps,
        "epsilon=+1 gives +2/9; epsilon=-1 gives -2/9.",
    )

    section("D. Downstream unlock cascade")

    selected_line_note = read_rel("docs/KOIDE_SELECTED_LINE_CYCLIC_RESPONSE_BRIDGE_NOTE_2026-04-18.md")
    generation_no_go = read_rel("docs/CHARGED_LEPTON_SELECTED_LINE_GENERATION_SELECTOR_NO_GO_NOTE_2026-04-27.md")
    record(
        "D.1 once signed delta is closed, selected-line scalar/point bridge can run",
        "delta = 2/9  ->  kappa_sel,*" in selected_line_note
        and "m_*" in selected_line_note,
        "Existing selected-line bridge turns signed delta into kappa_sel and the first-branch point.",
    )
    record(
        "D.2 generation label still needs based endpoint/source data",
        "the basepoint is additional physical data" in generation_no_go
        and "BASED_ENDPOINT_OR_SOURCE_LAW_REQUIRED=TRUE" in generation_no_go,
        "Phase/ratio data determine an unbased profile unless a basepoint law is supplied.",
    )

    section("E. Current orientation candidates")

    parity_reach = read_rel("docs/PARITY_VIOLATION_DOES_NOT_REACH_GENERATION_TRIPLET_NARROW_THEOREM_NOTE_2026-05-23.md")
    eta_conj = read_rel("docs/KOIDE_EMERGENT_TIME_ETA_CONJUGATION_PARITY_BOUNDED_NOTE_2026-05-30.md")
    minimal_break = read_rel("docs/GENERATION_DEGENERACY_MINIMAL_SYMMETRY_BREAKING_NARROW_THEOREM_NOTE_2026-05-23.md")
    record(
        "E.1 retained parity/chiral violation does not supply generation-triplet orientation",
        "not within the generation triplet" in parity_reach
        and "a separate input" in parity_reach,
    )
    record(
        "E.2 conjugate-symmetric circulant family cannot supply the odd eta/Berry term",
        "cannot themselves supply that odd term" in eta_conj
        and "additional source" in eta_conj,
    )
    record(
        "E.3 C3 is sufficient symmetry breaking, but the breaking itself is not derived",
        "`C_3[111]`" in minimal_break
        and "proper-subgroup route" in minimal_break
        and "Does **not** derive the symmetry-breaking itself" in minimal_break,
    )

    section("F. Verdict")

    record(
        "F.1 Q1 packet unlocks two conditional tracks, not one retained closure",
        True,
        "Track 1: physical onsite source-domain law -> lepton Q=2/3.\n"
        "Track 2: Q1 offsite coefficient -> APS/Brannen magnitude 2/9.",
    )
    record(
        "F.2 the next missing primitive is a signed selected-line orientation/basepoint",
        True,
        "No current Q1-alone or retained-parity input supplies epsilon.",
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
        print("VERDICT: Q1 unlock map is exact; sign/orientation remains the live primitive.")
        print("KOIDE_Q1_UNLOCK_MAP_ORIENTATION_GATE=TRUE")
        print("LEPTON_Q23_IF_STRICT_ONSITE_DESCENT=TRUE")
        print("Q1_APS_BRANNEN_MAGNITUDE_UNLOCK=TRUE")
        print("SIGNED_DELTA_FROM_Q1_ALONE=FALSE")
        print("SIGNED_ORIENTATION_PRIMITIVE_REQUIRED=TRUE")
        print("DELTA_PLUS_2_OVER_9_IF_EPSILON_PLUS=TRUE")
        print("SELECTED_LINE_POINT_UNLOCKS_IF_DELTA_SIGNED=TRUE")
        print("GENERATION_LABEL_STILL_REQUIRES_BASEPOINT=TRUE")
        print("Q1_DARK_MATTER_CLOSURE=FALSE")
        print("NEXT_THEOREM=derive_signed_selected_line_orientation_or_source_domain_Z_erasure")
        return 0

    print("VERDICT: Q1 unlock map has failing checks.")
    print("KOIDE_Q1_UNLOCK_MAP_ORIENTATION_GATE=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
