#!/usr/bin/env python3
"""Class-A exact verification for the sampled-grid trend toward the projective endpoint
(eps=1 exact control).

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_branching_slack_rate_eps_2026_06_12.py
"""
import math
import sys
from dataclasses import dataclass

import numpy as np


NFRAGS = (3, 4, 5)
EPS_GRID = (0.3, 0.6, 0.9, 0.95, 0.99)
STRICT_INCREASE_EPS_GRID = (0.3, 0.6, 0.9)
CONTROL_EPS = (0.0, 1.0)
THRESHOLDS = (0.3, 0.5, 0.7)
MAIN_THRESHOLD = 0.5
ZERO_WEIGHT_TOL = 1.0e-14
PURE_TOL = 1.0e-12
ENTROPY_TOL = 1.0e-9
RATE_CLOSENESS_BOUNDS = {
    0.9: 0.0136,
    0.99: 0.000149,
}

CHECK_RESULTS = []


@dataclass(frozen=True)
class BranchStats:
    path: str
    weight: float
    z_pointer: float
    blanks: int
    records: dict
    slack: int
    marginal_sum_entropy: float


@dataclass(frozen=True)
class Analysis:
    nfrag: int
    eps: float
    initial_pointer: str
    branches: tuple
    zero_weight_branches: int
    total_weight: float


def check(name, condition, detail):
    ok = bool(condition)
    CHECK_RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}: {detail}")


def bit_z_values(size, bit):
    idx = np.arange(size, dtype=np.uint64)
    return np.where((idx & (1 << bit)) == 0, 1.0, -1.0)


def initial_state(nfrag, pointer):
    size = 1 << (nfrag + 1)
    state = np.zeros(size, dtype=np.float64)
    if pointer == "plus":
        state[0] = 1.0 / math.sqrt(2.0)
        state[1] = 1.0 / math.sqrt(2.0)
    elif pointer == "zero":
        state[0] = 1.0
    else:
        raise ValueError(f"unknown pointer initial state: {pointer}")
    return state


def apply_cnot_pointer_to_fragment(state, frag):
    size = state.size
    idx = np.arange(size, dtype=np.uint64)
    target_mask = np.uint64(1 << (frag + 1))
    pointer_is_one = (idx & np.uint64(1)) != 0
    out_idx = np.where(pointer_is_one, idx ^ target_mask, idx).astype(np.int64)
    out = np.empty_like(state)
    out[out_idx] = state
    return out


def apply_weak_kraus(state, eps, outcome):
    z_pointer = bit_z_values(state.size, 0)
    raw = (1.0 + outcome * eps * z_pointer) / 2.0
    factors = np.sqrt(np.maximum(raw, 0.0))
    return state * factors


def build_tree(nfrag, eps, pointer="plus"):
    branches = [("", initial_state(nfrag, pointer))]
    for frag in range(nfrag):
        next_branches = []
        for path, state in branches:
            broadcast = apply_cnot_pointer_to_fragment(state, frag)
            for label, outcome in (("+", 1.0), ("-", -1.0)):
                next_branches.append((path + label, apply_weak_kraus(broadcast, eps, outcome)))
        branches = next_branches
    return branches


def z_expectation(state, bit):
    prob = state * state
    return float(np.dot(prob, bit_z_values(state.size, bit)))


def zz_expectation(state, bit_a, bit_b):
    prob = state * state
    za = bit_z_values(state.size, bit_a)
    zb = bit_z_values(state.size, bit_b)
    return float(np.dot(prob, za * zb))


def prob_one(state, bit):
    prob = state * state
    idx = np.arange(state.size, dtype=np.uint64)
    mask = np.uint64(1 << bit)
    return float(np.sum(prob[(idx & mask) != 0]))


def connected_correlators(state, nfrag):
    zp = z_expectation(state, 0)
    vals = []
    for frag in range(nfrag):
        bit = frag + 1
        zf = z_expectation(state, bit)
        vals.append(zz_expectation(state, 0, bit) - zp * zf)
    return vals


def record_count(state, nfrag, threshold):
    return sum(1 for c in connected_correlators(state, nfrag) if abs(c) > threshold)


