#!/usr/bin/env python3
"""Finite supplied Cl4 module and arithmetic diagnostics; physical bridges open.
Authority note: docs/HUBBLE_LANE5_C1_CL4C_CONDITIONAL_DERIVATION_CHAIN_CONSTRUCTION_NOTE_2026-04-30.md
Checks verify algebra and supplied numbers, not absolute-scale or Hubble closure.
"""

from __future__ import annotations

import cmath
import math
import sys
from itertools import product

import numpy as np


PASS_COUNT = 0
FAIL_COUNT = 0
TOL = 1.0e-12


def check(name: str, passed: bool, detail: str) -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if passed else "FAIL"
    if passed:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"[{status}] {name}: {detail}")
    return passed


# ----------------------------------------------------------------------------
# Pauli infrastructure
# ----------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)
X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
Y = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
Z = np.diag([1.0, -1.0]).astype(complex)


def kron(*mats: np.ndarray) -> np.ndarray:
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


def anticomm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b + b @ a


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def is_close(a: np.ndarray, b: np.ndarray, tol: float = TOL) -> bool:
    return float(np.linalg.norm(a - b)) < tol


def is_hermitian(a: np.ndarray, tol: float = TOL) -> bool:
    return float(np.linalg.norm(a - a.conj().T)) < tol


def is_unitary(a: np.ndarray, tol: float = TOL) -> bool:
    n = a.shape[0]
    return float(np.linalg.norm(a @ a.conj().T - np.eye(n, dtype=complex))) < tol


# ----------------------------------------------------------------------------
# H_cell, P_A, Hamming-weight-1 basis
# ----------------------------------------------------------------------------
def hamming_weight(idx: int) -> int:
    return int(bin(idx).count("1"))


def build_p_a() -> tuple[np.ndarray, list[int]]:
    """Return P_A projector on H_cell ~= C^16 and the Hamming-weight-1 indices."""
    n_modes = 4
    dim = 2**n_modes
    indices = [i for i in range(dim) if hamming_weight(i) == 1]
    p_a = np.zeros((dim, dim), dtype=complex)
    for i in indices:
        p_a[i, i] = 1.0
    return p_a, indices


def restrict(matrix: np.ndarray, indices: list[int]) -> np.ndarray:
    return matrix[np.ix_(indices, indices)]


# ----------------------------------------------------------------------------
# Arrow 1: explicit Pauli construction of the Cl_4 coframe response on K
# ----------------------------------------------------------------------------
def coframe_generators() -> list[np.ndarray]:
    """Return [Gamma_t, Gamma_n, Gamma_tau1, Gamma_tau2] on K = C^4."""
    return [
        kron(X, I2),
        kron(Y, I2),
        kron(Z, X),
        kron(Z, Y),
    ]


def coframe_response(coeffs: list[complex], gammas: list[np.ndarray]) -> np.ndarray:
    out = np.zeros_like(gammas[0])
    for c, g in zip(coeffs, gammas, strict=True):
        out = out + c * g
    return out


# ----------------------------------------------------------------------------
# Hamming-weight-1 basis bijection to K = C^4
# ----------------------------------------------------------------------------
def hw1_to_k_isometry(p_a_indices: list[int]) -> np.ndarray:
    """Isometry V: K -> P_A H_cell mapping (|t>, |n>, |tau1>, |tau2>) on K to the
    Hamming-weight-1 basis vectors of H_cell (in index order |1000>, |0100>,
    |0010>, |0001>)."""
    dim_cell = 16
    v = np.zeros((dim_cell, 4), dtype=complex)
    for col, idx in enumerate(p_a_indices):
        v[idx, col] = 1.0
    return v


# ----------------------------------------------------------------------------
# Section runner
# ----------------------------------------------------------------------------
def section(title: str) -> None:
    print()
    print("-" * 72)
    print(title)
    print("-" * 72)


