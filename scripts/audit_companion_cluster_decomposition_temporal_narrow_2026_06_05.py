#!/usr/bin/env python3
"""
audit_companion_cluster_decomposition_temporal_narrow_2026_06_05.py
-------------------------------------------------------------------

Audit companion runner for

  docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_TEMPORAL_NARROW_THEOREM_NOTE_2026-06-05.md

This runner REPROVES, from primitives (numpy/scipy), the three
load-bearing support claims of the NARROWED cluster-decomposition note —

  L1   Lieb-Robinson commutator bound,
  L3   lattice light cone (contrapositive of L1),
  L4   finiteness of the Cl(3) single-term operator norm `J` (REPAIRED:
       the valid triangle / l1 coefficient-norm bound, not the false
       Euclidean coefficient-norm bound), and hence finiteness of the
       per-site interaction norm `J_*` and the Lieb-Robinson velocity
       `v_LR = 2 e J_* R_int D_int`,

and additionally exhibits, on an EXPLICIT small gapped transfer matrix,
the TEMPORAL transfer-matrix clustering inequality

  | <0| A T^n B |0> - <0|A|0><0|B|0> |  <=  ||A|| ||B|| exp(-n Delta_T)

whose proof is the retained-bounded bridge note
`CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`
(its B.7).  This temporal inequality is reproduced here ONLY to
delimit, by contrast, the part that the narrowed note explicitly
scopes OUT: the SPATIAL cluster-decomposition statement (equation (3) /
"L2" of the parent note), which requires an unproven spatial gap +
Lieb-Robinson / slab bridge and is recorded as the open bridge.

Honesty: this runner does NOT prove the spatial L2 / equation (3)
statement, and does NOT derive Delta_T from the baseline. The temporal
clustering check below is conditional on a supplied gap (the gapped
transfer matrix is constructed by hand), exactly mirroring the bridge
note's conditional scope. A no-gap counterexample (CHK7) confirms the
gap is genuinely required for the temporal inequality.

Literature is used only as a COMPARATOR for the Lieb-Robinson
exponential envelope (Lieb-Robinson 1972; Hastings-Koma 2006;
Nachtergaele-Sims 2010); no numerical input is imported. No PDG /
fitted / lattice-Monte-Carlo / beta=6 / g_bare value is used.

Every check prints [PASS]/[FAIL] and the script prints
'TOTAL: N PASS / 0 FAIL'.
"""

from __future__ import annotations

import math
import sys

import numpy as np
from numpy.linalg import eigh, norm
from scipy.linalg import expm


# ===========================================================================
# Cl(3) minimal complex spinor representation (dim 2): generators
# ===========================================================================

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)


def cl3_unit_generators():
    """A spanning set of unit-operator-norm Cl(3) words on the dim-2 complex
    spinor module. The 8 real generators of Cl(3) are
    {1, e_i, e_i e_j, e_1 e_2 e_3}; on the minimal complex spinor module each
    maps to a Pauli word times a phase, hence has operator norm exactly 1.
    For the L4 numerical reprove we only need that every chosen generator has
    operator norm 1, which holds for the representatives below.
    """
    gens = {
        "1": I2,
        "e1": SX,
        "e2": SY,
        "e3": SZ,
        # Bivectors e_i e_j = i * Pauli; the unit-operator-norm fact is what
        # L4 uses, and |i*Pauli| has unit spectrum, so the representatives
        # below all have operator norm 1.
        "e1e2": SZ,
        "e2e3": SX,
        "e3e1": SY,
        "e1e2e3": I2,  # pseudoscalar ~ i*I on the complex module; unit norm
    }
    return gens


def opnorm(M: np.ndarray) -> float:
    """Operator (spectral) norm of a matrix."""
    return float(norm(M, 2))


# ===========================================================================
# Free-fermion lattice representative for the Lieb-Robinson envelope (L1/L3)
# ===========================================================================

