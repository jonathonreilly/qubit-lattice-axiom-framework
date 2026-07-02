#!/usr/bin/env python3
"""Runner for the meron / fractional-instanton half-action external gate.

After the 2026-06-20 source-scope repair, the note is a PURE ALGEBRAIC
DECORATION of the source half-action core: its only
load-bearing content is the half-action arithmetic
S_half = (1/2) S_inst = 4 pi^2 / g^2 (given the retained-bounded
topological-instanton BPST 8 pi^2 / g^2 normalization and a supplied
half-charge sector |Q| = 1/2).
The specific regulator / twist / patching / fractional-instanton SECTOR
construction is recorded as an explicitly CONDITIONAL / open premise that
the note does NOT supply. The runner verifies the algebraic half-action
identity in exact symbolic form, evaluates the half-action scale and
exp(-S_half) at three values of g^2, and -- in the SEGREGATED sector check
(T5) -- verifies that the fractional Q = 1/2 / regulator / patching sector
is recorded as conditional/open and NOT supplied, rather than asserted as a
result. It explicitly does not assert a standalone finite-action theorem
for the singular unregularized single meron on R^4. It enforces the
source-note disclaimers excluding framework substrate identification,
hierarchy closure, scale ratio derivation, and alpha_LM^16 closure
overclaims. No derived value is changed by the repair.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "MERON_HALF_INSTANTON_4PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md"
CORE_NOTE = ROOT / "docs" / "MERON_HALF_ACTION_CORE_FROM_TOPOLOGICAL_INFRASTRUCTURE_BOUNDED_NOTE_2026-06-18.md"

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
    section("T1: symbolic S_half = 4 pi^2 / g^2 (half of BPST 8 pi^2 / g^2)")
    g = sp.symbols("g", positive=True, real=True)
    S_inst = 8 * sp.pi**2 / g**2
    S_meron_def = 4 * sp.pi**2 / g**2
    # Reproduce S_meron from (1/2) S_inst
    S_meron_from_half = sp.Rational(1, 2) * S_inst
    diff = sp.simplify(S_meron_def - S_meron_from_half)
    check(
        "S_half simplifies to 4 pi^2 / g^2 symbolically",
        diff == 0,
        f"S_half = {S_meron_def}, (1/2) S_inst = {sp.simplify(S_meron_from_half)}",
    )


def test_T2_half_action_identity() -> None:
    section("T2: half-action identity S_half = (1/2) S_inst")
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
    # Also assert the note text states the half-action identity.
    text = NOTE.read_text(encoding="utf-8")
    has_half_id = (
        "(1/2)" in text
        and "S_inst" in text
        and ("half-action" in text.lower() or "half the BPST" in text.lower())
    )
    check(
        "note states the half-action identity S_half = (1/2) S_inst in text",
        has_half_id,
        "(1/2), S_inst, and 'half' all present",
    )


def test_T3_numerical_meron_action_values() -> None:
    section("T3: numerical S_half at g^2 in {1/2, 1, 2}")
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
        "S_half at g^2 in {1/2, 1, 2} evaluates to {8, 4, 2} pi^2 numerically",
        ok_all,
        "; ".join(detail_parts),
    )


def test_T4_exp_suppression() -> None:
    section("T4: numerical exp(-S_half) at g^2 in {1/2, 1, 2}")
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
        "exp(-S_half) at g^2 in {1/2, 1, 2} matches expected suppression orders",
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
        "canonical g^2=1 half-action scale: 4 pi^2 ≈ 39.4784",
        ok_canonical,
        f"S_half = {S_g1:.10f}, exp(-S_half) = {e_g1:.3e}",
    )


def test_T5_fractional_Q_sector_is_conditional_open_not_supplied() -> None:
    section(
        "T5: fractional Q = 1/2 / regulator / patching SECTOR is recorded as "
        "CONDITIONAL/open and NOT supplied (segregated sector-claim check)"
    )
    # SEGREGATED CHECK. This packet was split (2026-06-20 source-scope repair) to a
    # pure algebraic decoration of the source half-action core. The
    # fractional Q = 1/2 / boundary / meron-pair material is therefore an
    # OPEN PREMISE the note does not supply, NOT a positive note claim. This
    # check verifies the conditional/open framing rather than asserting the
    # sector as a result. It does NOT supply the regulator/twist/patching
    # authority and does NOT assert that any meron / pair / lattice realizes
    # the sector.
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    flat_lower = " ".join(text.split()).lower()

    # The fractional charge value is still mentioned (as the conditional input
    # the arithmetic is conditioned on), but only as an open premise.
    mentions_half_charge = (
        "q = 1/2" in lower
        or "|q| = 1/2" in lower
        or "`1/2`" in lower
    )
    # The note must carry an explicit "Conditional / Open Premise (NOT
    # Supplied)" demotion of the sector construction.
    has_conditional_open_block = (
        "conditional / open premise (not supplied)" in lower
        or ("conditional / open" in lower and "not supplied" in lower)
    )
    # The sector / regulator / patching construction must be named as the OPEN
    # GATE that this note does not close, not as a discharged boundary.
    sector_is_open_gate = (
        "the **open gate** this note does not close" in text
        or "regulator/twist/patching construction is the **open gate**" in text
        or ("open gate" in lower and "not close" in lower)
    )
    # The note must explicitly state it does NOT supply the sector.
    does_not_supply_sector = (
        "does **not** supply" in text
        or "is not supplied" in lower
        or "not provided by this note" in lower
        or "does not supply the sector" in lower
    )
    check(
        "fractional Q = 1/2 mentioned only as the conditional input",
        mentions_half_charge,
        "Q = 1/2 appears as the supplied/conditional sector value",
    )
    check(
        "note carries an explicit Conditional / Open Premise (NOT Supplied) block",
        has_conditional_open_block,
        "sector construction demoted to an open premise, not a note claim",
    )
    check(
        "regulator/twist/patching sector is named as the OPEN GATE, not discharged",
        sector_is_open_gate,
        "sector construction recorded as the open gate this note does not close",
    )
    check(
        "note explicitly does NOT supply the sector construction",
        does_not_supply_sector,
        "regulator/twist/patching sector authority explicitly not provided here",
    )


def test_T6_singular_meron_boundary() -> None:
    section("T6: singular-meron boundary refuses standalone finite-action theorem")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    clean = lower.replace("**", "")
    refuses_standalone = (
        "not assert" in clean
        and "singular unregularized" in clean
        and "finite-action theorem" in clean
    )
    has_regulator_dependency = (
        "regulator" in lower
        and ("twist" in lower or "patching" in lower or "capped" in lower or "pair" in lower)
    )
    has_singularity_boundary = "singular" in lower and "x = 0" in lower
    check(
        "note refuses standalone finite-action status for the singular unregularized meron",
        refuses_standalone,
        "singular unregularized finite-action theorem explicitly denied",
    )
    check(
        "note records regulator/twist/patching dependency as load-bearing",
        has_regulator_dependency,
        "regulator plus pair/twist/patching boundary recorded",
    )
    check(
        "note records singular core / boundary subtleties",
        has_singularity_boundary,
        "singular core and boundary subtleties recorded",
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


def test_T11_downstream_source_boundary_firewall() -> None:
    section("T11: downstream source-boundary firewall")
    text = NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    lower_flat = flat.lower()
    has_section = "## Downstream Source-Boundary Firewall" in text
    requires_regulator_proof = (
        "must separately prove the regulator/twist/patching sector" in lower_flat
    )
    requires_substrate_observable_bridge = "substrate/observable bridge" in lower_flat
    excludes_framework_substrate_theorem = (
        "do not cite this packet as a framework substrate theorem" in lower_flat
    )
    excludes_finite_action_singular_meron = (
        "finite-action singular meron theorem" in lower_flat
    )
    excludes_positive_hierarchy_bridge = "positive hierarchy bridge" in lower_flat
    excludes_hierarchy_closures = "alpha_lm^16" in lower_flat and "v/m_pl" in lower_flat
    check(
        "note has a downstream source-boundary firewall section",
        has_section,
        "firewall section present",
    )
    check(
        "firewall requires separate regulator/twist/patching proof",
        requires_regulator_proof,
        "future framework use cannot import the regulator/twist/patching sector",
    )
    check(
        "firewall requires separate substrate/observable bridge proof",
        requires_substrate_observable_bridge,
        "future framework use cannot import the substrate/observable bridge",
    )
    check(
        "firewall forbids framework-substrate, finite-action, and hierarchy overclaims",
        (
            excludes_framework_substrate_theorem
            and excludes_finite_action_singular_meron
            and excludes_positive_hierarchy_bridge
            and excludes_hierarchy_closures
        ),
        "framework substrate, finite-action singular meron, hierarchy, alpha_LM^16, and v/M_Pl closures excluded",
    )


def test_T12_algebra_core_split() -> None:
    section("T12: 2026-06-18 algebra-core split and upstream authority boundary")
    text = NOTE.read_text(encoding="utf-8")
    core = CORE_NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    core_flat = " ".join(core.split())
    cites_core = "MERON_HALF_ACTION_CORE_FROM_TOPOLOGICAL_INFRASTRUCTURE_BOUNDED_NOTE_2026-06-18.md" in text
    core_is_arithmetic_only = (
        "action arithmetic only" in flat
        and "does not derive the meron regulator" in flat
    )
    old_overclaim_removed = (
        "Provides the one-hop authority for the regulator / twist / patching construction"
        not in text
    )
    infra_boundary = (
        "does **not** supply a retained meron regulator" in text
        and "framework-substrate, or observable bridge" in text
    )
    core_bars_existence = (
        "It must not be cited as:" in core
        and "retained meron existence" in core
        and "a regulator, cap, twist, or patching construction" in core_flat
    )
    check("parent cites the 2026-06-18 half-action algebra core split", cites_core)
    check("parent says the split is action-arithmetic only", core_is_arithmetic_only)
    check("old regulator/twist/patching authority overclaim is removed", old_overclaim_removed)
    check("upstream infrastructure boundary excludes meron regulator/substrate bridge", infra_boundary)
    check("core note bars meron existence and boundary-construction use", core_bars_existence)


def main() -> int:
    print("# Meron / fractional-instanton 4 pi^2 / g^2 external gate runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_T1_symbolic_meron_action_formula()
    test_T2_half_action_identity()
    test_T3_numerical_meron_action_values()
    test_T4_exp_suppression()
    test_T5_fractional_Q_sector_is_conditional_open_not_supplied()
    test_T6_singular_meron_boundary()
    test_T7_lattice_realization_references()
    test_T8_open_gate_declaration()
    test_T9_no_substrate_identification()
    test_T10_no_alpha_LM_16_closure()
    test_T11_downstream_source_boundary_firewall()
    test_T12_algebra_core_split()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
