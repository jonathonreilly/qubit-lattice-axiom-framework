#!/usr/bin/env python3
"""Classify T-odd generation-factor candidates for the K-reality gate.

Source note:
  docs/T_ODD_K_REALITY_SOURCE_SPACE_CLASSIFIER_NO_GO_NOTE_2026-06-07.md

Finite carrier:
  V = C^3 with the C3 cyclic shift C, K = entrywise conjugation, and
  S = C + C^2 selecting the singlet | doublet partition.

The runner checks that K-odd Hermitian operators split into:

  span{A = i(C-C^2)}          commuting C3 current, partition-blind
  bridge_2d                  singlet-doublet bridge, C3-breaking

Thus "T-odd and non-commuting with S" is not one extra scalar condition. It is
equivalent, on this finite carrier, to supplying a nonzero vector in the C3
doublet plane. C3 averaging kills that bridge component.
"""

from __future__ import annotations

import sys
from typing import Iterable

import numpy as np


PASS = 0
FAIL = 0
TOL = 1e-9


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  --  {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def frob_inner(a: np.ndarray, b: np.ndarray) -> complex:
    return np.trace(a.conj().T @ b)


def frob_norm(a: np.ndarray) -> float:
    return float(np.sqrt(np.real_if_close(frob_inner(a, a))))


def cyclic_shift() -> np.ndarray:
    c = np.zeros((3, 3), dtype=complex)
    for j in range(3):
        c[(j + 1) % 3, j] = 1.0
    return c


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def c3_average(m: np.ndarray, c: np.ndarray) -> np.ndarray:
    c2 = c @ c
    return (m + c @ m @ c.conj().T + c2 @ m @ c2.conj().T) / 3.0


def bridge_from_vector(v: np.ndarray, u: np.ndarray) -> np.ndarray:
    """K-odd Hermitian bridge i(v u^T - u v^T), for real v perpendicular to u."""
    v = np.asarray(v, dtype=float)
    u = np.asarray(u, dtype=float)
    r = np.outer(v, u) - np.outer(u, v)
    return 1j * r


def sorted_eigs(m: np.ndarray) -> np.ndarray:
    h = (m + m.conj().T) / 2
    return np.sort(np.linalg.eigvalsh(h).real)


def random_coefficients() -> Iterable[tuple[float, float, float]]:
    return [
        (0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
        (1.2, -0.3, 0.7),
        (-0.5, 2.0, 1.0),
        (3.0, -1.0, -2.0),
        (-2.2, 0.4, 1.6),
    ]


def main() -> int:
    c = cyclic_shift()
    c2 = c @ c
    i3 = np.eye(3, dtype=complex)
    s = c + c2
    a_current = 1j * (c - c2)

    u = np.ones(3) / np.sqrt(3.0)
    p0 = np.outer(u, u)
    p1 = i3 - p0

    e1 = np.array([1.0, -1.0, 0.0]) / np.sqrt(2.0)
    e2 = np.array([1.0, 1.0, -2.0]) / np.sqrt(6.0)
    b1 = bridge_from_vector(e1, u)
    b2 = bridge_from_vector(e2, u)

    section("A. Carrier and partition checks")
    check("C^3 = I", np.allclose(np.linalg.matrix_power(c, 3), i3))
    check("S = C+C^2 is K-even Hermitian", np.allclose(s, s.conj().T) and np.allclose(s.conj(), s))
    check("S eigenvalues are {-1,-1,+2}", np.allclose(sorted_eigs(s), [-1.0, -1.0, 2.0]))
    check("P0 is singlet rank 1 and P1 is doublet rank 2",
          abs(np.trace(p0).real - 1.0) < TOL and abs(np.trace(p1).real - 2.0) < TOL)
    check("S = 3 P0 - I", np.allclose(s, 3.0 * p0 - i3))

    section("B. K-odd Hermitian source-space basis")
    basis = [a_current, b1, b2]
    for idx, m in enumerate(basis):
        check(f"basis[{idx}] is Hermitian and K-odd",
              np.allclose(m, m.conj().T) and np.allclose(m.conj(), -m))
    gram = np.array([[frob_inner(x, y).real for y in basis] for x in basis])
    check("A, B1, B2 are linearly independent K-odd Hermitian directions",
          abs(np.linalg.det(gram)) > TOL, f"det Gram={np.linalg.det(gram):.6g}")
    check("A = i(C-C^2) commutes with C and S",
          np.allclose(comm(a_current, c), 0) and np.allclose(comm(a_current, s), 0))
    check("B1 and B2 do not commute with S",
          frob_norm(comm(b1, s)) > TOL and frob_norm(comm(b2, s)) > TOL,
          f"||[B1,S]||={frob_norm(comm(b1,s)):.6g}, ||[B2,S]||={frob_norm(comm(b2,s)):.6g}")

    section("C. Orthogonal split: current plus singlet-doublet bridge")
    all_decompositions_ok = True
    for coeffs in random_coefficients():
        t = coeffs[0] * a_current + coeffs[1] * b1 + coeffs[2] * b2
        alpha = (frob_inner(a_current, t) / frob_inner(a_current, a_current)).real
        t_current = alpha * a_current
        t_bridge = t - t_current
        current_ok = np.allclose(comm(t_current, s), 0, atol=1e-8)
        bridge_offblock = (
            np.linalg.norm(p0 @ t_bridge @ p0)
            + np.linalg.norm(p1 @ t_bridge @ p1)
        )
        bridge_ok = bridge_offblock < 1e-8
        comm_bridge = frob_norm(comm(t_bridge, s))
        bridge_nonzero = frob_norm(t_bridge) > 1e-8
        iff_ok = (comm_bridge > 1e-8) == bridge_nonzero
        all_decompositions_ok = all_decompositions_ok and current_ok and bridge_ok and iff_ok
    check("every sampled T splits into commuting current + pure off-block bridge",
          all_decompositions_ok)

    # The bridge is exactly the data of a doublet vector q = P1 T u.
    vector_recovery_ok = True
    for theta in np.linspace(0.0, 2.0 * np.pi, 13)[:-1]:
        v = np.cos(theta) * e1 + np.sin(theta) * e2
        b = bridge_from_vector(v, u)
        q = p1 @ b @ u
        expected = 1j * v
        recovered = (-1j) * q
        vector_recovery_ok = vector_recovery_ok and np.allclose(q, expected, atol=1e-8)
        vector_recovery_ok = vector_recovery_ok and np.allclose(recovered.real, v, atol=1e-8)
    check("noncommuting T-odd bridge is equivalent to choosing a doublet vector",
          vector_recovery_ok)

    section("D. C3 action fixes A and rotates/kills the bridge")
    avg_ok = True
    for coeffs in random_coefficients():
        t = coeffs[0] * a_current + coeffs[1] * b1 + coeffs[2] * b2
        alpha = (frob_inner(a_current, t) / frob_inner(a_current, a_current)).real
        avg_ok = avg_ok and np.allclose(c3_average(t, c), alpha * a_current, atol=1e-8)
    check("C3 averaging kills exactly the noncommuting bridge component", avg_ok)

    # Matrix of Ad_C on the bridge basis, using the orthogonal but not unit basis.
    bridge_gram = np.array([[frob_inner(x, y).real for y in [b1, b2]] for x in [b1, b2]])
    action = np.zeros((2, 2), dtype=float)
    for j, bj in enumerate([b1, b2]):
        image = c @ bj @ c.conj().T
        rhs = np.array([frob_inner(b1, image).real, frob_inner(b2, image).real])
        action[:, j] = np.linalg.solve(bridge_gram, rhs)
    check("Ad_C on bridge has trace -1 and determinant +1",
          abs(np.trace(action) + 1.0) < 1e-8 and abs(np.linalg.det(action) - 1.0) < 1e-8,
          f"action={np.round(action, 6).tolist()}")
    check("bridge has no nonzero C3-fixed vector",
          abs(np.linalg.det(action - np.eye(2))) > 1e-8,
          f"det(Ad_C-I)={np.linalg.det(action - np.eye(2)):.6g}")

    section("E. Scalar invariants are angle-blind on the unit bridge")
    eig_ok = True
    comm_norm_ok = True
    for theta in np.linspace(0.0, 2.0 * np.pi, 25)[:-1]:
        v = np.cos(theta) * e1 + np.sin(theta) * e2
        b = bridge_from_vector(v, u)
        eig_ok = eig_ok and np.allclose(sorted_eigs(b), [-1.0, 0.0, 1.0], atol=1e-8)
        comm_norm_ok = comm_norm_ok and abs(frob_norm(comm(b, s)) - 3.0 * np.sqrt(2.0)) < 1e-8
    check("all unit bridge orientations have eigenvalues {-1,0,+1}", eig_ok)
    check("all unit bridge orientations have the same ||[T,S]||", comm_norm_ok)

    # The commutant U(1) generated by A rotates bridge orientations continuously.
    theta = 0.37
    w, vmat = np.linalg.eigh(a_current / np.sqrt(3.0))
    u_theta = vmat @ np.diag(np.exp(1j * theta * w)) @ vmat.conj().T
    rotated = u_theta @ b1 @ u_theta.conj().T
    check("exp(i theta A/sqrt(3)) commutes with C and rotates bridge orientation",
          np.allclose(comm(u_theta, c), 0, atol=1e-8)
          and abs(frob_norm(rotated) - frob_norm(b1)) < 1e-8
          and frob_norm(rotated - b1) > 1e-4)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: T-odd K-reality source-space classifier checks FAILED.")
        return 1
    print("VERDICT: source-space classifier checks pass.")
    print("  K-odd Hermitian candidates split as current A plus a C3-breaking")
    print("  singlet-doublet bridge. The noncommuting bridge is exactly a")
    print("  supplied doublet vector; C3 averaging kills it. No K-reality")
    print("  closure is claimed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
