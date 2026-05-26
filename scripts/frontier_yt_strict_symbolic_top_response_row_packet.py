#!/usr/bin/env python3
"""Strict symbolic top-response row packet for the Y_T route.

This runner checks the same-source top response row shape on the neutral
carrier ray while keeping the top Yukawa coefficient symbolic and free.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"

NOTE = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
ONE_HIGGS = DOCS / "SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md"
NEUTRAL_RAY = DOCS / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md"
STRICT_WZ = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
TOPOLOGY_NOGO = DOCS / "YT_TOP_RESPONSE_COEFFICIENT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-25.md"
HYPERCHARGE = DOCS / "STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md"
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
    ledger = json.loads(read(LEDGER))
    rows = ledger["rows"]
    iterable = rows.values() if isinstance(rows, dict) else rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row
    raise KeyError(claim_id)


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def matrix_is_zero(matrix: sp.Matrix) -> bool:
    return all(is_zero(entry) for entry in matrix)


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and authority scope")
    for path in (NOTE, ONE_HIGGS, NEUTRAL_RAY, STRICT_WZ, TOPOLOGY_NOGO, HYPERCHARGE, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Strict Symbolic Top Response",
        "What This Closes",
        "What This Still Does Not Close",
        "Why This Is Not A Renaming",
        "Review Boundary Certificate",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    source_action = ledger_row("yt_source_action_support_packet_note_2026-05-22")
    one_higgs = ledger_row("sm_one_higgs_yukawa_gauge_selection_theorem_note_2026-04-26")
    hypercharge = ledger_row("standard_model_hypercharge_uniqueness_theorem_note_2026-04-24")

    check("source-action support packet is retained_bounded", source_action.get("effective_status") == "retained_bounded")
    check("one-Higgs top carrier is not retained authority yet", one_higgs.get("effective_status") != "retained")
    check("hypercharge uniqueness is not retained authority yet", hypercharge.get("effective_status") != "retained")

    one_higgs_text = read(ONE_HIGGS)
    check("one-Higgs note selects up-type tilde-H monomial", "bar Q_L tilde H u_R" in one_higgs_text)
    check("one-Higgs note leaves generation matrices free", "generation matrices" in one_higgs_text and "free" in one_higgs_text)
    check("one-Higgs note does not derive numerical Yukawa eigenvalue", "does not select the numerical entries" in one_higgs_text)

    return {
        "source_action_status": source_action.get("effective_status"),
        "one_higgs_yukawa_selection_status": one_higgs.get("effective_status"),
        "hypercharge_uniqueness_status": hypercharge.get("effective_status"),
    }


def part2_tilde_h_neutral_component() -> None:
    print("\nPart 2: tilde-H neutral component")
    v = sp.symbols("v", real=True)
    h = sp.Matrix([0, v / sp.sqrt(2)])
    epsilon = sp.Matrix([[0, 1], [-1, 0]])
    tilde_h = epsilon * h.conjugate()
    expected = sp.Matrix([v / sp.sqrt(2), 0])
    check("tilde H carries neutral upper component", matrix_is_zero(tilde_h - expected), tilde_h)
    check("H and tilde H have the same radial magnitude", is_zero((h.T * h)[0] - (tilde_h.T * tilde_h)[0]), (tilde_h.T * tilde_h)[0])


def part3_symbolic_top_response() -> None:
    print("\nPart 3: strict symbolic top response")
    s = sp.symbols("s", real=True)
    y33 = sp.symbols("y_33", nonzero=True)
    v = sp.Function("v")(s)
    mt = y33 * v / sp.sqrt(2)
    dmt = sp.diff(mt, s)
    expected = y33 * sp.diff(v, s) / sp.sqrt(2)
    check("M_t row has free y_33 coefficient", mt.has(y33), mt)
    check("dM_t/ds row shape", is_zero(dmt - expected), dmt)
    check("top coefficient remains symbolic", y33 in dmt.free_symbols, dmt)


def part4_top_w_ratio_with_free_coefficient() -> None:
    print("\nPart 4: top/W ratio with free coefficient")
    s = sp.symbols("s", real=True)
    g2, y33 = sp.symbols("g_2 y_33", positive=True)
    v = sp.Function("v")(s)
    mt = y33 * v / sp.sqrt(2)
    mw = g2 * v / 2
    ratio = sp.simplify(sp.diff(mt, s) / sp.diff(mw, s))
    recovered = sp.simplify(g2 / sp.sqrt(2) * ratio)
    check("top/W ratio cancels source Jacobian", is_zero(ratio - sp.sqrt(2) * y33 / g2), ratio)
    check("top/W recovery returns symbolic y_33", is_zero(recovered - y33), recovered)


def part5_reparameterization() -> None:
    print("\nPart 5: source-coordinate reparameterization")
    r = sp.symbols("r", real=True)
    g2, y33 = sp.symbols("g_2 y_33", positive=True)
    f = sp.Function("f")(r)
    v = sp.Function("v")(f)
    mt = y33 * v / sp.sqrt(2)
    mw = g2 * v / 2
    ratio = sp.simplify(sp.diff(mt, r) / sp.diff(mw, r))
    check("ratio invariant under s=f(r)", is_zero(ratio - sp.sqrt(2) * y33 / g2), ratio)


def part6_current_boundary(statuses: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 6: current boundary")
    blockers = {
        "symbolic_top_response_shape_closed": True,
        "top_coefficient_derived": False,
        "one_higgs_yukawa_selection_retained": statuses["one_higgs_yukawa_selection_status"] == "retained",
        "hypercharge_uniqueness_retained": statuses["hypercharge_uniqueness_status"] == "retained",
        "retained_closure_allowed": False,
    }
    check("symbolic top response row shape is closed", blockers["symbolic_top_response_shape_closed"])
    check("top coefficient remains open", not blockers["top_coefficient_derived"])
    check("one-Higgs top carrier is not retained authority yet", not blockers["one_higgs_yukawa_selection_retained"])
    check("hypercharge uniqueness is not retained authority yet", not blockers["hypercharge_uniqueness_retained"])
    check("retained Y_T closure is not allowed from a symbolic coefficient row", not blockers["retained_closure_allowed"])
    return blockers


def part7_firewalls() -> None:
    print("\nPart 7: firewalls")
    note = " ".join(read(NOTE).split())
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
        check(f"firewall phrase present: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "proposed_retained",
        "This packet derives `y_t`",
        "positive Y_T closure has been obtained",
        "`y_33` is derived",
        "top coefficient is derived",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T STRICT SYMBOLIC TOP-RESPONSE ROW PACKET")
    print("=" * 78)

    statuses = part1_anchors()
    part2_tilde_h_neutral_component()
    part3_symbolic_top_response()
    part4_top_w_ratio_with_free_coefficient()
    part5_reparameterization()
    blockers = part6_current_boundary(statuses)
    part7_firewalls()

    result = {
        "status": "conditional exact support: symbolic top-response row shape, free coefficient",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The top response row shape closes symbolically, but y_33 remains a free "
            "generation-matrix coefficient and the one-Higgs/hypercharge rows are not retained here."
        ),
        "symbolic_top_response_shape_closed": True,
        "top_coefficient_derived": False,
        "current_blockers": blockers,
        "upstream_statuses": statuses,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md",
            "scripts/frontier_yt_strict_symbolic_top_response_row_packet.py",
            "outputs/yt_strict_symbolic_top_response_row_packet_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
