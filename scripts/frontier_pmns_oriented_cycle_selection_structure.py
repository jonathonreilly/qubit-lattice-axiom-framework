#!/usr/bin/env python3
"""Raw finite matrix identities for the PMNS oriented-cycle row.

This runner deliberately checks only the displayed 3x3 matrices and maps:

  1. exact C3 covariance on A_fwd = c1 E12 + c2 E23 + c3 E31;
  2. zero forward-cycle coefficients for the specified identity matrix I3;
  3. the fixed locus of the prescribed map A -> P23 A^dag P23.

It also checks that the repaired source note and generated audit metadata
exclude the prior carrier/value-law and physical-bridge readings.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=140)

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "pmns_oriented_cycle_selection_structure_note"
NOTE_PATH = ROOT / "docs/PMNS_ORIENTED_CYCLE_SELECTION_STRUCTURE_NOTE.md"
LEDGER_PATH = ROOT / "docs/audit/data/audit_ledger.json"
GRAPH_PATH = ROOT / "docs/audit/data/citation_graph.json"
QUEUE_PATH = ROOT / "docs/audit/data/audit_queue.json"

PASS_COUNT = 0
FAIL_COUNT = 0


def e(i: int, j: int) -> np.ndarray:
    out = np.zeros((3, 3), dtype=complex)
    out[i, j] = 1.0
    return out


E12 = e(0, 1)
E23 = e(1, 2)
E31 = e(2, 0)
CYCLE = E12 + E23 + E31
I3 = np.eye(3, dtype=complex)
P23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)


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


def cycle_block(coeffs: np.ndarray) -> np.ndarray:
    c1, c2, c3 = np.asarray(coeffs, dtype=complex)
    return c1 * E12 + c2 * E23 + c3 * E31


def forward_cycle_coeffs(a: np.ndarray) -> np.ndarray:
    return np.array([a[0, 1], a[1, 2], a[2, 0]], dtype=complex)


def cycle_covariant_rotate(a: np.ndarray) -> np.ndarray:
    return CYCLE @ a @ CYCLE.conj().T


def residual_swap_conjugate(a: np.ndarray) -> np.ndarray:
    return P23 @ a.conj().T @ P23


def forbidden_phrases() -> list[str]:
    return [
        "carrier and observable law are " + "closed",
        "sole axiom " + "selects",
        "graph-first selected-axis " + "route",
        "[" + "PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md" + "]",
    ]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def queue_position(queue_data: dict) -> tuple[int | None, dict | None]:
    for index, item in enumerate(queue_data.get("queue", []), start=1):
        if isinstance(item, dict) and item.get("claim_id") == CLAIM_ID:
            return index, item
    return None, None


def part0_source_and_audit_metadata_firewall() -> None:
    print("\n" + "=" * 88)
    print("PART 0: SOURCE AND AUDIT METADATA FIREWALL")
    print("=" * 88)

    note = NOTE_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    corpus = note + "\n" + source

    required_note_phrases = [
        "Raw Matrix Identities",
        "raw-matrix repair",
        "does not claim the carrier or native observable/value law",
        "does not claim that the specified identity block is the physical sole-axiom free-point block",
        "does not claim that graph-first induces the prescribed swap-conjugation map",
        "The carrier and observable law remain outside this repaired row",
    ]
    for phrase in required_note_phrases:
        check(f"source note states boundary phrase: {phrase}", phrase in note)

    for phrase in forbidden_phrases():
        check(f"source corpus excludes stale overclaim phrase: {phrase}", phrase not in corpus)

    ledger = load_json(LEDGER_PATH)
    row = ledger["rows"].get(CLAIM_ID)
    check("audit ledger row exists", row is not None)
    if row is None:
        return
    check("audit ledger keeps source claim type bounded_theorem", row.get("claim_type") == "bounded_theorem", str(row.get("claim_type")))
    check("audit ledger row reset to unaudited for re-audit", row.get("audit_status") == "unaudited", str(row.get("audit_status")))
    check("effective status reset to unaudited for re-audit", row.get("effective_status") == "unaudited", str(row.get("effective_status")))
    check("raw-matrix repair has no ledger dependencies", row.get("deps") == [], str(row.get("deps")))

    graph = load_json(GRAPH_PATH)
    node = graph["nodes"].get(CLAIM_ID)
    outgoing = [edge for edge in graph["edges"] if edge.get("from") == CLAIM_ID]
    check("citation graph node exists", node is not None)
    if node is not None:
        check("citation graph node has no dependencies", node.get("deps") == [], str(node.get("deps")))
    check("citation graph has no outgoing dependency edge", outgoing == [], str(outgoing))

    queue = load_json(QUEUE_PATH)
    position, item = queue_position(queue)
    check("raw-matrix repair is queued for audit", item is not None, f"position={position}")
    if item is not None:
        check("queued row is ready because deps are empty", item.get("ready") is True, str(item.get("ready")))
        check("queued row has empty dependency list", item.get("deps") == [], str(item.get("deps")))


def part1_exact_c3_covariance_collapses_to_one_complex_slot() -> None:
    print("\n" + "=" * 88)
    print("PART 1: EXACT C3 COVARIANCE COLLAPSES TO ONE COMPLEX SLOT")
    print("=" * 88)

    coeffs = np.array([1.0 + 0.2j, -0.3 + 0.7j, 0.5 - 0.4j], dtype=complex)
    a = cycle_block(coeffs)
    rotated = cycle_covariant_rotate(a)
    rotated_coeffs = forward_cycle_coeffs(rotated)
    sigma = 0.37 + 0.11j
    sigma_block = cycle_block(np.array([sigma, sigma, sigma], dtype=complex))

    check(
        "C3 conjugation cyclically permutes forward-cycle coefficients",
        np.linalg.norm(rotated_coeffs - np.array([coeffs[1], coeffs[2], coeffs[0]], dtype=complex)) < 1e-12,
        f"rotated={np.round(rotated_coeffs, 6)}",
    )
    check(
        "The exact C3 fixed locus contains sigma*(1,1,1)",
        np.linalg.norm(cycle_covariant_rotate(sigma_block) - sigma_block) < 1e-12,
        f"sigma={sigma}",
    )
    check(
        "The C3-fixed block is exactly sigma C",
        np.linalg.norm(sigma_block - sigma * CYCLE) < 1e-12,
    )


def part2_specified_identity_input_has_zero_cycle_coefficients() -> None:
    print("\n" + "=" * 88)
    print("PART 2: SPECIFIED IDENTITY INPUT HAS ZERO CYCLE COEFFICIENTS")
    print("=" * 88)

    coeffs = forward_cycle_coeffs(I3)
    sigma = np.mean(coeffs)

    check("I3 has zero forward-cycle coefficients", np.linalg.norm(coeffs) < 1e-12, f"coeffs={np.round(coeffs, 6)}")
    check("Therefore the specified identity input has sigma = 0", abs(sigma) < 1e-12, f"sigma={sigma}")
    print("  [INFO] This is only a matrix identity on I3, not a physical free-point bridge.")


def part3_prescribed_swap_conjugation_fixed_locus() -> None:
    print("\n" + "=" * 88)
    print("PART 3: PRESCRIBED SWAP-CONJUGATION FIXED LOCUS")
    print("=" * 88)

    coeffs_good = np.array([0.41 + 0.32j, 0.28 + 0.0j, 0.41 - 0.32j], dtype=complex)
    coeffs_bad = np.array([0.41 + 0.32j, 0.28 + 0.07j, 0.33 - 0.11j], dtype=complex)
    a_good = cycle_block(coeffs_good)
    a_bad = cycle_block(coeffs_bad)
    mapped_good = residual_swap_conjugate(a_good)
    mapped_bad = residual_swap_conjugate(a_bad)

    check(
        "The prescribed swap-conjugation map preserves the displayed cycle support",
        np.array_equal(np.abs(mapped_good) > 1e-12, np.abs(a_good) > 1e-12),
    )
    check(
        "Its fixed locus contains c1 = conjugate(c3), c2 real",
        np.linalg.norm(mapped_good - a_good) < 1e-12,
        f"coeffs={np.round(coeffs_good, 6)}",
    )
    check(
        "A generic cycle triple is not fixed by the prescribed map",
        np.linalg.norm(mapped_bad - a_bad) > 1e-6,
        f"coeffs={np.round(coeffs_bad, 6)}",
    )
    print("  [INFO] The prescribed map leaves a 3-real fixed family: (Re c1, Im c1, c2).")


def part4_result() -> None:
    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Raw finite matrix identities:")
    print("    - exact C3 covariance collapses the displayed cycle subspace to sigma C")
    print("    - the specified identity input sets sigma = 0")
    print("    - the prescribed swap-conjugation map fixes c1 = conjugate(c3), c2 real")
    print()
    print("  The carrier and observable law remain outside this repaired row.")


def main() -> int:
    print("=" * 88)
    print("PMNS ORIENTED CYCLE RAW MATRIX REPAIR")
    print("=" * 88)
    print()
    print("Question:")
    print("  What finite matrix identities follow for the displayed cycle subspace")
    print("  and prescribed swap-conjugation map?")

    part0_source_and_audit_metadata_firewall()
    part1_exact_c3_covariance_collapses_to_one_complex_slot()
    part2_specified_identity_input_has_zero_cycle_coefficients()
    part3_prescribed_swap_conjugation_fixed_locus()
    part4_result()

    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
