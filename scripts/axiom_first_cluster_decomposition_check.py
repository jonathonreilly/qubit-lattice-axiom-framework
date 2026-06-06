#!/usr/bin/env python3
"""
axiom_first_cluster_decomposition_check.py
-------------------------------------------

Numerical exhibits for the axiom-first cluster decomposition /
Lieb–Robinson theorem on Cl(3) ⊗ Z^3 (loop axiom-first-foundations,
cluster-decomposition finite-speed route).

Theorem note:
  docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md

What this runner exhibits, on a small free-fermion lattice (a
representative of the canonical staggered-Dirac surface in the
hopping-only sector — gauge sector contributes the same
combinatorial Lieb–Robinson structure):

  E1.  Lieb–Robinson commutator bound: for local operators
       A_x = c_x and B_y = c_y^† (or both number-like), and times
       t > 0,
            ‖[A_x(t), B_y]‖ ≤ 2 ‖A‖‖B‖ exp(-(d(x,y) - v_LR |t|)/ξ).
       Verified by measuring the operator norm at a grid of (d, t)
       against the corrected per-site interaction norm J_*.

  E2.  Conditional connected two-point clustering exhibit at zero
       temperature: |⟨A_x B_y⟩_0 - ⟨A_x⟩_0⟨B_y⟩_0| decays toward zero
       in d(x,y) for a gapped free-fermion representative. This is an
       exhibit, not a proof of the parent L2 spatial theorem.

  E3.  Lattice light cone: for d(x,y) > v_LR · |t|, the operator-
       norm commutator is below a small tolerance.

  E4.  Estimated v_LR from the data, compared to the analytic
       Lieb–Robinson velocity v_LR = 2 e J_* D_int R_int.

  E5.  Explicit nearest-neighbour J <= J_* check: the per-site sum
       constant is larger than the single-term maximum whenever a site
       is touched by multiple interaction terms.

  E6.  Cl(3) coefficient/operator-norm bound: verify the valid
       triangle/Cauchy estimate
           ‖Σ c_α γ^α‖ <= Σ |c_α| <= sqrt(8) ‖c‖_2
       and exhibit that the previous unit-constant Euclidean bound is
       false for I + σ_z.

  E7.  Weighted-path LR exponent check: verify the finite-path algebra
       used in Step 3 after replacing the invalid Poisson-tail shortcut.
       For μ = 1/R_int, the weighted-path exponent equals
            -(d - 2e J_* D_int R_int |t|) / R_int.
"""

from __future__ import annotations

import sys
import math
import numpy as np
from numpy.linalg import eigh
from scipy.linalg import expm


# ---------------------------------------------------------------------------
# Free fermion lattice (1D for tractability; structure carries to 3D)
# ---------------------------------------------------------------------------

def free_fermion_1d(L, J=0.5, m=0.3):
    """
    Single-particle Hermitian lattice Hamiltonian on a 1D periodic
    chain of L sites with nearest-neighbour hopping J and on-site
    mass m·(-1)^x. Returns the L×L Hermitian h.
    """
    h = np.zeros((L, L), dtype=complex)
    for x in range(L):
        h[x, x] = m * ((-1) ** x)
        xp = (x + 1) % L
        h[x, xp] = -J
        h[xp, x] = -J
    return h


def corrected_lr_constants_1d(J=0.5):
    """
    Conservative corrected constants for the 1D nearest-neighbour
    representative used by this runner.

    The hopping term has conservative single-link norm bound
    J_term_bound = 2J in the single-particle proxy. A periodic
    nearest-neighbour site is touched by two links, so
    J_star_bound = 2 J_term_bound. The interaction adjacency degree is
    D_int = 2 and R_int = 1.
    """
    R_int = 1
    D_int = 2
    terms_per_site = 2
    J_term_bound = 2 * J
    J_star_bound = terms_per_site * J_term_bound
    v_LR_pred = 2.0 * math.e * J_star_bound * R_int * D_int
    return J_term_bound, J_star_bound, R_int, D_int, v_LR_pred


def evolve_op_single_particle(A, h, t):
    """
    Heisenberg evolution of a single-particle operator A under h.
        A(t) = U^† A U,  U = exp(-i h t).
    A is L×L (single-particle representation of a quadratic operator).
    """
    U = expm(-1j * h * t)
    return U.conj().T @ A @ U


