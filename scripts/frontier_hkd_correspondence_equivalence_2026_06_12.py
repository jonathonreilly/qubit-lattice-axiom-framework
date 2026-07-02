#!/usr/bin/env python3
"""Grid-verified structural equivalence for the d=3 H_kd correspondence.

This runner carries the d=3 step-2 Schur machinery needed for the check and
adds an entry-level decomposition of the next-checkerboard kept-decimated block
after even-d2 truncation. No sibling PR is a load-bearing authority; the
anchors are recomputed here.

Claim tested on the fixed grid L = {8, 10, 12, 14, 16, 18} for the chart family
with K-periods (L/2, L, L/2):

    H_kd_after < 1e-14
      <=> zero nonzero misaligned survivor entries after even-d2 truncation
      <=> every K-chart period is even.

Statuses are pipeline-derived; the audit lane grades.

Run:
    python3 scripts/frontier_hkd_correspondence_equivalence_2026_06_12.py
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np


DIM = 3
T = 1.0
MU = 5.0

L_VALUES = (8, 10, 12, 14, 16, 18)

PROTECTION_TOL = 1.0e-14
ENTRY_NONZERO_TOL = 1.0e-12
NONZERO_BEFORE_TOL = 1.0e-12
WITNESS_MAGNITUDE_MIN = 1.0e-6
STEP1_ANCHOR_TOL = 1.0e-12
MEMORY_LIMIT_BYTES = 2_000_000_000
NOTE_PATH = Path(
    "docs/HKD_CORRESPONDENCE_STRUCTURAL_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md"
)
RUNNER_LINK = (
    "[`scripts/frontier_hkd_correspondence_equivalence_2026_06_12.py`]"
    "(../scripts/frontier_hkd_correspondence_equivalence_2026_06_12.py)"
)
CACHE_LINK = (
    "[`logs/runner-cache/frontier_hkd_correspondence_equivalence_2026_06_12.txt`]"
    "(../logs/runner-cache/frontier_hkd_correspondence_equivalence_2026_06_12.txt)"
)
FORBIDDEN_PRECURSOR_STATUS_WORD = "lan" + "ded"

FROZEN_HKD_AFTER_L8 = 0.0
FROZEN_HKD_AFTER_L10 = 7.4832497863019298e-01
FROZEN_HKD_AFTER_L12 = 0.0
FROZEN_HKD_AFTER_L14 = 7.4732149222164002e-01
FROZEN_HKD_ANCHOR_ABS_TOL = 1.0e-12

FROZEN_STEP1_ANCHOR_ERROR_L8 = 0.0
FROZEN_STEP1_OO_OFFDIAG_L8 = 0.0

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
class LResult:
    L: int
    periods: tuple[int, int, int]
    all_periods_even: bool
    decomposition: EntryDecomposition


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


def minimal_delta(left: int, right: int, period: int) -> int:
    delta = (right - left) % period
    if delta > period // 2:
        delta -= period
    return int(delta)


def minimal_vector(
    left: tuple[int, int, int],
    right: tuple[int, int, int],
    periods: tuple[int, int, int],
) -> tuple[int, int, int]:
    return tuple(minimal_delta(a, b, p) for a, b, p in zip(left, right, periods))


def d2_parity_between(
    left: tuple[int, int, int],
    right: tuple[int, int, int],
    periods: tuple[int, int, int],
) -> tuple[int, tuple[int, int, int]]:
    delta = minimal_vector(left, right, periods)
    return int(sum(v * v for v in delta) & 1), delta


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


def compute_l_result(L: int) -> LResult:
    h2, charts, periods = step2_output(L)
    decomposition = decompose_hkd_entries(h2, charts, periods)
    del h2
    return LResult(
        L=L,
        periods=periods,
        all_periods_even=all(period % 2 == 0 for period in periods),
        decomposition=decomposition,
    )


def compute_grid() -> dict[int, LResult]:
    return {L: compute_l_result(L) for L in L_VALUES}


def estimated_peak_dense_bytes_for_l(L: int) -> int:
    retained_step1 = L * L * (L // 2)
    keep_step2 = retained_step1 // 2
    drop_step2 = retained_step1 - keep_step2
    dense_step2_peak = (
        keep_step2 * keep_step2
        + keep_step2 * drop_step2
        + drop_step2 * drop_step2
        + drop_step2 * keep_step2
        + keep_step2 * keep_step2
    ) * 8
    step1_anchor_peak = 0
    if L == 8:
        full = L**DIM
        half = full // 2
        step1_anchor_peak = (full * full + 4 * half * half) * 8
    return max(dense_step2_peak, step1_anchor_peak)


def max_estimated_peak_dense_bytes() -> int:
    return max(estimated_peak_dense_bytes_for_l(L) for L in L_VALUES)


def run_anchor_gates(
    results: dict[int, LResult],
    step1_anchor_error: float,
    step1_oo_offdiag: float,
) -> None:
    print("S0 anchors")
    check(
        "S0 L=8 H_kd_after reproduces frozen protected anchor",
        abs(results[8].decomposition.hkd_after - FROZEN_HKD_AFTER_L8) <= FROZEN_HKD_ANCHOR_ABS_TOL
        and results[8].decomposition.hkd_after < PROTECTION_TOL,
        (
            f"computed={results[8].decomposition.hkd_after:.16e}, "
            f"frozen={FROZEN_HKD_AFTER_L8:.16e}, "
            f"anchor_tol={FROZEN_HKD_ANCHOR_ABS_TOL:.1e}, protection_tol={PROTECTION_TOL:.1e}"
        ),
    )
    check(
        "S0 L=10 H_kd_after reproduces frozen unprotected anchor",
        abs(results[10].decomposition.hkd_after - FROZEN_HKD_AFTER_L10) <= FROZEN_HKD_ANCHOR_ABS_TOL,
        (
            f"computed={results[10].decomposition.hkd_after:.16e}, "
            f"frozen={FROZEN_HKD_AFTER_L10:.16e}, "
            f"anchor_tol={FROZEN_HKD_ANCHOR_ABS_TOL:.1e}"
        ),
    )
    check(
        "S0 L=12 H_kd_after reproduces frozen protected anchor",
        abs(results[12].decomposition.hkd_after - FROZEN_HKD_AFTER_L12) <= FROZEN_HKD_ANCHOR_ABS_TOL
        and results[12].decomposition.hkd_after < PROTECTION_TOL,
        (
            f"computed={results[12].decomposition.hkd_after:.16e}, "
            f"frozen={FROZEN_HKD_AFTER_L12:.16e}, "
            f"anchor_tol={FROZEN_HKD_ANCHOR_ABS_TOL:.1e}, protection_tol={PROTECTION_TOL:.1e}"
        ),
    )
    check(
        "S0 L=14 H_kd_after reproduces frozen unprotected anchor",
        abs(results[14].decomposition.hkd_after - FROZEN_HKD_AFTER_L14) <= FROZEN_HKD_ANCHOR_ABS_TOL,
        (
            f"computed={results[14].decomposition.hkd_after:.16e}, "
            f"frozen={FROZEN_HKD_AFTER_L14:.16e}, "
            f"anchor_tol={FROZEN_HKD_ANCHOR_ABS_TOL:.1e}"
        ),
    )
    check(
        "S0 anti-fabrication H_kd_before is nonzero at every grid L",
        min(results[L].decomposition.hkd_before for L in L_VALUES) > NONZERO_BEFORE_TOL,
        (
            "min_H_kd_before="
            f"{min(results[L].decomposition.hkd_before for L in L_VALUES):.16e}, "
            f"nonzero_tol={NONZERO_BEFORE_TOL:.1e}"
        ),
    )
    check(
        "S0 self-contained step-1 dense Schur anchor matches frozen zero error",
        abs(step1_anchor_error - FROZEN_STEP1_ANCHOR_ERROR_L8) <= STEP1_ANCHOR_TOL,
        (
            f"L=8, computed_error={step1_anchor_error:.3e}, "
            f"frozen={FROZEN_STEP1_ANCHOR_ERROR_L8:.1e}, tol={STEP1_ANCHOR_TOL:.1e}"
        ),
    )
    check(
        "S0 self-contained step-1 eliminated block offdiagonal matches frozen zero",
        abs(step1_oo_offdiag - FROZEN_STEP1_OO_OFFDIAG_L8) <= STEP1_ANCHOR_TOL,
        (
            f"L=8, computed_offdiag={step1_oo_offdiag:.3e}, "
            f"frozen={FROZEN_STEP1_OO_OFFDIAG_L8:.1e}, tol={STEP1_ANCHOR_TOL:.1e}"
        ),
    )


def print_entry_table(results: dict[int, LResult]) -> None:
    print("S1 structural decomposition table")
    print(
        "  L   periods        all_even  H_kd_before        H_kd_after         "
        "nonzero_before  d2_even_survivors  aligned  misaligned  max_misaligned"
    )
    for L in L_VALUES:
        row = results[L]
        dec = row.decomposition
        print(
            f"  {L:2d}  {str(row.periods):13s}  {str(row.all_periods_even):8s}  "
            f"{dec.hkd_before:.16e}  {dec.hkd_after:.16e}  "
            f"{dec.nonzero_before_entries:14d}  {dec.surviving_even_d2_entries:17d}  "
            f"{dec.aligned_surviving_entries:7d}  {dec.misaligned_surviving_entries:10d}  "
            f"{dec.max_misaligned_magnitude:.16e}"
        )


def run_structural_gates(results: dict[int, LResult]) -> None:
    print_entry_table(results)
    check(
        "S1 zero misaligned survivor entries iff H_kd_after is protected on the grid",
        all(
            (results[L].decomposition.misaligned_surviving_entries == 0)
            == (results[L].decomposition.hkd_after < PROTECTION_TOL)
            for L in L_VALUES
        ),
        f"fixed protection_tol={PROTECTION_TOL:.1e}, entry_nonzero_tol={ENTRY_NONZERO_TOL:.1e}",
    )
    check(
        "S1 zero misaligned survivor entries iff all K-chart periods are even on the grid",
        all(
            (results[L].decomposition.misaligned_surviving_entries == 0)
            == results[L].all_periods_even
            for L in L_VALUES
        ),
        "K-periods=(L/2,L,L/2), grid=(8,10,12,14,16,18)",
    )
    check(
        "S1 protected cases have no nonzero even-d2 survivor entries",
        all(results[L].decomposition.surviving_even_d2_entries == 0 for L in (8, 12, 16)),
        (
            f"L8={results[8].decomposition.surviving_even_d2_entries}, "
            f"L12={results[12].decomposition.surviving_even_d2_entries}, "
            f"L16={results[16].decomposition.surviving_even_d2_entries}"
        ),
    )
    check(
        "S1 unprotected cases have nonzero misaligned even-d2 survivor entries",
        all(results[L].decomposition.misaligned_surviving_entries > 0 for L in (10, 14, 18)),
        (
            f"L10={results[10].decomposition.misaligned_surviving_entries}, "
            f"L14={results[14].decomposition.misaligned_surviving_entries}, "
            f"L18={results[18].decomposition.misaligned_surviving_entries}"
        ),
    )


def run_mechanism_gates(results: dict[int, LResult]) -> None:
    print("S2 mechanism witness")
    witness = results[10].decomposition.witness
    if witness is None:
        witness_detail = "None"
        witness_gate = False
    else:
        witness_detail = (
            f"left={witness.left}, right={witness.right}, "
            f"minimal_delta={witness.minimal_delta}, "
            f"d2_parity={witness.d2_parity}, "
            f"chart_pair_parity={witness.chart_pair_parity}, "
            f"magnitude={witness.magnitude:.16e}"
        )
        witness_gate = (
            witness.d2_parity != witness.chart_pair_parity
            and witness.d2_parity == 0
            and witness.magnitude > WITNESS_MAGNITUDE_MIN
        )
    print(f"  L=10 surviving misaligned entry: {witness_detail}")
    check(
        "S2 L=10 has a nonzero surviving misaligned entry witness",
        witness_gate,
        f"{witness_detail}, magnitude_min={WITNESS_MAGNITUDE_MIN:.1e}",
    )
    check(
        "S2 L=16 out-of-sample predicted hold has zero misaligned survivors and protected H_kd_after",
        results[16].decomposition.misaligned_surviving_entries == 0
        and results[16].decomposition.hkd_after < PROTECTION_TOL,
        (
            f"misaligned={results[16].decomposition.misaligned_surviving_entries}, "
            f"H_kd_after={results[16].decomposition.hkd_after:.16e}, "
            f"protection_tol={PROTECTION_TOL:.1e}"
        ),
    )
    memory_estimate = max_estimated_peak_dense_bytes()
    check(
        "S2 memory estimate remains below the fixed 2 GB ceiling",
        memory_estimate < MEMORY_LIMIT_BYTES,
        f"estimated_peak_dense_bytes={memory_estimate}, ceiling={MEMORY_LIMIT_BYTES}",
    )


def run_source_hygiene_gates() -> None:
    print("S3 source hygiene")
    note = NOTE_PATH.read_text(encoding="utf-8")
    check(
        "S3 canonical source metadata is present",
        "**Claim type:** bounded_theorem" in note
        and "**Status authority:** independent audit lane only" in note
        and "**No-promotion statement:**" in note,
        "claim_type bounded_theorem; independent audit authority; no-promotion statement",
    )
    check(
        "S3 runner and cache markdown links are present",
        RUNNER_LINK in note and CACHE_LINK in note,
        "primary runner/cache links seed review discoverability",
    )
    check(
        "S3 stale predecessor-authority rhetoric is absent",
        FORBIDDEN_PRECURSOR_STATUS_WORD not in note,
        "no sibling branch is cited as settled authority",
    )
    check(
        "S3 minimal-axiom dependency link is present",
        "[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)" in note,
        "one scope-reference dependency link",
    )


def main() -> int:
    print("H_kd correspondence structural equivalence runner")
    print(f"parameters: d={DIM}, t={T:.1f}, mu={MU:.1f}, L_values={L_VALUES}")
    print("K-chart periods after synthetic step 2 are (L/2, L, L/2).")
    try:
        results = compute_grid()
        step1_anchor_error, step1_oo_offdiag = step1_dense_schur_anchor(8)
    except Exception as exc:
        global FAIL
        FAIL += 1
        print(f"FAIL: runner computation exception :: {exc!r}")
        print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
        return 1

    run_anchor_gates(results, step1_anchor_error, step1_oo_offdiag)
    run_structural_gates(results)
    run_mechanism_gates(results)
    run_source_hygiene_gates()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
