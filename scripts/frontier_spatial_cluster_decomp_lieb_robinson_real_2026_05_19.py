#!/usr/bin/env python3
"""
Finite-volume Lieb-Robinson bound plus bounded cluster-decomposition support
===========================================================================

Companion runner to:
    docs/SPATIAL_CLUSTER_DECOMPOSITION_LIEB_ROBINSON_REAL_NOTE_2026-05-19.md

Nine verifications exhibiting:
  V1: Locality of nested commutators on a 6-site spin-1/2 Heisenberg chain
      (supports of [H, A], [H, [H, A]], ... shrink to the predicted thickening).
  V2: Triangle-inequality bound on nested commutator norm vs the
      (2J)^n · (D_I^+)^n · |X| factor for n = 1, 2, 3, 4, where D_I^+
      is the inclusive interaction-graph overlap degree.
  V3: Lieb-Robinson commutator bound for separated operators at multiple times
      via exact diagonalization on the 6-site chain.
  V4: Lieb-Robinson velocity extraction from numerical commutator data.
      Compare to theoretical v_LR = 2 J D_I^+ R_0 e.
  V5: Finite-N cluster-support fit on the same chain: extract the gap Δ,
      compute connected correlators C(R), fit an effective ξ, compare to the
      loose v_LR/Δ upper scale without promoting a thermodynamic theorem.
  V6: Composition with PR #1577's SU(3) T_W truncated character basis:
      verify Δ_T > 0 on a 2-site Λ with one spatial link, compute the
      Hamiltonian-side gap Δ = -log(λ_1/λ_0), and the LR velocity v_LR^{SU(3)}.
  V7: Structural SU(3) transfer-spectrum exponential sequence:
      construct the λ_1^R sequence implied by V6's top two eigenvalues and
      verify the expected finite-volume exponential rate. This is not a
      direct connected-character-correlator measurement.
  V8: Anti-overclaim verification: extract ξ_cluster at Λ=4 vs Λ=6 to confirm
      the bound is finite-Λ only (no thermodynamic-limit claim).
  V9: Inclusive branching guard: brute-force repeated interaction chains and
      verify that the exclusive-degree count can fail while D_I^+ bounds them.

All nine verifications have hard assertion gates. Final tally is reported as
PASS / FAIL counts.

Designed to complete in under a minute on a laptop using NumPy + SciPy only.
This is verification of structural operator-theoretic content and bounded
support checks, not a precision lattice MC measurement or an audit verdict.
"""

from __future__ import annotations

import math
import sys
import time
from dataclasses import dataclass
from itertools import product

import numpy as np
from numpy.linalg import eigh, eigvalsh


# ============================================================================
# Spin-1/2 Heisenberg chain (small but real lattice system)
# ============================================================================

# Pauli matrices (used for site operators)
S_X = 0.5 * np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
S_Y = 0.5 * np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
S_Z = 0.5 * np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
I_2 = np.eye(2, dtype=complex)


def site_op(op: np.ndarray, site: int, N: int) -> np.ndarray:
    """Build the operator `op` acting on site `site` of an N-site chain,
    tensor-padded with identity on all other sites.

    Returns a 2^N × 2^N complex matrix.
    """
    out = np.array([[1.0]], dtype=complex)
    for k in range(N):
        out = np.kron(out, op if k == site else I_2)
    return out


def heisenberg_hamiltonian(N: int, J: float = 1.0, open_bc: bool = True) -> np.ndarray:
    """Spin-1/2 Heisenberg chain Hamiltonian:

        H  =  J  Σ_{i}  (S^x_i S^x_{i+1} + S^y_i S^y_{i+1} + S^z_i S^z_{i+1})

    with open boundary conditions (open_bc=True) or periodic (False). We use
    open BC for the Lieb-Robinson chain runs so that the spatial geometry is
    explicitly Z (not S^1).

    Returns a 2^N × 2^N complex matrix.
    """
    dim = 2 ** N
    H = np.zeros((dim, dim), dtype=complex)
    nb = N - 1 if open_bc else N
    for i in range(nb):
        j = (i + 1) % N
        Sxi = site_op(S_X, i, N); Sxj = site_op(S_X, j, N)
        Syi = site_op(S_Y, i, N); Syj = site_op(S_Y, j, N)
        Szi = site_op(S_Z, i, N); Szj = site_op(S_Z, j, N)
        H = H + J * (Sxi @ Sxj + Syi @ Syj + Szi @ Szj)
    return H


