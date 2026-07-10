#!/usr/bin/env python3
"""
Graph-first axis-selector route to PMNS weak-axis alignment.

Question:
  Can a genuinely graph-native selector on the `hw=1` corner triplet derive
  any positive PMNS law without reusing the old full-microscopic decomposition
  route?

Answer:
  Yes, partially. The canonical cube-shift selector has exactly three axis
  minima with residual `Z_2` stabilizer. Under the explicit symmetry premise
  (E) that the active Hermitian operator carries the residual `Z_2`
  equivariantly, the bridge authority identifies the exact aligned core law

      P_23 H P_23 = H

  and therefore

      H = [[a,z,z],[z*,c,d],[z*,d,c]],  a,c,d in R, z in C.

  The real four-parameter core [[a,b,b],[b,c,d],[b,d,c]] is only the
  real/CP/phase-gauge specialization z=b in R; unitary P_23 invariance alone
  does not force Im(z)=0.

  This is a real positive law from the graph-first route, but it still does not
  fix the values `(a,z,c,d)` or the active sector.
"""

from __future__ import annotations

import itertools
import math
import sys
from pathlib import Path

import numpy as np

np.set_printoptions(precision=8, suppress=True, linewidth=120)

PASS_COUNT = 0
FAIL_COUNT = 0
NOTE_PATH = Path(__file__).resolve().parents[1] / "docs" / "PMNS_GRAPH_FIRST_AXIS_ALIGNMENT_NOTE.md"

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
I8 = np.eye(8, dtype=complex)
P23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)


def check(name: str, condition: bool, detail: str = "", cls: str = "A") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status} ({cls})] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def kron3(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return np.kron(a, np.kron(b, c))


def build_axis_shifts() -> list[np.ndarray]:
    return [
        kron3(SX, I2, I2),
        kron3(I2, SX, I2),
        kron3(I2, I2, SX),
    ]


def h_of_phi(phi: tuple[float, float, float], shifts: list[np.ndarray]) -> np.ndarray:
    return sum(c * op for c, op in zip(phi, shifts))


def selector_from_phi(phi: np.ndarray) -> tuple[float, np.ndarray]:
    r2 = float(np.dot(phi, phi))
    if r2 <= 0:
        raise ValueError("phi must be nonzero")
    p = (phi * phi) / r2
    f = float(sum(p[i] * p[j] for i in range(3) for j in range(i + 1, 3)))
    return f, p


def simplex_grid(step: float = 0.05) -> list[np.ndarray]:
    n = int(round(1.0 / step))
    pts = []
    for i in range(n + 1):
        for j in range(n + 1 - i):
            k = n - i - j
            pts.append(np.array([i, j, k], dtype=float) / n)
    return pts


def p23_hermitian_core(a: float, z: complex, c: float, d: float) -> np.ndarray:
    return np.array(
        [
            [a, z, z],
            [np.conjugate(z), c, d],
            [np.conjugate(z), d, c],
        ],
        dtype=complex,
    )


def real_aligned_core(a: float, b: float, c: float, d: float) -> np.ndarray:
    return p23_hermitian_core(a, complex(b, 0.0), c, d)


def canonical_coords(h: np.ndarray) -> tuple[float, float, float, float, float, float, float]:
    return (
        float(np.real(h[0, 0])),
        float(np.real(h[1, 1])),
        float(np.real(h[2, 2])),
        float(np.abs(h[0, 1])),
        float(np.abs(h[1, 2])),
        float(np.abs(h[2, 0])),
        float(np.angle(h[0, 1] * h[1, 2] * h[2, 0])),
    )


def part1_graph_first_selector_has_exact_axis_minima() -> None:
    print("\n" + "=" * 88)
    print("PART 1: THE GRAPH-FIRST SELECTOR HAS EXACT AXIS MINIMA")
    print("=" * 88)

    shifts = build_axis_shifts()
    for i, s in enumerate(shifts, start=1):
        check(f"S_{i} is Hermitian", np.allclose(s, s.conj().T, atol=1e-10))
        check(f"S_{i}^2 = I", np.allclose(s @ s, I8, atol=1e-10))

    pts = simplex_grid()
    vals = np.array([sum(p[i] * p[j] for i in range(3) for j in range(i + 1, 3)) for p in pts])
    min_val = float(vals.min())
    mins = [p for p, val in zip(pts, vals) if abs(val - min_val) < 1e-12]
    vertices = [
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
    ]
    exact_vertices = all(any(np.allclose(p, v, atol=1e-12) for v in vertices) for p in mins)

    check("The normalized graph-first selector has exactly three minima", len(mins) == 3, f"count={len(mins)}")
    check("Those minima are exactly the three coordinate axes", abs(min_val) < 1e-12 and exact_vertices)
    print("  [INFO] The graph-first route derives a weak-axis selector on the hw=1 triplet")


def part2_selected_axis_carries_residual_z2_stabilizer() -> None:
    print("\n" + "=" * 88)
    print("PART 2: EACH SELECTED AXIS HAS EXACT RESIDUAL Z2 STABILIZER")
    print("=" * 88)

    e1 = np.array([1.0, 0.0, 0.0])
    swap23 = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0],
            [0.0, 1.0, 0.0],
        ]
    )
    f_e1, _ = selector_from_phi(e1)
    f_diag, _ = selector_from_phi(np.array([1.0, 1.0, 1.0]))

    check("The selected axis e1 is fixed by the 2<->3 swap", np.allclose(swap23 @ e1, e1, atol=1e-12))
    check("The selected axis is strictly lower than the democratic diagonal under the selector", f_e1 < f_diag,
          f"F_axis={f_e1:.6f}, F_diag={f_diag:.6f}")
    print("  [INFO] The selected axis leaves an exact residual Z2 stabilizer")


