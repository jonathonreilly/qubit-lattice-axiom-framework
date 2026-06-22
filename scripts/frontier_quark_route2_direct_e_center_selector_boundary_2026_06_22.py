#!/usr/bin/env python3
"""Verify the Route-2 direct E-center selector boundary."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs/QUARK_ROUTE2_DIRECT_E_CENTER_SELECTOR_BOUNDARY_NOTE_2026-06-22.md"
READOUT = ROOT / "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
S3 = ROOT / "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
BLOCK114 = ROOT / "docs/QUARK_ROUTE2_TRIVIAL_CHARACTER_SOURCE_UNIT_OBSTRUCTION_NOTE_2026-06-22.md"
BLOCK113 = ROOT / "docs/QUARK_ROUTE2_SOURCE_UNIT_SCALE_CHARACTER_BOUNDARY_NOTE_2026-06-22.md"
BLOCK112 = ROOT / "docs/QUARK_ROUTE2_NO_SCALE_CURVATURE_COEFFICIENT_NO_GO_NOTE_2026-06-22.md"

passes = 0
fails = 0

RHO_TARGET = Fraction(21, 4)
Q_E_TARGET = Fraction(15, 8)
Q_T = Fraction(5, 6)
S_TE = Fraction(-2, 1)
C_TE_TARGET = Fraction(-8, 9)

E_SHELL = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
E_CENTER = (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0))
T_SHELL = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
T_CENTER = (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6))


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


def p_map(rho: Fraction) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    return (
        (Fraction(1), Fraction(0), rho, Fraction(0)),
        (Fraction(0), Fraction(-2), Fraction(0), Fraction(2)),
    )


def apply_row(row: tuple[Fraction, ...], vector: tuple[Fraction, ...]) -> Fraction:
    return sum(a * b for a, b in zip(row, vector))


def gamma_e_shell(rho: Fraction) -> Fraction:
    return apply_row(p_map(rho)[0], E_SHELL)


def gamma_e_center(rho: Fraction) -> Fraction:
    return apply_row(p_map(rho)[0], E_CENTER)


def gamma_t_shell(rho: Fraction) -> Fraction:
    return apply_row(p_map(rho)[1], T_SHELL)


def gamma_t_center(rho: Fraction) -> Fraction:
    return apply_row(p_map(rho)[1], T_CENTER)


def q_e(rho: Fraction) -> Fraction:
    return gamma_e_center(rho) / gamma_e_shell(rho)


def q_t(rho: Fraction) -> Fraction:
    return gamma_t_center(rho) / gamma_t_shell(rho)


def s_te(rho: Fraction) -> Fraction:
    return gamma_t_shell(rho) / gamma_e_shell(rho)


def c_te(rho: Fraction) -> Fraction:
    return gamma_t_center(rho) / gamma_e_center(rho)


def frobenius_sq(rho: Fraction) -> Fraction:
    return sum(x * x for row in p_map(rho) for x in row)


def main() -> int:
    print("Route-2 direct E-center selector boundary")
    print("=" * 78)

    print("\nA. Source-note and authority boundary")
    note = read(NOTE)
    note_c = compact(note)
    note_lower = note.lower()
    check(NOTE.exists(), "new source note exists", str(NOTE.relative_to(ROOT)))
    check("**Actual current-surface status:** no-go" in note, "new note declares scoped no-go status")
    check("**Claim type:** no_go" in note, "new note declares no_go claim type")
    check("direct readout stretch attempt" in note, "new note records direct-readout stretch role")
    check("The result is negative" in note_c, "new note states selector no-go")
    check("derive q_E = 15/8 directly" in note, "new note states direct positive residue")
    check(
        "proposed_retained" not in note_c
        and "would become retained" not in note_c
        and "retained branch-local" not in note_c,
        "new note has no retained proposal wording",
    )

    authorities = [
        (READOUT, ["P(rho_E)", "beta_E / alpha_E = 21/4", "exact missing-map obstruction"]),
        (S3, ["endpoint triple", "not yet derived", "unique exact `Theta_R -> Lambda_R`"]),
        (BLOCK114, ["E/T endpoint equality", "source-unit normalization"]),
        (BLOCK113, ["g(w) = C w^m", "regular positive-ray scale-character covariance"]),
        (BLOCK112, ["g_E/g_T = 1", "endpoint ratio"]),
    ]
    for path, markers in authorities:
        text = compact(read(path))
        missing = [marker for marker in markers if marker not in text]
        check(not missing, f"{path.name} contains required boundary markers", "; ".join(markers))

    print("\nB. Reduced family algebra")
    for rho in [Fraction(0), Fraction(1), Fraction(2), RHO_TARGET, Fraction(-5)]:
        check(gamma_e_shell(rho) == 1, f"rho={rho} preserves E-shell normalization")
        check(q_t(rho) == Q_T, f"rho={rho} preserves q_T=5/6")
        check(s_te(rho) == S_TE, f"rho={rho} preserves s_TE=-2")
    check(q_e(RHO_TARGET) == Q_E_TARGET, "rho=21/4 gives q_E=15/8")
    check(c_te(RHO_TARGET) == C_TE_TARGET, "rho=21/4 gives c_TE=-8/9")
    check(6 * (Q_E_TARGET - 1) == RHO_TARGET, "q_E=15/8 is equivalent to rho=21/4")
    check("The target `q_E=15/8` is exactly equivalent to `rho=21/4`" in note, "note records target equivalence")

    print("\nC. Direct selector no-go checks")
    positive_samples = [Fraction(-5), Fraction(0), Fraction(1), Fraction(2), RHO_TARGET, Fraction(8)]
    check(all(q_e(rho) >= 0 for rho in positive_samples), "E-center positivity leaves multiple sampled rho values")
    check(all(q_e(rho) >= 0 for rho in [Fraction(-6), Fraction(-5), Fraction(0), RHO_TARGET]), "rho >= -6 sampled positivity condition")
    check(q_e(Fraction(-7)) < 0, "positivity lower wall is nontrivial")
    check(min([Fraction(-5), Fraction(0), Fraction(1), Fraction(2), RHO_TARGET], key=lambda r: abs(q_e(r) - 1)) == 0, "minimal center deformation selects rho=0")
    check(min([Fraction(-5), Fraction(0), Fraction(1), Fraction(2), RHO_TARGET], key=frobenius_sq) == 0, "minimal Frobenius norm selects rho=0")
    check(frobenius_sq(RHO_TARGET) == Fraction(585, 16), "target Frobenius norm is 585/16")
    check(frobenius_sq(Fraction(0)) == 9, "rho=0 Frobenius norm is 9")
    check(frobenius_sq(Fraction(0)) < frobenius_sq(RHO_TARGET), "minimal norm prefers rho=0 over target")
    check("Minimal center deformation" in note and "not `21/4`" in note, "note records minimal-deformation miss")
    check("Minimal matrix norm" in note and "rho = 0" in note, "note records minimal-norm miss")

    print("\nD. Endpoint-chain selector is circular")
    q_from_chain = S_TE * Q_T / C_TE_TARGET
    rho_from_chain = 6 * (q_from_chain - 1)
    check(q_from_chain == Q_E_TARGET, "imported c_TE target forces q_E=15/8")
    check(rho_from_chain == RHO_TARGET, "imported endpoint chain forces rho=21/4")
    check(c_te(Fraction(0)) == Fraction(-5, 3), "rho=0 gives different c_TE")
    check(c_te(Fraction(1)) == Fraction(-10, 7), "rho=1 gives different c_TE")
    check("imports the target endpoint chain" in note_c, "note labels endpoint-chain selector as imported target")
    check("not a direct E-center derivation" in note, "note blocks circular route")

    print("\nE. Current-surface boundary")
    check("does not select" in note and "rho_E = 21/4" in note, "note states scoped no-go conclusion")
    check("derive the E-center excess q_E - 1 = 7/8" in note, "note states exact positive route")
    check("The direct E-center wall is independent" in note, "note separates source-unit chain")
    check("No observed masses, fitted endpoint values" in note, "note excludes fitted/observed hidden inputs")
    check("target endpoint chain is not used as a selector" in note_c, "note preserves selector firewall")
    check("unselected `E`-center map entry" in note, "note matches S3 residual")
    check("future theorem premises" in note, "note labels positive route as future premise")
    check("audit verdict" in note_lower and "does not set" in note_c.lower(), "note leaves audit authority untouched")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={passes}, FAIL={fails}")
    if fails:
        print("STATUS: failure in direct E-center selector verifier.")
        return 1
    print(
        "STATUS: scoped no-go/exact support. Direct shell/T-side/positivity "
        "and minimality selectors do not pick rho_E=21/4 from the restricted "
        "readout family; a direct E-center excess theorem q_E-1=7/8 remains "
        "the needed positive route."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
