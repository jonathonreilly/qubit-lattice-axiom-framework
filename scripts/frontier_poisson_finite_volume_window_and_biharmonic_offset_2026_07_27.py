#!/usr/bin/env python3
"""Finite-volume Poisson-window and biharmonic-offset checks.

This runner supports the paired bounded theorem note. It makes four finite
claims:

* fixed and scaling Poisson windows give different finite-volume results;
* the parent raw exponent estimator uses a scaling window;
* on five tested Dirichlet grids that estimator scores the biharmonic profile
  closer to exponent one than the Poisson profile;
* the raw periodic biharmonic fit is dominated by an additive infrared offset,
  while a constant-shift-invariant chord slope approaches the continuum
  -1/(8*pi) comparator.

It does not repair the parent susceptibility/sign bridge, test the full parent
operator family, or make a self-consistency claim.
"""

from __future__ import annotations

import inspect
import sys
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import splu

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import frontier_self_consistent_field_equation as F  # noqa: E402

FIX_LO = 4
FIX_HI = 10
PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> bool:
    """Record and print one decisive check."""
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{status}] {label}")
    if detail:
        for line in detail.splitlines():
            print(f"         {line}")
    return condition


def laplacian_symbol(n: int) -> np.ndarray:
    """Fourier symbol of the nearest-neighbor graph Laplacian."""
    k = 2 * np.pi * np.fft.fftfreq(n)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    return 2 * (np.cos(kx) + np.cos(ky) + np.cos(kz)) - 6.0


def greens_periodic(n: int, power: int = 1) -> np.ndarray:
    """Mean-zero inverse of Delta**power on the periodic finite lattice."""
    symbol = laplacian_symbol(n) ** power
    inverse_symbol = np.zeros_like(symbol, dtype=complex)
    nonzero = np.abs(symbol) > 1e-13
    inverse_symbol[nonzero] = 1.0 / symbol[nonzero]
    return np.fft.ifftn(inverse_symbol).real


def axis_fit(
    field: np.ndarray,
    lo: int,
    hi: int,
    origin: tuple[int, int, int] = (0, 0, 0),
) -> tuple[float, float]:
    """Fit abs(field) to r**(-beta) along the positive y-axis."""
    radii: list[float] = []
    values: list[float] = []
    for radius in range(lo, hi + 1):
        index = (origin[0], origin[1] + radius, origin[2])
        if index[1] >= field.shape[1]:
            break
        value = abs(float(field[index]))
        if value > 1e-300:
            radii.append(float(radius))
            values.append(value)
    if len(radii) < 3:
        return float("nan"), float("nan")
    log_r = np.log(radii)
    log_v = np.log(values)
    coefficient = np.polyfit(log_r, log_v, 1)
    fitted = coefficient[0] * log_r + coefficient[1]
    residual = float(np.sum((log_v - fitted) ** 2))
    total = float(np.sum((log_v - np.mean(log_v)) ** 2))
    r_squared = 1.0 - residual / total if total > 0 else 0.0
    return float(-coefficient[0]), float(r_squared)


