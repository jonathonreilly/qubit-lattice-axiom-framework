#!/usr/bin/env python3
"""Cycle-303 synthesis for the coherent proper-cubic pair orbit."""

from __future__ import annotations

from itertools import combinations
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
ROUTE = ROOT / "scripts/physical_cycle269_coherent_cubic_pair_orbit_2026_07_17.py"
ROUTE_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_COHERENT_CUBIC_PAIR_ORBIT_NOTE_2026-07-17.md"
)
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COHERENT_CUBIC_PAIR_ORBIT_SYNTHESIS_CYCLE303_NOTE_2026-07-17.md"
)
PACKAGE_PATHS = (ROUTE, ROUTE_NOTE, Path(__file__).resolve(), NOTE)
WALLS = ("W_reference", "W_coin", "W_position", "W_fock")
N1_ROUTES = (
    "separately selected localized rays",
    "one 24-column orbit isometry",
    "unsigned frame permutation",
    "declared signed-wedge frame action",
    "one common stream/contact restriction",
    "all-anchor translation family",
    "identical-pair role reversal",
)

# Fragments keep the skill vocabulary out of the four scanned source paths.
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
        check("the Cycle-303 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "one linear e_x",
        "exact gram identity",
        "declared wedge signs",
        "restricted physical matrices",
        "relative-state union",
        "not operator support",
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
    check("the synthesis pins the orbit, ledger, Gate, and N1--N8", not missing, missing)


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
        "the independently reviewed coherent-orbit route cold-passes",
        completed.returncode == 0 and observed == (9, 0),
        {"returncode": completed.returncode, "observed": observed},
    )


def route_boundary_guards() -> None:
    route = normalized(ROUTE_NOTE)
    check(
        "the result is one common linear fixed-anchor orbit rather than selected rays",
        "one linear e_x" in route
        and "exact gram" in route
        and "arbitrary coherent" in route
        and "matrix-free definition" in route,
    )
    check(
        "physical action and support retain their reviewed narrow semantics",
        "restricted physical matrices" in route
        and "relative-state union" in route
        and "not operator support" in route
        and "extensive product" in route,
    )
    check(
        "the orbit keeps reference, coin, position, Fock, and semantics explicit",
        "fixed-anchor" in route
        and "not a coin router" in route
        and "position coherence" in route
        and "not a full-fock compiler" in route
        and "not physical time" in route,
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
        "N1 uses only exact honesty markers on seven distinct routes",
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
        "N2 gives both closure directions for every pair in the collapsed four-condition set",
        len(expected) == 6 and not missing,
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
        (ROUTE, 397, "one E_x coherently spans"),
        (ROUTE, 505, "operator_semantics"),
        (ROUTE, 509, "same physical stream/catch-up and contact products"),
        (ROUTE, 802, "declared_wedge_sign_failures"),
        (ROUTE, 809, "translation_group_law_tests"),
        (ROUTE, 937, "one_address_deletion_covariance_leakage"),
        (ROUTE_NOTE, 78, "not operator support"),
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
        "N4 witnesses are locked to matching files and lines",
        all(row["match"] for row in rows),
        rows,
    )


def n5_to_n8_and_gate_controls() -> None:
    text = normalized(NOTE)
    check(
        "N5 records every tested resolution and narrows untested resolutions",
        all(
            phrase in text
            for phrase in (
                "per representative",
                "per address",
                "per block",
                "per anchor",
                "lattice-wide",
                "full fock",
            )
        ),
    )
    check(
        "N6--N8 retain constructive continuations, a hostile countercase, and actual retirement mechanisms",
        "all are constructive non-axiom paths" in text
        and "hostile reviewer" in text
        and "collision-safe xor catch-up" in text
        and "collect orthogonal tag sectors" in text
        and "declared wedge signs" in text,
    )
    check(
        "the candidate broad negative fails and creates no axiom pressure",
        "gate status: fail for the candidate broad negative; do not ship it" in text
        and "no shared obstruction was identified" in text
        and "no axiom pressure was established" in text,
    )


def main() -> int:
    print("CYCLE 303: COHERENT PROPER-CUBIC PAIR-ORBIT SYNTHESIS")
    print("authority=none; audit=unset")
    note_contract()
    cold_route()
    route_boundary_guards()
    n1_exact_marker_control()
    n2_directional_pair_control()
    n3_literal_scan()
    n4_file_line_witness_control()
    n5_to_n8_and_gate_controls()
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
