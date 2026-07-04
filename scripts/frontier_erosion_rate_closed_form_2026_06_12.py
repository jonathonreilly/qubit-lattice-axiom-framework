#!/usr/bin/env python3
"""Finite-dimensional verification for the source note

    docs/EROSION_GEOMETRIC_RATE_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-12.md

Scope: the uniform-sign geometric branch of the landed erosion recurrence.
The audit lane grades.

Run:
    python3 scripts/frontier_erosion_rate_closed_form_2026_06_12.py
"""

from __future__ import annotations

import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import sympy as sp


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "docs" / "EROSION_GEOMETRIC_RATE_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-12.md"
CACHE = REPO / "logs" / "runner-cache" / "frontier_erosion_rate_closed_form_2026_06_12.txt"

EPS_DOMAIN = (0, 1)

# Landed finite-tree constants mirrored for S0 anchors.
N_QUBITS = 4
N_FRAG = 3
DIM = 2**N_QUBITS
PHASE2_STEPS = 7

# S0 fixed anchors, frozen before evaluation.
ANCHOR_PATH_EPS = 0.6
ANCHOR_PATH_P0 = 0.6
ANCHOR_PATH_C0 = 0.64
ANCHOR_PATH_SIGNS = (1, -1, 1, -1, 1)
ANCHOR_PATH_PRODUCT_TOL = 1.0e-14
ANCHOR_FIRST_STEP_C = 0.22145328719723184
ANCHOR_FIRST_STEP_C_TOL = 1.0e-12
ANCHOR_RATE_EPS = 0.8
ANCHOR_FINITE_WINDOW_PRE_ASYMPTOTIC_LANDED_RATE_EPS08 = 0.3255283695
ANCHOR_LANDED_RATE_TOL = 1.0e-3
ANTI_FAB_EPS = 0.3
ANTI_FAB_STEPS = 4
ANTI_FAB_MIN_RANGE = 0.7

# S2 fixed grid and tolerances.
S2_EPS_GRID = (0.05, 0.1, 0.2, 0.3, 0.4)
S2_ASYMPTOTIC_STEPS = 800
S2_RATE_TOL = 1.0e-10
S2_PSTAR_TOL = 1.0e-12

# S3 fixed window gates.
LANDED_GEOMETRIC_EPS_LO = 0.5
LANDED_GEOMETRIC_EPS_HI = 0.8
CLOSED_RATE_AT_EPS_LO = 1.0 / 3.0
CLOSED_RATE_AT_EPS_HI = 1.0 / 9.0
S3_WINDOW_TOL = 1.0e-15
S3_MONOTONE_GRID = (0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8)

# S4 fixed counterexample.
MIXED_EPS = 0.2
MIXED_STEPS = 200
MIXED_RATE_UNIT_TOL = 1.0e-14
MIXED_UNIFORM_GAP_MIN = 0.1

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        print(f"PASS: {name}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL: {name}" + (f" :: {detail}" if detail else ""))


def section(name: str) -> None:
    print("=" * 78)
    print(name)
    print("=" * 78)


def bit(index: int, qubit: int, nqubits: int = N_QUBITS) -> int:
    return (index >> (nqubits - qubit - 1)) & 1


def flip_bit(index: int, qubit: int, nqubits: int = N_QUBITS) -> int:
    return index ^ (1 << (nqubits - qubit - 1))


def initial_state() -> np.ndarray:
    psi = np.zeros(DIM, dtype=complex)
    psi[0] = 1.0 / math.sqrt(2.0)
    psi[8] = 1.0 / math.sqrt(2.0)
    return psi


def cnot_pointer_to_fragment(psi: np.ndarray, frag: int) -> np.ndarray:
    target = 1 + frag
    out = np.zeros_like(psi)
    for i, amp in enumerate(psi):
        if bit(i, 0) == 1:
            out[flip_bit(i, target)] += amp
        else:
            out[i] += amp
    return out


def measure_fragment(psi: np.ndarray, frag: int, eps: float) -> list[tuple[float, np.ndarray]]:
    q = 1 + frag
    out: list[tuple[float, np.ndarray]] = []
    for y in (1.0, -1.0):
        phi = psi.copy()
        for i in range(DIM):
            z = 1.0 if bit(i, q) == 0 else -1.0
            phi[i] *= math.sqrt(max(0.0, (1.0 + y * eps * z) / 2.0))
        p = float(np.vdot(phi, phi).real)
        if p > 1.0e-15:
            out.append((p, phi / math.sqrt(p)))
    return out


