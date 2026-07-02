#!/usr/bin/env python3
"""Discriminating checks for Higgs Y_H from Yukawa closure equations."""

from fractions import Fraction
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "HIGGS_Y_FROM_LHCM_AND_YUKAWA_STRUCTURE_NOTE_2026-05-02.md"
TOL = 1.0e-12

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    print(f"[{tag}] {label} ({detail})")


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def frac_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def residual(term: dict, y_h: Fraction) -> Fraction:
    return term["h_coeff"] * y_h + term["constant"]


note_text = NOTE_PATH.read_text(encoding="utf-8")

Y_QL = Fraction(1, 3)
Y_LL = Fraction(-1)
Y_uR = Fraction(4, 3)
Y_dR = Fraction(-2, 3)
Y_eR = Fraction(-2)
Y_nuR = Fraction(0)

# Each displayed Yukawa closure is encoded as h_coeff * Y_H + constant = 0.
# Htilde contributes -Y_H; barred left-handed fields contribute -Y(left).
terms = [
    {
        "name": "up-quark Qbar_L Htilde u_R",
        "h_coeff": Fraction(-1),
        "constant": -Y_QL + Y_uR,
        "displayed": "Y(H)  =  Y(u_R) − Y(Q_L)",
    },
    {
        "name": "down-quark Qbar_L H d_R",
        "h_coeff": Fraction(1),
        "constant": -Y_QL + Y_dR,
        "displayed": "Y(H) = Y(Q_L) − Y(d_R)",
    },
    {
        "name": "charged-lepton Lbar_L H e_R",
        "h_coeff": Fraction(1),
        "constant": -Y_LL + Y_eR,
        "displayed": "Y(H)  =  Y(L_L) − Y(e_R)",
    },
    {
        "name": "neutral-lepton Lbar_L Htilde nu_R",
        "h_coeff": Fraction(-1),
        "constant": -Y_LL + Y_nuR,
        "displayed": "+Y(H) =  Y(ν_R) − Y(L_L)",
    },
]


section("Displayed note scope")
displayed_fragments = [
    "Higgs Y_H from LHCM-Derived Hypercharges and Yukawa Structure",
    "Y_H  =  +1",
    "Q̄_L · H̃ · u_R",
    "Q̄_L · H · d_R",
    "L̄_L · H · e_R",
    "L̄_L · H̃ · ν_R",
    "These appear inconsistent — but recall `Q̄_L` is the conjugate.",
]
for fragment in displayed_fragments:
    check(f"note displays {fragment!r}", fragment in note_text)
for term in terms:
    check(f"note displays closure target for {term['name']}", term["displayed"] in note_text)


section("Linear solve for Y_H from all displayed Yukawa closures")
A = np.array([[float(term["h_coeff"])] for term in terms], dtype=float)
b = np.array([float(-term["constant"]) for term in terms], dtype=float)
solution, residuals, rank, singular_values = np.linalg.lstsq(A, b, rcond=None)
solved_y_h = Fraction.from_float(float(solution[0])).limit_denominator(10**6)
numeric_residual = A @ solution - b
check(
    "combined closure system has rank one for the single unknown Y_H",
    rank == 1,
    detail=f"singular_values={singular_values}",
)
check(
    "Y_H = +1 comes out of the linear solve",
    abs(float(solution[0]) - 1.0) < TOL and solved_y_h == Fraction(1),
    detail=f"solution={solution[0]:.16g}, rationalized={solved_y_h}",
)
check(
    "all closure equations vanish at the solved value",
    np.linalg.norm(numeric_residual, ord=np.inf) < TOL,
    detail=f"max_residual={np.linalg.norm(numeric_residual, ord=np.inf):.3e}",
)


section("Per-term computed closure relations")
for term in terms:
    individual_y_h = -term["constant"] / term["h_coeff"]
    check(
        f"{term['name']} derives Y_H = +1",
        individual_y_h == Fraction(1),
        detail=(
            f"{term['h_coeff']}*Y_H + ({frac_text(term['constant'])}) = 0 -> "
            f"Y_H={frac_text(individual_y_h)}"
        ),
    )
    check(
        f"{term['name']} is hypercharge-neutral at solved Y_H",
        residual(term, Fraction(1)) == 0,
        detail=f"residual={frac_text(residual(term, Fraction(1)))}",
    )

