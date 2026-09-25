#!/usr/bin/env python3
"""Finite exact-side mod-3 kernel diagnostics for the post-mark Jacobi model.

The exact identities and sufficient fixed-index criterion are in the paired
note. Spectral scans use double precision and are exploratory only: they do
not prove a kernel limit, readout limit, or a model/axiom conclusion.
"""
from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import eigh_tridiagonal, expm
from scipy.special import jv

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = (
    "docs/FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/SHORT_TIME_SCALING_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/POSTMARK_ELECTRIC_MOVING_INDEX_CELL_SYMBOL_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/POSTMARK_ELECTRIC_TWO_BAND_CENTRAL_MATCH_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/POSTMARK_ELECTRIC_EXACT_SIDE_FIXED_INDEX_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "scripts/core_derivation.py",
)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUTPUT_DIR = ROOT / "outputs" / "postmark_moving_index_2026_09_24"
SOURCE_REVISION = "c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6"

POS_LEFT = (0, 1, 0, 1, 1, 1, 2, 1, 2, 2, 2, 3, 2, 3, 3)
POS_RIGHT = (0, 0, 0, 1, 0, 1, 1, 1, 2, 1, 2, 2, 2, 3, 2)
NEG_LEFT = (-1, -2, -1, -2, -2, -2, -3, -2, -3, -3, -3, -4, -3, -4, -4)
NEG_RIGHT = (-1, -1, -1, -2, -1, -2, -2, -2, -3, -2, -3, -3, -3, -4, -3)