def run_arrow_1_checks() -> None:
    section("Arrow 1: Cl_4(C) -> metric-compatible coframe response on P_A H_cell")

    # Check 1: rank(P_A) = 4 and c_cell = 1/4.
    p_a, p_a_indices = build_p_a()
    rank = int(round(float(np.trace(p_a).real)))
    c_cell = rank / 16
    check(
        "1_rank_P_A_equals_four_and_c_cell_one_quarter",
        rank == 4 and math.isclose(c_cell, 0.25, abs_tol=1.0e-15),
        f"rank(P_A)={rank}, c_cell={c_cell:.12f}, indices={p_a_indices}",
    )

    # Check 2: Pauli generators are Hermitian and unitary.
    gammas = coframe_generators()
    all_hermitian = all(is_hermitian(g) for g in gammas)
    all_unitary = all(is_unitary(g) for g in gammas)
    check(
        "2_pauli_generators_hermitian_and_unitary",
        all_hermitian and all_unitary,
        f"all Hermitian={all_hermitian}, all unitary={all_unitary}",
    )

    # Check 3: Cl_4 anticommutator algebra exact.
    worst = 0.0
    for i, gi in enumerate(gammas):
        for j, gj in enumerate(gammas):
            target = (2.0 if i == j else 0.0) * np.eye(4, dtype=complex)
            worst = max(worst, float(np.linalg.norm(anticomm(gi, gj) - target)))
    check(
        "3_cl4_anticommutator_algebra_exact",
        worst < TOL,
        f"worst residual={worst:.3e}",
    )

    # Check 4: Linear coframe response D(v)^2 = ||v||^2 I on a sweep of
    # primitive coframe vectors.
    rng = np.random.default_rng(seed=20260430)
    worst_metric = 0.0
    for _ in range(64):
        coeffs = rng.standard_normal(4) + 1j * rng.standard_normal(4)
        # Restrict to real coefficients for the metric-compatibility test (the
        # primitive coframe is a real vector space).
        coeffs = coeffs.real.astype(complex)
        norm_sq = float(np.sum(coeffs.real**2))
        d_v = coframe_response(list(coeffs), gammas)
        target = norm_sq * np.eye(4, dtype=complex)
        worst_metric = max(worst_metric, float(np.linalg.norm(d_v @ d_v - target)))
    check(
        "4_linear_coframe_response_metric_compatible",
        worst_metric < 1.0e-9,
        f"worst D(v)^2 residual on 64 random real coframe vectors={worst_metric:.3e}",
    )

    # Check 5: Basis-label permutation — face permutation (x <-> y) lifts to a
    # unitary U_swap conjugating the Cl_4 presentation into a unitarily
    # equivalent Cl_4 presentation.
    # Build a face permutation as a unitary on K that swaps the second and
    # third basis labels (interpreted as swapping n <-> tau_1 in this
    # face-pair / tangent-pair embedding).
    swap_23 = np.eye(4, dtype=complex)
    swap_23[[1, 2], :] = swap_23[[2, 1], :]
    swapped_gammas = [swap_23 @ g @ swap_23.conj().T for g in gammas]
    swap_clifford_residual = 0.0
    for i, gi in enumerate(swapped_gammas):
        for j, gj in enumerate(swapped_gammas):
            target = (2.0 if i == j else 0.0) * np.eye(4, dtype=complex)
            swap_clifford_residual = max(
                swap_clifford_residual,
                float(np.linalg.norm(anticomm(gi, gj) - target)),
            )
    swap_changes_basis = max(
        float(np.linalg.norm(a - b)) for a, b in zip(gammas, swapped_gammas, strict=True)
    )
    check(
        "5_face_permutation_gauge_unitary_equivalence",
        swap_clifford_residual < TOL and swap_changes_basis > 0.5,
        (
            f"swapped Cl_4 residual={swap_clifford_residual:.3e}, "
            f"basis change norm={swap_changes_basis:.3e}"
        ),
    )

    # Check 6: Active-basis U(1) phase gauge — diag(1, e^{i theta}, 1, 1)
    # conjugates the Cl_4 presentation without changing its algebra.
    phase_unitary = np.diag([1.0, np.exp(0.37j), 1.0, 1.0]).astype(complex)
    phase_gammas = [phase_unitary @ g @ phase_unitary.conj().T for g in gammas]
    phase_clifford_residual = 0.0
    for i, gi in enumerate(phase_gammas):
        for j, gj in enumerate(phase_gammas):
            target = (2.0 if i == j else 0.0) * np.eye(4, dtype=complex)
            phase_clifford_residual = max(
                phase_clifford_residual,
                float(np.linalg.norm(anticomm(gi, gj) - target)),
            )
    phase_changes_basis = max(
        float(np.linalg.norm(a - b)) for a, b in zip(gammas, phase_gammas, strict=True)
    )
    check(
        "6_active_basis_phase_gauge_preserves_clifford_algebra",
        phase_clifford_residual < TOL and phase_changes_basis > 0.05,
        (
            f"phase-rotated Cl_4 residual={phase_clifford_residual:.3e}, "
            f"basis change norm={phase_changes_basis:.3e}"
        ),
    )

    # Check 7: CAR pairing — c_N, c_T satisfy two-mode CAR.
    g_t, g_n, g_tau1, g_tau2 = gammas
    c_N = (g_t + 1j * g_n) / 2.0
    c_T = (g_tau1 + 1j * g_tau2) / 2.0
    car_pairs = [(c_N, c_T)]
    car_worst = 0.0
    # {c_i, c_j} = 0 for all i,j (including i=j giving c^2 = 0).
    for ci in (c_N, c_T):
        for cj in (c_N, c_T):
            car_worst = max(car_worst, float(np.linalg.norm(anticomm(ci, cj))))
    # {c_i, c_j^dagger} = delta_ij I_K.
    for i, ci in enumerate((c_N, c_T)):
        for j, cj in enumerate((c_N, c_T)):
            target = (1.0 if i == j else 0.0) * np.eye(4, dtype=complex)
            car_worst = max(
                car_worst,
                float(np.linalg.norm(anticomm(ci, cj.conj().T) - target)),
            )
    check(
        "7_two_mode_CAR_pairing_exact",
        car_worst < 1.0e-10,
        f"worst CAR residual={car_worst:.3e}",
    )

    # Check 8: K ~= F(C^2). Construct the two-mode Fock vacuum |0_N 0_T> as
    # the simultaneous null vector of c_N, c_T and verify it has exactly one
    # such common kernel direction; (c_N^dagger, c_T^dagger) generate the
    # remaining three Fock basis vectors.
    null_N = c_N
    null_T = c_T
    annihilation_kernel = np.linalg.svd(np.vstack([null_N, null_T]), compute_uv=False)
    smallest = float(annihilation_kernel[-1])
    second_smallest = float(annihilation_kernel[-2])
    check(
        "8_K_isomorphic_to_F_C_squared_unique_fock_vacuum",
        smallest < 1.0e-10 and second_smallest > 0.5,
        (
            f"smallest singular value of [c_N; c_T]={smallest:.3e} (vacuum), "
            f"second smallest={second_smallest:.3e} (no second vacuum)"
        ),
    )