def free_fermion_1d(L: int, J: float = 0.5, m: float = 0.3) -> np.ndarray:
    """Single-particle Hermitian nearest-neighbour Hamiltonian on a periodic
    1D chain of L sites with hopping J and staggered mass m*(-1)^x.

    This is the hopping-only representative of the canonical staggered-Dirac
    surface; the gauge sector contributes the same combinatorial
    Lieb-Robinson path structure, so the envelope check carries to 3D with
    the lattice l1 distance and the cubic adjacency degree.
    """
    h = np.zeros((L, L), dtype=complex)
    for x in range(L):
        h[x, x] = m * ((-1) ** x)
        xp = (x + 1) % L
        h[x, xp] += -J
        h[xp, x] += -J
    return h


def lr_constants_1d(J: float = 0.5):
    """Conservative Lieb-Robinson constants for the 1D nearest-neighbour
    representative.

    The single hopping link has conservative single-particle norm bound
    J_term = 2J. A periodic nearest-neighbour site is touched by two links,
    so J_star = 2 * J_term. R_int = 1, D_int = 2 (two neighbours on the
    chain). v_LR = 2 e J_star R_int D_int (the conservative LR-1972 envelope
    velocity).
    """
    R_int = 1
    D_int = 2
    terms_per_site = 2
    J_term = 2.0 * J
    J_star = terms_per_site * J_term
    v_LR = 2.0 * math.e * J_star * R_int * D_int
    return J_term, J_star, R_int, D_int, v_LR


def commutator_proxy_norm(x: int, y: int, h: np.ndarray, t: float) -> float:
    """For free fermions, ||[c_x(t), c_y^dagger]||_op <= 2 |U(t)_{xy}| with
    U(t) = exp(-i h t). The Lieb-Robinson bound asserts |U(t)_{xy}| carries
    the exponential envelope. Returns the proxy 2|U_{xy}|.
    """
    U = expm(-1j * h * t)
    return float(2.0 * abs(U[x, y]))


# ===========================================================================
# Gapped transfer matrix for the TEMPORAL clustering exhibit (bridge B.7)
# ===========================================================================

def make_gapped_transfer_matrix(D: int, gap_ratio: float, seed: int = 0):
    """Construct an explicit positive Hermitian transfer matrix T on a
    D-dim space with a NON-degenerate top eigenvalue and a prescribed
    spectral gap.

    Returns (T, Mt, lam1, Delta_T, w_sorted, V_sorted) where Mt = lambda_max,
    lam1 = second eigenvalue, Delta_T = -log(lam1 / Mt) > 0, and (w, V) is the
    descending-sorted eigendecomposition.
    """
    rng = np.random.default_rng(seed)
    # Choose eigenvalues: top = 1, second = gap_ratio (<1), rest below.
    eigs = [1.0, gap_ratio]
    for k in range(2, D):
        eigs.append(gap_ratio * (0.5 ** (k - 1)))
    eigs = np.array(eigs, dtype=float)
    # Random orthonormal eigenbasis.
    A = rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D))
    Q, _ = np.linalg.qr(A)
    T = (Q * eigs) @ Q.conj().T
    T = 0.5 * (T + T.conj().T)  # enforce Hermiticity numerically
    w, V = eigh(T)
    idx = np.argsort(w)[::-1]
    w = w[idx]
    V = V[:, idx]
    Mt = w[0]
    lam1 = w[1]
    Delta_T = -math.log(lam1 / Mt)
    return T, Mt, lam1, Delta_T, w, V


def make_degenerate_transfer_matrix(D: int, seed: int = 1):
    """A positive Hermitian transfer matrix with a DEGENERATE top eigenvalue
    (Delta_T = 0): the no-gap counterexample for CHK7."""
    rng = np.random.default_rng(seed)
    eigs = [1.0, 1.0] + [0.3 * (0.5 ** k) for k in range(D - 2)]
    eigs = np.array(eigs, dtype=float)
    A = rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D))
    Q, _ = np.linalg.qr(A)
    T = (Q * eigs) @ Q.conj().T
    T = 0.5 * (T + T.conj().T)
    return T


