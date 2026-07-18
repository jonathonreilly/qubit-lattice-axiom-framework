#!/usr/bin/env python3
"""Cycle 317 strict release certificate for N1-N8 and baseline discipline."""

from __future__ import annotations

from itertools import combinations
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md"
)
SCIENCE = ROOT / (
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py"
)
FRESH_MAIN = "17cb0c5c32e753ef1297b185fbd1e8c6d41920c2"
PASS = 0
FAIL = 0

N1_ROUTES = (
    "fixed actual-contact trine",
    "apparatus-only quarter coin",
    "bounded mixed-projective compiler",
    "literal arbitrary-finite X1 in one fixed pointer",
    "sequential/time-multiplexed arbitrary X1",
    "autonomous programmable apparatus",
    "occurrence-first numerical law",
    "process-functional/global-history route",
)
WALLS = ("W_prog", "W_grade", "W_occ", "W_record", "W_global")
TRIGGER_PARTS = (
    ("we", " assume"),
    ("by", " construction"),
    ("as is", " standard"),
    ("the framework", " provides"),
    ("bridge", " context"),
    ("back", "ground"),
    ("natur", "ally"),
    ("obvious", "ly"),
    ("standard", " qft"),
    ("regis", "tered"),
    ("canon", "ical"),
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("STRICT PASS", label, "::", detail)
    else:
        FAIL += 1
        print("STRICT FAIL", label, "::", detail)


def section(body: str, start: str, end: str | None) -> str:
    left = body.index(start)
    right = len(body) if end is None else body.index(end, left)
    return body[left:right]


def line_has(path: Path, line_number: int, fragment: str) -> bool:
    rows = path.read_text(encoding="utf-8").splitlines()
    return (
        1 <= line_number <= len(rows)
        and fragment.lower() in rows[line_number - 1].lower()
    )


def science_cold_run() -> None:
    completed = subprocess.run(
        [sys.executable, str(SCIENCE)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=240,
        check=False,
    )
    matches = re.findall(
        r"SUMMARY PASS\s+(\d+)\s+FAIL\s+(\d+)", completed.stdout
    )
    observed = tuple(map(int, matches[-1])) if matches else None
    check(
        "the Cycle-317 science certificate reruns cold",
        completed.returncode == 0 and observed == (15, 0),
        {"returncode": completed.returncode, "observed": observed},
    )


def freshness_and_baseline_controls(note: str) -> None:
    completed = subprocess.run(
        ["git", "merge-base", "--is-ancestor", FRESH_MAIN, "origin/main"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    check(
        "the recorded no-go methodology commit remains an ancestor of origin/main",
        completed.returncode == 0,
        {"recorded": FRESH_MAIN, "current_ref": "origin/main"},
    )
    required_rows = (
        "| operational quantum / Records | 61% | 27% | 88% | 3.2/5 |",
        "| causal time / clock | 34% | 17% | 62% | 1.8/5 |",
        "| inertia / matter | 73% | 34% | 94% | 4.0/5 |",
        "| gravity / source / resource | 39% | 16% | 65% | 2.0/5 |",
        "| Born / probability / realized history | 34% | 14% | 85% | 2.0/5 |",
    )
    missing = tuple(row for row in required_rows if row not in note)
    check(
        "the release note carries the accepted Cycle-315/318 and conservative Cycle-317 planning baseline",
        not missing,
        missing,
    )


def n1_controls(note: str) -> None:
    n1 = section(note, "### N1", "### N2")
    allowed = {
        "ATTEMPTED",
        "RULED OUT BY PRIOR RESULT",
        "OPEN / UNTESTED",
    }
    markers = {}
    malformed = []
    for route in N1_ROUTES:
        pattern = re.compile(
            rf"^\|\s*{re.escape(route)}\s*\|[^|]*\|\s*(\*\*[^*]+\*\*)\s*\|",
            re.MULTILINE,
        )
        match = pattern.search(n1)
        raw = match.group(1) if match else ""
        marker = raw.replace("*", "")
        markers[route] = marker
        if raw != f"**{marker}**" or marker not in allowed:
            malformed.append((route, raw, marker))
    all_bold = tuple(re.findall(r"\*\*([^*]+)\*\*", n1))
    check(
        "N1 uses only exact bold honesty markers on eight distinct routes",
        not malformed
        and len(markers) == 8
        and len(all_bold) == 8
        and set(all_bold) <= allowed
        and tuple(markers.values()).count("ATTEMPTED") == 4
        and tuple(markers.values()).count("OPEN / UNTESTED") == 4,
        {"markers": markers, "malformed": malformed, "all_bold": all_bold},
    )


def n2_controls(note: str) -> None:
    n2 = section(note, "### N2", "### N3")
    rows = []
    for left, right in combinations(WALLS, 2):
        pattern = re.compile(
            rf"^\|\s*`{left}/{right}`\s*\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|",
            re.MULTILINE | re.IGNORECASE,
        )
        match = pattern.search(n2)
        values = tuple(value.lower() for value in match.groups()) if match else None
        rows.append((left, right, values))
    check(
        "N2 validates both closure directions for the complete ten-pair collapsed wall table",
        len(rows) == 10 and all(row[2] == ("no", "no", "yes") for row in rows),
        rows,
    )


def n3_controls() -> None:
    release_paths = (SCIENCE, NOTE, Path(__file__).resolve())
    rows = []
    for path in release_paths:
        content = path.read_text(encoding="utf-8").lower().splitlines()
        hits = []
        for parts in TRIGGER_PARTS:
            trigger = "".join(parts)
            hits.extend(
                (trigger, line_number)
                for line_number, line in enumerate(content, 1)
                if trigger in line
            )
        rows.append(
            {"path": str(path.relative_to(ROOT)), "hits": tuple(hits)}
        )
    check(
        "N3 literal hidden-condition procedure scan has zero hits on every release path",
        all(not row["hits"] for row in rows),
        rows,
    )


def n4_controls(note: str) -> None:
    local_witnesses = (
        (
            ROOT / "docs/work_history/repo/review_feedback/ACTUAL_CONTACT_ACTION_SYNDROME_TOURNAMENT_CYCLE285_NOTE_2026-07-17.md",
            248,
            "deletion close norm",
        ),
        (
            ROOT / "docs/work_history/repo/review_feedback/ACTUAL_CONTACT_ACTION_SYNDROME_TOURNAMENT_CYCLE285_NOTE_2026-07-17.md",
            267,
            "with matter disturbance zero. This does not show",
        ),
        (
            ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_COMMON_M64_FIXED_SEAM_CYCLE311_NOTE_2026-07-18.md",
            52,
            "exp(i binom(n,2) g),  g=0.37",
        ),
        (
            ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_COMMON_M64_FIXED_SEAM_CYCLE311_NOTE_2026-07-18.md",
            196,
            "at most fifty-six M2",
        ),
        (
            ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_COMMON_M64_FIXED_SEAM_CYCLE311_NOTE_2026-07-18.md",
            259,
            "one-particle mass fixture is unchanged",
        ),
        (
            ROOT / "docs/work_history/repo/review_feedback/CONTACT_CLOSE_TYPED_RECORD_DAG_CYCLE287_NOTE_2026-07-17.md",
            280,
            "No pointer, close bit, history carrier",
        ),
    )
    local_rows = tuple(
        (
            str(path.relative_to(ROOT)),
            line_number,
            fragment,
            line_has(path, line_number, fragment),
            f"{path.relative_to(ROOT)}:{line_number}" in note,
        )
        for path, line_number, fragment in local_witnesses
    )
    check(
        "N4 validates every decisive prior local witness at one exact file and line",
        all(row[3] and row[4] for row in local_rows),
        local_rows,
    )

    fragments = (
        "the accepted Cycle-311 same-number seam qubit carries the actual Cycle-230 contact as diag(exp(ig),1) through held L=6",
        "one fixed physical Naimark isometry derives a normalized positive contact-sensitive ternary trine menu",
        "the PR-5479 smooth non-Born family satisfies every held binary complement but fails physically dilated ternary menus",
        "the bounded X1^(8) dilation compiler derives the exact ray-split and four-component merge menus used by PR-5479 T3",
        "every held qubit effect is an element of the same bounded mixed-projective dilation domain with at most three components",
        "a held Born trace functional satisfies the compiled normalization, ray-refinement, merge, and same-effect identities",
        "every physical dilation block has bounded matrix-unit support, zero inherited leakage, and constant three-M2 pointer overhead through held L=6",
        "the contact-trine and split/merge dilation families have carried covariance under all 24 proper-cubic frames",
        "deleting one fine dilation branch creates detected normalization loss rather than a hidden coarse-menu relabeling",
    )
    science_lines = SCIENCE.read_text(encoding="utf-8").splitlines()
    relative = str(SCIENCE.relative_to(ROOT))
    current_rows = []
    for fragment in fragments:
        hits = tuple(
            number
            for number, line in enumerate(science_lines, 1)
            if fragment in line
        )
        reference = f"{relative}:{hits[0]}" if len(hits) == 1 else None
        current_rows.append(
            (fragment, hits, reference, bool(reference and reference in note))
        )
    check(
        "N4 pins every decisive current residual to one exact executable line",
        all(len(row[1]) == 1 and row[3] for row in current_rows),
        current_rows,
    )

    remote = (
        (
            "84053108a424cef26dc23e484549df331ad2050f",
            "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md",
        ),
        (
            "ba43072a9edffa698d28b3ca3de578e31c8ca527",
            "docs/MINIMAL_RECORD_INSTRUMENT_DILATION_SCALAR_EXCHANGE_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md",
        ),
        (
            "ba43072a9edffa698d28b3ca3de578e31c8ca527",
            "docs/AUTONOMOUS_INTERMITTENT_RECORD_INSTRUMENT_CALIBRATION_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md",
        ),
    )
    remote_rows = []
    for sha, path in remote:
        completed = subprocess.run(
            ["git", "cat-file", "-e", f"{sha}:{path}"],
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        remote_rows.append((sha, path, completed.returncode, f"{sha}:{path}" in note))
    check(
        "N4 pins the remote theorem/instrument evidence to exact immutable objects",
        all(row[2] == 0 and row[3] for row in remote_rows),
        remote_rows,
    )


def n5_to_n8_and_broad_controls(note: str) -> None:
    flat = " ".join(note.split())
    requirements = (
        (
            "N5 separates effect, site, block, one-shot-capacity, and global resolutions",
            (
                "per-effect/site tested",
                "per-mode/block tested",
                "lattice/global tested",
                "one ternary menu is not G2",
                "eight-label compiler is not literal arbitrary-finite X1",
            ),
        ),
        (
            "N6 retains six explicit physical import-retirement paths",
            (
                "direction/weight program into bounded physical states",
                "sequential pointer reuse",
                "operational equivalence theorem",
                "actual member/Record law",
                "repeated spacelike/timelike compositions",
                "certified repeated Record corpus",
            ),
        ),
        (
            "N7 contains the strongest autonomous-program/effect-equivalence steelman",
            (
                "hostile constructive reviewer",
                "operational equivalence theorem",
                "recurrent outcome/Record law",
                "selected physical law without altering the substrate",
            ),
        ),
        (
            "N8 records six constructive cross-cycle retirement mechanisms",
            (
                "Cycle 230 coarse CAR cell",
                "Cycle 278 had only a binary support-pointer instrument",
                "Cycle 285 required a cross-number phase reference",
                "PR-5451 dilation/instrument nonselection",
                "Cycle 284 supplied a finite trace process",
                "Cycle 287 conditional Record DAG",
            ),
        ),
    )
    for label, required in requirements:
        missing = tuple(item for item in required if item not in flat)
        check(label, not missing, missing)
    broad_required = (
        "Broad gate status: FAIL / DO NOT SHIP",
        "There is no shared obstruction and no axiom pressure.",
        "Do not claim G2, literal arbitrary-finite X1, a selected weight law",
    )
    missing = tuple(item for item in broad_required if item not in flat)
    check(
        "the broad Born/Record no-go, minimum-content, and axiom-pressure release is explicitly blocked",
        not missing,
        missing,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    science_cold_run()
    freshness_and_baseline_controls(note)
    n1_controls(note)
    n2_controls(note)
    n3_controls()
    n4_controls(note)
    n5_to_n8_and_broad_controls(note)
    print("STRICT SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "STRICT RESULT",
        "CYCLE317_RELEASE_DISCIPLINE_GREEN"
        if FAIL == 0
        else "CYCLE317_RELEASE_BLOCKED",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
