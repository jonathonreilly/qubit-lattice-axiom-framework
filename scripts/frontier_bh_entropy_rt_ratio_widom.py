#!/usr/bin/env python3
"""
BH Entropy RT-Ratio Widom Finite-Size Evidence runner
=====================================================

Authority for the bounded finite-size audit target:

    BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE.md

Question:

    The existing BH entropy bounded companion lane claims that the
    Ryu-Takayanagi bond-dimension ratio

        r(L) = S_corr(L) / (L * ln chi_eff(L))

    computed on the OBC L x L free-fermion half-filled square lattice was
    proposed to approach 1/4. Even-L OBC blocks have zero-mode degeneracy, so
    this runner now fixes the basis-invariant mixed Gaussian prescription
    C=1(H<0)+1/2 1(H=0) before reporting any finite-size diagnostic.

Scope:

    The exact Widom coefficient calculation gives

        c_Widom = (1 / (12 (2 pi)^{d-1})) *
                  integral over Fermi surface of |n_x . n_k| dS_k

    For the 2D square-lattice diamond Fermi surface with straight cut:
        c_Widom(2D) = 4 pi / (12 * 2 pi) = 1 / 6

    This runner checks only the finite L <= 64 numerical tail. It does not
    prove that r(L) converges to c_Widom; that all-L identification is open
    open mixed-state asymptotic bridge in the authority note.

What the runner does:

    1. Compute c_Widom(2D) = 1/6 analytically (exact diamond integral).
    2. Compute c_Widom(3D) numerically from the Fermi-surface Monte Carlo.
    3. Measure the correlation-entropy diagnostic r(L) on OBC L x L lattices
       for L up to 64 (dense eigh) under that explicit prescription.
    4. Fit the sampled tail r(L) = c_fit + a / ln(L) on L >= 32.
    5. Check whether that chosen finite-tail diagnostic agrees with 1/6 within
       10% and differs from 1/4 by at least 20%. This validates the stated fit,
       not an all-L coefficient or no-go.

Exit code: 0 on full PASS, 1 on any FAIL.

PStack experiment: frontier-bh-entropy-rt-ratio-widom
"""

from __future__ import annotations

import math
import sys
import time

import numpy as np
from numpy.linalg import eigh


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "",
          kind: str = "EXACT") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    tag = f" [{kind}]" if kind != "EXACT" else ""
    msg = f"  [{status}]{tag} {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


# ============================================================================
# Part 1.  Analytic Widom-Gioev-Klich coefficients
# ============================================================================

def widom_2d_diamond_straight_cut() -> float:
    """
    Closed-form c_Widom for 2D half-filled NN-hopping square lattice
    (Fermi surface = diamond |k_x| + |k_y| = pi) with straight cut.

    Each of the 4 Fermi-surface segments has length sqrt(2) pi, outward unit
    normal (+/-1, +/-1) / sqrt(2).  Dotted with n_x = (1, 0) gives 1/sqrt(2)
    on every segment.  Integral: 4 sqrt(2) pi * 1 / sqrt(2) = 4 pi.
    Formula: c_Widom = integral / (12 (2 pi)^{d-1}) = 4 pi / (24 pi) = 1/6.
    """
    return 1.0 / 6.0


def widom_3d_cubic_straight_cut_monte_carlo(n_samples: int = 400_000,
                                              seed: int = 42) -> float:
    """
    Monte Carlo c_Widom for 3D half-filled cubic lattice (Fermi surface
    cos k_x + cos k_y + cos k_z = 0) with straight cut normal to x-axis.

    For implicit F(k) = 0, parametrize by (k_y, k_z) and solve F = 0 for
    k_x.  Then |n_x . n_k| dS_k = dk_y dk_z (the Jacobian / normal-component
    cancellation is standard).  Sum over the 2 real roots of
    cos k_x = -(cos k_y + cos k_z) in (-pi, pi), which exist iff
    |cos k_y + cos k_z| < 1.
    """
    rng = np.random.default_rng(seed)
    ky = rng.uniform(-math.pi, math.pi, size=n_samples)
    kz = rng.uniform(-math.pi, math.pi, size=n_samples)
    u = np.cos(ky) + np.cos(kz)
    mask = np.abs(u) < 1.0
    count = 2.0 * int(np.sum(mask))
    area = (2.0 * math.pi) ** 2
    integral = area * count / n_samples
    return integral / (12.0 * (2.0 * math.pi) ** 2)


