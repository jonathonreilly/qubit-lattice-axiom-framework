#!/usr/bin/env python3
"""Exploratory finite Newtonian Hartree diagnostics (open_gate).
The supplied solver is not relativistic dynamics. Nonconvergence and censored
scans must remain visible. No stellar stability, horizon exclusion or echo
prediction follows. Original source/output are preserved in the PR9839 archive.
"""

from __future__ import annotations


# Heavy compute / sweep runner — `AUDIT_TIMEOUT_SEC = 1800`
# means the audit-lane precompute and live audit runner allow up to
# 30 min of wall time before recording a timeout. The 120 s default
# ceiling is too tight under concurrency contention; see
# `docs/audit/RUNNER_CACHE_POLICY.md`.
AUDIT_TIMEOUT_SEC = 1800

import math
import sys
import time

import numpy as np
from numpy.linalg import eigh
from scipy import sparse
from scipy.sparse.linalg import eigsh


# ============================================================================
# Physical constants (SI)
# ============================================================================
HBAR = 1.0546e-34       # J s
C = 2.998e8              # m/s
G_SI = 6.674e-11         # m^3 kg^-1 s^-2
M_SUN = 1.989e30         # kg
M_PLANCK = 2.176e-8      # kg
L_PLANCK = 1.616e-35     # m
T_PLANCK = 5.391e-44     # s
M_NUCLEON = 1.673e-27    # kg


# ============================================================================
# 1D Hamiltonian infrastructure (dense, for moderate N)
# ============================================================================

def build_1d_hamiltonian(N: int, t: float = 1.0,
                         potential: np.ndarray | None = None) -> np.ndarray:
    """Tight-binding Hamiltonian on 1D chain with open BC."""
    H = np.zeros((N, N))
    for i in range(N - 1):
        H[i, i + 1] = -t
        H[i + 1, i] = -t
    if potential is not None:
        np.fill_diagonal(H, potential)
    return H


def self_consistent_1d(N: int, n_particles: int, G: float,
                       n_iter: int = 100, damping: float = 0.5,
                       tol: float = 1e-7):
    """Self-consistent Hartree for fermions in their own 1D gravity."""
    V = np.zeros(N)

    for iteration in range(n_iter):
        H = build_1d_hamiltonian(N, t=1.0, potential=V)
        eps, vecs = eigh(H)

        n_occ = min(n_particles, N)
        density = np.zeros(N)
        for k in range(n_occ):
            density += np.abs(vecs[:, k]) ** 2

        V_new = np.zeros(N)
        for i in range(N):
            for j in range(N):
                r = max(abs(i - j), 1)
                V_new[i] -= G * density[j] / r

        change = np.max(np.abs(V_new - V))
        V = damping * V + (1 - damping) * V_new
        if change < tol:
            break

    # Final observables
    H_final = build_1d_hamiltonian(N, t=1.0, potential=V)
    eps_final, vecs_final = eigh(H_final)
    H_kin = build_1d_hamiltonian(N, t=1.0)

    density_final = np.zeros(N)
    E_kin = 0.0
    E_grav = 0.0
    for k in range(n_occ):
        psi = vecs_final[:, k]
        density_final += np.abs(psi) ** 2
        E_kin += psi @ H_kin @ psi
        E_grav += psi @ np.diag(V) @ psi

    positions = np.arange(N, dtype=float)
    total_density = max(np.sum(density_final), 1e-10)
    mean_pos = np.sum(positions * density_final) / total_density
    var_pos = np.sum((positions - mean_pos) ** 2 * density_final) / total_density
    width = np.sqrt(var_pos)
    f_max = np.max(np.abs(V))

    return {
        "density": density_final,
        "potential": V,
        "width": width,
        "E_kin": E_kin,
        "E_grav": E_grav,
        "f_max": f_max,
        "converged": change < tol,
        "n_iterations": iteration + 1,
        "eps": eps_final,
    }


# ============================================================================
# 3D Hamiltonian infrastructure (sparse, for large lattices)
# ============================================================================

def idx_3d(ix, iy, iz, L):
    """Map 3D index to flat index."""
    return ix * L * L + iy * L + iz