def density(psi: np.ndarray) -> np.ndarray:
    return np.outer(psi, psi.conj())


def partial_trace(rho: np.ndarray, keep: list[int], nqubits: int = N_QUBITS) -> np.ndarray:
    tensor = rho.reshape([2] * (2 * nqubits))
    traced = [q for q in range(nqubits) if q not in keep]
    for q in sorted(traced, reverse=True):
        half = tensor.ndim // 2
        tensor = np.trace(tensor, axis1=q, axis2=q + half)
    dim = 2 ** len(keep)
    return tensor.reshape((dim, dim))


def entropy_bits(rho: np.ndarray) -> float:
    herm = 0.5 * (rho + rho.conj().T)
    vals = np.linalg.eigvalsh(herm)
    vals = np.clip(vals.real, 0.0, 1.0)
    vals = vals[vals > 1.0e-15]
    if vals.size == 0:
        return 0.0
    return float(-np.sum(vals * np.log2(vals)))


def mutual_information(rho: np.ndarray, a: list[int], b: list[int]) -> float:
    ab = sorted(a + b)
    return (
        entropy_bits(partial_trace(rho, a))
        + entropy_bits(partial_trace(rho, b))
        - entropy_bits(partial_trace(rho, ab))
    )


def branch_rbar(branches: list[tuple[float, np.ndarray]]) -> float:
    total = 0.0
    for w, psi in branches:
        rho = density(psi)
        total += w * float(
            np.mean([mutual_information(rho, [0], [1 + frag]) for frag in range(N_FRAG)])
        )
    return total


def advance_measure(
    branches: list[tuple[float, np.ndarray]], frag: int, eps: float
) -> list[tuple[float, np.ndarray]]:
    new: list[tuple[float, np.ndarray]] = []
    for w, psi in branches:
        for p, phi in measure_fragment(psi, frag, eps):
            new.append((w * p, phi))
    return new


def landed_rbar_trajectory(eps: float) -> list[float]:
    branches: list[tuple[float, np.ndarray]] = [(1.0, initial_state())]
    for frag in range(N_FRAG):
        branches = [(w, cnot_pointer_to_fragment(psi, frag)) for w, psi in branches]
        branches = advance_measure(branches, frag, eps)

    values = [branch_rbar(branches)]
    for step in range(PHASE2_STEPS):
        branches = advance_measure(branches, step % N_FRAG, eps)
        values.append(branch_rbar(branches))
    return values


def odd_step_geometric_rate(rbar: list[float]) -> float:
    odd_values = [rbar[t] for t in (1, 3, 5, 7)]
    ratios = [b / a for a, b in zip(odd_values[:-1], odd_values[1:])]
    return float(math.exp(sum(math.log(x) for x in ratios) / 3.0))


def next_p(p: float, eps: float, s: int) -> float:
    return (p + s * eps) / (1.0 + s * eps * p)


def c_factor(p: float, eps: float, s: int) -> float:
    return (1.0 - eps * eps) / (1.0 + s * eps * p) ** 2


def closed_rate(eps: float) -> float:
    return (1.0 - eps) / (1.0 + eps)


@dataclass(frozen=True)
class PathRun:
    p_values: tuple[float, ...]
    c_values: tuple[float, ...]
    factors: tuple[float, ...]
    product_c: float


def run_path(eps: float, p0: float, c0: float, signs: tuple[int, ...]) -> PathRun:
    p = p0
    c = c0
    p_values = [p]
    c_values = [c]
    factors = []
    for s in signs:
        factor = c_factor(p, eps, s)
        factors.append(factor)
        c *= factor
        p = next_p(p, eps, s)
        c_values.append(c)
        p_values.append(p)
    product_c = c0 * math.prod(factors)
    return PathRun(tuple(p_values), tuple(c_values), tuple(factors), product_c)


