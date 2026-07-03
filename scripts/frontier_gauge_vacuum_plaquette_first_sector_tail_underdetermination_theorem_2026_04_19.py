#!/usr/bin/env python3
"""
Executable repair for first-sector tail underdetermination.

The archived source note named this runner, but the file was absent.  This
version constructs two factorized-class extensions of the same retained
first-sector packet:

1. the zero extension rho_0;
2. a nonnegative conjugation-symmetric exponentially decaying tail extension.

The retained four-weight packet and three-sample triple are identical, but the
same source operator J sees different Perron/Jacobi packets.  This restores the
missing executable separation without retagging the audited row.
"""

from __future__ import annotations

import sys

import numpy as np

from frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_principle_theorem_2026_04_19 import (
    RETAINED_SUPPORT,
    retained_packet,
    transfer_from_packet,
    zero_extension,
)
from frontier_gauge_vacuum_plaquette_first_sector_rank_one_transfer_realization_2026_04_19 import (
    completed_sector_data,
)
from frontier_gauge_vacuum_plaquette_first_three_sample_environment_evaluator_route_2026_04_17 import (
    sample_angle_units,
)
from frontier_gauge_vacuum_plaquette_perron_jacobi_underdetermination import (
    dominant_eigenpair,
    lanczos_jacobi,
    moments,
)
from frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_2026_04_17 import (
    evaluation_matrix,
)
from frontier_gauge_vacuum_plaquette_spatial_environment_character_measure import (
    build_recurrence_matrix,
    conjugation_swap_matrix,
)


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


def decaying_tail_extension(
    rho0: np.ndarray,
    weights: list[tuple[int, int]],
    index: dict[tuple[int, int], int],
    epsilon: float = 2.0,
    alpha: float = 0.25,
    gamma: float = 0.08,
) -> np.ndarray:
    retained = {index[w] for w in RETAINED_SUPPORT}
    rho = np.array(rho0, dtype=float)
    for i, (p, q) in enumerate(weights):
        if i in retained:
            continue
        rho[i] += epsilon * np.exp(-alpha * (p + q) - gamma * ((p - q) ** 2))
    return rho


def retained_vector(rho: np.ndarray, index: dict[tuple[int, int], int]) -> np.ndarray:
    return np.array([rho[index[w]] for w in RETAINED_SUPPORT], dtype=float)


def retained_samples(rho: np.ndarray, index: dict[tuple[int, int], int], z00: float) -> np.ndarray:
    angles = [(u1 * np.pi / 16.0, u2 * np.pi / 16.0) for u1, u2 in sample_angle_units().values()]
    sample_mat = evaluation_matrix(list(RETAINED_SUPPORT), angles)
    return np.real_if_close(z00 * (sample_mat @ retained_vector(rho, index))).real


def transfer_diagnostics(transfer: np.ndarray, swap: np.ndarray) -> dict[str, float]:
    eigvals = np.linalg.eigvalsh(transfer)
    return {
        "sym_gap": float(np.max(np.abs(transfer - transfer.T))),
        "swap_gap": float(np.max(np.abs(swap @ transfer - transfer @ swap))),
        "eig_min": float(eigvals[0]),
        "lambda_top": float(eigvals[-1]),
        "spectral_gap": float(eigvals[-1] - eigvals[-2]),
        "entry_min": float(np.min(transfer)),
    }


def perron_packet(transfer: np.ndarray, source: np.ndarray) -> dict[str, object]:
    lam, psi = dominant_eigenpair(transfer)
    mom = moments(source, psi, 5)
    alpha, beta = lanczos_jacobi(source, psi, 6)
    return {
        "lambda": lam,
        "psi": psi,
        "moments": mom,
        "alpha": alpha,
        "beta": beta,
    }


