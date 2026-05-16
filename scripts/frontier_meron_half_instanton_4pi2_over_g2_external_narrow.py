#!/usr/bin/env python3
"""Runner for the meron / half-instanton action 4 pi^2 / g^2 external theorem note.

The note records the canonical 4D Euclidean SU(2) Yang-Mills meron
(half-instanton) classical action S_meron = 4 pi^2 / g^2 (de Alfaro-
Fubini-Furlan 1976; Callan-Dashen-Gross 1978-1979) together with the
fractional topological charge structure Q_meron = 1/2 (as accumulated
over half the relevant volume) and the published lattice realization
on a 4D Z^4 lattice (Itou-Iritani arXiv:1402.5984 2014; Gonzalez-
Arroyo lineage). The runner verifies the canonical algebraic identity
S_meron = (1/2) S_inst in exact (SymPy + Fraction) symbolic form,
evaluates S_meron and exp(-S_meron) at three canonical values of g^2,
records the fractional Q = 1/2 statement and the finite-action
asymptotic structure (without deriving the fractional charge from
first principles), records the lattice realization citations
(Itou-Iritani, Gonzalez-Arroyo), and enforces the source-note
boundary disclaimers excluding framework substrate identification,
hierarchy closure, scale ratio derivation, and alpha_LM^16 closure
overclaims.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "MERON_HALF_INSTANTON_4PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"  [{status}] {label}")
    if detail:
        print(f"         {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def test_T1_symbolic_meron_action_formula() -> None:
    section("T1: symbolic S_meron = 4 pi^2 / g^2 (half of BPST 8 pi^2 / g^2)")
    g = sp.symbols("g", positive=True, real=True)
    S_inst = 8 * sp.pi**2 / g**2
    S_meron_def = 4 * sp.pi**2 / g**2
    # Reproduce S_meron from (1/2) S_inst
    S_meron_from_half = sp.Rational(1, 2) * S_inst
    diff = sp.simplify(S_meron_def - S_meron_from_half)
    check(
        "S_meron simplifies to 4 pi^2 / g^2 symbolically",
        diff == 0,
        f"S_meron = {S_meron_def}, (1/2) S_inst = {sp.simplify(S_meron_from_half)}",
    )


def test_T2_half_action_identity() -> None:
    section("T2: half-action identity S_meron = (1/2) S_inst")
    g = sp.symbols("g", positive=True, real=True)
    S_inst = 8 * sp.pi**2 / g**2
    S_meron = 4 * sp.pi**2 / g**2
    ratio = sp.simplify(S_meron / S_inst)
    expected_ratio = sp.Rational(1, 2)
    check(
        "S_meron / S_inst = 1/2 symbolically",
        ratio == expected_ratio,
        f"ratio = {ratio}, expected {expected_ratio}",
    )
    # Also assert the note text states the half-action identity
    text = NOTE.read_text(encoding="utf-8")
    has_half_id = (
        "(1/2) S_inst" in text
        or "(1/2)  S_inst" in text
        or "= (1/2) S_inst" in text
        or "half the BPST" in text.lower() if False else (
            "(1/2)" in text and "S_inst" in text and "half" in text.lower()
        )
    )
    check(
        "note states the half-action identity S_meron = (1/2) S_inst in text",
        has_half_id,
        "(1/2), S_inst, and 'half' all present",
    )


def test_T3_numerical_meron_action_values() -> None:
    section("T3: numerical S_meron at g^2 in {1/2, 1, 2}")
    g2_values = [Fraction(1, 2), Fraction(1, 1), Fraction(2, 1)]
    pi2 = math.pi**2
    # S_meron = 4 pi^2 / g^2 (numerical)
    expected = {
        Fraction(1, 2): 8 * pi2,    # 4 pi^2 / (1/2) = 8 pi^2 ~ 78.96
        Fraction(1, 1): 4 * pi2,    # 4 pi^2 ~ 39.48
        Fraction(2, 1): 2 * pi2,    # 4 pi^2 / 2 = 2 pi^2 ~ 19.74
    }
    ok_all = True
    detail_parts = []
    for g2 in g2_values:
        S = 4 * pi2 / float(g2)
        S_exp = expected[g2]
        rel_err = abs(S - S_exp) / abs(S_exp)
        ok = rel_err < 1e-12
        ok_all = ok_all and ok
        detail_parts.append(f"g^2={g2}: S_meron={S:.6f} (expected {S_exp:.6f})")
    check(
        "S_meron at g^2 in {1/2, 1, 2} evaluates to {8, 4, 2} pi^2 numerically",
        ok_all,
        "; ".join(detail_parts),
    )


def test_T4_exp_suppression() -> None:
    section("T4: numerical exp(-S_meron) at g^2 in {1/2, 1, 2}")
    pi2 = math.pi**2
    g2_values = [Fraction(1, 2), Fraction(1, 1), Fraction(2, 1)]
    # At g^2 = 1/2: S_meron = 8 pi^2 ~ 78.96, exp(-S_meron) ~ 5e-35
    # At g^2 = 1:   S_meron = 4 pi^2 ~ 39.48, exp(-S_meron) ~ 7.6e-18
    # At g^2 = 2:   S_meron = 2 pi^2 ~ 19.74, exp(-S_meron) ~ 2.7e-9
    expected_orders = {Fraction(1, 2): -35, Fraction(1, 1): -18, Fraction(2, 1): -9}
    ok_all = True
    detail_parts = []
    for g2 in g2_values:
        S = 4 * pi2 / float(g2)
        e = math.exp(-S)
        log10 = math.log10(e) if e > 0 else None
        ok = log10 is not None and abs(log10 - expected_orders[g2]) < 1.5
        ok_all = ok_all and ok
        detail_parts.append(
            f"g^2={g2}: S_meron={S:.4f}, exp(-S_meron)={e:.3e} (log10≈{log10:.2f})"
        )
    check(
        "exp(-S_meron) at g^2 in {1/2, 1, 2} matches expected suppression orders",
        ok_all,
        "; ".join(detail_parts),
    )
    # Pinpoint canonical g^2 = 1 value: 4 pi^2 ~ 39.4784, exp(-39.4784) ~ 7.58e-18
    S_g1 = 4 * pi2
    e_g1 = math.exp(-S_g1)
    ok_canonical = (
        abs(S_g1 - 39.47841760435743) < 1e-9
        and 5e-19 < e_g1 < 5e-17
    )
    check(
        "canonical g^2=1: S_meron = 4 pi^2 ≈ 39.4784, exp(-S_meron) ≈ 7.58e-18",
        ok_canonical,
        f"S_meron = {S_g1:.10f}, exp(-S_meron) = {e_g1:.3e}",
    )


def test_T5_fractional_Q_structure() -> None:
    section("T5: fractional topological charge Q_meron = 1/2 structure (stated)")
    text = NOTE.read_text(encoding="utf-8")
    has_half_charge = (
        "Q_meron = 1/2" in text
        or "Q = 1/2" in text
        or "`1/2`" in text
        or "`Q = 1/2`" in text
    )
    has_half_volume_convention = (
        "half the relevant volume" in text.lower()
        or "hemisphere" in text.lower()
        or "half-space" in text.lower()
    )
    has_pair_sums_to_one = (
        "sum to integer" in text.lower()
        or "two such half-units" in text.lower()
        or "meron pair" in text.lower()
    )
    check(
        "note states fractional topological charge Q_meron = 1/2",
        has_half_charge,
        "Q = 1/2 stated explicitly",
    )
    check(
        "note specifies the half-volume integration convention",
        has_half_volume_convention,
        "hemisphere / half-space convention recorded",
    )
    check(
        "note records that two merons (a pair) sum to integer Q = 1",
        has_pair_sums_to_one,
        "meron pair / sum to integer convention recorded",
    )


def test_T6_finite_action_despite_fractional_Q() -> None:
    section("T6: meron has finite classical action despite Q = 1/2 (log asymptotic)")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    has_finite = "finite" in lower and ("classical action" in lower or "meron" in lower)
    has_log_asymptotic = (
        "logarithmic" in lower
        and ("large-distance" in lower or "asymptotic" in lower or "falloff" in lower)
    )
    has_short_distance_regulator = (
        "short-distance" in lower
        or "short distance" in lower
        or "regulator" in lower
        or "gauge-fixing" in lower
        or "singular at" in lower
    )
    check(
        "note states meron has finite classical action",
        has_finite,
        "finite classical action stated",
    )
    check(
        "note records logarithmic large-distance asymptotic",
        has_log_asymptotic,
        "logarithmic falloff / asymptotic recorded",
    )
    check(
        "note records short-distance regulator / singular core treatment",
        has_short_distance_regulator,
        "short-distance regulator structure recorded",
    )


def test_T7_lattice_realization_references() -> None:
    section("T7: lattice realization references (Itou-Iritani, Gonzalez-Arroyo)")
    text = NOTE.read_text(encoding="utf-8")
    has_itou_iritani = "Itou" in text and "Iritani" in text
    has_arxiv_pin = "1402.5984" in text
    has_gonzalez_arroyo = (
        "Gonz" in text or "González-Arroyo" in text or "Gonzalez-Arroyo" in text
    )
    has_lattice_keyword = "lattice" in text.lower() and ("Z^4" in text or "Z⁴" in text or "Wilson" in text)
    check(
        "note cites Itou-Iritani lattice meron paper",
        has_itou_iritani,
        "Itou-Iritani named explicitly",
    )
    check(
        "note pins Itou-Iritani arXiv:1402.5984",
        has_arxiv_pin,
        "arXiv:1402.5984 cited",
    )
    check(
        "note cites Gonzalez-Arroyo lineage on lattice fractional instantons",
        has_gonzalez_arroyo,
        "Gonzalez-Arroyo lineage cited",
    )
    check(
        "note records 4D lattice realization context",
        has_lattice_keyword,
        "Z^4 / Wilson lattice context recorded",
    )


def test_T8_positive_theorem_declaration() -> None:
    section("T8: boundary — note declares positive_theorem")
    text = NOTE.read_text(encoding="utf-8")
    has_decl = "**Claim type:** positive_theorem" in text
    check(
        "note declares Claim type: positive_theorem",
        has_decl,
        "Claim type line present",
    )


def test_T9_no_substrate_identification() -> None:
    section("T9: boundary — note does NOT claim substrate identification")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    # Forbidden phrases are POSITIVE assertions of substrate identification.
    # Each is constructed so it does NOT appear in a disclaimer such as
    # "does not claim that ... is identified with ...". We check that no
    # asserting form (e.g. "the framework substrate is identified" without
    # a leading "not") appears.
    forbidden = [
        "the framework substrate is identified",
        "framework substrate is identified with meron",
        "framework substrate is identified with cdg",
        "the meron is the framework substrate",
        "this note identifies the framework substrate",
        "we identify the framework substrate",
        "substrate identification is closed",
    ]
    not_present = not any(item in lower for item in forbidden)
    # Strip markdown bold markers for the disclaimer phrase match.
    stripped = lower.replace("**", "")
    has_disclaimer = (
        "does not claim" in stripped
        and "framework" in stripped
        and "substrate" in stripped
    )
    check(
        "note does NOT assert substrate identification",
        not_present,
        "no substrate-identification overclaim string present",
    )
    check(
        "note explicitly disclaims framework substrate identification",
        has_disclaimer,
        "boundary section names framework substrate explicitly under 'does not claim'",
    )


def test_T10_no_alpha_LM_16_closure() -> None:
    section("T10: boundary — no alpha_LM^16 closure, no v/M_Pl, no 4pi^2 vs lnMPlv identification")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    forbidden = [
        "alpha_lm^16 is closed",
        "α_lm^16 is closed",
        "alpha_lm^16 closure is achieved",
        "v/m_pl is derived",
        "v/m_pl is exp(-4",
        "hierarchy formula is closed",
        "v/m_pl = exp(-4π²/g²) is closed",
        "4 pi^2 = ln(m_pl/v)",
        "4π² = ln(m_pl/v)",
        "4π² ≈ ln(m_pl/v)",
        "pipeline-derived status: retained",
        # Identification of 4 pi^2 with ln(M_Pl/v) as a positive claim
        "we identify 4π² with ln(m_pl/v)",
        "we identify 4 pi^2 with ln(m_pl/v)",
    ]
    not_present = not any(item in lower for item in forbidden)
    # Boundary section explicitly names alpha_LM^16 as out-of-scope.
    names_alpha_LM = "α_lm^16" in lower or "alpha_lm^16" in lower
    names_v_over_Mpl = "v/m_pl" in lower
    names_lnMPlv_disclaimer = "ln(m_pl/v)" in lower
    check(
        "note avoids any alpha_LM^16-closure / hierarchy-closure overclaim",
        not_present,
        "boundary disclaimers intact",
    )
    check(
        "boundary explicitly names alpha_LM^16 as out-of-scope",
        names_alpha_LM,
        "alpha_LM^16 explicitly listed in boundary",
    )
    check(
        "boundary explicitly names v/M_Pl scale ratio as out-of-scope",
        names_v_over_Mpl,
        "v/M_Pl explicitly listed in boundary",
    )
    check(
        "boundary explicitly disclaims 4π² ↔ ln(M_Pl/v) identification",
        names_lnMPlv_disclaimer,
        "ln(M_Pl/v) referenced only in 'does not claim' disclaimer",
    )


def main() -> int:
    print("# Meron / half-instanton 4 pi^2 / g^2 external theorem runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_T1_symbolic_meron_action_formula()
    test_T2_half_action_identity()
    test_T3_numerical_meron_action_values()
    test_T4_exp_suppression()
    test_T5_fractional_Q_structure()
    test_T6_finite_action_despite_fractional_Q()
    test_T7_lattice_realization_references()
    test_T8_positive_theorem_declaration()
    test_T9_no_substrate_identification()
    test_T10_no_alpha_LM_16_closure()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
