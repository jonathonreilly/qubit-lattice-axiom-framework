#!/usr/bin/env python3
"""Verify the exact Fierz-channel boundary for a scalar map on G.

The load-bearing premise checked here is supplied directly:

    G_prime = a * G.

The runner does not derive that premise from the link-level replacement
U -> u_0 V. Its scope checks require the paired note to keep that bridge open.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "YT_EW_M_RESIDUAL_NOTE_2026-05-02.md"
TOL = 1e-10


def su2_generators() -> list[np.ndarray]:
    return [
        np.array([[0, 1], [1, 0]], dtype=complex) / 2,
        np.array([[0, -1j], [1j, 0]], dtype=complex) / 2,
        np.array([[1, 0], [0, -1]], dtype=complex) / 2,
    ]


def su3_generators() -> list[np.ndarray]:
    matrices = [
        [[0, 1, 0], [1, 0, 0], [0, 0, 0]],
        [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]],
        [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
        [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
        [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]],
        [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
        [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]],
        (np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / np.sqrt(3)).tolist(),
    ]
    return [np.array(matrix, dtype=complex) / 2 for matrix in matrices]


def generators(n_c: int) -> list[np.ndarray]:
    if n_c == 2:
        return su2_generators()
    if n_c == 3:
        return su3_generators()
    raise ValueError(f"unsupported N_c={n_c}")


def channels(g: np.ndarray, basis: list[np.ndarray]) -> tuple[float, float]:
    n_c = g.shape[0]
    singlet = abs(np.trace(g)) ** 2 / n_c
    adjoint = 2 * sum(abs(np.trace(g @ t_a)) ** 2 for t_a in basis)
    return float(singlet), float(adjoint)


def report(label: str, ok: bool, detail: str) -> bool:
    print(f"{label}: {'PASS' if ok else 'FAIL'}")
    print(f"  {detail}")
    return ok


def main() -> None:
    rng = np.random.default_rng(42)
    results: list[bool] = []

    print("=" * 76)
    print("COMMON PROPAGATOR RESCALING: EXACT FIERZ-CHANNEL NEGATIVE BOUNDARY")
    print("=" * 76)
    print("Declared premise: G_prime = a * G.")
    print("No implication from U -> u_0 V to the propagator is derived or tested.")
    print()

    max_fierz_error = 0.0
    for n_c in (2, 3):
        basis = generators(n_c)
        for _ in range(20):
            g = rng.normal(size=(n_c, n_c)) + 1j * rng.normal(size=(n_c, n_c))
            s_g, c_g = channels(g, basis)
            total = float(np.trace(g.conj().T @ g).real)
            max_fierz_error = max(max_fierz_error, abs(total - s_g - c_g))
    results.append(
        report(
            "TEST 1 — Fierz identity",
            max_fierz_error < TOL,
            f"max |Tr(G^dagger G)-S-C| = {max_fierz_error:.3e}",
        )
    )

    max_generator_error = 0.0
    for n_c in (2, 3):
        basis = generators(n_c)
        for a_index, t_a in enumerate(basis):
            max_generator_error = max(
                max_generator_error,
                float(np.linalg.norm(t_a - t_a.conj().T)),
                abs(float(np.trace(t_a).real)),
                abs(float(np.trace(t_a).imag)),
            )
            for b_index, t_b in enumerate(basis):
                expected = 0.5 if a_index == b_index else 0.0
                max_generator_error = max(
                    max_generator_error,
                    abs(complex(np.trace(t_a @ t_b)) - expected),
                )
    results.append(
        report(
            "TEST 2 — generator normalization",
            max_generator_error < TOL,
            f"max Hermiticity/trace/Gram error = {max_generator_error:.3e}",
        )
    )

    max_homogeneity_error = 0.0
    scalars = (0.0, 0.85, -1.2, 0.4 + 0.3j)
    for n_c in (2, 3):
        basis = generators(n_c)
        for _ in range(20):
            g = rng.normal(size=(n_c, n_c)) + 1j * rng.normal(size=(n_c, n_c))
            s_g, c_g = channels(g, basis)
            for scalar in scalars:
                s_scaled, c_scaled = channels(scalar * g, basis)
                factor = abs(scalar) ** 2
                max_homogeneity_error = max(
                    max_homogeneity_error,
                    abs(s_scaled - factor * s_g),
                    abs(c_scaled - factor * c_g),
                )
    results.append(
        report(
            "TEST 3 — degree-two homogeneity",
            max_homogeneity_error < TOL,
            f"real/complex scalar max error = {max_homogeneity_error:.3e}",
        )
    )

    max_ratio_error = 0.0
    ratio_trials = 0
    for n_c in (2, 3):
        basis = generators(n_c)
        for _ in range(40):
            g = rng.normal(size=(n_c, n_c)) + 1j * rng.normal(size=(n_c, n_c))
            s_g, c_g = channels(g, basis)
            scalar = 0.4 + 0.3j
            s_scaled, c_scaled = channels(scalar * g, basis)
            if s_g > TOL and s_g + c_g > TOL:
                max_ratio_error = max(
                    max_ratio_error,
                    abs(c_scaled / s_scaled - c_g / s_g),
                    abs(c_scaled / (s_scaled + c_scaled) - c_g / (s_g + c_g)),
                )
                ratio_trials += 1
    results.append(
        report(
            "TEST 4 — nonzero-scalar ratio invariance",
            ratio_trials > 0 and max_ratio_error < TOL,
            f"{ratio_trials} trials; max ratio error = {max_ratio_error:.3e}",
        )
    )

    basis = generators(3)
    g = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    s_zero, c_zero = channels(0.0 * g, basis)
    results.append(
        report(
            "TEST 5 — zero scalar erases both channels",
            abs(s_zero) < TOL and abs(c_zero) < TOL,
            f"S(0G)={s_zero:.1f}, C(0G)={c_zero:.1f}",
        )
    )

    note = NOTE.read_text(encoding="utf-8")
    required = (
        "exact negative boundary",
        "does **not** infer",
        "The only additional premise used in the no-go",
        "does not disprove CMT-only adjoint",
        "Closing that physical rule requires",
    )
    forbidden = (
        "It closes the *naive* M interpretation as DISPROVEN",
        "CMT factorization is channel-blind",
        "under U → u_0 V factorization, **both S and C inherit",
    )
    missing = [phrase for phrase in required if phrase not in note]
    present_forbidden = [phrase for phrase in forbidden if phrase in note]
    results.append(
        report(
            "TEST 6 — note scope contract",
            not missing and not present_forbidden,
            f"missing={missing or 'none'}; forbidden_present={present_forbidden or 'none'}",
        )
    )

    print()
    print("=" * 76)
    for index, ok in enumerate(results, start=1):
        print(f"TEST {index}: {'PASS' if ok else 'FAIL'}")
    overall = all(results)
    print(f"OVERALL: {'PASS' if overall else 'FAIL'} ({sum(results)}/{len(results)})")
    print()
    print("CERTIFIED CLAIM:")
    print("  Given the explicit propagator-level premise G_prime = a*G, S and C")
    print("  both scale by |a|^2. It cannot select C by relative rescaling.")
    print("SCOPE EXCLUSION:")
    print("  No map from U -> u_0 V to G is derived; the physical CMT/EW-current")
    print("  matching rule remains open.")

    if not overall:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
