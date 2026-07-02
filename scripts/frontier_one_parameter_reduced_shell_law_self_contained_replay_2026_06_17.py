#!/usr/bin/env python3
"""Self-contained replay for the one-parameter reduced sewing-shell law.

This runner is an audit-packet repair artifact for
ONE_PARAMETER_REDUCED_SHELL_LAW_NOTE.md.  It intentionally does not import the
five frontier helper modules used by the primary runner.  Instead it inlines
the finite lattice operators and source constructors that the proof consumes:

1. the finite Dirichlet negative Laplacian on the 15^3 box;
2. star-supported point-Green columns;
3. the admitted local O_h source-family comparator;
4. the broader finite-rank source-family comparator;
5. exterior projection, shell-source extraction, radial averaging, and
   shell-mean readout.

The scientific claim boundary is unchanged: this is a bounded replay on the
imported/reduced R=4 shell surface, not a retained gravity closure or nonlinear
Einstein/Regge theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ONE_PARAMETER_REDUCED_SHELL_LAW_NOTE.md"
RUNNER_NAME = Path(__file__).name


@dataclass
class Check:
    name: str
    ok: bool
    detail: str
    status: str


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str, status: str = "FINITE") -> None:
    CHECKS.append(Check(name=name, ok=ok, detail=detail, status=status))
    tag = "PASS" if ok else "FAIL"
    print(f"[{status}] {tag}: {name}")
    if detail:
        print(f"    {detail}")


STAR_COORDS = [
    np.array([0, 0, 0], dtype=int),
    np.array([1, 0, 0], dtype=int),
    np.array([-1, 0, 0], dtype=int),
    np.array([0, 1, 0], dtype=int),
    np.array([0, -1, 0], dtype=int),
    np.array([0, 0, 1], dtype=int),
    np.array([0, 0, -1], dtype=int),
]

ACTIVE_ORBITS = [
    (3, 2, 2),
    (3, 3, 0),
    (4, 1, 0),
    (4, 1, 1),
]
ANCHOR_ORBIT = (3, 3, 0)


def build_neg_laplacian_sparse(size: int) -> tuple[sparse.csr_matrix, int]:
    interior = size - 2
    n = interior**3
    ii, jj, kk = np.mgrid[0:interior, 0:interior, 0:interior]
    flat = ii.ravel() * interior * interior + jj.ravel() * interior + kk.ravel()

    rows = [flat]
    cols = [flat]
    vals = [np.full(n, 6.0)]
    for di, dj, dk in [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]:
        ni = ii + di
        nj = jj + dj
        nk = kk + dk
        mask = (
            (ni >= 0)
            & (ni < interior)
            & (nj >= 0)
            & (nj < interior)
            & (nk >= 0)
            & (nk < interior)
        )
        src = flat[mask.ravel()]
        dst = ni[mask] * interior * interior + nj[mask] * interior + nk[mask]
        rows.append(src)
        cols.append(dst.ravel())
        vals.append(-np.ones(src.shape[0]))

    return sparse.csr_matrix(
        (np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
        shape=(n, n),
    ), interior


def flat_idx(i: int, j: int, k: int, interior: int) -> int:
    return i * interior * interior + j * interior + k


def solve_columns(matrix: sparse.spmatrix, support: list[int]) -> np.ndarray:
    cols = []
    for site in support:
        rhs = np.zeros(matrix.shape[0])
        rhs[site] = 1.0
        cols.append(spsolve(matrix, rhs))
    return np.column_stack(cols)


def support_projector(n: int, support: list[int]) -> np.ndarray:
    projector = np.zeros((n, len(support)))
    for col, site in enumerate(support):
        projector[site, col] = 1.0
    return projector


def star_support(size: int) -> tuple[list[int], int]:
    _, interior = build_neg_laplacian_sparse(size)
    center = interior // 2
    support = [
        flat_idx(center + v[0], center + v[1], center + v[2], interior)
        for v in STAR_COORDS
    ]
    return support, interior


def build_point_green_columns(size: int) -> list[np.ndarray]:
    h0, interior = build_neg_laplacian_sparse(size)
    support, _ = star_support(size)
    columns = []
    for site in support:
        rhs = np.zeros(h0.shape[0])
        rhs[site] = 1.0
        col = spsolve(h0, rhs)
        grid = np.zeros((size, size, size))
        grid[1:-1, 1:-1, 1:-1] = col.reshape((interior, interior, interior))
        columns.append(grid)
    return columns


def build_adapted_basis() -> np.ndarray:
    e0 = np.zeros(7)
    e0[0] = 1.0
    px, mx, py, my, pz, mz = [np.eye(7)[i] for i in range(1, 7)]
    s = (px + mx + py + my + pz + mz) / np.sqrt(6.0)
    e1 = (px + mx - py - my) / 2.0
    e2 = (px + mx + py + my - 2.0 * pz - 2.0 * mz) / np.sqrt(12.0)
    tx = (px - mx) / np.sqrt(2.0)
    ty = (py - my) / np.sqrt(2.0)
    tz = (pz - mz) / np.sqrt(2.0)
    return np.column_stack([e0, s, e1, e2, tx, ty, tz])


BASIS = build_adapted_basis()


def build_commutant_operator(a: float, b: float, c: float, lam_e: float, lam_t: float) -> np.ndarray:
    block = np.array(
        [
            [a, c, 0.0, 0.0, 0.0, 0.0, 0.0],
            [c, b, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, lam_e, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, lam_e, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, lam_t, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, lam_t, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, lam_t],
        ]
    )
    return BASIS @ block @ BASIS.T


def build_best_oh_phi_grid() -> np.ndarray:
    """Replay the admitted local O_h source-family comparator.

    The numeric literals below are copied current source-family definitions from
    the previous helper path. They are not observational targets and are not
    derived here from the axiom surface.
    """
    size = 15
    h0, interior = build_neg_laplacian_sparse(size)
    support, _ = star_support(size)
    g0p = solve_columns(h0, support)
    gs = g0p[support, :]

    x1, x2, mix, lam_e, lam_t = 0.0698, 0.0499, -0.0070, 0.0642, 0.1056
    m0, ms = 0.8247, 0.2271
    w = build_commutant_operator(x1, x2, mix, lam_e, lam_t)
    masses = np.zeros(7)
    masses[0] = m0
    masses[1:] = ms
    q_eff = np.linalg.solve(np.eye(7) - w @ gs, masses)
    phi_flat = g0p @ q_eff

    phi_grid = np.zeros((size, size, size))
    phi_grid[1:-1, 1:-1, 1:-1] = phi_flat.reshape((interior, interior, interior))

    center = interior // 2
    support_points = [
        (center + v[0] + 1, center + v[1] + 1, center + v[2] + 1)
        for v in STAR_COORDS
    ]
    phi_max = max(float(phi_grid[idx]) for idx in support_points)
    phi_grid *= 0.35 / phi_max
    return phi_grid


def finite_rank_setup() -> tuple[int, sparse.csr_matrix, int, list[int], np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Replay the admitted finite-rank source-family comparator.

    The base, correlation, scale, and mass literals are source-family
    definitions copied into the replay for inspectability. They are support
    comparators, not fitted observations or retained selector theorems.
    """
    size = 15
    h0, interior = build_neg_laplacian_sparse(size)
    support, _ = star_support(size)
    g0p = solve_columns(h0, support)
    gs = g0p[support, :]

    base = np.array([0.11, 0.08, 0.08, 0.075, 0.075, 0.07, 0.07])
    diag_gs = np.diag(gs)
    d = np.diag(np.sqrt(base / diag_gs))
    corr = np.eye(len(support)) + 0.18 * np.ones((len(support), len(support)))
    w_raw = d @ corr @ d

    eigvals = np.linalg.eigvals(w_raw @ gs)
    rho = max(abs(ev) for ev in eigvals)
    w = (0.45 / rho) * w_raw

    masses = np.array([1.0, 0.82, 0.77, 0.73, 0.69, 0.64, 0.61])
    return size, h0, interior, support, g0p, gs, w, masses


