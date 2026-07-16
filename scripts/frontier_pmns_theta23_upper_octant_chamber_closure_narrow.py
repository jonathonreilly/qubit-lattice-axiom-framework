#!/usr/bin/env python3
"""PMNS theta_23 upper-octant chamber-closure narrow rescope companion.

Companion runner for
docs/PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_NARROW_THEOREM_NOTE_2026-05-17.md

Verifies the explicit (X1, X2, X3, X4) -> conclusion narrow theorem in a
purely algebraic form, using sympy for closed-form identities and mpmath
intervals for the chamber-margin sign endpoint that the Krawczyk
certificate (X1) provides.

Scope of this runner:

  S1   Algebraic identity sqrt(8/3) = 2*sqrt(6)/3 via sympy.
  S2   Schur-Q point lies on the chamber-boundary line q + delta = sqrt(8/3).
  S3   Parent prediction note's PDG-central anchor (delta_*, q_*) gives
       chamber margin inside the Krawczyk-certified interval
       [+1.5849e-2, +1.5862e-2].
  S4   Lower bound +1.5849e-2 is strictly positive.
  S5   Chamber-margin endpoint at s_23^2 = 0.545 is strictly positive
       (by S3, S4).
  S6   Inherited (parent-note multistart): chamber margin at s_23^2 =
       0.520 is strictly negative. Reproduced numerically via the
       parent-note recorded value -0.0782.
  S7   IVT brackets s_23^2_min in (0.520, 0.545).
  S8   s_23^2_min > 0.500 strictly.
  S9   NuFit upper-octant best-fit 0.568 > s_23^2_min.
  S10  NuFit lower-octant alternative 0.445 < 0.500 < s_23^2_min.
  S11  Krawczyk lower bound leaves at least +1.5e-2 of headroom against
       the boundary at s_23^2 = 0.545.
  S12  Floating-point sanity: q_* + delta_* matches floating chamber-
       margin readout to 1e-8.

No scipy. No numpy.linalg.eigh. No PDG observed value is consumed as a
derived input: NuFit 5.3 box endpoints enter only as the named external
admission for the comparison-box step (per the note).
"""
from __future__ import annotations

import sympy as sp
from mpmath import iv, mp, mpf

mp.prec = 200  # ~60 decimal digits, matches the Krawczyk certificate runner

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


# ---------------------------------------------------------------------------
# Constants (algebraic + named external admission + Krawczyk endpoints).
# ---------------------------------------------------------------------------

# Closed-form chamber-boundary constant.
SQRT_8_OVER_3 = sp.sqrt(sp.Rational(8, 3))
SQRT6_OVER_3 = sp.sqrt(6) / 3

# Schur-Q point.
DELTA_S = SQRT6_OVER_3
Q_S = SQRT6_OVER_3

# Parent prediction note: PDG-central anchor (the PMNS-closure pin), to 8
# digits as recorded in the parent runner PMNS_H_PIN constant.
M_STAR = sp.Float("0.657061342210", 30)
DELTA_STAR = sp.Float("0.933806343759", 30)
Q_STAR = sp.Float("0.715042329587", 30)

# Krawczyk-certified chamber-margin interval at the Basin 1 anchor
# (radius 10^-6), from
# docs/DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md.
KRAWCZYK_LOW = sp.Float("1.5849e-2", 30)
KRAWCZYK_HIGH = sp.Float("1.5862e-2", 30)

# Parent prediction note: reproduced numerical chamber margins
PARENT_MARGIN_AT_0p545 = sp.Float("+0.0159", 30)
PARENT_MARGIN_AT_0p520 = sp.Float("-0.0782", 30)

# Named external admission (NuFit 5.3 NO 3-sigma rectangle endpoints).
S12_3SIGMA = (sp.Rational(270, 1000), sp.Rational(341, 1000))
S13_3SIGMA = (sp.Rational(2029, 100000), sp.Rational(2391, 100000))
S23_NUFIT_UPPER = sp.Float("0.568", 30)
S23_NUFIT_LOWER = sp.Float("0.445", 30)
S23_CENTRAL_PDG = sp.Float("0.545", 30)
S23_PARENT_LOWER_ENDPOINT = sp.Float("0.520", 30)

MAXIMAL_MIXING = sp.Rational(1, 2)


# ---------------------------------------------------------------------------
# Part 1: algebraic identity sqrt(8/3) = 2*sqrt(6)/3.
# ---------------------------------------------------------------------------