def dirichlet_greens(n: int, operator: str) -> np.ndarray:
    """Invert the parent runner's Dirichlet Poisson or biharmonic matrix."""
    laplacian, interior_size = F.build_laplacian_sparse(n)
    matrix = laplacian if operator == "poisson" else laplacian @ laplacian
    factorization = splu(matrix.tocsc())
    source = np.zeros((n, n, n))
    source[(n // 2, n // 2, n // 2)] = 1.0
    result = np.zeros_like(source)
    result[1 : n - 1, 1 : n - 1, 1 : n - 1] = factorization.solve(
        source[1 : n - 1, 1 : n - 1, 1 : n - 1].ravel()
    ).reshape((interior_size, interior_size, interior_size))
    return result


print(__doc__)
print("=" * 78)
print("FINITE PROTOCOL CHECKS")
print("=" * 78)

# U0: compare the parent sparse matrix against an independently assembled
# Dirichlet nearest-neighbor matrix, including its connectivity rather than
# only its distinct coefficient values.
n_control = 8
parent_matrix, m_control = F.build_laplacian_sparse(n_control)
parent_dense = parent_matrix.toarray()
expected_dense = np.zeros_like(parent_dense)
steps = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
for x in range(m_control):
    for y in range(m_control):
        for z in range(m_control):
            row = np.ravel_multi_index((x, y, z), (m_control,) * 3)
            expected_dense[row, row] = -6.0
            for dx, dy, dz in steps:
                neighbor = (x + dx, y + dy, z + dz)
                if all(0 <= coordinate < m_control for coordinate in neighbor):
                    column = np.ravel_multi_index(neighbor, (m_control,) * 3)
                    expected_dense[row, column] = 1.0
matrix_error = float(np.max(np.abs(parent_dense - expected_dense)))
check(
    "U0  periodic symbol and parent matrix share the same nearest-neighbor stencil",
    matrix_error == 0.0,
    f"maximum entrywise error against independent connectivity assembly: "
    f"{matrix_error:.3e}\n"
    "periodic symbol: 2*(cos kx + cos ky + cos kz) - 6",
)

# U1: fixed-window periodic Poisson control.
sizes = (32, 48, 64, 96, 128, 192)
fixed_rows: list[tuple[int, float, float, float]] = []
for n in sizes:
    green = -greens_periodic(n, power=1)
    beta, r_squared = axis_fit(green, FIX_LO, FIX_HI)
    normalization = 4 * np.pi * FIX_HI * float(green[0, FIX_HI, 0])
    fixed_rows.append((n, beta, r_squared, normalization))
fixed_betas = [row[1] for row in fixed_rows]
fixed_normalizations = [row[3] for row in fixed_rows]
check(
    "U1  the fixed-window periodic Poisson sequence trends toward beta=1 "
    "and 4*pi*r*G=1 over the tested sizes",
    all(
        fixed_betas[index] > fixed_betas[index + 1]
        for index in range(len(fixed_betas) - 1)
    )
    and fixed_betas[-1] < 1.15
    and all(
        fixed_normalizations[index] < fixed_normalizations[index + 1]
        for index in range(len(fixed_normalizations) - 1)
    )
    and fixed_normalizations[-1] > 0.85,
    "\n".join(
        f"N={n:4d} beta={beta:8.5f} R^2={r_squared:.5f} "
        f"4*pi*r*G(r={FIX_HI})={normalization:.5f}"
        for n, beta, r_squared, normalization in fixed_rows
    )
    + "\nThis is a finite trend check, not a lattice convergence proof.",
)

# U2: scaling-window periodic Poisson comparison.
scaling_rows: list[tuple[int, int, int, float, float, float]] = []
for n in sizes:
    green = -greens_periodic(n, power=1)
    lo = max(3, n // 16)
    hi = n // 4
    beta, r_squared = axis_fit(green, lo, hi)
    normalization = 4 * np.pi * hi * float(green[0, hi, 0])
    scaling_rows.append((n, lo, hi, beta, r_squared, normalization))
late_betas = [row[3] for row in scaling_rows[-3:]]
late_normalizations = [row[5] for row in scaling_rows[-3:]]
check(
    "U2  the scaling-window finite sequence stabilizes away from the "
    "continuum beta and normalization targets",
    max(late_betas) - min(late_betas) < 0.02
    and abs(late_betas[-1] - 1.0) > 0.5
    and max(late_normalizations) - min(late_normalizations) < 0.001
    and abs(late_normalizations[-1] - 1.0) > 0.6,
    "\n".join(
        f"N={n:4d} window={lo}..{hi:<3d} beta={beta:8.5f} "
        f"R^2={r_squared:.5f} 4*pi*r*G(outer)={normalization:.5f}"
        for n, lo, hi, beta, r_squared, normalization in scaling_rows
    )
    + f"\nlast-three beta spread={max(late_betas) - min(late_betas):.5f}; "
    f"outer normalization={late_normalizations[-1]:.5f}",
)

# U3: source pin for the parent estimator.
parent_estimator_source = inspect.getsource(F.check_field_physics)
source_pins = (
    "mid = N // 2",
    "for dy in range(1, mid - 2):",
    "mask = (np.abs(phi_arr) > 1e-30) & (r_arr > 1)",
)
check(
    "U3  the parent raw exponent estimator uses radii 2 through N/2-3",
    all(pin in parent_estimator_source for pin in source_pins),
    "\n".join(
        f"{pin!r}: {pin in parent_estimator_source}" for pin in source_pins
    )
    + "\nTogether these pins define the stated scaling window.",
)

# U4: finite Dirichlet counterexample using the parent matrices and window.
dirichlet_sizes = (16, 20, 24, 32, 40)
dirichlet_rows: dict[str, list[tuple[int, float, float]]] = {}
for operator in ("poisson", "biharmonic"):
    rows: list[tuple[int, float, float]] = []
    for n in dirichlet_sizes:
        green = dirichlet_greens(n, operator)
        beta, r_squared = axis_fit(
            green,
            2,
            n // 2 - 3,
            origin=(n // 2, n // 2, n // 2),
        )
        rows.append((n, beta, r_squared))
    dirichlet_rows[operator] = rows
poisson_dirichlet = [row[1] for row in dirichlet_rows["poisson"]]
biharmonic_dirichlet = [row[1] for row in dirichlet_rows["biharmonic"]]
biharmonic_scores_closer = all(
    abs(biharmonic_dirichlet[index] - 1.0)
    < abs(poisson_dirichlet[index] - 1.0)
    for index in range(len(dirichlet_sizes))
)
check(
    "U4  on all tested Dirichlet grids the parent raw score is closer to "
    "one for biharmonic than for Poisson",
    biharmonic_scores_closer
    and min(abs(beta - 1.0) for beta in biharmonic_dirichlet) < 0.01
    and min(abs(beta - 1.0) for beta in poisson_dirichlet) > 0.5,
    "\n".join(
        f"N={n:3d} window=2..{n // 2 - 3:<3d} "
        f"poisson beta={poisson_beta:7.4f} "
        f"biharmonic beta={biharmonic_beta:7.4f}"
        for (n, poisson_beta, _), (_, biharmonic_beta, _) in zip(
            dirichlet_rows["poisson"],
            dirichlet_rows["biharmonic"],
            strict=True,
        )
    )
    + "\nThis is a finite raw-estimator counterexample, not a claim that the "
    "biharmonic profile has inverse-distance asymptotics.",
)

# U5: the raw biharmonic beta is offset-contaminated. Check the O(N) offset
# directly and use a constant-shift-invariant chord slope for the physical
# shape. The independent continuum comparator is
# Delta^2[-r/(8*pi)] = delta.
biharmonic_rows: list[tuple[int, float, float, float, float, float]] = []
for n in sizes:
    green = greens_periodic(n, power=2)
    raw_beta, raw_r_squared = axis_fit(green, FIX_LO, FIX_HI)
    offset_per_n = float(green[0, 0, 0]) / n
    chord_slope = (
        float(green[0, FIX_HI, 0]) - float(green[0, FIX_LO, 0])
    ) / (FIX_HI - FIX_LO)
    normalized_slope = 8 * np.pi * abs(chord_slope)
    biharmonic_rows.append(
        (
            n,
            raw_beta,
            raw_r_squared,
            offset_per_n,
            chord_slope,
            normalized_slope,
        )
    )
raw_betas = [row[1] for row in biharmonic_rows]
offsets_per_n = [row[3] for row in biharmonic_rows]
chord_slopes = [row[4] for row in biharmonic_rows]
normalized_slopes = [row[5] for row in biharmonic_rows]
relative_offset_spread = (
    max(offsets_per_n) - min(offsets_per_n)
) / np.mean(offsets_per_n)
check(
    "U5  the raw biharmonic beta is offset-contaminated; the invariant "
    "slope approaches -1/(8*pi)",
    all(
        raw_betas[index] > raw_betas[index + 1]
        for index in range(len(raw_betas) - 1)
    )
    and raw_betas[-1] < 0.2
    and relative_offset_spread < 0.04
    and all(slope < 0 for slope in chord_slopes)
    and all(
        normalized_slopes[index] < normalized_slopes[index + 1]
        for index in range(len(normalized_slopes) - 1)
    )
    and normalized_slopes[-1] > 0.93,
    "\n".join(
        f"N={n:4d} raw_beta={raw_beta:8.5f} "
        f"G(0)/N={offset_per_n:.7f} chord_slope={chord_slope:.7f} "
        f"8*pi*abs(slope)={normalized_slope:.6f}"
        for (
            n,
            raw_beta,
            _,
            offset_per_n,
            chord_slope,
            normalized_slope,
        ) in biharmonic_rows
    )
    + f"\nrelative spread of G(0)/N={relative_offset_spread:.5f}; "
    "continuum target slope=-1/(8*pi)=-0.0397887\n"
    "The raw beta tending to zero is therefore not interpreted as flatness.",
)

print("=" * 78)
print(f"TOTAL: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL")
print("=" * 78)
sys.exit(0 if FAIL_COUNT == 0 else 1)
