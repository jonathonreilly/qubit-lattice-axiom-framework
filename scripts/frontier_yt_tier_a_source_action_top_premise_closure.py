#!/usr/bin/env python3
"""Y_T source-action conditional-calculation runner.

Verifies the narrow claim:

  explicit open source-measure/P-cal hypothesis
    + normalized top source operator
    -> primitive RN/Fisher source coordinate
    -> lambda = 1
    -> y_33 = 1/sqrt(6)

It also verifies the status boundary: the result is conditional support, not
retained Y_T closure or premise supply.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_tier_a_source_action_top_premise_closure_2026-05-29.json"

NOTE = DOCS / "YT_TIER_A_SOURCE_ACTION_TOP_PREMISE_CLOSURE_NOTE_2026-05-29.md"
DECISION_HISTORY = DOCS / "audit" / "data" / "premise_decision_history.json"
AXIOM_PREMISE_REGISTRY = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
HISTORICAL_INDEX = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
P1P2_SYNTHESIS = DOCS / "OBSERVABLE_PRINCIPLE_P1P2_TWO_STAGE_SYNTHESIS_NARROW_THEOREM_NOTE_2026-05-28.md"
SOURCE_ACTION_CANDIDATE = DOCS / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
LSP_SOURCE = DOCS / "YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md"
SOURCE_COV = DOCS / "YT_SOURCE_COVARIANCE_NORMALIZATION_SUPPORT_NOTE_2026-05-24.md"
FISHER_SOURCE = DOCS / "YT_PRIMITIVE_SOURCE_UNIT_FISHER_NORMALIZATION_SUPPORT_NOTE_2026-05-25.md"
OPERATIONAL_SOURCE = DOCS / "YT_OPERATIONAL_SOURCE_ACTION_BRIDGE_THEOREM_ATTEMPT_NOTE_2026-05-25.md"
PHYSICAL_TOP_CANDIDATE = DOCS / "YT_PHYSICAL_TOP_INTERVENTION_IDENTIFICATION_CANDIDATE_NOTE_2026-05-25.md"
UNIT_SOURCE_NOGO = DOCS / "YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md"
SOURCE_SCALE_BOUNDARY = DOCS / "YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
PLANCK_SOURCE_UNIT = DOCS / "PLANCK_SOURCE_UNIT_NORMALIZATION_SUPPORT_THEOREM_NOTE_2026-04-25.md"
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


def ledger_row(claim_id: str) -> dict[str, Any] | None:
    rows = json.loads(read(LEDGER))["rows"]
    if isinstance(rows, dict):
        return rows.get(claim_id)
    for row in rows:
        if isinstance(row, dict) and row.get("claim_id") == claim_id:
            return row
    return None


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchor_status() -> dict[str, Any]:
    print("\nPart 1: anchors and status boundary")
    required = (
        NOTE,
        DECISION_HISTORY,
        AXIOM_PREMISE_REGISTRY,
        HISTORICAL_INDEX,
        P1P2_SYNTHESIS,
        SOURCE_ACTION_CANDIDATE,
        LSP_SOURCE,
        SOURCE_COV,
        FISHER_SOURCE,
        OPERATIONAL_SOURCE,
        PHYSICAL_TOP_CANDIDATE,
        UNIT_SOURCE_NOGO,
        SOURCE_SCALE_BOUNDARY,
        PLANCK_SOURCE_UNIT,
        LEDGER,
    )
    for path in required:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Question",
        "Answer",
        "Finite RN Proof",
        "Top Operator Application",
        "Relation To The Current No-Go",
        "Relation To Planck And Scale Setting",
        "Claim-Status Certificate",
        "Non-Claims",
    ):
        check(f"note contains section/phrase: {phrase}", phrase in note)

    registry = json.loads(read(DECISION_HISTORY))
    axiom_registry = json.loads(read(AXIOM_PREMISE_REGISTRY))
    derivation_targets = registry.get("derivation_targets", {})
    conventions = registry.get("conventions", {})
    reclassified_primitives = registry.get("reclassified_primitives", {})
    check("decision history contains no live P1 premise", "observable_principle_from_axiom_note" not in derivation_targets)
    check("decision history is non-authoritative", "Non-authoritative" in registry.get("description", ""))
    check("scale reference is not an admission target", "scale_reference_primitive" not in derivation_targets)
    check("scale reference moved to approved primitive registry", "scale_reference_primitive" in axiom_registry.get("canonical_ids", []))
    check("history preserves scale primitive reclassification provenance", "scale_reference_primitive" in reclassified_primitives)
    check("g0 convention is not an accepted derivation target", "g_bare_rigidity_theorem_note" in conventions)

    p1p2 = read(P1P2_SYNTHESIS)
    p1p2_lower = p1p2.lower()
    check("P1P2 synthesis names P-cal residual", "P-cal" in p1p2)
    check(
        "P1P2 synthesis does not close parent scalar-additivity premise",
        "does not close the parent scalar-additivity premise" in p1p2_lower
        or "does **not** close the parent scalar-additivity premise" in p1p2_lower,
    )

    source_candidate = read(SOURCE_ACTION_CANDIDATE)
    check("source/action candidate states action derivatives define insertions", "Local source derivatives of `S` define the local operator insertions" in source_candidate)
    check("source/action candidate is open_gate, not unilateral closure", "open_gate" in source_candidate and "not as a unilateral foundation change" in source_candidate)

    rows = {
        "lsp_source": ledger_row("yt_lsp_signed_record_source_readout_support_note_2026-05-24"),
        "source_cov": ledger_row("yt_source_covariance_normalization_support_note_2026-05-24"),
        "unit_source_nogo": ledger_row("yt_primitive_unit_source_action_physical_premise_no_go_note_2026-05-25"),
        "source_scale_boundary": ledger_row("yt_lsp_source_scale_boundary_and_strict_response_contract_note_2026-05-26"),
    }
    check("LSP source context row is present", rows["lsp_source"] is not None)
    check("source covariance context row is present", rows["source_cov"] is not None)
    check(
        "primitive unit source/action no-go row is present and non-positive",
        rows["unit_source_nogo"] and rows["unit_source_nogo"].get("claim_type") == "no_go"
        and rows["unit_source_nogo"].get("effective_status") != "retained",
        None if rows["unit_source_nogo"] is None else rows["unit_source_nogo"].get("effective_status"),
    )
    check(
        "source-scale boundary row does not claim unbounded closure",
        rows["source_scale_boundary"] is None or rows["source_scale_boundary"].get("effective_status") != "retained",
        None if rows["source_scale_boundary"] is None else rows["source_scale_boundary"].get("effective_status"),
    )
    return {
        "historical_p1_record": derivation_targets.get("observable_principle_from_axiom_note", {}),
        "scale_reference_primitive": axiom_registry.get("nodes", {}).get("scale_reference_primitive", {}),
        "ledger_statuses": {k: None if v is None else v.get("effective_status") for k, v in rows.items()},
    }


def part2_rn_source_unit() -> dict[str, str]:
    print("\nPart 2: finite RN/Fisher source unit")
    eps, h = sp.symbols("epsilon h", real=True)
    lam = sp.symbols("lambda", positive=True)
    # For a signed record epsilon^2 = 1, the primitive exponential family at
    # h=0 has score epsilon and Fisher E[epsilon^2] = 1.
    score = eps
    fisher = sp.simplify(score**2).subs(eps**2, 1)
    scaled_score = lam * eps
    scaled_fisher = sp.simplify(scaled_score**2).subs(eps**2, 1)
    check("primitive signed source score is epsilon", score == eps, score)
    check("primitive Fisher norm is one", fisher == 1, fisher)
    check("scaled score is lambda epsilon", scaled_score == lam * eps, scaled_score)
    check("scaled Fisher norm is lambda^2", scaled_fisher == lam**2, scaled_fisher)
    check("lambda=1 is forced by primitive Fisher unit", sp.solve(sp.Eq(scaled_fisher, 1), lam) == [1], sp.solve(sp.Eq(scaled_fisher, 1), lam))

    # Action/log-density identity: P_h = R_h P_0 with R_h=exp(h O)/Z gives
    # S_h = S_0 - h O + c(h)I.  The non-identity derivative is -O.
    O, S0, c = sp.symbols("O S_0 c_h")
    S_h = S0 - h * O + c
    dS = sp.diff(S_h, h)
    check("source/action derivative gives -O modulo identity", dS == -O, dS)
    scaled_S_h = S0 - h * lam * O + c
    scaled_dS = sp.diff(scaled_S_h, h)
    check("scaled source/action derivative gives -lambda O", scaled_dS == -lam * O, scaled_dS)
    return {
        "primitive_score": "epsilon",
        "primitive_fisher_norm": "1",
        "scaled_fisher_norm": "lambda^2",
        "action_derivative": "-O modulo identity",
    }


def part3_top_operator() -> dict[str, str]:
    print("\nPart 3: normalized six-component top operator")
    lam = sp.symbols("lambda", positive=True)
    u = sp.Matrix([sp.sqrt(sp.Rational(1, 6))] * 6)
    norm_sq = sp.simplify((u.T * u)[0])
    component = u[0]
    y_lambda = sp.simplify(lam * component)
    check("six-component top vector is unit normalized", norm_sq == 1, norm_sq)
    check("each component is 1/sqrt(6)", is_zero(component - 1 / sp.sqrt(6)), component)
    check("lambda family is lambda/sqrt(6)", is_zero(y_lambda - lam / sp.sqrt(6)), y_lambda)
    check("conditional unit-source hypothesis gives y=1/sqrt(6)", is_zero(y_lambda.subs(lam, 1) - 1 / sp.sqrt(6)), y_lambda.subs(lam, 1))

    # Projective probabilities do not select lambda: the normalized ray is
    # independent of positive lambda.
    scaled = lam * u
    ray = sp.simplify(scaled / sp.sqrt((scaled.T * scaled)[0]))
    check("positive lambda preserves normalized top source ray", ray == u, ray)
    check("projective component probability remains 1/6", is_zero(ray[0] ** 2 - sp.Rational(1, 6)), ray[0] ** 2)
    return {
        "unit_top_operator": "sum_i O_i/sqrt(6)",
        "lambda_family": "lambda/sqrt(6)",
        "conditional_unit_branch": "lambda=1",
    }


def part4_planck_scope() -> dict[str, str]:
    print("\nPart 4: Planck/scale scope")
    planck = read(PLANCK_SOURCE_UNIT)
    note = read(NOTE)
    check("Planck source-unit theorem separates bare and physical source unit", "bare source coefficient" in planck and "physical source unit" in planck)
    check("Planck source-unit theorem is not standalone minimal-stack closure", "not a standalone minimal-stack closure" in planck)
    note_flat = one_line(note)
    check("Y_T note treats Planck as context-only", "Context-only input" in note and "not used to prove the dimensionless Y_T coefficient" in note_flat)
    check("Y_T note says Planck does not determine dimensionless top Yukawa", "does not determine the dimensionless top Yukawa normalization" in note)
    return {
        "planck_role": "dimensionful scale/source-unit analogy only",
        "yt_dimensionless_proof_input": "not Planck",
    }


def part5_firewalls() -> dict[str, Any]:
    print("\nPart 5: firewalls and claim status")
    note = read(NOTE)
    flat = one_line(note)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed top/W/Z masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "Planck, alpha_s, or a fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in flat)

    forbidden_overclaims = (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives P-cal/P1 from the two axioms",
        "P-cal/P1 is derived from the two axioms",
        "strict same-source top/W pole-response evidence has been produced",
        "bare_retained_allowed: true",
        "proposal_allowed: true",
    )
    for phrase in forbidden_overclaims:
        check(f"forbidden overclaim absent: {phrase}", phrase not in flat)

    required_status = (
        "actual_current_surface_status: bounded-support",
        "trace_class: direct_blocker_closure",
        "reachability_to_target: partially_closes",
        "proposal_allowed: false",
        "bare_retained_allowed: false",
    )
    for phrase in required_status:
        check(f"status certificate records: {phrase}", phrase in note)
    return {
        "actual_current_surface_status": "bounded-support",
        "trace_class": "direct_blocker_closure",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
    }


def main() -> int:
    status = part1_anchor_status()
    rn = part2_rn_source_unit()
    top = part3_top_operator()
    planck = part4_planck_scope()
    claim = part5_firewalls()
    result = {
        "claim": "open source-measure hypothesis gives lambda=1 conditionally for the normalized top source",
        "actual_current_surface_status": "bounded-support",
        "trace_class": "direct_blocker_closure",
        "reachability_to_target": "partially_closes",
        "conditional_calculation_result": {
            "lambda": "1",
            "y_33": "1/sqrt(6)",
        },
        "not_closed_unbounded": [
            "P-cal/P1 derivation from A1+A2",
            "strict same-source top/W pole-response certificate",
        ],
        "status": status,
        "rn_source_unit": rn,
        "top_operator": top,
        "planck_scope": planck,
        "claim_status_certificate": claim,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
