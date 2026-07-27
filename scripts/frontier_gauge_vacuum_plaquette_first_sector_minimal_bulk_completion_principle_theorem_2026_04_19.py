#!/usr/bin/env python3
"""Finite-cone minimal-bulk completion theorem check.

On the 36-slot box W_5 = {(p,q): 0 <= p,q <= 5}, an admissible extension
of the retained first-sector packet is nonnegative, invariant under
(p,q) <-> (q,p), and fixed on the four retained slots.  The non-retained
conjugation-orbit indicators are the extreme generators of its tail cone.

The source note proves, for an arbitrary nonnegative combination of those
generators, that

  * the zero extension is the unique coefficient-order least element;
  * every tail functional strictly positive away from zero has the zero
    extension as its unique minimizer; and
  * T(rho) = M D_loc diag(rho) M is Loewner monotone and injective on the
    tail cone when M is symmetric/invertible and D_loc is positive diagonal.

This runner checks all hypotheses and exhausts all orbit generators.  Tails
A and B remain only as regression examples; no universal claim is inferred
from a random sweep or from those two examples.
"""

from __future__ import annotations

import sys

import numpy as np

from frontier_gauge_vacuum_plaquette_first_sector_rank_one_transfer_realization_2026_04_19 import (
    completed_sector_data,
)
from frontier_gauge_vacuum_plaquette_first_sector_zero_extension_factorized_class_theorem_2026_04_19 import (
    local_factor_diagonal,
)
from frontier_gauge_vacuum_plaquette_spatial_environment_character_measure import (
    BETA,
    build_recurrence_matrix,
    matrix_exponential_symmetric,
    dim_su3,
)


PASS_COUNT = 0
FAIL_COUNT = 0

RETAINED_SUPPORT = ((0, 0), (1, 0), (0, 1), (1, 1))


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return condition


def retained_packet() -> tuple[np.ndarray, float]:
    """Return the displayed retained packet; its properties are checked here."""
    v_min, _z_min = completed_sector_data()
    z00 = float(v_min[0])
    return np.asarray(v_min / z00, dtype=float), z00


def zero_extension(
    weights: list[tuple[int, int]],
    index: dict[tuple[int, int], int],
    rho_ret: np.ndarray,
) -> np.ndarray:
    rho = np.zeros(len(weights), dtype=float)
    for value, weight in zip(rho_ret, RETAINED_SUPPORT):
        rho[index[weight]] = float(value)
    return rho


def add_tail(
    rho0: np.ndarray,
    index: dict[tuple[int, int], int],
    updates: dict[tuple[int, int], float],
) -> np.ndarray:
    rho = np.array(rho0, dtype=float)
    for weight, value in updates.items():
        rho[index[weight]] += float(value)
    return rho


def conjugation_error(
    packet: np.ndarray,
    weights: list[tuple[int, int]],
    index: dict[tuple[int, int], int],
) -> float:
    return max(
        abs(float(packet[i]) - float(packet[index[(q, p)]]))
        for i, (p, q) in enumerate(weights)
    )


def tail_orbit_generators(
    weights: list[tuple[int, int]],
    index: dict[tuple[int, int], int],
) -> list[tuple[tuple[tuple[int, int], ...], np.ndarray]]:
    """Indicators of all non-retained (p,q)<->(q,p) orbits.

    Their supports are disjoint and cover the tail, so every admissible tail
    has one and only one nonnegative expansion in these generators.
    """
    retained = set(RETAINED_SUPPORT)
    visited: set[tuple[int, int]] = set()
    generators: list[tuple[tuple[tuple[int, int], ...], np.ndarray]] = []
    for weight in weights:
        if weight in retained or weight in visited:
            continue
        partner = (weight[1], weight[0])
        orbit = (weight,) if partner == weight else (weight, partner)
        generator = np.zeros(len(weights), dtype=float)
        for member in orbit:
            if member in retained:
                raise AssertionError("retained support must be a union of conjugation orbits")
            generator[index[member]] = 1.0
            visited.add(member)
        generators.append((orbit, generator))
    return generators


def tail_metrics(
    rho: np.ndarray,
    rho0: np.ndarray,
    weights: list[tuple[int, int]],
    index: dict[tuple[int, int], int],
) -> dict[str, float]:
    tail_indices = [i for i, weight in enumerate(weights) if weight not in RETAINED_SUPPORT]
    tail = np.asarray(rho[tail_indices] - rho0[tail_indices], dtype=float)
    dims = np.asarray([dim_su3(*weights[i]) for i in tail_indices], dtype=float)
    return {
        "tail_min": float(np.min(tail)) if len(tail) else 0.0,
        "tail_mass": float(np.sum(tail)),
        "tail_l2_sq": float(np.dot(tail, tail)),
        "tail_dim_mass": float(np.dot(dims, tail)),
        "tail_support": int(np.count_nonzero(tail > 0.0)),
    }


