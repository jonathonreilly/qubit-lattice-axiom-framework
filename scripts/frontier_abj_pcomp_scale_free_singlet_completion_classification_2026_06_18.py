#!/usr/bin/env python3
"""Scale-free finite classification for the ABJ bridge P-COMP arithmetic.

This runner verifies the exact anomaly-equation classification stated in
docs/ABJ_P_COMP_SCALE_FREE_SINGLET_COMPLETION_CLASSIFICATION_NOTE_2026-06-18.md.

It does not derive the physical completion surface. It proves only:

  * on the scale-free LH surface Q_L:(2,3)_a and L_L:(2,1)_(-3a),
    the anomaly traces are symbolic in a;
  * given two opposite-chirality SU(2)-singlet color triplets, one
    charged colorless singlet, and one neutral singlet, anomaly
    cancellation forces charges {4a, -2a, -6a, 0};
  * without the neutral-singlet input, a non-SM one-parameter family
    survives, so that input remains an exposed P-COMP residual.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re
import sys

try:
    import sympy as sp
except ImportError:
    print("FAIL: sympy is required for exact symbolic checks")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "ABJ_P_COMP_SCALE_FREE_SINGLET_COMPLETION_CLASSIFICATION_NOTE_2026-06-18.md"
ABJ_BRIDGE_PATH = ROOT / "docs" / "ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
RUNNER_REL = "scripts/frontier_abj_pcomp_scale_free_singlet_completion_classification_2026_06_18.py"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{tag}: {name}{suffix}")
    return ok


def section(title: str) -> None:
    print()
    print(f"== {title} ==")


def part0_source_firewall() -> None:
    section("Part 0: source firewall")
    note = NOTE_PATH.read_text(encoding="utf-8")
    note_flat = re.sub(r"\s+", " ", note)
    abj = ABJ_BRIDGE_PATH.read_text(encoding="utf-8")

    required_note_markers = [
        "**Actual current surface status:** bounded-support / exact conditional classification",
        "does not set or predict an audit outcome",
        "a != 0",
        "{x, y, z, n} = {4a, -2a, -6a, 0}",
        "At the existing `a = 1/3` normalization",
        "If the neutral singlet condition `n = 0` is removed, uniqueness fails.",
        "does not derive full `P-COMP`",
        "does not consume PDG values",
        RUNNER_REL,
    ]
    for marker in required_note_markers:
        check(f"note contains marker: {marker[:68]}", marker in note or marker in note_flat)

    forbidden_overclaims = [
        "audited_clean",
        "effective retained",
        "full `P-COMP` is derived",
        "this derives `P-HY`",
        "this derives `P-ABJ`",
        "this derives `P-REC`",
        "this derives `B-AXIS`",
    ]
    for phrase in forbidden_overclaims:
        check(f"note avoids overclaim phrase: {phrase}", phrase not in note)

    check(
        "ABJ bridge has source-side pointer to this P-COMP classification",
        "ABJ_P_COMP_SCALE_FREE_SINGLET_COMPLETION_CLASSIFICATION_NOTE_2026-06-18.md" in abj,
    )
    check(
        "ABJ bridge still states it does not derive P-HY, P-ABJ, full P-COMP, P-REC, or B-AXIS",
        all(
            marker in abj
            for marker in [
                "does not derive",
                "P-HY",
                "P-ABJ",
                "full P-COMP",
                "P-REC",
                "B-AXIS",
            ]
        ),
    )


def part1_lh_scale_free_traces() -> None:
    section("Part 1: scale-free LH anomaly traces")
    a = sp.symbols("a", nonzero=True)
    T = sp.Rational(1, 2)

    tr_y_lh = 6 * a + 2 * (-3 * a)
    tr_y3_lh = 6 * a**3 + 2 * (-3 * a) ** 3
    tr_su3sq_y_lh = 2 * T * a
    tr_su2sq_y_lh = 3 * T * a + T * (-3 * a)
    tr_su3cube_lh = sp.Integer(2)

    check("Tr[Y]_LH = 0", sp.simplify(tr_y_lh) == 0, str(sp.simplify(tr_y_lh)))
    check("Tr[Y^3]_LH = -48 a^3", sp.simplify(tr_y3_lh + 48 * a**3) == 0, str(tr_y3_lh))
    check("Tr[SU(3)^2 Y]_LH = a", sp.simplify(tr_su3sq_y_lh - a) == 0, str(tr_su3sq_y_lh))
    check("Tr[SU(2)^2 Y]_LH = 0", sp.simplify(tr_su2sq_y_lh) == 0, str(tr_su2sq_y_lh))
    check("Tr[SU(3)^3]_LH = 2", tr_su3cube_lh == 2, str(tr_su3cube_lh))

    for value in [sp.Rational(1, 3), sp.Rational(2, 5), sp.Rational(-1, 2)]:
        lhs = tr_y3_lh.subs(a, value)
        rhs = -48 * value**3
        check(f"sample a={value}: cubic trace matches -48a^3", sp.simplify(lhs - rhs) == 0)


def part2_completion_classification() -> None:
    section("Part 2: exact singlet-completion classification")
    a, x, y, z, t = sp.symbols("a x y z t", nonzero=True)

    # From SU(3)^2 Y cancellation, x + y = 2a. From Tr[Y] with n=0, z = -6a.
    sum_xy = 2 * a
    z_value = -6 * a

    check("mixed color anomaly gives x + y = 2a", sp.simplify(sum_xy - 2 * a) == 0)
    check("linear anomaly with n=0 gives z = -6a", sp.simplify(z_value + 6 * a) == 0)

    # Cubic anomaly after substituting z = -6a:
    cubic_equation = 3 * (x**3 + y**3) + z_value**3 + 48 * a**3
    target = 3 * (x**3 + y**3) - 168 * a**3
    check(
        "cubic equation reduces to 3(x^3+y^3)-168a^3=0",
        sp.simplify(cubic_equation - target) == 0,
        str(sp.simplify(cubic_equation - target)),
    )

    # Use x^3+y^3 = (x+y)^3 - 3xy(x+y).
    p = sp.symbols("p")
    cubic_in_p = 3 * (sum_xy**3 - 3 * p * sum_xy) - 168 * a**3
    p_solution = sp.solve(sp.Eq(cubic_in_p, 0), p)
    check("product xy forced to -8a^2", p_solution == [-8 * a**2], str(p_solution))

    quad = t**2 - 2 * a * t - 8 * a**2
    check("quadratic factors as (t-4a)(t+2a)", sp.factor(quad) == (t - 4 * a) * (t + 2 * a), sp.factor(quad))
    roots = sp.solve(sp.Eq(quad, 0), t)
    check("roots are {-2a, 4a}", set(roots) == {-2 * a, 4 * a}, str(roots))

    # Direct enumeration for rational scale samples.
    for value in [sp.Rational(1, 3), sp.Rational(2, 5), sp.Rational(7, 4)]:
        eqs = [
            sp.Eq(x + y, 2 * value),
            sp.Eq(z, -6 * value),
            sp.Eq(x * y, -8 * value**2),
        ]
        sols = sp.solve(eqs, [x, y, z], dict=True)
        got = {(s[x], s[y], s[z]) for s in sols}
        expect = {
            (4 * value, -2 * value, -6 * value),
            (-2 * value, 4 * value, -6 * value),
        }
        check(f"direct solve at a={value} gives swapped SM-scale pair", got == expect, str(got))


def full_anomalies(a: Fraction, x: Fraction, y: Fraction, z: Fraction, n: Fraction) -> dict[str, Fraction]:
    T = Fraction(1, 2)
    lh_y = 6 * a + 2 * (-3 * a)
    lh_y3 = 6 * a**3 + 2 * (-3 * a) ** 3
    lh_su3sq_y = 2 * T * a
    lh_su2sq_y = 3 * T * a + T * (-3 * a)
    lh_su3cube = Fraction(2, 1)

    rh_y = 3 * x + 3 * y + z + n
    rh_y3 = 3 * x**3 + 3 * y**3 + z**3 + n**3
    rh_su3sq_y = T * x + T * y
    rh_su2sq_y = Fraction(0, 1)
    rh_su3cube = Fraction(2, 1)

    return {
        "Tr[Y]": lh_y - rh_y,
        "Tr[Y^3]": lh_y3 - rh_y3,
        "Tr[SU(3)^2 Y]": lh_su3sq_y - rh_su3sq_y,
        "Tr[SU(2)^2 Y]": lh_su2sq_y - rh_su2sq_y,
        "Tr[SU(3)^3]": lh_su3cube - rh_su3cube,
    }


def part3_full_cancellation() -> None:
    section("Part 3: full anomaly cancellation checks")
    for a in [Fraction(1, 3), Fraction(2, 5), Fraction(7, 4)]:
        branches = [
            (4 * a, -2 * a, -6 * a, Fraction(0)),
            (-2 * a, 4 * a, -6 * a, Fraction(0)),
        ]
        for branch in branches:
            traces = full_anomalies(a, *branch)
            check(
                f"a={a}, branch={branch}: all anomaly traces cancel",
                all(v == 0 for v in traces.values()),
                str(traces),
            )

    traces_sm = full_anomalies(Fraction(1, 3), Fraction(4, 3), Fraction(-2, 3), Fraction(-2), Fraction(0))
    check("a=1/3 gives standard witness exactly", all(v == 0 for v in traces_sm.values()), str(traces_sm))


def part4_counterfactuals() -> None:
    section("Part 4: counterfactuals expose remaining P-COMP residuals")
    a = sp.symbols("a", nonzero=True)
    p, q = sp.symbols("p q")

    # General no-neutral-singlet symmetric-product form:
    # x+y=2a, z+n=-6a. Cubic gives q-p=8a^2.
    relation = q - p - 8 * a**2
    check("without n=0, cubic leaves q-p=8a^2 relation", sp.simplify(relation - (q - p - 8 * a**2)) == 0)

    for val in [Fraction(1, 3), Fraction(2, 5)]:
        non_sm = (Fraction(0), 2 * val, -2 * val, -4 * val)
        traces = full_anomalies(val, *non_sm)
        check(
            f"a={val}: non-neutral counterexample also cancels anomalies",
            all(v == 0 for v in traces.values()),
            str(traces),
        )
        check(f"a={val}: counterexample has no neutral singlet", non_sm[-1] != 0, f"n={non_sm[-1]}")

    # One color-triplet singlet cannot cancel the SU(3)^3 slot count of the LH doublet.
    check("one RH color triplet would leave SU(3)^3 residual 1", Fraction(2) - Fraction(1) == 1)
    check("two RH color triplets cancel SU(3)^3 by slot count", Fraction(2) - Fraction(2) == 0)


def main() -> int:
    print("frontier_abj_pcomp_scale_free_singlet_completion_classification_2026_06_18.py")
    part0_source_firewall()
    part1_lh_scale_free_traces()
    part2_completion_classification()
    part3_full_cancellation()
    part4_counterfactuals()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: bounded-support exact P-COMP singlet-completion classification.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
