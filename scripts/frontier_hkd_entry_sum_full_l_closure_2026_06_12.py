#!/usr/bin/env python3
"""Full-L support runner for the d=3 H_kd entry-support criterion.

This runner computes the bounded dense-anchor HKD entry decomposition
self-contained and combines those anchors with the unconditional period-parity
lemma from
``frontier_commensuration_unconditional_lemma_2026_06_12.py``.

Dense Hamiltonian work is deliberately restricted to the anchor grid
L = {8, 10, 12, 14, 16, 18}.  The full-L support claim is combinatorial and is
checked for every even L in {8, ..., 40}; this runner does not claim an all-L
dense-Hamiltonian magnitude theorem.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

import numpy as np


DIM = 3
T = 1.0
MU = 5.0

ANCHOR_L_VALUES = (8, 10, 12, 14, 16, 18)
FULL_L_VALUES = tuple(range(8, 42, 2))
MAX_DENSE_HAMILTONIAN_L = 18

PROTECTION_TOL = 1.0e-14
ENTRY_NONZERO_TOL = 1.0e-12
NONZERO_BEFORE_TOL = 1.0e-12
STEP1_ANCHOR_TOL = 1.0e-12
WITNESS_MAGNITUDE_MIN = 1.0e-6

FROZEN_HKD_AFTER_ANCHORS = (
    (8, 0.0),
    (10, 7.4832497863019298e-01),
    (12, 0.0),
    (14, 7.4732149222164002e-01),
    (16, 0.0),
    (18, 7.4728589243652488e-01),
)
FROZEN_HKD_ANCHOR_ABS_TOL = 1.0e-12
FROZEN_STEP1_ANCHOR_ERROR_L8 = 0.0
FROZEN_STEP1_OO_OFFDIAG_L8 = 0.0

FROZEN_ANCHOR_MISALIGNED_COUNTS = (
    (8, 0),
    (10, 5700),
    (12, 0),
    (14, 43512),
    (16, 0),
    (18, 197640),
)
FROZEN_AXIS_FLIP_SIGNATURE = (
    (0, (0,), (0,)),
    (1, (0, 1), (0, 1)),
)
FROZEN_EXISTENCE_BY_PERIOD_PARITY = (
    ((0, 0, 0), (False,)),
    ((1, 0, 1), (True,)),
)
FROZEN_FULL_L_COUNTEREXAMPLES = 0
FROZEN_L22_WITNESS = ((0, 0, 0), (0, 1, 6), (0, 1, -5), 0, 1)
FROZEN_DENSE_L_VALUES = (8, 10, 12, 14, 16, 18)

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class MisalignmentWitness:
    left: tuple[int, int, int]
    right: tuple[int, int, int]
    minimal_delta: tuple[int, int, int]
    d2_parity: int
    chart_pair_parity: int
    magnitude: float


@dataclass(frozen=True)
class EntryDecomposition:
    hkd_before: float
    hkd_after: float
    nonzero_before_entries: int
    surviving_even_d2_entries: int
    aligned_surviving_entries: int
    misaligned_surviving_entries: int
    max_misaligned_magnitude: float
    witness: MisalignmentWitness | None


@dataclass(frozen=True)
class AnchorResult:
    L: int
    periods: tuple[int, int, int]
    all_periods_even: bool
    decomposition: EntryDecomposition


@dataclass(frozen=True)
class FullLRow:
    L: int
    periods: tuple[int, int, int]
    period_parities: tuple[int, int, int]
    some_period_odd: bool
    l_not_0_mod_4: bool
    misaligned_count: int
    misaligned_exists: bool


def check(label: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS: {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {label} :: {detail}")


def chart_periods(L: int) -> tuple[int, int, int]:
    return (L // 2, L, L // 2)


def chart_parity(chart: tuple[int, int, int]) -> int:
    return int(sum(chart) & 1)


def site_index(coord: tuple[int, int, int], L: int) -> int:
    x, y, z = coord
    return (x * L + y) * L + z


def minimal_delta(left: int, right: int, period: int) -> int:
    """Landed centered representative; ties at period/2 stay positive."""
    delta = (right - left) % period
    if delta > period // 2:
        delta -= period
    return int(delta)


def minimal_vector(
    left: tuple[int, int, int],
    right: tuple[int, int, int],
    periods: tuple[int, int, int],
) -> tuple[int, int, int]:
    return tuple(minimal_delta(a, b, q) for a, b, q in zip(left, right, periods))


def d2_parity_between(
    left: tuple[int, int, int],
    right: tuple[int, int, int],
    periods: tuple[int, int, int],
) -> tuple[int, tuple[int, int, int]]:
    delta = minimal_vector(left, right, periods)
    return int(sum(v * v for v in delta) & 1), delta


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


def original_hamiltonian(L: int) -> np.ndarray:
    n = L**DIM
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
                    neighbor = ((x + dx) % L, (y + dy) % L, (z + dz) % L)
                    h[i, site_index(neighbor, L)] = T
    return h


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


def step1_dense_schur_anchor(L: int) -> tuple[float, float]:
    coords = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    retained = [i for i, coord in enumerate(coords) if chart_parity(coord) == 0]
    eliminated = [i for i, coord in enumerate(coords) if chart_parity(coord) == 1]
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


def step2_output(
    L: int,
) -> tuple[np.ndarray, list[tuple[int, int, int]], tuple[int, int, int]]:
    if L > MAX_DENSE_HAMILTONIAN_L:
        raise ValueError(f"dense Hamiltonian construction forbidden for L={L}")

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
    return h2, k_charts, chart_periods(L)


def decompose_hkd_entries(
    matrix: np.ndarray,
    charts: list[tuple[int, int, int]],
    periods: tuple[int, int, int],
) -> EntryDecomposition:
    keep = [i for i, chart in enumerate(charts) if chart_parity(chart) == 0]
    drop = [i for i, chart in enumerate(charts) if chart_parity(chart) == 1]

    hkd_before = 0.0
    hkd_after = 0.0
    nonzero_before_entries = 0
    surviving_even_d2_entries = 0
    aligned_surviving_entries = 0
    misaligned_surviving_entries = 0
    max_misaligned_magnitude = 0.0
    witness: MisalignmentWitness | None = None

    for i in keep:
        left = charts[i]
        row = matrix[i]
        left_parity = chart_parity(left)
        for j in drop:
            right = charts[j]
            magnitude = abs(float(row[j]))
            if magnitude > hkd_before:
                hkd_before = magnitude
            if magnitude > ENTRY_NONZERO_TOL:
                nonzero_before_entries += 1

            d2_parity, delta = d2_parity_between(left, right, periods)
            if d2_parity != 0:
                continue

            if magnitude > hkd_after:
                hkd_after = magnitude
            if magnitude <= ENTRY_NONZERO_TOL:
                continue

            surviving_even_d2_entries += 1
            chart_pair_parity = left_parity ^ chart_parity(right)
            if d2_parity == chart_pair_parity:
                aligned_surviving_entries += 1
            else:
                misaligned_surviving_entries += 1
                if magnitude > max_misaligned_magnitude:
                    max_misaligned_magnitude = magnitude
                    witness = MisalignmentWitness(
                        left=left,
                        right=right,
                        minimal_delta=delta,
                        d2_parity=d2_parity,
                        chart_pair_parity=chart_pair_parity,
                        magnitude=magnitude,
                    )

    return EntryDecomposition(
        hkd_before=hkd_before,
        hkd_after=hkd_after,
        nonzero_before_entries=nonzero_before_entries,
        surviving_even_d2_entries=surviving_even_d2_entries,
        aligned_surviving_entries=aligned_surviving_entries,
        misaligned_surviving_entries=misaligned_surviving_entries,
        max_misaligned_magnitude=max_misaligned_magnitude,
        witness=witness,
    )


def compute_anchor_result(L: int) -> AnchorResult:
    h2, charts, periods = step2_output(L)
    decomposition = decompose_hkd_entries(h2, charts, periods)
    del h2
    return AnchorResult(
        L=L,
        periods=periods,
        all_periods_even=all(period % 2 == 0 for period in periods),
        decomposition=decomposition,
    )


def compute_anchor_grid() -> dict[int, AnchorResult]:
    return {L: compute_anchor_result(L) for L in ANCHOR_L_VALUES}


def coordinate_pair_table(period: int) -> dict[tuple[int, int, int], int]:
    counts: dict[tuple[int, int, int], int] = defaultdict(int)
    for left in range(period):
        for right in range(period):
            delta = minimal_delta(left, right, period)
            counts[(left & 1, right & 1, (delta * delta) & 1)] += 1
    return dict(counts)


def combinatorial_misaligned_survivor_count(L: int) -> int:
    state: dict[tuple[int, int, int], int] = {(0, 0, 0): 1}
    for period in chart_periods(L):
        next_state: dict[tuple[int, int, int], int] = defaultdict(int)
        axis_counts = coordinate_pair_table(period)
        for (left_sum, right_sum, d2_sum), base_count in state.items():
            for (left_parity, right_parity, d2_parity), axis_count in axis_counts.items():
                next_state[
                    (
                        (left_sum + left_parity) & 1,
                        (right_sum + right_parity) & 1,
                        (d2_sum + d2_parity) & 1,
                    )
                ] += base_count * axis_count
        state = dict(next_state)

    # HKD kept-decimated after even-d2 truncation: left even, right odd, d2 even.
    # For this block chart_pair_parity=1 and d2_parity=0, hence every survivor
    # in this cell is misaligned.
    return state.get((0, 1, 0), 0)


def axis_flip_support(period: int) -> tuple[int, ...]:
    support = set()
    for (left_parity, right_parity, d2_parity), count in coordinate_pair_table(period).items():
        if count:
            support.add(left_parity ^ right_parity ^ d2_parity)
    return tuple(sorted(support))


def axis_signature() -> tuple[tuple[int, tuple[int, ...], tuple[int, ...]], ...]:
    return (
        (0, axis_flip_support(4), axis_flip_support(8)),
        (1, axis_flip_support(5), axis_flip_support(11)),
    )


def compute_full_l_rows() -> tuple[FullLRow, ...]:
    rows: list[FullLRow] = []
    for L in FULL_L_VALUES:
        periods = chart_periods(L)
        period_parities = tuple(period & 1 for period in periods)
        count = combinatorial_misaligned_survivor_count(L)
        rows.append(
            FullLRow(
                L=L,
                periods=periods,
                period_parities=period_parities,
                some_period_odd=any(period_parities),
                l_not_0_mod_4=(L % 4) != 0,
                misaligned_count=count,
                misaligned_exists=count > 0,
            )
        )
    return tuple(rows)


def existence_by_period_parity(rows: tuple[FullLRow, ...]) -> tuple[tuple[tuple[int, int, int], tuple[bool, ...]], ...]:
    classes: dict[tuple[int, int, int], set[bool]] = defaultdict(set)
    for row in rows:
        classes[row.period_parities].add(row.misaligned_exists)
    return tuple(
        (period_parities, tuple(sorted(values)))
        for period_parities, values in sorted(classes.items())
    )


def l22_witness() -> tuple[
    tuple[int, int, int],
    tuple[int, int, int],
    tuple[int, int, int],
    int,
    int,
]:
    L = 22
    periods = chart_periods(L)
    odd_axis_witness = (periods[2] + 1) // 2
    left = (0, 0, 0)
    right = (0, 1, odd_axis_witness)
    d2_parity, delta = d2_parity_between(left, right, periods)
    chart_pair_parity = chart_parity(left) ^ chart_parity(right)
    return (left, right, delta, d2_parity, chart_pair_parity)


def run_s0_anchor_gates(
    anchor_results: dict[int, AnchorResult],
    step1_anchor_error: float,
    step1_oo_offdiag: float,
) -> None:
    print("S0 anchors")
    for L, frozen_after in FROZEN_HKD_AFTER_ANCHORS:
        computed = anchor_results[L].decomposition.hkd_after
        protected_clause = True
        if frozen_after == 0.0:
            protected_clause = computed < PROTECTION_TOL
        check(
            f"S0 L={L} H_kd_after reproduces frozen anchor",
            abs(computed - frozen_after) <= FROZEN_HKD_ANCHOR_ABS_TOL and protected_clause,
            (
                f"computed={computed:.16e}, frozen={frozen_after:.16e}, "
                f"anchor_tol={FROZEN_HKD_ANCHOR_ABS_TOL:.1e}, "
                f"protection_tol={PROTECTION_TOL:.1e}"
            ),
        )

    min_before = min(anchor_results[L].decomposition.hkd_before for L in ANCHOR_L_VALUES)
    check(
        "S0 anti-fabrication H_kd_before is nonzero on every anchor L",
        min_before > NONZERO_BEFORE_TOL,
        f"min_H_kd_before={min_before:.16e}, nonzero_tol={NONZERO_BEFORE_TOL:.1e}",
    )
    check(
        "S0 step-1 dense Schur anchor matches frozen zero error",
        abs(step1_anchor_error - FROZEN_STEP1_ANCHOR_ERROR_L8) <= STEP1_ANCHOR_TOL,
        (
            f"L=8, computed_error={step1_anchor_error:.3e}, "
            f"frozen={FROZEN_STEP1_ANCHOR_ERROR_L8:.1e}, tol={STEP1_ANCHOR_TOL:.1e}"
        ),
    )
    check(
        "S0 step-1 eliminated block offdiagonal matches frozen zero",
        abs(step1_oo_offdiag - FROZEN_STEP1_OO_OFFDIAG_L8) <= STEP1_ANCHOR_TOL,
        (
            f"L=8, computed_offdiag={step1_oo_offdiag:.3e}, "
            f"frozen={FROZEN_STEP1_OO_OFFDIAG_L8:.1e}, tol={STEP1_ANCHOR_TOL:.1e}"
        ),
    )
    check(
        "S0 dense Hamiltonian construction is restricted to the frozen anchor grid",
        ANCHOR_L_VALUES == FROZEN_DENSE_L_VALUES and max(ANCHOR_L_VALUES) == MAX_DENSE_HAMILTONIAN_L,
        f"dense_L_values={ANCHOR_L_VALUES}, max_dense_L={MAX_DENSE_HAMILTONIAN_L}",
    )


def print_anchor_table(anchor_results: dict[int, AnchorResult]) -> None:
    print("S1 anchor entry-decomposition table")
    print(
        "  L   periods        all_even  H_kd_before        H_kd_after         "
        "nonzero_before  d2_even_survivors  aligned  misaligned"
    )
    for L in ANCHOR_L_VALUES:
        row = anchor_results[L]
        dec = row.decomposition
        print(
            f"  {L:2d}  {str(row.periods):13s}  {str(row.all_periods_even):8s}  "
            f"{dec.hkd_before:.16e}  {dec.hkd_after:.16e}  "
            f"{dec.nonzero_before_entries:14d}  {dec.surviving_even_d2_entries:17d}  "
            f"{dec.aligned_surviving_entries:7d}  {dec.misaligned_surviving_entries:10d}"
        )


def run_s1_criterion_gates(anchor_results: dict[int, AnchorResult]) -> None:
    print("S1 L-independent survivor criterion")
    print(
        "  criterion: kept-decimated survivor after even-d2 truncation is the "
        "parity cell left_chart=0, right_chart=1, d2=0; in this cell "
        "chart_pair_parity=1 != d2_parity=0, so each nonzero survivor is misaligned."
    )
    print(
        "  per-axis dependence: even period has flip support {0}; odd period has "
        "flip support {0,1}.  Only period parity enters the existence criterion."
    )
    print_anchor_table(anchor_results)

    dense_counts = tuple(
        (L, anchor_results[L].decomposition.misaligned_surviving_entries)
        for L in ANCHOR_L_VALUES
    )
    combinatorial_counts = tuple(
        (L, combinatorial_misaligned_survivor_count(L)) for L in ANCHOR_L_VALUES
    )
    check(
        "S1 dense Hamiltonian misaligned counts reproduce frozen grid counts",
        dense_counts == FROZEN_ANCHOR_MISALIGNED_COUNTS,
        f"observed={dense_counts}",
    )
    check(
        "S1 combinatorial predictor reproduces frozen grid counts",
        combinatorial_counts == FROZEN_ANCHOR_MISALIGNED_COUNTS,
        f"observed={combinatorial_counts}",
    )
    check(
        "S1 combinatorial predictor equals Hamiltonian truth on the anchor grid",
        combinatorial_counts == dense_counts,
        f"combinatorial={combinatorial_counts}, dense={dense_counts}",
    )
    check(
        "S1 axis flip support depends only on period parity",
        axis_signature() == FROZEN_AXIS_FLIP_SIGNATURE,
        f"signature={axis_signature()}",
    )


def print_full_l_table(rows: tuple[FullLRow, ...]) -> None:
    print("S2 full-L combinatorial support dichotomy table")
    print("  L   periods          q_parity   count       exists  L!=0mod4  some_q_odd")
    for row in rows:
        print(
            f"  {row.L:2d}  {str(row.periods):15s}  {str(row.period_parities):9s}  "
            f"{row.misaligned_count:10d}  {str(row.misaligned_exists):6s}  "
            f"{str(row.l_not_0_mod_4):8s}  {str(row.some_period_odd):10s}"
        )


def run_s2_full_l_gates(rows: tuple[FullLRow, ...]) -> None:
    print_full_l_table(rows)
    counterexamples = tuple(
        row.L
        for row in rows
        if not (
            row.misaligned_exists == row.l_not_0_mod_4 == row.some_period_odd
        )
    )
    check(
        "S2 full-L support criterion has zero counterexamples on every even L in {8,...,40}",
        len(counterexamples) == FROZEN_FULL_L_COUNTEREXAMPLES,
        f"counterexamples={counterexamples}, frozen={FROZEN_FULL_L_COUNTEREXAMPLES}",
    )
    check(
        "S2 existence classes are determined by chart-period parity",
        existence_by_period_parity(rows) == FROZEN_EXISTENCE_BY_PERIOD_PARITY,
        f"classes={existence_by_period_parity(rows)}",
    )


def run_s3_witness_gate() -> None:
    print("S3 L=22 combinatorial witness")
    witness = l22_witness()
    left, right, delta, d2_parity, chart_pair_parity = witness
    L = 22
    periods = chart_periods(L)
    count = combinatorial_misaligned_survivor_count(L)
    valid = (
        witness == FROZEN_L22_WITNESS
        and chart_parity(left) == 0
        and chart_parity(right) == 1
        and d2_parity == 0
        and chart_pair_parity == 1
        and d2_parity != chart_pair_parity
        and count > 0
    )
    print(
        f"  L=22 periods={periods}, witness={witness}, "
        f"misaligned_count={count}"
    )
    check(
        "S3 L=22 witness uses a=(q+1)/2 on an odd axis and is a valid surviving misaligned entry",
        valid,
        (
            f"left={left}, right={right}, delta={delta}, "
            f"d2_parity={d2_parity}, chart_pair_parity={chart_pair_parity}, "
            f"frozen={FROZEN_L22_WITNESS}, count={count}, "
            f"witness_magnitude_min={WITNESS_MAGNITUDE_MIN:.1e} applies only to dense anchors"
        ),
    )


def main() -> int:
    print("H_kd entry-support full-L period-parity runner")
    print(f"parameters: d={DIM}, t={T:.1f}, mu={MU:.1f}")
    print(f"anchor_L_values={ANCHOR_L_VALUES}; full_L_values={FULL_L_VALUES}")
    print("chart family: K-periods=(L/2,L,L/2)")
    try:
        anchor_results = compute_anchor_grid()
        step1_anchor_error, step1_oo_offdiag = step1_dense_schur_anchor(8)

        run_s0_anchor_gates(anchor_results, step1_anchor_error, step1_oo_offdiag)
        run_s1_criterion_gates(anchor_results)
        full_rows = compute_full_l_rows()
        run_s2_full_l_gates(full_rows)
        run_s3_witness_gate()
    except Exception as exc:
        global FAIL
        FAIL += 1
        print(f"FAIL: runner exception :: {exc!r}")

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
