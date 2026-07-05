#!/usr/bin/env python3
"""Under Born-weighted branching the record-budget ledger becomes an INEQUALITY:
on the exact 8-branch tree (1 pointer + 3 blank fragments; broadcast CNOT then
two-outcome weak Kraus per step, eps=0.6, depth 3) the per-branch relation is
R_b <= 3 - B_b (at the |C| > 0.5 record threshold; threshold-relative
strict counts probed at 0.3/0.5/0.7) -- branches can CONSUME a blank without a
threshold-clearing record (2 of 8 branches, printed verbatim; weak-measurement
partial decoherence) -- while the branch-averaged budget bound survives
(sum_b w_b S_b = 1.22 <= 3) and every branch respects the register deficit bound.
Controls: eps=0 recovers the landed linear ledger exactly; eps=1 projective branches
register nothing new; |0>-pointer registers nothing; weights sum to 1; no-prune.

Class-A exact verification for the source note

    docs/BRANCHING_RECORD_BUDGET_INEQUALITY_BOUNDED_THEOREM_NOTE_2026-06-12.md

Broadcast + weak-measurement model only, 4 qubits, depth 3, exact, no MC; NOT
claimed: thermodynamic specialness (separately registered input), measures over
states, Born derivation (derived-chain cap inherited), other dynamics/models.
Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_branching_record_budget_inequality_2026_06_12.py
"""
import sys

import numpy as np


N_QUBITS = 4
DIM = 1 << N_QUBITS
POINTER = 0
FRAGMENTS = (1, 2, 3)
MAIN_EPS = 0.6
WEIGHT_TOL = 1e-12
BLANK_TOL = 1e-9

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name, condition, detail):
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"[PASS] {name}: {detail}")
    else:
        FAIL_COUNT += 1
        print(f"[FAIL] {name}: {detail}")


def bit_position(qubit):
    return N_QUBITS - 1 - qubit


def bit_at(index, qubit):
    return (index >> bit_position(qubit)) & 1


def flip_bit(index, qubit):
    return index ^ (1 << bit_position(qubit))


def basis_index(bits):
    out = 0
    for bit in bits:
        out = (out << 1) | int(bit)
    return out


def initial_state(kind):
    state = np.zeros(DIM, dtype=np.complex128)
    if kind == "plus":
        amp = 1.0 / np.sqrt(2.0)
        state[basis_index((0, 0, 0, 0))] = amp
        state[basis_index((1, 0, 0, 0))] = amp
    elif kind == "zero":
        state[basis_index((0, 0, 0, 0))] = 1.0
    else:
        raise ValueError(f"unknown initial state {kind!r}")
    return state


def cnot(state, control, target):
    out = np.zeros_like(state)
    for idx, amp in enumerate(state):
        if bit_at(idx, control):
            out[flip_bit(idx, target)] += amp
        else:
            out[idx] += amp
    return out


def apply_weak_measurement(state, eps, outcome):
    sign = 1.0 if outcome == "+" else -1.0
    out = state.copy()
    for idx in range(DIM):
        z_pointer = 1.0 if bit_at(idx, POINTER) == 0 else -1.0
        out[idx] *= np.sqrt((1.0 + sign * eps * z_pointer) / 2.0)
    return out


def norm2(state):
    return float(np.vdot(state, state).real)


def run_model(eps, initial="plus", branch=True, prune_zero=False):
    branches = [{"path": "", "weight": 1.0, "state": initial_state(initial)}]
    for fragment in FRAGMENTS:
        next_branches = []
        for branch_state in branches:
            broadcast_state = cnot(branch_state["state"], POINTER, fragment)
            if not branch:
                next_branches.append(
                    {
                        "path": branch_state["path"],
                        "weight": branch_state["weight"],
                        "state": broadcast_state,
                    }
                )
                continue

            for outcome in ("+", "-"):
                raw = apply_weak_measurement(broadcast_state, eps, outcome)
                conditional_weight = norm2(raw)
                total_weight = branch_state["weight"] * conditional_weight
                if conditional_weight <= 0.0:
                    if prune_zero:
                        continue
                    normalized = raw
                else:
                    normalized = raw / np.sqrt(conditional_weight)
                next_branches.append(
                    {
                        "path": branch_state["path"] + outcome,
                        "weight": total_weight,
                        "state": normalized,
                    }
                )
        branches = next_branches
    return branches


def expectation_z(state, qubit):
    total = 0.0
    probabilities = np.abs(state) ** 2
    for idx, probability in enumerate(probabilities):
        z = 1.0 if bit_at(idx, qubit) == 0 else -1.0
        total += z * probability
    return float(total)


def expectation_zz(state, qubit_a, qubit_b):
    total = 0.0
    probabilities = np.abs(state) ** 2
    for idx, probability in enumerate(probabilities):
        z_a = 1.0 if bit_at(idx, qubit_a) == 0 else -1.0
        z_b = 1.0 if bit_at(idx, qubit_b) == 0 else -1.0
        total += z_a * z_b * probability
    return float(total)