def s0_anchors() -> None:
    section("S0 anchors first")
    path = run_path(
        ANCHOR_PATH_EPS, ANCHOR_PATH_P0, ANCHOR_PATH_C0, ANCHOR_PATH_SIGNS
    )
    path_err = abs(path.c_values[-1] - path.product_c)
    first_step_err = abs(path.c_values[1] - ANCHOR_FIRST_STEP_C)
    print(
        "landed path-product anchor: "
        f"eps={ANCHOR_PATH_EPS}, p0={ANCHOR_PATH_P0}, c0={ANCHOR_PATH_C0}, "
        f"signs={ANCHOR_PATH_SIGNS}, c_final={path.c_values[-1]:.16g}"
    )
    check(
        "S0 internal consistency of the recurrence with its closed path product",
        path_err <= ANCHOR_PATH_PRODUCT_TOL,
        f"abs_err={path_err:.3e}, tol={ANCHOR_PATH_PRODUCT_TOL:.1e}",
    )
    check(
        "S0 landed eps=0.6 first-step branch value c=0.221453287197 is reproduced",
        first_step_err <= ANCHOR_FIRST_STEP_C_TOL,
        f"c1={path.c_values[1]:.16g}, err={first_step_err:.3e}",
    )

    anchor_rbar = landed_rbar_trajectory(ANCHOR_RATE_EPS)
    anchor_rate = odd_step_geometric_rate(anchor_rbar)
    asymptotic_rate_at_anchor_eps = closed_rate(ANCHOR_RATE_EPS)
    rate_err = abs(
        anchor_rate - ANCHOR_FINITE_WINDOW_PRE_ASYMPTOTIC_LANDED_RATE_EPS08
    )
    print(
        f"finite-window pre-asymptotic landed rate anchor: eps={ANCHOR_RATE_EPS}, "
        f"computed_r_eff={anchor_rate:.10f}, "
        "frozen="
        f"{ANCHOR_FINITE_WINDOW_PRE_ASYMPTOTIC_LANDED_RATE_EPS08:.10f}, "
        f"asymptotic_r={asymptotic_rate_at_anchor_eps:.10f}"
    )
    check(
        "S0 finite-window pre-asymptotic landed anchor (NOT the asymptotic closed form) at eps=0.8 is reproduced within 1e-3",
        rate_err <= ANCHOR_LANDED_RATE_TOL,
        (
            f"abs_err={rate_err:.3e}, "
            f"asymptotic_r(0.8)={asymptotic_rate_at_anchor_eps:.10f}"
        ),
    )

    anti = run_path(
        ANTI_FAB_EPS,
        0.0,
        1.0,
        tuple(1 for _ in range(ANTI_FAB_STEPS)),
    )
    p_range = max(anti.p_values) - min(anti.p_values)
    print(
        f"anti-fabrication p-trajectory: eps={ANTI_FAB_EPS}, "
        f"p_values={[round(x, 12) for x in anti.p_values]}"
    )
    check(
        "S0 anti-fabrication: exact p-trajectory is nonconstant before convergence",
        p_range >= ANTI_FAB_MIN_RANGE,
        f"range={p_range:.12f}",
    )


@dataclass(frozen=True)
class SymbolicDerivation:
    fixed_polynomial_plus: sp.Expr
    stable_plus: sp.Expr
    stable_minus: sp.Expr
    stability_plus: sp.Expr
    stability_minus: sp.Expr
    rate_plus: sp.Expr
    rate_minus: sp.Expr
    closed_form: sp.Expr