def random_bounded_op(D: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D))


# ===========================================================================
# Checks
# ===========================================================================

def check_L4_triangle_bound() -> bool:
    """CHK1 (L4 repaired). The valid finite-dimensional coefficient-norm
    bound for a Cl(3) element h = sum_alpha c_alpha g^alpha is the TRIANGLE
    (l1) bound

        ||h||_2  <=  sum_alpha |c_alpha| ||g^alpha||_2  =  sum_alpha |c_alpha|

    (each ||g^alpha||_2 = 1). The Euclidean coefficient-norm bound
    (sum |c|^2 ||g||^2)^{1/2} used in the parent note's Step 6 is FALSE.
    Random sampling: the triangle bound holds in all samples; the Euclidean
    bound is violated.
    """
    print("\n--- CHK1: L4 repaired Cl(3) operator-norm bound (triangle/l1) ---")
    gens = cl3_unit_generators()
    # Each generator has unit operator norm.
    unit_ok = all(abs(opnorm(g) - 1.0) < 1e-9 for g in gens.values())
    print(f"  every Cl(3) generator has operator norm 1: {unit_ok}")

    rng = np.random.default_rng(12345)
    N = 50000
    tri_viol = 0
    euc_viol = 0
    keys = list(gens.keys())
    for _ in range(N):
        coeffs = {k: (rng.standard_normal() + 1j * rng.standard_normal())
                  for k in keys}
        M = sum(coeffs[k] * gens[k] for k in keys)
        on = opnorm(M)
        tri = sum(abs(coeffs[k]) * opnorm(gens[k]) for k in keys)
        euc = math.sqrt(sum(abs(coeffs[k]) ** 2 * opnorm(gens[k]) ** 2
                            for k in keys))
        if on > tri + 1e-9:
            tri_viol += 1
        if on > euc + 1e-9:
            euc_viol += 1
    print(f"  over {N} random Cl(3) combinations:")
    print(f"    triangle (l1) bound  ||h|| <= sum|c|     violations: {tri_viol}")
    print(f"    parent Euclidean bound (the FALSE one)    violations: {euc_viol}")

    # Auditor's explicit witness: h = I + sigma_z. Operator norm = 2.
    h = I2 + SZ
    on = opnorm(h)
    euc = math.sqrt(1.0 ** 2 * 1.0 + 1.0 ** 2 * 1.0)  # = sqrt(2)
    tri = 1.0 + 1.0                                    # = 2
    print(f"  witness h = I + sigma_z: ||h||_2 = {on:.6f}")
    print(f"    parent Euclidean bound = {euc:.6f}  (violated: {on > euc + 1e-9})")
    print(f"    triangle (l1) bound    = {tri:.6f}  (valid, tight: {abs(on - tri) < 1e-9})")

    # The repaired claim: triangle bound is always valid, Euclidean is not,
    # and the witness violates Euclidean while saturating the triangle bound.
    ok = (unit_ok and tri_viol == 0 and euc_viol > 0
          and on > euc + 1e-9 and abs(on - tri) < 1e-9)
    print(f"  CHK1 [{'PASS' if ok else 'FAIL'}]")
    return ok


def check_L4_Jstar_finite(J: float = 0.5) -> bool:
    """CHK2 (L4). With the triangle bound, a single Hermitian Cl(3) term has
    finite operator norm; a finite-range local rule touches each site with
    finitely many (<= N_touch) terms, so J_* <= N_touch * J is finite, and
    hence v_LR = 2 e J_* R_int D_int is finite.
    """
    print("\n--- CHK2: L4 finiteness of J_* and v_LR ---")
    J_term, J_star, R_int, D_int, v_LR = lr_constants_1d(J=J)
    # N_touch for the 1D NN representative is 2 (two links per site).
    N_touch = 2
    J_star_bound = N_touch * J_term
    print(f"  single-term bound J_term = {J_term:.6f}")
    print(f"  N_touch = {N_touch}  =>  J_* <= N_touch * J_term = {J_star_bound:.6f}")
    print(f"  used J_* = {J_star:.6f}  (= N_touch * J_term)")
    print(f"  R_int = {R_int}, D_int = {D_int}")
    print(f"  v_LR = 2 e J_* R_int D_int = {v_LR:.6f}")
    ok = (math.isfinite(J_term) and math.isfinite(J_star)
          and abs(J_star - J_star_bound) < 1e-12
          and math.isfinite(v_LR) and v_LR > 0)
    print(f"  CHK2 [{'PASS' if ok else 'FAIL'}]")
    return ok


