#!/usr/bin/env python3
r"""Route-2 time-coupling direct-consumer ambiguity gate.

Safe claim:
  The exact conditional time-coupling family

      Xi_P(t ; c) = (P_R c) otimes exp(-t Lambda_R) u_*

  inherits the unresolved Route-2 readout selector in exactly one place on the
  restricted carrier class: the E-center source factor 1 + rho_E / 6.

  This runner does not derive the endpoint triple. It checks that varying
  rho_E changes the E-center time-coupled tensor and leaves the E-shell,
  T-shell, T-center, and slice dynamics unchanged.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import numpy as np

from frontier_quark_route2_exact_readout_map import (
    EXACT_TOL,
    admissible_readout_matrix,
    restricted_readout_data,
    theorem_target_lands,
)
from frontier_quark_route2_exact_time_coupling import (
    route2_slice_backbone,
    v_r,
    xi_p,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
DIRECT_NOTE = REPO_ROOT / "docs" / "QUARK_ROUTE2_TIME_COUPLING_DIRECT_CONSUMER_AMBIGUITY_GATE_NOTE_2026-06-21.md"
PARENT_NOTE = REPO_ROOT / "docs" / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
TIME_NOTE = REPO_ROOT / "docs" / "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md"
READOUT_NOTE = REPO_ROOT / "docs" / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"

TIMES = [Fraction(0, 1), Fraction(1, 4), Fraction(1, 2), Fraction(1, 1), Fraction(2, 1)]
RHO_ZERO = Fraction(0, 1)
RHO_STAR = Fraction(21, 4)
DELTA_Q = Fraction(7, 8)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def q_e(rho: Fraction) -> Fraction:
    return Fraction(1, 1) + rho / 6


def reduced_map(rho: Fraction) -> np.ndarray:
    return admissible_readout_matrix(1.0, float(rho), -2.0, 2.0)


def f_float(value: Fraction) -> float:
    return value.numerator / value.denominator


def part1_source_surfaces() -> None:
    print("\n" + "=" * 72)
    print("PART 1: Direct Consumer Source Surfaces")
    print("=" * 72)

    parent = text(PARENT_NOTE)
    time_note = text(TIME_NOTE)
    readout_note = text(READOUT_NOTE)
    direct = text(DIRECT_NOTE)

    check(
        "direct packet and one-hop source notes exist",
        DIRECT_NOTE.exists() and PARENT_NOTE.exists() and TIME_NOTE.exists() and READOUT_NOTE.exists(),
        "direct, parent, time-coupling, and readout notes are present",
    )
    check(
        "parent S3 note remains an open gate rather than a closed unique theorem",
        "open_gate route survey" in parent
        and "no unique exact `Theta_R -> Lambda_R` coupling theorem on this arm" in parent,
        "parent boundary is explicit",
    )
    check(
        "time-coupling note supplies the exact conditional family",
        "Xi_P(t ; c) = (P_R c)" in time_note
        and "V_R(t) = exp(-t Lambda_R) u_*" in time_note,
        "time-coupling source family is present",
    )
    check(
        "readout note compresses the missing endpoint to the dimensionless triple",
        "(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)" in readout_note
        and "= (-1, -2, 21/4)" in readout_note,
        "readout triple target is named upstream",
    )
    check(
        "direct note states the narrow downstream inheritance claim",
        "E-center source factor `1 + rho_E / 6`" in direct
        and "not a new slice-dynamics" in direct
        and "ambiguity" in direct,
        "direct packet does not claim endpoint closure",
    )


def part2_exact_source_factor_algebra() -> None:
    print("\n" + "=" * 72)
    print("PART 2: Exact Source-Factor Algebra")
    print("=" * 72)

    data = restricted_readout_data()
    p0 = reduced_map(RHO_ZERO)
    p_star = reduced_map(RHO_STAR)
    theorem_lands = theorem_target_lands(data)

    expected_e_shell = np.array([1.0, 0.0, 0.0, 0.0])
    expected_e_center = np.array([1.0, 0.0, 1.0 / 6.0, 0.0])
    expected_t_shell = np.array([0.0, 1.0, 0.0, 0.0])
    expected_t_center = np.array([0.0, 1.0, 0.0, 1.0 / 6.0])

    check(
        "restricted carrier columns match the exact shell/center basis",
        np.max(np.abs(data.carrier_e_shell - expected_e_shell)) < EXACT_TOL
        and np.max(np.abs(data.carrier_e_center - expected_e_center)) < EXACT_TOL
        and np.max(np.abs(data.carrier_t_shell - expected_t_shell)) < EXACT_TOL
        and np.max(np.abs(data.carrier_t_center - expected_t_center)) < EXACT_TOL,
        "E-shell, E-center, T-shell, T-center columns are exact",
    )
    check(
        "rho_E=0 gives q_E=1 and rho_E=21/4 gives q_E=15/8 exactly",
        q_e(RHO_ZERO) == Fraction(1, 1) and q_e(RHO_STAR) == Fraction(15, 8),
        f"q0={q_e(RHO_ZERO)}, qstar={q_e(RHO_STAR)}",
    )
    check(
        "the E-center source-factor separation is exactly 7/8",
        q_e(RHO_STAR) - q_e(RHO_ZERO) == DELTA_Q,
        f"Delta q_E={DELTA_Q}",
    )

    shell0 = p0 @ data.carrier_e_shell
    shell_star = p_star @ data.carrier_e_shell
    center0 = p0 @ data.carrier_e_center
    center_star = p_star @ data.carrier_e_center
    t_shell0 = p0 @ data.carrier_t_shell
    t_shell_star = p_star @ data.carrier_t_shell
    t_center0 = p0 @ data.carrier_t_center
    t_center_star = p_star @ data.carrier_t_center

    print(f"  P(0)      E-center = {np.array2string(center0, precision=12, floatmode='fixed')}")
    print(f"  P(21/4)   E-center = {np.array2string(center_star, precision=12, floatmode='fixed')}")
    print(f"  Delta q_E           = {DELTA_Q}")

    check(
        "varying rho_E leaves the E-shell source factor fixed",
        np.max(np.abs(shell0 - shell_star)) < EXACT_TOL and np.max(np.abs(shell0 - np.array([1.0, 0.0]))) < EXACT_TOL,
        f"shell residual={np.max(np.abs(shell0 - shell_star)):.3e}",
    )
    check(
        "varying rho_E changes only the E-center source factor",
        np.max(np.abs(center0 - np.array([1.0, 0.0]))) < EXACT_TOL
        and np.max(np.abs(center_star - np.array([15.0 / 8.0, 0.0]))) < EXACT_TOL,
        "E-center factors are 1 and 15/8",
    )
    check(
        "varying rho_E leaves the T-shell source factor fixed",
        np.max(np.abs(t_shell0 - t_shell_star)) < EXACT_TOL
        and np.max(np.abs(t_shell0 - np.array([0.0, -2.0]))) < EXACT_TOL,
        f"T-shell residual={np.max(np.abs(t_shell0 - t_shell_star)):.3e}",
    )
    check(
        "varying rho_E leaves the T-center source factor fixed",
        np.max(np.abs(t_center0 - t_center_star)) < EXACT_TOL
        and np.max(np.abs(t_center0 - np.array([0.0, -5.0 / 3.0]))) < EXACT_TOL,
        f"T-center residual={np.max(np.abs(t_center0 - t_center_star)):.3e}",
    )
    check(
        "the live current-surface readout theorem still does not land",
        not theorem_lands,
        "this runner is a direct-consumer boundary, not an endpoint-triple derivation",
    )


def part3_time_coupling_inheritance() -> None:
    print("\n" + "=" * 72)
    print("PART 3: Exact Time-Coupling Inheritance")
    print("=" * 72)

    data = restricted_readout_data()
    backbone = route2_slice_backbone()
    p0 = reduced_map(RHO_ZERO)
    p_star = reduced_map(RHO_STAR)

    lambda_sym_err = float(np.max(np.abs(backbone.lambda_sym - backbone.lambda_sym.T)))
    lambda_min = float(np.min(np.linalg.eigvalsh(backbone.lambda_sym)))
    check(
        "the shared Route-2 slice generator is symmetric positive definite",
        lambda_sym_err < EXACT_TOL and lambda_min > 0.0,
        f"symmetry={lambda_sym_err:.3e}, min_eig={lambda_min:.6e}",
    )

    for t in TIMES:
        tf = f_float(t)
        seed = v_r(backbone, tf)
        seed_norm = float(np.linalg.norm(seed))

        shell_delta = float(
            np.linalg.norm(
                xi_p(p_star, data.carrier_e_shell, seed)
                - xi_p(p0, data.carrier_e_shell, seed)
            )
        )
        center_zero = xi_p(p0, data.carrier_e_center, seed)
        center_star = xi_p(p_star, data.carrier_e_center, seed)
        center_delta = float(np.linalg.norm(center_star - center_zero))
        expected_delta = f_float(DELTA_Q) * seed_norm
        scale_err = float(np.max(np.abs(center_star - f_float(q_e(RHO_STAR)) * center_zero)))

        check(
            f"at t={tf:g}, the slice seed is nonzero",
            seed_norm > 0.0,
            f"||V_R(t)||={seed_norm:.12e}",
        )
        check(
            f"at t={tf:g}, E-shell time coupling is rho_E-invariant",
            shell_delta < EXACT_TOL,
            f"shell tensor delta={shell_delta:.3e}",
        )
        check(
            f"at t={tf:g}, E-center tensor separation is exactly (7/8)||V_R(t)||",
            abs(center_delta - expected_delta) < 1.0e-10,
            f"observed={center_delta:.12e}, expected={expected_delta:.12e}",
        )
        check(
            f"at t={tf:g}, rho_E=21/4 scales the rho_E=0 E-center tensor by 15/8",
            scale_err < 1.0e-10,
            f"scale residual={scale_err:.3e}",
        )


def part4_one_dimensional_boundary() -> None:
    print("\n" + "=" * 72)
    print("PART 4: One-Dimensional Direct-Consumer Boundary")
    print("=" * 72)

    data = restricted_readout_data()
    backbone = route2_slice_backbone()
    p0 = reduced_map(RHO_ZERO)
    p_star = reduced_map(RHO_STAR)
    delta_p = p_star - p0

    source_deltas = np.column_stack(
        [
            delta_p @ data.carrier_e_shell,
            delta_p @ data.carrier_e_center,
            delta_p @ data.carrier_t_shell,
            delta_p @ data.carrier_t_center,
        ]
    )
    rank = int(np.linalg.matrix_rank(source_deltas, tol=EXACT_TOL))

    check(
        "the rho_E ambiguity is rank-one on the restricted source columns",
        rank == 1 and np.max(np.abs(source_deltas[:, 1] - np.array([7.0 / 8.0, 0.0]))) < EXACT_TOL,
        f"source-delta rank={rank}",
    )
    check(
        "only the E-center column carries the rho_E source delta",
        np.max(np.abs(source_deltas[:, [0, 2, 3]])) < EXACT_TOL
        and np.linalg.norm(source_deltas[:, 1]) > 0.0,
        "E-shell, T-shell, and T-center deltas vanish",
    )

    tensor_deltas = []
    for t in TIMES:
        seed = v_r(backbone, f_float(t))
        tensor_deltas.append(
            xi_p(p_star, data.carrier_e_center, seed)
            - xi_p(p0, data.carrier_e_center, seed)
        )

    min_delta_norm = min(float(np.linalg.norm(delta)) for delta in tensor_deltas)
    check(
        "the same nonzero slice factor prevents cancellation at every checked time",
        min_delta_norm > 0.0,
        f"minimum E-center tensor delta over checked times={min_delta_norm:.12e}",
    )
    check(
        "the parent S3 target remains upstream readout selection rather than a new slice law",
        "The next theorem target is the missing readout-map endpoint triple" in text(PARENT_NOTE)
        and "A future positive" in text(DIRECT_NOTE)
        and "attack the upstream readout selector" in text(DIRECT_NOTE),
        "direct-consumer packet points back to rho_E selection",
    )


def main() -> int:
    print("Route-2 time-coupling direct-consumer ambiguity gate")
    print("=" * 72)

    part1_source_surfaces()
    part2_exact_source_factor_algebra()
    part3_time_coupling_inheritance()
    part4_one_dimensional_boundary()

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print("Status: direct-consumer no-go/support boundary; endpoint triple remains open.")
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
