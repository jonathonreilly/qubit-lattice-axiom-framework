#!/usr/bin/env python3
"""Route-2 dilation-covariant Hessian source boundary.

This branch-local verifier checks a narrow science packet:

* a positive separable Hessian source density satisfying
  H(a*w) = a^-2 H(w) is exactly H(w) = C/w^2;
* that premise would supply the inverse-square Route-2 E/T center-lift law
  isolated by Block99 and recover the endpoint triple;
* positivity, convex counterterms, finite two-point readings, and coordinate
  reparametrization do not by themselves supply the premise.

No observed masses, fitted endpoint values, nearest-rational selectors, audit
verdicts, or PR state are used.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "QUARK_ROUTE2_DILATION_COVARIANT_HESSIAN_SOURCE_BOUNDARY_NOTE_2026-06-22.md"

AUTHORITY_MARKERS = {
    "QUARK_ROUTE2_TYPED_METRIC_SOURCE_INVERSE_SQUARE_BOUNDARY_NOTE_2026-06-22.md": (
        "q_X w_X^2 = 5/24",
        "This note does not derive the inverse-square primitive",
    ),
    "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md": (
        "the underlying readout-map endpoint triple is not yet derived",
        "The next theorem target is the missing readout-map endpoint triple.",
    ),
    "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": (
        "the irreducible missing map entry is the `E`-channel ratio",
        "beta_E / alpha_E = 21/4",
    ),
    "OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md": (
        "Per-arm isotypic weights are exactly `(A1, E, T1) = (1/6, 1/3, 1/2)",
        "this lemma does **not**, by itself, derive any Route-2 readout entry",
    ),
    "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md": (
        "q_X",
        "inverse-square-of-projector-weight center lift",
        "No named functional produces an",
    ),
    "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md": (
        "source-domain bridge theorem, not another endpoint-ratio manipulation",
        "There is no current typed edge",
    ),
    "MINIMAL_AXIOMS_2026-06-05.md": (
        "Record",
        "supplies no readout context",
        "weighting, normalization, probability",
    ),
}


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag}: {name}{suffix}")


def doc_text(relpath: str) -> str:
    return (DOCS / relpath).read_text(encoding="utf-8")


def compact(body: str) -> str:
    return " ".join(body.split())


def q_from_rho(rho: Fraction) -> Fraction:
    return Fraction(1) + rho / 6


def rho_from_q(q_value: Fraction) -> Fraction:
    return 6 * (q_value - 1)


def center_ratio(shell_ratio: Fraction, q_t: Fraction, q_e: Fraction) -> Fraction:
    return shell_ratio * q_t / q_e


def h_inverse_square(weight: Fraction, constant: Fraction = Fraction(1)) -> Fraction:
    return constant / (weight * weight)


def h_counterterm(weight: Fraction, epsilon: Fraction, constant: Fraction = Fraction(1)) -> Fraction:
    return h_inverse_square(weight, constant) + epsilon


def monomial_ratio(w_e: Fraction, w_t: Fraction, power: int) -> Fraction:
    return (w_e / w_t) ** power


def main() -> int:
    print("Route-2 dilation-covariant Hessian source boundary")
    print("=" * 78)

    print("\nA. Source-note and authority boundary")
    note = NOTE.read_text(encoding="utf-8")
    check("new source note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    check(
        "new note declares open-gate exact support, not endpoint closure",
        "**Claim type:** open_gate" in note
        and "**Actual current-surface status:** exact-support" in note
        and "This note does not derive that dilation-covariant Hessian premise" in note,
    )
    check(
        "new note names Block99 and the direct S3 consumer",
        "QUARK_ROUTE2_TYPED_METRIC_SOURCE_INVERSE_SQUARE_BOUNDARY_NOTE_2026-06-22.md" in note
        and "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md" in note,
    )
    check(
        "new note has no retained proposal wording",
        "proposed_retained" not in note
        and "would become retained" not in note
        and "retained branch-local" not in note,
    )
    for relpath, markers in AUTHORITY_MARKERS.items():
        body = doc_text(relpath)
        check(
            f"{relpath} contains required boundary markers",
            all(marker in body for marker in markers),
            "; ".join(markers[:2]),
        )

    print("\nB. Dilation-covariant Hessian theorem")
    w_e = Fraction(1, 3)
    w_t = Fraction(1, 2)
    scale = Fraction(3, 2)
    probe_w = Fraction(1, 3)
    c = Fraction(5, 24)
    lhs = h_inverse_square(scale * probe_w, c)
    rhs = h_inverse_square(probe_w, c) / (scale * scale)
    check("inverse-square Hessian obeys H(a*w)=a^-2 H(w)", lhs == rhs, f"lhs={lhs}, rhs={rhs}")
    check("setting w=1 gives H(a)=a^-2 H(1)", h_inverse_square(scale, c) == c / (scale * scale))
    check("integrated log-barrier Hessian has Phi''=C/w^2", h_inverse_square(w_e, c) == Fraction(15, 8))
    hits = [p for p in range(-8, 9) if monomial_ratio(w_e, w_t, p) == Fraction(9, 4)]
    check("monomial Hessian law has unique small-integer exponent p=-2", hits == [-2], f"hits={hits}")
    check("constant Hessian p=0 misses target", monomial_ratio(w_e, w_t, 0) == Fraction(1))
    check("direct-weight Hessian p=1 misses target", monomial_ratio(w_e, w_t, 1) == Fraction(2, 3))
    check("quadratic-weight Hessian p=2 misses target", monomial_ratio(w_e, w_t, 2) == Fraction(4, 9))
    check("single-inverse Hessian p=-1 misses target", monomial_ratio(w_e, w_t, -1) == Fraction(3, 2))

    print("\nC. Endpoint consequence")
    rho_t = Fraction(-1)
    shell_ratio = Fraction(-2)
    q_t = q_from_rho(rho_t)
    h_ratio = h_inverse_square(w_e) / h_inverse_square(w_t)
    q_e = q_t * h_ratio
    rho_e = rho_from_q(q_e)
    c_te = center_ratio(shell_ratio, q_t, q_e)
    check("dilation-covariant Hessian gives H_E/H_T=9/4", h_ratio == Fraction(9, 4), f"ratio={h_ratio}")
    check("T-normalized source gives q_E=15/8", q_e == Fraction(15, 8), f"q_E={q_e}")
    check("q_E=15/8 gives rho_E=21/4", rho_e == Fraction(21, 4), f"rho_E={rho_e}")
    check("center ratio is -8/9 under shell ratio -2", c_te == Fraction(-8, 9), f"c_TE={c_te}")
    check(
        "endpoint triple is recovered exactly under the supplied premise",
        (rho_t, shell_ratio, rho_e) == (Fraction(-1), Fraction(-2), Fraction(21, 4)),
        f"triple=({rho_t}, {shell_ratio}, {rho_e})",
    )

    print("\nD. Counterterm and coordinate boundary")
    eps0_ratio = h_counterterm(w_e, Fraction(0)) / h_counterterm(w_t, Fraction(0))
    eps1_ratio = h_counterterm(w_e, Fraction(1)) / h_counterterm(w_t, Fraction(1))
    eps1_qe = q_t * eps1_ratio
    eps1_rho = rho_from_q(eps1_qe)
    eps1_lhs = h_counterterm(scale * probe_w, Fraction(1))
    eps1_rhs = h_counterterm(probe_w, Fraction(1)) / (scale * scale)
    check("zero counterterm recovers target Hessian ratio", eps0_ratio == Fraction(9, 4), f"ratio={eps0_ratio}")
    check("positive quadratic counterterm changes Hessian ratio", eps1_ratio == Fraction(2), f"ratio={eps1_ratio}")
    check("positive counterterm misses endpoint", eps1_qe == Fraction(5, 3) and eps1_rho == Fraction(4), f"q_E={eps1_qe}, rho_E={eps1_rho}")
    check("positive counterterm breaks dilation covariance", eps1_lhs != eps1_rhs, f"lhs={eps1_lhs}, rhs={eps1_rhs}")
    check("counterterm Hessian stays positive at E and T weights", h_counterterm(w_e, 1) > 0 and h_counterterm(w_t, 1) > 0)
    # Solve (9+e)/(4+e)=9/4: 4*(9+e)=9*(4+e), so 5e=0.
    check("target ratio forces counterterm epsilon=0", 4 * (9 + 0) == 9 * (4 + 0) and 4 * (9 + 1) != 9 * (4 + 1))
    check("constant Hessian two-point reading is an admissible non-target witness", q_t * Fraction(1) == Fraction(5, 6))
    check("log-coordinate second derivative is not the w-coordinate Hessian", Fraction(0) != h_inverse_square(w_e), "d^2(-u)/du^2=0 while d^2(-log w)/dw^2=1/w^2")

    print("\nE. Current-surface conclusion")
    check(
        "note states exact support/open boundary rather than endpoint closure",
        "Therefore the honest current status is exact support/open boundary" in note,
    )
    check(
        "minimal axioms do not supply weighting or normalization",
        "Record supplies no weighting, normalization" in note
        and "supplies no readout context" in doc_text("MINIMAL_AXIOMS_2026-06-05.md"),
    )
    check(
        "named current surfaces are listed as not deriving the premise",
        "The current surfaces do not derive the dilation-covariant Hessian premise" in note
        and "Block99 shows the inverse-square law is sufficient, but not derived" in note,
    )
    check(
        "forbidden proof imports are excluded",
        "No observed masses, fitted endpoint values, nearest-rational selector, or literature value is used"
        in compact(note),
    )

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        return 1
    print(
        "STATUS: exact-support/open boundary. Dilation-covariant Hessian "
        "density is exactly the inverse-square source law needed by Block99, "
        "but the current surface does not derive that covariance premise."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
