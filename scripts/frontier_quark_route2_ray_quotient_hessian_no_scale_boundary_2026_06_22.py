#!/usr/bin/env python3
"""Verify the Route-2 ray-quotient Hessian no-scale boundary."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs/QUARK_ROUTE2_RAY_QUOTIENT_HESSIAN_NO_SCALE_BOUNDARY_NOTE_2026-06-22.md"
BLOCK101 = ROOT / "docs/QUARK_ROUTE2_HESSIAN_COUNTERTERM_EXCLUSION_BOUNDARY_NOTE_2026-06-22.md"
BLOCK100 = ROOT / "docs/QUARK_ROUTE2_DILATION_COVARIANT_HESSIAN_SOURCE_BOUNDARY_NOTE_2026-06-22.md"
BLOCK99 = ROOT / "docs/QUARK_ROUTE2_TYPED_METRIC_SOURCE_INVERSE_SQUARE_BOUNDARY_NOTE_2026-06-22.md"
S3 = ROOT / "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
READOUT = ROOT / "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
SCHUR = ROOT / "docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md"
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


def hessian(c: Fraction, eps: Fraction, w: Fraction) -> Fraction:
    return c / (w * w) + eps


def pullback_residual(c: Fraction, eps: Fraction, a: Fraction, w: Fraction) -> Fraction:
    return a * a * hessian(c, eps, a * w) - hessian(c, eps, w)


def euler_residual(c: Fraction, eps: Fraction, w: Fraction) -> Fraction:
    derivative = -2 * c / (w**3)
    return w * derivative + 2 * hessian(c, eps, w)


def ratio(eps: Fraction, c: Fraction = Fraction(1)) -> Fraction:
    w_e = Fraction(1, 3)
    w_t = Fraction(1, 2)
    return hessian(c, eps, w_e) / hessian(c, eps, w_t)


def main() -> int:
    print("Route-2 ray-quotient Hessian no-scale boundary")
    print("=" * 78)

    print("\nA. Source-note and authority boundary")
    note = read(NOTE)
    note_c = compact(note)
    check(NOTE.exists(), "new source note exists", str(NOTE.relative_to(ROOT)))
    check(
        "Actual current-surface status:** exact-support" in note,
        "new note declares exact-support, not endpoint closure",
    )
    check(
        "ray-quotient Hessian two-form" in note
        and "epsilon=0" in note_c
        and "not endpoint closure" in note,
        "new note states the support theorem and open boundary",
    )
    check(
        "proposed_retained" not in note_c
        and "would become retained" not in note_c
        and "retained branch-local" not in note_c,
        "new note has no retained proposal wording",
    )

    authorities = [
        (BLOCK101, ["The current surface does not exclude `epsilon > 0`", "epsilon=0"]),
        (BLOCK100, ["H(a w) = a^-2 H(w)", "C / w^2"]),
        (BLOCK99, ["q_X w_X^2 = 5/24", "21/4"]),
        (S3, ["the underlying readout-map endpoint triple is not yet derived"]),
        (READOUT, ["beta_E / alpha_E = 21/4", "exact missing-map obstruction"]),
        (SCHUR, ["q_X", "w_X", "inverse-square"]),
        (MINIMAL, ["Record", "supplies no readout context"]),
    ]
    for path, markers in authorities:
        text = read(path)
        missing = [marker for marker in markers if marker not in text]
        check(not missing, f"{path.name} contains required boundary markers", "; ".join(markers))

    print("\nB. Ray-quotient Hessian theorem")
    c = Fraction(5, 24)
    samples = [
        (Fraction(2), Fraction(1, 3)),
        (Fraction(3, 2), Fraction(1, 2)),
        (Fraction(5, 3), Fraction(2, 5)),
    ]
    check(
        all(pullback_residual(c, Fraction(0), a, w) == 0 for a, w in samples),
        "pure inverse-square Hessian two-form is ray-pullback invariant",
    )
    check(
        all(
            pullback_residual(c, Fraction(7), a, w) == Fraction(7) * (a * a - 1)
            for a, w in samples
        ),
        "counterterm pullback residual is epsilon*(a^2-1)",
    )
    check(
        pullback_residual(c, Fraction(1), Fraction(2), Fraction(1, 3)) == Fraction(3),
        "positive counterterm violates nontrivial ray pullback invariance",
        "residual=3",
    )
    check(
        pullback_residual(c, Fraction(7), Fraction(1), Fraction(1, 3)) == 0,
        "unit scale is correctly identified as uninformative",
    )
    check(
        all(euler_residual(c, Fraction(0), w) == 0 for _, w in samples),
        "Euler no-scale residual vanishes for inverse-square Hessian",
    )
    check(
        all(euler_residual(c, Fraction(5), w) == Fraction(10) for _, w in samples),
        "Euler no-scale residual is 2*epsilon for counterterm family",
    )
    check(
        Fraction(0) * (Fraction(2) ** 2 - 1) == 0
        and Fraction(3) * (Fraction(2) ** 2 - 1) != 0,
        "one nontrivial scale already forces epsilon=0 inside the additive family",
    )
    hits = []
    for p in range(-8, 9):
        if Fraction(2) ** (p + 2) == 1 and Fraction(3) ** (p + 2) == 1:
            hits.append(p)
    check(hits == [-2], "monomial ray-pullback invariant exponent is uniquely p=-2", f"hits={hits}")

    print("\nC. Endpoint consequence")
    w_e = Fraction(1, 3)
    w_t = Fraction(1, 2)
    q_t = Fraction(5, 6)
    h_ratio = hessian(Fraction(1), Fraction(0), w_e) / hessian(Fraction(1), Fraction(0), w_t)
    q_e = q_t * h_ratio
    rho_e = 6 * (q_e - 1)
    c_te = Fraction(-2) * q_t / q_e
    check(h_ratio == Fraction(9, 4), "ray-quotient Hessian gives H_E/H_T=9/4", f"ratio={h_ratio}")
    check(q_e == Fraction(15, 8), "T-normalized source gives q_E=15/8", f"q_E={q_e}")
    check(rho_e == Fraction(21, 4), "q_E=15/8 gives rho_E=21/4", f"rho_E={rho_e}")
    check(c_te == Fraction(-8, 9), "center ratio is -8/9 under shell ratio -2", f"c_TE={c_te}")
    check(
        (Fraction(-1), Fraction(-2), rho_e) == (Fraction(-1), Fraction(-2), Fraction(21, 4)),
        "endpoint triple is recovered under supplied no-scale premise",
    )

    print("\nD. Counterterm and variational boundary")
    check(ratio(Fraction(0)) == Fraction(9, 4), "zero counterterm recovers target ratio")
    check(ratio(Fraction(1)) == Fraction(2), "epsilon=1 lowers ratio to 2", f"ratio={ratio(Fraction(1))}")
    check(ratio(Fraction(5)) == Fraction(14, 9), "epsilon=5 lowers ratio to 14/9", f"ratio={ratio(Fraction(5))}")
    check(
        all(ratio(eps) < Fraction(9, 4) for eps in [Fraction(1), Fraction(2), Fraction(5), Fraction(20)]),
        "every sampled positive counterterm misses the endpoint ratio",
    )
    derivs = [Fraction(-5, (4 + eps) ** 2) for eps in [Fraction(0), Fraction(1), Fraction(5)]]
    check(all(d < 0 for d in derivs), "R(epsilon) derivative is negative for epsilon>=0 samples", str(derivs))
    eps = Fraction(0)
    check(
        4 * (9 + eps) == 9 * (4 + eps)
        and all(4 * (9 + e) != 9 * (4 + e) for e in [Fraction(1), Fraction(5)]),
        "target ratio equation forces epsilon=0 in the additive family",
    )
    grid = [Fraction(i, 4) for i in range(0, 17)]
    max_eps = max(grid, key=ratio)
    check(max_eps == 0, "inverse-square endpoint is unique max-leverage grid point", f"epsilon={max_eps}")
    check(
        "choosing the maximum because it matches the target would be circular" in note_c,
        "note labels max-leverage selection as an open variational premise",
    )

    print("\nE. Coordinate and current-surface boundary")
    check(
        "u=log(w)" in note and "physical Hessian coordinate" in note,
        "note records the coordinate-bridge boundary",
    )
    check(
        "-log(w)" not in note or "ordinary second derivatives" in note,
        "note avoids treating a coordinate Hessian as coordinate-free closure",
    )
    minimal = read(MINIMAL)
    check(
        "supplies no readout context" in minimal and "weighting" in minimal,
        "minimal axioms do not supply source weights or Hessian coordinate",
    )
    block101 = read(BLOCK101)
    check(
        "Positivity and convexity are preserved by `epsilon >= 0`" in block101
        and "Separability is preserved" in block101,
        "Block101 confirms positivity/separability do not exclude counterterms",
    )
    check(
        "The current surface does not derive that premise" in note,
        "new note states exact support/open boundary rather than closure",
    )
    check(
        "No observed masses, fitted endpoint values" in note_c,
        "forbidden observed/fitted imports are excluded",
    )

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={passes}, FAIL={fails}")
    if fails:
        print("STATUS: failure in ray-quotient Hessian no-scale boundary verifier.")
        return 1
    print(
        "STATUS: exact-support/open boundary. A ray-quotient Hessian two-form "
        "forces the additive counterterm to zero and recovers the inverse-square "
        "Route-2 source law, but the current surface does not derive that "
        "no-scale source premise."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