naive_down = Y_dR - Y_QL
down_term = terms[1]
check(
    "displayed naive down-quark subtraction gives the advertised inconsistent -1",
    naive_down == Fraction(-1),
    detail=f"Y(d_R)-Y(Q_L)={frac_text(naive_down)}",
)
check(
    "the conjugate-field down closure rejects the naive Y_H=-1 value",
    residual(down_term, naive_down) != 0,
    detail=f"closure residual at Y_H=-1 is {frac_text(residual(down_term, naive_down))}",
)


section("Refutation: wrong Y_H values violate displayed closures")
wrong_values = [Fraction(0), Fraction(-1), Fraction(2, 3), Fraction(5, 3)]
check(
    "rank-one solve gives a unique Y_H value",
    all(term["h_coeff"] != 0 for term in terms) and solved_y_h == Fraction(1),
    detail="for this one-unknown system, any Y_H != 1 leaves nonzero residual",
)
for wrong_y_h in wrong_values:
    violations = [residual(term, wrong_y_h) for term in terms]
    check(
        f"wrong Y_H={frac_text(wrong_y_h)} violates at least one closure equation",
        any(value != 0 for value in violations),
        detail=f"residuals={[frac_text(value) for value in violations]}",
    )


section("Electric-charge consequence at solved Y_H")
T_3_Hplus = Fraction(1, 2)
T_3_H0 = Fraction(-1, 2)
Q_Hplus = T_3_Hplus + solved_y_h / 2
Q_H0 = T_3_H0 + solved_y_h / 2
check(
    "Q(H+) = T_3(H+) + Y_H/2 = +1 (charged Higgs)",
    Q_Hplus == Fraction(1),
    detail=f"1/2 + {frac_text(solved_y_h)}/2 = {frac_text(Q_Hplus)}",
)
check(
    "Q(H0) = T_3(H0) + Y_H/2 = 0 (neutral Higgs)",
    Q_H0 == Fraction(0),
    detail=f"-1/2 + {frac_text(solved_y_h)}/2 = {frac_text(Q_H0)}",
)


section("Displayed non-closure boundaries")
non_closures = [
    "What this does NOT close",
    "The SM Yukawa coupling form itself (admitted as standard SM convention)",
    "The retention of LHCM (still depends on SM-definition convention",
    "The retention of `STANDARD_MODEL_HYPERCHARGE_UNIQUENESS` (still",
    "The Higgs VEV `v` value (admitted external)",
]
for item in non_closures:
    check(f"non-closure boundary present: {item}", item in note_text)


section("Source-boundary firewall")
pinned_note_fragments = [
    (
        "status line",
        "**Status:** exact algebraic identity / support theorem on retained\n"
        "graph-first surface + LHCM closure trio (cycles 1-3) + Yukawa-structure\n"
        "admitted SM convention. NOT proposed_retained — see\n"
        "CLAIM_STATUS_CERTIFICATE.md.",
    ),
    (
        "authority role",
        "**Authority role:** exact-support theorem extending the LHCM atlas\n"
        "(cycle 6 / PR #262) to derive the Higgs Y assignment on the SM Yukawa\n"
        "surface.",
    ),
    (
        "status yaml condition",
        "conditional on:\n"
        "    - LHCM atlas (cycle 6, PR #262) modulo SM-definition conventions\n"
        "    - SM hypercharge uniqueness theorem (proposed_retained, unaudited)\n"
        "    - SM Yukawa coupling structural form (admitted SM convention)",
    ),
    (
        "proposal boundary",
        "Multiple admitted conditions remain (SM Yukawa form, LHCM SM-definition\n"
        "  conventions). Honest tier is exact-support modulo these admissions.",
    ),
    (
        "machine proposal gate",
        "proposal_allowed: false",
    ),
]
for label, fragment in pinned_note_fragments:
    check(f"pinned {label}", fragment in note_text)


print("\nSUMMARY: Yukawa-closure algebra only; SM Yukawa form and upstream hypercharges remain source-bound.")
print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
sys.exit(1 if FAIL_COUNT else 0)