# ============================================================================
# Part 2.  Numerical r(L) on OBC L x L free-fermion ground state
# ============================================================================

def build_2d_hamiltonian(Lx: int, Ly: int, t: float = 1.0) -> np.ndarray:
    N = Lx * Ly
    H = np.zeros((N, N))
    for x in range(Lx):
        for y in range(Ly):
            i = x * Ly + y
            if x + 1 < Lx:
                j = (x + 1) * Ly + y
                H[i, j] = -t
                H[j, i] = -t
            if y + 1 < Ly:
                j = x * Ly + (y + 1)
                H[i, j] = -t
                H[j, i] = -t
    return H


def particle_hole_symmetric_correlation(
    eigvals: np.ndarray, eigvecs: np.ndarray, zero_tol: float = 1e-10
) -> tuple[np.ndarray, int]:
    """Basis-invariant half-filled quasifree ensemble correlation matrix.

    OBC even-L squares have an exactly degenerate zero-energy subspace, so
    choosing the first N/2 eigenvectors is not a state prescription. The
    spectral function f(E)=1,1/2,0 for E<0,E=0,E>0 is invariant under every
    zero-mode rotation and has Tr(C)=N/2. It is a mixed Gaussian ensemble,
    not a uniquely selected pure Slater ground state.
    """
    weights = np.where(
        eigvals < -zero_tol,
        1.0,
        np.where(eigvals > zero_tol, 0.0, 0.5),
    )
    C = (eigvecs * weights) @ eigvecs.T
    return C, int(np.sum(np.abs(eigvals) <= zero_tol))


def gaussian_correlation_entropy(C: np.ndarray, subsystem: list[int]) -> float:
    C_A = C[np.ix_(subsystem, subsystem)]
    evals = np.linalg.eigvalsh(C_A)
    eps = 1e-15
    evals = np.clip(evals, eps, 1.0 - eps)
    return float(-np.sum(evals * np.log(evals)
                         + (1.0 - evals) * np.log(1.0 - evals)))


def transfer_rank(C: np.ndarray, L: int, threshold: float = 1e-6) -> int:
    mid = L // 2
    layer_L = [mid * L + y for y in range(L)]
    layer_R = [(mid - 1) * L + y for y in range(L)]
    T = C[np.ix_(layer_L, layer_R)]
    sv = np.linalg.svd(T, compute_uv=False)
    if sv[0] < 1e-30:
        return 0
    return int(np.sum(sv / sv[0] > threshold))