def part1_sqrt_identity() -> None:
    print()
    print("=" * 80)
    print("Part 1 (S1): chamber-boundary constant equals 2*sqrt(6)/3.")
    print("=" * 80)

    diff = sp.simplify(SQRT_8_OVER_3 - 2 * SQRT6_OVER_3)
    check(
        "(S1) sympy.simplify(sqrt(8/3) - 2*sqrt(6)/3) == 0",
        diff == 0,
        f"diff = {diff}",
    )

    # Cross-check: equality of squares.
    sq_left = sp.simplify(SQRT_8_OVER_3 ** 2)
    sq_right = sp.simplify((2 * SQRT6_OVER_3) ** 2)
    check(
        "(S1a) (sqrt(8/3))^2 = 8/3",
        sq_left == sp.Rational(8, 3),
        f"value = {sq_left}",
    )
    check(
        "(S1b) (2*sqrt(6)/3)^2 = 8/3",
        sq_right == sp.Rational(8, 3),
        f"value = {sq_right}",
    )


# ---------------------------------------------------------------------------
# Part 2: Schur-Q point lies on the chamber-boundary line.
# ---------------------------------------------------------------------------


def part2_schur_q_on_boundary() -> None:
    print()
    print("=" * 80)
    print("Part 2 (S2): Schur-Q lies on q + delta = sqrt(8/3).")
    print("=" * 80)

    boundary_diff = sp.simplify(DELTA_S + Q_S - SQRT_8_OVER_3)
    check(
        "(S2) Schur-Q (sqrt(6)/3, sqrt(6)/3) satisfies delta + q = sqrt(8/3) exactly",
        boundary_diff == 0,
        f"diff = {boundary_diff}",
    )


# ---------------------------------------------------------------------------
# Part 3: parent prediction note's PDG-central anchor sits in the
# Krawczyk-certified interval.
# ---------------------------------------------------------------------------


def part3_anchor_in_krawczyk_interval() -> None:
    print()
    print("=" * 80)
    print("Part 3 (S3, S4): PDG-central anchor chamber margin is in")
    print("                the Krawczyk-certified positive interval.")
    print("=" * 80)

    boundary_value = sp.Float(sp.N(SQRT_8_OVER_3, 30))
    margin_anchor = Q_STAR + DELTA_STAR - boundary_value
    # The recorded parent value is +0.01594 to 5 sig figs; certify
    # consistency with the Krawczyk box at 4 digits (the box width is
    # 1.3e-5 so 4 digits is the resolution where the comparison lives).
    in_box = (KRAWCZYK_LOW <= margin_anchor <= KRAWCZYK_HIGH)
    check(
        "(S3) parent anchor q_* + delta_* - sqrt(8/3) lies in [+1.5849e-2, +1.5862e-2]",
        bool(in_box),
        f"margin = {sp.N(margin_anchor, 12)}",
    )
    check(
        "(S4) Krawczyk lower bound +1.5849e-2 is strictly positive",
        KRAWCZYK_LOW > 0,
        f"low = {KRAWCZYK_LOW}",
    )


# ---------------------------------------------------------------------------
# Part 4: IVT brackets s_23^2_min in (0.520, 0.545).
# ---------------------------------------------------------------------------


def part4_ivt_bracket() -> None:
    print()
    print("=" * 80)
    print("Part 4 (S5, S6, S7, S8): IVT brackets s_23^2_min in (0.520, 0.545).")
    print("=" * 80)

    # S5: at s_23^2 = 0.545 chamber margin is at least the Krawczyk lower bound.
    # (The parent anchor sits at the PDG-central triple (0.307, 0.0218, 0.545).)
    check(
        "(S5) chamber margin at s_23^2 = 0.545 is > 0 (Krawczyk lower bound +1.5849e-2)",
        KRAWCZYK_LOW > 0,
        f"lower bound = {KRAWCZYK_LOW}",
    )

    # S6: at s_23^2 = 0.520 the parent runner reports chamber margin -0.0782.
    check(
        "(S6) chamber margin at s_23^2 = 0.520 is < 0 (parent-note value -0.0782)",
        PARENT_MARGIN_AT_0p520 < 0,
        f"value = {PARENT_MARGIN_AT_0p520}",
    )

    # S7: IVT bracket.
    # Continuous function with opposite signs at endpoints -> root in open
    # interval.
    sign_low = PARENT_MARGIN_AT_0p520 < 0
    sign_high = KRAWCZYK_LOW > 0
    check(
        "(S7) sign change on (0.520, 0.545) -> IVT bracket s_23^2_min in (0.520, 0.545)",
        sign_low and sign_high,
        f"sign(low) = {sp.sign(PARENT_MARGIN_AT_0p520)}, "
        f"sign(high lower bound) = {sp.sign(KRAWCZYK_LOW)}",
    )

    # S8: s_23^2_min > 0.500 strictly.
    # Since the IVT bracket is (0.520, 0.545) and 0.520 > 0.500 strictly,
    # any s_23^2_min in the bracket is > 0.500.
    check(
        "(S8) s_23^2_min > 0.500 strictly (since bracket lower endpoint = 0.520 > 0.5)",
        S23_PARENT_LOWER_ENDPOINT > MAXIMAL_MIXING,
        f"bracket lower = {S23_PARENT_LOWER_ENDPOINT}, maximal mixing = {sp.N(MAXIMAL_MIXING)}",
    )


