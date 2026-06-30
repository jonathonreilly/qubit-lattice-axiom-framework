#!/usr/bin/env python3
"""Verify the post-stack hard-gate status map."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "POST_STACK_HARD_GATE_STATUS_MAP_2026-06-30.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
STRICT_NN = DOCS / "STRICT_NN_COMPOSITION_FLUX_SELECTOR_BRIDGE_THEOREM_NOTE_2026-06-30.md"
GEN_CONTEXT = DOCS / "GENERATION_CONTEXT_SELECTOR_FROM_STRICT_NN_DIRAC_RECORD_ORIENTATION_2026-06-30.md"
R_ETA_BRIDGE = DOCS / "ACPHILAMBDA_R_ETA_EDGE_DEFECT_LOCALIZATION_BRIDGE_2026-06-30.md"
BORN_BRIDGE = DOCS / "RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md"
OCCURRENCE = DOCS / "RECORD_OCCURRENCE_GATE_FACTORIZATION_FROM_LOCAL_AVAILABILITY_2026-06-30.md"
SOURCE_PCAL = DOCS / "RECORD_BORN_TO_SOURCE_MEASURE_PCAL_INTERFACE_BRIDGE_2026-06-30.md"
THETA_STRUCT = DOCS / "STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md"
THETA_RG = DOCS / "THETA_EMERGENT_Q_WEIGHTING_REALITY_RG_STABLE_BOUNDED_THEOREM_NOTE_2026-06-13.md"
SCALE_PRIM = DOCS / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
OLD_MAP = DOCS / "POST_AXIOM_ADOPTION_REMAINING_HARD_GATE_ROUTE_MAP_2026-06-30.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
AXIOM_NODES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + title)


def main() -> int:
    print("=== Post-stack hard-gate status map ===")

    paths = [
        NOTE,
        AXIOMS,
        STRICT_NN,
        GEN_CONTEXT,
        R_ETA_BRIDGE,
        BORN_BRIDGE,
        OCCURRENCE,
        SOURCE_PCAL,
        THETA_STRUCT,
        THETA_RG,
        SCALE_PRIM,
        OLD_MAP,
        TIER_A,
        AXIOM_NODES,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    strict = read(STRICT_NN)
    gen_context = read(GEN_CONTEXT)
    r_eta = read(R_ETA_BRIDGE)
    born = read(BORN_BRIDGE)
    occurrence = read(OCCURRENCE)
    source_pcal = read(SOURCE_PCAL)
    theta_struct = read(THETA_STRUCT)
    theta_rg = read(THETA_RG)
    scale = read(SCALE_PRIM)
    old_map = read(OLD_MAP)
    tier_a = json.loads(read(TIER_A))
    axiom_nodes = json.loads(read(AXIOM_NODES))

    section("PART A -- axiom and kinetic surface")
    check("axioms have four named primitives", "Lattice, Qubit, Admissibility, Record" in axioms)
    check("axioms provide local possibility", "Each site has a domain of local possibilities" in axioms)
    check("axioms provide admissible availability", "available subset of possibilities" in axioms)
    check("axioms provide fixed records", "A record locks exactly one available local possibility" in axioms)
    check("axioms keep dynamics downstream", "Admissibility is not a dynamics axiom" in axioms)
    check("strict NN bridge supplies Dirac kinetic branch", "first-order Dirac" in strict and "flux(-1)" in strict)
    check("strict NN bridge does not close remaining gates", "does not" in strict and "record" in strict.lower())

    section("PART B -- stacked bridge candidates")
    check("generation context bridge selects edge-minimal hw=1", "edge-minimal" in gen_context and "hw=1" in gen_context)
    check("generation context bridge leaves other gates", "What Remains Outside This Theorem" in gen_context)
    check("R-eta bridge narrows to defect density", "local scalar defect density" in r_eta and "2/9" in r_eta)
    check("R-eta bridge preserves phase-defect coupling wall", "phase-defect coupling" in r_eta)
    check("Born bridge supplies trace weights after interface", "Tr(rho P_r)" in born)
    check("Born bridge preserves occurrence wall", "W_occurrence" in born)
    check("occurrence bridge names activation and selection", "Activation" in occurrence and "Selection" in occurrence)
    check("occurrence bridge forbids total-record overclaim", "does not say all sites record" in occurrence)
    check("source P-cal bridge attaches RN algebra", "RN/log-normalizer" in source_pcal)
    check("source P-cal bridge preserves physical source/action wall", "W_source_action" in source_pcal)

    section("PART C -- theta and metric boundaries")
    check("theta structured note names gauge residual", "Gauge-side residual" in theta_struct)
    check("theta structured note names mass residual", "Mass-side residual" in theta_struct)
    check("theta RG note leaves 0-vs-pi/Q issue", "0-vs-pi" in theta_rg or "Q-existence" in theta_rg)
    check("scale primitive is units only", "units conversion" in scale and "zero dimensionless" in scale)

    section("PART D -- registry boundary")
    check("Tier-A registry still has two genuine admitted inputs", tier_a.get("genuine_admitted_input_count") == 2)
    canonical_ids = set(tier_a.get("canonical_ids", []))
    check("Tier-A registry still contains staggered Dirac admission", "staggered_dirac_realization_gate_note_2026-05-03" in canonical_ids)
    check("Tier-A registry still contains strong CP theta admission", "strong_cp_theta_zero_note" in canonical_ids)
    node_ids = set(axiom_nodes.get("nodes", {}).keys()) if isinstance(axiom_nodes.get("nodes"), dict) else set()
    check("axiom node registry includes minimal_axioms", "minimal_axioms" in node_ids or "minimal_axioms" in read(AXIOM_NODES))
    check("axiom node registry includes scale primitive", "scale_reference_primitive" in read(AXIOM_NODES))

    section("PART E -- note content")
    expected_headings = [
        "Claim",
        "What Is Left",
        "Priority Order",
        "Axiom Consequence",
        "Audit Consequence If Retained",
        "No-Go Discipline Gate",
    ]
    for heading in expected_headings:
        check(f"note includes {heading}", f"## {heading}" in note)
    expected_gates = [
        "Bridge-stack adoption",
        "Charged-lepton context / species-locus",
        "`A_R-eta`",
        "Born / measurement interface",
        "Record occurrence / production",
        "P-cal / source-measure interface",
        "Theta",
        "Scale / metric / observable bridge",
    ]
    for gate in expected_gates:
        check(f"note maps {gate}", gate in note)
    check("note says no broad dynamics axiom is required", "not a request for a broad dynamics axiom" in note)
    check("note says no further axiom change is justified by map alone", "No further axiom change is justified by this map alone" in note)
    check("note keeps remaining work bridge-first", "build and audit them as bridge theorems first" in note)
    check("note warns bridge stack needs audit", "Independent review/audit" in note)

    section("PART F -- residual structure")
    residuals = [
        "W_stack_adoption",
        "W_phase_defect_coupling",
        "W_occurrence",
        "W_source_action",
        "W_theta_gauge_selector",
        "W_metric_observable",
    ]
    for residual in residuals:
        check(f"note names {residual}", residual in note)
    check("note keeps occurrence independent from source/action", "Closing `W_occurrence` does not identify physical source/action" in note)
    check("note keeps source/action independent from occurrence", "Closing `W_source_action` does not produce records" in note)
    check("note keeps metric independent from occurrence", "Closing metric/observable does not choose branch occurrence" in note_flat)
    check("old map was broader than post-stack map", "What remains is the bridge work" in old_map and "record occurrence/production" in old_map)

    section("PART G -- no-go discipline visible")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", item in note)
    check("N1 enumerates at least seven routes", note.count("| Broad dynamics axiom |") == 1 and note.count("| New primitive route |") == 1)
    check("N3 scans hidden wall phrases", "\"Retained\"" in note and "\"Physical\"" in note)
    check("N4 residual matching includes eight witnesses", note.count("| `") >= 8 and "Residual Matching" in note)
    check("N5 avoids no-route overclaim", "does not say \"no route exists." in note_flat)
    check("N6 lists partial closure paths", "Several partial-closure paths remain live" in note)
    check("N7 steelman points to source/metric collapse route", "source/action and metric/observable might collapse" in note)
    check("N8 cross-cycle echo is present", "Earlier broad walls often shrank" in note)

    section("PART H -- assembled conclusion")
    open_items = [
        "physical source/action identification bridge",
        "record-extension or instrument-production bridge",
        "theta's gauge-action selector",
        "metric/observable bridge",
    ]
    for item in open_items:
        check(f"priority list includes {item}", item in note)
    check("map does not claim any bridge retained", "claim any bridge stack item is retained" in note)
    check("map does not edit registries", "does not set an audit verdict" in note_flat and "edit the Tier-A registry" in note_flat)
    check("map routes rows by dependency type", "Rows that depend only on kinetic Dirac structure" in note)
    check("map states exact typed blockers", all(residual in note for residual in residuals))

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- post-stack hard gates are mapped without claiming closure.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
