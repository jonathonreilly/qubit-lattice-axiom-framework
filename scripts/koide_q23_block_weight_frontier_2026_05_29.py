#!/usr/bin/env python3
"""Bounded Koide Q=2/3 block-weight frontier checks."""

from __future__ import annotations

import math
import sys

import numpy as np

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"[{'PASS' if ok else 'FAIL'}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def q_from_components(a: float, b_abs: float) -> float:
    return (3.0 * a * a + 6.0 * b_abs * b_abs) / (9.0 * a * a)


def q_from_trivial_power(p_plus: float) -> float:
    return 1.0 / (3.0 * p_plus)


def real_irrep_blocks_for_cyclic(d: int) -> int:
    blocks = 1
    if d % 2 == 0:
        blocks += 1
    blocks += (d - 1) // 2
    return blocks


def main() -> int:
    section("C_3 generation surface")
    r = np.array([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
    vals = np.linalg.eigvals(r)
    expected = np.array([1.0, np.exp(2j * np.pi / 3), np.exp(4j * np.pi / 3)])
    check(
        "cyclic generator has cube-root spectrum",
        np.allclose(np.sort_complex(vals), np.sort_complex(expected)),
        f"eig={np.round(np.sort_complex(vals), 6)}",
    )
    body = np.ones(3) / math.sqrt(3)
    check("body diagonal is the fixed direction", np.allclose(r @ body, body))

    plane_1 = np.array([1.0, -1.0, 0.0])
    plane_1 /= np.linalg.norm(plane_1)
    plane_2 = np.cross(body, plane_1)
    axis_cross = np.array(
        [[0.0, -body[2], body[1]], [body[2], 0.0, -body[0]], [-body[1], body[0], 0.0]]
    )
    basis = np.column_stack([plane_1, plane_2])
    j_plane = basis.T @ axis_cross @ basis
    check("doublet plane carries a complex structure", np.allclose(j_plane @ j_plane, -np.eye(2)))

    section("Koide value from isotype power split")
    for ratio, expected_q in [(0.0, 1 / 3), (0.5, 2 / 3), (1.0, 1.0)]:
        q = q_from_components(1.0, math.sqrt(ratio))
        check(
            f"|b|^2/a^2={ratio:g} gives expected Q",
            abs(q - expected_q) < 1e-12,
            f"Q={q:.12f}",
        )

    rows = [
        ("democratic endpoint", 1.0, 1 / 3),
        ("equal-block rule", 0.5, 2 / 3),
        ("dimension/Plancherel rule", 1 / 3, 1.0),
    ]
    for label, p_plus, expected_q in rows:
        q = q_from_trivial_power(p_plus)
        check(label, abs(q - expected_q) < 1e-12, f"p_plus={p_plus:.6f}, Q={q:.12f}")

    section("Dimension-three localization")
    for d, expected_blocks in [(2, 2), (3, 2), (4, 3), (5, 3), (6, 4)]:
        got = real_irrep_blocks_for_cyclic(d)
        check(f"R[Z_{d}] real block count", got == expected_blocks, f"B={got}")
    slope = (
        ((3.0 + 1e-6 - 3.0) / (2 * (3.0 + 1e-6)))
        - ((3.0 - 1e-6 - 3.0) / (2 * (3.0 - 1e-6)))
    ) / (2e-6)
    check("Q_equipartition and range midpoint cross transversally at d=3", abs(slope - 1 / 6) < 1e-9)

    section("Counting-vs-splitting localization")
    gamma = (2.0 / 3.0) * np.ones((3, 3)) - np.eye(3)
    h_circ = 1.3 * np.eye(3) + 0.7 * r + 0.2 * (r @ r)
    comm = np.max(np.abs(h_circ @ r - r @ h_circ))
    anti = np.max(np.abs(h_circ @ gamma + gamma @ h_circ))
    check("C_3-equivariant example commutes with the C_3 generator", comm < 1e-12, f"comm={comm:.2e}")
    check("same example is not chiral for Gamma_chi", anti > 1e-3, f"anti={anti:.3f}")
    h_chiral = np.outer(body, plane_1) + np.outer(plane_1, body)
    anti_chiral = np.max(np.abs(h_chiral @ gamma + gamma @ h_chiral))
    comm_chiral = np.max(np.abs(h_chiral @ r - r @ h_chiral))
    check("orbit-splitting example anticommutes with Gamma_chi", anti_chiral < 1e-12, f"anti={anti_chiral:.2e}")
    check("orbit-splitting example breaks C_3 equivariance", comm_chiral > 1e-3, f"comm={comm_chiral:.3f}")

    section("Summary")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("The equal-block rule gives Q=2/3 exactly, but this runner does not derive or approve that physical rule.")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