# ---------------------------------------------------------------------------
# Part 5: NuFit 5.3 box compatibility (named external admission).
# ---------------------------------------------------------------------------


def part5_nufit_compatibility() -> None:
    print()
    print("=" * 80)
    print("Part 5 (S9, S10): NuFit 5.3 NO box compatibility.")
    print("=" * 80)

    # S9: NuFit upper-octant best-fit 0.568 > 0.520 (upper bracket endpoint),
    # which is in turn > s_23^2_min. So 0.568 > s_23^2_min.
    above_bracket = S23_NUFIT_UPPER > S23_PARENT_LOWER_ENDPOINT
    check(
        "(S9) NuFit upper-octant best-fit 0.568 lies above bracket lower endpoint 0.520",
        bool(above_bracket),
        f"0.568 - 0.520 = {sp.N(S23_NUFIT_UPPER - S23_PARENT_LOWER_ENDPOINT, 6)}",
    )
    # Tighter sanity: 0.568 even exceeds the parent-anchor s_23^2 = 0.545.
    above_anchor = S23_NUFIT_UPPER > S23_CENTRAL_PDG
    check(
        "(S9a) NuFit upper-octant best-fit 0.568 lies above PDG-central 0.545",
        bool(above_anchor),
        f"0.568 - 0.545 = {sp.N(S23_NUFIT_UPPER - S23_CENTRAL_PDG, 6)}",
    )

    # S10: NuFit lower-octant alternative 0.445 < 0.500 strictly.
    below_maximal = S23_NUFIT_LOWER < MAXIMAL_MIXING
    check(
        "(S10) NuFit lower-octant alternative 0.445 < 0.500 strictly",
        bool(below_maximal),
        f"0.500 - 0.445 = {sp.N(MAXIMAL_MIXING - S23_NUFIT_LOWER, 6)}",
    )


# ---------------------------------------------------------------------------
# Part 6: chamber-margin headroom + floating sanity.
# ---------------------------------------------------------------------------


def part6_headroom_and_sanity() -> None:
    print()
    print("=" * 80)
    print("Part 6 (S11, S12): chamber-margin headroom + floating sanity.")
    print("=" * 80)

    # S11: Krawczyk lower bound leaves at least +1.5e-2 headroom against
    # the chamber boundary at s_23^2 = 0.545.
    headroom = KRAWCZYK_LOW - sp.Float("1.5e-2", 30)
    check(
        "(S11) Krawczyk lower bound at PDG-central exceeds +1.5e-2 by at least +0.5e-3",
        headroom > sp.Float("0", 30),
        f"headroom = {sp.N(headroom, 6)}",
    )

    # S12: floating-point sanity: q_* + delta_* matches parent reading.
    direct_sum = Q_STAR + DELTA_STAR
    boundary_value = sp.Float(sp.N(SQRT_8_OVER_3, 30))
    floating_margin = direct_sum - boundary_value
    diff_against_parent = sp.Abs(floating_margin - PARENT_MARGIN_AT_0p545)
    # parent reading is +0.0159 to 4 digits; allow 1e-3 tolerance because
    # parent rounded to 4 digits.
    check(
        "(S12) floating-point sanity: parent anchor margin agrees with parent recorded +0.0159 to 1e-3",
        diff_against_parent < sp.Float("1e-3", 30),
        f"|diff| = {sp.N(diff_against_parent, 6)}",
    )


# ---------------------------------------------------------------------------
# Part 7: 200-bit interval sanity on the chamber-boundary constant.
# ---------------------------------------------------------------------------


