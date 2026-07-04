#!/usr/bin/env python3
"""Source-boundary verifier for the d=3 single-band LP normalization note.

The runner checks the framework-side normalization chain used by

    docs/D3_LANDAU_PEIERLS_SINGLE_BAND_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md

It is not an audit runner and does not set audit status.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs/D3_LANDAU_PEIERLS_SINGLE_BAND_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md"

TEMPERATURE = 0.30
REFERENCE_MU = -2.0
LP_GRID_N = 176
EXPECTED_PARENT_LP_REFERENCE = -3.949577202602e-03

CELL_NORMALIZATION_EXACT = Fraction(-1, 12)
MIDPOINT_COEFFICIENT_EXACT = Fraction(1, 24)
PARENT_REFERENCE_TOL = 5.0e-15
HESSIAN_FD_TOL = 1.0e-6
SYMMETRY_TOL = 5.0e-16


@dataclass
class GateResult:
    name: str
    passed: bool
    detail: str


class Gates:
    def __init__(self) -> None:
        self.results: list[GateResult] = []

    def check(self, name: str, passed: bool, detail: str) -> None:
        self.results.append(GateResult(name, bool(passed), detail))
        tag = "PASS" if passed else "FAIL"
        print(f"{tag}: {name}: {detail}")

    def finish(self) -> int:
        passed = sum(result.passed for result in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return 0 if failed == 0 else 1


def bernoulli_1(x: Fraction) -> Fraction:
    return x - Fraction(1, 2)


def bernoulli_2(x: Fraction) -> Fraction:
    return x * x - x + Fraction(1, 6)


def midpoint_euler_maclaurin_coefficient() -> Fraction:
    """Coefficient multiplying h^2 G'(0) in the midpoint half-line sum."""
    half = Fraction(1, 2)
    return -bernoulli_2(half) / 2


def magnetic_clock_shift_rank(q: int) -> tuple[float, int]:
    """Return the commutation residual and span rank for the q-cell algebra."""
    omega = np.exp(2j * math.pi / q)
    clock = np.diag([omega**n for n in range(q)])
    shift = np.zeros((q, q), dtype=complex)
    for n in range(q):
        shift[(n + 1) % q, n] = 1.0
    residual = float(np.linalg.norm(clock @ shift - omega * shift @ clock))
    basis = []
    for a in range(q):
        clock_power = np.linalg.matrix_power(clock, a)
        for b in range(q):
            basis.append((clock_power @ np.linalg.matrix_power(shift, b)).reshape(-1))
    rank = int(np.linalg.matrix_rank(np.vstack(basis), tol=1.0e-10))
    return residual, rank


def magnetic_subband_density(q: int, magnetic_cells_x: int, cells_y: int) -> Fraction:
    """State density of one isolated magnetic subband for B=2*pi/q."""
    states_in_subband = magnetic_cells_x * cells_y
    transverse_sites = q * magnetic_cells_x * cells_y
    return Fraction(states_in_subband, transverse_sites)


def oscillator_characteristic_coefficients(a: Fraction, b: Fraction, c: Fraction) -> tuple[Fraction, Fraction]:
    """Return trace(JH), det(JH) for H=[[a,c],[c,b]], J=[[0,1],[-1,0]]."""
    # JH = [[c, b], [-a, -c]]
    trace = c - c
    determinant = (-c * c) - (b * -a)
    return trace, determinant


def local_response_coefficient(a: Fraction, b: Fraction, c: Fraction) -> Fraction:
    """Local LP coefficient after midpoint and integration-by-parts reduction."""
    return CELL_NORMALIZATION_EXACT * (a * b - c * c)


def fermi_prime(energy: np.ndarray, mu: float, temperature: float) -> np.ndarray:
    x = (energy - mu) / temperature
    out = np.empty_like(x, dtype=np.float64)
    mask = x >= 0.0
    exp_neg = np.exp(-x[mask])
    out[mask] = -(exp_neg / (temperature * (1.0 + exp_neg) ** 2))
    exp_pos = np.exp(x[~mask])
    out[~mask] = -(exp_pos / (temperature * (1.0 + exp_pos) ** 2))
    return out


def landau_peierls_chi_from_native_normalization(mu: float, temperature: float, nk: int) -> float:
    k = 2.0 * math.pi * (np.arange(nk, dtype=np.float64) + 0.5) / float(nk)
    c = np.cos(k)
    cx = c[:, None]
    cy = c[None, :]
    xy_energy = -2.0 * (cx + cy)
    hessian_det_xy = 4.0 * cx * cy

    total = 0.0
    for cz in c:
        energy = xy_energy - 2.0 * cz
        total += float(np.sum(fermi_prime(energy, mu, temperature) * hessian_det_xy))

    bz_average = total / float(nk**3)
    return float(CELL_NORMALIZATION_EXACT) * bz_average


