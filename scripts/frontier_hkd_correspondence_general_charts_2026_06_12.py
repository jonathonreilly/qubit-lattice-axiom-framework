#!/usr/bin/env python3
"""Bounded real-Schur HKD/correspondence check on general 3D charts.

Run:
    python3 scripts/frontier_hkd_correspondence_general_charts_2026_06_12.py

This runner intentionally computes the kept/decimated block from a real dense
nearest-neighbor Hamiltonian and Schur complements.  The parity count is a
separate support diagnostic; it is not used to manufacture H_kd_after.
"""

from __future__ import annotations

from dataclasses import dataclass
import itertools
import sys

import numpy as np


ZERO_TOL = 1.0e-14
FROZEN_VALUE_TOL = 1.0e-12
ONSITE = 4.0
HOP = -1.0
SCHUR_ENERGY = -0.6
DECIMATION_AXES = (0, 2)
FROZEN_PROTECTED_ANCHOR_HKD_AFTER = 0.0
FROZEN_UNPROTECTED_ANCHOR_HKD_AFTER = 0.7524355973958257
FROZEN_BEFORE_MIN = 0.5
FROZEN_EQUIVALENCE_EXPECTED = True
MAX_SITES_BOUND = 3000

ANCHOR_CHARTS = (
    ("anchor_L8_original_family_protected", (4, 8, 4)),
    ("anchor_L10_original_family_unprotected", (5, 10, 5)),
)

TEST_CHARTS = (
    ("all_even_cube", (4, 4, 4)),
    ("all_even_rectangular", (4, 6, 4)),
    ("one_odd_middle", (4, 5, 4)),
    ("one_odd_first_minimal", (3, 4, 4)),
    ("all_even_larger", (6, 6, 4)),
    ("one_odd_first", (5, 6, 4)),
)


@dataclass(frozen=True)
class AxisParity:
    raw: int
    periodic: int
    preserved: bool


@dataclass(frozen=True)
class SchurState:
    periods: tuple[int, int, int]
    coords: list[tuple[int, int, int]]
    h: np.ndarray


@dataclass(frozen=True)
class Witness:
    keep_coord: tuple[int, int, int]
    drop_coord: tuple[int, int, int]
    delta: tuple[int, int, int]
    raw_parities: tuple[int, int, int]
    periodic_parities: tuple[int, int, int]
    d2: int
    magnitude: float


@dataclass(frozen=True)
class ChartResult:
    label: str
    periods: tuple[int, int, int]
    sites: int
    schur_sites: int
    keep_count: int
    drop_count: int
    all_periods_even: bool
    hkd_before: float
    hkd_after: float
    misaligned_survivors: int
    witness: Witness | None


class CheckBook:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, name: str, condition: bool, detail: str) -> None:
        if bool(condition):
            self.pass_count += 1
            print(f"PASS: {name} -- {detail}")
        else:
            self.fail_count += 1
            print(f"FAIL: {name} -- {detail}")

    def finish(self) -> None:
        print(f"TOTAL: PASS={self.pass_count} FAIL={self.fail_count}")
        if self.fail_count:
            sys.exit(1)