def single_qubit_rho(state, qubit):
    rho = np.zeros((2, 2), dtype=np.complex128)
    full_mask = DIM - 1
    q_mask = 1 << bit_position(qubit)
    other_mask = full_mask ^ q_mask
    for i, amp_i in enumerate(state):
        if amp_i == 0.0:
            continue
        bit_i = bit_at(i, qubit)
        for j, amp_j in enumerate(state):
            if (i & other_mask) != (j & other_mask):
                continue
            bit_j = bit_at(j, qubit)
            rho[bit_i, bit_j] += amp_i * np.conjugate(amp_j)
    return rho


def von_neumann_entropy(rho):
    hermitian = 0.5 * (rho + rho.conjugate().T)
    eigenvalues = np.linalg.eigvalsh(hermitian).real
    eigenvalues = np.clip(eigenvalues, 0.0, 1.0)
    nonzero = eigenvalues[eigenvalues > 1e-15]
    if len(nonzero) == 0:
        return 0.0
    return float(-np.sum(nonzero * np.log2(nonzero)))


def is_z_basis_pure(rho, tol=BLANK_TOL):
    diagonal = np.real(np.diag(rho))
    offdiag = rho - np.diag(np.diag(rho))
    offdiag_small = np.max(np.abs(offdiag)) <= tol
    pure_population = np.max(diagonal) >= 1.0 - tol
    return bool(offdiag_small and pure_population)


def ledger_for_state(state):
    pointer_z = expectation_z(state, POINTER)
    connected = []
    entropies = []
    blank_count = 0

    for fragment in FRAGMENTS:
        fragment_z = expectation_z(state, fragment)
        zz = expectation_zz(state, POINTER, fragment)
        connected_value = zz - pointer_z * fragment_z
        connected.append(float(connected_value))

        rho = single_qubit_rho(state, fragment)
        entropies.append(von_neumann_entropy(rho))
        if is_z_basis_pure(rho):
            blank_count += 1

    record_count = sum(1 for value in connected if abs(value) > 0.5)
    entropy_sum = float(np.sum(entropies))
    return {
        "R": int(record_count),
        "B": int(blank_count),
        "S": entropy_sum,
        "connected": tuple(connected),
        "entropies": tuple(entropies),
    }


def branch_rows(branches):
    rows = []
    for branch_state in branches:
        ledger = ledger_for_state(branch_state["state"])
        rows.append({**branch_state, **ledger, "norm": np.sqrt(branch_state["weight"])})
    return rows


def print_rows(title, rows):
    print(title)
    print("path        weight          norm            R  B  S               c01             c02             c03")
    for row in rows:
        path = row["path"] if row["path"] else "linear"
        c01, c02, c03 = row["connected"]
        print(
            f"{path:<10}  {row['weight']:.12g}  {row['norm']:.12g}  "
            f"{row['R']:>1}  {row['B']:>1}  {row['S']:.12g}  "
            f"{c01:.12g}  {c02:.12g}  {c03:.12g}"
        )


def all_finite(rows):
    for row in rows:
        values = [row["weight"], row["norm"], row["S"], *row["connected"], *row["entropies"]]
        if not np.all(np.isfinite(values)):
            return False
    return True


def report_scope():
    print("SCOPE:")
    print("broadcast+weak-measurement model, 4 qubits, 3 steps, exact.")
    print("branch-resolved budget bound and observed per-branch relation are the data.")
    print("NOT claimed: thermodynamic specialness (the named separate input), measures over states,")
    print("Born derivation (derived-chain cap inherited), general dynamics.")
    print("Statuses pipeline-derived; audit lane grades.")


