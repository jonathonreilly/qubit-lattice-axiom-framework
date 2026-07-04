#!/usr/bin/env python3
"""Verifier for the AC R-eta C3 ratification non-supply no-go."""

from __future__ import annotations

import json
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_R_ETA_C3_RATIFICATION_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
C3_CONTEXT = DOCS / "C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md"
SPECIES_RATIFICATION = DOCS / "ACPHILAMBDA_SPECIES_BRIDGE_C3_GRADE_OWNER_RATIFICATION_RETIREMENT_NOTE_2026-07-04.md"
R_ETA_NARROWING = DOCS / "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md"
R_ETA_W2 = DOCS / "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md"
R_ETA_CURRENT = DOCS / "ACPHILAMBDA_R_ETA_CURRENT_SURFACE_READOUT_IDENTIFICATION_NO_GO_NOTE_2026-07-04.md"
FIXED_LOCUS = DOCS / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 96)
    print(title)
    print("=" * 96)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def ledger_row(claim_id: str) -> dict:
    row = json.loads(read(LEDGER))["rows"].get(claim_id)
    if row is None:
        raise AssertionError(f"missing ledger row {claim_id}")
    return row


def hs_inner(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    return sp.trace(a.T * b)


def main() -> int:
    print("AC_phi_lambda R-eta C3 ratification non-supply verifier")

    paths = [
        NOTE,
        TIER_A,
        LEDGER,
        REGISTRY,
        C3_CONTEXT,
        SPECIES_RATIFICATION,
        R_ETA_NARROWING,
        R_ETA_W2,
        R_ETA_CURRENT,
        FIXED_LOCUS,
        MINIMAL,
    ]
    texts = {path: read(path) for path in paths}
    flats = {path: flat(text) for path, text in texts.items()}
    note = texts[NOTE]
    note_flat = flats[NOTE]

    section("A. source presence, metadata, and no-overclaim firewall")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    check("note has Type no_go", "**Type:** no_go" in note)
    check("note has Claim type no_go", "**Claim type:** no_go" in note)
    check("note has audit boundary", "**Audit boundary:** independent audit lane only." in note)
    check("runner link is wired", Path(__file__).name in note)
    for phrase in [
        "does not derive, refute, re-grade, retire, or remove R-eta or AC_phi_lambda",
        "does not edit any Tier-A registry",
        "No axiom, primitive, registry, audit verdict, or publication-status surface is edited.",
        "future R-eta theorem/governance routes are untouched.",
    ]:
        check(f"scope boundary present: {phrase[:64]}", phrase in note_flat)
    for banned in [
        "R-eta is retired",
        "R-eta is derived",
        "AC_phi_lambda is retired",
        "we remove R-eta",
        "the Tier-A registry is edited",
        "new R-eta primitive is approved",
    ]:
        check(f"banned overclaim absent: {banned}", banned not in note_flat)

    section("B. Tier-A registry state after July hygiene")
    tier = json.loads(read(TIER_A))
    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "AC minimum decomposition remains AC(i)+R-eta",
        ac["minimum_decomposition"] == ["reading_occupancy_selection", "delta_readout_identification_R_eta"],
        ac["minimum_decomposition"],
    )
    check("species bridge partial reclassification exists", "species_bridge_c3_grade" in ac.get("partial_reclassifications", {}))
    species_reclass = ac["partial_reclassifications"]["species_bridge_c3_grade"]
    check("species bridge reclassification source is July 4 note", species_reclass.get("source") == "docs/ACPHILAMBDA_SPECIES_BRIDGE_C3_GRADE_OWNER_RATIFICATION_RETIREMENT_NOTE_2026-07-04.md")
    check("species bridge boundary excludes AC(i)", "AC(i)" in species_reclass.get("boundary", ""))
    check("species bridge boundary excludes AC(ii)", "AC(ii)" in species_reclass.get("boundary", ""))
    check("AC statement still names R-eta", "R-eta" in ac["statement"])
    check("AC statement keeps magnitude conditional on R-eta", "conditional on R-eta" in ac["statement"])
    check("human registry says species bridge retired side record", "Retired side record" in texts[REGISTRY])
    check(
        "human registry keeps R-eta residual",
        ("R-eta" in texts[REGISTRY] or "R-η" in texts[REGISTRY])
        and "density-read-as-angle" in texts[REGISTRY],
    )

    section("C. source-surface boundary checks")
    c3 = texts[C3_CONTEXT]
    c3_flat = flats[C3_CONTEXT]
    species = texts[SPECIES_RATIFICATION]
    species_flat = flats[SPECIES_RATIFICATION]
    narrowing = texts[R_ETA_NARROWING]
    w2 = texts[R_ETA_W2]
    current = texts[R_ETA_CURRENT]
    fixed = texts[FIXED_LOCUS]
    minimal = texts[MINIMAL]

    for phrase in [
        "singlet cell",
        "doublet cell",
        "Hilbert-Schmidt normalization",
        "outcome naming",
        "channel naming",
        "Does not supply a weighting, normalization, probability rule, occupancy rule",
        "Does not select among scoring rules",
        "Does not modify any axiom or primitive",
    ]:
        check(f"C3 context boundary: {phrase[:60]}", phrase in c3_flat)
    check("C3 context does not mention R-eta", "R-eta" not in c3)
    check("C3 context does not mention density-read-as-angle", "density-read-as-angle" not in c3)
    check("C3 context does not mention fixed-locus density value", "2/9" not in c3)

    for phrase in [
        "AC_phi_lambda itself does **not** retire",
        "measure-side occupancy realization binary and R-eta readout identification remain admitted",
        "Does not retire AC_phi_lambda(i), AC_phi_lambda(ii), AC_phi_lambda as a row, or theta",
        "Does not derive a value of `r`, `delta`",
        "Does not create an approved primitive",
    ]:
        check(f"species ratification boundary: {phrase[:64]}", phrase in species_flat)

    for phrase in [
        "A_R-eta",
        "h-class",
        "h-unit",
        "remains a Tier-A admission",
        "No claim that `A_R-eta` is forced",
    ]:
        check(f"R-eta narrowing boundary: {phrase[:64]}", phrase in flats[R_ETA_NARROWING])
    check(
        "R-eta narrowing boundary: registered delta is fixed-locus density",
        "the registered |delta| IS the AB/Lefschetz fixed-locus density" in narrowing
        or (
            "the registered `|delta|` equals" in flats[R_ETA_NARROWING]
            and "Atiyah-Bott/Lefschetz fixed-locus density" in flats[R_ETA_NARROWING]
        ),
    )

    for phrase in [
        "The value atom `A_R-eta` remains admitted",
        "physical charged-lepton carrier must be shown to realize this context",
        "does not identify the R-eta value",
    ]:
        check(f"W2 context boundary: {phrase[:64]}", phrase in flats[R_ETA_W2])

    for phrase in [
        "R-eta is not derived, refuted, re-graded, or removed from Tier-A",
        "Future readout-license theorems remain open",
        "no owner decision",
        "magnitude arithmetic is fixed-locus support conditional on R-eta",
    ]:
        check(f"current R-eta no-go boundary: {phrase[:64]}", phrase in flats[R_ETA_CURRENT])

    for phrase in [
        "2/9",
        "physical single-summand readout",
        "remains a separate named open bridge",
        "This note does not touch that readout",
    ]:
        check(f"fixed-locus boundary: {phrase[:64]}", phrase in flat(fixed))
    check("fixed-locus boundary: L3(1,2)", "L3(1,2)" in fixed or "L₃(1,2)" in fixed)

    for phrase in [
        "readout-context selection",
        "physical-observable identification",
        "the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`",
    ]:
        check(f"minimal axiom keeps open: {phrase[:64]}", phrase in flat(minimal))

    section("D. ledger classifications for support rows")
    expected = {
        "c3_generation_readout_context_canonical_definition_note_2026-07-02": "meta",
        "acphilambda_species_bridge_c3_grade_owner_ratification_retirement_note_2026-07-04": "meta",
        "acphilambda_r_eta_readout_identification_narrowing_bounded_theorem_note_2026-06-11": "bounded_theorem",
        "acphilambda_r_eta_w2_registrability_context_bridge_note_2026-06-18": "bounded_theorem",
        "acphilambda_r_eta_current_surface_readout_identification_no_go_note_2026-07-04": "no_go",
        "koide_aps_c3_fixed_locus_weights_bridge_narrow_theorem_note_2026-06-05": "bounded_theorem",
    }
    for claim_id, claim_type in expected.items():
        row = ledger_row(claim_id)
        check(f"{claim_id} claim_type", row.get("claim_type") == claim_type, row.get("claim_type"))
        check(f"{claim_id} does not set retained effective status here", row.get("effective_status") != "retained" or claim_id == "koide_aps_c3_fixed_locus_weights_bridge_narrow_theorem_note_2026-06-05", row.get("effective_status"))
        check(f"{claim_id} has note path", bool(row.get("note_path")), row.get("note_path"))

    section("E. finite C3 cell algebra and independence from R-eta")
    N = 3
    I = sp.eye(N)
    J = sp.ones(N)
    B = J - I
    check("B = J - I has zero diagonal and unit off-diagonal", B == sp.Matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]]))
    check("HS norm ||I||^2 = 3", hs_inner(I, I) == 3)
    check("HS norm ||B||^2 = 6", hs_inner(B, B) == 6)
    check("HS inner <I,B> = 0", hs_inner(I, B) == 0)
    L = sp.Rational(2, 9)
    S_sum = 3 * L
    c = sp.symbols("c", real=True)
    delta_c = c * L
    phi_c = 3 * delta_c
    check("fixed-locus L = 2/9", L == sp.Rational(2, 9))
    check("S_sum = 3L = 2/3", S_sum == sp.Rational(2, 3))
    check("Phi(c) = c*S_sum", sp.simplify(phi_c - c * S_sum) == 0)
    check("c=1 gives R-eta target Phi=2/3", sp.simplify(phi_c.subs(c, 1) - sp.Rational(2, 3)) == 0)
    check("C3 cell norm ratio is not L", sp.Rational(hs_inner(I, I), hs_inner(B, B)) != L)
    check("C3 cell complement norm normalized by total is not L", sp.Rational(hs_inner(B, B), hs_inner(I, I) + hs_inner(B, B)) != L)
    check("context algebra leaves symbolic c free", c in phi_c.free_symbols)
    for value in [sp.Rational(1, 2), sp.Integer(1), sp.Rational(9, 2)]:
        check(f"alternate c={value} is algebraically allowed on line", sp.simplify(phi_c.subs(c, value) - phi_c.subs(c, 1)) != 0 or value == 1)

    section("F. note theorem and no-go discipline")
    for phrase in [
        "The implication is invalid.",
        "The canonical C3 readout context and the C3-grade species-bridge ratification do not retire R-eta.",
        "They do not supply:",
        "the density-read-as-angle / holonomy-readout identification",
        "not the C3-grade species naming bridge",
        "Direct R-eta readout-license theorem",
        "Owner governance route",
    ]:
        check(f"note contains synthesis phrase: {phrase[:64]}", phrase in note_flat)
    for idx in range(1, 9):
        check(f"N{idx} gate present", f"**N{idx}" in note)
    check("N2 separates species naming from R-eta", "species bridge is a C3-grade abstract-to-physical naming wall" in note_flat)
    check("N4 matches registry after hygiene", "`delta_readout_identification_R_eta` remains in the live minimum decomposition" in note_flat)
    check("steelman preserves support", "necessary infrastructure for R-eta" in note_flat)

    total = PASS + FAIL
    print("\n" + "=" * 96)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL} CHECKS={total}")
    print("=" * 96)
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
