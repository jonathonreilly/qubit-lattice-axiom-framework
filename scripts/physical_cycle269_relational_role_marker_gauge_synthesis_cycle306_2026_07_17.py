#!/usr/bin/env python3
"""Cycle 306 release synthesis for the relational role-marker gauge."""

from __future__ import annotations

import ast
from itertools import permutations
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
PHYSICAL_RUNNER = ROOT / (
    "scripts/physical_cycle269_relational_role_marker_gauge_cycle306_2026_07_17.py"
)
PHYSICAL_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_RELATIONAL_ROLE_MARKER_GAUGE_CYCLE306_NOTE_2026-07-17.md"
)
SYNTHESIS_RUNNER = Path(__file__).resolve()
SYNTHESIS_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_RELATIONAL_ROLE_MARKER_GAUGE_SYNTHESIS_CYCLE306_NOTE_2026-07-17.md"
)
PATHS = (PHYSICAL_RUNNER, PHYSICAL_NOTE, SYNTHESIS_RUNNER, SYNTHESIS_NOTE)

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


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def note_contract() -> None:
    if not SYNTHESIS_NOTE.exists():
        check("the Cycle-306 synthesis note exists", False, SYNTHESIS_NOTE)
        return
    body = text(SYNTHESIS_NOTE).lower()
    required = (
        "authority: none",
        "audit: unset",
        "four-path release package",
        "physical 17/0",
        "broad negative: fail / do not ship",
        "no shared obstruction",
        "no axiom pressure",
        "c_ref",
        "c_wrap",
        "c_local",
        "59%",
        "67%",
        "3.1/5",
        "3.6/5",
        "common-shell projector",
        "dense ninety-term constraint",
        "initial code state",
    )
    missing = tuple(item for item in required if item not in body)
    check("the synthesis note pins the release corrections", not missing, missing)


def cold_run_physical() -> None:
    completed = subprocess.run(
        (sys.executable, str(PHYSICAL_RUNNER)),
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=120,
    )
    summaries = re.findall(r"^SUMMARY (\{.*\})$", completed.stdout, flags=re.MULTILINE)
    summary = ast.literal_eval(summaries[-1]) if summaries else {}
    expected_lines = (
        "standalone X_flag R selector",
        "exactly the intended forty-two columns",
        "flips the gauge-invariant role marker autonomously",
        "all 24 proper-cubic frames",
        "all 27 L=3 translations",
        "held L=6",
    )
    missing = tuple(item for item in expected_lines if item not in completed.stdout)
    check(
        "the physical certificate cold-runs at 17/0 with every release-critical control",
        completed.returncode == 0
        and summary == {"pass": 17, "fail": 0}
        and not missing,
        {
            "returncode": completed.returncode,
            "summary": summary,
            "missing_output_contract": missing,
            "stderr": completed.stderr[-500:],
        },
    )


def hidden_premise_zero_scan() -> None:
    phrases = (
        " ".join(("we", "assume")),
        " ".join(("by", "construction")),
        " ".join(("as", "is", "standard")),
        " ".join(("the", "framework", "provides")),
        " ".join(("bridge", "context")),
        "".join(("back", "ground")),
        "".join(("natural", "ly")),
        "".join(("obvious", "ly")),
        " ".join(("standard", "qft")),
        "".join(("register", "ed")),
        "".join(("canoni", "cal")),
    )
    hits = []
    for path in PATHS:
        body = text(path).lower()
        for phrase in phrases:
            if phrase in body:
                hits.append((path.name, phrase))
    check(
        "the literal hidden-premise scan has zero hits across exactly four release paths",
        len(PATHS) == 4 and not hits,
        {"paths": tuple(path.name for path in PATHS), "hits": hits},
    )


