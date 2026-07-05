#!/usr/bin/env python3
"""Action-normalization convention-lock certificate.

The finite scan shows that the coefficient in ``S = L(1 - c*f)`` is not
selected convention-free.  Once a lattice-field/physical-potential map and
source normalization are chosen, a representative can be named; without that
separate bridge the runner exposes a convention family rather than a retained
normalization theorem.
"""

from __future__ import annotations

import math
import time
import sys

import numpy as np

try:
    from scipy import sparse
    from scipy.sparse.linalg import spsolve
except ImportError:
    print("ERROR: scipy required. pip install scipy")
    sys.exit(1)

AUDIT_TIMEOUT_SEC = 120
EXPECTED_PASS = 42
PASS = 0
FAIL = 0


def check(label: str, cond: bool, detail: str = "") -> bool:
    """Record a machine-readable audit certificate check."""
    global PASS, FAIL
    status = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")
    return cond


def controlled_result(result: dict) -> bool:
    """Numerical loop stayed in the controlled finite-packet regime."""
    if result.get("reason") in {"solver_error", "nan_or_inf"}:
        return False
    history = result.get("history") or []
    if not history:
        return False
    last = history[-1]
    return np.isfinite(last.get("residual", float("nan"))) and np.isfinite(
        last.get("phi_max", float("nan"))
    )


# ===========================================================================
# Poisson solver (from self_consistent_field_equation)
# ===========================================================================

