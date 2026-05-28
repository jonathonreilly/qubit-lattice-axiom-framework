#!/usr/bin/env python3
"""APS eta-invariant scoping runner for staggered Dirac on Z^3 x S^1.

Verifies the narrow scoping claims of
docs/HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING_SCOPING_NOTE_2026-05-26.md

Claims verified:

  (L1)  Bulk-spectrum-symmetry bulk-vanishing: the Hermitian staggered
        Dirac operator on Z^3 x S^1 at minimal block L_s = 2,
        L_t in {2, 4}, APBC, mean-field gauge u_0 delta_{ab}, m = 0,
        has signed-sum-of-eigenvalues = 0 identically (Sum sign(lambda) = 0).

  (L2)  Identity-collapse at d=4: the three rationals
          A(d) = 2^(1 - d)
          B(d) = 1 / (2d)
          C(d) = 1 - eta(d)/zeta(d)
        coincide on 1/8 at d = 4 and the simultaneous coincidence
        A(d) = B(d) = C(d) for integer d >= 2 holds uniquely at d = 4
        (equivalent to the existing integer-alignment equation
        2^(d-2) = d, witness (iii) of
        HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR
        narrow theorem note 2026-05-10).

All checks are exact-rational (Fraction / sympy) or floating-point
numpy on small finite matrices. No PDG, no Monte Carlo, no observational
comparator.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from itertools import product
from typing import Callable

import numpy as np
import sympy as sp


# ----------------------------------------------------------------------
# Check infrastructure
# ----------------------------------------------------------------------
PASS = 0
FAIL = 0
FAILURES: list[str] = []


def check(name: str, predicate: Callable[[], bool], detail: str = "") -> None:
    global PASS, FAIL
    try:
        ok = predicate()
    except Exception as e:  # noqa: BLE001
        ok = False
        detail = f"{detail} (exception: {e!r})"
    if ok:
        PASS += 1
        print(f"  PASS: {name}")
    else:
        FAIL += 1
        FAILURES.append(f"{name}: {detail}")
        print(f"  FAIL: {name} -- {detail}")


# ----------------------------------------------------------------------
# Section 1: Lemma L1 -- bulk-spectrum-symmetry on the framework block
# ----------------------------------------------------------------------
# We verify (L1) two ways:
#   (1) Algebraically on the analytic eigenvalue structure
#       lambda^2(k, omega) = u_0^2 * (sum sin^2(k_mu) + sin^2(omega))
#       with APBC mode lattice. The Hermitian operator anticommutes with
#       staggered Gamma_5, so each |lambda| appears with both signs.
#   (2) Numerically on an explicit Hermitian staggered Dirac matrix on
#       L_s = 2 x L_s = 2 x L_s = 2 x L_t in {2, 4} (so total sites N =
#       8 * L_t), built from the standard Kogut-Susskind kinetic term.
print("Section 1: Bulk-vanishing lemma L1")


def staggered_phase(coords: tuple[int, ...], mu: int) -> int:
    """Kogut-Susskind staggered phase eta_mu(x) = (-1)^{x_0 + ... + x_{mu-1}}.

    For mu = 0 (time), phase = +1.
    """
    return (-1) ** sum(coords[:mu])


def build_staggered_dirac(L_s: int, L_t: int, u_0: float = 1.0) -> np.ndarray:
    """Build the L_s^3 x L_t Hermitian staggered Dirac with APBC in time
    and APBC in space (matching the framework parent narrow theorem).

    H_stag = sum_mu (i/2) eta_mu(x) [shift_+mu - shift_-mu] * u_0

    Returns an N x N real-skew matrix multiplied by i, so the operator
    is Hermitian. Convention: index sites by (x, y, z, t) with x in
    {0, ..., L_s-1}, t in {0, ..., L_t-1}. APBC means hopping across
    the boundary picks up a -1 phase.

    For L_s = 2 the spatial directions have only one independent
    plaquette per direction; for L_t = 2, 4 the temporal modes are
    the canonical APBC Matsubara modes.
    """
    dims = (L_s, L_s, L_s, L_t)
    N = L_s ** 3 * L_t

    def site_index(coords: tuple[int, int, int, int]) -> int:
        x, y, z, t = coords
        return ((x * L_s + y) * L_s + z) * L_t + t

    H = np.zeros((N, N), dtype=complex)
    for coords in product(range(L_s), range(L_s), range(L_s), range(L_t)):
        i = site_index(coords)
        for mu, L_mu in enumerate(dims):
            # Forward hop in direction mu, with APBC sign at wraparound
            new = list(coords)
            new[mu] = (coords[mu] + 1) % L_mu
            sign = -1 if new[mu] == 0 and coords[mu] == L_mu - 1 else +1
            j = site_index(tuple(new))
            phase = staggered_phase(coords, mu)
            # H_{ij} = +i/2 eta_mu(x) * sign * u_0
            H[i, j] += 1j * 0.5 * phase * sign * u_0
            # Hermitian conjugate: H_{ji} = -i/2 eta_mu(x) * sign * u_0
            H[j, i] += -1j * 0.5 * phase * sign * u_0
    return H


def gamma5_staggered(L_s: int, L_t: int) -> np.ndarray:
    """Staggered Gamma_5 = (-1)^{x + y + z + t} (sublattice parity)."""
    N = L_s ** 3 * L_t
    diag = np.empty(N)
    idx = 0
    for x, y, z, t in product(range(L_s), range(L_s), range(L_s), range(L_t)):
        diag[idx] = (-1) ** (x + y + z + t)
        idx += 1
    return np.diag(diag)


def s1_construction_L_t2_hermitian() -> bool:
    """H_stag is Hermitian for L_t = 2."""
    H = build_staggered_dirac(2, 2)
    return np.allclose(H, H.conj().T, atol=1e-12)


def s1_construction_L_t4_hermitian() -> bool:
    """H_stag is Hermitian for L_t = 4."""
    H = build_staggered_dirac(2, 4)
    return np.allclose(H, H.conj().T, atol=1e-12)


def s1_chirality_anticommutes_L_t2() -> bool:
    """{Gamma_5, H_stag} = 0 for L_t = 2."""
    H = build_staggered_dirac(2, 2)
    G5 = gamma5_staggered(2, 2)
    anticomm = G5 @ H + H @ G5
    return np.allclose(anticomm, 0, atol=1e-12)


def s1_chirality_anticommutes_L_t4() -> bool:
    """{Gamma_5, H_stag} = 0 for L_t = 4."""
    H = build_staggered_dirac(2, 4)
    G5 = gamma5_staggered(2, 4)
    anticomm = G5 @ H + H @ G5
    return np.allclose(anticomm, 0, atol=1e-12)


def s1_spectrum_pm_paired_L_t2() -> bool:
    """Eigenvalues of H_stag at L_t = 2 come in +/- pairs."""
    H = build_staggered_dirac(2, 2)
    w = np.linalg.eigvalsh(H)
    # Sort by magnitude, then check that for each lambda > 0 there is a
    # corresponding -lambda within tolerance.
    pos = sorted(w[w > 1e-9])
    neg = sorted(-w[w < -1e-9])
    return len(pos) == len(neg) and np.allclose(pos, neg, atol=1e-9)


def s1_spectrum_pm_paired_L_t4() -> bool:
    """Eigenvalues of H_stag at L_t = 4 come in +/- pairs."""
    H = build_staggered_dirac(2, 4)
    w = np.linalg.eigvalsh(H)
    pos = sorted(w[w > 1e-9])
    neg = sorted(-w[w < -1e-9])
    return len(pos) == len(neg) and np.allclose(pos, neg, atol=1e-9)


def s1_signed_sum_zero_L_t2() -> bool:
    """Signed sum of eigenvalues = 0 at L_t = 2 (bare eta)."""
    H = build_staggered_dirac(2, 2)
    w = np.linalg.eigvalsh(H)
    signed_sum = float(np.sum(np.sign(w[np.abs(w) > 1e-9])))
    return abs(signed_sum) < 1e-9


def s1_signed_sum_zero_L_t4() -> bool:
    """Signed sum of eigenvalues = 0 at L_t = 4 (bare eta)."""
    H = build_staggered_dirac(2, 4)
    w = np.linalg.eigvalsh(H)
    signed_sum = float(np.sum(np.sign(w[np.abs(w) > 1e-9])))
    return abs(signed_sum) < 1e-9


def s1_eigenvalue_magnitude_L_t2() -> bool:
    """At L_s = 2, L_t = 2, mean-field u_0 = 1, every |lambda|^2 in the
    spectrum should be 4 (= 3 spatial + 1 temporal sin^2)."""
    H = build_staggered_dirac(2, 2, u_0=1.0)
    w = np.linalg.eigvalsh(H)
    expected_lambda_sq = 4.0  # 3 spatial sin^2 (=1 each) + sin^2(pi/2) = 1
    lambda_sq = w ** 2
    return np.allclose(lambda_sq, expected_lambda_sq, atol=1e-9)


def s1_eigenvalue_magnitude_L_t4() -> bool:
    """At L_s = 2, L_t = 4, mean-field u_0 = 1, every |lambda|^2 should
    be 7/2 = 3.5 (= 3 spatial sin^2 + 1/2 Klein-four temporal sin^2)."""
    H = build_staggered_dirac(2, 4, u_0=1.0)
    w = np.linalg.eigvalsh(H)
    expected_lambda_sq = 3.5
    lambda_sq = w ** 2
    return np.allclose(lambda_sq, expected_lambda_sq, atol=1e-9)


def s1_signed_sum_zero_with_u0_variation_L_t4() -> bool:
    """Signed sum is u_0-independent at L_t = 4 (bulk-vanishing is
    robust under mean-field rescaling)."""
    results = []
    for u_0 in [0.5, 1.0, 1.7, 2.3]:
        H = build_staggered_dirac(2, 4, u_0=u_0)
        w = np.linalg.eigvalsh(H)
        signed_sum = float(np.sum(np.sign(w[np.abs(w) > 1e-9])))
        results.append(abs(signed_sum))
    return max(results) < 1e-9


for name, fn in [
    ("L1: H_stag is Hermitian at L_t=2", s1_construction_L_t2_hermitian),
    ("L1: H_stag is Hermitian at L_t=4", s1_construction_L_t4_hermitian),
    ("L1: {Gamma_5, H_stag} = 0 at L_t=2", s1_chirality_anticommutes_L_t2),
    ("L1: {Gamma_5, H_stag} = 0 at L_t=4", s1_chirality_anticommutes_L_t4),
    ("L1: eigenvalues ± paired at L_t=2", s1_spectrum_pm_paired_L_t2),
    ("L1: eigenvalues ± paired at L_t=4", s1_spectrum_pm_paired_L_t4),
    ("L1: Σ sign(λ) = 0 at L_t=2", s1_signed_sum_zero_L_t2),
    ("L1: Σ sign(λ) = 0 at L_t=4", s1_signed_sum_zero_L_t4),
    ("L1: |λ|² = 4 uniform at L_t=2", s1_eigenvalue_magnitude_L_t2),
    ("L1: |λ|² = 7/2 uniform at L_t=4", s1_eigenvalue_magnitude_L_t4),
    ("L1: Σ sign(λ) = 0 stable under u_0 variation at L_t=4", s1_signed_sum_zero_with_u0_variation_L_t4),
]:
    check(name, fn)


# ----------------------------------------------------------------------
# Section 2: Identity collapse L2 at d=4
# ----------------------------------------------------------------------
print("\nSection 2: Identity-collapse observation L2")


def A_of_d(d):
    return sp.Rational(2) ** (1 - d)


def B_of_d(d):
    return sp.Rational(1, 2 * d)


def C_of_d(d):
    return 1 - sp.dirichlet_eta(d) / sp.zeta(d)


def s2_A_at_d4_is_one_eighth() -> bool:
    return sp.simplify(A_of_d(4) - sp.Rational(1, 8)) == 0


def s2_B_at_d4_is_one_eighth() -> bool:
    return sp.simplify(B_of_d(4) - sp.Rational(1, 8)) == 0


def s2_C_at_d4_is_one_eighth() -> bool:
    return sp.simplify(C_of_d(4) - sp.Rational(1, 8)) == 0


def s2_A_equals_C_identity() -> bool:
    """A(d) = C(d) at every integer d in {2,...,8} (Riemann-Dirichlet
    identity in closed-rational form). Sympy does not auto-simplify the
    symbolic ratio eta(s)/zeta(s) but it does evaluate at integer s where
    both eta(s) and zeta(s) have closed pi-form. We check at several
    even s (where the ratio is rational in 1/π^something cancellation)
    and verify A(d) - C(d) simplifies to 0."""
    for d in [2, 4, 6, 8]:
        a = sp.Rational(2) ** (1 - d)
        c = 1 - sp.dirichlet_eta(d) / sp.zeta(d)
        if sp.simplify(a - c) != 0:
            return False
    return True


def s2_simultaneous_only_at_d4() -> bool:
    """A(d) = B(d) iff d in solution set of 2^(d-2) = d, which is unique
    integer solution d = 4 (no other d in {2, ..., 10})."""
    matches = []
    for d in range(2, 11):
        a = A_of_d(d)
        b = B_of_d(d)
        c = C_of_d(d)
        if sp.simplify(a - b) == 0 and sp.simplify(a - c) == 0:
            matches.append(d)
    return matches == [4]


def s2_integer_alignment_eqn() -> bool:
    """2^(d-2) = d unique integer solution at d = 4 among d in [2, 20]."""
    sols = [d for d in range(2, 21) if 2 ** (d - 2) == d]
    return sols == [4]


def s2_witness_collapse_to_riemann_dirichlet() -> bool:
    """A(d) = B(d) collapses to 1/(2d) = 2^(1-d), equivalent to
    d * 2^(2-d) = 1, equivalent to 2^(d-2) = d. This is exactly
    witness (iii) of the
    HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR.

    Direct check: at d=4, 1/(2·4) = 2^(1-4) = 1/8 numerically; and the
    equivalence 1/(2d) = 2^(1-d) <-> 2^(d-2) = d is verified by
    checking the integer solutions of 2^(d-2) = d agree with the
    integer solutions of 1/(2d) = 2^(1-d) on d in [2, 20].
    """
    # Check the algebraic equivalence by enumerating integer solutions.
    sol_a = [d for d in range(2, 21) if sp.Rational(1, 2 * d) == sp.Rational(2) ** (1 - d)]
    sol_b = [d for d in range(2, 21) if 2 ** (d - 2) == d]
    return sol_a == [4] and sol_b == [4] and sol_a == sol_b


for name, fn in [
    ("L2: A(4) = 2^(1-4) = 1/8", s2_A_at_d4_is_one_eighth),
    ("L2: B(4) = 1/(2·4) = 1/8", s2_B_at_d4_is_one_eighth),
    ("L2: C(4) = 1 - η(4)/ζ(4) = 1/8", s2_C_at_d4_is_one_eighth),
    ("L2: A(s) = C(s) as Riemann-Dirichlet identity (multiple integer s)", s2_A_equals_C_identity),
    ("L2: A(d) = B(d) = C(d) unique at d = 4 in {2,...,10}", s2_simultaneous_only_at_d4),
    ("L2: integer alignment 2^(d-2) = d unique at d=4 in {2,...,20}", s2_integer_alignment_eqn),
    ("L2: A=B collapses to the upstream anchor witness (iii)", s2_witness_collapse_to_riemann_dirichlet),
]:
    check(name, fn)


# ----------------------------------------------------------------------
# Section 3: Bare-bulk eta-over-two conjecture test on the bulk surface
# ----------------------------------------------------------------------
# The conjecture claims:
#   eta_APS(D_staggered, framework substrate) / 2 = 1/8
# Lemma L1 establishes eta_APS = 0 on the framework substrate, so the
# left-hand side is 0/2 = 0, not 1/8. Therefore the conjecture is
# not equal on the exact bulk substrate.
#
# This section also records that "1/8 candidates" A, B, C are not
# providing an independent witness via APS-eta on the framework's
# substrate; they are all algebraic expressions in the existing
# integer-alignment identity 2^(d-2) = d.
print("\nSection 3: bare-bulk η_APS/2 = 1/8 test on the bulk substrate")


def s3_eta_aps_over_two_at_L_t2() -> bool:
    """eta_APS / 2 = 0/2 = 0 at L_t = 2 on bulk substrate; not 1/8."""
    H = build_staggered_dirac(2, 2)
    w = np.linalg.eigvalsh(H)
    eta = float(np.sum(np.sign(w[np.abs(w) > 1e-9])))
    eta_over_two = eta / 2.0
    # Conjecture says == 1/8 = 0.125
    return abs(eta_over_two - 0.0) < 1e-9 and abs(eta_over_two - 0.125) > 0.1


def s3_eta_aps_over_two_at_L_t4() -> bool:
    """eta_APS / 2 = 0/2 = 0 at L_t = 4 on bulk substrate; not 1/8."""
    H = build_staggered_dirac(2, 4)
    w = np.linalg.eigvalsh(H)
    eta = float(np.sum(np.sign(w[np.abs(w) > 1e-9])))
    eta_over_two = eta / 2.0
    return abs(eta_over_two - 0.0) < 1e-9 and abs(eta_over_two - 0.125) > 0.1


def s3_conjecture_collapse_into_existing_witnesses() -> bool:
    """If you interpret 'eta_APS / 2 = 1/8' as a rational identity
    (rather than as a spectral computation on the bulk), it reduces to
    one of A, B, C at d=4 -- all equal to 1/8 by L2. This is the same
    algebraic identity as the
    HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR
    witness (iii), not an independent witness."""
    # The three expressions A(4), B(4), C(4) all evaluate to 1/8 by L2.
    # If a putative "eta_APS / 2" computes to 1/8, it shares the same
    # algebraic content unless it provides a structurally distinct
    # derivation surface.
    target = sp.Rational(1, 8)
    A4 = A_of_d(4)
    B4 = B_of_d(4)
    C4 = C_of_d(4)
    return all(sp.simplify(x - target) == 0 for x in (A4, B4, C4))


for name, fn in [
    ("L3: η_APS/2 = 0 ≠ 1/8 on L_t=2 bulk substrate", s3_eta_aps_over_two_at_L_t2),
    ("L3: η_APS/2 = 0 ≠ 1/8 on L_t=4 bulk substrate", s3_eta_aps_over_two_at_L_t4),
    ("L3: 1/8 conjecture collapses into existing A=B=C witnesses (no new content)", s3_conjecture_collapse_into_existing_witnesses),
]:
    check(name, fn)


# ----------------------------------------------------------------------
# Section 4: Gap inventory sanity (NB1-NB3 not present at bulk surface)
# ----------------------------------------------------------------------
# The bulk-vanishing lemma L1 depends on:
#   (i)  staggered chirality {Gamma_5, D} = 0 -- relies on m = 0
#   (ii) ± pairing of eigenvalues
# Any non-trivial eta-invariant must break one of (i), (ii).
print("\nSection 4: Gap inventory consistency")


def s4_mass_breaks_chirality_anticommutation() -> bool:
    """Adding mass term m * epsilon(x) breaks {Gamma_5, D} = 0 for
    nontrivial m, so the L1 anticommutation proof no longer applies.
    A nonzero eta still requires extra structure such as a sign-changing
    Wilson/domain-wall mass."""
    # epsilon(x) = (-1)^(x + y + z + t) is the staggered mass parity
    L_s, L_t = 2, 2
    N = L_s ** 3 * L_t
    diag = []
    for x, y, z, t in product(range(L_s), range(L_s), range(L_s), range(L_t)):
        diag.append((-1) ** (x + y + z + t))
    eps = np.diag(diag)
    H0 = build_staggered_dirac(L_s, L_t)
    m = 0.3
    H_m = H0 + m * eps
    G5 = gamma5_staggered(L_s, L_t)
    anticomm = G5 @ H_m + H_m @ G5
    # {Gamma_5, H_m} should NOT be zero for m != 0 -- this opens the
    # door to non-trivial eta when combined with a sign flip.
    return not np.allclose(anticomm, 0, atol=1e-12)


def s4_uniform_mass_no_sign_flip_still_paired() -> bool:
    """Uniform staggered mass m * epsilon(x) (without sign flip on a
    wall) still gives a zero signed sum on this finite block."""
    L_s, L_t = 2, 2
    N = L_s ** 3 * L_t
    diag = []
    for x, y, z, t in product(range(L_s), range(L_s), range(L_s), range(L_t)):
        diag.append((-1) ** (x + y + z + t))
    eps = np.diag(diag)
    H0 = build_staggered_dirac(L_s, L_t)
    H_m = H0 + 0.3 * eps
    w = np.linalg.eigvalsh(H_m)
    signed_sum = float(np.sum(np.sign(w[np.abs(w) > 1e-9])))
    # eps equals the staggered Gamma_5, so this mass breaks the L1
    # anticommutation relation rather than preserving it. On this finite
    # block the signed sum is still zero; a Wilson/domain-wall APS
    # construction requires extra sign-changing structure across a wall.
    return abs(signed_sum) < 1e-9


for name, fn in [
    ("Gap: nonzero staggered mass breaks the L1 anticommutation proof", s4_mass_breaks_chirality_anticommutation),
    ("Gap: uniform staggered mass still gives Σ sign(λ) = 0 (no wall = no eta)", s4_uniform_mass_no_sign_flip_still_paired),
]:
    check(name, fn)


# ----------------------------------------------------------------------
# Summary
# ----------------------------------------------------------------------
print(f"\n{'=' * 60}")
print(f"PASS={PASS} FAIL={FAIL}")
if FAILURES:
    print("FAILURES:")
    for f in FAILURES:
        print(f"  - {f}")
    sys.exit(1)
sys.exit(0)
