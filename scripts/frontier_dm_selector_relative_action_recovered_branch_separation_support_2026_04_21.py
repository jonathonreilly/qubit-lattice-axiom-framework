#!/usr/bin/env python3
"""
DM selector relative-action / recovered-branch separation support theorem.

Question:
  Does the supplied relative-action candidate on the fixed N_e seed
  parameterization coincide with the recovered selector branch and its
  canonical threshold candidate?

Answer:
  No.

  The conditional calculator returns an eta/eta_obs = 1 source on the supplied
  seed parameterization, but that source:

  - does not coincide with any recovered-bank point,
  - does not coincide with any recovered active target,
  - is not selected by the recovered-bank canonical breakpoint tau_b,min,
  - and instead carries its own later intrinsic breakpoint tau_b,rel.

  So the remaining selector burden is sharper than “derive minimal relative
  action.” A future theorem must derive and bridge that candidate
  to the recovered right-sensitive selector branch, or replace it with a finer
  microscopic law.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, differential_evolution, minimize

from dm_selector_branch_support import ANCHOR_OFFSET, common_shift, recovered_bank
from frontier_dm_leptogenesis_pmns_observable_relative_action_law import (
    XBAR_NE,
    YBAR_NE,
    best_eta_from_params,
    build_active_from_params,
    eta_columns_from_active,
    relative_action_from_params,
)
from frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem import (
    active_target_from_h,
)
from frontier_dm_neutrino_source_surface_atomic_witness_volume_selector_nonrealization import (
    inverse_eigenvalue_parameters,
    witness_volume_from_atomic_field,
)

ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0


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


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def observable_relative_action_selection() -> tuple[int, np.ndarray, np.ndarray, float, np.ndarray, np.ndarray]:
    extremal = differential_evolution(
        lambda p: -best_eta_from_params(np.asarray(p, dtype=float)),
        bounds=[
            (-4.0, 4.0),
            (-4.0, 4.0),
            (-4.0, 4.0),
            (-4.0, 4.0),
            (-math.pi, math.pi),
        ],
        seed=0,
        maxiter=20,
        popsize=10,
        polish=False,
        disp=False,
    )
    x_opt, y_opt, delta_opt = build_active_from_params(extremal.x)
    _h_opt, _packet_opt, etas_opt = eta_columns_from_active(x_opt, y_opt, delta_opt)
    i_star = int(np.argmax(etas_opt))

    def eta_i(params: np.ndarray) -> float:
        x, y, delta = build_active_from_params(params)
        _h, _packet, etas = eta_columns_from_active(x, y, delta)
        return float(etas[i_star])

    def line_profile(t: float) -> np.ndarray:
        return np.asarray(extremal.x, dtype=float) * t

    t_root = brentq(lambda t: eta_i(line_profile(t)) - 1.0, 0.0, 1.0)
    start = line_profile(t_root)

    result = minimize(
        relative_action_from_params,
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
        options={"ftol": 1.0e-12, "maxiter": 500},
    )

    x_sel, y_sel, delta_sel = build_active_from_params(result.x)
    h_sel, _packet_sel, etas_sel = eta_columns_from_active(x_sel, y_sel, delta_sel)
    return i_star, x_sel, y_sel, float(delta_sel), np.asarray(h_sel, dtype=complex), np.asarray(etas_sel, dtype=float)


def main() -> int:
    print("=" * 88)
    print("DM SELECTOR RELATIVE-ACTION / RECOVERED-BRANCH SEPARATION SUPPORT THEOREM")
    print("=" * 88)

    rel_note = read("docs/DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_CONDITIONAL_CALCULATOR_NOTE_2026-07-12.md")
    own_note = read("docs/DM_SELECTOR_RELATIVE_ACTION_RECOVERED_BRANCH_SEPARATION_SUPPORT_THEOREM_NOTE_2026-04-21.md")
    thresh_note = read("docs/DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_NOTE_2026-04-21.md")

    i_star, x_sel, y_sel, delta_sel, h_sel, etas_sel = observable_relative_action_selection()
    _lifts, hs_bank, repairs_bank, targets = recovered_bank()
    mu_bank = common_shift(repairs_bank, ANCHOR_OFFSET)

    target_sel = np.asarray(active_target_from_h(h_sel), dtype=float)
    target_bank = [np.asarray(t, dtype=float) for t in targets]
    h_distances = np.array([np.linalg.norm(h_sel - np.asarray(h, dtype=complex)) for h in hs_bank], dtype=float)
    target_distances = np.array([np.linalg.norm(target_sel - t) for t in target_bank], dtype=float)

    params_bank = [inverse_eigenvalue_parameters(h, mu_bank) for h in hs_bank]
    params_sel = inverse_eigenvalue_parameters(h_sel, mu_bank)
    tau_b_bank = np.array([math.log1p(p[1]) for p in params_bank], dtype=float)
    tau_b_min = float(np.min(tau_b_bank))
    tau_b_sel = float(math.log1p(params_sel[1]))

    v_sel_low = float(witness_volume_from_atomic_field(params_sel, 0.13))
    v_sel_high = float(witness_volume_from_atomic_field(params_sel, 0.14))
    vals_bmin = np.array([witness_volume_from_atomic_field(p, tau_b_min) for p in params_bank], dtype=float)
    v_sel_bmin = float(witness_volume_from_atomic_field(params_sel, tau_b_min))
    vals_bsel = np.array([witness_volume_from_atomic_field(p, tau_b_sel) for p in params_bank], dtype=float)
    v_sel_bsel = float(witness_volume_from_atomic_field(params_sel, tau_b_sel))

    print("\n" + "=" * 88)
    print("PART 1: THE RELATIVE-ACTION SOURCE IS A SUPPLIED SELECTOR CANDIDATE")
    print("=" * 88)

    check(
        "The conditional note records the objective as supplied rather than physically derived",
        "supplied law" in rel_note and "not a framework derivation" in rel_note,
    )
    check(
        "The reconstructed source stays on the supplied fixed seed parameterization",
        abs(np.mean(x_sel) - XBAR_NE) < 1.0e-12 and abs(np.mean(y_sel) - YBAR_NE) < 1.0e-12,
        f"(xbar,ybar)=({np.mean(x_sel):.6f},{np.mean(y_sel):.6f})",
    )
    check(
        "The reconstructed source still closes the favored transport column exactly",
        i_star == 0 and abs(etas_sel[0] - 1.0) < 1.0e-12,
        f"delta={delta_sel:.12e}, etas={np.round(etas_sel, 12)}",
    )

    print("\n" + "=" * 88)
    print("PART 2: THE RELATIVE-ACTION SOURCE STAYS OFF THE RECOVERED SELECTOR BRANCH")
    print("=" * 88)

    check(
        "No recovered-bank Hermitian source coincides with the relative-action source",
        float(np.min(h_distances)) > 1.0e-6,
        f"min Frobenius distance = {float(np.min(h_distances)):.12f}",
    )
    check(
        "No recovered active target coincides with the relative-action target",
        float(np.min(target_distances)) > 1.0e-6,
        f"min target distance = {float(np.min(target_distances)):.12f}",
    )
    check(
        "The nearest recovered point is the preferred lift, but the gap is still macroscopically nonzero on the checked scale",
        int(np.argmin(h_distances)) == 0 and float(np.min(h_distances)) > 1.0,
        f"nearest recovered index = {int(np.argmin(h_distances))}",
    )

    print("\n" + "=" * 88)
    print("PART 3: THE RELATIVE-ACTION SOURCE DOES NOT REALIZE THE RECOVERED THRESHOLD CANDIDATE")
    print("=" * 88)

    check(
        "The earlier threshold note still records the recovered-bank canonical breakpoint tau_b,min",
        "tau_b,min" in thresh_note
        and ("earliest middle-branch" in thresh_note or "canonical breakpoint candidate" in thresh_note),
    )
    check(
        "The relative-action source has its own later middle-branch breakpoint",
        tau_b_sel > tau_b_min,
        f"(tau_b_sel, tau_b_min)=({tau_b_sel:.15f}, {tau_b_min:.15f})",
    )
    check(
        "At tau = 0.13 and tau = 0.14 the relative-action source is still on the full-volume shoulder of the witness family",
        abs(v_sel_low - 1.0) < 1.0e-12 and abs(v_sel_high - 1.0) < 1.0e-12,
        f"(V_0.13, V_0.14)=({v_sel_low:.12f}, {v_sel_high:.12f})",
    )
    check(
        "At the recovered-bank canonical breakpoint tau_b,min, the preferred recovered lift still beats the relative-action source",
        vals_bmin[0] + 1.0e-12 < v_sel_bmin,
        f"(V_pref, V_rel)=({vals_bmin[0]:.12f}, {v_sel_bmin:.12f})",
    )
    check(
        "At its own breakpoint tau_b,rel, the relative-action source becomes strictly smaller than every recovered-bank competitor",
        v_sel_bsel + 1.0e-12 < float(np.min(vals_bsel)),
        f"(V_rel, min_bank)=({v_sel_bsel:.12f}, {float(np.min(vals_bsel)):.12f})",
    )

    print("\n" + "=" * 88)
    print("PART 4: SCIENTIFIC CONSEQUENCE")
    print("=" * 88)

    check(
        "The support note leaves the physical bridge open",
        "derive and bridge the supplied observable-relative-action candidate" in own_note
        and "support theorem, not closure" in own_note.lower(),
    )
    check(
        "The relative-action and recovered-bank candidates are distinct on the checked packet",
        float(np.min(h_distances)) > 1.0e-3 and float(np.min(target_distances)) > 1.0e-3,
        "conditional support narrowing only",
    )

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  The supplied relative-action candidate does not")
    print("  collapse to the recovered selector branch.")
    print("  Its exact source stays off the recovered bank, carries its own later")
    print("  intrinsic breakpoint, and is not selected by the recovered-bank")
    print("  canonical breakpoint tau_b,min.")
    print("  So the remaining microscopic selector burden is now sharper:")
    print("    derive and bridge the supplied candidate to the recovered")
    print("    right-sensitive selector branch, or replace it with a finer law.")
    print()
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")

    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