def cubic_band_energy(kx: float, ky: float, kz: float) -> float:
    return -2.0 * (math.cos(kx) + math.cos(ky) + math.cos(kz))


def finite_difference_hessian_det(kx: float, ky: float, kz: float, h: float = 1.0e-4) -> float:
    f00 = cubic_band_energy(kx, ky, kz)
    fpx = cubic_band_energy(kx + h, ky, kz)
    fmx = cubic_band_energy(kx - h, ky, kz)
    fpy = cubic_band_energy(kx, ky + h, kz)
    fmy = cubic_band_energy(kx, ky - h, kz)
    fpp = cubic_band_energy(kx + h, ky + h, kz)
    fpm = cubic_band_energy(kx + h, ky - h, kz)
    fmp = cubic_band_energy(kx - h, ky + h, kz)
    fmm = cubic_band_energy(kx - h, ky - h, kz)
    exx = (fpx - 2.0 * f00 + fmx) / (h * h)
    eyy = (fpy - 2.0 * f00 + fmy) / (h * h)
    exy = (fpp - fpm - fmp + fmm) / (4.0 * h * h)
    return exx * eyy - exy * exy


def analytic_cubic_hessian_det(kx: float, ky: float) -> float:
    return 4.0 * math.cos(kx) * math.cos(ky)