def build_finite_rank_phi_grid() -> np.ndarray:
    size, h0, interior, support, _, _, w, masses = finite_rank_setup()
    p = support_projector(h0.shape[0], support)
    full = solve_columns(h0 - sparse.csr_matrix(p @ w @ p.T), support)
    phi_flat = full @ masses
    phi_grid = np.zeros((size, size, size))
    phi_grid[1:-1, 1:-1, 1:-1] = phi_flat.reshape((interior, interior, interior))
    return phi_grid


def full_neg_laplacian(field: np.ndarray) -> np.ndarray:
    lap = np.zeros_like(field)
    lap[1:-1, 1:-1, 1:-1] = (
        6.0 * field[1:-1, 1:-1, 1:-1]
        - field[2:, 1:-1, 1:-1]
        - field[:-2, 1:-1, 1:-1]
        - field[1:-1, 2:, 1:-1]
        - field[1:-1, :-2, 1:-1]
        - field[1:-1, 1:-1, 2:]
        - field[1:-1, 1:-1, :-2]
    )
    return lap


def radii_grid(size: int) -> np.ndarray:
    center = (size - 1) / 2.0
    i, j, k = np.mgrid[0:size, 0:size, 0:size]
    return np.sqrt((i - center) ** 2 + (j - center) ** 2 + (k - center) ** 2)