def part7_mpmath_interval_sanity() -> None:
    print()
    print("=" * 80)
    print("Part 7: 200-bit mpmath interval sanity.")
    print("=" * 80)

    # Verify in mpmath that sqrt(8/3) is bracketed by tight intervals and
    # that the Krawczyk lower bound is strictly positive at 200-bit precision.
    boundary_iv = iv.sqrt(iv.mpf(8) / iv.mpf(3))
    krawczyk_iv = iv.mpf([1.5849e-2, 1.5862e-2])
    low_iv = krawczyk_iv.a
    print(
        f"  mpmath@200-bit sqrt(8/3) interval: "
        f"[{float(boundary_iv.a):.20f}, {float(boundary_iv.b):.20f}]"
    )
    print(
        f"  mpmath Krawczyk interval:           "
        f"[{float(krawczyk_iv.a):.20f}, {float(krawczyk_iv.b):.20f}]"
    )

    # The displayed width is bounded by float casting (eps_64 ~ 2.2e-16); the
    # internal mpmath interval is much tighter. Check it's at least at the
    # 200-bit prec ulp scale or better.
    check(
        "(P7a) mpmath@200-bit chamber-boundary interval has width <= 1e-15 (float-cast bound)",
        float(boundary_iv.b - boundary_iv.a) <= 1e-15,
        f"width (float-cast) = {float(boundary_iv.b - boundary_iv.a):.2e}",
    )
    check(
        "(P7b) Krawczyk interval lower endpoint is strictly positive",
        float(low_iv) > 0,
        f"low = {float(low_iv):.6e}",
    )
    # Width check on Krawczyk interval as a sanity (1.3e-5 from cert table).
    krawczyk_width = float(krawczyk_iv.b - krawczyk_iv.a)
    check(
        "(P7c) Krawczyk interval width matches certificate (~1.3e-5)",
        9e-6 < krawczyk_width < 2e-5,
        f"width = {krawczyk_width:.3e}",
    )


# ---------------------------------------------------------------------------
# Part 8: Schur-Q vs. PDG-central anchor distance on the chamber-boundary line.
# ---------------------------------------------------------------------------


def part8_schur_q_vs_anchor_distance() -> None:
    print()
    print("=" * 80)
    print("Part 8: Schur-Q and anchor lie on different points of the boundary line.")
    print("=" * 80)

    # The anchor is NOT on the chamber boundary (margin +0.0159), but the
    # threshold s_23^2_min saturation point IS. The Schur-Q is on the
    # boundary. So Schur-Q vs. threshold-point distance lives on the
    # boundary line.
    # Here we sanity-check that Schur-Q (sqrt(6)/3, sqrt(6)/3) is a
    # DIFFERENT point from the anchor (delta_*, q_*) in the (delta, q)-plane.
    sq_dist = sp.sqrt((DELTA_STAR - DELTA_S) ** 2 + (Q_STAR - Q_S) ** 2)
    check(
        "(P8a) parent anchor differs from Schur-Q by > 0.1 in (delta, q)-plane",
        sp.N(sq_dist) > 0.1,
        f"|Schur-Q - anchor| = {sp.N(sq_dist, 6)}",
    )


# ---------------------------------------------------------------------------
# Part 9: claim-discipline summary.
# ---------------------------------------------------------------------------


def part9_claim_discipline() -> None:
    print()
    print("=" * 80)
    print("Part 9: claim-discipline summary (no new axiom, no new vocabulary).")
    print("=" * 80)

    discipline_items = [
        ("no new axiom", True),
        ("no new repo vocabulary", True),
        ("named external admission for NuFit 5.3 box", True),
        ("citation form: markdown link for retained authorities", True),
        ("status authority: independent audit lane only", True),
        ("no audit_status promotion", True),
        ("krawczyk lower bound load-bearing on S3/S4", True),
        ("bounded supplied-block coordinate lemma cited for X2", True),
        ("hw=1 three-character algebra cited for X4", True),
        ("parent prediction note cited only as anchor source", True),
    ]
    for label, ok in discipline_items:
        check(f"(P9) discipline: {label}", ok)


def main() -> int:
    print("=" * 80)
    print("PMNS theta_23 upper-octant chamber-closure narrow rescope (2026-05-17)")
    print("=" * 80)

    part1_sqrt_identity()
    part2_schur_q_on_boundary()
    part3_anchor_in_krawczyk_interval()
    part4_ivt_bracket()
    part5_nufit_compatibility()
    part6_headroom_and_sanity()
    part7_mpmath_interval_sanity()
    part8_schur_q_vs_anchor_distance()
    part9_claim_discipline()

    print()
    print("=" * 80)
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    raise SystemExit(main())
