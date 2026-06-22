#!/usr/bin/env python3
"""Verify the Route-2 source-unit scale-character boundary."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs/QUARK_ROUTE2_SOURCE_UNIT_SCALE_CHARACTER_BOUNDARY_NOTE_2026-06-22.md"
BLOCK112 = ROOT / "docs/QUARK_ROUTE2_NO_SCALE_CURVATURE_COEFFICIENT_NO_GO_NOTE_2026-06-22.md"
BLOCK111 = ROOT / "docs/QUARK_ROUTE2_SOURCE_ACTION_PRIMITIVE_BOUNDARY_NOTE_2026-06-22.md"
BLOCK110 = ROOT / "docs/QUARK_ROUTE2_LOG_ACTION_COCYCLE_HESSIAN_BOUNDARY_NOTE_2026-06-22.md"
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


def chi(power: int, scale: Fraction) -> Fraction:
    return scale ** power


def g_ratio(power: int) -> Fraction:
    return (W_E / W_T) ** power


def row_ratio(power: int) -> Fraction:
    return (W_E / W_T) ** (power - 2)


def endpoint_from_row_ratio(ratio: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_e = Q_T * ratio
    rho_e = 6 * (q_e - 1)
    c_te = S_TE * Q_T / q_e
    return q_e, rho_e, c_te


def scale_covariant_value(power: int, scale: Fraction, w: Fraction, base_c: Fraction) -> Fraction:
    return base_c * (scale * w) ** power


def main() -> int:
    print("Route-2 source-unit scale-character boundary")
    print("=" * 78)

    print("\nA. Source-note and authority boundary")
    note = read(NOTE)
    note_c = compact(note)
    note_lower = note.lower()
    check(NOTE.exists(), "new source note exists", str(NOTE.relative_to(ROOT)))
    check("**Actual current-surface status:** no-go" in note, "new note declares scoped no-go status")
    check("**Claim type:** no_go" in note, "new note declares no_go claim type")
    check("regular scale covariance" in note, "new note states scale-covariance target")
    check("It is not." in note, "new note states covariance-alone nonselection")
    check("chi(a) = 1" in note, "new note states trivial-character positive route")
    check(
        "proposed_retained" not in note_c
        and "would become retained" not in note_c
        and "retained branch-local" not in note_c,
        "new note has no retained proposal wording",
    )

    authorities = [
        (BLOCK112, ["g(a w) = g(w)", "Homogeneous prefactors", "future theorem premise"]),
        (BLOCK111, ["g(w) Phi''(w)", "constant source unit / no weight-dependent prefactor"]),
        (BLOCK110, ["multiplicative-to-additive cocycle", "Hessian row readout"]),
        (SOURCE_LOG, ["up to scale, not the unit `c=1`", "lambda > 0"]),
        (SOURCE_RN, ["Fisher norm `lambda^2`", "primitive unit source coordinate"]),
        (SOURCE_PLANCK, ["bounded bridge", "Fisher norm `lambda^2`"]),
        (YT_UNIT, ["lambda family preserves all current structural tests", "lambda = 1"]),
        (S3, ["endpoint triple", "not yet derived"]),
    ]
    for path, markers in authorities:
        text = compact(read(path))
        missing = [marker for marker in markers if marker not in text]
        check(not missing, f"{path.name} contains required boundary markers", "; ".join(markers))

    print("\nB. Multiplicative character algebra")
    scales = [Fraction(2, 3), Fraction(3, 5), Fraction(5, 4)]
    for power in [-2, -1, 0, 1, 2, 3]:
        for a in scales:
            for b in scales:
                check(chi(power, a * b) == chi(power, a) * chi(power, b), f"m={power} character law for a={a}, b={b}")
        check(chi(power, Fraction(1)) == 1, f"m={power} character identity")
        check(chi(power, Fraction(3, 2)) * chi(power, Fraction(2, 3)) == 1, f"m={power} inverse character law")

    print("\nC. Scale-covariant coefficient witnesses")
    base_c = Fraction(7, 5)
    for power in [-1, 0, 1, 2]:
        for scale in [Fraction(2, 3), Fraction(3, 2)]:
            for w in [W_E, W_T, Fraction(5, 12)]:
                left = scale_covariant_value(power, scale, w, base_c)
                right = chi(power, scale) * scale_covariant_value(power, Fraction(1), w, base_c)
                check(left == right, f"m={power} satisfies g(a w)=chi(a)g(w)", f"a={scale}, w={w}")
        check(scale_covariant_value(power, Fraction(1), W_E, base_c) / scale_covariant_value(power, Fraction(1), W_T, base_c) == g_ratio(power), f"m={power} coefficient E/T ratio", f"g_E/g_T={g_ratio(power)}")

    print("\nD. Endpoint consequences")
    expected = {
        -1: (Fraction(3, 2), Fraction(27, 8), Fraction(45, 16), Fraction(87, 8), Fraction(-16, 27)),
        0: (Fraction(1, 1), Fraction(9, 4), Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)),
        1: (Fraction(2, 3), Fraction(3, 2), Fraction(5, 4), Fraction(3, 2), Fraction(-4, 3)),
        2: (Fraction(4, 9), Fraction(1, 1), Fraction(5, 6), Fraction(-1, 1), Fraction(-2, 1)),
    }
    for power, (exp_g, exp_row, exp_q, exp_rho, exp_c) in expected.items():
        got_g = g_ratio(power)
        got_row = row_ratio(power)
        got_q, got_rho, got_c = endpoint_from_row_ratio(got_row)
        check(got_g == exp_g, f"m={power} g_E/g_T", f"g_ratio={got_g}")
        check(got_row == exp_row, f"m={power} row ratio", f"R={got_row}")
        check((got_q, got_rho, got_c) == (exp_q, exp_rho, exp_c), f"m={power} endpoint consequence", f"q_E={got_q}, rho_E={got_rho}, c_TE={got_c}")
    target_ms = [power for power in range(-6, 7) if row_ratio(power) == Fraction(9, 4)]
    check(target_ms == [0], "integer character scan hits endpoint only at m=0", f"target_ms={target_ms}")
    check(row_ratio(0) == Fraction(9, 4), "trivial character gives Hessian endpoint ratio")
    check(row_ratio(1) == Fraction(3, 2), "nontrivial character m=1 misses endpoint")
    check(row_ratio(2) == Fraction(1, 1), "nontrivial character m=2 misses endpoint")
    check("m = 0" in note, "note states endpoint selects m=0 inside character family")
    check("Concrete integer witnesses:" in note, "note displays character counter-witnesses")

    print("\nE. Endpoint equality is not an independent source-unit proof")
    endpoint_diagnostic = (Fraction(2, 3) ** 0 == 1) and all(Fraction(2, 3) ** m != 1 for m in [-3, -2, -1, 1, 2, 3])
    check(endpoint_diagnostic, "character family endpoint diagnostic selects trivial integer witness only")
    check("Diagnostic, Not A Source Law" in note, "note labels endpoint equality as diagnostic")
    check("uses the endpoint equality" in note_c.lower(), "note forbids using target endpoint as proof")
    check("plugging in the target endpoint" in note, "note states source theorem must be independent")

    print("\nF. Source-scale analogy boundary")
    check("W_c = c log Z" in note, "note records log-coordinate scale analogy")
    check("Fisher norm `lambda^2`" in note, "note records RN scale analogy")
    check("transfers only the discipline, not the conclusion" in note, "note avoids importing source-measure conclusion")
    check("zero-weight theorem" in note, "note names the Route-2-specific missing theorem")
    check("regular source scale" in note, "note states regular scale is too weak")

    print("\nG. Current-surface boundary")
    check("Forbidden proof inputs:" in note and "observed masses" in note, "note records forbidden proof-input firewall")
    check("assuming from the start that the coefficient character is trivial" in note, "note forbids importing trivial character")
    check("using endpoint equality as a proof" in note, "note forbids endpoint-as-source-law proof")
    check("regular positive-ray scale-character covariance of g" in note, "note states scoped no-go")
    check("The current surface still does not derive" in note, "note preserves open current surface")
    check("No observed masses, fitted endpoint values" in note, "note excludes fitted/observed hidden inputs")
    check("zero-weight coefficient theorem" in note, "note matches S3/Route-2 residual")
    check("future theorem premises" in note, "note labels positive route as future premise")
    check("audit verdict" in note_lower and "does not set" in note_c.lower(), "note leaves audit authority untouched")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={passes}, FAIL={fails}")
    if fails:
        print("STATUS: failure in source-unit scale-character verifier.")
        return 1
    print(
        "STATUS: scoped no-go/exact support. Regular positive-ray scale-character "
        "covariance reduces the coefficient freedom to g(w)=C w^m but does not "
        "select the trivial character m=0. A future Route-2 source-unit theorem "
        "forcing chi(a)=1 would close the Block112 coefficient subgate."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
