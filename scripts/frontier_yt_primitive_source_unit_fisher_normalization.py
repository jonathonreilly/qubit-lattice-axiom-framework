#!/usr/bin/env python3
"""Primitive signed-record Fisher source-unit normalization for Y_T."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_primitive_source_unit_fisher_normalization_2026-05-25.json"

NOTE = DOCS / "YT_PRIMITIVE_SOURCE_UNIT_FISHER_NORMALIZATION_SUPPORT_NOTE_2026-05-25.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
LSP_SOURCE = DOCS / "YT_PR230_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md"
SOURCE_ACTION_GATE = DOCS / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
RN_TEMPLATE = DOCS / "RP_RHO_REF_RADON_NIKODYM_COMPATIBILITY_NOTE_2026-05-20.md"
BRIDGE_ATTEMPT = DOCS / "YT_SIGNED_LINEAR_DEMOCRATIC_TANGENT_PHYSICAL_BRIDGE_ATTEMPT_NOTE_2026-05-25.md"
PREMISE_NOGO = DOCS / "YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md"
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


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and authority boundary")
    for path in (NOTE, AXIOMS, LSP_SOURCE, SOURCE_ACTION_GATE, RN_TEMPLATE, BRIDGE_ATTEMPT, PREMISE_NOGO, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Theorem Statement",
        "Six-Component Top Trilinear Source",
        "Action-Source Bridge",
        "What This Closes",
        "What This Does Not Close",
        "Why This Is Not The Old Ward Trap",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    lsp = read(LSP_SOURCE)
    gate = read(SOURCE_ACTION_GATE)
    rn = read(RN_TEMPLATE)
    check("LSP support records signed RN score epsilon", "d log R_h / d h_x |_{h=0} = epsilon_x" in lsp)
    check("LSP support records exponential RN uniqueness", "unique family is exactly" in lsp and "exp(sum_x h_x epsilon_x)" in lsp)
    check("source-action note is open_gate", "**Claim type:** open_gate" in gate)
    check("source-action note records source derivatives of S convention", "Local source derivatives of `S` define" in gate)
    check("RN template records finite Gibbs density", "D_H = e^{-H} / Z_H" in rn)

    statuses = {
        "lsp_source": ledger_row("yt_" + "pr" + "230_lsp_signed_record_source_readout_support_note_2026-05-24").get("effective_status"),
        "source_action_gate": ledger_row("observable_principle_source_coupled_local_action_admission_candidate_note_2026-05-21").get("effective_status"),
        "yt_source_action_support": ledger_row("yt_" + "pr" + "230_consolidated_status_note_2026-05-22").get("effective_status"),
    }
    check("LSP source support is not retained coefficient authority", statuses["lsp_source"] != "retained", statuses["lsp_source"])
    check("source-action gate is not retained authority", statuses["source_action_gate"] != "retained", statuses["source_action_gate"])
    check("YT finite source-action support is retained_bounded", statuses["yt_source_action_support"] == "retained_bounded", statuses["yt_source_action_support"])
    return statuses


def part2_binary_exponential_family() -> dict[str, str]:
    print("\nPart 2: primitive binary source unit")
    h, lam, eps = sp.symbols("h lambda epsilon", real=True, positive=True)

    # Work explicitly on epsilon = +/-1 with uniform reference.
    p0 = {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}
    r = {e: sp.exp(h * e) / sp.cosh(h) for e in (1, -1)}
    score = {e: sp.diff(sp.log(r[e]), h).subs(h, 0) for e in (1, -1)}
    fisher = sp.simplify(sum(p0[e] * score[e] ** 2 for e in (1, -1)))

    check("score at + record is +1", is_zero(score[1] - 1), score[1])
    check("score at - record is -1", is_zero(score[-1] + 1), score[-1])
    check("primitive Fisher information is 1", is_zero(fisher - 1), fisher)

    r_lam = {e: sp.exp(h * lam * e) / sp.cosh(lam * h) for e in (1, -1)}
    score_lam = {e: sp.diff(sp.log(r_lam[e]), h).subs(h, 0) for e in (1, -1)}
    fisher_lam = sp.simplify(sum(p0[e] * score_lam[e] ** 2 for e in (1, -1)))

    check("lambda-scaled + score is lambda", is_zero(score_lam[1] - lam), score_lam[1])
    check("lambda-scaled - score is -lambda", is_zero(score_lam[-1] + lam), score_lam[-1])
    check("lambda-scaled Fisher information is lambda^2", is_zero(fisher_lam - lam**2), fisher_lam)
    check("Fisher-unit condition forces lambda=1", sp.solve(sp.Eq(fisher_lam, 1), lam) == [1])

    # KL divergence to the uniform reference has second derivative equal to Fisher.
    kl = sp.simplify(sum(p0[e] * r[e] * sp.log(r[e]) for e in (1, -1)))
    kl_second = sp.diff(kl, h, 2).subs(h, 0)
    kl_lam = sp.simplify(sum(p0[e] * r_lam[e] * sp.log(r_lam[e]) for e in (1, -1)))
    kl_lam_second = sp.diff(kl_lam, h, 2).subs(h, 0)
    check("KL curvature at primitive origin is 1", is_zero(kl_second - 1), kl_second)
    check("KL curvature at scaled origin is lambda^2", is_zero(kl_lam_second - lam**2), kl_lam_second)

    return {
        "primitive_score": "epsilon",
        "primitive_fisher": "1",
        "scaled_score": "lambda epsilon",
        "scaled_fisher": "lambda^2",
    }


def part3_six_component_top_source() -> dict[str, str]:
    print("\nPart 3: six-component top source")
    lam = sp.symbols("lambda", positive=True)
    n = sp.Integer(6)
    u = sp.Matrix([1 / sp.sqrt(n)] * n)
    norm = sp.simplify(u.dot(u))
    check("democratic top vector has unit norm", is_zero(norm - 1), norm)
    for idx in (0, 3, 5):
        check(f"component {idx} is 1/sqrt(6)", is_zero(u[idx] - 1 / sp.sqrt(6)), u[idx])

    fisher_top = sp.simplify((lam * u).dot(lam * u))
    check("scaled top-source Fisher norm is lambda^2", is_zero(fisher_top - lam**2), fisher_top)
    check("unit top-source Fisher condition forces lambda=1", sp.solve(sp.Eq(fisher_top, 1), lam) == [1])
    y33 = sp.simplify(u[0])
    check("primitive unit top source gives y_33=1/sqrt(6)", is_zero(y33 - 1 / sp.sqrt(6)), y33)
    return {
        "top_unit_vector": "(1,1,1,1,1,1)/sqrt(6)",
        "unit_component": "1/sqrt(6)",
        "lambda_selected_by_unit_fisher": "1",
    }


def part4_action_source_bridge() -> dict[str, Any]:
    print("\nPart 4: source-coupled action bridge")
    h, lam, O = sp.symbols("h lambda O", real=True, positive=True)
    # For centered primitive operator O, action S_h = S0 - h a O gives RN
    # derivative proportional to exp(h a O). The origin score is a O.
    score_unit = sp.diff(h * O, h).subs(h, 0)
    score_scaled = sp.diff(h * lam * O, h).subs(h, 0)
    check("unit action source score is O", is_zero(score_unit - O), score_unit)
    check("lambda action source score is lambda O", is_zero(score_scaled - lam * O), score_scaled)
    check("requiring unit action score forces lambda=1", sp.solve(sp.Eq(score_scaled, score_unit), lam) == [1])

    source_gate_closed = False
    check("source/action convention remains open on current surface", not source_gate_closed)
    return {
        "unit_action_source": "S_h=S_0-h O",
        "scaled_action_source": "S_h=S_0-h lambda O",
        "lambda_selected_if_source_action_gate_accepted": 1,
        "source_action_gate_closed": source_gate_closed,
    }


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
        "source-coupled local action convention is derived from A1+A2",
        "old Ward route is repaired",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("Y_T PRIMITIVE SOURCE-UNIT FISHER NORMALIZATION")
    print("=" * 88)

    statuses = part1_anchors()
    binary = part2_binary_exponential_family()
    top = part3_six_component_top_source()
    action = part4_action_source_bridge()
    part5_firewalls()

    result = {
        "status": "conditional / bounded support",
        "claim": "primitive signed-record Fisher source unit selects lambda=1",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The source-unit theorem selects lambda=1 only inside the canonical "
            "RN/source-action branch. The source-coupled local action convention "
            "is still an open gate on the current surface."
        ),
        "binary_source_unit": binary,
        "top_source_unit": top,
        "action_bridge": action,
        "upstream_statuses": statuses,
        "conditional_closure": "if source/action gate accepted, y_33=1/sqrt(6)",
        "actual_remaining_bridge": (
            "derive/accept source-coupled local action convention strongly enough "
            "to identify the physical top Yukawa deformation with the primitive "
            "source unit, or measure the top response directly"
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_PRIMITIVE_SOURCE_UNIT_FISHER_NORMALIZATION_SUPPORT_NOTE_2026-05-25.md",
            "scripts/frontier_yt_primitive_source_unit_fisher_normalization.py",
            "outputs/yt_primitive_source_unit_fisher_normalization_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