def transfer(multiplier: np.ndarray, d_local: np.ndarray, rho: np.ndarray) -> np.ndarray:
    return multiplier @ d_local @ np.diag(np.asarray(rho, dtype=float)) @ multiplier


def psd_with_scale(matrix: np.ndarray) -> bool:
    scale = max(1.0, float(np.linalg.norm(matrix, ord=2)))
    return float(np.min(np.linalg.eigvalsh(matrix))) >= -1.0e-12 * scale


def main() -> int:
    print("=" * 118)
    print("GAUGE-VACUUM PLAQUETTE FIRST-SECTOR FINITE-CONE MINIMAL-BULK COMPLETION THEOREM")
    print("=" * 118)

    rho_ret, z00 = retained_packet()
    jmat, weights, index = build_recurrence_matrix(5)
    multiplier = matrix_exponential_symmetric(jmat, BETA / 2.0)
    d_local = local_factor_diagonal(weights)
    rho0 = zero_extension(weights, index, rho_ret)
    generators = tail_orbit_generators(weights, index)

    tail_indices = [i for i, weight in enumerate(weights) if weight not in RETAINED_SUPPORT]
    expected_cover = np.zeros(len(weights), dtype=float)
    expected_cover[tail_indices] = 1.0
    actual_cover = np.sum([generator for _orbit, generator in generators], axis=0)

    t0 = transfer(multiplier, d_local, rho0)
    rho_a = add_tail(rho0, index, {(2, 0): 0.05, (0, 2): 0.05})
    rho_b = add_tail(rho0, index, {(2, 1): 0.03, (1, 2): 0.03, (2, 2): 0.02})

    print()
    print(f"  finite box / tail slots / tail orbits       = {len(weights)} / {len(tail_indices)} / {len(generators)}")
    print(f"  z00_min                                     = {z00:.12f}")
    print(f"  rho_ret                                     = {np.round(rho_ret, 12).tolist()}")
    print(f"  min diag(D_loc)                             = {float(np.min(np.diag(d_local))):.3e}")
    print(f"  min singular value(M)                       = {float(np.min(np.linalg.svd(multiplier, compute_uv=False))):.3e}")
    print()

    rho_00, rho_10, rho_01, rho_11 = (float(value) for value in rho_ret)
    check(
        "The supplied retained packet directly satisfies the theorem's finite, normalized, nonnegative symmetry hypotheses",
        rho_ret.shape == (4,)
        and np.all(np.isfinite(rho_ret))
        and abs(rho_00 - 1.0) < 1.0e-12
        and abs(rho_10 - rho_01) < 1.0e-12
        and min(rho_00, rho_10, rho_01, rho_11) >= -1.0e-12,
        f"rho11={rho_11:.3e}, conjugation_error={abs(rho_10-rho_01):.3e}",
    )

    retained_match_error = max(
        abs(float(rho0[index[weight]]) - float(value))
        for weight, value in zip(RETAINED_SUPPORT, rho_ret)
    )
    check(
        "rho_0 is an admissible conjugation-symmetric extension and vanishes on every non-retained slot",
        retained_match_error < 1.0e-12
        and float(np.min(rho0)) >= -1.0e-12
        and conjugation_error(rho0, weights, index) < 1.0e-12
        and np.count_nonzero(rho0[tail_indices]) == 0,
        f"retained_match={retained_match_error:.3e}, tail_nonzeros={np.count_nonzero(rho0[tail_indices])}",
    )

    generator_symmetry_error = max(
        conjugation_error(generator, weights, index) for _orbit, generator in generators
    )
    check(
        "The conjugation-orbit generators are nonnegative, disjoint, and cover every tail slot exactly once",
        len(generators) > 0
        and all(float(np.min(generator)) >= 0.0 for _orbit, generator in generators)
        and np.array_equal(actual_cover, expected_cover)
        and generator_symmetry_error == 0.0,
        f"orbits={len(generators)}, cover_error={float(np.max(np.abs(actual_cover-expected_cover))):.1e}",
    )

    # A deterministic tail with a distinct positive coefficient on every
    # orbit checks the unique coordinate recovery implied by disjoint support.
    coefficients = np.arange(1, len(generators) + 1, dtype=float) / (10.0 * len(generators))
    delta = sum(
        (coefficient * generator for coefficient, (_orbit, generator) in zip(coefficients, generators)),
        start=np.zeros(len(weights), dtype=float),
    )
    recovered = np.asarray(
        [delta[np.flatnonzero(generator)[0]] for _orbit, generator in generators],
        dtype=float,
    )
    reconstruction = sum(
        (coefficient * generator for coefficient, (_orbit, generator) in zip(recovered, generators)),
        start=np.zeros(len(weights), dtype=float),
    )
    check(
        "Every admissible tail has unique nonnegative orbit coordinates, proving rho_0 is the unique coefficient-order least extension",
        np.all(recovered >= 0.0)
        and np.array_equal(recovered, coefficients)
        and np.array_equal(reconstruction, delta)
        and np.all(rho0 + delta >= rho0),
        f"coordinate_reconstruction_error={float(np.max(np.abs(reconstruction-delta))):.1e}",
    )

    multiplier_symmetry_error = float(np.max(np.abs(multiplier - multiplier.T)))
    multiplier_smin = float(np.min(np.linalg.svd(multiplier, compute_uv=False)))
    d_min = float(np.min(np.diag(d_local)))
    check(
        "The factorized transfer has symmetric invertible M and strictly positive diagonal D_loc",
        multiplier_symmetry_error < 1.0e-12
        and multiplier_smin > 1.0e-12
        and np.max(np.abs(d_local - np.diag(np.diag(d_local)))) == 0.0
        and d_min > 0.0,
        f"symmetry_error={multiplier_symmetry_error:.3e}, sigma_min={multiplier_smin:.3e}, d_min={d_min:.3e}",
    )

    increments = [
        multiplier @ d_local @ np.diag(generator) @ multiplier
        for _orbit, generator in generators
    ]
    min_increment_eigenvalue = min(float(np.min(np.linalg.eigvalsh(increment))) for increment in increments)
    min_increment_norm = min(float(np.linalg.norm(increment)) for increment in increments)
    check(
        "Every tail-orbit generator has a nonzero PSD congruence increment; nonnegative sums prove arbitrary-tail Loewner monotonicity",
        all(psd_with_scale(increment) for increment in increments)
        and all(float(np.linalg.norm(increment)) > 0.0 for increment in increments),
        f"min_eigenvalue={min_increment_eigenvalue:.3e}, min_nonzero_norm={min_increment_norm:.3e}",
    )

    generator_metrics = [
        tail_metrics(rho0 + generator, rho0, weights, index)
        for _orbit, generator in generators
    ]
    check(
        "Positive weighted mass, p-mass, and support separate zero from every nonzero tail generator",
        all(
            metrics["tail_mass"] > 0.0
            and metrics["tail_dim_mass"] > 0.0
            and metrics["tail_l2_sq"] > 0.0
            and metrics["tail_support"] > 0
            for metrics in generator_metrics
        ),
        "strict positivity on all generators extends to every nonzero nonnegative orbit combination",
    )

    ma = tail_metrics(rho_a, rho0, weights, index)
    mb = tail_metrics(rho_b, rho0, weights, index)
    increment_a = transfer(multiplier, d_local, rho_a - rho0)
    increment_b = transfer(multiplier, d_local, rho_b - rho0)
    check(
        "Legacy tails A and B agree with the universal coefficient, functional, and PSD conclusions (regression only)",
        np.all(rho_a >= rho0)
        and np.all(rho_b >= rho0)
        and ma["tail_mass"] > 0.0
        and mb["tail_mass"] > 0.0
        and psd_with_scale(increment_a)
        and psd_with_scale(increment_b)
        and float(np.linalg.norm(increment_a)) > 0.0
        and float(np.linalg.norm(increment_b)) > 0.0,
        f"massA={ma['tail_mass']:.3e}, massB={mb['tail_mass']:.3e}",
    )

    print("\n" + "=" * 118)
    print("RESULT")
    print("=" * 118)
    print("  Bounded finite-cone result:")
    print("    - all non-retained conjugation-orbit generators are exhausted")
    print("    - their nonnegative cone is exactly the set of admissible tails")
    print("    - rho_0 is the unique coefficient-order least extension")
    print("    - strictly positive bulk-tail functionals uniquely select rho_0")
    print("    - positive diagonal congruence proves Loewner monotonicity for every")
    print("      admissible tail on W_5, with injectivity from M and D_loc")
    print("    - no infinite-weight or physical environment-selection claim is made")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
