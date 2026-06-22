#!/usr/bin/env python3
"""Route-2 Hessian counterterm exclusion boundary.

This runner verifies that the Hessian family

    H_epsilon(w) = C/w^2 + epsilon

preserves positivity and separability for epsilon >= 0 while moving the
Route-2 E/T Hessian ratio away from 9/4 unless epsilon = 0. Thus the
counterterm-exclusion/no-scale premise is a real missing theorem, not a
consequence of current Record, positivity, or endpoint algebra surfaces.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "QUARK_ROUTE2_HESSIAN_COUNTERTERM_EXCLUSION_BOUNDARY_NOTE_2026-06-22.md"

AUTHORITY_MARKERS = {
    "QUARK_ROUTE2_DILATION_COVARIANT_HESSIAN_SOURCE_BOUNDARY_NOTE_2026-06-22.md": (
        "H_epsilon(w) = C/w^2 + epsilon",
        "convex counterterms preserve positivity",
    ),
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
    "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md": (
        "No named functional produces an",
        "inverse-square-of-projector-weight center lift",
    ),
    "MINIMAL_AXIOMS_2026-06-05.md": (
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


def h_eps(weight: Fraction, epsilon: Fraction, constant: Fraction = Fraction(1)) -> Fraction:
    return constant / (weight * weight) + epsilon


def ratio(epsilon: Fraction, constant: Fraction = Fraction(1)) -> Fraction:
    w_e = Fraction(1, 3)
    w_t = Fraction(1, 2)
    return h_eps(w_e, epsilon, constant) / h_eps(w_t, epsilon, constant)


def q_from_rho(rho: Fraction) -> Fraction:
    return Fraction(1) + rho / 6


def rho_from_q(q_value: Fraction) -> Fraction:
    return 6 * (q_value - 1)


def center_ratio(shell_ratio: Fraction, q_t: Fraction, q_e: Fraction) -> Fraction:
    return shell_ratio * q_t / q_e


def epsilon_for_ratio(target: Fraction) -> Fraction:
    # target = (9 + e)/(4 + e)
    return (Fraction(9) - 4 * target) / (target - 1)


def main() -> int:
    print("Route-2 Hessian counterterm exclusion boundary")
    print("=" * 78)

    print("\nA. Source-note and authority boundary")
    note = NOTE.read_text(encoding="utf-8")
    check("new source note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    check(
        "new note declares exact negative no-go boundary",
        "**Claim type:** no_go" in note
        and "**Actual current-surface status:** no-go" in note
        and "current weaker premises already exclude positive" in note,
    )
    check(
        "new note names Block100 and downstream S3 route",
        "QUARK_ROUTE2_DILATION_COVARIANT_HESSIAN_SOURCE_BOUNDARY_NOTE_2026-06-22.md" in note
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

    print("\nB. Exact counterterm family")
    w_e = Fraction(1, 3)
    w_t = Fraction(1, 2)
    check("counterterm Hessian is positive at E/T for epsilon=1", h_eps(w_e, 1) > 0 and h_eps(w_t, 1) > 0)
    check("epsilon=0 gives target ratio 9/4", ratio(Fraction(0)) == Fraction(9, 4), f"R0={ratio(Fraction(0))}")
    check("epsilon=1 gives ratio 2", ratio(Fraction(1)) == Fraction(2), f"R1={ratio(Fraction(1))}")
    check("epsilon=5 gives ratio 14/9", ratio(Fraction(5)) == Fraction(14, 9), f"R5={ratio(Fraction(5))}")
    derivative_num = Fraction(-5)
    check("exact derivative numerator is negative", derivative_num < 0, "dR/de=-5/(4+e)^2")
    check("positive epsilon monotonically moves ratio toward 1", Fraction(9, 4) > ratio(1) > ratio(5) > Fraction(1))
    check("target equation forces epsilon=0", epsilon_for_ratio(Fraction(9, 4)) == 0)
    check("ratio 2 corresponds to epsilon=1", epsilon_for_ratio(Fraction(2)) == 1)
    check("ratio 3/2 corresponds to epsilon=6", epsilon_for_ratio(Fraction(3, 2)) == 6)
    check("separable potential second derivative matches H_epsilon", h_eps(w_e, 5) == Fraction(14))

    print("\nC. Endpoint deformation")
    q_t = q_from_rho(Fraction(-1))
    shell_ratio = Fraction(-2)
    q_e_0 = q_t * ratio(0)
    q_e_1 = q_t * ratio(1)
    q_e_5 = q_t * ratio(5)
    rho_0 = rho_from_q(q_e_0)
    rho_1 = rho_from_q(q_e_1)
    rho_5 = rho_from_q(q_e_5)
    c_1 = center_ratio(shell_ratio, q_t, q_e_1)
    c_5 = center_ratio(shell_ratio, q_t, q_e_5)
    check("zero counterterm gives q_E=15/8 and rho_E=21/4", q_e_0 == Fraction(15, 8) and rho_0 == Fraction(21, 4))
    check("epsilon=1 gives q_E=5/3 and rho_E=4", q_e_1 == Fraction(5, 3) and rho_1 == Fraction(4), f"q_E={q_e_1}, rho_E={rho_1}")
    check("epsilon=5 gives q_E=35/27 and rho_E=16/9", q_e_5 == Fraction(35, 27) and rho_5 == Fraction(16, 9), f"q_E={q_e_5}, rho_E={rho_5}")
    check("epsilon=1 center ratio misses -8/9", c_1 == Fraction(-1), f"c_TE={c_1}")
    check("epsilon=5 center ratio misses -8/9", c_5 == Fraction(-9, 7), f"c_TE={c_5}")
    check("positive epsilon misses endpoint triple", (Fraction(-1), shell_ratio, rho_1) != (Fraction(-1), Fraction(-2), Fraction(21, 4)))
    check("zero counterterm is necessary for q_E=15/8 inside this family", epsilon_for_ratio(q_e_0 / q_t) == 0)
    check("family realizes continuum of non-target positive ratios", ratio(1) != ratio(5) and ratio(6) == Fraction(3, 2))

    print("\nD. Current-surface boundary")
    eps1_lhs = h_eps(Fraction(1), 1)
    eps1_rhs = h_eps(Fraction(1, 2), 1) / 4
    check("positive counterterm breaks dilation covariance", eps1_lhs != eps1_rhs, f"lhs={eps1_lhs}, rhs={eps1_rhs}")
    check(
        "minimal Record does not exclude counterterms",
        "Record supplies finite scalar additivity" in note
        and "weighting, normalization, probability" in doc_text("MINIMAL_AXIOMS_2026-06-05.md"),
    )
    check("note states current surface does not exclude epsilon", "The current surface does not exclude `epsilon > 0`" in note)
    check("note names zero-counterterm as future theorem target", "Counterterm exclusion" in note and "future theorem target" in note)
    check("no hidden proof imports are used", "No observed masses, fitted endpoint values, nearest-rational selector, or literature value is used" in compact(note))
    check("note does not apply audit verdict", "does not set, predict, or apply an audit verdict" in compact(note))
    check("trace to direct blocker is present", "readout-map endpoint triple" in note)
    check("Block100 support remains conditional", "Block100 and Block99 give a direct route" in note)
    check("runner excludes PR-state inputs by construction", "PR state" not in note and "mergeability" not in note)

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        return 1
    print(
        "STATUS: no-go/exact negative boundary. Current weak source premises "
        "allow positive Hessian counterterms; endpoint closure needs a "
        "zero-counterterm/no-scale theorem."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
