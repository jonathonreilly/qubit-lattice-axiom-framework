#!/usr/bin/env python3
"""Finite numerical comparison on supplied relative-action/recovered packets.
No physical selector, exact uniqueness, all-shift or DM closure is established.
The relative-action source uses an imposed observed-target equality and local
optimization. Checks below compare finite fixtures and sampled shifts only.
"""

from __future__ import annotations

import sys

import numpy as np

from dm_selector_branch_support import SHIFT_OFFSETS, recovered_bank
from frontier_dm_leptogenesis_pmns_observable_relative_action_law import H_SEED
from frontier_dm_selector_shifted_doublet_imag_sign_support_2026_04_21 import (
    imag12_from_h,
)


AUDIT_TIMEOUT_SEC = 300

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






def unique_argmin(values: np.ndarray) -> tuple[int, float]:
    vals = np.asarray(values, dtype=float)
    order = np.argsort(vals)
    return int(order[0]), float(vals[order[1]] - vals[order[0]])


def shifted_relative_action_to_seed(h: np.ndarray, mu: float) -> float:
    a_seed = np.asarray(H_SEED, dtype=complex) + float(mu) * np.eye(3, dtype=complex)
    a = np.asarray(h, dtype=complex) + float(mu) * np.eye(3, dtype=complex)
    m = np.linalg.inv(a_seed) @ a
    sign, logdet = np.linalg.slogdet(m)
    if abs(sign) < 1.0e-12:
        raise ValueError("shifted relative-action matrix left the positive branch")
    return float(np.real(np.trace(m) - logdet - 3.0))


def dense_shift_grid(mu_floor: float) -> np.ndarray:
    return np.concatenate(
        [
            np.linspace(mu_floor + 1.0e-6, mu_floor + 0.1, 20),
            np.linspace(mu_floor + 0.1, mu_floor + 2.0, 20),
            np.linspace(mu_floor + 2.0, mu_floor + 20.0, 20),
        ]
    )


def main() -> int:
    print("=" * 88)
    print("DM SHIFTED-RELATIVE-ACTION FINITE RECOVERED-PACKET COMPARISON")
    print("=" * 88)


    _lifts, hs_bank, repairs_bank, _targets = recovered_bank()
    mu_floor = float(np.max(repairs_bank))
    imag_bank = np.array([imag12_from_h(h) for h in hs_bank], dtype=float)
    tested_shifts = list(mu_floor + np.asarray(SHIFT_OFFSETS, dtype=float)) + list(dense_shift_grid(mu_floor)) + [mu_floor + 1.0e6]
    check("All compared seed/bank matrices are positive definite at every tested shift",
          all(np.min(np.linalg.eigvalsh(np.asarray(h, dtype=complex) + mu*np.eye(3))) > 0
              for mu in tested_shifts for h in [H_SEED, *hs_bank]))

    print("\n" + "=" * 88)
    print("PART 1: THE SAME EXACT SCALAR LAW EXTENDS TO THE COMMON POSITIVE WINDOWS")
    print("=" * 88)

    check(
        "One common positivity threshold mu_floor exists on the recovered bank",
        mu_floor > 0.0,
        f"mu_floor = {mu_floor:.15f}",
    )

    print("\n" + "=" * 88)
    print("PART 2: EVERY TESTED COMMON POSITIVE SHIFT PICKS THE SAME PREFERRED LIFT")
    print("=" * 88)

    tested = []
    for offset in SHIFT_OFFSETS:
        mu = mu_floor + float(offset)
        vals = np.array([shifted_relative_action_to_seed(h, mu) for h in hs_bank], dtype=float)
        idx, margin = unique_argmin(vals)
        tested.append((mu, idx, margin))

    tested_ok = all(idx == 0 and margin > 1.0e-9 for _mu, idx, margin in tested)
    tested_margin = min(margin for _mu, _idx, margin in tested)
    check(
        "Across the full tested shift family, the shifted relative action uniquely minimizes at recovered lift 0",
        tested_ok,
        f"worst tested margin = {tested_margin:.12f}",
    )
    check(
        "At the first tested shift above positivity, lift 0 is already unique",
        tested[0][1] == 0 and tested[0][2] > 1.0e-9,
        f"(mu, margin)=({tested[0][0]:.15f}, {tested[0][2]:.12f})",
    )
    check(
        "At the largest tested shift, lift 0 is still unique",
        tested[-1][1] == 0 and tested[-1][2] > 1.0e-9,
        f"(mu, margin)=({tested[-1][0]:.15f}, {tested[-1][2]:.12f})",
    )

    print("\n" + "=" * 88)
    print("PART 3: THE SAME MINIMIZER PERSISTS ON A DENSE ADMISSIBLE STRESS RANGE")
    print("=" * 88)

    worst_mu = None
    worst_margin = float("inf")
    dense_ok = True
    for mu in dense_shift_grid(mu_floor):
        vals = np.array([shifted_relative_action_to_seed(h, float(mu)) for h in hs_bank], dtype=float)
        idx, margin = unique_argmin(vals)
        if idx != 0 or margin <= 1.0e-9:
            dense_ok = False
        if margin < worst_margin:
            worst_mu = float(mu)
            worst_margin = float(margin)

    check(
        "On the dense admissible stress range from the positivity edge to large shifts, the same unique minimizer persists",
        dense_ok,
        f"worst dense margin = {worst_margin:.12f} at mu = {worst_mu:.15f}",
    )
    large_mu = mu_floor + 1.0e6
    large_vals = np.array([shifted_relative_action_to_seed(h, large_mu) for h in hs_bank], dtype=float)
    large_idx, large_margin = unique_argmin(large_vals)
    check(
        "At the single tested large shift, lift 0 has the smallest computed value",
        large_idx == 0 and large_margin > 1.0e-18,
        f"(large_mu, margin)=({large_mu:.1f}, {large_margin:.12e})",
    )

    print("\n" + "=" * 88)
    print("PART 4: THE SAME EXACT SCALAR LAW ACTIVATES THE POSITIVE ODD DOUBLET SIDE")
    print("=" * 88)

    positive_idx = np.where(imag_bank > 0.0)[0]
    check(
        "Exactly one recovered lift has positive shifted-imaginary doublet mixing",
        len(positive_idx) == 1 and int(positive_idx[0]) == 0,
        f"Im(K12)_bank = {np.round(imag_bank, 12)}",
    )
    check(
        "So the same shifted relative-action law and the odd doublet-sign packet select the same preferred lift",
        tested_ok and dense_ok and len(positive_idx) == 1 and int(positive_idx[0]) == 0,
        "same recovered lift 0",
    )

    print("\n" + "=" * 88)
    print("PART 5: SCIENTIFIC CONSEQUENCE")
    print("=" * 88)

    check(
        "The sampled shifted-action and sign comparisons agree on recovered lift zero",
        tested_ok and dense_ok and len(positive_idx) == 1 and int(positive_idx[0]) == 0,
        "finite numerical agreement only",
    )

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  The sampled shifted-action comparisons select the same finite-bank index.")
    print("  Physical minimization, all-shift persistence and DM closure remain open.")
    print("[SCOPE] Supplied finite numerical comparisons; physical selection remains open.")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
