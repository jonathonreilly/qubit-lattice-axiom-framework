#!/usr/bin/env python3
"""Verify the post-axiom remaining hard-gate route map."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs" / "POST_AXIOM_ADOPTION_REMAINING_HARD_GATE_ROUTE_MAP_2026-06-30.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
STRICT_NN = ROOT / "docs" / "STRICT_NN_COMPOSITION_FLUX_SELECTOR_BRIDGE_THEOREM_NOTE_2026-06-30.md"
DIRAC_PATH = ROOT / "docs" / "DIRAC_DYNAMICS_UNLOCK_PATH_FROM_AXIOM_RESET_2026-06-30.md"
AC_POST = ROOT / "docs" / "ACPHILAMBDA_POST_DIRAC_REDUCTION_MAP_2026-06-30.md"
R_HALF = ROOT / "docs" / "ACPHILAMBDA_R_HALF_DURABLE_RECORD_IDEMPOTENCE_BRIDGE_THEOREM_NOTE_2026-06-30.md"
SPECIES = ROOT / "docs" / "ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md"
R_ETA = ROOT / "docs" / "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md"
HW_COMP = ROOT / "docs" / "ACPHILAMBDA_HW_COMPLEMENTATION_EQUIVARIANCE_SUPPORT_NOTE_2026-06-09.md"
GRADE1 = ROOT / "docs" / "KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md"
FLAVOR_CARRIER = ROOT / "docs" / "FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31.md"
THREE_GEN = ROOT / "docs" / "THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md"
THETA_STRUCT = ROOT / "docs" / "STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md"
THETA_RG = ROOT / "docs" / "THETA_EMERGENT_Q_WEIGHTING_REALITY_RG_STABLE_BOUNDED_THEOREM_NOTE_2026-06-13.md"
RECORD_PROD = ROOT / "docs" / "RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md"
RECORD_DYN = ROOT / "docs" / "RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md"
BORN_BOUNDARY = ROOT / "docs" / "RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md"
OBS_PCAL = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_P1P2_TWO_STAGE_SYNTHESIS_NARROW_THEOREM_NOTE_2026-05-28.md"
GATE_B = ROOT / "docs" / "GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md"
ACTION_NORM = ROOT / "docs" / "ACTION_NORMALIZATION_NOTE.md"
SOURCE_TANGENT = ROOT / "docs" / "SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md"
SOURCE_PLANCK = ROOT / "docs" / "SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT_BRIDGE_NOTE_2026-05-30.md"
SCALE_PRIM = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC_PRIM = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED_PRIM = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
AXIOM_NODES = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

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


def main() -> int:
    print("=== Post-axiom adoption remaining hard-gate route map ===")

    paths = [
        NOTE,
        AXIOMS,
        STRICT_NN,
        DIRAC_PATH,
        AC_POST,
        R_HALF,
        SPECIES,
        R_ETA,
        HW_COMP,
        GRADE1,
        FLAVOR_CARRIER,
        THREE_GEN,
        THETA_STRUCT,
        THETA_RG,
        RECORD_PROD,
        RECORD_DYN,
        BORN_BOUNDARY,
        OBS_PCAL,
        GATE_B,
        ACTION_NORM,
        SOURCE_TANGENT,
        SOURCE_PLANCK,
        SCALE_PRIM,
        KINETIC_PRIM,
        REALIZED_PRIM,
        AXIOM_NODES,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    axioms_flat = flat(axioms)
    strict = read(STRICT_NN)
    dirac = read(DIRAC_PATH)
    ac_post = read(AC_POST)
    r_half = read(R_HALF)
    species = read(SPECIES)
    r_eta = read(R_ETA)
    hw_comp = read(HW_COMP)
    grade1 = read(GRADE1)
    flavor = read(FLAVOR_CARRIER)
    three_gen = read(THREE_GEN)
    theta_struct = read(THETA_STRUCT)
    theta_rg = read(THETA_RG)
    record_prod = read(RECORD_PROD)
    record_dyn = read(RECORD_DYN)
    born = read(BORN_BOUNDARY)
    pcal = read(OBS_PCAL)
    gate_b = read(GATE_B)
    action_norm = read(ACTION_NORM)
    source_tangent = read(SOURCE_TANGENT)
    source_planck = read(SOURCE_PLANCK)
    scale = read(SCALE_PRIM)
    kinetic = read(KINETIC_PRIM)
    realized = read(REALIZED_PRIM)
    nodes = read(AXIOM_NODES)

    print("\nPART A -- new axiom and Dirac bridge surface")
    check("axioms have four named premises", "Lattice, Qubit, Admissibility, Record" in axioms)
    check("axioms supply nearest-neighbor admissibility", "nearest-neighbor admissibility rule" in axioms)
    check("axioms keep further structure downstream", "structure requires derivation, bridge" in axioms_flat)
    check("axioms do not supply record production", "record-production process" in axioms)
    check("strict NN bridge selects flux(-1)", "selects flux(-1)" in strict)
    check("strict NN bridge rejects face-diagonal leakage", "face-diagonal leakage" in strict)
    check("Dirac path leaves AC_phi_lambda open", "AC_phi_lambda" in dirac and "does not by itself derive" in dirac)

    print("\nPART B -- AC_phi_lambda residuals")
    check("post-Dirac AC map names W_r", "W_r" in ac_post)
    check("post-Dirac AC map names W_eta", "W_eta" in ac_post)
    check("post-Dirac AC map names W_locus", "W_locus" in ac_post)
    check("r-half theorem is context-local", "not every site records" in r_half and "charged-lepton two-outcome record" in r_half)
    check("r-half theorem maps x=2r", "x = 2r" in r_half and "r = 1/2" in r_half)
    check("species note decomposes naming", "Naming" in species and "vacuous" in species)
    check("species note leaves carrier-locus residual", "carrier-locus selection" in species)
    check("species note uses realized-state primitive pointwise", "pointwise" in species and "registered data" in species)

    print("\nPART C -- context/locus evidence")
    check("three-generation theorem proves M3 algebra", "M_3(C)" in three_gen and "irreducible generation algebra" in three_gen)
    check("flavor carrier proves momentum type", "Carrier TYPE = momentum factor" in flavor)
    check("flavor carrier leaves hw=1 locus open", "Carrier LOCUS = hw=1 triplet" in flavor and "open physical-locus bridge" in flavor)
    check("hw complement note exchanges hw=1 and hw=2", "hw=1" in hw_comp and "hw=2" in hw_comp and "complementation" in hw_comp)
    check("hw complement note says support-only", "support-only" in hw_comp or "support only" in hw_comp)
    check("grade-1 note supplies compatibility not closure", "compatibility result" in grade1 and "not a closure" in grade1)

    print("\nPART D -- R-eta and theta")
    check("R-eta note isolates A_R-eta", "A_R-eta" in r_eta)
    check("R-eta note splits h-class/h-unit", "h-class" in r_eta and "h-unit" in r_eta)
    check("R-eta note says formal layer cannot select value", "machinery provably cannot select" in flat(r_eta))
    check("theta structured note maps gauge-side residual", "Gauge-side residual" in theta_struct)
    check("theta structured note maps mass-side residual", "Mass-side residual" in theta_struct)
    check("theta RG note gives CP-even set not zero", "{0, π}" in theta_rg or "{0, pi}" in theta_rg)
    check("theta RG note leaves Q existence open", "Q functional exists" in theta_rg or "Q-existence" in theta_rg)

    print("\nPART E -- record production, probability, measurement")
    check("record production checklist has instrument gate", "physical record-writing instrument" in record_prod)
    check("record production checklist separates produced record", "produced record" in record_prod)
    check("record production checklist separates local observability", "local observability" in record_prod)
    check("record dynamics separates three layers", "pre-record carrier" in record_dyn and "post-record information dynamics" in record_dyn)
    check("record dynamics says exact layer is consumer", "consumer" in record_dyn and "not a producer" in record_dyn)
    check("Born boundary says counts are post-record", "counts are information after realization" in born)
    check("Born boundary says IID/probability extra", "IID probability model is supplied" in born)
    check("Born boundary keeps probability model separate", "extra probability input" in born)

    print("\nPART F -- source/action/observable/scale primitives")
    check("P-cal note names P-cal", "P-cal" in pcal)
    check("P-cal note narrows P1/P2/P4", "replacing `{P1, P2, P4}`" in pcal or "replacing three" in pcal)
    check("Gate B note splits GB-S1", "GB-S1a" in gate_b and "GB-S1b" in gate_b)
    check("Gate B note leaves normalization residual", "normalization residual" in gate_b)
    check("action normalization note says convention locked", "convention-" in action_norm and "locked unless" in action_norm)
    check("source tangent note supplies Fisher tangent not full source semantics", "Fisher tangent" in source_tangent and "physical source semantics" in source_tangent)
    check("source Planck note leaves physical top source hinge", "remaining row-level audit question" in source_planck or "Remaining Hinge" in source_planck)
    check("scale primitive is units only", "units conversion" in scale and "It carries zero dimensionless" in scale)
    check("kinetic primitive is OS0 only", "c_t = c_s" in kinetic and "does not supply" in kinetic)
    check("realized primitive is pointwise only", "pointwise evaluation" in realized and "not a state-selection rule" in realized)
    check("axiom nodes register primitives", "scale_reference_primitive" in nodes and "kinetic_isotropy_primitive" in nodes and "realized_state_primitive" in nodes)

    print("\nPART G -- route map content")
    expected_sections = [
        "Charged-Lepton Context Selection",
        "Species / Locus Bridge",
        "`A_R-eta`",
        "Theta",
        "Record Occurrence / Production",
        "Probability, Born Weights, And Measurement Semantics",
        "Source / Action Coefficients",
        "Scale / Metric / Observable Bridge",
        "Priority Order",
        "Immediate Build Recommendation",
    ]
    for section in expected_sections:
        check(f"note includes {section}", section in note)
    check("note names generation context selector target", "GENERATION_CONTEXT_SELECTOR_FROM_STRICT_NN_DIRAC_RECORD_ORIENTATION" in note)
    check("note prioritizes context/locus first", "Generation-context selector / species-locus bridge" in note)
    check("note warns not to derive Born from counts alone", "not from record counts alone" in note)
    check("note preserves scale primitive boundary", "scale primitive should not be treated as an observable bridge" in note_flat)
    check("note identifies convention and selector routes", "Convention route" in note and "Selector route" in note)

    print("\nPART H -- no-go discipline gate")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", item in note)
    check("N1 has at least five route rows", note.count("|") >= 30)
    check("N2 names collapsed residual set", "Collapsed residual set" in note and "W_context_locus" in note)
    check("N4 residual table references all major gates", "W_source_action_observable" in note and "W_metric_scale_bridge" in note)
    check("N7 steelman is present", "A hostile reviewer can argue" in note)
    check("N8 cross-cycle echo is present", "broad imports often retire" in note)
    check("note does not claim closure", "not closed" in note_flat and "does not ship a terminal no-go" in note_flat)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- remaining hard gates are route-mapped and next bridge target is the generation context selector.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
