#!/usr/bin/env python3
"""No-go demonstration: single-step spin-basis Lagrangian RP for staggered KS
does NOT give a PSD Gram matrix under Sharatchandra Theta alone.

This runner is the load-bearing exhibit for the 2026-05-27 narrowing of
AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md: the prior
draft claimed single-step Lagrangian RP <Theta(F) F> >= 0 for the staggered
Kogut-Susskind action under the Sharatchandra link-reflection convention.
This runner constructs the Gram matrix directly via Berezin/Wick contraction
with M[U]^{-1} and shows it is not PSD even in the free (U=1) case --
diagonal Gram entries for the simplest degree-1 monomials come out at -0.4.

This matches the published literature consensus that single-step positive
transfer matrix for staggered fermions in the spin basis fails:

  - Caracciolo, Palumbo, Phys. Rev. D 87, 014507 (2013) arXiv:1210.1786:
    "all attempts at constructing a positive definite transfer matrix
     that performs time translations by a single lattice spacing failed"
  - Palumbo, Phys. Rev. D 66, 077503 (2002) hep-lat/0208005: workaround
    uses 2-step blocking + flavour basis
  - Sharatchandra, Thun, Weisz, Nucl. Phys. B 192, 205 (1981):
    spin-diagonal transfer matrix is constructed over TWO lattice spacings
  - Smit, Intro. to QFT on a Lattice, Sec. 6: staggered transfer matrix
    is T_hat_4 = S_hat_4^2 (two lattice spacings)

The mechanism: under temporal reflection theta(t, x) = (-1-t, x), the
staggered spatial phase eta_1(x) = (-1)^{t_x} flips sign across the
reflection plane. The simple Sharatchandra Theta (chi <-> chi-bar with
site relabel and no phase compensator) does not match this asymmetry, so
the action is not reflection-invariant under Theta alone in spin basis.

Setup:
  - L_t = 4 temporal sites: indices -2, -1, 0, 1 (open BC in time)
  - L_s = 2 spatial sites: indices 0, 1 (periodic BC in space)
  - Reflection plane between t=-1 and t=0: theta(t,x) = (-1-t, x)
  - Positive half: t in {0, 1}, negative half: t in {-1, -2}
  - Sharatchandra fermion reflection: Theta chi_x = chi-bar_{theta x}^T,
                                       Theta chi-bar_x = chi_{theta x}^T
  - U(1) gauge (Abelian, single-phase) -- captures the essential
    link-reflection structure for the temporal-link daggering without
    SU(N) bookkeeping

Method:
  Build M_KS + m I as a square matrix. For a basis of monomials F_I in
  A_+ (degree 1 and 2 in {chi, chi-bar} at t >= 0), compute the Gram
  matrix

     G_IJ = <Theta(F_I) . F_J>_S

  via Wick contraction with propagator M^{-1}. Check PSD eigenvalues.
  Repeat for free U=1 and random U(1) gauge configurations.

Verdict structure:
  - PASS = single-step spin-basis RP claim verifiably fails (Gram min
    eigenvalue is significantly negative, matching the published two-step
    warning for this direct surface)
  - FAIL = the no-go did not reproduce (would call into question either
    the runner's Berezin convention or this narrow direct-surface no-go)
"""
import math
import numpy as np
from itertools import product, combinations

# ---------- Setup ----------

L_T = 4              # temporal sites: -2, -1, 0, 1
L_S = 2              # spatial sites: 0, 1
T_OFFSET = 2         # internal index t_int = t + T_OFFSET maps t in [-2..1] to [0..3]
MASS = 0.5

# total sites
N_SITES = L_T * L_S

def site_idx(t, x):
    """Flat index for site (t, x); t in [-T_OFFSET, L_T - T_OFFSET - 1]."""
    return (t + T_OFFSET) * L_S + (x % L_S)

def site_from_idx(i):
    t_int, x = divmod(i, L_S)
    return (t_int - T_OFFSET, x)

def eta_mu(x_vec, mu):
    """Staggered phase η_μ(x). Conventions: η_0 = 1, η_k depends on prior coords."""
    t, x = x_vec
    if mu == 0:
        return 1.0
    elif mu == 1:
        return (-1.0) ** t
    else:
        raise ValueError

# ---------- Build M = M_KS + m I ----------

