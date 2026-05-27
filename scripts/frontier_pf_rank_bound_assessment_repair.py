#!/usr/bin/env python3
"""Bounded gap-assessment runner for the PF rank-bound citation note."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "PLAQUETTE_V1_PICARD_FUCHS_ODE_RANK_BOUND_CITATION_NOTE_2026-05-06.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PASS = 0
FAIL = 0

RETAINED_DEPS = [
    "plaquette_v1_picard_fuchs_ode_note_2026-05-05",
    "plaquette_v1_picard_fuchs_ode_minimality_proof_note_2026-05-06",
    "plaquette_v1_picard_fuchs_ode_koutschan_minimality_note_2026-05-06",
    "plaquette_v1_picard_fuchs_ode_rank_exclusion_r2_d12_narrow_theorem_note_2026-05-17",
]


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def one_line(text: str) -> str:
    return " ".join(text.split())


def ledger_rows() -> dict[str, dict[str, Any]]:
    return json.loads(read(LEDGER))["rows"]


def retained_bounded(status: str | None) -> bool:
    return status == "retained_bounded"


def main() -> int:
    print("# PF rank-bound citation bounded assessment repair")
    text = read(NOTE)
    flat = one_line(text)
    rows = ledger_rows()

    required_phrases = [
        "bounded gap-assessment support only",
        "does not claim an all-degree rank theorem",
        "does not claim an all-degree rank theorem",
        "all-order minimal-annihilator theorem",
        "2026-05-27 Runner And Scope Repair",
        "old textbook-style `rank <= N` citation is not established",
        "all-degree / all-order minimal-annihilator conclusion remains open",
        "It does not convert the assessment into an all-order rank theorem",
        "This note classifies the deliverable as **PARTIAL**",
    ]
    for phrase in required_phrases:
        check(f"source contains boundary phrase: {phrase}", phrase in flat)

    for cid in RETAINED_DEPS:
        row = rows[cid]
        check(f"{cid} is retained_bounded", retained_bounded(row.get("effective_status")), row.get("effective_status"))

    target = rows["plaquette_v1_picard_fuchs_ode_rank_bound_citation_note_2026-05-06"]
    check("target claim type is bounded_theorem", target.get("claim_type") == "bounded_theorem", target.get("claim_type"))
    check("target source path is correct", target.get("note_path") == "docs/PLAQUETTE_V1_PICARD_FUCHS_ODE_RANK_BOUND_CITATION_NOTE_2026-05-06.md")

    forbidden = [
        "all-degree rank theorem is proved",
        "all-order minimal-annihilator theorem is proved",
        "rank(J) <= 3 is retained",
        "classified as **UPGRADE-READY**",
    ]
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in text)

    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
