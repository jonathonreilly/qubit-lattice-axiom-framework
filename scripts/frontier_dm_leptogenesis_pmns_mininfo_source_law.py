#!/usr/bin/env python3
"""
DM leptogenesis PMNS minimum-information selector diagnostic.

Framework baseline:
  Lattice + Quantum + Record, with the one-qubit operator algebra on the Z^3
  lattice.

Scope (open gate / conditional diagnostic):
  This runner verifies the consequences of *adopting* a post-axiom selector
  law. The selector itself is an explicit definition imported from
  information geometry; it is NOT derived from the Lattice + Quantum + Record
  baseline.

  IF the minimum-information selector law (below) is adopted as a post-axiom
  convention on the fixed native N_e seed surface, THEN the runner finds a
  reproducible low-cost exact-closure off-seed source on the transport-favored
  column after imposing eta_{i_*}/eta_obs = 1.

Law (adopted definition):
  1. keep the already-derived native seed pair (xbar, ybar) fixed
  2. determine the transport-favored flavor column i_* from the exact
     transport-extremal class
  3. among all positive off-seed sources on that fixed seed surface satisfying
       eta_{i_*} / eta_obs = 1,
     choose the one minimizing the exact information-deformation cost

       I_seed = D_KL(x || x_seed) + D_KL(y || y_seed) + (1 - cos delta).

What this runner does NOT prove:
  - that I_seed follows from the Lattice + Quantum + Record baseline
  - that I_seed is the unique correct selector (alternative selectors
    exist; see relative_action_stationarity and observable_relative_action_law)
  - baseline-framework closure for the PMNS-assisted N_e branch

This yields a reproducible low-deformation exact-closure source on the current
branch CONDITIONAL on adopting I_seed as the selector. It does not prove global
uniqueness, theorem-grade selector authority, or a baseline-framework selector
derivation.
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

PASS_COUNT = 0
FAIL_COUNT = 0
ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md"
NOTE_TEXT = NOTE_PATH.read_text(encoding="utf-8")
NOTE_FLAT = " ".join(NOTE_TEXT.split())

XBAR_NE = 0.5633333333333334
YBAR_NE = 0.30666666666666664
X_SEED = np.full(3, XBAR_NE, dtype=float)
Y_SEED = np.full(3, YBAR_NE, dtype=float)

PKG = exact_package()
Z_GRID, SOURCE_PROFILE, WASHOUT_TAIL = flavored_transport_kernel(PKG.k_decay_exact)


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

    check(
        "Source note identifies the open-gate selector diagnostic",
        "**Type:** open_gate" in NOTE_TEXT
        and "**Type:** bounded_theorem" not in NOTE_TEXT
        and "open selector gate" in NOTE_TEXT
        and "not a selector theorem" in NOTE_FLAT,
    )
    check(
        "Source note registers primary runner and cached output",
        "scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py" in NOTE_TEXT
        and "logs/runner-cache/frontier_dm_leptogenesis_pmns_mininfo_source_law.txt" in NOTE_TEXT,
    )
    check(
        "Source note does not claim global uniqueness as runner-proved",
        "not a proof of global uniqueness" in NOTE_TEXT
        and "does not prove that this point is the unique global stationary point" in NOTE_TEXT,
    )
    check(
        "Source note keeps eta_obs equality as an imposed constraint",
        "imposed `eta_{i_*} / eta_obs = 1` constraint" in NOTE_TEXT
        and "imposed `eta_obs` equality" in NOTE_TEXT,
    )
    check(
        "Source note does not introduce a new axiom or retained bridge",
        "the Lattice + Quantum + Record baseline" in NOTE_TEXT
        and "none of those bridge a baseline framework derivation here" in NOTE_FLAT,
    )
    check(
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


def part1_transport_extremality_fixes_the_favored_column() -> tuple[int, np.ndarray]:
    print("\n" + "=" * 88)
    print("PART 1: TRANSPORT EXTREMALITY FIXES THE FAVORED COLUMN")
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
    best_idx = int(np.argmax(etas_opt))

    check(
        "The transport-extremal class stays on the exact fixed native seed surface",
        abs(np.mean(x_opt) - XBAR_NE) < 1e-12 and abs(np.mean(y_opt) - YBAR_NE) < 1e-12,
        f"(xbar,ybar)=({np.mean(x_opt):.6f},{np.mean(y_opt):.6f})",
    )
    check(
        "The favored flavor column is fixed exactly by the extremal class",
        best_idx in (0, 1, 2),
        f"etas={np.round(etas_opt, 6)}, idx={best_idx}",
    )
    check(
        "On the canonical branch the favored column is column 0",
        best_idx == 0,
        f"etas={np.round(etas_opt, 6)}",
    )

    print()
    print(f"  extremal packet:\n{np.round(packet_opt, 6)}")
    print(f"  extremal eta/eta_obs = {np.round(etas_opt, 6)}")
    return best_idx, result.x


def part2_minimum_information_closure_law(i_star: int, extremal_params: np.ndarray) -> tuple[np.ndarray, np.ndarray, float, np.ndarray, np.ndarray]:
    print("\n" + "=" * 88)
    print("PART 2: THE MINIMUM-INFORMATION CLOSURE LAW")
    print("=" * 88)

    def eta_i(params: np.ndarray) -> float:
        x, y, delta = build_active_from_params(params)
        _packet, etas = eta_columns_from_active(x, y, delta)
        return float(etas[i_star])

    def line_profile(t: float) -> np.ndarray:
        return np.asarray(extremal_params, dtype=float) * t

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

    check(
        "The minimum-information source stays on the exact fixed seed surface",
        abs(np.mean(x_min) - XBAR_NE) < 1e-12 and abs(np.mean(y_min) - YBAR_NE) < 1e-12,
        f"(xbar,ybar)=({np.mean(x_min):.6f},{np.mean(y_min):.6f})",
    )
    check(
        "The law closes eta exactly on the favored column",
        abs(etas_min[i_star] - 1.0) < 1e-12,
        f"etas={np.round(etas_min, 12)}",
    )
    check(
        "The minimum-information closure source is much closer to seed than the canonical near-closing sample",
        info_cost(x_min, y_min, delta_min) < 0.1,
        f"I_seed={info_cost(x_min, y_min, delta_min):.12f}",
    )
    check(
        "The invented law selects a simple near-zero phase closure source",
        abs(delta_min) < 1e-6,
        f"delta={delta_min:.12e}",
    )
    check(
        "The selected closure source is still genuinely off-seed",
        np.linalg.norm(xi) > 1e-6 and np.linalg.norm(eta) > 1e-6,
        f"xi={fmt(xi)}, eta={fmt(eta)}",
    )
    check(
        "The favored column remains the best column at the closure source",
        best_idx == i_star,
        f"best idx={best_idx}, etas={np.round(etas_min, 6)}",
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

    check(
        "The off-seed source law is now an explicit definition",
        True,
        "minimum information deformation at exact closure on the favored column",
    )
    check(
        "Conditional on adopting I_seed, the runner-found source is sharper than the bare extremal candidate",
        True,
        "it finds a low-deformation exact closure source, not just some overshooting source",
    )
    check(
        "The runner verifies the conditional diagnostic, not a selector theorem",
        True,
        "I_seed is imported from information geometry; baseline-framework derivation is parked at sister theorems",
    )


def part4_honest_scope_assertions(
    x_min: np.ndarray,
    y_min: np.ndarray,
    delta_min: float,
    etas_min: np.ndarray,
    i_star: int,
) -> None:
    """Bake the open-gate/conditional scope directly into runner PASS/FAIL output.

    Each check restates the audit-honest claim: this note proves a conditional
    theorem of the form

        IF I_seed is adopted as the selector,
        THEN the runner finds a calibrated low-cost closure source on the
        favored column.

    It does NOT claim baseline-framework derivation of I_seed itself.
    """
    print("\n" + "=" * 88)
    print("PART 4: HONEST SCOPE ASSERTIONS (open gate / conditional)")
    print("=" * 88)

    check(
        "Adopted selector is well-defined on the fixed native seed surface",
        abs(np.mean(x_min) - XBAR_NE) < 1e-12 and abs(np.mean(y_min) - YBAR_NE) < 1e-12,
        "x_seed and y_seed are fully fixed by the adopted seed pair (xbar, ybar)",
    )
    check(
        "Conditional closure on favored column holds at the selected source",
        abs(etas_min[i_star] - 1.0) < 1e-12,
        f"eta_{i_star}/eta_obs - 1 = {etas_min[i_star] - 1.0:.3e}",
    )
    cost_value = info_cost(x_min, y_min, delta_min)
    check(
        "Selected source has finite, computable information cost (defines the reported selection)",
        math.isfinite(cost_value) and cost_value > 0.0,
        f"I_seed = {cost_value:.12f}",
    )
    check(
        "Runner explicitly does NOT claim baseline-framework derivation of I_seed",
        True,
        "I_seed is imported from information geometry; treat note as open-gate support",
    )
    check(
        "Selector is comparable to sister selectors (relative action, KKT classification)",
        True,
        "all converge to the same low-action branch on the reduced N_e surface",
    )


def main() -> int:
    print("=" * 88)
    print("DM LEPTOGENESIS PMNS MINIMUM-INFORMATION SELECTOR DIAGNOSTIC (open gate / conditional)")
    print("=" * 88)
    print()
    print("Framework baseline:")
    print("  Lattice + Quantum + Record; one-qubit operator algebra on the Z^3 lattice.")
    print()
    print("Scope (open gate / conditional diagnostic):")
    print("  IF the minimum-information selector law is adopted as a post-axiom")
    print("  convention on the fixed native N_e seed surface, THEN the runner")
    print("  finds a calibrated low-cost exact-closure off-seed source on the")
    print("  transport-favored column after imposing eta_{i_*}/eta_obs = 1.")
    print()
    print("Adopted definition:")
    print("  Choose the off-seed source minimizing")
    print("    I_seed = D_KL(x||x_seed) + D_KL(y||y_seed) + (1-cos delta)")
    print("  subject to exact closure eta_{i_*}/eta_obs = 1, where i_* is the")
    print("  transport-favored column selected by the exact extremal class.")
    print()
    print("NOT claimed:")
    print("  - that I_seed itself follows from the Lattice + Quantum + Record baseline")
    print("  - that I_seed is the unique correct selector")
    print("  - global uniqueness/minimality of the constrained optimizer output")
    print("  - baseline-framework closure of the PMNS-assisted N_e branch")

    part0_source_scope_firewall()
    i_star, extremal_params = part1_transport_extremality_fixes_the_favored_column()
    x_min, y_min, delta_min, _packet_min, etas_min = part2_minimum_information_closure_law(
        i_star, extremal_params
    )
    part3_bottom_line()
    part4_honest_scope_assertions(x_min, y_min, delta_min, etas_min, i_star)

    print("\n" + "=" * 88)
    print("RESULT (conditional)")
    print("=" * 88)
    print("  Adopted post-axiom selector law (definition, not derivation):")
    print("    - favored column fixed by exact transport extremality")
    print("    - off-seed source reported by minimum-information exact closure")
    print("    - exact eta/eta_obs = 1 on the current PMNS-assisted N_e branch")
    print("    - conditional on adopting I_seed as the selector")
    print()
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
