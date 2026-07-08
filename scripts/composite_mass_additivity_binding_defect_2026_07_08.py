#!/usr/bin/env python3
"""Composite mass additivity and binding-defect checks.

Companion runner for
COMPOSITE_MASS_ADDITIVITY_BINDING_DEFECT_TWO_STEP_SURFACE_BOUNDED_NOTE_2026-07-08.md.

Declared imports used here:
- block01/block02: one-particle two-step surface dispersion conventions,
  E(p) = arcsinh(sqrt(m^2 + sin^2 p)), M_I(m) = m*sqrt(1+m^2),
  and F(x) = sinh(2x)/2.
- I-INT: supplied short-range contact interaction, comparator role only,
  non-derivation.  The contact strength U is an input to the runner.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

import numpy as np
from scipy.linalg import eigvalsh


PASS_COUNT = 0
FAIL_COUNT = 0

BOUND_MASSES = (0.5, 1.0)
BOUND_US = (0.2, 0.4, 0.8)

SPEC_NOTES = (
    "CHECK-02: the equal-mass identity bottom(P) = 2*E(P/2) is exact only at even total-P (P/2 on the one-particle grid); curvature is extracted by an even-P quadratic+quartic fit, and the odd-P grid-parity shift is reported as context.",
    "CHECK-04: band curvature is extracted by a quadratic+quartic fit in P^2; the pure-quadratic fit residual at these windows is real quartic curvature, not numerics.",
    "CHECK-05 physics: composite inertial mass is bandwidth-dominated (binding RAISES M_comp on the lattice), so no species-blind function of rest energy alone can give exact finite-spacing composite universality; gates use fixed thresholds and the scaling-window trend is reported.",
)


@dataclass(frozen=True)
class QuadraticFit:
    curvature: float
    mass: float
    residual: float
    linear: float
    intercept: float


@dataclass(frozen=True)
class CompositeMeasurement:
    m: float
    U: float
    E0: float
    binding: float
    curvature: float
    M_comp: float
    fit_residual: float
    F_E0: float
    Delta_univ: float
    Delta_add: float


def report(num: int, name: str, condition: bool, residual: float, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    PASS_COUNT += int(ok)
    FAIL_COUNT += int(not ok)
    line = f"CHECK-{num:02d} {name}: {'PASS' if ok else 'FAIL'} residual={residual:.3e}"
    if detail:
        line += f" {detail}"
    print(line)


def momentum_grid(L: int) -> np.ndarray:
    return 2.0 * np.pi * np.arange(L, dtype=float) / float(L)


def momentum_value(K: int, L: int) -> float:
    return 2.0 * np.pi * (K % L) / float(L)


def signed_momentum_value(K: int, L: int) -> float:
    idx = K % L
    if idx > L // 2:
        idx -= L
    return 2.0 * np.pi * idx / float(L)


def near_zero_indices(L: int, radius: int) -> list[int]:
    return [(-n) % L for n in range(radius, 0, -1)] + [0] + list(range(1, radius + 1))


def dispersion(m: float, p: np.ndarray | float) -> np.ndarray | float:
    return np.arcsinh(np.sqrt(m * m + np.sin(p) ** 2))


def inertial_mass(m: float) -> float:
    return float(m * np.sqrt(1.0 + m * m))


def universal_function(x: float) -> float:
    return float(0.5 * np.sinh(2.0 * x))


@lru_cache(maxsize=None)
def dft_phase(L: int) -> np.ndarray:
    r = np.arange(L, dtype=float)
    q = momentum_grid(L)
    return np.exp(1j * np.outer(r, q)) / np.sqrt(float(L))


def spectral_matrix_from_eigenvalues(eigenvalues: np.ndarray) -> np.ndarray:
    phase = dft_phase(int(eigenvalues.size))
    matrix = (phase * eigenvalues[np.newaxis, :]) @ phase.conj().T
    return 0.5 * (matrix + matrix.conj().T)


def one_particle_kinetic(L: int, m: float) -> np.ndarray:
    return spectral_matrix_from_eigenvalues(np.asarray(dispersion(m, momentum_grid(L)), dtype=float))


def pblock_hamiltonian(L: int, m_a: float, m_b: float, U: float, K: int) -> np.ndarray:
    q = momentum_grid(L)
    P = momentum_value(K, L)
    eigenvalues = np.asarray(dispersion(m_a, q) + dispersion(m_b, P - q), dtype=float)
    matrix = spectral_matrix_from_eigenvalues(eigenvalues)
    matrix = matrix.copy()
    matrix[0, 0] -= U
    return 0.5 * (matrix + matrix.conj().T)


def lowest_pblock_energy(L: int, m_a: float, m_b: float, U: float, K: int) -> float:
    return float(eigvalsh(pblock_hamiltonian(L, m_a, m_b, U, K), subset_by_index=[0, 0])[0])


def full_two_particle_hamiltonian(L: int, m_a: float, m_b: float, U: float) -> np.ndarray:
    if L > 48:
        raise ValueError("full two-particle Hamiltonian is only used for L <= 48")
    K_a = one_particle_kinetic(L, m_a)
    K_b = one_particle_kinetic(L, m_b)
    ident = np.eye(L, dtype=complex)
    H = np.kron(K_a, ident) + np.kron(ident, K_b)
    for x in range(L):
        H[x * L + x, x * L + x] -= U
    return 0.5 * (H + H.conj().T)


def total_translation_operator(L: int) -> np.ndarray:
    T = np.zeros((L * L, L * L), dtype=complex)
    for x1 in range(L):
        for x2 in range(L):
            old = x1 * L + x2
            new = ((x1 + 1) % L) * L + ((x2 + 1) % L)
            T[new, old] = 1.0
    return T


def total_momentum_sector_basis(L: int, K: int) -> np.ndarray:
    P = momentum_value(K, L)
    V = np.zeros((L * L, L), dtype=complex)
    norm = 1.0 / np.sqrt(float(L))
    for r in range(L):
        for X in range(L):
            x1 = (X + r) % L
            x2 = X
            V[x1 * L + x2, r] = norm * np.exp(1j * P * X)
    return V


def fit_quadratic(xs: np.ndarray, ys: np.ndarray) -> QuadraticFit:
    coeff = np.polyfit(xs, ys, 2)
    pred = np.polyval(coeff, xs)
    curvature = float(2.0 * coeff[0])
    mass = float("inf") if curvature == 0.0 else float(1.0 / curvature)
    return QuadraticFit(
        curvature=curvature,
        mass=mass,
        residual=float(np.max(np.abs(pred - ys))),
        linear=float(coeff[1]),
        intercept=float(coeff[2]),
    )


def fit_even_quartic(xs: np.ndarray, ys: np.ndarray, sextic: bool = False) -> QuadraticFit:
    """Fit the even model y = c0 + c1 P^2 + c2 P^4 (+ c3 P^6) and return
    curvature 2*c1.

    The band is an even analytic function of P, so this isolates the exact
    quadratic coefficient from the real quartic/sextic curvature that a pure
    quadratic fit misattributes."""
    x2 = xs * xs
    columns = [np.ones_like(x2), x2, x2 * x2]
    if sextic:
        columns.append(x2 * x2 * x2)
    design = np.column_stack(columns)
    coeffs, *_ = np.linalg.lstsq(design, ys, rcond=None)
    pred = design @ coeffs
    c1 = float(coeffs[1])
    curvature = 2.0 * c1
    mass = float("inf") if curvature == 0.0 else float(1.0 / curvature)
    return QuadraticFit(
        curvature=curvature,
        mass=mass,
        residual=float(np.max(np.abs(pred - ys))),
        linear=float(coeffs[2]),
        intercept=float(coeffs[0]),
    )


def richardson_curvature(f, h0: float = 0.05, levels: int = 6) -> float:
    """Richardson-extrapolated second derivative of an even function at 0."""
    best = None
    prev = None
    h = h0
    for _ in range(levels):
        coarse = (f(h) - 2.0 * f(0.0) + f(-h)) / (h * h)
        fine = (f(0.5 * h) - 2.0 * f(0.0) + f(-0.5 * h)) / (0.25 * h * h)
        value = (4.0 * fine - coarse) / 3.0
        if prev is not None and best is not None and abs(value - prev) > best:
            break
        best = abs(value - prev) if prev is not None else None
        prev = value
        h *= 0.5
    return float(prev)


def check_01_pblock_exactness() -> None:
    L = 12
    m_a = m_b = 0.7
    U = 0.5
    H_full = full_two_particle_hamiltonian(L, m_a, m_b, U)
    T = total_translation_operator(L)

    max_spectrum_resid = 0.0
    max_translation_resid = 0.0
    max_orth_resid = 0.0
    for K in range(L):
        P = momentum_value(K, L)
        V = total_momentum_sector_basis(L, K)
        max_orth_resid = max(max_orth_resid, float(np.max(np.abs(V.conj().T @ V - np.eye(L)))))
        max_translation_resid = max(
            max_translation_resid,
            float(np.max(np.abs(T @ V - np.exp(-1j * P) * V))),
        )
        H_sector = V.conj().T @ H_full @ V
        H_sector = 0.5 * (H_sector + H_sector.conj().T)
        sector_vals = eigvalsh(H_sector)[:3]
        block_vals = eigvalsh(pblock_hamiltonian(L, m_a, m_b, U, K))[:3]
        max_spectrum_resid = max(max_spectrum_resid, float(np.max(np.abs(sector_vals - block_vals))))

    residual = max(max_spectrum_resid, max_translation_resid, max_orth_resid)
    report(
        1,
        "PBLOCK-EXACTNESS",
        residual <= 1e-10,
        residual,
        "spectrum={:.3e} translation={:.3e} orth={:.3e}".format(
            max_spectrum_resid, max_translation_resid, max_orth_resid
        ),
    )


def check_02_free_additivity() -> None:
    L = 64
    masses = (0.5, 1.0)
    rest_resid = 0.0
    equal_curvature_resid = 0.0
    equal_formula_resid = 0.0
    equal_fit_resid = 0.0
    exact_even_formula_resid = 0.0

    even_Ks = [(-6) % L, (-4) % L, (-2) % L, 0, 2, 4, 6]
    even_xs = np.array([signed_momentum_value(K, L) for K in even_Ks], dtype=float)
    odd_Ks = [(-1) % L, 1]

    for m_a in masses:
        for m_b in masses:
            bottom0 = lowest_pblock_energy(L, m_a, m_b, 0.0, 0)
            target0 = float(np.arcsinh(m_a) + np.arcsinh(m_b))
            rest_resid = max(rest_resid, abs(bottom0 - target0))

            even_ys = np.array([lowest_pblock_energy(L, m_a, m_b, 0.0, K) for K in even_Ks], dtype=float)
            fit = fit_even_quartic(even_xs, even_ys)
            reduced_curvature = 1.0 / (inertial_mass(m_a) + inertial_mass(m_b))

            if m_a == m_b:
                even_formula = np.array([2.0 * dispersion(m_a, P / 2.0) for P in even_xs], dtype=float)
                exact_even_formula_resid = max(
                    exact_even_formula_resid,
                    float(np.max(np.abs(even_ys - even_formula))),
                )
                equal_formula_resid = exact_even_formula_resid
                # The identity bottom(P) = 2 E(P/2) is exact at even P, so
                # the curvature statement needs no band fit: Richardson on
                # the continuum function is the correct extraction, and the
                # target 1/(2 M_I) is block01's exact derivative.
                curv_exact = richardson_curvature(lambda P, mm=m_a: 2.0 * float(dispersion(mm, P / 2.0)))
                equal_curvature_resid = max(equal_curvature_resid, abs(curv_exact - reduced_curvature))
                equal_fit_resid = max(equal_fit_resid, fit.residual)

                odd_shift = max(
                    abs(lowest_pblock_energy(L, m_a, m_b, 0.0, K) - 2.0 * dispersion(m_a, signed_momentum_value(K, L) / 2.0))
                    for K in odd_Ks
                )
                print(
                    "MEASURE-02 equal m={:.1f} richardson_curvature={:.12e} target_1_over_2MI={:.12e} "
                    "curvature_resid={:.3e} evenP_identity_resid={:.3e} bandfit_curvature_context={:.12e} "
                    "oddP_grid_parity_shift_context={:.3e}".format(
                        m_a,
                        curv_exact,
                        reduced_curvature,
                        abs(curv_exact - reduced_curvature),
                        exact_even_formula_resid,
                        fit.curvature,
                        odd_shift,
                    )
                )
            else:
                print(
                    "REPORT-02 unequal m_a={:.1f} m_b={:.1f} evenP_curvature_fit={:.12e} "
                    "reported_reduced_inertia={:.12e} quartic_fit_resid={:.3e}".format(
                        m_a, m_b, fit.curvature, reduced_curvature, fit.residual
                    )
                )

    residual = max(rest_resid, equal_curvature_resid, equal_formula_resid)
    report(
        2,
        "FREE-ADDITIVITY",
        rest_resid <= 1e-10 and equal_curvature_resid <= 1e-8 and equal_formula_resid <= 1e-10,
        residual,
        "rest={:.3e} richardson_curvature={:.3e} evenP_identity={:.3e} bandfit_context={:.3e}".format(
            rest_resid,
            equal_curvature_resid,
            exact_even_formula_resid,
            equal_fit_resid,
        ),
    )


def compute_composite_measurements() -> list[CompositeMeasurement]:
    L = 64
    fit_Ks = near_zero_indices(L, 3)
    fit_xs = np.array([signed_momentum_value(K, L) for K in fit_Ks], dtype=float)
    measurements: list[CompositeMeasurement] = []

    for m in BOUND_MASSES:
        for U in BOUND_US:
            ys = np.array([lowest_pblock_energy(L, m, m, U, K) for K in fit_Ks], dtype=float)
            fit = fit_even_quartic(fit_xs, ys, sextic=True)
            fit_p4 = fit_even_quartic(fit_xs, ys, sextic=False)
            print(
                "EXTRACTION-04 m={:.1f} U={:.1f} curvature_p6={:.12e} curvature_p4={:.12e} "
                "extraction_shift={:.3e}".format(
                    m, U, fit.curvature, fit_p4.curvature, abs(fit.curvature - fit_p4.curvature)
                )
            )
            E0 = lowest_pblock_energy(L, m, m, U, 0)
            binding = float(2.0 * np.arcsinh(m) - E0)
            F_E0 = universal_function(E0)
            M_free = 2.0 * inertial_mass(m)
            measurements.append(
                CompositeMeasurement(
                    m=m,
                    U=U,
                    E0=E0,
                    binding=binding,
                    curvature=fit.curvature,
                    M_comp=fit.mass,
                    fit_residual=fit.residual,
                    F_E0=F_E0,
                    Delta_univ=fit.mass - F_E0,
                    Delta_add=fit.mass - M_free,
                )
            )
    return measurements


def check_03_bound_state(measurements: list[CompositeMeasurement]) -> None:
    min_separation = float("inf")
    for item in measurements:
        edge = float(2.0 * np.arcsinh(item.m))
        min_separation = min(min_separation, item.binding)
        print(
            "MEASURE-03 m={:.1f} U={:.1f} E2_P0={:.12e} continuum_edge={:.12e} E_B={:.12e}".format(
                item.m, item.U, item.E0, edge, item.binding
            )
        )

    residual = max(0.0, 1e-8 - min_separation)
    report(
        3,
        "BOUND-STATE+BINDING-DEFECT",
        min_separation > 1e-8,
        residual,
        f"min_binding={min_separation:.3e}",
    )


def check_04_composite_inertial_mass(measurements: list[CompositeMeasurement]) -> None:
    min_mass = float("inf")
    max_fit_resid = 0.0
    for item in measurements:
        min_mass = min(min_mass, item.M_comp)
        max_fit_resid = max(max_fit_resid, item.fit_residual)
        print(
            "LOAD-BEARING-04 m={:.1f} U={:.1f} M_comp={:.12e} free_2MI={:.12e} "
            "F_E2={:.12e} Delta_univ={:.12e} Delta_add={:.12e} curvature={:.12e} "
            "fit_resid={:.3e}".format(
                item.m,
                item.U,
                item.M_comp,
                2.0 * inertial_mass(item.m),
                item.F_E0,
                item.Delta_univ,
                item.Delta_add,
                item.curvature,
                item.fit_residual,
            )
        )

    residual = max(max_fit_resid, max(0.0, -min_mass))
    report(
        4,
        "COMPOSITE-INERTIAL-MASS",
        min_mass > 0.0 and max_fit_resid < 1e-7,
        residual,
        f"min_M_comp={min_mass:.3e} max_quartic_fit_resid={max_fit_resid:.3e}",
    )


def check_05_common_acceleration(measurements: list[CompositeMeasurement]) -> None:
    """Gated dichotomy with FIXED thresholds.

    (a) Q-coupling (species-blind charge counting): the composite's
        universality violation |2 M_I / M_comp - 1| must be a real signal
        (>= 0.25) at the strongest binding U = 0.8: force counts charges
        while the bandwidth-dominated M_comp grows, so charge-counting
        couplings cannot give composite universality.
    (b) No-rest-energy-source exhibit: the singles-exact source F(rest gap)
        (block01 T5 makes single-particle universality exact by
        construction) must FAIL for composites, |F(E2(0))/M_comp - 1| >=
        0.25 at U = 0.8: F is forced by singles and convex, and M_comp is
        bandwidth-dominated, so no species-blind function of rest energy
        alone gives exact finite-spacing composite universality.
    (c) Scaling-window trend (reported, ungated): both violations must be
        read against their U -> 0 baselines; the printed trend shows them
        shrinking with weaker binding, which is the honest scaling-window
        statement.
    """
    max_gate_deficit = 0.0
    for item in measurements:
        M_I = inertial_mass(item.m)
        a_Q_over_g = 2.0 / item.M_comp
        a_F_over_g = item.F_E0 / item.M_comp
        q_violation = abs(2.0 * M_I / item.M_comp - 1.0)
        f_violation = abs(a_F_over_g - 1.0)
        single_f_check = abs(universal_function(float(np.arcsinh(item.m))) / M_I - 1.0)

        if abs(item.U - 0.8) < 1e-12:
            max_gate_deficit = max(
                max_gate_deficit,
                max(0.0, 0.25 - q_violation),
                max(0.0, 0.25 - f_violation),
                max(0.0, single_f_check - 1e-12),
            )

        print(
            "MEASURE-05 m={:.1f} U={:.1f} a_Q/g={:.12e} a_F/g={:.12e} "
            "Q_composite_violation={:.6e} F_composite_violation={:.6e} "
            "F_single_violation={:.3e} E_B={:.6e}".format(
                item.m,
                item.U,
                a_Q_over_g,
                a_F_over_g,
                q_violation,
                f_violation,
                single_f_check,
                item.binding,
            )
        )

    for m in BOUND_MASSES:
        M_I = inertial_mass(m)
        f_baseline = abs(universal_function(float(2.0 * np.arcsinh(m))) / (2.0 * M_I) - 1.0)
        print(
            "CONTEXT-05 m={:.1f} U->0 baseline: F(2 m_gap)/(2 M_I) - 1 = {:.6e} "
            "(convexity of F: even the FREE composite breaks F-universality; "
            "additivity and F-universality are compatible only in the scaling window)".format(
                m, f_baseline
            )
        )

    report(
        5,
        "COMMON-ACCELERATION-DICHOTOMY",
        max_gate_deficit <= 0.0,
        max_gate_deficit,
        "gate: singles F-exact (violation<=1e-12) AND composite Q/F violations >= 0.25 at U=0.8",
    )


def ring_delta(xs: np.ndarray, center: float, L: int) -> np.ndarray:
    return ((xs - center + 0.5 * L) % L) - 0.5 * L


def gaussian_packet(L: int, center: float, sigma_x: float) -> np.ndarray:
    xs = np.arange(L, dtype=float)
    packet = np.exp(-(ring_delta(xs, center, L) ** 2) / (4.0 * sigma_x * sigma_x)).astype(complex)
    packet /= np.sqrt(np.vdot(packet, packet).real)
    return packet


def product_state_free_energy_delta(K: np.ndarray, phi_1: np.ndarray, phi_2: np.ndarray) -> float:
    K_phi_1 = K @ phi_1
    K_phi_2 = K @ phi_2
    single_sum = float((np.vdot(phi_1, K_phi_1) + np.vdot(phi_2, K_phi_2)).real)
    psi = np.outer(phi_1, phi_2)
    H_psi = np.outer(K_phi_1, phi_2) + np.outer(phi_1, K_phi_2)
    product_energy = float(np.vdot(psi, H_psi).real)
    return product_energy - single_sum


def check_06_separation_overlap_bound() -> None:
    L = 128
    m = 1.0
    sigma_x = 4.0
    separations = (16, 32, 48)
    K = one_particle_kinetic(L, m)

    max_energy_delta = 0.0
    max_overlap_factor_resid = 0.0
    for d in separations:
        center_1 = 0.5 * L - 0.5 * d
        center_2 = 0.5 * L + 0.5 * d
        phi_1 = gaussian_packet(L, center_1, sigma_x)
        phi_2 = gaussian_packet(L, center_2, sigma_x)
        overlap = abs(np.vdot(phi_1, phi_2))
        gaussian_bound = float(np.exp(-(d * d) / (8.0 * sigma_x * sigma_x)))
        ratio = float(overlap / gaussian_bound)
        if ratio < 1.0 / 3.0:
            factor_resid = (1.0 / 3.0) - ratio
        elif ratio > 3.0:
            factor_resid = ratio - 3.0
        else:
            factor_resid = 0.0
        max_overlap_factor_resid = max(max_overlap_factor_resid, factor_resid)

        energy_delta = product_state_free_energy_delta(K, phi_1, phi_2)
        max_energy_delta = max(max_energy_delta, abs(energy_delta))
        print(
            "MEASURE-06 d={} overlap={:.12e} gaussian_bound={:.12e} ratio={:.6e} "
            "energy_delta={:.3e} reason=free distinguishable theory is exactly additive regardless of overlap".format(
                d, overlap, gaussian_bound, ratio, energy_delta
            )
        )

    residual = max(max_energy_delta, max_overlap_factor_resid)
    report(
        6,
        "SEPARATION/OVERLAP-BOUND",
        max_overlap_factor_resid <= 0.0 and max_energy_delta <= 1e-10,
        residual,
        f"max_energy_delta={max_energy_delta:.3e} max_overlap_factor_resid={max_overlap_factor_resid:.3e}",
    )


def main() -> int:
    print("COMPOSITE MASS ADDITIVITY / BINDING DEFECT RUNNER")
    print("CONVENTIONS: 1D E(p)=arcsinh(sqrt(m^2+sin^2 p)); M_I=m*sqrt(1+m^2); F(x)=sinh(2x)/2")
    for note in SPEC_NOTES:
        print(f"SPEC-NOTE: {note}")

    check_01_pblock_exactness()
    check_02_free_additivity()
    measurements = compute_composite_measurements()
    check_03_bound_state(measurements)
    check_04_composite_inertial_mass(measurements)
    check_05_common_acceleration(measurements)
    check_06_separation_overlap_bound()
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
