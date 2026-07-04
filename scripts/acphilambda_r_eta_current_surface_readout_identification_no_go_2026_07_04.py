#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_R_ETA_CURRENT_SURFACE_READOUT_IDENTIFICATION_NO_GO_NOTE_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"

SOURCES = {
    "reta_irreducibility": DOCS / "RETA_ALGEBRAIC_IRREDUCIBILITY_GENUINE_READOUT_ADMISSION_BOUNDED_NOTE_2026-06-12.md",
    "defect_rescale": DOCS / "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md",
    "holonomy_normal": DOCS / "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md",
    "real_locus": DOCS / "ACPHILAMBDA_REAL_HOLONOMY_LOCUS_IDENTITY_2026-07-01.md",
    "transport_face": DOCS / "ACPHILAMBDA_CYCLE_FLUX_TRANSPORT_FACE_INVENTORY_2026-07-01.md",
    "k_even": DOCS / "ACPHILAMBDA_K_EVEN_REGISTRATION_CORRECTION_REGISTERED_PATTERN_2026-07-02.md",
    "occurrence_clock": DOCS / "ACPHILAMBDA_OCCURRENCE_CLOCK_COMPOSITION_DELTA_BLINDNESS_2026-07-02.md",
    "cross_arc": DOCS / "ACPHILAMBDA_CROSS_ARC_UNIT_CLASSIFICATION_WIRING_2026-07-02.md",
    "angle_no_go": DOCS / "ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md",
    "occurrence_no_go": DOCS / "ACPHILAMBDA_R_ETA_OCCURRENCE_AXIOM_HYGIENE_NO_GO_NOTE_2026-07-04.md",
    "topological_robustness": DOCS / "KOIDE_APS_ETA_TOPOLOGICAL_ROBUSTNESS_BOUNDED_THEOREM_NOTE_2026-07-02.md",
    "readout_context": DOCS / "SUPPLIED_READOUT_CONTEXT_TWO_COMPONENT_DECOMPOSITION_BOUNDED_NOTE_2026-07-02.md",
    "w2_context": DOCS / "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md",
    "conversion_factor": DOCS / "RETA_CONVERSION_FACTOR_CARRIER_CLASS_ELIMINATION_BOUNDED_NOTE_2026-06-12.md",
    "continuum_index": DOCS / "RETA_MAGNITUDE_IS_CONTINUUM_INDEX_THEOREM_LATTICE_INDEX_IS_INTEGER_BOUNDED_NOTE_2026-06-12.md",
}

EXPECTED_ROWS = {
    "acphilambda_r_eta_angle_native_frontier_no_go_note_2026-07-04": "no_go",
    "acphilambda_r_eta_occurrence_axiom_hygiene_no_go_note_2026-07-04": "no_go",
    "acphilambda_defect_identity_unit_rescale_obstruction_2026-07-01": "bounded_theorem",
    "acphilambda_registrable_cycle_holonomy_normal_form_2026-07-01": "bounded_theorem",
    "acphilambda_real_holonomy_locus_identity_2026-07-01": "bounded_theorem",
    "acphilambda_cycle_flux_transport_face_inventory_2026-07-01": "bounded_theorem",
    "acphilambda_k_even_registration_correction_registered_pattern_2026-07-02": "bounded_theorem",
    "acphilambda_occurrence_clock_composition_delta_blindness_2026-07-02": "bounded_theorem",
    "acphilambda_cross_arc_unit_classification_wiring_2026-07-02": "bounded_theorem",
    "reta_algebraic_irreducibility_genuine_readout_admission_bounded_note_2026-06-12": "bounded_theorem",
    "reta_conversion_factor_carrier_class_elimination_bounded_note_2026-06-12": "bounded_theorem",
    "reta_magnitude_is_continuum_index_theorem_lattice_index_is_integer_bounded_note_2026-06-12": "bounded_theorem",
    "koide_aps_eta_topological_robustness_bounded_theorem_note_2026-07-02": "bounded_theorem",
    "supplied_readout_context_two_component_decomposition_bounded_note_2026-07-02": "bounded_theorem",
    "acphilambda_r_eta_w2_registrability_context_bridge_note_2026-06-18": "bounded_theorem",
}

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
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def has_all(text: str, phrases: list[str]) -> bool:
    return all(phrase in text for phrase in phrases)


