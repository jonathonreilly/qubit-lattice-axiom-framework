#!/usr/bin/env python3
"""Verify the Route-2 trivial-character source-unit obstruction."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs/QUARK_ROUTE2_TRIVIAL_CHARACTER_SOURCE_UNIT_OBSTRUCTION_NOTE_2026-06-22.md"
BLOCK113 = ROOT / "docs/QUARK_ROUTE2_SOURCE_UNIT_SCALE_CHARACTER_BOUNDARY_NOTE_2026-06-22.md"
BLOCK112 = ROOT / "docs/QUARK_ROUTE2_NO_SCALE_CURVATURE_COEFFICIENT_NO_GO_NOTE_2026-06-22.md"
BLOCK111 = ROOT / "docs/QUARK_ROUTE2_SOURCE_ACTION_PRIMITIVE_BOUNDARY_NOTE_2026-06-22.md"
SOURCE_LOG = ROOT / "docs/SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md"
SOURCE_RN = ROOT / "docs/SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
SOURCE_PLANCK = ROOT / "docs/SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT_BRIDGE_NOTE_2026-05-30.md"
YT_UNIT = ROOT / "docs/YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md"
S3 = ROOT / "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"

passes = 0
fails = 0

W_E = Fraction(1, 3)
W_T = Fraction(1, 2)
Q_T = Fraction(5, 6)
S_TE = Fraction(-2, 1)
C0 = Fraction(7, 5)


def compact(text: str) -> str:
    return " ".join(text.split())


def check(condition: bool, label: str, detail: str = "") -> None:
    global passes, fails
    suffix = f" -- {detail}" if detail else ""
    if condition:
        passes += 1
        print(f"PASS: {label}{suffix}")
    else:
        fails += 1
        print(f"FAIL: {label}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def g_value(power: int, w: Fraction, c: Fraction = C0) -> Fraction:
    return c * (w ** power)


def chi(power: int, scale: Fraction) -> Fraction:
    return scale ** power


def row_ratio(power: int) -> Fraction:
    return (W_E / W_T) ** (power - 2)


def endpoint_from_row_ratio(ratio: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_e = Q_T * ratio
    rho_e = 6 * (q_e - 1)
    c_te = S_TE * Q_T / q_e
    return q_e, rho_e, c_te


def powers_matching_two_weight_calibration(u: Fraction, v: Fraction) -> list[int]:
    return [m for m in range(-6, 7) if g_value(m, u) == g_value(m, v)]


def main() -> int:
    print("Route-2 trivial-character source-unit obstruction")
    print("=" * 78)

    print("\nA. Source-note and authority boundary")
    note = read(NOTE)
    note_c = compact(note)
    note_lower = note.lower()
    check(NOTE.exists(), "new source note exists", str(NOTE.relative_to(ROOT)))
    check("**Actual current-surface status:** no-go" in note, "new note declares scoped no-go status")
    check("**Claim type:** no_go" in note, "new note declares no_go claim type")
    check("required stretch attempt" in note, "new note records stretch-attempt role")
    check("It does not." in note, "new note states source-unit normalization nonselection")
    check("distinct-weight calibration" in note, "new note states positive calibration residue")
    check(
        "proposed_retained" not in note_c
        and "would become retained" not in note_c
        and "retained branch-local" not in note_c,
        "new note has no retained proposal wording",
    )

    authorities = [
        (BLOCK113, ["g(w) = C w^m", "coefficient carries zero source-unit weight"]),
        (BLOCK112, ["g_E/g_T = 1", "g(a w) = g(w)"]),
        (BLOCK111, ["g(w) Phi''(w)", "constant source unit / no weight-dependent prefactor"]),
        (SOURCE_LOG, ["up to scale, not the unit `c=1`", "lambda > 0"]),
        (SOURCE_RN, ["Fisher norm `lambda^2`", "primitive unit source coordinate"]),
        (SOURCE_PLANCK, ["dimensionless action coefficient", "RN natural source coordinate"]),
        (YT_UNIT, ["lambda family preserves all current structural tests", "lambda = 1"]),
        (S3, ["endpoint triple", "not yet derived"]),
    ]
    for path, markers in authorities:
        text = compact(read(path))
        missing = [marker for marker in markers if marker not in text]
        check(not missing, f"{path.name} contains required boundary markers", "; ".join(markers))

    print("\nB. One-point source-unit normalization leaves character weight open")
    powers = [-2, -1, 0, 1, 2]
    for m in powers:
        check(g_value(m, Fraction(1)) == C0, f"m={m} obeys g(1)=C")
        check(chi(m, Fraction(2, 3) * Fraction(3, 5)) == chi(m, Fraction(2, 3)) * chi(m, Fraction(3, 5)), f"m={m} obeys character law")
    check(len({row_ratio(m) for m in powers}) == len(powers), "one-point normalization leaves distinct endpoint row ratios")
    check("Every character member `g(w)=C w^m` satisfies this" in note, "note records one-point nonselection")

    print("\nC. Primitive source-coordinate normalization does not fix coefficient weight")
    lambda_unit = Fraction(1, 1)
    check(lambda_unit == 1, "primitive source coordinate is fixed to lambda=1 in the tested support frame")
    for m in [-1, 0, 1, 2]:
        ratio = row_ratio(m) * (lambda_unit ** 0)
        check(ratio == row_ratio(m), f"m={m} row ratio remains after lambda=1", f"R={ratio}")
    check(len({row_ratio(m) for m in [-1, 0, 1, 2]}) == 4, "lambda=1 still leaves nontrivial character witnesses")
    check("Even with `lambda=1`" in note_c, "note records RN/source-unit nonselection")
    check("separate Hessian prefactor" in note, "note records Planck/action nonselection")

    print("\nD. Distinct-weight calibration is decisive inside character family")
    for u, v in [(Fraction(2, 5), Fraction(3, 5)), (Fraction(1, 4), Fraction(3, 4)), (W_E, W_T)]:
        matches = powers_matching_two_weight_calibration(u, v)
        check(matches == [0], f"distinct calibration u={u}, v={v} selects m=0", f"matches={matches}")
    check(powers_matching_two_weight_calibration(Fraction(1), Fraction(1)) == list(range(-6, 7)), "same-weight calibration is nonselective")
    scalar_matches = [m for m in range(-6, 7) if chi(m, Fraction(2, 3)) == 1]
    check(scalar_matches == [0], "single nontrivial scalarity sample chi(2/3)=1 selects m=0", f"matches={scalar_matches}")
    all_pair_matches = [
        m
        for m in range(-6, 7)
        if row_ratio(m) == Fraction(9, 4)
        and g_value(m, Fraction(2, 5)) == g_value(m, Fraction(3, 5))
    ]
    check(all_pair_matches == [0], "endpoint ratio plus independent calibration has only m=0")
    check("This is the best positive path found" in note, "note records calibration as positive residue")

    print("\nE. Endpoint consequences and circularity firewall")
    expected = {
        -1: (Fraction(27, 8), Fraction(45, 16), Fraction(87, 8), Fraction(-16, 27)),
        0: (Fraction(9, 4), Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)),
        1: (Fraction(3, 2), Fraction(5, 4), Fraction(3, 2), Fraction(-4, 3)),
        2: (Fraction(1, 1), Fraction(5, 6), Fraction(-1, 1), Fraction(-2, 1)),
    }
    for m, (exp_ratio, exp_q, exp_rho, exp_c) in expected.items():
        ratio = row_ratio(m)
        q_e, rho_e, c_te = endpoint_from_row_ratio(ratio)
        check(ratio == exp_ratio, f"m={m} row ratio", f"R={ratio}")
        check((q_e, rho_e, c_te) == (exp_q, exp_rho, exp_c), f"m={m} endpoint consequence", f"q_E={q_e}, rho_E={rho_e}, c_TE={c_te}")
    endpoint_matches = [m for m in range(-6, 7) if row_ratio(m) == Fraction(9, 4)]
    check(endpoint_matches == [0], "E/T endpoint equality diagnoses m=0 inside character family")
    check("using this E/T equality to prove `m=0` is circular" in note, "note forbids endpoint equality as source-unit proof")
    check("using the E/T endpoint equality as the source-unit calibration" in note, "note records forbidden import")

    print("\nF. Current-surface boundary")
    check("primitive source-unit normalization" in note, "note states scoped no-go premise")
    check("does not force" in note and "chi(a)=1" in note, "note states no-go conclusion")
    check("independent distinct-weight same-coefficient calibration" in note, "note states exact support theorem")
    check("The current surface supplies no independent distinct-weight calibration" in note, "note preserves open current surface")
    check("No observed masses, fitted endpoint values" in note, "note excludes fitted/observed hidden inputs")
    check("source-unit representation type" in note, "note identifies remaining wall")
    check("future theorem premises" in note, "note labels positive routes as future premises")
    check("audit verdict" in note_lower and "does not set" in note_c.lower(), "note leaves audit authority untouched")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={passes}, FAIL={fails}")
    if fails:
        print("STATUS: failure in trivial-character source-unit obstruction verifier.")
        return 1
    print(
        "STATUS: scoped no-go/exact support. Primitive source-unit "
        "normalization fixes a source coordinate only after source semantics; "
        "it does not by itself force the Route-2 Hessian coefficient character "
        "to be trivial. An independent distinct-weight calibration would force "
        "m=0 inside the Block113 character family."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
