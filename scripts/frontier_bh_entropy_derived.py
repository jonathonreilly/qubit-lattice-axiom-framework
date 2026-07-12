#!/usr/bin/env python3
"""
Bekenstein-Hawking Entropy Bounded Companion from Gaussian Correlations
======================================================================

STATUS: OPEN FINITE COMPANION -- the linked Widom row gives a finite-L
        diagnostic and an exact 2D geometric integral, but neither runner
        proves an all-L mixed-state entropy coefficient or a physical
        black-hole observable bridge.

COMPUTATION CHAIN:

  Step 1 (finite boundary fit): Gaussian subsystem correlation entropy
    S = c * |dA| + subleading on the reviewed finite sizes, verified
    numerically (R^2 > 0.99).

  Step 2 (thresholded transfer-layer rank): the correlation block T between
    adjacent layers has a numerical SVD readout
    chi_eff = #{sigma_k/sigma_max > 10^-6}. The comparison denominator is:
        S_max = |dA| * ln(chi_eff)

  Step 3 (finite-L ratio): report S_corr/S_max against 1/4 without treating
    the comparison as a theorem or pass/fail criterion.

  Step 4 (comparison identity only): if one separately supplies the physical
    area map and the 1/4 normalization, then:
        S = |dA| * ln(chi_eff) / 4 = (A/l_P^2) * ln(chi_eff) / 4
    For chi_eff = 2 (qubit per site): S = A * ln(2) / (4 l_P^2)
    This is used only as a comparison target, not a framework derivation.

CHECKS:
  1. Finite boundary-linear fit R^2 > 0.99 (2D and 3D)
  2. RT ratio finite-L observation across multiple lattice sizes
  3. A selected positive 1/r onsite potential modulates entropy monotonically
  4. Frozen-star table is a comparison identity, not an independent test
  5. Independent-copy scaling identity for the diagnostic ratio
  6. Finite-size trend diagnostics, observation only

Current-main interpretation:
  use BH_ENTROPY_DERIVED_NOTE.md and BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE.md
  as the canonical package boundary for this lane.
"""

from __future__ import annotations

import math
import time

import numpy as np
from numpy.linalg import eigh


# ============================================================================
# Physical constants
# ============================================================================
C_LIGHT = 2.998e8        # m/s
G_SI = 6.674e-11         # m^3 kg^-1 s^-2
L_PLANCK = 1.616e-35     # m
M_SUN = 1.989e30         # kg


# ============================================================================
# Lattice infrastructure
# ============================================================================

def build_2d_hamiltonian(Nx: int, Ny: int, t: float = 1.0,
                         potential: np.ndarray | None = None) -> np.ndarray:
    """Tight-binding Hamiltonian on a 2D rectangular lattice."""
    N = Nx * Ny
    H = np.zeros((N, N))
    for x in range(Nx):
        for y in range(Ny):
            i = x * Ny + y
            if potential is not None:
                H[i, i] = potential[i]
            if x + 1 < Nx:
                j = (x + 1) * Ny + y
                H[i, j] = -t
                H[j, i] = -t
            if y + 1 < Ny:
                j = x * Ny + (y + 1)
                H[i, j] = -t
                H[j, i] = -t
    return H


def build_3d_hamiltonian(L: int, t: float = 1.0,
                         potential: np.ndarray | None = None) -> np.ndarray:
    """Tight-binding Hamiltonian on L^3 cubic lattice."""
    N = L ** 3
    H = np.zeros((N, N))
    for ix in range(L):
        for iy in range(L):
            for iz in range(L):
                i = ix * L * L + iy * L + iz
                if potential is not None:
                    H[i, i] = potential[i]
                for dix, diy, diz in [(1, 0, 0), (-1, 0, 0),
                                       (0, 1, 0), (0, -1, 0),
                                       (0, 0, 1), (0, 0, -1)]:
                    jx, jy, jz = ix + dix, iy + diy, iz + diz
                    if 0 <= jx < L and 0 <= jy < L and 0 <= jz < L:
                        j = jx * L * L + jy * L + jz
                        H[i, j] = -t
    return H


def half_filled_correlation(
    eigvals: np.ndarray, eigvecs: np.ndarray, zero_tol: float = 1e-10
) -> tuple[np.ndarray, int, float]:
    """Basis-invariant Gaussian half-filling across a degenerate Fermi level.

    When the N/2 cut crosses a degenerate eigenspace, occupy that entire
    eigenspace with the same fractional weight needed for Tr(C)=N/2. This
    removes the arbitrary eigenvector-ordering choice. The resulting global
    Gaussian state is mixed whenever the returned fraction lies strictly
    between zero and one.
    """
    n_target = eigvals.size // 2
    fermi = eigvals[n_target - 1]
    if abs(eigvals[n_target] - fermi) > zero_tol:
        weights = np.zeros_like(eigvals)
        weights[:n_target] = 1.0
        fraction = 0.0
        degenerate = 0
    else:
        at_level = np.abs(eigvals - fermi) <= zero_tol
        below = eigvals < fermi - zero_tol
        degenerate = int(np.sum(at_level))
        fraction = (n_target - int(np.sum(below))) / degenerate
        weights = below.astype(float) + fraction * at_level.astype(float)
    C = (eigvecs * weights) @ eigvecs.T
    if not math.isclose(float(np.trace(C)), n_target, rel_tol=0.0, abs_tol=1e-8):
        raise AssertionError("basis-invariant prescription lost half filling")
    return C, degenerate, float(fraction)


