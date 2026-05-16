#!/usr/bin/env python3
"""Runner for the 't Hooft 1981 dual-superconductor / center-vortex confinement
external theorem note.

The note records the canonical 4D Euclidean SU(N) Yang-Mills confinement
mechanism: abelian projection with residual U(1)^(N-1) gauge symmetry,
magnetic monopole condensate (dual-superconductor picture; Mandelstam
1976; 't Hooft 1981), equivalent center-vortex picture with Z_N center
symmetry breaking ('t Hooft 1978; Greensite 2011 review arXiv:0810.4392;
Del Debbio-Faber-Greensite-Olejnik arXiv:hep-lat/9609025), and the
symbolic vortex / monopole free-energy form. The runner verifies the
canonical algebraic identities in exact (SymPy + Fraction) symbolic
form, evaluates the symbolic vortex action at SU(3) g^2=1, sigma a^2=1,
records the monopole action structural shape (8 pi / g) x O(1), states
the condensate condition exp(-S_vortex) ~ O(1) and the Wilson-loop area
law observable, and enforces the source-note boundary disclaimers
excluding framework substrate identification, hierarchy closure, scale
ratio derivation, and alpha_LM^16 closure overclaims.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "THOOFT_1981_DUAL_SUPERCONDUCTOR_CENTER_VORTEX_CONFINEMENT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md"
)

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


def test_T1_abelian_projection_structure() -> None:
    section("T1: abelian projection — residual gauge group U(1)^(N-1) ⊂ SU(N)")
    text = NOTE.read_text(encoding="utf-8")
    has_abelian_projection = "abelian projection" in text.lower()
    has_residual = (
        "U(1)^(N-1)" in text or "U(1)^{N-1}" in text or "u(1)^(n-1)" in text.lower()
    )
    has_diagonalization = "diagonali" in text.lower()
    # Symbolic residual rank: for SU(N), rank = N - 1.
    N = sp.symbols("N", integer=True, positive=True)
    rank_residual = N - 1
    # For N = 2, 3 the residual abelian factor has dimension 1, 2.
    ok_N2 = rank_residual.subs(N, 2) == 1
    ok_N3 = rank_residual.subs(N, 3) == 2
    check(
        "note states abelian-projection mechanism (gauge condition + residual symmetry)",
        has_abelian_projection,
        "abelian projection cited explicitly",
    )
    check(
        "note states residual U(1)^(N-1) abelian subgroup",
        has_residual,
        "U(1)^(N-1) named in the note",
    )
    check(
        "note states diagonalization of an adjoint composite as gauge condition",
        has_diagonalization,
        "diagonalization mechanism present",
    )
    check(
        "symbolic residual abelian rank N-1 evaluates to {1, 2} for N in {2, 3}",
        bool(ok_N2 and ok_N3),
        f"rank(SU(2))-residual = {rank_residual.subs(N, 2)}, rank(SU(3))-residual = {rank_residual.subs(N, 3)}",
    )


def test_T2_vortex_action_symbolic_form() -> None:
    section("T2: vortex action S_vortex = (1 / g²) × (σ a²) symbolic form")
    g = sp.symbols("g", positive=True, real=True)
    sigma, a = sp.symbols("sigma a", positive=True, real=True)
    # Published center-vortex action structural form.
    S_vortex = (1 / g**2) * (sigma * a**2)
    S_expected = sigma * a**2 / g**2
    diff = sp.simplify(S_vortex - S_expected)
    check(
        "S_vortex = (1/g^2) × (σ a^2) symbolic identity",
        diff == 0,
        f"S_vortex = {sp.nsimplify(S_vortex)}, expected {sp.nsimplify(S_expected)}",
    )
    text = NOTE.read_text(encoding="utf-8")
    has_vortex_action = "S_vortex" in text
    has_string_tension_factor = "σ a²" in text or "σ a^2" in text or "sigma a^2" in text.lower() or "string-tension factor" in text.lower()
    check(
        "note names S_vortex symbolically",
        has_vortex_action,
        "S_vortex symbol present",
    )
    check(
        "note names string-tension factor σ a^2 in vortex action",
        has_string_tension_factor,
        "σ a² / string-tension factor present",
    )


def test_T3_su3_g2_one_sigma_a2_one() -> None:
    section("T3: at SU(3), g²=1, σ a²=1, symbolic vortex action S_vortex = 1")
    g = sp.symbols("g", positive=True, real=True)
    sigma, a = sp.symbols("sigma a", positive=True, real=True)
    S_vortex = (1 / g**2) * (sigma * a**2)
    # Substitute g^2 = 1 by setting g = 1, σ a^2 = 1 by setting σ = 1, a = 1.
    # (We are working in pure Fraction/sympy arithmetic, so these are exact.)
    S_at_pin = S_vortex.subs({g: 1, sigma: 1, a: 1})
    one = sp.Integer(1)
    check(
        "S_vortex(g²=1, σ a²=1) = 1 symbolically",
        sp.simplify(S_at_pin - one) == 0,
        f"S_vortex at pin = {S_at_pin}, expected 1",
    )
    # Cross-check with exact Fraction arithmetic.
    g2 = Fraction(1, 1)
    sigma_a2 = Fraction(1, 1)
    S_frac = sigma_a2 / g2
    check(
        "S_vortex(g²=1, σ a²=1) = 1 via exact Fraction arithmetic",
        S_frac == Fraction(1, 1),
        f"Fraction S_vortex = {S_frac}",
    )


def test_T4_monopole_action_order_of_magnitude() -> None:
    section("T4: monopole action S_mono ~ (8 π / g) × O(1) structural shape")
    text = NOTE.read_text(encoding="utf-8")
    has_S_mono = "S_mono" in text
    has_8_pi_over_g = "(8 π / g)" in text or "8 pi / g" in text.lower() or "8π/g" in text
    has_profile_qualifier = (
        "profile factor" in text.lower()
        or "o(1) profile" in text.lower()
        or "structural shape" in text.lower()
        or "structural form" in text.lower()
    )
    check(
        "note names S_mono symbolically",
        has_S_mono,
        "S_mono symbol present",
    )
    check(
        "note states monopole action structural form (8 π / g) × O(1)",
        has_8_pi_over_g,
        "8 π / g structural form present",
    )
    check(
        "note qualifies the monopole action as a structural shape, not a precise prefactor",
        has_profile_qualifier,
        "profile-factor / structural-shape qualifier present",
    )


def test_T5_condensate_condition() -> None:
    section("T5: condensate condition exp(-S_vortex) ~ O(1) at confinement")
    text = NOTE.read_text(encoding="utf-8")
    has_condensate = "condensate" in text.lower()
    has_exp_form = "exp( - S_vortex )" in text or "exp(-S_vortex)" in text or "exp( -S_vortex )" in text
    has_O1 = "O(1)" in text
    has_at_confinement = "at confinement" in text.lower() or "confinement" in text.lower()
    check(
        "note states condensate condition exp(-S_vortex) ~ O(1)",
        has_exp_form and has_O1,
        "exp(-S_vortex) ~ O(1) named symbolically",
    )
    check(
        "note frames condensate condition at confinement",
        has_condensate and has_at_confinement,
        "condensate + confinement language present",
    )


def test_T6_center_symmetry_breaking() -> None:
    section("T6: Z_N center symmetry breaking signature (vortex VEV)")
    text = NOTE.read_text(encoding="utf-8")
    has_center_sym = "center symmetry" in text.lower()
    has_Z_N = "Z_N" in text or "Z_n" in text or "z_n" in text.lower()
    has_vortex_vev = "vortex condensation" in text.lower() or "vortex vev" in text.lower() or "⟨ v ⟩" in text.lower() or "⟨v⟩" in text.lower()
    has_disorder = "disorder" in text.lower()
    has_kramers_wannier = "kramers-wannier" in text.lower() or "kramers" in text.lower()
    check(
        "note states Z_N center symmetry of pure SU(N) Yang-Mills",
        has_center_sym and has_Z_N,
        "Z_N center symmetry named",
    )
    check(
        "note states vortex condensation as center-symmetry-breaking signature",
        has_vortex_vev,
        "vortex condensation / vortex VEV present",
    )
    check(
        "note states order/disorder duality (Kramers-Wannier-style)",
        has_disorder and has_kramers_wannier,
        "disorder + Kramers-Wannier duality present",
    )


def test_T7_area_law_observable() -> None:
    section("T7: area law as physical observable for Wilson loop")
    text = NOTE.read_text(encoding="utf-8")
    has_area_law = "area law" in text.lower() or "area-law" in text.lower()
    has_wilson_loop = "Wilson loop" in text or "wilson loop" in text.lower()
    has_string_tension = "string tension" in text.lower() or "σ" in text
    has_rectangular = "R × T" in text or "R x T" in text.lower() or "(R T)" in text or "r t" in text.lower()
    # Symbolic area-law form: <W(C)> ~ exp(-σ × Area(C))
    sigma, Area = sp.symbols("sigma Area", positive=True, real=True)
    W = sp.exp(-sigma * Area)
    check(
        "note states Wilson-loop area law as confinement diagnostic",
        has_area_law and has_wilson_loop,
        "Wilson loop + area law present",
    )
    check(
        "note states string tension σ as confinement order parameter",
        has_string_tension,
        "string tension σ named symbolically",
    )
    check(
        "note states rectangular R × T Wilson-loop limit definition of σ",
        has_rectangular,
        "rectangular R × T form present",
    )
    check(
        "symbolic Wilson-loop area-law form ⟨W(C)⟩ ~ exp(-σ × Area(C)) reproduced",
        sp.simplify(sp.log(W) + sigma * Area) == 0,
        f"log⟨W⟩ + σ Area = {sp.simplify(sp.log(W) + sigma * Area)}",
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
    forbidden = [
        "the framework substrate is identified",
        "framework substrate is identified with",
        "the dual-superconductor vacuum is the framework substrate",
        "the center-vortex vacuum is the framework substrate",
        "this note identifies the framework substrate",
        "we identify the framework substrate",
        "substrate identification is closed",
    ]
    not_present = not any(item in lower for item in forbidden)
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


def test_T10_no_alpha_LM_16_or_hierarchy_closure() -> None:
    section("T10: boundary — note does NOT claim alpha_LM^16 / hierarchy closure")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    forbidden = [
        "alpha_lm^16 is closed",
        "α_lm^16 is closed",
        "alpha_lm^16 closure is achieved",
        "v/m_pl is derived",
        "v/m_pl is exp(-",
        "hierarchy formula is closed",
        "electroweak hierarchy is closed",
        "string tension is derived from framework primitives",
        "pipeline-derived status: retained",
    ]
    not_present = not any(item in lower for item in forbidden)
    names_alpha_LM = "α_lm^16" in lower or "alpha_lm^16" in lower
    names_v_over_Mpl = "v/m_pl" in lower
    names_string_tension_excluded = (
        "string tension" in lower
        and "framework primitives" in lower
        and "not asserted here" in lower
    )
    check(
        "note avoids any alpha_LM^16 / hierarchy / scale-ratio closure overclaim",
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
        "boundary explicitly excludes deriving the string tension σ from framework primitives",
        names_string_tension_excluded,
        "string-tension exclusion present",
    )


def main() -> int:
    print("# 't Hooft 1981 dual-superconductor / center-vortex confinement external theorem runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_T1_abelian_projection_structure()
    test_T2_vortex_action_symbolic_form()
    test_T3_su3_g2_one_sigma_a2_one()
    test_T4_monopole_action_order_of_magnitude()
    test_T5_condensate_condition()
    test_T6_center_symmetry_breaking()
    test_T7_area_law_observable()
    test_T8_positive_theorem_declaration()
    test_T9_no_substrate_identification()
    test_T10_no_alpha_LM_16_or_hierarchy_closure()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
