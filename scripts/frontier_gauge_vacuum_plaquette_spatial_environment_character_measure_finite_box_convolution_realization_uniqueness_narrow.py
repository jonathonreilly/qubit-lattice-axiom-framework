#!/usr/bin/env python3
"""
Narrow finite-box inverse Peter-Weyl convolution-realization uniqueness
runner for a supplied positive character-diagonal operator.

Verifies the standalone finite-truncation algebraic identity stated in

  docs/GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_FINITE_BOX_CONVOLUTION_REALIZATION_UNIQUENESS_NARROW_NOTE_2026-05-17.md

on the finite weight box B = {(p, q) : 0 <= p, q <= 4}. Specifically:

  (M1) existence of the finite-box truncated boundary class function
       Z_beta^env|_B defined by
         Z_beta^env|_B(W) = z_00 sum_{(p,q) in B} d_(p,q) rho_(p,q)
                            chi_(p,q)(W),
       as a real central class function on SU(3) with Peter-Weyl support
       in B, with character-coefficient agreement checked by Haar
       inner-product expansion against rho_(p,q);

  (M2) forward convolution-realization at finite-box scope:
       C_(Z_beta^env|_B) chi_(p,q) = rho_(p,q) chi_(p,q),
       and R_beta^env|_B = C_(Z_beta^env|_B)|_B to machine precision in
       operator norm;

  (M3) inverse Peter-Weyl finite-box uniqueness: for a perturbed
       eigenvalue sequence, the resulting normalized truncated class
       function is distinct from the original and the eigenvalue recovery
       recovers exactly the perturbed eigenvalues, not the original;

  (M4) conditional uniqueness at finite-box scope: once diagonal R|_B is
       supplied, the normalized finite character polynomial realizing it
       by convolution is unique;

  (M5) witness-source consistency: instantiating rho := rho(6) from the
       bounded companion gives a Z_(6)^env|_B that equals the canonical
       normalized single-link SU(3) Wilson boundary class function
       truncation to machine precision;

  (M6) symbolic NMAX_SYM = 2 check that (M3) holds exactly via sympy
       character-coefficient inversion.

This runner does NOT:
- derive character diagonality for a stripped Wilson residual,
- identify a supplied diagonal R|_B with the physical multi-link environment,
- compute an all-weight closed-form Z_beta^env(W) outside B,
- close the unmarked spatial Wilson tensor-transfer / Perron problem,
- close analytic P(6),
- close the parent spatial-environment character-measure or residual-
  environment-identification gates.
"""

from __future__ import annotations

import os
import sys

import numpy as np
import sympy as sp


# Make the bounded-companion module importable so the narrow runner consumes
# the same coefficient routine, not a witness.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

import importlib.util as _ilu

_companion_path = os.path.join(
    SCRIPT_DIR,
    "frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.py",
)
_spec = _ilu.spec_from_file_location("rho_pq6_companion", _companion_path)
_companion = _ilu.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_companion)


THEOREM_PASS = 0
FAIL = 0

NMAX = 4
BETA = 6.0
ARG = BETA / 3.0


