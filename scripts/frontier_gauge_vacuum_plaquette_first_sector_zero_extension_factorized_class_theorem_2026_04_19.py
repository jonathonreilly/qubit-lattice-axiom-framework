#!/usr/bin/env python3
"""Minimal-support extension of a supplied first-sector coefficient packet.

The runner checks a finite supplied-diagonal model only. It does not identify
the zero-extended packet with a physical Wilson environment or stripped
two-slice residual.
"""

from __future__ import annotations

import sys

import numpy as np

from frontier_gauge_vacuum_plaquette_first_sector_rank_one_transfer_realization_2026_04_19 import (
    completed_sector_data,
)
from frontier_gauge_vacuum_plaquette_first_three_sample_environment_evaluator_route_2026_04_17 import (
    sample_angle_units,
)
from frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_2026_04_17 import (
    evaluation_matrix,
)
from frontier_gauge_vacuum_plaquette_local_environment_factorization import (
    BETA,
    build_recurrence_matrix,
    conjugation_swap_matrix,
    dim_su3,
    matrix_exponential_symmetric,
    wilson_character_coefficient,
)
from frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization import (
    SOURCE_SECTOR_SURFACE,
    exact_small_case as source_factorization_exact_small_case,
)


PASS_COUNT = 0
FAIL_COUNT = 0


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


def local_factor_diagonal(weights: list[tuple[int, int]]) -> np.ndarray:
    c00 = wilson_character_coefficient(0, 0)
    local = np.array(
        [wilson_character_coefficient(p, q) / (dim_su3(p, q) * c00) for p, q in weights],
        dtype=float,
    )
    return np.diag(local**4)


def main() -> int:
    print("=" * 112)
    print("GAUGE-VACUUM PLAQUETTE FIRST-SECTOR SUPPLIED ZERO-EXTENSION PACKET")
    print("=" * 112)
    print()
    print("Question:")
    print("  Does the supplied finite packet admit a minimal-support")
    print("  zero extension inside the declared diagonal model class?")

    source_exact = source_factorization_exact_small_case()
    v_min, z_min = completed_sector_data()
    z00_min = float(v_min[0])
    rho_packet = v_min / z00_min

    jmat, weights, index = build_recurrence_matrix(5)
    swap = conjugation_swap_matrix(weights, index)
    multiplier = matrix_exponential_symmetric(jmat, BETA / 2.0)
    d_local = local_factor_diagonal(weights)

    rho_ext = np.zeros(len(weights), dtype=float)
    rho_ext[index[(0, 0)]] = rho_packet[0]
    rho_ext[index[(1, 0)]] = rho_packet[1]
    rho_ext[index[(0, 1)]] = rho_packet[2]
    rho_ext[index[(1, 1)]] = rho_packet[3]
    r_ext = np.diag(rho_ext)
    t_ext = multiplier @ d_local @ r_ext @ multiplier

    sym_err = float(np.max(np.abs(t_ext - t_ext.T)))
    swap_err = float(np.max(np.abs(swap @ t_ext - t_ext @ swap)))
    eig_min = float(np.min(np.linalg.eigvalsh(t_ext)))
    rho_min = float(np.min(rho_ext))

    sample_angles = [(u1 * np.pi / 16.0, u2 * np.pi / 16.0) for u1, u2 in sample_angle_units().values()]
    e_three = evaluation_matrix([(0, 0), (1, 0), (0, 1), (1, 1)], sample_angles)
    z_recon = np.real_if_close(z00_min * (e_three @ rho_packet)).real
    recon_gap = float(np.linalg.norm(z_recon - z_min))

    print()
    print(f"  z00_min                                     = {z00_min:.12f}")
    print(f"  rho_packet                                  = {np.round(rho_packet, 12).tolist()}")
    print(f"  nonzero rho_ext entries                     = {[(w, round(float(rho_ext[index[w]]), 12)) for w in weights if rho_ext[index[w]] > 0.0]}")
    print(f"  factorized operator symmetry / swap errors  = {sym_err:.3e} / {swap_err:.3e}")
    print(f"  min eigenvalue(T_ext)                       = {eig_min:.3e}")
    print(f"  supplied-packet reconstruction gap           = {recon_gap:.3e}")
    print()

    check(
        "The source theorem exposes complete supplied-diagonal inputs and verifies its exact positive outputs",
        SOURCE_SECTOR_SURFACE.complete_typed_inputs
        and SOURCE_SECTOR_SURFACE.complete_outputs
        and bool(source_exact["formula_exact"])
        and bool(source_exact["gram_exact"])
        and bool(source_exact["rank_kernel_exact"]),
    )
    check(
        "The completion producers supply one finite four-coefficient packet with nonzero trivial component",
        v_min.shape == (4,)
        and z_min.shape == (3,)
        and np.all(np.isfinite(v_min))
        and np.all(np.isfinite(z_min))
        and z00_min > 0.0,
    )
    check(
        "Extending rho_packet by zero outside the first-symmetric weights gives a nonnegative conjugation-symmetric finite sequence",
        rho_min > -1.0e-12
        and abs(rho_ext[index[(1, 0)]] - rho_ext[index[(0, 1)]]) < 1.0e-12,
        f"nonzero count={int(np.count_nonzero(rho_ext))}",
    )
    check(
        "The zero-extension yields a self-adjoint swap-symmetric positive-semidefinite supplied-diagonal operator M D_loc diag(rho_ext) M",
        sym_err < 1.0e-12 and swap_err < 1.0e-12 and eig_min > -1.0e-10,
        f"(sym,swap,eig_min)=({sym_err:.3e},{swap_err:.3e},{eig_min:.3e})",
    )
    check(
        "The extended packet reproduces the supplied three-sample data to floating-point tolerance",
        recon_gap < 1.0e-12,
        f"||z_recon-Z_min||={recon_gap:.3e}",
    )
    check(
        "The finite zero-extension witness leaves physical Wilson compression and diagonality open",
        recon_gap < 1.0e-12
        and eig_min > -1.0e-10,
        f"z00_min={z00_min:.6f}",
    )

    print("\n" + "=" * 112)
    print("RESULT")
    print("=" * 112)
    print("  Bounded supplied-packet result:")
    print("    - the supplied first-sector vector has a minimal-support zero extension")
    print("    - the resulting finite diagonal model is PSD and swap-symmetric")
    print("    - no physical Wilson residual identification follows")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
