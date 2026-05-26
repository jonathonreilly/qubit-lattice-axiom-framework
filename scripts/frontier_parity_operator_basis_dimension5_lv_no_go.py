#!/usr/bin/env python3
"""
Parity-Operator Basis: Dimension-5 LV Formal Dirac-Signature Runner
===================================================================

Companion runner for
  docs/PARITY_OPERATOR_BASIS_DIMENSION5_LV_NO_GO_THEOREM_NOTE_2026-05-02.md

This runner verifies the bounded formal-signature theorem, narrowed to
templates with odd total spatial-index parity:

  1. The free staggered Hamiltonian H_0 satisfies the sublattice-parity
     anti-symmetry  epsilon H_0 epsilon + H_0 = 0  to machine precision
     on L = 4, 6, 8.

  2. For each of the four named dim-5 SME-style formal Dirac templates,
     an EXHAUSTIVE enumeration over all allowed index assignments
     (mu, nu, rho in {0,1,2,3}) is performed:
       (i) If the total spatial-index parity is odd, the template has
           formal P-sign = -1.
       (ii) If even (the residual mixed/time-only cases excluded from
            the narrowed theorem scope), the template has formal
            P-sign = +1.
     In both cases the Dirac action P_Dirac M P_Dirac^{-1} is combined
     with the explicit formal derivative-label convention
     chi(partial_0)=+1, chi(partial_i)=-1. The runner does not construct
     or claim any actual staggered-lattice derivative representative.

  3. The formal P-symmetric projection vanishes exactly when the total
     spatial-index parity is odd; symmetrically, the formal
     P-antisymmetric projection vanishes when even.

The runner counts ALL allowed index assignments per Dirac structure;
the PASS count therefore reports the number of index combinations
checked, not a representative count.

Status: PASS=N FAIL=0 indicates all algebraic identities verified.
"""

from __future__ import annotations

import sys

import numpy as np


# ---------------------------------------------------------------------------
# Staggered framework primitives
# ---------------------------------------------------------------------------

def lattice_sites(L: int) -> np.ndarray:
    """All sites of an L^3 periodic lattice as integer triples."""
    coords = np.indices((L, L, L)).reshape(3, -1).T
    return coords  # shape (L^3, 3)


def staggered_epsilon(L: int) -> np.ndarray:
    """Sublattice parity epsilon(x) = (-1)^{x1+x2+x3} on Z^3."""
    coords = lattice_sites(L)
    parities = (-1) ** np.sum(coords, axis=1)
    return parities.astype(np.float64)


def staggered_hopping_hamiltonian(L: int) -> np.ndarray:
    """Free staggered fermion Hamiltonian on L^3 periodic lattice with
    standard staggered phases eta_mu(x) (a single-component formulation
    sufficient for the parity check on H_0).

    H_{xy} = (1/2) * sum_mu eta_mu(x) * [delta_{y, x+e_mu} - delta_{y, x-e_mu}]
    """
    coords = lattice_sites(L)
    n_sites = coords.shape[0]
    # Map x -> linear index
    site_index = {tuple(c): i for i, c in enumerate(coords)}

    H = np.zeros((n_sites, n_sites), dtype=np.float64)

    for i, x in enumerate(coords):
        for mu in range(3):
            # Standard staggered phase: eta_1 = 1, eta_2 = (-1)^{x1},
            # eta_3 = (-1)^{x1 + x2}.
            if mu == 0:
                eta = 1.0
            elif mu == 1:
                eta = (-1.0) ** x[0]
            else:
                eta = (-1.0) ** (x[0] + x[1])

            for sign in (+1, -1):
                y = x.copy()
                y[mu] = (y[mu] + sign) % L
                j = site_index[tuple(y)]
                H[i, j] += sign * 0.5 * eta

    return H


# ---------------------------------------------------------------------------
# Formal P-sign computation on the SME-style template basis
# ---------------------------------------------------------------------------

# 4x4 Dirac gammas in the chiral (Weyl) basis
GAMMA0 = np.array([[0, 0, 1, 0],
                   [0, 0, 0, 1],
                   [1, 0, 0, 0],
                   [0, 1, 0, 0]], dtype=np.complex128)

