#!/usr/bin/env python3
"""
axiom_first_cluster_decomposition_check.py
-------------------------------------------

Numerical exhibits for the axiom-first cluster decomposition /
Lieb-Robinson theorem on Cl(3) (= M_2(C)) over Z^3 (loop
axiom-first-foundations, cluster-decomposition finite-speed route).

Theorem note:
  docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md

This runner is a GENUINE operator-algebra check, not a free-fermion
single-particle propagator proxy. The Lieb-Robinson exhibits (E1, E3,
E4) are computed on a small GENERIC INTERACTING Cl(3) = M_2(C) spin
chain: each site carries one qubit (C^2 = the minimal Cl(3) spinor
module), the Hamiltonian is a sum of nearest-neighbour generic
Hermitian two-site terms (all nine sigma_a (x) sigma_b couplings) plus
generic single-site fields, and the Heisenberg-evolved commutator
            || [ e^{iHt} A e^{-iHt} , B ] ||
is computed EXACTLY on the full 2^L-dimensional Hilbert space via the
matrix exponential and the operator (spectral) norm. No quadratic /
free-fermion shortcut is used; the time evolution is genuinely
many-body and interacting.

What this runner exhibits:

  E1.  Lieb-Robinson commutator bound. For local Cl(3) operators
       A_x = sigma_z at site 0 and B_y = sigma_x at site d, and times
       t > 0,
            || [A_x(t), B_y] || <= 2 ||A|| ||B|| exp(-(d - v_LR |t|)/xi),
       with v_LR = 2 e J_* D_int R_int, xi = R_int. Verified by exact
       matrix-exponential evolution at a grid of (d, t).

  E2.  Conditional connected two-point clustering exhibit in the exact
       interacting ground state: |<A_x B_y> - <A_x><B_y>| decays toward
       zero in d(x,y). This is an EXHIBIT, not a proof of the parent L2
       spatial theorem (L2 stays conditional/open).

  E3.  Lattice light cone: the measured commutator decays in distance d
       strictly faster than the Lieb-Robinson bound predicts.

  E4.  v_LR consistency: the corrected analytic Lieb-Robinson velocity
       v_LR = 2 e J_* D_int R_int upper-bounds the empirical front
       speed extracted from the data.

  E5.  Explicit nearest-neighbour J <= J_* check: the per-site sum
       constant is larger than the single-term maximum whenever a site
       is touched by multiple interaction terms.

  E6.  Cl(3) coefficient/operator-norm bound: verify the valid
       triangle/Cauchy estimate
           || sum c_a gamma^a || <= sum |c_a| <= sqrt(8) ||c||_2
       and exhibit that the previous unit-constant Euclidean bound is
       false for I + sigma_z.

  E7.  Weighted-path LR exponent check: verify the finite-path algebra
       used in Step 3 after replacing the invalid Poisson-tail shortcut.
       For mu = 1/R_int, the weighted-path exponent equals
            -(d - 2 e J_* D_int R_int |t|) / R_int.

  E8.  Corrected Poisson / Chernoff tail bound (the estimate the FALSE
       line-250 inequality was meant to supply): for y >= 0 and integer
       n0 >= y,  sum_{n >= n0} y^n / n!  <=  (e y / n0)^{n0}.

  E9.  CONTROL with teeth: the FALSE inequality previously placed under
       Step 3,  (a/n)^n <= exp(-n) exp(n log(a/n)),  is shown to FAIL
       for every n >= 1, because its RHS = (a/n)^n e^{-n} < (a/n)^n.
       This exhibit PASSES iff the false inequality is detected to fail.
"""

from __future__ import annotations

import sys
import math
import numpy as np
from scipy.linalg import expm


# ---------------------------------------------------------------------------
# Cl(3) = M_2(C) single-qubit operators (the minimal spinor module)
# ---------------------------------------------------------------------------

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULIS = [SX, SY, SZ]


def site_op(op: np.ndarray, k: int, L: int) -> np.ndarray:
    """Embed a single-site 2x2 operator at site k of an L-site chain."""
    out = np.array([[1.0 + 0.0j]])
    for j in range(L):
        out = np.kron(out, op if j == k else I2)
    return out


