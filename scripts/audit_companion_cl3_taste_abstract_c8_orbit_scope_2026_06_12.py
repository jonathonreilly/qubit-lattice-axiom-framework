#!/usr/bin/env python3
"""Verify the abstract C^8 S3/Z3 orbit theorem for CL3 taste generation scope repair.

This runner intentionally checks only the representation-theory content used by
docs/CL3_TASTE_GENERATION_THEOREM.md after the 2026-06-12 narrowing:

  C^8 = (C^2)^{otimes 3} under tensor-position S3 permutations,
  the hw=1 three-state subspace as A1+E with a Z3 orbit,
  and the restricted spectra of the locally defined Y and T3 operators.

It does not assert a framework matter-carrier realization or a physical-family
identification of the three orbit labels.
"""

from itertools import product as iproduct

import numpy as np


EPS = 1e-12
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {label}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return ok


def kron(*mats: np.ndarray) -> np.ndarray:
    result = mats[0]
    for mat in mats[1:]:
        result = np.kron(result, mat)
    return result


def state_idx(b1: int, b2: int, b3: int) -> int:
    return 4 * b1 + 2 * b2 + b3


def perm_matrix_8d(perm: list[int]) -> np.ndarray:
    """perm[i] = j means new axis i takes old axis j."""
    mat = np.zeros((8, 8), dtype=complex)
    for b1, b2, b3 in iproduct(range(2), repeat=3):
        bits = [b1, b2, b3]
        new_bits = [bits[perm[i]] for i in range(3)]
        mat[state_idx(*new_bits), state_idx(b1, b2, b3)] = 1.0
    return mat


def main() -> int:
    print("=" * 78)
    print("CL3 abstract C^8 S3/Z3 orbit and restricted-spectrum verifier")
    print("=" * 78)

    i2 = np.eye(2, dtype=complex)
    i8 = np.eye(8, dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)

    t12 = perm_matrix_8d([1, 0, 2])
    t23 = perm_matrix_8d([0, 2, 1])
    z3 = perm_matrix_8d([2, 0, 1])

    print("\n-- S3/Z3 group action on C^8 --")
    check("T12^2 = I8", np.allclose(t12 @ t12, i8, atol=EPS))
    check("T23^2 = I8", np.allclose(t23 @ t23, i8, atol=EPS))
    check("Z3^3 = I8", np.allclose(z3 @ z3 @ z3, i8, atol=EPS))
    check("(T12*T23)^3 = I8", np.allclose((t12 @ t23) @ (t12 @ t23) @ (t12 @ t23), i8, atol=EPS))

    hw1_idx = [state_idx(1, 0, 0), state_idx(0, 1, 0), state_idx(0, 0, 1)]
    hw1_proj = np.diag([1.0 if idx in hw1_idx else 0.0 for idx in range(8)])
    check("hw=1 subspace is invariant under T12,T23,Z3",
          all(np.allclose(op @ hw1_proj @ op.conj().T, hw1_proj, atol=EPS) for op in (t12, t23, z3)))

    basis = [np.zeros(8) for _ in hw1_idx]
    for i, idx in enumerate(hw1_idx):
        basis[i][idx] = 1.0

    print("\n-- Z3 orbit on the hw=1 labels --")
    check("Z3: (1,0,0) -> (0,1,0)", np.allclose(z3 @ basis[0], basis[1], atol=EPS))
    check("Z3: (0,1,0) -> (0,0,1)", np.allclose(z3 @ basis[1], basis[2], atol=EPS))
    check("Z3: (0,0,1) -> (1,0,0)", np.allclose(z3 @ basis[2], basis[0], atol=EPS))

    print("\n-- Character decomposition --")
    chi_e = float(np.trace(i8).real)
    chi_2c = float(np.trace(t12).real)
    chi_3c = float(np.trace(z3).real)
    check("chi(e)=8", np.isclose(chi_e, 8), f"got {chi_e:.1f}")
    check("chi(2-cycle)=4", np.isclose(chi_2c, 4), f"got {chi_2c:.1f}")
    check("chi(3-cycle)=2", np.isclose(chi_3c, 2), f"got {chi_3c:.1f}")

    n_a1 = (chi_e + 3 * chi_2c + 2 * chi_3c) / 6
    n_a2 = (chi_e - 3 * chi_2c + 2 * chi_3c) / 6
    n_e = (2 * chi_e - 2 * chi_3c) / 6
    check("C^8 = 4*A1 + 0*A2 + 2*E",
          np.isclose(n_a1, 4) and np.isclose(n_a2, 0) and np.isclose(n_e, 2),
          f"n_A1={n_a1:.1f}, n_A2={n_a2:.1f}, n_E={n_e:.1f}")

    chi_hw1_2c = float(np.trace(t12 @ hw1_proj).real)
    chi_hw1_3c = float(np.trace(z3 @ hw1_proj).real)
    n_a1_hw1 = (3 + 3 * chi_hw1_2c) / 6
    n_e_hw1 = (2 * 3 - 2 * chi_hw1_3c) / 6
    check("hw=1 sector = A1 + E",
          np.isclose(chi_hw1_2c, 1) and np.isclose(chi_hw1_3c, 0)
          and np.isclose(n_a1_hw1, 1) and np.isclose(n_e_hw1, 1),
          f"chi_hw1=(3,{chi_hw1_2c:.0f},{chi_hw1_3c:.0f})")

    print("\n-- Restricted Y and T3 spectra on hw=1 --")
    p_swap = np.zeros((8, 8), dtype=complex)
    for b1, b2, b3 in iproduct(range(2), repeat=3):
        p_swap[state_idx(b1, b2, b3), state_idx(b2, b1, b3)] = 1.0
    p_symm = (i8 + p_swap) / 2
    p_antisymm = (i8 - p_swap) / 2
    y_op = (1 / 3) * p_symm - p_antisymm
    t3_op = kron(np.eye(4, dtype=complex), s3 / 2)

    evals_y_hw1 = sorted(np.linalg.eigvalsh(y_op[np.ix_(hw1_idx, hw1_idx)].real))
    evals_t3_hw1 = sorted(np.linalg.eigvalsh(t3_op[np.ix_(hw1_idx, hw1_idx)].real))
    check("hw=1 Y spectrum = {-1,+1/3,+1/3}",
          np.allclose(evals_y_hw1, sorted([-1.0, 1 / 3, 1 / 3]), atol=EPS),
          f"got {np.round(evals_y_hw1, 6)}")
    check("hw=1 T3 spectrum = {-1/2,+1/2,+1/2}",
          np.allclose(evals_t3_hw1, sorted([-0.5, 0.5, 0.5]), atol=EPS),
          f"got {np.round(evals_t3_hw1, 6)}")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: abstract C^8 S3/Z3 orbit verifier FAILED.")
        return 1
    print("VERDICT: the abstract C^8 tensor-position S3 representation decomposes as "
          "4*A1 + 0*A2 + 2*E; the hw=1 subspace is A1+E with a Z3 three-label orbit; "
          "the restricted Y and T3 spectra are {-1,+1/3,+1/3} and {-1/2,+1/2,+1/2}. "
          "No carrier or physical-family identification is asserted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