def symbolic_derivation() -> SymbolicDerivation:
    eps = sp.symbols("eps", positive=True)
    p = sp.symbols("p")
    rec_plus = (p + eps) / (1 + eps * p)
    rec_minus = (p - eps) / (1 - eps * p)

    fixed_num_plus = sp.factor(sp.together(p - rec_plus).as_numer_denom()[0])
    fixed_num_minus = sp.factor(sp.together(p - rec_minus).as_numer_denom()[0])
    roots_plus = tuple(sorted(sp.solve(sp.Eq(fixed_num_plus, 0), p), key=sp.default_sort_key))
    roots_minus = tuple(sorted(sp.solve(sp.Eq(fixed_num_minus, 0), p), key=sp.default_sort_key))

    deriv_plus = sp.diff(rec_plus, p)
    deriv_minus = sp.diff(rec_minus, p)
    probe_eps = sp.Rational(1, 5)
    stable_plus = min(
        roots_plus,
        key=lambda root: float(abs(deriv_plus.subs({eps: probe_eps, p: root}))),
    )
    stable_minus = min(
        roots_minus,
        key=lambda root: float(abs(deriv_minus.subs({eps: probe_eps, p: root}))),
    )

    rate_plus = sp.simplify((1 - eps**2) / (1 + eps * stable_plus) ** 2)
    rate_minus = sp.simplify((1 - eps**2) / (1 - eps * stable_minus) ** 2)
    stability_plus = sp.simplify(deriv_plus.subs(p, stable_plus))
    stability_minus = sp.simplify(deriv_minus.subs(p, stable_minus))
    closed_form = sp.simplify((1 - eps) / (1 + eps))
    return SymbolicDerivation(
        fixed_polynomial_plus=sp.factor(fixed_num_plus),
        stable_plus=sp.simplify(stable_plus),
        stable_minus=sp.simplify(stable_minus),
        stability_plus=stability_plus,
        stability_minus=stability_minus,
        rate_plus=rate_plus,
        rate_minus=rate_minus,
        closed_form=closed_form,
    )


def s1_symbolic() -> SymbolicDerivation:
    section("S1 sympy fixed point derivation")
    eps = sp.symbols("eps", positive=True)
    p = sp.symbols("p")
    deriv = symbolic_derivation()
    fixed_poly_err = sp.simplify(deriv.fixed_polynomial_plus - eps * (p**2 - 1))
    plus_p_err = sp.simplify(deriv.stable_plus - 1)
    minus_p_err = sp.simplify(deriv.stable_minus + 1)
    plus_rate_err = sp.simplify(deriv.rate_plus - deriv.closed_form)
    minus_rate_err = sp.simplify(deriv.rate_minus - deriv.closed_form)
    plus_stability_err = sp.simplify(deriv.stability_plus - deriv.closed_form)
    minus_stability_err = sp.simplify(deriv.stability_minus - deriv.closed_form)
    stability_gap = sp.simplify(1 - deriv.closed_form)
    print(
        "sympy result: "
        f"fixed_polynomial_plus={deriv.fixed_polynomial_plus}, "
        f"pstar_plus={deriv.stable_plus}, pstar_minus={deriv.stable_minus}, "
        f"|f'(p*)|={deriv.closed_form}, r(eps)={deriv.closed_form}"
    )
    check(
        "S1 fixed-point equation for s=+1 reduces to eps*(p^2-1)",
        fixed_poly_err == 0,
        f"simplify_diff={fixed_poly_err}",
    )
    check(
        "S1 sympy-selected attractive fixed points are p*=+1 for s=+1 and p*=-1 for s=-1",
        plus_p_err == 0 and minus_p_err == 0,
        f"plus_diff={plus_p_err}, minus_diff={minus_p_err}",
    )
    check(
        "S1 closed-form rate simplifies by sympy to (1-eps)/(1+eps) for both uniform signs",
        plus_rate_err == 0 and minus_rate_err == 0,
        f"plus_diff={plus_rate_err}, minus_diff={minus_rate_err}",
    )
    check(
        "S1 stability gate: |f'(p*)| = (1-eps)/(1+eps) < 1 on EPS_DOMAIN=(0,1)",
        plus_stability_err == 0
        and minus_stability_err == 0
        and stability_gap == sp.simplify(2 * eps / (1 + eps))
        and EPS_DOMAIN == (0, 1),
        (
            f"plus_diff={plus_stability_err}, minus_diff={minus_stability_err}, "
            f"one_minus_abs_deriv={stability_gap}"
        ),
    )
    return deriv


def asymptotic_uniform_rate(eps: float, steps: int) -> tuple[float, float]:
    p = 0.0
    rate = math.nan
    for _ in range(steps):
        rate = c_factor(p, eps, 1)
        p = next_p(p, eps, 1)
    return rate, p


