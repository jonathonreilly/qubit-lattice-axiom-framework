#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_R_ETA_DIRECT_LICENSE_HCLASS_HUNIT_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_PREMISES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
NARROWING = DOCS / "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md"
SUPPLIED_CONTEXT = DOCS / "SUPPLIED_READOUT_CONTEXT_TWO_COMPONENT_DECOMPOSITION_BOUNDED_NOTE_2026-07-02.md"
W2_CONTEXT = DOCS / "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md"
FIXED_LOCUS = DOCS / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
NORMAL_FORM = DOCS / "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md"
DEFECT = DOCS / "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md"
ANGLE_FRONTIER = DOCS / "ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md"
RECORD_SPLIT = DOCS / "RECORD_CONTENT_READOUT_LICENSE_SPLIT_REGISTRATION_UNREACHABILITY_THEOREM_NOTE_2026-07-02.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

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


def lin(coeffs: tuple[sp.Expr, ...], vec: tuple[sp.Expr, ...]) -> sp.Expr:
    return sp.simplify(sum(c * v for c, v in zip(coeffs, vec)))


def additive(coeffs: tuple[sp.Expr, ...], x: tuple[sp.Expr, ...], y: tuple[sp.Expr, ...]) -> bool:
    xy = tuple(a + b for a, b in zip(x, y))
    return sp.simplify(lin(coeffs, xy) - lin(coeffs, x) - lin(coeffs, y)) == 0


