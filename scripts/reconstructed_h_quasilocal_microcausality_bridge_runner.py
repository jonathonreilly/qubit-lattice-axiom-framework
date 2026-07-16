#!/usr/bin/env python3
"""Verify the fixed-mass one-particle log-transfer contour statement.

This runner deliberately does not certify a Lieb-Robinson bound or a causal
cone. It separates the one-particle contraction spectrum from the full Fock
spectrum, checks H_1(p) = E_d(p) / a_tau, and verifies the one-coordinate
contour shift behind the axis-kernel exponential bound.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "RECONSTRUCTED_H_QUASILOCAL_FROM_ANALYTIC_DISPERSION_"
    "MICROCAUSALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md"
)

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"  | {detail}" if detail else ""
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{suffix}")
    return ok


def energy(momentum: np.ndarray, mass: float) -> np.ndarray:
    """E_d(p) for an array whose final axis indexes momentum components."""
    p = np.asarray(momentum)
    return np.arcsinh(np.sqrt(mass * mass + np.sum(np.sin(p) ** 2, axis=-1)))


def source_boundary_checks() -> None:
    text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    required = [
        "**Claim type:** bounded_theorem",
        "bounded one-particle fixed-mass contour support",
        "This interval is **not** the full Fock spectrum",
        "E_d(p) / a_tau",
        "one-coordinate strip",
        "does not prove a Lieb-Robinson bound",
        "does not claim a strict or sharp light cone",
        "does not assert a general-dimension gapless power-law exponent",
    ]
    check("source note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    check(
        "source note states the narrowed one-particle boundary and open bridges",
        all(marker in text for marker in required),
        f"{sum(marker in text for marker in required)}/{len(required)} markers",
    )
    forbidden = [
        "H = E(p) >= 0",
        "H = E(p) ≥ 0",
        "finite LR-cone diagnostic v_LR",
        "H(x) ~ x^-4",
        "H(x) ~ x^{−4}",
    ]
    check(
        "withdrawn unit, LR-velocity, and gapless-exponent claims are absent",
        all(marker not in text for marker in forbidden),
    )


def spectrum_split_checks() -> None:
    mass = 0.3
    dimension = 3
    grid = np.linspace(-np.pi, np.pi, 19, endpoint=False)
    p1, p2, p3 = np.meshgrid(grid, grid, grid, indexing="ij")
    momenta = np.stack([p1, p2, p3], axis=-1)
    energies = energy(momenta, mass)
    e_min = float(np.arcsinh(mass))
    e_max = float(np.arcsinh(np.sqrt(mass * mass + dimension)))
    contractions = np.exp(-2.0 * energies)
    check(
        "one-particle contraction spectrum lies in the analytic interval",
        float(contractions.min()) >= np.exp(-2.0 * e_max) - 1e-12
        and float(contractions.max()) <= np.exp(-2.0 * e_min) + 1e-12,
        f"sample=[{contractions.min():.6f}, {contractions.max():.6f}]",
    )

    sample_energies = np.array([e_min, float(energy(np.array([0.4, 0.0, 0.0]), mass)), e_max])
    occupations = list(product((0, 1), repeat=len(sample_energies)))
    fock_spectrum = np.array(
        [np.exp(-2.0 * np.dot(np.array(n, dtype=float), sample_energies)) for n in occupations]
    )
    one_particle = np.exp(-2.0 * sample_energies)
    multiparticle = np.array(
        [value for n, value in zip(occupations, fock_spectrum) if sum(n) >= 2]
    )
    check(
        "full Fock spectrum contains the vacuum eigenvalue 1",
        np.isclose(fock_spectrum.max(), 1.0) and occupations[int(np.argmax(fock_spectrum))] == (0, 0, 0),
    )
    check(
        "multiparticle products extend below the one-particle interval",
        float(multiparticle.min()) < float(one_particle.min()),
        f"multi_min={multiparticle.min():.6e}, one_min={one_particle.min():.6e}",
    )


def unit_checks() -> None:
    p = np.array([0.37, -0.21, 0.48])
    e = float(energy(p, 0.3))
    values = []
    ok = True
    for a_tau in (0.5, 1.0, 2.0):
        h_one = e / a_tau
        values.append(h_one)
        ok = ok and abs(a_tau * h_one - e) < 1e-14
    check(
        "one-particle Hamiltonian eigenvalue is E_d(p)/a_tau",
        ok and values[0] > values[1] > values[2],
        ", ".join(f"a_tau={a}: H1={e/a:.6f}" for a in (0.5, 1.0, 2.0)),
    )


def strip_checks() -> None:
    details: list[str] = []
    ok = True
    identity_ok = True
    for mass in (0.1, 0.3, 1.0):
        rho = 0.8 * float(np.arcsinh(mass))
        lower = mass * mass - np.sinh(rho) ** 2
        r_zero_height = float(np.arcsinh(mass))
        r_minus_one_height = float(np.arcsinh(np.sqrt(mass * mass + 1.0)))
        xs = np.linspace(-np.pi, np.pi, 513, endpoint=False)
        ys = np.linspace(-rho, rho, 17)
        z = xs[:, None] + 1j * ys[None, :]
        radicand = mass * mass + np.sin(z) ** 2
        exact_real = (
            mass * mass
            + np.sin(xs[:, None]) ** 2 * np.cosh(2.0 * ys[None, :])
            - np.sinh(ys[None, :]) ** 2
        )
        sampled_min = float(np.min(radicand.real))
        identity_ok = identity_ok and float(np.max(np.abs(radicand.real - exact_real))) < 1e-12
        case_ok = (
            lower > 0
            and sampled_min >= lower - 1e-12
            and rho < r_zero_height < r_minus_one_height
        )
        ok = ok and case_ok
        details.append(
            f"m={mass}: rho={rho:.5f}, lower={lower:.3e}, sampled_min={sampled_min:.3e}"
        )
    check(
        "Re sin^2(x+i y) = sin^2(x) cosh(2y) - sinh^2(y)",
        identity_ok,
    )
    check(
        "one-coordinate strip stays in Re R > 0 before the R=0 and R=-1 branch heights",
        ok,
        "; ".join(details),
    )


def contour_identity_checks() -> None:
    mass = 0.3
    a_tau = 1.7
    rho = 0.5 * float(np.arcsinh(mass))
    count = 80
    grid = 2.0 * np.pi * np.arange(count) / count
    p1, p2, p3 = np.meshgrid(grid, grid, grid, indexing="ij")
    real_momenta = np.stack([p1, p2, p3], axis=-1)
    shifted_momenta = real_momenta.astype(complex)
    shifted_momenta[..., 0] += 1j * rho
    e_real = energy(real_momenta, mass)
    e_shift = energy(shifted_momenta, mass)
    errors: list[float] = []
    scale_errors: list[float] = []
    for n in (2, 4, 6):
        phase = np.exp(1j * n * p1)
        h_real = np.mean(e_real * phase) / a_tau
        h_shift = np.exp(-rho * n) * np.mean(e_shift * phase) / a_tau
        errors.append(float(abs(h_real - h_shift)))
        scale_errors.append(float(abs((a_tau * h_real) - np.mean(e_real * phase))))
    check(
        "shifted one-coordinate contour reproduces the axis Fourier coefficients",
        max(errors) < 1e-11,
        f"max_abs_error={max(errors):.3e}, rho={rho:.6f}",
    )
    check(
        "axis kernel carries only the overall 1/a_tau energy scale",
        max(scale_errors) < 1e-14,
        f"max_scale_error={max(scale_errors):.3e}",
    )


def main() -> int:
    global PASS, FAIL
    PASS = 0
    FAIL = 0
    print("FIXED-MASS ONE-PARTICLE LOG-TRANSFER CONTOUR CHECK")
    print("=" * 72)
    print("Scope: free U=1; one-particle spectrum and one-coordinate axis kernel.")
    print()
    source_boundary_checks()
    spectrum_split_checks()
    unit_checks()
    strip_checks()
    contour_identity_checks()
    print()
    print("Open: Fock interaction decomposition, quasilocal LR composition, exact causal relation,")
    print("      record-formation event order, and continuum/manifold interface.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