def s2_numeric_grid() -> None:
    section("S2 exact-recursion asymptotic-rate grid")
    stability_grid_ok = True
    stability_grid_details = []
    for eps in S2_EPS_GRID:
        empirical, p_last = asymptotic_uniform_rate(eps, S2_ASYMPTOTIC_STEPS)
        theory = closed_rate(eps)
        derivative_at_pstar = c_factor(1.0, eps, 1)
        rate_err = abs(empirical - theory)
        p_err = abs(p_last - 1.0)
        deriv_err = abs(derivative_at_pstar - theory)
        stability_grid_ok = (
            stability_grid_ok
            and EPS_DOMAIN[0] < eps < EPS_DOMAIN[1]
            and deriv_err <= S2_RATE_TOL
            and 0.0 < derivative_at_pstar < 1.0
        )
        stability_grid_details.append(f"{eps:g}:{derivative_at_pstar:.12g}")
        print(
            f"eps={eps:.2f}: empirical_rate={empirical:.16g}, "
            f"closed_rate={theory:.16g}, |f'(p*)|={derivative_at_pstar:.16g}, "
            f"p_last={p_last:.16g}"
        )
        check(
            f"S2 eps={eps:.2f}: empirical asymptotic rate equals closed form within 1e-10",
            rate_err <= S2_RATE_TOL,
            f"abs_err={rate_err:.3e}",
        )
        check(
            f"S2 eps={eps:.2f}: p_j converges to p*=1 within 1e-12",
            p_err <= S2_PSTAR_TOL,
            f"abs_err={p_err:.3e}",
        )
    check(
        "S2 numeric stability gate on fixed eps grid: 0 < |f'(p*)| = (1-eps)/(1+eps) < 1",
        stability_grid_ok,
        "abs_deriv_grid={" + ", ".join(stability_grid_details) + "}",
    )


def inverse_closed_rate(rate: float) -> float:
    return (1.0 - rate) / (1.0 + rate)


def s3_window_and_monotone() -> None:
    section("S3 landed window and decreasing-rate tie")
    rate_at_lo = closed_rate(LANDED_GEOMETRIC_EPS_LO)
    rate_at_hi = closed_rate(LANDED_GEOMETRIC_EPS_HI)
    inverse_lo = inverse_closed_rate(CLOSED_RATE_AT_EPS_LO)
    inverse_hi = inverse_closed_rate(CLOSED_RATE_AT_EPS_HI)
    print(
        "landed moderate eps window [0.5, 0.8] maps under r(eps) "
        f"to [{rate_at_hi:.16g}, {rate_at_lo:.16g}]"
    )
    check(
        "S3 fixed interval: eps in [0.5,0.8] corresponds to r in [1/9,1/3]",
        abs(rate_at_lo - CLOSED_RATE_AT_EPS_LO) <= S3_WINDOW_TOL
        and abs(rate_at_hi - CLOSED_RATE_AT_EPS_HI) <= S3_WINDOW_TOL
        and abs(inverse_lo - LANDED_GEOMETRIC_EPS_LO) <= S3_WINDOW_TOL
        and abs(inverse_hi - LANDED_GEOMETRIC_EPS_HI) <= S3_WINDOW_TOL,
        (
            f"r(0.5)={rate_at_lo:.16g}, r(0.8)={rate_at_hi:.16g}, "
            f"inv(1/3)={inverse_lo:.16g}, inv(1/9)={inverse_hi:.16g}"
        ),
    )
    rates = [closed_rate(eps) for eps in S3_MONOTONE_GRID]
    monotone = all(a > b for a, b in zip(rates[:-1], rates[1:]))
    print(
        "monotone tie grid: "
        + ", ".join(f"r({eps:g})={rate:.12g}" for eps, rate in zip(S3_MONOTONE_GRID, rates))
    )
    check(
        "S3 r(eps) is decreasing on the fixed eps grid, matching the landed eta direction",
        monotone,
        f"rates={[round(x, 12) for x in rates]}",
    )


def mixed_alternating_rate(eps: float, steps: int) -> tuple[float, float]:
    p = 0.0
    log_factor_sum = 0.0
    for j in range(steps):
        s = 1 if j % 2 == 0 else -1
        factor = c_factor(p, eps, s)
        log_factor_sum += math.log(factor)
        p = next_p(p, eps, s)
    return math.exp(log_factor_sum / steps), p


