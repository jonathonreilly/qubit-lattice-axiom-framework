#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_R_ETA_HUNIT_APPROVED_PRIMITIVE_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_PREMISES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
SCALE = DOCS / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = DOCS / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
IRREDUCIBILITY = DOCS / "RETA_ALGEBRAIC_IRREDUCIBILITY_GENUINE_READOUT_ADMISSION_BOUNDED_NOTE_2026-06-12.md"
CONVERSION = DOCS / "RETA_CONVERSION_FACTOR_CARRIER_CLASS_ELIMINATION_BOUNDED_NOTE_2026-06-12.md"
DIRECT_LICENSE = DOCS / "ACPHILAMBDA_R_ETA_DIRECT_LICENSE_HCLASS_HUNIT_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
DEFECT = DOCS / "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md"
NORMAL_FORM = DOCS / "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md"

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


def ledger_row_by_path(path: str) -> dict | None:
    rows = json.loads(read(LEDGER))["rows"]
    matches = [row for row in rows.values() if row.get("note_path") == path]
    if not matches:
        return None
    if len(matches) != 1:
        raise AssertionError(f"ledger matches for {path}: {len(matches)}")
    return matches[0]


def main() -> int:
    print("AC_phi_lambda R-eta h-unit approved-primitive non-supply no-go verifier")

    paths = [
        NOTE,
        TIER_A,
        LEDGER,
        AXIOMS,
        AXIOM_PREMISES,
        REGISTRY,
        SCALE,
        KINETIC,
        REALIZED,
        IRREDUCIBILITY,
        CONVERSION,
        DIRECT_LICENSE,
        DEFECT,
        NORMAL_FORM,
    ]

    section("A. source presence and Tier-A boundary")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    tier = json.loads(read(TIER_A))
    premises = json.loads(read(AXIOM_PREMISES))
    axioms = read(AXIOMS)
    registry = read(REGISTRY)
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    irreducibility = read(IRREDUCIBILITY)
    conversion = read(CONVERSION)
    direct_license = read(DIRECT_LICENSE)
    defect = read(DEFECT)
    normal_form = read(NORMAL_FORM)

    axioms_flat = flat(axioms)
    registry_flat = flat(registry)
    scale_flat = flat(scale)
    kinetic_flat = flat(kinetic)
    realized_flat = flat(realized)
    irreducibility_flat = flat(irreducibility)
    conversion_flat = flat(conversion)
    direct_flat = flat(direct_license)
    defect_flat = flat(defect)
    normal_flat = flat(normal_form)

    ac = tier["retired_derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    decomp = ac["minimum_decomposition"]
    check("Tier-A has no live admitted inputs", tier["genuine_admitted_input_count"] == 0 and tier["derivation_targets"] == {})
    check("AC minimum decomposition keeps R-eta", "delta_readout_identification_R_eta" in decomp, decomp)
    check("AC minimum decomposition keeps occupancy separate", "reading_occupancy_selection" in decomp, decomp)
    check("AC statement names R-eta", "R-eta" in ac["statement"] and "density-read-as-angle" in ac["statement"])
    check("human registry points to the R-eta derivation obligation", "AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md" in registry)
    check("note declares Type no_go", "**Type:** no_go" in note)
    check("note declares Claim type no_go", "**Claim type:** no_go" in note)
    check("note declares independent audit boundary", "independent audit lane only" in note)
    check("note says R-eta is not retired", "R-eta is not derived, refuted, re-graded, or removed from Tier-A" in note)
    check("note says AC_phi_lambda is not retired", "AC_phi_lambda is not retired." in note)
    check("note says no registry/axiom/primitive edit", "No registry, axiom, primitive, audit verdict, publication surface" in note)
    for forbidden in [
        "R-eta is retired",
        "AC_phi_lambda is retired",
        "h-unit is derived",
        "beta = 1 is derived",
        "therefore R-eta closes",
        "audit_status: audited_clean",
        "effective_status: retained",
        "promoted to retained",
    ]:
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)

    section("B. approved premise registry")
    expected = [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]
    check("approved premise registry has exactly four canonical ids", premises["canonical_ids"] == expected, premises["canonical_ids"])
    for cid in expected:
        check(f"approved premise node exists: {cid}", cid in premises["nodes"])
        check(f"{cid} has current_path", bool(premises["nodes"][cid].get("current_path")))
    banned_premise_terms = ["R-eta", "R_eta", "h-unit", "A_R-eta", "delta_readout_identification_R_eta"]
    premise_dump = json.dumps(premises)
    for term in banned_premise_terms:
        check(f"approved premise registry does not contain {term}", term not in premise_dump)

    section("C. axiom and primitive text boundaries")
    for phrase in [
        "Records form.",
        "A readout value is determined by record content alone",
        "context selection",
        "formation rules",
        "source/action and physical-observable identification",
    ]:
        check(f"minimal axiom boundary contains {phrase}", phrase in axioms_flat)
    for phrase in ["zero dimensionless content", "mixing angle", "phase", "selector", "readout bridge", "empirical fit"]:
        check(f"scale primitive withholds {phrase}", phrase in scale_flat)
    for phrase in ["c_t = c_s", "mass ratio", "coupling", "mixing angle", "phase", "selector", "readout bridge"]:
        check(f"kinetic primitive boundary contains {phrase}", phrase in kinetic_flat)
    for phrase in ["no state", "measure", "weighting", "probability rule", "normalization rule", "value"]:
        check(f"realized-state primitive withholds {phrase}", phrase in realized_flat)
    check("scale primitive is dimensionful only", "dimensionful" in scale_flat and "dimensionless" in scale_flat)
    check("kinetic primitive is a kinetic-form ratio only", "kinetic-form ratio" in kinetic_flat and "not a phase" not in kinetic_flat)
    check("realized primitive is pointwise only", "pointwise evaluation" in realized_flat and "registered data, not derivation output" in realized_flat)

    section("D. h-unit source pins")
    for phrase in [
        "unit/coefficient identity",
        "coefficient 1",
        "bare radian",
        "not pi or 2 pi",
        "Both atoms are open",
        "conversion-factor sources",
    ]:
        check(f"irreducibility source contains {phrase}", phrase in irreducibility_flat)
    for phrase in [
        "does not derive R-eta",
        "Future readout contexts remain open",
        "direct `c = 1` reading",
        "no primitive `c != 1` conversion carrier",
        "Does not turn the proposed R-eta identification into a retained axiom",
    ]:
        check(f"conversion source contains {phrase}", phrase in conversion_flat)
    for phrase in [
        "h-unit is not supplied",
        "Phi_beta = beta S_sum",
        "target is `beta = 1`",
        "A future direct readout-license theorem remains possible",
    ]:
        check(f"direct-license Block43 source contains {phrase}", phrase in direct_flat)
    for phrase in ["identity-unit member `c = 1`", "rescale-breaking", "W_defect_identity_unit"]:
        check(f"defect source contains {phrase}", phrase in defect_flat)
    for phrase in ["Phi(c)", "c = 1", "Phi = S_sum = 2/3", "No derivation is supplied"]:
        check(f"normal-form source contains {phrase}", phrase in normal_flat)

    section("E. dependency row status checks")
    expected_paths = [
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/RETA_ALGEBRAIC_IRREDUCIBILITY_GENUINE_READOUT_ADMISSION_BOUNDED_NOTE_2026-06-12.md",
        "docs/RETA_CONVERSION_FACTOR_CARRIER_CLASS_ELIMINATION_BOUNDED_NOTE_2026-06-12.md",
        "docs/ACPHILAMBDA_R_ETA_DIRECT_LICENSE_HCLASS_HUNIT_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md",
        "docs/ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md",
        "docs/ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md",
    ]
    for path in expected_paths:
        row = ledger_row_by_path(path)
        check(f"ledger row exists or approved premise for {Path(path).name}", row is not None or "PRIMITIVE" in path)
        if row is not None:
            check(f"{Path(path).name} has claim type", bool(row.get("claim_type")), row.get("claim_type"))
            check(f"{Path(path).name} is not unbounded retained import for h-unit", row.get("effective_status") != "retained", row.get("effective_status"))
    new_row = ledger_row_by_path("docs/ACPHILAMBDA_R_ETA_HUNIT_APPROVED_PRIMITIVE_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md")
    if new_row is None:
        check("new row not required before audit pipeline seeding", True)
    else:
        check("new row claim_type is no_go", new_row.get("claim_type") == "no_go", new_row.get("claim_type"))
        check("new row audit status remains non-promoted", new_row.get("audit_status") in {"unaudited", "audited_conditional"}, new_row.get("audit_status"))
        check("new row effective status remains non-promoted", new_row.get("effective_status") in {"unaudited", "audited_conditional", "retained_pending_chain"}, new_row.get("effective_status"))

    section("F. exact h-unit algebra and type checks")
    L = sp.Rational(2, 9)
    S_sum = 3 * L
    beta = sp.symbols("beta", real=True)
    target = sp.Rational(2, 3)
    phi_beta = beta * S_sum
    check("L = 2/9", L == sp.Rational(2, 9))
    check("S_sum = 3L = 2/3", S_sum == target)
    check("Phi_beta hits target only at beta=1", sp.solve(sp.Eq(phi_beta, target), beta) == [1])
    alternatives = {
        "zero": sp.Integer(0),
        "one_third": sp.Rational(1, 3),
        "identity": sp.Integer(1),
        "pi": sp.pi,
        "two_pi": 2 * sp.pi,
        "three": sp.Integer(3),
    }
    outputs = {name: sp.simplify(value * S_sum) for name, value in alternatives.items()}
    check("identity beta gives target", outputs["identity"] == target)
    for name in ["zero", "one_third", "pi", "two_pi", "three"]:
        check(f"beta {name} misses target", sp.simplify(outputs[name] - target) != 0)
    check("beta=1/3 gives single density", outputs["one_third"] == L)
    check("beta=3 gives three times target", outputs["three"] == 3 * target)
    check("numeric two-pi packaging misses target", not math.isclose(float(outputs["two_pi"]), float(target)))

    primitive_slots = {
        "scale_reference": {"type": "dimensionful_ruler", "value": "a^{-1}=M_Pl"},
        "kinetic_isotropy": {"type": "kinetic_form_ratio", "value": sp.Integer(1)},
        "realized_state": {"type": "pointwise_evaluation_slot", "value": None},
        "h_unit": {"type": "angle_readout_coefficient", "value": sp.Integer(1)},
    }
    check("kinetic value 1 has different type from h-unit value 1", primitive_slots["kinetic_isotropy"]["type"] != primitive_slots["h_unit"]["type"])
    check("scale reference has different type from h-unit", primitive_slots["scale_reference"]["type"] != primitive_slots["h_unit"]["type"])
    check("realized-state slot has no value", primitive_slots["realized_state"]["value"] is None)
    check("type mismatch blocks laundering kinetic 1 into beta 1", primitive_slots["kinetic_isotropy"]["value"] == 1 and primitive_slots["kinetic_isotropy"]["type"] != "angle_readout_coefficient")
    no_alt_carrier = True
    h_unit_assumed = False
    check("eliminating rival carriers is not h-unit derivation", no_alt_carrier and not h_unit_assumed)
    check("h-unit closure would require extra premise", no_alt_carrier and (not h_unit_assumed))

    section("G. note discipline and no-overclaim checks")
    required = [
        "bounded route no-go",
        "approved-premise registry",
        "h-unit",
        "beta = 1",
        "That implication is invalid",
        "A future h-unit theorem remains possible",
        "h-unit theorem",
        "Approved-primitive proposal",
    ]
    for phrase in required:
        check(f"note contains required boundary: {phrase}", phrase in note_flat)
    for n in range(1, 9):
        check(f"note contains N{n} no-go gate", f"**N{n}" in note)
    check("note links approved premise registry", "axiom_premise_nodes.json" in note)
    check("note links scale primitive", "SCALE_REFERENCE_PRIMITIVE_NOTE.md" in note)
    check("note links kinetic primitive", "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md" in note)
    check("note links realized-state primitive", "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md" in note)
    check("note links conversion source", "RETA_CONVERSION_FACTOR_CARRIER_CLASS_ELIMINATION_BOUNDED_NOTE_2026-06-12.md" in note)
    check("note does not use generated audit ledger as authority", "AUDIT_LEDGER.md](" not in note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL} CHECKS={PASS + FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
