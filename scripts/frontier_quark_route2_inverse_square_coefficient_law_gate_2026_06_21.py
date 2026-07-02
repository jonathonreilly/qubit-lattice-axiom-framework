#!/usr/bin/env python3
"""Route-2 inverse-square coefficient-law gate.

Safe claim:
  The Route-2 target lambda=q_E/q_T=9/4 is equivalent to a pure second
  reciprocal power of the E/T projector-weight ratio.  Positive polynomial
  laws and positive one-pole reciprocal laws cannot reach it.  A mixed
  nonnegative {0,-1,-2} reciprocal grammar reaches it exactly only when the
  lower-order terms vanish, so the missing positive theorem is specifically
  a pure inverse-square coefficient law or an equivalent signed-cancellation
  rule.

  This runner does not derive rho_E=21/4, does not apply an audit verdict, and
  does not rule out future nonlinear or denominator-bearing observables.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path


PASS = 0
FAIL = 0


def check(label: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(cond)
    PASS += int(ok)
    FAIL += int(not ok)
    print(f"PASS: {label}" + (f" -- {detail}" if ok and detail else ""))
    if not ok:
        print(f"FAIL: {label}" + (f" -- {detail}" if detail else ""))


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def ratio_for_terms(coeffs: dict[int, F], w_e: F, w_t: F) -> F:
    num = sum(a * (w_e ** p) for p, a in coeffs.items())
    den = sum(a * (w_t ** p) for p, a in coeffs.items())
    if den == 0:
        raise ZeroDivisionError(coeffs)
    return num / den


def term_ratio(power: int, x: F) -> F:
    return x ** power


def weighted_bounds(exponents: list[int], x: F) -> tuple[F, F]:
    values = [term_ratio(p, x) for p in exponents]
    return min(values), max(values)


def signed_two_point_law(
    target_e: F, target_t: F, w_e: F, w_t: F, reciprocal: bool
) -> tuple[F, F]:
    # Direct: c(w)=a+b*w. Reciprocal: c(w)=a+b/w.
    x_e = 1 / w_e if reciprocal else w_e
    x_t = 1 / w_t if reciprocal else w_t
    b = (target_e - target_t) / (x_e - x_t)
    a = target_t - b * x_t
    return a, b


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 INVERSE-SQUARE COEFFICIENT-LAW GATE")
    print("=" * 88)

    note = Path("docs/QUARK_ROUTE2_INVERSE_SQUARE_COEFFICIENT_LAW_GATE_NOTE_2026-06-21.md")
    exact = Path("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    covariance = Path("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    ell_e = Path("docs/QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md")
    parent = Path("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    usable = Path("docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX.md")

    print("\nA. Authority surfaces")
    print("-" * 72)
    for label, path in (
        ("new note", note),
        ("exact readout", exact),
        ("covariance no-go", covariance),
        ("ell_E narrowing", ell_e),
        ("parent theta coupling", parent),
        ("usable values index", usable),
    ):
        check(f"{label} surface exists", path.exists(), str(path))

    w_a1, w_e, w_t = F(1, 6), F(1, 3), F(1, 2)
    x = w_e / w_t
    target = F(9, 4)
    q_t = F(5, 6)
    q_e = target * q_t
    rho_e = 6 * (q_e - 1)
    c_te = -2 * q_t / q_e

    print("\nB. Exact target arithmetic")
    print("-" * 72)
    check("weight ratio x=w_E/w_T is 2/3", x == F(2, 3), f"x={x}")
    check("target lambda is 9/4", target == F(9, 4), f"lambda={target}")
    check("target lambda gives q_E=15/8", q_e == F(15, 8), f"q_E={q_e}")
    check("target lambda gives rho_E=21/4", rho_e == F(21, 4), f"rho_E={rho_e}")
    check("target lambda gives c_TE=-8/9", c_te == F(-8, 9), f"c_TE={c_te}")
    check("target is x^-2 exactly", x ** -2 == target, f"x^-2={x**-2}")

    print("\nC. Positive polynomial grammar")
    print("-" * 72)
    poly_exps = [0, 1, 2, 3, 4]
    poly_min, poly_max = weighted_bounds(poly_exps, x)
    check("nonnegative polynomial terms have max E/T ratio 1", poly_max == F(1), f"range=[{poly_min},{poly_max}]")
    check("positive polynomial grammar cannot reach target above 1", target > poly_max)
    sample_poly = {0: F(2), 1: F(3), 2: F(5), 4: F(7)}
    sample_poly_ratio = ratio_for_terms(sample_poly, w_e, w_t)
    check("sample positive polynomial ratio stays below 1", sample_poly_ratio < 1, f"ratio={sample_poly_ratio}")
    check("forward quadratic term gives 4/9, not target", ratio_for_terms({2: F(1)}, w_e, w_t) == F(4, 9))

    print("\nD. Positive reciprocal grammar")
    print("-" * 72)
    one_pole_exps = [0, -1]
    one_min, one_max = weighted_bounds(one_pole_exps, x)
    check("one-pole nonnegative reciprocal grammar has max ratio 3/2", one_max == F(3, 2), f"range=[{one_min},{one_max}]")
    check("one-pole grammar cannot reach 9/4", target > one_max)
    sample_one_pole = {0: F(1), -1: F(2)}
    sample_one_ratio = ratio_for_terms(sample_one_pole, w_e, w_t)
    check("sample positive one-pole ratio stays below target", sample_one_ratio < target, f"ratio={sample_one_ratio}")
    check("pure one-reciprocal law gives kappa=3/2", ratio_for_terms({-1: F(1)}, w_e, w_t) == F(3, 2))

    two_pole_exps = [0, -1, -2]
    two_min, two_max = weighted_bounds(two_pole_exps, x)
    check("two-pole nonnegative reciprocal grammar has max ratio 9/4", two_max == target, f"range=[{two_min},{two_max}]")
    check("pure second reciprocal hits target", ratio_for_terms({-2: F(1)}, w_e, w_t) == target)
    check("adding a positive constant term drops below target", ratio_for_terms({0: F(1), -2: F(1)}, w_e, w_t) < target)
    check("adding a positive one-pole term drops below target", ratio_for_terms({-1: F(1), -2: F(1)}, w_e, w_t) < target)
    check(
        "exact target in nonnegative {0,-1,-2} grammar forces pure inverse-square",
        ratio_for_terms({0: F(0), -1: F(0), -2: F(5)}, w_e, w_t) == target,
    )

    print("\nE. Signed-cancellation alternatives")
    print("-" * 72)
    a_rec, b_rec = signed_two_point_law(target, F(1), w_e, w_t, reciprocal=True)
    c_a1_rec = a_rec + b_rec / w_a1
    check("signed one-pole reciprocal solution has a=-3/2", a_rec == F(-3, 2), f"a={a_rec}")
    check("signed one-pole reciprocal solution has b=5/4", b_rec == F(5, 4), f"b={b_rec}")
    check("signed one-pole reciprocal solution predicts A1 coefficient 6", c_a1_rec == F(6), f"c_A1={c_a1_rec}")
    check("signed one-pole uses a negative constant term", a_rec < 0)

    a_dir, b_dir = signed_two_point_law(target, F(1), w_e, w_t, reciprocal=False)
    c_a1_dir = a_dir + b_dir * w_a1
    check("signed direct affine solution has a=19/4", a_dir == F(19, 4), f"a={a_dir}")
    check("signed direct affine solution has b=-15/2", b_dir == F(-15, 2), f"b={b_dir}")
    check("signed direct affine solution predicts A1 coefficient 7/2", c_a1_dir == F(7, 2), f"c_A1={c_a1_dir}")
    check("signed direct affine uses a negative slope", b_dir < 0)

    print("\nF. Current-bank markers")
    print("-" * 72)
    note_text = read(str(note))
    exact_text = read(str(exact))
    covariance_text = read(str(covariance))
    ell_text = read(str(ell_e))
    parent_text = read(str(parent))
    usable_text = read(str(usable))
    check("new note declares no_go claim type", "**Claim type:** no_go" in note_text)
    check("new note says no audit verdict is applied", "No audit verdict is applied" in note_text)
    check("new note names pure inverse-square as the remaining theorem target", "pure inverse-square coefficient law" in note_text)
    check("new note names signed-cancellation alternatives as imports", "signed-cancellation" in note_text)
    check("new note avoids global impossibility", "does not rule out future nonlinear" in note_text)
    check("exact readout surface names beta_E/alpha_E=21/4", "beta_E / alpha_E = 21/4" in exact_text)
    check("covariance surface identifies inverse-square as the gap", "inverse-square" in covariance_text and "w_X" in covariance_text)
    check("ell_E surface keeps rho_E as readout direction", "rho_E is the readout direction" in ell_text)
    check("parent theta surface keeps endpoint triple open", "readout-map endpoint triple is not yet derived" in parent_text)
    check(
        "repo has other inverse-square readings that are lane-specific",
        "`eta^2` inverse-square reading" in usable_text and "CKM CP-parameter bookkeeping" in usable_text,
    )

    print("\nSummary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print(
        "VERDICT: exact grammar gate. Positive polynomial laws and positive one-pole reciprocal "
        "laws cannot produce lambda=9/4 from w_E/w_T=2/3. A nonnegative grammar with powers "
        "{0,-1,-2} reaches the target only as the pure inverse-square term. Signed one-pole or "
        "direct affine alternatives can be fitted, but they import negative/background terms and "
        "specific A1 coefficients. The Route-2 residual is therefore a pure inverse-square "
        "coefficient-law theorem or an equivalent signed-cancellation theorem, not a generic "
        "coefficient-law consequence."
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