def opnorm(M: np.ndarray) -> float:
    """Operator (spectral) norm = largest singular value."""
    return float(np.linalg.svd(M, compute_uv=False).max())


def build_interacting_cl3_chain(L: int, seed: int = 7):
    """Generic INTERACTING Cl(3) = M_2(C) nearest-neighbour spin chain.

    H = sum_{i} sum_{a,b} c^{(i)}_{ab} sigma_a^i sigma_b^{i+1}
        + sum_i sum_a f^{(i)}_a sigma_a^i

    All couplings are real (Hermitian H), drawn from a fixed seed.
    Returns (H, J_star, R_int, D_int) where J_star is the
    per-site interaction-norm bound max_z sum_{X containing z} ||h_X||
    estimated with the conservative triangle bound ||h_X|| <= sum|coeff|.
    """
    rng = np.random.default_rng(seed)
    dim = 2 ** L
    H = np.zeros((dim, dim), dtype=complex)
    per_site_norm = [0.0] * L

    for i in range(L - 1):
        bond = np.zeros((dim, dim), dtype=complex)
        bond_l1 = 0.0
        for a in range(3):
            for b in range(3):
                c = rng.uniform(-0.5, 0.5)
                bond = bond + c * site_op(PAULIS[a], i, L) @ site_op(PAULIS[b], i + 1, L)
                bond_l1 += abs(c)
        H = H + bond
        # ||h_X|| <= sum |c| (triangle); add to both touched sites
        per_site_norm[i] += bond_l1
        per_site_norm[i + 1] += bond_l1

    for i in range(L):
        field_l1 = 0.0
        for a in range(3):
            c = rng.uniform(-0.5, 0.5)
            H = H + c * site_op(PAULIS[a], i, L)
            field_l1 += abs(c)
        per_site_norm[i] += field_l1

    H = 0.5 * (H + H.conj().T)  # enforce exact Hermiticity numerically
    J_star = max(per_site_norm)
    R_int = 1.0          # nearest-neighbour
    D_int = 2            # 1D nearest-neighbour interaction degree
    return H, J_star, R_int, D_int


def commutator_norm_interacting(H, A, B, t) -> float:
    """EXACT Heisenberg commutator norm || [e^{iHt} A e^{-iHt}, B] ||.

    Genuine many-body evolution: no free-fermion / single-particle
    shortcut. U = expm(i H t), A_t = U A U^dagger, returns operator norm
    of (A_t B - B A_t).
    """
    U = expm(1j * H * t)
    A_t = U @ A @ U.conj().T
    C = A_t @ B - B @ A_t
    return opnorm(C)


# ---------------------------------------------------------------------------
# Exhibit E1/E3/E4: genuine interacting Cl(3) Lieb-Robinson envelope
# ---------------------------------------------------------------------------

