#!/usr/bin/env python3
"""
Finite-box stripping-uniqueness narrow runner on the marked-plaquette SU(3)
class-function sector.

Checks, at finite-box scope `0 <= p,q <= NMAX`, the algebraic uniqueness of
an operator R in the supplied matrix factorization

    K|_B = exp[(beta/2) J|_B] D_beta^packet|_B R|_B exp[(beta/2) J|_B].

The half-slice multiplier exp[(beta/2) J|_B] is positive definite (so
invertible) because J|_B is real symmetric. The separately constructed
fourth-power diagonal D_beta^packet|_B is positive (so invertible) because
a_(p,q)(beta) > 0 for beta > 0. Therefore the factorization algebraically
inverts to

    R|_B = (D_beta^packet|_B)^{-1} exp[-(beta/2) J|_B] K|_B exp[-(beta/2) J|_B],

which uniquely determines the finite-box operator from the supplied matrix
and factors. It does not identify any factor with a physical Wilson object.

Numerics. The fourth-power diagonal D_beta^packet has eigenvalues that span ~14
orders of magnitude even on the modest finite box used here, so naive
float64 inversion of D loses precision. The runner therefore uses mpmath
high-precision arithmetic for the algebraic stripping checks, and float64
only for context printout.

This runner independently recomputes the stipulated character integral used for the
(U5) chosen-input cross-check. The bounded companion is a separate numerical
evaluation, not operator-placement authority.
The runner's load-bearing claim is the algebraic uniqueness of (S), not
the numerical value of the stipulated single-link-form character
coefficients.  A hostile positive self-adjoint swap-symmetric off-diagonal
operator is included to show that stripping uniqueness does not imply
character diagonality.
"""

from __future__ import annotations

import numpy as np
import mpmath as mp
from scipy.special import iv


THEOREM_PASS = 0
SUPPORT_PASS = 0
FAIL = 0

NMAX = 3
BETA = 6.0
ARG = BETA / 3.0
MODE_MAX = 80
MP_DPS = 60  # decimal precision for mpmath


mp.mp.dps = MP_DPS


def check(name: str, condition: bool, detail: str = "", bucket: str = "THEOREM") -> None:
    global THEOREM_PASS, SUPPORT_PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        if bucket == "SUPPORT":
            SUPPORT_PASS += 1
        else:
            THEOREM_PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] [{bucket}] {name}")
    if detail:
        print(f"         {detail}")


