#!/usr/bin/env python3
"""Deterministic exact-rational verifier for the W73 E-channel construction.

The runner checks the algebraic source/readout construction in
docs/QUARK_ROUTE2_E_CHANNEL_SOURCE_READOUT_CONSTRUCTION_BOUNDED_NOTE_2026-06-12.md.
It uses Fraction arithmetic for every derived value and static text checks for
the audit-facing boundaries.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

PASS = 0
FAIL = 0

REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "docs" / "QUARK_ROUTE2_E_CHANNEL_SOURCE_READOUT_CONSTRUCTION_BOUNDED_NOTE_2026-06-12.md"


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS: {name} {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {name} {detail}")


def f_adj(nc: int) -> Fraction:
    return Fraction(nc * nc - 1, nc * nc)


def q_from_rho(rho: Fraction, denominator: int = 6) -> Fraction:
    return Fraction(1, 1) + rho / denominator


def rho_from_q(q: Fraction, denominator: int = 6) -> Fraction:
    return denominator * (q - 1)


def q_e_from_center_bridge(
    c_te: Fraction,
    *,
    denominator: int = 6,
    rho_t: Fraction = Fraction(-1, 1),
    s_te: Fraction = Fraction(-2, 1),
) -> Fraction:
    q_t = q_from_rho(rho_t, denominator)
    return s_te * q_t / c_te


def bridge_result(nc: int, denominator: int = 6, sign: int = -1) -> tuple[Fraction, Fraction, Fraction]:
    c_te = sign * f_adj(nc)
    q_e = q_e_from_center_bridge(c_te, denominator=denominator)
    rho_e = rho_from_q(q_e, denominator)
    return c_te, q_e, rho_e


def dot(row: tuple[Fraction, Fraction], w: tuple[Fraction, Fraction]) -> Fraction:
    return row[0] * w[0] + row[1] * w[1]


def main() -> int:
    note = NOTE.read_text(encoding="utf-8")

    w_shell = (Fraction(1), Fraction(0))
    w_center = (Fraction(1), Fraction(1, 6))
    ell_t = (Fraction(-2), Fraction(2))
    ell_e_target = (Fraction(1), Fraction(21, 4))

    gamma_t_shell = dot(ell_t, w_shell)
    gamma_t_center = dot(ell_t, w_center)
    gamma_e_shell = dot(ell_e_target, w_shell)
    gamma_e_center = dot(ell_e_target, w_center)

    check(
        "scaling channel endpoints are exact",
        w_shell == (1, 0) and w_center == (1, Fraction(1, 6)),
        f"w_shell={w_shell}, w_center={w_center}",
    )
    check(
        "supplied T row gives rho_T=-1 exactly",
        ell_t[1] / ell_t[0] == Fraction(-1),
        f"rho_T={ell_t[1] / ell_t[0]}",
    )
    check(
        "supplied T row gives q_T=5/6 exactly",
        gamma_t_center / gamma_t_shell == Fraction(5, 6),
        f"q_T={gamma_t_center / gamma_t_shell}",
    )
    check(
        "target E row gives rho_E=21/4 exactly when supplied",
        ell_e_target[1] / ell_e_target[0] == Fraction(21, 4),
        f"rho_E={ell_e_target[1] / ell_e_target[0]}",
    )
    check(
        "target E row gives q_E=15/8 exactly when supplied",
        gamma_e_center / gamma_e_shell == Fraction(15, 8),
        f"q_E={gamma_e_center / gamma_e_shell}",
    )
    check(
        "target rows give c_TE=-8/9 exactly",
        gamma_t_center / gamma_e_center == Fraction(-8, 9),
        f"c_TE={gamma_t_center / gamma_e_center}",
    )

    rho_zero = Fraction(0)
    e_shell_zero = dot((Fraction(1), rho_zero), w_shell)
    e_center_zero = dot((Fraction(1), rho_zero), w_center)
    e_shell_target = dot(ell_e_target, w_shell)
    e_center_target = dot(ell_e_target, w_center)
    check(
        "distinct E rows agree at shell but differ at center",
        e_shell_zero == e_shell_target == 1 and e_center_zero == 1 and e_center_target == Fraction(15, 8),
        f"zero=({e_shell_zero},{e_center_zero}), target=({e_shell_target},{e_center_target})",
    )
    check(
        "time factor is conditional because P_R c carries the rho_E dependence",
        e_center_target - e_center_zero == Fraction(7, 8),
        f"center prefactor delta={e_center_target - e_center_zero}",
    )

    c3, q3, rho3 = bridge_result(3)
    check("F_adj at N_c=3 is 8/9", f_adj(3) == Fraction(8, 9), f"F_adj={f_adj(3)}")
    check(
        "signed N_c=3 bridge returns q_E=15/8",
        c3 == Fraction(-8, 9) and q3 == Fraction(15, 8),
        f"c_TE={c3}, q_E={q3}",
    )
    check(
        "signed N_c=3 bridge returns rho_E=21/4",
        rho3 == Fraction(21, 4),
        f"rho_E={rho3}",
    )

    c2, q2, rho2 = bridge_result(2)
    check(
        "wrong color count N_c=2 breaks the target",
        c2 == Fraction(-3, 4) and q2 == Fraction(20, 9) and rho2 == Fraction(22, 3) and rho2 != Fraction(21, 4),
        f"c_TE={c2}, q_E={q2}, rho_E={rho2}",
    )
    c5, q5, rho5 = bridge_result(3, denominator=5)
    check(
        "wrong support denominator 5 breaks the target",
        q_from_rho(Fraction(-1), 5) == Fraction(4, 5) and q5 == Fraction(9, 5) and rho5 == Fraction(4),
        f"c_TE={c5}, q_E={q5}, rho_E={rho5}",
    )
    c12, q12, rho12 = bridge_result(3, denominator=12)
    check(
        "wrong support denominator 12 breaks the target",
        q_from_rho(Fraction(-1), 12) == Fraction(11, 12) and q12 == Fraction(33, 16) and rho12 == Fraction(51, 4),
        f"c_TE={c12}, q_E={q12}, rho_E={rho12}",
    )
    c_wrong_sign, q_wrong_sign, rho_wrong_sign = bridge_result(3, sign=1)
    check(
        "wrong bridge sign breaks the target",
        c_wrong_sign == Fraction(8, 9) and q_wrong_sign == Fraction(-15, 8) and rho_wrong_sign == Fraction(-69, 4),
        f"c_TE={c_wrong_sign}, q_E={q_wrong_sign}, rho_E={rho_wrong_sign}",
    )
    q_no_lift = q_from_rho(Fraction(0))
    c_no_lift = Fraction(-2) * Fraction(5, 6) / q_no_lift
    check(
        "no E-center lift breaks the target",
        q_no_lift == 1 and c_no_lift == Fraction(-5, 3),
        f"q_E={q_no_lift}, c_TE={c_no_lift}",
    )
    q_same_slope = q_from_rho(Fraction(-1))
    c_same_slope = Fraction(-2) * Fraction(5, 6) / q_same_slope
    check(
        "same-slope reuse breaks the target",
        q_same_slope == Fraction(5, 6) and c_same_slope == Fraction(-2),
        f"q_E={q_same_slope}, c_TE={c_same_slope}",
    )

    kappa_zero = f_adj(3) + Fraction(0) * (1 - f_adj(3))
    kappa_one = f_adj(3) + Fraction(1) * (1 - f_adj(3))
    kappa_quarter = f_adj(3) + Fraction(1, 4) * (1 - f_adj(3))
    check(
        "kappa_EW family distinguishes count from physical weight",
        kappa_zero == Fraction(8, 9) and kappa_one == 1 and kappa_quarter == Fraction(11, 12),
        f"R(0)={kappa_zero}, R(1/4)={kappa_quarter}, R(1)={kappa_one}",
    )
    check(
        "rho_E target is equivalent to q_E target",
        rho_from_q(Fraction(15, 8)) == Fraction(21, 4) and q_from_rho(Fraction(21, 4)) == Fraction(15, 8),
        "rho_E <-> q_E",
    )
    check(
        "color bridge arithmetic is conditional not a bridge derivation",
        "does not supply the typed signed" in note and "does not use `kappa_EW=0` as a proof" in note,
        "bridge and weighting firewall present",
    )

    required_links = [
        "[QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md]",
        "[QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md]",
        "[TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md]",
        "[S3_TIME_BILINEAR_TENSOR_PRIMITIVE_RANK1_FACTORIZATION_NOTE_2026-05-17.md]",
        "[RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md]",
        "[MINIMAL_AXIOMS_2026-06-05.md]",
    ]
    check(
        "one-hop authority links are present",
        all(link in note for link in required_links),
        "authority table linked",
    )
    check(
        "non-authority refs are plain text",
        ".claude/tmp/refs/W69_NOTE.md" in note
        and "](.claude/tmp/refs/W69_NOTE.md)" not in note
        and "scripts/runner_cache.py" in note
        and "](../scripts/runner_cache.py)" not in note,
        "context pointers not markdown-linked",
    )
    check(
        "status authority block is present",
        "Status authority:** independent audit lane only" in note
        and "does not set,\npredict, or estimate any audit verdict" in note,
        "audit status delegated",
    )
    forbidden_overreach = [
        "only " + "route",
        "last " + "route",
        "exhaus" + "ted",
        "closes " + "the program",
    ]
    lower_note = note.lower()
    check(
        "overreach language is absent",
        all(phrase not in lower_note for phrase in forbidden_overreach),
        "forbidden phrases absent",
    )
    check(
        "comparator firewall is explicit",
        "are not proof inputs here" in note
        and "bounded comparator context" in note
        and "nearest-rational selection from live\nendpoint values" in note,
        "comparators separated",
    )
    check(
        "construction differentiates itself from W69",
        "W69 named the missing theorem" in note and "This note performs the construction pass" in note,
        "W69 distinction present",
    )
    check(
        "naturality boundary distinction is present",
        "The 2026-04-28 naturality boundary tested" in note
        and "rank-1 carrier factorization -> row covector evaluation" in note,
        "naturality distinction present",
    )
    for label in [f"**N{i}" for i in range(1, 9)]:
        check(f"no-go discipline {label} present", label in note, label)
    check(
        "No-Go gate result is scoped and not an audit verdict",
        "Gate result: PASS for the scoped localized construction result. This is not\nan audit verdict." in note,
        "N1-N8 scoped",
    )
    check(
        "boundary excludes direct derivation claims",
        "This note does not establish:" in note
        and "a direct derivation of `rho_E = 21/4`" in note
        and "a physical `kappa_EW` weighting selector" in note,
        "boundary list present",
    )

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
