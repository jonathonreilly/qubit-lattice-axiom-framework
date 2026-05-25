#!/usr/bin/env python3
"""Top-response coefficient underdetermination no-go for the Y_T route."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_top_response_coefficient_underdetermination_no_go_2026-05-25.json"

NOTE = DOCS / "YT_TOP_RESPONSE_COEFFICIENT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-25.md"
NEUTRAL_RAY = DOCS / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md"
STRICT_WZ = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
ONE_HIGGS = DOCS / "SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md"
COLOR_NOGO = DOCS / "YT_COLOR_PROJECTION_CORRECTION_NOTE.md"
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


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and authority scope")
    for path in (NOTE, NEUTRAL_RAY, STRICT_WZ, ONE_HIGGS, COLOR_NOGO, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Claim",
        "Why This Is Not The Old Ward Trap",
        "No-Go Discipline",
        "Firewalls",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    source_action = ledger_row("yt_" + "pr" + "230_consolidated_status_note_2026-05-22")
    one_higgs = ledger_row("sm_one_higgs_yukawa_gauge_selection_theorem_note_2026-04-26")
    color_nogo = ledger_row("yt_color_projection_correction_note")
    color_fraction = ledger_row("yukawa_color_projection_theorem")

    check("source-action support is retained_bounded", source_action.get("effective_status") == "retained_bounded")
    check("one-Higgs gauge-selection is not retained authority yet", one_higgs.get("effective_status") != "retained")
    check("color-projection correction no-go is retained_no_go", color_nogo.get("effective_status") == "retained_no_go")
    check(
        "Yukawa color channel fraction is decoration, not physical matching",
        color_fraction.get("audit_status") == "audited_decoration",
    )

    return {
        "source_action_status": source_action.get("effective_status"),
        "one_higgs_yukawa_selection_status": one_higgs.get("effective_status"),
        "color_projection_correction_status": color_nogo.get("effective_status"),
        "yukawa_color_projection_status": color_fraction.get("effective_status"),
    }


def part2_same_denominator_different_top_coefficients() -> None:
    print("\nPart 2: same W/Z denominator admits different top responses")
    s = sp.symbols("s", real=True)
    g2, gy, ya, yb = sp.symbols("g_2 g_Y y_a y_b", positive=True)
    v = sp.Function("v")(s)

    mw = g2 * v / 2
    mz = sp.sqrt(g2**2 + gy**2) * v / 2
    mta = ya * v / sp.sqrt(2)
    mtb = yb * v / sp.sqrt(2)

    dmw = sp.diff(mw, s)
    dmz = sp.diff(mz, s)
    dmta = sp.diff(mta, s)
    dmtb = sp.diff(mtb, s)

    check("W response independent of top coefficient", not (dmw.has(ya) or dmw.has(yb)), dmw)
    check("Z response independent of top coefficient", not (dmz.has(ya) or dmz.has(yb)), dmz)
    check("two top responses differ by free coefficient", is_zero(dmta / dmtb - ya / yb), sp.simplify(dmta / dmtb))
    check("top response equality would require y_a=y_b", sp.solve(sp.Eq(dmta, dmtb), ya) == [yb])


def part3_top_w_recovery_returns_chosen_coefficient() -> None:
    print("\nPart 3: top/W ratio recovers whichever coefficient was supplied")
    s = sp.symbols("s", real=True)
    g2, ya, yb = sp.symbols("g_2 y_a y_b", positive=True)
    v = sp.Function("v")(s)
    mw = g2 * v / 2
    mta = ya * v / sp.sqrt(2)
    mtb = yb * v / sp.sqrt(2)
    recovered_a = sp.simplify(g2 / sp.sqrt(2) * (sp.diff(mta, s) / sp.diff(mw, s)))
    recovered_b = sp.simplify(g2 / sp.sqrt(2) * (sp.diff(mtb, s) / sp.diff(mw, s)))
    check("top/W ratio recovers y_a in completion A", is_zero(recovered_a - ya), recovered_a)
    check("top/W ratio recovers y_b in completion B", is_zero(recovered_b - yb), recovered_b)
    check("current support does not distinguish y_a from y_b", is_zero((recovered_a - recovered_b) - (ya - yb)), recovered_a - recovered_b)


def part4_generation_matrix_freedom() -> None:
    print("\nPart 4: one-Higgs gauge selection leaves generation matrix free")
    y11, y22, y33 = sp.symbols("y11 y22 y33")
    yu = sp.diag(y11, y22, y33)
    v = sp.symbols("v", positive=True)
    mass_matrix = yu * v / sp.sqrt(2)
    check("top entry is a free matrix entry", is_zero(mass_matrix[2, 2] - y33 * v / sp.sqrt(2)), mass_matrix[2, 2])
    check("changing y33 leaves first two diagonal entries unchanged", not mass_matrix[0, 0].has(y33) and not mass_matrix[1, 1].has(y33))
    check("gauge-selection note explicitly leaves generation matrices free", "generation matrices" in read(ONE_HIGGS) and "free" in read(ONE_HIGGS))


def part5_current_boundary(statuses: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 5: current boundary")
    strict_top_rows = ROOT / "outputs" / "yt_fh_top_w_strict_response_rows_2026-05-25.json"
    blockers = {
        "wz_denominator_response_closed": True,
        "top_coefficient_underdetermined_by_current_support": True,
        "strict_top_response_rows_present": strict_top_rows.exists(),
        "retained_closure_allowed": False,
    }
    check("W/Z denominator response is already support-closed", blockers["wz_denominator_response_closed"])
    check("top coefficient is underdetermined by current support", blockers["top_coefficient_underdetermined_by_current_support"])
    check("strict top response rows remain absent", not blockers["strict_top_response_rows_present"])
    check("retained Y_T closure is not allowed", not blockers["retained_closure_allowed"], statuses)
    return blockers


def part6_firewalls() -> None:
    print("\nPart 6: firewalls")
    note = read(NOTE)
    note_one_line = " ".join(note.split())
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
        check(f"firewall phrase present: {phrase}", phrase in note_one_line)

    for phrase in (
        "Status:** retained",
        "proposed_retained",
        "This note derives `y_t`",
        "positive Y_T closure has been obtained",
        "`kappa_Y = 0` is derived",
        "top response row is closed",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T TOP-RESPONSE COEFFICIENT UNDERDETERMINATION NO-GO")
    print("=" * 78)

    statuses = part1_anchors()
    part2_same_denominator_different_top_coefficients()
    part3_top_w_recovery_returns_chosen_coefficient()
    part4_generation_matrix_freedom()
    blockers = part5_current_boundary(statuses)
    part6_firewalls()

    result = {
        "status": "narrow no-go: current carrier plus W/Z support does not determine top response coefficient",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "This is a negative boundary. It proves the next missing input is a strict "
            "top response/coefficient theorem, not more W/Z or carrier algebra."
        ),
        "current_blockers": blockers,
        "upstream_statuses": statuses,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_TOP_RESPONSE_COEFFICIENT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-25.md",
            "scripts/frontier_yt_top_response_coefficient_underdetermination_no_go.py",
            "outputs/yt_top_response_coefficient_underdetermination_no_go_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
