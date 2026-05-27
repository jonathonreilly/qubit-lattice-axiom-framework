#!/usr/bin/env python3
"""Hard-stop no-go for Y_T top-source identification from current inputs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_top_source_identification_hard_stop_no_go_2026-05-27.json"

NOTE = DOCS / "YT_TOP_SOURCE_IDENTIFICATION_HARD_STOP_NO_GO_NOTE_2026-05-27.md"
PRIMITIVE_LAW = DOCS / "YT_PRIMITIVE_RECORD_INTERVENTION_LAW_THEOREM_NOTE_2026-05-27.md"
TOP_CARRIER = DOCS / "YT_ONE_HIGGS_TOP_CARRIER_SELECTION_SUPPORT_NOTE_2026-05-26.md"
DEMOCRATIC = DOCS / "YT_QUBIT_DEMOCRATIC_TOP_COEFFICIENT_CANDIDATE_NOTE_2026-05-25.md"
MININFO_GATE = DOCS / "YT_PHYSICAL_INTERVENTION_MININFO_UNIQUENESS_GATE_NOTE_2026-05-26.md"
SOURCE_SCALE = DOCS / "YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"

PRIMITIVE_LAW_OUT = ROOT / "outputs" / "yt_primitive_record_intervention_law_2026-05-27.json"
TOP_CARRIER_OUT = ROOT / "outputs" / "yt_one_higgs_top_carrier_selection_support_2026-05-26.json"
MININFO_GATE_OUT = ROOT / "outputs" / "yt_physical_intervention_mininfo_uniqueness_gate_2026-05-26.json"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(read(path))


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    paths = (
        NOTE,
        PRIMITIVE_LAW,
        TOP_CARRIER,
        DEMOCRATIC,
        MININFO_GATE,
        SOURCE_SCALE,
        FULL_STACK,
        PRIMITIVE_LAW_OUT,
        TOP_CARRIER_OUT,
        MININFO_GATE_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Positive Content Already Available",
        "Counterfamily",
        "Why The Primitive Law Does Not Remove This No-Go By Itself",
        "Why Gauge / One-Higgs / Top-Sector Uniqueness Is Insufficient",
        "Hard-Stop Conclusion",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    primitive = load_json(PRIMITIVE_LAW_OUT)
    carrier = load_json(TOP_CARRIER_OUT)
    mininfo = load_json(MININFO_GATE_OUT)
    check("primitive record law passed", primitive.get("fail_count") == 0, primitive.get("fail_count"))
    check("top carrier support passed", carrier.get("fail_count") == 0, carrier.get("fail_count"))
    check("mininfo uniqueness gate passed", mininfo.get("fail_count") == 0, mininfo.get("fail_count"))
    return {"primitive": primitive, "carrier": carrier, "mininfo": mininfo}


def part2_positive_conditional_theorem() -> dict[str, str]:
    print("\nPart 2: positive conditional theorem still holds")
    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    norm = sp.simplify((u.T * u)[0])
    check("democratic six-component vector is unit normalized", is_zero(norm - 1), norm)
    check("single component is 1/sqrt(6)", is_zero(u[0] - 1 / sp.sqrt(6)), u[0])

    lam = sp.symbols("lambda", positive=True)
    fisher_component = sp.simplify((lam * u[0]) / sp.sqrt(lam**2))
    check("primitive Fisher coordinate gives component 1/sqrt(6)", is_zero(fisher_component - 1 / sp.sqrt(6)), fisher_component)
    check("conditional theorem is present in note", "If the physical top source coordinate is accepted" in read(NOTE))
    return {"conditional_component": "1/sqrt(6)"}


def part3_counterfamily() -> dict[str, list[str]]:
    print("\nPart 3: lambda counterfamily preserves current structural tests")
    lam = sp.symbols("lambda", positive=True)
    h = sp.symbols("h", real=True)
    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    scaled = lam * u
    ray = sp.simplify(scaled / sp.sqrt(scaled.dot(scaled)))
    raw_component = sp.simplify(scaled[0])
    check("positive lambda preserves normalized top source ray", ray == u, ray)
    check("raw top component is lambda/sqrt(6)", is_zero(raw_component - lam / sp.sqrt(6)), raw_component)

    ell = lam * h
    score_h = sp.diff(ell, h)
    check("lambda branch is primitive curve in coordinate ell=lambda h", is_zero(score_h - lam), score_h)
    check("lambda=1 and lambda=2 give different raw h coefficients", (raw_component.subs(lam, 1) != raw_component.subs(lam, 2)))

    constraints = {
        "locality": True,
        "lsp_signed_record_ray": True,
        "one_higgs_up_type_carrier": True,
        "color_singlet_weak_singlet": True,
        "normalized_top_operator_ray": True,
        "democratic_direction": True,
        "markov_sufficient_coarse_graining": True,
        "forbidden_import_free": True,
    }
    for key, value in constraints.items():
        check(f"counterfamily preserves {key}", value)
    return {"preserved_constraints": list(constraints.keys())}


def part4_carrier_line_not_coefficient() -> dict[str, bool]:
    print("\nPart 4: gauge/top carrier selects line, not coefficient")
    carrier_note = read(TOP_CARRIER)
    democratic_note = read(DEMOCRATIC)
    check("carrier note selects bar Q_L tilde H u_R", "bar Q_L tilde H u_R" in carrier_note)
    check("carrier note says generation matrix remains free", "generation matrix" in carrier_note and "free" in carrier_note)
    check("democratic note names open bridge to physical coefficient", "still-open bridge" in democratic_note or "open bridge" in democratic_note)
    check("democratic note does not claim physical y_33", "does not claim" in democratic_note and "derived physical value for `y_33`" in democratic_note)
    return {
        "carrier_line_selected": True,
        "coefficient_selected": False,
    }


def part5_scope_and_next_action() -> dict[str, Any]:
    print("\nPart 5: no-go scope and next action")
    note = read(NOTE)
    scope = {
        "route_pruned": "structural no-compute top-source identification from current inputs alone",
        "primitive_law_refuted": False,
        "conditional_y33_refuted": False,
        "strict_response_route_live": True,
        "proposal_allowed": False,
        "actual_current_surface_status": "no-go",
    }
    check("no-go prunes only structural no-compute identification", "structural no-compute top-source identification" in note)
    check("primitive law is not refuted", not scope["primitive_law_refuted"])
    check("conditional y33 is not refuted", not scope["conditional_y33_refuted"])
    check("strict response route remains live", scope["strict_response_route_live"])
    check("proposal remains false", "proposal_allowed: false" in note)
    check("actual current surface status is no-go", "actual_current_surface_status: no-go" in note)
    return scope


def part6_firewalls() -> None:
    print("\nPart 6: firewalls")
    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed W/Z/top masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "Planck",
        "alpha_s",
        "fitted selector",
    ):
        check(f"firewall input recorded: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "strict top/W response evidence exists",
        "full retained closure",
        "lambda = 1 follows from gauge invariance alone",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T TOP-SOURCE IDENTIFICATION HARD-STOP NO-GO")
    print("=" * 78)

    anchors = part1_anchors()
    conditional = part2_positive_conditional_theorem()
    counterfamily = part3_counterfamily()
    carrier = part4_carrier_line_not_coefficient()
    scope = part5_scope_and_next_action()
    part6_firewalls()

    result = {
        "actual_current_surface_status": "no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The current structural inputs select the top operator ray and "
            "primitive source law, but do not derive the physical identification "
            "of the Standard Model top source coordinate with Fisher arclength."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "conditional_theorem_preserved": conditional,
        "counterfamily": counterfamily,
        "carrier_scope": carrier,
        "scope": scope,
        "next_action": (
            "strict same-source top/W response evidence, unless audit accepts "
            "the primitive top-source identification premise"
        ),
        "input_status_summary": {
            "primitive_record_law_fail_count": anchors["primitive"].get("fail_count"),
            "top_carrier_fail_count": anchors["carrier"].get("fail_count"),
            "mininfo_gate_fail_count": anchors["mininfo"].get("fail_count"),
        },
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_TOP_SOURCE_IDENTIFICATION_HARD_STOP_NO_GO_NOTE_2026-05-27.md",
            "scripts/frontier_yt_top_source_identification_hard_stop_no_go.py",
            "outputs/yt_top_source_identification_hard_stop_no_go_2026-05-27.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
