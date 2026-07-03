#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/NO_RECOVERY_INTERMEDIATE_BUDGET_EFFICIENCY_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_no_recovery_efficiency_table_2026_06_12.py
"""
import sys

import numpy as np


POINTER_STATES = 2
FRAGMENT_STATES = 4
FRAGMENT_COUNT = 3
LATTICE_SHAPE = (POINTER_STATES,) + (FRAGMENT_STATES,) * FRAGMENT_COUNT
LATTICE_SIZE = POINTER_STATES * (FRAGMENT_STATES ** FRAGMENT_COUNT)

BLANK = 0
RECORD_ZERO = 1
RECORD_ONE = 2
ERASED = 3

PHASE1_STEPS = 3
PHASE2_STEPS = 5
TOTAL_STEPS = PHASE1_STEPS + PHASE2_STEPS

EPS_GRID = np.array([0.3, 0.6, 0.9], dtype=float)
CONTROL_EPS_ZERO = 0.0
PRIMARY_THRESHOLD = 0.5
THRESHOLDS = np.array([0.3, 0.5, 0.7], dtype=float)

EROSION_PER_EPS = 0.07

TOL_ANCHOR = 1.0e-12
TOL_MONOTONE = 1.0e-12
TOL_BUDGET = 1.0e-9
TOL_EXACT = 1.0e-12
TOL_PROB = 1.0e-12

ANCHOR_GRID_INDEX = 1
ANCHOR_B = np.array([3.0, 2.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
ANCHOR_C = np.array([0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0])
ANCHOR_R50 = np.array(
    [
        0.0,
        0.958,
        1.8757639999999998,
        2.754981912,
        2.6392726716959998,
        2.5284232194847673,
        2.4222294442664074,
        2.3204958076072177,
        2.223034983687715,
    ],
    dtype=float,
)


PASS_COUNT = 0
FAIL_COUNT = 0


def check(label, condition):
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
        print(f"PASS: {label}")
    else:
        FAIL_COUNT += 1
        print(f"FAIL: {label}")


def fragment_slice(fragment, state):
    key = [slice(None)] * (FRAGMENT_COUNT + 1)
    key[fragment + 1] = state
    return tuple(key)


def pointer_fragment_slice(pointer, fragment, state):
    key = [slice(None)] * (FRAGMENT_COUNT + 1)
    key[0] = pointer
    key[fragment + 1] = state
    return tuple(key)


def encode_state(pointer, fragments):
    return int(np.ravel_multi_index((pointer,) + tuple(fragments), LATTICE_SHAPE, mode="raise"))


def decode_state(index):
    return np.unravel_index(index, LATTICE_SHAPE)


def initial_distribution(pointer_mode):
    dist = np.zeros(LATTICE_SHAPE, dtype=float)
    if pointer_mode == "balanced":
        dist[(0, BLANK, BLANK, BLANK)] = 0.5
        dist[(1, BLANK, BLANK, BLANK)] = 0.5
    elif pointer_mode == "zero":
        dist[(0, BLANK, BLANK, BLANK)] = 1.0
    else:
        raise ValueError(f"unknown pointer mode: {pointer_mode}")
    return dist


def broadcast(dist, fragment):
    out = dist.copy()
    for pointer, record_state in ((0, RECORD_ZERO), (1, RECORD_ONE)):
        blank_key = pointer_fragment_slice(pointer, fragment, BLANK)
        record_key = pointer_fragment_slice(pointer, fragment, record_state)
        moved = dist[blank_key].copy()
        out[blank_key] -= moved
        out[record_key] += moved
    return out


def erode_fragment(dist, fragment, eps):
    disturbance = EROSION_PER_EPS * eps
    out = dist.copy()
    erased_key = fragment_slice(fragment, ERASED)
    for record_state in (RECORD_ZERO, RECORD_ONE):
        record_key = fragment_slice(fragment, record_state)
        moved = dist[record_key] * disturbance
        out[record_key] -= moved
        out[erased_key] += moved
    return out


def erode_all_fragments(dist, eps):
    out = dist
    for fragment in range(FRAGMENT_COUNT):
        out = erode_fragment(out, fragment, eps)
    return out


def blank_count(dist):
    total = 0.0
    for fragment in range(FRAGMENT_COUNT):
        total += float(np.sum(dist[fragment_slice(fragment, BLANK)]))
    return total


def pointer_z_grid():
    z = np.array([1.0, -1.0], dtype=float)
    return z.reshape((POINTER_STATES,) + (1,) * FRAGMENT_COUNT)


def fragment_z_grid(fragment):
    z = np.array([0.0, 1.0, -1.0, 0.0], dtype=float)
    shape = [1] * (FRAGMENT_COUNT + 1)
    shape[fragment + 1] = FRAGMENT_STATES
    return z.reshape(shape)


POINTER_Z = pointer_z_grid()
FRAGMENT_Z = [fragment_z_grid(fragment) for fragment in range(FRAGMENT_COUNT)]


def connected_correlators(dist):
    pointer_mean = float(np.sum(dist * POINTER_Z))
    values = []
    for fragment in range(FRAGMENT_COUNT):
        fragment_z = FRAGMENT_Z[fragment]
        fragment_mean = float(np.sum(dist * fragment_z))
        joint_mean = float(np.sum(dist * POINTER_Z * fragment_z))
        values.append(joint_mean - pointer_mean * fragment_mean)
    return np.array(values, dtype=float)


def record_count(dist, threshold):
    correlators = connected_correlators(dist)
    counted = np.where(correlators >= threshold, correlators, 0.0)
    return float(np.sum(counted))


def metrics(dist, threshold):
    b_value = blank_count(dist)
    return b_value, FRAGMENT_COUNT - b_value, record_count(dist, threshold)


def run_history(eps, pointer_mode="balanced", threshold=PRIMARY_THRESHOLD):
    dist = initial_distribution(pointer_mode)
    states = [dist]
    b_values = []
    c_values = []
    r_values = []

    b_value, c_value, r_value = metrics(dist, threshold)
    b_values.append(b_value)
    c_values.append(c_value)
    r_values.append(r_value)

    for fragment in range(PHASE1_STEPS):
        dist = broadcast(dist, fragment)
        dist = erode_all_fragments(dist, eps)
        states.append(dist)
        b_value, c_value, r_value = metrics(dist, threshold)
        b_values.append(b_value)
        c_values.append(c_value)
        r_values.append(r_value)

    for _ in range(PHASE2_STEPS):
        dist = erode_all_fragments(dist, eps)
        states.append(dist)
        b_value, c_value, r_value = metrics(dist, threshold)
        b_values.append(b_value)
        c_values.append(c_value)
        r_values.append(r_value)

    return {
        "eps": eps,
        "pointer_mode": pointer_mode,
        "threshold": threshold,
        "states": states,
        "B": np.array(b_values, dtype=float),
        "C": np.array(c_values, dtype=float),
        "R": np.array(r_values, dtype=float),
    }


def final_efficiency(history, threshold):
    final_dist = history["states"][-1]
    c_final = history["C"][-1]
    r_final = record_count(final_dist, threshold)
    return r_final / c_final, r_final, c_final


def all_primary_histories():
    return [run_history(float(eps), "balanced", PRIMARY_THRESHOLD) for eps in EPS_GRID]


def final_efficiency_table(histories):
    rows = []
    for threshold in THRESHOLDS:
        for history in histories:
            eta, r_final, c_final = final_efficiency(history, float(threshold))
            rows.append(
                {
                    "threshold": float(threshold),
                    "eps": float(history["eps"]),
                    "eta": eta,
                    "R_final": r_final,
                    "C_final": c_final,
                }
            )
    return rows


def eta_matrix(rows):
    matrix = np.zeros((len(THRESHOLDS), len(EPS_GRID)), dtype=float)
    for threshold_index, threshold in enumerate(THRESHOLDS):
        for eps_index, eps in enumerate(EPS_GRID):
            matches = [
                row["eta"]
                for row in rows
                if row["threshold"] == float(threshold) and row["eps"] == float(eps)
            ]
            matrix[threshold_index, eps_index] = matches[0]
    return matrix


def lattice_probe_ok():
    first_index_ok = encode_state(0, (BLANK, BLANK, BLANK)) == 0
    last_index_ok = encode_state(1, (ERASED, ERASED, ERASED)) == LATTICE_SIZE - 1
    probe_indices = np.array([0, 1, LATTICE_SIZE - 2, LATTICE_SIZE - 1], dtype=int)
    roundtrip_ok = True
    for index in probe_indices:
        decoded = decode_state(int(index))
        encoded = encode_state(decoded[0], decoded[1:])
        roundtrip_ok = roundtrip_ok and (encoded == int(index))
    size_ok = LATTICE_SIZE == int(np.prod(np.array(LATTICE_SHAPE, dtype=int)))
    shape_ok = LATTICE_SHAPE == (2, 4, 4, 4)
    return first_index_ok and last_index_ok and roundtrip_ok and size_ok and shape_ok


def probability_probe_ok(histories):
    state_sums = []
    state_mins = []
    for history in histories:
        for state in history["states"]:
            state_sums.append(float(np.sum(state)))
            state_mins.append(float(np.min(state)))
    sums_ok = np.max(np.abs(np.array(state_sums, dtype=float) - 1.0)) <= TOL_PROB
    mins_ok = np.min(np.array(state_mins, dtype=float)) >= -TOL_PROB
    return sums_ok and mins_ok


def print_histories(histories):
    print("HISTORY threshold=0.5")
    print("eps,t,B,C,R")
    for history in histories:
        eps = history["eps"]
        for t in range(TOTAL_STEPS + 1):
            print(
                f"{eps:.1f},{t},"
                f"{history['B'][t]:.12f},"
                f"{history['C'][t]:.12f},"
                f"{history['R'][t]:.12f}"
            )


def print_efficiencies(rows):
    print("EFFICIENCY threshold,eps,eta,R_final,C_final")
    for row in rows:
        print(
            f"{row['threshold']:.1f},"
            f"{row['eps']:.1f},"
            f"{row['eta']:.12f},"
            f"{row['R_final']:.12f},"
            f"{row['C_final']:.12f}"
        )


def main():
    histories = all_primary_histories()
    rows = final_efficiency_table(histories)
    etas = eta_matrix(rows)

    anchor = histories[ANCHOR_GRID_INDEX]
    anchor_condition = (
        np.max(np.abs(anchor["B"] - ANCHOR_B)) <= TOL_ANCHOR
        and np.max(np.abs(anchor["C"] - ANCHOR_C)) <= TOL_ANCHOR
        and np.max(np.abs(anchor["R"] - ANCHOR_R50)) <= TOL_ANCHOR
    )
    check("ANCHOR reproduction eps=0.6 threshold=0.5 B/C/R histories", anchor_condition)

    primary_record_sum = float(np.sum([history["R"][-1] for history in histories]))
    primary_consumed_sum = float(np.sum([history["C"][-1] for history in histories]))
    check(
        "ANTI-FAB nonzero primary records and consumed blanks",
        primary_record_sum > 0.0 and primary_consumed_sum > 0.0,
    )

    check("FINITE lattice pointer+3 fragments size and no index wraparound", lattice_probe_ok())
    check("Born weights stay normalized and nonnegative", probability_probe_ok(histories))

    disturbance_values = EROSION_PER_EPS * EPS_GRID
    check(
        "weak-measure disturbances stay inside the stochastic finite-lattice kernel",
        np.min(disturbance_values) >= 0.0 and np.max(disturbance_values) <= 1.0,
    )

    for history in histories:
        eps = history["eps"]
        check(
            f"blank count B(t) non-increasing for eps={eps:.1f}",
            np.all(np.diff(history["B"]) <= TOL_MONOTONE),
        )
        check(
            f"record-functional budget R(t)<=C(t)+1e-9 for every tracked time at eps={eps:.1f}",
            np.all(history["R"] <= history["C"] + TOL_BUDGET),
        )

    eta_decreases_by_eps = np.all(np.diff(etas, axis=1) <= TOL_EXACT)
    check("efficiency eta decreases with eps for every probed threshold", eta_decreases_by_eps)

    threshold_monotone = np.all(np.diff(etas, axis=0) <= TOL_EXACT)
    check("threshold probe final eta is non-increasing as threshold rises", threshold_monotone)

    eps_zero_history = run_history(CONTROL_EPS_ZERO, "balanced", PRIMARY_THRESHOLD)
    check(
        "eps=0 control has R(t)=C(t) at all tracked times",
        np.max(np.abs(eps_zero_history["R"] - eps_zero_history["C"])) <= TOL_EXACT,
    )
    eta_zero, r_zero, c_zero = final_efficiency(eps_zero_history, PRIMARY_THRESHOLD)
    check(
        "eps=0 control has eta=1 exactly after consumed blanks",
        abs(eta_zero - 1.0) <= TOL_EXACT and abs(r_zero - c_zero) <= TOL_EXACT,
    )

    zero_pointer_histories = [
        run_history(float(eps), "zero", PRIMARY_THRESHOLD)
        for eps in np.array([0.0, 0.3, 0.6, 0.9], dtype=float)
    ]
    zero_pointer_r_max = np.max(
        np.abs(np.concatenate([history["R"] for history in zero_pointer_histories]))
    )
    zero_pointer_c_final_min = np.min(np.array([history["C"][-1] for history in zero_pointer_histories]))
    zero_pointer_eta_max = np.max(
        np.abs(
            np.array(
                [
                    final_efficiency(history, PRIMARY_THRESHOLD)[0]
                    for history in zero_pointer_histories
                ],
                dtype=float,
            )
        )
    )
    check(
        "|0>-pointer consumes blanks with connected-correlator R=0",
        zero_pointer_c_final_min == 3.0 and zero_pointer_r_max <= TOL_EXACT,
    )
    check(
        "|0>-pointer final eta=0",
        zero_pointer_eta_max <= TOL_EXACT,
    )

    print_histories(histories)
    print_efficiencies(rows)

    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT != 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