def main():
    report_scope()

    main_branches = run_model(MAIN_EPS, initial="plus", branch=True, prune_zero=False)
    main_rows = branch_rows(main_branches)
    print_rows("\nMAIN eps=0.6 branch table:", main_rows)

    total_weight = sum(row["weight"] for row in main_rows)
    min_norm = min(row["norm"] for row in main_rows)
    check(
        "W4a tree exactness weights",
        abs(total_weight - 1.0) <= WEIGHT_TOL,
        f"sum weights = {total_weight:.17g}",
    )
    check(
        "W4a tree exactness no-prune",
        len(main_rows) == 8 and min_norm > WEIGHT_TOL,
        f"branches = {len(main_rows)}, min branch norm = {min_norm:.17g}",
    )

    exceptions = [
        (row["path"], row["R"], row["B"], 3 - row["B"])
        for row in main_rows
        if row["R"] != 3 - row["B"]
    ]
    bound_ok = all(row["R"] <= 3 - row["B"] for row in main_rows)
    table_ok = len(main_rows) == 8 and all_finite(main_rows)
    if exceptions:
        print("\nW4b exceptions to exact R_b = 3 - B_b (path, R_b, B_b, 3-B_b):")
        for path, record_count, blank_count, available in exceptions:
            print(f"{path}  R_b={record_count}  B_b={blank_count}  3-B_b={available}")
        relation_detail = (
            f"exact equality fails on {len(exceptions)} branch(es); "
            "observed relation is R_b <= 3 - B_b for every computed branch"
        )
    else:
        relation_detail = "observed exact equality R_b = 3 - B_b on every computed branch"
    print(f"W4b observed per-branch relation: {relation_detail}.")
    check(
        "W4b PER-BRANCH LEDGER bound",
        table_ok and bound_ok,
        relation_detail,
    )
    check(
        "W4b PER-BRANCH LEDGER relation evaluated",
        table_ok,
        f"computed {len(main_rows)} branch rows and reported exact-equality exceptions verbatim",
    )

    weighted_r = sum(row["weight"] * row["R"] for row in main_rows)
    weighted_s = sum(row["weight"] * row["S"] for row in main_rows)
    diff = weighted_r - weighted_s
    print(
        "\nW4c weighted ledger: "
        f"sum_b w_b R_b = {weighted_r:.12g}, "
        f"sum_b w_b S_b = {weighted_s:.12g}, "
        f"difference = {diff:.12g}"
    )
    check(
        "W4c weighted entropy budget",
        weighted_s <= 3.0 + 1e-9,
        f"sum_b w_b S_b = {weighted_s:.17g} <= 3 + 1e-9",
    )

    # Threshold-relativity probe (panel edit): the record threshold |C| > 0.5 is a
    # CHOICE; the strict-branch count is threshold-relative while the INEQUALITY is
    # not. Recomputed from the stored connected tuples at 0.3 / 0.5 / 0.7.
    thr_detail = []
    thr_ineq_ok = True
    for thr in (0.3, 0.5, 0.7):
        exceptions = 0
        for row in main_rows:
            r_thr = sum(1 for c in row["connected"] if abs(c) > thr)
            if r_thr != 3 - row["B"]:
                exceptions += 1
            if r_thr > 3 - row["B"]:
                thr_ineq_ok = False
        thr_detail.append(f"|C|>{thr}: {exceptions} strict")
    check(
        "W4g threshold-relativity (panel edit): the strict-branch count is "
        "THRESHOLD-RELATIVE (counts per threshold reported) while the inequality "
        "R_b <= 3 - B_b holds at every probed threshold",
        thr_ineq_ok,
        "; ".join(thr_detail),
    )

    check(
        "W4d DEFICIT BOUND PER BRANCH",
        all(row["R"] <= 3 for row in main_rows),
        f"max R_b = {max(row['R'] for row in main_rows)} <= initial register deficit 3",
    )

    eps0_branches = run_model(0.0, initial="plus", branch=False)
    eps0_rows = branch_rows(eps0_branches)
    print_rows("\nCONTROL eps=0 no-branch linear ledger:", eps0_rows)
    eps0_row = eps0_rows[0]
    check(
        "W4e eps=0 single branch",
        len(eps0_rows) == 1,
        f"branches = {len(eps0_rows)}",
    )
    check(
        "W4e eps=0 landed linear ledger",
        eps0_row["R"] == 3 and eps0_row["B"] == 0 and abs(eps0_row["S"] - 3.0) <= 1e-12,
        f"R={eps0_row['R']}, S={eps0_row['S']:.17g}, B={eps0_row['B']}",
    )

    eps1_branches = run_model(1.0, initial="plus", branch=True, prune_zero=True)
    eps1_rows = branch_rows(eps1_branches)
    print_rows("\nCONTROL eps=1 projective nonzero branches:", eps1_rows)
    pointer_eigen = all(is_z_basis_pure(single_qubit_rho(row["state"], POINTER)) for row in eps1_rows)
    check(
        "W4e eps=1 projective branch support",
        len(eps1_rows) == 2 and abs(sum(row["weight"] for row in eps1_rows) - 1.0) <= WEIGHT_TOL,
        f"nonzero branches = {len(eps1_rows)}, paths = {[row['path'] for row in eps1_rows]}",
    )
    check(
        "W4e eps=1 pointer eigenstates",
        pointer_eigen,
        "all nonzero projective branches have Z-basis pure pointer marginals",
    )
    check(
        "W4e eps=1 deterministic copies have R_b=0",
        all(row["R"] == 0 for row in eps1_rows),
        f"R_b values = {[row['R'] for row in eps1_rows]}",
    )

    zero_branches = run_model(MAIN_EPS, initial="zero", branch=True, prune_zero=False)
    zero_rows = branch_rows(zero_branches)
    print_rows("\nCONTROL pointer initial |0>, eps=0.6:", zero_rows)
    check(
        "W4f pointer-eigenstate tree",
        len(zero_rows) == 8 and abs(sum(row["weight"] for row in zero_rows) - 1.0) <= WEIGHT_TOL,
        f"branches = {len(zero_rows)}, sum weights = {sum(row['weight'] for row in zero_rows):.17g}",
    )
    check(
        "W4f pointer-eigenstate initial condition",
        all(row["R"] == 0 for row in zero_rows),
        f"R_b values = {[row['R'] for row in zero_rows]}",
    )

    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        sys.exit(1)


if __name__ == "__main__":
    main()
