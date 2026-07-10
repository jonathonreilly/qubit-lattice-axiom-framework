#!/usr/bin/env python3
"""Check periodic-lattice Laplacian, compact zero-mode, and Yukawa formulas.

The implemented class is L_mu = -Delta + mu^2.  The runner checks its Fourier
symbol, its single compact zero mode at mu=0, mean-subtracted inversion, finite
Green-function windows, and the exact lattice Yukawa pole relation.  It does
not classify broader higher-derivative laws or attach a physical source or
field interpretation.  Companion note:
SOURCE_FIELD_STATIC_LAW_CLASSIFICATION_BOUNDED_NOTE_2026-07-08.md.
"""

from __future__ import annotations

import math
import sys
import time

import numpy as np


CHECK_TOL = 1.0e-12
sys.dont_write_bytecode = True


def laplacian_symbol(shape: tuple[int, ...]) -> np.ndarray:
    """Symbol of -Delta for the nearest-neighbor periodic lattice."""
    grids = np.meshgrid(*[2.0 * np.pi * np.arange(length) / length for length in shape], indexing="ij")
    lam = np.zeros(shape, dtype=np.float64)
    for grid in grids:
        lam += 2.0 * (1.0 - np.cos(grid))
    return lam


def solve_fft(shape: tuple[int, ...], rho: np.ndarray, mu: float) -> np.ndarray:
    lam = laplacian_symbol(shape) + mu * mu
    rho_hat = np.fft.fftn(rho)
    phi_hat = np.zeros_like(rho_hat, dtype=np.complex128)
    if mu == 0.0:
        mask = lam > 0.0
        phi_hat[mask] = rho_hat[mask] / lam[mask]
        phi_hat[~mask] = 0.0
    else:
        phi_hat = rho_hat / lam
    return np.fft.ifftn(phi_hat).real


def apply_l_mu_fft(phi: np.ndarray, mu: float) -> np.ndarray:
    lam = laplacian_symbol(phi.shape) + mu * mu
    return np.fft.ifftn(lam * np.fft.fftn(phi)).real


def periodic_distances(shape: tuple[int, ...]) -> tuple[np.ndarray, ...]:
    grids = np.meshgrid(*[np.arange(length) for length in shape], indexing="ij")
    out = []
    for grid, length in zip(grids, shape):
        out.append(np.minimum(grid, length - grid).astype(np.float64))
    return tuple(out)


def leg1_kernel_and_subtraction() -> tuple[bool, str]:
    shapes = ((64,), (32, 32), (16, 16, 16))
    mu_positive = 0.3
    kernel_parts: list[str] = []
    max_subtracted_residual = 0.0
    max_massive_residual = 0.0
    max_inconsistency = 0.0
    ok = True

    for shape in shapes:
        lam = laplacian_symbol(shape)
        flat = np.sort(lam.ravel())
        zero_mult = int(np.count_nonzero(lam == 0.0))
        gap = float(flat[1])
        ok = ok and zero_mult == 1 and gap > 0.0

        dim_label = f"d{len(shape)}"
        kernel_parts.append(f"{dim_label}:zero_mult={zero_mult},gap={gap:.6g}")

        rho = np.zeros(shape, dtype=np.float64)
        rho[(0,) * len(shape)] = 1.0
        rho_hat = np.fft.fftn(rho)
        inconsistency = float(abs(rho_hat[(0,) * len(shape)]))
        max_inconsistency = max(max_inconsistency, inconsistency)
        ok = ok and inconsistency == 1.0

        rho_sub = rho - np.mean(rho)
        phi_sub = solve_fft(shape, rho_sub, 0.0)
        sub_res = float(np.max(np.abs(apply_l_mu_fft(phi_sub, 0.0) - rho_sub)))
        max_subtracted_residual = max(max_subtracted_residual, sub_res)

        phi_massive = solve_fft(shape, rho, mu_positive)
        massive_res = float(np.max(np.abs(apply_l_mu_fft(phi_massive, mu_positive) - rho)))
        max_massive_residual = max(max_massive_residual, massive_res)
        ok = ok and sub_res <= CHECK_TOL and massive_res <= CHECK_TOL

    # Constants are the exact zero mode of -Delta; adding mu^2 breaks the shift.
    ones = np.ones((64,), dtype=np.float64)
    shift_l0 = float(np.max(np.abs(apply_l_mu_fft(ones, 0.0))))
    shift_lmu = float(np.mean(apply_l_mu_fft(ones, mu_positive)))
    ok = ok and shift_l0 == 0.0 and abs(shift_lmu - mu_positive * mu_positive) <= CHECK_TOL

    detail = (
        f"KERNELS+SUBTRACTION CHECK-01/02 {';'.join(kernel_parts)} shift(L0*1={shift_l0:.1e},"
        f"Lmu*1={shift_lmu:.6g}) SUBTRACTION k0_res={max_inconsistency:.1f},"
        f"sub_res={max_subtracted_residual:.1e},massive_res={max_massive_residual:.1e}"
    )
    return ok, detail


def radial_shell_profile(phi: np.ndarray, radii: np.ndarray, half_width: float) -> np.ndarray:
    coords = periodic_distances(phi.shape)
    dist2 = np.zeros(phi.shape, dtype=np.float64)
    for coord in coords:
        dist2 += coord * coord
    dist = np.sqrt(dist2)
    values = []
    for radius in radii:
        mask = np.abs(dist - radius) <= half_width
        if not np.any(mask):
            raise RuntimeError(f"empty radial shell at r={radius}")
        values.append(float(np.mean(phi[mask])))
    return np.array(values, dtype=np.float64)


