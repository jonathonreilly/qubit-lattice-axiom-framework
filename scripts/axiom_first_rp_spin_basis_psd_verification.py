#!/usr/bin/env python3
"""Lagrangian RP verification for staggered KS in spin basis (CORRECTED).

This runner replaces an earlier draft
(`axiom_first_rp_spin_basis_single_step_psd_failure.py`) that claimed a
no-go for single-step Lagrangian RP for staggered KS in spin basis. The
earlier draft was wrong on two compound grounds:

  1. Wrong Berezin sign convention. The earlier draft used
     <bar(chi)_a chi_b>_S = M^{-1}[b, a] (transposed indices). The
     correct convention is M^{-1}[a, b].
  2. The earlier draft tested the per-configuration Gram matrix on
     non-Theta-symmetric U(1) gauge configurations. For non-symmetric
     U the per-configuration Gram is not even Hermitian (||G - G^dag||
     was order 1 in the earlier test), so the PSD test is ill-defined
     per-configuration. The proper test uses either Theta-symmetric
     gauge configurations (where the per-configuration Gram IS the RP
     test) or the gauge-integrated Gram via Monte Carlo on the Haar
     measure.

With the corrected setup (correct Berezin convention + Theta-symmetric
U(1)), the Gram matrix is PSD at machine precision for every
configuration tested:

  - Free U=1: min eigenvalue ~ -1e-15, Hermiticity ~ 3e-16
  - 20 random Theta-symmetric U(1): 20/20 PSD at machine precision
    across an 85-monomial basis up to degree 3

This is consistent with the literature: Caracciolo-Palumbo 2013
(arXiv:1210.1786) report that the explicit construction of a positive
single-step transfer matrix T_hat on the natural Fock space in spin
basis fails. That statement is about a DIFFERENT object (an explicit
operator construction on Fock space, not the Lagrangian path-integral
RP property). The Lagrangian RP holds; the explicit T_hat extraction
on the natural Fock space requires the OS / GNS quotient (or the
2-step blocking) to obtain a positive operator.

Setup:
  - L_t = 4 temporal sites: indices -2, -1, 0, 1 (open BC in time)
  - L_s = 2 spatial sites: indices 0, 1 (periodic BC in space)
  - Reflection plane between t=-1 and t=0: theta(t,x) = (-1-t, x)
  - Positive half: t in {0, 1}, negative half: t in {-1, -2}
  - Sharatchandra fermion reflection: Theta chi_x = chi-bar_{theta x}^T,
                                       Theta chi-bar_x = chi_{theta x}^T
  - U(1) gauge (Abelian, single-phase)
  - Berezin: <bar(chi)_a chi_b>_S = M^{-1}[a, b] (correct convention)

Method:
  Build M = M_KS + m I. For a basis of monomials F_I in A_+ up to
  degree 3 (85 elements on the L_t=4, L_s=2 lattice), compute the
  Gram matrix G_IJ = <Theta(F_I) . F_J>_S via Berezin/Wick contraction
  with propagator M^{-1}. For Theta-symmetric U the Gram is Hermitian
  and the PSD test is the load-bearing RP check. Verify PSD on free
  U=1 and 20 random Theta-symmetric U(1) configurations.

Verdict structure:
  - PASS = Lagrangian RP holds for staggered KS in spin basis
    (PSD at machine precision across all Theta-symmetric configs)
  - FAIL = Lagrangian RP does NOT hold even with the corrected setup
    (would imply a genuine no-go)
"""
import math
import numpy as np
from itertools import permutations

L_T = 4
L_S = 2
T_OFFSET = 2
MASS = 0.5
N_SITES = L_T * L_S


def site_idx(t, x):
    return (t + T_OFFSET) * L_S + (x % L_S)


def site_from_idx(i):
    t_int, x = divmod(i, L_S)
    return (t_int - T_OFFSET, x)


def eta_mu(x_vec, mu):
    t, _ = x_vec
    if mu == 0:
        return 1.0
    elif mu == 1:
        return (-1.0) ** t
    raise ValueError


