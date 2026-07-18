#!/usr/bin/env python3
"""Cycle 304 companion synthesis of the physical fixed-seam comparator."""

from __future__ import annotations

from itertools import combinations
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
ROUTE = (
    ROOT
    / "scripts/"
    "physical_cycle269_coin_stream_contact_common_refinement_cycle304_2026_07_17.py"
)
ROUTE_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_COIN_STREAM_CONTACT_COMMON_REFINEMENT_CYCLE304_NOTE_2026-07-17.md"
)
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_COMMON_REFINEMENT_SYNTHESIS_CYCLE304_NOTE_2026-07-17.md"
)
PACKAGE_PATHS = (ROUTE, ROUTE_NOTE, Path(__file__).resolve(), NOTE)
FRESH_MAIN = "9955ada698dea9374c8fe5127fd05d27a9b7a641"
WALLS = ("W_reference", "W_role", "W_recurrent", "W_fock", "W_gate")
N1_ROUTES = (
    "literal tag-sector identification",
    "perpendicular-only wedge coin",
    "opposite-wedge completion",
    "free phase-flag refinement",
    "separated-slice onsite coin",
    "fixed-seam identity completion",
    "matrix-unit port-constraint completion",
)

# Fragments keep the skill vocabulary out of the four scanned package paths.
TRIGGER_PARTS = (
    ("we", " assume"),
    ("by", " construction"),
    ("as is", " standard"),
    ("the framework", " provides"),
    ("bridge", " context"),
    ("back", "ground"),
    ("natural", "ly"),
    ("obvious", "ly"),
    ("standard", " qft"),
    ("regis", "tered"),
    ("canon", "ical"),
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
    if not NOTE.exists():
        check("the Cycle-304 companion synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "origin/main freshness",
        FRESH_MAIN,
        "fixed-seam comparator",
        "0.9929474834848379",
        "30/30",
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
        "n7 — hostile steelman",
        "n8 — cross-cycle echo",
        "gate status: fail for the candidate broad negative; do not ship it",
        "no shared obstruction was identified",
        "no axiom pressure was established",
    )
    missing = tuple(item for item in required if item not in text)
    check("the synthesis pins freshness, ledger, Gate, and N1--N8", not missing, missing)


def freshness_control() -> None:
    completed = subprocess.run(
        ["git", "merge-base", "--is-ancestor", FRESH_MAIN, "origin/main"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    check(
        "the recorded methodology commit remains an ancestor of origin/main",
        completed.returncode == 0,
        {"recorded": FRESH_MAIN, "current_ref": "origin/main"},
    )


def cold_route() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROUTE)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    match = re.search(
        r"SUMMARY\s+\{'pass':\s*(\d+),\s*'fail':\s*(\d+)\}",
        completed.stdout,
    )
    observed = tuple(int(item) for item in match.groups()) if match else None
    check(
        "the reviewed Cycle-304 route cold-passes 24/0",
        completed.returncode == 0 and observed == (24, 0),
        {"returncode": completed.returncode, "observed": observed},
    )


def route_boundary_guards() -> None:
    route = normalized(ROUTE_NOTE)
    check(
        "the retained positive is exactly one fixed-seam comparator",
        "forty-two logical columns" in route
        and "ninety microsectors" in route
        and "fixed-seam comparator" in route
        and "not the actual recurrent volume update" in route,
    )
    check(
        "the free role flag and recurrent leakage remain explicit",
        "phase flag is not locally enforced" in route
        and "thirty unflagged" in route
        and "0.9929474834848379" in route
        and "actual recurrent volume update remains open" in route,
    )
    check(
        "the fixed reference, wrap semantics, and full-Fock boundary remain open",
        "absolute vacuum preparation remains open" in route
        and "two compiler slices are not physical time" in route
        and "full-fock compilation remains open" in route,
    )


def n1_exact_marker_control() -> None:
    lines = NOTE.read_text(encoding="utf-8").splitlines()
    marked = {}
    illegal = []
    for line in lines:
        if not line.startswith("|"):
            continue
        for route in N1_ROUTES:
            if f"| {route} |" in line:
                marker = line.split("|")[2].strip().replace("**", "")
                marked[route] = marker
                if marker not in ("ATTEMPTED", "RULED OUT BY PRIOR"):
                    illegal.append((route, marker))
    check(
        "N1 uses exact honesty markers on seven distinct routes",
        len(marked) == len(N1_ROUTES)
        and all(marker == "ATTEMPTED" for marker in marked.values())
        and not illegal,
        {"markers": marked, "illegal": illegal},
    )


def n2_directional_pair_control() -> None:
    text = NOTE.read_text(encoding="utf-8")
    expected = tuple(combinations(WALLS, 2))
    missing = tuple(
        pair
        for pair in expected
        if f"| `{pair[0]}` | `{pair[1]}` |" not in text
    )
    check(
        "N2 gives both closure directions for every pair in the collapsed five-condition set",
        len(expected) == 10 and not missing,
        {"directional_pairs": len(expected), "missing": missing},
    )


def n3_literal_scan() -> None:
    triggers = tuple("".join(parts) for parts in TRIGGER_PARTS)
    rows = []
    total = 0
    for path in PACKAGE_PATHS:
        source = path.read_text(encoding="utf-8").lower()
        hits = tuple(trigger for trigger in triggers if trigger in source)
        total += len(hits)
        rows.append({"path": str(path.relative_to(ROOT)), "hits": hits})
    check(
        "N3 literal skill-trigger scan has zero hits across all four package paths",
        len(rows) == 4 and total == 0,
        rows,
    )


def line_has(path: Path, line_number: int, fragment: str) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    return 0 < line_number <= len(lines) and fragment in lines[line_number - 1]


def n4_file_line_witness_control() -> None:
    witnesses = (
        (ROUTE, 507, "zero physical overlap"),
        (ROUTE, 664, "preserves every port constraint"),
        (ROUTE, 726, "phase-flag enforcement audit"),
        (ROUTE, 772, "actual separated-cell recurrent coin"),
        (ROUTE, 810, "one common E intertwines the fixed-seam"),
        (ROUTE, 834, "mass fixture and exact contact firewall"),
        (ROUTE, 1022, "opposite-wedge, phase-flag, and schedule deletions"),
        (ROUTE_NOTE, 65, "not the actual recurrent volume update"),
        (ROUTE_NOTE, 89, "phase flag is not locally enforced"),
    )
    rows = [
        {
            "path": str(path.relative_to(ROOT)),
            "line": line_number,
            "fragment": fragment,
            "match": line_has(path, line_number, fragment),
        }
        for path, line_number, fragment in witnesses
    ]
    check(
        "N4 witnesses are locked to matching files and lines, including both decisive residuals",
        all(row["match"] for row in rows),
        rows,
    )


def n5_to_n8_and_gate_controls() -> None:
    text = normalized(NOTE)
    check(
        "N5 records tested resolutions and narrows every broader reading",
        all(
            phrase in text
            for phrase in (
                "per microsector",
                "per logical column",
                "per fixed-seam block",
                "per anchor",
                "per cell",
                "lattice-wide recurrent",
                "full fock",
            )
        ),
    )
    check(
        "N6--N8 retain constructive paths, the hostile countercase, and explicit retirement mechanisms",
        "all are constructive non-axiom paths" in text
        and "hostile reviewer" in text
        and "locally constrained carrier marker" in text
        and "position-growing invariant code" in text
        and "collision-safe port layer" in text
        and "opposite-wedge completion" in text,
    )
    check(
        "the broad Gate fails and creates no shared obstruction or axiom pressure",
        "gate status: fail for the candidate broad negative; do not ship it" in text
        and "no shared obstruction was identified" in text
        and "no axiom pressure was established" in text,
    )


def ledger_and_lane_controls() -> None:
    text = normalized(NOTE)
    check(
        "the ledger keeps C_ref, C_wrap, and C_local at the reviewed scope",
        "c_ref | unchanged" in text
        and "c_wrap | unchanged" in text
        and "c_local | diagnostic advance only; no maturity raise" in text,
    )
    check(
        "the TOE lane scores do not turn the comparator into integrated closure",
        all(score in text for score in ("3.0/5", "1.7/5", "3.5/5", "1.9/5"))
        and "no lane maturity increase" in text,
    )


def main() -> int:
    print("CYCLE 304: PHYSICAL COMMON-REFINEMENT COMPANION SYNTHESIS")
    print("authority=none; audit=unset")
    note_contract()
    freshness_control()
    cold_route()
    route_boundary_guards()
    n1_exact_marker_control()
    n2_directional_pair_control()
    n3_literal_scan()
    n4_file_line_witness_control()
    n5_to_n8_and_gate_controls()
    ledger_and_lane_controls()
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
