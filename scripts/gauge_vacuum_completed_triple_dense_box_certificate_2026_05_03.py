#!/usr/bin/env python3
"""
Gauge-vacuum completed-triple — dense parameter-box gap certificate (2026-05-03).

Finite-grid repair runner for
`docs/GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_COMPLETED_TRIPLE_CURRENT_TRANSFER_FAMILY_BOUNDARY_NOTE_2026-04-19.md`.

Earlier versions fixed the boundary faces
(`tau_transfer = 10^-4`, `tau_boundary = 4.0`, `asym_decay = 10^-8`)
and only checked local inward perturbations. A positive residual on those
faces does not rule out an exact or smaller-gap realization elsewhere in the
continuous parameter box.

This certificate provides a finite deterministic-search route: an explicit 4D
structured grid across the listed parameter box, evaluating the gap at every
one of its 1440 points and reporting the minimum.

The dense grid is NOT a symbolic / interval-arithmetic global
certificate. It proves only the sampled-grid statement.

Listed parameter box:
  tau_transfer  ∈ [10^-4, 5e-2]  (log scale, ~2.7 decades)
  tau_boundary  ∈ [0.5, 4.0]      (linear scale, factor 8)
  asym_decay    ∈ [10^-8, 10^-4]  (log scale, 4 decades)
  linear_decay  ∈ [0.05, 1.0]     (8 linearly spaced points)

The binding predicate is numerical and finite: for every listed grid point,
the float64 value returned by ``gap_at`` after its analytic optimal-scalar fit
must be finite and greater than ``NUMERICAL_ZERO_THRESHOLD``. No statement
about unsampled points in the continuous parameter box is made.
"""
from __future__ import annotations

import math
import os
import sys
import time

import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19 import (
    build_recurrence_matrix,
    completed_sector_data,
    gap_at,
    sample_operator,
    NMAX,
)


AUDIT_INPUT_PATHS = (
    "docs/GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_COMPLETED_TRIPLE_CURRENT_TRANSFER_FAMILY_BOUNDARY_NOTE_2026-04-19.md",
    "scripts/frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19.py",
    "scripts/frontier_gauge_vacuum_plaquette_first_sector_rank_one_transfer_realization_2026_04_19.py",
    "scripts/frontier_gauge_vacuum_plaquette_first_three_sample_environment_evaluator_route_2026_04_17.py",
    "scripts/frontier_gauge_vacuum_plaquette_first_three_sample_local_wilson_retained_positive_cone_obstruction_2026_04_17.py",
    "scripts/frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_2026_04_17.py",
)


# Listed parameter box (per the source note)
TAU_TRANSFER_BOX = (1e-4, 5e-2)
TAU_BOUNDARY_BOX = (0.5, 4.0)
ASYM_DECAY_BOX = (1e-8, 1e-4)
LINEAR_DECAY_BOX = (0.05, 1.0)

# Regression pins are checked only after the sweep; they never select or
# replace the computed argmin.
EXPECTED_Z_MIN = np.array(
    [0.135165279562, 0.374012880009, 0.543843858544], dtype=float
)
EXPECTED_MIN_GAP = 7.791551e-3
NUMERICAL_ZERO_THRESHOLD = 1.0e-6

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))
    return ok


def logspace(lo: float, hi: float, n: int) -> list[float]:
    values = [
        10 ** (math.log10(lo) + i * (math.log10(hi) - math.log10(lo)) / (n - 1))
        for i in range(n)
    ]
    values[0], values[-1] = lo, hi
    return values


def linspace(lo: float, hi: float, n: int) -> list[float]:
    values = [lo + i * (hi - lo) / (n - 1) for i in range(n)]
    values[0], values[-1] = lo, hi
    return values


