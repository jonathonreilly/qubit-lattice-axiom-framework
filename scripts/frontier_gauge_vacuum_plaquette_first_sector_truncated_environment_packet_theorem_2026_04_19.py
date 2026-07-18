#!/usr/bin/env python3
"""Finite supplied diagonal coefficient packet from the completed triple.

The normalization/reconstruction algebra is exact for the supplied vector.
The decimal packet is a finite numerical witness and is not identified with
the physical stripped Wilson residual.
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
from frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization import (
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


def main() -> int:
    print("=" * 112)
    print("GAUGE-VACUUM PLAQUETTE FIRST-SECTOR SUPPLIED COEFFICIENT PACKET")
    print("=" * 112)
    print()
    print("Question:")
    print("  Does the completed first-sector triple determine one supplied finite")
    print("  coefficient packet, without identifying it as a physical Wilson")
    print("  residual or environment operator?")

    source_exact = source_factorization_exact_small_case()
    v_min, z_min = completed_sector_data()
    z00_min = float(v_min[0])
    rho_packet = v_min / z00_min

    sample_angles = [(u1 * np.pi / 16.0, u2 * np.pi / 16.0) for u1, u2 in sample_angle_units().values()]
    e_three = evaluation_matrix([(0, 0), (1, 0), (0, 1), (1, 1)], sample_angles)
    z_recon = np.real_if_close(z00_min * (e_three @ rho_packet)).real
    recon_gap = float(np.linalg.norm(z_recon - z_min))
    rho_swap_gap = float(abs(rho_packet[1] - rho_packet[2]))

    print()
    print(f"  v_min                                       = {np.round(v_min, 12).tolist()}")
    print(f"  z00_min                                     = {z00_min:.12f}")
    print(f"  rho_packet                                  = {np.round(rho_packet, 12).tolist()}")
    print(f"  reconstructed sample triple                 = {np.round(z_recon, 12).tolist()}")
    print(f"  reconstruction gap                          = {recon_gap:.6e}")
    print()

    check(
        "The source theorem verifies its supplied-diagonal matrix and Gram identities exactly",
        bool(source_exact["formula_exact"])
        and bool(source_exact["gram_exact"])
        and bool(source_exact["rank_kernel_exact"]),
    )
    check(
        "The completion producers return one finite four-coefficient vector and one finite three-sample target",
        v_min.shape == (4,)
        and z_min.shape == (3,)
        and np.all(np.isfinite(v_min))
        and np.all(np.isfinite(z_min))
        and z00_min > 0.0,
    )
    check(
        "Normalizing by the supplied trivial-channel coefficient defines a finite packet with rho_(0,0)=1",
        abs(rho_packet[0] - 1.0) < 1.0e-12 and rho_packet[1] > 0.0 and rho_packet[3] > -1.0e-12,
        f"rho_packet={np.round(rho_packet, 10).tolist()}",
    )
    check(
        "The supplied packet is conjugation-symmetric on the first-symmetric sector",
        rho_swap_gap < 1.0e-12,
        f"|rho_(1,0)-rho_(0,1)|={rho_swap_gap:.3e}",
    )
    check(
        "The supplied three-sample triple reconstructs to floating-point tolerance from (z00_min, rho_packet)",
        recon_gap < 1.0e-12,
        f"||z_recon-Z_min||={recon_gap:.3e}",
    )
    check(
        "The finite packet witness composes with the exact supplied-diagonal output surface",
        recon_gap < 1.0e-12
        and e_three.shape == (3, 4)
        and bool(source_exact["positive_case_exact"])
        and bool(source_exact["zero_case_exact"]),
        f"z00_min={z00_min:.6f}",
    )

    print("\n" + "=" * 112)
    print("RESULT")
    print("=" * 112)
    print("  Conditional finite-packet refinement:")
    print("    - the completed first-sector triple already determines one explicit")
    print("      supplied diagonal coefficient packet on the first-symmetric sector")
    print("    - namely one overall scale z00_min together with one normalized")
    print("      conjugation-symmetric coefficient packet rho_packet")
    print("    - Wilson residual diagonality/identification and full-weight extension")
    print("      remain open; this runner proves neither")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
