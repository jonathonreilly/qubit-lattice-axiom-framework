#!/usr/bin/env python3
"""Cycle-299 synthesis for the collision-safe physical catch-up component."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
ROUTE = ROOT / "scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py"
ROUTE_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_COLLISION_SAFE_AUXILIARY_PORTS_NOTE_2026-07-17.md"
)
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COLLISION_SAFE_PHYSICAL_CATCHUP_SYNTHESIS_CYCLE299_NOTE_2026-07-17.md"
)
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "ten-m2",
        "six auxiliary port m2 per cell",
        "four-bit matter/port",
        "not an assembled encoded macrostep",
        "not physical time",
        "c_ref",
        "c_num",
        "c_wrap",
        "c_int",
        "c_local",
        "c_source",
        "n1 — alternative routes",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "gate status: fail for the candidate broad negative; do not ship it",
        "no shared obstruction was identified",
        "no axiom pressure was established",
    )
    missing = tuple(item for item in required if item not in text)
    check("the synthesis pins scope, ledger, and N1--N8", not missing, missing)


def cold_route() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROUTE)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    match = re.search(r"SUMMARY:\s+(\d+)\s+passed,\s+(\d+)\s+failed", completed.stdout)
    observed = tuple(int(item) for item in match.groups()) if match else None
    check(
        "the independently reviewed collision-safe route passes",
        completed.returncode == 0 and observed == (10, 0),
        {"returncode": completed.returncode, "observed": observed},
    )


def boundary_guards() -> None:
    route = normalized(ROUTE_NOTE)
    check(
        "physical and decoded surfaces remain distinct",
        "physical ten-m2 catch-up gate and decoded four-bit macrostep are separate" in route
        and "not an assembled encoded stream/catch-up matrix" in route,
    )
    check(
        "the failed axis word is narrow and alternate schedules remain open",
        "noncovariance only for the tested three-axis shared-cell word" in route
        and "other constant-depth colorings" in route,
    )
    check(
        "the route keeps state, coin routing, contact, and semantics open",
        "bounded physical state encoder" in route
        and "joint matter-coin/port-routing" in route
        and "same-code contact seam" in route
        and "port tag is not a record" in route,
    )


def main() -> int:
    note_contract()
    cold_route()
    boundary_guards()
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
