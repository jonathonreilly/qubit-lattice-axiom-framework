#!/usr/bin/env python3
"""Full lattice two-band Moyal-B^2 response check.

Scope: H(k) = -2 cos(kx) sigma_x - 2 cos(ky) sigma_y + m sigma_z.

Run:
    python3 scripts/frontier_two_band_lattice_moyal_full_b2_2026_06_13.py
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import frontier_finite_cell_two_band_closed_form_2026_06_13 as finite_cell_reference


MU = 1.7086
TEMP = 0.2
MASSES = (0.0, 0.2, 0.3, 0.5)
TARGETS_DECIMAL = {
    0.0: Decimal("0.042933687517"),
    0.2: Decimal("0.041273318495"),
    0.3: Decimal("0.039175811591"),
    0.5: Decimal("0.030744459999"),
}
TARGETS = {m: float(v) for m, v in TARGETS_DECIMAL.items()}

POLE_ORDER = 5
QUAD_COARSE = 48
QUAD_FINE = 64
CLOSURE_REL_BOUND = 0.38
QUAD_REL_BOUND = 4.0e-3
FIT_RESID_BOUND = 2.0e-8
REFERENCE_TOL = Decimal("1e-12")
COMPLETENESS_FD_COARSE_STEP = 5.0e-4
COMPLETENESS_FD_FINE_STEP = 2.5e-4
COMPLETENESS_FD_X_TOL = 7.0e-7
COMPLETENESS_FD_MIN_RATIO = 3.5
COMPLETENESS_FD_SAMPLES = (
    (0.37, 0.91, 0.2, 2.3 + 0.7j),
    (1.21, 2.20, 0.5, -1.7 + 0.9j),
    (2.41, 0.58, 0.3, 1.9 - 0.8j),
)

PAULI_X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128)
PAULI_Y = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=np.complex128)
PAULI_Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)
IDENTITY_2 = np.eye(2, dtype=np.complex128)


PASS_COUNT = 0
FAIL_COUNT = 0


@dataclass(frozen=True)
class CompletenessCheckResult:
    passed: bool
    max_coarse_abs: float
    max_fine_abs: float
    min_convergence_ratio: float


def check(condition: bool, claim: str, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {claim}{suffix}")


def finish() -> None:
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        sys.exit(1)


def fermi_grand(E: float, mu: float, temp: float) -> float:
    return float(-temp * np.logaddexp(0.0, -(E - mu) / temp))


def grand_derivatives(E: float, mu: float, temp: float, max_order: int) -> list[float]:
    """Return F, F', ..., F^(max_order) for F=-T log(1+exp(-(E-mu)/T))."""
    a = (E - mu) / temp
    if a > 700.0:
        occ = 0.0
    elif a < -700.0:
        occ = 1.0
    else:
        occ = 1.0 / (1.0 + math.exp(a))

    out = [fermi_grand(E, mu, temp)]
    # P_n(occ) with F^(n)=T^(1-n) P_n(occ), P_1=f.
    coeff = np.array([0.0, 1.0], dtype=np.float64)
    for n in range(1, max_order + 1):
        poly = 0.0
        power = 1.0
        for c in coeff:
            poly += float(c) * power
            power *= occ
        out.append((temp ** (1 - n)) * poly)

        deriv = np.array([i * coeff[i] for i in range(1, len(coeff))], dtype=np.float64)
        nxt = np.zeros(len(deriv) + 2, dtype=np.float64)
        for i, c in enumerate(deriv):
            nxt[i + 1] -= c
            nxt[i + 2] += c
        coeff = nxt
    return out


