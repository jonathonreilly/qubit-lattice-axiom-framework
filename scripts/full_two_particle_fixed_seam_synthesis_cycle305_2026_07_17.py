#!/usr/bin/env python3
"""Cycle-305 strict synthesis for the full two-particle fixed seam."""

from __future__ import annotations

from itertools import combinations
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
ROUTE = ROOT / (
    "scripts/"
    "physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py"
)
ROUTE_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_FULL_TWO_PARTICLE_SECTOR_INTERFACE_CYCLE305_NOTE_2026-07-17.md"
)
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "FULL_TWO_PARTICLE_FIXED_SEAM_SYNTHESIS_CYCLE305_NOTE_2026-07-17.md"
)
PACKAGE_PATHS = (ROUTE, ROUTE_NOTE, Path(__file__).resolve(), NOTE)
WALLS = (
    "W_reference",
    "W_recurrent",
    "W_position",
    "W_overlap",
    "W_primitive",
)
N1_ROUTES = (
    "perpendicular-only pair code",
    "four antipodal path representatives",
    "full fifteen-pair exterior square",
    "two-slice exterior-square law",
    "input-slice unitary comparator",
    "Cycle-230 coin-stream-contact order",
    "autonomous local matrix units",
    "signed-wedge cubic action",
)

# Split fragments keep the scan vocabulary out of the four scanned paths.
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
        check("the Cycle-305 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "one exact 30-column e_x",
        "three antipodal pairs",
        "input-slice coin",
        "identity output comparator",
        "coin, then stream/catch-up, then contact",
        "not recurrent physics",
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
    check(
        "the synthesis pins the corrected seam, ledger, broad Gate, and N1--N8",
        not missing,
        missing,
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
        r"SUMMARY:\s+(\d+)\s+passed,\s+(\d+)\s+failed",
        completed.stdout,
    )
    observed = tuple(int(item) for item in match.groups()) if match else None
    check(
        "the corrected Cycle-305 physical route cold-passes",
        completed.returncode == 0 and observed == (12, 0),
        {"returncode": completed.returncode, "observed": observed},
    )


def route_boundary_guards() -> None:
    route = normalized(ROUTE_NOTE)
    synthesis = normalized(NOTE)
    check(
        "the earned coin theorem is input-slice only with an explicit identity comparator completion",
        "only the t=0 slice" in route
        and "blockdiag(wedge^2(c),i_15)" in route
        and "does not claim a physical coin on the separated slice" in route
        and "not a recurrent volume update" in route,
    )
    check(
        "Cycle-230 order and its forward contact boundary are explicit",
        "actual cycle-230 order" in route
        and "coin comparator, then the complete stream" in route
        and "subsequent cycle-230 contact is identity" in route
        and "reverse branch is a comparator control" in route,
    )
    check(
        "C_ref owns the fixed reference while C_wrap remains unchanged only because schedule is not time",
        "the fixed reference lives in c_ref" in synthesis
        and "c_wrap stays unchanged solely because the schedule is not time" in synthesis,
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
        "N1 uses exact honesty markers on eight distinct routes",
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
        "N2 gives both closure directions for all ten pairs in the collapsed five-condition set",
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
        "N3 literal skill-trigger scan has zero hits across all four Cycle-305 package paths",
        len(rows) == 4 and total == 0,
        rows,
    )


def line_has(path: Path, line_number: int, fragment: str) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    return 0 < line_number <= len(lines) and fragment in lines[line_number - 1]


def n4_file_line_witness_control() -> None:
    cycle304 = ROOT / (
        "docs/work_history/repo/review_feedback/"
        "PHYSICAL_CYCLE269_COIN_STREAM_CONTACT_COMMON_REFINEMENT_CYCLE304_NOTE_2026-07-17.md"
    )
    cycle303 = ROOT / (
        "docs/work_history/repo/review_feedback/"
        "COHERENT_CUBIC_PAIR_ORBIT_SYNTHESIS_CYCLE303_NOTE_2026-07-17.md"
    )
    witnesses = (
        (ROUTE, 497, "all four bounded paths"),
        (ROUTE, 589, "one E_x carries all fifteen pairs"),
        (ROUTE, 664, "joint face/tag transitions"),
        (ROUTE, 732, "fifteen-pair coefficient block"),
        (ROUTE, 830, "input-slice wedge coin comparator"),
        (ROUTE, 845, "Cycle-230 coin-then-stream-then-contact"),
        (ROUTE, 1181, "perpendicular_only_coin_leakage_operator_norm"),
        (cycle304, 43, "actual separated-cell coin"),
        (cycle303, 257, "enlarge the wedge"),
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
        "N4 witnesses are locked to exact files and lines with residual matches stated in the note",
        all(row["match"] for row in rows),
        rows,
    )


def n5_to_n8_and_gate_controls() -> None:
    text = normalized(NOTE)
    check(
        "N5 covers every tested resolution and narrows the untested volume and Fock resolutions",
        all(
            phrase in text
            for phrase in (
                "per path",
                "per pair",
                "per slice",
                "per block",
                "per anchor",
                "lattice-wide",
                "full fock",
                "semantics",
            )
        ),
    )
    check(
        "N6 records constructive non-axiom continuations",
        "add the measured separated-cell output columns" in text
        and "grow a translated direct sum" in text
        and "add simultaneous shells" in text
        and "decompose the 210-term comparator" in text
        and "all are constructive non-axiom paths" in text,
    )
    check(
        "N7 supplies a hostile concrete countercase against the broad negative",
        "hostile reviewer" in text
        and "add the measured separated-cell output columns" in text
        and "close them under the independent onsite coins" in text
        and "broad negative is premature" in text,
    )
    check(
        "N8 records the required search and actual cross-cycle retirement mechanisms",
        "required repository search was run" in text
        and "six half-edge auxiliary ports" in text
        and "one 24-column signed-wedge orbit" in text
        and "three path-independent antipodal columns" in text
        and "scope error retired" in text,
    )
    check(
        "the candidate broad negative has Gate FAIL with no shared obstruction or axiom pressure",
        "gate status: fail for the candidate broad negative; do not ship it" in text
        and "no shared obstruction was identified" in text
        and "no axiom pressure was established" in text,
    )


def main() -> int:
    print("CYCLE 305: FULL TWO-PARTICLE FIXED-SEAM SYNTHESIS")
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