def main() -> int:
    print("=" * 80)
    print(" gauge_vacuum_completed_triple_dense_box_certificate_2026_05_03.py")
    print(" Finite-grid repair runner: dense parameter-box gap certificate")
    print("=" * 80)
    print()
    print(" Listed parameter box:")
    print(f"   tau_transfer ∈ [{TAU_TRANSFER_BOX[0]:.0e}, {TAU_TRANSFER_BOX[1]:.0e}]")
    print(f"   tau_boundary ∈ [{TAU_BOUNDARY_BOX[0]}, {TAU_BOUNDARY_BOX[1]}]")
    print(f"   asym_decay   ∈ [{ASYM_DECAY_BOX[0]:.0e}, {ASYM_DECAY_BOX[1]:.0e}]")
    print(f"   linear_decay ∈ [{LINEAR_DECAY_BOX[0]}, {LINEAR_DECAY_BOX[1]}]")
    print()
    print("\n--- Build recurrence-matrix infrastructure ---")
    v_min, z_min = completed_sector_data()
    jmat, weights, index = build_recurrence_matrix(NMAX)
    e_three = sample_operator(weights)

    # Dense 4D grid
    n_tau_t = 6
    n_tau_b = 6
    n_asym = 5
    n_ld = 8
    tau_t_grid = logspace(*TAU_TRANSFER_BOX, n_tau_t)
    tau_b_grid = linspace(*TAU_BOUNDARY_BOX, n_tau_b)
    asym_grid = logspace(*ASYM_DECAY_BOX, n_asym)
    ld_grid = linspace(*LINEAR_DECAY_BOX, n_ld)
    total = n_tau_t * n_tau_b * n_asym * n_ld
    grid_points = [
        (tt, tb, ad, ld)
        for tt in tau_t_grid
        for tb in tau_b_grid
        for ad in asym_grid
        for ld in ld_grid
    ]

    print(f"\n--- Dense {n_tau_t}x{n_tau_b}x{n_asym}x{n_ld} = {total} grid sweep ---")
    t0 = time.time()
    gaps = []
    min_gap = float("inf")
    min_pt = None
    max_projection_residual = 0.0
    for tt, tb, ad, ld in grid_points:
        gap, zhat, c_best = gap_at(
            jmat,
            weights,
            index,
            e_three,
            z_min,
            tau_transfer=tt,
            tau_boundary=tb,
            linear_decay=ld,
            asym_decay=ad,
        )
        gaps.append(gap)
        projection_residual = abs(float(np.dot(zhat, c_best * zhat - z_min)))
        max_projection_residual = max(max_projection_residual, projection_residual)
        if gap < min_gap:
            min_gap = gap
            min_pt = (tt, tb, ad, ld)
    elapsed = time.time() - t0
    gaps = np.array(gaps)
    print(f"  swept {total} grid points in {elapsed:.1f} s")
    print(f"  minimum runner-evaluated gap = {min_gap:.12e}")
    print(f"  median gap                  = {float(np.median(gaps)):.6e}")
    print(f"  max gap                     = {float(np.max(gaps)):.6e}")
    print(f"  minimum / numerical-zero threshold = "
          f"{min_gap / NUMERICAL_ZERO_THRESHOLD:.3f}")
    print(f"  max optimal-scalar projection residual = "
          f"{max_projection_residual:.3e}")
    print(f"  argmin grid point:")
    print(f"    tau_transfer = {min_pt[0]:.4e}")
    print(f"    tau_boundary = {min_pt[1]:.4f}")
    print(f"    asym_decay   = {min_pt[2]:.4e}")
    print(f"    linear_decay = {min_pt[3]:.4f}")
    print()

    expected_min_pt = (
        tau_t_grid[0],
        tau_b_grid[-1],
        asym_grid[0],
        ld_grid[2],
    )
    check(
        "finite numerical grid contract has exactly 1440 unique Cartesian points and the stated boundary endpoints",
        len(grid_points) == total
        and len(set(grid_points)) == total
        and tau_t_grid[0] == TAU_TRANSFER_BOX[0]
        and tau_t_grid[-1] == TAU_TRANSFER_BOX[1]
        and tau_b_grid[0] == TAU_BOUNDARY_BOX[0]
        and tau_b_grid[-1] == TAU_BOUNDARY_BOX[1]
        and asym_grid[0] == ASYM_DECAY_BOX[0]
        and asym_grid[-1] == ASYM_DECAY_BOX[1]
        and ld_grid[0] == LINEAR_DECAY_BOX[0]
        and ld_grid[-1] == LINEAR_DECAY_BOX[1],
        f"count={len(grid_points)}, unique={len(set(grid_points))}",
    )
    check(
        "completed-sector target readout consumed by the sweep matches the note's listed triple",
        float(np.max(np.abs(z_min - EXPECTED_Z_MIN))) < 1.0e-12,
        f"max target drift={float(np.max(np.abs(z_min - EXPECTED_Z_MIN))):.3e}",
    )
    check(
        "gap_at satisfies the algebraic optimal-scalar projection identity at every grid point",
        max_projection_residual < 1.0e-12,
        f"max |zhat·(c_best zhat-Z_min)|={max_projection_residual:.3e}",
    )
    expected_audit_inputs = {
        "docs/GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_COMPLETED_TRIPLE_CURRENT_TRANSFER_FAMILY_BOUNDARY_NOTE_2026-04-19.md",
        "scripts/frontier_gauge_vacuum_plaquette_first_sector_completed_triple_current_transfer_family_boundary_2026_04_19.py",
        "scripts/frontier_gauge_vacuum_plaquette_first_sector_rank_one_transfer_realization_2026_04_19.py",
        "scripts/frontier_gauge_vacuum_plaquette_first_three_sample_environment_evaluator_route_2026_04_17.py",
        "scripts/frontier_gauge_vacuum_plaquette_first_three_sample_local_wilson_retained_positive_cone_obstruction_2026_04_17.py",
        "scripts/frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_2026_04_17.py",
    }
    check(
        "dependency manifest pins the source note and complete five-helper import closure",
        set(AUDIT_INPUT_PATHS) == expected_audit_inputs
        and all(os.path.isfile(os.path.join(ROOT, path)) for path in AUDIT_INPUT_PATHS),
        f"declared inputs={len(AUDIT_INPUT_PATHS)}",
    )
    check(
        "all 1440 runner-evaluated gaps are finite and above the numerical-zero threshold",
        bool(np.all(np.isfinite(gaps)))
        and bool(np.all(gaps > NUMERICAL_ZERO_THRESHOLD)),
        f"min gap={min_gap:.12e}, threshold={NUMERICAL_ZERO_THRESHOLD:.1e}",
    )
    check(
        "computed sampled argmin and minimum reproduce the finite-grid regression pins",
        min_pt == expected_min_pt
        and abs(min_gap - EXPECTED_MIN_GAP) < 5.0e-10,
        f"argmin={min_pt}, min gap={min_gap:.12e}",
    )

    print()
    print(" Honest scope of this certificate:")
    print(f"   - On the explicit {total}-point Cartesian grid, every float64 gap_at")
    print(f"     result is finite and greater than {NUMERICAL_ZERO_THRESHOLD:.1e}.")
    print(f"   - The dense grid is NOT a symbolic / interval-arithmetic global")
    print(f"     certificate, even at the sampled coordinates; exact-arithmetic and")
    print(f"     unsampled continuous-family statements remain outside this claim.")
    print(f"   - The finite numerical result is the exhaustive runner predicate above,")
    print(f"     including its explicit threshold and optimal-scalar projection check.")
    print()

    print("=" * 80)
    print(f" SUMMARY: PASS={PASS}, FAIL={FAIL}")
    print("=" * 80)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