PAULI_X = np.array([[0, 1], [1, 0]], dtype=np.complex128)
PAULI_Y = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
PAULI_Z = np.array([[1, 0], [0, -1]], dtype=np.complex128)
PAULIS = [PAULI_X, PAULI_Y, PAULI_Z]


def gamma_i(i: int) -> np.ndarray:
    """gamma^i in the chiral basis, i in {1,2,3}."""
    sigma = PAULIS[i - 1]
    top = np.zeros((2, 2), dtype=np.complex128)
    return np.block([[top, -sigma], [sigma, top]])


def gamma_mu(mu: int) -> np.ndarray:
    """gamma^mu in the chiral basis, mu in {0,1,2,3}."""
    if mu == 0:
        return GAMMA0
    return gamma_i(mu)


def gamma5() -> np.ndarray:
    """gamma_5 = i gamma^0 gamma^1 gamma^2 gamma^3 in chiral basis."""
    g = 1j * GAMMA0 @ gamma_i(1) @ gamma_i(2) @ gamma_i(3)
    return g


def sigma_munu(mu: int, nu: int) -> np.ndarray:
    """sigma^{mu nu} = (i/2) [gamma^mu, gamma^nu]; mu, nu in {0,1,2,3}."""
    gm = gamma_mu(mu)
    gn = gamma_mu(nu)
    return 0.5j * (gm @ gn - gn @ gm)


def parity_conjugate_gamma(M: np.ndarray) -> np.ndarray:
    """P-conjugation on a Dirac matrix: P M P^{-1} with P_Dirac = gamma^0.

    This is the standard parity action on Dirac bilinears: gamma^0 -> gamma^0,
    gamma^i -> -gamma^i, gamma^5 -> -gamma^5, sigma^{0i} -> -sigma^{0i},
    sigma^{ij} -> sigma^{ij}.
    """
    return GAMMA0 @ M @ GAMMA0


def derivative_parity_sign(deriv_indices) -> int:
    """Formal parity sign of a product of partial-mu labels.

    This is a bookkeeping convention for the formal template theorem,
    not a construction of a staggered-lattice derivative operator.
    Each partial_0 contributes +1; each partial_i (i in {1,2,3})
    contributes -1.
    """
    sign = 1
    for mu in deriv_indices:
        if mu != 0:
            sign = -sign
    return sign


def spatial_index_count(*indices) -> int:
    """Count spatial indices (1,2,3) in a tuple of mu-labels."""
    return sum(1 for mu in indices if mu != 0)


# ---------------------------------------------------------------------------
# Test 1: epsilon H_0 epsilon = -H_0 on staggered free Hamiltonian
# ---------------------------------------------------------------------------

def test_sublattice_parity_anti_commutes_with_H0(L: int):
    H = staggered_hopping_hamiltonian(L)
    eps = staggered_epsilon(L)
    Eps = np.diag(eps)
    lhs = Eps @ H @ Eps
    rhs = -H
    norm_diff = np.linalg.norm(lhs - rhs) / max(np.linalg.norm(H), 1e-12)
    return norm_diff


# ---------------------------------------------------------------------------
# Formal template construction.
#
# A template carries a 4x4 Dirac matrix Gamma and formal derivative labels.
# Its formal parity image is
#
#   P_formal(T) = (P_Dirac Gamma P_Dirac^{-1}) * chi(derivative labels),
#
# where chi(partial_0)=+1 and chi(partial_i)=-1. This is deliberately a
# formal sign convention, not a lattice derivative-representative theorem.
# ---------------------------------------------------------------------------

def full_op_from_structure(Gamma: np.ndarray, deriv_indices) -> np.ndarray:
    """Return the template's Dirac-side matrix.

    The formal derivative sign is carried separately by
    `derivative_parity_sign` and applied in `formal_parity_image`.
    """
    return Gamma


def formal_parity_image(Gamma: np.ndarray, deriv_indices) -> np.ndarray:
    """Apply the formal parity action to a template."""
    Gamma_P = parity_conjugate_gamma(Gamma)
    deriv_sign = derivative_parity_sign(deriv_indices)
    return Gamma_P * deriv_sign