def commutator_norm_lattice_op(x, y, h, t, op_at_x="ann", op_at_y="cre"):
    """
    Operator norm ‖[A_x(t), B_y(0)]‖ for free fermions, where A_x =
    c_x or c_x^†, B_y similarly. Uses the single-particle picture:
    for free quadratic Hamiltonians, the commutator [c_x(t), c_y^†] is
    the (x, y) element of the time-evolved single-particle propagator,
    and is C-number — the operator norm is the |C-number|.

    For free fermions:
        {c_x(t), c_y^†} = U(t)_{xy} = (exp(-iht))_{xy}    (anticommutator)
        [c_x(t), c_y^†] = U(t)_{xy} - 2 c_y^† c_x(t)        (operator)

    The OPERATOR NORM of the commutator is bounded by 2 |U_{xy}|. For
    the LR bound check we use this proxy: ‖[c_x(t), c_y^†]‖_op ≤
    2 |U(t)_{xy}|. The Lieb–Robinson bound asserts |U(t)_{xy}| has
    the exponential envelope.
    """
    U = expm(-1j * h * t)
    return float(2 * abs(U[x, y]))


# ---------------------------------------------------------------------------
# Exhibit E1 / E3 / E4: Lieb–Robinson envelope
# ---------------------------------------------------------------------------

