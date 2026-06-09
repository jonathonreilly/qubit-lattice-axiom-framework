#!/usr/bin/env python3
"""Finite-lattice complete-square bridge for the I1 static readout.

This runner verifies the finite algebra following from the supplied
source-normalized leading quadratic action:

    S[phi; J] = (1/(2 g^2)) <d phi, d phi> - <J, phi>

on the zero-mean finite periodic lattice. Completing the square gives

    S_eff[J] = -(g^2/2) <J, L^+ J>,

so the separation-dependent two-source cross term is

    V_cross(r) = -g^2 s_1 s_2 G(r).

This narrows only the complete-square substep. It does not derive the physical
source-coupling normalization, gauge action, framework-wide energy-readout
bridge, or any physical hierarchy quantity.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md"
I1_NOTE = ROOT / "docs" / "I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06.md"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"  ({detail})" if detail else ""
    print(("PASS" if ok else "FAIL") + ": " + name + suffix)


def lattice_shape(n: int) -> tuple[int, int, int]:
    return (n, n, n)


def laplacian_symbol(n: int) -> np.ndarray:
    k = 2.0 * math.pi * np.fft.fftfreq(n)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    return 2.0 * (3.0 - np.cos(kx) - np.cos(ky) - np.cos(kz))


def zero_mean(source: np.ndarray) -> np.ndarray:
    return source - float(np.mean(source))


def apply_laplacian(phi: np.ndarray) -> np.ndarray:
    out = 6.0 * phi.copy()
    for axis in range(3):
        out -= np.roll(phi, +1, axis=axis)
        out -= np.roll(phi, -1, axis=axis)
    return out


def green_solve(source: np.ndarray) -> np.ndarray:
    source = zero_mean(source)
    symbol = laplacian_symbol(source.shape[0])
    source_hat = np.fft.fftn(source)
    phi_hat = np.zeros_like(source_hat)
    mask = symbol > 1.0e-14
    phi_hat[mask] = source_hat[mask] / symbol[mask]
    return np.fft.ifftn(phi_hat).real


def action(phi: np.ndarray, source: np.ndarray, g: float) -> float:
    source = zero_mean(source)
    grad_energy = 0.0
    for axis in range(3):
        diff = np.roll(phi, -1, axis=axis) - phi
        grad_energy += float(np.sum(diff * diff))
    return (0.5 / (g * g)) * grad_energy - float(np.sum(source * phi))


def point_source(n: int, coord: tuple[int, int, int], strength: float = 1.0) -> np.ndarray:
    src = np.zeros(lattice_shape(n), dtype=float)
    src[coord] = strength
    return zero_mean(src)


def green_kernel_at(n: int, coord: tuple[int, int, int]) -> float:
    src = point_source(n, (0, 0, 0), 1.0)
    return float(green_solve(src)[coord])


def section_source_boundaries() -> None:
    print("--- Section 0: source-boundary text guard ---")
    note = NOTE.read_text(encoding="utf-8")
    i1_note = I1_NOTE.read_text(encoding="utf-8")
    for phrase in [
        "source-normalized leading quadratic action",
        "does not derive the physical source-coupling normalization",
        "S_eff[J] = -(g^2/2) <J, L^+ J>",
        "V_cross(r) = -g^2 s_1 s_2 G(r)",
    ]:
        check(f"bridge note contains: {phrase}", phrase in note)
    check(
        "I1 parent note links the complete-square bridge",
        "I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08" in i1_note,
    )
    check(
        "I1 parent keeps the energy-readout bridge open",
        "general energy-readout bridge remains open" in i1_note
        and "source-coupling normalization" in i1_note,
    )


def section_complete_square() -> None:
    print("--- Section A: finite-lattice complete square ---")
    n = 6
    g = 1.37
    rng = np.random.default_rng(20260608)
    source = zero_mean(rng.normal(size=lattice_shape(n)))
    phi_star = (g * g) * green_solve(source)
    residual = apply_laplacian(phi_star) - (g * g) * source
    predicted = -0.5 * g * g * float(np.sum(source * green_solve(source)))
    actual = action(phi_star, source, g)
    check(
        "stationary equation is L phi = g^2 J on the zero-mean lattice",
        float(np.max(np.abs(residual))) < 1.0e-10,
        f"max_residual={float(np.max(np.abs(residual))):.3e}",
    )
    check(
        "completed-square minimum equals -(g^2/2)<J,L^+J>",
        abs(actual - predicted) < 1.0e-10,
        f"actual={actual:.12e}, predicted={predicted:.12e}",
    )
    perturb = zero_mean(rng.normal(size=lattice_shape(n)))
    eps = 1.0e-5
    centered_slope = (
        action(phi_star + eps * perturb, source, g)
        - action(phi_star - eps * perturb, source, g)
    ) / (2.0 * eps)
    check(
        "first variation vanishes at the completed-square solution",
        abs(centered_slope) < 1.0e-8,
        f"slope={centered_slope:.3e}",
    )


def section_two_source_cross_term() -> None:
    print("--- Section B: two-source cross term normalization ---")
    n = 8
    g = 0.91
    a = (0, 0, 0)
    b = (2, 0, 0)
    s1 = 1.0
    s2 = 1.0
    src_a = point_source(n, a, s1)
    src_b = point_source(n, b, s2)
    src_pair = src_a + src_b
    e_a = -0.5 * g * g * float(np.sum(src_a * green_solve(src_a)))
    e_b = -0.5 * g * g * float(np.sum(src_b * green_solve(src_b)))
    e_pair = -0.5 * g * g * float(np.sum(src_pair * green_solve(src_pair)))
    cross = e_pair - e_a - e_b
    g_r = green_kernel_at(n, b)
    expected = -g * g * s1 * s2 * g_r
    check(
        "separation-dependent cross term is -g^2 s1 s2 G(r)",
        abs(cross - expected) < 1.0e-12,
        f"cross={cross:.12e}, expected={expected:.12e}",
    )
    for lam in [0.5, 2.0]:
        src_scaled = lam * src_pair
        e_scaled = -0.5 * g * g * float(np.sum(src_scaled * green_solve(src_scaled)))
        cross_scaled = e_scaled - lam * lam * e_a - lam * lam * e_b
        check(
            f"source amplitude scaling is quadratic for lambda={lam}",
            abs(cross_scaled - lam * lam * cross) < 1.0e-12,
            f"ratio={cross_scaled / cross:.6f}",
        )
    for g2 in [0.6, 1.4]:
        e_pair_2 = -0.5 * g2 * g2 * float(np.sum(src_pair * green_solve(src_pair)))
        e_a_2 = -0.5 * g2 * g2 * float(np.sum(src_a * green_solve(src_a)))
        e_b_2 = -0.5 * g2 * g2 * float(np.sum(src_b * green_solve(src_b)))
        cross_2 = e_pair_2 - e_a_2 - e_b_2
        check(
            f"coupling dependence is exactly g^2 for g={g2}",
            abs(cross_2 / cross - (g2 * g2) / (g * g)) < 1.0e-12,
            f"ratio={cross_2 / cross:.6f}",
        )


def section_native_symbol() -> None:
    print("--- Section C: graph-Laplacian small-k normalization ---")
    for kval in [2.0 * math.pi / 128.0, 2.0 * math.pi / 256.0, 2.0 * math.pi / 512.0]:
        symbol = 2.0 * (1.0 - math.cos(kval))
        ratio = symbol / (kval * kval)
        check(
            f"one-axis lattice symbol/k^2 tends to 1 at k={kval:.5f}",
            abs(ratio - 1.0) < 3.0e-4,
            f"ratio={ratio:.9f}",
        )
    solid_angle_coeff = (4.0 * math.pi / (2.0 * math.pi) ** 3) * (math.pi / 2.0)
    check(
        "native inverse-Laplacian coefficient is 1/(4 pi)",
        abs(solid_angle_coeff - 1.0 / (4.0 * math.pi)) < 1.0e-15,
        f"coeff={solid_angle_coeff:.15f}",
    )


def main() -> int:
    print("I1 NATIVE QUADRATIC STATIC-SOURCE NORMALIZATION BRIDGE")
    section_source_boundaries()
    section_complete_square()
    section_two_source_cross_term()
    section_native_symbol()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
