#!/usr/bin/env python3
"""Y_T source-measure Tier-A source-unit boundary gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = ROOT / "outputs" / "yt_source_measure_tier_a_source_unit_boundary_2026-05-30.json"

NOTE = DOCS / "YT_SOURCE_MEASURE_TIER_A_SOURCE_UNIT_BOUNDARY_NOTE_2026-05-30.md"
TIER_A_YT = DOCS / "YT_TIER_A_SOURCE_ACTION_TOP_PREMISE_CLOSURE_NOTE_2026-05-29.md"
DEMOCRATIC = DOCS / "YT_QUBIT_DEMOCRATIC_TOP_COEFFICIENT_CANDIDATE_NOTE_2026-05-25.md"
SOURCE_ACTION = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
LSP_SOURCE = DOCS / "YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md"
SOURCE_COV = DOCS / "YT_SOURCE_COVARIANCE_NORMALIZATION_SUPPORT_NOTE_2026-05-24.md"
WZ_PACKET = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
TOP_RATIO = DOCS / "YT_SOURCE_COORDINATE_INVARIANT_TOP_W_RATIO_GATE_NOTE_2026-05-25.md"
EW_INTERTWINER = DOCS / "YT_EW_HIGGS_SOURCE_INTERTWINER_GATE_NOTE_2026-05-25.md"
PCAL_SYNTHESIS = DOCS / "SOURCE_MEASURE_PCAL_RETIREMENT_SYNTHESIS_NOTE_2026-05-30.md"
LOG_BOUNDARY = DOCS / "SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md"
TIER_A_REGISTRY = DOCS / "audit" / "data" / "premise_decision_history.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

AUDIT_ROOTS = [
    "yt_tier_a_source_action_top_premise_closure_note_2026-05-29",
    "yt_primitive_source_unit_fisher_normalization_support_note_2026-05-25",
    "yt_operational_source_action_bridge_theorem_attempt_note_2026-05-25",
    "yt_strict_symbolic_top_response_row_packet_note_2026-05-25",
    "yt_fh_top_w_response_ratio_gate_note_2026-05-25",
    "sm_one_higgs_yukawa_gauge_selection_theorem_note_2026-04-26",
    "standard_model_hypercharge_uniqueness_theorem_note_2026-04-24",
]

RETAINED_GRADE_BOUNDED_SUPPORT = [
    "yt_qubit_democratic_top_coefficient_candidate_note_2026-05-25",
    "yt_lsp_signed_record_source_readout_support_note_2026-05-24",
    "yt_source_covariance_normalization_support_note_2026-05-24",
    "yt_source_action_support_packet_note_2026-05-22",
    "yt_strict_wz_neutral_carrier_response_packet_note_2026-05-25",
    "yt_source_coordinate_invariant_top_w_ratio_gate_note_2026-05-25",
    "yt_ew_higgs_source_intertwiner_gate_note_2026-05-25",
]

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


def zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def ledger_rows() -> dict[str, dict[str, Any]]:
    data = json.loads(read(LEDGER))["rows"]
    iterable = data.values() if isinstance(data, dict) else data
    return {row.get("claim_id"): row for row in iterable if isinstance(row, dict)}


def part1_documents() -> dict[str, Any]:
    print("\nPart 1: documents and source boundary")
    for path in (
        NOTE,
        TIER_A_YT,
        DEMOCRATIC,
        SOURCE_ACTION,
        LSP_SOURCE,
        SOURCE_COV,
        WZ_PACKET,
        TOP_RATIO,
        EW_INTERTWINER,
        PCAL_SYNTHESIS,
        LOG_BOUNDARY,
        TIER_A_REGISTRY,
        LEDGER,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Statement",
        "Load-Bearing Chain",
        "Why This Is Not The Old Ward/H-Unit Trap",
        "Bounded Claim Boundary",
        "Rows That Still Need Audit Or Repair",
        "Relation To P-Cal Release Work",
        "Non-Claims",
        "Boundary Summary",
    ):
        check(f"package note contains section: {phrase}", phrase in note)

    check("package keeps audit status authority independent", "independent audit lane only" in note)
    check("package does not claim a unilateral status change", "no unilateral status change is claimed here" in note)
    conditional_key = "conditional_" + "surface_status"
    proposal_key = "proposal_" + "allowed"
    check("package avoids retained-status promotion language", conditional_key not in note and proposal_key not in note)

    tier = read(TIER_A_YT)
    check("YT note states the calculation is conditional", "Conditionally. Under the explicit open source-measure hypothesis" in tier)
    check("YT note computes lambda=1 under that hypothesis", "lambda = 1" in tier and "y_33 = 1 / sqrt(6)" in tier)
    check("YT note does not claim premise closure", "supplies no premise" in tier)

    pcal = read(PCAL_SYNTHESIS)
    boundary = read(LOG_BOUNDARY)
    check(
        "P-cal synthesis names narrow source-measure bridge",
        "semantic bridge" in pcal and "smooth sharp-record probability intervention" in pcal,
    )
    check("log boundary keeps finite-record-alone route pruned", "finite record-intervention theorem alone retires P-cal" in boundary)

    return {
        "source_boundary": "Tier-A source-measure surface only",
        "status_authority": "independent audit lane only",
    }


def part2_ledger_statuses() -> dict[str, Any]:
    print("\nPart 2: ledger status boundary")
    rows = ledger_rows()
    support_statuses = {}
    for cid in RETAINED_GRADE_BOUNDED_SUPPORT:
        row = rows.get(cid)
        status = None if row is None else row.get("effective_status")
        audit = None if row is None else row.get("audit_status")
        support_statuses[cid] = {"effective_status": status, "audit_status": audit}
        check(f"{cid} is retained-grade bounded support", status == "retained_bounded" and audit == "audited_clean", support_statuses[cid])

    root_statuses = {}
    for cid in AUDIT_ROOTS:
        row = rows.get(cid)
        status = None if row is None else row.get("effective_status")
        audit = None if row is None else row.get("audit_status")
        root_statuses[cid] = {"effective_status": status, "audit_status": audit}
        check(f"{cid} is present", row is not None)
        check(f"{cid} is not silently promoted", status != "retained", root_statuses[cid])

    tier_registry = json.loads(read(TIER_A_REGISTRY))
    derivation_targets = tier_registry.get("derivation_targets", {})
    check("decision history contains no live P1 premise", "observable_principle_from_axiom_note" not in derivation_targets)
    check("decision history is non-authoritative", "Non-authoritative" in tier_registry.get("description", ""))
    return {"support_statuses": support_statuses, "root_statuses": root_statuses}


def part3_algebra() -> dict[str, str]:
    print("\nPart 3: source-side algebra")
    lam = sp.symbols("lambda", positive=True)
    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    norm = sp.simplify(u.dot(u))
    y33_lambda = sp.simplify(lam * u[0])
    fisher_lambda = sp.simplify((lam * u).dot(lam * u))

    check("democratic six-component top source is unit", zero(norm - 1), norm)
    check("top component of unit source is 1/sqrt(6)", zero(u[0] - 1 / sp.sqrt(6)), u[0])
    check("scaled top source has Fisher norm lambda^2", zero(fisher_lambda - lam**2), fisher_lambda)
    check("scaled top coefficient is lambda/sqrt(6)", zero(y33_lambda - lam / sp.sqrt(6)), y33_lambda)
    check("Tier-A primitive source unit selects lambda=1", sp.solve(sp.Eq(fisher_lambda, 1), lam) == [1])
    check("selected Y_T source-side coefficient is 1/sqrt(6)", zero(y33_lambda.subs(lam, 1) - 1 / sp.sqrt(6)), y33_lambda.subs(lam, 1))

    return {
        "unit_vector": "(1,1,1,1,1,1)/sqrt(6)",
        "fisher_scaled": "lambda^2",
        "tier_a_selected": "lambda=1",
        "source_side_result": "y_33=1/sqrt(6)",
    }


def part4_firewalls() -> None:
    print("\nPart 4: firewalls and overclaim checks")
    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed top/W/Z masses",
        "PDG targets",
        "`alpha_LM`",
        "plaquette/u0",
        "fitted selectors",
    ):
        check(f"package firewall names forbidden input: {phrase}", phrase in note)

    for phrase in (
        "actual_current_surface_status: retained",
        "bare_retained_allowed: true",
        "proposal_allowed: true",
        "unbounded Y_T closure is proved",
        "P-cal/P1 is derived from A1+A2",
        "strict same-source top/W pole-response evidence is produced",
        "old Ward chain is repaired",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("Y_T SOURCE-MEASURE TIER-A SOURCE-UNIT BOUNDARY")
    print("=" * 88)

    result = {
        "documents": part1_documents(),
        "ledger": part2_ledger_statuses(),
        "algebra": part3_algebra(),
    }
    part4_firewalls()

    result["summary"] = {
        "pass": PASS_COUNT,
        "fail": FAIL_COUNT,
        "source_boundary": "Tier-A source-measure surface only",
        "status_authority": "independent audit lane only",
        "tier_a_input": "P-cal/source-measure primitive normalized RN/Fisher coordinate",
        "closed_on_tier_a_surface": ["lambda=1", "y_33=1/sqrt(6)"],
        "not_closed_unbounded": [
            "P-cal/P1 derivation or native RN/Fisher source-measure acceptance",
            "strict same-source top/W pole-response evidence",
            "physical-scale g_2 and matching/running",
        ],
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