def exterior_projector(field: np.ndarray, cutoff_radius: float) -> np.ndarray:
    return np.where(radii_grid(field.shape[0]) > cutoff_radius + 1e-12, field, 0.0)


def solve_from_source(source_grid: np.ndarray) -> np.ndarray:
    size = source_grid.shape[0]
    h0, interior = build_neg_laplacian_sparse(size)
    rhs = source_grid[1:-1, 1:-1, 1:-1].reshape(-1)
    sol = spsolve(h0, rhs)
    out = np.zeros_like(source_grid)
    out[1:-1, 1:-1, 1:-1] = sol.reshape((interior, interior, interior))
    return out


def radial_average_shell(source_grid: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    size = source_grid.shape[0]
    center = (size - 1) / 2.0
    out = np.zeros_like(source_grid)
    groups: dict[int, list[tuple[int, int, int]]] = {}
    for i in range(size):
        for j in range(size):
            for k in range(size):
                if abs(source_grid[i, j, k]) > tol:
                    dx = i - center
                    dy = j - center
                    dz = k - center
                    d2 = int(dx * dx + dy * dy + dz * dz)
                    groups.setdefault(d2, []).append((i, j, k))
    for pts in groups.values():
        avg = float(np.mean([source_grid[p] for p in pts]))
        for p in pts:
            out[p] = avg
    return out


def orbit_key(i: int, j: int, k: int, size: int) -> tuple[int, int, int]:
    center = (size - 1) // 2
    return tuple(sorted([abs(i - center), abs(j - center), abs(k - center)], reverse=True))


def radial_profile(source_grid: np.ndarray) -> list[tuple[float, float]]:
    sigma_rad = radial_average_shell(source_grid)
    total_charge = float(np.sum(sigma_rad))
    size = source_grid.shape[0]
    center = (size - 1) / 2.0
    groups: dict[int, list[tuple[int, int, int]]] = {}
    for i in range(size):
        for j in range(size):
            for k in range(size):
                if abs(sigma_rad[i, j, k]) <= 1e-12:
                    continue
                d2 = int((i - center) ** 2 + (j - center) ** 2 + (k - center) ** 2)
                groups.setdefault(d2, []).append((i, j, k))
    rows = []
    for d2 in sorted(groups):
        shell_sum = float(np.sum([sigma_rad[p] for p in groups[d2]]))
        rows.append((float(np.sqrt(d2)), shell_sum / total_charge))
    return rows


def shell_mean_rows(field: np.ndarray, cutoff: float = 5.0) -> list[tuple[float, float]]:
    size = field.shape[0]
    center = (size - 1) / 2.0
    groups: dict[int, list[tuple[int, int, int]]] = {}
    for i in range(size):
        for j in range(size):
            for k in range(size):
                d2 = int((i - center) ** 2 + (j - center) ** 2 + (k - center) ** 2)
                groups.setdefault(d2, []).append((i, j, k))
    rows = []
    for d2 in sorted(groups):
        radius = float(np.sqrt(d2))
        if radius <= cutoff + 1e-12:
            continue
        vals = np.array([field[p] for p in groups[d2]], dtype=float)
        rows.append((radius, float(np.mean(vals))))
    return rows


def reduced_data(phi_grid: np.ndarray, shell_radius: float = 4.0) -> dict[str, object]:
    sigma = full_neg_laplacian(exterior_projector(phi_grid, shell_radius))
    sigma_rad = radial_average_shell(sigma)
    delta_sigma = sigma - sigma_rad
    phi_shell = solve_from_source(sigma)
    phi_aniso = solve_from_source(delta_sigma)

    size = sigma.shape[0]
    orbit_sums: dict[tuple[int, int, int], float] = {}
    for i in range(size):
        for j in range(size):
            for k in range(size):
                key = orbit_key(i, j, k, size)
                orbit_sums.setdefault(key, 0.0)
                orbit_sums[key] += float(delta_sigma[i, j, k])
    active = {k: v for k, v in orbit_sums.items() if abs(v) > 1e-12}

    total_charge = float(np.sum(sigma))
    anchor = active[ANCHOR_ORBIT]
    norm_orbit = {k: active[k] / total_charge for k in ACTIVE_ORBITS}
    mean_shell = [(r, m / total_charge) for r, m in shell_mean_rows(phi_shell)]
    mean_aniso = [(r, m / total_charge) for r, m in shell_mean_rows(phi_aniso)]
    return {
        "Q": total_charge,
        "anchor_per_Q": anchor / total_charge,
        "radial_profile": radial_profile(sigma),
        "norm_orbit": norm_orbit,
        "mean_shell": mean_shell,
        "mean_aniso": mean_aniso,
    }


def max_profile_diff(a: list[tuple[float, float]], b: list[tuple[float, float]]) -> float:
    if len(a) != len(b):
        return float("inf")
    out = 0.0
    for (ra, va), (rb, vb) in zip(a, b):
        out = max(out, abs(ra - rb), abs(va - vb))
    return out


def max_mode_diff(
    a: dict[tuple[int, int, int], float], b: dict[tuple[int, int, int], float]
) -> float:
    return max(abs(a[k] - b[k]) for k in ACTIVE_ORBITS)


def source_firewall_checks() -> None:
    note = NOTE.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    forbidden = [
        "_frontier" + "_loader",
        "load_" + "frontier",
        "import frontier" + "_",
        "from frontier" + "_",
    ]
    record(
        "source note registers this self-contained replay runner without status promotion",
        RUNNER_NAME in note
        and "self-contained reduced-shell replay" in note
        and "does not promote this row" in note,
        RUNNER_NAME,
        status="BOUNDED",
    )
    record(
        "self-contained replay source has no frontier-loader or helper-module imports",
        all(phrase not in source for phrase in forbidden),
        "forbidden loader/helper import strings absent",
        status="BOUNDED",
    )


def main() -> None:
    print("Self-contained one-parameter reduced sewing-shell replay")
    print("=" * 72)
    source_firewall_checks()

    columns = build_point_green_columns(15)
    point_data = [reduced_data(col) for col in columns]
    ref = point_data[0]

    point_charge_diff = max(abs(float(d["Q"]) - 1.0) for d in point_data)
    point_rad_diff = max(
        max_profile_diff(ref["radial_profile"], d["radial_profile"]) for d in point_data
    )
    point_mode_diff = max(
        max_mode_diff(ref["norm_orbit"], d["norm_orbit"]) for d in point_data
    )
    point_shell_diff = max(
        max_profile_diff(ref["mean_shell"], d["mean_shell"]) for d in point_data
    )
    point_aniso_diff = max(
        max_profile_diff(ref["mean_aniso"], d["mean_aniso"]) for d in point_data
    )
    c_aniso = float(ref["anchor_per_Q"])

    family_oh = reduced_data(build_best_oh_phi_grid())
    family_fr = reduced_data(build_finite_rank_phi_grid())
    families = [family_oh, family_fr]
    family_rad_diff = max(
        max_profile_diff(ref["radial_profile"], fam["radial_profile"]) for fam in families
    )
    family_mode_diff = max(
        max_mode_diff(ref["norm_orbit"], fam["norm_orbit"]) for fam in families
    )
    family_shell_diff = max(
        max_profile_diff(ref["mean_shell"], fam["mean_shell"]) for fam in families
    )
    family_aniso_diff = max(
        max_profile_diff(ref["mean_aniso"], fam["mean_aniso"]) for fam in families
    )
    family_c_diff = max(abs(float(fam["anchor_per_Q"]) - c_aniso) for fam in families)

    print(f"c_aniso = {c_aniso:.15f}")
    print(f"max point-column charge difference from unity = {point_charge_diff:.3e}")
    print(f"max point-column radial-profile difference = {point_rad_diff:.3e}")
    print(f"max point-column orbit-mode difference = {point_mode_diff:.3e}")
    print(f"max point-column shell-mean total-field difference = {point_shell_diff:.3e}")
    print(f"max point-column shell-mean anisotropic-field difference = {point_aniso_diff:.3e}")
    print(f"max family-vs-reference c_aniso difference = {family_c_diff:.3e}")

    record(
        "all seven point-Green columns carry unit total charge",
        point_charge_diff < 1e-12,
        f"max |Q-1| across columns = {point_charge_diff:.3e}",
    )
    record(
        "all seven point-Green columns induce the same radial shell kernel per unit charge",
        point_rad_diff < 1e-12,
        f"max radial-profile difference = {point_rad_diff:.3e}",
    )
    record(
        "all seven point-Green columns induce the same anisotropic orbit mode per unit charge",
        point_mode_diff < 1e-12,
        f"max orbit-mode difference = {point_mode_diff:.3e}",
    )
    record(
        "all seven point-Green columns induce the same shell-mean exterior response per unit charge",
        point_shell_diff < 1e-12 and point_aniso_diff < 1e-12,
        (
            f"max total-field difference = {point_shell_diff:.3e}, "
            f"max anisotropic-field difference = {point_aniso_diff:.3e}"
        ),
    )
    record(
        "the anisotropic anchor amplitude obeys A_aniso = c_aniso * Q with one computed finite-lattice constant",
        point_mode_diff < 1e-12 and point_charge_diff < 1e-12,
        f"c_aniso = {c_aniso:.15f}",
    )
    record(
        "self-contained c_aniso reproduces the registered reduced-shell constant",
        abs(c_aniso - 0.081435402995901) < 5e-16,
        f"c_aniso = {c_aniso:.15f}",
    )
    record(
        "the admitted local O_h and finite-rank source-family comparators satisfy the same one-parameter reduced shell law",
        family_rad_diff < 1e-12
        and family_mode_diff < 1e-12
        and family_shell_diff < 1e-12
        and family_aniso_diff < 1e-12
        and family_c_diff < 1e-12,
        (
            f"radial={family_rad_diff:.3e}, orbit={family_mode_diff:.3e}, "
            f"shell={family_shell_diff:.3e}, aniso={family_aniso_diff:.3e}, "
            f"c_diff={family_c_diff:.3e}"
        ),
    )
    record(
        "on the reduced surface the sewing-shell law behaves like one isotropic shell density plus one cubic shear mode tied to total charge",
        family_mode_diff < 1e-12 and family_c_diff < 1e-12,
        f"c_aniso = {c_aniso:.15f}",
        status="BOUNDED",
    )

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    n_pass = sum(c.ok for c in CHECKS)
    n_fail = sum(not c.ok for c in CHECKS)
    print(f"PASS={n_pass} FAIL={n_fail} TOTAL={len(CHECKS)}")
    if n_fail == 0:
        print("All checks passed.")
    else:
        print("Some checks failed.")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
