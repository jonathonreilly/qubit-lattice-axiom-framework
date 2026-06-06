"""Finite checks for the Z=det fermionic-statistics locator.

The runner verifies that supplied Grassmann/CAR variables realize a determinant
amplitude, while the tested finite hard-core/tensor-product routes do not force
that statistics choice. It does not derive FS from baseline axioms or introduce
a new axiom/admission.
"""

from __future__ import annotations

import itertools
from pathlib import Path

import numpy as np


SP = np.array([[0.0, 1.0], [0.0, 0.0]])
S3 = np.array([[1.0, 0.0], [0.0, -1.0]])
I2 = np.eye(2)


def kron(*ops: np.ndarray) -> np.ndarray:
    out = np.array([[1.0]])
    for op in ops:
        out = np.kron(out, op)
    return out


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = 0
    for i, left in enumerate(perm):
        for right in perm[i + 1 :]:
            if left > right:
                inversions += 1
    return -1 if inversions % 2 else 1


def berezin_det(matrix: np.ndarray) -> float:
    """Signed permutation sum for the finite Berezin determinant identity."""
    n = matrix.shape[0]
    total = 0.0
    for perm in itertools.permutations(range(n)):
        total += permutation_sign(perm) * np.prod([matrix[i, perm[i]] for i in range(n)])
    return float(total)


def permanent(matrix: np.ndarray) -> float:
    n = matrix.shape[0]
    total = 0.0
    for perm in itertools.permutations(range(n)):
        total += np.prod([matrix[i, perm[i]] for i in range(n)])
    return float(total)


def main() -> int:
    passed: list[bool] = []

    matrix = np.array(
        [
            [2.0, 0.7, 0.1],
            [0.3, 1.5, 0.4],
            [0.2, 0.1, 1.8],
        ]
    )
    det_value = float(np.linalg.det(matrix))
    perm_value = permanent(matrix)

    passed.append(
        check(
            "Berezin finite Gaussian gives det(M) once Grassmann variables are supplied",
            abs(berezin_det(matrix) - det_value) < 1e-9,
            f"berezin={berezin_det(matrix):.6f}; det={det_value:.6f}",
        )
    )

    a1, a2 = kron(SP, I2), kron(I2, SP)
    passed.append(
        check(
            "ordinary cross-site qubit ladders commute",
            np.allclose(a1 @ a2 - a2 @ a1, 0.0),
        )
    )

    c1, c2 = kron(SP, I2), kron(S3, SP)
    passed.append(
        check(
            "Jordan-Wigner dressing realizes cross-site CAR as a generator change",
            np.allclose(c1 @ c2 + c2 @ c1, 0.0),
        )
    )

    passed.append(
        check(
            "local dimension two is shared by fermions and hard-core bosons",
            np.allclose(SP @ SP, 0.0) and np.allclose(a1 @ a2 - a2 @ a1, 0.0),
        )
    )

    passed.append(
        check(
            "signed determinant and unsigned permanent are distinct statistics choices",
            abs(det_value - perm_value) > 1e-6,
            f"det={det_value:.6f}; permanent={perm_value:.6f}",
        )
    )

    j_matrix = np.ones((3, 3))
    gamma_chi = (2.0 / 3.0) * j_matrix - np.eye(3)
    c3_shift = np.array(
        [
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ]
    )
    c3_equivariant_mass = 1.3 * np.eye(3) + 0.6 * c3_shift + 0.6 * c3_shift.T
    passed.append(
        check(
            "Gamma_chi is an internal-generation object distinct from spatial CAR",
            np.allclose(sorted(np.linalg.eigvalsh(gamma_chi)), [-1.0, -1.0, 1.0])
            and np.allclose(gamma_chi @ c3_equivariant_mass - c3_equivariant_mass @ gamma_chi, 0.0),
            "Gamma_chi commutes with the tested C3-equivariant mass operator",
        )
    )

    root = Path(__file__).resolve().parents[1]
    note = (root / "docs" / "FLAVOR_ZDET_FERMIONIC_STATISTICS_ADMISSION_2026-06-04.md").read_text()
    banned = [
        "owner-approved",
        "Tier-A admission",
        "The three baseline axioms do not force FS",
        "approved axioms and primitives",
        "assign a claim grade",
    ]
    required = [
        "does not derive the choice of Grassmann/CAR variables",
        "does not introduce a new axiom or admission",
        "No new axiom is introduced.",
    ]
    passed.append(
        check(
            "source boundary guard: finite locator only, no baseline/admission conclusion promoted",
            all(term not in note for term in banned) and all(term in note for term in required),
            "the packet leaves FS selection open",
        )
    )

    pass_count = sum(passed)
    fail_count = len(passed) - pass_count
    print(f"\nSCORECARD PASS={pass_count} FAIL={fail_count}")
    print("FINDING: supplied Grassmann/CAR variables realize the determinant amplitude.")
    print("The tested finite hard-core/tensor-product routes do not force that statistics choice.")
    print("Koide generation chirality remains a separate internal-factor residual.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
