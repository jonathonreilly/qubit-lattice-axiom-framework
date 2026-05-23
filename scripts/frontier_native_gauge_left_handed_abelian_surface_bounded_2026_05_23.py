#!/usr/bin/env python3
"""Bounded left-handed abelian surface runner.

This runner preserves the selected-axis +1/3 / -1 eigenvalue calculation
outside the nonabelian native gauge closure claim. It intentionally does not
claim anomaly-complete U(1)_Y, electroweak matching, matter labels, electric
charge, or downstream phenomenology.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
TOL = 1.0e-10
RETAINED_GRADES = {"retained", "retained_bounded", "retained_no_go"}

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    msg = f"  [{status}] {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return condition


def close(a: np.ndarray, b: np.ndarray, tol: float = TOL) -> bool:
    return np.linalg.norm(a - b) < tol


def cube_basis() -> list[tuple[int, int, int]]:
    return [(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)]


def cube_index() -> dict[tuple[int, int, int], int]:
    return {bits: i for i, bits in enumerate(cube_basis())}


def residual_swap(axis: int) -> np.ndarray:
    idx = cube_index()
    others = [i for i in range(3) if i != axis]
    a, b = others
    op = np.zeros((8, 8), dtype=complex)
    for bits, i in idx.items():
        swapped = list(bits)
        swapped[a], swapped[b] = swapped[b], swapped[a]
        op[idx[tuple(swapped)], i] = 1.0
    return op


def verify_dependency_surface() -> None:
    print("\nGRAPH-FIRST SELECTED-AXIS DEPENDENCY SURFACE")
    with LEDGER_PATH.open("r", encoding="utf-8") as handle:
        rows = json.load(handle)["rows"]

    required = {
        "graph_first_selector_derivation_note": (
            "positive_theorem",
            "scripts/frontier_graph_first_selector_derivation.py",
        ),
        "graph_first_su3_integration_note": (
            "positive_theorem",
            "scripts/frontier_graph_first_su3_integration.py",
        ),
    }
    for claim_id, (claim_type, runner_path) in required.items():
        row = rows[claim_id]
        check(
            f"{claim_id} claim_type is {claim_type}",
            row.get("claim_type") == claim_type,
            str(row.get("claim_type")),
        )
        check(
            f"{claim_id} audit_status is audited_clean",
            row.get("audit_status") == "audited_clean",
            str(row.get("audit_status")),
        )
        check(
            f"{claim_id} effective_status is retained-grade",
            row.get("effective_status") in RETAINED_GRADES,
            str(row.get("effective_status")),
        )
        check(
            f"{claim_id} runner path registered",
            row.get("runner_path") == runner_path,
            str(row.get("runner_path")),
        )
        check(f"{claim_id} runner exists", (REPO_ROOT / runner_path).exists())


def verify_bounded_abelian_surface() -> None:
    print("\nBOUNDED LEFT-HANDED ABELIAN EIGENVALUE SURFACE")
    i8 = np.eye(8, dtype=complex)

    for axis in range(3):
        tau = residual_swap(axis)
        pi_plus = (i8 + tau) / 2.0
        pi_minus = (i8 - tau) / 2.0
        y_like = (1.0 / 3.0) * pi_plus - pi_minus
        eigs = np.linalg.eigvalsh(y_like.real)

        print(f"\nSelected axis {axis + 1}")
        check("tau^2 = I", close(tau @ tau, i8))
        check("Pi_+ is a projector", close(pi_plus @ pi_plus, pi_plus))
        check("Pi_- is a projector", close(pi_minus @ pi_minus, pi_minus))
        check("Pi_+ Pi_- = 0", close(pi_plus @ pi_minus, np.zeros((8, 8), dtype=complex)))
        check("rank Pi_+ = 6", np.linalg.matrix_rank(pi_plus, tol=TOL) == 6)
        check("rank Pi_- = 2", np.linalg.matrix_rank(pi_minus, tol=TOL) == 2)
        check("Y_like is Hermitian", close(y_like, y_like.conj().T))
        check("Tr Y_like = 0", abs(np.trace(y_like)) < TOL)
        check(
            "Y_like eigenvalue +1/3 has multiplicity 6",
            int(np.sum(np.abs(eigs - 1.0 / 3.0) < 1e-8)) == 6,
        )
        check(
            "Y_like eigenvalue -1 has multiplicity 2",
            int(np.sum(np.abs(eigs + 1.0) < 1e-8)) == 2,
        )


def main() -> int:
    print("=" * 76)
    print("NATIVE GAUGE LEFT-HANDED ABELIAN SURFACE BOUNDED RUNNER")
    print("=" * 76)
    print("Excluded: anomaly-complete U(1)_Y, EW matching, matter labels,")
    print("          electric charge, and downstream phenomenology.")

    verify_dependency_surface()
    verify_bounded_abelian_surface()

    print("\nSUMMARY")
    if FAIL_COUNT:
        print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
        return 1
    print(f"PASS={PASS_COUNT} FAIL=0")
    print("FINAL_TAG: NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
