"""Finite checks for the Z=det fermionic-statistics locator.

The runner verifies that supplied Grassmann/CAR variables realize a determinant
amplitude, while the tested finite hard-core/tensor-product routes do not
force that statistics choice. The 2026-06-07 repair additionally verifies that
the determinant side can be routed through existing audited one-hop supports
inside the abstract two-candidate Grassmann-vs-bosonic scope. It does not
derive physical FS from baseline axioms or introduce a new axiom/admission.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np

from flavor_occupancy_boundary_checks_2026_06_13 import run_occupancy_boundary_checks


PARITY_DEP = "fermion_parity_z2_grading_theorem_note_2026-05-02"
GRASSMANN_BRIDGE_DEP = "staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16"

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


def ledger_rows(root: Path) -> dict[str, dict[str, object]]:
    ledger_path = root / "docs" / "audit" / "data" / "audit_ledger.json"
    payload = json.loads(ledger_path.read_text())
    rows = payload["rows"]
    assert isinstance(rows, dict)
    return rows


def flat(text: str) -> str:
    return " ".join(text.split())


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
    rows = ledger_rows(root)
    parity_row = rows.get(PARITY_DEP, {})
    grassmann_row = rows.get(GRASSMANN_BRIDGE_DEP, {})
    passed.append(
        check(
            "one-hop dependency status: fermion parity Z2 grading is audited retained",
            parity_row.get("effective_status") == "retained",
            f"{PARITY_DEP} -> {parity_row.get('effective_status')}",
        )
    )
    passed.append(
        check(
            "one-hop dependency status: abstract Grassmann forcing bridge is audited retained or retained_bounded",
            grassmann_row.get("effective_status") in {"retained", "retained_bounded"},
            f"{GRASSMANN_BRIDGE_DEP} -> {grassmann_row.get('effective_status')}",
        )
    )

    parity = kron(S3, S3)
    c1_dag, c2_dag = c1.T, c2.T
    bilinear = c1_dag @ c2
    passed.append(
        check(
            "graded tensor route composes parity-odd generators into CAR with even bilinears",
            np.allclose(parity @ c1 @ parity, -c1)
            and np.allclose(parity @ c2 @ parity, -c2)
            and np.allclose(c1 @ c2 + c2 @ c1, 0.0)
            and np.allclose(parity @ bilinear - bilinear @ parity, 0.0),
            "F c_i F=-c_i, {c1,c2}=0, and c1^dag c2 is Z2-even",
        )
    )

    note = (root / "docs" / "FLAVOR_ZDET_FERMIONIC_STATISTICS_ADMISSION_2026-06-04.md").read_text()
    parity_note = (root / "docs" / "FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md").read_text()
    grassmann_note = (
        root / "docs" / "STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md"
    ).read_text()
    note_flat = flat(note)
    banned = [
        "owner-approved",
        "Tier-A admission",
        "The three baseline axioms do not force FS",
        "approved axioms and primitives",
        "assign a claim grade",
        "universal spin-statistics theorem",
        "promote those consumers",
    ]
    required = [
        "does not derive the physical-lattice choice of Grassmann/CAR variables",
        "does not introduce a new axiom or admission",
        "audited abstract Grassmann forcing bridge",
        "physical spin-statistics selector remains open",
        "No new axiom is introduced.",
    ]
    passed.append(
        check(
            "source boundary guard: finite bridge only, no physical baseline/admission conclusion promoted",
            all(term not in note_flat for term in banned) and all(term in note_flat for term in required),
            "the packet leaves the physical FS selector open",
        )
    )
    passed.append(
        check(
            "dependency boundary guard: consumed supports are algebraic, not physical spin-statistics selectors",
            "does not by itself prove a physical fermion-statistics selector" in parity_note
            and "U4 bridge remains open" in grassmann_note
            and "part of the abstract framing" in grassmann_note
            and "Grassmann generators in the cited upstream narrow theorem" in grassmann_note,
            "parity supplies Z2 grading; Grassmann bridge supplies abstract two-candidate determinant scope",
        )
    )
    passed.extend(run_occupancy_boundary_checks(root, check, "downstream occupancy atom"))

    pass_count = sum(passed)
    fail_count = len(passed) - pass_count
    print(f"\nSCORECARD PASS={pass_count} FAIL={fail_count}")
    print("FINDING: the abstract two-candidate determinant side now has one-hop audited support.")
    print("The physical-lattice cross-site CAR/Grassmann selector remains open.")
    print("The tested finite hard-core/tensor-product routes still do not force that statistics choice.")
    print("Koide generation chirality remains a separate internal-factor residual.")
    print("DOWNSTREAM: determinant statistics does not select the Koide occupancy/slot-degree atom.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