def run_arrow_2_checks() -> None:
    section("Spin-lift identities and supplied action-unit comparison")

    gammas = coframe_generators()
    g_t, g_n, g_tau1, g_tau2 = gammas

    # Spin-lift U(theta)=exp(theta*Gamma_t*Gamma_n/2), without an extra i.
    bivector = g_t @ g_n  # (Gamma_t Gamma_n) is anti-Hermitian; squares to -I.
    # Exponentiate: U(theta) = exp(theta/2 * bivector) implements rotation by
    # theta in the (t,n) plane on vectors. theta = 2*pi -> U = -I_K.
    eigvals_bivector = np.linalg.eigvals(bivector)
    bivector_squared_to_minus_I = is_close(bivector @ bivector, -np.eye(4, dtype=complex))
    # Eigenvalues of bivector are +i, -i (each with multiplicity 2).
    # exp((2 pi / 2) * bivector) = exp(pi * bivector) = cos(pi) I + sin(pi) bivector ... no, this is matrix exp.
    # Cleanly: since bivector^2 = -I, exp(t * bivector) = cos(t) I + sin(t) bivector.
    u_2pi = math.cos(math.pi) * np.eye(4, dtype=complex) + math.sin(math.pi) * bivector
    u_4pi = math.cos(2 * math.pi) * np.eye(4, dtype=complex) + math.sin(2 * math.pi) * bivector
    spin_2pi_is_minus_I = is_close(u_2pi, -np.eye(4, dtype=complex), tol=1.0e-10)
    spin_4pi_is_plus_I = is_close(u_4pi, np.eye(4, dtype=complex), tol=1.0e-10)
    check(
        "9_spin_lift_periodicity_4pi_angle",
        bivector_squared_to_minus_I and spin_2pi_is_minus_I and spin_4pi_is_plus_I,
        (
            f"bivector^2=-I: {bivector_squared_to_minus_I}, "
            f"U(2pi)=-I: {spin_2pi_is_minus_I}, U(4pi)=+I: {spin_4pi_is_plus_I}, "
            f"eigvals(bivector)={np.sort_complex(eigvals_bivector)}"
        ),
    )

    # Check 10: Action-unit invariance witness (A2 boundary). (S, kappa) ->
    # (lambda S, lambda kappa) leaves exp(i S/kappa) invariant.
    s_dim = 0.25 + 0.37
    base_phase = cmath.exp(1j * s_dim / 1.0)
    worst_spread = 0.0
    for lam in (0.5, 1.0, 2.0, 8.0):
        scaled_phase = cmath.exp(1j * (lam * s_dim) / (lam * 1.0))
        worst_spread = max(worst_spread, abs(scaled_phase - base_phase))
    check(
        "10_action_unit_rescaling_invariance_A2_boundary_witnessed",
        worst_spread < TOL,
        f"worst (S,kappa) common-rescale phase spread={worst_spread:.3e}",
    )

    # Check 11: Spinor angular period is 4*pi (full spinor period).
    full_period = 4 * math.pi
    u_full = math.cos(full_period / 2) * np.eye(4, dtype=complex) + math.sin(full_period / 2) * bivector
    check(
        "11_spinor_angular_period_4pi",
        is_close(u_full, np.eye(4, dtype=complex), tol=1.0e-9),
        f"||U(4pi) - I|| = {float(np.linalg.norm(u_full - np.eye(4, dtype=complex))):.3e}",
    )