def build_3d_hamiltonian_sparse(L: int, t: float = 1.0,
                                potential: np.ndarray | None = None):
    """Tight-binding Hamiltonian on L^3 cubic lattice, sparse."""
    N = L ** 3
    rows, cols, vals = [], [], []

    for ix in range(L):
        for iy in range(L):
            for iz in range(L):
                i = idx_3d(ix, iy, iz, L)
                # Diagonal
                v = 0.0
                if potential is not None:
                    v = potential[i]
                rows.append(i)
                cols.append(i)
                vals.append(v)
                # Hopping to neighbours (open BC)
                for dix, diy, diz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
                    jx, jy, jz = ix+dix, iy+diy, iz+diz
                    if 0 <= jx < L and 0 <= jy < L and 0 <= jz < L:
                        j = idx_3d(jx, jy, jz, L)
                        rows.append(i)
                        cols.append(j)
                        vals.append(-t)

    H = sparse.csr_matrix((vals, (rows, cols)), shape=(N, N))
    return H


def self_consistent_3d(L: int, n_particles: int, G: float,
                       n_iter: int = 60, damping: float = 0.5,
                       tol: float = 1e-5, n_extra_eigs: int = 5):
    """Self-consistent Hartree on L^3 cubic lattice using sparse eigensolver."""
    N = L ** 3
    V = np.zeros(N)

    # Precompute 3D distance table
    center = L // 2
    coords = np.array([(ix, iy, iz)
                        for ix in range(L) for iy in range(L) for iz in range(L)],
                       dtype=float)

    n_occ = min(n_particles, N)
    n_eigs = min(n_occ + n_extra_eigs, N - 1)

    for iteration in range(n_iter):
        H = build_3d_hamiltonian_sparse(L, t=1.0, potential=V)
        eps, vecs = eigsh(H, k=n_eigs, which='SA')
        sort_idx = np.argsort(eps)
        eps = eps[sort_idx]
        vecs = vecs[:, sort_idx]

        density = np.zeros(N)
        for k in range(n_occ):
            density += np.abs(vecs[:, k]) ** 2

        # Gravitational potential from density (O(N^2) — main bottleneck)
        V_new = np.zeros(N)
        for i in range(N):
            dx = coords[i, 0] - coords[:, 0]
            dy = coords[i, 1] - coords[:, 1]
            dz = coords[i, 2] - coords[:, 2]
            r = np.sqrt(dx**2 + dy**2 + dz**2)
            r[r < 1.0] = 1.0  # regularize self-interaction
            V_new[i] = -G * np.sum(density / r)

        change = np.max(np.abs(V_new - V))
        V = damping * V + (1 - damping) * V_new
        if change < tol:
            break

    # Final observables
    H_final = build_3d_hamiltonian_sparse(L, t=1.0, potential=V)
    eps_f, vecs_f = eigsh(H_final, k=n_eigs, which='SA')
    sort_idx = np.argsort(eps_f)
    eps_f = eps_f[sort_idx]
    vecs_f = vecs_f[:, sort_idx]

    density_final = np.zeros(N)
    for k in range(n_occ):
        density_final += np.abs(vecs_f[:, k]) ** 2

    # Width = RMS radius from centre of mass
    total_d = max(np.sum(density_final), 1e-10)
    com = np.sum(coords * density_final[:, None], axis=0) / total_d
    r2 = np.sum(np.sum((coords - com)**2, axis=1) * density_final) / total_d
    width = np.sqrt(r2)
    f_max = np.max(np.abs(V))

    # Kinetic energy: <psi|H_kin|psi>
    H_kin = build_3d_hamiltonian_sparse(L, t=1.0)
    E_kin = 0.0
    for k in range(n_occ):
        psi = vecs_f[:, k]
        E_kin += psi @ H_kin @ psi

    return {
        "density": density_final,
        "potential": V,
        "width": width,
        "E_kin": E_kin,
        "f_max": f_max,
        "converged": change < tol,
        "n_iterations": iteration + 1,
    }


# ============================================================================
# PROBE 1: Analytical scaling argument (lattice-size independent)
# ============================================================================

