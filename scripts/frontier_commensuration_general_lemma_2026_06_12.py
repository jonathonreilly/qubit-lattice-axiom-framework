#!/usr/bin/env python3
"""Class-A finite-dimensional verification runner for

    docs/COMMENSURATION_GENERAL_LEMMA_PERIOD_PARITY_BOUNDED_THEOREM_NOTE_2026-06-12.md

This extends the landed d=3 step-2 commensuration criterion.
The K-chart periods are (L/2, L, L/2).  The residue-class claim is that the
minimal-vector d^2 parity agrees with the chart parity exactly when every
K-period is even, i.e. exactly when L = 0 mod 4 for even L.

Anchor gates are first and compare the only Hamiltonian computation here
(L=8 and L=10) against frozen parent constants.  The general lemma is then
sanity-checked by SymPy residue algebra (formula/table check, not an
independent proof) and verified by a cheap combinatorial grid.

Run: python3 scripts/frontier_commensuration_general_lemma_2026_06_12.py
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import product
import sys

import numpy as np
import sympy as sp


DIM = 3
T = 1.0
MU = 5.0

ANCHOR_L_VALUES = (8, 10)
EXTENDED_L_VALUES = (8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30)

FROZEN_PARENT_HKD_AFTER_L8 = 0.0
FROZEN_PARENT_HKD_AFTER_L10 = 7.483249786301930e-1
HKD_AFTER_ABS_TOL = 1.0e-12
PROTECTED_HKD_TOL = 1.0e-14
FAILING_HKD_MIN = 1.0e-1
ANTI_FAB_D2_MIN = 1

FROZEN_L10_FAIL_LEFT = (0, 0, 0)
FROZEN_L10_FAIL_RIGHT = (0, 0, 3)
FROZEN_L10_FAIL_DELTA = (0, 0, -2)
FROZEN_L10_D2_PARITY = 0
FROZEN_L10_CHART_DELTA_PARITY = 1

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class HAnchor:
    L: int
    periods: tuple[int, int, int]
    hkd_before: float
    hkd_after: float


@dataclass(frozen=True)
class ParityCheck:
    holds: bool
    total_kept_decimated_pairs: int
    mismatch_count: int
    first_mismatch: tuple[
        tuple[int, int, int],
        tuple[int, int, int],
        tuple[int, int, int],
        int,
        int,
    ] | None


@dataclass(frozen=True)
class SymbolicCaseSplit:
    l0_mismatch_sum: int
    l2_flip_mismatch_rows: tuple[tuple[int, int, int], ...]
    l2_forced_minimal_z: sp.Expr
    l2_forced_mismatch: sp.Expr


def check(label: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS: {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {label} :: {detail}")


def minimal_delta(a: int, b: int, period: int) -> int:
    delta = (b - a) % period
    if delta > period // 2:
        delta -= period
    return int(delta)


def minimal_vector(
    left: tuple[int, int, int],
    right: tuple[int, int, int],
    periods: tuple[int, int, int],
) -> tuple[int, int, int]:
    return tuple(minimal_delta(a, b, p) for a, b, p in zip(left, right, periods))


def chart_parity(chart: tuple[int, int, int]) -> int:
    return int(sum(chart) & 1)


def k_chart_sites(L: int) -> list[tuple[int, int, int]]:
    return [
        (a, b, c)
        for a in range(L // 2)
        for b in range(L)
        for c in range(L // 2)
    ]


def retained_coord_from_chart(chart: tuple[int, int, int], L: int) -> tuple[int, int, int]:
    a, b, c = chart
    return (a % L, b % L, (2 * c - a - b) % L)


def retained_sites(L: int) -> tuple[list[tuple[int, int, int]], list[tuple[int, int, int]]]:
    charts: list[tuple[int, int, int]] = []
    coords: list[tuple[int, int, int]] = []
    for a in range(L):
        for b in range(L):
            for c in range(L // 2):
                chart = (a, b, c)
                charts.append(chart)
                coords.append(retained_coord_from_chart(chart, L))
    return charts, coords


def k_chart_from_r_chart(r_chart: tuple[int, int, int]) -> tuple[int, int, int]:
    a, b, c = r_chart
    return (a // 2, b, c)


def step1_displacements() -> tuple[tuple[tuple[int, int, int], float], ...]:
    displacements: list[tuple[tuple[int, int, int], float]] = [
        ((0, 0, 0), MU - (6.0 * T * T / MU)),
    ]
    axial_value = -(T * T / MU)
    face_value = -(2.0 * T * T / MU)

    for axis in range(DIM):
        for step in (-2, 2):
            delta = [0, 0, 0]
            delta[axis] = step
            displacements.append((tuple(delta), axial_value))

    for zero_axis in range(DIM):
        axes = [axis for axis in range(DIM) if axis != zero_axis]
        for s0 in (-1, 1):
            for s1 in (-1, 1):
                delta = [0, 0, 0]
                delta[axes[0]] = s0
                delta[axes[1]] = s1
                displacements.append((tuple(delta), face_value))

    return tuple(displacements)


STEP1_DISPLACEMENTS = step1_displacements()


def step2_output(L: int) -> tuple[np.ndarray, list[tuple[int, int, int]], tuple[int, int, int]]:
    r_charts, r_coords = retained_sites(L)
    n = len(r_charts)
    keep_pos = np.full(n, -1, dtype=int)
    drop_pos = np.full(n, -1, dtype=int)
    k_charts: list[tuple[int, int, int]] = []

    keep_count = 0
    drop_count = 0
    for i, chart in enumerate(r_charts):
        if chart[0] % 2 == 0:
            keep_pos[i] = keep_count
            keep_count += 1
            k_charts.append(k_chart_from_r_chart(chart))
        else:
            drop_pos[i] = drop_count
            drop_count += 1

    h_kk = np.zeros((keep_count, keep_count), dtype=float)
    h_kd = np.zeros((keep_count, drop_count), dtype=float)
    h_dd = np.zeros((drop_count, drop_count), dtype=float)
    coord_to_index = {coord: i for i, coord in enumerate(r_coords)}

    for i, coord in enumerate(r_coords):
        x, y, z = coord
        i_keep = keep_pos[i]
        i_drop = drop_pos[i]
        for (dx, dy, dz), value in STEP1_DISPLACEMENTS:
            j = coord_to_index[((x + dx) % L, (y + dy) % L, (z + dz) % L)]
            j_keep = keep_pos[j]
            if i_keep >= 0:
                if j_keep >= 0:
                    h_kk[i_keep, j_keep] = value
                else:
                    h_kd[i_keep, drop_pos[j]] = value
            elif j_keep < 0:
                h_dd[i_drop, drop_pos[j]] = value

    solved = np.linalg.solve(h_dd, h_kd.T)
    h2 = h_kk - h_kd @ solved
    return h2, k_charts, (L // 2, L, L // 2)


def next_checkerboard_hkd_maxima(
    matrix: np.ndarray,
    charts: list[tuple[int, int, int]],
    periods: tuple[int, int, int],
) -> tuple[float, float]:
    keep = [i for i, chart in enumerate(charts) if chart_parity(chart) == 0]
    drop = [i for i, chart in enumerate(charts) if chart_parity(chart) == 1]
    before = float(np.max(np.abs(matrix[np.ix_(keep, drop)])))
    after = 0.0
    for i in keep:
        ci = charts[i]
        row = matrix[i]
        for j in drop:
            delta = minimal_vector(ci, charts[j], periods)
            if sum(v * v for v in delta) % 2 == 0:
                after = max(after, abs(float(row[j])))
    return before, after


def compute_h_anchor(L: int) -> HAnchor:
    matrix, charts, periods = step2_output(L)
    before, after = next_checkerboard_hkd_maxima(matrix, charts, periods)
    return HAnchor(L=L, periods=periods, hkd_before=before, hkd_after=after)


def coordinate_pair_table(period: int) -> dict[tuple[int, int, int], int]:
    counts: dict[tuple[int, int, int], int] = defaultdict(int)
    for left in range(period):
        for right in range(period):
            delta = minimal_delta(left, right, period)
            counts[(left & 1, right & 1, (delta * delta) & 1)] += 1
    return dict(counts)


def parity_correspondence_counts(L: int) -> ParityCheck:
    periods = (L // 2, L, L // 2)
    state: dict[tuple[int, int, int], int] = {(0, 0, 0): 1}
    for period in periods:
        next_state: dict[tuple[int, int, int], int] = defaultdict(int)
        axis_counts = coordinate_pair_table(period)
        for (left_sum, right_sum, d2_sum), base_count in state.items():
            for (left_par, right_par, d2_par), axis_count in axis_counts.items():
                next_state[
                    (
                        (left_sum + left_par) & 1,
                        (right_sum + right_par) & 1,
                        (d2_sum + d2_par) & 1,
                    )
                ] += base_count * axis_count
        state = dict(next_state)

    mismatch_count = state.get((0, 1, 0), 0)
    match_count = state.get((0, 1, 1), 0)
    first = first_mismatch(L, periods) if mismatch_count else None
    return ParityCheck(
        holds=mismatch_count == 0,
        total_kept_decimated_pairs=match_count + mismatch_count,
        mismatch_count=mismatch_count,
        first_mismatch=first,
    )


def first_mismatch(
    L: int,
    periods: tuple[int, int, int],
) -> tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int], int, int] | None:
    charts = k_chart_sites(L)
    lefts = [chart for chart in charts if chart_parity(chart) == 0]
    rights = [chart for chart in charts if chart_parity(chart) == 1]
    for left in lefts:
        for right in rights:
            delta = minimal_vector(left, right, periods)
            d2_parity = int(sum(v * v for v in delta) & 1)
            chart_delta_parity = chart_parity(left) ^ chart_parity(right)
            if d2_parity != chart_delta_parity:
                return (left, right, delta, d2_parity, chart_delta_parity)
    return None


def symbolic_case_split() -> SymbolicCaseSplit:
    a, b, c, q, fx, fz = sp.symbols("a b c q fx fz", integer=True, nonnegative=True)

    l0_mismatch_sum = 0
    for apar, bpar, cpar in product((0, 1), repeat=3):
        chart = sp.Mod(apar + bpar + cpar, 2)
        d2 = sp.Mod(apar + bpar + cpar, 2)
        l0_mismatch_sum += int(sp.Mod(d2 - chart, 2))

    l2_rows: list[tuple[int, int, int]] = []
    l2_d2_expr = sp.Mod(a + b + c + fx + fz, 2)
    l2_chart_expr = sp.Mod(a + b + c, 2)
    for fxv, fzv in product((0, 1), repeat=2):
        mismatch_values: set[int] = set()
        for apar, bpar, cpar in product((0, 1), repeat=3):
            d2_val = int(l2_d2_expr.subs({a: apar, b: bpar, c: cpar, fx: fxv, fz: fzv}))
            chart_val = int(l2_chart_expr.subs({a: apar, b: bpar, c: cpar}))
            mismatch_values.add(d2_val ^ chart_val)
        if len(mismatch_values) != 1:
            raise AssertionError("nonconstant L=2 mod 4 flip table")
        l2_rows.append((fxv, fzv, mismatch_values.pop()))

    period_z = 2 * q + 1
    high_z_residue = q + 1
    forced_minimal_z = sp.simplify(high_z_residue - period_z)
    forced_d2_parity = sp.Mod(q, 2)
    forced_chart_delta_parity = sp.Mod(q + 1, 2)
    forced_mismatch = sp.simplify(sp.Mod(forced_chart_delta_parity - forced_d2_parity, 2))

    return SymbolicCaseSplit(
        l0_mismatch_sum=l0_mismatch_sum,
        l2_flip_mismatch_rows=tuple(l2_rows),
        l2_forced_minimal_z=forced_minimal_z,
        l2_forced_mismatch=forced_mismatch,
    )


def run_anchor_gates(anchors: dict[int, HAnchor], l10_parity: ParityCheck) -> None:
    print("A. landed Hamiltonian anchors first")
    check(
        "A1 L=8 H_kd_after equals frozen parent protected value",
        abs(anchors[8].hkd_after - FROZEN_PARENT_HKD_AFTER_L8) <= HKD_AFTER_ABS_TOL,
        (
            f"computed={anchors[8].hkd_after:.16e}, "
            f"frozen={FROZEN_PARENT_HKD_AFTER_L8:.16e}, tol={HKD_AFTER_ABS_TOL:.1e}"
        ),
    )
    check(
        "A2 L=10 H_kd_after equals frozen parent failing value",
        abs(anchors[10].hkd_after - FROZEN_PARENT_HKD_AFTER_L10) <= HKD_AFTER_ABS_TOL,
        (
            f"computed={anchors[10].hkd_after:.16e}, "
            f"frozen={FROZEN_PARENT_HKD_AFTER_L10:.16e}, tol={HKD_AFTER_ABS_TOL:.1e}"
        ),
    )
    check(
        "A3 L=8/L=10 H_kd_after dichotomy is protected/failing",
        anchors[8].hkd_after <= PROTECTED_HKD_TOL and anchors[10].hkd_after >= FAILING_HKD_MIN,
        (
            f"L8={anchors[8].hkd_after:.3e} <= {PROTECTED_HKD_TOL:.1e}; "
            f"L10={anchors[10].hkd_after:.3e} >= {FAILING_HKD_MIN:.1e}"
        ),
    )

    first = l10_parity.first_mismatch
    first_matches_frozen = first == (
        FROZEN_L10_FAIL_LEFT,
        FROZEN_L10_FAIL_RIGHT,
        FROZEN_L10_FAIL_DELTA,
        FROZEN_L10_D2_PARITY,
        FROZEN_L10_CHART_DELTA_PARITY,
    )
    d2_norm = -1 if first is None else sum(v * v for v in first[2])
    mismatch_bit = -1 if first is None else first[3] ^ first[4]
    print(
        "  L=10 failing coset: "
        f"left={None if first is None else first[0]}, "
        f"right={None if first is None else first[1]}, "
        f"minimal_vector={None if first is None else first[2]}, "
        f"d2_parity={None if first is None else first[3]}, "
        f"chart_delta_parity={None if first is None else first[4]}"
    )
    check(
        "A4 anti-fabrication L=10 failing coset is frozen and nontrivial",
        first_matches_frozen and d2_norm >= ANTI_FAB_D2_MIN and mismatch_bit == 1,
        (
            f"d2_norm={d2_norm}, min={ANTI_FAB_D2_MIN}, "
            f"mismatch_bit={mismatch_bit}, frozen_match={first_matches_frozen}"
        ),
    )


def run_symbolic_gates(symbolic: SymbolicCaseSplit) -> None:
    print("B. symbolic residue-class algebra")
    print("  L=0 mod 4: all K-periods even, so minimal parity equals chart parity.")
    print(
        "  L=2 mod 4: d2_mod2 = chart_mod2 + high_x + high_z (mod 2); "
        f"flip rows={symbolic.l2_flip_mismatch_rows}"
    )
    print(
        "  forced L=2 mod 4 high-z coset: "
        f"minimal_z={symbolic.l2_forced_minimal_z}, mismatch={symbolic.l2_forced_mismatch}"
    )
    check(
        "B1 SymPy L=0 mod 4 residue table has zero mismatches",
        symbolic.l0_mismatch_sum == 0,
        f"mismatch_sum={symbolic.l0_mismatch_sum}",
    )
    check(
        "B2 SymPy L=2 mod 4 flip table: odd-axis parity-flip branch forces the mismatch",
        symbolic.l2_flip_mismatch_rows == ((0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)),
        f"rows={symbolic.l2_flip_mismatch_rows}",
    )
    check(
        "B3 SymPy forced odd-period coset flips parity",
        symbolic.l2_forced_minimal_z == -sp.symbols("q", integer=True, nonnegative=True)
        and symbolic.l2_forced_mismatch == 1,
        f"minimal_z={symbolic.l2_forced_minimal_z}, mismatch={symbolic.l2_forced_mismatch}",
    )


def run_grid_gates(results: dict[int, ParityCheck]) -> None:
    print("C. extended combinatorial grid")
    for L in EXTENDED_L_VALUES:
        result = results[L]
        expected_holds = L % 4 == 0
        first_detail = "none" if result.first_mismatch is None else str(result.first_mismatch)
        print(
            f"  L={L:2d} periods={(L // 2, L, L // 2)} "
            f"pairs={result.total_kept_decimated_pairs} mismatches={result.mismatch_count} "
            f"holds={result.holds} first_mismatch={first_detail}"
        )
        check(
            f"C L={L} correspondence iff L=0 mod 4",
            result.holds == expected_holds,
            f"holds={result.holds}, expected={expected_holds}, mismatches={result.mismatch_count}",
        )

    check(
        "C-summary protected L values have zero mismatches",
        all(results[L].mismatch_count == 0 for L in EXTENDED_L_VALUES if L % 4 == 0),
        "protected grid L=(8,12,16,20,24,28)",
    )
    check(
        "C-summary unprotected L values have at least one mismatch",
        all(results[L].mismatch_count >= 1 for L in EXTENDED_L_VALUES if L % 4 == 2),
        "unprotected grid L=(10,14,18,22,26,30)",
    )


def main() -> int:
    print("commensuration general lemma period-parity runner")
    print(f"parameters: d={DIM}, t={T:.1f}, mu={MU:.1f}")
    print(f"extended_grid={EXTENDED_L_VALUES}")
    try:
        anchors = {L: compute_h_anchor(L) for L in ANCHOR_L_VALUES}
        l10_parity = parity_correspondence_counts(10)
        run_anchor_gates(anchors, l10_parity)

        symbolic = symbolic_case_split()
        run_symbolic_gates(symbolic)

        grid_results = {L: parity_correspondence_counts(L) for L in EXTENDED_L_VALUES}
        run_grid_gates(grid_results)
    except Exception as exc:
        global FAIL
        FAIL += 1
        print(f"FAIL: runner exception :: {exc!r}")

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
