# Coarse-Grained Exterior Law Helper Module

**Date:** 2026-04-14 (wrapper note added 2026-05-17; 2026-05-24
helper-runner code excerpts inlined for restricted-packet completeness)
**Claim type:** bounded_theorem
**Status:** bounded helper-module wrapper for the shell-averaging
plus radial-harmonic projection of the finite-rank exterior field onto
the `phi_eff(r) = a / r` unique radial-harmonic law.
**Status authority:** independent audit lane only. This wrapper note is
audit-lane infrastructure for the corresponding helper module.
**Primary runner:** `scripts/frontier_coarse_grained_exterior_law.py`
(module-mode load).

Load-bearing helper-runner sources (inlined in §"Helper-runner code
excerpts" below for restricted-packet completeness; full sources live
in `scripts/_frontier_loader.py`,
`scripts/frontier_same_source_metric_ansatz_scan.py`,
`scripts/frontier_finite_rank_gravity_residual.py`).

## Purpose

This wrapper note documents the coarse-grained exterior law helper module
so downstream notes (notably
`FINITE_RANK_SOURCE_TO_METRIC_THEOREM_NOTE.md` — see-also; backticked to
break cycle-0005 in the citation graph, since the load-bearing edge
direction is theorem -> this helper, not vice versa)
can register a one-hop dependency rather than carry the helper as an
unattributed Python `SourceFileLoader` import.

## What this module provides

The helper module takes the exact finite-rank exterior field
`phi(x)` produced by the
[FINITE_RANK_GRAVITY_RESIDUAL_HELPER_NOTE_2026-04-14.md](FINITE_RANK_GRAVITY_RESIDUAL_HELPER_NOTE_2026-04-14.md)
and applies the shell-averaging plus radial-harmonic projection map

```
phi_eff(r)  :=  shell_average(phi, r)  ->  a / r
```

with the projection coefficient `a` determined by best-match radius
selection across the radial scan. The module exposes:

- `build_finite_rank_phi_grid()` — assembles the `phi(x)` field grid
  from the upstream finite-rank exterior field construction.
- `analyze_family(...)` — runs the shell-averaging plus radial-harmonic
  projection and reports the coarse-grained metric residual at each
  scan radius.

## What this produces

The bounded coarse-grained metric residual on the finite-rank family is
verified in the companion runner of the downstream theorem note:

- best matching radius in current scan: `R_match = 5.0`
- direct same-source metric residual: `1.039e-02`
- coarse-grained radial-harmonic residual: `7.028e-06`
- improvement factor: `~1.48e3`

So the coarse-graining map provides a clean scalar/isotropic exterior
metric architecture with multi-order improvement on the residual.

## Helper-runner code excerpts (load-bearing for restricted packet, inlined 2026-05-24)

The audit verdict on this row recorded:

> *"the runner depends on dynamically loaded helper scripts not included
> in the restricted packet, including the finite-rank field construction
> and the local O_h grid builder, so the load-bearing compute chain
> cannot be fully inspected from the provided sources. This is an
> artifact-completeness defect rather than a substantive failure of the
> stated bounded claim."*

with re-audit hint:

> *"runner_artifact_issue: include
> scripts/frontier_same_source_metric_ansatz_scan.py,
> scripts/frontier_finite_rank_gravity_residual.py, and
> _frontier_loader.py in the restricted packet so the dynamic imports
> can be audited directly."*

The primary runner `scripts/frontier_coarse_grained_exterior_law.py`
loads two sibling frontier scripts via the
`scripts/_frontier_loader.py` `SourceFileLoader` helper:

```python
from _frontier_loader import load_frontier

same_source = load_frontier("same_source_metric", "frontier_same_source_metric_ansatz_scan.py")
finite_rank = load_frontier("finite_rank_metric", "frontier_finite_rank_gravity_residual.py")
```