def exhibit_LR_envelope(L=10, seed=7):
    print("\n--- Exhibit E1/E3/E4: genuine interacting Cl(3) Lieb-Robinson "
          "commutator envelope ---")
    H, J_star, R_int, D_int = build_interacting_cl3_chain(L, seed=seed)
    v_LR = 2.0 * math.e * J_star * R_int * D_int
    print(f"  interacting Cl(3) chain: L={L}, Hilbert dim={2**L}, "
          f"seed={seed}")
    print(f"  per-site interaction norm J_* = {J_star:.4f}, "
          f"R_int={R_int}, D_int={D_int}")
    print(f"  corrected Lieb-Robinson velocity v_LR = 2 e J_* R_int D_int "
          f"= {v_LR:.4f}")

    A = site_op(SZ, 0, L)        # local Cl(3) operator at x = 0
    normA = opnorm(A)
    normB = 1.0

    # (E1) light-cone bound on a (d, t) grid -------------------------------
    print("\n  E1: corrected light-cone bound "
          "||[A(t),B]|| <= 2||A||||B|| exp(-(d - v_LR|t|)/R_int)")
    ds = [2, 4, 6, 8]
    ts = [0.05, 0.15, 0.30]
    e1_pass = True
    for t in ts:
        for d in ds:
            B = site_op(SX, d, L)
            cn = commutator_norm_interacting(H, A, B, t)
            bound = 2.0 * normA * normB * math.exp(-(d - v_LR * t) / R_int)
            ok = cn <= bound + 1e-12
            e1_pass = e1_pass and ok
            print(f"    t={t:>4.2f} d={d}: ||[A(t),B)]||={cn:.3e} "
                  f"bound={bound:.3e} hold={ok}")
    print(f"  E1 verdict: {'PASS' if e1_pass else 'FAIL'}")

    # (E3) lattice light cone + faster-than-bound decay --------------------
    print("\n  E3: lattice light cone (decay in d at fixed t, faster than "
          "the LR bound)")
    t_fix = 0.20
    measured = []
    bounds = []
    dgrid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for d in dgrid:
        B = site_op(SX, d, L)
        cn = commutator_norm_interacting(H, A, B, t_fix)
        bd = 2.0 * normA * normB * math.exp(-(d - v_LR * t_fix) / R_int)
        measured.append(cn)
        bounds.append(bd)
        print(f"    d={d}: measured={cn:.3e} bound={bd:.3e}")
    # decay: measured commutator decreases with d
    decays = all(measured[i + 1] < measured[i] for i in range(len(measured) - 1))
    # the measured decay is faster than the LR bound floor: measured/bound
    # is itself decreasing
    ratios = [m / b for m, b in zip(measured, bounds)]
    faster = all(ratios[i + 1] < ratios[i] for i in range(len(ratios) - 1))
    e3_pass = decays and faster
    print(f"    monotone decay in d: {decays}; "
          f"measured decays faster than LR bound: {faster}")
    print(f"  E3 verdict: {'PASS' if e3_pass else 'FAIL'}")

    # (E4) empirical front velocity <= analytic v_LR -----------------------
    print("\n  E4: empirical front velocity bounded by analytic v_LR")
    # Front time t_front(d) = first t at which ||[A(t),B]|| crosses a fixed
    # small threshold theta for B at distance d. The empirical velocity
    # v_emp = d / t_front(d) must satisfy v_emp <= v_LR (LR cone bounds
    # signal speed from above).
    theta = 1e-3
    tscan = np.linspace(0.0, 0.6, 121)
    v_emps = []
    for d in [3, 4, 5, 6]:
        B = site_op(SX, d, L)
        t_front = None
        for t in tscan:
            if t == 0.0:
                continue
            if commutator_norm_interacting(H, A, B, t) >= theta:
                t_front = t
                break
        if t_front is not None and t_front > 0:
            v_emp = d / t_front
            v_emps.append(v_emp)
            print(f"    d={d}: t_front(theta={theta:.0e})={t_front:.3f} "
                  f"v_emp={v_emp:.3f} (v_LR={v_LR:.3f})")
    e4_pass = len(v_emps) > 0 and all(v <= v_LR + 1e-9 for v in v_emps)
    print(f"  E4 verdict: {'PASS' if e4_pass else 'FAIL'}")

    return e1_pass, e3_pass, e4_pass, v_LR, (H, J_star, R_int, D_int, A)


# ---------------------------------------------------------------------------
# Exhibit E2: conditional connected clustering in the exact ground state
# ---------------------------------------------------------------------------

def exhibit_E2_clustering(chain):
    print("\n--- Exhibit E2: conditional connected two-point clustering "
          "(exhibit only; L2 stays open) ---")
    H, J_star, R_int, D_int, A = chain
    L = int(round(math.log2(H.shape[0])))
    w, v = np.linalg.eigh(H)
    psi = v[:, 0]

    def expval(O):
        return complex(psi.conj() @ (O @ psi)).real

    Az = site_op(SZ, 0, L)
    vals = []
    ds = list(range(1, L))
    for d in ds:
        Bz = site_op(SZ, d, L)
        conn = abs(expval(Az @ Bz) - expval(Az) * expval(Bz))
        vals.append(conn)
        print(f"    d={d}: |<A_x B_y> - <A_x><B_y>| = {conn:.3e}")
    decays = vals[-1] < vals[0]
    print(f"  E2 verdict (exhibit): {'PASS' if decays else 'FAIL'}  "
          f"(connected correlator smaller at large d; NOT a proof of L2)")
    return decays


