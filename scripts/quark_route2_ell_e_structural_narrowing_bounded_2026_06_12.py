#!/usr/bin/env python3
"""Exact structural narrowing checks for Route-2 ell_E.

This runner uses only rational endpoint algebra. It verifies:

* endpoint quotients reduce ell_E to a projective slope rho_E;
* positivity narrows the projective family to rho_E > -6;
* norm/idempotency normalization fixes representative scale but not slope;
* the Route-2 center-ratio sign is negative throughout the positive family
  under the granted T-side orientation;
* the exact Fierz fraction is positive magnitude support, not a signed
  Route-2 endpoint bridge by itself.

No randomness, date-dependent input, live fitted endpoint comparator, external
citation, or physical kappa_EW weighting rule is used.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys


PASS_COUNT = 0
FAIL_COUNT = 0

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md"
)

DELTA_CENTER = Fraction(1, 6)
RHO_T = Fraction(-1, 1)
S_TE = Fraction(-2, 1)
Q_T = Fraction(5, 6)
F_ADJ_NC3 = Fraction(8, 9)
TARGET_C_TE = Fraction(-8, 9)
TARGET_Q_E = Fraction(15, 8)
TARGET_RHO_E = Fraction(21, 4)


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        print(f"PASS: {name}")
    else:
        FAIL_COUNT += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def q_e(rho_e: Fraction) -> Fraction:
    return Fraction(1, 1) + rho_e * DELTA_CENTER


def rho_from_q(q: Fraction) -> Fraction:
    return Fraction(6, 1) * (q - 1)


def c_te_from_q(q: Fraction, s_te: Fraction = S_TE) -> Fraction:
    return s_te * Q_T / q


def c_te_from_rho(rho_e: Fraction, s_te: Fraction = S_TE) -> Fraction:
    return c_te_from_q(q_e(rho_e), s_te)


def f_adj(n_c: int) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def same_projective_endpoint(
    alpha: Fraction, beta: Fraction, scale: Fraction
) -> bool:
    if alpha == 0 or scale == 0:
        return False
    rho = beta / alpha
    scaled_alpha = scale * alpha
    scaled_beta = scale * beta
    scaled_rho = scaled_beta / scaled_alpha
    shell = alpha
    center = alpha + beta * DELTA_CENTER
    scaled_shell = scaled_alpha
    scaled_center = scaled_alpha + scaled_beta * DELTA_CENTER
    return (
        scaled_rho == rho
        and center / shell == scaled_center / scaled_shell
        and center / shell == q_e(rho)
    )


def positive_e_family(alpha: Fraction, beta: Fraction) -> bool:
    return alpha > 0 and alpha + beta * DELTA_CENTER > 0


def unit_norm_squared_pair(rho_e: Fraction) -> tuple[Fraction, Fraction]:
    denom = Fraction(1, 1) + rho_e * rho_e
    return Fraction(1, 1) / denom, (rho_e * rho_e) / denom


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Quark Route-2 ell_E structural narrowing bounded checks")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set, predict, promote, or demote any audit outcome."
    )
    print("No new imports: exact rational endpoint algebra only.")

    print()
    print("Endpoint/projective structure")
    check("delta_A1(center) is 1/6 exactly", DELTA_CENTER == Fraction(1, 6))
    check("T-side rho_T=-1 gives q_T=5/6 exactly", 1 + RHO_T / 6 == Q_T)
    check("target q_E=15/8 gives rho_E=21/4 exactly", rho_from_q(TARGET_Q_E) == TARGET_RHO_E)
    check("target rho_E=21/4 gives q_E=15/8 exactly", q_e(TARGET_RHO_E) == TARGET_Q_E)
    check(
        "endpoint quotient is scale invariant for a sample E row",
        same_projective_endpoint(Fraction(2, 3), Fraction(7, 5), Fraction(11, 4)),
    )
    check(
        "endpoint quotient is scale invariant for a negative-scale sample",
        same_projective_endpoint(Fraction(-3, 2), Fraction(5, 7), Fraction(-9, 5)),
    )
    check(
        "alpha_E=0 is outside the endpoint quotient domain",
        not same_projective_endpoint(Fraction(0, 1), Fraction(1, 1), Fraction(2, 1)),
    )
    check(
        "rho_E=0 and rho_E=21/4 are distinct projective directions",
        Fraction(0, 1) != TARGET_RHO_E and q_e(0) != q_e(TARGET_RHO_E),
        f"q(0)={q_e(Fraction(0, 1))}, q(target)={q_e(TARGET_RHO_E)}",
    )

    print()
    print("Positivity and normalization")
    check(
        "positive shell and center are equivalent to rho_E > -6 in sample target",
        positive_e_family(Fraction(1, 1), TARGET_RHO_E)
        and TARGET_RHO_E > Fraction(-6, 1),
    )
    check(
        "rho_E=0 is inside the positive projective family",
        positive_e_family(Fraction(1, 1), Fraction(0, 1)),
    )
    check(
        "rho_E=-7 violates E-center positivity",
        not positive_e_family(Fraction(1, 1), Fraction(-7, 1)),
    )
    check(
        "rho_E=-6 is the zero-center boundary, not a valid center quotient",
        q_e(Fraction(-6, 1)) == 0,
    )
    a2_zero, b2_zero = unit_norm_squared_pair(Fraction(0, 1))
    a2_target, b2_target = unit_norm_squared_pair(TARGET_RHO_E)
    check("unit normalization admits rho_E=0", a2_zero + b2_zero == 1)
    check("unit normalization admits rho_E=21/4", a2_target + b2_target == 1)
    check(
        "unit normalization changes scale but not projective slope",
        b2_target / a2_target == TARGET_RHO_E * TARGET_RHO_E,
        f"beta^2/alpha^2={b2_target / a2_target}",
    )
    check(
        "two unit-normalized slopes remain distinct",
        (a2_zero, b2_zero) != (a2_target, b2_target),
        f"rho0 squares={(a2_zero, b2_zero)}, target squares={(a2_target, b2_target)}",
    )

    print()
    print("Sign separation")
    check("F_adj(N_c=3) is 8/9 exactly", f_adj(3) == F_ADJ_NC3)
    check("F_adj(N_c=2) is positive", f_adj(2) == Fraction(3, 4) and f_adj(2) > 0)
    check("F_adj(N_c=4) is positive", f_adj(4) == Fraction(15, 16) and f_adj(4) > 0)
    check(
        "Fierz dimension fraction alone has positive sign",
        F_ADJ_NC3 > 0 and -F_ADJ_NC3 == TARGET_C_TE,
        f"F_adj={F_ADJ_NC3}, -F_adj={-F_ADJ_NC3}",
    )
    check(
        "correct T orientation gives negative c_TE at rho_E=0",
        c_te_from_rho(Fraction(0, 1)) == Fraction(-5, 3)
        and c_te_from_rho(Fraction(0, 1)) < 0,
    )
    check(
        "correct T orientation gives negative c_TE at target rho_E",
        c_te_from_rho(TARGET_RHO_E) == TARGET_C_TE
        and c_te_from_rho(TARGET_RHO_E) < 0,
    )
    check(
        "positive E-family sample rho_E=1 still has negative sign",
        c_te_from_rho(Fraction(1, 1)) == Fraction(-10, 7)
        and c_te_from_rho(Fraction(1, 1)) < 0,
    )
    check(
        "wrong T orientation flips the sign for positive q_E",
        c_te_from_rho(TARGET_RHO_E, s_te=Fraction(2, 1)) == Fraction(8, 9),
    )
    check(
        "violating E-center positivity flips the sign despite correct T orientation",
        c_te_from_rho(Fraction(-7, 1)) == Fraction(10, 1),
    )
    check(
        "sign-only does not pin the magnitude",
        c_te_from_rho(Fraction(0, 1)) < 0
        and c_te_from_rho(Fraction(0, 1)) != TARGET_C_TE,
        f"rho=0 gives c_TE={c_te_from_rho(Fraction(0, 1))}",
    )
    check(
        "c_TE=-8/9 pins q_E=15/8 exactly",
        (S_TE * Q_T) / TARGET_C_TE == TARGET_Q_E,
    )
    check(
        "c_TE=-8/9 pins rho_E=21/4 exactly",
        rho_from_q((S_TE * Q_T) / TARGET_C_TE) == TARGET_RHO_E,
    )

    print()
    print("Note hygiene")
    text = note_text()
    check("note file exists", bool(text))
    check(
        "note has status-authority block",
        "Status authority: independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome."
        in text,
    )
    check("note uses canonical bounded_theorem claim type", "**Claim type:** bounded_theorem" in text)
    for required in [
        "[QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md]",
        "[S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md]",
        "[ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md]",
        "[RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md]",
        "[QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md]",
        "[QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md]",
    ]:
        check(f"note links authority {required}", required in text)
    check("note avoids branch-local scratch references", ".claude/tmp/refs" not in text)
    banned_phrases = [
        ("sole-route phrasing", "only " + "route"),
        ("terminal-route phrasing", "last " + "route"),
        ("depletion phrasing", "ex" + "hausted"),
        ("program-closure phrasing", "closes the " + "program"),
        ("audit-clean status token", "audited" + "_clean"),
        ("retention-status prefix", "retain" + "ed_"),
    ]
    for label, banned in banned_phrases:
        check(f"note avoids {label}", banned not in text)
    check("note records narrowed positive projective family", "rho_E > -6" in text)
    check("note records sign separation", "c_TE < 0" in text)
    check("note records exact target arithmetic", "rho_E = 21/4" in text and "c_TE = -8/9" in text)

    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
