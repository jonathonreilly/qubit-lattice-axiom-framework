#!/usr/bin/env python3
"""Verifier for the minimal operational primitive update recommendation."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def flat(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    print("=== Minimal operational primitive update recommendation ===")

    files = [
        "docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/OPERATIONAL_PREMISE_GAP_MAP_2026-07-01.md",
        "docs/ACPHILAMBDA_PHASE_DEFECT_READOUT_NORMAL_FORM_2026-07-01.md",
        "docs/LOCAL_RECORD_EXTENSION_KERNEL_NORMAL_FORM_2026-06-30.md",
        "docs/SOURCE_ACTION_RN_FACTORIZATION_FROM_RECORD_BORN_INTERFACE_2026-06-30.md",
        "docs/THETA_POINTWISE_SECTOR_WEIGHT_SELECTOR_2026-07-01.md",
        "docs/EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md",
        "docs/OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    ]
    for rel in files:
        check(f"{rel} exists", exists(rel))

    note = read("docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md")
    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    registry = read("docs/audit/data/axiom_premise_nodes.json")
    gap = read("docs/OPERATIONAL_PREMISE_GAP_MAP_2026-07-01.md")
    readout = read("docs/ACPHILAMBDA_PHASE_DEFECT_READOUT_NORMAL_FORM_2026-07-01.md")
    occurrence = read("docs/LOCAL_RECORD_EXTENSION_KERNEL_NORMAL_FORM_2026-06-30.md")
    source = read("docs/SOURCE_ACTION_RN_FACTORIZATION_FROM_RECORD_BORN_INTERFACE_2026-06-30.md")
    theta = read("docs/THETA_POINTWISE_SECTOR_WEIGHT_SELECTOR_2026-07-01.md")
    metric = read("docs/EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md")
    scalar_no_go = read("docs/OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md")
    scale = read("docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md")
    flat_note = flat(note)

    print("\nPART A -- axiom and registry boundary")
    flat_axioms = flat(axioms)
    flat_scale = flat(scale)
    check("note declares no registry/axiom edit", "does not set an audit verdict, edit registries, register primitives, change axioms" in flat_note)
    check("note keeps four ontology axioms", "Lattice" in note and "Qubit / Local Possibility" in note and "Admissibility / Local Constraint" in note and "Record" in note)
    check("axioms supply current ontology", "Physical sites are" in axioms and "domain of local possibilities" in axioms and "invariant under repeated readout" in axioms)
    check("axioms keep downstream structures out", "Further physical structure requires" in flat_axioms)
    check("registry has approved minimal axioms", '"minimal_axioms"' in registry)
    check("registry has scale primitive separate", '"scale_reference_primitive"' in registry)
    check("scale primitive says units only", "units conversion" in flat_scale and "zero dimensionless content" in flat_scale)
    check("note says no broad dynamics axiom", "not another \"dynamics\" axiom" in note)

    print("\nPART B -- candidate primitive set")
    candidates = [
        "P_readout_selection",
        "P_record_extension",
        "P_physical_source",
        "P_gauge_sector_measure",
        "P_metric_observable",
    ]
    for candidate in candidates:
        check(f"candidate present: {candidate}", candidate in note)
    headings = [
        "Physical Readout Selection",
        "Record Extension / Occurrence",
        "Physical Source Selector",
        "Gauge-Sector Measure",
        "Metric / Observable Bridge",
    ]
    for heading in headings:
        check(f"heading present: {heading}", f"###" in note and heading in note)
    check("note says candidates are fallback only", "fallback primitive candidates" in note)
    check("note says bridge-first should continue", "Bridge-first work should continue" in note)
    check("note says not primitive registrations", "not primitive registrations in this note" in flat_note)

    print("\nPART C -- candidate wording checks")
    required_phrases = [
        "local covariant map from specified record/context invariants",
        "does not say every invariant is readable",
        "never overwrites records",
        "never locks unavailable possibilities",
        "does not force every site to record",
        "physical action-exponent direction and unit",
        "pointwise record-facing sector measure",
        "joint gauge/mass invariant angle",
        "clock-rate/conformal factor",
        "does not turn every scalar record into a measured observable",
    ]
    for phrase in required_phrases:
        check(f"wording contains: {phrase}", phrase in flat_note)
    check("charged-lepton first target names selected C3 edge defect", "selected C3 edge defect" in note)
    check("readout effect composes with phase-defect normal form", "phase-defect normal form" in note and "2/9" in note)
    check("source effect composes with RN factorization", "source/action RN factorization" in note)
    check("theta effect composes with theta selector", "theta pointwise sector selector" in note)
    check("metric effect composes with conformal class/source response", "conformal-class / source-response" in note)

    print("\nPART D -- evidence matching")
    check("gap map names W_readout_coupling", "W_readout_coupling" in gap)
    check("gap map names W_occurrence", "W_occurrence" in gap)
    check("gap map names W_physical_source", "W_physical_source" in gap)
    check("gap map names W_theta_sector", "W_theta_sector" in gap)
    check("gap map names W_metric_observable", "W_metric_observable" in gap)
    check("readout note names W_defect_readout_selection", "W_defect_readout_selection" in readout)
    check("occurrence note names physical kernel/generator remains", "physical kernel" in occurrence and "a clock or rate" in occurrence)
    check("source note names physical source direction and unit", "physical source direction and unit" in source)
    check("theta note names emergent Q and sector measure", "emergent integer Q" in theta and "pointwise nonnegative" in theta)
    check("metric note names conformal factor clock rate", "conformal factor" in metric and "clock rate" in metric)
    check("record scalar no-go says Record does not choose scalar map", "Record additivity alone" in scalar_no_go and "branch-to-scalar" in scalar_no_go)

    print("\nPART E -- priority and governance")
    for i, heading in enumerate(headings, start=1):
        check(f"priority item {i} present", f"{i}. **{heading.split(' / ')[0]}" in note or f"{i}. **{heading}" in note)
    governance_phrases = [
        "exact primitive wording",
        "explicit boundaries",
        "a source note",
        "a verifier",
        "registry entry in `docs/audit/data/axiom_premise_nodes.json`",
        "no change to the four ontology axioms",
        "downstream claims must treat these as open bridge targets",
    ]
    for phrase in governance_phrases:
        check(f"governance phrase present: {phrase}", phrase in note)

    print("\nPART F -- no-go discipline N1-N8")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", f"### {item}" in note)
    routes = [
        "More-ontology route",
        "Readout-selection route",
        "Occurrence route",
        "Source route",
        "Theta route",
        "Metric/observable route",
        "New primitive route",
    ]
    for route in routes:
        check(f"N1 route present: {route}", route in note)
    check("N2 collapsed wall set includes all candidates", all(candidate in note for candidate in candidates))
    check("N3 classifies primitive as future approved", "future approved framework primitive" in note)
    check("N4 witness table covers readout", "ACPHILAMBDA_PHASE_DEFECT_READOUT_NORMAL_FORM" in note)
    check("N4 witness table covers occurrence", "LOCAL_RECORD_EXTENSION_KERNEL_NORMAL_FORM" in note)
    check("N4 witness table covers source", "SOURCE_ACTION_RN_FACTORIZATION" in note)
    check("N4 witness table covers theta", "THETA_POINTWISE_SECTOR_WEIGHT_SELECTOR" in note)
    check("N4 witness table covers metric", "EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS" in note)
    check("N5 avoids cannot-derive overclaim", "bridge derivations are impossible" in note)
    check("N6 names five bridge-first paths", note.count("derive ") >= 5 and "If any path closes" in note)
    check("N7 steelman accepts single future action principle", "single future local action principle" in note)
    check("N8 cross-cycle echo present", "Earlier cycles overclaimed" in note)

    print("\nPART G -- non-overclaim checks")
    forbidden = [
        "these primitives are registered",
        "axioms must be changed",
        "dynamics axiom is required",
        "bridges cannot be derived",
        "full theory closure",
        "solve Strong CP",
        "AC_phi_lambda is solved",
    ]
    for phrase in forbidden:
        check(f"note avoids overclaim phrase: {phrase}", phrase not in note)
    check("note explicitly says no terminal closure", "claim terminal closure" in note)
    check("note explicitly says not premises until adopted", "not usable as premises until adopted" in flat_note)
    check("note keeps owner governance boundary", "owner governance" in note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL -- primitive update recommendation is not verifier-clean.")
        return 1
    print(
        "RESULT: PASS -- remaining gates map to narrow operational primitive "
        "candidates, not a broad ontology axiom."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
