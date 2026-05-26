#!/usr/bin/env python3
"""Raw Hermitian-pair to projector-packet interface.

This runner verifies only finite linear algebra:

  * U_pair = U_e^dagger U_nu is unitary;
  * |U_pair|^2 is doubly stochastic;
  * |U_pair|^2 is invariant under independent eigenvector rephasings.

It intentionally does not compute leptogenesis transport diagnostics or import
the DM transport helper module.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=140)

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "dm_leptogenesis_pmns_projector_interface_note_2026-04-16"
NOTE_PATH = ROOT / "docs/DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md"
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


def canonical_left_diagonalizer(h: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    evals, u = np.linalg.eigh(h)
    order = np.argsort(np.real(evals))
    evals = np.real(evals[order])
    u = u[:, order]
    return evals, u


def projector_packet(h_nu: np.ndarray, h_e: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    _eval_nu, u_nu = canonical_left_diagonalizer(h_nu)
    _eval_e, u_e = canonical_left_diagonalizer(h_e)
    u_pair = u_e.conj().T @ u_nu
    return u_pair, np.abs(u_pair) ** 2


def deterministic_pairs() -> list[tuple[str, np.ndarray, np.ndarray]]:
    rng = np.random.default_rng(seed=20260525)
    pairs: list[tuple[str, np.ndarray, np.ndarray]] = []

    h_nu = np.array(
        [
            [2.6, 0.2 + 0.1j, -0.3j],
            [0.2 - 0.1j, 1.7, 0.4 + 0.2j],
            [0.3j, 0.4 - 0.2j, 1.2],
        ],
        dtype=complex,
    )
    h_e = np.array(
        [
            [1.1, -0.1j, 0.15 + 0.04j],
            [0.1j, 2.4, -0.2 + 0.05j],
            [0.15 - 0.04j, -0.2 - 0.05j, 3.0],
        ],
        dtype=complex,
    )
    pairs.append(("canonical", h_nu + 2.0 * np.eye(3), h_e + 2.0 * np.eye(3)))

    for idx in range(8):
        a = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
        b = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
        h1 = a @ a.conj().T + 1e-3 * np.eye(3)
        h2 = b @ b.conj().T + 1e-3 * np.eye(3)
        pairs.append((f"random_{idx}", h1, h2))
    return pairs


def part0_source_and_audit_metadata_firewall() -> None:
    print("\n" + "=" * 88)
    print("PART 0: SOURCE AND AUDIT METADATA FIREWALL")
    print("=" * 88)

    note = NOTE_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    required_note_phrases = [
        "Raw Pair-to-Projector Interface",
        "raw-interface repair",
        "does not claim carrier authority",
        "does not claim physical N1 column selection",
        "does not compute or retain eta/eta_obs diagnostics",
        "does not import dm_leptogenesis_exact_common",
        "No new axiom is introduced",
    ]
    for phrase in required_note_phrases:
        check(f"source note states boundary phrase: {phrase}", phrase in note)

    forbidden_source_phrases = [
        "from " + "dm_leptogenesis_exact_common import",
        "solve_multisource_" + "flavored_transport",
        "eta_ratio_single_source_" + "flavored",
    ]
    for phrase in forbidden_source_phrases:
        check(f"runner source excludes transport helper phrase: {phrase}", phrase not in source)

    ledger = load_json(LEDGER_PATH)
    row = ledger["rows"].get(CLAIM_ID)
    check("audit ledger row exists", row is not None)
    if row is None:
        return
    check("claim type remains bounded_theorem", row.get("claim_type") == "bounded_theorem", str(row.get("claim_type")))
    check("audit status reset to unaudited for re-audit", row.get("audit_status") == "unaudited", str(row.get("audit_status")))
    check("effective status reset to unaudited for re-audit", row.get("effective_status") == "unaudited", str(row.get("effective_status")))
    check("raw interface has no ledger dependencies", row.get("deps") == [], str(row.get("deps")))
    check("raw interface has no helper runner paths", row.get("helper_runner_paths") == [], str(row.get("helper_runner_paths")))

    graph = load_json(GRAPH_PATH)
    node = graph["nodes"].get(CLAIM_ID)
    outgoing = [edge for edge in graph["edges"] if edge.get("from") == CLAIM_ID]
    check("citation graph node exists", node is not None)
    if node is not None:
        check("citation graph node has no dependencies", node.get("deps") == [], str(node.get("deps")))
        check("citation graph node has no helper runners", node.get("helper_runner_paths") == [], str(node.get("helper_runner_paths")))
    check("citation graph has no outgoing dependency edge", outgoing == [], str(outgoing))

    queue = load_json(QUEUE_PATH)
    position, item = queue_position(queue)
    check("raw interface is queued for audit", item is not None, f"position={position}")
    if item is not None:
        check("queued row is ready because deps are empty", item.get("ready") is True, str(item.get("ready")))


def part1_unitary_and_doubly_stochastic() -> list[tuple[str, np.ndarray]]:
    print("\n" + "=" * 88)
    print("PART 1: UNITARY PAIR MATRIX AND DOUBLY STOCHASTIC PACKET")
    print("=" * 88)

    packets: list[tuple[str, np.ndarray]] = []
    max_unitary_err = 0.0
    max_row_err = 0.0
    max_col_err = 0.0
    min_entry = 1.0
    for name, h_nu, h_e in deterministic_pairs():
        u_pair, packet = projector_packet(h_nu, h_e)
        packets.append((name, packet))
        max_unitary_err = max(max_unitary_err, float(np.linalg.norm(u_pair @ u_pair.conj().T - np.eye(3))))
        max_row_err = max(max_row_err, float(np.linalg.norm(np.sum(packet, axis=1) - np.ones(3))))
        max_col_err = max(max_col_err, float(np.linalg.norm(np.sum(packet, axis=0) - np.ones(3))))
        min_entry = min(min_entry, float(np.min(packet)))

    check("U_pair is unitary on every deterministic Hermitian pair", max_unitary_err < 1e-10, f"max err={max_unitary_err:.2e}")
    check("|U_pair|^2 has row sums equal to one", max_row_err < 1e-10, f"max row err={max_row_err:.2e}")
    check("|U_pair|^2 has column sums equal to one", max_col_err < 1e-10, f"max col err={max_col_err:.2e}")
    check("|U_pair|^2 entries are non-negative", min_entry >= -1e-14, f"min entry={min_entry:.2e}")

    print("  canonical packet:")
    print(np.round(packets[0][1], 6))
    return packets


def part2_rephasing_invariance() -> None:
    print("\n" + "=" * 88)
    print("PART 2: EIGENVECTOR REPHASING INVARIANCE")
    print("=" * 88)

    rng = np.random.default_rng(seed=20260526)
    max_rephase_err = 0.0
    samples = 0
    for _name, h_nu, h_e in deterministic_pairs():
        _eval_nu, u_nu = canonical_left_diagonalizer(h_nu)
        _eval_e, u_e = canonical_left_diagonalizer(h_e)
        base = np.abs(u_e.conj().T @ u_nu) ** 2
        for _ in range(8):
            phase_nu = np.diag(np.exp(1j * rng.uniform(-np.pi, np.pi, size=3)))
            phase_e = np.diag(np.exp(1j * rng.uniform(-np.pi, np.pi, size=3)))
            phased = np.abs((u_e @ phase_e).conj().T @ (u_nu @ phase_nu)) ** 2
            max_rephase_err = max(max_rephase_err, float(np.linalg.norm(base - phased)))
            samples += 1

    check(
        "|U_pair|^2 is invariant under independent eigenvector rephasings",
        max_rephase_err < 1e-10,
        f"max err={max_rephase_err:.2e}, samples={samples}",
    )


def part3_result() -> None:
    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Raw algebraic interface:")
    print("    - supplied Hermitian pair -> U_pair = U_e^dagger U_nu")
    print("    - |U_pair|^2 is doubly stochastic")
    print("    - |U_pair|^2 is invariant under eigenvector rephasings")
    print()
    print("  Carrier authority, physical N1 column selection, and eta diagnostics remain outside this repaired row.")


def main() -> int:
    print("=" * 88)
    print("DM LEPTOGENESIS PMNS PROJECTOR RAW INTERFACE")
    print("=" * 88)

    part0_source_and_audit_metadata_firewall()
    part1_unitary_and_doubly_stochastic()
    part2_rephasing_invariance()
    part3_result()

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
