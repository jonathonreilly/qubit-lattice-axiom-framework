#!/usr/bin/env python3
"""Bounded Bogoliubov / CMW infrared certificate.

This runner supports MERMIN_WAGNER_BOGOLIUBOV_TEXTBOOK_IMPORT_NOTE_2026-05-18.
It does not import a textbook theorem as executable evidence. It checks the
finite Gibbs-state Bogoliubov inequality and the lattice infrared mechanism
used by the Mermin-Wagner/Hohenberg finite-temperature argument on Z^d.
"""

from __future__ import annotations

import math
from itertools import product

import numpy as np


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def gibbs_state(hamiltonian: np.ndarray, beta: float) -> np.ndarray:
    evals, evecs = np.linalg.eigh(hamiltonian)
    weights = np.exp(-beta * evals)
    diagonal = np.diag(weights / weights.sum())
    return evecs @ diagonal @ evecs.conj().T


def thermal_expectation(rho: np.ndarray, op: np.ndarray) -> complex:
    return np.trace(rho @ op)


def bogoliubov_trial(seed: int) -> tuple[float, float, float]:
    """Check |<[C,A]>|^2 <= beta/2 <{A,A^dagger}> <[[C,H],C^dagger]>."""

    rng = np.random.default_rng(seed)
    beta = 0.8
    energies = np.array([0.1, 0.7, 1.4, 2.2], dtype=float)
    h = np.diag(energies)
    rho = gibbs_state(h, beta)
    a = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    c = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))

    lhs = abs(thermal_expectation(rho, comm(c, a))) ** 2
    anti = thermal_expectation(rho, a @ a.conj().T + a.conj().T @ a).real
    double = thermal_expectation(rho, comm(comm(c, h), c.conj().T)).real
    rhs = beta * anti * double / 2.0
    margin = rhs - lhs
    return lhs, rhs, margin


def dispersion(k_vec: tuple[float, ...]) -> float:
    """Lattice Goldstone dispersion E_k = 2 sum_mu (1 - cos k_mu)."""

    return 2.0 * sum(1.0 - math.cos(k) for k in k_vec)


def ir_sum(length: int, dim: int) -> float:
    volume = length**dim
    total = 0.0
    for mode in product(range(length), repeat=dim):
        if all(n == 0 for n in mode):
            continue
        k_vec = tuple(2.0 * math.pi * n / length for n in mode)
        total += 1.0 / dispersion(k_vec)
    return total / volume


def exact_ir_sum_1d(length: int) -> float:
    """Exact identity: L^-1 sum_{n=1}^{L-1} [4 sin^2(pi n/L)]^-1."""

    return (length * length - 1.0) / (12.0 * length)


def main() -> int:
    print("=" * 78)
    print("BOUNDED BOGOLIUBOV / CMW INFRARED CERTIFICATE")
    print("=" * 78)

    print("\nPART A: finite Gibbs-state Bogoliubov inequality")
    bog_ok = True
    for seed in range(6):
        lhs, rhs, margin = bogoliubov_trial(seed)
        ok = margin >= -1e-10
        assert margin >= -1e-10
        bog_ok &= ok
        print(
            f"  seed={seed}: lhs={lhs:.6e} rhs={rhs:.6e} "
            f"margin={margin:.6e} [{'PASS' if ok else 'FAIL'}]"
        )

    print("\nPART B: one-dimensional IR sum exact identity")
    id_ok = True
    for length in [8, 16, 32, 64, 128]:
        direct = ir_sum(length, 1)
        exact = exact_ir_sum_1d(length)
        ok = abs(direct - exact) < 1e-12
        assert abs(direct - exact) < 1e-12
        id_ok &= ok
        print(
            f"  L={length:3d}: direct={direct:.9f} exact={exact:.9f} "
            f"I_1/L={direct/length:.9f} [{'PASS' if ok else 'FAIL'}]"
        )

    print("\nPART C: two-dimensional logarithmic IR growth")
    lengths_2d = [8, 16, 32, 64, 96, 128]
    vals_2d = [ir_sum(length, 2) for length in lengths_2d]
    ratios_2d = [val / math.log(length) for val, length in zip(vals_2d, lengths_2d)]
    growing_2d = all(b > a for a, b in zip(vals_2d, vals_2d[1:]))
    stable_2d = max(ratios_2d[-3:]) - min(ratios_2d[-3:]) < 0.03
    for length, val, ratio in zip(lengths_2d, vals_2d, ratios_2d):
        print(f"  L={length:3d}: I_2={val:.9f} I_2/log(L)={ratio:.9f}")
    print(f"  monotone growth: {growing_2d}")
    print(f"  last-three ratio spread < 0.03: {stable_2d}")

    print("\nPART D: three-dimensional finite IR window")
    lengths_3d = [6, 8, 10, 12, 16, 20]
    vals_3d = [ir_sum(length, 3) for length in lengths_3d]
    bounded_3d = max(vals_3d) < 0.27
    final_change = abs(vals_3d[-1] - vals_3d[-2]) / vals_3d[-2]
    converging_3d = final_change < 0.04
    for length, val in zip(lengths_3d, vals_3d):
        print(f"  L={length:3d}: I_3={val:.9f}")
    print(f"  bounded below 0.27 on tested window: {bounded_3d}")
    print(f"  final relative change < 0.04: {converging_3d} ({final_change:.6e})")

    print("\nPART E: Bogoliubov-bound consequence")
    bounds_1d = [math.sqrt(1.0 / ir_sum(length, 1)) for length in [8, 16, 32, 64, 128]]
    bounds_2d = [math.sqrt(1.0 / ir_sum(length, 2)) for length in lengths_2d]
    dec_1d = all(b < a for a, b in zip(bounds_1d, bounds_1d[1:]))
    dec_2d = all(b < a for a, b in zip(bounds_2d, bounds_2d[1:]))
    print(f"  d=1 |m_L| upper bounds: {[round(v, 6) for v in bounds_1d]}")
    print(f"  d=2 |m_L| upper bounds: {[round(v, 6) for v in bounds_2d]}")
    print(f"  d=1 bound decreasing: {dec_1d}")
    print(f"  d=2 bound decreasing: {dec_2d}")

    checks = {
        "finite Bogoliubov inequality": bog_ok,
        "exact d=1 IR identity": id_ok,
        "d=2 logarithmic growth": growing_2d and stable_2d,
        "d=3 finite window": bounded_3d and converging_3d,
        "Bogoliubov bound tightens in d<=2": dec_1d and dec_2d,
    }

    print("\nSUMMARY")
    classes = {
        "finite Bogoliubov inequality": "A",
        "exact d=1 IR identity": "A",
        "d=2 logarithmic growth": "C",
        "d=3 finite window": "C",
        "Bogoliubov bound tightens in d<=2": "C",
    }
    for name, ok in checks.items():
        cls = classes[name]
        verdict = f"PASS ({cls})" if ok else "FAIL"
        print(f"  [{verdict}] {name}")
    passed = sum(checks.values())
    print(f"  PASS={passed} FAIL={len(checks) - passed}")
    if passed != len(checks):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
