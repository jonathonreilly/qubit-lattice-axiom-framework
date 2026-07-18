#!/usr/bin/env python3
"""Cycle-308 strict synthesis and bounded-negative release gate."""

from __future__ import annotations

from itertools import combinations
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
ROUTE = ROOT / (
    "scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py"
)
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_HIGHER_NUMBER_FIXED_SEAM_CYCLE308_NOTE_2026-07-17.md"
)
PACKAGE_PATHS = (ROUTE, NOTE, Path(__file__).resolve())
N1_ROUTES = (
    "bare three-occupation face syndrome",
    "one selected complement-port carrier",
    "equal positive complement sum",
    "oriented coherent complement carrier",
    "arbitrary quadruple matching paths",
    "oriented Hodge quadruple basis",
    "one proper-cubic occupation orbit",
    "ambient branch matrix units",
)
WALLS = (
    "W_bare",
    "W_prepare",
    "W_recurrent",
    "W_overlap",
    "W_common",
)

# Split fragments keep the scan vocabulary out of the package paths.
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
    observed = tuple(int(value) for value in match.groups()) if match else None
    check(
        "the Cycle-308 physical route cold-passes",
        completed.returncode == 0 and observed == (11, 0),
        {"returncode": completed.returncode, "observed": observed},
    )


def construction_contract() -> None:
    note = normalized(NOTE)
    route = normalized(ROUTE)
    required_note = (
        "40 logical columns",
        "120 literal microstates",
        "thirty logical columns",
        "exp(i 3g)",
        "exp(i 6g)",
        "k_physical,n = e_n k_n e_n^dagger + i - p_n",
        "target branch a",
        "conjugate(alpha_(j,b))",
        "coin, then stream/catch-up, then contact",
        "reverse branch is tested only as a comparator completion",
        "one-particle mass fixture unchanged",
        "held l=6",
    )
    missing_note = tuple(phrase for phrase in required_note if phrase not in note)
    check(
        "the note pins dimensions, carrier weights, actual contact, order, mass firewall, and held size",
        not missing_note,
        missing_note,
    )
    required_route = (
        "def ambient_coin_matrix",
        "encoding @ logical_comparator @ encoding.conj().t",
        "physical_coin = ambient_coin_matrix",
        "coin_image = physical_coin @ encoding",
        "anchor_physical_contact @ anchor_physical_stream @ anchor_physical_coin",
        "target_amplitude np.conjugate(source_amplitude)",
        "(-0.35, true)",
        "number (number - 1) // 2",
    )
    missing_route = tuple(phrase for phrase in required_route if phrase not in route)
    check(
        "the executable constructs the ambient physical coin and uses it in DSK for trained and held beta",
        not missing_route,
        missing_route,
    )


def n1_exact_markers() -> None:
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
        "N1 uses exact honesty markers on eight distinct executed routes",
        len(marked) == len(N1_ROUTES)
        and all(marker == "ATTEMPTED" for marker in marked.values())
        and not illegal,
        {"markers": marked, "illegal": illegal},
    )


def n2_directed_pairs() -> None:
    text = NOTE.read_text(encoding="utf-8")
    expected = tuple(combinations(WALLS, 2))
    missing = tuple(
        pair
        for pair in expected
        if f"| `{pair[0]}` | `{pair[1]}` | no | no | yes |" not in text
    )
    check(
        "N2 answers both closure directions for every pair in the collapsed five-condition set",
        len(expected) == 10 and not missing,
        {"directed_answers": 2 * len(expected), "missing": missing},
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
        "N3 literal hidden-condition scan has zero hits across all Cycle-308 package paths",
        len(rows) == 3 and total == 0,
        rows,
    )


def line_has(path: Path, line_number: int, fragment: str) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    return 0 < line_number <= len(lines) and fragment in lines[line_number - 1]


def n4_exact_witnesses() -> None:
    cycle269 = ROOT / (
        "docs/work_history/repo/review_feedback/"
        "WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md"
    )
    cycle245 = ROOT / (
        "docs/work_history/repo/review_feedback/"
        "HAEGEMAN_PARITY_SECTOR_GAUGING_CYCLE245_NOTE_2026-07-17.md"
    )
    cycle305 = ROOT / (
        "docs/work_history/repo/review_feedback/"
        "PHYSICAL_CYCLE269_FULL_TWO_PARTICLE_SECTOR_INTERFACE_CYCLE305_NOTE_2026-07-17.md"
    )
    cycle306 = ROOT / (
        "docs/work_history/repo/review_feedback/"
        "PHYSICAL_CYCLE269_RELATIONAL_ROLE_MARKER_GAUGE_CYCLE306_NOTE_2026-07-17.md"
    )
    witnesses = (
        (ROUTE, 566, "product_B ="),
        (ROUTE, 611, "all n=4 pairing/path words"),
        (ROUTE, 1019, "both physical seams exactly intertwine"),
        (ROUTE, 1249, "the complete occupation bases and literal carrier branches"),
        (cycle269, 43, "total-even matter"),
        (cycle245, 55, "lawful odd state image"),
        (cycle305, 221, "deleting all three antipodal columns"),
        (cycle306, 39, "one additional ordinary M2"),
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
        "N4 locks every matched and deliberately dropped residual to an exact file and line",
        all(row["match"] for row in rows),
        rows,
    )


def n5_to_n8_and_gate() -> None:
    text = normalized(NOTE)
    check(
        "N5 narrows the negative at every tested and untested resolution",
        all(
            phrase in text
            for phrase in (
                "per face generator",
                "per bare triple",
                "per carrier branch",
                "per encoded column",
                "per local block",
                "per anchor/size",
                "lattice-wide recurrent volume",
                "overlapping/full fock",
                "restricted to a bare three-occupation syndrome",
            )
        ),
    )
    check(
        "N6 gives constructive non-axiom closure paths",
        "coherent complement-port carrier" in text
        and "prepare the carrier with a bounded local gauge/resource circuit" in text
        and "close measured separated-cell coin images" in text
        and "add simultaneous shells" in text
        and "enlarge the bosonization graph" in text
        and "no new primitive or axiom is requested" in text,
    )
    check(
        "N7 supplies a hostile concrete counterexample to the broad negative",
        "hostile reviewer" in text
        and "ordinary physical carrier" in text
        and "40-column code" in text
        and "route-independent obstruction does not" in text,
    )
    check(
        "N8 records the required search and actual constructive cross-cycle echoes",
        "required repository negative-phrase search" in text
        and "no_go_ledger.md" in text
        and "cycle 245 parity-sector gauging" in text
        and "cycle 305 complete two-particle seam" in text
        and "cycle 306 relational role-marker gauge" in text
        and "cycle 308 complement-port carrier" in text,
    )
    check(
        "the candidate broad negative has Gate FAIL / DO NOT SHIP with no shared obstruction or axiom pressure",
        "gate status: fail for the candidate broad negative; do not ship it" in text
        and "no shared obstruction" in text
        and "no axiom pressure" in text,
    )


def main() -> int:
    print("CYCLE 308: HIGHER-NUMBER FIXED-SEAM STRICT SYNTHESIS")
    print("authority=none; audit=unset")
    construction_contract()
    cold_route()
    n1_exact_markers()
    n2_directed_pairs()
    n3_literal_scan()
    n4_exact_witnesses()
    n5_to_n8_and_gate()
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
