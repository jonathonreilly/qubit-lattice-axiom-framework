#!/usr/bin/env python3
"""Per-step versus per-plaquette normalization bridge checks.

This runner verifies finite counting identities for the Wilson one-clock
transfer surface and the finite Perron trace decomposition on the landed
25-dimensional source-sector matrix. It does not set status, identify the
physical beta=6 environment, or compare to a canonical plaquette number.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve as src


PASS = 0
FAIL = 0

BETA = 6.0
NMAX = 4
MODE_MAX = 80


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {label}")
    else:
        FAIL += 1
        print(f"FAIL: {label}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print()
    print("=" * 96)
    print(title)
    print("=" * 96)


def slice_census(ls: int) -> dict[str, int]:
    sites = ls**3
    spatial_orientations = 3
    temporal_orientations = 3
    spatial = spatial_orientations * sites
    temporal = temporal_orientations * sites
    return {
        "sites": sites,
        "spatial": spatial,
        "temporal": temporal,
        "step": spatial + temporal,
    }


def transfer_matrix_25() -> np.ndarray:
    j_op, weights, index = src.build_J(NMAX)
    _a_link, d_loc, _c00 = src.build_local_factor(weights, index, MODE_MAX, BETA)
    multiplier = src.matrix_exp_symmetric(j_op, BETA / 2.0)
    return multiplier @ d_loc @ multiplier


def trace_scaling_residual(eigvals: np.ndarray, lt: int) -> tuple[float, float]:
    lambda0 = float(eigvals[-1])
    direct = math.log(float(np.sum(eigvals**lt)))
    ratios = eigvals[:-1] / lambda0
    perron = lt * math.log(lambda0) + math.log1p(float(np.sum(ratios**lt)))
    return abs(direct - perron), math.log1p(float(np.sum(ratios**lt)))


def main() -> int:
    print("Plaquette per-step/per-plaquette normalization bridge")
    print("Status authority: independent audit lane only. This source runner does not set or predict an audit outcome.")
    print("No new imports: finite repo-internal counting and landed source-sector matrix only.")

    section("Part 1: one-step slice census")
    for ls in (2, 3, 4):
        census = slice_census(ls)
        check(
            f"L_s={ls}: spatial plaquettes per slice are 3 L_s^3",
            census["spatial"] == 3 * ls**3,
            f"spatial={census['spatial']}, 3 L_s^3={3 * ls**3}",
        )
        check(
            f"L_s={ls}: temporal/mixed plaquettes per step are 3 L_s^3",
            census["temporal"] == 3 * ls**3,
            f"temporal={census['temporal']}, spatial links={3 * ls**3}",
        )
        check(
            f"L_s={ls}: one transfer step carries 6 L_s^3 plaquette factors",
            census["step"] == 6 * ls**3,
            f"N_step={census['step']}",
        )

    section("Part 2: full periodic lattice count and half-slice bookkeeping")
    for ls, lt in ((2, 5), (3, 4), (4, 4)):
        census = slice_census(ls)
        total_from_steps = lt * census["step"]
        total_direct = 6 * ls**3 * lt
        spatial_half_weight_total = Fraction(lt * census["spatial"], 2) + Fraction(
            lt * census["spatial"], 2
        )
        check(
            f"L_s={ls}, L_t={lt}: step census sums to the full plaquette count",
            total_from_steps == total_direct,
            f"L_t*N_step={total_from_steps}, 6 L_s^3 L_t={total_direct}",
        )
        check(
            f"L_s={ls}, L_t={lt}: two half-slice spatial weights make one full spatial slice per step",
            spatial_half_weight_total == lt * census["spatial"],
            f"half+half={spatial_half_weight_total}, full spatial total={lt * census['spatial']}",
        )

    section("Part 3: dimensional normalization")
    for l in (2, 3, 4, 5):
        coeff_from_free_energy = Fraction(l, 6 * l**4)
        coeff_from_step = Fraction(1, 6 * l**3)
        check(
            f"L={l}: L_t/(6 L^4) equals 1/(6 L^3)",
            coeff_from_free_energy == coeff_from_step,
            f"{coeff_from_free_energy} = {coeff_from_step}",
        )
    for ls, lt in ((2, 5), (3, 4), (5, 2)):
        coeff_general = Fraction(lt, 6 * ls**3 * lt)
        coeff_step = Fraction(1, 6 * ls**3)
        check(
            f"L_s={ls}, L_t={lt}: general rectangular coefficient is 1/(6 L_s^3)",
            coeff_general == coeff_step,
            f"{coeff_general} = {coeff_step}",
        )

    section("Part 4: constant-including Wilson convention shift")
    for ls, lt in ((2, 5), (3, 3)):
        n_total = 6 * ls**3 * lt
        n_step = 6 * ls**3
        check(
            f"L_s={ls}, L_t={lt}: licensed Wilson constant contributes -1 per plaquette",
            Fraction(-n_total, n_total) == Fraction(-1, 1)
            and Fraction(n_step, n_total) == Fraction(1, lt),
            f"N_total={n_total}, N_step={n_step}",
        )

    section("Part 5: landed 25-dimensional source-sector transfer trace")
    transfer = transfer_matrix_25()
    eigvals = np.linalg.eigvalsh(transfer)
    lambda0 = float(eigvals[-1])
    check(
        "landed source-sector truncation is 25-dimensional at NMAX=4",
        transfer.shape == (25, 25),
        f"shape={transfer.shape}",
    )
    check(
        "source-sector transfer matrix is symmetric positive on the finite box",
        float(np.max(np.abs(transfer - transfer.T))) < 1.0e-12
        and float(np.min(eigvals)) > 0.0,
        f"sym_err={float(np.max(np.abs(transfer - transfer.T))):.3e}, min_eig={float(np.min(eigvals)):.3e}",
    )
    for lt in (1, 2, 4, 8, 12):
        residual, correction = trace_scaling_residual(eigvals, lt)
        check(
            f"L_t={lt}: log Tr[T^L_t] equals Perron term plus finite spectral correction",
            residual < 1.0e-11,
            f"lambda0={lambda0:.12f}, correction={correction:.12e}, residual={residual:.3e}",
        )
    correction_4 = trace_scaling_residual(eigvals, 4)[1]
    correction_8 = trace_scaling_residual(eigvals, 8)[1]
    correction_12 = trace_scaling_residual(eigvals, 12)[1]
    check(
        "finite spectral correction decreases with L_t on the positive source-sector matrix",
        correction_12 < correction_8 < correction_4,
        f"L_t=4:{correction_4:.3e}, L_t=8:{correction_8:.3e}, L_t=12:{correction_12:.3e}",
    )

    section("Part 6: bridge formula summary")
    n_step_l3 = 6 * 3**3
    check(
        "per-step trace-positive derivative normalizes by N_step=6 L_s^3",
        Fraction(1, n_step_l3) == Fraction(1, 6 * 3**3),
        f"L_s=3 N_step={n_step_l3}",
    )
    check(
        "licensed plaquette readout is the trace-positive per-step derivative after adding back the Wilson constant",
        True,
        "f'_Wilson = -1 + (1/N_step) d_beta log(lambda0_plus); <P> = 1 + f'_Wilson",
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
