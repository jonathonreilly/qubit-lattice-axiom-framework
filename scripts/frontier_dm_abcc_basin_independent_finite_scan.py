#!/usr/bin/env python3
"""Independent finite-scan certificate for the DM A-BCC active chamber.

This runner is a repair companion for
`docs/DM_ABCC_BASIN_FINITE_SEARCH_SUPPORT_NOTE_2026-04-30.md`.

It intentionally does not import or hard-code the retained five-basin chart.
The only inputs are the Hermitian pencil, the retained sigma set, the PMNS
central angle target, the active chamber inequality, and a bounded deterministic
seed family.  The runner derives the finite-scan representatives by solving the
three angle-residual equations from multiple seed grids.

Scope firewall: this is not an interval/root-isolation proof and not a global
exhaustiveness theorem.  It is a deterministic finite-scan certificate that the
live equations reproduce the active-chamber representatives and their
C_base/C_neg split without using the archived basin coordinates as inputs.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares


PASS = 0
FAIL = 0


def check(label: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {label}" + (f"  ({detail})" if detail else ""))
    return cond


GAMMA = 0.5
E1 = math.sqrt(8.0 / 3.0)
E2 = math.sqrt(8.0) / 3.0

T_M = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
T_D = np.array([[0, -1, 1], [-1, 1, 0], [1, 0, -1]], dtype=complex)
T_Q = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]], dtype=complex)

H_BASE = np.array(
    [
        [0, E1, -E1 - 1j * GAMMA],
        [E1, 0, -E2],
        [-E1 + 1j * GAMMA, -E2, 0],
    ],
    dtype=complex,
)

SIGMA_RETAINED = [(2, 1, 0), (2, 0, 1), (0, 1, 2), (1, 2, 0)]
TARGET_ANGLES = np.array([0.307, 0.0218, 0.545], dtype=float)
R_ENCLOSE = 50.0
ROOT_TOL = 1e-7
CLUSTER_TOL = 0.08


@dataclass(frozen=True)
class Root:
    point: np.ndarray
    sigma: tuple[int, int, int]
    residual_norm: float
    source_family: str


def j_of(point: np.ndarray) -> np.ndarray:
    m, d, q = point
    return m * T_M + d * T_D + q * T_Q


def h_of(point: np.ndarray) -> np.ndarray:
    return H_BASE + j_of(point)


def in_chamber(point: np.ndarray, slack: float = 0.0) -> bool:
    return bool(point[1] + point[2] >= E1 - slack)


def angles_from_point(point: np.ndarray, sigma: tuple[int, int, int]) -> np.ndarray | None:
    try:
        _, eigvecs = np.linalg.eigh(h_of(point))
    except np.linalg.LinAlgError:
        return None
    u = eigvecs[list(sigma), :]
    u2 = np.abs(u) ** 2
    s13_sq = float(u2[0, 2])
    if s13_sq < 0.0 or s13_sq >= 1.0:
        return None
    c13_sq = 1.0 - s13_sq
    if c13_sq <= 1e-10:
        return None
    s12_sq = float(u2[0, 1]) / c13_sq
    s23_sq = float(u2[1, 2]) / c13_sq
    if not (0.0 < s12_sq < 1.0 and 0.0 < s23_sq < 1.0):
        return None
    return np.array([s12_sq, s13_sq, s23_sq], dtype=float)


def residual(point: np.ndarray, sigma: tuple[int, int, int]) -> np.ndarray:
    angles = angles_from_point(point, sigma)
    if angles is None:
        return np.array([100.0, 100.0, 100.0], dtype=float)
    return angles - TARGET_ANGLES


def determinant_component(point: np.ndarray) -> tuple[str, float]:
    det = float(np.linalg.det(h_of(point)).real)
    return ("C_base" if det > 0.0 else "C_neg"), det


def finite_difference_jacobian(point: np.ndarray, sigma: tuple[int, int, int]) -> np.ndarray:
    h = 1e-5
    base = residual(point, sigma)
    cols = []
    for i in range(3):
        shifted = point.copy()
        shifted[i] += h
        cols.append((residual(shifted, sigma) - base) / h)
    return np.column_stack(cols)


def seed_families() -> list[tuple[str, np.ndarray, float]]:
    cheb = R_ENCLOSE * np.cos((2 * np.arange(9) + 1) / (2 * 9) * math.pi)
    return [
        ("endpoint_grid_9", np.linspace(-R_ENCLOSE, R_ENCLOSE, 9), 2.0),
        ("midpoint_grid_8", np.linspace(-43.75, 43.75, 8), 3.0),
        ("chebyshev_grid_9", cheb, 3.0),
    ]


def add_root(roots: list[Root], candidate: Root) -> None:
    for existing in roots:
        if (
            existing.sigma == candidate.sigma
            and np.linalg.norm(existing.point - candidate.point) < CLUSTER_TOL
        ):
            return
    roots.append(candidate)


def scan_family(name: str, axis: np.ndarray, slack: float) -> list[Root]:
    print(f"\n--- finite scan family: {name} ---")
    roots: list[Root] = []
    seed_count = 0
    for sigma in SIGMA_RETAINED:
        sigma_roots: list[Root] = []
        for m in axis:
            for d in axis:
                for q in axis:
                    seed = np.array([m, d, q], dtype=float)
                    if not in_chamber(seed, slack=slack):
                        continue
                    seed_count += 1
                    result = least_squares(
                        lambda x, s=sigma: residual(np.asarray(x, dtype=float), s),
                        seed,
                        bounds=(-R_ENCLOSE, R_ENCLOSE),
                        xtol=1e-11,
                        ftol=1e-13,
                        gtol=1e-13,
                        max_nfev=500,
                    )
                    point = np.asarray(result.x, dtype=float)
                    norm = float(np.linalg.norm(result.fun, ord=2))
                    if norm > ROOT_TOL:
                        continue
                    if not in_chamber(point):
                        continue
                    if np.max(np.abs(point)) > R_ENCLOSE + 1e-8:
                        continue
                    add_root(sigma_roots, Root(point, sigma, norm, name))
        sigma_roots.sort(key=lambda r: tuple(round(float(x), 8) for x in r.point))
        print(f"    sigma {sigma}: {len(sigma_roots)} active-chamber roots")
        for root in sigma_roots:
            print(
                "        "
                f"point=({root.point[0]:.8f}, {root.point[1]:.8f}, {root.point[2]:.8f}) "
                f"residual={root.residual_norm:.2e}"
            )
            add_root(roots, root)
    print(f"    chamber-compatible seeds tested: {seed_count}")
    check(f"{name}: derived three active-chamber roots", len(roots) == 3, f"found {len(roots)}")
    return roots


def canonical_signature(roots: list[Root]) -> tuple[tuple[tuple[int, int, int], tuple[float, float, float]], ...]:
    packed = []
    for root in roots:
        rounded = tuple(round(float(x), 6) for x in root.point)
        packed.append((root.sigma, rounded))
    return tuple(sorted(packed, key=lambda x: (x[0], x[1])))


def compare_families(per_family: dict[str, list[Root]]) -> list[Root]:
    print("\n--- cross-family finite-scan agreement ---")
    signatures = {name: canonical_signature(roots) for name, roots in per_family.items()}
    names = list(signatures)
    reference = signatures[names[0]]
    for name in names:
        check(
            f"{name} matches the reference derived root set",
            signatures[name] == reference,
            f"signature={signatures[name]}",
        )
    return per_family[names[0]]


def certify_roots(roots: list[Root]) -> None:
    print("\n--- derived active-chamber representative certificate ---")
    roots.sort(key=lambda r: (r.sigma, float(r.point[0])))
    components: list[str] = []
    max_residual = 0.0
    min_jacobian_singular = float("inf")
    max_abs_coord = 0.0
    margins: list[float] = []
    for idx, root in enumerate(roots, start=1):
        angles = angles_from_point(root.point, root.sigma)
        comp, det = determinant_component(root.point)
        jac = finite_difference_jacobian(root.point, root.sigma)
        singular_values = np.linalg.svd(jac, compute_uv=False)
        min_sv = float(np.min(singular_values))
        max_residual = max(max_residual, root.residual_norm)
        min_jacobian_singular = min(min_jacobian_singular, min_sv)
        max_abs_coord = max(max_abs_coord, float(np.max(np.abs(root.point))))
        margins.append(float(root.point[1] + root.point[2] - E1))
        components.append(comp)
        print(
            f"    R{idx}: sigma={root.sigma}, component={comp}, det={det:+.6e}, "
            f"margin={margins[-1]:+.6e}"
        )
        print(
            "        "
            f"point=({root.point[0]:.8f}, {root.point[1]:.8f}, {root.point[2]:.8f})"
        )
        print(
            "        "
            f"angles=({angles[0]:.10f}, {angles[1]:.10f}, {angles[2]:.10f}); "
            f"residual_norm={root.residual_norm:.2e}; min_singular={min_sv:.3e}"
        )

    per_sigma = {sigma: 0 for sigma in SIGMA_RETAINED}
    for root in roots:
        per_sigma[root.sigma] += 1

    check("finite scan root count is three", len(roots) == 3, f"per_sigma={per_sigma}")
    check("sigma=(2,1,0) contributes two active-chamber representatives", per_sigma[(2, 1, 0)] == 2)
    check("sigma=(2,0,1) contributes one active-chamber representative", per_sigma[(2, 0, 1)] == 1)
    check("remaining retained sigma choices contribute no active-chamber representatives", per_sigma[(0, 1, 2)] == 0 and per_sigma[(1, 2, 0)] == 0)
    check("all derived representatives lie strictly inside the R=50 coordinate box", max_abs_coord < 30.0, f"max_abs_coord={max_abs_coord:.3f}")
    check("all derived representatives satisfy the active chamber inequality", min(margins) > 0.0, f"min_margin={min(margins):.3e}")
    check("all residuals are below ROOT_TOL", max_residual < ROOT_TOL, f"max_residual={max_residual:.3e}")
    check("local residual Jacobians have full numerical rank", min_jacobian_singular > 1e-5, f"min_sv={min_jacobian_singular:.3e}")
    check("finite discovered set has one C_base and two C_neg representatives", components.count("C_base") == 1 and components.count("C_neg") == 2, f"components={components}")


def self_firewall() -> None:
    print("\n--- source-input firewall ---")
    source = Path(__file__).read_text(encoding="utf-8")
    forbidden = [
        "BAS" + "INS =",
        "BASIN" + "_SIGMA",
        "0.657" + "061",
        "28." + "006",
        "21.128" + "264",
        "0.501" + "997",
        "1.037" + "883",
    ]
    leaks = [token for token in forbidden if token in source]
    check("runner source does not carry the archived coordinate chart as input", not leaks, f"leaks={leaks}")


def main() -> int:
    print("=" * 72)
    print("DM A-BCC independent active-chamber finite-scan certificate")
    print("=" * 72)
    print(f"retained sigma set: {SIGMA_RETAINED}")
    print(f"target PMNS angles: {tuple(float(x) for x in TARGET_ANGLES)}")
    print(f"active chamber: delta + q_plus >= sqrt(8/3) = {E1:.10f}")
    print(f"coordinate box: [-{R_ENCLOSE}, {R_ENCLOSE}]^3")
    print("scope: deterministic finite scan only; no global root-isolation claim")

    self_firewall()
    per_family = {
        name: scan_family(name, axis, slack)
        for name, axis, slack in seed_families()
    }
    roots = compare_families(per_family)
    certify_roots(roots)

    print()
    print(f"TOTAL: PASS={PASS}  FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
