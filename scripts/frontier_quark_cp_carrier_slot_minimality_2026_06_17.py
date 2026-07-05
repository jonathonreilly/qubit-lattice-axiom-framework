#!/usr/bin/env python3
"""Exact carrier-slot minimality check for the quark CP completion lane.

This runner does not fit quark masses, CKM magnitudes, or J.  It checks the
structural phase-gauge algebra behind the parent completion note's chosen
complex 1-3 carrier:

* phases on the fixed Schur-NNI tree edges are removable by diagonal rephasing;
* adding one Hermitian off-tree edge to the three-generation tree has only one
  possible slot, the 1-3 closing edge;
* the 1-3 phase is the unique cycle invariant after the tree is gauge-fixed;
* Hermitian off-diagonal carriers are determinant-phase neutral: the determinant
  is real, so no continuous strong-CP phase is introduced by the slot itself.

The result is exact support for the carrier slot under the fixed-tree/Hermitian
one-edge-extension boundary.  It does not derive xi_u, xi_d, comparator targets,
or a small-correction interpretation.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


PASS_COUNT = 0
FAIL_COUNT = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "QUARK_CP_CARRIER_SLOT_MINIMALITY_THEOREM_NOTE_2026-06-17.md"
PARENT = ROOT / "docs" / "QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md"


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"  [{status}] {label}{suffix}")
    return bool(ok)


def wrap(angle: float) -> float:
    return (angle + math.pi) % (2.0 * math.pi) - math.pi


def incidence_matrix(edges: list[tuple[int, int]], n_vertices: int = 3) -> np.ndarray:
    mat = np.zeros((len(edges), n_vertices), dtype=float)
    for row, (i, j) in enumerate(edges):
        mat[row, i] = -1.0
        mat[row, j] = 1.0
    return mat


def invariant_dimension(edges: list[tuple[int, int]]) -> int:
    mat = incidence_matrix(edges)
    rank = np.linalg.matrix_rank(mat, tol=1e-12)
    return len(edges) - int(rank)


def rephase(phases: dict[tuple[int, int], float], theta: np.ndarray) -> dict[tuple[int, int], float]:
    return {
        edge: wrap(phi - theta[edge[0]] + theta[edge[1]])
        for edge, phi in phases.items()
    }


def gauge_fix_tree(phases: dict[tuple[int, int], float]) -> tuple[np.ndarray, dict[tuple[int, int], float]]:
    # Set theta_0 = 0 and make the 1-2 and 2-3 tree edges real.
    theta = np.zeros(3, dtype=float)
    theta[1] = theta[0] - phases[(0, 1)]
    theta[2] = theta[1] - phases[(1, 2)]
    return theta, rephase(phases, theta)


def cycle_phase(phases: dict[tuple[int, int], float]) -> float:
    # Phase of M_12 M_23 M_31 for Hermitian M, with stored phases on M_ij, i<j.
    return wrap(phases[(0, 1)] + phases[(1, 2)] - phases[(0, 2)])


def hermitian_matrix(
    diag: tuple[float, float, float],
    magnitudes: dict[tuple[int, int], float],
    phases: dict[tuple[int, int], float],
) -> np.ndarray:
    mat = np.diag(np.asarray(diag, dtype=float)).astype(complex)
    for (i, j), mag in magnitudes.items():
        z = mag * np.exp(1j * phases[(i, j)])
        mat[i, j] = z
        mat[j, i] = np.conj(z)
    return mat


def closed_form_det(
    diag: tuple[float, float, float],
    magnitudes: dict[tuple[int, int], float],
    phases: dict[tuple[int, int], float],
) -> float:
    a, b, c = diag
    x = magnitudes[(0, 1)]
    y = magnitudes[(1, 2)]
    z = magnitudes[(0, 2)]
    return (
        a * b * c
        - a * y * y
        - b * z * z
        - c * x * x
        + 2.0 * x * y * z * math.cos(cycle_phase(phases))
    )


def main() -> int:
    print("Quark CP carrier slot minimality verifier")
    print("=" * 78)

    tree_edges = [(0, 1), (1, 2)]
    triangle_edges = [(0, 1), (1, 2), (0, 2)]
    all_possible_edges = {(0, 1), (1, 2), (0, 2)}

    print("\nPart A: phase-gauge rank")
    tree_rank = np.linalg.matrix_rank(incidence_matrix(tree_edges), tol=1e-12)
    tri_rank = np.linalg.matrix_rank(incidence_matrix(triangle_edges), tol=1e-12)
    check("fixed Schur-NNI tree has no phase invariant", invariant_dimension(tree_edges) == 0)
    check("three-edge Hermitian support has one cycle invariant", invariant_dimension(triangle_edges) == 1)
    check("both connected supports have vertex-rephasing rank two", tree_rank == 2 and tri_rank == 2)

    print("\nPart B: unique one-edge completion of the fixed tree")
    missing_edges = sorted(all_possible_edges - set(tree_edges))
    check("the only off-tree edge on three generations is 1-3", missing_edges == [(0, 2)])
    check(
        "a one-edge Hermitian extension of the fixed tree is therefore the 1-3 carrier slot",
        set(tree_edges + missing_edges) == set(triangle_edges),
    )

    print("\nPart C: gauge fixing and cycle phase")
    rng = np.random.default_rng(20260617)
    for idx in range(6):
        phases = {
            (0, 1): float(rng.uniform(-math.pi, math.pi)),
            (1, 2): float(rng.uniform(-math.pi, math.pi)),
            (0, 2): float(rng.uniform(-math.pi, math.pi)),
        }
        theta, fixed = gauge_fix_tree(phases)
        transformed = rephase(phases, theta)
        inv0 = cycle_phase(phases)
        inv1 = cycle_phase(transformed)
        check(
            f"sample {idx + 1}: tree phases gauge-fix to zero",
            abs(fixed[(0, 1)]) < 1e-12 and abs(fixed[(1, 2)]) < 1e-12,
        )
        check(
            f"sample {idx + 1}: cycle phase is rephasing invariant",
            abs(wrap(inv0 - inv1)) < 1e-12,
        )
        check(
            f"sample {idx + 1}: residual 1-3 phase equals the negative cycle phase",
            abs(wrap(fixed[(0, 2)] + inv0)) < 1e-12,
        )

    print("\nPart D: determinant-phase neutrality")
    diag = (1.0e-5, 7.4e-3, 1.0)
    magnitudes = {
        (0, 1): 1.48 * math.sqrt(diag[0] * diag[1]),
        (1, 2): 0.65 * math.sqrt(diag[1] * diag[2]),
        (0, 2): 0.12 * math.sqrt(diag[0] * diag[2]),
    }
    det_imag_ok = True
    det_formula_ok = True
    phase_sensitive = False
    det_values: list[float] = []
    for phi in np.linspace(-math.pi, math.pi, 17):
        phases = {(0, 1): 0.0, (1, 2): 0.0, (0, 2): float(phi)}
        mat = hermitian_matrix(diag, magnitudes, phases)
        det_np = np.linalg.det(mat)
        det_cf = closed_form_det(diag, magnitudes, phases)
        det_values.append(float(np.real(det_np)))
        det_imag_ok = det_imag_ok and abs(float(np.imag(det_np))) < 1e-18
        det_formula_ok = det_formula_ok and abs(float(np.real(det_np)) - det_cf) < 1e-18
    phase_sensitive = max(det_values) - min(det_values) > 1e-9
    check("Hermitian 1-3 carrier leaves determinant phase real", det_imag_ok)
    check("determinant equals the real closed-form cycle-cosine expression", det_formula_ok)
    check("the 1-3 phase is physically visible through the cycle cosine", phase_sensitive)

    print("\nPart E: source boundary checks")
    note_text = NOTE.read_text(encoding="utf-8")
    parent_text = PARENT.read_text(encoding="utf-8")
    check(
        "new note states the fixed-tree/Hermitian one-edge boundary",
        "fixed Schur-NNI tree" in note_text
        and "Hermitian one-edge extension" in note_text
        and "does not derive `xi_u` or `xi_d`" in note_text,
    )
    check(
        "parent note points to the exact-support slot-minimality companion",
        "QUARK_CP_CARRIER_SLOT_MINIMALITY_THEOREM_NOTE_2026-06-17.md" in parent_text
        and "fitted numerical values remain open" in parent_text,
    )
    check(
        "no retained-status overclaim in the new note",
        "Status:** exact support" in note_text
        and "not an audit verdict" in note_text
        and "retained theorem" not in note_text,
    )

    print("\nSummary")
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
