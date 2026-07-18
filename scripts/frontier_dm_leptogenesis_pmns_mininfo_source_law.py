#!/usr/bin/env python3
"""
DM leptogenesis PMNS minimum-information selector diagnostic.

Framework baseline:
  Lattice + Qubit + Admissibility + Record, with the one-qubit operator algebra
  on the Z^3 lattice.

Scope (open gate / conditional diagnostic):
  This runner verifies the consequences of *adopting* a downstream selector
  law. The selector itself is an explicit definition imported from
  information geometry; it is NOT derived from the current four-axiom
  baseline.

  IF the minimum-information selector law (below) is adopted as a downstream
  definition on a fixed supplied seed surface and at a supplied column index,
  THEN the runner finds a reproducible feasible locally stationary off-seed
  candidate after imposing eta_{i_*}/eta_obs = 1.

Law (adopted definition):
  1. keep the supplied seed pair (xbar, ybar) fixed
  2. adopt the supplied finite-fixture column index i_* = 0
  3. seek local stationary candidates among positive off-seed sources on that
     fixed seed surface satisfying
       eta_{i_*} / eta_obs = 1,
     using the information-deformation cost

       I_seed = D_KL(x/sum(x) || x_seed/sum(x_seed))
              + D_KL(y/sum(y) || y_seed/sum(y_seed)) + (1 - cos delta).

What this runner does NOT prove:
  - that I_seed follows from the current four-axiom baseline
  - that I_seed is the unique correct selector or that comparisons with other
    supplied objectives provide selector authority
  - baseline-framework closure for the PMNS-assisted N_e branch

This yields a reproducible low-deformation feasible local candidate on the
supplied fixture CONDITIONAL on adopting I_seed and i_* = 0. It does not prove
global minimality or uniqueness, theorem-grade selector authority, a physical
column choice, or a baseline-framework selector derivation.
"""

from __future__ import annotations

import math
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import brentq, differential_evolution, minimize

from dm_leptogenesis_exact_common import (
    C_SPH,
    D_THERMAL_EXACT,
    ETA_OBS,
    S_OVER_NGAMMA_EXACT,
    exact_package,
)
from frontier_dm_leptogenesis_flavor_column_functional_theorem import (
    flavored_column_functional,
    flavored_transport_kernel,
)
from frontier_dm_leptogenesis_pmns_active_projector_reduction import active_packet_from_h
from frontier_dm_leptogenesis_pmns_projector_interface import canonical_h

EVIDENCE_PASS_COUNT = 0
EVIDENCE_FAIL_COUNT = 0
HYGIENE_PASS_COUNT = 0
HYGIENE_FAIL_COUNT = 0
ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md"
NOTE_TEXT = NOTE_PATH.read_text(encoding="utf-8")
NOTE_FLAT = " ".join(NOTE_TEXT.split())

XBAR_NE = 0.5633333333333334
YBAR_NE = 0.30666666666666664
X_SEED = np.full(3, XBAR_NE, dtype=float)
Y_SEED = np.full(3, YBAR_NE, dtype=float)
SUPPLIED_COLUMN_INDEX = 0

PKG = exact_package()
Z_GRID, SOURCE_PROFILE, WASHOUT_TAIL = flavored_transport_kernel(PKG.k_decay_exact)


def evidence_check(name: str, condition: bool, detail: str = "") -> bool:
    """Record a computed numerical or algebraic evidence check."""
    global EVIDENCE_PASS_COUNT, EVIDENCE_FAIL_COUNT
    status = "EVIDENCE PASS" if condition else "EVIDENCE FAIL"
    if condition:
        EVIDENCE_PASS_COUNT += 1
    else:
        EVIDENCE_FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def hygiene_check(name: str, condition: bool, detail: str = "") -> bool:
    """Record a source-scope or documentation-hygiene check."""
    global HYGIENE_PASS_COUNT, HYGIENE_FAIL_COUNT
    status = "HYGIENE PASS" if condition else "HYGIENE FAIL"
    if condition:
        HYGIENE_PASS_COUNT += 1
    else:
        HYGIENE_FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def soft3(u: float, v: float, total: float) -> np.ndarray:
    logits = np.array([u, v, 0.0], dtype=float)
    logits -= np.max(logits)
    weights = np.exp(logits)
    weights /= np.sum(weights)
    return total * weights