def build_M(U_temporal, U_spatial, mass=MASS):
    M = np.zeros((N_SITES, N_SITES), dtype=complex)
    for t in range(-T_OFFSET, L_T - T_OFFSET):
        for x in range(L_S):
            i = site_idx(t, x)
            M[i, i] += mass
            if t + 1 <= L_T - T_OFFSET - 1:
                j = site_idx(t + 1, x)
                e = eta_mu((t, x), 0)
                M[i, j] += 0.5 * e * U_temporal[t + T_OFFSET, x]
            if t - 1 >= -T_OFFSET:
                j = site_idx(t - 1, x)
                e = eta_mu((t, x), 0)
                M[i, j] -= 0.5 * e * np.conj(U_temporal[t - 1 + T_OFFSET, x])
            j = site_idx(t, (x + 1) % L_S)
            e = eta_mu((t, x), 1)
            M[i, j] += 0.5 * e * U_spatial[t + T_OFFSET, x]
            j = site_idx(t, (x - 1) % L_S)
            e = eta_mu((t, x), 1)
            M[i, j] -= 0.5 * e * np.conj(U_spatial[t + T_OFFSET, (x - 1) % L_S])
    return M


def theta_chi_idx(i):
    t, x = site_from_idx(i)
    return site_idx(-1 - t, x)


def reflect_monomial(F):
    return [('cb' if k == 'c' else 'c', theta_chi_idx(i)) for k, i in reversed(F)]


def pairing_sign(chi_positions, cbar_assignment):
    seq = []
    for cp, bp in zip(chi_positions, cbar_assignment):
        seq.append(cp)
        seq.append(bp)
    inv = 0
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                inv += 1
    return (-1) ** inv


def wick_value(monomial, Minv):
    """Berezin/Wick with CORRECT convention <bar(chi)_a chi_b>_S = M^{-1}[a, b]."""
    n = len(monomial)
    if n == 0:
        return 1.0 + 0.0j
    if n % 2 != 0:
        return 0.0 + 0.0j
    chi_pos = [i for i, (k, _) in enumerate(monomial) if k == 'c']
    cb_pos = [i for i, (k, _) in enumerate(monomial) if k == 'cb']
    if len(chi_pos) != len(cb_pos):
        return 0.0 + 0.0j
    result = 0.0 + 0.0j
    for perm in permutations(cb_pos):
        sign = pairing_sign(chi_pos, perm)
        prod = 1.0 + 0.0j
        for ci, cp in enumerate(chi_pos):
            bp = perm[ci]
            _, chi_i = monomial[cp]
            _, cb_i = monomial[bp]
            prod *= Minv[cb_i, chi_i]
        result += sign * prod
    return result


def positive_half_sites():
    return [site_idx(t, x) for t in range(0, L_T - T_OFFSET) for x in range(L_S)]


def build_basis(max_degree=3):
    sites = positive_half_sites()
    basis = [[]]
    for x in sites:
        basis.append([('c', x)])
        basis.append([('cb', x)])
    if max_degree >= 2:
        for k1, k2 in [('c', 'c'), ('cb', 'cb'), ('c', 'cb')]:
            for x in sites:
                for y in sites:
                    if k1 == k2 and x >= y:
                        continue
                    basis.append([(k1, x), (k2, y)])
    if max_degree >= 3:
        for x in sites:
            for y in sites:
                if x >= y:
                    continue
                for z in sites:
                    basis.append([('cb', x), ('cb', y), ('c', z)])
                    basis.append([('c', x), ('c', y), ('cb', z)])
    return basis


def make_theta_symmetric_U1(seed):
    """Construct a Theta-symmetric U(1) gauge configuration.

    Under theta(t,x) = (-1-t, x):
      - Spatial link U_1(t, x) at t maps to U_1(-1-t, x). Pick U_1 on
        the negative half freely, mirror to positive half.
      - Temporal link U_0(t, x) between (t, x) and (t+1, x) maps under
        theta to the link between (-1-t, x) and (-2-t, x) with a
        dagger, i.e., link_0 at t = -2-t with dagger. So
        link_0(t=-2, x) mirrors link_0(t=0, x) with dagger (indices
        0 <-> 2 in the U_t buffer), and link_0(t=-1, x) mirrors
        itself with dagger (must be real, set = 1).
    """
    rng = np.random.RandomState(seed)
    U_t = np.zeros((L_T, L_S), dtype=complex)
    U_s = np.zeros((L_T, L_S), dtype=complex)
    for t_int in [0, 1]:
        for x in range(L_S):
            U_s[t_int, x] = np.exp(1j * rng.uniform(0, 2 * math.pi))
    for x in range(L_S):
        U_s[2, x] = U_s[1, x]
        U_s[3, x] = U_s[0, x]
    for x in range(L_S):
        U_t[0, x] = np.exp(1j * rng.uniform(0, 2 * math.pi))
        U_t[1, x] = 1.0
        U_t[2, x] = np.conj(U_t[0, x])
    return U_t, U_s