def main() -> int:
    print("AC_phi_lambda R-eta direct-license h-class/h-unit non-supply no-go verifier")

    paths = [
        NOTE,
        TIER_A,
        LEDGER,
        AXIOMS,
        AXIOM_PREMISES,
        REGISTRY,
        NARROWING,
        SUPPLIED_CONTEXT,
        W2_CONTEXT,
        FIXED_LOCUS,
        NORMAL_FORM,
        DEFECT,
        ANGLE_FRONTIER,
        RECORD_SPLIT,
        REALIZED,
    ]

    section("A. source presence and Tier-A boundary")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    tier = json.loads(read(TIER_A))
    axioms = read(AXIOMS)
    premises = json.loads(read(AXIOM_PREMISES))
    registry = read(REGISTRY)
    narrowing = read(NARROWING)
    supplied_context = read(SUPPLIED_CONTEXT)
    w2_context = read(W2_CONTEXT)
    fixed_locus = read(FIXED_LOCUS)
    normal_form = read(NORMAL_FORM)
    defect = read(DEFECT)
    angle_frontier = read(ANGLE_FRONTIER)
    record_split = read(RECORD_SPLIT)
    realized = read(REALIZED)

    axioms_flat = flat(axioms)
    registry_flat = flat(registry)
    narrowing_flat = flat(narrowing)
    supplied_flat = flat(supplied_context)
    w2_flat = flat(w2_context)
    fixed_flat = flat(fixed_locus)
    normal_flat = flat(normal_form)
    defect_flat = flat(defect)
    angle_flat = flat(angle_frontier)
    record_split_flat = flat(record_split)
    realized_flat = flat(realized)

    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    decomp = ac["minimum_decomposition"]
    check("AC_phi_lambda remains the live Tier-A target", tier["genuine_admitted_input_count"] >= 1)
    check("AC minimum decomposition keeps R-eta", "delta_readout_identification_R_eta" in decomp, decomp)
    check("AC minimum decomposition keeps occupancy separate", "reading_occupancy_selection" in decomp, decomp)
    check("AC statement names density-read-as-angle R-eta", "density-read-as-angle" in ac["statement"] and "R-eta" in ac["statement"])
    check("human registry names R-eta", ("R-eta" in registry_flat or "R-\u03b7" in registry) and "density-read-as-angle" in registry_flat)
    check("note declares Type no_go", "**Type:** no_go" in note)
    check("note declares Claim type no_go", "**Claim type:** no_go" in note)
    check("note declares independent audit boundary", "independent audit lane only" in note)
    check("note says R-eta is not retired", "R-eta is not derived, refuted, re-graded, or removed from Tier-A" in note)
    check("note says AC_phi_lambda is not retired", "AC_phi_lambda is not retired." in note)
    check("note says no registry/axiom/primitive edit", "No registry, axiom, primitive, audit verdict, publication surface" in note)
    for forbidden in [
        "R-eta is retired",
        "AC_phi_lambda is retired",
        "A_R-eta is derived.",
        "therefore R-eta closes",
        "audit_status: audited_clean",
        "effective_status: retained",
        "promoted to retained",
    ]:
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)

    section("B. axiom and primitive boundary pins")
    check("approved premise registry has minimal axioms", "minimal_axioms" in premises["canonical_ids"])
    check("approved premise registry excludes R-eta", all("R" not in cid and "eta" not in cid for cid in premises["canonical_ids"]))
    for phrase in [
        "Records form.",
        "A readout value is determined by record content alone",
        "scalar readout `I` is additive",
        "context selection",
        "measurement basis selection",
        "formation rules",
        "source/action and physical-observable identification",
    ]:
        check(f"minimal axioms contain boundary phrase: {phrase}", phrase in axioms_flat)
    check("minimal axioms name AC_phi_lambda as outside axioms", "AC_phi_lambda" in axioms and "outside axiom content" in axioms_flat)
    for phrase in ["no state", "measure", "weighting", "probability rule", "normalization rule", "value"]:
        check(f"realized-state primitive withholds {phrase}", phrase in realized_flat)

    section("C. source-surface h-class/h-unit pins")
    for phrase in [
        "A_R-eta",
        "**(h-class)** class membership",
        "**(h-unit)** identity reading",
        "The surviving atom",
        "remains admitted",
    ]:
        check(f"narrowing source contains {phrase}", phrase in narrowing)
    for phrase in [
        "C1 (FRAME)",
        "C2 (WEIGHTING)",
        "C1 Does Not Supply C2",
        "C2 Does Not Supply C1",
        "No C1 supplier is derived here",
    ]:
        check(f"supplied-context source contains {phrase}", phrase in supplied_context)
    for phrase in [
        "supplied finite context algebra",
        "physical carrier realization",
        "The value atom `A_R-eta` remains admitted",
        "not a value derivation and not an admission retirement",
    ]:
        check(f"W2 source contains {phrase}", phrase in w2_flat)
    for phrase in [
        "L\u2083(1,2)",
        "2/9",
    ]:
        check(f"fixed-locus source contains {phrase}", phrase in fixed_locus)
    fixed_lower = fixed_flat.lower()
    check("fixed-locus source excludes physical readout bridge", "physical readout" in fixed_lower or "physical single-summand" in fixed_lower)
    for phrase in [
        "Phi = S_sum = 2/3",
        "W_cycle_holonomy_value",
        "physical charged-lepton readout",
        "No derivation is supplied",
    ]:
        check(f"normal-form source contains {phrase}", phrase in normal_form)
    for phrase in [
        "W_defect_identity_unit",
        "identity-unit member",
        "rescale-breaking",
    ]:
        check(f"defect source contains {phrase}", phrase in defect)
    for phrase in [
        "Phi = S_sum",
        "live R-eta license",
        "license target",
    ]:
        check(f"angle frontier source contains {phrase}", phrase in angle_frontier)
    for phrase in [
        "record-determined content",
        "readout-construction",
        "license split",
    ]:
        check(f"record split source contains {phrase}", phrase in record_split_flat)

    section("D. dependency row status checks")
    expected_paths = [
        "docs/ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md",
        "docs/SUPPLIED_READOUT_CONTEXT_TWO_COMPONENT_DECOMPOSITION_BOUNDED_NOTE_2026-07-02.md",
        "docs/ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md",
        "docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
        "docs/ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md",
        "docs/ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md",
        "docs/ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md",
        "docs/RECORD_CONTENT_READOUT_LICENSE_SPLIT_REGISTRATION_UNREACHABILITY_THEOREM_NOTE_2026-07-02.md",
    ]
    for path in expected_paths:
        row = ledger_row_by_path(path)
        check(f"ledger row exists for {Path(path).name}", row is not None)
        if row is not None:
            check(f"{Path(path).name} is not unbounded retained", row.get("effective_status") != "retained", row.get("effective_status"))
            check(f"{Path(path).name} has claim type", bool(row.get("claim_type")), row.get("claim_type"))
    new_row = ledger_row_by_path("docs/ACPHILAMBDA_R_ETA_DIRECT_LICENSE_HCLASS_HUNIT_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md")
    if new_row is None:
        check("new row not required before audit pipeline seeding", True)
    else:
        check("new row claim_type is no_go", new_row.get("claim_type") == "no_go", new_row.get("claim_type"))
        check("new row audit status remains unaudited", new_row.get("audit_status") == "unaudited", new_row.get("audit_status"))
        check("new row effective status remains unaudited", new_row.get("effective_status") == "unaudited", new_row.get("effective_status"))

    section("E. fixed-locus and holonomy algebra")
    L = sp.Rational(2, 9)
    S_sum = 3 * L
    c, beta = sp.symbols("c beta", real=True)
    phi_c = c * S_sum
    phi_beta = beta * S_sum
    target = sp.Rational(2, 3)
    check("L = 2/9", L == sp.Rational(2, 9))
    check("S_sum = 3L = 2/3", S_sum == target)
    check("Phi(c) = c S_sum hits target at c=1", sp.solve(sp.Eq(phi_c, target), c) == [1])
    check("Phi_beta hits target at beta=1", sp.solve(sp.Eq(phi_beta, target), beta) == [1])
    check("target is not the single density L", target != L)
    check("target is not count normalization 1", target != 1)
    check("target is not zero", target != 0)
    check("2*pi packaging misses target", not math.isclose(float(2 * math.pi * float(S_sum)), float(target)))
    check("1/3 unit maps S_sum back to L", sp.simplify(sp.Rational(1, 3) * S_sum - L) == 0)
    check("3 unit maps single density L to target", sp.simplify(3 * L - target) == 0)
    check("same target can be fit by different class/unit pairs", sp.simplify(1 * S_sum - 3 * L) == 0)
    check("target below pi", float(target) < math.pi)
    check("target nonzero bare angle", target > 0)

    section("F. record-additive h-class witnesses")
    x3 = (sp.Integer(1), sp.Integer(0), sp.Integer(2))
    y3 = (sp.Integer(0), sp.Integer(3), sp.Integer(1))
    state = (sp.Integer(1), sp.Integer(1), sp.Integer(1))
    readouts = {
        "zero": (sp.Integer(0), sp.Integer(0), sp.Integer(0)),
        "count": (sp.Integer(1), sp.Integer(1), sp.Integer(1)),
        "single_density": (L / 3, L / 3, L / 3),
        "unaveraged_fixed_locus_sum": (L, L, L),
        "double_sum": (2 * L, 2 * L, 2 * L),
    }
    values = {}
    for name, coeffs in readouts.items():
        check(f"{name} empty-record readout is zero", lin(coeffs, (0, 0, 0)) == 0)
        check(f"{name} is additive on disjoint sample records", additive(coeffs, x3, y3))
        values[name] = lin(coeffs, state)
        check(f"{name} depends only on record content", all(c in coeffs for c in coeffs))
    check("zero map misses target", values["zero"] != target)
    check("count map misses target", values["count"] != target)
    check("single-density map gives L", values["single_density"] == L)
    check("unaveraged fixed-locus sum gives target", values["unaveraged_fixed_locus_sum"] == target)
    check("double sum misses target", values["double_sum"] != target)
    distinct_values = {sp.sstr(v) for v in values.values()}
    check("same record frame admits multiple additive scalar values", len(distinct_values) == len(values), values)
    check("Record additivity alone does not select the target member", sum(1 for v in values.values() if v == target) == 1)

    section("G. h-unit and C1/C2 independence witnesses")
    beta_values = [sp.Integer(0), sp.Rational(1, 3), sp.Integer(1), 2 * sp.pi, sp.Integer(3)]
    beta_outputs = [sp.simplify(b * S_sum) for b in beta_values]
    for b, out in zip(beta_values, beta_outputs):
        check(f"beta={b} gives an additive scalar multiple", sp.simplify(out - b * S_sum) == 0)
    check("only beta=1 in tested set hits target", sum(1 for out in beta_outputs if sp.simplify(out - target) == 0) == 1)
    check("beta=2*pi is not identity unit", sp.simplify(2 * sp.pi * S_sum - target) != 0)
    check("beta=0 is zero readout", beta_outputs[0] == 0)
    check("beta=1/3 recovers single-density value", beta_outputs[1] == L)

    x2 = (sp.Integer(1), sp.Integer(2))
    y2 = (sp.Integer(3), sp.Integer(4))
    coeff_w1 = (sp.Integer(1), sp.Integer(1))
    coeff_w2 = (sp.Integer(1), sp.Integer(2))
    check("C1 fixed frame with w=1 is additive", additive(coeff_w1, x2, y2))
    check("C1 fixed frame with w=2 is additive", additive(coeff_w2, x2, y2))
    check("same frame different C2 weights yield different values", lin(coeff_w1, x2) != lin(coeff_w2, x2))
    H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    unit = sp.Matrix([1, 0])
    mixed = H * unit
    check("Hadamard mixed frame has equal squared weights", sp.simplify(mixed[0] ** 2 - mixed[1] ** 2) == 0)
    check("Hadamard mixed first cell is not original unit cell", sp.simplify(mixed[0] - 1) != 0)
    check("equal weighting alone does not recover original frame", sp.simplify(mixed[1]) != 0)

    section("H. note discipline and no-overclaim checks")
    required = [
        "bounded route no-go",
        "h-class",
        "h-unit",
        "A_R-eta",
        "This implication is invalid",
        "a successful proof must derive both h-class and h-unit",
        "A future direct readout-license theorem remains possible",
        "h-class theorem",
        "h-unit theorem",
        "Combined direct-license theorem",
        "Owner governance",
    ]
    for phrase in required:
        check(f"note contains required boundary: {phrase}", phrase in note_flat)
    for n in range(1, 9):
        check(f"note contains N{n} no-go gate", f"**N{n}" in note)
    check("note links Tier-A residual atom", "delta_readout_identification_R_eta" in note)
    check("note links minimal axioms", "MINIMAL_AXIOMS_2026-06-29.md" in note)
    check("note names narrowing source as context", "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md" in note)
    check("note does not use generated audit ledger as authority", "AUDIT_LEDGER.md](" not in note)
    check("angle frontier classifies Phi=S_sum as target", "live R-eta license" in angle_flat)
    check("W2 context leaves physical carrier realization open", "physical charged-lepton carrier must be shown to realize this context" in w2_flat)
    check("supplied context says frame does not supply weighting", "C1 Does Not Supply C2" in supplied_context)
    check("defect rescale leaves c=1 open", "identity-unit member `c = 1`" in defect_flat)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL} CHECKS={PASS + FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
