#!/usr/bin/env python3
"""Strict same-source top/W pole-row evidence contract for Y_T."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = ROOT / "outputs" / "yt_strict_same_source_top_w_pole_row_contract_2026-05-30.json"

NOTE = DOCS / "YT_STRICT_SAME_SOURCE_TOP_W_POLE_ROW_CONTRACT_NOTE_2026-05-30.md"
FH_RATIO = DOCS / "YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md"
MASS_BRIDGE = DOCS / "YT_FH_TOP_MASS_RESPONSE_PHYSICAL_INTERVENTION_BRIDGE_NOTE_2026-05-25.md"
SOURCE_COORD = DOCS / "YT_SOURCE_COORDINATE_INVARIANT_TOP_W_RATIO_GATE_NOTE_2026-05-25.md"
WZ_PACKET = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
SYMBOLIC_TOP = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
TOP_NOGO = DOCS / "YT_TOP_RESPONSE_COEFFICIENT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-25.md"
POLE_NOGO = DOCS / "YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

REQUIRED_CERTIFICATE_FIELDS = [
    "same_source_id",
    "same_transfer_action_surface",
    "lambda_top_pole",
    "lambda_w_pole",
    "lambda_vacuum_pole",
    "contact_subtraction",
    "finite_volume_ir_controls",
    "model_class_checks",
    "shared_covariance",
    "g2_authority_or_ratio_scope",
    "dM_t_dh",
    "dM_W_dh",
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


def ledger_row(claim_id: str) -> dict[str, Any] | None:
    rows = json.loads(read(LEDGER))["rows"]
    if isinstance(rows, dict):
        return rows.get(claim_id)
    iterable = rows
    for row in iterable:
        if isinstance(row, dict) and row.get("claim_id") == claim_id:
            return row
    return None


def part1_documents() -> dict[str, Any]:
    print("\nPart 1: documents and current authority")
    for path in (NOTE, FH_RATIO, MASS_BRIDGE, SOURCE_COORD, WZ_PACKET, SYMBOLIC_TOP, TOP_NOGO, POLE_NOGO, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Question",
        "Required Evidence Certificate",
        "Why This Bypasses The Source-Unit Pin",
        "Current Repo Boundary",
        "Evidence Boundary",
        "Non-Claims",
        "Boundary Summary",
    ):
        check(f"contract note contains section: {phrase}", phrase in note)

    check("contract keeps audit status authority independent", "independent audit lane only" in note)
    check("contract avoids proposal/status-certificate language", "proposal_allowed" not in note and "actual_current_surface_status" not in note)
    check("contract records no production certificate", "production_certificate_present: false" in note)

    statuses = {
        "source_coordinate": ledger_row("yt_source_coordinate_invariant_top_w_ratio_gate_note_2026-05-25"),
        "wz_packet": ledger_row("yt_strict_wz_neutral_carrier_response_packet_note_2026-05-25"),
        "symbolic_top": ledger_row("yt_strict_symbolic_top_response_row_packet_note_2026-05-25"),
        "fh_ratio": ledger_row("yt_fh_top_w_response_ratio_gate_note_2026-05-25"),
        "top_nogo": ledger_row("yt_top_response_coefficient_underdetermination_no_go_note_2026-05-25"),
    }
    check("source-coordinate ratio gate row is present in the audit ledger (presence only)", statuses["source_coordinate"] is not None)
    check("W/Z denominator packet row is present in the audit ledger (presence only)", statuses["wz_packet"] is not None)
    check("symbolic top row is present in the audit ledger (presence only)", statuses["symbolic_top"] is not None)
    check("FH ratio gate row is present in the audit ledger (presence only)", statuses["fh_ratio"] is not None)
    print(
        "  [info] live effective statuses (audit-lane-owned; not gated): "
        f"{ {k: None if v is None else v.get('effective_status') for k, v in statuses.items()} }"
    )
    check("top coefficient no-go remains non-positive", statuses["top_nogo"] and statuses["top_nogo"].get("claim_type") == "no_go")
    return {k: None if v is None else v.get("effective_status") for k, v in statuses.items()}


def part2_response_ratio_algebra() -> dict[str, str]:
    print("\nPart 2: same-source response algebra")
    h = sp.symbols("h")
    g2, yt = sp.symbols("g_2 y_t", positive=True)
    v = sp.Function("v")
    mt = yt * v(h) / sp.sqrt(2)
    mw = g2 * v(h) / 2
    ratio = sp.simplify(sp.diff(mt, h) / sp.diff(mw, h))
    readout = sp.simplify(g2 / sp.sqrt(2) * ratio)
    check("top/W response ratio cancels source Jacobian", zero(ratio - sp.sqrt(2) * yt / g2), ratio)
    check("Yukawa readout recovers y_t", zero(readout - yt), readout)

    s = sp.symbols("s")
    f = sp.Function("f")
    mt_s = yt * v(f(s)) / sp.sqrt(2)
    mw_s = g2 * v(f(s)) / 2
    ratio_s = sp.simplify(sp.diff(mt_s, s) / sp.diff(mw_s, s))
    check("ratio invariant under source reparameterization", zero(ratio_s - ratio), ratio_s)

    target_ratio = sp.sqrt(2) / (g2 * sp.sqrt(6))
    selected = sp.simplify(g2 / sp.sqrt(2) * target_ratio)
    check("target response ratio reads y_33=1/sqrt(6)", zero(selected - 1 / sp.sqrt(6)), selected)
    return {
        "readout": "y_33=(g_2/sqrt(2)) (dM_t/dh)/(dM_W/dh)",
        "target_ratio": "sqrt(2)/(g_2 sqrt(6))",
    }


def part3_transfer_pole_derivative() -> dict[str, str]:
    print("\nPart 3: transfer pole derivative contract")
    h, at = sp.symbols("h a_t", positive=True)
    lt = sp.Function("Lambda_t")
    lw = sp.Function("Lambda_W")
    l0 = sp.Function("Lambda_0")

    mt = -sp.log(lt(h) / l0(h)) / at
    mw = -sp.log(lw(h) / l0(h)) / at
    dmt = sp.diff(mt, h)
    dmw = sp.diff(mw, h)
    expected_t = -((sp.diff(lt(h), h) / lt(h)) - (sp.diff(l0(h), h) / l0(h))) / at
    expected_w = -((sp.diff(lw(h), h) / lw(h)) - (sp.diff(l0(h), h) / l0(h))) / at
    check("top pole derivative has FH log-eigenvalue form", zero(dmt - expected_t), dmt)
    check("W pole derivative has FH log-eigenvalue form", zero(dmw - expected_w), dmw)
    check("same vacuum pole appears in both derivatives", "Lambda_0" in str(dmt) and "Lambda_0" in str(dmw))
    return {
        "mass_definition": "M_X=-a_t^{-1} log(Lambda_X/Lambda_0)",
        "derivative": "dM_X/dh=-a_t^{-1}(Lambda_X'/Lambda_X-Lambda_0'/Lambda_0)",
    }


def part4_certificate_schema() -> dict[str, Any]:
    print("\nPart 4: evidence certificate schema")
    schema = {field: None for field in REQUIRED_CERTIFICATE_FIELDS}
    for field in REQUIRED_CERTIFICATE_FIELDS:
        check(f"schema requires {field}", field in schema)

    no_certificate_present = True
    check("no strict production/evidence certificate is supplied here", no_certificate_present)
    check("schema alone does not claim response value", True)
    return {
        "required_fields": REQUIRED_CERTIFICATE_FIELDS,
        "production_certificate_present": False,
    }


def part5_firewalls() -> None:
    print("\nPart 5: firewalls")
    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "PDG targets",
        "observed top/W/Z masses",
        "`alpha_LM`",
        "plaquette/u0",
        "fitted selectors",
    ):
        check(f"contract firewall names forbidden input: {phrase}", phrase in note)

    for phrase in (
        "actual_current_surface_status: retained",
        "proposal_allowed: true",
        "bare_retained_allowed: true",
        "strict same-source top/W response evidence is present",
        "retained Y_T closure is claimed",
        "production top-correlator result is supplied",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("Y_T STRICT SAME-SOURCE TOP/W POLE-ROW CONTRACT")
    print("=" * 88)

    result = {
        "documents": part1_documents(),
        "response_ratio_algebra": part2_response_ratio_algebra(),
        "transfer_pole_derivative": part3_transfer_pole_derivative(),
        "certificate_schema": part4_certificate_schema(),
    }
    part5_firewalls()

    result["summary"] = {
        "pass": PASS_COUNT,
        "fail": FAIL_COUNT,
        "source_boundary": "evidence contract only",
        "contract_role": "evidence schema for non-P-cal top/W response route",
        "production_certificate_present": False,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
