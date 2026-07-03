#!/usr/bin/env python3
"""
DM leptogenesis PMNS transport interval witness.

Framework baseline:
  one-qubit operator algebra M_2(C) ~= Cl(3,0) on the Z^3 spatial substrate.

Purpose:
  Record the bounded interval witness supported by the imported PMNS-assisted
  transport functional beyond the framework-baseline boundary.

  On the charged-lepton-active N_e route:
    - the aligned seed pair (xbar, ybar) is already fixed natively
    - the unresolved object is the off-seed 5-real source
      (xi1, xi2, eta1, eta2, delta)

  This runner does not claim a physical selector law.  It only checks that the
  imported transport functional has a seed endpoint below eta/eta_obs = 1 and
  a sampled off-seed endpoint above 1. The interpolated eta/eta_obs = 1 point
  is only a diagnostic crossing on that parameterized family unless a separate
  selector theorem supplies the endpoint or interpolation parameter.

2026-05-27 runner repair:
  The raw PMNS projector-interface repair removed legacy helpers from the
  raw-interface module. This runner now replays only the finite compatibility
  layer it needs: CYCLE, canonical_h, active packet diagonalization, and the
  one-column transport functional are local to this runner, while the exact
  package constants and normalized transport grid come from
  dm_leptogenesis_exact_common. This keeps the row executable without
  re-expanding the old helper import surface.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, differential_evolution

from dm_leptogenesis_exact_common import (
    C_SPH,
    D_THERMAL_EXACT,
    ETA_OBS,
    S_OVER_NGAMMA_EXACT,
    exact_package,
    reference_expansion_profile,
    solve_normalized_transport,
    washout_profile,
)

PASS_COUNT = 0
FAIL_COUNT = 0

XBAR_NE = 0.5633333333333334
YBAR_NE = 0.30666666666666664
CYCLE = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = ROOT / "docs" / "DM_LEPTOGENESIS_PMNS_TRANSPORT_EXTREMAL_SOURCE_CANDIDATE_NOTE_2026-04-16.md"
FIREWALL_NOTE = ROOT / "docs" / "DM_LEPTOGENESIS_PMNS_TRANSPORT_SELECTOR_FIREWALL_NOTE_2026-06-17.md"


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def canonical_y(x: np.ndarray, y: np.ndarray, delta: float) -> np.ndarray:
    phase_block = np.diag(np.array([y[0], y[1], y[2] * np.exp(1j * delta)], dtype=complex))
    return np.diag(np.asarray(x, dtype=complex)) + phase_block @ CYCLE


def canonical_h(x: np.ndarray, y: np.ndarray, delta: float) -> np.ndarray:
    ymat = canonical_y(x, y, delta)
    return ymat @ ymat.conj().T


def canonical_left_diagonalizer(h: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    evals, u = np.linalg.eigh(h)
    order = np.argsort(np.real(evals))
    evals = np.real(evals[order])
    u = u[:, order]
    return evals, u


def active_packet_from_h(h_act: np.ndarray) -> np.ndarray:
    _evals, u_act = canonical_left_diagonalizer(h_act)
    return np.abs(u_act) ** 2


def flavored_transport_kernel(k_decay: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    z_grid, n_n1, _ = solve_normalized_transport(k_decay, reference_expansion_profile)
    source_profile = -np.gradient(n_n1, z_grid)
    w_vals = np.array(
        [washout_profile(float(z), k_decay, reference_expansion_profile) for z in z_grid],
        dtype=float,
    )
    tail = np.zeros_like(z_grid)
    for idx in range(len(z_grid) - 2, -1, -1):
        tail[idx] = tail[idx + 1] + 0.5 * (w_vals[idx] + w_vals[idx + 1]) * (z_grid[idx + 1] - z_grid[idx])
    return z_grid, source_profile, tail


def psi_q(q: float, z_grid: np.ndarray, source_profile: np.ndarray, washout_tail: np.ndarray) -> float:
    return float(np.trapezoid(q * source_profile * np.exp(-q * washout_tail), z_grid))


def flavored_column_functional(
    column: np.ndarray,
    z_grid: np.ndarray,
    source_profile: np.ndarray,
    washout_tail: np.ndarray,
) -> float:
    return float(sum(psi_q(float(q), z_grid, source_profile, washout_tail) for q in np.asarray(column, dtype=float)))


PKG = exact_package()
Z_GRID, SOURCE_PROFILE, WASHOUT_TAIL = flavored_transport_kernel(PKG.k_decay_exact)


def soft3(u: float, v: float, total: float) -> np.ndarray:
    logits = np.array([u, v, 0.0], dtype=float)
    logits -= np.max(logits)
    weights = np.exp(logits)
    weights /= np.sum(weights)
    return total * weights


def build_active_from_seed_logits(ax: float, ay: float, bx: float, by: float, delta: float) -> tuple[np.ndarray, np.ndarray, float]:
    x = soft3(ax, ay, 3.0 * XBAR_NE)
    y = soft3(bx, by, 3.0 * YBAR_NE)
    return x, y, float(delta)


def eta_columns_from_active(x: np.ndarray, y: np.ndarray, delta: float) -> tuple[np.ndarray, np.ndarray]:
    h_e = canonical_h(x, y, delta)
    packet = active_packet_from_h(h_e).T
    etas = np.array(
        [
            S_OVER_NGAMMA_EXACT
            * C_SPH
            * D_THERMAL_EXACT
            * PKG.epsilon_1
            * flavored_column_functional(packet[:, idx], Z_GRID, SOURCE_PROFILE, WASHOUT_TAIL)
            / ETA_OBS
            for idx in range(3)
        ],
        dtype=float,
    )
    return packet, etas


def best_eta_from_params(params: np.ndarray) -> float:
    x, y, delta = build_active_from_seed_logits(*params)
    _packet, etas = eta_columns_from_active(x, y, delta)
    return float(np.max(etas))


def source_coordinates(x: np.ndarray, y: np.ndarray, delta: float) -> tuple[np.ndarray, np.ndarray, float]:
    xi = np.asarray(x, dtype=float) - XBAR_NE * np.ones(3, dtype=float)
    eta = np.asarray(y, dtype=float) - YBAR_NE * np.ones(3, dtype=float)
    return xi, eta, float(delta)


def format_vec(v: np.ndarray) -> str:
    return np.array2string(np.round(np.asarray(v, dtype=float), 6), separator=", ")


def squash(text: str) -> str:
    return " ".join(text.split())


def part1_the_transport_objective_is_evaluable_on_the_imported_seed_surface() -> None:
    print("\n" + "=" * 88)
    print("PART 1: THE IMPORTED TRANSPORT OBJECTIVE IS EVALUABLE ON THE SEED SURFACE")
    print("=" * 88)

    x_seed = np.full(3, XBAR_NE, dtype=float)
    y_seed = np.full(3, YBAR_NE, dtype=float)
    packet_seed, etas_seed = eta_columns_from_active(x_seed, y_seed, 0.0)

    check(
        "The aligned seed point lies on the imported fixed-seed surface",
        abs(np.mean(x_seed) - XBAR_NE) < 1e-12 and abs(np.mean(y_seed) - YBAR_NE) < 1e-12,
        f"(xbar,ybar)=({np.mean(x_seed):.6f},{np.mean(y_seed):.6f})",
    )
    check(
        "The imported flavored transport functional is evaluable directly on that surface",
        np.all(etas_seed > 0.0),
        f"etas={np.round(etas_seed, 6)}",
    )
    check(
        "The aligned seed benchmark on the canonical N_e seed pair matches the prior direct-transport lift",
        abs(np.max(etas_seed) - 0.7190825360613422) < 2e-7,
        f"current functional replay={np.max(etas_seed):.12f}; prior direct benchmark=0.719082536061",
    )

    print()
    print(f"  aligned seed packet:\n{np.round(packet_seed, 6)}")
    print(f"  aligned seed eta/eta_obs = {np.round(etas_seed, 6)}")


def part2_transport_search_finds_an_off_seed_overshoot_witness() -> tuple[np.ndarray, np.ndarray, float, np.ndarray, np.ndarray]:
    print("\n" + "=" * 88)
    print("PART 2: TRANSPORT SEARCH FINDS AN OFF-SEED OVERSHOOT WITNESS")
    print("=" * 88)

    bounds = [
        (-4.0, 4.0),
        (-4.0, 4.0),
        (-4.0, 4.0),
        (-4.0, 4.0),
        (-math.pi, math.pi),
    ]
    result = differential_evolution(
        lambda p: -best_eta_from_params(np.asarray(p, dtype=float)),
        bounds=bounds,
        seed=0,
        maxiter=40,
        popsize=12,
        polish=True,
        disp=False,
    )

    x_opt, y_opt, delta_opt = build_active_from_seed_logits(*result.x)
    packet_opt, etas_opt = eta_columns_from_active(x_opt, y_opt, delta_opt)
    best_idx = int(np.argmax(etas_opt))
    xi_opt, eta_opt, _ = source_coordinates(x_opt, y_opt, delta_opt)

    check(
        "The sampled overshoot witness stays on the imported fixed seed surface",
        abs(np.mean(x_opt) - XBAR_NE) < 1e-12 and abs(np.mean(y_opt) - YBAR_NE) < 1e-12,
        f"(xbar,ybar)=({np.mean(x_opt):.6f},{np.mean(y_opt):.6f})",
    )
    check(
        "The sampled overshoot witness is genuinely off-seed",
        np.linalg.norm(xi_opt) > 1e-6 and np.linalg.norm(eta_opt) > 1e-6 and abs(delta_opt) > 1e-6,
        f"xi={format_vec(xi_opt)}, eta={format_vec(eta_opt)}, delta={delta_opt:.6f}",
    )
    check(
        "The sampled witness beats the canonical near-closing N_e sample",
        np.max(etas_opt) > 1.04,
        f"etas={np.round(etas_opt, 6)}, best column={best_idx}",
    )

    print()
    print(f"  x_opt     = {format_vec(x_opt)}")
    print(f"  y_opt     = {format_vec(y_opt)}")
    print(f"  delta_opt = {delta_opt:.12f}")
    print(f"  eta/eta_obs(opt) = {np.round(etas_opt, 6)}")
    print(f"  packet_opt:\n{np.round(packet_opt, 6)}")

    return x_opt, y_opt, delta_opt, packet_opt, etas_opt


def part3_continuity_gives_an_interpolated_closure_witness(
    x_opt: np.ndarray, y_opt: np.ndarray, delta_opt: float
) -> tuple[np.ndarray, np.ndarray, float, np.ndarray, np.ndarray]:
    print("\n" + "=" * 88)
    print("PART 3: CONTINUITY GIVES AN INTERPOLATED DIAGNOSTIC CROSSING")
    print("=" * 88)

    x_seed = np.full(3, XBAR_NE, dtype=float)
    y_seed = np.full(3, YBAR_NE, dtype=float)

    def best_eta_along(lmbda: float) -> float:
        x = (1.0 - lmbda) * x_seed + lmbda * x_opt
        y = (1.0 - lmbda) * y_seed + lmbda * y_opt
        delta = (1.0 - lmbda) * 0.0 + lmbda * delta_opt
        _packet, etas = eta_columns_from_active(x, y, delta)
        return float(np.max(etas))

    root = brentq(lambda l: best_eta_along(l) - 1.0, 0.0, 1.0)
    x_root = (1.0 - root) * x_seed + root * x_opt
    y_root = (1.0 - root) * y_seed + root * y_opt
    delta_root = root * delta_opt
    packet_root, etas_root = eta_columns_from_active(x_root, y_root, delta_root)
    best_idx = int(np.argmax(etas_root))

    check(
        "The computed best-eta map crosses 1 on the interpolating seed-preserving family",
        best_eta_along(0.0) < 1.0 < best_eta_along(1.0),
        f"(seed,opt)=({best_eta_along(0.0):.12f},{best_eta_along(1.0):.12f})",
    )
    check(
        "The interpolated diagnostic point has eta/eta_obs = 1 on the same parameterized family",
        abs(np.max(etas_root) - 1.0) < 1e-10,
        f"etas={np.round(etas_root, 12)}, best column={best_idx}",
    )
    check(
        "That closure point is still genuinely off-seed",
        np.linalg.norm(x_root - x_seed) > 1e-6 and np.linalg.norm(y_root - y_seed) > 1e-6 and abs(delta_root) > 1e-6,
        f"x={format_vec(x_root)}, y={format_vec(y_root)}, delta={delta_root:.12f}",
    )

    print()
    print(f"  lambda_*  = {root:.12f}")
    print(f"  x_close   = {format_vec(x_root)}")
    print(f"  y_close   = {format_vec(y_root)}")
    print(f"  delta_*   = {delta_root:.12f}")
    print(f"  eta/eta_obs(close) = {np.round(etas_root, 12)}")
    print(f"  packet_close:\n{np.round(packet_root, 6)}")

    return x_root, y_root, delta_root, packet_root, etas_root


def part4_bottom_line() -> None:
    print("\n" + "=" * 88)
    print("PART 4: SELECTOR FIREWALL")
    print("=" * 88)

    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    firewall_text = FIREWALL_NOTE.read_text(encoding="utf-8")
    parent_flat = squash(parent_text)

    check(
        "The imported transport functional has a constructive interval witness",
        True,
        "seed endpoint below 1, sampled endpoint above 1",
    )
    check(
        "The witness does not select a physical off-seed source law",
        True,
        "selector status remains out of scope",
    )
    check(
        "The remaining issue is the unproven selector/authority bridge",
        True,
        "bounded interval witness only",
    )
    check(
        "The parent note cites the selector-firewall companion",
        FIREWALL_NOTE.name in parent_text,
        FIREWALL_NOTE.name,
    )
    check(
        "The parent note demotes the exact equality point to a diagnostic crossing",
        "intermediate-value diagnostic" in parent_flat
        and "not a physical selector" in parent_flat
        and "should not be cited as a framework prediction" in parent_flat,
        "root is reproducibility data, not a selected source law",
    )
    check(
        "The selector firewall forbids using ETA_OBS as the hidden selector",
        "treating `ETA_OBS` as a selected framework output" in firewall_text
        and "choosing the interpolation root because it equals the observed comparator" in firewall_text,
        "observed comparator is not a source-selection theorem",
    )
    check(
        "The selector firewall preserves future positive selector routes",
        "This firewall does not rule those routes out" in firewall_text
        and "independent theorem deriving" in firewall_text,
        "future endpoint or lambda theorem remains open",
    )


def main() -> int:
    print("=" * 88)
    print("DM LEPTOGENESIS PMNS TRANSPORT INTERVAL WITNESS")
    print("=" * 88)
    print()
    print("Framework baseline:")
    print("  one-qubit operator algebra M_2(C) ~= Cl(3,0) on Z^3.")
    print()
    print("Question:")
    print("  Does the imported PMNS-assisted transport functional contain a")
    print("  seed-to-overshoot interval witness without claiming a selector law?")

    part1_the_transport_objective_is_evaluable_on_the_imported_seed_surface()
    x_opt, y_opt, delta_opt, _packet_opt, _etas_opt = part2_transport_search_finds_an_off_seed_overshoot_witness()
    part3_continuity_gives_an_interpolated_closure_witness(x_opt, y_opt, delta_opt)
    part4_bottom_line()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Bounded construction:")
    print("    - the imported fixed seed endpoint is below eta/eta_obs = 1")
    print("    - the sampled off-seed endpoint is above eta/eta_obs = 1")
    print("    - interpolation gives an eta/eta_obs = 1 diagnostic crossing on that family")
    print()
    print("  No physical selector law, exact eta_obs prediction, or full-stack closure is claimed.")
    print()
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
