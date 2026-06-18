#!/usr/bin/env python3
"""W69 Route-2 E-center lift derivation attempt checker.

The runner uses exact rational arithmetic for the Route-2 endpoint algebra and
text checks for the source-boundary claims recorded in the companion note.
It does not use live endpoint values as proof inputs.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md"
READOUT = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
TIME = DOCS / "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md"
NATURALITY = DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
S3_GATE = DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
S3_RIGIDITY = DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md"
CENTER_EXCESS = DOCS / "TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md"
MEASURED = DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md"
QUOTIENT = DOCS / "QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md"
SOURCE_BRIDGE = DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md"
RECORD_POSITIVITY = DOCS / "ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md"
PRIMITIVES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def q_from_rho(rho: Fraction, center_denominator: int = 6) -> Fraction:
    return Fraction(1, 1) + rho / center_denominator


def q_t_from_rho_t(rho_t: Fraction = Fraction(-1, 1), center_denominator: int = 6) -> Fraction:
    return q_from_rho(rho_t, center_denominator)


def c_te_from_rho(
    rho_e: Fraction,
    center_denominator: int = 6,
    shell_ratio_te: Fraction = Fraction(-2, 1),
    rho_t: Fraction = Fraction(-1, 1),
) -> Fraction:
    return shell_ratio_te * q_t_from_rho_t(rho_t, center_denominator) / q_from_rho(
        rho_e, center_denominator
    )


def solve_from_center_ratio(
    c_te: Fraction,
    center_denominator: int = 6,
    shell_ratio_te: Fraction = Fraction(-2, 1),
    rho_t: Fraction = Fraction(-1, 1),
) -> tuple[Fraction, Fraction, Fraction]:
    q_t = q_t_from_rho_t(rho_t, center_denominator)
    q_e = shell_ratio_te * q_t / c_te
    rho_e = center_denominator * (q_e - 1)
    return q_t, q_e, rho_e


def f_adj(n_c: int) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def solve_from_adjoint_bridge(n_c: int, center_denominator: int = 6) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    f = f_adj(n_c)
    q_t, q_e, rho_e = solve_from_center_ratio(-f, center_denominator)
    return f, q_t, q_e, rho_e


def contains_all(haystack: str, needles: tuple[str, ...]) -> bool:
    return all(needle in haystack for needle in needles)


def flat(s: str) -> str:
    return " ".join(s.split())


def main() -> int:
    print("W69 ROUTE-2 E-CENTER LIFT DERIVATION ATTEMPT CHECK")

    print("Authority/file presence")
    for path in (
        NOTE,
        READOUT,
        TIME,
        NATURALITY,
        S3_GATE,
        S3_RIGIDITY,
        CENTER_EXCESS,
        MEASURED,
        QUOTIENT,
        SOURCE_BRIDGE,
        RECORD_POSITIVITY,
        PRIMITIVES,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = text(NOTE)
    readout = text(READOUT)
    time_note = text(TIME)
    naturality = text(NATURALITY)
    s3_gate = text(S3_GATE)
    s3_rigidity = text(S3_RIGIDITY)
    center_excess = text(CENTER_EXCESS)
    measured = text(MEASURED)
    quotient = text(QUOTIENT)
    source_bridge = text(SOURCE_BRIDGE)
    record_pos = text(RECORD_POSITIVITY)
    primitives = text(PRIMITIVES)

    print("Source-boundary text checks")
    check(
        "new note preserves independent audit status authority block",
        "Status authority:** independent audit lane only. This source note does not set,"
        in note
        and "predict, or estimate any audit verdict" in note,
    )
    forbidden_status_tokens = (
        "audited_" + "clean",
        "audited_" + "conditional",
        "retained_" + "no_go",
        "retained_" + "bounded",
        "proposed_" + "no_go",
    )
    check(
        "new note does not assign audit/effective status labels",
        not any(token in note for token in forbidden_status_tokens),
    )
    forbidden_overreach = (
        "only " + "route",
        "last " + "route",
        "exhaus" + "ted",
        "closes the " + "program",
    )
    check(
        "new note avoids barred overreach phrases",
        not any(token in note.lower() for token in forbidden_overreach),
    )
    check(
        "new note lists one-hop authorities as markdown links",
        contains_all(
            note,
            (
                "[QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md]",
                "[QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md]",
                "[S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md]",
                "[TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md]",
                "[QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md]",
            ),
        ),
    )
    check(
        "new note contains no untracked checkpoint authority pointers",
        ".claude/tmp" not in note,
    )

    print("Definition-chain checks")
    check(
        "readout note defines gamma_E and gamma_T coefficient rows",
        contains_all(
            readout,
            (
                "gamma_E = alpha_E u_E + beta_E delta_A1 u_E",
                "gamma_T = alpha_T u_T + beta_T delta_A1 u_T",
                "P_R = [[alpha_E, 0, beta_E, 0],",
            ),
        ),
    )
    check(
        "readout note defines endpoint q_E algebra",
        "q_E   := gamma_E(center) / gamma_E(shell) = 1 + (beta_E / alpha_E) / 6"
        in readout,
    )
    check(
        "center-excess note supplies delta_A1 endpoint denominator",
        contains_all(
            center_excess,
            (
                "phi_support(center) - phi_support(arm_mean) = 1/6",
                "delta_A1(r) = 1 / (6 (1 + sqrt(6) r))",
            ),
        ),
    )
    check(
        "s3 gate names endpoint triple as theorem target",
        "(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E) = (-1, -2, 21/4)"
        in s3_gate,
    )
    check(
        "time-coupling note is conditional on supplied P_R",
        contains_all(
            flat(time_note),
            (
                "Given any admissible readout map `P_R`",
                "What it lacks is a theorem that selects one unique `P_R`.",
            ),
        ),
    )
    check(
        "factor-rigidity note keeps rho_E arbitrary",
        contains_all(
            s3_rigidity,
            (
                "valid for every admissible readout in the 1-parameter family",
                "Does **not** derive the readout-triple",
            ),
        ),
    )

    print("Exact endpoint arithmetic")
    rho_target = Fraction(21, 4)
    q_e_target = q_from_rho(rho_target)
    check("rho_E=21/4 gives q_E=15/8 exactly", q_e_target == Fraction(15, 8), str(q_e_target))
    check("rho_E/6 is 7/8 exactly", rho_target / 6 == Fraction(7, 8), str(rho_target / 6))
    check(
        "granted rho_T=-1 gives q_T=5/6 exactly",
        q_t_from_rho_t() == Fraction(5, 6),
        str(q_t_from_rho_t()),
    )
    check(
        "rho_E=21/4 gives c_TE=-8/9 under granted T-side values",
        c_te_from_rho(rho_target) == Fraction(-8, 9),
        str(c_te_from_rho(rho_target)),
    )
    q_t, q_e, rho_e = solve_from_center_ratio(Fraction(-8, 9))
    check("c_TE=-8/9 solves q_E=15/8", q_e == Fraction(15, 8), str(q_e))
    check("c_TE=-8/9 solves rho_E=21/4", rho_e == rho_target, str(rho_e))
    f, q_t2, q_e2, rho_e2 = solve_from_adjoint_bridge(3)
    check("N_c=3 adjoint bridge value is 8/9", f == Fraction(8, 9), str(f))
    check("adding the typed adjoint bridge computes rho_E=21/4", rho_e2 == rho_target, str(rho_e2))

    print("Wrong-structure falsifiers")
    f2, qt2, qe2, rho2 = solve_from_adjoint_bridge(2)
    check("wrong N_c=2 does not compute 21/4", rho2 == Fraction(22, 3), f"F={f2}, q_E={qe2}, rho_E={rho2}")
    f3, qt_m5, qe_m5, rho_m5 = solve_from_adjoint_bridge(3, center_denominator=5)
    check(
        "wrong center-excess denominator 5 does not compute 21/4",
        rho_m5 == Fraction(4, 1),
        f"F={f3}, q_T={qt_m5}, q_E={qe_m5}, rho_E={rho_m5}",
    )
    f4, qt_m12, qe_m12, rho_m12 = solve_from_adjoint_bridge(3, center_denominator=12)
    check(
        "wrong dimension-style denominator 12 does not compute 21/4",
        rho_m12 == Fraction(51, 4),
        f"F={f4}, q_T={qt_m12}, q_E={qe_m12}, rho_E={rho_m12}",
    )
    check(
        "no-lift rho_E=0 is an exact counter-witness to forced c_TE=-8/9",
        c_te_from_rho(Fraction(0, 1)) == Fraction(-5, 3),
        str(c_te_from_rho(Fraction(0, 1))),
    )

    print("Obstruction and comparator firewall checks")
    escape_quote = (
        "remains a free parameter unless an additional E-center endpoint ratio,\n"
        "source-domain, or readout-map primitive is supplied"
    )
    check("naturality note contains the escape clause", escape_quote in naturality)
    check(
        "naturality note names q_E=15/8 discharge form",
        contains_all(
            naturality,
            (
                "derive the E-center lift",
                "gamma_E(center)/gamma_E(shell) = 15/8.",
            ),
        ),
    )
    check(
        "measured calibration states it is not a derivation",
        contains_all(
            measured.lower(),
            (
                "not a derivation",
                "exact infinite-volume identification",
            ),
        ),
    )
    check(
        "endpoint quotient law classifies q_E=15/8 as nearest-rational match",
        contains_all(
            quotient,
            (
                "nearest-rational match",
                "rather than a derivation from",
                "tensor machinery",
            ),
        ),
    )
    check(
        "source bridge note keeps c_TE=-R_conn as missing typed bridge",
        contains_all(
            source_bridge,
            (
                "R_conn = (N_c^2 - 1) / N_c^2",
                "?=> gamma_T(center) / gamma_E(center) = -R_conn",
            ),
        ),
    )
    check(
        "record/positivity note leaves rho_E direction free",
        contains_all(
            flat(record_pos),
            (
                "`rho_E` is the readout **direction**",
                "shell-vs-center **distinguishing** input",
            ),
        ),
    )
    check(
        "primitive registry does not supply readout bridge content",
        contains_all(
            primitives,
            (
                "scale_reference_primitive",
                "kinetic_isotropy_primitive",
                "realized_state_primitive",
                "readout bridge",
            ),
        ),
    )
    check(
        "new note names the exact missing computation",
        "exact computation would have to derive `gamma_E(center)/gamma_E(shell) = 15/8`"
        in note,
    )
    check(
        "new note separates comparator evidence from proof inputs",
        "Comparator Evidence Not Used As Proof Input" in note
        and "not used to derive `rho_E = 21/4`" in flat(note),
    )
    check(
        "new note records route inventory",
        "| Route | Attempt | Blocked at |" in note
        and "Exact E-channel slice row" in note
        and "Measured calibration" in note,
    )
    check(
        "new note records no-go discipline sections N1-N8",
        all(f"**N{i}" in note for i in range(1, 9)),
    )

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
