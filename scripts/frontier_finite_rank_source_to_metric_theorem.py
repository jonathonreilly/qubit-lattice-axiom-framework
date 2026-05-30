#!/usr/bin/env python3
"""Self-contained finite-rank source-to-metric finite-lattice certificate.

This runner intentionally avoids SourceFileLoader/helper-wrapper imports for
the finite-rank source, Schur boundary-action, and coarse radial metric checks.
The claim is finite and bounded: a fixed lattice construction closes the
source-to-exterior algebra and gives a strongly reduced scalar/static
isotropic residual. It does not prove full tensorial `3+1` matching or full GR.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.ndimage import map_coordinates
from scipy.sparse.linalg import spsolve


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
QUEUE = ROOT / "docs/audit/data/audit_queue.json"
CLAIM_ID = "finite_rank_source_to_metric_theorem_note"
RUNNER_PATH = "scripts/frontier_finite_rank_source_to_metric_theorem.py"


@dataclass
class Check:
    name: str
    ok: bool
    detail: str
    status: str


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str, status: str = "EXACT") -> None:
    CHECKS.append(Check(name=name, ok=ok, detail=detail, status=status))
    tag = "PASS" if ok else "FAIL"
    print(f"[{status}] {tag}: {name}")
    if detail:
        print(f"    {detail}")


def build_neg_laplacian_sparse(size: int) -> tuple[sparse.csr_matrix, int]:
    interior = size - 2
    n = interior * interior * interior
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


def full_from_flat(idx: int, interior: int) -> tuple[int, int, int]:
    i = idx // (interior * interior)
    rem = idx % (interior * interior)
    j = rem // interior
    k = rem % interior
    return i + 1, j + 1, k + 1


def flat_from_full(i: int, j: int, k: int, interior: int) -> int:
    return flat_idx(i - 1, j - 1, k - 1, interior)


def support_projector(n: int, support: list[int]) -> np.ndarray:
    p = np.zeros((n, len(support)))
    for col, site in enumerate(support):
        p[site, col] = 1.0
    return p


def solve_columns(matrix: sparse.spmatrix, support: list[int]) -> np.ndarray:
    cols = []
    for site in support:
        rhs = np.zeros(matrix.shape[0])
        rhs[site] = 1.0
        cols.append(spsolve(matrix, rhs))
    return np.column_stack(cols)


def finite_rank_setup():
    size = 15
    h0, interior = build_neg_laplacian_sparse(size)
    center = interior // 2
    support = [
        flat_idx(center, center, center, interior),
        flat_idx(center + 1, center, center, interior),
        flat_idx(center - 1, center, center, interior),
        flat_idx(center, center + 1, center, interior),
        flat_idx(center, center - 1, center, interior),
        flat_idx(center, center, center + 1, interior),
        flat_idx(center, center, center - 1, interior),
    ]
    g0p = solve_columns(h0, support)
    gs = g0p[support, :]

    base = np.array([0.11, 0.08, 0.08, 0.075, 0.075, 0.07, 0.07])
    d = np.diag(np.sqrt(base / np.diag(gs)))
    corr = np.eye(len(support)) + 0.18 * np.ones((len(support), len(support)))
    w_raw = d @ corr @ d

    rho = max(abs(ev) for ev in np.linalg.eigvals(w_raw @ gs))
    w = (0.45 / rho) * w_raw
    masses = np.array([1.0, 0.82, 0.77, 0.73, 0.69, 0.64, 0.61])
    return size, h0, interior, support, g0p, gs, w, masses


def exact_finite_rank_field():
    size, h0, interior, support, g0p, gs, w, masses = finite_rank_setup()
    p = support_projector(h0.shape[0], support)
    full = solve_columns(h0 - sparse.csr_matrix(p @ w @ p.T), support)
    formula = g0p @ np.linalg.inv(np.eye(w.shape[0]) - w @ gs)
    err_cols = float(np.max(np.abs(full - formula)))
    record(
        "finite-rank column identity",
        err_cols < 1e-12,
        f"max column error={err_cols:.3e}, support size={len(support)}",
    )

    phi_exact = full @ masses
    q_eff = np.linalg.solve(np.eye(w.shape[0]) - w @ gs, masses)
    phi_formula = g0p @ q_eff
    err_phi = float(np.max(np.abs(phi_exact - phi_formula)))
    record(
        "finite-rank compressed source",
        err_phi < 1e-12,
        f"max field error={err_phi:.3e}, q_eff_sum={np.sum(q_eff):.8f}",
    )

    residual = h0 @ phi_formula
    mask = np.ones(h0.shape[0], dtype=bool)
    mask[support] = False
    ext_res = float(np.max(np.abs(residual[mask])))
    record(
        "finite-rank exterior harmonicity outside support",
        ext_res < 5e-12,
        f"max exterior residual={ext_res:.3e}",
    )

    grid = np.zeros((size, size, size))
    grid[1:-1, 1:-1, 1:-1] = phi_formula.reshape((interior, interior, interior))
    return grid, support, interior, q_eff


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


def exterior_sets(size: int, cutoff_radius: float) -> tuple[np.ndarray, np.ndarray]:
    radii = radii_grid(size)
    ext_full = np.zeros((size, size, size), dtype=bool)
    ext_full[1:-1, 1:-1, 1:-1] = radii[1:-1, 1:-1, 1:-1] > cutoff_radius + 1e-12

    interior = size - 2
    trace: list[int] = []
    bulk: list[int] = []
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            for k in range(1, size - 1):
                if not ext_full[i, j, k]:
                    continue
                is_trace = False
                for di, dj, dk in [
                    (1, 0, 0),
                    (-1, 0, 0),
                    (0, 1, 0),
                    (0, -1, 0),
                    (0, 0, 1),
                    (0, 0, -1),
                ]:
                    if not ext_full[i + di, j + dj, k + dk]:
                        is_trace = True
                        break
                idx = flat_from_full(i, j, k, interior)
                if is_trace:
                    trace.append(idx)
                else:
                    bulk.append(idx)
    return np.array(trace, dtype=int), np.array(bulk, dtype=int)


def schur_dtn_matrix(size: int, cutoff_radius: float):
    trace_idx, bulk_idx = exterior_sets(size, cutoff_radius)
    h0, interior = build_neg_laplacian_sparse(size)

    h_tt = h0[trace_idx][:, trace_idx].toarray()
    if bulk_idx.size:
        h_tb = h0[trace_idx][:, bulk_idx].toarray()
        h_bt = h0[bulk_idx][:, trace_idx].toarray()
        h_bb = h0[bulk_idx][:, bulk_idx].tocsr()
        x = spsolve(h_bb, h_bt)
        lam = h_tt - h_tb @ x
    else:
        lam = h_tt
    return lam, trace_idx, bulk_idx, interior


def trace_values_from_grid(grid: np.ndarray, trace_idx: np.ndarray, interior: int) -> np.ndarray:
    vals = np.zeros(trace_idx.shape[0], dtype=float)
    for row, idx in enumerate(trace_idx):
        i, j, k = full_from_flat(int(idx), interior)
        vals[row] = float(grid[i, j, k])
    return vals


def harmonic_extension_from_trace(
    trace_vals: np.ndarray, trace_idx: np.ndarray, bulk_idx: np.ndarray, size: int
) -> np.ndarray:
    h0, interior = build_neg_laplacian_sparse(size)
    if bulk_idx.size:
        a = h0[bulk_idx][:, bulk_idx].tocsr()
        b = h0[bulk_idx][:, trace_idx].tocsr()
        bulk_sol = spsolve(a, -(b @ trace_vals))
    else:
        bulk_sol = np.zeros(0, dtype=float)

    interior_vec = np.zeros(h0.shape[0], dtype=float)
    interior_vec[trace_idx] = trace_vals
    if bulk_idx.size:
        interior_vec[bulk_idx] = bulk_sol

    grid = np.zeros((size, size, size), dtype=float)
    grid[1:-1, 1:-1, 1:-1] = interior_vec.reshape((interior, interior, interior))
    return grid


def trace_flux_from_extension(ext_grid: np.ndarray, trace_idx: np.ndarray, interior: int) -> np.ndarray:
    sigma = full_neg_laplacian(ext_grid)
    vals = np.zeros(trace_idx.shape[0], dtype=float)
    for row, idx in enumerate(trace_idx):
        i, j, k = full_from_flat(int(idx), interior)
        vals[row] = float(sigma[i, j, k])
    return vals


def boundary_stationarity_report(phi_grid: np.ndarray):
    lam, trace_idx, bulk_idx, interior = schur_dtn_matrix(15, 4.0)
    ext = exterior_projector(phi_grid, 4.0)
    f = trace_values_from_grid(ext, trace_idx, interior)
    ext_rebuilt = harmonic_extension_from_trace(f, trace_idx, bulk_idx, ext.shape[0])
    j_trace = trace_flux_from_extension(ext_rebuilt, trace_idx, interior)
    grad = lam @ f - j_trace
    sym_err = float(np.max(np.abs(lam - lam.T)))
    min_eig = float(np.min(np.linalg.eigvalsh(0.5 * (lam + lam.T))))
    return {
        "rebuild_err": float(np.max(np.abs(ext_rebuilt - ext))),
        "flux_err": float(np.max(np.abs(lam @ f - j_trace))),
        "stationary_grad": float(np.max(np.abs(grad))),
        "sym_err": sym_err,
        "min_eig": min_eig,
        "trace_count": int(trace_idx.size),
        "bulk_count": int(bulk_idx.size),
    }


def shell_data(phi_grid: np.ndarray):
    size = phi_grid.shape[0]
    center = (size - 1) / 2.0
    shells: dict[int, list[float]] = {}
    radii: dict[int, float] = {}
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            for k in range(1, size - 1):
                dx = i - center
                dy = j - center
                dz = k - center
                d2 = int(dx * dx + dy * dy + dz * dz)
                if d2 <= 1 or d2 == 0:
                    continue
                shells.setdefault(d2, []).append(float(phi_grid[i, j, k]))
                radii[d2] = float(np.sqrt(d2))
    usable = sorted(d2 for d2, vals in shells.items() if len(vals) >= 6 and radii[d2] <= center - 1)
    return usable, radii, shells


def fit_radial_harmonic_projection(phi_grid: np.ndarray, r_match: float):
    usable, radii, shells = shell_data(phi_grid)
    d2s = [d2 for d2 in usable if radii[d2] >= r_match]
    r = np.array([radii[d2] for d2 in d2s], dtype=float)
    y = np.array([np.mean(shells[d2]) for d2 in d2s], dtype=float)
    a = float(np.linalg.lstsq((1.0 / r).reshape(-1, 1), y, rcond=None)[0][0])
    pred = a / r
    rel_rms = float(np.sqrt(np.mean((y - pred) ** 2)) / max(np.max(np.abs(y)), 1e-12))
    max_rel = float(np.max(np.abs(y - pred) / np.maximum(np.abs(y), 1e-12)))
    return a, rel_rms, max_rel


def interpolate_phi(phi_grid: np.ndarray, point: np.ndarray) -> float:
    center = (phi_grid.shape[0] - 1) / 2.0
    coords = np.array([[center + point[0]], [center + point[1]], [center + point[2]]], dtype=float)
    return float(map_coordinates(phi_grid, coords, order=3, mode="nearest")[0])


def metric_from_phi(phi: float) -> np.ndarray:
    psi = 1.0 + phi
    alpha = (1.0 - phi) / (1.0 + phi)
    return np.diag(np.array([-(alpha**2), psi**4, psi**4, psi**4], dtype=float))


def christoffel(metric_fn, point: np.ndarray, h: float = 0.05) -> np.ndarray:
    g = metric_fn(point)
    g_inv = np.linalg.inv(g)
    dg = np.zeros((4, 4, 4))
    for axis in range(1, 4):
        dp = point.copy()
        dm = point.copy()
        dp[axis - 1] += h
        dm[axis - 1] -= h
        dg[axis] = (metric_fn(dp) - metric_fn(dm)) / (2.0 * h)
    gamma = np.zeros((4, 4, 4))
    for lam_idx in range(4):
        for mu in range(4):
            for nu in range(4):
                total = 0.0
                for rho in range(4):
                    total += g_inv[lam_idx, rho] * (
                        dg[mu, rho, nu] + dg[nu, rho, mu] - dg[rho, mu, nu]
                    )
                gamma[lam_idx, mu, nu] = 0.5 * total
    return gamma


def dgamma(metric_fn, point: np.ndarray, axis: int, h: float = 0.05) -> np.ndarray:
    if axis == 0:
        return np.zeros((4, 4, 4))
    dp = point.copy()
    dm = point.copy()
    dp[axis - 1] += h
    dm[axis - 1] -= h
    return (christoffel(metric_fn, dp, h) - christoffel(metric_fn, dm, h)) / (2.0 * h)


def einstein_tensor(metric_fn, point: np.ndarray, h: float = 0.05) -> np.ndarray:
    g = metric_fn(point)
    g_inv = np.linalg.inv(g)
    gamma = christoffel(metric_fn, point, h)
    dgammas = np.zeros((4, 4, 4, 4))
    for axis in range(1, 4):
        dgammas[axis] = dgamma(metric_fn, point, axis, h)

    ricci = np.zeros((4, 4))
    for mu in range(4):
        for nu in range(4):
            term1 = term2 = term3 = term4 = 0.0
            for lam_idx in range(4):
                term1 += dgammas[lam_idx, lam_idx, mu, nu]
                term2 += dgammas[nu, lam_idx, mu, lam_idx]
                trace_lam = sum(gamma[rho, lam_idx, rho] for rho in range(4))
                term3 += gamma[lam_idx, mu, nu] * trace_lam
                for rho in range(4):
                    term4 += gamma[rho, mu, lam_idx] * gamma[lam_idx, nu, rho]
            ricci[mu, nu] = term1 - term2 + term3 - term4
    scalar = float(np.sum(g_inv * ricci))
    return ricci - 0.5 * g * scalar


def probe_points(r_match: float) -> list[np.ndarray]:
    return [
        np.array([r_match, 0.0, 0.0]),
        np.array([r_match / np.sqrt(2.0), r_match / np.sqrt(2.0), 0.0]),
        np.array([r_match / np.sqrt(3.0)] * 3),
    ]


def residual_at_radius(phi_grid: np.ndarray, r_match: float, a: float) -> tuple[float, float]:
    def direct_metric(point: np.ndarray) -> np.ndarray:
        return metric_from_phi(interpolate_phi(phi_grid, point))

    def coarse_metric(point: np.ndarray) -> np.ndarray:
        r = max(np.linalg.norm(point), 1e-12)
        return metric_from_phi(a / r)

    direct_vals = []
    coarse_vals = []
    for point in probe_points(r_match):
        direct_vals.append(float(np.max(np.abs(einstein_tensor(direct_metric, point)))))
        coarse_vals.append(float(np.max(np.abs(einstein_tensor(coarse_metric, point)))))
    return max(direct_vals), max(coarse_vals)


def coarse_metric_report(phi_grid: np.ndarray):
    rows = []
    for r_match in [3.0, 3.5, 4.0, 4.5, 5.0]:
        a, rel_rms, max_rel = fit_radial_harmonic_projection(phi_grid, r_match)
        direct_res, coarse_res = residual_at_radius(phi_grid, r_match, a)
        rows.append((r_match, a, rel_rms, max_rel, direct_res, coarse_res))
    best = min(rows, key=lambda row: row[5])
    return rows, best, float(best[4] / max(best[5], 1e-15))


def audit_metadata_checks() -> None:
    if not LEDGER.exists() or not QUEUE.exists():
        return
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    row = ledger["rows"][CLAIM_ID]
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))["queue"]
    queue_entry = next((entry for entry in queue if entry["claim_id"] == CLAIM_ID), None)

    print("\nAUDIT METADATA")
    record("claim type remains bounded_theorem", row.get("claim_type") == "bounded_theorem", row.get("claim_type", ""), "META")
    record("audit status reset for re-audit", row.get("audit_status") == "unaudited", row.get("audit_status", ""), "META")
    record("effective status reset for re-audit", row.get("effective_status") == "unaudited", row.get("effective_status", ""), "META")
    record("runner path is registered", row.get("runner_path") == RUNNER_PATH, row.get("runner_path", ""), "META")
    record("direct dependency list is empty", row.get("deps") == [], str(row.get("deps")), "META")
    record("helper runner paths are empty", row.get("helper_runner_paths") == [], str(row.get("helper_runner_paths")), "META")
    record("open dependency paths are empty", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")), "META")
    record("queue entry is ready", queue_entry is not None and queue_entry.get("ready") is True, str(queue_entry), "META")


def main() -> int:
    print("FINITE-RANK SOURCE-TO-METRIC SELF-CONTAINED FINITE-LATTICE CERTIFICATE")
    print("=" * 78)

    phi_grid, support, _interior, q_eff = exact_finite_rank_field()
    print(f"support size={len(support)}, q_eff_sum={np.sum(q_eff):.8f}")

    boundary = boundary_stationarity_report(phi_grid)
    record(
        "Schur DtN matrix is symmetric positive on the exterior shell",
        boundary["sym_err"] < 1e-12 and boundary["min_eig"] > 0.0,
        (
            f"trace={boundary['trace_count']}, bulk={boundary['bulk_count']}, "
            f"sym_err={boundary['sym_err']:.3e}, min_eig={boundary['min_eig']:.6e}"
        ),
    )
    record(
        "finite-rank shell trace is recovered by exterior Dirichlet extension",
        boundary["rebuild_err"] < 1e-12,
        f"boundary reconstruction error={boundary['rebuild_err']:.3e}",
    )
    record(
        "finite-rank shell trace is stationary for the Schur boundary action",
        boundary["flux_err"] < 1e-12 and boundary["stationary_grad"] < 1e-12,
        f"flux_err={boundary['flux_err']:.3e}, stationary_grad={boundary['stationary_grad']:.3e}",
    )

    rows, best, improvement = coarse_metric_report(phi_grid)
    print("\nfinite-rank radial projection scan:")
    for row in rows:
        print(
            f"  R_match={row[0]:.1f}  a={row[1]:.6f}  shell_rms={row[2]:.3f}  "
            f"shell_max_rel={row[3]:.3f}  direct={row[4]:.3e}  coarse={row[5]:.3e}"
        )
    record(
        "finite-rank family admits a vacuum-close coarse radial isotropic metric",
        best[5] < 1e-5,
        f"R_match={best[0]:.1f}, a={best[1]:.6f}, shell_rms={best[2]:.3f}, coarse={best[5]:.3e}",
        "BOUNDED",
    )
    record(
        "coarse radial isotropic candidate strongly improves the direct same-source residual",
        best[4] > 1e-3 and improvement > 1e3,
        f"direct={best[4]:.3e}, coarse={best[5]:.3e}, improvement={improvement:.1f}x",
        "BOUNDED",
    )
    record(
        "direct same-source residual remains nonzero, so tensorial completion is still open",
        best[4] > 1e-3,
        f"direct residual={best[4]:.3e}",
        "BOUNDARY",
    )

    audit_metadata_checks()

    print("\n" + "=" * 78)
    print("BOUNDARY")
    print("=" * 78)
    print(
        "The row proves no full tensorial `3+1` matching law and no full nonlinear GR. "
        "It is a fixed finite-lattice source-to-exterior plus scalar/static "
        "isotropic residual certificate."
    )

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    n_pass = sum(c.ok for c in CHECKS)
    n_fail = sum(not c.ok for c in CHECKS)
    print(f"PASS={n_pass} FAIL={n_fail} TOTAL={len(CHECKS)}")
    exact = sum(1 for c in CHECKS if c.status == "EXACT")
    bounded = sum(1 for c in CHECKS if c.status == "BOUNDED")
    meta = sum(1 for c in CHECKS if c.status == "META")
    print(f"EXACT={exact} BOUNDED={bounded} META={meta}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