def coords_for_periods(periods: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    q1, q2, q3 = periods
    return [(x, y, z) for x in range(q1) for y in range(q2) for z in range(q3)]


def site_parity(coord: tuple[int, int, int]) -> int:
    return (coord[0] + coord[1] + coord[2]) & 1


def raw_checkerboard_indices(
    coords: list[tuple[int, int, int]],
) -> tuple[np.ndarray, np.ndarray]:
    keep = np.array([i for i, coord in enumerate(coords) if site_parity(coord) == 0], dtype=np.int64)
    drop = np.array([i for i, coord in enumerate(coords) if site_parity(coord) == 1], dtype=np.int64)
    return keep, drop


def periodic_axis_delta(a: int, b: int, period: int) -> int:
    raw = abs(a - b)
    return min(raw, period - raw)


def axis_parity(a: int, b: int, period: int) -> AxisParity:
    raw = abs(a - b) & 1
    periodic = periodic_axis_delta(a, b, period) & 1
    return AxisParity(raw=raw, periodic=periodic, preserved=(raw == periodic))


def axis_decomposition(
    a: tuple[int, int, int], b: tuple[int, int, int], periods: tuple[int, int, int]
) -> tuple[tuple[int, int, int], tuple[AxisParity, AxisParity, AxisParity]]:
    deltas = tuple(periodic_axis_delta(a[i], b[i], periods[i]) for i in range(3))
    parities = tuple(axis_parity(a[i], b[i], periods[i]) for i in range(3))
    return deltas, parities  # type: ignore[return-value]


def periodic_d2_matrix(coords: list[tuple[int, int, int]], periods: tuple[int, int, int]) -> np.ndarray:
    coord_array = np.array(coords, dtype=np.int64)
    period_array = np.array(periods, dtype=np.int64)
    delta = np.abs(coord_array[:, None, :] - coord_array[None, :, :])
    delta = np.minimum(delta, period_array - delta)
    return np.sum(delta * delta, axis=2)


def build_nearest_neighbor_hamiltonian(periods: tuple[int, int, int]) -> SchurState:
    coords = coords_for_periods(periods)
    index = {coord: i for i, coord in enumerate(coords)}
    h = ONSITE * np.eye(len(coords), dtype=np.float64)

    for i, coord in enumerate(coords):
        for axis in range(3):
            neighbor = list(coord)
            neighbor[axis] = (neighbor[axis] + 1) % periods[axis]
            j = index[tuple(neighbor)]
            h[i, j] += HOP
            h[j, i] += HOP

    return SchurState(periods=periods, coords=coords, h=0.5 * (h + h.T))


def schur_decimate_axis_even(state: SchurState, axis: int) -> SchurState:
    keep = np.array(
        [i for i, coord in enumerate(state.coords) if coord[axis] % 2 == 0],
        dtype=np.int64,
    )
    drop = np.array(
        [i for i, coord in enumerate(state.coords) if coord[axis] % 2 == 1],
        dtype=np.int64,
    )
    if keep.size == 0 or drop.size == 0:
        raise ValueError(
            f"axis decimation needs nonempty kept/dropped sets; axis={axis}, "
            f"periods={state.periods}, keep={keep.size}, drop={drop.size}"
        )

    h_kk = state.h[np.ix_(keep, keep)]
    h_kd = state.h[np.ix_(keep, drop)]
    h_dd = state.h[np.ix_(drop, drop)] - SCHUR_ENERGY * np.eye(drop.size, dtype=np.float64)
    h_dk = state.h[np.ix_(drop, keep)]
    h_eff = h_kk - h_kd @ np.linalg.solve(h_dd, h_dk)
    h_eff = 0.5 * (h_eff + h_eff.T)
    h_eff[np.abs(h_eff) < 5.0e-16] = 0.0

    return SchurState(
        periods=state.periods,
        coords=[state.coords[int(i)] for i in keep],
        h=h_eff,
    )


def build_real_schur_state(periods: tuple[int, int, int]) -> SchurState:
    state = build_nearest_neighbor_hamiltonian(periods)
    for axis in DECIMATION_AXES:
        state = schur_decimate_axis_even(state, axis)
    return state


def truncate_even_d2(state: SchurState) -> SchurState:
    d2 = periodic_d2_matrix(state.coords, state.periods)
    keep = np.eye(state.h.shape[0], dtype=bool) | ((d2 % 2) == 0)
    h_trunc = np.where(keep, state.h, 0.0)
    h_trunc = 0.5 * (h_trunc + h_trunc.T)
    return SchurState(periods=state.periods, coords=list(state.coords), h=h_trunc)


def hkd_block_max(state: SchurState) -> float:
    keep, drop = raw_checkerboard_indices(state.coords)
    if keep.size == 0 or drop.size == 0:
        return 0.0
    block = state.h[np.ix_(keep, drop)]
    return float(np.max(np.abs(block))) if block.size else 0.0


def hkd_witness(state: SchurState) -> Witness | None:
    keep, drop = raw_checkerboard_indices(state.coords)
    if keep.size == 0 or drop.size == 0:
        return None
    block = state.h[np.ix_(keep, drop)]
    if not block.size:
        return None
    local_i, local_j = np.unravel_index(int(np.argmax(np.abs(block))), block.shape)
    magnitude = float(abs(block[local_i, local_j]))
    if magnitude <= ZERO_TOL:
        return None

    keep_coord = state.coords[int(keep[local_i])]
    drop_coord = state.coords[int(drop[local_j])]
    deltas, parities = axis_decomposition(keep_coord, drop_coord, state.periods)
    return Witness(
        keep_coord=keep_coord,
        drop_coord=drop_coord,
        delta=deltas,
        raw_parities=tuple(axis.raw for axis in parities),
        periodic_parities=tuple(axis.periodic for axis in parities),
        d2=sum(delta * delta for delta in deltas),
        magnitude=magnitude,
    )


def misaligned_survivor_count(
    coords: list[tuple[int, int, int]], periods: tuple[int, int, int]
) -> int:
    count = 0
    keep, drop = raw_checkerboard_indices(coords)
    for keep_index in keep:
        keep_coord = coords[int(keep_index)]
        for drop_index in drop:
            drop_coord = coords[int(drop_index)]
            _, parities = axis_decomposition(keep_coord, drop_coord, periods)
            periodic_sum = sum(axis.periodic for axis in parities) & 1
            raw_sum = sum(axis.raw for axis in parities) & 1
            if periodic_sum == 0 and raw_sum == 1:
                count += 1
    return count


def analyze_chart(label: str, periods: tuple[int, int, int]) -> ChartResult:
    sites = periods[0] * periods[1] * periods[2]
    if sites > MAX_SITES_BOUND:
        raise ValueError(f"{label}: sites={sites} exceeds MAX_SITES_BOUND={MAX_SITES_BOUND}")

    schur_state = build_real_schur_state(periods)
    hkd_before = hkd_block_max(schur_state)
    truncated_state = truncate_even_d2(schur_state)
    hkd_after = hkd_block_max(truncated_state)
    witness = hkd_witness(truncated_state)
    keep, drop = raw_checkerboard_indices(schur_state.coords)
    misaligned = misaligned_survivor_count(schur_state.coords, periods)

    return ChartResult(
        label=label,
        periods=periods,
        sites=sites,
        schur_sites=len(schur_state.coords),
        keep_count=int(keep.size),
        drop_count=int(drop.size),
        all_periods_even=all(period % 2 == 0 for period in periods),
        hkd_before=hkd_before,
        hkd_after=hkd_after,
        misaligned_survivors=misaligned,
        witness=witness,
    )


def period_axis_has_parity_flip(period: int) -> bool:
    for a, b in itertools.product(range(period), repeat=2):
        if axis_parity(a, b, period).preserved is False:
            return True
    return False


def print_result_table(title: str, results: tuple[ChartResult, ...]) -> None:
    print(title)
    print(
        "  label                              periods      sites schur keep/drop "
        "all_even H_before          H_after           misaligned"
    )
    for result in results:
        print(
            f"  {result.label:<34s} {str(result.periods):<12s} "
            f"{result.sites:5d} {result.schur_sites:5d} "
            f"{result.keep_count:4d}/{result.drop_count:<4d} "
            f"{str(result.all_periods_even):<8s} "
            f"{result.hkd_before: .16e} {result.hkd_after: .16e} "
            f"{result.misaligned_survivors:10d}"
        )
    print()


def describe_witness(prefix: str, result: ChartResult) -> None:
    if result.witness is None:
        print(
            f"{prefix}: {result.label} periods={result.periods}: "
            f"no real misaligned H_kd survivor; H_kd_after={result.hkd_after:.16e}"
        )
        return
    witness = result.witness
    print(
        f"{prefix}: {result.label} periods={result.periods}: "
        f"keep={witness.keep_coord} drop={witness.drop_coord} "
        f"delta={witness.delta} raw_parity={witness.raw_parities} "
        f"periodic_parity={witness.periodic_parities} d2={witness.d2} "
        f"magnitude={witness.magnitude:.16e} H_kd_after={result.hkd_after:.16e}"
    )


def dense_array_bound_mb(sites: int) -> float:
    return sites * sites * np.dtype(np.float64).itemsize / 1.0e6


def main() -> None:
    checks = CheckBook()

    print("# HKD/correspondence general-chart bounded real-Schur check")
    print("STATUS: pipeline-derived; audit lane grades.")
    print(
        "CONVENTION: dense nearest-neighbor Hamiltonian with "
        f"onsite={ONSITE:.1f}, hop={HOP:.1f}; fixed-energy Schur "
        f"E={SCHUR_ENERGY:.1f}; axis decimations={DECIMATION_AXES}; "
        "H_kd uses the raw checkerboard block after even-d2 truncation."
    )
    print(
        f"MEMORY: total sites per chart <= {MAX_SITES_BOUND}; largest single "
        f"dense float64 array at the bound is {dense_array_bound_mb(MAX_SITES_BOUND):.1f} MB, "
        "below the stated ~150 MB ceiling; charts are processed one at a time."
    )
    print()

    anchor_results = tuple(analyze_chart(label, periods) for label, periods in ANCHOR_CHARTS)
    print_result_table("S0 anchors (original (L/2,L,L/2) family):", anchor_results)

    protected = anchor_results[0]
    unprotected = anchor_results[1]
    checks.check(
        "S0 anchor protected L=8 real H_kd_after equals frozen zero",
        abs(protected.hkd_after - FROZEN_PROTECTED_ANCHOR_HKD_AFTER) <= ZERO_TOL,
        (
            f"measured={protected.hkd_after:.16e}, "
            f"frozen={FROZEN_PROTECTED_ANCHOR_HKD_AFTER:.16e}, "
            f"residual={protected.hkd_after - FROZEN_PROTECTED_ANCHOR_HKD_AFTER:.3e}, "
            f"tol={ZERO_TOL:.1e}"
        ),
    )
    checks.check(
        "S0 anchor unprotected L=10 real H_kd_after equals frozen Schur value",
        abs(unprotected.hkd_after - FROZEN_UNPROTECTED_ANCHOR_HKD_AFTER) <= FROZEN_VALUE_TOL,
        (
            f"measured={unprotected.hkd_after:.16e}, "
            f"frozen={FROZEN_UNPROTECTED_ANCHOR_HKD_AFTER:.16e}, "
            f"residual={unprotected.hkd_after - FROZEN_UNPROTECTED_ANCHOR_HKD_AFTER:.3e}, "
            f"tol={FROZEN_VALUE_TOL:.1e}"
        ),
    )
    checks.check(
        "S0 anti-fabrication: real H_kd_before is nonzero before even-d2 truncation",
        min(protected.hkd_before, unprotected.hkd_before) >= FROZEN_BEFORE_MIN,
        (
            f"protected_before={protected.hkd_before:.16e}, "
            f"unprotected_before={unprotected.hkd_before:.16e}, "
            f"frozen_min={FROZEN_BEFORE_MIN:.1f}"
        ),
    )
    print()

    test_results = tuple(analyze_chart(label, periods) for label, periods in TEST_CHARTS)
    print_result_table("S1 fixed mixed-parity general charts:", test_results)

    unique_periods = tuple(sorted({period for _, periods in ANCHOR_CHARTS + TEST_CHARTS for period in periods}))
    axis_lemma_ok = all(period_axis_has_parity_flip(period) == (period % 2 == 1) for period in unique_periods)
    checks.check(
        "S1 per-axis parity lemma on all periods used",
        axis_lemma_ok == FROZEN_EQUIVALENCE_EXPECTED,
        (
            "period flip table: "
            + ", ".join(
                f"q={period}:flip={period_axis_has_parity_flip(period)} expected_odd={period % 2 == 1}"
                for period in unique_periods
            )
        ),
    )

    for result in test_results:
        zero_after = result.hkd_after < ZERO_TOL
        zero_misaligned = result.misaligned_survivors == 0
        three_way = (zero_after == zero_misaligned) and (zero_misaligned == result.all_periods_even)
        checks.check(
            f"S1 three-way coincidence for {result.periods}",
            three_way == FROZEN_EQUIVALENCE_EXPECTED,
            (
                f"(real H_kd_after<{ZERO_TOL:.1e})={zero_after}, "
                f"zero_misaligned={zero_misaligned}, all_periods_even={result.all_periods_even}, "
                f"H_kd_after={result.hkd_after:.16e}, misaligned={result.misaligned_survivors}"
            ),
        )
    print()

    all_even_result = next(result for result in test_results if result.periods == (4, 4, 4))
    one_odd_result = next(result for result in test_results if result.periods == (4, 5, 4))
    print("S2 witnesses:")
    describe_witness("  all-even", all_even_result)
    describe_witness("  one-odd", one_odd_result)
    checks.check(
        "S2 one-odd witness magnitude equals real H_kd_after",
        (
            one_odd_result.witness is not None
            and abs(one_odd_result.witness.magnitude - one_odd_result.hkd_after) <= ZERO_TOL
        )
        == FROZEN_EQUIVALENCE_EXPECTED,
        (
            f"witness_magnitude="
            f"{one_odd_result.witness.magnitude if one_odd_result.witness else 'None'}, "
            f"H_kd_after={one_odd_result.hkd_after:.16e}, tol={ZERO_TOL:.1e}"
        ),
    )

    checks.finish()


if __name__ == "__main__":
    main()