def probe1_analytical_scaling():
    """Evaluate a supplied nonrelativistic Fermi estimate and packing floor.

    E(R)=C_k N^(5/3)/R^2-C_g N^2/R has stationary radius
    R_Fermi=2C_k/(C_g N^(1/3)). With this model's coefficients this is
    hbar^2(6pi^2)^(2/3)/(G m^3 N^(1/3)). The distinct packing floor is
    a N^(1/3). Neither formula establishes a relativistic stellar solution,
    a horizon statement or the physical Chandrasekhar mass limit.
    """
    print("=" * 72)
    print("PROBE 1: Analytical scaling — lattice-size independent")
    print("=" * 72)

    # ------------------------------------------------------------------
    # Part A: derive key formulae and print them
    # ------------------------------------------------------------------
    print("\n  A) Energy balance on a 3D lattice with spacing a")
    print("  " + "-" * 60)

    # Fermi gas equilibrium radius (supplied nonrelativistic estimate)
    # R_min_Fermi = C_F / (G m^3 N^{1/3})
    #   where C_F = hbar^2 (6pi^2)^{2/3} / 1
    C_F = HBAR**2 * (6 * math.pi**2)**(2/3)
    print(f"  C_F = hbar^2 (6pi^2)^(2/3) = {C_F:.4e} J m^2 kg")

    # Model packing crossover number: N_Ch = [C_F / (G m^3 a)]^{3/2}
    a = L_PLANCK
    m = M_NUCLEON
    N_Ch = (C_F / (G_SI * m**3 * a))**(3/2)
    M_Ch = N_Ch * m
    print(f"\n  Model packing crossover number (a = l_Planck, m = m_nucleon):")
    print(f"    N_Ch = (C_F / G m^3 a)^(3/2) = {N_Ch:.4e}")
    print(f"    M_Ch = N_Ch * m = {M_Ch:.4e} kg = {M_Ch/M_SUN:.2f} M_sun")

    # ------------------------------------------------------------------
    # Part B: R_min / R_Schwarzschild as function of mass
    # ------------------------------------------------------------------
    print(f"\n  B) Compactness: R_min / R_Schwarzschild vs mass")
    print("  " + "-" * 60)

    # Below N_Ch: standard Fermi gas
    #   R_min = C_F / (G m^3 N^{1/3})
    #   R_S = 2 G N m / c^2
    #   R_min / R_S = C_F c^2 / (2 G^2 m^4 N^{4/3})
    #              = (C_F c^2 / (2 G^2 m^4)) * N^{-4/3}

    # Above N_Ch: lattice-limited (packing-floor branch)
    #   R_min = N^{1/3} * a  (every fermion on one lattice site)
    #   R_S = 2 G N m / c^2
    #   R_min / R_S = a c^2 / (2 G m N^{2/3})
    #              = (a c^2 / (2 G m)) * N^{-2/3}

    print(f"\n  {'M / M_sun':>12s}  {'N_particles':>14s}  {'R_min (m)':>12s}  "
          f"{'R_S (m)':>12s}  {'R_min/R_S':>12s}  {'regime':>12s}")

    mass_range_solar = [0.1, 0.5, 1.0, 1.4, 2.0, 5.0, 10.0, 30.0, 60.0, 100.0]
    analytical_results = []

    for M_solar in mass_range_solar:
        M = M_solar * M_SUN
        N_p = M / m

        R_S = 2 * G_SI * M / C**2

        # Fermi gas equilibrium
        R_fermi = C_F / (G_SI * m**3 * N_p**(1/3))

        # Lattice floor
        R_lattice = N_p**(1/3) * a

        if N_p < N_Ch:
            R_min = R_fermi
            regime = "Fermi gas"
        else:
            R_min = R_lattice
            regime = "packing floor"

        ratio = R_min / R_S
        analytical_results.append({
            "M_solar": M_solar, "N": N_p, "R_min": R_min,
            "R_S": R_S, "ratio": ratio, "regime": regime,
        })

        print(f"  {M_solar:12.1f}  {N_p:14.4e}  {R_min:12.4e}  "
              f"{R_S:12.4e}  {ratio:12.4e}  {regime:>12s}")

    # ------------------------------------------------------------------
    # Part C: Key scaling laws
    # ------------------------------------------------------------------
    print(f"\n  C) Key scaling laws (lattice-size INDEPENDENT)")
    print("  " + "-" * 60)
    print(f"  Below Model packing crossover mass ({M_Ch/M_SUN:.2f} M_sun):")
    print(f"    R_min = C_F / (G m^3 N^{{1/3}})  [standard Fermi]")
    print(f"    R_min / R_S = (C_F c^2 / 2G^2 m^4) N^{{-4/3}}")
    print(f"    Compare R_min with R_S separately; Newtonian validity is not guaranteed.")
    print()
    print(f"  Above Model packing crossover mass (packing-floor branch):")
    print(f"    R_min = N^{{1/3}} a  [lattice hard floor]")
    print(f"    R_min / R_S = a c^2 / (2 G m) * N^{{-2/3}}")

    # Evaluate the prefactor
    prefactor = a * C**2 / (2 * G_SI * m)
    print(f"    Prefactor = a c^2 / (2Gm) = {prefactor:.4e}")
    print(f"    At M = M_sun: ratio = {prefactor * (M_SUN/m)**(-2/3):.4e}")
    print(f"    At M = 60 M_sun: ratio = {prefactor * (60*M_SUN/m)**(-2/3):.4e}")
    print()
    print(f"  Critical finding: R_min/R_S -> 0 as M -> infinity")
    print(f"  But R_min > 0 ALWAYS (lattice provides hard floor)")
    print(f"  => No conclusion about curvature singularities or event horizons follows.")
    print(f"  => This is a model packing bound, not a relativistic solution.")

    return {
        "N_Ch": N_Ch,
        "M_Ch_solar": M_Ch / M_SUN,
        "analytical_results": analytical_results,
        "prefactor": prefactor,
    }


