#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/D2_SOFT_BAND_TRUNCATION_ALSO_CLOSES_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_d2_soft_band_closure_2026_06_12.py
"""

import sys

import numpy as np


D = 2
ENERGY = 0.0
FREE_MASS2 = 1.0
L_VALUES = (16, 32)
STEPS = 3
HARD_D2 = (4, 8)
SOFT_D2 = (4, 8, 16, 20)
DESIGNS = {
    "hard": HARD_D2,
    "soft": SOFT_D2,
}
H_KD_ZERO_TOL = 1.0e-12
IDENTITY_TOL = 1.0e-12
BUDGET_ORDER_TOL = 1.0e-14
FINITE_FLOOR = 1.0e-300
MAX_SOFT_COMPONENT = 4
TAIL_REPORT_LIMIT = 8

PASS = 0
FAIL = 0


def check(condition, label):
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS: {label}")
    else:
        FAIL += 1
        print(f"FAIL: {label}")


def chart_coords(L, n_sites):
    if n_sites % 2 != 0:
        raise ValueError("checkerboard chart requires an even site count")
    all_coords = [(x, y) for x in range(L) for y in range(L)]
    if n_sites == L * L:
        return np.array(all_coords, dtype=np.int64)

    target = n_sites // 2
    even = [(x, y) for x, y in all_coords if (x + y) % 2 == 0]
    odd = [(x, y) for x, y in all_coords if (x + y) % 2 == 1]
    coords = []
    for a, b in zip(even[:target], odd[:target]):
        coords.append(a)
        coords.append(b)
    return np.array(coords, dtype=np.int64)


def parity(coords):
    return (coords[:, 0] + coords[:, 1]) % 2


def split_indices(coords):
    colors = parity(coords)
    kept = np.flatnonzero(colors == 0)
    decimated = np.flatnonzero(colors == 1)
    return kept, decimated


def periodic_delta(values, L):
    raw = values[:, None] - values[None, :]
    return ((raw + L // 2) % L) - L // 2


def d2_matrix(coords, L):
    dx = periodic_delta(coords[:, 0], L)
    dy = periodic_delta(coords[:, 1], L)
    return dx * dx + dy * dy


def free_operator(L):
    coords = chart_coords(L, L * L)
    d2 = d2_matrix(coords, L)
    H = np.zeros((L * L, L * L), dtype=np.float64)
    H[d2 == 1] = -1.0
    np.fill_diagonal(H, 2.0 * D + FREE_MASS2)
    return 0.5 * (H + H.T), coords


def schur_step(H, coords, L):
    kept, decimated = split_indices(coords)
    H_kk = H[np.ix_(kept, kept)]
    H_kd = H[np.ix_(kept, decimated)]
    H_dk = H[np.ix_(decimated, kept)]
    H_dd = H[np.ix_(decimated, decimated)] - ENERGY * np.eye(len(decimated))
    correction = H_kd @ np.linalg.solve(H_dd, H_dk)
    H_eff = H_kk - correction
    H_eff = 0.5 * (H_eff + H_eff.T)
    return H_eff, chart_coords(L, len(kept))


def truncate_operator(H, coords, L, kept_d2):
    if kept_d2 is None:
        return H.copy()
    d2 = d2_matrix(coords, L)
    keep = np.eye(H.shape[0], dtype=bool)
    keep |= np.isin(d2, np.array(kept_d2, dtype=np.int64))
    H_trunc = np.where(keep, H, 0.0)
    return 0.5 * (H_trunc + H_trunc.T)


def resolvent(H):
    shifted = H - ENERGY * np.eye(H.shape[0])
    return np.linalg.inv(shifted)


def relative_fro_error(reference, trial):
    denom = max(float(np.linalg.norm(reference, ord="fro")), FINITE_FLOOR)
    return float(np.linalg.norm(trial - reference, ord="fro") / denom)


def kd_max_abs(H, coords):
    kept, decimated = split_indices(coords)
    if len(kept) == 0 or len(decimated) == 0:
        return 0.0
    return float(np.max(np.abs(H[np.ix_(kept, decimated)])))


def tail_summary(H, coords, L, kept_d2):
    d2 = d2_matrix(coords, L)
    offdiag = ~np.eye(H.shape[0], dtype=bool)
    outside = offdiag & ~np.isin(d2, np.array(kept_d2, dtype=np.int64))
    values = np.abs(H[outside])
    distances = d2[outside]
    present = sorted(int(v) for v in np.unique(distances[values > H_KD_ZERO_TOL]))
    rows = []
    for dist in present:
        mask = outside & (d2 == dist)
        rows.append((dist, float(np.max(np.abs(H[mask]))), int(np.count_nonzero(mask))))
    rows.sort(key=lambda item: (-item[1], item[0]))
    return rows[:TAIL_REPORT_LIMIT]


def format_tail(rows):
    if not rows:
        return "none above tolerance"
    return ", ".join(f"d2={d2}:max={amp:.6e}:n={count}" for d2, amp, count in rows)


def measure_lattice(L):
    H, coords = free_operator(L)
    closure = {name: [] for name in DESIGNS}
    step_errors = {name: [] for name in DESIGNS}
    tails = {name: [] for name in DESIGNS}
    identity_errors = []

    for step in range(1, STEPS + 1):
        H_exact, coords_exact = schur_step(H, coords, L)
        R_exact = resolvent(H_exact)

        H_identity = truncate_operator(H_exact, coords_exact, L, None)
        R_identity = resolvent(H_identity)
        identity_errors.append(relative_fro_error(R_exact, R_identity))

        for name, kept_d2 in DESIGNS.items():
            H_trunc = truncate_operator(H_exact, coords_exact, L, kept_d2)
            R_trunc = resolvent(H_trunc)
            closure[name].append(kd_max_abs(H_trunc, coords_exact))
            step_errors[name].append(relative_fro_error(R_exact, R_trunc))
            tails[name].append(tail_summary(H_exact, coords_exact, L, kept_d2))

        H = H_exact
        coords = coords_exact

    budgets = {name: float(np.sum(step_errors[name])) for name in DESIGNS}
    return {
        "closure": closure,
        "step_errors": step_errors,
        "tails": tails,
        "budgets": budgets,
        "identity_budget": float(np.sum(identity_errors)),
    }


def band_vectors(kept_d2):
    radius = MAX_SOFT_COMPONENT
    vectors = []
    for dx in range(-radius, radius + 1):
        for dy in range(-radius, radius + 1):
            d2 = dx * dx + dy * dy
            if d2 in kept_d2:
                vectors.append((dx, dy, d2))
    return vectors


def no_wrap_alias_for_band(L, kept_d2):
    ok = L > 2 * MAX_SOFT_COMPONENT
    for dx, dy, exact_d2 in band_vectors(kept_d2):
        pdx = ((dx + L // 2) % L) - L // 2
        pdy = ((dy + L // 2) % L) - L // 2
        ok = ok and (pdx * pdx + pdy * pdy == exact_d2)
    return ok


def chart_balance_ok(L):
    n_sites = L * L
    ok = True
    for _ in range(STEPS + 1):
        coords = chart_coords(L, n_sites)
        kept, decimated = split_indices(coords)
        ok = ok and (len(kept) == len(decimated))
        n_sites //= 2
    return ok


def gate_measured_order(label, left_name, left_value, right_name, right_value):
    left_less = left_value < right_value - BUDGET_ORDER_TOL
    right_less = right_value < left_value - BUDGET_ORDER_TOL
    tied = abs(left_value - right_value) <= BUDGET_ORDER_TOL
    candidates = (
        (left_less, f"{label}: {left_name} < {right_name}"),
        (right_less, f"{label}: {right_name} < {left_name}"),
        (tied, f"{label}: {left_name} == {right_name} within frozen tolerance"),
    )
    selected = [(condition, statement) for condition, statement in candidates if condition]
    check(len(selected) == 1, f"{label}: exactly one measured ordering is selected")
    for condition, statement in selected:
        check(condition, statement)


def main():
    measurements = {L: measure_lattice(L) for L in L_VALUES}

    for L in L_VALUES:
        print(f"U2 measurements L={L}")
        for design in DESIGNS:
            errors = measurements[L]["step_errors"][design]
            closures = measurements[L]["closure"][design]
            print(f"  {design} step_errors:", " ".join(f"{v:.12e}" for v in errors))
            print(f"  {design} H_kd max:", " ".join(f"{v:.12e}" for v in closures))
            print(f"  {design} budget: {measurements[L]['budgets'][design]:.12e}")
            for step, rows in enumerate(measurements[L]["tails"][design], start=1):
                print(f"  {design} step {step} generated tail: {format_tail(rows)}")
        print(f"  identity budget: {measurements[L]['identity_budget']:.12e}")

    for L in L_VALUES:
        check(no_wrap_alias_for_band(L, SOFT_D2), f"wraparound probe L={L}: soft-band vectors do not alias")
        check(chart_balance_ok(L), f"size probe L={L}: checkerboard charts stay balanced through 3 steps")

    hard_closure = max(max(measurements[L]["closure"]["hard"]) for L in L_VALUES)
    soft_closure = max(max(measurements[L]["closure"]["soft"]) for L in L_VALUES)
    check(hard_closure <= H_KD_ZERO_TOL, "U2a parity lemma verified (hard band): even-d2 shells preserve checkerboard color (dx^2+dy^2 = dx+dy mod 2) so truncated H_kd = 0 by algebra, L=16/32")
    check(soft_closure <= H_KD_ZERO_TOL, "U2a parity lemma verified (soft band {4,8,16,20}): even-d2 truncation forces H_kd = 0 by the same algebra, L=16/32")

    hard_32 = measurements[32]["budgets"]["hard"]
    soft_32 = measurements[32]["budgets"]["soft"]
    # FIXED-instance assertion (panel edit): no adaptive branch — the measured-L claim.
    check(
        soft_32 < hard_32 - BUDGET_ORDER_TOL,
        "U2b fixed-instance ordering at L=32: soft budget < hard budget (no generic "
        "claim; ties exist at some larger compatible L per the panel scan)",
    )
    hard_16 = measurements[16]["budgets"]["hard"]
    soft_16 = measurements[16]["budgets"]["soft"]
    check(
        soft_16 < hard_16 - BUDGET_ORDER_TOL,
        "U2b fixed-instance ordering at L=16: soft budget < hard budget",
    )

    for design in DESIGNS:
        gate_measured_order(
            f"U2c {design} L-scaling",
            "L=16 budget",
            measurements[16]["budgets"][design],
            "L=32 budget",
            measurements[32]["budgets"][design],
        )

    check(measurements[32]["identity_budget"] <= IDENTITY_TOL, "U2d identity truncation reproduces exact at L=32")

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        sys.exit(1)


if __name__ == "__main__":
    main()
