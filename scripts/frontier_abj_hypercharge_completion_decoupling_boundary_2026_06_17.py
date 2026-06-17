#!/usr/bin/env python3
"""ABJ hypercharge/completion decoupling boundary.

This runner proves the exact arithmetic behind the ABJ P-HY/P-COMP boundary:
given the left-handed +1/3 x6, -1 x2 surface and an admitted minimal
SU(2)-singlet RH completion, anomaly cancellation forces the RH hypercharges.

It also checks the honest boundaries: nu_R neutrality, vectorlike/mirror
exclusion, absolute Y scale, physical U(1)_Y identification, and ABJ
anomaly-to-inconsistency are not derived here.
"""

from __future__ import annotations

from fractions import Fraction
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs/ABJ_HYPERCHARGE_COMPLETION_DECOUPLING_BOUNDARY_NOTE_2026-06-17.md"
ABJ_NOTE_PATH = ROOT / "docs/ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
SM_DECOUPLED_NOTE_PATH = ROOT / "docs/SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08.md"
LH_SURFACE_NOTE_PATH = ROOT / "docs/NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md"
NO_NUR_NOTE_PATH = ROOT / "docs/SM_HYPERCHARGE_UNIQUENESS_WITHOUT_NU_R_INPUT_THEOREM_NOTE_2026-05-02.md"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name}")
    if detail:
        print(f"      {detail}")
    PASS += int(condition)
    FAIL += int(not condition)
    return condition


def rational_sqrt(q: Fraction) -> Fraction | None:
    if q < 0:
        return None
    rn = isqrt(q.numerator)
    rd = isqrt(q.denominator)
    if rn * rn == q.numerator and rd * rd == q.denominator:
        return Fraction(rn, rd)
    return None


def tr_y(fields: list[tuple[int, Fraction]]) -> Fraction:
    return sum(m * y for m, y in fields)


def tr_y3(fields: list[tuple[int, Fraction]]) -> Fraction:
    return sum(m * y**3 for m, y in fields)


def all_left_fields(yu: Fraction, yd: Fraction, ye: Fraction, ynu: Fraction | None = None) -> list[tuple[int, Fraction]]:
    """One generation in all-left anomaly bookkeeping.

    RH fields enter as left-conjugates, so their hypercharges are negated.
    """
    fields = [
        (6, Fraction(1, 3)),   # Q_L
        (2, Fraction(-1, 1)),  # L_L
        (3, -yu),              # u_R^c
        (3, -yd),              # d_R^c
        (1, -ye),              # e_R^c
    ]
    if ynu is not None:
        fields.append((1, -ynu))
    return fields


def part0_source_firewall() -> None:
    print("\n== Part 0: source firewall ==")
    note = NOTE_PATH.read_text(encoding="utf-8")
    abj = ABJ_NOTE_PATH.read_text(encoding="utf-8")
    sm_decoupled = SM_DECOUPLED_NOTE_PATH.read_text(encoding="utf-8")
    lh_surface = LH_SURFACE_NOTE_PATH.read_text(encoding="utf-8")
    no_nur = NO_NUR_NOTE_PATH.read_text(encoding="utf-8")

    for phrase in [
        "bounded support / exact boundary",
        "independent audit lane only",
        "without introducing a new axiom",
        "P-HY is still the declared physical identification premise",
        "P-COMP-min",
        "Matter content is not anomaly-unique",
        "The absolute hypercharge scale is a convention",
        "not a retained closure",
    ]:
        check(f"new note contains boundary phrase: {phrase}", phrase in note)

    for phrase in [
        "ABJ_HYPERCHARGE_COMPLETION_DECOUPLING_BOUNDARY_NOTE_2026-06-17.md",
        "P-HY/P-COMP decoupling boundary",
        "does not derive P-HY or P-COMP",
    ]:
        check(f"ABJ bridge routes new boundary phrase: {phrase}", phrase in abj)

    check(
        "left-handed abelian note excludes anomaly-complete U(1)_Y and completion",
        "does not claim anomaly-complete" in lh_surface
        and "right-handed completion" in lh_surface
        and "left-handed eigenvalue surface" in lh_surface,
    )
    check(
        "SM decoupled note records minimal RH completion as admitted, not imported",
        "minimal right-handed" in sm_decoupled
        and "explicit admitted premise rather than imported" in sm_decoupled
        and "imported from `anomaly_forces_time_theorem`" in sm_decoupled,
    )
    check(
        "SM decoupled note contains full nu_R family check, not Tr[Y]-only",
        "y_u = 4/3 + t" in sm_decoupled
        and "y_d = -2/3 - t" in sm_decoupled
        and "Tr[Y^3] = 0" in sm_decoupled,
    )
    check(
        "no-nu_R note proves uniqueness without neutral-singlet input",
        "No neutral-singlet hypercharge" in no_nur
        and "input is needed" in no_nur
        and "No ν_R is included in the minimal completion" in no_nur,
    )

    forbidden = [
        "P-HY is derived",
        "P-COMP is derived",
        "matter completion is derived",
        "is a retained closure",
        "sets the audit verdict",
    ]
    for phrase in forbidden:
        check(f"new note avoids forbidden closure phrase: {phrase}", phrase not in note)