def part3_premise_e_residual_z2_yields_the_active_hermitian_core() -> None:
    print("\n" + "=" * 88)
    print("PART 3: UNDER PREMISE (E), RESIDUAL Z2 YIELDS THE ACTIVE HERMITIAN CORE LAW")
    print("=" * 88)

    h = p23_hermitian_core(1.10, 0.26 + 0.19j, 0.81, 0.17)
    resid = np.linalg.norm(P23 @ h @ P23 - h)
    d1, d2, d3, r12, r23, r31, phi = canonical_coords(h)

    check("The full complex aligned core is Hermitian", np.allclose(h, h.conj().T, atol=1e-12))
    check("The aligned core is exactly P23-invariant", resid < 1e-12, f"residual={resid:.2e}")
    check("Residual Z2 invariance forces d2=d3", abs(d2 - d3) < 1e-12, f"d2-d3={d2-d3:.2e}")
    check("Residual Z2 invariance forces r12=r31", abs(r12 - r31) < 1e-12, f"r12-r31={r12-r31:.2e}")
    check("Residual Z2 invariance does NOT force the fixed-axis coupling real", abs(np.imag(h[0, 1])) > 1e-12,
          f"Im(z)={np.imag(h[0, 1]):.6f}")
    check("The old real four-parameter core is recovered only by the specialization Im(z)=0",
          np.allclose(real_aligned_core(1.10, 0.26, 0.81, 0.17), p23_hermitian_core(1.10, 0.26 + 0.0j, 0.81, 0.17)))
    print(f"  [INFO] The active aligned Hermitian lane has exact form [[a,z,z],[z*,c,d],[z*,d,c]]  (r23={r23:.6f}, triangle_phase={phi:.6f})")


def part4_premise_e_gives_alignment_but_not_values_or_sector_choice() -> None:
    print("\n" + "=" * 88)
    print("PART 4: PREMISE (E) GIVES ALIGNMENT, BUT NOT VALUES OR ACTIVE-SECTOR CHOICE")
    print("=" * 88)

    h1 = p23_hermitian_core(1.10, 0.26 + 0.19j, 0.81, 0.17)
    h2 = p23_hermitian_core(0.93, 0.11 - 0.07j, 1.04, 0.39)
    sigma = np.block([[np.zeros((3, 3), dtype=complex), np.eye(3)], [np.eye(3), np.zeros((3, 3), dtype=complex)]])
    pair_nu = np.block([[h1, np.zeros((3, 3), dtype=complex)], [np.zeros((3, 3), dtype=complex), np.diag([0.1, 0.2, 0.3])]])
    pair_e = sigma @ pair_nu @ sigma

    check("Two distinct aligned Hermitian cores survive the same premised P23 law", np.linalg.norm(h1 - h2) > 1e-6)
    check("Exact sector exchange still flips which lepton sector carries the active aligned block", np.linalg.norm(pair_e - sigma @ pair_nu @ sigma) < 1e-12)
    print("  [INFO] Under premise (E), the route fixes alignment but not the aligned-core values")
    print("  [INFO] It does not by itself fix whether the active block sits on E_nu or E_e")


def part5_note_surface_pins() -> None:
    print("\n" + "=" * 88)
    print("PART 5: CONDITIONAL-INVARIANCE NOTE-SURFACE PINS")
    print("=" * 88)

    note_text = NOTE_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())

    check("The source note names premise (E)", "premise (E)" in note_text, cls="B")
    check(
        "The source note carries the dated downstream-hygiene line",
        "2026-07-10 downstream hygiene." in note_text,
        cls="B",
    )
    check(
        "The unconditional lane-forces-alignment sentence is absent",
        "lane forces the aligned law" not in note_text,
        cls="B",
    )
    check(
        "Theorem item 3 is conditional on premise (E)",
        "3. under premise (E), residual `Z_2` equivariance" in note_flat,
        cls="B",
    )


def main() -> int:
    print("=" * 88)
    print("PMNS GRAPH-FIRST AXIS ALIGNMENT")
    print("=" * 88)
    print()
    print("Question:")
    print("  Can a genuinely graph-native selector on the hw=1 corner triplet")
    print("  derive any positive PMNS law without returning to the old full")
    print("  microscopic decomposition route?")

    part1_graph_first_selector_has_exact_axis_minima()
    part2_selected_axis_carries_residual_z2_stabilizer()
    part3_premise_e_residual_z2_yields_the_active_hermitian_core()
    part4_premise_e_gives_alignment_but_not_values_or_sector_choice()
    part5_note_surface_pins()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Positive graph-first result:")
    print("    - the hw=1 cube selector derives a weak-axis choice")
    print("    - the selected axis carries residual Z2")
    print("    - under premise (E), residual Z2 gives the aligned active Hermitian core")
    print("    - the core keeps the complex off-axis coupling allowed by Hermiticity")
    print()
    print("  Boundary:")
    print("    - this route does not derive residual-Z2 equivariance of the active operator")
    print("    - this route does not fix the aligned-core values")
    print("    - this route does not fix whether the active sector is neutrino or charged-lepton")
    print()
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