def blank_count(state, nfrag):
    # A blank is the original fragment state |0>: Z-pure with no |1> weight.
    return sum(1 for frag in range(nfrag) if prob_one(state, frag + 1) <= PURE_TOL)


def entropy_bits(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def marginal_sum_entropy(state, nfrag):
    total = 0.0
    for frag in range(nfrag):
        total += entropy_bits(prob_one(state, frag + 1))
    return total


def analyze(nfrag, eps, pointer="plus"):
    stats = []
    total_weight = 0.0
    zero_weight = 0
    for path, state in build_tree(nfrag, eps, pointer):
        weight = float(np.dot(state, state))
        if weight <= ZERO_WEIGHT_TOL:
            zero_weight += 1
            continue
        total_weight += weight
        norm_state = state / math.sqrt(weight)
        records = {threshold: record_count(norm_state, nfrag, threshold) for threshold in THRESHOLDS}
        blanks = blank_count(norm_state, nfrag)
        slack = (nfrag - blanks) - records[MAIN_THRESHOLD]
        stats.append(
            BranchStats(
                path=path,
                weight=weight,
                z_pointer=z_expectation(norm_state, 0),
                blanks=blanks,
                records=records,
                slack=slack,
                marginal_sum_entropy=marginal_sum_entropy(norm_state, nfrag),
            )
        )
    return Analysis(
        nfrag=nfrag,
        eps=eps,
        initial_pointer=pointer,
        branches=tuple(stats),
        zero_weight_branches=zero_weight,
        total_weight=total_weight,
    )


def weighted_slack(analysis, threshold=MAIN_THRESHOLD):
    nfrag = analysis.nfrag
    return sum(b.weight * ((nfrag - b.blanks) - b.records[threshold]) for b in analysis.branches)


def weighted_marginal_sum_entropy(analysis):
    return sum(b.weight * b.marginal_sum_entropy for b in analysis.branches)


def fmt(x):
    return f"{x:.6f}"


def fmt12(x):
    return f"{x:.12f}"


def fmt_eps(eps):
    return f"{eps:.2f}".rstrip("0").rstrip(".")


def print_scope():
    print(
        "SCOPE: broadcast+weak-measurement model, exact trees; "
        "the sampled-grid trend toward the projective endpoint (eps=1 exact control); "
        "the slack table and its eps/NFRAG patterns are the data; "
        "threshold-relativity probed; NOT claimed: thermodynamic specialness, "
        "measures over states, other dynamics; Born cap inherited."
    )


def print_slack_table(analyses):
    print("\nSLACK TABLE (threshold |C| > 0.5; S=sum_b w_b s_b)")
    header_cells = [f"eps={fmt_eps(eps)} S/rate".ljust(20) for eps in EPS_GRID]
    print("NFRAG  " + " ".join(header_cells))
    for nfrag in NFRAGS:
        cells = []
        for eps in EPS_GRID:
            s_val = weighted_slack(analyses[(nfrag, eps)])
            cells.append(f"{fmt(s_val)}/{fmt(s_val / nfrag)}".ljust(20))
        print(f"{nfrag:5d}  " + " ".join(cells))


def print_threshold_table(analyses):
    print("\nTHRESHOLD-RELATIVITY TABLE (weighted slack; columns are |C| thresholds)")
    print("NFRAG  eps    t=0.3     t=0.5     t=0.7")
    for nfrag in NFRAGS:
        for eps in EPS_GRID:
            analysis = analyses[(nfrag, eps)]
            cells = [fmt(weighted_slack(analysis, t)) for t in THRESHOLDS]
            print(f"{nfrag:5d}  {fmt_eps(eps):>5s}  {cells[0]:>8s}  {cells[1]:>8s}  {cells[2]:>8s}")


def describe_branch(analysis, branch):
    return (
        f"N={analysis.nfrag} eps={fmt_eps(analysis.eps)} path={branch.path} "
        f"B={branch.blanks} R={branch.records[MAIN_THRESHOLD]} slack={branch.slack}"
    )


def run_x4a(analyses):
    max_gap = -10**9
    worst = None
    cases = 0
    min_main_slack = 10**9
    for analysis in analyses.values():
        nfrag = analysis.nfrag
        for branch in analysis.branches:
            rhs = nfrag - branch.blanks
            min_main_slack = min(min_main_slack, rhs - branch.records[MAIN_THRESHOLD])
            for threshold in THRESHOLDS:
                cases += 1
                gap = branch.records[threshold] - rhs
                if gap > max_gap:
                    max_gap = gap
                    worst = (
                        analysis,
                        branch,
                        threshold,
                        branch.records[threshold],
                        rhs,
                    )
    detail = (
        f"universal R_b <= NFRAG-B_b over {cases} branch-threshold cases; "
        f"max(R-rhs)={max_gap}; min main slack={min_main_slack}; "
        f"worst={describe_branch(worst[0], worst[1])} threshold={worst[2]:.1f} "
        f"R={worst[3]} rhs={worst[4]}"
    )
    check("X4a branch budget inequality at thresholds 0.3/0.5/0.7", max_gap <= 0, detail)


def run_x4b(analyses):
    rows = []
    monotone = True
    for nfrag in NFRAGS:
        vals = [weighted_slack(analyses[(nfrag, eps)]) for eps in STRICT_INCREASE_EPS_GRID]
        row_ok = all(a < b for a, b in zip(vals, vals[1:]))
        monotone = monotone and row_ok
        eps_vals = ", ".join(
            f"eps={fmt_eps(eps)} S={fmt(val)}" for eps, val in zip(STRICT_INCREASE_EPS_GRID, vals)
        )
        rows.append(f"N={nfrag}: {eps_vals}")
    detail = "strict increase with eps at fixed NFRAG on eps=0.3/0.6/0.9; " + " | ".join(rows)
    check(
        "X4b weighted mean slack strictly increasing on the sampled eps grid eps=0.3/0.6/0.9",
        monotone,
        detail,
    )


def run_x4c(analyses):
    rate_rows = []
    for eps in EPS_GRID:
        rates = np.array([weighted_slack(analyses[(nfrag, eps)]) / nfrag for nfrag in NFRAGS])
        rate_devs = np.abs(rates - 1.0)
        max_dev = float(np.max(rate_devs))
        bound_text = ""
        if eps in RATE_CLOSENESS_BOUNDS:
            bound_text = f" bound<{fmt12(RATE_CLOSENESS_BOUNDS[eps])}"
        per_nfrag = "; ".join(
            f"N={nfrag} rate={fmt12(float(rate))} |rate-1|={fmt12(float(dev))}"
            for nfrag, rate, dev in zip(NFRAGS, rates, rate_devs)
        )
        rate_rows.append(
            f"eps={fmt_eps(eps)} max|rate-1|={fmt12(max_dev)}{bound_text} [{per_nfrag}]"
        )
    closeness_holds = all(
        max(
            abs(weighted_slack(analyses[(nfrag, eps)]) / nfrag - 1.0)
            for nfrag in NFRAGS
        )
        < bound
        for eps, bound in RATE_CLOSENESS_BOUNDS.items()
    )
    detail = (
        "sampled-grid trend toward the projective endpoint (eps=1 exact control): "
        "eps=0.9 max |rate-1| < 0.0136 and eps=0.99 max |rate-1| < 0.000149; "
        + " | ".join(rate_rows)
    )
    check(
        "X4c eps=0.9 max |rate-1| < 0.0136 and eps=0.99 max |rate-1| < 0.000149 over sampled NFRAG",
        closeness_holds,
        detail,
    )


def run_x4d(all_plus_analyses):
    max_excess = -10**9
    worst = None
    max_norm_error = 0.0
    for analysis in all_plus_analyses.values():
        entropy = weighted_marginal_sum_entropy(analysis)
        excess = entropy - analysis.nfrag
        norm_error = abs(analysis.total_weight - 1.0)
        max_norm_error = max(max_norm_error, norm_error)
        if excess > max_excess:
            max_excess = excess
            worst = (analysis, entropy)
    detail = (
        f"max(weighted marginal-sum entropy - NFRAG)={max_excess:.12g} "
        f"at N={worst[0].nfrag} eps={fmt_eps(worst[0].eps)} entropy={worst[1]:.12g}; "
        f"max Born-weight normalization error={max_norm_error:.12g}"
    )
    condition = max_excess <= ENTROPY_TOL and max_norm_error <= ENTROPY_TOL
    check("X4d weighted marginal-sum entropy bound", condition, detail)


def run_x4e_eps0(eps0_analyses):
    max_abs_slack = 0
    min_records = 10**9
    max_blanks = 0
    for analysis in eps0_analyses.values():
        for branch in analysis.branches:
            max_abs_slack = max(max_abs_slack, abs(branch.slack))
            min_records = min(min_records, branch.records[MAIN_THRESHOLD])
            max_blanks = max(max_blanks, branch.blanks)
    detail = (
        f"eps=0 recovers R_b=NFRAG and B_b=0 on every active branch; "
        f"max |slack|={max_abs_slack}, min R={min_records}, max B={max_blanks}"
    )
    check("X4e control eps=0 linear ledger", max_abs_slack == 0 and max_blanks == 0, detail)


def run_x4e_eps1(eps1_analyses):
    eigen_ok = True
    record_ok = True
    slack_identity_ok = True
    reports = []
    for analysis in eps1_analyses.values():
        branch_reports = []
        for branch in analysis.branches:
            eigen_ok = eigen_ok and abs(abs(branch.z_pointer) - 1.0) <= PURE_TOL
            record_ok = record_ok and all(branch.records[t] == 0 for t in THRESHOLDS)
            slack_identity_ok = slack_identity_ok and branch.slack == analysis.nfrag - branch.blanks
            branch_reports.append(f"{branch.path}:B={branch.blanks},s={branch.slack}")
        reports.append(f"N={analysis.nfrag} active={len(analysis.branches)} {' '.join(branch_reports)}")
    detail = (
        "eps=1 active branches are pointer Z-eigenstates with R_b=0; "
        "reported slack=NFRAG-B_b; " + " | ".join(reports)
    )
    check("X4e control eps=1 eigenstate branches", eigen_ok and record_ok and slack_identity_ok, detail)


def run_x4e_pointer0(pointer0_analyses):
    max_record = 0
    min_blanks = 10**9
    for analysis in pointer0_analyses.values():
        for branch in analysis.branches:
            max_record = max(max_record, max(branch.records.values()))
            min_blanks = min(min_blanks, branch.blanks)
    detail = (
        "|0>-pointer control has zero connected-correlator records at all thresholds; "
        f"max R={max_record}, min B={min_blanks}"
    )
    check("X4e control |0>-pointer zero records", max_record == 0, detail)


def main():
    print_scope()

    main_analyses = {(nfrag, eps): analyze(nfrag, eps, "plus") for nfrag in NFRAGS for eps in EPS_GRID}
    eps0_analyses = {(nfrag, 0.0): analyze(nfrag, 0.0, "plus") for nfrag in NFRAGS}
    eps1_analyses = {(nfrag, 1.0): analyze(nfrag, 1.0, "plus") for nfrag in NFRAGS}
    all_plus_analyses = dict(main_analyses)
    all_plus_analyses.update(eps0_analyses)
    all_plus_analyses.update(eps1_analyses)
    pointer0_analyses = {
        (nfrag, eps): analyze(nfrag, eps, "zero")
        for nfrag in NFRAGS
        for eps in (0.0,) + EPS_GRID + (1.0,)
    }

    print_slack_table(main_analyses)
    print_threshold_table(main_analyses)
    print()

    run_x4a(main_analyses)
    run_x4b(main_analyses)
    run_x4c(main_analyses)
    run_x4d(all_plus_analyses)
    run_x4e_eps0(eps0_analyses)
    run_x4e_eps1(eps1_analyses)
    run_x4e_pointer0(pointer0_analyses)

    passes = sum(1 for ok in CHECK_RESULTS if ok)
    fails = len(CHECK_RESULTS) - passes
    print(f"TOTAL: PASS={passes} FAIL={fails}")
    if fails:
        sys.exit(1)


if __name__ == "__main__":
    main()
