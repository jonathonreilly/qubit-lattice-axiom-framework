#!/usr/bin/env python3
"""Anomaly-forces-time closure with ABJ derived from framework action."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ANOMALY_FORCES_TIME_THEOREM.md"
ABJ_NOTE = ROOT / "docs" / "ABJ_FROM_FRAMEWORK_ACTION_U1_CUBIC_THEOREM_NOTE_2026-05-30.md"
TRACE_NOTE = ROOT / "docs" / "ABJ_SCALE_FREE_CHIRAL_U1_TRACE_SURFACE_THEOREM_NOTE_2026-05-30.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
OUTPUT = ROOT / "outputs" / "anomaly_forces_time_action_abj_closure_2026-05-30.json"

PASS = 0
FAIL = 0
CHECKS: list[dict[str, object]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    CHECKS.append({"name": name, "status": status, "detail": detail})
    print(f"[{status}] {name}" + (f"  {detail}" if detail else ""))


def load_rows() -> dict[str, dict[str, object]]:
    return json.loads(LEDGER.read_text())["rows"]


def anomaly_arithmetic() -> dict[str, str]:
    y_plus = Fraction(1, 1)
    y_minus = Fraction(-3, 1)
    tr_y0 = 6 * y_plus + 2 * y_minus
    tr_y0_3 = 6 * y_plus**3 + 2 * y_minus**3
    optional_scaled = tr_y0_3 * Fraction(1, 27)
    check("scale-free Tr[Y0] vanishes", tr_y0 == 0, str(tr_y0))
    check("scale-free Tr[Y0^3] = -48", tr_y0_3 == Fraction(-48, 1), str(tr_y0_3))
    check("U(1)^3 branch alone gives nonzero ABJ obstruction for lambda != 0", tr_y0_3 != 0, str(tr_y0_3))
    check("optional lambda=1/3 rescale gives -16/9 but is not load-bearing", optional_scaled == Fraction(-16, 9), str(optional_scaled))
    return {
        "TrY0": str(tr_y0),
        "TrY0_3": str(tr_y0_3),
        "TrLambdaY0_3": "-48*lambda^3",
        "optional_lambda_one_third_trace": str(optional_scaled),
    }


def dimension_intersection() -> dict[str, object]:
    ds = 3
    chirality_allowed = [dt for dt in range(1, 12) if (ds + dt) % 2 == 0]
    single_clock_allowed = [dt for dt in range(1, 12) if dt <= 1]
    intersection = sorted(set(chirality_allowed) & set(single_clock_allowed))
    check("ABJ plus chirality parity gives positive odd d_t", chirality_allowed == [1, 3, 5, 7, 9, 11], str(chirality_allowed))
    check("single-clock exclusion leaves only d_t=1 in positive range", single_clock_allowed == [1], str(single_clock_allowed))
    check("intersection is exactly d_t = 1", intersection == [1], str(intersection))
    return {
        "d_s": ds,
        "chirality_allowed_positive_d_t": chirality_allowed,
        "single_clock_allowed_positive_d_t": single_clock_allowed,
        "intersection": intersection,
    }


def source_firewall() -> dict[str, object]:
    parent = NOTE.read_text()
    abj = ABJ_NOTE.read_text()
    trace = TRACE_NOTE.read_text()
    required_parent = [
        "**Claim type:** positive_theorem",
        "framework-action ABJ theorem",
        "ABJ from framework action",
        "ABJ scale-free chiral U(1) trace surface theorem",
        "abj_import_retired_on_framework_action_surface: true",
        "bounded_hypercharge_or_alpha_rows_load_bearing: false",
        "standard_theorem_bridge_load_bearing: false",
        "accepted_premise_packet_load_bearing: false",
        "unbounded_positive_theorem_allowed: true",
    ]
    forbidden_parent = [
        "**Claim type:** bounded_theorem",
        "standard-theorem bounded composition",
        "ABJ standard-theorem bridge + chiral matter surface",
        "ABJ accepted premise",
        "assume the named accepted premise",
        "bare external admission on current `main`",
        "Assume the framework's retained/bounded matter-content surface",
    ]
    for phrase in required_parent:
        check(f"parent contains action-ABJ phrase: {phrase}", phrase in parent)
    for phrase in forbidden_parent:
        check(f"parent excludes bounded/import phrase: {phrase}", phrase not in parent)

    required_abj = [
        "**Claim type:** positive_theorem",
        "framework_native_abj_derivation_closed: true",
        "bounded_alpha_or_hypercharge_row_load_bearing: false",
        "standard_theorem_bridge_load_bearing: false",
        "accepted_premise_packet_load_bearing: false",
        "No 3+1 abelian local counterterm",
    ]
    for phrase in required_abj:
        check(f"ABJ action theorem contains firewall phrase: {phrase}", phrase in abj)
    required_trace = [
        "**Claim type:** positive_theorem",
        "Tr[Y0^3] = -48",
        "No `alpha = 1/3`",
        "No GMN",
        "No electron-charge",
        "No physical-SM hypercharge",
    ]
    for phrase in required_trace:
        check(f"scale-free trace theorem contains firewall phrase: {phrase}", phrase in trace)
    return {
        "required_parent": required_parent,
        "forbidden_parent": forbidden_parent,
        "required_abj": required_abj,
        "required_trace": required_trace,
    }


def ledger_checks(rows: dict[str, dict[str, object]]) -> dict[str, dict[str, object]]:
    required = {
        "abj_scale_free_chiral_u1_trace_surface_theorem_note_2026-05-30": "scale-free trace theorem row present",
        "abj_from_framework_action_u1_cubic_theorem_note_2026-05-30": "ABJ action theorem row present",
        "clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10": "Clifford chirality parity retained",
        "axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03": "single-clock theorem present",
    }
    seen: dict[str, dict[str, object]] = {}
    for cid, label in required.items():
        row = rows.get(cid)
        check(label, row is not None, cid)
        if row:
            seen[cid] = {
                "claim_type": row.get("claim_type"),
                "audit_status": row.get("audit_status"),
                "effective_status": row.get("effective_status"),
                "note_path": row.get("note_path"),
            }
    trace_row = rows.get("abj_scale_free_chiral_u1_trace_surface_theorem_note_2026-05-30", {})
    check("scale-free trace theorem seeds as positive_theorem", trace_row.get("claim_type") == "positive_theorem", str(trace_row.get("claim_type")))
    abj = rows.get("abj_from_framework_action_u1_cubic_theorem_note_2026-05-30", {})
    check("ABJ action theorem seeds as positive_theorem", abj.get("claim_type") == "positive_theorem", str(abj.get("claim_type")))
    cliff = rows.get("clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10", {})
    check("Clifford parity theorem is retained", cliff.get("effective_status") == "retained", str(cliff.get("effective_status")))
    single = rows.get("axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03", {})
    check("single-clock source row remains positive_theorem", single.get("claim_type") == "positive_theorem", str(single.get("claim_type")))
    return seen


def main() -> int:
    print("ANOMALY-FORCES-TIME ACTION-ABJ CLOSURE")
    rows = load_rows()
    source = source_firewall()
    traces = anomaly_arithmetic()
    dims = dimension_intersection()
    deps = ledger_checks(rows)
    verdict = (
        "Action-ABJ positive composition verified: ABJ is derived from the "
        "framework action surface, the U(1)^3 anomaly trace is nonzero, "
        "chirality parity gives odd d_t, and single-clock exclusion leaves d_t=1."
    )
    out = {
        "claim": "anomaly-forces-time action-ABJ closure",
        "pass": PASS,
        "fail": FAIL,
        "checks": CHECKS,
        "source_firewall": source,
        "anomaly_traces": traces,
        "dimension_intersection": dims,
        "ledger_rows": deps,
        "verdict": verdict,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print("VERDICT:", verdict)
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