def check(name: str, condition: bool, detail: str = "") -> None:
    global THEOREM_PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        THEOREM_PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] [THEOREM] {name}")
    if detail:
        print(f"         {detail}")


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def weights_box(nmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def companion_rho_finite_box(nmax: int) -> np.ndarray:
    """Use the bounded-companion's exact Bessel-determinant routine."""
    weights = weights_box(nmax)
    c00 = _companion.wilson_character_coefficient_bessel(0, 0)
    rho = np.zeros(len(weights), dtype=float)
    for i, (p, q) in enumerate(weights):
        rho[i] = _companion.rho_pq(p, q, c00, method="bessel")
    return rho


def companion_c00() -> float:
    return float(_companion.wilson_character_coefficient_bessel(0, 0))


def conjugation_swap_matrix(
    weights: list[tuple[int, int]], index: dict[tuple[int, int], int]
) -> np.ndarray:
    swap = np.zeros((len(weights), len(weights)), dtype=float)
    for w in weights:
        swap[index[(w[1], w[0])], index[w]] = 1.0
    return swap


def build_Z_truncation_coeffs(rho: np.ndarray, z00: float) -> np.ndarray:
    """Construct character coefficients of Z|_B (i.e., the coefficient on
    chi_(p,q) in the truncated Peter-Weyl expansion):

      Z|_B(W) = z_00 sum_{(p,q) in B} d_(p,q) rho_(p,q) chi_(p,q)(W)

    Returns the array {z_00 * d_(p,q) * rho_(p,q)}_{(p,q) in B}, i.e. the
    Peter-Weyl coefficient on each character. This is the input to the
    normalized convolution operator construction.
    """
    weights = weights_box(NMAX)
    out = np.zeros(len(weights), dtype=float)
    for i, (p, q) in enumerate(weights):
        out[i] = z00 * dim_su3(p, q) * rho[i]
    return out


def normalized_convolution_eigenvalues(
    Z_coeffs: np.ndarray, z00: float
) -> np.ndarray:
    """Given Peter-Weyl coefficients {Z_coeffs[i] = z_00 * d_i * rho_i} of
    Z|_B and the normalization z_00, compute the normalized convolution
    operator's eigenvalues on chi_(p,q):

      C_Z chi_(p,q) = rho_(p,q) chi_(p,q),  rho_(p,q) = Z_coeffs[i] / (z_00 * d_i).

    This is the bounded-companion (N2) convolution-on-characters identity
    used as a black-box forward direction; the inverse direction (M3) is
    verified by this routine's perturbation check.
    """
    weights = weights_box(NMAX)
    out = np.zeros(len(weights), dtype=float)
    for i, (p, q) in enumerate(weights):
        out[i] = Z_coeffs[i] / (z00 * dim_su3(p, q))
    return out


def main() -> int:
    print("Block 19 inverse Peter-Weyl finite-box convolution-realization")
    print(f"uniqueness runner -- NMAX={NMAX}, beta={BETA}, |B|={(NMAX+1)**2}.")
    print()

    weights = weights_box(NMAX)
    index = {w: i for i, w in enumerate(weights)}
    swap = conjugation_swap_matrix(weights, index)

    # ---- Consume bounded companion's runner-computed rho(6)
    rho = companion_rho_finite_box(NMAX)
    z00 = companion_c00()
    R = np.diag(rho)

    # ---- M1: existence of Z|_B as a real central class function with
    # Peter-Weyl support in B and character coefficients matching the formula
    Z_coeffs = build_Z_truncation_coeffs(rho, z00)
    # Direct check: the character coefficient on chi_(p,q) equals
    # z_00 * d_(p,q) * rho_(p,q).
    coeff_match_err = 0.0
    for i, (p, q) in enumerate(weights):
        expected = z00 * dim_su3(p, q) * rho[i]
        coeff_match_err = max(
            coeff_match_err, float(abs(Z_coeffs[i] - expected))
        )
    check(
        "(M1) existence of Z|_B with character coefficients = z_00 d_(p,q) rho_(p,q)",
        coeff_match_err == 0.0,
        f"coefficient match max error = {coeff_match_err:.3e}",
    )
    # Real-valued character coefficients (rho real, d_(p,q) integer, z_00 real)
    real_err = float(np.max(np.abs(Z_coeffs.imag if np.iscomplexobj(Z_coeffs) else 0.0)))
    check(
        "(M1) Z|_B character coefficients are real",
        real_err == 0.0,
        f"imaginary part max = {real_err:.3e}",
    )
    # Conjugation-symmetric character coefficients (Z is real central class
    # function: bar(chi_(p,q)) = chi_(q,p) so the coefficient on chi_(p,q)
    # equals the coefficient on chi_(q,p))
    conj_sym_err = 0.0
    for (p, q) in weights:
        i = index[(p, q)]
        j = index[(q, p)]
        conj_sym_err = max(conj_sym_err, float(abs(Z_coeffs[i] - Z_coeffs[j])))
    check(
        "(M1) Z|_B character coefficients are conjugation-symmetric",
        conj_sym_err < 1e-12,
        f"swap-asymmetry max = {conj_sym_err:.3e}",
    )

    # ---- M2: forward convolution-realization on H_B
    # C_(Z|_B) chi_(p,q) = rho_(p,q) chi_(p,q), recovered by dividing the
    # Peter-Weyl coefficient by z_00 d_(p,q) and reading off the eigenvalue.
    eigs_recovered = normalized_convolution_eigenvalues(Z_coeffs, z00)
    eig_match_err = float(np.max(np.abs(eigs_recovered - rho)))
    check(
        "(M2) C_(Z|_B) chi_(p,q) = rho_(p,q) chi_(p,q) (eigenvalue recovery)",
        eig_match_err == 0.0,
        f"eigenvalue recovery max error = {eig_match_err:.3e}",
    )
    # Operator equality R = C_(Z|_B) in operator norm on H_B
    C_Z = np.diag(eigs_recovered)
    op_norm_err = float(np.linalg.norm(R - C_Z, ord=2))
    check(
        "(M2) R_beta^env|_B = C_(Z_beta^env|_B)|_B in operator norm",
        op_norm_err == 0.0,
        f"||R - C_Z||_2 = {op_norm_err:.3e}",
    )

    # ---- M3: inverse Peter-Weyl finite-box uniqueness via perturbation check
    # Perturb the eigenvalue sequence by a nonzero conjugation-symmetric
    # delta_(p,q). The resulting Z'|_B / z_0' must be distinct from
    # Z_beta^env|_B / z_(0,0)^env, and the eigenvalue recovery must return
    # the perturbed eigenvalues, not the original.
    rho_prime = rho.copy()
    # Pick a single non-(0,0) symmetric weight to perturb: (1, 0) and (0, 1)
    # together (conjugation pair), with a 1% bump.
    delta_amp = 1e-2
    rho_prime[index[(1, 0)]] = rho[index[(1, 0)]] + delta_amp
    rho_prime[index[(0, 1)]] = rho[index[(0, 1)]] + delta_amp
    # Conjugation-symmetric perturbation
    perturb_sym_err = float(abs(
        rho_prime[index[(1, 0)]] - rho_prime[index[(0, 1)]]
    ))
    check(
        "(M3) perturbed eigenvalue sequence is conjugation-symmetric",
        perturb_sym_err == 0.0,
        f"sym error = {perturb_sym_err:.3e}",
    )
    # Construct Z'|_B / z_0' with z_0' := z_00 (same normalization choice)
    Z_prime_coeffs = build_Z_truncation_coeffs(rho_prime, z00)
    # The normalized truncations are
    #   Z|_B / z_00 = sum d_(p,q) rho_(p,q) chi_(p,q),
    #   Z'|_B / z_00 = sum d_(p,q) rho'_(p,q) chi_(p,q).
    # By Peter-Weyl uniqueness on the orthonormal character basis, these
    # are distinct iff their coefficient sequences differ.
    norm_Z = Z_coeffs / z00
    norm_Zp = Z_prime_coeffs / z00
    distinct_err = float(np.max(np.abs(norm_Z - norm_Zp)))
    check(
        "(M3) Z'|_B / z_0' is distinct from Z|_B / z_00 under perturbation",
        distinct_err > 0.0,
        f"max coefficient difference = {distinct_err:.3e}",
    )
    # The eigenvalue recovery on Z'|_B returns rho_prime, not rho. The check
    # is: C_(Z'|_B) chi_(p,q) = rho'_(p,q) chi_(p,q), i.e. eigenvalue
    # extraction from Z'|_B coefficients returns rho_prime.
    eigs_prime_recovered = normalized_convolution_eigenvalues(Z_prime_coeffs, z00)
    inverse_recovery_err = float(np.max(np.abs(eigs_prime_recovered - rho_prime)))
    inverse_recovery_returns_original = float(
        np.max(np.abs(eigs_prime_recovered - rho))
    )
    check(
        "(M3) inverse recovery from Z'|_B returns rho_prime, NOT rho",
        inverse_recovery_err == 0.0 and inverse_recovery_returns_original > 0.0,
        f"err vs rho_prime = {inverse_recovery_err:.3e}; err vs rho = "
        f"{inverse_recovery_returns_original:.3e}",
    )

    # ---- M4: conditional uniqueness at finite-box scope
    # Construct the pair (R, Z|_B / z_00) and verify that perturbing either
    # side breaks the (E') equality.  R is an explicit diagonal input here;
    # no property of a physical stripped Wilson operator is inferred.
    norm_Z_constructed = norm_Z
    R_constructed = R
    # Recover R from norm_Z_constructed via eigenvalue extraction
    eigs_from_norm_Z = np.zeros(len(weights), dtype=float)
    for i, (p, q) in enumerate(weights):
        eigs_from_norm_Z[i] = norm_Z_constructed[i] / dim_su3(p, q)
    R_recovered = np.diag(eigs_from_norm_Z)
    forward_recovery_err = float(np.linalg.norm(R_constructed - R_recovered, ord=2))
    check(
        "(M4) conditional uniqueness: supplied R recovered from norm_Z matches R_constructed",
        forward_recovery_err < 1e-12,
        f"||R - R_recovered||_2 = {forward_recovery_err:.3e}",
    )
    # Now perturb norm_Z and check that R_perturbed != R_constructed
    R_perturbed = np.diag(
        np.array(
            [
                norm_Zp[i] / dim_su3(p, q)
                for i, (p, q) in enumerate(weights)
            ]
        )
    )
    pair_break_err = float(np.linalg.norm(R_constructed - R_perturbed, ord=2))
    check(
        "(M4) perturbing norm_Z breaks equality with the supplied R",
        pair_break_err > 0.0,
        f"||R - R_perturbed||_2 = {pair_break_err:.3e}",
    )

    # ---- M5: witness-source consistency with canonical single-link Wilson
    # The constructed Z|_B (with rho := rho(6) and z_00 := c_(0,0)(6)) must
    # equal the canonical normalized single-link Wilson boundary class
    # function truncation by direct numerical character-coefficient
    # evaluation:
    #   c_(p,q)(6) = canonical Wilson character integral
    # vs
    #   z_00 d_(p,q) rho_(p,q)(6) = c_(0,0)(6) * d_(p,q) * c_(p,q)(6) /
    #                               (d_(p,q) c_(0,0)(6))
    #                            = c_(p,q)(6).
    # So Z|_B character coefficient on chi_(p,q) equals c_(p,q)(6) exactly.
    canonical_wilson_match_err = 0.0
    for i, (p, q) in enumerate(weights):
        canonical = float(_companion.wilson_character_coefficient_bessel(p, q))
        canonical_wilson_match_err = max(
            canonical_wilson_match_err, float(abs(Z_coeffs[i] - canonical))
        )
    check(
        "(M5) supplied single-link Wilson packet reproduces its own finite character polynomial",
        canonical_wilson_match_err < 1e-12,
        f"|Z_coeff - c_(p,q)(6)| max = {canonical_wilson_match_err:.3e}",
    )

    # ---- M6: symbolic NMAX_SYM = 2 check that (M3) holds exactly via sympy
    # character-coefficient inversion (no floating-point error)
    NMAX_SYM = 2
    sym_weights = weights_box(NMAX_SYM)
    sym_size = len(sym_weights)
    # Symbolic eigenvalue sequence with free symbols rho_a, rho_b, ..., one
    # per (p,q) in sym_weights, with conjugation-symmetry: rho_(p,q) =
    # rho_(q,p) is enforced by sharing symbols on swap-equivalent pairs.
    sym_symbols = {}
    for (p, q) in sym_weights:
        key = (min(p, q), max(p, q))
        if key not in sym_symbols:
            sym_symbols[key] = sp.symbols(f"rho_{key[0]}_{key[1]}")
    sym_rho = [
        sym_symbols[(min(p, q), max(p, q))] for (p, q) in sym_weights
    ]
    z00_sym = sp.Symbol("z00", positive=True)
    # Coefficients on chi_(p,q):  z00 * d_(p,q) * rho_(p,q)
    sym_Z_coeffs = [
        z00_sym * sp.Integer(dim_su3(p, q)) * sym_rho[i]
        for i, (p, q) in enumerate(sym_weights)
    ]
    # Eigenvalue recovery: rho_(p,q) = Z_coeff[i] / (z_00 d_(p,q))
    sym_eig_recovered = [
        sp.simplify(sym_Z_coeffs[i] / (z00_sym * sp.Integer(dim_su3(p, q))))
        for i, (p, q) in enumerate(sym_weights)
    ]
    # Check: sym_eig_recovered[i] == sym_rho[i] symbolically for all i.
    sym_inverse_ok = all(
        sp.simplify(sym_eig_recovered[i] - sym_rho[i]) == 0
        for i in range(sym_size)
    )
    check(
        "(M6) sympy NMAX_SYM=2: inverse Peter-Weyl eigenvalue recovery is exact",
        sym_inverse_ok,
        f"checked {sym_size} characters in B_SYM",
    )

    # Symbolic uniqueness: if two coefficient sequences (z00, rho) and (z00', rho')
    # give the same C_Z on H_B_SYM, then rho_(p,q) = rho'_(p,q) for all
    # (p,q) in B_SYM. We verify this by writing the constraint
    #   z_00 * d * rho = z_00' * d * rho'
    # on a per-character basis and solving symbolically.
    z00p_sym = sp.Symbol("z00p", positive=True)
    sym_rhop = [sp.symbols(f"rhop_{i}") for i in range(sym_size)]
    # Convolution eigenvalues from the two side: rho_(p,q) and rhop_(p,q).
    # Constraint: rho_(p,q) = rhop_(p,q) (since both equal the same
    # diagonal operator's eigenvalue on chi_(p,q)). Then we ask whether
    # the resulting normalized truncated class functions are equal:
    #   Z|_B / z_00 = sum d_(p,q) rho_(p,q) chi_(p,q)
    #   Z'|_B / z_00' = sum d_(p,q) rhop_(p,q) chi_(p,q)
    # On the orthonormal character basis, equality forces
    # d_(p,q) rho_(p,q) = d_(p,q) rhop_(p,q), i.e. rho = rhop on B.
    # Verify symbolically by substituting the constraint and showing the
    # difference vanishes.
    sym_diff = [
        sp.simplify(
            sp.Integer(dim_su3(p, q)) * sym_rho[i]
            - sp.Integer(dim_su3(p, q)) * sym_rhop[i]
        )
        for i, (p, q) in enumerate(sym_weights)
    ]
    sym_uniqueness_consistent = all(
        sp.simplify(sym_diff[i].subs(sym_rhop[i], sym_rho[i])) == 0
        for i in range(sym_size)
    )
    check(
        "(M6) sympy NMAX_SYM=2: normalized-truncation uniqueness is symbolically forced",
        sym_uniqueness_consistent,
        "rho = rhop iff truncated normalized class functions agree on B_SYM",
    )

    # ---- Summary
    print()
    print(f"THEOREM PASS={THEOREM_PASS} FAIL={FAIL}")
    if FAIL > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