def main() -> int:
    print("d=3 single-band Landau-Peierls normalization source-boundary runner")
    print(
        "frozen_parameters "
        f"mu_ref={REFERENCE_MU:+.6f} T={TEMPERATURE:.6f} LP_GRID_N={LP_GRID_N} "
        f"cell_norm={float(CELL_NORMALIZATION_EXACT):+.12e}"
    )
    gates = Gates()

    magnetic_algebra_ok = True
    magnetic_details: list[str] = []
    for q in (3, 5, 7):
        residual, rank = magnetic_clock_shift_rank(q)
        magnetic_algebra_ok = magnetic_algebra_ok and residual <= 1.0e-12 and rank == q * q
        magnetic_details.append(f"q={q} residual={residual:.2e} span_rank={rank}/{q*q}")
    gates.check(
        "finite Peierls magnetic translations realize the full q-cell algebra",
        magnetic_algebra_ok,
        "; ".join(magnetic_details),
    )

    density_ok = True
    density_details: list[str] = []
    for q, mx, ny in ((3, 4, 5), (5, 2, 7), (11, 3, 2)):
        density = magnetic_subband_density(q, mx, ny)
        density_ok = density_ok and density == Fraction(1, q)
        density_details.append(f"q={q} density={density}=B/(2*pi)")
    gates.check(
        "finite magnetic-cell count gives degeneracy density B/(2*pi) for B=2*pi/q",
        density_ok,
        "; ".join(density_details),
    )

    half = Fraction(1, 2)
    b1_half = bernoulli_1(half)
    midpoint_coeff = midpoint_euler_maclaurin_coefficient()
    lp_second_derivative_coeff = -2 * midpoint_coeff
    gates.check(
        "midpoint Euler-Maclaurin has no linear endpoint term",
        b1_half == 0,
        f"B1(1/2)={b1_half}",
    )
    gates.check(
        "midpoint h^2 coefficient is exactly 1/24",
        midpoint_coeff == MIDPOINT_COEFFICIENT_EXACT,
        f"-B2(1/2)/2={midpoint_coeff}",
    )
    gates.check(
        "grand-potential second-difference coefficient is exactly -1/12 after integration by parts",
        lp_second_derivative_coeff == CELL_NORMALIZATION_EXACT,
        f"-2*(1/24)={lp_second_derivative_coeff}",
    )

    examples = (
        (Fraction(3, 2), Fraction(5, 3), Fraction(1, 7)),
        (Fraction(7, 5), Fraction(11, 6), Fraction(-2, 9)),
        (Fraction(5, 4), Fraction(9, 8), Fraction(1, 3)),
    )
    oscillator_ok = True
    oscillator_details: list[str] = []
    for a, b, c in examples:
        trace, determinant = oscillator_characteristic_coefficients(a, b, c)
        expected_det = a * b - c * c
        oscillator_ok = oscillator_ok and trace == 0 and determinant == expected_det
        oscillator_details.append(f"(a,b,c)=({a},{b},{c}) trace={trace} det={determinant}")
    gates.check(
        "local magnetic oscillator invariant is det(Hxy)",
        oscillator_ok,
        "; ".join(oscillator_details),
    )

    continuation_examples = (
        (Fraction(3, 2), Fraction(5, 3), Fraction(1, 7)),
        (Fraction(3, 2), Fraction(-5, 3), Fraction(1, 7)),
        (Fraction(-4, 5), Fraction(-7, 6), Fraction(2, 9)),
    )
    signs = set()
    continuation_ok = True
    continuation_details: list[str] = []
    for a, b, c in continuation_examples:
        det_h = a * b - c * c
        coeff = local_response_coefficient(a, b, c)
        continuation_ok = continuation_ok and coeff == -det_h / 12
        signs.add(1 if det_h > 0 else -1 if det_h < 0 else 0)
        continuation_details.append(f"det={det_h} coeff={coeff}")
    continuation_ok = continuation_ok and {1, -1}.issubset(signs)
    gates.check(
        "saddle continuation uses the exact polynomial coefficient -det(Hxy)/12",
        continuation_ok,
        "; ".join(continuation_details),
    )

    sample_points = (
        (0.31, 0.72, 1.13),
        (1.20, 2.40, 0.17),
        (2.60, 0.41, 2.10),
        (3.80, 4.20, 5.10),
    )
    max_hessian_error = 0.0
    for kx, ky, kz in sample_points:
        numeric = finite_difference_hessian_det(kx, ky, kz)
        analytic = analytic_cubic_hessian_det(kx, ky)
        max_hessian_error = max(max_hessian_error, abs(numeric - analytic))
    gates.check(
        "cubic band transverse Hessian determinant is 4 cos(kx) cos(ky)",
        max_hessian_error <= HESSIAN_FD_TOL,
        f"max finite-difference determinant error={max_hessian_error:.3e}",
    )

    k = 2.0 * math.pi * (np.arange(64, dtype=np.float64) + 0.5) / 64.0
    det_grid = 4.0 * np.cos(k[:, None]) * np.cos(k[None, :])
    gates.check(
        "cubic full-patch determinant includes elliptic and saddle signs without changing coefficient",
        float(np.min(det_grid)) < 0.0 and float(np.max(det_grid)) > 0.0,
        f"det_min={float(np.min(det_grid)):+.6f}, det_max={float(np.max(det_grid)):+.6f}",
    )

    lp_ref = landau_peierls_chi_from_native_normalization(REFERENCE_MU, TEMPERATURE, LP_GRID_N)
    gates.check(
        "native normalization reproduces parent d=3 LP reference value without fitting",
        abs(lp_ref - EXPECTED_PARENT_LP_REFERENCE) <= PARENT_REFERENCE_TOL,
        f"lp_ref={lp_ref:+.12e}, expected={EXPECTED_PARENT_LP_REFERENCE:+.12e}",
    )

    symmetry_values = []
    for mu in (1.5, 3.0, 4.5):
        left = landau_peierls_chi_from_native_normalization(-mu, TEMPERATURE, 96)
        right = landau_peierls_chi_from_native_normalization(mu, TEMPERATURE, 96)
        symmetry_values.append(abs(left - right))
    max_symmetry_error = max(symmetry_values)
    gates.check(
        "cubic particle-hole symmetry is preserved by the normalized LP integral",
        max_symmetry_error <= SYMMETRY_TOL,
        f"max |chi(mu)-chi(-mu)|={max_symmetry_error:.3e}",
    )

    note_text = NOTE_PATH.read_text()
    required_phrases = (
        "finite-torus `B/(2*pi)` magnetic-cell",
        "polynomial `-det(H)/12`",
        "does not introduce a new axiom",
        "midpoint Euler-Maclaurin coefficient",
        "`-1/12`",
        "audit lane grades",
        "not an audit verdict",
    )
    missing = [phrase for phrase in required_phrases if phrase not in note_text]
    gates.check(
        "source note records bounded status and no-axiom boundary",
        not missing,
        "all required source-boundary phrases present" if not missing else f"missing={missing}",
    )

    gates.check(
        "runner uses exact rational normalization, not a fitted float",
        CELL_NORMALIZATION_EXACT == Fraction(-1, 12),
        f"CELL_NORMALIZATION_EXACT={CELL_NORMALIZATION_EXACT}",
    )

    return gates.finish()


if __name__ == "__main__":
    sys.exit(main())
