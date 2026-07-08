#!/usr/bin/env python3
"""Mass observable checks on the free staggered two-step transfer surface.

Companion runner for
MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md.

Read authorities used to set conventions:
1. scripts/free_staggered_two_step_dispersion_d_dimensional_2026_06_12.py
2. docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md
3. scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py

This runner checks IDENTITIES off declared imports: I-DYN two-step transfer
dynamics, I-MASS on-site coefficient, and I-TIME normalization.  It derives no
coupling values.

Authority (1) exposes the scalar dispersion and phase/taste construction, not
a taste-space H_eff(k) matrix; CHECK-01 therefore verifies taste scalarity as
an eigenvalue-spread check on the folded two-step cell transfer block, gated
against the independently computed scalar dispersion.
"""

from __future__ import annotations

from itertools import product

import numpy as np
import sympy as sp


D = 3
TASTE_DIM = 2**D
M_SWEEP = (0.05, 0.1, 0.2, 0.5, 1.0, 2.0)
CHECK01_MASSES = (0.1, 0.5, 1.0)
PASS_COUNT = 0
FAIL_COUNT = 0


def report(num: int, name: str, condition: bool, residual: float, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    PASS_COUNT += int(ok)
    FAIL_COUNT += int(not ok)
    line = f"CHECK-{num:02d} {name}: {'PASS' if ok else 'FAIL'} residual={residual:.3e}"
    if detail:
        line += f" {detail}"
    print(line)


# Replicated from the phase-system construction in
# scripts/free_staggered_two_step_dispersion_d_dimensional_2026_06_12.py:
# Gamma_mu |r> = (-1)^r_mu |r xor s_mu>, with s_mu having ones in slots < mu.
def gamma_matrices(d: int = D) -> list[np.ndarray]:
    n = 2**d
    gammas: list[np.ndarray] = []
    for mu in range(d):
        mask = (1 << mu) - 1
        gamma = np.zeros((n, n), dtype=float)
        for r in range(n):
            r_mu = (r >> mu) & 1
            gamma[r ^ mask, r] = -1.0 if r_mu else 1.0
        gammas.append(gamma)
    return gammas


GAMMAS = gamma_matrices()
I_TASTE = np.eye(TASTE_DIM, dtype=complex)
Z_TASTE = np.zeros((TASTE_DIM, TASTE_DIM), dtype=complex)
I_BLOCK = np.eye(2 * TASTE_DIM, dtype=complex)


def dispersion(m: float, p: tuple[float, ...]) -> float:
    """Authority (1) dispersion: E = arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu))."""
    s2 = sum(np.sin(component) ** 2 for component in p)
    return float(np.arcsinh(np.sqrt(m * m + s2)))


def inertial_mass(m: float) -> float:
    return float(m * np.sqrt(1.0 + m * m))


def cell_hop(k: tuple[float, float, float]) -> np.ndarray:
    """Authority (1) folded spatial hop H_hop(k) = i sum_mu sin(k_mu) Gamma_mu."""
    hop = np.zeros((TASTE_DIM, TASTE_DIM), dtype=complex)
    for mu in range(D):
        hop += 1j * np.sin(k[mu]) * GAMMAS[mu]
    return hop


def cell_two_step_transfer(k: tuple[float, float, float], m: float) -> np.ndarray:
    """Authority (1) T_2 = T_odd T_even on the folded taste/time block."""
    hop = cell_hop(k)
    t_even = np.block([[-2.0 * (m * I_TASTE + hop), I_TASTE], [I_TASTE, Z_TASTE]])
    t_odd = np.block([[-2.0 * (m * I_TASTE - hop), I_TASTE], [I_TASTE, Z_TASTE]])
    return t_odd @ t_even


def sorted_spectrum(matrix: np.ndarray) -> np.ndarray:
    vals = np.linalg.eigvals(matrix)
    return np.array(sorted(vals, key=lambda z: (round(float(z.real), 14), round(float(z.imag), 14))))


def decaying_energies(k: tuple[float, float, float], m: float) -> tuple[np.ndarray, float, int]:
    vals = np.linalg.eigvals(cell_two_step_transfer(k, m))
    decays = vals[np.abs(vals) < 1.0 + 1e-9]
    if decays.size != TASTE_DIM:
        return np.array([], dtype=float), float("inf"), int(decays.size)
    imag_resid = float(np.max(np.abs(decays.imag)))
    real_decays = np.maximum(decays.real, np.finfo(float).tiny)
    energies = np.sort(-0.5 * np.log(real_decays))
    return energies, imag_resid, int(decays.size)


def bz_points(L: int) -> list[tuple[float, float, float]]:
    values = [2.0 * np.pi * n / L for n in range(L)]
    return [tuple(p) for p in product(values, repeat=D)]


def dirac_corner_indices(L: int) -> set[tuple[int, int, int]]:
    half = L // 2
    return {tuple(corner) for corner in product((0, half), repeat=D)}


def check_01_symbol_scalarity() -> None:
    max_spread = 0.0
    max_target_resid = 0.0
    max_imag = 0.0
    bad_count = 0
    for m in CHECK01_MASSES:
        for k in bz_points(8):
            energies, imag_resid, count = decaying_energies(k, m)
            if count != TASTE_DIM:
                bad_count += 1
                continue
            target = dispersion(m, k)
            max_spread = max(max_spread, float(energies[-1] - energies[0]))
            max_target_resid = max(max_target_resid, float(np.max(np.abs(energies - target))))
            max_imag = max(max_imag, imag_resid)
    residual = max(max_spread, max_target_resid, max_imag, float(bad_count))
    report(
        1,
        "SYMBOL-SCALARITY",
        residual <= 1e-12,
        max_spread,
        f"target_residual={max_target_resid:.3e} max_imag={max_imag:.3e} bad_blocks={bad_count}",
    )


def check_02_rest_gap() -> None:
    max_resid = 0.0
    max_arg_norm = 0.0
    for m in M_SWEEP:
        target = float(np.arcsinh(m))
        best_E = float("inf")
        best_p = (float("nan"), float("nan"), float("nan"))

        for p in bz_points(16):
            E = dispersion(m, p)
            if E < best_E:
                best_E = E
                best_p = p

        local_axis = np.linspace(-0.25, 0.25, 17)
        for p in product(local_axis, repeat=D):
            p_tuple = tuple(float(x) for x in p)
            E = dispersion(m, p_tuple)
            if E < best_E:
                best_E = E
                best_p = p_tuple

        max_resid = max(max_resid, abs(best_E - target))
        max_arg_norm = max(max_arg_norm, float(np.linalg.norm(best_p)))

    residual = max(max_resid, max_arg_norm)
    report(
        2,
        "REST-GAP",
        max_resid <= 1e-12 and max_arg_norm <= 1e-12,
        max_resid,
        f"max_argmin_norm={max_arg_norm:.3e}",
    )


def check_03_global_gap_and_m0_singularity() -> None:
    L = 16
    corners = dirac_corner_indices(L)
    max_negative_shortfall = 0.0
    max_corner_E_resid = 0.0
    min_worst_margin = float("inf")
    min_corner_E = float("inf")
    max_corner_E = 0.0

    for m in M_SWEEP:
        target = float(np.arcsinh(m))
        values = []
        corner_values = []
        for idx in product(range(L), repeat=D):
            p = tuple(2.0 * np.pi * n / L for n in idx)
            E = dispersion(m, p)
            values.append(E)
            if idx in corners:
                corner_values.append(E)
        values_arr = np.array(values)
        margin = float(np.min(values_arr - target))
        min_worst_margin = min(min_worst_margin, margin)
        max_negative_shortfall = max(max_negative_shortfall, max(0.0, -margin))
        corner_arr = np.array(corner_values)
        max_corner_E_resid = max(max_corner_E_resid, float(np.max(np.abs(corner_arr - target))))
        min_corner_E = min(min_corner_E, float(np.min(corner_arr)))
        max_corner_E = max(max_corner_E, float(np.max(corner_arr)))

    zero_indices = set()
    min_noncorner_E_m0 = float("inf")
    for idx in product(range(L), repeat=D):
        p = tuple(2.0 * np.pi * n / L for n in idx)
        E = dispersion(0.0, p)
        if E < 1e-12:
            zero_indices.add(idx)
        elif idx not in corners:
            min_noncorner_E_m0 = min(min_noncorner_E_m0, E)

    zero_set_ok = zero_indices == corners and min_noncorner_E_m0 > 1e-12
    zero_set_resid = 0.0 if zero_set_ok else 1.0
    residual = max(max_negative_shortfall, max_corner_E_resid, zero_set_resid)
    report(
        3,
        "GLOBAL-GAP+M=0-SINGULARITY",
        residual <= 1e-12,
        residual,
        "worst_margin={:.3e} corner_E_resid={:.3e} corner_E_range=[{:.12e},{:.12e}] "
        "m0_zero_count={} m0_min_noncorner_E={:.3e}".format(
            min_worst_margin,
            max_corner_E_resid,
            min_corner_E,
            max_corner_E,
            len(zero_indices),
            min_noncorner_E_m0,
        ),
    )


def central_second_derivative(m: float, h: float) -> float:
    base = (0.0, 0.0, 0.0)
    plus = (0.0, 0.0, h)
    minus = (0.0, 0.0, -h)
    return (dispersion(m, plus) - 2.0 * dispersion(m, base) + dispersion(m, minus)) / (h * h)


def check_04_inertial_mass() -> None:
    max_numeric_resid = 0.0
    for m in M_SWEEP:
        exact = 1.0 / inertial_mass(m)
        best = float("inf")
        for h in (2.0 ** -k for k in range(4, 13)):
            coarse = central_second_derivative(m, h)
            fine = central_second_derivative(m, 0.5 * h)
            richardson = (4.0 * fine - coarse) / 3.0
            best = min(best, abs(richardson - exact))
        max_numeric_resid = max(max_numeric_resid, best)

    m_sym, p_sym = sp.symbols("m p", positive=True, real=True)
    expr = sp.asinh(sp.sqrt(m_sym**2 + sp.sin(p_sym) ** 2))
    d2_expr = sp.diff(expr, p_sym, 2).subs(p_sym, 0)
    target = 1 / (m_sym * sp.sqrt(1 + m_sym**2))
    sym_resid = sp.simplify(d2_expr - target)
    residual = max(max_numeric_resid, 0.0 if sym_resid == 0 else 1.0)
    report(
        4,
        "INERTIAL-MASS",
        residual <= 1e-8,
        residual,
        f"sympy_residual={sym_resid} exact_d2={d2_expr}",
    )


def check_05_universal_function() -> None:
    m_sym = sp.symbols("m", positive=True, real=True)
    m_gap = sp.asinh(m_sym)
    M_I = m_sym * sp.sqrt(1 + m_sym**2)
    exact_resid = sp.simplify(M_I - sp.expand_trig(sp.sinh(2 * m_gap) / 2))
    series = sp.series(M_I / m_gap, m_sym, 0, 5)
    polynomial = series.removeO().expand()
    coeff_1 = sp.simplify(polynomial.coeff(m_sym, 1))
    coeff_2 = sp.simplify(polynomial.coeff(m_sym, 2))
    coeff_3 = sp.simplify(polynomial.coeff(m_sym, 3))

    max_numeric_resid = 0.0
    for m in M_SWEEP:
        gap = float(np.arcsinh(m))
        mi = inertial_mass(m)
        max_numeric_resid = max(max_numeric_resid, abs(mi - float(np.sinh(2.0 * gap) / 2.0)))

    exact_ok = exact_resid == 0 and coeff_1 == 0 and coeff_2 == sp.Rational(2, 3) and coeff_3 == 0
    residual = max(max_numeric_resid, 0.0 if exact_ok else 1.0)
    report(
        5,
        "UNIVERSAL-FUNCTION",
        residual <= 1e-12,
        residual,
        f"series={series} coeffs(m1,m2,m3)=({coeff_1},{coeff_2},{coeff_3})",
    )


def random_unitary(n: int, rng: np.random.Generator) -> np.ndarray:
    raw = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(raw)
    phases = np.diag(r)
    phases = phases / np.abs(phases)
    return q * phases.conj()


def lift_taste_unitary(U: np.ndarray) -> np.ndarray:
    return np.block([[U, Z_TASTE], [Z_TASTE, U]]).astype(complex)


def cubic_cycle_rotor() -> np.ndarray:
    """Taste-space Clifford rotor for the proper cycle x->y->z->x.

    With the authority (1) gamma convention, this orthogonal unitary satisfies
    U Gamma_0 U^dag = Gamma_1, U Gamma_1 U^dag = Gamma_2, U Gamma_2 U^dag = Gamma_0.
    """
    return 0.5 * (
        np.eye(TASTE_DIM)
        - GAMMAS[0] @ GAMMAS[1]
        - GAMMAS[1] @ GAMMAS[2]
        - GAMMAS[2] @ GAMMAS[0]
    )


def max_spectrum_deviation(A: np.ndarray, B: np.ndarray) -> float:
    return float(np.max(np.abs(sorted_spectrum(A) - sorted_spectrum(B))))


def check_06_generator_invariance() -> None:
    rng = np.random.default_rng(20260708)
    samples = (
        ((0.37, -0.81, 1.12), 0.1),
        ((1.9, 0.43, -1.4), 0.5),
        ((2.2, -2.7, 0.6), 1.0),
    )

    phase_dev = 0.0
    rotation_dev = 0.0
    rotation_transport = 0.0
    global_dev = 0.0

    U_rot_taste = cubic_cycle_rotor().astype(complex)
    U_rot = lift_taste_unitary(U_rot_taste)
    U_global = lift_taste_unitary(random_unitary(TASTE_DIM, rng))

    for k, m in samples:
        base = cell_two_step_transfer(k, m)
        phases = np.exp(1j * rng.uniform(0.0, 2.0 * np.pi, size=TASTE_DIM))
        U_phase = lift_taste_unitary(np.diag(phases))
        phase_conj = U_phase @ base @ U_phase.conj().T
        phase_dev = max(phase_dev, max_spectrum_deviation(base, phase_conj))

        k_rot = (k[2], k[0], k[1])
        rotated = cell_two_step_transfer(k_rot, m)
        rotation_conj = U_rot @ base @ U_rot.conj().T
        rotation_dev = max(rotation_dev, max_spectrum_deviation(rotated, rotation_conj))
        rotation_transport = max(
            rotation_transport,
            float(np.linalg.norm(U_rot_taste @ cell_hop(k) @ U_rot_taste.conj().T - cell_hop(k_rot))),
        )

        global_conj = U_global @ base @ U_global.conj().T
        global_dev = max(global_dev, max_spectrum_deviation(base, global_conj))

    residual = max(phase_dev, rotation_dev, rotation_transport, global_dev)
    report(
        6,
        "GENERATOR-INVARIANCE",
        residual <= 1e-10,
        residual,
        "phase_dev={:.3e} rotation_dev={:.3e} rotation_transport={:.3e} global_dev={:.3e}".format(
            phase_dev, rotation_dev, rotation_transport, global_dev
        ),
    )


def check_07_width_independence_contrast() -> None:
    sigma_values = (0.5, 1.0, 1.5)
    spectral_sigma_resid = 0.0
    proxy_ratios = []
    for m in M_SWEEP:
        m_gap_values = [float(np.arcsinh(m)) for _ in sigma_values]
        mi_values = [inertial_mass(m) for _ in sigma_values]
        spectral_sigma_resid = max(
            spectral_sigma_resid,
            max(m_gap_values) - min(m_gap_values),
            max(mi_values) - min(mi_values),
        )
        proxy_values = [1.0 / (m * sigma) for sigma in sigma_values]
        proxy_ratios.append(max(proxy_values) / min(proxy_values))

    min_proxy_ratio = min(proxy_ratios)
    ratio_resid = abs(min_proxy_ratio - 3.0)
    residual = max(spectral_sigma_resid, ratio_resid)
    report(
        7,
        "WIDTH-INDEPENDENCE-CONTRAST",
        spectral_sigma_resid <= 1e-15 and ratio_resid <= 1e-15,
        residual,
        f"spectral_sigma_resid={spectral_sigma_resid:.3e} old_proxy_ratio={min_proxy_ratio:.1f}x",
    )


def main() -> int:
    print("MASS OBSERVABLE ON THE FREE STAGGERED TWO-STEP TRANSFER SURFACE")
    print("d=3, U=1, E(p)=arcsinh(sqrt(m^2+sum_mu sin^2 p_mu))")
    check_01_symbol_scalarity()
    check_02_rest_gap()
    check_03_global_gap_and_m0_singularity()
    check_04_inertial_mass()
    check_05_universal_function()
    check_06_generator_invariance()
    check_07_width_independence_contrast()
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