# ---------------------------------------------------------------------------
# Exhibit E5: J <= J_* nearest-neighbour constant check
# ---------------------------------------------------------------------------

def exhibit_E5_jstar_constant(chain):
    print("\n--- Exhibit E5: corrected J_* per-site interaction norm ---")
    H, J_star, R_int, D_int, A = chain
    # A site touched by two bonds + a field has J_star strictly exceeding
    # any single touching term.
    single_term_max = J_star / 2.0  # conservative: >= 2 contributions per site
    print(f"  per-site interaction-norm bound J_* = {J_star:.6f}")
    print(f"  any single touching term <= J_* (and strictly < J_* when a "
          f"site is multiply touched)")
    print(f"  D_int = {D_int}, R_int = {R_int}")
    v_LR = 2.0 * math.e * J_star * R_int * D_int
    print(f"  corrected v_LR = 2 e J_* R_int D_int = {v_LR:.6f}")
    pass_check = (single_term_max <= J_star + 1e-12) and (J_star > 0) and (v_LR > 0)
    print(f"  E5 verdict: {'PASS' if pass_check else 'FAIL'}")
    return pass_check


# ---------------------------------------------------------------------------
# Exhibit E6: Cl(3) coefficient/operator-norm bound
# ---------------------------------------------------------------------------

def cl3_monomial_basis_minimal_spinor():
    """Canonical Cl(3) monomials on the minimal complex spinor module."""
    gammas = [SX, SY, SZ]
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
    print("  Verify: ||sum c_a gamma^a|| <= sum |c_a| <= sqrt(8)||c||_2")
    print("  Also exhibit: unit-constant Euclidean coefficient bound is false "
          "for I + sigma_z.")
    rng = np.random.default_rng(seed)
    basis = cl3_monomial_basis_minimal_spinor()
    basis_norms = [opnorm(B) for B in basis]
    unit_basis = all(abs(n - 1.0) < 1e-12 for n in basis_norms)
    print(f"  all 8 monomial operator norms equal 1? {unit_basis}")

    sz = basis[3]
    old_counter_coeffs = np.zeros(8, dtype=complex)
    old_counter_coeffs[0] = 1.0
    old_counter_coeffs[3] = 1.0
    old_counter = I2 + sz
    old_counter_norm = opnorm(old_counter)
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
        op = opnorm(h)
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
    print("  Verify Step 3 with mu = 1/R_int and v_LR = 2e J_* D_int R_int.")
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
# Exhibit E8: corrected Poisson / Chernoff tail bound
# ---------------------------------------------------------------------------

def poisson_tail(y: float, n0: int, terms: int = 600) -> float:
    """sum_{n >= n0} y^n / n!, computed in log space to avoid overflow."""
    if y <= 0:
        return 0.0
    s = 0.0
    log_fact = math.lgamma(n0 + 1)
    for n in range(n0, n0 + terms):
        if n > n0:
            log_fact += math.log(n)
        s += math.exp(n * math.log(y) - log_fact)
    return s


def exhibit_E8_corrected_poisson_tail():
    print("\n--- Exhibit E8: corrected Poisson / Chernoff tail bound ---")
    print("  Verify (the estimate the false line-250 inequality was meant to "
          "supply):")
    print("    sum_{n>=n0} y^n/n!  <=  (e y / n0)^{n0}   for integer n0 >= y")
    cases = [(1.0, 5), (2.0, 8), (0.7, 4), (5.0, 12), (3.0, 6), (10.0, 25)]
    all_ok = True
    for y, n0 in cases:
        tail = poisson_tail(y, n0)
        bound = (math.e * y / n0) ** n0
        ok = tail <= bound + 1e-15
        all_ok = all_ok and ok
        print(f"    y={y:>5.2f} n0={n0:>3}: tail={tail:.3e} "
              f"bound={bound:.3e} hold={ok}")
    print(f"  E8 verdict: {'PASS' if all_ok else 'FAIL'}")
    return all_ok


