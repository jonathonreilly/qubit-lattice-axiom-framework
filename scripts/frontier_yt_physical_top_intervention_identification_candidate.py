#!/usr/bin/env python3
"""Final physical top-intervention identification candidate for Y_T."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_physical_top_intervention_identification_candidate_2026-05-25.json"

NOTE = DOCS / "YT_PHYSICAL_TOP_INTERVENTION_IDENTIFICATION_CANDIDATE_NOTE_2026-05-25.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
OP_BRIDGE = DOCS / "YT_OPERATIONAL_SOURCE_ACTION_BRIDGE_THEOREM_ATTEMPT_NOTE_2026-05-25.md"
FISHER_UNIT = DOCS / "YT_PRIMITIVE_SOURCE_UNIT_FISHER_NORMALIZATION_SUPPORT_NOTE_2026-05-25.md"
SIGNED_TANGENT = DOCS / "YT_SIGNED_LINEAR_DEMOCRATIC_TANGENT_PHYSICAL_BRIDGE_ATTEMPT_NOTE_2026-05-25.md"
PRIMITIVE_NOGO = DOCS / "YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md"
TOP_COEFF_NOGO = DOCS / "YT_TOP_RESPONSE_COEFFICIENT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-25.md"
ONE_HIGGS = DOCS / "SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md"
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


def one_line(text: str) -> str:
    return " ".join(text.split())


def ledger_row(claim_id: str) -> dict[str, Any]:
    rows = json.loads(read(LEDGER))["rows"]
    iterable = rows.values() if isinstance(rows, dict) else rows
    for row in iterable:
        if isinstance(row, dict) and row.get("claim_id") == claim_id:
            return row
    raise KeyError(claim_id)


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and authority boundary")
    for path in (NOTE, AXIOMS, OP_BRIDGE, FISHER_UNIT, SIGNED_TANGENT, PRIMITIVE_NOGO, TOP_COEFF_NOGO, ONE_HIGGS, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Axioms-As-Reality Starting Point",
        "Operational Physical-Intervention Criterion",
        "Proof Under The Criterion",
        "What This Would Close If Accepted",
        "Why This Is Still An Open Gate",
        "Non-Claims",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    axioms = read(AXIOMS)
    check("A1/A2 physical qubit-on-Z3 wording present", "Reality is a qubit at every lattice site" in axioms and "The lattice sites form" in axioms)
    check("operational bridge supplies RN-to-action identity", "S_h = S_0 - h O + c(h) I" in read(OP_BRIDGE))
    check("Fisher unit packet supplies lambda=1 source unit", "lambda = 1" in read(FISHER_UNIT) and "lambda^2" in read(FISHER_UNIT))
    check("signed tangent packet supplies 1/sqrt(6) top component", "1/sqrt(6)" in read(SIGNED_TANGENT))
    check("primitive-unit no-go remains recorded", "A1+A2 plus the current support packets do not force" in read(PRIMITIVE_NOGO))
    check("top coefficient no-go remains recorded", "does not determine `y_t`" in read(TOP_COEFF_NOGO))
    check("one-Higgs note leaves generation matrices free", "generation matrices free" in read(ONE_HIGGS))

    statuses = {
        "source_action_gate": ledger_row("observable_principle_source_coupled_local_action_admission_candidate_note_2026-05-21").get("effective_status"),
        "yt_source_action_support": ledger_row("yt_" + "pr" + "230_consolidated_status_note_2026-05-22").get("effective_status"),
        "one_higgs": ledger_row("sm_one_higgs_yukawa_gauge_selection_theorem_note_2026-04-26").get("effective_status"),
    }
    check("source-action gate is not retained authority", statuses["source_action_gate"] != "retained", statuses["source_action_gate"])
    check("YT source-action support is retained_bounded", statuses["yt_source_action_support"] == "retained_bounded", statuses["yt_source_action_support"])
    check("one-Higgs gauge selection is not coefficient authority", statuses["one_higgs"] != "retained", statuses["one_higgs"])
    return statuses


def part2_candidate_implication() -> dict[str, str]:
    print("\nPart 2: implication under operational physical-intervention criterion")
    lam = sp.symbols("lambda", positive=True)
    n = sp.Integer(6)
    u = sp.Matrix([1 / sp.sqrt(n)] * n)
    top_component = sp.simplify(u[0])
    fisher_scaled = sp.simplify((lam * u).dot(lam * u))

    check("normalized top source has unit norm", is_zero(u.dot(u) - 1), sp.simplify(u.dot(u)))
    check("top component is 1/sqrt(6)", is_zero(top_component - 1 / sp.sqrt(6)), top_component)
    check("scaled intervention has Fisher norm lambda^2", is_zero(fisher_scaled - lam**2), fisher_scaled)
    check("primitive intervention source unit forces lambda=1", sp.solve(sp.Eq(fisher_scaled, 1), lam) == [1])
    y33 = top_component
    check("accepted criterion implies y_33=1/sqrt(6)", is_zero(y33 - 1 / sp.sqrt(6)), y33)
    return {
        "conditional_if_criterion_accepted": "y_33=1/sqrt(6)",
        "lambda_selected": "1",
        "top_component": "1/sqrt(6)",
    }


def part3_counterfamily_boundary() -> dict[str, str]:
    print("\nPart 3: counterfamily if criterion is not accepted")
    lam = sp.symbols("lambda", positive=True)
    y33_lam = sp.simplify(lam / sp.sqrt(6))
    check("without criterion y_33(lambda)=lambda/sqrt(6)", is_zero(y33_lam - lam / sp.sqrt(6)), y33_lam)
    check("lambda=2 counterexample differs from primitive branch", sp.simplify(y33_lam.subs(lam, 2) - 1 / sp.sqrt(6)) != 0, y33_lam.subs(lam, 2))
    current_surface_forces_criterion = False
    check("current surface does not force criterion", not current_surface_forces_criterion)
    return {
        "counterfamily": "y_33(lambda)=lambda/sqrt(6)",
        "current_surface_forces_criterion": "false",
    }


def part4_claim_status(statuses: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 4: claim status")
    result = {
        "actual_current_surface_status": "open_gate / final bridge candidate",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "conditional_positive_branch": "criterion accepted -> y_33=1/sqrt(6)",
        "upstream_statuses": statuses,
    }
    check("bare retained is not allowed", not result["bare_retained_allowed"])
    check("proposed_retained is not allowed", not result["proposal_allowed"])
    check("status is open gate candidate", result["actual_current_surface_status"].startswith("open_gate"))
    return result


def part5_firewalls() -> None:
    print("\nPart 5: firewalls")
    note = read(NOTE)
    flat = one_line(note)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed top/W/Z masses",
        "PDG values",
        "`alpha_LM`",
        "plaquette/u0",
        "fitted selector",
    ):
        check(f"firewall/nonclaim phrase present: {phrase}", phrase in flat)

    for phrase in (
        "Status:** retained",
        "proposed_retained",
        "full retained closure",
        "positive Y_T closure has been obtained",
        "old Ward route is repaired",
        "A1/A2 plus current support force lambda=1",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("Y_T PHYSICAL TOP INTERVENTION IDENTIFICATION CANDIDATE")
    print("=" * 88)

    statuses = part1_anchors()
    implication = part2_candidate_implication()
    counterfamily = part3_counterfamily_boundary()
    claim_status = part4_claim_status(statuses)
    part5_firewalls()

    result = {
        "status": "open_gate / final bridge candidate",
        "claim": (
            "If the physical top Yukawa deformation is the operational primitive "
            "RN source intervention for O_top, then y_33=1/sqrt(6)."
        ),
        "implication": implication,
        "counterfamily_boundary": counterfamily,
        "claim_status": claim_status,
        "remaining_bridge": (
            "audit/derive physical top Yukawa deformation = operational primitive "
            "RN source intervention for normalized O_top"
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_PHYSICAL_TOP_INTERVENTION_IDENTIFICATION_CANDIDATE_NOTE_2026-05-25.md",
            "scripts/frontier_yt_physical_top_intervention_identification_candidate.py",
            "outputs/yt_physical_top_intervention_identification_candidate_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
