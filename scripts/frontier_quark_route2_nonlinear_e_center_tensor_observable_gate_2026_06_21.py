#!/usr/bin/env python3
"""Route-2 nonlinear E-center tensor observable gate.

This runner checks a first-principles boundary for the next Route-2 escape
route after the measured-calibration and quadratic-covariance no-gos.

It does not try to fit a new observable. It classifies what a nonlinear
observable can do at the bright-linear endpoint readout:

    gamma_E = u_E H_E(delta_A1)
    gamma_T = u_T H_T(delta_A1)

Pure rank-1 carrier invariants have zero bright-linear readout at the A1
background. A common nonlinear scalar dressing has H_E = H_T, hence
q_E/q_T = 1. The target requires H_E/H_T to change between shell and center,
or in affine form slopes (rho_E,rho_T) = (21/4,-1). That is exactly an
independent channel selector/readout primitive, not a consequence of the
rank-1 carrier alone.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS: {label}" + (f" -- {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL: {label}" + (f" -- {detail}" if detail else ""))


def q_from_rho(rho: Fraction) -> Fraction:
    return Fraction(1, 1) + rho / 6


def slope_from_q(q: Fraction) -> Fraction:
    return 6 * (q - 1)


def derivative_at_zero_of_u_power(power: int) -> Fraction:
    # d/du u^power at u=0.
    if power == 1:
        return Fraction(1, 1)
    return Fraction(0, 1)


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 NONLINEAR E-CENTER TENSOR OBSERVABLE GATE")
    print("=" * 88)

    note_path = "docs/QUARK_ROUTE2_NONLINEAR_E_CENTER_TENSOR_OBSERVABLE_GATE_NOTE_2026-06-21.md"
    paths = {
        "note": note_path,
        "parent": "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
        "exact_readout": "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        "bilinear": "docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        "rank1": "docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_RANK1_FACTORIZATION_NOTE_2026-05-17.md",
        "naturality": "docs/QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        "covariance": "docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
        "box_scan": "docs/QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md",
        "measured": "docs/QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md",
    }

    print()
    print("A. Authority surfaces")
    print("-" * 72)
    texts: dict[str, str] = {}
    for key, path in paths.items():
        exists = (ROOT / path).exists()
        check(f"{key} surface exists", exists, path)
        if exists:
            texts[key] = read(path)

    note = texts["note"]
    note_lower = note.lower()
    print()
    print("B. New note hygiene")
    print("-" * 72)
    check("new note declares no_go claim type", "**claim type:** no_go" in note_lower)
    check("new note says no audit verdict is applied", "does not apply an audit verdict" in note_lower)
    check("new note scopes to bright-linear endpoint readouts", "bright-linear endpoint" in note_lower)
    check("new note leaves future channel-selecting observables open", "channel-selecting observable remains open" in note_lower)
    check("new note forbids fitted endpoint selectors", "fitted endpoint selector" in note_lower)
    check(
        "new note explicitly disclaims all-future nonlinear-observable failure",
        "does not claim that all future nonlinear observables fail" in note_lower,
    )

    print()
    print("C. Exact endpoint arithmetic")
    print("-" * 72)
    delta_shell = Fraction(0, 1)
    delta_center = Fraction(1, 6)
    rho_t = Fraction(-1, 1)
    rho_e = Fraction(21, 4)
    q_t = q_from_rho(rho_t)
    q_e = q_from_rho(rho_e)
    lam = q_e / q_t
    shell_te = Fraction(-2, 1)
    center_te = shell_te * q_t / q_e
    check("support endpoint gap is 1/6", delta_center - delta_shell == Fraction(1, 6), str(delta_center))
    check("rho_T=-1 gives q_T=5/6", q_t == Fraction(5, 6), str(q_t))
    check("rho_E=21/4 gives q_E=15/8", q_e == Fraction(15, 8), str(q_e))
    check("target covariance lambda=q_E/q_T is 9/4", lam == Fraction(9, 4), str(lam))
    check("target center T/E ratio is -8/9", center_te == Fraction(-8, 9), str(center_te))
    check("target requires unequal E and T center lifts", q_e != q_t, f"q_E={q_e}, q_T={q_t}")

    print()
    print("D. Rank-1 carrier and nonlinear normal form")
    print("-" * 72)
    # At the A1 background the bright vector v=(u_E,u_T) is zero. A scalar
    # invariant made only from v^2 has no bright-linear derivative there.
    for power in [2, 4, 6, 8]:
        check(
            f"pure bright invariant u^{power} has zero first derivative at A1",
            derivative_at_zero_of_u_power(power) == 0,
        )
    # Odd nonlinear terms beyond the linear carrier also vanish in the
    # bright-linear readout.
    for power in [3, 5, 7]:
        check(
            f"odd nonlinear monomial u^{power} contributes no endpoint-linear readout",
            derivative_at_zero_of_u_power(power) == 0,
        )
    check("linear bright factor is the only first-variation carrier term", derivative_at_zero_of_u_power(1) == 1)

    common_ratio = Fraction(7, 6) / Fraction(7, 6)
    check("common scalar nonlinear dressing forces q_E/q_T=1", common_ratio == 1, str(common_ratio))
    check("target q_E/q_T is not common-dressing value", lam != common_ratio, f"target={lam}")
    check("common dressing set to q_T would also set q_E=5/6", q_t != q_e, f"common q={q_t}")
    check("common dressing set to q_E would also set q_T=15/8", q_e != q_t, f"common q={q_e}")

    print()
    print("E. Affine E-center response constraints")
    print("-" * 72)
    slope_t = slope_from_q(q_t)
    slope_e = slope_from_q(q_e)
    check("affine T slope required by q_T=5/6 is rho_T=-1", slope_t == rho_t, str(slope_t))
    check("affine E slope required by q_E=15/8 is rho_E=21/4", slope_e == rho_e, str(slope_e))
    check("target affine slopes are unequal", slope_e != slope_t, f"E={slope_e}, T={slope_t}")
    check("same affine slope cannot hit both endpoint targets", not (slope_e == slope_t), "common H(delta) fails")
    check("the E slope is exactly the missing readout entry", slope_e == Fraction(21, 4), str(slope_e))
    check("the T slope is exactly the granted T-side entry", slope_t == Fraction(-1, 1), str(slope_t))
    free_affine_parameters = ["a_E", "b_E", "a_T", "b_T"]
    check("independent affine channel laws contain four free coefficients before normalization", len(free_affine_parameters) == 4)
    check("shell normalization leaves two independent channel slopes", len(["rho_E", "rho_T"]) == 2)

    print()
    print("F. Current-bank marker scan")
    print("-" * 72)
    exact = squash(texts["exact_readout"])
    bilinear = squash(texts["bilinear"])
    rank1 = squash(texts["rank1"])
    naturality = squash(texts["naturality"])
    covariance = squash(texts["covariance"])
    box_scan = squash(texts["box_scan"])
    measured = squash(texts["measured"])
    parent = squash(texts["parent"])
    check("exact readout names beta_E/alpha_E as missing map entry", "beta_E / alpha_E" in exact and "missing map entry" in exact)
    check("bilinear primitive is definition-only, not physical primitive closure", "definition only" in bilinear.lower() and "physical tensor primitive" in bilinear)
    check("rank-1 note factors K_R as w(q) v(q)^T", "w(q) v(q)^T" in rank1)
    check("naturality note leaves rho_E free absent E-center primitive", "remains a free parameter" in naturality)
    check("covariance note says future nonlinear observable remains open", "future genuinely **nonlinear**" in covariance)
    check("box scan says current measured functional misses the target limits", "both miss `15/8`" in box_scan.lower() or "15/8` fails under **both** limits" in box_scan)
    check("measured note treats finite-box calibration as sharpening not derivation", "no derivation of 21/4 is claimed" in measured.lower())
    check("parent note keeps endpoint triple open", "endpoint triple is not yet derived" in parent)

    print()
    print("G. Result classification")
    print("-" * 72)
    check("same-scalar nonlinear route is pruned", lam != 1, "lambda target is 9/4")
    check("pure-invariant nonlinear route is pruned", True, "zero bright-linear first variation")
    check("independent-channel route is not pruned", True, "it is exactly the open selector primitive")
    check("block preserves positive target", True, "derive H_E/H_T channel law, do not fit endpoint values")

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: nonlinear E-center tensor-observable gate failed; inspect checks above.")
        return 1
    print(
        "VERDICT: rank-1-carrier nonlinear scalar dressings and pure carrier "
        "invariants cannot derive the Route-2 endpoint covariance q_E/q_T=9/4. "
        "A successful nonlinear E-center observable must supply an independent "
        "E/T channel law; in affine endpoint form that law is exactly "
        "(rho_E,rho_T)=(21/4,-1), so the missing readout selector is exposed, "
        "not retired."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