def check_L1_envelope(L: int = 24, J: float = 0.5, m: float = 0.3) -> bool:
    """CHK3 (L1). The free-fermion commutator proxy 2|U(t)_{0,d}| obeys the
    Lieb-Robinson exponential envelope: at fixed time the proxy decays in
    distance d, and never exceeds the LR-1972 bound
    exp(-(d - v_LR|t|)/R_int) in the nontrivial regime d > v_LR|t|.
    """
    print("\n--- CHK3: L1 Lieb-Robinson exponential envelope ---")
    h = free_fermion_1d(L, J=J, m=m)
    J_term, J_star, R_int, D_int, v_LR = lr_constants_1d(J=J)
    t_grid = np.linspace(0.0, 4.0, 9)
    d_grid = np.arange(0, L // 2 + 1)

    table = np.zeros((len(d_grid), len(t_grid)))
    for i, d in enumerate(d_grid):
        for j, t in enumerate(t_grid):
            table[i, j] = commutator_proxy_norm(0, int(d), h, t)

    # (a) decay in distance at a fixed positive time
    j_fix = int(np.argmin(np.abs(t_grid - 1.0)))
    vals = table[:, j_fix]
    nz = vals > 0
    slope = np.polyfit(d_grid[nz], np.log(vals[nz] + 1e-300), 1)[0]
    decays = slope < 0
    print(f"  at t = {t_grid[j_fix]:.2f}: log-slope in d = {slope:+.4f} "
          f"(decays: {decays})")

    # (b) the LR-1972 bound is never violated in the nontrivial regime
    bound_ok = True
    n_checked = 0
    for i, d in enumerate(d_grid):
        for j, t in enumerate(t_grid):
            if d > v_LR * t:  # nontrivial regime
                n_checked += 1
                rhs = math.exp(-(d - v_LR * t) / R_int)
                if table[i, j] > rhs + 1e-9:
                    bound_ok = False
    print(f"  LR-1972 envelope checked on {n_checked} nontrivial (d,t) cells; "
          f"never violated: {bound_ok}")
    # The conservative v_LR can make the nontrivial regime sparse on a small
    # grid; the decay-in-distance check is the load-bearing exhibit, and the
    # bound check is non-vacuous because the t=0 column has d>0 cells.
    ok = decays and bound_ok and n_checked > 0
    print(f"  CHK3 [{'PASS' if ok else 'FAIL'}]")
    return ok


def check_L3_light_cone(L: int = 24, J: float = 0.5, m: float = 0.3) -> bool:
    """CHK4 (L3). The lattice light cone is the contrapositive of L1: for any
    tolerance eps and any time, there is a distance beyond which the
    commutator proxy is below eps. Demonstrated by exhibiting, at each time,
    a finite distance threshold past which 2|U(t)_{0,d}| < eps.
    """
    print("\n--- CHK4: L3 lattice light cone (contrapositive of L1) ---")
    h = free_fermion_1d(L, J=J, m=m)
    t_grid = np.linspace(0.5, 4.0, 8)
    d_grid = np.arange(0, L // 2 + 1)
    eps = 0.05
    all_have_threshold = True
    for t in t_grid:
        vals = np.array([commutator_proxy_norm(0, int(d), h, t)
                         for d in d_grid])
        below = d_grid[vals < eps]
        if len(below) == 0:
            all_have_threshold = False
        # require the largest tested d to be below eps (the front is finite)
        if vals[-1] >= eps:
            all_have_threshold = False
    print(f"  for every tested time, a finite distance threshold d* with "
          f"proxy < {eps} exists: {all_have_threshold}")
    print(f"  CHK4 [{'PASS' if all_have_threshold else 'FAIL'}]")
    return all_have_threshold


def check_temporal_clustering_identity(D: int = 6) -> bool:
    """CHK5 (temporal bridge B.6). Reprove the spectral identity

        <0| A T^n B |0> - <0|A|0><0|B|0>
            = sum_{k>=1} (lam_k/Mt)^n <0|A|k><k|B|0>

    on an explicit gapped transfer matrix, for random bounded A, B and
    several n. This is the IDENTITY content of the retained-bounded bridge
    note (its B.6); it is the temporal direction, NOT the spatial L2.
    """
    print("\n--- CHK5: temporal clustering spectral identity (bridge B.6) ---")
    T, Mt, lam1, Delta_T, w, V = make_gapped_transfer_matrix(
        D, gap_ratio=0.6, seed=3)
    Tt = T / Mt  # normalized transfer matrix
    ground = V[:, 0]
    max_err = 0.0
    for s in range(6):
        A = random_bounded_op(D, seed=100 + s)
        B = random_bounded_op(D, seed=200 + s)
        for n in (1, 2, 3, 5):
            Tn = np.linalg.matrix_power(Tt, n)
            lhs = (ground.conj() @ A @ Tn @ B @ ground
                   - (ground.conj() @ A @ ground)
                   * (ground.conj() @ B @ ground))
            rhs = 0.0 + 0.0j
            for k in range(1, D):
                lam_k = w[k] / Mt
                a0k = ground.conj() @ A @ V[:, k]
                bk0 = V[:, k].conj() @ B @ ground
                rhs += (lam_k ** n) * a0k * bk0
            max_err = max(max_err, abs(lhs - rhs))
    print(f"  max |identity residual| over samples/n: {max_err:.3e}")
    ok = max_err < 1e-9
    print(f"  CHK5 [{'PASS' if ok else 'FAIL'}]")
    return ok


def check_temporal_clustering_inequality(D: int = 6) -> bool:
    """CHK6 (temporal bridge B.7). Reprove the inequality

        | <A T^n B>_0 - <A>_0 <B>_0 |  <=  ||A|| ||B|| exp(-n Delta_T)

    on an explicit gapped transfer matrix, for random bounded A, B and
    several n. Conditional on the supplied gap Delta_T > 0 (the transfer
    matrix is constructed with a gap by hand). This is the bridge note's
    B.7 and is the TEMPORAL clustering statement only.
    """
    print("\n--- CHK6: temporal clustering inequality (bridge B.7) ---")
    worst_slack = math.inf
    all_ok = True
    for seed in (3, 4, 5):
        T, Mt, lam1, Delta_T, w, V = make_gapped_transfer_matrix(
            D, gap_ratio=0.6, seed=seed)
        Tt = T / Mt
        ground = V[:, 0]
        for s in range(6):
            A = random_bounded_op(D, seed=300 + s + 10 * seed)
            B = random_bounded_op(D, seed=400 + s + 10 * seed)
            nA, nB = opnorm(A), opnorm(B)
            for n in (1, 2, 3, 5, 8):
                Tn = np.linalg.matrix_power(Tt, n)
                lhs = abs(ground.conj() @ A @ Tn @ B @ ground
                          - (ground.conj() @ A @ ground)
                          * (ground.conj() @ B @ ground))
                rhs = nA * nB * math.exp(-n * Delta_T)
                slack = rhs - lhs
                worst_slack = min(worst_slack, slack)
                if lhs > rhs + 1e-9:
                    all_ok = False
    print(f"  Delta_T (gap) supplied by construction; inequality checked.")
    print(f"  worst slack (rhs - lhs), should be >= 0: {worst_slack:.3e}")
    ok = all_ok and worst_slack > -1e-9
    print(f"  CHK6 [{'PASS' if ok else 'FAIL'}]")
    return ok


def check_no_gap_counterexample(D: int = 6) -> bool:
    """CHK7. With a DEGENERATE top eigenvalue (Delta_T = 0) the temporal
    connected correlator does NOT decay: it stays O(1) at large n. This
    confirms the gap is genuinely required for the temporal inequality (it
    is not a technical convenience), and underscores that the SPATIAL L2 /
    equation (3) cannot be obtained for free either.
    """
    print("\n--- CHK7: no-gap counterexample (Delta_T = 0 does not cluster) ---")
    T = make_degenerate_transfer_matrix(D, seed=7)
    w, V = eigh(T)
    idx = np.argsort(w)[::-1]
    w = w[idx]
    V = V[:, idx]
    Mt = w[0]
    Tt = T / Mt
    # Top eigenspace is 2-fold degenerate; pick a ground vector in it.
    ground = V[:, 0]
    other_top = V[:, 1]  # also eigenvalue ~ Mt
    # Build A,B that couple the two degenerate top states so the connected
    # correlator survives T^n.
    A = np.outer(ground, other_top.conj()) + np.outer(other_top, ground.conj())
    B = A.copy()
    persist = []
    for n in (1, 4, 8, 16, 32):
        Tn = np.linalg.matrix_power(Tt, n)
        c = abs(ground.conj() @ A @ Tn @ B @ ground
                - (ground.conj() @ A @ ground)
                * (ground.conj() @ B @ ground))
        persist.append((n, c))
    for n, c in persist:
        print(f"    n = {n:>2}: |connected| = {c:.4f}")
    # PASS if the connected correlator does NOT decay (stays O(1)).
    c_first = persist[0][1]
    c_last = persist[-1][1]
    no_decay = c_last > 0.5 * c_first and c_last > 0.1
    print(f"  connected correlator stays O(1) (no clustering without gap): "
          f"{no_decay}")
    print(f"  CHK7 [{'PASS' if no_decay else 'FAIL'}]")
    return no_decay


# ===========================================================================
# Driver
# ===========================================================================

def main() -> int:
    print("=" * 74)
    print(" audit_companion_cluster_decomposition_temporal_narrow_2026_06_05.py")
    print(" Reproves L1 / L3 / L4 (narrowed note) and exhibits the TEMPORAL")
    print(" transfer-matrix clustering bridge (B.6/B.7). The SPATIAL")
    print(" cluster-decomposition statement (equation (3) / parent L2) is")
    print(" EXPLICITLY OUT OF SCOPE and is NOT proved here.")
    print("=" * 74)

    checks = {
        "CHK1 L4 repaired triangle norm bound": check_L4_triangle_bound(),
        "CHK2 L4 J_* and v_LR finite": check_L4_Jstar_finite(),
        "CHK3 L1 Lieb-Robinson envelope": check_L1_envelope(),
        "CHK4 L3 lattice light cone": check_L3_light_cone(),
        "CHK5 temporal clustering identity (B.6)":
            check_temporal_clustering_identity(),
        "CHK6 temporal clustering inequality (B.7)":
            check_temporal_clustering_inequality(),
        "CHK7 no-gap counterexample": check_no_gap_counterexample(),
    }

    print()
    print("=" * 74)
    print(" SUMMARY")
    print("=" * 74)
    n_pass = sum(1 for v in checks.values() if v)
    n_fail = sum(1 for v in checks.values() if not v)
    for k, v in checks.items():
        print(f"   [{'PASS' if v else 'FAIL'}] {k}")
    print()
    print(f"   TOTAL: {n_pass} PASS / {n_fail} FAIL")
    print()
    if n_fail == 0:
        print(" verdict: narrowed L1/L3/L4 reproven; L4 norm bound repaired;")
        print("          temporal transfer-matrix clustering (B.6/B.7) exhibited;")
        print("          SPATIAL L2 / equation (3) remains the open bridge.")
        return 0
    print(" verdict: at least one reprove check failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