# ============================================================================
# PROBE 2: Large 1D lattice verification
# ============================================================================

def probe2_large_1d():
    """Measure finite-width diagnostics on 1D chains of N = 100, 200, 500, 1000."""
    print("\n" + "=" * 72)
    print("PROBE 2: Large 1D lattice verification")
    print("=" * 72)

    lattice_sizes = [100, 200, 500, 1000]
    G = 1.0
    n_particles = 20

    print(f"\n  G = {G}, N_particles = {n_particles}")
    print(f"  Reporting finite iterates; width is not a stability test")
    print(f"\n  {'N_sites':>8s}  {'width':>10s}  {'f_max':>10s}  {'E_kin':>12s}  "
          f"{'E_grav':>12s}  {'converged':>10s}  {'iters':>6s}  {'status':>10s}")

    results = []
    for N in lattice_sizes:
        t0 = time.time()
        r = self_consistent_1d(N, n_particles, G, n_iter=150, tol=1e-8)
        elapsed = time.time() - t0
        collapsed = r["width"] < 2.5
        status = "BELOW_WIDTH_CUT" if collapsed else "ABOVE_WIDTH_CUT"

        results.append({
            "N": N, "width": r["width"], "f_max": r["f_max"],
            "E_kin": r["E_kin"], "E_grav": r["E_grav"],
            "converged": r["converged"], "iters": r["n_iterations"],
            "status": status, "time": elapsed,
        })

        print(f"  {N:8d}  {r['width']:10.4f}  {r['f_max']:10.6f}  "
              f"{r['E_kin']:12.6f}  {r['E_grav']:12.6f}  "
              f"{str(r['converged']):>10s}  {r['n_iterations']:6d}  "
              f"{status:>10s}")

    # Check width convergence: does width plateau as N -> infinity?
    widths = [r["width"] for r in results]
    print(f"\n  Width convergence check:")
    print(f"    N=100:  width = {widths[0]:.4f}")
    print(f"    N=200:  width = {widths[1]:.4f}")
    print(f"    N=500:  width = {widths[2]:.4f}")
    print(f"    N=1000: width = {widths[3]:.4f}")

    if len(widths) >= 2:
        relative_change = abs(widths[-1] - widths[-2]) / max(widths[-2], 1e-10)
        print(f"    Relative change (500->1000): {relative_change:.6f}")
        converged = relative_change < 0.01
        print(f"    Last-two width agreement (< 1% change), not solver convergence: {converged}")

    # Now test at stronger coupling
    print(f"\n  --- Strong coupling G = 3.0 ---")
    G_strong = 3.0
    print(f"  {'N_sites':>8s}  {'width':>10s}  {'f_max':>10s}  {'status':>10s}")

    for N in [100, 200, 500]:
        r = self_consistent_1d(N, n_particles, G_strong, n_iter=150)
        collapsed = r["width"] < 2.5
        status = "BELOW_WIDTH_CUT" if collapsed else "ABOVE_WIDTH_CUT"
        print(f"  {N:8d}  {r['width']:10.4f}  {r['f_max']:10.6f}  {status:>10s} converged={r['converged']}")

    # Scan particle count at various lattice sizes to check N_crit independence
    print(f"\n  --- N_crit vs lattice size at G = 2.0 ---")
    G_test = 2.0
    print(f"  {'N_sites':>8s}  {'N_crit':>8s}  {'width_crit':>12s}")

    ncrit_results = []
    for N in [100, 200, 500]:
        N_crit = None
        scan = []
        for n_p in range(2, 80, 2):
            r = self_consistent_1d(N, n_p, G_test, n_iter=120)
            scan.append({"particles": n_p, "width": r["width"], "converged": r["converged"]})
            print(f"    scan N={N} particles={n_p} width={r['width']:.4f} converged={r['converged']}")
            if r["width"] < 2.5:
                N_crit = n_p
                break
        ncrit_results.append({"N": N, "N_crit": N_crit, "censored_above": 78 if N_crit is None else None, "last_converged": r["converged"], "scan": scan})
        nc_str = str(N_crit) if N_crit else ">78"
        w_str = f"{r['width']:.4f}" if N_crit else "N/A"
        print(f"  {N:8d}  {nc_str:>8s}  {w_str:>12s}")

    print("\n  Censored counts remain >78, not omitted from comparison.")
    print("  No lattice-size independence or stability follows from this finite scan.")

    return {"results": results, "ncrit_results": ncrit_results}