def build_active_from_params(params: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    ax, ay, bx, by, delta = np.asarray(params, dtype=float)
    x = soft3(ax, ay, 3.0 * XBAR_NE)
    y = soft3(bx, by, 3.0 * YBAR_NE)
    return x, y, float(delta)


def eta_columns_from_active(x: np.ndarray, y: np.ndarray, delta: float) -> tuple[np.ndarray, np.ndarray]:
    h_e = canonical_h(x, y, delta)
    packet = active_packet_from_h(h_e).T
    etas = np.array(
        [
            S_OVER_NGAMMA_EXACT
            * C_SPH
            * D_THERMAL_EXACT
            * PKG.epsilon_1
            * flavored_column_functional(packet[:, idx], Z_GRID, SOURCE_PROFILE, WASHOUT_TAIL)
            / ETA_OBS
            for idx in range(3)
        ],
        dtype=float,
    )
    return packet, etas


def best_eta_from_params(params: np.ndarray) -> float:
    x, y, delta = build_active_from_params(params)
    _packet, etas = eta_columns_from_active(x, y, delta)
    return float(np.max(etas))


def part0_source_scope_firewall() -> None:
    print("\n" + "=" * 88)
    print("PART 0: SOURCE SCOPE FIREWALL")
    print("=" * 88)

    hygiene_check(
        "Source note identifies the open-gate selector diagnostic",
        "**Type:** open_gate" in NOTE_TEXT
        and "**Type:** bounded_theorem" not in NOTE_TEXT
        and "open selector gate" in NOTE_TEXT
        and "not a selector theorem" in NOTE_FLAT,
    )
    hygiene_check(
        "Source note registers primary runner and cached output",
        "scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py" in NOTE_TEXT
        and "logs/runner-cache/frontier_dm_leptogenesis_pmns_mininfo_source_law.txt" in NOTE_TEXT,
    )
    hygiene_check(
        "Source note does not claim global uniqueness as runner-proved",
        "not a proof of global minimality" in NOTE_FLAT
        and "does not prove that this point is a global minimizer" in NOTE_FLAT,
    )
    hygiene_check(
        "Source note keeps eta_obs equality as an imposed constraint",
        "imposed `eta_{i_*} / eta_obs = 1` constraint" in NOTE_FLAT
        and "imposed `eta_obs` equality" in NOTE_FLAT,
    )
    hygiene_check(
        "Source note does not introduce a new axiom or retained bridge",
        "Lattice, Qubit, Admissibility, and Record" in NOTE_TEXT
        and "No physical closure bridge is cited or load-bearing here" in NOTE_TEXT,
    )
    hygiene_check(
        "Source note forbids retained selector-theorem reuse",
        "must not be cited as a retained" in NOTE_TEXT
        and "No retained-grade promotion" in NOTE_TEXT,
    )


def info_cost(x: np.ndarray, y: np.ndarray, delta: float) -> float:
    px = x / np.sum(x)
    py = y / np.sum(y)
    qx = X_SEED / np.sum(X_SEED)
    qy = Y_SEED / np.sum(Y_SEED)
    kl_x = float(np.sum(px * np.log(px / qx)))
    kl_y = float(np.sum(py * np.log(py / qy)))
    return kl_x + kl_y + (1.0 - math.cos(float(delta)))


def info_cost_from_params(params: np.ndarray) -> float:
    x, y, delta = build_active_from_params(params)
    return info_cost(x, y, delta)


def fmt(v: np.ndarray) -> str:
    return np.array2string(np.round(np.asarray(v, dtype=float), 6), separator=", ")


def part1_finite_seeded_initialization_trace() -> tuple[int, np.ndarray]:
    print("\n" + "=" * 88)
    print("PART 1: FINITE SEEDED INITIALIZATION TRACE (NO EXTREMAL AUTHORITY)")
    print("=" * 88)

    bounds = [
        (-4.0, 4.0),
        (-4.0, 4.0),
        (-4.0, 4.0),
        (-4.0, 4.0),
        (-math.pi, math.pi),
    ]
    result = differential_evolution(
        lambda p: -best_eta_from_params(np.asarray(p, dtype=float)),
        bounds=bounds,
        seed=0,
        maxiter=20,
        popsize=10,
        polish=False,
        disp=False,
    )
    x_opt, y_opt, delta_opt = build_active_from_params(result.x)
    packet_opt, etas_opt = eta_columns_from_active(x_opt, y_opt, delta_opt)
    trace_idx = int(np.argmax(etas_opt))

    evidence_check(
        "The finite seeded search trace stays on the supplied fixed seed surface",
        abs(np.mean(x_opt) - XBAR_NE) < 1e-12 and abs(np.mean(y_opt) - YBAR_NE) < 1e-12,
        f"(xbar,ybar)=({np.mean(x_opt):.6f},{np.mean(y_opt):.6f})",
    )
    evidence_check(
        "The finite trace has its largest sampled readout at the supplied column index 0",
        trace_idx == SUPPLIED_COLUMN_INDEX,
        f"etas={np.round(etas_opt, 6)}",
    )

    print()
    print(f"  search success = {result.success}; iterations = {result.nit}")
    print(f"  search message = {result.message}")
    print("  This bounded seeded search is used only to initialize a local solve.")
    print("  Its termination and sampled ordering do not establish an extremum or column law.")
    print(f"  finite-trace packet:\n{np.round(packet_opt, 6)}")
    print(f"  finite-trace eta/eta_obs = {np.round(etas_opt, 6)}")
    return SUPPLIED_COLUMN_INDEX, result.x


def finite_difference_gradient(function, point: np.ndarray) -> np.ndarray:
    """Independent centered finite-difference gradient for local KKT diagnostics."""
    values = []
    for index, coordinate in enumerate(point):
        step = 1e-5 * max(1.0, abs(float(coordinate)))
        offset = np.zeros_like(point, dtype=float)
        offset[index] = step
        values.append((function(point + offset) - function(point - offset)) / (2.0 * step))
    return np.asarray(values, dtype=float)


def part2_local_information_candidate(
    i_star: int, initialization_params: np.ndarray
) -> tuple[np.ndarray, np.ndarray, float, np.ndarray, np.ndarray]:
    print("\n" + "=" * 88)
    print("PART 2: FEASIBLE LOCALLY STATIONARY INFORMATION-COST CANDIDATE")
    print("=" * 88)

    def eta_i(params: np.ndarray) -> float:
        x, y, delta = build_active_from_params(params)
        _packet, etas = eta_columns_from_active(x, y, delta)
        return float(etas[i_star])

    def line_profile(t: float) -> np.ndarray:
        return np.asarray(initialization_params, dtype=float) * t

    t_root = brentq(lambda t: eta_i(line_profile(t)) - 1.0, 0.0, 1.0)
    start = line_profile(t_root)

    result = minimize(
        info_cost_from_params,
        start,
        method="SLSQP",
        bounds=[
            (-6.0, 6.0),
            (-6.0, 6.0),
            (-6.0, 6.0),
            (-6.0, 6.0),
            (-math.pi, math.pi),
        ],
        constraints=[{"type": "eq", "fun": lambda p: eta_i(np.asarray(p, dtype=float)) - 1.0}],
        options={"ftol": 1e-12, "maxiter": 500},
    )

    x_min, y_min, delta_min = build_active_from_params(result.x)
    packet_min, etas_min = eta_columns_from_active(x_min, y_min, delta_min)
    xi = x_min - X_SEED
    eta = y_min - Y_SEED
    best_idx = int(np.argmax(etas_min))

    evidence_check(
        "The local solver reports successful termination",
        bool(result.success),
        f"status={result.status}, iterations={result.nit}, message={result.message}",
    )
    evidence_check(
        "The local candidate stays on the supplied fixed seed surface",
        abs(np.mean(x_min) - XBAR_NE) < 1e-12 and abs(np.mean(y_min) - YBAR_NE) < 1e-12,
        f"(xbar,ybar)=({np.mean(x_min):.6f},{np.mean(y_min):.6f})",
    )
    evidence_check(
        "The imposed equality is satisfied at the supplied column index",
        abs(etas_min[i_star] - 1.0) < 1e-12,
        f"etas={np.round(etas_min, 12)}",
    )
    evidence_check(
        "The candidate has a finite positive information-deformation cost",
        math.isfinite(info_cost(x_min, y_min, delta_min)) and info_cost(x_min, y_min, delta_min) > 0.0,
        f"I_seed={info_cost(x_min, y_min, delta_min):.12f}",
    )
    evidence_check(
        "The local candidate has a numerically near-zero phase",
        abs(delta_min) < 1e-6,
        f"delta={delta_min:.12e}",
    )
    evidence_check(
        "The local candidate is genuinely off the supplied seed",
        np.linalg.norm(xi) > 1e-6 and np.linalg.norm(eta) > 1e-6,
        f"xi={fmt(xi)}, eta={fmt(eta)}",
    )
    evidence_check(
        "The supplied column is also the largest finite readout at this candidate",
        best_idx == i_star,
        f"best idx={best_idx}, etas={np.round(etas_min, 6)}",
    )

    objective_gradient = finite_difference_gradient(info_cost_from_params, result.x)
    constraint_gradient = finite_difference_gradient(
        lambda params: eta_i(np.asarray(params, dtype=float)) - 1.0,
        result.x,
    )
    constraint_norm_sq = float(np.dot(constraint_gradient, constraint_gradient))
    lambda_local = float(np.dot(objective_gradient, constraint_gradient) / constraint_norm_sq)
    kkt_residual = objective_gradient - lambda_local * constraint_gradient
    bound_margin = min(
        *(float(result.x[index]) + 6.0 for index in range(4)),
        *(6.0 - float(result.x[index]) for index in range(4)),
        float(result.x[4]) + math.pi,
        math.pi - float(result.x[4]),
    )
    evidence_check(
        "The equality-constraint gradient is nonzero at the local candidate",
        constraint_norm_sq > 1e-8,
        f"||grad C||={math.sqrt(constraint_norm_sq):.6e}",
    )
    evidence_check(
        "The local candidate is interior to the imposed parameter bounds",
        bound_margin > 1e-6,
        f"minimum bound margin={bound_margin:.6e}",
    )
    evidence_check(
        "An independent finite-difference KKT residual is small",
        float(np.linalg.norm(kkt_residual, ord=np.inf)) < 1e-5,
        f"lambda={lambda_local:.9f}, ||grad J-lambda grad C||_inf={np.linalg.norm(kkt_residual, ord=np.inf):.3e}",
    )

    print()
    print(f"  x_min     = {fmt(x_min)}")
    print(f"  y_min     = {fmt(y_min)}")
    print(f"  xi_min    = {fmt(xi)}")
    print(f"  eta_min   = {fmt(eta)}")
    print(f"  delta_min = {delta_min:.12e}")
    print(f"  I_seed    = {info_cost(x_min, y_min, delta_min):.12f}")
    print(f"  packet_min:\n{np.round(packet_min, 6)}")
    print(f"  eta/eta_obs(min-law) = {np.round(etas_min, 12)}")

    return x_min, y_min, delta_min, packet_min, etas_min


def part3_bottom_line() -> None:
    print("\n" + "=" * 88)
    print("PART 3: BOTTOM LINE (conditional)")
    print("=" * 88)

    print("  Computed evidence above establishes one feasible interior local KKT candidate.")
    print("  It does not establish global minimality, uniqueness, or a physical column selector.")


def main() -> int:
    print("=" * 88)
    print("DM LEPTOGENESIS PMNS MINIMUM-INFORMATION SELECTOR DIAGNOSTIC (open gate / conditional)")
    print("=" * 88)
    print()
    print("Framework baseline:")
    print("  Lattice + Qubit + Admissibility + Record; one-qubit algebra on Z^3.")
    print()
    print("Scope (open gate / conditional diagnostic):")
    print("  IF the minimum-information selector law is adopted as a downstream")
    print("  definition on the fixed supplied seed surface with supplied i_*=0,")
    print("  THEN the runner finds a feasible locally stationary off-seed candidate")
    print("  after imposing eta_{i_*}/eta_obs = 1.")
    print()
    print("Adopted definition:")
    print("  Seek local off-seed candidates for")
    print("    I_seed = D_KL(x/sum(x)||x_seed/sum(x_seed))")
    print("           + D_KL(y/sum(y)||y_seed/sum(y_seed)) + (1-cos delta)")
    print("  subject to eta_{i_*}/eta_obs = 1 at the supplied index i_*=0.")
    print()
    print("NOT claimed:")
    print("  - that I_seed itself follows from the current four-axiom baseline")
    print("  - that I_seed is the unique correct selector")
    print("  - global uniqueness/minimality of the local-solver candidate")
    print("  - baseline-framework closure of the PMNS-assisted N_e branch")

    part0_source_scope_firewall()
    i_star, initialization_params = part1_finite_seeded_initialization_trace()
    part2_local_information_candidate(
        i_star, initialization_params
    )
    part3_bottom_line()

    print("\n" + "=" * 88)
    print("RESULT (conditional)")
    print("=" * 88)
    print("  Adopted downstream selector law (definition, not derivation):")
    print("    - supplied finite-fixture column index i_*=0")
    print("    - one feasible interior local KKT candidate")
    print("    - numerical eta/eta_obs = 1 on the supplied matrix/transport fixture")
    print("    - conditional on adopting I_seed, all helper inputs, and the constraint")
    print()
    print(f"EVIDENCE: PASS={EVIDENCE_PASS_COUNT} FAIL={EVIDENCE_FAIL_COUNT}")
    print(f"HYGIENE/SUPPORT: PASS={HYGIENE_PASS_COUNT} FAIL={HYGIENE_FAIL_COUNT}")
    return 1 if EVIDENCE_FAIL_COUNT or HYGIENE_FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