def load_core_derivation():
    path = HERE / "core_derivation.py"
    spec = importlib.util.spec_from_file_location("postmark_core_derivation", path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


physical_model = load_core_derivation()


def f(m: int) -> int:
    return m * (m + 1)


def edge_labels(n: int) -> tuple[int, int]:
    """Return the signed effective Casimir labels on edge n -> n+1."""
    if n >= 0:
        k, r = divmod(n, 15)
        return 3 * k + POS_LEFT[r], 3 * k + POS_RIGHT[r]
    cells = -(n // 15)
    r = n + 15 * cells
    return 3 * cells + NEG_LEFT[r], 3 * cells + NEG_RIGHT[r]


def verify_signed_label_geometry() -> dict:
    """Check the exact Casimir reflection and the endpoint-barrier offsets."""
    for r in range(15):
        if NEG_LEFT[r] != -POS_LEFT[r] - 1:
            raise ArithmeticError(("left Casimir reflection", r))
        if NEG_RIGHT[r] != -POS_RIGHT[r] - 1:
            raise ArithmeticError(("right Casimir reflection", r))
        if abs(5 * POS_LEFT[r] - r) >= 5:
            raise ArithmeticError(("left coordinate offset", r))
        if abs(5 * POS_RIGHT[r] - r) >= 5:
            raise ArithmeticError(("right coordinate offset", r))

    edges_checked = 0
    max_factor_offset_times5 = 0
    for n in range(-1000, 1001):
        k, r = divmod(n, 15)
        reference = (3 * k + POS_LEFT[r], 3 * k + POS_RIGHT[r])
        actual = edge_labels(n)
        if tuple(f(m) for m in actual) != tuple(f(m) for m in reference):
            raise ArithmeticError(("signed Casimir edge identity", n, actual, reference))
        # Exact numerator for |m - n/5|. A preceding-edge factor gets
        # an additional 1/5 when measured relative to the node n.
        max_factor_offset_times5 = max(
            max_factor_offset_times5,
            abs(5 * reference[0] - n), abs(5 * reference[1] - n),
        )
        mirror = edge_labels(-5 - n)
        if tuple(sorted(f(m) for m in actual)) != tuple(sorted(f(m) for m in mirror)):
            raise ArithmeticError(("path reflection Casimir identity", n, actual, mirror))
        edges_checked += 1
    if max_factor_offset_times5 >= 5:
        raise ArithmeticError(("signed factor offset is not <1", max_factor_offset_times5))
    return {
        "residue_reflection": "m_minus=-m_plus-1; f(m)=f(-m-1)",
        "residue_count": 15,
        "finite_edges_checked": edges_checked,
        "path_reflection": "edge n mirrors to edge -5-n; node n mirrors to -4-n",
        "reflected_edges_checked": edges_checked,
        "max_abs_edge_factor_offset_from_n_over5": max_factor_offset_times5 / 5.0,
        "preceding_edge_offset_bound_from_node": "<6/5",
    }


def finite_spin_matrix(spin: int):
    """Return N_S=J M_S J on I_S=[-5S,5S-4], in increasing n order."""
    if spin < 1:
        raise ValueError("spin must be a positive integer")
    casimir = spin * (spin + 1)
    lo, hi = -5 * spin, 5 * spin - 4
    nodes = np.arange(lo, hi + 1, dtype=np.int64)
    diagonal = np.empty(nodes.size, dtype=np.float64)
    positive_links = np.empty(nodes.size - 1, dtype=np.float64)

    def weight(label: int) -> float:
        return 1.0 - f(label) / casimir

    for i, n_value in enumerate(nodes):
        n = int(n_value)
        left, _right = edge_labels(n)
        _previous_left, previous_right = edge_labels(n - 1)
        diagonal[i] = weight(left) + weight(previous_right)
        if i + 1 < nodes.size:
            _left, right = edge_labels(n)
            a, b = weight(left), weight(right)
            if a < -1e-13 or b < -1e-13:
                raise ArithmeticError(("negative exact edge weight", spin, n, a, b))
            positive_links[i] = math.sqrt(max(a, 0.0) * max(b, 0.0))

    # M_S has positive path links. J M_S J reverses their signs.
    return lo, hi, diagonal, -positive_links, positive_links


def verify_physical_coefficients() -> dict:
    """Compare the residue formula to direct physical-hop enumeration."""
    rows = []
    maximum = 0.0
    for spin in (1, 2, 3, 5, 8):
        lo, hi, diagonal, negative_links, positive_links = finite_spin_matrix(spin)
        path = physical_model.walk_nodes(5 * spin)
        if not all(n in path for n in range(lo, hi + 1)):
            raise ArithmeticError(("physical path coverage", spin, lo, hi))
        inverse = {state: n for n, state in path.items()}
        worst = 0.0
        for n in range(lo, hi + 1):
            h2 = physical_model.finite_spin_h2(path[n], spin)
            m_diagonal = -float(h2.get(path[n], 0.0))
            worst = max(worst, abs(m_diagonal - diagonal[n - lo]))
            if n < hi:
                m_link = -float(h2.get(path[n + 1], 0.0))
                if inverse.get(path[n + 1]) != n + 1:
                    raise ArithmeticError(("path coordinate", spin, n))
                worst = max(worst, abs(m_link - positive_links[n - lo]))
                staggered_link = ((-1) ** n) * ((-1) ** (n + 1)) * m_link
                worst = max(worst, abs(staggered_link + positive_links[n - lo]))
                worst = max(worst, abs(staggered_link - negative_links[n - lo]))
        if worst > 2e-12:
            raise ArithmeticError(("physical coefficient mismatch", spin, worst))
        rows.append({"S": spin, "sites": hi - lo + 1,
                     "max_abs_entry_error": worst})
        maximum = max(maximum, worst)
    return {
        "independent_reconstruction": "scripts/core_derivation.py enumerates the physical charge/electric states and all ordered two-hop paths",
        "spins": rows,
        "maximum_abs_entry_error": maximum,
        "convention": "the physical M_S=-H_2 has positive links; N_S=J M_S J has negative links",
    }


def verify_operator_difference_coefficients() -> dict:
    """Check the weighted O(S^-2) Jacobi coefficient majorant on test spins."""
    spins = (1, 2, 3, 4, 8, 16, 32, 64)
    rows = []
    global_max = 0.0
    for spin in spins:
        lo, hi, diagonal, offdiag, _positive = finite_spin_matrix(spin)
        max_diagonal = 0.0
        max_link = 0.0
        for n in range(lo - 3, hi + 4):
            actual_diagonal = diagonal[n - lo] if lo <= n <= hi else 0.0
            scaled = spin**2 * abs(actual_diagonal - 2.0) / (1.0 + n * n)
            max_diagonal = max(max_diagonal, float(scaled))
            actual_link = offdiag[n - lo] if lo <= n < hi else 0.0
            scaled = spin**2 * abs(actual_link + 1.0) / (1.0 + n * n)
            max_link = max(max_link, float(scaled))
        if max(max_diagonal, max_link) > 12.0 + 1e-10:
            raise ArithmeticError(("weighted Jacobi difference bound", spin,
                                   max_diagonal, max_link))
        global_max = max(global_max, max_diagonal, max_link)
        rows.append({"S": spin, "max_scaled_diagonal_difference": max_diagonal,
                     "max_scaled_link_difference": max_link})
    return {
        "tested_spins": rows,
        "maximum_scaled_coefficient_difference": global_max,
        "analytic_majorant": "12*(1+n^2)/S^2 for each diagonal/link coefficient, proved from the signed-label offset table; this finite scan is corroboration only",
    }


def cap_diagnostic(spin: int, eigenvalues: np.ndarray,
                   eigenvectors: np.ndarray, epsilons=(1.0, 2.0, 4.0)):
    lo = -5 * spin
    nodes = np.arange(lo, 5 * spin - 3, dtype=np.int64)
    x = nodes / (5.0 * spin)
    w4 = 4.0 * (1.0 - x * x)
    records = []
    for eps in epsilons:
        cap = w4 <= eps / 2.0
        mask = eigenvalues >= eps
        if not np.any(mask):
            max_mass = 0.0
        else:
            masses = np.sum(np.abs(eigenvectors[cap, :][:, mask]) ** 2, axis=0)
            max_mass = float(np.max(masses))
        records.append({"epsilon": eps, "cap_sites": int(np.count_nonzero(cap)),
                        "eigenvectors_with_lambda_at_least_epsilon": int(np.count_nonzero(mask)),
                        "maximum_cap_mass": max_mass})
    return records


def evolve(eigenvalues: np.ndarray, eigenvectors: np.ndarray,
           vector: np.ndarray, phases: np.ndarray) -> np.ndarray:
    return eigenvectors @ (phases * (eigenvectors.T @ vector))


def cauchy_profile_tail_bound(time: float, radius: int, strip: float = 1.5) -> float:
    """Analytic l2 tail bound for exp(-it(2-U-U*)^2)|0> outside |n|<=R."""
    exponent = abs(time) * (2.0 + 2.0 * math.cosh(strip)) ** 2
    square = 2.0 * math.exp(
        2.0 * exponent - 2.0 * strip * (radius + 1)
    ) / (1.0 - math.exp(-2.0 * strip))
    return math.sqrt(square)


def infinite_reference_profile(time: float, radius: int = 24,
                               grid: int = 65536,
                               taylor_terms: int = 64):
    """Fourier coefficients of eta_inf, checked by an operator-power series."""
    k = 2.0 * np.pi * np.arange(grid) / grid
    symbol = 2.0 - 2.0 * np.cos(k)
    fourier = np.fft.ifft(np.exp(-1j * time * symbol**2))

    # N_inf^2 has Laurent coefficients [1,-4,6,-4,1] at shifts -2,...,2.
    # Expanding its exponential gives a second, independent coefficient route.
    h2_laurent = np.array([1.0, -4.0, 6.0, -4.0, 1.0], dtype=np.complex128)
    series = np.zeros(4 * taylor_terms + 1, dtype=np.complex128)
    power = np.array([1.0 + 0.0j])
    coefficient = 1.0 + 0.0j
    center = 2 * taylor_terms
    for order in range(taylor_terms + 1):
        reach = 2 * order
        series[center - reach:center + reach + 1] += coefficient * power
        if order < taylor_terms:
            power = np.convolve(power, h2_laurent)
            coefficient *= (-1j * time) / (order + 1)

    modes = range(-radius, radius + 1)
    fourier_values = {n: complex(fourier[n % grid]) for n in modes}
    taylor_values = {n: complex(series[center + n]) for n in modes}
    max_error = max(abs(fourier_values[n] - taylor_values[n]) for n in modes)
    if max_error > 2e-11:
        raise ArithmeticError(("infinite reference profile crosscheck", max_error))

    x = 16.0 * abs(time)
    taylor_remainder_bound = (
        math.exp(x) * x ** (taylor_terms + 1)
        / math.factorial(taylor_terms + 1)
    )
    tail_bounds = {
        str(r): cauchy_profile_tail_bound(time, r)
        for r in sorted({min(radius, 16), min(radius, 20), radius})
    }
    return fourier_values, {
        "profile": "eta_inf(n;t)=(2pi)^-1 integral exp(-it(2-2cos k)^2) exp(ink) dk",
        "uniform_fourier_grid_points": grid,
        "independent_method": "Laurent-series expansion of N_inf^2=6I-4(U+U*)+(U^2+U*^2)",
        "operator_power_series_terms": taylor_terms + 1,
        "operator_power_series_remainder_bound": taylor_remainder_bound,
        "tested_modes": [min(modes), max(modes)],
        "maximum_fourier_vs_operator_series_error": float(max_error),
        "cauchy_tail_bound_formula": "sqrt(2*exp(2*A_y-2*y*(R+1))/(1-exp(-2y))), A_y=|t|*(2+2*cosh(y))^2, y=1.5",
        "cauchy_tail_bounds_by_radius": tail_bounds,
        "status": "Fourier/series agreement is a double-precision crosscheck; the stated Cauchy tail inequality is analytic",
    }


def kernel_and_readout(spin: int, time: float, profile: dict[int, complex],
                       fixed_sites=(-1, 0, 1)):
    lo, hi, diagonal, offdiag, _positive_links = finite_spin_matrix(spin)
    eigenvalues, eigenvectors = eigh_tridiagonal(
        diagonal, offdiag, eigvals_only=False, lapack_driver="auto"
    )
    row_sums = np.abs(diagonal).copy()
    row_sums[:-1] += np.abs(offdiag)
    row_sums[1:] += np.abs(offdiag)
    x = np.arange(lo, hi + 1, dtype=np.float64) / (5.0 * spin)
    row_bound_excess = float(np.max(
        spin * (row_sums - 4.0 * (1.0 - x * x))
    ))
    if row_bound_excess > 24.0 + 1e-10:
        raise ArithmeticError(("buffered-cap row bound", spin, row_bound_excess))
    casimir = spin * (spin + 1)
    theta = time * casimir
    nodes = np.arange(lo, hi + 1, dtype=np.int64)
    omega = np.exp(2j * np.pi * np.remainder(nodes, 3) / 3)
    plus = np.exp(1j * theta * eigenvalues)
    minus = np.conjugate(plus)

    kernel = {}
    for b in fixed_sites:
        if not lo <= b <= hi:
            continue
        basis_b = np.zeros(nodes.size, dtype=np.float64)
        basis_b[b - lo] = 1.0
        before_character = evolve(eigenvalues, eigenvectors, basis_b, plus)
        after_character = omega * before_character
        column = evolve(eigenvalues, eigenvectors, after_character, minus)
        for a in fixed_sites:
            if lo <= a <= hi:
                kernel[f"{a},{b}"] = {
                    "real": float(column[a - lo].real),
                    "imag": float(column[a - lo].imag),
                }

    # The exact factorization of the full generator is tested two ways:
    # e^{-it(N^2-CN)}|0> = e^{itCN} e^{-itN^2}|0>.
    origin = np.zeros(nodes.size, dtype=np.float64)
    origin[-lo] = 1.0
    eta = evolve(eigenvalues, eigenvectors, origin,
                 np.exp(-1j * time * eigenvalues**2))
    factored_state = evolve(eigenvalues, eigenvectors, eta, plus)
    direct_state = evolve(eigenvalues, eigenvectors, origin,
                          np.exp(-1j * time * (eigenvalues**2 - casimir * eigenvalues)))
    factorization_error = float(np.linalg.norm(factored_state - direct_state))
    endpoint_tail_rows = []
    for epsilon in (0.25, 0.5, 1.0, 2.0, 4.0):
        low = eigenvalues < epsilon
        cap = 4.0 * (1.0 - x * x) <= epsilon / 2.0
        low_spectral_mass = float(np.sum(eigenvectors[-lo, low] ** 2))
        actual_cap_mass = float(np.sum(np.abs(factored_state[cap]) ** 2))
        arcsine_limit = float(np.arccos(1.0 - epsilon / 2.0) / np.pi)
        low_mass_error = abs(low_spectral_mass - arcsine_limit)
        if spin >= 32 and low_mass_error > 2e-2:
            raise ArithmeticError(("prepared-state low-energy arcsine check",
                                   spin, epsilon, low_spectral_mass,
                                   arcsine_limit, low_mass_error))
        endpoint_tail_rows.append({
            "epsilon": epsilon,
            "low_spectral_mass_of_delta0": low_spectral_mass,
            "arcsine_limit_low_spectral_mass": arcsine_limit,
            "low_spectral_mass_abs_error": low_mass_error,
            "buffered_cap_sites": int(np.count_nonzero(cap)),
            "actual_prepared_state_buffered_cap_mass_at_theta_tC":
                actual_cap_mass,
            "status": "finite-spin diagnostic; theorem is the limsup prepared-state bound in the paired note",
        })

    # Readout from the evolved state and from its conjugated-observable form.
    actual_v = np.vdot(factored_state, omega * factored_state)
    observable = (1.0 + omega + np.conjugate(omega)) / 3.0
    direct_o = np.vdot(factored_state, observable * factored_state)
    reported_o = float((1.0 + 2.0 * actual_v.real) / 3.0)
    observable_error = float(abs(direct_o.real - reported_o))
    q_eta = evolve(eigenvalues, eigenvectors, eta, plus)
    b_eta = evolve(eigenvalues, eigenvectors, omega * q_eta, minus)
    kernel_v = np.vdot(eta, b_eta)
    identity_error = float(abs(actual_v - kernel_v))

    # Directly sample the fixed limiting profile.  Its support
    # is truncated only for this numerical diagnostic; the note supplies the
    # analytic Cauchy bound for the omitted l2 tail.
    profile_radius = min(24, -lo, hi)
    eta_reference = np.zeros(nodes.size, dtype=np.complex128)
    for n in range(-profile_radius, profile_radius + 1):
        eta_reference[n - lo] = profile[n]
    ref_plus = evolve(eigenvalues, eigenvectors, eta_reference, plus)
    ref_b = evolve(eigenvalues, eigenvectors, omega * ref_plus, minus)
    profile_v = np.vdot(eta_reference, ref_b)
    profile_spectral_coefficients = eigenvectors.T @ eta_reference
    profile_diagonal_character = (eigenvectors * eigenvectors).T @ omega
    profile_diagonal_v = np.sum(
        np.abs(profile_spectral_coefficients) ** 2 * profile_diagonal_character
    )
    profile_offdiagonal_v = profile_v - profile_diagonal_v
    profile_gap = float(abs(reported_o - (1.0 + 2.0 * profile_v.real) / 3.0))
    profile_state_distance = float(np.linalg.norm(eta - eta_reference))
    profile_tail_bound = cauchy_profile_tail_bound(time, profile_radius)
    if max(factorization_error, identity_error, observable_error) > 2e-10:
        raise ArithmeticError(("finite-time readout identities", spin,
                               factorization_error, identity_error, observable_error))

    return {
        "S": spin,
        "dimension": int(nodes.size),
        "time": time,
        "time_times_C": theta,
        "max_S_times_row_sum_minus_4w": row_bound_excess,
        "fixed_index_kernel_entries": kernel,
        "actual_prepared_state_v_expectation": {
            "real": float(actual_v.real), "imag": float(actual_v.imag),
        },
        "actual_O_expectation": reported_o,
        "direct_O_diagonal_expectation": float(direct_o.real),
        "kernel_quadratic_form_v_expectation": {
            "real": float(kernel_v.real), "imag": float(kernel_v.imag),
        },
        "factorization_l2_error": factorization_error,
        "actual_readout_identity_error": identity_error,
        "projector_character_identity_error": observable_error,
        "limiting_profile_radius": profile_radius,
        "limiting_profile_l2_tail_bound": profile_tail_bound,
        "limiting_profile_truncated_v_quadratic_form": {
            "real": float(profile_v.real), "imag": float(profile_v.imag),
        },
        "limiting_profile_spectral_diagonal_term": {
            "real": float(profile_diagonal_v.real),
            "imag": float(profile_diagonal_v.imag),
        },
        "limiting_profile_spectral_offdiagonal_term": {
            "real": float(profile_offdiagonal_v.real),
            "imag": float(profile_offdiagonal_v.imag),
        },
        "limiting_profile_truncated_O_readout": float((1.0 + 2.0 * profile_v.real) / 3.0),
        "prepared_vs_truncated_limit_profile_l2_diagnostic": profile_state_distance,
        "actual_vs_truncated_limit_profile_readout_gap_diagnostic": profile_gap,
        "endpoint_high_energy_cap_mass": cap_diagnostic(
            spin, eigenvalues, eigenvectors
        ),
        "prepared_state_endpoint_tail_diagnostics": endpoint_tail_rows,
    }


def verify_small_dense_identities(profile: dict[int, complex]) -> dict:
    """Cross-check spectral propagation with independent dense expm calls."""
    spin, time = 3, 0.25
    lo, hi, diagonal, offdiag, _positive = finite_spin_matrix(spin)
    eigenvalues, eigenvectors = eigh_tridiagonal(diagonal, offdiag)
    nodes = np.arange(lo, hi + 1, dtype=np.int64)
    N = np.diag(diagonal) + np.diag(offdiag, 1) + np.diag(offdiag, -1)
    C = spin * (spin + 1)
    theta = time * C
    omega = np.diag(np.exp(2j * np.pi * np.remainder(nodes, 3) / 3))
    Qminus = (eigenvectors * np.exp(-1j * theta * eigenvalues)) @ eigenvectors.T
    Qplus = Qminus.conj().T
    Qminus_expm = expm(-1j * theta * N)
    Qplus_expm = expm(1j * theta * N)
    direct = Qminus_expm @ omega @ Qplus_expm
    # V N V* echo form: e^{-i theta N} e^{i theta V N V*} V.
    conjugated_generator = omega @ N @ omega.conj().T
    echo = Qminus_expm @ expm(1j * theta * conjugated_generator) @ omega
    echo_error = float(np.linalg.norm(direct - echo, ord=2))
    reflection = np.zeros_like(N)
    for i, n in enumerate(nodes):
        reflection[-4 - int(n) - lo, i] = 1.0
    reflection_matrix_error = float(np.linalg.norm(
        reflection @ N @ reflection - N, ord=2
    ))
    omega_scalar = np.exp(-2j * np.pi / 3.0)
    reflection_kernel_error = float(np.linalg.norm(
        reflection @ direct @ reflection - omega_scalar * direct.conj().T,
        ord=2,
    ))
    kernel_spectral_error = float(np.linalg.norm(
        (Qminus @ omega @ Qplus) - direct, ord=2
    ))
    origin = np.zeros(nodes.size, dtype=np.complex128)
    origin[-lo] = 1.0
    G = N @ N - C * N
    direct_generator = expm(-1j * time * G) @ origin
    factor_generator = Qplus_expm @ (expm(-1j * time * (N @ N)) @ origin)
    state_error = float(np.linalg.norm(direct_generator - factor_generator))
    # Exercise the production fixed-index extraction against independent dense
    # matrix exponentials, including the prepared-state quadratic form.
    production = kernel_and_readout(spin, time, profile, fixed_sites=(-1, 0, 1))
    entry_errors = []
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            key = f"{a},{b}"
            value = production["fixed_index_kernel_entries"][key]
            entry = value["real"] + 1j * value["imag"]
            entry_errors.append(abs(entry - direct[a - lo, b - lo]))
    kernel_entries_error = float(max(entry_errors))
    actual_readout = production["actual_prepared_state_v_expectation"]
    actual_readout_value = actual_readout["real"] + 1j * actual_readout["imag"]
    direct_readout = np.vdot(direct_generator, omega @ direct_generator)
    readout_error = float(abs(actual_readout_value - direct_readout))
    eta_reference = np.zeros(nodes.size, dtype=np.complex128)
    for n in range(-production["limiting_profile_radius"],
                   production["limiting_profile_radius"] + 1):
        eta_reference[n - lo] = profile[n]
    dephased_character = np.zeros_like(omega, dtype=np.complex128)
    for j in range(nodes.size):
        projector = np.outer(eigenvectors[:, j], eigenvectors[:, j])
        dephased_character += projector @ omega @ projector
    dense_diagonal_term = np.vdot(
        eta_reference, dephased_character @ eta_reference
    )
    reported_diagonal = production["limiting_profile_spectral_diagonal_term"]
    reported_diagonal_value = (reported_diagonal["real"]
                               + 1j * reported_diagonal["imag"])
    diagonal_term_error = float(abs(reported_diagonal_value - dense_diagonal_term))
    if max(echo_error, reflection_matrix_error, reflection_kernel_error,
           state_error, kernel_spectral_error, kernel_entries_error,
           readout_error, diagonal_term_error) > 2e-11:
        raise ArithmeticError(("dense identity check", echo_error,
                               reflection_matrix_error, reflection_kernel_error,
                               state_error,
                               kernel_spectral_error, kernel_entries_error,
                               readout_error, diagonal_term_error))
    return {"spin": spin, "time": time, "echo_operator_identity_error_2norm": echo_error,
            "finite_path_reflection_N_error_2norm": reflection_matrix_error,
            "finite_path_reflection_B_error_2norm": reflection_kernel_error,
            "generator_factorization_l2_error": state_error,
            "spectral_kernel_vs_dense_expm_error_2norm": kernel_spectral_error,
            "production_fixed_entry_vs_dense_expm_max_error": kernel_entries_error,
            "production_readout_vs_dense_expm_error": readout_error,
            "spectral_diagonal_vs_dense_pinching_error": diagonal_term_error}


def verify_homogeneous_bessel_kernel() -> dict:
    """Check the translation-invariant reference formula by Fourier quadrature."""
    phi = 2.0 * np.pi / 3.0
    modes = ((-2, 1), (-1, 0), (0, 0), (1, -1), (2, 2))
    grid = 16384
    k = 2.0 * np.pi * np.arange(grid) / grid
    rows = []
    max_error = 0.0
    for theta in (0.0, 0.3, 1.0, 10.0, 100.0):
        z = 2.0 * np.sqrt(3.0) * theta
        row_max = 0.0
        for a, b in modes:
            m = a - b
            integral = np.exp(1j * b * phi) * np.mean(np.exp(
                1j * m * k + 1j * z * np.cos(k + np.pi / 6.0)
            ))
            formula = (np.exp(1j * b * phi) * (1j ** m)
                       * np.exp(-1j * m * np.pi / 6.0) * jv(m, z))
            error = float(abs(integral - formula))
            max_error = max(max_error, error)
            row_max = max(row_max, error)
        rows.append({"theta": theta, "bessel_argument": z,
                     "max_quadrature_formula_error": row_max})
    if max_error > 2e-12:
        raise ArithmeticError(("homogeneous Fourier/Bessel kernel", max_error))
    return {
        "operator": "N_infinity=2I-U-U*, V U V*=omega U",
        "kernel_formula": "omega^b * i^(a-b) * exp(-i*(a-b)*pi/6) * J_(a-b)(2*sqrt(3)*theta)",
        "modes": [list(x) for x in modes],
        "uniform_grid_points_per_integral": grid,
        "theta_samples": rows,
        "maximum_Fourier_quadrature_vs_Bessel_error": max_error,
        "analytic_consequence": "for fixed integer a,b, stationary phase gives K_infinity=O(theta^-1/2); with theta=t*S(S+1), this reference kernel is O(S^-1) at fixed nonzero t",
        "scope": "translation-invariant infinite Jacobi reference only; it does not approximate the finite-spin kernel uniformly at theta of order S^2",
    }


def main():
    label_geometry = verify_signed_label_geometry()
    physical = verify_physical_coefficients()
    operator_difference = verify_operator_difference_coefficients()
    homogeneous = verify_homogeneous_bessel_kernel()
    limit_profile, limit_profile_crosscheck = infinite_reference_profile(0.25)
    dense = verify_small_dense_identities(limit_profile)
    spins = (4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128,
             192, 256, 384, 512)
    time = 0.25
    rows = [kernel_and_readout(spin, time, limit_profile) for spin in spins]
    result = {
        "claim_status": "exact finite-dimensional reduction plus double-precision exploratory spectral diagnostics; no fixed-time kernel or readout limit is proved",
        "source_revision": SOURCE_REVISION,
        "upstream_source_sha256": {
            "fast_vacancy_note": "d235b264783de82bd563d17c217c0b3bc22718638223106215ae43edfd7dbb23",
            "zero_mode_note": "b697aecbc9c8551df69eea76ea2e2aeb404dc0478fdc32e4dd1554b26a08fec8",
            "core_boundary_note": "6b791a007320753af0ac5f2d3a11ea713598360ab757185b3bc3c1c2c77d808e",
            "physical_hop_enumerator": "e282bbe1a92afdd8306892a95b537caa5222ea189a4f74a2ab8cac86f743b9c5",
        },
        "operator": "N_S=J M_S J, C=S(S+1), G_S=N_S^2-C*N_S, V|n>=exp(2*pi*i*n/3)|n>, O=(I+V+V*)/3",
        "finite_interval": "I_S=[-5S,5S-4] intersect Z",
        "exact_algebra": {
            "factorization": "e^{-itG_S}|0> = e^{it*C*N_S} eta_S(t), eta_S(t)=e^{-it*N_S^2}|0>",
            "kernel": "K_S(a,b;t)=<a|e^{-it*C*N_S} V e^{it*C*N_S}|b>",
            "prepared_state_expectation": "<V>_S=<eta_S(t)|B_S(t)|eta_S(t)>, B_S=e^{-it*C*N_S} V e^{it*C*N_S}",
            "spectral_sum": "sum_{j,k} exp(-it*C*lambda_j) exp(+it*C*lambda_k) phi_j(a) phi_k(b) sum_n omega^n phi_j(n) phi_k(n), for a real orthonormal Jacobi eigenbasis",
            "echo_identity": "K_S(a,b;t)=omega^b<a|e^{-it*C*N_S}e^{it*C*V*N_S*V*}|b>",
            "finite_path_reflection": "R_S|n>=|-4-n>, R_S N_S R_S=N_S, R_S V R_S=omega^-1 V*, hence K_S(-4-a,-4-b)=omega^-1 conjugate(K_S(b,a))",
            "single_profile_scalar": "define q_S=<eta_inf, P_S B_S P_S eta_inf>; strong eta_S->eta_inf and ||B_S||<=1 give |<V>_S-q_S|<=2||eta_S-eta_inf||, so only Re(q_S) is needed for the actual O readout limit",
            "finite_profile_approximation": "q_S is uniformly approximated by the fixed-core quadratic form sum_{a,b=-R}^R conjugate(eta_inf(a))*K_S(a,b)*eta_inf(b), with error <=2||eta_inf-P_R eta_inf||",
            "prepared_profile_rate": "at t=1/4, weighted Jacobi coefficient bounds plus Duhamel give ||eta_S-eta_inf||_2 <= 15*(28*sqrt(517)+sqrt(11900))/S^2 < 1.12e4/S^2",
            "fixed_index_zero_suffices": "entrywise decay of every fixed K_S(a,b) implies q_S->0 by finite-support approximation, but is stronger than the single scalar target",
            "falsifier_boundary": "one nonzero/nonconvergent fixed entry invalidates this sufficient criterion only; a certified wall for the physical readout requires separated actual <O> subsequences",
        },
        "physical_hop_coefficient_crosscheck": physical,
        "weighted_operator_difference_crosscheck": operator_difference,
        "signed_label_geometry_crosscheck": label_geometry,
        "small_dense_identity_crosscheck": dense,
        "homogeneous_reference_crosscheck": homogeneous,
        "limiting_profile_crosscheck": limit_profile_crosscheck,
        "diagnostic_method": "SciPy eigh_tridiagonal in float64; fixed-index entries by two spectral matrix-vector actions; all displayed scans are exploratory and are not interval-certified",
        "numerics": {"numpy": np.__version__, "scipy": scipy.__version__, "time": time,
                     "spins": list(spins), "rows": rows},
        "interpretation": "The scan can expose likely oscillation and prioritize proof work, but finite double-precision values prove neither convergence nor nonconvergence and do not force an axiom revision.",
    }
    target = OUTPUT_DIR / "EXACT_SIDE_FIXED_INDEX_KERNEL_RESULTS.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
