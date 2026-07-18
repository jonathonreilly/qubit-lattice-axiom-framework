#!/usr/bin/env python3
"""Master gate for the July 13 deeper pre-language axiom probes.

This runner composes the extensional-rule, operational-reconstruction, and
complete-interface runners, then adds exact controls for deterministic
frequency selection and the Bell-local intervention boundary.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import re
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "DEEPER_PROBES_FINAL_AXIOM_CONTENT_GATE_NOTE_2026-07-13.md"
CHILDREN = (
    ROOT / "scripts" / "extensional_nearest_neighbor_rule_deep_probe_2026_07_13.py",
    ROOT / "scripts" / "operational_record_reconstruction_deep_probe_2026_07_13.py",
    ROOT / "scripts" / "four_axiom_toe_completeness_gate_2026_07_13.py",
)

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    suffix = f" :: {detail}" if detail else ""
    if condition:
        PASS += 1
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        print(f"FAIL {label}{suffix}")


def note_contract() -> None:
    section("A - Synthesis-note contract")
    raw = NOTE.read_text()
    note = " ".join(raw.lower().replace("**", "").split())
    check("A synthesis is authority-free", "authority: none" in note)
    check("A synthesis contains N1-N8", all(f"### N{i}" in raw for i in range(1, 9)))
    for marker in (
        "the four possible constitutional seams",
        "the predictive specification is larger than these sentences",
        "five-output project checklist",
        "record-state sufficiency",
        "generated finite-site composition",
        "operational nouns do not need to be axioms",
        "current declared remaining toe content",
        "decisive constructive tests still required",
        "compute/storage interpretation remains viable but not yet physics",
    ):
        check(f"A synthesis marker: {marker}", marker in note)
    for key in ("`h`", "`r`", "`m`", "`c`", "`s`"):
        check(f"A operational closure key present: {key}", key in note)


def child_campaign() -> int:
    section("B - Child deep-probe campaign")
    total_child_pass = 0
    for child in CHILDREN:
        result = subprocess.run(
            [sys.executable, str(child)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        matches = re.findall(r"TOTAL PASS=(\d+) FAIL=(\d+)", result.stdout)
        parsed = bool(matches)
        child_pass, child_fail = (map(int, matches[-1])) if parsed else (0, -1)
        total_child_pass += child_pass
        check(f"B child exits cleanly: {child.name}", result.returncode == 0)
        check(f"B child reports zero failures: {child.name}", parsed and child_fail == 0)
    check("B child campaign totals 177 explicit passes", total_child_pass == 177, str(total_child_pass))
    return total_child_pass


def deterministic_frequency_controls() -> None:
    section("C - Determinism versus frequency selection")
    identity = sp.eye(2)
    invariant_weights = []
    for p in (sp.Rational(1, 7), sp.Rational(1, 2), sp.Rational(6, 7)):
        distribution = sp.Matrix([[p, 1 - p]])
        invariant_weights.append(distribution * identity == distribution)
    check("C one deterministic identity law preserves multiple measures", all(invariant_weights))

    cycle = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    p0, p1, p2 = sp.symbols("p0 p1 p2")
    distribution = sp.Matrix([[p0, p1, p2]])
    equations = list(distribution * cycle - distribution) + [p0 + p1 + p2 - 1]
    stationary = sp.solve(equations, (p0, p1, p2), dict=True)
    check(
        "C a deterministic three-cycle has a unique stationary measure",
        stationary == [{p0: sp.Rational(1, 3), p1: sp.Rational(1, 3), p2: sp.Rational(1, 3)}],
    )

    visits = []
    state = 0
    for _ in range(12):
        visits.append(state)
        state = (state + 1) % 3
    check("C every cycle orbit has uniform long-run visit counts", all(visits.count(index) == 4 for index in range(3)))
    check("C determinism alone neither forces nor forbids a frequency theorem", all(invariant_weights) and len(stationary) == 1)


def bell_local_control() -> None:
    section("D - Bell-local deterministic intervention boundary")
    values = []
    for a0, a1, b0, b1 in product((-1, 1), repeat=4):
        chsh = a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1
        values.append(chsh)
    check("D all deterministic setting-independent local assignments obey CHSH <= 2", max(abs(value) for value in values) == 2)
    check("D the deterministic bound is attained", set(values) == {-2, 2})


def final_classification(child_passes: int) -> None:
    section("E - Final bounded classification")
    note = " ".join(NOTE.read_text().lower().replace("**", "").split())
    check("E continuation/permanence may retire under an exact rule", "continuation and permanence retire" in note)
    check("E composition may retire under a generation theorem", "composition retires" in note)
    check("E operational PREP-FRAME may retire definitionally", "prep-frame" in note and "definitions" in note)
    check(
        "E no universal more-axioms claim is made",
        "no universal no-go or unavoidable-axiom claim is made" in note.replace("`", ""),
    )
    check("E child evidence remains exact and green", child_passes == 177)


def main() -> None:
    note_contract()
    child_passes = child_campaign()
    deterministic_frequency_controls()
    bell_local_control()
    final_classification(child_passes)
    print("\n" + "=" * 79)
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    print(f"CHILD PASS={child_passes}")
    if FAIL:
        print("RESULT: FAIL")
        print("BOUNDARY: pre-language synthesis only; no axiom edit is authorized")
        raise SystemExit(1)
    print("RESULT: PASS")
    print("BOUNDARY: the named finite probes are green; the next gate is an exact predictive specification or a proved physical-equivalence class")


if __name__ == "__main__":
    main()
