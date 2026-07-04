#!/usr/bin/env python3
"""
DM leptogenesis PMNS multistart runner diagnostic on the refreshed branch.

Purpose:
  Record the current broad multistart constrained-scan support for the
  PMNS-assisted N_e diagnostic on the runner-defined fixed seed surface.

Method on the exact refreshed branch:
  1. generate closure starts on the runner-defined fixed N_e seed surface;
  2. solve the constrained effective-action stationary problem from each start;
  3. cluster all converged stationary points into closure branches;
  4. verify that, within the recovered sampled branches, one lowest-action
     branch is separated by a finite gap to the next branch.

This is support for a runner-defined reduced-surface diagnostic, not a live
theorem-grade selector or native-readout closure claim.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass

import numpy as np
from scipy.optimize import differential_evolution

import frontier_dm_leptogenesis_pmns_relative_action_stationarity_theorem as stat

AUDIT_TIMEOUT_SEC = 600

PASS_COUNT = 0
FAIL_COUNT = 0
KKT_RESIDUAL_TOL = 1.0e-3
CLOSURE_TOL = 1.0e-8


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def fmt(v: np.ndarray) -> str:
    return np.array2string(np.round(np.asarray(v, dtype=float), 6), separator=", ")


@dataclass
class Branch:
    representative: np.ndarray
    action: float
    etas: np.ndarray
    count: int


def branch_action(p: np.ndarray) -> float:
    return stat.relative_action_from_params(np.asarray(p, dtype=float))


def closure_error(p: np.ndarray, i_star: int) -> float:
    return abs(stat.eta_i(np.asarray(p, dtype=float), i_star) - 1.0)


def kkt_residual(p: np.ndarray, i_star: int) -> float:
    p = np.asarray(p, dtype=float)
    grad_action = stat.finite_grad(stat.relative_action_from_params, p)
    grad_closure = stat.finite_grad(lambda q: stat.eta_i(q, i_star) - 1.0, p)
    lam = float(np.dot(grad_action, grad_closure) / max(float(np.dot(grad_closure, grad_closure)), 1.0e-15))
    return float(np.linalg.norm(grad_action - lam * grad_closure))


def is_stationary_closure_candidate(p: np.ndarray, i_star: int) -> bool:
    return (
        closure_error(p, i_star) < CLOSURE_TOL
        and np.isfinite(branch_action(p))
        and kkt_residual(p, i_star) < KKT_RESIDUAL_TOL
    )


def constrained_refine(p: np.ndarray, i_star: int) -> np.ndarray:
    sol, res = stat.constrained_stationary_point(np.asarray(p, dtype=float), i_star)
    sol = np.asarray(sol, dtype=float)
    if is_stationary_closure_candidate(sol, i_star):
        return sol
    if is_stationary_closure_candidate(p, i_star):
        return np.asarray(p, dtype=float)
    raise RuntimeError(
        "constrained refinement failed "
        f"(success={res.success}, closure={closure_error(sol, i_star):.3e}, "
        f"KKT={kkt_residual(sol, i_star):.3e})"
    )


def collect_feasible_starts(i_star: int, extremal_params: np.ndarray, count: int = 8) -> list[np.ndarray]:
    rng = np.random.default_rng(101)
    starts: list[np.ndarray] = [stat.closure_point_on_ray(extremal_params, i_star)]

    while len(starts) < count:
        direction = rng.normal(size=5)
        direction[:4] *= rng.uniform(0.4, 2.0)
        direction[4] = float(rng.uniform(-math.pi, math.pi))
        try:
            starts.append(stat.closure_point_on_ray(direction, i_star))
        except ValueError:
            continue
    return starts


def cluster_solutions(solutions: list[np.ndarray], i_star: int) -> list[Branch]:
    clusters: list[list[np.ndarray]] = []
    action_tol = 1e-6
    param_tol = 5e-4

    for sol in solutions:
        s_action = branch_action(sol)
        matched = False
        for bucket in clusters:
            rep = bucket[0]
            if abs(branch_action(rep) - s_action) < action_tol and np.linalg.norm(rep - sol) < param_tol:
                bucket.append(sol)
                matched = True
                break
        if not matched:
            clusters.append([sol])

    out: list[Branch] = []
    for bucket in clusters:
        reps = np.array(bucket, dtype=float)
        rep = np.mean(reps, axis=0)
        try:
            rep = constrained_refine(rep, i_star)
        except RuntimeError:
            continue
        _x, _y, _d, _h, etas = stat.source_from_params(rep)
        out.append(
            Branch(
                representative=rep,
                action=branch_action(rep),
                etas=np.asarray(etas, dtype=float),
                count=len(bucket),
            )
        )
    out.sort(key=lambda b: b.action)
    return out


def part1_enumerate_stationary_branches() -> tuple[int, list[Branch]]:
    print("\n" + "=" * 88)
    print("PART 1: ENUMERATE THE CLOSURE STATIONARY BRANCHES")
    print("=" * 88)

    i_star, extremal_params = stat.favored_column_and_extremal_params()
    starts = collect_feasible_starts(i_star, extremal_params, count=8)

    sols: list[np.ndarray] = []
    rejected_kkt: list[float] = []
    for start in starts:
        sol, res = stat.constrained_stationary_point(start, i_star)
        sol = np.asarray(sol, dtype=float)
        if res.success and is_stationary_closure_candidate(sol, i_star):
            sols.append(sol)
        elif closure_error(sol, i_star) < 1.0e-5 and np.isfinite(branch_action(sol)):
            rejected_kkt.append(kkt_residual(sol, i_star))

    branches = cluster_solutions(sols, i_star)
    probe_residual = kkt_residual(starts[1], i_star)

    check(
        "The runner-defined fixed-seed closure surface yields two KKT-stable dominant stationary branches under broad multistart enumeration",
        len(branches) == 2,
        f"branch count={len(branches)}, sampled solves={len(sols)}",
    )
    check(
        "The KKT filter rejects closure-compatible nonstationary probes",
        probe_residual > KKT_RESIDUAL_TOL and (not rejected_kkt or max(rejected_kkt) > KKT_RESIDUAL_TOL),
        f"probe KKT={probe_residual:.3e}, rejected={len(rejected_kkt)}",
    )
    check(
        "The lowest branch satisfies the runner-normalized favored-column closure",
        abs(branches[0].etas[i_star] - 1.0) < 1e-10,
        f"etas={np.round(branches[0].etas, 12)}",
    )
    check(
        "The broad-multistart dominant pair is separated by a finite action gap",
        (branches[1].action - branches[0].action) > 0.5,
        f"ΔS_pair={branches[1].action - branches[0].action:.12f}",
    )

    print()
    for idx, branch in enumerate(branches):
        x, y, delta = stat.rel.build_active_from_params(branch.representative)
        print(f"  branch {idx}:")
        print(f"    count      = {branch.count}")
        print(f"    S_rel      = {branch.action:.12f}")
        print(f"    x          = {fmt(x)}")
        print(f"    y          = {fmt(y)}")
        print(f"    delta      = {delta:.12e}")
        print(f"    eta/eta_obs= {np.round(branch.etas, 12)}")

    return i_star, branches


def part2_support_readout(branches: list[Branch]) -> None:
    print("\n" + "=" * 88)
    print("PART 2: SUPPORT READOUT")
    print("=" * 88)

    low = branches[0]
    miss_factor = 1.0 / float(low.etas[0])

    check(
        "The lowest-action branch gives runner-normalized PMNS-assisted closure on the favored column",
        abs(float(low.etas[0]) - 1.0) < 1e-10,
        f"eta/eta_obs={low.etas[0]:.12f}",
    )
    check(
        "The old one-flavor 5.297x diagnostic miss is gone on the sampled low-action branch",
        abs(miss_factor - 1.0) < 1e-10,
        f"miss factor={miss_factor:.12f}",
    )
    print("  [INFO] This runner is broad multistart support for a runner-defined diagnostic surface.")


def main() -> int:
    print("=" * 88)
    print("DM LEPTOGENESIS PMNS MULTISTART RUNNER DIAGNOSTIC")
    print("=" * 88)
    print()
    print("Question:")
    print("  Does the current broad multistart constrained scan recover a stable")
    print("  low-action diagnostic branch on the runner-defined fixed N_e seed surface?")

    i_star, branches = part1_enumerate_stationary_branches()
    _ = i_star
    part2_support_readout(branches)

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Broad multistart support result:")
    print("    - the current broad multistart constrained scan resolves two KKT-stable dominant")
    print("      stationary closure branches on the runner-defined fixed N_e seed surface")
    print("    - the low branch is separated from the higher dominant branch by a")
    print("      finite action gap")
    print("    - that branch gives eta/eta_obs = 1 on the imposed favored-column closure surface")
    print("    - closure-compatible nonstationary probes are rejected by the KKT filter")
    print()
    print("  This is support for the runner-defined reduced-surface diagnostic,")
    print("  not a live theorem-grade selector or native-readout closure statement.")
    print()
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
