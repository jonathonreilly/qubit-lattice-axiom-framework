#!/usr/bin/env python3
"""No-go certificate for the SU(3) L_s=2 uniform-pairing shortcut."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
from scipy.special import iv

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/SU3_CUBE_INDEX_GRAPH_SHORTCUT_OPEN_GATE_NOTE_2026-05-03.md"
LEDGER = REPO_ROOT / "docs/audit/data/audit_ledger.json"
QUEUE = REPO_ROOT / "docs/audit/data/audit_queue.json"

CLAIM_ID = "su3_cube_index_graph_shortcut_open_gate_note_2026-05-03"
RUNNER_PATH = "scripts/frontier_su3_cube_index_graph_shortcut_open_gate.py"

BETA = 6.0
EPSILON_WITNESS = 3.03e-4
BRIDGE_SUPPORT_TARGET = 0.5935306800
EXPECTED_P_CANDIDATE = 0.4291049969

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", kind: str = "A") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] [{kind}] {name}{suffix}")


def note_boundary_checks() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").split())
    required = [
        "Claim type:** no_go",
        "Status:** bounded no-go",
        "uniform-pairing shortcut route",
        "P_candidate(6) = 0.4291049969",
        "which is more than five hundred times the witness scale",
        "does not claim",
        "any new axiom or audit verdict",
    ]
    for phrase in required:
        check(f"note boundary contains: {phrase}", phrase in text)

    forbidden = [
        "Status:** open gate, unaudited",
        "Primary runner:",
        "parent theorem promotion",
        "verdict_rationale_template",
        "intrinsic_status:",
    ]
    for phrase in forbidden:
        check(f"note omits stale audit/open-gate phrase: {phrase}", phrase not in text)


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def wilson_character_coefficient(p: int, q: int, mode_max: int, arg: float) -> float:
    """SU(3) Wilson character coefficient c_(p,q)(beta) by Bessel determinant."""
    lam = [p + q, q, 0]
    total = 0.0
    for mode in range(-mode_max, mode_max + 1):
        mat = np.array(
            [[iv(mode + lam[j] + i - j, arg) for j in range(3)] for i in range(3)],
            dtype=float,
        )
        total += float(np.linalg.det(mat))
    return total


def all_plaquettes_with_links() -> List[Tuple[Tuple[int, int, int], int, int, List[Tuple[int, int, int, int]]]]:
    """Enumerate the 12 L_s=2 PBC plaquettes with forward directed links."""
    plaquettes = []
    for plane_dir1, plane_dir2 in [(0, 1), (0, 2), (1, 2)]:
        orth = ({0, 1, 2} - {plane_dir1, plane_dir2}).pop()
        for orth_val in range(2):
            for start_in_plane_idx in range(2):
                site = [0, 0, 0]
                site[plane_dir1] = start_in_plane_idx
                site[plane_dir2] = 0
                site[orth] = orth_val
                cur = list(site)
                links = []
                for direction in [plane_dir1, plane_dir2, plane_dir1, plane_dir2]:
                    links.append((cur[0], cur[1], cur[2], direction))
                    cur[direction] = (cur[direction] + 1) % 2
                plaquettes.append((tuple(site), plane_dir1, plane_dir2, links))

    seen = set()
    unique = []
    for plaquette in plaquettes:
        link_set = frozenset(plaquette[3])
        if link_set not in seen:
            seen.add(link_set)
            unique.append(plaquette)
    return unique


def link_to_plaquette_slots(plaquettes: List[Tuple]) -> Dict[Tuple[int, int, int, int], List[Tuple[int, int]]]:
    out: Dict[Tuple[int, int, int, int], List[Tuple[int, int]]] = {}
    for p_idx, (_, _, _, links) in enumerate(plaquettes):
        for slot, link in enumerate(links):
            out.setdefault(link, []).append((p_idx, slot))
    return out


def build_index_graph(plaquettes: List[Tuple]) -> Tuple[int, List[Tuple[int, int]]]:
    """Build cyclic-index identifications induced by shared links."""
    n_nodes = 4 * len(plaquettes)
    edges: List[Tuple[int, int]] = []
    for occurrences in link_to_plaquette_slots(plaquettes).values():
        if len(occurrences) != 2:
            continue
        (p_a, slot_a), (p_b, slot_b) = occurrences
        in_a = 4 * p_a + (slot_a - 1) % 4
        out_a = 4 * p_a + slot_a
        in_b = 4 * p_b + (slot_b - 1) % 4
        out_b = 4 * p_b + slot_b
        edges.append((in_a, in_b))
        edges.append((out_a, out_b))
    return n_nodes, edges


def count_connected_components(n_nodes: int, edges: List[Tuple[int, int]]) -> int:
    parent = list(range(n_nodes))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for a, b in edges:
        union(a, b)
    return len({find(i) for i in range(n_nodes)})


def candidate_rho(beta: float, nmax: int, n_components: int, mode_max: int = 200) -> Dict[Tuple[int, int], float]:
    """Candidate rho under the unproved uniform-pairing trace ansatz."""
    arg = beta / 3.0
    c00 = wilson_character_coefficient(0, 0, mode_max, arg)
    rho: Dict[Tuple[int, int], float] = {}
    for p in range(nmax + 1):
        for q in range(nmax + 1):
            dim = dim_su3(p, q)
            coeff = wilson_character_coefficient(p, q, mode_max, arg)
            topological_factor = float(dim ** (n_components - 24))
            rho[(p, q)] = ((dim * coeff / c00) ** 12) * topological_factor
    norm = rho[(0, 0)]
    return {key: value / norm for key, value in rho.items()}


def dominant_weights_box(nmax: int) -> List[Tuple[int, int]]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def recurrence_neighbors(p: int, q: int) -> List[Tuple[int, int]]:
    out = []
    for a, b in [(p + 1, q), (p - 1, q + 1), (p, q - 1), (p, q + 1), (p + 1, q - 1), (p - 1, q)]:
        if a >= 0 and b >= 0:
            out.append((a, b))
    return out


def build_j(nmax: int) -> Tuple[np.ndarray, List[Tuple[int, int]], Dict[Tuple[int, int], int]]:
    weights = dominant_weights_box(nmax)
    index = {weight: i for i, weight in enumerate(weights)}
    j_op = np.zeros((len(weights), len(weights)), dtype=float)
    for p, q in weights:
        source = index[(p, q)]
        for neighbor in recurrence_neighbors(p, q):
            if neighbor in index:
                j_op[index[neighbor], source] += 1.0 / 6.0
    return j_op, weights, index


def build_local_factor(weights: List[Tuple[int, int]], index: Dict[Tuple[int, int], int], mode_max: int, beta: float) -> np.ndarray:
    arg = beta / 3.0
    coeffs = np.array([wilson_character_coefficient(p, q, mode_max, arg) for p, q in weights], dtype=float)
    dims = np.array([dim_su3(p, q) for p, q in weights], dtype=float)
    c00 = coeffs[index[(0, 0)]]
    a_link = coeffs / (dims * c00)
    return np.diag(a_link ** 4)


def matrix_exp_symmetric(matrix: np.ndarray, tau: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(matrix)
    return (vecs * np.exp(tau * vals)) @ vecs.T


def candidate_perron_value(rho: Dict[Tuple[int, int], float], nmax: int = 7, mode_max: int = 200) -> Tuple[float, float]:
    j_op, weights, index = build_j(nmax)
    multiplier = matrix_exp_symmetric(j_op, 3.0)
    d_loc = build_local_factor(weights, index, mode_max, BETA)
    c_env = np.diag(np.array([rho.get(weight, 0.0) for weight in weights], dtype=float))
    transfer = multiplier @ d_loc @ c_env @ multiplier
    vals, vecs = np.linalg.eigh(transfer)
    idx = int(np.argmax(vals))
    psi = vecs[:, idx]
    if np.sum(psi) < 0.0:
        psi = -psi
    return float(psi @ (j_op @ psi)), float(vals[idx])


def shortcut_checks() -> None:
    print("\n=== finite shortcut graph ===")
    plaquettes = all_plaquettes_with_links()
    n_nodes, edges = build_index_graph(plaquettes)
    n_components = count_connected_components(n_nodes, edges)
    exponent = n_components - 24
    check("12 unique L_s=2 PBC plaquettes", len(plaquettes) == 12, str(len(plaquettes)))
    check("48 cyclic index nodes", n_nodes == 48, str(n_nodes))
    check("48 link-induced identifications", len(edges) == 48, str(len(edges)))
    check("8 connected components", n_components == 8, str(n_components))
    check("uniform-pairing exponent is -16", exponent == -16, str(exponent))

    print("\n=== candidate rho and Perron comparison ===")
    rho = candidate_rho(BETA, 4, n_components)
    check("rho(0,0) normalized to one", math.isclose(rho[(0, 0)], 1.0, rel_tol=0.0, abs_tol=1e-12), f"{rho[(0, 0)]:.12f}")
    check("rho(1,0) equals rho(0,1)", math.isclose(rho[(1, 0)], rho[(0, 1)], rel_tol=1e-12, abs_tol=1e-12), f"{rho[(1, 0)]:.6e}/{rho[(0, 1)]:.6e}")
    check("rho(1,0) matches cached candidate", abs(rho[(1, 0)] - 2.124624e-01) < 5e-8, f"{rho[(1, 0)]:.6e}")
    check("rho(1,1) matches cached candidate", abs(rho[(1, 1)] - 5.587932e-03) < 5e-9, f"{rho[(1, 1)]:.6e}")

    p_candidate, eig_candidate = candidate_perron_value(rho)
    gap = abs(BRIDGE_SUPPORT_TARGET - p_candidate)
    ratio = gap / EPSILON_WITNESS
    check("candidate Perron value matches expected", abs(p_candidate - EXPECTED_P_CANDIDATE) < 5e-10, f"{p_candidate:.10f}")
    check("candidate Perron value is normalized finite", 0.0 < p_candidate < 1.0, f"{p_candidate:.10f}")
    check("candidate misses target by witness-scale margin", ratio > 500.0, f"gap={gap:.10f}, gap/eps={ratio:.1f}", kind="B")
    check("uniform-pairing shortcut cannot close target", p_candidate + EPSILON_WITNESS < BRIDGE_SUPPORT_TARGET, f"{p_candidate:.10f} < {BRIDGE_SUPPORT_TARGET:.10f}", kind="B")
    print(f"  Perron eigenvalue: {eig_candidate:.10f}")


def audit_metadata_checks() -> None:
    if not LEDGER.exists() or not QUEUE.exists():
        print("\n=== audit metadata unavailable before pipeline ===")
        return
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    row = ledger["rows"][CLAIM_ID]
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))["queue"]
    queue_entry = next(e for e in queue if e["claim_id"] == CLAIM_ID)

    print("\n=== regenerated audit metadata ===")
    check("ledger claim_type is no_go", row.get("claim_type") == "no_go")
    check("ledger audit_status reset to unaudited", row.get("audit_status") == "unaudited")
    check("ledger effective_status reset to unaudited", row.get("effective_status") == "unaudited")
    check("ledger runner_path registered", row.get("runner_path") == RUNNER_PATH, str(row.get("runner_path")))
    check("ledger has no direct deps", row.get("deps") == [], str(row.get("deps")))
    check("no open dependency paths remain", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))
    check("queue marks row ready", queue_entry.get("ready") is True, str(queue_entry.get("ready")))
    check("descendant chain remains material", int(row.get("transitive_descendants") or 0) >= 100, str(row.get("transitive_descendants")), kind="B")


def main() -> int:
    note_boundary_checks()
    shortcut_checks()
    audit_metadata_checks()
    print("\nSU(3) cube uniform-pairing shortcut no-go certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