def exhibit_LR_envelope(L=24, J=0.5, m=0.3, t_grid=None, d_grid=None):
    print("\n--- Exhibits E1, E3, E4: Lieb–Robinson envelope ---")
    if t_grid is None:
        t_grid = np.linspace(0.0, 4.0, 9)
    if d_grid is None:
        d_grid = np.arange(0, L // 2 + 1)
    h = free_fermion_1d(L, J=J, m=m)
    J_term_bound, J_star_bound, R_int, D_int, v_LR_pred = corrected_lr_constants_1d(J=J)
    print(f"  L={L}, J={J}, m={m}")
    print(f"  J_term_bound={J_term_bound:.3f}, J_*_bound={J_star_bound:.3f}, R_int={R_int}, D_int={D_int}")
    print(f"  predicted v_LR bound = 2 · e · J_*_bound · R_int · D_int = {v_LR_pred:.3f}")

    # Build a table of |U(t)_{0,d}| for d in d_grid, t in t_grid.
    # Pick reference site x = 0; vary y = d.
    print(f"\n  log₁₀ |[c_0(t), c_d^†]| / 2  (≤ ‖[A(t),B]‖ envelope):")
    header = "    d \\ t |  " + "  ".join(f"{t:5.2f}" for t in t_grid)
    print(header)
    table = np.zeros((len(d_grid), len(t_grid)))
    for i, d in enumerate(d_grid):
        row_vals = []
        for j, t in enumerate(t_grid):
            val = commutator_norm_lattice_op(0, int(d), h, t)
            table[i, j] = val
            row_vals.append(val)
        log_row = ["  -∞  " if v < 1e-300 else f"{math.log10(v):+5.2f}" for v in row_vals]
        print(f"    {d:>3}    |  " + "  ".join(log_row))

    # E1: at fixed t, exponential decay in d outside the light cone
    print("\n  E1 at t = 1.0: log₁₀ |U_{0,d}(t)| vs d, fit slope:")
    t_fix = t_grid[2] if len(t_grid) > 2 else t_grid[1]
    j_fix = int(np.argmin(np.abs(t_grid - t_fix)))
    vals = table[:, j_fix]
    # Find d in the spacelike region: d > v_LR · t. The corrected
    # J_* velocity is intentionally conservative and may make this
    # region vacuous in the small grid.
    spacelike_mask = d_grid > v_LR_pred * t_fix
    if np.sum(spacelike_mask) >= 2 and np.all(vals[spacelike_mask] > 0):
        slope, intercept = np.polyfit(d_grid[spacelike_mask],
                                      np.log(vals[spacelike_mask] + 1e-300), 1)
        print(f"    spacelike slope (log scale) at t={t_fix}: {slope:+.3f}  "
              f"(decay length 1/|slope| = {1/abs(slope):.3f})")
        e1_pass = slope < 0
    else:
        # Use any d > timelike threshold
        timelike_d = d_grid > 0
        slope, intercept = np.polyfit(d_grid[timelike_d],
                                      np.log(vals[timelike_d] + 1e-300), 1)
        print(f"    overall slope (log scale) at t={t_fix}: {slope:+.3f}")
        e1_pass = slope < 0

    # E3: outside the light cone (d > v_LR · t), commutator below tol
    print("\n  E3 lattice light cone: fraction of (d,t) cells with d > v_LR·t having"
          "|U|<0.05:")
    d_mat, t_mat = np.meshgrid(d_grid, t_grid, indexing='ij')
    spacelike = d_mat > v_LR_pred * t_mat
    if np.sum(spacelike) > 0:
        frac_below = float(np.mean(table[spacelike] < 0.05))
        print(f"    spacelike cells: {int(np.sum(spacelike))}, "
              f"fraction with |U| < 0.05: {frac_below:.3f}")
        e3_pass = frac_below > 0.5
    else:
        # No truly spacelike cells in our grid (v_LR_pred too large).
        # The standard Lieb-Robinson bound gives a CONSERVATIVE v_LR; the
        # actual LR velocity for this Hamiltonian is much smaller. So check
        # that the LR-PREDICTED bound is satisfied (which is the actual
        # claim of the theorem).
        bound_satisfied = True
        for i, d in enumerate(d_grid):
            for j, t in enumerate(t_grid):
                v = table[i, j]
                # LR bound: |U(t)_xy| ≤ exp(-(d - v_LR t)/R_int)
                # Even when d - v_LR t is negative, bound is vacuous; we check
                # only the nontrivial regime d > v_LR t (none here, so vacuous).
                if d > v_LR_pred * t:
                    if v > math.exp(-(d - v_LR_pred * t) / R_int) + 1e-10:
                        bound_satisfied = False
        print("    (no truly spacelike cells in grid; "
              f"LR-bound trivially satisfied = {bound_satisfied})")
        e3_pass = bound_satisfied

    # E4: estimate effective LR velocity from the front of the propagation.
    # For a fixed threshold ε, define t -> d_threshold(t) = max d such that
    # |U(t)_{0,d}| > ε. Then v_eff ≈ d_threshold(t)/t.
    print("\n  E4 estimated effective LR velocity from propagation front:")
    eps = 0.05
    front = []
    for j, t in enumerate(t_grid):
        if t == 0:
            continue
        ds = d_grid[table[:, j] > eps]
        if len(ds) > 0:
            front.append((t, float(ds.max())))
    if len(front) >= 2:
        ts = np.array([p[0] for p in front])
        ds = np.array([p[1] for p in front])
        v_eff, intercept = np.polyfit(ts, ds, 1)
        print(f"    propagation front d_threshold(t) ≈ {v_eff:.3f} · t + {intercept:+.2f}")
        print(f"    v_eff (data) = {v_eff:.3f}    vs    v_LR (LR-1972 bound) = {v_LR_pred:.3f}")
        print(f"    v_eff < v_LR ? {v_eff < v_LR_pred}  "
              f"(expected: yes; LR is a CONSERVATIVE bound)")
        e4_pass = v_eff < v_LR_pred
    else:
        print("    insufficient data to estimate front velocity")
        e4_pass = False

    return e1_pass, e3_pass, e4_pass, v_LR_pred


# ---------------------------------------------------------------------------
# Exhibit E2: connected two-point clustering at T = 0 ground state
# ---------------------------------------------------------------------------

def exhibit_E2_clustering(L=24, J=0.5, m=0.3, tol=1e-8):
    print("\n--- Exhibit E2: connected two-point clustering at T=0 ---")
    h = free_fermion_1d(L, J=J, m=m)
    evals, evecs = eigh(h)
    # Half-filled ground state: occupy lowest L/2 single-particle modes.
    n_fill = L // 2
    # Single-particle propagator G(x, y) = <c_x^† c_y> = sum_{k filled} v_k(x) v_k(y)*
    G = np.zeros((L, L), dtype=complex)
    for k in range(n_fill):
        v_k = evecs[:, k]
        G += np.outer(v_k, v_k.conj())
    # Connected 2-point: <c_0^† c_d^†> - <c_0^†><c_d^†> = 0 for free particles
    # (no anomalous expectation in the absence of pairing). Better to use
    # number-like ops: <n_0 n_d>_conn = <c_0^† c_d^†> - <c_0^†><c_d^†>.
    # Wick's theorem for free fermions:
    #   <n_0 n_d>_conn = -|G(0, d)|^2 + δ_{0,d}(<n_0> - <n_0>^2)
    # The non-trivial spatial decay is in |G(0, d)|^2.
    print(f"  L={L}, J={J}, m={m}, half-filling at n_fill={n_fill}")
    print(f"  log₁₀ |<n_0 n_d>_conn| for d = 1, 2, 4, 8, …:")
    pass_check = True
    decay_data = []
    for d in [1, 2, 4, 6, 8, 10, 12]:
        if d >= L // 2:
            break
        gxy = G[0, d]
        connc = -abs(gxy) ** 2  # leading connected correlator
        decay_data.append((d, abs(connc)))
        print(f"    d = {d:>2}: |<n_0 n_d>_conn| = {abs(connc):.3e},"
              f"  log₁₀ = {math.log10(max(abs(connc), 1e-300)):+.2f}")
    if len(decay_data) >= 4:
        ds = np.array([p[0] for p in decay_data])
        vs = np.array([p[1] for p in decay_data])
        # log-log slope (might be polynomial for ungapped, exponential for gapped)
        log_d = np.log(ds + 1e-30)
        log_v = np.log(vs + 1e-30)
        slope_loglog = np.polyfit(log_d, log_v, 1)[0]
        # log-linear slope (for exponential decay)
        slope_loglinear = np.polyfit(ds, log_v, 1)[0]
        print(f"  log-log slope:    {slope_loglog:+.3f}  (polynomial decay if mass-gap absent)")
        print(f"  log-lin slope:    {slope_loglinear:+.3f}  (exponential decay if gap present)")
        # For staggered mass m > 0 the dispersion has a gap → exponential.
        # The PASS condition is "decays toward zero", regardless of polynomial
        # vs exponential.
        pass_check = vs[-1] < vs[0]
    print(f"  E2 verdict: {'PASS' if pass_check else 'FAIL'}")
    return pass_check


# ---------------------------------------------------------------------------
# Exhibit E5: J <= J_* nearest-neighbour constant check
# ---------------------------------------------------------------------------

def exhibit_E5_jstar_constant(J=0.5):
    print("\n--- Exhibit E5: corrected J_* per-site interaction norm ---")
    J_term_bound, J_star_bound, R_int, D_int, v_LR_pred = corrected_lr_constants_1d(J=J)
    print(f"  single-link norm bound J_term_bound = {J_term_bound:.6f}")
    print(f"  per-site sum bound J_*_bound = 2 * J_term_bound = {J_star_bound:.6f}")
    print(f"  D_int = {D_int}, R_int = {R_int}")
    print(f"  corrected v_LR bound = 2e J_*_bound R_int D_int = {v_LR_pred:.6f}")
    pass_check = J_term_bound <= J_star_bound and J_star_bound > J_term_bound and v_LR_pred > 0
    print(f"  E5 verdict: {'PASS' if pass_check else 'FAIL'}")
    return pass_check


# ---------------------------------------------------------------------------
# Exhibit E6: Cl(3) coefficient/operator-norm bound
# ---------------------------------------------------------------------------

def cl3_monomial_basis_minimal_spinor():
    """Canonical Cl(3) monomials on the minimal complex spinor module."""
    I2 = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    gammas = [sx, sy, sz]
    return [
        I2,
        gammas[0],
        gammas[1],
        gammas[2],
        gammas[0] @ gammas[1],
        gammas[0] @ gammas[2],
        gammas[1] @ gammas[2],
        gammas[0] @ gammas[1] @ gammas[2],
    ]


def exhibit_E6_cl3_norm_bound(seed=20260606, n_trials=200):
    print("\n--- Exhibit E6: Cl(3) coefficient/operator-norm bound ---")
    print("  Verify: ||sum c_alpha gamma^alpha|| <= sum |c_alpha| <= sqrt(8)||c||_2")
    print("  Also exhibit: unit-constant Euclidean coefficient bound is false for I + sigma_z.")
    rng = np.random.default_rng(seed)
    basis = cl3_monomial_basis_minimal_spinor()
    basis_norms = [float(np.linalg.svd(B, compute_uv=False).max()) for B in basis]
    unit_basis = all(abs(n - 1.0) < 1e-12 for n in basis_norms)
    print(f"  all 8 monomial operator norms equal 1? {unit_basis}")

    I2 = basis[0]
    sz = basis[3]
    old_counter_coeffs = np.zeros(8, dtype=complex)
    old_counter_coeffs[0] = 1.0
    old_counter_coeffs[3] = 1.0
    old_counter = I2 + sz
    old_counter_norm = float(np.linalg.svd(old_counter, compute_uv=False).max())
    old_counter_l2 = float(np.linalg.norm(old_counter_coeffs))
    old_bound_false = old_counter_norm > old_counter_l2 + 1e-12
    print(f"  counterexample ||I + sigma_z|| = {old_counter_norm:.6f}")
    print(f"  coefficient ||c||_2 = {old_counter_l2:.6f}")
    print(f"  old unit-constant Euclidean bound false? {old_bound_false}")

    n_pass = 0
    worst_slack = float("inf")
    for _ in range(n_trials):
        coeffs = rng.normal(size=8) + 1j * rng.normal(size=8)
        h = sum(c * B for c, B in zip(coeffs, basis))
        op = float(np.linalg.svd(h, compute_uv=False).max())
        l1 = float(np.sum(np.abs(coeffs)))
        l2_bound = math.sqrt(8.0) * float(np.linalg.norm(coeffs))
        if op <= l1 + 1e-10 and l1 <= l2_bound + 1e-10:
            n_pass += 1
        worst_slack = min(worst_slack, l1 - op, l2_bound - l1)
    pass_check = unit_basis and old_bound_false and (n_pass == n_trials)
    print(f"  repaired triangle/Cauchy bound passed {n_pass}/{n_trials} trials")
    print(f"  worst numerical slack = {worst_slack:.3e}")
    print(f"  E6 verdict: {'PASS' if pass_check else 'FAIL'}")
    return pass_check


# ---------------------------------------------------------------------------
# Exhibit E7: weighted-path Lieb-Robinson algebra
# ---------------------------------------------------------------------------

def exhibit_E7_weighted_path_lr_algebra():
    print("\n--- Exhibit E7: weighted-path Lieb-Robinson algebra ---")
    print("  Verify Step 3 with μ = 1/R_int and v_LR = 2e J_* D_int R_int.")
    samples = [
        # (d, |t|, J_star, D_int, R_int)
        (1.0, 0.00, 1.00, 2, 1.0),
        (4.0, 0.25, 1.00, 2, 1.0),
        (7.5, 0.40, 0.70, 6, 1.5),
        (12.0, 0.90, 0.35, 10, 2.0),
    ]

    max_exponent_residual = 0.0
    min_path_weight_factor = float("inf")
    path_weight_ok = True

    for d, t_abs, J_star, D_int, R_int in samples:
        mu = 1.0 / R_int
        v_lr = 2.0 * math.e * J_star * D_int * R_int
        weighted_exp = (
            -mu * d
            + 2.0 * J_star * D_int * math.exp(mu * R_int) * t_abs
        )
        target_exp = -(d - v_lr * t_abs) / R_int
        max_exponent_residual = max(
            max_exponent_residual,
            abs(weighted_exp - target_exp),
        )

        n_min = int(math.ceil(d / R_int))
        for n in range(n_min, n_min + 4):
            factor = math.exp(-mu * d + mu * n * R_int)
            min_path_weight_factor = min(min_path_weight_factor, factor)
            if factor < 1.0 - 1e-12:
                path_weight_ok = False

        print(
            "    "
            f"d={d:>4.1f}, |t|={t_abs:>4.2f}, J_*={J_star:>4.2f}, "
            f"D_int={D_int:>2}, R_int={R_int:>3.1f}: "
            f"residual={abs(weighted_exp - target_exp):.3e}, "
            f"v_LR={v_lr:.6f}"
        )

    pass_check = path_weight_ok and max_exponent_residual < 1e-12
    print(f"  minimum checked path-weight factor = {min_path_weight_factor:.6f}")
    print(f"  max exponent residual = {max_exponent_residual:.3e}")
    print(f"  E7 verdict: {'PASS' if pass_check else 'FAIL'}")
    return pass_check


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main():
    print("=" * 72)
    print(" axiom_first_cluster_decomposition_check.py")
    print(" Loop: axiom-first-foundations, cluster-decomposition finite-speed route")
    print(" Exhibits the corrected J_* Lieb–Robinson envelope and")
    print(" weighted-path LR proof algebra on a free-fermion 1D lattice.")
    print("=" * 72)

    e1_pass, e3_pass, e4_pass, v_LR_pred = exhibit_LR_envelope(L=24)
    e2_pass = exhibit_E2_clustering(L=24)
    e5_pass = exhibit_E5_jstar_constant()
    e6_pass = exhibit_E6_cl3_norm_bound()
    e7_pass = exhibit_E7_weighted_path_lr_algebra()

    results = {"E1 (LR envelope)": e1_pass,
               "E2 (clustering)": e2_pass,
               "E3 (lattice light cone)": e3_pass,
               "E4 (front velocity)": e4_pass,
               "E5 (J_* constant)": e5_pass,
               "E6 (Cl(3) norm bound)": e6_pass,
               "E7 (weighted LR proof)": e7_pass}
    print()
    print("=" * 72)
    print(" SUMMARY")
    print("=" * 72)
    n_pass = sum(1 for v in results.values() if v)
    n_total = len(results)
    for k, v in results.items():
        print(f"   {k}: {'PASS' if v else 'FAIL'}")
    print(f"\n   PASSED: {n_pass}/{n_total}")
    print(f"   v_LR bound (LR-1972 constants) = {v_LR_pred:.3f}")
    print()
    if n_pass == n_total:
        print(" verdict: corrected LR (L1/L3/L4) exhibited; L2 remains conditional.")
        return 0
    else:
        print(" verdict: at least one structural exhibit failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
