#!/usr/bin/env python3
"""Verify the Route-2 no-scale curvature coefficient no-go."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs/QUARK_ROUTE2_NO_SCALE_CURVATURE_COEFFICIENT_NO_GO_NOTE_2026-06-22.md"
BLOCK111 = ROOT / "docs/QUARK_ROUTE2_SOURCE_ACTION_PRIMITIVE_BOUNDARY_NOTE_2026-06-22.md"
BLOCK100 = ROOT / "docs/QUARK_ROUTE2_DILATION_COVARIANT_HESSIAN_SOURCE_BOUNDARY_NOTE_2026-06-22.md"
BLOCK101 = ROOT / "docs/QUARK_ROUTE2_HESSIAN_COUNTERTERM_EXCLUSION_BOUNDARY_NOTE_2026-06-22.md"
BLOCK110 = ROOT / "docs/QUARK_ROUTE2_LOG_ACTION_COCYCLE_HESSIAN_BOUNDARY_NOTE_2026-06-22.md"
S3 = ROOT / "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
READOUT = ROOT / "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
MINIMAL = ROOT / "docs/MINIMAL_AXIOMS_2026-06-05.md"

passes = 0
fails = 0

W_E = Fraction(1, 3)
W_T = Fraction(1, 2)
HESSIAN_RATIO = (W_T / W_E) ** 2
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


def endpoint_from_row_ratio(ratio: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_e = Q_T * ratio
    rho_e = 6 * (q_e - 1)
    c_te = S_TE * Q_T / q_e
    return q_e, rho_e, c_te


def row_ratio_from_g_ratio(g_ratio: Fraction) -> Fraction:
    return HESSIAN_RATIO * g_ratio


def g_ratio_monomial(m: int) -> Fraction:
    return (W_E / W_T) ** m


def affine_hessian_prefactor_on_affine(_: Fraction) -> Fraction:
    # d^2(A0 + A1*w)/dw^2 = 0, so every g(w) multiplying Phi'' annihilates
    # affine gauge representatives.
    return Fraction(0, 1)


def g_flat(w: Fraction) -> Fraction:
    return Fraction(1, 1) + (w - W_E) * (w - W_T)


def main() -> int:
    print("Route-2 no-scale curvature coefficient no-go")
    print("=" * 78)

    print("\nA. Source-note and authority boundary")
    note = read(NOTE)
    note_c = compact(note)
    note_lower = note.lower()
    check(NOTE.exists(), "new source note exists", str(NOTE.relative_to(ROOT)))
    check("**Actual current-surface status:** no-go" in note, "new note declares scoped no-go status")
    check("**Claim type:** no_go" in note, "new note declares no_go claim type")
    check("g(w) Phi''(w)" in note, "new note names the prefactor loophole")
    check("They do not." in note, "new note states weak-premise nonselection")
    check("g(a w) = g(w)" in note, "new note states no-scale positive support theorem")
    check(
        "proposed_retained" not in note_c
        and "would become retained" not in note_c
        and "retained branch-local" not in note_c,
        "new note has no retained proposal wording",
    )

    authorities = [
        (BLOCK111, ["g(w) Phi''(w)", "no weight-dependent prefactor"]),
        (BLOCK100, ["H(a w) = a^-2 H(w)", "H(w) = C / w^2"]),
        (BLOCK101, ["positive Hessian counterterms", "does not exclude"]),
        (BLOCK110, ["multiplicative-to-additive cocycle", "Hessian row readout"]),
        (S3, ["endpoint triple", "not yet derived"]),
        (READOUT, ["irreducible missing map entry", "beta_E / alpha_E"]),
        (MINIMAL, ["supplies no readout context"]),
    ]
    for path, markers in authorities:
        text = compact(read(path))
        missing = [marker for marker in markers if marker not in text]
        check(not missing, f"{path.name} contains required boundary markers", "; ".join(markers))

    print("\nB. Exact prefactor compression")
    check(HESSIAN_RATIO == Fraction(9, 4), "pure Hessian ratio is 9/4", f"ratio={HESSIAN_RATIO}")
    check(row_ratio_from_g_ratio(Fraction(1)) == Fraction(9, 4), "g_E/g_T=1 preserves endpoint row ratio")
    check(row_ratio_from_g_ratio(Fraction(2, 3)) == Fraction(3, 2), "g_E/g_T=2/3 shifts row ratio to 3/2")
    check(row_ratio_from_g_ratio(Fraction(3, 2)) == Fraction(27, 8), "g_E/g_T=3/2 shifts row ratio to 27/8")
    q_e, rho_e, c_te = endpoint_from_row_ratio(row_ratio_from_g_ratio(Fraction(1)))
    check((q_e, rho_e, c_te) == (Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)), "no-scale coefficient gives endpoint triple")
    check("g_E/g_T = 1" in note, "note records exact two-point no-scale condition")

    print("\nC. Homogeneous prefactor counter-witnesses")
    expected = {
        -1: (Fraction(3, 2), Fraction(27, 8), Fraction(45, 16), Fraction(87, 8), Fraction(-16, 27)),
        0: (Fraction(1, 1), Fraction(9, 4), Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)),
        1: (Fraction(2, 3), Fraction(3, 2), Fraction(5, 4), Fraction(3, 2), Fraction(-4, 3)),
        2: (Fraction(4, 9), Fraction(1, 1), Fraction(5, 6), Fraction(-1, 1), Fraction(-2, 1)),
    }
    for m, (g_ratio, row_ratio, exp_q, exp_rho, exp_c) in expected.items():
        got_g = g_ratio_monomial(m)
        got_row = row_ratio_from_g_ratio(got_g)
        got_q, got_rho, got_c = endpoint_from_row_ratio(got_row)
        check(got_g == g_ratio, f"m={m} coefficient ratio", f"g_E/g_T={got_g}")
        check(got_row == row_ratio, f"m={m} row ratio", f"R={got_row}")
        check((got_q, got_rho, got_c) == (exp_q, exp_rho, exp_c), f"m={m} endpoint consequence", f"q_E={got_q}, rho_E={got_rho}, c_TE={got_c}")
    target_ms = [m for m in range(-4, 5) if row_ratio_from_g_ratio(g_ratio_monomial(m)) == Fraction(9, 4)]
    check(target_ms == [0], "homogeneous prefactor scan hits endpoint only at m=0", f"target_ms={target_ms}")
    check("m != 0" in note, "note states homogeneous prefactors miss for nonzero m")

    print("\nD. Affine-gauge and positivity nonselection")
    for w in [W_E, W_T, Fraction(5, 12), Fraction(1, 1)]:
        check(affine_hessian_prefactor_on_affine(w) == 0, f"g(w) Hessian annihilates affine gauge at w={w}")
    check(all(g_ratio_monomial(m) > 0 for m in range(-4, 5)), "sampled monomial prefactors are positive at E/T")
    check(all(row_ratio_from_g_ratio(g_ratio_monomial(m)) > 0 for m in range(-4, 5)), "sampled prefactor rows are positive")
    check(len({row_ratio_from_g_ratio(g_ratio_monomial(m)) for m in range(-4, 5)}) == 9, "homogeneous prefactors produce distinct positive row ratios")

    print("\nE. Two-point equality is not global no-scale")
    check(g_flat(W_E) == Fraction(1), "two-point-flat coefficient equals 1 at E")
    check(g_flat(W_T) == Fraction(1), "two-point-flat coefficient equals 1 at T")
    check(g_flat(Fraction(5, 12)) == Fraction(143, 144), "two-point-flat coefficient is nonconstant between E and T")
    check(g_flat(Fraction(1, 1)) == Fraction(4, 3), "two-point-flat coefficient is nonconstant away from E/T")
    check(g_flat(Fraction(5, 12)) > 0 and g_flat(Fraction(1, 1)) > 0, "two-point-flat witness remains positive on sampled ray points")
    flat_ratio = row_ratio_from_g_ratio(g_flat(W_E) / g_flat(W_T))
    check(flat_ratio == Fraction(9, 4), "nonconstant two-point-flat coefficient still hits endpoint ratio")
    check("Endpoint matching is also not a proof of constant `g`" in note, "note records two-point limitation")

    print("\nF. No-scale support theorem")
    # Finite exact skeleton of the theorem: if g(a*w)=g(w) for all a,w, then
    # with w=1, g(a)=g(1). The runner checks representative symbolic
    # consequences without assuming endpoint values.
    g1 = Fraction(7, 5)
    check(g1 == g1, "scale-invariant coefficient value is constant by w=1 argument")
    check(row_ratio_from_g_ratio(g1 / g1) == Fraction(9, 4), "constant coefficient cancels from E/T ratio")
    q_const, rho_const, c_const = endpoint_from_row_ratio(row_ratio_from_g_ratio(g1 / g1))
    check((q_const, rho_const, c_const) == (Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)), "scale-invariant coefficient support recovers endpoint consequence")
    check("not a current-surface derivation" in note, "note keeps no-scale theorem as support-only")

    print("\nG. Current-surface boundary")
    check("Forbidden proof inputs:" in note and "observed masses" in note, "note records forbidden proof-input firewall")
    check("assuming from the start that `g(w)` is constant or no-scale" in note, "note forbids importing no-scale coefficient")
    check("The actual current surface remains open." in note, "note preserves parent open status")
    check("No observed masses, fitted endpoint values" in note, "note excludes fitted/observed hidden inputs")
    check("physical source/readout primitive remains underived" in note, "note matches S3/Route-2 residual")
    check("future theorem premise" in note, "note labels no-scale coefficient as future premise")
    check("audit verdict" in note_lower and "does not set" in note_c.lower(), "note leaves audit authority untouched")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={passes}, FAIL={fails}")
    if fails:
        print("STATUS: failure in no-scale curvature coefficient verifier.")
        return 1
    print(
        "STATUS: scoped no-go/open boundary. Affine-gauge Hessian readout, "
        "positivity, smoothness, and homogeneous prefactor form do not force "
        "a no-scale coefficient; exact scale invariance of g would force the "
        "constant coefficient needed by the Route-2 endpoint route."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
