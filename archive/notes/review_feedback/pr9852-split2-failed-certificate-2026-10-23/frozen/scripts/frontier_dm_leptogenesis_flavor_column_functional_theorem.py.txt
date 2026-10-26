#!/usr/bin/env python3
"""Conditional flavor-column integrating-factor identity.

The algebraic identity verified here is conditional on supplied transport
equations, profiles, boundary data, and projector columns.  The numerical
kernel and canonical packet are finite fixtures, not axiom-native physical
derivations.
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import numpy as np
from scipy import integrate

from dm_leptogenesis_exact_common import (
    decay_profile,
    exact_package,
    n_eq_normalized_mb,
    reference_expansion_profile,
    solve_multisource_flavored_transport,
    solve_normalized_transport,
    washout_profile,
)
from frontier_dm_leptogenesis_pmns_projector_interface import (
    canonical_h,
    canonical_left_diagonalizer,
)

AUDIT_TIMEOUT_SEC = 120

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", cls: str = "A") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{cls}] {status}: {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def active_packet_from_h(h_act: np.ndarray) -> np.ndarray:
    """Finite linear-algebra packet from a supplied Hermitian matrix."""
    _evals, u_act = canonical_left_diagonalizer(h_act)
    return np.abs(u_act) ** 2


def _validated_kernel_arrays(
    source_profile: np.ndarray, washout_tail: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    source = np.asarray(source_profile, dtype=float)
    tail = np.asarray(washout_tail, dtype=float)
    if source.ndim != 1 or tail.ndim != 1 or source.shape != tail.shape:
        raise ValueError("source_profile and washout_tail must be same-shape 1D arrays")
    if source.size < 2:
        raise ValueError("kernel arrays must contain at least two samples")
    if not np.all(np.isfinite(source)) or not np.all(np.isfinite(tail)):
        raise ValueError("kernel arrays must be finite")
    return source, tail


def flavored_transport_kernel(
    k_decay: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return the primary finite numerical kernel supplied by the helper stack."""
    z_grid, n_n1, _ = solve_normalized_transport(
        k_decay, reference_expansion_profile
    )
    source_profile = -np.gradient(n_n1, z_grid)
    w_vals = np.array(
        [
            washout_profile(float(z), k_decay, reference_expansion_profile)
            for z in z_grid
        ],
        dtype=float,
    )
    tail = np.zeros_like(z_grid)
    for idx in range(len(z_grid) - 2, -1, -1):
        tail[idx] = tail[idx + 1] + 0.5 * (
            w_vals[idx] + w_vals[idx + 1]
        ) * (z_grid[idx + 1] - z_grid[idx])
    return z_grid, source_profile, tail