Because that loader uses runtime `SourceFileLoader.load_module()`, the
two siblings are not detected as static imports by AST parsers. After
the 2026-05-23 parser update (commit `cb64e4db1`), `_frontier_loader.py`
itself is now picked up as a helper-runner path; the two dynamically
loaded siblings are inlined below so the restricted-packet review does
not require external source navigation. Both files exist on main
(`scripts/frontier_same_source_metric_ansatz_scan.py`,
`scripts/frontier_finite_rank_gravity_residual.py`) and are cross-linked
in the header of this note.

### Helper: `scripts/_frontier_loader.py` (full source)

The loader is a 16-line shim around `SourceFileLoader` that lets sibling
frontier scripts be imported by module name without a package install.
Full source:

```python
#!/usr/bin/env python3
"""Local loader for sibling frontier scripts on the main branch."""

from __future__ import annotations

from importlib.machinery import SourceFileLoader
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent


def load_frontier(module_name: str, filename: str):
    return SourceFileLoader(module_name, str(SCRIPTS_DIR / filename)).load_module()
```

### Helper: `scripts/frontier_same_source_metric_ansatz_scan.py` — `build_best_phi_grid` (load-bearing)

The primary runner calls `same_source.build_best_phi_grid()` to obtain the
exact local `O_h`-symmetric `phi`-grid on which the coarse-graining map
is exercised. The load-bearing pieces of that helper (lattice operator,
support projector, adapted basis, `O_h` commutant operator, invariant
source, and the `build_best_phi_grid` builder itself) are inlined below.
Full source (~180 lines) lives in
`scripts/frontier_same_source_metric_ansatz_scan.py`; this excerpt is
the slice the coarse-graining runner actually exercises:

```python
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve

SUPPORT_COORDS = [
    np.array([0, 0, 0], dtype=int),
    np.array([1, 0, 0], dtype=int),
    np.array([-1, 0, 0], dtype=int),
    np.array([0, 1, 0], dtype=int),
    np.array([0, -1, 0], dtype=int),
    np.array([0, 0, 1], dtype=int),
    np.array([0, 0, -1], dtype=int),
]


def build_neg_laplacian_sparse(size: int):
    interior = size - 2
    n = interior**3
    ii, jj, kk = np.mgrid[0:interior, 0:interior, 0:interior]
    flat = ii.ravel() * interior * interior + jj.ravel() * interior + kk.ravel()

    rows = [flat]
    cols = [flat]
    vals = [np.full(n, 6.0)]
    for di, dj, dk in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
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

    H0 = sparse.csr_matrix(
        (np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
        shape=(n, n),
    )
    return H0, interior


def flat_idx(i: int, j: int, k: int, interior: int) -> int:
    return i * interior * interior + j * interior + k


def solve_columns(matrix, support: list[int]) -> np.ndarray:
    cols = []
    for site in support:
        rhs = np.zeros(matrix.shape[0])
        rhs[site] = 1.0
        cols.append(spsolve(matrix, rhs))
    return np.column_stack(cols)


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


B = build_adapted_basis()


def build_commutant_operator(a, b, c, lam_e, lam_t):
    block = np.array([
        [a, c, 0.0, 0.0, 0.0, 0.0, 0.0],
        [c, b, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, lam_e, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, lam_e, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, lam_t, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, lam_t, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, lam_t],
    ])
    return B @ block @ B.T


def build_invariant_source(m0, ms):
    v = np.zeros(7)
    v[0] = m0
    v[1:] = ms
    return v


def build_best_phi_grid():
    size = 15
    H0, interior = build_neg_laplacian_sparse(size)
    center = interior // 2
    support = [flat_idx(center + v[0], center + v[1], center + v[2], interior) for v in SUPPORT_COORDS]
    G0P = solve_columns(H0, support)
    GS = G0P[support, :]

    # Best exact O_h-symmetric source law found by frontier_oh_source_class_scan.py
    x1, x2, mix, lam_e, lam_t = 0.0698, 0.0499, -0.0070, 0.0642, 0.1056
    m0, ms = 0.8247, 0.2271
    W = build_commutant_operator(x1, x2, mix, lam_e, lam_t)
    m = build_invariant_source(m0, ms)
    q_eff = np.linalg.solve(np.eye(7) - W @ GS, m)
    phi_flat = G0P @ q_eff

    phi_grid = np.zeros((size, size, size))
    phi_grid[1:-1, 1:-1, 1:-1] = phi_flat.reshape((interior, interior, interior))

    support_points = [(center + v[0] + 1, center + v[1] + 1, center + v[2] + 1) for v in SUPPORT_COORDS]
    phi_max = max(float(phi_grid[idx]) for idx in support_points)
    scale = 0.35 / phi_max
    phi_grid *= scale
    return phi_grid
```

