#!/usr/bin/env python3
"""Runner for the 4D instanton action bounded normalization certificate.

The note no longer certifies the broader external instanton theorem package.
It only records the supplied-normalization algebra giving
S_inst = 8 pi^2 / g^2 for a charge-one self-dual sector, evaluates the
arithmetic consequences at three sample couplings, and enforces boundaries.
Atiyah-Singer integrality, BPST existence, and Luescher lattice-topology
preservation remain context only and are not load-bearing retained inputs for
this row.
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


def test_T2_global_inputs_non_load_bearing() -> None:
    section("T2: global instanton inputs are explicitly non-load-bearing context")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    names_global_inputs = (
        "atiyah-singer" in lower
        and "bpst" in lower
        and ("luescher" in lower or "lüscher" in lower)
    )
    non_load_bearing = "not load-bearing retained authorities" in lower or "non-load-bearing" in lower
    explicit_context = "external context only" in lower
    not_retained_inputs = "not retained-grade inputs" in lower
    names_non_claims = (
        "does **not** claim" in lower
        and "retained atiyah-singer integrality" in lower
        and "retained bpst existence" in lower
        and ("retained luescher lattice-topology preservation" in lower or "retained lüscher lattice-topology preservation" in lower)
    )
    check(
        "note names Atiyah-Singer/BPST/Luescher as background only",
        names_global_inputs and explicit_context,
        "global theorem package is present only in the context section",
    )
    check(
        "note states global theorem package is not retained/load-bearing for this row",
        non_load_bearing and not_retained_inputs and names_non_claims,
        "non-claims section and context boundary are explicit",
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


def test_T7_lattice_context_is_non_retained() -> None:
    section("T7: lattice/admissibility language is context only, not a retained theorem")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    has_lattice_terms = (
        ("luescher" in lower or "lüscher" in lower)
        and ("admissibility" in lower or "admissible" in lower)
        and ("wilson-flow" in lower or "wilson flow" in lower or "gradient flow" in lower)
    )
    has_nonclaim = (
        "does **not** claim" in lower
        and ("retained luescher lattice-topology preservation" in lower or "retained lüscher lattice-topology preservation" in lower)
    )
    has_scope_boundary = (
        "not a retained preservation theorem" in lower
        or "not cited here as retained authority" in lower
        or "context only" in lower
    )
    avoids_binding_continuum_control = (
        "continuum-limit `o(a²)` control" in lower
        or "continuum-limit `o(a^2)` control" in lower
        or "continuum-limit" in lower and "control" in lower and "does **not** claim" in lower
    )
    check(
        "note keeps Luescher/admissibility/Wilson-flow language visible as context",
        has_lattice_terms,
        "lattice language remains available for later bridge work",
    )
    check(
        "note disclaims retained lattice-topology preservation and continuum control",
        has_nonclaim and has_scope_boundary and avoids_binding_continuum_control,
        "lattice package is non-load-bearing for this bounded certificate",
    )


def test_T8_bounded_theorem_declaration() -> None:
    section("T8: boundary — note declares bounded_theorem")
    text = NOTE.read_text(encoding="utf-8")
    has_decl = "**Claim type:** bounded_theorem" in text
    has_type = "**Type:** bounded_theorem" in text
    lacks_old_decl = "**Claim type:** positive_theorem" not in text
    check(
        "note declares bounded_theorem and no longer declares positive_theorem",
        has_decl and has_type and lacks_old_decl,
        "bounded metadata lines present",
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
    print("# 4D instanton 8 pi^2 / g^2 bounded normalization runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_T1_symbolic_action_formula()
    test_T2_global_inputs_non_load_bearing()
    test_T3_numerical_action_values()
    test_T4_exp_suppression()
    test_T5_canonical_g2_one()
    test_T6_self_duality_saturation()
    test_T7_lattice_context_is_non_retained()
    test_T8_bounded_theorem_declaration()
    test_T9_no_substrate_identification()
    test_T10_no_alpha_LM_16_closure()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
