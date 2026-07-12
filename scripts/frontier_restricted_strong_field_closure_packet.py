#!/usr/bin/env python3
"""Self-contained restricted static-conformal finite-box closure certificate.

The load-bearing calculation in this runner has no frontier/helper imports and
does not start from the fitted benchmark field.  It constructs the finite
Dirichlet lattice operator, quantifies over the two basis directions of the
local O_h-invariant seven-star source space, and derives in order

    q -> phi -> phi_ext -> sigma -> u -> (psi, chi) -> (rho, S) -> (f, j).

In particular, the Schur source is j = sigma|Gamma, fixed before the boundary
action is evaluated.  It is not defined as Lambda f for a desired target f.

The certificate is a bounded finite-dimensional theorem.  It does not claim
that the framework's minimal axioms derive the Einstein equations, a physical
stress tensor, full tensorial 3+1 gravity, or a continuum limit.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh, splu, spsolve


SIZE = 15
INTERIOR = SIZE - 2
R_CUTOFF = 4.0
TOL = 2.0e-11
NEIGHBORS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
STAR = (
    (0, 0, 0),
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


@dataclass(frozen=True)
class Check:
    name: str
    ok: bool
    detail: str
    status: str


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str, status: str = "EXACT") -> None:
    CHECKS.append(Check(name, ok, detail, status))
    print(f"[{status}] {'PASS' if ok else 'FAIL'}: {name}")
    print(f"    {detail}")


def flat_idx(i: int, j: int, k: int) -> int:
    return i * INTERIOR * INTERIOR + j * INTERIOR + k


def full_from_flat(idx: int) -> tuple[int, int, int]:
    i = idx // (INTERIOR * INTERIOR)
    rem = idx % (INTERIOR * INTERIOR)
    j = rem // INTERIOR
    k = rem % INTERIOR
    return i + 1, j + 1, k + 1


def build_operator() -> sparse.csr_matrix:
    n = INTERIOR**3
    rows: list[int] = []
    cols: list[int] = []
    vals: list[float] = []
    for i, j, k in product(range(INTERIOR), repeat=3):
        row = flat_idx(i, j, k)
        rows.append(row)
        cols.append(row)
        vals.append(6.0)
        for di, dj, dk in NEIGHBORS:
            ni, nj, nk = i + di, j + dj, k + dk
            if 0 <= ni < INTERIOR and 0 <= nj < INTERIOR and 0 <= nk < INTERIOR:
                rows.append(row)
                cols.append(flat_idx(ni, nj, nk))
                vals.append(-1.0)
    return sparse.csr_matrix((vals, (rows, cols)), shape=(n, n))


def relative_coordinates() -> np.ndarray:
    center = (SIZE - 1) // 2
    coords = np.zeros((INTERIOR**3, 3), dtype=int)
    for idx in range(INTERIOR**3):
        i, j, k = full_from_flat(idx)
        coords[idx] = (i - center, j - center, k - center)
    return coords


COORDS = relative_coordinates()
RADII = np.linalg.norm(COORDS, axis=1)


def source_vector(q0: float, qs: float) -> np.ndarray:
    center = INTERIOR // 2
    source = np.zeros(INTERIOR**3, dtype=float)
    for arm, (di, dj, dk) in enumerate(STAR):
        source[flat_idx(center + di, center + dj, center + dk)] = q0 if arm == 0 else qs
    return source


def exterior_sets() -> tuple[np.ndarray, np.ndarray]:
    ext = RADII > R_CUTOFF + 1.0e-12
    trace: list[int] = []
    bulk: list[int] = []
    coord_to_idx = {tuple(coord): idx for idx, coord in enumerate(COORDS)}
    for idx, coord in enumerate(COORDS):
        if not ext[idx]:
            continue
        is_trace = any(
            not ext[coord_to_idx[tuple(coord + np.array(delta))]]
            for delta in NEIGHBORS
            if tuple(coord + np.array(delta)) in coord_to_idx
        )
        (trace if is_trace else bulk).append(idx)
    return np.asarray(trace, dtype=int), np.asarray(bulk, dtype=int)


def max_orbit_spread(field: np.ndarray) -> float:
    groups: dict[tuple[int, int, int], list[float]] = {}
    for coord, value in zip(COORDS, field):
        key = tuple(sorted((abs(int(coord[0])), abs(int(coord[1])), abs(int(coord[2])))))
        groups.setdefault(key, []).append(float(value))
    return max(float(np.ptp(values)) for values in groups.values())


def invariant_star_subspace_certificate() -> tuple[int, float, float]:
    """Enumerate O_h on the seven-star and certify its fixed subspace."""
    star = np.asarray(STAR, dtype=int)
    lookup = {tuple(coord): idx for idx, coord in enumerate(star)}
    representations: list[np.ndarray] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rep = np.zeros((7, 7), dtype=float)
            for col, coord in enumerate(star):
                mapped = tuple(signs[axis] * int(coord[perm[axis]]) for axis in range(3))
                rep[lookup[mapped], col] = 1.0
            representations.append(rep)

    invariant_projector = sum(representations) / len(representations)
    rank = int(np.linalg.matrix_rank(invariant_projector, tol=1.0e-12))
    basis = np.zeros((7, 2), dtype=float)
    basis[0, 0] = 1.0
    basis[1:, 1] = 1.0
    fixed_error = max(float(np.max(np.abs(rep @ basis - basis))) for rep in representations)
    basis_projector = basis @ np.linalg.inv(basis.T @ basis) @ basis.T
    projector_error = float(np.max(np.abs(invariant_projector - basis_projector)))
    return rank, fixed_error, projector_error


def schur_operator(h0: sparse.csr_matrix, trace: np.ndarray, bulk: np.ndarray) -> np.ndarray:
    h_tt = h0[trace][:, trace].toarray()
    h_tb = h0[trace][:, bulk].toarray()
    h_bt = h0[bulk][:, trace].toarray()
    h_bb = h0[bulk][:, bulk].tocsc()
    return h_tt - h_tb @ spsolve(h_bb, h_bt)


def analyze_source(
    label: str,
    q0: float,
    qs: float,
    h0: sparse.csr_matrix,
    hsolve,
    trace: np.ndarray,
    bulk: np.ndarray,
    lam: np.ndarray,
) -> dict[str, float]:
    microscopic_source = source_vector(q0, qs)
    phi = hsolve(microscopic_source)
    phi_ext = np.where(RADII > R_CUTOFF + 1.0e-12, phi, 0.0)
    sigma = h0 @ phi_ext

    shell = np.abs(sigma) > 2.0e-12
    shell_min = float(np.min(RADII[shell]))
    shell_max = float(np.max(RADII[shell]))
    charge_error = abs(float(np.sum(sigma) - np.sum(microscopic_source)))

    # Independent bridge solve.  The equality u=phi_ext is a consequence of
    # H u=sigma and invertibility; it is not assigned below.
    u = hsolve(sigma)
    bridge_error = float(np.max(np.abs(u - phi_ext)))
    amplitude = float(np.max(np.abs(u)))
    if amplitude >= 1.0:
        raise RuntimeError(f"{label}: bridge leaves the declared |u|<1 theorem domain")

    psi = 1.0 + u
    chi = 1.0 - u
    alpha = chi / psi
    rho = sigma / (2.0 * np.pi * psi**5)
    stress = 0.5 * rho * (1.0 / alpha - 1.0)
    first_residual = h0 @ u - 2.0 * np.pi * psi**5 * rho
    second_residual = h0 @ (-u) + 2.0 * np.pi * alpha * psi**5 * (rho + 2.0 * stress)

    # j is obtained from the already constructed microscopic shell source.
    # Since sigma vanishes in the harmonic bulk, block elimination must give
    # j=Lambda f.
    f = phi_ext[trace]
    j = sigma[trace]
    bulk_source = float(np.max(np.abs(sigma[bulk])))
    schur_flux_error = float(np.max(np.abs(lam @ f - j)))
    minimizer = np.linalg.solve(lam, j)
    minimizer_error = float(np.max(np.abs(minimizer - f)))

    rng = np.random.default_rng(1701)
    completion_error = 0.0
    minimum_gain = np.inf
    base_action = 0.5 * float(f @ (lam @ f)) - float(j @ f)
    for _ in range(4):
        delta = rng.normal(size=f.size)
        delta *= 1.0e-5 / np.linalg.norm(delta)
        trial = f + delta
        trial_action = 0.5 * float(trial @ (lam @ trial)) - float(j @ trial)
        exact_gain = 0.5 * float(delta @ (lam @ delta))
        minimum_gain = min(minimum_gain, trial_action - base_action)
        completion_error = max(completion_error, abs((trial_action - base_action) - exact_gain))

    return {
        "shell_min": shell_min,
        "shell_max": shell_max,
        "charge_error": charge_error,
        "bridge_error": bridge_error,
        "amplitude": amplitude,
        "orbit_phi": max_orbit_spread(phi),
        "orbit_sigma": max_orbit_spread(sigma),
        "first_residual": float(np.max(np.abs(first_residual))),
        "second_residual": float(np.max(np.abs(second_residual))),
        "bulk_source": bulk_source,
        "schur_flux_error": schur_flux_error,
        "minimizer_error": minimizer_error,
        "minimum_gain": float(minimum_gain),
        "completion_error": completion_error,
    }


def main() -> None:
    print("Self-contained restricted static-conformal finite-box closure")
    print("=" * 78)
    print("theorem source space: q=(q0,qs,qs,qs,qs,qs,qs), |H^-1 H Pi H^-1 Pq|_inf < 1")
    print("forbidden proof inputs: fitted benchmark parameters, observed targets, helper outputs")

    h0 = build_operator()
    hsolve = splu(h0.tocsc()).solve
    sym_error = float(np.max(np.abs((h0 - h0.T).data))) if (h0 - h0.T).nnz else 0.0
    min_h_eig = float(eigsh(h0, k=1, which="SA", return_eigenvectors=False)[0])
    record(
        "the finite Dirichlet nearest-neighbor operator is symmetric positive definite",
        sym_error < TOL and min_h_eig > 0.0,
        f"symmetry error={sym_error:.3e}, min eigenvalue={min_h_eig:.9e}",
    )

    trace, bulk = exterior_sets()
    lam = schur_operator(h0, trace, bulk)
    lam_sym_error = float(np.max(np.abs(lam - lam.T)))
    min_lam_eig = float(np.min(np.linalg.eigvalsh(0.5 * (lam + lam.T))))
    record(
        "the exact exterior Schur operator is symmetric positive definite",
        lam_sym_error < TOL and min_lam_eig > 0.0,
        f"trace={trace.size}, bulk={bulk.size}, symmetry error={lam_sym_error:.3e}, min eigenvalue={min_lam_eig:.9e}",
    )

    # The first two rows span the full O_h-invariant source space; the other
    # rows are deterministic signed-mixture stress tests, not fitted targets.
    sources = (
        ("center basis", 0.20, 0.00),
        ("six-arm invariant basis", 0.00, 0.03),
        ("positive mixture", 0.14, 0.02),
        ("signed mixture A", 0.08, -0.01),
        ("signed mixture B", -0.05, 0.025),
    )
    reports = [analyze_source(name, q0, qs, h0, hsolve, trace, bulk, lam) for name, q0, qs in sources]
    for (name, q0, qs), report in zip(sources, reports):
        print(
            f"{name:26s} q=({q0:+.3f},{qs:+.3f}) "
            f"band=[{report['shell_min']:.6f},{report['shell_max']:.6f}] "
            f"bridge={report['bridge_error']:.3e} constraints="
            f"({report['first_residual']:.3e},{report['second_residual']:.3e}) "
            f"Schur={report['schur_flux_error']:.3e}"
        )

    invariant_rank, fixed_error, projector_error = invariant_star_subspace_certificate()
    record(
        "the two tested basis sources span the complete local O_h-invariant seven-star source space",
        invariant_rank == 2 and fixed_error < TOL and projector_error < TOL,
        (
            f"48-element signed-permutation average has rank={invariant_rank}, "
            f"fixed-basis error={fixed_error:.3e}, projector error={projector_error:.3e}"
        ),
    )
    record(
        "O_h covariance propagates from each invariant microscopic source to phi and sigma",
        max(max(r["orbit_phi"], r["orbit_sigma"]) for r in reports) < TOL,
        f"max orbit spread={max(max(r['orbit_phi'], r['orbit_sigma']) for r in reports):.3e}",
    )
    record(
        "the projector source is confined to the nearest-neighbor sewing band 3 < r <= 5",
        min(r["shell_min"] for r in reports) > 3.0 and max(r["shell_max"] for r in reports) <= 5.0 + TOL,
        f"global band=[{min(r['shell_min'] for r in reports):.6f},{max(r['shell_max'] for r in reports):.6f}]",
    )
    record(
        "the shell construction preserves the independently supplied microscopic total charge",
        max(r["charge_error"] for r in reports) < TOL,
        f"max |sum(sigma)-sum(q)|={max(r['charge_error'] for r in reports):.3e}",
    )
    record(
        "the unique solve H u=sigma reconstructs the projected exterior field",
        max(r["bridge_error"] for r in reports) < TOL,
        f"max bridge reconstruction error={max(r['bridge_error'] for r in reports):.3e}",
    )
    record(
        "the tested source basis and mixtures remain in the nondegenerate |u|<1 bridge domain",
        max(r["amplitude"] for r in reports) < 1.0,
        f"max |u|={max(r['amplitude'] for r in reports):.6f}",
        status="DOMAIN",
    )
    record(
        "the two restricted static-conformal equations solve exactly for rho and S",
        max(max(r["first_residual"], r["second_residual"]) for r in reports) < TOL,
        f"max constraint residual={max(max(r['first_residual'], r['second_residual']) for r in reports):.3e}",
    )
    record(
        "the independently constructed shell source vanishes on the exterior harmonic bulk",
        max(r["bulk_source"] for r in reports) < TOL,
        f"max |sigma_bulk|={max(r['bulk_source'] for r in reports):.3e}",
    )
    record(
        "the microscopic boundary source j=sigma|Gamma equals the Schur flux Lambda f",
        max(r["schur_flux_error"] for r in reports) < TOL,
        f"max |Lambda f-j|={max(r['schur_flux_error'] for r in reports):.3e}; j was fixed from sigma before the action solve",
    )
    record(
        "the Schur action reconstructs the shell trace without a target-defined source",
        max(r["minimizer_error"] for r in reports) < TOL,
        f"max |Lambda^-1 j-f|={max(r['minimizer_error'] for r in reports):.3e}",
    )
    record(
        "strict convexity gives the exact completion-of-squares minimum identity",
        min(r["minimum_gain"] for r in reports) > 0.0 and max(r["completion_error"] for r in reports) < TOL,
        f"min sampled gain={min(r['minimum_gain'] for r in reports):.3e}, max completion error={max(r['completion_error'] for r in reports):.3e}",
    )
    print("=" * 78)
    passed = sum(check.ok for check in CHECKS)
    failed = len(CHECKS) - passed
    print(f"PASS={passed} FAIL={failed} TOTAL={len(CHECKS)}")
    if failed:
        raise SystemExit(1)
    print("[EXACT] PASS: self-contained arbitrary-O_h finite-box closure certificate")
    print("[DEPENDENCY] proof inputs are H, P, arbitrary (q0,qs), Pi, and the stated bounded sector")
    print("[DEPENDENCY] fitted benchmark parameters, observed targets, and helper outputs are excluded")
    print("[BOUNDARY] physical GR/source identification remains outside this bounded theorem")


if __name__ == "__main__":
    main()