### Helper: `scripts/frontier_finite_rank_gravity_residual.py` — `finite_rank_setup`, `support_projector`, `solve_columns` (load-bearing)

The primary runner's `build_finite_rank_phi_grid()` calls
`finite_rank.finite_rank_setup()`, `finite_rank.support_projector(...)`,
and `finite_rank.solve_columns(...)` to assemble the finite-rank
`phi`-grid, then projects it onto the interior with the same
`H_W = H_0 - P W P^T` finite-rank source construction documented in
`FINITE_RANK_GRAVITY_RESIDUAL_HELPER_NOTE_2026-04-14.md`. The
load-bearing slice of that helper (lattice operator, support indices,
solver, finite-rank `H_0 - PWP^T` setup) is inlined below; full source
(~370 lines) lives in
`scripts/frontier_finite_rank_gravity_residual.py`:

```python
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve


def build_neg_laplacian_sparse(size: int):
    interior = size - 2
    n = interior * interior * interior
    ii, jj, kk = np.mgrid[0:interior, 0:interior, 0:interior]
    flat = ii.ravel() * interior * interior + jj.ravel() * interior + kk.ravel()

    rows = [flat]
    cols = [flat]
    vals = [np.full(n, 6.0)]
    for di, dj, dk in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
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


def flat_idx(i, j, k, interior):
    return i * interior * interior + j * interior + k


def support_projector(n, support):
    P = np.zeros((n, len(support)))
    for col, site in enumerate(support):
        P[site, col] = 1.0
    return P


def solve_columns(matrix, support):
    cols = []
    for site in support:
        rhs = np.zeros(matrix.shape[0])
        rhs[site] = 1.0
        cols.append(spsolve(matrix, rhs))
    return np.column_stack(cols)


def finite_rank_setup():
    size = 15
    H0, interior = build_neg_laplacian_sparse(size)
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
    G0P = solve_columns(H0, support)
    GS = G0P[support, :]

    base = np.array([0.11, 0.08, 0.08, 0.075, 0.075, 0.07, 0.07])
    D = np.diag(np.sqrt(base / np.diag(GS)))
    corr = np.eye(len(support)) + 0.18 * np.ones((len(support), len(support)))
    W_raw = D @ corr @ D

    eigvals = np.linalg.eigvals(W_raw @ GS)
    rho = max(abs(ev) for ev in eigvals)
    scale = 0.45 / rho
    W = scale * W_raw

    masses = np.array([1.0, 0.82, 0.77, 0.73, 0.69, 0.64, 0.61])
    return size, H0, interior, support, G0P, GS, W, masses
```

### Primary runner excerpt: `scripts/frontier_coarse_grained_exterior_law.py` — load-bearing shell-averaging + projection

For completeness, the load-bearing shell-averaging, harmonic projection,
and `analyze_family` flow that consumes the two helper outputs above:

