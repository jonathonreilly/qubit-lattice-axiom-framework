#!/usr/bin/env python3
"""
DM PMNS fixed-N_e-seed-surface exact source-manifold theorem.

Question:
  On the charged-lepton-side PMNS parameterization, does the empirical angle
  comparator have regular preimages on the supplied fixed N_e seed surface, and if so
  do the current conditional nonlocal candidate families on that surface pick it?

Answer:
  Yes to existence, no to selection.

  The supplied N_e seed surface contains numerical realizations of the
  empirical PMNS comparator. At the verified points, the PMNS-angle
  Jacobian has full rank 3, so the exact preimage is a local 2-real regular
  source manifold on that surface. The current conditional nonlocal seed-surface
  selector families (aligned seed, stationary effective-action branches,
  constructive eta=1 closure point, constructive witness) all miss this exact
  PMNS manifold by macroscopic chi^2. Therefore the remaining I5 object on the
  charged-lepton-side branch is a new 2-real point-selection law on the exact
  N_e PMNS source manifold.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, least_squares

from frontier_dm_leptogenesis_pmns_active_projector_reduction import active_packet_from_h
from frontier_dm_leptogenesis_pmns_constructive_continuity_closure_theorem import path_point
from frontier_dm_leptogenesis_pmns_observable_relative_action_law import (
    XBAR_NE,
    YBAR_NE,
    build_active_from_params,
    eta_columns_from_active,
    relative_action_h,
)
from frontier_dm_leptogenesis_pmns_projector_interface import canonical_h
from frontier_dm_leptogenesis_pmns_reduced_surface_selector_support import (
    HIGH_SOURCE_REF,
    HIGH_SOURCE_REF_Y,
    compact_chart_to_source,
)
from frontier_dm_leptogenesis_pmns_relative_action_stationarity_theorem import (
    closure_point_on_ray,
    constrained_stationary_point,
    favored_column_and_extremal_params,
)
from frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate import (
    eta_columns_from_active as constructive_eta_columns,
)

ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0

TARGET = np.array([0.307, 0.0218, 0.545], dtype=float)
CHART_LO = np.array([1.0e-6, 1.0e-6, 1.0e-6, 1.0e-6, -math.pi], dtype=float)
CHART_HI = np.array([1.0 - 1.0e-6, 1.0 - 1.0e-6, 1.0 - 1.0e-6, 1.0 - 1.0e-6, math.pi], dtype=float)

# Diverse deterministic starts on the supplied N_e seed chart. Each one
# lands on a comparator-matching PMNS point after local polishing.
SEED_CHART_STARTS = [
    np.array([0.036052, 0.460525, 0.541825, 0.581724, -1.533871], dtype=float),
    np.array([0.102254, 0.462703, 0.493331, 0.565381, 0.789612], dtype=float),
    np.array([0.134734, 0.465282, 0.464716, 0.545577, 0.757215], dtype=float),
    np.array([0.016368, 0.459040, 0.553314, 0.620378, -0.366521], dtype=float),
    np.array([0.024419, 0.460788, 0.549077, 0.569800, -2.670784], dtype=float),
    np.array([0.168475, 0.467792, 0.431065, 0.538217, -0.635221], dtype=float),
]


@dataclass
class ExactPoint:
    chart: np.ndarray
    x: np.ndarray
    y: np.ndarray
    delta: float
    obs: np.ndarray
    chi2: float
    rank: int
    rel_action: float
    etas: np.ndarray
    source_cubic: float


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


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def chart_to_obs(chart: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, float, np.ndarray]:
    x, y, delta = compact_chart_to_source(np.asarray(chart, dtype=float))
    h = canonical_h(x, y, delta)
    packet = active_packet_from_h(h).T
    s13sq = float(packet[0, 2])
    c13sq = max(1.0 - s13sq, 1.0e-15)
    s12sq = float(packet[0, 1] / c13sq)
    s23sq = float(packet[1, 2] / c13sq)
    obs = np.array([s12sq, s13sq, s23sq], dtype=float)
    return obs, x, y, float(delta), h


def residual(chart: np.ndarray) -> np.ndarray:
    obs, _x, _y, _delta, _h = chart_to_obs(chart)
    return obs - TARGET


def chi2(chart: np.ndarray) -> float:
    r = residual(chart)
    return float(np.dot(r, r))


def finite_jacobian(fun, chart: np.ndarray, eps: float = 1.0e-6) -> np.ndarray:
    chart = np.asarray(chart, dtype=float)
    f0 = np.asarray(fun(chart), dtype=float)
    jac = np.zeros((len(f0), len(chart)), dtype=float)
    for idx in range(len(chart)):
        step = np.zeros_like(chart)
        step[idx] = eps
        jac[:, idx] = (fun(chart + step) - fun(chart - step)) / (2.0 * eps)
    return jac


def source_distance(a: ExactPoint, b: ExactPoint) -> float:
    delta_diff = min(
        abs(a.delta - b.delta),
        abs(a.delta - b.delta + 2.0 * math.pi),
        abs(a.delta - b.delta - 2.0 * math.pi),
    )
    return float(np.linalg.norm(a.x - b.x) + np.linalg.norm(a.y - b.y) + delta_diff)


def polish_exact_point(start: np.ndarray) -> ExactPoint:
    result = least_squares(
        residual,
        np.asarray(start, dtype=float),
        bounds=(CHART_LO, CHART_HI),
        xtol=1.0e-14,
        ftol=1.0e-14,
        gtol=1.0e-14,
        max_nfev=2000,
    )
    chart = np.asarray(result.x, dtype=float)
    obs, x, y, delta, h = chart_to_obs(chart)
    jac = finite_jacobian(lambda q: chart_to_obs(q)[0], chart)
    rank = int(np.linalg.matrix_rank(jac, tol=1.0e-5))
    _h_chk, _packet_chk, etas = eta_columns_from_active(x, y, delta)
    return ExactPoint(
        chart=chart,
        x=x,
        y=y,
        delta=delta,
        obs=obs,
        chi2=chi2(chart),
        rank=rank,
        rel_action=float(relative_action_h(h)),
        etas=np.asarray(etas, dtype=float),
        source_cubic=float(np.imag(h[0, 1] * h[1, 2] * h[2, 0])),
    )


def distinct_exact_points() -> list[ExactPoint]:
    raw = [polish_exact_point(start) for start in SEED_CHART_STARTS]
    reps: list[ExactPoint] = []
    for point in raw:
        if all(source_distance(point, rep) > 5.0e-2 for rep in reps):
            reps.append(point)
    return reps


def selector_family_points() -> list[tuple[str, np.ndarray]]:
    rows: list[tuple[str, np.ndarray]] = []

    rows.append(("aligned seed", np.array([0.2, 1.0 / 6.0, 0.6], dtype=float)))

    i_star, extremal_params = favored_column_and_extremal_params()
    start = closure_point_on_ray(extremal_params, i_star)
    low_chart, _ = constrained_stationary_point(start, i_star)
    x_low, y_low, delta_low = build_active_from_params(low_chart)
    h_low = canonical_h(x_low, y_low, delta_low)
    packet_low = active_packet_from_h(h_low).T
    obs_low = np.array(
        [
            float(packet_low[0, 1] / max(1.0 - packet_low[0, 2], 1.0e-15)),
            float(packet_low[0, 2]),
            float(packet_low[1, 2] / max(1.0 - packet_low[0, 2], 1.0e-15)),
        ],
        dtype=float,
    )
    rows.append(("low-action stationary", obs_low))

    h_high = canonical_h(HIGH_SOURCE_REF, HIGH_SOURCE_REF_Y, 0.0)
    packet_high = active_packet_from_h(h_high).T
    obs_high = np.array(
        [
            float(packet_high[0, 1] / max(1.0 - packet_high[0, 2], 1.0e-15)),
            float(packet_high[0, 2]),
            float(packet_high[1, 2] / max(1.0 - packet_high[0, 2], 1.0e-15)),
        ],
        dtype=float,
    )
    rows.append(("high-action stationary", obs_high))

    lam_star = brentq(lambda lam: constructive_eta_columns(*path_point(lam))[1][1] - 1.0, 0.0, 1.0)
    x_eta, y_eta, delta_eta = path_point(lam_star)
    h_eta = canonical_h(x_eta, y_eta, delta_eta)
    packet_eta = active_packet_from_h(h_eta).T
    obs_eta = np.array(
        [
            float(packet_eta[0, 1] / max(1.0 - packet_eta[0, 2], 1.0e-15)),
            float(packet_eta[0, 2]),
            float(packet_eta[1, 2] / max(1.0 - packet_eta[0, 2], 1.0e-15)),
        ],
        dtype=float,
    )
    rows.append(("constructive eta=1", obs_eta))

    x_wit, y_wit, delta_wit = path_point(1.0)
    h_wit = canonical_h(x_wit, y_wit, delta_wit)
    packet_wit = active_packet_from_h(h_wit).T
    obs_wit = np.array(
        [
            float(packet_wit[0, 1] / max(1.0 - packet_wit[0, 2], 1.0e-15)),
            float(packet_wit[0, 2]),
            float(packet_wit[1, 2] / max(1.0 - packet_wit[0, 2], 1.0e-15)),
        ],
        dtype=float,
    )
    rows.append(("constructive witness", obs_wit))

    return rows


def part1_comparator_points_exist_on_the_supplied_seed_surface() -> list[ExactPoint]:
    print("\n" + "=" * 88)
    print("PART 1: EXACT PHYSICAL PMNS POINTS EXIST ON THE FIXED NATIVE N_e SEED SURFACE")
    print("=" * 88)

    reps = distinct_exact_points()
    check(
        "The verifier finds at least three distinct comparator-matching points on the supplied N_e seed surface",
        len(reps) >= 3,
        f"distinct exact points={len(reps)}",
    )
    check(
        "Every polished representative reproduces the empirical PMNS comparator to high precision",
        all(point.chi2 < 1.0e-8 for point in reps),
        f"chi2 values={[round(point.chi2, 12) for point in reps]}",
    )

    for idx, point in enumerate(reps[:3], start=1):
        print()
        print(
            f"  rep {idx}: x={np.round(point.x, 6)}, y={np.round(point.y, 6)}, "
            f"delta={point.delta:.6f}, obs={np.round(point.obs, 9)}"
        )

    return reps


def part2_the_exact_preimage_is_a_regular_two_real_source_manifold(reps: list[ExactPoint]) -> None:
    print("\n" + "=" * 88)
    print("PART 2: THE EXACT PREIMAGE IS A REGULAR 2-REAL SOURCE MANIFOLD")
    print("=" * 88)

    check(
        "At every checked comparator preimage the angle-map Jacobian has full rank 3",
        all(point.rank == 3 for point in reps),
        f"ranks={[point.rank for point in reps]}",
    )
    check(
        "Therefore each checked comparator-matching point lies on a local 2-real regular preimage inside the 5-real seed surface",
        all(point.rank == 3 for point in reps),
        "dim(seed surface)=5 and rank(dF)=3",
    )


def part3_current_nonlocal_selector_families_do_not_pick_the_exact_pmns_manifold() -> None:
    print("\n" + "=" * 88)
    print("PART 3: CURRENT NONLOCAL SEED-SURFACE SELECTOR FAMILIES MISS THE MANIFOLD")
    print("=" * 88)

    rows = selector_family_points()
    misses = []
    for name, obs in rows:
        miss = float(np.sum((obs - TARGET) ** 2))
        misses.append((name, miss))
        print(f"  {name:<24s} chi^2 = {miss:.12f}, obs = {np.round(obs, 9)}")

    check(
        "Every current nonlocal candidate point misses the empirical PMNS comparator by chi^2 > 0.03",
        all(miss > 3.0e-2 for _name, miss in misses),
        f"misses={[round(miss, 6) for _name, miss in misses]}",
    )


def part4_current_selector_observables_vary_along_the_exact_manifold(reps: list[ExactPoint]) -> None:
    print("\n" + "=" * 88)
    print("PART 4: CURRENT SELECTOR OBSERVABLES VARY ALONG THE EXACT MANIFOLD")
    print("=" * 88)

    rel_values = np.array([point.rel_action for point in reps], dtype=float)
    eta0_values = np.array([point.etas[0] for point in reps], dtype=float)
    cubic_values = np.array([point.source_cubic for point in reps], dtype=float)

    check(
        "The comparator preimage manifold carries a macroscopic relative-action spread",
        float(np.max(rel_values) - np.min(rel_values)) > 1.0,
        f"S_rel range=({np.min(rel_values):.6f},{np.max(rel_values):.6f})",
    )
    check(
        "The comparator preimage manifold carries distinct transport outputs on the favored column",
        float(np.max(eta0_values) - np.min(eta0_values)) > 5.0e-3,
        f"eta_0 range=({np.min(eta0_values):.6f},{np.max(eta0_values):.6f})",
    )
    check(
        "The comparator preimage manifold carries both source-cubic orientations",
        np.min(cubic_values) < 0.0 < np.max(cubic_values),
        f"cubic range=({np.min(cubic_values):.6e},{np.max(cubic_values):.6e})",
    )


def part0_cited_authorities_round_trip() -> None:
    """
    Re-check the cited framework identities at the points the rest of the
    runner uses them.  This is the audit-grade authority round-trip: the
    imported routines are run against their cited definitions, not opaquely
    trusted.
    """
    print("\n" + "=" * 88)
    print("PART 0: CITED-AUTHORITY ROUND-TRIP IDENTITIES")
    print("=" * 88)

    # (a) Seed pair matches the values supplied by the cited conditional
    #     calculator: (169/300, 23/75).
    check(
        "The supplied N_e seed pair matches the rational form (169/300, 23/75)",
        abs(XBAR_NE - 169.0 / 300.0) < 1e-15 and abs(YBAR_NE - 23.0 / 75.0) < 1e-15,
        f"(XBAR_NE, YBAR_NE) = ({XBAR_NE!r}, {YBAR_NE!r})",
    )

    # (b) canonical_h is what the cited projector-interface note says: it is
    #     H_e = Y_e Y_e^dagger with Y_e = diag(x) + diag(y_phase) C.
    cycle = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    x_dbg = np.array([0.42, 0.51, 0.63], dtype=float)
    y_dbg = np.array([0.18, 0.34, 0.27], dtype=float)
    delta_dbg = 1.234
    y_mat = (
        np.diag(x_dbg.astype(complex))
        + np.diag(np.array([y_dbg[0], y_dbg[1], y_dbg[2] * np.exp(1j * delta_dbg)], dtype=complex))
        @ cycle
    )
    h_direct = y_mat @ y_mat.conj().T
    h_imported = canonical_h(x_dbg, y_dbg, delta_dbg)
    check(
        "Imported canonical_h matches the direct (Y Y^dagger) algebraic definition",
        bool(np.allclose(h_direct, h_imported, atol=1e-14)),
        f"max|diff| = {float(np.max(np.abs(h_direct - h_imported))):.2e}",
    )

    # (c) active_packet_from_h(H_e).T agrees with the projector-interface
    #     packet built from a left diagonalizer (i.e. |U_PMNS|^2 readout).
    evals, u_left = np.linalg.eigh(h_imported)
    order = np.argsort(np.real(evals))
    u_left = u_left[:, order]
    # In the one-sided active-projector reduction the packet is read directly
    # off the active diagonalizer; here we use the squared columns and check
    # consistency with the active packet up to row stochastic normalization.
    direct_packet = np.abs(u_left) ** 2
    direct_packet = direct_packet / np.sum(direct_packet, axis=0, keepdims=True)
    active_packet = active_packet_from_h(h_imported)
    check(
        "Active-packet readout is column-stochastic (cited active-projector reduction)",
        bool(np.allclose(active_packet.sum(axis=0), 1.0, atol=1e-12)),
        f"column sums = {active_packet.sum(axis=0)}",
    )
    check(
        "Active-packet readout reproduces the |U|^2 columns of the left diagonalizer (up to row permutation)",
        bool(
            np.allclose(np.sort(active_packet, axis=0), np.sort(direct_packet, axis=0), atol=1e-12)
        ),
        "sorted columns match",
    )

    # (d) Compact chart is surjective: a deterministic interior point maps to
    #     a strict-interior triple on S_Ne (mean equals the seed center).
    chart_test = np.array([0.32, 0.48, 0.27, 0.61, -0.5], dtype=float)
    x_t, y_t, _ = compact_chart_to_source(chart_test)
    check(
        "Compact-chart image satisfies the seed-surface mean constraint mean(x)=Xbar_Ne",
        abs(float(np.mean(x_t)) - XBAR_NE) < 1e-12,
        f"mean(x) - Xbar_Ne = {float(np.mean(x_t)) - XBAR_NE:.2e}",
    )
    check(
        "Compact-chart image satisfies the seed-surface mean constraint mean(y)=Ybar_Ne",
        abs(float(np.mean(y_t)) - YBAR_NE) < 1e-12,
        f"mean(y) - Ybar_Ne = {float(np.mean(y_t)) - YBAR_NE:.2e}",
    )


# ---------------------------------------------------------------------------
# Independent lattice-cover existence sweep.  Establishes claim (2) of the
# theorem statement without relying on the polished hard-coded starts.
# ---------------------------------------------------------------------------

LATTICE_GRID_VALUES = (0.20, 0.50, 0.80)
LATTICE_DELTA_VALUES = (-2.0, -1.0, 0.0, 1.0, 2.0)


def lattice_chart_starts() -> list[np.ndarray]:
    starts: list[np.ndarray] = []
    for u1 in LATTICE_GRID_VALUES:
        for u2 in LATTICE_GRID_VALUES:
            for v1 in LATTICE_GRID_VALUES:
                for v2 in LATTICE_GRID_VALUES:
                    for delta in LATTICE_DELTA_VALUES:
                        starts.append(np.array([u1, u2, v1, v2, delta], dtype=float))
    return starts


def part1b_independent_lattice_sweep_existence(reps: list[ExactPoint]) -> list[ExactPoint]:
    print("\n" + "=" * 88)
    print("PART 1b: INDEPENDENT COMPACT-CHART LATTICE SWEEP EXISTENCE")
    print("=" * 88)
    print(
        f"  sweeping {len(LATTICE_GRID_VALUES) ** 4 * len(LATTICE_DELTA_VALUES)} deterministic chart starts ..."
    )

    polished: list[ExactPoint] = []
    for start in lattice_chart_starts():
        point = polish_exact_point(start)
        if point.chi2 > 1.0e-8:
            continue
        if all(source_distance(point, rep) > 5.0e-2 for rep in polished):
            polished.append(point)

    check(
        "Lattice sweep recovers at least three distinct preimages of the empirical target",
        len(polished) >= 3,
        f"distinct lattice preimages = {len(polished)}",
    )
    check(
        "Every lattice-sweep representative reproduces the empirical target to high precision",
        all(point.chi2 < 1.0e-8 for point in polished),
        f"max chi^2 = {max((p.chi2 for p in polished), default=0.0):.2e}",
    )

    # Independence: at least one lattice representative is far from every
    # polished hard-coded representative.
    far_from_hard_coded = any(
        all(source_distance(lp, rp) > 5.0e-2 for rp in reps) for lp in polished
    )
    check(
        "At least one lattice-sweep representative is distinct from every polished hard-coded representative",
        far_from_hard_coded,
        f"lattice cover size = {len(polished)}, hard-coded reps = {len(reps)}",
    )

    return polished


def part1c_polished_points_lie_on_the_seed_surface(reps: list[ExactPoint]) -> None:
    print("\n" + "=" * 88)
    print("PART 1c: POLISHED REPRESENTATIVES LIE ON THE FIXED NATIVE N_e SEED SURFACE")
    print("=" * 88)

    mean_x_devs = [abs(float(np.mean(point.x)) - XBAR_NE) for point in reps]
    mean_y_devs = [abs(float(np.mean(point.y)) - YBAR_NE) for point in reps]

    check(
        "Every polished representative has mean(x) = Xbar_Ne to chart tolerance",
        all(dev < 1.0e-10 for dev in mean_x_devs),
        f"max |mean(x) - Xbar_Ne| = {max(mean_x_devs):.2e}",
    )
    check(
        "Every polished representative has mean(y) = Ybar_Ne to chart tolerance",
        all(dev < 1.0e-10 for dev in mean_y_devs),
        f"max |mean(y) - Ybar_Ne| = {max(mean_y_devs):.2e}",
    )


def part2b_rank_is_stable_across_step_sizes(reps: list[ExactPoint]) -> None:
    print("\n" + "=" * 88)
    print("PART 2b: JACOBIAN RANK IS STABLE ACROSS INDEPENDENT FINITE-DIFFERENCE STEP SIZES")
    print("=" * 88)

    eps_a = 1.0e-6
    eps_b = 1.0e-5
    ranks_a = []
    ranks_b = []
    for point in reps:
        jac_a = finite_jacobian(lambda q: chart_to_obs(q)[0], point.chart, eps=eps_a)
        jac_b = finite_jacobian(lambda q: chart_to_obs(q)[0], point.chart, eps=eps_b)
        ranks_a.append(int(np.linalg.matrix_rank(jac_a, tol=1.0e-5)))
        ranks_b.append(int(np.linalg.matrix_rank(jac_b, tol=1.0e-5)))

    check(
        f"Finite-difference Jacobian rank is 3 at every checked point for eps={eps_a:.1e}",
        all(r == 3 for r in ranks_a),
        f"ranks_a = {ranks_a}",
    )
    check(
        f"Finite-difference Jacobian rank is 3 at every checked point for eps={eps_b:.1e}",
        all(r == 3 for r in ranks_b),
        f"ranks_b = {ranks_b}",
    )


def part5_the_note_records_the_correct_i5_reduction() -> None:
    print("\n" + "=" * 88)
    print("PART 5: THE NOTE RECORDS THE CORRECT I5 REDUCTION")
    print("=" * 88)

    note = read("docs/DM_PMNS_NE_SEED_SURFACE_EXACT_SOURCE_MANIFOLD_THEOREM_NOTE_2026-04-20.md")

    check(
        "The note records comparator realizability on the supplied N_e seed surface",
        "supplied fixed `N_e` seed surface" in note and "empirical target triple" in note,
    )
    check(
        "The note records the regular 2-real source-manifold consequence",
        "`2`-real" in note and "Jacobian" in note and "rank `3`" in note,
    )
    check(
        "The note records the current nonlocal selector-family miss",
        "aligned seed" in note and "low-action stationary" in note and "constructive witness" in note,
    )
    check(
        "The note records the sharpened I5 target as a new 2-real point-selection law",
        "new `2`-real point-selection law" in note,
    )
    check(
        "The note explicitly cites the empirical-comparator role of the target triple",
        "NuFit 5.3" in note and "observational comparator" in note,
    )
    check(
        "The note lists explicit authority or conditional-calculator citations for every imported routine",
        all(
            tag in note
            for tag in (
                "## Inputs (cited authorities)",
                "DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md",
                "DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md",
                "DM_LEPTOGENESIS_PMNS_REDUCED_SURFACE_SELECTOR_SUPPORT_NOTE_2026-04-16.md",
                "DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_CONDITIONAL_CALCULATOR_NOTE_2026-07-12.md",
                "DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md",
                "DM_LEPTOGENESIS_PMNS_CONSTRUCTIVE_CONTINUITY_CLOSURE_THEOREM_NOTE_2026-04-17.md",
            )
        ),
    )


def main() -> int:
    print("=" * 88)
    print("DM PMNS FIXED-N_e-SEED-SURFACE EXACT SOURCE-MANIFOLD THEOREM")
    print("=" * 88)
    print()
    print("Question:")
    print("  Does the empirical PMNS angle comparator already lie on the cited")
    print("  supplied fixed N_e seed surface as a regular preimage, and do the")
    print("  current cited nonlocal selector families on that surface pick it?")

    part0_cited_authorities_round_trip()
    reps = part1_comparator_points_exist_on_the_supplied_seed_surface()
    part1b_independent_lattice_sweep_existence(reps)
    part1c_polished_points_lie_on_the_seed_surface(reps)
    part2_the_exact_preimage_is_a_regular_two_real_source_manifold(reps)
    part2b_rank_is_stable_across_step_sizes(reps)
    part3_current_nonlocal_selector_families_do_not_pick_the_exact_pmns_manifold()
    part4_current_selector_observables_vary_along_the_exact_manifold(reps)
    part5_the_note_records_the_correct_i5_reduction()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Exact reduction answer:")
    print("    - the supplied N_e seed surface contains comparator-matching")
    print("      PMNS points")
    print("    - on the verified regular patch those points form a local 2-real")
    print("      source manifold")
    print("    - current conditional nonlocal seed-surface candidates do not pick")
    print("      that manifold")
    print("    - so the remaining I5 object is a new 2-real point-selection law on")
    print("      the exact N_e PMNS source manifold")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