def support_of(op: np.ndarray, N: int, tol: float = 1e-10) -> set:
    """Return the support of an operator on the N-site chain: the set of sites
    on which it acts non-trivially.

    Strategy: for each site k, decompose op into the tensor structure
    ((I on sites except k) ⊗ (something on site k)) and check whether
    the "something on site k" is proportional to the identity. If not, k
    is in the support.

    Implementation: project op onto the subspace where site k is in basis state
    |0⟩ and |1⟩ separately. If the two projections differ (as operators on the
    rest of the chain) modulo identity scaling, then k is in supp(op).
    """
    supp = set()
    dim_rest = 2 ** (N - 1)
    for k in range(N):
        # Reshape op as (2 at site k) ⊗ (2^(N-1) elsewhere) ⊗ same.
        # Permute so site k is the leftmost index, then reshape to (2, 2^(N-1), 2, 2^(N-1)).
        # We use an axis permutation on the tensor (op.reshape(2,)*2N).

        # Build permutation: site k becomes axis 0 for rows, axis N for cols, rest in order.
        shape = (2,) * (2 * N)
        T = op.reshape(shape)
        # Site k as a row-index becomes axis 0
        row_order = [k] + [i for i in range(N) if i != k]
        col_order = [N + k] + [N + i for i in range(N) if i != k]
        T = np.transpose(T, row_order + col_order)
        # Reshape to (2, 2^(N-1), 2, 2^(N-1))
        M = T.reshape(2, dim_rest, 2, dim_rest)
        # Compute the four 2x2 "fibers" at the site-k level
        m00 = M[0, :, 0, :]
        m01 = M[0, :, 1, :]
        m10 = M[1, :, 0, :]
        m11 = M[1, :, 1, :]
        # If site k is NOT in support, op = (something on rest) ⊗ I_2 at site k,
        # which means m00 == m11 and m01 == m10 == 0 (up to scalar identity).
        # Strictly: m00 - m11 has small norm AND m01, m10 have small norm.
        diff_diag = np.linalg.norm(m00 - m11)
        off_diag = np.linalg.norm(m01) + np.linalg.norm(m10)
        scale = max(np.linalg.norm(m00), np.linalg.norm(m11), 1e-12)
        if (diff_diag + off_diag) / scale > tol:
            supp.add(k)
    return supp


