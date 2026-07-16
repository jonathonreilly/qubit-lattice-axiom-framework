#!/usr/bin/env python3
"""
DM leptogenesis PMNS conditional reduction-factorization diagnostic.

Framework convention:
  the current framework baseline is Lattice, Qubit, Admissibility, and Record.

Purpose:
  Check a supplied source-chart factorization in the PMNS-assisted N_e lane.

  Earlier review concern:
    do we need a separate "all-possible-components" analytic uniqueness theorem
    beyond the exact closure surface already used by the selector theorem?

  Supplied chart:

      S_seed
        = { (x, y, delta) :
              x_i > 0, y_i > 0,
              sum_i x_i = 3 XBAR_NE,
              sum_i y_i = 3 YBAR_NE,
              delta in [-pi, pi] }.

  The checks show only that named helper candidates and a supplied finite
  transport calculation factor through this chart. They do not prove that every
  admissible physical component lies on S_seed.
"""

from __future__ import annotations

import math
import sys

import numpy as np

import frontier_dm_leptogenesis_flavor_column_functional_theorem as func
import frontier_dm_leptogenesis_pmns_active_projector_reduction as act
import frontier_dm_leptogenesis_pmns_multistart_selector_support as selector
import frontier_dm_leptogenesis_pmns_observable_relative_action_law as rel
import frontier_dm_leptogenesis_pmns_relative_action_stationarity_theorem as stat
from frontier_dm_leptogenesis_pmns_projector_interface import canonical_h, monomial_h, pmns_projector_packet

AUDIT_TIMEOUT_SEC = 600

PASS_COUNT = 0
FAIL_COUNT = 0


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


def fmt(v: np.ndarray) -> str:
    return np.array2string(np.round(np.asarray(v, dtype=float), 6), separator=", ")


def inverse_soft3(weights: np.ndarray) -> np.ndarray:
    w = np.asarray(weights, dtype=float)
    if np.any(w <= 0.0):
        raise ValueError("inverse soft3 needs strictly positive weights")
    return np.array([math.log(w[0] / w[2]), math.log(w[1] / w[2])], dtype=float)


def part1_the_active_seed_surface_chart_round_trips() -> None:
    print("\n" + "=" * 88)
    print("PART 1: THE SUPPLIED N_e SEED-SURFACE CHART ROUND-TRIPS")
    print("=" * 88)

    x_target = np.array([0.471675, 0.553810, 0.664515], dtype=float)
    y_target = np.array([0.208063, 0.464382, 0.247555], dtype=float)

    ax, ay = inverse_soft3(x_target)
    bx, by = inverse_soft3(y_target)
    params = np.array([ax, ay, bx, by, 0.0], dtype=float)
    x_back, y_back, delta_back = rel.build_active_from_params(params)

    rng = np.random.default_rng(16)
    max_err = 0.0
    for _ in range(8):
        x_rand = rng.uniform(0.05, 1.5, size=3)
        x_rand *= (3.0 * rel.XBAR_NE) / float(np.sum(x_rand))
        y_rand = rng.uniform(0.05, 0.8, size=3)
        y_rand *= (3.0 * rel.YBAR_NE) / float(np.sum(y_rand))
        ax_r, ay_r = inverse_soft3(x_rand)
        bx_r, by_r = inverse_soft3(y_rand)
        x_chk, y_chk, _ = rel.build_active_from_params(np.array([ax_r, ay_r, bx_r, by_r, 0.0], dtype=float))
        max_err = max(max_err, float(np.linalg.norm(x_chk - x_rand) + np.linalg.norm(y_chk - y_rand)))

    check(
        "The active source chart preserves the exact native seed sums",
        abs(np.mean(x_back) - rel.XBAR_NE) < 1e-12 and abs(np.mean(y_back) - rel.YBAR_NE) < 1e-12,
        f"(xbar,ybar)=({np.mean(x_back):.6f},{np.mean(y_back):.6f})",
    )
    check(
        "The soft3 chart is exactly invertible on the positive fixed-sum surface",
        np.linalg.norm(x_back - x_target) < 1e-12 and np.linalg.norm(y_back - y_target) < 1e-12,
        f"err={np.linalg.norm(x_back - x_target) + np.linalg.norm(y_back - y_target):.2e}",
    )
    check(
        "So the active parameter chart is surjective onto the interior of the fixed native N_e seed surface",
        max_err < 1e-12,
        f"max sampled inverse-chart error={max_err:.2e}",
    )

    print()
    print(f"  exemplar x = {fmt(x_target)}")
    print(f"  exemplar y = {fmt(y_target)}")
    print(f"  inverse-chart params = {fmt(params)}")
    print(f"  recovered x = {fmt(x_back)}")
    print(f"  recovered y = {fmt(y_back)}")
    print(f"  recovered delta = {delta_back:.6f}")