def main() -> int:
    print("=" * 112)
    print("GAUGE-VACUUM PLAQUETTE FIRST-SECTOR TAIL UNDERDETERMINATION")
    print("=" * 112)
    print()
    print("Question:")
    print("  Can two factorized-class extensions agree on the retained first-sector")
    print("  packet and sample triple while inducing different Perron/Jacobi data?")

    rho_ret, z00 = retained_packet()
    _v_min, z_min = completed_sector_data()
    jmat, weights, index = build_recurrence_matrix(5)
    swap = conjugation_swap_matrix(weights, index)
    retained = {index[w] for w in RETAINED_SUPPORT}

    rho0 = zero_extension(weights, index, rho_ret)
    rho_tail = decaying_tail_extension(rho0, weights, index)
    delta = rho_tail - rho0
    nonret_delta = np.array([delta[i] for i in range(len(weights)) if i not in retained], dtype=float)

    z_zero = retained_samples(rho0, index, z00)
    z_tail = retained_samples(rho_tail, index, z00)
    retained_gap = float(np.linalg.norm(retained_vector(rho0, index) - retained_vector(rho_tail, index)))
    z_zero_gap = float(np.linalg.norm(z_zero - z_min))
    z_tail_gap = float(np.linalg.norm(z_tail - z_min))
    z_pair_gap = float(np.linalg.norm(z_zero - z_tail))

    t0 = transfer_from_packet(weights, rho0)
    t_tail = transfer_from_packet(weights, rho_tail)
    diag0 = transfer_diagnostics(t0, swap)
    diag_tail = transfer_diagnostics(t_tail, swap)

    packet0 = perron_packet(t0, jmat)
    packet_tail = perron_packet(t_tail, jmat)
    psi0 = np.asarray(packet0["psi"], dtype=float)
    psi_tail = np.asarray(packet_tail["psi"], dtype=float)
    moments0 = list(packet0["moments"])
    moments_tail = list(packet_tail["moments"])
    alpha0 = list(packet0["alpha"])
    alpha_tail = list(packet_tail["alpha"])
    beta0 = list(packet0["beta"])
    beta_tail = list(packet_tail["beta"])

    psi_gap = float(np.linalg.norm(psi_tail - psi0))
    m1_gap = abs(float(moments_tail[1]) - float(moments0[1]))
    m2_gap = abs(float(moments_tail[2]) - float(moments0[2]))
    alpha0_gap = abs(float(alpha_tail[0]) - float(alpha0[0]))
    beta1_gap = abs(float(beta_tail[0]) - float(beta0[0]))
    tail_swap_gap = 0.0
    for i, (p, q) in enumerate(weights):
        tail_swap_gap = max(tail_swap_gap, abs(float(rho_tail[i]) - float(rho_tail[index[(q, p)]])))

    print()
    print(f"  z00_min                                    = {z00:.12f}")
    print(f"  retained packet                            = {np.round(rho_ret, 12).tolist()}")
    print(f"  non-retained tail min/max/mass             = {float(np.min(nonret_delta)):.6e} / {float(np.max(nonret_delta)):.6e} / {float(np.sum(nonret_delta)):.6e}")
    print(f"  retained packet gap zero-vs-tail           = {retained_gap:.3e}")
    print(f"  retained sample gaps zero/tail/pair        = {z_zero_gap:.3e} / {z_tail_gap:.3e} / {z_pair_gap:.3e}")
    print(f"  zero transfer diagnostics                  = {diag0}")
    print(f"  tail transfer diagnostics                  = {diag_tail}")
    print()
    print("  Perron/Jacobi comparison for the same source operator J:")
    print(f"    lambda zero/tail                         = {packet0['lambda']:.12f} / {packet_tail['lambda']:.12f}")
    print(f"    m1 zero/tail                             = {moments0[1]:.12f} / {moments_tail[1]:.12f}")
    print(f"    m2 zero/tail                             = {moments0[2]:.12f} / {moments_tail[2]:.12f}")
    print(f"    alpha0 zero/tail                         = {alpha0[0]:.12f} / {alpha_tail[0]:.12f}")
    print(f"    beta1 zero/tail                          = {beta0[0]:.12f} / {beta_tail[0]:.12f}")
    print(f"    gaps psi/m1/m2/alpha0/beta1              = {psi_gap:.3e} / {m1_gap:.3e} / {m2_gap:.3e} / {alpha0_gap:.3e} / {beta1_gap:.3e}")
    print()

    check(
        "The zero extension and decaying-tail extension have exactly the same retained first-sector packet",
        retained_gap < 1.0e-14,
        f"retained_gap={retained_gap:.3e}",
    )
    check(
        "Both extensions reproduce the completed three-sample triple on the retained projection",
        z_zero_gap < 1.0e-12 and z_tail_gap < 1.0e-12 and z_pair_gap < 1.0e-14,
        f"(zero,tail,pair)=({z_zero_gap:.3e},{z_tail_gap:.3e},{z_pair_gap:.3e})",
    )
    check(
        "The tail extension is nonnegative, conjugation-symmetric, and strictly positive on every non-retained weight in the sampled box",
        float(np.min(rho_tail)) >= 0.0
        and float(np.min(nonret_delta)) > 0.0
        and tail_swap_gap < 1.0e-14,
        f"(tail_min,delta_min,swap_gap)=({float(np.min(rho_tail)):.3e},{float(np.min(nonret_delta)):.3e},{tail_swap_gap:.3e})",
    )
    check(
        "Both factorized-class transfers are self-adjoint, conjugation-symmetric, and positive semidefinite on the truncated box",
        diag0["sym_gap"] < 1.0e-12
        and diag_tail["sym_gap"] < 1.0e-12
        and diag0["swap_gap"] < 1.0e-12
        and diag_tail["swap_gap"] < 1.0e-12
        and diag0["eig_min"] > -1.0e-12
        and diag_tail["eig_min"] > -1.0e-12,
        f"eigmins=({diag0['eig_min']:.3e},{diag_tail['eig_min']:.3e})",
    )
    check(
        "The Perron states are numerically unique and separated for the same source operator J",
        diag0["spectral_gap"] > 1.0
        and diag_tail["spectral_gap"] > 1.0
        and psi_gap > 5.0e-4,
        f"(gaps,psi_gap)=({diag0['spectral_gap']:.3e},{diag_tail['spectral_gap']:.3e},{psi_gap:.3e})",
    )
    check(
        "The induced Perron moments and Jacobi coefficients differ while the retained packet is unchanged",
        m1_gap > 2.0e-4
        and m2_gap > 2.0e-4
        and alpha0_gap > 2.0e-4
        and beta1_gap > 2.0e-5,
        f"(m1,m2,alpha0,beta1)=({m1_gap:.3e},{m2_gap:.3e},{alpha0_gap:.3e},{beta1_gap:.3e})",
    )

    print("\n" + "=" * 112)
    print("RESULT")
    print("=" * 112)
    print("  Executable underdetermination restored:")
    print("    - the zero extension and positive decaying-tail extension have the")
    print("      same retained first-sector packet and the same retained samples")
    print("    - the same source operator J reads different Perron/Jacobi packets")
    print("    - therefore the retained first-sector projection alone does not")
    print("      determine the higher-tail Perron/Jacobi data")
    print("    - this runner restores the missing executable artifact for re-audit")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