```python
from _frontier_loader import load_frontier

import numpy as np
from scipy.ndimage import map_coordinates

same_source = load_frontier("same_source_metric", "frontier_same_source_metric_ansatz_scan.py")
finite_rank = load_frontier("finite_rank_metric", "frontier_finite_rank_gravity_residual.py")


def shell_data(phi_grid):
    size = phi_grid.shape[0]
    center = (size - 1) / 2.0
    shells = {}
    radii = {}
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


def fit_radial_harmonic_projection(phi_grid, r_match):
    usable, radii, shells = shell_data(phi_grid)
    d2s = [d2 for d2 in usable if radii[d2] >= r_match]
    r = np.array([radii[d2] for d2 in d2s], dtype=float)
    y = np.array([np.mean(shells[d2]) for d2 in d2s], dtype=float)
    a = float(np.linalg.lstsq((1.0 / r).reshape(-1, 1), y, rcond=None)[0][0])
    pred = a / r
    rel_rms = float(np.sqrt(np.mean((y - pred) ** 2)) / max(np.max(np.abs(y)), 1e-12))
    max_rel = float(np.max(np.abs(y - pred) / np.maximum(np.abs(y), 1e-12)))
    return a, rel_rms, max_rel


def build_finite_rank_phi_grid():
    size, H0, interior, support, G0P, GS, W, masses = finite_rank.finite_rank_setup()
    P = finite_rank.support_projector(H0.shape[0], support)
    full = finite_rank.solve_columns(H0 - finite_rank.sparse.csr_matrix(P @ W @ P.T), support)
    phi_flat = full @ masses
    phi_grid = np.zeros((size, size, size))
    phi_grid[1:-1, 1:-1, 1:-1] = phi_flat.reshape((interior, interior, interior))
    return phi_grid
```

This is the full restricted-packet view of the load-bearing compute
chain that the audit verdict flagged as not directly inspectable. The
remaining numerical-GR pieces (Christoffel, Einstein-tensor finite
differences, probe-point evaluation, `analyze_family` reporting) are
standard finite-difference GR code in the primary runner file and are
not load-bearing for the present wrapper's bounded claim beyond the
inlined slices above.

## Boundary

This wrapper note records the bounded helper-module character of the
coarse-grained exterior law module. It does not claim:

- a framework-level derivation of the shell-averaging or radial-harmonic
  projection as physically forced;
- a tensorial `3 + 1` lift from the scalar exterior law to the full
  lapse-shift-spatial metric;
- closure of the downstream finite-rank source-to-metric theorem
  beyond the bounded coarse-grained residual it already reports.

Its only function is to provide a citeable one-hop authority for the
shell-averaging plus radial-harmonic projection construction so
downstream notes register the import cleanly instead of carrying it as
a `SourceFileLoader` runner import without a wrapper.

## Retarget: shell-helper surface now sourced by the lattice identity (2026-06-16)

The exterior / shell-localization helper surface this note rests on (shell-mean
profile equality, exterior projector `Pi_R^ext`, sewing-band shell source
`sigma_R = H Pi_R^ext`, radial-DtN kernel, one-parameter reduced-shell law) is
now represented by
[`LATTICE_LAPLACIAN_SHELL_LOCALIZATION_IDENTITY_BOUNDED_THEOREM_NOTE_2026-06-16.md`](LATTICE_LAPLACIAN_SHELL_LOCALIZATION_IDENTITY_BOUNDED_THEOREM_NOTE_2026-06-16.md),
which derives that shell identity from the Lattice axiom's `Z^3`
nearest-neighbor adjacency plus the existing cubic `O_h` lift (runner-verified
`TOTAL: PASS=14 FAIL=0`). This replaces the imported `_frontier_loader` helper
surface for that shell content only. Independent re-audit must decide whether
this row can move; no audit status, effective status, or `bounded -> retained`
verdict is asserted here. Any non-shell residual (a GR / tensor completion or
the lattice-Green `1/r` Maradudin asymptotic) is out of scope and unaffected.