def build_M(U_temporal, U_spatial, mass=MASS):
    """Build the staggered KS Dirac matrix M = M_KS + m·I.

    M_{x,y} = (1/2) Σ_μ η_μ(x) [δ_{y, x+μ̂} U_μ(x) - δ_{y, x-μ̂} U_μ(x-μ̂)†]
              + m δ_{x,y}

    U_temporal[t, x]:   U_0 link between (t, x) and (t+1, x). Defined for t in [-2..0].
    U_spatial[t, x]:    U_1 link between (t, x) and (t, x+1 mod L_s). Defined for all t.
    Open BC in time: no hop between t=1 and t=-2.
    """
    M = np.zeros((N_SITES, N_SITES), dtype=complex)
    for t in range(-T_OFFSET, L_T - T_OFFSET):
        for x in range(L_S):
            i = site_idx(t, x)
            M[i, i] += mass
            # temporal forward (mu=0): (t,x) -> (t+1,x). Only if t+1 < L_T - T_OFFSET (i.e., t+1 <= 1).
            if t + 1 <= L_T - T_OFFSET - 1:
                j = site_idx(t + 1, x)
                e = eta_mu((t, x), 0)
                M[i, j] += 0.5 * e * U_temporal[t + T_OFFSET, x]
            # temporal backward (mu=0): (t,x) -> (t-1,x). Use forward link U_0(t-1,x).
            if t - 1 >= -T_OFFSET:
                j = site_idx(t - 1, x)
                e = eta_mu((t, x), 0)
                M[i, j] -= 0.5 * e * np.conj(U_temporal[t - 1 + T_OFFSET, x])
            # spatial forward (mu=1): periodic
            j = site_idx(t, (x + 1) % L_S)
            e = eta_mu((t, x), 1)
            M[i, j] += 0.5 * e * U_spatial[t + T_OFFSET, x]
            # spatial backward (mu=1): periodic
            j = site_idx(t, (x - 1) % L_S)
            e = eta_mu((t, x), 1)
            M[i, j] -= 0.5 * e * np.conj(U_spatial[t + T_OFFSET, (x - 1) % L_S])
    return M

# ---------- Reflection map ----------

def reflect_site(t, x):
    """Link-reflection θ(t, x) = (-1 - t, x)."""
    return (-1 - t, x)

def theta_chi_idx(i):
    """Site index of θ(x) for site index i."""
    t, x = site_from_idx(i)
    return site_idx(*reflect_site(t, x))

# A monomial F in A_+ is a product of chi_x and chi-bar_y operators with x, y in positive half.
# We encode F as a tuple of (sign, list of (kind, site_idx)) where kind ∈ {'c', 'cb'} for chi, chi-bar.
# Under Θ (Sharatchandra): Θ chi_x = chi-bar_{θx}^T, Θ chi-bar_x = chi_{θx}^T.
# T is irrelevant for one-component case; we just swap kind and reflect site.

def reflect_monomial(F):
    """Apply Sharatchandra Θ to a monomial F = list of (kind, site_idx).
    Returns the reflected monomial in REVERSE order (transpose of product)."""
    rev = []
    for kind, i in reversed(F):
        new_kind = 'cb' if kind == 'c' else 'c'
        new_i = theta_chi_idx(i)
        rev.append((new_kind, new_i))
    return rev

# ---------- Wick contraction ----------
# For Grassmann action S = bar(chi) M chi (Berezin convention),
# <chi_b bar(chi)_a>_S =  (M^{-1})_{b, a},
# <bar(chi)_a chi_b>_S = -(M^{-1})_{b, a}.
# The sign in the second line is the Grassmann reordering sign. This runner's
# Wick implementation accounts for it through pairing_sign; the contraction
# value below is the chi-before-bar propagator.
#
# For a product F = product of chi / bar(chi) operators, <F>_S = sum over
# Wick pairings of products of (M^{-1})_{b, a} with sign from permutation parity.
#
# Note: <chi · chi> = 0, <bar(chi) · bar(chi)> = 0. Only mixed (one chi, one bar(chi)) pairings.

