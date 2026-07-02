#!/usr/bin/env python3
"""Firewall for the gauge-algebra parent kinematic bridge wiring.

This runner does not derive the gauge subgroup selection. It checks that the
parent open-gate note consumes the retained-bounded local-frame / minimal-
coupling kinematic bridge for the link-transporter law, while still leaving
MR_color, factorwise subgroup selection, chiral su(2)_L, and gauge dynamics
open.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

RETAINED = {"retained", "retained_bounded", "retained_no_go"}

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if detail:
        print(f"       {detail}")
    PASS += int(ok)
    FAIL += int(not ok)


def ledger_status(claim_id: str) -> str | None:
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    row = rows.get(claim_id, {})
    return row.get("effective_status") or row.get("audit_status")


def main() -> int:
    print("GAUGE ALGEBRA PARENT KINEMATIC BRIDGE FIREWALL")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")
    flat = " ".join(note.split())

    retained_sources = {
        "fiber_frame_local_redundancy_bridge_narrow_theorem_note_2026-06-09":
            ledger_status("fiber_frame_local_redundancy_bridge_narrow_theorem_note_2026-06-09"),
        "matter_gauge_minimal_coupling_fiber_frame_forces_connection_narrow_theorem_note_2026-06-08":
            ledger_status("matter_gauge_minimal_coupling_fiber_frame_forces_connection_narrow_theorem_note_2026-06-08"),
        "gauge_gauging_selection_conjugation_independence_no_go_note_2026-06-16":
            ledger_status("gauge_gauging_selection_conjugation_independence_no_go_note_2026-06-16"),
    }

    check(
        "kinematic bridge authorities are retained-grade in the live ledger",
        all(status in RETAINED for status in retained_sources.values()),
        ", ".join(f"{cid}={status}" for cid, status in retained_sources.items()),
    )
    check(
        "parent note lists this firewall runner and cache",
        "gauge_algebra_parent_kinematic_bridge_firewall_2026_06_18.py" in note
        and "gauge_algebra_parent_kinematic_bridge_firewall_2026_06_18.txt" in note,
    )
    check(
        "old unstructured link-connection convention wording is retired",
        "the **link-connection convention**" not in note
        and "the single-qubit fibre algebra boundary" in note,
    )
    check(
        "parent note records retained-bounded local-frame link kinematics",
        "2026-06-18 kinematic bridge update" in note
        and "retained-bounded kinematic bridge" in note
        and "local-fibre-frame covariance now supplies the current-surface link transporter" in flat,
    )
    check(
        "parent note cites the retained-bounded kinematic bridge notes",
        "FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md" in note
        and "MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md" in note,
    )
    check(
        "MR_color and factor-locality remain open",
        "does **not** derive `MR_color` or factor-locality" in note
        and "factor-locality/`MR_color`" in note,
    )
    check(
        "factorwise subgroup selection remains open",
        "does **not** select the factorwise" in note
        and "selection of the factorwise subgroup" in note,
    )
    check(
        "chiral weak coupling and gauge dynamics remain open",
        "does **not** derive chiral `su(2)_L`" in flat
        and "does **not** supply gauge action, dynamics" in flat
        and "chiral `su(2)_L`, and gauge action/dynamics" in flat,
    )
    check(
        "status and audit authority are not promoted by this source change",
        "**Claim type:** open_gate" in note
        and "independent audit lane only" in note
        and "audited_clean" not in note
        and "proposed_retained" not in note,
    )

    print()
    print(
        "VERDICT: retained-bounded local-frame/minimal-coupling kinematics are "
        "wired into the parent gauge row, while MR_color, factorwise subgroup "
        "selection, chiral su(2)_L, and gauge dynamics remain open."
    )
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