# ============================================================================
# PROBE 3: 3D lattice verification
# ============================================================================

def probe3_3d_lattice():
    """Measure finite-width diagnostics on 3D lattices: L = 6, 8, 10, 12, 14."""
    print("\n" + "=" * 72)
    print("PROBE 3: 3D lattice verification")
    print("=" * 72)

    # Start with smaller sizes to be tractable
    lattice_sides = [6, 8, 10, 12]
    G = 0.5
    n_particles = 8

    print(f"\n  G = {G}, N_particles = {n_particles}")
    print(f"  {'L':>4s}  {'N_sites':>8s}  {'width':>10s}  {'f_max':>10s}  "
          f"{'E_kin':>12s}  {'converged':>10s}  {'iters':>6s}  "
          f"{'time (s)':>10s}  {'status':>10s}")

    results = []
    for L in lattice_sides:
        N_sites = L**3
        t0 = time.time()

        try:
            r = self_consistent_3d(L, n_particles, G,
                                   n_iter=40, damping=0.4, tol=1e-4)
            elapsed = time.time() - t0
            collapsed = r["width"] < 1.5  # tighter threshold for 3D
            status = "BELOW_WIDTH_CUT" if collapsed else "ABOVE_WIDTH_CUT"

            results.append({
                "L": L, "N_sites": N_sites, "width": r["width"],
                "f_max": r["f_max"], "E_kin": r["E_kin"],
                "converged": r["converged"], "iters": r["n_iterations"],
                "status": status, "time": elapsed,
            })

            print(f"  {L:4d}  {N_sites:8d}  {r['width']:10.4f}  "
                  f"{r['f_max']:10.6f}  {r['E_kin']:12.6f}  "
                  f"{str(r['converged']):>10s}  {r['n_iterations']:6d}  "
                  f"{elapsed:10.1f}  {status:>10s}")

        except Exception as e:
            elapsed = time.time() - t0
            print(f"  {L:4d}  {N_sites:8d}  {'FAILED':>10s}  "
                  f"{'':>10s}  {'':>12s}  {'':>10s}  {'':>6s}  "
                  f"{elapsed:10.1f}  {str(e)[:30]}")

    # Check width convergence in 3D
    valid = [r for r in results if r["status"] != "BELOW_WIDTH_CUT"]
    if len(valid) >= 2:
        widths_3d = [(r["L"], r["width"]) for r in valid]
        print(f"\n  3D width convergence:")
        for L, w in widths_3d:
            print(f"    L={L}: width = {w:.4f} (in lattice spacings)")
        if len(widths_3d) >= 2:
            rel = abs(widths_3d[-1][1] - widths_3d[-2][1]) / max(widths_3d[-2][1], 1e-10)
            print(f"    Relative change (last two): {rel:.4f}")
            print(f"    Last-two width agreement (< 5% change), not solver convergence: {rel < 0.05}")

    # Try larger lattice with fewer iterations if tractable
    print(f"\n  --- Attempting L=14 (2744 sites) ---")
    L_large = 14
    try:
        t0 = time.time()
        r = self_consistent_3d(L_large, n_particles, G,
                               n_iter=25, damping=0.4, tol=1e-3)
        elapsed = time.time() - t0
        collapsed = r["width"] < 1.5
        status = "BELOW_WIDTH_CUT" if collapsed else "ABOVE_WIDTH_CUT"
        print(f"  L={L_large}: width = {r['width']:.4f}, f_max = {r['f_max']:.6f}, "
              f"status = {status}, converged={r['converged']}, time = {elapsed:.1f}s")
        results.append({
            "L": L_large, "N_sites": L_large**3, "width": r["width"],
            "f_max": r["f_max"], "status": status, "time": elapsed, "converged": r["converged"],
        })
    except Exception as e:
        print(f"  L={L_large}: FAILED ({e})")

    return {"results": results}


