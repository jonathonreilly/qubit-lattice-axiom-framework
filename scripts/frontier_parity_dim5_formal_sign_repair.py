#!/usr/bin/env python3
"""Formal parity sign identities for dimension-5 SME-style bilinears.

This runner verifies only the repaired scope:

  * 4x4 Dirac parity conjugation by gamma^0;
  * abstract derivative sign character partial_i -> -partial_i;
  * exhaustive formal parity weights for four dimension-5 structures;
  * audit metadata registers the row as dependency-free re-audit work.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "parity_operator_basis_dimension5_lv_no_go_theorem_note_2026-05-02"
RUNNER_PATH = "scripts/frontier_parity_dim5_formal_sign_repair.py"
NOTE_PATH = ROOT / "docs/PARITY_OPERATOR_BASIS_DIMENSION5_LV_NO_GO_THEOREM_NOTE_2026-05-02.md"
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


GAMMA0 = np.array(
    [
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
    ],
    dtype=np.complex128,
)

PAULI_X = np.array([[0, 1], [1, 0]], dtype=np.complex128)
PAULI_Y = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
PAULI_Z = np.array([[1, 0], [0, -1]], dtype=np.complex128)
PAULIS = [PAULI_X, PAULI_Y, PAULI_Z]
INDEX_RANGE = (0, 1, 2, 3)


def gamma_i(i: int) -> np.ndarray:
    sigma = PAULIS[i - 1]
    zero = np.zeros((2, 2), dtype=np.complex128)
    return np.block([[zero, -sigma], [sigma, zero]])


def gamma_mu(mu: int) -> np.ndarray:
    return GAMMA0 if mu == 0 else gamma_i(mu)


def gamma5() -> np.ndarray:
    return 1j * GAMMA0 @ gamma_i(1) @ gamma_i(2) @ gamma_i(3)


def sigma_munu(mu: int, nu: int) -> np.ndarray:
    return 0.5j * (gamma_mu(mu) @ gamma_mu(nu) - gamma_mu(nu) @ gamma_mu(mu))


def parity_conjugate_gamma(matrix: np.ndarray) -> np.ndarray:
    return GAMMA0 @ matrix @ GAMMA0


def derivative_parity_sign(deriv_indices: tuple[int, ...]) -> int:
    sign = 1
    for mu in deriv_indices:
        if mu != 0:
            sign = -sign
    return sign


def spatial_count(indices: tuple[int, ...]) -> int:
    return sum(1 for mu in indices if mu != 0)


def operator_p_weight(gamma: np.ndarray, deriv_indices: tuple[int, ...]) -> int:
    full_p = parity_conjugate_gamma(gamma) * derivative_parity_sign(deriv_indices)
    if np.allclose(full_p, gamma, atol=1e-10):
        return 1
    if np.allclose(full_p, -gamma, atol=1e-10):
        return -1
    return 0


def enumerate_structures() -> list[tuple[str, np.ndarray, tuple[int, ...], int]]:
    records: list[tuple[str, np.ndarray, tuple[int, ...], int]] = []
    eye4 = np.eye(4, dtype=np.complex128)

    for mu in INDEX_RANGE:
        for nu in INDEX_RANGE:
            for rho in INDEX_RANGE:
                total = spatial_count((mu, nu, rho))
                records.append((f"gamma^{mu} d{nu} d{rho}", gamma_mu(mu), (nu, rho), total))

    for mu in INDEX_RANGE:
        for nu in INDEX_RANGE:
            total = spatial_count((mu, nu))
            records.append((f"I d{mu} d{nu}", eye4, (mu, nu), total))

    g5 = gamma5()
    for mu in INDEX_RANGE:
        for nu in INDEX_RANGE:
            total = 3 + spatial_count((mu, nu))
            records.append((f"gamma5 gamma^{mu} d{nu}", g5 @ gamma_mu(mu), (nu,), total))

    for mu in INDEX_RANGE:
        for nu in INDEX_RANGE:
            if mu == nu:
                continue
            for rho in INDEX_RANGE:
                total = spatial_count((mu, nu, rho))
                records.append((f"sigma^{mu}{nu} d{rho}", sigma_munu(mu, nu), (rho,), total))

    return records


def part0_source_firewall() -> None:
    section("PART 0: SOURCE FIREWALL")
    note = NOTE_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    required_note_phrases = [
        "formal sign rescope",
        "bounded-support - formal parity sign algebra",
        "This row does not claim a lattice-action Lorentz-violation no-go",
        "actual lattice derivative representatives",
        "This row does not depend on a CPT theorem",
        "This row does not add a new axiom",
        RUNNER_PATH,
    ]
    for phrase in required_note_phrases:
        check(f"source note contains boundary phrase: {phrase}", phrase in note)

    forbidden_note_phrases = [
        "epsilon " + "H_0 epsilon = -H_0",
        "CPT_" + "EXACT_NOTE.md",
        "staggered Cl(3)" + "/Z^3 framework",
        "lattice-action coefficient no-go",
        "P_inv * epsilon conjugates" + " the actual lattice derivative",
    ]
    for phrase in forbidden_note_phrases:
        check(f"source note excludes overbroad phrase: {phrase}", phrase not in note)

    forbidden_runner_phrases = [
        "staggered_" + "hopping",
        "CPT_" + "EXACT",
        "epsilon " + "H_0",
    ]
    for phrase in forbidden_runner_phrases:
        check(f"runner source excludes lattice-representative phrase: {phrase}", phrase not in source)


def part1_formal_sign_algebra() -> None:
    section("PART 1: EXHAUSTIVE FORMAL PARITY SIGN ALGEBRA")

    records = enumerate_structures()
    odd_count = 0
    even_count = 0
    max_sym_odd = 0.0
    max_asym_even = 0.0

    for label, gamma, deriv_indices, total in records:
        expected = -1 if total % 2 else 1
        actual = operator_p_weight(gamma, deriv_indices)
        check(f"{label}: P-weight = (-1)^{total}", actual == expected, f"actual={actual}, expected={expected}")

        p_image = parity_conjugate_gamma(gamma) * derivative_parity_sign(deriv_indices)
        sym = 0.5 * (gamma + p_image)
        asym = 0.5 * (gamma - p_image)
        if total % 2:
            odd_count += 1
            max_sym_odd = max(max_sym_odd, float(np.linalg.norm(sym)))
        else:
            even_count += 1
            max_asym_even = max(max_asym_even, float(np.linalg.norm(asym)))

    check("odd-N formal sector is nonempty", odd_count > 0, f"odd={odd_count}")
    check("even-N formal sector is nonempty", even_count > 0, f"even={even_count}")
    check("P-symmetric projection vanishes on odd-N sector", max_sym_odd < 1e-10, f"max={max_sym_odd:.2e}")
    check("P-antisymmetric projection vanishes on even-N sector", max_asym_even < 1e-10, f"max={max_asym_even:.2e}")
    check("exhaustive record count matches expected basis enumeration", len(records) == 144, f"records={len(records)}")


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
    check("formal sign row has no ledger dependencies", row.get("deps") == [], str(row.get("deps")))
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
    print("Parity dimension-5 formal sign repair")
    print(f"Claim: {CLAIM_ID}")
    print(f"Runner: {RUNNER_PATH}")

    part0_source_firewall()
    part1_formal_sign_algebra()
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
