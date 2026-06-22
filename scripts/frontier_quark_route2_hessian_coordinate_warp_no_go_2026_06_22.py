#!/usr/bin/env python3
"""Verify the Route-2 Hessian coordinate-warp no-go."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs/QUARK_ROUTE2_HESSIAN_COORDINATE_WARP_NO_GO_NOTE_2026-06-22.md"
BLOCK102 = ROOT / "docs/QUARK_ROUTE2_RAY_QUOTIENT_HESSIAN_NO_SCALE_BOUNDARY_NOTE_2026-06-22.md"
BLOCK101 = ROOT / "docs/QUARK_ROUTE2_HESSIAN_COUNTERTERM_EXCLUSION_BOUNDARY_NOTE_2026-06-22.md"
BLOCK100 = ROOT / "docs/QUARK_ROUTE2_DILATION_COVARIANT_HESSIAN_SOURCE_BOUNDARY_NOTE_2026-06-22.md"
BLOCK99 = ROOT / "docs/QUARK_ROUTE2_TYPED_METRIC_SOURCE_INVERSE_SQUARE_BOUNDARY_NOTE_2026-06-22.md"
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


def log_derivative(b: Fraction, w: Fraction) -> Fraction:
    return Fraction(1, 1) / w + b


def ratio_b(b: Fraction) -> Fraction:
    return (log_derivative(b, Fraction(1, 3)) / log_derivative(b, Fraction(1, 2))) ** 2


def q_e_from_ratio(ratio: Fraction) -> Fraction:
    return Fraction(5, 6) * ratio


def rho_from_q(q: Fraction) -> Fraction:
    return 6 * (q - 1)


def c_te_from_q(q: Fraction) -> Fraction:
    return Fraction(-2) * Fraction(5, 6) / q


def main() -> int:
    print("Route-2 Hessian coordinate-warp no-go")
    print("=" * 78)

    print("\nA. Source-note and authority boundary")
    note = read(NOTE)
    note_c = compact(note)
    check(NOTE.exists(), "new source note exists", str(NOTE.relative_to(ROOT)))
    check("Actual current-surface status:** no-go" in note, "new note declares exact no-go boundary")
    check("y_b(w) = w exp(b w)" in note and "positive coordinate" in note, "new note states the coordinate-warp family")
    check(
        "proposed_retained" not in note_c
        and "would become retained" not in note_c
        and "retained branch-local" not in note_c,
        "new note has no retained proposal wording",
    )

    authorities = [
        (BLOCK102, ["ray-quotient Hessian two-form", "epsilon=0"]),
        (BLOCK101, ["H_epsilon(w) = C/w^2 + epsilon", "The current surface does not exclude `epsilon > 0`"]),
        (BLOCK100, ["H(a w) = a^-2 H(w)", "C / w^2"]),
        (BLOCK99, ["q_X w_X^2 = 5/24", "21/4"]),
        (S3, ["the underlying readout-map endpoint triple is not yet derived"]),
        (MINIMAL, ["Record", "supplies no readout context"]),
    ]
    for path, markers in authorities:
        text = read(path)
        missing = [marker for marker in markers if marker not in text]
        check(not missing, f"{path.name} contains required boundary markers", "; ".join(markers))

    print("\nB. Coordinate-warp theorem")
    samples = [Fraction(0), Fraction(1), Fraction(2), Fraction(5)]
    check(all(log_derivative(b, Fraction(1, 3)) > 0 for b in samples), "y_b is monotone at E weight for sampled b")
    check(all(log_derivative(b, Fraction(1, 2)) > 0 for b in samples), "y_b is monotone at T weight for sampled b")
    check(log_derivative(Fraction(0), Fraction(1, 3)) == 3, "unwarped E log-derivative is 3")
    check(log_derivative(Fraction(0), Fraction(1, 2)) == 2, "unwarped T log-derivative is 2")
    check(log_derivative(Fraction(1), Fraction(1, 3)) == 4, "b=1 E log-derivative is 4")
    check(log_derivative(Fraction(1), Fraction(1, 2)) == 3, "b=1 T log-derivative is 3")
    check(ratio_b(Fraction(0)) == Fraction(9, 4), "b=0 gives target ratio 9/4", f"R0={ratio_b(Fraction(0))}")
    check(ratio_b(Fraction(1)) == Fraction(16, 9), "b=1 gives non-target ratio 16/9", f"R1={ratio_b(Fraction(1))}")
    check(ratio_b(Fraction(2)) == Fraction(25, 16), "b=2 gives non-target ratio 25/16", f"R2={ratio_b(Fraction(2))}")
    check(all(ratio_b(b) < Fraction(9, 4) for b in [Fraction(1), Fraction(2), Fraction(5)]), "positive coordinate warps lower the E/T ratio")
    derivs = [Fraction(-2) * (b + 3) / ((b + 2) ** 3) for b in [Fraction(0), Fraction(1), Fraction(2)]]
    check(all(d < 0 for d in derivs), "dR_b/db is negative for b>=0 samples", str(derivs))
    check(
        all(4 * (b + 3) ** 2 != 9 * (b + 2) ** 2 for b in [Fraction(1), Fraction(2), Fraction(5)])
        and 4 * (0 + 3) ** 2 == 9 * (0 + 2) ** 2,
        "target ratio equation forces b=0 in sampled nonnegative family",
    )

    print("\nC. Endpoint deformation")
    q0 = q_e_from_ratio(ratio_b(Fraction(0)))
    q1 = q_e_from_ratio(ratio_b(Fraction(1)))
    q2 = q_e_from_ratio(ratio_b(Fraction(2)))
    check(q0 == Fraction(15, 8), "b=0 gives q_E=15/8", f"q0={q0}")
    check(rho_from_q(q0) == Fraction(21, 4), "b=0 gives rho_E=21/4")
    check(q1 == Fraction(40, 27), "b=1 gives q_E=40/27", f"q1={q1}")
    check(rho_from_q(q1) == Fraction(26, 9), "b=1 gives rho_E=26/9", f"rho1={rho_from_q(q1)}")
    check(c_te_from_q(q1) == Fraction(-9, 8), "b=1 center ratio misses -8/9", f"c1={c_te_from_q(q1)}")
    check(q2 == Fraction(125, 96), "b=2 gives q_E=125/96", f"q2={q2}")
    check(rho_from_q(q2) == Fraction(29, 16), "b=2 gives rho_E=29/16", f"rho2={rho_from_q(q2)}")
    check(c_te_from_q(q2) == Fraction(-32, 25), "b=2 center ratio misses -8/9", f"c2={c_te_from_q(q2)}")

    print("\nD. Current-surface boundary")
    check("does not prove that the source Hessian coordinate is exactly `w`" in note, "note states the coordinate bridge remains open")
    check("Power-law coordinate `w^a`" in note and "would be sufficient" in note, "note identifies sufficient coordinate-bridge class")
    check("Arbitrary positive coordinate" in note and "Leaves the E/T ratio free" in note, "note records no-go scope")
    minimal = read(MINIMAL)
    check("source/action" in minimal and "physical-observable identification" in minimal, "minimal axioms do not supply source-coordinate bridge")
    check("No observed masses, fitted endpoint values" in note, "forbidden observed/fitted imports are excluded")
    check("does not assert" in note and "current framework content" in note, "note avoids closure rhetoric")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={passes}, FAIL={fails}")
    if fails:
        print("STATUS: failure in Hessian coordinate-warp no-go verifier.")
        return 1
    print(
        "STATUS: no-go/exact negative boundary. No-scale form in an unspecified "
        "positive coordinate does not force the Route-2 inverse-square source law; "
        "a physical coordinate bridge remains required."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