def run_arrow_3_checks() -> None:
    section("Supplied crossing counts and unit arithmetic; physical bridge open")

    # Supplied arithmetic only. Neither the crossings nor a continuum entropy
    # coefficient follows from the finite CAR representation.
    n_normal = 2  # supplied normal count
    half_zone_measure = 0.5  # supplied half-zone measure
    n_tangent = 2 * half_zone_measure  # supplied tangent contribution
    n_x = n_normal + n_tangent
    c_widom = n_x / 12.0
    check(
        "12_supplied_crossing_arithmetic_one_quarter",
        math.isclose(c_widom, 0.25, abs_tol=TOL) and math.isclose(n_x, 3.0, abs_tol=TOL),
        f"<N_x>={n_x}, c_Widom={c_widom:.12f}",
    )

    # Check 13: c_Widom = c_cell = 1/4.
    c_cell = 4.0 / 16.0
    check(
        "13_c_widom_matches_c_cell",
        math.isclose(c_widom, c_cell, abs_tol=TOL),
        f"c_Widom={c_widom:.12f}, c_cell={c_cell:.12f}",
    )

    # Check 14: lambda = 4 c_cell = 1, G_Newton,lat = 4*pi * G_kernel = 1.
    g_kernel = 1.0 / (4 * math.pi)  # bare Green-kernel coefficient
    lam = 4 * c_cell
    g_newton_lat = (4 * math.pi) * g_kernel
    check(
        "14_supplied_kernel_normalization_one",
        math.isclose(lam, 1.0, abs_tol=TOL) and math.isclose(g_newton_lat, 1.0, abs_tol=TOL),
        f"lambda={lam:.12f}, G_Newton,lat={g_newton_lat:.12f}",
    )

    # Check 15: a / l_P = 1 in lattice-natural units.
    a_lat = 1.0
    hbar_nat = 1.0
    c_speed_nat = 1.0
    g_nat = g_newton_lat
    l_p_sq = hbar_nat * g_nat / (c_speed_nat**3)
    l_p = math.sqrt(l_p_sq)
    ratio = a_lat / l_p
    check(
        "15_supplied_units_ratio_one",
        math.isclose(ratio, 1.0, abs_tol=TOL),
        f"l_P={l_p:.12f}, a/l_P={ratio:.12f}",
    )


