#!/usr/bin/env python3
"""Verify the Route-2 log-weight second-variation row boundary."""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs/QUARK_ROUTE2_LOG_WEIGHT_SECOND_VARIATION_ROW_BOUNDARY_NOTE_2026-06-22.md"
BLOCK106 = ROOT / "docs/QUARK_ROUTE2_SOURCE_ROW_DEGREE_SELECTOR_NO_GO_NOTE_2026-06-22.md"
BLOCK105 = ROOT / "docs/QUARK_ROUTE2_DIRECT_E_CENTER_SOURCE_ROW_DEGREE_BOUNDARY_NOTE_2026-06-22.md"
BLOCK104 = ROOT / "docs/QUARK_ROUTE2_POWER_LAW_COORDINATE_BRIDGE_BOUNDARY_NOTE_2026-06-22.md"
RAY = ROOT / "docs/QUARK_ROUTE2_RAY_QUOTIENT_HESSIAN_NO_SCALE_BOUNDARY_NOTE_2026-06-22.md"
S3 = ROOT / "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
MINIMAL = ROOT / "docs/MINIMAL_AXIOMS_2026-06-05.md"

passes = 0
fails = 0


def compact(text: str) -> str:
    return " ".join(text.split())


def check(condition: bool, label: str, detail: str = "") -> None:
    global passes, fails
    if condition:
        passes += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"PASS: {label}{suffix}")
    else:
        fails += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"FAIL: {label}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def hessian(c: Fraction, w: Fraction) -> Fraction:
    return c / (w * w)


def pullback_residual(c: Fraction, scale: Fraction, w: Fraction) -> Fraction:
    return scale * scale * hessian(c, scale * w) - hessian(c, w)


def derivative_order_ratio(order: int) -> Fraction:
    # The n-th ordinary derivative of log(w) is proportional to w^-n.
    # Endpoint ratios only see the degree.
    return Fraction(3, 2) ** order


def derivative_of_log_coeff(order: int, w: Fraction) -> Fraction:
    if order < 1:
        raise ValueError("ordinary log derivative order must be >= 1")
    sign = 1 if order % 2 == 1 else -1
    return Fraction(sign * factorial(order - 1), 1) / (w**order)


def q_e_from_ratio(ratio: Fraction) -> Fraction:
    return Fraction(5, 6) * ratio


def rho_e(q_e: Fraction) -> Fraction:
    return 6 * (q_e - 1)


def c_te(q_e: Fraction) -> Fraction:
    return Fraction(-2) * Fraction(5, 6) / q_e