# ============================================================================
# PROBE 4: Compactness ratio R_min/R_S vs mass (numerical confirmation)
# ============================================================================

def probe4_compactness_numerical():
    """Compute finite width divided by the supplied scale 2 G n."""
    print("\n" + "=" * 72)
    print("PROBE 4: Compactness R_min/R_S vs mass (numerical)")
    print("=" * 72)

    N = 500
    G_values = [0.3, 0.5, 1.0, 2.0, 3.0, 5.0]

    print(f"\n  Lattice N = {N}")
    print(f"  Supplied comparison radius 1/(G*N_p); ratio to 2*G*N_p has exponent -2")
    print(f"\n  {'G':>6s}  {'N_p':>6s}  {'R_frozen':>10s}  {'R_S':>10s}  "
          f"{'R/R_S':>10s}  {'R/R_S (analytic)':>18s}  {'status':>10s}")

    results = []
    for G in G_values:
        for n_p in [4, 8, 16, 24, 32, 40, 50]:
            r = self_consistent_1d(N, n_p, G, n_iter=120)
            R_frozen = r["width"]
            R_S = 2.0 * G * n_p
            ratio = R_frozen / max(R_S, 0.01)
            collapsed = R_frozen < 2.5

            # 1D analytic: R_min ~ (t / G N_p)  where t = 1
            # This is a supplied comparison ansatz, not a derived stellar formula
            R_analytic_1d = 1.0 / (G * n_p) if G * n_p > 0 else float('inf')
            ratio_analytic = R_analytic_1d / max(R_S, 0.01)

            status = "BELOW_WIDTH_CUT" if collapsed else "ABOVE_WIDTH_CUT"
            results.append({
                "G": G, "n_p": n_p, "R_frozen": R_frozen,
                "R_S": R_S, "ratio": ratio,
                "ratio_analytic": ratio_analytic,
                "status": status, "converged": r["converged"],
            })

            if True:  # Preserve every width-threshold result.
                print(f"  {G:6.2f}  {n_p:6d}  {R_frozen:10.4f}  {R_S:10.4f}  "
                      f"{ratio:10.4f}  {ratio_analytic:18.4f}  {status:>10s} converged={r['converged']}")

    # Fit the scaling: R/R_S ~ (G * N_p)^alpha
    stable = [r for r in results if r["status"] == "ABOVE_WIDTH_CUT" and r["G"] > 0.2]
    if len(stable) >= 5:
        x = np.log([r["G"] * r["n_p"] for r in stable])
        y = np.log([r["ratio"] for r in stable])
        coeffs = np.polyfit(x, y, 1)
        print(f"\n  Scaling fit: R/R_S ~ (G*N_p)^({coeffs[0]:.3f})")
        print(f"  Supplied 1/(G*N_p) radius ansatz gives ratio exponent -2, not -1")
        print(f"  Deviation from -2: {abs(coeffs[0] + 2):.3f}")

    # Find minimum ratio across all stable configurations
    stable_ratios = [r["ratio"] for r in results if r["status"] == "ABOVE_WIDTH_CUT"]
    if stable_ratios:
        print(f"\n  Minimum width/(2Gn) in above-cut subset: {min(stable_ratios):.4f}")
        most_compact = min([r for r in results if r["status"] == "ABOVE_WIDTH_CUT"],
                          key=lambda x: x["ratio"])
        print(f"  At G={most_compact['G']}, N_p={most_compact['n_p']}")

    return {"results": results}


def main():
    t0 = time.time()
    print("Open finite Hartree diagnostics; no physical stability or echo claim")
    probe1_analytical_scaling()
    probe2_large_1d()
    probe3_3d_lattice()
    probe4_compactness_numerical()
    print("Finite widths and threshold crossings do not certify dynamical stability.")
    print("Nonconverged iterates and censored scans do not establish infinite-volume limits.")
    print(f"Total elapsed: {time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