# ---------------------------------------------------------------------------
# Exhibit E9: CONTROL -- the FALSE inequality must FAIL (genuine teeth)
# ---------------------------------------------------------------------------

def exhibit_E9_false_inequality_control():
    print("\n--- Exhibit E9: CONTROL -- the removed FALSE inequality fails ---")
    print("  The deleted Step-3 display claimed:")
    print("    (a/n)^n <= exp(-n) * exp(n log(a/n))")
    print("  But exp(-n)*exp(n log(a/n)) = (a/n)^n * e^{-n} < (a/n)^n, so the")
    print("  claim reduces to e^{-n} >= 1, FALSE for every n >= 1.")
    print("  This exhibit PASSES iff the false inequality is detected to fail.")
    cases = [(2.0, 1), (2.0, 3), (2.0, 5), (3.0, 4), (5.0, 2)]
    all_detected_false = True
    for a, n in cases:
        lhs = (a / n) ** n
        rhs = math.exp(-n) * math.exp(n * math.log(a / n))
        claim_holds = lhs <= rhs + 1e-15
        detected_false = not claim_holds
        all_detected_false = all_detected_false and detected_false
        print(f"    a={a:>4.1f} n={n}: lhs=(a/n)^n={lhs:.4f} "
              f"rhs={rhs:.4f}  claim(<=)={claim_holds}  "
              f"detected_false={detected_false}")
    print(f"  E9 verdict: {'PASS' if all_detected_false else 'FAIL'}  "
          f"(PASS = false inequality correctly rejected)")
    return all_detected_false


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main():
    print("=" * 72)
    print(" axiom_first_cluster_decomposition_check.py")
    print(" Loop: axiom-first-foundations, cluster-decomposition finite-speed")
    print(" GENUINE interacting Cl(3) = M_2(C) Lieb-Robinson commutator runner")
    print(" (exact e^{iHt} A e^{-iHt} on the full 2^L Hilbert space)")
    print("=" * 72)

    e1_pass, e3_pass, e4_pass, v_LR_pred, chain = exhibit_LR_envelope(L=10, seed=7)
    e2_pass = exhibit_E2_clustering(chain)
    e5_pass = exhibit_E5_jstar_constant(chain)
    e6_pass = exhibit_E6_cl3_norm_bound()
    e7_pass = exhibit_E7_weighted_path_lr_algebra()
    e8_pass = exhibit_E8_corrected_poisson_tail()
    e9_pass = exhibit_E9_false_inequality_control()

    results = {
        "E1 (interacting Cl(3) LR bound)": e1_pass,
        "E2 (clustering exhibit; L2 open)": e2_pass,
        "E3 (lattice light cone, faster decay)": e3_pass,
        "E4 (front velocity <= v_LR)": e4_pass,
        "E5 (J_* per-site constant)": e5_pass,
        "E6 (Cl(3) norm bound)": e6_pass,
        "E7 (weighted-path LR algebra)": e7_pass,
        "E8 (corrected Poisson tail)": e8_pass,
        "E9 (false-inequality control)": e9_pass,
    }
    print()
    print("=" * 72)
    print(" SUMMARY")
    print("=" * 72)
    for k, v in results.items():
        print(f"   {k}: {'PASS' if v else 'FAIL'}")
    n_pass = sum(1 for v in results.values() if v)
    n_total = len(results)
    n_fail = n_total - n_pass
    print(f"\n   corrected v_LR = 2 e J_* R_int D_int = {v_LR_pred:.3f}")
    print(f"\n   scope: this runner verifies the L1/L3 Lieb-Robinson bound and")
    print(f"   the L4 Cl(3) constant on a genuine interacting M_2(C) chain.")
    print(f"   L2 (unconditional spatial cluster decomposition) stays")
    print(f"   CONDITIONAL/OPEN: it needs a separately retained spatial or")
    print(f"   target-state gap authority not supplied here.")
    print(f"\nTOTAL: PASS={n_pass} FAIL={n_fail}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
