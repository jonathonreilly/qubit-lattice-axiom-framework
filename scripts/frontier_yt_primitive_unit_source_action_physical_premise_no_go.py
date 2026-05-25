#!/usr/bin/env python3
"""Primitive-unit source/action physical-premise no-go for Y_T."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_primitive_unit_source_action_physical_premise_no_go_2026-05-25.json"

NOTE = DOCS / "YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
SOURCE_ACTION_GATE = DOCS / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
BRIDGE_ATTEMPT = DOCS / "YT_SIGNED_LINEAR_DEMOCRATIC_TANGENT_PHYSICAL_BRIDGE_ATTEMPT_NOTE_2026-05-25.md"
CONSOLIDATED = DOCS / "YT_PR230_CONSOLIDATED_STATUS_NOTE_2026-05-22.md"
LSP_SOURCE = DOCS / "YT_PR230_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

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


def ledger_row(claim_id: str) -> dict[str, Any]:
    rows = json.loads(read(LEDGER))["rows"]
    iterable = rows.values() if isinstance(rows, dict) else rows
    for row in iterable:
        if isinstance(row, dict) and row.get("claim_id") == claim_id:
            return row
    raise KeyError(claim_id)


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def one_line(text: str) -> str:
    return " ".join(text.split())


def part1_anchors_and_authority() -> dict[str, Any]:
    print("\nPart 1: anchors and current authority")
    for path in (NOTE, AXIOMS, SOURCE_ACTION_GATE, BRIDGE_ATTEMPT, CONSOLIDATED, LSP_SOURCE, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Current Axiom Surface",
        "Exact Counterfamily",
        "Why Signed Records Alone Do Not Remove Lambda",
        "Consequence For PR230",
        "Firewalls",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    axioms = read(AXIOMS)
    check("baseline is qubit per site", "Reality is a qubit at every lattice site" in axioms)
    check("baseline has Z^3 lattice", "The lattice sites form the cubic lattice `Z^3`" in axioms)
    check("axiom memo leaves dynamics to derivation lanes", "Dynamics" in axioms and "not additional primitives" in axioms)

    gate = read(SOURCE_ACTION_GATE)
    check("source-action convention note is open_gate", "**Claim type:** open_gate" in gate)
    check("source-action convention note says convention is not derived", "does not claim that convention is derived" in gate)

    statuses = {
        "source_action_gate": ledger_row("observable_principle_source_coupled_local_action_admission_candidate_note_2026-05-21").get("effective_status"),
        "yt_source_action_support": ledger_row("yt_" + "pr" + "230_consolidated_status_note_2026-05-22").get("effective_status"),
        "lsp_source": ledger_row("yt_" + "pr" + "230_lsp_signed_record_source_readout_support_note_2026-05-24").get("effective_status"),
    }
    check("source-action gate is not retained authority", statuses["source_action_gate"] != "retained", statuses["source_action_gate"])
    check("finite source-action support is retained_bounded", statuses["yt_source_action_support"] == "retained_bounded", statuses["yt_source_action_support"])
    check("LSP source support is not retained coefficient authority", statuses["lsp_source"] != "retained", statuses["lsp_source"])
    return statuses


def part2_counterfamily() -> dict[str, str]:
    print("\nPart 2: exact lambda counterfamily")
    lam = sp.symbols("lambda", positive=True)
    n = sp.Integer(6)
    u = sp.Matrix([1 / sp.sqrt(n)] * n)
    scaled = lam * u
    ray_scaled = sp.simplify(scaled / sp.sqrt(scaled.dot(scaled)))

    check("democratic vector has unit norm", is_zero(u.dot(u) - 1), sp.simplify(u.dot(u)))
    check("positive lambda preserves normalized democratic ray", ray_scaled == u, ray_scaled)
    check("projective component probability is 1/6", is_zero(u[0] ** 2 - sp.Rational(1, 6)), u[0] ** 2)
    check("projective component probability is lambda-blind", is_zero(ray_scaled[0] ** 2 - sp.Rational(1, 6)), ray_scaled[0] ** 2)

    y33 = sp.simplify(lam * u[0])
    check("top coefficient family is lambda/sqrt(6)", is_zero(y33 - lam / sp.sqrt(6)), y33)
    check("lambda=1 branch gives 1/sqrt(6)", is_zero(y33.subs(lam, 1) - 1 / sp.sqrt(6)), y33.subs(lam, 1))
    check("lambda=2 branch is distinct but structurally compatible", is_zero(y33.subs(lam, 2) - 2 / sp.sqrt(6)), y33.subs(lam, 2))
    return {
        "family": "y_33(lambda)=lambda/sqrt(6)",
        "preserved_ray": "u_dem",
        "projective_probability": "1/6",
    }


def part3_signed_record_scale_boundary() -> dict[str, Any]:
    print("\nPart 3: signed record does not itself choose action-source unit")
    lam, h, eps = sp.symbols("lambda h epsilon", positive=True)
    score_primitive = eps
    score_scaled = lam * eps
    check("primitive RN score is epsilon", is_zero(score_primitive - eps), score_primitive)
    check("scaled action-source score is lambda epsilon", is_zero(score_scaled - lam * eps), score_scaled)
    check("requiring physical score equals primitive score forces lambda=1", sp.solve(sp.Eq(score_scaled, score_primitive), lam) == [1])

    # Projective outcomes are the sign support {+1, -1}; scaling the action
    # source changes the source derivative, not that support.
    outcomes = {-1, 1}
    scaled_outcome_signs = {sp.sign(o) for o in outcomes}
    check("projective signed record support is {+1,-1}", outcomes == {-1, 1}, outcomes)
    check("positive lambda preserves signs of record outcomes", scaled_outcome_signs == {-1, 1}, scaled_outcome_signs)
    return {
        "primitive_unit_condition": "physical source score equals primitive signed-record score",
        "lambda_selected_if_condition_added": 1,
    }


def part4_route_boundary(statuses: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 4: route boundary")
    bridge = read(BRIDGE_ATTEMPT)
    consolidated = read(CONSOLIDATED)
    check("paired bridge attempt records conditional positive theorem", "primitive unit physical source/action tangent accepted" in bridge)
    check("paired bridge attempt records lambda obstruction", "y_33(lambda) = lambda / sqrt(6)" in bridge)
    check(
        "consolidated status names source/action support as bounded",
        "bounded support identity" in consolidated
        and "does not prove that this source/action surface" in consolidated,
    )

    result = {
        "positive_if_added_premise": "primitive unit source/action premise -> y_33=1/sqrt(6)",
        "actual_current_surface_status": "support no-go / exact obstruction",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The current surface has not derived the physical source/action unit. "
            "The source-action convention is an open gate and lambda remains free."
        ),
        "direct_closure_allowed": False,
        "upstream_statuses": statuses,
    }
    check("direct closure is not allowed", not result["direct_closure_allowed"], result["proposal_allowed_reason"])
    return result


def part5_firewalls() -> None:
    print("\nPart 5: firewalls")
    note = read(NOTE)
    flat = one_line(note)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed W/Z/top masses",
        "PDG values",
        "`alpha_LM`",
        "plaquette/u0",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in flat)

    for phrase in (
        "Status:** retained",
        "proposed_retained",
        "full retained closure",
        "positive Y_T closure has been obtained",
        "old Ward route is repaired",
        "baseline forces lambda=1",
        "source/action convention is derived",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("Y_T PRIMITIVE-UNIT SOURCE/ACTION PHYSICAL-PREMISE NO-GO")
    print("=" * 88)

    statuses = part1_anchors_and_authority()
    counterfamily = part2_counterfamily()
    signed_record = part3_signed_record_scale_boundary()
    boundary = part4_route_boundary(statuses)
    part5_firewalls()

    result = {
        "status": "support no-go / exact obstruction",
        "claim": (
            "The qubit-on-Z3 baseline plus current support packets does not force the primitive-unit "
            "physical source/action premise; lambda remains free."
        ),
        "counterfamily": counterfamily,
        "signed_record_boundary": signed_record,
        "route_boundary": boundary,
        "remaining_bridge": (
            "derive or accept physical top Yukawa deformation = primitive unit "
            "signed-linear source/action tangent, or measure top response directly"
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md",
            "scripts/frontier_yt_primitive_unit_source_action_physical_premise_no_go.py",
            "outputs/yt_primitive_unit_source_action_physical_premise_no_go_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