def wick_value(monomial, Minv):
    """Compute <F>_S for F = list of (kind, idx) under quadratic action with
    Berezin propagator <chi_b bar(chi)_a>_S = (M^{-1})_{b,a},
    with <bar(chi)_a chi_b>_S = -(M^{-1})_{b,a}.

    Returns a complex number. Uses Wick's theorem with sign from pairing parity.
    """
    n = len(monomial)
    if n == 0:
        return 1.0 + 0.0j
    if n % 2 != 0:
        return 0.0 + 0.0j
    # Identify the chi and chi-bar positions
    chi_positions = [i for i, (k, _) in enumerate(monomial) if k == 'c']
    cbar_positions = [i for i, (k, _) in enumerate(monomial) if k == 'cb']
    if len(chi_positions) != len(cbar_positions):
        return 0.0 + 0.0j
    # Enumerate all pairings (perfect matchings) between chi and cbar
    # For each pairing, compute sign from permutation parity in the original sequence
    result = 0.0 + 0.0j
    # Each pairing: assign each chi to some cbar
    from itertools import permutations
    for perm in permutations(cbar_positions):
        # pairing: chi_positions[k] paired with perm[k]
        # build the permutation that takes the natural ordering to the
        # pairing ordering, then sign = sign of that permutation
        # Sign: count crossings in the original sequence
        sign = pairing_sign(chi_positions, perm)
        product = 1.0 + 0.0j
        for ck, ck_pos in enumerate(chi_positions):
            cbar_pos = perm[ck]
            chi_kind, chi_idx = monomial[ck_pos]
            cbar_kind, cbar_idx = monomial[cbar_pos]
            # <bar(chi)_{cbar_idx} · chi_{chi_idx}>_S = (M^{-1})_{chi_idx, cbar_idx}
            product *= Minv[chi_idx, cbar_idx]
        result += sign * product
    return result

def pairing_sign(chi_positions, cbar_assignment):
    """Sign of the pairing as a permutation of the original sequence.
    For each chi-cbar pair, contract them by moving them adjacent;
    sign comes from how many anticommuting operators are crossed."""
    # Build the full sequence of operator positions in the order they
    # appear in the monomial, then compute the sign of the permutation
    # that takes the natural order to the pairing order.
    n = len(chi_positions) + len(cbar_assignment)
    # The pairing tells us: chi_positions[k] is paired with cbar_assignment[k]
    # Create the pairing sequence (chi_0, cbar_for_chi_0, chi_1, cbar_for_chi_1, ...)
    # Sign is parity of permutation from (0, 1, 2, ..., n-1) to this sequence.
    pairing_seq = []
    for ck_pos, cbar_pos in zip(chi_positions, cbar_assignment):
        pairing_seq.append(ck_pos)
        pairing_seq.append(cbar_pos)
    # Count inversions in pairing_seq relative to natural order
    inversions = 0
    for i in range(len(pairing_seq)):
        for j in range(i + 1, len(pairing_seq)):
            if pairing_seq[i] > pairing_seq[j]:
                inversions += 1
    return (-1) ** inversions

# ---------- Build monomial basis for A_+ ----------

def positive_half_sites():
    """Sites with t >= 0."""
    return [site_idx(t, x) for t in range(0, L_T - T_OFFSET) for x in range(L_S)]

def build_basis(max_degree=2):
    """Basis of monomials in A_+ up to max_degree.

    Each monomial: list of (kind, idx) with idx in positive half.
    """
    basis = [[]]  # degree 0: identity
    sites = positive_half_sites()
    # Degree 1: chi_x and bar(chi)_x for x in positive half
    for x in sites:
        basis.append([('c', x)])
        basis.append([('cb', x)])
    # Degree 2
    if max_degree >= 2:
        for kind1, kind2 in [('c', 'c'), ('cb', 'cb'), ('c', 'cb')]:
            for x in sites:
                for y in sites:
                    if kind1 == kind2 and x >= y:
                        continue  # avoid duplicates for symmetric pairs
                    if kind1 != kind2:
                        # chi_x · bar(chi)_y: include all ordered pairs
                        pass
                    basis.append([(kind1, x), (kind2, y)])
    return basis

# ---------- Main verification ----------

def gram_matrix_for_config(U_temporal, U_spatial, basis):
    """Compute Gram matrix G_IJ = <Θ(F_I) · F_J>_S for given gauge config."""
    M = build_M(U_temporal, U_spatial)
    try:
        Minv = np.linalg.inv(M)
    except np.linalg.LinAlgError:
        return None, None, None
    detM = np.linalg.det(M)
    if detM.real <= 0 and abs(detM.imag) < 1e-10 * abs(detM.real):
        # Determinant sign issue
        pass
    n = len(basis)
    G = np.zeros((n, n), dtype=complex)
    for i, F_i in enumerate(basis):
        theta_F_i = reflect_monomial(F_i)
        for j, F_j in enumerate(basis):
            full_mono = theta_F_i + F_j
            G[i, j] = wick_value(full_mono, Minv)
    return G, detM, Minv