def part1_lh_surface_anomalies() -> None:
    print("\n== Part 1: left-handed surface anomaly traces ==")
    yq = Fraction(1, 3)
    yl = Fraction(-1, 1)
    tf = Fraction(1, 2)

    tr_lh_y = 6 * yq + 2 * yl
    tr_lh_y3 = 6 * yq**3 + 2 * yl**3
    su3sq_y = 2 * tf * yq
    su2sq_y = 3 * tf * yq + tf * yl
    su3_cubic = Fraction(2, 1)

    check("LH Tr[Y] = 0", tr_lh_y == 0, str(tr_lh_y))
    check("LH Tr[Y^3] = -16/9", tr_lh_y3 == Fraction(-16, 9), str(tr_lh_y3))
    check("LH Tr[SU(3)^2 Y] = 1/3", su3sq_y == Fraction(1, 3), str(su3sq_y))
    check("LH Tr[SU(2)^2 Y] = 0", su2sq_y == 0, str(su2sq_y))
    check("LH SU(3)^3 anomaly = +2", su3_cubic == 2, str(su3_cubic))
    check("three ABJ-relevant LH traces are nonzero", all(x != 0 for x in [tr_lh_y3, su3sq_y, su3_cubic]))


def part2_minimal_rh_solution() -> tuple[Fraction, Fraction, Fraction]:
    print("\n== Part 2: minimal RH hypercharge solution ==")
    s = Fraction(2, 3)              # y_u + y_d from SU(3)^2Y
    ye = -3 * s                     # Tr[Y] gives 3s + y_e = 0
    lh_tr_y3 = Fraction(-16, 9)
    sum_cubes = (lh_tr_y3 - ye**3) / 3
    product = (s**3 - sum_cubes) / (3 * s)
    disc = s**2 - 4 * product
    root = rational_sqrt(disc)

    check("RH quadratic discriminant is a rational square", root is not None, f"disc={disc}, sqrt={root}")
    assert root is not None
    yu = (s + root) / 2
    yd = s - yu

    check("minimal RH sum y_u+y_d = 2/3", yu + yd == Fraction(2, 3), f"{yu + yd}")
    check("minimal RH product y_u*y_d = -8/9", yu * yd == Fraction(-8, 9), f"{yu * yd}")
    check("minimal RH y_e = -2", ye == Fraction(-2, 1), f"{ye}")
    check("minimal RH values are {4/3,-2/3,-2}", {yu, yd} == {Fraction(4, 3), Fraction(-2, 3)} and ye == -2)

    # Choose the positive-charge convention for u_R.
    yu, yd = max(yu, yd), min(yu, yd)
    return yu, yd, ye


