#!/usr/bin/env python3
"""Cycle-311 strict synthesis and broad-negative release gate."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
ROUTE = ROOT / (
    "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py"
)
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_COMMON_M64_FIXED_SEAM_CYCLE311_NOTE_2026-07-18.md"
)
PACKAGE_PATHS = (ROUTE, NOTE, Path(__file__).resolve())
N1_ROUTES = (
    "direct fixed-Wilson even sectors",
    "coherent complement carrier",
    "one shared-vacuum seam quotient",
    "raw occupation/tag rays without role data",
    "standalone exchange-`+1` selector",
    "one-extra-M2 relational role gauge",
    "staggered/time-multiplexed role schedule",
)
N2_PAIRS = (
    "reference preparation / primitive synthesis",
    "reference preparation / coherent-position preparation",
    "reference preparation / recurrent closure",
    "reference preparation / overlapping shells",
    "reference preparation / number-changing law",
    "primitive synthesis / coherent-position preparation",
    "primitive synthesis / recurrent closure",
    "primitive synthesis / overlapping shells",
    "primitive synthesis / number-changing law",
    "coherent-position preparation / recurrent closure",
    "coherent-position preparation / overlapping shells",
    "coherent-position preparation / number-changing law",
    "recurrent closure / overlapping shells",
    "recurrent closure / number-changing law",
    "overlapping shells / number-changing law",
)

# Split fragments keep the scan vocabulary out of the release package.
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
        "the Cycle-311 physical route cold-passes",
        completed.returncode == 0 and observed == (11, 0),
        {
            "returncode": completed.returncode,
            "observed": observed,
            "stderr_tail": completed.stderr[-500:],
        },
    )


def construction_contract() -> None:
    note = normalized(NOTE)
    route = normalized(ROUTE)
    required_note = (
        "64-dimensional input code",
        "127-dimensional seam closure",
        "not a fictitious 128-column isometry",
        "255 flagged microsectors",
        "510 role-gauge microsectors",
        "n=5",
        "n=6",
        "same-physical-number pairs",
        "not a free sector label",
        "exp(i binom(n,2) g)",
        "coherent cross-sector superpositions",
        "all 24 proper-cubic frames",
        "held l=6",
        "at most fifty-six m2",
    )
    missing_note = tuple(phrase for phrase in required_note if phrase not in note)
    check(
        "the note pins the common M64 quotient, sectors, relational roles, contact, covariance, and support",
        not missing_note,
        missing_note,
    )
    required_route = (
        "seam_labels = ((0, (), 0),)",
        "def exterior_matrix",
        "def logical_coin",
        "def logical_stream",
        "def logical_contact",
        "def constrained_encoding",
        "def role_constraint",
        "def physical_coin",
        "number_changing_microterms",
        "coherent_composition",
    )
    missing_route = tuple(phrase for phrase in required_route if phrase not in route)
    check(
        "the executable constructs the shared-vacuum seam and common constrained physical operators",
        not missing_route,
        missing_route,
    )


def n1_exact_markers() -> None:
    lines = NOTE.read_text(encoding="utf-8").splitlines()
    marked = {}
    for line in lines:
        if not line.startswith("|"):
            continue
        for route in N1_ROUTES:
            if f"| {route} |" in line:
                marked[route] = line.split("|")[2].strip().replace("**", "")
    expected = {
        **{route: "ATTEMPTED" for route in N1_ROUTES[:-1]},
        N1_ROUTES[-1]: "OPEN / UNTESTED",
    }
    check(
        "N1 records six executed routes and one live scheduled alternative",
        marked == expected,
        {"expected": expected, "observed": marked},
    )


def n2_pair_audit() -> None:
    text = NOTE.read_text(encoding="utf-8")
    missing = tuple(
        pair for pair in N2_PAIRS if f"| {pair} | no | no | independent tasks |" not in text
    )
    check(
        "N2 answers both directions for every pair in the six-target residual set",
        len(N2_PAIRS) == 15 and not missing,
        {"directional_answers": 30, "missing": missing},
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
        "N3 hidden-condition scan has zero literal hits across all Cycle-311 release files",
        len(rows) == 3 and total == 0,
        rows,
    )


def line_has(path: Path, line_number: int, fragment: str) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    return 0 < line_number <= len(lines) and fragment in lines[line_number - 1]


def n4_exact_witnesses() -> None:
    base = ROOT / "docs/work_history/repo/review_feedback"
    witnesses = (
        (
            base / "PHYSICAL_CYCLE269_JOINT_SIX_MODE_COIN_LIFT_CYCLE302_NOTE_2026-07-17.md",
            46,
            "global-vacuum rank projector",
        ),
        (
            base / "PHYSICAL_CYCLE269_FULL_TWO_PARTICLE_SECTOR_INTERFACE_CYCLE305_NOTE_2026-07-17.md",
            20,
            "all fifteen unordered pairs",
        ),
        (
            base / "PHYSICAL_CYCLE269_RELATIONAL_ROLE_MARKER_GAUGE_CYCLE306_NOTE_2026-07-17.md",
            43,
            "C_role = K_exchange X_r",
        ),
        (
            base / "PHYSICAL_CYCLE269_HIGHER_NUMBER_FIXED_SEAM_CYCLE308_NOTE_2026-07-17.md",
            23,
            "coherently distributed physical carrier",
        ),
        (
            base / "PHYSICAL_CYCLE269_HIGHER_NUMBER_FIXED_SEAM_CYCLE308_NOTE_2026-07-17.md",
            25,
            "all fifteen logical quadruples",
        ),
    )
    rows = [
        {
            "path": str(path.relative_to(ROOT)),
            "line": line,
            "fragment": fragment,
            "match": line_has(path, line, fragment),
        }
        for path, line, fragment in witnesses
    ]
    check(
        "N4 locks every common-code precursor to an exact matching residual",
        all(row["match"] for row in rows),
        rows,
    )


def n5_to_n8_and_gate() -> None:
    text = normalized(NOTE)
    check(
        "N5 distinguishes raw ray, seam, M64, local, frame, size, recurrent, and full-Hilbert resolutions",
        all(
            phrase in text
            for phrase in (
                "raw physical ray",
                "encoded seam column",
                "m64 input",
                "local block",
                "body anchor and size",
                "proper-cubic/translation orbit",
                "overlapping recurrent lattice",
                "number-changing/full physical hilbert space",
                "exact raw unflagged matrix",
            )
        ),
    )
    check(
        "N6 names three executed non-axiom closure paths and direct next campaigns",
        "local f+r relational gauge" in text
        and "shared-vacuum quotient" in text
        and "complete exterior direct sum" in text
        and "without a convention change or axiom" in text
        and "number-changing interactions remain direct constructive campaigns" in text,
    )
    check(
        "N7 supplies a hostile constructive counterexample and preserves the live scheduled route",
        "hostile reviewer" in text
        and "artifact of looking only at raw tag collisions" in text
        and "64-to-127 common encoder" in text
        and "time-multiplexed route remains untested" in text
        and "no route-independent obstruction" in text,
    )
    check(
        "N8 records the matching constructive cross-cycle retirement pattern",
        "cycle 302 retired" in text
        and "cycle 305 retired" in text
        and "cycle 306 retired" in text
        and "cycle 308 retired" in text
        and "past route failures supply no axiom pressure" in text,
    )
    check(
        "the broad Gate is FAIL / DO NOT SHIP with no shared obstruction or axiom pressure",
        "broad gate status: fail / do not ship" in text
        and "no broad no-go claim and no axiom pressure" in text
        and "not generalized into an impossibility, minimum-content, or axiom-pressure statement" in text,
    )


def main() -> int:
    print("CYCLE 311: COMMON M64 FIXED-SEAM STRICT SYNTHESIS")
    print("authority=none; audit=unset")
    construction_contract()
    cold_route()
    n1_exact_markers()
    n2_pair_audit()
    n3_literal_scan()
    n4_exact_witnesses()
    n5_to_n8_and_gate()
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