def s4_boundary() -> None:
    section("S4 mixed-sign boundary of validity")
    eps = sp.symbols("eps", positive=True)
    p0 = sp.Integer(0)
    p1 = sp.simplify((p0 + eps) / (1 + eps * p0))
    factor1 = sp.simplify((1 - eps**2) / (1 + eps * p0) ** 2)
    factor2 = sp.simplify((1 - eps**2) / (1 - eps * p1) ** 2)
    two_step_product_err = sp.simplify(factor1 * factor2 - 1)
    mixed_rate, p_last = mixed_alternating_rate(MIXED_EPS, MIXED_STEPS)
    uniform = closed_rate(MIXED_EPS)
    unit_err = abs(mixed_rate - 1.0)
    gap = abs(mixed_rate - uniform)
    print(
        f"mixed-sign counterexample: eps={MIXED_EPS}, signs=+-+-..., "
        f"measured_rate={mixed_rate:.16g}, uniform_closed_rate={uniform:.16g}, "
        f"p_last={p_last:.16g}"
    )
    check(
        "S4 sympy identity: alternating two-step c-factor product is exactly 1",
        two_step_product_err == 0 and EPS_DOMAIN == (0, 1),
        f"factor1={factor1}, factor2={factor2}, product_minus_1={two_step_product_err}",
    )
    check(
        "S4 alternating branch has measured two-step geometric rate 1, not the uniform-sign rate",
        unit_err <= MIXED_RATE_UNIT_TOL and gap >= MIXED_UNIFORM_GAP_MIN,
        f"unit_err={unit_err:.3e}, gap={gap:.3e}",
    )


def s5_note_hygiene() -> None:
    section("S5 note hygiene")
    note = NOTE.read_text(encoding="utf-8")
    note_norm = " ".join(note.split())
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", note)
    expected_links = [
        (
            "`EROSION_EXACT_RECURRENCE_PATH_PRODUCT_THRESHOLD_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-06-12.md`",
            "EROSION_EXACT_RECURRENCE_PATH_PRODUCT_THRESHOLD_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-06-12.md",
        ),
        (
            "`EROSION_RATE_TABLE_NO_TESTED_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-12.md`",
            "EROSION_RATE_TABLE_NO_TESTED_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-12.md",
        ),
    ]
    check(
        "S5 canonical claim type and status-authority front matter are present",
        "**Claim type:** bounded_theorem" in note
        and "**Status authority:** independent audit lane" in note
        and "**No-promotion statement:**" in note
        and f"**Primary runner:** `{Path(__file__).relative_to(REPO)}`" in note
        and f"**Runner cache:** `{CACHE.relative_to(REPO)}`" in note
        and "**Type:**" not in note
        and "audit lane grades" not in note.lower(),
    )
    check(
        "S5 dependency links are exactly the landed erosion predecessors",
        links == expected_links,
        f"links={links}",
    )
    check(
        "S5 scope remains the uniform-sign branch and excludes mixed paths",
        "Scope is the uniform-sign geometric branch" in note_norm
        and "It does not claim a closed form for the nonlinear threshold-count envelope" in note_norm
        and "mixed-sign paths" in note_norm,
    )
    check(
        "S5 no new axiom, primitive, measure, weighting, normalization, or probability rule is imported",
        "imports no new axiom, primitive, measure, weighting, normalization, or probability rule"
        in note_norm,
    )
    check(
        "S5 note, runner, and cache all exist in this spec path set",
        _touched_spec_files_ok(),
    )


def _touched_spec_files_ok() -> bool:
    import subprocess

    status = subprocess.run(
        [
            "git",
            "status",
            "--short",
            "--",
            str(NOTE.relative_to(REPO)),
            str(Path(__file__).relative_to(REPO)),
            str(CACHE.relative_to(REPO)),
        ],
        cwd=REPO,
        check=False,
        text=True,
        capture_output=True,
    )
    touched = [line for line in status.stdout.splitlines() if line.strip()]
    print(f"  [info] landing-time git status for the spec path set: {touched!r}")
    return NOTE.is_file() and Path(__file__).is_file() and CACHE.is_file()


def main() -> int:
    print("Uniform-sign closed-form erosion-rate verification")
    print("Recurrence: p_s=(p+s eps)/(1+s eps p), c_s=c*(1-eps^2)/(1+s eps p)^2")
    s0_anchors()
    s1_symbolic()
    s2_numeric_grid()
    s3_window_and_monotone()
    s4_boundary()
    s5_note_hygiene()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