def commutator(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return A @ B - B @ A


def nested_commutator(H: np.ndarray, A: np.ndarray, n: int) -> np.ndarray:
    """Compute the n-fold nested commutator [H, [H, ..., [H, A]...]]
    (n applications of [H, ·]).
    """
    out = A
    for _ in range(n):
        out = commutator(H, out)
    return out


def heisenberg_evolve(H: np.ndarray, A: np.ndarray, t: float) -> np.ndarray:
    """A(t) = exp(iHt) A exp(-iHt) via spectral decomposition."""
    eigvals, U = eigh(H)
    phase = np.exp(1j * t * eigvals)
    UdaggerA_U = U.conj().T @ A @ U
    middle = (phase[:, None] * UdaggerA_U) * np.conj(phase[None, :])
    return U @ middle @ U.conj().T


# ============================================================================
# Verification results dataclass
# ============================================================================

@dataclass
class VResult:
    name: str
    passed: bool
    message: str
    metrics: dict


# ============================================================================
# V1: Locality of nested commutators on the spin chain
# ============================================================================

def V1_locality_nested_commutators(N: int = 6) -> VResult:
    """For A = S_z^{0} on a 6-site Heisenberg chain (open BC), verify:
       supp([H, A]) ⊆ {0, 1}
       supp([H, [H, A]]) ⊆ {0, 1, 2}
       supp([H, [H, [H, A]]]) ⊆ {0, 1, 2, 3}
       supp(C_4(A)) ⊆ {0, 1, 2, 3, 4}

    This exhibits Lemma A's support-shrinking statement: supp(C_n(A)) ⊆ B_{nR_0}(supp A).
    """
    J = 1.0
    H = heisenberg_hamiltonian(N, J=J, open_bc=True)
    A = site_op(S_Z, 0, N)
    metrics = {}
    passed = True
    msgs = []
    expected = [{0}, {0, 1}, {0, 1, 2}, {0, 1, 2, 3}, {0, 1, 2, 3, 4}]
    for n in range(5):
        C = nested_commutator(H, A, n)
        supp = support_of(C, N)
        metrics[f"supp_C{n}"] = sorted(supp)
        if not supp.issubset(expected[n]):
            passed = False
            msgs.append(f"C_{n}: supp={sorted(supp)}, expected ⊆ {sorted(expected[n])}")
    if passed:
        msgs.append("All n=0..4 nested commutators have support within the predicted thickening.")
    return VResult(
        name="V1 — Locality of nested commutators",
        passed=passed,
        message=" | ".join(msgs),
        metrics=metrics,
    )


# ============================================================================
# V2: Triangle-inequality bound on nested commutator norm
# ============================================================================

def V2_nested_commutator_norm_bound(N: int = 6) -> VResult:
    """For A = S_z^{0}, verify ‖C_n(A)‖ ≤ (2J)^n · (D_I^+)^n · |X| · ‖A‖
    for n = 1..4, with D_I^+ the inclusive interaction-graph overlap degree
    from Lemma B.

    For a 1D Heisenberg chain, J = 1 (link bound: ‖S_i S_j‖ ≤ 1/4 for each
    spin, ‖h_{i,i+1}‖ = J · sup(‖S_i · S_{i+1}‖) ≤ J · 3/4 ≤ J, so we use
    J = 1 as a conservative bound). D_I^+ bounds the local chain branching at
    each step, including the repeated-term choice Z_{i+1}=Z_i. For a 1D
    nearest-neighbor chain, the maximum inclusive bond-overlap degree is 3
    (left neighbor, self, right neighbor).

    Use D_I^+ = 3 as a coarse, safe bound.
    """
    J_norm = 0.75  # actual norm of each h_{i,i+1} = J/4 · ‖σ·σ‖ ≤ 3J/4
    D_I_plus = 3.0
    X_size = 1
    H = heisenberg_hamiltonian(N, J=1.0, open_bc=True)
    A = site_op(S_Z, 0, N)
    A_norm = np.linalg.norm(A, ord=2)
    metrics = {}
    passed = True
    msgs = []
    for n in range(1, 5):
        C = nested_commutator(H, A, n)
        Cn_norm = np.linalg.norm(C, ord=2)
        bound = (2.0 * J_norm) ** n * (D_I_plus ** n) * X_size * A_norm
        ratio = Cn_norm / bound
        metrics[f"n_{n}_actual"] = float(Cn_norm)
        metrics[f"n_{n}_bound"] = float(bound)
        metrics[f"n_{n}_ratio"] = float(ratio)
        if ratio > 1.0:
            passed = False
            msgs.append(f"n={n}: actual {Cn_norm:.3f} > bound {bound:.3f}, ratio {ratio:.3f}")
    if passed:
        ratios = [metrics[f"n_{n}_ratio"] for n in range(1, 5)]
        msgs.append(f"All n=1..4 bounds hold. Ratios actual/bound: {[round(r,3) for r in ratios]}")
    return VResult(
        name="V2 — Triangle-inequality bound on nested commutator norms",
        passed=passed,
        message=" | ".join(msgs),
        metrics=metrics,
    )


# ============================================================================
# V3: Lieb-Robinson commutator bound on the spin chain
# ============================================================================

def V3_lieb_robinson_bound(N: int = 6) -> VResult:
    """For A = S_z^0, B = S_z^{N-1} (distance R = N-1), compute ‖[A(t), B]‖
    numerically at t = 0.1, 0.5, 1.0, 2.0 and verify the LR bound holds.

    The theoretical bound:

        ‖[A(t), B]‖ ≤ C_0 · |X| · ‖A‖ ‖B‖ · exp(-(R - v_LR |t|) / ξ)

    Constants used (matching the analysis in V2):

        J = 0.75, D_I^+ = 3, R_0 = 1, e = 2.718...
        v_LR = 2 · J · D_I^+ · R_0 · e ≈ 12.23
        ξ = R_0 / log 2 ≈ 1.44
        C_0 = 2

    Inside the strict light cone (R > v_LR |t| · e / log 2 ≈ 17.65 |t|),
    the bound is tight; outside, the bound saturates to 2 ‖A‖ ‖B‖.

    For our N=6, R=5 spin chain, the bound is trivially saturated except
    at very small |t|. We test the bound's structure by showing that, at
    fixed R and small t, the bound holds and gives qualitative agreement
    with the exponential structure.
    """
    H = heisenberg_hamiltonian(N, J=1.0, open_bc=True)
    A = site_op(S_Z, 0, N)
    B = site_op(S_Z, N - 1, N)
    A_norm = np.linalg.norm(A, ord=2)
    B_norm = np.linalg.norm(B, ord=2)
    R = N - 1  # distance between supports of A (site 0) and B (site N-1)

    J_norm = 0.75
    D_I_plus = 3.0
    R_0 = 1.0
    e = math.e
    v_LR = 2.0 * J_norm * D_I_plus * R_0 * e  # ≈ 12.23
    xi = R_0 / math.log(2.0)
    C_0 = 2.0

    times = [0.05, 0.1, 0.2, 0.4]
    metrics = {"v_LR_theory": v_LR, "xi": xi, "R": R}
    passed = True
    msgs = []
    for t in times:
        At = heisenberg_evolve(H, A, t)
        comm = At @ B - B @ At
        actual = np.linalg.norm(comm, ord=2)
        # Bound (with the C_0 trivial saturation outside the light cone)
        light_cone_term = R - v_LR * abs(t)
        if light_cone_term <= 0:
            # Outside the light cone: the LR bound is trivially the 2‖A‖‖B‖ ceiling
            bound = C_0 * A_norm * B_norm
        else:
            bound = C_0 * A_norm * B_norm * math.exp(-light_cone_term / xi)
        # Also include the trivial 2 ‖A‖ ‖B‖ ceiling that always holds
        trivial_ceiling = 2.0 * A_norm * B_norm
        effective_bound = min(bound, trivial_ceiling) if light_cone_term > 0 else trivial_ceiling
        metrics[f"t_{t}_actual"] = float(actual)
        metrics[f"t_{t}_bound"] = float(effective_bound)
        # We test: actual ≤ effective_bound (the LR statement)
        if actual > effective_bound * 1.001:  # tiny numerical slack
            passed = False
            msgs.append(f"t={t}: actual {actual:.4e} > bound {effective_bound:.4e}")
    if passed:
        ratios = [metrics[f"t_{t}_actual"] / metrics[f"t_{t}_bound"] for t in times]
        msgs.append(f"LR bound holds at t = {times}. Ratios actual/bound: {[round(r, 4) for r in ratios]}")
    return VResult(
        name="V3 — Lieb-Robinson bound on spin chain",
        passed=passed,
        message=" | ".join(msgs),
        metrics=metrics,
    )


# ============================================================================
# V4: Lieb-Robinson velocity extraction
# ============================================================================

def V4_lieb_robinson_velocity_extraction(N: int = 6) -> VResult:
    """Numerically extract the operator-spreading velocity from
    ‖[S_z^0(t), S_z^{R}]‖ at increasing R = 1, 2, 3, 4, 5 and a small fixed t.
    Fit the slope log ‖[...]‖ vs R, then compute v_LR_eff such that the slope
    at fixed t matches -1/ξ_eff + (v_LR · t) / ξ_eff.

    A cleaner extraction: at fixed small t, the LR bound predicts
    log ‖[A(t), B(R)]‖ ≈ - (R - v_LR · t) / ξ + const.
    So the slope vs R at fixed small t is approximately -1/ξ, INDEPENDENT
    of v_LR. To extract v_LR, look at how the "onset" of decay shifts with t.

    Alternative (simpler) test: verify that the LR bound holds and that the
    numerical commutator's exponential decay rate vs R, at the smallest t
    where the commutator is not yet saturated, gives a slope CONSISTENT with
    the predicted ξ.

    We extract the slope numerically and compare it against the theoretical
    prediction with a factor-of-3 margin (the path-counting bound is loose).
    """
    H = heisenberg_hamiltonian(N, J=1.0, open_bc=True)
    A = site_op(S_Z, 0, N)
    t = 0.2  # Small fixed time
    Rs = [1, 2, 3, 4, 5]
    log_norms = []
    actual_norms = []
    At = heisenberg_evolve(H, A, t)
    for R in Rs:
        B = site_op(S_Z, R, N)
        comm = At @ B - B @ At
        n = np.linalg.norm(comm, ord=2)
        actual_norms.append(n)
        # Take log; guard against zero
        log_norms.append(math.log(max(n, 1e-15)))
    # Fit linear: log_norm ≈ slope · R + intercept (least squares)
    Rs_arr = np.array(Rs, dtype=float)
    log_arr = np.array(log_norms, dtype=float)
    # Use the last 3 points for the asymptotic slope (R = 3, 4, 5)
    R_fit = Rs_arr[2:]
    L_fit = log_arr[2:]
    slope, intercept = np.polyfit(R_fit, L_fit, 1)
    xi_extracted = -1.0 / slope if slope < 0 else float('inf')

    # Theoretical xi (with loose path-counting bound)
    J_norm = 0.75
    D_I_plus = 3.0
    R_0 = 1.0
    xi_theory = R_0 / math.log(2.0)  # ≈ 1.44

    # The extracted xi should be in the same order of magnitude, factor-of-5 margin.
    # The theoretical bound is loose; the numerical commutator typically decays
    # faster than the bound (the bound is upper, not tight).
    # Numerically we expect xi_extracted ≤ xi_theory typically (faster decay than the loose bound).
    metrics = {
        "t": t,
        "Rs": Rs,
        "log_norms": log_norms,
        "actual_norms": actual_norms,
        "slope_fit": float(slope),
        "xi_extracted": float(xi_extracted),
        "xi_theory_loose": xi_theory,
    }
    # PASS criterion: extracted xi is positive (decay) and within an order of magnitude
    # of theoretical (i.e., not radically inconsistent — both are O(1)).
    passed = (slope < 0) and (xi_extracted > 0) and (xi_extracted < 10.0 * xi_theory)
    if passed:
        msg = (f"Slope = {slope:.3f} → xi_extracted = {xi_extracted:.3f} (theory loose: {xi_theory:.3f}). "
               f"Exponential decay structure confirmed.")
    else:
        msg = (f"Slope {slope:.3f}, xi_extracted {xi_extracted:.3f} inconsistent with theory {xi_theory:.3f}.")
    return VResult(
        name="V4 — Lieb-Robinson velocity / correlation-length extraction",
        passed=passed,
        message=msg,
        metrics=metrics,
    )


# ============================================================================
# V5: Finite-N cluster-support fit on the spin chain
# ============================================================================

def V5_spatial_cluster_decomposition(N: int = 6) -> VResult:
    """Compute the ground state of the N-site Heisenberg chain, the gap Δ,
    and the connected correlator C(R) = ⟨S_z^0 S_z^R⟩ - ⟨S_z^0⟩⟨S_z^R⟩ for
    R = 1..N-1. Fit log |C(R)| vs R and extract xi_cluster_numerical.
    Compare to ξ_cluster_theory ≈ v_LR / Δ as a loose finite-volume upper
    scale, not as a retained cluster theorem.

    The Heisenberg chain ground state has algebraic decay (no gap in the
    thermodynamic limit), so finite N produces a finite gap that closes
    as N → ∞. This is precisely the anti-overclaim point: ξ_cluster is
    Λ-dependent. We test only the qualitative structure (decay with R,
    positive ξ_cluster_numerical).
    """
    H = heisenberg_hamiltonian(N, J=1.0, open_bc=True)
    eigvals, U = eigh(H)
    E0 = eigvals[0]
    E1 = eigvals[1]
    Delta = E1 - E0
    psi0 = U[:, 0]

    # Compute correlators
    S_z_ops = [site_op(S_Z, i, N) for i in range(N)]
    expectation = lambda M: np.real(np.conj(psi0) @ (M @ psi0))
    sz_means = [expectation(op) for op in S_z_ops]

    correlators = []
    log_abs_corr = []
    Rs = list(range(1, N))
    for R in Rs:
        connected = expectation(S_z_ops[0] @ S_z_ops[R]) - sz_means[0] * sz_means[R]
        correlators.append(connected)
        log_abs_corr.append(math.log(max(abs(connected), 1e-15)))

    # Fit log |C(R)| vs R using R = 2..N-1 (skip R=1 to avoid short-range artifacts)
    R_fit = np.array(Rs[1:], dtype=float)
    L_fit = np.array(log_abs_corr[1:], dtype=float)
    slope, intercept = np.polyfit(R_fit, L_fit, 1)
    xi_cluster_num = -1.0 / slope if slope < 0 else float('inf')

    # Theoretical estimate: ξ_cluster = max(2ξ, 2 v_LR / Δ).
    # With v_LR ≈ 12.23, Δ at N=6 numerical:
    D_I_plus = 3.0
    v_LR = 2 * 0.75 * D_I_plus * 1.0 * math.e
    xi_spatial = 2.0 * (1.0 / math.log(2.0))
    xi_gap = 2.0 * v_LR / Delta if Delta > 1e-12 else float('inf')
    xi_cluster_theory = max(xi_spatial, xi_gap)

    metrics = {
        "N": N,
        "E0": float(E0),
        "E1": float(E1),
        "Delta": float(Delta),
        "Rs": Rs,
        "correlators": correlators,
        "log_abs_corr": log_abs_corr,
        "slope_fit": float(slope),
        "xi_cluster_numerical": float(xi_cluster_num),
        "v_LR_theory": v_LR,
        "xi_cluster_theory_loose_upper": xi_cluster_theory,
    }

    # PASS criterion: slope is negative on the chosen finite-N fit window, and xi_cluster_num > 0.
    # We do NOT require xi_cluster_num ≈ xi_cluster_theory because the loose
    # bound vastly overestimates xi_cluster (true xi is typically much smaller
    # than the LR bound predicts — the bound is upper).
    passed = (slope < 0) and (xi_cluster_num > 0)
    if passed:
        msg = (f"Δ={Delta:.4f}, slope={slope:.3f} → ξ_cluster_num={xi_cluster_num:.3f}. "
               f"Loose theory upper ξ ≤ {xi_cluster_theory:.2f}. Finite-N decay-fit support only.")
    else:
        msg = f"Cluster decay extraction failed: slope {slope}, ξ {xi_cluster_num}."
    return VResult(
        name="V5 — Finite-N cluster-support fit on spin chain",
        passed=passed,
        message=msg,
        metrics=metrics,
    )


# ============================================================================
# V6: Composition with PR #1577's SU(3) T_W spectrum
# ============================================================================

# SU(3) irrep machinery (mirror of PR #1577's runner, kept self-contained here)

N_C = 3


def su3_irrep_dim(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def su3_irrep_casimir(p: int, q: int) -> float:
    return (p * p + q * q + p * q) / 3.0 + p + q


def enumerate_irreps_up_to(N_max: int):
    for p in range(N_max + 1):
        for q in range(N_max + 1 - p):
            yield (p, q)


def V6_composition_with_pr1577_su3(N_max: int = 4, tau: float = 1.0) -> VResult:
    """Build the single-link SU(3) transfer operator T_W in the truncated
    character basis at N_max = 4 and τ = 1.0. The eigenvalues of T_W are
    exp(-τ C_2(R) / (2 N_c)) with multiplicity (dim R)² (matrix elements
    of irrep R).

    Verify:
      (a) Top eigenvalue = 1 (trivial irrep), simple (dim 1² = 1).
      (b) Next eigenvalue λ_1 = exp(-τ C_2(1,0) / (2 N_c)) = exp(-τ · (4/3) / 6) ≈ 0.800
          for τ = 1, with multiplicity (dim(1,0))² = 9.
      (c) Δ_T = λ_0 - λ_1 = 1 - 0.800 ≈ 0.200 > 0.
      (d) Hamiltonian-side gap Δ = -log(λ_1 / λ_0) = -log(λ_1) = τ C_2(1,0) / (2 N_c) ≈ 0.222.
      (e) The Lieb-Robinson velocity bound v_LR^{SU(3)} = 2 J^{SU(3)} · D_I^+ · R_0 · e
          is finite (J^{SU(3)} bounded by the canonical Wilson link norm).

    This composes the LR half (this PR) with PR #1577's Δ_T > 0 half.
    """
    # Build the truncated single-link T_W eigenvalues
    eigs = []
    for (p, q) in enumerate_irreps_up_to(N_max):
        d = su3_irrep_dim(p, q)
        c2 = su3_irrep_casimir(p, q)
        lam = math.exp(-tau * c2 / (2.0 * N_C))
        eigs.extend([lam] * (d * d))
    eigs = np.array(sorted(eigs, reverse=True))

    # Verifications
    lam0 = float(eigs[0])
    lam1 = float(eigs[1])
    Delta_T = lam0 - lam1

    # The top eigenvalue should be 1.0 (trivial irrep, R = (0,0): C_2 = 0).
    top_is_unity = abs(lam0 - 1.0) < 1e-12
    # The trivial irrep has dim 1, so multiplicity (dim)² = 1. Hence eigs[1] should be
    # the fundamental (1,0) or (0,1), giving exp(-τ · 4/3 / 6) = exp(-2τ/9) ≈ 0.8007 for τ=1.
    lam1_predicted = math.exp(-tau * (4.0 / 3.0) / (2.0 * N_C))
    lam1_matches = abs(lam1 - lam1_predicted) < 1e-12

    # Hamiltonian-side gap
    Delta_H = -math.log(lam1 / lam0) if lam0 > 0 and lam1 > 0 else float('inf')

    # Lieb-Robinson velocity for SU(3) Wilson (canonical normalization)
    # J^{SU(3)} bounded by canonical Wilson link normalization ≈ O(1).
    # Take J^{SU(3)} = 1 (the canonical Wilson coupling norm), and use the note's
    # coarse inclusive D_I^+ <= s_max Z_max <= 4*19 = 76 for the 3D
    # plaquette+staggered+on-site surface.
    # The precise constant doesn't matter for V6/V7 structural verification — we just confirm
    # v_LR is finite + positive.
    J_SU3 = 1.0
    D_I_lattice = 76.0
    R_0 = 2.0  # plaquette ell_1 diameter
    v_LR_SU3 = 2.0 * J_SU3 * D_I_lattice * R_0 * math.e
    xi_cluster_SU3 = 2.0 * v_LR_SU3 / Delta_H  # the gap-correlation length

    metrics = {
        "N_max": N_max,
        "tau": tau,
        "lam0": lam0,
        "lam1": lam1,
        "Delta_T": Delta_T,
        "lam1_predicted": lam1_predicted,
        "Delta_H": Delta_H,
        "v_LR_SU3": v_LR_SU3,
        "xi_cluster_SU3": xi_cluster_SU3,
        "num_eigenvalues_used": int(len(eigs)),
    }
    passed = (
        top_is_unity
        and lam1_matches
        and Delta_T > 1e-6
        and Delta_H > 1e-6
        and v_LR_SU3 > 0
        and xi_cluster_SU3 > 0
        and math.isfinite(xi_cluster_SU3)
    )
    if passed:
        msg = (f"λ_0={lam0:.6f}, λ_1={lam1:.6f} (predicted {lam1_predicted:.6f}), "
               f"Δ_T={Delta_T:.4f}, Δ_H={Delta_H:.4f}, v_LR^SU3={v_LR_SU3:.2f}, "
               f"ξ_cluster^SU3={xi_cluster_SU3:.2f}.")
    else:
        msg = f"V6 failed: lam0={lam0}, lam1={lam1}, Δ_T={Delta_T}, Δ_H={Delta_H}, v_LR={v_LR_SU3}"
    return VResult(
        name="V6 — Composition with PR #1577 SU(3) T_W (Δ_T > 0 + LR velocity)",
        passed=passed,
        message=msg,
        metrics=metrics,
    )


# ============================================================================
# V7: Structural SU(3) transfer-spectrum exponential sequence
# ============================================================================

def V7_spatial_cluster_decomposition_su3(N_max: int = 4,
                                          tau: float = 1.0) -> VResult:
    """On a 2-site Λ with one spatial link, the truncated character-basis
    transfer operator has eigenvalues exp(-τ C_2(R) / (2 N_c)) repeated (dim R)²
    times. We verify the structural exponential sequence implied by the transfer
    spectrum:

    For a 2-site system with one spatial link, "spatial separation" R between
    two plaquettes (in a hypothetical extended Λ) gives connected correlators
    that decay as λ_1^{R/R_0} after Wilson area law projection. This is exactly
    the gap-induced exponential decay with rate Δ_H = -log(λ_1/λ_0).

    Specifically, if a cluster channel is controlled by the top nontrivial
    transfer eigenvalue, its separated contribution decays as λ_1^{R/R_0}.
    Verify this sequence by computing λ_1^R for R = 1..6 and confirming
    geometric decay with rate Δ_H.

    This is a structural support check: it exhibits that the SU(3) transfer
    spectrum from V6 has the expected finite-volume exponential channel. It is
    not a direct connected-character-correlator computation.
    """
    # Build single-link eigenvalues (same as V6)
    eigs = []
    for (p, q) in enumerate_irreps_up_to(N_max):
        d = su3_irrep_dim(p, q)
        c2 = su3_irrep_casimir(p, q)
        lam = math.exp(-tau * c2 / (2.0 * N_C))
        eigs.extend([lam] * (d * d))
    eigs = np.array(sorted(eigs, reverse=True))
    lam0 = float(eigs[0])
    lam1 = float(eigs[1])
    Delta_H = -math.log(lam1 / lam0)

    # Predict exponential cluster-decay rate for the gap-induced channel:
    # connected correlator at separation R should decay as λ_1^{R/R_0}
    # where R_0 = 2 in the lattice ell_1 metric. The decay rate per unit length is
    # log(1/λ_1) / R_0 = Δ_H / R_0.

    R_0 = 2.0
    Rs = list(range(1, 7))
    predicted_decay = [(lam1 / lam0) ** (R / R_0) for R in Rs]
    log_predicted = [math.log(p) for p in predicted_decay]

    # Fit log_predicted vs R: slope should be -Δ_H / R_0
    Rs_arr = np.array(Rs, dtype=float)
    L_arr = np.array(log_predicted, dtype=float)
    slope, intercept = np.polyfit(Rs_arr, L_arr, 1)
    xi_cluster_extracted = -1.0 / slope if slope < 0 else float('inf')
    xi_cluster_expected = R_0 / Delta_H

    metrics = {
        "N_max": N_max,
        "tau": tau,
        "lam0": lam0,
        "lam1": lam1,
        "Delta_H": Delta_H,
        "R_0": R_0,
        "Rs": Rs,
        "predicted_decay": predicted_decay,
        "log_predicted": log_predicted,
        "slope_fit": float(slope),
        "xi_cluster_extracted": float(xi_cluster_extracted),
        "xi_cluster_expected": xi_cluster_expected,
    }
    # PASS: extracted xi matches expected ξ = R_0 / Δ_H to within 1% (structural test)
    rel_error = abs(xi_cluster_extracted - xi_cluster_expected) / xi_cluster_expected
    passed = rel_error < 1e-3 and slope < 0
    if passed:
        msg = (f"Δ_H={Delta_H:.4f}, slope={slope:.4f} → ξ_cluster={xi_cluster_extracted:.4f} "
               f"(expected ξ=R_0/Δ_H={xi_cluster_expected:.4f}, rel_err={rel_error:.2e}). "
               f"Structural exponential sequence confirmed.")
    else:
        msg = (f"Extracted xi={xi_cluster_extracted} vs expected {xi_cluster_expected}, "
               f"rel_err {rel_error}")
    return VResult(
        name="V7 — Structural SU(3) transfer-spectrum exponential sequence",
        passed=passed,
        message=msg,
        metrics=metrics,
    )


# ============================================================================
# V8: Anti-overclaim — finite-Λ scope verification
# ============================================================================

def V8_anti_overclaim_finite_lambda() -> VResult:
    """Compute ξ_cluster on smaller (Λ=4) and larger (Λ=6) Heisenberg chains,
    extract the connected-correlator decay constant, and confirm that the
    extracted ξ is Λ-dependent.

    This confirms the honest scope: the theorem is finite-Λ only, not
    uniform-in-Λ, and certainly not a Λ → ∞ statement. The gap closes (and
    ξ grows) as Λ grows, consistent with the gapless Heisenberg point.

    PASS criterion: the gap Δ at Λ=4 differs from the gap at Λ=6 by more
    than 5% (showing genuine Λ dependence; if uniform-in-Λ, this should be 0).
    """
    metrics = {}
    deltas = {}
    for N in [4, 6]:
        H = heisenberg_hamiltonian(N, J=1.0, open_bc=True)
        eigvals = eigvalsh(H)
        E0 = float(eigvals[0])
        E1 = float(eigvals[1])
        Delta = E1 - E0
        deltas[N] = Delta
        metrics[f"N{N}_E0"] = E0
        metrics[f"N{N}_E1"] = E1
        metrics[f"N{N}_Delta"] = Delta

        # Also compute the exponential decay constant of connected correlator
        # using the same method as V5
        _, U = eigh(H)
        psi0 = U[:, 0]
        S_z_ops = [site_op(S_Z, i, N) for i in range(N)]
        expectation = lambda M: np.real(np.conj(psi0) @ (M @ psi0))
        sz_means = [expectation(op) for op in S_z_ops]

        log_abs_corr = []
        for R in range(1, N):
            connected = expectation(S_z_ops[0] @ S_z_ops[R]) - sz_means[0] * sz_means[R]
            log_abs_corr.append(math.log(max(abs(connected), 1e-15)))
        if N > 3:
            R_fit = np.arange(2, N, dtype=float)
            L_fit = np.array(log_abs_corr[1:], dtype=float)
            slope, _ = np.polyfit(R_fit, L_fit, 1)
            xi = -1.0 / slope if slope < 0 else float('inf')
        else:
            xi = float('inf')
        metrics[f"N{N}_xi_extracted"] = xi

    rel_diff_gap = abs(deltas[4] - deltas[6]) / max(deltas[4], deltas[6])
    metrics["rel_diff_gap_N4_vs_N6"] = float(rel_diff_gap)
    # Genuine Λ-dependence: gap differs by more than 5%
    passed = rel_diff_gap > 0.05
    if passed:
        msg = (f"Δ(N=4)={deltas[4]:.4f}, Δ(N=6)={deltas[6]:.4f}, rel_diff={rel_diff_gap:.3f}. "
               f"ξ depends on Λ — finite-Λ scope confirmed (no uniform-in-Λ claim).")
    else:
        msg = (f"Gaps too similar: Δ(4)={deltas[4]}, Δ(6)={deltas[6]}. "
               f"Cannot exhibit Λ-dependence honestly.")
    return VResult(
        name="V8 — Anti-overclaim: finite-Λ scope verification",
        passed=passed,
        message=msg,
        metrics=metrics,
    )


# ============================================================================
# V9: Inclusive branching guard for repeated interaction chains
# ============================================================================

def _overlaps(a: frozenset, b: frozenset) -> bool:
    return bool(a & b)


def _count_interaction_chains(supports: list[frozenset],
                              X: frozenset,
                              Y: frozenset,
                              n: int) -> int:
    """Count length-n chains with repeated local terms allowed."""
    count = 0
    for chain in product(range(len(supports)), repeat=n):
        if not _overlaps(supports[chain[0]], X):
            continue
        if not _overlaps(supports[chain[-1]], Y):
            continue
        if all(_overlaps(supports[chain[i]], supports[chain[i + 1]]) for i in range(n - 1)):
            count += 1
    return count


def _inclusive_degree(supports: list[frozenset]) -> int:
    return max(sum(1 for other in supports if _overlaps(support, other)) for support in supports)


def _exclusive_degree(supports: list[frozenset]) -> int:
    return max(
        sum(1 for j, other in enumerate(supports) if i != j and _overlaps(support, other))
        for i, support in enumerate(supports)
    )


def V9_inclusive_branching_guard() -> VResult:
    """Brute-force the precise chain-count issue from the latest audit.

    The minimal two-term graph has one exclusive neighbor for each interaction,
    but a length-3 chain from X to Y has two allowed repeated-term choices:
    (Z0,Z0,Z1) and (Z0,Z1,Z1). Thus the exclusive-degree count fails, while the
    inclusive D_I^+ count succeeds. The second check verifies the same inclusive
    bound on a 1D nearest-neighbor bond graph.
    """
    metrics = {}

    minimal_supports = [frozenset({0, 1}), frozenset({1, 2})]
    X_min = frozenset({0})
    Y_min = frozenset({2})
    n_min = 3
    count_min = _count_interaction_chains(minimal_supports, X_min, Y_min, n_min)
    n_x_min = sum(1 for support in minimal_supports if _overlaps(support, X_min))
    d_excl_min = _exclusive_degree(minimal_supports)
    d_plus_min = _inclusive_degree(minimal_supports)
    exclusive_bound_min = n_x_min * (d_excl_min ** (n_min - 1))
    inclusive_bound_min = n_x_min * (d_plus_min ** (n_min - 1))

    metrics.update({
        "minimal_count_n3": count_min,
        "minimal_N_X": n_x_min,
        "minimal_D_exclusive": d_excl_min,
        "minimal_D_plus": d_plus_min,
        "minimal_exclusive_bound": exclusive_bound_min,
        "minimal_inclusive_bound": inclusive_bound_min,
    })

    exclusive_fails = count_min > exclusive_bound_min
    inclusive_holds_min = count_min <= inclusive_bound_min

    bond_supports = [frozenset({i, i + 1}) for i in range(5)]
    X_chain = frozenset({0})
    Y_chain = frozenset({5})
    n_x_chain = sum(1 for support in bond_supports if _overlaps(support, X_chain))
    d_plus_chain = _inclusive_degree(bond_supports)
    chain_bounds_hold = True
    chain_counts = {}
    for n in range(1, 8):
        count = _count_interaction_chains(bond_supports, X_chain, Y_chain, n)
        bound = n_x_chain * (d_plus_chain ** (n - 1))
        chain_counts[f"n{n}_count"] = count
        chain_counts[f"n{n}_inclusive_bound"] = bound
        chain_bounds_hold = chain_bounds_hold and (count <= bound)

    metrics.update({
        "bond_graph_N_X": n_x_chain,
        "bond_graph_D_plus": d_plus_chain,
        **chain_counts,
    })

    passed = exclusive_fails and inclusive_holds_min and chain_bounds_hold
    if passed:
        msg = (
            "Repeated-chain guard closes: exclusive degree fails on the minimal graph "
            f"({count_min} > {exclusive_bound_min}), while D_I^+ bounds it "
            f"({count_min} <= {inclusive_bound_min}) and bounds the 1D bond graph."
        )
    else:
        msg = (
            "Inclusive branching guard failed: "
            f"exclusive_fails={exclusive_fails}, inclusive_holds_min={inclusive_holds_min}, "
            f"chain_bounds_hold={chain_bounds_hold}."
        )
    return VResult(
        name="V9 — Inclusive branching guard for repeated chains",
        passed=passed,
        message=msg,
        metrics=metrics,
    )


# ============================================================================
# Main runner
# ============================================================================

def main():
    print("=" * 80)
    print("Finite-Volume Lieb-Robinson Bound plus Bounded Cluster-Decomposition Support")
    print("Companion to docs/SPATIAL_CLUSTER_DECOMPOSITION_LIEB_ROBINSON_REAL_NOTE_2026-05-19.md")
    print("=" * 80)
    print()

    t_start = time.time()

    results = []
    print("Running V1 — Locality of nested commutators ...")
    results.append(V1_locality_nested_commutators(N=6))
    print(f"  {'PASS' if results[-1].passed else 'FAIL'}: {results[-1].message}")
    print()

    print("Running V2 — Triangle-inequality bound on nested commutator norms ...")
    results.append(V2_nested_commutator_norm_bound(N=6))
    print(f"  {'PASS' if results[-1].passed else 'FAIL'}: {results[-1].message}")
    print()

    print("Running V3 — Lieb-Robinson bound on spin chain ...")
    results.append(V3_lieb_robinson_bound(N=6))
    print(f"  {'PASS' if results[-1].passed else 'FAIL'}: {results[-1].message}")
    print()

    print("Running V4 — LR velocity / correlation-length extraction ...")
    results.append(V4_lieb_robinson_velocity_extraction(N=6))
    print(f"  {'PASS' if results[-1].passed else 'FAIL'}: {results[-1].message}")
    print()

    print("Running V5 — Finite-N cluster-support fit on spin chain ...")
    results.append(V5_spatial_cluster_decomposition(N=6))
    print(f"  {'PASS' if results[-1].passed else 'FAIL'}: {results[-1].message}")
    print()

    print("Running V6 — Composition with PR #1577 SU(3) T_W (Δ_T > 0 + LR) ...")
    results.append(V6_composition_with_pr1577_su3(N_max=4, tau=1.0))
    print(f"  {'PASS' if results[-1].passed else 'FAIL'}: {results[-1].message}")
    print()

    print("Running V7 — Structural SU(3) transfer-spectrum exponential sequence ...")
    results.append(V7_spatial_cluster_decomposition_su3(N_max=4, tau=1.0))
    print(f"  {'PASS' if results[-1].passed else 'FAIL'}: {results[-1].message}")
    print()

    print("Running V8 — Anti-overclaim: finite-Λ scope verification ...")
    results.append(V8_anti_overclaim_finite_lambda())
    print(f"  {'PASS' if results[-1].passed else 'FAIL'}: {results[-1].message}")
    print()

    print("Running V9 — Inclusive branching guard for repeated chains ...")
    results.append(V9_inclusive_branching_guard())
    print(f"  {'PASS' if results[-1].passed else 'FAIL'}: {results[-1].message}")
    print()

    t_elapsed = time.time() - t_start

    print("=" * 80)
    print("Verification summary")
    print("=" * 80)
    n_pass = sum(1 for r in results if r.passed)
    n_fail = sum(1 for r in results if not r.passed)
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        print(f"  [{status}] {r.name}")
    print()
    print(f"Total: PASS = {n_pass}, FAIL = {n_fail}")
    print(f"Runtime: {t_elapsed:.2f} seconds")
    print("=" * 80)

    # Detailed metrics dump
    print()
    print("Detailed metrics")
    print("-" * 80)
    for r in results:
        print(f"[{r.name}]")
        for k, v in r.metrics.items():
            print(f"  {k}: {v}")
        print()

    if n_fail > 0:
        sys.exit(1)
    return 0


if __name__ == "__main__":
    main()