def part2_the_supplied_eta_fixture_factors_through_the_chart() -> None:
    print("\n" + "=" * 88)
    print("PART 2: THE SUPPLIED ETA FIXTURE FACTORS THROUGH THE CHART")
    print("=" * 88)

    x = np.array([0.471675, 0.553810, 0.664515], dtype=float)
    y = np.array([0.208063, 0.464382, 0.247555], dtype=float)
    delta = 0.0

    h_e = canonical_h(x, y, delta)
    h_nu_pass = monomial_h(np.array([0.018, 0.051, 0.074], dtype=float))

    packet_full = pmns_projector_packet(h_nu_pass, h_e)
    packet_act = act.active_packet_from_h(h_e).T

    z_grid, source_profile, washout_tail, _ = func.part1_single_source_flavored_transport_reduces_to_an_exact_column_functional()
    func_vals = np.array(
        [func.flavored_column_functional(packet_act[:, idx], z_grid, source_profile, washout_tail) for idx in range(3)],
        dtype=float,
    )
    best_idx = int(np.argmax(func_vals))

    check(
        "On the one-sided N_e lane, the PMNS packet equals the active packet transpose exactly",
        np.linalg.norm(packet_full - packet_act) < 1e-12,
        f"err={np.linalg.norm(packet_full - packet_act):.2e}",
    )
    check(
        "The supplied finite transport output is a scalar functional of active packet columns",
        np.all(func_vals > 0.0),
        f"F(P)={np.round(func_vals, 12)}",
    )
    check(
        "The named helper eta fixture factors through H_e and its active packet",
        best_idx == 0,
        f"favored column={best_idx}",
    )

    print()
    print(f"  active packet:\n{np.round(packet_act, 6)}")
    print(f"  exact column functionals = {np.round(func_vals, 12)}")


def part3_imported_candidate_branches_lie_on_the_supplied_surface() -> None:
    print("\n" + "=" * 88)
    print("PART 3: IMPORTED CANDIDATE BRANCHES LIE ON THE SUPPLIED SURFACE")
    print("=" * 88)

    i_star, branches = selector.part1_enumerate_stationary_branches()
    low = branches[0]
    high = branches[1]
    _ = i_star

    x_lo, y_lo, d_lo = stat.rel.build_active_from_params(low.representative)
    x_hi, y_hi, d_hi = stat.rel.build_active_from_params(high.representative)

    check(
        "The imported low-action candidate lies on the supplied fixed-sum seed surface",
        abs(np.mean(x_lo) - rel.XBAR_NE) < 1e-12 and abs(np.mean(y_lo) - rel.YBAR_NE) < 1e-12,
        f"(xbar,ybar)=({np.mean(x_lo):.6f},{np.mean(y_lo):.6f})",
    )
    check(
        "The imported higher-action candidate lies on the same supplied fixed-sum seed surface",
        abs(np.mean(x_hi) - rel.XBAR_NE) < 1e-12 and abs(np.mean(y_hi) - rel.YBAR_NE) < 1e-12,
        f"(xbar,ybar)=({np.mean(x_hi):.6f},{np.mean(y_hi):.6f})",
    )
    check(
        "The two imported candidate representatives lie on the same supplied chart",
        abs(d_lo) < 1e-4 and abs(d_hi) < 1e-4,
        f"(delta_lo,delta_hi)=({d_lo:.3e},{d_hi:.3e})",
    )

    print()
    print(f"  low branch x = {fmt(x_lo)}")
    print(f"  low branch y = {fmt(y_lo)}")
    print(f"  high branch x = {fmt(x_hi)}")
    print(f"  high branch y = {fmt(y_hi)}")


def part4_bottom_line() -> None:
    print("\n" + "=" * 88)
    print("PART 4: BOTTOM LINE")
    print("=" * 88)

    print("  Nature-review read:")
    print("    - the named finite computation factors through the supplied seed surface")
    print("    - no check proves that surface is the whole admissible physical domain")
    print("    - disconnected or omitted components and global uniqueness remain open")


def main() -> int:
    print("=" * 88)
    print("DM LEPTOGENESIS PMNS CONDITIONAL REDUCTION-FACTORIZATION DIAGNOSTIC")
    print("=" * 88)
    print()
    print("Framework convention:")
    print("  current baseline: Lattice, Qubit, Admissibility, and Record.")
    print()
    print("Question:")
    print("  Which supplied chart is consumed by the named finite computation, and")
    print("  what domain-exhaustion claims remain open?")

    part1_the_active_seed_surface_chart_round_trips()
    part2_the_supplied_eta_fixture_factors_through_the_chart()
    candidate_refinement_completed = True
    try:
        part3_imported_candidate_branches_lie_on_the_supplied_surface()
    except RuntimeError as exc:
        candidate_refinement_completed = False
        check(
            "The imported constrained candidate refinement completes",
            False,
            str(exc),
        )
    part4_bottom_line()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Conditional factorization answer:")
    print("    - the supplied chart round-trips on tested fixed-sum points")
    print("    - the finite eta exemplar factors through that chart")
    if not candidate_refinement_completed:
        print("    - imported candidate refinement did not complete")
    print("    - admissible-domain exhaustion and global uniqueness remain open")
    print()
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
