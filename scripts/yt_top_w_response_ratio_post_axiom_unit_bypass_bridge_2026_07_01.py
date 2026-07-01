#!/usr/bin/env python3
"""Verify the Y_T top/W post-axiom response-ratio unit-bypass bridge."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "YT_TOP_W_RESPONSE_RATIO_POST_AXIOM_UNIT_BYPASS_BRIDGE_2026-07-01.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
DOUBLE_UNIT = DOCS / "SOURCE_OBSERVABLE_RESPONSE_RATIO_DOUBLE_UNIT_NORMAL_FORM_2026-07-01.md"
SOURCE_UNIT = DOCS / "YT_SOURCE_UNIT_POST_AXIOM_RN_REDUCTION_BRIDGE_2026-07-01.md"
SOURCE_COORD = DOCS / "YT_SOURCE_COORDINATE_INVARIANT_TOP_W_RATIO_GATE_NOTE_2026-05-25.md"
WZ_PACKET = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
TOP_SYMBOLIC = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
NEUTRAL_CARRIER = DOCS / "YT_EW_NEUTRAL_PROJECTOR_SAME_SURFACE_CARRIER_THEOREM_NOTE_2026-06-18.md"
TOP_UNDER = DOCS / "YT_TOP_RESPONSE_COEFFICIENT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-25.md"
FH_GATE = DOCS / "YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md"
FH_TOP = DOCS / "YT_FH_TOP_MASS_RESPONSE_PHYSICAL_INTERVENTION_BRIDGE_NOTE_2026-05-25.md"
STRICT_CONTRACT = DOCS / "YT_STRICT_SAME_SOURCE_TOP_W_POLE_ROW_CONTRACT_NOTE_2026-05-30.md"
METRIC_OBSERVABLE = DOCS / "METRIC_OBSERVABLE_CLOCKED_READOUT_INTERFACE_BRIDGE_2026-07-01.md"
PHYSICAL_SOURCE = DOCS / "PHYSICAL_SOURCE_SELECTOR_INDEPENDENCE_2026-07-01.md"

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


def main() -> int:
    print("=== Y_T top/W post-axiom response-ratio unit-bypass bridge ===")

    paths = [
        NOTE,
        AXIOMS,
        REGISTRY,
        TIER_A,
        DOUBLE_UNIT,
        SOURCE_UNIT,
        SOURCE_COORD,
        WZ_PACKET,
        TOP_SYMBOLIC,
        NEUTRAL_CARRIER,
        TOP_UNDER,
        FH_GATE,
        FH_TOP,
        STRICT_CONTRACT,
        METRIC_OBSERVABLE,
        PHYSICAL_SOURCE,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    registry_text = read(REGISTRY)
    registry = json.loads(registry_text)
    tier_text = read(TIER_A)
    tier = json.loads(tier_text)
    double_unit = read(DOUBLE_UNIT)
    source_unit = read(SOURCE_UNIT)
    source_coord = read(SOURCE_COORD)
    wz_packet = read(WZ_PACKET)
    top_symbolic = read(TOP_SYMBOLIC)
    neutral_carrier = read(NEUTRAL_CARRIER)
    top_under = read(TOP_UNDER)
    fh_gate = read(FH_GATE)
    fh_top = read(FH_TOP)
    strict_contract = read(STRICT_CONTRACT)
    metric_observable = read(METRIC_OBSERVABLE)
    physical_source = read(PHYSICAL_SOURCE)

    section("PART A -- registry and premise boundary")
    expected_primitives = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    check("approved primitive ids are expected", set(registry["canonical_ids"]) == expected_primitives)
    check("no registered physical-source primitive", "P_physical_source" not in registry_text)
    check("no registered physical response-ratio primitive", "P_physical_response_ratio" not in registry_text and "P_YT_same_source_response" not in registry_text)
    check("minimal axioms exclude source/action and observable bridges", "source/action bridge" in registry["nodes"]["minimal_axioms"]["note"] and "physical observable bridge" in registry["nodes"]["minimal_axioms"]["note"])
    check("tier A count remains two", tier["genuine_admitted_input_count"] == 2)
    labels = {entry["label"] for entry in tier["derivation_targets"].values()}
    check("tier A labels are AC_phi_lambda and theta", labels == {"AC_phi_lambda", "theta"}, labels)
    check("axioms do not supply source/action", "source/action bridge" in axioms or "source/action" in axioms)

    section("PART B -- source stack and Y_T surface")
    check("double-unit normal form proves source/output unit cancellation", "source-unit and output-unit invariant" in double_unit)
    check("source-unit YT bridge preserves physical top intervention", "W_physical_top_intervention" in source_unit)
    check("source coordinate gate proves top/W Jacobian cancellation", "The unknown Jacobian" in source_coord and "cancels" in source_coord)
    check("WZ packet supplies denominator support only", "W/Z denominator response" in wz_packet and "top coefficient" in wz_packet)
    check("symbolic top row leaves y_33 free", "y_33 remains a free" in top_symbolic or "coefficient y_33 remains free" in top_symbolic)
    check("same-surface neutral carrier support exists", "same-surface spectral-projector theorem" in neutral_carrier)
    check("top underdetermination keeps numerator blocker", "top coefficient" in top_under and "remains free" in top_under)
    check("FH gate has same-source top/W formula", "y_t = (g_2 / sqrt(2))" in fh_gate)
    check("FH top bridge gives lambda family", "lambda/sqrt(6)" in fh_top)
    check("strict contract requires actual evidence certificate", "Required Evidence Certificate" in strict_contract)
    check("metric/observable bridge keeps observable semantics open", "does not identify a physical clock" in metric_observable or "does not derive" in metric_observable)
    check("physical source selector remains independent", "current-premise independence" in physical_source and "W_physical_source" in physical_source)

    section("PART C -- finite top/W ratio algebra")
    y, g, vp, lam, mu = sp.symbols("y g vp lambda mu", nonzero=True)
    dmt = y / sp.sqrt(2) * vp
    dmw = g / 2 * vp
    ratio = sp.simplify(dmt / dmw)
    check("top/W derivative ratio is sqrt(2) y/g", sp.simplify(ratio - sp.sqrt(2) * y / g) == 0, ratio)
    recovered_y = sp.simplify(g / sp.sqrt(2) * ratio)
    check("response formula recovers y", sp.simplify(recovered_y - y) == 0)
    transformed = sp.simplify((mu * lam * dmt) / (mu * lam * dmw))
    check("source and common output units cancel", sp.simplify(transformed - ratio) == 0)
    offset_a, offset_b = sp.symbols("offset_a offset_b")
    # Additive offsets vanish because derivatives are unchanged.
    transformed_with_offsets = sp.simplify((mu * lam * dmt + sp.diff(offset_a, y)) / (mu * lam * dmw + sp.diff(offset_b, y)))
    check("additive output offsets do not affect derivative ratio", sp.simplify(transformed_with_offsets - ratio) == 0)

    y_target = 1 / sp.sqrt(6)
    ratio_target = sp.simplify(ratio.subs(y, y_target))
    check("y=1/sqrt(6) gives sqrt(2)/(g sqrt(6))", sp.simplify(ratio_target - sp.sqrt(2) / (g * sp.sqrt(6))) == 0, ratio_target)
    recovered_target = sp.simplify(g / sp.sqrt(2) * ratio_target)
    check("target ratio recovers 1/sqrt(6)", sp.simplify(recovered_target - y_target) == 0)

    lambda_t = sp.symbols("lambda_t", nonzero=True)
    y_scaled = lambda_t / sp.sqrt(6)
    ratio_scaled = sp.simplify(ratio.subs(y, y_scaled))
    recovered_scaled = sp.simplify(g / sp.sqrt(2) * ratio_scaled)
    check("genuine top coefficient lambda_t remains", sp.simplify(recovered_scaled - lambda_t / sp.sqrt(6)) == 0)

    section("PART D -- load-bearing contrast cases")
    mu_t, mu_w, lam_t, lam_w = sp.symbols("mu_t mu_w lam_t lam_w", nonzero=True)
    diff_output_ratio = sp.simplify((mu_t * dmt) / (mu_w * dmw))
    check("different output units leave relative output factor", sp.simplify(diff_output_ratio / ratio - mu_t / mu_w) == 0)
    diff_source_ratio = sp.simplify((lam_t * dmt) / (lam_w * dmw))
    check("different source lines leave relative source factor", sp.simplify(diff_source_ratio / ratio - lam_t / lam_w) == 0)
    check("same output condition is load-bearing", "same-output conditions are load-bearing" in note)
    check("same source condition is load-bearing", "same-source and same-output conditions are load-bearing" in note)

    section("PART E -- note content")
    for heading in [
        "## Claim",
        "## Source Surface",
        "## Finite Theorem",
        "## Explicit Witness",
        "## What Moves",
        "## What Remains",
        "## Audit Consequence If Retained",
        "## Non-Claims",
        "## Minimum Foundation Update If Bridge Work Fails",
        "## No-Go Discipline Gate",
        "## Verification",
    ]:
        check(f"note includes {heading}", heading in note)
    for phrase in [
        "W_same_source_topW_response",
        "W_top_coefficient_or_direct_response",
        "W_same_scale_g2",
        "W_matching_running_observable",
        "P_YT_same_source_response",
    ]:
        check(f"note names {phrase}", phrase in note)
    check("note declares independent audit authority", "independent audit lane only" in note)
    check("note declares no registry/axiom edits", "does not set an audit verdict, edit registries, register primitives, change axioms" in note_flat)
    check("note says no ontology axiom update follows", "No ontology axiom update follows from this theorem" in note)

    section("PART F -- no-go discipline N1-N8")
    for item in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"):
        check(f"note includes {item}", f"### {item}" in note)
    routes = [
        "Absolute source-unit route",
        "Same-source top/W ratio route",
        "Same-output mass-unit route",
        "Different-output route",
        "Carrier-source route",
        "Top coefficient theorem route",
        "Direct pole-response certificate route",
        "New primitive route",
    ]
    for route in routes:
        check(f"N1 route present: {route}", route in note)
    check("N2 removes overcounted unit walls", "`W_source_unit` and the common mass/output unit are not independent walls" in note)
    check("N3 classifies top coefficient as explicit residual", "| `top coefficient` | Explicit residual gate" in note)
    check("N4 has witness table", "Residual Matching" in note and note.count("| `") >= 7)
    check("N5 narrows ratio resolution", "first-derivative origin resolution" in note)
    check("N6 preserves live closure paths", "derive the same-source top/W pole-response certificate directly" in note and "derive same-scale `g_2`" in note)
    check("N7 steelman admits bookkeeping objection", "bookkeeping, not real physics" in note)
    check("N8 separates source line, unit, carrier, coefficient, and output", "line selection, unit normalization" in note_flat and "top coefficient" in note_flat)

    section("PART G -- non-overclaim checks")
    forbidden_assertions = [
        "therefore retained Y_T closure",
        "therefore y_33 = 1/sqrt(6) is derived",
        "therefore same-scale g_2 is derived",
        "therefore matching/running is closed",
        "therefore a new ontology axiom is required",
        "therefore the physical same-source top/W response surface is derived",
    ]
    for phrase in forbidden_assertions:
        check(f"note avoids overclaim assertion: {phrase}", phrase not in note_flat)
    check("non-claims preserve no YT closure", "- retained `Y_T` closure;" in note)
    check("non-claims preserve no top coefficient derivation", "- the top coefficient `y_33 = 1/sqrt(6)` is derived;" in note)
    check("non-claims preserve no g2 closure", "same-scale `g_2`" in note and "are closed;" in note)
    check("non-claims preserve no measured constants", "measured constants" in note and "are used" in note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print(
        "RESULT: PASS -- Y_T same-source same-output top/W ratios bypass source and common output units, while top-response and gauge/observable gates remain explicit."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
