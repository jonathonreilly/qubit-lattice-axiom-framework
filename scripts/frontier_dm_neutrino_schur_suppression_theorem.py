#!/usr/bin/env python3
"""Conditional supplied-block Schur identity; curvature-to-mass and physical Yukawa identifications are extra premises."""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300

import math
import sys

import numpy as np

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return condition


I2 = np.eye(2, dtype=complex)
I16 = np.eye(16, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)


def kron4(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:
    return np.kron(a, np.kron(b, np.kron(c, d)))


def selector_potential(phi: np.ndarray) -> float:
    return 32.0 * (
        phi[0] ** 2 * phi[1] ** 2
        + phi[0] ** 2 * phi[2] ** 2
        + phi[1] ** 2 * phi[2] ** 2
    )


G0 = kron4(SZ, SZ, SZ, SX)
G1 = kron4(SX, I2, I2, I2)
G2 = kron4(SZ, SX, I2, I2)
G3 = kron4(SZ, SZ, SX, I2)
FULL_STATES = [(a, b, c, t) for a in range(2) for b in range(2) for c in range(2) for t in range(2)]
INDEX = {state: i for i, state in enumerate(FULL_STATES)}

O0 = [(0, 0, 0)]
T1 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
T2 = [(1, 1, 0), (1, 0, 1), (0, 1, 1)]


def projector(spatial_states: list[tuple[int, int, int]]) -> np.ndarray:
    p = np.zeros((16, 16), dtype=complex)
    for t in (0, 1):
        for s in spatial_states:
            p[INDEX[s + (t,)], INDEX[s + (t,)]] = 1.0
    return p


def compress(matrix: np.ndarray, projector_matrix: np.ndarray) -> np.ndarray:
    cols = np.where(np.diag(projector_matrix) > 0.5)[0]
    return matrix[np.ix_(cols, cols)]


def schur_complement(block_matrix: np.ndarray, keep: np.ndarray, elim: np.ndarray) -> np.ndarray:
    keep_idx = np.where(np.diag(keep) > 0.5)[0]
    elim_idx = np.where(np.diag(elim) > 0.5)[0]
    a = block_matrix[np.ix_(keep_idx, keep_idx)]
    b = block_matrix[np.ix_(keep_idx, elim_idx)]
    c = block_matrix[np.ix_(elim_idx, keep_idx)]
    d = block_matrix[np.ix_(elim_idx, elim_idx)]
    return a - b @ np.linalg.inv(d) @ c


def finite_hessian(fun, point: np.ndarray, h: float = 1e-6) -> np.ndarray:
    n = len(point)
    out = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            ei = np.zeros(n)
            ej = np.zeros(n)
            ei[i] = 1.0
            ej[j] = 1.0
            out[i, j] = (
                fun(point + h * ei + h * ej)
                - fun(point + h * ei - h * ej)
                - fun(point - h * ei + h * ej)
                + fun(point - h * ei - h * ej)
            ) / (4.0 * h * h)
    return out


def k_from_yukawa(y_nu: float, alpha_lm: float, m_pl: float, v_ew: float, m3_gev: float) -> float:
    m_r = y_nu**2 * v_ew**2 / m3_gev
    return math.log(m_r / m_pl) / math.log(alpha_lm)


def main() -> int:
    print("=" * 78)
    print("NEUTRINO SCHUR SUPPRESSION THEOREM")
    print("=" * 78)
    print()

    print("Part 1: Exact selector curvature at the weak-axis minimum")
    h_num = finite_hessian(selector_potential, np.array([1.0, 0.0, 0.0]))
    h_exact = np.diag([0.0, 64.0, 64.0])
    transverse = h_exact[1:, 1:]
    quad_coeff = 0.5 * transverse[0, 0]
    print("  Hessian at e1:")
    print(h_num)
    print()
    check("finite-difference Hessian matches the exact axis Hessian",
          np.allclose(h_num, h_exact, atol=5e-4),
          detail="H(e1) = diag(0,64,64)")
    check("transverse selector curvature is degenerate",
          np.allclose(transverse, 64.0 * np.eye(2), atol=1e-12))
    check("quadratic selector coefficient is 32",
          abs(quad_coeff - 32.0) < 1e-12,
          detail=f"V_sel(e1 + d_perp) = 32 |d_perp|^2 + O(d^3)")

    print()
    print("Part 2: Exact Schur complement on T1 after integrating out O0 + T2")
    p_t1 = projector(T1)
    p_int = projector(O0 + T2)

    for m in (0.5, 1.0, 32.0):
        for j in (0.01, 0.1, 0.2):
            block = m * I16 + j * G1
            s_eff = schur_complement(block, p_t1, p_int)
            target = (m - j * j / m) * np.eye(s_eff.shape[0], dtype=complex)
            err = np.linalg.norm(s_eff - target)
            check(
                f"Schur complement gives (m-j^2/m)I on T1 for m={m}, j={j}",
                err < 1e-12,
                detail=f"error = {err:.3e}",
            )

    bridge_identity = compress(p_t1 @ G1 @ p_int @ G1 @ p_t1, p_t1)
    check(
        "intermediate return identity on T1 is exact",
        np.allclose(bridge_identity, np.eye(bridge_identity.shape[0]), atol=1e-12),
        detail="P_T1 Gamma_1 P_int Gamma_1 P_T1 = I",
    )

    print()
    print("Part 3: Supplied m=32 and j=g/sqrt(2) comparison")
    g_weak = 0.653
    j_base = g_weak / math.sqrt(2.0)
    m_selector = 32.0  # Explicit block input; equality with potential coefficient is not derived.
    y_eff = (j_base * j_base) / m_selector

    pi = math.pi
    alpha_bare = 1.0 / (4.0 * pi)
    u0 = 0.5934 ** 0.25
    alpha_lm = alpha_bare / u0
    m_pl = 1.2209e19
    c_apbc = (7.0 / 8.0) ** 0.25
    v_ew = m_pl * c_apbc * alpha_lm**16
    m3_gev = math.sqrt(2.453e-3) * 1.0e-9
    k_eff = k_from_yukawa(y_eff, alpha_lm, m_pl, v_ew, m3_gev)

    print(f"  supplied base j = g_weak/sqrt(2) = {j_base:.12f}")
    print(f"  selector coefficient m = 32      = {m_selector:.12f}")
    print(f"  supplied correction y_eff = j^2 / m        = {y_eff:.12e}")
    print(f"  alpha_LM^2                      = {alpha_lm**2:.12e}")
    print(f"  implied staircase level k_eff   = {k_eff:.6f}")
    print()
    check("generated coefficient equals g_weak^2 / 64",
          abs(y_eff - (g_weak * g_weak) / 64.0) < 1e-15)
    check("generated coefficient lands near alpha_LM^2",
          0.5 < y_eff / (alpha_lm**2) < 2.0,
          detail=f"y_eff / alpha_LM^2 = {y_eff / (alpha_lm**2):.6f}")
    check("Supplied staircase comparison is within 0.05 of 8",
          abs(k_eff - 8.0) < 0.05,
          detail=f"k_eff = {k_eff:.6f}")

    print()
    print("Honest read:")
    print("The Schur correction is j^2/m for the specified invertible eliminated block.")
    print("Setting block m equal to potential coefficient 32 requires a separate normalization/units bridge.")
    print("The Yukawa and staircase readings are conditional comparisons, not physical selection.")
    print("=" * 78)
    print(f"RESULT: {PASS_COUNT} PASS, {FAIL_COUNT} FAIL")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