def strict_no_go_surface() -> None:
    body = text(PHYSICAL_NOTE)
    n1 = body.split("### N1", 1)[1].split("### N2", 1)[0]
    statuses = re.findall(r"\|\s*\*\*([^*]+)\*\*\s*\|", n1)
    allowed = {
        "ATTEMPTED",
        "RULED OUT BY PRIOR RESULT",
        "OPEN / UNTESTED",
    }
    check(
        "N1 uses only the three exact bold status markers and keeps open alternatives visible",
        len(statuses) == 7
        and set(statuses) == allowed
        and "LIVE / UNTESTED" not in n1,
        statuses,
    )

    n2 = body.split("### N2", 1)[1].split("### N3", 1)[0]
    wall_rows = re.findall(r"^\| `(W_[^`]+)` \| `(W_[^`]+)` \| no \|", n2, re.MULTILINE)
    walls = ("W_prim", "W_rec", "W_prep", "W_Fock")
    expected = set(permutations(walls, 2))
    check(
        "N2 contains the complete twelve-row directional implication table",
        len(wall_rows) == 12 and set(wall_rows) == expected,
        {"rows": len(wall_rows), "missing": sorted(expected - set(wall_rows))},
    )

    n3 = body.split("### N3", 1)[1].split("### N4", 1)[0]
    n4 = body.split("### N4", 1)[1].split("### N5", 1)[0]
    n5 = body.split("### N5", 1)[1].split("### N6", 1)[0]
    check(
        "N3-N5 expose a zero-hit scan, exact file-line witnesses, and a multi-resolution table",
        "literal hit count is zero" in n3
        and len(re.findall(r"\.md:\d+`", n4)) == 6
        and "| claim surface | microsector | 42-column shell | bounded patch | lattice-wide | outside tested resolution |" in n5,
    )

    n6_n8 = body.split("### N6", 1)[1].split("## Six-wall ledger", 1)[0]
    check(
        "N6-N8 retain the constructive closure, hostile counterargument, and actual cross-cycle echo",
        "one-extra-M2 relational gauge is the partial-closure path" in n6_n8
        and "Reject the broad negative." in n6_n8
        and "Cycle 248" in n6_n8
        and "Cycle 273" in n6_n8
        and "FAIL / DO NOT SHIP" in n6_n8
        and "no axiom pressure" in n6_n8,
    )


def witness_line_controls() -> None:
    body = text(PHYSICAL_NOTE)
    citations = re.findall(r"`([A-Z0-9_\-]+\.md):(\d+)`", body)
    failures = []
    for filename, line_text in citations:
        path = ROOT / "docs/work_history/repo/review_feedback" / filename
        line = int(line_text)
        if not path.exists():
            failures.append((filename, line, "missing file"))
            continue
        lines = text(path).splitlines()
        if line < 1 or line > len(lines) or not lines[line - 1].strip():
            failures.append((filename, line, "missing line"))
    check(
        "all six N4 witness locations resolve to nonempty source lines",
        len(citations) == 6 and not failures,
        {"citations": citations, "failures": failures},
    )


def ledger_score_and_inventory_controls() -> None:
    body = text(PHYSICAL_NOTE)
    ledger = body.split("## Six-wall ledger", 1)[1].split("## TOE lane update", 1)[0]
    scores = body.split("## TOE lane update", 1)[1].split("## Optimal next probe", 1)[0]
    check(
        "the ledger assigns role enforcement to C_local while C_ref and C_wrap remain unchanged",
        "| `C_ref` | unchanged; every column remains relative" in ledger
        and "| `C_wrap` | unchanged; the role marker and compiler schedule are not time" in ledger
        and "| `C_local` | the free role-flag clause is retired" in ledger
        and "physical event equivalence, clock selection, recurrence, interval, and rate calibration" in ledger,
    )
    required_scores = (
        "| operational quantum / Records | 59% | 26% | 82% | 3.1/5 |",
        "| causal time / clock | 33% | 17% | 60% | 1.7/5 |",
        "| inertia / matter | 67% | 30% | 87% | 3.6/5 |",
        "| gravity / source / resource | 38% | 15% | 63% | 1.9/5 |",
        "| Born / probability / realized history | 33% | 14% | 79% | 1.7/5 |",
    )
    check(
        "the planning scores rise only in operational and matter lanes",
        all(row in scores for row in required_scores),
        tuple(row for row in required_scores if row not in scores),
    )
    required_inventory = (
        "common-shell projector",
        "dense ninety-term constraint",
        "initial code state",
        "fixed `+++` Wilson reference ray",
        "one additional homogeneous ordinary `r` M2",
    )
    check(
        "the supplied-structure inventory names every release-critical imported object",
        all(item in body for item in required_inventory),
        tuple(item for item in required_inventory if item not in body),
    )


def main() -> int:
    print("CYCLE 306 SYNTHESIS: RELATIONAL ROLE-MARKER RELEASE")
    print("authority=none; audit=unset")
    note_contract()
    cold_run_physical()
    hidden_premise_zero_scan()
    strict_no_go_surface()
    witness_line_controls()
    ledger_score_and_inventory_controls()
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
