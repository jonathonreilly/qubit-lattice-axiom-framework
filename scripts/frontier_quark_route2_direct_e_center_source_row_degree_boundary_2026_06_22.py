#!/usr/bin/env python3
"""Verify the Route-2 direct E-center source-row degree boundary."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs/QUARK_ROUTE2_DIRECT_E_CENTER_SOURCE_ROW_DEGREE_BOUNDARY_NOTE_2026-06-22.md"
S3 = ROOT / "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
EXACT_READOUT = ROOT / "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
E_CENTER_ATTEMPT = ROOT / "docs/QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md"
E_BLIND = ROOT / "docs/QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md"
POWER_LAW = ROOT / "docs/QUARK_ROUTE2_POWER_LAW_COORDINATE_BRIDGE_BOUNDARY_NOTE_2026-06-22.md"
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


def pow_fraction(base: Fraction, degree: int) -> Fraction:
    if degree >= 0:
        return base**degree
    return Fraction(1, 1) / (base ** (-degree))


def row_ratio_for_degree(degree: int) -> Fraction:
    """Return q_E/q_T for a homogeneous direct source row of weight degree."""

    w_e = Fraction(1, 3)
    w_t = Fraction(1, 2)
    return pow_fraction(w_e / w_t, degree)


def q_e_for_degree(degree: int) -> Fraction:
    return Fraction(5, 6) * row_ratio_for_degree(degree)


def rho_e_from_q(q_e: Fraction) -> Fraction:
    return 6 * (q_e - 1)


def c_te_from_q(q_e: Fraction) -> Fraction:
    return Fraction(-2) * Fraction(5, 6) / q_e


def all_integer_degrees(lo: int = -8, hi: int = 8) -> list[int]:
    return list(range(lo, hi + 1))


def main() -> int:
    print("Route-2 direct E-center source-row degree boundary")
    print("=" * 78)

    print("\nA. Source-note and status guardrails")
    note = read(NOTE)
    note_c = compact(note)
    check(NOTE.exists(), "new source note exists", str(NOTE.relative_to(ROOT)))
    check("Actual current-surface status:** exact-support" in note, "new note declares exact-support/open status")
    check("homogeneous source-row degree `d=-2`" in note, "new note names the exact degree target")
    check("does not derive `d=-2`" in note, "new note leaves the degree-selection theorem open")
    check(
        "proposed_retained" not in note_c
        and "would become retained" not in note_c
        and "retained branch-local" not in note_c,
        "new note has no retained proposal wording",
    )

    authorities = [
        (S3, ["endpoint triple", "not yet derived"]),
        (EXACT_READOUT, ["beta_E / alpha_E = 21/4", "smallest exact missing map entry"]),
        (E_CENTER_ATTEMPT, ["derive gamma_E(center)/gamma_E(shell) = 15/8"]),
        (E_BLIND, ["A positive repair must supply a genuine E-center lift"]),
        (POWER_LAW, ["H_E/H_T = (w_T/w_E)^2 = 9/4"]),
        (MINIMAL, ["supplies no readout context"]),
    ]
    for path, markers in authorities:
        text = compact(read(path))
        missing = [marker for marker in markers if marker not in text]
        check(not missing, f"{path.name} contains required boundary markers", "; ".join(markers))

    print("\nB. Direct homogeneous source-row algebra")
    w_e = Fraction(1, 3)
    w_t = Fraction(1, 2)
    q_t = Fraction(5, 6)
    target_ratio = Fraction(9, 4)
    check(w_e == Fraction(1, 3), "E source weight is 1/3", f"w_E={w_e}")
    check(w_t == Fraction(1, 2), "T source weight is 1/2", f"w_T={w_t}")
    check(w_e / w_t == Fraction(2, 3), "E/T weight quotient is 2/3", f"w_E/w_T={w_e / w_t}")
    check(row_ratio_for_degree(-2) == target_ratio, "degree -2 gives q_E/q_T=9/4")
    check(q_e_for_degree(-2) == Fraction(15, 8), "degree -2 gives q_E=15/8", f"q_E={q_e_for_degree(-2)}")
    check(rho_e_from_q(q_e_for_degree(-2)) == Fraction(21, 4), "degree -2 gives rho_E=21/4")
    check(c_te_from_q(q_e_for_degree(-2)) == Fraction(-8, 9), "degree -2 gives center ratio -8/9")
    check(
        (Fraction(-1), Fraction(-2), rho_e_from_q(q_e_for_degree(-2)))
        == (Fraction(-1), Fraction(-2), Fraction(21, 4)),
        "degree -2 recovers the endpoint triple under supplied T-side values",
    )

    print("\nC. Uniqueness and falsifiers")
    integer_solutions = [d for d in all_integer_degrees() if row_ratio_for_degree(d) == target_ratio]
    check(integer_solutions == [-2], "unique integer degree in scan gives target ratio", f"solutions={integer_solutions}")
    check(row_ratio_for_degree(-1) == Fraction(3, 2), "degree -1 is a non-target witness", f"ratio={row_ratio_for_degree(-1)}")
    check(row_ratio_for_degree(0) == Fraction(1, 1), "degree 0 is a non-target witness", f"ratio={row_ratio_for_degree(0)}")
    check(row_ratio_for_degree(1) == Fraction(2, 3), "degree 1 is a non-target witness", f"ratio={row_ratio_for_degree(1)}")
    check(row_ratio_for_degree(2) == Fraction(4, 9), "degree 2 is a non-target witness", f"ratio={row_ratio_for_degree(2)}")
    check(q_e_for_degree(-1) == Fraction(5, 4), "degree -1 gives q_E=5/4, not 15/8")
    check(rho_e_from_q(q_e_for_degree(-1)) == Fraction(3, 2), "degree -1 gives rho_E=3/2, not 21/4")
    check(q_e_for_degree(0) == Fraction(5, 6), "degree 0 reuses q_T, not q_E target")
    check(rho_e_from_q(q_e_for_degree(0)) == Fraction(-1, 1), "degree 0 gives rho_E=-1")
    check(c_te_from_q(q_e_for_degree(-1)) == Fraction(-4, 3), "degree -1 gives center ratio -4/3, not -8/9")
    check(c_te_from_q(q_e_for_degree(0)) == Fraction(-2, 1), "degree 0 gives center ratio -2, not -8/9")
    check(all(row_ratio_for_degree(d) != target_ratio for d in [-8, -7, -6, -5, -4, -3, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]), "all scanned non--2 degrees miss 9/4")

    print("\nD. Boundary against hidden selectors")
    check("No observed masses, fitted endpoint values" in note, "forbidden observed/fitted imports are excluded")
    check("The target rationals appear only as exact comparison values" in note, "target rationals are comparison values")
    check("A direct row theorem must therefore derive the degree, not merely choose it." in note, "note names the missing selector")
    check("same algebraic target from the row side" in note, "note is not a duplicate coordinate-bridge claim")
    check("actual current surface remains open" in note, "note preserves open endpoint status")
    check("does not supply a physical source-row degree selector" in note, "note avoids closure rhetoric")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={passes}, FAIL={fails}")
    if fails:
        print("STATUS: failure in direct E-center source-row degree boundary verifier.")
        return 1
    print(
        "STATUS: exact-support/open boundary. A homogeneous direct E-center "
        "source-row law forces the Route-2 endpoint exactly only at degree -2; "
        "the current surface still does not derive that source-row degree."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
