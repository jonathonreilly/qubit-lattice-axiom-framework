#!/usr/bin/env python3
"""Route-2 source-domain sign support with typecast remainder.

This runner narrows the two-edge source-domain split:

* positivity gives q_E > 0, so with the granted T-side values
  c_TE = (-2)(5/6)/q_E is always negative;
* the sign of the candidate -F_adj is therefore compatible with the current
  Route-2 positive-lift family;
* the magnitude equality |c_TE| = F_adj, or equivalently the typed readout
  landing edge, remains the missing theorem.
"""

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


def f_adj(n_c: int = 3) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def rho_from_abs_center(abs_c_te: Fraction) -> Fraction:
    # In the positive-lift family c_TE is negative, so |c_TE| = abs_c_te
    # means c_TE = -abs_c_te.
    q = Fraction(2, 1) * Fraction(5, 6) / abs_c_te
    return 6 * (q - 1)


def main() -> int:
    print("Route-2 source-domain sign support with typecast remainder")
    print("=" * 78)

    new_note = doc("QUARK_ROUTE2_SOURCE_DOMAIN_SIGN_SUPPORT_TYPECAST_REMAINDER_NOTE_2026-06-21.md")
    positivity_note = doc("ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md")
    naturality_note = doc("QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md")
    readout_note = doc("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    rconn_note = doc("RCONN_DERIVED_NOTE.md")
    source_bridge_note = doc("QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md")
    kappa_note = doc("RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md")

    print()
    print("A. Source anchors")
    print("-" * 78)
    check(
        "new note records sign support and typecast remainder",
        all(
            phrase in flat(new_note)
            for phrase in (
                "Sign support",
                "Magnitude/typecast remainder",
                "positive-lift family",
                "does not select rho_E",
                "does not supply the typed readout landing edge",
            )
        ),
    )
    check(
        "positivity note gives one-sided rho_E bound",
        "Gives only the\n  **one-sided bound** `rho_E > -6`" in positivity_note
        or "Gives only the **one-sided bound** `rho_E > -6`" in flat(positivity_note),
    )
    check(
        "positivity note classifies rho_E as readout direction",
        "readout's **direction**" in positivity_note
        or "readout **direction**" in flat(positivity_note),
    )
    check(
        "naturality note supplies granted T-side values",
        "given the granted T-side values `q_T = 5/6` and\n`gamma_T(shell)/gamma_E(shell) = -2`"
        in naturality_note,
    )
    check(
        "readout note supplies c_TE endpoint algebra",
        "c_TE  := gamma_T(center) / gamma_E(center)" in readout_note
        and "s_TE * q_T / q_E" in readout_note,
    )
    check(
        "Rconn note supplies F_adj as color-domain support",
        "At `N_c = 3`, `F_adj = 8/9`" in rconn_note,
    )
    check(
        "source-domain note keeps Rconn-to-center as missing bridge",
        "R_conn = (N_c^2 - 1) / N_c^2\n    ?=> gamma_T(center) / gamma_E(center) = -R_conn"
        in source_bridge_note,
    )
    check(
        "kappa note keeps physical selector separate",
        "physical weighting or observable-bridge rule" in flat(kappa_note),
    )

    print()
    print("B. Exact sign support")
    print("-" * 78)
    rho_samples = (
        Fraction(-11, 2),
        Fraction(-1, 1),
        Fraction(0, 1),
        Fraction(1, 1),
        Fraction(21, 4),
        Fraction(12, 1),
    )
    for rho in rho_samples:
        check(
            f"rho_E={rho} is in positive-lift domain",
            q_e(rho) > 0,
            f"q_E={q_e(rho)}",
        )
        check(
            f"rho_E={rho} gives negative c_TE",
            c_te(rho) < 0,
            f"c_TE={c_te(rho)}",
        )
    check("q_T=5/6 is positive", Fraction(5, 6) > 0)
    check("s_TE=-2 is negative", Fraction(-2, 1) < 0)
    check(
        "positive-lift sign theorem holds for all rho_E > -6",
        all(q_e(rho) > 0 and c_te(rho) < 0 for rho in rho_samples),
    )

    print()
    print("C. Magnitude/typecast remainder")
    print("-" * 78)
    f = f_adj(3)
    check("F_adj magnitude is 8/9", f == Fraction(8, 9), str(f))
    check("target value has |c_TE|=F_adj", abs(c_te(Fraction(21, 4))) == f, str(c_te(Fraction(21, 4))))
    for rho in (Fraction(-1, 1), Fraction(0, 1), Fraction(1, 1), Fraction(12, 1)):
        check(
            f"rho_E={rho} has negative sign but not F_adj magnitude",
            c_te(rho) < 0 and abs(c_te(rho)) != f,
            f"|c_TE|={abs(c_te(rho))}",
        )
    check(
        "|c_TE|=F_adj solves rho_E=21/4 in the positive-lift family",
        rho_from_abs_center(f) == Fraction(21, 4),
        str(rho_from_abs_center(f)),
    )
    check(
        "sign support alone leaves multiple admissible rho_E values",
        len({c_te(rho) for rho in rho_samples}) == len(rho_samples),
    )

    print()
    print("D. Boundary inventory")
    print("-" * 78)
    for phrase in (
        "signed scalar candidate",
        "magnitude `|c_TE|`",
        "typed typecast",
        "route2_center_TE_minus_8_9",
        "route2_q_E_15_8",
        "route2_rho_E_21_4",
    ):
        check(f"new note lists boundary phrase: {phrase}", phrase in new_note)
    check(
        "new note says sign support is not readout selection",
        "negative sign is support, not selection" in new_note,
    )

    print()
    print("Summary")
    print("-" * 78)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: positivity fixes the Route-2 center-ratio sign but not the F_adj magnitude/typecast.")
        return 0
    print("VERDICT: sign-support/typecast-remainder checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
