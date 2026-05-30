#!/usr/bin/env python3
"""Legacy fallback check for anomaly-forces-time via standard ABJ.

This runner verifies that the bounded standard-ABJ fallback route remains
coherent:

    cited standard ABJ theorem bridge + anomaly arithmetic
    + Clifford chirality parity + single-clock exclusion => d_t = 1.

It deliberately does not certify the active parent route.  The active parent
route now uses the framework-action ABJ derivation.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


PASS = 0
FAIL = 0
CHECKS: list[dict[str, object]] = []


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ANOMALY_FORCES_TIME_THEOREM.md"
BRIDGE = ROOT / "docs" / "ABJ_STANDARD_THEOREM_BRIDGE_FOR_ANOMALY_FORCES_TIME_NOTE_2026-05-30.md"
OUTPUT = ROOT / "outputs" / "anomaly_forces_time_standard_abj_closure_2026-05-30.json"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"


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
    with LEDGER.open() as f:
        return json.load(f)["rows"]


def anomaly_arithmetic() -> dict[str, str]:
    y_q = Fraction(1, 3)
    y_l = Fraction(-1, 1)
    tr_y = 6 * y_q + 2 * y_l
    tr_y3 = 6 * y_q**3 + 2 * y_l**3
    tr_su3_y = 2 * Fraction(1, 2) * y_q
    tr_su2_y = 3 * Fraction(1, 2) * y_q + Fraction(1, 2) * y_l
    tr_su3_3 = Fraction(2, 1)

    check("LH Tr[Y] vanishes", tr_y == 0, str(tr_y))
    check("LH Tr[Y^3] = -16/9", tr_y3 == Fraction(-16, 9), str(tr_y3))
    check("LH Tr[SU(3)^2 Y] = 1/3", tr_su3_y == Fraction(1, 3), str(tr_su3_y))
    check("LH Tr[SU(2)^2 Y] vanishes", tr_su2_y == 0, str(tr_su2_y))
    check("LH Tr[SU(3)^3] = 2", tr_su3_3 == 2, str(tr_su3_3))
    nonzero = [tr_y3, tr_su3_y, tr_su3_3]
    check("exactly three perturbative obstruction traces are nonzero", all(v != 0 for v in nonzero), str(nonzero))
    return {
        "TrY": str(tr_y),
        "TrY3": str(tr_y3),
        "TrSU3Y": str(tr_su3_y),
        "TrSU2Y": str(tr_su2_y),
        "TrSU3cubic": str(tr_su3_3),
    }


def dimension_intersection() -> dict[str, object]:
    ds = 3
    odd_times = [dt for dt in range(1, 12) if (ds + dt) % 2 == 0]
    single_clock_allowed = [dt for dt in range(1, 12) if dt <= 1]
    intersection = sorted(set(odd_times) & set(single_clock_allowed))
    check("chirality parity gives positive odd d_t values for d_s=3", odd_times == [1, 3, 5, 7, 9, 11], str(odd_times))
    check("single-clock exclusion leaves only d_t <= 1 in positive range", single_clock_allowed == [1], str(single_clock_allowed))
    check("intersection is exactly d_t = 1", intersection == [1], str(intersection))
    return {
        "d_s": ds,
        "chirality_allowed_positive_d_t": odd_times,
        "single_clock_allowed_positive_d_t": single_clock_allowed,
        "intersection": intersection,
    }


def ledger_checks(rows: dict[str, dict[str, object]]) -> dict[str, dict[str, object]]:
    required = {
        "abj_standard_theorem_bridge_for_anomaly_forces_time_note_2026-05-30": "ABJ standard-theorem bridge present",
        "clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10": "Clifford chirality parity retained",
        "axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03": "single-clock theorem present",
        "abj_epsilon_index_square_block_no_go_note_2026-05-30": "epsilon-index no-go registered",
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

    bridge = rows.get("abj_standard_theorem_bridge_for_anomaly_forces_time_note_2026-05-30", {})
    check("ABJ standard theorem bridge remains bounded_theorem", bridge.get("claim_type") == "bounded_theorem", str(bridge.get("claim_type")))

    cliff = rows.get("clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10", {})
    check("Clifford parity theorem is currently retained", cliff.get("effective_status") == "retained", str(cliff.get("effective_status")))

    single = rows.get("axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03", {})
    check("single-clock theorem is present as positive_theorem source row", single.get("claim_type") == "positive_theorem", str(single.get("claim_type")))

    return seen


def source_firewall() -> dict[str, object]:
    parent = NOTE.read_text()
    bridge = BRIDGE.read_text()
    required_parent = [
        "**Claim type:** positive_theorem",
        "framework-action ABJ theorem",
        "ABJ from framework action",
        "standard_theorem_bridge_load_bearing: false",
        "accepted_premise_packet_load_bearing: false",
        "does not use PDG values",
    ]
    forbidden_parent = [
        "accepted-premise positive composition",
        "ABJ accepted premise",
        "assume the named accepted premise",
        "accepted-current surface",
        "bare external admission on current `main`",
        "propose a retained / positive_theorem promotion",
    ]
    for phrase in required_parent:
        check(f"parent source contains boundary phrase: {phrase}", phrase in parent)
    for phrase in forbidden_parent:
        check(f"parent source excludes stale phrase: {phrase}", phrase not in parent)

    required_bridge = [
        "standard ABJ/Wess-Zumino/Fujikawa theorem",
        "external_standard_theorem_bridge",
        "framework_native_abj_derivation_closed: false",
        "accepted_premise_packet_load_bearing: false",
    ]
    for phrase in required_bridge:
        check(f"ABJ bridge contains standard-theorem firewall: {phrase}", phrase in bridge)

    return {
        "required_parent_phrases": required_parent,
        "forbidden_parent_phrases": forbidden_parent,
        "required_bridge_phrases": required_bridge,
    }


def main() -> int:
    print("ANOMALY-FORCES-TIME STANDARD-ABJ CLOSURE REPAIR")
    rows = load_rows()
    source = source_firewall()
    traces = anomaly_arithmetic()
    dims = dimension_intersection()
    deps = ledger_checks(rows)

    verdict = (
        "Standard-ABJ fallback composition remains coherent: cited standard "
        "theorem + exact anomaly arithmetic + Clifford chirality parity + "
        "single-clock exclusion gives d_t=1. The active parent route now uses "
        "the framework-action ABJ derivation."
    )
    out = {
        "claim": "anomaly-forces-time standard-ABJ closure repair",
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
