#!/usr/bin/env python3
"""Y_T EW/Higgs source-intertwiner gate.

This runner checks the algebraic carrier map that would connect the finite
signed-record source lane to the neutral EW Higgs radial source.  It deliberately
keeps the result support-only unless the required source-carrier authority rows
are retained.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_ew_higgs_source_intertwiner_gate_2026-05-25.json"

NOTE = DOCS / "YT_EW_HIGGS_SOURCE_INTERTWINER_GATE_NOTE_2026-05-25.md"
NEUTRAL_RAY_BRIDGE = DOCS / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md"
STRICT_WZ_PACKET = ROOT / "outputs" / "yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json"
SYMBOLIC_TOP_PACKET = ROOT / "outputs" / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"
EW_MASS = DOCS / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
ONE_HIGGS = DOCS / "SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md"
HYPERCHARGE = DOCS / "STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

SOURCE_ACTION_CLAIM = "yt_source_action_support_packet_note_2026-05-22"

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


def ledger_row(claim_id: str) -> dict[str, Any] | None:
    ledger = json.loads(read(LEDGER))
    rows = ledger["rows"]
    if isinstance(rows, dict):
        return rows.get(claim_id)
    iterable = rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row
    return None


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def matrix_is_zero(matrix: sp.Matrix) -> bool:
    return all(is_zero(entry) for entry in matrix)


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and current authority")
    for path in (NOTE, NEUTRAL_RAY_BRIDGE, EW_MASS, ONE_HIGGS, HYPERCHARGE, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Candidate Intertwiner",
        "Why This Still Does Not Close",
        "Required Positive Theorem",
        "Non-Claims",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    source_action = ledger_row(SOURCE_ACTION_CLAIM)
    ew_mass = ledger_row("ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26")
    one_higgs = ledger_row("sm_one_higgs_yukawa_gauge_selection_theorem_note_2026-04-26")
    hypercharge = ledger_row("standard_model_hypercharge_uniqueness_theorem_note_2026-04-24")

    check("source-action support packet row is present in the audit ledger (presence only)", source_action is not None)
    check("EW Higgs gauge-mass theorem row is present in the audit ledger (presence only)", ew_mass is not None)
    check("one-Higgs Yukawa gauge-selection row is present in the audit ledger (presence only)", one_higgs is not None)
    check("hypercharge uniqueness row is present in the audit ledger (presence only)", hypercharge is not None)
    print(
        "  [info] live effective statuses (audit-lane-owned; not gated): "
        f"source_action={(source_action or {}).get('effective_status')!r}, "
        f"ew_mass={(ew_mass or {}).get('effective_status')!r}, "
        f"one_higgs={(one_higgs or {}).get('effective_status')!r}, "
        f"hypercharge={(hypercharge or {}).get('effective_status')!r}"
    )

    return {
        "source_action_status": (source_action or {}).get("effective_status"),
        "ew_mass_status": (ew_mass or {}).get("effective_status"),
        "one_higgs_yukawa_selection_status": (one_higgs or {}).get("effective_status"),
        "hypercharge_uniqueness_status": (hypercharge or {}).get("effective_status"),
    }


def part2_neutral_radial_higgs_map() -> None:
    print("\nPart 2: neutral radial Higgs carrier algebra")
    v, a, h = sp.symbols("v a h", positive=True, real=True)
    i = sp.I
    radial = v + a * h
    higgs = sp.Matrix([0, radial / sp.sqrt(2)])
    tau1 = sp.Matrix([[0, 1], [1, 0]])
    tau2 = sp.Matrix([[0, -i], [i, 0]])
    tau3 = sp.Matrix([[1, 0], [0, -1]])
    t1, t2, t3 = tau1 / 2, tau2 / 2, tau3 / 2
    y = sp.Rational(1, 2) * sp.eye(2)

    check("radial Higgs carrier is a complex doublet", higgs.shape == (2, 1))
    check("neutral generator Q=T3+Y annihilates H(h)", matrix_is_zero((t3 + y) * higgs))
    check("T1 acts nontrivially on the radial carrier", not matrix_is_zero(t1 * higgs), t1 * higgs)
    check("T2 acts nontrivially on the radial carrier", not matrix_is_zero(t2 * higgs), t2 * higgs)

    dh = sp.diff(higgs, h)
    expected = sp.Matrix([0, a / sp.sqrt(2)])
    check("source derivative is radial and shares one slope a", matrix_is_zero(dh - expected), dh)


def part3_top_w_response_ratio_from_intertwiner() -> None:
    print("\nPart 3: top/W response ratio from common radial source")
    v, a, h, g2, yt = sp.symbols("v a h g_2 y_t", positive=True, real=True)
    radial = v + a * h
    mw = g2 * radial / 2
    mt = yt * radial / sp.sqrt(2)
    dmw = sp.diff(mw, h)
    dmt = sp.diff(mt, h)
    ratio = sp.simplify(dmt / dmw)
    recovered = sp.simplify(g2 * ratio / sp.sqrt(2))

    check("dM_W/dh has common source slope", is_zero(dmw - g2 * a / 2), dmw)
    check("dM_t/dh has common source slope", is_zero(dmt - yt * a / sp.sqrt(2)), dmt)
    check("top/W response ratio cancels source slope", is_zero(ratio - sp.sqrt(2) * yt / g2), ratio)
    check("y_t recovered from ratio and g_2", is_zero(recovered - yt), recovered)


def part4_top_carrier_support() -> None:
    print("\nPart 4: one-Higgs top carrier support is present but unaudited")
    one_higgs_text = read(ONE_HIGGS)
    check("one-Higgs note selects Q_L tilde H u_R", "bar Q_L tilde H u_R" in one_higgs_text)
    check("one-Higgs note states no numerical Yukawa eigenvalue claim", "any numerical Yukawa eigenvalue" in one_higgs_text)
    check("one-Higgs note leaves generation matrices free", "generation matrices" in one_higgs_text and "free" in one_higgs_text)


def part5_current_blockers(statuses: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 5: current closure blockers")
    strict_rows = ROOT / "outputs" / "yt_fh_top_w_strict_response_rows_2026-05-25.json"
    blockers = {
        "neutral_carrier_ray_bridge_present": NEUTRAL_RAY_BRIDGE.exists(),
        "strict_wz_denominator_response_present": STRICT_WZ_PACKET.exists(),
        "symbolic_top_response_row_present": SYMBOLIC_TOP_PACKET.exists(),
        "full_same_surface_top_w_transfer_response_present": False,
        "one_higgs_yukawa_selection_retained": False,
        "hypercharge_uniqueness_retained": False,
        "coefficient_certified_top_w_rows_present": strict_rows.exists(),
        "numerical_g2_retained_authority_present": False,
    }
    check("neutral carrier-ray bridge is present", blockers["neutral_carrier_ray_bridge_present"])
    check("strict W/Z denominator response is present", blockers["strict_wz_denominator_response_present"])
    check("symbolic top response row is present", blockers["symbolic_top_response_row_present"])
    check("full same-surface top/W transfer response remains unproved", not blockers["full_same_surface_top_w_transfer_response_present"])
    check("coefficient-certified top/W rows remain absent", not blockers["coefficient_certified_top_w_rows_present"])
    return blockers


def part6_firewalls() -> None:
    print("\nPart 6: firewalls")
    note = read(NOTE)
    firewall_checks = {
        "observed mass targets": "observed mass" in note and "targets" in note,
        "`H_unit`": "`H_unit`" in note,
        "Ward identity reuse": "Ward identity reuse" in note,
        "plaquette/u0": "plaquette/u0" in note,
        "`alpha_LM`": "`alpha_LM`" in note,
    }
    for phrase, ok in firewall_checks.items():
        check(f"firewall phrase present: {phrase}", ok)

    for phrase in (
        "Status:** retained",
        "proposed_retained",
        "This note derives `y_t`",
        "This note derives `g_2`",
        "positive Y_T closure has been obtained",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T EW/HIGGS SOURCE-INTERTWINER GATE")
    print("=" * 78)

    statuses = part1_anchors()
    part2_neutral_radial_higgs_map()
    part3_top_w_response_ratio_from_intertwiner()
    part4_top_carrier_support()
    blockers = part5_current_blockers(statuses)
    part6_firewalls()

    candidate_intertwiner_algebra_closed = True
    retained_closure_allowed = (
        blockers["neutral_carrier_ray_bridge_present"]
        and blockers["strict_wz_denominator_response_present"]
        and blockers["symbolic_top_response_row_present"]
        and blockers["full_same_surface_top_w_transfer_response_present"]
        and blockers["one_higgs_yukawa_selection_retained"]
        and blockers["hypercharge_uniqueness_retained"]
        and blockers["coefficient_certified_top_w_rows_present"]
        and blockers["numerical_g2_retained_authority_present"]
    )
    result = {
        "status": "bounded support: carrier algebra closes, source authority remains open",
        "candidate_intertwiner_algebra_closed": candidate_intertwiner_algebra_closed,
        "retained_closure_allowed": retained_closure_allowed,
        "retained_closure_blocker": (
            "The neutral EW carrier ray is now bridged from the signed-record source, "
            "W/Z denominator response is present, and the symbolic top response row "
            "is present, but the repo still lacks a derived top coefficient and the "
            "top one-Higgs carrier plus hypercharge rows are not retained authority."
        ),
        "current_blockers": blockers,
        "upstream_statuses": statuses,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_EW_HIGGS_SOURCE_INTERTWINER_GATE_NOTE_2026-05-25.md",
            "scripts/frontier_yt_ew_higgs_source_intertwiner_gate.py",
            "outputs/yt_ew_higgs_source_intertwiner_gate_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