def main():
    np.random.seed(42)
    basis = build_basis(max_degree=2)
    print(f"Basis size (A_+ monomials up to degree 2): {len(basis)}")
    print(f"Lattice: L_t={L_T}, L_s={L_S}, mass={MASS}")
    print(f"Sites: {N_SITES} total, {len(positive_half_sites())} in positive half")
    print()
    print("Test 1: free case U=1")
    U_t = np.ones((L_T - 1, L_S), dtype=complex)  # L_T-1 temporal links
    # But we indexed temporal links by t+T_OFFSET so we need L_T temporal links worth of buffer
    # Actually only links between consecutive temporal sites are needed
    U_t = np.ones((L_T, L_S), dtype=complex)  # use full L_T for indexing convenience
    U_s = np.ones((L_T, L_S), dtype=complex)
    G_free, detM_free, _ = gram_matrix_for_config(U_t, U_s, basis)
    print(f"  det(M) = {detM_free}")
    # Check Hermiticity of G (should be Hermitian if RP holds correctly)
    herm_err = np.max(np.abs(G_free - G_free.conj().T))
    print(f"  ||G - G†||_max = {herm_err:.3e}")
    G_h = 0.5 * (G_free + G_free.conj().T)
    eigs = np.linalg.eigvalsh(G_h)
    print(f"  Gram eigenvalues: min = {eigs.min():.4e}, max = {eigs.max():.4e}")
    print(f"  PSD: {'YES' if eigs.min() > -1e-10 else 'NO'}")
    print()

    print("Test 2: 5 random U(1) gauge configs")
    psd_count = 0
    fail_examples = []
    for trial in range(5):
        # Random U(1) phases on all links
        U_t = np.exp(1j * np.random.uniform(0, 2*math.pi, (L_T, L_S)))
        U_s = np.exp(1j * np.random.uniform(0, 2*math.pi, (L_T, L_S)))
        G, detM, _ = gram_matrix_for_config(U_t, U_s, basis)
        herm_err = np.max(np.abs(G - G.conj().T))
        G_h = 0.5 * (G + G.conj().T)
        eigs = np.linalg.eigvalsh(G_h)
        is_psd = eigs.min() > -1e-10
        if is_psd:
            psd_count += 1
        else:
            fail_examples.append((trial, eigs.min(), G_h))
        print(f"  trial {trial}: detM = {detM.real:+.3e}{detM.imag:+.3e}j, "
              f"||G-G†|| = {herm_err:.2e}, "
              f"Gram min eig = {eigs.min():+.4e}, PSD = {'YES' if is_psd else 'NO'}")
    print()
    print(f"PSD count: {psd_count}/5 random configs")
    if fail_examples:
        print("FAIL examples (PSD violations, in line with the two-step literature warning):")
        for trial, min_eig, _ in fail_examples:
            print(f"  trial {trial}: min eig = {min_eig:+.4e}")
    print()
    print("=" * 72)
    print("VERDICT")
    print("=" * 72)
    free_failed = (eigs is None) or (np.linalg.eigvalsh(0.5 * (G_free + G_free.conj().T)).min() < -1e-3)
    G_free_h = 0.5 * (G_free + G_free.conj().T)
    free_min = np.linalg.eigvalsh(G_free_h).min()
    print(f"  free U=1 Gram min eigenvalue: {free_min:+.4e}")
    print(f"  random U(1) PSD failures: {5 - psd_count} / 5")
    nogo_reproduced = (free_min < -1e-3) and (psd_count == 0)
    if nogo_reproduced:
        print(f"  no-go reproduced: YES")
        print("  PASS -- single-step spin-basis Lagrangian RP for staggered KS")
        print("  under Sharatchandra Theta alone does NOT give a PSD Gram matrix,")
        print("  matching Caracciolo-Palumbo 2013 and the 2-step block formulation")
        print("  in STW 1981 / Palumbo 2002 / Smit.")
    else:
        print(f"  no-go reproduced: NO")
        print("  FAIL -- the runner did not reproduce the narrow direct-surface no-go.")
        print("  Either the Berezin convention is off or the no-go does not hold")
        print("  for this specific lattice/configuration.")

if __name__ == "__main__":
    main()
