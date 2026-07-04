#!/usr/bin/env python3
"""Y_T same-source FH top/W response-ratio gate.

This runner checks the exact conditional algebra behind the proposed Y_T
top/W bypass:

    y_t = (g_2 / sqrt(2)) * (dM_t/dh) / (dM_W/dh)

when both masses are differentiated with respect to the same scalar source.
It also checks that the current repo does not yet contain the physical
same-source response evidence needed for positive Y_T closure.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_fh_top_w_response_ratio_gate_2026-05-25.json"

NOTE = DOCS / "YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md"
SOURCE_ACTION_STATUS = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
POLE_NOGO = DOCS / "YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md"
EW_MASS = DOCS / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
EW_COUPLING = DOCS / "EW_COUPLING_DERIVATION_NOTE.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

STRICT_TOP_W_ROWS = OUTPUT.parent / "yt_fh_top_w_strict_response_rows_2026-05-25.json"
STRICT_WZ_PACKET = OUTPUT.parent / "yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json"
SYMBOLIC_TOP_PACKET = OUTPUT.parent / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"

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


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and current authority")
    for path in (NOTE, SOURCE_ACTION_STATUS, POLE_NOGO, EW_MASS, EW_COUPLING, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    required = [
        "Same-Source Top/W Response Ratio",
        "Transfer-Matrix Feynman-Hellmann Form",
        "Why This Beats The Pole-Row Normalization No-Go",
        "Current Attempt Result",
        "Non-Claims",
    ]
    for phrase in required:
        check(f"note contains required section: {phrase}", phrase in note)

    ew_mass_row = ledger_row("ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26")
    source_action_row = ledger_row("yt_source_action_support_packet_note_2026-05-22")
    pole_row = ledger_row("yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23")
    ew_coupling_row = ledger_row("ew_coupling_derivation_note")

    check("EW Higgs mass diagonalization row is present in the audit ledger (presence only)", ew_mass_row is not None)
    check("source-action support packet row is present in the audit ledger (presence only)", source_action_row is not None)
    check("pole-row normalization no-go row is present in the audit ledger (presence only)", pole_row is not None)
    check("EW coupling note row is present in the audit ledger (presence only)", ew_coupling_row is not None)
    print(
        "  [info] live effective statuses (audit-lane-owned; not gated): "
        f"ew_mass={(ew_mass_row or {}).get('effective_status')!r}, "
        f"source_action={(source_action_row or {}).get('effective_status')!r}, "
        f"pole_no_go={(pole_row or {}).get('effective_status')!r}, "
        f"ew_coupling={(ew_coupling_row or {}).get('effective_status')!r}"
    )

    return {
        "ew_mass_status": (ew_mass_row or {}).get("effective_status"),
        "source_action_status": (source_action_row or {}).get("effective_status"),
        "pole_no_go_status": (pole_row or {}).get("effective_status"),
        "ew_coupling_status": (ew_coupling_row or {}).get("effective_status"),
    }


def part2_transfer_matrix_fh() -> None:
    print("\nPart 2: transfer-matrix Feynman-Hellmann derivative identity")
    h, a = sp.symbols("h a", positive=True)
    lambda_t = sp.Function("Lambda_t")(h)
    lambda_0 = sp.Function("Lambda_0")(h)
    mass = -sp.log(lambda_t / lambda_0) / a
    derivative = sp.diff(mass, h)
    expected = -(sp.diff(lambda_t, h) / lambda_t - sp.diff(lambda_0, h) / lambda_0) / a
    check("d[-log(Lambda_t/Lambda_0)/a]/dh identity", is_zero(derivative - expected))


def part3_top_w_ratio() -> None:
    print("\nPart 3: same-source top/W response ratio")
    y, g, dv = sp.symbols("y_t g_2 dv_dh", positive=True)
    dmt = y * dv / sp.sqrt(2)
    dmw = g * dv / 2
    ratio = sp.simplify(dmt / dmw)
    recovered = sp.simplify(g / sp.sqrt(2) * ratio)
    check("response ratio equals sqrt(2) y_t / g_2", is_zero(ratio - sp.sqrt(2) * y / g), ratio)
    check("y_t recovered from g_2 and response ratio", is_zero(recovered - y), recovered)

    c = sp.symbols("c", positive=True)
    scaled_ratio = sp.simplify((dmt / c) / (dmw / c))
    check("same-source reparameterization h' = c h cancels", is_zero(scaled_ratio - ratio), scaled_ratio)


def part4_w_denominator() -> None:
    print("\nPart 4: retained W denominator algebra")
    g, gy, v = sp.symbols("g_2 g_Y v", positive=True)
    mw = g * v / 2
    mz = sp.sqrt(g**2 + gy**2) * v / 2
    ratio = sp.simplify(mw**2 / mz**2)
    check("M_W^2/M_Z^2 is v-independent", is_zero(sp.diff(ratio, v)), ratio)
    recovered_v = sp.simplify(2 * mw / g)
    check("absolute W response plus g_2 recovers v", is_zero(recovered_v - v), recovered_v)


def part5_current_blockers() -> dict[str, Any]:
    print("\nPart 5: current closure blockers")
    strict_top_w_present = STRICT_TOP_W_ROWS.exists()
    strict_wz_present = STRICT_WZ_PACKET.exists()
    symbolic_top_present = SYMBOLIC_TOP_PACKET.exists()
    check("symbolic top response row packet present", symbolic_top_present, SYMBOLIC_TOP_PACKET.relative_to(ROOT).as_posix())
    check("coefficient-certified top/W FH rows absent", not strict_top_w_present, STRICT_TOP_W_ROWS.relative_to(ROOT).as_posix())
    check("strict W/Z denominator-response packet present", strict_wz_present, STRICT_WZ_PACKET.relative_to(ROOT).as_posix())

    source_action_text = read(SOURCE_ACTION_STATUS)
    check(
        "source-action support note says physical neutral EW/Higgs authority remains open",
        "not yet accepted as current neutral EW/Higgs authority" in source_action_text
        or "not same-surface neutral EW/Higgs authority" in source_action_text,
    )
    check("source-action support note lists W/Z bypass as open gate", "same-source W/Z physical-response bypass" in source_action_text)

    return {
        "strict_top_w_rows_present": strict_top_w_present,
        "strict_wz_packet_present": strict_wz_present,
        "symbolic_top_response_row_present": symbolic_top_present,
        "same_source_ew_higgs_authority_present": False,
        "numerical_g2_retained_authority_present": False,
    }


def part6_firewalls() -> None:
    print("\nPart 6: firewalls")
    note = read(NOTE)
    required_firewalls = [
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "`alpha_LM`",
        "plaquette/u0",
        "PDG",
        "observed W/Z/top masses",
    ]
    for phrase in required_firewalls:
        check(f"firewall phrase present: {phrase}", phrase in note)

    forbidden = [
        "Status:** retained",
        "proposed_retained",
        "positive Y_T closure has been obtained",
        "This note derives a numerical `y_t`",
        "`kappa_Y = 0` is derived",
    ]
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T FH TOP/W RESPONSE-RATIO GATE")
    print("=" * 78)

    statuses = part1_anchors()
    part2_transfer_matrix_fh()
    part3_top_w_ratio()
    part4_w_denominator()
    blockers = part5_current_blockers()
    part6_firewalls()

    proposal_allowed = (
        blockers["strict_top_w_rows_present"]
        and blockers["numerical_g2_retained_authority_present"]
    )
    result = {
        "status": "exact conditional top/W response-ratio theorem; current repo remains open-gate",
        "route_algebra_closed": True,
        "proposal_allowed": proposal_allowed,
        "proposal_allowed_reason": (
            "Blocked: W/Z denominator response is present, but the source-action support "
            "packet is retained_bounded only, the symbolic top response row still has "
            "a free coefficient, coefficient-certified top FH rows are absent, and "
            "v-scale g_2 authority is not retained."
        ),
        "current_blockers": blockers,
        "upstream_statuses": statuses,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md",
            "scripts/frontier_yt_fh_top_w_response_ratio_gate.py",
            "outputs/yt_fh_top_w_response_ratio_gate_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
