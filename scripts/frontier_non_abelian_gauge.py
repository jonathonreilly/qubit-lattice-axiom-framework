#!/usr/bin/env python3
"""Audit-grade nonabelian native gauge closure runner.

Authority boundary:
  - prove the native cubic Cl(3) / SU(2) algebra directly;
  - verify cubic parity/chiral anticommutation directly;
  - verify that the graph-first selector and SU(3) integration rows are
    audit-ratified positive-theorem retained dependencies.

This runner intentionally excludes the left-handed abelian eigenvalue
surface, anomaly-complete U(1)_Y, electroweak matching, matter labels,
Wilson dynamics, and downstream phenomenology. The bounded abelian surface
is checked by its own split runner.
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


def commutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def anticommutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b + b @ a


def close(a: np.ndarray, b: np.ndarray, tol: float = TOL) -> bool:
    return np.linalg.norm(a - b) < tol


def kron3(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return np.kron(a, np.kron(b, c))


I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
I8 = np.eye(8, dtype=complex)


def clifford_generators() -> list[np.ndarray]:
    return [
        kron3(SX, I2, I2),
        kron3(SY, SX, I2),
        kron3(SY, SY, SX),
    ]


def verify_native_clifford_su2() -> None:
    print("\nNATIVE CUBIC Cl(3) / SU(2)")
    gammas = clifford_generators()

    for index, gamma in enumerate(gammas, start=1):
        check(f"Gamma_{index} is Hermitian", close(gamma, gamma.conj().T))
        check(f"Gamma_{index}^2 = I_8", close(gamma @ gamma, I8))

    zero = np.zeros((8, 8), dtype=complex)
    for i in range(3):
        for j in range(i, 3):
            expected = 2.0 * I8 if i == j else zero
            err = np.linalg.norm(anticommutator(gammas[i], gammas[j]) - expected)
            check(
                f"{{Gamma_{i + 1}, Gamma_{j + 1}}} = 2 delta_ij I_8",
                err < TOL,
                f"err={err:.2e}",
            )

    s1 = -0.5j * gammas[1] @ gammas[2]
    s2 = -0.5j * gammas[2] @ gammas[0]
    s3 = -0.5j * gammas[0] @ gammas[1]

    for index, s in enumerate((s1, s2, s3), start=1):
        check(f"S_{index} is Hermitian", close(s, s.conj().T))

    check("[S_1, S_2] = i S_3", close(commutator(s1, s2), 1j * s3))
    check("[S_2, S_3] = i S_1", close(commutator(s2, s3), 1j * s1))
    check("[S_3, S_1] = i S_2", close(commutator(s3, s1), 1j * s2))

    casimir = s1 @ s1 + s2 @ s2 + s3 @ s3
    err = np.linalg.norm(casimir - 0.75 * I8)
    check("S_1^2 + S_2^2 + S_3^2 = (3/4) I_8", err < TOL, f"err={err:.2e}")


def site_index(side: int, x: int, y: int, z: int) -> int:
    return x * side * side + y * side + z


def verify_cubic_chiral_parity(side: int = 4) -> None:
    print("\nCUBIC PARITY / CHIRAL CHECK")
    n = side**3
    hop = np.zeros((n, n), dtype=complex)
    parity = np.zeros(n, dtype=float)

    for x in range(side):
        for y in range(side):
            for z in range(side):
                i = site_index(side, x, y, z)
                parity[i] = 1.0 if (x + y + z) % 2 == 0 else -1.0

                if x + 1 < side:
                    j = site_index(side, x + 1, y, z)
                    hop[i, j] = 1.0
                    hop[j, i] = 1.0
                if y + 1 < side:
                    j = site_index(side, x, y + 1, z)
                    eta_y = -1.0 if x % 2 else 1.0
                    hop[i, j] = eta_y
                    hop[j, i] = eta_y
                if z + 1 < side:
                    j = site_index(side, x, y, z + 1)
                    eta_z = -1.0 if (x + y) % 2 else 1.0
                    hop[i, j] = eta_z
                    hop[j, i] = eta_z

    p = np.diag(parity)
    check("P^2 = I on finite open cubic block", close(p @ p, np.eye(n)))
    err = np.linalg.norm(hop @ p + p @ hop)
    check("H_hop P + P H_hop = 0", err < TOL, f"err={err:.2e}")


def verify_retained_graph_first_dependencies() -> None:
    print("\nRETAINED GRAPH-FIRST NONABELIAN DEPENDENCIES")
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


def main() -> int:
    print("=" * 76)
    print("NATIVE GRAPH-FIRST NONABELIAN GAUGE CLOSURE")
    print("=" * 76)
    print("Excluded: abelian eigenvalue surface, U(1)_Y, EW matching, matter labels,")
    print("          Wilson dynamics, and downstream phenomenology.")

    verify_native_clifford_su2()
    verify_cubic_chiral_parity()
    verify_retained_graph_first_dependencies()

    print("\nSUMMARY")
    print("  Exact native cubic Cl(3) / SU(2): checked directly.")
    print("  Graph-first selector and structural SU(3): checked as retained dependencies.")
    print("  Abelian factor: excluded from this runner and source boundary.")

    if FAIL_COUNT:
        print(f"\nPASS={PASS_COUNT} FAIL={FAIL_COUNT}")
        return 1
    print(f"\nPASS={PASS_COUNT} FAIL=0")
    print("FINAL_TAG: NATIVE_GRAPH_FIRST_NONABELIAN_GAUGE_CLOSURE_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