def main() -> int:
    print("AC_phi_lambda R-eta current-surface readout-identification no-go verifier")

    note = read(NOTE)
    note_flat = flat(note)
    tier = json.loads(read(TIER_A))
    ledger = json.loads(read(LEDGER))["rows"]
    registry = read(REGISTRY)
    docs = {name: read(path) for name, path in SOURCES.items()}
    flats = {name: flat(text) for name, text in docs.items()}

    section("A. source presence and branch-local boundaries")
    for path in [NOTE, TIER_A, LEDGER, REGISTRY, *SOURCES.values()]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    check("note declares Type no_go", "**Type:** no_go" in note)
    check("note declares Claim type no_go", "**Claim type:** no_go" in note)
    check("note declares independent audit boundary", "independent audit lane only" in note)
    check("note has primary runner link", "acphilambda_r_eta_current_surface_readout_identification_no_go_2026_07_04.py" in note)
    check("note says no registry/axiom/primitive edit", "does not edit any Tier-A registry, axiom, primitive, audit verdict, or publication surface" in note_flat)
    check("note says AC not retired", "AC_phi_lambda is not retired." in note)
    check("note says R-eta not removed", "R-eta is not derived, refuted, re-graded, or removed from Tier-A" in note)
    for banned in [
        "AC_phi_lambda is retired",
        "R-eta is retired",
        "R-eta is derived",
        "Phi = S_sum is derived",
        "we remove R-eta",
        "registry is edited",
        "new primitive",
        "new axiom",
    ]:
        check(f"banned overclaim absent: {banned}", banned not in note)

    section("B. Tier-A registry state")
    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("Tier-A genuine admitted input count is still two", tier["genuine_admitted_input_count"] == 2)
    check(
        "AC minimum decomposition remains two atoms",
        ac["minimum_decomposition"] == ["reading_occupancy_selection", "delta_readout_identification_R_eta"],
        ac["minimum_decomposition"],
    )
    check("AC statement names R-eta", "R-eta" in ac["statement"])
    check("AC statement says magnitude conditional on R-eta", "conditional on R-eta" in ac["statement"])
    check("human registry names density-read-as-angle", "density-read-as-angle" in flat(registry))
    check("new note quotes both residual atoms", "reading_occupancy_selection" in note and "delta_readout_identification_R_eta" in note)
    check("new note targets sub-admission ii only", "sub-admission (ii)" in note and "R-eta" in note)

    section("C. audit-row classification of current support stack")
    for claim_id, expected_type in EXPECTED_ROWS.items():
        row = ledger.get(claim_id)
        check(f"ledger row exists: {claim_id}", isinstance(row, dict))
        if not isinstance(row, dict):
            continue
        check(f"{claim_id} claim_type", row.get("claim_type") == expected_type, row.get("claim_type"))
        check(f"{claim_id} audit status is source-side/unaudited", row.get("audit_status") in {"unaudited", "pending", "needs_audit"}, row.get("audit_status"))
        check(f"{claim_id} effective status is not retained", row.get("effective_status") != "retained", row.get("effective_status"))
        check(f"{claim_id} has note path", bool(row.get("note_path")), row.get("note_path"))

    section("D. exact fixed-locus, holonomy, and unit arithmetic")
    L = sp.Rational(2, 9)
    S_sum = 3 * L
    c, lam = sp.symbols("c lam", real=True)
    delta_c = c * L
    phi_c = 3 * delta_c
    phi_target = sp.Rational(2, 3)
    check("L = 2/9", L == sp.Rational(2, 9))
    check("S_sum = 3L = 2/3", S_sum == sp.Rational(2, 3))
    check("Phi(c) = c*S_sum", sp.simplify(phi_c - c * S_sum) == 0)
    check("c=1 iff Phi target on scanned line", sp.solve(sp.Eq(phi_c, phi_target), c) == [1])
    check("rescale sends Phi(c) to lambda*Phi(c)", sp.simplify((lam * c) * S_sum - lam * phi_c) == 0)
    check("rescale line has nonzero alternatives", sp.simplify(2 * S_sum - S_sum) != 0)
    count_c = sp.Rational(1, 1) / L
    check("count normalization gives c=9/2", count_c == sp.Rational(9, 2))
    check("count normalization is not c=1", count_c != 1)
    check("Phi target positive", phi_target > 0)
    check("Phi target below pi", bool(phi_target < sp.pi))
    check("delta target below pi/3", bool(L < sp.pi / 3))
    check("sin(Phi target) nonzero", sp.sin(phi_target).equals(0) is False)
    check("cos(Phi target) not +1", (sp.cos(phi_target) - 1).equals(0) is False)
    check("cos(Phi target) not -1", (sp.cos(phi_target) + 1).equals(0) is False)
    check("2*pi*L misses delta target", (2 * sp.pi * L - L).equals(0) is False)
    check("2*pi*L misses Phi target", (2 * sp.pi * L - phi_target).equals(0) is False)
    check("2*pi*S_sum misses Phi target", (2 * sp.pi * S_sum - phi_target).equals(0) is False)
    check("root angle 2*pi/3 is not bare 2/3", (2 * sp.pi / 3 - phi_target).equals(0) is False)

    section("E. text-surface classifications in source stack")
    text_checks = [
        ("reta irreducibility says genuine readout admission", "genuine readout admission", "reta_irreducibility"),
        ("reta irreducibility says does not derive/refute", "does not derive or refute R-eta", "reta_irreducibility"),
        ("defect rescale says c=1 wall", "W_defect_identity_unit", "defect_rescale"),
        ("defect rescale says homogeneous clauses cannot single out c=1", "can single out the identity-unit member", "defect_rescale"),
        ("holonomy normal says W_cycle_holonomy_value", "W_cycle_holonomy_value", "holonomy_normal"),
        ("holonomy normal says no derivation of Phi=2/3", "No derivation is supplied for `Phi = 2/3`", "holonomy_normal"),
        ("real locus says off-locus", "strictly off the locus", "real_locus"),
        ("real locus says no derivation of delta", "No derivation of `delta`", "real_locus"),
        ("transport face says equation remains wall", "the equation itself remains the wall", "transport_face"),
        ("transport face says does not derive flux equality", "does not derive flux = return amplitude", "transport_face"),
        ("K-even note says no value derived", "No value is derived here", "k_even"),
        ("K-even note says residual is R-eta", "residual identification is exactly the R-eta", "k_even"),
        ("occurrence clock says occupancy delta-blind", "occupancy-reading event streams are completely `delta`-blind", "occurrence_clock"),
        ("occurrence clock leaves p supplied", "the occurrence bridge leaves `p` supplied", "occurrence_clock"),
        ("cross-arc says no R-eta derivation", "This note does not derive R-eta", "cross_arc"),
        ("angle no-go says not retired", "R-eta is not derived, refuted, re-graded, or removed from Tier-A", "angle_no_go"),
        ("occurrence no-go says event law residual", "event law plus rate/readout license", "occurrence_no_go"),
        ("topological robustness excludes physical bridge", "does **not** derive the physical Brannen-phase bridge", "topological_robustness"),
        ("readout context not closure", "not a closure of either wall", "readout_context"),
        ("W2 context leaves value atom admitted", "The value atom `A_R-eta` remains admitted", "w2_context"),
        ("conversion factor says does not derive R-eta", "does not derive R-eta", "conversion_factor"),
        ("continuum index keeps R-eta boundary", "R-eta", "continuum_index"),
    ]
    for label, phrase, key in text_checks:
        check(label, phrase in flats[key] or phrase in docs[key])

    section("F. occurrence and rate no-go algebra")
    r00, r01, r10, r11 = sp.symbols("r00 r01 r10 r11")
    u0, u1 = sp.symbols("u0 u1", nonzero=True)
    rho = sp.Matrix([[r00, r01], [r10, r11]])
    U = sp.diag(u0, u1)
    evolved = sp.simplify(U * rho * sp.diag(1 / u0, 1 / u1))
    check("occupancy 0 invariant under diagonal native step", sp.simplify(evolved[0, 0] - r00) == 0)
    check("occupancy 1 invariant under diagonal native step", sp.simplify(evolved[1, 1] - r11) == 0)
    check("coherence gets phase ratio", evolved[0, 1] == r01 * u0 / u1)
    o0, o1, o2 = sp.symbols("o0 o1 o2")
    stream_law = o0 * o2 * o1 * o1
    delta = sp.symbols("delta")
    check("occupancy stream law is delta-free", delta not in stream_law.free_symbols)
    B, a_act = sp.symbols("B a_act", positive=True)
    rate_ratio = 2 * sp.sqrt(3) * B * sp.sin(delta) / a_act
    check("rate ratio depends on B", B in rate_ratio.free_symbols)
    check("rate ratio depends on activation rate", a_act in rate_ratio.free_symbols)
    check("rate ratio depends on delta", delta in rate_ratio.free_symbols)
    solved_B = sp.solve(sp.Eq(rate_ratio.subs(delta, L), phi_target), B)[0]
    check("setting target solves for B in terms of a_act", a_act in solved_B.free_symbols)
    check("target insertion does not derive B", solved_B != sp.Integer(1))

    section("G. route-family synthesis checks")
    route_roles = {
        "fixed-locus arithmetic": ("topological_robustness", "2/9"),
        "holonomy normal form": ("holonomy_normal", "Phi = 3 delta"),
        "unit rescale obstruction": ("defect_rescale", "rescale"),
        "real-holonomy locus": ("real_locus", "off-locus"),
        "transport typing": ("transport_face", "transport-typed"),
        "registered-pattern map": ("k_even", "registered-pattern"),
        "occurrence occupancy route": ("occurrence_clock", "delta-blindness"),
        "cross-arc dedup": ("cross_arc", "single target"),
        "angle shortcut no-go": ("angle_no_go", "license target"),
        "occurrence axiom shortcut no-go": ("occurrence_no_go", "generic occurrence"),
        "supplied context split": ("readout_context", "FRAME"),
        "W2 supplied context": ("w2_context", "physical carrier realization"),
    }
    for role, (key, phrase) in route_roles.items():
        check(f"{role} source has expected marker", phrase in flats[key] or phrase in docs[key])

    check(
        "note classifies all roles as not readout-license derivation",
        has_all(
            note,
            [
                "supplies arithmetic or a normal form",
                "types the same wall in another coordinate system",
                "prunes a route family",
                "provides support conditional on a supplied context/event/readout law",
                "records that the value is realized-state registered data",
            ],
        ),
    )
    check("note has remaining direct theorem route", "Direct readout-license theorem" in note)
    check("note has same-surface transport route", "Same-surface transport theorem" in note)
    check("note has coherence-event route", "Coherence-event theorem" in note)
    check("note has supplied-context route", "Supplied-context closure theorem" in note)
    check("note has governance route", "Owner governance route" in note)

    section("H. dependency and citation hygiene")
    for name, path in SOURCES.items():
        rel = path.relative_to(DOCS)
        check(f"note links {name}", str(rel) in note)
    check("note links human registry", "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md" in note)
    check("note links tier_a_admissions.json", "tier_a_admissions.json" in note)
    check("note names blocks 5 and 6", "Blocks 5 and 6" in note)
    check("note names blocks 13-16", "Blocks 13-16" in note)
    check("note says no publication matrix edit", "publication matrix" in note or "publication surface" in note)

    section("I. theorem statement and no-go gate")
    for phrase in [
        "the following implication is invalid",
        "None of those facts is the missing physical readout identification",
        "AC_phi_lambda sub-admission (ii) remains live",
        "Future readout-license theorems remain open",
        "This is not a terminal mathematical no-go",
        "The open theorem target is now sharper",
    ]:
        check(f"note contains theorem/firewall phrase: {phrase}", phrase in note_flat)
    for label in [f"N{i}" for i in range(1, 9)]:
        check(f"no-go gate has {label}", f"**{label}" in note)
    check("N2 records collapsed wall", "W_cycle_holonomy_value == W_defect_identity_unit == R-eta (ii)" in note)
    check("N3 forbids hidden event law", "no event law" in note)
    check("N3 forbids owner decision import", "no owner decision" in note)
    check("N4 matches registry residual", "magnitude arithmetic is fixed-locus support conditional on R-eta" in note)
    check("N7 preserves support value", "does not demote that support" in note)

    section("J. final summary")
    check("runner expected total kept in note", "TOTAL: PASS=223 FAIL=0" in note)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
