#!/usr/bin/env python3
"""Finite R_conn channel-fraction algebra with explicit selector premise.

This runner verifies only the repaired scope:

  * M_3(C) splits into a 1-dimensional scalar channel and an 8-dimensional
    traceless channel;
  * the channel fraction is exactly 8/9;
  * kappa_EW parameterizes the missing selector rather than being derived;
  * the audit ledger/queue register the row as dependency-free re-audit work.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "rconn_derived_note"
RUNNER_PATH = "scripts/frontier_rconn_admitted_selector_channel_fraction_repair.py"
NOTE_PATH = ROOT / "docs/RCONN_DERIVED_NOTE.md"
LEDGER_PATH = ROOT / "docs/audit/data/audit_ledger.json"
GRAPH_PATH = ROOT / "docs/audit/data/citation_graph.json"
QUEUE_PATH = ROOT / "docs/audit/data/audit_queue.json"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def queue_position(queue_data: dict) -> tuple[int | None, dict | None]:
    for index, item in enumerate(queue_data.get("queue", []), start=1):
        if isinstance(item, dict) and item.get("claim_id") == CLAIM_ID:
            return index, item
    return None, None


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def part0_source_firewall() -> None:
    section("PART 0: SOURCE FIREWALL")
    note = NOTE_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    required_note_phrases = [
        "admitted-selector rescope",
        "conditional-support - finite channel-fraction algebra",
        "This row does not derive the connected-trace selector `(M0)`",
        "This row does not prove `kappa_EW = 0`",
        "This row does not depend on a Yukawa color-projection theorem",
        "This row does not add a new axiom",
        RUNNER_PATH,
    ]
    for phrase in required_note_phrases:
        check(f"source note contains boundary phrase: {phrase}", phrase in note)

    forbidden_note_phrases = [
        "R_conn(MC)",
        "canonical_" + "plaquette_surface",
        "YUKAWA_COLOR" + "_PROJECTION_THEOREM.md",
        "EW_CURRENT_MATCHING_RULE_OPEN_GATE" + "_NOTE_2026-05-03.md",
        "beta = 6 (g_bare",
        "large-N_c structural estimate",
        "retained lattice-current primitives derive",
    ]
    for phrase in forbidden_note_phrases:
        check(f"source note excludes old dependency phrase: {phrase}", phrase not in note)

    forbidden_runner_phrases = [
        "canonical_" + "plaquette_surface",
        "frontier_" + "color_projection_mc",
        "YUKAWA_" + "COLOR" + "_PROJECTION",
        "observ" + "ed alpha",
    ]
    for phrase in forbidden_runner_phrases:
        check(f"runner source excludes old dependency phrase: {phrase}", phrase not in source)


def part1_exact_channel_fraction() -> None:
    section("PART 1: EXACT CHANNEL-FRACTION ALGEBRA")

    n = 3
    total_dim = n * n
    scalar_dim = 1
    traceless_dim = total_dim - scalar_dim
    f_adj = Fraction(traceless_dim, total_dim)
    f_singlet = Fraction(scalar_dim, total_dim)

    check("M_3(C) has dimension 9", total_dim == 9, f"dim={total_dim}")
    check("scalar channel has dimension 1", scalar_dim == 1, f"dim={scalar_dim}")
    check("traceless channel has dimension 8", traceless_dim == 8, f"dim={traceless_dim}")
    check("channel dimensions sum to the total", scalar_dim + traceless_dim == total_dim)
    check("adjoint/traceless channel fraction is 8/9", f_adj == Fraction(8, 9), f"F_adj={f_adj}")
    check("singlet/scalar channel fraction is 1/9", f_singlet == Fraction(1, 9), f"F_singlet={f_singlet}")

    for kappa, expected in [
        (Fraction(0), Fraction(8, 9)),
        (Fraction(1), Fraction(1)),
        (Fraction(1, 2), Fraction(17, 18)),
    ]:
        readout = f_adj + kappa * f_singlet
        check(f"P(kappa_EW={kappa}) = {expected}", readout == expected, f"P={readout}")

    k0 = Fraction(1, 1) / (f_adj + Fraction(0) * f_singlet)
    k1 = Fraction(1, 1) / (f_adj + Fraction(1) * f_singlet)
    check("inverse package factor at selector kappa=0 is 9/8", k0 == Fraction(9, 8), f"K={k0}")
    check("inverse package factor at full trace kappa=1 is 1", k1 == Fraction(1), f"K={k1}")
    check("finite algebra admits at least two distinct selector completions", k0 != k1, f"K0={k0}, K1={k1}")


def part2_audit_metadata() -> None:
    section("PART 2: AUDIT METADATA AFTER PIPELINE")

    ledger = load_json(LEDGER_PATH)
    row = ledger.get("rows", {}).get(CLAIM_ID)
    check("claim ledger row exists", row is not None)
    if row is None:
        return

    check("claim type remains bounded_theorem", row.get("claim_type") == "bounded_theorem", str(row.get("claim_type")))
    check("audit status reset to unaudited for re-audit", row.get("audit_status") == "unaudited", str(row.get("audit_status")))
    check("effective status reset to unaudited for re-audit", row.get("effective_status") == "unaudited", str(row.get("effective_status")))
    check("primary runner is registered", row.get("runner_path") == RUNNER_PATH, str(row.get("runner_path")))
    check("no helper runners are imported", row.get("helper_runner_paths") == [], str(row.get("helper_runner_paths")))
    check("narrowed row has no ledger dependencies", row.get("deps") == [], str(row.get("deps")))
    check("no open dependency paths remain", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))

    graph = load_json(GRAPH_PATH)
    node = graph.get("nodes", {}).get(CLAIM_ID)
    outgoing = [edge for edge in graph.get("edges", []) if edge.get("from") == CLAIM_ID]
    check("citation graph node exists", node is not None)
    if node is not None:
        check("citation graph node has no dependencies", node.get("deps") == [], str(node.get("deps")))
        check("citation graph node has registered runner", node.get("runner_path") == RUNNER_PATH, str(node.get("runner_path")))
        check("citation graph node has no helper runners", node.get("helper_runner_paths") == [], str(node.get("helper_runner_paths")))
    check("citation graph has no outgoing dependency edges", outgoing == [], str(outgoing))

    queue = load_json(QUEUE_PATH)
    position, item = queue_position(queue)
    check("claim is queued for audit", item is not None, f"position={position}")
    if item is not None:
        check("queued claim is ready", item.get("ready") is True, str(item.get("ready")))
        open_dependency_paths = item.get("open_dependency_paths") or []
        check("queue item has no open dependency paths", open_dependency_paths == [], str(item.get("open_dependency_paths")))


def main() -> int:
    print("R_conn admitted-selector channel-fraction repair")
    print(f"Claim: {CLAIM_ID}")
    print(f"Runner: {RUNNER_PATH}")

    part0_source_firewall()
    part1_exact_channel_fraction()
    part2_audit_metadata()

    print("\n" + "=" * 88)
    print("SUMMARY")
    print("=" * 88)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
