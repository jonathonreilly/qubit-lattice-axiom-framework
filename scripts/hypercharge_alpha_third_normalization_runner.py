#!/usr/bin/env python3
"""Bounded premise-packet bridge: alpha = 1/3 by exact arithmetic.

The runner checks only:

1. the retained 6+2 traceless ratio beta = -3 alpha;
2. the explicitly accepted P1-P4 premise packet in the source note;
3. the exact rational solve for alpha = 1/3;
4. the generated audit metadata after pipeline reset.

It deliberately does not use quark charge cross-checks, fitted values, Monte
Carlo data, or any lattice-action input.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "hypercharge_alpha_third_normalization_bridge_bounded_note_2026-05-25"
NOTE_PATH = ROOT / "docs/HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md"
LEDGER_PATH = ROOT / "docs/audit/data/audit_ledger.json"
QUEUE_PATH = ROOT / "docs/audit/data/audit_queue.json"
GRAPH_PATH = ROOT / "docs/audit/data/citation_graph.json"
EXPECTED_DEPS = [
    "graph_first_su3_integration_note",
    "graph_first_selector_derivation_note",
]

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    msg = f"{status}: {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return condition


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def queue_position(queue_data: dict) -> tuple[int | None, dict | None]:
    for index, item in enumerate(queue_data.get("queue", []), start=1):
        if isinstance(item, dict) and item.get("claim_id") == CLAIM_ID:
            return index, item
    return None, None


def part0_source_and_audit_metadata() -> None:
    print("\n== Part 0: source and audit metadata ==")
    note = NOTE_PATH.read_text(encoding="utf-8")

    required = [
        "Accepted-premise packet (not axioms)",
        "P1 Anti^2-as-L_L readout convention",
        "P2 Gell-Mann-Nishijima convention",
        "P3 weak-isospin assignment",
        "P4 electron-charge unit convention",
        "does not claim to derive the premise packet",
        "no new axiom is introduced",
    ]
    for phrase in required:
        check(f"source contains boundary phrase: {phrase}", phrase in note)

    forbidden = [
        "empirical SM electric " + "charges",
        "Q(" + "u_L)",
        "Q(" + "d_L)",
    ]
    for phrase in forbidden:
        check(f"source note excludes non-load-bearing cross-check phrase: {phrase}", phrase not in note)

    ledger = load_json(LEDGER_PATH)
    row = ledger["rows"].get(CLAIM_ID)
    check("audit ledger row exists", row is not None)
    if row is None:
        return
    check("claim type remains bounded_theorem", row.get("claim_type") == "bounded_theorem", str(row.get("claim_type")))
    check("audit status reset to unaudited for re-audit", row.get("audit_status") == "unaudited", str(row.get("audit_status")))
    check("effective status reset to unaudited for re-audit", row.get("effective_status") == "unaudited", str(row.get("effective_status")))
    check("retained graph-first dependencies are explicit", row.get("deps") == EXPECTED_DEPS, str(row.get("deps")))

    graph = load_json(GRAPH_PATH)
    node = graph["nodes"].get(CLAIM_ID)
    check("citation graph node exists", node is not None)
    if node is not None:
        check("citation graph deps match retained graph-first inputs", node.get("deps") == EXPECTED_DEPS, str(node.get("deps")))

    queue = load_json(QUEUE_PATH)
    position, item = queue_position(queue)
    check("premise-packet bridge is queued for audit", item is not None, f"position={position}")
    if item is not None:
        check("queued row is ready because deps are retained", item.get("ready") is True, str(item.get("ready")))


def part1_exact_ratio() -> Fraction:
    print("\n== Part 1: retained 6+2 traceless ratio ==")
    sym_multiplicity = Fraction(6, 1)
    anti_multiplicity = Fraction(2, 1)
    beta_over_alpha = -sym_multiplicity / anti_multiplicity
    check("tracelessness on the 6+2 split gives beta/alpha = -3", beta_over_alpha == Fraction(-3, 1), str(beta_over_alpha))
    return beta_over_alpha


def part2_exact_solve(beta_over_alpha: Fraction) -> Fraction:
    print("\n== Part 2: exact rational solve from P1-P4 ==")
    t3_e_left = Fraction(-1, 2)
    q_e_left = Fraction(-1, 1)

    alpha = (q_e_left - t3_e_left) * Fraction(2, 1) / beta_over_alpha
    check("alpha = 1/3 follows from Q(e_L), T3(e_L), and Y(L_L)=beta", alpha == Fraction(1, 3), str(alpha))

    y_l_left = beta_over_alpha * alpha
    check("Y(L_L) = -1 at alpha = 1/3", y_l_left == Fraction(-1, 1), str(y_l_left))
    return alpha


def part3_result(alpha: Fraction) -> None:
    print("\n== Result ==")
    print(f"alpha = {alpha}")
    print("Bounded bridge: retained 6+2 split/tracelessness + accepted premise packet P1-P4.")
    print("No new axiom and no claim to derive P1-P4.")


def main() -> int:
    print("HYPERCHARGE ALPHA=1/3 PREMISE-PACKET BRIDGE")
    part0_source_and_audit_metadata()
    beta_over_alpha = part1_exact_ratio()
    alpha = part2_exact_solve(beta_over_alpha)
    part3_result(alpha)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded premise-packet bridge passes; alpha = 1/3 follows "
            "from retained 6+2 split/tracelessness + accepted premise packet P1-P4 "
            "by rational arithmetic."
        )
        return 0
    print("VERDICT: bounded premise-packet bridge FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
