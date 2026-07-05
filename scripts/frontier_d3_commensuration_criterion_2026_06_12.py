#!/usr/bin/env python3
"""Finite-dimensional verification for

    docs/D3_TRUNCATION_COMMENSURATION_CRITERION_BOUNDED_THEOREM_NOTE_2026-06-12.md

The runner mirrors the d=3 step-2 Schur machinery from
``frontier_d3_step2_range_unbounded_2026_06_12.py`` and tests the
commensuration criterion for the synthetic second chart family:

    on the tested grid, even-d^2 truncation protects the next checkerboard
    iff every K-chart period is even.  In this family K-periods are
    (L/2, L, L/2), so the protected cases are exactly L = 0 mod 4 on the
    tested grid.

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_d3_commensuration_criterion_2026_06_12.py
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "D3_TRUNCATION_COMMENSURATION_CRITERION_BOUNDED_THEOREM_NOTE_2026-06-12.md"

DIM = 3
T = 1.0
MU = 5.0

L_VALUES = (8, 10, 12, 14, 16, 18)
PROTECTED_L_VALUES = (8, 12, 16)
UNPROTECTED_L_VALUES = (10, 14, 18)

STEP1_ANCHOR_L = 8
STEP1_ANCHOR_TOL = 1.0e-12
NONZERO_TOL = 1.0e-12
NEXT_HKD_TOL = 1.0e-14
FAIL_BRANCH_MIN = 1.0e-1

WAVE8_L10_AFTER = 7.48e-1
WAVE8_L14_AFTER = 7.47e-1
WAVE8_ANCHOR_ABS_TOL = 1.0e-2

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class ParityCheck:
    holds: bool
    total_kept_decimated_pairs: int
    mismatch_count: int
    first_mismatch: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int], int, int] | None


@dataclass(frozen=True)
class LResult:
    L: int
    periods: tuple[int, int, int]
    hkd_before: float
    hkd_after: float
    parity: ParityCheck


def check(label: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS: {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {label} :: {detail}")


def site_index(coord: tuple[int, int, int], L: int) -> int:
    x, y, z = coord
    return (x * L + y) * L + z


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


def d2_between(
    left: tuple[int, int, int],
    right: tuple[int, int, int],
    periods: tuple[int, int, int],
) -> int:
    delta = minimal_vector(left, right, periods)
    return int(sum(v * v for v in delta))


def chart_parity(chart: tuple[int, int, int]) -> int:
    return int(sum(chart) & 1)


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


def k_chart_sites(L: int) -> list[tuple[int, int, int]]:
    return [
        (a, b, c)
        for a in range(L // 2)
        for b in range(L)
        for c in range(L // 2)
    ]


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


def build_step1_closed(L: int, coords: list[tuple[int, int, int]]) -> np.ndarray:
    n = len(coords)
    h = np.zeros((n, n), dtype=float)
    coord_to_index = {coord: i for i, coord in enumerate(coords)}
    for i, coord in enumerate(coords):
        x, y, z = coord
        for (dx, dy, dz), value in STEP1_DISPLACEMENTS:
            neighbor = ((x + dx) % L, (y + dy) % L, (z + dz) % L)
            h[i, coord_to_index[neighbor]] = value
    return h


def original_hamiltonian(L: int) -> np.ndarray:
    n = L ** DIM
    h = np.zeros((n, n), dtype=float)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = site_index((x, y, z), L)
                h[i, i] = MU
                for dx, dy, dz in (
                    (1, 0, 0),
                    (-1, 0, 0),
                    (0, 1, 0),
                    (0, -1, 0),
                    (0, 0, 1),
                    (0, 0, -1),
                ):
                    j = site_index(((x + dx) % L, (y + dy) % L, (z + dz) % L), L)
                    h[i, j] = T
    return h


def step1_dense_schur_anchor(L: int) -> tuple[float, float]:
    coords = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    retained = [i for i, c in enumerate(coords) if (c[0] + c[1] + c[2]) % 2 == 0]
    eliminated = [i for i, c in enumerate(coords) if (c[0] + c[1] + c[2]) % 2 == 1]
    h = original_hamiltonian(L)
    h_rr = h[np.ix_(retained, retained)]
    h_ro = h[np.ix_(retained, eliminated)]
    h_or = h[np.ix_(eliminated, retained)]
    h_oo = h[np.ix_(eliminated, eliminated)]
    schur = h_rr - h_ro @ np.linalg.solve(h_oo, h_or)
    closed = build_step1_closed(L, [coords[i] for i in retained])
    offdiag_oo = h_oo - np.diag(np.diag(h_oo))
    return (
        float(np.max(np.abs(schur - closed))),
        float(np.max(np.abs(offdiag_oo))),
    )


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
    del h_kk, h_kd, h_dd, solved
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
            if d2_between(ci, charts[j], periods) % 2 == 0:
                value = abs(float(row[j]))
                if value > after:
                    after = value
    return before, after


def parity_correspondence(L: int) -> ParityCheck:
    periods = (L // 2, L, L // 2)
    charts = k_chart_sites(L)
    keep = [chart for chart in charts if chart_parity(chart) == 0]
    drop = [chart for chart in charts if chart_parity(chart) == 1]
    total = 0
    mismatches = 0
    first: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int], int, int] | None = None

    for left in keep:
        for right in drop:
            total += 1
            chart_delta_parity = chart_parity(left) ^ chart_parity(right)
            delta = minimal_vector(left, right, periods)
            d2_parity = int(sum(v * v for v in delta) & 1)
            if d2_parity != chart_delta_parity:
                mismatches += 1
                if first is None:
                    first = (left, right, delta, d2_parity, chart_delta_parity)

    return ParityCheck(
        holds=mismatches == 0,
        total_kept_decimated_pairs=total,
        mismatch_count=mismatches,
        first_mismatch=first,
    )


def compute_l_result(L: int) -> LResult:
    h2, charts, periods = step2_output(L)
    before, after = next_checkerboard_hkd_maxima(h2, charts, periods)
    del h2
    return LResult(
        L=L,
        periods=periods,
        hkd_before=before,
        hkd_after=after,
        parity=parity_correspondence(L),
    )


def compute_grid() -> dict[int, LResult]:
    results: dict[int, LResult] = {}
    for L in L_VALUES:
        results[L] = compute_l_result(L)
    return results


def format_mismatch(parity: ParityCheck) -> str:
    if parity.first_mismatch is None:
        return "first_mismatch=None"
    left, right, delta, d2_parity, chart_delta_parity = parity.first_mismatch
    return (
        f"first_mismatch left={left}, right={right}, minimal_delta={delta}, "
        f"d2_parity={d2_parity}, chart_delta_parity={chart_delta_parity}"
    )


def print_dichotomy_table(results: dict[int, LResult]) -> None:
    print("S2 dichotomy table after even-d^2 truncation:")
    print("  L   K-periods       all_periods_even  parity_holds  H_kd_before        H_kd_after")
    for L in L_VALUES:
        result = results[L]
        all_even = all(period % 2 == 0 for period in result.periods)
        print(
            f"  {L:2d}  {str(result.periods):14s}  {str(all_even):16s}  "
            f"{str(result.parity.holds):12s}  "
            f"{result.hkd_before:.16e}  {result.hkd_after:.16e}"
        )


def run_checks(results: dict[int, LResult], step1_anchor_error: float, step1_oo_offdiag: float) -> None:
    print("S0 anchors")
    check(
        "S0 wave-8 anchor L=8 protection holds",
        results[8].hkd_after < NEXT_HKD_TOL,
        f"L=8 max_abs_after={results[8].hkd_after:.3e}, tol={NEXT_HKD_TOL:.1e}",
    )
    check(
        "S0 wave-8 anchor L=12 protection holds",
        results[12].hkd_after < NEXT_HKD_TOL,
        f"L=12 max_abs_after={results[12].hkd_after:.3e}, tol={NEXT_HKD_TOL:.1e}",
    )
    check(
        "S0 wave-8 anchor L=10 failure magnitude",
        abs(results[10].hkd_after - WAVE8_L10_AFTER) <= WAVE8_ANCHOR_ABS_TOL,
        (
            f"L=10 max_abs_after={results[10].hkd_after:.16e}, "
            f"anchor={WAVE8_L10_AFTER:.3f}, tol={WAVE8_ANCHOR_ABS_TOL:.1e}"
        ),
    )
    check(
        "S0 wave-8 anchor L=14 failure magnitude",
        abs(results[14].hkd_after - WAVE8_L14_AFTER) <= WAVE8_ANCHOR_ABS_TOL,
        (
            f"L=14 max_abs_after={results[14].hkd_after:.16e}, "
            f"anchor={WAVE8_L14_AFTER:.3f}, tol={WAVE8_ANCHOR_ABS_TOL:.1e}"
        ),
    )
    check(
        "S0 anti-fabrication next-checkerboard H_kd before truncation is nonzero at every L",
        all(results[L].hkd_before > NONZERO_TOL for L in L_VALUES),
        (
            "min_fixed_before="
            f"{min(results[L].hkd_before for L in L_VALUES):.16e}, "
            f"nonzero_tol={NONZERO_TOL:.1e}"
        ),
    )
    check(
        "S0 landed step-1 dense Schur anchor matches closed form",
        step1_anchor_error <= STEP1_ANCHOR_TOL,
        (
            f"L={STEP1_ANCHOR_L}, max_abs_error={step1_anchor_error:.3e}, "
            f"tol={STEP1_ANCHOR_TOL:.1e}"
        ),
    )
    check(
        "S0 landed step-1 eliminated block is diagonal",
        step1_oo_offdiag <= STEP1_ANCHOR_TOL,
        f"L={STEP1_ANCHOR_L}, max_offdiag={step1_oo_offdiag:.3e}, tol={STEP1_ANCHOR_TOL:.1e}",
    )

    print("S1 parity-correspondence finite check")
    for L in L_VALUES:
        parity = results[L].parity
        print(
            f"  L={L}: pairs={parity.total_kept_decimated_pairs}, "
            f"mismatches={parity.mismatch_count}, holds={parity.holds}; "
            f"{format_mismatch(parity)}"
        )

    check(
        "S1 correspondence holds for L=8,12,16",
        all(results[L].parity.holds for L in PROTECTED_L_VALUES),
        "protected_L_values=(8,12,16)",
    )
    check(
        "S1 correspondence fails for L=10,14,18",
        all(not results[L].parity.holds for L in UNPROTECTED_L_VALUES),
        "unprotected_L_values=(10,14,18)",
    )
    check(
        "S1 correspondence equals all-K-periods-even on the grid",
        all(results[L].parity.holds == all(period % 2 == 0 for period in results[L].periods) for L in L_VALUES),
        "K_periods=(L/2,L,L/2), grid=(8,10,12,14,16,18)",
    )
    check(
        "S1 correspondence-holds iff H_kd_after is below the fixed protection tolerance on the grid",
        all(results[L].parity.holds == (results[L].hkd_after < NEXT_HKD_TOL) for L in L_VALUES),
        f"fixed protection tolerance={NEXT_HKD_TOL:.1e}",
    )

    print_dichotomy_table(results)
    check(
        "S2 out-of-sample L=16 prediction: protection holds",
        results[16].hkd_after < NEXT_HKD_TOL,
        f"L=16 max_abs_after={results[16].hkd_after:.3e}, tol={NEXT_HKD_TOL:.1e}",
    )
    check(
        "S2 out-of-sample L=18 prediction: protection fails",
        results[18].hkd_after > FAIL_BRANCH_MIN,
        f"L=18 max_abs_after={results[18].hkd_after:.16e}, threshold={FAIL_BRANCH_MIN:.1e}",
    )
    check(
        "S2 protected branch L=8,12,16 holds at 1e-14",
        all(results[L].hkd_after < NEXT_HKD_TOL for L in PROTECTED_L_VALUES),
        (
            f"L8={results[8].hkd_after:.3e}, "
            f"L12={results[12].hkd_after:.3e}, "
            f"L16={results[16].hkd_after:.3e}, tol={NEXT_HKD_TOL:.1e}"
        ),
    )
    check(
        "S2 unprotected branch L=10,14,18 fails above 0.1",
        all(results[L].hkd_after > FAIL_BRANCH_MIN for L in UNPROTECTED_L_VALUES),
        (
            f"L10={results[10].hkd_after:.3e}, "
            f"L14={results[14].hkd_after:.3e}, "
            f"L18={results[18].hkd_after:.3e}, threshold={FAIL_BRANCH_MIN:.1e}"
        ),
    )

    print("S3 note hygiene")
    note = NOTE.read_text(encoding="utf-8")
    check(
        "canonical claim type is present and noncanonical Type front matter is absent",
        "**Claim type:** bounded_theorem" in note and "**Type:**" not in note,
        "bounded_theorem with single claim-type field",
    )
    check(
        "status authority and no-promotion statements are present",
        "**Status authority:** independent audit lane" in note
        and "**No-promotion statement:**" in note,
        "audit status remains independent",
    )
    check(
        "step-2 dichotomy and step-1 parity dependencies are linked",
        "[`D3_STEP2_RANGE_GROWTH_PERIOD_CLASS_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-12.md`]"
        "(D3_STEP2_RANGE_GROWTH_PERIOD_CLASS_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-12.md)" in note
        and "[`D3_CHECKERBOARD_STEP1_CLOSED_FORM_PARITY_LEMMA_BOUNDED_THEOREM_NOTE_2026-06-12.md`]"
        "(D3_CHECKERBOARD_STEP1_CLOSED_FORM_PARITY_LEMMA_BOUNDED_THEOREM_NOTE_2026-06-12.md)" in note,
        "dependency graph receives both structural anchors",
    )


def main() -> int:
    print("d=3 truncation commensuration criterion at E=0")
    print(f"parameters: d={DIM}, t={T:.1f}, mu={MU:.1f}, L_values={L_VALUES}")
    print("K-chart periods after synthetic step 2 are (L/2, L, L/2).")
    try:
        results = compute_grid()
        step1_anchor_error, step1_oo_offdiag = step1_dense_schur_anchor(STEP1_ANCHOR_L)
    except Exception as exc:
        global FAIL
        FAIL += 1
        print(f"FAIL: runner computation exception :: {exc!r}")
        print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
        return 1

    run_checks(results, step1_anchor_error, step1_oo_offdiag)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