def part3_full_anomaly_cancellation(yu: Fraction, yd: Fraction, ye: Fraction) -> None:
    print("\n== Part 3: full minimal content anomaly cancellation ==")
    fields = all_left_fields(yu, yd, ye)
    tf = Fraction(1, 2)

    su3_cubic = 2 - 1 - 1
    su2sq_y = tf * (3 * Fraction(1, 3) + Fraction(-1, 1))
    su3sq_y = 2 * tf * Fraction(1, 3) - tf * yu - tf * yd
    witten_doublets = 3 + 1

    check("minimal content Tr[Y] = 0", tr_y(fields) == 0, str(tr_y(fields)))
    check("minimal content Tr[Y^3] = 0", tr_y3(fields) == 0, str(tr_y3(fields)))
    check("minimal content Tr[SU(3)^2Y] = 0", su3sq_y == 0, str(su3sq_y))
    check("minimal content Tr[SU(2)^2Y] = 0", su2sq_y == 0, str(su2sq_y))
    check("minimal content SU(3)^3 = 0", su3_cubic == 0, str(su3_cubic))
    check("minimal content Witten SU(2) doublet count is even", witten_doublets % 2 == 0, str(witten_doublets))
    check("SU(2)^3 cubic is identically zero for SU(2)", True)


def part4_boundaries(yu: Fraction, yd: Fraction, ye: Fraction) -> None:
    print("\n== Part 4: boundary and non-uniqueness checks ==")
    neutral = all_left_fields(yu, yd, ye, Fraction(0, 1))
    check("adding neutral nu_R leaves Tr[Y] zero", tr_y(neutral) == 0, str(tr_y(neutral)))
    check("adding neutral nu_R leaves Tr[Y^3] zero", tr_y3(neutral) == 0, str(tr_y3(neutral)))

    t = Fraction(1, 2)
    fam_yu = Fraction(4, 3) + t
    fam_yd = Fraction(-2, 3) - t
    fam_ye = Fraction(-2, 1) - t
    fam_ynu = t
    family = all_left_fields(fam_yu, fam_yd, fam_ye, fam_ynu)
    family_su3sq_y = 2 * Fraction(1, 2) * Fraction(1, 3) - Fraction(1, 2) * fam_yu - Fraction(1, 2) * fam_yd
    check("free nu_R family cancels Tr[SU(3)^2Y] at t=1/2", family_su3sq_y == 0, str(family_su3sq_y))
    check("free nu_R family cancels Tr[Y] at t=1/2", tr_y(family) == 0, str(tr_y(family)))
    check("free nu_R family cancels Tr[Y^3] at t=1/2", tr_y3(family) == 0, str(tr_y3(family)))

    vectorlike = all_left_fields(yu, yd, ye) + [(1, Fraction(5, 1)), (1, Fraction(-5, 1))]
    check("vectorlike pair preserves Tr[Y] zero", tr_y(vectorlike) == 0, str(tr_y(vectorlike)))
    check("vectorlike pair preserves Tr[Y^3] zero", tr_y3(vectorlike) == 0, str(tr_y3(vectorlike)))

    lam = Fraction(7, 5)
    scaled = [(m, lam * y) for m, y in all_left_fields(yu, yd, ye)]
    check("global Y-scale rescaling preserves Tr[Y] zero", tr_y(scaled) == 0, str(tr_y(scaled)))
    check("global Y-scale rescaling preserves Tr[Y^3] zero", tr_y3(scaled) == 0, str(tr_y3(scaled)))


def main() -> int:
    print("ABJ HYPERCHARGE/COMPLETION DECOUPLING BOUNDARY")
    part0_source_firewall()
    part1_lh_surface_anomalies()
    yu, yd, ye = part2_minimal_rh_solution()
    part3_full_anomaly_cancellation(yu, yd, ye)
    part4_boundaries(yu, yd, ye)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: bounded ABJ hypercharge/completion decoupling boundary passes.")
        return 0
    print("VERDICT: bounded ABJ hypercharge/completion decoupling boundary FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
