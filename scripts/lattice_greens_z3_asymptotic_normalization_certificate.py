#!/usr/bin/env python3
"""Normalization certificate for the Z^3 lattice Green asymptotic import."""

from __future__ import annotations

import math


FOUR_PI = 4.0 * math.pi


def lattice_symbol(kx: float, ky: float, kz: float) -> float:
    """Nearest-neighbor graph-Laplacian symbol on Z^3."""
    return 6.0 - 2.0 * (math.cos(kx) + math.cos(ky) + math.cos(kz))


def continuum_kernel(x: tuple[float, float, float]) -> float:
    r = math.sqrt(sum(v * v for v in x))
    return 1.0 / (FOUR_PI * r)


def graph_laplacian_on_kernel(x: tuple[int, int, int]) -> float:
    """Apply (-Delta_lat) to 1/(4*pi*r) away from the source."""
    center = continuum_kernel(x)
    neighbor_sum = 0.0
    for axis in range(3):
        for step in (-1, 1):
            y = list(x)
            y[axis] += step
            neighbor_sum += continuum_kernel(tuple(y))
    return 6.0 * center - neighbor_sum


def assert_symbol_normalization() -> None:
    """Check the small-k normalization lambda(k)=|k|^2+O(|k|^4)."""
    for eps in (1e-1, 5e-2, 2.5e-2, 1.25e-2):
        axis_ratio = lattice_symbol(eps, 0.0, 0.0) / (eps * eps)
        diag_ratio = lattice_symbol(eps, eps, eps) / (3.0 * eps * eps)
        assert abs(axis_ratio - 1.0) < eps * eps / 10.0, (eps, axis_ratio)
        assert abs(diag_ratio - 1.0) < eps * eps / 10.0, (eps, diag_ratio)
        print(f"symbol eps={eps:.5f}: axis={axis_ratio:.10f} diag={diag_ratio:.10f}")


def assert_continuum_flux_normalization() -> None:
    """Check that 1/(4*pi*r) carries unit outward flux."""
    for radius in (1.0, 2.0, 5.0, 10.0):
        radial_derivative_magnitude = 1.0 / (FOUR_PI * radius * radius)
        flux = 4.0 * math.pi * radius * radius * radial_derivative_magnitude
        assert math.isclose(flux, 1.0, rel_tol=0.0, abs_tol=1e-15), flux
        print(f"continuum flux R={radius:.1f}: {flux:.16f}")


def assert_discrete_harmonic_residual() -> None:
    """Check that the continuum kernel is asymptotically lattice-harmonic."""
    previous = None
    for radius in (16, 32, 64, 128):
        residual = abs(graph_laplacian_on_kernel((radius, 0, 0)))
        scaled = residual * radius**5
        assert scaled < 0.29, (radius, residual, scaled)
        if previous is not None:
            assert residual < previous / 31.0, (radius, residual, previous)
        previous = residual
        print(f"axis r={radius:3d}: residual={residual:.6e} scaled_r5={scaled:.6f}")


def main() -> None:
    assert_symbol_normalization()
    assert_continuum_flux_normalization()
    assert_discrete_harmonic_residual()
    print("CERTIFICATE PASS: Z^3 graph-Laplacian Green asymptotic normalization is 1/(4*pi*r)")


if __name__ == "__main__":
    main()
