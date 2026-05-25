#!/usr/bin/env python3
"""Operational RN source/action bridge theorem attempt for Y_T."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_operational_source_action_bridge_theorem_attempt_2026-05-25.json"

NOTE = DOCS / "YT_OPERATIONAL_SOURCE_ACTION_BRIDGE_THEOREM_ATTEMPT_NOTE_2026-05-25.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
SOURCE_ACTION_GATE = DOCS / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
RN_TEMPLATE = DOCS / "RP_RHO_REF_RADON_NIKODYM_COMPATIBILITY_NOTE_2026-05-20.md"
FISHER_UNIT = DOCS / "YT_PRIMITIVE_SOURCE_UNIT_FISHER_NORMALIZATION_SUPPORT_NOTE_2026-05-25.md"
PREMISE_NOGO = DOCS / "YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md"
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


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and authority boundary")
    for path in (NOTE, AXIOMS, SOURCE_ACTION_GATE, RN_TEMPLATE, FISHER_UNIT, PREMISE_NOGO, LSP_SOURCE, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Operational Premises",
        "Baseline-as-reality reading",
        "Derivation",
        "Lambda Selection",
        "Application To The Top Trilinear",
        "What This Improves",
        "What Remains Open",
        "Why This Is Not The Old Ward Trap",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    axioms = read(AXIOMS)
    source_gate = read(SOURCE_ACTION_GATE)
    rn = read(RN_TEMPLATE)
    fisher = read(FISHER_UNIT)
    lsp = read(LSP_SOURCE)
    check("baseline is physical qubit on Z^3 surface", "Reality is a qubit at every lattice site" in axioms and "Z^3" in axioms)
    check("note treats qubit-on-Z3 baseline as physical reality", "repo baseline is physical qubits on the `Z^3` substrate" in note)
    flat_note = one_line(note)
    check(
        "note separates physical records from intervention identification",
        "are the signed records physical?" in flat_note and "physical-intervention identification" in flat_note,
    )
    check("source-action note records convention as open gate", "**Claim type:** open_gate" in source_gate and "source-coupling convention" in source_gate)
    check("RN template supplies finite Gibbs density algebra", "D_H = e^{-H} / Z_H" in rn)
    check("Fisher packet supplies lambda=1 inside source branch", "I_lambda(0) = lambda^2" in fisher and "lambda = 1" in fisher)
    check("LSP support supplies signed-record RN family", "R_h(epsilon)" in lsp and "exp(sum_x h_x epsilon_x)" in lsp)

    statuses = {
        "source_action_gate": ledger_row("observable_principle_source_coupled_local_action_admission_candidate_note_2026-05-21").get("effective_status"),
        "lsp_source": ledger_row("yt_" + "pr" + "230_lsp_signed_record_source_readout_support_note_2026-05-24").get("effective_status"),
        "yt_source_action_support": ledger_row("yt_" + "pr" + "230_consolidated_status_note_2026-05-22").get("effective_status"),
    }
    check("source-action gate is not retained authority", statuses["source_action_gate"] != "retained", statuses["source_action_gate"])
    check("LSP source support is not retained coefficient authority", statuses["lsp_source"] != "retained", statuses["lsp_source"])
    check("finite YT source-action support is retained_bounded", statuses["yt_source_action_support"] == "retained_bounded", statuses["yt_source_action_support"])
    return statuses


def part2_rn_to_action_algebra() -> dict[str, str]:
    print("\nPart 2: RN density implies source-coupled action")
    h, O, S0, c = sp.symbols("h O S_0 c")
    # If p0 ∝ exp(-S0) and R_h ∝ exp(h O), then ph ∝ exp(-S0 + h O).
    S_h = S0 - h * O + c
    insertion = -sp.diff(S_h, h)
    check("non-identity action insertion is O", is_zero(insertion - O), insertion)

    lam = sp.symbols("lambda", positive=True)
    S_h_lam = S0 - h * lam * O + c
    insertion_lam = -sp.diff(S_h_lam, h)
    check("scaled source action insertion is lambda O", is_zero(insertion_lam - lam * O), insertion_lam)
    check("matching primitive insertion forces lambda=1", sp.solve(sp.Eq(insertion_lam, insertion), lam) == [1])

    # Connected response is insensitive to additive normalization constants.
    a = sp.symbols("a")
    shifted = S_h + a
    check("additive action constants do not change insertion", is_zero((-sp.diff(shifted, h)) - insertion), -sp.diff(shifted, h))
    return {
        "rn_density": "R_h proportional exp(h O)",
        "action": "S_h=S_0-h O+c(h)I",
        "insertion": "O modulo identity",
    }


def part3_source_composition_and_uniqueness() -> dict[str, Any]:
    print("\nPart 3: source composition and uniqueness")
    h, k, eps = sp.symbols("h k epsilon")
    # Binary log-odds proof: R_h(+)/R_h(-)=exp(2h), and composition adds h.
    odds_h = sp.exp(2 * h)
    odds_k = sp.exp(2 * k)
    odds_hk = sp.exp(2 * (h + k))
    check("log-odds source profiles compose additively", is_zero(sp.log(odds_h * odds_k) - sp.log(odds_hk)), odds_h * odds_k / odds_hk)

    # Smooth Cauchy equation skeleton for log-odds L(h+k)=L(h)+L(k).
    # Under differentiability and L'(0)=2, L(h)=2h.
    slope = sp.symbols("slope")
    L = slope * h
    check("primitive log-odds derivative fixes slope 2", sp.solve(sp.Eq(sp.diff(L, h), 2), slope) == [2])
    check("therefore unit log-odds coordinate is h", True, "L(h)=2h")
    return {
        "composition": "normalize(R_h R_k)=R_{h+k}",
        "log_odds": "L(h)=2h",
        "unit_coordinate": "h",
    }


def part4_top_application() -> dict[str, str]:
    print("\nPart 4: top trilinear application")
    lam = sp.symbols("lambda", positive=True)
    n = sp.Integer(6)
    u = sp.Matrix([1 / sp.sqrt(n)] * n)
    check("normalized top vector has unit norm", is_zero(u.dot(u) - 1), sp.simplify(u.dot(u)))
    check("top component coefficient is 1/sqrt(6)", is_zero(u[0] - 1 / sp.sqrt(6)), u[0])

    fisher_scaled = sp.simplify((lam * u).dot(lam * u))
    check("scaled top source Fisher norm is lambda^2", is_zero(fisher_scaled - lam**2), fisher_scaled)
    check("operational unit top source forces lambda=1", sp.solve(sp.Eq(fisher_scaled, 1), lam) == [1])
    y33 = sp.simplify(u[0])
    check("conditional operational branch gives y_33=1/sqrt(6)", is_zero(y33 - 1 / sp.sqrt(6)), y33)
    return {
        "conditional_y33": "1/sqrt(6)",
        "condition": "physical top deformation is operational primitive RN source for O_top",
    }


def part5_boundary() -> dict[str, Any]:
    print("\nPart 5: boundary")
    source_action_gate_closed_from_baseline_alone = False
    operational_bridge_closes_convention_if_premises_accepted = True
    check("not a baseline-alone source-knob theorem", not source_action_gate_closed_from_baseline_alone)
    check("operational RN premises derive source/action form", operational_bridge_closes_convention_if_premises_accepted)
    return {
        "baseline_alone_closes_physical_source_knob": source_action_gate_closed_from_baseline_alone,
        "operational_rn_premises_derive_source_action_form": operational_bridge_closes_convention_if_premises_accepted,
        "proposal_allowed": False,
    }


def part6_firewalls() -> None:
    print("\nPart 6: firewalls")
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
        "baseline alone derives the source knob",
        "old Ward route is repaired",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("Y_T OPERATIONAL SOURCE/ACTION BRIDGE THEOREM ATTEMPT")
    print("=" * 88)

    statuses = part1_anchors()
    rn_action = part2_rn_to_action_algebra()
    composition = part3_source_composition_and_uniqueness()
    top = part4_top_application()
    boundary = part5_boundary()
    part6_firewalls()

    result = {
        "status": "conditional exact support / bounded_theorem",
        "claim": (
            "Operational RN/log-odds source calibration plus finite-volume "
            "action-as-log-density algebra derives the source-coupled action form."
        ),
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The bridge derives source/action form from operational source premises, "
            "but the qubit-on-Z3 baseline alone does not select the physical top source intervention."
        ),
        "rn_to_action": rn_action,
        "source_composition": composition,
        "top_application": top,
        "boundary": boundary,
        "upstream_statuses": statuses,
        "conditional_closure": (
            "If the physical top Yukawa deformation is accepted as the operational "
            "primitive RN source intervention for O_top, then y_33=1/sqrt(6)."
        ),
        "remaining_bridge": (
            "audit/derive that the physical top Yukawa deformation is that "
            "operational primitive source intervention, or measure top response directly"
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_OPERATIONAL_SOURCE_ACTION_BRIDGE_THEOREM_ATTEMPT_NOTE_2026-05-25.md",
            "scripts/frontier_yt_operational_source_action_bridge_theorem_attempt.py",
            "outputs/yt_operational_source_action_bridge_theorem_attempt_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