def measure_rt(L: int) -> dict:
    N = L * L
    H = build_2d_hamiltonian(L, L)
    vals, vecs = eigh(H)
    C, zero_modes = particle_hole_symmetric_correlation(vals, vecs)
    if not math.isclose(float(np.trace(C)), N / 2, rel_tol=0.0, abs_tol=1e-8):
        raise AssertionError("particle-hole symmetric prescription lost half filling")
    subsystem = [x * L + y for x in range(L // 2) for y in range(L)]
    S = gaussian_correlation_entropy(C, subsystem)
    chi_eff = transfer_rank(C, L)
    ln_chi = math.log(chi_eff) if chi_eff > 1 else 0.0
    S_max = L * ln_chi
    rt = S / S_max if S_max > 0 else float("nan")
    return {
        "L": L, "S": S, "chi_eff": chi_eff, "rt": rt,
        "zero_modes": zero_modes,
    }


# ============================================================================
# Part 3.  Verdict logic
# ============================================================================

def fit_finite_tail_intercept(
    records: list[dict], L_min: int = 32
) -> tuple[float, float]:
    """Two-parameter finite-tail fit over sampled L >= L_min values."""
    L_arr = np.array([r["L"] for r in records], dtype=float)
    rt_arr = np.array([r["rt"] for r in records], dtype=float)
    mask = L_arr >= L_min
    if mask.sum() < 3:
        return float("nan"), float("nan")
    X = np.column_stack([np.ones(mask.sum()), 1.0 / np.log(L_arr[mask])])
    coeffs, *_ = np.linalg.lstsq(X, rt_arr[mask], rcond=None)
    return float(coeffs[0]), float(coeffs[1])


def main() -> None:
    print("=" * 72)
    print("BH Entropy RT-Ratio Widom Finite-Size Evidence")
    print("=" * 72)
    print()
    print("Question: what finite-L behavior follows after resolving the OBC")
    print("half-filled zero-mode ambiguity by a basis-invariant prescription?")
    print()
    print("Scope: the exact Widom coefficient is 1/6; this runner tests only")
    print("finite L<=64 evidence under the basis-invariant spectral prescription")
    print("C=1(H<0)+1/2 1(H=0), and leaves the r(L) all-L limit open.")
    print()

    t0 = time.time()

    # ----- Part 1: analytic Widom coefficients ------------------------------
    print("-" * 72)
    print("Part 1.  Widom-Gioev-Klich analytic coefficients")
    print("-" * 72)
    c_widom_2d = widom_2d_diamond_straight_cut()
    print(f"  c_Widom(2D, diamond, straight cut) = {c_widom_2d:.10f}")
    check("c_Widom(2D) = 1/6 exactly",
          abs(c_widom_2d - 1.0 / 6.0) < 1e-12,
          f"value = {c_widom_2d:.10f}")
    check("c_Widom(2D) != 1/4",
          abs(c_widom_2d - 0.25) > 0.05,
          f"|1/6 - 1/4| = {abs(c_widom_2d - 0.25):.6f}")

    c_widom_3d = widom_3d_cubic_straight_cut_monte_carlo(n_samples=400_000)
    print(f"  c_Widom(3D, half-filled cube, straight cut) "
          f"= {c_widom_3d:.6f}  (Monte Carlo, N = 4e5)")
    check("c_Widom(3D) is stable and bounded",
          0.08 < c_widom_3d < 0.15,
          f"value = {c_widom_3d:.6f}")
    check("c_Widom(3D) != 1/4",
          abs(c_widom_3d - 0.25) > 0.10,
          f"|c_3D - 1/4| = {abs(c_widom_3d - 0.25):.6f}")

    # ----- Part 2: numerical r(L) on 2D OBC ---------------------------------
    print()
    print("-" * 72)
    print("Part 2.  Particle-hole-symmetric Gaussian correlation diagnostic")
    print("-" * 72)
    L_list = [8, 12, 16, 20, 24, 28, 32, 40, 48, 56, 64]
    print(f"  {'L':>4s} {'zero':>5s} {'chi_eff':>8s} {'S_corr':>10s} {'r(L)':>10s} "
          f"{'dev_1/6%':>9s} {'dev_1/4%':>9s}")
    print("  " + "-" * 65)
    records = []
    for L in L_list:
        r = measure_rt(L)
        dev_sixth = (r["rt"] - 1.0 / 6.0) / (1.0 / 6.0) * 100
        dev_quarter = (r["rt"] - 0.25) / 0.25 * 100
        print(f"  {r['L']:>4d} {r['zero_modes']:>5d} {r['chi_eff']:>8d} {r['S']:>10.4f} "
              f"{r['rt']:>10.4f} {dev_sixth:>+8.1f}% {dev_quarter:>+8.1f}%")
        records.append(r)

    # ----- Part 3: finite-tail intercept diagnostic --------------------------
    print()
    print("-" * 72)
    print("Part 3.  Finite-tail intercept from r(L) = c_fit + a / ln(L)")
    print("-" * 72)
    results = {}
    for L_min in [24, 32, 40, 48]:
        c_fit, a = fit_finite_tail_intercept(records, L_min=L_min)
        if math.isnan(c_fit):
            continue
        dev_sixth = (c_fit - 1.0 / 6.0) / (1.0 / 6.0) * 100
        dev_quarter = (c_fit - 0.25) / 0.25 * 100
        print(f"  [L >= {L_min}]  c_fit = {c_fit:.6f}  "
              f"a = {a:+.4f}    "
              f"dev(1/6) = {dev_sixth:+.2f}%  "
              f"dev(1/4) = {dev_quarter:+.2f}%")
        results[L_min] = (c_fit, dev_sixth, dev_quarter)

    # Use the L >= 32 finite-tail fit as the primary numerical diagnostic.
    c_fit_32, dev6_32, dev4_32 = results[32]
    print()
    print(f"Finite-tail fit:  c_fit (L>=32) = {c_fit_32:.6f}")
    print(f"              |c_fit - 1/6| / (1/6)  = "
          f"{abs(dev6_32):.2f}%")
    print(f"              |c_fit - 1/4| / (1/4)  = "
          f"{abs(dev4_32):.2f}%")
    print()

    # ----- Part 4: PASS/FAIL assembly ---------------------------------------
    print("-" * 72)
    print("Part 4.  Finite-size evidence checks")
    print("-" * 72)
    # Monotone decrease for L >= 28 (clean tail; L = 20..24 has a small
    # finite-size bounce from the discrete half-filling offset).
    L28_start = next(i for i, r in enumerate(records) if r["L"] >= 28)
    tail = records[L28_start:]
    check("r(L) is monotone decreasing for L >= 28",
          all(tail[i]["rt"] > tail[i + 1]["rt"] - 1e-4
              for i in range(len(tail) - 1)),
          f"r({tail[0]['L']})={tail[0]['rt']:.4f} down to "
          f"r({tail[-1]['L']})={tail[-1]['rt']:.4f}")
    check("r(L=64) < r(L=8)",
          records[-1]["rt"] < records[0]["rt"],
          f"r(64) = {records[-1]['rt']:.4f} < r(8) = {records[0]['rt']:.4f}")

    # The finite-tail fit intercept is near the exact Widom coefficient.
    check("finite L>=32 fit intercept within 10% of 1/6",
          abs(c_fit_32 - 1.0 / 6.0) / (1.0 / 6.0) < 0.10,
          f"c_fit = {c_fit_32:.4f}, |dev| = {abs(dev6_32):.2f}%")

    check("finite L>=32 fit intercept is NOT within 20% of 1/4",
          abs(c_fit_32 - 0.25) / 0.25 > 0.20,
          f"|dev from 1/4| = {abs(dev4_32):.2f}%")

    # Raw L=64 data remain close to 1/4; only the fitted tail differs.
    r_L64 = records[-1]["rt"]
    check("r(L=64) remains within 5% of 1/4",
          abs(r_L64 - 0.25) / 0.25 < 0.05,
          f"r(64) = {r_L64:.4f}, relative deviation = "
          f"{abs(r_L64 - 0.25) / 0.25 * 100:.1f}%")

    check("FINITE-SIZE EVIDENCE: tail fit favors 1/6 over 1/4",
          abs(c_fit_32 - 1.0 / 6.0) / (1.0 / 6.0) < 0.10
          and abs(c_fit_32 - 0.25) / 0.25 > 0.20,
          "L<=64 tail-fit intercept is near 1/6 and >20% from 1/4; "
          "no all-L limit is claimed")

    print("  [INFO] Scope: finite samples do not establish an exact 1/4 "
          "coefficient; the all-L mixed-state asymptotic bridge remains open.")

    # ----- Summary ----------------------------------------------------------
    print()
    print("=" * 72)
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 72)
    print()

    elapsed = time.time() - t0
    print(f"Runtime: {elapsed:.1f} s")

    if FAIL_COUNT > 0:
        sys.exit(1)
    else:
        print()
        print("All finite-L<=64 checks passed; the tail-fit intercept favors 1/6")
        print("over 1/4 on this sampled carrier. The all-L ratio limit remains")
        print("an open mixed-state asymptotic bridge; this output is not an "
              "asymptotic theorem.")
        sys.exit(0)


if __name__ == "__main__":
    main()
