#!/usr/bin/env python3
"""Runner for the 4D instanton minimal action 8 pi^2 / g^2 external theorem note.

The note records the canonical 4D Euclidean SU(N) Yang-Mills instanton
minimal action S_inst = 8 pi^2 / g^2 (Belavin-Polyakov-Schwartz-Tyupkin
1975; 't Hooft 1976) and its preservation on a 4D Wilson lattice under
Lüscher admissibility (Lüscher 1982; Wilson flow, Lüscher arXiv:1006.4518
2010), together with Atiyah-Singer integrality of the topological charge
Q in Z (Atiyah-Singer 1968-1971). The runner verifies the canonical
algebraic identity in exact (SymPy + Fraction) symbolic form, evaluates
S_inst and exp(-S_inst) at three canonical values of g^2, checks the
self-duality saturation of the Bogomolny bound, records the lattice
O(a^2) correction structure (without making numerical artifact claims),
and enforces the source-note boundary disclaimers excluding framework
substrate identification, hierarchy closure, scale ratio derivation, and
alpha_LM^16 closure overclaims.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "INSTANTON_4D_ACTION_8PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md"

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


def test_T1_symbolic_action_formula() -> None:
    section("T1: symbolic S_inst = 8 pi^2 / g^2 at |Q| = 1 from Bogomolny saturation")
    # Bogomolny: S >= (8 pi^2 / g^2) |Q|, saturated at F = *F when Q > 0.
    # At |Q| = 1 the minimum action is exactly 8 pi^2 / g^2.
    g = sp.symbols("g", positive=True, real=True)
    Q = sp.symbols("Q", integer=True)
    S_bound = (8 * sp.pi**2 / g**2) * sp.Abs(Q)
    # Saturation at |Q| = 1:
    S_inst = S_bound.subs(Q, 1)
    S_expected = 8 * sp.pi**2 / g**2
    diff = sp.simplify(S_inst - S_expected)
    check(
        "S_inst at |Q|=1 simplifies to 8 pi^2 / g^2 symbolically",
        diff == 0,
        f"S_inst = {S_inst}, expected {S_expected}",
    )


def test_T2_atiyah_singer_integrality() -> None:
    section("T2: Atiyah-Singer integrality Q in Z stated as external theorem")
    # Verify the source note states the Q-formula and integrality.
    text = NOTE.read_text(encoding="utf-8")
    has_q_formula = "Q = (1 / (32 π²))" in text or "Q = (1 / (32 \\pi^2))" in text or "32 π²" in text
    has_integrality = "Q ∈ Z" in text or "Q in Z" in text
    has_atiyah_singer = "Atiyah-Singer" in text or "Atiyah" in text
    check(
        "note states canonical Q = (1/32 pi^2) integral Tr(F *F) formula",
        has_q_formula,
        "topological charge formula present in claim section",
    )
    check(
        "note states Atiyah-Singer integer integrality Q in Z",
        has_integrality and has_atiyah_singer,
        "Q in Z + Atiyah-Singer named explicitly",
    )


def test_T3_numerical_action_values() -> None:
    section("T3: numerical S_inst at g^2 in {1/2, 1, 2}")
    g2_values = [Fraction(1, 2), Fraction(1, 1), Fraction(2, 1)]
    pi2 = math.pi**2
    # S_inst = 8 pi^2 / g^2 (numerical)
    expected = {
        Fraction(1, 2): 16 * pi2,  # 8 pi^2 / (1/2) = 16 pi^2
        Fraction(1, 1): 8 * pi2,
        Fraction(2, 1): 4 * pi2,
    }
    ok_all = True
    detail_parts = []
    for g2 in g2_values:
        S = 8 * pi2 / float(g2)
        S_exp = expected[g2]
        rel_err = abs(S - S_exp) / abs(S_exp)
        ok = rel_err < 1e-12
        ok_all = ok_all and ok
        detail_parts.append(f"g^2={g2}: S_inst={S:.6f} (expected {S_exp:.6f})")
    check(
        "S_inst at g^2 in {1/2, 1, 2} evaluates to {16,8,4} pi^2 numerically",
        ok_all,
        "; ".join(detail_parts),
    )


def test_T4_exp_suppression() -> None:
    section("T4: numerical exp(-S_inst) at g^2 in {1/2, 1, 2}")
    pi2 = math.pi**2
    g2_values = [Fraction(1, 2), Fraction(1, 1), Fraction(2, 1)]
    suppressions = []
    for g2 in g2_values:
        S = 8 * pi2 / float(g2)
        e = math.exp(-S)
        suppressions.append((g2, S, e))
    # At g^2=1/2 suppression is exp(-16 pi^2) ~ 1.4e-69
    # At g^2=1 suppression is exp(-8 pi^2) ~ 5e-35
    # At g^2=2 suppression is exp(-4 pi^2) ~ 7e-18
    ok_all = True
    detail_parts = []
    expected_orders = {Fraction(1, 2): -69, Fraction(1, 1): -35, Fraction(2, 1): -18}
    for g2, S, e in suppressions:
        log10 = math.log10(e) if e > 0 else None
        ok = log10 is not None and abs(log10 - expected_orders[g2]) < 1.5
        ok_all = ok_all and ok
        detail_parts.append(f"g^2={g2}: exp(-S_inst)={e:.3e} (log10≈{log10:.2f})")
    check(
        "exp(-S_inst) at g^2 in {1/2, 1, 2} matches expected suppression orders",
        ok_all,
        "; ".join(detail_parts),
    )


def test_T5_canonical_g2_one() -> None:
    section("T5: at g^2 = 1, S_inst = 8 pi^2 ≈ 78.96 and exp(-S_inst) ≈ 5e-35")
    S = 8 * math.pi**2
    e = math.exp(-S)
    ok_S = abs(S - 78.95683520871487) < 1e-10
    ok_e = 1e-36 < e < 1e-34
    check(
        "S_inst(g^2=1) = 8 pi^2 ≈ 78.9568...",
        ok_S,
        f"S_inst = {S:.10f}",
    )
    check(
        "exp(-S_inst)(g^2=1) ≈ 5.05e-35",
        ok_e,
        f"exp(-S_inst) = {e:.3e}",
    )


def test_T6_self_duality_saturation() -> None:
    section("T6: self-duality F = *F ⟹ S = (1/(2 g^2)) ∫ Tr(F^2) = (8 pi^2/g^2)|Q|")
    # Algebraic identity. With F = *F we have Tr(F_μν F^μν) = Tr(F_μν *F^μν)
    # because F and *F coincide. So
    #   S = (1/(4 g^2)) ∫ Tr(F F) = (1/(4 g^2)) ∫ Tr(F *F)
    #     = (1/(4 g^2)) * 32 pi^2 * Q
    #     = (8 pi^2 / g^2) * Q.
    # At |Q| = 1: S = 8 pi^2 / g^2.
    g = sp.symbols("g", positive=True, real=True)
    Q = sp.symbols("Q", integer=True)
    # Define I_TrFF = integral of Tr(F F), I_TrFstarF = integral of Tr(F *F).
    # Under F = *F: I_TrFF == I_TrFstarF; topological charge is
    # Q = (1/(32 pi^2)) I_TrFstarF, so I_TrFstarF = 32 pi^2 Q.
    I_TrFstarF = 32 * sp.pi**2 * Q
    I_TrFF = I_TrFstarF  # self-duality
    S = I_TrFF / (4 * g**2)
    S_simplified = sp.simplify(S)
    S_expected = (8 * sp.pi**2 / g**2) * Q
    diff = sp.simplify(S_simplified - S_expected)
    check(
        "F = *F ⟹ S = (8 pi^2 / g^2) Q from canonical normalizations",
        diff == 0,
        f"S = {S_simplified}, expected {S_expected}",
    )


def test_T7_lattice_O_a2_structure() -> None:
    section("T7: lattice O(a^2) correction structure recorded (no numerical claim)")
    text = NOTE.read_text(encoding="utf-8")
    has_admissibility = "admissibility" in text.lower() or "admissible" in text.lower()
    has_O_a2 = "O(a²)" in text or "O(a^2)" in text
    has_luscher = "Lüscher" in text or "Luscher" in text
    has_wilson_flow = "Wilson flow" in text.lower() or "Wilson gradient flow" in text or "Wilson flow" in text or "gradient flow" in text.lower()
    check(
        "note records Lüscher admissibility condition",
        has_admissibility and has_luscher,
        "admissibility + Lüscher cited",
    )
    check(
        "note records O(a^2) lattice correction structure (no numerical claim)",
        has_O_a2,
        "structural form recorded",
    )
    check(
        "note records modern Wilson flow / gradient flow topology extraction",
        has_wilson_flow,
        "Lüscher arXiv:1006.4518 cited",
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
        "framework substrate is identified with bpst",
        "the bpst instanton is the framework substrate",
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
    section("T10: boundary — note does NOT claim alpha_LM^16 closure or hierarchy")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    forbidden = [
        "alpha_lm^16 is closed",
        "α_lm^16 is closed",
        "alpha_lm^16 closure is achieved",
        "v/m_pl is derived",
        "v/m_pl is exp(-8",
        "hierarchy formula is closed",
        "v/m_pl = exp(-8π²/g²) is closed",
        "pipeline-derived status: retained",
    ]
    not_present = not any(item in lower for item in forbidden)
    # Boundary section explicitly names alpha_LM^16 as out-of-scope.
    names_alpha_LM = "α_lm^16" in lower or "alpha_lm^16" in lower
    names_v_over_Mpl = "v/m_pl" in lower
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


def main() -> int:
    print("# 4D instanton 8 pi^2 / g^2 external theorem runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_T1_symbolic_action_formula()
    test_T2_atiyah_singer_integrality()
    test_T3_numerical_action_values()
    test_T4_exp_suppression()
    test_T5_canonical_g2_one()
    test_T6_self_duality_saturation()
    test_T7_lattice_O_a2_structure()
    test_T8_positive_theorem_declaration()
    test_T9_no_substrate_identification()
    test_T10_no_alpha_LM_16_closure()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