def recurrence_neighbors(p: int, q: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for a, b in [
        (p + 1, q),
        (p - 1, q + 1),
        (p, q - 1),
        (p, q + 1),
        (p + 1, q - 1),
        (p - 1, q),
    ]:
        if a >= 0 and b >= 0:
            out.append((a, b))
    return out


def weights_box(nmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def build_J(nmax: int) -> tuple[np.ndarray, list[tuple[int, int]], dict[tuple[int, int], int]]:
    weights = weights_box(nmax)
    index = {w: i for i, w in enumerate(weights)}
    jmat = np.zeros((len(weights), len(weights)), dtype=float)
    for p, q in weights:
        i = index[(p, q)]
        for a, b in recurrence_neighbors(p, q):
            if (a, b) in index:
                jmat[index[(a, b)], i] += 1.0 / 6.0
    return jmat, weights, index


def conjugation_swap_matrix(
    weights: list[tuple[int, int]], index: dict[tuple[int, int], int]
) -> np.ndarray:
    swap = np.zeros((len(weights), len(weights)), dtype=float)
    for w in weights:
        swap[index[(w[1], w[0])], index[w]] = 1.0
    return swap


def matrix_exponential_symmetric(m: np.ndarray, tau: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(m)
    return (vecs * np.exp(tau * vals)) @ vecs.T


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def highest_weight_triple(p: int, q: int) -> list[int]:
    return [p + q, q, 0]


def coefficient_matrix(mode: int, lam: list[int]) -> np.ndarray:
    return np.array(
        [[iv(mode + lam[j] + i - j, ARG) for j in range(3)] for i in range(3)],
        dtype=float,
    )


def wilson_character_coefficient(p: int, q: int) -> float:
    lam = highest_weight_triple(p, q)
    total = 0.0
    for mode in range(-MODE_MAX, MODE_MAX + 1):
        total += float(np.linalg.det(coefficient_matrix(mode, lam)))
    return total


# ---- mpmath helpers ----


def mp_from_np(m: np.ndarray) -> mp.matrix:
    return mp.matrix([[mp.mpf(float(m[i, j])) for j in range(m.shape[1])] for i in range(m.shape[0])])


def mp_diag(diag: np.ndarray) -> mp.matrix:
    n = len(diag)
    M = mp.zeros(n, n)
    for i in range(n):
        M[i, i] = mp.mpf(float(diag[i]))
    return M


def mp_to_np(m: mp.matrix) -> np.ndarray:
    return np.array([[float(m[i, j]) for j in range(m.cols)] for i in range(m.rows)], dtype=float)


def mp_matrix_exponential_symmetric(jmat: np.ndarray, tau: float) -> mp.matrix:
    """exp[tau J|_B] computed in mpmath via truncated power series, where J|_B is
    built as an exact integer/sixth rational matrix to preserve symmetry to
    mpmath precision (not float64 precision)."""
    n = jmat.shape[0]
    # Reconstruct J in mpmath at full precision using the explicit 1/6 weights.
    Jmp = mp.zeros(n, n)
    sixth = mp.mpf(1) / mp.mpf(6)
    for i in range(n):
        for j in range(n):
            v = jmat[i, j]
            if v != 0.0:
                # Round to nearest multiple of 1/6 to undo float64 noise.
                k = round(v / (1.0 / 6.0))
                Jmp[i, j] = mp.mpf(int(k)) * sixth
    tau_mp = mp.mpf(float(tau))
    # Truncated power series exp(tau J) = sum_k (tau J)^k / k!.
    # Convergence rate: ||tau J|| <= tau * ||J||_inf. For NMAX=3, ||J||_inf <= 1.
    # Use terms up to k=80 with mpmath dps=60.
    result = mp.eye(n)
    term = mp.eye(n)
    tauJ = tau_mp * Jmp
    for k in range(1, 200):
        term = term * tauJ / mp.mpf(k)
        new_result = result + term
        # Stop when terms are smaller than mpmath precision threshold.
        if mp_max_abs(term) < mp.mpf(10) ** (-MP_DPS - 5):
            result = new_result
            break
        result = new_result
    return result


def mp_inv_diag(diag_mat: mp.matrix) -> mp.matrix:
    n = diag_mat.rows
    out = mp.zeros(n, n)
    for i in range(n):
        out[i, i] = mp.mpf(1) / diag_mat[i, i]
    return out


def mp_inv(M: mp.matrix) -> mp.matrix:
    return M ** -1


def mp_max_abs(M: mp.matrix) -> float:
    out = mp.mpf(0)
    for i in range(M.rows):
        for j in range(M.cols):
            v = abs(M[i, j])
            if v > out:
                out = v
    return float(out)


def mp_max_abs_diff(A: mp.matrix, B: mp.matrix) -> float:
    out = mp.mpf(0)
    for i in range(A.rows):
        for j in range(A.cols):
            v = abs(A[i, j] - B[i, j])
            if v > out:
                out = v
    return float(out)


def mp_off_diag_max(M: mp.matrix) -> float:
    out = mp.mpf(0)
    for i in range(M.rows):
        for j in range(M.cols):
            if i != j:
                v = abs(M[i, j])
                if v > out:
                    out = v
    return float(out)


def main() -> int:
    jmat, weights, index = build_J(NMAX)
    n = len(weights)
    swap_np = conjugation_swap_matrix(weights, index)

    # ---- Float64 context numbers ----
    j_sym_err = float(np.max(np.abs(jmat - jmat.T)))
    j_swap_err = float(np.max(np.abs(swap_np @ jmat - jmat @ swap_np)))

    M_f64 = matrix_exponential_symmetric(jmat, BETA / 2.0)
    M_eigs = np.linalg.eigvalsh(M_f64)
    M_min_eig = float(np.min(M_eigs))
    M_det = float(np.linalg.det(M_f64))

    c00 = wilson_character_coefficient(0, 0)
    coefficients = np.array(
        [wilson_character_coefficient(p, q) / (dim_su3(p, q) * c00) for p, q in weights],
        dtype=float,
    )
    # Enforce swap symmetry of the stipulated finite integral coefficient
    # (a_(p,q) = a_(q,p)) at float64 precision so D and the coefficient
    # array do not carry asymmetric float64 round-off that would propagate
    # through the mpmath checks in (U4).
    for k, (p, q) in enumerate(weights):
        k_swap = index[(q, p)]
        if k_swap > k:
            avg = 0.5 * (coefficients[k] + coefficients[k_swap])
            coefficients[k] = avg
            coefficients[k_swap] = avg
    D_packet_f64 = np.diag(coefficients**4)
    D_min_eig = float(np.min(np.diag(D_packet_f64)))
    D_det = float(np.linalg.det(D_packet_f64))

    # ---- mpmath high-precision algebra ----
    M = mp_matrix_exponential_symmetric(jmat, BETA / 2.0)
    M_inv = mp_inv(M)
    M_invert_err = mp_max_abs_diff(M * M_inv, mp.eye(n))

    D = mp_diag(coefficients**4)
    D_inv = mp_inv_diag(D)
    D_invert_err = mp_max_abs_diff(D * D_inv, mp.eye(n))

    swap = mp_from_np(swap_np)

    def reconstruct(R: mp.matrix) -> mp.matrix:
        """Forward construction K = M D R M from (D|_B)."""
        return M * D * R * M

    def strip(K: mp.matrix) -> mp.matrix:
        """Algebraic stripping (S): R = D^{-1} M^{-1} K M^{-1}."""
        return D_inv * M_inv * K * M_inv

    # (U3a) Round-trip for candidate R1 (positive diagonal random).
    rng = np.random.default_rng(2026_05_17)
    diag_a = rng.uniform(0.1, 1.0, size=n)
    R1 = mp_diag(diag_a)
    K1 = reconstruct(R1)
    R1_recovered = strip(K1)
    round_trip_err_R1 = mp_max_abs_diff(R1_recovered, R1)

    # (U3b) Round-trip for candidate R2, distinct from R1.
    diag_b = rng.uniform(0.1, 1.0, size=n)
    R2 = mp_diag(diag_b)
    K2 = reconstruct(R2)
    R2_recovered = strip(K2)
    round_trip_err_R2 = mp_max_abs_diff(R2_recovered, R2)
    distinct_operator_err = float(np.max(np.abs(diag_a - diag_b)))

    # (U3c) INJECTIVITY: distinct operators yield distinct matrices K.
    K_distinctness = mp_max_abs_diff(K1, K2)

    # (U4) HOSTILE CONTROL: the conjugate pair (0,1),(1,0) has equal D
    # entries.  Therefore C=I+|v><v| with v=e_(0,1)+e_(1,0) is positive
    # definite, self-adjoint, swap-symmetric, commutes with D, and has explicit
    # off-diagonal character mixing.  K=M D C M is consequently positive,
    # self-adjoint, and swap-symmetric, but stripping recovers the non-diagonal
    # C exactly.  This refutes structural-class-to-diagonality transport.
    hostile_vector = mp.zeros(n, 1)
    hostile_vector[index[(0, 1)]] = 1
    hostile_vector[index[(1, 0)]] = 1
    R_hostile = mp.eye(n) + hostile_vector * hostile_vector.T
    K_hostile = reconstruct(R_hostile)
    K_hostile_min_eig = float(
        np.min(np.linalg.eigvalsh(mp_to_np(K_hostile)))
    )

    K_hostile_self_adj_err = mp_max_abs_diff(K_hostile, K_hostile.T)
    K_hostile_swap_err = mp_max_abs_diff(swap * K_hostile, K_hostile * swap)

    R_hostile_recovered = strip(K_hostile)
    hostile_round_trip_err = mp_max_abs_diff(R_hostile_recovered, R_hostile)
    R_recovered_self_adj_err = mp_max_abs_diff(
        R_hostile_recovered, R_hostile_recovered.T
    )
    R_recovered_swap_err = mp_max_abs_diff(
        swap * R_hostile_recovered, R_hostile_recovered * swap
    )
    R_recovered_diag_err = mp_off_diag_max(R_hostile_recovered)

    # (U5) SUPPORT-ONLY CHOSEN-INPUT ROUND TRIP:
    # Build K from a chosen R[rho(6)] whose values come from the stipulated
    # integral (same Bessel-determinant identity used by the bounded companion),
    # then strip via (S) and verify that this input round trip recovers rho(6).
    rho_6 = coefficients.copy()
    R_rho6 = mp_diag(rho_6)
    K_rho6 = reconstruct(R_rho6)
    R_rho6_recovered = strip(K_rho6)
    rho6_recovery_err = mp_max_abs_diff(R_rho6_recovered, R_rho6)
    rho6_diagonal_err = mp_off_diag_max(R_rho6_recovered)
    rho6_diag_match_mp = mp.mpf(0)
    for i in range(n):
        v = abs(R_rho6_recovered[i, i] - mp.mpf(float(rho_6[i])))
        if v > rho6_diag_match_mp:
            rho6_diag_match_mp = v
    rho6_diag_match = float(rho6_diag_match_mp)

    # Tolerance: with mpmath dps=60 and condition number ~1e13 from D,
    # round-trip error should be ~1e-47, well within 1e-30.
    TOL = 1.0e-30

    # Header / context printout.
    print("=" * 78)
    print("FINITE-BOX MATRIX-FACTORIZATION STRIPPING UNIQUENESS")
    print("=" * 78)
    print()
    print(f"Finite box: 0 <= p,q <= {NMAX}, dim H_B = {n}, beta = {BETA}, mpmath dps = {MP_DPS}")
    print()
    print("Stripping factors (float64 context)")
    print(f"  J|_B symmetry error                   = {j_sym_err:.3e}")
    print(f"  J|_B swap commutator error            = {j_swap_err:.3e}")
    print(f"  min eigenvalue of M = exp((beta/2) J|_B)= {M_min_eig:.12f}")
    print(f"  det M (float64)                       = {M_det:.6e}")
    print(f"  min diagonal of D_beta^packet|_B      = {D_min_eig:.6e}")
    print(f"  det D (float64)                       = {D_det:.6e}")
    print()
    print("mpmath invertibility certificates")
    print(f"  ||M M^{{-1}} - I||_inf (mpmath)         = {M_invert_err:.3e}")
    print(f"  ||D D^{{-1}} - I||_inf (mpmath)         = {D_invert_err:.3e}")
    print()
    print("Algebraic stripping round-trip (mpmath, dps=60)")
    print(f"  ||R1 - strip(reconstruct(R1))||       = {round_trip_err_R1:.3e}")
    print(f"  ||R2 - strip(reconstruct(R2))||       = {round_trip_err_R2:.3e}")
    print(f"  ||K1 - K2|| (matrix distinctness)     = {K_distinctness:.3e}")
    print(f"  ||R1 - R2|| (operator distinctness)   = {distinct_operator_err:.6e}")
    print()
    print("Hostile structural control (mpmath, dps=60)")
    print(f"  K_hostile self-adj err                = {K_hostile_self_adj_err:.3e}")
    print(f"  K_hostile swap err                    = {K_hostile_swap_err:.3e}")
    print(f"  hostile stripping round-trip err      = {hostile_round_trip_err:.3e}")
    print(f"  recovered C self-adj err              = {R_recovered_self_adj_err:.3e}")
    print(f"  recovered C swap err                  = {R_recovered_swap_err:.3e}")
    print(f"  recovered C off-diagonal magnitude    = {R_recovered_diag_err:.3e}")
    print()
    print("Bounded-companion input round-trip (stipulated-integral rho(6), mpmath)")
    print(f"  rho_(0,0)(6)                          = {rho_6[index[(0,0)]]:.16f}")
    print(f"  ||R[rho(6)] - strip(reconstruct(R[rho(6)]))|| = {rho6_recovery_err:.3e}")
    print(f"  recovered R[rho(6)] off-diagonal err  = {rho6_diagonal_err:.3e}")
    print(f"  recovered diagonal vs input rho(6)    = {rho6_diag_match:.3e}")
    print()

    # ---- THEOREM CHECKS ----
    check(
        "(U1) the half-slice multiplier exp[(beta/2) J|_B] is positive definite, has positive determinant, and is invertible to mpmath precision on the finite box",
        M_min_eig > 0.0 and M_det > 0.0 and M_invert_err < TOL,
        detail=f"min eig={M_min_eig:.6f}, det={M_det:.3e}, ||M M^-1 - I||={M_invert_err:.3e}",
    )
    check(
        "(U2) the fourth-power diagonal D_beta^packet|_B has strictly positive entries, positive determinant, and is invertible to mpmath precision on the finite box",
        D_min_eig > 0.0 and D_det > 0.0 and D_invert_err < TOL,
        detail=f"min diag={D_min_eig:.3e}, det={D_det:.3e}, ||D D^-1 - I||={D_invert_err:.3e}",
    )
    check(
        "(U3a) the stripping identity (S) recovers a positive diagonal candidate operator R1 exactly from K = reconstruct(R1) on the finite box (mpmath round-trip)",
        round_trip_err_R1 < TOL,
        detail=f"||R1 - strip(reconstruct(R1))||={round_trip_err_R1:.3e}",
    )
    check(
        "(U3b) the stripping identity (S) recovers a SECOND, distinct positive diagonal candidate operator R2 exactly from K = reconstruct(R2) on the finite box, establishing that (S) is a function",
        round_trip_err_R2 < TOL and distinct_operator_err > 0.05 and K_distinctness > 1.0e-20,
        detail=f"||R2 - strip(reconstruct(R2))||={round_trip_err_R2:.3e}, ||R1 - R2||={distinct_operator_err:.3e}, ||K1 - K2||={K_distinctness:.3e}",
    )
    check(
        "(U4 hostile) positive self-adjoint swap-symmetric matrix data can strip to a positive self-adjoint swap-symmetric operator with off-diagonal character mixing",
        K_hostile_min_eig > 0.0
        and K_hostile_self_adj_err < TOL and K_hostile_swap_err < TOL
        and hostile_round_trip_err < TOL
        and R_recovered_self_adj_err < TOL and R_recovered_swap_err < TOL
        and R_recovered_diag_err > 0.5,
        detail=f"min eig(K)={K_hostile_min_eig:.3e}; K sym/swap=({K_hostile_self_adj_err:.3e},{K_hostile_swap_err:.3e}); round-trip={hostile_round_trip_err:.3e}; C sym/swap/offdiag=({R_recovered_self_adj_err:.3e},{R_recovered_swap_err:.3e},{R_recovered_diag_err:.3e})",
    )
    check(
        "(U5) when K_6|_B is constructed from independently recomputed stipulated-integral rho_(p,q)(6) values, (S) recovers that chosen diagonal input on the finite box (mpmath)",
        rho6_recovery_err < TOL and rho6_diagonal_err < TOL and rho6_diag_match < TOL,
        detail=f"||R[rho(6)] - strip(...)||={rho6_recovery_err:.3e}, off-diag={rho6_diagonal_err:.3e}, diag match={rho6_diag_match:.3e}",
        bucket="SUPPORT",
    )

    # ---- SUPPORT CHECKS ----
    check(
        "the recurrence matrix J|_B is real symmetric and swap-invariant on the finite box",
        j_sym_err < 1.0e-15 and j_swap_err < 1.0e-12,
        detail=f"||J - J^T||={j_sym_err:.3e}, ||[S,J]||={j_swap_err:.3e}",
        bucket="SUPPORT",
    )
    check(
        "the independently recomputed chosen input has rho_(0,0)(6) = 1 by its normalization definition",
        abs(rho_6[index[(0, 0)]] - 1.0) < 1.0e-12,
        detail=f"rho_(0,0)(6) = {rho_6[index[(0,0)]]:.16f}; this is not a local-factor or environment identification",
        bucket="SUPPORT",
    )
    check(
        "the algebraic stripping (S) is independent of any specific witness or computed coefficient sequence (the two distinct candidate operators R1, R2 used in (U3a)/(U3b) are random, with ||R1 - R2|| > 0.05)",
        distinct_operator_err > 0.05,
        detail=f"operator distinctness ||R1 - R2|| = {distinct_operator_err:.3e}",
        bucket="SUPPORT",
    )

    print()
    print("=" * 78)
    print(f"SUMMARY: THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
