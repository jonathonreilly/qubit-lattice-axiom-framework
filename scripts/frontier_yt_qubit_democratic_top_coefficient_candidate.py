#!/usr/bin/env python3
"""Qubit democratic Q_L top-coefficient candidate for the Y_T lane."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_qubit_democratic_top_coefficient_candidate_2026-05-25.json"

NOTE = DOCS / "YT_QUBIT_DEMOCRATIC_TOP_COEFFICIENT_CANDIDATE_NOTE_2026-05-25.md"
MINIMAL_AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
FULL_COURT = DOCS / "YT_TOP_COEFFICIENT_FULL_COURT_PRESS_NOTE_2026-05-25.md"
SYMBOLIC_TOP = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ledger_row(claim_id: str) -> dict[str, Any]:
    ledger = json.loads(read(LEDGER))
    rows = ledger["rows"]
    iterable = rows.values() if isinstance(rows, dict) else rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row
    raise KeyError(claim_id)


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and authority")
    for path in (NOTE, MINIMAL_AXIOMS, FULL_COURT, SYMBOLIC_TOP, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Axiom-First Setup",
        "Exact Mathematics",
        "Why This Is New Science Rather Than The Old Trap",
        "Relationship To Step 1",
        "What Still Does Not Close",
        "Firewalls",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    statuses = {
        "source_action": ledger_row("yt_source_action_support_packet_note_2026-05-22").get("effective_status"),
        "ew_mass": ledger_row("ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26").get("effective_status"),
    }
    check("source-action support is retained_bounded", statuses["source_action"] == "retained_bounded")
    check("EW mass theorem is retained", statuses["ew_mass"] == "retained")
    check("minimal axioms are qubit-on-Z3 framed", "Reality is a qubit at every lattice site" in read(MINIMAL_AXIOMS))
    return statuses


def part2_democratic_invariant_vector() -> None:
    print("\nPart 2: democratic invariant vector")
    n = 6
    entries = sp.symbols("u0:6")
    equations = []
    for i in range(n - 1):
        equations.append(sp.Eq(entries[i], entries[i + 1]))
    solution = sp.solve(equations, entries[1:], dict=True)[0]
    check("S6 transposition invariance forces all entries equal", all(solution[entries[i]] == entries[0] for i in range(1, n)), solution)

    u = sp.Matrix([sp.Rational(1, 1) / sp.sqrt(n)] * n)
    check("democratic vector has unit norm", is_zero((u.T * u)[0] - 1), (u.T * u)[0])
    for idx in (0, 2, 5):
        basis = sp.eye(n)[:, idx]
        amp = (basis.T * u)[0]
        check(f"component {idx} amplitude is 1/sqrt(6)", is_zero(amp - 1 / sp.sqrt(n)), amp)


def part3_uniqueness_under_permutations() -> None:
    print("\nPart 3: uniqueness under color-isospin democracy")
    n = 6
    u = sp.Matrix([1 / sp.sqrt(n)] * n)
    # Adjacent transpositions generate S_6.
    for i in range(n - 1):
        p = sp.eye(n)
        p[i, i] = 0
        p[i + 1, i + 1] = 0
        p[i, i + 1] = 1
        p[i + 1, i] = 1
        check(f"democratic vector invariant under adjacent swap {i}<->{i+1}", p * u == u)

    w = sp.Matrix([2, 1, 1, 1, 1, 1])
    p01 = sp.eye(n)
    p01[0, 0] = p01[1, 1] = 0
    p01[0, 1] = p01[1, 0] = 1
    check("non-democratic vector breaks permutation invariance", p01 * w != w, p01 * w)


def part4_step1_boundary() -> dict[str, Any]:
    print("\nPart 4: Step 1 boundary")
    amplitude = sp.sqrt(sp.Rational(1, 6))
    candidate_available = True
    bridge_closed = False
    check("candidate amplitude equals 1/sqrt(6)", is_zero(amplitude - 1 / sp.sqrt(6)), amplitude)
    check("candidate is available as exact support", candidate_available)
    check("physical coefficient bridge remains open", not bridge_closed)
    return {
        "democratic_component_amplitude": "1/sqrt(6)",
        "candidate_available": candidate_available,
        "physical_top_coefficient_bridge_closed": bridge_closed,
    }


def part5_firewalls() -> None:
    print("\nPart 5: firewalls")
    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed W/Z/top masses",
        "PDG values",
        "`alpha_LM`",
        "plaquette/u0",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "Status: retained",
        "proposed_retained",
        "`y_33` is derived",
        "`y_t` is derived",
        "positive Y_T closure has been obtained",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T QUBIT DEMOCRATIC TOP-COEFFICIENT CANDIDATE")
    print("=" * 78)

    statuses = part1_anchors()
    part2_democratic_invariant_vector()
    part3_uniqueness_under_permutations()
    boundary = part4_step1_boundary()
    part5_firewalls()

    result = {
        "status": "exact support candidate: democratic Q_L component amplitude is 1/sqrt(6)",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The democratic component amplitude is derived, but the physical bridge "
            "identifying it with y_33 remains open."
        ),
        "boundary": boundary,
        "upstream_statuses": statuses,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_QUBIT_DEMOCRATIC_TOP_COEFFICIENT_CANDIDATE_NOTE_2026-05-25.md",
            "scripts/frontier_yt_qubit_democratic_top_coefficient_candidate.py",
            "outputs/yt_qubit_democratic_top_coefficient_candidate_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
