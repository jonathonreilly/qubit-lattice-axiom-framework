#!/usr/bin/env python3
"""Exact Route-2 color/covariance bridge equivalence support.

This verifier checks the algebraic relation between the two live positive
bridge targets:

    lambda = q_E/q_T = kappa^2
    c_TE = -F_adj

under the granted Route-2 T-side orientation. It does not derive either typed
bridge and does not use observed/fitted endpoint data.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"

NOTE = DOCS / "QUARK_ROUTE2_COLOR_COVARIANCE_BRIDGE_EQUIVALENCE_SUPPORT_NOTE_2026-06-21.md"
READOUT = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
OH_LEVERAGE = DOCS / "OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md"
FIERZ = DOCS / "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md"
QE_KAPPA = DOCS / "QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md"
RCONN_TYPED = DOCS / "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md"

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
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {name}{suffix}")


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def f_adj(n_c: int) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def rho_from_lambda(lam: Fraction, q_t: Fraction = Fraction(5, 6)) -> Fraction:
    q_e = lam * q_t
    return Fraction(6, 1) * (q_e - 1)


def lambda_from_c_te(c_te: Fraction, s_te: Fraction = Fraction(-2, 1)) -> Fraction:
    return s_te / c_te


def c_te_from_lambda(lam: Fraction, s_te: Fraction = Fraction(-2, 1)) -> Fraction:
    return s_te / lam


def contains_all(haystack: str, needles: tuple[str, ...]) -> bool:
    return all(needle in haystack for needle in needles)


def flat(haystack: str) -> str:
    return " ".join(haystack.split())


def main() -> int:
    print("Route-2 color/covariance bridge equivalence verifier")
    print("=" * 72)

    note = text(NOTE)
    readout = text(READOUT)
    oh = text(OH_LEVERAGE)
    fierz = text(FIERZ)
    qe_kappa = text(QE_KAPPA)
    rconn = text(RCONN_TYPED)

    check(
        "note is scoped as exact support, not endpoint-triple closure",
        "does not derive `rho_E = 21/4`" in note
        and "does not derive the\ntyped color bridge" in note
        and "does not derive the typed covariance bridge" in note,
    )
    check(
        "readout authority supplies endpoint algebra and T-side target chain",
        "c_TE" in readout
        and "gamma_T(center) / gamma_E(center)" in readout
        and "q_T" in readout
        and "beta_T / alpha_T = -1" in readout,
    )
    check(
        "O_h leverage authority supplies kappa=3/2 without readout closure",
        "3/2" in oh
        and "9/4" in oh
        and "does **not**, by itself, derive any Route-2 readout entry" in oh,
    )
    check(
        "Fierz authority supplies exact F_adj=8/9 at N_c=3",
        "(N_c^2 − 1) / N_c^2" in fierz
        and "8/9" in fierz
        and "matching rule" in fierz
        and "**not derived in this note**" in fierz,
    )
    check(
        "covariance no-go names lambda=kappa^2 as missing bridge",
        "bridge `λ = q_E/q_T = κ²` is not a consequence" in qe_kappa
        and "covariance rule `λ = κ²`" in qe_kappa,
    )
    check(
        "Rconn typed note names F_adj -> c_TE as missing bridge",
        "F_adj = 8/9" in rconn
        and "c_TE = gamma_T(center)/gamma_E(center) = -F_adj" in rconn
        and "typed edge" in rconn,
    )

    rho_t = Fraction(-1, 1)
    s_te = Fraction(-2, 1)
    q_t = Fraction(1, 1) + rho_t / 6
    kappa = Fraction(3, 2)
    kappa_sq = kappa * kappa
    f3 = f_adj(3)
    target_lambda = Fraction(9, 4)
    target_c_te = Fraction(-8, 9)
    target_q_e = Fraction(15, 8)
    target_rho_e = Fraction(21, 4)

    check("granted rho_T=-1 gives q_T=5/6", q_t == Fraction(5, 6), str(q_t))
    check("same-domain kappa=3/2 gives kappa^2=9/4", kappa_sq == target_lambda, str(kappa_sq))
    check("N_c=3 gives F_adj=8/9", f3 == Fraction(8, 9), str(f3))
    check(
        "current constants obey F_adj = -s_TE/kappa^2",
        f3 == -s_te / kappa_sq,
        f"F_adj={f3}, -s_TE/kappa^2={-s_te / kappa_sq}",
    )
    check(
        "covariance bridge lambda=kappa^2 gives color target c_TE=-F_adj",
        c_te_from_lambda(kappa_sq, s_te) == -f3 == target_c_te,
        f"c_TE={c_te_from_lambda(kappa_sq, s_te)}",
    )
    check(
        "color bridge c_TE=-F_adj gives covariance target lambda=kappa^2",
        lambda_from_c_te(-f3, s_te) == kappa_sq == target_lambda,
        f"lambda={lambda_from_c_te(-f3, s_te)}",
    )
    check(
        "either bridge gives q_E=15/8",
        target_lambda * q_t == target_q_e,
        f"q_E={target_lambda * q_t}",
    )
    check(
        "either bridge gives rho_E=21/4",
        rho_from_lambda(target_lambda, q_t) == target_rho_e,
        f"rho_E={rho_from_lambda(target_lambda, q_t)}",
    )
    check(
        "endpoint color form and covariance form are mutually inverse under s_TE",
        c_te_from_lambda(lambda_from_c_te(target_c_te, s_te), s_te) == target_c_te,
    )

    f2 = f_adj(2)
    lambda_from_wrong_color = lambda_from_c_te(-f2, s_te)
    check(
        "wrong N_c=2 breaks color/covariance equivalence",
        f2 == Fraction(3, 4)
        and lambda_from_wrong_color == Fraction(8, 3)
        and lambda_from_wrong_color != kappa_sq,
        f"F_adj(2)={f2}, lambda={lambda_from_wrong_color}",
    )
    check(
        "wrong N_c=2 implies rho_E=22/3 instead of 21/4",
        rho_from_lambda(lambda_from_wrong_color, q_t) == Fraction(22, 3),
        f"rho_E={rho_from_lambda(lambda_from_wrong_color, q_t)}",
    )
    check(
        "wrong kappa=1 breaks equivalence with F_adj",
        c_te_from_lambda(Fraction(1, 1), s_te) == Fraction(-2, 1)
        and c_te_from_lambda(Fraction(1, 1), s_te) != -f3,
    )
    wrong_s_te = Fraction(-1, 1)
    check(
        "wrong shell ratio s_TE=-1 breaks F_adj = -s_TE/kappa^2",
        -wrong_s_te / kappa_sq == Fraction(4, 9)
        and -wrong_s_te / kappa_sq != f3,
        f"-s/kappa^2={-wrong_s_te / kappa_sq}",
    )
    check(
        "without shell orientation the relation stays symbolic",
        contains_all(note, ("no T-side shell orientation", "remains symbolic")),
    )
    check(
        "note records bridge compression instead of independent route count",
        "They are not two independent missing primitives" in flat(note)
        and "Future work should therefore not count these as independent positive routes" in flat(note),
    )
    check(
        "note records all major falsifiers",
        contains_all(note, ("`N_c=2`", "`kappa=1`", "`s_TE=-1`", "no T-side shell orientation")),
    )
    check(
        "note does not claim typed bridge derivation",
        "This note does not derive `lambda=kappa^2`" in note
        and "This note does not derive `c_TE=-F_adj`" in note,
    )

    print("=" * 72)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
