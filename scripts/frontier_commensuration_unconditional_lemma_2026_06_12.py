#!/usr/bin/env python3
"""Finite-dimensional verification runner for

    docs/COMMENSURATION_UNCONDITIONAL_PERIOD_PARITY_LEMMA_NARROW_THEOREM_NOTE_2026-06-12.md

This runner checks the elementary period-parity lemma under the centered
minimal_delta convention used in the d=3 step-2 chart family: ties at
period/2 stay on the positive side.

Run:
    python3 scripts/frontier_commensuration_unconditional_lemma_2026_06_12.py
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import product
import sys

import sympy as sp


PASS = 0
FAIL = 0

EVEN_Q_NUMERIC_SET = tuple(range(2, 101, 2))
ODD_Q_NUMERIC_SET = tuple(range(3, 100, 2))
ASSEMBLY_L_VALUES = (8, 10, 12, 16, 18, 26)

FROZEN_EVEN_NUMERIC_CASES = 2550
FROZEN_ODD_NUMERIC_CASES = 2499
FROZEN_ZERO_FAILURES = 0
FROZEN_Q99_FLIP_PROFILE = (50, 98, 49)

FROZEN_EVEN_SYMBOLIC_ROWS = (
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 0),
)
FROZEN_ODD_SYMBOLIC_ROWS = (
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 1, 1),
)
FROZEN_ODD_WITNESS_SYMBOLIC = ("1", "-m", "1")

FROZEN_PR3798_L10_MISMATCH_COUNT = 5700
FROZEN_PR3798_L26_MISMATCH_COUNT = 1802892
FROZEN_PR3798_MISMATCH_COUNTS = (
    (8, 0),
    (10, 5700),
    (12, 0),
    (16, 0),
    (18, 197640),
    (26, 1802892),
)
FROZEN_L10_WITNESS = ((0, 0, 0), (0, 0, 3), (0, 0, -2), 0, 1)
FROZEN_L10_WITNESS_D2_NORM = 4
FROZEN_L10_WITNESS_FLIP_BIT = 1
FROZEN_ASSEMBLY_IFF_DISAGREEMENTS = 0
FROZEN_PROTECTED_SELECTED_MISMATCH_TOTAL = 0
FROZEN_UNPROTECTED_SELECTED_EMPTY_FAILURES = 0


@dataclass(frozen=True)
class AxisNumericSummary:
    even_cases: int
    odd_cases: int
    reduction_failures: int
    even_qk_odd_cases: int
    even_parity_failures: int
    odd_flip_rule_failures: int
    odd_flip_set_mismatch_q: int
    odd_empty_flip_set_q: int
    odd_witness_failures: int
    q99_flip_profile: tuple[int, int, int]


@dataclass(frozen=True)
class SymbolicSummary:
    even_rows: tuple[tuple[int, int, int], ...]
    odd_rows: tuple[tuple[int, int, int], ...]
    odd_witness: tuple[str, str, str]


@dataclass(frozen=True)
class AssemblyCheck:
    L: int
    periods: tuple[int, int, int]
    per_axis_predicts_holds: bool
    mismatch_count: int
    first_mismatch: tuple[
        tuple[int, int, int],
        tuple[int, int, int],
        tuple[int, int, int],
        int,
        int,
    ] | None


def check(label: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS: {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {label} :: {detail}")


def minimal_delta(left: int, right: int, period: int) -> int:
    """Centered representative convention; ties stay on the positive side."""
    delta = (right - left) % period
    if delta > period // 2:
        delta -= period
    return int(delta)


def minimal_residue_delta(residue: int, period: int) -> int:
    return minimal_delta(0, residue, period)


def centered_round_for_residue(residue: int, period: int) -> int:
    return 1 if 2 * residue > period else 0


def chart_parity(chart: tuple[int, int, int]) -> int:
    return int(sum(chart) & 1)


def minimal_vector(
    left: tuple[int, int, int],
    right: tuple[int, int, int],
    periods: tuple[int, int, int],
) -> tuple[int, int, int]:
    return tuple(minimal_delta(a, b, q) for a, b, q in zip(left, right, periods))


def k_chart_sites(L: int) -> list[tuple[int, int, int]]:
    return [(a, b, c) for a in range(L // 2) for b in range(L) for c in range(L // 2)]


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


def coordinate_pair_table(period: int) -> dict[tuple[int, int, int], int]:
    counts: dict[tuple[int, int, int], int] = defaultdict(int)
    for left in range(period):
        for right in range(period):
            delta = minimal_delta(left, right, period)
            counts[(left & 1, right & 1, (delta * delta) & 1)] += 1
    return dict(counts)


def full_coset_mismatch_count(L: int) -> int:
    periods = (L // 2, L, L // 2)
    state: dict[tuple[int, int, int], int] = {(0, 0, 0): 1}
    for period in periods:
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
    return state.get((0, 1, 0), 0)


def compute_assembly_checks() -> tuple[AssemblyCheck, ...]:
    checks: list[AssemblyCheck] = []
    for L in ASSEMBLY_L_VALUES:
        periods = (L // 2, L, L // 2)
        mismatch_count = full_coset_mismatch_count(L)
        checks.append(
            AssemblyCheck(
                L=L,
                periods=periods,
                per_axis_predicts_holds=all(period % 2 == 0 for period in periods),
                mismatch_count=mismatch_count,
                first_mismatch=first_mismatch(L, periods) if mismatch_count else None,
            )
        )
    return tuple(checks)


def symbolic_axis_summary() -> SymbolicSummary:
    m = sp.symbols("m", integer=True, nonnegative=True)
    a_parity = sp.symbols("a_parity", integer=True)

    even_rows: list[tuple[int, int, int]] = []
    for apar, kpar in product((0, 1), repeat=2):
        expr = sp.Mod((a_parity + apar - (2 * m) * kpar) - (a_parity + apar), 2)
        even_rows.append((apar, kpar, int(sp.simplify(expr))))

    odd_rows: list[tuple[int, int, int]] = []
    for apar, kpar in product((0, 1), repeat=2):
        expr = sp.Mod((a_parity + apar - (2 * m + 1) * kpar) - (a_parity + apar), 2)
        odd_rows.append((apar, kpar, int(sp.simplify(expr))))

    odd_q = 2 * m + 1
    witness_a = m + 1
    witness_round_margin = sp.simplify(2 * witness_a - odd_q)
    witness_delta = sp.simplify(witness_a - odd_q)
    witness_flip = sp.simplify(sp.Mod(witness_delta - witness_a, 2))

    return SymbolicSummary(
        even_rows=tuple(even_rows),
        odd_rows=tuple(odd_rows),
        odd_witness=(str(witness_round_margin), str(witness_delta), str(witness_flip)),
    )


def numeric_axis_summary() -> AxisNumericSummary:
    even_cases = 0
    odd_cases = 0
    reduction_failures = 0
    even_qk_odd_cases = 0
    even_parity_failures = 0
    odd_flip_rule_failures = 0
    odd_flip_set_mismatch_q = 0
    odd_empty_flip_set_q = 0
    odd_witness_failures = 0
    q99_flip_set: tuple[int, ...] = ()

    for q in EVEN_Q_NUMERIC_SET:
        for a in range(q):
            even_cases += 1
            delta = minimal_residue_delta(a, q)
            k = centered_round_for_residue(a, q)
            if delta != a - q * k:
                reduction_failures += 1
            if (q * k) & 1:
                even_qk_odd_cases += 1
            if (delta - a) & 1:
                even_parity_failures += 1

    for q in ODD_Q_NUMERIC_SET:
        flip_set: list[int] = []
        round_odd_set: list[int] = []
        for a in range(q):
            odd_cases += 1
            delta = minimal_residue_delta(a, q)
            k = centered_round_for_residue(a, q)
            if delta != a - q * k:
                reduction_failures += 1
            flip = (delta - a) & 1
            expected_flip = k & 1
            if flip != expected_flip:
                odd_flip_rule_failures += 1
            if flip:
                flip_set.append(a)
            if expected_flip:
                round_odd_set.append(a)

        if not flip_set:
            odd_empty_flip_set_q += 1
        if tuple(flip_set) != tuple(round_odd_set):
            odd_flip_set_mismatch_q += 1

        witness = (q + 1) // 2
        witness_delta = minimal_residue_delta(witness, q)
        witness_k = centered_round_for_residue(witness, q)
        if witness_k != 1 or ((witness_delta - witness) & 1) != 1:
            odd_witness_failures += 1
        if q == 99:
            q99_flip_set = tuple(flip_set)

    q99_profile = (
        q99_flip_set[0] if q99_flip_set else -1,
        q99_flip_set[-1] if q99_flip_set else -1,
        len(q99_flip_set),
    )
    return AxisNumericSummary(
        even_cases=even_cases,
        odd_cases=odd_cases,
        reduction_failures=reduction_failures,
        even_qk_odd_cases=even_qk_odd_cases,
        even_parity_failures=even_parity_failures,
        odd_flip_rule_failures=odd_flip_rule_failures,
        odd_flip_set_mismatch_q=odd_flip_set_mismatch_q,
        odd_empty_flip_set_q=odd_empty_flip_set_q,
        odd_witness_failures=odd_witness_failures,
        q99_flip_profile=q99_profile,
    )


def run_anchor_gates(assembly_checks: tuple[AssemblyCheck, ...]) -> None:
    print("A. frozen full-coset anchors first")
    l10 = next(row for row in assembly_checks if row.L == 10)
    l26 = next(row for row in assembly_checks if row.L == 26)
    check(
        "anchor L=10 mismatch count reproduces frozen copy",
        l10.mismatch_count == FROZEN_PR3798_L10_MISMATCH_COUNT,
        f"computed={l10.mismatch_count}, frozen={FROZEN_PR3798_L10_MISMATCH_COUNT}",
    )
    check(
        "anchor L=26 mismatch count reproduces frozen copy",
        l26.mismatch_count == FROZEN_PR3798_L26_MISMATCH_COUNT,
        f"computed={l26.mismatch_count}, frozen={FROZEN_PR3798_L26_MISMATCH_COUNT}",
    )

    observed_counts = tuple((row.L, row.mismatch_count) for row in assembly_checks)
    check(
        "selected mismatch counts reproduce frozen copies",
        observed_counts == FROZEN_PR3798_MISMATCH_COUNTS,
        f"observed={observed_counts}",
    )

    witness = l10.first_mismatch
    witness_d2_norm = -1 if witness is None else sum(v * v for v in witness[2])
    witness_flip_bit = -1 if witness is None else witness[3] ^ witness[4]
    print(
        "  L=10 witness: "
        f"left={None if witness is None else witness[0]}, "
        f"right={None if witness is None else witness[1]}, "
        f"minimal_vector={None if witness is None else witness[2]}, "
        f"d2_parity={None if witness is None else witness[3]}, "
        f"chart_delta_parity={None if witness is None else witness[4]}"
    )
    check(
        "anti-fabrication L=10 witness coset parity flip is frozen",
        witness == FROZEN_L10_WITNESS
        and witness_d2_norm == FROZEN_L10_WITNESS_D2_NORM
        and witness_flip_bit == FROZEN_L10_WITNESS_FLIP_BIT,
        f"witness={witness}, d2_norm={witness_d2_norm}, flip_bit={witness_flip_bit}",
    )


def run_axis_gates(symbolic: SymbolicSummary, numeric: AxisNumericSummary) -> None:
    print("B. per-axis reduction gates")
    check(
        "SymPy even-q residue classes preserve parity",
        symbolic.even_rows == FROZEN_EVEN_SYMBOLIC_ROWS,
        f"rows={symbolic.even_rows}",
    )
    check(
        "SymPy odd-q residue classes flip exactly on odd k",
        symbolic.odd_rows == FROZEN_ODD_SYMBOLIC_ROWS,
        f"rows={symbolic.odd_rows}",
    )
    check(
        "SymPy odd witness has centered round k=1 and flips parity",
        symbolic.odd_witness == FROZEN_ODD_WITNESS_SYMBOLIC,
        f"(round_margin, delta, flip)={symbolic.odd_witness}",
    )
    check(
        "numeric even-q sweep covers the frozen case count",
        numeric.even_cases == FROZEN_EVEN_NUMERIC_CASES,
        f"cases={numeric.even_cases}",
    )
    check(
        "numeric odd-q sweep covers the frozen case count",
        numeric.odd_cases == FROZEN_ODD_NUMERIC_CASES,
        f"cases={numeric.odd_cases}",
    )
    check(
        "centered delta equals a - q*k for every swept residue",
        numeric.reduction_failures == FROZEN_ZERO_FAILURES,
        f"failures={numeric.reduction_failures}",
    )
    # q=1 degenerate guard: with period 1 there is a SINGLE residue class
    # (a in {0}), minimal delta is identically 0, so parity is vacuously
    # preserved despite q being odd.  The "odd q flips parity" branch needs a
    # non-trivial residue (a witness with k odd), which requires q >= 3.  The
    # criterion is therefore stated for q_i >= 2; the chart family (L/2, L, L/2)
    # with even L >= 4 always has periods >= 2, so q=1 never arises in scope.
    q1_deltas = tuple(minimal_delta(a, 0, 1) for a in range(-3, 4))
    q1_all_zero = all(d == 0 for d in q1_deltas)
    check(
        "q=1 degenerate guard: period-1 axis has the single trivial coset "
        "(delta == 0), parity vacuously preserved; criterion scoped to q_i >= 2",
        q1_all_zero,
        f"q1_deltas={q1_deltas}",
    )
    check(
        "even q has no odd q*k branch and no parity failures",
        numeric.even_qk_odd_cases == FROZEN_ZERO_FAILURES
        and numeric.even_parity_failures == FROZEN_ZERO_FAILURES,
        (
            f"qk_odd={numeric.even_qk_odd_cases}, "
            f"parity_failures={numeric.even_parity_failures}"
        ),
    )
    check(
        "odd q flip set matches centered odd-k round set and is nonempty",
        numeric.odd_flip_rule_failures == FROZEN_ZERO_FAILURES
        and numeric.odd_flip_set_mismatch_q == FROZEN_ZERO_FAILURES
        and numeric.odd_empty_flip_set_q == FROZEN_ZERO_FAILURES,
        (
            f"rule_failures={numeric.odd_flip_rule_failures}, "
            f"set_mismatch_q={numeric.odd_flip_set_mismatch_q}, "
            f"empty_flip_q={numeric.odd_empty_flip_set_q}"
        ),
    )
    check(
        "odd q witness a=(q+1)/2 succeeds for every swept odd q",
        numeric.odd_witness_failures == FROZEN_ZERO_FAILURES,
        f"witness_failures={numeric.odd_witness_failures}",
    )
    check(
        "q=99 flip profile is the frozen high-half odd-k profile",
        numeric.q99_flip_profile == FROZEN_Q99_FLIP_PROFILE,
        f"profile={numeric.q99_flip_profile}",
    )


def run_assembly_gates(assembly_checks: tuple[AssemblyCheck, ...]) -> None:
    print("C. assembled chart-family gates")
    for row in assembly_checks:
        print(
            f"  L={row.L:2d} periods={row.periods} "
            f"per_axis_predicts_holds={row.per_axis_predicts_holds} "
            f"mismatches={row.mismatch_count} first_mismatch={row.first_mismatch}"
        )

    iff_disagreements = sum(
        (row.mismatch_count == 0) != row.per_axis_predicts_holds for row in assembly_checks
    )
    protected_mismatch_total = sum(
        row.mismatch_count for row in assembly_checks if row.per_axis_predicts_holds
    )
    unprotected_empty_failures = sum(
        row.mismatch_count == 0 for row in assembly_checks if not row.per_axis_predicts_holds
    )

    check(
        "full-coset checks agree exactly with per-axis iff prediction",
        iff_disagreements == FROZEN_ASSEMBLY_IFF_DISAGREEMENTS,
        f"iff_disagreements={iff_disagreements}",
    )
    check(
        "selected all-even-period charts have zero full-coset mismatches",
        protected_mismatch_total == FROZEN_PROTECTED_SELECTED_MISMATCH_TOTAL,
        f"protected_mismatch_total={protected_mismatch_total}",
    )
    check(
        "selected odd-period charts all have a nonempty failure set",
        unprotected_empty_failures == FROZEN_UNPROTECTED_SELECTED_EMPTY_FAILURES,
        f"unprotected_empty_failures={unprotected_empty_failures}",
    )


def main() -> int:
    print("commensuration unconditional period-parity lemma runner")
    print(f"even_q_numeric_set={EVEN_Q_NUMERIC_SET}")
    print(f"odd_q_numeric_set={ODD_Q_NUMERIC_SET}")
    print(f"assembly_L_values={ASSEMBLY_L_VALUES}")
    try:
        assembly_checks = compute_assembly_checks()
        run_anchor_gates(assembly_checks)

        symbolic = symbolic_axis_summary()
        numeric = numeric_axis_summary()
        run_axis_gates(symbolic, numeric)
        run_assembly_gates(assembly_checks)
    except Exception as exc:
        global FAIL
        FAIL += 1
        print(f"FAIL: runner exception :: {exc!r}")

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
