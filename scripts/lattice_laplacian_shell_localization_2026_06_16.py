#!/usr/bin/env python3
"""Standalone Z^3 lattice-Laplacian shell-localization checks.

This runner intentionally does not import any repo frontier/helper module.
It builds the centered finite Dirichlet box, the nearest-neighbor negative
Laplacian, the seven star-support Green columns, the exterior truncation
Pi_R^ext, and the induced shell source sigma_R = H Pi_R^ext phi.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np


SIZE = 15
R_CUTOFF = 4.0
TOL = 1e-11
STAR = [
    (0, 0, 0),
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]
NEIGHBORS = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]
ACTIVE_ORBITS = [(3, 2, 2), (3, 3, 0), (4, 1, 0), (4, 1, 1)]
ANCHOR_ORBIT = (3, 3, 0)


@dataclass
class Check:
    name: str
    ok: bool
    detail: str


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str) -> None:
    CHECKS.append(Check(name, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'}: {name}")
    if detail:
        print(f"  {detail}")


def flat_idx(i: int, j: int, k: int, interior: int) -> int:
    return i * interior * interior + j * interior + k


def build_neg_laplacian_dense(size: int) -> tuple[np.ndarray, np.ndarray, int]:
    interior = size - 2
    n = interior**3
    center = (size - 1) // 2
    H = np.zeros((n, n), dtype=float)
    rel_coords = np.zeros((n, 3), dtype=int)

    for i in range(interior):
        for j in range(interior):
            for k in range(interior):
                row = flat_idx(i, j, k, interior)
                full = np.array([i + 1, j + 1, k + 1], dtype=int)
                rel_coords[row] = full - center
                H[row, row] = 6.0
                for di, dj, dk in NEIGHBORS:
                    ni, nj, nk = i + di, j + dj, k + dk
                    if 0 <= ni < interior and 0 <= nj < interior and 0 <= nk < interior:
                        H[row, flat_idx(ni, nj, nk, interior)] = -1.0
    return H, rel_coords, interior


def star_indices(interior: int) -> list[int]:
    c = interior // 2
    return [flat_idx(c + x, c + y, c + z, interior) for x, y, z in STAR]


def inflate(vec: np.ndarray, size: int, interior: int) -> np.ndarray:
    grid = np.zeros((size, size, size), dtype=float)
    grid[1:-1, 1:-1, 1:-1] = vec.reshape((interior, interior, interior))
    return grid


def flatten_interior(grid: np.ndarray) -> np.ndarray:
    return grid[1:-1, 1:-1, 1:-1].reshape(-1)


def d2_grid(size: int) -> np.ndarray:
    center = (size - 1) // 2
    i, j, k = np.mgrid[0:size, 0:size, 0:size]
    return (i - center) ** 2 + (j - center) ** 2 + (k - center) ** 2


def full_neg_laplacian(field: np.ndarray) -> np.ndarray:
    out = np.zeros_like(field)
    out[1:-1, 1:-1, 1:-1] = (
        6.0 * field[1:-1, 1:-1, 1:-1]
        - field[2:, 1:-1, 1:-1]
        - field[:-2, 1:-1, 1:-1]
        - field[1:-1, 2:, 1:-1]
        - field[1:-1, :-2, 1:-1]
        - field[1:-1, 1:-1, 2:]
        - field[1:-1, 1:-1, :-2]
    )
    return out


def exterior_projector(field: np.ndarray, cutoff: float) -> np.ndarray:
    return np.where(d2_grid(field.shape[0]) > cutoff * cutoff + 1e-12, field, 0.0)


def shell_mean_rows(field: np.ndarray, min_d2: int, max_d2: int | None = None) -> list[tuple[int, float]]:
    d2 = d2_grid(field.shape[0])
    rows = []
    for key in sorted(int(x) for x in np.unique(d2)):
        if key < min_d2:
            continue
        if max_d2 is not None and key > max_d2:
            continue
        mask = d2 == key
        if np.count_nonzero(mask) >= 6:
            rows.append((key, float(np.mean(field[mask]))))
    return rows


def profile_values(rows: list[tuple[int, float]]) -> np.ndarray:
    return np.array([v for _, v in rows], dtype=float)


def support_band(source: np.ndarray, tol: float = TOL) -> tuple[float, float, int]:
    d2 = d2_grid(source.shape[0])
    mask = np.abs(source) > tol
    radii = np.sqrt(d2[mask])
    return float(np.min(radii)), float(np.max(radii)), int(np.count_nonzero(mask))


def orbit_key(full_idx: tuple[int, int, int], center: int) -> tuple[int, int, int]:
    return tuple(sorted((abs(full_idx[0] - center), abs(full_idx[1] - center), abs(full_idx[2] - center)), reverse=True))


def grouped_points_by_d2(mask: np.ndarray) -> dict[int, list[tuple[int, int, int]]]:
    d2 = d2_grid(mask.shape[0])
    groups: dict[int, list[tuple[int, int, int]]] = {}
    for p in zip(*np.where(mask)):
        groups.setdefault(int(d2[p]), []).append(tuple(int(x) for x in p))
    return groups


def radial_average_on_support(source: np.ndarray, tol: float = TOL) -> np.ndarray:
    mask = np.abs(source) > tol
    out = np.zeros_like(source)
    for pts in grouped_points_by_d2(mask).values():
        avg = float(np.mean([source[p] for p in pts]))
        for p in pts:
            out[p] = avg
    return out


def shell_sums_on_support(source: np.ndarray, tol: float = TOL) -> dict[int, float]:
    mask = np.abs(source) > tol
    return {key: float(sum(source[p] for p in pts)) for key, pts in grouped_points_by_d2(mask).items()}


def orbit_sums(source: np.ndarray, tol: float = TOL) -> dict[tuple[int, int, int], float]:
    center = (source.shape[0] - 1) // 2
    out: dict[tuple[int, int, int], float] = {}
    for p in zip(*np.where(np.abs(source) > tol)):
        key = orbit_key(tuple(int(x) for x in p), center)
        out[key] = out.get(key, 0.0) + float(source[p])
    return out


def aligned_dict_values(dicts: list[dict], keys: Iterable) -> np.ndarray:
    keys = list(keys)
    return np.array([[d.get(k, 0.0) for k in keys] for d in dicts], dtype=float)


def max_column_spread(values: np.ndarray) -> float:
    ref = values[0]
    return float(np.max(np.abs(values - ref)))


def exterior_sets(size: int, interior: int, cutoff: float) -> tuple[np.ndarray, np.ndarray]:
    d2 = d2_grid(size)
    ext = d2 > cutoff * cutoff + 1e-12
    trace: list[int] = []
    bulk: list[int] = []
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            for k in range(1, size - 1):
                if not ext[i, j, k]:
                    continue
                is_trace = any(not ext[i + di, j + dj, k + dk] for di, dj, dk in NEIGHBORS)
                idx = flat_idx(i - 1, j - 1, k - 1, interior)
                if is_trace:
                    trace.append(idx)
                else:
                    bulk.append(idx)
    return np.array(trace, dtype=int), np.array(bulk, dtype=int)


def solve_exterior_dirichlet(
    H: np.ndarray,
    trace_values: np.ndarray,
    trace_idx: np.ndarray,
    bulk_idx: np.ndarray,
) -> np.ndarray:
    out = np.zeros((H.shape[0], trace_values.shape[1]), dtype=float)
    out[trace_idx, :] = trace_values
    if bulk_idx.size:
        A = H[np.ix_(bulk_idx, bulk_idx)]
        B = H[np.ix_(bulk_idx, trace_idx)]
        out[bulk_idx, :] = np.linalg.solve(A, -(B @ trace_values))
    return out


def main() -> None:
    print("Standalone lattice-Laplacian exterior/shell-localization runner")
    print(f"finite box: {SIZE}^3, zero Dirichlet boundary, R={R_CUTOFF}")
    print("=" * 72)

    H, rel_coords, interior = build_neg_laplacian_dense(SIZE)
    n = H.shape[0]
    support = star_indices(interior)
    rhs = np.zeros((n, len(STAR)), dtype=float)
    for col, idx in enumerate(support):
        rhs[idx, col] = 1.0
    green = np.linalg.solve(H, rhs)
    green_grids = [inflate(green[:, i], SIZE, interior) for i in range(len(STAR))]

    # Adjoint certificate for the proof: shell indicators outside the star
    # induce O_h-invariant potentials that are harmonic on the seven-site star.
    d2_rel = np.sum(rel_coords * rel_coords, axis=1)
    shell_keys = sorted(int(x) for x in np.unique(d2_rel) if 1 < x <= (SIZE // 2 - 1) ** 2)
    shell_rhs = np.column_stack([(d2_rel == key).astype(float) for key in shell_keys])
    shell_potentials = np.linalg.solve(H, shell_rhs)
    star_vals = shell_potentials[support, :]
    adjoint_star_spread = float(np.max(np.abs(star_vals - star_vals[0:1, :])))
    record(
        "adjoint shell potentials are constant on the seven-site star",
        adjoint_star_spread < TOL,
        f"max star spread over {len(shell_keys)} shell indicators = {adjoint_star_spread:.3e}",
    )

    # Raw Green shell means.
    raw_rows = [shell_mean_rows(grid, min_d2=2, max_d2=(SIZE // 2 - 1) ** 2) for grid in green_grids]
    raw_matrix = np.vstack([profile_values(rows) for rows in raw_rows])
    raw_spread = max_column_spread(raw_matrix)
    centered_profile = raw_matrix[0]
    row_map = np.vstack([profile_values(rows) for rows in raw_rows]).T
    singular = np.linalg.svd(row_map, compute_uv=False)
    rank_tail = float(singular[1] if singular.size > 1 else 0.0)
    record(
        "all seven point-Green columns have identical shell-mean profiles",
        raw_spread < TOL,
        f"max profile spread = {raw_spread:.3e}; rank-one tail singular value = {rank_tail:.3e}",
    )
    diff_basis = np.eye(len(STAR))[:, 1:] - np.eye(len(STAR))[:, [0]]
    killed = row_map @ diff_basis
    record(
        "shell-mean quotient kills the six zero-total-charge star modes",
        float(np.max(np.abs(killed))) < TOL,
        f"max quotient image of e_i - e_0 = {float(np.max(np.abs(killed))):.3e}",
    )

    # Exterior projector and shell source.
    ext_grids = [exterior_projector(grid, R_CUTOFF) for grid in green_grids]
    sigma_grids = [full_neg_laplacian(grid) for grid in ext_grids]
    sigma = np.column_stack([flatten_interior(grid) for grid in sigma_grids])
    reconstructed = np.linalg.solve(H, sigma)
    rec_err = float(np.max(np.abs(reconstructed - np.column_stack([flatten_interior(g) for g in ext_grids]))))
    record(
        "Pi_R^ext Green columns reconstruct exactly from sigma_R = H Pi_R^ext G",
        rec_err < TOL,
        f"max reconstruction error = {rec_err:.3e}",
    )

    trace_idx, bulk_idx = exterior_sets(SIZE, interior, R_CUTOFF)
    trace_values = green[trace_idx, :]
    dtn_ext = solve_exterior_dirichlet(H, trace_values, trace_idx, bulk_idx)
    dtn_err = float(np.max(np.abs(dtn_ext - np.column_stack([flatten_interior(g) for g in ext_grids]))))
    record(
        "Pi_R^ext Green columns equal the unique exterior Dirichlet extensions of their traces",
        dtn_err < TOL,
        f"trace nodes = {trace_idx.size}, bulk nodes = {bulk_idx.size}, max mismatch = {dtn_err:.3e}",
    )

    bands = [support_band(grid) for grid in sigma_grids]
    band_ok = all(lo > R_CUTOFF - 1.0 and hi <= R_CUTOFF + 1.0 + 1e-12 for lo, hi, _ in bands)
    record(
        "sigma_R is localized to the nearest-neighbor sewing band R-1 < r <= R+1",
        band_ok,
        "bands = " + ", ".join(f"[{lo:.6f}, {hi:.6f}]/{cnt}" for lo, hi, cnt in bands),
    )

    charges = np.array([float(np.sum(grid)) for grid in sigma_grids])
    charge_spread = float(np.max(np.abs(charges - 1.0)))
    record(
        "each point-column shell source carries unit total charge",
        charge_spread < TOL,
        f"charges = {np.array2string(charges, precision=15)}, max |Q-1| = {charge_spread:.3e}",
    )

    radial_dicts = [shell_sums_on_support(grid) for grid in sigma_grids]
    radial_keys = sorted(set().union(*(d.keys() for d in radial_dicts)))
    radial = aligned_dict_values(radial_dicts, radial_keys) / charges[:, None]
    radial_spread = max_column_spread(radial)
    record(
        "all seven point columns induce the same normalized radial DtN shell kernel",
        radial_spread < TOL,
        f"radii^2 = {radial_keys}; max normalized spread = {radial_spread:.3e}",
    )

    sigma_rad_grids = [radial_average_on_support(grid) for grid in sigma_grids]
    delta_grids = [grid - rad for grid, rad in zip(sigma_grids, sigma_rad_grids)]
    delta_charges = np.array([float(np.sum(grid)) for grid in delta_grids])
    record(
        "anisotropic remainder has zero total charge",
        float(np.max(np.abs(delta_charges))) < TOL,
        f"max |sum(delta_sigma)| = {float(np.max(np.abs(delta_charges))):.3e}",
    )

    orbit_dicts = [orbit_sums(grid) for grid in delta_grids]
    orbit_keys = sorted(set().union(*(d.keys() for d in orbit_dicts)), reverse=True)
    orbit = aligned_dict_values(orbit_dicts, orbit_keys) / charges[:, None]
    orbit_spread = max_column_spread(orbit)
    active = aligned_dict_values(orbit_dicts, ACTIVE_ORBITS) / charges[:, None]
    c_aniso = orbit_dicts[0].get(ANCHOR_ORBIT, 0.0) / charges[0]
    record(
        "all seven point columns induce the same normalized anisotropic orbit mode",
        orbit_spread < TOL,
        f"max normalized orbit spread = {orbit_spread:.3e}; c_aniso = {c_aniso:.15f}",
    )
    active_pattern_err = max(abs(active[0, 0] + active[0, 2]), abs(active[0, 1] + active[0, 3]))
    record(
        "active orbit vector matches the reduced one-parameter pattern",
        max_column_spread(active) < TOL and active_pattern_err < TOL,
        "active/Q = "
        + np.array2string(active[0], precision=15)
        + f"; anchor = {c_aniso:.15f}; pair-cancellation err = {active_pattern_err:.3e}",
    )

    delta = np.column_stack([flatten_interior(grid) for grid in delta_grids])
    phi_shell = reconstructed
    phi_aniso = np.linalg.solve(H, delta)
    phi_shell_grids = [inflate(phi_shell[:, i], SIZE, interior) for i in range(len(STAR))]
    phi_aniso_grids = [inflate(phi_aniso[:, i], SIZE, interior) for i in range(len(STAR))]
    mean_shell = np.vstack([profile_values(shell_mean_rows(g, min_d2=26)) for g in phi_shell_grids]) / charges[:, None]
    mean_aniso = np.vstack([profile_values(shell_mean_rows(g, min_d2=26)) for g in phi_aniso_grids]) / charges[:, None]
    mean_shell_spread = max_column_spread(mean_shell)
    mean_aniso_spread = max_column_spread(mean_aniso)
    record(
        "shell-mean exterior responses are the same per unit charge",
        mean_shell_spread < TOL and mean_aniso_spread < TOL,
        f"total-field spread = {mean_shell_spread:.3e}; anisotropic-field spread = {mean_aniso_spread:.3e}",
    )

    weights = np.array([1.0, 0.82, 0.77, 0.73, 0.69, 0.64, 0.61], dtype=float)
    combo_sigma = sum(w * g for w, g in zip(weights, sigma_grids))
    combo_q = float(np.sum(combo_sigma))
    combo_rad = np.array([shell_sums_on_support(combo_sigma).get(k, 0.0) for k in radial_keys]) / combo_q
    combo_delta = combo_sigma - radial_average_on_support(combo_sigma)
    combo_orb = np.array([orbit_sums(combo_delta).get(k, 0.0) for k in ACTIVE_ORBITS]) / combo_q
    combo_rad_err = float(np.max(np.abs(combo_rad - radial[0])))
    combo_orb_err = float(np.max(np.abs(combo_orb - active[0])))
    record(
        "arbitrary star-supported sources factor through total charge on the reduced shell surface",
        combo_rad_err < TOL and combo_orb_err < TOL,
        f"Q = {combo_q:.12f}; radial err = {combo_rad_err:.3e}; active-orbit err = {combo_orb_err:.3e}",
    )

    zero_weights = np.array([6.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], dtype=float)
    zero_sigma = sum(w * g for w, g in zip(zero_weights, sigma_grids))
    zero_rad = np.array([shell_sums_on_support(zero_sigma).get(k, 0.0) for k in radial_keys])
    zero_delta = zero_sigma - radial_average_on_support(zero_sigma)
    zero_orb = np.array([orbit_sums(zero_delta).get(k, 0.0) for k in ACTIVE_ORBITS])
    zero_reduced = max(float(np.max(np.abs(zero_rad))), float(np.max(np.abs(zero_orb))))
    record(
        "the reduced shell map annihilates zero-total-charge star combinations",
        zero_reduced < TOL,
        f"max reduced zero-charge component = {zero_reduced:.3e}",
    )

    print("=" * 72)
    n_pass = sum(c.ok for c in CHECKS)
    n_fail = sum(not c.ok for c in CHECKS)
    print(f"TOTAL: PASS={n_pass} FAIL={n_fail}")
    if n_fail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