def main() -> int:
    print("Route-2 log-weight second-variation row boundary")
    print("=" * 78)

    print("\nA. Source-note and authority boundary")
    note = read(NOTE)
    note_c = compact(note)
    check(NOTE.exists(), "new source note exists", str(NOTE.relative_to(ROOT)))
    check("Actual current-surface status:** exact-support" in note, "new note declares exact-support/open status")
    check("scale-shift-invariant second variation" in note, "new note states the positive primitive")
    check("does not derive that the Route-2 source row is such a second variation" in note, "new note leaves physical primitive open")
    check(
        "proposed_retained" not in note_c
        and "would become retained" not in note_c
        and "retained branch-local" not in note_c,
        "new note has no retained proposal wording",
    )

    authorities = [
        (BLOCK106, ["generic homogeneous source-row constraints do not select `d=-2`", "degree selector is the missing import"]),
        (BLOCK105, ["homogeneous source-row degree `d=-2`", "does not derive `d=-2`"]),
        (BLOCK104, ["multiplicatively homogeneous", "does not derive a homogeneous physical source coordinate"]),
        (RAY, ["H(a w) = a^-2 H(w)", "H(w)=C/w^2"]),
        (S3, ["endpoint triple", "not yet derived"]),
        (MINIMAL, ["supplies no readout context"]),
    ]
    for path, markers in authorities:
        text = compact(read(path))
        missing = [marker for marker in markers if marker not in text]
        check(not missing, f"{path.name} contains required boundary markers", "; ".join(markers))

    print("\nB. Scale-shift second-variation theorem")
    c = Fraction(7, 5)
    weights = [Fraction(1, 3), Fraction(1, 2), Fraction(5, 7)]
    scales = [Fraction(2), Fraction(3, 5), Fraction(11, 4)]
    check(all(pullback_residual(c, a, w) == 0 for a in scales for w in weights), "C/w^2 Hessian two-form is pullback-invariant under scale shifts")
    check(hessian(Fraction(1), Fraction(1, 3)) / hessian(Fraction(1), Fraction(1, 2)) == Fraction(9, 4), "second variation gives E/T ratio 9/4")
    check(derivative_order_ratio(2) == Fraction(9, 4), "ordinary second derivative of log has row degree -2")
    check(abs(derivative_of_log_coeff(2, Fraction(1, 3))) == 9, "second derivative magnitude at w_E has inverse-square scaling")
    check(abs(derivative_of_log_coeff(2, Fraction(1, 2))) == 4, "second derivative magnitude at w_T has inverse-square scaling")
    check(
        abs(derivative_of_log_coeff(2, Fraction(1, 3)))
        / abs(derivative_of_log_coeff(2, Fraction(1, 2)))
        == Fraction(9, 4),
        "log second-variation coefficient ratio is 9/4",
    )

    print("\nC. Endpoint consequence")
    ratio = derivative_order_ratio(2)
    q_e = q_e_from_ratio(ratio)
    rho = rho_e(q_e)
    center = c_te(q_e)
    check(q_e == Fraction(15, 8), "second-variation row gives q_E=15/8", f"q_E={q_e}")
    check(rho == Fraction(21, 4), "second-variation row gives rho_E=21/4", f"rho_E={rho}")
    check(center == Fraction(-8, 9), "second-variation row gives c_TE=-8/9", f"c_TE={center}")
    check((Fraction(-1), Fraction(-2), rho) == (Fraction(-1), Fraction(-2), Fraction(21, 4)), "endpoint triple follows under supplied T-side values")

    print("\nD. Derivative-order falsifiers")
    expected = {
        1: (Fraction(3, 2), Fraction(5, 4), Fraction(3, 2), Fraction(-4, 3)),
        2: (Fraction(9, 4), Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)),
        3: (Fraction(27, 8), Fraction(45, 16), Fraction(87, 8), Fraction(-16, 27)),
        4: (Fraction(81, 16), Fraction(135, 32), Fraction(309, 16), Fraction(-32, 81)),
    }
    for order, (ratio_expected, q_expected, rho_expected, c_expected) in expected.items():
        ratio_o = derivative_order_ratio(order)
        q_o = q_e_from_ratio(ratio_o)
        check(ratio_o == ratio_expected, f"order {order} E/T ratio", f"ratio={ratio_o}")
        check(q_o == q_expected, f"order {order} q_E", f"q_E={q_o}")
        check(rho_e(q_o) == rho_expected, f"order {order} rho_E", f"rho_E={rho_e(q_o)}")
        check(c_te(q_o) == c_expected, f"order {order} c_TE", f"c_TE={c_te(q_o)}")
    check([order for order in range(1, 7) if derivative_order_ratio(order) == Fraction(9, 4)] == [2], "only derivative order 2 hits 9/4 in order scan")
    check("first variation gives degree `-1`" in note, "note records first-variation falsifier")
    check("third variation gives degree `-3`" in note, "note records third-variation falsifier")

    print("\nE. Current-surface boundary")
    check("No observed masses, fitted endpoint values" in note, "forbidden observed/fitted imports are excluded")
    check("second-variation primitive is the remaining import" in note, "note identifies the remaining import")
    check("actual current surface remains open" in note, "note preserves parent open status")
    check("not an endpoint closure" in note, "note avoids endpoint-closure rhetoric")
    check("supplies no readout context" in read(MINIMAL), "minimal axioms do not supply source-row primitive")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={passes}, FAIL={fails}")
    if fails:
        print("STATUS: failure in log-weight second-variation row boundary verifier.")
        return 1
    print(
        "STATUS: exact-support/open boundary. A scale-shift-invariant "
        "second variation in the physical weight coordinate forces row "
        "degree -2 and the Route-2 endpoint, but the current surface does "
        "not derive that second-variation source-row primitive."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
