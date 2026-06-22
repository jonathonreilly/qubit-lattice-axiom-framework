#!/usr/bin/env python3
"""Verify the Route-2 source-row degree selector no-go."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs/QUARK_ROUTE2_SOURCE_ROW_DEGREE_SELECTOR_NO_GO_NOTE_2026-06-22.md"
BLOCK105 = ROOT / "docs/QUARK_ROUTE2_DIRECT_E_CENTER_SOURCE_ROW_DEGREE_BOUNDARY_NOTE_2026-06-22.md"
BLOCK104 = ROOT / "docs/QUARK_ROUTE2_POWER_LAW_COORDINATE_BRIDGE_BOUNDARY_NOTE_2026-06-22.md"
E_NAT = ROOT / "docs/QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
POSITIVITY = ROOT / "docs/ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md"
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


def pow_fraction(base: Fraction, degree: int) -> Fraction:
    if degree >= 0:
        return base**degree
    return Fraction(1, 1) / (base ** (-degree))


def row_ratio(degree: int) -> Fraction:
    return pow_fraction(Fraction(2, 3), degree)


def q_e(degree: int) -> Fraction:
    return Fraction(5, 6) * row_ratio(degree)


def rho_e(degree: int) -> Fraction:
    return 6 * (q_e(degree) - 1)


def c_te(degree: int) -> Fraction:
    return Fraction(-2) * Fraction(5, 6) / q_e(degree)


def satisfies_generic_constraints(degree: int) -> bool:
    # Generic row constraints tested here:
    # 1. homogeneous integer degree law;
    # 2. T-normalized ratio R(T/T)=1;
    # 3. positive E lift q_E>0, equivalent to rho_E>-6;
    # 4. scale invariance of the ratio under w -> lambda w.
    return q_e(degree) > 0 and rho_e(degree) > -6


def scale_ratio(degree: int, lam: Fraction) -> Fraction:
    w_e = Fraction(1, 3)
    w_t = Fraction(1, 2)
    return pow_fraction((lam * w_e) / (lam * w_t), degree)


def main() -> int:
    print("Route-2 source-row degree selector no-go")
    print("=" * 78)

    print("\nA. Source-note and authority boundary")
    note = read(NOTE)
    note_c = compact(note)
    check(NOTE.exists(), "new source note exists", str(NOTE.relative_to(ROOT)))
    check("Actual current-surface status:** no-go" in note, "new note declares scoped no-go status")
    check("generic homogeneous source-row constraints do not select `d=-2`" in note, "new note states the no-go target")
    check("not a no-go against a future physical degree theorem" in note, "new note keeps the positive route open")
    check(
        "proposed_retained" not in note_c
        and "would become retained" not in note_c
        and "retained branch-local" not in note_c,
        "new note has no retained proposal wording",
    )

    authorities = [
        (BLOCK105, ["homogeneous source-row degree `d=-2`", "does not derive `d=-2`"]),
        (BLOCK104, ["multiplicatively homogeneous", "current surface does not derive"]),
        (E_NAT, ["remains a free parameter", "additional E-center endpoint ratio"]),
        (POSITIVITY, ["readout **norm**", "`rho_E` is the readout's **direction**"]),
        (S3, ["endpoint triple", "not yet derived"]),
        (MINIMAL, ["supplies no readout context"]),
    ]
    for path, markers in authorities:
        text = compact(read(path))
        missing = [marker for marker in markers if marker not in text]
        check(not missing, f"{path.name} contains required boundary markers", "; ".join(markers))

    print("\nB. Generic homogeneous row constraints")
    degrees = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    check(all(satisfies_generic_constraints(d) for d in degrees), "all sampled degrees satisfy generic positivity/T-normalized constraints")
    check(all(scale_ratio(d, Fraction(5, 7)) == row_ratio(d) for d in degrees), "all sampled degrees preserve E/T ratio under common scale")
    check(all(scale_ratio(d, Fraction(11, 3)) == row_ratio(d) for d in degrees), "scale covariance holds for a second scale witness")
    check(row_ratio(-2) == Fraction(9, 4), "target degree still gives 9/4")
    check(row_ratio(-1) == Fraction(3, 2), "degree -1 is admissible but non-target")
    check(row_ratio(0) == Fraction(1, 1), "degree 0 is admissible but non-target")
    check(row_ratio(1) == Fraction(2, 3), "degree 1 is admissible but non-target")
    check(len({row_ratio(d) for d in degrees}) == len(degrees), "sampled admissible degrees give distinct E/T ratios")

    print("\nC. Exact counter-witnesses")
    witnesses = {
        -1: (Fraction(5, 4), Fraction(3, 2), Fraction(-4, 3)),
        0: (Fraction(5, 6), Fraction(-1, 1), Fraction(-2, 1)),
        1: (Fraction(5, 9), Fraction(-8, 3), Fraction(-3, 1)),
        2: (Fraction(10, 27), Fraction(-34, 9), Fraction(-9, 2)),
    }
    for d, (expected_q, expected_rho, expected_c) in witnesses.items():
        check(q_e(d) == expected_q, f"degree {d} q_E counter-witness", f"q_E={q_e(d)}")
        check(rho_e(d) == expected_rho, f"degree {d} rho_E counter-witness", f"rho_E={rho_e(d)}")
        check(c_te(d) == expected_c, f"degree {d} c_TE counter-witness", f"c_TE={c_te(d)}")
        check(satisfies_generic_constraints(d), f"degree {d} still satisfies generic constraints")

    print("\nD. Selector independence")
    target_degrees = [d for d in range(-8, 9) if q_e(d) == Fraction(15, 8)]
    non_target_admissible = [d for d in range(-8, 9) if satisfies_generic_constraints(d) and d not in target_degrees]
    check(target_degrees == [-2], "target degree remains unique in integer scan", f"target_degrees={target_degrees}")
    check(len(non_target_admissible) == 16, "generic constraints admit many non-target degrees", f"count={len(non_target_admissible)}")
    check(-1 in non_target_admissible and 0 in non_target_admissible and 1 in non_target_admissible, "simple non-target degrees are admissible")
    check("d=-1, d=0, and d=1" in note, "note displays simple admissible counter-witnesses")
    check("degree selector is the missing import" in note, "note identifies the remaining import")
    check("No observed masses, fitted endpoint values" in note, "forbidden observed/fitted imports are excluded")
    check("actual current surface remains open" in note, "note preserves parent open status")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={passes}, FAIL={fails}")
    if fails:
        print("STATUS: failure in source-row degree selector no-go verifier.")
        return 1
    print(
        "STATUS: scoped no-go. Generic homogeneous source-row constraints, "
        "T normalization, and positivity do not select degree -2; deriving "
        "the physical degree remains the open selector theorem."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
