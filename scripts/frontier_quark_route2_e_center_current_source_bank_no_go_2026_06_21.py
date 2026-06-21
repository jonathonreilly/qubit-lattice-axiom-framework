#!/usr/bin/env python3
"""Current-source-bank no-go for the Route-2 E-center lift.

The runner uses exact rational arithmetic and text checks to verify that the
named current source-bank invariants do not distinguish rho_E=0 from
rho_E=21/4. It does not use observed masses, fitted targets, or live endpoint
nearest-rational selection.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
NOTE = DOCS / "QUARK_ROUTE2_E_CENTER_CURRENT_SOURCE_BANK_NO_GO_NOTE_2026-06-21.md"
CENTER_EXCESS = DOCS / "TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md"
BILINEAR = DOCS / "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md"
READOUT = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
ELL_E = DOCS / "QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md"
OH_LEVERAGE = DOCS / "OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md"
RCONN_TYPED = DOCS / "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md"
MEASURED = DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class CurrentSourceBank:
    delta_step: Fraction
    q_t: Fraction
    s_te: Fraction
    f_adj: Fraction
    kappa: Fraction
    kappa_squared: Fraction
    hom_e_t1_zero: bool
    positive_e_family: bool
    sign_correct: bool


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {name}{suffix}")


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def q_e(rho_e: Fraction) -> Fraction:
    return Fraction(1, 1) + rho_e / Fraction(6, 1)


def c_te(rho_e: Fraction) -> Fraction:
    return Fraction(-2, 1) * Fraction(5, 6) / q_e(rho_e)


def source_bank_for(rho_e: Fraction) -> CurrentSourceBank:
    return CurrentSourceBank(
        delta_step=Fraction(1, 6),
        q_t=Fraction(5, 6),
        s_te=Fraction(-2, 1),
        f_adj=Fraction(8, 9),
        kappa=Fraction(3, 2),
        kappa_squared=Fraction(9, 4),
        hom_e_t1_zero=True,
        positive_e_family=rho_e > Fraction(-6, 1),
        sign_correct=c_te(rho_e) < 0,
    )


def solve_from_c_te(target_c_te: Fraction) -> Fraction:
    target_q_e = Fraction(-2, 1) * Fraction(5, 6) / target_c_te
    return Fraction(6, 1) * (target_q_e - 1)


def solve_from_covariance(lambda_et: Fraction) -> Fraction:
    target_q_e = lambda_et * Fraction(5, 6)
    return Fraction(6, 1) * (target_q_e - 1)


def contains_all(haystack: str, needles: tuple[str, ...]) -> bool:
    return all(needle in haystack for needle in needles)


def main() -> int:
    print("Route-2 E-center current source-bank no-go verifier")
    print("=" * 72)

    note = text(NOTE)
    center = text(CENTER_EXCESS)
    bilinear = text(BILINEAR)
    readout = text(READOUT)
    ell_e = text(ELL_E)
    oh = text(OH_LEVERAGE)
    rconn = text(RCONN_TYPED)
    measured = text(MEASURED)

    check(
        "note scopes the result as a bounded current-bank obstruction",
        "bounded current-bank obstruction" in note
        and "does not derive `rho_E = 21/4`" in note
        and "does not prove that no future" in note,
    )
    check(
        "center-excess authority supplies the 1/6 support step",
        "phi_support(center) - phi_support(arm_mean) = 1/6" in center
        and "delta_A1(r) = 1 / (6 (1 + sqrt(6) r))" in center,
    )
    check(
        "bilinear primitive authority is definition-only under admitted inputs",
        "K_R(q) := [[u_E(q), u_T(q)], [delta_A1(q) u_E(q), delta_A1(q) u_T(q)]]"
        in bilinear
        and "does **not** prove that this symbol is a physical tensor primitive" in bilinear,
    )
    check(
        "readout authority supplies the rho_E endpoint algebra",
        "q_E   := gamma_E(center) / gamma_E(shell) = 1 + (beta_E / alpha_E) / 6"
        in readout
        and "rho_E" in readout,
    )
    check(
        "ell_E note keeps the magnitude open after positivity/sign separation",
        "rho_E > -6" in ell_e
        and "c_TE < 0" in ell_e
        and "The magnitude remains open" in ell_e,
    )
    check(
        "O_h shell leverage supplies kappa but not the covariance bridge",
        "3/2" in oh
        and "9/4" in oh
        and "does **not**, by itself, derive any Route-2 readout entry" in oh,
    )
    check(
        "Rconn typed bridge note keeps F_adj -> c_TE as the missing edge",
        "F_adj = 8/9" in rconn
        and "su3_R_conn_8_9 -> route2_center_TE_minus_8_9" in rconn
        and "does not derive the bridge" in rconn,
    )
    check(
        "measured calibration is comparator evidence, not a derivation",
        "not a derivation" in measured.lower()
        and "exact infinite-volume identification" in measured,
    )

    rho_zero = Fraction(0, 1)
    rho_target = Fraction(21, 4)
    bank_zero = source_bank_for(rho_zero)
    bank_target = source_bank_for(rho_target)

    check(
        "rho_E=0 and rho_E=21/4 have identical current source-bank invariants",
        bank_zero == bank_target,
        f"bank={bank_zero}",
    )
    check(
        "the same two rows have different q_E values",
        q_e(rho_zero) == Fraction(1, 1)
        and q_e(rho_target) == Fraction(15, 8)
        and q_e(rho_zero) != q_e(rho_target),
        f"q_E(0)={q_e(rho_zero)}, q_E(target)={q_e(rho_target)}",
    )
    check(
        "the same two rows have different center T/E ratios",
        c_te(rho_zero) == Fraction(-5, 3)
        and c_te(rho_target) == Fraction(-8, 9)
        and c_te(rho_zero) != c_te(rho_target),
        f"c_TE(0)={c_te(rho_zero)}, c_TE(target)={c_te(rho_target)}",
    )
    check(
        "both rows satisfy the positive sign-correct family",
        bank_zero.positive_e_family
        and bank_target.positive_e_family
        and bank_zero.sign_correct
        and bank_target.sign_correct,
    )
    check(
        "sign-only information does not pin the magnitude",
        c_te(rho_zero) < 0 and c_te(rho_target) < 0 and c_te(rho_zero) != c_te(rho_target),
    )
    check(
        "F_adj alone is identical across the counter-witness pair",
        bank_zero.f_adj == bank_target.f_adj == Fraction(8, 9),
    )
    check(
        "kappa-squared alone is identical across the counter-witness pair",
        bank_zero.kappa_squared == bank_target.kappa_squared == Fraction(9, 4),
    )
    check(
        "adding c_TE=-F_adj would conditionally pin rho_E=21/4",
        solve_from_c_te(-bank_zero.f_adj) == rho_target,
        f"rho={solve_from_c_te(-bank_zero.f_adj)}",
    )
    check(
        "adding q_E/q_T=kappa^2 would conditionally pin rho_E=21/4",
        solve_from_covariance(bank_zero.kappa_squared) == rho_target,
        f"rho={solve_from_covariance(bank_zero.kappa_squared)}",
    )
    check(
        "adding q_E=15/8 would conditionally pin rho_E=21/4",
        Fraction(6, 1) * (Fraction(15, 8) - 1) == rho_target,
    )
    check(
        "wrong color count falsifies an untyped F_adj recipe",
        solve_from_c_te(-Fraction(3, 4)) == Fraction(22, 3),
        f"N_c=2 recipe gives rho={solve_from_c_te(-Fraction(3, 4))}",
    )
    check(
        "a third positive sample shares the bank but gives a third E-center value",
        source_bank_for(Fraction(1, 1)) == bank_zero
        and q_e(Fraction(1, 1)) == Fraction(7, 6)
        and c_te(Fraction(1, 1)) == Fraction(-10, 7),
    )
    check(
        "note records the exact counter-witness pair",
        contains_all(
            note,
            (
                "rho_E = 0",
                "rho_E = 21/4",
                "identical current source-bank invariants",
            ),
        ),
    )

    print("=" * 72)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
