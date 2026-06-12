#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/RECORD_EROSION_BRANCH_VS_ENSEMBLE_PERSISTENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_record_erosion_ensemble_persistence_2026_06_12.py
"""
import math
import sys

import numpy as np


EPS_GRID = (0.3, 0.6, 0.9)
STEPS = 10
NQ = 4
DIM = 2**NQ
TOL = 1e-10

basis = np.arange(DIM)
BITS = np.vstack(
    (
        (basis >> 3) & 1,  # pointer
        (basis >> 2) & 1,  # fragment 1
        (basis >> 1) & 1,  # fragment 2
        basis & 1,  # fragment 3
    )
)
ZVALS = 1.0 - 2.0 * BITS
POINTER_Z = ZVALS[0]

CNOT_PERMS = {}
for frag in (1, 2, 3):
    shift = 3 - frag
    perm = basis.copy()
    pointer_one = BITS[0].astype(bool)
    perm[pointer_one] = perm[pointer_one] ^ (1 << shift)
    CNOT_PERMS[frag] = perm

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name, condition, detail):
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    print(f"{tag}: {name} :: {detail}")


def idx(pointer, f1, f2, f3):
    return (pointer << 3) | (f1 << 2) | (f2 << 1) | f3


def initial_state(pointer_initial):
    state = np.zeros(DIM, dtype=np.complex128)
    if pointer_initial == "plus":
        state[idx(0, 0, 0, 0)] = 1.0 / math.sqrt(2.0)
        state[idx(1, 0, 0, 0)] = 1.0 / math.sqrt(2.0)
    elif pointer_initial == "zero":
        state[idx(0, 0, 0, 0)] = 1.0
    else:
        raise ValueError(f"unknown pointer_initial={pointer_initial!r}")
    return state


def apply_cnot(state, frag):
    out = np.zeros_like(state)
    out[CNOT_PERMS[frag]] = state
    return out


def apply_pointer_kraus(state, eps, sign):
    factors = np.sqrt((1.0 + sign * eps * POINTER_Z) / 2.0)
    return state * factors


def split_measure(branches, eps):
    out = []
    for weight, state in branches:
        for sign in (1.0, -1.0):
            raw = apply_pointer_kraus(state, eps, sign)
            prob = float(np.vdot(raw, raw).real)
            new_weight = weight * prob
            if prob > 0.0:
                new_state = raw / math.sqrt(prob)
            else:
                new_state = state.copy()
            out.append((new_weight, new_state))
    return out


def connected_count(state):
    prob = np.abs(state) ** 2
    ezp = float(prob @ ZVALS[0])
    count = 0
    for frag in (1, 2, 3):
        ezf = float(prob @ ZVALS[frag])
        ezz = float(prob @ (ZVALS[0] * ZVALS[frag]))
        if abs(ezz - ezp * ezf) > 0.5:
            count += 1
    return count


def joint_distribution(branches, frag):
    joint = np.zeros((2, 2), dtype=np.float64)
    p_bits = BITS[0]
    f_bits = BITS[frag]
    for weight, state in branches:
        if weight == 0.0:
            continue
        probs = weight * (np.abs(state) ** 2)
        np.add.at(joint, (p_bits, f_bits), probs)
    return joint


def mutual_information_bits(joint):
    total = float(joint.sum())
    if total <= 0.0:
        return 0.0
    pxy = joint / total
    px = pxy.sum(axis=1)
    py = pxy.sum(axis=0)
    denom = px[:, None] * py[None, :]
    mask = (pxy > 0.0) & (denom > 0.0)
    return float(np.sum(pxy[mask] * np.log2(pxy[mask] / denom[mask])))


def measures(branches, t):
    weight_sum = float(sum(weight for weight, _ in branches))
    rbar = float(sum(weight * connected_count(state) for weight, state in branches))
    mis = [mutual_information_bits(joint_distribution(branches, frag)) for frag in (1, 2, 3)]
    rens = int(sum(mi > 0.5 for mi in mis))
    return {
        "t": t,
        "branches": len(branches),
        "weight_sum": weight_sum,
        "rbar": rbar,
        "rens": rens,
        "mis": mis,
    }


def simulate(phase1_eps, phase2_eps=None, pointer_initial="plus", steps=STEPS):
    if phase2_eps is None:
        phase2_eps = phase1_eps
    branches = [(1.0, initial_state(pointer_initial))]
    rows = []
    for t in range(1, steps + 1):
        if t <= 3:
            branches = [(weight, apply_cnot(state, t)) for weight, state in branches]
        eps = phase1_eps if t <= 3 else phase2_eps
        branches = split_measure(branches, eps)
        rows.append(measures(branches, t))
    return rows


def fmt(values):
    return "[" + ", ".join(f"{value:.12g}" for value in values) + "]"


def analytic_t3_rbar(eps):
    a = (1.0 + eps) / 2.0
    b = (1.0 - eps) / 2.0
    total = 0.0
    for plus_count in range(4):
        minus_count = 3 - plus_count
        amp0 = (a**plus_count) * (b**minus_count)
        amp1 = (b**plus_count) * (a**minus_count)
        branch_weight = 0.5 * (amp0 + amp1)
        posterior0 = amp0 / (amp0 + amp1)
        posterior1 = amp1 / (amp0 + amp1)
        connected = 4.0 * posterior0 * posterior1
        if connected > 0.5:
            total += 3.0 * math.comb(3, plus_count) * branch_weight
    return total


def allclose(values, targets, atol=1e-12):
    return bool(np.allclose(np.array(values), np.array(targets), atol=atol, rtol=0.0))


def main():
    sims = {eps: simulate(eps) for eps in EPS_GRID}

    print("TRACE: t=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
    for eps in EPS_GRID:
        rbar_path = [row["rbar"] for row in sims[eps]]
        rens_path = [row["rens"] for row in sims[eps]]
        print(f"TRACE: eps={eps:.1f} Rbar={fmt(rbar_path)} Rens={fmt(rens_path)}")

    for eps in EPS_GRID:
        rows = sims[eps]
        max_weight_err = max(abs(row["weight_sum"] - 1.0) for row in rows)
        no_prune = all(row["branches"] == 2**row["t"] for row in rows)
        check(
            f"Y4a exact no-prune tree eps={eps:.1f}",
            max_weight_err < TOL and no_prune,
            f"max_weight_err={max_weight_err:.3e}, branch_counts={[row['branches'] for row in rows]}",
        )

    t3_rbar = [sims[eps][2]["rbar"] for eps in EPS_GRID]
    t3_expected = [analytic_t3_rbar(eps) for eps in EPS_GRID]
    check(
        "Y4b branch t=3 matches repeated-readout closed form",
        allclose(t3_rbar, t3_expected),
        f"computed={fmt(t3_rbar)}, closed_form={fmt(t3_expected)}",
    )

    t3_rens = [sims[eps][2]["rens"] for eps in EPS_GRID]
    t3_mis = [sims[eps][2]["mis"] for eps in EPS_GRID]
    check(
        "Y4b ensemble t=3 has all three classical records",
        t3_rens == [3, 3, 3] and all(all(abs(mi - 1.0) < 1e-12 for mi in row) for row in t3_mis),
        f"Rens={t3_rens}, MI={[[round(mi, 12) for mi in row] for row in t3_mis]}",
    )

    for eps in EPS_GRID:
        phase2 = [row["rbar"] for row in sims[eps][2:]]
        deltas = np.diff(np.array(phase2))
        if eps == 0.9:
            even_zero = all(abs(phase2[i]) < 1e-12 for i in range(0, len(phase2), 2))
            odd_vals = [phase2[i] for i in range(1, len(phase2), 2)]
            odd_decaying = all(odd_vals[i + 1] < odd_vals[i] for i in range(len(odd_vals) - 1))
            check(
                "Y4c eps=0.9 phase-2 trajectory OSCILLATES with decaying envelope: "
                "even steps exactly zero, odd-step rebounds strictly decaying "
                "(odd-step envelope strictly decreasing (ratio reported in detail)) -- not monotone-zero",
                even_zero and odd_decaying and odd_vals[-1] < 1e-3,
                f"phase2_Rbar={fmt(phase2)}",
            )
        else:
            check(
                f"Y4c eps={eps:.1f} threshold-count trajectory has phase-2 rebounds",
                bool(np.any(deltas > 1e-12)) and phase2[-1] < phase2[0],
                f"phase2_Rbar={fmt(phase2)}, deltas={fmt(deltas)}",
            )

    formation_persistence = all(
        row["rens"] == min(row["t"], 3)
        for eps in EPS_GRID
        for row in sims[eps]
    )
    phase2_mi_one = all(
        all(abs(mi - 1.0) < 1e-12 for mi in row["mis"])
        for eps in EPS_GRID
        for row in sims[eps][2:]
    )
    check(
        "Y4d ensemble record forms by broadcast count and persists through phase 2",
        formation_persistence and phase2_mi_one,
        "Rens(t)=min(t,3) for t=1..10 and every phase-2 fragment MI is 1 bit",
    )

    eps0_rows = simulate(0.0)
    eps0_phase2 = [row["rbar"] for row in eps0_rows[2:]]
    check(
        "Y4e eps=0 phase 2 changes no branch-relational records",
        max(abs(value - 3.0) for value in eps0_phase2) < 1e-12,
        f"phase2_Rbar={fmt(eps0_phase2)}",
    )

    projective_rows = simulate(0.0, phase2_eps=1.0, steps=4)
    check(
        "Y4e projective phase-2 step kills all connected correlators in one step",
        abs(projective_rows[2]["rbar"] - 3.0) < 1e-12 and abs(projective_rows[3]["rbar"]) < 1e-12,
        f"before={projective_rows[2]['rbar']:.12g}, after={projective_rows[3]['rbar']:.12g}",
    )

    zero_rows_by_eps = {eps: simulate(eps, pointer_initial="zero") for eps in EPS_GRID}
    zero_rbar_max = max(abs(row["rbar"]) for rows in zero_rows_by_eps.values() for row in rows)
    zero_rens_max = max(row["rens"] for rows in zero_rows_by_eps.values() for row in rows)
    zero_mi_max = max(mi for rows in zero_rows_by_eps.values() for row in rows for mi in row["mis"])
    check(
        "Y4e |0> pointer initial registers no branch or ensemble records",
        zero_rbar_max < 1e-12 and zero_rens_max == 0 and zero_mi_max < 1e-12,
        f"max_Rbar={zero_rbar_max:.3e}, max_Rens={zero_rens_max}, max_MI={zero_mi_max:.3e}",
    )

    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        sys.exit(1)


if __name__ == "__main__":
    main()