def independently_recomputed_kernel(
    k_decay: float, n_eval: int = 12001
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Recompute the fixture on another grid using the ODE source expression."""
    z_grid, n_n1, _ = solve_normalized_transport(
        k_decay, reference_expansion_profile, n_eval=n_eval
    )
    source_profile = np.array(
        [
            decay_profile(float(z), k_decay, reference_expansion_profile)
            * (float(n_val) - n_eq_normalized_mb(float(z)))
            for z, n_val in zip(z_grid, n_n1, strict=True)
        ],
        dtype=float,
    )
    w_vals = np.array(
        [
            washout_profile(float(z), k_decay, reference_expansion_profile)
            for z in z_grid
        ],
        dtype=float,
    )
    reversed_integral = integrate.cumulative_trapezoid(
        w_vals[::-1], z_grid[::-1], initial=0.0
    )
    tail = -reversed_integral[::-1]
    return z_grid, source_profile, tail


def psi_q(
    q: float,
    z_grid: np.ndarray,
    source_profile: np.ndarray,
    washout_tail: np.ndarray,
) -> float:
    q_value = float(q)
    z = np.asarray(z_grid, dtype=float)
    source, tail = _validated_kernel_arrays(source_profile, washout_tail)
    if z.ndim != 1 or z.shape != source.shape or not np.all(np.isfinite(z)):
        raise ValueError("z_grid must be a finite 1D array matching the kernel")
    if not np.all(np.diff(z) > 0.0):
        raise ValueError("z_grid must be strictly increasing")
    if not math.isfinite(q_value) or q_value < 0.0 or q_value > 1.0:
        raise ValueError("q must lie in the projector interval [0,1]")
    return float(
        np.trapezoid(
            q_value * source * np.exp(-q_value * tail),
            z,
        )
    )


def flavored_column_functional(
    column: np.ndarray,
    z_grid: np.ndarray,
    source_profile: np.ndarray,
    washout_tail: np.ndarray,
) -> float:
    values = np.asarray(column, dtype=float)
    if values.ndim != 1 or values.size != 3 or not np.all(np.isfinite(values)):
        raise ValueError("column must be a finite three-flavor 1D array")
    if np.any(values < 0.0) or np.any(values > 1.0):
        raise ValueError("column entries must lie in [0,1]")
    if not math.isclose(float(math.fsum(values)), 1.0, rel_tol=0.0, abs_tol=1.0e-12):
        raise ValueError("column entries must sum to one")
    return float(
        math.fsum(
            psi_q(float(q), z_grid, source_profile, washout_tail)
            for q in values
        )
    )


def flavored_transport_direct(column: np.ndarray, k_decay: float) -> float:
    """Independent helper ODE evaluation for a supplied projector column."""
    _, _, asym_grid = solve_multisource_flavored_transport(
        lambdas=np.array([1.0]),
        k_decays=np.array([k_decay]),
        source_matrix=np.array([column], dtype=float),
        washout_matrix=np.array([column], dtype=float),
    )
    return float(asym_grid[:, -1].sum())


def trapezoid_measure_weights(
    z_grid: np.ndarray, source_profile: np.ndarray
) -> np.ndarray:
    z = np.asarray(z_grid, dtype=float)
    source = np.asarray(source_profile, dtype=float)
    if z.ndim != 1 or source.shape != z.shape or z.size < 2:
        raise ValueError("z_grid and source_profile must be matching 1D arrays")
    dz = np.diff(z)
    weights = np.zeros_like(source)
    weights[0] = 0.5 * dz[0] * source[0]
    weights[-1] = 0.5 * dz[-1] * source[-1]
    weights[1:-1] = 0.5 * (dz[:-1] + dz[1:]) * source[1:-1]
    return weights


def finite_kernel_derivative(
    q: float, weights: np.ndarray, washout_tail: np.ndarray
) -> float:
    return float(
        math.fsum(
            float(weight)
            * math.exp(-float(q) * float(tail))
            * (1.0 - float(q) * float(tail))
            for weight, tail in zip(weights, washout_tail, strict=True)
        )
    )


def finite_kernel_second_derivative(
    q: float, weights: np.ndarray, washout_tail: np.ndarray
) -> float:
    return float(
        math.fsum(
            float(weight)
            * float(tail)
            * math.exp(-float(q) * float(tail))
            * (float(q) * float(tail) - 2.0)
            for weight, tail in zip(weights, washout_tail, strict=True)
        )
    )


def bisect_stationary_point(
    lower: float,
    upper: float,
    weights: np.ndarray,
    washout_tail: np.ndarray,
    iterations: int = 70,
) -> float:
    lo = float(lower)
    hi = float(upper)
    f_lo = finite_kernel_derivative(lo, weights, washout_tail)
    f_hi = finite_kernel_derivative(hi, weights, washout_tail)
    if not (f_lo > 0.0 and f_hi < 0.0):
        raise ValueError("stationary-point bracket must have derivative signs +,-")
    for _ in range(iterations):
        mid = 0.5 * (lo + hi)
        f_mid = finite_kernel_derivative(mid, weights, washout_tail)
        if f_mid > 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def _raises_value_error(callable_obj: object) -> bool:
    try:
        callable_obj()
    except ValueError:
        return True
    return False


def part0_source_scope_firewall() -> None:
    print("\n" + "=" * 88)
    print("PART 0: SELF-CONTAINED RUNNER-SCOPE FIREWALL")
    print("=" * 88)

    source = Path(__file__).read_text(encoding="utf-8")

    required_source_phrases = (
        "conditional on supplied transport",
        "finite fixtures, not axiom-native physical",
        "GLOBAL UNIQUENESS OPEN",
        "No physical yield conversion or canonical-packet derivation",
    )
    for phrase in required_source_phrases:
        check(
            f"runner source carries required scope phrase: {phrase}",
            phrase in source,
            cls="B",
        )

    forbidden_physical_imports = (
        "ETA_" + "OBS",
        "C_" + "SPH",
        "D_THERMAL_" + "EXACT",
        "S_OVER_NGAMMA_" + "EXACT",
    )
    for name in forbidden_physical_imports:
        check(
            f"runner source does not reference or consume physical readout name: {name}",
            name not in source,
            cls="B",
        )


def part1_integrating_factor_identity_has_independent_analytic_checks() -> None:
    print("\n" + "=" * 88)
    print("PART 1: CONDITIONAL INTEGRATING-FACTOR IDENTITY")
    print("=" * 88)

    length = 4.0
    source_level = 1.7
    washout_level = 0.8
    z_const = np.linspace(0.0, length, 40001)
    source_const = np.full_like(z_const, source_level)
    tail_const = washout_level * (length - z_const)
    q_samples = (0.0, 1.0e-6, 0.03549, 1.0 / 3.0, 1.0)
    constant_errors = []
    for q_value in q_samples:
        computed = psi_q(q_value, z_const, source_const, tail_const)
        expected = (
            0.0
            if q_value == 0.0
            else source_level
            / washout_level
            * (1.0 - math.exp(-q_value * washout_level * length))
        )
        constant_errors.append(abs(computed - expected))
    check(
        "finite functional agrees with the closed-form constant-profile solution",
        max(constant_errors) < 2.0e-9,
        f"max_error={max(constant_errors):.3e}",
    )

    length_var = 3.0
    z_var = np.linspace(0.0, length_var, 30001)
    source_var = 1.0 + 0.2 * np.sin(2.0 * np.pi * z_var / length_var)
    tail_var = (
        0.4 * (length_var - z_var)
        + 0.05 * (length_var**2 - z_var**2)
    )

    variable_errors = []
    for q_value in q_samples:
        computed = psi_q(q_value, z_var, source_var, tail_var)

        def rhs(z_value: float, state: np.ndarray) -> list[float]:
            source_value = 1.0 + 0.2 * math.sin(
                2.0 * math.pi * z_value / length_var
            )
            washout_value = 0.4 + 0.1 * z_value
            return [
                q_value * source_value
                - q_value * washout_value * float(state[0])
            ]

        sol = integrate.solve_ivp(
            rhs,
            (0.0, length_var),
            (0.0,),
            method="DOP853",
            rtol=2.0e-12,
            atol=1.0e-13,
        )
        if not sol.success:
            raise RuntimeError(sol.message)
        variable_errors.append(abs(computed - float(sol.y[0, -1])))
    check(
        "finite functional agrees with an independent ODE solve for a non-constant profile",
        max(variable_errors) < 2.0e-9,
        f"max_error={max(variable_errors):.3e}",
    )

    check(
        "invalid negative projector weight is rejected",
        _raises_value_error(
            lambda: psi_q(-1.0e-6, z_const, source_const, tail_const)
        ),
    )
    check(
        "invalid non-monotone integration grid is rejected",
        _raises_value_error(
            lambda: psi_q(
                0.2,
                z_const[::-1],
                source_const,
                tail_const,
            )
        ),
    )
    check(
        "invalid non-finite column is rejected",
        _raises_value_error(
            lambda: flavored_column_functional(
                np.array([0.5, np.nan, 0.5]),
                z_const,
                source_const,
                tail_const,
            )
        ),
    )
    check(
        "invalid non-three-flavor column is rejected",
        _raises_value_error(
            lambda: flavored_column_functional(
                np.array([0.5, 0.5]),
                z_const,
                source_const,
                tail_const,
            )
        ),
    )
    check(
        "invalid non-simplex column is rejected",
        _raises_value_error(
            lambda: flavored_column_functional(
                np.array([0.6, 0.6, 0.0]),
                z_const,
                source_const,
                tail_const,
            )
        ),
    )


def deterministic_simplex_columns() -> list[np.ndarray]:
    columns = [
        np.array([1.0, 0.0, 0.0], dtype=float),
        np.array([1.0 / 3.0] * 3, dtype=float),
        np.array([1.0e-8, 0.49999999, 0.5], dtype=float),
        np.array([0.07126668, 0.90030676, 0.02842656], dtype=float),
    ]
    rng = np.random.default_rng(20260716)
    columns.extend(rng.dirichlet(np.array([0.25, 1.0, 4.0]), size=8))
    return columns


def part2_supplied_numerical_kernel_is_cross_recomputed() -> tuple[
    np.ndarray, np.ndarray, np.ndarray, float
]:
    print("\n" + "=" * 88)
    print("PART 2: SUPPLIED FINITE KERNEL CROSS-RECOMPUTATION")
    print("=" * 88)

    pkg = exact_package()
    z_grid, source_profile, washout_tail = flavored_transport_kernel(
        pkg.k_decay_exact
    )
    z_ind, source_ind, tail_ind = independently_recomputed_kernel(
        pkg.k_decay_exact
    )
    columns = deterministic_simplex_columns()

    functional_values = np.array(
        [
            flavored_column_functional(
                column, z_grid, source_profile, washout_tail
            )
            for column in columns
        ],
        dtype=float,
    )
    independent_values = np.array(
        [
            flavored_column_functional(column, z_ind, source_ind, tail_ind)
            for column in columns
        ],
        dtype=float,
    )
    direct_values = np.array(
        [
            flavored_transport_direct(column, pkg.k_decay_exact)
            for column in columns
        ],
        dtype=float,
    )

    recompute_error = float(
        np.max(np.abs(functional_values - independent_values))
    )
    direct_error = float(np.max(np.abs(functional_values - direct_values)))
    check(
        "primary gradient kernel agrees with a different-grid ODE-source recomputation",
        recompute_error < 1.0e-7,
        f"max_error={recompute_error:.3e}, samples={len(columns)}",
        cls="B",
    )
    check(
        "finite functional agrees with the independent direct flavored ODE solve",
        direct_error < 1.0e-7,
        f"max_error={direct_error:.3e}, samples={len(columns)}",
        cls="B",
    )
    check(
        "the supplied fixture has increasing z, non-negative primary source weights, and decreasing tail",
        bool(
            np.all(np.diff(z_grid) > 0.0)
            and np.min(source_profile) >= -1.0e-12
            and np.all(np.diff(washout_tail) <= 1.0e-10)
        ),
        (
            f"source_min={np.min(source_profile):.3e}, "
            f"tail_range=[{np.min(washout_tail):.3e},{np.max(washout_tail):.6f}]"
        ),
        cls="B",
    )

    print()
    print(
        "  This cross-check is conditional on the helper's supplied equations, "
        "profiles, constants, and boundary data."
    )
    return z_grid, source_profile, washout_tail, pkg.k_decay_exact


def part3_finite_kernel_has_only_a_local_stationary_isolation_check(
    z_grid: np.ndarray,
    source_profile: np.ndarray,
    washout_tail: np.ndarray,
) -> None:
    print("\n" + "=" * 88)
    print("PART 3: LOCAL STATIONARY-POINT ISOLATION; GLOBAL UNIQUENESS OPEN")
    print("=" * 88)

    weights = trapezoid_measure_weights(z_grid, source_profile)
    lower = 0.03549
    upper = 0.03550
    d_lower = finite_kernel_derivative(lower, weights, washout_tail)
    d_upper = finite_kernel_derivative(upper, weights, washout_tail)
    root = bisect_stationary_point(
        lower, upper, weights, washout_tail
    )
    second_at_root = finite_kernel_second_derivative(
        root, weights, washout_tail
    )

    check(
        "analytic derivative changes sign inside the stated finite-kernel bracket",
        d_lower > 1.0e-5 and d_upper < -1.0e-5,
        (
            f"Psi_h'({lower:.5f})={d_lower:.3e}, "
            f"Psi_h'({upper:.5f})={d_upper:.3e}"
        ),
    )
    check(
        (
            "second-derivative terms are non-positive and their sum is "
            "negative throughout that bracket"
        ),
        bool(
            np.min(weights) >= 0.0
            and upper * float(np.max(washout_tail)) < 2.0
            and np.any((weights > 0.0) & (washout_tail > 0.0))
            and second_at_root < 0.0
        ),
        (
            f"q_root={root:.12f}, q_hi*T_max="
            f"{upper * float(np.max(washout_tail)):.6f}, "
            f"Psi_h''(q_root)={second_at_root:.6f}"
        ),
    )

    local_value = psi_q(root, z_grid, source_profile, washout_tail)
    democratic_value = psi_q(
        1.0 / 3.0, z_grid, source_profile, washout_tail
    )
    pure_value = psi_q(1.0, z_grid, source_profile, washout_tail)
    check(
        "the locally isolated finite-kernel point exceeds the democratic and pure-flavor samples",
        local_value > democratic_value and local_value > pure_value,
        (
            f"Psi_h(root)={local_value:.12f}, "
            f"Psi_h(1/3)={democratic_value:.12f}, "
            f"Psi_h(1)={pure_value:.12f}"
        ),
    )

    print()
    print(
        "  No check in this runner asserts that this is the only stationary "
        "point on [0,1] or for a continuum profile."
    )


def part4_supplied_canonical_packet_has_a_finite_middle_column_ordering(
    z_grid: np.ndarray,
    source_profile: np.ndarray,
    washout_tail: np.ndarray,
    k_decay: float,
) -> None:
    print("\n" + "=" * 88)
    print("PART 4: SUPPLIED CANONICAL PACKET FINITE ORDERING")
    print("=" * 88)

    h_e_act = canonical_h(
        np.array([0.24, 0.38, 1.07], dtype=float),
        np.array([0.09, 0.22, 0.61], dtype=float),
        1.10,
    )
    packet = active_packet_from_h(h_e_act).T

    direct_vals = np.array(
        [
            flavored_transport_direct(packet[:, idx], k_decay)
            for idx in range(3)
        ],
        dtype=float,
    )
    func_vals = np.array(
        [
            flavored_column_functional(
                packet[:, idx], z_grid, source_profile, washout_tail
            )
            for idx in range(3)
        ],
        dtype=float,
    )
    direct_best = int(np.argmax(direct_vals))
    functional_best = int(np.argmax(func_vals))
    sorted_vals = np.sort(func_vals)

    check(
        "the supplied eigensystem packet is column-stochastic and non-negative",
        bool(
            np.min(packet) >= -1.0e-14
            and np.max(np.abs(np.sum(packet, axis=0) - 1.0)) < 1.0e-12
        ),
        (
            f"min_entry={np.min(packet):.3e}, "
            f"max_column_sum_error="
            f"{np.max(np.abs(np.sum(packet, axis=0) - 1.0)):.3e}"
        ),
        cls="B",
    )
    check(
        "functional and direct ODE computations agree on all three supplied packet columns",
        float(np.max(np.abs(func_vals - direct_vals))) < 1.0e-7,
        f"max_error={np.max(np.abs(func_vals - direct_vals)):.3e}",
        cls="B",
    )
    check(
        "both finite computations order the supplied packet with middle column first",
        direct_best == 1 and functional_best == 1,
        (
            f"argmax_direct={direct_best}, "
            f"argmax_functional={functional_best}, "
            f"functional_gap={sorted_vals[-1] - sorted_vals[-2]:.6e}"
        ),
        cls="B",
    )

    permutation = np.array([2, 0, 1])
    permuted_packet = packet[:, permutation]
    permuted_vals = np.array(
        [
            flavored_column_functional(
                permuted_packet[:, idx],
                z_grid,
                source_profile,
                washout_tail,
            )
            for idx in range(3)
        ]
    )
    check(
        "column relabeling only relabels the finite functional values",
        bool(np.allclose(permuted_vals, func_vals[permutation], atol=1.0e-13)),
        f"permutation={permutation.tolist()}",
    )

    print()
    print("  supplied canonical N_e packet:")
    print(np.round(packet, 6))
    print(f"  direct finite transport factors = {np.round(direct_vals, 12)}")
    print(f"  finite functional values        = {np.round(func_vals, 12)}")
    print(
        "  No physical yield conversion or canonical-packet derivation is "
        "claimed here."
    )


def part1_single_source_flavored_transport_reduces_to_an_exact_column_functional(
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """Legacy downstream API for the supplied finite transport fixture.

    The historical function name is retained only so existing diagnostic
    runners can obtain the four kernel objects.  This compatibility wrapper
    does not certify the old theorem-grade wording encoded in that name.
    """
    pkg = exact_package()
    z_grid, source_profile, washout_tail = flavored_transport_kernel(
        pkg.k_decay_exact
    )
    return z_grid, source_profile, washout_tail, pkg.k_decay_exact


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--intentional-failure-probe",
        action="store_true",
        help="inject one failed check to verify truthful nonzero exit behavior",
    )
    args = parser.parse_args(argv)

    print("=" * 88)
    print("DM LEPTOGENESIS CONDITIONAL FLAVOR-COLUMN FUNCTIONAL IDENTITY")
    print("=" * 88)

    part0_source_scope_firewall()
    part1_integrating_factor_identity_has_independent_analytic_checks()
    z_grid, source_profile, washout_tail, k_decay = (
        part2_supplied_numerical_kernel_is_cross_recomputed()
    )
    part3_finite_kernel_has_only_a_local_stationary_isolation_check(
        z_grid, source_profile, washout_tail
    )
    part4_supplied_canonical_packet_has_a_finite_middle_column_ordering(
        z_grid, source_profile, washout_tail, k_decay
    )

    if args.intentional_failure_probe:
        check(
            "intentional failure probe",
            False,
            "expected failure used only to verify exit status",
        )

    print("\n" + "=" * 88)
    print(f"SUMMARY: classified_pass={PASS_COUNT} fail={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
