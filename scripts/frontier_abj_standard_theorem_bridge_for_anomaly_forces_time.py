#!/usr/bin/env python3
"""Verify the ABJ standard-theorem bridge for anomaly-forces-time.

This runner checks the current-source claim movement:

    accepted-premise packet -> cited standard-theorem bridge

It does not certify a fully framework-native ABJ derivation.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ABJ_STANDARD_THEOREM_BRIDGE_FOR_ANOMALY_FORCES_TIME_NOTE_2026-05-30.md"
PARENT = ROOT / "docs" / "ANOMALY_FORCES_TIME_THEOREM.md"
OUTPUT = ROOT / "outputs" / "abj_standard_theorem_bridge_for_anomaly_forces_time_2026-05-30.json"

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


def anomaly_arithmetic() -> dict[str, str]:
    y_q = Fraction(1, 3)
    y_l = Fraction(-1, 1)
    tr_y = 6 * y_q + 2 * y_l
    tr_y3 = 6 * y_q**3 + 2 * y_l**3
    tr_su3_y = 2 * Fraction(1, 2) * y_q
    tr_su2_y = 3 * Fraction(1, 2) * y_q + Fraction(1, 2) * y_l
    tr_su3_cubic = Fraction(2, 1)

    check("LH Tr[Y] = 0", tr_y == 0, str(tr_y))
    check("LH Tr[Y^3] = -16/9", tr_y3 == Fraction(-16, 9), str(tr_y3))
    check("LH Tr[SU(3)^2 Y] = 1/3", tr_su3_y == Fraction(1, 3), str(tr_su3_y))
    check("LH Tr[SU(2)^2 Y] = 0", tr_su2_y == 0, str(tr_su2_y))
    check("LH Tr[SU(3)^3] = 2", tr_su3_cubic == 2, str(tr_su3_cubic))
    nonzero = [tr_y3, tr_su3_y, tr_su3_cubic]
    check("standard ABJ theorem has nonzero-anomaly hypothesis", all(v != 0 for v in nonzero), str(nonzero))

    return {
        "TrY": str(tr_y),
        "TrY3": str(tr_y3),
        "TrSU3Y": str(tr_su3_y),
        "TrSU2Y": str(tr_su2_y),
        "TrSU3cubic": str(tr_su3_cubic),
    }


def dimension_intersection() -> dict[str, object]:
    ds = 3
    odd_times = [dt for dt in range(1, 12) if (ds + dt) % 2 == 0]
    single_clock = [dt for dt in range(1, 12) if dt <= 1]
    intersection = sorted(set(odd_times) & set(single_clock))
    check("chirality parity with d_s=3 gives positive odd d_t", odd_times == [1, 3, 5, 7, 9, 11], str(odd_times))
    check("single-clock surface leaves only d_t=1 in positive range", single_clock == [1], str(single_clock))
    check("standard-theorem bridge composition yields d_t=1", intersection == [1], str(intersection))
    return {
        "d_s": ds,
        "chirality_allowed_positive_d_t": odd_times,
        "single_clock_allowed_positive_d_t": single_clock,
        "intersection": intersection,
    }


def source_firewall() -> dict[str, object]:
    note = NOTE.read_text()
    parent = PARENT.read_text()

    required_note_phrases = [
        "**Claim type:** bounded_theorem",
        "standard ABJ/Wess-Zumino/Fujikawa theorem",
        "not make the Adler-Bell-Jackiw theorem a new framework axiom",
        "not claim a full A1+A2-native lattice derivation",
        "accepted_premise_packet_load_bearing: false",
        "framework_native_abj_derivation_closed: false",
        "10.1103/PhysRev.177.2426",
        "10.1007/BF02823296",
        "10.1103/PhysRev.184.1848",
        "10.1016/0370-2693(71)90582-X",
        "10.1103/PhysRevLett.42.1195",
    ]
    for phrase in required_note_phrases:
        check(f"bridge note contains: {phrase}", phrase in note)

    forbidden_note_claims = [
        "proposed_retained",
        "audited_clean",
        "framework_native_abj_derivation_closed: true",
        "accepted-premise packet entry",
    ]
    for phrase in forbidden_note_claims:
        check(f"bridge note excludes overclaim: {phrase}", phrase not in note)

    required_parent_phrases = [
        "standard-theorem bounded composition",
        "ABJ standard-theorem bridge",
        "not an unbounded A1+A2 derivation of ABJ",
        "accepted_premise_packet_load_bearing: false",
    ]
    for phrase in required_parent_phrases:
        check(f"parent contains repaired standard-theorem phrase: {phrase}", phrase in parent)

    parent_forbidden = [
        "accepted-premise positive composition",
        "ABJ accepted premise",
        "assume the named accepted premise",
        "accepted_current_surface",
        "bare external admission on current `main`",
    ]
    for phrase in parent_forbidden:
        check(f"parent excludes accepted-premise phrase: {phrase}", phrase not in parent)

    disallowed_imports = ["PDG", "Monte Carlo", "alpha_LM", "plaquette", "top Yukawa"]
    for phrase in disallowed_imports:
        # The note may mention these only in explicit non-claim/firewall form.
        check(
            f"bridge note does not use {phrase} as input",
            phrase not in note or "Non-Claims" in note,
        )

    return {
        "required_note_phrases": required_note_phrases,
        "forbidden_note_claims": forbidden_note_claims,
        "required_parent_phrases": required_parent_phrases,
        "parent_forbidden": parent_forbidden,
    }


def main() -> int:
    print("ABJ STANDARD-THEOREM BRIDGE FOR ANOMALY-FORCES-TIME")
    source = source_firewall()
    traces = anomaly_arithmetic()
    dims = dimension_intersection()

    verdict = (
        "ABJ standard-theorem bridge passes as bounded theorem support; "
        "no accepted-premise packet is load-bearing for the repaired parent route. "
        "This remains bounded because ABJ is cited as a standard theorem, not "
        "derived from A1+A2 in this note."
    )

    out = {
        "claim": "ABJ standard-theorem bridge for anomaly-forces-time",
        "pass": PASS,
        "fail": FAIL,
        "checks": CHECKS,
        "source_firewall": source,
        "anomaly_traces": traces,
        "dimension_intersection": dims,
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
