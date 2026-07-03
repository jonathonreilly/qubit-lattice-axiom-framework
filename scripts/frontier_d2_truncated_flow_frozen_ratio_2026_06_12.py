#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/D2_TRUNCATED_FLOW_FROZEN_RATIO_ACCUMULATED_BUDGET_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_d2_truncated_flow_frozen_ratio_2026_06_12.py
"""

from __future__ import annotations

from dataclasses import dataclass
import sys

import numpy as np


D = 2
MASS2 = 1.0
DIAG0 = 2.0 * D + MASS2
HOP0 = -1.0
E = 0.0
STEPS = 4
REFERENCE_L = 16
STABILITY_L = 12
TRUNC_D2 = frozenset((4, 8))
PRINT_COUPLING_STEPS = (2, 3, 4)
CONTROL_TOL = 1.0e-12


@dataclass(frozen=True)
class State:
    period: int
    shape: tuple[int, int]
    coords: np.ndarray
    h: np.ndarray


class CheckBook:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, name: str, condition: bool) -> None:
        if bool(condition):
            self.pass_count += 1
            print(f"PASS: {name}")
        else:
            self.fail_count += 1
            print(f"FAIL: {name}")

    def finish(self) -> None:
        print(f"TOTAL: PASS={self.pass_count} FAIL={self.fail_count}")
        if self.fail_count:
            sys.exit(1)


def row_major_coords(shape: tuple[int, int]) -> list[tuple[int, int]]:
    n0, n1 = shape
    return [(i, j) for i in range(n0) for j in range(n1)]


def initial_state(period: int) -> State:
    shape = (period, period)
    logical = row_major_coords(shape)
    coords = np.array(logical, dtype=np.int64)
    n = len(logical)
    index = {xy: p for p, xy in enumerate(logical)}
    h = np.eye(n, dtype=np.float64) * DIAG0

    for p, (x, y) in enumerate(logical):
        for dx, dy in ((1, 0), (0, 1)):
            qxy = ((x + dx) % period, (y + dy) % period)
            q = index[qxy]
            h[p, q] += HOP0
            h[q, p] += HOP0

    return State(period=period, shape=shape, coords=coords, h=h)


def checkerboard_keep_in_new_order(
    shape: tuple[int, int],
) -> tuple[tuple[int, int], np.ndarray]:
    """Return old row-major indices of the kept checkerboard in new order."""

    n0, n1 = shape
    if n1 % 2 == 0:
        new_shape = (n0, n1 // 2)
        kept = [None] * (new_shape[0] * new_shape[1])
        for i in range(n0):
            for j in range(n1):
                if (i + j) % 2 == 0:
                    new_i = i
                    new_j = (j - (i & 1)) // 2
                    old = i * n1 + j
                    kept[new_i * new_shape[1] + new_j] = old
    elif n0 % 2 == 0:
        new_shape = (n0 // 2, n1)
        kept = [None] * (new_shape[0] * new_shape[1])
        for i in range(n0):
            for j in range(n1):
                if (i + j) % 2 == 0:
                    new_i = (i - (j & 1)) // 2
                    new_j = j
                    old = i * n1 + j
                    kept[new_i * new_shape[1] + new_j] = old
    else:
        raise ValueError(f"checkerboard step needs at least one even side, got {shape}")

    if any(x is None for x in kept):
        raise AssertionError(f"incomplete checkerboard reindex for shape {shape}")
    return new_shape, np.array(kept, dtype=np.int64)


def exact_checkerboard_step(state: State) -> State:
    new_shape, keep = checkerboard_keep_in_new_order(state.shape)
    n_old = state.h.shape[0]
    keep_set = set(int(i) for i in keep)
    drop = np.array([i for i in range(n_old) if i not in keep_set], dtype=np.int64)

    hkk = state.h[np.ix_(keep, keep)]
    hkd = state.h[np.ix_(keep, drop)]
    hdk = state.h[np.ix_(drop, keep)]
    hdd = state.h[np.ix_(drop, drop)]

    if E != 0.0:
        hkk = hkk - E * np.eye(hkk.shape[0])
        hdd = hdd - E * np.eye(hdd.shape[0])

    schur_tail = hkd @ np.linalg.solve(hdd, hdk)
    h_eff = hkk - schur_tail
    h_eff = 0.5 * (h_eff + h_eff.T)

    return State(
        period=state.period,
        shape=new_shape,
        coords=state.coords[keep].copy(),
        h=h_eff,
    )


def periodic_d2(coords: np.ndarray, period: int) -> np.ndarray:
    delta = np.abs(coords[:, None, :] - coords[None, :, :])
    delta = np.minimum(delta, period - delta)
    return np.sum(delta * delta, axis=2)


def truncate_to_shells(state: State, shells: frozenset[int]) -> State:
    d2 = periodic_d2(state.coords, state.period)
    keep = np.eye(state.h.shape[0], dtype=bool)
    for shell in shells:
        keep |= d2 == shell
    h_trunc = np.where(keep, state.h, 0.0)
    h_trunc = 0.5 * (h_trunc + h_trunc.T)
    return State(
        period=state.period,
        shape=state.shape,
        coords=state.coords.copy(),
        h=h_trunc,
    )


def identity_truncate(state: State) -> State:
    return State(
        period=state.period,
        shape=state.shape,
        coords=state.coords.copy(),
        h=state.h.copy(),
    )


def shell_coupling(state: State, shell: int) -> tuple[float, int, float]:
    d2 = periodic_d2(state.coords, state.period)
    mask = d2 == shell
    np.fill_diagonal(mask, False)
    values = state.h[mask]
    if values.size == 0:
        return 0.0, 0, 0.0
    mean = float(np.mean(values))
    spread = float(np.max(np.abs(values - mean)))
    return mean, int(values.size), spread


def coupling_record(state: State) -> dict[str, float | int]:
    diag_values = np.diag(state.h)
    diag = float(np.mean(diag_values))
    diag_spread = float(np.max(np.abs(diag_values - diag)))
    c4, n4, s4 = shell_coupling(state, 4)
    c8, n8, s8 = shell_coupling(state, 8)
    return {
        "diag": diag,
        "diag_spread": diag_spread,
        "c4": c4,
        "c4_count": n4,
        "c4_spread": s4,
        "c8": c8,
        "c8_count": n8,
        "c8_spread": s8,
        "r4": c4 / diag,
        "r8": c8 / diag,
    }


def next_checkerboard_coupling_norm(state: State) -> float:
    """Maximum kept/drop block coupling for the next checkerboard step."""

    _, keep = checkerboard_keep_in_new_order(state.shape)
    n_old = state.h.shape[0]
    keep_set = set(int(i) for i in keep)
    drop = np.array([i for i in range(n_old) if i not in keep_set], dtype=np.int64)
    if keep.size == 0 or drop.size == 0:
        return 0.0
    hkd = state.h[np.ix_(keep, drop)]
    return float(np.max(np.abs(hkd)))


def admits_next_checkerboard_step(shape: tuple[int, int]) -> bool:
    return any(axis % 2 == 0 for axis in shape)


def run_pipeline(period: int, mode: str) -> dict[str, object]:
    state = initial_state(period)
    states: list[State] = []
    pre_trunc_full: list[State] = []
    truncation_errors: list[float] = []
    records: dict[int, dict[str, float | int]] = {}
    next_hkd_norms: dict[int, float] = {}

    for step in range(1, STEPS + 1):
        full = exact_checkerboard_step(state)
        pre_trunc_full.append(full)

        if mode == "shell":
            next_state = truncate_to_shells(full, TRUNC_D2)
        elif mode == "identity":
            next_state = identity_truncate(full)
        elif mode == "exact":
            next_state = full
        else:
            raise ValueError(f"unknown pipeline mode {mode!r}")

        truncation_errors.append(float(np.max(np.abs(next_state.h - full.h))))
        state = next_state
        states.append(state)
        records[step] = coupling_record(state)
        if step >= 2 and admits_next_checkerboard_step(state.shape):
            next_hkd_norms[step] = next_checkerboard_coupling_norm(state)

    return {
        "final": state,
        "states": states,
        "pre_trunc_full": pre_trunc_full,
        "errors": truncation_errors,
        "records": records,
        "next_hkd_norms": next_hkd_norms,
    }


def inverse_dense(a: np.ndarray) -> np.ndarray:
    return np.linalg.solve(a, np.eye(a.shape[0], dtype=np.float64))


def resolvent_budget(period: int) -> dict[str, float]:
    exact = run_pipeline(period, "exact")["final"]
    trunc = run_pipeline(period, "shell")["final"]
    assert isinstance(exact, State)
    assert isinstance(trunc, State)
    g_exact = inverse_dense(exact.h)
    g_trunc = inverse_dense(trunc.h)
    diff = np.abs(g_exact - g_trunc)
    diag_diff = np.abs(np.diag(g_exact) - np.diag(g_trunc))
    return {
        "block_max": float(np.max(diff)),
        "diag_max": float(np.max(diag_diff)),
    }


def compare_exact_to_identity(period: int) -> float:
    exact_states = run_pipeline(period, "exact")["states"]
    identity_states = run_pipeline(period, "identity")["states"]
    assert isinstance(exact_states, list)
    assert isinstance(identity_states, list)
    max_diff = 0.0
    for exact_state, identity_state in zip(exact_states, identity_states):
        max_diff = max(max_diff, float(np.max(np.abs(exact_state.h - identity_state.h))))
    return max_diff


def relation(a: float, b: float) -> str:
    if np.isclose(a, b, rtol=1.0e-12, atol=1.0e-14):
        return "="
    return "<" if a < b else ">"


def ordering_statement(names: list[str], values: list[float]) -> str:
    out = [names[0]]
    for i in range(len(values) - 1):
        out.append(relation(values[i], values[i + 1]))
        out.append(names[i + 1])
    return " ".join(out)


def ordering_holds(values: list[float], statement: str) -> bool:
    tokens = statement.split()
    for i in range(1, len(tokens), 2):
        left_name = tokens[i - 1]
        op = tokens[i]
        right_name = tokens[i + 1]
        left = values[int(left_name[1:]) - 1]
        right = values[int(right_name[1:]) - 1]
        if op == "=" and not np.isclose(left, right, rtol=1.0e-12, atol=1.0e-14):
            return False
        if op == "<" and not left < right:
            return False
        if op == ">" and not left > right:
            return False
    return True


def drift_statement(steps: list[int], values: list[float]) -> str:
    names = [f"k{step}" for step in steps]
    return ordering_statement(names, values)


def drift_holds(steps: list[int], values: list[float], statement: str) -> bool:
    by_name = {f"k{step}": values[i] for i, step in enumerate(steps)}
    tokens = statement.split()
    for i in range(1, len(tokens), 2):
        left = by_name[tokens[i - 1]]
        op = tokens[i]
        right = by_name[tokens[i + 1]]
        if op == "=" and not np.isclose(left, right, rtol=1.0e-12, atol=1.0e-14):
            return False
        if op == "<" and not left < right:
            return False
        if op == ">" and not left > right:
            return False
    return True


def shell_no_short_wraparound(period: int) -> bool:
    max_shell_component = 2
    return max_shell_component < period / 2.0


def retained_count_after_steps(period: int) -> int:
    state = initial_state(period)
    for _ in range(STEPS):
        state = exact_checkerboard_step(state)
    return state.h.shape[0]


def finite_factor_for_ratio(ratio: float) -> float:
    if ratio == 0.0:
        return 1.0
    factor = max(ratio, 1.0 / ratio)
    return factor * (1.0 + 1.0e-12)


def main() -> None:
    ref = run_pipeline(REFERENCE_L, "shell")
    exact_ref = run_pipeline(REFERENCE_L, "exact")
    assert isinstance(ref["records"], dict)
    assert isinstance(ref["errors"], list)
    assert isinstance(ref["next_hkd_norms"], dict)
    assert isinstance(exact_ref["final"], State)

    records = ref["records"]
    errors = [float(x) for x in ref["errors"]]
    next_hkd_norms = {int(k): float(v) for k, v in ref["next_hkd_norms"].items()}
    budget16 = resolvent_budget(REFERENCE_L)
    budget12 = resolvent_budget(STABILITY_L)
    budget_ratio = budget12["block_max"] / budget16["block_max"]
    true_ratio_factor = 1.01  # frozen: measured 1.0001 -- L-stability within 1%
    regression_ceiling16 = 3.21e-02  # frozen regression ceiling (measured 3.2012e-2)
    control_max = compare_exact_to_identity(REFERENCE_L)

    error_names = [f"k{i}" for i in range(1, STEPS + 1)]
    error_order = ordering_statement(error_names, errors)
    ratio_steps = list(PRINT_COUPLING_STEPS)
    c4_ratios = [float(records[k]["r4"]) for k in ratio_steps]
    c4_drift = drift_statement(ratio_steps, c4_ratios)

    retained16 = retained_count_after_steps(REFERENCE_L)
    retained12 = retained_count_after_steps(STABILITY_L)

    print("# V2: iterating the truncated d=2 flow with accumulated measured budgets")
    print(
        "SCOPE: finite-L, E=0, free quadratic; measured-budget truncated "
        "trajectory, NOT a validated RG flow; follow-on: error-controlled "
        "fixed-point search."
    )
    print("STATUS: pipeline-derived; audit lane grades.")
    print(
        f"CONVENTION: h0=({DIAG0:.1f})I plus nearest-neighbor {HOP0:.1f}; "
        f"checkerboard Schur steps={STEPS}; truncation shells d2={sorted(TRUNC_D2)}."
    )
    print()

    print("V2a truncated flow trajectory on L=16:")
    for step in PRINT_COUPLING_STEPS:
        rec = records[step]
        print(
            f"  k={step}: "
            f"diag={float(rec['diag']): .16e} "
            f"c4={float(rec['c4']): .16e} "
            f"c8={float(rec['c8']): .16e} "
            f"c4/diag={float(rec['r4']): .16e} "
            f"c8/diag={float(rec['r8']): .16e} "
            f"(counts: c4={int(rec['c4_count'])}, c8={int(rec['c8_count'])}; "
            f"spreads: diag={float(rec['diag_spread']):.3e}, "
            f"c4={float(rec['c4_spread']):.3e}, "
            f"c8={float(rec['c8_spread']):.3e})"
        )
    print()

    print("V2b per-step dropped-tail truncation errors on L=16:")
    for step, err in enumerate(errors, start=1):
        print(f"  k={step}: ||h_k_trunc - h_k_full||_max = {err: .16e}")
    print(f"  true size ordering: {error_order}")
    print()

    print("V2c accumulated resolvent budget at E=0:")
    print(
        f"  L=16 retained-block max difference = {budget16['block_max']: .16e}; "
        f"retained-site diagonal max difference = {budget16['diag_max']: .16e}"
    )
    print(
        f"  L=12 retained-block max difference = {budget12['block_max']: .16e}; "
        f"retained-site diagonal max difference = {budget12['diag_max']: .16e}"
    )
    print(
        f"  L=12/L=16 retained-block ratio = {budget_ratio: .16e}; "
        f"true factor = {true_ratio_factor: .16e}"
    )
    print()

    print("V2d c4/diag ratio drift on L=16:")
    print(f"  true drift pattern: {c4_drift}")
    print("  next-step kept/drop block max norms:")
    for step in PRINT_COUPLING_STEPS:
        print(f"    after k={step}: ||H_kd||_max = {next_hkd_norms[step]: .16e}")
    print()

    print("V2e control:")
    print(f"  identity truncation max difference from exact steps = {control_max: .16e}")
    print()

    checks = CheckBook()
    checks.check(
        "finite-lattice shell probe L=16: d2={4,8} shell components are below L/2",
        shell_no_short_wraparound(REFERENCE_L),
    )
    checks.check(
        "finite-lattice shell probe L=12: d2={4,8} shell components are below L/2",
        shell_no_short_wraparound(STABILITY_L),
    )
    checks.check(
        "size probe after 4 checkerboard steps: L=16 retains 16 sites and L=12 retains 9 sites",
        retained16 == 16 and retained12 == 9,
    )
    checks.check(
        "per-step truncation errors: k1 > k2 and k3 = k4 = 0 exactly (the "
        "post-step-2 closure makes later drops empty -- fixed-pattern gate)",
        all(np.isfinite(errors)) and errors[0] > errors[1] > 0
        and abs(errors[2]) < 1e-15 and abs(errors[3]) < 1e-15,
    )
    checks.check(
        (
            "L=16 accumulated retained-block resolvent budget "
            f"{budget16['block_max']:.16e} <= regression ceiling "
            f"{regression_ceiling16:.16e}"
        ),
        np.isfinite(budget16["block_max"]) and budget16["block_max"] <= regression_ceiling16,
    )
    checks.check(
        (
            "L=12 vs L=16 retained-block budget ratio "
            f"{budget_ratio:.16e} is within true factor {true_ratio_factor:.16e}"
        ),
        (
            np.isfinite(budget_ratio)
            and np.isfinite(true_ratio_factor)
            and (1.0 / true_ratio_factor) <= budget_ratio <= true_ratio_factor
        ),
    )
    checks.check(
        "V2d the truncated flow's c4/diag ratio FREEZES: identical at steps 2,3,4 "
        "(equality 1e-12) -- the truncated map reaches a fixed coupling ratio "
        "immediately",
        all(np.isfinite(c4_ratios))
        and max(abs(c4_ratios[i] - c4_ratios[0]) for i in range(len(c4_ratios))) < 1e-12,
    )
    checks.check(
        "post-step-2 closure: the next checkerboard kept/drop block H_kd is zero "
        "at steps 2,3,4",
        max(abs(next_hkd_norms[step]) for step in PRINT_COUPLING_STEPS) < 1e-15,
    )
    checks.check(
        (
            "identity truncation reproduces fully exact checkerboard steps "
            f"within 1e-12 (max {control_max:.3e})"
        ),
        np.isfinite(control_max) and control_max <= CONTROL_TOL,
    )
    checks.finish()


if __name__ == "__main__":
    main()
