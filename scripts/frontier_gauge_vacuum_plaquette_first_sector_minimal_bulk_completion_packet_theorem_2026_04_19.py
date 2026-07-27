#!/usr/bin/env python3
"""
Selected Wilson/Perron packet on the bounded zero-extension branch.

The sibling principle proves that the zero extension is the unique minimal
packet on its finite tail cone.  This runner does not infer that status from
substrings in the sibling note; it directly checks that the selected packet
has zero tail and then computes the explicit first-layer packet on that
branch.
"""

from __future__ import annotations

import math
import sys

import numpy as np

from frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_principle_theorem_2026_04_19 import (
    RETAINED_SUPPORT,
    retained_packet,
    zero_extension,
)
from frontier_gauge_vacuum_plaquette_first_sector_zero_extension_factorized_class_theorem_2026_04_19 import (
    local_factor_diagonal,
)
from frontier_gauge_vacuum_plaquette_perron_reduction_theorem import (
    dominant_eigenpair,
    lanczos_jacobi,
)
from frontier_gauge_vacuum_plaquette_spatial_environment_character_measure import (
    BETA,
    build_recurrence_matrix,
    conjugation_swap_matrix,
    matrix_exponential_symmetric,
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


def selected_transfer_and_packet() -> dict[str, np.ndarray | float]:
    rho_ret, _z00 = retained_packet()
    jmat, weights, index = build_recurrence_matrix(5)
    swap = conjugation_swap_matrix(weights, index)
    rho_ext = zero_extension(weights, index, rho_ret)
    tail_indices = [i for i, weight in enumerate(weights) if weight not in RETAINED_SUPPORT]
    multiplier = matrix_exponential_symmetric(jmat, BETA / 2.0)
    d_local = local_factor_diagonal(weights)
    transfer = multiplier @ d_local @ np.diag(rho_ext) @ multiplier
    eig, psi = dominant_eigenpair(transfer)
    alpha, beta, _basis = lanczos_jacobi(jmat, psi, 6)
    m1 = float(psi @ (jmat @ psi))
    m2 = float(psi @ (jmat @ (jmat @ psi)))
    beta1 = math.sqrt(max(m2 - m1 * m1, 0.0))
    return {
        "jmat": jmat,
        "swap": swap,
        "rho_ext": rho_ext,
        "tail_max": float(np.max(np.abs(rho_ext[tail_indices]))),
        "transfer": transfer,
        "eig": float(eig),
        "psi": psi,
        "alpha0": float(alpha[0]),
        "beta1": float(beta[0]),
        "m1": m1,
        "m2": m2,
        "beta1_from_moments": beta1,
    }


def main() -> int:
    print("=" * 118)
    print("GAUGE-VACUUM PLAQUETTE FIRST-SECTOR MINIMAL-BULK COMPLETION PACKET")
    print("=" * 118)
    print()
    print("Question:")
    print("  What explicit Wilson/Perron first-layer packet is obtained on the")
    print("  finite-cone zero-extension branch of the minimal-bulk principle?")

    pkg = selected_transfer_and_packet()
    transfer = np.asarray(pkg["transfer"], dtype=float)
    swap = np.asarray(pkg["swap"], dtype=float)
    psi = np.asarray(pkg["psi"], dtype=float)
    sym_err = float(np.max(np.abs(transfer - transfer.T)))
    swap_err = float(np.max(np.abs(swap @ transfer - transfer @ swap)))
    psi_swap_err = float(np.linalg.norm(swap @ psi - psi))
    eig_min = float(np.min(np.linalg.eigvalsh(transfer)))

    print()
    print(f"  selected alpha0,beta1                       = ({pkg['alpha0']:.12f}, {pkg['beta1']:.12f})")
    print(f"  selected m1,m2                              = ({pkg['m1']:.12f}, {pkg['m2']:.12f})")
    print(f"  Perron eigenvalue                           = {pkg['eig']:.12f}")
    print(f"  transfer symmetry/swap/Perron-swap errors   = ({sym_err:.3e}, {swap_err:.3e}, {psi_swap_err:.3e})")
    print(f"  min eigenvalue(T_sel)                       = {eig_min:.6e}")
    print()

    check(
        "The selected finite-box packet directly has zero mass in every non-retained slot",
        pkg["tail_max"] == 0.0,
        f"max_abs_tail={pkg['tail_max']:.1e}",
    )
    check(
        "That selected extension yields one positive self-adjoint conjugation-symmetric factorized transfer operator",
        sym_err < 1.0e-12 and swap_err < 1.0e-12 and eig_min > -1.0e-12,
        f"(sym,swap,eig_min)=({sym_err:.3e},{swap_err:.3e},{eig_min:.3e})",
    )
    check(
        "Its Perron state is conjugation-symmetric and therefore defines one explicit first-layer Wilson/Perron packet",
        psi_swap_err < 1.0e-12 and np.min(psi) >= -1.0e-12,
        f"psi_swap={psi_swap_err:.3e}",
    )
    check(
        "The selected first Jacobi layer is equivalent to the first-Hankel packet by alpha0=m1 and beta1^2=m2-m1^2",
        abs(pkg["alpha0"] - pkg["m1"]) < 1.0e-12
        and abs(pkg["beta1"] - pkg["beta1_from_moments"]) < 1.0e-12,
        f"(alpha0,beta1)=({pkg['alpha0']:.6f},{pkg['beta1']:.6f})",
    )
    check(
        "So on the finite-cone zero-extension branch, the Wilson-side first-layer packet is explicit",
        pkg["beta1"] > 0.0,
        f"(m1,m2)=({pkg['m1']:.6f},{pkg['m2']:.6f})",
    )

    print("\n" + "=" * 118)
    print("RESULT")
    print("=" * 118)
    print("  Selected Wilson/Perron packet on the finite-cone zero-extension branch:")
    print(f"    - alpha0 = {pkg['alpha0']:.15f}")
    print(f"    - beta1  = {pkg['beta1']:.15f}")
    print(f"    - m1     = {pkg['m1']:.15f}")
    print(f"    - m2     = {pkg['m2']:.15f}")
    print("    - this is now the explicit first-layer packet of the selected")
    print("      factorized-class finite-cone zero-extension branch")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