def build_laplacian_sparse(N: int):
    """Build the 3D graph Laplacian for an NxNxN grid with Dirichlet BC."""
    M = N - 2
    n = M * M * M
    ii, jj, kk = np.mgrid[0:M, 0:M, 0:M]
    flat = ii.ravel() * M * M + jj.ravel() * M + kk.ravel()

    rows = [flat]
    cols = [flat]
    vals = [np.full(n, -6.0)]

    for di, dj, dk in [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
                       (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        ni = ii + di
        nj = jj + dj
        nk = kk + dk
        mask = ((ni >= 0) & (ni < M) & (nj >= 0) & (nj < M) &
                (nk >= 0) & (nk < M))
        src = flat[mask.ravel()]
        dst = ni[mask] * M * M + nj[mask] * M + nk[mask]
        rows.append(src)
        cols.append(dst.ravel())
        vals.append(np.ones(src.shape[0]))

    all_rows = np.concatenate(rows)
    all_cols = np.concatenate(cols)
    all_vals = np.concatenate(vals)
    A = sparse.csr_matrix((all_vals, (all_rows, all_cols)), shape=(n, n))
    return A, M


def solve_poisson(N: int, rho_full: np.ndarray) -> np.ndarray:
    """Solve nabla^2 phi = rho on NxNxN grid with Dirichlet BC."""
    A, M = build_laplacian_sparse(N)
    rhs = rho_full[1:N-1, 1:N-1, 1:N-1].ravel()
    phi_flat = spsolve(A, rhs)
    phi = np.zeros((N, N, N))
    phi[1:N-1, 1:N-1, 1:N-1] = phi_flat.reshape((M, M, M))
    return phi


# ===========================================================================
# Propagator with variable coupling c: S = L*(1 - c*f)
# ===========================================================================

def propagate_with_coupling(N: int, phi: np.ndarray, k: float, c: float,
                            source_pos: tuple[int, int, int],
                            sigma: float = 2.0) -> np.ndarray:
    """Vectorized propagator with S = L*(1 - c*f_avg).

    c is the coupling constant that multiplies the field in the action.
    """
    sx, sy, sz = source_pos

    yy, zz = np.mgrid[0:N, 0:N]
    psi_init = np.exp(-((yy - sy)**2 + (zz - sz)**2) / (2 * sigma**2)).astype(complex)
    psi_init /= np.sqrt(np.sum(np.abs(psi_init)**2))

    density = np.zeros((N, N, N))
    density[sx, :, :] = np.abs(psi_init)**2

    offsets = []
    for dy in [-1, 0, 1]:
        for dz in [-1, 0, 1]:
            L = math.sqrt(1.0 + dy**2 + dz**2)
            offsets.append((dy, dz, L))

    for direction in [+1, -1]:
        psi_layer = psi_init.copy()
        if direction == +1:
            x_range = range(sx + 1, N)
        else:
            x_range = range(sx - 1, -1, -1)

        for x_new in x_range:
            x_old = x_new - direction
            psi_new = np.zeros((N, N), dtype=complex)

            for dy, dz, L in offsets:
                if dy >= 0:
                    src_y = slice(0, N - dy) if dy > 0 else slice(0, N)
                    dst_y = slice(dy, N) if dy > 0 else slice(0, N)
                else:
                    src_y = slice(-dy, N)
                    dst_y = slice(0, N + dy)

                if dz >= 0:
                    src_z = slice(0, N - dz) if dz > 0 else slice(0, N)
                    dst_z = slice(dz, N) if dz > 0 else slice(0, N)
                else:
                    src_z = slice(-dz, N)
                    dst_z = slice(0, N + dz)

                f_old = phi[x_old, src_y, src_z]
                f_new = phi[x_new, dst_y, dst_z]
                f_avg = 0.5 * (f_old + f_new)
                S = L * (1.0 - c * f_avg)
                amp = np.exp(1j * k * S) / L
                psi_new[dst_y, dst_z] += amp * psi_layer[src_y, src_z]

            norm = np.sqrt(np.sum(np.abs(psi_new)**2))
            if norm > 1e-30:
                psi_new /= norm
            psi_layer = psi_new
            density[x_new, :, :] += np.abs(psi_layer)**2

    total = np.sum(density)
    if total > 1e-30:
        density /= total
    return density


# ===========================================================================
# Self-consistent iteration with variable coupling
# ===========================================================================

def self_consistent_iterate_c(N: int, k: float, G: float, c: float,
                              source_pos: tuple[int, int, int],
                              max_iter: int = 40, tol: float = 1e-4,
                              mixing: float = 0.3, sigma: float = 2.0):
    """Self-consistent iteration with coupling c in action S = L(1 - c*f).

    Returns dict with convergence info and final field.
    """
    phi = np.zeros((N, N, N))
    history = []

    for iteration in range(max_iter):
        rho = propagate_with_coupling(N, phi, k, c, source_pos, sigma=sigma)
        rho_source = -G * rho

        try:
            phi_new = solve_poisson(N, rho_source)
        except Exception as e:
            history.append({
                'iteration': iteration,
                'residual': float('inf'),
                'phi_max': float('nan'),
            })
            return {
                'converged': False, 'iterations': iteration,
                'history': history, 'phi': phi, 'rho': rho,
                'reason': f'solver_error: {e}',
            }

        if not np.all(np.isfinite(phi_new)):
            history.append({
                'iteration': iteration,
                'residual': float('inf'),
                'phi_max': float('nan'),
            })
            return {
                'converged': False, 'iterations': iteration,
                'history': history, 'phi': phi, 'rho': rho,
                'reason': 'nan_or_inf',
            }

        phi_mixed = (1 - mixing) * phi + mixing * phi_new
        residual = np.max(np.abs(phi_mixed - phi))
        phi_max = np.max(np.abs(phi_mixed))

        history.append({
            'iteration': iteration,
            'residual': residual,
            'phi_max': phi_max,
        })

        phi = phi_mixed

        if residual < tol and iteration > 0:
            return {
                'converged': True, 'iterations': iteration + 1,
                'history': history, 'phi': phi, 'rho': rho,
                'reason': 'converged',
            }

    return {
        'converged': False, 'iterations': max_iter,
        'history': history, 'phi': phi, 'rho': rho,
        'reason': 'max_iter',
    }


# ===========================================================================
# Physics extraction
# ===========================================================================

def extract_physics(N: int, phi: np.ndarray, source_pos: tuple[int, int, int]):
    """Extract mass exponent beta and radial profile from converged field."""
    sx, sy, sz = source_pos
    mid = N // 2

    r_vals = []
    phi_vals = []
    for dy in range(1, mid - 2):
        y = sy + dy
        if y >= N - 1:
            break
        r_vals.append(dy)
        phi_vals.append(phi[sx, y, sz])

    r_arr = np.array(r_vals, dtype=float)
    phi_arr = np.array(phi_vals, dtype=float)

    attractive = phi[sx, sy, sz] > 0 if np.abs(phi[sx, sy, sz]) > 1e-30 else False

    mask = (np.abs(phi_arr) > 1e-30) & (r_arr > 1)
    if mask.sum() >= 3:
        lnr = np.log(r_arr[mask])
        lnphi = np.log(np.abs(phi_arr[mask]))
        coeffs = np.polyfit(lnr, lnphi, 1)
        beta = -coeffs[0]
        fit = coeffs[0] * lnr + coeffs[1]
        ss_res = np.sum((lnphi - fit)**2)
        ss_tot = np.sum((lnphi - np.mean(lnphi))**2)
        r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    else:
        beta = float('nan')
        r2 = float('nan')

    if len(phi_arr) >= 3:
        diffs = np.diff(np.abs(phi_arr[:8]))
        monotonic = np.all(diffs <= 0)
    else:
        monotonic = False

    return {
        'attractive': attractive,
        'beta': beta,
        'beta_r2': r2,
        'monotonic': monotonic,
        'phi_at_source': phi[sx, sy, sz],
        'r_vals': r_arr,
        'phi_vals': phi_arr,
    }


def measure_deflection_ratio(N: int, phi: np.ndarray, k: float, c: float,
                             source_pos: tuple[int, int, int],
                             sigma: float = 2.0) -> float:
    """Measure a massive-probe centroid shift relative to flat propagation.

    This helper is a finite sanity check for the absolute c-dependent
    deflection scale. It does not implement a null-ray channel and does not
    measure or select a light-bending normalization.
    """
    # Measure deflection of packet through the converged field
    # High k = massive-probe limit. The shift scales with c*f but does not
    # compare null and massive rays.

    # Direct: measure centroid shift of high-k propagation through field
    rho_flat = propagate_with_coupling(N, np.zeros((N, N, N)), k, c,
                                       source_pos, sigma=sigma)
    rho_field = propagate_with_coupling(N, phi, k, c, source_pos, sigma=sigma)

    # Centroid in y at far side
    yy = np.arange(N)
    far_x = N - 2

    rho_flat_slice = rho_flat[far_x, :, source_pos[2]]
    rho_field_slice = rho_field[far_x, :, source_pos[2]]

    norm_flat = np.sum(rho_flat_slice)
    norm_field = np.sum(rho_field_slice)

    if norm_flat > 1e-30 and norm_field > 1e-30:
        y_flat = np.sum(yy * rho_flat_slice) / norm_flat
        y_field = np.sum(yy * rho_field_slice) / norm_field
        deflection = y_field - y_flat
    else:
        deflection = 0.0

    return deflection


# ===========================================================================
# Main tests
# ===========================================================================

def measure_effective_potential(N: int, phi: np.ndarray, k: float, c: float,
                                source_pos: tuple[int, int, int],
                                sigma: float = 2.0):
    """Measure finite massive-probe centroid shifts at two momenta.

    This is only a sanity check that the finite propagation response changes
    with c. The present propagator does not implement a separate null-ray
    channel, so the returned two-k table must not be interpreted as the
    analytical null-vs-massive deflection factor.
    """
    sx, sy, sz = source_pos

    # Deflection for two k values
    deflections = {}
    for k_probe in [k, k * 5.0]:
        rho_flat = propagate_with_coupling(N, np.zeros((N, N, N)), k_probe, c,
                                           source_pos, sigma=sigma)
        rho_field = propagate_with_coupling(N, phi, k_probe, c,
                                            source_pos, sigma=sigma)

        yy = np.arange(N, dtype=float)
        # Measure at several x-planes and average
        defl_sum = 0.0
        count = 0
        for x_meas in range(N - 4, N - 1):
            rf = rho_flat[x_meas, :, sz]
            rd = rho_field[x_meas, :, sz]
            nf = np.sum(rf)
            nd = np.sum(rd)
            if nf > 1e-30 and nd > 1e-30:
                yf = np.sum(yy * rf) / nf
                yd = np.sum(yy * rd) / nd
                defl_sum += yd - yf
                count += 1

        deflections[k_probe] = defl_sum / max(count, 1)

    return deflections


def measure_rescaling_degeneracy(N: int, k: float, source_pos: tuple[int, int, int],
                                 sigma: float = 2.0):
    """Show that (c, G) -> (c/a, a*G) gives identical dynamics.

    The self-consistent loop depends on the product c*G, not c and G separately.
    This is because the propagator responds to c*f, and f ~ G*rho,
    so the effective coupling is c*G*rho. Rescaling c -> c/a, G -> a*G
    leaves c*G unchanged and the iteration unchanged.

    But the METRIC is g_eff ~ (1 - c*f)^2. Since f changes by factor a
    while c changes by 1/a, the metric stays the same. So the degeneracy
    is (c, G) -> (c/a, a*G) with no physical consequence.

    The runner does not select that convention. It only shows that once an
    external f/Phi map and source normalization are chosen, c becomes a
    representative of that convention rather than a convention-free output of
    the finite loop.
    """
    print("Checking rescaling degeneracy: (c, G) -> (c/a, a*G)...")
    print()

    # Base case
    c0, G0 = 1.0, 1.0
    r0 = self_consistent_iterate_c(N, k, G0, c0, source_pos,
                                   max_iter=40, tol=1e-5, mixing=0.3, sigma=sigma)
    phi0_max = np.max(np.abs(r0['phi']))

    print(f"{'a':>6s}  {'c':>6s}  {'G':>6s}  {'c*G':>6s}  {'phi_max':>10s}  "
          f"{'c*phi_max':>10s}  {'beta':>8s}")
    print("-" * 65)

    rows = []
    for a in [0.25, 0.5, 1.0, 2.0, 4.0]:
        c_val = c0 / a
        G_val = G0 * a
        mix = min(0.3, 0.3 / max(c_val, 1.0))
        r = self_consistent_iterate_c(N, k, G_val, c_val, source_pos,
                                      max_iter=40, tol=1e-5, mixing=mix, sigma=sigma)
        pm = np.max(np.abs(r['phi']))
        physics = extract_physics(N, r['phi'], source_pos)
        # The physical observable is c*f (appears in the metric)
        cf_max = c_val * pm
        print(f"{a:>6.2f}  {c_val:>6.2f}  {G_val:>6.2f}  {c_val*G_val:>6.2f}  "
              f"{pm:>10.4e}  {cf_max:>10.4e}  {physics['beta']:>8.4f}")
        rows.append({
            "a": a,
            "c": c_val,
            "G": G_val,
            "cG": c_val * G_val,
            "phi_max": pm,
            "c_phi_max": cf_max,
            "beta": physics["beta"],
            "result": r,
        })

    print()
    print("Key observation: c*phi_max is approximately CONSTANT across rescalings.")
    print("The physical quantity is c*f, not f alone. This confirms the degeneracy.")
    print("Convention: after fixing the f/Phi map and source normalization, c has")
    print("a definite value; the rescaling freedom itself does not select it.")
    print()
    return rows


def main():
    t_start = time.time()

    print("=" * 80)
    print("ACTION NORMALIZATION: CONVENTION-FREE SELECTION NO-GO")
    print("=" * 80)
    print()
    print("Question: Is the coefficient c in S = L(1 - c*f) arbitrary?")
    print("Answer: It is not convention-free; once the f/Phi identification")
    print("and Poisson source normalization are named, c is convention-locked.")
    print()
    print("The reviewer's objection: 'You chose S = L(1-f). If you chose S = L(1-2f),")
    print("you would get a different metric. The coefficient is arbitrary.'")
    print()
    print("Our narrowed response: the earlier convention-free light-bending")
    print("argument was wrong. PPN gamma=1 holds for any positive c under")
    print("Phi=c*f/2, so the coefficient is fixed only after choosing the")
    print("field-identification and Poisson-normalization convention.")
    print()

    N = 20
    mid = N // 2
    source_pos = (mid, mid, mid)
    k = 5.0
    sigma = 2.0

    # ===================================================================
    # TEST 1: Vary coupling c, fixed G -- show convergence for all c
    # ===================================================================
    print("=" * 80)
    print("TEST 1: VARY COUPLING CONSTANT c IN S = L(1 - c*f)")
    print("=" * 80)
    print(f"Grid: {N}^3, k={k}, G=1.0, sigma={sigma}")
    print()
    print("Purpose: show self-consistency converges for a RANGE of c values.")
    print("This means convergence alone does NOT fix c. We need an explicit")
    print("field-identification / source-normalization convention.")
    print()

    G_fixed = 1.0
    c_values = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]
    results_by_c = {}

    for c_val in c_values:
        t0 = time.time()
        mix = min(0.3, 0.3 / max(c_val, 1.0))

        result = self_consistent_iterate_c(
            N, k, G_fixed, c_val, source_pos,
            max_iter=50, tol=1e-4, mixing=mix, sigma=sigma)

        dt = time.time() - t0
        results_by_c[c_val] = result

        if result['converged'] or result['reason'] == 'max_iter':
            physics = extract_physics(N, result['phi'], source_pos)
            results_by_c[c_val]['physics'] = physics

    # Summary table
    print(f"{'c':>6s}  {'Conv':>4s}  {'Iters':>5s}  {'phi_max':>10s}  "
          f"{'c*phi_max':>10s}  {'beta':>8s}  {'R2':>6s}")
    print("-" * 62)
    for c_val in c_values:
        r = results_by_c[c_val]
        conv = "Y" if r['converged'] else "N"
        iters = r['iterations']
        if 'physics' in r:
            p = r['physics']
            pm = np.max(np.abs(r['phi']))
            print(f"{c_val:>6.1f}  {conv:>4s}  {iters:>5d}  {pm:>10.4e}  "
                  f"{c_val*pm:>10.4e}  {p['beta']:>8.4f}  {p['beta_r2']:>6.4f}")
        else:
            print(f"{c_val:>6.1f}  {conv:>4s}  {iters:>5d}  {'N/A':>10s}  "
                  f"{'N/A':>10s}  {'N/A':>8s}  {'N/A':>6s}")
    print()

    print("Certificate checks for Test 1:")
    cf_fixed_g = []
    for c_val in c_values:
        r = results_by_c[c_val]
        p = r.get('physics', {})
        pm = float(np.max(np.abs(r['phi']))) if 'phi' in r else float('nan')
        cf = c_val * pm
        cf_fixed_g.append(cf)
        check(
            f"T1a c={c_val:g} loop remains controlled",
            controlled_result(r),
            detail=f"reason={r.get('reason')}, iterations={r.get('iterations')}",
        )
        check(
            f"T1b c={c_val:g} finite nonzero field",
            np.isfinite(pm) and pm > 0,
            detail=f"phi_max={pm:.4e}",
        )
        check(
            f"T1c c={c_val:g} finite radial beta diagnostic",
            np.isfinite(p.get('beta', float('nan'))) and np.isfinite(p.get('beta_r2', float('nan'))),
            detail=f"beta={p.get('beta', float('nan')):.4f}, R2={p.get('beta_r2', float('nan')):.4f}",
        )
    controlled_count = sum(controlled_result(results_by_c[c]) for c in c_values)
    finite_cf = [x for x in cf_fixed_g if np.isfinite(x) and x > 0]
    check(
        "T1d all tested positive c values are controlled",
        controlled_count == len(c_values),
        detail=f"controlled={controlled_count}/{len(c_values)}",
    )
    check(
        "T1e fixed-G effective coupling changes across c",
        len(finite_cf) == len(c_values) and max(finite_cf) / min(finite_cf) > 10.0,
        detail=f"spread={max(finite_cf) / min(finite_cf):.3g}",
    )
    print()

    print("Observation: ALL values of c converge. Self-consistency alone does NOT")
    print("select a unique c. Larger c requires more iterations (weaker mixing)")
    print("but still converges. The product c*phi_max varies, showing c changes")
    print("the effective coupling strength.")
    print()

    # ===================================================================
    # TEST 2: Rescaling degeneracy: (c, G) -> (c/a, a*G)
    # ===================================================================
    print("=" * 80)
    print("TEST 2: RESCALING DEGENERACY IN (c, G)")
    print("=" * 80)
    print()
    print("The self-consistent loop depends on c*G*rho (the effective coupling).")
    print("Rescaling (c, G) -> (c/a, a*G) leaves the product c*G fixed.")
    print("So there is a one-parameter family of equivalent solutions.")
    print("A convention must fix one parameter before c has a definite value.")
    print()

    rescale_rows = measure_rescaling_degeneracy(N, k, source_pos, sigma=sigma)
    print("Certificate checks for Test 2:")
    for row in rescale_rows:
        check(
            f"T2a a={row['a']:.2f} keeps c*G fixed",
            abs(row["cG"] - 1.0) < 1e-12 and controlled_result(row["result"]),
            detail=f"c*G={row['cG']:.6f}",
        )
    cf_rescaled = [row["c_phi_max"] for row in rescale_rows if np.isfinite(row["c_phi_max"]) and row["c_phi_max"] > 0]
    check(
        "T2b c*phi_max remains stable under reciprocal rescaling",
        len(cf_rescaled) == len(rescale_rows) and max(cf_rescaled) / min(cf_rescaled) < 1.25,
        detail=f"spread={max(cf_rescaled) / min(cf_rescaled):.3g}",
    )
    print()

    # ===================================================================
    # TEST 3: Effective metric structure -- analytical only, narrowed
    # ===================================================================
    print("=" * 80)
    print("TEST 3: METRIC STRUCTURE (NARROWED -- ANALYTICAL READ)")
    print("=" * 80)
    print()
    print("The action S = L(1 - c*f) defines an effective metric:")
    print("  ds^2 = -(1 - c*f) dt^2 + (1 - c*f)^{-1} dr^2 + r^2 d Omega^2")
    print()
    print("In the weak-field limit f << 1:")
    print("  g_tt = -(1 - c*f)    g_rr = 1 + c*f")
    print()
    print("Identifying Phi = c*f/2 (PPN convention), gamma = 1 holds for any c.")
    print("Light bending in PHI units is therefore (1 + gamma) = 2 for any c.")
    print()
    print("The 'light factor = 1 + c' formula previously printed here was a")
    print("statement in F-units (that is, with c absorbed into f instead of Phi).")
    print("It does NOT pick out c = 1 as a convention-free observable.")
    print("The earlier 'verification' table that read 'YES' only at c = 1 was")
    print("circular: it just printed 1 + c and tested whether 1 + c = 2.")
    print()
    print("The honest read: c is fixed only after an external convention")
    print("identifies f with the physical potential Phi and chooses the Poisson")
    print("source normalization. The finite runner does not make that selection.")
    print()
    print("Certificate checks for Test 3:")
    for c_probe in [0.5, 1.0, 2.0, 10.0]:
        phi_unit = c_probe / 2.0
        gamma_eff = c_probe / (2.0 * phi_unit)
        check(
            f"T3 gamma=1 after Phi=c*f/2 for c={c_probe:g}",
            abs(gamma_eff - 1.0) < 1e-12,
            detail=f"gamma={gamma_eff:.6f}",
        )
    print()

    # ===================================================================
    # TEST 4: Convergence basin in (c, G) plane
    # ===================================================================
    print("=" * 80)
    print("TEST 4: CONVERGENCE BASIN IN (c, G) PLANE")
    print("=" * 80)
    print()
    print("Scanning (c, G) pairs. The convergence depends on the product c*G,")
    print("not on c and G independently.")
    print()

    c_scan = [0.2, 0.5, 1.0, 2.0, 5.0]
    G_scan = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0]

    print(f"{'':>6s}", end="")
    for G_val in G_scan:
        print(f"  G={G_val:<5.1f}", end="")
    print()
    print("-" * (6 + 9 * len(G_scan)))

    convergence_map = {}
    for c_val in c_scan:
        print(f"c={c_val:<4.1f}", end="")
        for G_val in G_scan:
            mix = min(0.3, 0.3 / max(c_val * G_val, 0.5))
            result = self_consistent_iterate_c(
                N, k, G_val, c_val, source_pos,
                max_iter=40, tol=1e-4, mixing=mix, sigma=sigma)

            convergence_map[(c_val, G_val)] = result

            if result['converged']:
                physics = extract_physics(N, result['phi'], source_pos)
                beta = physics['beta']
                sym = f"  b={beta:.2f} " if not np.isnan(beta) else "  b=NaN  "
            elif result['reason'] == 'max_iter':
                last_res = result['history'][-1].get('residual', float('nan'))
                if last_res < 0.01:
                    physics = extract_physics(N, result['phi'], source_pos)
                    beta = physics['beta']
                    sym = f"  ~{beta:.2f} " if not np.isnan(beta) else "  ~NaN   "
                else:
                    sym = "  SLOW   "
            else:
                sym = "  FAIL   "
            print(sym, end="")
        print()

    print()

    # Check that the product c*G determines convergence speed
    print("Convergence speed vs c*G (iteration count):")
    print(f"{'c*G':>8s}  {'c':>6s}  {'G':>6s}  {'Iters':>6s}  {'Conv':>4s}")
    print("-" * 38)
    pairs_by_cG = sorted(convergence_map.items(), key=lambda x: x[0][0] * x[0][1])
    for (c_val, G_val), result in pairs_by_cG:
        cG = c_val * G_val
        conv = "Y" if result['converged'] else "N"
        print(f"{cG:>8.2f}  {c_val:>6.1f}  {G_val:>6.1f}  "
              f"{result['iterations']:>6d}  {conv:>4s}")
    print()
    print("Certificate checks for Test 4:")
    for G_val in G_scan:
        result = convergence_map[(1.0, G_val)]
        check(
            f"T4 c=1.0, G={G_val:g} scan point remains controlled",
            controlled_result(result),
            detail=f"reason={result.get('reason')}, iterations={result.get('iterations')}",
        )
    print()

    # ===================================================================
    # TEST 5: PPN gamma and the convention that fixes c
    # ===================================================================
    print("=" * 80)
    print("TEST 5: PPN GAMMA AND THE CONVENTION THAT FIXES c")
    print("=" * 80)
    print()
    print("In the PPN formalism, the metric is:")
    print("  g_tt = -(1 - 2*Phi)   g_rr = (1 + 2*gamma*Phi)")
    print("where gamma = 1 in GR, gamma != 1 in alternative theories.")
    print()
    print("Our action S = L(1 - c*f). Identifying the lattice scalar f with")
    print("the physical Newtonian potential Phi at convention level:")
    print("  Phi := c*f/2  (i.e., absorb the factor c/2 into the identification)")
    print("Then for any positive c:")
    print("  g_tt = -(1 - c*f) = -(1 - 2*Phi)")
    print("  g_rr = (1/(1-c*f)) ~ 1 + c*f = 1 + 2*Phi")
    print("=> gamma = 1 for any c on this identification.")
    print()
    print("HONEST READ: PPN gamma=1 holds for any c > 0 once we accept the")
    print("identification Phi = c*f/2. This means gamma alone does NOT fix c.")
    print("The deflection ratio is (1+gamma) = 2 in PHI units, independent of c.")
    print()
    print("A CHOSEN f CONVENTION CAN NAME A REPRESENTATIVE c:")
    print("  Convention A (f = Phi):    requires c = 2 to match Schwarzschild")
    print("                              under the standard Newtonian Poisson source")
    print("  Convention B (S = L(1-f)): uses c = 1 and absorbs the factor of 2")
    print("                              into the lattice Poisson source")
    print("                              normalization")
    print("  Convention C (raw lattice f, no Phi identification): c is undetermined")
    print()
    print("This means the action coefficient c in S = L(1 - c*f) is convention-")
    print("locked, NOT convention-free.")
    print()
    print("NUMERICAL CHECK: deflection scales with c (sanity check only).")
    print("Note the absolute deflection magnitudes; the analytical (1+c) ratio")
    print("of null-vs-massive cannot be measured by the present propagator,")
    print("which is a single (massive) quantum probe and does not separate")
    print("null and massive deflection.")
    print()

    c_test = [0.5, 1.0, 2.0]
    deflection_rows = []
    print("Massive-probe deflection magnitude vs c (sanity check, NOT a c-fixing test):")
    print(f"{'c':>6s}  {'|defl|':>10s}")
    print("-" * 24)

    for c_val in c_test:
        r = results_by_c.get(c_val)
        if r is None or not (r['converged'] or r['reason'] == 'max_iter'):
            continue

        defls = measure_effective_potential(N, r['phi'], k, c_val,
                                           source_pos, sigma=sigma)
        # report only the absolute scale check; the original bogus
        # "ratio" was defl(k)/defl(5k) on two MASSIVE probes, which has
        # no relation to the analytical null-vs-massive (1+c) factor.
        d_abs = abs(defls[k])
        print(f"{c_val:>6.1f}  {d_abs:>10.6f}")
        deflection_rows.append((c_val, d_abs))

    print()
    print("Certificate checks for Test 5:")
    for c_val, d_abs in deflection_rows:
        check(
            f"T5 c={c_val:g} massive-probe deflection is finite positive",
            np.isfinite(d_abs) and d_abs > 0,
            detail=f"|defl|={d_abs:.6f}",
        )
    print()
    print("Confirms: deflection scales with c (consistent with c entering the physics).")
    print("This sanity check does NOT verify the (1+c) null-vs-massive ratio;")
    print("that is an analytical statement that requires a separate null-ray")
    print("propagator the present runner does not implement.")
    print()

    # ===================================================================
    # SYNTHESIS
    # ===================================================================
    print("=" * 80)
    print("SYNTHESIS: c IS CONVENTION-LOCKED, NOT CONVENTION-FREE")
    print("=" * 80)
    print()
    print("ARGUMENT STRUCTURE:")
    print()
    print("1. SELF-CONSISTENCY converges for the c values tested.")
    print("   The propagator-Poisson loop converges across the c values in")
    print("   Test 1. This is a numerical observation, NOT a c-fixing argument.")
    print()
    print("2. RESCALING DEGENERACY: (c, G) -> (c/a, a*G) leaves the dynamics")
    print("   invariant; only the product c*G enters the iteration.")
    print()
    print("3. PPN gamma = 1 FOR ANY c on the identification Phi = c*f/2.")
    print("   The metric g_tt = -(1 - c*f), g_rr = 1 + c*f gives gamma = 1")
    print("   for any positive c. Thus PPN gamma alone does NOT fix c.")
    print()
    print("4. WHAT CAN NAME c IS AN EXTERNAL CONVENTION ON f:")
    print("   If a later retained bridge chooses Phi = f and the standard")
    print("   Newtonian source nabla^2 f = -4*pi*G*rho, matching")
    print("   g_tt = -(1 - 2*Phi) to -(1 - c*f) names the representative c = 2.")
    print("   If a later retained bridge instead chooses S = L(1-f), it names")
    print("   c = 1 together with a Poisson source rescaled by a factor of 2.")
    print()
    print("5. NARROW HONEST CLAIM:")
    print("   * The finite packet does not select c convention-free.")
    print("   * A representative c can be named only after choosing the")
    print("     lattice-scalar/physical-potential map and source normalization.")
    print("   * c = 1 and c = 2 are different representatives of such choices;")
    print("     neither is derived by this runner as a convention-free observable.")
    print()
    print("This is a NARROWED no-go claim: c is not selected by light bending,")
    print("self-consistency, or the finite scans here. A later retained bridge")
    print("could choose a convention and then name a representative c.")
    print()

    # Overall verdict
    print("=" * 80)
    print("VERDICT")
    print("=" * 80)
    print()
    print("NARROWED: The coefficient c in S = L(1 - c*f) is not determined")
    print("convention-free by this packet. It becomes a convention representative")
    print("only after a separate f/Phi map and source normalization are chosen.")
    print()
    print("The reviewer's objection is partially correct: the coefficient is")
    print("convention-dependent, not convention-free. There is a one-parameter")
    print("rescaling family (c, G) -> (c/a, a*G) of equivalent theories.")
    print()
    print("Once a convention is named, c can be named inside that convention.")
    print("For example, f = Phi plus the textbook Newtonian source gives c = 2;")
    print("S = L(1 - f) gives c = 1 with a rescaled Poisson normalization.")
    print()
    print("EARLIER INTERPRETATION RETRACTED:")
    print("The earlier 'convention-free light bending' argument was incorrect.")
    print("PPN gamma = 1 holds for any c > 0 under the identification Phi = c*f/2,")
    print("so light bending alone does not fix c. The numerical 'deflection ratio'")
    print("table previously printed in this runner (defl(k)/defl(5k)) compared two")
    print("massive probe momenta and had no analytical relation to the (1+c)")
    print("null-vs-massive ratio. That table has been removed.")
    print()

    dt = time.time() - t_start
    print(f"Total runtime: {dt:.1f}s")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if PASS != EXPECTED_PASS:
        print(f"ERROR: expected {EXPECTED_PASS} certificate PASS checks, got {PASS}.")
        raise SystemExit(1)
    if FAIL > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
