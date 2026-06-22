#!/usr/bin/env python3
"""Route-2 typed metric/source inverse-square primitive boundary.

This runner verifies a narrow branch-local science packet:

* the endpoint triple follows exactly if a typed inverse-square center-lift
  primitive q_X w_X^2 = constant is supplied on the E/T channels;
* among small integer monomial projector-weight laws q_X proportional to w_X^p,
  the endpoint covariance q_E/q_T = 9/4 uniquely requires p = -2;
* current named Route-2/S3 surfaces record that this inverse-square primitive
  is not supplied by the existing carrier, equivariant, quadratic, Fierz,
  registration, or readout-map notes.

No observed masses, fitted endpoint values, audit verdicts, or PR state are
used.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "QUARK_ROUTE2_TYPED_METRIC_SOURCE_INVERSE_SQUARE_BOUNDARY_NOTE_2026-06-22.md"

AUTHORITY_MARKERS = {
    "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md": (
        "the underlying readout-map endpoint triple is not yet derived",
        "The next theorem target is the missing readout-map endpoint triple.",
    ),
    "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": (
        "(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)",
        "= (-1, -2, 21/4)",
        "the irreducible missing map entry is the `E`-channel ratio",
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
    "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md": (
        "physical tensor primitive in the GR-readout chain",
        "does **not** prove that this symbol is a physical tensor primitive",
    ),
    "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md": (
        "coexists with at least two exact Route-2 readout maps",
        "endpoint triple still needs upstream derivation",
        "Direct Fierz count",
    ),
    "QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md": (
        "blind to the E-center column cannot derive those values",
        "A positive repair\nmust supply a genuine E-center lift",
    ),
    "ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md": (
        "readout's **direction** in the (shell, center) plane",
        "shell-vs-center **distinguishing** input",
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


def text(relpath: str) -> str:
    return (DOCS / relpath).read_text(encoding="utf-8")


def q_from_rho(rho: Fraction) -> Fraction:
    return Fraction(1) + rho / 6


def rho_from_q(q_value: Fraction) -> Fraction:
    return 6 * (q_value - 1)


def center_ratio(shell_ratio: Fraction, q_t: Fraction, q_e: Fraction) -> Fraction:
    return shell_ratio * q_t / q_e


def q_e_from_power(q_t: Fraction, w_e: Fraction, w_t: Fraction, power: int) -> Fraction:
    return q_t * (w_e / w_t) ** power


def main() -> int:
    print("Route-2 typed metric/source inverse-square primitive boundary")
    print("=" * 78)

    print("\nA. Source-note and authority boundary")
    note = NOTE.read_text(encoding="utf-8")
    check("new source note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    check(
        "new note declares open-gate exact support, not closure",
        "**Claim type:** open_gate" in note
        and "**Actual current-surface status:** exact-support" in note
        and "This note does not derive the inverse-square primitive" in note,
    )
    check(
        "new note names the direct consumer",
        "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md" in note
        and "endpoint triple" in note,
    )
    check(
        "new note has no retained proposal wording",
        "proposed_retained" not in note
        and "would become retained" not in note
        and "retained branch-local" not in note,
    )

    for relpath, markers in AUTHORITY_MARKERS.items():
        body = text(relpath)
        check(
            f"{relpath} contains required boundary markers",
            all(marker in body for marker in markers),
            "; ".join(markers[:2]),
        )

    print("\nB. Exact inverse-square conditional closure")
    w_e = Fraction(1, 3)
    w_t = Fraction(1, 2)
    rho_t = Fraction(-1)
    shell_ratio = Fraction(-2)
    q_t = q_from_rho(rho_t)
    constant = q_t * w_t * w_t
    q_e = constant / (w_e * w_e)
    rho_e = rho_from_q(q_e)
    lam = q_e / q_t
    c_te = center_ratio(shell_ratio, q_t, q_e)

    check("T-side target gives q_T=5/6 exactly", q_t == Fraction(5, 6), f"q_T={q_t}")
    check("inverse-square constant is q_T*w_T^2=5/24", constant == Fraction(5, 24), f"C={constant}")
    check("same constant with w_E=1/3 gives q_E=15/8", q_e == Fraction(15, 8), f"q_E={q_e}")
    check("q_E=15/8 gives rho_E=21/4", rho_e == Fraction(21, 4), f"rho_E={rho_e}")
    check("endpoint covariance q_E/q_T is 9/4", lam == Fraction(9, 4), f"lambda={lam}")
    check("center T/E ratio is -8/9 under shell ratio -2", c_te == Fraction(-8, 9), f"c_TE={c_te}")
    check(
        "target triple is recovered exactly",
        (rho_t, shell_ratio, rho_e) == (Fraction(-1), Fraction(-2), Fraction(21, 4)),
        f"triple=({rho_t}, {shell_ratio}, {rho_e})",
    )

    print("\nC. Monomial-law uniqueness")
    hits: list[int] = []
    table: dict[int, Fraction] = {}
    for power in range(-8, 9):
        value = q_e_from_power(q_t, w_e, w_t, power) / q_t
        table[power] = value
        if value == Fraction(9, 4):
            hits.append(power)

    check("small integer projector-weight monomial search has unique p=-2 hit", hits == [-2], f"hits={hits}")
    check("constant lift p=0 misses target", table[0] == Fraction(1) and table[0] != Fraction(9, 4), f"lambda={table[0]}")
    check("single inverse leverage p=-1 gives 3/2, not 9/4", table[-1] == Fraction(3, 2), f"lambda={table[-1]}")
    check("direct projector leverage p=1 gives 2/3, not 9/4", table[1] == Fraction(2, 3), f"lambda={table[1]}")
    check("quadratic projector scaling p=2 gives 4/9, not 9/4", table[2] == Fraction(4, 9), f"lambda={table[2]}")

    print("\nD. Wrong-structure and slot-separation checks")
    f_adj = Fraction(8, 9)
    q_e_from_f_adj_center = shell_ratio * q_t / (-f_adj)
    rho_e_from_f_adj_center = rho_from_q(q_e_from_f_adj_center)
    check(
        "F_adj used as a signed center-ratio bridge would compute the target only after that typed bridge is granted",
        q_e_from_f_adj_center == Fraction(15, 8)
        and rho_e_from_f_adj_center == Fraction(21, 4),
        f"q_E={q_e_from_f_adj_center}, rho_E={rho_e_from_f_adj_center}",
    )
    check(
        "F_adj is not the same slot as endpoint covariance",
        f_adj != lam,
        f"F_adj={f_adj}, lambda={lam}",
    )
    q_e_single_inverse = q_e_from_power(q_t, w_e, w_t, -1)
    rho_single_inverse = rho_from_q(q_e_single_inverse)
    check(
        "one inverse-power law gives the wrong E-center lift",
        q_e_single_inverse == Fraction(5, 4)
        and rho_single_inverse == Fraction(3, 2),
        f"q_E={q_e_single_inverse}, rho_E={rho_single_inverse}",
    )
    q_e_quadratic = q_e_from_power(q_t, w_e, w_t, 2)
    rho_quadratic = rho_from_q(q_e_quadratic)
    check(
        "quadratic projector-weight law gives the wrong E-center lift",
        q_e_quadratic == Fraction(10, 27)
        and rho_quadratic == Fraction(-34, 9),
        f"q_E={q_e_quadratic}, rho_E={rho_quadratic}",
    )

    print("\nE. Current-surface conclusion")
    check(
        "current named surfaces expose rather than close the primitive",
        "No named functional produces an\n  inverse-square-of-projector-weight center lift."
        in text("QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md"),
    )
    check(
        "the exact conditional law is sufficient but not supplied",
        "the missing bridge is now exactly the typed inverse-square lift law" in note,
    )

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print(
            "STATUS: exact-support/open boundary. The endpoint triple follows from "
            "q_X*w_X^2=5/24, and p=-2 is the unique small-integer monomial law; "
            "the current named surfaces do not derive that typed primitive."
        )
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
