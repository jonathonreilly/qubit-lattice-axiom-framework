#!/usr/bin/env python3
"""Cycle-302 synthesis for the joint physical six-mode coin lift."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
ROUTE = ROOT / "scripts/physical_cycle269_joint_six_mode_coin_lift_cycle302_2026_07_17.py"
ROUTE_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_JOINT_SIX_MODE_COIN_LIFT_CYCLE302_NOTE_2026-07-17.md"
)
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "JOINT_SIX_MODE_COIN_BRIDGE_SYNTHESIS_CYCLE302_NOTE_2026-07-17.md"
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
        "30-by-6 shell isometry",
        "five non-antipodal reference rays",
        "bounded physical matrix-unit polynomial",
        "at most 54 m2",
        "gf(2) cocycle",
        "unique up to global sign",
        "raw equal-phase shell",
        "rest-mass firewall",
        "not physical energy",
        "not a rate",
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
    check("the synthesis pins the physical coin, ledger, and N1--N8", not missing, missing)


def cold_route() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROUTE)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    match = re.search(r"SUMMARY\s+\{'pass':\s*(\d+),\s*'fail':\s*(\d+)\}", completed.stdout)
    observed = tuple(int(item) for item in match.groups()) if match else None
    check(
        "the independently reviewed coin route passes",
        completed.returncode == 0 and observed == (47, 0),
        {"returncode": completed.returncode, "observed": observed},
    )


def boundary_guards() -> None:
    route = normalized(ROUTE_NOTE)
    check(
        "the dense coefficient block has a bounded physical completion",
        "dense block is not by itself called the physical update" in route
        and "bounded physical polynomial" in route
        and "other 4,066 local tag patterns" in route,
    )
    check(
        "the phase defect is repaired locally without a preferred axis order",
        "108 of the 144" in route
        and "720 equations" in route
        and "unique up to" in route
        and "no preferred axis order" in route,
    )
    check(
        "the route keeps preparation, position, composition, and semantics open",
        "absolute vacuum preparation remains open" in route
        and "coherent position remains open" in route
        and "stream/contact composition" in route
        and "not physical energy" in route,
    )


def main() -> int:
    note_contract()
    cold_route()
    boundary_guards()
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