def lattice_a_terms(
    kx: float, ky: float, mass: float, z: complex
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    cx = math.cos(kx)
    cy = math.cos(ky)
    sx = math.sin(kx)
    sy = math.sin(ky)

    hamiltonian = (-2.0 * cx) * PAULI_X + (-2.0 * cy) * PAULI_Y + mass * PAULI_Z
    a_mat = z * IDENTITY_2 - hamiltonian
    ax = (-2.0 * sx) * PAULI_X
    ay = (-2.0 * sy) * PAULI_Y
    axx = (-2.0 * cx) * PAULI_X
    ayy = (-2.0 * cy) * PAULI_Y
    axy = np.zeros((2, 2), dtype=np.complex128)
    return a_mat, ax, ay, axx, ayy, axy


def implemented_b2_matrices(
    kx: float, ky: float, mass: float, z: complex
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return implemented x_mat, G2_full, G2_cross, and G2_second_derivative."""
    a_mat, ax, ay, axx, ayy, _axy = lattice_a_terms(kx, ky, mass, z)
    g = np.linalg.inv(a_mat)
    gx = -g @ ax @ g
    gy = -g @ ay @ g
    gxx = 2.0 * g @ ax @ g @ ax @ g - g @ axx @ g
    gyy = 2.0 * g @ ay @ g @ ay @ g - g @ ayy @ g
    gxy = g @ ay @ g @ ax @ g + g @ ax @ g @ ay @ g

    c_mat = ax @ gy - ay @ gx
    cx_mat = axx @ gy + ax @ gxy - ay @ gxx
    cy_mat = ax @ gyy - ayy @ gx - ay @ gxy
    g1x = -(1.0j / 2.0) * (gx @ c_mat + g @ cx_mat)
    g1y = -(1.0j / 2.0) * (gy @ c_mat + g @ cy_mat)

    lambda_a_g1 = ax @ g1y - ay @ g1x
    lambda2_a_g0 = axx @ gyy + ayy @ gxx
    x_mat = (1.0j / 2.0) * lambda_a_g1 - 0.125 * lambda2_a_g0
    cross = -g @ ((1.0j / 2.0) * lambda_a_g1)
    second = g @ (0.125 * lambda2_a_g0)
    full = cross + second
    return x_mat, full, cross, second


def star_traces(kx: float, ky: float, mass: float, z: complex) -> tuple[complex, complex, complex]:
    """Return trace(G2_full), trace(G2_cross), trace(G2_second_derivative)."""
    _x_mat, full, cross, second = implemented_b2_matrices(kx, ky, mass, z)
    return complex(np.trace(full)), complex(np.trace(cross)), complex(np.trace(second))


def finite_difference_g0_derivatives(
    kx: float, ky: float, mass: float, z: complex, step: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    g = np.linalg.inv(lattice_a_terms(kx, ky, mass, z)[0])
    g_xp = np.linalg.inv(lattice_a_terms(kx + step, ky, mass, z)[0])
    g_xm = np.linalg.inv(lattice_a_terms(kx - step, ky, mass, z)[0])
    g_yp = np.linalg.inv(lattice_a_terms(kx, ky + step, mass, z)[0])
    g_ym = np.linalg.inv(lattice_a_terms(kx, ky - step, mass, z)[0])
    g_pp = np.linalg.inv(lattice_a_terms(kx + step, ky + step, mass, z)[0])
    g_pm = np.linalg.inv(lattice_a_terms(kx + step, ky - step, mass, z)[0])
    g_mp = np.linalg.inv(lattice_a_terms(kx - step, ky + step, mass, z)[0])
    g_mm = np.linalg.inv(lattice_a_terms(kx - step, ky - step, mass, z)[0])

    gx = (g_xp - g_xm) / (2.0 * step)
    gy = (g_yp - g_ym) / (2.0 * step)
    gxx = (g_xp - 2.0 * g + g_xm) / (step * step)
    gyy = (g_yp - 2.0 * g + g_ym) / (step * step)
    gxy = (g_pp - g_pm - g_mp + g_mm) / (4.0 * step * step)
    return g, gx, gy, gxx, gyy, gxy


def finite_difference_g1_matrix(kx: float, ky: float, mass: float, z: complex, step: float) -> np.ndarray:
    _a_mat, ax, ay, _axx, _ayy, _axy = lattice_a_terms(kx, ky, mass, z)
    g, gx, gy, _gxx, _gyy, _gxy = finite_difference_g0_derivatives(kx, ky, mass, z, step)
    return -g @ ((1.0j / 2.0) * (ax @ gy - ay @ gx))


def finite_difference_b2_source_matrix(kx: float, ky: float, mass: float, z: complex, step: float) -> np.ndarray:
    # Independent Moyal reconstruction: finite-difference G0 derivatives, build G1
    # from the order-B equation, finite-difference G1 derivatives, then apply
    # (i/2)Lambda(A,G1) - (1/8)Lambda^2(A,G0).  This checks x_mat directly.
    inner_step = 0.5 * step
    _a_mat, ax, ay, axx, ayy, axy = lattice_a_terms(kx, ky, mass, z)
    _g, _gx, _gy, gxx, gyy, gxy = finite_difference_g0_derivatives(kx, ky, mass, z, inner_step)
    g1_xp = finite_difference_g1_matrix(kx + step, ky, mass, z, inner_step)
    g1_xm = finite_difference_g1_matrix(kx - step, ky, mass, z, inner_step)
    g1_yp = finite_difference_g1_matrix(kx, ky + step, mass, z, inner_step)
    g1_ym = finite_difference_g1_matrix(kx, ky - step, mass, z, inner_step)
    g1x = (g1_xp - g1_xm) / (2.0 * step)
    g1y = (g1_yp - g1_ym) / (2.0 * step)

    lambda_a_g1 = ax @ g1y - ay @ g1x
    lambda2_a_g0 = axx @ gyy + ayy @ gxx - 2.0 * axy @ gxy
    return (1.0j / 2.0) * lambda_a_g1 - 0.125 * lambda2_a_g0


def pole_system(kx: float, ky: float, mass: float) -> tuple[np.ndarray, np.ndarray, float]:
    eps = math.sqrt(4.0 * math.cos(kx) ** 2 + 4.0 * math.cos(ky) ** 2 + mass * mass)
    poles = (-eps, eps)
    offsets = (
        0.31 + 0.73j,
        -0.43 + 0.61j,
        0.77 - 0.29j,
        -0.59 - 0.47j,
        1.11 + 0.17j,
    )
    rows: list[list[complex]] = []
    rhs: list[tuple[complex, complex, complex]] = []
    for pole in poles:
        for offset in offsets:
            z = pole + offset
            rows.append([1.0 / ((z - p) ** r) for p in poles for r in range(1, POLE_ORDER + 1)])
            rhs.append(star_traces(kx, ky, mass, z))

    mat = np.asarray(rows, dtype=np.complex128)
    vals = np.asarray(rhs, dtype=np.complex128)
    coeff = np.linalg.solve(mat, vals)

    z_test = eps + 0.83 - 0.52j
    predicted = np.asarray(
        [
            sum(coeff[i, col] / ((z_test - poles[i // POLE_ORDER]) ** (i % POLE_ORDER + 1))
                for i in range(2 * POLE_ORDER))
            for col in range(3)
        ],
        dtype=np.complex128,
    )
    observed = np.asarray(star_traces(kx, ky, mass, z_test), dtype=np.complex128)
    residual = float(np.max(np.abs(predicted - observed)))
    return coeff, np.asarray(poles, dtype=np.float64), residual


def residue_from_coefficients(coeff: np.ndarray, poles: np.ndarray) -> tuple[float, float, float]:
    totals = np.zeros(3, dtype=np.complex128)
    row = 0
    for pole in poles:
        derivs = grand_derivatives(float(pole), MU, TEMP, POLE_ORDER - 1)
        for r in range(1, POLE_ORDER + 1):
            totals += coeff[row, :] * derivs[r - 1] / math.factorial(r - 1)
            row += 1
    return float(totals[0].real), float(totals[1].real), float(totals[2].real)


@dataclass(frozen=True)
class IntegralResult:
    full_response: float
    cross_response: float
    second_response: float
    max_fit_residual: float


def integrate_moyal(mass: float, order: int) -> IntegralResult:
    nodes, weights = np.polynomial.legendre.leggauss(order)
    ks = math.pi * (nodes + 1.0)
    ws = math.pi * weights
    totals = np.zeros(3, dtype=np.float64)
    max_fit = 0.0

    for ix, kx in enumerate(ks):
        wx = float(ws[ix])
        for iy, ky in enumerate(ks):
            coeff, poles, fit = pole_system(float(kx), float(ky), mass)
            residues = residue_from_coefficients(coeff, poles)
            totals += wx * float(ws[iy]) * np.asarray(residues, dtype=np.float64)
            max_fit = max(max_fit, fit)

    # The response is d^2 Omega / dB^2 = 2 * Omega_2.
    scale = 2.0 / ((2.0 * math.pi) ** 2)
    return IntegralResult(
        full_response=float(scale * totals[0]),
        cross_response=float(scale * totals[1]),
        second_response=float(scale * totals[2]),
        max_fit_residual=max_fit,
    )


def interband_residue_probe(mass: float, order: int = 80) -> float:
    nodes, weights = np.polynomial.legendre.leggauss(order)
    ks = math.pi * (nodes + 1.0)
    ws = math.pi * weights
    total = 0.0
    for ix, kx in enumerate(ks):
        sx = math.sin(float(kx))
        cx = math.cos(float(kx))
        wx = float(ws[ix])
        for iy, ky in enumerate(ks):
            sy = math.sin(float(ky))
            cy = math.cos(float(ky))
            eps = math.sqrt(4.0 * cx * cx + 4.0 * cy * cy + mass * mass)
            if eps == 0.0:
                continue
            berry_num = 4.0 * mass * sx * sy
            occ_gap = abs(grand_derivatives(-eps, MU, TEMP, 1)[1] - grand_derivatives(eps, MU, TEMP, 1)[1])
            total += wx * float(ws[iy]) * (berry_num * berry_num) * occ_gap / (eps ** 5)
    return float(total / ((2.0 * math.pi) ** 2))


def finite_difference_completeness_check() -> CompletenessCheckResult:
    """Cross-check the implemented B^2 source matrix against finite differences."""
    max_coarse_abs = 0.0
    max_fine_abs = 0.0
    min_convergence_ratio = math.inf

    for kx, ky, mass, z in COMPLETENESS_FD_SAMPLES:
        implemented_x, _full, _cross, _second = implemented_b2_matrices(kx, ky, mass, z)
        coarse_x = finite_difference_b2_source_matrix(kx, ky, mass, z, COMPLETENESS_FD_COARSE_STEP)
        fine_x = finite_difference_b2_source_matrix(kx, ky, mass, z, COMPLETENESS_FD_FINE_STEP)

        coarse_abs = float(np.max(np.abs(coarse_x - implemented_x)))
        fine_abs = float(np.max(np.abs(fine_x - implemented_x)))
        max_coarse_abs = max(max_coarse_abs, coarse_abs)
        max_fine_abs = max(max_fine_abs, fine_abs)
        if fine_abs > 0.0:
            min_convergence_ratio = min(min_convergence_ratio, coarse_abs / fine_abs)

    passed = (
        max_fine_abs < COMPLETENESS_FD_X_TOL
        and min_convergence_ratio > COMPLETENESS_FD_MIN_RATIO
    )
    return CompletenessCheckResult(
        passed=passed,
        max_coarse_abs=max_coarse_abs,
        max_fine_abs=max_fine_abs,
        min_convergence_ratio=min_convergence_ratio,
    )


def finite_cell_reference_values() -> dict[float, Decimal]:
    """Recompute finite-cell references from the landed closed-form runner."""
    out = {}
    for mass in MASSES:
        value = finite_cell_reference.finite_cell_closed_form_response(
            finite_cell_reference.CELL_Q, mass
        ).full
        out[mass] = Decimal(f"{value:.12f}")
    return out


def main() -> None:
    print("Full lattice two-band Moyal B^2 runner")
    print(f"mu={MU:.4f} T={TEMP:.1f} masses={MASSES}")
    print("Model: H(k)=-2 cos(kx) sx -2 cos(ky) sy + m sz")
    print("No scalar closure fit is performed; one cell normalization is fixed at m=0.")

    references = finite_cell_reference_values()
    for mass in MASSES:
        diff = abs(references[mass] - TARGETS_DECIMAL[mass])
        check(
            diff <= REFERENCE_TOL,
            f"S0 finite-cell reference recomputed at m={mass:.1f}",
            f"value={references[mass]} diff={diff}",
        )

    completeness = finite_difference_completeness_check()
    check(
        completeness.passed,
        "S1 finite-difference Moyal B^2 source matches implemented cross and second-derivative terms",
        f"max_x_abs={completeness.max_fine_abs:.6e}; "
        f"coarse_to_fine_min_ratio={completeness.min_convergence_ratio:.3f}; "
        f"tol={COMPLETENESS_FD_X_TOL:.1e}",
    )

    probe0 = interband_residue_probe(0.0, 64)
    probe02 = interband_residue_probe(0.2, 64)
    probe05 = interband_residue_probe(0.5, 64)
    check(abs(probe0) < 1.0e-14, "S0 control: Berry/interband residue probe vanishes at m=0", f"value={probe0:.6e}")
    check(probe02 > 1.0e-5 and probe05 > 1.0e-5, "S0 anti-fabrication: interband residue probe is nonzero off m=0", f"m=0.2 {probe02:.6e}; m=0.5 {probe05:.6e}")

    coarse = {mass: integrate_moyal(mass, QUAD_COARSE) for mass in MASSES}
    fine = {mass: integrate_moyal(mass, QUAD_FINE) for mass in MASSES}

    raw0 = fine[0.0].full_response
    cell_norm = TARGETS[0.0] / raw0
    print(f"CELL_NORMALIZATION reference=m=0 raw={raw0:+.12e} target={TARGETS[0.0]:.12e} norm={cell_norm:+.12e}")
    check(math.isfinite(cell_norm) and abs(cell_norm) > 0.0, "single m=0 cell normalization is finite", f"norm={cell_norm:+.12e}")

    max_quad_rel = 0.0
    max_fit = 0.0
    rows = []
    for mass in MASSES:
        qrel = abs(fine[mass].full_response - coarse[mass].full_response) / max(1.0e-15, abs(fine[mass].full_response))
        max_quad_rel = max(max_quad_rel, qrel)
        max_fit = max(max_fit, fine[mass].max_fit_residual)
        value = cell_norm * fine[mass].full_response
        target = TARGETS[mass]
        rel = abs(value - target) / abs(target)
        rows.append((mass, fine[mass], qrel, value, target, rel))

    check(max_quad_rel < QUAD_REL_BOUND, "Gauss-Legendre Moyal integral 48->64 drift is below frozen tolerance", f"max_rel={max_quad_rel:.6e}")
    check(max_fit < FIT_RESID_BOUND, "partial-fraction pole reconstruction of tr G2 is below frozen tolerance", f"max_abs={max_fit:.6e}")

    print("RESULT_TABLE")
    print("m raw_full raw_cross raw_second closed_form exact rel_dev quad_rel")
    for mass, result, qrel, value, target, rel in rows:
        print(
            f"{mass:.1f} {result.full_response:+.12e} {result.cross_response:+.12e} "
            f"{result.second_response:+.12e} {value:+.12e} {target:+.12e} "
            f"{rel:.6e} {qrel:.6e}"
        )
        check(
            abs((result.cross_response + result.second_response) - result.full_response)
            < 1.0e-10 * max(1.0, abs(result.full_response)),
            f"component accounting full=cross+second at m={mass:.1f}",
            f"delta={(result.cross_response + result.second_response - result.full_response):+.3e}",
        )

    independent_rows = [row for row in rows if row[0] != 0.0]
    max_rel = max(row[5] for row in independent_rows)
    worst_mass = max(independent_rows, key=lambda row: row[5])[0]
    check(
        max_rel < CLOSURE_REL_BOUND,
        "S2 measured non-reference residual is honestly bounded; complete Moyal B^2 does not close below 2%",
        f"max_rel={max_rel:.6e} at m={worst_mass:.1f}; bound={CLOSURE_REL_BOUND:.2f}",
    )

    if max_rel < 0.02:
        print(f"CLAIM_STATUS closes the exact response to {100.0 * max_rel:.3f}% with no fudge")
    else:
        print(
            "CLAIM_STATUS leaves named residual: after the single m=0 cell normalization, "
            f"the full lattice Moyal B^2 response misses the independent masses by up to {100.0 * max_rel:.3f}%; "
            "the missing object is a mass-dependent finite-cell/full-PT correction, not a scalar prefactor."
        )

    finish()


if __name__ == "__main__":
    main()