def formal_p_sign(Gamma: np.ndarray, deriv_indices):
    """Return (+1, -1, 0) for the formal P-sign of a template.

    +1 means P_formal(T)=+T, -1 means P_formal(T)=-T.
    """
    image = formal_parity_image(Gamma, deriv_indices)
    if np.allclose(image, Gamma, atol=1e-10):
        return +1
    if np.allclose(image, -Gamma, atol=1e-10):
        return -1
    return 0


# ---------------------------------------------------------------------------
# Tests 2 & 3 (combined, exhaustive)
# ---------------------------------------------------------------------------

# Allowed mu-labels for derivative/gamma indices: 0..3.
INDEX_RANGE = (0, 1, 2, 3)


def is_dispersion_modifying(*all_indices) -> bool:
    """Template filter: at least one spatial index.

    This excludes the pure-time-only case. It is a formal template
    filter and does not assert a physical lattice LV operator.
    """
    return any(mu != 0 for mu in all_indices)


def enumerate_dim5_structures():
    """Yield (structure_label, Gamma_matrix, deriv_indices_tuple,
              all_indices_tuple, spatial_count, structure_class)
    over all allowed index assignments for the four named SME-style
    formal Dirac templates.

    The four classes (per the theorem's exact basis):
      (a) gamma^mu partial_nu partial_rho     -- one gamma index, two derivs
      (b) (unit Clifford) partial_mu partial_nu -- zero gamma indices, two derivs
      (c) gamma_5 gamma^mu partial_nu          -- gamma_5 fixed, one gamma idx, one deriv
      (d) sigma^{mu nu} partial_rho            -- two gamma indices (mu != nu), one deriv
    """
    eye4 = np.eye(4, dtype=np.complex128)

    # (a) gamma^mu partial_nu partial_rho
    for mu in INDEX_RANGE:
        for nu in INDEX_RANGE:
            for rho in INDEX_RANGE:
                # Premise: dispersion-modifying (at least one spatial idx).
                if not is_dispersion_modifying(mu, nu, rho):
                    continue
                label = f"(a) gamma^{mu} partial_{nu} partial_{rho}"
                Gamma = gamma_mu(mu)
                deriv = (nu, rho)
                all_idx = (mu, nu, rho)
                s = spatial_index_count(*all_idx)
                yield label, Gamma, deriv, all_idx, s, "a"

    # (b) 1 * partial_mu partial_nu
    for mu in INDEX_RANGE:
        for nu in INDEX_RANGE:
            if not is_dispersion_modifying(mu, nu):
                continue
            label = f"(b) 1 * partial_{mu} partial_{nu}"
            Gamma = eye4
            deriv = (mu, nu)
            all_idx = (mu, nu)
            s = spatial_index_count(*all_idx)
            yield label, Gamma, deriv, all_idx, s, "b"

    # (c) gamma_5 gamma^mu partial_nu
    g5 = gamma5()
    for mu in INDEX_RANGE:
        for nu in INDEX_RANGE:
            if not is_dispersion_modifying(mu, nu):
                continue
            label = f"(c) gamma_5 gamma^{mu} partial_{nu}"
            Gamma = g5 @ gamma_mu(mu)
            deriv = (nu,)
            # gamma_5 contributes 3 spatial indices (in the contraction
            # 1*2*3); equivalently it has spatial-index parity 1.
            all_idx = (mu, nu)
            s = spatial_index_count(*all_idx) + 3  # gamma_5 contributes 3
            yield label, Gamma, deriv, all_idx, s, "c"

    # (d) sigma^{mu nu} partial_rho   (mu != nu by antisymmetry)
    for mu in INDEX_RANGE:
        for nu in INDEX_RANGE:
            if mu == nu:
                continue
            # sigma^{nu mu} = -sigma^{mu nu}; keep mu < nu to avoid
            # redundant double-counting (the sign on the algebraic side
            # cancels in the formal P-sign identity).
            if mu > nu:
                continue
            for rho in INDEX_RANGE:
                if not is_dispersion_modifying(mu, nu, rho):
                    continue
                label = f"(d) sigma^{{{mu}{nu}}} partial_{rho}"
                Gamma = sigma_munu(mu, nu)
                deriv = (rho,)
                all_idx = (mu, nu, rho)
                s = spatial_index_count(*all_idx)
                yield label, Gamma, deriv, all_idx, s, "d"


