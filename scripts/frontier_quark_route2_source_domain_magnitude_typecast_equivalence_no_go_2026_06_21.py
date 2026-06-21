#!/usr/bin/env python3
"""Magnitude/typecast equivalence no-go for the Route-2 E-center bridge."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def doc(name: str) -> str:
    path = DOCS / name
    check(f"{name} exists", path.exists(), str(path.relative_to(ROOT)))
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def q_e(rho_e: Fraction) -> Fraction:
    return 1 + rho_e / 6


def c_te(rho_e: Fraction) -> Fraction:
    return Fraction(-2, 1) * Fraction(5, 6) / q_e(rho_e)


def abs_c_te(rho_e: Fraction) -> Fraction:
    return abs(c_te(rho_e))


def rho_from_abs_c_te(magnitude: Fraction) -> Fraction:
    return Fraction(10, 1) / magnitude - 6


def f_adj(n_c: int = 3) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def main() -> int:
    print("Route-2 source-domain magnitude/typecast equivalence no-go")
    print("=" * 78)

    new_note = doc("QUARK_ROUTE2_SOURCE_DOMAIN_MAGNITUDE_TYPECAST_EQUIVALENCE_NO_GO_NOTE_2026-06-21.md")
    positivity_note = doc("ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md")
    naturality_note = doc("QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md")
    readout_note = doc("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    rconn_note = doc("RCONN_DERIVED_NOTE.md")
    source_note = doc("QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md")

    print()
    print("A. Source anchors")
    print("-" * 78)
    check(
        "new note records magnitude/typecast equivalence sections",
        all(
            phrase in flat(new_note)
            for phrase in (
                "Magnitude equivalence",
                "Typecast no-go",
                "rho_E = 10 / |c_TE| - 6",
                "not a weaker scalar condition",
                "does not supply a typed source-domain theorem",
            )
        ),
    )
    check(
        "positivity note supplies positive-lift domain",
        "one-sided bound** `rho_E > -6`" in flat(positivity_note),
    )
    check(
        "naturality note supplies q_T and shell ratio",
        "given the granted T-side values `q_T = 5/6` and `gamma_T(shell)/gamma_E(shell) = -2`"
        in flat(naturality_note),
    )
    check(
        "readout note states c_TE algebra",
        "c_TE := gamma_T(center) / gamma_E(center) = s_TE * q_T / q_E." in flat(readout_note),
    )
    check("Rconn note supplies F_adj=8/9", "At `N_c = 3`, `F_adj = 8/9`" in rconn_note)
    check(
        "source-domain note keeps typed bridge missing",
        "There is no current typed edge" in source_note
        and "R_conn = 8/9 -> c_TE = gamma_T(center)/gamma_E(center) = -8/9" in source_note,
    )

    print()
    print("B. Magnitude equivalence")
    print("-" * 78)
    samples = (
        Fraction(-11, 2),
        Fraction(-1, 1),
        Fraction(0, 1),
        Fraction(1, 1),
        Fraction(21, 4),
        Fraction(12, 1),
    )
    for rho in samples:
        m = abs_c_te(rho)
        check(
            f"rho_E={rho} round-trips through |c_TE|",
            rho_from_abs_c_te(m) == rho,
            f"|c_TE|={m}, roundtrip={rho_from_abs_c_te(m)}",
        )
    check(
        "positive-lift magnitude map is injective on tested samples",
        len({abs_c_te(rho) for rho in samples}) == len(samples),
    )
    check(
        "magnitude formula sends F_adj=8/9 to rho_E=21/4",
        rho_from_abs_c_te(f_adj(3)) == Fraction(21, 4),
        str(rho_from_abs_c_te(f_adj(3))),
    )
    check(
        "target rho_E has |c_TE|=F_adj",
        abs_c_te(Fraction(21, 4)) == f_adj(3),
        str(abs_c_te(Fraction(21, 4))),
    )

    print()
    print("C. Magnitude candidates are readout selectors")
    print("-" * 78)
    candidates = {
        "F_adj_SU2": f_adj(2),
        "F_adj_SU3": f_adj(3),
        "F_adj_SU4": f_adj(4),
        "unit": Fraction(1, 1),
        "five_sixths": Fraction(5, 6),
    }
    expected = {
        "F_adj_SU2": Fraction(22, 3),
        "F_adj_SU3": Fraction(21, 4),
        "F_adj_SU4": Fraction(14, 3),
        "unit": Fraction(4, 1),
        "five_sixths": Fraction(6, 1),
    }
    for name, magnitude in candidates.items():
        check(
            f"{name} magnitude selects its own rho_E",
            rho_from_abs_c_te(magnitude) == expected[name],
            f"rho_E={rho_from_abs_c_te(magnitude)}",
        )
    check(
        "choosing F_adj_SU3 is exactly choosing one magnitude in a continuum",
        len({rho_from_abs_c_te(mag) for mag in candidates.values()}) == len(candidates),
    )

    print()
    print("D. Boundary inventory")
    print("-" * 78)
    for phrase in (
        "|c_TE| = F_adj",
        "route2_center_TE_minus_8_9",
        "route2_q_E_15_8",
        "route2_rho_E_21_4",
        "magnitude/typecast equality is the missing selection",
    ):
        check(f"new note lists boundary phrase: {phrase}", phrase in new_note)
    check(
        "new note keeps future positive theorem open",
        "future positive theorem" in new_note
        and "must source the magnitude/typecast equality" in flat(new_note),
    )

    print()
    print("Summary")
    print("-" * 78)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: |c_TE|=F_adj is equivalent to E-center readout selection unless independently typed.")
        return 0
    print("VERDICT: magnitude/typecast equivalence checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