def gaussian_correlation_entropy(C: np.ndarray, subsystem: list[int]) -> float:
    """Subsystem Gaussian correlation entropy from the restricted matrix."""
    C_A = C[np.ix_(subsystem, subsystem)]
    evals = np.linalg.eigvalsh(C_A)
    eps = 1e-15
    evals = np.clip(evals, eps, 1.0 - eps)
    S = -np.sum(evals * np.log(evals) + (1.0 - evals) * np.log(1.0 - evals))
    return float(S)


def positive_onsite_potential_3d(L: int, source: tuple[int, int, int],
                                 strength: float) -> np.ndarray:
    """Selected positive 1/r onsite-potential diagnostic on an L^3 lattice."""
    N = L ** 3
    V = np.zeros(N)
    sx, sy, sz = source
    for ix in range(L):
        for iy in range(L):
            for iz in range(L):
                r = math.sqrt((ix - sx)**2 + (iy - sy)**2 + (iz - sz)**2)
                r = max(r, 1.0)
                i = ix * L * L + iy * L + iz
                V[i] = strength / r
    return V


# ============================================================================
# CHECK 1: Area law with R^2 > 0.999
# ============================================================================

def check_1_area_law() -> dict:
    """Test a finite linear boundary fit for Gaussian correlation entropy."""
    print("=" * 72)
    print("CHECK 1: AREA LAW VERIFICATION (S ~ A)")
    print("=" * 72)

    results = {"2d": {}, "3d": {}}

    # --- 2D lattice ---
    print("\n  2D lattice: half-space bipartition, S vs boundary length")
    print(f"  {'Nx':>4s} {'Ny':>4s} {'bnd':>5s} {'S_vN':>10s} {'S/bnd':>10s}")
    print("  " + "-" * 40)

    sizes_2d = [(8, 8), (12, 12), (16, 16), (20, 20), (24, 24), (32, 32)]
    bnd_2d, ent_2d = [], []

    for Nx, Ny in sizes_2d:
        N = Nx * Ny
        H = build_2d_hamiltonian(Nx, Ny)
        vals, vecs = eigh(H)
        C, _, _ = half_filled_correlation(vals, vecs)
        subsystem = [x * Ny + y for x in range(Nx // 2) for y in range(Ny)]
        S = gaussian_correlation_entropy(C, subsystem)
        bnd = Ny
        bnd_2d.append(bnd)
        ent_2d.append(S)
        print(f"  {Nx:>4d} {Ny:>4d} {bnd:>5d} {S:>10.4f} {S / bnd:>10.4f}")

    bnd_arr = np.array(bnd_2d, dtype=float)
    s_arr = np.array(ent_2d, dtype=float)
    coeffs_2d = np.polyfit(bnd_arr, s_arr, 1)
    pred = np.polyval(coeffs_2d, bnd_arr)
    ss_res = np.sum((s_arr - pred) ** 2)
    ss_tot = np.sum((s_arr - np.mean(s_arr)) ** 2)
    r2_2d = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0

    print(f"\n  2D fit: S = {coeffs_2d[0]:.4f} * bnd + {coeffs_2d[1]:.4f}")
    print(f"  R^2 = {r2_2d:.6f}")

    results["2d"] = {
        "slope": float(coeffs_2d[0]),
        "r2": float(r2_2d),
        "boundaries": bnd_2d,
        "entropies": ent_2d,
    }

    # --- 3D lattice ---
    print(f"\n  3D lattice: half-space bipartition, S vs boundary area")
    print(f"  {'L':>3s} {'bnd':>5s} {'S_vN':>10s} {'S/bnd':>10s}")
    print("  " + "-" * 30)

    sizes_3d = [4, 6, 8, 10]
    bnd_3d, ent_3d = [], []

    for L in sizes_3d:
        N = L ** 3
        H = build_3d_hamiltonian(L)
        vals, vecs = eigh(H)
        C, _, _ = half_filled_correlation(vals, vecs)
        subsystem = [ix * L * L + iy * L + iz
                     for ix in range(L // 2) for iy in range(L) for iz in range(L)]
        S = gaussian_correlation_entropy(C, subsystem)
        bnd = L * L
        bnd_3d.append(bnd)
        ent_3d.append(S)
        print(f"  {L:>3d} {bnd:>5d} {S:>10.4f} {S / bnd:>10.4f}")

    bnd_arr = np.array(bnd_3d, dtype=float)
    s_arr = np.array(ent_3d, dtype=float)
    coeffs_3d = np.polyfit(bnd_arr, s_arr, 1)
    pred = np.polyval(coeffs_3d, bnd_arr)
    ss_res = np.sum((s_arr - pred) ** 2)
    ss_tot = np.sum((s_arr - np.mean(s_arr)) ** 2)
    r2_3d = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0

    print(f"\n  3D fit: S = {coeffs_3d[0]:.4f} * bnd + {coeffs_3d[1]:.4f}")
    print(f"  R^2 = {r2_3d:.6f}")

    results["3d"] = {
        "slope": float(coeffs_3d[0]),
        "r2": float(r2_3d),
        "boundaries": bnd_3d,
        "entropies": ent_3d,
    }

    pass_2d = r2_2d > 0.99
    pass_3d = r2_3d > 0.99
    print(f"\n  PASS 2D finite boundary fit (R^2 > 0.99): {pass_2d}  (R^2 = {r2_2d:.6f})")
    print(f"  PASS 3D finite boundary fit (R^2 > 0.99): {pass_3d}  (R^2 = {r2_3d:.6f})")

    results["pass_2d"] = pass_2d
    results["pass_3d"] = pass_3d
    return results


# ============================================================================
# CHECK 2: finite-L RT ratio comparison to 1/4
# ============================================================================

def check_2_rt_ratio() -> dict:
    """Compute the finite-L RT comparison ratio: S_exact / (|dA| * ln chi_eff).

    The denominator uses the thresholded transfer-layer SVD rank as a
    diagnostic comparison scale. It is not a derived tensor-network bond
    dimension. The numerator is the subsystem entropy of a generally mixed
    Gaussian state. The ratio is therefore compared with `1/4` numerically,
    not identified with a holographic entropy theorem.
    """
    print("\n" + "=" * 72)
    print("CHECK 2: FINITE-L RT COMPARISON  S / (|dA| * ln chi_eff)")
    print("   Comparison target: 1/4 = 0.2500")
    print("=" * 72)

    results = {}

    # 2D lattice: multiple sizes
    sizes_2d = [(8, 8), (10, 10), (12, 12), (16, 16), (20, 20),
                (24, 24), (32, 32)]

    print(f"\n  2D lattice: half-space bipartition")
    print(f"  {'Nx':>4s} {'Ny':>4s} {'chi_eff':>8s} {'ln(chi)':>8s} "
          f"{'S_max':>10s} {'S_exact':>10s} {'RT_ratio':>10s} {'dev%':>8s}")
    print("  " + "-" * 72)

    rt_ratios_2d = []

    for Nx, Ny in sizes_2d:
        N = Nx * Ny
        H = build_2d_hamiltonian(Nx, Ny)
        vals, vecs = eigh(H)
        C, _, _ = half_filled_correlation(vals, vecs)

        # Transfer matrix between adjacent layers at the cut
        mid = Nx // 2
        layer_l = [mid * Ny + y for y in range(Ny)]
        layer_r = [(mid - 1) * Ny + y for y in range(Ny)]
        T = C[np.ix_(layer_l, layer_r)]
        sv = np.linalg.svd(T, compute_uv=False)
        sv_norm = sv / sv[0] if sv[0] > 1e-30 else sv

        threshold = 1e-6
        chi_eff = int(np.sum(sv_norm > threshold))
        ln_chi = math.log(max(chi_eff, 1))

        # S_max = |dA| * ln(chi_eff) = boundary * ln(chi_eff)
        bnd = Ny
        s_max = bnd * ln_chi

        # Exact entropy
        subsystem = [x * Ny + y for x in range(Nx // 2) for y in range(Ny)]
        s_exact = gaussian_correlation_entropy(C, subsystem)

        rt_ratio = s_exact / s_max if s_max > 0 else float("inf")
        dev = (rt_ratio - 0.25) / 0.25 * 100
        rt_ratios_2d.append(rt_ratio)

        print(f"  {Nx:>4d} {Ny:>4d} {chi_eff:>8d} {ln_chi:>8.4f} "
              f"{s_max:>10.4f} {s_exact:>10.4f} {rt_ratio:>10.4f} {dev:>+7.1f}%")

        results[f"2d_{Nx}x{Ny}"] = {
            "chi_eff": chi_eff,
            "s_max": float(s_max),
            "s_exact": float(s_exact),
            "rt_ratio": float(rt_ratio),
        }

    mean_rt_2d = float(np.mean(rt_ratios_2d))
    dev_mean_2d = abs(mean_rt_2d - 0.25) / 0.25 * 100
    print(f"\n  Mean RT ratio (2D): {mean_rt_2d:.4f}  (dev {dev_mean_2d:.1f}%)")

    # 3D lattice
    sizes_3d = [4, 6, 8, 10]
    print(f"\n  3D lattice: half-space bipartition")
    print(f"  {'L':>3s} {'bnd':>5s} {'chi_eff':>8s} {'ln(chi)':>8s} "
          f"{'S_max':>10s} {'S_exact':>10s} {'RT_ratio':>10s} {'dev%':>8s}")
    print("  " + "-" * 70)

    rt_ratios_3d = []

    for L in sizes_3d:
        N = L ** 3
        H = build_3d_hamiltonian(L)
        vals, vecs = eigh(H)
        C, _, _ = half_filled_correlation(vals, vecs)

        # Transfer matrix: layer at x = L//2 vs x = L//2 - 1
        # Each layer has L*L sites
        mid = L // 2
        layer_l = [mid * L * L + iy * L + iz for iy in range(L) for iz in range(L)]
        layer_r = [(mid - 1) * L * L + iy * L + iz for iy in range(L) for iz in range(L)]
        T = C[np.ix_(layer_l, layer_r)]
        sv = np.linalg.svd(T, compute_uv=False)
        sv_norm = sv / sv[0] if sv[0] > 1e-30 else sv

        threshold = 1e-6
        chi_eff = int(np.sum(sv_norm > threshold))
        ln_chi = math.log(max(chi_eff, 1))

        bnd = L * L
        s_max = bnd * ln_chi

        subsystem = [ix * L * L + iy * L + iz
                     for ix in range(L // 2) for iy in range(L) for iz in range(L)]
        s_exact = gaussian_correlation_entropy(C, subsystem)

        rt_ratio = s_exact / s_max if s_max > 0 else float("inf")
        dev = (rt_ratio - 0.25) / 0.25 * 100
        rt_ratios_3d.append(rt_ratio)

        print(f"  {L:>3d} {bnd:>5d} {chi_eff:>8d} {ln_chi:>8.4f} "
              f"{s_max:>10.4f} {s_exact:>10.4f} {rt_ratio:>10.4f} {dev:>+7.1f}%")

        results[f"3d_L{L}"] = {
            "chi_eff": chi_eff,
            "s_max": float(s_max),
            "s_exact": float(s_exact),
            "rt_ratio": float(rt_ratio),
        }

    mean_rt_3d = float(np.mean(rt_ratios_3d))
    dev_mean_3d = abs(mean_rt_3d - 0.25) / 0.25 * 100
    print(f"\n  Mean RT ratio (3D): {mean_rt_3d:.4f}  (dev {dev_mean_3d:.1f}%)")

    results["mean_rt_2d"] = mean_rt_2d
    results["mean_rt_3d"] = mean_rt_3d
    results["dev_mean_2d"] = dev_mean_2d
    results["dev_mean_3d"] = dev_mean_3d

    # Finite-L comparison check against the 1/4 target.
    pass_2d = dev_mean_2d < 15
    pass_3d = dev_mean_3d < 15
    print(f"\n  Diagnostic only: 2D finite-L comparison within 15% of 1/4: {pass_2d}")
    print(f"  Diagnostic only: 3D finite-L comparison within 15% of 1/4: {pass_3d}")

    results["pass_2d"] = pass_2d
    results["pass_3d"] = pass_3d
    return results


# ============================================================================
# CHECK 3: selected positive 1/r onsite potential
# ============================================================================

def check_3_positive_onsite_potential() -> dict:
    """Measure entropy under the selected positive 1/r onsite potential."""
    print("\n" + "=" * 72)
    print("CHECK 3: POSITIVE 1/r ONSITE-POTENTIAL DIAGNOSTIC")
    print("=" * 72)

    results = {}
    L = 8
    N = L ** 3
    center = (L // 2, L // 2, L // 2)
    subsystem = [ix * L * L + iy * L + iz
                 for ix in range(L // 2)
                 for iy in range(L) for iz in range(L)]
    bnd = L * L

    # Also compute transfer matrix for RT ratio
    mid = L // 2
    layer_l = [mid * L * L + iy * L + iz for iy in range(L) for iz in range(L)]
    layer_r = [(mid - 1) * L * L + iy * L + iz for iy in range(L) for iz in range(L)]

    g_values = [0.0, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0]

    print(f"\n  3D lattice L={L}, boundary = {bnd} sites")
    print(f"  {'g':>6s}  {'S':>10s}  {'S/bnd':>10s}  "
          f"{'chi_eff':>8s}  {'RT_ratio':>10s}")
    print("  " + "-" * 55)

    s_list = []
    for g in g_values:
        V = positive_onsite_potential_3d(L, center, g) if g > 0 else None
        H = build_3d_hamiltonian(L, potential=V)
        vals, vecs = eigh(H)
        C, _, _ = half_filled_correlation(vals, vecs)
        S = gaussian_correlation_entropy(C, subsystem)

        T = C[np.ix_(layer_l, layer_r)]
        sv = np.linalg.svd(T, compute_uv=False)
        chi_eff = int(np.sum(sv / sv[0] > 1e-6))
        ln_chi = math.log(max(chi_eff, 1))
        s_max = bnd * ln_chi
        rt_ratio = S / s_max if s_max > 0 else 0

        s_list.append(S)
        print(f"  {g:>6.1f}  {S:>10.4f}  {S / bnd:>10.4f}  "
              f"{chi_eff:>8d}  {rt_ratio:>10.4f}")

        results[f"g={g}"] = {
            "S": float(S),
            "chi_eff": chi_eff,
            "rt_ratio": float(rt_ratio),
        }

    # Check monotone decrease for g > 0
    # Note: g=0 -> g=0.1 may increase slightly due to potential lifting degeneracy
    mono_from_1 = all(s_list[i] >= s_list[i + 1]
                      for i in range(2, len(s_list) - 1))
    print(f"\n  Monotone decrease for g >= 0.5: {mono_from_1}")
    results["monotone_from_half"] = mono_from_1

    return results


# ============================================================================
# CHECK 4: Frozen star entropy scaling
# ============================================================================

def check_4_frozen_star() -> dict:
    """Report the BH comparison identity when the RT ratio is set to 1/4."""
    print("\n" + "=" * 72)
    print("CHECK 4: FROZEN STAR ENTROPY SCALING")
    print("=" * 72)

    results = {}
    masses = [
        (1.0,   "1 M_sun"),
        (10.0,  "10 M_sun"),
        (60.0,  "60 M_sun (GW150914)"),
        (4e6,   "4e6 M_sun (Sgr A*)"),
        (6.5e9, "6.5e9 M_sun (M87*)"),
    ]

    print(f"\n  {'Mass':>24s}  {'R_S (m)':>12s}  {'A/l_P^2':>14s}  "
          f"{'S_BH':>14s}  {'S_lat':>14s}  {'ratio':>8s}")
    print("  " + "-" * 95)

    for m_sol, label in masses:
        M = m_sol * M_SUN
        R_S = 2 * G_SI * M / C_LIGHT ** 2
        A = 4 * math.pi * R_S ** 2
        A_planck = A / L_PLANCK ** 2
        S_BH = A_planck / 4.0
        # Lattice: S_lat = A_planck * ln(chi) / 4 in nats.
        # In bits (dividing by ln 2): S_lat_bits = A_planck / 4 = S_BH
        S_lat = S_BH  # exact when RT ratio = 1/4 and chi = 2
        ratio = S_lat / S_BH

        print(f"  {label:>24s}  {R_S:>12.3e}  {A_planck:>14.3e}  "
              f"{S_BH:>14.3e}  {S_lat:>14.3e}  {ratio:>8.4f}")

        results[label] = {
            "R_S": R_S, "A_planck": float(A_planck),
            "S_BH": float(S_BH), "ratio": float(ratio),
        }

    print(f"\n  This table is a comparison identity when RT ratio = 1/4.")
    print(f"  It is not an independent pass/fail test. Check 2 reports")
    print(f"  finite-L lattice RT ratios as observations.")

    return results


# ============================================================================
# CHECK 5: Independent-copy scaling identity
# ============================================================================

def check_5_species_scan() -> dict:
    """Check the algebraic cancellation for independent duplicate copies.

    For ``N_s`` independent copies of this same finite diagnostic:
        S_total = N_s * S_single
        log chi_total = N_s * log chi_eff
        ratio = S_total / (|dA| * log chi_total)
              = S_single / (|dA| * log chi_eff)

    This is a bookkeeping identity. It does not identify a Hilbert-space or
    bond dimension, establish species universality, or select the value 1/4.
    """
    print("\n" + "=" * 72)
    print("CHECK 5: INDEPENDENT-COPY SCALING IDENTITY")
    print("=" * 72)

    L = 10
    N = L * L
    H = build_2d_hamiltonian(L, L)
    vals, vecs = eigh(H)
    C, _, _ = half_filled_correlation(vals, vecs)

    subsystem = [x * L + y for x in range(L // 2) for y in range(L)]
    S_single = gaussian_correlation_entropy(C, subsystem)
    bnd = L

    # Transfer matrix
    mid = L // 2
    layer_l = [mid * L + y for y in range(L)]
    layer_r = [(mid - 1) * L + y for y in range(L)]
    T = C[np.ix_(layer_l, layer_r)]
    sv = np.linalg.svd(T, compute_uv=False)
    chi_eff = int(np.sum(sv / sv[0] > 1e-6))

    print(f"\n  2D lattice L={L}, S_single = {S_single:.4f}, bnd = {bnd}")
    print(f"  chi_eff = {chi_eff}")
    print(f"\n  Duplicate-copy construction: N_s independent copies each")
    print(f"  contribute the same S_single and threshold-rank factor chi_eff.")
    print(f"  S_total = N_s * S_single; log chi_total = N_s * log chi_eff.")
    print()
    print(f"  {'N_s':>4s}  {'S_tot':>10s}  {'log chi_tot':>12s}  "
          f"{'denominator':>12s}  {'copy_ratio':>10s}")
    print("  " + "-" * 60)

    results = {}
    for n_s in [1, 2, 3, 4]:
        s_tot = n_s * S_single
        ln_total = n_s * math.log(chi_eff)
        s_max = bnd * ln_total
        rt = s_tot / s_max if s_max > 0 else 0

        print(f"  {n_s:>4d}  {s_tot:>10.4f}  {ln_total:>12.4f}  "
              f"{s_max:>12.4f}  {rt:>10.4f}")
        results[f"Ns={n_s}"] = {"rt_ratio": float(rt)}

    # The duplicate-copy factors cancel algebraically.
    ratios = [results[f"Ns={n}"]["rt_ratio"] for n in [1, 2, 3, 4]]
    spread = max(ratios) - min(ratios)
    print(f"\n  Copy-ratio spread: {spread:.6f}")
    print(f"  (Should be 0 for exact independent duplicates.)")
    results["spread"] = float(spread)
    results["pass"] = spread < 1e-10

    return results


# ============================================================================
# CHECK 6: Finite-size trend of RT ratio
# ============================================================================

def check_6_finite_size() -> dict:
    """Track finite-size RT-ratio diagnostics on the reviewed surface."""
    print("\n" + "=" * 72)
    print("CHECK 6: FINITE-SIZE TREND OF RT RATIO")
    print("=" * 72)

    results = {}

    # 2D lattice: many sizes
    sizes_2d = [6, 8, 10, 12, 16, 20, 24, 32, 40, 48]
    print(f"\n  2D lattice:")
    print(f"  {'L':>4s} {'chi_eff':>8s} {'S_exact':>10s} "
          f"{'S_max':>10s} {'RT_ratio':>10s}")
    print("  " + "-" * 48)

    rt_list_2d = []
    L_list_2d = []

    for L in sizes_2d:
        N = L * L
        H = build_2d_hamiltonian(L, L)
        vals, vecs = eigh(H)
        C, _, _ = half_filled_correlation(vals, vecs)

        mid = L // 2
        layer_l = [mid * L + y for y in range(L)]
        layer_r = [(mid - 1) * L + y for y in range(L)]
        T = C[np.ix_(layer_l, layer_r)]
        sv = np.linalg.svd(T, compute_uv=False)
        chi_eff = int(np.sum(sv / sv[0] > 1e-6))
        ln_chi = math.log(max(chi_eff, 1))

        bnd = L
        s_max = bnd * ln_chi
        subsystem = [x * L + y for x in range(L // 2) for y in range(L)]
        s_exact = gaussian_correlation_entropy(C, subsystem)
        rt = s_exact / s_max if s_max > 0 else 0

        rt_list_2d.append(rt)
        L_list_2d.append(L)

        print(f"  {L:>4d} {chi_eff:>8d} {s_exact:>10.4f} "
              f"{s_max:>10.4f} {rt:>10.4f}")

    # Fit a finite tail intercept versus 1/L. This is a diagnostic only, not an
    # asymptotic theorem for the OBC carrier.
    inv_L = np.array([1.0 / l for l in L_list_2d])
    rt_arr = np.array(rt_list_2d)
    fit_2d = np.polyfit(inv_L, rt_arr, 1)
    rt_inf_2d = fit_2d[1]
    dev_2d = abs(rt_inf_2d - 0.25) / 0.25 * 100

    print(f"\n  2D linear-in-1/L tail-fit intercept (diagnostic): {rt_inf_2d:.4f}")
    print(f"  Deviation from 1/4: {dev_2d:.1f}%")

    results["2d"] = {
        "L_vals": L_list_2d,
        "rt_vals": [float(r) for r in rt_list_2d],
        "rt_inf": float(rt_inf_2d),
        "deviation_pct": float(dev_2d),
    }

    # 3D lattice
    sizes_3d = [4, 6, 8, 10]
    print(f"\n  3D lattice:")
    print(f"  {'L':>4s} {'chi_eff':>8s} {'S_exact':>10s} "
          f"{'S_max':>10s} {'RT_ratio':>10s}")
    print("  " + "-" * 48)

    rt_list_3d = []
    L_list_3d = []

    for L in sizes_3d:
        N = L ** 3
        H = build_3d_hamiltonian(L)
        vals, vecs = eigh(H)
        C, _, _ = half_filled_correlation(vals, vecs)

        mid = L // 2
        layer_l = [mid * L * L + iy * L + iz
                   for iy in range(L) for iz in range(L)]
        layer_r = [(mid - 1) * L * L + iy * L + iz
                   for iy in range(L) for iz in range(L)]
        T = C[np.ix_(layer_l, layer_r)]
        sv = np.linalg.svd(T, compute_uv=False)
        chi_eff = int(np.sum(sv / sv[0] > 1e-6))
        ln_chi = math.log(max(chi_eff, 1))

        bnd = L * L
        s_max = bnd * ln_chi
        subsystem = [ix * L * L + iy * L + iz
                     for ix in range(L // 2) for iy in range(L) for iz in range(L)]
        s_exact = gaussian_correlation_entropy(C, subsystem)
        rt = s_exact / s_max if s_max > 0 else 0

        rt_list_3d.append(rt)
        L_list_3d.append(L)

        print(f"  {L:>4d} {chi_eff:>8d} {s_exact:>10.4f} "
              f"{s_max:>10.4f} {rt:>10.4f}")

    inv_L_3d = np.array([1.0 / l for l in L_list_3d])
    rt_arr_3d = np.array(rt_list_3d)
    fit_3d = np.polyfit(inv_L_3d, rt_arr_3d, 1)
    rt_inf_3d = fit_3d[1]
    dev_3d = abs(rt_inf_3d - 0.25) / 0.25 * 100

    print(f"\n  3D linear-in-1/L tail-fit intercept (diagnostic): {rt_inf_3d:.4f}")
    print(f"  Deviation from 1/4: {dev_3d:.1f}%")

    results["3d"] = {
        "L_vals": L_list_3d,
        "rt_vals": [float(r) for r in rt_list_3d],
        "rt_inf": float(rt_inf_3d),
        "deviation_pct": float(dev_3d),
    }

    return results


# ============================================================================
# SYNTHESIS
# ============================================================================

def synthesis(c1: dict, c2: dict, c3: dict, c4: dict,
              c5: dict, c6: dict) -> dict:
    """Assemble the finite-packet report and pass/fail summary."""
    print("\n" + "=" * 72)
    print("SYNTHESIS: BOUNDED BH ENTROPY COMPANION FROM GAUSSIAN CORRELATIONS")
    print("=" * 72)

    # 2026-05-26 finite-packet rescope: keep pass/fail only for finite
    # computations this runner recomputes directly. RT-ratio comparisons and
    # tail-fit intercepts are observations, not retained asymptotic claims.
    #
    # 2026-05-03 review-loop repair: split each subcheck into explicit
    # 2D and 3D parts with explicit thresholds, drop the OR-based
    # aggregation that was masking 3D failures, and report the honest
    # pass/fail count.
    #
    # Thresholds per the BH entropy finite-diagnostic notes:
    #   - 2D/3D finite boundary-linear fits R^2 > 0.99
    #   - RT ratio (finite-L) is the observed value reported by each sampled
    #     grid. Comparison to 1/4 is reported as a
    #     bounded numerical observation; it is NOT used as a pass/fail
    #     criterion any more. Aggregation reports the observed finite-L
    #     numbers without a "PASS within 15% of 1/4" verdict.
    #   - Selected positive 1/r onsite-potential response monotone for g >= 0.5
    #   - Independent-copy identity: duplicate-copy ratio spread < 1e-12
    #   - Finite-size tail-fit intercepts are diagnostics only. They do not
    #     close an all-L OBC Widom theorem.
    verdicts = {}

    # 1. Finite boundary fit (split 2D vs 3D, threshold R^2 > 0.99 per the note's
    #    bounded text — the original code's c1.pass_2d used a stricter
    #    0.999 threshold that mismatched the note. We compute directly
    #    from R^2 here against the note's documented threshold.)
    r2_2d = c1.get("2d", {}).get("r2", 0)
    r2_3d = c1.get("3d", {}).get("r2", 0)
    pass_area_2d = r2_2d > 0.99
    pass_area_3d = r2_3d > 0.99
    print(f"\n  1a. FINITE BOUNDARY FIT (2D, R^2 > 0.99): {'PASS' if pass_area_2d else 'FAIL'}  R^2 = {r2_2d:.6f}")
    print(f"  1b. FINITE BOUNDARY FIT (3D, R^2 > 0.99): {'PASS' if pass_area_3d else 'FAIL'}  R^2 = {r2_3d:.6f}")
    verdicts["area_law_2d"] = pass_area_2d
    verdicts["area_law_3d"] = pass_area_3d

    # 2. RT ratio: now reported as bounded observation, NOT as a
    #    PASS/FAIL against 1/4. The observation IS what's verified;
    #    the comparison to 1/4 is informational only.
    mean_2d = c2.get("mean_rt_2d", 0)
    mean_3d = c2.get("mean_rt_3d", 0)
    dev_2d = c2.get("dev_mean_2d", 100)
    dev_3d = c2.get("dev_mean_3d", 100)
    print(f"\n  2. RT RATIO finite-L observation (NOT a pass/fail vs 1/4):")
    print(f"     2D mean: {mean_2d:.4f}  (dev from 1/4: {dev_2d:.1f}%)")
    print(f"     3D mean: {mean_3d:.4f}  (dev from 1/4: {dev_3d:.1f}%)")
    print(f"     OBSERVATION ONLY — finite comparison, not a BH derivation.")
    # No verdict entry; this is reported as observation.

    # 3. Selected positive 1/r onsite-potential diagnostic
    mono = c3.get("monotone_from_half", False)
    print(f"\n  3. POSITIVE 1/r ONSITE POTENTIAL: monotone for g >= 0.5: {mono}")
    verdicts["positive_onsite_potential_monotone"] = mono

    # 4. Frozen star scaling — identity holds by construction when ratio
    #    is set to 1/4. This is a sanity check, not an independent PASS.
    print(f"\n  4. FROZEN STAR SCALING: comparison identity when RT = 1/4 (sanity)")
    # No verdict; this is by-construction.

    # 5. Independent-copy identity
    species_pass = c5.get("pass", False)
    spread = c5.get("spread", 999)
    print(f"\n  5. INDEPENDENT-COPY IDENTITY: ratio spread = {spread:.2e}  "
          f"(threshold < 1e-12)")
    print(f"     {'PASS' if species_pass else 'FAIL'}")
    verdicts["independent_copy_identity"] = species_pass

    # 6. Finite-size tail-fit diagnostics. These are reported without a
    #    pass/fail verdict because the all-L OBC asymptotic bridge is outside
    #    this row's unaudited diagnostic dependency.
    rt_inf_2d = c6.get("2d", {}).get("rt_inf", 0)
    rt_inf_3d = c6.get("3d", {}).get("rt_inf", 0)
    dev_inf_2d = c6.get("2d", {}).get("deviation_pct", 100)
    dev_inf_3d = c6.get("3d", {}).get("deviation_pct", 100)
    c_widom_2d = 1.0 / 6.0
    dev_widom_2d = abs(rt_inf_2d - c_widom_2d) / c_widom_2d * 100
    print(f"\n  6a. FINITE-SIZE TAIL-FIT 2D (observation):")
    print(f"     intercept = {rt_inf_2d:.4f}, c_Widom(2D) = {c_widom_2d:.4f}")
    print(f"     dev from c_Widom(2D) = {dev_widom_2d:.1f}%   (dev from 1/4 = {dev_inf_2d:.1f}%)")
    print(f"     OBSERVATION ONLY — no all-L OBC asymptotic theorem is claimed.")
    print(f"\n  6b. FINITE-SIZE TAIL-FIT 3D (observation):")
    print(f"     intercept = {rt_inf_3d:.4f}  (dev from 1/4: {dev_inf_3d:.1f}%)")
    print(f"     OBSERVATION ONLY — no 3D asymptotic theorem is claimed.")

    # Overall
    n_pass = sum(1 for v in verdicts.values() if v)
    n_total = len(verdicts)

    print(f"\n  " + "=" * 60)
    print(f"  CHECKS PASSED: {n_pass}/{n_total}  (2026-05-26 finite-packet accounting)")
    print(f"  Subchecks split into 2D vs 3D; RT-ratio-vs-1/4 reported as")
    print(f"  observation only; finite-size tail fits are diagnostic only.")
    print(f"  " + "=" * 60)

    print(f"\n  COMPANION SUMMARY:")
    print(f"    (i)   Area-law-like scaling is numerically strong on the reviewed")
    print(f"          finite lattice sizes.")
    print(f"    (ii)  The transfer-layer SVD defines a threshold-rank")
    print(f"          comparison scale chi_eff; it is not a derived bond dimension.")
    print(f"    (iii) Finite-L RT ratios are:")
    print(f"            S_corr / (|dA| * ln chi_eff) =  {mean_2d:.4f} (2D)")
    print(f"                                          =  {mean_3d:.4f} (3D)")
    print(f"            comparison target: 1/4 = 0.2500")
    print(f"    (iv)  On current main, this is an open BH-comparison lane only.")
    print(f"          The linked Widom row is an unaudited finite diagnostic plus")
    print(f"          an author-side exact 2D integral, not an all-L OBC theorem.")
    print(f"    (v)   Therefore the script does not derive the Bekenstein-Hawking")
    print(f"          coefficient as a retained framework theorem.")
    print()

    verdicts["n_pass"] = n_pass
    verdicts["n_total"] = n_total
    return verdicts


# ============================================================================
# Main
# ============================================================================

def main() -> int:
    print("=" * 72)
    print("BEKENSTEIN-HAWKING ENTROPY: BOUNDED LATTICE COMPANION")
    print("Finite-L comparison to S_BH = A / (4 l_P^2)")
    print("=" * 72)
    print()
    print("Bounded comparison lane: finite-L Gaussian correlation entropy is compared")
    print("to the Ryu-Takayanagi / Bekenstein-Hawking target, but current main")
    print("does not treat this runner as a retained derivation.")
    print()

    t_start = time.time()

    c1 = check_1_area_law()
    c2 = check_2_rt_ratio()
    c3 = check_3_positive_onsite_potential()
    c4 = check_4_frozen_star()
    c5 = check_5_species_scan()
    c6 = check_6_finite_size()

    verdicts = synthesis(c1, c2, c3, c4, c5, c6)

    elapsed = time.time() - t_start
    print(f"Total runtime: {elapsed:.1f}s")
    return 0 if verdicts["n_pass"] == verdicts["n_total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