def expected_p_weight_from_spatial_parity(spatial_count: int) -> int:
    """The bounded theorem (post-narrowing) claims:
       odd total spatial-index parity  =>  formal P-sign = -1
       even total spatial-index parity =>  formal P-sign = +1
    """
    return -1 if (spatial_count % 2 == 1) else +1


def expected_sym_norm_is_zero(spatial_count: int) -> bool:
    """The P-symmetric projection vanishes iff the template is P-odd,
    i.e. iff spatial_count is odd."""
    return (spatial_count % 2 == 1)


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main() -> int:
    pass_count = 0
    fail_count = 0

    print("=" * 72)
    print("Parity-Operator Basis: Dim-5 LV Formal Dirac-Signature Runner")
    print("(formal templates; odd-total-spatial-index-parity sector)")
    print("=" * 72)

    # ---- Test 1: lattice identity epsilon H_0 epsilon + H_0 = 0 ----
    print("\n[1] epsilon H_0 epsilon + H_0 = 0  on L = 4, 6, 8")
    for L in (4, 6, 8):
        err = test_sublattice_parity_anti_commutes_with_H0(L)
        ok = err < 1e-12
        status = "PASS" if ok else "FAIL"
        if ok:
            pass_count += 1
        else:
            fail_count += 1
        print(f"    L = {L}:  || epsilon H epsilon + H || / || H || = {err:.3e}   [{status}]")

    # ---- Test 2: exhaustive formal P-sign per index assignment ----
    print("\n[2] Exhaustive formal P-sign per allowed index assignment")
    print("    (odd spatial-index parity -> formal P-sign = -1;")
    print("     even spatial-index parity -> formal P-sign = +1)")
    odd_count = 0
    even_count = 0
    by_class = {"a": 0, "b": 0, "c": 0, "d": 0}
    for label, Gamma, deriv, all_idx, s, cls in enumerate_dim5_structures():
        expected = expected_p_weight_from_spatial_parity(s)
        w = formal_p_sign(Gamma, deriv)
        ok = (w == expected)
        if ok:
            pass_count += 1
            by_class[cls] += 1
            if s % 2 == 1:
                odd_count += 1
            else:
                even_count += 1
        else:
            fail_count += 1
            print(f"    [FAIL] {label}: spatial_count={s}, expected formal P-sign={expected:+d}, got {w:+d}")
    print(f"    enumeration totals -- class (a): {by_class['a']}, (b): {by_class['b']}, "
          f"(c): {by_class['c']}, (d): {by_class['d']}")
    print(f"    odd-spatial-parity (theorem sector): {odd_count} templates; "
          f"even-spatial-parity (excluded sector): {even_count} templates")

    # ---- Test 3: exhaustive formal P-symmetric projection per assignment ----
    print("\n[3] Exhaustive formal P-symmetric projection per allowed index assignment")
    print("    (P_sym(T) = (T + P_formal(T))/2; vanishes iff odd-spatial-parity)")
    for label, Gamma, deriv, all_idx, s, cls in enumerate_dim5_structures():
        template = full_op_from_structure(Gamma, deriv)
        image = formal_parity_image(Gamma, deriv)

        sym = 0.5 * (template + image)
        asym = 0.5 * (template - image)
        sym_norm = float(np.linalg.norm(sym))
        asym_norm = float(np.linalg.norm(asym))

        expected_sym_zero = expected_sym_norm_is_zero(s)
        if expected_sym_zero:
            ok = sym_norm < 1e-12
        else:
            ok = asym_norm < 1e-12

        if ok:
            pass_count += 1
        else:
            fail_count += 1
            print(f"    [FAIL] {label}: spatial_count={s}, sym_norm={sym_norm:.3e}, "
                  f"asym_norm={asym_norm:.3e}, expected_sym_zero={expected_sym_zero}")

    print("\n" + "=" * 72)
    print(f"PASS={pass_count}  FAIL={fail_count}")
    print("=" * 72)
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
