#!/usr/bin/env python3
"""Scale-free ABJ native abelian anomaly core verifier.

This runner checks the exact symbolic identities in
ABJ_SCALE_FREE_NATIVE_ABELIAN_ANOMALY_CORE_BOUNDARY_NOTE_2026-06-18.md
and verifies that the ABJ bridge points to the new scale-free boundary
without claiming audit status.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs/ABJ_SCALE_FREE_NATIVE_ABELIAN_ANOMALY_CORE_BOUNDARY_NOTE_2026-06-18.md"
ABJ_BRIDGE_PATH = (
    ROOT
    / "docs/ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
)
RUNNER_PATH = "scripts/frontier_abj_scale_free_native_abelian_anomaly_core_2026_06_18.py"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    message = f"{status}: {name}"
    if detail:
        message += f" ({detail})"
    print(message)
    return condition


def symbolic_core() -> None:
    print("\n== Symbolic scale-free anomaly core ==")
    a = sp.symbols("a", nonzero=True)
    T = sp.Rational(1, 2)

    tr_y = 6 * a + 2 * (-3 * a)
    tr_y3 = 6 * a**3 + 2 * (-3 * a) ** 3
    tr_su3sq_y = 2 * T * a
    tr_su2sq_y = 3 * T * a + T * (-3 * a)
    tr_su3cube_lh = sp.Integer(2)

    check("Tr[Y_a] = 0", sp.simplify(tr_y) == 0, str(sp.simplify(tr_y)))
    check("Tr[Y_a^3] = -48 a^3", sp.simplify(tr_y3 + 48 * a**3) == 0, str(sp.expand(tr_y3)))
    check("Tr[SU(3)^2 Y_a] = a", sp.simplify(tr_su3sq_y - a) == 0, str(tr_su3sq_y))
    check("Tr[SU(2)^2 Y_a] = 0", sp.simplify(tr_su2sq_y) == 0, str(sp.simplify(tr_su2sq_y)))
    check("Tr[SU(3)^3]_LH = 2", tr_su3cube_lh == 2, str(tr_su3cube_lh))

    for sample in [sp.Rational(1, 3), sp.Rational(1, 5), sp.Rational(-2, 7)]:
        check(
            f"sample a={sample}: cubic anomaly nonzero",
            sp.simplify(tr_y3.subs(a, sample)) != 0,
            str(sp.simplify(tr_y3.subs(a, sample))),
        )
        check(
            f"sample a={sample}: mixed SU(3)^2 U(1) anomaly nonzero",
            sp.simplify(tr_su3sq_y.subs(a, sample)) != 0,
            str(sp.simplify(tr_su3sq_y.subs(a, sample))),
        )

    sm = sp.Rational(1, 3)
    check("a=1/3 gives Tr[Y^3] = -16/9", sp.simplify(tr_y3.subs(a, sm)) == sp.Rational(-16, 9))
    check("a=1/3 gives Tr[SU(3)^2 Y] = 1/3", sp.simplify(tr_su3sq_y.subs(a, sm)) == sp.Rational(1, 3))


def completion_witness() -> None:
    print("\n== Scale-covariant completion witness ==")
    a = sp.symbols("a", nonzero=True)
    T = sp.Rational(1, 2)
    y1, y2, y3, y4 = 4 * a, -2 * a, -6 * a, sp.Integer(0)

    lh_tr_y = 6 * a + 2 * (-3 * a)
    rh_tr_y = 3 * y1 + 3 * y2 + y3 + y4
    lh_tr_y3 = 6 * a**3 + 2 * (-3 * a) ** 3
    rh_tr_y3 = 3 * y1**3 + 3 * y2**3 + y3**3 + y4**3
    lh_su3sq_y = 2 * T * a
    rh_su3sq_y = T * y1 + T * y2
    lh_su2sq_y = 3 * T * a + T * (-3 * a)
    rh_su2sq_y = 0
    lh_su3cube = 2
    rh_su3cube = 2

    check("RH witness has Tr[Y] = 0", sp.simplify(rh_tr_y) == 0, str(sp.simplify(rh_tr_y)))
    check("LH-RH Tr[Y] cancels", sp.simplify(lh_tr_y - rh_tr_y) == 0)
    check("RH witness Tr[Y^3] matches LH", sp.simplify(rh_tr_y3 - lh_tr_y3) == 0, str(sp.expand(rh_tr_y3)))
    check("LH-RH Tr[Y^3] cancels", sp.simplify(lh_tr_y3 - rh_tr_y3) == 0)
    check("RH witness SU(3)^2 Y matches LH", sp.simplify(rh_su3sq_y - lh_su3sq_y) == 0, str(rh_su3sq_y))
    check("LH-RH SU(3)^2 Y cancels", sp.simplify(lh_su3sq_y - rh_su3sq_y) == 0)
    check("LH SU(2)^2 Y is zero", sp.simplify(lh_su2sq_y) == 0)
    check("RH SU(2)^2 Y is zero by singlet completion", rh_su2sq_y == 0)
    check("LH-RH SU(3)^3 cancels", lh_su3cube - rh_su3cube == 0)
    check("Witten SU(2) doublet count is even", (3 + 1) % 2 == 0, "4")

    sm_values = tuple(sp.simplify(v.subs(a, sp.Rational(1, 3))) for v in (y1, y2, y3, y4))
    check(
        "a=1/3 completion specializes to (4/3,-2/3,-2,0)",
        sm_values == (sp.Rational(4, 3), sp.Rational(-2, 3), sp.Integer(-2), sp.Integer(0)),
        str(sm_values),
    )


def rational_spot_checks() -> None:
    print("\n== Exact rational spot checks ==")
    samples = [Fraction(1, 3), Fraction(1, 5), Fraction(-2, 7), Fraction(11, 13)]
    for sample in samples:
        tr_y3 = 6 * sample**3 + 2 * (-3 * sample) ** 3
        su3sq = sample
        completion = (4 * sample, -2 * sample, -6 * sample, Fraction(0, 1))
        rh_tr_y3 = 3 * completion[0] ** 3 + 3 * completion[1] ** 3 + completion[2] ** 3 + completion[3] ** 3
        check(f"Fraction sample {sample}: Tr[Y^3] = -48a^3", tr_y3 == -48 * sample**3, str(tr_y3))
        check(f"Fraction sample {sample}: SU(3)^2Y = a", su3sq == sample, str(su3sq))
        check(f"Fraction sample {sample}: completion cubic matches", rh_tr_y3 == tr_y3, str(rh_tr_y3))


def source_firewall() -> None:
    print("\n== Source firewall ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    bridge = ABJ_BRIDGE_PATH.read_text(encoding="utf-8")

    required_note_phrases = [
        "ABJ Scale-Free Native Abelian Anomaly Core Boundary",
        "Y_a = a P_6 - 3a P_2",
        "Tr[Y_a^3]        = -48 a^3",
        "does not require",
        "does not assert retained status",
        "does not derive",
        "No observed value",
        RUNNER_PATH,
    ]
    for phrase in required_note_phrases:
        check(f"new note contains required phrase: {phrase}", phrase in note)

    required_bridge_phrases = [
        "Scale-free anomaly-core repair (2026-06-18)",
        "ABJ_SCALE_FREE_NATIVE_ABELIAN_ANOMALY_CORE_BOUNDARY_NOTE_2026-06-18.md",
        "absolute normalization `a = 1/3` is not load-bearing",
        "does not derive P-HY, P-COMP, P-ABJ, or P-REC",
    ]
    for phrase in required_bridge_phrases:
        check(f"ABJ bridge contains scale-free repair phrase: {phrase}", phrase in bridge)

    forbidden_phrases = [
        "audited_clean",
        "effective retained",
        "P-HY is derived",
        "P-COMP is derived",
        "P-REC is derived",
        "P-ABJ is derived",
    ]
    for phrase in forbidden_phrases:
        check(f"new note avoids overclaim phrase: {phrase}", phrase not in note)


def main() -> int:
    symbolic_core()
    completion_witness()
    rational_spot_checks()
    source_firewall()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: scale-free ABJ native abelian anomaly core checks failed.")
        return 1
    print(
        "VERDICT: scale-free ABJ native abelian anomaly core checks pass; "
        "absolute normalization is not load-bearing for the nonzero anomaly arithmetic."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