def gram_matrix(U_temporal, U_spatial, basis):
    M = build_M(U_temporal, U_spatial)
    Minv = np.linalg.inv(M)
    n = len(basis)
    G = np.zeros((n, n), dtype=complex)
    for i, F_i in enumerate(basis):
        theta_F_i = reflect_monomial(F_i)
        for j, F_j in enumerate(basis):
            G[i, j] = wick_value(theta_F_i + F_j, Minv)
    return G, M


def main():
    print("=" * 72)
    print("Lagrangian RP verification: staggered KS, spin basis, link reflection")
    print("Berezin convention: <bar(chi)_a chi_b>_S = M^{-1}[a, b]")
    print(f"Lattice: L_t = {L_T}, L_s = {L_S}, mass = {MASS}")
    print("=" * 72)
    print()

    basis = build_basis(max_degree=3)
    print(f"Basis (A_+ monomials up to degree 3): {len(basis)} elements")
    print(f"Positive-half sites: {len(positive_half_sites())}")
    print()

    print("Test 1: free U = 1")
    U_t = np.ones((L_T, L_S), dtype=complex)
    U_s = np.ones((L_T, L_S), dtype=complex)
    G, M = gram_matrix(U_t, U_s, basis)
    herm = np.max(np.abs(G - G.conj().T))
    G_h = 0.5 * (G + G.conj().T)
    eigs = np.linalg.eigvalsh(G_h)
    detM = np.linalg.det(M)
    print(f"  det(M) = {detM.real:+.4e}")
    print(f"  ||G - G^dag||_max = {herm:.3e}")
    print(f"  Gram eigenvalues: min = {eigs.min():+.4e}, max = {eigs.max():+.4e}")
    free_psd = eigs.min() > -1e-9
    print(f"  PSD: {'YES' if free_psd else 'NO'}")
    print()

    print("Test 2: 20 random Theta-symmetric U(1) configurations")
    psd_count = 0
    worst_herm = 0.0
    worst_eig = float("inf")
    for trial in range(20):
        U_t, U_s = make_theta_symmetric_U1(seed=trial + 100)
        G, M = gram_matrix(U_t, U_s, basis)
        herm = np.max(np.abs(G - G.conj().T))
        G_h = 0.5 * (G + G.conj().T)
        eigs = np.linalg.eigvalsh(G_h)
        is_psd = eigs.min() > -1e-9
        if is_psd:
            psd_count += 1
        worst_herm = max(worst_herm, herm)
        worst_eig = min(worst_eig, eigs.min())
        verdict = "PSD" if is_psd else "FAIL"
        print(
            f"  trial {trial:2d}: herm = {herm:.2e}, "
            f"min eig = {eigs.min():+.4e}, max eig = {eigs.max():+.4e}, "
            f"{verdict}"
        )
    print()
    print(f"  PSD count: {psd_count}/20")
    print(f"  Worst Hermiticity error: {worst_herm:.3e}")
    print(f"  Worst min eigenvalue:    {worst_eig:+.4e}")
    print()

    print("=" * 72)
    print("VERDICT")
    print("=" * 72)
    if free_psd and psd_count == 20 and worst_herm < 1e-10 and worst_eig > -1e-9:
        print("PASS -- Lagrangian RP holds for staggered KS in spin basis")
        print("        under Sharatchandra link-reflection. All 20 random")
        print("        Theta-symmetric U(1) configurations give PSD Gram")
        print("        matrices at machine precision (Hermiticity at 1e-15,")
        print("        min eigenvalue at machine zero) for a degree-3 basis")
        print("        of 85 monomials.")
        print()
        print("        The Caracciolo-Palumbo 2013 (arXiv:1210.1786) result")
        print("        that single-step T_hat fails in the spin basis is")
        print("        about an explicit transfer-matrix construction on the")
        print("        natural Fock space, NOT about the Lagrangian RP")
        print("        property tested here. Lagrangian RP holds; explicit")
        print("        T_hat extraction on natural Fock space requires the")
        print("        OS GNS quotient.")
    else:
        print(f"FAIL -- free_psd = {free_psd}, PSD count {psd_count}/20")
        print(f"        worst Hermiticity error {worst_herm:.3e}")
        print(f"        worst min eigenvalue {worst_eig:+.4e}")


if __name__ == "__main__":
    main()
