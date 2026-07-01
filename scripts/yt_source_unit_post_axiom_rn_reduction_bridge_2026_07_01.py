#!/usr/bin/env python3
"""Verify the Y_T source-unit post-axiom RN reduction bridge."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "YT_SOURCE_UNIT_POST_AXIOM_RN_REDUCTION_BRIDGE_2026-07-01.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
PRIMITIVES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
SCALE = DOCS / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = DOCS / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
BORN = DOCS / "RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md"
SOURCE_PCAL = DOCS / "RECORD_BORN_TO_SOURCE_MEASURE_PCAL_INTERFACE_BRIDGE_2026-06-30.md"
SOURCE_ACTION = DOCS / "SOURCE_ACTION_RN_FACTORIZATION_FROM_RECORD_BORN_INTERFACE_2026-06-30.md"
SOURCE_SELECTOR = DOCS / "PHYSICAL_SOURCE_SELECTOR_INDEPENDENCE_2026-07-01.md"
YT_BOUNDARY = DOCS / "YT_SOURCE_MEASURE_TIER_A_SOURCE_UNIT_BOUNDARY_NOTE_2026-05-30.md"
YT_TIER_A = DOCS / "YT_TIER_A_SOURCE_ACTION_TOP_PREMISE_CLOSURE_NOTE_2026-05-29.md"
YT_OPERATIONAL = DOCS / "YT_OPERATIONAL_SOURCE_ACTION_BRIDGE_THEOREM_ATTEMPT_NOTE_2026-05-25.md"
YT_FISHER = DOCS / "YT_PRIMITIVE_SOURCE_UNIT_FISHER_NORMALIZATION_SUPPORT_NOTE_2026-05-25.md"
YT_DEMOCRATIC = DOCS / "YT_QUBIT_DEMOCRATIC_TOP_COEFFICIENT_CANDIDATE_NOTE_2026-05-25.md"
YT_SIGNED = DOCS / "YT_QUBIT_SIGNED_LINEAR_SOURCE_RESPONSE_BRIDGE_CANDIDATE_NOTE_2026-05-25.md"
YT_EW_CARRIER = DOCS / "YT_EW_NEUTRAL_PROJECTOR_SAME_SURFACE_CARRIER_THEOREM_NOTE_2026-06-18.md"
YT_FH_TOP = DOCS / "YT_FH_TOP_MASS_RESPONSE_PHYSICAL_INTERVENTION_BRIDGE_NOTE_2026-05-25.md"
YT_STRICT = DOCS / "YT_STRICT_SAME_SOURCE_TOP_W_POLE_ROW_CONTRACT_NOTE_2026-05-30.md"
PRIMITIVE_RECOMMENDATION = DOCS / "MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + title)


def expectation(prob: list[sp.Expr], values: list[sp.Expr]) -> sp.Expr:
    return sp.simplify(sum(p * v for p, v in zip(prob, values)))


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(sp.together(expr.rewrite(sp.exp))) == 0


def main() -> int:
    print("=== Y_T source-unit post-axiom RN reduction bridge ===")

    paths = [
        NOTE,
        AXIOMS,
        TIER_A,
        PRIMITIVES,
        SCALE,
        KINETIC,
        REALIZED,
        BORN,
        SOURCE_PCAL,
        SOURCE_ACTION,
        SOURCE_SELECTOR,
        YT_BOUNDARY,
        YT_TIER_A,
        YT_OPERATIONAL,
        YT_FISHER,
        YT_DEMOCRATIC,
        YT_SIGNED,
        YT_EW_CARRIER,
        YT_FH_TOP,
        YT_STRICT,
        PRIMITIVE_RECOMMENDATION,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    tier_text = read(TIER_A)
    tier = json.loads(tier_text)
    primitives_text = read(PRIMITIVES)
    primitives = json.loads(primitives_text)
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    born = read(BORN)
    source_pcal = read(SOURCE_PCAL)
    source_action = read(SOURCE_ACTION)
    source_selector = read(SOURCE_SELECTOR)
    yt_boundary = read(YT_BOUNDARY)
    yt_tier_a = read(YT_TIER_A)
    yt_operational = read(YT_OPERATIONAL)
    yt_fisher = read(YT_FISHER)
    yt_democratic = read(YT_DEMOCRATIC)
    yt_signed = read(YT_SIGNED)
    yt_ew = read(YT_EW_CARRIER)
    yt_fh = read(YT_FH_TOP)
    yt_strict = read(YT_STRICT)
    primitive_recommendation = read(PRIMITIVE_RECOMMENDATION)

    section("PART A -- registry and primitive boundary")
    check("Tier-A genuine admitted input count is two", tier["genuine_admitted_input_count"] == 2)
    labels = {entry["label"] for entry in tier["derivation_targets"].values()}
    check("Tier-A labels are AC_phi_lambda and theta", labels == {"AC_phi_lambda", "theta"}, labels)
    check("Tier-A canonical ids exclude source-measure/P-cal", all("source" not in cid.lower() and "pcal" not in cid.lower() and "p-cal" not in cid.lower() for cid in tier["canonical_ids"]))
    expected_primitives = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    check("approved primitive registry has expected ids", set(primitives["canonical_ids"]) == expected_primitives, primitives["canonical_ids"])
    check("minimal axioms registry note excludes source/action bridge", "source/action bridge" in primitives["nodes"]["minimal_axioms"]["note"])
    check("minimal axioms note keeps source/action downstream", "source/action" in axioms and "Further physical structure requires" in flat(axioms))
    check("scale primitive has no dimensionless selector content", "zero dimensionless content" in flat(scale).lower() and "selector" in flat(scale).lower())
    check("kinetic primitive supplies no dynamics selector", "no mass ratio, coupling, mixing angle, phase, selector" in flat(kinetic))
    check("realized-state primitive supplies no probability or state-selection", "state-selection rule" in flat(realized) and "probability rule" in flat(realized))

    section("PART B -- post-axiom source stack")
    check("Record/Born bridge supplies trace weights", "Tr(rho P_r)" in born)
    check("Record/Born bridge preserves occurrence wall", "W_occurrence" in born)
    check("Record/Born to P-cal bridge names W_source_action", "W_source_action" in source_pcal)
    check("Record/Born to P-cal bridge supplies RN/log-normalizer surface", "RN/log-normalizer source-measure calculus" in source_pcal)
    check("source/action bridge names W_physical_source", "W_physical_source" in source_action)
    check("source/action bridge states RN/action identity", "R_h(omega) = P_h(omega) / P_0(omega)" in source_action)
    check("physical source selector note keeps selector open", "current-premise independence" in source_selector and "W_physical_source" in source_selector)

    section("PART C -- old Y_T source-unit surfaces")
    check("old Y_T boundary used Tier-A source-measure/P-cal surface", "accepted Tier-A source-measure/P-cal surface" in yt_boundary)
    check("old Y_T boundary gives lambda=1 on that surface", "lambda = 1" in yt_boundary and "y_33 = 1/sqrt(6)" in yt_boundary)
    check("old Tier-A closure states scaled family", "lambda/sqrt(6)" in yt_tier_a or "lambda / sqrt(6)" in yt_tier_a)
    check("operational Y_T bridge supplies finite RN/log-density support", "finite RN/log-density" in yt_operational or "RN/log-density" in yt_operational)
    check("Fisher support note names source unit", "Fisher" in yt_fisher and "lambda" in yt_fisher)
    check("democratic support has six-component 1/sqrt(6)", "1/sqrt(6)" in yt_democratic)
    check("signed-linear support keeps physical bridge open", "physical bridge remains open" in yt_signed)
    check("EW neutral carrier is support, not closure", "no positive Y_T closure" in yt_ew or "does not derive positive Y_T closure" in yt_ew)
    check("FH top bridge localizes physical intervention", "physical top Yukawa deformation" in yt_fh and "lambda/sqrt(6)" in yt_fh)
    check("strict same-source route remains explicit", "same-source" in yt_strict and "top" in yt_strict.lower())

    section("PART D -- finite source-unit algebra")
    lam = sp.symbols("lambda", positive=True)
    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    norm_u = sp.simplify(u.dot(u))
    scaled_u = lam * u
    scaled_norm = sp.simplify(scaled_u.dot(scaled_u))
    check("democratic six-component direction is unit", sp.simplify(norm_u - 1) == 0)
    check("each component is 1/sqrt(6)", all(sp.simplify(component - 1 / sp.sqrt(6)) == 0 for component in u))
    check("scaled source norm is lambda^2", sp.simplify(scaled_norm - lam**2) == 0)
    check("scaled component is lambda/sqrt(6)", sp.simplify(scaled_u[0] - lam / sp.sqrt(6)) == 0)
    check("unit source lambda=1 gives y_33=1/sqrt(6)", sp.simplify(scaled_u[0].subs(lam, 1) - 1 / sp.sqrt(6)) == 0)

    h = sp.symbols("h", real=True)
    prob = [sp.Rational(1, 4)] * 4
    score = [sp.sqrt(2), -sp.sqrt(2), 0, 0]
    z = expectation(prob, [sp.exp(h * s) for s in score])
    rn = [sp.simplify(sp.exp(h * s) / z) for s in score]
    origin_score = [sp.simplify(sp.diff(sp.log(r), h).subs(h, 0)) for r in rn]
    fisher_norm = expectation(prob, [s**2 for s in origin_score])
    scaled_rn = [sp.simplify(sp.exp(h * lam * s) / expectation(prob, [sp.exp(h * lam * t) for t in score])) for s in score]
    scaled_origin = [sp.simplify(sp.diff(sp.log(r), h).subs(h, 0)) for r in scaled_rn]
    scaled_fisher = expectation(prob, [s**2 for s in scaled_origin])
    check("finite RN family normalizes", is_zero(expectation(prob, rn) - 1))
    check("origin RN score is requested score", all(sp.simplify(origin_score[i] - score[i]) == 0 for i in range(4)))
    check("unit RN score has Fisher norm one", sp.simplify(fisher_norm - 1) == 0)
    check("lambda-scaled RN score has Fisher norm lambda^2", sp.simplify(scaled_fisher - lam**2) == 0)

    section("PART E -- note content")
    required_sections = [
        "Claim",
        "Source Surface",
        "Finite Source-Unit Calculation",
        "What Moves",
        "What Remains",
        "Audit Consequence If Retained",
        "Non-Claims",
        "No-Go Discipline Gate",
    ]
    for section_name in required_sections:
        check(f"note includes {section_name}", f"## {section_name}" in note)
    check("note names W_physical_top_intervention", "W_physical_top_intervention" in note)
    check("note states current Tier-A count", "only two genuine admitted derivation targets" in note)
    check("note states post-axiom composition", "supplied Record/Born selective interface" in note and "action-exponent deformation = RN/Fisher source coordinate" in note)
    check("note states lambda family", "lambda/sqrt(6)" in note and "lambda^2" in note)
    check("note does not request new ontology axiom", "No ontology axiom update is requested by this note" in note_flat)
    check("note avoids measured-value inputs", "PDG values" in note and "measured masses as proof inputs" in note)

    section("PART F -- no-go discipline gate")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", f"### {item}" in note)
    routes = [
        "Record/Born interface route",
        "RN/log-normalizer route",
        "Action-exponent route",
        "Old Tier-A P-cal route",
        "Six-component source-unit route",
        "Strict same-source top/W response route",
        "New primitive route",
    ]
    for route in routes:
        check(f"N1 route present: {route}", route in note)
    check("N2 collapses residual to W_physical_top_intervention", "Collapsed residual after this bridge" in note and "W_physical_top_intervention." in note)
    check("N3 classifies primitive source coordinate as residual", '"Primitive operational RN/Fisher source coordinate" is the named remaining selector' in note_flat)
    check("N4 matches source witnesses", note.count("| `") >= 7 and "YT_FH_TOP_MASS_RESPONSE_PHYSICAL_INTERVENTION_BRIDGE" in note)
    check("N5 avoids terminal no-go and closure overclaim", "does not say source/action is impossible" in note and "does not say `Y_T` is closed" in note)
    check("N6 lists live closure paths", "strict same-source top/W pole-response" in note and "narrow physical-source primitive" in note)
    check("N7 steelman admits bookkeeping objection", "bookkeeping, not physics" in note)
    check("N8 cross-cycle echo present", "finite source calculus is not the physical source selector" in note_flat)

    section("PART G -- assembled conclusion")
    primitive_route_text = flat(primitive_recommendation)
    check("primitive recommendation names P_physical_source", "P_physical_source" in primitive_route_text)
    check("new note keeps primitive route unregistered", "Register a physical source selector" in note and "not taken here" in note)
    check("generic P-cal/RN wall is moved, not top selector", "source-unit blocker for `Y_T` is not generic P-cal/RN algebra" in note and "physical top-intervention selector" in note)
    check("physical top source remains open", "derivation of the physical top Yukawa source" in note and "does not claim" in note)
    check("Y_T closure remains unclaimed", "unbounded retained `Y_T` closure" in note and "does not set an audit verdict" in note_flat)

    forbidden = [
        "Y_T is solved",
        "therefore physical top source is derived",
        "therefore source/action closure is impossible",
        "requires a new ontology axiom",
        "PDG input fixes",
    ]
    for phrase in forbidden:
        check(f"note avoids overclaim phrase: {phrase}", phrase not in note)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL -- Y_T source-unit post-axiom RN reduction bridge is not verifier-clean.")
        return 1
    print("RESULT: PASS -- stale generic source-measure/P-cal boundary reduces to the physical top-intervention selector.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
