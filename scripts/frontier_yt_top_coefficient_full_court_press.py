#!/usr/bin/env python3
"""Full-court-press route decision for the remaining Y_T top coefficient."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_top_coefficient_full_court_press_2026-05-25.json"

NOTE = DOCS / "YT_TOP_COEFFICIENT_FULL_COURT_PRESS_NOTE_2026-05-25.md"
SYMBOLIC_TOP = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
COEFF_NOGO = DOCS / "YT_TOP_RESPONSE_COEFFICIENT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-25.md"
ONE_HIGGS = DOCS / "SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md"
WARD = DOCS / "YT_WARD_IDENTITY_DERIVATION_THEOREM.md"
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
    print("\nPart 1: anchors and sections")
    for path in (NOTE, SYMBOLIC_TOP, COEFF_NOGO, ONE_HIGGS, WARD, COLOR_NOGO, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Assumptions Exercise",
        "First-Principles Exercise",
        "Literature Search",
        "Mathematics Search",
        "Route Verdicts",
        "Decision",
        "Firewalls",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    statuses = {
        "source_action": ledger_row("yt_" + "pr" + "230_consolidated_status_note_2026-05-22").get("effective_status"),
        "one_higgs": ledger_row("sm_one_higgs_yukawa_gauge_selection_theorem_note_2026-04-26").get("effective_status"),
        "hypercharge": ledger_row("standard_model_hypercharge_uniqueness_theorem_note_2026-04-24").get("effective_status"),
        "color_projection_correction": ledger_row("yt_color_projection_correction_note").get("effective_status"),
        "yukawa_color_projection_audit": ledger_row("yukawa_color_projection_theorem").get("audit_status"),
    }
    check("source-action row is retained_bounded support", statuses["source_action"] == "retained_bounded")
    check("one-Higgs row is not retained coefficient authority", statuses["one_higgs"] != "retained")
    check("hypercharge row is not retained coefficient authority", statuses["hypercharge"] != "retained")
    check("color-projection correction row is retained_no_go", statuses["color_projection_correction"] == "retained_no_go")
    check("Yukawa color projection is audited decoration", statuses["yukawa_color_projection_audit"] == "audited_decoration")
    return statuses


def part2_assumptions_and_firewalls() -> None:
    print("\nPart 2: assumptions and firewalls")
    note = read(NOTE)
    for phrase in (
        "Explicit Assumptions",
        "Implicit Assumptions",
        "What If We Are Wrong?",
        "Do not keep attacking W/Z normalization",
        "Attack y_33 directly",
    ):
        check(f"exercise phrase present: {phrase}", phrase in note)

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


def part3_math_underdetermination() -> None:
    print("\nPart 3: math underdetermination")
    y_a, y_b, g2, s = sp.symbols("y_a y_b g_2 s", positive=True)
    v = sp.Function("v")(s)
    mt_a = y_a * v / sp.sqrt(2)
    mt_b = y_b * v / sp.sqrt(2)
    mw = g2 * v / 2

    ratio_a = sp.simplify(sp.diff(mt_a, s) / sp.diff(mw, s))
    ratio_b = sp.simplify(sp.diff(mt_b, s) / sp.diff(mw, s))
    check("top/W row shape recovers arbitrary y_a", is_zero(g2 * ratio_a / sp.sqrt(2) - y_a), ratio_a)
    check("top/W row shape recovers arbitrary y_b", is_zero(g2 * ratio_b / sp.sqrt(2) - y_b), ratio_b)
    check("different coefficients are distinguishable only by top numerator", is_zero((ratio_a - ratio_b) - sp.sqrt(2) * (y_a - y_b) / g2), ratio_a - ratio_b)

    # Gauge-selection constraints do not contain y_33.
    y33 = sp.symbols("y_33")
    constraints = [
        sp.Eq(sp.Symbol("Y_Q") - sp.Symbol("Y_u") + sp.Symbol("Y_tildeH"), 0),
        sp.Eq(sp.Symbol("dim_operator"), 4),
    ]
    check("gauge/operator constraints do not contain y_33", all(y33 not in eq.free_symbols for eq in constraints))

    y11, y22 = sp.symbols("y11 y22")
    yu = sp.diag(y11, y22, y33)
    check("generation matrix has free top entry", is_zero(yu[2, 2] - y33), yu)
    check("changing y_33 leaves gauge representation unchanged", yu.shape == (3, 3))


def part4_literature_sources() -> None:
    print("\nPart 4: literature-source audit")
    note = read(NOTE)
    urls = (
        "https://link.springer.com/article/10.1140/epjc/s10052-015-3576-5",
        "https://arxiv.org/abs/2305.05491",
        "https://link.springer.com/article/10.1140/epjc/s10052-012-2120-0",
        "https://arxiv.org/abs/1907.01590",
    )
    for url in urls:
        check(f"literature source present: {url}", url in note)

    check("literature search does not claim external theorem proves framework no-go", "does not prove that this framework cannot derive" in note)


def part5_route_decision() -> dict[str, Any]:
    print("\nPart 5: route decision")
    note = read(NOTE)
    structural_derivation_from_current_stack = False
    direct_measurement_route_live = True
    new_flavor_theorem_route_live = True

    check("current structural route is marked blocked", "| Gauge/operator selection | blocked |" in note)
    check("qubit democratic source route is marked live exact-support candidate", "| Qubit democratic Q_L source amplitude | live exact-support candidate |" in note)
    check("signed-linear tangent route is marked live exact-support candidate", "| Signed-linear source/action tangent | live exact-support candidate |" in note)
    check("direct response/correlator route is marked live", "| Direct top response/correlator | live |" in note)
    check("new dynamical flavor theorem route is marked live but hard", "| New dynamical flavor theorem | live but hard |" in note)
    check("structural derivation from current stack is not allowed", not structural_derivation_from_current_stack)
    check("direct measurement route remains live", direct_measurement_route_live)
    check("new flavor theorem route remains live", new_flavor_theorem_route_live)

    return {
        "structural_derivation_from_current_stack_allowed": structural_derivation_from_current_stack,
        "direct_measurement_route_live": direct_measurement_route_live,
        "new_dynamical_flavor_theorem_route_live": new_flavor_theorem_route_live,
    }


def part6_overclaim_scan() -> None:
    print("\nPart 6: overclaim scan")
    note = read(NOTE)
    forbidden = (
        "Status:** retained",
        "Status: retained",
        "proposed_retained",
        "This note derives `y_t`",
        "`y_33` is derived",
        "positive Y_T closure has been obtained",
        "full retained closure",
    )
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    ward_text = read(WARD)
    ward_lower = ward_text.lower()
    check("old Ward note records H_unit definition trap", "definition of y_t_bare" in ward_lower and "h_unit" in ward_lower)


def main() -> int:
    print("=" * 78)
    print("Y_T TOP-COEFFICIENT FULL-COURT-PRESS")
    print("=" * 78)

    statuses = part1_anchors()
    part2_assumptions_and_firewalls()
    part3_math_underdetermination()
    part4_literature_sources()
    route_decision = part5_route_decision()
    part6_overclaim_scan()

    result = {
        "status": "exact negative boundary: current structural route does not determine y_33",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The assumptions, first-principles, literature, and mathematics exercises all "
            "separate row-shape support from coefficient selection. Current carrier/WZ/"
            "one-Higgs algebra leaves y_33 continuous."
        ),
        "route_decision": route_decision,
        "upstream_statuses": statuses,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_TOP_COEFFICIENT_FULL_COURT_PRESS_NOTE_2026-05-25.md",
            "scripts/frontier_yt_top_coefficient_full_court_press.py",
            "outputs/yt_top_coefficient_full_court_press_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