def run_arrow_4_checks() -> None:
    section("Supplied auxiliary-factor commutation; no physical orthogonality proof")

    gammas = coframe_generators()

    # Supplied auxiliary complex factor; this is not a physical derivation
    # of the C2 projector, real carrier or cosmological independence.
    aux_dim = 2  # supplied complex dimension
    p_c2 = np.diag([1.0, 0.0]).astype(complex)  # rank-1 projector on aux factor
    worst_comm = 0.0
    for g in gammas:
        op_carrier = kron(g, np.eye(aux_dim, dtype=complex))
        op_yukawa = kron(np.eye(4, dtype=complex), p_c2)
        worst_comm = max(worst_comm, float(np.linalg.norm(comm(op_carrier, op_yukawa))))
    check(
        "16_Cl4_carrier_commutes_with_C2_yukawa_projector_on_orthogonal_factor",
        worst_comm < TOL,
        f"worst [Gamma_a tensor I, I tensor P_C2] norm={worst_comm:.3e}",
    )

    # Check 17: K and the Yukawa-side dW_e^H algebra act on disjoint
    # tensor-factor subsystems. We verify this by showing that the carrier
    # algebra (any element of M_4(C) acting on K factor) and the Yukawa
    # algebra (any element of M_2(C) acting on aux factor) commute.
    rng = np.random.default_rng(seed=20260430)
    worst_alg = 0.0
    for _ in range(8):
        a_carrier = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
        b_yukawa = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
        op_a = kron(a_carrier, np.eye(2, dtype=complex))
        op_b = kron(np.eye(4, dtype=complex), b_yukawa)
        worst_alg = max(worst_alg, float(np.linalg.norm(comm(op_a, op_b))))
    check(
        "17_carrier_and_yukawa_algebras_act_on_disjoint_factors",
        worst_alg < 1.0e-9,
        f"worst commutator across disjoint factors={worst_alg:.3e}",
    )

    # Invariance under transformations on the other supplied tensor factor.
    # No physical Schur-projection or source selection law is derived.
    schur_probe = kron(np.eye(4, dtype=complex), p_c2)
    worst_invariance = 0.0
    for g in gammas:
        carrier_unitary = np.cos(0.5) * np.eye(8, dtype=complex) + 1j * np.sin(0.5) * kron(g, np.eye(2, dtype=complex))
        transformed = carrier_unitary @ schur_probe @ carrier_unitary.conj().T
        worst_invariance = max(worst_invariance, float(np.linalg.norm(transformed - schur_probe)))
    check(
        "18_supplied_tensor_factor_invariance",
        worst_invariance < 1.0e-9,
        (
            f"worst ||U_carrier P_C2 U_carrier^dagger - P_C2|| under Cl_4 carrier "
            f"transformations={worst_invariance:.3e}"
        ),
    )


def run_forbidden_import_guard() -> None:
    section("Forbidden-import guard")

    forbidden = {
        "H_0_obs": "observed Hubble constant",
        "H_inf_obs": "observed late-time de Sitter rate",
        "Lambda_obs": "observed cosmological constant",
        "M_Pl_SI": "SI Planck mass",
        "hbar_SI": "SI reduced Planck constant",
        "G_SI": "SI Newton constant",
    }
    source_path = __file__
    with open(source_path, "r", encoding="utf-8") as fh:
        text = fh.read()
    # Strip comments and docstrings to be safe — we only forbid these names
    # appearing as proof-input variables, not as annotation strings.
    # Conservative check: forbid the literal token usage as an assignment.
    for name, desc in forbidden.items():
        present_as_assignment = (
            f"{name} =" in text or f"{name}=" in text or f"{name} = " in text
        )
        check(
            f"forbidden_import_not_used_as_proof_input::{name}",
            not present_as_assignment,
            f"{desc}: not used as proof input",
        )


def main() -> int:
    print("=" * 72)
    print("Lane 5 (C1) Cl_4(C)-conditional derivation chain construction runner")
    print("=" * 72)

    run_arrow_1_checks()
    run_arrow_2_checks()
    run_arrow_3_checks()
    run_arrow_4_checks()
    run_forbidden_import_guard()

    # Counterexamples to extending real metric and spatial-rotation claims.
    d_imag = coframe_response([1j, 0, 0, 0], coframe_generators())
    check("complex_bilinear_not_hermitian_norm",
          is_close(d_imag @ d_imag, -np.eye(4)) and not is_close(d_imag @ d_imag, np.eye(4)),
          "v=i e1 has bilinear square -1 and Hermitian norm squared +1")
    odd_swap = np.array([[0,1,0],[1,0,0],[0,0,1]])
    check("odd_spatial_permutation_not_rotation", np.linalg.det(odd_swap) == -1,
          "odd swap lies in O(3), not SO(3)")


    print()
    print("=" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("=" * 72)
    if FAIL_COUNT == 0:
        print("Conclusion: finite identities and supplied arithmetic passed.")
        print("Physical crossing, action, Newton-coupling and absolute-scale bridges remain open.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
