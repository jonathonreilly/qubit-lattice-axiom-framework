#!/usr/bin/env python3
"""Verify the operational premise gap map."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "OPERATIONAL_PREMISE_GAP_MAP_2026-07-01.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
PRIMITIVES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
POST_STACK = DOCS / "POST_STACK_HARD_GATE_STATUS_MAP_2026-06-30.md"
AC_STACK = DOCS / "ACPHILAMBDA_STACKED_ATOM_REDUCTION_2026-07-01.md"
OCCURRENCE = DOCS / "RECORD_OCCURRENCE_GATE_FACTORIZATION_FROM_LOCAL_AVAILABILITY_2026-06-30.md"
BORN = DOCS / "RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md"
SOURCE_RN = DOCS / "SOURCE_ACTION_RN_FACTORIZATION_FROM_RECORD_BORN_INTERFACE_2026-06-30.md"
SOURCE_PCAL = DOCS / "RECORD_BORN_TO_SOURCE_MEASURE_PCAL_INTERFACE_BRIDGE_2026-06-30.md"
THETA = DOCS / "THETA_POINTWISE_SECTOR_WEIGHT_SELECTOR_2026-07-01.md"
SCALE = DOCS / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
KINETIC = DOCS / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
R_ETA = DOCS / "ACPHILAMBDA_R_ETA_EDGE_DEFECT_LOCALIZATION_BRIDGE_2026-06-30.md"
RECORD_SELECTOR = DOCS / "RECORD_SELECTOR_AUDIT_SIDECAR_2026-06-05.md"

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
    print("=== Operational premise gap map ===")

    paths = [
        NOTE,
        AXIOMS,
        PRIMITIVES,
        POST_STACK,
        AC_STACK,
        OCCURRENCE,
        BORN,
        SOURCE_RN,
        SOURCE_PCAL,
        THETA,
        SCALE,
        REALIZED,
        KINETIC,
        R_ETA,
        RECORD_SELECTOR,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    axioms_flat = flat(axioms)
    primitives = json.loads(read(PRIMITIVES))
    post_stack = read(POST_STACK)
    ac_stack = read(AC_STACK)
    occurrence = read(OCCURRENCE)
    born = read(BORN)
    source_rn = read(SOURCE_RN)
    source_pcal = read(SOURCE_PCAL)
    theta = read(THETA)
    scale = read(SCALE)
    realized = read(REALIZED)
    kinetic = read(KINETIC)
    r_eta = read(R_ETA)
    record_selector = read(RECORD_SELECTOR)

    section("PART A -- axiom and primitive boundary")
    check("axioms are current four-axiom reset", "The Four Framework Axioms" in axioms and "Admissibility / Local Constraint" in axioms)
    check("axioms supply lattice locality", "Physical sites are the points of the cubic lattice" in axioms)
    check("axioms supply local possibility", "Each site has a domain of local possibilities" in axioms)
    check("axioms supply admissible availability", "available subset of possibilities" in axioms)
    check("axioms supply fixed records", "A record locks exactly one available local possibility" in axioms)
    check("axioms keep further structure downstream", "Further physical structure requires derivation" in axioms_flat)
    check("axioms say admissibility is not dynamics", "Admissibility is not a dynamics axiom" in axioms)
    check("axioms do not supply record production", "record-production process" in axioms)

    canonical = set(primitives["canonical_ids"])
    expected_primitives = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    check("primitive registry has expected approved nodes", canonical == expected_primitives, detail=str(sorted(canonical)))
    check("scale primitive is units only", "Units conversion only" in scale or "units conversion" in scale)
    check("kinetic primitive is structural only", "carries no dimensionless dynamical content" in kinetic)
    check("realized-state primitive supplies no selector", "state-selection rule" in realized and "typical" in realized.lower())

    section("PART B -- source witness residuals")
    check("post-stack map names W_phase_defect_coupling", "W_phase_defect_coupling" in post_stack)
    check("post-stack map names W_occurrence", "W_occurrence" in post_stack)
    check("post-stack map names W_source_action", "W_source_action" in post_stack)
    check("post-stack map names W_theta_gauge_selector", "W_theta_gauge_selector" in post_stack)
    check("post-stack map names W_metric_observable", "W_metric_observable" in post_stack)
    check("AC stack collapses to W_phase_defect", "W_phase_defect" in ac_stack and "W_stack_adoption" in ac_stack)
    check("R-eta bridge names phase-defect coupling", "phase-defect coupling" in r_eta)
    check("occurrence bridge names activation and selection", "Activation" in occurrence and "Selection" in occurrence)
    check("Born bridge supplies trace weights", "Tr(rho P_r)" in born)
    check("Born bridge preserves occurrence", "W_occurrence" in born)
    check("source P-cal bridge names W_source_action", "W_source_action" in source_pcal)
    check("source RN factorization names W_physical_source", "W_physical_source" in source_rn)
    check("theta bridge names W_theta_sector", "W_theta_sector" in theta)
    check("theta bridge preserves emergent Q wall", "emergent `Q`" in theta)
    check("record selector sidecar names observable-identification bridge", "observable_identification_bridge" in record_selector)

    section("PART C -- map content")
    required_targets = [
        "W_readout_coupling",
        "W_occurrence",
        "W_physical_source",
        "W_theta_sector",
        "W_metric_observable",
    ]
    for target in required_targets:
        check(f"note names {target}", target in note)
    check("note rejects broad dynamics word", "not one broad" in note and "dynamics" in note)
    check("note says no axiom update requested", "No axiom update is requested by this map" in note)
    check("note keeps bridge-first policy", "Build bridge theorems first" in note)
    check("note says primitive registration only if bridge-first fails", "If a bridge route fails" in note)

    section("PART D -- candidate primitive shapes")
    candidate_sections = [
        "Record Extension / Occurrence",
        "Physical Readout Coupling",
        "Physical Source / Observable Selector",
        "Gauge-Sector Measure / Theta Selector",
    ]
    for section_name in candidate_sections:
        check(f"note includes candidate {section_name}", section_name in note)
    check("record-extension candidate forbids overwrites", "never overwrites records" in note)
    check("record-extension candidate forbids unavailable locks", "never locks unavailable possibilities" in note_flat)
    check("readout candidate names phase-defect target", "charged-lepton phase magnitude records the selected local C3 defect" in note_flat)
    check("source candidate names direction and unit", "direction, unit, and measured observable semantics" in note_flat)
    check("theta candidate names theta_bar", "theta_bar" in note)

    section("PART E -- collapsed residual logic")
    collapsed = {
        "W_readout_coupling",
        "W_occurrence",
        "W_physical_source",
        "W_theta_sector",
        "W_metric_observable",
    }
    check("collapsed residual set has five targets", len(collapsed) == 5)
    check("collapsed set excludes W_stack_adoption as physics premise", "W_stack_adoption" not in collapsed)
    check("readout is independent from occurrence", "Closing readout coupling does not produce records" in note)
    check("occurrence is independent from source", "Closing occurrence does not choose physical source direction" in note_flat)
    check("source is independent from theta", "Closing source direction does not construct theta sectors" in note_flat)
    check("theta is independent from metric", "Closing theta does not identify the operational metric" in note)
    check("metric does not close phase or occurrence", "Closing metric/observable semantics does not by itself identify the phase-defect" in note_flat)

    section("PART F -- no-go discipline gate")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", item in note)
    check("N1 enumerates seven routes", note.count("| More-ontology route |") == 1 and note.count("| New primitive route |") == 1)
    check("N2 lists collapsed residuals", "Collapsed residuals" in note and all(target in note for target in required_targets))
    check("N3 classifies approved primitive", "Approved primitive" in note)
    check("N4 matches seven witnesses", note.count("| `") >= 7 and "Residual Matching" in note)
    check("N5 avoids cannot-derive overclaim", "does not say the remaining gates cannot be derived" in note)
    check("N6 lists five partial closure routes", note.count("derive `W_") >= 5)
    check("N7 steelman accepts bridge-first objection", "That objection is strong and accepted" in note)
    check("N8 cross-cycle echo present", "generic dynamics language" in note_flat)

    section("PART G -- non-overclaim checks")
    forbidden_positive_overclaims = [
        "records always form",
        "AC_phi_lambda is solved",
        "theta is solved",
    ]
    for phrase in forbidden_positive_overclaims:
        check(f"note does not overclaim: {phrase}", phrase not in note_flat)
    check("note explicitly avoids full-closure claim", "does not set an audit verdict" in note_flat and "does not" in note[:500] and "full theory closure" in note_flat)
    check("note explicitly avoids new-axiom-required claim", "not a claim that new axioms are required" in note_flat)
    check("note does not edit registries by claim", "edit registries" in note and "does not" in note[:500])
    check("note keeps current ontology story", "reality is a physical lattice of local possibility" in note_flat)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- remaining gates are localized to operational bridge/primitive candidates, not a broad ontology axiom.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
