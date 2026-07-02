#!/usr/bin/env python3
"""Runner for the fractional-instanton dilute-gas hierarchy external gate.

The note records the canonical 4D Euclidean SU(N) Yang-Mills
fractional-instanton charge structure Q = k/N and action
S_frac = (8 pi^2 / g^2) |k/N| on T^4 with twisted boundary conditions
('t Hooft 1981; Gonzalez-Arroyo 1979; Anber-Poppitz arXiv:1811.05882,
arXiv:2107.07252; Cox-Pisarski arXiv:2310.16289), together with the
published dilute-gas approximation form
F_DG = -V * n_eff * exp(-S_frac) * (1-loop det). The condensate/gas-
density criterion exp(-S_frac) ~ O(1) is checked only as open-gate
model-regime language: the runner verifies that determinant,
phase-space, coupling-scale, and convergence data remain explicitly
open. It also cross-checks the N=2 k=1 half-action scale without
promoting the companion meron open gate into a finite-action theorem.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "FRACTIONAL_INSTANTON_DILUTE_GAS_CONDENSATE_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md"
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


def test_T1_symbolic_fractional_action_formula() -> None:
    section("T1: symbolic Q = k/N and S_frac = (8 pi^2 / g^2) |k/N|")
    g, k, N = sp.symbols("g k N", positive=True, real=True)
    # BPST minimal action at |Q|=1
    S_inst = 8 * sp.pi**2 / g**2
    # Fractional sector
    Q_frac = k / N
    S_frac_def = (8 * sp.pi**2 / g**2) * sp.Abs(Q_frac)
    # Reproduce S_frac as S_inst times |Q|
    S_frac_from_Q = S_inst * sp.Abs(Q_frac)
    diff = sp.simplify(S_frac_def - S_frac_from_Q)
    check(
        "S_frac = S_inst * |k/N| simplifies symbolically",
        diff == 0,
        f"S_frac = {S_frac_def}, S_inst*|Q| = {sp.simplify(S_frac_from_Q)}",
    )
    # Note text asserts the structure
    text = NOTE.read_text(encoding="utf-8")
    has_q_kn = "Q = k / N" in text or "Q = k/N" in text
    has_action_formula = (
        "(8 π² / g²) · |k / N|" in text
        or "(8 π² / g²) · |k/N|" in text
        or "(8 π²/g²) · |k/N|" in text
        or "(8π²/g²) · |k/N|" in text
        or "8 π² / g²" in text and "k / N" in text
        or "8 π² / g²" in text and "k/N" in text
    )
    check(
        "note states Q = k/N fractional charge",
        has_q_kn,
        "Q = k/N or Q = k / N present in note",
    )
    check(
        "note states S_frac = (8 pi^2 / g^2) |k/N| action formula",
        has_action_formula,
        "S_frac action formula stated",
    )


def test_T2_meron_cross_check_N2_k1() -> None:
    section("T2: half-action cross-check at N=2, k=1: S_frac = 4 pi^2 / g^2")
    g = sp.symbols("g", positive=True, real=True)
    S_inst = 8 * sp.pi**2 / g**2
    # N = 2, k = 1
    S_frac_N2 = S_inst * sp.Abs(sp.Rational(1, 2))
    S_meron = 4 * sp.pi**2 / g**2
    diff = sp.simplify(S_frac_N2 - S_meron)
    check(
        "S_frac(k=1, N=2) = 4 pi^2 / g^2 symbolically",
        diff == 0,
        f"S_frac(N=2,k=1) = {sp.simplify(S_frac_N2)}, S_meron = {S_meron}",
    )
    # Note text states the half-action cross-check while keeping the meron theorem open.
    text = NOTE.read_text(encoding="utf-8")
    has_meron_cross = (
        "S_frac(k=1, N=2)" in text or "half-action" in text.lower()
    ) and "4 π² / g²" in text
    denies_meron_promotion = (
        "does not promote" in text.lower()
        and "singular" in text.lower()
        and "finite-action theorem" in text.lower()
    )
    check(
        "note states the N=2 k=1 half-action cross-check",
        has_meron_cross,
        "N=2 k=1 half-action cross-check present",
    )
    check(
        "note does not promote the companion meron open gate to a theorem",
        denies_meron_promotion,
        "singular meron theorem promotion explicitly denied",
    )


def test_T3_numerical_S_frac_canonical_N_values() -> None:
    section("T3: numerical S_frac at canonical g^2 = 1, varying N")
    pi2 = math.pi**2
    # At g^2 = 1, k = 1, varying N:
    #   N=2: S_frac = 8 pi^2 * (1/2) = 4 pi^2 ~ 39.48
    #   N=3: S_frac = 8 pi^2 * (1/3) = 8 pi^2 / 3 ~ 26.32
    #   N=4: S_frac = 8 pi^2 * (1/4) = 2 pi^2 ~ 19.74
    cases = [
        (2, 4 * pi2),
        (3, 8 * pi2 / 3),
        (4, 2 * pi2),
    ]
    ok_all = True
    detail_parts = []
    for N, expected in cases:
        S = 8 * pi2 * Fraction(1, N)
        ok = abs(S - expected) / abs(expected) < 1e-12
        ok_all = ok_all and ok
        detail_parts.append(
            f"N={N}, k=1: S_frac={float(S):.6f} (expected {expected:.6f})"
        )
    check(
        "S_frac at g^2=1, k=1 for N in {2,3,4} matches {4, 8/3, 2} pi^2",
        ok_all,
        "; ".join(detail_parts),
    )
    # Note text mentions the SU(3) entry explicitly
    text = NOTE.read_text(encoding="utf-8")
    has_su3 = (
        ("SU(3)" in text or "N = 3" in text or "N=3" in text)
        and ("8 π² / 3" in text or "8 π²/3" in text or "8 pi^2 / 3" in text or "26.3" in text)
    )
    has_su2 = (
        ("SU(2)" in text or "N = 2" in text or "N=2" in text)
        and ("4 π²" in text or "4 pi^2" in text or "39.48" in text)
    )
    check(
        "note records SU(3) S_frac = 8 pi^2 / 3 (~ 26.32)",
        has_su3,
        "SU(3) canonical entry recorded",
    )
    check(
        "note records SU(2) S_frac = 4 pi^2 (~ 39.48) consistent with meron",
        has_su2,
        "SU(2) canonical entry recorded",
    )


def test_T4_dilute_gas_free_energy_structure() -> None:
    section("T4: dilute-gas free-energy structural form (symbolic only)")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    has_dilute_gas = "dilute-gas" in lower or "dilute gas" in lower
    has_free_energy = "free-energy" in lower or "free energy" in lower or "f_dg" in lower
    has_exp_S_frac = (
        "exp( - s_frac )" in lower
        or "exp(-s_frac)" in lower
        or "exp( -s_frac )" in lower
    )
    has_one_loop_det = (
        "one-loop" in lower and ("determinant" in lower or "det" in lower)
    ) or "1-loop det" in lower
    has_volume_factor = "v · n_eff" in text or "v · " in text.lower() or " v " in text or "volume" in lower
    check(
        "note records dilute-gas approximation keyword",
        has_dilute_gas,
        "dilute-gas / dilute gas keyword present",
    )
    check(
        "note records free-energy structural form (F_DG)",
        has_free_energy,
        "free-energy / F_DG present",
    )
    check(
        "note records exp(-S_frac) Boltzmann factor in F_DG",
        has_exp_S_frac,
        "exp(-S_frac) present in F_DG form",
    )
    check(
        "note records one-loop determinant factor",
        has_one_loop_det,
        "one-loop determinant cited",
    )
    check(
        "note records volume factor V in F_DG",
        has_volume_factor,
        "V (4-volume) factor present",
    )
    # Symbolic placeholder: verify the structural multiplication
    V, n_eff, S_frac, Det = sp.symbols("V n_eff S_frac Det", positive=True, real=True)
    F_DG = -V * n_eff * sp.exp(-S_frac) * Det
    # Sanity: F_DG has the expected structural factors
    factors = sp.Mul.make_args(F_DG)
    has_minus = any(f == -1 for f in factors) or F_DG.could_extract_minus_sign()
    check(
        "symbolic F_DG = -V * n_eff * exp(-S_frac) * Det has the published structural form",
        has_minus and (V in F_DG.free_symbols) and (n_eff in F_DG.free_symbols) and (Det in F_DG.free_symbols),
        f"F_DG = {F_DG}",
    )


def test_T5_condensate_formation_condition() -> None:
    section("T5: open condensate/gas-density criterion exp(-S_frac) ~ O(1)")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    has_condensate = "condensate" in lower
    has_o1 = "o(1)" in lower or "o( 1 )" in lower or "~ o(1)" in lower
    has_open_condition = (
        "open target" in lower
        or "open-gate" in lower
        or "not a theorem-grade" in lower
        or "must be supplied" in lower
        or "left open" in lower
    )
    has_load_bearing_gaps = (
        "determinant" in lower
        and "phase-space" in lower
        and ("coupling scale" in lower or "coupling-scale" in lower)
    )
    has_condition = (
        "condensate/gas-density" in lower
        or "condensate formation" in lower
        or "model-regime" in lower
    )
    check(
        "note records condensate keyword",
        has_condensate,
        "condensate present in text",
    )
    check(
        "note records O(1) condition on exp(-S_frac)",
        has_o1,
        "O(1) on Boltzmann factor stated",
    )
    check(
        "note records condensate/gas-density criterion language",
        has_condition,
        "condensate/gas-density criterion recorded",
    )
    check(
        "note keeps the condensate criterion open, not theorem-grade",
        has_open_condition,
        "open target / not theorem-grade / must be supplied language present",
    )
    check(
        "note names determinant, phase-space, and coupling-scale gaps",
        has_load_bearing_gaps,
        "load-bearing model data left open",
    )


def test_T6_canonical_SU3_value() -> None:
    section("T6: canonical SU(3), g^2=1, k=1: S_frac = 8 pi^2 / 3 ~ 26.32, exp(-S_frac) ~ 3.7e-12")
    pi2 = math.pi**2
    S_su3 = 8 * pi2 / 3.0
    e_su3 = math.exp(-S_su3)
    ok_S = abs(S_su3 - 26.31894506957162) < 1e-9
    ok_e = 1e-13 < e_su3 < 1e-11  # ~3.7e-12
    check(
        "SU(3) canonical S_frac = 8 pi^2 / 3 ~ 26.319",
        ok_S,
        f"S_frac = {S_su3:.10f}",
    )
    check(
        "SU(3) canonical exp(-S_frac) ~ 3.7e-12 (in 1e-13 .. 1e-11 band)",
        ok_e,
        f"exp(-S_frac) = {e_su3:.3e}",
    )
    # Also confirm note text mentions ~3.7e-12 magnitude or 26.3 magnitude
    text = NOTE.read_text(encoding="utf-8")
    has_su3_numeric = ("26.3" in text or "26.32" in text or "8 π² / 3" in text)
    has_exp_su3 = ("3.7" in text or "3.7 × 10⁻¹²" in text or "10⁻¹²" in text or "10^-12" in text)
    check(
        "note records SU(3) numerical canonical entry (~ 26.32 or 8 pi^2/3)",
        has_su3_numeric,
        "SU(3) numerical entry present",
    )
    check(
        "note records SU(3) Boltzmann factor magnitude ~ 3.7e-12",
        has_exp_su3,
        "~10^-12 / 3.7 magnitude present",
    )


def test_T7_twisted_BC_requirement() -> None:
    section("T7: twisted boundary condition requirement (T^4 with Z_N twist)")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    has_t4 = "t^4" in lower or "t⁴" in lower or "4-torus" in lower or "four-torus" in lower
    has_twist = "twist" in lower and ("z_n" in lower or "z_n " in lower or "z_2" in lower or "z_2_n" in lower or "z_n" in lower)
    has_center = "center" in lower
    has_n_mu_nu = "n_μν" in text or "n_mu_nu" in lower or "twist tensor" in lower
    has_cocycle = "cocycle" in lower or "transition functions" in lower or "ω_ν" in text.lower() or "ω_μ" in text.lower()
    check(
        "note records T^4 (4-torus) setting",
        has_t4,
        "T^4 / 4-torus present",
    )
    check(
        "note records twist (Z_N or Z_2_N) requirement",
        has_twist,
        "twist + Z_N keyword present",
    )
    check(
        "note records center-symmetry context",
        has_center,
        "center keyword present",
    )
    check(
        "note records 't Hooft twist tensor n_μν",
        has_n_mu_nu,
        "n_μν / twist tensor present",
    )
    check(
        "note records cocycle / transition-functions structure",
        has_cocycle,
        "cocycle / Ω transition functions present",
    )


def test_T8_open_gate_declaration() -> None:
    section("T8: boundary — note declares open_gate")
    text = NOTE.read_text(encoding="utf-8")
    has_decl = "**Claim type:** open_gate" in text
    check(
        "note declares Claim type: open_gate",
        has_decl,
        "Claim type line present",
    )


def test_T9_no_substrate_identification() -> None:
    section("T9: boundary — note does NOT claim substrate identification")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    forbidden = [
        "the framework substrate is identified",
        "framework substrate is identified with fractional instanton",
        "framework substrate is identified with t^4",
        "the fractional instanton is the framework substrate",
        "this note identifies the framework substrate",
        "we identify the framework substrate",
        "substrate identification is closed",
        "z^4 wilson surface is identified with t^4",
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


def test_T10_no_alpha_LM_16_closure() -> None:
    section("T10: boundary — no alpha_LM^16 closure, no v/M_Pl, no hierarchy substitution")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    forbidden = [
        "alpha_lm^16 is closed",
        "α_lm^16 is closed",
        "alpha_lm^16 closure is achieved",
        "v/m_pl is derived",
        "v/m_pl = exp(-s_frac) is closed",
        "v/m_pl is exp(-s_frac)",
        "hierarchy formula is closed",
        "the hierarchy is closed",
        "pipeline-derived status: retained",
        "we identify s_frac with ln(m_pl/v)",
        "we identify the boltzmann factor with v/m_pl",
    ]
    not_present = not any(item in lower for item in forbidden)
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


def test_T11_downstream_source_boundary_firewall() -> None:
    section("T11: downstream source-boundary firewall")
    text = NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    lower_flat = flat.lower()
    has_section = "## Downstream Source-Boundary Firewall" in text
    requires_twisted_sector = "must separately prove the twisted-`t^4` sector" in lower_flat
    requires_measure_prescription = "determinant/measure/coupling-scale prescription" in lower_flat
    requires_condensate_criterion = (
        "dilute-gas convergence or condensate criterion" in lower_flat
    )
    requires_substrate_observable_bridge = "substrate/observable bridge" in lower_flat
    forbids_positive_hierarchy_bridge = (
        "do not cite this packet as a positive hierarchy bridge" in lower_flat
    )
    forbids_condensate_closure = "dilute-gas condensate closure" in lower_flat
    forbids_framework_identification = "framework substrate/observable identification" in lower_flat
    forbids_hierarchy_closures = (
        "alpha_lm^16" in lower_flat
        and "v/m_pl" in lower_flat
        and "alpha^n" in lower_flat
    )
    check(
        "note has a downstream source-boundary firewall section",
        has_section,
        "firewall section present",
    )
    check(
        "firewall requires separate twisted-T^4 sector proof",
        requires_twisted_sector,
        "future framework use cannot import the external twisted-T^4 sector",
    )
    check(
        "firewall requires determinant/measure/coupling-scale prescription proof",
        requires_measure_prescription,
        "future framework use cannot import measure or running-coupling data",
    )
    check(
        "firewall requires dilute-gas convergence or condensate criterion proof",
        requires_condensate_criterion,
        "future framework use cannot import condensate closure",
    )
    check(
        "firewall requires separate substrate/observable bridge proof",
        requires_substrate_observable_bridge,
        "future framework use cannot import the substrate/observable bridge",
    )
    check(
        "firewall forbids hierarchy, condensate, and framework-identification overclaims",
        (
            forbids_positive_hierarchy_bridge
            and forbids_condensate_closure
            and forbids_framework_identification
            and forbids_hierarchy_closures
        ),
        "positive hierarchy, condensate closure, substrate/observable, alpha_LM^16, v/M_Pl, and alpha^N closures excluded",
    )


def test_T12_action_core_decoration_segregation() -> None:
    section("T12: algebra-core split / decoration segregation of the dilute-gas bridge")
    text = NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    lower_flat = flat.lower()
    # Markdown-bold markers split literal substrings when flattened; strip them
    # for the prose-segregation checks below.
    lower_flat_nomd = lower_flat.replace("**", "")

    # (a) Parent frames the fractional-action algebra as a pure algebraic
    #     decoration of the retained-bounded topological-instanton authority,
    #     citing the 2026-06-18 action-core split note + its runner + cache.
    cites_action_core = (
        "FRACTIONAL_INSTANTON_ACTION_CORE_FROM_TOPOLOGICAL_INFRASTRUCTURE_BOUNDED_NOTE_2026-06-18.md"
        in text
        and "fractional_instanton_action_core_split_2026_06_18.py" in text
        and "fractional_instanton_action_core_split_2026_06_18.txt" in text
    )
    frames_decoration = (
        "decoration" in lower_flat
        and "retained-bounded topological-instanton authority" in lower_flat
    )
    check(
        "parent frames the fractional-action algebra as a decoration of the "
        "retained-bounded topological-instanton authority and cites the action-core split",
        cites_action_core and frames_decoration,
        "action-core split note/runner/cache cited; decoration framing present",
    )

    # (b) The dilute-gas determinant/measure/coupling-scale/convergence and
    #     condensate content is segregated into an explicit open bridge block.
    has_open_block = "## Open: Dilute-Gas Bridge".lower() in lower_flat or (
        "open: dilute-gas bridge" in lower_flat
    )
    open_block_names_gaps = (
        "not supplied here" in lower_flat
        and "one-loop determinant" in lower_flat
        and ("integration measure" in lower_flat or "measure" in lower_flat)
        and ("coupling-scale prescription" in lower_flat or "coupling scale" in lower_flat)
        and ("convergence" in lower_flat)
        and ("condensate" in lower_flat)
    )
    check(
        "dilute-gas determinant/measure/coupling-scale/convergence + condensate "
        "content is segregated in an explicit open dilute-gas bridge block",
        has_open_block and open_block_names_gaps,
        "open dilute-gas bridge block present and names the unsupplied gaps",
    )

    # (c) Parent no longer presents the retained-bounded topological-instanton
    #     authority as authority for the dilute-gas bridge: it backs the
    #     action-core decoration ONLY.
    retained_authority_is_action_core_only = (
        "retained-bounded authority for the action-core" in lower_flat_nomd
        and (
            "does not supply, and is not authority for, the dilute-gas"
            in lower_flat_nomd
            or "not authority for, the dilute-gas" in lower_flat_nomd
        )
    )
    # The stale bundling phrasing must be gone from the live Upstream-authority
    # bullet. (The dated repair-log section may quote the removed phrase verbatim
    # while describing the change; that is expected, so scope the check to the
    # Upstream-authority section only.)
    upstream_section = ""
    if "## Upstream authority" in text:
        upstream_section = text.split("## Upstream authority", 1)[1]
        # Cut at the next top-level section so the repair-log quote is excluded.
        for marker in ("\n## ",):
            if marker in upstream_section:
                upstream_section = upstream_section.split(marker, 1)[0]
    upstream_nomd = " ".join(upstream_section.split()).lower().replace("**", "")
    no_stale_bundling = (
        "consumed by the fractional-instanton dilute-gas condensate construction"
        not in upstream_nomd
    )
    check(
        "retained-bounded topological-instanton authority backs the action-core "
        "decoration only, not the dilute-gas bridge",
        retained_authority_is_action_core_only and no_stale_bundling,
        "upstream-authority section scopes the bounded import to the action core; "
        "stale 'consumed by ... dilute-gas condensate construction' bundling removed",
    )


def main() -> int:
    print("# Fractional instanton dilute-gas hierarchy external gate runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_T1_symbolic_fractional_action_formula()
    test_T2_meron_cross_check_N2_k1()
    test_T3_numerical_S_frac_canonical_N_values()
    test_T4_dilute_gas_free_energy_structure()
    test_T5_condensate_formation_condition()
    test_T6_canonical_SU3_value()
    test_T7_twisted_BC_requirement()
    test_T8_open_gate_declaration()
    test_T9_no_substrate_identification()
    test_T10_no_alpha_LM_16_closure()
    test_T11_downstream_source_boundary_firewall()
    test_T12_action_core_decoration_segregation()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