def d3_green_profile(length: int) -> tuple[np.ndarray, np.ndarray]:
    shape = (length, length, length)
    rho = np.zeros(shape, dtype=np.float64)
    rho[0, 0, 0] = 1.0
    rho -= np.mean(rho)
    phi = solve_fft(shape, rho, 0.0)
    radii = np.arange(2, 7, dtype=np.float64)
    return radii, radial_shell_profile(phi, radii, half_width=0.4)


def leg2_newtonian_window_and_d1() -> tuple[bool, str]:
    radii16, profile16 = d3_green_profile(16)
    radii24, profile24 = d3_green_profile(24)
    continuum = 1.0 / (4.0 * np.pi * radii16)

    # The compact Green's function is mean-zero, so the local 1/r comparison has
    # one fitted additive offset.  The amplitude c is fixed to c=1.
    gate_slice = slice(0, 4)  # r = 2,3,4,5
    offset16 = float(np.mean(profile16[gate_slice] - continuum[gate_slice]))
    offset24 = float(np.mean(profile24[gate_slice] - continuum[gate_slice]))
    rel16 = np.abs(profile16 - offset16 - continuum) / continuum
    rel24 = np.abs(profile24 - offset24 - continuum) / continuum
    window_ok = bool(np.max(rel16[gate_slice]) <= 0.08 and np.all(rel24[gate_slice] < rel16[gate_slice]))

    length = 64
    rho = np.zeros((length,), dtype=np.float64)
    rho[0] = 1.0
    rho -= np.mean(rho)
    phi = solve_fft((length,), rho, 0.0)
    x = np.arange(length, dtype=np.float64)
    dist = np.minimum(x, length - x)
    # For d != 0 on the ring, -Delta(-d/2 + d^2/(2L)) = -1/L; at d=0
    # the slope jump contributes the missing unit source.  The d^2/(2L)
    # term is exactly the uniform background-subtraction compensation.
    exact_without_const = -0.5 * dist + (dist * dist) / (2.0 * length)
    const = float(np.mean(phi - exact_without_const))
    d1_max_abs = float(np.max(np.abs(phi - (exact_without_const + const))))
    d1_ok = d1_max_abs <= 1.0e-10

    rel16_text = ",".join(f"r{int(r)}:{v:.3g}" for r, v in zip(radii16, rel16))
    rel24_text = ",".join(f"r{int(r)}:{v:.3g}" for r, v in zip(radii24, rel24))
    detail = (
        f"WINDOW CHECK-03/04 d3_rel16=[{rel16_text}] d3_rel24=[{rel24_text}] "
        f"d1_ring_max={d1_max_abs:.1e} SPEC-NOTE d3_mean_zero_offset_fit,"
        f"d1_G=-|x|/2+x^2/(2L)+const"
    )
    return window_ok and d1_ok, detail


def yukawa_axis_fit(mu: float, length: int = 64) -> tuple[float, float, float]:
    shape = (length, length, length)
    rho = np.zeros(shape, dtype=np.float64)
    rho[0, 0, 0] = 1.0
    phi = solve_fft(shape, rho, mu)
    radii = np.arange(3, 9, dtype=np.float64)
    axis_values = np.array([phi[int(radius), 0, 0] for radius in radii], dtype=np.float64)
    if np.any(axis_values <= 0.0):
        raise RuntimeError("nonpositive Yukawa axis value")

    # The lattice pole in the axis direction obeys
    # mu^2 + 2(1 - cosh kappa) = 0, hence
    # 2(cosh(1/xi) - 1) = mu^2 and xi = 1 / (2 asinh(mu/2)).
    # The b/r^2 term absorbs short-distance lattice prefactor curvature while
    # leaving the fitted exponential range as the reported quantity.
    design = np.column_stack([np.ones_like(radii), -radii, 1.0 / (radii * radii)])
    coeff, *_ = np.linalg.lstsq(design, np.log(radii * axis_values), rcond=None)
    kappa_fit = float(coeff[1])
    xi_fit = 1.0 / kappa_fit
    xi_exact = 1.0 / math.acosh(1.0 + 0.5 * mu * mu)
    rel = abs(xi_fit - xi_exact) / xi_exact
    return xi_fit, xi_exact, rel


def leg2_yukawa() -> tuple[bool, str]:
    mu_positive = 0.3
    shift_lmu = mu_positive * mu_positive
    parts = []
    ok = True
    for mu in (0.2, 0.5):
        xi_fit, xi_exact, rel = yukawa_axis_fit(mu)
        ok = ok and rel <= 0.02
        parts.append(f"mu={mu}:xi_fit={xi_fit:.5g},xi_exact={xi_exact:.5g},rel={rel:.3g}")
    detail = (
        "YUKAWA CHECK-05 "
        + ";".join(parts)
        + f" shift_broken_Lmu1={shift_lmu:.6g} SPEC-NOTE xi=1/(2asinh(mu/2)),fit=log(rG)+b/r^2"
    )
    return ok, detail


def main() -> int:
    started = time.time()
    ok1, line1 = leg1_kernel_and_subtraction()
    ok_window, line2 = leg2_newtonian_window_and_d1()
    ok_yukawa, line3 = leg2_yukawa()
    passed = ok1 and ok_window and ok_yukawa
    verdict = "PASS" if passed else "MACHINERY-FAIL"
    flags = [
        "compact-zero-mode-and-subtraction" if ok1 else "zero-mode-check-failed",
        "finite-green-windows" if ok_window else "green-window-check-failed",
        "lattice-yukawa-range" if ok_yukawa else "yukawa-check-failed",
    ]
    elapsed = time.time() - started

    print(line1)
    print(line2)
    print(line3)
    print(f"TOTAL {verdict} flags={','.join(flags)} elapsed={elapsed:.2f}s")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
